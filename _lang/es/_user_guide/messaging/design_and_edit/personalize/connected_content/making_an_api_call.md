---
nav_title: Realizar una llamada de contenido conectado
article_title: Realizar una llamada a la API de contenido conectado
page_order: 0
description: "Este artículo de referencia cubre cómo realizar una llamada a la API de contenido conectado, así como ejemplos útiles y casos de uso avanzados de contenido conectado."
search_rank: 2
toc_headers: h2
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"}Realizar una llamada a la API de contenido conectado {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomconnected-content-stylefloatrightwidth120pxborder0-classnoimgbordermake-a-connected-content-api-call}

> Usa contenido conectado para insertar cualquier información accesible por API directamente en los mensajes que envías a los usuarios. Puedes extraer contenido directamente desde tu servidor web o desde API de acceso público.<br><br>Esta página cubre cómo realizar llamadas a la API de contenido conectado, casos de uso avanzados de contenido conectado, manejo de errores y más.

## Acerca del volumen de llamadas de contenido conectado {#understanding-connected-content-call-volume}

{% alert important %}
Un envío no equivale a una llamada de contenido conectado. Braze no garantiza una proporción 1:1 entre envíos de mensajes y solicitudes de contenido conectado. El sistema está diseñado para priorizar la representación y entrega correcta de mensajes por encima de minimizar el número de llamadas. Tus endpoints deben estar preparados para manejar más solicitudes que el número de destinatarios o mensajes enviados.
{% endalert %}

Braze puede realizar la misma llamada a la API de contenido conectado más de una vez por destinatario. Las razones comunes incluyen:

- **Correo electrónico con múltiples partes:** Un solo correo electrónico puede desencadenar pases de representación separados para el cuerpo HTML, el cuerpo de texto plano y la versión de páginas móviles aceleradas (AMP) (si está presente). Cada pase puede desencadenar contenido conectado en esa parte, por lo que un destinatario puede generar múltiples llamadas idénticas o similares.
- **Validación y reintentos:** Las cargas útiles de los mensajes pueden representarse múltiples veces por destinatario para validación, lógica de reintentos u otros propósitos internos.
- **Comportamiento del canal:** El contenido conectado se ejecuta cuando el mensaje se representa. Para los mensajes dentro de la aplicación, el mensaje se representa en el momento de la impresión.

