---
nav_title: Punchh
article_title: Punchh
page_order: 1
description: "Este artículo de referencia describe la asociación entre Braze y Punchh, una plataforma de fidelización e interacción, que permite sincronizar datos entre las dos plataformas. Los datos publicados en Braze estarán disponibles para la segmentación y pueden sincronizar los datos de usuario de nuevo en Punchh a través de plantillas de webhook configuradas en Braze."
page_type: partner
search_tag: Partner

---

# Punchh

> [Punchh](https://punchh.com/) es una plataforma de fidelización e interacción líder del sector que permite a las marcas ofrecer programas omnicanal de fidelización de clientes tanto en la tienda como digitalmente.

_Esta integración está mantenida por Punchh._

## Sobre la integración {#about-the-integration}

La integración de Braze y Punchh permite sincronizar los datos para regalos y fidelización entre las dos plataformas. Los datos publicados en Braze estarán disponibles para la segmentación y pueden sincronizar los datos de usuario de nuevo en Punchh a través de webhooks de Braze.

## ¿Cuáles son los beneficios? {#what-are-the-benefits}

- Ingesta de datos de fidelización de Punchh a Braze en tiempo real.
- Aprovecha y estratifica los potentes datos de audiencia de Braze para entregar experiencias significativas y dinámicas en todos los canales (aplicación, móvil, web, correo electrónico y SMS).
  - ¿Han abierto los clientes los correos electrónicos? ¿Los clientes abrieron la aplicación cerca de una tienda?
- Estandariza el aspecto de los correos electrónicos transaccionales enviados a través de Braze.
- Crea recorridos que permitan realizar pruebas A/B y optimizaciones sobre la marcha.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta Punchh | Necesitas una cuenta Punchh activa para beneficiarte de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel de Braze desde **Settings** > **API Keys**. |
| Punto de conexión REST de Braze | [La URL de tu punto de conexión REST]({{site.baseurl}}/api/basics/#endpoints). Tu punto de conexión depende de la URL de Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ¿Qué más debo saber? {#what-else-should-i-know}

#### Antes de integrar {#before-integrating}

- Al utilizar la integración de Braze, serán necesarias dos campañas, una en Punchh y la segunda en Braze. Por ejemplo, si envías una campaña con una oferta adjunta, la campaña de regalo se configurará dentro de Punchh, y la notificación podrá enviarse desde Braze.
- Los invitados ya deben existir en Punchh y Braze. Punchh filtrará a cualquier cliente que no esté ya fidelizado.

#### Aspectos importantes {#important-things-to-note}

- Punchh ha añadido la posibilidad de desactivar el envío de atributos de usuario predeterminados a Braze, para que el cliente no incurra en excedentes de puntos de datos. Esto se configura durante la configuración del adaptador.
- Si se utilizan segmentos personalizados en campañas recurrentes, debe utilizarse el nombre de la campaña en lugar del ID de campaña, ya que los ID cambian cada vez que se ejecuta la campaña.
- Los canales de comunicación disponibles en cada campaña de regalo de Punchh incluyen mensajes enriquecidos, notificaciones push, SMS y correo electrónico.
- Una vez que los usuarios han sido enviados a un segmento personalizado de Punchh desde Braze, no pueden ser eliminados. Solo se pueden añadir nuevos invitados a un segmento personalizado existente. Si es necesario eliminar invitados de un segmento personalizado de Punchh existente, será necesario crear una nueva campaña de webhook en Braze para enviar usuarios a un nuevo segmento personalizado de Punchh.

## Integración {#integration}

Punchh ofrece varios puntos de conexión a disposición de los clientes de Braze para ayudar a añadir ID externos a la plataforma Punchh utilizando los siguientes puntos de conexión de la API de Punchh. Una vez añadidos los ID externos, crea un adaptador en Punchh, proporciona tus credenciales de Braze y selecciona los eventos que deseas sincronizar. A continuación, puedes tomar el ID de segmento de Punchh y utilizarlo para crear un webhook de Punchh para desencadenar la sincronización de clientes en un recorrido de Canvas.

Ten en cuenta que el `user_id` de Punchh y el `external_id` de Braze deben estar disponibles en cualquiera de las dos plataformas para que la integración se sincronice correctamente.
- Los eventos enviados desde Punchh a Braze incluirán el `external_id` de Braze como identificador. Si Punchh está configurado para utilizar el `external_source_id`, ese valor se establecerá como el `external_id` de Braze. De lo contrario, la integración predeterminará la configuración del `user_id` de Punchh como el `external_id` de Braze.
- Para enviar webhooks de Braze a Punchh, el `user_id` de Punchh debe estar disponible en el perfil de usuario de Braze. Si no se utiliza el `user_id` de Punchh como el `external_id` de Braze, debe establecerse como atributo personalizado "punchh_user_id".

### Paso 1: Configurar puntos de conexión de ingestión de ID externos (opcional) {#step-1-set-up-external-id-ingestion-endpoints-optional}

Los ID externos de Braze pueden añadirse utilizando los siguientes puntos de conexión para usuarios nuevos y existentes de Punchh.

{% alert important %}
Los valores de los campos `external_source` y `external_source_id` deben ser exclusivos de Punchh y no estar asociados a perfiles existentes.
{% endalert %}

1. Nuevos usuarios de Punchh<br>
Crea nuevos usuarios en Punchh con un punto de conexión de registro de Punchh utilizando los campos `external_source` y `external_source_id`. Punchh permite enviar identificadores externos con un perfil de usuario a través de uno de los siguientes puntos de conexión de registro:
- [API de registro móvil](https://developers.punchh.com/docs/dev-portal-mobile/2e67abf6f8e12-sign-up-register)
- [API de registro SSO](https://developers.punchh.com/docs/dev-portal-online-ordering/58f18dfdd2a3d-signup-with-email-and-password)<br><br>
2. Usuarios actuales de Punchh <br>
Actualiza `external_source_id` para los usuarios existentes de Punchh. Punchh permite añadir identificadores externos a un perfil a través de un punto de conexión de actualización de la API de usuario:
- [Actualización de usuario móvil](https://developers.punchh.com/docs/dev-portal-mobile/c9b928e35a6f3-update-user-profile)
- [Actualización de usuario SSO](https://developers.punchh.com/docs/dev-portal-online-ordering/eef4eef6c97a0-update-user-information)
- [Actualización de usuario del panel de control](https://developers.punchh.com/docs/dev-portal-platform-functions/6351feaf591aa-update-a-user)
<br><br>
{% tabs local %}
{% tab User sign-up API example %}
Este ejemplo permite enviar identificadores externos con un perfil de usuario en el momento del registro. Esto se hace enviando `external_source` como "customer_id" y `external_source_id` como "111111111111111111" como tipo de datos de cadena.

```bash
curl --location --request POST 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Accept-Timezone: Etc/UTC' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--data-raw '{
    "client":"CLIENT",
    "user" : {
      "email": "test@example.com",
      "password": "PASSWORD",
      "first_name":"FIRST_NAME",
      "last_name":"LAST_NAME",
      "terms_and_conditions":"true",
      "anniversary":"2014-02-02",
      "zip_code":"94497",
      "birthday":"2004-02-02",
      "external_source":"customer_id",
      "external_source_id":"111111111111111111"
      }
}'
```
{% endtab %}
{% tab User update API example %}
Este ejemplo permite actualizar identificadores externos con un perfil de usuario. Esto se hace enviando `external_source` como "customer_id" y `external_source_id` como "111111111111111111" como tipo de datos de cadena.

```bash
curl --location --request PUT 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Authorization: Bearer ACCESS_TOKEN' \
--data-raw '{
    "client":"CLIENT",
    "user": {
        "external_source":"customer_id",
        "external_source_id":"111111111111111111"
    }
}'
```
{% endtab %}
{% endtabs %}

{% alert note %}
**Configuración de la plataforma:** Para activar los identificadores externos en Punchh, desde el panel de control de Punchh, ve a **Cockpit** > **Dashboard** > **External User Identifier**.
{% endalert %}

### Paso 2: Configuración del adaptador de Braze en Punchh {#step-2-braze-adapter-setup-in-punchh}

#### Eventos disponibles para sincronizar {#available-events-to-sync}

1. **Invitado:** Se activa al registrarse, actualizar el perfil de invitado, desactivarlo o eliminarlo.
2. **Registro de fidelización:** Se activa en las transacciones de fidelización o al escanear el código de barras del recibo.
3. **Registro de regalos:** Se desencadena por puntos regalados de una campaña.
4. **Canje:** Se activa en caso de canje de cualquier recompensa, excluidos los cupones Punchh, ya que estos se enviarían por separado como eventos de cupón, incluida la emisión y el canje.
5. **Recompensas:** Se activa a partir de recompensas otorgadas por campañas, actividad, conversión de puntos en recompensas o por la administración.
6. **Notificaciones de transacciones:** Se activa cuando un usuario realiza una transacción en el sistema Punchh (por ejemplo, caducidad de puntos).
7. **Notificaciones de marketing:** Se activa en función de diferentes configuraciones de campaña en Punchh para un segmento asociado de usuarios.

{% alert note %}
Consulta la documentación de Punchh sobre el aspecto que pueden tener las cargas útiles de muestra para estos eventos disponibles.
{% endalert %}

Trabaja con tu gestor de implementación de Punchh para configurar este adaptador.

Para configurar la integración de Braze y Punchh, haz lo siguiente:

1. En el panel de control de Punchh, ve a **Cockpit** > **Dashboard** > **Major Features** > **Enable Webhook Management** y activa **Enable Webhook Management**.<br><br>
2. A continuación, habilita los adaptadores accediendo a **Settings** > **Webhooks Manager** > **Configurations** > **Show Adapters Tab** y activa **Show Adapters Tab**.<br><br>
3. Ve a **Webhooks Manager** en la pestaña **Settings**, selecciona la pestaña **Adapters** y haz clic en **Create Adapter**. <br><br>![]({% image_buster /assets/img/punchh/punchh1.png %})<br><br>
4. Introduce el nombre del adaptador, la descripción y el correo electrónico del administrador. Selecciona **Braze** como adaptador e indica el punto de conexión de la REST API de Braze y la clave de API de Braze.<br><br>
5. A continuación, selecciona los eventos disponibles que deseas activar. Encontrarás una lista de estos eventos en [Eventos disponibles para sincronizar](#available-events-to-sync).<br><br>![]({% image_buster /assets/img/punchh/punchh3.png %})<br><br>
6. Haz clic en **Submit** para activar el webhook.

## Crear webhook de Punchh en Braze {#create-punchh-webhook-in-braze}

Braze puede añadir usuarios a un segmento de Punchh a través de webhooks utilizando segmentos personalizados de Punchh.

1. Crea un segmento personalizado en Punchh y observa el `custom_segment_id` presente en la URL del panel de control del segmento de Punchh, como se muestra a continuación. Pueden utilizarse constructores de segmentos clásicos o beta. Sin embargo, se recomienda la versión beta, ya que la versión clásica quedará obsoleta con el tiempo.<br><br>En la plataforma Punchh, ve a **Guest** > **Segment** > **Custom List** > **New Custom List**.<br><br>![]({% image_buster /assets/img/punchh/update1.png %})<br><br>

2. Crea una campaña de webhook en Braze utilizando el punto de conexión de Punchh para añadir un usuario a un segmento personalizado como URL de webhook. Aquí, puedes proporcionar el `custom_segment_id` extraído de la URL y el `user_id` como pares clave-valor.<br><br>![]({% image_buster /assets/img/punchh/punchh4.png %})<br><br>

3. Este webhook puede configurarse como una campaña singular o como un paso dentro de un Canvas. Alternativamente, si el webhook que añade usuarios a este segmento específico de Punchh se va a utilizar en múltiples Campaigns o Canvas, se puede configurar como una [plantilla]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates/).<br><br>
La clave `user_id` del webhook corresponde al ID de usuario de Punchh. Este identificador deberá añadirse a todos los webhooks creados en Braze para añadir usuarios a un segmento personalizado de Punchh. El atributo personalizado `punch_user_id` puede rellenarse dinámicamente como valor de la clave `user_id` utilizando [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#pre-formatted-variables). Puedes insertar la variable de atributo personalizado `punchh_user_id` utilizando el icono azul "más" situado en la parte superior derecha de cualquier campo de texto de plantilla.<br><br>![]({% image_buster /assets/img/punchh/update3.png %}){: style="max-width:65%;"}<br><br>![]({% image_buster /assets/img/punchh/update4.png %}){: style="max-width:65%;"}<br><br>

4. Una vez guardado el webhook, puede utilizarse para sincronizar usuarios, como se muestra a continuación. Por ejemplo, se añadirían 136 invitados al segmento personalizado de Punchh cuando se lance esta campaña de webhook de Braze.<br><br>![Un ejemplo de sincronización de usuarios utilizando el webhook guardado gracias a la integración de Braze y Punchh.]({% image_buster /assets/img/punchh/punchh6.png %})

Para más información sobre cómo se utilizan los webhooks en Braze, consulta [Crear un webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/).

## Campañas de casos de uso {#use-case-campaigns}

### Configuración de Campaign y Canvas {#campaign-and-canvas-configuration}

#### Desencadenar {#triggering}

Los casos de uso para la mensajería de Braze desencadenados por eventos de Punchh que se envían a Braze, como eventos de recompensa o eventos de invitados, pueden crearse como [campañas basadas en acciones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#action-based-delivery) o Canvas desencadenados por el evento de Punchh correspondiente.

Al añadir un desencadenador, aparecerá la lista de eventos creados en Braze. Elige el evento que debe desencadenar tu Campaign o Canvas que se enviará al usuario que registró el evento.

![]({% image_buster /assets/img/punchh/update5.png %})

Se pueden añadir filtros de propiedades para filtrar aún más el evento desencadenante. Por ejemplo, el mensaje solo debe desencadenarse cuando un cliente active el evento "checkins_gift" en el que la propiedad del evento aprobado sea `true`. Se trata de una función opcional que puede no ser aplicable a todos los casos de uso.

#### Segmentación {#segmentation}

En muchos casos, las Campaigns y Canvas de Braze desencadenados por eventos de Punchh pueden configurarse para una audiencia de "Todos los usuarios", porque la segmentación de los usuarios que desencadenan estos eventos se determina dentro de Punchh. Sin embargo, los clientes que deseen refinar aún más la audiencia de usuarios que recibirán la mensajería de Braze activada por el evento pueden hacerlo añadiendo filtros y segmentos adicionales en la sección **Target Audiences** del compositor de Campaign o en la **Audiencia de entrada** del compositor de Canvas.

### Casos de uso {#use-cases}

{% tabs local %}
{% tab Signup %}
#### Campaña de registro {#sign-up-campaign}

Al utilizar la configuración de Braze para una campaña de registro con una oferta adjunta, será necesario configurar una campaña de regalo de registro en Punchh y un mensaje de bienvenida en Braze.

Punchh recomienda que se añada un retraso de ejecución a la campaña de registro, para que Braze pueda activar primero el mensaje de bienvenida basado en el evento del invitado. Si quieres enviar un mensaje de seguimiento informando al usuario de que ha sido recompensado, puedes desencadenarlo basándote en el evento de recompensa.

En el caso de una campaña de registro, todos los inscritos pueden utilizarse para el segmento; por lo tanto, no será necesario un segmento personalizado de Braze.

Configuraciones de Punchh requeridas:
- Campaña: Registro
- Segmento: Todos inscritos
- Recompensa: Elección del cliente
Eventos requeridos:
- Evento de recompensa
- Evento de invitado
Consideraciones:
- Retraso de ejecución, se recomienda que el invitado añada un retraso de 5-10 minutos

![Se configura un segmento de usuarios en Punchh, y los invitados se inscriben en un programa de fidelización. A continuación, se activa el evento de invitado, si se ha activado, y la campaña de mensajería de Braze. Después, la campaña de regalos de registro en Punchh se desencadena a los 10 minutos, desencadenando el evento de recompensa y el mensaje de seguimiento opcional.]({% image_buster /assets/img/punchh/usecase3.png %})
{% endtab %}

{% tab Braze welcome %}
#### Campaña de bienvenida de Braze {#braze-welcome-campaign}

Cuando un nuevo usuario se registra, Punchh envía a Braze un evento de invitado que crea al usuario y envía un atributo personalizado `signup_channel`, que puedes utilizar para desencadenar la campaña de bienvenida de Braze.

Para configurar la campaña de bienvenida de Braze, sigue estos pasos:

1. En Braze, crea una campaña basada en acciones.
2. Para el desencadenador, selecciona **Change Custom Attribute Value** con el atributo personalizado `signup_channel` establecido en **Any new value**.
3. Sigue creando tu campaña, ¡y envíala cuando esté lista!

{% endtab %}
{% tab Mass offer %}
#### Campaña de ofertas masivas {#mass-offer-campaign}

Cuando utilices una campaña de oferta masiva para regalos, deberás configurar una campaña de oferta masiva en Punchh y una campaña de mensajería en Braze.

Si deseas utilizar un segmento de Braze para tu campaña o enviar una comunicación desde Braze antes de obsequiar a los invitados en la plataforma Punchh, será necesario un [segmento personalizado de Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze) para la campaña de obsequios de Punchh.

Crear el segmento de usuarios para recibir esta oferta en Braze solo se recomienda cuando se utilizan atributos no disponibles en Punchh. De lo contrario, se puede utilizar la segmentación de Punchh, y la campaña de mensajería de Braze se creará como una campaña basada en acciones activada por los usuarios que reciban su recompensa (el evento de recompensa activado por Punchh).

Configuraciones de Punchh requeridas:
- Campaña: Oferta masiva
- Segmento: Lista personalizada o a elección del cliente
- Recompensa: Elección del cliente

**Utilizando Punchh para la segmentación y el regalo, y Braze para la mensajería:**<br>
Por ejemplo, una recompensa de 2 $ de descuento se envía a un segmento configurable dentro de Punchh con mensajería enviada a través de Braze.<br>
![Se puede configurar un segmento de usuarios en Punchh, y los usuarios reciben un regalo a través de una campaña de oferta masiva de Punchh. A continuación, se desencadena un evento de recompensa y, después, la campaña de mensajería de Braze.]({% image_buster /assets/img/punchh/usecase6.png %}){: style="max-width:80%;"}

**Utilizando la segmentación y mensajería de Braze, y Punchh para regalar:**<br>
Por ejemplo, una recompensa de 2 $ de descuento y mensajes enviados a un segmento con atributos no disponibles en Punchh.<br>
![Se puede configurar un segmento de usuarios en Braze y, a continuación, enviar un mensaje desde un segmento de Braze a Braze. Después, los usuarios se envían al segmento personalizado de Punchh a través de un webhook de Braze con el segmento y el ID de usuario. A continuación, el usuario recibe un regalo a través de la campaña de ofertas masivas de Punchh con un segmento personalizado. Después se desencadena el evento de recompensa.]({% image_buster /assets/img/punchh/usecase5.png %}){: style="max-width:80%;"}

**Utilizando la segmentación de Braze y Punchh para regalar o enviar mensajes, o ambas cosas:**<br>
Por ejemplo, se envía una recompensa de 2 $ de descuento a un segmento con atributos no disponibles en Punchh, pero no se requiere mensajería, o la mensajería puede enviarse a través de Punchh (ten en cuenta que todos los invitados deben estar presentes en Punchh).<br>
![Se puede configurar un segmento de usuarios en Braze, y los usuarios se envían al segmento personalizado de Punchh a través de un webhook de Braze con el segmento y el ID de usuario. A continuación, el usuario recibe un regalo a través de la campaña de ofertas masivas de Punchh con un segmento personalizado. Después se desencadena el evento de recompensa.]({% image_buster /assets/img/punchh/usecase4.png %})

{% endtab %}
{% tab Recurring mass offer %}
#### Campaña recurrente de ofertas masivas {#recurring-mass-offer-campaign}

Al utilizar una campaña de oferta masiva recurrente para regalos, será necesario configurar una campaña de oferta masiva en Punchh y una campaña de mensajería en Braze. Será necesario un segmento personalizado de Punchh si el cliente desea utilizar la segmentación de Braze (solo se recomienda si se utilizan atributos no disponibles en Punchh). De lo contrario, se puede utilizar la segmentación de Punchh, y la campaña de mensajería de Braze se activará en función del evento de recompensa.

Configuraciones de Punchh requeridas:
- Campaña: Oferta masiva recurrente
- Segmento: Lista personalizada o a elección del cliente
- Recompensa: Elección del cliente
Consideraciones:
- Los ID de campaña y los nombres de campaña se envían a Braze como una propiedad del evento. Si quieres utilizar un identificador de campaña de Punchh en Braze para filtrar aún más la audiencia que recibe la campaña, debes utilizar el nombre de la campaña porque los ID de campaña cambian a diario.

{% endtab %}
{% tab Post check-in offer with notification %}
#### Campaña de oferta posterior al check-in con notificación {#post-check-in-offer-campaign-with-notification}

Al utilizar una campaña de oferta posterior al check-in, Braze enviará la notificación relativa al regalo, y cuando el invitado haga el check-in, recibirá el regalo de la campaña posterior al check-in de Punchh. Por lo tanto, será necesario configurar una campaña de oferta posterior al check-in en Punchh y una campaña de mensajería en Braze (si se va a notificar la campaña a los clientes).

Configuraciones de Punchh requeridas:
- Campaña: Oferta posterior al check-in
- Segmento: Lista personalizada
- Recompensa: Elección del cliente

Por ejemplo, un correo electrónico notificando a los invitados que visiten este fin de semana para obtener el doble de puntos a un segmento con atributos no disponibles en Punchh. Punchh obsequiará a este segmento con puntos tras un registro de entrada válido y un mensaje opcional de Braze.

![Se configura un segmento de usuarios en Braze y se envían mensajes desde la campaña posterior al check-in de Braze. A continuación, los usuarios que cumplen los requisitos se envían al segmento personalizado de Punchh a través de un webhook de Braze con el segmento y el ID de usuario. Por último, el usuario cualificado del segmento personalizado se registra y recibe el regalo y el mensaje opcional a través de la campaña posterior al registro.]({% image_buster /assets/img/punchh/update7.png %})

{% endtab %}
{% tab Post check-in offer without notification %}
#### Campaña de oferta posterior al check-in sin notificación {#post-check-in-offer-campaign-without-notification}

Al utilizar una campaña de oferta posterior al check-in que no notifique primero a los clientes, la campaña será un regalo (mensajería opcional) y activará cualquier notificación dentro de Braze. Por lo tanto, se debe configurar una campaña de oferta posterior al check-in en Punchh; sin embargo, no se requiere una lista personalizada. En su lugar, puedes elegir el segmento que desees dentro de Punchh.

Configuraciones de Punchh requeridas:
- Campaña: Oferta posterior al check-in
- Segmento: Elección del cliente
- Recompensa: Elección del cliente

Por ejemplo, se envía una campaña de sorpresa y deleite de Braze a un segmento disponible en Punchh, agradeciendo a los invitados su visita y recompensándoles con 2 $ de descuento en su próxima visita.

![Se puede configurar un segmento de usuarios cualificados dentro de Punchh, y un usuario cualificado se registra y recibe un regalo a través de una campaña posterior al check-in de Punchh. Después de esto, se desencadena un evento de recompensa y se envía el mensaje de recordatorio notificando a los invitados la recompensa enviada desde Braze.]({% image_buster /assets/img/punchh/usecase2.png %})

{% endtab %}
{% tab Anniversary %}
#### Campaña de aniversario {#anniversary-campaign}

Al utilizar una campaña de aniversario, el usuario recibirá primero un regalo por su aniversario de la campaña de Punchh. Este regalo (evento de recompensa) desencadenará la campaña de mensajería dentro de Braze que notifica al usuario el regalo. Por lo tanto, no es necesaria una lista personalizada. En su lugar, puedes elegir la configuración del segmento y del aniversario dentro de Punchh.

Configuraciones de Punchh requeridas:
- Campaña: Campaña de aniversario
- Segmento: Elección del cliente
- Recompensa: Elección del cliente
Consideraciones:
- Regalos el mes del registro
- Duración de la vida útil (¿durante cuánto tiempo es válida la recompensa de cumpleaños?)
- Campañas recurrentes, programación requerida

![Se puede crear un segmento opcional dentro de Punchh, y un usuario que cumpla los requisitos recibe una recompensa a través de una campaña de aniversario de Punchh. Después de esto, se desencadena un evento de recompensa y se envía el mensaje de recordatorio notificando a los invitados la recompensa enviada desde Braze.]({% image_buster /assets/img/punchh/usecase1.png %})

{% endtab %}
{% tab Recall %}
#### Campaña de recuperación {#recall-campaign}

Cuando te dirijas a usuarios en función de su inactividad, puedes utilizar una campaña de recuperación. El cliente puede crear el segmento y la campaña dentro de Punchh pero utilizar Braze para la mensajería.

Si deseas utilizar la segmentación creada en Braze, se puede adjuntar un [segmento personalizado de Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze) basado en la inactividad a una campaña de oferta masiva recurrente.

Configuraciones de Punchh requeridas:
- Campaña: Campaña de recuperación
- Segmento: Elección del cliente
- Recompensa: Elección del cliente
Consideraciones:
- La campaña se ejecuta según un calendario

![Se puede crear un segmento opcional dentro de Punchh, y un usuario que cumpla los requisitos recibe una recompensa a través de una campaña de recuperación de Punchh. Después de esto, se desencadena un evento de recompensa, y se envía el mensaje de recordatorio notificando a los invitados la recompensa enviada desde Braze.]({% image_buster /assets/img/punchh/usecase.png %})

{% endtab %}
{% endtabs %}