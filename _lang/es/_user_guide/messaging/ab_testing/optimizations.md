---
nav_title: Optimizaciones
article_title: Optimiza las pruebas A/B con variante ganadora o variantes personalizadas
page_order: 1
page_type: reference
description: "Aprende a utilizar la variante ganadora o la variante personalizada al crear pruebas multivariantes y pruebas A/B."
---

# Optimiza las pruebas A/B con variante ganadora o variantes personalizadas {#optimize-ab-tests-with-winning-variant-or-personalized-variants}

> Aprende a utilizar la variante ganadora o la variante personalizada al crear pruebas multivariantes y pruebas A/B.

Al [crear una prueba A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests/) para campañas de correo electrónico, push, webhook, SMS y WhatsApp programadas para un solo envío, puedes seleccionar una optimización. Hay dos opciones de optimización: **Winning Variant** y **Personalized Variant**.

![Opciones de optimización listadas en la sección de pruebas A/B al elegir tu audiencia objetivo. Se listan tres opciones: Sin optimización, Variante ganadora y Variante personalizada. Variante personalizada está seleccionada.]({% image_buster /assets/img_archive/ab_personalized_variant.png %})

Ambas opciones funcionan enviando una prueba inicial a un porcentaje de tu segmento objetivo. Una vez finalizada la prueba, los usuarios restantes de tu audiencia reciben la variante con mejor rendimiento (variante ganadora) o la variante con la que es más probable que interactúen (variante personalizada).

{% alert tip %}
Las optimizaciones se encuentran en el paso **Target Audiences** de la creación de campañas, en **A/B Testing**.
{% endalert %}

## Variante ganadora {#winning-variant}

Enviar la variante ganadora es similar a una prueba A/B estándar. Los usuarios de este grupo recibirán la variante ganadora cuando se complete la prueba inicial.

1. Selecciona **Winning Variant** y especifica qué porcentaje de la audiencia de tu campaña debe asignarse al grupo de variante ganadora.
2. Configura los siguientes ajustes adicionales.

| Campo | Descripción |
| --- | --- |
| Determine Winning Variant | La métrica a optimizar. Elige entre *Unique Opens* o *Clicks* para correo electrónico, *Opens* para push, o *Primary Conversion Rate* para todos los canales. Seleccionar *Opens* o *Clicks* para determinar la ganadora no afecta lo que elijas para los [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) de la campaña. <br><br>Ten en cuenta que si estás utilizando un grupo de control, los usuarios del grupo de control no pueden realizar *Opens* ni *Clicks*, por lo que el rendimiento del grupo de control será `0`. Como resultado, el grupo de control no puede ganar la prueba A/B. Sin embargo, es posible que aún quieras usar un grupo de control para hacer seguimiento de otras métricas para los usuarios que no reciben un mensaje. |
| Winning Variant Send Time | La fecha y hora en que se envía la variante ganadora. |
| If No Winning Variant Can Be Determined | Qué sucede si ninguna variante gana por un margen estadísticamente significativo. Elige entre enviar la variante con mejor rendimiento de todos modos o finalizar la prueba y no enviar más mensajes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Winning Variant" }

## Variante personalizada {#personalized-variant}

Usa las variantes personalizadas para enviar a cada usuario de tu segmento objetivo la variante con la que es más probable que interactúe.

Para determinar la mejor variante para cada usuario, Braze enviará una prueba inicial a una parte de tu audiencia objetivo para buscar asociaciones entre las características de los usuarios y las preferencias de mensajes. Según cómo respondan los usuarios a cada variante en la prueba inicial, estas características se utilizan para determinar qué usuarios restantes recibirán cada variante. Si no se encuentran asociaciones y no se pueden hacer personalizaciones, la variante ganadora se envía automáticamente a los usuarios restantes. Para obtener más información sobre cómo se determinan las variantes personalizadas, consulta [Análisis de pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics/#personalized-variant).

1. Selecciona **Personalized Variant** y especifica qué porcentaje de la audiencia de tu campaña debe asignarse al grupo de variante personalizada.
2. Configura los siguientes ajustes adicionales.

| Campo | Descripción |
| --- | --- |
| Determine Personalized Variant | La métrica a optimizar. Elige entre *Unique Opens* o *Clicks* para correo electrónico, *Opens* para push, o *Primary Conversion Rate* para todos los canales. Seleccionar *Opens* o *Clicks* para determinar la ganadora no afecta lo que elijas para los [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) de la campaña. <br><br>Ten en cuenta que si estás utilizando un grupo de control, los usuarios del grupo de control no pueden realizar *Opens* ni *Clicks*, por lo que el rendimiento del grupo de control será `0`. Como resultado, el grupo de control no puede ganar la prueba A/B. Sin embargo, es posible que aún quieras usar un grupo de control para hacer seguimiento de otras métricas para los usuarios que no reciben un mensaje. |
| Personalized Variant Send Time | La fecha y hora en que se envía la variante personalizada. |
| If No Personalized Variant Can Be Determined | Qué sucede si no se encuentran variantes personalizadas. Elige entre enviar la variante ganadora en su lugar o finalizar la prueba y no enviar más mensajes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Personalized Variant" }

## Análisis {#analytics}

Para conocer los resultados de tu prueba A/B con una optimización, consulta [Análisis de pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics/).