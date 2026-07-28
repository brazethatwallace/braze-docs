---
page_order: 0
nav_title: Inicio
article_title: Partners tecnológicos
alias: /partners/partners/
layout: dev_guide
search_tag: Partner
description: "Explora los partners tecnológicos de Braze (Alloys) por categoría. Encuentra documentación de integración para personalización, orquestación, datos, eCommerce, Audience Sync y más."

guide_top_header: "Partners tecnológicos"
guide_top_text: "Te damos la bienvenida a la documentación de Braze Alloys, nuestros partners tecnológicos. Explora las categorías de partners para encontrar guías de integración técnica.<br><br>Para ver una lista completa de todos los partners tecnológicos de Braze con opciones de búsqueda y filtrado, visita el <a href='https://marketplace.braze.com/t/type/technology-partner'>Braze Marketplace</a>. ¿Quieres unirte a nuestra comunidad de clientes que usan Braze para modernizar su experiencia del cliente? Consulta nuestro <a href='https://brazefirebrands.splashthat.com/'>Programa Customer Champions</a>."

guide_featured_title: "Categorías de partners"
guide_featured_list:
  - name: Personalización de mensajes
    link: /docs/partners/message_personalization
    image: /assets/img/braze_icons/magic-wand-02.svg
  - name: Orquestación de mensajes
    link: /docs/partners/message_orchestration
    image: /assets/img/braze_icons/send-01.svg
  - name: Datos y análisis
    link: /docs/partners/data_and_analytics
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: Canvas Audience Sync
    link: /docs/partners/canvas_audience_sync
    image: /assets/img/braze_icons/refresh-ccw-02.svg
  - name: eCommerce
    link: /docs/partners/ecommerce
    image: /assets/img/braze_icons/shopping-cart-03.svg
  - name: Canales adicionales y extensiones
    link: /docs/partners/additional_channels_and_extensions
    image: /assets/img/braze_icons/puzzle-piece-01.svg
  - name: Proveedores de modelos de IA
    link: /docs/partners/ai_model_providers
    image: /assets/img/braze_icons/stars-01.svg
---

## Solución de problemas de conexiones con partners {#troubleshooting-partner-connections}

Si la integración requiere configuración del lado de Braze, inicia sesión en tu panel de Braze y ve a **Integraciones de socios** > **Partners tecnológicos**.

{% alert note %}
Las integraciones que son completamente propiedad del partner pueden no aparecer aquí. Consulta la documentación específica del partner para verificar la propiedad de la integración y los pasos de configuración.
{% endalert %}

Si ves **Credenciales no válidas** para un partner en Braze pero la integración parece correcta en el panel de ese partner, desconecta y vuelve a conectar la integración en la página de partners tecnológicos y confirma las claves de API, los tokens de OAuth y los permisos del lado del partner.

Algunos paneles externos (por ejemplo, herramientas de capacidad de entrega o monitoreo de buzón de entrada) pueden mostrar un estado de conexión o verificación diferente al de la página de partners tecnológicos de Braze. Usa el mosaico del partner en Braze para ver el estado de conexión en el que Braze se basa para la sincronización y el envío.