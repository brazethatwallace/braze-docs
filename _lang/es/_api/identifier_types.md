---
nav_title: "Tipos de identificadores API"
article_title: "Tipos de identificadores API"
page_order: 2.2
toc_headers: h2
description: "Este artículo de referencia cubre los diferentes tipos de identificadores API que existen en el panel de Braze, dónde puedes encontrarlos y para qué se utilizan."
page_type: reference
---

# Tipos de identificadores API {#api-identifier-types}

> Esta guía de referencia aborda los distintos tipos de identificadores de API que se pueden encontrar en el panel de Braze, su finalidad, dónde encontrarlos y cómo se suelen utilizar. Para obtener información sobre las claves de API REST o las claves de API del espacio de trabajo, consulta el [resumen de la API]({{site.baseurl}}/api/basics).

Los siguientes identificadores pueden utilizarse para acceder a tu plantilla, Canvas, Campaign o Segment desde la API externa de Braze. Todos los mensajes deben seguir la codificación [UTF-8](https://en.wikipedia.org/wiki/UTF-8).

## Identificador de la aplicación {#app-identifier}

El identificador de la aplicación o `app_id` es un parámetro que asocia la actividad con una aplicación específica en tu espacio de trabajo. Designa con qué aplicación dentro del espacio de trabajo estás interactuando. Por ejemplo, puedes encontrar que tienes un `app_id` para tu aplicación iOS, un `app_id` para tu aplicación Android y un `app_id` para tu integración web. En Braze, es posible que tengas múltiples aplicaciones para la misma plataforma en los diversos tipos de plataforma que Braze admite.

### ¿Dónde puedo encontrarlo? {#where-can-i-find-it}

Hay dos formas de localizar tu `app_id`:

{% tabs local %}
{% tab Identificadores de aplicación %}
Ve a **Configuración** > **API e identificadores** > **Identificadores de aplicación**. Tu clave de API para cada aplicación aparece en la columna **Identificador**.
{% endtab %}

{% tab Configuración de la aplicación %}
Ve a **Configuración** > **Configuración de la aplicación**. Tu clave de API aparece junto al campo **API Key** en la sección de configuración.

{% endtab %}
{% endtabs %}

### ¿Para qué se puede usar? {#what-can-it-be-used-for}

Los identificadores de aplicación en Braze se utilizan al integrar el SDK y también se usan para hacer referencia a una aplicación específica en las llamadas a la REST API. Con el `app_id` puedes hacer muchas cosas, como extraer datos de un evento personalizado que ocurrió para una aplicación en particular, recuperar estadísticas de desinstalación, estadísticas de nuevos usuarios, estadísticas de DAU y estadísticas de inicio de sesión para una aplicación específica.

{% alert tip %}
A veces, es posible que se te solicite un `app_id`, pero no estás trabajando con una aplicación, porque es un campo heredado específico de una plataforma en particular. Puedes omitir este campo incluyendo cualquier cadena de caracteres como marcador de posición para este parámetro obligatorio.
{% endalert %}

### Múltiples identificadores de aplicación {#multiple-app-identifiers}

Durante la configuración del SDK, el caso de uso más común para múltiples identificadores de aplicación es separar esos identificadores para las variantes de compilación de depuración y producción.

Para alternar fácilmente entre múltiples identificadores de aplicación en tus compilaciones, te recomendamos crear un archivo `braze.xml` separado para cada [variante de compilación](https://developer.android.com/studio/build/build-variants.html) relevante. Una variante de compilación es una combinación de tipo de compilación y variante de producto. De forma predeterminada, un nuevo proyecto de Android se configura con los tipos de compilación `debug` y `release` y sin variantes de producto.

Para cada variante de compilación relevante, crea un nuevo `braze.xml` en `src/<build variant name>/res/values/`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">{YOUR_BUILD_VARIANT_API_KEY}</string>
</resources>
```
Cuando se compila la variante de compilación, se utiliza el nuevo identificador.

## Identificador de plantilla {#template-identifier}

Un [identificador de plantilla]({{site.baseurl}}/api/endpoints/templates) o ID de plantilla es una clave aleatoria generada por Braze para una plantilla determinada dentro del panel. Los ID de plantilla son únicos para cada plantilla y se pueden usar para hacer referencia a plantillas a través de la API.

Las plantillas son útiles si tu empresa subcontrata los diseños HTML para Campaigns. Una vez que las plantillas se han creado, tienes una plantilla que no es específica de una Campaign, sino que se puede aplicar a una serie de Campaigns, como un boletín informativo.

### ¿Dónde puedo encontrarlo?

Puedes encontrar tu ID de plantilla de una de dos formas:

{% tabs local %}
{% tab Plantillas %}
Ve a **Plantillas**, selecciona una página de plantilla y luego selecciona una plantilla preexistente. Si la plantilla que deseas aún no existe, crea una y guárdala. En la parte inferior de la página de la plantilla individual, puedes encontrar tu identificador de plantilla.
{% endtab %}

{% tab Claves de API %}
Ve a **Configuración** > **API e identificadores**. Aquí, Braze ofrece una búsqueda de **Identificadores de API adicionales** donde puedes buscar identificadores específicos.

{% endtab %}
{% endtabs %}

### ¿Para qué se puede usar?

- Actualizar plantillas usando la API
- Obtener información sobre una plantilla específica

## Identificador de Canvas {#canvas-identifier}

Un identificador de [Canvas]({{site.baseurl}}/user_guide/messaging/canvas) o ID de Canvas es una clave aleatoria generada por Braze para un Canvas determinado dentro del panel. Los ID de Canvas son únicos para cada Canvas y se pueden utilizar para hacer referencia a los Canvas a través de la API.

Ten en cuenta que si tienes un Canvas con variantes, existe un ID de Canvas general, así como ID de Canvas de variantes individuales anidados bajo el Canvas principal.

### ¿Dónde puedo encontrarlo?

Puedes encontrar tu ID de Canvas en el panel. Ve a **Messaging** > **Canvas** y selecciona un Canvas preexistente. Si el Canvas que deseas aún no existe, crea uno y guárdalo. En la parte inferior de la página de un Canvas individual, haz clic en **Analyze Variants**. Aparecerá una ventana con el identificador de API de Canvas ubicado en la parte inferior.

### ¿Para qué se puede utilizar?

- Rastrear análisis de un mensaje específico
- Obtener estadísticas agregadas de alto nivel sobre el rendimiento de Canvas
- Obtener detalles de un Canvas específico
- Con Currents para incorporar datos a nivel de usuario con un enfoque de "visión global" de los Canvas
- Con la entrega desencadenada por API para recopilar estadísticas de mensajes transaccionales

## Identificador de Campaign {#campaign-identifier}

Un identificador de [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) o ID de Campaign es una clave aleatoria generada por Braze para una Campaign determinada dentro del panel. Los ID de Campaign son únicos para cada Campaign y pueden usarse para hacer referencia a las Campaigns a través de la API.

Ten en cuenta que, si tienes una Campaign con variantes, existe tanto un ID de Campaign general como ID de Campaign de variantes individuales anidados bajo la Campaign principal.

### ¿Dónde puedo encontrarlo?

Puedes encontrar tu ID de Campaign de dos formas:

{% tabs local %}
{% tab Campaigns %}
Ve a **Mensajería** > **Campaigns** y selecciona una Campaign preexistente. Si la Campaign que deseas aún no existe, crea una y guárdala. En la parte inferior de la página de la Campaign individual, puedes encontrar tu **Identificador de API de Campaign**.

{% endtab %}

{% tab Claves de API %}
Ve a **Configuración** > **API e identificadores**. Aquí, Braze ofrece una búsqueda de **Identificadores de API adicionales** donde puedes buscar identificadores específicos.

{% endtab %}
{% endtabs %}

### ¿Para qué se puede usar?

- Rastrear análisis de un mensaje específico
- Obtener estadísticas agregadas de alto nivel sobre el rendimiento de una Campaign
- Obtener detalles de una Campaign específica
- Con Currents para incorporar datos a nivel de usuario con un enfoque de "panorama general" de las Campaigns
- Con entrega activada por API para recopilar estadísticas de mensajes transaccionales
- Para [buscar una Campaign específica]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/search_campaigns) en la página de **Campaigns** usando el filtro `api_id:YOUR_API_ID`

## Identificador de Segment {#segment-identifier}

Un identificador de [Segment]({{site.baseurl}}/user_guide/audience/segments) o ID de Segment es una clave aleatoria generada por Braze para un Segment determinado dentro del panel. Los ID de Segment son únicos para cada Segment y se pueden utilizar para hacer referencia a los Segments a través de la API.

### ¿Dónde puedo encontrarlo?

Puedes encontrar tu ID de Segment de una de estas dos formas:

{% tabs local %}
{% tab Segments %}
Ve a **Audiencia** > **Segments** y selecciona un Segment preexistente. Si el Segment que deseas aún no existe, crea uno y guárdalo. En la parte inferior de la página individual del Segment, puedes encontrar tu identificador de Segment.

{% endtab %}

{% tab Claves de API %}
Ve a **Configuración** > **API e identificadores**. Aquí, Braze ofrece una búsqueda de **Identificadores de API adicionales** donde puedes buscar identificadores específicos.

{% endtab %}
{% endtabs %}

### ¿Para qué se puede utilizar?

- Obtener detalles sobre un Segment específico
- Recuperar análisis de un Segment específico
- Consultar cuántas veces se registró un evento personalizado para un Segment en particular
- Especificar y enviar una Campaign a los miembros de un Segment desde la API

## Identificador de envío {#send-identifier}

Un identificador de envío, o send ID, es una clave generada por Braze o creada por ti para un envío de mensaje determinado, bajo la cual se rastrean los análisis. El identificador de envío te permite recuperar análisis de una instancia específica de un envío de Campaign a través del [endpoint `/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics).

### ¿Dónde puedo encontrarlo?

Las Campaigns activadas por API y las Campaigns de API que se envían como difusión generan automáticamente un identificador de envío si no se proporciona uno. Si deseas especificar tu propio identificador de envío, primero debes crear uno a través del [endpoint `/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids). El identificador debe contener solo caracteres ASCII y tener como máximo 64 caracteres de longitud. Puedes reutilizar un identificador de envío en múltiples envíos de la misma Campaign si deseas agrupar los análisis de esos envíos.

### ¿Para qué se puede utilizar?
Envía y rastrea el rendimiento de los mensajes de forma programática, sin necesidad de crear una Campaign para cada envío.

## Identificador de grupo de suscripción {#subscription-group-identifier}

Un identificador de grupo de suscripción, o ID de grupo de suscripción, es una clave generada por Braze para un grupo de suscripción determinado. Los ID son únicos para cada grupo de suscripción y se pueden utilizar para hacer referencia a los grupos de suscripción a través de la API.

### ¿Dónde puedo encontrarlo?

Ve a **Audiencia** > **Suscripciones** y copia el ID junto al grupo de suscripción correspondiente.

### ¿Para qué se puede utilizar?

- Listar los grupos de suscripción de un usuario
- Obtener el estado del grupo de suscripción de un usuario
- Actualizar el estado del grupo de suscripción de un usuario