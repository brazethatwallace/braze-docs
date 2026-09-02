---
nav_title: Etiquetas de personalización compatibles
article_title: Etiquetas de personalización de Liquid compatibles
page_order: 1
description: "Este artículo de referencia cubre una lista completa de las etiquetas de personalización de Liquid compatibles."
search_rank: 1
---

# Etiquetas de personalización compatibles {#supported-personalization-tags}

> Este artículo de referencia cubre una lista completa de las etiquetas de personalización de Liquid compatibles.

## Resumen de etiquetas compatibles {#summary-of-supported-tags}

A modo de referencia, se proporciona un resumen de las etiquetas de personalización compatibles. Para obtener más detalles sobre cada tipo de etiqueta y las mejores prácticas, continúa leyendo.

{% raw %}

| Tipo de etiqueta de personalización | Etiquetas |
| -------------  | ---- |
| Atributos estándar (predeterminados) | `{{${city}}}` <br> `{{${country}}}` <br> `{{${date_of_birth}}}` <br> `{{${email_address}}}` <br> `{{${first_name}}}` <br> `{{${gender}}}` <br> `{{${language}}}` <br> `{{${last_name}}}` <br> `{{${last_used_app_date}}}` <br> `{{${most_recent_app_version}}}` <br> `{{${most_recent_locale}}}` <br> `{{${most_recent_location}}}` <br> `{{${phone_number}}}` <br> `{{${time_zone}}}` <br> `{{${user_id}}}` <br> `{{${braze_id}}}` <br> `{{${random_bucket_number}}}` <br> `{{subscribed_state.${email_global}}}` <br> `{{subscribed_state.${subscription_group_id}}}` |
| Atributos de dispositivo | `{{most_recently_used_device.${carrier}}}` <br> `{{most_recently_used_device.${id}}}` <br> `{{most_recently_used_device.${idfa}}}` <br> `{{most_recently_used_device.${model}}}` <br> `{{most_recently_used_device.${os}}}` <br> `{{most_recently_used_device.${platform}}}` <br> `{{most_recently_used_device.${google_ad_id}}}` <br> `{{most_recently_used_device.${roku_ad_id}}}` <br> `{{most_recently_used_device.${foreground_push_enabled}}}`|
| <a href='/docs/user_guide/channels/email/subscriptions#changing-email-subscriptions'>Atributos de lista de correo electrónico</a> | `{{${set_user_to_unsubscribed_url}}}` <br>Esta etiqueta reemplaza la etiqueta anterior `{{${unsubscribe_url}}}`. Aunque la etiqueta anterior aún funciona en correos electrónicos creados previamente, te recomendamos que uses la etiqueta más reciente en su lugar. <br><br> `{{${set_user_to_one_click_list_unsubscribe}}}` <br> `{{${set_user_to_subscribed_url}}}` <br> `{{${set_user_to_opted_in_url}}}` |
| <a href='/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting#trigger-messages'>Atributos de servicio de mensajes cortos</a> | `{{sms.${inbound_message_body}}}` <br> `{{sms.${inbound_media_urls}}}` |
| <a href='/docs/user_guide/channels/whatsapp/message_processing/messaging_users'>Atributos de WhatsApp</a> | `{{whats_app.${inbound_message_body}}}` <br> `{{whats_app.${inbound_media_urls}}}` <br> `{{whats_app.${inbound_flow_response}}}` <br> `{{whats_app.${inbound_product_id}}}` <br> `{{whats_app.${inbound_catalog_id}}}` <br> `{{whats_app.${inbound_profile_name}}}` |
| Atributos de Campaign y de paso en Canvas | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| Atributos de Canvas | `{{canvas.${name}}}` <br> `{{canvas.${api_id}}}` <br> `{{canvas.${variant_name}}}` <br> `{{canvas.${variant_api_id}}}` |
| Atributos de tarjeta | `{{card.${api_id}}}` <br> `{{card.${name}}}` |
| Eventos de geovallado | `{{event_properties.${geofence_name}}}` <br> `{{event_properties.${geofence_set_name}}}` |
| Propiedades del evento <br> (Son personalizadas para tu espacio de trabajo.) | `{{event_properties.${your_custom_event_property}}}` |
| Variables de contexto de Canvas | `{{context.${your_context_variable}}}` |
| Atributos personalizados <br> (Son personalizados para tu espacio de trabajo.) | `{{custom_attribute.${your_custom_attribute}}}` |
| <a href='/docs/api/objects_filters/trigger_properties_object'>Propiedades de desencadenamiento de API</a> | `{{api_trigger_properties.${your_api_trigger_property}}}` |
| Propiedades de entrada de Canvas | `{{context.${property_name}}}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Resumen de etiquetas compatibles" }

{% endraw %}

{% alert note %}
Las propiedades de desencadenamiento de API deben usar dos llaves por etiqueta: {% raw %}`{{api_trigger_properties.${your_api_trigger_property}}}`. Las llaves triples (por ejemplo, `{{{...}}}`){% endraw %} no son una sintaxis de personalización válida en Braze. Consulta [¿Por qué mi Liquid desencadenado por API falla en Braze?]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/faq#why-is-my-api-triggered-liquid-failing-in-braze).
{% endalert %}

### Atributos compatibles {#supported-attributes}

Los atributos de Campaign, tarjeta y Canvas solo son compatibles en sus plantillas de mensajería correspondientes. Por ejemplo, `dispatch_id` es compatible con Liquid para canales de mensajería como correo electrónico, push, servicio de mensajes cortos y WhatsApp, pero no para mensajes dentro de la aplicación ni Banners.

Consulta [Atributos de Campaign y Canvas en distintas fuentes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/campaign_and_canvas_attributes_across_sources) para obtener más detalles.

### Diferencias entre etiquetas de Canvas y Campaign {#canvas-and-campaign-tag-differences}

El comportamiento de las siguientes etiquetas difiere entre Canvas y Campaigns:
{% raw %}
- El comportamiento de `dispatch_id` difiere porque Braze trata los pasos de Canvas como eventos desencadenados, incluso cuando están "programados" (excepto los pasos de entrada, que pueden programarse). Para más información, consulta [Comportamiento de dispatch ID]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id).
- Usar la etiqueta `{{campaign.${name}}}` con Canvas muestra el nombre del componente de Canvas. Cuando se usa esta etiqueta con Campaigns, muestra el nombre de la campaña.
{% endraw %}

#### Nombres de Campaign en URLs {#campaign-names-in-urls}

{% raw %}
Los nombres de Campaign y de variantes de mensaje pueden incluir caracteres que no son seguros para URLs, como `%`, espacios o `&`. Cuando insertes `{{campaign.${name}}}` o `{{campaign.${message_name}}}` en un enlace o cadena de consulta, como un parámetro `utm_campaign`, aplica el filtro [`url_encode`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#url-filters) para que la URL se analice correctamente. Por ejemplo:

```liquid
https://example.com/?utm_campaign={{ campaign.${name} | url_encode }}
```
{% endraw %}

## Información del dispositivo utilizado más recientemente {#most-recently-used-device-information}

Puedes usar como plantilla los siguientes atributos del dispositivo más reciente del usuario en todas las plataformas. Si un usuario no ha utilizado tu aplicación (por ejemplo, si importaste al usuario a través de la REST or transferencia de estado representacional API), todos estos valores serán `null`.

{% raw %}

|Etiqueta | Descripción |
|---|---|
|`{{most_recently_used_device.${browser}}}` | El navegador utilizado más recientemente en el dispositivo del usuario. Algunos ejemplos son "Chrome" y "Safari". |
|`{{most_recently_used_device.${id}}}` | El identificador de dispositivo de Braze. En iOS, puede ser el identificador de proveedor de Apple (IDFV) o un UUID. Para Android y otras plataformas, es un UUID generado aleatoriamente. |
| `{{most_recently_used_device.${carrier}}}` | El operador de servicio telefónico del dispositivo utilizado más recientemente, si está disponible. Algunos ejemplos son "Verizon" y "Orange". |
| `{{most_recently_used_device.${ad_tracking_enabled}}}` | Si el dispositivo tiene habilitado el seguimiento de anuncios o no. Es un valor booleano (`true` o `false`). |
| `{{most_recently_used_device.${idfa}}}` | Para dispositivos iOS, este valor es el identificador de publicidad (IDFA) si tu aplicación está configurada con nuestra [recopilación opcional de IDFA]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection). Para dispositivos que no son iOS, este valor es null. |
| `{{most_recently_used_device.${google_ad_id}}}` | Para dispositivos Android, este valor es el identificador de publicidad de Google Play si tu aplicación está configurada con nuestra recopilación opcional del ID de publicidad de Google Play. Para dispositivos que no son Android, este valor es null. |
| `{{most_recently_used_device.${roku_ad_id}}}` | Para dispositivos Roku, este valor es el identificador de publicidad de Roku que se recopila cuando tu aplicación está configurada con Braze. Para dispositivos que no son Roku, este valor es null. |
| `{{most_recently_used_device.${model}}}` | El nombre del modelo del dispositivo, si está disponible. Algunos ejemplos son "iPhone 6S", "Nexus 6P" y "Firefox". |
| `{{most_recently_used_device.${os}}}` | El sistema operativo del dispositivo, si está disponible. Algunos ejemplos son "iOS 9.2.1", "Android (Lollipop)" y "Windows". |
| `{{most_recently_used_device.${platform}}}` | La plataforma del dispositivo, si está disponible. Si está configurada, el valor es uno de `ios`, `android`, `kindle`, `android_china`, `web` o `tvos`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Información del dispositivo utilizado más recientemente" }

Dado que existe una amplia variedad de operadores de dispositivos, nombres de modelos y sistemas operativos, te recomendamos que pruebes a fondo cualquier Liquid que dependa condicionalmente de alguno de esos valores. Estos valores son `null` si no están disponibles en un dispositivo en particular.

## Información de la aplicación segmentada {#targeted-app-information}

Para los mensajes dentro de la aplicación, puedes utilizar los siguientes atributos de la aplicación dentro de Liquid. Los valores se basan en la clave de API de SDK or kit de desarrollo de software que tus aplicaciones utilizan para solicitar mensajería.

|Etiqueta | Descripción |
|------------------|---|
| `{{app.${api_id}}}` | La clave de API de la aplicación que solicita el mensaje. Por ejemplo, puedes usar esta clave junto con `abort_message()` de Liquid para evitar el envío de mensajes dentro de la aplicación a ciertas aplicaciones, como plataformas de TV o compilaciones de desarrollo que utilizan una clave de API de SDK or kit de desarrollo de software independiente.|
| `{{app.${name}}}` | El nombre de la aplicación (tal como se define en el panel de Braze) que solicita el mensaje. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Información de la aplicación segmentada" }

Por ejemplo, este código Liquid cancela un mensaje si las aplicaciones solicitantes no son una de las dos claves de API de la lista:

```liquid
{% assign allowed_api_keys = 'sdk_api_key_1,sdk_api_key_2' | split: ',' %}
{% if allowed_api_keys contains {{app.${api_id}}} %}
User is in list of apps
{% else %}
{% abort_message("User not in list of apps") %}
{% endif %}
```

## Información del dispositivo objetivo {#targeted-device-information}

Para notificaciones push, mensajes dentro de la aplicación y Banners, puedes incluir mediante plantillas los siguientes atributos del dispositivo que recibe el mensaje. Una notificación push, un mensaje dentro de la aplicación o un Banner puede incluir atributos del dispositivo en el que el usuario lee el mensaje. Estos atributos no funcionan para Content Cards ni correos electrónicos. En el caso de los correos electrónicos, los mensajes se renderizan antes de enviarse, por lo que el dispositivo en el que el usuario abre el correo electrónico es desconocido en ese momento.

| Etiqueta | Descripción |
|------------------|---|
| `{{targeted_device.${id}}}` | Este es el identificador de dispositivo de Braze. En iOS, puede ser el Apple Identifier for Vendor (IDFV) o un UUID. Para Android y otras plataformas, es un UUID generado aleatoriamente. Por ejemplo, si un usuario tiene cinco dispositivos, se produce un intento de envío para los cinco dispositivos, cada uno utilizando el identificador de dispositivo correspondiente. Si un mensaje está configurado para enviarse al dispositivo usado más recientemente por el usuario, solo se produce un intento de envío al dispositivo usado más recientemente identificado a través de Braze. |
| `{{targeted_device.${carrier}}}` | El operador de servicio telefónico del dispositivo usado más recientemente, si está disponible. Ejemplos incluyen "Verizon" y "Orange". |
| `{{targeted_device.${idfa}}}` | Para dispositivos iOS, este valor es el Identifier for Advertising (IDFA) si tu aplicación está configurada con nuestra [recopilación opcional de IDFA]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection). Para dispositivos que no son iOS, este valor es nulo. |
| `{{targeted_device.${google_ad_id}}}` | Para dispositivos Android, este valor es el Google Play Advertising Identifier si tu aplicación está configurada con nuestra [recopilación opcional del Google Play Advertising ID]. Para dispositivos que no son Android, este valor es nulo. |
| `{{targeted_device.${roku_ad_id}}}` | Para dispositivos Roku, este valor es el Roku Advertising Identifier que se recopila cuando tu aplicación está configurada con Braze. Para dispositivos que no son Roku, este valor es nulo. |
| `{{targeted_device.${model}}}` | El nombre del modelo del dispositivo, si está disponible. Ejemplos incluyen "iPhone 6S", "Nexus 6P" y "Firefox". |
| `{{targeted_device.${os}}}` | El sistema operativo del dispositivo, si está disponible. Ejemplos incluyen "iOS 9.2.1", "Android (Lollipop)" y "Windows". |
| `{{targeted_device.${platform}}}` | La plataforma del dispositivo, si está disponible. Si está configurada, el valor es uno de `ios`, `android`, `kindle`, `android_china`, `web` o `tvos`. También puedes usar la etiqueta de personalización `most_recently_used_device`. |
| `{{targeted_device.${foreground_push_enabled}}}` | Este valor es `true` cuando el dispositivo objetivo tiene habilitado el push en primer plano, `false` en caso contrario. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Información del dispositivo objetivo" }

{% endraw %}

Dado que existe una amplia variedad de operadores de dispositivos, nombres de modelos y sistemas operativos, te aconsejamos que pruebes exhaustivamente cualquier lógica que dependa condicionalmente de cualquiera de esos valores. Estos valores son `null` si no están disponibles en un dispositivo en particular.

Además, para las notificaciones push, es posible que Braze no pueda determinar el dispositivo asociado a la notificación push en ciertas circunstancias, como cuando el token de notificaciones push fue importado a través de la API, lo que resulta en valores `null` para esos mensajes.

![Ejemplo de uso de un valor predeterminado de "there" al utilizar una variable de nombre en un mensaje push.]({% image_buster /assets/img_archive/personalized_firstname_.png %})

### Uso de lógica condicional en lugar de un valor predeterminado {#using-conditional-logic-instead-of-a-default-value}

En algunas circunstancias, puedes optar por usar [lógica condicional]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic) en lugar de establecer un valor predeterminado. La lógica condicional te permite enviar mensajes que difieren según el valor de un atributo personalizado. Además, puedes usar lógica condicional para [cancelar mensajes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) a clientes con valores de atributos nulos o en blanco.

#### Ejemplo {#use-case}

Por ejemplo, supongamos que estás enviando una notificación de saldo de recompensas a los clientes. No hay una buena manera de tener en cuenta a los clientes con saldos bajos y nulos usando valores predeterminados.

En este caso, hay dos opciones que pueden funcionar mejor que establecer un valor predeterminado:

1. Cancelar el mensaje para clientes con saldos bajos, nulos y en blanco.

{% raw %}

   ```liquid
   {% if {{custom_attribute.${balance}}} > 0 %}
   Your rewards balance is {{custom_attribute.${balance}}}
   {% else %}
   {% abort_message() %}
   {% endif %}
   ```

{% endraw %}

2. Enviar un mensaje completamente diferente a estos clientes, como:

{% raw %}

   ```liquid
   {% if ${first_name} != blank and ${first_name} != null %}
   Hello {{${first_name} | default: 'there'}}, thanks for downloading!
   {% else %}
   Thanks for downloading!
   {% endif %}
   ```

En este ejemplo, un usuario con un nombre en blanco o nulo recibe el mensaje "Thanks for downloading". Deberías incluir un [valor predeterminado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) para el nombre para asegurarte de que tu cliente no vea Liquid en caso de un error.

{% endraw %}

## Etiquetas de variable {#variable-tags}

Puedes usar la etiqueta `assign` para crear una variable en el creador de mensajes. Te recomendamos usar un nombre único para tu variable. Si creas una variable con un nombre similar al de las etiquetas de personalización compatibles (como `language`), esto puede afectar tu lógica de mensajería.

Después de crear una variable, puedes hacer referencia a ella en tu lógica de mensajería o mensaje. Esta etiqueta es útil cuando quieres reformatear contenido que se devuelve desde nuestra característica de [contenido conectado]({% image_buster /assets/img_archive/personalized_firstname_.png %}). Puedes leer más en la documentación de Shopify sobre [etiquetas de variable](https://docs.shopify.com/themes/liquid/tags/variable-tags).

{% alert important %}
Las cadenas envueltas en comillas simples dentro de una etiqueta `assign` se tratan como cadenas literales. Las etiquetas de personalización de Liquid dentro de comillas simples no se interpolan. Por ejemplo:

{% raw %}
```liquid
{% assign name_intro = 'My name is {{${first_name}}}' %}
{{ name_intro }}
```
{% endraw %}

Esto genera el texto literal {% raw %}`My name is {{${first_name}}}`{% endraw %} en lugar del nombre del usuario.

Para incluir personalización, usa variables o concatena cadenas con el filtro [`append`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters#string-filters). Para la creación de plantillas de URL con personalización, consulta [plantillas de enlace]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template).
{% endalert %}

{% alert tip %}
¿Te encuentras asignando las mismas variables en cada mensaje? En lugar de escribir la etiqueta `assign` una y otra vez, puedes guardar esa etiqueta como un bloque de contenido y colocarla en la parte superior de tu mensaje.

1. [Crea un bloque de contenido]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks#create-a-content-block).
2. Dale un nombre a tu bloque de contenido (sin espacios ni caracteres especiales).
3. Selecciona **Editar** en la parte inferior de la página.
4. Escribe tus etiquetas `assign`.

Siempre que el bloque de contenido esté en la parte superior de tu mensaje, cada vez que la variable se inserte en tu mensaje como un objeto, hará referencia a tu atributo personalizado elegido.
{% endalert %}

### Ejemplo

Supongamos que permites a tus clientes canjear sus puntos de recompensas por premios después de acumular 100 puntos de recompensas. Entonces, solo quieres enviar mensajes a los clientes que tendrían un saldo de puntos mayor o igual a 100 si realizaran esa compra adicional:

{% raw %}
```liquid
{% assign new_points_balance = {{custom_attribute.${current_rewards_balance} | plus: 50}} %}
{% if new_points_balance >= 100 %}
Make a purchase to bring your rewards points to {{new_points_balance}} and cash in today!
{% else %}
{% abort_message('not enough points') %}
{% endif %}
```
{% endraw %}

## Etiquetas de iteración {#iteration-tags}

{% raw %}
Las etiquetas de iteración se pueden usar para ejecutar un bloque de código de forma repetida. El ejemplo a continuación presenta la etiqueta `for`.

### Ejemplo

Supongamos que tienes una oferta en zapatillas Nike y quieres enviar un mensaje a los clientes que han expresado interés en Nike. Tienes un array de marcas de productos visualizadas en el perfil de cada cliente. Este array podría contener hasta 25 marcas de productos, pero solo quieres enviar un mensaje a los clientes que vieron un producto Nike como una de sus 5 visualizaciones de productos más recientes.

```liquid
{% for items in {{custom_attribute.${Brands Viewed}}} limit:5 %}
{% if {{items}} contains 'Converse' %}
{% assign converse_viewer = true %}
{% endif %}
{% endfor %}
{% if converse_viewer == true %}
Sale on Converse!
{% else %}
{% abort_message() %}
{% endif %}
```

En este ejemplo, verificamos los primeros cinco elementos en el array de marcas de zapatillas visualizadas. Si uno de esos elementos es Converse, creamos la variable `converse_viewer` y la establecemos como verdadera.

Luego, enviamos el mensaje de oferta cuando `converse_viewer` es verdadera. De lo contrario, abortamos el mensaje.

Este es un ejemplo sencillo de cómo se pueden usar las etiquetas de iteración en el creador de mensajes de Braze. Puedes encontrar más información en la documentación de Shopify sobre [etiquetas de iteración](https://docs.shopify.com/themes/liquid/tags/iteration-tags).

## Etiquetas de sintaxis {#syntax-tags}

Las etiquetas de sintaxis se pueden usar para controlar cómo se renderiza Liquid. Puedes usar la etiqueta `echo` para devolver una expresión. Esto es lo mismo que envolver una expresión usando llaves, excepto que puedes usar esta etiqueta dentro de etiquetas de Liquid. También puedes usar la etiqueta `liquid` para tener un bloque de Liquid sin delimitadores en cada etiqueta. Cada etiqueta debe estar en su propia línea cuando uses la etiqueta `liquid`. Consulta la documentación de Shopify sobre [etiquetas de sintaxis](https://shopify.dev/api/liquid/tags#syntax-tags) para obtener más información y ejemplos.

Con el [control de espacios en blanco](https://shopify.github.io/liquid/basics/whitespace/), puedes eliminar los espacios en blanco alrededor de tus etiquetas, lo que te ayuda a controlar aún más el aspecto de la salida de Liquid.

## Códigos de estado HTTP {#http-personalization}

Puedes utilizar el estado HTTP de una llamada de [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) guardándolo primero como una variable local y luego usando la clave `__http_status_code__`. Por ejemplo:

```html
{% connected_content https://example.com/api/endpoint :save connected %}
{% if connected.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert note %}
Esta clave solo se agrega automáticamente al objeto de contenido conectado si el endpoint devuelve un objeto JSON. Si el endpoint devuelve un array u otro tipo, esa clave no se puede establecer automáticamente en la respuesta.
{% endalert %}

## Enviar mensajes según el idioma, la configuración regional más reciente y la zona horaria {#send-messages-based-on-language-most-recent-locale-and-time-zone}

En algunas situaciones, es posible que desees enviar mensajes específicos para configuraciones regionales particulares. Por ejemplo, el portugués brasileño suele ser diferente del portugués europeo.

### Ejemplo: Localizar según la configuración regional más reciente {#use-case-localize-based-on-recent-locale}

Aquí tienes un ejemplo de cómo puedes usar la configuración regional más reciente para localizar aún más un mensaje internacionalizado.

{% raw %}

```liquid
{% if ${language} == 'en' %}
Message in English
{% elsif  ${language} == 'fr' %}
Message in French
{% elsif  ${language} == 'ja' %}
Message in Japanese
{% elsif  ${language} == 'ko' %}
Message in Korean
{% elsif  ${language} == 'ru' %}
Message in Russian
{% elsif ${most_recent_locale} == 'pt_BR' %}
Message in Brazilian Portuguese
{% elsif ${most_recent_locale} == 'pt_PT' %}
Message in European Portuguese
{% elsif  ${language} == 'pt' %}
Message in default Portuguese
{% else %}
Message in default language
{% endif %}
```

En este ejemplo, los clientes con una configuración regional más reciente de `pt_BR` reciben un mensaje en portugués brasileño, y los clientes con una configuración regional más reciente de `pt_PT` reciben un mensaje en portugués europeo. Los clientes que no cumplen las dos primeras condiciones pero tienen su idioma configurado en portugués reciben un mensaje en el tipo de portugués predeterminado que tú elijas.

### Ejemplo: Segmentar usuarios por zona horaria {#use-case-target-users-by-time-zone}

También puedes segmentar usuarios por su zona horaria. Por ejemplo, enviar un mensaje si se encuentran en EST y otro si están en PST. Para hacer esto, guarda la hora actual en UTC y compara una declaración if/else con la hora actual del usuario para enviar el mensaje correcto en la zona horaria correcta. Debes configurar la Campaign para que se envíe en la zona horaria local del usuario, de modo que reciba la Campaign en el momento adecuado.

Consulta el siguiente ejemplo para saber cómo escribir un mensaje que se entregue entre las 2 pm y las 3 pm con un mensaje específico para cada zona horaria.

```liquid
{% assign hour_in_utc = 'now' | date: '%H' | plus:0 %}
{% if hour_in_utc >= 19 && hour_in_utc < 20 %}
It is between 2:00:00 pm and 2:59:59 pm ET!
{% elsif hour_in_utc >= 22 && hour_in_utc < 23 %}
It is between 2:00:00 pm and 2:59:59 pm PT!
{% else %}
{% abort_message %}
{% endif %}
```

{% endraw %}

## Enviar mensajes con un número aleatorio {#send-messages-with-a-random-number}

{% raw %}
La etiqueta `{% random %}` devuelve un número aleatorio. Puedes usarla para lógica de estilo A/B, muestreo o variar el contenido de los mensajes.

| Etiqueta | Descripción |
|-------|--------------|
| `{% random %}` | Un flotante entre 0 y 1 (inclusive de 0, exclusive de 1). |
| `{% random 10 %}` (argumento entero) | Un entero que va desde 0 hasta, pero sin incluir, el entero especificado. Por ejemplo, `{% random 10 %}` devuelve un entero de 0 a 9. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Enviar mensajes con un número aleatorio" }

{% endraw %}

### Ejemplo: Enviar variantes aleatorias a los usuarios {#use-case-send-users-random-variants}

{% raw %}
```liquid
{% capture roll_str %}{% random %}{% endcapture %}
{% assign roll = roll_str | plus: 0 %}
{% if roll < 0.5 %}
Show variant A
{% else %}
Show variant B
{% endif %}
```
{% endraw %}

## Etiqueta de carrito de compras de comercio electrónico {#shopping-cart-tag}

La etiqueta `shopping_cart` accede al contenido del carrito de un usuario en los casos de uso de Canvas de comercio electrónico de [carrito abandonado]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases?tab=abandoned%20cart#abandoned-cart) y [pago abandonado]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases?tab=abandoned%20checkout#abandoned-checkout). Reemplaza `CART_ID` con el valor real del ID del carrito, como {% raw %}`{{context.${cart_id}}}`{% endraw %}.

{% raw %}
```liquid
{% shopping_cart CART_ID :abort_if_not_abandoned false %}
```
{% endraw %}

El parámetro `abort_if_not_abandoned` en este ejemplo se aplica solo al caso de uso de [pago abandonado]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases?tab=abandoned%20checkout#abandoned-checkout) cuando se usa con el evento `ecommerce.checkout_started`. No es aplicable a los casos de uso de carrito abandonado. Para más detalles, consulta [`abort_if_not_abandoned`]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases?tab=abandoned%20checkout#abort-if-not-abandoned).

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags