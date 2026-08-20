---
nav_title: 구독 관리 블록
article_title: 구독 관리 블록
description: "이 문서에서는 Braze 랜딩 페이지에 구독 관리 양식 블록을 추가하고 구성하여 소비자가 이메일 구독 그룹에 옵트인하고 관리할 수 있도록 하는 방법을 다룹니다."
page_order: 5
---

# 구독 관리 블록 {#manage-subscriptions-block}

> 랜딩 페이지에 **구독 관리** 블록을 추가하여 사용자가 이메일 구독 그룹을 확인하고, 옵트인하고, 업데이트할 수 있도록 합니다.

**구독 관리** 블록은 두 가지 주요 사용 사례를 지원합니다:

- **[기존 구독 관리](#update-existing-subscriptions):** 랜딩 페이지의 [Liquid 태그]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users)를 이메일 또는 다른 채널 메시지에서 공유합니다. 식별된 사용자가 페이지를 열면, 블록이 각 구독 그룹의 체크박스를 현재 구독 상태에 맞게 자동으로 미리 채워주므로 사용자가 환경설정을 검토하고 업데이트할 수 있습니다.
- **[신규 옵트인 수집](#capture-new-subscribers):** 리드 생성 랜딩 페이지에 **이메일 캡처** 블록과 함께 블록을 추가하여 새로운 방문자가 양식을 제출할 때 가입할 구독 그룹을 선택할 수 있도록 합니다.

{% alert important %}
**구독 관리** 블록은 [이메일 구독 그룹]({{site.baseurl}}/api/endpoints/subscription_groups)만 지원합니다. SMS, RCS 또는 WhatsApp 구독 그룹은 지원하지 않습니다.
{% endalert %}

## 전제 조건 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| 이메일 구독 그룹 | [대시보드에서 생성]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups)하거나 [구독 그룹 엔드포인트]({{site.baseurl}}/user_guide/channels/email/subscriptions#creating-a-subscription-group)를 통해 생성한 [이메일 구독 그룹]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups)이 하나 이상 필요합니다. |
| 랜딩 페이지 권한 | 랜딩 페이지를 생성하고 편집하는 데 필요한 것과 동일한 [권한]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites)이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="전제 조건" }

## 1단계: 구독 관리 블록 추가 {#step-1-add-the-manage-subscriptions-block}

드래그 앤 드롭 랜딩 페이지 편집기에서 **빌드** 섹션으로 이동하여 **양식 블록**을 선택합니다. **구독 관리**를 페이지의 행으로 드래그하면 열 너비에 맞게 자동 조정됩니다.

블록에 구독 그룹을 추가하기 전까지는 블록이 비어 있습니다.

## 2단계: 구독 그룹 선택 {#step-2-select-the-subscription-groups}

**구독 관리** 블록을 선택한 상태에서 오른쪽 **블록 속성** 패널에서 **+ 구독 그룹 추가**를 선택합니다. 워크스페이스에서 사용 가능한 [이메일 구독 그룹]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups) 목록이 열립니다.

포함하려는 각 구독 그룹 옆의 체크박스를 선택한 다음 선택을 확인하여 블록에 추가합니다. 각 구독 그룹은 랜딩 페이지에서 선택 가능한 개별 체크박스로 표시됩니다.

{% alert note %}
**구독 관리** 블록은 명시적으로 추가한 그룹만 나열합니다. 블록에 구독 그룹을 추가해도 방문자가 자동으로 구독되지 않습니다. 방문자가 해당 그룹의 체크박스를 선택하고 양식을 제출해야 합니다.
{% endalert %}

## 3단계: 블록 설정 구성 {#step-3-configure-the-block-settings}

**블록 속성** 패널을 사용하여 블록의 동작과 표시 방식을 조정합니다.

### 구독 그룹 {#subscription-groups}

