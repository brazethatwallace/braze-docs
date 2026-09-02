---
nav_title: Preguntas frecuentes sobre la migración
article_title: Preguntas frecuentes sobre la migración del SDK or kit de desarrollo de software de iOS
platform: iOS
page_order: 12
description: "Esta página responde a las preguntas más frecuentes sobre la migración del SDK or kit de desarrollo de software de Appboy para iOS (Objective-C) al SDK or kit de desarrollo de software Swift de Braze."
noindex: true
---

# Preguntas frecuentes sobre la migración del SDK or kit de desarrollo de software de iOS {#ios-sdk-migration-faq}

> Esta página responde a las preguntas más frecuentes sobre la migración del SDK or kit de desarrollo de software de Appboy para iOS heredado (también conocido como el SDK or kit de desarrollo de software de Objective-C) al SDK or kit de desarrollo de software Swift de Braze.

{% multi_lang_include deprecations/objective-c.md %}

## Compatibilidad de versiones y fin de vida útil {#version-support-and-end-of-life}

### ¿El SDK or kit de desarrollo de software de Appboy para iOS 4.7.0 ha llegado al fin de vida útil? {#is-appboy-ios-sdk-470-end-of-life}

Sí, el SDK or kit de desarrollo de software de Appboy para iOS 4.7.0 (y todas las versiones 4.x) ha llegado al fin de vida útil. No se proporcionan correcciones de seguridad ni correcciones de errores críticos. Aunque la mensajería y los análisis siguen funcionando con normalidad, la versión 4.7.0 debe considerarse como no compatible desde el punto de vista de la seguridad.

### ¿Cuál es la versión mínima del SDK or kit de desarrollo de software de Swift compatible en producción? {#what-is-the-minimum-swift-sdk-version-for-production-support}

Las versiones principales actuales (16.x y posteriores) son el objetivo del soporte continuo, las correcciones de errores y las nuevas características. Es posible que las versiones secundarias anteriores no reciban mantenimiento continuo.

## Bibliotecas de compatibilidad {#compatibility-libraries}

### ¿BrazeKitCompat y BrazeUICompat son compatibles para uso en producción en Swift SDK or kit de desarrollo de software 17.x? {#are-brazekitcompat-and-brazeuicompat-supported-for-production-use-on-swift-sdk-17x}

Sí, `BrazeKitCompat` y `BrazeUICompat` son compatibles para uso en producción durante la migración. Están pensadas como un "paso intermedio" de migración mínima para ayudarte a pasar del SDK or kit de desarrollo de software de Appboy al Swift SDK or kit de desarrollo de software con cambios de código mínimos, no como un destino a largo plazo. Aunque cuentan con soporte formal y siguen recibiendo correcciones de errores, la intención es migrar eventualmente de estas bibliotecas de compatibilidad a las API modernas del Swift SDK or kit de desarrollo de software.

### ¿Cuándo se eliminarán BrazeKitCompat y BrazeUICompat? {#when-will-brazekitcompat-and-brazeuicompat-be-removed}

El equipo del Swift SDK or kit de desarrollo de software tiene planes de descontinuar la biblioteca `BrazeKitCompat`, pero aún no se ha anunciado un cronograma específico. Se recomienda planificar una migración completa a las API modernas del Swift SDK or kit de desarrollo de software (`BrazeKit`, `BrazeUI`) en lugar de depender de las bibliotecas de compatibilidad de forma indefinida.

## Inicialización diferida {#delayed-initialization}

### ¿Puedo retrasar la inicialización del SDK or kit de desarrollo de software hasta después del consentimiento del usuario? {#can-i-delay-sdk-initialization-until-after-user-consent}

Sí. El SDK or kit de desarrollo de software de Swift admite la inicialización diferida, lo cual es útil para aplicaciones que necesitan esperar el consentimiento del usuario antes de iniciar el SDK or kit de desarrollo de software. Llama a `Braze.prepareForDelayedInitialization()` (opcionalmente con un parámetro `analyticsBehavior`) de forma temprana en `application(_:didFinishLaunchingWithOptions:)`, y luego inicializa el SDK or kit de desarrollo de software más tarde llamando al inicializador estándar de Braze después de obtener el consentimiento.

Para una implementación detallada, consulta [Configurar la inicialización diferida]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift#swift_step-2-set-up-delayed-initialization-optional).

### ¿Cuál es la versión mínima del SDK or kit de desarrollo de software de Swift requerida para la inicialización diferida? {#what-is-the-minimum-swift-sdk-version-required-for-delayed-initialization}

