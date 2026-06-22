---
nav_title: "푸시 토큰 수명 주기"
article_title: "푸시 토큰 수명 주기"
page_order: 1
page_type: reference
description: "이 참조 문서에서는 푸시 등록의 의미와 Braze에서 푸시 메시지를 보내고 푸시 토큰 및 푸시 등록을 처리하는 방법에 대해 설명합니다."
channel:
 - push

---

# 푸시 토큰 수명 주기 {#push-token-lifecycle}

> 이 문서에서는 사용자에게 푸시 토큰이 할당되는 과정과 Braze가 사용자에게 푸시 메시지를 보내는 방법을 다룹니다.

## 푸시 토큰 정보 {#push-tokens}

앱이 기기에 푸시 권한을 요청하면, 기기의 푸시 서비스 공급자가 해당 앱에 대한 푸시 토큰을 생성합니다. 각 앱에는 고유한 익명 푸시 토큰이 부여되며, 이를 통해 푸시 알림을 보낼 때 기기와 현재 앱 인스턴스를 식별합니다.

푸시 토큰은 영구적인 정적 식별자가 아닙니다&#8212;업데이트될 수 있으며 [만료](#push-token-expire)될 수도 있습니다.

{% alert tip %}
플랫폼별 세부 정보는 [푸시 토큰 등록](#push-token-registration)을 참조하세요.
{% endalert %}

### 포그라운드 푸시 vs. 백그라운드 푸시 {#foreground-vs-background}

푸시 토큰은 포그라운드 및 백그라운드 푸시 알림을 모두 보내는 데 사용됩니다.

| 유형 | 옵트인 필요 여부 | 설명 |
|------------------|------------------|--------------------------------------------------------------------------------------------------------------|
| 포그라운드 푸시 | 예 | 앱이 포그라운드에 있는 동안 사용자에게 알림이 표시됩니다. |
| 백그라운드 푸시 | 아니요 | 알림이 표시되지 않고 백그라운드에서 조용히 전달됩니다. 제거 추적과 같은 기능에 자주 사용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="포그라운드 푸시 vs. 백그라운드 푸시" }

사용자가 앱의 푸시 알림에 옵트인하면 "푸시 등록됨"으로 간주되며, Braze에서 `Foreground Push Enabled for App` 세분화 필터를 사용하여 타겟팅할 수 있습니다.

