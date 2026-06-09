---
nav_title: mParticle de Rokt
article_title: mParticle de Rokt
alias: /partners/mparticle/
description: "Este artículo de referencia describe la asociación entre Braze y mParticle, una plataforma de datos de los clientes que recopila y encamina información entre fuentes de tu stack de marketing."
page_type: partner
search_tag: Partner

---

# mParticle de Rokt {#mparticle-by-rokt}

{% multi_lang_include video.html id="Njhqwd36gZM" align="right" %}

> Con la plataforma de datos de los clientes de mParticle, podrás hacer mucho más con tus datos. Los especialistas en marketing más sofisticados utilizan mParticle para orquestar los datos de todo su stack de crecimiento, lo que les permite ganar en los momentos clave del recorrido del cliente.

La integración de Braze y mParticle te permite controlar fácilmente el flujo de información entre ambos sistemas:
- Sincroniza las audiencias de mParticle con Braze para la segmentación de Campaign y Canvas de Braze.
- Comparte datos entre las dos plataformas. Esto puede hacerse mediante la integración del kit de mParticle y la integración de servidor a servidor.
- [Envía la interacción del usuario de Braze a mParticle a través de Currents]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents/), haciéndola procesable en todo el stack de crecimiento.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de mParticle | Se necesita una [cuenta de mParticle](https://app.mparticle.com/login) para beneficiarse de esta asociación. |
| Instancia de Braze | Tu instancia de Braze se encuentra en la [página de resumen de la API]({{site.baseurl}}/api/basics/#endpoints) (por ejemplo, `US-01` o `US-02`). |
| Clave de identificación de la aplicación de Braze | Tu clave de identificación de la aplicación. <br><br>Se encuentra en **Administrar configuración** > **Clave de API** en el dashboard de Braze. |
| Clave de API REST del espacio de trabajo | (Servidor a servidor) Una clave de API REST de Braze<br><br>Se puede crear en **Consola para desarrolladores** > **Configuración de la aplicación** > **Clave de API** en el dashboard de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Audiencias {#audiences}

Utiliza la asociación de Braze y mParticle para configurar tu integración e importar audiencias de mParticle directamente a Braze para reorientar, creando un ciclo completo de datos de un sistema a otro.

Cualquier integración que configures registrará puntos de datos. Si tienes alguna pregunta sobre los matices de los puntos de datos de Braze, tu director de cuentas de Braze puede responderlas.

#### Reenvío de audiencias {#forwarding-audiences}

mParticle ofrece tres formas de establecer los atributos de pertenencia a cohortes, controladas por la configuración "[Enviar segmentos como](#send_settings)". Consulta las siguientes secciones para el procesamiento de cada opción:

- [Atributo de cadena única](#string)
- [Atributo de array único](#array)
- [Un atributo por segmento](#per-segment)
- [Atributo de array único y atributo de cadena única](#both-1)
- [Atributo de array único y un atributo por segmento](#both-2)
- [Atributo de cadena única y un atributo por segmento](#both-3)
- [Atributo de array único, atributo de cadena única y un atributo por segmento](#multi)

##### Atributo de cadena única {#string}

mParticle creará un único atributo personalizado llamado `SegmentMembership`. El valor de este atributo es una cadena de ID de audiencia de mParticle separados por comas que coinciden con el usuario. Estos ID de audiencia se pueden encontrar en el dashboard de mParticle en **Audiences**.

Por ejemplo, si una audiencia de mParticle "Ibiza dreamers" tiene un ID de audiencia de "11036", puedes segmentar a estos usuarios con el filtro `SegmentMembership` — `matches regex` — `11036`.

Aunque esta es la opción predeterminada en mParticle, la mayoría de los usuarios de la empresa optan por utilizar [atributos de array único](#array) para la experiencia de filtrado al crear segmentos en Braze.

{% alert important %}
Esta solución no se recomienda si tienes más de unas pocas audiencias, ya que los atributos personalizados pueden tener hasta 255 caracteres de longitud, por lo que no podrás almacenar docenas o cientos de audiencias en un perfil de usuario con este método. Si tienes un gran número de cohortes por usuario, recomendamos encarecidamente la configuración "un atributo por segmento".
{% endalert %}

![Pertenencia a segmento de mParticle]({% image_buster /assets/img_archive/mparticle1.png %})

##### Atributo de array único {#array}

mParticle crea un único atributo de array personalizado en Braze para cada usuario, llamado `SegmentMembershipArray`. El valor de este atributo es un array de ID de audiencia de mParticle que coinciden con el usuario.

Por ejemplo, si un usuario es miembro de tres audiencias de mParticle con los ID de audiencia "13053", "13052" y "13051", puedes segmentar a los usuarios que coincidan con una de esas audiencias con el filtro `SegmentMembershipArray` — `includes value` — `13051`.

{% alert note %}
Los atributos de array de Braze tienen una longitud máxima predeterminada de 500. Si alguno de tus usuarios es miembro de más de 500 audiencias, Braze truncará su información de pertenencia. Para una solución alternativa, ponte en contacto con tu director de cuentas de Braze para aumentar el umbral de longitud máxima del array.
{% endalert %}

##### Un atributo por segmento {#per-segment}

mParticle creará un atributo personalizado booleano para cada audiencia a la que pertenezca un usuario. Por ejemplo, si una audiencia de mParticle se llama "Possible Parisians", puedes segmentar a estos usuarios con el filtro `In Possible Parisians` - `equals` - `true`.

![Atributo personalizado de mParticle]({% image_buster /assets/img_archive/mparticle2.png %})

##### Atributo de array único y atributo de cadena única {#both-1}

mParticle enviará atributos como se describe tanto en atributo de array único como en atributo de cadena única.

##### Atributo de array único y un atributo por segmento {#both-2}

mParticle enviará atributos como se describe tanto en atributo de array único como en un atributo por segmento.

##### Atributo de cadena única y un atributo por segmento {#both-3}

mParticle enviará atributos como se describe tanto en atributo de cadena única como en un atributo por segmento.

##### Atributo de array único, atributo de cadena única y un atributo por segmento {#multi}

mParticle enviará atributos como se describe en atributo de array único, atributo de cadena única y un atributo por segmento.

#### Paso 1: Crear una audiencia en mParticle {#send_settings}

Para crear una audiencia en mParticle:

1. Ve a **Audiences** > **Single Workspace** > **+ New Audience**.
2. Para conectar Braze como salida para tu audiencia, debes proporcionar los siguientes campos:

| Nombre del campo | Descripción |
| ------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Clave de API | Se encuentra en el dashboard de Braze en **Settings** > **API Keys**. |
| Sistema operativo de la clave de API | Selecciona a qué sistema operativo corresponde tu clave de API de Braze. Esta selección limitará los tipos de tokens de notificaciones push reenviados en una actualización de audiencia. |
| Enviar segmentos como | El método de envío de audiencias a Braze. Consulta la sección [Reenvío de audiencias](#forwarding-audiences) para más detalles. |
| Clave de API REST del espacio de trabajo | Clave de API REST de Braze con permisos completos. Se puede crear en el dashboard de Braze desde **Settings** > **API Keys**. |
| Tipo de identidad externa | El tipo de identidad de usuario de mParticle que se reenviará como ID externo a Braze. Recomendamos dejarlo en el valor predeterminado, Customer ID. |
| Tipo de identidad de correo electrónico | El tipo de identidad de usuario de mParticle que se reenviará como correo electrónico a Braze. |
| Instancia de Braze | Especifica a qué clúster se reenviarán tus datos de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 1: Crear una audiencia en mParticle" }

{:start="3"}
3. Por último, **guarda** tu audiencia.

Deberías empezar a ver las audiencias sincronizándose con Braze en unos minutos. La pertenencia a la audiencia solo se actualizará para los usuarios con `external_ids` (es decir, no para usuarios anónimos). Para más información sobre cómo crear audiencias de mParticle en Braze, consulta la documentación de mParticle sobre [Configuración](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings).

#### Paso 2: Segmentar usuarios en Braze {#step-2-segment-users-in-braze}

En Braze, para crear un segmento de estos usuarios, ve a **Segments** en **Engagement** y nombra tu segmento. A continuación se muestran dos ejemplos de segmentos según la opción que hayas seleccionado para **Enviar segmentos como**. Para más detalles sobre cada opción, consulta [Reenvío de audiencias](#forwarding-audiences).

- **Atributo de array único:** Selecciona `SegmentMembershipArray` como tu filtro. A continuación, utiliza la opción "includes value" e introduce el ID de audiencia deseado. ![Filtro de segmento de mParticle "SegmentMembershipArray" configurado como "includes value" e ID de audiencia.]({% image_buster /assets/img_archive/mparticle5.png %})<br><br>
- **Un atributo por segmento:** Selecciona tu atributo personalizado como filtro. A continuación, utiliza la opción "equals" y elige la lógica adecuada. ![Filtro de segmento de mParticle "in possible parisians" configurado como "equals" y "true".]({% image_buster /assets/img_archive/mparticle3.png %})

Una vez guardado, puedes hacer referencia a este segmento durante la creación de Canvas o Campaign en el paso de segmentación de usuarios.

#### Desactivar y eliminar conexiones {#deactivating-and-deleting-connections}

Dado que mParticle no mantiene directamente segmentos en Braze, no eliminará segmentos cuando la conexión de audiencia de mParticle correspondiente se elimine o desactive. Cuando esto suceda, mParticle no actualizará los atributos de usuario de la audiencia en Braze para eliminar la audiencia de cada usuario.

Para eliminar la audiencia de un usuario de Braze antes de la eliminación, ajusta los filtros de audiencia para forzar el tamaño de la audiencia a 0 antes de eliminar una audiencia. Una vez que el cálculo de la audiencia se haya completado y devuelva 0 usuarios, elimina la audiencia. Entonces, la pertenencia a la audiencia se actualizará en Braze a `false` para la opción de atributo único o eliminará el ID de audiencia del formato de array.

## Mapeado de datos {#data-mapping}

Los datos se pueden mapear a Braze utilizando la [integración de kit embebido](#embedded-kit-integration) si deseas conectar tus aplicaciones móviles y web a Braze a través de mParticle. También puedes utilizar la [integración de API de servidor a servidor](#server-api-integration) para reenviar datos del lado del servidor a Braze.

Independientemente del enfoque que elijas, debes configurar Braze como salida:

### Configurar los ajustes de salida de Braze {#configure-your-braze-output-settings}

En mParticle, ve a **Setup > Outputs > Add Outputs** y selecciona **Braze** para abrir la configuración del kit de Braze. **Guarda** cuando hayas terminado.

| Nombre del ajuste | Descripción |
| ------------ | ----------- |
| Clave de identificación de la aplicación de Braze | Tu clave de identificación de la aplicación de Braze se encuentra en el dashboard de Braze en **Settings** > **API Keys**. Ten en cuenta que las claves de API serán diferentes para cada plataforma (iOS, Android y Web). |
| Tipo de identidad externa | El tipo de identidad de usuario de mParticle que se reenviará como ID externo a Braze. Recomendamos dejarlo en el valor predeterminado, Customer ID. |
| Tipo de identidad de correo electrónico | El tipo de identidad de usuario de mParticle que se reenviará como correo electrónico a Braze. Recomendamos dejarlo en el valor predeterminado, Email. |
| Instancia de Braze | El clúster al que se reenviarán tus datos de Braze; debe ser el mismo clúster en el que se encuentra tu dashboard. |
| Habilitar reenvío de flujo de eventos | (Servidor a servidor) Cuando está habilitado, todos los eventos se reenviarán en tiempo real. Si no, todos los eventos se reenviarán en lote. Al elegir habilitar el reenvío de flujo de eventos, asegúrate de que los datos que envías a Braze respeten los [límites de velocidad]({{site.baseurl}}/api/api_limits/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurar los ajustes de salida de Braze" }

![]({% image_buster /assets/img_archive/configure_settings.png %})

### Integración de kit embebido {#embedded-kit-integration}

Los SDK de mParticle y Braze estarán presentes en tu aplicación a través de la integración de kit embebido. Sin embargo, a diferencia de una integración directa de Braze, mParticle se encarga de llamar a la mayoría de los métodos del SDK de Braze por ti. Los métodos de mParticle que utilizas para rastrear datos de usuario se mapearán automáticamente a los métodos del SDK de Braze.

Estos mapeados del SDK de mParticle para [Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy), [iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy) y [Web](https://github.com/mparticle-integrations/mparticle-javascript-integration-braze) son de código abierto y se pueden encontrar en la [página de GitHub de mParticle](https://github.com/mparticle-integrations).

La integración del SDK de kit embebido te permite aprovechar nuestro conjunto completo de características (push, mensajes dentro de la aplicación y todo el seguimiento de análisis de mensajes relevante).

{% alert note %}
Para las integraciones de Content Cards y mensajes dentro de la aplicación personalizados, llama directamente a los métodos del SDK de Braze.
{% endalert %}

#### Paso 1: Integrar los SDK de mParticle {#step-1-integrate-the-mparticle-sdks}

Integra los SDK de mParticle apropiados en tu aplicación según las necesidades de tu plataforma:

* [mParticle para Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticle para iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticle para Web](https://docs.mparticle.com/developers/sdk/web/getting-started/)

#### Paso 2: Completar la integración del kit de eventos de Braze de mParticle {#step-2-complete-mparticles-braze-event-kit-integration}

Aunque el SDK de Braze no necesita incluirse directamente en tu sitio web o aplicación para esta integración de mParticle, se debe instalar el siguiente kit Appboy de mParticle para reenviar datos desde tu aplicación a Braze.

La [guía de integración del kit de eventos de Braze](https://docs.mparticle.com/integrations/braze/event/#kit-integration) de mParticle te guiará a través de las instrucciones de alineación personalizadas de mParticle y Braze según tus necesidades de mensajería (push, seguimiento de ubicación, etc.).

#### Paso 3: Configuración de conexiones para tu salida de Braze {#step-3-connections-settings-for-your-braze-output}

En mParticle, ve a **Connections** > **Connect** > **[Tu plataforma deseada]** > **Connect Output** para agregar Braze como salida. Luego, selecciona **Save**.

![]({% image_buster /assets/img_archive/mParticle_event_config.png %})

No todos los ajustes de conexión se aplicarán a todas las plataformas y tipos de integración. Para un desglose de los ajustes de conexión y las plataformas a las que se aplican, consulta la [documentación de mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

### Integración de API de servidor {#server-api-integration}

Este es un complemento para enrutar los datos de tu backend a Braze si estás utilizando los SDK del lado del servidor de mParticle (por ejemplo, Ruby, Python, etc.). Para configurar esta integración de servidor a servidor con Braze, sigue la [documentación de mParticle](https://docs.mparticle.com/guides/platform-guide/connections/).

{% alert important %}
La integración de servidor a servidor no es compatible con las características de la interfaz de usuario de Braze, como los mensajes dentro de la aplicación, Content Cards o notificaciones push. También existen datos capturados automáticamente, como los campos a nivel de dispositivo, que no están disponibles a través de este método.

Considera una integración en paralelo si deseas utilizar estas características.

Para que los datos del lado del servidor se reenvíen a Braze, deben incluir un `external_id`; los usuarios anónimos no se reenviarán.
{% endalert %}

#### Configuración de conexiones para tu salida de Braze {#connections-settings-for-your-braze-output}

En mParticle, ve a **Connections > Connect > [Tu plataforma deseada] > Connect Output** para agregar Braze como salida. **Guarda** cuando hayas terminado.

![]({% image_buster /assets/img_archive/mParticle_connections.png %})

No todos los ajustes de conexión se aplicarán a todas las plataformas y tipos de integración. Para un desglose de los ajustes de conexión y las plataformas a las que se aplican, consulta la [documentación de mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

Antes de habilitar "Enriched User Attributes" o "Enriched User Identities", te recomendamos revisar [Posibles excedentes de puntos de datos](#potential-data-point-overages) para asegurarte de que conoces cómo estos ajustes afectarán el uso de puntos de datos.

### Detalles del mapeado de datos {#data-mapping-details}

#### Tipos de datos {#data-types}
No todos los tipos de datos son compatibles entre ambas plataformas.
- Las [propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) admiten objetos de cadena, numéricos, booleanos o de fecha. No admiten arrays ni objetos anidados.
- Los [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) admiten objetos de cadena, numéricos, booleanos, de fecha y arrays, pero no admiten objetos ni objetos anidados.

{% alert note %}
Braze no admite marcas de tiempo anteriores al año 0 ni posteriores al año 3000 en atributos personalizados de tipo `Time`. Braze ingerirá estos valores cuando sean enviados por mParticle, pero el valor se almacenará como una cadena.
{% endalert %}

#### Mapeado de datos

| Tipo de datos de mParticle | Tipo de datos de Braze | Descripción |
| ------------------- | --------------- | ----------- |
| Atributos de usuario (reservados) | Atributo estándar | Por ejemplo, la clave de atributo de usuario reservada `$FirstName` de mParticle se mapea al campo de atributo estándar `first_name` de Braze. |
| Atributos de usuario (otros) | Atributo personalizado | Cualquier atributo de usuario pasado a mParticle que no esté dentro de sus claves de atributo de usuario reservadas se registra en Braze como un atributo personalizado.<br><br>Los atributos de usuario admiten cadena, numéricos, booleanos, fecha y arrays, pero no admiten objetos ni objetos anidados. |
| Evento personalizado | Evento personalizado | Los eventos personalizados de mParticle son reconocidos por Braze como un evento personalizado. Los atributos del evento se reenvían como propiedades del evento personalizado.<br><br>Los atributos de evento pasados a Braze como propiedades del evento admiten objetos de cadena, numéricos, booleanos o de fecha, pero no admiten arrays ni objetos anidados. |
| Evento de comercio de compra | Evento de compra | Los eventos de comercio de compra se mapearán a eventos de compra de Braze. <br><br>Alterna el valor del ajuste para agrupar datos de eventos de comercio para registrar compras a nivel de pedido o de producto. Por ejemplo, si es `false`, un único evento entrante con dos productos, promociones o impresiones únicos resultaría en al menos dos eventos salientes de Braze. Si se establece en `true`, resultaría en un único evento saliente con un array anidado de productos, promociones o impresiones, respectivamente.<br><br>Para más información sobre los campos de comercio adicionales que se registrarán, consulta la [documentación de mParticle](https://docs.mparticle.com/integrations/braze/event/#purchase-events). <br><br>Al configurar "bundle commerce event data" como `false`, los atributos de producto pasados a Braze como propiedades del evento de compra admiten objetos de cadena, numéricos, booleanos o de fecha, pero no admiten arrays ni objetos anidados. |
| Todos los demás eventos de comercio | Evento personalizado | Todos los demás eventos de comercio se mapearán a eventos personalizados. <br><br>Alterna el valor del ajuste para agrupar datos de eventos de comercio para registrar compras a nivel de pedido o de producto. Por ejemplo, si es `false`, un único evento entrante con dos productos, promociones o impresiones únicos resultaría en al menos dos eventos salientes de Braze. Si se establece en `true`, resultaría en un único evento saliente con un array anidado de productos, promociones o impresiones, respectivamente.<br><br>Además de ciertos valores de comercio predeterminados, los atributos de producto se registrarán como propiedades del evento de Braze. Para más información sobre los campos de comercio adicionales que se registrarán, consulta la [documentación de mParticle](https://docs.mparticle.com/integrations/braze/event/#other-commerce-events)<br><br>Al configurar "bundle commerce event data" como `false`, los atributos de producto pasados a Braze como propiedades del evento admiten objetos de cadena, numéricos, booleanos o de fecha, pero no admiten arrays ni objetos anidados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mapeado de datos" }

#### Mapeado de identidad de usuario {#user-identity-mapping}
Para cada salida de mParticle, puedes seleccionar el tipo de identidad externa que se enviará a Braze como `external_id`. Aunque el valor predeterminado es customer ID, puedes elegir mapear otro ID, como `MPID`, para enviarlo a Braze como `external_id`. Ten en cuenta que elegir un identificador distinto al customer ID puede influir en cómo se envían los datos en Braze.

Por ejemplo, mapear MPID a tu `external_id` de Braze tendrá los siguientes efectos:
- Debido a la naturaleza de cuándo se asigna el MPID, a todos los usuarios se les asignará un `external_id` al inicio de la sesión.
- La configuración de Currents puede requerir un mapeado adicional debido a los diferentes tipos de datos entre MPID y `external_id`.

### Reenvío de solicitudes de eliminación (solicitudes de sujetos de datos) {#forwarding-erasure-requests-data-subject-requests}

Reenvía solicitudes de eliminación a Braze configurando una salida de solicitud de sujeto de datos a Braze. Para reenviar solicitudes de eliminación a Braze, sigue la [documentación de mParticle](https://docs.mparticle.com/integrations/braze/forwarding-dsr/).

## Posibles excedentes de puntos de datos {#potential-data-point-overages}

### Atributos de usuario enriquecidos {#enriched-user-attributes}

#### Habilitar atributos/identidades de usuario enriquecidos (solo servidor a servidor) {#enriched}

En la configuración de conexión de mParticle, Braze recomienda desactivar **Include Enriched User Attributes**. Si está habilitado, mParticle reenviará todos los atributos de usuario disponibles (como atributos estándar, atributos personalizados y atributos calculados) del perfil existente a Braze en cada evento registrado. Esto resulta en un alto consumo de puntos de datos porque mParticle envía a Braze los mismos atributos sin cambios en cada llamada.

Por ejemplo, si un usuario agrega su nombre, apellido y número de teléfono durante su primera sesión y luego se suscribe a un boletín y agrega la misma información y un correo electrónico, desencadenando un evento de suscripción al boletín:
- Si está activado (predeterminado), se incurrirá en cinco puntos de datos. (evento de suscripción, dirección de correo electrónico, nombre, apellido y número de teléfono)
- Si está desactivado, se incurrirá en dos puntos de datos (evento de suscripción y dirección de correo electrónico)

{% alert note %}
Desactivar este ajuste no verificará los datos que cambian. Sin embargo, evitará que la integración envíe todos los atributos de usuario del perfil del usuario que no se recibieron en el lote entrante original o que no se establecieron explícitamente como atributo para el evento. Es importante verificar que solo se pasen deltas a Braze.
{% endalert %}

#### Consideraciones al desactivar los atributos de usuario enriquecidos {#considerations-of-turning-off-enriched-user-attributes}

Hay algunas consideraciones a tener en cuenta al desactivar **Include Enriched User Attributes**:
1. La integración de servidor a servidor utiliza la API de eventos de mParticle para enviar eventos a Braze. Cada solicitud se desencadena por un evento. Cuando se cambia un atributo de usuario, como actualizar una dirección de correo electrónico, pero no está asociado con un evento específico (por ejemplo, un evento personalizado de actualización de perfil), el nuevo valor solo se pasa a una salida como Braze como un "atributo enriquecido" en la carga útil del siguiente evento desencadenado por el usuario. Cuando **Include Enriched User Attributes** está desactivado, este nuevo valor de atributo no asociado con un evento específico no se pasará a Braze.
  - Para resolver esto, recomendamos crear un evento separado de "atributo de usuario actualizado" que solo envíe los atributos de usuario específicos que se hayan actualizado a Braze. Ten en cuenta que con este enfoque, aún estás registrando un punto de datos adicional para el evento "atributo de usuario actualizado", pero el uso de puntos de datos será mucho menor que enviar todos los atributos de usuario en cada llamada con la característica habilitada.
2. Los atributos calculados se pasan a Braze como un atributo de usuario enriquecido, por lo que cuando "Enriched User Attributes" está desactivado, estos ya no se pasarán a Braze. Para reenviar atributos calculados a Braze cuando "Enriched User Attributes" está desactivado, un [feed de atributos calculados](https://docs.mparticle.com/guides/platform-guide/calculated-attributes/using-calculated-attributes/#forward-calculated-attributes-in-the-calculated-attributes-feed) podría ayudar sin enviar todos los atributos. El feed enviará una actualización a Braze cuando un atributo calculado cambie.

## Solución de problemas {#troubleshooting}

### Solución de problemas de notificaciones push de iOS con el kit de eventos de Braze {#troubleshooting-ios-push-notifications-with-the-braze-event-kit}

Si las notificaciones push no funcionan al usar el kit de eventos de Braze (integración de kit embebido) en iOS, verifica lo siguiente:
1. **Reenvío de tokens de push:** Confirma que mParticle está reenviando tokens de push a Braze. En tu dashboard de mParticle, verifica que la conexión del kit de Braze tenga push habilitado y que la credencial de push de Apple correcta esté configurada en el dashboard de Braze.
2. **Orden de inicialización del kit:** El kit de Braze debe inicializarse antes de que tu aplicación solicite permisos de push. Si los permisos de push se solicitan antes de que el kit esté activo, el token de push puede no reenviarse a Braze. Verifica que el SDK de mParticle se inicie temprano en el ciclo de vida de tu aplicación.
3. **Method swizzling:** El kit de Apple de mParticle utiliza method swizzling para reenviar automáticamente tokens de push y manejar eventos de notificaciones push. Si has deshabilitado el swizzling u otro SDK está interfiriendo, los tokens de push pueden no llegar a Braze. Verifica que el swizzling esté habilitado en tu configuración de mParticle.
4. **Manejo manual de tokens:** Si gestionas los tokens de push manualmente (por ejemplo, implementando `application:didRegisterForRemoteNotificationsWithDeviceToken:`), asegúrate de pasar el token a mParticle asignándolo a la propiedad de token de notificación push, por ejemplo: `MParticle.sharedInstance().pushNotificationToken = deviceToken`. El kit lo reenviará a Braze.
5. **Discrepancia de entorno:** Confirma que el entorno de la credencial de APNs (desarrollo vs. producción) coincida con la compilación de tu aplicación. Para más detalles, consulta [Solución de problemas de push en iOS]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift).
6. **Temporización de la inicialización del kit:** Si accedes a la instancia de Braze desde `didFinishLaunchingWithOptions`, el kit de mParticle puede no estar listo cuando llega una notificación push. Inicializa el manejo de push en [`userNotificationCenter(_:didReceive:withCompletionHandler:)`]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) (o el delegado de respuesta de notificación equivalente) para que el kit de Braze esté activo cuando el usuario abra una notificación.

### Envío de datos innecesarios o duplicados a Braze {#sending-unnecessary-or-duplicate-data-to-braze}
Braze cuenta un punto de datos cada vez que se pasa un atributo a Braze, incluso si el valor no ha cambiado. Por esta razón, Braze recomienda reenviar solo los datos necesarios para actuar dentro de Braze y asegurarse de que solo se pasen deltas de atributos.