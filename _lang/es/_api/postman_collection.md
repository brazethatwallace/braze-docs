---
nav_title: Postman y solicitudes de ejemplo
article_title: Postman y solicitudes de ejemplo
page_order: 3
description: "Este artículo de referencia cubre la colección Braze Postman, qué es, cómo configurar y utilizar la colección, así como cómo editar y enviar solicitudes."
page_type: reference

---

# Postman y solicitudes de ejemplo {#postman-and-sample-requests}

> Braze te permite generar solicitudes de API de ejemplo para todos nuestros puntos finales a través de nuestra colección de Postman. Este artículo de referencia cubre la colección Braze Postman, qué es, cómo configurar y utilizar la colección, así como cómo editar y enviar solicitudes.

## ¿Qué es Postman? {#what-is-postman}

Postman es una herramienta gratuita de edición visual para crear y probar solicitudes de API. En comparación con otros métodos (por ejemplo, usando cURL), Postman te permite editar solicitudes de API, ver información de encabezados y mucho más. Puedes guardar colecciones (bibliotecas de solicitudes de API de ejemplo prefabricadas). Para acelerar la configuración con nuestra REST API, proporcionamos una colección con ejemplos prefabricados para todos los puntos finales.

Consulta o descarga nuestra colección de Postman haciendo clic en **Run in Postman** en nuestra [documentación de Postman](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro) para empezar.

## Uso de la colección Braze Postman {#using-the-braze-postman-collection}

Si tienes una cuenta de Postman (puedes descargar las versiones para macOS, Windows y Linux desde el [sitio web de Postman](https://www.getpostman.com)), puedes abrir nuestra documentación de Postman en tu propia aplicación de Postman haciendo clic en el botón naranja **Run in Postman**. A continuación, puedes [crear un entorno](#setting-up-your-postman-environment), o usar nuestro entorno Braze REST API como plantilla, y editar las solicitudes `POST` y `GET` disponibles para adaptarlas a tus propias necesidades.

### Configuración del entorno Postman {#setting-up-your-postman-environment}

{% raw %}
La colección Braze Postman utiliza una variable de plantilla, `{{instance_url}}`, para sustituir la URL de la REST API de tu instancia de Braze en las solicitudes preconstruidas, y la variable `{{api_key}}` para tu clave de API. En lugar de tener que editar manualmente todas las solicitudes de la colección, puedes configurar esta variable en tu entorno Postman. Puedes seleccionar nuestra plantilla de entorno (Braze REST API Environment Template) en el menú desplegable y sustituir los valores de las variables por los tuyos propios, o puedes configurar tu propio entorno.
{% endraw %}

Para configurar tu propio entorno, realiza los siguientes pasos:

1. En la pestaña **Workspaces**, selecciona **Environments**.
2. Haz clic en el botón **+** (más) para crear un nuevo entorno.
3. Dale un nombre a este entorno (por ejemplo, "Braze API Requests") y añade claves para `instance_url` y `api_key` con los valores correspondientes a tu [instancia de Braze]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints) y [clave de API REST de Braze]({{site.baseurl}}/api/api_key).
4. Haz clic en **Save**.

{% alert note %}
En los cuerpos de solicitud `POST`, `api_key` debe ir entre comillas: `"MY-API-KEY-EXAMPLE"`. En las URL de `GET`, no debe ir entre comillas. Ya te hemos proporcionado este formato en los cuerpos de solicitud `POST`, las URL `GET` y la plantilla de entorno para `YOUR-API-KEY-HERE` de esta documentación.
{% endalert %}

![Añadir variables para la clave de API y la URL de instancia al entorno Braze REST API en Postman.]({% image_buster /assets/img_archive/postman_variable.png %})

### Uso de las solicitudes preconstruidas de la colección {#using-the-pre-built-requests-from-the-collection}

Una vez que hayas configurado tu entorno, puedes usar cualquiera de las solicitudes preconstruidas de la colección como plantilla para crear nuevas solicitudes de API. Para empezar a usar una de las solicitudes preconstruidas, haz clic en ella dentro del menú **Collections** de Postman. Esto abrirá la solicitud como una nueva pestaña en la ventana principal de la aplicación Postman.

En general, hay dos tipos de solicitudes que aceptan los puntos finales de la API de Braze: `GET` y `POST`. Dependiendo del método `HTTP` que utilice el punto de conexión, tendrás que editar la solicitud preconstruida de forma diferente.

#### Editar una solicitud POST {#edit-a-post-request}

Para editar una solicitud `POST`, abre la solicitud y navega a la sección **Body** en el editor de solicitudes. Para facilitar la lectura, selecciona el botón de opción **raw** para dar formato al cuerpo de la solicitud `JSON`.

![Pestaña Body al editar una solicitud POST User Track en Postman]({% image_buster /assets/img_archive/postman_post.png %})

#### Editar una solicitud GET {#edit-a-get-request}

Al editar una solicitud `GET`, edita los parámetros pasados en la URL de la solicitud. Para ello, selecciona la pestaña **Params** y edita los pares clave-valor en los campos que aparecen.

![Pestaña Params al editar una solicitud GET Query List of Unsubscribed Email Addresses en Postman.]({% image_buster /assets/img_archive/postman_get.png %})

### Envía tu solicitud {#send-your-request}

Cuando tu solicitud de API esté lista, haz clic en **Send**. La solicitud se envía y los datos de respuesta se muestran en una sección debajo del editor de solicitudes. Desde aquí, puedes ver los datos sin procesar devueltos por la API de Braze, el código de respuesta HTTP, el tiempo que tardó en procesarse la solicitud y la información del encabezado.

![Ejemplo de datos de respuesta del cuerpo de una solicitud POST con un estado de 201 Created y un tiempo de respuesta de 269 milisegundos.]({% image_buster /assets/img_archive/postman_response.png %})