---
nav_title: Analizar
article_title: Operator Analyze
page_order: 100
description: "Haz preguntas en lenguaje natural sobre la participación de tus canales, los ingresos atribuidos y cómo te comparas con los puntos de referencia del sector. Obtienes gráficos, comparaciones y análisis accionables en segundos."
page_type: reference
hidden: true
---

# Operator Analyze {#operator-analyze}

> Operator Analyze responde preguntas de rendimiento en lenguaje natural dentro de BrazeAI Operator<sup>TM</sup>. Las respuestas incluyen gráficos, comparaciones e información breve. No necesitas crear un panel ni generar un informe completo primero.

{% alert important %}
Operator Analyze se encuentra actualmente en fase beta. Las capacidades y los análisis compatibles están en evolución. Para solicitar acceso para tu cuenta, ponte en contacto con tu administrador de éxito de cliente.
{% endalert %}

## ¿Por qué usar Operator Analyze? {#why-use-operator-analyze}

La mayoría de las preguntas sobre rendimiento aún requieren cambiar de herramienta, crear vistas o esperar a que alguien más lo haga. Algunos ejemplos incluyen "¿Cómo fue la semana pasada?", "¿Estamos alineados con el punto de referencia?" y "¿Qué Campaign está generando los mejores resultados?"

Operator Analyze cubre métricas de participación, *ingresos atribuidos* y puntos de referencia del sector. Son los mismos datos que de otro modo tendrías que extraer en un informe o panel. Pregunta con tus propias palabras desde el panel de Operator. Obtienes un gráfico, una comparación clasificada o una tabla, además de uno a cinco análisis accionables.

## Acceder a Operator Analyze {#access-operator-analyze}

Operator Analyze se ejecuta en el panel de conversación de Operator.

