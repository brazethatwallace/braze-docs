## 필수 조건 {#prerequisites}

이 튜토리얼을 시작하기 전에 Braze SDK가 최소 버전 요구 사항을 충족하는지 확인하십시오:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Android SDK용 배너 표시 {#displaying-banners-for-the-android-sdk}

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Displaying Banners Android" %}

{% scrolly %}

```kotlin file=MainApplication.kt
import android.app.Application
import android.util.Log
import com.braze.Braze
import com.braze.configuration.BrazeConfig
import com.braze.support.BrazeLogger

public class MainApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Turn on verbose Braze logging
        BrazeLogger.logLevel = Log.VERBOSE

        // Configure Braze with your SDK key and endpoint
        val config = BrazeConfig.Builder()
            .setApiKey("YOUR-API-KEY")
            .setCustomEndpoint("YOUR-ENDPOINT")
            .build()
        Braze.configure(this, config)

        // Subscribe to Banner updates
        Braze.getInstance(this)
            .subscribeToBannersUpdates { update ->
                for (banner in update.banners) {
                    Log.d("brazeBanners", "Received banner for placement: ${banner.placementId}")
                    // Add any custom banner logic you'd like
                }
            }
    }
}
```

```kotlin file=MainActivity.kt
import android.os.Bundle
import androidx.activity.ComponentActivity

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // Inflate the XML layout
        setContentView(R.layout.banners)

        // Refresh placements
        Braze.getInstance(this)
            .requestBannersRefresh(
                listOf("top-1")
            )
    }
}
```

```xml file=banners.xml
<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="16dp">

    <LinearLayout
        android:orientation="vertical"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:gravity="center_horizontal">

        <!-- Banner placement -->
        <com.braze.ui.banners.BannerView
            android:id="@+id/banner_view_1"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            app:placementId="top-1" />

        <!-- ...the rest of your activity layout -->

    </LinearLayout>
</ScrollView>
```

!!step
lines-MainApplication.kt=12

### 1. 디버깅 활성화(선택 사항) {#1-enable-debugging-optional} {#1-enable-debugging-optional}

개발 중 문제 해결을 쉽게 하기 위해 디버깅을 활성화하는 것을 고려하세요.

!!step
lines-MainApplication.kt=21-28

### 2. 배너 업데이트 구독 {#2-subscribe-to-banner-updates} {#2-subscribe-to-banner-updates}

`subscribeToBannersUpdates()`를 사용하여 배너가 업데이트될 때마다 실행되는 핸들러를 등록합니다.

!!step
lines-MainActivity.kt=10-14

### 3. 배치 새로고침 {#3-refresh-your-placements} {#3-refresh-your-placements}

Braze SDK를 초기화한 후 `requestBannersRefresh(["PLACEMENT_ID"])`를 호출하여 해당 배치에 대한 최신 배너 콘텐츠를 가져옵니다.

이 호출은 기존 배너 캐시에 병합됩니다. 요청한 배치 ID만 추가, 업데이트 또는 제거됩니다. 다른 배치에 대한 캐시된 배너는 캐시에 유지되며 원래 만료 시간에 만료됩니다. 서버가 요청된 배치에 대해 배너를 반환하지 않으면 해당 배치는 캐시에서 제거됩니다.

!!step
lines-banners.xml=15-19

### 4. `banners.xml`에서 `BannerView` 정의 {#4-define-bannerview-in-your-bannersxml} {#4-define-bannerview-in-your-bannersxml}

`banners.xml`에서 `app:placementId="PLACEMENT_ID"`를 포함하는 `<com.braze.ui.banners.BannerView>` 요소를 선언합니다. Braze는 이 요소를 사용하여 UI에 배너를 삽입합니다.

새로고침 후 SDK는 해당 배치의 콘텐츠가 변경된 경우에만 `BannerView`를 업데이트합니다. 변경되지 않은 표시된 배너는 그대로 유지됩니다.

{% endscrolly %}