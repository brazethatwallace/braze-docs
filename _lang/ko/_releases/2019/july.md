---
nav_title: 7월
page_order: 6
noindex: true
page_type: update
description: "이 문서에는 2019년 7월의 릴리스 노트가 포함되어 있습니다."
---

# 2019년 7월 {#july-2019}

{% alert update %}
이번 달에는 Braze의 제품 출시 주기가 두 번(맞습니다. **두 번**) 있었습니다! 최신 릴리스는 상단에 표시되며, 이전 릴리스는 [이달 초](#earlier-this-month) 섹션에서 확인할 수 있습니다!
{% endalert %}

## SAML/SSO

[SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on)(싱글 사인온)를 통해 기업들은 Braze 대시보드에 대한 액세스를 안전하고 중앙 집중화된 방식으로 제어할 수 있습니다. 즉, 하나의 자격 증명 세트를 사용하여 Braze를 포함한 다양한 애플리케이션에 액세스할 수 있습니다.

[OAuth 2.0 지원을 사용하는 Google 로그인](https://developers.google.com/identity/protocols/OAuth2) 외에도 기업들은 SAML(Security Assertion Markup Language)이 지원되는 SSO를 원합니다. 이를 통해 최신 업계 표준(SAML 2.0)을 지원하는 [Azure 액티브 디렉토리]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso) 및 [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta)를 비롯한 대규모 ID 공급자(IdP)와 원활하게 통합할 수 있습니다.

Braze는 다음을 지원합니다:
- [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin)
- [Azure 액티브 디렉토리]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso)
- [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta)

## Adjust 이벤트 API 키 표시 {#adjust-event-api-key-shows}

고객이 이 API 키에 액세스할 수 있도록 Adjust의 파트너 페이지를 업데이트했습니다.

## 새로운 파트너 {#new-partners}

새로운 파트너가 Alloys 프로그램에 합류하여 문서에 추가되었습니다! 신규 파트너 목록:
- [FiveTran]({{site.baseurl}}/partners/fivetran)
- [Talon.One]({{site.baseurl}}/partners/talonone)
- [Voucherify]({{site.baseurl}}/partners/voucherify)

## Campaign 세부 정보 개선 {#campaign-details-improvement}

확장된 Campaign 세부 정보는 이제 **Campaign** 페이지의 ...잠깐만...**Campaign Details** 섹션에 표시됩니다!

## Segments 및 Canvas에 내 항목만 보기 {#show-only-mine-in-segments-canvas}

**Campaigns** 페이지의 "내 항목만 보기" 확인 필터는 큰 인기를 얻고 있습니다. 따라서 Canvas 및 Segment 목록에도 이 옵션을 추가합니다!

### 진행 동작 {#advancement-behavior}

이제 [사용자가 한 캔버스 단계에서 다음 단계로 넘어갈 시점]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases)을 선택할 수 있습니다. 이러한 옵션에는 "Message Sent" 및 "Entire Audience After Delay"가 포함됩니다.

### Canvas의 인앱 메시지 {#in-app-messages-in-canvas}

이제 Canvas에서 [인앱 메시지]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas)를 사용할 수 있습니다! 캔버스 단계를 추가하고 사용 가능한 채널을 탐색하여 인앱 메시지를 추가하세요.

# 이달 초 {#earlier-this-month}

## 사용자 프로필 이미지 제거 {#user-profile-image-removal}

Braze 고객 프로필과 사용자 검색에 표시되는 사용자 프로필 사진을 삭제합니다.

## Content Cards의 연결된 콘텐츠 {#connected-content-in-content-cards}

이제 [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)에서 [연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content#about-connected-content) 문자열과 기능을 사용할 수 있습니다.

외부 서버에 대한 연결된 콘텐츠 호출은 사용자가 카드를 볼 때가 아니라 실제로 카드가 전송될 때 발생합니다. 이메일과 마찬가지로 동적 콘텐츠는 카드가 실제로 조회되는 시점이 아니라 전송 시점에 계산되고 결정됩니다.

## "회신 주소" null 설정 {#null-reply-to-address}

이제 고객은 Braze의 **이메일 설정** 페이지 또는 [API]({{site.baseurl}}/api/objects_filters/messaging/email_object)를 사용하여 이메일 메시지의 "회신 주소"로 `null` 값을 설정할 수 있습니다. 사용 시 답장은 나열된 "보낸 사람" 주소로 전송됩니다. 이제 "보낸 사람" 주소 필드를 `dan@emailaddress.com`으로 개인화할 수 있으며, 고객은 Dan에게 직접 답장할 수 있습니다.

Braze에서 이메일 메시지의 "회신 주소"로 `null` 값을 설정하려면 탐색 메뉴에서 **설정 관리**로 이동한 다음 **이메일 설정** 탭으로 이동합니다. **Outbound Email Settings** 섹션으로 스크롤하여 **Exclude "Reply-To" and send replies to "From"**을 기본 주소로 선택합니다.

## Campaign 비교 {#campaign-comparisons}

하나의 창에서 [여러 Campaign을 한 번에 확인하여 상대적인 성과를]({{site.baseurl}}/report_builder) Braze에서 나란히 비교해 보세요!

## Liquid를 사용하여 발송 ID를 메시지로 템플릿화 {#template-dispatch-id-into-messages-with-liquid}

{% alert note %}
`dispatch_id`에 대한 동작은 Canvas와 Campaigns 간에 다르며, 이는 Braze가 캔버스 단계(스케줄 가능한 엔트리 단계 제외)를 "스케줄됨"인 경우에도 트리거된 이벤트로 취급하기 때문입니다. Canvases와 Campaigns의 [`dispatch_id` 동작]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id)에 대해 자세히 알아보세요.
{% endalert %}

메시지 내에서 메시지 발송을 추적하려면(예: URL) `dispatch_id`를 템플릿으로 사용할 수 있습니다. [Canvas Attributes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) 아래의 지원되는 개인화 태그 목록에서 이에 대한 서식을 찾을 수 있습니다.

Campaign 생성 시 `api_id`를 사용할 수 없으므로 입력 안내로 템플릿이 지정되고 `dispatch_id_for_unsent_campaign`으로 미리보기된다는 점에서 `api_id`와 동일하게 작동합니다. ID는 메시지가 전송되기 전에 생성되며 전송 시점에 포함됩니다.

{% alert warning %}
인앱 메시지에는 `dispatch_id`가 없으므로 `dispatch_id_for_unsent_campaign`의 Liquid 템플릿은 인앱 메시지에서 작동하지 않습니다.
{% endalert %}

## "내 항목만 보기" 설정 유지 {#show-only-mine-setting-persists}

Campaigns 그리드의 "내 항목만 보기" 필터는 **Campaigns** 페이지를 방문할 때마다 그대로 유지됩니다.

## A/B 테스트 업데이트 {#ab-testing-updates}

최대 8개의 배리언트(및 선택 사항인 컨트롤)가 포함된 일회성 [A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing)를 사용자가 지정한 Campaign 오디언스의 비율로 전송한 다음, 미리 스케줄된 시간에 나머지 오디언스에게 최적의 배리언트를 전송할 수 있습니다.