---
nav_title: Content Cards
article_title: Content Cards
page_order: 2
page_type: landing
description: "Envía un flujo dinámico de contenido enriquecido a tus usuarios con Content Cards, integradas directamente en tu aplicación o sitio web."
channel:
  - content cards
search_rank: 5
---

# Content Cards {#content-cards}

> Con Content Cards, puedes enviar un flujo de contenido enriquecido altamente segmentado y dinámico a tus clientes dentro de las aplicaciones que les encantan, sin interrumpir su experiencia. Las Content Cards se integran directamente en tu aplicación o sitio web, lo que te permite crear buzones de entrada de mensajes e interfaces personalizadas que amplían el alcance de otros canales como el correo electrónico o las notificaciones push.

## Requisitos previos {#prerequisites}

La disponibilidad de Content Cards depende de tu paquete de Braze. Ponte en contacto con tu director de cuentas o administrador de éxito de cliente para empezar.

Antes de poder usar Content Cards, debes integrar el [SDK de Braze]({{site.baseurl}}/developer_guide/content_cards) en tu aplicación o sitio web. No se requiere configuración adicional. Para construir tu propia interfaz de usuario, consulta la [guía de personalización de Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards).

## Beneficios de usar Content Cards {#benefits-of-using-content-cards}

Estos son algunos beneficios de usar Content Cards en lugar de que tus desarrolladores construyan el contenido directamente en tu aplicación:

- **Segmentación y personalización más sencillas:** Los datos de tus usuarios están en Braze, lo que facilita definir tu audiencia y personalizar tus mensajes con Content Cards.
- **Informes centralizados:** Los análisis de Content Cards se registran en Braze, así que tienes información sobre todas tus Campaigns en una sola ubicación.
- **Recorridos del cliente cohesivos:** Puedes combinar Content Cards con otros canales en Braze para crear experiencias del cliente consistentes. Un caso de uso popular es enviar una notificación push y luego guardar esa notificación como una tarjeta de contenido en tu aplicación para cualquier persona que no haya interactuado con el push. Si el contenido lo construyen directamente tus desarrolladores en la aplicación, entonces queda aislado del resto de tu mensajería.
- **No se requiere adhesión voluntaria:** De manera similar a los mensajes dentro de la aplicación, Content Cards no requieren adhesión voluntaria ni permisos de tus usuarios. Pero mientras que los mensajes dentro de la aplicación no requieren permisos y son efímeros, Content Cards no requieren permisos y son permanentes. Esto significa que las estrategias de mensajería que combinan mensajes dentro de la aplicación y Content Cards logran un gran equilibrio.
- **Más control sobre la experiencia de mensajería:** Aunque seguirás necesitando a tus desarrolladores para la configuración inicial de Content Cards, después podrás controlar el mensaje, los destinatarios, el momento del envío y más directamente desde tu panel de Braze.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

## Content Cards en cifras {#content-cards-by-the-numbers}

Cuando creas Content Cards en Braze, puedes actualizar la mensajería y medir el impacto sin necesidad de reformar tu aplicación o sitio web. Los aspectos destacados de la investigación de Braze incluyen:

- Las Content Cards son **38 veces** más efectivas que el correo electrónico para impulsar las ventas en un período de 72 horas.[^1]
- El uso de Content Cards en Campaigns de inscripción de fidelización aumenta las conversiones **5 veces**.[^1]
- El alcance a través de notificaciones push, In-App Messages y Content Cards genera **6,9 veces** más sesiones que el push por sí solo.[^2]
- El alcance a través del correo electrónico, In-App Messages y Content Cards genera una vida útil promedio del usuario **3,6 veces** más larga que el correo electrónico por sí solo.[^2]

## Ejemplos {#use-cases}

Consulta esta sección para conocer algunos ejemplos comunes de Content Cards.

{% alert tip %}
Para más inspiración, consulta la [Guía de inspiración de Content Cards](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide), que incluye más de 20 campañas personalizables, como programas de referidos, lanzamientos de nuevos productos y renovaciones de suscripción.
{% endalert %}

{% tabs %}
{% tab Incorporación y próximos pasos %}

A medida que los nuevos usuarios exploran tu aplicación y sitio web, guíalos a través de los valores y beneficios de lo que ofreces con Content Cards colocadas estratégicamente. Anima a los usuarios a adherirse a otros canales de comunicación con una tarjeta de contenido en tu página de inicio, y guarda las tareas de incorporación pendientes en una pestaña de incorporación dedicada impulsada por Content Cards. ¡No olvides eliminar una tarjeta después de que un usuario complete la tarea deseada!

![Ejemplo de caso de uso de incorporación con Content Cards.]({% image_buster /assets/img_archive/cc_usecase_onboarding.png %})

{% endtab %}
{% tab Asistencia a eventos %}

Muestra Content Cards en la parte superior de la página de inicio de un usuario para fomentar la asistencia a eventos, utilizando la segmentación por ubicación para llegar a los usuarios potenciales donde se encuentren. Invitar a los usuarios a eventos físicos relevantes los hace sentir especiales, especialmente con mensajería personalizada que aprovecha su actividad previa con tu marca.

![Ejemplo de caso de uso de asistencia a eventos con Content Cards.]({% image_buster /assets/img_archive/cc_usecase_event.png %})

{% endtab %}
{% tab Recomendaciones %}

Utiliza los datos que tienes sobre los comportamientos y preferencias de los usuarios para mostrar contenido relevante en tiempo real desde Content Cards en la página de inicio o el buzón de entrada, y atráelos de vuelta a tu oferta de productos.

![Ejemplo de caso de uso de recomendaciones con Content Cards.]({% image_buster /assets/img_archive/cc_usecase_recommendation.png %})

{% endtab %}
{% tab Ventas y promociones %}

Aprovecha las Content Cards para destacar mensajes promocionales y ofertas no reclamadas directamente en tu página de inicio o en un buzón de entrada promocional dedicado. Muestra contenido relevante basado en las compras anteriores de cada cliente para ofrecer promociones personalizadas que capten la atención.

![Ejemplo de caso de uso de ventas y promociones con Content Cards.]({% image_buster /assets/img_archive/cc_usecase_promo.png %})

{% endtab %}
{% endtabs %}

### Otros ejemplos {#other-use-cases}

Fuera de estos ejemplos principales, los clientes usan Content Cards de muchas maneras diferentes. El poder de las Content Cards está en su flexibilidad. Si el ejemplo que deseas no se muestra aquí, puedes configurar [pares clave-valor]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) y enviar las cargas útiles a tu aplicación o sitio web.

Para un resumen sobre cómo implementar ubicaciones de Content Cards en tu aplicación o sitio web, consulta [Crear Content Cards personalizadas]({{site.baseurl}}/developer_guide/content_cards/creating_cards).

## Próximos pasos {#next-steps}

{% article_tiles %}
- name: Crear una tarjeta de contenido
  link: /docs/user_guide/channels/content_cards/create_a_content_card
- name: Detalles creativos
  link: /docs/user_guide/channels/content_cards/creative_details
{% endarticle_tiles %}

[^1]: [8 consejos para aprovechar al máximo tus campañas de retención de clientes](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2]: [Informe: La diferencia del marketing multicanal](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)