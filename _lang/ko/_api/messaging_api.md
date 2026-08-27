---
nav_title: Device Messaging API
article_title: Device Messaging API
search_tag: Endpoint
page_order: 2.2
layout: dev_guide
permalink: /api/device_messaging_api
description: "이 랜딩 페이지에서는 Braze Device Messaging API를 소개합니다."
page_type: landing
hidden: true
guide_top_header: "Device Messaging API"
guide_top_text: "Braze Device Messaging API를 사용하면 Braze SDK를 통합하지 않고도 배너 속성을 검색하고 배너 노출 및 클릭 이벤트를 보고할 수 있습니다. Device Messaging API는 클라이언트 측 및 서버 측 통합을 지원하며, 단일 워크스페이스로 범위가 제한된 클라이언트 측 REST API 키를 사용합니다."
guide_top_text2: "참고: 이 API는 지정된 배너의 속성만 검색하며, 배너 HTML은 반환하지 않습니다."
guide_featured_title: "시작하기"
guide_featured_list:
  - name: "Device Messaging API 개요"
    link: /docs/api/device_messaging_api/overview
    image: /assets/img/braze_icons/annotation-info.svg
  - name: "인증 및 보안"
    link: /docs/api/device_messaging_api/authentication
    image: /assets/img/braze_icons/key-01.svg
  - name: "오류 처리 및 재시도"
    link: /docs/api/device_messaging_api/error_handling
    image: /assets/img/braze_icons/alert-circle.svg
  - name: "사용량 제한"
    link: /docs/api/device_messaging_api/rate_limits
    image: /assets/img/braze_icons/speedometer-01.svg
guide_menu_title: "배너 엔드포인트"
guide_menu_list:
  - name: "POST: 사용자의 배너 조회"
    link: /docs/api/device_messaging_api/endpoints/banners/post_sync_banners
    image: /assets/img/braze_icons/download-01.svg
  - name: "POST: 배너 분석 이벤트 추적"
    link: /docs/api/device_messaging_api/endpoints/banners/post_track_banner_events
    image: /assets/img/braze_icons/line-chart-up-02.svg
---

{% alert important %}
이 페이지는 베타 버전입니다. Device Messaging API의 기능 및 설명서는 변경될 수 있습니다.
{% endalert %}