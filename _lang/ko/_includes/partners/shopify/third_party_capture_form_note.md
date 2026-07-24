{% alert note %}
[Shopify 개요]({{site.baseurl}}/shopify_overview)에서 언급한 바와 같이, 서드파티 캡처 양식을 사용하려면 개발자가 Braze SDK 코드를 통합해야 합니다. 이를 통해 양식 제출에서 이메일 주소와 글로벌 이메일 가입 상태를 캡처할 수 있습니다. 구체적으로, `theme.liquid` 파일에 다음 메서드를 구현하고 테스트해야 합니다:<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): 고객 프로필에 이메일 주소를 설정합니다
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): 글로벌 이메일 가입 상태를 업데이트합니다
{% endalert %}