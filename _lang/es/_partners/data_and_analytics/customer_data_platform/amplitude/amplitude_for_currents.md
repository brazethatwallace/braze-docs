---
nav_title: Amplitude para Currents
article_title: Amplitude para Currents
page_order: 0
description: "Este artículo de referencia describe la asociación entre Braze Currents y Amplitude, una plataforma de análisis de productos e inteligencia empresarial."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude para Currents {#amplitude-for-currents}

> [Amplitude](https://amplitude.com/) es una plataforma de análisis de productos e inteligencia empresarial.

La integración bidireccional de Braze y Amplitude te permite [sincronizar tus cohortes de Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences), rasgos de usuario y eventos en Braze, así como aprovechar Braze Currents para [exportar tus eventos de Braze a Amplitude](#data-export-integration) y realizar análisis más profundos de tus datos de producto y marketing.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta de Amplitude | Se requiere una [cuenta de Amplitude](https://amplitude.com/) para aprovechar esta integración. |
| Currents | Para exportar datos de vuelta a Amplitude, necesitas tener [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) configurado para tu cuenta. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración de exportación de datos {#data-export-integration}

Puedes encontrar una lista completa de los eventos y propiedades del evento que se pueden exportar de Braze a Amplitude en las siguientes secciones. Todos los eventos enviados a Amplitude incluirán el `external_user_id` del usuario como ID de usuario de Amplitude. Las propiedades del evento específicas de Braze se enviarán bajo la clave `event_properties` en los datos enviados a Amplitude.

{% alert important %}
Para utilizar esta característica, tu ID de usuario de Amplitude debe coincidir con el ID externo de Braze.
{% endalert %}

Braze solo enviará datos de eventos para los usuarios que tengan configurado su `external_user_id` o para usuarios anónimos que tengan configurado su `device_id`. Para los usuarios anónimos, necesitarás sincronizar tu ID de dispositivo de Amplitude con el ID de dispositivo de Braze en el SDK. Por ejemplo:

```java
amplitude.setDeviceId(Appboy.getInstance(context).getDeviceId();)
```

Puedes exportar dos tipos de eventos a Amplitude: [eventos de participación en mensajes](#supported-currents-events), que consisten en los eventos de Braze directamente relacionados con el envío de mensajes, y [eventos de comportamiento del cliente](#supported-currents-events), que incluyen otras actividades de la aplicación o el sitio web, como sesiones, eventos personalizados y compras rastreadas a través de la plataforma. Todos los eventos regulares tienen el prefijo `[Appboy]`, y todos los eventos personalizados tienen el prefijo `[Appboy] [Custom Event]`. Las propiedades de eventos personalizados y de eventos de compra tienen el prefijo `[Custom event property]` y `[Purchase property]`, respectivamente.

{% alert note %}
Braze Currents aplica el prefijo `[Appboy]` al exportar eventos a Amplitude. La etiqueta hace referencia al nombre de producto heredado de Braze. Este es el comportamiento esperado y no indica un problema con el SDK o la integración.
{% endalert %}

Todas las cohortes nombradas e importadas a Braze tendrán el prefijo `[Amplitude]` y el sufijo de su `cohort_id`. Esto significa que una cohorte llamada "TEST_COHORT" con el `cohort_id` "abcd1234" se titulará `[Amplitude] TEST_COHORT: abcd1234` en los filtros de Braze.

Contacta a tu director de cuentas o abre un [ticket de soporte]({{site.baseurl}}/braze_support) si necesitas acceso a autorizaciones de eventos adicionales.

### Paso 1: Configurar la integración de Amplitude en Braze {#step-1-configure-amplitude-integration-in-braze}

En Amplitude, localiza tu clave de API de exportación de Amplitude.

{% alert warning %}
Mantén tu clave de API de Amplitude actualizada. Si las credenciales de tu conector caducan, el conector dejará de enviar eventos. Si esto persiste durante más de **48 horas**, los eventos del conector se descartarán y los datos se perderán permanentemente.
{% endalert %}

### Paso 2: Crear un Braze Current {#step-2-create-braze-current}

En Braze, ve a **Currents > + Create Current > Create Amplitude Export**. Proporciona un nombre de integración, correo electrónico de contacto, clave de API de exportación de Amplitude y región de Amplitude en los campos indicados. A continuación, selecciona los eventos que deseas rastrear; se proporciona una lista de eventos disponibles. Por último, haz clic en **Launch Current**

{% alert note %}
Los eventos enviados desde Braze Currents a Amplitude contarán para tu cuota de volumen de eventos de Amplitude.
{% endalert %}

![La página de Braze Amplitude Currents. Esta página incluye campos para el nombre de integración, correo electrónico de contacto, clave de API y región de EE. UU. La mitad inferior de la página de Currents muestra los eventos de Currents disponibles que puedes enviar.]({% image_buster /assets/img/amplitude4.png %})

{% alert tip %}
Si recibes un error de "Clave de API no válida" al pegar tu clave de API de Amplitude, intenta escribir la clave manualmente. Algunos navegadores pueden añadir caracteres ocultos al copiar y pegar, lo que puede provocar errores de validación.
{% endalert %}

{% tab note %}
Para obtener más información, consulta la documentación de Amplitude sobre la [integración de Appboy con Amplitude](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration).
{% endtab %}

## Límites de velocidad {#rate-limits}

Currents se conecta a la API HTTP de Amplitude, que tiene un [límite de velocidad](https://developers.amplitude.com/docs/http-api-v2#upload-limit) de 30 eventos/segundo por dispositivo y un límite no documentado de 500K eventos/día por dispositivo. Si se superan estos umbrales, Amplitude limitará los eventos registrados a través de Currents. Si un dispositivo en tu integración excede este límite de velocidad, es posible que experimentes un retraso en el momento en que los eventos de todos los dispositivos aparecerán en Amplitude.

Los dispositivos no deberían reportar más de 30 eventos/segundo o 500K eventos/día en circunstancias normales, y este patrón de eventos solo debería ocurrir debido a una integración mal configurada. Para evitar este tipo de retraso, asegúrate de que tu integración de SDK reporte eventos a una tasa normal, tal como se especifica en nuestras instrucciones de integración de SDK, y evita ejecutar pruebas automatizadas que generen muchos eventos para un solo dispositivo.

## Eventos de Currents compatibles {#supported-currents-events}

Braze permite exportar los siguientes eventos a Amplitude:

- [Eventos de participación en mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)
- [Eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)

Para consultar la estructura de la carga útil de cada evento, selecciona la pestaña **Amplitude** en el [glosario de eventos de participación en mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) y en el [glosario de eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).