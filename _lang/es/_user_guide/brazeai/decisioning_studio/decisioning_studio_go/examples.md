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
| **No recomendado** | El ejemplo entra en conflicto con la forma en que el agente aprende. Elige un tipo de programa diferente, o habla con tu CSM o consultor de soluciones sobre una configuración diferente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Niveles de ajuste" }

{% alert note %}
En todos los niveles de ajuste, el agente aprende mejor cuando tu audiencia genera suficiente señal de participación para que el algoritmo detecte patrones. Como regla general, apunta a audiencias de decenas de miles de usuarios o más, con un volumen de envío semanal constante. El agente puede funcionar con audiencias más pequeñas, pero espera un período de aprendizaje más largo y mejoras menos fiables. Tu CSM o consultor de soluciones puede ayudarte a confirmar si una audiencia determinada tiene el tamaño adecuado.
{% endalert %}

## Mejor ajuste {#best-fit}

### Campaigns con calendario continuo {#always-on-calendared-campaigns}

| Tema | Detalles |
|---|---|
| Cómo se ve | Un calendario de marketing que se ejecuta durante varios meses o más, con contenido que se intercambia a lo largo del tiempo; por ejemplo, un calendario para miembros de recompensas, un cronograma de lanzamiento de contenido, o un calendario de estilo de vida o inspiración. |
| Por qué encaja | Los programas de larga duración le dan al agente tiempo para aprender qué funciona para diferentes usuarios. La audiencia es estable, el contenido se actualiza regularmente y los clics suelen ser un indicador significativo de participación. |
| Qué necesitas aportar | Múltiples creativos base o conjuntos de variantes que estés dispuesto a rotar. El agente selecciona qué versión funciona para cada usuario, pero necesita suficiente variedad en las opciones que proporcionas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaigns con calendario continuo" }

### Programas permanentes {#evergreen-programs}

| Tema | Detalles |
|---|---|
| Cómo se ve | Campaigns en curso que no están vinculadas a fechas o eventos específicos: recuperación de usuarios, programas de reactivación, recordatorios para cuentas inactivas o celebraciones de hitos. |
| Por qué encaja | Al igual que las Campaigns con calendario, la audiencia es dinámica pero el programa se ejecuta de forma indefinida. El agente tiene tiempo para aprender, el contenido es flexible y los clics son un indicador adelantado contra el cual el agente puede optimizar. |
| Qué necesitas aportar | Opciones de variantes para la línea del asunto y el CTA que enmarquen el mensaje según distintas motivaciones. Las variantes de imagen ayudan si cuentas con ellas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Programas permanentes" }

## Ejemplos admitidos {#supported-use-cases}

### Promociones con múltiples correos electrónicos {#multi-email-promotions}

| Tema | Detalles |
|---|---|
| Cómo se ve | Un conjunto de correos electrónicos enviados a lo largo de varias semanas bajo la misma temática promocional; por ejemplo, una serie de vuelta al cole o una promoción de categoría de varias semanas. |
| Por qué funciona | Si la promoción dura lo suficiente —al menos varias semanas—, el agente tiene margen para aprender dentro de la promoción. El click-through suele ser un indicador adelantado sólido de la participación promocional. |
| Consideraciones | En promociones más cortas, es posible que el agente no cuente con suficientes días de datos para aprender antes de que termine el programa. Como pauta general, el agente necesita al menos 10 días de Campaign para desarrollar recomendaciones sólidas. Si tu promoción es más corta, considera si un programa permanente podría asumir el aprendizaje; luego aplica lo aprendido a la próxima promoción. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Promociones con múltiples correos electrónicos" }

### Recorridos basados en acciones o eventos {#action-or-event-driven-journeys}

| Tema | Detalles |
|---|---|
| Cómo se ve | Un correo electrónico individual o una secuencia desencadenada por una acción del cliente: abandono del carrito de compras, abandono de navegación o seguimiento posterior a la compra. |
| Por qué funciona | Los desencadenadores crean un punto de entrada limpio. Si el recorrido es recurrente y el volumen de audiencia es constante, el agente puede aprender qué contenido funciona para cada usuario. |
| Consideraciones | El momento importa. Si el correo electrónico debe enviarse a los pocos minutos del evento desencadenante, consulta con tu CSM o consultor de soluciones para confirmar que el calendario de envío del agente es compatible. Si los usuarios deben recibir los correos en un orden específico (correo A antes del correo B), necesitas orquestar los movimientos de audiencia tú mismo: el agente no secuencia envíos para un mismo usuario a lo largo de un recorrido con múltiples correos electrónicos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Recorridos basados en acciones o eventos" }

