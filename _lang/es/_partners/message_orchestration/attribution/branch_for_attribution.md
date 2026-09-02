---
nav_title: Branch para atribución
article_title: Branch para atribución
alias: /partners/branch_for_attribution/
description: "Este artículo de referencia describe la asociación entre Braze y Branch, una plataforma de vinculación móvil que te ayuda a adquirir, interactuar y medir en todos los dispositivos, canales y plataformas."
page_type: partner
search_tag: Partner
---

# Branch para atribución {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch](https://docs.branch.io/pages/integrations/braze/), una plataforma de vinculación móvil, te ayuda a adquirir, interactuar y medir en todos los dispositivos, canales y plataformas, proporcionando una visión holística de todos los puntos de intervención del usuario.

_Esta integración está mantenida por Branch._

## Sobre la integración {#about-the-integration}

La integración de Braze y Branch te ayudará a comprender exactamente cuándo y dónde fueron adquiridos los usuarios, así como a personalizar sus recorridos mediante una sólida atribución y [vinculación en profundidad]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking).

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta de Branch | Se necesita una cuenta de Branch para beneficiarse de esta asociación. |
| Aplicación para iOS o Android | Esta integración es compatible con aplicaciones iOS y Android. Dependiendo de tu plataforma, es posible que se requieran fragmentos de código en tu aplicación. Encontrarás más detalles sobre estos requisitos en el paso 1 del proceso de integración. |
| SDK or kit de desarrollo de software de Branch | Además del SDK or kit de desarrollo de software de Braze necesario, debes instalar el [SDK or kit de desarrollo de software de Branch](https://help.branch.io/developers-hub/docs/native-sdks-overview). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Mapear ID de dispositivos {#step-1-map-device-ids}

#### Android

Si tienes una aplicación Android, tendrás que pasar un ID de dispositivo Braze único a Branch. Este ID puede configurarse en el método `setRequestMetadataKey()` del SDK or kit de desarrollo de software de Branch. El siguiente fragmento de código debe incluirse antes de llamar a `initSession`. También debes inicializar el SDK or kit de desarrollo de software de Braze antes de configurar los metadatos de solicitud en el SDK or kit de desarrollo de software de Branch.

{% tabs local %}
{% tab Java %}
```java
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId);
```
{% endtab %}
{% tab Kotlin %}
```kotlin
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId)
```
{% endtab %}
{% endtabs %}

#### iOS

{% alert important %}
Antes de febrero de 2023, nuestra integración de atribución de Branch utilizaba el identificador de proveedor (IDFV) como identificador principal para cotejar los datos de atribución de iOS. No es necesario que los clientes de Braze que utilicen Objective-C obtengan el `device_id` de Braze y lo envíen a Branch durante la instalación, ya que no se produce ninguna interrupción del servicio.
{% endalert%}

Para quienes utilicen Swift SDK or kit de desarrollo de software v5.7.0+, si deseas seguir utilizando IDFV como identificador mutuo, debes asegurarte de que el campo `useUUIDAsDeviceId` esté configurado en `false` para que no haya interrupciones en la integración.

Si se establece en `true`, debes implementar el mapeado de ID de dispositivo iOS para Swift con el fin de pasar el `device_id` de Braze a Branch durante la instalación de la aplicación para que Braze pueda hacer coincidir correctamente las atribuciones de iOS.

{% tabs local %}
{% tab Objective-C %}
```objc
[braze deviceIdOnQueue:dispatch_get_main_queue() completion:^(NSString * _Nonnull deviceId) {
  [[Branch getInstance] setRequestMetadataKey:@"$braze_install_id" value:deviceId];
  // Branch init
}];
```
{% endtab %}
{% tab Swift %}

```swift
braze.deviceId { deviceId in
  Branch.getInstance.setRequestMetadata("$braze_install_id", deviceId)
  // Branch init
}
```

{% endtab %}
{% endtabs %}

### Paso 2: Obtener la clave de importación de datos de Braze {#step-2-get-the-braze-data-import-key}

En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **Branch**.

Aquí encontrarás el endpoint REST y generarás tu clave de importación de datos de Braze. Una vez generada la clave, puedes crear una nueva o invalidar una existente. La clave de importación de datos y el endpoint REST se utilizan en el siguiente paso al configurar un postback en el panel de Branch.<br><br>![Esta imagen muestra el cuadro "Importación de datos para la atribución de instalación" que se encuentra en la página de tecnología de Branch. En este cuadro, se te muestra la clave de importación de datos y el endpoint REST.]({% image_buster /assets/img/attribution/branch.png %}){: style="max-width:90%;"}

### Paso 3: Configurar fuentes de datos {#step-3-set-up-data-feeds}

1. En Branch, en la sección **Exports**, selecciona **Data Feeds**.
2. En la página **Data Feeds Administrador**, selecciona la pestaña **Data Integrations** en la parte superior de la página.
3. Selecciona Braze de la lista de partners de datos disponibles.
4. En la página de exportación de Braze, proporciona la clave de importación de datos y el endpoint REST or transferencia de estado representacional que encontraste en el panel de Braze y selecciona **Enable**.

### Paso 4: Confirmar la integración {#step-4-confirm-the-integration}

Después de que Braze reciba los datos de atribución de Branch, el indicador de estado de la conexión en la página de socios tecnológicos de Branch en Braze cambia de "Not Connected" a "Connected" e incluye una marca de tiempo de la última solicitud realizada con éxito.

Este estado solo cambia cuando Braze recibe datos sobre una instalación atribuida. Braze ignora las instalaciones orgánicas (las excluye del postback de Branch) y no las cuenta a la hora de determinar si la conexión se ha realizado correctamente.

## Mapeado de campos {#field-mapping}

Los campos de atribución de Branch se mapean a Braze de la siguiente manera:

| Campo de Branch | Campo de Braze |
| --- | --- |
| Campaign | `campaign` |
| Channel | `source` |
| Ad Set Name | `adgroup` |
| Ad Name | `ad` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Mapeado de campos de Branch" }

## Datos de atribución de Facebook y X (antes Twitter) {#facebook-and-x-formerly-twitter-attribution-data}

Los datos de atribución de las campañas de Facebook y X (antes Twitter) no están disponibles a través de nuestros partners. Estas fuentes de medios no permiten a sus partners compartir datos de atribución con terceros y, por lo tanto, nuestros partners no pueden enviar esos datos a Braze.

## URL de seguimiento de clics de Branch en Braze (opcional) {#branch-click-tracking-urls-in-braze-optional}

El uso de enlaces de seguimiento de clics en tus campañas de Braze te permitirá ver fácilmente qué campañas están impulsando la instalación de aplicaciones y la reactivación. Como resultado, podrás medir tus esfuerzos de marketing con mayor eficacia y tomar decisiones basadas en datos sobre dónde invertir más recursos para obtener el máximo ROI or retorno de la inversión.

Para empezar a utilizar los enlaces de seguimiento de clics de Branch, visita su [documentación](https://help.branch.io/using-branch/docs/ad-links). Puedes insertar directamente los enlaces de seguimiento de clics de Branch en tus campañas de Braze. A continuación, Branch utilizará sus [metodologías de atribución probabilística](https://help.branch.io/using-branch/docs/branch-attribution-logic-settings) para atribuir al usuario que ha hecho clic en el enlace. Te recomendamos que añadas a tus enlaces de seguimiento de Branch un identificador de dispositivo para mejorar la precisión de las atribuciones de tus campañas de Braze. Esto atribuirá de forma determinista al usuario que ha hecho clic en el enlace.

{% tabs local %}
{% tab Android %}
Para Android, Braze permite a los clientes la adhesión voluntaria a la [recopilación de ID de publicidad de Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection#optional-google-advertising-id). El GAID también se recoge de forma nativa a través de la integración del SDK or kit de desarrollo de software de Branch. Puedes incluir el GAID en tus enlaces de seguimiento de clics de Branch utilizando la siguiente lógica de Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
user_data_aaid={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto Braze como Branch recogen automáticamente el IDFV de forma nativa a través de nuestras integraciones de SDK or kit de desarrollo de software. Puede utilizarse como identificador del dispositivo. Puedes incluir el IDFV en tus enlaces de seguimiento de clics de Branch utilizando la siguiente lógica de Liquid:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
user_data_idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**Esta recomendación es puramente opcional**<br>
Si actualmente no utilizas ningún identificador de dispositivo —como el IDFV o el GAID— en tus enlaces de seguimiento de clics, o no piensas hacerlo en el futuro, Branch podrá seguir atribuyendo estos clics mediante su modelado probabilístico.
{% endalert %}