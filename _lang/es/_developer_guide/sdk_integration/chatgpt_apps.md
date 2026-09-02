---
page_order: 2.1
nav_title: Aplicaciones ChatGPT
article_title: Integra Braze con las aplicaciones ChatGPT
description: "Aprende a integrar Braze con las aplicaciones ChatGPT para habilitar análisis y registro de eventos en aplicaciones basadas en inteligencia artificial."
platform:
  - ChatGPT Apps
---

# Integra Braze con las aplicaciones ChatGPT {#integrate-braze-with-chatgpt-apps}

> Esta guía explica cómo integrar Braze con las aplicaciones ChatGPT para habilitar análisis y registro de eventos dentro de aplicaciones basadas en inteligencia artificial.

![Una tarjeta de contenido integrada en una aplicación ChatGPT.]({% image_buster /assets/img/chatgpt_app_integration.png %}){: style="float:right;max-width:30%;border:none;" }

## Resumen {#overview}

Las aplicaciones ChatGPT proporcionan una potente plataforma para crear aplicaciones conversacionales de IA. Al integrar Braze con tu aplicación ChatGPT, puedes seguir manteniendo el control de los datos propios en la era de la IA, incluyendo cómo:

- Realizar un seguimiento de la interacción y el comportamiento de los usuarios dentro de tu aplicación ChatGPT (por ejemplo, identificando qué preguntas o características de chat utilizan tus clientes).
- Segmentar y reorientar Campaigns de Braze basándote en patrones de interacción de IA (como el envío por correo electrónico a usuarios que hayan utilizado el chat más de tres veces por semana).

### Ventajas principales {#key-benefits}

- **Controla el recorrido del cliente:** Mientras los usuarios interactúan con tu marca a través de ChatGPT, tú mantienes la visibilidad de su comportamiento, preferencias y patrones de interacción. Estos datos se transfieren directamente a los perfiles de usuario de Braze, no solo a los análisis de la plataforma de IA.
- **Retargeting multiplataforma:** Realiza un seguimiento de las interacciones de los usuarios en tu aplicación ChatGPT y reoriéntalos a través de tus canales propios (correo electrónico, SMS, notificaciones push, mensajes dentro de la aplicación) con campañas personalizadas basadas en sus patrones de uso de la IA.
- **Devuelve contenido promocional 1:1 a las conversaciones de ChatGPT:** Entrega [mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages) de Braze, [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards) y mucho más directamente dentro de tu experiencia ChatGPT utilizando los componentes personalizados de la interfaz de usuario conversacional que tu equipo ha creado para tu aplicación.
- **Atribución de ingresos:** Realiza un seguimiento de las compras y conversiones que se originan en las interacciones con la aplicación ChatGPT.

<!-- ### Practical Use Cases

- **E-commerce**: Track product inquiries, cart additions, and purchases made through ChatGPT conversations
- **software como servicio (SaaS)**: Monitor feature requests, support interactions, and trial-to-paid conversions
- **Content/Media**: Understand what topics users are most interested in and create targeted content campaigns
- **SERVICIOS FINANCIEROS**: Track financial advice requests and product recommendations for compliance and optimization
- **Travel**: Monitor destination research, booking inquiries, and trip planning interactions

By integrating Braze with your ChatGPT App, you ensure that every AI interaction becomes a data point in your customer engagement strategy, not just a black box interaction on someone else's platform. -->

## Requisitos previos {#prerequisites}

Antes de integrar Braze con tu aplicación ChatGPT, debes disponer de lo siguiente:

- Una nueva aplicación web y una clave de API en tu espacio de trabajo de Braze
- Una [aplicación ChatGPT](https://openai.com/index/introducing-apps-in-chatgpt/) creada en la plataforma OpenAI ([aplicación de muestra de OpenAI](https://github.com/openai/openai-apps-sdk-examples))

{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}