---
nav_title: OtherLevels
article_title: OtherLevels
alias: /partners/otherlevels/
description: "Este artículo cubre la integración entre OtherLevels Experience Platform y Braze."
page_type: partner
search_tag: OtherLevels

---

# OtherLevels

> [OtherLevels](https://www.otherlevels.com/) Experience Platform utiliza GenAI para transformar la forma en que las marcas deportivas, los editores y los operadores conectan con sus clientes, convirtiendo el contenido tradicional en experiencias personalizadas de video y rich media de marca a escala.

*Esta integración está mantenida por OtherLevels.*

## Resumen {#overview}

La integración de Braze y OtherLevels te permite crear videos GenAI personalizados a través de llamadas API a OtherLevels Experience Platform, y luego enviar estos videos a tus usuarios como videos push de iOS a través de [contenido conectado de Braze]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call).

Ofrece a tus usuarios una mejor experiencia con las experiencias potenciadas por IA de OtherLevels. Transforma el contenido existente y de terceros en video y rich media altamente escalables para audiencias que ya consumen contenido de forma diferente y responden con fuerza a las experiencias personalizadas contextualmente.

## Requisitos previos {#prerequisites}

Antes de empezar, necesitarás lo siguiente:

| Requisito          | Descripción                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Una cuenta de OtherLevels   | Se requiere una cuenta de OtherLevels para aprovechar esta asociación.                                                                     |
| Una clave de API REST de Braze  | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel de Braze desde **Configuración** > **Claves de API**. |
| Un endpoint REST de Braze | [La URL de tu endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Tu endpoint dependerá de la URL de Braze de tu instancia.                                                 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

Esta integración requiere llamar a la API de OtherLevels Experience Platform como parte del proceso de generación de video antes de que los mensajes puedan enviarse a tus usuarios desde Braze. Se proporcionan ejemplos cURL como parte de esta documentación; sin embargo, recomendamos usar clientes API como Postman para automatizar las llamadas API.

## Ejemplos {#use-cases}

Utiliza los videos GenAI creados con OtherLevels Experience Platform para:
- Crear mejores experiencias para propietarios y ligas deportivas, interacción con los aficionados, apuestas deportivas, iGaming y loterías.
- Amplificar tu marketing del cliente transformando el contenido basado en texto en rich media y video, creando experiencias humanas y atractivas.
- Elevar los resultados desde la adquisición hasta la retención ampliando, no retocando, tu integración de Braze existente.

## Integración de OtherLevels Experience Platform {#integrating-the-otherlevels-experience-platform}

### Paso 1: Llama a la API de OtherLevels Experience Platform para generar un video {#step-1}

El primer paso de la integración consiste en llamar a la API de OtherLevels Experience Platform para generar un nuevo video. Ten en cuenta que la generación de video no es instantánea. Dependiendo de la longitud y complejidad del video, el contenido puede tardar hasta media hora en generarse. Planifica tus calendarios de mensajería y llamadas a la API en consecuencia, de modo que las llamadas a la API para generar videos se realicen con suficiente antelación respecto a la hora en que está programado el envío de tus mensajes de Braze.

{% alert important %}
La siguiente solicitud utiliza cURL. Para una gestión más eficiente de las solicitudes de API, recomendamos usar un cliente de API como Postman.
{% endalert %}

Consulta el siguiente ejemplo para saber cómo estructurar tu llamada a la API. Para más información sobre cómo personalizar los detalles del video y estructurar tu llamada a la API, consulta [Personalizar el video GenAI](#customizing-the-genai-video).

{% raw %}
```bash
curl --request POST \
  --url 'https://exp-platform-api.prod.awsotherlevels.com/v1/app/OTHERLEVELS_PROJECT_KEY/media?=' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/10.3.0' \
  --data '{
    "task": {
        "type": "tasks",
        "tasks": {
            "image_video_overlay": {
                "width": "= .orientation == '\''portrait'\'' ? '\''1080'\'' : .orientation == '\''landscape'\'' ? '\''1920'\''",
                "height": "= .orientation == '\''portrait'\'' ? '\''1920'\'' : .orientation == '\''landscape'\'' ? '\''1080'\''",
                "color": "255,255,255,0",
                "y_pos": "0",
                "x_pos": "0",
                "image_input": "= tasks.resize_image.jpg ?? tasks.resize_image.png",
                "video_input": "= tasks.talking_talent_replace_bg.mp4",
                "type": "compose.ImageVideoOverlay"
            },
            "resize_image": {
                "media_input": "= tasks.bg_image.jpg ?? tasks.bg_image.png",
                "type": "compose.MediaResize",
                "width": "= .orientation == '\''portrait'\'' ? '\''1080'\'' : .orientation == '\''landscape'\'' ? '\''1920'\''",
                "height": "= .orientation == '\''portrait'\'' ? '\''1920'\'' : .orientation == '\''landscape'\'' ? '\''1080'\''"
            },
            "bg_image": {
                "type": "load",
                "url": "BACKGROUND_IMAGE_URL",
                "refresh_interval": "12h"
            },
            "talking_head": {
                "test": false,
                "title": "INSERT_TITLE",
                "caption": false,
                "templateId": "TALENT_TEMPLATE",
                "type": "TALENT_MODEL",
                "variables": {
                    "script": {
                        "name": "script",
                        "properties": {
                            "content": "= tasks.translate_text.text"
                        },
                        "type": "text"
                    }
                }
            },
            "translate_text": {
                "type": "translate_text",
                "source": "en",
                "target": "en",
                "text": "INSERT_SCRIPT"
            },
            "talking_talent_speed": {
                "type": "compose.VideoSetSpeed",
                "speed": "1.0",
                "video_input": "= tasks.talking_head.mp4"
            },
            "talking_talent_replace_bg": {
                "type": "compose.VideoReplaceBg",
                "video_background": "= tasks.resize_image.jpg ?? tasks.resize_image.png",
                "video_input": "= tasks.talking_talent_speed.mp4"
            }
        },
        "output": "image_video_overlay"
    }
}'
```
{% endraw %}

Sustituye lo siguiente:

| Marcador de posición          | Descripción                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `OTHERLEVELS_PROJECT_KEY`   | Se te proporcionará una clave de proyecto de OtherLevels cuando se te aprovisione con una cuenta de OtherLevels.                                                                     |
| `BACKGROUND_IMAGE_URL`  | Una URL HTTPS para el fondo del video. |
| `INSERT_TITLE` | El título del video; es una referencia interna y no se mostrará en el video.                                                 |
| `TALENT_TEMPLATE` | Un ID de plantilla de talento. OtherLevels trabajará contigo durante el aprovisionamiento de la cuenta para crear un talento (avatar). Se te proporcionará uno o varios ID de talento que podrás utilizar.                                                 |
| `TALENT_MODEL` | Un ID de modelo de talento. OtherLevels trabajará contigo durante el aprovisionamiento de la cuenta para crear un talento (avatar). Se te proporcionarán uno o varios modelos de talento que podrás utilizar.                                                 |
| `INSERT_SCRIPT` | El guion exacto que te gustaría que el talento diga durante el video.                                                 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 1: Llama a la API de OtherLevels Experience Platform para generar un video" }

Como parte de la respuesta de la API, OtherLevels devolverá una carga útil JSON que indica una llamada a la API exitosa. El JSON contendrá un `recipe_id` único para identificar el video generado. El `recipe_id` será necesario en el siguiente paso.

Aquí tienes un ejemplo de respuesta de la API:

{% raw %}
```bash
{"$schema":"https://exp-platform-api.prod.awsotherlevels.com/schemas/GenerateMediaResBody.json","message":"success","recipe_id":"LMINHWXV2BBD6JGV5VF3ZNZV7BDDRR7FH5FJH6MMX4BVLTPRKTWQ","media_short_id":"LMINHWX","status":"triggered"}
```
{% endraw %}

### Paso 2: Configurar el `recipe_id` como atributo personalizado {#step-2-setting-the-recipe_id-as-a-custom-attribute}

El `recipe_id` que recibes del [paso 1](#step-1) se establece ahora como atributo personalizado de Braze para el usuario o usuarios a los que deseas enviar los videos.

Según tu caso de uso, puede que hayas generado un único video destinado a una gran audiencia, en cuyo caso este mismo `recipe_id` puede configurarse para varios usuarios. Alternativamente, puede que hayas generado múltiples videos únicos, cada uno dirigido a un usuario diferente, en cuyo caso cada usuario debería tener su `recipe_id` personalizado configurado como atributos personalizados de Braze.

{% alert important %}
La siguiente solicitud utiliza cURL. Para una gestión más eficiente de las solicitudes de API, recomendamos usar un cliente de API como Postman.
{% endalert %}

{% raw %}
```bash
curl --location --request POST 'BRAZE_API_ENDPOINT/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer BRAZE_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "USER_ID",
      "olxpmedia": "RECIPE_ID"
    }
  ]
}'
```
{% endraw %}

Sustituye lo siguiente:

| Marcador de posición             | Descripción                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT`    | La URL del endpoint REST de Braze de tu instancia de Braze actual. Para más información, consulta [Claves de API REST]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab#rest-api-keys). |
| `BRAZE_API_KEY`         | Tu clave de API REST de Braze con el permiso `users.track`.                                                                                                                                      |
| `USER_ID`              | El ID de usuario que recibirá este video en particular. Para más ejemplos de los identificadores que pueden utilizarse, consulta [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track).                                                                                                                                                  |
| `RECIPE_ID`       | El `recipe_id` recibido de la respuesta de la API de OtherLevels en el [paso 1](#step-1).                                                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Configurar el recipe_id como atributo personalizado" }

### Paso 3: Envío a través de contenido conectado de Braze {#step-3-sending-through-braze-connected-content}

Para enviar los videos GenAI como mensajes push de iOS a tus usuarios, sigue estos pasos:

1. Crea una campaña de notificaciones push de iOS en Braze.
2. Mientras redactas tu campaña, ve a la sección **Activos** y pega la siguiente sintaxis de contenido conectado en el campo **Añadir desde URL**.

{% raw %}
```
{% connected_content https://exp-platform-api-external.prod.awsotherlevels.com/v1/app/OTHERLEVELS_PROJECT_KEY/media/{{custom_attribute.${olxpmedia}}} %}
```
{% endraw %}

A continuación, sustituye `OTHERLEVELS_PROJECT_KEY` por la clave del proyecto proporcionada por OtherLevels.

{: start="3"}
3. En el desplegable de **Formato de archivo de URL**, selecciona **MP4**.
4. Configura el resto de la campaña (como el contenido del mensaje, el calendario de envío y el público objetivo) según tus preferencias.

![Ejemplo de campos de activos para contenido conectado.]({% image_buster /assets/img/otherlevels/1.png %})

## Personalizar el video GenAI {#customizing-the-genai-video}

### Tamaño y atributos del video {#video-size-and-attributes}

El fondo del video se puede especificar dentro de la clave `bg_image`.

| Parámetro             | Descripción                  |
|-------------------------|----------------------------|
| `url`    | URL HTTPS para la imagen de fondo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tamaño y atributos del video" }

El tamaño del fondo del video se puede especificar dentro de la clave `resize_image`. Recomendamos que la imagen de fondo tenga el mismo tamaño que el configurado aquí.

| Parámetro             | Descripción                  |
|-------------------------|----------------------------|
| `width`    | Anchura de la imagen de fondo, con opciones para los modos vertical y horizontal. |
| `height`     | Altura de la imagen de fondo, con opciones para los modos vertical y horizontal.                              |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tamaño y atributos del video" }

Las opciones de superposición de video se pueden especificar dentro de la clave `image_video_overlay`.

| Parámetro             | Descripción                  |
|-------------------------|----------------------------|
| `width`    | Anchura de la superposición, con opciones para los modos vertical y horizontal. |
| `height`         | Altura de la superposición, con opciones para los modos vertical y horizontal.                                              |
| `color`              | Color de la superposición especificado en RGB junto con la transparencia del video.                                                                   |
| `y_pos`       | Desplazamiento del eje Y desde el centro.                                                              |
| `x_pos`    | Desplazamiento del eje X desde el centro. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tamaño y atributos del video" }

### Talento y guion {#talent-and-script}

Como parte del aprovisionamiento, OtherLevels trabajará contigo para generar uno o varios talentos (a veces denominados avatares) para utilizarlos en tus videos. Dependiendo de tu caso de uso y de tu marca, puede adoptar la forma de uno de tus embajadores de marca existentes o de una creación única.

Una vez creados, se te proporcionarán los ID utilizables `TALENT_TEMPLATE` y `TALENT_MODEL` para que los uses con nuestra API.

El modelo de voz utilizado para procesar guiones de entrada funciona mejor cuando se proporciona un guion natural que leería un humano. En la mayoría de los casos, no necesitas puntuación adicional para guiar manualmente el guion. Sin embargo, recomendamos que pruebes todos tus guiones antes de enviarlos a una audiencia real. La velocidad a la que el talento lee el guion se puede especificar dentro de la clave `talking_talent_speed`.

| Parámetro             | Descripción                  |
|-------------------------|----------------------------|
| `speed`    | Especifica la velocidad a la que el talento leerá el guion. Por ejemplo, `1.5`.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Talento y guion" }

## Consideraciones adicionales {#additional-considerations}

- Solo la plataforma de notificaciones push de iOS admite de forma nativa medios de video. Las notificaciones push de Android no admiten videos de forma nativa, por lo que esta integración solo puede utilizarse con tu audiencia de iOS.
- Al recibir notificaciones push de video en dispositivos iOS, los usuarios deben mantener pulsada la notificación push para que el video se cargue y se reproduzca. Este es un comportamiento estándar en la plataforma iOS y no se puede personalizar.