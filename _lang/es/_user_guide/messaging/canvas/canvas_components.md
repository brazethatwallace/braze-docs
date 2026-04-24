---
nav_title: Componentes de Canvas
article_title: Componentes de Canvas
page_order: 3
alias: "/user_guide/messaging/canvas/canvas_components/about/"
layout: dev_guide
guide_top_header: "Componentes de Canvas"
guide_top_text: "Mejora tu recorrido de Canvas con los componentes de Canvas. Los componentes de Canvas se pueden utilizar para simplificar el proceso de determinar la efectividad de tu Canvas, sustituyendo pasos completos excesivos por uno solo. Los componentes en Canvas se refieren al recorrido personalizado del usuario en las ramas de tu Canvas."

page_type: landing
description: "Esta página de inicio alberga artículos sobre componentes de Canvas que te ayudarán a crear Canvas más avanzados. Algunos de estos componentes incluyen el paso de mensaje, el paso de retraso, el paso para la división de decisiones y más."
tool: Canvas

guide_featured_title: "Artículos de la sección"
guide_featured_list:
  - name: Paso de Rutas de acción
    link: /docs/user_guide/messaging/canvas/canvas_components/action_paths
    image: /assets/img/braze_icons/zap.svg
  - name: Paso de agente
    link: /docs/user_guide/messaging/canvas/canvas_components/agent_step
    image: /assets/img/braze_icons/briefcase-01.svg
  - name: Paso de Rutas de audiencia
    link: /docs/user_guide/messaging/canvas/canvas_components/audience_paths
    image: /assets/img/braze_icons/users-01.svg 
  - name: Paso de sincronización de audiencia
    link: /docs/partners/canvas_audience_sync/
    image: /assets/img/braze_icons/refresh-ccw-02.svg
  - name: Paso del Optimizador de contenidos
    link: /docs/user_guide/messaging/canvas/canvas_components/content_optimizer_step
    image: /assets/img/braze_icons/target-04.svg
  - name: Paso de contexto
    link: /docs/user_guide/messaging/canvas/canvas_components/context
    image: /assets/img/braze_icons/file-search-02.svg
  - name: Paso de División de decisiones
    link: /docs/user_guide/messaging/canvas/canvas_components/decision_split
    image: /assets/img/braze_icons/dataflow-04.svg
  - name: Paso de retraso
    link: /docs/user_guide/messaging/canvas/canvas_components/delay_step
    image: /assets/img/braze_icons/clock-stopwatch.svg
  - name: Paso de Recorridos de experimentos
    link: /docs/user_guide/messaging/canvas/canvas_components/experiment_step
    image: /assets/img/braze_icons/columns-01.svg
  - name: Conmutadores de características
    link: /docs/user_guide/messaging/canvas/canvas_components/feature_flags
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: Paso de mensaje
    link: /docs/user_guide/messaging/canvas/canvas_components/message_step
    image: /assets/img/braze_icons/message-square-02.svg
  - name: Paso de enviar al destino
    link: /docs/user_guide/messaging/canvas/canvas_components/send_to_destination
    image: /assets/img/braze_icons/dataflow-02.svg
  - name: Paso de Actualización de usuario
    link: /docs/user_guide/messaging/canvas/canvas_components/user_update
    image: /assets/img/braze_icons/user-check-01.svg
---

## Acerca de los componentes de Canvas

Con los componentes de Canvas, puedes desbloquear nuevos recorridos de usuario para mejorar tu proceso y aumentar la efectividad del alcance de tu audiencia.

### Personalizar los recorridos de usuario

![Ejemplo de un recorrido de usuario en Canvas con un paso de División de decisiones seguido de pasos de retraso y pasos de mensaje.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %}){: style="float:right;max-width:55%;margin-left:15px;"}

Usa las [Rutas de acción]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) para dividir el recorrido de tus usuarios en función de acciones y eventos de interacción, como realizar una compra. Si quieres filtrar y segmentar tus audiencias, las [Rutas de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) te ayudan a simplificar la segmentación de usuarios enviándolos por diferentes rutas de Canvas según criterios de audiencia.

Los componentes de [División de decisiones]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) utilizan una lógica simple de "sí o no" para crear dos rutas mutuamente excluyentes en los recorridos de tus usuarios, basadas en una acción o un atributo de usuario. Esto puede ayudar a identificar y segmentar tus grupos de usuarios.

Los componentes de [retraso]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) te permiten retrasar un solo paso en tu Canvas. Este paso de retraso independiente en tu Canvas es ideal para comunicar mensajes a tus usuarios en un momento específico. Además, los componentes de retraso también pueden aumentar el alcance de tu audiencia al permitir más tiempo para que tu audiencia cumpla con los criterios del componente.

### Pruebas

Al crear los recorridos de tus usuarios, es posible que también quieras probar cuál es la ruta de Canvas más efectiva. Con los [Recorridos de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step), puedes probar múltiples rutas de Canvas en cualquier paso. También puedes usar las conexiones entre pasos como una vista previa de alto nivel. Las conexiones de color naranja indican que el paso anterior hará avanzar inmediatamente a los usuarios al siguiente paso.

### Integración

¿Quieres sincronizar los datos de usuario propios de tu marca? Aprovecha las opciones de sincronización de audiencia disponibles para [Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) y [Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/).