---
nav_title: Tipos de entrega y entrada
article_title: Tipos de entrega y entrada
page_order: 5
page_type: reference
description: "Este artículo de referencia describe los tipos de entrega para campañas, los tipos de entrada para Canvas y las características basadas en el tiempo al configurar una campaña o un Canvas."
tool:
    - Campaigns
    - Canvas
---

# Tipos de entrega y entrada {#delivery-and-entry-types}

> En Braze, hay tres formas diferentes de planificar tu mensaje: planificada, basada en acciones y desencadenada por API. Elegir cómo y cuándo se entrega tu mensaje es crucial para desarrollar un mensaje eficaz.

Para las campañas, el tipo de entrega determina cuándo tus usuarios entrarán en tu campaña y cuándo se enviará. Dado que un Canvas se construye como un recorrido continuo del usuario, el concepto de mensajería de una planificación se denomina tipo de entrada.

| Tipos de entrega<nobr> y entrada | Descripción |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Planificada** | Este tipo de planificación está diseñado para mensajes únicos que deseas enviar de inmediato, como campañas sobre un evento actual. <br><br>Al enviar mensajes de prueba dirigidos solo a ti o a tu equipo, esta opción te permite entregarlos de inmediato. |
| **Basada en acciones** | Los mensajes de entrega basada en acciones, o campañas y Canvas desencadenados por eventos, son muy eficaces para mensajes transaccionales o basados en logros. Puedes desencadenarlos para que se envíen después de que un usuario complete un evento determinado, en lugar de enviar tu mensaje en días específicos. |
| **Desencadenada por API** | Los mensajes desencadenados por API te permiten administrar el texto del mensaje, las pruebas multivariante y las reglas de reelegibilidad en el dashboard de Braze, mientras desencadenas la entrega de ese contenido desde tus propios servidores y sistemas. <br><br>La solicitud de API para desencadenar el mensaje también puede incluir datos adicionales para insertarlos en el mensaje en tiempo real mediante plantillas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de entrega y entrada" }

## Opciones basadas en el tiempo {#time-based-options}

{% tabs %}
{% tab Campaign %}
Puedes elegir entre las siguientes opciones cuando uses la entrega planificada:

- Enviar tan pronto como se lance la campaña
- Enviar a una hora designada
- [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)
{% endtab %}

{% tab Canvas %}
Con la entrega planificada, los usuarios entrarán según una planificación de tiempo, de forma similar a como planificarías una campaña. Puedes inscribir usuarios en un Canvas tan pronto como se lance o a una hora designada.

### Horas designadas {#designated-times}

Puedes elegir enviar tu Canvas con una frecuencia de entrada específica, incluyendo solo una vez, diariamente, semanalmente o mensualmente. Para Canvas con una entrega planificada recurrente, puedes configurar la recurrencia para permitir que los usuarios entren en el Canvas hasta 30 veces designadas.
{% endtab %}
{% endtabs %}

## Opciones basadas en acciones {#action-based-options}

{% tabs %}
{% tab Campaign %}
La entrega basada en acciones enviará campañas a los usuarios que realicen una acción específica. Después de que ocurra esta acción, puedes decidir cuándo enviar la campaña: de inmediato, después de un tiempo específico, a una hora específica o en un momento futuro.
{% endtab %}

{% tab Canvas %}
Las opciones basadas en acciones determinan qué acciones (o desencadenantes) necesita realizar un usuario para entrar en un Canvas y en qué momento específico se le permite comenzar a entrar. Por ejemplo, podrías evaluar a tus usuarios por las siguientes acciones:

- Abrir tu aplicación
- Añadir una dirección de correo electrónico
- Entrar en una ubicación

### Ventana de entrada {#entry-window}

La ventana de entrada de tu Canvas determina qué usuarios pueden entrar en el Canvas a la hora de inicio designada (y la hora de finalización opcional). De forma similar a las campañas basadas en acciones, puedes elegir que los usuarios entren en su zona horaria local.
{% endtab %}
{% endtabs %}

## Opciones de desencadenamiento por API {#api-trigger-options}

{% tabs %}
{% tab Campaign %}
Cuando selecciones desencadenada por API como tu opción de entrega, recibirás un ID de campaña para identificar qué campaña enviar con el [punto de conexión `/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#prerequisites).
{% endtab %}

{% tab Canvas %}
Cuando selecciones desencadenada por API como tu tipo de entrada, recibirás un ID de Canvas para identificar qué Canvas enviar con el [punto de conexión `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).
{% endtab %}
{% endtabs %}