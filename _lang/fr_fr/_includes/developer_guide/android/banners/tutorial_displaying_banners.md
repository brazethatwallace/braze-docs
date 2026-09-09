## Conditions préalables {#prerequisites}

Avant de commencer ce tutoriel, veuillez vérifier que votre SDK Braze répond aux exigences minimales en matière de version :

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Affichage de bannières pour le SDK Android {#displaying-banners-for-the-android-sdk}

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

### 1. Activer le débogage (facultatif) {#1-enable-debugging-optional} {#1-enable-debugging-optional}

Pour faciliter la résolution des problèmes pendant le développement, vous pouvez activer le débogage.

!!step
lines-MainApplication.kt=21-28

### 2. S'abonner aux mises à jour des bannières {#2-subscribe-to-banner-updates} {#2-subscribe-to-banner-updates}

Utilisez `subscribeToBannersUpdates()` pour enregistrer un gestionnaire qui s'exécute chaque fois qu'une bannière est mise à jour.

!!step
lines-MainActivity.kt=10-14

### 3. Actualiser vos placements {#3-refresh-your-placements} {#3-refresh-your-placements}

Après avoir initialisé le SDK Braze, appelez `requestBannersRefresh(["PLACEMENT_ID"])` pour récupérer le contenu de bannière le plus récent pour ce placement.

Cet appel fusionne les données dans le cache de bannières existant. Seuls les ID de placement que vous demandez sont ajoutés, mis à jour ou supprimés. Les bannières en cache pour d'autres placements restent dans le cache et expirent à leur date d'expiration d'origine. Si le serveur ne renvoie aucune bannière pour un placement demandé, ce placement est supprimé du cache.

!!step
lines-banners.xml=15-19

### 4. Définir `BannerView` dans votre `banners.xml` {#4-define-bannerview-in-your-bannersxml} {#4-define-bannerview-in-your-bannersxml}

Dans `banners.xml`, déclarez un élément `<com.braze.ui.banners.BannerView>` avec `app:placementId="PLACEMENT_ID"`. Braze utilisera cet élément pour insérer votre bannière dans votre interface.

Après une actualisation, le SDK met à jour un `BannerView` uniquement lorsque le contenu de ce placement change. Les bannières affichées qui n'ont pas changé restent telles quelles.

{% endscrolly %}