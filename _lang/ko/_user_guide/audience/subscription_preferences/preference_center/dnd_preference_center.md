---
nav_title: 드래그 앤 드롭 이메일 환경설정 센터
article_title: 드래그 앤 드롭 이메일 환경설정 센터
alias: "/dnd_preference_center/"
description: "이 참조 페이지에서는 드래그 앤 드롭 편집기를 사용하여 이메일 환경설정 센터를 만드는 방법을 다룹니다."
page_order: 2
---

# 드래그 앤 드롭으로 이메일 환경설정 센터 만들기 {#create-an-email-preference-center-with-drag-and-drop}

> 드래그 앤 드롭 편집기를 사용하면 환경설정 센터를 만들고 커스터마이즈하여 어떤 사용자가 특정 유형의 커뮤니케이션을 수신할지 관리할 수 있습니다. 워크스페이스당 최대 100개의 환경설정 센터를 보유할 수 있습니다.

{% multi_lang_include alerts/tip_alerts.md alert="Landing pages manage subscriptions" %}

기존 드래그 앤 드롭 환경설정 센터는 **오디언스** > **이메일 환경설정 센터**에서 관리할 수 있습니다:

- 환경설정 센터의 이름이나 콘텐츠를 변경하려면 대시보드에서 환경설정 센터를 엽니다.
- 드래그 앤 드롭 환경설정 센터는 대시보드에서 삭제할 수 없습니다. 제거하려면 먼저 이메일 Campaign 또는 캔버스 단계에서 해당 Liquid 태그를 제거한 다음 [Braze 고객지원]({{site.baseurl}}/support_contact)에 문의하세요.
- 제거된 환경설정 센터가 이전에 발송된 메시지에서 사용되었다면, 해당 전달된 이메일에서 더 이상 작동하지 않습니다.
{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## 1단계: 이메일 환경설정 센터 만들기 {#step-1-create-an-email-preference-center}

**오디언스** > **이메일 환경설정 센터**로 이동하여 환경설정 센터를 만듭니다. 여기에 커스텀 환경설정 센터 목록이 표시됩니다. **새로 만들기**를 선택하여 새 환경설정 센터를 만들거나, 기존 환경설정 센터의 이름을 선택하여 변경합니다.

## 2단계: 이메일 환경설정 센터 이름 지정 {#step-2-name-the-email-preference-center}

환경설정 센터 이름에는 영숫자, 대시 또는 밑줄만 사용할 수 있습니다. 입력한 이름에 따라 생성되는 Liquid 태그의 구문이 결정됩니다.

이 Liquid 태그는 모든 아웃바운드 이메일 Campaigns 또는 캔버스 단계에 포함할 수 있으며, 사용자를 환경설정 센터로 안내합니다.

## 3단계: 환경설정 센터에 구독 그룹 추가 {#step-3-add-subscription-groups-to-the-preference-center}

**Launch Editor**를 선택하여 드래그 앤 드롭 편집기에서 환경설정 센터 디자인을 시작합니다.

### 사용 가능한 구독 그룹 정의 {#define-available-subscription-groups}

환경설정 센터에 표시할 구독 그룹을 결정하려면 **+ Add subscription groups** 버튼을 선택하여 원하는 구독 그룹을 선택할 수 있는 Modal을 실행합니다. 선택을 완료한 후 **Add Subscription Groups** 버튼을 선택하여 환경설정 센터에 추가합니다.

스마트 블록을 선택하고 블록 속성을 조정하여 선택한 구독 그룹을 추가로 구성할 수 있습니다.

- 구독 그룹의 순서 조정
- 추가 구독 그룹 추가 또는 제거
- 설명 포함
- 이 블록에 표시된 모든 구독 그룹에 사용자를 가입시키는 **Subscribe to all** 체크박스 추가 또는 제거
- 이 블록에 표시된 모든 구독 그룹에서 사용자를 탈퇴시키는 **Unsubscribe from all** 체크박스 추가 또는 제거

템플릿 하단의 **Unsubscribe from all** 버튼은 제거할 수 없으며, 사용자가 모든 이메일 메시지 수신을 [전체 탈퇴]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states)하도록 합니다.

