## Pré-requisitos {#prerequisites}

Antes de começar este tutorial, verifique se o seu SDK Braze atende aos requisitos mínimos de versão:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Exibindo banners para o SDK Android {#displaying-banners-for-the-android-sdk}

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

### 1. Ativar depuração (opcional) {#1-enable-debugging-optional} {#1-enable-debugging-optional}

Para facilitar a solução de problemas durante o desenvolvimento, considere ativar a depuração.

!!step
lines-MainApplication.kt=21-28

### 2. Assinar atualizações de Banner {#2-subscribe-to-banner-updates} {#2-subscribe-to-banner-updates}

Use `subscribeToBannersUpdates()` para registrar um handler que é executado sempre que um Banner é atualizado.

!!step
lines-MainActivity.kt=10-14

### 3. Atualizar suas colocações {#3-refresh-your-placements} {#3-refresh-your-placements}

Após inicializar o SDK da Braze, chame `requestBannersRefresh(["PLACEMENT_ID"])` para buscar o conteúdo de Banner mais recente para essa colocação.

Essa chamada é mesclada ao cache de Banners existente. Apenas os IDs de colocação que você solicitar são adicionados, atualizados ou removidos. Banners em cache para outras colocações permanecem no cache e expiram no tempo de vencimento original. Se o servidor não retornar nenhum Banner para uma colocação solicitada, essa colocação é removida do cache.

!!step
lines-banners.xml=15-19

### 4. Definir `BannerView` no seu `banners.xml` {#4-define-bannerview-in-your-bannersxml} {#4-define-bannerview-in-your-bannersxml}

No `banners.xml`, declare um elemento `<com.braze.ui.banners.BannerView>` com `app:placementId="PLACEMENT_ID"`. A Braze usará esse elemento para inserir seu Banner na sua interface.

Após uma atualização, o SDK atualiza uma `BannerView` somente quando o conteúdo dessa colocação é alterado. Banners exibidos sem alterações permanecem como estão.

{% endscrolly %}