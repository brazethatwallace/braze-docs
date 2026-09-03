---
nav_title: 랜딩 페이지
article_title: 랜딩 페이지
page_order: 8
guide_top_header: "랜딩 페이지"
description: "이 문서에는 Braze 랜딩 페이지를 구축하고 커스터마이즈하는 데 필요한 리소스가 포함되어 있습니다."
alias: /landing_pages/
---

# 랜딩 페이지 소개 {#about-landing-pages}

> Braze 랜딩 페이지는 사용자 확보 및 인게이지먼트 전략을 추진할 수 있는 독립형 웹 페이지입니다.

랜딩 페이지를 사용하여 오디언스를 확대하고, 사용자 데이터를 수집하고, 특별 혜택을 홍보하고, 멀티채널 Campaign을 지원하세요. 랜딩 페이지 드래그 앤 드롭 블록에 대한 참조는 [편집기 블록(랜딩 페이지)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages)을 확인하세요.

{% alert note %}
랜딩 페이지 및 커스텀 도메인 사용 가능 여부는 Braze 패키지에 따라 다릅니다. 시작하려면 계정 매니저 또는 고객 성공 매니저에게 문의하세요.
{% endalert %}

{% multi_lang_include video.html id="eg4r7agod1" source="wistia" %}

## 전제 조건 {#prerequisites}

랜딩 페이지에 접근하고, 만들고, 게시하려면 관리자 [권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions)이 있거나 다음 권한이 모두 필요합니다:

- View Landing Pages
- Edit Landing Page Drafts
- Publish Landing Pages

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## 플랜 등급 {#plan-tiers}

게시할 수 있는 랜딩 페이지 수, 커스텀 도메인 수 및 사용할 수 있는 기능은 플랜 유형(무료 또는 프로(증분))에 따라 다릅니다.

| 기능                                                                                                   | 무료 등급     | 프로 등급(증분)     |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| 게시된 랜딩 페이지                                                                 | 회사당 5개 | 추가 20개 |
| 커스텀 도메인          | 회사당 1개 | 추가 5개 |
| [Liquid 개인화]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages) | 사용 불가 | 사용 가능 |
| 미리 채워진 폼 필드 | 사용 불가 | 사용 가능 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="플랜 등급" }

## 사용량 제한 {#rate-limits}

Braze는 캐시되지 않은 랜딩 페이지에 대해 워크스페이스당 3초당 500건의 요청(초당 약 167건의 요청)의 사용량 제한을 적용합니다. 이 제한은 트래픽이 많은 기간에 시스템 성능과 안정성을 유지하는 데 도움이 됩니다.