{% alert note %}
이것은 `Foreground Push Enabled` 세분화 필터와 다릅니다. 이 필터는 특정 앱이 아닌 앱 중 하나 이상에 옵트인한 사용자를 식별하는 데 사용됩니다. 자세한 내용은 [세분화 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#foreground-push-enabled)를 참조하세요.
{% endalert %}

### 하나의 기기에 여러 사용자 {#multiple-users-on-a-device}

푸시 토큰은 기기와 앱 모두에 고유하므로, 여러 사용자가 동일한 기기를 사용하는 경우 푸시 토큰으로 특정 사용자를 타겟팅할 수 없습니다.

예를 들어, Charlie와 Kim이라는 두 명의 사용자가 있다고 가정합니다. Charlie가 자신의 휴대폰에서 앱의 푸시 알림을 활성화한 상태에서 Kim이 Charlie의 휴대폰을 사용하여 Charlie의 프로필에서 로그아웃하고 자신의 프로필로 로그인하면, 푸시 토큰이 Kim의 프로필로 재할당됩니다. 그러면 Kim이 로그아웃하고 Charlie가 다시 로그인할 때까지 해당 기기에서 푸시 토큰은 Kim의 프로필에 할당된 상태로 유지됩니다.

앱이나 웹사이트는 기기당 하나의 푸시 구독만 가질 수 있습니다. 따라서 사용자가 기기나 웹사이트에서 로그아웃하고 새 사용자가 로그인하면, 푸시 토큰이 새 사용자에게 재할당됩니다. 이는 사용자 프로필의 **Engagement** 탭에 있는 **Contact Settings** 섹션에 반영됩니다.

![사용자 프로필의 Engagement 탭에 있는 푸시 토큰 체인지로그로, 푸시 토큰이 다른 사용자에게 이동된 시점과 해당 토큰이 무엇인지 표시합니다.]({% image_buster /assets/img/push_token_changelog.png %})

푸시 공급자(APNs/FCM)가 하나의 기기에서 여러 사용자를 구분할 방법이 없기 때문에, 마지막으로 로그인한 사용자에게 푸시 토큰을 전달하여 기기에서 푸시를 타겟팅할 사용자를 결정합니다.

{% alert tip %}
**Contact Settings** > **Push Changelog**에서 오류 메시지가 표시되면, [일반적인 푸시 오류 메시지]({{site.baseurl}}/user_guide/channels/push/push_error_codes/)에서 설명과 다음 단계를 확인하세요.
{% endalert %}

## 푸시 토큰 등록 {#push-token-registration}

각 기기 플랫폼은 푸시 토큰 등록을 다르게 처리합니다. 플랫폼별 세부 정보는 다음을 참조하세요:

{% tabs local %}
{% tab 웹 %}
네이티브 브라우저 권한 대화 상자를 통해 사용자에게 명시적인 옵트인을 요청해야 합니다. 사용자가 옵트인한 후 토큰을 받게 됩니다. iOS 및 Android와 달리 앱이 언제든지 권한 프롬프트를 표시할 수 있는 것과 다르게, 일부 최신 브라우저는 "사용자 제스처"(마우스 클릭 또는 키 입력)에 의해 트리거된 경우에만 프롬프트를 표시합니다. 사이트가 페이지 로드 시 푸시 알림 권한을 요청하려고 하면, 브라우저에 의해 무시되거나 차단될 가능성이 높습니다.
{% endtab %}

{% tab Android %}
앱이 설치되면 앱에 대한 푸시 토큰이 자동으로 생성됩니다&#8212;그러나 사용자가 명시적으로 옵트인할 때까지 [백그라운드 푸시 알림](#foreground-vs-background)에만 사용할 수 있습니다. 또한 Android 버전에 따라 등록이 다르게 처리됩니다:

| 버전 | 세부 정보 |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Android 13** | 사용자가 푸시 권한을 요청하고 승인해야 합니다. 앱에서 수동으로 권한을 요청하거나, [알림 채널](https://developer.android.com/reference/android/app/NotificationChannel)이 생성된 후 자동으로 프롬프트가 표시됩니다. |
| **Android 12 이하** | 모든 사용자는 첫 번째 세션 후 `Subscribed`로 간주됩니다. Braze는 이 시점에서 자동으로 푸시 토큰을 요청하여, 유효한 토큰과 기본 구독 상태 `Subscribed`로 사용자의 푸시를 활성화합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="푸시 토큰 등록" }
{% endtab %}

{% tab iOS %}
iOS는 앱이 설치될 때 자동으로 푸시 토큰을 생성하지 않습니다. 또한 iOS 버전에 따라 등록이 다르게 처리됩니다:

| 버전 | 임시 승인 여부 | 세부 정보 |
|------------------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **iOS 12** | 예 | 사용자가 푸시 알림에 옵트인하면 표준 승인이 부여되어 [포그라운드 푸시 알림](#foreground-vs-background)을 보낼 수 있습니다. 그러나 [임시 승인]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options/#provisional-push)을 요청하여 알림 센터로 직접 조용한 [백그라운드 푸시 알림](#foreground-vs-background)을 보낼 수도 있습니다. |
| **iOS 11 이하** | 아니요 | 모든 사용자는 푸시 알림을 받으려면 명시적으로 옵트인해야 합니다. 권한이 부여된 후에만 푸시 토큰이 생성됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="푸시 토큰 등록" }
{% endtab %}
{% endtabs %}

### 사용자의 푸시 구독 상태 확인 {#checking-users-push-subscription-state}

![Engagement 탭에서 푸시 구독 상태와 푸시 등록 세부 정보를 보여주는 Jane Doe의 사용자 프로필.]({% image_buster /assets/img/push_implementation_guide/checking-users-push-subscription-state.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Braze에서 사용자의 푸시 구독 상태를 확인하는 방법은 두 가지가 있습니다:

- **사용자 프로필**: Braze 대시보드의 [사용자 검색]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/) 페이지에서 개별 사용자 프로필에 접근할 수 있습니다. 사용자의 프로필을 찾은 후(이메일 주소, 전화번호 또는 외부 사용자 ID를 통해), **Engagement** 탭을 선택하여 사용자의 구독 상태를 확인하고 수동으로 조정할 수 있습니다.
- **REST API 내보내기**: [Segment별 사용자]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) 또는 [식별자별 사용자]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) 엔드포인트를 사용하여 개별 사용자 프로필을 JSON 형식으로 내보낼 수 있습니다. Braze는 기기별 푸시 활성화 정보가 포함된 푸시 토큰 오브젝트를 반환합니다.

### 푸시 등록 상태 확인 {#checking-push-registration-status}

