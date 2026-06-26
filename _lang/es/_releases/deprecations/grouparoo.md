---
nav_title: Grouparoo
page_order: 1
page_type: update
noindex: true
description: "Este artículo describe la asociación entre Braze y Grouparoo, una herramienta ETL inversa de código abierto utilizada para potenciar las herramientas de marketing, ventas y soporte con datos de tu almacén de datos."

---

# Grouparoo

{% alert update %}
La compatibilidad con Grouparoo se interrumpió a partir de abril de 2022.
{% endalert %}

> [Grouparoo](https://www.grouparoo.com/) es una herramienta ETL inversa de código abierto que sincroniza los datos de tu almacén con las herramientas de marketing, ventas y soporte. Su interfaz de usuario centrada en el modelo permite a los miembros no técnicos del equipo configurar y programar sincronizaciones de datos.

La integración de Braze y Grouparoo sincroniza los datos del almacén con Braze. Las programaciones de sincronización automática mantienen las comunicaciones con los clientes al día con información actualizada.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta y proyecto Grouparoo | Para beneficiarte de esta asociación es necesario disponer de una cuenta y un proyecto de Grouparoo.<br><br>Esta integración se puede utilizar con la edición comunitaria gratuita y las soluciones empresariales proporcionadas por Grouparoo. La configuración tendrá lugar en la interfaz de usuario de configuración de Grouparoo. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos de usuarios y seguimiento. <br><br> Se puede crear en el panel de Braze desde **Configuración** > **Claves de API**. |
| Punto de conexión REST de Braze | [La URL de tu punto de conexión REST](https://www.grouparoo.com/). Tu punto de conexión dependerá de la URL de Braze para tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Crear una aplicación Braze en Grouparoo {#step-1-create-a-braze-app-in-grouparoo}

En Grouparoo, ve a **Apps** y selecciona **Braze** para crear una nueva aplicación Braze. En el modal que aparece, proporciona tu clave de API de Braze y el punto de conexión REST.

![El modal Crear aplicación Braze en Grouparoo, con campos para la clave de API de Braze y el punto de conexión REST.]({% image_buster /assets/img/grouparoo/add-app.png %})

### Paso 2: Configurar un modelo y un origen de datos {#step-2-set-up-a-model-and-data-source}

Esta integración requiere que tengas un modelo existente y un origen de datos configurado antes de continuar con el siguiente paso. Si no lo tienes configurado, visita la documentación de Grouparoo para aprender a configurar un [modelo](https://www.grouparoo.com/docs/config/models) y un [origen de datos](https://www.grouparoo.com/docs/config/sources).

### Paso 3: Crear un destino Braze en Grouparoo {#step-3-create-a-braze-destination-in-grouparoo}

#### Selecciona el modo de sincronización {#select-sync-mode}

En Grouparoo, selecciona tu modelo en la barra de navegación. A continuación, desplázate hasta la sección **Destinations** y haz clic en **Add new Destination**.

A continuación, selecciona la aplicación **Braze** que creaste, asigna un nombre al destino y selecciona el modo de sincronización que desees de entre los siguientes:
- **Sync**: Añade, actualiza y elimina usuarios de la empresa según sea necesario. Esta opción busca nuevos registros, cambios en registros existentes y eliminaciones.
- **Additive**: Añade y actualiza los usuarios de la empresa según sea necesario, pero no elimina a nadie. Esta opción busca nuevos usuarios para añadir a Braze y cambios en los usuarios de la empresa existentes, pero no realiza un seguimiento de las eliminaciones.
- **Enrich**: Solo actualiza los usuarios que ya existen en Braze. No añade ni elimina usuarios. Esta opción solo actualizará los usuarios existentes en Braze.

#### Mapeado de campos de propiedad {#property-field-mapping}

A continuación, debes mapear los campos de propiedad de Grouparoo a los campos de propiedad de Braze.

![Ejemplo de campos de mapeado de propiedades. El userID de Grouparoo está configurado para mapearse a external_id. email, firstName y lastName están configurados como campos equivalentes de Grouparoo "email", "first_name" y "last_name".]({% image_buster /assets/img/grouparoo/mapping.png %}){: style="max-width:80%;"}

Asegúrate de que el campo `external_id` de Braze esté mapeado a la clave primaria de tu tabla de origen. Mapea el resto de los campos según sea necesario para tu caso de uso.

Sección **Send Record Properties**: una lista de campos de perfil de usuario preestablecidos disponibles para mapear datos. Cualquiera de estos se puede sincronizar desde las propiedades de Grouparoo.

Sección **Optional Braze User Profile Fields**: crea campos de perfil de usuario de Braze personalizados opcionales. Si haces clic en **Add New Braze User Profile Field**, verás todas las propiedades disponibles que puedes mapear a Braze. El nombre de cualquier campo nuevo que crees será el mismo que el de la propiedad de Grouparoo, pero puedes cambiarle el nombre.

#### Grupos de Grouparoo {#grouparoo-groups}

Además del mapeado, también puedes optar por añadir grupos de Grouparoo a los grupos de suscripción de Braze.

![En "Braze Subscription Groups" de la ventana de configuración de destino de Grouparoo, el grupo de Grouparoo "High value with recent automotive purchase" se añadirá al grupo de suscripción de Braze "High value with recent automotive purchase".]({% image_buster /assets/img/grouparoo/lists.png %}){: style="max-width:80%;"}

{% alert important %}
Encontrarás más detalles y actualizaciones sobre esta integración en [la documentación de Grouparoo](https://www.grouparoo.com/docs/integrations/grouparoo-braze).
{% endalert %}