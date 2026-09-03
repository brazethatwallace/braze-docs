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
- [메시징 한도 및 품질 등급](#messaging-limits-and-quality-rating)
- [WhatsApp 템플릿 및 작성기](#whatsapp-templates-and-composer)
- [전달 가능성 및 청구](#deliverability-and-billing)
- [통합, 데이터 및 리포트](#integrations-data-and-reporting)
- [미디어 및 이미지](#media-and-images)

### WhatsApp 비즈니스 계정 {#whatsapp-business-accounts}

#### WhatsApp 비즈니스 계정은 어떻게 만드나요? {#how-do-i-create-a-whatsapp-business-account}
Braze 대시보드의 임베디드 가입 플로우를 통해 WhatsApp 비즈니스 계정(WABA)을 만드는 것을 권장합니다.

#### 이미 Meta 비즈니스 계정이 있습니다. WhatsApp 비즈니스 계정이 여전히 필요한가요? {#i-already-have-a-meta-business-account-do-i-still-need-a-whatsapp-business-account}
네, WhatsApp 비즈니스 계정을 별도로 만들어야 합니다. [메인 Meta 비즈니스 계정 하위에 WABA를 연결]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)하는 것을 권장합니다.

#### WhatsApp 비즈니스 계정에 어떻게 접근하나요? {#how-do-i-access-my-whatsapp-business-account}
임베디드 가입 플로우를 완료한 후, business.facebook.com에서 [WhatsApp 섹션](https://business.facebook.com/wa/manage/home)으로 이동하여 계정에 접근할 수 있습니다.

#### 여러 WABA를 Braze에 연결할 수 있나요? {#can-i-connect-multiple-wabas-to-braze}
네, 워크스페이스당 최대 10개의 WhatsApp 비즈니스 계정을 추가할 수 있으며, 각 비즈니스 계정은 서로 다른 Meta Business Manager 하위에 연결할 수 있습니다.

![Braze와 WhatsApp 에코시스템의 다이어그램으로, 워크스페이스와 WhatsApp 비즈니스 계정이 서로 어떻게 연결되는지 보여줍니다. 하나의 구독 그룹을 하나의 전화번호에, 여러 WhatsApp 비즈니스 계정을 하나의 워크스페이스에, 하나의 워크스페이스를 여러 Meta Business Portfolio에 연결할 수 있습니다.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %})

#### WhatsApp 비즈니스 계정의 통화를 변경할 수 있나요? {#can-i-change-my-whatsapp-business-account-currency}
아니요. Meta가 WhatsApp 비즈니스 계정의 통화를 관리하며, Braze에서는 이를 변경하거나 환산할 수 없습니다. 다른 통화를 사용하려면 해당 통화로 [별도의 WhatsApp 비즈니스 계정을 생성]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)하거나, Meta 지원팀에 문의하여 기존 계정의 통화를 업데이트할 수 있는지 확인하세요.

#### 비즈니스 인증이란 무엇인가요? {#what-is-business-verification}
비즈니스 인증은 브랜드가 합법적인 비즈니스인지 확인하기 위해 사용되는 WhatsApp 개념입니다. WhatsApp 매니저에서 완료할 수 있습니다. 비즈니스 인증은 메시징을 확장하기 위해서도 필요합니다. 비즈니스 인증 없이는 고객이 24시간 롤링 기간 동안 최대 250명의 고유 최종 사용자에게만 발송할 수 있습니다.

#### 공식 비즈니스 계정이란 무엇인가요? {#what-is-an-official-business-account}
OBA는 표시 이름 옆에 녹색 체크 마크를 부여하며, 선택 사항입니다. 비즈니스 인증을 완료한 후 공식 비즈니스 계정을 신청할 수 있습니다. 비즈니스 인증과 공식 비즈니스 계정은 서로 다른 WhatsApp 개념입니다.

#### WhatsApp 비즈니스 표시 이름이 거부될 수 있는 이유는 무엇인가요? {#why-might-my-whatsapp-business-display-name-be-rejected}
WhatsApp 비즈니스 표시 이름 거부는 Meta가 관리합니다. 표시 이름이 거부된 경우 [WhatsApp의 표시 이름 가이드라인](https://faq.whatsapp.com/793641088597363)을 참조하세요.

표시 이름이 가이드라인을 충족하지만 여전히 거부되는 경우, Braze에서는 구체적인 사유를 확인할 수 없습니다. 다만 가장 일반적인 거부 사유는 비즈니스의 온라인 존재감이 너무 낮거나, [규제 또는 제한 제품](https://business.whatsapp.com/policy#further-guidance)을 마케팅하는 경우입니다.

표시 이름 거부에 대한 추가 안내는 [Meta 리소스]({{site.baseurl}}/user_guide/channels/whatsapp/meta_resources)를 참조하세요.

### WhatsApp 비즈니스 계정 전화번호 {#whatsapp-business-account-phone-numbers}
#### WhatsApp 비즈니스 계정에 전화번호가 필요한가요? {#do-i-need-a-phone-number-for-my-whatsapp-business-account}
네, 접근 가능한 번호가 필요합니다. 임베디드 가입 플로우를 진행할 때 2단계 인증으로 전화번호를 확인하게 됩니다. 해당 전화번호는 다른 WhatsApp 계정(비즈니스 또는 개인)에 사용할 수 없습니다.

#### WhatsApp에서 지원되는 전화번호 유형은 무엇인가요? {#what-types-of-phone-numbers-are-supported-with-whatsapp}
자세한 내용은 Meta의 [전화번호](https://developers.facebook.com/docs/whatsapp/phone-numbers) 요구사항을 참조하세요.

#### 하나의 전화번호를 여러 WABA에서 사용할 수 있나요? {#can-i-use-one-phone-number-across-multiple-wabas}
아니요. 전화번호는 여러 WABA 간에 공유할 수 없습니다.

#### 특정 국가에 메시지를 보내려면 특정 유형의 전화번호가 필요한가요? {#do-i-need-a-specific-type-of-phone-number-to-send-messages-to-specific-countries}
아니요. WhatsApp에서는 지원되는 모든 전화번호에서 어떤 국가의 최종 사용자에게든 메시지를 보낼 수 있습니다. 자세한 내용은 Meta의 [전화번호](https://developers.facebook.com/docs/whatsapp/phone-numbers) 요구사항을 참조하세요.

#### 사용자 전화번호를 Braze에 어떤 형식으로 저장해야 하나요? {#how-do-user-phone-numbers-need-to-be-stored-in-braze}
사용자 전화번호는 [E.164 형식]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers#formatting)으로 저장해야 합니다.

#### 사용자 전화번호를 가져올 수 있나요? {#can-i-import-user-phone-numbers}
네. [사용자 전화번호를 가져올]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers) 수 있습니다.

### 옵트인 및 구독 관리 {#opt-in-and-subscription-management}

#### WhatsApp에서 최종 사용자에게 마케팅 메시지를 보내려면 옵트인을 수집해야 하나요? {#do-i-need-to-collect-opt-in-to-send-marketing-messages-to-end-users-on-whatsapp}
네, WhatsApp에서는 비즈니스가 최종 사용자에게 마케팅 메시지를 보내기 위해 [옵트인 동의를 수집](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)해야 합니다.

#### 옵트인 동의를 수집하기 위해 WhatsApp에서 최종 사용자에게 먼저 메시지를 보낼 수 있나요? {#can-i-proactively-message-end-users-on-whatsapp-to-collect-opt-in-consent}
최종 사용자에게 먼저 메시지를 보내기로 한 경우, 첫 번째 비즈니스 시작 메시지에서 사용자가 비즈니스의 마케팅 메시지를 수신하고 싶은지 확인해야 하며, Meta의 [옵트인 수집](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) 요구사항을 준수해야 합니다. WhatsApp이 채널에서 비즈니스 평판을 모니터링하므로, 최종 사용자에게 명확하게 안내하고 수신을 원하는 메시지만 보내는 것이 권장 모범 사례입니다.

#### 옵트인을 수집할 때 최종 사용자의 전화번호도 수집해야 하나요? {#do-i-need-to-collect-the-end-users-phone-number-when-i-collect-opt-in}
메시지를 보내려면 Braze 프로필에 최종 사용자의 전화번호가 있어야 합니다.
- 이미 전화번호를 보유하고 있다면, 옵트인 시에 별도로 수집할 필요가 없습니다.
- 최종 사용자의 전화번호를 보유하지 않은 경우, 옵트인 방법에 전화번호 수집이 포함되어야 합니다.

#### 옵트인한 최종 사용자의 구독 상태를 어떻게 업데이트하나요? {#how-do-i-update-the-subscription-status-of-end-users-who-opt-in}
WhatsApp 채널의 구독 관리는 다른 Braze 채널과 유사하게 작동합니다. 자세한 내용은 [사용자 구독 관리]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)를 참조하세요.

#### WhatsApp에서 마케팅 메시지를 수신하기로 옵트인한 사용자 목록이 이미 있는 경우, Braze에서 구독 상태를 어떻게 업데이트하나요? {#if-i-already-have-a-list-of-users-who-have-opted-in-to-receive-marketing-messages-on-whatsapp-how-do-i-update-their-subscription-status-in-braze}
[사용자 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import#updating-subscription-group-status-optional)를 통해 구독 상태를 업데이트할 수 있습니다.

#### 옵트인을 수집하기 위해 어떤 방법을 사용해야 하나요? {#what-methods-should-i-use-to-collect-opt-ins}
규정 준수를 위해 [Meta의 옵트인 방법 가이드라인](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)을 참조하는 것을 권장합니다. Canvas 및 Campaign 설정 방법은 [옵트인 및 옵트아웃]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs)을 참조하세요.

#### WhatsApp에 이중 옵트인이 필요한가요? {#is-double-opt-in-required-for-whatsapp}
아니요, 이중 옵트인은 필요하지 않습니다.

#### 사용자가 WhatsApp 메시지를 어떻게 옵트아웃하나요? {#how-do-my-users-opt-out-of-whatsapp-messages}
사용자는 두 가지 방법으로 옵트아웃할 수 있습니다:
1. 특정 옵트아웃 키워드를 사용한 인바운드 WhatsApp 메시지를 설정하고, 웹훅을 사용하여 사용자 구독 상태를 업데이트합니다.
2. WhatsApp 템플릿 내에 옵트아웃 빠른 답장을 추가하고, 이에 대응하는 웹훅으로 업데이트합니다.

#### 서드파티를 통해 WhatsApp 메시지를 보내는 경우 Braze WhatsApp 구독 그룹을 사용할 수 있나요? {#can-i-use-a-braze-whatsapp-subscription-group-if-i-send-whatsapp-messages-through-a-third-party}
아니요. Braze WhatsApp 구독 그룹은 Braze WhatsApp 채널을 통해 보낸 메시지에 적용됩니다. 서드파티 공급자나 Braze WhatsApp Campaigns 및 Canvases 외부의 커스텀 통합을 통해 WhatsApp 메시지를 보내는 경우, 옵트인 동의를 커스텀 속성(또는 자체 구독 모델)에 저장하고 해당 속성을 세분화 및 자격 요건에 사용할 수 있습니다. Braze가 WhatsApp 번호를 소유하고 있는 경우의 관련 패턴은 [Braze에서 WhatsApp 지원과 마케팅을 어떻게 연결하나요?](#how-do-i-connect-whatsapp-support-and-marketing-in-braze)를 참조하세요.

### 메시징 한도 및 품질 등급 {#messaging-limits-and-quality-rating}

#### 메시징 한도란 무엇인가요? {#what-are-messaging-limits}
메시징 한도는 WhatsApp의 무결성 구축 개념입니다. 각 전화번호가 24시간 롤링 기간 동안 시작할 수 있는 비즈니스 시작 대화의 최대 수를 결정합니다. 메시징 한도 레벨은 1k, 10k, 100k, 무제한의 네 가지가 있습니다.

#### 메시징 한도를 어떻게 늘리나요? {#how-do-i-increase-my-messaging-limit}
다음 조건을 충족하면 WhatsApp에서 메시징 한도를 늘려줍니다:
1. [전화번호 상태](https://www.facebook.com/business/help/896873687365001)가 **연결됨**
2. [전화번호 품질 등급](https://www.facebook.com/business/help/896873687365001)이 **보통** 또는 **높음**
3. 지난 7일 동안 X명 이상의 고유 사용자와 대화를 시작했으며, 여기서 X는 현재 메시징 한도를 2로 나눈 값

따라서 100k에서 무제한으로 올리려면, 7일 기간 동안 최소 50,000건의 비즈니스 시작 대화를 보내야 합니다.

#### 메시징 한도를 늘리는 데 얼마나 걸리나요? {#how-long-does-it-take-to-increase-my-messaging-limits}
위의 모든 조건이 충족되면, 4일 만에 메시징 한도를 1k에서 무제한으로 늘릴 수 있습니다.

#### 현재 메시징 한도는 어디에서 확인할 수 있나요? {#where-can-i-see-my-current-messaging-limit}
**WhatsApp 매니저 > 개요 대시보드 > 인사이트** 탭에서 현재 메시징 한도를 확인할 수 있습니다.

#### 메시징 한도에 이미 도달한 상태에서 메시지를 보내려고 하면 어떻게 되나요? {#what-happens-if-i-attempt-to-send-messages-when-i-have-already-reached-my-messaging-limit}
현재 한도가 허용하는 것보다 더 많은 고유 사용자에게 Campaign 또는 Canvas를 보내려고 하면 메시지 전송에 실패합니다. Braze는 메시징 한도가 증가할 경우 최대 하루 동안 메시지 재전송을 계속 시도합니다.

#### 메시징 한도가 줄어들 수 있나요? {#can-my-messaging-limit-decrease}
네, 전화번호 품질 등급이 너무 낮아지면 WhatsApp에서 메시징 한도를 줄일 수 있습니다. Braze는 전화번호 상태 및 메시징 한도 레벨 업데이트를 포함한 WhatsApp의 품질 관련 업데이트를 구독하고 알림을 받는 것을 권장합니다. WhatsApp 매니저 대시보드에서 직접 알림을 구독할 수 있습니다.

#### 전화번호 품질 등급에 영향을 미치는 요인은 무엇이며, 품질 등급이 너무 낮아지면 어떻게 되나요? {#what-factors-affect-phone-number-quality-rating-and-what-happens-when-my-quality-rating-drops-too-low}
전화번호 품질 등급에 영향을 미치는 요인으로는 최종 사용자가 비즈니스를 차단하는 것(및 차단 시 제공하는 사유)과 최종 사용자가 비즈니스를 신고하는 것이 있습니다.

품질 등급이 낮으면 전화번호 상태가 **연결됨**에서 **경고**로 변경됩니다. 7일 내에 품질이 개선되지 않으면 상태가 **연결됨**으로 복귀하지만, 메시징 한도는 다음 레벨로 감소합니다. 예를 들어, 100,000 메시징 한도를 가지고 있던 전화번호는 이제 10,000 메시징 한도를 갖게 됩니다.

#### Meta 처리량 한도란 무엇인가요? {#what-is-the-meta-throughput-limit}
Meta는 WABA 메시징 한도와 별도로 자체 처리량 한도를 가지고 있습니다. 클라우드 API가 지원하는 기본 한도는 초당 80개 메시지입니다. Campaign이 이 한도를 초과할 것으로 예상되면 한도 증가를 [요청](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/#throughput)할 수 있습니다. Meta는 Campaign 발송 최소 3일 전에 이 요청을 제출할 것을 권장합니다.

### WhatsApp 템플릿 및 작성기 {#whatsapp-templates-and-composer}

#### WhatsApp 템플릿이란 무엇인가요? {#what-is-a-whatsapp-template}
WhatsApp에서는 모든 비즈니스 시작 메시지가 승인된 템플릿을 사용하여 시작해야 합니다. 템플릿에는 메시지 본문과 함께 이미지, 클릭 유도 문구(CTA), 빠른 답장 버튼과 같은 선택적 리치 미디어가 포함됩니다. WhatsApp이 템플릿을 승인하면 Braze에서 WhatsApp 메시지를 작성하는 데 사용할 수 있습니다.

#### WhatsApp 템플릿을 어디에서 만들고, 편집하고, 관리하나요? {#where-do-i-create-edit-and-manage-my-whatsapp-templates}
Braze에서 [WhatsApp 템플릿 빌더]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder)를 사용하거나 Meta의 WhatsApp 매니저에서 템플릿을 만들고 제출할 수 있습니다. 어느 위치에서 만들든 Braze 대시보드에 상태 표시기와 함께 나타납니다. 제출 후 잠긴 필드는 Meta 재승인이 필요합니다. 자세한 내용은 [템플릿 빌더 FAQ의 편집 제한 사항]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder#can-i-edit-a-template-after-its-been-approved)을 참조하세요.

#### WhatsApp이 템플릿 제출을 검토하는 데 얼마나 걸리나요? {#how-long-does-it-take-whatsapp-to-review-a-template-submission}
승인 프로세스는 최대 24시간까지 걸릴 수 있지만, 대부분의 템플릿은 몇 시간 또는 몇 분 내에 처리됩니다.

#### 한 번에 몇 개의 템플릿을 가질 수 있나요? {#how-many-templates-can-i-have-at-a-given-time}
메시지 템플릿 한도는 비즈니스 인증 상태에 따라 다릅니다. **WhatsApp 매니저 > 메시지 템플릿** 페이지에서 한도를 확인할 수 있습니다.

#### Braze에서 템플릿 본문과 리치 미디어를 어떻게 개인화하나요? {#how-do-i-personalize-template-copy-and-rich-media-in-braze}
WhatsApp은 메시지 템플릿에 변수 매개변수를 삽입할 수 있도록 합니다. 메시지는 변수 매개변수로 시작하거나 끝날 수 없습니다. 변수 매개변수는 Braze 플랫폼에서 Liquid 로직으로 채울 수 있습니다. 변수 매개변수에 대한 자세한 내용은 [Braze에서 WhatsApp 메시지 작성하기]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message)를 참조하세요.

#### 템플릿이 거부되었습니다. Braze에서 승인을 도와줄 수 있나요? {#my-template-got-rejected-can-braze-help-me-get-it-approved}
Braze 팀은 템플릿 거부에 대한 가시성이 없습니다. WhatsApp 비즈니스 매니저에서 직접 작업하여 템플릿을 편집하고 다시 제출해야 합니다. 필요한 경우 샘플 템플릿을 제공해야 합니다. 템플릿이 Meta의 [비즈니스](https://www.whatsapp.com/legal/business-policy/?fbclid=IwAR2qWg6yFKdyjDMxJkbNSM38FLGsxXxffC1qStY2gaHOyp-gl_8g72rZNIw) 또는 [상거래](https://www.whatsapp.com/legal/commerce-policy/?fbclid=IwAR3bzN3LTZ-7kO-wnO7X3smtPKGy0asxaFod-U1Ub8B9JUpnrfy1_y7LpAQ) 정책을 준수하는지 다시 확인하세요.

#### Braze에서 리치 미디어를 타겟팅하거나 개인화할 수 있나요? {#can-rich-media-be-targeted-or-personalized-in-braze}
네. 미디어 라이브러리에서 정적 이미지를 업로드하거나, URL로 이미지를 추가하고 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) 또는 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)로 개인화할 수 있습니다. 이미지 URL은 URL 내 어디서든 전체 Liquid 로직을 지원합니다. 이는 템플릿 메시지와 응답 메시지(미디어 메시지 및 빠른 답장 레이아웃)에 적용됩니다. 자세한 내용은 [동적 이미지]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#dynamic-images)를 참조하세요.

#### WhatsApp 템플릿에서 어떤 종류의 리치 미디어가 지원되나요? {#what-kind-of-rich-media-is-supported-in-whatsapp-templates}
WhatsApp 템플릿에 이미지, 클릭 유도 문구(URL 또는 전화번호), 빠른 답장 버튼을 추가할 수 있습니다. WhatsApp에서 직접 템플릿을 작성할 때 이러한 요소를 추가할 수 있습니다.

#### 내 템플릿이 WhatsApp의 상거래 정책 위반으로 잘못 플래그된 경우 어떻게 하나요? {#what-if-my-template-was-falsely-flagged-for-violating-whatsapps-commerce-policy}
Meta가 잘못 플래그했다고 판단되면, WhatsApp에서 보낸 이메일의 검토 링크를 사용하여 재검토를 요청하세요. WhatsApp 비즈니스 팀이 결정을 검토하고, 적절한 경우 이를 번복합니다.

#### 가져온 WhatsApp 템플릿이 작성기에서 "메시지 불완전"으로 표시되는 이유는 무엇인가요? {#why-does-my-imported-whatsapp-template-show-message-incomplete-in-the-composer}
"메시지 불완전" 경고는 필수 템플릿 변수 슬롯이 작성기에서 유효한 값으로 채워지지 않았을 때 나타납니다.

[WhatsApp 템플릿 빌더]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder)를 사용하여 템플릿을 만들면, Braze가 변수를 순차적 플레이스홀더({% raw %}`{{1}}`, `{{2}}`, `{{3}}`{% endraw %} 등)로 다시 번호를 매깁니다. Meta의 WhatsApp 매니저에서 외부적으로 만든 템플릿에는 변수 매핑을 오류에 취약하게 만드는 패턴이 포함될 수 있습니다. 예를 들면:

- 비순차적 번호 매기기(예: {% raw %}`{{1}}`, `{{3}}`, `{{5}}`{% endraw %})
- 시퀀스에서 누락된 변수(예: {% raw %}`{{2}}`{% endraw %} 건너뛰기)
- 1이 아닌 다른 번호에서 시작하는 변수

이를 해결하려면 Meta의 WhatsApp 매니저에서 템플릿을 편집하여 순차적 플레이스홀더 형식을 사용한 다음, Braze로 다시 가져오세요. Braze에서 각 필수 변수 필드가 유효한 Liquid 값으로 채워져 있는지 확인하세요.

#### WhatsApp Campaign이 템플릿 미리보기에도 불구하고 전송되지 않는 이유는 무엇인가요? {#why-is-my-whatsapp-campaign-not-sending-despite-template-previewing}
템플릿이 올바르게 미리보기되지만 처리 원장에 **중단**이 표시되고 세부사항에 "Param text cannot have new-line/tab characters or more than 4 consecutive spaces"가 나타나면, 메시지의 Liquid 템플릿 매개변수 값을 확인하세요. WhatsApp에서는 매개변수 텍스트 값에 다음이 포함되지 않아야 합니다:

- 줄바꿈 문자
- 탭 문자
- 4개 이상의 연속 공백

템플릿 매개변수를 채우는 모든 Liquid 로직이 발송 전에 이러한 문자를 제거하거나 텍스트를 적절하게 포맷하는지 확인하세요.

### 전달 가능성 및 청구 {#deliverability-and-billing}

#### 메시지가 전달되지 않는 이유는 무엇인가요? {#why-would-a-message-not-be-delivered}
네트워크 문제와 기기 전원이 꺼진 경우를 포함하여 메시지가 전달되지 않는 다양한 이유가 있습니다.

#### 메시지가 전달되지 않으면 청구되나요? {#if-a-message-is-not-delivered-will-i-be-billed}
아니요. 메시지가 전달되지 않으면 청구되지 않습니다.

#### 사용자가 내 비즈니스를 차단하면 어떻게 되나요? {#what-happens-if-a-user-blocks-my-business}
사용자가 비즈니스를 차단하면 이후에 보내려는 메시지가 전달되지 않으며 청구되지 않습니다. 사용자의 구독 상태는 업데이트되지 않습니다.

#### 사용자가 메시지를 신고하면 어떻게 되나요? {#what-happens-if-a-user-reports-a-message}
사용자가 메시지를 신고해도 이후 메시지를 계속 보낼 수 있습니다. 그러나 신고는 채널의 품질 등급에 영향을 줄 수 있습니다. 사용자의 구독 상태는 업데이트되지 않습니다.

#### 내 WhatsApp 계정을 신고한 사용자를 향후 발송에서 제외하려면 어떻게 하나요? {#how-can-i-exclude-users-who-report-my-whatsapp-account-from-upcoming-launches}
Braze는 계정이 플래그되거나 신고될 때 WhatsApp으로부터 알림을 받지 않으므로, Braze에서 해당 사용자를 자동으로 식별하거나 제외할 수 없습니다. 계정을 신고한 사용자는 WhatsApp 구독 그룹에 남아 있을 수 있으며 향후 메시지 수신 자격을 유지할 수 있습니다.

그러나 사용자가 옵트아웃 키워드로 응답할 때 트리거되는 Campaign을 설정하여 [`/subscription/status/set` 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)를 사용하여 자동으로 구독 취소할 수 있습니다. 자세한 내용은 [WhatsApp 옵트인 및 옵트아웃 프로세스]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-opt-in-and-opt-out-process)를 참조하세요.

#### WhatsApp 전달이 실패할 때 Braze에서 자동 SMS 대체를 지원하나요? {#does-braze-support-automatic-sms-fallback-when-whatsapp-delivery-fails}

아니요. Braze는 기본 WhatsApp-SMS 대체 경로를 제공하지 않습니다. 다른 채널에서 재시도하려면 WhatsApp 전송 실패 사용자(예: Currents 실패 이벤트 사용)를 세그먼트하고 SMS 또는 이메일 Campaign을 타겟으로 합니다.

#### WhatsApp 응답 메시지는 무료인가요? {#are-whatsapp-response-messages-free}

Braze Campaign 또는 Canvas 편집기에서 작성된(승인된 WhatsApp 템플릿이 아닌) 응답 메시지는 Meta에 의해 서비스 메시지로 분류됩니다. 2026년 9월 30일까지 Braze의 기본 WhatsApp 통합을 통해 전송된 서비스 메시지는 열려 있는 고객 서비스 창 내에서 [응답 메시지]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages)로 전송될 때 Action Credit을 소비하지 않습니다.

2026년 10월 1일부터 서비스 메시지는 전달된 메시지당 Action Credit을 소비합니다. 이 분류는 메시지 자체에 따라 결정됩니다. 비템플릿 응답은 대화가 템플릿으로 시작되었더라도 서비스 메시지입니다. 승인된 마케팅, 유틸리티 또는 인증 템플릿으로 응답하는 경우 해당 메시지는 템플릿 카테고리에 따라 청구됩니다.

| 메시지 유형 | Action Credit | 비고 |
|---|---|---|
| 응답 메시지(인바운드 답장) | 2026년 9월 30일까지 소비 안 됨; 2026년 10월 1일부터 소비됨 | Braze에서 작성됨; Meta 승인 템플릿이 아닙니다. Meta에서 서비스 메시지로 분류합니다. |
| 템플릿 메시지 | 소비됨 | 마케팅, 유틸리티, 인증 및 한시적 오퍼 템플릿은 전송당 청구됩니다. |
| 서비스 창 내 유틸리티 템플릿 | 2026년 9월 30일까지 Meta에서 과금하지 않음; 2026년 10월 1일부터 과금됨 | Action Credit 소비는 계약에 따릅니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="응답 메시지 Action Credit" }

원래 24시간 창이 지난 후 사용자가 빠른 답장을 탭하는 Canvas 플로우에 대한 내용은 [24시간 창 외부의 빠른 답장 및 인바운드 메시지]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window)를 참조하세요.

#### 24시간 창이 닫힌 후 사용자가 답장하거나 빠른 답장을 탭하면 어떻게 되나요? {#what-happens-if-a-user-replies-or-taps-a-quick-reply-after-the-24-hour-window-closes}
새로운 24시간 고객 서비스 창이 열립니다. [24시간 창 외부의 빠른 답장 및 인바운드 메시지]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window)를 참조하세요.

