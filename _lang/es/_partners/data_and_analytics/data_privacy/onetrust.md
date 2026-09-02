---
nav_title: OneTrust
article_title: OneTrust
description: "Este artículo de referencia describe la asociación entre Braze y OneTrust, un proveedor de software de seguridad y privacidad de datos, que te permite utilizar el generador de flujos de trabajo de OneTrust para crear flujos de trabajo de seguridad para tu producto."
alias: /partners/onetrust/
page_type: partner
search_tag: Partner

---

# OneTrust

> [OneTrust](https://www.onetrust.com/) es un proveedor de software de privacidad y seguridad que proporciona la visibilidad que necesitas para comprender mejor tu panorama de confianza, la acción para aprovechar información valiosa y la automatización para mantenerte por delante de la competencia.

_Esta integración está mantenida por OneTrust._

## Sobre la integración {#about-the-integration}

La integración de Braze y OneTrust te permite utilizar el generador de flujos de trabajo de OneTrust para crear flujos de trabajo de seguridad para tu producto.
## Requisitos previos {#prerequisites}

| Requisitos | Descripción |
|---|---|
| Cuenta de OneTrust | Una cuenta de [OneTrust](https://www.onetrust.com/) para aprovechar esta asociación. |
| Clave de API de Braze | Una clave de API REST or transferencia de estado representacional de Braze con los permisos necesarios para el punto de conexión que utilizará tu acción de OneTrust.<br><br>Se puede crear en el dashboard de Braze desde **Configuración** > **Claves de API**. |
| Instancia de Braze | Tu instancia de Braze se puede obtener a través de tu administrador de incorporación de Braze o en la [página de resumen de la API]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

La siguiente integración proporciona orientación para crear un flujo de trabajo de actualización de consentimiento de usuario y un flujo de trabajo de eliminación de usuario. Para más detalles sobre los puntos de conexión de Braze soportados adicionalmente, consulta [Otras acciones soportadas](#Other-supported-actions).

### Añadir credenciales de Braze a OneTrust {#add-braze-credentials-to-onetrust}

En el menú **Integrations** de OneTrust, ve a **Credentials** > botón **Add New** para abrir la pantalla **Select System**. Aquí, busca **Braze** y haz clic en el botón **Next**.

Sigue las instrucciones de la pantalla **Enter Credential Details** y proporciona la siguiente información. Guarda tus credenciales cuando hayas terminado.
  - Nombre de credencial
  - Establece el tipo de conector en **Web App**
  - Nombre de host: `<your-braze-instance-url>`
  - **Encabezado de solicitud**:
    - **Authorization**: Bearer
    - **Content-Type**: application/json
  - Token: `<your-braze-api-key>`

### Añadir Braze como sistema {#add-braze-as-a-system}

#### Paso 1: Crear un flujo de trabajo {#step-1-create-a-workflow}

{% tabs %}
{% tab Actualización de consentimiento de usuario %}
1. En el menú de integraciones de OneTrust, ve a **Gallery** > **Braze** > **Add** para crear un nuevo flujo de trabajo.![Galería de OneTrust mostrando la integración de Braze con un botón Add.]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. Proporciona un nombre y un correo electrónico de notificación en el modal del flujo de trabajo. Haz clic en el botón **Create**. Al crearlo, accederás al generador de flujos de trabajo. Tu flujo de trabajo de Braze se rellenará con llamadas a la API y acciones que pueden utilizarse para procesar solicitudes de eliminación. <br><br>
3. En el generador de flujos de trabajo, selecciona la acción que deseas activar en el flujo de trabajo.<br>![Generador de flujos de trabajo de OneTrust para un evento de actualización de consentimiento del interesado.]({% image_buster /assets/img/onetrust/onetrust2.png %})

{% endtab %}
{% tab Eliminación de usuario %}

1. En el menú de integraciones de OneTrust, ve a **Gallery** > **Braze** > **Add** para crear un nuevo flujo de trabajo.![Galería de OneTrust mostrando la integración de Braze con un botón Add.]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. Proporciona un nombre y un correo electrónico de notificación en el modal del flujo de trabajo. Haz clic en el botón **Create**. Al crearlo, accederás al generador de flujos de trabajo. Tu flujo de trabajo de Braze se rellenará con llamadas a la API y acciones que pueden utilizarse para procesar solicitudes de eliminación. <br><br>
3. En el generador de flujos de trabajo, selecciona la acción que deseas activar en el flujo de trabajo.<br>![Generador de flujos de trabajo de OneTrust para un evento de eliminación del interesado.]({% image_buster /assets/img/onetrust/onetrust8.png %})
{% endtab %}
{% endtabs %}

#### Paso 2: Seleccionar acción {#step-2-select-action}
{% tabs %}
{% tab Actualización de consentimiento de usuario %}

1. Cuando hayas terminado, haz clic en **Done** y selecciona **Add Action**. Ten en cuenta que la acción que elijas dependerá del tipo de preferencia que se esté actualizando y de tu punto de conexión preferido.
- Para actualizar las preferencias globales de suscripción de un usuario, selecciona la acción **POST User track - attributes**.
- Para actualizar las preferencias del grupo de suscripción de un usuario, selecciona la acción **POST User Track - Attributes** o la acción **POST Set Users Subscription Group Status**.<br>![Menú Add Action de OneTrust mostrando POST User track - attributes.]({% image_buster /assets/img/onetrust/onetrust4.png %})<br><br>
2. Elige la acción deseada, selecciona tus credenciales de Braze creadas anteriormente y haz clic en **Next**.<br>![Selección de credenciales de OneTrust para una acción POST User track - attributes.]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% tab Eliminación de usuario %}

1. Cuando hayas terminado, haz clic en **Done** y selecciona **Add Action**.
- Para eliminar un usuario de Braze, selecciona la acción **POST User Delete Action**.
<br>![Menú Add Action de OneTrust mostrando POST User Delete.]({% image_buster /assets/img/onetrust/onetrust9.png %})<br><br>
2. Elige la acción deseada, selecciona tus credenciales de Braze creadas anteriormente y haz clic en **Next**.<br>![Selección de credenciales de OneTrust para una acción POST User Delete.]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% endtabs %}
#### Paso 3: Actualizar el cuerpo de la solicitud {#step-3-update-request-body}
{% tabs %}
{% tab Actualización de consentimiento de usuario %}

1. Actualiza el cuerpo para incluir los valores dinámicos necesarios. Asegúrate de que el cuerpo de la acción coincide con el [punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) y con el [punto de conexión `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).
2. Personaliza el flujo de trabajo con parámetros adicionales o lógica condicional para satisfacer las necesidades de tu organización.
3. Cuando termines de editar, haz clic en **Finish** y luego en **Activate** para habilitar el flujo de trabajo.

{% alert note %}
Al utilizar los flujos de trabajo de OneTrust para actualizar las preferencias del grupo de suscripción en Braze, el `subscription_group_id` debe coincidir con el ID establecido por Braze cuando se creó el grupo de suscripción. Puedes acceder al `subscription_group_id` de un grupo de suscripción navegando a la página **Subscription Group** en el dashboard de Braze.
{% endalert %}

![Cuerpo de solicitud de OneTrust para POST User track - attributes con campos de grupo de suscripción.]({% image_buster /assets/img/onetrust/onetrust6.png %})

{% endtab %}
{% tab Eliminación de usuario %}

1. Actualiza el cuerpo para incluir los valores dinámicos necesarios. Asegúrate de que el cuerpo de la acción coincide con el [punto de conexión `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/).
2. Cuando termines de editar, selecciona **Finish** y luego **Activate** para habilitar el flujo de trabajo.

![Cuerpo de solicitud de OneTrust para POST User Delete con un campo external_id.]({% image_buster /assets/img/onetrust/onetrust10.png %})

#### Actualizar el flujo de trabajo de solicitud del interesado {#update-the-data-subject-request-workflow}
1. En el menú **Privacy Rights Automation**, selecciona **Workflows**.
2. Selecciona el flujo de trabajo que deseas actualizar con la integración de Braze.
3. Selecciona el botón **Edit** para habilitar la edición.
4. A continuación, selecciona el paso del flujo de trabajo al que deseas añadir la integración de Braze y haz clic en **Add Connection**.
5. Añade el flujo de trabajo de Braze creado anteriormente como una subtarea del sistema.

{% endtab %}
{% endtabs %}

## Otras acciones soportadas {#other-supported-actions}

Además de las acciones **POST User track - Attributes**, **POST Set Users Subscription Group Status** y **POST User Delete**, Braze admite otros puntos de conexión que pueden utilizarse para crear flujos de trabajo personalizados y como subtareas dentro de flujos de trabajo existentes.

Para ver la lista completa de acciones admitidas:
1. En OneTrust, haz clic en **Systems** en el menú **Integrations**.
2. Elige el sistema **Braze**.
3. Ve a la pestaña **Actions**.

![Pestaña Actions del sistema Braze en OneTrust mostrando las acciones de API soportadas.]({% image_buster /assets/img/onetrust/onetrust7.png %})