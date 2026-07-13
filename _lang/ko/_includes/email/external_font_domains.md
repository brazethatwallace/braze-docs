### 외부 폰트 도메인 {#external-font-domains}

커스텀 {{ include.page_type }} 페이지를 만들 때, Braze는 크로스 사이트 스크립팅(XSS) 공격을 방지하기 위해 HTML 입력을 검사합니다. 이 보안 조치의 일환으로, 폰트 URL을 포함한 외부 리소스 URL은 다음 허용 도메인에서 제공되지 않는 한 제거됩니다.

- `assets.appboycdn.com`
- `braze-images.com`
- `cdn.braze.com`
- `cdn.braze.eu`
- `fonts.googleapis.com`
- `fonts.gstatic.com`

{{ include.page_type }} 페이지에서 커스텀 폰트를 사용해야 하는 경우, 위 도메인 중 하나에서 폰트를 참조하거나 [웹 안전 폰트](https://www.w3schools.com/cssref/css_websafe_fonts.php)를 대신 사용하세요.

이메일 목록 관리 모범 사례에 대해서는 [이메일 가입]({{site.baseurl}}/user_guide/channels/email/subscriptions)을 참조하세요.