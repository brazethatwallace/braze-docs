---
nav_title: 4월
page_order: 9
noindex: true
page_type: update
description: "이 문서에는 2017년 4월의 릴리스 노트가 포함되어 있습니다."
---

# 2017년 4월 {#april-2017}

## HTML 인브라우저 메시지 {#html-in-browser-messages}

이제 커스텀 HTML 및 이메일 캡처 형식을 포함한 인터랙티브 인브라우저 메시지 유형을 지원하므로 고객이 어디에 있든 고객에게 다가갈 수 있습니다. [인앱 메시지]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices)에 대해 자세히 알아보세요.

## 연결된 콘텐츠가 포함된 개인화된 인앱 메시지 {#personalized-in-app-message-with-connected-content}

트리거된 인앱 메시지에 {% raw %} {%connected_content%} {% endraw %} 블록을 추가하여 API를 통해 액세스할 수 있는 모든 정보를 메시지에 직접 삽입함으로써 풍부한 개인화 기능을 추가할 수 있습니다. 이제 푸시, 이메일, 웹훅 외에도 앱 내에서 연결된 콘텐츠를 사용할 수 있습니다. [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)에 대해 자세히 알아보세요.

## 뉴스피드 카드 탐색 기능 개선 {#improved-navigation-for-news-feed-cards}

뉴스피드 카드 제작 UI를 개선하여 캠페인을 더 쉽게 탐색하고 만들 수 있도록 했습니다. [뉴스피드 카드]({{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item#news-feed-cards)에 대해 자세히 알아보세요.

## iOS 리치 알림의 미리보기 개선 {#improved-preview-for-ios-rich-notifications}

이제 iOS의 미리보기 알림에 리치 알림이 표시되어 고객에게 보내는 내용을 글꼴 크기까지 정확하게 확인할 수 있습니다. [iOS 리치 알림]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#ios-10-rich-notifications)에 대해 자세히 알아보세요.

## 푸시 통계에 "영향받은 열람 수" 추가 {#added-influenced-opens-to-push-statistics}

Braze에서 제공하는 표준 Campaign 및 Canvas 통계 목록에 "영향받은 열람 수"를 추가하여 영향받은 열람, 직접 열람 및 총 열람 수의 Campaign 내역을 더 쉽게 파악할 수 있도록 했습니다. [영향받은 열람 수]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens)에 대해 자세히 알아보세요.

## 내부 그룹으로 업그레이드 {#upgrade-to-internal-groups}

이제 여러 개의 내부 그룹을 만들고 해당 그룹을 SDK 로깅, REST API 로깅 또는 메시지 콘텐츠 테스트에 사용할지 여부를 나타내는 속성을 할당할 수 있습니다. [이벤트 사용자 로그]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab#event-user-log-tab)에 대해 자세히 알아보세요.

> 업데이트: 내부 그룹을 사용하여 [시드 이메일을 보낼]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console#seed-groups) 수도 있습니다.

## 웹 URL에 대한 새로운 옵션 {#new-options-for-web-urls}

이제 푸시 메시지, 인앱 및 인브라우저 메시지, 뉴스피드 카드에 대해 외부 웹 브라우저에서 웹 URL을 열 수 있는 옵션이 제공됩니다. "앱으로 딥링크" 동작은 이제 HTTP/HTTPS 딥링크와도 호환됩니다. Branch or 브랜치 또는 Apple의 유니버설 링크와 같은 파트너를 사용하는 경우 SDK 커스터마이징이 필요합니다. [딥링킹]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#what-is-deep-linking)에 대해 자세히 알아보세요.

## 새로운 "전환 수행" 이벤트 Canvas {#new-performed-conversion-event-canvas}

새로운 "전환 수행" 이벤트와 "Canvas 컨트롤 내" 필터를 추가하여 리타겟팅 옵션을 개선했습니다. [리타겟팅 필터]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns) 사용에 대해 자세히 알아보세요.