Si ves más llamadas de contenido conectado en tus registros que envíos o destinatarios, ese comportamiento es esperado. Para orientación sobre cómo reducir la carga y planificar la escalabilidad, consulta [Mejores prácticas para endpoints de alto volumen](#best-practices-for-high-volume-endpoints).

## Enviar una llamada de contenido conectado {#send-a-connected-content-call}

Para enviar una llamada de contenido conectado, usa la etiqueta {% raw %}`{% connected_content %}`{% endraw %}. Con esta etiqueta, puedes asignar o declarar variables usando `:save`. Los aspectos de estas variables pueden referenciarse más adelante en el mensaje con [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid).

### Desglose de la llamada a la API {#break-down-the-api-call}

El siguiente ejemplo usa la API Sunrise-Sunset e incluye la hora del amanecer de hoy en un mensaje:

{% raw %}
```
{% connected_content https://api.sunrise-sunset.org/v2?lat=40.7128&lng=-74.0060&date=today :save result %}
Hi there, today's sunrise in NYC is at {{result.sunrise}}.
```
{% endraw %}

Esto es lo que hace cada parte:

| Componente | Qué hace |
| --- | --- |
| Etiqueta `connected_content` | Indica a Braze que realice una solicitud HTTP mientras renderiza el mensaje. |
| `https://api.sunrise-sunset.org/v2` | El endpoint de la API al que Braze llama. |
| `lat=40.7128&lng=-74.0060` | Parámetros de consulta para las coordenadas de la ciudad de Nueva York. |
| `date=today` | Solicita datos del día actual en esas coordenadas. |
| `:save result` | Almacena la respuesta de la API en una variable local llamada `result`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Desglose de la llamada a la API" }

### Cómo funciona la respuesta de la API Sunrise-Sunset {#how-the-sunrise-sunset-api-response-works}

Este endpoint devuelve JSON con campos de nivel superior como `sunrise`, `sunset` y `tzid`. Los horarios se devuelven en la zona horaria de la ubicación de forma predeterminada (en este ejemplo, hora de Nueva York).

Por ejemplo, la forma de la respuesta es similar a:

```json
{
  "date": "2026-07-23",
  "tzid": "America/New_York",
  "sunrise": "2026-07-23T05:42:11-04:00",
  "sunset": "2026-07-23T20:21:32-04:00"
}
```

### Mapear la respuesta de la API a Liquid {#map-the-api-response-to-liquid}

Dado que la respuesta se guarda como `result`, puedes referenciar cada campo directamente desde ese objeto.

{% raw %}
```liquid
{{result.sunrise}}
{{result.sunset}}
{{result.tzid}}
```
{% endraw %}

Usa este patrón siempre que guardes JSON desde contenido conectado:

1. Guarda la respuesta de la API con `:save`.
2. Encuentra el campo que deseas en la respuesta JSON.
3. Referéncialo en Liquid como `saved_variable.field_name`.

### Añadir variables {#add-variables}

También puedes incluir atributos del perfil de usuario como variables en la cadena de URL al realizar solicitudes de contenido conectado.

Por ejemplo, puedes tener un servicio web que devuelve contenido basado en la dirección de correo electrónico y el ID de un usuario. Si estás pasando atributos que contienen caracteres especiales, como el signo de arroba (@), asegúrate de usar el filtro de Liquid `url_param_escape` para reemplazar cualquier carácter no permitido en las URL con sus versiones escapadas compatibles con URL, como se muestra en el siguiente atributo de dirección de correo electrónico.

{% raw %}
```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
Los valores de los atributos deben estar rodeados por `${}` para funcionar correctamente dentro de nuestra versión de la sintaxis de Liquid.
{% endalert %}

Las solicitudes de contenido conectado solo admiten solicitudes GET y POST.

## Manejo de errores {#error-handling}

Si la URL no está disponible y llega a una página 404, Braze muestra una cadena vacía en su lugar. Si la URL llega a una página HTTP 500 o 502, la URL falla en la lógica de reintento.

Si el endpoint devuelve JSON, puedes detectarlo comprobando si el valor `connected` es nulo y luego [cancelar condicionalmente el mensaje]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content). Braze solo permite URLs que se comunican a través del puerto 80 (HTTP) y 443 (HTTPS).

### Detección de host no saludable {#unhealthy-host-detection}

El contenido conectado emplea un mecanismo de detección de host no saludable para detectar cuándo el host de destino experimenta una alta tasa de lentitud significativa o sobrecarga, lo que resulta en tiempos de espera agotados, demasiadas solicitudes u otros resultados que impiden que Braze se comunique correctamente con el endpoint de destino. Actúa como una protección para reducir la carga innecesaria que puede estar causando problemas al host de destino. También sirve para estabilizar la infraestructura de Braze y mantener velocidades de mensajería rápidas.

Si el host de destino experimenta una alta tasa de lentitud significativa o sobrecarga, Braze detiene temporalmente las solicitudes al host de destino durante un minuto, simulando en su lugar respuestas que indican el fallo. Después de un minuto, Braze sondea la salud del host utilizando un pequeño número de solicitudes antes de reanudar las solicitudes a velocidad completa si se determina que el host está saludable. Si el host sigue sin estar saludable, Braze espera otro minuto antes de intentarlo de nuevo.

Si las solicitudes al host de destino son detenidas por el detector de host no saludable, Braze continúa renderizando mensajes y siguiendo tu lógica de Liquid como si hubiera recibido un código de respuesta de error. Si quieres asegurarte de que estas solicitudes de contenido conectado se reintenten cuando son detenidas por el detector de host no saludable, usa la opción `:retry`. Para más información sobre la opción `:retry`, consulta [Reintentos de contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries).

Si crees que la detección de host no saludable puede estar causando problemas, contacta con [soporte de Braze]({{site.baseurl}}/support_contact).

{% alert note %}
Puedes añadir URLs específicas a una lista de permitidos para ser utilizadas con contenido conectado. Para acceder a esta característica, contacta con tu administrador de éxito de cliente.
{% endalert %}

{% alert tip %}
Para más información sobre códigos de error comunes, consulta [Solucionar problemas de solicitudes de webhook y contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#unhealthy-host-detection).
{% endalert %}

### Límites de velocidad (429) versus detección de host no saludable {#rate-limits-429-versus-unhealthy-host-detection}

Los siguientes son mecanismos diferentes:

- **429 Too Many Requests:** Tu endpoint (o un servicio upstream) está devolviendo esta respuesta. Significa que tu servidor o middleware está rechazando tráfico, a menudo porque tiene su propio límite de velocidad. Braze no aplica un límite de velocidad separado al contenido conectado; el volumen de solicitudes de contenido conectado escala directamente con tu [límite de velocidad de entrega de mensajes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting). Dado que los mensajes pueden renderizarse múltiples veces por destinatario (por ejemplo, para HTML de correo electrónico, texto plano y AMP), el número de solicitudes de contenido conectado puede superar ese límite de velocidad; no asumas que será menor o igual a los mensajes por minuto que configures. Si ves errores 429, escala tu endpoint o middleware para manejar el volumen de solicitudes esperado, o reduce el [límite de velocidad de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) de la Campaign o Canvas para que se envíen menos mensajes (y por lo tanto menos llamadas de contenido conectado) por minuto.
- **Detección de host no saludable:** Una protección del lado de Braze que se activa después de una alta tasa y volumen de *fallos* en una ventana de un minuto. El conteo de fallos incluye los códigos de estado `408`, `429`, `502`, `503`, `504` y `529`. Cuando se activa, Braze detiene temporalmente las solicitudes a ese host y simula una respuesta de fallo. Esto es independiente de tu propio límite de velocidad. Para los umbrales de detección y más detalles, consulta [Solucionar problemas de solicitudes de webhook y contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#unhealthy-host-detection). Para evitar activar la detección de host no saludable, asegúrate de que tu endpoint pueda manejar el volumen de llamadas descrito en [Comprender el volumen de llamadas de contenido conectado](#understanding-connected-content-call-volume) y [Mejores prácticas para endpoints de alto volumen](#best-practices-for-high-volume-endpoints).

## Permitir un rendimiento eficiente {#allowing-for-efficient-performance}

Dado que Braze entrega mensajes a una velocidad muy alta, asegúrate de que tu servidor pueda manejar miles de conexiones simultáneas para que no se sobrecargue al extraer contenido. Al usar API públicas, confirma que tu uso no violará ningún límite de velocidad que el proveedor de la API pueda emplear. Braze requiere que el tiempo de respuesta del servidor sea inferior a dos segundos por razones de rendimiento; si el servidor tarda más de dos segundos en responder, el contenido no se inserta.

Para más información sobre la planificación de la capacidad del endpoint y la reducción del volumen de llamadas, consulta [Mejores prácticas para endpoints de alto volumen](#best-practices-for-high-volume-endpoints).

## Cosas que debes saber {#things-to-know}

- Braze no cobra por las llamadas a la API y no cuenta para tu uso de puntos de datos asignado.
- Hay un límite de 1 MB para las respuestas de contenido conectado.
- El contenido conectado se ejecuta cuando se renderiza el mensaje. Para los mensajes dentro de la aplicación, el mensaje se renderiza en el momento de la impresión.
- Las llamadas de contenido conectado no siguen redirecciones.

### Cómo se procesan las llamadas de contenido conectado {#how-connected-content-calls-are-processed}

Las llamadas de contenido conectado dentro de una sola plantilla de mensaje se ejecutan secuencialmente (de arriba a abajo) durante el renderizado de Liquid. Esto significa que las llamadas posteriores pueden hacer referencia a variables establecidas por llamadas anteriores. En este ejemplo, la primera llamada recupera datos de usuario y la segunda llamada utiliza esos datos para obtener preferencias:

{% raw %}
```liquid
{% connected_content https://api.example.com/user :save user_data %}
{% connected_content https://api.example.com/preferences?user_id={{user_data.id}} :save preferences %}
```
{% endraw %}

### Envío global y volumen de solicitudes {#global-sending-and-request-volume}

Aunque las llamadas de contenido conectado se ejecutan secuencialmente dentro de un solo mensaje, los mensajes se envían en paralelo a través de tus Campaigns y Canvas. Los envíos de alto volumen pueden generar un tráfico de solicitudes significativo hacia tus endpoints durante los períodos de envío pico. Para gestionar y limitar ese tráfico, incluyendo los límites de velocidad de mensajería del espacio de trabajo, la limitación de velocidad de entrega y el almacenamiento en caché, consulta [Mejores prácticas para endpoints de alto volumen](#best-practices-for-high-volume-endpoints).

## Prácticas recomendadas para endpoints de alto volumen {#best-practices-for-high-volume-endpoints}

Si tus mensajes utilizan contenido conectado y envías a gran volumen, planifica para más solicitudes que el número de destinatarios o envíos:

- **Estima la carga máxima:** Utiliza un multiplicador conservador al dimensionar tu endpoint o middleware: las solicitudes de contenido conectado pueden superar el número de destinatarios o mensajes enviados. Por ejemplo, para correo electrónico, un solo destinatario puede generar múltiples llamadas (HTML, texto plano y AMP), por lo que destinatarios × 2 o × 3 se usa a menudo como estimación conservadora.
- **Usa el almacenamiento en caché cuando sea apropiado:** Las solicitudes GET se almacenan en caché de forma predeterminada. Para solicitudes POST, añade `:cache_max_age` cuando la respuesta pueda reutilizarse durante un periodo (por ejemplo, un token o contenido que no cambia por solicitud). Consulta [Almacenamiento en caché de respuestas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses) y las [preguntas frecuentes sobre almacenamiento en caché de POST](#what-is-caching-behavior) en la siguiente sección.
- **Establece límites de velocidad de mensajes:** Los [límites de velocidad de mensajería del espacio de trabajo]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) y la [limitación de velocidad de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) en Campaigns o Canvas limitan indirectamente el volumen de solicitudes de contenido conectado; Braze no aplica límites de velocidad al contenido conectado en sí. Estos son valores aproximados, no exactos, porque las solicitudes de contenido conectado no tienen una relación 1:1 con los mensajes. Úsalos para mantener el volumen de mensajes (y, por tanto, de contenido conectado) dentro de lo que tu endpoint pueda manejar.
- **Diseña para idempotencia y reintentos:** Braze puede llamar a tu endpoint más de una vez por destinatario. Asegúrate de que tu endpoint pueda tolerar solicitudes duplicadas sin efectos secundarios incorrectos.

## Tipos de autenticación {#authentication-types}

### Uso de autenticación básica {#using-basic-authentication}

Si la URL requiere autenticación básica, Braze puede almacenar una credencial de autenticación básica para que la utilices en tu llamada a la API. Puedes gestionar las credenciales de autenticación básica existentes y añadir nuevas en **Configuración** > **Contenido conectado**.

![La configuración de contenido conectado en el panel de Braze.]({% image_buster /assets/img/connected_content/basic_auth_mgmt.png %})

Para añadir una nueva credencial, selecciona **Añadir credencial** > **Autenticación básica**.

![Desplegable "Añadir credencial" con la opción de usar autenticación básica o autenticación por token.]({% image_buster /assets/img/connected_content/add_credential_button.png %}){: style="max-width:60%"}

Asigna un nombre a tu credencial e introduce el nombre de usuario y la contraseña.

![La ventana "Crear nueva credencial" con la opción de introducir un nombre, nombre de usuario y contraseña.]({% image_buster /assets/img/connected_content/basic_auth_token.png %}){: style="max-width:60%"}

Después puedes usar esta credencial de autenticación básica en tus llamadas a la API haciendo referencia al nombre del token:

{% raw %}
```
Hi there, here is some fun trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
Si eliminas una credencial, ten en cuenta que cualquier llamada de contenido conectado que intente utilizarla será cancelada.
{% endalert %}

Las credenciales almacenadas se aplican a las solicitudes {% raw %}`{% connected_content %}`{% endraw %} mientras Braze renderiza un mensaje. No se aplican a la solicitud HTTP principal configurada en un paso de [webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#authentication-and-connected-content-credentials). Usa los encabezados de solicitud o una etiqueta {% raw %}`{% connected_content %}`{% endraw %} dentro de un campo de encabezado o cuerpo de webhook cuando necesites recuperar secretos para esa llamada.

### Uso de autenticación por token {#using-token-authentication}

Al usar contenido conectado de Braze, es posible que algunas API requieran un token en lugar de un nombre de usuario y una contraseña. Braze también puede almacenar credenciales que contengan valores de encabezado de autenticación por token.

Para añadir una credencial que contenga valores de token, selecciona **Añadir credencial** > **Autenticación por token**. Luego, añade los pares clave-valor para los encabezados de tu llamada a la API y el dominio permitido.

![Un ejemplo de token "token_credential_abc" con detalles de autenticación por token.]({% image_buster /assets/img/connected_content/token_auth.png %}){: style="max-width:60%"}

Después puedes usar esta credencial en tus llamadas a la API haciendo referencia al nombre de la credencial:

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

### Uso de Open Authentication (OAuth) {#use-open-authentication-oauth}

Algunas configuraciones de API requieren la obtención de un token de acceso que luego se puede usar para autenticar el endpoint de la API al que deseas acceder.

#### Paso 1: Obtener el token de acceso {#step-1-retrieve-the-access-token}

El siguiente ejemplo ilustra cómo obtener y guardar un token de acceso en una variable local, que luego se puede usar para autenticar la llamada a la API posterior. Se puede añadir un parámetro `:cache_max_age` para que coincida con el tiempo de validez del token de acceso y reducir el número de llamadas salientes de contenido conectado. Consulta [Almacenamiento en caché configurable]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses) para más información.

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

{% alert note %}
Cuando el endpoint del token espera `application/x-www-form-urlencoded` y pasas credenciales en `:body`, codifica en URL cualquier carácter especial en los valores de los parámetros. Por ejemplo, las barras diagonales (`/`) se convierten en `%2F` y los signos de suma (`+`) se convierten en `%2B`. Los caracteres especiales sin codificar pueden provocar que las solicitudes de token OAuth fallen.
{% endalert %}

#### Paso 2: Autorizar la API usando el token de acceso obtenido {#step-2-authorize-the-api-using-the-retrieved-access-token}

Una vez guardado el token, se puede insertar dinámicamente como plantilla en la llamada de contenido conectado posterior para autorizar la solicitud:

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

### Edición de credenciales {#editing-credentials}

Puedes editar el nombre de la credencial para los tipos de autenticación.

- Para la autenticación básica, puedes actualizar el nombre de usuario y la contraseña. Ten en cuenta que la contraseña introducida anteriormente no será visible.
- Para la autenticación por token, puedes actualizar los pares clave-valor del encabezado y el dominio permitido. Ten en cuenta que los valores de encabezado establecidos anteriormente no serán visibles.

## Lista de IP permitidas de contenido conectado {#connected-content-ip-allowlisting}

Cuando se envía un mensaje que utiliza contenido conectado desde Braze, los servidores de Braze realizan automáticamente solicitudes de red a los servidores de nuestros clientes o de terceros para obtener datos. Con la lista de IP permitidas, puedes verificar que las solicitudes de contenido conectado realmente provienen de Braze, añadiendo una capa de seguridad.

Braze enviará solicitudes de contenido conectado desde los siguientes rangos de IP. Los rangos enumerados se añaden automática y dinámicamente a cualquier clave de API que haya sido habilitada para la lista de permitidos.

Braze tiene un conjunto reservado de IP que se utilizan para todos los servicios, y no todas están activas en un momento dado. Esto está diseñado para que Braze pueda enviar desde un centro de datos diferente o realizar mantenimiento, si es necesario, sin afectar a los clientes. Braze puede utilizar una, un subconjunto o todas las siguientes IP enumeradas al realizar solicitudes de contenido conectado.

Si las solicitudes de contenido conectado devuelven consistentemente `403 Forbidden` y la autenticación está configurada correctamente, añade estas IP a la lista de permitidos en el servidor que recibe la solicitud. Un `403` también puede indicar permisos insuficientes o credenciales no válidas, así que confirma tanto la configuración de red como la de autenticación. Para orientación específica sobre webhooks, consulta [403 Forbidden y lista de IP permitidas]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#403-forbidden-and-ip-allowlisting).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### Uso de la lista de IP permitidas con Amazon S3 {#using-ip-allowlisting-with-amazon-s3}

Cuando utilices contenido conectado para recuperar archivos de Amazon S3, configura tu contenedor para permitir solicitudes HTTP `GET` no autenticadas desde las direcciones IP de Braze.

1. **Añade una política de contenedor con condiciones de IP:** Otorga `s3:GetObject` en los objetos de tu contenedor con `Principal: "*"` y una condición `IpAddress` que utilice los [rangos de IP de Braze](#connected-content-ip-allowlisting) para tu instancia. No necesitas establecer ACL de lectura pública en objetos individuales.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*",
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": ["{YOUR_BRAZE_IP_RANGE}"]
        }
      }
    }
  ]
}
```

Sustituye `{YOUR_BRAZE_IP_RANGE}` por los rangos de IP de Braze para tu instancia enumerados en [Lista de IP permitidas de contenido conectado](#connected-content-ip-allowlisting). Puedes añadir uno o más rangos como valores separados en el array `aws:SourceIp`.

{: start="2"}
2. **Revisa la configuración de bloqueo de acceso público de S3:** Las políticas de contenedor que utilizan `Principal: "*"` son tratadas como acceso público por AWS, incluso con condiciones de IP. Es posible que necesites permitir el acceso público basado en políticas de contenedor mientras mantienes bloqueado el acceso público basado en ACL.

3. **Usa la URL del objeto S3 en tu etiqueta de contenido conectado:** Haz referencia al objeto con su URL estándar de S3 (por ejemplo, `https://your-bucket.s3.amazonaws.com/path/to/object.json`).

