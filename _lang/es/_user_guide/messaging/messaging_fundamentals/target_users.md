---
nav_title: Segmentar usuarios
article_title: Segmentar usuarios
page_order: 12
page_type: reference
description: "Este artículo de referencia cubre cómo segmentar tu audiencia en los editores de Campaign y Canvas."
tool:
    - Campaigns
    - Canvas
---

# Segmentar usuarios {#target-users}

> Determinar cómo segmentar a tus usuarios es uno de los pasos más cruciales al crear una Campaign o un Canvas. Al comprender cómo segmentar tu audiencia en función de sus comportamientos, preferencias y datos demográficos, puedes personalizar y adaptar tus mensajes.

## Crear una audiencia objetivo {#creating-a-target-audience}

### Paso 1: Elige usuarios {#step-1-choose-users}

En **Opciones de segmentación**, puedes usar las siguientes opciones para elegir a qué usuarios deseas dirigir tu Campaign o Canvas. Solo los usuarios que coincidan con los criterios definidos recibirán el mensaje. Ten en cuenta que la pertenencia exacta al segmento siempre se calcula justo antes de que se envíe el mensaje.

{% tabs local %}
{% tab segmento único %}
Para dirigirte a miembros de un segmento creado previamente, selecciona un segmento del menú desplegable en **Selecciona a usuarios por segmento**.
{% endtab %}

{% tab múltiples segmentos %}
Para dirigirte a usuarios que pertenecen a múltiples segmentos creados previamente, añade múltiples segmentos del menú desplegable en **Selecciona a usuarios por segmento**. La audiencia objetivo resultante serán los usuarios que estén tanto en el primer segmento como en el segundo y en el tercero, etc.
{% endtab %}

{% tab múltiples filtros %}
Para dirigirte a usuarios sin añadir un segmento, puedes usar una serie de filtros. Esta es una audiencia improvisada durante la creación del mensaje y te permite omitir la creación de segmentos al enviar a audiencias puntuales.

![Filtros adicionales para un mensaje que se dirige a usuarios que abrieron la aplicación por última vez en el día, nunca han recibido una Campaign o un paso en Canvas, y que realizaron una compra hace menos de 30 días.]({% image_buster /assets/img_archive/additional_filters.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab segmentos y filtros %}
También puedes dirigirte a usuarios de uno o más segmentos creados previamente que además cumplan con filtros adicionales. Después de seleccionar tus segmentos, puedes refinar aún más tu audiencia en la sección **Filtros adicionales**. Esto se demuestra en la siguiente captura de pantalla, que se dirige a usuarios que están en el segmento "Usuarios activos diarios", el segmento "Nunca abrió correo electrónico" y que realizaron una compra hace más de 30 días.

![Opciones de segmentación para un mensaje que incluye dos segmentos y tiene un filtro adicional para una última compra realizada hace menos de 30 días.]({% image_buster /assets/img_archive/target_segmenter.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab Aplicaciones específicas %}

Puedes entregar un mensaje de Campaign o un paso en Canvas a aplicaciones específicas, como enviar un mensaje dentro de la aplicación o una notificación push solo a aplicaciones Android o iOS.

Sin embargo, recuerda que es posible que un usuario utilice múltiples aplicaciones. El filtro "Tiene la aplicación" identifica a todos los usuarios que tienen la aplicación seleccionada, pero no controla qué aplicaciones reciben los mensajes. Por ejemplo, si aplicas un filtro de segmento donde "Tiene la aplicación" está configurado como Android, cualquier usuario que también tenga la aplicación iOS recibirá el mensaje en su aplicación iOS.

![Un filtro para usuarios que tienen la aplicación "Hello, World (Android)".]({% image_buster /assets/img_archive/has_app_hello_world.png %}){: style="max-width:60%;"}

Supongamos que quieres enviar un mensaje dentro de la aplicación solo a aplicaciones Android.

1. Crea un segmento y configura **Aplicaciones y sitios web objetivo** como **Usuarios de aplicaciones específicas**, luego selecciona tu aplicación Android.

![Un segmento que se dirige a usuarios de una aplicación específica, "Test_Android".]({% image_buster /assets/img_archive/app_test_android.png %}){: style="max-width:60%;"}

{: start="2"}
2. En el paso **Públicos objetivo**, confirma que tu segmento esté añadido en la sección **Selecciona a usuarios por segmento**.

![El paso "Públicos objetivo" con un segmento de ejemplo seleccionado.]({% image_buster /assets/img_archive/target_users_by_segment_example.png %})

{% alert note %}
Esto no funcionará si añades tu segmento en la sección **Filtros adicionales** a través de un filtro de pertenencia a segmento. Debes hacer referencia directamente a tu segmento en **Selecciona a usuarios por segmento** para entregar tu mensaje solo a esa aplicación.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert tip %}
Para Campaigns de correo electrónico, puedes dirigirte a grupos semilla en la sección **Grupos semilla**. Ten en cuenta que los grupos semilla no están disponibles para Campaigns de API, aunque puedes incluir grupos semilla a través de una entrada activada por API en una Campaign. Para más información, consulta [Grupos semilla]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups).
{% endalert %}

### Paso 2: Prueba tu audiencia {#step-2-test-your-audience}

Después de añadir segmentos y filtros a tu audiencia, puedes probar si tu audiencia está configurada como se espera [buscando un usuario]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) para confirmar si coincide con los criterios de la audiencia.

![La sección "Búsqueda de usuario" con un botón "Buscar usuario".]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

#### Resumen de audiencia {#audience-summary}

