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

## Casos de uso {#use-cases}

Aquí tienes algunos ejemplos de casos de uso para agregar metadatos con pares clave-valor:

1. **Parámetros de seguimiento:** Adjuntar parámetros UTM con fines de análisis
   - Clave: `utm_campaign`
   - Valor: `spring_sale`
2. **Etiquetas personalizadas:** Agregar etiquetas para enrutamiento interno o categorización
   - Clave: `priority`
   - Valor: `high`
3. **Desencadenadores de comportamiento:** Metadatos utilizados para desencadenar o personalizar comportamientos dentro de la aplicación
   - Clave: `deep_link`
   - Valor: `app://promo-page`

## Notificaciones push {#push-notifications}

Los pares clave-valor se pueden agregar a las notificaciones push de Android, iOS y web. Puedes usar pares clave-valor para actualizar métricas internas y contenido de la aplicación, o personalizar las propiedades de las notificaciones push, como la priorización de alertas, la localización y los sonidos.

En el creador de mensajes, selecciona la pestaña **Settings**, selecciona **Add New Pair** y especifica tus pares clave-valor.

### iOS

El servicio de notificaciones push de Apple (APN) admite la configuración de preferencias de alertas y el envío de datos personalizados mediante pares clave-valor. APN utiliza la biblioteca reservada de Apple `aps`, que incluye claves y valores predeterminados que gobiernan las propiedades de las alertas.

##### Biblioteca APS {#aps-library}

| Clave  | Tipo de valor  | Descripción del valor |
|-------------------|-----------------------------|----------------------------------|
| alert             | cadena u objeto de diccionario | Para entradas de cadena, muestra una alerta con la cadena como mensaje con botones Cerrar y Ver; para entradas que no son cadenas, muestra una alerta o banner dependiendo de las propiedades secundarias de la entrada |
| badge             | número                      | Gobierna el número que se muestra como señal en el icono de la aplicación                                                                                                                              |
| sound             | cadena                      | El nombre del archivo de sonido que se reproduce como alerta; debe estar en el paquete de la aplicación o en la carpeta ```Library/Sounds```                                                                                    |
| content-available | número                      | Los valores de entrada de 1 señalan a la aplicación la disponibilidad de nueva información al iniciar o reanudar la sesión |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Biblioteca APS" }


##### Biblioteca de propiedades de alertas {#alert-properties-library}

| Clave            | Tipo de valor               | Descripción del valor                                                                                                                             |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| title         | cadena                   | Una cadena corta que Apple Watch muestra brevemente como parte de una notificación                                                                    |
| body         | cadena                   | El contenido de la notificación push                                                                                                                  |
| title-loc-key  | cadena o nulo           | Una clave que establece la cadena de título para la localización actual desde el archivo ```Localizable.strings```                                          |
| title-loc-args | matriz de cadenas o nulo | Valores de cadena que pueden aparecer en lugar de los especificadores de formato de localización del título en title-loc-key                                           |
| action-loc-key | matriz de cadenas o nulo  | Si está presente, la cadena especificada establece la localización para los botones Cerrar y Ver                                                         |
| loc-key        | cadena o nulo           | Una clave que establece el mensaje de notificación para la localización actual desde el archivo ```Localizable.strings```                                  |
| loc-args       | matriz de cadenas         | Valores de cadena que pueden aparecer en lugar de los especificadores de formato de localización en loc-key                                                       |
| launch-image   | cadenas                  | El nombre de un archivo de imagen en el paquete de la aplicación que deseas usar como imagen de lanzamiento cuando los usuarios tocan el botón de acción o deslizan la acción |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Biblioteca de propiedades de alertas" }

El creador de mensajes de Braze maneja automáticamente la creación de las siguientes claves: **alert** y **sus propiedades**, **content-available**, **sound** y **category**.

Estos valores se pueden ingresar en la pestaña **Settings** al crear un mensaje push. Selecciona **Alert Options** y selecciona una clave de diccionario de alertas para que la clave se complete automáticamente en una nueva entrada de par clave-valor.

![]({% image_buster /assets/img_archive/keyvalue_automatickeys.png %})
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

Además de los valores de carga útil de la biblioteca `aps`, puedes enviar pares clave-valor personalizados al dispositivo de un usuario. Los valores en estos pares están restringidos a tipos primitivos: diccionario (objeto), matriz, cadena, número y booleano.

![]({% image_buster /assets/img_archive/keyvalue_enterpairs.png %})

Los casos de uso para pares clave-valor personalizados incluyen, entre otros, el mantenimiento de métricas internas y la configuración del contexto para la interfaz de usuario. Braze te permite enviar pares clave-valor adicionales junto con una notificación push para ser utilizados a través de tu aplicación dentro de la [clave extras]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings/#extracting-data-from-push-key-value-pairs). Si prefieres usar otra clave, confirma que tu aplicación pueda manejar esta clave personalizada.

{% alert warning %}
Debes evitar manejar una clave o diccionario de nivel superior llamado ab en tu aplicación.
{% endalert %}

Apple aconseja a los clientes evitar incluir información del cliente o cualquier dato sensible como datos de carga útil personalizada. Además, Apple recomienda que cualquier acción asociada con un mensaje de alerta no elimine datos en un dispositivo.

{% alert warning %}
Si estás usando la API del proveedor HTTP/2, cualquier carga útil individual que envíes a APN no puede exceder un tamaño de 4096 bytes. La interfaz binaria heredada, que pronto será descontinuada, solo admite un tamaño de carga útil de 2048 bytes.
{% endalert %}

###### Campaigns desencadenadas por API {#api-triggered-campaigns}

