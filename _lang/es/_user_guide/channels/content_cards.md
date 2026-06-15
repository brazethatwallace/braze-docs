---
nav_title: Tarjetas de contenido
article_title: Tarjetas de contenido
page_order: 2
page_type: landing
description: "Envía un flujo dinámico de contenido enriquecido a tus usuarios con Tarjetas de contenido, integradas directamente en tu aplicación o sitio web."
channel:
  - content cards
search_rank: 5
---

# Tarjetas de contenido

> Con las Tarjetas de contenido, puedes enviar un flujo de contenido enriquecido altamente segmentado y dinámico a tus clientes dentro de las aplicaciones que les encantan, sin interrumpir su experiencia. Las Tarjetas de contenido se integran directamente en tu aplicación o sitio web, lo que te permite crear buzones de entrada de mensajes e interfaces personalizadas que amplían el alcance de otros canales como el correo electrónico o las notificaciones push.

## Requisitos previos

La disponibilidad de las Tarjetas de contenido depende de tu paquete de Braze. Ponte en contacto con tu director de cuentas o administrador del éxito del cliente para empezar.

Antes de poder usar las Tarjetas de contenido, necesitas integrar el [SDK de Braze]({{site.baseurl}}/developer_guide/content_cards/) en tu aplicación o sitio web. No se requiere configuración adicional. Para crear tu propia interfaz, consulta la [guía de personalización de Tarjetas de contenido]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/).

## Beneficios de usar Tarjetas de contenido

Estos son algunos beneficios de usar Tarjetas de contenido en lugar de que tus desarrolladores integren contenido directamente en tu aplicación:

- **Segmentación y personalización más fáciles:** Tus datos de usuario están en Braze, lo que facilita definir tu audiencia y personalizar tus mensajes con Content Cards.
- **Informes centralizados:** Los análisis de tarjeta se rastrean en Braze, por lo que tienes información sobre todas tus Campaigns en una sola ubicación.
- **Recorridos del cliente cohesivos:** Puedes combinar Content Cards con otros canales en Braze para crear experiencias de cliente consistentes. Un caso de uso popular es enviar una notificación push y luego guardar esa notificación como una Content Card en tu aplicación para cualquier persona que no haya interactuado con el push. Si el contenido lo integran directamente tus desarrolladores en la aplicación, queda aislado del resto de tu mensajería.
- **No se requiere adhesión voluntaria:** De forma similar a In-App Messages, Content Cards no requieren adhesión voluntaria ni permisos de tus usuarios. Pero mientras que In-App Messages no requieren permisos y son de corta duración, Content Cards no requieren permisos y son permanentes. Esto significa que las estrategias de mensajería que combinan In-App Messages y Content Cards logran un gran equilibrio.
- **Más control sobre la experiencia de mensajería:** Aunque seguirás necesitando a tus desarrolladores para la configuración inicial de Content Cards, después podrás controlar el mensaje, los destinatarios, el momento de envío y más directamente desde tu dashboard de Braze.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

## Tarjetas de contenido en cifras

Cuando creas Tarjetas de contenido en Braze, puedes actualizar la mensajería y medir el impacto sin necesidad de renovar tu aplicación o sitio web. Datos destacados de la investigación de Braze incluyen:

- Las Content Cards son **38 veces** más efectivas que el correo electrónico para impulsar las ventas en una ventana de 72 horas.[^1]
- Usar Content Cards en campañas de inscripción a programas de fidelización aumenta las conversiones **5 veces**.[^1]
- La comunicación a través de notificaciones push, In-App Messages y Content Cards genera **6,9 veces** más sesiones que el push solo.[^2]
- La comunicación a través de correo electrónico, In-App Messages y Content Cards genera un tiempo de vida promedio del usuario **3,6 veces** más largo que el correo electrónico solo.[^2]

[^1]: [8 consejos para sacar el máximo partido a tus campañas de retención de clientes](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2]: [Informe: La diferencia del marketing multicanal](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)

## Casos de uso

Consulta esta sección para conocer algunos casos de uso comunes de las Tarjetas de contenido.

{% alert tip %}
Para más inspiración, consulta la [Guía de inspiración de Tarjetas de contenido](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide), que incluye más de 20 campañas personalizables, como programas de referidos, lanzamientos de nuevos productos y renovaciones de suscripciones.
{% endalert %}

{% tabs %}
{% tab Incorporación y próximos pasos %}

A medida que los nuevos usuarios exploran tu aplicación y sitio web, guíalos a través de los valores y beneficios de lo que ofreces con Tarjetas de contenido ubicadas estratégicamente. Anima a los usuarios a suscribirse a otros canales de comunicación con una tarjeta de contenido en tu página de inicio, y guarda las tareas de incorporación pendientes en una pestaña dedicada de incorporación impulsada por Tarjetas de contenido. ¡No olvides eliminar una tarjeta después de que el usuario complete la tarea deseada!

![Ejemplo de caso de uso de incorporación con Tarjetas de contenido.]({% image_buster /assets/img_archive/cc_usecase_onboarding.png %})

{% endtab %}
{% tab Asistencia a eventos %}

Muestra Tarjetas de contenido en la parte superior de la página de inicio del usuario para fomentar la asistencia a eventos, utilizando la segmentación por ubicación para llegar a los usuarios potenciales donde se encuentran. Invitar a los usuarios a eventos presenciales relevantes los hace sentir especiales, especialmente con mensajería personalizada que aprovecha su actividad previa con tu marca.

![Ejemplo de caso de uso de asistencia a eventos con Tarjetas de contenido.]({% image_buster /assets/img_archive/cc_usecase_event.png %})

{% endtab %}
{% tab Recomendaciones %}

Usa los datos que tienes sobre los comportamientos y preferencias de los usuarios para mostrar contenido relevante en tiempo real desde Tarjetas de contenido en la página de inicio o en el buzón de entrada, y atráelos de vuelta a tu oferta de productos.

![Ejemplo de caso de uso de recomendaciones con Tarjetas de contenido.]({% image_buster /assets/img_archive/cc_usecase_recommendation.png %})

{% endtab %}
{% tab Ventas y promociones %}

Aprovecha las Tarjetas de contenido para destacar mensajes promocionales y ofertas no reclamadas directamente en tu página de inicio o en un buzón de entrada promocional dedicado. Muestra contenido relevante basado en las compras anteriores de cada cliente para ofrecer promociones personalizadas que capten la atención.

![Ejemplo de caso de uso de ventas y promociones con Tarjetas de contenido.]({% image_buster /assets/img_archive/cc_usecase_promo.png %})

{% endtab %}
{% endtabs %}

### Otros casos de uso

Más allá de estos casos de uso principales, los clientes utilizan las Tarjetas de contenido de muchas formas diferentes. El poder de las Tarjetas de contenido está en su flexibilidad. Si el caso de uso que deseas no se muestra aquí, puedes configurar [pares clave-valor]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs/) y enviar las cargas útiles a tu aplicación o sitio web.

Para un resumen sobre cómo implementar ubicaciones de Tarjetas de contenido en tu aplicación o sitio web, consulta [Crear Tarjetas de contenido personalizadas]({{site.baseurl}}/developer_guide/content_cards/creating_cards/).

## Próximos pasos

- [Crear una tarjeta de contenido]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/)
- [Detalles creativos]({{site.baseurl}}/user_guide/channels/content_cards/creative_details/)