El **Resumen de audiencia** mostrará una vista general de quién está en tu audiencia objetivo. Aquí, puedes limitar aún más tu audiencia estableciendo un límite máximo de usuarios o [limitando la velocidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) de entrega.

![La sección "Resumen de audiencia" con opciones para establecer un límite máximo de usuarios o limitar la velocidad de entrega.]({% image_buster /assets/img_archive/audience_summary.png %})

#### Pruebas A/B {#ab-testing}

En la sección **Pruebas A/B**, puedes configurar una prueba para comparar las respuestas de los usuarios a múltiples versiones de la misma campaña de marketing. Estas versiones comparten objetivos de marketing similares pero difieren en la redacción y el estilo. El objetivo es identificar la versión de la campaña que mejor cumple tus objetivos de marketing.

Para más información y mejores prácticas, consulta [Pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

#### Estadísticas de audiencia {#audience-statistics}

Braze proporciona estadísticas detalladas de la audiencia de los canales objetivo en el pie de página. Cuanto mayor sea tu base de usuarios, más probable es que la cantidad de **Usuarios alcanzables** sea una estimación aproximada. El número de usuarios alcanzables puede disminuir si usas un [grupo de control global]({{site.baseurl}}/user_guide/audience/global_control_group) o configuras la elegibilidad de mensajes.

- Para determinar un número preciso de tus usuarios alcanzables, selecciona [Calcular estadísticas exactas]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#calculating-exact-statistics), ya que esto buscará a cada usuario en tu base de usuarios.
- Para ver qué porcentaje de tu base de usuarios está siendo segmentado o el LTV (LTV) para este segmento, selecciona **Mostrar estadísticas adicionales**.

##### Por qué el recuento de la audiencia objetivo podría diferir del recuento de usuarios alcanzables {#why-the-target-audience-count-could-differ-from-the-reachable-users-count}

{% multi_lang_include audience/segments.md section='Differing audience size' %}

![La sección "Población total" con recuentos estimados de usuarios alcanzables en cada canal objetivo.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

{% alert note %}
Calcular estadísticas exactas puede tardar unos minutos en ejecutarse. Esta función solo calcula las estadísticas exactas a nivel de segmento, no a nivel de filtro o grupo de filtros.<br><br>
Para segmentos grandes, es normal ver ligeras variaciones incluso al calcular estadísticas exactas. Se espera que la precisión de esta función sea del 99,999 % o superior.
{% endalert %}

## Cómo funcionan juntos la audiencia objetivo y los criterios de entrada {#how-target-audience-and-entry-criteria-work-together}

Cuando creas una Campaign o un Canvas en Braze, la segmentación ocurre en dos partes:

1. **Audiencia objetivo:** Quién califica
2. **Criterios de entrada:** Qué desencadena la entrega

El orden importa: Braze verifica si alguien está en la audiencia objetivo antes de que se evalúen los criterios de entrada. Si un usuario no califica para la audiencia en ese momento, no entrará en la Campaign o el Canvas, incluso si más tarde desencadena el evento de entrada. Piensa en la audiencia objetivo como una sala de espera: solo los usuarios que ya están dentro cuando ocurre el desencadenante pueden avanzar.

### Ejemplo 1 {#example-1}

Quieres enviar un mensaje push durante la primera sesión de un usuario.

Configuras:

- **Audiencia objetivo:** Usuarios con recuento de sesiones = 0
- **Evento de entrada:** Inicio de sesión

Cuando el usuario abre tu aplicación, Braze ve que su recuento de sesiones ahora es 1, y ya no califica para la audiencia. El evento de entrada ocurre después de que son elegibles, por lo que el mensaje no se enviará.

Para que esto funcione, el usuario necesita calificar para la audiencia antes de que comience la sesión (invierte la audiencia objetivo y el desencadenante de entrada).

### Ejemplo 2 {#example-2}

Quieres enviar un correo electrónico a usuarios que han gastado más de $10 en los últimos 7 días.

Configuras:

- **Audiencia objetivo:** Usuarios que gastaron más de $10 en los últimos 7 días
- **Evento de entrada:** Cualquier compra

Ahora imagina que un usuario gasta $12 hoy. Eso no desencadena el mensaje, solo lo hace elegible para entrar en la audiencia. No recibirá el correo electrónico a menos que realice otra compra más adelante.

Un mejor enfoque sería usar una audiencia más amplia y mover el filtro a los criterios de entrada:

- **Audiencia:** Todos los usuarios (o tu audiencia base)
- **Evento de entrada:** Realizar una compra
- **Filtro de entrada:** Gasto total en los últimos 7 días > $10

De esta manera, una compra que califique cumple tanto el filtro como desencadena el mensaje, sin necesidad de una segunda acción.

## Mejores prácticas {#best-practices}

- Asegúrate de que el segmento de audiencia incluya usuarios antes de que ocurran los criterios de entrada.
- Evita usar filtros de audiencia que solo apliquen después de tu evento. Si un filtro depende de algo que sucede en el momento del desencadenante (como "recuento de sesiones = 0"), el usuario puede que ya no califique para cuando Braze lo verifique.
- Usa la lógica basada en tiempo de manera reflexiva. Por ejemplo, si quieres dirigirte a usuarios nuevos:
    - Configura tu audiencia objetivo como "usó la aplicación por primera vez en los últimos 7 días".
    - Configura tu evento de entrada como "inicio de sesión".
    - De esta manera, solo los usuarios que aún estén dentro de su primera semana calificarán y entrarán cuando inicien una sesión.