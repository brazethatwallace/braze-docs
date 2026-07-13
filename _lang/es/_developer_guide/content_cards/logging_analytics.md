---
nav_title: Registrar análisis
article_title: Registrar análisis
page_order: 1
description: "Este artículo explica cómo registrar manualmente impresiones, clics, descartes y gestionar el comportamiento de clic en tus Content Cards personalizadas."
toc_headers: "h2"

---

# Registrar análisis {#log-analytics}

{% multi_lang_include developer_guide/_shared/logging_analytics/content_cards.md %}

## Descartes únicos superiores a impresiones únicas {#unique-dismissals-higher-than-unique-impressions}

Si los *descartes únicos* superan a las *impresiones únicas*, tu integración personalizada de Content Cards registró descartes sin registrar impresiones para esas mismas tarjetas. La interfaz predeterminada de Content Cards de Braze registra ambos automáticamente, por lo que esta discrepancia solo aparece cuando utilizas una interfaz personalizada.

Registra una impresión cada vez que muestres una tarjeta, y registra un descarte cuando el usuario la descarte. Para los nombres de los métodos y ejemplos, consulta las secciones de plataforma a continuación.

## Análisis de Content Cards faltantes {#missing-content-cards-analytics}

Si las Content Cards aparecen correctamente en tu aplicación pero no recibes ningún análisis de forma consistente (impresiones, clics, etc.), es probable que se trate de un problema de integración de SDK.

- **Vistas personalizadas de Content Cards (Android, iOS, Web):** La interfaz predeterminada de Braze registra impresiones y clics automáticamente en todas las plataformas. Si estás utilizando una vista o implementación personalizada de Content Cards, debes llamar explícitamente a los métodos de registro apropiados dentro de tu aplicación. Consulta [Registrar análisis]({{site.baseurl}}/developer_guide/content_cards/logging_analytics) para tu plataforma. Para implementaciones Web personalizadas específicamente, asegúrate de que el SDK Web de Braze esté cargado, revisa la consola del navegador en busca de errores y verifica que se estén recibiendo los datos de las tarjetas.
- **Inicialización del SDK e identificación de usuarios:** Asegúrate de que el SDK esté completamente inicializado antes de mostrar las tarjetas. Los eventos se descartan silenciosamente (no se ponen en cola) si el SDK no está inicializado, está en modo de inicialización diferida o tiene el RGPD desactivado. El SDK sí registra análisis para usuarios anónimos, pero las métricas del panel como "impresiones diarias únicas" requieren una identidad de usuario resuelta, así que llama a `changeUser` antes de que se muestren las tarjetas siempre que sea posible.

## ID de Content Card {#content-card-id}

Cada envío de una Campaign a un destinatario genera un nuevo ID de Content Card. Si el mismo usuario recibe la Campaign de nuevo en un envío posterior, Braze asigna un nuevo ID. Haz referencia al `id` de la tarjeta al registrar impresiones, clics y descartes en implementaciones personalizadas.