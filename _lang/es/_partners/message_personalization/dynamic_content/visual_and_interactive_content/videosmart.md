---
nav_title: VideoSmart
article_title: VideoSmart
description: "Este artículo de referencia describe la integración entre Braze y VideoSmart, una tecnología de video personalizado e interactivo que permite a las marcas entregar contenido basado en datos y no lineal a escala."
alias: /partners/videosmart/
page_type: partner
search_tag: Partner
---

# VideoSmart

> [VideoSmart](https://www.videosmart.com/) ofrece tecnología de video personalizado e interactivo que te permite entregar contenido basado en datos y no lineal a escala. Cada video se genera dinámicamente utilizando datos a nivel de cliente, lo que permite mensajería personalizada y recorridos de usuario dentro de una única experiencia de video.
>
> La integración de VideoSmart te permite incrustar contenido de video personalizado en campañas de correo electrónico utilizando contenido conectado de Braze y plantillas Liquid para solicitar activos de video de VideoSmart. Esta integración se implementa normalmente a través de una plantilla reutilizable de bloque de contenido de Braze, lo que permite un despliegue consistente entre campañas y al mismo tiempo ofrece flexibilidad en la selección de campañas y la lógica de personalización.

_Esta integración es desarrollada y mantenida por VideoSmart._

## Acerca de esta integración {#about-this-integration}

VideoSmart se integra con Braze para generar dinámicamente activos de video personalizados en el momento del envío, que luego se incrustan directamente en el contenido de correo electrónico de tus Campaign y Canvas en Braze.

En Braze, seleccionas la Campaign de VideoSmart correspondiente y envías atributos del cliente (mediante plantillas Liquid) a VideoSmart cuando realizas el envío. Estos atributos se utilizan para renderizar una experiencia de video única y personalizada para cada destinatario. A continuación, puedes usar contenido conectado de Braze para solicitar URLs de video o activos de la API de VideoSmart en tiempo real, lo que permite la personalización a gran escala.

Esta integración está diseñada para mensajes de correo electrónico de Braze que admiten plantillas Liquid y contenido conectado, y se puede configurar para funcionar con atributos estándar del perfil de usuario de Braze o campos de datos personalizados.

## Ejemplos {#use-cases}


Los ejemplos comunes incluyen los siguientes:

- Incorporación de clientes y recorridos de bienvenida
- Educación financiera (como pensiones y pólizas de seguros)
- Estados de cuenta anuales y comunicaciones regulatorias
- Campaigns de conocimiento de producto y venta cruzada
- Campaigns de retención y reactivación de clientes
- Recordatorios de carrito abandonado: cuando un cliente agrega productos a su carrito pero no realiza la compra, envías un correo electrónico con un video personalizado que destaca los artículos que dejó atrás
- Seguimientos posteriores a la compra: después de una compra, envía un video de agradecimiento personalizado y recomienda productos relacionados

## Requisitos previos {#prerequisites}

Antes de comenzar, confirma que tienes lo siguiente:

| Requisito                        | Descripción                                                                                                                 |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Credenciales de contenido conectado de Braze | Una credencial de autenticación básica de contenido conectado llamada **basic_credentials**, configurada con los valores proporcionados por VideoSmart |
| Plantilla de **VideoSmart Content Block**   | La plantilla de **VideoSmart Content Block** añadida a tu panel de Braze (proporcionada por VideoSmart)                                |
| Un mensaje de correo electrónico de Braze               | Un correo electrónico de Campaign de Braze o un paso de correo electrónico en Canvas donde insertarás el **VideoSmart Content Block**                              |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Sigue estos pasos para habilitar el **bloque de contenido de VideoSmart** y usarlo en un correo electrónico.

### Paso 1: Configura la plantilla del bloque de contenido de VideoSmart en Braze {#step-1-set-up-the-videosmart-content-block-template-in-braze}

Solicita la plantilla del **bloque de contenido de VideoSmart** a tu representante de VideoSmart y agrégala a tu panel de Braze.

VideoSmart proporcionará las credenciales para la autenticación de contenido conectado que utiliza el Content Block.

### Paso 2: Configura la autenticación de contenido conectado {#step-2-set-up-connected-content-authentication}

Crea una credencial de autenticación básica de contenido conectado en Braze llamada "basic_credentials".

- Sigue las instrucciones en [Uso de la autenticación básica]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call#using-basic-authentication).
- Usa el nombre de usuario y la contraseña proporcionados por VideoSmart.

### Paso 3: Agrega el Content Block a tu correo electrónico {#step-3-add-the-content-block-to-your-email}

Inserta el **bloque de contenido de VideoSmart** en tu correo electrónico donde desees que aparezca el contenido de video.

En la mayoría de las configuraciones de Braze, los Content Blocks se referencian usando el siguiente patrón (reemplaza "VideoSmart_Campaign" con el nombre del Content Block en tu cuenta):

{% raw %}`{{content_blocks.${VideoSmart_Campaign}}}`{% endraw %}

{% alert important %}
El nombre del Content Block distingue entre mayúsculas y minúsculas y debe coincidir exactamente con lo que has configurado en Braze.
{% endalert %}

### Paso 4: Anula la Campaign y los datos del registro (opcional) {#step-4-override-campaign-and-record-data-optional}

Si tu Content Block admite valores predeterminados, puedes usarlo sin establecer ninguna variable.

Si necesitas elegir una Campaign de VideoSmart específica, pasar campos de personalización personalizados, o ambas cosas, establece las siguientes variables de Liquid antes de renderizar el Content Block:

- `vs_campaign_id`: identificador de la Campaign de VideoSmart
- `vs_record_data`: una cadena JSON que contiene los valores que deseas pasar a la plantilla de VideoSmart

#### Ejemplo {#example}

Este ejemplo utiliza atributos de usuario de Braze para el nombre y el apellido:

{% raw %}
```liquid
{% assign vs_campaign_id = "CAMPAIGN_ID" %}

{% capture vs_record_data %}
{
  "FirstName": "{{ ${first_name} | default: 'Alex' | json_escape }}",
  "LastName": "{{ ${last_name} | default: 'Doe' | json_escape }}"
}
{% endcapture %}
{% assign vs_record_data = vs_record_data | strip_newlines %}
```
{% endraw %}

{% alert note %}
- Proporciona siempre valores predeterminados para los valores utilizados en `vs_record_data` para que la vista previa de tu correo electrónico en Braze se muestre correctamente.
- `vs_record_data` debe ser un JSON válido, codificado como una sola cadena (el ejemplo usa `strip_newlines`).
{% endalert %}

### Paso 5: Usa las variables generadas por la plantilla del Content Block de VideoSmart {#step-5-use-the-variables-generated-by-videosmarts-content-block-template}

Después de que el Content Block se ejecuta, genera variables que puedes referenciar en otras partes de tu correo electrónico.

Las variables comunes incluyen:

{% raw %}
| Variable | Descripción |
| --------------------------------- | ----------------------------------------------------- |
| `{{ video_url }}` | URL del video personalizado |
| `{{ poster_url }}` | URL de la imagen del póster para el video |
| `{{ output_data.VARIABLE_NAME }}` | Campos de salida adicionales expuestos por el Content Block |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 5: Usa las variables generadas por la plantilla del Content Block de VideoSmart" }
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 5: Usa las variables generadas por la plantilla del Content Block de VideoSmart" }

## Límites de velocidad {#rate-limits}

La API de VideoSmart tiene un límite de velocidad de 10 000 solicitudes por minuto. Si superas este límite, podrías recibir errores o experimentar retrasos en la generación de videos.

Para reducir este riesgo, configura los límites de velocidad de Campaign en Braze de modo que la tasa de envío de mensajes se mantenga por debajo de la capacidad de la API de VideoSmart.

Para obtener orientación de Braze sobre la velocidad de entrega y los límites de velocidad, consulta [Velocidad de entrega y límites de velocidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting).

## Consideraciones {#considerations}

- El contenido conectado se ejecuta cuando el mensaje se renderiza, por lo que los valores pueden diferir entre la vista previa y el envío si tus valores predeterminados o atributos son diferentes.
- Confirma que tu correo electrónico incluya el Content Block antes de hacer referencia a variables como `video_url`.
- Si utilizas campos personalizados en `vs_record_data`, confirma los nombres de campo esperados con VideoSmart.

## Solución de problemas {#troubleshooting}

### La vista previa no funciona {#preview-not-working}

Si la vista previa de Braze falla (por ejemplo, reintentos repetidos o errores de autenticación), comprueba que:

- La credencial de contenido conectado "basic_credentials" existe y está configurada correctamente.
- La plantilla del **bloque de contenido de VideoSmart** está presente en tu cuenta de Braze.
- Todas las variables requeridas (por ejemplo, `vs_campaign_id` o los campos obligatorios en `vs_record_data`) tienen valores predeterminados configurados para la vista previa.

### Las variables de la plantilla del bloque de contenido de VideoSmart no generan el resultado esperado {#videosmarts-content-block-template-variables-not-generating-expected-output}

Si las variables generadas por la plantilla del bloque de contenido de VideoSmart no generan el resultado esperado, comprueba lo siguiente:

- La plantilla del **bloque de contenido de VideoSmart** está configurada correctamente en Braze.
- La autenticación del contenido conectado está configurada correctamente con las credenciales apropiadas.
- Imprime las variables en tu correo electrónico para confirmar que se están estableciendo. Por ejemplo: `{% raw %}{{ video_url }}{% endraw %}`

Si estás usando una Campaign personalizada, verifica también:

- `vs_campaign_id` está establecido con un identificador de Campaign válido.
- `vs_record_data` es JSON válido y contiene los campos esperados.