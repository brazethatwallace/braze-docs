---
nav_title: Adjust
article_title: Adjust
alias: /partners/adjust/
description: "Este artículo de referencia describe la asociación entre Braze y Adjust, una empresa de atribución y análisis de móviles que te permite importar datos de atribución de instalaciones no orgánicas para segmentar de forma más inteligente dentro de tus campañas según el ciclo de vida."
page_type: partner
search_tag: Partner

---

# Adjust

> [Adjust](https://www.adjust.com/) es una empresa de atribución y análisis de móviles que combina la atribución de fuentes publicitarias con análisis avanzados para obtener una visión completa de la inteligencia empresarial.

_Esta integración es mantenida por Adjust._

## Sobre la integración {#about-the-integration}

La integración de Braze y Adjust te permite importar datos de atribución de instalaciones no orgánicas para segmentar de forma más inteligente dentro de tus campañas según el ciclo de vida.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta de Adjust | Se necesita una cuenta de Adjust para beneficiarse de esta asociación. |
| Aplicación para iOS o Android | Esta integración es compatible con aplicaciones iOS y Android. Dependiendo de tu plataforma, es posible que se requieran fragmentos de código en tu aplicación. Encontrarás más detalles sobre estos requisitos en el paso 1 del proceso de integración. |
| SDK or kit de desarrollo de software de Adjust | Además del SDK or kit de desarrollo de software de Braze necesario, debes instalar el [SDK or kit de desarrollo de software de Adjust](https://dev.adjust.com/en/sdk). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Mapear ID de dispositivos {#step-1-map-device-ids}

#### Android

Si tienes una aplicación Android, debes pasar un ID de dispositivo Braze único a Adjust. Este ID puede establecerse en el método `addGlobalPartnerParameter()` del SDK or kit de desarrollo de software de Adjust. El siguiente fragmento de código debe incluirse antes de inicializar el SDK or kit de desarrollo de software en `Adjust.initSdk.`

```
Adjust.addGlobalPartnerParameter("braze_device_id", Braze.getInstance(getApplicationContext()).getDeviceId()););
```

#### iOS

<!--
{% alert important %}
Prior to February 2023, our Adjust attribution integration used the Identifier for Vendor (IDFV) as the primary identifier to match iOS attribution data. Braze customers don't need to use Objective-C to fetch the Braze `device_id` and send it to Adjust upon installation because there is no service disruption.
{% endalert%}

For those using the Swift SDK or kit de desarrollo de software v5.7.0+, if you wish to continue using IDFV as the mutual identifier, you must ensure that the `useUUIDAsDeviceId` field is set to `false` so there is no disruption of the integration.

If set to `true`, you must implement the iOS device ID mapping for Swift to pass the Braze `device_id` to Adjust upon app installation in order for Braze to match iOS attributions appropriately.
--->

{% tabs local %}
{% tab Objective-C %}

Si tienes una aplicación iOS, tu IDFV será recogido por Adjust y enviado a Braze. Este ID se asignará a un ID de dispositivo único en Braze.

Braze seguirá almacenando los valores IDFA de los usuarios que hayan optado por la adhesión voluntaria si estás recopilando el IDFA con Braze, tal y como se describe en nuestra [Guía de actualización de iOS]({{site.baseurl}}/developer_guide/platforms/swift/ios_18/). En caso contrario, el IDFV se utilizará como identificador alternativo para asignar usuarios.

{% endtab %}
{% tab Swift %}

Si tienes una aplicación para iOS, puedes optar por recoger IDFV configurando el campo `useUUIDAsDeviceId` en `false`. Si no se establece, es probable que la atribución de iOS no se asigne con precisión de Adjust a Braze. Para más información, consulta [Recoger IDFV]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift).

{% endtab %}
{% endtabs %}

{% alert note %}
Si piensas enviar eventos posteriores a la instalación desde Adjust a Braze, tendrás que hacer lo siguiente: <br><br>1) Asegúrate de que añades `external_id` como parámetro de sesión y evento dentro del SDK or kit de desarrollo de software de Adjust. Para el reenvío de eventos de ingresos, también tendrás que configurar `product_id` como parámetro para los eventos. Visita [la documentación de Adjust](https://github.com/adjust/sdks) para obtener más información sobre la definición de parámetros de socio para el reenvío de eventos.<br><br>2) Genera una nueva clave de API para introducirla en Adjust. Para ello, selecciona el botón **Generate API Key** que encontrarás en la página del socio Adjust en el panel de Braze.
{% endalert %}

### Paso 2: Obtener la clave de importación de datos de Braze {#step-2-get-the-braze-data-import-key}

En Braze, ve a **Integraciones** > **Socios tecnológicos** y selecciona **Adjust**.

Aquí encontrarás el punto de conexión REST y generarás tu clave de importación de datos de Braze. Una vez generada la clave, puedes crear una nueva o invalidar una existente. La clave de importación de datos y el punto de conexión REST se utilizan en el siguiente paso cuando se configura un postback en el dashboard de Adjust.<br><br>![Esta imagen muestra la casilla "Importación de datos para la atribución de instalación" que se encuentra en la página de tecnología de Adjust. En este cuadro, se te muestra la clave de importación de datos y el punto de conexión REST.]({% image_buster /assets/img/attribution/adjust.png %}){: style="max-width:90%;"}

### Paso 3: Configurar Braze en Adjust {#step-3-configure-braze-in-adjust}

1. En el dashboard de Adjust, ve a **App Settings** y navega a **Partner Setup** y, a continuación, **Add Partners**.
2. Selecciona **Braze (formerly Appboy)** y proporciona la clave de importación de datos y el punto de conexión REST or transferencia de estado representacional de Braze.
3. Haz clic en **Save & Close**.

### Paso 4: Confirmar la integración {#step-4-confirm-the-integration}

Después de que Braze reciba datos de atribución de Adjust, el indicador de estado de la conexión en la página de socios tecnológicos de Adjust en Braze cambia de "Not Connected" a "Connected" e incluye una marca de tiempo de la última solicitud realizada con éxito.

Este estado solo cambia cuando Braze recibe datos sobre una instalación atribuida. Braze ignora las instalaciones orgánicas (las excluye del postback de Adjust) y no las cuenta a la hora de determinar si la conexión se ha realizado correctamente.

## Campos de datos disponibles {#available-data-fields}

Suponiendo que configures tu integración como se sugiere, Braze asignará los datos de Adjust a filtros de segmento como se describe en la siguiente tabla.

| Campo de datos de Adjust | Filtro de segmento de Braze |
| --- | --- |
| `{network_name}` | Attributed Source |
| `{campaign_name}` | Attributed Campaign |
| `{adgroup_name}` | Attributed Adgroup |
| `{creative_name}` | Attributed Ad |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campos de datos disponibles" }

## Datos de atribución de Facebook y X (antes Twitter) {#facebook-and-x-formerly-twitter-attribution-data}

Los datos de atribución de las campañas de Facebook y X (antes Twitter) no están disponibles a través de nuestros socios. Estas fuentes de medios no permiten a sus socios compartir datos de atribución con terceros y, por lo tanto, nuestros socios no pueden enviar esos datos a Braze.

## URL de seguimiento de clics de Adjust en Braze (opcional) {#adjust-click-tracking-urls-in-braze-optional}

El uso de enlaces de seguimiento de clics en tus campañas de Braze te permitirá ver fácilmente qué campañas están impulsando la instalación de aplicaciones y la reactivación de la interacción. Como resultado, podrás medir tus esfuerzos de marketing con mayor eficacia y tomar decisiones basadas en datos sobre dónde invertir más recursos para obtener el máximo ROI or retorno de la inversión.

Para empezar a utilizar los enlaces de seguimiento de clics de Adjust, visita su [documentación](https://help.adjust.com/tracking/attribution/tracker-urls). Puedes insertar directamente los enlaces de seguimiento de clics de Adjust en tus campañas de Braze. Adjust utilizará entonces sus [metodologías de atribución probabilística](https://www.adjust.com/blog/attribution-compatible-with-ios14/) para atribuir al usuario que ha hecho clic en el enlace. Te recomendamos que añadas un identificador de dispositivo a tus enlaces de seguimiento de Adjust para mejorar la precisión de las atribuciones de tus campañas de Braze. Esto atribuirá de forma determinista al usuario que ha hecho clic en el enlace.

{% tabs local %}
{% tab Android %}
Para Android, Braze permite a los clientes la adhesión voluntaria a la [recopilación de ID de publicidad de Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration/#google-advertising-id). El GAID también se recoge de forma nativa a través de la integración del SDK or kit de desarrollo de software de Adjust. Puedes incluir el GAID en tus enlaces de seguimiento de clics de Adjust utilizando la siguiente lógica de Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto Braze como Adjust recopilan automáticamente el IDFV de forma nativa a través de nuestras integraciones de SDK or kit de desarrollo de software. Puede utilizarse como identificador del dispositivo. Puedes incluir el IDFV en tus enlaces de seguimiento de clics de Adjust utilizando la siguiente lógica de Liquid:

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
Si actualmente no utilizas ningún identificador de dispositivo —como el IDFV o el GAID— en tus enlaces de seguimiento de clics, o no piensas hacerlo en el futuro, Adjust podrá seguir atribuyendo estos clics mediante su modelado probabilístico.
{% endalert %}