---
nav_title: Números de contenedor aleatorio
article_title: Números de contenedor aleatorio
page_order: 2
page_type: reference
description: "Este artículo cubre el concepto de números de contenedor aleatorio y cómo puedes usarlos para crear variantes y grupos de control."
page_type: reference
tool:
  - Campaign
  - Canvas

---

# Números de contenedor aleatorio {#random-bucket-numbers}

> Un número de contenedor aleatorio es un atributo de usuario que se puede utilizar para crear segmentos uniformemente distribuidos de usuarios aleatorios.

## Resumen {#overview}

Cuando se crea un perfil de usuario en Braze, a ese usuario se le asigna automáticamente un número de contenedor aleatorio entre 0 y 9999 (ambos inclusive). Puedes usar estos segmentos para probar la eficacia de múltiples campañas o Canvas en grupos de usuarios a lo largo del tiempo.

### Uso del grupo de control global {#global-control-group-usage}

Los números de contenedor aleatorio se utilizan en tu grupo de control global&#8212;un grupo de usuarios que no recibe ninguna campaña ni Canvas. Braze selecciona aleatoriamente múltiples rangos de números de contenedor aleatorio e incluye a los usuarios de esos contenedores seleccionados. Los números de contenedor aleatorio se asignan sin ponderación ni consideración de números asignados recientemente.

{% alert note %}
Cuando un usuario se elimina y se vuelve a crear, se le asigna un número de contenedor aleatorio diferente porque se considera un usuario nuevo.
{% endalert %}

Si tienes un grupo de control global configurado y quieres usar números de contenedor aleatorio para otros casos de uso, consulta [Aspectos a tener en cuenta]({{site.baseurl}}/user_guide/audience/global_control_group/#things-to-watch-for).

### Cuándo usar números de contenedor aleatorio {#when-to-use-random-bucket-numbers}

Si quieres realizar pruebas a largo plazo sobre la eficacia de múltiples campañas o Canvas a lo largo del tiempo, puedes usar números de contenedor aleatorio para segmentar a tus usuarios.

### Cuándo usar otra alternativa {#when-to-use-something-else}

Si quieres segmentar usuarios para pruebas dentro de una sola campaña o un solo Canvas, usa [pruebas A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests/) para campañas. Para Canvas, puedes crear diferentes [variantes]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-21-add-a-variant) para pruebas a nivel de recorrido, o usar [Recorridos de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/) para pruebas a nivel de paso.

## Crear segmentos usando números de contenedor aleatorio {#create-segments-using-random-bucket-numbers}

Al [crear un segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/), añade el filtro "Random Bucket #". Luego, especifica un número o rango de números para incluir en tu segmento.

![Un filtro de segmento para números de contenedor aleatorio no mayores a "3000".]({% image_buster /assets/img_archive/random_buckets_filterexample.png %})

Puede que quieras usar estos tipos de segmentos si deseas ejecutar una prueba de tres variantes diferentes e incluir también un grupo de control. Considera el siguiente plan de ejemplo para crear segmentos de igual tamaño para tres variantes y un grupo de control:

- Los números de contenedor 0 a 2499 corresponden al segmento de control
- Los números de contenedor 2500 a 4999 corresponden al segmento que recibirá la variante 1
- Los números de contenedor 5000 a 7499 corresponden al segmento que recibirá la variante 2
- Los números de contenedor 7500 a 9999 corresponden al segmento que recibirá la variante 3

Dependiendo de cuántos segmentos quieras y la distribución de usuarios dentro de cada segmento, tu plan puede verse diferente.

Para cada uno de tus segmentos de número de contenedor aleatorio, incluido el grupo de control, activa el [seguimiento de análisis]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/). Al evaluar el éxito de las variantes en relación con el grupo de control, puedes ir a tu página de [eventos personalizados]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report/) y ver con qué frecuencia cada segmento ha completado ciertos eventos personalizados.

{% alert tip %}
Al usar segmentos de número de contenedor aleatorio en un Canvas, por ejemplo como filtro en un paso de [División de decisiones]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/), asegúrate de que los [criterios de salida]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria/) de tu Canvas, los filtros de audiencia y los pasos anteriores no apunten a segmentos que se superpongan con uno de tus rangos de contenedores. Si lo hacen, los usuarios en ese rango pueden ser eliminados de forma desproporcionada antes de llegar a la división, causando una distribución desigual entre los recorridos.
{% endalert %}

### Reingreso aleatorio de audiencia usando números de contenedor aleatorio {#random-audience-re-entry-using-random-bucket-numbers}

El reingreso aleatorio de audiencia puede ser útil para [pruebas A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/#what-are-multivariate-and-ab-testing) o para dirigirte a grupos específicos de usuarios en tus campañas. Para realizar un reingreso aleatorio de audiencia con números de contenedor aleatorio, haz lo siguiente:

1. [Crea tu segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/).
2. Define los contenedores aleatorios. En tu campaña o Canvas, usa el filtro de contenedor aleatorio para dividir tu audiencia en diferentes grupos. Por ejemplo, puedes especificar exactamente dos contenedores aleatorios para dividir tu audiencia (50 % de usuarios por contenedor).
3. En la sección **Target Audiences** de tu campaña o Canvas, especifica la configuración de contenedores aleatorios. Esto permite que Braze asigne automáticamente a los usuarios a los contenedores apropiados según los porcentajes definidos.
4. Configura una lógica que permita a los usuarios reingresar al segmento. Por ejemplo, puedes permitir que los usuarios reingresen al segmento si no han interactuado con una aplicación durante 15 días.
5. Lanza tu campaña y monitorea el rendimiento de cada contenedor. Puedes analizar métricas como tasas de interacción y tasas de conversión para determinar qué tan efectivo es el reingreso aleatorio de audiencia en tu caso de uso.