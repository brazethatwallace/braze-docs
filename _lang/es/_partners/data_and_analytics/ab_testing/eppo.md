---
nav_title: Eppo
article_title: Eppo
description: "Aprende a integrar Eppo con Braze."
alias: /partners/eppo/
page_type: partner
search_tag: Partner
---

# Eppo

> [Eppo](https://www.geteppo.com/) es una plataforma de experimentación de nueva generación que permite a los equipos realizar pruebas A/B, gestionar características a escala y aprovechar la información basada en IA para la toma de decisiones basada en datos.

*Esta integración está mantenida por Eppo.*

La integración de Braze y Eppo te permite configurar pruebas A/B en Braze y analizar los resultados en Eppo para descubrir información y vincular el rendimiento de los mensajes a métricas empresariales a largo plazo, como los ingresos o la retención.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|------------------------------------|-------------------------------------------------------------------------------------|
| Cuenta Eppo | Se necesita una cuenta de Eppo para beneficiarse de esta asociación. |
| Currents o uso compartido de datos de Snowflake | Para que Eppo analice los datos de los experimentos, es necesario Currents o el uso compartido de datos de Snowflake. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Configurar Currents o el uso compartido de datos de Snowflake en Braze {#step-1-configure-currents-or-snowflake-data-sharing-in-braze}

Eppo analiza los experimentos directamente en tu almacén de datos. Para habilitar la integración, los datos de interacción con mensajes de Braze deben estar disponibles en el almacén conectado a Eppo. Puedes exportar datos de campañas desde Braze utilizando Currents, o acceder a los datos de Braze en tu instancia de Snowflake utilizando el [uso compartido de datos de Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/).

### Paso 2: Configura tu experimento en una campaña o Canvas de Braze {#step-2-set-up-your-experiment-in-a-braze-campaign-or-canvas}

Puedes utilizar las características nativas de pruebas A/B en tus campañas y Canvas. Para saber más, consulta [Pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#what-are-multivariate-and-ab-testing).

### Paso 3: Configurar Eppo para medir experimentos de Braze {#step-3-set-up-eppo-to-measure-braze-experiments}

Para realizar experimentos utilizando datos de Braze en Eppo, crea [tablas de asignaciones](https://docs.geteppo.com/data-management/definitions/assignment-sql/) en tu almacén basadas en los datos de eventos de mensajes a nivel de usuario exportados desde Braze. Se recomiendan tablas separadas para los experimentos en Canvas y en campañas, porque se basan en metadatos diferentes.

{% tabs local %}
{% tab canvas experiments %}
Para los experimentos en Canvas, las asignaciones pueden crearse de dos formas:

- En el nivel de entrada de Canvas (`users.canvas.Entry`)
- O en un paso de experimento en Canvas (`users.canvas.experimentstep.SplitEntry`)

En estos casos, se utilizan campos como `canvas_name`, `experiment_step_id`, `canvas_variation_name` y `experiment_split_id` para definir el nombre y la variante del experimento.

{% endtab %}

{% tab campaign experiments %}
Para los experimentos de campañas, utiliza eventos de envío (como push, correo electrónico, SMS) para determinar cuándo un usuario entró en el experimento. Se utilizan `campaign_name`, `message_variation_name` y `time` para rellenar la tabla de asignaciones.

{% endtab %}
{% endtabs %}

Para hacer un seguimiento de las métricas específicas de los mensajes (como clics o aperturas), incluye una **entidad secundaria** creando un `combined_id` que una el ID de usuario con el nombre de la campaña o Canvas. Este `combined_id` también se utiliza en tus tablas de hechos para alinear las métricas con el experimento y la variante correctos.

Eppo utiliza estas asignaciones y tablas de hechos para analizar los resultados, y se recomienda establecer un **protocolo** en Eppo para estandarizar la configuración de futuros experimentos. Para más información, consulta [la documentación de Eppo](https://docs.geteppo.com/guides/marketing/integrating-with-braze/).

## Soporte {#support}

Si tienes preguntas sobre cómo configurar Braze Currents, el uso compartido de datos de Snowflake o configurar campañas multivariantes, ponte en contacto con tu administrador del éxito del cliente de Braze.

Si necesitas ayuda para configurar Eppo para medir experimentos de Braze, ponte en contacto con el equipo de soporte de Eppo.