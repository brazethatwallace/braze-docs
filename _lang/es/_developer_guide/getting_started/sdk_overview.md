---
nav_title: Visión general del SDK
article_title: Resumen del SDK para desarrolladores
description: "Este artículo de referencia sobre la incorporación proporciona un resumen técnico para desarrolladores del SDK de Braze. Habla de los análisis predeterminados de los que hace seguimiento el SDK."
page_order: 0
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/developer/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"}Resumen del SDK para desarrolladores {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecompathdevelopersdk-integration-basics-stylefloatrightwidth120pxborder0-classnoimgbordersdk-overview-for-developers}

> Antes de empezar a integrar los SDK de Braze, puede que te preguntes qué estás construyendo e integrando exactamente. Quizá tengas curiosidad por saber cómo puedes personalizar el SDK para adaptarlo aún más a tus necesidades. Este artículo puede ayudarte a responder a todas tus preguntas sobre el SDK.

¿Eres especialista en marketing y buscas un resumen básico del SDK? Echa un vistazo a nuestro [resumen para especialistas en marketing]({{site.baseurl}}/user_guide/get_started/sdk_overview).

En resumen, el SDK de Braze:
* Recoge y sincroniza los datos de usuario en un perfil de usuario consolidado
* Recoge automáticamente datos de sesión, información del dispositivo y tokens de notificaciones push
* Captura datos de interacción de marketing y datos personalizados específicos de tu empresa
* Potencia las notificaciones push, los mensajes dentro de la aplicación y los canales de mensajería de Content Cards

Mira el siguiente video para una breve introducción a los conceptos básicos de integración del SDK de Braze y su funcionalidad principal.

{% multi_lang_include video.html id="il152jayp0" source="wistia" %}

## Rendimiento de la aplicación {#app-performance}

Braze no debería tener ningún impacto negativo en el rendimiento de tu aplicación.

Los SDK de Braze tienen una huella muy pequeña. Cambiamos automáticamente la frecuencia con la que enviamos los datos de los usuarios dependiendo de la calidad de la red, además de permitir el control manual de la red. Agrupamos automáticamente las solicitudes de API del SDK para asegurar que los datos se registran rápidamente y se mantiene la máxima eficiencia de red. Por último, la cantidad de datos enviados desde el cliente a Braze en cada llamada a la API es extremadamente pequeña.

## Compatibilidad del SDK {#sdk-compatibility}

El SDK de Braze está diseñado para comportarse de manera muy eficiente y no interferir con otros SDK presentes en tu aplicación. Si experimentas algún problema que crees que podría deberse a una incompatibilidad con otro SDK, contacta con el soporte de Braze.

## Análisis predeterminados y gestión de sesiones {#default-analytics-and-session-handling}

Ciertos datos de usuario son recopilados automáticamente por nuestro SDK, por ejemplo, Primera vez que se usó la aplicación, Última vez que se usó la aplicación, Recuento total de sesiones, SO del dispositivo, etc. Si sigues nuestras guías de integración para implementar nuestros SDK, podrás aprovechar esta [recopilación de datos predeterminada]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection). Revisar esta lista puede ayudarte a evitar almacenar la misma información sobre los usuarios más de una vez. Con la excepción del inicio y el final de sesión, todos los demás datos rastreados automáticamente no cuentan para tu uso de puntos de datos.

{% alert note %}
Todas nuestras características son configurables, pero es buena idea implementar completamente el modelo de recopilación de datos predeterminado.

