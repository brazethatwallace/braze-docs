---
nav_title: 오류 및 응답
article_title: API 오류 및 응답
description: "이 참고 문서에서는 Braze API를 사용하는 동안 발생할 수 있는 다양한 오류 및 서버 응답과 문제 해결 방법에 대해 설명합니다."
page_type: reference
page_order: 2.3

---
# API 오류 및 응답 {#api-errors-and-responses}

> 이 참고 문서에서는 Braze API를 사용하는 동안 발생할 수 있는 다양한 오류 및 서버 응답과 문제 해결 방법에 대해 설명합니다.

## 서버 응답 {#server-responses}

POST 페이로드가 서버에 수락되면, 성공적인 메시지는 다음과 같은 응답을 받습니다:

```json
{
  "message" : "success"
}
```

success는 RESTful API 페이로드가 올바르게 구성되어 푸시 알림, 이메일 또는 기타 메시징 서비스로 전달되었다는 것만 의미합니다. 메시지가 실제로 전달되었다는 의미는 아닙니다. 추가적인 요인으로 인해 메시지가 전달되지 않을 수 있습니다(예: 기기가 오프라인 상태이거나, 푸시 토큰이 Apple 서버에 의해 거부되었거나, 알 수 없는 사용자 ID를 제공했을 수 있습니다).

### 메시지가 전달되지 않았는데 요청이 성공을 반환하는 이유는 무엇인가요? {#why-does-my-request-return-success-when-no-message-was-delivered}

