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

También puedes pasar tus audiencias (cohortes) de AppsFlyer directamente a Braze con la integración [AppsFlyer Audiences]({{site.baseurl}}/partners/data_and_analytics/cohort_import/appsflyer_audiences), lo que te permite crear potentes campañas de interacción con los clientes dirigidas a los usuarios adecuados en el momento oportuno.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta de AppsFlyer | Se necesita una cuenta de AppsFlyer para aprovechar esta integración. |
| Aplicación iOS o Android | Esta integración es compatible con aplicaciones iOS y Android. Dependiendo de tu plataforma, es posible que se requieran fragmentos de código en tu aplicación. Los detalles sobre estos requisitos se encuentran en el paso 1 del proceso de integración. |
| SDK de AppsFlyer | Además del SDK de Braze requerido, debes instalar el [SDK de AppsFlyer](https://dev.appsflyer.com/hc/docs/getting-started). |
| Configuración del dominio de correo electrónico completa | Debes haber completado el [paso de configuración de IP y dominio]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains) de la configuración de tu correo electrónico durante la incorporación a Braze. |
| Certificado SSL | Tu [certificado SSL]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate) debe estar configurado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Mapear el ID del dispositivo {#step-1-map-device-id}

{% tabs local %}
{% tab Android %}
Si tienes una aplicación Android, debes pasar un ID de dispositivo Braze único a AppsFlyer.

Asegúrate de que las siguientes líneas de código se insertan en el lugar correcto, después del lanzamiento de Braze SDK y antes del código de inicialización del SDK de AppsFlyer. Consulta la [guía de integración del SDK de Android](https://dev.appsflyer.com/hc/docs/integrate-android-sdk#initializing-the-android-sdk) de AppsFlyer para obtener más información.

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
Antes de febrero de 2023, nuestra integración de atribución de AppsFlyer utilizaba el Identifier for Vendor (IDFV) como identificador principal para asociar los datos de atribución de iOS. No es necesario que los clientes de Braze que usan Objective-C obtengan el `device_id` de Braze y lo envíen a AppsFlyer durante la instalación, ya que no hay interrupción del servicio.
{% endalert%}

Para quienes usan Swift SDK v5.7.0+, si desean continuar usando IDFV como identificador mutuo, deben confirmar que el campo `useUUIDAsDeviceId` está configurado como `false` para evitar una interrupción de la integración.

Si se configura como `true`, debes implementar el mapeado de ID de dispositivo iOS para Swift con el fin de pasar el `device_id` de Braze a AppsFlyer durante la instalación de la aplicación, para que Braze asocie adecuadamente las atribuciones de iOS.

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

En Braze, ve a **Integraciones de partners** > **Partners tecnológicos** y selecciona **AppsFlyer**.

Aquí encontrarás el endpoint REST y podrás generar tu clave de importación de datos de Braze. Una vez generada la clave, puedes crear una nueva o invalidar una existente. La clave de importación de datos y el endpoint REST se utilizan en el siguiente paso para configurar un postback en el panel de AppsFlyer.<br><br>![El cuadro "Importación de datos para atribución de instalación" disponible en la página de tecnología de AppsFlyer. En este cuadro se incluyen la clave de importación de datos y el endpoint REST.]({% image_buster /assets/img/attribution/appsflyer.png %}){: style="max-width:70%;"}

### Paso 3: Configurar Braze en el panel de AppsFlyer {#step-3-configure-braze-in-appsflyers-dashboard}

1. En AppsFlyer, ve a la página **Integrated Partners** desde el menú de navegación. A continuación, busca **Braze** y selecciona el logotipo de Braze para abrir una ventana de configuración.
2. En la pestaña **Integration**, activa **Activate Partner**.
3. Proporciona la clave de importación de datos y el endpoint REST que encontraste en el panel de Braze.
4. Desactiva **Advanced Privacy** y guarda tu configuración.

{% alert important %}
Al introducir el endpoint REST de Braze en la pestaña de integración de AppsFlyer, ingresa solo el dominio (por ejemplo, `rest.fra-02.braze.eu`) sin el protocolo `https://` y sin la ruta `/attribution/appsflyer`. AppsFlyer antepone automáticamente el protocolo y añade la ruta. Incluir cualquiera de los dos en tu entrada provocará errores en los postbacks.
{% endalert %}

Puedes encontrar información adicional sobre estas instrucciones en la [documentación de AppsFlyer](https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration).

### Paso 4: Confirmar la integración {#step-4-confirm-the-integration}

En la página de partners tecnológicos de AppsFlyer en Braze, el indicador de conexión muestra **Not Connected** hasta que generes una clave de API de importación de datos en el paso 2. Después de generar la clave, el indicador cambia a **Connected** y muestra una marca temporal. Esa marca temporal refleja cuándo se configuró la integración por primera vez en Braze (cuando se creó la clave de importación de datos), no cuándo AppsFlyer envió un postback por última vez.

Para confirmar que los datos de atribución de instalación están llegando desde AppsFlyer, usa el paso 5 para verificar que los datos de instalaciones no orgánicas aparezcan en los filtros de Segment de Braze. Braze ignora las instalaciones orgánicas de los postbacks de AppsFlyer y no las almacena como datos de instalación atribuidos.

### Paso 5: Ver los datos de atribución de usuarios {#step-5-viewing-user-attribution-data}

#### Campos de datos disponibles {#available-data-fields}

Si tu integración fue exitosa, Braze mapea todos los datos de instalaciones no orgánicas a filtros de Segment.

| Campo de datos de AppsFlyer | Filtro de Segment de Braze |
| -------------------- | --------------------- |
| `media_source` | Attributed Source |
| `campaign` | Attributed Campaign |
| `af_adset` | Attributed Adgroup |
| `af_ad` | Attributed Ad |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campos de datos disponibles" }

Puedes segmentar tu base de usuarios por datos de atribución en el panel de Braze usando los filtros de atribución de instalación.

![Cuatro filtros disponibles. El primero es "Install Attribution Source is network_val_0". El segundo es "Install Attribution Source is campaign_val_0". El tercero es "Install Attribution Source is adgroup_val_0". El cuarto es "Install Attribution Source is creative_val_0". Junto a los filtros listados, puedes ver cómo estas fuentes de atribución se añaden al perfil de usuario. En el cuadro "Install Attribution" en la página de información de un usuario, Install Source aparece como network_val_0, campaign aparece como campaign_val_0, etc.]({% image_buster /assets/img/braze_attribution.png %})

Además, los datos de atribución de un usuario en particular están disponibles en el perfil de cada usuario en el panel de Braze.

{% alert note %}
Los datos de atribución de Campaigns de Facebook y X (anteriormente Twitter) no están disponibles a través de nuestros partners. Estas fuentes de medios no permiten que sus partners compartan datos de atribución con terceros y, por lo tanto, nuestros partners no pueden enviar esos datos a Braze.
{% endalert %}

## Integrar AppsFlyer con Braze para vinculación en profundidad {#integrate-appsflyer-with-braze-for-deep-linking}

Los vínculos profundos&#8212;enlaces que dirigen a los usuarios hacia una página o lugar específico dentro de una aplicación o sitio web&#8212;se utilizan para crear una experiencia de usuario personalizada.

Aunque se utilizan ampliamente, pueden surgir problemas al usar vínculos profundos en correos electrónicos con seguimiento de clics&#8212;otra característica importante utilizada en la recopilación de datos de usuario. Estos problemas se deben a que los proveedores de servicios de correo electrónico (ESP) envuelven los vínculos profundos en un dominio de registro de clics, rompiendo el enlace original. Por ello, la compatibilidad con vínculos profundos requiere una configuración adicional.

AppsFlyer proporciona un [servicio](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer) que evita estos problemas, permitiendo que AppsFlyer actúe como intermediario entre el servidor del ESP y tu nombre de dominio. Su función como proxy permite el suministro de archivos de asociación (AASA/asset links), lo que facilita la vinculación en profundidad.

## Paso 1 - Crear un dominio de seguimiento de clics {#step-1-create-a-click-tracking-domain}

Siguiendo los elementos iniciales de la [guía de configuración de correo electrónico de Braze]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate), crea un dominio de envío de correo electrónico y un dominio de seguimiento de clics. Para obtener ayuda, puedes crear un ticket a través del panel de Braze para iniciar la configuración del nuevo CTD con el equipo de correo electrónico de Braze.

![Interfaz de Braze mostrando el botón "Get Help" debajo del botón "Support" en la barra de navegación superior.]({% image_buster /assets/img/attribution/appsflyer/1.png %})

Es obligatorio crear un nuevo CTD, incluso si ya utilizas uno existente. Esto garantiza que no haya impacto en el tráfico de las Campaigns de correo electrónico actualmente en vivo.

{% alert important%}
AppsFlyer crea el certificado SSL. En esta etapa, es probable que los enlaces de correo electrónico no estén protegidos, lo que significa que el prefijo de la URL es HTTP en lugar de HTTPS. Esto se resuelve en pasos posteriores.
{%endalert%}

## Paso 2 - Crear una plantilla OneLink en AppsFlyer {#step-2-create-a-onelink-template-in-appsflyer}
Crea una [plantilla OneLink](https://support.appsflyer.com/hc/en-us/articles/207032246-Create-a-OneLink-template#procedures) y configura los Universal Links/App Links en "When app is installed". Esta plantilla se utiliza más adelante para crear enlaces OneLink para tus campañas de correo electrónico.

{% alert note%} Si ya tienes una plantilla OneLink existente configurada que habilita Universal Links/App Links, puedes utilizarla.
{%endalert%}

## Paso 3 - Configura tu integración de Braze en AppsFlyer {#step-3-set-up-your-braze-integration-in-appsflyer}
Ahora es el momento de configurar tu integración de Braze en AppsFlyer. Este paso y el siguiente ("Configura tu aplicación") pueden realizarse al mismo tiempo.
Para configurar tu integración de Braze en AppsFlyer:

### 1. En AppsFlyer, desde el menú lateral, selecciona Engage > ESP integration. {#1-in-appsflyer-from-the-side-menu-select-engage-esp-integration}
![Interfaz de AppsFlyer mostrando el botón "ESP Integration" en el menú de navegación.]({% image_buster /assets/img/attribution/appsflyer/2.png %})


### 2. Selecciona Braze. {#2-select-braze}
![Interfaz de AppsFlyer mostrando la lista de integraciones ESP, incluyendo Braze.]({% image_buster /assets/img/attribution/appsflyer/3.png %})


### 3. Selecciona la plantilla OneLink que deseas utilizar para las campañas de correo electrónico y luego haz clic en Next. {#3-select-the-onelink-template-you-want-to-use-for-email-campaigns-then-click-next}
![Interfaz de AppsFlyer mostrando el menú desplegable que permite a los usuarios seleccionar su plantilla.]({% image_buster /assets/img/attribution/appsflyer/4.png %})


### 4. Introduce tu dominio de seguimiento de clics y el valor del "Braze endpoint", proporcionado con el nuevo CTD creado en el paso 1, y luego haz clic en Validate connection. {#4-enter-your-click-tracking-domain-and-braze-endpoint-value-which-was-provided-with-the-new-ctd-created-in-step-1-then-click-validate-connection}

Esto valida que el dominio de seguimiento de clics apunta al endpoint que ingresaste.

![Interfaz de AppsFlyer destacando dónde los clientes deben agregar su dominio de seguimiento de clics y los detalles asociados.]({% image_buster /assets/img/attribution/appsflyer/5.png %})

Con "Braze Endpoint", AppsFlyer solicita los detalles proporcionados por Braze en el paso 1 de esta guía, específicamente el nuevo CTD.

Luego haz clic en **Validate connection**, que valida que el dominio de seguimiento de clics apunta al endpoint que ingresaste.
Cuando hayas terminado, haz clic en **Next**.

### 5. Redirige el tráfico de enlaces a AppsFlyer: {#5-route-link-traffic-to-appsflyer}

#### a. Copia y envía las instrucciones prefabricadas personalizadas de AppsFlyer a tu administrador de TI o de dominio. {#a-copy-and-send-the-customized-pre-fabricated-instructions-in-appsflyer-to-your-it-or-domain-administrator}

Tu administrador debe redirigir el tráfico de tus campañas de correo electrónico desde los servidores del ESP hacia los servidores de AppsFlyer actualizando tus registros DNS CNAME con el nuevo dominio proporcionado por AppsFlyer.

Como resultado, cada vez que se hace clic en un enlace, el clic se redirige a AppsFlyer, que a su vez lo redirige al endpoint del ESP.

![Diagrama que ilustra cómo los datos de clics pasan de tu dominio a AppsFlyer y luego al endpoint de tu ESP.]({% image_buster /assets/img/attribution/appsflyer/6.png %})

#### b. Después de copiar y enviar las instrucciones, haz clic en Done. {#b-after-copying-and-sending-the-instructions-click-done}
Tu integración de Braze ha sido creada.

{%alert important%}
El estado de tu integración de Braze está pendiente y solo comienza a funcionar después de que se mapee el registro CNAME. Puede tardar hasta 24 horas después del mapeo para que una nueva integración comience a funcionar y se active.
{%endalert%}

## Paso 4: Configura tu aplicación (tarea del desarrollador) {#step-4-configure-your-app-developer-task}
Appsflyer [ofrece orientación](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer#step-2-configure-your-app-developer-task) sobre la configuración correcta de la aplicación, que debe seguir tu equipo web o de aplicaciones para admitir la vinculación universal.

## Paso 5: Confirmar que el seguimiento de clics SSL está habilitado con Braze {#step-5-confirm-ssl-click-tracking-is-enabled-with-braze}

En esta etapa, después de compartir y validar los detalles de CTD en AppsFlyer, te recomendamos realizar un envío de prueba para confirmar si tu dominio de envío Onelink tiene un certificado SSL. Esto está en línea con nuestra guía de [configuración de correo electrónico]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate).

Puedes realizar el control de calidad y la solución de problemas enviando un vínculo profundo usando OneLink. Consulta la [documentación de AppsFlyer](https://support.appsflyer.com/hc/en-us/articles/360001437497-Integrating-AppsFlyer-and-Braze#step-3-sending-your-first-email::2ffdb79a) para obtener detalles sobre el uso de OneLink.

Si los enlaces CTD se identifican como HTTP, contacta al equipo de Email Ops de Braze para habilitar el seguimiento de clics SSL. Esto garantiza que todos los enlaces HTTP se conviertan automáticamente a HTTPS.
Puedes usar el siguiente mensaje de ejemplo cuando contactes a tu CSM, o al crear un ticket en el panel de Braze nuevamente, como en el paso 1:

```
Hi Team,
Could you please enable SSL click tracking for CTD XXX? It is currently set to HTTP instead of HTTPS.
```

### URLs de seguimiento de clics de AppsFlyer en Braze (opcional) {#appsflyer-click-tracking-urls-in-braze-optional}

Puedes usar los [enlaces de atribución OneLink](https://support.AppsFlyer.com/hc/en-us/articles/360001294118) de AppsFlyer en Campaigns de Braze a través de push, correo electrónico y más. Esto te permite enviar datos de atribución de instalación o reactivación desde tus Campaigns de Braze a AppsFlyer. Como resultado, puedes medir tus esfuerzos de marketing de manera más eficaz y tomar decisiones basadas en datos.

Simplemente puedes crear tu URL de seguimiento OneLink en AppsFlyer e insertarla directamente en tus Campaigns de Braze. AppsFlyer entonces utiliza sus [metodologías de atribución probabilística](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling) para atribuir al usuario que hizo clic en el enlace. Te recomendamos añadir un identificador de dispositivo a tus enlaces de seguimiento de AppsFlyer para mejorar la precisión de las atribuciones de tus Campaigns de Braze. Esto atribuye de manera determinista al usuario que hizo clic en el enlace.

{% tabs local %}
{% tab Android %}
Para Android, Braze permite a los clientes optar por la [recopilación del ID de publicidad de Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection#optional-google-advertising-id). La integración del SDK de AppsFlyer también recopila el GAID. Puedes incluir el GAID en tus enlaces de seguimiento de clics de AppsFlyer utilizando la siguiente lógica de Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto Braze como AppsFlyer recopilan automáticamente el IDFV de forma nativa a través de nuestras integraciones de SDK. Puedes usar el IDFV como identificador de dispositivo. Puedes incluir el IDFV en tus enlaces de seguimiento de clics de AppsFlyer utilizando la siguiente lógica de Liquid:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}