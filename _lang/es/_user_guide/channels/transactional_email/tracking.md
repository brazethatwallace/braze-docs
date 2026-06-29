---
nav_title: "Configurar el seguimiento"
article_title: "Seguimiento"
page_order: 2
description: "Este artículo de referencia explica cómo configurar el seguimiento en tiempo real para campañas de correo electrónico transaccional."
page_type: reference
tool:
  - Campaigns
channel: email

---

# Seguimiento de correos electrónicos transaccionales {#track-transactional-emails}

> Esta página describe cómo configurar el seguimiento en tiempo real para [campañas de correo electrónico transaccional]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email/). Para más información sobre el punto de conexión en sí, consulta [Enviar correos electrónicos transaccionales mediante entrega activada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/).

Cuando envías correos electrónicos transaccionales, como confirmaciones de pedido o restablecimientos de contraseña, es fundamental saber si llegan a tus clientes. Con los postbacks de eventos HTTP transaccionales de Braze, obtendrás información en tiempo real sobre el estado de cada correo electrónico transaccional, para que puedas actuar rápidamente si surge algún problema.

Usa esta característica para:

- **Monitorear tus correos electrónicos en tiempo real:** Ver de inmediato si los mensajes se envían, procesan, entregan o encuentran problemas.
- **Responder de forma proactiva:** Reintentar mensajes, cambiar a otro canal como SMS o usar sistemas alternativos para asegurarte de que tus comunicaciones se entreguen.

## Seguimiento de tus correos electrónicos transaccionales {#tracking-your-transactional-emails}

{% multi_lang_include channels/transactional_email/http_event_postback.md %}