사용자 프로필의 **Engagement** 탭에서 **Push Registered For** 뒤에 앱 이름이 표시됩니다. 해당 기기에 대한 앱 정보가 없으면 두 개의 대시(**&#45;&#45;**)가 표시됩니다. 사용자에게 속한 모든 기기에 대한 항목이 있습니다.

기기 항목의 앱 이름 앞에 `Foreground:`가 붙어 있으면, 해당 앱은 해당 기기에서 포그라운드 푸시 알림(사용자에게 표시됨)과 백그라운드 푸시 알림(사용자에게 표시되지 않음)을 모두 수신할 수 있도록 승인된 것입니다.

![예시 푸시 토큰이 있는 푸시 체인지로그.]({% image_buster /assets/img/push_changelog.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:10px;"}

반면, 기기 항목의 앱 이름 앞에 `Background:`가 붙어 있으면, 해당 앱은 [백그라운드 푸시]({{site.baseurl}}/user_guide/channels/push/types/#background-push-notifications)만 수신할 수 있도록 승인되었으며 해당 기기에서 사용자에게 표시되는 알림을 표시할 수 없습니다. 이는 일반적으로 사용자가 해당 기기에서 앱의 알림을 비활성화했음을 나타냅니다.

푸시 토큰이 동일한 기기의 다른 사용자에게 이동되면, 첫 번째 사용자는 더 이상 푸시 등록 상태가 아닙니다.

## 푸시 토큰 관리 {#push-token-management}

다음 차트에서 푸시 토큰 변경 또는 사용자 프로필에서 제거로 이어지는 동작을 확인하세요.

| 동작 | 설명 |
| ------ | ----------- |
| `changeUser()` 메서드 호출 | Braze `changeUser()` 메서드는 SDK가 사용자 행동 데이터를 할당하는 사용자 ID를 전환합니다. 이 메서드는 일반적으로 사용자가 애플리케이션에 로그인할 때 호출됩니다. 특정 기기에서 다른 또는 새로운 사용자 ID로 `changeUser()`가 호출되면, 해당 기기의 푸시 토큰이 해당 사용자 ID에 대응하는 적절한 Braze 프로필로 이동됩니다. |
| 푸시 오류 발생 | 토큰 제거로 이어지는 일반적인 푸시 오류에는 `MismatchSenderId`, `InvalidRegistration` 및 기타 유형의 푸시 반송이 포함됩니다. <br><br>일반적인 [푸시 오류]({{site.baseurl}}/user_guide/channels/push/push_error_codes/)의 전체 목록을 확인하세요. |
| 사용자가 앱 제거 | 사용자가 기기에서 애플리케이션을 제거하면, Braze는 프로필에서 해당 사용자의 푸시 토큰을 제거합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="푸시 토큰 관리" }

### 더 큰 규모에서는 어떻게 보이나요? {#what-does-this-look-like-on-a-broader-scale}

사용자가 새 애플리케이션을 열고 푸시 프롬프트에서 푸시 접근을 허용하면, Braze SDK에서 푸시 공급자로 호출이 이루어집니다. 해당 호출이 이루어지면, 푸시 공급자는 모든 것이 올바르게 설정되었는지 확인합니다. 설정이 올바르면, 푸시 토큰이 기기로 전달됩니다. 토큰이 도착하면, SDK가 이를 Braze에 전달합니다. Braze가 푸시 공급자로부터 토큰을 받으면, 새 사용자 프로필을 업데이트하거나 생성합니다. 이 사용자들은 이제 등록된 것으로 간주됩니다.

Campaign(캠페인)을 시작하려면, Braze에서 Campaign을 생성하여 푸시 공급자에게 보낼 푸시 페이로드를 생성합니다. 그런 다음 공급자가 사용자의 기기에 푸시 페이로드를 전달하고, SDK가 메시징 상태를 Braze에 전달합니다.

![Braze, 고객, Apple 푸시 알림 서비스 또는 Firebase Cloud Messaging 간의 앞서 설명한 푸시 프로세스를 매핑한 흐름도.]({% image_buster /assets/img/push_process.png %})

| 등록 단계 | 메시징 단계 |
| ------------------ | --------------- |
| 1. 고객(기기)이 푸시 공급자에 등록<br>2. 공급자가 푸시 토큰을 생성하고 전달<br>3. Braze에 토큰 플러시 |1. Braze가 공급자에게 푸시 페이로드 전송<br>2. 공급자가 기기에 푸시 페이로드 전달<br>3. SDK가 메시징 통계를 Braze에 전달 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="더 큰 규모에서는 어떻게 보이나요?" }

## 자주 묻는 질문 {#frequently-asked-questions}

### 옵트인한 사용자가 앱을 삭제한 후 다시 다운로드하면 어떻게 되나요? {#what-happens-when-an-opted-in-user-deletes-and-then-redownloads-my-app}

사용자가 푸시에 옵트인하고, 일부 푸시 메시지를 받은 후, 나중에 앱을 삭제한다고 가정합니다. 이렇게 하면 기기 수준에서 푸시 동의가 제거됩니다. 이후 제거 후 첫 번째 반송된 푸시는 자동으로 해당 사용자를 향후 푸시 메시징에서 옵트아웃 처리합니다. 이후 사용자가 앱을 다시 설치하지만 실행하지 않으면, 앱에 대한 푸시 토큰이 다시 부여되지 않았기 때문에 Braze는 해당 사용자에게 푸시를 보낼 수 없습니다.

또한, 사용자가 포그라운드 푸시를 다시 활성화하면, 푸시 메시징을 받기 시작하려면 세션 시작이 필요하여 사용자 프로필에서 이 정보를 업데이트해야 합니다.

### 푸시 토큰은 언제 만료되나요? {#push-token-expire}

안타깝게도, APNs와 FCM은 이를 명확하게 정의하지 않습니다. 푸시 토큰은 앱이 업데이트되거나, 사용자가 데이터를 새 기기로 전송하거나, 운영체제를 다시 설치할 때 만료될 수 있습니다. 대부분의 경우, 푸시 공급자가 특정 푸시 토큰을 만료시키는 이유에 대한 인사이트가 없습니다.

이러한 모호성을 고려하여, SDK 푸시 통합은 항상 세션 시작 시 토큰을 등록하고 플러시하여 최신 토큰을 확보합니다.