---
nav_title: Postman y solicitudes de ejemplo
article_title: Postman y solicitudes de ejemplo
page_order: 3
description: "Este artículo de referencia cubre la colección Braze Postman, qué es, cómo configurar y utilizar la colección, así como cómo editar y enviar solicitudes."
page_type: reference
---

# Postman y solicitudes de ejemplo {#postman-and-sample-requests}

> Braze te permite generar solicitudes de API de ejemplo para todos nuestros endpoints a través de nuestra colección de Postman. Este artículo de referencia cubre la colección Braze Postman, qué es, cómo configurar y utilizar la colección, así como cómo editar y enviar solicitudes.

## ¿Qué es Postman? {#what-is-postman}

Postman es una herramienta de edición visual gratuita para crear y probar solicitudes de API. En comparación con otros métodos (por ejemplo, usar cURL), Postman te permite editar solicitudes de API, ver información de encabezados y mucho más. Puedes guardar colecciones (bibliotecas de solicitudes de API prediseñadas de ejemplo). Para acelerar la configuración con nuestra REST API, proporcionamos una colección con ejemplos prediseñados para todos los endpoints.

Consulta o descarga nuestra colección de Postman haciendo clic en **Run in Postman** en nuestra [documentación de Postman](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro) para comenzar.

## Uso de la colección de Postman de Braze {#using-the-braze-postman-collection}

Si tienes una cuenta de Postman (puedes descargar las versiones para macOS, Windows y Linux desde el [sitio web de Postman](https://www.getpostman.com)), puedes abrir nuestra documentación de Postman en tu propia aplicación de Postman haciendo clic en el botón naranja **Run in Postman**. A continuación, puedes [crear un entorno](#setting-up-your-postman-environment) o utilizar nuestro entorno de la REST API de Braze como plantilla, y editar las solicitudes `POST` y `GET` disponibles para adaptarlas a tus necesidades.

### Configuración de tu entorno de Postman {#setting-up-your-postman-environment}

{% raw %}
La colección de Postman de Braze utiliza una variable de plantilla, `{{instance_url}}`, para sustituir la URL de la REST API de tu instancia de Braze en las solicitudes preconstruidas, y la variable `{{api_key}}` para tu clave de API. En lugar de tener que editar manualmente todas las solicitudes de la colección, puedes configurar esta variable en tu entorno de Postman. Puedes seleccionar nuestro entorno con plantilla (Braze REST API Environment Template) en el menú desplegable y reemplazar los valores de las variables por los tuyos, o puedes configurar tu propio entorno.
{% endraw %}

Para configurar tu propio entorno, realiza los siguientes pasos:

1. Desde la pestaña **Workspaces**, selecciona **Environments**.
2. Haz clic en el botón **+** (más) para crear un nuevo entorno.
3. Dale un nombre a este entorno (por ejemplo, "Braze API Requests") y añade claves para `instance_url` y `api_key` con valores correspondientes a tu [instancia de Braze]({{site.baseurl}}/api/basics) y [clave de API REST de Braze]({{site.baseurl}}/api/basics).
4. Haz clic en **Save**.

{% alert note %}
En los cuerpos de las solicitudes `POST`, la `api_key` debe estar encapsulada entre comillas: `"MY-API-KEY-EXAMPLE"`. En las URL `GET`, no debe estarlo. Ya hemos proporcionado este formato en los cuerpos de solicitudes `POST`, las URL `GET` y la plantilla de entorno para `YOUR-API-KEY-HERE` de esta documentación.
{% endalert %}

![Adición de variables para la clave de API y la URL de instancia al entorno de la REST API de Braze en Postman.]({% image_buster /assets/img_archive/postman_variable.png %})

### Uso de las solicitudes preconstruidas de la colección {#using-the-pre-built-requests-from-the-collection}

Una vez que hayas configurado tu entorno, puedes utilizar cualquiera de las solicitudes preconstruidas en la colección como plantilla para crear nuevas solicitudes de API. Para empezar a utilizar una de las solicitudes preconstruidas, haz clic en ella dentro del menú **Collections** de Postman. Esto abrirá la solicitud como una nueva pestaña en la ventana principal de la aplicación de Postman.

En general, hay dos tipos de solicitudes que los endpoints de la API de Braze aceptan: `GET` y `POST`. Dependiendo del método `HTTP` que utilice el endpoint, tendrás que editar la solicitud preconstruida de forma diferente.

#### Editar una solicitud POST {#edit-a-post-request}

Al editar una solicitud `POST`, abre la solicitud y navega a la sección **Body** en el editor de solicitudes. Para mayor legibilidad, selecciona el botón de opción **raw** para dar formato al cuerpo de la solicitud `JSON`.

![Pestaña Body al editar una solicitud POST User Track en Postman]({% image_buster /assets/img_archive/postman_post.png %})

#### Editar una solicitud GET {#edit-a-get-request}

Al editar una solicitud `GET`, edita los parámetros pasados en la URL de la solicitud. Para ello, selecciona la pestaña **Params** y edita los pares clave-valor en los campos que aparecen.

![Pestaña Params al editar una solicitud GET de consulta de lista de direcciones de correo electrónico canceladas en Postman.]({% image_buster /assets/img_archive/postman_get.png %})

### Envía tu solicitud {#send-your-request}

Cuando tu solicitud de API esté lista, haz clic en **Send**. La solicitud se envía y los datos de respuesta se completan en una sección debajo del editor de solicitudes. Desde aquí, puedes ver los datos sin procesar devueltos por la API de Braze, ver el código de respuesta HTTP, ver cuánto tiempo tardó en procesarse la solicitud y consultar la información del encabezado.

![Ejemplo de datos de respuesta del cuerpo de una solicitud POST con un estado de 201 Created y un tiempo de respuesta de 269 milisegundos.]({% image_buster /assets/img_archive/postman_response.png %})