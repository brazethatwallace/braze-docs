---
nav_title: Referencias y aplicaciones de ejemplo
article_title: "Referencias, repositorios y aplicaciones de ejemplo de Braze SDK"
page_order: 5.5
description: "Esta es una lista de documentación de referencia, repositorios GitHub y aplicaciones de ejemplo pertenecientes a cada SDK de Braze."
toc_headers: h2
---

# Referencias, repositorios y aplicaciones de ejemplo {#references-repositories-and-sample-apps}

> Esta es una lista de documentación de referencia, repositorios GitHub y aplicaciones de ejemplo pertenecientes a cada SDK de Braze. La documentación de referencia de un SDK detalla las clases, tipos, funciones y variables disponibles. El repositorio GitHub proporciona información sobre las declaraciones de funciones y atributos de ese SDK, los cambios en el código y el versionado. Cada repositorio también incluye aplicaciones de ejemplo totalmente compilables que puedes utilizar para probar las características de Braze o implementar junto con tus propias aplicaciones.

Para ver el contenido del README del repositorio reflejado en la documentación, consulta [Guías de repositorios]({{site.baseurl}}/developer_guide/sdk_repository_guides).

## Lista de recursos {#list-of-resources}

{% alert note %}
Actualmente, algunos SDK no cuentan con documentación de referencia dedicada, pero estamos trabajando activamente en ello.
{% endalert %}

