---
nav_title: Amplitude para Currents
article_title: Amplitude para Currents
page_order: 0
description: "Este artículo de referencia describe la asociación entre Braze Currents y Amplitude, una plataforma de análisis de productos e inteligencia empresarial."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude para Currents {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomamplitude-integration-with-braze-stylefloatrightwidth120pxborder0-classnoimgborderamplitude-for-currents}

> [Amplitude](https://amplitude.com/) es una plataforma de análisis de productos e inteligencia empresarial.

La integración bidireccional de Braze y Amplitude te permite [sincronizar tus cohortes de Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences/), rasgos de usuario y eventos en Braze, así como aprovechar Braze Currents para [exportar tus eventos de Braze a Amplitude](#data-export-integration) y realizar análisis más profundos de tus datos de producto y marketing.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta de Amplitude | Se necesita una [cuenta de Amplitude](https://amplitude.com/) para beneficiarse de esta asociación. |
| Currents | Para poder exportar datos a Amplitude, debes tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) en tu cuenta. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración de la exportación de datos {#data-export-integration}

Puedes encontrar una lista completa de los eventos y propiedades de eventos que se pueden exportar de Braze a Amplitude en las siguientes secciones. Todos los eventos enviados a Amplitude incluirán el `external_user_id` del usuario como ID de usuario de Amplitude. Las propiedades de eventos específicas de Braze se enviarán bajo la clave `event_properties` en los datos enviados a Amplitude.

{% alert important %}
Para utilizar esta función, tu ID de usuario de Amplitude debe coincidir con el ID externo de Braze.
{% endalert %}

Braze solo enviará datos de eventos para usuarios que tengan su `external_user_id` configurado o usuarios anónimos que tengan su `device_id` configurado. Para los usuarios anónimos, tendrás que sincronizar el ID de dispositivo de Amplitude con el ID de dispositivo de Braze en el SDK. Por ejemplo:

```java
amplitude.setDeviceId(Appboy.getInstance(context).getDeviceId();)
```

Puedes exportar dos tipos de eventos a Amplitude: [eventos de interacción con mensajes](#supported-currents-events), que consisten en los eventos de Braze directamente relacionados con el envío de mensajes, y [eventos de comportamiento del cliente](#supported-currents-events), que incluyen otra actividad de la aplicación o del sitio web, como sesiones, eventos personalizados y compras rastreadas a través de la plataforma. Todos los eventos regulares llevan el prefijo `[Appboy]`, y todos los eventos personalizados llevan el prefijo `[Appboy] [Custom Event]`. Las propiedades de eventos personalizados y eventos de compra llevan el prefijo `[Custom event property]` y `[Purchase property]`, respectivamente.

Todas las cohortes nombradas e importadas a Braze llevarán el prefijo `[Amplitude]` y el sufijo `cohort_id`. Esto significa que una cohorte denominada "TEST_COHORT" con el `cohort_id` "abcd1234" se titulará `[Amplitude] TEST_COHORT: abcd1234` en los filtros de Braze.

Ponte en contacto con tu director de cuentas o abre un [ticket de soporte]({{site.baseurl}}/braze_support/) si necesitas acceder a derechos de eventos adicionales.

### Paso 1: Configurar la integración de Amplitude en Braze {#step-1-configure-amplitude-integration-in-braze}

En Amplitude, localiza tu clave de API de exportación de Amplitude.

{% alert warning %}
Mantén actualizada tu clave de API de Amplitude. Si las credenciales de tu conector caducan, el conector dejará de enviar eventos. Si esto persiste durante más de **48 horas**, los eventos del conector se eliminarán y los datos se perderán permanentemente.
{% endalert %}

### Paso 2: Crear un Current en Braze {#step-2-create-braze-current}

En Braze, ve a **Currents > + Create Current > Create Amplitude Export**. Proporciona un nombre de integración, un correo electrónico de contacto, una clave de API de exportación de Amplitude y una región de Amplitude en los campos indicados. A continuación, selecciona los eventos que deseas rastrear; se proporciona una lista de los eventos disponibles. Por último, haz clic en **Launch Current**.

{% alert note %}
Los eventos enviados desde Braze Currents a Amplitude contarán para tu cuota de volumen de eventos de Amplitude.
{% endalert %}

![La página de Braze Amplitude Currents. Esta página incluye campos para el nombre de la integración, el correo electrónico de contacto, la clave de API y la región de EE. UU. La mitad inferior de la página de Currents enumera los eventos de Currents disponibles que puedes enviar.]({% image_buster /assets/img/amplitude4.png %})

{% tab note %}
Consulta la [documentación de integración](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration) de Amplitude para obtener más información.
{% endtab %}

## Límites de velocidad {#rate-limits}

Currents se conecta a la API HTTP de Amplitude, que tiene un [límite de velocidad](https://developers.amplitude.com/docs/http-api-v2#upload-limit) de 30 eventos/segundo por dispositivo y un límite no documentado de 500K eventos/día por dispositivo. Si se superan estos umbrales, Amplitude limitará los eventos registrados a través de Currents. Si un dispositivo de tu integración supera este límite de velocidad, puede que experimentes un retraso en el momento en que los eventos de todos los dispositivos aparezcan en Amplitude.

Los dispositivos no deberían reportar más de 30 eventos/segundo o 500K eventos/día en circunstancias normales, y este patrón de eventos solo debería producirse debido a una integración mal configurada. Para evitar este tipo de retraso, asegúrate de que tu integración de SDK reporta los eventos a un ritmo normal, tal y como se especifica en nuestras instrucciones de integración de SDK, y abstente de ejecutar pruebas automatizadas que generen muchos eventos para un único dispositivo.

## Eventos de Currents compatibles {#supported-currents-events}

Braze admite la exportación de los siguientes eventos a Amplitude:

- [Eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)
- [Eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)

Para la estructura de la carga útil de cada evento, selecciona la pestaña **Amplitude** en el [glosario de eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) y el [glosario de eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/).