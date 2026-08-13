---
nav_title: Crear una transformación
article_title: Crear una transformación
page_order: 1
page_type: reference
description: "Este artículo de referencia proporciona los pasos para crear una transformación utilizando Transformación de datos de Braze."
---

# Crear una transformación {#create-a-transformation}

> Transformación de datos de Braze te permite crear y gestionar integraciones de webhook para automatizar el flujo de datos desde plataformas externas a Braze. Estas integraciones de webhook pueden impulsar casos de uso de marketing aún más sofisticados. Puedes crear tu Transformación de datos a partir del código predeterminado o utilizando nuestra biblioteca de plantillas dedicada para ayudarte a empezar con determinadas plataformas externas.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Autenticación de dos factores o SSO | Debes tener habilitada la [autenticación de dos factores]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#two-factor-authentication-2fa) (2FA) o el [inicio de sesión único]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#single-sign-on-sso-authentication) (SSO) para tu cuenta. |
| Permisos correctos | Debes ser administrador de la cuenta o del espacio de trabajo, o tener permisos de usuario para "Gestionar transformaciones". |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Paso 1: Identificar una plataforma de origen {#step-1-identify-a-source-platform}

Identifica una plataforma externa que quieras conectar a Braze y comprueba que la plataforma admite webhooks. Estas configuraciones a veces se denominan "notificaciones API" o "solicitudes de servicio web".

A continuación se muestra un ejemplo de [webhook de Typeform](https://www.typeform.com/help/a/webhooks-360029573471/), que se puede configurar iniciando sesión en su plataforma:

![Un ejemplo de carga útil de webhook de Typeform en la configuración de la plataforma Typeform.]({% image_buster /assets/img/data_transformation/data_transformation8.png %})

## Paso 2: Crear una transformación {#step-2-create-a-transformation}

{% multi_lang_include data_activation/create_transformation.md location="default" %}

## Paso 3: Enviar un webhook de prueba (recomendado) {#step-3-send-a-test-webhook-recommended}

Este paso es opcional, pero recomendamos enviar un webhook de prueba desde tu plataforma de origen a tu transformación recién creada.

1. Copia la URL de tu transformación.
2. En tu plataforma de origen, busca la función "Enviar prueba" para que genere un webhook de ejemplo y lo envíe a esta URL.
- Si tu plataforma de origen solicita un tipo de solicitud, selecciona **POST**.
- Si tu plataforma de origen proporciona opciones de autenticación, selecciona **No authentication**.
- Si tu plataforma de origen te pide secretos, selecciona **No secrets**.
3. Actualiza tu página en el panel de Braze para ver si se ha recibido el webhook. Si se ha recibido, deberías ver la carga útil del webhook en **Most recent webhook**.

Esto es lo que se ve para Typeform:

![Ejemplo de código de Transformación de datos que asigna el webhook a perfiles de usuario de Braze.]({% image_buster /assets/img/data_transformation/data_transformation11.png %})

{% alert note %}
Es posible que Transformación de datos de Braze aún no admita plataformas externas que requieran una verificación o autenticación especial para los webhooks. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="webhook authentication for external platforms" %}
{% endalert %}

## Paso 4: Escribir código de transformación {#step-4-write-transformation-code}

Si tienes poca o ninguna experiencia con código JavaScript o prefieres instrucciones más detalladas, sigue la pestaña **Principiante - POST: Track users** o **Principiante - PUT: Update multiple catalog items** para escribir tu código de transformación.

Si eres desarrollador o tienes mucha experiencia con código JavaScript, sigue la pestaña **Avanzado - POST: Track users** para obtener instrucciones de alto nivel sobre cómo escribir tu código de transformación.

{% alert tip %}
Para generar código de transformación con IA, elige **Code with Operator** en el editor de código de transformación. Para usarlo, se debe enviar un webhook a tu transformación. Para empezar con una plantilla prediseñada, elige **Insert Template**. Para ver ejemplos de prompts, consulta [Generar código de transformación de datos]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-data-transformation-code).

