---
nav_title: Actualizaciones de precios de WhatsApp
permalink: "/whatsapp_pricing_updates/"
hidden: true
noindex: true
hide_toc: true
---

# Actualizaciones de precios de WhatsApp {#whatsapp-pricing-updates}

## Cambios adicionales en los precios de WhatsApp en octubre de 2025 {#additional-whatsapp-pricing-changes-in-october-2025}
*Última actualización: 3 de septiembre de 2025*

### Cambios de precios en algunas regiones {#pricing-changes-in-some-regions}

A partir del **1 de octubre**, Meta está actualizando las tarifas en mercados específicos.

- **Para mensajes de utilidad y autenticación:** Se están reduciendo las tarifas en Argentina, Egipto, México y Norteamérica para garantizar que los precios sigan siendo atractivos.
- **Para mensajes de marketing:** Se están reduciendo las tarifas en México para garantizar que los precios continúen motivando la adopción y fomentando un ecosistema de mensajería saludable.

| País y tipo de mensaje | % de cambio |
| --- | --- |
| Argentina - Autenticación                | -10,04%  |
| Argentina - Utilidad                       | -10,04%  |
| Egipto - Autenticación                    | -30,43%  |
| Egipto - Autenticación - Internacional    | -0,58%   |
| Egipto - Utilidad                           | -30,43%  |
| México - Marketing                        | -30,08%  |
| Norteamérica - Autenticación            | -70,39%  |
| Arabia Saudita - Autenticación             | -6,89%   |
| Arabia Saudita - Utilidad                    | -6,89%   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Cambios adicionales en los precios de WhatsApp en julio de 2025 {#additional-whatsapp-pricing-changes-in-july-2025}
*Última actualización: 12 de junio de 2025*

Además de las actualizaciones de precios de julio anunciadas previamente, Meta está implementando un par de actualizaciones adicionales que también entrarán en vigor el 1 de julio de 2025.

Aquí tienes un resumen rápido de los cambios anunciados anteriormente:
- Los precios de WhatsApp pasarán a un modelo "por mensaje" en lugar de un modelo "por conversación". **Las tarifas "por mensaje" serán las mismas que las tarifas actuales "por conversación".**
- Las plantillas de utilidad enviadas en respuesta a mensajes de usuarios (es decir, dentro de una [ventana de servicio al cliente](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows) abierta) serán gratuitas.

*Para más detalles sobre estos cambios, consulta la publicación anterior con fecha del 12 de marzo más adelante en este artículo.*

Cambios adicionales del 1 de julio (anunciados por Meta el 15 de mayo):
- Meta está actualizando las tarifas de utilidad y autenticación en varios mercados como parte de sus esfuerzos continuos para garantizar que los precios estén a la par con los canales alternativos.
    - Los precios de mensajería de utilidad y autenticación están bajando en todos los mercados excepto Indonesia. En Indonesia, los precios de utilidad están aumentando y los precios de autenticación están disminuyendo.
- Meta está refinando su definición de utilidad, basándose en la participación y el sentimiento de los usuarios, trasladando así casos de uso específicos hacia y desde la categoría de utilidad. Consulta la nueva [definición de plantilla de utilidad](https://developers.facebook.com/docs/whatsapp/pricing/updates-to-pricing#updates-to-template-category-guidelines) de Meta.

Para la mayoría de los clientes, estas actualizaciones entrarán en vigor automáticamente el 1 de julio.

## Próximos cambios en los precios de WhatsApp en julio de 2025 {#upcoming-whatsapp-pricing-changes-in-july-2025}

*Última actualización: 12 de marzo de 2025 (Publicado originalmente el 13 de diciembre de 2024)*

WhatsApp está realizando dos actualizaciones más en sus precios a partir del 1 de julio de 2025. Braze actualizará nuestros precios para reflejar estos cambios en la misma fecha. A continuación encontrarás un resumen de los cambios y las mejores prácticas para tenerlos en cuenta.

### Actualización 1: Los precios de WhatsApp pasarán a un modelo "por mensaje" en lugar de un modelo "por conversación". {#update-1-whatsapp-pricing-will-shift-to-a-per-message-model-instead-of-a-per-conversation-model}

**Las tarifas "por mensaje" serán las mismas que las tarifas actuales "por conversación".**

#### ¿Por qué están haciendo este cambio? {#why-are-they-making-this-change}

Meta está cambiando a un modelo "por mensaje" para ayudar a las marcas a simplificar los cálculos del ROI or retorno de la inversión or retorno de la inversión (ROI or retorno de la inversión). Este cambio también facilitará que las marcas realicen comparaciones directas de ROI or retorno de la inversión con otros canales que se cobran por mensaje.

#### ¿Cómo afectará esto a mi uso actual de WhatsApp? {#how-will-this-affect-my-current-whatsapp-usage}

- Las conversaciones actuales que se envían con una plantilla de mensaje en la ventana de 24 horas no se verán afectadas.
- **Las conversaciones actuales que se envían con dos o más plantillas de mensaje del _mismo tipo_ en la ventana de 24 horas aumentarán de costo.** Por ejemplo, enviar dos plantillas de marketing en el período de 24 horas tendrá el doble de costo porque se te cobrará por plantilla de mensaje.

| Escenario de ejemplo | Precios antes de abril de 2025 | Precios después de abril de 2025 |
| --- | --- | --- |
| La marca envía una plantilla de mensaje de marketing en la ventana de 24 horas | Cobro por una conversación de marketing | Cobro por un mensaje de marketing |
| La marca envía dos plantillas de mensaje de marketing en la ventana de 24 horas | Cobro por una conversación de marketing | Cobro por dos mensajes de marketing |
| La marca envía una plantilla de mensaje de utilidad en la ventana de 24 horas | Cobro por una conversación de utilidad | Cobro por un mensaje de utilidad |
| La marca envía dos plantillas de mensaje de utilidad en la ventana de 24 horas | Cobro por una conversación de utilidad | Cobro por dos mensajes de utilidad |
| La marca envía una plantilla de mensaje de marketing y una plantilla de mensaje de utilidad en la ventana de 24 horas | Cobro por una conversación de marketing y una conversación de utilidad | Cobro por un mensaje de marketing y un mensaje de utilidad |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Esta actualización se aplica a las plantillas de marketing, utilidad y autenticación. Las conversaciones de servicio son gratuitas desde el 1 de noviembre de 2024.

*Nota: Esta actualización estaba originalmente programada para el 1 de abril, el 1 de mayo y ahora el **1 de julio**.*

### Actualización 2: Las plantillas de utilidad enviadas durante una ventana de servicio al cliente de 24 horas serán gratuitas. {#update-2-utility-templates-sent-during-a-24-hour-customer-service-window-will-be-free-of-charge}

#### ¿Cómo funciona esto? {#how-does-this-work}

Se crea una [ventana de servicio al cliente de 24 horas](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows) cuando un usuario final envía un mensaje a una marca. Si tu marca responde con una plantilla de utilidad, no se realizará ningún cobro.

Las plantillas de utilidad enviadas fuera de una ventana de servicio al cliente de 24 horas (por ejemplo, plantillas de utilidad enviadas proactivamente por una marca para cosas como recordatorios de cuenta y actualizaciones del estado del pedido) seguirán siendo cobradas.

Recomendamos las siguientes mejores prácticas para tener en cuenta estos cambios y maximizar tu presupuesto de marketing en WhatsApp:

- Limita el envío de múltiples plantillas de mensaje del mismo tipo (sin una respuesta del usuario) en el período de 24 horas. No se te cobrará más de lo que se te cobraba anteriormente bajo el modelo "por conversación". Esta también es una mejor práctica para proporcionar experiencias de calidad a tus clientes y limitar la fatiga de mensajes.
- Usa la [mensajería de respuesta]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages) al responder a los mensajes de los usuarios finales. La mensajería de respuesta es gratuita.

| Escenario de ejemplo | Precios antes de abril de 2025 | Precios después de abril de 2025 |
| --- | --- | --- |
| - La marca envía una plantilla de marketing <br>- El usuario responde <br>- La marca responde con un mensaje de respuesta | Cobro por una conversación de marketing | Cobro por un mensaje de marketing |
| - El usuario envía un mensaje a la marca <br>- La marca responde con un mensaje de respuesta | Sin cargo <br> _Clasificada como conversación de servicio_ | Sin cargo <br> _Clasificada como conversación de servicio_ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Recomendamos las siguientes mejores prácticas para tener en cuenta estos cambios y maximizar tu presupuesto de marketing en WhatsApp:

- Limita el envío de múltiples plantillas de mensaje del mismo tipo (sin una respuesta del usuario) en el período de 24 horas. Esto evita que se te cobre más de lo que se te cobraba anteriormente bajo el modelo "por conversación". Esta también es una mejor práctica para proporcionar experiencias de calidad a tus clientes y limitar la fatiga de mensajes.
- Usa la [mensajería de respuesta]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages) al responder a los mensajes de los usuarios finales. La mensajería de respuesta es gratuita.

