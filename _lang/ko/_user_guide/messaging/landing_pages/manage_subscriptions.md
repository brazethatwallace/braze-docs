---
nav_title: 구독 관리 블록
article_title: 구독 관리 블록
description: "이 문서에서는 Braze 랜딩 페이지에 구독 관리 양식 블록을 추가하고 구성하여 소비자가 이메일, SMS 또는 WhatsApp 구독 그룹에 옵트인하고 관리할 수 있도록 하는 방법을 다룹니다."
page_order: 5
---

# 구독 관리 블록 {#manage-subscriptions-block}

> 랜딩 페이지에 **구독 관리** 블록을 추가하여 사용자가 이메일, SMS 또는 WhatsApp 구독 그룹을 확인하고, 옵트인하고, 업데이트할 수 있도록 합니다.

**구독 관리** 블록은 두 가지 주요 사용 사례를 지원합니다:

- **[기존 구독 관리](#update-existing-subscriptions):** 랜딩 페이지의 [Liquid 태그]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users)를 이메일, SMS, WhatsApp 또는 다른 채널 메시지에서 공유합니다. 식별된 사용자가 페이지를 열면, 블록이 각 구독 그룹의 체크박스를 현재 구독 상태에 맞게 자동으로 미리 채워주므로 사용자가 환경설정을 검토하고 업데이트할 수 있습니다.
- **[신규 옵트인 수집](#capture-new-subscribers):** 리드 생성 랜딩 페이지에 **이메일 캡처** 또는 **전화번호 캡처** 블록과 함께 블록을 추가하여 새로운 방문자가 양식을 제출할 때 가입할 구독 그룹을 선택할 수 있도록 합니다.

{% alert important %}
각 **구독 관리** 블록은 하나의 채널에 대해 사용됩니다: [이메일]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups), [SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states) 또는 [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-subscription-states). 두 개 이상의 채널을 수집하려면 각 채널에 대해 블록을 추가하세요. RCS 동의를 수집하려면 [전화번호 캡처]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages) 블록을 대신 사용하세요.
{% endalert %}

## 사전 요구 사항 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| 이메일, SMS 또는 WhatsApp 구독 그룹 | 블록에 추가하는 채널에 대해 최소 하나의 [이메일 구독 그룹]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups), [SMS 구독 그룹]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states) 또는 [WhatsApp 구독 그룹]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-subscription-states)이 필요합니다. 이메일 그룹은 대시보드 또는 [구독 그룹 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups)에서 생성할 수 있습니다. SMS 그룹은 [SMS 설정]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#enable-subscription-groups) 중에 프로비저닝됩니다. WhatsApp 그룹은 워크스페이스에 [WhatsApp을 통합]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)할 때 생성됩니다. |
| 랜딩 페이지 권한 | 랜딩 페이지를 만들고 편집하는 데 필요한 것과 동일한 [권한]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites)이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사전 요구 사항" }

## 1단계: 구독 관리 블록 추가하기 {#step-1-add-the-manage-subscriptions-block}

드래그 앤 드롭 랜딩 페이지 편집기에서 **빌드** 섹션으로 이동하여 **양식 블록**을 선택합니다. **구독 관리**를 페이지의 행으로 드래그하면 열 너비에 맞게 자동으로 조정됩니다.

블록은 구독 그룹을 추가하기 전까지 비어 있습니다. 두 개 이상의 채널에 대한 그룹을 표시하려면 각 채널마다 **구독 관리** 블록을 추가하세요.

## 2단계: 채널 및 구독 그룹 선택 {#step-2-select-the-channel-and-subscription-groups}

**구독 관리** 블록을 선택한 상태에서 오른쪽 **블록 속성** 패널에서 **+ 구독 그룹 추가**를 선택합니다. **구독 그룹 추가** Modal이 열립니다.

1. **채널 선택**에서 **이메일**, **SMS** 또는 **WhatsApp**을 선택합니다. 각 블록은 하나의 채널만 지원합니다. 페이지에 이미 해당 채널의 **구독 관리** 블록이 있는 경우, 해당 채널 카드는 비활성화되고 **추가됨**으로 표시됩니다.
2. **구독 그룹 선택**에서 포함할 그룹을 선택합니다. 목록 제목은 채널에 따라 다릅니다(**이메일 구독 그룹**, **SMS 구독 그룹** 또는 **WhatsApp 구독 그룹**).
3. **선택 항목 추가**를 선택합니다.

각 구독 그룹은 랜딩 페이지에서 선택 가능한 개별 체크박스로 표시됩니다.

**SMS**를 선택했는데 워크스페이스에 SMS 구독 그룹이 아직 없는 경우, Modal에 **SMS 구독 그룹이 아직 없습니다**라고 표시됩니다. [SMS 구독 그룹 설정]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states)을 완료한 후 블록으로 돌아오세요.

**WhatsApp**을 선택했는데 워크스페이스에 WhatsApp 구독 그룹이 아직 없는 경우, Modal에 **WhatsApp 구독 그룹이 아직 없습니다**라고 표시됩니다. [WhatsApp 구독 그룹 설정]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-subscription-states)을 완료한 후 블록으로 돌아오세요.

