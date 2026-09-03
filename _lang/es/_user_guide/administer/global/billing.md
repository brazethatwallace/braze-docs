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

Aquí encuentras gráficos de uso que aplican a tus espacios de trabajo. Es posible que tu propio panel muestre diferentes métricas de uso en función de los productos que hayas adquirido.

![Gráfico de uso que muestra visitantes únicos mensuales]({% image_buster /assets/img/subscription_and_billing4.png %}){: style="max-width:90%;"}

Estos gráficos pueden mostrar usuarios activos mensuales, visitantes únicos mensuales y envíos de correo electrónico. Los gráficos de uso como estos son particularmente útiles cuando intentas presupuestar el uso y obtener una comprensión más profunda de qué espacios de trabajo contribuyen al uso general.

### Detalles del contrato {#contract-details}

Los detalles del contrato enumeran la fecha de inicio y finalización de tu contrato actual con Braze.

#### Consideraciones {#considerations}

Si tu contrato utiliza visitantes únicos mensuales (MUV) y cambias a un contrato que utiliza solo usuarios activos mensuales (MAU), tus datos históricos seguirán apareciendo en el gráfico de MUV y tus nuevos datos aparecerán solo en el gráfico de MAU. Por ejemplo, si tu contrato finaliza en octubre, el gráfico de MUV muestra datos hasta finales de septiembre.

## Eventos y atributos más utilizados por aplicación {#most-used-events-and-attributes-by-app}

En **Eventos y atributos más utilizados por aplicación**, puedes consultar los factores que impulsan el uso de puntos de datos de tus atributos y eventos personalizados.

![Eventos y atributos más utilizados por aplicación]({% image_buster /assets/img/most_used_events_attributes_time.png %})

Para cada aplicación, puedes seleccionar **Ver desglose** para ver un recuento estimado de cada atributo personalizado, atributo de perfil y evento personalizado específico del periodo de tiempo seleccionado, así como el porcentaje de actualizaciones de atributos y eventos de esa aplicación que fueron impulsadas por ese atributo o evento.

![Pestaña de desglose de eventos y atributos más utilizados por aplicación]({% image_buster /assets/img/most_used_events_attributes_2.png %}){: style="max-width:60%"}

Desgloses de datos como estos pueden ayudarte a entender qué puntos de datos específicos están ocupando grandes porcentajes de tu asignación. Te recomendamos que monitorices esta información de vez en cuando para asegurarte de que no estás gastando puntos de datos de forma accidental e innecesaria. Tu administrador de éxito de cliente puede orientarte para sacar el máximo partido de tu plan actual o proporcionarte opciones con mayor flexibilidad.

## Dashboard de puntos de datos totales {#total-data-points-dashboard}

La pestaña **Uso total de puntos de datos** ofrece una visión detallada de tu uso de puntos de datos. Puedes ver todos los datos de esta sección agregados por semanas o meses.

{% alert note %}
La información de puntos de datos se almacena en caché cada 24 horas.
{% endalert %}

Si eres administrador y no puedes ver la pestaña **Uso total de puntos de datos**, asegúrate de que tu navegador permita cookies de terceros para el dominio de tu panel de Braze y de que no esté en modo incógnito.

![Filtrar el uso de puntos de datos por semanas]({% image_buster /assets/img/subscription_and_billing2.png %})

### Detalles del contrato

Aquí encontrarás información sobre cuándo comienza y termina tu contrato actual de Braze, así como los puntos de datos asignados y la suma de todos los puntos de datos que se han utilizado hasta el momento en tu contrato actual.

Los campos de esta sección se definen de la siguiente manera:

- **Tipo de contrato:** Estructura del periodo de facturación, ya sea anual o multianual.
- **Fecha de inicio y fin del contrato:** Fecha de inicio y fin de todo el contrato.
- **Puntos de datos asignados:** La cantidad de puntos de datos asignados en el contrato por periodo de facturación.
- **Uso de puntos de datos del contrato:** Un total acumulado de todos los puntos de datos registrados durante la vigencia del contrato, que no se restablece en el siguiente periodo de facturación.

### Datos de facturación de la empresa {#company-billing-data}

#### Uso total de puntos de datos a nivel de aplicación {#app-level-total-data-point-usage}

Este gráfico muestra tu uso de puntos de datos en todas las aplicaciones.

![El uso total de puntos de datos a nivel de aplicación muestra los puntos de datos utilizados para cada aplicación.]({% image_buster /assets/img/app_level_total.png %})

Selecciona uno de los totales para ver la tabla **Uso de puntos de datos a lo largo del tiempo**, que muestra los totales semanales de puntos de datos para cada espacio de trabajo. Las filas que tienen una columna **Nombre de la aplicación** en blanco representan puntos de datos que no están asociados con ninguna aplicación (como los puntos de datos utilizados en solicitudes que no especifican un `app_id`).

![Uso de puntos de datos a lo largo del tiempo mostrando los puntos de datos semanales totales para dos espacios de trabajo.]({% image_buster /assets/img/data_point_usage_time.png %})

#### Uso de puntos de datos por espacio de trabajo {#workspace-data-point-usage}

Este gráfico te permite evaluar el uso total de puntos de datos de una empresa por espacio de trabajo. Este gráfico te da la capacidad de evaluar cómo cada espacio de trabajo contribuye al uso de puntos de datos de la empresa.

![Gráfico de uso de puntos de datos por espacio de trabajo para dos espacios de trabajo]({% image_buster /assets/img/appgroup_datapoint_usage.png %}){: style="max-width:90%;"}

#### Uso de puntos de datos del ciclo de facturación por origen de evento {#billing-cycle-data-point-usage-by-event-source}

Este gráfico te permite ver cómo se distribuye el uso de puntos de datos entre diferentes orígenes de eventos, como distintos atributos de API, eventos personalizados y sesiones.

![Uso de puntos de datos del ciclo de facturación por origen de evento mostrando la distribución de puntos de datos entre los diferentes orígenes de eventos.]({% image_buster /assets/img/event_source_stats.png %})

#### Uso de puntos de datos a lo largo del tiempo {#data-point-usage-over-time}

Este gráfico te da la capacidad de ver rápidamente tu uso total de puntos de datos en comparación con tu cantidad asignada de puntos de datos.

![Uso de puntos de datos a lo largo del tiempo comparando los puntos de datos asignados del ciclo de facturación actual con el total acumulado]({% image_buster /assets/img/company_data_point_usage_time.png %}){: style="max-width:90%;"}

## Próximos pasos {#next-steps}

{% article_tiles %}
- name: Preferencias de notificación
  link: /docs/user_guide/administer/global/admin_settings/notification_preferences
- name: Dashboard de uso de créditos
  link: /docs/credits_usage_dashboard
{% endarticle_tiles %}