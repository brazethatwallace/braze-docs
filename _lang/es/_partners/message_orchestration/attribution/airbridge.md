---
nav_title: Airbridge
article_title: Airbridge
alias: /partners/airbridge/
description: "Este artículo de referencia describe la asociación entre Braze y Airbridge, que ofrece atribución basada en las personas y medición incremental para medir la verdadera eficacia del marketing a través de dispositivos, identidades y plataformas."
page_type: partner
search_tag: Partner

---

# Airbridge

> [Airbridge](https://www.airbridge.io/) es una plataforma unificada de medición móvil para descubrir fuentes de crecimiento a través de la atribución móvil, la medición incremental y el modelado de la mezcla de marketing.

_Esta integración está mantenida por Airbridge._

## Sobre la integración {#about-the-integration}

La integración de Braze y Airbridge te permite pasar todos los datos de atribución de instalaciones no orgánicas de Airbridge a Braze para crear campañas de marketing personalizadas.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta Airbridge | Se necesita una cuenta Airbridge para beneficiarse de esta asociación. |
| Aplicación para iOS o Android | Esta integración es compatible con aplicaciones iOS y Android. Dependiendo de tu plataforma, es posible que se requieran fragmentos de código en tu aplicación. |
| SDK de Airbridge | Además del SDK de Braze necesario, debes instalar el SDK de Airbridge [para Android](https://help.airbridge.io/en/developers/android-sdk) o [iOS](https://help.airbridge.io/en/developers/ios-sdk). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integración {#integration}

### Paso 1: Mapear ID de dispositivo {#step-1-map-device-id}

La integración de servidor a servidor puede activarse incluyendo los siguientes fragmentos de código en tus aplicaciones.

#### Android

Si tienes una aplicación Android, tendrás que pasar un ID de dispositivo Braze único a Airbridge.

{% tabs %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
// MainApplciation.java
@Override
public void onCreate() {
    super.onCreate();
    // Initialize Airbridge SDK
    AirbridgeConfig config = new AirbridgeConfig.Builder("APP_NAME", "APP_TOKEN")
        // Make Airbridge SDK explicitly start tracking
        .setAutoStartTrackingEnabled(false)
        .build();
    Airbridge.init(this, config);

    // Set device alias into Airbridge SDK
    Airbridge.getCurrentUser().setAlias("braze_device_id", Braze.getInstance(this).getDeviceId());
    // Explicitly start tracking
    Airbridge.startTracking();
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
// MainApplication.kt
override fun onCreate() {
    super.onCreate()
    // Initialize Airbridge SDK
    val config = AirbridgeConfig.Builder("YOUR_APP_NAME", "YOUR_APP_SDK_TOKEN")
        // Make Airbridge SDK explicitly start tracking
        .setAutoStartTrackingEnabled(false)
        .build()
    Airbridge.init(this, config)

    // Set device alias into Airbridge SDK
    Airbridge.getCurrentUser().setAlias("braze_device_id", Braze.getInstance(this).deviceId)
    // Explicitly start tracking
    Airbridge.startTracking()
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### iOS

Si tienes una aplicación iOS, puedes optar por recopilar IDFV estableciendo el campo useUUIDAsDeviceId en false. Si no se establece, es probable que la atribución de iOS no se asigne con precisión de Airbridge a Braze. Para más información, consulta Recopilación de IDFV.

{% tabs %}
{% tab iOS %}
{% subtabs %}
{% subtab Swift %}

```swift
// AppDelegate.swift
func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]?
) {
    AirBridge.setAutoStartTrackingEnabled(false)
    AirBridge.getInstance("YOUR_APP_TOKEN", appName:"YOUR_APP_NAME", withLaunchOptions:launchOptions)

    AirBridge.state()?.addUserAlias(withKey:"braze_device_id", value:Appboy.sharedInstance()?.getDeviceId())
    AirBridge.startTracking()
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// AppDelegate.m
-           (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  AirBridge.autoStartTrackingEnabled = NO;
  [AirBridge getInstance:@"YOUR_APP_TOKEN" appName:@"YOUR_APP_NAME" withLaunchOptions:launchOptions];

    [AirBridge.state addUserAliasWithKey:@"braze_device_id" value:Appboy.sharedInstance.getDeviceId];
    [AirBridge startTracking];
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### React Native

{% tabs %}
{% tab TypeScript %}

```typescript
Braze.getInstallTrackingId(function (error, brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
    Airbirdge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Cordova

{% tabs %}
{% tab TypeScript %}

```typescript
AppboyPlugin.getDeviceId(function (brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
  Airbridge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Flutter

{% tabs %}
{% tab TypeScript %}

```typescript
BrazePlugin.getInstallTrackingId().then((brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
  Airbridge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Unity

{% tabs %}
{% tab C# %}

```c#
string BrazeID = AppboyBinding.GetInstallTrackingId();
AirbridgeUnity.SetDeviceAlias("braze_device_id", BrazeID);
AirbridgeUnity.StartTracking()
```

{% endtab %}
{% endtabs %}

### Paso 2: Obtener la clave de importación de datos de Braze {#step-2-get-the-braze-data-import-key}

En Braze, ve a **Partner Integrations** > **Technology Partners** y selecciona **Airbridge**.

Aquí encontrarás el punto de conexión REST y generarás tu clave de importación de datos de Braze. Una vez generada la clave, puedes crear una nueva o invalidar una existente. La clave de importación de datos y el punto de conexión REST se utilizan en el siguiente paso al configurar un postback en el dashboard de Airbridge.

![]({% image_buster /assets/img/airbridge/airbridge_integration_step_1.png %})

### Paso 3: Configura Braze en el dashboard de Airbridge {#step-3-configure-braze-in-airbridges-dashboard}

1. En Airbridge, ve a **Integrations > Third-party Integrations** en la barra lateral izquierda y selecciona **Braze**.
2. Proporciona la clave de importación de datos y el punto de conexión REST que encontraste en el dashboard de Braze.
3. Selecciona el tipo de evento (Install Event o Install & Deeplink Open Event) y guárdalo.

{% alert note %}
Los datos de atribución de las campañas que dieron lugar a eventos de apertura de enlaces profundos se actualizan a nivel de dispositivo. Por ejemplo, si dos usuarios utilizan un mismo dispositivo y uno de ellos realiza un evento de apertura de enlace profundo, los datos de atribución de este evento también se reflejan en los datos del otro usuario.
{% endalert %}

Para obtener instrucciones más detalladas, visita [Airbridge](https://help.airbridge.io/en/guides/braze).

### Paso 4: Confirmar la integración {#step-4-confirm-the-integration}

Después de que Braze reciba los datos de atribución de Airbridge, el indicador de estado de la conexión en la página de socios tecnológicos de Airbridge en Braze cambia de "Not Connected" a "Connected" e incluye una marca de tiempo de la última solicitud realizada con éxito.

Este estado solo cambia cuando Braze recibe datos sobre una instalación atribuida. Braze ignora las instalaciones orgánicas (las excluye del postback de Airbridge) y no las cuenta a la hora de determinar si la conexión se ha realizado correctamente.

## Campos de datos disponibles {#available-data-fields}

Airbridge puede enviar cuatro tipos de datos de atribución a Braze que se enumeran en el siguiente cuadro de campos de datos. Estos datos pueden visualizarse en el dashboard de Airbridge y se utilizan para la atribución de instalaciones de usuarios y el filtrado.

Suponiendo que configures tu integración como se sugiere, Braze asignará los datos de instalación a los filtros de segmento.

| Campo de datos Airbridge | Filtro de segmento de Braze | Descripción |
| -------------------- | ---------------------| ---- |
| `Channel` | Fuente de atribución de instalación | El canal al que se atribuyen las instalaciones o las aperturas de enlaces profundos |
| `Campaign` | Campaign de atribución de instalación | La Campaign a la que se atribuyen las instalaciones o las aperturas de enlaces profundos |
| `Ad Group` | Grupo de anuncios de atribución de instalación | El grupo de anuncios al que se atribuyen las instalaciones o las aperturas de enlaces profundos |
| `Ad Creative` | Anuncio de atribución de instalación | La creatividad del anuncio al que se atribuyen las instalaciones o las aperturas de enlaces profundos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Available data fields" }

Tu base de usuarios puede segmentarse por datos de atribución en el dashboard de Braze utilizando los filtros de atribución de instalación.

![]({% image_buster /assets/img/airbridge/airbridge_integration_step_2.png %})

## Datos de atribución de Meta Business {#meta-business-attribution-data}

Los datos de atribución de las campañas de Meta Business no están disponibles a través de nuestros socios. Esta fuente de medios no permite a sus socios compartir datos de atribución con terceros y, por lo tanto, nuestros socios no pueden enviar esos datos a Braze.

## URL de seguimiento de clics de Airbridge en Braze (opcional) {#airbridge-click-tracking-urls-in-braze-optional}

El uso de enlaces de seguimiento de clics en tus campañas de Braze muestra qué campañas impulsan la instalación de aplicaciones y la reactivación de la interacción. Utiliza los resultados para medir el rendimiento del marketing y decidir dónde invertir los recursos para obtener un mayor ROI.

Para empezar a utilizar los enlaces de seguimiento de clics de Airbridge, visita [Airbridge](https://help.airbridge.io/en/guides/creating-a-new-tracking-link). Una vez finalizada la configuración, puedes insertar directamente los enlaces de seguimiento de clics de Airbridge en tus campañas de Braze. A continuación, Airbridge utilizará sus [metodologías de atribución probabilística](https://help.airbridge.io/en/guides/identity-matching) para atribuir al usuario que ha hecho clic en el enlace. Recomendamos añadir un identificador de dispositivo a los enlaces de seguimiento de Airbridge para mejorar la precisión de las atribuciones de tus campañas de Braze. Esto atribuirá de forma determinista al usuario que ha hecho clic en el enlace.

{% tabs %}
{% tab Android %}
Para Android, Braze permite a los clientes la adhesión voluntaria a la [recopilación de ID de publicidad de Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). El GAID también se recoge de forma nativa a través de la integración del SDK de Airbridge. Puedes incluir el GAID en tus enlaces de seguimiento de clics de Airbridge utilizando la siguiente lógica de Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto Braze como Airbridge recopilan automáticamente el IDFV de forma nativa a través de nuestras integraciones de SDK. Puede utilizarse como identificador del dispositivo. Puedes incluir el IDFV en tus enlaces de seguimiento de clics de Airbridge utilizando la siguiente lógica de Liquid:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**Esta recomendación es meramente opcional**<br>
Si actualmente no utilizas ningún identificador de dispositivo —como el IDFV o el GAID— en tus enlaces de seguimiento de clics, o no tienes previsto hacerlo en el futuro, Airbridge podrá seguir atribuyendo estos clics a través de su modelado probabilístico.
{% endalert %}