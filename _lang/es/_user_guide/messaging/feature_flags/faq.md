---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes
page_order: 50
description: "Esta página ofrece respuestas a preguntas frecuentes sobre los conmutadores de características."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web
---

# Preguntas frecuentes {#frequently-asked-questions}

> Este artículo ofrece respuestas a algunas preguntas frecuentes sobre los conmutadores de características.

## Funcionalidad y soporte {#functionality-and-support}

### ¿En qué plataformas se admiten los conmutadores de características de Braze? {#platforms}

Braze admite conmutadores de características en las plataformas iOS, Android y Web con los siguientes requisitos de versión del SDK:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

¿Necesitas soporte en otras plataformas? Envía un correo electrónico a nuestro equipo: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

### ¿Cuál es el nivel de esfuerzo implicado en la implementación de un conmutador de características? {#level-of-effort}

Un conmutador de características se puede crear e integrar en unos minutos.

La mayor parte del esfuerzo estará relacionada con que tu equipo de ingeniería construya la nueva característica que planeas lanzar. Pero en lo que respecta a añadir un conmutador de características, es tan sencillo como una sentencia `IF`/`ELSE` en el código de tu aplicación o sitio web:

{% tabs %}
{% tab JavaScript %}

```javascript
import { getFeatureFlag } from "@braze/web-sdk";

if (getFeatureFlag("new_shopping_cart").enabled) {
    // Show the new homepage your team has built
}
else {
    // Show the old homepage
}
```

{% endtab %}
{% tab Java %}

