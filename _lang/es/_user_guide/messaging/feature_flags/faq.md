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

# Preguntas frecuentes

> Este artículo ofrece respuestas a algunas preguntas frecuentes sobre los conmutadores de características.

## Funcionalidad y soporte

### ¿En qué plataformas se admiten los conmutadores de características de Braze? {#platforms}

Braze admite conmutadores de características en las plataformas iOS, Android y Web con los siguientes requisitos de versión del SDK:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

¿Necesitas soporte en otras plataformas? Envía un correo electrónico a nuestro equipo: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

### ¿Cuánto esfuerzo implica implementar un conmutador de características? {#level-of-effort}

Un conmutador de características se puede crear e integrar en pocos minutos.

La mayor parte del esfuerzo estará relacionada con tu equipo de ingeniería construyendo la nueva característica que planeas lanzar. Pero cuando se trata de añadir un conmutador de características, es tan sencillo como una sentencia `IF`/`ELSE` en el código de tu aplicación o sitio web:

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

### ¿Cómo pueden beneficiar los conmutadores de características a los equipos de marketing? {#marketing-teams}

Los equipos de marketing pueden usar conmutadores de características para coordinar anuncios de productos (como correos electrónicos de lanzamiento de productos) cuando una característica solo está habilitada para un pequeño porcentaje de usuarios.

Por ejemplo, con los conmutadores de características de Braze, puedes lanzar un nuevo programa de fidelización de clientes al 10 % de los usuarios de tu aplicación, y enviar un correo electrónico, push u otra mensajería a ese mismo 10 % de usuarios habilitados usando el paso de conmutador de características de Canvas.

### ¿Cómo pueden beneficiar los conmutadores de características a los equipos de producto? {#product-teams}

Los equipos de producto pueden usar conmutadores de características para realizar lanzamientos graduales o lanzamientos suaves de nuevas características con el fin de monitorear indicadores clave de rendimiento y la retroalimentación de los clientes antes de ponerlas a disposición de todos los usuarios.

Los equipos de producto pueden usar las [propiedades de los conmutadores de características]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#properties) para rellenar contenido de forma remota en una aplicación, como vínculos profundos, texto, imágenes u otro contenido dinámico.

Usando el paso de conmutador de características de Canvas, los equipos de producto también pueden ejecutar una prueba A/B dividida para medir cómo una nueva característica afecta las tasas de conversión en comparación con los usuarios que tienen la característica deshabilitada.

### ¿Cómo pueden beneficiar los conmutadores de características a los equipos de ingeniería? {#engineering-teams}

Los equipos de ingeniería pueden usar conmutadores de características para reducir el riesgo inherente al lanzamiento de nuevas características y evitar tener que desplegar correcciones de código de forma apresurada en medio de la noche.

Al publicar código nuevo oculto detrás de un conmutador de características, tu equipo puede activar o desactivar la característica de forma remota desde el panel de Braze, evitando la demora de publicar código nuevo o esperar la aprobación de una actualización en la tienda de aplicaciones.

## Lanzamientos de características y segmentación

### ¿Se puede lanzar un conmutador de características solo a un grupo selecto de usuarios? {#target-users}

Sí, crea un segmento en Braze que se dirija a usuarios específicos&mdash;por dirección de correo electrónico, `user_id` o cualquier otro atributo en sus perfiles de usuario. Luego, despliega el conmutador de características para el 100 % de ese segmento.

### ¿Cómo afecta el ajuste del porcentaje de lanzamiento a los usuarios que previamente fueron asignados al grupo habilitado? {#random-buckets}

Los lanzamientos de conmutadores de características se mantienen consistentes para los usuarios entre dispositivos y sesiones.

- Cuando un conmutador de características se lanza al 10 % de usuarios aleatorios, ese 10 % permanecerá habilitado y persistirá durante toda la vida útil de ese conmutador de características.
- Si aumentas el lanzamiento del 10 % al 20 %, el mismo 10 % permanecerá habilitado, más un nuevo 10 % adicional de usuarios se añadirá al grupo habilitado.
- Si reduces el lanzamiento del 20 % al 10 %, solo el 10 % original de usuarios permanecerá habilitado.

Esta estrategia ayuda a garantizar que los usuarios vean una experiencia consistente en tu aplicación y no alternen de un lado a otro entre sesiones. Por supuesto, deshabilitar una característica al 0 % eliminará a todos los usuarios del conmutador de características, lo cual es útil si descubres un error o necesitas deshabilitar la característica por completo.

## Temas técnicos

### ¿Se pueden usar los conmutadores de características para controlar cuándo se inicializa el SDK de Braze? {#initialization}

No, el SDK debe inicializarse para descargar y sincronizar los conmutadores de características del usuario actual. Esto significa que no puedes usar conmutadores de características para limitar qué usuarios se crean o rastrean en Braze.

### ¿Con qué frecuencia actualiza el SDK los conmutadores de características? {#refresh-frequency}

Los conmutadores de características se actualizan al inicio de la sesión y al cambiar de usuario activo. Los conmutadores de características también se pueden actualizar manualmente usando el [método de actualización]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#refreshing) del SDK. Las actualizaciones de conmutadores de características tienen un límite de velocidad de una vez cada cinco minutos (sujeto a cambios).

Ten en cuenta que las buenas prácticas de datos recomiendan no actualizar los conmutadores de características con demasiada frecuencia (con posible limitación de velocidad si se hace así), por lo que es mejor actualizarlos solo antes de que un usuario interactúe con nuevas características o periódicamente en la aplicación si es necesario.

### ¿Están disponibles los conmutadores de características cuando un usuario está sin conexión? {#offline}

Sí, después de que los conmutadores de características se actualizan, se almacenan localmente en el dispositivo del usuario y se puede acceder a ellos sin conexión.

### ¿Qué sucede si los conmutadores de características se actualizan a mitad de sesión? {#listen-for-updates}

Los conmutadores de características pueden actualizarse a mitad de sesión. Hay escenarios en los que puedes querer actualizar tu aplicación si ciertas variables o tu configuración deben cambiar. Hay otros escenarios en los que puedes no querer actualizar tu aplicación, para evitar un cambio brusco en cómo se renderiza tu interfaz de usuario.

Para controlar esto, [escucha las actualizaciones]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#updates) de los conmutadores de características y determina si volver a renderizar tu aplicación en función de qué conmutadores de características han cambiado.

### ¿Por qué los usuarios de mi grupo de control global no reciben experimentos de conmutadores de características?

No puedes habilitar conmutadores de características para usuarios en tu [grupo de control global]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/). Esto significa que los usuarios en tu grupo de control global tampoco pueden formar parte de experimentos de conmutadores de características.

## ¿Tienes preguntas adicionales?

¿Tienes preguntas o comentarios? Envía un correo electrónico a nuestro equipo: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).