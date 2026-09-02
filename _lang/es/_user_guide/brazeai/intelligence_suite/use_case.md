---
nav_title: "Casos de uso"
article_title: "Caso de uso: Intelligence Suite"
page_order: 10
search_rank: 12
description: "¿Eres nuevo en Intelligence Suite de Braze? Lee este caso de uso sobre cómo se puede aprovechar Intelligent Timing para enviar promociones personalizadas en un Canvas unificado."
tool:
  - Dashboard
---

# Caso de uso: convierte el comportamiento pasado en la aplicación en ofertas personalizadas en el canal adecuado {#use-case-turn-past-app-behavior-into-personalized-offers-on-the-right-channel}

> Este ejemplo muestra cómo una marca ficticia utiliza Intelligent Timing para aprovechar los datos de interacción pasada con la aplicación y los mensajes, y enviar promociones personalizadas en un Canvas unificado.

Supongamos que Marvin es director de marketing en SandwichEmperor, un restaurante de comida rápida que lanza ofertas frecuentes por tiempo limitado. El equipo de Marvin se encarga de entregar mensajes promocionales en su aplicación para promocionar un nuevo artículo del menú por tiempo limitado: el Super Sub.

Hasta ahora, cada mensaje para artículos por tiempo limitado se gestionaba como un silo: diferentes pruebas de texto y enfoques se entregaban como envíos separados; probaban distintos ángulos de mensajería para impulsar una mayor interacción sin comprender del todo cuándo las promociones por tiempo limitado son más populares entre sus usuarios en la aplicación.

Para la nueva promoción del Super Sub, Marvin quiere un Canvas coordinado que siga aprendiendo con el tiempo, utilizando el comportamiento que Braze ya captura (sesiones, aperturas, clics) en lugar de adivinar los horarios de envío o un único mensaje ganador.

Con Intelligent Timing, Marvin puede entregar pasos de mensaje cuando cada persona tiene más probabilidades de interactuar, basándose en el análisis estadístico de interacciones pasadas (por ejemplo, patrones de sesión e interacción por canal).

Este recorrido describe cómo Marvin:

- Construye un Canvas con push, correo electrónico y servicio de mensajes cortos en pasos de mensaje
- Utiliza Intelligent Timing en esos pasos para que la entrega se alinee con los patrones de interacción inferidos por usuario y canal

## Paso 1: Define la métrica de éxito y construye el Canvas {#step-1-define-the-success-metric-and-build-the-canvas}

Marvin decide qué significa "éxito" para el Super Sub (por ejemplo, pedidos o un evento personalizado que se desencadena cuando alguien completa una compra del Super Sub o lo añade en la aplicación).

A continuación, Marvin crea un Canvas para que los nuevos usuarios entren en una planificación constante mientras la oferta esté activa.

1. En el dashboard de Braze, Marvin navega a **Messaging** > **Canvas**.
2. Crea un Canvas y lo nombra "Limited item - Super Sub".
3. Luego añade un evento de conversión y otra variante en el Canvas.
4. Completa los detalles restantes del Canvas y ya está listo para mapear el recorrido del usuario en el constructor de Canvas.

## Paso 2: Configura los ajustes de entrega {#step-2-set-up-delivery-settings}

En la pestaña **Delivery Settings** del paso de mensaje, Marvin planea usar Intelligent Timing para analizar las interacciones pasadas de sus usuarios con la aplicación y cada canal de mensajería, y luego seleccionar automáticamente el mejor momento para promocionar el Super Sub a cada usuario. Esto significa que algunos usuarios pueden recibir la promoción por la tarde, mientras que otros pueden recibirla por la noche.

Selecciona **la hora más popular para usar la aplicación entre todos los usuarios** para aquellos usuarios que no tienen suficientes interacciones pasadas para analizar.

## Paso 3: Añade retrasos e Intelligent Timing a los pasos de mensaje {#step-3-add-delays-and-intelligent-timing-to-message-steps}

Para los pasos de mensaje que usan Intelligent Timing, Marvin sigue las directrices de Canvas: coloca un paso de retraso de al menos dos días naturales entre la entrada (o un paso anterior) y el paso de mensaje con Intelligent Timing. Prefiere días naturales para los retrasos cuando usa Intelligent Timing, de modo que la entrega ocurra en el día previsto a la hora óptima de cada usuario.

En cada paso de mensaje de notificación push, correo electrónico y servicio de mensajes cortos, abre **Delivery Settings** y elige **Using Intelligent Timing**. Establece una hora alternativa para los usuarios que no tienen suficiente historial de interacción para determinar una hora óptima. Observa que los pasos de mensaje con múltiples canales pueden enviar o intentar enviar a diferentes horas por canal, reflejando cómo algunos clientes interactúan más con el correo electrónico por la mañana y con push por la noche.

## Paso 4: Monitorea y optimiza {#step-4-monitor-and-optimize}

Marvin coordina los activos promocionales del Super Sub en push, correo electrónico y servicio de mensajes cortos en los pasos de mensaje (y cualquier paso posterior que utilicen sus variantes) y lanza el Canvas.

Después del lanzamiento, observa los análisis del Canvas y los recuentos de conversión, y concluye que Intelligent Timing sigue optimizando cuándo se activa cada canal para cada usuario en función de los patrones de interacción en curso. Como resultado, Marvin ayudó con éxito a SandwichEmperor a conectar el rendimiento de las ofertas por tiempo limitado con cuándo y qué recorrido funciona, en lugar de solo qué mensaje promocional puntual ganó la última vez.