*Nota: Esta actualización estaba originalmente programada para el 1 de abril y ahora el **1 de julio**.*

## Cambios en los precios de WhatsApp de agosto de 2024 a noviembre de 2024 {#whatsapp-pricing-changes-from-august-2024-november-2024}

*Última actualización: 29 de octubre de 2024*

### Conversaciones de utilidad {#utility-conversations}

El 1 de agosto de 2024, Meta redujo las tarifas de las conversaciones de utilidad para animar a las marcas a facilitar más recorridos del cliente posteriores a la compra en la plataforma. Hemos trasladado estas reducciones de costos a tus derechos de créditos de mensajes o créditos de WhatsApp en proporciones iguales. Esta actualización entró en vigor el mismo día que la de Meta (1 de agosto).

#### ¿Qué son las conversaciones de utilidad? {#what-are-utility-conversations}

Las conversaciones de utilidad te permiten hacer seguimiento de acciones o solicitudes específicas del cliente. Los ejemplos incluyen confirmación de adhesión voluntaria, actualizaciones y confirmaciones de pedidos, actualizaciones o alertas de cuenta (por ejemplo, recordatorios de pago) o cuestionarios de opinión.

#### ¿Cómo puedes beneficiarte de esta actualización? {#how-can-you-benefit-from-this-update}