#### WhatsApp 빠른 답장을 위해 Canvas 행동 경로를 31일로 설정해야 하나요? {#do-i-need-to-set-my-canvas-action-path-to-31-days-for-whatsapp-quick-replies}
아니요. 기본 행동 경로 기간이면 충분합니다. [24시간 창 외부의 빠른 답장 및 인바운드 메시지]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window)를 참조하세요.

#### 특정 Campaign 또는 Canvas가 소비한 WhatsApp 크레딧을 확인할 수 있나요? {#can-i-see-how-many-whatsapp-credits-a-specific-campaign-or-canvas-consumed}
현재 Braze 대시보드에서는 확인할 수 없습니다. Campaign 및 Canvas 분석에서는 전송, 전달 및 실패를 표시하지만, 메시지당 크레딧 소비는 표시하지 않습니다. 전송 수는 크레딧 사용량과 일대일로 일치하지 않습니다. 템플릿 카테고리와 메시지 유형에 따라 청구가 다르게 적용되기 때문입니다. 청구에 대한 자세한 내용은 [WhatsApp 응답 메시지는 무료인가요?](#are-whatsapp-response-messages-free)를 참조하세요.

### 통합, 데이터 및 리포트 {#integrations-data-and-reporting}

#### 기술 파트너에 WhatsApp이 표시되지 않는 이유는 무엇인가요? {#why-isnt-whatsapp-listed-under-technology-partners}
WhatsApp은 회사에 WhatsApp이 활성화된 경우 **기술 파트너** 페이지에 나타납니다. 해당 페이지에서 WhatsApp이 보이지 않으면 Braze 계정 팀에 문의하여 대시보드에 WhatsApp이 프로비저닝되었는지 확인하세요.

#### Braze에서 챗봇이나 상담원 지원 채팅과 같은 고객 지원 사용 사례를 지원하나요? {#does-braze-support-customer-support-use-cases-like-chatbots-and-human-assisted-chat-for-whatsapp}
Braze 내에서 또는 직접 통합을 통해 챗봇이나 상담원 지원 채팅은 지원하지 않습니다.

이미 WhatsApp을 고객 지원 채널로 사용하고 있다면 현재 설정을 유지하고, 마케팅 메시징을 위해 Braze를 통해 새 WABA를 만드는 것을 권장합니다. 이 WABA에는 새로운 전화번호가 필요합니다.

#### Braze에서 WhatsApp 지원과 마케팅을 어떻게 연결하나요? {#how-do-i-connect-whatsapp-support-and-marketing-in-braze}

WhatsApp Liquid 속성을 사용하여 Braze에서 다른 플랫폼(고객 지원 도구 포함)으로 인바운드 WhatsApp 메시지 콘텐츠(메시지 본문 및 미디어 URL 포함)를 전달할 수 있습니다. 자세한 내용은 [지원되는 개인화 태그]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)를 참조하세요.

