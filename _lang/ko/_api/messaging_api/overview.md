---
nav_title: 개요
article_title: 기기 메시징 API 개요
permalink: /api/device_messaging_api/overview
page_order: 0
page_type: reference
description: "Braze 기기 메시징 API와 얼리 액세스 기능에 대해 알아보세요."
hidden: true
---

# 기기 메시징 API 개요 {#device-messaging-api-overview}

Braze 기기 메시징 API는 Braze SDK 없이 Braze 메시징 기능을 통합하기 위한 REST 엔드포인트 세트입니다. 클라이언트 또는 서버 애플리케이션에서 이러한 엔드포인트를 호출할 수 있습니다.

{% alert important %}
이 페이지는 베타 버전입니다. 기기 메시징 API의 기능과 설명서는 변경될 수 있습니다. 액세스를 요청하려면 Braze 계정 매니저에게 문의하세요.
{% endalert %}

## 지원되는 기능 {#supported-capabilities}

얼리 액세스 기간 동안 기기 메시징 API를 사용하여 다음을 수행할 수 있습니다.

- 외부 사용자 ID 및 배치 세트에 대해 [적격한 배너 검색]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_sync_banners)
- [배너 노출 횟수 및 클릭 이벤트 보고]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_track_banner_events)

기기 메시징 API는 커스텀 인터페이스를 구축할 수 있도록 구조화된 배너 속성정보를 반환합니다. 렌더링된 HTML은 반환하지 않습니다.

## 통합 요구 사항 {#integration-requirements}

Device Messaging API를 통합하려면 다음이 필요합니다:

- Device Messaging API가 활성화된 워크스페이스
- 해당 워크스페이스의 클라이언트 측 REST API 키
- 해당 워크스페이스의 REST 엔드포인트
- 사용자의 외부 사용자 ID
- 앱의 API 식별자

자격 증명에 대한 자세한 내용은 [인증 및 보안]({{site.baseurl}}/api/device_messaging_api/authentication)을 참조하세요.

## 기기 메시징 API 및 REST API 안내 {#device-messaging-api-and-rest-api-guidance}

기기 메시징 API는 Braze REST API와 동일한 리전별 REST 엔드포인트를 사용하지만, 별도의 인증 및 응답 계약을 따릅니다. 비공개 서버 측 키, 응답 본문, 오류, 사용량 제한에 대한 일반적인 REST API 안내는 기기 메시징 API 문서에서 명시적으로 참조하지 않는 한 적용되지 않습니다.

요청 필드, 응답 본문, 상태 코드 및 제한 사항에 대한 정확한 정보는 기기 메시징 API 엔드포인트 설명서를 기준으로 참조하세요.