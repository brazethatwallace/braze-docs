---
nav_title: Mensajes de error comunes de push
article_title: Mensajes de error comunes de push
page_order: 22
page_type: reference
description: "Este artículo cubre los mensajes de error comunes relacionados con push para iOS y Android, y te guía a través de posibles soluciones."
channel: push
platform:
- iOS
- Android
---

# Mensajes de error comunes de push {#common-push-error-messages}

> Esta página cubre los mensajes de error comunes de la mensajería push.

{% tabs %}
{% tab Android %}
## Push rebotado: MismatchSenderId {#push-bounced-mismatchsenderid}
`MismatchSenderId` indica un fallo de autenticación. Firebase Cloud Messaging (FCM) se autentica con un par de datos clave: senderID y clave de API de FCM. Ambos deben validarse para verificar su exactitud. Para más información, consulta la [documentación de Android](https://firebase.google.com/docs/cloud-messaging/http-server-ref#error-codes) sobre este problema.

Los fallos comunes pueden incluir:
- [senderID]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android) incorrecto
- Registro múltiple si se registran con otro servicio push con un senderID diferente

### Push rebotado: InvalidRegistration {#push-bounced-invalidregistration}
`InvalidRegistration` puede ocurrir cuando un token de notificaciones push está malformado. Los fallos comunes pueden incluir cuando:
- Las personas pasan tokens de registro de Braze manualmente pero no llaman a `getToken()`. Por ejemplo, pueden pasar el ID de instancia completo. El token en el mensaje de error se ve como `&#124;ID&#124;1&#124;:[regular token]`.
- Las personas se registran con múltiples servicios. Actualmente esperamos que los intents de registro push lleguen de la forma antigua, así que si las personas se registran en múltiples lugares y capturamos intents de otros servicios, podemos obtener tokens de notificaciones push malformados.

### Push rebotado: NotRegistered {#notregistered}

`NotRegistered` generalmente significa que la aplicación ha sido eliminada del dispositivo (como nuestra señal de desinstalación). Esto también puede ocurrir si hay un registro múltiple y un segundo registro invalida el token de notificaciones push que Braze recibe.

### DEVICE_UNREGISTERED {#device-unregistered}

Este error aparece en el Registro de actividad de mensajes como: `Received 'Error: DEVICE_UNREGISTERED, ' sending to '[Token String]'`

Esto generalmente ocurre por una de las siguientes razones:

- El usuario desinstaló la aplicación. Esta es la causa más común. Cuando la aplicación se elimina de un dispositivo, el token de notificaciones push se vuelve inválido.
- Las credenciales push se actualizaron en la aplicación. Si tu equipo cambió las credenciales o certificados de FCM incluidos en la aplicación, los usuarios que se registraron con las credenciales anteriores tienen tokens inválidos hasta que la aplicación los vuelva a registrar.
- Una lógica personalizada está cancelando el registro de los usuarios de push. Esto es poco frecuente, pero es técnicamente posible cancelar programáticamente el registro de un dispositivo de push usando el [SDK or kit de desarrollo de software de Firebase/Android](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#deleteToken()).

{% alert note %}
Este error no significa que el usuario tenga push deshabilitado, solo que un token específico fue eliminado de su perfil. Esto es común en usuarios que están probando funcionalidades e instalando y desinstalando la aplicación con frecuencia. Para verificar si el usuario aún tiene tokens válidos, ve a **Búsqueda de usuarios** y revisa la sección **Configuración de contacto** en la pestaña **Participación**.
{% endalert %}

### La entidad solicitada no fue encontrada {#requested-entity-was-not-found}

Este error puede ocurrir por las siguientes razones:

- El usuario final desinstaló la aplicación. Puedes verificar su perfil de usuario para confirmar si este es el caso.
- Hay un canal de notificación no válido. Dependiendo de tu integración, los dispositivos pueden tener tokens de notificaciones push que solo son válidos para ciertos canales de notificación. Al enviar a un canal no válido, el mensaje rebota.
- El tamaño de la carga útil es demasiado grande.

Para más información, consulta la [documentación de Google](https://firebase.google.com/docs/cloud-messaging/manage-tokens#stale-and-expired-tokens) sobre tokens de registro obsoletos y expirados.

{% endtab %}
{% tab iOS %}

### Error al enviar push porque la carga útil no era válida {#error-sending-push-because-the-payload-was-invalid}

Este mensaje puede aparecer en la pestaña **Participación** del perfil de usuario en **Configuración de contacto** > **Registro de cambios de push** cuando el servicio de notificaciones push de Apple (APN) rechaza la solicitud push debido a una carga útil no válida.

En Braze, este mensaje del panel puede corresponder a una de las siguientes razones de error de APN:

- `PayloadEmpty`: la carga útil no contenía el contenido requerido para el tipo de push que se estaba enviando.
- `PayloadTooLarge`: la carga útil excedió el tamaño máximo de carga útil de APN.

Las causas comunes incluyen:

- Claves personalizadas (y sus valores) que hacen la carga útil demasiado grande (esto puede incluir valores renderizados por Liquid inesperadamente grandes).
- Una alerta o cuerpo vacío o faltante donde es requerido (o una carga útil `aps` malformada de otra manera).

Próximos pasos:

- Reduce el tamaño de la carga útil recortando claves personalizadas y acortando valores dinámicos grandes.
- Si envías a través de la API, valida la carga útil JSON final (incluyendo el tamaño) antes de enviar.

### Push rebotado: BadToken {#push-bounced-badtoken}

El error `BadToken` puede ocurrir por varias razones:
- El token de notificaciones push no se está enviando a Braze correctamente (por ejemplo, en `registerDeviceToken:` o el equivalente de tu plataforma).
	- Verifica el token en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log). Generalmente debería verse como una cadena larga de letras y números (como `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`). Si no es así, revisa el código involucrado en el envío del token de notificaciones push a Braze.<br><br>
- Entorno de aprovisionamiento no coincidente:
	- Si te registras con un certificado de desarrollo e intentas enviar con uno de producción, puedes ver este error.
	- Braze solo admite certificados universales para entornos de producción. Probar push en entornos de desarrollo con un certificado universal no funcionará.
	- Este reporte envía rebotes en producción pero no en desarrollo.<br><br>
- Perfil de aprovisionamiento no coincidente:
	- Esto puede ocurrir si tu certificado no coincide con el que se usó para obtener el token. Si se sospecha esto, los próximos pasos incluyen:
		- Asegurarte de que el certificado push que se usa para enviar push desde el panel de Braze y el perfil de aprovisionamiento estén configurados correctamente.
		- Recrear la certificación APNS y luego recrear el perfil de aprovisionamiento después de que el certificado APNS esté configurado para el `app_id`. Esto a veces puede resolver algunos problemas más visibles.

### ID de paquete no permitido {#bundle-id-not-allowed}

El error `TopicDisallowed` significa que APN rechazó el push porque el tema (ID de paquete) en la solicitud no está permitido para las credenciales de autenticación que se están usando. Para resolver esto:

1. **Verifica el ID de paquete.** Confirma que el ID de paquete configurado en la configuración de tu aplicación en Braze coincida exactamente con el ID de paquete de tu aplicación. Esto incluye cualquier variación de sufijo (por ejemplo, `.debug`, `.staging`).
2. **Verifica tu configuración de autenticación de APN.** Confirma que tu aplicación esté configurada con la clave `.p8` de APN correcta y que la clave esté asociada con el mismo equipo de Apple Developer que la aplicación a la que estás enviando.
3. **Confirma el entorno de la aplicación.** Si tienes IDs de aplicación separados en Braze para compilaciones de desarrollo y producción, verifica que cada uno esté configurado con las credenciales push y el entorno correctos.

### Unregistered {#ios-unregistered}

Este error aparece en el Registro de actividad de mensajes como:

`Received 'Unregistered' sending to '[Token String]'`

Este es el equivalente en iOS del error [DEVICE_UNREGISTERED](#device-unregistered) de Android. Generalmente ocurre por una de las siguientes razones:

- El usuario desinstaló la aplicación. Esta es la causa más común.
- Los certificados push se actualizaron. Si tu equipo cambió o renovó los certificados de APN, los usuarios que se registraron con los certificados anteriores pueden tener tokens inválidos hasta que la aplicación los vuelva a registrar.
- Una lógica personalizada está cancelando el registro de los usuarios de push. Esto es poco frecuente, pero es técnicamente posible cancelar programáticamente el registro de notificaciones remotas usando el SDK or kit de desarrollo de software de iOS.

{% alert note %}
Este error no significa que el usuario tenga push deshabilitado, solo que un token específico fue eliminado de su perfil. Para verificar si el usuario aún tiene tokens válidos, ve a **Búsqueda de usuarios** y revisa la sección **Configuración de contacto** en la pestaña **Participación**.
{% endalert %}

### InvalidProviderToken

El error `InvalidProviderToken` significa que APN rechazó la solicitud porque el token de autenticación (de una clave `.p8`) o el certificado push (`.p12`) no coincide con el ID de paquete o el Team ID de la aplicación. Para resolver esto:

1. **Verifica tu Team ID y Key ID:** si estás usando una clave de autenticación `.p8`, confirma que el **Team ID** y el **Key ID** configurados en el panel de Braze (**Configuración** > **Configuración de la aplicación** > selecciona tu aplicación iOS) coincidan con los valores en tu cuenta de Apple Developer.
2. **Verifica el ID de paquete:** asegúrate de que el ID de paquete registrado en Braze coincida con el ID de paquete de tu aplicación. Una discrepancia, como una diferencia en mayúsculas o un sufijo `.debug`, causa este error.
3. **Vuelve a cargar la clave o el certificado:** si la clave `.p8` o el certificado `.p12` se regeneró o revocó recientemente, carga la nueva clave en Braze y elimina la anterior.
4. **Confirma el entorno de APN:** si estás usando un certificado `.p12`, verifica que seleccionaste el entorno correcto (desarrollo versus producción) al cargarlo. Para las claves `.p8`, esto se maneja automáticamente.

### Push rebotado: el servicio de retroalimentación de APNS lo eliminó {#push-bounced-apns-feedback-service-removed}

Esto generalmente ocurre cuando alguien desinstala la aplicación. Braze consulta el servicio de retroalimentación de APNS cada noche para obtener una lista de tokens inválidos. Para más información, consulta la documentación de Apple sobre [Comunicación con APN](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html).

{% endtab %}
{% endtabs %}