---
nav_title: Facturación
article_title: Facturación
alias: /subscription_and_usage/
page_order: 5
page_type: reference
description: "Este artículo de referencia cubre la página de facturación, donde puedes supervisar y comprobar tu consumo de datos."
tool: Dashboard
search_rank: 5
---

# Facturación {#billing}

> Aprende a usar la página **Facturación** para supervisar y comprobar tu consumo de datos en espacios de trabajo, aplicaciones y fuentes de eventos. Este artículo cubre las diferentes secciones de la página y la información que pueden proporcionarte.

Para ir a la página **Facturación**, ve a **Configuración** > **Facturación**.

La página **Facturación** incluye las siguientes pestañas:

- [Suscripciones y uso](#subscriptions-and-usage)
- [Eventos y atributos más utilizados por aplicación](#most-used-events-and-attributes-by-app)
- [Total de uso de puntos de datos](#total-data-points-dashboard)

## Suscripciones y uso {#subscriptions-and-usage}

La pestaña **Suscripciones y uso** incluye gráficos de uso y los detalles de tu contrato. Los datos de esta página se actualizan diariamente a las 10:00 PM hora del este (ET). No reflejan la actividad en tiempo real.

### Gráficos de uso {#usage-graphs}

Aquí encontrarás gráficos de uso que aplican a tus espacios de trabajo. Es posible que tu propio panel muestre diferentes métricas de uso según los productos que hayas adquirido.

![Gráfico de uso que muestra visitantes únicos mensuales]({% image_buster /assets/img/subscription_and_billing4.png %}){: style="max-width:90%;"}

Estos gráficos pueden mostrar MAU or usuarios activos al mes or usuarios activos al mes, visitantes únicos mensuales y envíos de correo electrónico. Los gráficos de uso como estos son particularmente útiles cuando intentas presupuestar el uso y obtener una comprensión más profunda de qué espacios de trabajo contribuyen al uso general.

### Detalles del contrato {#contract-details}

Los detalles del contrato enumeran la fecha de inicio y finalización de tu contrato actual con Braze.

#### Consideraciones {#considerations}

Si tu contrato utiliza visitantes únicos mensuales (MUV) y cambias a un contrato que solo utiliza MAU or usuarios activos al mes or usuarios activos al mes (MAU or usuarios activos al mes), tus datos históricos seguirán apareciendo en el gráfico de MUV y tus nuevos datos aparecerán solo en el gráfico de MAU or usuarios activos al mes. Por ejemplo, si tu contrato finaliza en octubre, el gráfico de MUV muestra datos hasta finales de septiembre.

## Eventos y atributos más utilizados por aplicación {#most-used-events-and-attributes-by-app}

En **Eventos y atributos más utilizados por aplicación**, puedes comprobar los factores que impulsan el uso de puntos de datos de tus atributos y eventos personalizados.

![Eventos y atributos más utilizados por aplicación]({% image_buster /assets/img/most_used_events_attributes_time.png %})

Para cada aplicación, puedes seleccionar **Ver desglose** para ver un recuento estimado de cada atributo personalizado, atributo de perfil y evento personalizado específico para el período de tiempo seleccionado, así como el porcentaje de las actualizaciones de atributos y eventos de esa aplicación que fueron impulsadas por ese atributo o evento.

![Pestaña de desglose de eventos y atributos más utilizados por aplicación]({% image_buster /assets/img/most_used_events_attributes_2.png %}){: style="max-width:60%"}

Los desgloses de datos como estos pueden ayudarte a entender qué puntos de datos específicos están ocupando grandes porcentajes de tu asignación. Te recomendamos que supervises esta información de vez en cuando para asegurarte de que no estés gastando puntos de datos de manera accidental e innecesaria. Tu CSM or administrador de éxito de cliente or administrador de éxito de cliente puede orientarte para sacar el máximo provecho de tu plan actual o proporcionarte opciones para una mayor flexibilidad.

## Dashboard de total de puntos de datos {#total-data-points-dashboard}

La pestaña **Total de uso de puntos de datos** proporciona una visión detallada del uso de tus puntos de datos. Puedes ver todos los datos en esta sección agregados por semanas o por meses.

{% alert note %}
La información de puntos de datos se almacena en caché cada 24 horas.
{% endalert %}

Si eres administrador y no puedes ver la pestaña **Total de uso de puntos de datos**, asegúrate de que tu navegador permita cookies de terceros para el dominio de tu panel de Braze y de que no esté en modo incógnito.

![Filtrado del uso de puntos de datos por semanas]({% image_buster /assets/img/subscription_and_billing2.png %})

### Detalles del contrato

Aquí encontrarás información sobre cuándo comienza y termina tu contrato actual con Braze, así como los puntos de datos asignados y una suma de todos los puntos de datos que se han utilizado hasta el momento en tu contrato actual.

Los campos en esta sección se definen de la siguiente manera:

- **Tipo de contrato:** Estructura del período de facturación, ya sea anual o multianual.
- **Fecha de inicio y finalización del contrato:** Fecha de inicio y finalización del contrato completo.
- **Puntos de datos asignados:** La cantidad de puntos de datos asignados en el contrato por período de facturación.
- **Uso de puntos de datos del contrato:** Un total acumulado de todos los puntos de datos registrados durante la vigencia del contrato, que no se restablece en el siguiente período de facturación.

### Datos de facturación de la empresa {#company-billing-data}

#### Uso total de puntos de datos a nivel de aplicación {#app-level-total-data-point-usage}

Este gráfico muestra el uso de puntos de datos en todas las aplicaciones.

![El uso total de puntos de datos a nivel de aplicación muestra los puntos de datos utilizados para cada aplicación.]({% image_buster /assets/img/app_level_total.png %})

Selecciona uno de los totales para ver la tabla **Uso de puntos de datos a lo largo del tiempo**, que muestra los totales semanales de puntos de datos para cada espacio de trabajo. Las filas que tienen una columna **Nombre de la aplicación** en blanco representan puntos de datos que no están asociados con ninguna aplicación (como los puntos de datos utilizados en solicitudes que no especifican un `app_id`).

![Uso de puntos de datos a lo largo del tiempo que muestra los totales semanales de puntos de datos para dos espacios de trabajo.]({% image_buster /assets/img/data_point_usage_time.png %})

#### Uso de puntos de datos por espacio de trabajo {#workspace-data-point-usage}

Este gráfico te permite evaluar el uso total de puntos de datos de una empresa por espacio de trabajo. Te da la posibilidad de ver cómo cada espacio de trabajo contribuye al uso de puntos de datos de la empresa.

![Gráfico de uso de puntos de datos por espacio de trabajo para dos espacios de trabajo]({% image_buster /assets/img/appgroup_datapoint_usage.png %}){: style="max-width:90%;"}

#### Uso de puntos de datos del ciclo de facturación por fuente de eventos {#billing-cycle-data-point-usage-by-event-source}

Este gráfico te permite ver cómo se distribuye el uso de puntos de datos entre diferentes fuentes de eventos, como diferentes atributos de API, eventos personalizados y sesiones.

![Uso de puntos de datos del ciclo de facturación por fuente de eventos que muestra la asignación de puntos de datos entre diferentes fuentes de eventos.]({% image_buster /assets/img/event_source_stats.png %})

#### Uso de puntos de datos a lo largo del tiempo {#data-point-usage-over-time}

Este gráfico te permite ver rápidamente tu uso total de puntos de datos en comparación con tu cantidad asignada de puntos de datos.

![Uso de puntos de datos a lo largo del tiempo que contrasta los puntos de datos asignados del ciclo de facturación actual con el total acumulado]({% image_buster /assets/img/company_data_point_usage_time.png %}){: style="max-width:90%;"}

## Próximos pasos {#next-steps}

- [Preferencias de notificación]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences) para configurar alertas de eventos relacionados con la facturación y umbrales de uso.
- [Dashboard de uso de créditos]({{site.baseurl}}/credits_usage_dashboard) para supervisar el consumo de créditos de mensajes.