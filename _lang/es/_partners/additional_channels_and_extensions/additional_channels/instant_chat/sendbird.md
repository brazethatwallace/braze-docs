---
nav_title: Sendbird
article_title: Sendbird
description: "Este artículo de referencia describe la asociación entre Braze y Sendbird, una solución líder de mensajería dentro de la aplicación que permite a los usuarios recibir notificaciones dentro de la aplicación en la plataforma Sendbird."
alias: /partners/sendbird/
page_type: partner
search_tag: Partner

---

# Sendbird

> [Sendbird](https://sendbird.com/) Notifications ofrece a los especialistas en marketing y gestores de producto un nuevo y potente canal para comunicarse con sus clientes dentro de la aplicación con mensajes unidireccionales persistentes e interactivos. Estos mensajes pueden utilizarse para cualquier tipo de comunicación y se emplean sobre todo con fines promocionales y transaccionales.

_Esta integración está mantenida por Sendbird._

## Sobre la integración {#about-the-integration}

La integración de Braze y Sendbird permite a los usuarios de la empresa:
* Utilizar las funciones de segmentación y desencadenamiento de Braze para iniciar notificaciones personalizadas dentro de la aplicación.
* Crear notificaciones personalizadas dentro de la aplicación en la plataforma Sendbird Notifications, que luego se entregan dentro del entorno de la aplicación, mejorando la interacción del usuario.

Al aprovechar las capacidades conjuntas de Braze y Sendbird Notifications, las empresas pueden elevar la interacción con los clientes y aumentar las tasas de conversión a través de estrategias eficaces de notificación dentro de la aplicación.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Sendbird | Se requiere una cuenta Sendbird para beneficiarse de esta asociación. |
| Sendbird UIKit | Debes tener el Sendbird UIKit instalado en tu aplicación [iOS](https://sendbird.com/docs/notifications/v1/uikit/ios/install-uikit) o [Android](https://sendbird.com/docs/notifications/v1/uikit/android/install-uikit). |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel de Braze desde **Configuración** > **Claves de API**. |
| Punto de conexión REST de Braze | [La URL de tu punto de conexión REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto de conexión dependerá de la URL de Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

![]({% image_buster /assets/img/sendbird/use-cases.png %})

La integración de Braze y Sendbird Notifications ofrece una amplia gama de casos de uso para impulsar la interacción con los clientes y ofrecer una experiencia de usuario excepcional:

- **Marketing**: Mejora las campañas dirigidas con promociones personalizadas y recomendaciones adaptadas a las preferencias de los usuarios, como descuentos exclusivos basados en el historial de navegación o en compras anteriores.
- **Transaccional**: Mejora la comunicación con el cliente mediante actualizaciones en tiempo real sobre pedidos, entregas, facturación y pagos, incluidas notificaciones sobre el estado del pedido, detalles del envío y plazos de entrega estimados.

## Integración {#integration}

### Paso 1: Crear una plantilla de notificación {#step-1-create-a-notification-template}

[Las plantillas de Sendbird](https://sendbird.com/docs/notifications/v1/templates) te permiten enviar notificaciones personalizadas dentro de la aplicación creando y utilizando varias plantillas para cada canal. Las plantillas pueden crearse y personalizarse en Sendbird Dashboard sin necesidad de escribir código.

![]({% image_buster /assets/img/sendbird/sendbird-dashboard-template.png %})

### Paso 2: Configurar la integración de Braze en el panel de Sendbird {#step-2-set-up-the-braze-integration-on-sendbird-dashboard}

Desde **Sendbird Dashboard**, selecciona tu aplicación, navega a **Notifications > Integrations** y haz clic en **Add** en la sección **Braze**. Aquí necesitarás tu clave de API REST de Braze y tu punto de conexión REST de Braze.

Una vez que hayas proporcionado todos los campos, haz clic en **Save** para completar la integración y acceder a los puntos de conexión de integración y al token de API.

### Paso 3: Instalar Sendbird Notification Builder {#step-3-install-sendbird-notification-builder}

A continuación, debes instalar [Sendbird Notification Builder](https://chrome.google.com/webstore/detail/apbhgfffamdcdogeijjcnjbmghahoaji). Esta extensión de Google Chrome te permite enviar notificaciones personalizadas a través de Sendbird en el panel de Braze.

![]({% image_buster /assets/img/sendbird/sendbird-notification-builder.png %})

#### Añadir credenciales de Sendbird a la extensión {#add-sendbird-credentials-to-the-extension}

Una vez instalada la extensión, haz clic en el icono de Sendbird en la barra de herramientas de tu navegador y selecciona **Settings**. Aquí, proporciona el ID de tu aplicación y el token de API que se encuentra en **Sendbird Notification Builder**.

### Paso 4: Asignar el ID de usuario de Sendbird al ID de usuario de Braze {#step-4-map-sendbird-user-id-to-braze-user-id}

Se debe añadir un ID de usuario de Sendbird a un perfil de usuario de Braze como [atributo personalizado]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) para que pueda utilizarse la integración. Puedes cargar y actualizar perfiles de usuario mediante archivos CSV desde la página de [importación de usuarios]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv). También puedes utilizar el ID de usuario de Braze como ID de usuario de Sendbird.

### Paso 5: Configura tu plantilla de webhook {#step-5-set-up-your-webhook-template}

En Braze, desde **Plantillas y medios**, ve a **Plantillas de Webhook** y elige la **Sendbird Webhook Template**. Ten en cuenta que esta plantilla solo estará disponible si tienes instalada la extensión Sendbird Notification Builder.

{% raw %}
1. Proporciona un nombre de plantilla y añade equipos y etiquetas según sea necesario.
2. Copia un punto de conexión en tiempo real o por lotes del panel de Sendbird en la **Webhook URL**.
3. En el campo **Receiver**, haz clic en el icono <i class="fas fa-plus"></i> e inserta el atributo de usuario asignado al ID de usuario de Sendbird.
    - `{{ '{{' }}custom_attribute.${sendbird_id}}}` si estás utilizando un atributo personalizado `sendbird_id` como ID de usuario de Sendbird.
    - `{{ '{{' }}${user_id}}}` si utilizas el ID de usuario de Braze como ID de usuario de Sendbird.
4. En la pestaña **Settings**, sustituye `SENDBIRD_API_TOKEN` por el token de la API de notificaciones del panel de Sendbird.
5. Guarda la plantilla.
{% endraw %}

## Uso de esta integración {#using-this-integration}

### Campaigns

1. En el panel de Braze, en la página **Campaigns**, haz clic en **Crear campaña** > **Webhook**.
2. Selecciona la plantilla de webhook que creaste anteriormente. Se recomienda encarecidamente utilizar el punto de conexión por lotes para las Campaigns.
3. Personaliza la plantilla editando sus variables en la pestaña **Redactar**.

### Canvas

1. Desde un Canvas nuevo o existente, añade un componente **Message**.
2. Abre el componente y selecciona **Webhook** en **Canales de mensajería**.
3. Selecciona la plantilla de webhook que creaste anteriormente. Se recomienda encarecidamente utilizar el punto de conexión en tiempo real para los Canvas.
4. Personaliza la plantilla editando sus variables en la pestaña **Redactar**.

## Personalización {#customization}

### Seguimiento de la entrega y el estado de apertura {#track-delivery-and-open-status}

Para integrar el evento de entrega y estado de apertura de las notificaciones con la métrica de conversión de una Campaign, añade un evento personalizado en el panel de Braze.

1. En el panel de Braze, ve a **Configuración > Administrar configuración > Eventos personalizados** y haz clic en **+ Añadir evento personalizado**.
2. Después de crear un evento personalizado, haz clic en **Administrar propiedades**, añade una propiedad llamada "status" y elige "String" como tipo de propiedad.
3. Cuando redactes una notificación en Campaigns o Canvas, introduce el nombre del evento personalizado en el campo **Event Name**.

Este evento personalizado se activará dos veces para cada notificación: cuando se envíe un mensaje y cuando un usuario abra el mensaje.
- Cuando se envía un mensaje, se activa un evento personalizado con el estado `SENT`.
- Cuando se lee un mensaje, se activa un evento personalizado con el estado `READ`.