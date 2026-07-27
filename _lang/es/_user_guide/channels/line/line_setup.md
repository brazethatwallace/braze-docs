---
nav_title: "Configuración"
article_title: Configuración de LINE
description: "Este artículo explica cómo configurar el canal LINE de Braze, incluidos los requisitos previos y los próximos pasos sugeridos."
page_type: partner
search_tag: Partner
page_order: 0
channel:
 - LINE
alias: /line/line_setup/
---


# Configuración de LINE {#line-setup}

> Este artículo explica cómo configurar el canal LINE en Braze, incluido cómo configurar usuarios, reconciliar ID de usuario y crear usuarios de prueba de LINE en Braze.

## Requisitos previos {#prerequisites}

Necesitarás lo siguiente para integrar LINE con Braze:

- [Cuenta empresarial de LINE](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- Estado de cuenta premium o verificada (necesario para sincronizar seguidores existentes)
   - Consulta las [directrices de cuentas de LINE](https://terms2.line.me/official_account_guideline_oth)
- [Cuenta de desarrollador de LINE](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [Canal de API de mensajería de LINE](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

El envío de mensajes de LINE desde Braze consume los créditos de mensaje o de acción de tu cuenta.

{% alert note %}
**Configurar `native_line_id`**: Puedes configurar `native_line_id` enviando actualizaciones de usuario a Braze (por ejemplo, con el [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), la [importación CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) o la [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)). Si tu SDK del lado del cliente no tiene un campo dedicado para `native_line_id`, envíalo en las actualizaciones de usuario del lado del servidor utilizando uno de estos métodos.
{% endalert %}

## Tipos de cuentas LINE {#types-of-line-accounts}

| Tipo de cuenta | Descripción |
| --- | --- |
| Cuenta no verificada | Una cuenta no revisada que cualquier persona (individual o corporativa) puede obtener. Esta cuenta se representa con una señal gris y no aparecerá en los resultados de búsqueda dentro de la aplicación LINE. |
| Cuenta verificada | Una cuenta que ha pasado la revisión de LINE Yahoo. Esta cuenta se representa con una señal azul y aparecerá en los resultados de búsqueda dentro de la aplicación LINE.<br><br>Esta cuenta solo está disponible para cuentas con sede en Japón, Taiwán, Tailandia e Indonesia. |
| Cuenta premium | Una cuenta que ha pasado la revisión de LINE Yahoo. Esta cuenta se representa con una señal verde y aparecerá en los resultados de búsqueda dentro de la aplicación LINE. Este tipo de cuenta se otorga automáticamente durante la revisión a discreción de LINE. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de cuentas LINE" }

### Tipo de cuenta requerido {#required-account-type}

Para sincronizar seguidores en Braze, tu cuenta LINE debe estar verificada o ser premium. Cuando creas una cuenta, su estado predeterminado será no verificada. Tendrás que solicitar la verificación de la cuenta.

### Solicitar una cuenta LINE verificada {#applying-for-a-verified-line-account}

{% alert important %}
Las cuentas verificadas solo están disponibles para cuentas con sede en Japón, Taiwán, Tailandia e Indonesia.
{% endalert %}

1. En la página de **Official Account** de LINE, selecciona **Settings**.
2. En **Information Disclosure Verification Status**, selecciona **Request Account Verification**.
3. Introduce la información requerida.
4. Espera una notificación con los resultados de la revisión.

## Integración de LINE {#integrating-line}

Para configurar actualizaciones de usuario consistentes, importar los ID de LINE de los usuarios existentes y sincronizarlos todos con los estados de suscripción de LINE:

1. [Importar o actualizar usuarios de LINE existentes conocidos](#step-1-import-or-update-existing-line-users)
2. [Integrar el canal de LINE](#step-2-integrate-line-channel)
3. [Conciliar los ID de usuario](#step-3-reconcile-user-ids)
4. [Cambiar los métodos de actualización de usuarios](#step-4-change-your-user-update-methods)
5. [(Opcional) Fusionar perfiles de usuario](#step-5-merge-profiles-optional)

{% alert note %}
Solo puedes tener una cuenta de LINE en un único espacio de trabajo. Si tienes varias cuentas de LINE, te recomendamos usar cada una en un espacio de trabajo diferente.
{% endalert %}

## Paso 1: Importar o actualizar usuarios LINE existentes {#step-1-import-or-update-existing-line-users}

Este paso es necesario si tienes un usuario LINE existente e identificado, ya que Braze posteriormente extraerá automáticamente su estado de suscripción y actualizará el perfil de usuario correcto. Si no has reconciliado previamente a los usuarios con su ID de LINE, omite este paso.

Puedes importar o actualizar usuarios utilizando cualquiera de los métodos que Braze admite, incluido el endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), la [importación CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) o la [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

Independientemente del método que utilices, actualiza `native_line_id` para proporcionar el ID de LINE del usuario. Para obtener más información sobre `native_line_id`, consulta [Configuración de usuario](#user-setup).

{% alert note %}
No se debe especificar el estado del grupo de suscripción, y será ignorado. LINE es la fuente de verdad para el estado de suscripción del usuario, que se sincronizará con Braze a través de la herramienta de sincronización de suscripciones o mediante actualizaciones de eventos.
{% endalert %}

## Paso 2: Integrar el canal de LINE {#step-2-integrate-line-channel}

Una vez que se complete el proceso de integración, Braze extraerá automáticamente los seguidores de LINE de ese canal a Braze. Para cualquier ID de LINE que ya esté asociado con un perfil de usuario de Braze, cada perfil se actualizará con el estado "subscribed", y cualquier ID de LINE restante generará usuarios anónimos. Además, los nuevos seguidores de tu canal de LINE tendrán perfiles de usuario no identificados creados cuando sigan el canal.

### Paso 2.1: Editar la configuración del webhook {#step-21-edit-webhook-settings}

1. En LINE, ve a la pestaña **Messaging API** y edita tu **Webhook settings**:
   - Establece la **Webhook URL** en `https://anna.braze.com/line/events`.
      - Braze cambiará automáticamente esta URL a una diferente durante la integración, según el clúster de tu panel.
   - Activa **Use webhook** y **Webhook redelivery**. <br><br> ![Página de configuración de webhook para verificar o editar la URL del webhook, con opciones para activar o desactivar "Use webhook", "Webhook redelivery" y "Error statistics aggregation".]({% image_buster /assets/img/line/webhook_settings.png %}){: style="max-width:70%;"}
2. Toma nota de la siguiente información en la pestaña **Providers**:

| Tipo de información | Ubicación |
| --- | --- |
| Provider ID | Selecciona tu proveedor y luego ve a ***Settings** > **Basic information** |
| Channel ID | Selecciona tu proveedor y luego ve a **Channels** > tu canal > **Basic settings** |
| Channel secret | Selecciona tu proveedor y luego ve a **Channels** > tu canal > **Basic settings**. |
| Channel access token | Selecciona tu proveedor y luego ve a **Channels** > tu canal > **Messaging API**. Si no hay un token de acceso al canal, selecciona **Issue**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2.1: Editar la configuración del webhook" }

{% alert note %}
Puedes actualizar o rotar el channel secret y el channel access token de un canal de LINE ya integrado yendo a **Integraciones de partners** > **Partners tecnológicos** > **LINE** y seleccionando tu integración.
{% endalert %}

{: start="3"}
3. Ve a tu página de **Settings** > **Response settings** y haz lo siguiente:
   - Desactiva **Greeting message**. Esto se puede gestionar en Braze activándolo al seguir.
   - Desactiva **Auto-response messages**. Toda la mensajería activada debe realizarse a través de Braze. Esto no te impedirá enviar directamente desde la consola de LINE.
   - Activa **Webhooks**.

![Página de configuración de respuestas con opciones para gestionar cómo tu cuenta maneja los chats.]({% image_buster /assets/img/line/response_settings.png %}){: style="max-width:80%;"}

### Paso 2.2: Generar grupos de suscripción de LINE en Braze {#step-22-generate-line-subscription-groups-in-braze}

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

1. Ve a la página de partners tecnológicos de Braze para LINE e introduce la información que anotaste de la pestaña **Providers** de LINE:
   - Provider ID
   - Channel ID
   - Channel secret
   - Channel access token

Si deseas añadir listas blancas de IP en tu cuenta de LINE, agrega todas las direcciones IP listadas para tu clúster en [Lista de IP permitidas]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting) a tu lista de permitidos.

{% alert important %}
Durante la integración, asegúrate de verificar que tu channel secret sea correcto. Si es incorrecto, puede haber inconsistencias en el estado de la suscripción.
{% endalert %}

![Página de integración de mensajería de LINE con la sección de integración de LINE.]({% image_buster /assets/img/line/integration.png %}){: style="max-width:80%;"}

{: start="2"}
2. Después de conectar, Braze generará automáticamente un grupo de suscripción de Braze para cada integración de LINE que se haya añadido correctamente a tu espacio de trabajo. <br><br> Cualquier cambio en tu lista de seguidores (como nuevos seguidores o personas que dejan de seguir) se enviará automáticamente a Braze.

![Sección de grupos de suscripción de LINE que muestra un grupo de suscripción para el canal "LINE".]({% image_buster /assets/img/line/line_subscription_groups.png %}){: style="max-width:80%;"}

## Paso 3: Reconciliar los ID de usuario {#step-3-reconcile-user-ids}

Combina los ID de LINE de tus usuarios con sus perfiles de usuario de Braze existentes siguiendo los pasos en [Reconciliación de ID de usuario](#user-id-reconciliation).

## Paso 4: Cambia tus métodos de actualización de usuarios {#step-4-change-your-user-update-methods}

Suponiendo que ya tienes un método para proporcionar actualizaciones de usuarios a Braze, necesitarás actualizarlo para incluir el nuevo campo `native_line_id` de modo que las actualizaciones de usuarios posteriores enviadas a Braze incluyan ese campo.

Es posible que existan en Braze perfiles de usuario no identificados con un `native_line_id` que se crearon como parte del proceso de sincronización del estado de suscripción, o cuando un nuevo seguidor siguió tu canal.

Cuando un usuario de LINE es identificado en tu aplicación a través de la [reconciliación de usuarios](#user-id-reconciliation) u otros medios, puedes dirigirte a un perfil de usuario potencialmente no identificado en Braze utilizando el endpoint [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify). Cada perfil de usuario no identificado con un `native_line_id` también tiene un alias de usuario `line_id` que se puede utilizar para dirigirse al perfil de usuario a identificar.

A continuación se muestra un ejemplo de carga útil para `/users/identify` que se dirige a un perfil de usuario no identificado mediante el alias de usuario `line_id`:

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

Si no existe un perfil de usuario para el `external_id` proporcionado, se añadirá al perfil de usuario no identificado, convirtiéndolo en identificado. Si ya existe un perfil de usuario para el `external_id`, todos los atributos que sean exclusivos del perfil de usuario no identificado se copiarán al perfil de usuario conocido, incluyendo `native_line_id` y el estado de suscripción del usuario.

Puedes actualizar los usuarios de LINE que son conocidos en tu aplicación a través del endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) pasando sus identificadores externos y `native_line_id`. Si ya existe un perfil de usuario no identificado para un usuario y se añade el mismo `native_line_id` a un perfil de usuario diferente a través de `/users/track`, este heredará todos los estados de suscripción del perfil de usuario no identificado. Sin embargo, existirán perfiles de usuario duplicados con el mismo `native_line_id`. Cualquier actualización de suscripción posterior proveniente de actualizaciones de eventos actualizará todos los perfiles en consecuencia.

{% alert note %}
Los estados de suscripción de LINE se rastrean por `native_line_id`, no por `external_id`. Por ejemplo, si el perfil de usuario del Usuario B se crea con el mismo `native_line_id` que el Usuario A, pero no con el mismo `external_id`, el Usuario B hereda el estado de suscripción de LINE del Usuario A.
{% endalert %}

A continuación se muestra un ejemplo de carga útil para `/users/track` que actualiza un perfil de usuario mediante el ID externo de usuario para añadir un `native_line_id`:

{% raw %}
```json
{
   "attributes": [
       {
           "external_id": "known_external_id_from_your_application",
           "native_line_id": "U89f4a626548ccd48482f529a482f138b",
           "other": "attribute"
       }
   ]
}
```
{% endraw %}

## Paso 5: Fusionar perfiles (opcional) {#step-5-merge-profiles-optional}

Como se describió anteriormente en esta sección, existe la posibilidad de que existan múltiples perfiles de usuario con el mismo `native_line_id`. Si tus métodos de actualización crean perfiles de usuario duplicados, puedes fusionar perfiles de usuario no identificados con perfiles de usuario identificados mediante el endpoint `/user/merge`.

Aquí tienes un ejemplo de carga útil para `/users/merge` que apunta a un perfil de usuario no identificado por alias de usuario `line_id`:

{% raw %}
```json
{
 "merge_updates": [
   {
     "identifier_to_merge": {
       "user_alias": {
         "alias_name": "U89f4a626548ccd48482f529a482f138b",
         "alias_label": "line_id"
       }
     },
     "identifier_to_keep": {
       "external_id": "known_external_id_from_your_application"
     }
   }
 ]
}
```
{% endraw %}

{% alert tip %}
Para obtener más información sobre la gestión de usuarios duplicados en Braze, consulta [Usuarios duplicados]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).
{% endalert %}

## Configuración de usuarios {#user-setup}

LINE es la fuente de verdad para los estados de suscripción de los usuarios. Incluso si tienes el ID de LINE de un usuario (`native_line_id`), si ese usuario no ha seguido el canal de LINE desde el que estás enviando, LINE no entregará mensajes al usuario.

Para ayudar a gestionar esto, Braze ofrece herramientas y lógica que respaldan una base de usuarios bien integrada, incluyendo la sincronización de suscripciones y las actualizaciones de eventos para seguimientos y cancelaciones de seguimiento en LINE.

### Sincronización de suscripciones y lógica de eventos {#subscription-syncing-and-event-logic}

1. **Herramienta de sincronización de suscripciones:** Esta herramienta se despliega automáticamente tras una integración exitosa del canal de LINE. Úsala para actualizar perfiles existentes y crear nuevos perfiles.<br><br>Todos los perfiles de usuario de Braze que tengan un `native_line_id` que siga el canal de LINE se actualizarán para tener un estado del grupo de suscripción de `subscribed`. Cualquier seguidor del canal de LINE que no tenga un perfil de usuario de Braze con el `native_line_id` tendrá:<br><br>- Un perfil de usuario anónimo creado con `native_line_id` establecido como el ID de LINE del usuario que sigue el canal <br>- Un alias de usuario `line_id` establecido como el ID de LINE del usuario que sigue el canal <br>- Un estado del grupo de suscripción de `subscribed`

{: start="2"}
2. **Actualizaciones de eventos:** Se utilizan para actualizar el estado de suscripción de un usuario. Cuando Braze recibe actualizaciones de eventos de usuario para el canal de LINE integrado y el evento es un seguimiento, el perfil de usuario tendrá un estado del grupo de suscripción de `subscribed`. Si el evento es una cancelación de seguimiento, el perfil de usuario tendrá un estado del grupo de suscripción de `unsubscribed`.<br><br>- Todos los perfiles de usuario de Braze con un `native_line_id` coincidente se actualizarán automáticamente. <br>- Si no existe un perfil de usuario coincidente para un evento, Braze [creará un usuario anónimo]({{site.baseurl}}/line/user_management).

## Reintegrar un canal de LINE en otro espacio de trabajo {#re-integrate-a-line-channel-in-another-workspace}

Para usar un canal de LINE en un espacio de trabajo de Braze diferente:

1. En el espacio de trabajo original, archiva el grupo de suscripción de ese canal.
2. En el espacio de trabajo de destino, integra el canal siguiendo el [Paso 2: Integrar el canal de LINE](#step-2-integrate-line-channel).

Confirma que tienes el permiso [Gestionar grupos de suscripción]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions) en ambos espacios de trabajo. Sin permisos en ambos espacios de trabajo, la integración falla con un error que indica que el canal ya está conectado.

Para saber cómo el archivado afecta a los grupos de suscripción, consulta [Grupos de suscripción de LINE]({{site.baseurl}}/line/subscription_groups#archive-behavior).

## Ejemplos {#use-cases}

Estos son ejemplos de cómo se pueden actualizar los usuarios después de seguir los pasos de configuración.

### Un perfil de usuario de Braze existente ya sigue el canal de LINE {#existing-braze-user-profile-already-follows-line-channel}

1. El perfil de usuario de Braze se actualiza con un atributo `native_line_id`. Su estado de suscripción predeterminado es `unsubscribed`.
2. Se ejecuta la herramienta de sincronización de suscripciones, detecta que el usuario sigue el canal de LINE y luego actualiza el perfil de usuario con el estado de suscripción `subscribed`.
3. Si se produce algún cambio en el estado de suscripción (como que el usuario bloquee, elimine de amigos o vuelva a seguir el canal), Braze recibe la actualización de LINE y actualiza el perfil de usuario con el `native_line_id` correspondiente.

### Un perfil de usuario existente ha bloqueado, eliminado de amigos o dejado de seguir el canal de LINE {#existing-user-profile-has-blocked-unfriended-or-unfollowed-line-channel}

1. El perfil de usuario de Braze se actualiza con un atributo `native_line_id`. Su estado de suscripción predeterminado es `unsubscribed`.
2. La herramienta de sincronización de suscripciones no detecta que el usuario siga el canal de LINE y el estado de suscripción del usuario permanece como `unsubscribed`.
3. Si el usuario sigue el canal más adelante, Braze recibe la actualización de LINE y actualiza el perfil de usuario con el estado de suscripción `subscribed`.

### La creación del perfil de usuario ocurre después de seguir en LINE {#user-profile-creation-occurs-after-line-follow}

1. El canal obtiene un nuevo seguidor de LINE.
2. Braze crea un perfil de usuario anónimo con el atributo `native_line_id` establecido como el ID de LINE del seguidor, y un alias de usuario de `line_id` establecido como el ID de LINE del seguidor. El perfil tiene un estado de suscripción de `subscribed`.
3. El usuario es identificado como poseedor del ID de LINE a través de la [reconciliación de usuarios](#user-id-reconciliation).
  - El perfil de usuario anónimo puede ser identificado utilizando el endpoint [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify). Las actualizaciones posteriores (a través del endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), [importación CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) o [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)) a este perfil de usuario pueden dirigirse al usuario mediante este `external_id` conocido.

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

  - Se puede crear un nuevo perfil de usuario (a través del endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), [importación CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) o [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)) estableciendo el `native_line_id`. Este nuevo perfil heredará el estado de suscripción del perfil de usuario anónimo existente. Ten en cuenta que esto dará como resultado múltiples perfiles que comparten el mismo `native_line_id`. Estos se pueden fusionar en cualquier momento utilizando el endpoint `/users/merge` en el proceso descrito en el [Paso 5](#step-5-merge-profiles-optional).

### La creación del perfil de usuario ocurre antes de seguir en LINE {#user-profile-creation-occurs-before-line-follow}

1. Adquieres un nuevo usuario y envías la información a Braze. Se crea un nuevo perfil de usuario (perfil 1).
2. El usuario sigue tu cuenta de LINE.
3. Braze recibe un evento de seguimiento y crea un perfil de usuario anónimo (perfil 2).
4. El usuario es identificado como poseedor del ID de LINE a través de la [reconciliación de usuarios](#user-id-reconciliation).
5. Actualizas el perfil 1 para establecer el atributo `native_line_id`. Este perfil hereda el estado de suscripción del perfil 2.
  - Ahora hay dos perfiles de usuario con el mismo `native_line_id`. Estos se pueden fusionar en cualquier momento utilizando el endpoint `/users/merge` en el proceso descrito en el [Paso 5](#step-5-merge-profiles-optional).

## Reconciliación de ID de usuario {#user-id-reconciliation}

Los ID de LINE son recibidos automáticamente por Braze cuando un usuario sigue tu canal, o cuando utilizas el flujo de trabajo único de "sincronizar seguidores". Los ID de LINE también son específicos del canal que siguen los usuarios, por lo que es poco probable que los usuarios puedan proporcionar sus ID de LINE.

Hay dos formas de combinar un ID de LINE con un perfil de usuario existente en Braze:

- [Inicio de sesión con LINE](#line-login)
- [Vinculación de cuentas de usuario](#user-account-linking)

### Inicio de sesión con LINE {#line-login}

Este método utiliza inicios de sesión de redes sociales para la reconciliación. Cuando un usuario inicia sesión en tu aplicación, se le da la opción de usar [LINE Login](https://developers.line.biz/en/docs/line-login/overview/) para crear una cuenta de usuario o iniciar sesión.

{% alert note %}
Para adquirir el ID de LINE correcto para cada usuario, configura LINE Login bajo el mismo proveedor que tu cuenta oficial de LINE o canal integrado con Braze.
{% endalert %}

1. Ve a la consola para desarrolladores de LINE y [solicita permiso para obtener las direcciones de correo electrónico de los usuarios](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission) que inician sesión en tu aplicación a través de LINE Login.

2. Sigue los pasos apropiados proporcionados por LINE para implementar LINE Login:<br><br>
  - [Instrucciones para aplicaciones web](https://developers.line.biz/en/docs/line-login/integrate-line-login/)
  - [Instrucciones para aplicaciones nativas](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-openid-to-register-new-users)<br><br>Asegúrate de incluir `email` en la [configuración de alcance](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes) para las solicitudes de verificación.

{: start="3"}
3. Usa la [llamada de verificación de token de ID](https://developers.line.biz/en/reference/line-login/#verify-id-token) para adquirir el correo electrónico del usuario.

4. Guarda el ID de LINE del usuario (`native_line_id`) en el perfil del usuario con un correo electrónico coincidente en tu base de datos, o crea un nuevo perfil de usuario con el correo electrónico y el ID de LINE del usuario.

5. Envía la información de usuario nueva o actualizada a Braze usando el [endpoint `/user/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), [importación CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) o [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

#### Flujos de trabajo {#workflows}

##### Un seguidor existente usa LINE Login {#existing-follower-uses-line-login}

**Escenario:** Se creó un usuario anónimo durante la sincronización inicial de suscriptores o después de la integración a través de un evento de "seguir".

1. El usuario inicia sesión en tu aplicación usando LINE Login.
2. LINE te proporciona el correo electrónico del usuario.
3. Envías a Braze el usuario actualizado (el perfil de usuario existente con ese correo electrónico para agregar el ID de LINE) o actualizas el usuario anónimo con el correo electrónico.

##### Un nuevo seguidor usa LINE Login {#new-follower-uses-line-login}

**Escenario:** No existe ningún perfil de usuario en Braze con el ID de LINE del usuario.

1. El usuario inicia sesión en tu aplicación usando LINE Login.
2. LINE te proporciona el correo electrónico del usuario.
3. Puedes:
  - Actualizar un perfil de usuario existente con ese correo electrónico para que también tenga el ID de LINE del usuario.
  - Crear un nuevo perfil de usuario con el correo electrónico y el ID de LINE.
4. Cuando el usuario sigue tu cuenta oficial de LINE, Braze recibe un evento de seguimiento y actualiza el estado de suscripción del usuario a `subscribed`.

### Vinculación de cuentas de usuario {#user-account-linking}

Este método permite a los usuarios vincular su cuenta de LINE con la cuenta de usuario de tu aplicación. Luego puedes usar Liquid en Braze, como {% raw %}`{{line_id}}`{% endraw %}, para crear una URL personalizada para el usuario que pase el ID de LINE del usuario de vuelta a tu sitio web o aplicación, donde puede asociarse con un usuario conocido.

1. Crea un Canvas basado en acciones que se base en un cambio de estado de suscripción y se desencadene cuando un usuario se suscribe a tu canal de LINE.<br>![Canvas que se desencadena cuando un usuario se suscribe al canal de LINE.]({% image_buster /assets/img/line/account_link_1.png %})
2. Crea un mensaje que incentive a los usuarios a iniciar sesión en tu sitio web o aplicación, pasando el ID de LINE del usuario como parámetro de consulta (a través de Liquid), como:

```
Thanks for following Flash n' Thread on LINE! For personalized offers and 20% off your next purchase, sign-in to your account: https://flashandthread.com/sign_in?line_user_id={{line_id}}
```

{: start="3"}
3. Crea un mensaje de seguimiento que entregue el código de cupón.
4. (Opcional) Crea una Campaign o Canvas basado en acciones que se desencadene cuando el usuario de LINE sea identificado para enviarle su código de cupón. <br>![Campaign basada en acciones que se desencadena cuando el usuario de LINE es identificado.]({% image_buster /assets/img/line/account_link_2.png %})

#### Cómo funciona {#how-it-works}

Después de que el usuario inicia sesión, se realiza un cambio en tu sitio web o aplicación para que el ID de usuario se envíe de vuelta a Braze y se asocie con el ID de LINE que se pasó como parte de la URL, con un código de ejemplo como:

```javascript
const currentUrl = new URL(window.location.href)
const queryParams = new URLSearchParams(currentUrl.search);
const lineUserId = queryParams.get("line_user_id")

if (user && isLoggedIn && lineUserId) {
  post(
   "https://rest.iad-03.braze.com	/users/identify",
   {
     "aliases_to_identify": [
       {
   "external_id": user.getUserId(),
   "user_alias": {
     "alias_name": lineUserId,
     "alias_label": "line_id"
   }
 }
      ]
    }
  )
  braze.logCustomEvent("identified_line_user_for_promotion");
}
```

#### Flujos de trabajo

##### Un usuario existente sigue tu canal de LINE {#existing-user-follows-your-line-channel}

**Escenario:** Un usuario existente en Braze sigue tu canal en LINE.

1. LINE envía a Braze un evento de seguimiento.
2. Braze crea un perfil de usuario anónimo con el ID de LINE, el alias de usuario `line_id` y el estado del grupo de suscripción de LINE como `subscribed`.
3. El usuario recibe un mensaje de LINE con un enlace a tu sitio web y aplicación e inicia sesión. Su perfil de usuario ahora es conocido.
4. El perfil de usuario anónimo que se creó es identificado y se fusiona a través del [endpoint /users/identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) con el perfil de usuario conocido del usuario. El perfil de usuario conocido ahora contiene el ID de LINE y tiene un estado de suscripción de `subscribed`.
5. (Opcional) El usuario recibe un mensaje de LINE con el código de cupón y Braze registra el envío en el perfil de usuario de Braze.

## Creación de usuarios de prueba de LINE en Braze {#creating-line-test-users-in-braze}

Puedes probar tu canal de LINE antes de configurar la [reconciliación de usuarios](#user-id-reconciliation) creando un Canvas o Campaign de tipo "¿Quién soy?".

1. Configura un Canvas que devuelva el ID de usuario de Braze de un usuario con una palabra desencadenante específica. <br><br>Ejemplo de desencadenante <br><br>![Desencadenante para enviar la Campaign a usuarios que enviaron un LINE entrante a un grupo de suscripción específico.]({% image_buster /assets/img/line/trigger.png %}){: style="max-width:80%;"}<br><br>Ejemplo de mensaje<br><br>![Mensaje de LINE que muestra el ID de usuario de Braze.]({% image_buster /assets/img/line/message.png %}){: style="max-width:40%;"}<br><br>

2. En Braze, puedes usar el ID de Braze para buscar usuarios específicos y modificarlos según sea necesario.

{% alert important %}
Asegúrate de que el Canvas no tenga control global ni grupos de control que impidan los envíos.
{% endalert %}