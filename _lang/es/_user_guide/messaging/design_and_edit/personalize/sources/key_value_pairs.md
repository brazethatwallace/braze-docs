---
nav_title: Pares clave-valor
article_title: Pares clave-valor
page_order: 4
description: "Este artículo de referencia cubre los pares clave-valor y cómo usarlos para enviar cargas útiles de datos adicionales a los dispositivos de los usuarios."
channel:
  - push
  - in-app messages
  - content cards

---

# Pares clave-valor {#key-value-pairs}

> Esta página cubre cómo usar pares clave-valor para enviar cargas útiles de datos adicionales a los dispositivos de los usuarios. Esta característica está disponible en los canales de mensajería push, dentro de la aplicación, correo electrónico y Content Cards.

Usa pares clave-valor para agregar metadatos estructurados a los mensajes. Estas cargas útiles de datos adicionales pueden enriquecer los mensajes con información contextual adicional que puede influir en cómo se renderiza o procesa un mensaje.

Dado que los pares clave-valor son metadatos, estos datos no son necesariamente visibles para el destinatario, pero pueden ser utilizados por tus sistemas o procesos conectados para personalizar el manejo de mensajes.

Cada par consiste en:

- **Clave:** El identificador (Ejemplo: `utm_source`)
- **Valor:** Los datos asociados (Ejemplo: `newsletter`)

## Ejemplos {#use-cases}

Estos son algunos ejemplos para añadir metadatos con pares clave-valor:

1. **Parámetros de seguimiento:** Adjuntar parámetros UTM con fines de análisis
   - Clave: `utm_campaign`
   - Valor: `spring_sale`
2. **Etiquetas personalizadas:** Añadir etiquetas para enrutamiento interno o categorización
   - Clave: `priority`
   - Valor: `high`
3. **Desencadenantes de comportamiento:** Metadatos utilizados para desencadenar o personalizar comportamientos dentro de la aplicación
   - Clave: `deep_link`
   - Valor: `app://promo-page`

## Notificaciones push {#push-notifications}

Los pares clave-valor pueden añadirse a las notificaciones push de Android, iOS y web. Puedes utilizar pares clave-valor para actualizar métricas internas y contenido de la aplicación, o personalizar las propiedades de las notificaciones push, como la priorización de alertas, la localización y los sonidos.

En el creador de mensajes, selecciona la pestaña **Configuración**, selecciona **Añadir nuevo par** y especifica tus pares clave-valor.

Cuando añades pares clave-valor en el creador de mensajes, los valores se envían como cadenas. Para notificaciones push de iOS, las claves de alerta reservadas del servicio de notificaciones push de Apple (APN) que añadas a través de **Opciones de alerta** (como `loc-args` para argumentos de localización) se formatean con los tipos JSON correctos en la carga útil. Para claves personalizadas, tu aplicación recibe valores de cadena a menos que los analices en tu integración.

### iOS

El servicio de notificaciones push de Apple (APN) admite la configuración de preferencias de alerta y el envío de datos personalizados mediante pares clave-valor. APN utiliza la biblioteca reservada de Apple `aps`, que incluye claves y valores predeterminados que controlan las propiedades de las alertas.

#### Biblioteca APS {#aps-library}

| Clave  | Tipo de valor  | Descripción del valor |
|-------------------|-----------------------------|----------------------------------|
| alert             | cadena u objeto de diccionario | Para entradas de cadena, muestra una alerta con la cadena como mensaje con los botones Cerrar y Ver; para entradas que no son de cadena, muestra una alerta o un banner dependiendo de las propiedades secundarias de la entrada |
| badge             | número                      | Controla el número que se muestra como señal en el icono de la aplicación                                                                                                                              |
| sound             | cadena                      | El nombre del archivo de sonido que se reproduce como alerta; debe estar en el paquete de la aplicación o en la carpeta ```Library/Sounds```                                                                                    |
| content-available | número                      | Los valores de entrada de 1 indican a la aplicación la disponibilidad de nueva información al iniciar o reanudar una sesión |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Biblioteca APS" }


##### Biblioteca de propiedades de alerta {#alert-properties-library}

| Clave            | Tipo de valor               | Descripción del valor                                                                                                                             |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| title         | cadena                   | Una cadena corta que Apple Watch muestra brevemente como parte de una notificación                                                                    |
| body         | cadena                   | El contenido de la notificación push                                                                                                                  |
| title-loc-key  | cadena o nulo           | Una clave que establece la cadena de título para la localización actual desde el archivo ```Localizable.strings```                                          |
| title-loc-args | matriz de cadenas o nulo | Valores de cadena que pueden aparecer en lugar de los especificadores de formato de localización del título en title-loc-key                                           |
| action-loc-key | matriz de cadenas o nulo  | Si está presente, la cadena especificada establece la localización para los botones Cerrar y Ver                                                         |
| loc-key        | cadena o nulo           | Una clave que establece el mensaje de notificación para la localización actual desde el archivo ```Localizable.strings```                                  |
| loc-args       | matriz de cadenas         | Valores de cadena que pueden aparecer en lugar de los especificadores de formato de localización en loc-key                                                       |
| launch-image   | cadenas                  | El nombre de un archivo de imagen en el paquete de la aplicación que deseas usar como imagen de inicio cuando los usuarios tocan el botón de acción o deslizan la acción |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Biblioteca de propiedades de alerta" }