Braze에 정보를 보내려면(예: 사용자가 활성 지원 대화 중임을 나타내기 위해), 커스텀 속성(예: "has existing support chat = true/false" 불리언)을 기록하고 마케팅 Campaign에서 세분화 기준으로 사용할 수 있습니다. 또한 두 채팅 스레드 간에 딥링크를 설정하여 사용자를 마케팅 스레드에서 지원 스레드로, 또는 그 반대로 안내할 수 있습니다.

#### Braze에서 사용자 응답을 저장하나요? {#does-braze-store-user-responses}
메시지는 처리에 필요한 시간 동안만 저장됩니다. 사용자 메시지에 접근하려면 Currents를 사용하세요.

#### Braze 대시보드에서 어떤 측정기준을 확인할 수 있나요? {#what-metrics-are-available-in-the-braze-dashboard}
Braze 대시보드에서 고유 수신자, 전송, 전달, 읽음 및 실패를 확인할 수 있습니다. Braze가 읽음을 추적하려면 사용자의 수신 확인이 "켜짐" 상태여야 합니다. 다른 채널과 유사하게 전환 이벤트를 설정하여 Campaign 성능을 모니터링할 수도 있습니다.

#### WhatsApp 대화란 무엇인가요? {#what-is-a-whatsapp-conversation}
WhatsApp은 양방향 메시징에 중점을 둔 채널이므로, 개별 메시지 수가 아닌 대화를 기준으로 합니다. 대화는 비즈니스와 최종 사용자 간의 24시간 스레드입니다.

- **비즈니스 시작 대화**: 비즈니스가 최종 사용자에게 승인된 템플릿 메시지를 보내는 것으로 시작하는 대화입니다. 비즈니스가 메시지를 보내는 순간 24시간 창이 시작됩니다.
- **사용자 시작 대화**: 최종 사용자가 비즈니스에 메시지를 보내는 것으로 시작하는 대화입니다. 비즈니스가 이에 대한 응답 메시지를 보내면 24시간 창이 시작됩니다.

### 미디어 및 이미지 {#media-and-images}

#### WhatsApp 메시지로 전송했을 때 이미지가 로드되지 않는 이유는 무엇인가요? {#why-wont-images-load-when-sent-as-a-whatsapp-message}
사용자가 WhatsApp 메시지의 이미지가 다운로드되지 않거나 다운로드 아이콘이 반응하지 않는다고 보고하는 경우, 이는 이전 WhatsApp 앱 버전의 알려진 문제 때문일 가능성이 높습니다. 이 문제는 보통 기기를 최신 버전의 WhatsApp으로 업그레이드하면 해결됩니다.