`message: success` 또는 `2XX` 응답은 Braze가 관련 엔드포인트에 대한 요청을 수락하고 대기줄에 넣었다는 의미이며, 모든 수신자가 메시지를 받았다는 의미는 아닙니다. 메시징의 경우, 전달은 채널 자격, 토큰, 공급자 오류 및 콘텐츠 유효성 검사에 따라 달라집니다. 전송을 차단하는 HTTP 오류에 대해서는 [심각한 오류]({{site.baseurl}}/api/errors#fatal-errors) 표를 참조하고, 다운스트림 전달 측정기준에 대해서는 Campaign 또는 Canvas 분석을 확인하세요.

[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)와 같이 메시지를 보내지 않는 엔드포인트의 경우, 성공 메시지는 Braze가 처리를 위한 요청을 수신했다는 것만 의미합니다. 처리 후 별칭에 대한 일치 항목이 없으면 요청이 중단됩니다.

메시지가 성공했지만 심각하지 않은 오류가 있는 경우, 다음과 같은 응답을 받습니다:

```json
{
  "message" : "success", "errors" : [<minor error message>]
}
```

성공의 경우, `errors` 배열의 오류에 영향을 받지 않은 메시지는 여전히 전달됩니다. 메시지에 심각한 오류가 있는 경우 다음과 같은 응답을 받습니다:

```json
{
  "message" : <fatal error message>, "errors" : [<minor error message>]
}
```

## 추적된 전송 ID에 대한 응답 {#responses-for-tracked-send-ids}

분석은 항상 Campaigns에서 사용할 수 있습니다. 또한 Campaign이 브로드캐스트로 전송된 경우, 특정 Campaign 전송 인스턴스에 대한 분석도 사용할 수 있습니다. 특정 Campaign 전송 인스턴스에 대해 추적이 가능한 경우, 다음과 같은 응답을 받게 됩니다:

```json
{
  "message": "success", "send_id" : "example_send_id"
}
```

제공된 전송 ID는 `/send/data_series` 엔드포인트의 파라미터로 사용하여 전송별 분석 데이터를 조회할 수 있습니다.

## 오류 {#errors}

서버 응답의 상태 코드 요소는 3자리 숫자이며, 코드의 첫 번째 자릿수가 응답의 클래스를 정의합니다.

- **2XX 클래스** 상태 코드(심각하지 않은 오류)는 **요청**이 성공적으로 수신, 이해 및 수락되었음을 나타냅니다.
- **4XX 클래스** 상태 코드(심각한 오류)는 **클라이언트 오류**를 나타냅니다. 4XX 오류 코드 및 설명의 전체 목록은 심각한 오류 차트를 참조하세요.
- **5XX 클래스** 상태 코드(심각한 오류)는 **서버 오류**를 나타냅니다. 잠재적인 원인은 여러 가지가 있습니다. 예를 들어, 접근하려는 서버가 요청을 실행할 수 없거나, 서버가 유지보수 중이어서 요청을 실행할 수 없거나, 서버에 높은 수준의 트래픽이 발생하는 경우 등이 있습니다. 이 경우 지수 백오프를 사용하여 요청을 재시도하는 것을 권장합니다. 인시던트 또는 장애가 발생한 경우, Braze는 인시던트 기간 동안 실패한 REST API 호출을 재실행할 수 없습니다. 인시던트 기간 동안 실패한 모든 호출을 직접 재시도해야 합니다.
  - **502 오류**는 요청이 대상 서버에 도달하기 전에 발생하는 장애입니다.
  - **503 오류**는 요청이 대상 서버에 도달했지만, 충분한 용량이 없거나 네트워크 문제 등으로 인해 요청을 완료할 수 없음을 의미합니다.
  - **504 오류**는 서버가 업스트림의 다른 서버로부터 응답을 받지 못했음을 나타냅니다.

### 심각한 오류 {#fatal-errors}

요청에 심각한 오류가 발생하면 다음 상태 코드와 관련 오류 메시지가 반환됩니다.

{% alert warning %}
다음 오류 코드가 반환되면 메시지가 전송되지 않습니다.
{% endalert %}

| 오류 코드 | 설명 |
|---|---|
| `5XX Internal Server Error` | 지수 백오프를 사용하여 요청을 재시도하세요.|
| `400 Bad Request` | 잘못된 구문입니다. 유효하지 않은 JSON은 HTTP 400을 반환합니다. `error` 필드에는 요청 본문에 유효한 `application/json`을 전달해야 한다는 메시지 또는 `Error while parsing request body. Please check your syntax.`가 포함될 수 있습니다. [요청 본문 파싱 오류](#error-while-parsing-request-body)를 참조하세요.|
| `400 No Recipients` | 요청에 외부 ID, Segment ID 또는 푸시 토큰이 없습니다.|
| `400 Invalid Campaign ID` | 제공한 Campaign ID에 해당하는 메시징 API Campaign을 찾을 수 없습니다.|
| `400 Message Variant Unspecified` | Campaign ID는 제공했지만 메시지 배리언트 ID가 없습니다.|
| `400 Invalid Message Variant` | 유효한 Campaign ID를 제공했지만, 메시지 배리언트 ID가 해당 Campaign의 메시지와 일치하지 않습니다.|
| `400 Mismatched Message Type` | 하나 이상의 메시지에 대해 잘못된 메시지 유형의 메시지 배리언트를 제공했습니다.|
| `400 Invalid Extra Push Payload` | `apple_push` 또는 `android_push`에 `extra` 키를 제공했지만 사전 형식이 아닙니다.|
| `400 Max Input Length Exceeded` | `/users/track`의 경우, 이 오류는 단일 요청에서 허용되는 최대 객체 수를 초과했을 때 발생합니다. 제한은 사용량 제한 모델에 따라 다릅니다. 대부분의 고객의 경우, 각 요청은 `attributes`, `events`, `purchases`를 합산하여 최대 75개의 총 객체를 지원합니다. 레거시 사용량 제한을 사용하는 고객의 경우, 각 배열은 독립적으로 최대 75개의 객체를 지원합니다. 자세한 내용은 [POST: 사용자 생성 및 업데이트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 참조하세요.|
| `400 The max number of external_ids and aliases per request was exceeded` | 50개를 초과하는 외부 ID를 호출하여 발생합니다.|
| `400 The max number of ids per request was exceeded` | 50개를 초과하는 외부 ID를 호출하여 발생합니다.|
| `400 No message to send` | 메시지에 대한 페이로드가 지정되지 않았습니다.|
| `400 Slideup Message Length Exceeded` | 슬라이드업 메시지가 140자를 초과합니다.|
| `400 Apple Push Length Exceeded` | JSON 페이로드가 1,912바이트를 초과합니다.|
| `400 Android Push Length Exceeded` | JSON 페이로드가 4,000바이트를 초과합니다.|
| `400 Bad Request` | `send_at` 날짜/시간을 파싱할 수 없습니다.|
| `400 Bad Request` | 요청에서 `in_local_time`이 true이지만, 회사 시간대 기준으로 `time`이 이미 지났습니다.|
| `401 Unauthorized` | 유효하지 않은 API 키입니다. 일반적인 원인은 다음과 같습니다:<br><br>- **Authorization 헤더가 누락되었거나 형식이 올바르지 않습니다.** 헤더 값은 `Bearer` 뒤에 공백과 API 키가 와야 합니다: `Authorization: Bearer YOUR-API-KEY`. 일반적인 실수로는 `Bearer`를 생략하거나, `Bearer` 뒤에 키를 생략하거나, 값을 따옴표로 감싸는 경우가 있습니다.<br>- **잘못된 REST 엔드포인트.** 잘못된 [인스턴스]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)로 요청을 보내고 있습니다. 예를 들어, 계정이 EU 인스턴스(`https://dashboard-01.braze.eu`)에 있는 경우, 요청은 `https://rest.fra-01.braze.eu`로 보내야 합니다.<br>- **권한이 부족합니다.** 각 API 키는 특정 워크스페이스와 권한 세트로 범위가 지정됩니다. 대시보드에서 **설정** > **API 키**에서 키의 권한을 확인하세요.<br>- **잘못된 API 키.** API 키는 워크스페이스별로 고유합니다. 하나의 워크스페이스에서 생성된 키는 다른 워크스페이스의 요청을 인증하는 데 사용할 수 없습니다. |
| `403 Forbidden` | 요금제에서 지원하지 않거나, 계정이 비활성화되었습니다.|
| `403 Access Denied` | 사용 중인 REST API 키에 충분한 권한이 없습니다. 일반적인 원인은 다음과 같습니다: {::nomarkdown}<ul><li><strong>API 키가 기능보다 먼저 생성되었습니다.</strong> 기능이 출시되기 전에 API 키가 생성된 경우(예: 구독 그룹 또는 카탈로그), 해당 키에 자동으로 권한이 부여되지 않습니다. <strong>설정</strong> &gt; <strong>API 키</strong>에서 필요한 권한을 가진 새 API 키를 생성하세요.</li><li><strong>엔드포인트별 권한이 누락되었습니다.</strong> 각 API 엔드포인트에는 특정 권한 범위가 필요합니다(예: <code>users.track</code> 또는 <code>email.status</code>). 호출하려는 엔드포인트와 키의 권한이 일치하는지 확인하세요.</li><li><strong>URL의 후행 슬래시 또는 오타.</strong> 예를 들어, <code>/users/track</code> 대신 <code>/users/track/</code>(후행 슬래시 포함)를 사용하면 예기치 않은 오류가 발생할 수 있습니다.</li></ul>{:/}|
| `404 Not Found` | 유효하지 않은 URL입니다. |
| `415 Unsupported Media Type` | `Content-Type` 요청 헤더가 누락되었거나 올바르지 않습니다. **설정** 페이지에서 `Content-Type`을 `application/json` 값으로 추가하세요. |
| `429 Rate Limited` | 사용량 제한을 초과했습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="심각한 오류" }

### 요청 본문 파싱 오류 {#error-while-parsing-request-body}

Braze는 요청 본문이 유효한 JSON이 아닌 경우 HTTP 400을 반환합니다. 이는 POST, PUT, PATCH와 같이 JSON 본문을 수락하는 REST 엔드포인트에 적용됩니다.

`error` 필드에는 요청 본문에 유효한 `application/json`을 전달해야 한다는 메시지가 포함됩니다. `Error while parsing request body. Please check your syntax.`라는 메시지가 표시될 수도 있습니다.

일반적인 원인으로는 후행 쉼표, JSON 내부의 주석, 작은따옴표로 감싼 문자열, 페이로드 앞의 추가 여는 `{`, 또는 JSON 인코딩된 객체 대신 연결된 문자열을 전송하는 경우가 있습니다.

재시도하기 전에:

1. JSON 린터로 페이로드를 검증하세요.
2. `Content-Type: application/json`을 설정하고 UTF-8로 인코딩된 JSON을 전송하세요.
3. HTTP 클라이언트가 원시 문자열을 연결하는 대신 객체를 JSON으로 인코딩하는지 확인하세요.

`/users/track` 페이로드 크기 및 요청당 객체 제한에 대한 자세한 내용은 [구문 오류 또는 파싱 오류로 `400 Bad Request`가 발생하는 이유는 무엇인가요?]({{site.baseurl}}/api/endpoints/user_data/post_user_track#why-do-i-get-400-bad-request-with-a-bad-syntax-or-parse-error)를 참조하세요.