El creador de mensajes de Braze gestiona automáticamente la creación de las siguientes claves: **alert** y **sus propiedades**, **content-available**, **sound** y **category**.

Estos valores pueden introducirse en la pestaña **Configuración** al crear un mensaje push. Selecciona **Opciones de alerta** y selecciona una clave del diccionario de alertas para que la clave se rellene automáticamente en una nueva entrada de par clave-valor.

![Estos valores pueden introducirse en la pestaña Configuración al crear un mensaje push. Selecciona Opciones de alerta y selecciona una clave del diccionario de alertas para que la clave se rellene automáticamente en una nueva entrada de par clave-valor.]({% image_buster /assets/img_archive/keyvalue_automatickeys.png %})
{% raw %}
Cuando Braze envía una notificación push a APN, la carga útil se formateará como JSON.

**Carga útil simple**

```
{
    "aps" : { "alert" : "Message received from Spencer" },
}
```

**Carga útil compleja**

```
{
    "aps" : {
        "alert" : {
            "body" : "Hi, welcome to our app!",
            "loc-key" : "France",
            "loc-args" : ["Bonjour", "bienvenue"],
            "action-loc-key" : "Button_Type_1",
            "launch-image" : "Paris"
      },
        "content-available" : 1
    },
}
```

{% endraw %}

##### Pares clave-valor personalizados {#custom-key-value-pairs}

Además de los valores de la carga útil de la biblioteca `aps`, puedes enviar pares clave-valor personalizados al dispositivo de un usuario. Los valores en estos pares están restringidos a tipos primitivos: diccionario (objeto), matriz, cadena, número y booleano.

![Captura de pantalla relacionada con los pares clave-valor personalizados.]({% image_buster /assets/img_archive/keyvalue_enterpairs.png %})

Entre los ejemplos de uso de pares clave-valor personalizados se incluyen, entre otros, el seguimiento de métricas internas y la configuración del contexto para la interfaz de usuario. Braze te permite enviar pares clave-valor adicionales junto con una notificación push para que tu aplicación los utilice a través de la [clave extras]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=swift#swift_settings). Si prefieres utilizar otra clave, confirma que tu aplicación pueda gestionar esta clave personalizada.

{% alert warning %}
Debes evitar manejar una clave de nivel superior o un diccionario llamado ab en tu aplicación.
{% endalert %}

Apple aconseja a los clientes evitar incluir información del cliente o cualquier dato sensible como datos de carga útil personalizada. Además, Apple recomienda que cualquier acción asociada a un mensaje de alerta no debe eliminar datos en un dispositivo.

{% alert warning %}
Si utilizas la API del proveedor HTTP/2, cualquier carga útil individual que envíes a APN no puede superar un tamaño de 4096 bytes. La interfaz binaria heredada, que pronto será obsoleta, solo admite un tamaño de carga útil de 2048 bytes.
{% endalert %}

###### Campaigns desencadenadas por API {#api-triggered-campaigns}

Braze te permite enviar pares clave-valor de cadena personalizados, conocidos como `extras`. Para acceder a tus extras en Campaigns desencadenadas por API y en Campaigns programadas desencadenadas por API, en el panel establece una clave como "example_key" y un valor como {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Esto dará como resultado una salida en la consola para desarrolladores de `"extras": { "test": { "foo": 1, "bar": 1 }`

### Android

Braze te permite enviar cargas útiles de datos adicionales en las notificaciones push mediante pares clave-valor.

#### Carga útil de datos {#data-payload}

De forma similar a las notificaciones push de iOS, puedes enviar pares clave-valor personalizados al dispositivo de un usuario.

Algunos ejemplos de uso de pares clave-valor personalizados incluyen el seguimiento de métricas internas y la configuración del contexto para la interfaz de usuario, pero pueden utilizarse para cualquier propósito que elijas.

{% alert important %}
El backend de tu aplicación debe poder procesar los pares clave-valor personalizados para que la carga útil de datos funcione correctamente.
{% endalert %}

##### Campaigns desencadenadas por API

Braze te permite enviar pares clave-valor de cadena personalizados, conocidos como `extras`. Para acceder a tus extras en Campaigns desencadenadas por API y en Campaigns programadas desencadenadas por API, en el panel establece una clave como "example_key" y un valor como {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Esto dará como resultado una salida en la consola para desarrolladores de `"extras": { "test": { "foo": 1, "bar": 1 }`.

##### Opciones de mensajería FCM {#fcm-messaging-options}

Las notificaciones push de Android pueden personalizarse aún más con las opciones de mensajes FCM. Estas incluyen [prioridad de notificación]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_settings), [sonido]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_settings), retraso, tiempo de vida y compresibilidad. Estos valores pueden especificarse en la pestaña **Configuración** al crear un mensaje push. Consulta [Configuración avanzada de notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_settings) para obtener más instrucciones sobre cómo establecer estas opciones en el creador de mensajes de Braze.

