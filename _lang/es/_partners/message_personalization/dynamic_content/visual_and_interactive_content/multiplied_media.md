---
nav_title: Multiplied Media
article_title: Multiplied Media
description: "Aprende a usar Multiplied Media con Braze para enviar imágenes personalizadas, GIF y video a través de correo electrónico, notificaciones push, mensajes dentro de la aplicación, Content Cards y WhatsApp."
alias: /partners/multiplied_media/
page_type: partner
search_tag: Partner
---

# Multiplied Media

> [Multiplied Media](https://multiplied.media) es un estudio de creatividad y automatización que utiliza tus datos de CRM para crear imágenes personalizadas, GIF y video, un activo único para cada cliente. La integración de Multiplied Media y Braze te permite enviar estos contenidos multimedia a través de correo electrónico, notificaciones push, mensajes dentro de la aplicación, Content Cards y WhatsApp.
>
> Multiplied Media es un servicio gestionado, no una herramienta de software. El equipo de Multiplied Media se encarga del concepto, el diseño, la animación, la conexión de datos y el renderizado. Para usar esta integración, inserta una URL de contenido multimedia con una etiqueta de combinación de [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) en tu Campaign o Canvas.

_Esta integración es mantenida por Multiplied Media._

## Acerca de esta integración {#about-this-integration}

El equipo de Multiplied Media trabaja contigo desde el primer concepto hasta el lanzamiento. Diseñan y animan contenido multimedia para tu marca, conectan tus datos y automatizan el renderizado. No necesitas aprender ningún software nuevo.

La integración conecta tus datos de Braze —atributos de clientes y segmentos— con Multiplied Media. Multiplied Media renderiza un activo multimedia único para cada cliente y lo aloja en una URL que contiene el identificador de ese cliente. Tú haces referencia a esa URL en tu mensaje de Braze con una etiqueta de combinación de Liquid. Cada cliente ve entonces su propia imagen, GIF o video.

La integración admite dos flujos:

- **Campañas por lotes:** Envía datos por CSV, S3 o API. Multiplied Media renderiza y aloja todos los contenidos multimedia antes del envío.
- **Automatizaciones de Canvas en tiempo real:** Un paso de [webhook]({{site.baseurl}}/user_guide/channels/webhooks) en tu Canvas activa el renderizado cuando un cliente llega a ese paso.

## Ejemplos {#use-cases}

- **Campañas personalizadas:** Lanzamientos de productos, campañas de resumen del año ("wrapped" y year-in-review), promociones de temporada y visualizaciones de datos personales.
- **Automatizaciones siempre activas:** Flujos de bienvenida, incorporación, celebraciones de hitos, correos electrónicos de recuperación, carrito abandonado, notificaciones de envío, alertas de reposición de stock y actualizaciones de fidelización.
- **Recorridos omnicanal:** Un concepto, renderizado para cada canal. Los mismos datos del cliente pueden convertirse en una imagen principal de correo electrónico, una imagen push, un elemento visual dentro de la aplicación y un video de WhatsApp, de modo que un recorrido mantiene una identidad visual coherente en cada punto de intervención.

## Requisitos previos {#prerequisites}

La arquitectura de Multiplied Media admite campañas por lotes a través de S3 o API y automatización de Canvas en tiempo real a través de webhooks. Al pregenerar y alojar activos multimedia únicos antes de la entrega, Multiplied Media garantiza que las experiencias visuales uno a uno estén listas para combinarse en tus plantillas con etiquetas de Liquid o atributos personalizados en el momento en que se activa tu mensaje.

Antes de empezar, confirma que tienes lo siguiente:

| Requisito | Descripción |
| --- | --- |
| Contrato activo con Multiplied Media | Multiplied Media es un servicio gestionado. Antes de comenzar en Braze, el equipo de Multiplied Media define el alcance de tu campaña, diseña y construye tus plantillas multimedia y configura el renderizado. Para empezar, visita [multiplied.media](https://multiplied.media) o envía un correo electrónico a [hello@multiplied.media](mailto:hello@multiplied.media). |
| Origen de datos | Conecta tus datos de clientes a Multiplied Media por CSV, S3, API o webhooks de Braze. El equipo de Multiplied Media lo configura contigo durante la incorporación. |
| Identificador unificador | Tus datos deben incluir un identificador compartido entre Braze y Multiplied Media, como `external_id`. Este identificador forma parte de la URL multimedia de cada cliente, y tu mensaje de Braze lo referencia con Liquid. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Usar Multiplied Media con Braze {#use-multiplied-media-with-braze}

Multiplied Media diseña, construye y renderiza tu contenido multimedia personalizado y te ayuda a conectar tus datos. Los siguientes pasos son lo que queda por hacer en Braze.

### Paso 1: Confirma que tu contenido multimedia está listo {#step-1-confirm-your-media-is-ready}

Antes del lanzamiento, el equipo de Multiplied Media confirma que tu contenido multimedia está renderizado (campañas por lotes) o que tu endpoint de renderizado está en vivo (flujos de Canvas en tiempo real). Luego te proporcionan la URL multimedia de tu campaña. Por ejemplo:

{% raw %}
```
https://cdn.multiplied.media/yourbrand/campaign-name/{{${user_id}}}.gif
```
{% endraw %}

El identificador en la ruta de la URL es el identificador unificador acordado durante la configuración.

### Paso 2: Inserta la URL en tu Campaign o Canvas {#step-2-insert-the-url-into-your-campaign-or-canvas}

Pega la URL de Multiplied Media —con la etiqueta de combinación de Liquid— en el campo correspondiente a tu canal:

- **Correo electrónico:** La fuente de imagen en tu plantilla de correo electrónico.
- **Notificaciones push:** El campo de imagen de tu mensaje push.
- **Mensajes dentro de la aplicación y Content Cards:** El campo de contenido multimedia.
- **WhatsApp:** El campo de encabezado multimedia.

Para automatizaciones de Canvas en tiempo real, añade el paso de webhook de Multiplied Media (configurado contigo durante la incorporación) junto con un nodo de retraso antes de tu paso de mensaje. Esto garantiza que el contenido multimedia se renderice para cada cliente antes de la entrega.

### Paso 3: Previsualiza, prueba y lanza {#step-3-preview-test-and-launch}

Usa las vistas previas y los envíos de prueba de Braze para confirmar que la etiqueta de Liquid se resuelve y que cada usuario de prueba ve su propio contenido multimedia. El equipo de Multiplied Media revisa los envíos de prueba contigo antes del lanzamiento.

## Consideraciones {#considerations}

- El activo multimedia de cada cliente es único. Si un cliente no está en el origen de datos conectado, la URL sirve una versión alternativa (predeterminada) del contenido multimedia. Multiplied Media diseña la alternativa como parte de cada proyecto.
- Multiplied Media renderiza y aloja los activos antes de la entrega; no los renderiza en el momento de apertura. El contenido multimedia se carga inmediatamente al abrir y muestra los datos del cliente tal como estaban en el momento del renderizado. Si los datos deben estar actualizados en el momento del envío —por ejemplo, en flujos de Canvas activados—, usa el paso de webhook en tiempo real.
- Para campañas por lotes programadas, tus datos deben llegar a Multiplied Media antes del momento de envío para que puedan renderizar todos los activos. Tu equipo de Multiplied Media acuerda contigo el plazo límite durante la configuración.

## Solución de problemas {#troubleshooting}

Multiplied Media es un servicio gestionado, por lo que tu equipo de Multiplied Media es tu primera línea de soporte. Contáctalos en [hello@multiplied.media](mailto:hello@multiplied.media).

Consulta la siguiente tabla si tu imagen dinámica no se muestra.

| Problema | Resolución |
| --- | --- |
| La imagen dinámica no se muestra | Confirma que la etiqueta de Liquid en la URL coincide con el identificador unificador acordado durante la configuración (por ejemplo, `user_id` frente a un atributo personalizado). Confirma que el cliente existe en el origen de datos conectado. Si el identificador se resuelve pero no existe un activo personalizado, se muestra el contenido multimedia alternativo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solución de problemas" }