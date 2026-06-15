---
nav_title: SDK 개요
article_title: SDK 개요
page_order: 9
page_type: reference
description: "이 참조 문서는 Braze SDK의 기본 사항을 다룹니다."
---

# SDK 개요 {#sdk-overview}

> Braze SDK는 세션 데이터를 수집하고, 사용자를 식별하며, 웹사이트나 앱을 통해 구매 및 커스텀 이벤트를 기록합니다. SDK를 사용하여 Braze 대시보드에서 직접 In-App Messages와 푸시 알림을 보내 사용자와 소통할 수도 있습니다.

간단히 말해서, Braze SDK는:
* 사용자 데이터를 수집하고 통합된 고객 프로필로 동기화합니다
* 마케팅 참여 데이터 및 비즈니스에 특화된 커스텀 데이터를 캡처합니다
* 푸시 알림, In-App Messages 및 콘텐츠 카드 메시징 채널을 지원합니다

## SDK란 무엇입니까? {#what-is-an-sdk}
소프트웨어 개발 키트(SDK)는 새로운 기능을 지원하기 위해 디지털 애플리케이션에 추가할 수 있는 사전 제작된 도구 세트&mdash;작은 코드 블록들&mdash;입니다. Braze SDK는 앱 또는 사이트로 정보를 보내고 받는 데 사용됩니다. 고객 프로필 생성, 커스텀 이벤트 로깅, 푸시 알림 트리거링 등 시작부터 필수 기능을 제공하도록 설계되었습니다.

이 기능은 Braze에서 기본으로 제공되므로 개발자는 핵심 비즈니스에 집중할 수 있습니다. SDK가 없으면 모든 Braze 클라이언트는 데이터 처리, 세분화 논리, 전달 옵션, 익명 사용자 처리, Campaign 분석 등을 위한 모든 인프라와 도구를 완전히 처음부터 만들어야 합니다. 이는 SDK를 통합하는 데 걸리는 한 시간 정도보다 훨씬 더 오래 걸리고 훨씬 더 고통스러울 것입니다.

## 구현 {#implementation}

앱이나 사이트에 SDK를 통합하려면 누군가가 SDK의 코드를 해당 애플리케이션을 구동하는 전체 코드 베이스에 추가해야 합니다. 이는 엔지니어링 팀이 참여하여 본질적으로 앱을 연결하여 정보와 동작이 앱 사이에서 흐르도록 한다는 것을 의미합니다. 하지만 개발자가 참여하더라도 SDK는 가볍고 통합하기 쉽게 설계되었습니다.

시간을 절약하고 원활한 통합을 보장하기 위해 마케팅 팀과 엔지니어링 팀이 커스텀 이벤트, 커스텀 속성 및 SDK를 동시에 설정할 것을 권장합니다. 마케팅 팀과 엔지니어링 팀이 함께 검토해야 할 단계에 대해 자세히 알아보려면 [구현 문서]({{site.baseurl}}/user_guide/get_started/integrations/)를 참조하세요.

## 데이터 집계 {#data-aggregation}

Braze SDK는 사용자 수준의 데이터를 자동으로 캡처하여 앱과 사용자 기반에 대한 주요 측정기준을 제공합니다. 유사한 앱을 단일 워크스페이스로 그룹화하여(예: iOS 및 Android 버전을 함께) 플랫폼 간 수집된 데이터를 보고 사용자 활동의 전체 그림을 구축할 수 있습니다. 자세한 내용은 [홈 페이지]({{site.baseurl}}/user_guide/analytics/dashboards/home/) 문서를 참조하세요.

## 인앱 메시징 {#in-app-messaging}

SDK를 사용하여 In-App Messages를 직접 작성하고 보낼 수 있습니다. Campaign 전략에 따라 슬라이드업, 모달 또는 전체화면 메시지를 선택할 수 있습니다. 작성 세부 정보는 [In-App Messages 만들기]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/)를 참조하세요.

![웹 브라우저에 표시된 푸시]({% image_buster /assets/img_archive/web_push_macbook.png %}){: style="float:right;max-width:45%;margin-left:20px;border:0;"}

## 푸시 알림 {#push-notifications}

푸시 알림은 사용자와 소통할 수 있는 또 다른 훌륭한 옵션이며, 특히 시간에 민감한 행동 유도를 처리하는 데 유용합니다. 모바일 푸시 알림은 사용자의 기기에 나타나며, 웹 푸시 알림은 사이트가 열려 있지 않을 때에도 나타납니다. 푸시 알림 사용에 대한 자세한 내용은 [푸시 알림 문서]({{site.baseurl}}/user_guide/channels/push/)를 참조하세요.

웹사이트 또는 앱 사용자는 푸시 알림을 받기 위해 옵트인해야 합니다. 자세한 내용은 [푸시 프라이밍]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages/)을 참조하세요.

## 세분화 및 전달 규칙 {#segmentation-and-delivery-rules}

기본적으로 In-App Messages를 포함하는 Campaign은 해당 워크스페이스의 모든 버전의 앱으로 전송됩니다. 예를 들어, 메시지는 웹 및 모바일 사용자 모두에게 전송됩니다. 웹 또는 모바일에만 In-App Messages를 보내려면 Campaign을 적절하게 세분화해야 하며, 이는 기본적으로 Braze SDK를 통해 지원됩니다.

**Apps and websites targeted**를 **Users from specific apps**로 설정한 다음 **Specific Apps**에서 웹사이트만 선택하여 웹 사용자 Segment를 생성할 수 있습니다.

![웹 앱에 초점을 맞춘 Segment 세부 정보 페이지]({% image_buster /assets/img_archive/web-users-segment.png %}){:style="max-width:60%"}

이를 통해 사용자의 행동을 기반으로 지능적으로 타겟팅할 수 있습니다. 웹 사용자가 모바일 앱을 다운로드하도록 유도하려면 이 Segment를 타겟 오디언스로 설정하면 됩니다. 모바일 In-App Messages는 포함하지만 웹 메시지는 포함하지 않는 메시징 캠페인을 보내려면 Segment에서 웹사이트 아이콘의 선택을 해제하면 됩니다.

## 지원되는 플랫폼 {#supported-platforms}

Braze는 웹, Android 및 Swift와 같은 여러 플랫폼에 대한 SDK를 제공합니다. 전체 목록은 [Braze 개발자 가이드]({{site.baseurl}}/developer_guide/home/)를 참조하세요.