Para más información sobre políticas de contenedor y claves de condición, consulta la [documentación de AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html).

### Encabezado `User-Agent` {#user-agent-header}

Braze incluye un encabezado `User-Agent` en todas las solicitudes de contenido conectado y webhooks que es similar al siguiente:

```text
Braze Sender 75e404755ae1270441f07eb238f0faf25e44dfdc
```

{% alert tip %}
Ten en cuenta que el valor del hash cambia regularmente. Si estás filtrando el tráfico por `User-Agent`, permite todos los valores que comiencen con `Braze Sender`.
{% endalert %}

## Solución de problemas {#troubleshooting}

Si tu llamada de contenido conectado no se renderiza correctamente o no se renderiza en absoluto, comprueba los siguientes detalles:

- **Confirma que se realizó una llamada de contenido conectado:** Puedes comprobar que se realizó una llamada en la [pestaña historial de mensajes]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab). También puedes hacer un envío de prueba de una única solicitud de contenido conectado.
- **Verifica a través de Postman o una solicitud CURL si la solicitud ideal tiene éxito:** Si la solicitud funciona y devuelve una respuesta, compara la solicitud en detalle (incluidos los encabezados). Confirma que los encabezados están capturados en pares clave-valor con comillas dobles.
- **Valida que la autorización se gestiona correctamente:** Confirma que se utiliza la opción `:basic_auth`/`:auth_credentials` y que se ha añadido la autorización de contenido conectado a la configuración del espacio de trabajo de contenido conectado. A veces, la URL de contenido conectado requiere encabezados más allá de la autenticación que deben introducirse.
- **Verifica que los datos están en un formato esperado:** Para el cuerpo de la respuesta, Braze analiza JSON válido en un objeto Liquid; de lo contrario, la respuesta se trata como texto plano (incluido HTML). La opción `:content_type` establece los encabezados `Content-Type` y `Accept` de salida en tu solicitud y no afecta al análisis de la respuesta. Para el `:body` de la solicitud, si tu JSON contiene espacios, sigue las indicaciones en la sección [Proporcionar cuerpo JSON]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/local_connected_content_variables#providing-json-body).
- **Confirma que los datos se han analizado correctamente:** Comprueba que Liquid hace referencia correctamente al campo esperado. Para JSON anidado, usa {% raw %}`{{sampleresult.data[0].sample_field}}`{% endraw %} para apuntar al campo anidado deseado. Puedes comprobar las propiedades del JSON anidado imprimiendo el resultado esperado con {% raw %}`RESPONSE:{{sampleresult.data}}`{% endraw %}.
- **Comprueba el código de estado de la respuesta:** El código de estado de la respuesta debe ser un código `2XX`. El contenido conectado no tiene forma de consumir la respuesta cuando el código no es `2XX`.

