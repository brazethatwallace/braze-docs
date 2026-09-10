---
nav_title: API 및 식별자
article_title: API 및 식별자
page_order: 0
page_type: reference
description: "이 문서에서는 워크스페이스의 API 식별자를 표시하는 API 및 식별자 페이지에 대해 설명합니다."
---

# API 및 식별자 {#apis-and-identifiers}

> **API 및 식별자** 페이지는 모든 REST API 키를 한 곳에서 관리할 수 있는 중앙 허브입니다. 여기에서 각 워크스페이스의 API 키 및 앱 식별자 세트에 접근할 수 있습니다.

**API 및 식별자** 페이지는 **설정** > **설정 및 테스트** > **API 및 식별자**에서 찾을 수 있습니다.

## API 키 {#api-keys}

이 섹션에서는 워크스페이스의 REST API 키를 제공합니다. 이 키는 워크스페이스의 데이터에 접근할 수 있게 해주는 고유 식별자입니다. Braze API에 요청할 때마다 REST API 키가 필요합니다. API 키 생성 및 사용에 대한 자세한 내용은 [REST API 키 개요]({{site.baseurl}}/api/basics)를 참조하세요.

### API IP 허용 목록 {#api-ip-allowlisting}

추가적인 보안을 위해 특정 REST API 키에 대해 REST API 요청을 보낼 수 있는 IP 주소 및 서브넷 목록을 지정할 수 있습니다. 이를 IP 허용 목록이라고 합니다. 특정 IP 주소 또는 서브넷을 허용하려면 새 REST API 키를 생성할 때 **Allowlist IPs** 섹션에 추가하세요.

![새 REST API 키 생성 시 API IP 허용 목록 섹션]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

아무것도 지정하지 않으면 모든 IP 주소에서 요청을 보낼 수 있습니다.

{% alert tip %}
Braze 간 웹훅을 만들면서 허용 목록을 사용하고 계신가요? [허용 목록에 추가할 IP]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting) 목록을 확인하세요.
{% endalert %}

### API 사용량 알림 {#api-usage-alerts}

API 사용량 알림을 설정하면 주요 API 활동을 모니터링하고 문제를 조기에 발견할 수 있습니다. 이 알림은 예상치 못한 트래픽 패턴이 사용 환경에 영향을 미치기 전에 감지하는 데 도움이 됩니다.

두 가지 유형의 API 활동을 추적할 수 있습니다.

- **REST API 엔드포인트:** 메시지 전송, Campaign 생성, 데이터 내보내기 등의 작업입니다.
- **SDK API 요청:** 인앱 메시지 트리거 또는 고객 프로필 동기화 등 고객 경험에서 발생하는 이벤트입니다. *이 기능은 월간 활성 사용자(CY 24–25)를 구매한 경우 사용할 수 있습니다.*

추적할 항목을 선택한 후 알림 조건을 정의할 수 있습니다. 예를 들어, 1시간 이내에 오류 응답이 20% 증가하면 알림을 받을 수 있습니다. 설정에 따라 이메일, 웹훅 또는 두 가지 모두로 알림을 받게 됩니다. 시작하려면 [API 사용량 알림]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts)을 참조하세요.

## 앱 식별자 {#app-identifiers}

이 섹션에는 Braze API에 대한 요청에서 특정 앱을 참조하는 데 사용되는 식별자 목록이 포함되어 있습니다. 앱 식별자에 대해 자세히 알아보려면 [앱 식별자 API 키]({{site.baseurl}}/api/identifier_types)를 참조하세요.

## 기타 식별자 {#other-identifiers}

Braze 외부 API에서 접근하려는 Segments, Campaigns, Content Cards 등과 관련된 식별자를 검색하여 API와 연동할 수 있습니다. 모든 메시지는 [UTF-8](https://en.wikipedia.org/wiki/UTF-8) 인코딩을 따라야 합니다. 항목을 선택하면 드롭다운 메뉴 아래에 식별자가 표시됩니다.

자세한 내용은 [API 식별자 유형]({{site.baseurl}}/api/identifier_types)을 참조하세요.