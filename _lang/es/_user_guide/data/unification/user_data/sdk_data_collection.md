---
nav_title: Recopilación de datos del SDK
article_title: Recopilación de datos del SDK
page_order: 1
page_type: reference
description: "Este artículo de referencia aborda los datos que recopila el SDK a través de una integración personalizada, una integración recopilada automáticamente y una integración mínima."

---

# Recopilación de datos del SDK {#sdk-data-collection}

> Cuando integras el SDK de Braze con tu aplicación o sitio, Braze recopila automáticamente determinados tipos de datos. Algunos de estos datos son esenciales para nuestros procesos y otros pueden activarse o desactivarse en función de tus necesidades. También puedes configurar Braze para que recopile tipos de datos adicionales para potenciar aún más tu segmentación y mensajería.

Braze está diseñado para permitir una recopilación de datos flexible, por lo que puedes integrar el SDK de Braze de las siguientes formas:

- **[Integración mínima](#minimum-integration):** Braze recopila automáticamente los datos necesarios para comunicarse con los servicios de Braze.
- **[Datos opcionales recopilados por defecto](#optional-data-collected-by-default):** Braze captura automáticamente algunos datos que son ampliamente útiles para la mayoría de tus casos de uso. Puedes optar por desactivar la recopilación automática de estos datos si no son esenciales para la comunicación con los servicios de Braze.
- **[Datos opcionales no recopilados por defecto](#data-not-collected-by-default):** Braze captura algunos datos que son útiles para determinados casos de uso y no habilita automáticamente la recopilación por motivos de cumplimiento general. Puedes optar por recopilar estos datos cuando se adapten a tus casos de uso.
- **[Integración personalizada](#personalized-integration):** Braze te da flexibilidad para recopilar datos además de los datos opcionales predeterminados.

## Integración mínima {#minimum-integration}

A continuación se enumeran los datos estrictamente necesarios que genera y recibe Braze cuando inicializas el SDK. Estos datos no son configurables y son esenciales en las funciones básicas de la plataforma. A excepción del inicio y el final de la sesión, el resto de datos registrados automáticamente no se tienen en cuenta para el uso de puntos de datos.

| Atributo | Descripción | Por qué se recopila |
| --------- | ----------- | ------------------ |
| App-Version-Name /<br> App-Version-Code | La versión más reciente de la aplicación | Este atributo se utiliza para enviar mensajes relacionados con la compatibilidad de la versión de la aplicación a los dispositivos correctos. Puede utilizarse para notificar a los usuarios interrupciones del servicio o errores. |
| País | País identificado mediante la geolocalización de la dirección IP. Si la geolocalización de la dirección IP no está disponible, se identifica mediante la [configuración regional del dispositivo](#optional-data-collected-by-default). El valor también podría ser el que los SDK establezcan directamente con `setCountry`, pero ten en cuenta que pasar un valor de atributo a través del SDK o la API registrará puntos de datos. **Una vez que el país se ha establecido manualmente (a través del método del SDK, la REST API o la carga de CSV), el SDK ya no actualiza automáticamente este valor.** | Este atributo se utiliza para dirigir mensajes en función de la ubicación. |
| ID del dispositivo | Identificador del dispositivo, una cadena generada aleatoriamente | Este atributo se utiliza para diferenciar los dispositivos de los usuarios y enviar mensajes al dispositivo correcto. |
| Sistema operativo y versión del sistema operativo | Dispositivo o navegador del que se informa actualmente y versión del dispositivo o navegador | Este atributo se utiliza para enviar mensajes solo a dispositivos compatibles. También puede utilizarse dentro de la segmentación para dirigirse a los usuarios con el fin de que actualicen las versiones de las aplicaciones. |
| Inicio y fin de la sesión | Cuando el usuario comienza a utilizar tu aplicación o sitio integrado | El SDK de Braze informa de los datos de sesión utilizados por el dashboard de Braze para calcular la interacción de los usuarios y otros análisis esenciales para comprender a tus usuarios. El momento exacto en que tu aplicación o sitio llama al inicio y al final de la sesión es configurable por un desarrollador ([Android]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android), [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift), [Web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web)). |
| Datos de interacción del mensaje SDK | Direct Opens de push, interacciones con mensajes dentro de la aplicación, interacciones con Content Cards | Este atributo se utiliza con fines de control de calidad, como comprobar que se ha recibido un mensaje y que el envío no está duplicado. |
| Versión del SDK | Versión actual del SDK | Este atributo se utiliza para enviar mensajes solo a dispositivos compatibles y evitar interrupciones del servicio. |
| ID y marca de tiempo de la sesión | Identificador de sesión, una cadena generada aleatoriamente y una marca de tiempo de sesión | Se utiliza para determinar si el usuario está iniciando una sesión nueva o ya existente y para determinar la reelegibilidad de los mensajes destinados a este usuario.<br><br>Algunos canales de mensajería, como los mensajes dentro de la aplicación y Content Cards, se sincronizan con el dispositivo al iniciar la sesión. Nuestro backend utilizará entonces los datos relacionados con la última vez que contactó con los servidores de Braze (que el dispositivo almacena y devuelve) para saber si el usuario es elegible para nuevos mensajes.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Minimum integration" }

### Métricas calculadas {#calculated-metrics}

Braze genera métricas calculadas sobre datos del SDK, datos de interacción de mensajes relacionados con mensajes no SDK e información derivada. Para mayor claridad, estos datos calculados no son rastreados por el SDK, sino generados por los servicios de Braze, y un perfil de usuario mostrará tanto los datos rastreados como los generados.

Las métricas calculadas incluyen métricas basadas en canales (enumeradas en el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/analytics/metrics_glossary/)) y los siguientes atributos.

| Atributo                                      | Descripción                                                          |
|------------------------------------------------|----------------------------------------------------------------------|
| Primera aplicación usada                                 | Hora                                                                 |
| Última aplicación utilizada                                  | Hora                                                                 |
| Recuento total de sesiones                            | Número                                                               |
| Tarjeta clicada                                   | Número                                                               |
| Último mensaje recibido                      | Hora                                                                 |
| Última Campaign de correo electrónico recibida                   | Hora                                                                 |
| Última Campaign push recibida                    | Hora                                                                 |
| Número de comentarios                       | Número                                                               |
| Número de sesiones en los últimos Y días          | Número y hora                                                      |
| Mensaje recibido de Campaign                 | Booleano. Este filtro se dirige a los usuarios en función de si han recibido una Campaign anterior. |
| Mensaje recibido de Campaign con etiqueta        | Booleano. Este filtro se dirige a los usuarios en función de si han recibido una Campaign que actualmente tiene una etiqueta. |
| Reorientar Campaign                              | Booleano. Este filtro se dirige a los usuarios en función de si han abierto o han hecho clic en un correo electrónico, push o mensaje dentro de la aplicación específico en el pasado. |
| Desinstalada                                    | Booleano y hora                                                     |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Calculated metrics" }

{% alert important %}
Si solo te interesa la integración mínima, y te integras con mParticle, Segment, Tealium o GTM, ten en cuenta lo siguiente:
- **Plataformas móviles**: Debes actualizar manualmente el código para estas configuraciones. mParticle y Segment no ofrecen una forma de hacerlo a través de su plataforma.
- **Web**: La integración de Braze debe realizarse de forma nativa para permitir la configuración de integración mínima. Los administradores de etiquetas no ofrecen la posibilidad de hacerlo a través de su plataforma.
{% endalert %}

## Datos opcionales recopilados por defecto {#optional-data-collected-by-default}

Además de los datos de integración mínima, Braze captura automáticamente los siguientes atributos cuando inicializas la integración del SDK. Puedes [optar por no recopilar]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection) estos atributos para permitir una integración mínima.

| Atributo               | Plataforma          | Descripción                                                                        | Por qué se recopila                                                                                                                                                      |
|-------------------------|-------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nombre del navegador            | Web               | Nombre del navegador                                                                | Este atributo se utiliza para enviar mensajes solo a navegadores compatibles. También puede utilizarse para la segmentación basada en el navegador.                                     |
| Configuración regional del dispositivo           | Android, iOS, Web | La configuración regional predeterminada del dispositivo                                                   | Este atributo se utiliza para traducir mensajes al idioma preferido del usuario.                                                                                            |
| Configuración regional más reciente del dispositivo           | Android, iOS, Web | La configuración regional predeterminada más reciente del dispositivo                                                   | Este atributo proviene de la configuración del dispositivo del usuario y se utiliza para traducir los mensajes al idioma preferido del usuario. Es independiente del atributo `Most Recent Location`.                                                                                            |
| Modelo de dispositivo            | Android, iOS      | El hardware específico del dispositivo                                                | Este atributo se utiliza para enviar mensajes solo a dispositivos compatibles. También puede utilizarse dentro de la segmentación.                                                 |
| Marca del dispositivo            | Android           | La marca del dispositivo (por ejemplo, Samsung)                                         | Este atributo se utiliza para enviar mensajes solo a dispositivos compatibles.                                                                                          |
| Operador inalámbrico del dispositivo | Android, iOS      | El operador de telefonía móvil                                                                 | Este atributo se utiliza opcionalmente para la orientación de mensajes.<br><br>**Nota:** Este campo ha quedado obsoleto a partir de iOS 16 y pasará por defecto a `--` en una futura versión de iOS. |
| Idioma                | Android, iOS, Web | Idioma del dispositivo o del navegador, tomado de la configuración regional del dispositivo.                                                           | Este atributo se utiliza para traducir mensajes al idioma preferido del usuario. Se basa en la configuración regional del dispositivo.                                                                                            |
| Configuración de notificaciones   | Android, iOS, Web | Si esta aplicación tiene activadas las notificaciones push.                                   | Este atributo se utiliza para habilitar las notificaciones push.                                                                                                                    |
| Resolución              | Android, iOS, Web | Resolución del dispositivo o navegador                                                          | Se utiliza opcionalmente para la orientación de mensajes basada en dispositivos. El formato de este valor es "`<width>`x`<height>`".                                                                 |
| Zona horaria               | Android, iOS, Web | Zona horaria del dispositivo o navegador                                                           | Este atributo se utiliza para enviar mensajes a la hora adecuada, según la zona horaria local de cada usuario.                                                   |
| Agente de usuario              | Web               | [Agente de usuario](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) | Este atributo se utiliza para enviar mensajes solo a dispositivos compatibles. También puede utilizarse dentro de la segmentación.                                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Optional data collected by default" }

Para saber más sobre el seguimiento de las propiedades a nivel de dispositivo (como operador inalámbrico del dispositivo, zona horaria, resolución y otros), consulta la documentación específica de la plataforma: [Android]({{site.baseurl}}/developer_guide/storage/?tab=android), [iOS]({{site.baseurl}}/developer_guide/storage/?tab=swift), [Web]({{site.baseurl}}/developer_guide/storage/#cookies).

## Datos no recopilados por defecto {#data-not-collected-by-default}

Por defecto, no se recopilan los siguientes atributos. Cada atributo debe integrarse manualmente.

| Atributo                  | Plataforma     | Descripción                                                                                                                                                                                                                                                                                                               | Por qué no se recopila                                                                                                                                                                                                                                                                 |
|----------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Seguimiento de anuncios del dispositivo habilitado | Android, iOS | En iOS:<br>[`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:))<br><br>En Android:<br>[`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) | Esta propiedad requiere permisos adicionales a nivel de aplicación, que deben ser concedidos por el integrador.                                                                                                                                                                                      |
| IDFA del dispositivo                | iOS          | Identificador de dispositivo para anunciantes                                                                                                                                                                                                                                                                                         | Esto requiere el marco de transparencia de seguimiento de anuncios, lo que provocará una revisión adicional de privacidad por parte de la App Store. Para más detalles, consulta [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)) |
| ID de publicidad de Google      | Android      | Identificador para publicidad en aplicaciones de Google Play                                                                                                                                                                                                                                                                        | Esto requiere que la aplicación recupere el GAID y se lo pase a Braze. Para más detalles, consulta [ID opcional de publicidad de Google]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration/#google-advertising-id).                                         |
| Ubicación más reciente | Android, iOS | Esta es la última ubicación GPS conocida del dispositivo del usuario. Se actualiza al inicio de la sesión y se almacena en el perfil del usuario. | Para ello, el usuario debe conceder permiso de ubicación a tu aplicación. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Data not collected by default" }

{% alert note %}
El SDK de Braze no almacena ninguna dirección IP localmente.
{% endalert %}

## Integración personalizada {#personalized-integration}

Para sacar el máximo partido de Braze, nuestros integradores de SDK a menudo implementan los SDK de Braze y registran [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#setting-custom-attributes), [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/#logging-custom-events) y [eventos de compra]({{site.baseurl}}/user_guide/data/activation/events/purchase_events/#logging-purchase-events) que son pertinentes para su negocio, además de los datos recopilados automáticamente.

Una integración personalizada permite una comunicación adaptada a la experiencia de tus usuarios.

{% alert important %}
Braze prohibirá o bloqueará a los usuarios con más de 5.000.000 de sesiones ("usuarios ficticios") y dejará de ingerir sus eventos del SDK. Para más información, consulta [Bloqueo de correo no deseado]({{site.baseurl}}/user_archival/#spam-blocking).
{% endalert %}