También puedes usar [Webhook.site](https://webhook.site/) para solucionar problemas con tus llamadas de contenido conectado y diagnosticar problemas con los encabezados de solicitud, el cuerpo de la solicitud y otra información que se envía en la llamada.

1. Cambia la URL en tu llamada de contenido conectado por la URL única generada en el sitio.
2. Previsualiza y prueba tu Campaign o paso en Canvas para ver las solicitudes llegar a este sitio web.

También puedes verificar que la etiqueta de Liquid incluya los parámetros que tu endpoint espera (por ejemplo, `:method`, `:headers`, `:content_type`, `:body` y `:basic_auth` cuando sea necesario). Si dependes de la clave del código de estado HTTP en un objeto JSON guardado, el endpoint debe devolver un objeto JSON y un estado `2XX`.

Para tasas de error altas de tu host, consulta [Detección de host en mal estado]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors#unhealthy-host-detection) y [Volumen de llamadas de contenido conectado](#understanding-connected-content-call-volume).

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Por qué hay más llamadas de contenido conectado que usuarios o envíos? {#why-are-there-more-connected-content-calls-than-users-or-sends}

Braze puede realizar la misma llamada a la API de contenido conectado más de una vez por destinatario para renderizar la carga útil de un mensaje. Las cargas útiles de los mensajes pueden renderizarse varias veces por destinatario para validación, lógica de reintentos u otros fines internos. Sin embargo, ten en cuenta que solo una de las llamadas de contenido conectado completa un mensaje.

Es esperable que una llamada a la API de contenido conectado se realice más de una vez por destinatario, incluso si la lógica de reintentos no se utiliza en la llamada. Recomendamos establecer el límite de velocidad de cualquier mensaje que contenga contenido conectado o configurar tus servidores para que puedan manejar mejor el volumen esperado que contempla múltiples llamadas de contenido conectado por envío de mensaje.

Consulta [Comprender el volumen de llamadas de contenido conectado](#understanding-connected-content-call-volume) y [Mejores prácticas para endpoints de alto volumen](#best-practices-for-high-volume-endpoints) para más detalles y mitigación.

### ¿Cómo funciona el límite de velocidad con el contenido conectado? {#how-does-rate-limiting-work-with-connected-content}

El contenido conectado no tiene su propio límite de velocidad. En su lugar, el límite de velocidad se basa en la tasa de envío de mensajes. Recomendamos establecer el límite de velocidad de mensajería más alto que tu límite de velocidad previsto para el contenido conectado si hay más llamadas de contenido conectado que mensajes enviados.

### ¿Cuál es el comportamiento de almacenamiento en caché? {#what-is-caching-behavior}

Las solicitudes GET se almacenan en caché de forma predeterminada (consulta [Almacenamiento en caché de respuestas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses)). **Las solicitudes POST no se almacenan en caché de forma predeterminada**, pero puedes habilitar el almacenamiento en caché añadiendo `:cache_max_age` a la llamada de contenido conectado. Esto puede reducir la carga del endpoint cuando la misma solicitud POST (por ejemplo, una solicitud de token o contenido) se realizaría repetidamente dentro de la ventana de caché.

{% raw %}
```liquid
{% connected_content https://api.example.com/token :method post :body grant_type=client_credentials :cache_max_age 900 :save token %}
```
{% endraw %}

El almacenamiento en caché puede ayudar a reducir las llamadas duplicadas de contenido conectado, pero no garantiza que se realice una sola llamada por usuario. La duración de la caché es de entre cinco minutos y cuatro horas. Para más detalles, consulta [Almacenamiento en caché de respuestas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses).

### ¿Cuál es el comportamiento HTTP predeterminado del contenido conectado? {#what-is-the-connected-content-http-default-behavior}

{% multi_lang_include connected_content/sections.md section='default behavior' %}

{% multi_lang_include connected_content/sections.md section='http post' %}

### ¿Qué sucede si uso la misma llamada de contenido conectado en varios lugares? {#what-happens-if-i-use-the-same-connected-content-call-in-multiple-places}

Cada etiqueta de contenido conectado se evalúa por separado, incluso si varias etiquetas usan la misma URL y los mismos parámetros. Cuando la URL y la configuración de caché lo permiten, las solicitudes idénticas pueden servirse desde la caché en lugar de desencadenar una nueva solicitud saliente (consulta [Almacenamiento en caché de respuestas]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses) para más detalles).