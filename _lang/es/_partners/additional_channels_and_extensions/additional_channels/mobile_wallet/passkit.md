---
nav_title: PassKit
article_title: PassKit
alias: /partners/passkit/
description: "Este artículo de referencia describe la asociación entre Braze y Passkit. Esta asociación te permite ampliar tu alcance móvil integrando los pases de Apple Wallet y Google Pay en la experiencia de tus clientes."
page_type: partner
search_tag: Partner

---

# PassKit

> PassKit te permite ampliar tu alcance móvil integrando pases de Apple Wallet y Google Pay en la experiencia de tus clientes. Crea, gestiona, distribuye y analiza fácilmente el rendimiento de cupones digitales, tarjetas de fidelización, carnés de socio, entradas y mucho más, sin que tus clientes necesiten otra aplicación.

_Esta integración está mantenida por Passkit._

## Sobre la integración {#about-the-integration}

La integración de Braze y PassKit te permite aumentar y medir la participación de tus campañas en línea mediante la entrega instantánea de pases personalizados de Apple Wallet y Google Pay. A continuación, puedes analizar el uso y realizar ajustes en tiempo real para aumentar el tráfico en la tienda activando mensajes basados en la ubicación y actualizaciones personalizadas y dinámicas en el monedero móvil del cliente.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta PassKit | Debes tener una cuenta PassKit y un director de cuentas PassKit. |
| `userDefinedID` | Para actualizar adecuadamente los eventos personalizados y los atributos personalizados de tus usuarios entre PassKit y Braze, debes establecer el ID externo de Braze como `userDefinedID`. Este `userDefinedID` se utiliza cuando se hacen llamadas a la API a los endpoints de PassKit. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con permisos `users.track`. <br><br> Puede crearse en el panel de Braze desde **Configuración** > **Claves de API**. |
| Endpoint REST or transferencia de estado representacional de Braze  | La URL de tu endpoint REST or transferencia de estado representacional. Tu endpoint dependerá de la [URL de Braze de tu instancia]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Para enriquecer aún más la experiencia de tus clientes con el monedero móvil, desde tu panel de PassKit puedes optar por pasar datos a Braze a través del [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) de Braze.

Ejemplos de datos para compartir desde PassKit incluyen:
- **Pase creado**: cuando un cliente hace clic en un enlace de pase y se le muestra por primera vez un pase.
- **Instalación del pase**: cuando el cliente añade y guarda el pase en su aplicación de monedero.
- **Actualizaciones de pases**: cuando se actualiza un pase.
- **Eliminación del pase**: cuando un cliente elimina el pase de su aplicación de monedero.

Una vez que los datos se pasan a Braze, puedes crear audiencias, personalizar el contenido mediante Liquid y desencadenar Campaigns o Canvas después de que se hayan realizado estas acciones.

## Conectar Passkit a Braze {#connect-passkit-to-braze}

Para pasar datos desde PassKit, asegúrate de que has configurado tu ID externo de Braze como `externalId` de PassKit.

1. Dentro de **Settings**, en **Integrations** en tu proyecto o programa de pases de PassKit, haz clic en **Connect** en la pestaña **Braze**.<br>![El mosaico de integración de Braze en la plataforma PassKit.]({% image_buster /assets/img/passkit/passkit5.png %}){: style="max-width:80%"}<br><br>
2. Introduce tu clave de API de Braze, la URL del endpoint y un nombre para tu conector.<br><br>
3. Activa **Enable Integration** y los eventos que desees en Braze para desencadenar o personalizar tus mensajes.<br>![El mosaico de integración PassKit Braze expandido para aceptar la clave de API, la URL del endpoint, el nombre de la integración, la configuración de habilitación, la configuración de afiliación y la configuración de pase.]({% image_buster /assets/img/passkit/passkit4.png %}){: style="max-width:70%"}

## Crear un pase utilizando un enlace SmartPass {#create-pass-using-a-smartpass-link}

Dentro de Braze, puedes configurar un enlace SmartPass para generar una URL única para que tus clientes instalen su pase en Android o iOS. Para ello, debes definir una carga útil de datos SmartPass cifrada que se pueda llamar desde un bloque de contenido de Braze. Este [bloque de contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) puede reutilizarse para futuros pases y cupones. Lo siguiente se utiliza durante tu integración:

