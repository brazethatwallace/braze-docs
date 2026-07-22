#!/usr/bin/env python3
"""
Tests for auto-translate API retry and chunked-routing helpers.

Run with:
    python3 -m pytest scripts/test_auto_translate_resilience.py -v
"""

import auto_translate as at


class TestRetryableApiErrors:
    def test_internal_server_error_is_retryable(self):
        assert at._is_retryable_api_error("Internal server error")

    def test_api_error_payload_is_retryable(self):
        err = "{'type': 'error', 'error': {'type': 'api_error', 'message': 'Internal server error'}}"
        assert at._is_retryable_api_error(err)

    def test_non_transient_error_is_not_retryable(self):
        assert not at._is_retryable_api_error("YAML front matter parse error")


class TestRetryableTranslationErrors:
    def test_liquid_paired_tag_imbalance_is_retryable(self):
        err = (
            "Liquid paired-tag imbalance in "
            "_lang/fr_fr/_user_guide/data/distribution/braze_currents/"
            "event_glossary/message_engagement_events.md: api=81 endapi=80"
        )
        assert at._is_retryable_translation_error(err)

    def test_api_errors_remain_retryable(self):
        assert at._is_retryable_translation_error("Internal server error")

    def test_non_transient_translation_error_is_not_retryable(self):
        assert not at._is_retryable_translation_error(
            "YAML front matter parse error"
        )


class TestMaxTokensChunkedFallback:
    def test_max_tokens_truncation_error_is_detected(self):
        exc = at.MaxTokensTruncatedError(
            "Output truncated (hit 128000 token limit). "
            "Increase TRANSLATION_MAX_TOKENS or use chunked translation."
        )
        assert at._is_max_tokens_truncation_error(exc)

    def test_translate_one_falls_back_to_chunked_on_max_tokens(self, monkeypatch):
        calls = {"chunked": 0, "translate_file": 0}

        def fake_translate_file(*_args, **_kwargs):
            calls["translate_file"] += 1
            raise at.MaxTokensTruncatedError(
                "Output truncated (hit 128000 token limit). "
                "Increase TRANSLATION_MAX_TOKENS or use chunked translation."
            )

        def fake_translate_one_chunked(*_args, **_kwargs):
            calls["chunked"] += 1
            return {
                "ok": True,
                "source": "_docs/_developer_guide/content_cards.md",
                "target": "_lang/ja/_developer_guide/content_cards.md",
                "lang": "ja",
                "chunked": True,
                "chunks": 2,
            }

        monkeypatch.setattr(at, "translate_file", fake_translate_file)
        monkeypatch.setattr(at, "translate_one_chunked", fake_translate_one_chunked)

        result = at.translate_one(
            client=None,
            prompt="prompt",
            fpath="_docs/_developer_guide/content_cards.md",
            relative="_developer_guide/content_cards.md",
            english_content="## Hello\n\nBody.",
            lang_key="ja",
            lang_info={"name": "Japanese", "dir": "ja"},
            glossary={},
            styleguide="",
        )

        assert result["ok"] is True
        assert result.get("chunked") is True
        assert calls["translate_file"] == 1
        assert calls["chunked"] == 1

    def test_translate_one_review_max_tokens_falls_back_to_chunked(self, monkeypatch):
        calls = {"review_file": 0, "chunked": 0}

        def fake_translate_file(*_args, **_kwargs):
            return "## Hola\n\nCuerpo."

        def fake_review_file(*_args, **_kwargs):
            calls["review_file"] += 1
            raise at.MaxTokensTruncatedError(
                "Output truncated (hit 128000 token limit). "
                "Increase TRANSLATION_MAX_TOKENS or use chunked translation."
            )

        def fake_translate_one_chunked(*_args, **_kwargs):
            calls["chunked"] += 1
            return {
                "ok": True,
                "source": "_docs/_user_guide/foo.md",
                "target": "_lang/es/_user_guide/foo.md",
                "lang": "es",
                "chunked": True,
                "chunks": 1,
            }

        monkeypatch.setattr(at, "translate_file", fake_translate_file)
        monkeypatch.setattr(at, "review_file", fake_review_file)
        monkeypatch.setattr(at, "translate_one_chunked", fake_translate_one_chunked)

        result = at.translate_one(
            client=None,
            prompt="prompt",
            fpath="_docs/_user_guide/foo.md",
            relative="_user_guide/foo.md",
            english_content="## Hello\n\nBody.",
            lang_key="es",
            lang_info={"name": "Spanish", "dir": "es"},
            glossary={},
            styleguide="",
        )

        assert result["ok"] is True
        assert calls["review_file"] == 1
        assert calls["chunked"] == 1


