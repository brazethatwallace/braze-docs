---
page_order: 6
nav_title: Avisos de push suave
article_title: Avisos de push suave para Web
description: "Aprende a configurar avisos de push suave para el SDK or kit de desarrollo de software Web de Braze antes del aviso nativo de permiso de notificación del navegador."
channel:
  - push notifications
---

# Avisos de push suave para Web {#soft-push-prompts-for-web}

> Los avisos de push suave son mensajes personalizados que se muestran antes del aviso nativo de permiso de notificación del navegador. Explican por qué los usuarios deberían habilitar las notificaciones push y pueden mejorar las tasas de adhesión voluntaria en comparación con mostrar el aviso del sistema en la primera visita. Esta guía cubre cómo implementar avisos de push suave con el SDK or kit de desarrollo de software Web de Braze, incluyendo cuándo desencadenar el aviso, cómo personalizar el contenido del mensaje y las mejores prácticas para programar la solicitud después de que los usuarios entiendan el valor del push.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/push_notifications/soft_push_prompts.md %}
{% endsdktab %}
{% endsdktabs %}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Qué es un aviso de push suave? {#what-is-a-soft-push-prompt}

Un aviso de push suave es un mensaje personalizado dentro de la aplicación o en el sitio que se muestra antes del diálogo nativo de permiso de notificación del navegador. Explica el valor del push para que los usuarios tengan más probabilidades de aceptar cuando aparezca el aviso del sistema.

### ¿Cuándo debo mostrar un aviso de push suave? {#when-should-i-show-a-soft-push-prompt}

Muestra un aviso de push suave después de que los usuarios entiendan el valor de tu producto, por ejemplo, después de la incorporación o de una acción significativa dentro de la aplicación, no en la primera carga de página. Consulta los pasos del SDK or kit de desarrollo de software Web en esta guía para obtener detalles de implementación.