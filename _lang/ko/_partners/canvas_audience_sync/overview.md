---
nav_title: Audience Sync 소개
article_title: Audience Sync 소개
alias: /partners/about_audience_sync/
description: "이 참조 문서에서는 Braze Audience Sync to Facebook을 사용하여 행동 트리거, 세분화 등을 기반으로 광고를 전달하는 방법을 다룹니다."
page_order: 0
tool:
  - Canvas

---

# Audience Sync 소개 {#about-audience-sync}

> Braze Audience Sync 기능은 캠페인의 도달 범위를 주요 소셜 및 광고 기술로 확장하는 데 도움을 줍니다. [Braze Canvas]({{site.baseurl}}/user_guide/messaging/canvas/)를 통해 브랜드는 퍼스트파티 사용자 데이터를 광고 생태계에 동적이고 안전하게 동기화하여 마케팅 및 운영 효율성을 높일 수 있습니다.

## 기능 가용성 {#feature-availability}

모든 Braze 고객은 Audience Sync to Google 및 Facebook에 즉시 액세스할 수 있으며, Action Credits를 사용하는 고객은 모든 Audience Sync 파트너에 액세스할 수 있습니다. Action Credits를 사용하지 않는 고객이 추가 Audience Sync 대상을 잠금 해제하려면 Audience Sync Pro를 구매하세요. 자세한 내용은 Braze 계정 매니저에게 문의하세요.

## 활용 사례 {#use-cases}

- 자사 및 유료 채널을 사용하여 고가치 사용자를 타겟팅하여 추가 구매 또는 참여를 유도합니다.
- 고가치 사용자의 유사 오디언스를 생성하여 신규 사용자 획득 비용과 전환을 최적화합니다.
- 다른 마케팅 채널에 반응이 적은 사용자를 광고로 리타겟팅합니다.
- 이미 브랜드의 충성 소비자인 사용자가 광고를 받지 않도록 억제 오디언스를 생성합니다.

## 개요 {#overview}

<style>
table td {
    word-break: break-word;
}
</style>

| 대상 | 대상이 오디언스 멤버를 매칭하는 데 걸리는 시간 | 사용량 제한 | 유사 또는 유사 행동 오디언스 | 팁 |
| --- | --- | --- | --- | --- |
| [Criteo]({{site.baseurl}}/partners/canvas_audience_sync/criteo_audience_sync/) | 최대 24시간 | 분당 250,000건의 요청. Google 피드백에 기반한 자동 재시도로 5초마다 배치 처리됩니다. | 예 | {::nomarkdown}<ul><li>Criteo는 최대 1,000개의 광고 오디언스를 지원합니다.</li><li>최소 오디언스 크기는 500이며, 20,000 이상을 권장합니다.</li></ul>{:/} |
| [Facebook 또는 Instagram]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) | 최대 24시간 | 시간당 190,000개의 광고 계정 | 예 | {::nomarkdown}<ul><li>Facebook은 최대 500개의 광고 오디언스를 지원합니다.</li><li>Facebook은 오디언스가 최소 1,000명의 사용자여야 합니다.</li></ul>{:/} |
| [Google Ads 또는 YouTube]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) | 6~12시간 | Google 피드백에 기반한 자동 재시도로 5초마다 배치 처리됩니다 | 아니요 | {::nomarkdown}<ul><li><b>고객 매칭:</b> 모바일 광고 ID, 이메일 주소 또는 전화번호를 사용합니다.</li><li>Google 오디언스는 광고 게재를 시작하려면 최소 5,000명의 사용자가 필요합니다.</li><li>오디언스 크기는 최소 1,000명의 사용자가 될 때까지 0으로 표시됩니다.</li></ul>{:/} |
| [LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync/) | 48시간 | LinkedIn은 초당 10개의 쿼리를 처리하고 요청당 100,000명의 사용자를 처리합니다. Braze는 5초마다 사용자를 배치 처리합니다. | AI 예측 오디언스 | {::nomarkdown}<ul><li>최소 오디언스 크기는 위치 타겟팅을 고려하여 300명입니다.</li><li>LinkedIn은 Braze 대시보드에서 매칭률을 표시합니다.</li></ul>{:/} |
| [Pinterest]({{site.baseurl}}/partners/canvas_audience_sync/pinterest_audience_sync/) | 24~48시간 | Pinterest는 초당 7개의 쿼리를 처리하고 요청당 1,900명의 사용자를 처리합니다. Braze는 5초마다 사용자를 배치 처리합니다. | 예 | Pinterest 오디언스는 최소 100명의 사용자가 필요합니다. |
| [Snapchat]({{site.baseurl}}/partners/canvas_audience_sync/snapchat_audience_sync/) | N/A | Snapchat은 초당 10개의 쿼리를 처리하고 요청당 100,000명의 사용자를 처리합니다. Braze는 5초마다 사용자를 배치 처리합니다. | 예 | Snapchat은 최대 1,000개의 광고 오디언스를 지원합니다. |
| [The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync/) | 최대 24시간 | N/A | 예 | {::nomarkdown}<ul><li>The Trade Desk에서 CRM 오디언스에 대한 최소 오디언스 크기는 없습니다.</li><li>The Trade Desk가 지원하는 오디언스 수에는 제한이 없습니다.</li><li>EU 지역으로 설정된 오디언스에 동기화하는 경우 전화번호는 지원되지 않습니다.</li></ul>{:/} |
| [TikTok]({{site.baseurl}}/partners/canvas_audience_sync/tiktok_audience_sync/) | 24~48시간 | TikTok은 초당 50개의 쿼리를 처리하고 요청당 10,000명의 사용자를 처리합니다. Braze는 5초마다 사용자를 배치 처리합니다. | 예 | {::nomarkdown}<ul><li>TikTok은 최대 400개의 광고 오디언스를 지원합니다.</li><li>TikTok 오디언스는 광고 게재를 시작하려면 최소 1,000명의 사용자가 필요합니다.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="개요" }
<sup>사용량 제한에 도달하면 Braze는 13시간 동안 동기화를 재시도합니다.</sup>