class TestExtractErrorFiles:
    def test_matches_lang_prefixed_path(self):
        output = "Liquid error in _lang/fr_fr/_user_guide/foo/bar.md: unclosed tag"
        assert at.extract_error_files(output, "fr_fr") == [
            "_lang/fr_fr/_user_guide/foo/bar.md",
        ]

    def test_matches_collections_dir_without_lang_prefix(self):
        output = "Error reading file fr_fr/_includes/analytics/campaign_analytics.md"
        assert at.extract_error_files(output, "fr_fr") == [
            "_lang/fr_fr/_includes/analytics/campaign_analytics.md",
        ]


class TestChunkedTranslationRouting:
    def test_pricing_path_chunks_below_max_file_kb(self):
        path = "_docs/_unlisted_docs/pricing/message_credits_gamma_0dhr.md"
        assert at._uses_chunked_translation(path, 53)

    def test_normal_doc_not_force_chunked_at_same_size(self):
        assert not at._uses_chunked_translation("_docs/_user_guide/foo.md", 53)

    def test_oversized_file_always_chunked(self):
        assert at._uses_chunked_translation("_docs/_user_guide/foo.md", 200)


class TestIncrementalH2Translation:
    def test_split_into_h2_chunks_at_headings(self):
        content = (
            "---\nlayout: page\n---\n\n"
            "Intro.\n\n"
            "## Section one {#one}\n\nBody one.\n\n"
            "## Section two {#two}\n\nBody two.\n"
        )
        chunks = at.split_into_h2_chunks(content)
        assert len(chunks) == 3
        assert chunks[0].startswith("---")
        assert "## Section one {#one}" in chunks[1]
        assert "## Section two {#two}" in chunks[2]

    def test_split_into_h2_chunks_skips_headings_inside_liquid(self):
        content = (
            "## Outer {#outer}\n\n"
            "{% details More %}\n\n"
            "## Inner heading\n\n"
            "Details body.\n\n"
            "{% enddetails %}\n"
        )
        chunks = at.split_into_h2_chunks(content)
        assert len(chunks) == 1
        assert "## Inner heading" in chunks[0]

    def test_chunks_requiring_translation_detects_changes(self):
        prev = at.split_into_h2_chunks(
            "Intro\n\n## One {#one}\n\nAlpha.\n\n## Two {#two}\n\nBeta.\n"
        )
        curr = at.split_into_h2_chunks(
            "Intro\n\n## One {#one}\n\nAlpha changed.\n\n## Two {#two}\n\nBeta.\n"
        )
        needs = at.chunks_requiring_translation(curr, prev)
        assert needs == [False, True, False]

    def test_chunks_requiring_translation_marks_new_sections(self):
        prev = at.split_into_h2_chunks("## One {#one}\n\nAlpha.\n")
        curr = at.split_into_h2_chunks(
            "## One {#one}\n\nAlpha.\n\n## Two {#two}\n\nBeta.\n"
        )
        needs = at.chunks_requiring_translation(curr, prev)
        assert needs == [False, True]

    def test_incremental_skips_unchanged_chunks(self, monkeypatch):
        english = (
            "Intro\n\n## One {#one}\n\nAlpha.\n\n## Two {#two}\n\nBeta.\n"
        )
        previous = english
        existing = (
            "Intro FR\n\n## Un {#one}\n\nAlpha FR.\n\n## Deux {#two}\n\nBeta FR.\n"
        )
        calls = []

        def fake_translate_file(*args, **kwargs):
            calls.append(kwargs.get("english") or args[2])
            return "## Deux {#two}\n\nBeta FR mis à jour.\n"

        monkeypatch.setattr(at, "translate_file", fake_translate_file)
        monkeypatch.setattr(at, "review_file", lambda *a, **k: a[2])

        target = at.REPO_ROOT / "_lang/fr_fr/_user_guide/test_incremental.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(existing)

        result = at.translate_one_incremental(
            client=None,
            prompt="",
            fpath="_docs/_user_guide/test_incremental.md",
            relative="_user_guide/test_incremental.md",
            english_content=english.replace("Beta.", "Beta updated."),
            previous_english_content=previous,
            lang_key="fr",
            lang_info=at.LANGUAGES["fr"],
            glossary={},
            styleguide="",
        )

        assert result["ok"]
        assert result["chunks_skipped"] == 2
        assert result["chunks_translated"] == 1
        assert len(calls) == 1
        assert "Beta updated." in calls[0]
        written = target.read_text()
        assert "Alpha FR." in written
        assert "Beta FR mis à jour." in written
        target.unlink()
        if target.parent.exists() and not any(target.parent.iterdir()):
            target.parent.rmdir()

    def test_incremental_all_unchanged_skips_api(self, monkeypatch):
        english = "Intro\n\n## One {#one}\n\nAlpha.\n"
        calls = []

        def fake_translate_file(*args, **kwargs):
            calls.append(1)
            return "should not run"

        monkeypatch.setattr(at, "translate_file", fake_translate_file)

        target = at.REPO_ROOT / "_lang/fr_fr/_user_guide/test_skip.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("Intro FR\n\n## Un {#one}\n\nAlpha FR.\n")

        result = at.translate_one_incremental(
            client=None,
            prompt="",
            fpath="_docs/_user_guide/test_skip.md",
            relative="_user_guide/test_skip.md",
            english_content=english,
            previous_english_content=english,
            lang_key="fr",
            lang_info=at.LANGUAGES["fr"],
            glossary={},
            styleguide="",
        )

        assert result["ok"]
        assert result["chunks_translated"] == 0
        assert calls == []
        target.unlink()
        if target.parent.exists() and not any(target.parent.iterdir()):
            target.parent.rmdir()

    def test_new_file_falls_back_to_full_translate_with_review(self, monkeypatch):
        english = (
            "Intro\n\n## One {#one}\n\nAlpha.\n\n## Two {#two}\n\nBeta.\n"
        )
        review_calls = []

        monkeypatch.setattr(at, "load_english_at_git_ref", lambda fpath, ref: None)
        monkeypatch.setattr(
            at,
            "translate_file",
            lambda *a, **k: "## Un {#one}\n\nAlpha FR.\n\n## Deux {#two}\n\nBeta FR.\n",
        )
        monkeypatch.setattr(
            at,
            "review_file",
            lambda *a, **k: review_calls.append(1) or a[2],
        )

        target = at.REPO_ROOT / "_lang/fr_fr/_user_guide/test_new_file.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            target.unlink()

        result = at.translate_one(
            client=None,
            prompt="",
            fpath="_docs/_user_guide/test_new_file.md",
            relative="_user_guide/test_new_file.md",
            english_content=english,
            lang_key="fr",
            lang_info=at.LANGUAGES["fr"],
            glossary={},
            styleguide="",
            english_base_ref="abc123",
        )

        assert result["ok"]
        assert review_calls == [1]
        assert "incremental" not in result
        if target.exists():
            target.unlink()
        if target.parent.exists() and not any(target.parent.iterdir()):
            target.parent.rmdir()


