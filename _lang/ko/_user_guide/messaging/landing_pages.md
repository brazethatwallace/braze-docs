---
nav_title: 랜딩 페이지
article_title: 랜딩 페이지
page_order: 8
guide_top_header: "랜딩 페이지"
description: "이 문서에는 Braze 랜딩 페이지를 구축하고 커스터마이징하는 데 필요한 리소스가 포함되어 있습니다."
alias: /landing_pages/
---

# 랜딩 페이지 소개 {#about-landing-pages}

> Braze 랜딩 페이지는 사용자 확보 및 참여 전략을 추진할 수 있는 독립형 웹 페이지입니다.

랜딩 페이지를 사용하여 오디언스를 확대하고, 사용자 데이터를 수집하고, 특별 혜택을 홍보하고, 멀티채널 캠페인을 지원하세요.

{% alert note %}
랜딩 페이지 및 커스텀 도메인 사용 가능 여부는 Braze 패키지에 따라 다릅니다. 시작하려면 계정 매니저 또는 고객 성공 매니저에게 문의하세요.
{% endalert %}

{% multi_lang_include video.html id="eg4r7agod1" source="wistia" %}

## 필수 조건 {#prerequisites}

랜딩 페이지에 액세스하고, 생성하고, 게시하려면 관리자 [권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#list-of-permissions)이 있거나 다음 권한이 모두 필요합니다:

- 랜딩 페이지 보기
- 랜딩 페이지 초안 편집
- 랜딩 페이지 게시

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## 플랜 티어 {#plan-tiers}

게시할 수 있는 랜딩 페이지 및 커스텀 도메인의 수는 플랜 유형(무료 또는 유료(증분))에 따라 다릅니다.

| 기능                                                                                                   | 무료 티어     | 유료 티어(증분)     |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| 게시된 랜딩 페이지                                                                 | 회사당 5개 | 추가 20개 |
| 커스텀 도메인          | 회사당 1개 | 추가 5개 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## 랜딩 페이지에 Google Tag Manager 추가하기 {#adding-google-tag-manager-to-a-landing-page}

랜딩 페이지에 Google Tag Manager를 추가하려면 드래그 앤 드롭 편집기에서 랜딩 페이지에 **커스텀 코드** 블록을 추가한 다음, 블록에 Tag Manager 코드를 삽입합니다. 다음 예시와 같이 Tag Manager 코드 앞에 데이터 레이어를 추가해야 합니다:

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

Google Tag Manager 구현에 대한 자세한 내용은 [Google 설명서](https://developers.google.com/tag-platform/tag-manager/datalayer#installation)를 참조하세요.

## 자주 묻는 질문 {#frequently-asked-questions}

### 랜딩 페이지의 최대 크기는 얼마인가요? {#whats-the-maximum-size-for-landing-pages}

랜딩 페이지 본문 크기는 최대 500KB입니다.

### 랜딩 페이지를 게시하기 위한 기술적 요구 사항이 있나요? {#are-there-any-technical-requirements-to-publish-a-landing-page}

아니요, 기술적 요구 사항은 없습니다.

### 랜딩 페이지용 HTML 편집기가 있나요? {#is-there-an-html-editor-for-landing-pages}

네. 드래그 앤 드롭 편집기에서 **커스텀 코드** 블록을 사용하여 HTML을 추가하거나 편집할 수 있습니다.

### 랜딩 페이지 내에서 웹훅을 생성할 수 있나요? {#can-i-create-a-webhook-inside-a-landing-page}

아니요, 현재 지원되지 않습니다.