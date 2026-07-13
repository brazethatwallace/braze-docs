---
nav_title: Kochava
article_title: Kochava
alias: /partners/kochava/
description: "Este artículo de referencia describe la asociación entre Braze y Kochava, una plataforma de atribución móvil que ofrece información de atribución y análisis para ayudarte a aprovechar tus datos para el crecimiento."
page_type: partner
search_tag: Partner

---

# Kochava

> [Kochava](https://www.kochava.com/) ofrece atribución y análisis móviles para ayudarte a aprovechar tus datos para crecer. La plataforma de audiencia de Kochava te permite planificar, direccionar, activar, medir y optimizar tus campañas de aplicaciones.

_Esta integración está mantenida por Kochava._

## Sobre la integración {#about-the-integration}

La integración de Braze y Kochava ayuda a impulsar una comprensión más holística de tus campañas mediante el envío de datos de atribución a Braze para comprender mejor qué campañas están impulsando las instalaciones, la actividad dentro de la aplicación y mucho más.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta Kochava | Para beneficiarte de esta asociación es necesario disponer de una cuenta Kochava. |
| Aplicación para iOS o Android | Esta integración es compatible con aplicaciones iOS y Android. Dependiendo de tu plataforma, es posible que se requieran fragmentos de código en tu aplicación. Encontrarás más detalles sobre estos requisitos en el paso 1 del proceso de integración. |
| SDK de Kochava | Además del SDK de Braze necesario, debes instalar el [SDK de Kochava](https://support.kochava.com/sdk-integration/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración {#integration}

### Paso 1: Asignar ID de usuario {#step-1-map-user-ids}

#### Android

El SDK [de Android](https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3) genera un identificador único global (GUID) como ID de Braze al iniciar la sesión. Este identificador debe pasarse al método Kochava `IdentityLink` para que Braze pueda reconciliar los datos con el perfil de usuario correcto. Recupera el ID de Braze con el siguiente método:

```java
Apppboy.getInstance(context).getDeviceId();
```

#### iOS

{% alert important %}
Antes de febrero de 2023, nuestra integración de atribución de Kochava utilizaba el identificador de vendedor (IDFV) como identificador principal para hacer coincidir los datos de atribución de iOS. No es necesario que los clientes de Braze que utilicen Objective-C obtengan el `device_id` de Braze y lo envíen a Kochava durante la instalación, porque no se interrumpe el servicio.
{% endalert%}

Para los que utilicen Swift SDK v5.7.0+, si deseas seguir utilizando IDFV como identificador mutuo, debes asegurarte de que el campo `useUUIDAsDeviceId` está configurado en `false` para que no haya interrupciones en la integración. Si se establece en `true`, debes implementar la asignación de ID de dispositivo iOS para Swift con el fin de pasar el `device_id` de Braze a Kochava al instalar la aplicación para que Braze coincida correctamente con las atribuciones de iOS.

Braze tiene dos API que producirán el mismo valor, una con un controlador de finalización y otra usando el nuevo soporte de concurrencia de Swift. Ten en cuenta que tendrás que modificar los siguientes fragmentos de código para ajustarlos a las instrucciones del [SDK para iOS](https://support.kochava.com/sdk-integration/ios-sdk-integration/) de Kochava. Si necesitas más ayuda, ponte en contacto con el soporte de Kochava.

##### Controlador de finalización {#completion-handler}
```
AppDelegate.braze?.deviceId(completion: { deviceId in
  // Use `deviceId`
})
```
##### Concurrencia Swift {#swift-concurrency}
```
let deviceId = await AppDelegate.braze?.deviceId()
```

### Paso 2: Obtener la clave de importación de datos de Braze {#step-2-get-the-braze-data-import-key}

En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **Kochava**.

Aquí encontrarás el punto de conexión REST y generarás tu clave de importación de datos de Braze. Una vez generada la clave, puedes crear una nueva o invalidar una existente. La clave de importación de datos y el punto de conexión REST se utilizan en el siguiente paso al configurar un postback en el dashboard de Kochava.<br><br>![Esta imagen muestra la casilla "Importación de datos para la atribución de instalación" que se encuentra en la página de tecnología de Kochava. En este cuadro, se te muestra la clave de importación de datos y el punto de conexión REST.]({% image_buster /assets/img/attribution/kochava.png %}){: style="max-width:90%;"}

### Paso 3: Configurar un postback desde Kochava {#step-3-set-up-a-postback-from-kochava}

[Añade un postback](https://support.kochava.com/campaign-management/create-a-kochava-certified-postback) en tu dashboard de Kochava. Se te pedirá la clave de importación de datos y el punto de conexión REST que encontraste en el dashboard de Braze.

### Paso 4: Confirmar la integración {#step-4-confirm-the-integration}

Después de que Braze reciba los datos de atribución de Kochava, el indicador de estado de la conexión en la página de socios tecnológicos de Kochava en Braze cambia de "Not Connected" a "Connected" e incluye una marca de tiempo de la última solicitud realizada con éxito.

Este estado solo cambia cuando Braze recibe datos sobre una instalación atribuida. Braze ignora las instalaciones orgánicas (las excluye del postback de Kochava) y no las cuenta a la hora de determinar si la conexión se ha realizado correctamente.

## Datos de atribución de Facebook y X (antes Twitter) {#facebook-and-x-formerly-twitter-attribution-data}

Los datos de atribución de las campañas de Facebook y X (antes Twitter) no están disponibles a través de nuestros socios. Estas fuentes de medios no permiten a sus socios compartir datos de atribución con terceros y, por lo tanto, nuestros socios no pueden enviar esos datos a Braze.

## URL de seguimiento de clics de Kochava en Braze (opcional) {#kochava-click-tracking-urls-in-braze-optional}

El uso de enlaces de seguimiento de clics en tus campañas de Braze te permitirá ver fácilmente qué campañas están impulsando la instalación de aplicaciones y la reactivación de la interacción. Como resultado, podrás medir tus esfuerzos de marketing con mayor eficacia y tomar decisiones basadas en datos sobre dónde invertir más recursos para obtener el máximo ROI.

Para empezar a utilizar los enlaces de seguimiento de clics de Kochava, visita su [documentación](https://support.kochava.com/reference-information/attribution-overview/). Puedes insertar directamente los enlaces de seguimiento de clics de Kochava en tus campañas de Braze. Kochava utilizará entonces sus [metodologías de atribución probabilística](https://www.kochava.com/getting-prepared-for-ios-14/) para atribuir al usuario que ha hecho clic en el enlace. Te recomendamos que añadas un identificador de dispositivo a tus enlaces de seguimiento de Kochava para mejorar la precisión de las atribuciones de tus campañas de Braze. Esto atribuirá de forma determinista al usuario que ha hecho clic en el enlace.

{% tabs local %}
{% tab Android %}
Para Android, Braze permite a los clientes la adhesión voluntaria a la [recopilación de ID de publicidad de Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). El GAID también se recoge de forma nativa a través de la integración del SDK de Kochava. Puedes incluir el GAID en tus enlaces de seguimiento de clics de Kochava utilizando la siguiente lógica de Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto Braze como Kochava recopilan automáticamente el IDFV de forma nativa a través de nuestras integraciones de SDK. Puede utilizarse como identificador del dispositivo. Puedes incluir el IDFV en tus enlaces de seguimiento de clics de Kochava utilizando la siguiente lógica de Liquid:

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
Si actualmente no utilizas ningún identificador de dispositivo —como el IDFV o el GAID— en tus enlaces de seguimiento de clics, o no tienes previsto hacerlo en el futuro, Kochava podrá seguir atribuyendo estos clics a través de su modelado probabilístico.
{% endalert %}