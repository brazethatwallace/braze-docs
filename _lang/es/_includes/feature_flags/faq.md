# Preguntas más frecuentes {#frequently-asked-questions}

> Este artículo responde a algunas preguntas frecuentes sobre las banderas de características.

## Funcionalidad y soporte {#functionality-and-support}

### ¿En qué plataformas se admiten los conmutadores de características de Braze? {#platforms}

Braze admite conmutadores de características en plataformas iOS, Android y Web con los siguientes requisitos de versión del SDK:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

¿Necesitas soporte en otras plataformas? Envía un correo electrónico a nuestro equipo: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

### ¿Cuál es el nivel de esfuerzo involucrado al implementar un conmutador de características? {#level-of-effort}

Un conmutador de características se puede crear e integrar en cuestión de minutos.

La mayor parte del esfuerzo estará relacionada con tu equipo de ingeniería construyendo la nueva característica que planeas lanzar. Pero en lo que respecta a añadir un conmutador de características, es tan sencillo como una sentencia `IF`/`ELSE` en el código de tu aplicación o sitio web:

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

### ¿Cómo pueden beneficiarse los equipos de marketing de los conmutadores de características? {#marketing-teams}

Los equipos de marketing pueden usar los conmutadores de características para coordinar anuncios de productos (como correos electrónicos de lanzamiento de productos) cuando una característica solo está habilitada para un pequeño porcentaje de usuarios.

Por ejemplo, con los conmutadores de características de Braze, puedes lanzar un nuevo programa de fidelización de clientes al 10 % de los usuarios en tu aplicación, y enviar un correo electrónico, push u otros mensajes a ese mismo 10 % de usuarios habilitados usando el paso de conmutador de características en Canvas.

### ¿Cómo pueden beneficiarse los equipos de producto de los conmutadores de características? {#product-teams}

Los equipos de producto pueden usar los conmutadores de características para realizar lanzamientos graduales o lanzamientos parciales de nuevas características con el fin de monitorizar indicadores clave de rendimiento y la retroalimentación de los clientes antes de ponerlas a disposición de todos los usuarios.

Los equipos de producto pueden usar las [propiedades de los conmutadores de características]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#properties) para rellenar contenido de forma remota en una aplicación, como vínculos profundos, texto, imágenes u otro contenido dinámico.

Usando el paso de conmutador de características en Canvas, los equipos de producto también pueden ejecutar una prueba A/B dividida para medir cómo una nueva característica afecta las tasas de conversión en comparación con los usuarios que tienen la característica deshabilitada.

### ¿Cómo pueden beneficiarse los equipos de ingeniería de los conmutadores de características? {#engineering-teams}

Los equipos de ingeniería pueden usar los conmutadores de características para reducir el riesgo inherente al lanzar nuevas características y evitar apresurarse a desplegar correcciones de código en mitad de la noche.

Al publicar código nuevo oculto detrás de un conmutador de características, tu equipo puede activar o desactivar la característica de forma remota desde el panel de Braze, evitando la demora de publicar nuevo código o esperar la aprobación de una actualización en la tienda de aplicaciones.

## Lanzamientos de características y segmentación {#feature-rollouts-and-targeting}

### ¿Se puede lanzar un conmutador de características solo para un grupo selecto de usuarios? {#target-users}

Sí, crea un Segment en Braze que se dirija a usuarios específicos, ya sea por dirección de correo electrónico, `user_id` o cualquier otro atributo en tus perfiles de usuario. Luego, despliega el conmutador de características para el 100% de ese Segment.

### ¿Cómo afecta el ajuste del porcentaje de lanzamiento a los usuarios que previamente fueron asignados al grupo habilitado? {#random-buckets}

Los lanzamientos de conmutadores de características se mantienen consistentes para los usuarios en todos los dispositivos y sesiones.

- Cuando un conmutador de características se lanza al 10% de usuarios aleatorios, ese 10% permanecerá habilitado y se mantendrá durante toda la vida útil de ese conmutador de características.
- Si aumentas el lanzamiento del 10% al 20%, el mismo 10% permanecerá habilitado, y un nuevo 10% adicional de usuarios se añadirá al grupo habilitado.
- Si reduces el lanzamiento del 20% al 10%, solo el 10% original de usuarios permanecerá habilitado.

Esta estrategia ayuda a garantizar que los usuarios vean una experiencia consistente en tu aplicación y no alternen de un lado a otro entre sesiones. Por supuesto, desactivar una característica al 0% eliminará a todos los usuarios del conmutador de características, lo cual es útil si descubres un error o necesitas desactivar la característica por completo.

## Temas técnicos {#technical-topics}

### ¿Se pueden usar los conmutadores de características para controlar cuándo se inicializa el SDK de Braze? {#initialization}

No, el SDK debe inicializarse para descargar y sincronizar los conmutadores de características del usuario actual. Esto significa que no puedes usar conmutadores de características para limitar qué usuarios se crean o rastrean en Braze.

### ¿Con qué frecuencia actualiza el SDK los conmutadores de características? {#refresh-frequency}

Los conmutadores de características se actualizan al inicio de la sesión y al cambiar de usuario activo. Los conmutadores de características también se pueden actualizar manualmente usando el [método de actualización]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#refreshing) del SDK. Las actualizaciones de los conmutadores de características tienen un límite de velocidad de una vez cada cinco minutos (sujeto a cambios).

Ten en cuenta que las buenas prácticas de datos recomiendan no actualizar los conmutadores de características con demasiada frecuencia (con posible limitación de velocidad si se hace así), por lo que lo mejor es actualizarlos solo antes de que un usuario interactúe con nuevas características o periódicamente en la aplicación si es necesario.

### ¿Están disponibles los conmutadores de características cuando un usuario no tiene conexión? {#offline}

Sí, después de que los conmutadores de características se actualizan, se almacenan localmente en el dispositivo del usuario y se puede acceder a ellos sin conexión.

### ¿Qué pasa si los conmutadores de características se actualizan a mitad de sesión? {#listen-for-updates}

Los conmutadores de características pueden actualizarse a mitad de sesión. Hay escenarios en los que quizás quieras actualizar tu aplicación si ciertas variables o tu configuración deben cambiar. Hay otros escenarios en los que quizás no quieras actualizar tu aplicación, para evitar un cambio brusco en cómo se renderiza tu interfaz de usuario.

Para controlar esto, [escucha las actualizaciones]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#updates) de los conmutadores de características y determina si volver a renderizar tu aplicación en función de qué conmutadores de características han cambiado.

### ¿Por qué los usuarios de mi grupo de control global no reciben experimentos de conmutadores de características? {#why-arent-users-in-my-global-control-group-receiving-feature-flags-experiments}

No puedes habilitar conmutadores de características para los usuarios de tu [grupo de control global]({{site.baseurl}}/user_guide/audience/global_control_group). Esto significa que los usuarios de tu grupo de control global tampoco pueden formar parte de experimentos de conmutadores de características.

## ¿Preguntas adicionales? {#additional-questions}

¿Tienes preguntas o comentarios? Envía un correo electrónico a nuestro equipo: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).