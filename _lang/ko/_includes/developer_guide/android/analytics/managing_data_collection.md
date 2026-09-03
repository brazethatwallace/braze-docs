## Google Play 개인정보 보호 설문지 {#privacy-questionnaire}

2022년 4월부터 Android 개발자는 개인정보 보호 및 보안 관행을 공개하기 위해 Google Play의 [데이터 안전 양식](https://support.google.com/googleplay/android-developer/answer/10787469)을 작성해야 합니다. 이 가이드는 Braze가 앱 데이터를 처리하는 방법에 대한 정보와 함께 이 새 양식을 작성하는 방법에 대한 지침을 제공합니다.

앱 개발자는 Braze에 전송하는 데이터를 직접 관리할 수 있습니다. Braze가 수신한 데이터는 사용자의 지침에 따라 처리됩니다. Google은 이를 [서비스 제공업체](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en#zippy=%2Cwhat-kinds-of-activities-can-service-providers-perform)로 분류합니다.

{% alert important %}
이 문서에서는 Google 안전 섹션 설문조사와 관련하여 Braze SDK가 처리하는 데이터에 대한 정보를 제공합니다. 이 문서는 법률 자문을 제공하지 않으므로 Google에 정보를 제출하기 전에 법무팀과 상담하는 것이 좋습니다.
{% endalert %}

### 질문 {#questions}

| 질문 | Braze SDK에 대한 답변 |
|---|---|
| 앱에서 필수 사용자 데이터 유형을 수집하거나 공유하나요? | 예. Braze Android SDK는 앱 개발자가 구성한 대로 데이터를 수집합니다. |
| 앱에서 수집한 모든 사용자 데이터는 전송 중에 암호화되나요? | 예. |
| 사용자가 자신의 데이터 삭제를 요청할 수 있는 방법을 제공하나요? | 예. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Questions" }

사용자의 데이터 및 삭제 요청 처리에 대한 자세한 내용은 [Braze 데이터 보존 정보]({{site.baseurl}}/api/data_retention)를 참조하세요.

### 데이터 수집 {#data-collection}

Braze에서 수집하는 데이터는 특정 통합 및 수집하기로 선택한 사용자 데이터에 따라 결정됩니다. Braze가 기본적으로 수집하는 데이터와 특정 속성을 비활성화하는 방법에 대해 자세히 알아보려면 [SDK 데이터 수집 옵션]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection#minimum-integration)을 참조하세요.

<table aria-label="데이터 수집" id="datatypes">
    <thead>
        <tr>
            <th width="25%">카테고리</th>
            <th width="25%">데이터 유형</th>
            <th width="50%">Braze 사용</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">위치</td>
            <td>대략적인 위치</td>
            <td rowspan="15">기본적으로 수집되지 않습니다.</td>
        </tr>
        <tr>
            <td>정확한 위치</td>
        </tr>
        <tr>
            <td rowspan="9">개인 정보</td>
            <td>이름</td>
        </tr>
        <tr>
            <td>이메일 주소</td>
        </tr>
        <tr>
            <td>사용자 ID</td>
        </tr>
        <tr>
            <td>주소</td>
        </tr>
        <tr>
            <td>전화번호</td>
        </tr>
        <tr>
            <td>인종 및 민족</td>
        </tr>
        <tr>
            <td>정치적 또는 종교적 신념</td>
        </tr>
        <tr>
            <td>성적 취향</td>
        </tr>
        <tr>
            <td>기타 정보</td>
        </tr>
        <tr>
            <td rowspan="4">재무 정보</td>
            <td>사용자 결제 정보</td>
        </tr>
        <tr>
            <td>구매 내역</td>
        </tr>
        <tr>
            <td>신용 점수</td>
        </tr>
        <tr>
            <td>기타 재무 정보</td>
        </tr>
        <tr>
            <td rowspan="2">건강 및 피트니스</td>
            <td>건강 정보</td>
            <td rowspan="2">기본적으로 수집되지 않습니다.</td>
        </tr>
        <tr>
            <td>피트니스 정보</td>
        </tr>
        <tr>
            <td rowspan="3">메시지</td>
            <td>이메일</td>
            <td rowspan="2">기본적으로 수집되지 않습니다.</td>
        </tr>
        <tr>
            <td>SMS 또는 MMS</td>
        </tr>
        <tr>
            <td>기타 인앱 메시지</td>
            <td>Braze를 통해 인앱 메시지 또는 푸시 알림을 보내는 경우, 사용자가 이러한 메시지를 열거나 읽은 시점에 대한 정보를 수집합니다.</td>
        </tr>
        <tr>
            <td rowspan="2">사진 및 동영상</td>
            <td>사진</td>
            <td rowspan="8">수집되지 않습니다.</td>
        </tr>
        <tr>
            <td>동영상</td>
        </tr>
        <tr>
            <td rowspan="3">오디오 파일</td>
            <td>음성 또는 사운드 녹음</td>
        </tr>
        <tr>
            <td>음악 파일</td>
        </tr>
        <tr>
            <td>기타 오디오 파일</td>
        </tr>
        <tr>
            <td>파일 및 문서</td>
            <td>파일 및 문서</td>
        </tr>
        <tr>
            <td>캘린더</td>
            <td>캘린더 이벤트</td>
        </tr>
        <tr>
            <td>연락처</td>
            <td>연락처</td>
        </tr>
        <tr>
            <td rowspan="5">앱 활동</td>
            <td>앱 상호 작용</td>
            <td>Braze는 기본적으로 세션 활동 데이터를 수집합니다. 다른 모든 상호 작용과 활동은 앱의 커스텀 통합에 의해 결정됩니다.</td>
        </tr>
        <tr>
            <td>앱 내 검색 기록</td>
            <td>수집되지 않습니다.</td>
        </tr>
        <tr>
            <td>설치된 앱</td>
            <td>수집되지 않습니다.</td>
        </tr>
        <tr>
            <td>기타 사용자 제작 콘텐츠</td>
            <td rowspan="2">기본적으로 수집되지 않습니다.</td>
        </tr>
        <tr>
            <td>기타 동작</td>
        </tr>
        <tr>
            <td>웹 브라우징</td>
            <td>웹 브라우징 기록</td>
            <td>수집되지 않습니다.</td>
        </tr>
        <tr>
            <td rowspan="3">앱 정보 및 성능</td>
            <td>크래시 로그</td>
            <td>Braze는 SDK 내에서 발생하는 오류에 대한 크래시 로그를 수집합니다. 여기에는 사용자의 휴대폰 모델 및 OS 수준과 Braze 전용 사용자 ID가 포함됩니다.</td>
        </tr>
        <tr>
            <td>진단</td>
            <td>수집되지 않습니다.</td>
        </tr>
        <tr>
            <td>기타 앱 성능 데이터</td>
            <td>수집되지 않습니다.</td>
        </tr>
        <tr>
            <td>기기 또는 기타 ID</td>
            <td>기기 또는 기타 ID</td>
            <td>Braze는 사용자의 기기를 구분하기 위해 기기 ID를 생성하고, 메시지가 의도한 기기로 올바르게 전송되었는지 확인합니다.</td>
        </tr>
    </tbody>
</table>

Braze가 수집하는 기타 기기 데이터 중 Google Play 데이터 안전 가이드라인의 범위를 벗어날 수 있는 데이터에 대해 자세히 알아보려면 [Android 스토리지 개요]({{site.baseurl}}/developer_guide/storage/?tab=android) 및 [SDK 데이터 수집 옵션]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection#minimum-integration)을 참조하세요.

## 데이터 추적 비활성화하기 {#disabling-data-tracking}

Android SDK에서 데이터 추적 활동을 비활성화하려면 [`disableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html) 메서드를 사용하세요. 이렇게 하면 모든 네트워크 연결이 취소되며, Braze SDK가 더 이상 Braze 서버로 데이터를 전송하지 않습니다.

## 이전에 저장된 데이터 삭제 {#wiping-previously-stored-data}

[`wipeData()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/wipe-data.html) 메서드를 사용하여 기기에 저장된 모든 클라이언트 측 데이터를 완전히 삭제할 수 있습니다.

## 데이터 추적 재개 {#resuming-data-tracking}

데이터 수집을 재개하려면 [`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html) 메서드를 사용할 수 있습니다. 이전에 삭제된 데이터는 복원되지 않는다는 점에 유의하세요.

## 로그아웃 및 푸시 등록 해제 {#logout-and-unregister-push}

Braze SDK는 사용자가 푸시 알림 등록을 해제하거나 로그아웃할 때 기기를 타겟팅 대상에서 제외하는 메서드를 제공합니다. 이 메서드는 Braze 서버와 SDK에서 현재 사용자의 푸시 등록 데이터를 제거하므로, Braze는 해당 사용자에게 더 이상 푸시 알림 Campaign을 전송하지 않습니다.

### 로그아웃 {#logout}

사용자가 애플리케이션에서 로그아웃할 때 SDK의 `logout` 메서드를 호출하여 현재 사용자로부터 기기의 푸시 등록을 제거하고 SDK에서 자동으로 정리 작업을 수행합니다. `logout` 메서드는 다음 작업을 수행합니다:

- Braze 서버에서 현재 사용자의 기기 푸시 토큰 등록을 해제합니다.
- 등록 해제 호출이 성공하면 SDK가 로컬에 저장된 SDK 데이터를 삭제하고 SDK를 비활성화합니다.
- 실패 시 오류와 `isRetriable` 플래그를 발생시켜 통합 담당자가 조치를 취할 수 있도록 합니다.

다음 콜백 예제는 `logout`의 성공 및 오류 처리를 보여줍니다. 콜백 기반 로그아웃 플로우에 사용하고, 로깅 부분을 재시도 또는 재인증 로직으로 교체하세요.

```kotlin
// Completion callback
Braze.getInstance(context).logout { result ->
  result
    .onSuccess {
      Log.d(TAG, "Logout successful")
    }
    .onFailure { error ->
      val pushError = error as? BrazePushUnregistrationException
      Log.e(TAG, "Logout failed: ${error.message}, isRetriable: ${pushError?.isRetriable}")
    }
}
```

다음 코루틴 예제는 일시 중단(suspending) `logout` API를 보여줍니다. 코루틴 기반 플로우에서 사용하고, 앱에 맞게 성공 및 실패 분기를 커스터마이즈하세요.

```kotlin
lifecycleScope.launch {
  runCatching { Braze.getInstance(context).logout() }
    .onSuccess {
      Log.d(TAG, "Logout successful")
    }
    .onFailure { error ->
      val pushError = error as? BrazePushUnregistrationException
      Log.e(TAG, "Logout failed: ${error.message}, isRetriable: ${pushError?.isRetriable}")
    }
}
```

#### `logout` 후 추적 및 푸시 다시 활성화하기 {#re-enable-tracking-and-push-after-logout}

`logout`이 성공한 후 [`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html)로 SDK를 다시 활성화한 다음, [Android 푸시 설정]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)을 따라 운영 체제(OS) 또는 푸시 제공자에 알림을 다시 등록하세요.

#### 즉시 등록 해제 호출 방지 {#avoid-immediate-unregister-calls}

OS 또는 푸시 제공자에 푸시 알림을 등록한 직후에 `logout` 또는 `unregisterPush`를 호출하지 마세요. 비동기 서버 처리로 인해 드물게 푸시 토큰이 Braze 사용자에게 다시 추가될 수 있습니다.

### 푸시 등록 해제 {#unregister-push}

추가적인 자동 정리 없이 기기로의 푸시 전송을 중지하려면 `unregisterPush` 메서드를 사용하세요. 이 메서드는 Braze 서버에서 현재 사용자의 기기 푸시 토큰을 제거하고, 로컬에 저장된 토큰을 삭제합니다.

다음 콜백 예제는 `unregisterPush` 결과를 처리하는 방법을 보여줍니다. 콜백 기반 플로우에서 사용하고, 로깅 부분을 자체 재시도 처리 로직으로 교체하세요.

```kotlin
// Completion callback
Braze.getInstance(context).unregisterPush { result ->
  result
    .onSuccess {
      Log.d(TAG, "Push unregistered successfully")
    }
    .onFailure { error ->
      val pushError = error as? BrazePushUnregistrationException
      Log.e(
        TAG,
        "Push unregistration failed: ${error.message}, isRetriable: ${pushError?.isRetriable}"
      )
    }
}
```

다음 코루틴 예제는 일시 중단(suspending) `unregisterPush` API를 보여줍니다. 코루틴 기반 플로우에서 사용하고, 앱에 맞게 성공 및 실패 분기를 커스터마이즈하세요.

```kotlin
lifecycleScope.launch {
  runCatching { Braze.getInstance(context).unregisterPush() }
    .onSuccess {
      Log.d(TAG, "Push unregistered successfully")
    }
    .onFailure { error ->
      val pushError = error as? BrazePushUnregistrationException
      Log.e(
        TAG,
        "Push unregistration failed: ${error.message}, isRetriable: ${pushError?.isRetriable}"
      )
    }
}
```

#### `unregisterPush` 후 푸시 다시 등록하기 {#re-register-push-after-unregisterpush}

`unregisterPush`를 호출한 후 Braze 푸시 알림을 다시 전송하려면, [Android 푸시 설정]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)을 따라 OS 또는 푸시 제공자에 알림을 다시 등록하세요.

#### 즉시 등록 해제 호출 방지

OS 또는 푸시 제공자에 푸시 알림을 등록한 직후에 `logout` 또는 `unregisterPush`를 호출하지 마세요. 비동기 서버 처리로 인해 드물게 푸시 토큰이 Braze 사용자에게 다시 추가될 수 있습니다.