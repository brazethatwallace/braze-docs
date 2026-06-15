---
nav_title: Mensajes dentro de la aplicación
article_title: Mensajes dentro de la aplicación en Canvas
alias: "/canvas_in-app_messages/"
page_order: 2
page_type: reference
description: "Este artículo de referencia describe las características y matices específicos de los mensajes dentro de la aplicación que puedes añadir a tu Canvas para mostrar mensajería enriquecida."
tool: Canvas
channel: in-app messages

---

# Mensajes dentro de la aplicación en Canvas {#in-app-messages-in-canvas}

> Puedes añadir mensajes dentro de la aplicación como parte de tu recorrido en Canvas para mostrar mensajería enriquecida cuando tu cliente interactúa con tu aplicación.

## Cómo funciona {#how-it-works}

Antes de poder usar mensajes dentro de la aplicación en tu Canvas, asegúrate de tener un [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) configurado con opciones de retraso y audiencia.

En el constructor de Canvas, añade un paso de [Mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) y selecciona **In-App Message** como tu **Messaging Channel**. Puedes personalizar [cuándo caducará tu mensaje](#in-app-message-expiration) y qué [comportamiento de avance](#advancement-behavior) tendrá.

Si tu espacio de trabajo tiene múltiples aplicaciones, dirige la aplicación correcta usando **plataformas de entrega**, las etiquetas de Liquid {% raw %}`{{targeted_device.${platform}}}`{% endraw %} o {% raw %}`{{app.${api_id}}}`{% endraw %}, no validaciones de entrega. Los mensajes dentro de la aplicación se muestran solo cuando el usuario abre la aplicación objetivo y cumple los criterios de desencadenamiento del paso. Para más información, consulta [Validaciones de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#delivery-validations).

## Añadir un mensaje dentro de la aplicación a tu recorrido de usuario {#adding-an-in-app-message-to-your-user-journey}

Para añadir un mensaje dentro de la aplicación a tu Canvas, haz lo siguiente:

1. Añade un paso de [Mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) a tu recorrido de usuario.
2. Selecciona **In-App Message** para tu **Messaging Channel**.
3. Determina [cuándo caducará tu mensaje](#in-app-message-expiration) y qué [comportamiento de avance](#advancement-behavior-options) tendrá.

## Mensajes dentro de la aplicación desencadenados {#triggered-in-app-messages}

Puedes seleccionar un desencadenante para que tus mensajes dentro de la aplicación se activen al inicio de sesión, o mediante eventos personalizados y compras.

Después de que pasen los retrasos y se comprueben las opciones de audiencia, los mensajes dentro de la aplicación se ponen en vivo cuando un usuario llega al paso de Mensaje. Si un usuario inicia una sesión y realiza el evento desencadenante del mensaje dentro de la aplicación, el usuario verá el mensaje dentro de la aplicación.

Para los pasos en Canvas que tienen entrada desencadenada por acciones, los usuarios pueden entrar al Canvas a mitad de sesión. Los mensajes dentro de la aplicación no se ponen en vivo hasta que se inicia una sesión, por lo que si un usuario está en medio de una sesión cuando llega al paso de Mensaje, no recibirá el mensaje dentro de la aplicación hasta que inicie otra sesión y realice el desencadenante correspondiente.

## Caducidad de mensajes dentro de la aplicación {#in-app-message-expiration}

Puedes elegir cuándo caducará el mensaje dentro de la aplicación. Durante este tiempo, el mensaje dentro de la aplicación esperará a ser visto hasta que llegue la fecha de caducidad. Una vez enviado el mensaje dentro de la aplicación, puede verse una sola vez.

![La sección de controles de mensaje de un paso de Mensaje para un mensaje dentro de la aplicación. El mensaje dentro de la aplicación caducará tres días después de que el paso esté disponible.]({% image_buster /assets/img_archive/canvas_expiration2.png %}){: style="max-width:90%"}

| Opción | Descripción | Ejemplo |
|---|---|---|
| **Una duración después de que el paso esté disponible** | Establece la caducidad del mensaje dentro de la aplicación en relación con el momento en que el paso está disponible para el usuario. | Un mensaje dentro de la aplicación con una caducidad de dos días estaría disponible cuando el usuario entre en el paso de Mensaje y se comprueben las opciones de audiencia. Cualquier retraso antes de llegar a este paso provendría de los pasos de Retraso anteriores en tu Canvas. El mensaje dentro de la aplicación estaría entonces disponible durante 2 días (48 horas) desde que el usuario entra en el paso, y durante esos dos días, los usuarios podrían ver el mensaje dentro de la aplicación si abren la aplicación. |
| **En una fecha y hora específicas** | Selecciona una fecha y hora específicas en las que el mensaje dentro de la aplicación dejará de estar disponible. | Si tienes una oferta que termina el 30 de noviembre de 2024, selecciona esta opción para que los usuarios ya no vean el mensaje dentro de la aplicación asociado cuando la oferta termine. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="In-app message expiration" }

Cuando un usuario inicia una sesión, Braze comprueba si su elegibilidad o caducidad para los mensajes dentro de la aplicación ha cambiado y envía información de caducidad actualizada a su dispositivo.

Si un mensaje dentro de la aplicación está configurado para caducar en una fecha y hora específicas que ya han pasado cuando el usuario llega al paso de Mensaje, ese usuario no recibe el mensaje dentro de la aplicación. Continuará a través del Canvas según tu [comportamiento de avance](#advancement-behavior) para ese paso.

Esto sucede a menudo cuando un paso anterior, como un paso de [Retraso]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step/), mantiene a los usuarios en un camino más largo. Por ejemplo, si lanzas un Canvas el 22 de mayo con un retraso de 72 horas seguido de un mensaje dentro de la aplicación que caduca el 23 de mayo a medianoche, los usuarios llegan al paso de Mensaje después del tiempo de caducidad y no ven el mensaje dentro de la aplicación.

## Casos de uso {#use-cases}

Braze recomienda que consideres usar esta característica en tus Canvas promocionales y de incorporación.

{% tabs %}
  {% tab Promocional %}

Las promociones, cupones y ofertas suelen tener fechas de caducidad fijas. El siguiente Canvas debería alertar a tus usuarios en los momentos más oportunos de que hay una promoción que pueden usar, y quizás influir en una compra. Esta promoción caduca el 28 de febrero de 2019 a las 11:15 am en la zona horaria de tu empresa.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table aria-label="Use cases" class="tg">
  <caption>Casos de uso</caption>
<thead>
  <tr>
    <th>Paso en Canvas</th>
    <th>Retraso</th>
    <th>Audiencia</th>
    <th>Canal</th>
    <th>Caducidad</th>
    <th>Avance</th>
    <th>Detalles</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Día 1: 50% de descuento</td>
    <td>Ninguno</td>
    <td>Todos desde la entrada</td>
    <td>Push</td>
    <td>N/A</td>
    <td>Avanzar audiencia después del retraso</td>
    <td>Push inicial que alerta a tus usuarios de la promoción. Está pensado para dirigir a los usuarios a tu aplicación para aprovechar la promoción.</td>
  </tr>
  <tr>
    <td>Dentro de la aplicación: 50% de descuento</td>
    <td>Ninguno</td>
    <td>Todos desde la entrada</td>
    <td>Mensaje dentro de la aplicación</td>
    <td><b>Caduca el:</b> 28/2/2019 11:15 AM Hora de la empresa</td>
    <td>Mensaje dentro de la aplicación visto</td>
    <td>El usuario ha abierto la aplicación y recibirá este mensaje independientemente de si fue por el mensaje push anterior o no.</td>
  </tr>
  <tr>
    <td>Recordatorio del 50% de descuento</td>
    <td>1 día después de que el usuario reciba el paso anterior</td>
    <td>Todos desde la entrada <br><br><b>Filtro:</b> Última compra realizada hace más de una semana</td>
    <td>Mensaje dentro de la aplicación</td>
    <td><b>Caduca el:</b> 28/2/2019 11:15 AM Hora de la empresa</td>
    <td>Ninguno (último mensaje en Canvas)</td>
    <td>El usuario ha recibido el mensaje dentro de la aplicación en el paso anterior pero no ha realizado una compra a pesar de estar en la aplicación. <br><br>Este mensaje está pensado para motivar aún más al usuario a realizar una compra usando la promoción.</td>
  </tr>
</tbody>
</table>

Los mensajes dentro de la aplicación caducan cuando la promoción caduca para evitar discrepancias entre la mensajería y la experiencia del cliente.

  {% endtab %}
  {% tab Incorporación de usuarios %}

Tu primera impresión con un usuario es, quizás, la más importante. Puede determinar las futuras visitas a tu aplicación. Tus comunicaciones iniciales con tu usuario deben estar bien programadas y fomentar visitas frecuentes a tu aplicación para promover el uso.

<table aria-label="Use cases" class="tg">
  <caption>Casos de uso</caption>
<thead>
  <tr>
    <th>Paso en Canvas</th>
    <th>Retraso</th>
    <th>Audiencia</th>
    <th>Canal</th>
    <th>Caducidad</th>
    <th>Avance</th>
    <th>Detalles</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Correo electrónico de bienvenida</td>
    <td>Ninguno</td>
    <td>Todos desde la entrada</td>
    <td>Correo electrónico</td>
    <td>N/A</td>
    <td>Avanzar audiencia después del retraso</td>
    <td>Correo electrónico inicial que da la bienvenida a tus usuarios a un proyecto, membresía u otro programa de incorporación. <br><br>Está pensado para dirigir a los usuarios a tu aplicación para comenzar su incorporación.</td>
  </tr>
  <tr>
    <td>Mensaje dentro de la aplicación del día 3-6</td>
    <td>3 días después de que el usuario reciba el paso anterior</td>
    <td>Todos desde la entrada</td>
    <td>Mensaje dentro de la aplicación</td>
    <td><b>Caduca:</b> 3 días después de que el paso esté disponible</td>
    <td>Mensaje dentro de la aplicación en vivo</td>
    <td>Si el usuario ha actuado en respuesta al correo electrónico y ha sido dirigido a la aplicación, recibirá el mensaje dentro de la aplicación deseado para continuar o recordarle su incorporación y cualquier requisito asociado.</td>
  </tr>
  <tr>
    <td>Push del día 5</td>
    <td>2 días después de que el usuario reciba el paso anterior</td>
    <td>Todos desde la entrada</td>
    <td>Push</td>
    <td>N/A</td>
    <td>Mensaje enviado</td>
    <td>Después de que los usuarios hayan recibido su mensaje dentro de la aplicación, recibirán un push de seguimiento para continuar su incorporación.</td>
  </tr>
</tbody>
</table>

Estas notificaciones push están espaciadas alrededor de un mensaje dentro de la aplicación para asegurar que el usuario haya visitado la aplicación y comenzado su incorporación. Esto ayuda a evitar cualquier correo no deseado o mensajería desordenada que pueda disuadir a los usuarios de visitar tu aplicación, y en su lugar crea un orden fluido y lógico para sus experiencias iniciales con tu aplicación.

  {% endtab %}
{% endtabs %}


## Priorizar mensajes dentro de la aplicación {#prioritizing-in-app-messages}

Un usuario puede desencadenar dos mensajes dentro de la aplicación en tu Canvas al mismo tiempo. Cuando esto sucede, Braze seguirá el siguiente orden de prioridad para determinar qué mensaje dentro de la aplicación se muestra.

Selecciona **Set exact priority** y arrastra los diferentes pasos en Canvas para reordenar su prioridad para el Canvas. Por defecto, los pasos anteriores en una variante en Canvas se mostrarán antes que los pasos posteriores. Después de que tus pasos estén en el orden de priorización que prefieras, selecciona **Apply sort**.

![El clasificador de prioridad con dos pasos "Welcome IAM" y "Followup IAM".]({% image_buster /assets/img_archive/canvas_priority2.png %}){: style="max-width:85%"}

### Realizar cambios en borradores de Canvas activos {#making-changes-to-drafts-of-active-canvases}

Si realizas cambios en la prioridad de mensajes dentro de la aplicación en **Send Settings** de un borrador de un Canvas activo, estos cambios se aplican directamente al Canvas activo cuando se cierra el clasificador de prioridad. Sin embargo, en un paso de Mensaje, el clasificador de prioridad se actualizará cuando se lance el borrador, ya que la configuración de los pasos en Canvas se aplica a nivel de paso.

## Comportamiento de avance {#advancement-behavior}

Los pasos de Mensaje avanzan automáticamente a todos los usuarios que entran en el paso. Ten en cuenta que no espera a que el mensaje dentro de la aplicación se desencadene o se muestre. No es necesario especificar el comportamiento de avance del mensaje, lo que simplifica la configuración general del paso.

Cuando un usuario entra en un paso de mensaje dentro de la aplicación, avanza fuera de él inmediatamente en lugar de ser retenido durante la ventana de caducidad. En este caso, tener un paso de Retraso en tu recorrido de usuario puede ser útil.

Para usar la opción **Advance when message sent**, añade una [ruta de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/) separada para filtrar a los usuarios que no recibieron el paso anterior.

{% details Editor original de Canvas %}

Ya no puedes crear ni duplicar Canvas usando el editor original. Esta sección está disponible como referencia para entender cómo funciona el comportamiento de avance para los pasos con mensajes dentro de la aplicación.

Los Canvas creados en el editor original necesitan especificar un comportamiento de avance: los criterios para avanzar a través de tu componente de Canvas. [Los pasos que solo contienen mensajes dentro de la aplicación](#steps-iam-only) tienen opciones de avance diferentes a los [pasos con múltiples tipos de mensaje](#steps-multiple-channels) (como push o correo electrónico). Para los mensajes dentro de la aplicación en el flujo de trabajo actual de Canvas, esta opción está configurada para siempre avanzar la audiencia inmediatamente.

La entrega basada en acciones no está disponible para los pasos de Canvas con mensajes dentro de la aplicación. Los pasos de Canvas con mensajes dentro de la aplicación deben ser planificados. En su lugar, los mensajes dentro de la aplicación en Canvas aparecerán la primera vez que tu usuario abra la aplicación (desencadenado por el inicio de sesión) después de que el mensaje planificado en el componente de Canvas les haya sido enviado.

Si tienes múltiples mensajes dentro de la aplicación en un solo Canvas, un usuario debe iniciar múltiples sesiones para recibir cada uno de esos mensajes individuales.

{% alert important %}
Cuando se selecciona **Advance When In-App Message Live**, el mensaje dentro de la aplicación estará disponible hasta que caduque, incluso si el usuario ha avanzado a pasos posteriores. Si no quieres que el mensaje dentro de la aplicación esté en vivo cuando se entreguen los siguientes pasos del Canvas, asegúrate de que la caducidad sea más corta que el retraso en los pasos posteriores.
{% endalert %}

#### Pasos con múltiples canales {#steps-multiple-channels}

Los pasos con un mensaje dentro de la aplicación y otro canal tienen las siguientes opciones de avance:

| Opción | Descripción |
|---|---|
| **Advance When Message Sent** | Los usuarios deben recibir un correo electrónico, webhook o notificación push, o ver el mensaje dentro de la aplicación para avanzar a los pasos posteriores del Canvas.  <br> <br>  Si el mensaje dentro de la aplicación caduca y el usuario no ha recibido el correo electrónico, webhook o push, o no ha visto el mensaje dentro de la aplicación, saldrá del Canvas y no avanzará a los pasos posteriores. |
| **Immediately Advance Audience** | Todos en la audiencia del paso avanzan a los siguientes pasos después de que transcurra el retraso, independientemente de si han visto el mensaje indicado o no. <br> <br> Los usuarios deben cumplir con los criterios de segmento y filtro del paso para avanzar a los siguientes pasos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Steps with multiple channels #steps-multiple-channels" }

{% alert important %}
Cuando se selecciona **Entire Audience**, el mensaje dentro de la aplicación estará disponible hasta que caduque, incluso si el usuario ha avanzado a pasos posteriores. Si no quieres que el mensaje dentro de la aplicación esté en vivo cuando se entreguen los siguientes pasos del Canvas, verifica que la caducidad sea más corta que el retraso en los pasos posteriores.
{% endalert %}

{% enddetails %}

## Acciones desencadenantes {#trigger-actions}

Puedes elegir entre las siguientes acciones desencadenantes para dirigirte a tus usuarios:

- **Realizar compra:** Dirige a los usuarios que realizan cualquier compra o una compra específica
- **Iniciar sesión:** Dirige a los usuarios que inician una sesión en cualquier aplicación o en una aplicación específica
- **Realizar evento personalizado:** Dirige a los usuarios que realizan el evento personalizado seleccionado (el evento personalizado debe enviarse usando el SDK).

Un usuario tiene que entrar en el paso en Canvas, iniciar una sesión y luego realizar el desencadenante para recibir un mensaje dentro de la aplicación. Esto significa que las actualizaciones a mitad de sesión no son compatibles. Por ejemplo, si el desencadenante es iniciar una sesión, el usuario solo necesita entrar en el paso en Canvas e iniciar una sesión para recibir el mensaje dentro de la aplicación. Si el desencadenante no es iniciar una sesión, el usuario tiene que entrar en el paso en Canvas, iniciar una sesión y luego realizar el desencadenante para recibir el mensaje dentro de la aplicación.

![Acción desencadenante con "Realizar una compra específica" seleccionado.]({% image_buster /assets/img_archive/canvas_trigger_actions.png %}){: style="max-width:90%"}

Las siguientes características de Canvas no están disponibles con mensajes dentro de la aplicación, por lo que no se aplicarán a tus mensajes dentro de la aplicación aunque estén activadas.

- Intelligent Timing
- Límite de velocidad
- Limitación de frecuencia
- Criterios de salida
- Horas tranquilas

## Propiedades de eventos personalizados en un Canvas {#custom-event-properties-in-a-canvas}

Las propiedades de eventos personalizados en mensajes dentro de la aplicación para Canvas son compatibles. Sin embargo, estas propiedades provienen del evento personalizado o la compra que desencadena el mensaje dentro de la aplicación, que se encuentra en el paso de Mensaje, no en la ruta de acción anterior.

## Consideraciones {#considerations}

Aquí hay algunas consideraciones al enviar mensajes dentro de la aplicación en un Canvas.

- Si el usuario nunca reinicia la aplicación o nunca inicia una sesión, la aplicación no podrá determinar si el usuario es elegible para el mensaje dentro de la aplicación, lo que significa que no se enviará un mensaje dentro de la aplicación.
- Cuando ocurre el primer clic y hay una variable de contexto de Canvas (propiedades de entrada de Canvas), y un usuario vuelve a entrar en un Canvas cinco veces, Braze tomará la quinta entrada y usará esa variable de contexto en el mensaje dentro de la aplicación.
- Un usuario puede ser elegible para hasta 10 mensajes dentro de la aplicación dentro del mismo paso en Canvas. Por ejemplo, si un Canvas permite la reentrada y un usuario entra al Canvas 11 veces, solo se le enviarán 10 mensajes dentro de la aplicación si ninguno ha caducado.