class TestLiquidRawBlockQc:
    def test_raw_blocks_exclude_liquid_tags_from_counts(self):
        content = (
            "{% alert important %}\n"
            "Example: {% raw %}{% if x %}{% endraw %}\n"
            "{% endalert %}\n"
        )
        assert at._count_liquid_tag(content, "if") == 0
        at.validate_liquid_paired_tags(content, label="raw example")

    def test_custom_attributes_h2_chunk_three_is_liquid_balanced(self):
        from pathlib import Path

        path = Path(
            "_docs/_user_guide/data/activation/attributes/custom_attributes.md"
        )
        if not path.exists():
            return
        chunks = at.split_into_h2_chunks(path.read_text())
        assert len(chunks) >= 3
        at.validate_liquid_paired_tags(chunks[2], label="custom_attributes chunk 3")

    def test_remove_tag_line_skips_matches_inside_raw_blocks(self):
        content = (
            "{% endif %}\n"
            "{% raw %}\n"
            "{% endif %}\n"
            "{% endraw %}\n"
        )
        updated = at._remove_one_liquid_tag_line(content, "endif", prefer_last=True)
        assert "{% raw %}\n{% endif %}\n{% endraw %}" in updated
        assert updated.count("{% endif %}") == 1

    def test_repair_does_not_strip_close_tags_inside_raw_blocks(self):
        english = (
            "{% alert important %}\n"
            "Example: {% raw %}{% if x %}{% endraw %}\n"
            "{% endalert %}\n"
        )
        translated = (
            "{% alert important %}\n"
            "Example: {% raw %}{% if x %}{% endraw %}\n"
            "{% endalert %}\n"
            "{% endif %}\n"
        )
        repaired = at.repair_liquid_paired_tags_from_english(
            english, translated, label="raw close repair"
        )
        assert "{% if x %}" in repaired
        assert repaired.count("{% endif %}") == 0
        at.validate_liquid_paired_tags(repaired, label="raw close repair")


