---
nav_title: Realizar una llamada de Contenido conectado
article_title: Realizar una llamada a la API de Contenido conectado
page_order: 0
description: "Este artículo de referencia cubre cómo realizar una llamada a la API de Contenido conectado, así como ejemplos útiles y casos de uso avanzados de Contenido conectado."
search_rank: 2
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"}Realizar una llamada a la API de Contenido conectado {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomconnected-content-stylefloatrightwidth120pxborder0-classnoimgbordermake-a-connected-content-api-call}

> Usa Contenido conectado para insertar cualquier información accesible por API directamente en los mensajes que envías a los usuarios. Puedes extraer contenido directamente desde tu servidor web o desde API de acceso público.<br><br>Esta página cubre cómo realizar llamadas a la API de Contenido conectado, casos de uso avanzados de Contenido conectado, manejo de errores y más.

## Comprender el volumen de llamadas de Contenido conectado {#understanding-connected-content-call-volume}

{% alert important %}
Un envío no equivale a una llamada de Contenido conectado. Braze no garantiza una proporción 1:1 entre envíos de mensajes y solicitudes de Contenido conectado. El sistema está diseñado para priorizar la representación y entrega correcta de mensajes por encima de minimizar el número de llamadas. Tus puntos de conexión deben estar preparados para manejar más solicitudes que el número de destinatarios o mensajes enviados.
{% endalert %}

Braze puede realizar la misma llamada a la API de Contenido conectado más de una vez por destinatario. Las razones comunes incluyen:

- **Correo electrónico con múltiples partes:** Un solo correo electrónico puede desencadenar pases de representación separados para el cuerpo HTML, el cuerpo de texto plano y la versión de páginas móviles aceleradas (AMP) (si está presente). Cada pase puede desencadenar Contenido conectado en esa parte, por lo que un destinatario puede generar múltiples llamadas idénticas o similares.
- **Validación y reintentos:** Las cargas útiles de los mensajes pueden representarse múltiples veces por destinatario para validación, lógica de reintentos u otros propósitos internos.
- **Comportamiento del canal:** El Contenido conectado se ejecuta cuando el mensaje se representa. Para los mensajes dentro de la aplicación, el mensaje se representa en el momento de la impresión.