**Code with Operator** solo está disponible si Operator está habilitado para tu cuenta. Si no lo ves, ponte en contacto con tu director de cuentas.
{% endalert %}

{% tabs %}
{% tab Principiante - Seguimiento de usuarios %}

Aquí, escribe código de transformación para definir cómo asignar varios valores de webhook a perfiles de usuario de Braze.

1. Las nuevas transformaciones tienen esta plantilla predeterminada en la sección **Transformation Code**:

```java
// Here, we will define a variable, "brazecall", to build up a `/users/track` request
// Everything from the incoming webhook is accessible via the special variable "payload"
// So you can template in desired values in your `/users/track` request with dot notation, such as payload.x.y.z

let brazecall = {
  "attributes": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "attribute_1": payload.attribute_1
    }
  ],
  "events": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "name": payload.event_1,
      "time": new Date(),
      "properties": {
        "property_1": payload.event_1.property_1
      }
    }
  ],
  "purchases": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "product_id": payload.product_id,
      "currency": payload.currency,
      "price": payload.price,
      "quantity": payload.quantity,
      "time": payload.timestamp,
      "properties": {
        "property_1": payload.purchase_1.property_1
      }
    }
  ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{:start="2"}
2. Para incluir atributos personalizados, eventos personalizados y compras en tus llamadas de transformación, salta al paso 3. De lo contrario, elimina las secciones que no necesites.<br><br>
3. Cada objeto de atributo, evento y compra requiere un identificador de usuario, ya sea `external_id`, `user_alias`, `braze_id`, `email` o `phone`. Encuentra el identificador de usuario en la carga útil del webhook entrante y usa ese valor como plantilla en tu código de transformación a través de una línea de carga útil. Utiliza la notación de puntos para acceder a las propiedades del objeto de carga útil. <br><br>
4. Encuentra los valores del webhook que te gustaría representar como atributos, eventos o compras, y usa esos valores como plantilla en tu código de transformación a través de una línea de carga útil. Utiliza la notación de puntos para acceder a las propiedades del objeto de carga útil.<br><br>
5. Para cada objeto de atributo, evento y compra, examina el valor `_update_existing_only`. Establécelo en `false` si deseas que la transformación cree un nuevo usuario que puede no existir. Déjalo en `true` para actualizar solo los perfiles existentes.<br><br>
6. Haz clic en **Validate** para obtener una vista previa de la salida de tu código y comprobar si se trata de una solicitud aceptable de `/users/track`.<br><br>
7. Activa tu transformación. Para obtener ayuda adicional con tu código antes de activarlo, ponte en contacto con tu director de cuentas de Braze.<br><br>
7. Haz que tu plataforma de origen comience a enviar webhooks. Tu código de transformación se ejecutará para cada webhook entrante, y los perfiles de usuario comenzarán a actualizarse.

¡Tu integración de webhook ya está completa!

{% endtab %}
{% tab Principiante - Actualizar elementos del catálogo %}

Aquí puedes escribir código de transformación para definir cómo quieres asignar varios valores de webhook a actualizaciones de elementos del catálogo de Braze.

1. Las nuevas transformaciones incluirán esta plantilla predeterminada en la sección **Transformation Code**:

```java
// This is a default template that you can use as a starting point
// Feel free to delete this entirely to start from scratch, or to edit specific components

// First, this code defines a variable, "brazecall", to build a PUT /catalogs/{catalog_name}/items request
// Everything from the incoming webhook is accessible via the special variable "payload"
// As such, you can template in desired values in your request with JS dot notation, such as payload.x.y.z

let brazecall = {
  // For Braze Data Transformation to update Catalog items, the special variable "catalog_name" is required
  // This variable is used to specify the catalog name which would otherwise go in the request URL
  "catalog_name": "catalog_name",

  // After defining "catalog name", construct the Update Multiple Catalog Items request as usual below
  // Documentation for the destination endpoint: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/
  "items": [
    {
      "id": payload.item_id_1,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    },
    {
      "id": payload.item_id_2,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    },
    {
      "id": payload.item_id_3,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    }
  ]
};

