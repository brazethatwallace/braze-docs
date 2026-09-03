---
nav_title: 번역
article_title: 번역 엔드포인트
search_tag: Endpoint
page_order: 9
layout: dev_guide

description: "이 랜딩 페이지에는 Braze 번역 엔드포인트가 나열되어 있습니다."
page_type: landing

guide_top_header: "번역 엔드포인트"
guide_top_text: "Braze 번역 엔드포인트를 사용하여 Campaigns, Canvases, Content Blocks, 이메일 템플릿, 웹훅 템플릿에서 번역을 관리하고 업데이트하세요."

guide_featured_title: "Campaign 엔드포인트"
guide_featured_list:
  - name: "GET: Campaign 번역 보기"
    link: /docs/api/endpoints/translations/campaigns/get_translation_campaign
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: Campaign에서 번역 업데이트"
    link: /docs/api/endpoints/translations/campaigns/put_update_translation_campaign
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: Campaign 기본 소스 번역 보기"
    link: /docs/api/endpoints/translations/campaigns/get_source_campaign
    image: /assets/img/braze_icons/message-plus-square.svg

guide_menu_title: "캔버스 엔드포인트"
guide_menu_list:
  - name: "GET: 캔버스 번역 보기"
    link: /docs/api/endpoints/translations/canvas/get_translation_canvas
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: 캔버스에서 번역 업데이트"
    link: /docs/api/endpoints/translations/canvas/put_update_translation_canvas
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: 캔버스 기본 소스 번역 보기"
    link: /docs/api/endpoints/translations/canvas/get_source_canvas
    image: /assets/img/braze_icons/message-plus-square.svg

guide_menu_title2: "이메일 템플릿 엔드포인트"
guide_menu_list2:
  - name: "GET: 이메일 템플릿 기본 소스 번역 보기"
    link: /docs/api/endpoints/translations/email_templates/get_view_source_template
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET: 특정 번역 및 로케일 보기"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_locale_template
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: 모든 번역 및 로케일 보기"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_template
    image: /assets/img/braze_icons/target-04.svg
  - name: "PUT: 이메일 템플릿에서 번역 업데이트"
    link: /docs/api/endpoints/translations/email_templates/put_update_template
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title3: "콘텐츠 블록 엔드포인트"
guide_menu_list3:
  - name: "GET: 콘텐츠 블록의 모든 번역 보기"
    link: /docs/api/endpoints/translations/content_blocks/get_translation_content_block
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: 콘텐츠 블록에서 번역 업데이트"
    link: /docs/api/endpoints/translations/content_blocks/put_update_translation_content_block
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title4: "웹훅 템플릿 엔드포인트"
guide_menu_list4:
  - name: "GET: 웹훅 템플릿 기본 소스 번역 보기"
    link: /docs/api/endpoints/translations/webhook_templates/get_view_source_webhook_template
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET: 웹훅 템플릿 번역 보기"
    link: /docs/api/endpoints/translations/webhook_templates/get_view_translations_webhook_template
    image: /assets/img/braze_icons/target-04.svg
  - name: "PUT: 웹훅 템플릿에서 번역 업데이트"
    link: /docs/api/endpoints/translations/webhook_templates/put_update_webhook_template
    image: /assets/img/braze_icons/target-04.svg

---

{% multi_lang_include alerts/early_access_beta_alert.md feature='Access to the Braze translation endpoints' %}

## 번역 엔드포인트 작동 방식 {#how-our-translation-endpoints-work}

번역 엔드포인트는 [다국어 작성]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings)과 함께 작동하며, 메시지를 수신하는 사용자에 따라 다른 버전으로 렌더링할 수 있는 메시지를 생성할 수 있습니다.

### 필수 조건 {#prerequisites}

이 엔드포인트를 사용하기 전에 [로케일을 추가]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings#add-a-locale)해야 합니다.

### 번역 테스트 방법 {#how-to-test-your-translations}

API와 Braze 대시보드를 사용하여 Campaigns, Canvases(개별 단계 포함), Content Blocks, 이메일 템플릿, 웹훅 템플릿에서 번역 지원을 검증하는 두 가지 방법이 있습니다.

- 작성 중(출시 전)
- 출시 후(출시 후 초안 사용)

번역 업데이트를 테스트하기 전에 다음을 수행해야 합니다.

1. [로케일을 추가]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings#add-a-locale)합니다.
2. 메시지를 작성하고 적절한 위치에 번역 태그를 사용합니다.
3. 메시지를 저장합니다.
4. 포함할 로케일을 선택합니다.