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

## Acerca de la integración {#about-the-integration}

La integración de Braze y Sendbird permite a los usuarios de la empresa:
{% multi_lang_include partners/instant_chat/sendbird_integration_bullets.md %}

Al aprovechar las capacidades conjuntas de Braze y Sendbird Notifications, las empresas pueden elevar la interacción con los clientes e impulsar mayores tasas de conversión a través de estrategias efectivas de notificaciones dentro de la aplicación.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Sendbird | Se requiere una cuenta de Sendbird para aprovechar esta integración. |
| Sendbird UIKit | Debes tener el Sendbird UIKit instalado en tu aplicación [iOS](https://sendbird.com/docs/notifications/v1/uikit/ios/install-uikit) o [Android](https://sendbird.com/docs/notifications/v1/uikit/android/install-uikit). |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Se puede crear en el panel de Braze desde **Configuración** > **Claves de API**. |
| Endpoint REST de Braze | [La URL de tu endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Tu endpoint dependerá de la URL de Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Ejemplos {#use-cases}

![Diagrama que resume los ejemplos de integración de Braze y Sendbird Notifications para mensajería de marketing y transaccional.]({% image_buster /assets/img/sendbird/use-cases.png %})

La integración de Braze y Sendbird Notifications ofrece una variedad de ejemplos para impulsar la interacción con los clientes y ofrecer una experiencia de usuario excepcional:

- **Marketing**: Mejora las campañas dirigidas con promociones personalizadas y recomendaciones adaptadas a las preferencias de los usuarios, como descuentos exclusivos basados en el historial de navegación o compras anteriores.
- **Transaccional**: Eleva la comunicación con los clientes mediante actualizaciones en tiempo real sobre pedidos, entregas, facturación y pagos, incluyendo notificaciones sobre el estado del pedido, detalles de envío y tiempos de entrega estimados.

## Integración {#integration}

### Paso 1: Crear una plantilla de notificación {#step-1-create-a-notification-template}

Las [plantillas de Sendbird](https://sendbird.com/docs/notifications/v1/templates) te permiten enviar notificaciones personalizadas dentro de la aplicación creando y utilizando múltiples plantillas para cada canal. Las plantillas se pueden crear y personalizar en el panel de Sendbird sin necesidad de escribir código.

![Editor de plantillas del panel de Sendbird para crear plantillas de notificación.]({% image_buster /assets/img/sendbird/sendbird-dashboard-template.png %})

### Paso 2: Configurar la integración de Braze en el panel de Sendbird {#step-2-set-up-the-braze-integration-on-sendbird-dashboard}

Desde el **panel de Sendbird**, selecciona tu aplicación, navega a **Notifications > Integrations** y haz clic en **Add** en la sección **Braze**. Aquí necesitarás tu clave de API REST de Braze y el endpoint REST de Braze.

Una vez que hayas completado todos los campos, haz clic en **Save** para completar la integración y acceder a los endpoints de integración y al token de API.

### Paso 3: Instalar Sendbird Notification Builder {#step-3-install-sendbird-notification-builder}

A continuación, debes instalar [Sendbird Notification Builder](https://chrome.google.com/webstore/detail/apbhgfffamdcdogeijjcnjbmghahoaji). Esta extensión de Google Chrome te permite enviar notificaciones personalizadas a través de Sendbird en el panel de Braze.

![Panel de la extensión de Chrome Sendbird Notification Builder en el panel de Braze.]({% image_buster /assets/img/sendbird/sendbird-notification-builder.png %})

#### Agregar credenciales de Sendbird a la extensión {#add-sendbird-credentials-to-the-extension}

Una vez instalada la extensión, haz clic en el icono de Sendbird en la barra de herramientas de tu navegador y selecciona **Settings**. Aquí, proporciona tu ID de aplicación y el token de API que se encuentran en **Sendbird Notification Builder**.

### Paso 4: Mapear el ID de usuario de Sendbird al ID de usuario de Braze {#step-4-map-sendbird-user-id-to-braze-user-id}

Se debe agregar un ID de usuario de Sendbird a un perfil de usuario de Braze como [atributo personalizado]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) para que la integración pueda utilizarse. Puedes cargar y actualizar perfiles de usuario mediante archivos CSV desde la página de [importación de usuarios]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv). Alternativamente, puedes usar el ID de usuario de Braze como el ID de usuario de Sendbird.

### Paso 5: Configurar tu plantilla de webhook {#step-5-set-up-your-webhook-template}

En Braze, desde **Plantillas y medios**, ve a **Plantillas de webhook** y elige la **plantilla de webhook de Sendbird**. Ten en cuenta que esta plantilla solo estará disponible si has instalado la extensión Sendbird Notification Builder.

{% raw %}
1. Proporciona un nombre de plantilla y agrega equipos y etiquetas según sea necesario.
2. Copia un endpoint en tiempo real o por lotes desde el panel de Sendbird en la **URL del webhook**.
3. En el campo **Receiver**, haz clic en el icono <i class="fas fa-plus"></i> e inserta el atributo de usuario mapeado al ID de usuario de Sendbird.
    - `{{ '{{' }}custom_attribute.${sendbird_id}}}` si estás usando un atributo personalizado `sendbird_id` como el ID de usuario de Sendbird.
    - `{{ '{{' }}${user_id}}}` si estás usando el ID de usuario de Braze como el ID de usuario de Sendbird.
4. En la pestaña **Settings**, reemplaza `SENDBIRD_API_TOKEN` con el token de API de notificaciones del panel de Sendbird.
5. Guarda la plantilla.
{% endraw %}

## Uso de esta integración {#using-this-integration}

### Campaigns

1. En el panel de Braze, en la página **Campaigns**, haz clic en **Create Campaign** > **Webhook**.
2. Selecciona la plantilla de webhook que creaste en esta sección. Se recomienda encarecidamente usar el endpoint Batch para Campaigns.
3. Personaliza la plantilla editando sus variables en la pestaña **Compose**.

### Canvas

1. Desde un Canvas nuevo o existente, añade un componente **Message**.
2. Abre el componente y selecciona **Webhook** en los **Messaging Channels**.
3. Selecciona la plantilla de webhook que creaste en esta sección. Se recomienda encarecidamente usar el endpoint en tiempo real para Canvas.
4. Personaliza la plantilla editando sus variables en la pestaña **Compose**.

## Personalización {#customization}

### Seguimiento del estado de entrega y apertura {#track-delivery-and-open-status}

Para integrar los eventos de estado de entrega y apertura de las notificaciones con la métrica de conversión de una Campaign, añade un evento personalizado en el panel de Braze.

1. Desde el panel de Braze, ve a **Configuración > Administrar configuración > Eventos personalizados** y haz clic en **+ Añadir evento personalizado**.
2. Después de crear un evento personalizado, haz clic en **Administrar propiedades**, añade una propiedad llamada "status" y elige "String" como tipo de propiedad.
3. Cuando compongas una notificación en Campaigns o Canvas, introduce el nombre del evento personalizado en el campo **Event Name**.

Este evento personalizado se desencadenará dos veces por cada notificación: cuando se envía un mensaje y cuando un usuario abre el mensaje.
- Cuando se envía un mensaje, se desencadena un evento personalizado con el estado `SENT`.
- Cuando se lee un mensaje, se desencadena un evento personalizado con el estado `READ`.