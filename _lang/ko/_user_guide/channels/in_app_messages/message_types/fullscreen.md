---
nav_title: "전체화면"
article_title: 전체화면 인앱 메시지
description: "이 참조 문서에서는 전체화면 인앱 메시지의 메시지 및 디자인 요구 사항을 다룹니다."
page_type: reference
page_order: 1
channel:
  - in-app messages
tool:
  - Media

---

# 전체화면 인앱 메시지 {#fullscreen-in-app-messages}

> 전체화면 메시지는 기기의 전체 화면을 차지합니다! 이 메시지 유형은 필수 앱 업데이트와 같이 사용자의 주의를 반드시 끌어야 할 때 유용합니다.

이 메시지 유형은 [드래그 앤 드롭]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/) 및 [기존 편집기]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/) 모두에서 사용할 수 있습니다.

{% tabs %}
{% tab 세로 %}

![세로 방향으로 나란히 표시된 두 개의 전체화면 인앱 메시지로, 이미지 및 텍스트 권장 사항을 자세히 설명합니다. 자세한 내용은 다음 섹션을 참조하세요.]({% image_buster /assets/img/full-screen-spec.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab 가로 %}

![가로 방향으로 나란히 표시된 두 개의 전체화면 인앱 메시지로, 이미지 및 텍스트 권장 사항을 자세히 설명합니다. 자세한 내용은 다음 섹션을 참조하세요.]({% image_buster /assets/img/full-screen-spec-landscape.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

## 이미지 {#images}

전체화면 인앱 메시지는 기기의 전체 높이를 채우며 필요에 따라 가로(좌우)로 잘릴 수 있습니다. 이미지 및 텍스트 전체화면 메시지는 기기 높이의 50%를 채웁니다. 모든 전체화면 인앱 메시지는 "노치" 기기에서 상태 표시줄을 채웁니다.

- 모든 이미지는 5&nbsp;MB 미만이어야 합니다.
- PNG, JPEG 및 [GIF]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs/#gifs) 파일 형식만 지원합니다.
- 이미지 크기는 500&nbsp;KB를 권장합니다.

{% alert tip %} 자신 있게 자산을 만들어 보세요! 인앱 메시지 이미지 템플릿과 안전 영역 오버레이는 모든 크기의 기기에서 잘 작동하도록 설계되었습니다. [디자인 템플릿 ZIP 다운로드]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

### 세로 {#portrait}

| 레이아웃 | 자산 크기 | 참고 |
|--- | --- | --- |
| 이미지 및 텍스트 | 6:5 종횡비<br> 고해상도 1200 x 1000&nbsp;px<br> 최소 600 x 500&nbsp;px | 모든 면에서 잘림이 발생할 수 있지만, 이미지는 항상 뷰포트 상단 50%를 채웁니다 |
| 이미지만 | 3:5 종횡비<br> 고해상도 1200 x 2000&nbsp;px<br> 최소 600 x 1000&nbsp;px | 더 긴 기기에서 좌우 가장자리에서 잘림이 발생할 수 있습니다 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Portrait" }

### 가로 {#landscape}

| 레이아웃 | 자산 크기 | 참고 |
|--- | --- | --- |
| 이미지 및 텍스트 | 10:3 종횡비<br> 고해상도 2000 x 600px<br> 최소 1000 x 300&nbsp;px | 모든 면에서 잘림이 발생할 수 있지만, 이미지는 항상 뷰포트 상단 50%를 채웁니다 |
| 이미지만 | 5:3 종횡비<br> 고해상도 2000 x 1200px<br> 최소 1000 x 600&nbsp;px | 더 긴 기기에서 좌우 가장자리에서 잘림이 발생할 수 있습니다 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Landscape" }

### 이미지 안전 영역 {#image-safe-zone}

Braze 플랫폼에서 전체화면 인앱 메시지를 미리볼 때, 다양한 기기에서 표시될 때 잘리지 않는 메시지 영역인 이미지 안전 영역을 활성화할 수 있습니다. 미리보기 창에서 이미지 안전 영역을 테스트하는 것 외에도, 항상 [메시지를 테스트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=in-app%20message)하는 것을 권장합니다.

![Braze에서 "이미지 안전 영역 표시"가 활성화된 인앱 메시지 미리보기. 이미지 안전 영역은 이미지 위에 오버레이로 표시되어 잘리지 않는 부분을 시각화합니다.]({% image_buster /assets/img/image-safe-zone-full-screen-in-app-message.png %})

## 큰 화면 {#larger-screens}

태블릿이나 데스크탑 브라우저에서 전체화면 인앱 메시지는 다음 스크린샷과 같이 앱 화면 가운데에 표시됩니다.

{% tabs %}
{% tab 세로 %}

![큰 화면에서 세로 방향으로 표시되는 전체화면 인앱 메시지. 메시지가 화면 가운데에 위치한 큰 모달로 나타납니다.]({% image_buster /assets/img/full-screen-large-viewport.png %}){: style="border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab 가로 %}

![큰 화면에서 가로 방향으로 표시되는 전체화면 인앱 메시지. 메시지가 화면 가운데에 위치한 큰 모달로 나타납니다.]({% image_buster /assets/img/full-screen-large-viewport-landscape.png %}){: style="max-width:80%;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}