---
nav_title: 인증 및 보안
article_title: Device Messaging API 인증 및 보안
permalink: /api/device_messaging_api/authentication
page_order: 1
page_type: reference
description: "Device Messaging API 요청을 안전하게 인증하는 방법을 알아보세요."
hidden: true
---

# Device Messaging API 인증 및 보안 {#device-messaging-api-authentication-and-security}

{% alert important %}
이 페이지는 베타 버전입니다. Device Messaging API의 기능과 설명서는 변경될 수 있습니다.
{% endalert %}

Device Messaging API는 클라이언트 측 REST API 키를 사용합니다. 이 키는 서버 측 Braze REST API 요청에 사용되는 비공개 REST API 키와는 별개입니다.

## 클라이언트 측 REST API 키 {#client-side-rest-api-keys}

클라이언트 측 REST API 키는 하나의 워크스페이스로 범위가 제한되며 기기 메시징 API 권한으로 제한됩니다. 이러한 키는 클라이언트 애플리케이션에 임베드할 수 있습니다.

{% alert important %}
클라이언트 애플리케이션에서는 클라이언트 측 REST API 키만 사용하세요. 비공개 서버 측 REST API 키를 클라이언트 측 코드에 절대 노출하지 마세요.
{% endalert %}

클라이언트 측 REST API 키를 생성하려면 다음과 같이 합니다:

1. Braze 대시보드에서 **설정** > **API 및 식별자** > **API 키**로 이동합니다.
2. **API 키 생성**을 선택합니다.
3. **키 유형**에서 **클라이언트**를 선택합니다.
4. 배너를 검색하려면 `banners.sync` 권한을, 배너 이벤트를 보고하려면 `banners.track` 권한을, 또는 두 권한 모두를 할당합니다.

## 요청 인증 {#authenticating-requests}

클라이언트 측 REST API 키를 `Authorization` 헤더에 bearer 토큰으로 전송합니다:

```bash
Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}
```

HTTPS와 Braze 인스턴스에 해당하는 [REST 엔드포인트]({{site.baseurl}}/api/basics#endpoints)를 사용합니다.

## 사용자 신원 {#user-identity}

클라이언트 측 REST API 키는 사용자가 아닌 호출 애플리케이션과 워크스페이스를 인증합니다. 요청의 `external_user_id`는 배너 콘텐츠 및 이벤트와 연결된 사용자를 식별합니다.

기기 메시징 API 요청을 수행하기 전에 애플리케이션의 인증 제어를 적용하세요.

## 인증 오류 {#authentication-errors}

인증 및 권한 실패는 엔드포인트에 따라 다를 수 있습니다. 각 엔드포인트의 상태 코드 표와 [기기 메시징 API 오류 처리]({{site.baseurl}}/api/device_messaging_api/error_handling)를 참조하세요.