class TestLiquidSafeChunkSplits:
    def test_does_not_split_inside_details_block(self):
        content = (
            "---\nlayout: page\n---\n\n"
            "{% details Intro %}\n\n"
            "## Inner heading\n\n"
            "Body text.\n\n"
            "{% enddetails %}\n\n"
            "{% api %}\n## Event one\n\n"
            "Payload.\n\n"
            "{% endapi %}\n"
        )
        chunks = at.split_into_chunks(content, max_chunk_kb=1)
        assert len(chunks) >= 1
        for chunk in chunks:
            assert at._liquid_block_stack_at(chunk, len(chunk)) == []

    def test_message_engagement_chunks_have_balanced_liquid(self):
        from pathlib import Path

        path = Path(
            "_docs/_user_guide/data/distribution/braze_currents/"
            "event_glossary/message_engagement_events.md"
        )
        if not path.exists():
            return
        content = path.read_text()
        chunks = at.split_into_chunks(content)
        assert len(chunks) >= 2
        for i, chunk in enumerate(chunks):
            assert at._liquid_block_stack_at(chunk, len(chunk)) == [], (
                f"chunk {i + 1} ends with open Liquid blocks"
            )
        reassembled = "\n\n".join(c.strip() for c in chunks)
        at.validate_liquid_paired_tags(reassembled, label="reassembled")

    def test_validate_liquid_paired_tags_raises_on_imbalance(self):
        bad = "{% api %}\n## Foo\n{% enddetails %}\n"
        try:
            at.validate_liquid_paired_tags(bad)
            assert False, "expected ValueError"
        except ValueError as exc:
            assert "api=1" in str(exc)
            assert "endapi=0" in str(exc)