Te animamos a aprovechar esta actualización utilizando WhatsApp para la mensajería transaccional. También puedes considerar trasladar algunos de tus mensajes servicio de mensajes cortos transaccionales a WhatsApp si tiene sentido para tu marca (en función del alcance de tu audiencia y la participación en cada canal). Por ejemplo, esta puede ser una buena opción para clientes en Asia, América Latina y Europa, donde WhatsApp es un canal muy utilizado.

### Conversaciones de marketing {#marketing-conversations}

El 1 de octubre de 2024, Meta redujo los precios de las conversaciones de marketing en el Reino Unido en un 25 % para reflejar la demanda actual. Hemos trasladado estas reducciones de costos a tus derechos de créditos de mensajes o créditos de WhatsApp en proporciones iguales. Esta actualización entró en vigor el mismo día que la de Meta (1 de octubre).

#### ¿Qué son las conversaciones de marketing? {#what-are-marketing-conversations}

Las conversaciones de marketing te permiten alcanzar una amplia gama de objetivos, desde generar conciencia de marca hasta impulsar ventas y reorientar clientes. Los ejemplos incluyen anuncios de nuevos productos, promociones/ofertas segmentadas y campañas de abandono del carrito de compras.

### Conversaciones de servicio {#service-conversations}

El 1 de noviembre de 2024, todas las conversaciones de servicio son gratuitas. Las conversaciones de servicio ya no consumirán derechos de créditos de mensajes o créditos de WhatsApp. Este cambio entrará en vigor el mismo día que el de Meta (1 de noviembre).

#### ¿Qué son las conversaciones de servicio? {#what-are-service-conversations}

Las conversaciones de servicio te permiten responder a las consultas de los clientes. Esto incluye las conversaciones iniciadas por un usuario final en las que la marca responde con un [mensaje de respuesta]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages) en lugar de un mensaje de plantilla.

#### ¿Cómo puedes beneficiarte de esta actualización?

Algunas conversaciones que anteriormente se cobraban como "servicio" ahora serán gratuitas. Estas incluyen:

- [Campaigns de respuesta no reconocida]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages), en las que un usuario final envía un mensaje que no se reconoce y la marca responde con un mensaje genérico utilizando [mensajería de respuesta]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages). Por ejemplo, un usuario final envía un mensaje sin una palabra clave y la marca responde con "No reconocemos tu mensaje, por favor contacta con el soporte al cliente".
- Conversaciones que comienzan cuando un usuario final envía a la marca una palabra clave promocionada y la marca responde utilizando un [mensaje de respuesta]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages). Los ejemplos comunes incluyen la adhesión voluntaria a la mensajería de WhatsApp o la participación en una promoción específica.

<br>

La información detallada sobre la reducción de las conversaciones de utilidad se encuentra en la siguiente sección:

| Región de facturación                      | Porcentaje de reducción de utilidad |
|--------------------------------------------|-------------------------------------|
| Argentina                                  | 16,7 %                              |
| Brasil                                     | 77,1 %                              |
| Chile                                      | 65,9 %                              |
| Colombia                                   | 97,6 %                              |
| Egipto                                     | 92,4 %                              |
| Francia                                    | 60,9 %                              |
| Alemania                                   | 35,5 %                              |
| India                                      | 66,7 %                              |
| Indonesia                                  | 0,0 %                               |
| Israel                                     | 71,8 %                              |
| Italia                                     | 28,6 %                              |
| Malasia                                    | 30,0 %                              |
| México                                     | 62,4 %                              |
| Países Bajos                               | 37,5 %                              |
| Nigeria                                    | 79,0 %                              |
| Norteamérica                               | 73,3 %                              |
| Otros                                      | 77,2 %                              |
| Pakistán                                   | 78,7 %                              |
| Perú                                       | 52,3 %                              |
| Resto de África                            | 61,9 %                              |
| Resto de Asia Pacífico                     | 66,7 %                              |
| Resto de Europa Central y del Este         | 43,0 %                              |
| Resto de América Latina                    | 77,1 %                              |
| Resto de Oriente Medio                     | 20,7 %                              |
| Resto de Europa Occidental                 | 28,6 %                              |
| Rusia                                      | 16,1 %                              |
| Arabia Saudita                             | 54,4 %                              |
| Sudáfrica                                  | 62,0 %                              |
| España                                     | 47,4 %                              |
| Turquía                                    | 43,0 %                              |
| Emiratos Árabes Unidos                     | 20,7 %                              |
| Reino Unido                                | 44,7 %                              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para comprender mejor cómo puedes aprovechar estas actualizaciones, contacta con tu CSM or administrador de éxito de cliente or administrador de éxito de cliente.