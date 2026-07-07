---
nav_title: Google
article_title: Google에 Canvas Audience Sync
alias: /google_audience_sync/
description: "이 참조 문서에서는 Braze Audience Sync to Google을 사용하여 행동 트리거, 세분화 등을 기반으로 광고를 전달하는 방법을 다룹니다."
tool:
  - Canvas
page_order: 3

---

# Google에 Audience Sync {#audience-sync-to-google}

{% alert important %}
Google은 2024년 3월 6일부터 시행되는 [디지털 시장법(DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html)의 변경 사항에 대응하여 [EU 사용자 동의 정책](https://www.google.com/about/company/user-consent-policy/)을 업데이트하고 있습니다. 이 새로운 변경 사항은 광고주가 EEA, 영국 및 스위스 최종 사용자에게 특정 정보를 공개하고 필요한 동의를 얻도록 요구합니다. 자세한 내용은 다음 설명서를 검토하세요.
{% endalert %}

Braze Audience Sync to Google 통합을 통해 브랜드는 크로스채널 고객 여정의 도달 범위를 Google 검색, Google 쇼핑, Gmail, YouTube 및 Google 디스플레이로 확장할 수 있습니다. 퍼스트파티 고객 데이터를 사용하여 동적 행동 트리거, 세분화 등을 기반으로 안전하게 광고를 전달할 수 있습니다. Braze Canvas의 일부로 메시지(예: 푸시, 이메일 또는 SMS)를 트리거하는 데 일반적으로 사용하는 모든 기준을 Google의 [Customer Match](https://support.google.com/google-ads/answer/6379332?hl=en)를 통해 해당 사용자에게 광고를 트리거하는 데 사용할 수 있습니다.

{% alert note %}
Braze Audience Sync to Google 통합은 Google Ads를 지원하며, Google Ads Manager는 지원하지 않습니다.
{% endalert %}

Google Ads는 더 이상 타겟팅 및 보고를 위한 유사 오디언스("유사 잠재고객"이라고도 함)를 생성하지 않습니다. 자세한 내용은 [Google Ads 설명서](https://support.google.com/google-ads/answer/12463119?)를 참조하세요.

**커스텀 오디언스 동기화의 일반적인 사용 사례:**
- 여러 채널을 통해 고가치 사용자를 타겟팅하여 구매 또는 인게이지먼트를 유도합니다.
- 다른 마케팅 채널에 덜 반응하는 사용자를 리타겟팅합니다.
- 이미 브랜드의 충성 소비자인 사용자가 광고를 받지 않도록 억제 오디언스를 생성합니다.

{% alert note %}
이 기능을 통해 브랜드는 Google과 공유되는 특정 퍼스트파티 데이터를 제어할 수 있습니다. Braze에서는 퍼스트파티 데이터를 공유할 수 있는 통합과 공유할 수 없는 통합에 대해 최대한 신중하게 고려합니다. 자세한 내용은 [Braze 데이터 프라이버시 정책](https://www.braze.com/privacy)을 참조하세요.
{% endalert %}

## 필수 조건 {#prerequisites}

Canvas에서 Google Audience 단계를 설정하기 전에 다음 항목이 생성되고 완료되었는지 확인하세요.

| 요구 사항 | 출처 | 설명 |
| ----------- | ------ | ----------- |
| Google Ads 계정 | [Google](https://support.google.com/google-ads/answer/6366720?hl=en) | 브랜드의 활성 Google Ads 계정.<br><br>여러 관리 계정에 걸쳐 오디언스를 공유하려면 [관리자 계정](https://support.google.com/google-ads/answer/6139186)에 오디언스를 업로드할 수 있습니다. |
| Google Ads 약관 및 Google Ads 정책 | [Google](https://support.google.com/adspolicy/answer/54818?hl=en) | Braze Audience Sync 사용 시 [Google 광고 약관](https://payments.google.com/u/0/paymentsinfofinder?hostOrigin=aHR0cHM6Ly9wYXltZW50cy5nb29nbGUuY29tOjQ0Mw..&sri=-40) 및 [Google 광고 정책](https://support.google.com/adspolicy/answer/6008942?sjid=15557182366992806023-NC)(해당되는 경우 [EU 사용자 동의 정책](https://www.google.com/about/company/user-consent-policy/) 포함)을 수락하고 준수해야 합니다.<br><br>EEA, 영국 및 스위스 최종 사용자를 위한 Google Ads 서비스를 사용하기 위해 적절한 동의를 수집하고 있는지 확인하려면 법무팀에 Google의 새로운 EU 사용자 동의 정책에 대해 문의하세요. |
| Google Customer Match | [Google](https://support.google.com/google-ads/answer/6299717) |  Customer Match는 모든 광고주가 사용할 수 있는 것은 아닙니다.<br><br>**Customer Match를 사용하려면 계정에 다음이 필요합니다:**<br>• 양호한 정책 준수 이력<br>• 양호한 결제 이력<br>• Google Ads에서 최소 90일 이력<br>• 총 누적 지출 USD 50,000 이상. USD 이외의 통화로 관리되는 계정의 경우 해당 통화의 월평균 환율을 사용하여 지출 금액이 USD로 변환됩니다.<br><br>계정이 이러한 기준을 충족하지 않으면 현재 Customer Match를 사용할 수 없습니다.<br><br>계정의 Customer Match 사용 가능 여부에 대한 자세한 안내는 Google Ads 담당자에게 문의하세요. |
| Google 동의 신호 | [Google](https://support.google.com/google-ads/answer/14310715) |  Google의 Customer Match 서비스를 사용하여 EEA 최종 사용자에게 광고를 제공하려면 Google의 EU 사용자 동의 정책의 일부로 다음 커스텀 속성(부울)을 Braze에 전달해야 합니다. 자세한 내용은 [EEA, 영국 및 스위스 최종 사용자에 대한 동의 수집](#collecting-consent-for-eea-uk-and-switzerland-end-users)에서 확인할 수 있습니다: <br> - `$google_ad_user_data` <br> - `$google_ad_personalization` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="필수 조건" }

### 필수 SDK 버전 {#required-sdk-versions}

Braze SDK를 사용하여 동의 신호를 수집할 때 다음 최소 버전을 충족하는지 확인하세요:

{% sdk_min_versions swift:7.6.0 android:1.3.2 web:3.0.0 %}

### EEA, 영국 및 스위스 최종 사용자에 대한 동의 수집 {#collecting-consent-for-eea-uk-and-switzerland-end-users}

Google의 EU 사용자 동의 정책은 광고주가 EEA, 영국 및 스위스 최종 사용자에게 다음 사항을 공개하고 동의를 얻도록 요구합니다:

* 법적으로 요구되는 경우 쿠키 또는 기타 로컬 저장소의 사용
* 광고 개인화를 위한 개인 데이터의 수집, 공유 및 사용

이는 미국 최종 사용자 또는 EEA, 영국 또는 스위스 외부에 위치한 기타 최종 사용자에게는 영향을 미치지 않습니다. EEA, 영국 및 스위스 최종 사용자를 위한 Google Ads 서비스를 사용하기 위해 적절한 동의를 수집하고 있는지 확인하려면 법무팀에 Google의 새로운 EU 사용자 동의 정책에 대해 문의하세요.

2024년 3월 6일부터 시행되는 디지털 시장법(DMA) 요구 사항에 따라, 광고주는 Google과 데이터를 공유할 때 EEA, 영국 및 스위스 최종 사용자에 대한 동의를 전달해야 합니다. 이 변경의 일환으로, 다음 부울 커스텀 속성으로 Braze에서 두 가지 동의 신호를 모두 수집할 수 있습니다:

* `$google_ad_user_data`
* `$google_ad_personalization`

Braze는 이러한 커스텀 속성의 데이터를 [Google의 적절한 동의 필드](https://support.google.com/google-ads/answer/14310715#:~:text=These%20consent%20fields%20are%3A)에 동기화합니다.

#### 철회된 동의 관리 {#managing-revoked-consent}

EEA 최종 사용자가 오디언스 목록에 추가된 후 두 가지 동의(`$google_ad_user_data` 또는 `$google_ad_personalization`) 중 하나를 철회한 경우 오디언스 목록을 최신 상태로 유지하려면, Audience Sync 단계를 사용하여 기존 오디언스 목록에서 사용자를 제거하는 Canvas를 설정해야 합니다.

{% alert note %}
EEA 사용자가 이전에 두 신호 모두에 대해 동의를 제공한 경우, 해당 목록이 만료되거나 Google Audience Sync를 통해 동의 상태가 명시적으로 업데이트되거나 둘 다 발생할 때까지 해당 데이터는 Google의 Customer Match에 계속 사용됩니다.
{% endalert %}

#### 팁 {#tips}

* 값을 문자열 유형이 아닌 부울 유형으로 전송하세요.
* 속성 이름에 달러 기호($)를 접두사로 붙이세요. Braze는 속성 이름 시작 부분의 달러 기호를 사용하여 이것이 특수하고 예약된 키임을 나타냅니다.
* 속성 이름을 소문자로 입력하세요.
* 사용자를 명시적으로 미지정으로 설정할 수는 없지만, `null` 또는 `nil` 값이나 `true` 또는 `false`가 아닌 값을 전송하면 Braze는 이 사용자를 `UNSPECIFIED`로 Google에 전달합니다.
* 동의 속성을 지정하지 않고 추가되거나 업데이트된 새 사용자는 해당 동의 속성이 미지정으로 표시된 상태로 Google에 동기화됩니다.

필요한 동의 필드와 승인 상태 없이 EEA 사용자를 동기화하려고 하면 Google은 이를 거부하고 해당 사용자에게 광고를 제공하지 않습니다. 또한 명시적 동의 없이 EEA 사용자에게 광고가 제공되면 책임을 질 수 있으며 재정적 위험에 처할 수 있습니다. 이를 방지하려면 `true` Google 동의 속성을 가진 EEA, 영국 및 스위스 사용자만 포함하는 Segment 필터가 있는 Campaign을 전송하는 것이 좋습니다. Customer Match 업로드 파트너를 위한 EU 사용자 동의 정책에 대한 자세한 내용은 Google의 [FAQ](https://support.google.com/google-ads/answer/14310715)를 참조하세요.

### Canvas 설정 {#setting-up-your-canvas}

Braze에 동기화한 후 다음 동의 속성을 고객 프로필 및 세분화에 사용할 수 있습니다:

- `$google_ad_user_data`
- `$google_ad_personalization`

EEA, 영국 및 스위스 최종 사용자를 대상으로 Google Audience Sync를 사용하여 오디언스에 사용자를 추가하는 모든 Canvas에서는 두 개의 동의 속성이 `true`가 아닌 값일 때 이러한 사용자를 제외해야 합니다. 동의 값이 `true`로 설정되었을 때 이러한 사용자를 세분화하여 이 작업을 수행할 수 있습니다. 이렇게 하면 Google이 이러한 사용자를 오디언스에서 거부할 것이라는 것을 알고 있기 때문에 사용자에 대한 보다 정확한 분석이 동기화됩니다. Google Audience Sync를 사용하여 오디언스에서 사용자를 제거하는 경우에는 동의 속성이 필요하지 않습니다.

## 통합 {#integration}

### 1단계: Google 계정 연결 {#step-1-connect-google-account}

{% alert important %}
Google Ads를 Braze 계정에 연결하려면 ["Admin" 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin)이 필요합니다.
{% endalert %}

시작하려면 **파트너 통합** > **기술 파트너** > **Google Ads**로 이동하여 **Connect Google Ads**를 선택합니다. Google Ads 계정과 연결된 이메일을 선택하라는 모달이 표시되며, 그런 다음 Braze에 Google Ads 계정에 대한 액세스 권한을 부여합니다.

Google Ads 계정을 성공적으로 연결하면 Google Ads 파트너 페이지로 돌아갑니다. 그런 다음 Braze 워크스페이스에서 액세스할 광고 계정을 선택하라는 메시지가 표시됩니다.

![Braze에 성공적으로 Google Ads 계정을 연결하는 워크플로를 보여주는 GIF입니다.]({% image_buster /assets/img/google_sync/googlesync.gif %}){: style="max-width:85%;"}

#### iOS IDFA 또는 Google 광고 ID 내보내기 {#export-ios-idfa-or-google-advertising-ids}

오디언스 동기화에서 iOS IDFA 또는 Google 광고 ID를 내보내려는 경우, Google은 요청 내에 iOS 앱 ID와 Android 앱 ID를 요구합니다. Google Audience Sync에서 **Add Mobile Advertising IDs**를 선택하고 iOS 앱 ID와 Android 앱 ID(앱 패키지 이름)를 입력한 후 각각 저장합니다.

<br><br>
![연결된 광고 계정을 보여주는 업데이트된 Google Ads 기술 페이지로, 계정을 다시 동기화하고 모바일 광고 ID를 추가할 수 있습니다.]({% image_buster /assets/img/google_sync/google_sync5.png %}){: style="max-width:75%;"}
<br><br>

단일 워크스페이스에 여러 앱이 있는 경우, 사용자의 모바일 광고 ID는 여러 앱에서 동일하므로 설정에서 앱 ID 중 아무거나 입력할 수 있습니다. 이는 Android GAID와 iOS IDFA 모두 기기의 범용 광고 식별자이며 앱별로 다르지 않기 때문입니다. 특정 앱의 사용자에 대한 모바일 광고 ID를 동기화하려면 Segment 필터("Last Used Specific App" 또는 "Most Recent App Version")를 사용하여 이러한 사용자를 타겟팅할 수 있습니다.

### 2단계: Canvas에 Google Audience 단계 추가 {#step-2-add-a-google-audience-step-in-canvas}

Canvas에 구성요소를 추가한 다음 **Audience Sync**를 선택합니다.

![편집기에서 Canvas 구성요소를 선택하는 메뉴입니다.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![사용자 여정에 추가된 Audience Sync 단계입니다.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### 3단계: 동기화 설정 {#step-3-sync-setup}

1. **Custom Audience**를 선택하여 구성요소 편집기를 엽니다.
2. Audience Sync 파트너로 **Google**을 선택합니다.

![동기화를 시작할 파트너를 선택하는 옵션이 있는 Audience Sync 단계 설정입니다.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

{: start="3"}
3. 원하는 Google 광고 계정을 선택합니다.
4. **Choose a New or Existing Audience** 드롭다운에서 새 오디언스 또는 기존 오디언스의 이름을 입력합니다.

{% tabs %}
{% tab 새 오디언스 생성 %}

1. 새 커스텀 오디언스의 이름을 입력합니다.
2. **Add Users to Audience**를 선택합니다.
3. 오디언스에 전송할 퍼스트파티 사용자 필드 데이터를 선택합니다. 다음 중 하나를 선택할 수 있습니다:

- **고객 연락처 정보**: Braze에 존재하는 경우 사용자의 이메일 또는 전화번호, 또는 둘 다를 포함합니다. Google은 별도의 식별자 대신 단일 필드로 동기화하도록 요구합니다. 식별자 중 하나만 있는 경우에도 이 단일 필드를 사용할 수 있습니다.
- **모바일 광고주 ID**: iOS IDFA 또는 Android GAID를 선택합니다. Google의 Customer Match 요구 사항으로 인해 동일한 고객 목록에 두 가지 모바일 광고주 ID를 모두 포함할 수 없습니다.

{% alert note %}
**"Missing Mobile Ad IDs? Let's fix that." 배너에 대해:** iOS IDFA 또는 Android GAID를 일치시킬 필드로 사용하여 오디언스에 동기화할 때 이 메시지가 단계 편집기에 나타날 수 있습니다. 이는 **정보 제공용이며 오류가 아닙니다**. 일치시키려는 모바일 광고 ID 필드가 오디언스 데이터에 존재하는지 확인하라는 알림입니다(예: Canvas 경로의 사용자가 해당 식별자를 수집했는지). 데이터를 확인한 후에는 이를 무시할 수 있습니다.
{% endalert %}

{: start="4"}
4. 다음으로, 단계 편집기 하단의 **Create Audience** 버튼을 선택하여 오디언스를 저장합니다.

![커스텀 오디언스 Canvas 구성요소의 확장된 보기입니다. 여기에서 원하는 광고 계정이 선택되고, 새 오디언스가 생성되며, "고객 연락처 정보" 체크박스가 선택됩니다.]({% image_buster /assets/img/audience_sync/g_sync.png %})

오디언스가 성공적으로 생성되거나 이 과정에서 오류가 발생하면 단계 편집기 상단에 알림이 표시됩니다. 오디언스가 초안 모드로 생성되었으므로 Canvas 여정의 나중에 사용자 제거를 위해 이 오디언스를 참조할 수 있습니다.

![Canvas 구성요소에서 새 오디언스가 생성된 후 나타나는 알림입니다.]({% image_buster /assets/img/audience_sync/g_sync3.png %})

새 오디언스로 Canvas를 시작하면 Braze는 Canvas 시작 시 새 커스텀 오디언스를 생성하고, 이후 사용자가 Google Audience 단계에 진입할 때 거의 실시간으로 동기화합니다.

{% alert important %}
Google의 Customer Match 요구 사항에 따라 동일한 고객 목록에 고객 연락처 정보와 모바일 광고주 ID를 함께 포함할 수 없습니다. 그런 다음 Google Customer Match는 이 정보를 사용하여 Google 검색, Google 디스플레이, YouTube 및 Gmail 내에서 타겟팅 가능한 사용자를 결정합니다. Google Customer Match 요구 사항에 대한 자세한 내용은 해당 [설명서](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507)를 검토하세요.
{% endalert %}
{% endtab %}
{% tab 기존 오디언스와 동기화 %}

Braze는 기존 Google 고객 목록에서 사용자를 추가하거나 제거하여 이러한 오디언스를 최신 상태로 유지하는 기능도 제공합니다. 기존 오디언스와 동기화하려면:

1. 동기화할 기존 커스텀 오디언스를 선택합니다.
2. **Add to the audience** 또는 **Remove from the audience** 중 원하는 옵션을 선택합니다.
3. Braze는 사용자가 Google Audience 단계에 진입할 때 거의 실시간으로 사용자를 추가하거나 제거합니다.
4. Google Audience 단계를 구성한 후 **Done**을 선택합니다. Google Audience 단계에 새 오디언스에 대한 세부 정보가 포함됩니다.

![커스텀 오디언스 Canvas 구성요소의 확장된 보기입니다. 여기에서 원하는 광고 계정과 기존 오디언스가 선택되며, "Add user to Audience" 라디오 버튼도 선택됩니다.]({% image_buster /assets/img/audience_sync/g_sync2.png %})

{% endtab %}
{% endtabs %}

### 4단계: Canvas 시작 {#step-4-launch-canvas}

Canvas 내에서 나머지 사용자 여정을 완료한 다음 시작하세요! 새 오디언스를 생성하기로 선택한 경우, Braze는 Google 내에서 오디언스를 생성한 다음 사용자가 Canvas의 이 단계에 도달하면 추가합니다. 기존 오디언스에서 사용자를 추가하거나 제거하기로 선택한 경우, Braze는 사용자가 사용자 여정의 이 단계에 도달하면 추가하거나 제거합니다.

그런 다음 사용자는 Canvas의 다음 구성요소가 있으면 해당 구성요소로 진행하거나, 사용자 여정의 마지막 단계인 경우 Canvas를 종료합니다.

## 사용자 동기화 및 사용량 제한 고려 사항 {#user-syncing-and-rate-limit-considerations}

사용자가 Audience Sync 구성요소에 도달하면 Braze는 Google Ads API 사용량 제한을 준수하면서 거의 실시간으로 이러한 사용자를 동기화합니다. 실제로 이는 Braze가 5초마다 가능한 한 많은 사용자를 일괄 처리하여 Google에 전송하려고 시도한다는 것을 의미합니다.

고객이 Google Ads API 사용량 제한에 근접하면 Google은 재시도 권장 사항에 대한 피드백을 Braze에 제공합니다. Braze 고객이 사용량 제한에 도달하면 Braze Canvas는 최대 &#126;13시간 동안 동기화를 재시도합니다. 동기화가 불가능한 경우 이러한 사용자는 오류 발생 사용자 측정기준에 나열됩니다.

## 분석 이해 {#understanding-analytics}

다음 표에는 Audience Sync 단계의 분석을 더 잘 이해하는 데 도움이 되는 측정기준과 설명이 포함되어 있습니다.

| 측정기준 | 설명 |
| ------ | ----------- |
| *진입함* | Google에 동기화하기 위해 이 단계에 진입한 사용자 수입니다. |
| *다음 단계로 진행함* | 다음 구성요소가 있는 경우 다음 구성요소로 진행한 사용자 수입니다. 모든 사용자가 자동으로 진행됩니다. Canvas 브랜치의 마지막 단계인 경우 이 측정기준은 0입니다. |
| *동기화된 사용자* | Google에 성공적으로 동기화된 사용자 수입니다. |
| *동기화되지 않은 사용자* | 일치시킬 필드가 누락되었거나 동의 속성이 `false`로 설정되어 동기화되지 않은 사용자 수입니다. |
| *오류 발생 사용자* | &#126;13시간의 재시도 후 오류로 인해 Google에 동기화되지 않은 사용자 수입니다. Google Ads API 서비스 중단과 같은 특정 오류의 경우 Canvas는 최대 &#126;13시간 동안 동기화를 재시도합니다. 해당 시점에서도 동기화가 불가능한 경우 *동기화되지 않은 사용자*가 채워집니다. |
| *대기 중인 사용자* | 현재 Braze에서 Google에 동기화하기 위해 처리 중인 사용자 수입니다. |
| *Canvas 종료함* | Canvas를 종료한 사용자 수입니다. 이는 Canvas의 마지막 단계가 Google 단계인 경우 발생합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="분석 이해" }

## 자주 묻는 질문 {#frequently-asked-questions}

### Google Audience 단계 구성에서 일치시킬 여러 필드를 선택할 수 없는 이유는 무엇인가요? {#why-can-i-not-select-multiple-fields-to-match-in-my-google-audience-step-configuration}

Google Customer Match는 이러한 오디언스의 형식과 포함되는 고객 정보에 대해 엄격한 요구 사항을 가지고 있습니다. 구체적으로, 모바일 광고주 ID는 고객 연락처 정보(예: 이메일 및 전화번호)와 별도로 업로드해야 합니다. 자세한 내용은 [Google의 Customer Match 설명서](https://support.google.com/google-ads/answer/7659867?hl=en#undefined)를 참조하세요.

### Google에서 오디언스가 동기화되는 데 얼마나 걸리나요? {#how-long-will-it-take-for-my-audiences-to-sync-in-google}

오디언스가 Google에 동기화되는 데 6~12시간이 소요될 수 있습니다.

### 오디언스를 동기화했는데 Google에서 오디언스 크기가 0인 이유는 무엇인가요? {#ive-synced-an-audience-so-why-is-the-audience-size-in-google-zero}

개인정보 보호를 위해 목록에 최소 1,000명의 구성원이 있을 때까지 사용자 목록 크기는 0으로 표시됩니다. 그 이후에는 크기가 가장 유효한 두 자릿수로 반올림됩니다.

### Braze에서 동기화한 사용자 수보다 Google에서 일치된 오디언스 크기가 작은 이유는 무엇인가요? {#why-is-my-matched-audience-size-in-google-lower-than-the-number-of-users-synced-from-braze}

Braze가 특정 수의 사용자를 Google에 동기화하더라도 Google Ads에서 확인되는 실제 일치된 오디언스 크기는 상당히 작을 수 있습니다. 이는 Google이 제공된 사용자 데이터(예: 이메일 주소 또는 전화번호)를 플랫폼의 실제 Google 계정과 일치시켜야 하기 때문입니다.

Braze 고객 프로필에 유효한 일치 필드가 포함되어 있더라도, 사용자는 일치하는 정보가 있는 Google 계정을 보유한 경우에만 Google 커스텀 오디언스에 표시됩니다.

일치율을 개선하려면:
- [데이터 형식이 올바른지](https://support.google.com/google-ads/answer/7659867) 확인하세요.
- 가능한 경우 여러 식별자를 제공하세요(예: 이메일과 전화번호 모두).
- Google이 사용자를 처리하고 일치시키는 데 48~72시간이 소요될 수 있으며, 경우에 따라 며칠이 걸릴 수도 있습니다.

최종 일치된 오디언스 크기는 전적으로 Google의 일치 프로세스에 따라 결정됩니다. 데이터가 Google 플랫폼으로 전달된 후에는 Braze에서 Google의 일치 과정을 확인할 수 없습니다.

### 오디언스를 Google에 동기화했는데 광고가 게재되지 않습니다. {#ive-synced-an-audience-into-google-but-my-ads-are-not-serving}

광고 게재를 시작하려면 오디언스에 최소 5,000명의 사용자가 포함되어 있는지 확인하세요.

### "모바일 앱 ID 삭제됨" 오류를 어떻게 해결하나요? {#how-do-i-resolve-the-mobile-app-ids-deleted-error}

Google에 오디언스를 동기화하는 경우, 동기화의 일부로 모바일 식별자를 동기화하도록 선택했지만 Google 파트너 페이지에서 모바일 앱 ID를 삭제한 경우 이 오류가 발생합니다. 이 문제를 해결하려면 iOS 및 Android에 적합한 모바일 앱 ID를 Google 파트너 페이지에 추가했는지 확인하세요.

### 대시보드에서 여전히 연결됨으로 표시되는데 Google Ads 잘못된 자격 증명 이메일을 받은 이유는 무엇인가요? {#why-did-i-get-a-google-ads-invalid-credentials-email-when-the-dashboard-still-shows-connected}

Braze는 Google의 API가 인증 오류를 반환할 때 이 이메일을 자동으로 전송합니다. 이는 대시보드에서 **Google Ads**가 여전히 연결된 것으로 표시되고 오디언스가 동기화되는 것처럼 보이는 경우에도 발생할 수 있습니다. 예를 들어, 연결된 Google 계정에 Google이 요청한 특정 작업에 대한 권한이 없거나 해당 계정에 대해 Google Ads 서비스 약관을 아직 수락해야 하는 경우입니다.

일부 인증 오류는 자체적으로 해결됩니다. Canvas **Audience Sync** 분석(예: *동기화된 사용자* 및 *오류 발생 사용자*)을 확인하여 사용자가 여전히 동기화되고 있는지 확인하세요. 문제가 계속되면 **파트너 통합** > **기술 파트너** > **Google Ads**로 이동하여 **Google Audience Sync**를 찾고 **Change Account**를 사용하여 필요한 액세스 권한과 완료된 설정이 있는 Google Ads 계정으로 다시 연결하세요.