class TestRepairLiquidPairedTagsFromEnglish:
    def test_removes_extra_api_open_to_match_english(self):
        english = "\n\n{% api %}\n## WhatsApp Send {#whatsapp-send}\n\nBody\n\n{% endapi %}\n"
        translated = (
            "\n\n{% api %}\n{% api %}\n## Envoi WhatsApp {#whatsapp-send}\n\n"
            "Corps\n\n{% endapi %}\n"
        )
        repaired = at.repair_liquid_paired_tags_from_english(
            english, translated, label="chunk 26/26"
        )
        assert at._count_liquid_tag(repaired, "api") == 1
        assert at._count_liquid_tag(repaired, "endapi") == 1
        at.validate_liquid_paired_tags(repaired, label="chunk 26/26")

    def test_appends_missing_endapi_to_match_english(self):
        english = "{% api %}\n## Foo\n{% endapi %}\n"
        translated = "{% api %}\n## Foo traduit\n"
        repaired = at.repair_liquid_paired_tags_from_english(
            english, translated, label="chunk"
        )
        assert repaired.rstrip().endswith("{% endapi %}")

    def test_removes_middle_spurious_open_between_complete_blocks(self):
        """Regression: prefer unmatched opens over prefer_last+skip_first."""
        english = (
            "{% api %}\n## One {#one}\nbody\n{% endapi %}\n\n"
            "{% api %}\n## Two {#two}\nbody\n{% endapi %}\n"
        )
        translated = (
            "{% api %}\n## Un {#one}\ncorps\n{% endapi %}\n\n"
            "{% api %}\n"
            "{% api %}\n## Deux {#two}\ncorps\n{% endapi %}\n"
        )
        repaired = at.repair_liquid_paired_tags_from_english(
            english, translated, label="chunk"
        )
        assert at._count_liquid_tag(repaired, "api") == 2
        assert at._count_liquid_tag(repaired, "endapi") == 2
        assert "## Un {#one}" in repaired
        assert "## Deux {#two}" in repaired
        # Prefer removing the unmatched middle open, not the second block's open.
        # Wrong prefer_last+skip_first behavior leaves: endapi, then ## Deux
        # with no opening api for the second block.
        two_block = repaired[repaired.index("{% endapi %}") :]
        assert two_block.index("{% api %}") < two_block.index("{#two}")
        at.validate_liquid_paired_tags(repaired, label="chunk")
        assert at._liquid_block_stack_at(repaired, len(repaired)) == []

    def test_validate_or_repair_chunk_liquid_repairs_without_retry(self):
        english = "{% api %}\n## Foo {#foo}\n{% endapi %}\n"
        translated = "{% api %}\n{% api %}\n## Foo FR {#foo}\n{% endapi %}\n"
        repaired = at._validate_or_repair_chunk_liquid(
            english, translated, "chunk 1/1"
        )
        assert at._count_liquid_tag(repaired, "api") == 1

    def test_remove_one_liquid_tag_line_skip_first_raises_with_single_match(self):
        content = "{% api %}\n## Foo\n"
        try:
            at._remove_one_liquid_tag_line(content, "api", skip_first=True)
            assert False, "expected ValueError"
        except ValueError as exc:
            assert "cannot preserve first 1" in str(exc)

    def test_remove_one_liquid_tag_line_skip_first_keeps_first_match(self):
        content = "{% api %}\n{% api %}\n## Foo\n"
        updated = at._remove_one_liquid_tag_line(
            content, "api", prefer_last=True, skip_first=True
        )
        assert updated.count("{% api %}") == 1
        assert updated.startswith("{% api %}")

    def test_remove_one_liquid_tag_line_preserve_first_n(self):
        content = "{% api %}\n{% api %}\n{% api %}\n## Foo\n"
        updated = at._remove_one_liquid_tag_line(
            content, "api", prefer_last=True, preserve_first_n=2
        )
        assert updated.count("{% api %}") == 2
        assert updated.startswith("{% api %}\n{% api %}\n")


