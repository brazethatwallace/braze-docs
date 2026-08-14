---
nav_title: Ejemplos
article_title: Ejemplos para Decisioning Studio Go
page_order: 5
page_type: reference
description: "Revisa los tipos comunes de programas de correo electrónico para determinar si Decisioning Studio Go es una buena opción para tu escenario."
---

# Ejemplos para Decisioning Studio Go {#examples-for-decisioning-studio-go}

> Decisioning Studio Go funciona mejor para programas de correo electrónico recurrentes en los que el agente tiene tiempo para aprender de la participación y en los que tu contenido incluye suficientes opciones de variantes para una personalización significativa. Esta página agrupa los ejemplos comunes de correo electrónico por nivel de ajuste, con ejemplos y orientación para cada uno.

Para un resumen de cómo funciona Decisioning Studio Go, consulta [BrazeAI Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go).

Cada ejemplo en esta guía está etiquetado con uno de los siguientes niveles de ajuste:

| Nivel de ajuste | Descripción |
|---|---|
| **Mejor ajuste** | El agente tiene suficiente tiempo para aprender, tu audiencia es lo bastante estable como para mostrar mejoras, y la personalización puede afectar significativamente la participación. Empieza aquí. |
| **Compatible** | El ejemplo puede funcionar bien, pero el éxito depende del momento, el tamaño de la audiencia o la secuenciación. Revisa las consideraciones antes de comprometerte. |
| **No recomendado** | El ejemplo entra en conflicto con la forma en que el agente aprende. Elige un tipo de programa diferente, o habla con tu administrador de éxito de cliente o consultor de soluciones sobre una configuración diferente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Niveles de ajuste" }

{% alert note %}
En todos los niveles de ajuste, el agente aprende mejor cuando tu audiencia genera suficiente señal de participación para que el algoritmo detecte patrones. Como regla general, apunta a audiencias de decenas de miles de usuarios o más, con un volumen de envío semanal constante. El agente puede funcionar con audiencias más pequeñas, pero espera un período de aprendizaje más largo y mejoras menos fiables. Tu administrador de éxito de cliente o consultor de soluciones puede ayudarte a confirmar si una audiencia determinada tiene el tamaño adecuado.
{% endalert %}

## Mejor ajuste {#best-fit}

### Campaigns con calendario permanente {#always-on-calendared-campaigns}

| Tema | Detalles |
|---|---|
| Cómo se ve | Un calendario de marketing que se ejecuta durante varios meses o más, con contenido que se intercambia a lo largo del tiempo; por ejemplo, un calendario de miembros de recompensas, un cronograma de lanzamiento de contenido, o un calendario de estilo de vida o inspiración. |
| Por qué encaja | Los programas de larga duración le dan al agente tiempo para aprender qué funciona para diferentes usuarios. La audiencia es estable, el contenido se actualiza regularmente y los clics suelen ser un indicador significativo de participación. |
| Qué necesitas | Múltiples creatividades base o conjuntos de variantes que estés dispuesto a rotar. El agente selecciona qué versión funciona para cada usuario, pero necesita suficiente variedad en las opciones que proporcionas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaigns con calendario permanente" }

### Programas permanentes {#evergreen-programs}

| Tema | Detalles |
|---|---|
| Cómo se ve | Campaigns continuas que no están vinculadas a fechas o eventos específicos: reactivaciones, programas de reactivación, recordatorios de cuentas inactivas o celebraciones de hitos. |
| Por qué encaja | Al igual que las Campaigns con calendario, la audiencia es dinámica pero el programa se ejecuta indefinidamente. El agente tiene tiempo para aprender, el contenido tiene flexibilidad y los clics son un indicador adelantado contra el que el agente puede optimizar. |
| Qué necesitas | Opciones de variantes para la línea del asunto y el CTA que enmarquen el mensaje para diferentes motivaciones. Las variantes de imagen ayudan si las tienes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Programas permanentes" }

## Ejemplos compatibles {#supported-use-cases}

### Promociones de múltiples correos electrónicos {#multi-email-promotions}

| Tema | Detalles |
|---|---|
| Cómo se ve | Un conjunto de correos electrónicos enviados durante varias semanas bajo el mismo tema promocional; por ejemplo, una serie de vuelta al cole o una promoción de categoría de varias semanas. |
| Por qué funciona | Si la promoción dura lo suficiente —al menos varias semanas— el agente tiene margen para aprender dentro de la promoción. El click-through suele ser un indicador adelantado sólido de la participación promocional. |
| Consideraciones | Para promociones más cortas, es posible que el agente no tenga suficientes días de datos para aprender antes de que el programa termine. Como pauta general, el agente necesita al menos 10 días de Campaign para desarrollar recomendaciones sólidas. Si tu promoción es más corta que eso, considera si un programa permanente podría llevar el aprendizaje en su lugar, y luego aplica lo que aprendas a la siguiente promoción. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Promociones de múltiples correos electrónicos" }

### Recorridos basados en acciones o eventos {#action-or-event-driven-journeys}

