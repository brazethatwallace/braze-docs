---
nav_title: Kameleoon
article_title: Kameleoon
description: "Aprende a integrar Kameleoon con Braze"
alias: /partners/kameleoon/
page_type: partner
search_tag: Partner
---

# Kameleoon

>[Kameleoon](https://www.kameleoon.com) es una solución de optimización con capacidades de experimentación, personalización basada en IA y gestión de características en una única plataforma unificada.

## Requisitos previos {#prerequisites}

Antes de empezar, necesitarás lo siguiente:

| Requisito | Descripción |
| --- | --- |
| Cuenta de Kameleoon | Se requiere una cuenta de Kameleoon para aprovechar esta integración.|
| Cuenta de Braze | Una cuenta activa de Braze con el [SDK Web de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) integrado en tu página web. También necesitarás tener habilitada la segmentación por propiedades del evento. Para solicitarla, consulta [Consideraciones](#considerations).|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Ejemplos {#use-cases}

Kameleoon envía eventos personalizados a Braze para identificar a los usuarios que participan en experimentos y Campaigns de personalización, lo que permite una segmentación más precisa y una mensajería personalizada.

## Integración de Kameleoon {#integrating-kameleoon}

Esta integración se ejecuta como un rastreador de JavaScript a través del engine.js de Kameleoon. Se puede habilitar desde la plataforma de Kameleoon.

### Paso 1: Ve a la página de Integraciones de Kameleoon {#step-1-go-to-the-kameleoon-integrations-page}

En tu aplicación de Kameleoon, selecciona **Admin** y luego **Integrations** en la barra lateral.

![El panel de administración en la plataforma Kameleoon.]({% image_buster /assets/img/kameleoon/img_1.png %}){: style="max-width:70%;"}

### Paso 2: Instala la herramienta de Braze {#step-2-install-the-braze-tool}

De forma predeterminada, la herramienta de Braze no está instalada. Busca el icono de Braze y selecciona **Install the tool**. ![Un cuadrado gris con una flecha apuntando hacia abajo.]({% image_buster /assets/img/kameleoon/img_2.png %})

Selecciona los proyectos para los cuales deseas activar la herramienta de Braze, de modo que los datos de Kameleoon se reporten correctamente a Braze.

![El icono de la herramienta de Braze en Kameleoon.]({% image_buster /assets/img/kameleoon/img_3.png %})

Después de configurar la herramienta, selecciona **Validate**, lo que cierra el panel de configuración. Aparecerá un interruptor **ON** junto al icono de la herramienta de Braze, que incluye el número de proyectos en los que está configurada la herramienta.

![La herramienta de Braze activada en Kameleoon.]({% image_buster /assets/img/kameleoon/img_4.png %})

### Paso 3: Asocia Braze con las campañas de Kameleoon {#step-3-associate-braze-with-kameleoon-campaigns}

#### En el editor gráfico/de código {#in-the-graphiccode-editor}

Para completar tu experimento, selecciona el paso **Integrations** para configurar Braze como herramienta de seguimiento y luego selecciona **Braze**.

![El panel de integraciones en Kameleoon que muestra todas las integraciones disponibles, incluida la integración activa de Braze.]({% image_buster /assets/img/kameleoon/img_5.png %})

Braze se menciona en el resumen antes de publicar. Kameleoon transmite automáticamente los datos a Braze, y puedes usarlos para análisis y segmentación directamente en Braze.

##### Creación de personalización {#personalization-creation}

En la página **Personalization Creation**, puedes seleccionar Braze entre las herramientas de informes para personalizar tus informes.

![Sección de herramientas de informes que muestra integraciones como Heap, Mixpanel, Clarity, con Braze seleccionado.]({% image_buster /assets/img/kameleoon/img_6.png %})

##### Creación de conmutadores de características {#feature-flag-creation}

Configura la integración en el entorno de conmutadores de características en la sección **Integrations**. Habilítala para los entornos en los que desees que esté activa.

![La página de conmutadores de características en Kameleoon con las integraciones disponibles. Hay dos interruptores para cada partner, "Delivery rules" y "Feature experiments".]({% image_buster /assets/img/kameleoon/img_7.png %})

##### Página de resultados {#results-page}

Después de configurar Braze como herramienta de informes para un experimento, puedes seleccionarla (o deseleccionarla) en la página de resultados de Kameleoon en el menú **Experiment configuration**.

{% alert note %}
Esta integración requiere una [implementación híbrida](https://developers.braze-presentation.preview.kameleoon.net/core-concepts/hybrid-experimentation?language=en#sending-exposure-events-to-third-party-analytics) y solo es compatible con SDK web.
{% endalert %}

![El panel lateral de la página de resultados en Kameleoon.]({% image_buster /assets/img/kameleoon/img_8.png %}){: style="max-width:50%;" }

Aparecen las herramientas de informes asociadas al experimento. Selecciona **Edit** para editar esta selección.

### Paso 4: Analiza y aprovecha tus datos de Kameleoon en Braze {#step-4-analyze-and-leverage-your-kameleoon-data-in-braze}

Una vez configurada la integración, Kameleoon envía eventos personalizados llamados `kameleoon_exposure` con propiedades como **Experiment name**, **Experiment ID**, **Variation name**, **Variation ID** a Braze.

![El registro de usuarios de eventos personalizados en Braze, que muestra un ejemplo de la carga útil del evento recibido por Braze desde Kameleoon.]({% image_buster /assets/img/kameleoon/img_9.png %})

Luego puedes ver estos datos en los eventos personalizados, crear informes de eventos personalizados para identificar la exposición a las campañas de Kameleoon y habilitar la segmentación basada en propiedades del evento. Puedes usar eventos personalizados al crear Campaigns y Canvas posteriores o vinculados mediante [Rutas de Acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths#action-groups), [desencadenadores basados en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) o al crear [Segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

Además, estos eventos son accesibles a través de [objetos de eventos personalizados de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) para permitir informes y análisis exhaustivos.

## Consideraciones {#considerations}

### Solicitar segmentación por propiedades del evento {#request-event-property-segmentation}

Antes de poder usar la segmentación por propiedades del evento, necesitarás que esté habilitada en Braze. Usa la siguiente plantilla para contactar a tu CSM de Braze o al equipo de soporte para obtener acceso.

   <table aria-label="Solicitar segmentación por propiedades del evento">
     <caption>Solicitar segmentación por propiedades del evento</caption>
   <thead>
      <tr>
         <th>Campo</th>
         <th>Detalles</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><strong>Asunto</strong></td>
         <td>Request to Enable Event Property Segmentation for Kameleoon Integration</td>
      </tr>
      <tr>
         <td><strong>Cuerpo</strong></td>
         <td>
         Hello Braze Team,<br><br>
         We would like to enable event property segmentation for events sent from our Kameleoon&lt;&gt;Braze integration. Here are the details:<br><br>
         - <strong>Event Name:</strong> Kameleoon<br>
         - <strong>Event Properties:</strong> <code>kameleoon_campaign_name</code>, <code>kameleoon_variation_name</code><br><br>
         Please confirm once the properties have been enabled in our account.<br><br>
         Thank you.
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 aria-label="Solicitar segmentación por propiedades del evento" }

### Puntos de datos de Braze {#braze-data-points}

El evento personalizado enviado desde Kameleoon a Braze&#8212;incluyendo cualquier propiedad del evento habilitada para segmentación&#8212;registrará puntos de datos en tu instancia de Braze.