- **URL de PassKit**: Tu URL de PassKit es una URL única para tu programa PassKit.<br>Cada programa tiene una URL única, y puedes encontrarla en la pestaña **Distribution** de tu programa o proyecto PassKit. (por ejemplo, https://pub1.pskt.io/c/ww0jir)<br><br>
- **Secreto de PassKit**: Junto con la URL, debes tener a mano la clave PassKit de este programa.<br>Se encuentra en la misma página que la URL de tu PassKit.<br><br>
- **ID del programa (o proyecto)**: Tu ID del programa PassKit es necesario para crear la URL del SmartPass. <br>Puedes encontrarlo en la pestaña **Settings** de tu proyecto o programa.

Para más información sobre la creación de enlaces SmartPass cifrados, consulta este [artículo de PassKit](https://help.passkit.com/en/articles/3742778-hashed-smartpass-links).

### Paso 1: Define la carga útil de los datos de tu pase {#passkit-integrations}

En primer lugar, debes definir la carga útil del cupón o del miembro.

Hay muchos componentes diferentes que puedes incluir en tu carga útil, pero aquí hay dos importantes a tener en cuenta:

| Componente | Obligatorio | Tipo | Descripción |
| --------- | -------- | ---- | ----------- |
| `person.externalId` | Obligatorio | Cadena | Establecido como el ID externo de Braze, es crucial para que funcionen las devoluciones de llamada de PassKit a Braze, permitiendo a los usuarios de la empresa tener cupones para múltiples ofertas en una Campaign. No se aplica como único. |
| `members.member.externalId` | Opcional | Cadena | Establecido como ID externo de Braze, puedes utilizar tu ID externo para actualizar el pase de socio. La configuración de este campo hace que el usuario sea único dentro del programa de afiliación.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paso 1: Define la carga útil de los datos de tu pase" }

Para obtener una lista completa de los campos disponibles, sus tipos y descripciones útiles, echa un vistazo a la [documentación de PassKit en GitHub](https://github.com/PassKit/smart-pass-link-from-csv-generator).

#### Ejemplo de carga útil {#example-payload}
{% raw %}
```liquid
{
  "members.member.externalId": "{{${user_id}}}",
  "members.member.points": "100",
  "members.tier.name": "current_customer",
  "person.displayName": "{{${first_name}}} {{${last_name}}}",
  "person.externalId": "{{${user_id}}}",
  "universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"
}
```
{% endraw %}

### Paso 2: Crear y codificar una variable de carga útil indefinida {#step-2-create-and-encode-an-undefined-payload-variable}

Para crear y nombrar un nuevo bloque de contenido, ve a **Contenido** > **Bloque de contenido** en el panel de Braze.

Selecciona **Crear bloque de contenido** para empezar.

A continuación, debes definir tu **etiqueta Liquid del bloque de contenido**. Después de guardar este bloque de contenido, se puede hacer referencia a esta etiqueta Liquid al redactar mensajes. En este ejemplo, hemos asignado la etiqueta Liquid como {% raw %}`{{content_blocks.${passKit_SmartPass_url}}}`{% endraw %}.

Dentro de este bloque de contenido, no incluiremos directamente la carga útil, sino que haremos referencia a ella en una variable {% raw %}`{{passData}}`{% endraw %}. El primer fragmento de código que debes añadir a tu bloque de contenido captura una codificación Base64 de la variable {% raw %}`{{passData}}`{% endraw %}.
{% raw %}
```liquid
{% capture base64JsonPayload %}{{passDatapassData|base64_encode}}{% endcapture %}
```
{% endraw %}

### Paso 3: Crea tu firma de cifrado utilizando un hash SHA1 HMAC {#step-3-create-your-encryption-signature-using-a-sha1-hmac-hash}

A continuación, crearás tu firma de cifrado utilizando un hash [SHA1 HMAC](https://en.wikipedia.org/wiki/HMAC) de la URL del proyecto y de la carga útil.

El segundo fragmento de código que debes añadir a tu bloque de contenido captura la URL que se utilizará para el hash.
{% raw %}
```liquid
{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}
```
{% endraw %}

A continuación, debes generar una firma utilizando este hash y tu `Project Secret`. Esto puede hacerse incluyendo un tercer fragmento de código:
{% raw %}
```liquid
{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}
```
{% endraw %}

Por último, añade la firma a la URL completa utilizando el quinto fragmento de código:
{% raw %}
```liquid
{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}{% endcapture %}
```
{% endraw %}

### Paso 4: Imprime tu URL {#step-4-print-your-url}

Por último, asegúrate de llamar a tu URL final para que imprima la URL de tu SmartPass dentro de tu mensaje.
{% raw %}
```liquid
{{longURL}}
```
{% endraw %}

Llegados a este punto, habrás creado un bloque de contenido con el siguiente aspecto:

{% raw %}
```liquid
{% capture base64JsonPayload %}{{passData|base64_encode}}{% endcapture %}

{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}

{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}

{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}&utm_source=braze&utm_campaign={{campaign.${name}}}{% endcapture %}{% capture longURL %}{{longURL | url_encode}}{% endcapture %}

{{longURL}}
```
{% endraw %}

En este ejemplo, se han añadido parámetros UTM para rastrear el origen de estas instalaciones hasta Braze y esta campaña.

{% alert tip %}
Recuerda guardar tu bloque de contenido antes de salir de la página.
{% endalert %}

### Paso 5: Ponerlo todo junto {#step-5-putting-it-all-together}

Una vez creado este bloque de contenido, se puede reutilizar en el futuro.

Puedes observar que hay dos variables sin definir en el bloque de contenido de ejemplo.<br>
{% raw %}`{{passData}}`{% endraw %} - Tu carga útil de datos de pase JSON definida en el [paso 1](#passkit-integrations) <br>
{% raw %}`{{projectUrl}}`{% endraw %} - La URL de tu proyecto o programa que encontrarás en la pestaña de distribución de tu proyecto Passkit.

Esta decisión es intencionada y favorece la reutilización del bloque de contenido. Dado que estas variables solo se referencian, no se crean dentro del bloque de contenido, pueden cambiar sin tener que rehacer el bloque de contenido.

Por ejemplo, quizá quieras cambiar la oferta introductoria para incluir más puntos iniciales en tu programa de fidelización, o quizá quieras crear una tarjeta de socio secundaria o un cupón. Estos escenarios requerirían diferentes `projectURLs` de Passkit o diferentes cargas útiles de pase, que definirías por campaña en Braze.

#### Componer el cuerpo del mensaje {#composing-the-message-body}

Querrás capturar ambas variables en el cuerpo del mensaje y luego llamar a tu bloque de contenido.
Captura la carga útil JSON minificada del [paso 1](#passkit-integrations):

**Asignar la URL del proyecto**
{% raw %}
```liquid
{% assign projectUrl = "https://pub1.pskt.io/c/ww0jir" %}
```
{% endraw %}

**Capturar el JSON**
{% raw %}
```liquid
{% capture passData %}{"members.member.externalId": "{{${user_id}}}","members.member.points": "100","members.tier.name": "current_customer","person.displayName": "{{${first_name}}} {{${last_name}}}","person.externalId": "{{${user_id}}}","universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"}{% endcapture %}
```
{% endraw %}

**Hacer referencia al bloque de contenido que acabas de crear**
{% raw %}
```liquid
{{content_block.${passkit_SmartPass_url}}}
```
{% endraw %}

El cuerpo del mensaje debería verse similar a esto:
![Una imagen del creador de mensajes del bloque de contenido con el JSON capturado y la referencia del bloque de contenido.]({% image_buster /assets/img/passkit/passkit1.png %}){: style="max-width:70%"}

La URL de salida de ejemplo es:
![La URL de salida que incluye una larga cadena de letras y números generada aleatoriamente.]({% image_buster /assets/img/passkit/passkit2.png %}){: style="max-width:70%"}

La URL de salida será larga. La razón es que contiene todos los datos del pase e incorpora seguridad de primer nivel para garantizar la integridad de los datos y que no se alteren mediante la modificación de la URL. Si utilizas servicio de mensajes cortos para distribuir esta URL, tal vez quieras pasarla por un proceso de acortamiento de enlaces como [bit.ly](https://dev.bitly.com/v4/#operation/createFullBitlink). Esto puede hacerse mediante una llamada de contenido conectado a un endpoint de bit.ly.

## Actualizar el pase utilizando el webhook de PassKit {#update-pass-using-the-passkit-webhook}

Dentro de Braze, puedes configurar una campaña de webhook o un webhook dentro de un Canvas para actualizar un pase existente basado en el comportamiento de tu usuario. Consulta los siguientes enlaces para obtener información sobre endpoints útiles de PassKit.
- [Proyectos de miembros](https://docs.passkit.io/protocols/member/)
- [Proyectos de cupones](https://docs.passkit.io/protocols/coupon/)
- [Proyectos de vuelos](https://docs.passkit.io/protocols/boarding/)

### Parámetros de la carga útil {#payload-parameters}

Antes de empezar, aquí están los parámetros de carga útil JSON comunes que puedes incluir dentro de tus webhooks de creación y actualización a PassKit.

| Datos | Tipo | Descripción |
| ---- | ---- | ----------- |
| `externalId` | Cadena | Permite añadir un ID único al registro de pases para proporcionar compatibilidad con un sistema existente que utilice identificadores de cliente únicos (por ejemplo, números de socio). Puedes recuperar los datos del pase utilizando este endpoint a través de `userDefinedId` y `campaignName` en lugar del ID del pase. Este valor debe ser único dentro de una campaña y, una vez establecido, no puede modificarse.<br><br>Para la integración con Braze, te recomendamos que utilices el ID externo de Braze: {% raw %}`{{${user_id}}}`{% endraw %} |
| `campaignId` (cupón) <br><br> `programId` (afiliación) | Cadena | El ID de la plantilla de campaña o programa que creaste en PassKit. Para encontrarlo, dirígete a la pestaña **Settings** de tu proyecto de pases de PassKit. |
| `expiryDate` | IO8601 fecha y hora | La fecha de caducidad del pase. Después de la fecha de caducidad, el pase se anula automáticamente (consulta `isVoided`). Este valor anulará el valor de la plantilla y de la fecha de finalización de la campaña. |
| `status` | Cadena | El estado actual de un cupón, como `REDEEMED` o `UNREDEEMED`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Parámetros de la carga útil" }

### Paso 1: Crea tu plantilla de webhook de Braze {#step-1-create-your-braze-webhook-template}

Para crear una plantilla de webhook de PassKit y utilizarla en futuras campañas o Canvas, ve a la sección **Plantillas y medios** en el panel de Braze. Si deseas crear una campaña de webhook de PassKit única o utilizar una plantilla existente, selecciona **Webhook** en Braze al crear una nueva campaña.

Una vez que hayas seleccionado la plantilla de webhook de PassKit, deberías ver lo siguiente:
- **URL del webhook**: `https://api-pub1.passkit.io/coupon/singleUse/coupon`
- **Cuerpo de la solicitud**: Texto sin procesar

#### Encabezados de solicitud y método {#request-headers-and-method}

PassKit requiere un `HTTP Header` para la autorización que incluya tu clave de API de PassKit codificada en base 64. Lo siguiente ya estará incluido dentro de la plantilla como un par clave-valor, pero en la pestaña **Settings**, debes sustituir el `<PASSKIT_LONG_LIVED_TOKEN>` por tu token de PassKit. Para recuperar tu token, ve a tu proyecto/programa de PassKit, navega a **Settings > Integrations > Long Lived Token**.

{% raw %}
- **Método HTTP**: PUT
- **Encabezado de solicitud**:
  - **Authorization**: Bearer `<PASSKIT_LONG_LIVED_TOKEN>`
  - **Content-Type**: application/json
{% endraw %}

#### Cuerpo de la solicitud {#request-body}

Para configurar el webhook, rellena los detalles del nuevo evento en el cuerpo de la solicitud, incluidos los parámetros de carga útil necesarios para tu caso de uso:

```json
{% raw %}{
  "externalId": "{{${user_id}}}",
  "campaignId": " 2xa1lRy8dBz4eEElBfmIz8",
  "expiryDate": "2020-05-10T00:00:00Z"
}{% endraw %}
```

### Paso 2: Previsualiza tu solicitud {#step-2-preview-your-request}

El texto en bruto se resaltará automáticamente si se trata de una etiqueta de Braze aplicable.

Previsualiza tu solicitud en el panel de **Vista previa** o navega a la pestaña **Test**, donde puedes seleccionar un usuario al azar, un usuario existente o personalizar el tuyo propio para probar tu webhook.

{% alert important %}
Recuerda guardar tu plantilla antes de salir de la página. <br>Las plantillas de webhook actualizadas pueden encontrarse en la lista **Plantillas de webhook guardadas** al crear una nueva [campaña de webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook).
{% endalert %}

## Recuperar detalles del pase a través de contenido conectado {#retrieve-pass-details-via-connected-content}

Además de crear y actualizar pases, también puedes recuperar los metadatos de los pases de tus usuarios mediante el [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call) de Braze para incorporar detalles personalizados de los pases en tus campañas de mensajería.

**Llamada al contenido conectado de PassKit**

{% raw %}
```liquid
{% connected_content  https://api-pub1.passkit.io/coupon/singleUse/coupon/externalId/{{${user_id}}} :headers {"Authorization": "Bearer <PASSKIT_LONG_LIVED_TOKEN>","Content-Type": "application/json"} :save passes %}

{{passes.status}}
```
{% endraw %}

**Ejemplo de respuestas de Liquid**

{% tabs local %}
{% tab passes redemptionDetails %}

```json
{
    "redemptionDate": null,
    "redemptionCode": "",
    "lat": 0,
    "lon": 0,
    "alt": 0,
    "redemptionSource": "",
    "redemptionReference": "",
    "transactionReference": "",
    "transactionAmount": 0
}
```

{% endtab %}
{% tab passes status %}
```
UNREDEEMED
```
{% endtab %}
{% endtabs %}