El SDK or kit de desarrollo de software de Swift 11.2.0 es la versión mínima para la inicialización diferida. La robustez de push y vínculos profundos para la inicialización diferida se mejoró aún más en la versión 14.1.0. El SDK or kit de desarrollo de software de Swift 17.0.0 supera con creces ambos umbrales.

### ¿Qué sucede con los eventos recibidos antes de que se inicialice el SDK or kit de desarrollo de software? {#what-happens-to-events-received-before-the-sdk-is-initialized}

Cuando se inicializa el SDK or kit de desarrollo de software, los elementos en cola se procesan. Sin embargo, el comportamiento varía según el canal:

| Canal | Comportamiento previo a la inicialización |
|---------|----------------------------|
| Tokens de notificaciones push | En cola; procesados en la inicialización |
| Aperturas/análisis de push | En cola de forma predeterminada (configurable para descartarlos mediante `analyticsBehavior`) |
| Vínculos profundos | En cola; procesados en la inicialización |
| In-App Messages | No se almacenan en búfer antes de la inicialización; requieren que el SDK or kit de desarrollo de software esté en ejecución |
| Content Cards | No se almacenan en búfer antes de la inicialización; se sincronizan desde el servidor después de la inicialización |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
No se garantiza la entrega de In-App Messages y Content Cards recibidos antes de la inicialización. Asegúrate de que el SDK or kit de desarrollo de software esté inicializado antes de intentar mostrar estos canales.
{% endalert %}

## Paquetes de recursos e integración con SPM {#resource-bundles-and-spm-integration}

### ¿Por qué veo un error en tiempo de ejecución sobre `braze-swift-sdk_BrazeUI.bundle` faltante? {#why-am-i-seeing-a-runtime-error-about-missing-braze-swift-sdk_brazeuibundle}

Esto no es un error conocido del SDK or kit de desarrollo de software y probablemente se deba a una configuración incorrecta de la integración. A partir del Swift SDK or kit de desarrollo de software 12.0.0, los XCFrameworks estáticos incluyen los recursos directamente en lugar de depender de paquetes de recursos externos.

### ¿Cuáles son los requisitos de SPM/Xcode/archivo para la incorporación de recursos? {#what-are-the-spmxcodearchive-requirements-for-resource-embedding}

A partir del Swift SDK or kit de desarrollo de software 12.0.0, debes seleccionar **Embed & Sign** para los XCFrameworks de Braze en la configuración de tu proyecto de Xcode; esto aplica tanto para las variantes estáticas como dinámicas. Esta es la causa raíz más común de los errores de paquete faltante al archivar o publicar.

### ¿Cómo puedo anular los paquetes de recursos para sistemas de compilación no estándar? {#how-do-i-override-resource-bundles-for-non-standard-build-systems}

Para sistemas de compilación no estándar (Tuist, Bazel, Buck, CI), usa las API de anulación aprobadas:

- `BrazeKit.overrideResourcesBundle` (nota el plural "Resources")
- `BrazeUI.overrideResourcesBundle` (nota el plural "Resources")

El singular `overrideResourceBundle` fue descontinuado en el Swift SDK or kit de desarrollo de software 8.1.0 y no debe usarse.

## Identidad de usuario y tokens de notificaciones push {#user-identity-and-push-tokens}

### ¿Existe una lista de verificación para preservar perfiles, asociaciones de dispositivos y tokens de notificaciones push? {#is-there-a-validation-checklist-for-preserving-profiles-device-associations-and-push-tokens}

No existe una lista de verificación oficial específica para migraciones en la documentación. Te recomendamos que realices los siguientes pasos de validación:

1. Confirma que `registerDeviceToken` o la automatización de push esté configurada correctamente después de la migración.
2. Verifica los recuentos de usuarios registrados para push en el panel antes y después del despliegue.
3. Comprueba de forma puntual algunos ID externos específicos para confirmar que las asociaciones de dispositivos permanecen intactas.

### ¿`changeUser` garantiza que los tokens de notificaciones push sigan al nuevo usuario? {#does-changeuser-guarantee-that-push-tokens-follow-the-new-user}

No existe una garantía explícita documentada por escrito. Sin embargo, la intención del diseño es que los tokens de notificaciones push sigan al dispositivo, no al usuario. Llamar a `changeUser` debería reasociar el token de dispositivo existente con el nuevo perfil de usuario. Deberías probar `changeUser`, verificar en el panel y confirmar que el token aparece en el nuevo perfil antes de un despliegue masivo.