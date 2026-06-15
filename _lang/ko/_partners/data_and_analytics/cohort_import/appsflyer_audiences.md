---
nav_title: AppsFlyer Audiences
article_title: AppsFlyer Audiences
alias: /partners/appsflyer_audiences/
description: "이 참조 문서에서는 Braze와 AppsFlyer Audiences 간의 파트너십에 대해 설명합니다. AppsFlyer Audiences는 AppsFlyer 플랫폼의 기능으로, 오디언스 세그먼트를 효율적으로 구축하고 파트너 네트워크에 연결할 수 있습니다."
page_type: partner
search_tag: Partner

---

# AppsFlyer Audiences

> 이 문서에서는 [AppsFlyer Audiences](https://www.appsflyer.com/product/audiences/) 통합을 사용하여 AppsFlyer에서 Braze로 사용자 코호트를 가져오는 방법을 설명합니다. AppsFlyer 통합 및 모바일 기여도 등 기타 기능에 대한 자세한 내용은 [AppsFlyer 문서]({{site.baseurl}}/partners/message_orchestration/deeplinking/appsflyer/appsflyer/)를 참조하세요.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| AppsFlyer 계정 | 이 파트너십을 활용하려면 AppsFlyer 계정이 필요합니다. |
| iOS 또는 Android 앱 | 이 통합은 iOS 및 Android 앱을 지원합니다. 플랫폼에 따라 애플리케이션에 코드 스니펫이 필요할 수 있습니다. 이러한 요구 사항에 대한 세부 정보는 통합 프로세스의 1단계에서 확인할 수 있습니다. |
| AppsFlyer SDK | 필수 Braze SDK 외에도 [AppsFlyer SDK](https://support.appsflyer.com/hc/en-us/articles/207032126-SDK-integration-overview)를 설치해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 데이터 가져오기 통합 {#data-import-integration}

### 1단계: AppsFlyer SDK 구성 {#step-1-configure-the-appsflyer-sdk}

이 통합을 사용하려면 AppsFlyer SDK의 `setPartnerData()` 함수를 사용하여 사용자의 Braze 외부 ID를 AppsFlyer에 전달해야 합니다.

#### Android
```java
Map<String, Object> brazeData = new HashMap<>();
partnerData.put("external_user_id", "some-braze-external-id-value");
AppsFlyerLib.getInstance().setPartnerData("braze_int", brazeData);
```

#### iOS
```objc
NSDictionary *brazeInfo = @{
     @"external_user_id":@"some-braze-external-id-value"
};
[[AppsFlyerLib shared]  setPartnerDataWithPartnerId:@"braze_int" partnerInfo:brazeInfo];
```

### 2단계: Braze 데이터 가져오기 키 가져오기 {#step-2-get-the-braze-data-import-key}

Braze에서 **파트너 통합** > **기술 파트너**로 이동하여 **AppsFlyer**를 선택합니다.

여기에서 REST 엔드포인트를 찾아 Braze 데이터 가져오기 키를 생성할 수 있습니다. 키가 생성되면 새 키를 만들거나 기존 키를 무효화할 수 있습니다. 데이터 가져오기 키와 REST 엔드포인트는 다음 단계에서 AppsFlyer 대시보드에서 포스트백을 설정할 때 사용됩니다.<br><br>![AppsFlyer 기술 페이지의 "코호트 가져오기를 사용한 데이터 가져오기" 상자. 이 상자에 데이터 가져오기 키와 REST 엔드포인트가 표시됩니다.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_data_import_key.png %}){: style="max-width:90%;"}

### 3단계: AppsFlyer Audiences에서 Braze 연결 구성 {#step-3-configure-a-braze-connection-in-appsflyer-audiences}

1. [AppsFlyer Audiences](https://support.appsflyer.com/hc/en-us/articles/115002689186-Audiences-guide#managing-connections)에서 **Connections** 탭으로 이동하여 **Add partner connection**을 클릭합니다.
2. 파트너로 Braze를 선택하고 연결에 이름을 지정합니다.
3. 데이터 가져오기 키와 Braze REST 엔드포인트를 입력합니다.
4. 연결을 저장하면 새 오디언스 또는 기존 오디언스에 연결할 수 있습니다.

![AppsFlyer 오디언스 플랫폼 파트너 연결 구성 페이지. 이미지의 하단에서는 Braze 외부 ID 상자가 선택되어 있음을 보여줍니다.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_braze_connection.png %}){: style="max-width:80%;"}

### 4단계: Braze에서 AppsFlyer Audiences 코호트 사용 {#step-4-using-appsflyer-audiences-cohorts-in-braze}

AppsFlyer 오디언스가 Braze에 업로드되면 Braze에서 세그먼트를 정의할 때 **AppsFlyer Cohorts** 필터를 선택하여 필터로 사용할 수 있습니다.

![사용자 속성 필터 "AppsFlyer Cohorts" 선택됨.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_cohorts_as_filter.png %})

{% alert important %}
Braze에 이미 존재하는 사용자만 코호트에 추가되거나 제거됩니다. 코호트 가져오기는 Braze에 새 사용자를 생성하지 않습니다.
{% endalert %}

## 사용자 매칭 {#user-matching}

식별된 사용자는 `external_id` 또는 `alias`로 매칭할 수 있습니다. 익명 사용자는 `device_id`로 매칭할 수 있습니다. 원래 익명 사용자로 생성된 식별된 사용자는 `device_id`로 식별할 수 없으며, `external_id` 또는 `alias`로 식별해야 합니다.