---
nav_title: Segment Engage
article_title: Segment Engage
page_order: 3
alias: /partners/segment_personas/
alias: /partners/segment_engage/
alias: /partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_personas/

description: "Este artículo de referencia describe la asociación entre Braze y Segment, una plataforma de datos de clientes que recopila y redirige información entre fuentes de tu stack de marketing."
page_type: partner
search_tag: Partner

---

# Segment Engage

> [Segment](https://segment.com) es una plataforma de datos de clientes que te ayuda a recopilar, limpiar y activar los datos de tus clientes. Este artículo de referencia ofrece un resumen de la conexión entre [Braze y Segment Engage](https://segment.com/docs/destinations/braze/#Engage), además de describir los requisitos y procesos para una implementación y uso adecuados.

La integración de Braze y Segment te permite utilizar [Engage](https://segment.com/docs/engage/), el creador de audiencias integrado de Segment, para crear segmentos de usuarios basados en datos que ya hayas recopilado de diversas fuentes. A continuación, estas audiencias se sincronizarán con Braze como una cohorte, o se indicarán en el perfil de usuario mediante [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) o [eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-events) que pueden utilizarse para crear segmentos en Braze y usarlos en la reorientación de Campaigns y Canvas.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Segment | Se necesita una [cuenta de Segment](https://app.segment.com/login) para beneficiarse de esta asociación. |
| Destino en la nube Braze | Ya debes haber configurado [Braze como destino]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) en tu integración de Segment.<br><br>Esto incluye proporcionar el centro de datos Braze y la clave de API REST correctos en tu [configuración de conexión]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment#connection-settings). |
| Clave de importación de datos de Braze | Para sincronizar audiencias de Engage con Braze como cohortes, debes generar una clave de importación de datos.<br><br>La importación de cohortes está en acceso anticipado; ponte en contacto con tu administrador de éxito de cliente de Braze para acceder a esta característica. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración del destino de cohortes {#cohorts-destination-integration}

### Paso 1: Crea una audiencia en Engage {#step-1-create-an-engage-audience}
1. En Segment, ve a la pestaña **Audiences** en Engage y haz clic en **New**.
2. Crea tu audiencia. Un rayo en la esquina superior de la página indicará si la audiencia se actualiza en tiempo real.
3. A continuación, selecciona Braze como destino.
4. Obtén una vista previa de tu audiencia haciendo clic en **Review & Create**. Por defecto, Segment consulta todos los datos históricos para establecer el valor actual del rasgo computado y la audiencia. Para omitir estos datos, desmarca **Historical Backfill**.

### Paso 2: Captura tu clave de importación de datos de cohortes {#step-2-capture-your-cohort-data-import-key}

En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **Segment**.

Aquí encontrarás tu endpoint REST y generarás tu clave de importación de datos de Braze. Una vez generada la clave, puedes crear una nueva o invalidar una existente.

### Paso 3: Conecta el destino de cohortes de Braze {#step-3-connect-the-braze-cohorts-destination}
Sigue [las instrucciones de Segment](https://segment.com/docs/connections/destinations/catalog/actions-braze-cohorts/#getting-started) sobre la configuración del destino de cohortes para sincronizar tus audiencias de Engage como cohortes con Braze.

### Paso 4: Crea un segmento en Braze a partir de la audiencia de Engage {#step-4-create-a-braze-segment-from-the-engage-audience}
En Braze, ve a **Segments**, crea un nuevo segmento y selecciona **Segment Cohorts** como filtro. Desde aquí, puedes elegir qué cohorte de Segment deseas incluir. Una vez creado el segmento de cohorte de Segment, puedes seleccionarlo como filtro de audiencia al crear una Campaign o Canvas.

![Creador de segmentos de Braze utilizando el filtro Segment Cohorts.]({% image_buster /assets/img/segment/segment3.png %})

## Integración en modo nube {#cloud-mode-integration}

### Paso 1: Crea un rasgo computado o audiencia en Segment {#step-1-create-a-segment-computed-trait-or-audience}

1. En Segment, ve a la pestaña **Computed Traits** o **Audiences** en **Engage** y haz clic en **New**.
2. Crea tu rasgo computado o audiencia. Un rayo en la esquina superior de la página indicará si el cálculo se actualiza en tiempo real.
3. A continuación, selecciona **Braze** como destino.
4. Obtén una vista previa de tu audiencia haciendo clic en **Review & Create**. Por defecto, Segment consulta todos los datos históricos para establecer el valor actual del rasgo computado y la audiencia. Para omitir estos datos, desmarca **Historical Backfill**.
5. En la configuración del rasgo computado o audiencia, ajusta la configuración de conexión en función de cómo quieras que se envíen tus datos a Braze.

#### Rasgos computados y audiencias {#computed-traits-and-audiences}

[Los rasgos computados](https://segment.com/docs/engage/audiences/computed-traits/) y las [audiencias](https://segment.com/docs/Engage/audiences/) pueden enviarse a Braze como atributos personalizados o eventos personalizados.
- Los rasgos y audiencias enviados mediante la llamada `identify` aparecerán en Braze como atributos personalizados.
- Los rasgos y audiencias enviados mediante la llamada `track` aparecerán en Braze como eventos personalizados.

Puedes elegir qué método utilizar (o utilizar ambos) cuando conectes el rasgo computado al destino Braze.

{% tabs %}
{% tab Identify %}

Puedes enviar rasgos y audiencias computados a Braze como llamadas `identify` para crear atributos personalizados en Braze.

Por ejemplo, si tienes un rasgo computado en Engage para "Last Product Viewed Item", encontrarás `last_product_viewed_item` en el perfil de usuario de Braze, en **Custom Attributes**. Si, en cambio, se tratara de una audiencia de Engage, encontrarías tu audiencia en **Custom Attributes** configurada como `true`.

| Rasgo computado | Audiencias |
| -------------- | --------- |
| ![La sección de atributos personalizados dentro del perfil de usuario muestra "last_product_viewed_item" como "Sweater".]({% image_buster /assets/img/segment/last_viewed-id-braze.png %}) | ![La sección de atributos personalizados dentro de un perfil de usuario muestra "dormant_shopper" como "true".]({% image_buster /assets/img/segment/dormant-identify-braze.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rasgos computados y audiencias" }

{% endtab %}
{% tab Track %}

Puedes enviar rasgos computados y audiencias a Braze como llamadas `track` para crear eventos personalizados en Braze.

Siguiendo con el ejemplo anterior, si un usuario tiene un rasgo computado para "Last Product Viewed Item", aparecerá en los perfiles de Braze de los usuarios como `Trait Computed` con el recuento correspondiente y la marca de tiempo más reciente en **Custom Events**. Si, en cambio, se tratara de una audiencia de Engage, encontrarías la audiencia, el recuento y la marca de tiempo más reciente en **Custom Attributes** configurados como `true`.

| Rasgo computado | Audiencias |
| -------------- | --------- |
| ![La sección de eventos personalizados dentro del perfil de usuario muestra "Trait Computed" "1" vez, siendo la última vez "hace 20 horas".]({% image_buster /assets/img/segment/last_viewed-track-braze.png %}) | ![La sección de atributos personalizados dentro de un perfil de usuario muestra "Audience Entered" "1" vez, siendo la última vez "9 de marzo a la 1:45 am".]({% image_buster /assets/img/segment/dormant-track-braze.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rasgos computados y audiencias" }

{% endtab %}
{% endtabs %}

### Paso 2: Segmentar usuarios en Braze {#step-2-segment-users-in-braze}

En Braze, para crear un segmento de estos usuarios, ve a **Segments** en **Engagement**, crea un nuevo segmento y dale un nombre. A continuación, en función de la llamada que hayas utilizado:
- **Identify**: Selecciona **custom attribute** como filtro y localiza tu atributo personalizado. A continuación, utiliza la opción "matches regex" (rasgo) o la opción "equals" (audiencia) e introduce la variable adecuada.
- **Track**: Selecciona **custom event** como filtro y localiza tu evento personalizado. A continuación, utiliza la opción "more than", "less than" o "exactly", e introduce el valor que desees. Esto dependerá de cómo quieras definir tu segmento.

Una vez guardado, puedes hacer referencia a este segmento durante la creación de Canvas o Campaigns en el paso de segmentación de usuarios.

## Tiempo de sincronización {#sync-time}

Aunque la configuración predeterminada para la conexión de Braze a Segment Engage es `Realtime`, hay algunos filtros que descalificarán a la persona para la sincronización en tiempo real, incluidos algunos filtros basados en el tiempo que restringen el tamaño de tu audiencia en el momento del envío del mensaje.

## Prueba del depurador de Segment {#segment-debugger-testing}

El panel de Segment proporciona una característica de "Debugger" que permite a los clientes probar si los datos de una "Source" se transfieren a un "Destination" como se esperaba.

Esta característica se conecta al [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) de Braze, lo que significa que solo puede utilizarse para usuarios identificados (usuarios que ya tienen un ID de usuario para su perfil de usuario de Braze).

Esto no funcionará para una integración en paralelo con Braze. No se transmitirá ningún dato del servidor si no has introducido la información correcta de la REST API de Braze.