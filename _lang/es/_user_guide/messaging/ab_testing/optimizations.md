---
nav_title: Optimizaciones
article_title: Optimiza las pruebas A/B con Variantes Ganadoras o Variantes Personalizadas
page_order: 1
page_type: reference
description: "Aprende a utilizar la Variante Ganadora o la Variante Personalizada al crear pruebas multivariante y pruebas A/B."
---

# Optimiza las pruebas A/B con Variantes Ganadoras o Variantes Personalizadas {#optimize-ab-tests-with-winning-variant-or-personalized-variants}

> Aprende a utilizar la Variante Ganadora o la Variante Personalizada al crear pruebas multivariante y pruebas A/B.

Al [crear una prueba A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests/) para campañas de correo electrónico, push, webhook, SMS y WhatsApp programadas para un solo envío, puedes seleccionar una optimización. Hay dos opciones de optimización: **Variante Ganadora** y **Variante Personalizada**.

![Opciones de optimización listadas en la sección de pruebas A/B al elegir tu audiencia objetivo. Se listan tres opciones: Sin optimización, Variante Ganadora y Variante Personalizada. Variante Personalizada está seleccionada.]({% image_buster /assets/img_archive/ab_personalized_variant.png %})

Ambas opciones funcionan enviando una prueba inicial a un porcentaje de tu segmento objetivo. Una vez finalizada la prueba, los usuarios restantes de tu audiencia reciben la variante con mejor rendimiento (Variante Ganadora) o la variante con la que es más probable que interactúen (Variante Personalizada).

{% alert tip %}
Las optimizaciones se encuentran en el paso **Públicos objetivo** de la creación de campañas, en **Pruebas A/B**.
{% endalert %}

## Variante Ganadora {#winning-variant}

Enviar la Variante Ganadora es similar a una prueba A/B estándar. Los usuarios de este grupo recibirán la Variante Ganadora cuando se complete la prueba inicial.

1. Selecciona **Variante Ganadora** y especifica qué porcentaje de la audiencia de tu campaña debe asignarse al grupo de Variante Ganadora.
2. Configura los siguientes ajustes adicionales.

| Campo | Descripción |
| --- | --- |
| Determinar Variante Ganadora | La métrica a optimizar. Elige entre *Aperturas únicas* o *Clics* para correo electrónico, *Aperturas* para push, o *Tasa de conversión primaria* para todos los canales. Seleccionar *Aperturas* o *Clics* para determinar la ganadora no afecta lo que elijas para los [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) de la campaña. <br><br>Ten en cuenta que si estás utilizando un grupo de control, los usuarios del grupo de control no pueden realizar *Aperturas* ni *Clics*, por lo que el rendimiento del grupo de control será `0`. Como resultado, el grupo de control no puede ganar la prueba A/B. Sin embargo, es posible que aún quieras usar un grupo de control para hacer seguimiento de otras métricas para los usuarios que no reciben un mensaje. |
| Hora de envío de la Variante Ganadora | La fecha y hora en que se envía la Variante Ganadora. |
| Si no se puede determinar una Variante Ganadora | Qué sucede si ninguna variante gana por un margen estadísticamente significativo. Elige entre enviar la variante con mejor rendimiento de todos modos o finalizar la prueba y no enviar más mensajes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Variante Personalizada {#personalized-variant}

Usa las Variantes Personalizadas para enviar a cada usuario de tu segmento objetivo la variante con la que es más probable que interactúe.

Para determinar la mejor variante para cada usuario, Braze enviará una prueba inicial a una parte de tu audiencia objetivo para buscar asociaciones entre las características de los usuarios y las preferencias de mensajes. Según cómo respondan los usuarios a cada variante en la prueba inicial, estas características se utilizan para determinar qué usuarios restantes recibirán cada variante. Si no se encuentran asociaciones y no se pueden hacer personalizaciones, la Variante Ganadora se envía automáticamente a los usuarios restantes. Para obtener más información sobre cómo se determinan las Variantes Personalizadas, consulta [Análisis de pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics/#personalized-variant).

1. Selecciona **Variante Personalizada** y especifica qué porcentaje de la audiencia de tu campaña debe asignarse al grupo de Variante Personalizada.
2. Configura los siguientes ajustes adicionales.

| Campo | Descripción |
| --- | --- |
| Determinar Variante Personalizada | La métrica a optimizar. Elige entre *Aperturas únicas* o *Clics* para correo electrónico, *Aperturas* para push, o *Tasa de conversión primaria* para todos los canales. Seleccionar *Aperturas* o *Clics* para determinar la ganadora no afecta lo que elijas para los [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) de la campaña. <br><br>Ten en cuenta que si estás utilizando un grupo de control, los usuarios del grupo de control no pueden realizar *Aperturas* ni *Clics*, por lo que el rendimiento del grupo de control será `0`. Como resultado, el grupo de control no puede ganar la prueba A/B. Sin embargo, es posible que aún quieras usar un grupo de control para hacer seguimiento de otras métricas para los usuarios que no reciben un mensaje. |
| Hora de envío de la Variante Personalizada | La fecha y hora en que se envía la Variante Personalizada. |
| Si no se puede determinar una Variante Personalizada | Qué sucede si no se encuentran Variantes Personalizadas. Elige entre enviar la Variante Ganadora en su lugar o finalizar la prueba y no enviar más mensajes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Análisis {#analytics}

Para conocer los resultados de tu prueba A/B con una optimización, consulta [Análisis de pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics/).