class TestJaCampaignComposerUiRepairs:
    def test_localizes_leaked_wizard_labels(self):
        content = (
            "On **Target Audiences**, use **Schedule Delivery** and "
            "**Audience Summary** in **User Lookup** before **Review Summary**."
        )
        path = (
            "_lang/ja/_user_guide/messaging/campaigns/creating_campaign.md"
        )
        new_content, repairs = at.repair_ja_campaign_composer_ui(
            path, content, "ja"
        )
        assert "**ターゲットオーディエンス**" in new_content
        assert "**配信をスケジュール**" in new_content
        assert "**オーディエンスの概要**" in new_content
        assert "**ユーザー検索**" in new_content
        assert "**レビューサマリー**" in new_content
        assert repairs

    def test_skips_non_japanese_locales(self):
        content = "On **Target Audiences**, define users."
        path = (
            "_lang/fr_fr/_user_guide/messaging/campaigns/creating_campaign.md"
        )
        new_content, repairs = at.repair_ja_campaign_composer_ui(
            path, content, "fr"
        )
        assert new_content == content
        assert repairs == []

    def test_repairs_partner_and_alt_text_variants(self):
        content = (
            'In **Schedule Delivery**, open the 「Schedule Delivery」 page and '
            "**Multichannel キャンペーン** option."
        )
        path = "_lang/ja/_partners/foo/bar.md"
        new_content, repairs = at.repair_ja_campaign_composer_ui(
            path, content, "ja"
        )
        assert "**配信をスケジュール**" in new_content
        assert "「配信をスケジュール」" in new_content
        assert "**マルチチャネル キャンペーン**" in new_content
        assert repairs

    def test_localizes_add_variant_dropdown_label(self):
        content = (
            "Use the **Add Variant** dropdown to select **Copy from Variant**."
        )
        path = "_lang/ja/_user_guide/channels/banners/create_a_banner.md"
        new_content, repairs = at.repair_ja_campaign_composer_ui(
            path, content, "ja"
        )
        assert "**バリアントを追加**" in new_content
        assert "**バリアントからコピー**" in new_content
        assert "Add Variant" not in new_content
        assert repairs

    def test_localizes_schedule_delivery_option_labels(self):
        content = (
            "On **Schedule Delivery**, choose **Action-Based Delivery** and "
            "**Send an SMS Inbound Message**."
        )
        path = "_lang/ja/_partners/foo/bar.md"
        new_content, repairs = at.repair_ja_campaign_composer_ui(
            path, content, "ja"
        )
        assert "**配信をスケジュール**" in new_content
        assert "**アクションベースの配信**" in new_content
        assert "**SMSインバウンドメッセージを送信する**" in new_content
        assert repairs

    def test_localizes_canvas_send_settings(self):
        content = (
            "**ターゲットオーディエンス** (for campaigns) or **Send Settings** "
            '(for Canvas). See the 「Send Settings」 step.'
        )
        path = "_lang/ja/_user_guide/messaging/messaging_fundamentals/frequency_capping.md"
        new_content, repairs = at.repair_ja_campaign_composer_ui(
            path, content, "ja"
        )
        assert "**送信設定**" in new_content
        assert "「送信設定」" in new_content
        assert "Send Settings" not in new_content
        assert repairs

    def test_localizes_search_users_and_schedule_short_form(self):
        content = (
            "Go to **Audience** > **Search Users**. In the campaign composer's "
            "**Schedule** section, select **Allow users to become re-eligible "
            "to receive campaign**."
        )
        path = "_lang/ja/_includes/developer_guide/_shared/sending_test_messages.md"
        new_content, repairs = at.repair_ja_campaign_composer_ui(
            path, content, "ja"
        )
        assert "**オーディエンス** > **ユーザーを検索**" in new_content
        assert "composer's **配信をスケジュール**" in new_content
        assert "**ユーザーがキャンペーンを再度受信できるようにする**" in new_content
        assert repairs

    def test_localizes_approval_workflow_labels(self):
        content = (
            "On the **Summary** step, set **Pending Approval** to **Approved** "
            "for **Target Audience** and **Entry Schedule**."
        )
        path = "_lang/ja/_user_guide/messaging/governance/approvals.md"
        new_content, repairs = at.repair_ja_campaign_composer_ui(
            path, content, "ja"
        )
        assert "**レビューサマリー**ステップ" in new_content
        assert "**承認待ち**" in new_content
        assert "**承認済み**" in new_content
        assert "**ターゲットオーディエンス**" in new_content
        assert "**エントリスケジュール**" in new_content
        assert repairs

    def test_localizes_event_history_permission_list(self):
        content = (
            "**ユーザーを検索**、**View User Event Properties**、および**View PII**"
        )
        path = "_lang/ja/_user_guide/audience/manage_audience/user_profiles.md"
        new_content, repairs = at.repair_ja_campaign_composer_ui(
            path, content, "ja"
        )
        assert "**ユーザーイベントプロパティを表示**" in new_content
        assert "**PIIを表示**" in new_content
        assert "View User Event Properties" not in new_content
        assert "View PII" not in new_content
        assert repairs

    def test_localizes_settings_api_keys_nav_path(self):
        content = (
            "In Braze, go to **Settings** > **API Keys** to locate your key."
        )
        path = "_lang/ja/_includes/developer_guide/_shared/sending_test_messages.md"
        new_content, repairs = at.repair_ja_campaign_composer_ui(
            path, content, "ja"
        )
        assert "**設定** > **APIキー**" in new_content
        assert "Settings" not in new_content
        assert repairs

    def test_repairs_create_campaign_after_product_term_pass(self):
        content = "Select **Create キャンペーン** to start."
        path = "_lang/ja/_user_guide/messaging/campaigns/creating_campaign.md"
        new_content, repairs = at.repair_ja_campaign_composer_ui(
            path, content, "ja"
        )
        assert "**キャンペーンを作成**" in new_content
        assert "Create キャンペーン" not in new_content
        assert repairs
