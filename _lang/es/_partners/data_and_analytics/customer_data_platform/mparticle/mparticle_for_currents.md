---
nav_title: mParticle para Currents
article_title: mParticle para Currents
alias: /partners/mparticle_for_currents/
description: "Este artículo de referencia describe la asociación entre Braze Currents y mParticle, una plataforma de datos de los clientes que recopila y encamina información entre las fuentes de tu stack de marketing."
page_type: partner
tool: Currents
search_tag: Partner

---

# mParticle para Currents {#mparticle-for-currents}

> [mParticle](https://www.mparticle.com) es una plataforma de datos de los clientes que recopila y encamina información de múltiples fuentes a una variedad de otras ubicaciones en tu stack de marketing.

La integración de Braze y mParticle te permite controlar fácilmente el flujo de información entre ambos sistemas. Con [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/), también puedes conectar los datos a mParticle para que sean procesables en todo el stack de crecimiento.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Currents | Para volver a exportar datos a mParticle, debes tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) en tu cuenta. |
| Cuenta de mParticle | Se necesita una [cuenta de mParticle](https://app.mparticle.com/login) para beneficiarse de esta asociación. |
| Clave y secreto de servidor a servidor de mParticle | Se pueden obtener navegando hasta tu dashboard de mParticle y creando las [fuentes necesarias](#step-1-create-feeds) que permitan a mParticle recibir datos de interacción de Braze para las plataformas iOS, Android y Web.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Acerca de las credenciales de mParticle {#about-mparticle-credentials}

mParticle tiene credenciales a nivel de aplicación y a nivel de espacio de trabajo que afectan al modo en que se envían tus eventos.

- **A nivel de aplicación:** mParticle separará los eventos por cada aplicación individual, lo que significa que las credenciales a nivel de aplicación que proporciones a tu aplicación iOS solo pueden utilizarse para enviar eventos específicos de iOS.
- **A nivel de espacio de trabajo:** mParticle agrupa todos los eventos (que **no** son específicos de una aplicación), lo que significa que las credenciales a nivel de espacio de trabajo que proporciones a tu grupo de aplicaciones se utilizarán para enviar todos tus eventos no específicos de una aplicación.

Puedes pensar en esto como si mParticle ingiriera una "fuente" basada en cada aplicación individual. Por ejemplo, si tienes una aplicación para iOS, una para Android y una para Web, tus eventos estarán separados. Esto significa que si proporcionas las mismas credenciales para cada aplicación, se utilizará una sola fuente de mParticle para recibir todos los datos de todas tus aplicaciones, sin duplicación.

## Integración {#integration}

### Paso 1: Crear fuentes {#step-1-create-feeds}

Desde tu cuenta de administrador de mParticle, ve a **Setup > Inputs**. Localiza **Braze** en el **Directory** de mParticle y añade la integración de fuente.

La integración de fuente de Braze admite cuatro fuentes separadas: iOS, Android, Web y Unbound. La fuente Unbound puede utilizarse para eventos como correos electrónicos que no están conectados a una plataforma. Necesitarás crear una entrada para cada fuente de plataforma principal. Puedes crear entradas adicionales desde **Setup > Inputs**, en la pestaña **Feed Configurations**.

![]({% image_buster /assets/img/braze-feed-inputs.png %})

Para cada fuente, en **Act as Platform** selecciona la plataforma correspondiente de la lista. Si no ves una opción para seleccionar una fuente **act-as**, los datos se tratarán como Unbound, pero aún podrán reenviarse a salidas de almacén de datos.

![El primer cuadro de diálogo de integración, que te solicita proporcionar un nombre de configuración, determinar un estado de fuente y seleccionar una plataforma como la cual actuar.]({% image_buster /assets/img/braze-feed-act1.png %}){: style="max-width:40%;"}  ![El segundo cuadro de diálogo de integración que muestra la clave de servidor a servidor y el secreto de servidor a servidor.]({% image_buster /assets/img/braze-feed-act2.png %}){: style="max-width:37%;"}

A medida que crees cada entrada, mParticle te proporcionará una clave y un secreto. Copia estas credenciales, asegurándote de anotar a qué fuente corresponde cada par de credenciales.

### Paso 2: Crear Current {#step-2-create-current}

En Braze, ve a **Currents > + Create Current > Create mParticle Export**. Proporciona un nombre de integración, un correo electrónico de contacto y la clave de API de mParticle y la clave secreta de mParticle para cada plataforma. A continuación, selecciona los eventos que deseas rastrear; se proporciona una lista de eventos disponibles. Por último, haz clic en **Launch Current**.

![La página de mParticle Currents en Braze. Aquí puedes encontrar campos para el nombre de integración, correo electrónico de contacto, clave de API y clave secreta.]({% image_buster /assets/img_archive/currents-mparticle-edit.png %})

{% alert important %}
Es importante mantener tu clave de API de mParticle y tu clave secreta de mParticle actualizadas; si las credenciales de tu conector caducan, el conector dejará de enviar eventos. Si esto persiste durante más de **5 días**, los eventos del conector se descartarán y los datos se perderán permanentemente.
{% endalert %}

Todos los eventos enviados a mParticle incluirán el `external_user_id` del usuario como `customerid`. En este momento, Braze no envía datos de eventos para usuarios que no tienen configurado su `external_user_id`. Si deseas mapear el `external_user_id` a un ID diferente en mParticle que no sea el `customerid` predeterminado, ponte en contacto con tu CSM de Braze.

## Eventos de Currents compatibles {#supported-currents-events}

Braze admite la exportación de los siguientes eventos a mParticle:

- [Eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)
- [Eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)

Para conocer la estructura de la carga útil de cada evento, selecciona la pestaña **mParticle** en el [glosario de eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) y el [glosario de eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/).

Para obtener más información sobre la integración de mParticle, visita la [documentación de mParticle](http://docs.mparticle.com/integrations/braze/feed).