```java
if (braze.getFeatureFlag("new_shopping_cart").getEnabled()) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
if (braze.getFeatureFlag("new_shopping_cart")?.enabled == true) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% endtabs %}

### ¿Cómo pueden los conmutadores de características beneficiar a los equipos de marketing? {#marketing-teams}

Los equipos de marketing pueden utilizar los conmutadores de características para coordinar los anuncios de productos (como los correos electrónicos de lanzamiento de productos) cuando una característica solo está habilitada para un pequeño porcentaje de usuarios.

Por ejemplo, con los conmutadores de características de Braze, puedes lanzar un nuevo programa de fidelización de clientes al 10 % de los usuarios en tu aplicación, y enviar un correo electrónico, push u otros mensajes a ese mismo 10 % de usuarios habilitados mediante el paso de conmutador de características en Canvas.

### ¿Cómo pueden los conmutadores de características beneficiar a los equipos de producto? {#product-teams}

Los equipos de producto pueden utilizar los conmutadores de características para realizar despliegues graduales o lanzamientos suaves de nuevas características con el fin de monitorizar indicadores clave de rendimiento y los comentarios de los clientes antes de ponerlas a disposición de todos los usuarios.

Los equipos de producto pueden usar las [propiedades de los conmutadores de características]({{site.baseurl}}/developer_guide/feature_flags/create#accessing-properties) para rellenar contenido de forma remota en una aplicación, como vínculos profundos, texto, imágenes u otro contenido dinámico.

Mediante el paso de conmutador de características en Canvas, los equipos de producto también pueden ejecutar una prueba A/B de división para medir cómo una nueva característica impacta en las tasas de conversión en comparación con los usuarios que tienen la característica deshabilitada.

### ¿Cómo pueden los conmutadores de características beneficiar a los equipos de ingeniería? {#engineering-teams}

Los equipos de ingeniería pueden utilizar los conmutadores de características para reducir el riesgo inherente al lanzamiento de nuevas características y evitar tener que desplegar correcciones de código de forma urgente en mitad de la noche.

Al lanzar nuevo código oculto detrás de un conmutador de características, tu equipo puede activar o desactivar la característica de forma remota desde el panel de Braze, evitando la demora de publicar nuevo código o esperar la aprobación de una actualización en la tienda de aplicaciones.

## Implementación de características y segmentación {#feature-rollouts-and-targeting}

### ¿Se puede implementar un conmutador de características solo para un grupo selecto de usuarios? {#target-users}

Sí, crea un Segment en Braze que se dirija a usuarios específicos, ya sea por dirección de correo electrónico, `user_id` o cualquier otro atributo en sus perfiles de usuario. Después, despliega el conmutador de características para el 100% de ese Segment.

### ¿Cómo afecta el ajuste del porcentaje de implementación a los usuarios que previamente fueron asignados al grupo habilitado? {#random-buckets}

Las implementaciones de conmutadores de características se mantienen consistentes para los usuarios en todos los dispositivos y sesiones.

- Cuando un conmutador de características se implementa para el 10% de usuarios aleatorios, ese 10% permanecerá habilitado y se mantendrá durante toda la vida útil de ese conmutador de características.
- Si aumentas la implementación del 10% al 20%, el mismo 10% permanecerá habilitado, y un 10% adicional de usuarios nuevos se añadirá al grupo habilitado.
- Si reduces la implementación del 20% al 10%, solo el 10% original de usuarios permanecerá habilitado.

Esta estrategia ayuda a garantizar que los usuarios vean una experiencia consistente en tu aplicación y no alternen entre estados de una sesión a otra. Por supuesto, desactivar una característica al 0% eliminará a todos los usuarios del conmutador de características, lo cual es útil si descubres un error o necesitas desactivar la característica por completo.

## Temas técnicos {#technical-topics}

### ¿Se pueden usar los conmutadores de características para controlar cuándo se inicializa el SDK de Braze? {#initialization}

No, el SDK debe inicializarse para descargar y sincronizar los conmutadores de características del usuario actual. Esto significa que no puedes usar los conmutadores de características para limitar qué usuarios se crean o rastrean en Braze.

### ¿Con qué frecuencia actualiza el SDK los conmutadores de características? {#refresh-frequency}

Los conmutadores de características se actualizan al inicio de la sesión y al cambiar de usuario activo. Los conmutadores de características también pueden actualizarse manualmente usando el [método de actualización]({{site.baseurl}}/developer_guide/feature_flags/create#refreshing) del SDK. Las actualizaciones de conmutadores de características están limitadas a una vez cada cinco minutos (sujeto a cambios).

Ten en cuenta que las buenas prácticas de datos recomiendan no actualizar los conmutadores de características demasiado rápido (con posible limitación de velocidad si se hace), por lo que es mejor actualizar solo antes de que un usuario interactúe con nuevas características o periódicamente en la aplicación si es necesario.

### ¿Los conmutadores de características están disponibles mientras un usuario está sin conexión? {#offline}

Sí, después de que los conmutadores de características se actualizan, se almacenan localmente en el dispositivo del usuario y se puede acceder a ellos sin conexión.

### ¿Qué pasa si los conmutadores de características se actualizan a mitad de sesión? {#listen-for-updates}

Los conmutadores de características pueden actualizarse a mitad de sesión. Hay escenarios en los que puedes querer actualizar tu aplicación si ciertas variables o tu configuración deben cambiar. Hay otros escenarios en los que puedes no querer actualizar tu aplicación, para evitar un cambio abrupto en cómo se renderiza tu interfaz.

Para controlar esto, [escucha las actualizaciones]({{site.baseurl}}/developer_guide/feature_flags/create#updates) de los conmutadores de características y determina si volver a renderizar tu aplicación en función de qué conmutadores de características han cambiado.

### ¿Por qué los usuarios de mi grupo de control global no reciben experimentos de conmutadores de características? {#why-arent-users-in-my-global-control-group-receiving-feature-flags-experiments}

No puedes habilitar conmutadores de características para los usuarios de tu [grupo de control global]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts). Esto significa que los usuarios de tu grupo de control global tampoco pueden ser parte de experimentos de conmutadores de características.

### ¿La identificación de destinatarios basada en correo electrónico es parte de los conmutadores de características de Braze? {#is-email-based-recipient-identification-part-of-braze-feature-flags}

No. Identificar destinatarios por correo electrónico cuando envías un mensaje no es parte del producto de conmutadores de características en esta página. Los conmutadores de características controlan experiencias dentro de la aplicación o en el sitio a través del SDK de Braze.

Los envíos de Campaigns y Canvas activados por API pueden incluir `email` en el [objeto de destinatarios]({{site.baseurl}}/api/objects_filters/recipient_object) en lugar de un `external_user_id`. Cuando usas `email`, incluye `prioritization` para que Braze pueda seleccionar el perfil de usuario coincidente. Esta opción de envío no está disponible en todos los espacios de trabajo.

Para la estructura de la solicitud, consulta [POST: Enviar Campaigns usando entrega activada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) y [POST: Enviar mensajes de Canvas usando entrega activada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).

## ¿Tienes más preguntas? {#additional-questions}

¿Tienes preguntas o comentarios? Envía un correo electrónico a nuestro equipo: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).