Braze te permite enviar pares clave-valor de cadena definidos de forma personalizada, conocidos como `extras`. Para acceder a tus extras en Campaigns desencadenadas por API y Campaigns planificadas desencadenadas por API, en el dashboard establece una clave como "example_key" y un valor como {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Esto resultará en una salida de la consola para desarrolladores de `"extras": { "test": { "foo": 1, "bar": 1 }`

### Android

Braze te permite enviar cargas útiles de datos adicionales en notificaciones push usando pares clave-valor.

##### Carga útil de datos {#data-payload}

Similar a las notificaciones push de iOS, puedes enviar pares clave-valor personalizados al dispositivo de un usuario.

Algunos casos de uso para pares clave-valor personalizados incluyen el mantenimiento de métricas internas y la configuración del contexto para la interfaz de usuario, pero pueden usarse para cualquier propósito que elijas.

{% alert important %}
El backend de tu aplicación debe ser capaz de procesar pares clave-valor personalizados para que la carga útil de datos funcione correctamente.
{% endalert %}

###### Campaigns desencadenadas por API

Braze te permite enviar pares clave-valor de cadena definidos de forma personalizada, conocidos como `extras`. Para acceder a tus extras en Campaigns desencadenadas por API y Campaigns planificadas desencadenadas por API, en el dashboard establece una clave como "example_key" y un valor como {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Esto resultará en una salida de la consola para desarrolladores de `"extras": { "test": { "foo": 1, "bar": 1 }`.

##### Opciones de mensajería FCM {#fcm-messaging-options}

Las notificaciones push de Android se pueden personalizar aún más con las opciones de mensajes FCM. Estas incluyen [prioridad de notificación]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#notification-priority), [sonido]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#sounds), retraso, duración y colapsabilidad. Estos valores se pueden especificar en la pestaña **Settings** al crear un mensaje push. Consulta [Configuración avanzada de notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_settings) para obtener más instrucciones sobre cómo configurar estas opciones en el creador de mensajes de Braze.

![]({% image_buster /assets/img_archive/keyvalue_androidkeys.png %})

### Notificaciones push silenciosas {#silent-push-notifications}

Una notificación push silenciosa es una notificación push que no contiene mensaje de alerta ni sonido, y se usa para actualizar la interfaz o el contenido de tu aplicación en segundo plano. Estas notificaciones hacen uso de pares clave-valor para desencadenar estas acciones de la aplicación en segundo plano. Las notificaciones push silenciosas también potencian nuestro [Uninstall Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/).

Los especialistas en marketing deben probar que las notificaciones push silenciosas desencadenen el comportamiento esperado antes de enviarlas a los usuarios de su aplicación. Después de redactar tu notificación push silenciosa de [iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) o [Android]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android), asegúrate de dirigirte solo a un usuario de prueba filtrando por [ID de usuario externo]({{site.baseurl}}/developer_guide/rest_api/messaging/#external-user-id) o [dirección de correo electrónico]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/).

Al lanzar la campaña, debes verificar que no hayas recibido ninguna notificación push visible en tu dispositivo de prueba.

{% alert note %}
La limitación de notificaciones silenciosas de iOS puede causar los siguientes síntomas:

- Métricas de Uninstall Tracking más bajas de lo esperado para usuarios de iOS
- Entrega inconsistente o retrasada de notificaciones push silenciosas
- [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories/) que no se muestran
- Push Stories que llegan sin sus imágenes, videos o páginas esperados

Esta es una limitación de la plataforma de Apple, no un problema de Braze. iOS puede retrasar o descartar notificaciones en segundo plano para algunas características de Braze, incluido Uninstall Tracking y Push Stories. Para más detalles sobre qué limita iOS y cuándo, consulta [Limitaciones de iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#ios-limitations).
{% endalert %}

## Mensajes dentro de la aplicación {#in-app-messages}

Puedes agregar un par clave-valor a un mensaje dentro de la aplicación en el [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/) seleccionando la pestaña **Settings**, seleccionando **Add New Pair** y luego especificando tus pares clave-valor.

{% alert note %}
Los pares clave-valor no se pueden configurar a través del editor de arrastrar y soltar para mensajes dentro de la aplicación.
{% endalert %}
![]({% image_buster /assets/img_archive/keyvalue_iam.png %})

#### Campaigns desencadenadas por API

Braze te permite enviar pares clave-valor de cadena definidos de forma personalizada, conocidos como `extras`. Para acceder a tus extras en Campaigns desencadenadas por API y Campaigns planificadas desencadenadas por API, en el dashboard establece una clave como "example_key" y un valor como {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Esto resultará en una salida de la consola para desarrolladores de `"extras": { "test": { "foo": 1, "bar": 1 }`.

## Correos electrónicos {#emails}

Tanto SparkPost como SendGrid admiten pares clave-valor en correos electrónicos. Si usas SendGrid, los pares clave-valor se enviarán como [argumentos únicos](https://docs.sendgrid.com/for-developers/sending-email/unique-arguments). SendGrid te permite adjuntar un número ilimitado de pares clave-valor de hasta 10,000 bytes de datos. Estos pares clave-valor se pueden ver en las publicaciones del [Event Webhook](https://sendgrid.com/docs/for-developers/tracking-events/event/) de SendGrid.

{% alert note %}
Los correos electrónicos rebotados no entregarán pares clave-valor a SparkPost o SendGrid.
{% endalert %}

![Pestaña de información de envío del creador de mensajes de correo electrónico en Braze.]({% image_buster /assets/img_archive/keyvalue_email.png %})

## Content Cards

Para agregar un par clave-valor a una Content Card, ve a la pestaña **Settings** en el creador de mensajes de Braze y selecciona **Add New Pair**.

![Agregar par clave-valor a una Content Card]({% image_buster /assets/img_archive/kvp_content_cards.png %}){: style="max-width:70%;"}