## 작동 방식 {#how-it-works}

Audience Sync to Google 또는 Facebook을 사용하려면 **기술 파트너** 페이지에서 파트너를 검색하여 광고 계정을 연결하세요.

![Facebook 기술 파트너.]({% image_buster /assets/img/audience_sync/facebook_partner.png %}){: style="max-width:35%;"} ![Google Ads 기술 파트너.]({% image_buster /assets/img/audience_sync/google_ads_partner.png %}){: style="max-width:35%;"}

광고 계정을 연결한 후 Audience Sync 단계가 포함된 Canvas를 생성할 수 있습니다.

![사용자 여정에 Audience Sync 단계를 추가하는 Canvas 구성요소 메뉴.]({% image_buster /assets/img/audience_sync/audience_sync7.png %}){: style="max-width:75%;"}

다음으로, 오디언스를 동기화할 파트너를 선택합니다.

![Audience Sync 단계에서 오디언스 동기화 파트너를 선택하는 옵션.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:85%;"}

각 파트너에 대해 Audience Sync 단계의 일부로 다음을 구성해야 합니다:

- 광고 계정
- 오디언스
- 사용자를 추가하거나 제거하는 동작
- 매칭할 필드

Braze는 사용자가 Canvas 내의 Audience Sync 단계에 진입하는 즉시 동기화한다는 점을 유의하세요.

각 Audience Sync 대상에 대해 파트너마다 전송할 수 있는 필드에 대한 요구 사항이 다를 수 있습니다. 자세한 내용은 해당 파트너 설명서를 참조하세요.

### Audience Sync Pro

TikTok, Pinterest, Snapchat 또는 Criteo를 포함한 Audience Sync Pro 파트너를 사용하려면 **기술 파트너** 페이지의 **Audience Sync Pro** 섹션에서 Audience Sync Pro 구매 할당량에 따라 파트너를 선택할 수 있습니다.

![아직 파트너가 선택되지 않은 Audience Sync Pro.]({% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}){: style="max-width:75%;"}

먼저 **파트너 선택**을 선택하여 사용하려는 파트너를 선택합니다. Audience Sync Pro를 구매할 때마다 3개의 Audience Sync Pro 대상이 할당되며, 대시보드 내 각 워크스페이스에서 사용할 수 있습니다.

![Braze에 연결할 최대 3개의 파트너를 선택하는 옵션.]({% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}){: style="max-width:65%;"}

Audience Sync Pro 대상을 선택한 후 파트너 타일을 클릭하여 선택한 파트너 광고 계정을 연결합니다.

![Audience Sync의 파트너로 Snapchat과 TikTok이 선택된 예시.]({% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}){: style="max-width:70%;"}

!["Snapchat 계정 1개를 성공적으로 연결했습니다"라는 메시지가 표시된 Snapchat Audience Sync 설정.]({% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}){: style="max-width:70%;"}

마지막으로, 이 Audience Sync Pro 대상을 사용하여 Canvas에서 Audience Sync 단계를 생성합니다.

### 배치 처리 및 지연 시간 {#batching-and-latency}

사용자가 Canvas의 Audience Sync 단계에 진입하면, Braze는 파트너 API로 전송하기 전에 사용자 업데이트를 집계하는 배치 처리 시스템에 대기열로 추가합니다. 다음 조건 중 하나가 충족되면 배치가 전송됩니다:

- **배치가 크기 제한에 도달한 경우.** 이는 파트너에 따라 다릅니다:
  - 기본값은 최대 2,000명의 사용자를 지원합니다
  - Google Ads는 최대 10,000명의 사용자를 지원합니다
  - Facebook 및 TikTok은 최대 2,000명의 사용자를 지원합니다
- **배치 지연 타이머가 만료된 경우.** 기본값은 1시간이지만, 파트너별로 구성할 수 있습니다. 예를 들어, The Trade Desk는 10분을 사용합니다.

대량 Canvas는 배치가 더 빨리 채워지므로 더 빨리 전송될 수 있습니다. 소량 Canvas는 지연 타이머가 만료될 때까지 대기합니다. Braze는 고정된 전송 시간을 보장하지 않으며, 타이밍은 배치 크기와 구성된 지연 기간에 따라 달라집니다.

Braze는 모니터링 및 문제 해결을 위해 내부 로그에 전송 활동을 기록하지만, 이러한 타임스탬프는 쿼리 가능한 필드로 노출되지 않습니다. Braze가 파트너 API에 배치를 전송한 후, 파트너는 자체 서비스 수준 계약에 따라 오디언스 업데이트를 처리합니다. 일반적으로 6~48시간이 소요됩니다.

Braze는 개별 사용자가 매칭되었거나 동기화되었다는 확인을 파트너로부터 받지 않습니다. 파트너 응답은 매칭 확인이 아닌 수신 확인을 위한 HTTP 응답입니다. 오디언스가 채워졌는지 확인하려면 파트너의 광고 플랫폼(예: Google Ads Audience Manager 또는 Meta Business Manager)을 확인하세요.

### Audience Sync 오류 이메일 {#audience-sync-error-emails}

오류가 전체 파트너 통합과 관련된 경우(예: 승인 문제), 통합을 연결한 사용자에게 이메일이 전송됩니다. 해당 사용자가 더 이상 존재하지 않으면 관리자가 이메일을 받게 됩니다.

오류가 Canvas의 Audience Sync 구성요소와 관련된 문제(예: "오디언스가 존재하지 않음")인 경우, Canvas를 설정한 사용자에게 이메일이 전송됩니다. 해당 사용자가 더 이상 존재하지 않으면 회사 관리자에게 전달됩니다.

이러한 이메일을 받을 사람을 구성하려면 고객 성공 매니저에게 연락하여 **알림 환경설정**에서 수신자를 추가하세요. 이 기능은 현재 동작을 변경하므로, Braze는 기본적으로 누구도 옵트인하지 않기 때문에 오류 이메일이 누락되지 않도록 이 새로운 알림 환경설정에 즉시 수신자를 추가해야 합니다.

## 데이터 프라이버시 고려 사항 {#data-privacy-considerations}

{% alert important %}
이 설명서는 법적 조언을 제공하기 위한 것이 아니며, 법적 조언으로 의존해서는 안 됩니다. Audience Sync의 사용은 특정 법적 요구 사항의 적용을 받습니다. 모든 관련 법률을 준수하여 사용하고 있는지 확인하려면 법률 고문의 조언을 구해야 합니다.
{% endalert %}

광고 추적을 위한 오디언스를 구축할 때, 사용자의 선호도에 따라 특정 사용자를 포함하거나 제외하고, [CCPA](https://oag.ca.gov/privacy/ccpa)에 따른 "판매 또는 공유 금지" 권리와 같은 개인정보 보호법을 준수하고자 할 수 있습니다. 마케터는 Canvas 진입 기준 내에서 사용자 자격에 대한 관련 필터를 구현해야 합니다. 아래에 몇 가지 옵션을 나열합니다.

[Braze SDK를 통해 iOS IDFA]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection)를 수집한 경우, "광고 추적 활성화됨" 필터를 사용할 수 있습니다. 값을 `true`로 선택하면 옵트인한 사용자만 Audience Sync 대상으로 전송됩니다.

![진입 오디언스가 "광고 추적 활성화됨이 true"인 Canvas.]({% image_buster /assets/img/audience_sync/audience_sync2.png %})

`opt-ins`, `opt-outs`, `Do Not Sell Or Share` 또는 기타 관련 커스텀 속성을 수집하는 경우, Canvas 진입 기준에 필터로 포함해야 합니다:

![진입 오디언스가 "opted_in_marketing이 true"인 Canvas.]({% image_buster /assets/img/audience_sync/audience_sync.png %})

Braze 플랫폼 내에서 이러한 데이터 보호법을 준수하는 방법에 대해 자세히 알아보려면 [데이터 보호 기술 지원]({{site.baseurl}}/dp-technical-assistance/)을 참조하세요.

## 광고 타겟팅에 대한 동의 관리 {#managing-consent-for-ad-targeting}

광고주로서 사용자의 광고 추적 또는 타겟팅에 대한 동의를 관리하는 것은 귀하의 책임입니다.

사용자에게 광고를 전송하려면 모든 관련 법률 및 규정, 그리고 광고 플랫폼의 정책 및 요구 사항을 준수해야 합니다. 동의를 얻은 사용자에 대해서만 Braze를 사용하여 타겟팅하고 동기화하세요.

이러한 광고 플랫폼에서 오디언스 목록을 최신 상태로 유지하고 동의를 철회한 사용자를 제거하려면, Audience Sync 단계를 사용하여 기존 오디언스 목록에서 사용자를 제거하는 Canvas를 설정하세요.