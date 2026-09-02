---
nav_title: Mensajes dentro de la aplicación de push primer
article_title: Mensajes dentro de la aplicación de push primer
page_order: 1
page_type: reference
description: "Este artículo cubre los requisitos previos para los mensajes dentro de la aplicación de push primer y cómo configurarlos."
channel: push

---

# Mensajes dentro de la aplicación de push primer {#push-primer-in-app-messages}

> Solo tienes una oportunidad para pedir permiso de push a los usuarios, así que optimizar tu registro de push es crucial para maximizar el alcance de tus mensajes push. Usa mensajes dentro de la aplicación para explicar qué tipo de mensajes pueden esperar recibir tus usuarios si eligen la adhesión voluntaria, antes de mostrarles el aviso nativo de push. Esto se conoce como push primer.

![Mensaje dentro de la aplicación de push primer para una aplicación de streaming. La notificación dice "¿Recibir notificaciones push de Movie Cannon? Las notificaciones pueden incluir nuevas películas, programas de TV u otros avisos y se pueden desactivar en cualquier momento."]({% image_buster /assets/img_archive/push_primer_iam.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

Para crear un mensaje dentro de la aplicación de push primer en Braze, puedes usar el comportamiento de clic en botón "Request Push Permission" al crear un mensaje dentro de la aplicación para iOS, Android o Web.

## Requisitos previos {#prerequisites}

Esta característica requiere [comportamiento de clic en botón](#button-actions), que es compatible con las siguientes versiones mínimas o posteriores:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

Además, ten en cuenta los siguientes detalles específicos de cada plataforma:

{% tabs local %}
{% tab android %}
| Versión del SO | Información adicional |
|----------|----------------------|
| **Android 12 y anteriores** | No se recomienda implementar push primers porque el push está habilitado de forma predeterminada. |
| **Android 13+** | Si un usuario rechaza tu solicitud de permiso de push dos veces, Android bloquea solicitudes posteriores, incluidos los mensajes de push primer de Braze. Para conceder el permiso después de esto, los usuarios deben habilitar manualmente el push para tu aplicación en la configuración de su dispositivo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }
{% endtab %}

{% tab swift %}
### Información general {#general-information}

- El aviso de push solo se puede mostrar una vez por instalación, impuesto por el sistema operativo.
- El aviso no se muestra si la configuración de push de la aplicación está explícitamente activada o desactivada. Solo se muestra para usuarios con [autorización provisional](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375).
  - **La configuración de push de la aplicación está activada:** Braze no muestra el mensaje dentro de la aplicación, ya que el usuario ya ha optado por la adhesión voluntaria.
  - **La configuración de push de la aplicación está desactivada:** Necesitas redirigir al usuario a la configuración de notificaciones push de tu aplicación dentro de la configuración del dispositivo.
- **Volver a probar después de rechazar:** Si un usuario rechaza el aviso nativo, iOS no lo muestra de nuevo para esa instalación de la aplicación. Para volver a probar el flujo de push primer, los usuarios normalmente necesitan desinstalar y reinstalar la aplicación, o cambiar el permiso de notificaciones para tu aplicación en **Configuración**.

### Eliminación manual de código {#manual-code-removal}

El mensaje dentro de la aplicación que configuras usando este tutorial llama automáticamente al código nativo de solicitud de push cuando un usuario hace clic en el botón del mensaje dentro de la aplicación. Para evitar solicitar el permiso de notificaciones push dos veces, o en el momento equivocado, un desarrollador debe modificar cualquier integración de notificaciones push existente que haya implementado para asegurarse de que tu mensaje dentro de la aplicación sea el primer push primer que vean tus usuarios.

Tu equipo de desarrollo debe revisar tu implementación de notificaciones push para tu aplicación o sitio y eliminar manualmente cualquier código que solicite permiso de push. Por ejemplo, elimina las referencias al siguiente código:

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
requestAuthorizationWithOptions
```
{% endsubtab %}
{% subtab swift %}
```swift
requestAuthorization
```
{% endsubtab %}
{% subtab JavaScript %}
```javascript
braze.requestPushPermission()
// or
appboy.registerAppboyPushMessages()
```
{% endsubtab %}
{% subtab Java %}
```java
android.permission.POST_NOTIFICATIONS
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Paso 1: Crea un mensaje dentro de la aplicación {#step-1-create-an-in-app-message}

Primero, [crea un mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional) y luego selecciona tu tipo de mensaje y diseño.

Para asegurarte de que tienes suficiente espacio tanto para tu mensaje como para los botones, usa un diseño de mensaje de pantalla completa o modal. Si eliges pantalla completa, ten en cuenta que se requiere una imagen.

## Paso 2: Construye tu mensaje {#step-2-build-your-message}

Ahora es momento de añadir tu texto. Recuerda que un push primer está destinado a preparar al usuario para activar las notificaciones push. En el cuerpo de tu mensaje, te sugerimos destacar las razones por las que tus usuarios deberían tener activadas las notificaciones push. Sé específico sobre qué tipo de notificaciones quieres enviar y qué valor pueden proporcionar.

Por ejemplo, una aplicación de noticias podría usar el siguiente push primer:

```plaintext
Breaking news on the go! Enable push notifications to get alerts for major stories and topics that matter to you.
```

Mientras que una aplicación de streaming podría usar lo siguiente:

```plaintext
Get push notifications from Movie Cannon? Notifications may include new movies, TV shows, or other notices and can be turned off at any time.
```

Para mejores prácticas y recursos adicionales, consulta [Crear avisos personalizados de adhesión voluntaria]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).

## Paso 3: Especifica el comportamiento de los botones {#button-actions}

Para añadir botones a tu mensaje dentro de la aplicación, arrastra dos bloques de **Botón** a tu mensaje, que actúan como los botones primario y secundario en tu mensaje dentro de la aplicación. También puedes arrastrar una fila a tu mensaje y luego arrastrar los botones a la fila, para que los botones estén en la misma fila horizontal (en lugar de apilados uno encima del otro). Recomendamos "Permitir notificaciones" y "Ahora no" como botones iniciales, pero hay muchos avisos de botón diferentes que puedes asignar.

Después de haber añadido el texto de los botones, especifica el comportamiento de clic para cada botón:

- **Botón 1:** Configúralo como "Close Message". Este es tu botón secundario, o la opción "Ahora no".
- **Botón 2:** Configúralo como "Request Push Permission". Este es tu botón primario, o la opción "Permitir notificaciones".

![Creador de mensajes dentro de la aplicación con dos botones: "Permitir notificaciones" y "Ahora no".]({% image_buster /assets/img_archive/push_primer_button_behavior.png %})

## Paso 4: Planifica la entrega {#step-4-schedule-delivery}

Para configurar tu push primer para que se envíe en un momento relevante, debes planificar tu mensaje dentro de la aplicación como un mensaje basado en acciones con **Perform Custom Event** como la acción desencadenante.

Aunque el momento ideal variará, Braze sugiere esperar hasta que un usuario complete algún tipo de [acción de alto valor](https://www.braze.com/resources/videos/mapping-high-value-actions), indicando que está empezando a ver valor en tu aplicación o sitio, o cuando haya una necesidad convincente que las notificaciones push puedan abordar (como después de que hayan realizado un pedido y quieras ofrecerles información de seguimiento de envío). De esta manera, el aviso es beneficioso para el cliente en lugar de solo para tu marca.

![Configuración de entrega basada en acciones para enviar a usuarios que realizaron el evento personalizado de "Add to Watch List".]({% image_buster /assets/img_archive/push_primer_trigger.png %})

## Paso 5: Segmenta a los usuarios {#step-5-target-users}

El objetivo de una Campaign de push primer es solicitar a los usuarios en cualquier dispositivo donde aún no hayan concedido permisos de push. Esto puede incluir usuarios nuevos o usuarios existentes que obtienen un nuevo dispositivo o reinstalan tu aplicación.

{% alert important %}
**Supresión automática con push primer sin código**: Si usas el push primer sin código (la acción de botón "Request Push Permission"), no necesitas añadir filtros de suscripción push a tu segmentación. El SDK or kit de desarrollo de software suprime automáticamente el mensaje dentro de la aplicación en dispositivos que ya tienen un token de push activo, independientemente del estado de push del usuario en otros dispositivos. Para más información sobre la segmentación de usuarios con múltiples dispositivos, consulta [Segmentar usuarios con múltiples dispositivos](#targeting-users-with-multiple-devices).
{% endalert %}

Si no estás usando el push primer sin código, añade un filtro donde `Foreground Push Enabled For App is false`. Este filtro identifica instalaciones individuales de la aplicación que aún no han optado por las notificaciones push en primer plano.

{% alert important %}
Usar un filtro a nivel de usuario como `Push Subscription Status is not Opted In` excluye a los usuarios que ya han optado por la adhesión voluntaria en otro dispositivo, impidiéndoles recibir el aviso en su nuevo dispositivo.
{% endalert %}

Más allá de eso, puedes decidir qué segmentos adicionales consideras más apropiados. Por ejemplo, podrías segmentar a usuarios que han completado una segunda compra, usuarios que acaban de crear una cuenta para convertirse en miembros, o incluso usuarios que visitan tu aplicación más de dos veces por semana. Segmentar a los usuarios en estos segmentos cruciales aumenta la probabilidad de que opten por la adhesión voluntaria y se habiliten para push.

### Segmentar usuarios con múltiples dispositivos {#targeting-users-with-multiple-devices}

Debido a que Braze captura los datos de usuario a nivel de perfil en lugar de a nivel de dispositivo, segmentar a usuarios que poseen múltiples dispositivos puede ser un desafío. Los filtros de suscripción push en la segmentación incluyen o excluyen usuarios basándose en el estado de suscripción de un solo dispositivo en lugar del estado de suscripción del dispositivo específico al que se dirige. Además, los estados provisionales en iOS añaden complejidad, ya que estos dispositivos técnicamente tienen tokens de push en primer plano, pero los usuarios no han optado explícitamente por la adhesión voluntaria.

#### El problema con los filtros de suscripción push {#the-problem-with-push-subscription-filters}

Cuando un usuario tiene múltiples dispositivos con diferentes estados de suscripción push, los filtros de suscripción push en tu segmentación pueden fallar al segmentar algunos dispositivos. Considera estos escenarios:

{% details Escenario 1: El usuario tiene dos dispositivos en diferentes plataformas %}

**El usuario tiene dos dispositivos:**
- Dispositivo A: Android, con adhesión voluntaria a push
- Dispositivo B: iOS, sin adhesión voluntaria a push

**Filtros de segmento que no funcionan:**
- `Push enabled = false` - El usuario tiene push habilitado en su dispositivo Android, por lo que no entra en el segmento. El segmento no incluye el dispositivo iOS.
- `Push subscription status is not opted in` - El usuario tiene push habilitado en su dispositivo Android, por lo que no entra en el segmento. El segmento no incluye el dispositivo iOS.

**Filtros de segmento que funcionan:**
- `Push enabled for iOS = false` - El usuario tiene push habilitado en su dispositivo Android, pero solo estamos segmentando dispositivos iOS, por lo que el usuario entra en el segmento. El segmento incluye el dispositivo iOS.

{% enddetails %}

{% details Escenario 2: El usuario tiene dos dispositivos iOS con diferentes estados %}

**El usuario tiene dos dispositivos iOS:**
- Dispositivo A: Con adhesión voluntaria a push
- Dispositivo B: Habilitado provisionalmente pero sin adhesión voluntaria

**Filtros de segmento que no funcionan:**
- `Push enabled = false` - El dispositivo A tiene adhesión voluntaria a push, por lo que el usuario no entra en el segmento. El segmento no incluye el dispositivo B.
- `Provisionally opted in = true` - El dispositivo A tiene adhesión voluntaria completa, lo que significa que no está en un estado provisional. El usuario no entra en el segmento. El segmento no incluye el dispositivo B.
- `Push enabled for app > iOS = false` - El dispositivo A tiene adhesión voluntaria a push en iOS, por lo que el usuario no entra en el segmento. El segmento no incluye el dispositivo B.
- `Push subscription status is not opted in` - El dispositivo A tiene adhesión voluntaria a push, por lo que el usuario no entra en el segmento. El segmento no incluye el dispositivo B.

**Resultado:** Usar cualquier combinación de estos filtros de push resulta en que el segmento excluya al menos un dispositivo.

{% enddetails %}

{% details Escenario 3: El usuario tiene tres o más dispositivos en el mismo SO %}

**El usuario tiene tres dispositivos:**
- Dispositivo A: Con adhesión voluntaria a push
- Dispositivo B: Sin adhesión voluntaria a push
- Dispositivo C: Sin adhesión voluntaria a push

**Filtros de segmento que no funcionan:**
- `Push enabled = false` - El dispositivo A tiene adhesión voluntaria a push, por lo que el usuario no entra en el segmento. El segmento no incluye los dispositivos B y C.
- `Push enabled for app > X = false` - El dispositivo A tiene adhesión voluntaria a push en la aplicación especificada, por lo que el usuario no entra en el segmento. El segmento no incluye los dispositivos B y C.
- `Push subscription status is not opted in` - El dispositivo A tiene adhesión voluntaria a push, por lo que el usuario no entra en el segmento. El segmento no incluye los dispositivos B y C.

**Resultado:** Usar cualquier combinación de estos filtros de push deja al menos un dispositivo sin segmentar.

{% enddetails %}

#### Solución: Usa el push primer sin código {#solution-use-the-no-code-push-primer}

La solución recomendada es usar el push primer sin código (la acción de botón "Request Push Permission") sin filtros adicionales de segmentación de estado de push.

{% alert important %}
**Supresión automática**: El push primer sin código se suprime automáticamente en dispositivos que ya tienen un token de push activo. El SDK or kit de desarrollo de software verifica si un usuario en su dispositivo específico ya tiene un token de push. Si el SDK or kit de desarrollo de software detecta que el usuario ya ha optado por la adhesión voluntaria (por ejemplo, de una solicitud anterior o a través de la configuración del dispositivo), el SDK or kit de desarrollo de software suprime automáticamente el mensaje dentro de la aplicación sin necesidad de filtros de segmentación adicionales. El primer se muestra en todos los demás escenarios, incluyendo si un usuario tiene adhesión voluntaria provisional a push.
{% endalert %}

El beneficio de usar el push primer sin código es que la funcionalidad es compatible con el SDK or kit de desarrollo de software de Braze. Debido a que el SDK or kit de desarrollo de software puede detectar el estado del token de push en el dispositivo específico que muestra el mensaje, no necesitas depender de filtros de segmentación a nivel de perfil que pueden excluir a usuarios con múltiples dispositivos.

#### Consideraciones {#considerations}

**Se requiere push primer sin código**: Debes usar el push primer sin código para que la supresión automática funcione. Si configuras lógica personalizada o vínculos profundos en lugar de usar la acción de botón "Request Push Permission", el SDK or kit de desarrollo de software no puede identificar que estás intentando mostrar un push primer. Esto resulta en que el mensaje se muestre independientemente del estado de suscripción de ese dispositivo.

**Supresión para usuarios que optaron por no recibir**: Es posible que quieras suprimir el mensaje dentro de la aplicación para usuarios que han optado explícitamente por no recibir push (por ejemplo, desde la solicitud nativa o la configuración del dispositivo) y reorientar a esos usuarios con una Campaign de nurture separada. Para hacer esto, usa la siguiente lógica Liquid en combinación con el primer sin código:

{% raw %}
```liquid
{% if targeted_device.${foreground_push_enabled} == false %}
{% abort_message('user turned off push notifications') %}
{% endif %}
- message goes here -
```
{% endraw %}

El filtro Liquid `targeted_device` solo mira el dispositivo donde se está mostrando el mensaje, en lugar del perfil de usuario. En ese dispositivo, `foreground_push_enabled` se establece en `true` cuando hay un token de push en primer plano activo y se establece en `false` cuando el sistema operativo informa que las notificaciones push han sido deshabilitadas (por ejemplo, el usuario las desactivó explícitamente). Para dispositivos completamente nuevos que aún no han respondido a un estado de permiso de push, `foreground_push_enabled` no está establecido y no tiene valor. Debido a que la condición Liquid verifica específicamente {% raw %}`false`{% endraw %}, solo suprime el primer para dispositivos con una exclusión explícita, mientras que los dispositivos en este estado desconocido aún califican y pueden recibir el push primer.

## Paso 6: Eventos de conversión {#step-6-conversion-events}

Braze sugiere configuraciones predeterminadas para conversiones, pero es posible que quieras configurar [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) relacionados con push primers.