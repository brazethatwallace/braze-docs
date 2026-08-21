---
nav_title: 인증 및 보안
article_title: Messaging API 인증 및 보안
page_order: 1
page_type: reference
description: "Messaging API 요청을 안전하게 인증하는 방법을 알아보세요."
hidden: true
---

# Messaging API 인증 및 보안 {#messaging-api-authentication-and-security}

{% alert important %}
이 페이지는 베타 버전입니다. Messaging API의 기능과 설명서는 변경될 수 있습니다.
{% endalert %}

Messaging API는 클라이언트 측 REST API 키를 사용합니다. 이 키는 서버 측 Braze REST API 요청에 사용되는 비공개 REST API 키와는 별개입니다.

## 클라이언트 측 REST API 키 {#client-side-rest-api-keys}

클라이언트 측 REST API 키는 하나의 워크스페이스로 범위가 제한되며 Messaging API 권한으로만 사용할 수 있습니다. 이 키를 클라이언트 애플리케이션에 포함할 수 있습니다.

{% alert important %}
클라이언트 애플리케이션에서는 클라이언트 측 REST API 키만 사용하세요. 절대 비공개 서버 측 REST API 키를 클라이언트 측 코드에 노출하지 마세요.
{% endalert %}

클라이언트 측 REST API 키를 생성하려면:

1. Braze 대시보드에서 **설정** > **API 및 식별자** > **API 키**로 이동합니다.
2. **API 키 생성**을 선택합니다.
3. **키 유형**에서 **클라이언트**를 선택합니다.
4. Banner를 가져오려면 `banners.sync` 권한을, Banner 이벤트를 보고하려면 `banners.track` 권한을, 또는 두 가지 모두를 할당합니다.

## 요청 인증 {#authenticating-requests}

클라이언트 측 REST API 키를 `Authorization` 헤더에 Bearer 토큰으로 전송합니다:

```bash
Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}
```

HTTPS와 Braze 인스턴스에 해당하는 [REST 엔드포인트]({{site.baseurl}}/api/basics#endpoints)를 사용하세요.

## 사용자 신원 {#user-identity}

클라이언트 측 REST API 키는 호출하는 애플리케이션과 워크스페이스를 인증하며, 사용자를 인증하지는 않습니다. 요청의 `external_user_id`는 Banner 콘텐츠 및 이벤트와 연결된 사용자를 식별합니다.

Messaging API 요청을 수행하기 전에 애플리케이션의 인가 제어를 적용하세요.

## 인증 오류 {#authentication-errors}

인증 및 권한 실패는 엔드포인트에 따라 다를 수 있습니다. 각 엔드포인트의 상태 코드 표와 [Messaging API 오류 처리]({{site.baseurl}}/api/messaging_api/error_handling)를 참조하세요.