- **그룹 순서 변경:** 구독 그룹의 핸들을 드래그하여 블록에 표시되는 순서를 변경합니다.
- **그룹 추가 또는 제거:** **+ 구독 그룹 추가**를 선택하여 더 많은 그룹을 포함하거나, 그룹 옆의 삭제 아이콘을 선택하여 블록에서 제거합니다.

### 설명 포함 {#include-descriptions}

**설명 포함**을 켜면 각 구독 그룹의 설명 텍스트가 이름과 함께 표시되어 방문자에게 옵트인 대상에 대한 더 많은 맥락을 제공합니다.

### "선택 해제" 체크박스 {#clear-selections-checkbox}

**"선택 해제" 체크박스** 설정을 켜면 블록에 추가 체크박스가 추가됩니다. 방문자가 이를 선택하면 블록의 모든 구독 그룹 체크박스가 해제됩니다. 양식을 제출하기 전에 나열된 모든 항목에서 빠르게 옵트아웃할 수 있어 유용합니다.

### "모두 구독" 체크박스 {#subscribe-to-all-checkbox}

**"모두 구독" 체크박스** 설정을 켜면 블록에 추가 체크박스가 추가됩니다. 방문자가 이를 선택하면 블록의 모든 구독 그룹 체크박스가 선택됩니다. 나열된 모든 그룹에 빠르게 옵트인할 수 있어 유용합니다.

## 기존 구독 업데이트 {#update-existing-subscriptions}

기존 사용자가 이메일 구독을 검토하고 업데이트할 수 있도록 하려면, 랜딩 페이지의 [Liquid 태그]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users)를 이메일, 캔버스 단계 또는 기타 메시지에서 공유합니다. 사용자가 해당 링크를 통해 페이지를 열면, Braze가 사용자를 식별하고 **구독 관리** 블록의 각 구독 그룹 체크박스를 현재 구독 상태에 맞게 자동으로 미리 채웁니다. 이는 [이메일 환경설정 센터]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center)와 유사합니다.

사용자는 체크박스를 선택하거나 해제하여 구독을 업데이트한 다음 양식을 제출하여 변경 사항을 저장할 수 있습니다.

{% alert note %}
**구독 관리** 블록에서 사용자의 현재 구독 상태를 미리 채우는 기능은 기본적으로 포함되어 있으며 [Landing Pages Pro 등급]({{site.baseurl}}/user_guide/messaging/landing_pages#plan-tiers)이 필요하지 않습니다. 이는 Landing Pages Pro가 필요한 다른 양식 필드의 [Liquid 기반 미리 채우기]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages#pre-fill-form-fields)와 다릅니다.
{% endalert %}

## 신규 구독자 수집 {#capture-new-subscribers}

리드 생성 랜딩 페이지 등에서 신규 구독자를 수집하려면, **구독 관리** 블록을 [이메일 캡처 블록]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages)과 함께 사용하여 소비자의 이메일 주소와 구독 그룹 선택을 함께 캡처합니다.

소비자가 식별되지 않은 경우(예: 랜딩 페이지 Liquid 태그 없이 도착한 경우), 체크박스는 선택되지 않은 상태로 시작됩니다. 양식을 제출하면 선택한 구독 그룹에 구독됩니다.

## 알아두어야 할 사항 {#things-to-know}

- **SMS, RCS 및 WhatsApp 동의:** 이메일 대신 랜딩 페이지에서 이러한 채널에 대한 동의를 수집하려면 [전화번호 캡처 블록]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages)을 사용합니다.
- **확인 경험:** **구독 관리**를 포함한 양식 블록이 있는 랜딩 페이지는 제출 후 확인 경험이 필요합니다. [확인 페이지를 생성]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-4-create-a-confirmation-page-optional)하고 **제출** 버튼에서 연결합니다.
- **편집기 블록 참조:** 모든 랜딩 페이지 블록과 해당 속성에 대한 전체 참조는 [편집기 블록(랜딩 페이지)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages)을 참조하세요.