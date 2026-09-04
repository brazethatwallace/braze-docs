---
nav_title: Optimizar con BrazeAI<sup>TM</sup>
article_title: Optimización de pruebas A/B con BrazeAI<sup>TM</sup>
page_order: 1.6
description: "Descubre cómo Optimizar con BrazeAI selecciona y distribuye automáticamente las variantes con mejor rendimiento en Campaigns de envío único y de envío múltiple."
search_rank: 10
toc_headers: h2
---

# Optimización de pruebas A/B con BrazeAI<sup>TM</sup> {#optimizing-ab-tests-with-brazeai}

> Activa **Optimizar con BrazeAI<sup>TM</sup>** para optimizar automáticamente una Campaign con múltiples variantes. El método de optimización depende de si la Campaign se envía una vez o se envía varias veces.

## Requisitos previos {#prerequisites}

Para usar **Optimize with BrazeAI<sup>TM</sup>**, tu Campaign debe incluir al menos dos variantes de mensaje.

Para una Campaign de envío múltiple, también debes:

- Definir al menos un evento de conversión.
- Establecer la ventana de reelegibilidad en 24 horas o más.

## Activar la optimización {#turn-on-optimization}

En el paso **Target Audiences**, ve a **Pruebas A/B** y activa **Optimize with BrazeAI<sup>TM</sup>**.

## Campaigns de envío único {#single-send-campaigns}

Para una Campaign de envío único, Braze envía una porción inicial de la audiencia a cada variante. Una vez que finaliza la duración del experimento, BrazeAI<sup>TM</sup> selecciona la variante con mejor rendimiento y la envía a la audiencia restante.

Braze aplica la configuración recomendada cuando activas la optimización. Para cambiar esta configuración, abre **Controles avanzados**:

- **Objetivo de optimización:** Selecciona la métrica que BrazeAI<sup>TM</sup> utiliza para comparar variantes. Los objetivos disponibles dependen del canal.
- **Duración del experimento:** Selecciona 4 horas, 24 horas, 72 horas, o introduce una duración personalizada.
- **Distribución de variantes:** Cambia el porcentaje asignado a cada variante o grupo de control.

La duración predeterminada del experimento es de 4 horas. Si optimizas para un evento de conversión primaria, el valor predeterminado es 24 horas.

### Objetivos de optimización predeterminados por canal {#default-optimization-goals-by-channel}

| Canal | Objetivo predeterminado |
|---|---|
| Notificaciones push | *Aperturas* |
| Correo electrónico | *Clics únicos* |
| SMS, MMS, RCS y WhatsApp | *Clics* |
| Otros canales compatibles | *Evento de conversión primaria - A* |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Objetivos de optimización predeterminados por canal" }

## Campaigns de envío múltiple {#multi-send-campaigns}

Para Campaigns recurrentes, basadas en acciones y activadas por API que se envían varias veces, BrazeAI<sup>TM</sup> optimiza continuamente la distribución de tu audiencia. Después de la fecha límite de conversión inicial, Braze revisa el rendimiento cada 12 horas y envía más usuarios a las variantes con mejor rendimiento.

La distribución inicial puede ser uniforme mientras BrazeAI<sup>TM</sup> recopila datos de rendimiento. La distribución cambia a medida que la optimización identifica tendencias de rendimiento.

Abre **Controles avanzados** para agregar o eliminar un grupo de control. Un grupo de control proporciona una línea de base para medir el rendimiento de la Campaign y no recibe un mensaje.

## Informes {#reporting}

Una vez que se completa un experimento de envío único, o después de que una campaña de envíos múltiples haya recopilado suficientes datos, la página **Campaign Analytics** muestra el incremento producido por la optimización.

![Análisis de Campaign mostrando el incremento de Optimizar con BrazeAI<sup>TM</sup>, incluyendo métricas de comparación después de la ventana del experimento.]({% image_buster /assets/img_archive/braze_ai_variant_selection_reporting.png %})

Para más información, consulta [Análisis de pruebas A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics).

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Por qué no puedo activar Optimizar con BrazeAI<sup>TM</sup>? {#why-cant-i-turn-on-optimize-with-brazeai}

La optimización no está disponible cuando:

- La Campaign tiene menos de dos variantes activas.
- Una Campaign de envío múltiple no tiene eventos de conversión.
- Una Campaign de envío múltiple tiene una ventana de reelegibilidad inferior a 24 horas.

### ¿Por qué mis variantes tienen recuentos de envío similares al principio? {#why-do-my-variants-have-similar-send-counts-at-first}

BrazeAI<sup>TM</sup> comienza con una distribución inicial para recopilar datos de rendimiento. Ajusta la distribución con el tiempo a medida que identifica tendencias de rendimiento.

### ¿Puede una Campaign de envío múltiple dejar de optimizar sin seleccionar una variante? {#can-a-multi-send-campaign-stop-optimizing-without-selecting-one-variant}

Sí. La optimización se detiene cuando BrazeAI<sup>TM</sup> tiene un 95 % de confianza en que continuar el experimento no mejorará la tasa de conversión en más de un 1 % de su tasa actual.