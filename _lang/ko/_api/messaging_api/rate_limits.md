---
nav_title: 사용량 제한
article_title: 메시징 API 사용량 제한
page_order: 3
page_type: reference
description: "메시징 API 사용량 제한과 응답 헤더의 작동 방식에 대해 알아보세요."
hidden: true
---

# 메시징 API 사용량 제한 {#messaging-api-rate-limits}

{% alert important %}
이 페이지는 베타 버전입니다. 메시징 API의 기능과 설명서는 변경될 수 있습니다.
{% endalert %}

Braze는 워크스페이스별로 메시징 API 사용량 제한을 적용합니다. 워크스페이스가 제한을 초과하면 Braze는 `429 Too Many Requests` 상태 코드를 반환합니다.

메시징 API 제한은 다른 Braze REST API 엔드포인트에 대해 문서화된 기본 제한과 별도로 적용됩니다. 다른 엔드포인트에 대해 문서화된 제한, 시간 창, 페이로드 크기 또는 재설정 스케줄이 메시징 API에도 적용된다고 가정하지 마세요.

## 사용량 제한 헤더 {#rate-limit-headers}

사용량 제한 정보가 제공되는 경우, 응답에는 다음 헤더가 포함됩니다:

| 헤더 | 설명 |
|---|---|
| `X-RateLimit-Limit` | 현재 간격 내에서 허용되는 최대 요청 수입니다. |
| `X-RateLimit-Remaining` | 현재 사용량 제한 창에서 남은 요청 수입니다. |
| `X-RateLimit-Reset` | 현재 사용량 제한 창이 재설정되는 UTC 에포크 시간입니다. |
| `X-RateLimit-Retry-After` | 사용량 제한이 적용된 요청을 재시도하기 전에 대기해야 하는 시간(초)입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="메시징 API 사용량 제한 헤더" }

이 헤더를 사용하여 제한에 도달하기 전에 요청을 줄이거나 일시 중지하세요. 헤더가 모든 응답에 포함되지 않을 수 있습니다.

## 사용량 제한 처리 {#handling-rate-limits}

`429` 응답을 수신한 경우:

1. 해당 워크스페이스에 대한 요청을 중지하거나 줄이세요.
2. `X-RateLimit-Retry-After`가 있는 경우 이를 사용하여 대기 시간을 결정하세요. 그렇지 않으면 `X-RateLimit-Reset`이 제공되는 경우 이를 사용하여 재개 시점을 결정하세요.
3. 지수 백오프와 최대 재시도 횟수를 적용하여 재시도하세요.