1. Selecciona **BrazeAI Operator<sup>TM</sup>** junto a tu perfil de usuario desde cualquier página del panel de Braze.
2. Pregunta sobre la participación de canales o comparaciones con puntos de referencia (consulta [Preguntas de ejemplo](#example-questions)).
3. Operator devuelve la respuesta y, cuando es útil, un gráfico o tabla y una breve lista de información.

Para más información sobre el panel de chat de Operator, consulta [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator).

## Preguntas de ejemplo {#example-questions}

Describe lo que quieres saber. No se requiere una redacción fija. Selecciona una pestaña para ver ejemplos de indicaciones.

{% tabs %}
{% tab Comparaciones con puntos de referencia %}

* "¿Cómo se compara nuestra *tasa de apertura* de correo electrónico con los puntos de referencia del sector en los últimos 30 días?"
* "¿Estamos por encima o por debajo del punto de referencia para la *tasa de click-through* de SMS este trimestre?"
* "¿En qué áreas estamos por debajo del sector en nuestra combinación de canales?"

{% endtab %}
{% tab Resúmenes de canales %}

* "¿Qué canales están teniendo mejor rendimiento para nosotros en el año fiscal 26 hasta la fecha?"
* "Desglosa la participación por canal en los últimos 90 días."
* "¿Cuántos *ingresos atribuidos* generó cada canal de marketing el trimestre pasado?"

{% endtab %}
{% tab Detalles de Campaign y Canvas %}

* "¿Cuáles son nuestras 10 mejores Campaigns de correo electrónico por *tasa de click-through* este trimestre fiscal?"
* "¿Qué Canvas generaron más *clics* el mes pasado?"
* "¿Qué Campaigns generaron más *ingresos atribuidos* en el Q1 del año fiscal 26?"
* "Muestra nuestras Campaigns de push con peor rendimiento en los últimos 30 días."

{% endtab %}
{% tab Análisis de tendencias %}

* "¿Cuál es la tendencia mes a mes en la participación de push para el año fiscal 26?"
* "¿Cómo ha cambiado la *tasa de click-through* de correo electrónico trimestre a trimestre durante el último año?"
* "¿Cómo han evolucionado nuestros *ingresos atribuidos* en los últimos 12 meses?"
* "Muéstrame nuestra tendencia de participación semanal para mensajes dentro de la aplicación en los últimos 90 días."

{% endtab %}
{% tab Ingresos y conversiones %}

Pregunta sobre *ingresos atribuidos* y *conversiones* agregados a nivel de Campaign, Canvas, canal o programa.

* "Compara los *ingresos atribuidos* y las *conversiones* del trimestre más reciente con el trimestre anterior."
* "¿Qué Campaigns generaron más *ingresos atribuidos* en los últimos 90 días?"
* "Desglosa los *ingresos atribuidos* por canal para el año fiscal 26 hasta la fecha."

{% endtab %}
{% tab Revisiones integrales %}

* "Dame una revisión completa de nuestro programa de participación con recomendaciones."
* "¿Dónde están nuestras mayores oportunidades y riesgos en todos los canales en este momento?"

{% endtab %}
{% endtabs %}

## Visualizaciones {#visualizations}

Operator añade un gráfico cuando los datos lo permiten. Los **gráficos de líneas** son adecuados para series temporales, los **gráficos de barras** para comparaciones por categoría y las **tablas** cubren otros casos. Las tablas muestran porcentajes con dos decimales y usan comas para números grandes.

Cuando una respuesta incluye múltiples métricas, Operator prioriza las tasas de participación (*tasa de apertura*, *tasa de clics*, *tasa de apertura de push*) sobre los conteos brutos.

## Canales y métricas compatibles {#supported-channels-and-metrics}

Los *ingresos atribuidos* y las *conversiones* usan la misma agregación por Campaign, Canvas, canal y programa que se muestra en [Preguntas de ejemplo](#example-questions) en la pestaña **Ingresos y conversiones**.

| Canal | Métricas | Puntos de referencia del sector |
| --- | --- | --- |
| Correo electrónico | *Envíos*, *Entregas*, *Unique Opens*, *Clics únicos*, *Cancelaciones de suscripción* | Sí |
| Push (iOS, Android, Web) | *Envíos*, *Entregas*, *Aperturas* | Sí |
| SMS | *Envíos*, *Entregas*, *Clics en enlaces* | Sí |
| In-App Messages | *Impresiones*, *Clics* | Sí |
| Content Cards | *Envíos*, *Impresiones*, *Clics* | Sí |
| WhatsApp | *Envíos*, *Entregas*, *Lecturas*, *Clics* | Aún no |
| RCS | *Envíos*, *Entregas*, *Lecturas*, *Clics* (incluidos los subtipos de URL de texto, botón, acción, acción de respuesta y botón de respuesta) | Aún no |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Canales compatibles, métricas y disponibilidad de puntos de referencia" }

{% alert tip %}
Operator usa conteos únicos para las tasas (por ejemplo, *Unique Opens* divididas entre *entregas* para la *tasa de apertura de correo electrónico*). Si una cifra difiere de un panel, compara la ventana de atribución, el rango de tiempo y la definición. Operator enumera los tres en cada respuesta.
{% endalert %}

## Períodos de tiempo y ventanas de atribución {#time-periods-and-attribution-windows}

### Año fiscal vs. año calendario {#fiscal-year-vs-calendar-year}

Operator Analyze usa de forma predeterminada el **año fiscal de Braze**, que va del 1 de febrero al 31 de enero.

| Trimestre fiscal | Meses |
| --- | --- |
| FQ1 | Feb – Abr |
| FQ2 | May – Jul |
| FQ3 | Ago – Oct |
| FQ4 | Nov – Ene |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Trimestres fiscales de Braze y meses del calendario" }

Para preguntas sobre el año calendario, incluye "CY", "año calendario" o "año estándar". Las indicaciones ambiguas como "el año pasado" hacen que Operator confirme a qué calendario te refieres.

También puedes usar rangos en formato ISO como `Q4 2025` o `2025-03-01 to 2025-05-31`.

### Ventanas de atribución {#attribution-windows}

Operator Analyze usa de forma predeterminada **7 días**. Indica una ventana en tu pregunta para cambiarla:

* **1 día** para verificaciones rápidas de participación
* **3 días** para Campaigns de ciclo corto
* **7 días** para resúmenes generales y lecturas de Campaigns (predeterminado)
* **30 días** para vistas estratégicas o de largo plazo
* **Todas las ventanas** para una comparación lado a lado de 1D / 3D / 7D / 30D

Si los resultados difieren en más del 50 % entre ventanas, Operator muestra las cuatro lado a lado.

## Actualización de datos {#data-freshness}

Los datos se actualizan diariamente. La actividad del mismo día aparece después de la siguiente actualización. Cada respuesta indica la fecha más reciente del conjunto de datos. Si esa fecha parece desactualizada, ponte en contacto con tu administrador de éxito de cliente.

## Fuera del alcance {#whats-out-of-scope}

* **Desgloses de rendimiento a nivel de producto.** Los *ingresos atribuidos* y la participación se agregan a nivel de Campaign, Canvas, canal o programa. No se desglosan por productos o SKU. Las preguntas a nivel de producto o SKU no son compatibles. Ponte en contacto con tu administrador de éxito de cliente para esos análisis.
* **Puntos de referencia del sector para WhatsApp y RCS.** Las métricas de participación para ambos canales son compatibles. Los puntos de referencia aún no están disponibles.

Las preguntas fuera del alcance reciben una respuesta directa, una alternativa sugerida cuando es posible, o una referencia a tu administrador de éxito de cliente.

## Consejos para obtener mejores resultados {#tips-for-better-results}

* **Rango de tiempo:** Prefiere rangos explícitos ("FY26 Q2", "los últimos 90 días") en lugar de frases vagas como "el trimestre pasado" cuando necesitas precisión.
* **Métricas:** Nombra la tasa que te interesa (*tasa de apertura*, *tasa de click-through*, *tasa de clic a apertura*). Operator informa la fórmula que utilizó.
* **Seguimientos:** Profundiza en un resultado, cambia la ventana o cambia de canal. Operator mantiene el contexto a lo largo del hilo.
* **Terminología de canales:** WhatsApp y RCS usan *tasa de lectura* (no *tasa de apertura*). SMS usa *tasa de clics en enlaces*.
* **Solicitudes combinadas:** Se admite punto de referencia más tendencia en una sola indicación.

## Privacidad y seguridad de datos {#data-privacy-and-security}

Operator Analyze sigue el mismo modelo de privacidad y seguridad que BrazeAI Operator<sup>TM</sup>. Para más información, consulta [Privacidad y seguridad de datos]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security).

## Próximos pasos {#next-steps}

* [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator)
* [Revisar acciones]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions)