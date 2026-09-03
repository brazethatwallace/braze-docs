---
nav_title: Optimizaciones
article_title: Optimización de pruebas A/B
page_order: 1
page_type: reference
description: "Aprende a optimizar pruebas multivariantes y pruebas A/B de campañas con BrazeAI."
---

# Optimización de pruebas A/B {#optimizing-ab-tests}

> Usa **Optimizar con BrazeAI<sup>TM</sup>** para optimizar automáticamente una campaña con múltiples variantes.

En el paso **Públicos objetivo**, ve a **Pruebas A/B** y activa **Optimizar con BrazeAI<sup>TM</sup>**.

Para una campaña de envío único, BrazeAI<sup>TM</sup> envía una prueba inicial y luego envía la variante con mejor rendimiento a la audiencia restante. Para una campaña de envíos múltiples, BrazeAI<sup>TM</sup> revisa el rendimiento cada 12 horas y redirige a más usuarios hacia las variantes con mejor rendimiento.

Para prerrequisitos, opciones de configuración y detalles de informes, consulta [Optimización de pruebas A/B con BrazeAI]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection).

{% alert note %}
Las campañas existentes que usan variante personalizada siguen siendo compatibles con esa optimización y sus análisis. La variante personalizada no está disponible al crear una nueva campaña.
{% endalert %}

Braze verifica de nuevo la elegibilidad del usuario antes del segundo envío en una optimización de envío único. Los usuarios que no eran elegibles para la prueba inicial pueden entrar en la audiencia restante, mientras que los usuarios que ya no son elegibles no reciben el envío de seguimiento.

Para información sobre los resultados de la campaña, consulta [Análisis de pruebas A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics).