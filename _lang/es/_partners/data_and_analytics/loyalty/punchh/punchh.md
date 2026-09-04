---
nav_title: Punchh
article_title: Punchh
page_order: 1
description: "Este artículo de referencia describe la asociación entre Braze y Punchh, una plataforma de fidelización y participación, que permite sincronizar datos entre las dos plataformas. Los datos publicados en Braze estarán disponibles para la segmentación y pueden sincronizar los datos de usuario de nuevo en Punchh a través de plantillas de webhook configuradas en Braze."
page_type: partner
search_tag: Partner
---

# Punchh

> [Punchh](https://punchh.com/) es una plataforma de fidelización y participación líder del sector que permite a las marcas ofrecer programas omnicanal de fidelización de clientes tanto en la tienda como digitalmente.

_Esta integración está mantenida por Punchh._

## Sobre la integración {#about-the-integration}

La integración de Braze y Punchh te permite sincronizar datos con fines de obsequios y fidelización en ambas plataformas. Los datos publicados en Braze estarán disponibles para segmentación y pueden sincronizar los datos de usuario de vuelta a Punchh a través de webhooks de Braze.

## ¿Cuáles son los beneficios? {#what-are-the-benefits}

- Ingesta de datos de fidelización de Punchh a Braze en tiempo real.
- Aprovecha y combina potentes datos de audiencia de Braze para ofrecer experiencias multicanal significativas y dinámicas (aplicación, móvil, web, correo electrónico y SMS).
  - ¿Los clientes abrieron correos electrónicos? ¿Los clientes abrieron la aplicación cerca de una tienda?
- Estandariza la apariencia de los correos transaccionales enviados a través de Braze.
- Crea recorridos que permitan pruebas A/B y optimización sobre la marcha.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta Punchh | Necesitas una cuenta Punchh activa para aprovechar esta integración. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos de `users.track`. <br><br> Se puede crear en el panel de Braze desde **Configuración** > **Claves de API**. |
| Endpoint REST de Braze | [La URL de tu endpoint REST]({{site.baseurl}}/api/basics#endpoints). Tu endpoint depende de la URL de Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## ¿Qué más debo saber? {#what-else-should-i-know}

### Antes de integrar {#before-integrating}

- Al utilizar la integración con Braze, se necesitarán dos campañas, una en Punchh y otra en Braze. Por ejemplo, si envías una campaña con una oferta adjunta, la campaña de regalo se configurará dentro de Punchh, y la notificación se puede enviar desde Braze.
- Los invitados ya deben existir en Punchh y Braze. Punchh filtrará a cualquier cliente que no sea ya un invitado de fidelización.

### Aspectos importantes a tener en cuenta {#important-things-to-note}

- Punchh ha añadido la posibilidad de deshabilitar el envío de atributos de usuario predeterminados a Braze, para que el cliente no incurra en excedentes de puntos de datos. Esto se configura durante la configuración del adaptador.
- Si se utilizan Segments personalizados en campañas recurrentes, se debe usar el nombre de la campaña en lugar del ID de la campaña, ya que los ID cambian cada vez que se ejecuta la campaña.
- Los canales de comunicación disponibles dentro de cada campaña de regalo de Punchh incluyen mensajes enriquecidos, notificaciones push, SMS y correo electrónico.
- Después de que los usuarios han sido enviados a un Segment personalizado de Punchh desde Braze, no se pueden eliminar. Solo se pueden añadir nuevos invitados a un Segment personalizado existente. Si es necesario eliminar invitados de un Segment personalizado de Punchh existente, será necesario crear una nueva campaña de webhook en Braze para enviar usuarios a un nuevo Segment personalizado de Punchh.

## Integración {#integration}

Punchh ofrece varios endpoints disponibles para los clientes de Braze para ayudar a agregar ID externos a la plataforma Punchh utilizando los siguientes endpoints de la API de Punchh. Después de agregar los ID externos, crea un adaptador en Punchh, proporciona tus credenciales de Braze y selecciona qué eventos te gustaría sincronizar. A continuación, puedes tomar el ID de Segment de Punchh y usarlo para crear un webhook de Punchh que desencadene la sincronización de clientes en un recorrido de Canvas.

Ten en cuenta que el `user_id` de Punchh y el `external_id` de Braze deben estar disponibles en cualquiera de las dos plataformas para que la integración se sincronice correctamente.
- Los eventos enviados desde Punchh a Braze incluirán el `external_id` de Braze como identificador. Si Punchh está configurado para usar el `external_source_id`, ese valor se establecerá como el `external_id` de Braze. De lo contrario, la integración usará por defecto el `user_id` de Punchh como el `external_id` de Braze.
- Para enviar webhooks desde Braze a Punchh, el `user_id` de Punchh debe estar disponible en el perfil de usuario de Braze. Si el `user_id` de Punchh no se utiliza como el `external_id` de Braze, debe establecerse como un atributo personalizado "punchh_user_id".

### Paso 1: Configurar endpoints de ingesta de ID externo (opcional) {#step-1-set-up-external-id-ingestion-endpoints-optional}

Los ID externos de Braze se pueden agregar utilizando los siguientes endpoints para usuarios de Punchh nuevos y existentes.

{% alert important %}
Los valores de los campos `external_source` y `external_source_id` deben ser únicos en Punchh y no estar asociados con perfiles existentes.
{% endalert %}

1. Nuevos usuarios de Punchh<br>
Crea nuevos usuarios en Punchh con un endpoint de registro de Punchh utilizando los campos `external_source` y `external_source_id`. Punchh permite enviar identificadores externos con un perfil de usuario a través de uno de los siguientes endpoints de registro:
- [API de registro móvil](https://developers.punchh.com/docs/dev-portal-mobile/2e67abf6f8e12-sign-up-register)
- [API de registro inicio de sesión único](https://developers.punchh.com/docs/dev-portal-online-ordering/58f18dfdd2a3d-signup-with-email-and-password)<br><br>
2. Usuarios existentes de Punchh <br>
Actualiza el `external_source_id` para usuarios existentes de Punchh. Punchh permite agregar identificadores externos a un perfil a través de un endpoint de actualización de la API de usuario:
- [Actualización de usuario móvil](https://developers.punchh.com/docs/dev-portal-mobile/c9b928e35a6f3-update-user-profile)
- [Actualización de usuario inicio de sesión único](https://developers.punchh.com/docs/dev-portal-online-ordering/eef4eef6c97a0-update-user-information)
- [Actualización de usuario del panel](https://developers.punchh.com/docs/dev-portal-platform-functions/6351feaf591aa-update-a-user)
<br><br>
{% tabs local %}
{% tab User sign-up API example %}
Este ejemplo te permite enviar identificadores externos con un perfil de usuario en el momento del registro. Esto se hace enviando `external_source` como "customer_id" y `external_source_id` como "111111111111111111" como un tipo de datos de cadena.

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
Este ejemplo te permite actualizar identificadores externos con un perfil de usuario. Esto se hace enviando `external_source` como "customer_id" y `external_source_id` como "111111111111111111" como un tipo de datos de cadena.

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
**Configuración de la plataforma:** Para habilitar identificadores externos en Punchh, desde el panel de Punchh, navega a **Cockpit** > **Dashboard** > **External User Identifier**.
{% endalert %}

### Paso 2: Configuración del adaptador de Braze en Punchh {#step-2-braze-adapter-setup-in-punchh}

#### Eventos disponibles para sincronizar {#available-events-to-sync}

1. **Invitado:** Se desencadena ante cualquier registro, actualización del perfil de invitado, desactivación o eliminación
2. **Check-in de fidelización:** Se desencadena para transacciones de fidelización o acumulación al escanear el código de barras del recibo
3. **Check-in de regalo:** Se desencadena para puntos regalados desde una campaña
4. **Canje:** Se desencadena en caso de cualquier canje de recompensas excluyendo cupones de Punchh, ya que estos se enviarían por separado como eventos de cupón, incluyendo tanto la emisión como el canje
5. **Recompensas:** Se desencadena desde recompensas otorgadas por campañas, actividad, conversión de puntos a recompensas u otorgamiento por administrador
6. **Notificaciones de transacción:** Se desencadena ante la actividad transaccional de un usuario dentro del sistema Punchh (por ejemplo, expiración de puntos)
7. **Notificaciones de marketing:** Se desencadena en función de diferentes configuraciones de campañas en Punchh para un Segment asociado de usuarios

{% alert note %}
Consulta la documentación de Punchh para ver cómo son las cargas útiles de ejemplo para estos eventos disponibles.
{% endalert %}

Trabaja con tu administrador de implementación de Punchh para configurar este adaptador.

Para configurar la integración de Braze y Punchh, haz lo siguiente:

1. En el panel de Punchh, navega a **Cockpit** > **Dashboard** > **Major Features** > **Enable Webhook Management** y activa **Enable Webhook Management**.<br><br>
2. A continuación, habilita los adaptadores navegando a **Settings** > **Webhooks Administrador** > **Configurations** > **Show Adapters Tab** y activa **Show Adapters Tab**.<br><br>
3. Navega a **Webhooks Manager** en la pestaña **Settings**, selecciona la pestaña **Adapters** y haz clic en **Create Adapter**. <br><br>![Pestaña de adaptadores del Webhooks Manager de Punchh con Create Adapter seleccionado.]({% image_buster /assets/img/punchh/punchh1.png %})<br><br>
4. Completa el nombre del adaptador, la descripción y el correo electrónico del administrador. Selecciona **Braze** como tu adaptador y proporciona tu endpoint de la REST API de Braze y tu clave de API de Braze.<br><br>
5. A continuación, selecciona los eventos disponibles que deseas habilitar. Puedes encontrar una lista de estos eventos en [Eventos disponibles para sincronizar](#available-events-to-sync).<br><br>![Configuración del adaptador Punchh mostrando los eventos seleccionables para la sincronización con Braze.]({% image_buster /assets/img/punchh/punchh3.png %})<br><br>
6. Haz clic en **Submit** para habilitar el webhook.

## Crear un webhook de Punchh en Braze {#create-punchh-webhook-in-braze}

Braze puede agregar usuarios a un Segment de Punchh a través de webhooks utilizando los Custom Segments de Punchh.

1. Crea un Segment personalizado en Punchh y anota el `custom_segment_id` presente en la URL del panel de Segments de Punchh, como se muestra en el siguiente ejemplo. Puedes utilizar tanto el constructor de Segments clásico como el beta. Sin embargo, se recomienda el beta, ya que el clásico acabará dejando de estar disponible.<br><br>En la plataforma Punchh, navega a **Guest** > **Segment** > **Custom List** > **New Custom List**.<br><br>![Panel de Segments personalizados de Punchh mostrando el ID del Segment personalizado en la URL.]({% image_buster /assets/img/punchh/update1.png %})<br><br>

2. Crea una Campaign de webhook en Braze utilizando el endpoint de Punchh para agregar un usuario a un Segment personalizado como la URL del webhook. Aquí puedes proporcionar el `custom_segment_id` extraído de la URL y el `user_id` como pares clave-valor.<br><br>![Creador de webhooks de Braze con el endpoint de Punchh y los campos de carga útil de pares clave-valor.]({% image_buster /assets/img/punchh/punchh4.png %})<br><br>

3. Este webhook puede configurarse como una Campaign individual o como un paso dentro de un Canvas. Alternativamente, si el webhook que agrega usuarios a este Segment de Punchh específico se utilizará en múltiples Campaigns o Canvas, puede configurarse como una [plantilla]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates).<br><br>
La clave `user_id` dentro del webhook se mapea al ID de usuario de Punchh. Este identificador deberá añadirse a todos los webhooks creados en Braze para agregar usuarios a un Segment personalizado de Punchh. El atributo personalizado `punch_user_id` puede rellenarse dinámicamente como el valor de la clave `user_id` usando [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid#pre-formatted-variables). Puedes insertar la variable del atributo personalizado `punchh_user_id` usando el icono azul de "más" en la barra de herramientas del campo de texto con plantilla.<br><br>![Campo de carga útil del webhook de Braze con la variable Liquid del ID de usuario de Punchh insertada.]({% image_buster /assets/img/punchh/update3.png %}){: style="max-width:65%;"}<br><br>![Selector de personalización de Braze mostrando el atributo personalizado punchh_user_id.]({% image_buster /assets/img/punchh/update4.png %}){: style="max-width:65%;"}<br><br>

4. Una vez guardado el webhook, puede utilizarse para sincronizar usuarios. Por ejemplo, 136 invitados se agregarían al Segment personalizado de Punchh cuando se lance esta Campaign de webhook de Braze.<br><br>![Un ejemplo de sincronización de usuarios utilizando el webhook guardado gracias a la integración de Braze y Punchh.]({% image_buster /assets/img/punchh/punchh6.png %})

Para obtener más información sobre cómo se utilizan los webhooks en Braze, consulta [Crear un webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook).

## Campaigns de ejemplo {#use-case-campaigns}

### Configuración de Campaign y Canvas {#campaign-and-canvas-configuration}

#### Desencadenamiento {#triggering}

Los ejemplos de mensajería de Braze desencadenados por eventos de Punchh enviados a Braze, como eventos de recompensa o eventos de invitados, pueden crearse como [Campaigns basadas en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) o Canvas desencadenados por el evento Punchh relevante.

Al añadir un desencadenador, se mostrará la lista de eventos creados en Braze. Elige el evento que debe desencadenar tu Campaign o Canvas para que se envíe al usuario que registró el evento.

![Configuración de desencadenamiento en Braze mostrando un evento Punchh seleccionado para una Campaign basada en acciones.]({% image_buster /assets/img/punchh/update5.png %})

Se pueden añadir filtros de propiedad para filtrar aún más el evento desencadenante. Por ejemplo, el mensaje solo debería desencadenarse cuando un cliente activa el evento "checkins_gift" donde la propiedad del evento aprobado es `true`. Esta es una característica opcional que puede no ser aplicable a todos los ejemplos.

#### Segmentación {#segmentation}

En muchos casos, las Campaigns y Canvas de Braze desencadenados por eventos de Punchh pueden configurarse con una audiencia de "Todos los usuarios", ya que la segmentación de los usuarios que desencadenan estos eventos se determina dentro de Punchh. Sin embargo, los clientes que busquen refinar aún más la audiencia de usuarios que recibirán la mensajería de Braze desencadenada por el evento pueden hacerlo añadiendo filtros y Segments adicionales en la sección **Target Audiences** del creador de Campaign o el **público de entrada** del creador de Canvas.

### Ejemplos {#use-cases}

{% tabs local %}
{% tab Registro %}
#### Campaign de registro {#sign-up-campaign}

Al utilizar la configuración de Braze para una campaña de registro con una oferta adjunta, será necesario configurar una campaña de regalo de registro dentro de Punchh y un mensaje de bienvenida en Braze.

Punchh recomienda que se añada un retraso de ejecución a la campaña de registro, para que Braze pueda primero desencadenar el mensaje de bienvenida basado en el evento de invitado. Si deseas enviar un mensaje de seguimiento informando al usuario de que ha recibido un regalo, puedes desencadenarlo basándote en el evento de recompensa.

En el caso de una campaña de registro, se puede utilizar "todos los registrados" para el Segment; por lo tanto, no se requerirá un Segment personalizado de Braze.

Configuraciones de Punchh requeridas:
- Campaign: Registro
- Segment: Todos los registrados
- Recompensa: Elección del cliente
Eventos requeridos:
- Evento de recompensa
- Evento de invitado
Consideraciones:
- Retraso de ejecución, se recomienda que el invitado añada un retraso de 5 a 10 minutos

![Un Segment de usuario se configura en Punchh, y los invitados se registran en un programa de fidelización. Después de esto, se desencadena el evento de invitado y la Campaign de mensajería de Braze. A continuación, la campaña de regalo de registro de Punchh se desencadena después de 10 minutos, activando el evento de recompensa y el mensaje de seguimiento opcional.]({% image_buster /assets/img/punchh/usecase3.png %})
{% endtab %}

{% tab Bienvenida de Braze %}
#### Campaign de bienvenida de Braze {#braze-welcome-campaign}

Cuando un nuevo usuario se registra, Punchh envía a Braze un evento de invitado que crea al usuario y envía un atributo personalizado `signup_channel`, que puedes utilizar para desencadenar la Campaign de bienvenida de Braze.

Para configurar la Campaign de bienvenida de Braze, sigue estos pasos:

1. En Braze, crea una Campaign basada en acciones.
2. Para el desencadenador, selecciona **Change Custom Attribute Value** con el atributo personalizado `signup_channel` configurado como **Any new value**.
3. Continúa creando tu Campaign y ¡envíala cuando esté lista!

{% endtab %}
{% tab Oferta masiva %}
#### Campaign de oferta masiva {#mass-offer-campaign}

Al utilizar una campaña de oferta masiva para regalos, será necesario configurar una campaña de oferta masiva dentro de Punchh y una Campaign de mensajería en Braze.

Si deseas utilizar un Segment de Braze para tu Campaign o enviar comunicación desde Braze antes de regalar a los invitados en la plataforma Punchh, se requerirá un [Segment personalizado de Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh#step-3-create-punchh-webhook-in-braze) para la campaña de regalos de Punchh.

Se recomienda crear el Segment de usuarios que recibirán esta oferta en Braze solo cuando se utilicen atributos no disponibles dentro de Punchh. De lo contrario, se puede utilizar la segmentación de Punchh, y la Campaign de mensajería de Braze se creará como una Campaign basada en acciones desencadenada por los usuarios que reciben su recompensa (el evento de recompensa desencadenado por Punchh).

Configuraciones de Punchh requeridas:
- Campaign: Oferta masiva
- Segment: Lista personalizada o elección del cliente
- Recompensa: Elección del cliente

**Uso de Punchh para segmentación y regalos, y Braze para mensajería:**<br>
Por ejemplo, una recompensa de $2 de descuento se envía a un Segment configurable dentro de Punchh con mensajería enviada a través de Braze.<br>
![Un Segment de usuario se puede configurar en Punchh, y los usuarios reciben un regalo a través de una campaña de oferta masiva de Punchh. A continuación, se desencadena un evento de recompensa y luego se desencadena la Campaign de mensajería de Braze.]({% image_buster /assets/img/punchh/usecase6.png %}){: style="max-width:80%;"}

**Uso de segmentación y mensajería de Braze, y Punchh para regalos:**<br>
Por ejemplo, una recompensa de $2 de descuento y mensajería enviada a un Segment con atributos no disponibles en Punchh.<br>
![Un Segment de usuario se puede configurar en Braze, y luego se puede enviar un mensaje desde un Segment de Braze a Braze. A continuación, los usuarios se envían al Segment personalizado de Punchh a través de un webhook de Braze con el Segment y el ID de usuario. Después de esto, el usuario recibe un regalo a través de la campaña de oferta masiva de Punchh con un Segment personalizado. Después de esto, se desencadena el evento de recompensa.]({% image_buster /assets/img/punchh/usecase5.png %}){: style="max-width:80%;"}

**Uso de segmentación de Braze y Punchh para regalos o mensajería, o ambos:**<br>
Por ejemplo, una recompensa de $2 de descuento se envía a un Segment con atributos no disponibles en Punchh, pero no se requiere mensajería, o la mensajería puede enviarse a través de Punchh (ten en cuenta que todos los invitados deben estar presentes en Punchh).<br>
![Un Segment de usuario se puede configurar en Braze, y los usuarios se envían al Segment personalizado de Punchh a través de un webhook de Braze con el Segment y el ID de usuario. Después de esto, el usuario recibe un regalo a través de la campaña de oferta masiva de Punchh con un Segment personalizado. Después de esto, se desencadena el evento de recompensa.]({% image_buster /assets/img/punchh/usecase4.png %})

{% endtab %}
{% tab Oferta masiva recurrente %}
#### Campaign de oferta masiva recurrente {#recurring-mass-offer-campaign}

Al utilizar una campaña de oferta masiva recurrente para regalos, será necesario configurar una campaña de oferta masiva dentro de Punchh y una Campaign de mensajería en Braze. Se requerirá un Segment personalizado de Punchh si el cliente desea utilizar la segmentación de Braze (solo se recomienda si se utilizan atributos no disponibles dentro de Punchh). De lo contrario, se puede utilizar la segmentación de Punchh, y la Campaign de mensajería de Braze se desencadenará basándose en el evento de recompensa.

Configuraciones de Punchh requeridas:
- Campaign: Oferta masiva recurrente
- Segment: Lista personalizada o elección del cliente
- Recompensa: Elección del cliente
Consideraciones:
- Los ID de Campaign y los nombres de Campaign se envían a Braze como propiedad del evento. Si deseas utilizar un identificador de campaña de Punchh en Braze para filtrar aún más la audiencia que recibe la Campaign, debes utilizar el nombre de la campaña, ya que los ID de Campaign cambian diariamente.

{% endtab %}
{% tab Oferta post check-in con notificación %}
#### Campaign de oferta post check-in con notificación {#post-check-in-offer-campaign-with-notification}

Al utilizar una campaña de oferta post check-in, Braze enviará la notificación sobre el regalo, y cuando el invitado realice un check-in, recibirá el regalo de la campaña post check-in de Punchh. Por lo tanto, será necesario configurar una campaña de oferta post check-in dentro de Punchh y una Campaign de mensajería en Braze (si se notifica a los clientes sobre la campaña).

Configuraciones de Punchh requeridas:
- Campaign: Oferta post check-in
- Segment: Lista personalizada
- Recompensa: Elección del cliente

Por ejemplo, un correo electrónico notificando a los invitados que visiten este fin de semana para obtener puntos dobles a un Segment con atributos no disponibles en Punchh. Punchh regalará puntos a este Segment después de un check-in válido y mensajería opcional desde Braze.

![Un Segment de usuario se configura en Braze, y se envían mensajes desde la Campaign post check-in de Braze. A continuación, los usuarios válidos se envían al Segment personalizado de Punchh a través de un webhook de Braze con el Segment y el ID de usuario. Por último, el usuario válido en el Segment personalizado realiza el check-in y recibe el regalo y el mensaje opcional a través de la campaña post check-in.]({% image_buster /assets/img/punchh/update7.png %})

{% endtab %}
{% tab Oferta post check-in sin notificación %}
#### Campaign de oferta post check-in sin notificación {#post-check-in-offer-campaign-without-notification}

Al utilizar una campaña de oferta post check-in que no notifica primero a los clientes, la campaña regalará (mensajería opcional) y desencadenará cualquier notificación dentro de Braze. Por lo tanto, se debe configurar una campaña de oferta post check-in dentro de Punchh; sin embargo, no se requiere una lista personalizada. En su lugar, puedes elegir el Segment que desees dentro de Punchh.

Configuraciones de Punchh requeridas:
- Campaign: Oferta post check-in
- Segment: Elección del cliente
- Recompensa: Elección del cliente

Por ejemplo, una Campaign de sorpresa y agrado de Braze se envía a un Segment disponible en Punchh, agradeciendo a los invitados su visita y recompensándolos con $2 de descuento en su próxima visita.

![Un Segment de usuarios válidos se puede configurar dentro de Punchh, y un usuario válido realiza el check-in y recibe un regalo a través de una campaña post check-in de Punchh. Después de esto, se desencadena un evento de recompensa y se envía el mensaje de recordatorio notificando a los invitados sobre la recompensa enviada desde Braze.]({% image_buster /assets/img/punchh/usecase2.png %})

{% endtab %}
{% tab Aniversario %}
#### Campaign de aniversario {#anniversary-campaign}

Al utilizar una campaña de aniversario, primero se regalará al usuario por su aniversario desde la campaña de Punchh. Este regalo (evento de recompensa) desencadenará la Campaign de mensajería dentro de Braze que notifica al usuario sobre el regalo. Por lo tanto, no se requiere una lista personalizada. En su lugar, puedes elegir el Segment y la configuración de aniversario dentro de Punchh.

Configuraciones de Punchh requeridas:
- Campaign: Campaña de aniversario
- Segment: Elección del cliente
- Recompensa: Elección del cliente
Consideraciones:
- Mes de regalo del registro
- Duración de vigencia (¿Cuánto tiempo es válida la recompensa de cumpleaños?)
- Campañas recurrentes, se requiere programación

![Se puede crear un Segment opcional dentro de Punchh, y un usuario válido recibe una recompensa a través de una campaña de aniversario de Punchh. Después de esto, se desencadena un evento de recompensa y se envía el mensaje de recordatorio notificando a los invitados sobre la recompensa enviada desde Braze.]({% image_buster /assets/img/punchh/usecase1.png %})

{% endtab %}
{% tab Recuperación %}
#### Campaign de recuperación {#recall-campaign}

Al dirigirse a usuarios basándose en la inactividad, se puede utilizar una campaña de recuperación. El cliente puede crear el Segment y la campaña dentro de Punchh, pero utilizar Braze para la mensajería.

Si deseas utilizar la segmentación creada en Braze, se puede adjuntar un [Segment personalizado de Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh#step-3-create-punchh-webhook-in-braze) basado en la inactividad a una campaña de oferta masiva recurrente.

Configuraciones de Punchh requeridas:
- Campaign: Campaña de recuperación
- Segment: Elección del cliente
- Recompensa: Elección del cliente
Consideraciones:
- La campaña se ejecuta según un horario programado

![Se puede crear un Segment opcional dentro de Punchh, y un usuario válido recibe una recompensa a través de una campaña de recuperación de Punchh. Después de esto, se desencadena un evento de recompensa y se envía el mensaje de recuperación notificando a los invitados sobre la recompensa enviada desde Braze.]({% image_buster /assets/img/punchh/usecase.png %})

{% endtab %}
{% endtabs %}