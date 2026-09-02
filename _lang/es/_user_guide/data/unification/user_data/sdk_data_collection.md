---
nav_title: Recopilación de datos del SDK or kit de desarrollo de software
article_title: Recopilación de datos del SDK or kit de desarrollo de software
page_order: 1
page_type: reference
description: "Este artículo de referencia aborda los datos que recopila el SDK or kit de desarrollo de software a través de una integración personalizada, una integración recopilada automáticamente y una integración mínima."
---

# Recopilación de datos del SDK or kit de desarrollo de software {#sdk-data-collection}

> Cuando integras el SDK or kit de desarrollo de software de Braze con tu aplicación o sitio, Braze recopila automáticamente determinados tipos de datos. Algunos de estos datos son esenciales para nuestros procesos y otros pueden activarse o desactivarse en función de tus necesidades. También puedes configurar Braze para que recopile tipos de datos adicionales para potenciar aún más tu segmentación y mensajería.

Braze está diseñado para permitir una recopilación de datos flexible, por lo que puedes integrar el SDK or kit de desarrollo de software de Braze de las siguientes formas:

- **[Integración mínima](#minimum-integration):** Braze recopila automáticamente los datos necesarios para comunicarse con los servicios de Braze.
- **[Datos opcionales recopilados por defecto](#optional-data-collected-by-default):** Braze captura automáticamente algunos datos que son ampliamente útiles para la mayoría de tus casos de uso. Puedes optar por desactivar la recopilación automática de estos datos si no son esenciales para la comunicación con los servicios de Braze.
- **[Datos opcionales no recopilados por defecto](#data-not-collected-by-default):** Braze captura algunos datos que son útiles para determinados casos de uso y no habilita automáticamente la recopilación por motivos de cumplimiento general. Puedes optar por recopilar estos datos cuando se adapten a tus casos de uso.
- **[Integración personalizada](#personalized-integration):** Braze te da flexibilidad para recopilar datos además de los datos opcionales predeterminados.

## Integración mínima {#minimum-integration}

A continuación se enumeran los datos estrictamente necesarios generados y recibidos por Braze cuando inicializas el SDK or kit de desarrollo de software. Estos datos no son configurables y son esenciales en las funciones principales de la plataforma. Excepto el inicio y el fin de sesión, todos los demás datos rastreados automáticamente no cuentan para tu uso de punto de datos.

| Atributo | Descripción | Por qué se recopila |
| --------- | ----------- | ------------------ |
| App-Version-Name /<br> App-Version-Code | La versión más reciente de la aplicación | Este atributo se utiliza para enviar mensajes relacionados con la compatibilidad de la versión de la aplicación a los dispositivos correctos. Puede usarse para notificar a los usuarios sobre interrupciones del servicio o errores. |
| País | País identificado por geolocalización de la dirección IP. Si la geolocalización de la dirección IP no está disponible, se identifica por la [configuración regional del dispositivo](#optional-data-collected-by-default). El valor podría ser alternativamente lo que los SDK or kit de desarrollo de software establezcan directamente con `setCountry`, pero ten en cuenta que pasar un valor de atributo a través del SDK or kit de desarrollo de software o la API registrará puntos de datos. **Después de que el país se haya establecido manualmente (a través del método del SDK or kit de desarrollo de software, la REST or transferencia de estado representacional API o la carga de CSV), el SDK or kit de desarrollo de software ya no actualiza automáticamente este valor.** | Este atributo se utiliza para segmentar mensajes basándose en la ubicación. |
| ID de dispositivo | Identificador del dispositivo, una cadena generada aleatoriamente | Este atributo se utiliza para diferenciar los dispositivos de los usuarios y enviar mensajes al dispositivo correcto. |
| Sistema operativo y versión del SO | Dispositivo o navegador reportado actualmente y versión del dispositivo o navegador | Este atributo se utiliza para enviar mensajes únicamente a dispositivos compatibles. También puede usarse dentro de la segmentación para dirigirse a usuarios que deben actualizar versiones de la aplicación. |
| Inicio y fin de sesión | Cuando el usuario comienza a usar tu aplicación o sitio integrado | El SDK or kit de desarrollo de software de Braze reporta datos de sesión utilizados por el panel de Braze para calcular la participación de los usuarios y otros análisis esenciales para comprender a tus usuarios. El momento exacto en que tu aplicación o sitio llama al inicio y fin de sesión es configurable por un desarrollador ([Android]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=android), [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=swift), [Web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=web)). |
| Datos de interacción de mensajes del SDK or kit de desarrollo de software | Direct Opens de push, interacciones con mensajes dentro de la aplicación, interacciones con Content Cards | Este atributo se utiliza con fines de control de calidad, como verificar que un mensaje fue recibido y que el envío no está duplicado. |
| Versión del SDK or kit de desarrollo de software | Versión actual del SDK or kit de desarrollo de software | Este atributo se utiliza para enviar mensajes únicamente a dispositivos compatibles y evitar interrupciones del servicio. |
| ID de sesión y marca de tiempo de sesión | Identificador de sesión, una cadena generada aleatoriamente y marca de tiempo de sesión | Se utiliza para determinar si el usuario está iniciando una sesión nueva o existente y para determinar la reelegibilidad de mensajes destinados a este usuario.<br><br>Ciertos canales de mensajería como los mensajes dentro de la aplicación y las Content Cards se sincronizan con el dispositivo al inicio de la sesión. Nuestro backend utilizará entonces datos relacionados con la última vez que contactó a los servidores de Braze (que el dispositivo almacena y envía de vuelta) para saber si el usuario es elegible para nuevos mensajes.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Integración mínima" }

### Métricas calculadas {#calculated-metrics}

Braze genera métricas calculadas a partir de tres entradas: [datos rastreados por el SDK or kit de desarrollo de software](#minimum-integration) (por ejemplo, [inicio y fin de sesión]({{site.baseurl}}/developer_guide/analytics/tracking_sessions)), [datos de interacción de mensajes para canales que no son del SDK or kit de desarrollo de software]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) y [campos de informes derivados de Braze]({{site.baseurl}}/user_guide/analytics/metrics_glossary). Estos valores son generados por los servicios de Braze, por lo que un perfil de usuario puede incluir tanto datos rastreados por el SDK or kit de desarrollo de software como datos generados por Braze.

Las métricas calculadas incluyen métricas basadas en canales (listadas en el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/analytics/metrics_glossary)) y los siguientes atributos.

| Atributo | Descripción |
|------------------------------------------------|----------------------------------------------------------------------|
| Primera vez que usó la aplicación | Hora |
| Última vez que usó la aplicación | Hora |
| Recuento total de sesiones | Número |
| Tarjeta clicada | Número |
| Último mensaje recibido de cualquier tipo | Hora |
| Última Campaign de correo electrónico recibida | Hora |
| Última Campaign push recibida | Hora |
| Número de elementos de retroalimentación | Número |
| Número de sesiones en los últimos Y días | Número y hora |
| Mensaje recibido de Campaign | Booleano. Este filtro segmenta a los usuarios en función de si han recibido una Campaign anterior. |
| Mensaje recibido de Campaign con etiqueta | Booleano. Este filtro segmenta a los usuarios en función de si han recibido una Campaign que actualmente tiene una etiqueta. |
| Reorientar Campaign | Booleano. Este filtro segmenta a los usuarios en función de si han abierto o hecho clic en un correo electrónico, push o mensaje dentro de la aplicación específico en el pasado. |
| Desinstalado | Booleano y hora |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métricas calculadas" }

La integración mínima significa que solo recopilas los datos requeridos listados en [Integración mínima](#minimum-integration) y optas por no recopilar los [datos opcionales recopilados por defecto](#optional-data-collected-by-default) [bloqueando la recopilación de datos opcionales del SDK or kit de desarrollo de software]({{site.baseurl}}/developer_guide/getting_started/sdk_overview).

{% alert important %}
Si deseas una integración mínima y usas mParticle, Segment, Tealium o GTM, ten en cuenta lo siguiente:
- **Plataformas móviles**: Debes actualizar manualmente el código para estas configuraciones. mParticle y Segment no ofrecen una forma de hacer esto a través de su plataforma.
- **Web**: La integración de Braze debe hacerse de forma nativa para permitir la configuración de integración mínima. Los gestores de etiquetas no ofrecen una forma de hacer esto a través de su plataforma.
{% endalert %}

## Datos opcionales recopilados de forma predeterminada {#optional-data-collected-by-default}

Además de los datos mínimos de integración, los siguientes atributos son capturados automáticamente por Braze cuando inicializas la integración de SDK or kit de desarrollo de software. Puedes [desactivar]({{site.baseurl}}/developer_guide/getting_started/sdk_overview) la recopilación de estos atributos para permitir una integración mínima.

| Atributo               | Plataforma          | Descripción                                                                        | Por qué se recopila                                                                                                                                                      |
|-------------------------|-------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nombre del navegador            | Web               | Nombre del navegador                                                                | Este atributo se utiliza para enviar mensajes solo a navegadores compatibles. También se puede usar para la segmentación basada en el navegador.                                     |
| Configuración regional del dispositivo           | Android, iOS, Web | La configuración regional predeterminada del dispositivo                                                   | Este atributo se utiliza para traducir mensajes al idioma preferido del usuario.                                                                                            |
| Configuración regional del dispositivo más reciente           | Android, iOS, Web | La configuración regional predeterminada más reciente del dispositivo                                                   | Este atributo proviene de la configuración del dispositivo del usuario y se utiliza para traducir mensajes al idioma preferido del usuario. Es independiente del atributo `Most Recent Location`.                                                                                            |
| Modelo del dispositivo            | Android, iOS      | El hardware específico del dispositivo                                                | Este atributo se utiliza para enviar mensajes solo a dispositivos compatibles. También se puede usar dentro de la segmentación.                                                 |
| Marca del dispositivo            | Android           | La marca del dispositivo (por ejemplo, Samsung)                                         | Este atributo se utiliza para enviar mensajes solo a dispositivos compatibles.                                                                                          |
| Operador inalámbrico del dispositivo | Android, iOS      | El operador móvil                                                                 | Este atributo se utiliza opcionalmente para la segmentación de mensajes.<br><br>**Nota:** Este campo ha quedado obsoleto a partir de iOS 16 y será `--` de forma predeterminada en una versión futura de iOS. |
| Idioma                | Android, iOS, Web | Idioma del dispositivo o navegador, tomado de la configuración regional del dispositivo.                                                           | Este atributo se utiliza para traducir mensajes al idioma preferido del usuario. Se basa en la configuración regional del dispositivo.                                                                                            |
| Configuración de notificaciones   | Android, iOS, Web | Si esta aplicación tiene las notificaciones push habilitadas.                                   | Este atributo se utiliza para habilitar las notificaciones push.                                                                                                                    |
| Resolución              | Android, iOS, Web | Resolución del dispositivo o navegador                                                          | Se utiliza opcionalmente para la segmentación de mensajes basada en el dispositivo. El formato de este valor es "`<width>`x`<height>`".                                                                 |
| Zona horaria               | Android, iOS, Web | Zona horaria del dispositivo o navegador                                                           | Este atributo se utiliza para enviar mensajes en el momento adecuado, según la zona horaria local de cada usuario.                                                   |
| Agente de usuario              | Web               | [Agente de usuario](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) | Este atributo se utiliza para enviar mensajes solo a dispositivos compatibles. También se puede usar dentro de la segmentación.                                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Datos opcionales recopilados de forma predeterminada" }

Para obtener más información sobre el seguimiento de propiedades a nivel de dispositivo (como operador inalámbrico del dispositivo, zona horaria, resolución y otros), consulta la documentación específica de cada plataforma: [Android]({{site.baseurl}}/developer_guide/storage?tab=android), [iOS]({{site.baseurl}}/developer_guide/storage?tab=swift), [Web]({{site.baseurl}}/developer_guide/storage#cookies).

## Datos no recopilados de forma predeterminada {#data-not-collected-by-default}

De forma predeterminada, los siguientes atributos no se recopilan. Cada atributo necesita integrarse manualmente.

| Atributo                  | Plataforma     | Descripción                                                                                                                                                                                                                                                                                                               | Por qué no se recopila                                                                                                                                                                                                                                                                 |
|----------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Device Ad Tracking Enabled | Android, iOS | En iOS:<br>[`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:))<br><br>En Android:<br>[`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) | Esta propiedad requiere permisos adicionales a nivel de la aplicación, que deben ser otorgados por el integrador.                                                                                                                                                                                      |
| Device IDFA                | iOS          | Identificador de dispositivo para anunciantes                                                                                                                                                                                                                                                                                         | Esto requiere el framework de Transparencia de Seguimiento de Anuncios, que activará una revisión de privacidad adicional por parte de la App Store. Para más detalles, consulta [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)) |
| Google Advertising ID      | Android      | Identificador para publicidad dentro de las aplicaciones de Google Play                                                                                                                                                                                                                                                                        | Esto requiere que la aplicación recupere el GAID y se lo pase a Braze. Para más detalles, consulta [Google Advertising ID opcional]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration#google-advertising-id).                                         |
| Ubicación más reciente | Android, iOS | Es la última ubicación GPS conocida del dispositivo del usuario. Se actualiza al inicio de la sesión y se almacena en el perfil del usuario. | Esto requiere que el usuario otorgue permiso de ubicación a tu aplicación. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Datos no recopilados de forma predeterminada" }

{% alert note %}
El SDK or kit de desarrollo de software de Braze no almacena direcciones IP de forma local.
{% endalert %}

## Integración personalizada {#personalized-integration}

Para aprovechar al máximo Braze, nuestros integradores de SDK or kit de desarrollo de software a menudo implementan los SDK or kit de desarrollo de software de Braze y registran [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#set-custom-attributes), [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events#logging-custom-events) y [eventos de compra]({{site.baseurl}}/user_guide/data/activation/events/purchase_events#log-purchase-events) que son relevantes para su negocio, además de los datos recopilados automáticamente.

Una integración personalizada permite una comunicación adaptada que es relevante para la experiencia de tus usuarios.

{% alert important %}
Braze bloquea los perfiles de usuario ("usuarios ficticios") con más de 5 000 000 de sesiones, más de 20 000 nombres distintos de eventos personalizados o más de 20 000 nombres distintos de productos en compras, y deja de ingerir todos los datos entrantes para ese perfil tanto desde los SDK or kit de desarrollo de software como desde la REST or transferencia de estado representacional API. Para más información, consulta [Bloqueo de correo no deseado]({{site.baseurl}}/user_archival).
{% endalert %}