## 4단계: 드래그 앤 드롭 편집기를 사용하여 환경설정 센터 커스터마이즈하기 {#step-4-customize-the-preference-center-using-the-drag-and-drop-editor}

### 공통 스타일 설정 {#set-common-styles}

**공통 스타일** 탭에서 환경설정 센터의 모든 관련 블록에 적용할 특정 스타일을 설정할 수 있습니다. 이 섹션에서 설정한 스타일은 특정 블록에 대해 재정의하지 않는 한 메시지 전체에 사용됩니다. 보다 쉬운 디자인 경험을 위해 블록 수준에서 스타일을 커스터마이즈하기 전에 페이지 수준 스타일을 먼저 설정하는 것을 권장합니다.

![텍스트, 버튼, 링크에 대한 공통 스타일 설정 예시.]({% image_buster /assets/img/preference_center/preference_center5.png %}){: style="max-width:45%;"}

{% alert tip %}
공통 스타일로 돌아가려면 개별 블록 속성에서 "X" 버튼을 선택합니다. 그런 다음 메시지 컨테이너, 메시지 "X" 버튼 또는 편집기 배경을 선택합니다.
{% endalert %}

## 드래그 앤 드롭 환경설정 센터 구성 요소 {#drag-and-drop-preference-center-components}

드래그 앤 드롭 편집기는 환경설정 센터 구성을 빠르고 쉽게 만들기 위해 두 가지 핵심 구성 요소인 행과 블록을 사용합니다. 모든 블록은 행 안에 배치해야 합니다.

{% tabs %}
{% tab 행 %}

행은 셀을 사용하여 메시지 섹션의 수평 구성을 정의하는 구조적 단위입니다.

![메시지에서 행 유형을 선택하는 옵션.]({% image_buster /assets/img/preference_center/preference_center6.png %}){: style="max-width:45%;"}

행을 선택하면 열 사용자 지정 섹션에서 필요한 열 수를 추가하거나 제거하여 서로 다른 콘텐츠 요소를 나란히 배치할 수 있습니다. 슬라이드를 사용하여 기존 열의 크기를 조정할 수도 있습니다.

![배경색, 테두리 스타일, 테두리 반경, 패딩 등 열 속성을 사용자 지정하는 옵션.]({% image_buster /assets/img/preference_center/preference_center7.png %}){: style="max-width:45%;"}

모범 사례로, 행 내부의 블록을 서식 지정하기 전에 행과 열 속성을 먼저 서식 지정하세요. 여백과 정렬을 여러 곳에서 조정할 수 있으므로, 기초부터 시작하면 진행하면서 편집하기가 더 쉬워집니다.

{% endtab %}
{% tab 블록 %}

블록은 메시지에서 사용할 수 있는 다양한 유형의 콘텐츠를 나타냅니다. 기존 행 세그먼트 안으로 블록을 드래그하면 셀 너비에 맞게 자동으로 조정됩니다.

![제목, 단락, 버튼, 이미지, 스페이서 등 블록을 선택하는 옵션.]({% image_buster /assets/img/preference_center/preference_center8.png %}){: style="max-width:45%;"}

모든 블록에는 패딩에 대한 세밀한 제어와 같은 고유한 설정이 있습니다. 오른쪽 패널은 선택한 콘텐츠 요소에 대한 스타일링 패널로 자동 전환됩니다. 자세한 내용은 [편집기 블록(환경설정 센터)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=preference%20center)을 참조하세요.

환경설정 센터에서 커스텀 코드 블록을 사용하는 경우, 사용자에게 전달될 때 커스텀 코드 내에서 인라인 프레임이 생성되지 않을 수 있습니다.

{% alert note %}
링크가 포함된 Content Blocks는 드래그 앤 드롭 환경설정 센터에서 사용할 수 없습니다. Content Blocks 내의 링크는 클릭할 수 없습니다.
{% endalert %}

{% endtab %}
{% endtabs %}

## 5단계: 확인 페이지 커스터마이즈하기 {#step-5-customize-your-confirmation-page}

