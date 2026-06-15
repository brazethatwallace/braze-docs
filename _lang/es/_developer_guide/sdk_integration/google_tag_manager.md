---
nav_title: Google Tag Manager
article_title: Google Tag Manager con el SDK de Braze
platform:
  - Android
  - FireOS
  - Swift
page_order: 1.1
description: "Aprende a inicializar el SDK de Braze utilizando métodos como la inicialización en tiempo de ejecución, la inicialización diferida o Google Tag Manager."

---

# Google Tag Manager con el SDK de Braze {#google-tag-manager-with-the-braze-sdk}

> Aprende a utilizar [Google Tag Manager (GTM)](https://developers.google.com/tag-platform/tag-manager) con el SDK de Braze, para que puedas controlar de forma remota el seguimiento de eventos y las actualizaciones de atributos de usuario de Braze sin necesidad de realizar cambios en el código ni lanzar nuevas versiones de la aplicación.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/google_tag_manager.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/google_tag_manager.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/google_tag_manager.md %}
{% endsdktab %}
{% endsdktabs %}

## Solución de problemas {#troubleshooting}

Si Braze no se inicializa o los eventos no aparecen como se esperaba, confirma que tu contenedor de GTM está publicado, que los desencadenantes y el orden de activación de las etiquetas están alineados con el [ciclo de vida y la estrategia de inicialización]({{site.baseurl}}/developer_guide/sdk_integration/) de tu SDK, y que los dispositivos de prueba no están bloqueando los puntos de conexión de Braze.

Para fallos de inicialización, verifica que la etiqueta de Braze o el proveedor de etiquetas personalizado reciba el `actionType` y los parámetros esperados (consulta las pestañas de Android, Swift y Web en esta página). Para habilitar el registro detallado mientras validas los eventos activados por GTM, activa el registro de depuración del SDK de tu plataforma como se describe en las guías de integración de plataforma enlazadas desde esas pestañas.