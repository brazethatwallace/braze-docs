---
nav_title: Pruebas A/B
article_title: Pruebas A/B
page_order: 6
layout: dev_guide
guide_top_header: "Pruebas A/B"
guide_top_text: "Ejecuta experimentos para optimizar tu mensajería. Una prueba A/B compara las respuestas de los usuarios a múltiples versiones de la misma campaña, mientras que una prueba multivariante amplía esto a dos o más variables. En Braze, los términos se usan indistintamente porque el proceso de configuración es el mismo. Usa <a href=\"/docs/user_guide/brazeai/intelligence_suite/variant_selection\">Optimizar con BrazeAI<sup>TM</sup></a> para optimizar automáticamente tus resultados."

page_type: landing
description: "Configura y analiza pruebas A/B y experimentos multivariantes en Braze."

guide_featured_title: "Artículos de la sección"
guide_featured_list:
  - name: Conceptos
    link: /docs/user_guide/messaging/ab_testing/concepts
    image: /assets/img/braze_icons/lightbulb-02.svg
  - name: Crear pruebas
    link: /docs/user_guide/messaging/ab_testing/create_tests
    image: /assets/img/braze_icons/plus-circle.svg
  - name: Optimizaciones
    link: /docs/user_guide/messaging/ab_testing/optimizations
    image: /assets/img/braze_icons/settings-01.svg
  - name: Análisis
    link: /docs/user_guide/messaging/ab_testing/analytics
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: Preguntas frecuentes
    link: /docs/user_guide/messaging/ab_testing/faq
    image: /assets/img/braze_icons/annotation-question.svg
---

## Cuándo usar pruebas A/B {#when-to-use-ab-tests}

- **Probar un nuevo tipo de mensajería:** Experimenta y descubre qué conecta con tus usuarios.
- **Campaigns de incorporación o envíos recurrentes:** Asegúrate de que las campañas con alto tráfico sean lo más efectivas posible.
- **Múltiples ideas de mensajes:** Ejecuta una prueba y toma una decisión basada en datos.
- **Cuestionar suposiciones:** Comprueba si las tácticas de marketing convencionales realmente funcionan para tu audiencia específica.

## Consejos para ejecutar pruebas eficaces {#tips-for-running-effective-tests}

- **Usa muestras grandes** para asegurarte de que los resultados reflejen a tu usuario promedio y no se vean distorsionados por valores atípicos.
- **Aleatoriza los grupos de prueba** para que las diferencias en las tasas de respuesta reflejen diferencias en los mensajes, no en las muestras.
- **Ten claro qué estás probando.** Aislar un solo cambio identifica qué elemento tuvo el mayor impacto; probar múltiples diferencias te permite comparar enfoques más amplios.
- **Establece la duración de la prueba de antemano** y no la finalices antes de tiempo, incluso si los primeros resultados parecen prometedores.
- **Añade las pruebas antes de lanzar.** Agregar una prueba a una Campaign en curso produce resultados inexactos. Clona la Campaign, detén la original y añade la prueba al clon.
- **Incluye un [grupo de control]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#including-a-control-group)** para medir el impacto en comparación con no enviar ningún mensaje.