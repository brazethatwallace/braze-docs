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
