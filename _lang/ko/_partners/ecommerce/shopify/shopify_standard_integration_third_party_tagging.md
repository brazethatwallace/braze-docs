---
nav_title: 타사 태그와 Shopify 표준 통합
article_title: 타사 태그와 Shopify 표준 통합
description: "이 참조 문서에서는 타사 태그 도구를 사용하여 표준 Shopify 통합을 설정하는 방법을 설명합니다."
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration_third_party_tagging/
page_order: 2
---

# 타사 태그 도구와 Shopify 표준 통합 {#shopify-standard-integration-with-third-party-tagging-tool}

> 이 페이지에서는 Google Tag Manager와 같은 타사 도구를 [Shopify 표준 통합]({{site.baseurl}}/shopify_standard_integration/)과 함께 사용하여 Braze 웹 SDK를 초기화하고 로드하는 방법을 안내합니다.

Shopify 온라인 스토어의 경우 Braze의 표준 통합 방법을 사용하여 사이트에서 Braze SDK를 지원하는 것을 권장합니다. 그러나 Google Tag Manager와 같은 타사 도구를 사용하는 것을 선호할 수 있다는 점을 이해합니다. 타사 도구를 Braze의 Shopify 커넥터와 함께 사용하기로 선택한 경우, 결제 프로세스 중에는 Braze 통합 및 앱 임베드가 SDK를 관리한다는 점에 유의하세요.

## 요구 사항 {#requirements}

- **타사 도구와 Shopify 커넥터 간의 일관된 API 키:** API 키는 Braze와 타사 도구 모두에서 일관되어야 합니다. 이를 통해 중복 사용자 생성을 방지하고 SDK 간 호환성을 유지할 수 있습니다.
  - **API 키 위치:** 표준 통합 경로를 온보딩하면 통합에서 자동으로 "Shopify"라는 이름의 Braze 웹 앱이 생성됩니다. 타사 도구 구성에 사용되는 API 키를 통합 내에서 확인하세요.
- **타사 도구와 Shopify 커넥터 간의 일관된 SDK 버전:** 타사 도구 내에서 SDK 버전은 `5.4`여야 합니다. 잘못된 버전 번호를 사용하면 일부 SDK 메서드가 이전 버전에 존재하지 않을 수 있으므로 호환성 문제가 발생할 수 있습니다.
- **일관된 SDK 초기화 타이밍:** Shopify 표준 통합 설정에서 세션 시작 시 또는 계정 로그인 시 초기화할 SDK를 선택할 수 있습니다. 이 설정은 타사 도구와 Braze 간에 일관되어야 합니다. 불일치가 있으면 사용자 및 데이터 동기화에 다운스트림 문제가 발생할 수 있습니다.

{% alert note %}
타사 태그 매니저와 함께 사용하기보다는 표준 통합 방법을 단독으로 사용하는 것을 권장합니다. 함께 사용하면 Braze SDK와 타사 도구 간에 충돌이 발생할 수 있습니다. 타사 도구를 사용하는 경우 모든 것이 예상대로 작동하는지 테스트하여 확인하세요.
{% endalert %}

## 타사 도구와 통합 설정하기 {#setting-up-the-integration-with-a-third-party-tool}

제공된 단계를 벗어나면 예기치 않은 문제가 발생할 수 있으므로 단계를 주의 깊게 따르세요.

1. [Shopify 표준 통합 설정]({{site.baseurl}}/shopify_standard_integration/)에서 제공된 단계를 따릅니다. [Braze 웹 SDK 활성화]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/#step-2-enable-braze-web-sdks) 과정에서 타사 도구를 사용하여 Shopify 사이트에 Braze 웹 SDK를 추가할 것임을 나타내는 확인란을 선택합니다.

!["Braze SDK 설정" 섹션에 타사 도구를 사용하여 Braze 웹 SDK를 추가할 것임을 나타내는 확인란이 있습니다.]({% image_buster /assets/img/shopify/third_party_enable.png %}){: style="max-width:80%;"}

{: start="2"}
2. **설정** > **앱 설정**으로 이동하여 **Shopify** 웹 앱을 선택한 다음 **API key for Shopify on Web**을 복사합니다.
3. 타사 도구의 웹 SDK 구성에 API 키를 붙여넣고 SDK 버전을 `5.4`로 설정합니다.

## Shopify 데이터 캡처 및 사용자 동기화 {#capturing-shopify-data-and-syncing-users}

타사 도구를 통해 Shopify 사이트의 프런트엔드에서 웹 SDK에 액세스할 수 있는 한, 표준 통합은 예상대로 Shopify 데이터를 캡처하고 사용자를 동기화합니다.

## 고려 사항 및 면책 조항 {#considerations-and-disclaimers}

- **초기화 설정:** 타사 도구를 통해 초기화 설정을 수정하면 사용자 및 데이터 동기화에 영향을 미칠 수 있습니다. 예를 들어, 쿠키 동의 양식이 수락될 때 SDK를 초기화하도록 선택하면 사용자가 동의할 때까지 Braze는 익명 사용자에 대한 추적이나 데이터를 수신하지 않습니다.
- **`dataLayer`를 통해 직접 속성을 설정하는 것은 지원되지 않습니다:** 속성을 설정하려면 `dataLayer` 대신 `window.braze`를 사용하세요.
- **잠재적 중복 사용자:** API 키가 Braze와 타사 도구 간에 일치하지 않으면 중복 사용자가 생성될 수 있습니다.
- **SDK 비호환성:** 잘못된 버전 번호를 사용하면 SDK 메서드에 문제가 발생할 수 있습니다.