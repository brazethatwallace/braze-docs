---
nav_title: 실시간 인앱 메시지 전달
article_title: 실시간 인앱 메시지 전달
permalink: "/real_time_in_app_messages/"
description: "이 페이지에서는 실시간 인앱 메시지 전달 얼리 액세스에 대해 다룹니다. 이 기능은 다음 세션 시작을 기다리지 않고 사용자가 자격을 갖추는 즉시 인앱 메시지를 기기에 전달합니다."
page_type: reference
hidden: true
noindex: true
---

# 실시간 인앱 메시지 전달 {#real-time-in-app-message-delivery}

> 실시간 전달을 사용하면 Braze는 사용자가 자격을 갖추는 즉시 인앱 메시지를 기기에 전송합니다. 사용자가 세션 중간에 자격을 갖추게 된 인앱 메시지를 수신하기 위해 더 이상 새 세션을 시작할 필요가 없습니다.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Real-time in-app message delivery' type='early_access' %}

## 작동 방식 {#how-it-works}

실시간 전달이 없으면 SDK는 세션 시작 시 적격한 인앱 메시지를 요청하고 기기에 캐시합니다. 세션 도중 적격해진 사용자는 다음 세션이 시작될 때까지 메시지를 받지 못합니다. 이 동작에 대한 자세한 내용은 [인앱 메시지 트리거]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages)를 참조하세요.

실시간 전달을 사용하면 Braze는 세션 중 SDK가 유지하는 실시간 연결을 통해 기기에 메시지를 푸시합니다. Braze는 두 가지 경우에 메시지를 보냅니다:

- 사용자가 인앱 메시지 Campaign에 적격해진 경우
- 사용자가 Canvas의 인앱 메시지 단계로 진행한 경우

실시간 전달은 메시지가 기기에 도달하는 시점을 변경합니다. 표시 동작은 동일하게 유지됩니다: 메시지는 트리거 이벤트가 발생할 때까지 대기한 후 표시됩니다.

### Campaigns에 미치는 영향 {#what-this-means-for-your-campaigns}

| 시나리오 | 실시간 전달 미사용 시 | 실시간 전달 사용 시 |
| --- | --- | --- |
| 사용자가 세션 도중 인앱 메시지 Campaign에 적격해진 경우 | 다음 세션 시작 시 메시지가 도착합니다 | 현재 세션 중 메시지가 도착합니다 |
| 사용자가 세션 도중 Canvas의 인앱 메시지 단계에 도달한 경우 | 다음 세션 시작 시 메시지가 도착합니다 | 현재 세션 중 메시지가 도착합니다 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="실시간 인앱 메시지 전달 비교" }

## SDK 요구 사항 {#sdk-requirements}

실시간 전달을 위해서는 다음과 같은 최소 SDK 버전이 필요합니다:

{% sdk_min_versions swift:18.0.0 android:43.1.1 web:6.12.0 %}

SDK 버전에 관계없이 기기는 세션 시작 시 인앱 메시지를 계속 수신합니다.

## 현재 제한 사항 {#current-limitations}

- **실시간 Campaign에 대한 편집은 다음 세션 시작 시 적용됩니다:** 기기가 이미 수신한 인앱 메시지를 변경하면, 해당 기기는 사용자의 다음 세션이 시작될 때까지 기존 버전을 유지합니다.

## 얼리 액세스에 참여하기 {#participate-in-early-access}

1. Braze 계정 매니저에게 연락하여 워크스페이스를 얼리 액세스에 추가하세요.
2. 앱을 플랫폼의 최소 SDK 버전으로 업그레이드하세요.
3. 업그레이드된 앱을 사용자에게 릴리스하세요.

실시간 전달에는 대시보드 구성, Campaign 변경 또는 SDK 코드 변경이 필요하지 않습니다. 워크스페이스가 얼리 액세스에 추가되면 실시간 전달이 기존 인앱 메시지 Campaigns 및 Canvases에 자동으로 적용됩니다.

## 피드백 공유 {#share-feedback}

Braze는 이 기능을 적극적으로 개발하고 있으며, 여러분의 피드백이 정식 출시에 반영됩니다. 전송 타이밍에 대한 관찰 사항, 예상과 다르게 동작한 부분, 그리고 실시간 전송이 다음으로 지원했으면 하는 시나리오를 계정 매니저에게 보내주세요.