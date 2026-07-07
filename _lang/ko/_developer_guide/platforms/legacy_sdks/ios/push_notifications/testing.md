---
nav_title: 테스팅
article_title: iOS용 푸시 알림 테스트
platform: iOS
page_order: 29
description: "이 참조 문서에서는 iOS 푸시 알림에 대한 명령줄 푸시 테스트를 다룹니다."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 테스트 {#push-testing}

명령줄을 통해 인앱 및 푸시 알림을 테스트하려면 CURL과 [메시징 API]({{site.baseurl}}/api/endpoints/messaging)를 사용하여 터미널에서 단일 알림을 보낼 수 있습니다. 다음 필드를 테스트 케이스에 맞는 올바른 값으로 바꿔야 합니다.

필수 필드:

- `YOUR-API-KEY-HERE` - **설정** > **API 키**에서 확인할 수 있습니다. `/messages/send` REST API 엔드포인트를 통해 메시지를 발송할 수 있도록 키가 승인되었는지 확인하세요.
- `EXTERNAL_USER_ID` - **사용자 검색** 페이지에서 확인할 수 있습니다.
- `REST_API_ENDPOINT_URL` - Braze [인스턴스]({{site.baseurl}}/api/basics#endpoints. Ensure using the endpoint corresponds to the Braze instance your workspace is on.

Optional fields:
- `YOUR_KEY1` (optional) 페이지에 나열되어 있습니다. 사용하는 엔드포인트가 워크스페이스가 속한 Braze 인스턴스에 해당하는지 확인하세요.

선택 필드:
- `YOUR_KEY1` (선택 사항)
- `YOUR_VALUE1` (선택 사항)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer YOUR-API-KEY-HERE" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://{REST_API_ENDPOINT_URL}/messages/send
```
