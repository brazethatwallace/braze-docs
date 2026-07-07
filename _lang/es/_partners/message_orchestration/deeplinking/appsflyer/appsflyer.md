---
nav_title: AppsFlyer
article_title: AppsFlyer
alias: /partners/appsflyer/
description: "Este artículo de referencia describe la asociación entre Braze y AppsFlyer, una plataforma de análisis y atribución de marketing móvil que te ayuda a analizar y optimizar tus aplicaciones."
page_type: partner
search_tag: Partner

---

# AppsFlyer

{% multi_lang_include video.html id="gQ9y2DA2LuQ" align="right" %}

> [AppsFlyer](https://www.appsflyer.com/) es una plataforma de análisis y atribución de marketing móvil que te ayuda a analizar y optimizar tus aplicaciones mediante análisis de marketing, atribución móvil y vinculación en profundidad.

La integración de Braze y AppsFlyer te permite comprender mejor cómo optimizar y crear campañas más holísticas aprovechando los datos de atribución de instalaciones móviles de AppsFlyer.

También puedes pasar tus audiencias (cohortes) de AppsFlyer directamente a Braze con la integración [AppsFlyer Audiences]({{site.baseurl}}/partners/data_and_analytics/cohort_import/appsflyer_audiences/), lo que te permite crear potentes campañas de interacción con los clientes dirigidas a los usuarios adecuados en el momento oportuno.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta de AppsFlyer | Se necesita una cuenta de AppsFlyer para beneficiarse de esta asociación. |
| Aplicación para iOS o Android | Esta integración es compatible con aplicaciones iOS y Android. Dependiendo de tu plataforma, es posible que se requieran fragmentos de código en tu aplicación. Encontrarás más detalles sobre estos requisitos en el paso 1 del proceso de integración. |
| SDK de AppsFlyer | Además del SDK de Braze necesario, debes instalar el [SDK de AppsFlyer](https://dev.appsflyer.com/hc/docs/getting-started).
| Configuración completa del dominio de correo electrónico | Debes haber completado el [paso de configuración de IP y dominio]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/) para configurar tu correo electrónico durante la incorporación a Braze. |
| Certificado SSL | Tu [certificado SSL]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl/#acquiring-an-ssl-certificate) debe estar configurado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Mapear ID de dispositivo {#step-1-map-device-id}

{% tabs local %}
{% tab Android %}
Si tienes una aplicación Android, debes pasar un ID de dispositivo Braze único a AppsFlyer.

Asegúrate de que las siguientes líneas de código se insertan en el lugar correcto: después de iniciar el SDK de Braze y antes del código de inicialización del SDK de AppsFlyer. Consulta la [guía de integración del SDK de Android](https://dev.appsflyer.com/hc/docs/integrate-android-sdk#initializing-the-android-sdk) de AppsFlyer para obtener más información.

```kotlin
val customData = HashMap<String, Any>()
Braze.getInstance(context).getDeviceIdAsync { deviceId ->
   customData["brazeCustomerId"] = deviceId
   setAdditionalData(customData)
}
```
{% endtab %}

{% tab ios %}
{% alert important %}
Antes de febrero de 2023, nuestra integración de atribución de AppsFlyer utilizaba el Identificador de Vendedor (IDFV) como identificador principal para cotejar los datos de atribución de iOS. No es necesario que los clientes de Braze que utilicen Objective-C obtengan el `device_id` de Braze y lo envíen a AppsFlyer en la instalación, porque no se interrumpe el servicio.
{% endalert%}

Para los que utilicen el SDK Swift v5.7.0+, si quieres seguir utilizando IDFV como identificador mutuo, debes confirmar que el campo `useUUIDAsDeviceId` está configurado en `false` para evitar una interrupción de la integración.

Si se establece en `true`, debes implementar el mapeado de ID de dispositivo iOS para Swift con el fin de pasar el `device_id` de Braze a AppsFlyer en la instalación de la aplicación para que Braze coincida adecuadamente con las atribuciones de iOS.

{% subtabs local %}
{% subtab Swift %}

```swift
let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>")
configuration.useUUIDAsDeviceId = false
let braze = Braze(configuration: configuration)
AppsFlyerLib.shared().customData = ["brazeDeviceId": braze.deviceId]
```
{% endsubtab %}

{% subtab Objective-C %}
```objc
BRZConfiguration *configurations = [[BRZConfiguration alloc] initWithApiKey:@"BRAZE_API_KEY" endpoint:@"BRAZE_END_POINT"];
[configurations setUseUUIDAsDeviceId:NO];
Braze *braze = [[Braze alloc] initWithConfiguration:configurations];
[[AppsFlyerLib shared] setAdditionalData:@{
    @"brazeDeviceId": braze.deviceId
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab unity %}
Para mapear el ID del dispositivo en Unity, utiliza lo siguiente:

```
Appboy.AppboyBinding.getDeviceId()
Dictionary<string, string> customData = new Dictionary<string, string>();
customData.Add("brazeCustomerId", Appboy.AppboyBinding.getDeviceId());
AppsFlyer.setAdditionalData(customData);
```
{% endtab %}
{% endtabs %}

### Paso 2: Obtener la clave de importación de datos de Braze {#step-2-get-the-braze-data-import-key}

En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **AppsFlyer**.

Aquí encontrarás el punto de conexión REST y generarás tu clave de importación de datos de Braze. Una vez generada la clave, puedes crear una nueva o invalidar una existente. La clave de importación de datos y el punto de conexión REST se utilizan en el siguiente paso cuando se configura un postback en el dashboard de AppsFlyer.<br><br>![El cuadro "Importación de datos para la atribución de instalaciones" disponible en la página de tecnología de AppsFlyer. En este cuadro se incluye la clave de importación de datos y el punto de conexión REST.]({% image_buster /assets/img/attribution/appsflyer.png %}){: style="max-width:70%;"}

### Paso 3: Configurar Braze en el dashboard de AppsFlyer {#step-3-configure-braze-in-appsflyers-dashboard}

1. En AppsFlyer, ve a la página de **Integrated Partners** en la barra de la izquierda. A continuación, busca **Braze** y selecciona el logotipo de Braze para abrir una ventana de configuración.
2. Dentro de la pestaña **Integration**, activa **Activate Partner**.
3. Proporciona la clave de importación de datos y el punto de conexión REST que encontraste en el dashboard de Braze.
4. Desactiva **Advanced Privacy** y guarda la configuración.

{% alert important %}
Al introducir el punto de conexión REST de Braze en la pestaña de integración de AppsFlyer, introduce solo el dominio (por ejemplo, `rest.fra-02.braze.eu`) sin el protocolo `https://` y sin la ruta `/attribution/appsflyer`. AppsFlyer antepone automáticamente el protocolo y añade la ruta. Incluir cualquiera de los dos en tu entrada provoca fallos en el postback.
{% endalert %}

Encontrarás información adicional sobre estas instrucciones en [la documentación de AppsFlyer](https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration).

### Paso 4: Confirmar la integración {#step-4-confirm-the-integration}

En la página de socios tecnológicos de AppsFlyer en Braze, el indicador de conexión muestra **Not Connected** hasta que generes una clave de API de importación de datos en el paso 2. Después de generar la clave, el indicador cambia a **Connected** y muestra una marca de tiempo. Esa marca de tiempo refleja cuándo se configuró la integración por primera vez en Braze (cuando se creó la clave de importación de datos), no cuándo AppsFlyer envió un postback por última vez.

Para confirmar que los datos de atribución de instalación están fluyendo desde AppsFlyer, utiliza el paso 5 para verificar que los datos de instalación no orgánica aparecen en los filtros de segmento de Braze. Braze ignora las instalaciones orgánicas de los postbacks de AppsFlyer y no las almacena como datos de instalación atribuida.

### Paso 5: Visualización de los datos de atribución de los usuarios {#step-5-viewing-user-attribution-data}

#### Campos de datos disponibles {#available-data-fields}

Si la integración se ha realizado correctamente, Braze mapea todos los datos de instalación no orgánicos en filtros de segmento.

| Campo de datos de AppsFlyer | Filtro de segmento de Braze |
| -------------------- | --------------------- |
| `media_source` | Fuente atribuida |
| `campaign` | Campaign atribuida |
| `af_adset` | Grupo de anuncios atribuido |
| `af_ad` | Anuncio atribuido |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campos de datos disponibles" }

Puedes segmentar tu base de usuarios por datos de atribución en el dashboard de Braze utilizando los filtros de atribución de instalación.

![Cuatro filtros disponibles. El primero es "La fuente de atribución de instalación es network_val_0". El segundo es "La fuente de atribución de instalación es campaign_val_0". El tercero es "La fuente de atribución de instalación es adgroup_val_0". El cuarto es "La fuente de atribución de instalación es creative_val_0". Junto a los filtros enumerados, puedes ver cómo se añadirán estas fuentes de atribución al perfil de usuario. En el cuadro "Atribución de instalación" de la página de información de un usuario, la fuente de instalación aparece como network_val_0, y la Campaign como campaign_val_0, etc.]({% image_buster /assets/img/braze_attribution.png %})

Además, los datos de atribución de un usuario concreto están disponibles en el perfil de cada usuario en el dashboard de Braze.

{% alert note %}
Los datos de atribución de las campañas de Facebook y X (antes Twitter) no están disponibles a través de nuestros socios. Estas fuentes de medios no permiten a sus socios compartir datos de atribución con terceros y, por lo tanto, nuestros socios no pueden enviar esos datos a Braze.
{% endalert %}

## Integrar AppsFlyer con Braze para vinculación en profundidad {#integrate-appsflyer-with-braze-for-deep-linking}

Los vínculos profundos&#8212;enlaces que dirigen a los usuarios a una página o lugar específicos dentro de una aplicación o sitio web&#8212;se utilizan para crear una experiencia de usuario personalizada.

Aunque su uso está muy extendido, pueden surgir problemas al utilizar vínculos profundos por correo electrónico con seguimiento de clics&#8212;otra característica importante utilizada en la recopilación de datos de usuario. Estos problemas se deben a que los proveedores de servicios de correo electrónico (ESP) envuelven los vínculos profundos en un dominio de registro de clics, rompiendo el vínculo original. Por lo tanto, la compatibilidad con los vínculos profundos requiere una configuración adicional.

AppsFlyer proporciona un [servicio](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer) que evita estos problemas, habilitando a AppsFlyer para que actúe como intermediario entre el servidor ESP y tu dominio. Su papel como proxy habilita la provisión de archivos de asociación (AASA/vínculos de activos), lo que facilita la vinculación en profundidad.

## Paso 1: Crear un dominio de seguimiento de clics {#step-1-create-a-click-tracking-domain}

Siguiendo los elementos iniciales de [la guía de configuración de correo electrónico de Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl/#acquiring-an-ssl-certificate), crea un dominio de envío de correo electrónico y un dominio de seguimiento de clics. Para obtener asistencia, puedes crear un ticket a través del dashboard de Braze para iniciar la configuración del nuevo CTD con el equipo de correo electrónico de Braze.

![La interfaz de usuario de Braze muestra el botón "Get Help", que se encuentra debajo del botón "Support" en la esquina superior derecha]({% image_buster /assets/img/attribution/appsflyer/1.png %})

Es obligatorio crear un nuevo CTD, aunque ya utilices uno existente. Esto garantiza que no haya ningún impacto en el tráfico de las campañas de correo electrónico en vivo actuales.

{% alert important%}
AppsFlyer crea el certificado SSL. En esta fase, es probable que los enlaces de correo electrónico no sean seguros, es decir, que el prefijo de la URL sea HTTP en lugar de HTTPS. Esto se resuelve en pasos posteriores.
{%endalert%}

## Paso 2: Crear una plantilla OneLink en AppsFlyer {#step-2-create-a-onelink-template-in-appsflyer}
Crea una [plantilla OneLink](https://support.appsflyer.com/hc/en-us/articles/207032246-Create-a-OneLink-template#procedures) y configura Universal Links/App Links en "When app is installed". Esta plantilla se utiliza posteriormente para crear enlaces OneLink para tus campañas de correo electrónico.

{% alert note%} Si ya tienes configurada una plantilla OneLink que habilita Universal Links/App Links, puedes utilizarla.
{%endalert%}

## Paso 3: Configura tu integración de Braze en AppsFlyer {#step-3-set-up-your-braze-integration-in-appsflyer}
Ahora es el momento de configurar tu integración de Braze en AppsFlyer. Este paso y el siguiente ("Configura tu aplicación") pueden configurarse al mismo tiempo.
Para configurar tu integración de Braze en AppsFlyer:

### 1. En AppsFlyer, en el menú lateral, selecciona Engage > ESP integration. {#1-in-appsflyer-from-the-side-menu-select-engage-esp-integration}
![La interfaz de usuario de AppsFlyer muestra el botón "ESP Integration", que se encuentra en el menú de la izquierda]({% image_buster /assets/img/attribution/appsflyer/2.png %})


### 2. Selecciona Braze. {#2-select-braze}
![La interfaz de usuario de AppsFlyer muestra la lista de integraciones ESP, incluida Braze.]({% image_buster /assets/img/attribution/appsflyer/3.png %})


### 3. Selecciona la plantilla OneLink que deseas utilizar para las campañas de correo electrónico y, a continuación, haz clic en Next. {#3-select-the-onelink-template-you-want-to-use-for-email-campaigns-then-click-next}
![La interfaz de usuario de AppsFlyer muestra el menú desplegable que permite a los usuarios seleccionar su plantilla.]({% image_buster /assets/img/attribution/appsflyer/4.png %})


### 4. Introduce tu dominio de seguimiento de clics y el valor "Braze endpoint", que se proporcionó con el nuevo CTD creado en el paso 1, y luego haz clic en Validate connection. {#4-enter-your-click-tracking-domain-and-braze-endpoint-value-which-was-provided-with-the-new-ctd-created-in-step-1-then-click-validate-connection}

Esto valida que el dominio de seguimiento de clics apunta al punto de conexión que has introducido.

![La interfaz de usuario de AppsFlyer resalta dónde los clientes deben añadir su dominio de seguimiento de clics y los detalles asociados.]({% image_buster /assets/img/attribution/appsflyer/5.png %})

Con "Braze Endpoint", AppsFlyer está pidiendo los detalles proporcionados por Braze en el paso 1 de esta guía, concretamente el nuevo CTD.

A continuación, haz clic en **Validate connection**, que valida que el dominio de seguimiento de clics apunta al punto de conexión que has introducido.
Cuando hayas terminado, haz clic en **Next**.

### 5. Enruta el tráfico de enlaces a AppsFlyer: {#5-route-link-traffic-to-appsflyer}

#### a. Copia y envía las instrucciones personalizadas prefabricadas en AppsFlyer a tu administrador de TI o de dominio. {#a-copy-and-send-the-customized-pre-fabricated-instructions-in-appsflyer-to-your-it-or-domain-administrator}

Tu administrador debe redirigir el tráfico de tu campaña de correo electrónico desde los servidores ESP a los servidores de AppsFlyer actualizando tus registros de DNS CNAME con el nuevo dominio que AppsFlyer te ha proporcionado.

Como resultado, cada vez que se hace clic en un enlace, el clic se redirige a AppsFlyer, que a su vez lo redirige al punto de conexión ESP.

![Diagrama que ilustra cómo los datos de los clics pasan de tu dominio, a AppsFlyer, a tu punto de conexión ESP]({% image_buster /assets/img/attribution/appsflyer/6.png %})

#### b. Después de copiar y enviar las instrucciones, haz clic en Done. {#b-after-copying-and-sending-the-instructions-click-done}
Se ha creado tu integración de Braze.

{%alert important%}
El estado de tu integración de Braze es pendiente y solo empezará a funcionar una vez mapeado el registro CNAME. Una nueva integración puede tardar hasta 24 horas después de ser mapeada en empezar a funcionar y activarse.
{%endalert%}

## Paso 4: Configura tu aplicación (tarea del desarrollador) {#step-4-configure-your-app-developer-task}
AppsFlyer [ofrece orientación](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer#step-2-configure-your-app-developer-task) sobre la correcta configuración de la aplicación, que deben seguir tus equipos web o de aplicaciones para soportar el enlace universal.

## Paso 5: Confirma que el seguimiento de clics SSL está habilitado con Braze {#step-5-confirm-ssl-click-tracking-is-enabled-with-braze}

En esta fase, después de compartir y validar los detalles del CTD en AppsFlyer, te recomendamos que realices un envío de prueba para confirmar si tu dominio de envío OneLink tiene un certificado SSL. Esto se ajusta a nuestra guía de [configuración del correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl/#acquiring-an-ssl-certificate).

Puedes realizar la garantía de calidad y la solución de problemas enviando un vínculo profundo mediante OneLink. Consulta la [documentación de AppsFlyer](https://support.appsflyer.com/hc/en-us/articles/360001437497-Integrating-AppsFlyer-and-Braze#step-3-sending-your-first-email::2ffdb79a) para más detalles sobre el uso de OneLink.

Si los enlaces CTD se identifican como HTTP, ponte en contacto con el equipo de operaciones de correo electrónico de Braze para habilitar el seguimiento de clics SSL. Esto garantiza que todos los enlaces HTTP se conviertan automáticamente a HTTPS.
Puedes utilizar el siguiente ejemplo de texto de mensaje cuando te pongas en contacto con tu administrador del éxito del cliente, o volviendo a crear un ticket en el dashboard de Braze, como en el paso 1:

```
Hi Team,
Could you please enable SSL click tracking for CTD XXX? It is currently set to HTTP instead of HTTPS.
```

### URL de seguimiento de clics de AppsFlyer en Braze (opcional) {#appsflyer-click-tracking-urls-in-braze-optional}

Puedes utilizar los [enlaces de atribución OneLink](https://support.AppsFlyer.com/hc/en-us/articles/360001294118) de AppsFlyer en Campaigns de Braze a través de push, correo electrónico y más. Esto te permite enviar datos de atribución de instalación o reactivación de la interacción de tus Campaigns de Braze a AppsFlyer. Como resultado, podrás medir tus esfuerzos de marketing con mayor eficacia y tomar decisiones basadas en datos.

Puedes simplemente crear tu URL de seguimiento OneLink en AppsFlyer e insertarla directamente en tus Campaigns de Braze. AppsFlyer utiliza entonces sus [metodologías de atribución probabilística](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling) para atribuir al usuario que ha hecho clic en el enlace. Te recomendamos que añadas a tus enlaces de seguimiento de AppsFlyer un identificador de dispositivo para mejorar la precisión de las atribuciones de tus Campaigns de Braze. Esto atribuye de forma determinista al usuario que ha hecho clic en el enlace.

{% tabs local %}
{% tab Android %}
Para Android, Braze permite a los clientes la adhesión voluntaria a la [recopilación de ID de publicidad de Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). La integración del SDK de AppsFlyer también recoge el GAID. Puedes incluir el GAID en tus enlaces de seguimiento de clics de AppsFlyer utilizando la siguiente lógica de Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto Braze como AppsFlyer recopilan automáticamente el IDFV de forma nativa a través de nuestras integraciones de SDK. Puedes utilizar el IDFV como identificador del dispositivo. Puedes incluir el IDFV en tus enlaces de seguimiento de clics de AppsFlyer utilizando la siguiente lógica de Liquid:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}