## No recomendado {#not-recommended}

### Secuencias por goteo {#drip-sequences}

| Tema | Detalles |
|---|---|
| Cómo se ve | Una secuencia de varios correos electrónicos (por ejemplo, un tutorial de incorporación) en la que los usuarios deben recibir el correo electrónico A, luego el B y luego el C en orden. |
| Por qué no encaja | El agente selecciona qué enviar a cada usuario en función de lo que probablemente genere un clic para ese usuario. No modela requisitos de secuencia. Si necesitas aplicar un orden específico, debes orquestar la audiencia tú mismo (moviendo a los usuarios de Segment a Segment después de cada correo electrónico), lo que reduce la mayor parte del beneficio de usar el agente. El agente tampoco puede confirmar de forma independiente que el correo electrónico A tuvo éxito antes de enviar el correo electrónico B. |
| Qué hacer en su lugar | Usa [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) para orquestar la secuencia por goteo. Si quieres optimización con IA dentro de una secuencia por goteo, habla con tu CSM o consultor de soluciones sobre si [Decisioning Studio Pro]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/get_started) es una mejor opción. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Secuencias por goteo" }

### Envíos masivos de correo electrónico únicos {#one-time-email-blasts}

| Tema | Detalles |
|---|---|
| Cómo se ve | Un solo correo electrónico enviado en un envío masivo: un anuncio de Black Friday, el lanzamiento de un nuevo producto o una comunicación corporativa puntual. |
| Por qué no encaja | El agente necesita tiempo para aprender. Un solo envío no le da oportunidad de mejorar las decisiones antes de que termine la Campaign. Para cuando tiene suficiente señal de participación para tomar mejores decisiones, el programa ya terminó. |
| Qué hacer en su lugar | Si tienes un programa permanente con contenido similar (por ejemplo, un programa de anuncios de productos durante todo el año), usa Decisioning Studio Go ahí y aplica lo que aprendas a los envíos únicos. Para un envío único, usa [Optimizar con BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection) para pruebas A/B. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Envíos masivos de correo electrónico únicos" }

## De un vistazo {#at-a-glance}

| Escenario | Idoneidad | Consideración clave |
|---|---|---|
| Campaigns con calendario permanente | Más adecuado | Proporciona múltiples creatividades base o conjuntos de variantes para renovar con el tiempo. |
| Programas permanentes (recuperación, reactivación) | Más adecuado | Proporciona opciones de variantes que enmarquen el mismo mensaje para diferentes motivaciones. |
| Promociones con múltiples correos electrónicos | Compatible | Apunta a un mínimo de 10 días de Campaign de margen; las promociones más cortas limitan el aprendizaje. |
| Recorridos activados por acciones o eventos | Compatible | Confirma los requisitos de temporización de envío; tú eres responsable de hacer cumplir la secuencia. |
| Secuencias de goteo (tutoriales de incorporación) | No recomendado | Usa Canvas para la secuenciación; revisa Decisioning Studio Pro para la optimización dentro del goteo. |
| Envíos masivos de correo electrónico puntuales | No recomendado | Usa Optimize con BrazeAI<sup>TM</sup> para pruebas A/B en su lugar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="tabla resumen de ejemplos" }

## Próximos pasos {#next-steps}

Contacta a tu CSM o consultor de soluciones de Braze si no estás seguro de si tu programa es adecuado. Las señales fuertes incluyen:

- La audiencia recibe correo electrónico de forma regular —al menos semanalmente— durante un periodo de un mes o más.
- La audiencia es lo suficientemente grande como para generar una señal de participación consistente (decenas de miles de usuarios es un objetivo inicial útil).
- Tienes al menos dos o tres opciones de variantes significativas que ofrecer (líneas del asunto, CTAs o imágenes que presenten el mensaje de forma diferente).
- Los clics son un indicador principal de valor de negocio para este programa, no solo una métrica de vanidad.
- El Segment no está siendo utilizado activamente por otro Canvas o Campaign que competiría por la participación de los mismos usuarios.