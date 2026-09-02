---
nav_title: Formulario de captura de correo electrónico
article_title: Formulario de captura de correo electrónico
page_order: 5
page_type: reference
description: "Este artículo ofrece un resumen del tipo de mensaje dentro de la aplicación de captura de correo electrónico."
channel:
  - in-app messages
---

# Formulario de captura de correo electrónico {#email-capture-form}

> Los mensajes de captura de correo electrónico te permiten solicitar a los usuarios de tu sitio que envíen su dirección de correo electrónico. Braze añade la dirección a su perfil de usuario para usarla en todas tus campañas de mensajería.

Este tipo de mensaje está disponible en el [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional).

Si recopilas correos electrónicos a través de un formulario personalizado en lugar de este tipo de mensaje dentro de la aplicación, y luego estableces la membresía del grupo de suscripción a través de la REST or transferencia de estado representacional API, verifica si ya existe un perfil antes de crear un usuario. Consulta [Mejores prácticas de recopilación]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices#step-1-check-if-the-user-exists).

## Cómo funciona {#how-it-works}

Cuando un usuario final ingresa su dirección de correo electrónico en este formulario, Braze agrega la dirección de correo electrónico a su perfil de usuario.

- Para [usuarios anónimos]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles) que aún no tienen una cuenta, la dirección de correo electrónico se almacena en el perfil de usuario anónimo vinculado al dispositivo del usuario.
- Si ya existe una dirección de correo electrónico en el perfil de usuario, la dirección de correo electrónico recién ingresada sobrescribe la dirección de correo electrónico existente.
- Si el usuario conocido tiene una dirección de correo electrónico marcada como [rebote duro]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#hard-bounce), Braze verifica si la dirección de correo electrónico recién ingresada difiere de la dirección en su perfil de Braze. Si la dirección de correo electrónico proporcionada es diferente, Braze actualiza la dirección de correo electrónico y elimina el estado de rebote duro.
- Si un usuario ingresa una dirección de correo electrónico no válida, ve el mensaje de error: "Please enter a valid email."
    - Direcciones de correo electrónico no válidas:
        - `example`
        - `example@`
        - `@gmail.com`
        - `example@gmail`
    - Direcciones de correo electrónico válidas:
        - `example@gmail.com`
        - `example@gnail.com` (con un error tipográfico)
    - Para más información sobre la validación de correo electrónico en Braze, consulta [Directrices y notas técnicas de correo electrónico]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation).

{% details Más sobre usuarios identificados versus anónimos %}

El formulario de captura de correo electrónico establece la dirección de correo electrónico en el perfil de usuario actualmente activo en Braze. El comportamiento difiere según si el usuario está identificado (ha iniciado sesión, se ha llamado a `changeUser`) o no.

Si un usuario anónimo ingresa su correo electrónico en el formulario y lo envía, Braze agrega la dirección de correo electrónico a su perfil. Si se llama a `changeUser` más adelante en su recorrido web y se asigna un nuevo `external_id` (como cuando un nuevo usuario se registra en el servicio), todos los datos del perfil de usuario anónimo se fusionan, incluida la dirección de correo electrónico.

Si se llama a `changeUser` con un `external_id` existente, el perfil de usuario anónimo queda huérfano y los [campos de datos específicos del perfil de usuario]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior) que aún no existen en el usuario identificado se fusionan, pero los campos que ya existen se pierden, incluida la dirección de correo electrónico.

Para más información, consulta el [Ciclo de vida del perfil de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle).

{% enddetails %}

## Paso 1: Crea una campaña de mensajes dentro de la aplicación {#step-1-create-an-in-app-message-campaign}

Para acceder a esta opción, debes crear una campaña de mensajería dentro de la aplicación. A partir de ahí, según tu caso de uso, establece **Send To** en **Web Browsers**, **Mobile Apps** o **Both Mobile Apps & Web Browsers**, y luego selecciona **Email Capture Form** como tu **Message Type**.

{% alert note %}
**¿Te diriges a usuarios web?** <br>Para habilitar los mensajes HTML dentro de la aplicación a través del SDK or kit de desarrollo de software Web, debes proporcionar la opción de inicialización `allowUserSuppliedJavascript` a Braze, por ejemplo, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Esto es por razones de seguridad, ya que los mensajes HTML dentro de la aplicación pueden ejecutar JavaScript, por lo que requerimos que un responsable del sitio los habilite.
{% endalert %}

## Paso 2: Personaliza el formulario {#customizable-features}

A continuación, personaliza tu formulario según sea necesario. Puedes personalizar las siguientes características de tu formulario de captura de correo electrónico:

- Texto del encabezado, cuerpo y botón de envío
- Una imagen opcional
- Un enlace opcional de "Términos de servicio"
- Diferentes colores para el texto del encabezado y cuerpo, botones y fondo
- Pares clave-valor
- Estilo del texto del encabezado y cuerpo, botones, color del borde de los botones, fondo y superposición
- Botón de envío
    - Ten en cuenta que el botón de envío solo aparece después de que el usuario introduce una dirección de correo electrónico válida. Esto te ayuda a recopilar direcciones de correo electrónico completas.

![Creador del formulario de captura de correo electrónico.]({% image_buster /assets/img/email_capture.png %})

Si necesitas más personalización, elige **Custom Code** como tu **Tipo de mensaje**. Usa esta [plantilla modal de captura de correo electrónico](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/5-email-capture-modal) del repositorio de GitHub de [Braze Templates](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates) como tu código inicial.

## Paso 3: Configura tu público de entrada {#step-3-set-your-entry-audience}

Si estás usando un mensaje dentro de la aplicación para capturar correos electrónicos de usuarios, es posible que desees limitar la audiencia a los usuarios que aún no han proporcionado esta información.

- **Para dirigirte a usuarios sin una dirección de correo electrónico:** Usa el filtro `Email Available` es `false`. Esto hace que el formulario solo aparezca a los usuarios que no tienen un correo electrónico registrado, lo que te ayuda a evitar solicitudes redundantes para usuarios conocidos.
- **Para dirigirte a usuarios anónimos sin ID externos:** Usa el filtro `External User ID` `is blank`. Esto es útil cuando deseas identificar usuarios que aún no se han autenticado o registrado.

También puedes combinar los dos filtros usando la lógica `AND`, si lo deseas. Esto hace que el formulario solo aparezca a los usuarios a quienes les faltan tanto una dirección de correo electrónico como un ID de usuario externo, lo cual es ideal para captar nuevos clientes potenciales o solicitar la creación de una cuenta.

## Paso 4: Segmenta a los usuarios que completaron el formulario (opcional) {#step-4-target-users-who-filled-out-the-form-optional}

Después de lanzar el formulario de captura de correo electrónico y recopilar direcciones de correo electrónico de tus usuarios, puedes segmentar a los usuarios que completaron el formulario.

1. En cualquier filtro de Segment en Braze, selecciona el filtro `Clicked/Opened Campaign`.
2. En el menú desplegable, selecciona `clicked in-app message button 1`.
3. Selecciona tu Campaign de formulario de captura de correo electrónico.