---
nav_title: Mejorar la baja latencia
article_title: Mejorar la baja latencia para Content Cards como banners
page_order: 10
description: "Este artículo cubre estrategias para garantizar que se cumplan los requisitos de baja latencia con Content Cards."
channel:
  - content cards
---

# Mejorar la latencia para Content Cards como banners {#improve-latency-for-content-cards-as-banners}

> Si estás experimentando latencia con tu implementación de Content Cards para casos de uso críticos, como banners en la página de inicio, revisa esta página para conocer estrategias y consejos que te ayuden a resolver y acelerar tu renderizado.

{% alert tip %}
¿Estás intentando mostrar banners prominentes y personalizados en tu aplicación o sitio web? Prueba los [Banners]({{site.baseurl}}/user_guide/channels/banners), que están diseñados para admitir casos de uso de banners con baja latencia.
{% endalert %}

## Usa entrada planificada en lugar de entrada basada en acciones {#use-scheduled-entry-instead-of-action-based-entry}

Las tarjetas basadas en acciones, tanto en Campaigns como en Canvas, requieren procesamiento en segundo plano. Braze primero debe recibir notificación de la acción desencadenante (como una compra realizada o el inicio de una sesión) antes de crear una tarjeta para un usuario. Como resultado, habrá un retraso antes de que estas tarjetas estén disponibles.

Las tarjetas basadas en acciones añadirán complejidad adicional a tu aplicación, donde podrías encontrarte consultando y actualizando continuamente para esperar a que la tarjeta esté disponible. En su lugar, configura tu tarjeta como `Scheduled Entry`, que actuará como una ventana de disponibilidad para que la tarjeta siempre esté disponible para la audiencia objetivo.

Si planificas tus tarjetas con anticipación, estarán listas, esperando a que el usuario abra tu aplicación y solicite tarjetas.

## Usa la lógica de envío "At First Impression" {#use-at-first-impression-send-logic}

Junto con los envíos planificados, la opción `At First Impression` evitará la latencia gracias a la velocidad con la que se crea y almacena una tarjeta en Braze. La opción `At Campaign Launch` crea todas las tarjetas para todos los usuarios segmentados con anticipación, lo que puede tardar en completarse. La opción `At First Impression` generará una tarjeta para un usuario la primera vez que se solicite, como cuando un usuario abre tu aplicación por primera vez.

Esto significa que, junto con la entrada planificada, las tarjetas estarán disponibles de inmediato, tan pronto como las necesites, ya sea al inicio de la sesión o para una ventana de elegibilidad basada en tiempo.

## Recuerda que la entrada al Canvas es un requisito previo para recibir tarjetas {#remember-that-canvas-entry-is-a-prerequisite-for-receiving-cards}

Al usar Canvas, recuerda que un usuario primero debe entrar al Canvas según los criterios de entrada que hayas configurado, y *luego* debe avanzar a través del paso de mensaje de tarjeta de contenido. Solo entonces la tarjeta estará disponible para tu aplicación o sitio web. Recuerda que existe una latencia incorporada para que la tarjeta se cree una vez que el usuario pasa por el paso, lo que puede retrasar el momento en que la tarjeta esté disponible.

## No actualices las tarjetas de forma excesiva {#dont-refresh-cards-excessively}

Content Cards se actualizan automáticamente por el SDK al inicio de cada nueva sesión. También puedes solicitar manualmente una actualización de Content Cards en cualquier momento durante una sesión activa.

Llamar al método `requestContentCardsRefresh` y actualizar con demasiada frecuencia puede provocar un límite de velocidad. Si tu aplicación queda temporalmente limitada, es posible que no puedas actualizar las tarjetas cuando lo necesites o en un momento crítico de la interacción del usuario con tu aplicación.

Para evitar que esto suceda, llama a este método de actualización solo en momentos importantes del ciclo de vida del usuario, como después de que un usuario realice una compra o después de que un usuario actualice su nivel de suscripción.

## Evita incluir contenido conectado {#avoid-including-connected-content}

El contenido conectado enriquece Content Cards con datos de API propios o de terceros. Sin embargo, cuando se incluye en un mensaje de tarjeta de contenido, bloqueará la disponibilidad de la tarjeta hasta que se complete la solicitud de red del contenido conectado. En algunos casos, esto hará que los SDK reintenten unos segundos después en un esfuerzo por no retrasar la lógica de renderizado de tu aplicación, que puede estar esperando a que el SDK complete su tarea de actualización.

Si necesitas usar contenido conectado, planifica estas tarjetas con anticipación y usa la opción `At Campaign Launch` para que las tarjetas se creen previamente antes de la próxima sesión del usuario. Ten en cuenta que estas tarjetas no estarán disponibles de inmediato, ya que Braze escribe todas las tarjetas para todos los usuarios elegibles.