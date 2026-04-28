Antes de crear plantillas de WhatsApp, debes completar la [configuración de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/) y tener:
- Una cuenta de WhatsApp Business (WABA) activa conectada a Braze
- Grupos de suscripción apropiados configurados en tu WABA
- Activos multimedia (imágenes o videos) listos para cargar
- Permisos de Braze para usuarios no administradores
    - Para que los usuarios creen nuevas plantillas en el constructor de plantillas:
        - "View WhatsApp Message Templates"
        - "Edit WhatsApp Message Templates"
    - Para que los usuarios redacten Campaigns o Canvas con plantillas de carrusel:
        - "View WhatsApp Message Templates"
- Conocimiento de plantillas Liquid (opcional, para contenido dinámico)

{% alert important %}
Todos los números de teléfono y grupos de suscripción dentro de la misma cuenta de WhatsApp Business (WABA) comparten plantillas. Si tienes múltiples grupos de suscripción dentro de una WABA, todos pueden acceder a las mismas plantillas de carrusel; sin embargo, las plantillas no se comparten entre diferentes WABAs.
{% endalert %}