캐시된 랜딩 페이지 조회수는 이 제한에 포함되지 않습니다. 캐싱이 트래픽에 미치는 영향에 대한 자세한 내용은 [랜딩 페이지가 대량의 트래픽 시나리오를 처리할 수 있나요?](#can-landing-pages-handle-high-traffic-scenarios)를 참조하세요.

## 랜딩 페이지에 Google Tag 매니저 추가하기 {#adding-google-tag-manager-to-a-landing-page}

랜딩 페이지에 Google Tag 매니저를 추가하려면 드래그 앤 드롭 편집기에서 랜딩 페이지에 **커스텀 코드** 블록을 추가한 다음, 해당 블록에 Tag 매니저 코드를 삽입합니다. 다음 예시와 같이 Tag 매니저 코드 앞에 데이터 레이어를 추가해야 합니다:

```
<script>
window.dataLayer = window.dataLayer || [];
</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXX');</script>
<!-- End Google Tag Manager -->
```

Google Tag 매니저 구현에 대한 자세한 내용은 [Google 설명서](https://developers.google.com/tag-platform/tag-manager/datalayer#installation)를 참조하세요.

## 자주 묻는 질문 {#frequently-asked-questions}

### 랜딩 페이지의 최대 크기는 얼마인가요? {#whats-the-maximum-size-for-landing-pages}

랜딩 페이지 본문 크기는 최대 500 KB입니다.

### 랜딩 페이지가 높은 트래픽 시나리오를 처리할 수 있나요? {#can-landing-pages-handle-high-traffic-scenarios}

네. 개인화되지 않은 랜딩 페이지는 높은 트래픽 시나리오를 효과적으로 처리합니다. 랜딩 페이지가 처음 요청되면 Braze는 Cloudflare를 통해 이를 캐시합니다. 동일한 링크에 대한 후속 요청은 캐시에서 제공되므로 트래픽이 많은 기간에 도움이 됩니다. 이 캐시는 24시간 동안 지속되며, 캐시된 페이지 조회수는 [사용량 제한](#rate-limits)에 포함되지 않습니다.

개인화된 랜딩 페이지는 더 짧은 Cloudflare 캐시를 사용하며 Braze에 대한 캐시되지 않은 요청을 더 많이 생성합니다. 이러한 캐시되지 않은 요청에는 [사용량 제한](#rate-limits)에 설명된 워크스페이스별 사용량 제한이 적용됩니다.

개인화된 페이지의 크기 제한 및 기타 성능 관련 안내 사항은 [개인화 고려 사항]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages#personalization-considerations)을 참조하세요.

### 랜딩 페이지를 게시하기 위한 기술적 요구 사항이 있나요? {#are-there-any-technical-requirements-to-publish-a-landing-page}

아니요, 기술적 요구 사항은 없습니다.

### 랜딩 페이지용 HTML 편집기가 있나요? {#is-there-an-html-editor-for-landing-pages}

네. 드래그 앤 드롭 편집기에서 **커스텀 코드** 블록을 사용하여 HTML을 추가하거나 편집할 수 있습니다. 커스텀 코드에서 Braze SDK와 연동하려면 [랜딩 페이지용 JavaScript 브리지]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge)를 참조하세요. 완전한 커스텀 UI를 랜딩 페이지 폼에 연결하려면 [커스텀 폼 블록 만들기]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks)를 참조하세요.

### 랜딩 페이지에서 iframe을 사용할 수 있나요? {#can-i-use-iframes-on-landing-pages}

네. 드래그 앤 드롭 편집기에서 **커스텀 코드** 블록을 추가하고, 삽입하려는 콘텐츠의 URL이 포함된 iframe 요소를 포함하세요.

삽입된 웹사이트가 콘텐츠 보안 정책(CSP)의 `frame-ancestors` 또는 `X-Frame-Options`를 통해 프레이밍을 제한하는 경우, iframe에서 페이지가 로드되지 않을 수 있습니다. Braze는 이러한 설정을 재정의할 수 없으며, 삽입된 사이트가 랜딩 페이지 도메인을 허용하도록 구성되어야 합니다.

### 랜딩 페이지 내에서 웹훅을 만들 수 있나요? {#can-i-create-a-webhook-inside-a-landing-page}

아니요. 하지만 **랜딩 페이지 폼 제출** 이벤트가 Canvases 또는 웹훅 Campaigns의 트리거 역할을 할 수 있습니다.

- **Canvas:** **랜딩 페이지 폼 제출** 이벤트를 Canvas 진입 트리거로 사용하고 웹훅 단계를 추가합니다.
- **Campaign:** **랜딩 페이지 폼 제출** 이벤트를 사용하여 폼 제출에 따라 트리거합니다.

페이지가 Braze 채널을 통해 전송되지 않은 경우(예: 웹사이트나 광고를 통한 경우), 제출 시 해당 사용자가 이미 Braze에 존재하더라도 새 고객 프로필이 생성될 수 있습니다. 이를 처리하려면 **랜딩 페이지 폼 제출**로 트리거되는 Canvas를 설정하고, [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) 엔드포인트를 호출하는 Braze-to-Braze 웹훅 단계를 추가하여 새 프로필을 기존 프로필과 병합합니다.

`landing_page_url` Liquid 태그를 사용하여 페이지를 공유하면 폼 제출이 기존 고객 프로필에 자동으로 연결됩니다. 그런 다음 랜딩 페이지에서 제출된 사용자 속성을 Liquid를 통해 참조하여 후속 템플릿 작성에 활용할 수 있습니다.