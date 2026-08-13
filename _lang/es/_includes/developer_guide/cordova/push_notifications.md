{% multi_lang_include developer_guide/prerequisites/cordova.md %} Después de integrar el SDK, la funcionalidad básica de notificaciones push se habilita de forma predeterminada. Para utilizar [notificaciones push enriquecidas]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=cordova) y [Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=cordova), tendrás que configurarlas individualmente. Para utilizar los mensajes push de iOS, también necesitas cargar un certificado push válido.

{% alert warning %}
Cada vez que añadas, elimines o actualices tus complementos de Cordova, Cordova sobrescribirá el archivo de bibliotecas en el proyecto Xcode de tu aplicación para iOS. Esto significa que tendrás que volver a configurar estas características cada vez que modifiques tus complementos de Cordova.
{% endalert %}

## Habilitar la vinculación en profundidad push {#enabling-push-deep-linking}

De forma predeterminada, el SDK de Braze para Cordova no gestiona automáticamente los vínculos profundos de las notificaciones push. Para habilitar la vinculación en profundidad push, sigue los pasos de configuración que se indican en [Vinculación en profundidad]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=cordova).
Para obtener más información sobre estas y otras opciones de configuración push, consulta [Configuraciones opcionales]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional).

## Desactivar las notificaciones push básicas (solo iOS) {#disabling-basic-push-notifications-ios-only}

Después de integrar el SDK de Braze para Cordova en iOS, la funcionalidad básica de notificaciones push se habilita de forma predeterminada. Para desactivar esta funcionalidad en tu aplicación iOS, añade lo siguiente a tu archivo `config.xml`. Para obtener más información, consulta [Configuraciones opcionales]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional).

```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
