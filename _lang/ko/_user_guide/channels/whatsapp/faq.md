---
nav_title: FAQ
article_title: FAQ
page_order: 30
description: "이 문서에서는 WhatsApp Campaign을 설정할 때 가장 자주 묻는 질문에 대한 답변을 제공합니다."
page_type: FAQ
channel:
  - WhatsApp

---

# 자주 묻는 질문 {#frequently-asked-questions}

> 이 페이지에서는 WhatsApp에 대한 가장 중요한 질문에 답변합니다!<br><br>이 FAQ는 법률 자문을 제공하거나 법률 자문으로 의존할 수 있는 것이 아닙니다. WhatsApp 채널의 사용은 Meta Platforms, Inc.의 특정 요구 사항을 따릅니다. 모든 관련 요구 사항 및 귀하에게 특별히 적용될 수 있는 법률을 준수하여 WhatsApp 채널을 사용하고 있는지 확인하려면 법률 고문의 조언을 구해야 합니다.

## FAQ 주제 {#faq-topics}
- [WhatsApp 비즈니스 계정](#whatsapp-business-accounts)
- [WhatsApp 비즈니스 계정 전화번호](#whatsapp-business-account-phone-numbers)
- [옵트인 및 구독 관리](#opt-in-and-subscription-management)
- [메시징 한도](#messaging-limits)
- [WhatsApp 템플릿](#whatsapp-templates)
- [전달 가능성](#deliverability)
- [기타](#miscellaneous)

### WhatsApp 비즈니스 계정 {#whatsapp-business-accounts}

#### WhatsApp 비즈니스 계정은 어떻게 만드나요? {#how-do-i-create-a-whatsapp-business-account}
Braze 대시보드의 임베디드 가입 플로우를 통해 WhatsApp 비즈니스 계정(WABA)을 만드는 것을 권장합니다.

#### 이미 Meta 비즈니스 계정이 있습니다. WhatsApp 비즈니스 계정도 필요한가요? {#i-already-have-a-meta-business-account-do-i-still-need-a-whatsapp-business-account}
네, WhatsApp 비즈니스 계정을 별도로 만들어야 합니다. [기본 Meta 비즈니스 계정 아래에 WABA를 중첩]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/)하는 것을 권장합니다.

#### WhatsApp 비즈니스 계정에 어떻게 접근하나요? {#how-do-i-access-my-whatsapp-business-account}
임베디드 가입 플로우를 완료한 후 business.facebook.com에서 [WhatsApp 섹션](https://business.facebook.com/wa/manage/home)으로 이동하여 계정에 접근할 수 있습니다.

#### 여러 WABA를 Braze에 연결할 수 있나요? {#can-i-connect-multiple-wabas-to-braze}
네, 워크스페이스당 최대 10개의 WhatsApp 비즈니스 계정을 추가할 수 있으며, 각 비즈니스 계정은 서로 다른 Meta Business Manager 아래에 중첩될 수 있습니다.

![Braze와 WhatsApp 에코시스템의 다이어그램으로, 워크스페이스와 WhatsApp 비즈니스 계정이 서로 어떻게 연결되는지 보여줍니다: 하나의 구독 그룹을 하나의 전화번호에, 여러 WhatsApp 비즈니스 계정을 하나의 워크스페이스에, 하나의 워크스페이스를 여러 Meta Business Portfolio에 연결할 수 있습니다.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %})

#### WhatsApp 비즈니스 계정의 통화를 변경할 수 있나요? {#can-i-change-my-whatsapp-business-account-currency}
아니요. Meta가 WhatsApp 비즈니스 계정의 통화를 관리하며, Braze는 이를 변경하거나 전환할 수 없습니다. 다른 통화를 사용하려면 해당 통화로 [별도의 WhatsApp 비즈니스 계정을 생성]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/)하거나, Meta 지원팀에 연락하여 기존 계정의 통화를 업데이트할 수 있는지 문의하세요.

### WhatsApp 비즈니스 계정 전화번호 {#whatsapp-business-account-phone-numbers}

#### WhatsApp 비즈니스 계정에 전화번호가 필요한가요? {#do-i-need-a-phone-number-for-my-whatsapp-business-account}
네, 접근 가능한 번호가 필요합니다. 임베디드 가입 플로우를 진행할 때 2단계 인증으로 전화번호를 확인하게 됩니다. 이 전화번호는 다른 WhatsApp 계정(비즈니스 또는 개인)에서 사용할 수 없습니다.

#### WhatsApp에서 지원하는 전화번호 유형은 무엇인가요? {#what-types-of-phone-numbers-are-supported-with-whatsapp}
자세한 내용은 Meta의 [전화번호](https://developers.facebook.com/docs/whatsapp/phone-numbers) 요구 사항을 참조하세요.

#### 하나의 전화번호를 여러 WABA에서 사용할 수 있나요? {#can-i-use-one-phone-number-across-multiple-wabas}
아니요. 전화번호는 여러 WABA 간에 공유할 수 없습니다.

#### 특정 국가에 메시지를 보내려면 특정 유형의 전화번호가 필요한가요? {#do-i-need-a-specific-type-of-phone-number-to-send-messages-to-specific-countries}
아니요. WhatsApp에서는 지원되는 모든 전화번호에서 모든 국가의 최종 사용자에게 메시지를 보낼 수 있습니다. 자세한 내용은 Meta의 [전화번호](https://developers.facebook.com/docs/whatsapp/phone-numbers) 요구 사항을 참조하세요.

#### 특정 국가에 발송하려면 해당 국가의 전화번호를 사용해야 하나요? {#do-i-need-to-use-a-country-specific-phone-number-to-send-to-certain-countries}
아니요. WhatsApp에서는 지원되는 모든 전화번호로 지원되는 모든 국가의 최종 사용자에게 발송할 수 있습니다.

### 옵트인 및 구독 관리 {#opt-in-and-subscription-management}

#### WhatsApp에서 최종 사용자에게 마케팅 메시지를 보내려면 옵트인을 수집해야 하나요? {#do-i-need-to-collect-opt-in-to-send-marketing-messages-to-end-users-on-whatsapp}
네, WhatsApp은 비즈니스가 최종 사용자에게 마케팅 메시지를 보내기 위해 [옵트인 동의를 수집](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)하도록 요구합니다.

#### 옵트인 동의를 수집하기 위해 WhatsApp에서 최종 사용자에게 먼저 메시지를 보낼 수 있나요? {#can-i-proactively-message-end-users-on-whatsapp-to-collect-opt-in-consent}
최종 사용자에게 먼저 메시지를 보내기로 선택한 경우, 첫 번째 비즈니스 시작 메시지에서 사용자가 귀하의 비즈니스로부터 마케팅 메시지를 수신할 의향이 있는지 물어야 하며, Meta의 [옵트인 수집](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) 요구 사항을 준수해야 합니다. WhatsApp은 채널에서 귀하의 비즈니스 평판을 모니터링하므로, 최종 사용자에게 명확하게 안내하고 수신을 원한다고 표시한 메시지만 보내는 것이 권장 모범 사례입니다.

#### 옵트인을 수집할 때 최종 사용자의 전화번호도 수집해야 하나요? {#do-i-need-to-collect-the-end-users-phone-number-when-i-collect-opt-in}
메시지를 보내려면 Braze 프로필에 최종 사용자의 전화번호가 있어야 합니다.
- 이미 번호를 보유하고 있다면 옵트인 시 별도로 수집할 필요가 없습니다.
- 최종 사용자의 번호가 없다면 옵트인 방법에 전화번호 수집이 포함되어야 합니다.

#### 옵트인한 최종 사용자의 구독 상태는 어떻게 업데이트하나요? {#how-do-i-update-the-subscription-status-of-end-users-who-opt-in}
WhatsApp 채널의 구독 관리는 다른 Braze 채널과 유사하게 작동합니다. 자세한 내용은 [사용자 구독 관리]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups/)를 참조하세요.

#### WhatsApp에서 마케팅 메시지 수신에 옵트인한 사용자 목록이 이미 있는 경우, Braze에서 구독 상태를 어떻게 업데이트하나요? {#if-i-already-have-a-list-of-users-who-have-opted-in-to-receive-marketing-messages-on-whatsapp-how-do-i-update-their-subscription-status-in-braze}
[사용자 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/#importing-custom-data)를 통해 구독 상태를 업데이트할 수 있습니다.

#### 옵트인을 수집하려면 어떤 방법을 사용해야 하나요? {#what-methods-should-i-use-to-collect-opt-ins}
Braze는 규정 준수를 유지하기 위해 [Meta의 옵트인 방법 가이드라인](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)을 참조할 것을 권장합니다. Braze [채널 및 옵트인 아이디어와 제안](https://docs.google.com/document/d/1rNKnKN2oIn-e9bXdYEvnwdlzlCsEOKs-xREcdVvPBE8/edit)에 대한 다음 리소스를 참조하세요.

#### WhatsApp에 이중 옵트인이 필요한가요? {#is-double-opt-in-required-for-whatsapp}
아니요, 이중 옵트인은 필요하지 않습니다.

#### 사용자가 WhatsApp 메시지를 수신 거부하려면 어떻게 하나요? {#how-do-my-users-opt-out-of-whatsapp-messages}
사용자는 두 가지 방법으로 수신 거부할 수 있습니다:
1. 특정 수신 거부 단어가 포함된 인바운드 WhatsApp 메시지를 설정하고 웹훅을 사용하여 사용자 구독 상태를 업데이트합니다.
2. WhatsApp 템플릿 내에 수신 거부 빠른 응답을 추가하고, 해당 웹훅으로 업데이트합니다.

### 메시징 한도 {#messaging-limits}

#### 메시징 한도란 무엇인가요? {#what-are-messaging-limits}
메시징 한도는 WhatsApp 무결성 구축 개념입니다. 각 전화번호가 24시간 롤링 기간 동안 시작할 수 있는 비즈니스 시작 대화의 최대 수를 결정합니다. 메시징 한도 레벨은 1k, 10k, 100k, 무제한의 네 가지가 있습니다.

#### 메시징 한도를 어떻게 늘리나요? {#how-do-i-increase-my-messaging-limit}
다음 조건을 충족하면 WhatsApp이 메시징 한도를 늘려줍니다:
1. [전화번호 상태](https://www.facebook.com/business/help/896873687365001)가 **Connected**인 경우
2. [전화번호 품질 등급](https://www.facebook.com/business/help/896873687365001)이 **Medium** 또는 **High**인 경우
3. 지난 7일 동안 X명 이상의 고유 사용자와 대화를 시작한 경우(X는 현재 메시징 한도를 2로 나눈 값)

따라서 100k에서 무제한으로 올리려면 7일 기간 동안 최소 50,000건의 비즈니스 시작 대화를 보내야 합니다.

#### 메시징 한도를 늘리는 데 얼마나 걸리나요? {#how-long-does-it-take-to-increase-my-messaging-limits}
위의 모든 조건이 충족되면 4일 만에 메시징 한도를 1k에서 무제한으로 늘릴 수 있습니다.

#### 현재 메시징 한도는 어디에서 확인할 수 있나요? {#where-can-i-see-my-current-messaging-limit}
**WhatsApp Manager > Overview Dashboard > Insights** 탭에서 현재 메시징 한도를 확인할 수 있습니다.

#### 이미 메시징 한도에 도달한 상태에서 메시지를 보내려고 하면 어떻게 되나요? {#what-happens-if-i-attempt-to-send-messages-when-i-have-already-reached-my-messaging-limit}
현재 한도가 허용하는 것보다 더 많은 고유 사용자에게 Campaign이나 Canvas를 보내려고 하면 메시지 발송에 실패합니다. Braze는 메시징 한도가 증가할 경우 최대 1일 동안 메시지 재발송을 계속 시도합니다.

#### 메시징 한도가 줄어들 수 있나요? {#can-my-messaging-limit-decrease}
네, 전화번호 품질 등급이 너무 낮아지면 WhatsApp이 메시징 한도를 줄일 위험이 있습니다. Braze는 전화번호 상태 및 메시징 한도 레벨 업데이트를 포함하여 WhatsApp의 품질 관련 업데이트에 대한 알림을 구독하고 받을 것을 권장합니다. WhatsApp Manager 대시보드에서 직접 알림을 구독할 수 있습니다.

#### Meta 처리량 한도란 무엇인가요? {#what-is-the-meta-throughput-limit}
Meta는 WABA 메시징 한도와 별도로 자체 처리량 한도를 가지고 있습니다. 클라우드 API가 지원하는 기본 한도는 초당 80개 메시지입니다. Campaign이 이 한도를 초과할 것으로 예상되면 한도 증가를 [요청](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/#throughput)할 수 있습니다. Meta는 Campaign 발송 최소 3일 전에 이 요청을 제출할 것을 권장합니다.

### WhatsApp 템플릿 {#whatsapp-templates}

#### WhatsApp 템플릿이란 무엇인가요? {#what-is-a-whatsapp-template}
WhatsApp은 모든 비즈니스 시작 메시지가 승인된 템플릿을 사용하여 시작하도록 요구합니다. 템플릿에는 메시지 문구와 함께 이미지, 행동 유도 버튼, 빠른 응답 버튼과 같은 선택적 리치 미디어가 포함됩니다. WhatsApp이 템플릿을 승인하면 Braze에서 WhatsApp 메시지를 작성하는 데 사용할 수 있습니다.

#### WhatsApp 템플릿은 어디에서 생성, 편집, 관리하나요? {#where-do-i-create-edit-and-manage-my-whatsapp-templates}
WhatsApp Manager에서 직접 템플릿을 생성, 편집, 관리하고 승인을 위해 제출합니다. WABA가 Braze에 연결되면 대시보드에서 상태 표시기와 함께 모든 템플릿을 볼 수 있습니다. 템플릿이 거부된 경우 WhatsApp Manager를 통해 직접 다시 제출합니다. **템플릿은 Braze에서 직접 생성하거나 편집할 수 없습니다.**

#### WhatsApp이 템플릿 제출을 검토하는 데 얼마나 걸리나요? {#how-long-does-it-take-whatsapp-to-review-a-template-submission}
승인 프로세스는 최대 24시간이 걸릴 수 있지만, 대부분의 템플릿은 몇 시간 또는 몇 분 내에 처리됩니다.

#### 한 번에 몇 개의 템플릿을 가질 수 있나요? {#how-many-templates-can-i-have-at-a-given-time}
메시지 템플릿 한도는 비즈니스 인증 상태에 따라 다릅니다. **WhatsApp Manager > Message Templates** 페이지에서 한도를 확인할 수 있습니다.

#### Braze에서 템플릿 문구와 리치 미디어를 어떻게 개인화하나요? {#how-do-i-personalize-template-copy-and-rich-media-in-braze}
WhatsApp은 메시지 템플릿에 변수 매개변수를 삽입할 수 있도록 허용합니다. 메시지는 변수 매개변수로 시작하거나 끝날 수 없습니다. 변수 매개변수는 Braze 플랫폼에서 Liquid 로직으로 채울 수 있습니다. 변수 매개변수에 대해 자세히 알아보려면 [Braze에서 WhatsApp 메시지 작성]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/#step-2-compose-your-whatsapp-message)을 참조하세요.

#### 템플릿이 거부되었습니다. Braze가 승인받는 데 도움을 줄 수 있나요? {#my-template-got-rejected-can-braze-help-me-get-it-approved}
Braze 팀은 템플릿 거부에 대한 가시성이 없습니다. WhatsApp Business Manager에서 직접 작업하여 템플릿을 편집하고 다시 제출해야 합니다. 필요한 경우 샘플 템플릿을 제공해야 합니다. 템플릿이 Meta의 [비즈니스](https://www.whatsapp.com/legal/business-policy/?fbclid=IwAR2qWg6yFKdyjDMxJkbNSM38FLGsxXxffC1qStY2gaHOyp-gl_8g72rZNIw) 또는 [커머스](https://www.whatsapp.com/legal/commerce-policy/?fbclid=IwAR3bzN3LTZ-7kO-wnO7X3smtPKGy0asxaFod-U1Ub8B9JUpnrfy1_y7LpAQ) 정책을 준수하는지 다시 확인하세요.

#### Braze에서 리치 미디어를 타겟팅하거나 개인화할 수 있나요? {#can-the-rich-media-be-targeted-or-personalized-in-braze}
이미지는 미디어 라이브러리에서 업로드할 수 있지만 동적으로 타겟팅할 수는 없습니다. URL의 경우 링크의 마지막 부분을 [Liquid를 사용하여 동적으로 채울]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/#use-liquid-personalization-in-urls) 수 있습니다.

### 전달 가능성 {#deliverability}

#### 메시지가 전달되지 않는 이유는 무엇인가요? {#why-would-a-message-not-be-delivered}
네트워크 문제 및 기기 전원 꺼짐 등 메시지가 전달되지 않는 다양한 이유가 있습니다.

#### 메시지가 전달되지 않으면 요금이 청구되나요? {#if-a-message-is-not-delivered-will-i-be-billed}
아니요. 메시지가 전달되지 않으면 요금이 청구되지 않습니다.

#### 최종 사용자가 내 비즈니스를 차단하면 어떻게 되나요? {#what-happens-if-an-end-user-blocks-my-business}
최종 사용자가 귀하의 비즈니스를 차단하면 이후 보내려는 메시지가 전달되지 않으며 요금도 청구되지 않습니다.

#### 최종 사용자가 메시지를 신고하면 어떻게 되나요? {#what-happens-if-an-end-user-reports-a-message}
최종 사용자가 메시지를 신고해도 이후 해당 사용자에게 메시지를 보낼 수 있습니다. 그러나 신고는 채널에서의 품질 등급에 영향을 줄 수 있습니다.

#### 최종 사용자가 내 비즈니스를 차단하거나 신고하면 Braze에서 구독 상태가 업데이트되나요? {#if-an-end-user-blocks-or-reports-my-business-will-their-subscription-status-be-updated-in-braze}
아니요. Braze 구독 상태는 업데이트되지 않습니다.

### 기타 {#miscellaneous}

#### Braze는 WhatsApp에 대한 챗봇이나 상담원 지원 채팅과 같은 고객 지원 사용 사례를 지원하나요? {#does-braze-support-customer-support-use-cases-like-chatbots-and-human-assisted-chat-for-whatsapp}
Braze 내에서 또는 직접 통합을 통한 챗봇이나 상담원 지원 채팅은 지원하지 않습니다.

이미 WhatsApp을 고객 지원 채널로 사용하고 있다면 현재 설정을 유지하고 마케팅 메시징을 위해 Braze를 통해 새 WABA를 만드는 것을 권장합니다. 이 WABA에는 새 전화번호가 필요합니다.

#### 고객 지원 메시징과 Braze를 통한 마케팅 메시징 간의 "격차를 해소"하려면 어떻게 하나요? {#how-can-i-bridge-the-gap-between-my-customer-support-messaging-and-my-marketing-messaging-via-braze}
WhatsApp Liquid 속성을 사용하여 인바운드 WhatsApp 메시지 콘텐츠(메시지 본문 및 미디어 URL 포함)를 Braze에서 고객 지원 도구를 포함한 다른 플랫폼으로 전달할 수 있습니다. 자세한 내용은 [지원되는 개인화 태그]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/)를 참조하세요.

Braze로 정보를 보내려면, 예를 들어 사용자가 활성 지원 대화 중임을 나타내기 위해 커스텀 속성(예: 부울 "has existing support chat = true/false")을 기록하고 마케팅 Campaign에서 세분화 기준으로 사용할 수 있습니다. 또한 두 채팅 스레드 간에 딥링크를 설정하여 마케팅 스레드에서 지원 스레드로, 그리고 반대로 사용자를 안내할 수 있습니다.

#### Braze는 사용자 응답을 저장하나요? {#does-braze-store-user-responses}
메시지는 처리하는 데 필요한 시간 동안만 저장됩니다. 사용자 메시지에 접근하려면 Currents를 사용하세요.

#### 사용자 전화번호는 Braze에 어떤 형식으로 저장해야 하나요? {#how-do-user-phone-numbers-need-to-be-stored-in-braze}
사용자 전화번호는 [E.164 형식]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers/#formatting)으로 저장해야 합니다.

#### WhatsApp 템플릿에서 지원되는 리치 미디어 유형은 무엇인가요? {#what-kind-of-rich-media-is-supported-in-whatsapp-templates}
WhatsApp 템플릿에 이미지, 행동 유도(URL 또는 전화번호), 빠른 응답 버튼을 추가할 수 있습니다. WhatsApp에서 직접 템플릿을 만들 때 이러한 요소를 추가할 수 있습니다.

#### 사용자 전화번호를 가져올 수 있나요? {#can-i-import-user-phone-numbers}
네. [사용자 전화번호를 가져올]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers/) 수 있습니다.

#### 비즈니스 인증이란 무엇인가요? {#what-is-business-verification}
비즈니스 인증은 브랜드가 합법적인 비즈니스임을 확인하는 데 사용되는 WhatsApp 개념입니다. WhatsApp Manager에서 완료할 수 있습니다. 비즈니스 인증은 메시징을 확장하는 데에도 필요합니다. 비즈니스 인증 없이는 고객이 24시간 롤링 기간 동안 최대 250명의 고유 최종 사용자에게만 발송할 수 있습니다.

#### 공식 비즈니스 계정이란 무엇인가요? {#what-is-an-official-business-account}
OBA는 표시 이름 옆에 녹색 체크 표시를 제공하며 선택 사항입니다. 비즈니스 인증을 완료한 후 공식 비즈니스 계정을 신청할 수 있습니다. 비즈니스 인증과 공식 비즈니스 계정은 서로 다른 WhatsApp 개념입니다.

#### Braze 대시보드에서 어떤 측정기준을 사용할 수 있나요? {#what-metrics-are-available-in-the-braze-dashboard}
Braze 대시보드에서 고유 수신자, 발송, 전달, 읽음, 실패를 확인할 수 있습니다. Braze가 읽음을 추적하려면 최종 사용자의 읽음 확인이 "켜짐"으로 설정되어 있어야 합니다. 다른 채널과 유사하게 전환 이벤트를 설정하여 Campaign 성과를 모니터링할 수도 있습니다.

#### WhatsApp 대화란 무엇인가요? {#what-is-a-whatsapp-conversation}
WhatsApp은 양방향 메시징에 중점을 둔 채널이므로 개별 메시지 수가 아닌 대화를 기준으로 합니다. 대화는 비즈니스와 최종 사용자 간의 24시간 스레드입니다.

- **비즈니스 시작 대화**: 비즈니스가 최종 사용자에게 승인된 템플릿 메시지를 보내면서 시작하는 대화입니다. 비즈니스가 메시지를 보내는 즉시 24시간 기간이 시작됩니다.
- **사용자 시작 대화**: 최종 사용자가 비즈니스에 메시지를 보내면서 시작하는 대화입니다. 비즈니스가 응답 메시지를 보내면 24시간 기간이 시작됩니다.

#### 전화번호 품질 등급에 영향을 미치는 요인은 무엇이며, 품질 등급이 너무 낮아지면 어떻게 되나요? {#what-factors-affect-phone-number-quality-rating-and-what-happens-when-my-quality-rating-drops-too-low}
전화번호 품질 등급에 영향을 미치는 요인에는 최종 사용자가 비즈니스를 차단하는 것(및 차단 시 제공하는 이유)과 최종 사용자가 비즈니스를 신고하는 것이 포함됩니다.

품질 등급이 낮으면 전화번호 상태가 **Connected**에서 **Flagged**로 변경됩니다. 7일 동안 품질이 개선되지 않으면 상태는 **Connected**로 돌아갑니다. 그러나 메시징 한도는 다음 레벨로 감소합니다. 예를 들어, 이전에 100,000 메시징 한도를 가졌던 전화번호는 이제 10,000 메시징 한도를 갖게 됩니다.

#### 템플릿이 WhatsApp의 커머스 정책 위반으로 잘못 플래그된 경우 어떻게 하나요? {#what-if-my-template-was-falsely-flagged-for-violating-whatsapps-commerce-policy}

Meta가 템플릿을 잘못 플래그했다고 판단되면 WhatsApp에서 보낸 이메일의 검토 링크를 사용하여 재검토를 요청하세요. WhatsApp Business 팀이 결정을 검토하고 적절한 경우 이를 번복합니다.