![Captura de pantalla relacionada con las opciones de mensajería FCM.]({% image_buster /assets/img_archive/keyvalue_androidkeys.png %})

### Notificaciones push silenciosas {#silent-push-notifications}

Una notificación push silenciosa es una notificación push que no contiene ningún mensaje de alerta ni sonido, y se utiliza para actualizar la interfaz o el contenido de tu aplicación en segundo plano. Estas notificaciones utilizan pares clave-valor para desencadenar estas acciones en segundo plano de la aplicación. Las notificaciones push silenciosas también potencian nuestro [seguimiento de desinstalaciones]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking).

Los especialistas en marketing deben probar que las notificaciones push silenciosas desencadenan el comportamiento esperado antes de enviarlas a los usuarios de su aplicación. Después de componer tu notificación push silenciosa de [iOS]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=swift) o [Android]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android), asegúrate de dirigirte únicamente a un usuario de prueba filtrando por [ID de usuario externo]({{site.baseurl}}/api/endpoints/messaging#external-user-id) o [dirección de correo electrónico]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

Al iniciar la Campaign, debes verificar que no has recibido ninguna notificación push visible en tu dispositivo de prueba.

{% alert note %}
La limitación de notificaciones silenciosas en iOS puede provocar los siguientes síntomas:

- Métricas de seguimiento de desinstalaciones inferiores a las esperadas para usuarios de iOS
- Entrega inconsistente o retrasada de notificaciones push silenciosas
- [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories) que no se muestran
- Push Stories que llegan sin sus imágenes, videos o páginas esperadas

Esto es una limitación de la plataforma de Apple y no un problema de Braze. iOS puede retrasar o descartar notificaciones en segundo plano para algunas características de Braze, incluido el seguimiento de desinstalaciones y Push Stories. Para más detalles sobre qué limita iOS y cuándo, consulta [Limitaciones de iOS]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=swift#ios-limitations).
{% endalert %}

## Mensajes dentro de la aplicación {#in-app-messages}

Puedes añadir un par clave-valor a un mensaje dentro de la aplicación en el [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional) seleccionando la pestaña **Configuración**, seleccionando **Añadir nuevo par** y especificando tus pares clave-valor.

{% alert note %}
Los pares clave-valor no se pueden configurar a través del editor de arrastrar y soltar para mensajes dentro de la aplicación.
{% endalert %}
![Captura de pantalla relacionada con los mensajes dentro de la aplicación.]({% image_buster /assets/img_archive/keyvalue_iam.png %})

### Campaigns desencadenadas por API

Braze te permite enviar pares clave-valor de cadenas definidas de forma personalizada, conocidos como `extras`. Para acceder a tus extras en Campaigns desencadenadas por API y Campaigns programadas desencadenadas por API, en el panel establece una clave como "example_key" y un valor como {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Esto dará como resultado una salida en la consola para desarrolladores de `"extras": { "test": { "foo": 1, "bar": 1 }`.

## Correos electrónicos {#emails}

Tanto SparkPost como SendGrid admiten pares clave-valor en los correos electrónicos. Si utilizas SendGrid, los pares clave-valor se enviarán como [argumentos únicos](https://docs.sendgrid.com/for-developers/sending-email/unique-arguments). SendGrid te permite adjuntar un número ilimitado de pares clave-valor de hasta 10 000 bytes de datos. Estos pares clave-valor se pueden ver en las publicaciones del [Event Webhook](https://sendgrid.com/docs/for-developers/tracking-events/event/) de SendGrid.

{% alert note %}
Los correos electrónicos rebotados no entregarán pares clave-valor a SparkPost ni a SendGrid.
{% endalert %}

![Pestaña Información de envío del creador de mensajes de correo electrónico en Braze.]({% image_buster /assets/img_archive/keyvalue_email.png %})

## Content Cards

Para agregar un par clave-valor a una Content Card, ve a la pestaña **Settings** en el creador de mensajes de Braze y selecciona **Add New Pair**.

![Agregar par clave-valor a una Content Card]({% image_buster /assets/img_archive/kvp_content_cards.png %}){: style="max-width:70%;"}

{% alert note %}
Las variantes de control no admiten pares clave-valor. Si necesitas capturar análisis para grupos de control en pruebas A/B, crea una variante de mensaje con un par clave-valor como `control=true` y ocúltala en el código de tu aplicación mientras registras impresiones.
{% endalert %}