{% alert note %}
**구독 관리** 블록에는 명시적으로 추가한 그룹만 표시됩니다. 블록에 구독 그룹을 추가하는 것만으로 방문자가 자동으로 해당 그룹에 가입되지는 않습니다. 방문자가 직접 해당 그룹의 체크박스를 선택하고 양식을 제출해야 합니다.
{% endalert %}

## 3단계: 블록 설정 구성하기 {#step-3-configure-the-block-settings}

**블록 속성** 패널을 사용하여 블록의 동작과 표시 방식을 조정합니다.

### 구독 그룹 {#subscription-groups}

- **그룹 순서 변경:** 구독 그룹의 핸들을 드래그하여 블록에 표시되는 순서를 변경할 수 있습니다.
- **그룹 추가 또는 제거:** **+ Add subscription groups**를 선택하여 더 많은 그룹을 추가하거나, 그룹 옆의 삭제 아이콘을 선택하여 블록에서 제거할 수 있습니다.

### 설명 포함 {#include-descriptions}

**Include descriptions**를 켜면 각 구독 그룹의 설명 텍스트가 이름과 함께 표시되어, 방문자가 무엇에 옵트인하는지에 대해 더 많은 맥락을 제공합니다. 이메일 그룹은 구독 관리에서 설명을 포함할 수 있습니다. 이 블록의 SMS 및 WhatsApp 그룹은 설명 텍스트를 표시하지 않습니다.

### "모두 구독" 체크박스 {#subscribe-to-all-checkbox}

**"Subscribe to all" checkbox** 설정을 켜면 블록에 추가 체크박스가 표시됩니다. 방문자가 이 체크박스를 선택하면 블록 내 모든 구독 그룹 체크박스가 선택되므로, 나열된 모든 그룹에 빠르게 옵트인할 때 유용합니다.

## 기존 구독 업데이트 {#update-existing-subscriptions}

기존 사용자가 이메일, SMS 또는 WhatsApp 구독을 검토하고 업데이트할 수 있도록 하려면, 이메일, SMS, WhatsApp, 캔버스 단계 또는 기타 메시지에서 [Liquid 태그]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users)를 사용하여 랜딩 페이지를 공유하세요. 사용자가 해당 링크를 통해 페이지를 열면, Braze가 사용자를 식별하고 **구독 관리** 블록의 각 구독 그룹 체크박스를 현재 구독 상태에 맞게 자동으로 미리 채웁니다. 이는 [이메일 환경설정 센터]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center)와 유사합니다.

사용자는 체크박스를 선택하거나 해제하여 구독을 업데이트한 다음, 양식을 제출하여 변경 사항을 저장할 수 있습니다.

{% alert note %}
**구독 관리** 블록에서 사용자의 현재 구독 상태를 미리 채우는 기능은 기본으로 포함되어 있으며, [랜딩 페이지 Pro 티어]({{site.baseurl}}/user_guide/messaging/landing_pages#plan-tiers)가 필요하지 않습니다. 이는 랜딩 페이지 Pro가 필요한 다른 양식 필드의 [Liquid 기반 미리 채우기]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages#pre-fill-form-fields)와는 다릅니다.
{% endalert %}

## 신규 구독자 확보 {#capture-new-subscribers}

신규 구독자를 수집하려면 **구독 관리** 블록을 해당 채널의 캡처 필드와 함께 사용하세요.

- **이메일:** [이메일 캡처]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages) 블록을 추가하면 방문자의 이메일 주소와 이메일 구독 그룹 선택 항목을 함께 수집할 수 있습니다.
- **SMS 또는 WhatsApp:** [전화번호 캡처]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages) 블록을 추가하면 방문자의 전화번호와 SMS 또는 WhatsApp 구독 그룹 선택 항목을 함께 수집할 수 있습니다.

방문자가 식별되지 않은 경우(예: 랜딩 페이지 Liquid 태그 없이 도착한 경우) 체크박스는 선택되지 않은 상태로 시작합니다. 방문자가 양식을 제출하면 선택한 구독 그룹에 가입됩니다.

## 알아두어야 할 사항 {#things-to-know}

- **채널당 하나의 블록:** 페이지에서 채널당 하나의 **구독 관리** 블록을 추가할 수 있습니다(이메일용 하나, SMS용 하나, WhatsApp용 하나).
- **RCS:** 이 블록에는 RCS 구독 그룹이 표시되지 않습니다. RCS에 대한 동의를 수집하려면 [전화번호 캡처]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages) 블록을 사용하세요.
- **확인 경험:** **구독 관리**를 포함한 양식 블록이 있는 랜딩 페이지에는 제출 후 확인 경험이 필요합니다. [확인 페이지를 만들고]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-4-create-a-confirmation-page-optional) **제출** 버튼에서 해당 페이지로 연결하세요.
- **편집기 블록 참조:** 모든 랜딩 페이지 블록과 해당 속성에 대한 전체 참조는 [편집기 블록(랜딩 페이지)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages)을 확인하세요.