| Tema | Detalles |
|---|---|
| Cómo se ve | Un correo electrónico individual o una secuencia desencadenada por una acción del cliente: abandono del carrito de compras, abandono de navegación o seguimiento posterior a la compra. |
| Por qué funciona | Los desencadenantes crean un punto de entrada limpio. Si el recorrido es recurrente y el volumen de audiencia es constante, el agente puede aprender qué contenido funciona para qué usuarios. |
| Consideraciones | El momento importa. Si el correo electrónico debe enviarse en cuestión de minutos después del evento desencadenante, trabaja con tu administrador de éxito de cliente o consultor de soluciones para confirmar que el calendario de envío del agente es compatible. Si los usuarios deben recibir los correos electrónicos en un orden específico (correo electrónico A antes del correo electrónico B), necesitas orquestar los movimientos de audiencia tú mismo; el agente no secuencia envíos para un solo usuario a lo largo de un recorrido de múltiples correos electrónicos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Recorridos basados en acciones o eventos" }

## No recomendado {#not-recommended}

### Secuencias de goteo {#drip-sequences}

| Tema | Detalles |
|---|---|
| Cómo se ve | Una secuencia de múltiples correos electrónicos —por ejemplo, un tutorial de incorporación— en la que los usuarios deben recibir el correo electrónico A, luego el B y luego el C en orden. |
| Por qué no encaja | El agente selecciona qué enviar a cada usuario en función de lo que probablemente genere un clic para ese usuario. No modela requisitos de secuencia. Si necesitas imponer un orden específico, debes orquestar la audiencia tú mismo (moviendo usuarios de segmento a segmento después de cada correo electrónico), lo que reduce la mayor parte del beneficio de usar el agente. El agente tampoco puede confirmar de forma independiente que el correo electrónico A tuvo éxito antes de enviar el correo electrónico B. |
| Qué hacer en su lugar | Usa [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) para orquestar la secuencia de goteo. Si quieres optimización con IA dentro de una secuencia de goteo, habla con tu administrador de éxito de cliente o consultor de soluciones sobre si [Decisioning Studio Pro]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/get_started) es una mejor opción. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Secuencias de goteo" }

### Envíos masivos de correo electrónico únicos {#one-time-email-blasts}

| Tema | Detalles |
|---|---|
| Cómo se ve | Un solo correo electrónico enviado en un único envío masivo: un anuncio de Black Friday, el lanzamiento de un nuevo producto o una comunicación corporativa puntual. |
| Por qué no encaja | El agente necesita tiempo para aprender. Un solo envío no le da oportunidad de mejorar las decisiones antes de que la Campaign termine. Para cuando tiene suficiente señal de participación para tomar mejores decisiones, el programa ya terminó. |
| Qué hacer en su lugar | Si tienes un programa permanente con contenido similar —por ejemplo, un programa de anuncios de productos durante todo el año— usa Decisioning Studio Go allí y aplica lo que aprendas a los envíos únicos. Para un envío masivo verdaderamente único, las [pruebas A/B]({{site.baseurl}}/user_guide/messaging/ab_testing) o la [selección inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection) son mejores opciones. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Envíos masivos de correo electrónico únicos" }

## De un vistazo {#at-a-glance}

| Escenario | Ajuste | Consideración clave |
|---|---|---|
| Campaigns con calendario permanente | Mejor ajuste | Proporciona múltiples creatividades base o conjuntos de variantes para actualizar a lo largo del tiempo. |
| Programas permanentes (reactivaciones, reactivación) | Mejor ajuste | Proporciona opciones de variantes que enmarquen el mismo mensaje para diferentes motivaciones. |
| Promociones de múltiples correos electrónicos | Compatible | Apunta a al menos 10 días de Campaign de margen; las promociones más cortas limitan el aprendizaje. |
| Recorridos basados en acciones o eventos | Compatible | Confirma los requisitos de momento de envío; tú eres responsable de imponer la secuencia. |
| Secuencias de goteo (tutoriales de incorporación) | No recomendado | Usa Canvas para la secuenciación; revisa Decisioning Studio Pro para optimización dentro de la secuencia de goteo. |
| Envíos masivos de correo electrónico únicos | No recomendado | Usa pruebas A/B o selección inteligente en su lugar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tabla resumen de ejemplos" }

## Próximos pasos {#next-steps}

Contacta a tu administrador de éxito de cliente o consultor de soluciones de Braze si no estás seguro de si tu programa es una buena opción. Las señales fuertes incluyen:

- La audiencia recibe correo electrónico regularmente —al menos semanalmente— durante un período de un mes o más.
- La audiencia es lo suficientemente grande como para generar una señal de participación constante (decenas de miles de usuarios es un objetivo inicial útil).
- Tienes al menos dos o tres opciones de variantes significativas para ofrecer (líneas del asunto, CTAs o imágenes que enmarquen el mensaje de forma diferente).
- Los clics son un indicador adelantado de valor de negocio para este programa, no solo una métrica de vanidad.
- El segmento no está siendo utilizado activamente por otro Canvas o Campaign que compita por la participación de los mismos usuarios.