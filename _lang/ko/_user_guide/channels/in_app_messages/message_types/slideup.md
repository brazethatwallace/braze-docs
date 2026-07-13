---
nav_title: 슬라이드업
article_title: 슬라이드업 인앱 메시지
page_order: 3
channel:
  - in-app messages
tool:
  - Media
description: "이 참조 문서에서는 슬라이드업 인앱 메시지의 메시지 및 디자인 요구 사항을 다룹니다."

---

# 슬라이드업 인앱 메시지 {#slideup-in-app-messages}

> 슬라이드업은 일반적으로 앱 화면의 상단 또는 하단에 표시됩니다(메시지를 생성할 때 설정할 수 있습니다). 이 메시지는 새로운 이용 약관, 쿠키 및 기타 정보 스니펫에 대해 사용자에게 알릴 때 유용합니다. 방해가 되지 않으며, 메시지가 표시되는 동안에도 사용자가 앱과 계속 상호작용할 수 있습니다.

이 메시지 유형은 [기존 편집기]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)에서 사용할 수 있습니다.

![화면 상단과 하단에서 각각 나타나는 두 개의 슬라이드업 인앱 메시지로, 이미지 및 텍스트 권장 사항을 자세히 설명합니다. 자세한 내용은 다음 섹션을 참조하세요.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width: 40%; border: none;"}

## 이미지 및 텍스트 동작 {#image-and-copy-behavior}

슬라이드업 메시지는 줄임표로 잘리기 전까지 최대 세 줄의 텍스트를 포함할 수 있습니다. 슬라이드업의 이미지는 절대 잘리거나 클리핑되지 않으며, 항상 50 x 50 픽셀 이미지 컨테이너에 맞게 축소됩니다.

- 모든 이미지는 5&nbsp;MB 미만이어야 합니다.
- PNG, JPEG, GIF 파일 형식만 지원됩니다.
- 이미지 크기는 500&nbsp;KB를 권장합니다.

{% alert tip %} 자신 있게 자산을 만드세요! 인앱 메시지 이미지 템플릿과 세이프 존 오버레이는 모든 크기의 기기에서 잘 작동하도록 설계되었습니다. [디자인 템플릿 ZIP 다운로드]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

| 레이아웃 | 자산 크기 | 참고 |
|--- | --- | --- |
| 이미지 + 텍스트 | 1:1 종횡비<br>고해상도 150 x 150&nbsp;px<br> 최소 50 x 50&nbsp;px | 다양한 종횡비의 이미지가 잘리지 않고 정사각형 이미지 컨테이너에 맞게 조정됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="이미지 및 텍스트 동작" }

이미지와 메시지의 가장 중요한 영역이 예상대로 표시되는지 확인하려면 항상 다양한 기기에서 [메시지를 미리보기하고 테스트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message)해야 합니다. 작성기에서 메시지를 미리볼 때 실제 기기에서의 렌더링은 다를 수 있습니다.

## 하이퍼링크 및 앵커 텍스트 {#hyperlinks-and-anchor-text}

슬라이드업에 링크를 추가하려면 **본문** 필드에 메시지 텍스트를 입력하고 **클릭 시 동작**에서 대상을 설정합니다(예: **URL로 리디렉션**). **클릭 시 동작**이 구성되면 닫기 제어를 제외한 메시지의 아무 곳이나 탭하면 해당 동작이 트리거됩니다.

커스텀 HTML 인앱 메시지의 경우 HTML 링크를 직접 사용할 수 있습니다. [커스텀 HTML 인앱 메시지]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html)를 참조하세요.

## 모바일 기기 {#mobile-devices}

모바일 기기에서 슬라이드업은 앱 화면의 상단 또는 하단에 표시됩니다. 메시지를 생성할 때 이를 지정할 수 있습니다. 사용자는 스와이프하여 슬라이드업을 닫거나, 클릭 동작이 포함된 경우 탭하여 열 수 있습니다. 슬라이드업에 클릭 동작이 추가되면 꺾쇠 ">"가 표시됩니다.

## 더 큰 화면 {#larger-screens}

{% tabs %}
{% tab 데스크탑 %}

데스크탑 브라우저에서 슬라이드업 인앱 메시지는 다음 스크린샷과 같이 화면 모서리에 표시됩니다(인앱 메시지를 생성할 때 별도로 지정하지 않은 경우). 사용자는 닫기 "X" 버튼을 클릭하여 슬라이드업을 닫을 수 있습니다.

![데스크탑 브라우저에 표시되는 슬라이드업 인앱 메시지. 메시지가 화면 오른쪽 하단 모서리에 나타나며 화면 전체 너비를 차지하지 않습니다.]({% image_buster /assets/img/slideup-large-viewport.png %}){: style="border: none;"}

{% endtab %}
{% tab 태블릿 %}

태블릿에서 슬라이드업 인앱 메시지는 화면 하단에 표시됩니다. 모바일 기기와 마찬가지로 사용자는 스와이프하여 슬라이드업을 닫거나, 클릭 동작이 포함된 경우 탭하여 열 수 있습니다. 슬라이드업에 클릭 동작이 추가되면 꺾쇠 ">"가 표시됩니다. 닫기 "X" 버튼은 기본적으로 표시되지 않습니다.

![태블릿 화면에 표시되는 슬라이드업 인앱 메시지. 메시지가 화면 하단 중앙에 나타나며 화면 전체 너비를 차지하지 않습니다.]({% image_buster /assets/img/slideup-tablet.png %}){: style="border: none;"}

{% endtab %}
{% endtabs %}