다음으로, **확인 페이지**를 선택하여 확인 페이지를 커스터마이즈합니다. 이 페이지는 사용자가 환경설정 센터를 사용하여 환경설정을 업데이트한 후에 표시됩니다. [공통 스타일 설정](#set-common-styles) 및 [드래그 앤 드롭 환경설정 센터 구성요소](#drag-and-drop-preference-center-components)의 동일한 스타일링 기능이 이 페이지에도 적용됩니다.

![사용자의 환경설정이 업데이트되었음을 알리는 확인 페이지 예시.]({% image_buster /assets/img/preference_center/preference_center9.png %}){: style="max-width:65%;"}

## 6단계: 환경설정 센터 미리보기 및 실행 {#step-6-preview-and-launch-your-preference-center}

편집기 내에서 **미리보기** 탭을 선택하여 환경설정 센터를 미리 볼 수 있습니다. 미리보기에는 환경설정 센터와 확인 페이지가 모두 표시됩니다.

단, 테스트 기능은 비활성화되어 있습니다. 또한 환경설정 센터 Liquid 태그가 포함된 Campaign 또는 캔버스 단계의 테스트 발송은 유효한 링크를 생성하지 않습니다. 이 미리보기에서는 구독 변경 사항을 저장할 수 없으며, 페이지가 어떻게 보이는지만 확인할 수 있습니다. 환경설정 저장을 테스트하려면 [환경설정 센터 테스트](#testing-preference-centers)를 참조하세요. 환경설정 센터 편집을 마친 후 **완료** 버튼을 선택하여 편집기를 닫을 수 있습니다.

**임시 저장**을 선택하면 나중에 이 환경설정 센터로 돌아올 수 있으며, 만족스러운 경우 **환경설정 센터 실행**을 선택합니다.

환경설정 센터를 실행할 때 이름을 확인하라는 메시지가 표시됩니다. 실행 후에는 이름을 수정할 수 없기 때문입니다. 이름을 확인하면 환경설정 센터가 실행되어 사용할 준비가 됩니다.

## 환경설정 센터 사용하기 {#use-the-preference-center}

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

이메일에 환경설정 센터 링크를 배치하려면, 원하는 환경설정 센터의 **Copy Liquid** 아이콘을 선택하여 Liquid 태그를 복사하세요.

![환경설정 센터 행에 있는 Copy Liquid 옵션.]({% image_buster /assets/img/preference_center/preference_center10.png %}){: style="max-width:75%;"}

[탈퇴 URL]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer#adding-a-custom-unsubscribe-link)을 삽입하는 방식과 유사하게, 이메일에서 원하는 위치에 Liquid 태그를 추가하세요.

{% multi_lang_include preference_center/testing.md %}

## 자주 묻는 질문 {#frequently-asked-questions}

### 테스트 발송에서 환경설정 센터가 작동하지 않는 이유는 무엇인가요? {#why-doesnt-my-preference-center-work-in-a-test-send}

환경설정 센터 링크는 실제 발송 컨텍스트가 필요합니다. 테스트 발송에서는 유효한 환경설정 센터 URL이 생성되지 않으며, 페이지가 로드되면 **환경설정 저장** 버튼이 비활성화됩니다. 이는 예상된 동작입니다. 포괄적인 테스트를 수행하려면 테스트 사용자 또는 소규모 내부 Segment에 Campaign 또는 캔버스 단계를 실행하세요. 자세한 내용은 [환경설정 센터 테스트](#testing-preference-centers)를 참조하세요.

## 오류 처리 {#handle-errors}

사용자가 환경설정 센터에서 **저장**을 선택할 때 오류가 발생하면, 다음과 같은 기본 오류 메시지가 표시됩니다. 이 메시지는 편집기에서 커스터마이즈하거나 스타일을 변경할 수 없습니다. 그러나 이러한 페이지에서는 오류 메시지의 현지화가 지원됩니다.

![환경설정 저장에 문제가 발생했다는 오류 메시지]({% image_buster /assets/img/preference_center/preference_center11.png %}){: style="max-width:55%;"}