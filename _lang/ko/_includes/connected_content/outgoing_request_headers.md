Braze는 발신 연결된 콘텐츠 요청에 다음 헤더를 추가합니다. 대부분은 태그에서 아직 제공하지 않은 경우에만 설정됩니다. `:headers`, 자격 증명 또는 태그 옵션을 통해 제공한 헤더는 그대로 전송됩니다.

| 헤더 | Braze가 설정하는 시점 |
| --- | --- |
| `User-Agent` | 아직 설정하지 않은 경우, Braze는 `Braze Sender <version>`을 전송합니다. 버전 문자열은 변경될 수 있습니다. `User-Agent`로 트래픽을 필터링하는 경우, `Braze Sender`로 시작하는 모든 값을 허용하세요. 일관된 값을 전송하려면 `:headers`에서 `User-Agent`를 설정하세요. |
| `X-Braze-Sender-Version` | 항상 연결된 콘텐츠 발신자 버전으로 설정됩니다. |
| `Accept-Encoding` | 아직 설정하지 않은 경우, Braze는 `gzip`을 전송합니다. |
| `Authorization` | URL에 사용자 이름과 비밀번호(`user:pass@host`)가 포함된 경우, Braze는 해당 자격 증명에서 파생된 Basic `Authorization` 헤더를 추가합니다. 명시적인 `Authorization` 헤더가 이를 재정의합니다. URL에 자격 증명을 넣는 대신 [`:basic_auth`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#using-basic-authentication) 또는 `:headers`를 사용하는 것이 좋습니다. |
| `Host` | `Host` 헤더를 설정하지 않은 경우, 요청 URL의 호스트 이름입니다(예: `https://www.example.com/abc/123`의 경우 `www.example.com`). |
| `Content-Length` | 본문이 있는 경우, 요청 본문의 크기(바이트 단위)입니다. |
| `BrazeToBraze` | Braze REST 엔드포인트에 대한 요청에만 `true`로 설정됩니다. 다른 대상에는 생략됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze가 연결된 콘텐츠에 추가하는 발신 요청 헤더" }