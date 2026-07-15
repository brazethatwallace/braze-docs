---
nav_title: "Ciclo de vida del token de notificaciones push"
article_title: "Ciclo de vida del token de notificaciones push"
page_order: 1
page_type: reference
description: "Este artículo de referencia explica qué significa estar registrado para push y cómo enviamos mensajes push y gestionamos los tokens de notificaciones push y el registro push en Braze."
channel:
 - push

---

# Ciclo de vida del token de notificaciones push {#push-token-lifecycle}

> Este artículo cubre el proceso mediante el cual se asigna un token de notificaciones push a un usuario, y cómo Braze envía mensajes push a tus usuarios.

## Acerca de los tokens de notificaciones push {#push-tokens}

Cuando una aplicación solicita permisos push a un dispositivo, el proveedor de servicios push del dispositivo genera un token de notificaciones push para esa aplicación. Cada aplicación recibe su propio token de notificaciones push único y anónimo, que es la forma en que identifica al dispositivo y a la instancia de la aplicación actual al enviar una notificación push.

Ten en cuenta que los tokens de notificaciones push no son identificadores estáticos que duran para siempre&#8212;pueden actualizarse y pueden [caducar](#push-token-expire).

{% alert tip %}
Para detalles específicos de cada plataforma, consulta [Registro de tokens de notificaciones push](#push-token-registration).
{% endalert %}

### Push en primer plano vs. en segundo plano {#foreground-vs-background}

Los tokens de notificaciones push se utilizan para enviar tanto notificaciones push en primer plano como en segundo plano.

| Tipo       | ¿Requiere adhesión voluntaria? | Descripción                                                 |
|------------------|------------------|--------------------------------------------------------------------------------------------------------------|
| Push en primer plano | Sí       | Se muestra visiblemente una notificación al usuario mientras la aplicación está en primer plano.           |
| Push en segundo plano | No        | Una notificación se entrega silenciosamente en segundo plano sin mostrarse. Se utiliza a menudo para funcionalidades como Uninstall Tracking. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Push en primer plano vs. en segundo plano" }

Cuando un usuario acepta recibir notificaciones push de tu aplicación, se le considerará "registrado para push", lo que significa que ahora puede ser segmentado utilizando el filtro de segmentación `Foreground Push Enabled for App` en Braze.

{% alert note %}
Esto es diferente del filtro de segmentación `Foreground Push Enabled`, que se utiliza para identificar a los usuarios que han aceptado recibir notificaciones push en al menos una de tus aplicaciones, no en una aplicación específica. Para más información, consulta [Filtros de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#foreground-push-enabled).
{% endalert %}

### Múltiples usuarios en un dispositivo {#multiple-users-on-a-device}

Los tokens de notificaciones push son únicos tanto para el dispositivo como para la aplicación, lo que significa que los tokens de notificaciones push no pueden utilizarse para dirigirse a usuarios específicos si múltiples usuarios están usando el mismo dispositivo.

Por ejemplo, supongamos que tienes dos usuarios: Charlie y Kim. Si Charlie ha habilitado las notificaciones push para tu aplicación en su teléfono y Kim usa el teléfono de Charlie para cerrar la sesión del perfil de Charlie e iniciar sesión en el suyo, el token de notificaciones push se reasignará al perfil de Kim. El token de notificaciones push permanecerá asignado al perfil de Kim en ese dispositivo hasta que ella cierre sesión y Charlie vuelva a iniciar sesión.

Una aplicación o sitio web solo puede tener una suscripción push por dispositivo. Así que cuando un usuario cierra sesión en un dispositivo o sitio web, y un nuevo usuario inicia sesión, el token de notificaciones push se reasigna al nuevo usuario. Esto se refleja en el perfil del usuario en la sección **Configuración de contacto** de la pestaña **Interacción**:

![Registro de cambios del token de notificaciones push en la pestaña **Interacción** del perfil de un usuario, que muestra cuándo se movió el token de notificaciones push a otro usuario y cuál era el token.]({% image_buster /assets/img/push_token_changelog.png %})

Dado que no hay forma de que los proveedores push (APNs/FCM) distingan entre múltiples usuarios en un dispositivo, pasamos el token de notificaciones push al último usuario que inició sesión para determinar a qué usuario dirigirse en el dispositivo para push.

{% alert tip %}
Si ves un mensaje de error en **Configuración de contacto** > **Registro de cambios push**, consulta [Mensajes de error push comunes]({{site.baseurl}}/user_guide/channels/push/push_error_codes) para obtener explicaciones y los pasos a seguir.
{% endalert %}

## Registro de tokens de notificaciones push {#push-token-registration}

Cada plataforma de dispositivo gestiona el registro de tokens de notificaciones push de manera diferente. Consulta lo siguiente para detalles específicos de cada plataforma:

{% tabs local %}
{% tab web %}
Debes solicitar la adhesión voluntaria explícita de los usuarios a través del diálogo de permisos nativo del navegador. Recibirás un token después de que los usuarios acepten. A diferencia de iOS y Android, que permiten que tu aplicación muestre el aviso de permisos en cualquier momento, algunos navegadores modernos solo mostrarán el aviso si se activa mediante un "gesto del usuario" (clic del ratón o pulsación de tecla). Si tu sitio intenta solicitar permiso de notificaciones push al cargar la página, probablemente será ignorado o silenciado por el navegador.
{% endtab %}

{% tab android %}
Cuando se instala tu aplicación, se genera automáticamente un token de notificaciones push para ella&#8212;sin embargo, solo puede utilizarse para [notificaciones push en segundo plano](#foreground-vs-background) hasta que el usuario acepte explícitamente. Además, el registro se gestiona de manera diferente en las distintas versiones de Android:

| Versión       | Detalles                                                                                                                                                |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Android 13**         | El permiso push debe ser solicitado y concedido por el usuario. Tu aplicación puede solicitar el permiso manualmente, o los usuarios serán avisados automáticamente después de crear un [canal de notificaciones](https://developer.android.com/reference/android/app/NotificationChannel). |
| **Android 12 y anteriores** | Todos los usuarios se consideran `Subscribed` después de su primera sesión. Braze solicita automáticamente un token de notificaciones push en este punto, habilitando al usuario para push con un token válido y un estado de suscripción predeterminado de `Subscribed`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Registro de tokens de notificaciones push" }
{% endtab %}

{% tab ios %}
iOS no genera automáticamente tokens de notificaciones push para una aplicación cuando se instala. Además, el registro se gestiona de manera diferente en las distintas versiones de iOS:

| Versión                         | ¿Autorización provisional? | Detalles                                                                                                                                                     |
|------------------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **iOS 12**      | Sí                         | Cuando un usuario acepta las notificaciones push, se te otorga autorización estándar, lo que te permite enviar [notificaciones push en primer plano](#foreground-vs-background). Sin embargo, también puedes solicitar [autorización provisional]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options#provisional-push), que te permite enviar [notificaciones push en segundo plano](#foreground-vs-background) silenciosas directamente al centro de notificaciones. |
| **iOS 11 o anteriores** | No                          | Todos los usuarios deben aceptar explícitamente para recibir notificaciones push. Un token de notificaciones push se genera solo después de que se conceda el permiso.                                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Registro de tokens de notificaciones push" }
{% endtab %}
{% endtabs %}

### Comprobar el estado de suscripción push de un usuario {#checking-users-push-subscription-state}

![Perfil de usuario de Jane Doe que muestra el estado de suscripción push y los detalles de registro push en la pestaña Interacción.]({% image_buster /assets/img/push_implementation_guide/checking-users-push-subscription-state.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Hay dos formas de comprobar el estado de suscripción push de un usuario con Braze:

- **Perfil de usuario**: Puedes acceder a los perfiles de usuario individuales a través del dashboard de Braze en la página [Búsqueda de usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles). Después de encontrar el perfil de un usuario (mediante dirección de correo electrónico, número de teléfono o ID de usuario externo), puedes seleccionar la pestaña **Interacción** para ver y ajustar manualmente el estado de suscripción de un usuario.
- **Exportación de REST API**: Puedes exportar perfiles de usuario individuales en formato JSON utilizando los puntos finales de exportación [Usuarios por Segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) o [Usuarios por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier). Braze devolverá un objeto de tokens de notificaciones push que contiene información de habilitación push por dispositivo.

### Comprobar el estado de registro push {#checking-push-registration-status}

En la pestaña **Interacción** del perfil de un usuario, verás **Push registrado para** seguido del nombre de una aplicación. Si no existe información de la aplicación para ese dispositivo, verás dos guiones (**&#45;&#45;**). Habrá una entrada por cada dispositivo que pertenezca al usuario.

Si el nombre de la aplicación en la entrada del dispositivo tiene el prefijo `Foreground:`, la aplicación está autorizada para recibir tanto notificaciones push en primer plano (visibles para el usuario) como notificaciones push en segundo plano (no visibles para el usuario) en ese dispositivo.

![Registro de cambios push con un ejemplo de token de notificaciones push.]({% image_buster /assets/img/push_changelog.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:10px;"}

Por otro lado, si el nombre de la aplicación en la entrada del dispositivo tiene el prefijo `Background:`, la aplicación solo está autorizada para recibir [push en segundo plano]({{site.baseurl}}/user_guide/channels/push/types#background-push-notifications) y no puede mostrar notificaciones visibles para el usuario en ese dispositivo. Esto generalmente indica que el usuario ha deshabilitado las notificaciones para la aplicación en ese dispositivo.

Si un token de notificaciones push se mueve a un usuario diferente en el mismo dispositivo, el primer usuario dejará de estar registrado para push.

## Gestión de tokens de notificaciones push {#push-token-management}

Consulta la siguiente tabla para conocer las acciones que provocan cambios o eliminación de tokens de notificaciones push en los perfiles de usuario.

| Acción | Descripción |
| ------ | ----------- |
| Se llama al método `changeUser()` | El método `changeUser()` de Braze cambia el ID de usuario al que los SDK asignan los datos de comportamiento del usuario. Este método se llama normalmente cuando un usuario inicia sesión en una aplicación. Cuando se llama a `changeUser()` con un ID de usuario diferente o nuevo en un dispositivo específico, el token de notificaciones push de ese dispositivo se moverá al perfil de Braze correspondiente con el ID de usuario adecuado. |
| Se produce un error push | Algunos errores push comunes que provocan la eliminación del token incluyen `MismatchSenderId`, `InvalidRegistration` y otros tipos de rebotes push. <br><br>Consulta nuestra lista completa de [errores push]({{site.baseurl}}/user_guide/channels/push/push_error_codes) comunes. |
| El usuario desinstala | Cuando un usuario desinstala la aplicación de un dispositivo, Braze eliminará el token de notificaciones push del usuario de su perfil. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gestión de tokens de notificaciones push" }

### ¿Cómo se ve esto a mayor escala? {#what-does-this-look-like-on-a-broader-scale}

Cuando un usuario abre una nueva aplicación y concede acceso push desde un aviso push, se realiza una llamada desde el SDK de Braze a los proveedores push. Cuando se realiza esa llamada, el proveedor push ejecuta una verificación para comprobar que todo está configurado correctamente. Si es así, se pasa un token de notificaciones push a tu dispositivo. Cuando ese token llega, el SDK lo comunica a Braze. Después de que Braze haya recibido el token del proveedor push, actualizamos o creamos un nuevo perfil de usuario. Estos usuarios ahora se consideran registrados.

Si queremos lanzar una Campaign, creamos una Campaign en Braze que genera una carga útil push para enviar al proveedor push. Desde ahí, el proveedor entrega la carga útil push al dispositivo del usuario y el SDK pasa el estado de mensajería a Braze.

![Un diagrama de flujo que muestra el proceso push mencionado anteriormente entre Braze, el cliente y Apple Push Notification Service o Firebase Cloud Messaging.]({% image_buster /assets/img/push_process.png %})

| Pasos de registro | Pasos de mensajería |
| ------------------ | --------------- |
| 1. El cliente (dispositivo) se registra en el proveedor push<br>2. El proveedor genera y entrega el token de notificaciones push<br>3. Se envían los tokens a Braze |1. Braze envía la carga útil push al proveedor<br>2. El proveedor entrega la carga útil push al dispositivo<br>3. El SDK pasa las estadísticas de mensajería a Braze |
{: .reset-td-br-1 .reset-td-br-2 aria-label="¿Cómo se ve esto a mayor escala?" }

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Qué sucede cuando un usuario que aceptó push elimina y luego vuelve a descargar mi aplicación? {#what-happens-when-an-opted-in-user-deletes-and-then-redownloads-my-app}

Supongamos que un usuario acepta push, recibe algunos mensajes push y luego elimina la aplicación. Esto eliminará el consentimiento push a nivel de dispositivo. A partir de aquí, el primer push rebotado después de la desinstalación hará que ese usuario sea excluido automáticamente de futuros mensajes push. Después de esto, si un usuario reinstalara la aplicación pero no la abriera, Braze no podrá enviarle un push porque los tokens de notificaciones push no se han vuelto a conceder para tu aplicación.

Además, si un usuario volviera a habilitar push en primer plano, se requeriría un inicio de sesión para actualizar esta información en su perfil de usuario y comenzar a recibir mensajes push.

### ¿Cuándo caducan los tokens de notificaciones push? {#push-token-expire}

Desafortunadamente, APNs y FCM realmente no definen esto. Los tokens de notificaciones push pueden caducar cuando se actualiza una aplicación, cuando los usuarios transfieren sus datos a un nuevo dispositivo o cuando reinstalan un sistema operativo. En su mayor parte, realmente no tenemos información sobre por qué los proveedores push caducan ciertos tokens de notificaciones push.

Para tener en cuenta esa ambigüedad, nuestras integraciones push del SDK siempre registran y envían los tokens al inicio de la sesión para asegurarnos de tener el token más actualizado.