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

| Requisito                          | Descripción                                                                         |
|------------------------------------|-------------------------------------------------------------------------------------|
| Cuenta de Eppo                     | Se requiere una cuenta de Eppo para aprovechar esta integración.                    |
| Currents o Snowflake Data Sharing  | Se requiere Currents o Snowflake Data Sharing para que Eppo pueda analizar los datos del experimento. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Configura Currents o Snowflake Data Sharing en Braze {#step-1-configure-currents-or-snowflake-data-sharing-in-braze}

Eppo analiza experimentos directamente en tu almacén de datos. Para habilitar la integración, los datos de participación en mensajes de Braze deben estar disponibles en el almacén conectado a Eppo. Puedes exportar datos de Campaigns desde Braze utilizando Currents, o acceder a los datos de Braze en tu instancia de Snowflake mediante [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake).

### Paso 2: Configura tu experimento en una Campaign o Canvas de Braze {#step-2-set-up-your-experiment-in-a-braze-campaign-or-canvas}

Puedes utilizar las características nativas de pruebas A/B en tus Campaigns y Canvas. Para obtener más información, consulta [Pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

### Paso 3: Configura Eppo para medir los experimentos de Braze {#step-3-set-up-eppo-to-measure-braze-experiments}

Para ejecutar experimentos utilizando datos de Braze en Eppo, crea [tablas de asignaciones](https://docs.geteppo.com/data-management/definitions/assignment-sql/) en tu almacén basándote en los datos de eventos de mensajes a nivel de usuario exportados desde Braze. Se recomiendan tablas separadas para los experimentos en Canvas y en Campaigns, ya que dependen de metadatos diferentes.

{% tabs local %}
{% tab experimentos en Canvas %}
Para los experimentos en Canvas, las asignaciones pueden crearse de dos formas:

- A nivel de entrada del Canvas (`users.canvas.Entry`)
- O en un paso de experimento en Canvas (`users.canvas.experimentstep.SplitEntry`)

En estos casos, campos como `canvas_name`, `experiment_step_id`, `canvas_variation_name` y `experiment_split_id` se utilizan para definir el nombre del experimento y la variante.

{% endtab %}

{% tab experimentos en Campaigns %}
Para los experimentos en Campaigns, utiliza eventos de envío (como push, correo electrónico o servicio de mensajes cortos) para determinar cuándo un usuario entró en el experimento. Los campos `campaign_name`, `message_variation_name` y `time` se utilizan para poblar la tabla de asignaciones.

{% endtab %}
{% endtabs %}

Para realizar un seguimiento de métricas específicas de mensajes (como clics o aperturas), incluye una **Entidad secundaria** creando un `combined_id` que una el ID del usuario con el nombre de la Campaign o el Canvas. Este `combined_id` también se utiliza en tus tablas de hechos para alinear las métricas con el experimento y la variante correctos.

Eppo utiliza estas asignaciones y tablas de hechos para analizar resultados, y se recomienda configurar un **Protocolo** en Eppo para estandarizar la configuración de futuros experimentos. Para más información, consulta la [documentación de Eppo](https://docs.geteppo.com/guides/marketing/integrating-with-braze/).

## Soporte {#support}

Si tienes preguntas sobre la configuración de Braze Currents, el uso compartido de datos de Snowflake o la configuración de Campaigns multivariantes, contacta a tu CSM or administrador de éxito de cliente or administrador de éxito de cliente de Braze.

Para obtener asistencia con la configuración de Eppo para medir experimentos de Braze, contacta al equipo de soporte de Eppo.