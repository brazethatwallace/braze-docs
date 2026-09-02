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
| Cuenta Kameleoon | Se necesita una cuenta Kameleoon para beneficiarse de esta asociación.|
| Cuenta Braze| Una cuenta Braze activa con el [SDK or kit de desarrollo de software Web de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) integrado en tu página web. También necesitarás que se habilite la segmentación de propiedades del evento. Para solicitarlo, consulta [Consideraciones](#considerations).|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

Kameleoon envía eventos personalizados a Braze para identificar a los usuarios que participan en campañas de experimentación y personalización, lo que permite una segmentación más precisa y mensajes personalizados.

## Integración de Kameleoon {#integrating-kameleoon}

Esta integración se ejecuta como un rastreador JavaScript a través de engine.js de Kameleoon. Se puede habilitar rápidamente desde la plataforma de Kameleoon.

### Paso 1: Ir a la página de integraciones de Kameleoon {#step-1-go-to-the-kameleoon-integrations-page}

En tu aplicación Kameleoon, selecciona **Admin** y luego **Integrations** en la barra lateral.

![El panel de administración de la plataforma Kameleoon.]({% image_buster /assets/img/kameleoon/img_1.png %}){: style="max-width:70%;"}

### Paso 2: Instala la herramienta Braze {#step-2-install-the-braze-tool}

Por defecto, la herramienta Braze no está instalada. Busca el icono de Braze y selecciona **Install the tool**. ![Un cuadrado gris con una flecha apuntando hacia abajo.]({% image_buster /assets/img/kameleoon/img_2.png %})

Selecciona los proyectos para los que quieres activar la herramienta Braze, de modo que los datos de Kameleoon se reporten correctamente a Braze.

![El icono de la herramienta Braze en Kameleoon.]({% image_buster /assets/img/kameleoon/img_3.png %})

Tras configurar la herramienta, selecciona **Validate**, con lo que se cerrará el panel de configuración. A continuación, verás un interruptor **ON** junto al icono de la herramienta Braze, que incluye el número de proyectos en los que está configurada la herramienta.

![La herramienta Braze activada en Kameleoon.]({% image_buster /assets/img/kameleoon/img_4.png %})

{% alert important %}
Esta característica está en fase beta. Únete al [Programa Beta de Kameleoon](https://help.kameleoon.com/account-and-team-management/join-beta-program/) para empezar a utilizar esta integración.
{% endalert %}

### Paso 3: Asociar Braze a las campañas de Kameleoon {#step-3-associate-braze-with-kameleoon-campaigns}

#### En el editor gráfico/código {#in-the-graphiccode-editor}

Para finalizar tu experimento, selecciona el paso **Integrations** para configurar Braze como herramienta de seguimiento y, a continuación, selecciona **Braze**.

![El panel de integraciones en Kameleoon muestra todas las integraciones disponibles, incluida la integración activa Braze.]({% image_buster /assets/img/kameleoon/img_5.png %})

Braze se mencionará en el resumen antes de salir en vivo. Kameleoon transmitirá automáticamente los datos a Braze, y podrás utilizarlos para el análisis y la segmentación directamente en Braze.

##### Creación de personalización {#personalization-creation}

En la página **Personalization Creation**, puedes seleccionar Braze entre las herramientas de elaboración de informes para personalizar tus informes.

![La sección de herramientas de elaboración de informes muestra integraciones como Heap, Mixpanel, Clarity, con Braze seleccionado.]({% image_buster /assets/img/kameleoon/img_6.png %})

##### Creación de conmutador de características {#feature-flag-creation}

Configura la integración en el entorno del conmutador de características en la sección **Integrations**. Habilítala para los entornos en los que quieras que esté activa.

![La página de conmutador de características en Kameleoon con las integraciones disponibles. Hay dos interruptores para cada socio, "Delivery rules" y "Feature experiments".]({% image_buster /assets/img/kameleoon/img_7.png %})

##### Página de resultados {#results-page}

Una vez establecido Braze como herramienta de elaboración de informes para un experimento, puedes seleccionarlo (o deseleccionarlo) en la página de resultados de Kameleoon, en el menú **Experiment configuration**.

{% alert note %}
Esta integración requiere una [implementación híbrida](https://developers.braze-presentation.preview.kameleoon.net/core-concepts/hybrid-experimentation?language=en#sending-exposure-events-to-third-party-analytics) y solo es compatible con SDK or kit de desarrollo de software Web.
{% endalert %}

![El panel lateral de la página de resultados en Kameleoon.]({% image_buster /assets/img/kameleoon/img_8.png %}){: style="max-width:50%;" }

Aparecerán las herramientas de informe asociadas al experimento. Selecciona **Edit** para modificar esta selección.

### Paso 4: Analiza y aprovecha tus datos de Kameleoon en Braze {#step-4-analyze-and-leverage-your-kameleoon-data-in-braze}

Una vez configurada la integración, Kameleoon enviará a Braze eventos personalizados denominados `kameleoon_exposure` con propiedades como **Experiment name**, **Experiment ID**, **Variation name** y **Variation ID**.

![El registro de usuarios del evento personalizado en Braze, mostrando un ejemplo de carga útil del evento que ha recibido Braze de Kameleoon.]({% image_buster /assets/img/kameleoon/img_9.png %})

A continuación, puedes ver estos datos en los eventos personalizados, crear informes de eventos personalizados para identificar la exposición a campañas de Kameleoon y habilitar la segmentación basada en las propiedades del evento. Puedes utilizar eventos personalizados al crear Campaigns y Canvas posteriores o vinculados mediante [Rutas de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/#action-groups), [desencadenantes basados en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/) o creando [segmentos]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/).

Además, se podrá acceder a estos eventos a través de [los objetos de eventos personalizados de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) para poder realizar informes y análisis exhaustivos.

## Consideraciones {#considerations}

### Solicitar segmentación de propiedades del evento {#request-event-property-segmentation}

Antes de poder utilizar la segmentación de propiedades de eventos, necesitarás habilitarla en Braze. Utiliza la siguiente plantilla para ponerte en contacto con tu CSM or administrador de éxito de cliente de Braze o con el equipo de soporte para obtener acceso.

   <table aria-label="Solicitar segmentación de propiedades del evento">
     <caption>Solicitar segmentación de propiedades del evento</caption>
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
   {: .reset-td-br-1 .reset-td-br-2 aria-label="Solicitar segmentación de propiedades del evento" }

### Puntos de datos de Braze {#braze-data-points}

El evento personalizado enviado desde Kameleoon a Braze&#8212;incluidas las propiedades del evento habilitadas para la segmentación&#8212;registrará puntos de datos en tu instancia de Braze.