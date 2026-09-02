---
nav_title: "Crear un correo electrónico transaccional"
article_title: "Crear un correo electrónico transaccional"
page_order: 1

description: "Este artículo de referencia cubre cómo crear y configurar una nueva campaña de correo electrónico transaccional de Braze."
page_type: reference
tool:
  - Campaigns
channel: email
alias: "/api/api_campaigns/transactional_campaigns"

---

# Crear un correo electrónico transaccional {#create-a-transactional-email}

> Los correos electrónicos transaccionales de Braze se envían para facilitar una transacción acordada entre un remitente y el destinatario. Este artículo de referencia cubre cómo crear una campaña de correo electrónico transaccional en el panel de Braze y generar un `campaign_id` para incluir en tus llamadas a la API para nuestro [endpoint `/transactional/v1/campaigns/{campaign_id}/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).

{% alert important %}
El correo electrónico transaccional de Braze solo está disponible como parte de paquetes selectos de Braze. Ponte en contacto con tu CSM de Braze o abre un [ticket de soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support) para más detalles.
{% endalert %}

El tipo de campaña de correo electrónico transaccional está diseñado específicamente para enviar mensajes de correo electrónico automatizados y no promocionales con el fin de facilitar una transacción acordada entre tú y tus clientes. Esto incluye información como:

- Confirmaciones de pedidos
- Restablecimiento de contraseñas
- Alertas de facturación
- Alertas de envío

En resumen, puedes usar correos electrónicos transaccionales para enviar notificaciones críticas para el negocio que se originan desde tu servicio para un único usuario, donde la velocidad es de suma importancia.

{% alert important %}
Los correos electrónicos transaccionales difieren de las campañas transaccionales, que pueden usarse para dirigirte a tus usuarios sin costes adicionales. Las campañas transaccionales, por ejemplo, pueden incluir mensajes enviados después de que un usuario añade un artículo a su carrito. Consulta las [opciones de segmentación de audiencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) para más información.
{% endalert %}

{% alert note %}
Los envíos de la API de correo electrónico transaccional son compatibles con el archivado de mensajes. Si el archivado de mensajes está habilitado para correo electrónico en tu espacio de trabajo, Braze guarda una copia renderizada de cada envío de correo electrónico transaccional. Para más información, consulta [Archivado de mensajes]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/message_archiving).
{% endalert %}

## Paso 1: Crear una nueva campaña {#step-1-create-a-new-campaign}

Para crear una nueva campaña de correo transaccional, crea una campaña y selecciona **Transactional Email** como tu canal de mensajería.

![Desplegable Crear Campaign con la opción de correo transaccional resaltada.]({% image_buster /assets/img/transactional_email_campaign.png %}){: width="534" height="800" style="float:right;max-width:35%;margin-left:15px;height:auto;"}

Ahora puedes continuar con la configuración de tu campaña de correo transaccional.

## Paso 2: Configura tu campaña {#step-2-configure-your-campaign}

El flujo de creación de campaña para las campañas de correo transaccional se simplifica en comparación con el de una [campaña de correo electrónico estándar]({{site.baseurl}}/user_guide/channels/email/html_editor) para garantizar que tu correo transaccional crítico para el negocio pueda llegar a todos los usuarios.

Como resultado, notarás que varias configuraciones con las que puedes estar familiarizado de otros tipos de campaña de Braze no son necesarias al configurar este tipo de campaña:

- El paso **Entrega** se ha simplificado para eliminar las opciones de programación. Los correos transaccionales siempre se desencadenan a través de la REST API de Braze usando el ID de campaña que se muestra en la página **Entrega**. También se han eliminado configuraciones adicionales, como los controles de reelegibilidad y la configuración de limitación de frecuencia, para confirmar que todos los usuarios sean accesibles para estas alertas transaccionales críticas cuando tu servicio desencadena una solicitud de envío.
- El paso **Públicos objetivo** se ha eliminado. Como los correos transaccionales inscriben a toda tu base de usuarios como elegibles (incluidos los usuarios cancelados), no es necesario especificar filtros ni Segments. Como resultado, si tienes alguna lógica que aplicar a quién debe recibir este mensaje, te recomendamos aplicar esa lógica antes de determinar si hacer la solicitud de API a Braze para desencadenar el mensaje a un usuario específico.
- El paso **Conversiones** se ha eliminado. Los correos transaccionales no admiten el seguimiento de eventos de conversión en este momento.

![Flujo de trabajo de Composición, Entrega y Confirmación para crear una campaña de correo transaccional.]({% image_buster /assets/img/transactional_campaign_compose.png %}){: width="1586" height="1112" style="max-width:80%;height:auto;"}

Para configurar tu campaña de correo transaccional, sigue estos pasos:

1. Añade un nombre descriptivo para que puedas encontrar los resultados en tu página de **Campaigns** después de haber enviado tus mensajes.
2. Redacta tu correo electrónico o selecciona una plantilla.
3. Toma nota de tu `campaign_id`. Después de guardar tu campaña de API, debes incluir los campos `campaign_id` generados con tu solicitud de API donde se indica en el artículo del [endpoint de correo transaccional]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).
4. Haz clic en **Save Campaign**, ¡y estarás listo para comenzar tu campaña de API!

{% alert note %}
La configuración de cancelación de suscripción con un clic de la lista para campañas de correo transaccional se establece de forma predeterminada en **Usar valor predeterminado del espacio de trabajo**, similar a otras campañas de correo electrónico. Dado que está pensada para mensajería transaccional, Braze no añade la cancelación de suscripción con un clic. Para añadir la cancelación de suscripción con un clic a este tipo de campaña, [edita esta configuración]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#message-level-one-click-list-unsubscribe) en **Información de envío**.
{% endalert %}

### Etiquetas no permitidas en correos transaccionales {#disallowed-tags-in-transactional-emails}

Las etiquetas de Liquid `Connected Content` y `Promotion Code` no están disponibles en las campañas de correo transaccional.

Usar la etiqueta `Connected Content` requiere que Braze haga una solicitud de API saliente durante nuestro proceso de envío, lo cual puede ralentizar el proceso de envío del mensaje si el servicio externo al que hacemos la solicitud experimenta latencia. De manera similar, la etiqueta `Promotion Code` requiere que Braze realice un procesamiento adicional para evaluar la disponibilidad de un código promocional antes del envío, lo cual puede ralentizar el proceso de envío en caso de que no haya uno disponible.

Como resultado, no admitimos incluir las etiquetas `Connected Content` o `Promotion Code` en ningún campo de tu campaña de correo transaccional.