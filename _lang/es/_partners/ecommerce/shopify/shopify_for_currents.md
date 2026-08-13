---
nav_title: Shopify para Currents
article_title: Shopify para Currents
description: "Este artículo de referencia describe la asociación entre Braze Currents y Shopify, una empresa de comercio global que te permite conectar fácilmente Braze con tu tienda Shopify para potenciar los informes internos y realizar un mejor seguimiento de la atribución de último contacto para las compras."
page_type: partner
tool: Currents
search_tag: Partner
alias: /shopify_for_currents/
hidden: true
noindex: true

---

# Shopify para Currents {#shopify-for-currents}

> [Shopify](https://www.shopify.com/) es una empresa líder en comercio global que proporciona herramientas de confianza para iniciar, hacer crecer, comercializar y administrar un negocio de cualquier tamaño. La plataforma y los servicios de Shopify están diseñados para ofrecer fiabilidad y una mejor experiencia de compra para los consumidores en todas partes.

{% alert important %}
Esta integración se encuentra actualmente en fase beta. Para más información, ponte en contacto con tu administrador del éxito del cliente de Braze.
{% endalert %}

La integración de Braze con Shopify proporciona una solución potente para los negocios de comercio electrónico que buscan mejorar la interacción con los clientes e impulsar esfuerzos de marketing personalizados. Con [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), puedes conectar datos a Shopify para potenciar los informes internos y realizar un mejor seguimiento de la atribución de último contacto para las compras.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Currents | Para exportar datos a Shopify, debes tener [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) configurado para tu cuenta. |
| Tienda Shopify | Asegúrate de haber [configurado al menos una tienda Shopify con Braze]({{site.baseurl}}/shopify_standard_integration). |
| Permisos de propietario o miembro del personal de la tienda Shopify | {::nomarkdown}<ul><li>Acceso a todos los ajustes de <b>General</b> y <b>Online Store</b>.</li><li> Permisos de administrador adicionales:</li><ul><li>Orders: View</li><li>Customer: ReadWrite</li><li>View Customer Events (Web Pixels)</li><li>Manage Settings</li><li>View Apps Developed by Staff/Collaborators</li><li>Manage/Install Apps and Channels</li><li>Manage/Add Custom Pixels</li></ul></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración {#integration}

### Paso 1: Configura tu tienda de Shopify {#step-1-set-up-your-shopify-store}

Si aún no lo has hecho, sigue los pasos de [configuración de la integración estándar de Shopify]({{site.baseurl}}/shopify_standard_integration) para configurar al menos una tienda de Shopify con Braze.

### Paso 2: Crea un Braze Current {#step-2-create-braze-current}

1. En Braze, ve a **Partner Integrations** > **Currents** > **+ Create New Current** > **Shopify Export**.
2. Proporciona un nombre de integración y un correo electrónico de contacto.
3. En la sección **Credenciales**, selecciona la tienda de Shopify que configuraste en el [Paso 1](#step-1-set-up-your-shopify-store).
4. Selecciona los eventos que deseas rastrear. Se proporciona una lista de eventos disponibles.
5. Selecciona **Launch Current**.

![La página de Braze Shopify Currents. Esta página incluye campos para el nombre de integración, correo electrónico de contacto y tienda de Shopify.]({% image_buster /assets/img/shopify/shopify_currents.png %})

## Sincronización de perfiles de usuario {#user-profile-sync}

Además de los datos de eventos, la integración de Shopify puede sincronizar actualizaciones de perfiles de usuario desde Braze a tu tienda de Shopify. Cuando el perfil de un usuario se actualiza en Braze, Currents crea o actualiza el cliente correspondiente en tu tienda.

{% alert note %}
La sincronización de perfiles de usuario no es compatible con los [conectores de prueba de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents#testing-currents-connectors). Las demás exportaciones de eventos no se ven afectadas. Para sincronizar perfiles de usuario, utiliza un [conector estándar de Shopify Currents](#step-2-create-braze-current).
{% endalert %}

### Coincidencia de usuarios {#user-matching}

Braze hace coincidir a los clientes de Shopify utilizando el `user_id` de Braze como un [identificador personalizado](https://shopify.dev/docs/api/admin-graphql/latest/mutations/customerSet) de Shopify (`customId`) con el espacio de nombres `braze` y la clave `user_id`. Si no existe ningún cliente con ese identificador en tu tienda, se crea un nuevo cliente. Los usuarios anónimos no se sincronizan.

### Mapeado de campos {#field-mapping}

Los siguientes campos de perfil de Braze se sincronizan con Shopify:

| Campo de Braze | Campo de cliente de Shopify | Notas |
| ----------- | ---------------------- | ----- |
| `first_name` | `firstName` | Se mapea tal cual. Se envía solo cuando está presente en la actualización del perfil. |
| `last_name` | `lastName` | Se mapea tal cual. Se envía solo cuando está presente en la actualización del perfil. |
| `email_address` | `email` | Se recortan los espacios y se convierte a minúsculas antes de enviar. |
| `phone_number` | `phone` | Se envía en formato [E.164](https://en.wikipedia.org/wiki/E.164). |
| `language` | `locale` | Se convierte a una configuración regional compatible con Shopify. Al portugués y al chino se les asigna una variante regional (como `pt-BR`) basada en el país del usuario. Si el idioma del usuario no es compatible con Shopify, este campo se omite. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Solo se envían los campos presentes en una actualización de perfil. Los campos omitidos en una actualización se dejan sin cambios en Shopify; una sincronización nunca borra ni elimina un campo en tu cliente de Shopify.

### Campos que no se sincronizan {#fields-that-are-not-synced}

La integración actualmente no escribe metacampos de Shopify, por lo que los campos de perfil que requerirían un metacampo no se sincronizan. En particular, los atributos personalizados no se envían a Shopify. Los demás campos que no se envían son `external_user_id`, `gender`, `dob` (fecha de nacimiento), `timezone`, `home_city`, `country` y `archived`.

Braze puede crear definiciones de metacampos bajo el espacio de nombres `braze` en tu tienda (por ejemplo, `braze.gender`). Estas definiciones están reservadas para un posible uso futuro; Braze actualmente no escribe valores en ellas. La excepción es `braze.user_id`, que almacena el identificador utilizado para hacer coincidir a tus clientes.