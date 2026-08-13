---
nav_title: RevenueCat
article_title: RevenueCat
description: "RevenueCat과 Braze의 통합을 통해 플랫폼 전반에서 고객의 구매 및 구독 라이프사이클 이벤트를 자동으로 동기화할 수 있습니다. 이를 통해 고객의 구독 라이프사이클 단계에 반응하는 캠페인을 구축할 수 있습니다. 예를 들어, 무료 체험 기간 중 옵트아웃한 고객에게 참여를 유도하거나 결제 문제가 있는 고객에게 알림을 보낼 수 있습니다."
alias: /partners/revenuecat/
page_type: partner
search_tag: Partner

---

# RevenueCat

> [RevenueCat](https://www.revenuecat.com/)은 iOS, Android, 웹 전반에서 구독 상태에 대한 단일 정보 소스입니다. 새로운 앱을 구축하든 이미 수백만 명의 구독자를 보유하고 있든, RevenueCat을 사용하여 크로스 플랫폼 인앱 구매를 구축하고, 제품과 구독자를 관리하며, 데이터를 분석할 수 있습니다. 서버 코드가 필요하지 않습니다.

_이 통합은 RevenueCat에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

RevenueCat과 Braze의 통합을 통해 플랫폼 전반에서 고객의 구매 및 구독 라이프사이클 이벤트를 자동으로 동기화할 수 있습니다. 이를 통해 고객의 구독 라이프사이클 단계에 반응하는 캠페인을 구축할 수 있습니다. 예를 들어, 무료 체험 기간 중 옵트아웃한 고객에게 참여를 유도하거나 결제 문제가 있는 고객에게 알림을 보낼 수 있습니다.

## 전제 조건 {#prerequisites}

최소한 RevenueCat 대시보드에서 통합을 활성화하여 RevenueCat을 Braze에 연결해야 합니다. Braze SDK를 사용하는 경우, RevenueCat과 Braze SDK를 함께 사용하여 두 시스템에서 동일한 고객 식별자가 사용되도록 하여 통합을 강화할 수 있습니다.

| 요구 사항 | 설명 |
|---|---|
| RevenueCat 계정 및 앱 | 이 파트너십을 활용하려면 [RevenueCat 계정](https://app.revenuecat.com/login)이 필요합니다. 또한 구성된 RevenueCat 앱이 있어야 합니다. |
| RevenueCat SDK | 필수 Braze SDK 외에도 RevenueCat에 사용자 별칭을 제공하기 위해 [RevenueCat SDK](https://docs.revenuecat.com/docs/configuring-sdk)를 설치하는 것을 권장합니다. |
| Braze 인스턴스 | Braze 인스턴스는 Braze 온보딩 매니저에게 문의하거나 [API 개요 페이지]({{site.baseurl}}/api/basics#endpoints)에서 확인할 수 있습니다.<br><br>RevenueCat은 올바른 Braze REST 엔드포인트로 서버 측 전송을 하기 위해 Braze 인스턴스가 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze 테스트 REST API 키(선택 사항) | 테스트 및 프로덕션 구매를 별도의 Braze 인스턴스로 전송하려는 경우 테스트 API 키를 사용할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="전제 조건" }

## 사용 사례 {#use-cases}

- 고객이 무료 체험을 시작할 때 프리미엄 기능을 강조하는 온보딩 캠페인을 트리거합니다.
- "결제 문제" 이벤트가 수신되면 결제 정보를 업데이트하라는 알림을 보냅니다.
- 고객이 무료 체험을 취소한 후 피드백 설문조사를 보냅니다.

## 통합 {#integration}

### 1단계: Braze 사용자 ID 설정 {#step-1-set-braze-user-identity}

Braze SDK에서 Braze 사용자 ID를 RevenueCat 앱 사용자 ID와 일치하도록 설정하여 Braze와 RevenueCat에서 전송된 이벤트가 동일한 사용자에게 동기화되도록 할 수 있습니다.

RevenueCat과 동일한 앱 사용자 ID로 Braze SDK를 구성하거나 Braze SDK `.changeUser()` 메서드를 사용합니다.

{% tabs local %}
{% tab swift %}
```swift
// Configure Purchases SDK
Purchases.configure(withAPIKey: "public_sdk_key", appUserID: "my_app_user_id")

// Change user in Braze SDK
Appboy.sharedInstance()?.changeUser("my_app_user_id")

// Optional User Alias Object attributes
Purchases.shared.setAttributes(["$brazeAliasName" : "name",
                             "$brazeAliasLabel" : "label"])
```
{% endtab %}
{% tab objective-c %}
```objc
// Configure Purchases SDK
[RCPurchases configureWithAPIKey:@"public_sdk_key" appUserID:@"my_app_user_id"];

// Change user in Braze SDK
[[Appboy sharedInstance] changeUser:@"my_app_user_id"];

// Optional User Alias Object attributes
[[RCPurchases sharedPurchases] setAttributes:@{
    @"$brazeAliasName": @"name",
    @"$brazeAliasLabel": @"label"
}];
```
{% endtab %}
{% tab java %}
```java
// Configure Purchases SDK
Purchases.configure(this, "public_sdk_key", "my_app_user_id");

// Change user in Braze SDK
Braze.getInstance(context).changeUser(my_app_user_id);

// Optional User Alias Object attributes
Map<String, String> attributes = new HashMap<String, String>();
attributes.put("$brazeAliasName", "name");
attributes.put("$brazeAliasLabel", "label");

Purchases.getSharedInstance().setAttributes(attributes);
```
{% endtab %}
{% endtabs %}

#### Braze에 사용자 별칭 오브젝트 전송(선택 사항) {#send-user-alias-object-to-braze-optional}

RevenueCat 앱 사용자 ID와 다른 대체 고유 사용자 식별자를 전송하려면 다음 데이터를 RevenueCat 구독자 속성으로 사용하여 사용자를 업데이트합니다.

| 키 | 설명 |
|---|---|
| `$brazeAliasName` | [사용자 별칭 오브젝트]({{site.baseurl}}/api/objects_filters/user_alias_object)의 Braze `alias_name` |
| `$brazeAliasLabel` | [사용자 별칭 오브젝트]({{site.baseurl}}/api/objects_filters/user_alias_object)의 Braze `alias_label` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze에 사용자 별칭 오브젝트 전송(선택 사항)" }

이벤트 데이터와 함께 [사용자 별칭 오브젝트]({{site.baseurl}}/api/objects_filters/user_alias_object)를 전송하려면 두 속성이 모두 필요합니다. 이러한 속성은 다른 [RevenueCat 구독자 속성](https://docs.revenuecat.com/docs/subscriber-attributes)과 마찬가지로 수동으로 설정할 수 있습니다. 예제 코드 스니펫은 1단계에 나와 있습니다.

### 2단계: RevenueCat 이벤트를 Braze로 전송 {#step-2-send-revenuecat-events-to-braze}

RevenueCat 구매 SDK와 Braze SDK가 동일한 사용자 ID를 사용하도록 설정한 후, RevenueCat 대시보드에서 통합을 활성화하고 이벤트 이름을 구성할 수 있습니다.

1. RevenueCat 대시보드에서 프로젝트로 이동하여 탐색 메뉴에서 **Integrations** 카드를 찾습니다. **+ New**를 선택합니다.
2. 다음으로, 사용 가능한 통합에서 **Braze**를 선택하고 Braze 인스턴스와 Braze REST API 키를 추가합니다.
3. RevenueCat이 전송할 이벤트 이름을 입력하거나 기본 이벤트 이름을 선택합니다. 사용 가능한 이벤트에 대한 자세한 내용은 [3단계](#configure-event-names)에서 확인할 수 있습니다.
4. RevenueCat에서 수익금(앱 스토어 수수료 차감 후)을 보고할지, 매출(총 판매액)을 보고할지 선택합니다.

![Braze 인스턴스, API 키 식별자, 샌드박스 식별자에 대한 필드가 있는 RevenueCat의 Braze 설정.]({% image_buster /assets/img/revenuecat/braze_settings_in_revenuecat.png %})

### 3단계: 이벤트 이름 구성 {#configure-event-names}

RevenueCat이 전송할 이벤트 이름을 입력하거나 **Use Default Event Names**를 선택하여 기본 이벤트 이름에서 선택합니다. RevenueCat이 전송을 지원하는 이벤트는 다음 표에 설명되어 있습니다.

| 이벤트 | 설명 |
|---|---|
| 최초 구매 | 무료 체험이 포함되지 않은 자동 갱신 구독 제품의 첫 번째 구매입니다. |
| 체험 시작 | 자동 갱신 구독 제품 무료 체험의 시작입니다. |
| 체험 전환 | 자동 갱신 구독 제품이 무료 체험에서 일반 유료 기간으로 전환될 때입니다. |
| 체험 취소 | 사용자가 무료 체험 기간 중 자동 갱신 구독 제품의 갱신을 해제할 때입니다. |
| 갱신 | 자동 갱신 구독 제품이 갱신되거나, 사용자가 구독 만료 후 자동 갱신 구독 제품을 재구매할 때입니다. |
| 취소 | 사용자가 일반 유료 기간 중 자동 갱신 구독 제품의 갱신을 해제할 때입니다. |
| 비구독 구매 | 자동 갱신 구독이 아닌 제품의 구매입니다. |
| 만료 | 구독이 만료될 때입니다. |
| 결제 문제 | 사용자에게 요금을 청구하는 데 문제가 발생했을 때입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="3단계: 이벤트 이름 구성" }

매출이 포함된 이벤트의 경우, RevenueCat은 체험 전환 및 갱신과 같은 이벤트와 함께 이 금액을 Braze에 자동으로 기록합니다.

## 이 통합 사용하기 {#using-this-integration}

RevenueCat에서 Braze 설정을 구성한 후, 별도의 조치 없이 RevenueCat에서 Braze로 이벤트가 자동으로 전송되기 시작합니다.

## 커스터마이제이션 {#customization}

### 테스트용 샌드박스 API 키 추가 {#add-a-sandbox-api-key-for-testing}

RevenueCat에 Braze REST API 키를 하나만 제공하면 프로덕션 이벤트만 전송됩니다. 샌드박스 테스트 이벤트도 전송하려면 [다른 Braze REST API 키를 생성]({{site.baseurl}}/api/basics#creating-rest-api-keys)하고 RevenueCat의 Braze 설정에 추가합니다.