Si ves más llamadas de Contenido conectado en tus registros que envíos o destinatarios, ese comportamiento es esperado. Para orientación sobre cómo reducir la carga y planificar la escalabilidad, consulta [Mejores prácticas para puntos de conexión de alto volumen](#best-practices-for-high-volume-endpoints).

## Enviar una llamada de Contenido conectado {#sending-a-connected-content-call}

{% raw %}

Para enviar una llamada de Contenido conectado, usa la etiqueta `{% connected_content %}`. Con esta etiqueta, puedes asignar o declarar variables usando `:save`. Los aspectos de estas variables pueden referenciarse más adelante en el mensaje con [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid/).

Por ejemplo, el siguiente cuerpo de mensaje accederá a la URL `http://numbersapi.com/random/trivia` e incluirá un dato curioso en tu mensaje:

```
{% connected_content http://numbersapi.com/random/trivia :save result %}
Hi there, here is some fun trivia for you!: {{result.text}}
```

### Agregar variables {#adding-variables}

También puedes incluir atributos del perfil de usuario como variables en la cadena de URL al realizar solicitudes de Contenido conectado.

Por ejemplo, puedes tener un servicio web que devuelve contenido basado en la dirección de correo electrónico y el ID de un usuario. Si estás pasando atributos que contienen caracteres especiales, como el signo de arroba (@), asegúrate de usar el filtro Liquid `url_param_escape` para reemplazar cualquier carácter no permitido en las URL con sus versiones escapadas compatibles con URL, como se muestra en el siguiente atributo de dirección de correo electrónico.

```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
Los valores de los atributos deben estar rodeados por `${}` para funcionar correctamente dentro de nuestra versión de la sintaxis Liquid.
{% endalert %}

Las solicitudes de Contenido conectado solo admiten solicitudes GET y POST.

## Manejo de errores {#error-handling}

Si la URL no está disponible y llega a una página 404, Braze representará una cadena vacía en su lugar. Si la URL llega a una página HTTP 500 o 502, la URL fallará en la lógica de reintentos.

Si el punto de conexión devuelve JSON, puedes detectarlo verificando si el valor `connected` es nulo, y luego [abortar condicionalmente el mensaje]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content/). Braze solo permite URL que se comunican a través del puerto 80 (HTTP) y 443 (HTTPS).

### Detección de host no saludable {#unhealthy-host-detection}

El Contenido conectado emplea un mecanismo de detección de host no saludable para detectar cuándo el host de destino experimenta una alta tasa de lentitud significativa o sobrecarga, lo que resulta en tiempos de espera agotados, demasiadas solicitudes u otros resultados que impiden que Braze se comunique exitosamente con el punto de conexión de destino. Actúa como una protección para reducir la carga innecesaria que puede estar causando problemas al host de destino. También sirve para estabilizar la infraestructura de Braze y mantener velocidades de mensajería rápidas.

Si el host de destino experimenta una alta tasa de lentitud significativa o sobrecarga, Braze detendrá temporalmente las solicitudes al host de destino durante un minuto, simulando en su lugar respuestas que indican el fallo. Después de un minuto, Braze sondeará la salud del host usando un pequeño número de solicitudes antes de reanudar las solicitudes a velocidad completa si se determina que el host está saludable. Si el host aún no está saludable, Braze esperará otro minuto antes de intentar de nuevo.

Si las solicitudes al host de destino son detenidas por el detector de host no saludable, Braze continuará representando mensajes y siguiendo tu lógica Liquid como si hubiera recibido un código de respuesta de error. Si quieres asegurarte de que estas solicitudes de Contenido conectado se reintenten cuando son detenidas por el detector de host no saludable, usa la opción `:retry`. Para más información sobre la opción `:retry`, consulta [Reintentos de Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries/).

Si crees que la detección de host no saludable puede estar causando problemas, ponte en contacto con [soporte de Braze]({{site.baseurl}}/support_contact/).

{% alert note %}
Puedes agregar URL específicas a una lista de permitidos para ser usadas con Contenido conectado. Para acceder a esta característica, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

{% alert tip %}
Para más información sobre códigos de error comunes, consulta [Solución de problemas de solicitudes de webhook y Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content/#unhealthy-host-detection).
{% endalert %}

### Límites de velocidad (429) versus detección de host no saludable {#rate-limits-429-versus-unhealthy-host-detection}

Los siguientes son mecanismos diferentes:

- **429 Too Many Requests:** Tu punto de conexión (o un servicio upstream) está devolviendo esta respuesta. Significa que tu servidor o middleware está rechazando tráfico, a menudo porque tiene su propio límite de velocidad. Braze no aplica un límite de velocidad separado al Contenido conectado; el volumen de solicitudes de Contenido conectado escala directamente con tu [límite de velocidad de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-speed-rate-limiting). Debido a que los mensajes pueden representarse múltiples veces por destinatario (por ejemplo, para HTML de correo electrónico, texto plano y AMP), el número de solicitudes de Contenido conectado puede exceder ese límite de velocidad; no asumas que será menor o igual a los mensajes por minuto que configuraste. Si ves errores 429, escala tu punto de conexión o middleware para manejar el volumen de solicitudes esperado, o reduce el límite de velocidad de la campaña o paso en Canvas para que se envíen menos mensajes (y por lo tanto menos llamadas de Contenido conectado) por minuto.
- **Detección de host no saludable:** Una protección del lado de Braze que se activa después de una alta tasa y volumen de *fallos* en una ventana de un minuto. El conteo de fallos incluye los códigos de estado `408`, `429`, `502`, `503`, `504` y `529`. Cuando se activa, Braze detiene temporalmente las solicitudes a ese host y simula una respuesta de fallo. Esto es independiente de tu propio límite de velocidad. Para los umbrales de detección y más detalles, consulta [Solución de problemas de solicitudes de webhook y Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content/#unhealthy-host-detection). Para evitar activar la detección de host no saludable, asegúrate de que tu punto de conexión pueda manejar el volumen de llamadas descrito en [Comprender el volumen de llamadas de Contenido conectado](#understanding-connected-content-call-volume) y [Mejores prácticas para puntos de conexión de alto volumen](#best-practices-for-high-volume-endpoints).

## Permitir un rendimiento eficiente {#allowing-for-efficient-performance}

Dado que Braze entrega mensajes a una velocidad muy alta, asegúrate de que tu servidor pueda manejar miles de conexiones simultáneas para que no se sobrecargue al extraer contenido. Al usar API públicas, confirma que tu uso no violará ningún límite de velocidad que el proveedor de la API pueda emplear. Braze requiere que el tiempo de respuesta del servidor sea inferior a dos segundos por razones de rendimiento; si el servidor tarda más de dos segundos en responder, el contenido no se inserta.

Para más información sobre la planificación de la capacidad del punto de conexión y la reducción del volumen de llamadas, consulta [Mejores prácticas para puntos de conexión de alto volumen](#best-practices-for-high-volume-endpoints).

## Cosas que debes saber {#things-to-know}

* Braze no cobra por las llamadas a la API y no contarán para tu uso de puntos de datos.
* Hay un límite de 1 MB para las respuestas de Contenido conectado.
* El Contenido conectado se ejecuta cuando el mensaje se representa. Para los mensajes dentro de la aplicación, el mensaje se representa en el momento de la impresión.
* Las llamadas de Contenido conectado no siguen redirecciones.

## Mejores prácticas para puntos de conexión de alto volumen {#best-practices-for-high-volume-endpoints}

Si tus mensajes usan Contenido conectado y envías a alto volumen, planifica para más solicitudes que el número de destinatarios o envíos:

1. **Estima la carga máxima:** Usa un multiplicador conservador al dimensionar tu punto de conexión o middleware; las solicitudes de Contenido conectado pueden exceder el número de destinatarios o mensajes enviados. Por ejemplo, para correo electrónico, un solo destinatario puede generar múltiples llamadas (HTML, texto plano y AMP), por lo que destinatarios × 2 o × 3 se usa frecuentemente como una estimación conservadora.
2. **Usa caché cuando sea apropiado:** Las solicitudes GET se almacenan en caché de forma predeterminada. Para solicitudes POST, agrega `:cache_max_age` cuando la respuesta pueda reutilizarse durante un período (por ejemplo, token o contenido que no cambia por solicitud). Consulta [Almacenamiento en caché de respuestas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses/) y las [preguntas frecuentes sobre caché de POST](#what-is-caching-behavior) a continuación.
3. **Configura el límite de velocidad de entrega:** El [límite de velocidad de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-speed-rate-limiting) en campañas o pasos en Canvas es la única palanca para limitar indirectamente el volumen de solicitudes de Contenido conectado; Braze no limita la velocidad del Contenido conectado en sí. Es solo un proxy, y no uno perfecto, porque las solicitudes de Contenido conectado no son 1:1 con los mensajes. Úsalo para mantener el volumen de mensajes (y por lo tanto de Contenido conectado) dentro de lo que tu punto de conexión puede manejar.
4. **Diseña para idempotencia y reintentos:** Braze puede llamar a tu punto de conexión más de una vez por destinatario. Asegúrate de que tu punto de conexión pueda tolerar solicitudes duplicadas sin efectos secundarios incorrectos.

## Tipos de autenticación {#authentication-types}

### Usar autenticación básica {#using-basic-authentication}

Si la URL requiere autenticación básica, Braze puede almacenar una credencial de autenticación básica para que la uses en tu llamada a la API. Puedes administrar las credenciales de autenticación básica existentes y agregar nuevas en **Settings** > **Connected Content**.

![La configuración de Contenido conectado en el panel de Braze.]({% image_buster /assets/img/connected_content/basic_auth_mgmt.png %})

Para agregar una nueva credencial, selecciona **Add credential** > **Basic authentication**.

![Menú desplegable "Add credential" con la opción de usar autenticación básica o autenticación por token.]({% image_buster /assets/img/connected_content/add_credential_button.png %}){: style="max-width:60%"}

Dale un nombre a tu credencial e ingresa el nombre de usuario y la contraseña.

![La ventana "Create New Credential" con la opción de ingresar un nombre, nombre de usuario y contraseña.]({% image_buster /assets/img/connected_content/basic_auth_token.png %}){: style="max-width:60%"}

Luego puedes usar esta credencial de autenticación básica en tus llamadas a la API haciendo referencia al nombre del token:

{% raw %}
```
Hi there, here is some fun trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
Si eliminas una credencial, ten en cuenta que cualquier llamada de Contenido conectado que intente usarla será abortada.
{% endalert %}

Las credenciales almacenadas se aplican a las solicitudes {% raw %}`{% connected_content %}`{% endraw %} mientras Braze representa un mensaje. No se aplican a la solicitud HTTP principal configurada en un paso de [webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/#authentication-and-connected-content-credentials). Usa encabezados de solicitud o una etiqueta {% raw %}`{% connected_content %}`{% endraw %} dentro de un campo de encabezado o cuerpo de webhook cuando necesites recuperar secretos para esa llamada.

### Usar autenticación por token {#using-token-authentication}

Al usar Contenido conectado de Braze, puedes encontrar que ciertas API requieren un token en lugar de un nombre de usuario y contraseña. Braze también puede almacenar credenciales que contienen valores de encabezado de autenticación por token.

Para agregar una credencial que contenga valores de token, selecciona **Add credential** > **Token authentication**. Luego, agrega los pares clave-valor para los encabezados de tu llamada a la API y el dominio permitido.

![Un ejemplo de token "token_credential_abc" con detalles de autenticación por token.]({% image_buster /assets/img/connected_content/token_auth.png %}){: style="max-width:60%"}

Luego puedes usar esta credencial en tus llamadas a la API haciendo referencia al nombre de la credencial:

{% raw %}
```
{% assign campaign_name="New Year Sale" %}
{% connected_content
     https://api.endpoint.com/your_path
     :method post
     :auth_credentials token_credential_abc
     :body campaign={{campaign_name}}&customer={{${user_id}}}&channel=Braze
     :content_type application/json
     :save publication
%}
```
{% endraw %}

### Usar Open Authentication (OAuth) {#using-open-authentication-oauth}

Algunas configuraciones de API requieren la recuperación de un token de acceso que luego puede usarse para autenticar el punto de conexión de la API al que deseas acceder.

#### Paso 1: Recuperar el token de acceso {#step-1-retrieve-the-access-token}

El siguiente ejemplo ilustra la recuperación y el almacenamiento de un token de acceso en una variable local, que luego puede usarse para autenticar la llamada a la API subsiguiente. Se puede agregar un parámetro `:cache_max_age` para que coincida con el tiempo de validez del token de acceso y reducir el número de llamadas salientes de Contenido conectado. Consulta [Caché configurable]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/local_connected_content_variables/#configurable-caching) para más información.

{% raw %}
```
{% connected_content
     https://your_API_access_token_endpoint_here/
     :method post
     :auth_credentials access_token_credential_abc
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE"
     }
     :cache_max_age 900
     :save token_response
%}
```
{% endraw %}

#### Paso 2: Autorizar la API usando el token de acceso recuperado {#step-2-authorize-the-api-using-the-retrieved-access-token}

Después de que el token se guarda, puede insertarse dinámicamente como plantilla en la llamada subsiguiente de Contenido conectado para autorizar la solicitud:

{% raw %}
```
{% connected_content
     https://your_API_endpoint_here/
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE",
       "Authorization": "{{token_response}}"
     }
     :body key1=value1&key2=value2
     :save response
%}
```
{% endraw %}

### Editar credenciales {#editing-credentials}

Puedes editar el nombre de la credencial para los tipos de autenticación.

- Para autenticación básica, puedes actualizar el nombre de usuario y la contraseña. Ten en cuenta que la contraseña ingresada anteriormente no será visible.
- Para autenticación por token, puedes actualizar los pares clave-valor del encabezado y el dominio permitido. Ten en cuenta que los valores de encabezado configurados anteriormente no serán visibles.

![La opción para editar credenciales.]({% image_buster /assets/img/connected_content/edit_credentials.png %}){: style="max-width:60%"}

## Lista de IP permitidas de Contenido conectado {#connected-content-ip-allowlisting}

Cuando se envía un mensaje que usa Contenido conectado desde Braze, los servidores de Braze realizan automáticamente solicitudes de red a los servidores de nuestros clientes o de terceros para extraer datos. Con la lista de IP permitidas, puedes verificar que las solicitudes de Contenido conectado realmente provienen de Braze, agregando una capa de seguridad.

Braze enviará solicitudes de Contenido conectado desde los siguientes rangos de IP. Los rangos listados se agregan automática y dinámicamente a cualquier clave de API que haya sido habilitada para la lista de permitidos.

Braze tiene un conjunto reservado de IP usadas para todos los servicios, no todas las cuales están activas en un momento dado. Esto está diseñado para que Braze pueda enviar desde un centro de datos diferente o realizar mantenimiento, si es necesario, sin afectar a los clientes. Braze puede usar una, un subconjunto o todas las siguientes IP listadas al realizar solicitudes de Contenido conectado.

{% multi_lang_include data_centers.md datacenters='ips' %}

### Encabezado `User-Agent` {#user-agent-header}

Braze incluye un encabezado `User-Agent` en todas las solicitudes de Contenido conectado y webhook que es similar al siguiente:

```text
Braze Sender 75e404755ae1270441f07eb238f0faf25e44dfdc
```

{% alert tip %}
Ten en cuenta que el valor hash cambia regularmente. Si estás filtrando tráfico por `User-Agent`, permite todos los valores que comiencen con `Braze Sender`.
{% endalert %}

## Solución de problemas {#troubleshooting}

Usa [Webhook.site](https://webhook.site/) para solucionar problemas con tus llamadas de Contenido conectado y para diagnosticar problemas con los encabezados de solicitud, el cuerpo de la solicitud y otra información que se envía en la llamada.

1. Cambia la URL en tu llamada de Contenido conectado por la URL única generada en el sitio.
2. Previsualiza y prueba tu campaña o paso en Canvas para ver las solicitudes llegar a este sitio web.

También puedes verificar que la etiqueta Liquid incluya los parámetros que tu punto de conexión espera (por ejemplo, `:method`, `:headers`, `:content_type`, `:body` y `:basic_auth` cuando sea necesario). Si dependes de la clave de código de estado HTTP en un objeto JSON guardado, el punto de conexión debe devolver un objeto JSON y un estado `2XX`.

Para tasas de error altas desde tu host, revisa [Detección de host no saludable]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors/#unhealthy-host-detection) y [Volumen de llamadas de Contenido conectado](#understanding-connected-content-call-volume).

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Por qué hay más llamadas de Contenido conectado que usuarios o envíos? {#why-are-there-more-connected-content-calls-than-users-or-sends}

Braze puede realizar la misma llamada a la API de Contenido conectado más de una vez por destinatario para representar una carga útil de mensaje. Las cargas útiles de los mensajes pueden representarse múltiples veces por destinatario para validación, lógica de reintentos u otros propósitos internos. Sin embargo, ten en cuenta que solo una de las llamadas de Contenido conectado completa un mensaje.

Es esperado que una llamada a la API de Contenido conectado pueda realizarse más de una vez por destinatario, incluso si la lógica de reintentos no se usa en la llamada. Recomendamos configurar el límite de velocidad de cualquier mensaje que contenga Contenido conectado o configurar tus servidores para que puedan manejar mejor el volumen esperado que tiene en cuenta múltiples llamadas de Contenido conectado realizadas por envío de mensaje.

Consulta [Comprender el volumen de llamadas de Contenido conectado](#understanding-connected-content-call-volume) y [Mejores prácticas para puntos de conexión de alto volumen](#best-practices-for-high-volume-endpoints) para detalles y mitigación.

### ¿Cómo funciona el límite de velocidad con Contenido conectado? {#how-does-rate-limiting-work-with-connected-content}

El Contenido conectado no tiene su propio límite de velocidad. En su lugar, el límite de velocidad se basa en la tasa de envío de mensajes. Recomendamos configurar el límite de velocidad de mensajería por debajo de tu límite de velocidad previsto de Contenido conectado si hay más llamadas de Contenido conectado que mensajes enviados.

### ¿Cuál es el comportamiento de caché? {#what-is-caching-behavior}

Las solicitudes GET se almacenan en caché de forma predeterminada (consulta [Almacenamiento en caché de respuestas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses/)). **Las solicitudes POST no se almacenan en caché de forma predeterminada**, pero puedes habilitar el almacenamiento en caché agregando `:cache_max_age` a la llamada de Contenido conectado. Esto puede reducir la carga del punto de conexión cuando la misma solicitud POST (por ejemplo, una solicitud de token o contenido) se realizaría repetidamente dentro de la ventana de caché.

{% raw %}
```liquid
{% connected_content https://api.example.com/token :method post :body grant_type=client_credentials :cache_max_age 900 :save token %}
```
{% endraw %}

El almacenamiento en caché puede ayudar a reducir las llamadas duplicadas de Contenido conectado, pero no se garantiza que resulte en una sola llamada por usuario. La duración del caché es entre cinco minutos y cuatro horas. Para todos los detalles, consulta [Almacenamiento en caché de respuestas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses/).

### ¿Cuál es el comportamiento HTTP predeterminado de Contenido conectado? {#what-is-the-connected-content-http-default-behavior}

{% multi_lang_include connected_content.md section='default behavior' %}

{% multi_lang_include connected_content.md section='http post' %}

### ¿Qué sucede si uso la misma llamada de Contenido conectado en múltiples lugares? {#what-happens-if-i-use-the-same-connected-content-call-in-multiple-places}

Cada etiqueta de Contenido conectado se evalúa por separado, incluso si múltiples etiquetas usan la misma URL y parámetros. Cuando la URL y la configuración de caché lo permiten, las solicitudes idénticas pueden servirse desde el caché en lugar de desencadenar una nueva solicitud saliente (consulta [Almacenamiento en caché de respuestas]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses/) para más detalles).