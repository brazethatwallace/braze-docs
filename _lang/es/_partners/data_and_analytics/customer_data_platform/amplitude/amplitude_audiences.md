---
nav_title: Amplitude
article_title: Amplitude
page_order: 0
alias: /partners/amplitude_recommend/
description: "Este artículo de referencia describe la asociación entre Braze y Amplitude, una plataforma de análisis de productos e inteligencia empresarial."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomamplitude-integration-with-braze-stylefloatrightwidth120pxborder0-classnoimgborderamplitude}

> [Amplitude](https://amplitude.com/) es una plataforma de análisis de productos e inteligencia empresarial.

La integración bidireccional de Braze y Amplitude te permite [importar tus cohortes de Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import/), rasgos de usuario y eventos a Braze, así como crear segmentos que pueden dirigirse a los usuarios en futuras Campaigns o Canvas. También puedes aprovechar Braze Currents para [exportar tus eventos de Braze a Amplitude]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/#data-export-integration) y realizar análisis más profundos de tus datos de producto y marketing.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta de Amplitude | Se necesita una [cuenta de Amplitude](https://amplitude.com/) para beneficiarse de esta asociación. |
| Currents | Para poder exportar los datos a Amplitude, debes tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) en tu cuenta. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Elige una integración {#choose-an-integration}

Amplitude y Braze ofrecen dos métodos de integración diferentes. Lee la documentación siguiente para decidir qué métodos se ajustan a tus necesidades:

- Braze Event Streaming: una integración que te permite enviar datos de eventos de Amplitude sin procesar directamente a Braze.
- [Importación de cohortes]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import/): una integración que permite reenviar cohortes de Amplitude a Braze.

## Braze Event Streaming

### Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Clave de API REST de Braze | Una clave de API REST de Braze con todos los permisos.<br><br> Puede crearse en el dashboard de Braze desde **Settings** > **API Keys**. |
| Punto de conexión REST de Braze | [La URL de tu punto de conexión REST][1]. Tu punto de conexión dependerá de la URL de Braze de tu instancia. |
| Identificador de la aplicación Braze | El identificador de la aplicación que recibirá los eventos de Amplitude. Esto se puede encontrar en **Braze Dashboard > Developer Console > Settings**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

### Configuración de Amplitude {#amplitude-setup}

1. En Amplitude, ve a **Data Destinations** y busca "Braze - Event Stream".
2. Introduce un nombre para la sincronización y haz clic en **Create Sync**.
3. Haz clic en **Edit** e indica tu punto de conexión REST API de Braze, tu clave de API REST y el identificador de la aplicación Braze.
4. Utiliza el filtro de envío de eventos para seleccionar los eventos que deseas enviar. Puedes enviar todos los eventos, pero Amplitude recomienda elegir los más importantes.
5. Cuando hayas terminado, habilita el destino y guárdalo.

Consulta [Braze Event Streaming](https://www.docs.developers.amplitude.com/data/destinations/braze/) para obtener más información sobre esta integración.

## Sincronizar rasgos de usuario y cómputos {#sync-user-traits-and-computations}

Utiliza Audiences para enviar propiedades de usuario y cálculos a Braze como atributos personalizados. Podrás sincronizar las propiedades de los usuarios o las propiedades computadas de los usuarios que hayan estado activos en los últimos 90 días.

Cuando se actualice una propiedad de usuario o un cálculo, Amplitude actualizará un atributo personalizado en Braze con el mismo nombre que esa propiedad de usuario o cálculo.

Las sincronizaciones de rasgos de usuario y cómputos crearán nuevos usuarios para identificadores de usuario que aún no existan en Braze. Los cómputos y los rasgos de usuario solo pueden sincronizarse utilizando identificadores de usuario. Un identificador de usuario puede ser cualquiera de los siguientes:
- ID externo
- ID de Braze
- Alias de usuario
- Dirección de correo electrónico

Consulta la documentación de Amplitude para obtener más información sobre la [sincronización de propiedades, recomendaciones y cohortes con destinos de terceros](https://help.amplitude.com/hc/en-us/articles/360060055531).

#### Cómo sincronizar las propiedades y los cálculos de los usuarios {#how-to-sync-user-properties-and-computations}

En Amplitude Audiences, selecciona **Syncs > Create Sync**.

![]({% image_buster /assets/img/amplitude11.png %})

A continuación, elige sincronizar una propiedad de usuario, un cálculo, una cohorte o una recomendación.

{% tabs %}
{% tab Syncing user property %}

Selecciona **User Property** y, a continuación, la propiedad de usuario que desees sincronizar.

![]({% image_buster /assets/img/amplitude7.png %})

A continuación, selecciona un destino con el que sincronizar tu propiedad de usuario.

![]({% image_buster /assets/img/amplitude8.png %})

Por último, define la frecuencia de tu sincronización.

![Define tu cadencia como sincronización única o sincronización programada.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% tab Syncing computation %}

Selecciona **Computation** y, a continuación, el cálculo que desees sincronizar.

![]({% image_buster /assets/img/amplitude10.png %})

A continuación, selecciona un destino para sincronizar tu cálculo.

![]({% image_buster /assets/img/amplitude8.png %})

Por último, define la frecuencia de tu sincronización.

![Define tu cadencia como sincronización única o sincronización programada.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% endtabs %}

## Solución de problemas {#troubleshooting}

### "We do not have enough data yet for this filter" al sincronizar una cohorte {#we-do-not-have-enough-data-yet-for-this-filter-when-syncing-a-cohort}

Si recibes este error al [importar una cohorte de Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import/) a Braze, prueba lo siguiente:

1. **Confirma la alineación del ID de usuario.** El User ID en Amplitude (no el Amplitude ID) debe coincidir exactamente con el External User ID en Braze (no el Braze o BSON ID). Por ejemplo, el User ID `12345` en Amplitude debe coincidir con el External User ID `12345` en Braze.
2. **Regenera tu clave de API de Braze.** En el dashboard de Braze, ve a **Partner Integrations** > **Technology Partners** > **Amplitude** y selecciona **Generate New Key**. Luego vuelve a intentar la sincronización de la cohorte de Amplitude con la nueva clave de API.
3. **Confirma que la cohorte se sincronizó en Amplitude.** Ponte en contacto con el [soporte de Amplitude](https://help.amplitude.com/) para confirmar que la cohorte se sincronizó correctamente del lado de Amplitude antes de seguir solucionando problemas en Braze.

## Puntos de conexión de la API del perfil de usuario de Amplitude {#amplitude-user-profile-api-endpoints}

Para consultar algunos de los puntos de conexión comunes de la API de Amplitude que se pueden utilizar con contenido conectado, consulta nuestra [documentación sobre la API de Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_user_profile_api/).