{% multi_lang_include developer_guide/prerequisites/web.md %} 그러나 추가 설정은 필요하지 않습니다.

## 메시지 유형 {#message-types}

모든 인앱 메시지는 [`InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html)에서 프로토타입을 상속하며, 이 클래스는 모든 인앱 메시지의 기본 동작과 특성을 정의합니다. 프로토타입 서브클래스로는 [`SlideUpMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html), [`ModalMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html), [`FullScreenMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html), [`HtmlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html)가 있습니다.

각 인앱 메시지 유형은 콘텐츠, 이미지, 아이콘, 클릭 액션, 분석, 표시 및 전달 전반에 걸쳐 사용자 지정할 수 있습니다.

{% tabs %}
{% tab 슬라이드업 %}

[`SlideUp`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html) 인앱 메시지는 기존 모바일 플랫폼에서 화면의 위쪽이나 아래쪽에서 "슬라이드 업" 또는 "슬라이드 다운"되는 방식에서 이름이 유래되었습니다. Braze 웹 SDK에서는 웹의 주요 패러다임에 맞추어 Growl 또는 Toast 스타일의 알림으로 표시됩니다. 화면의 작은 부분만 차지하며, 효과적이고 비침습적인 메시징 기능을 제공합니다.

![휴대폰 화면 하단에서 슬라이드되는 인앱 메시지로, "Humans are complicated. Custom engagement shouldn't be."라는 문구가 표시되어 있습니다. 배경에는 동일한 인앱 메시지가 웹 페이지의 하단 모서리에 표시되어 있습니다.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

[`Modal`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html) 인앱 메시지는 화면 중앙에 나타나며 반투명 패널로 둘러싸여 있습니다. 보다 중요한 메시지 전달에 유용하며, 최대 두 개의 클릭 액션 및 분석 지원 버튼을 포함할 수 있습니다.

![휴대폰 화면 중앙에 표시되는 Modal 인앱 메시지로, "Humans are complicated. Custom engagement shouldn't be."라는 문구가 표시되어 있습니다. 배경에는 동일한 인앱 메시지가 웹 페이지의 중앙에 표시되어 있습니다.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab 전체화면 %}

[`Full`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html) 인앱 메시지는 사용자 커뮤니케이션의 콘텐츠와 효과를 극대화하는 데 유용합니다. 좁은 브라우저 창(예: 모바일 웹)에서는 `full` 인앱 메시지가 전체 브라우저 창을 차지합니다. 큰 브라우저 창에서는 `full` 인앱 메시지가 `modal` 인앱 메시지와 유사하게 표시됩니다. `full` 인앱 메시지의 상단 절반에는 이미지가 포함되고, 하단 절반에는 최대 8줄의 텍스트와 최대 두 개의 클릭 액션 및 분석 지원 버튼을 포함할 수 있습니다.

![휴대폰 화면 전체에 표시되는 전체화면 인앱 메시지로, "Humans are complicated. Custom engagement shouldn't be."라는 문구가 표시되어 있습니다. 배경에는 동일한 인앱 메시지가 웹 페이지의 중앙에 크게 표시되어 있습니다.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab 커스텀 HTML %}

[`HTML`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html) 인앱 메시지는 완전히 사용자 지정된 콘텐츠를 만드는 데 유용합니다. 사용자 정의 HTML은 iFrame에 표시되며, 이미지, 글꼴, 비디오, 인터랙티브 요소 등 풍부한 콘텐츠를 포함할 수 있어 메시지 외형과 기능을 완전히 제어할 수 있습니다. HTML 내에서 Braze 웹 SDK의 메서드를 호출할 수 있는 JavaScript `brazeBridge` 인터페이스를 지원합니다. 자세한 내용은 [모범 사례]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices)를 참조하세요.

{% alert important %}
웹 SDK를 통해 HTML 인앱 메시지를 사용하려면 Braze에 `allowUserSuppliedJavascript` 초기화 옵션을 **반드시** 제공해야 합니다. 예: `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. 이는 보안상의 이유 때문입니다. HTML 인앱 메시지는 JavaScript를 실행할 수 있으므로, 사이트 관리자가 직접 활성화해야 합니다.
{% endalert %}

다음 예시는 페이지가 나뉘는 HTML 인앱 메시지를 보여줍니다:

![콘텐츠 캐러셀과 인터랙티브 버튼이 포함된 HTML 인앱 메시지.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

{% endtab %}
{% endtabs %}