<br>Si es necesario para tu caso de uso, puedes [limitar la recopilación de ciertos datos](#blocking-data-collection) una vez completada la integración.
{% endalert %}

## Carga y descarga de datos {#data-upload-and-download}

El SDK de Braze almacena datos en caché (sesiones, eventos personalizados, etc.) y los carga periódicamente. Solo después de que los datos se hayan cargado se actualizarán los valores en el panel. El intervalo de carga tiene en cuenta el estado del dispositivo y se rige por la calidad de la conexión de red:

|Calidad de la conexión de red |    Intervalo de vaciado de datos|
|---|---|
|Excelente    |10 segundos|
|Buena    |30 segundos|
|Deficiente    |60 segundos|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Carga y descarga de datos" }

Si no hay conexión de red, los datos se almacenan en caché de forma local en el dispositivo hasta que se restablezca la conexión. Cuando se restablece la conexión, los datos se cargan a Braze.

Braze envía datos al SDK al inicio de una sesión en función de los Segments en los que se encuentra el usuario en el momento de la sesión. Los nuevos mensajes dentro de la aplicación no se actualizarán durante la sesión. Sin embargo, los datos del usuario durante la sesión se seguirán procesando continuamente a medida que se envían desde el cliente. Por ejemplo, un usuario inactivo (que no haya utilizado la aplicación en más de 7 días) seguirá recibiendo contenido dirigido a usuarios inactivos en su primera sesión de vuelta en la aplicación.

## Bloqueo de la recopilación de datos {#blocking-data-collection}

Es posible (aunque no se recomienda) bloquear la recopilación automática de ciertos datos de tu integración de SDK, o crear una lista de permitidos de los procesos que lo hacen.

No se recomienda bloquear la recopilación de datos porque eliminar los datos analíticos reduce la capacidad de personalización y segmentación de tu plataforma. Por ejemplo:

- Si decides no integrar completamente la ubicación en uno de los SDK, no podrás personalizar tus mensajes en función del idioma o la ubicación.
- Si decides no integrar la zona horaria, es posible que no puedas enviar mensajes dentro de la zona horaria del usuario.
- Si decides no integrar información visual específica del dispositivo, el contenido de los mensajes podría no estar optimizado para ese dispositivo.

Recomendamos encarecidamente integrar completamente los SDK para aprovechar al máximo las capacidades de nuestro producto.

{% tabs %}
{% tab Web SDK %}

Puedes simplemente no integrar ciertas partes del SDK, o utilizar [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) para un usuario. Este método sincronizará los datos registrados antes de que se llamara a `disableSDK()`, y hará que todas las llamadas posteriores al SDK Web de Braze para esta página y futuras cargas de página sean ignoradas. Si deseas reanudar la recopilación de datos en un momento posterior, puedes utilizar el método [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) en el futuro para reanudar la recopilación de datos. Puedes obtener más información sobre esto en nuestro artículo [Desactivación del seguimiento web]({{site.baseurl}}/developer_guide/analytics/managing_data_collection?sdktab=web).

{% endtab %}
{% tab Android SDK %}

Puedes utilizar [`setDeviceObjectAllowlist`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html?query=fun%20setDeviceObjectAllowlist(deviceObjectAllowlist:%20EnumSet%3CDeviceKey%3E):%20BrazeConfig.Builder) para configurar el SDK de modo que solo envíe un subconjunto de las claves o valores del objeto de dispositivo según una lista de permitidos. Esto debe habilitarse mediante [`setDeviceObjectAllowlistEnabled`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html?query=fun%20setDeviceObjectAllowlistEnabled(enabled:%20Boolean):%20BrazeConfig.Builder).

{% alert important %}
Una lista de permitidos vacía hará que **no** se envíe ningún dato de dispositivo a Braze.
{% endalert %}

{% endtab %}
{% tab Swift SDK %}

Puedes asignar un conjunto de campos elegibles a [`configuration.devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) en tu `Braze.Configuration` para especificar una lista de permitidos de los campos de dispositivo que el SDK recopila. La lista completa de campos se define en [`Braze.Configuration.DeviceProperty`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty). Para desactivar la recopilación de todos los campos de dispositivo, establece el valor de esta propiedad como un conjunto vacío (`[]`).

{% alert important %}
De forma predeterminada, el SDK Swift de Braze recopila todos los campos. Eliminar algunas propiedades del dispositivo puede deshabilitar funciones del SDK.
{% endalert %}

Para obtener más detalles de uso, consulta [Almacenamiento]({{site.baseurl}}/developer_guide/storage?tab=swift) en la documentación del SDK Swift.

{% endtab %}
{% endtabs %}

## ¿Qué versión del SDK estoy utilizando? {#what-version-of-the-sdk-am-i-on}

Puedes usar el panel para ver la versión del SDK de una aplicación en particular visitando **Configuración > Configuración de la aplicación**. La **versión del SDK en vivo** muestra la versión más alta del SDK de Braze utilizada por tu aplicación en vivo más reciente para al menos el 5% de tus usuarios.

![Una aplicación llamada Swifty en un espacio de trabajo. La versión del SDK en vivo es 6.6.0.]({% image_buster /assets/img/live-sdk-version.png %}){: style="max-width:80%"}

{% alert tip %}
Si tienes una aplicación iOS, puedes confirmar que estás utilizando el [SDK de Swift]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift) en lugar del antiguo [SDK de Objective-C para iOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview) si tu **versión del SDK en vivo** es igual o superior a 5.0.0, que fue la primera versión publicada del SDK de Swift.
{% endalert %}