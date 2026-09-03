---
nav_title: Conmutador de características
article_title: Conmutador de características
page_order: 8
page_type: reference
description: "Este artículo de referencia explica cómo se pueden usar los conmutadores de características en Canvas."
tool: Canvas
local_redirect:
  create-a-feature-flag: '/docs/user_guide/messaging/feature_flags/create_feature_flags'
---

# Conmutador de características {#feature-flag}

> Los conmutadores de características te permiten experimentar y confirmar tus hipótesis sobre nuevas características. Los especialistas en marketing pueden usar los conmutadores de características para segmentar tu audiencia en [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) y hacer seguimiento del impacto del despliegue de características en las conversiones. Además, los [recorridos de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) te permiten optimizar estas conversiones probando diferentes mensajes o recorridos entre sí y determinando cuál es más efectivo. Usa el recorrido ganador a medida que despliegas progresivamente tu característica a una audiencia más amplia.

¿Buscas más información sobre los conmutadores de características y cómo se pueden usar en Braze? Consulta nuestros artículos dedicados sobre [conmutadores de características]({{site.baseurl}}/developer_guide/feature_flags).

## Crear un conmutador de características {#creating-a-feature-flag}

![Un ejemplo de paso de conmutador de características para la característica de botón de chat en vivo.]({% image_buster /assets/img/feature_flags/feature_flag_canvas_step.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Para crear un componente de conmutador de características, primero añade un paso a tu Canvas. Arrastra y suelta el componente desde la barra lateral, o haz clic en el botón <i class="fas fa-plus-circle"></i> de signo más en la parte inferior de un paso y selecciona **Feature Flag**. A continuación, selecciona el conmutador de características del menú desplegable, que contiene todos los conmutadores de características que no están archivados.

## Cómo funciona este paso {#how-this-step-works}

Cuando un Canvas se detiene, se archiva o se elimina un paso de conmutador de características, los usuarios que pasaron por ese paso dejan de recibir el conmutador de características y sus propiedades de ese paso.

Para un conmutador de características que no tiene despliegue ni experimento de conmutador de características, después de detener un Canvas que contiene un paso de conmutador de características que hace referencia a ese conmutador:

- Ningún usuario tiene ese conmutador de características en la pestaña **Feature Flags Eligibility**.
- Ningún usuario coincide con el filtro de segmentación `Feature Flags` para ese conmutador de características.

Si el conmutador de características tiene un despliegue, un experimento de conmutador de características u otro Canvas activo que lo referencia, los usuarios aún pueden ser elegibles a través de esos canales.

Las propiedades en un paso en Canvas se pueden cambiar después del lanzamiento, e incluso después de que un usuario pase por el paso. Los usuarios siempre reciben una versión dinámica y en tiempo real del conmutador de características, en lugar de la versión anterior guardada previamente.

- **Dos Canvas hacen referencia al mismo conmutador de características y un usuario entra en ambos:** el usuario recibe el valor establecido en el Canvas en el que entró más recientemente, no en el anterior. Ese valor aparece en la pestaña **Feature Flags Eligibility**.
- **Un Canvas tiene dos pasos de conmutador de características que hacen referencia al mismo conmutador de características:** el usuario recibe el valor establecido en el segundo paso mientras se encuentra en ese recorrido, y ese valor aparece en la pestaña **Feature Flags Eligibility**.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

## Sobrescribir propiedades {#overwriting-properties}

Al crear un conmutador de características, especificas propiedades predeterminadas. Al configurar un paso de conmutador de características en Canvas, puedes mantener los valores predeterminados o sobrescribir los valores para los usuarios que entren en este paso.

![Un conmutador de características "Preference Center" con "String" como propiedad, "url" como clave de propiedad y un valor.]({% image_buster /assets/img/feature_flags/feature_flags_canvas_details.png %}){: style="max-width:90%"}

Ve a **Mensajería** > **Feature Flags** para editar, añadir o eliminar propiedades adicionales.

## Diferencias entre Canvas y despliegue {#canvas-and-rollout-differences}

Canvas y el despliegue de un conmutador de características (arrastrando el control deslizante) pueden funcionar de forma independiente entre sí. Una advertencia importante es que la entrada a un paso en Canvas sobrescribirá cualquier configuración de despliegue predeterminada. Esto significa que si un usuario no cumple los requisitos para un conmutador de características, un paso en Canvas puede habilitar la característica para ese usuario.

De manera similar, si un usuario cumple los requisitos para un despliegue de conmutador de características con ciertas propiedades, y también entra en el paso en Canvas, recibirá los valores sobrescritos de ese paso en Canvas.