---
nav_title: 오류 처리 및 재시도
article_title: 메시징 API 오류 처리 및 재시도
page_order: 2
page_type: reference
description: "메시징 API 응답, 오류 및 재시도를 처리하는 방법을 알아보세요."
hidden: true
---

# 메시징 API 오류 처리 및 재시도 {#messaging-api-error-handling-and-retries}

{% alert important %}
이 페이지는 베타 버전입니다. 메시징 API의 기능 및 설명서는 변경될 수 있습니다.
{% endalert %}

메시징 API 응답 본문과 성공 의미는 엔드포인트마다 다릅니다. 각 엔드포인트의 응답 스키마와 상태 코드 표를 공식 계약으로 사용하세요.

## 성공 응답 {#success-responses}

배너 엔드포인트는 서로 다른 성공 응답을 사용합니다:

- `POST /v1/device-messaging/banners/sync`는 `banners` 객체와 함께 `200` 상태 코드를 반환합니다.
- `POST /v1/device-messaging/banners/track`는 `events_processed` 및 `message`와 함께 `202` 상태 코드를 반환합니다. Braze가 개별 이벤트를 건너뛴 경우, 응답에 `errors` 배열도 포함됩니다.

추적 엔드포인트의 `202` 응답은 Braze가 최소 하나의 유효한 이벤트를 수락했음을 의미합니다. `errors` 배열을 검토하여 건너뛴 이벤트를 확인하세요.

## 오류 응답 {#error-responses}

오류 응답 필드도 다양합니다:

- 배너 조회 오류는 `error` 필드를 사용합니다.
- 배너 추적 오류는 `message` 필드를 사용하며, 인덱싱된 `errors` 배열을 포함할 수 있습니다.

애플리케이션 동작을 결정하기 위해 오류 메시지 텍스트를 파싱하지 마세요. 대신 HTTP 상태 코드와 엔드포인트별 필드를 사용하세요.

## 재시도 안내 {#retry-guidance}

재시도 여부를 결정할 때 다음 안내를 참고하세요:

| 상태 코드 | 재시도 안내 |
|---|---|
| `400` | 재시도하기 전에 요청을 수정하세요. 배너 추적의 경우, 건너뛴 이벤트를 수정한 후 재시도하세요. |
| `401` 또는 `403` | 재시도하기 전에 클라이언트 측 REST API 키와 권한을 확인하세요. |
| `404` | 워크스페이스에서 메시징 API가 활성화되어 있는지, 엔드포인트 URL이 올바른지 확인하세요. |
| `429` | 요청 속도를 줄이고 지수 백오프를 적용하여 재시도하세요. 가능한 경우 속도 제한 응답 헤더를 사용하세요. |
| `5XX` | 지수 백오프와 최대 재시도 횟수를 적용하여 재시도하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="메시징 API 재시도 안내" }

정확한 응답 본문과 지원되는 상태 코드는 관련 엔드포인트를 참조하세요:

- [사용자의 배너 조회]({{site.baseurl}}/api/messaging_api/endpoints/banners/post_sync_banners)
- [배너 분석 이벤트 추적]({{site.baseurl}}/api/messaging_api/endpoints/banners/post_track_banner_events)