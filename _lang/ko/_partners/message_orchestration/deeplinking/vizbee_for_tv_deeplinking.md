---
nav_title: Vizbee
article_title: Vizbee TV 딥링킹
alias: /partners/vizbee/
page_type: partner
description: "이 참조 문서에서는 Braze와 Vizbee 간의 파트너십과 이를 사용하여 TV 딥링킹을 지원하는 방법을 설명합니다."
search_tag: Partner

---
# Vizbee {#vizbee}

> [Vizbee](https://vizbee.tv/)는 가정 내 모든 스마트폰과 스마트 TV가 하나의 매끄러운 기기처럼 함께 작동하여 뛰어난 사용자 경험을 제공할 수 있도록 합니다. Vizbee는 알림, 딥링크, 이메일과 같은 기존 모바일 앱 마케팅 채널을 사용하여 모든 커넥티드 TV(CTV) 기기(예: Roku, FireTV, 삼성 TV, LG TV 등)에서 시청자를 원활하게 확보하고 참여시킬 수 있도록 지원합니다.

_이 통합은 Vizbee에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Vizbee 통합을 사용하면 단일 콘솔에서 모바일 및 CTV 기기의 스트리밍 앱에서 시청자를 확보하고 유지하기 위한 마케팅 캠페인을 예약할 수 있습니다. 이 통합을 통해 다음을 수행할 수 있습니다:
- 타겟 사용자에게 모바일 알림을 예약하여, 탭하면 모바일 앱 시청으로 이어지거나 근처 스트리밍 기기 또는 TV에서 원활하게 재생을 시작할 수 있습니다.
- 타겟 사용자에게 이메일 마케팅 캠페인을 예약하여, 탭하면 Roku 또는 FireTV와 같은 CTV 기기에서 자동으로 CTV 앱이 설치되고 사용자가 로그인할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Vizbee 계정 | 이 파트너십을 활용하려면 [Vizbee](https://vizbee.tv/) 계정이 필요합니다. Vizbee에 앱을 등록하고 Vizbee ID를 할당받아야 합니다. |
| iOS 또는 Android 앱 | 이 통합은 iOS 및 Android 앱을 지원합니다. 플랫폼에 따라 애플리케이션에 코드 스니펫이 필요할 수 있습니다. |
| Vizbee SDK | 필수 Braze SDK 외에도 Vizbee SDK를 설치해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

Vizbee의 [SDK 통합 가이드](https://console.vizbee.tv/app/vzb1765003429/develop/guides/ios-continuity)를 따라 Vizbee와 Braze 통합을 시작하세요. 여기에서 모바일-TV 딥링킹, TV 앱 설치 및 시청 기여도에 대한 안내를 확인할 수 있습니다.

### 설치 및 기여도 보고서 보기 {#vizbee-tv-app-installs-viewership-attribution}

Vizbee와 Braze를 사용하면 모바일 및 CTV 기기 전반에 걸친 캠페인의 전체적인 성과를 확인할 수도 있습니다. Vizbee SDK는 커스텀 이벤트를 Braze SDK로 전송하며, 이를 Braze 대시보드의 캠페인 보고서에서 확인할 수 있습니다.