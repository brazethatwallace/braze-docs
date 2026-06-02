---
nav_title: Apteligent
article_title: Apteligent
alias: /partners/apteligent/
description: "이 참조 문서에서는 Braze와 Apteligent 간의 파트너십을 설명합니다. Apteligent는 크래시 리포팅을 제공하는 모바일 애플리케이션으로, 기존 Braze 솔루션에 중요한 데이터를 기록할 수 있습니다."
page_type: partner
search_tag: Partner

---

# Apteligent

> [Apteligent](https://www.vmware.com/products/workspace-one/intelligence-consumer-apps.html)는 개발자와 제품 매니저에게 도구와 인사이트를 제공하는 모바일 애플리케이션 성능 플랫폼입니다.

_이 통합은 Apteligent에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Apteligent 통합은 상세한 iOS 크래시 리포팅을 제공하여, 기존 Braze 솔루션에 중요한 데이터를 기록하고 애플리케이션 크래시를 경험한 사용자를 세분화하고 이해하며 참여시킬 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| TestDrive 계정 | 이 파트너십을 활용하려면 TestDrive 계정이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

{% alert warning %}
이 통합은 현재 iOS에서만 지원됩니다.
{% endalert %}

## 통합 {#apteligent-ios-integration}

### 1단계: 옵저버 등록 {#step-1-register-an-observer}

먼저 옵저버를 등록해야 합니다. Apteligent를 초기화하기 전에 이 작업을 수행해야 합니다.

```objc
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(crashDidOccur:)
                                             name:@"CRCrashNotification"
                                           object:nil];
```

### 2단계: 커스텀 크래시 분석 기록 {#step-2-log-custom-crash-analytics}

Apteligent SDK는 크래시가 발생한 후 사용자가 애플리케이션을 로드할 때 알림을 발생시킵니다. 이 알림에는 크래시 이름, 원인, 발생 날짜가 포함됩니다.

알림을 수신하면 커스텀 크래시 이벤트를 기록하고 Apteligent의 크래시 리포팅 분석으로 사용자 속성을 업데이트합니다:

```objc
- (void)crashDidOccur:(NSNotification*)notification {
  NSDictionary *crashInfo = notification.userInfo;
  [[Appboy sharedInstance] logCustomEvent:@"ApteligentCrashEvent" withProperties:crashInfo];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashName" andStringValue:crashInfo[@"crashName"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashReason" andStringValue:crashInfo[@"crashReason"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashDate" andDateValue:crashInfo[@"crashDate"]];
}
```

완료되면 Apteligent 플랫폼에서 확인된 크래시 정보를 사용하여 Braze의 세분화 및 참여 분석 기능을 활용할 수 있습니다.