
# QA test plan: unlisted_docs migration (local environment)

This QA plan verifies the migration of `braze-docs-hidden` content into `braze-docs:_docs/_unlisted_docs/`. Use it after starting the local Jekyll server.

## How to run the local server

From the repo root:

```bash
cd /Users/zair.kelleyortiz/Documents/braze-docs-main
rake
```

`rake` starts:

- The Jekyll dev server on `http://127.0.0.1:5006` (this is what serves `/docs/...` pages)
- A small Sinatra proxy on `http://127.0.0.1:4000`

All clickable URLs in this plan use `http://127.0.0.1:5006`. Wait until the build finishes (you'll see the prompt return without further regeneration messages).

## What this plan does and does not cover

- **Covered locally:** every canonical `/docs/<permalink>/` URL for the 66 migrated unlisted pages.
- **Not covered locally:** the legacy `/unlisted_docs/<permalink>/` URLs, because those redirects are configured in `vercel.json` (HTTP 308) and `rake` doesn't run Vercel's edge layer. To test them locally, run `vercel dev` (`npm i -g vercel`, then `vercel dev` from the repo root) and use the URLs in [Section: Testing legacy `/unlisted_docs/` redirects](#testing-legacy-unlisted_docs-redirects).

## Pages to test (66 URLs)

Click each URL. It should return HTTP 200 and render either the full page or, for archived stubs, an HTTP 0 meta-refresh redirect to the canonical public page (your browser will follow it automatically).

### `archive/` (22 pages)

- [ ] [api_usage_alerts](http://127.0.0.1:5006/docs/api_usage_alerts/) — `archive/api_usage_alerts.md` — redirects to `https://www.braze.com/docs/user_guide/analytics/dashboard/api_usage_alerts`
- [ ] [api_usage_dashboard](http://127.0.0.1:5006/docs/api_usage_dashboard/) — `archive/api_usage_dashboard.md` — redirects to `https://www.braze.com/docs/user_guide/analytics/dashboard/api_usage_dashboard`
- [ ] [audience_sync_trade_desk](http://127.0.0.1:5006/docs/audience_sync_trade_desk/) — `archive/audience_sync_trade_desk.md` — redirects to `https://www.braze.com/docs/partners/canvas_audience_sync/trade_desk_audience_sync/`
- [ ] [campaign_drafts](http://127.0.0.1:5006/docs/campaign_save_as_draft/) — `archive/campaign_drafts.md` — redirects to `https://www.braze.com/docs/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/#campaign-drafts`
- [ ] [canvas_triggered_iams](http://127.0.0.1:5006/docs/canvas_triggered_in-app_messages/) — `archive/canvas_triggered_iams.md` — redirects to `https://www.braze.com/docs/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/`
- [ ] [connected_content](http://127.0.0.1:5006/docs/connected_content/) — `archive/connected_content.md` — redirects to `https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/`
- [ ] [copying_canvases](http://127.0.0.1:5006/docs/copying_canvases_across_workspaces/) — `archive/copying_canvases.md` — redirects to `https://www.braze.com/docs/user_guide/engagement_tools/messaging_fundamentals/copying_across_workspaces/`
- [ ] [create_banner_card](http://127.0.0.1:5006/docs/create_banner_card/) — `archive/create_banner_card.md` — redirects to `https://www.braze.com/docs/developer_guide/banner_cards/creating_banner_cards/`
- [ ] [custom_domains](http://127.0.0.1:5006/docs/self_serve_custom_domains/) — `archive/custom_domains.md` — redirects to `https://www.braze.com/docs/custom_domains/`
- [ ] [inbox_vision](http://127.0.0.1:5006/docs/inbox_vision_best_practices/) — `archive/inbox_vision.md` — redirects to `https://www.braze.com/docs/user_guide/message_building_by_channel/email/inbox_vision`
- [ ] [line_click_tracking](http://127.0.0.1:5006/docs/line_click_tracking/) — `archive/line_click_tracking.md` — redirects to `https://www.braze.com/docs/line/click_tracking/`
- [ ] [multiple_stores](http://127.0.0.1:5006/docs/shopify_multiple_store/) — `archive/multiple_stores.md` — redirects to `https://www.braze.com/docs/partners/ecommerce/shopify/multiple_stores`
- [ ] [post_duplicate_canvas](http://127.0.0.1:5006/docs/post_duplicate_canvases/) — `archive/post_duplicate_canvas.md` — redirects to `https://www.braze.com/docs/api/endpoints/messaging/duplicate_messages/post_duplicate_canvases/`
- [ ] [post_user_track_synchronous](http://127.0.0.1:5006/docs/post_users_track_synchronous/) — `archive/post_user_track_synchronous.md` — redirects to `https://www.braze.com/docs/api/endpoints/user_data/post_user_track_synchronous`
- [ ] [rate_limiting](http://127.0.0.1:5006/docs/rate_limiting/) — `archive/rate_limiting.md` — redirects to `https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting`
- [ ] [report_builder_2](http://127.0.0.1:5006/docs/report_builder_2/) — `archive/report_builder_2.md` — redirects to `https://www.braze.com/docs/user_guide/analytics/reporting/report_builder/`
- [ ] [shopify](http://127.0.0.1:5006/docs/shopify_integration_overview/) — `archive/shopify.md` — redirects to `https://www.braze.com/docs/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_overview/`
- [ ] [shopify_features](http://127.0.0.1:5006/docs/shopify_data/) — `archive/shopify_features.md` — redirects to `https://www.braze.com/docs/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_data_features/`
- [ ] [shopify_user_reconciliation](http://127.0.0.1:5006/docs/shopify_user_reconciliation/) — `archive/shopify_user_reconciliation.md` — redirects to `https://www.braze.com/docs/partners/ecommerce/shopify/shopify_data_features/`
- [ ] [target_approvals](http://127.0.0.1:5006/docs/target_approvals/) — `archive/target_approvals.md` — redirects to `https://www.braze.com/docs/user_guide/engagement_tools/messaging_fundamentals/approvals/messaging_rules/`
- [ ] [text_only_rcs](http://127.0.0.1:5006/docs/text_only_rcs/) — `archive/text_only_rcs.md` — redirects to `https://braze.com/docs/user_guide/message_building_by_channel/sms_mms_rcs/rcs/create/`
- [ ] [using_shopify_with_braze](http://127.0.0.1:5006/docs/using_shopify_with_braze/) — `archive/using_shopify_with_braze.md` — redirects to `https://www.braze.com/docs/partners/ecommerce/shopify/shopify_overview/`

### `other/` (7 pages)

- [ ] [Core Endpoints](http://127.0.0.1:5006/docs/core_endpoints/) — `other/core_endpoints.md`
- [ ] [Device & Carriers](http://127.0.0.1:5006/docs/device_and_carriers/) — `other/devices_and_carriers.md`
- [ ] [Ephemeral custom events](http://127.0.0.1:5006/docs/ephemeral_custom_events/) — `other/ephemeral_custom_events.md`
- [ ] [Generations](http://127.0.0.1:5006/docs/iam_generations/) — `other/generations.md`
- [ ] [Entitlements handbook](http://127.0.0.1:5006/docs/handbooks/) — `other/handbooks.md`
- [ ] [RCS-Supported Sending Countries and Carrier Coverage](http://127.0.0.1:5006/docs/rcs_supported_countries/) — `other/rcs_supported_countries.md`
- [ ] [SMS Traffic Pumping Fraud FAQs](http://127.0.0.1:5006/docs/sms_traffic_pumping_fraud/) — `other/sms_traffic_pumping_fraud.md`

### `pricing/` (10 pages)

- [ ] [Braze Go](http://127.0.0.1:5006/docs/braze_go/) — `pricing/braze_go.md`
- [ ] [WhatsApp Credit Ratios](http://127.0.0.1:5006/docs/credits_whatsapp/) — `pricing/credit_ratios.md`
- [ ] [Message Credits - Calculator](http://127.0.0.1:5006/docs/message_credits_calc/) — `pricing/message_credits.md`
- [ ] [Message Credits - Delta](http://127.0.0.1:5006/docs/message_credits_delta_a3sy/) — `pricing/message_credits_delta_a3sy.md`
- [ ] [Braze Message Credits Descriptions](http://127.0.0.1:5006/docs/message_credits_descriptions/) — `pricing/message_credits_descriptions.md`
- [ ] [Message Credits - Gamma](http://127.0.0.1:5006/docs/message_credits_gamma_0dhr/) — `pricing/message_credits_gamma_0dhr.md`
- [ ] [Message Credits - Lambda](http://127.0.0.1:5006/docs/message_credits_lambda_k5gh/) — `pricing/message_credits_lambda_k5gh.md`
- [ ] [Message Credits - Sigma](http://127.0.0.1:5006/docs/message_credits_sigma_pow2/) — `pricing/message_credits_sigma_pow2.md`
- [ ] [Message Credits - Theta](http://127.0.0.1:5006/docs/message_credits_theta_d9kw/) — `pricing/message_credits_theta_d9kw.md`
- [ ] [WhatsApp Pricing Updates](http://127.0.0.1:5006/docs/whatsapp_pricing_updates/) — `pricing/whatsapp_pricing.md`

### `private_betas/` (27 pages)

- [ ] [Account Objects](http://127.0.0.1:5006/docs/account_object/) — `private_betas/accounts_opportunities_object.md`
- [ ] [AI Step](http://127.0.0.1:5006/docs/ai_step/) — `private_betas/ai_step.md`
- [ ] [Autosave for Campaigns](http://127.0.0.1:5006/docs/campaign_autosave/) — `private_betas/campaign_autosave.md`
- [ ] [Import User Data and CSV Events](http://127.0.0.1:5006/docs/csv_events/) — `private_betas/csv_events.md`
- [ ] [Custom Attributes](http://127.0.0.1:5006/docs/custom_attributes_entitlements/) — `private_betas/custom_attributes_entitlements.md`
- [ ] [Custom Events](http://127.0.0.1:5006/docs/custom_events_entitlements/) — `private_betas/custom_events_entitlements.md`
- [ ] [Preview Drag-and-Drop Editor Content Blocks](http://127.0.0.1:5006/docs/preview_dnd_content_blocks/) — `private_betas/dnd_content_blocks_preview.md`
- [ ] [Email HTML Editor](http://127.0.0.1:5006/docs/email_html_editor/) — `private_betas/email_html_react.md`
- [ ] [GET: List workspace Apps](http://127.0.0.1:5006/docs/get_app_group_apps/) — `private_betas/get_app_group_apps.md`
- [ ] [GET: List Link Alias for Campaigns](http://127.0.0.1:5006/docs/get_campaign_link_alias/) — `private_betas/get_campaign_url_info.md`
- [ ] [GET: List Link Aliases for Canvas](http://127.0.0.1:5006/docs/get_canvas_link_alias/) — `private_betas/get_canvas_url_info.md`
- [ ] [Idle Campaigns and Canvases](http://127.0.0.1:5006/docs/idle_campaigns_canvases/) — `private_betas/idle_campaigns.md`
- [ ] [Last-touch attribution](http://127.0.0.1:5006/docs/last-touch_attribution_metrics/) — `private_betas/last_touch_attribution_report_builder.md`
- [ ] [Message Prioritization](http://127.0.0.1:5006/docs/message_prioritization/) — `private_betas/message_prioritization.md`
- [ ] [Message Template Assistant](http://127.0.0.1:5006/docs/template_assistant/) — `private_betas/message_template_assistant.md`
- [ ] [POST: Track Users (Bulk)](http://127.0.0.1:5006/docs/track_users_bulk/) — `private_betas/post_track_users_bulk.md`
- [ ] [POST: Track Users (Bulk) for Braze Partners](http://127.0.0.1:5006/docs/track_users_bulk_partners/) — `private_betas/post_track_users_bulk_partners.md`
- [ ] [Rate Limiting for Push Campaigns and Multichannel Canvases](http://127.0.0.1:5006/docs/rate_limiting_v3/) — `private_betas/rate_limiting_v3.md`
- [ ] [Creating an RCS Message](http://127.0.0.1:5006/docs/create_rcs_message/) — `private_betas/rich_cards.md`
- [ ] [Sender Verification](http://127.0.0.1:5006/docs/sender_verification/) — `private_betas/sender_verification.md`
- [ ] [Shopify](http://127.0.0.1:5006/docs/shopify/) — `private_betas/shopify_beta.md`
- [ ] [Upgrading Shopify (Custom)](http://127.0.0.1:5006/docs/shopify_custom_upgrade/) — `private_betas/shopify_beta/shopify_custom_integration_upgrade.md`
- [ ] [Upgrading Shopify](http://127.0.0.1:5006/docs/shopify_standard_upgrade/) — `private_betas/shopify_beta/shopify_standard_integration_upgrade.md`
- [ ] [Shopify Upgrade Overview](http://127.0.0.1:5006/docs/shopify_upgrade_overview/) — `private_betas/shopify_beta/shopify_upgrade_overview.md`
- [ ] [Shopify Collections Sync](http://127.0.0.1:5006/docs/shopify_collections_sync/) — `private_betas/shopify_collections_sync.md`
- [ ] [In-app message surveys](http://127.0.0.1:5006/docs/user_guide/channels/in_app_messages/drag_and_drop/surveys/) — `channels/in_app_messages/drag_and_drop/surveys.md`
- [ ] [Landing page surveys](http://127.0.0.1:5006/docs/user_guide/messaging/landing_pages/create_landing_pages/surveys/) — `messaging/landing_pages/create_landing_pages/surveys.md`
- [ ] [Workspace rate limits](http://127.0.0.1:5006/docs/workspace_rate_limits/) — `private_betas/workspace_rate_limits.md`

## Bulk URL validator

Validate every URL in one shot from the command line (run while `rake` is up):

```bash
# From the repo root, with the local server running on port 5006
urls=(
  "http://127.0.0.1:5006/docs/api_usage_alerts/"
  "http://127.0.0.1:5006/docs/api_usage_dashboard/"
  "http://127.0.0.1:5006/docs/audience_sync_trade_desk/"
  "http://127.0.0.1:5006/docs/campaign_save_as_draft/"
  "http://127.0.0.1:5006/docs/canvas_triggered_in-app_messages/"
  "http://127.0.0.1:5006/docs/connected_content/"
  "http://127.0.0.1:5006/docs/copying_canvases_across_workspaces/"
  "http://127.0.0.1:5006/docs/create_banner_card/"
  "http://127.0.0.1:5006/docs/self_serve_custom_domains/"
  "http://127.0.0.1:5006/docs/inbox_vision_best_practices/"
  "http://127.0.0.1:5006/docs/line_click_tracking/"
  "http://127.0.0.1:5006/docs/shopify_multiple_store/"
  "http://127.0.0.1:5006/docs/post_duplicate_canvases/"
  "http://127.0.0.1:5006/docs/post_users_track_synchronous/"
  "http://127.0.0.1:5006/docs/rate_limiting/"
  "http://127.0.0.1:5006/docs/report_builder_2/"
  "http://127.0.0.1:5006/docs/shopify_integration_overview/"
  "http://127.0.0.1:5006/docs/shopify_data/"
  "http://127.0.0.1:5006/docs/shopify_user_reconciliation/"
  "http://127.0.0.1:5006/docs/target_approvals/"
  "http://127.0.0.1:5006/docs/text_only_rcs/"
  "http://127.0.0.1:5006/docs/using_shopify_with_braze/"
  "http://127.0.0.1:5006/docs/core_endpoints/"
  "http://127.0.0.1:5006/docs/device_and_carriers/"
  "http://127.0.0.1:5006/docs/ephemeral_custom_events/"
  "http://127.0.0.1:5006/docs/iam_generations/"
  "http://127.0.0.1:5006/docs/handbooks/"
  "http://127.0.0.1:5006/docs/rcs_supported_countries/"
  "http://127.0.0.1:5006/docs/sms_traffic_pumping_fraud/"
  "http://127.0.0.1:5006/docs/braze_go/"
  "http://127.0.0.1:5006/docs/credits_whatsapp/"
  "http://127.0.0.1:5006/docs/message_credits_calc/"
  "http://127.0.0.1:5006/docs/message_credits_delta_a3sy/"
  "http://127.0.0.1:5006/docs/message_credits_descriptions/"
  "http://127.0.0.1:5006/docs/message_credits_gamma_0dhr/"
  "http://127.0.0.1:5006/docs/message_credits_lambda_k5gh/"
  "http://127.0.0.1:5006/docs/message_credits_sigma_pow2/"
  "http://127.0.0.1:5006/docs/message_credits_theta_d9kw/"
  "http://127.0.0.1:5006/docs/whatsapp_pricing_updates/"
  "http://127.0.0.1:5006/docs/account_object/"
  "http://127.0.0.1:5006/docs/ai_step/"
  "http://127.0.0.1:5006/docs/campaign_autosave/"
  "http://127.0.0.1:5006/docs/csv_events/"
  "http://127.0.0.1:5006/docs/custom_attributes_entitlements/"
  "http://127.0.0.1:5006/docs/custom_events_entitlements/"
  "http://127.0.0.1:5006/docs/preview_dnd_content_blocks/"
  "http://127.0.0.1:5006/docs/email_html_editor/"
  "http://127.0.0.1:5006/docs/get_app_group_apps/"
  "http://127.0.0.1:5006/docs/get_campaign_link_alias/"
  "http://127.0.0.1:5006/docs/get_canvas_link_alias/"
  "http://127.0.0.1:5006/docs/idle_campaigns_canvases/"
  "http://127.0.0.1:5006/docs/last-touch_attribution_metrics/"
  "http://127.0.0.1:5006/docs/message_prioritization/"
  "http://127.0.0.1:5006/docs/template_assistant/"
  "http://127.0.0.1:5006/docs/track_users_bulk/"
  "http://127.0.0.1:5006/docs/track_users_bulk_partners/"
  "http://127.0.0.1:5006/docs/rate_limiting_v3/"
  "http://127.0.0.1:5006/docs/create_rcs_message/"
  "http://127.0.0.1:5006/docs/sender_verification/"
  "http://127.0.0.1:5006/docs/shopify/"
  "http://127.0.0.1:5006/docs/shopify_custom_upgrade/"
  "http://127.0.0.1:5006/docs/shopify_standard_upgrade/"
  "http://127.0.0.1:5006/docs/shopify_upgrade_overview/"
  "http://127.0.0.1:5006/docs/shopify_collections_sync/"
  "http://127.0.0.1:5006/docs/user_guide/channels/in_app_messages/drag_and_drop/surveys/"
  "http://127.0.0.1:5006/docs/user_guide/messaging/landing_pages/create_landing_pages/surveys/"
  "http://127.0.0.1:5006/docs/workspace_rate_limits/"
)
for u in "${urls[@]}"; do
  code=$(curl -s -o /dev/null -w "%{http_code}" -L "$u")
  printf "%s  %s\n" "$code" "$u"
done | tee /tmp/unlisted_qa_results.txt
# Anything other than 200 needs investigation:
grep -v "^200" /tmp/unlisted_qa_results.txt || echo "All URLs returned 200"
```

## Asset spot checks

Open at least one image and one downloadable file from the namespaced asset folder to confirm assets resolve:

- [ ] [Sample image (Shopify integration screenshot)](http://127.0.0.1:5006/docs/assets/unlisted_docs/img/shopify/add_personalization.png)
- [ ] [Sample PDF (Entitlements Handbook 27)](http://127.0.0.1:5006/docs/assets/unlisted_docs/download_file/Braze_Entitlements_Handbook_27.pdf)
- [ ] On any page that embeds an image (for example [Shopify](http://127.0.0.1:5006/docs/shopify/) or [In-app message surveys](http://127.0.0.1:5006/docs/user_guide/channels/in_app_messages/drag_and_drop/surveys/)), confirm images render inline rather than showing broken-image icons.

## Visibility checks (collection metadata)

These verify that the `unlisted_docs` collection is correctly excluded from nav, search, and the sitemap.

- [ ] Open any unlisted page and view source. The `<head>` should include `<meta name="robots" content="noindex, nofollow">`.
- [ ] Open any unlisted page and confirm there's no left-hand navigation menu and no breadcrumb.
- [ ] Open `http://127.0.0.1:5006/docs/sitemap.xml`. None of the unlisted permalinks above should appear in the sitemap.
- [ ] Open `http://127.0.0.1:5006/docs/` and use the on-page search box. Unlisted pages should not appear in autocomplete or results.
- [ ] Confirm the public Shopify partner page still works (it shares legacy URLs with one migrated page): `http://127.0.0.1:5006/docs/partners/shopify/` should resolve to the public page, not the migrated `shopify_beta` page.

## Testing legacy `/unlisted_docs/` redirects

`rake` doesn't honor `vercel.json` — it serves files straight off disk. To test the 308 redirects, install Vercel CLI and run `vercel dev`:

```bash
npm i -g vercel
cd /Users/zair.kelleyortiz/Documents/braze-docs-main
vercel dev
# Vercel will pick a port (usually 3000). Replace :PORT with the port shown in the terminal.
```

Then verify a handful of legacy URLs return HTTP 308 with the expected `Location:`:

```bash
# Page redirects:
curl -sI "http://localhost:3000/unlisted_docs/api_usage_alerts/" | grep -E "HTTP|location"  # expect 308 -> /docs/api_usage_alerts/
curl -sI "http://localhost:3000/unlisted_docs/api_usage_dashboard/" | grep -E "HTTP|location"  # expect 308 -> /docs/api_usage_dashboard/
curl -sI "http://localhost:3000/unlisted_docs/audience_sync_trade_desk/" | grep -E "HTTP|location"  # expect 308 -> /docs/audience_sync_trade_desk/
curl -sI "http://localhost:3000/unlisted_docs/campaign_save_as_draft/" | grep -E "HTTP|location"  # expect 308 -> /docs/campaign_save_as_draft/
curl -sI "http://localhost:3000/unlisted_docs/canvas_triggered_in-app_messages/" | grep -E "HTTP|location"  # expect 308 -> /docs/canvas_triggered_in-app_messages/

# Asset redirect:
curl -sI "http://localhost:3000/unlisted_docs/assets/img/braze_go/braze_go_overview.png" \
  | grep -E "HTTP|location"  # expect 308 -> /docs/assets/unlisted_docs/img/braze_go/braze_go_overview.png
```

For a full sweep of all 66 legacy page URLs, replace `127.0.0.1:5006/docs` with `localhost:3000/unlisted_docs` in the bulk URL validator above and look for `308`.

## Build-quality checks (run once before sign-off)

```bash
# 1. Permalink uniqueness across the full _docs/ tree
grep -rh '^permalink:' _docs/ | sort | uniq -c | sort -rn | awk '$1 > 1'
# Expected: no output

# 2. No alias collisions with new unlisted permalinks
grep -rh '^permalink:' _docs/_unlisted_docs/ | awk '{print $2}' | tr -d '"' | while read p; do
  slug=$(echo "$p" | sed "s|/$||")
  hits=$(grep -rln "^alias:.*${slug}/" _docs/ 2>/dev/null | grep -v _docs/_unlisted_docs | grep -v _lang/)
  if [ -n "$hits" ]; then echo "COLLISION: $p"; echo "$hits" | sed "s/^/  /"; fi
done
# Expected: no output
```

## Sign-off checklist

- [ ] Local server starts cleanly (`rake`).
- [ ] All 66 canonical URLs return HTTP 200 (bulk validator).
- [ ] Sample images and PDFs from `assets/unlisted_docs/` load.
- [ ] `noindex, nofollow` meta tag present on a sampled unlisted page.
- [ ] Unlisted permalinks absent from `/docs/sitemap.xml`.
- [ ] Unlisted pages absent from on-page search.
- [ ] (Optional but recommended) `vercel dev` shows HTTP 308 with the expected `Location:` header for legacy `/unlisted_docs/` URLs.
- [ ] No permalink-uniqueness or alias-collision warnings.

Once every box is checked, the migration is ready for review.