| Plataforma        | Referencia                                                                                                                                    | Repositorio                                                                 | Aplicación de ejemplo                                                                |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| SDK de Android       | [Documentación de referencia](https://braze-inc.github.io/braze-android-sdk/kdoc/index.html)                                                                           | [Repositorio de GitHub](https://github.com/braze-inc/braze-android-sdk)      | [Aplicación de ejemplo](https://github.com/braze-inc/braze-android-sdk/tree/master/samples)      |
| SDK de Swift         | [Documentación de referencia](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze)                                                                | [Repositorio de GitHub](https://github.com/braze-inc/braze-swift-sdk)            | [Aplicación de ejemplo](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)            |
| SDK Web           | [Documentación de referencia](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)                                                               | [Repositorio de GitHub](https://github.com/braze-inc/braze-web-sdk)              | [Aplicación de ejemplo](https://github.com/braze-inc/braze-web-sdk/tree/master/sample-builds)              |
| SDK de Javascript           | [Documentación de referencia](https://braze-inc.github.io/braze-javascript-sdk/)                                                               | [Repositorio de GitHub](https://github.com/braze-inc/braze-javascript-sdk/tree/main)              | N/A              |
| SDK de Cordova       | [Archivo de declaración](https://github.com/braze-inc/braze-cordova-sdk/blob/master/www/BrazePlugin.js)                                      | [Repositorio de GitHub](https://github.com/braze-inc/braze-cordova-sdk)      | [Aplicación de ejemplo](https://github.com/braze-inc/braze-cordova-sdk/tree/master/sample-project)      |
| SDK de Flutter       | [Documentación de referencia](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/)                                                   | [Repositorio de GitHub](https://github.com/braze-inc/braze-flutter-sdk)      | [Aplicación de ejemplo](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example)      |
| SDK de React Native  | [Documentación de referencia](https://braze-inc.github.io/braze-react-native-sdk/)                                                                   | [Repositorio de GitHub](https://github.com/braze-inc/braze-react-native-sdk) | [Aplicación de ejemplo](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject) |
| SDK de Vega          | [Documentación de referencia](https://braze-inc.github.io/braze-vega-sdk/)                                                                           | [Repositorio de GitHub](https://github.com/braze-inc/braze-vega-sdk)         | N/A                                                                                       |
| SDK de Roku          | N/A                                                                                                                                                         | [Repositorio de GitHub](https://github.com/braze-inc/braze-roku-sdk)            | [Aplicación de ejemplo](https://github.com/braze-inc/braze-roku-sdk/tree/main/torchietv)            |
| SDK de Unity         | [Archivo de declaración](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs)     | [Repositorio de GitHub](https://github.com/braze-inc/braze-unity-sdk)          | [Aplicación de ejemplo](https://github.com/braze-inc/braze-unity-sdk/tree/master/unity-samples)          |
| SDK .NET MAUI (anteriormente Xamarin)      | N/A                                                                                                                                                         | [Repositorio de GitHub](https://github.com/braze-inc/braze-xamarin-sdk)      | [Aplicación de ejemplo](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples)      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Lista de recursos" }

## Creación de una aplicación de muestra {#building-a-sample-app}

{% tabs %}
{% tab android %}
### Creación de "Droidboy" {#building-droidboy}

Nuestra aplicación de prueba dentro del [repositorio de GitHub del SDK de Android](https://github.com/braze-inc/braze-android-sdk) se llama Droidboy. Sigue estas instrucciones para crear una copia completamente funcional junto a tu proyecto.

1. Crea un nuevo [espacio de trabajo]({{site.baseurl}}/user_guide/get_started/workspaces) y anota la clave identificadora de la API de Braze.<br><br>
2. Copia tu ID de remitente de FCM y la clave identificadora de la API de Braze en los lugares correspondientes dentro de `/droidboy/res/values/braze.xml` (entre las etiquetas de las cadenas denominadas `com_braze_push_fcm_sender_id` y `com_braze_api_key`, respectivamente).<br><br>
3. Copia tu clave de servidor de FCM y el ID de servidor en la configuración de tu espacio de trabajo en **Administrar configuración**.<br><br>
4. Para ensamblar el APK de Droidboy, ejecuta `./gradlew assemble` dentro del directorio del SDK. Usa `gradlew.bat` en Windows.<br><br>
5. Para instalar automáticamente el APK de Droidboy en un dispositivo de prueba, ejecuta `./gradlew installDebug` dentro del directorio del SDK:

### Creación de "Hello Braze" {#building-hello-braze}

La aplicación de prueba Hello Braze muestra un caso de uso mínimo del SDK de Braze y, además, demuestra cómo integrar fácilmente el SDK de Braze en un proyecto Gradle.

1. Copia tu clave identificadora de la API desde la página **Administrar configuración** en tu archivo `braze.xml` en la carpeta `res/values`.
![Captura de pantalla relacionada con la creación de "Hello Braze".]({% image_buster /assets/img_archive/hello_appboy.png %})<br><br>
2. Para instalar la aplicación de muestra en un dispositivo o emulador, ejecuta el siguiente comando dentro del directorio del SDK:
```
./gradlew installDebug
```
Si no tienes tu variable `ANDROID_HOME` configurada correctamente o no tienes una carpeta `local.properties` con una carpeta `sdk.dir` válida, este plugin también instalará el SDK base por ti. Consulta el [repositorio del plugin](https://github.com/JakeWharton/sdk-manager-plugin) para más información.

Para más información sobre el sistema de compilación del SDK de Android, consulta el [README del repositorio de GitHub](https://github.com/braze-inc/braze-android-sdk/blob/master/README.md).
{% endtab %}

{% tab swift %}
### Creación de aplicaciones de prueba en Swift {#building-swift-test-apps}

Sigue estas instrucciones para compilar y ejecutar nuestras aplicaciones de prueba.

1. Crea un nuevo [espacio de trabajo]({{site.baseurl}}/user_guide/get_started/workspaces) y anota la clave de API del identificador de la aplicación y el endpoint.
2. Según tu método de integración (Swift Package Administrador, CocoaPods, manual), selecciona el archivo `xcodeproj` correspondiente para abrir.
3. Coloca tu clave de API y tu endpoint en el campo correspondiente del archivo `Credentials`.
{% endtab %}
{% endtabs %}

{% alert note %}
Mientras realizas pruebas de calidad en tu integración de SDK, usa el [Depurador del SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) para solucionar problemas sin activar el registro detallado en tu aplicación.
{% endalert %}