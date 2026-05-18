---
nav_title: "Tutorial: Restaurante de servicio rápido"
article_title: Tutorial de Intelligence Suite
page_order: 10
search_rank: 12
description: "¿Eres nuevo en Intelligence Suite de Braze? Empieza con este tutorial."
tool:
  - Dashboard
---

# Tutorial de Intelligence Suite {#intelligence-suite-tutorial}

> ¿Eres nuevo en Intelligence Suite de Braze? ¡Empieza con este tutorial! Para obtener información más general, consulta [Intelligence Suite]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/).

## Tutorial: Restaurante de servicio rápido {#tutorial-quick-service-restaurant}

Imaginemos que trabajamos en SandwichEmperor, un restaurante de comida rápida que tiene un nuevo artículo de menú por tiempo limitado: el Royal Roast. Utilizaremos dos características de Intelligence Suite para enviar promociones personalizadas en un Canvas.

### Paso 1: Utiliza Intelligent Timing para saber cuándo enviar las notificaciones {#step-1-use-intelligent-timing-for-when-to-send-notifications}

Utilizaremos Intelligent Timing para analizar las interacciones pasadas de nuestros usuarios con nuestra aplicación y cada canal de mensajería, y luego seleccionar automáticamente el mejor momento para promocionar el Royal Roast a cada usuario. Algunos usuarios pueden recibir la promoción por la tarde, mientras que otros pueden recibirla por la noche.

Proporcionaremos una hora alternativa para los usuarios que no tengan suficientes interacciones pasadas para analizar: la hora más popular de uso de la aplicación entre todos los usuarios.

![Configuración de entrega de Intelligent Timing para un paso de mensaje.]({% image_buster /assets/img/intelligence_suite1.png %})

### Paso 2: Utiliza Intelligent Selection para seleccionar la promoción {#step-2-use-intelligent-selection-to-select-the-promotion}

Para los mensajes promocionales propiamente dichos, utilizaremos Intelligent Selection para probar tres mensajes diferentes (notificación push, correo electrónico y SMS) para el Royal Roast. Intelligent Selection analizará el rendimiento de todos nuestros mensajes promocionales dos veces al día y, a continuación, enviará gradualmente más mensajes de los que obtengan mejores resultados y menos de los demás.

Después de que Intelligent Selection reúna suficientes datos para determinar el mensaje con mejor rendimiento, utilizará ese mensaje en el 100% de los envíos futuros.

![Sección de pruebas A/B de un Canvas con Intelligent Selection habilitada.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

### Paso 3: Lanza el Canvas {#step-3-launch-the-canvas}

Tanto con Intelligent Timing como con Intelligent Selection, hemos configurado nuestras promociones del Royal Roast para optimizar el tiempo y la mensajería. Podemos lanzar nuestro Canvas y ver cómo nuestros envíos cambian para adaptarse a las preferencias de los usuarios.