// After the request body is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{:start="2"}
2. Las transformaciones para destinos `/catalogs` requieren un `catalog_name` para definir el catálogo específico que se va a actualizar. Puedes codificar este campo directamente o usar como plantilla un campo del webhook a través de una línea de carga útil. Utiliza la notación de puntos para acceder a las propiedades del objeto de carga útil.<br><br>
3. Define qué elementos quieres actualizar en el catálogo con los campos `id` de la matriz de elementos. Puedes codificar estos campos directamente o usar como plantilla un campo del webhook a través de una línea de carga útil. <br><br> Ten en cuenta que `catalog_column` es un valor de marcador de posición. Asegúrate de que los objetos de elementos solo contengan campos que existan en el catálogo.<br><br>
4. Selecciona **Validate** para obtener una vista previa de la salida de tu código y comprobar si es una solicitud aceptable para el [endpoint Actualizar varios elementos del catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items).<br><br>
5. Activa tu transformación. Para obtener ayuda adicional con tu código antes de activarlo, ponte en contacto con tu director de cuentas de Braze.<br><br>
6. Asegúrate de comprobar si tu plataforma de origen tiene una configuración para iniciar el envío de webhooks. Tu código de transformación se ejecutará para cada webhook entrante, y los elementos del catálogo comenzarán a actualizarse.

¡Tu integración de webhook ya está completa!

{% endtab %}
{% tab Avanzado - Seguimiento de usuarios %}

En este paso, transformarás la carga útil del webhook de la plataforma de origen en un valor de retorno de objeto JavaScript. Este valor de retorno debe seguir el formato del cuerpo de la solicitud del endpoint `/users/track`:

{% multi_lang_include data_transformation/transformation_code_requirements.md %}

Selecciona **Validate** para obtener una vista previa de la salida de tu código y comprobar si se trata de una solicitud aceptable de `/users/track`.

{% alert note %}
Actualmente no se admiten solicitudes de red externas, bibliotecas de terceros ni webhooks que no sean JSON.
{% endalert %}

{% endtab %}
{% endtabs %}

## Paso 5: Supervisar tu transformación {#step-5-monitor-your-transformation}

Tras activar tu transformación, consulta los análisis en la página principal de **Transformations** para ver un resumen del rendimiento.

* **Incoming Requests:** es el número de webhooks recibidos en la URL de esta transformación. Si las solicitudes entrantes son 0, tu plataforma de origen no ha enviado ningún webhook o no se puede establecer la conexión.
* **Deliveries:** tras recibir las solicitudes entrantes, Transformación de datos aplica tu código de transformación para enviarlas al destino de Braze seleccionado.

Es un buen objetivo que el 100 % de las solicitudes entrantes den lugar a entregas. El número de entregas nunca superará el número de solicitudes entrantes.

### Solución de problemas {#troubleshooting}

Para una supervisión y solución de problemas más detalladas, consulta la página **Logs** para ver registros específicos, que es donde se registran las últimas 1000 solicitudes entrantes a todas las transformaciones de tus espacios de trabajo. Puedes seleccionar cada registro para ver el cuerpo de la solicitud entrante, la salida de la transformación y el cuerpo de la respuesta del destino de la transformación.

Si no hay entregas, comprueba que tu código de transformación no contenga errores de sintaxis y confirma que el código se compila. A continuación, comprueba si la salida es una solicitud de destino válida.

Si el número de entregas es inferior al de solicitudes entrantes, esto indica que al menos algunos webhooks se entregan correctamente. Consulta los registros de transformación para ver ejemplos de errores y comprueba si la salida de la transformación es la esperada. Es posible que tu código de transformación no tenga en cuenta todas las variaciones de los webhooks recibidos.