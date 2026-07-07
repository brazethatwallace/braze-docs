---
nav_title: Cancelación de suscripción difusa
article_title: Cancelación de suscripción difusa
description: "Este artículo de referencia explica cómo configurar la cancelación de suscripción difusa, un ajuste que intenta reconocer cuándo un mensaje de entrada no coincide con una palabra clave de cancelación de suscripción."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
page_order: 4

---

# Cancelación de suscripción difusa {#fuzzy-opt-out}

![Chat de mensajes en iOS que muestra mensajes salientes de cancelación de suscripción en respuesta al mensaje difuso de entrada "Please stopppp".]({% image_buster /assets/img/sms/fuzzy1.jpg %}){: style="float:right;max-width:30%;margin-left:15px;"}

> Los usuarios que envían SMS, MMS y RCS con Braze deben cumplir con las leyes, regulaciones y estándares del sector aplicables que se hayan definido. En lo que respecta a la cancelación de suscripción, leyes como la TCPA dictan que cuando un usuario envía cualquier mensaje que constituya una revocación razonable del consentimiento (incluidas las palabras clave de cancelación de suscripción reconocidas como "STOP", "STOPALL", "UNSUBSCRIBE", "CANCEL", "END" o "QUIT"), todos los mensajes posteriores relacionados con ese programa de mensajería deben detenerse. Braze procesa automáticamente las palabras clave de cancelación de suscripción reconocidas y cancela la suscripción del usuario.<br><br> La cancelación de suscripción difusa amplía esta capacidad al intentar reconocer mensajes de entrada que no coinciden con ninguna **palabra clave de cancelación de suscripción** configurada para la categoría **Opt-out** del grupo de suscripción (es decir, cualquier [palabra clave de cancelación de suscripción predeterminada]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout) o [palabra clave de cancelación de suscripción personalizada]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling)) pero que aún indican intención de cancelar la suscripción; por ejemplo, un mensaje como "goodbye" o "leave me alone".

La cancelación de suscripción difusa está deshabilitada de forma predeterminada. Si la cancelación de suscripción difusa está habilitada y un mensaje de entrada se considera "difuso", puedes configurar Braze para que cancele automáticamente la suscripción del usuario o envíe un mensaje que le indique cómo cancelar la suscripción manualmente. Para las marcas de EE. UU., se recomienda encarecidamente cancelar automáticamente la suscripción del usuario para cumplir con los requisitos de la TCPA.

{% alert note %}
Actualmente, solo se admiten las palabras clave de cancelación de suscripción (predeterminadas y personalizadas) creadas con el inglés como [idioma local]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling#multi-language-support).
{% endalert %}

## ¿Qué se considera difuso? {#what-is-deemed-as-fuzzy}

Los criterios para que una respuesta de entrada se considere "difusa" son los siguientes (las comparaciones utilizan todas las palabras clave de la categoría **Opt-out**, incluidas las predeterminadas y las personalizadas):
- Si al intercambiar una letra con la letra inmediatamente a la izquierda o a la derecha en un teclado QWERTY se obtiene una coincidencia con una palabra clave de cancelación de suscripción.
- Una subcadena del mensaje coincide con una palabra clave de cancelación de suscripción.

Por ejemplo, "Stpo" o "Please stopppp" se considerarán difusos y se enviará una respuesta de cancelación de suscripción difusa. Si el usuario responde después con una palabra clave de cancelación de suscripción, se desencadenará un evento de cancelación de suscripción.

## Configurar la cancelación de suscripción difusa {#configure-fuzzy-opt-out}

Para configurar la cancelación de suscripción difusa, ve a la página de administración de palabras clave del grupo de suscripción.

1. Ve a **Audiencia** > **Administración del grupo de suscripción** y selecciona un grupo de suscripción **SMS/MMS/RCS**.
2. En **Global Keywords**, busca la categoría **Opt-out** y selecciona el icono de lápiz.
3. Alterna **Fuzzy Opt-Out** a **On**.
4. Selecciona tu opción preferida de **Fuzzy Opt-Out Logic**:
   - **Automatically unsubscribe:** Cuando un usuario envía un mensaje similar a una palabra clave de cancelación de suscripción, se cancela su suscripción de inmediato sin que se le solicite confirmación. A continuación, se envía el mensaje estándar de confirmación de cancelación de suscripción.
   - **Send opt-out instructions:** Cuando un usuario envía un mensaje similar a una palabra clave de cancelación de suscripción, Braze envía una respuesta personalizada (el **Opt-out instruction message**) que explica cómo cancelar la suscripción.
5. Si seleccionaste **Send opt-out instructions**, introduce tu texto personalizado en el campo **Opt-out instruction message**. Este campo es obligatorio para este ajuste.
6. Selecciona **Save**.

![Sección para editar las palabras clave de cancelación de suscripción y proporcionar un mensaje con instrucciones de cancelación de suscripción.]({% image_buster /assets/img/sms/fuzzy2.png %})

## Buenas prácticas para los mensajes de cancelación de suscripción difusa {#best-practices-for-fuzzy-opt-out-messages}

Para garantizar una experiencia clara, conforme y positiva para tus suscriptores, es fundamental configurar tu mensaje de cancelación de suscripción difusa de forma cuidadosa. El propósito principal del mensaje de cancelación de suscripción difusa es **guiar a los usuarios que envían un mensaje similar, pero no exactamente igual, a tu palabra clave de cancelación de suscripción designada**. El mensaje indica a los usuarios cómo cancelar la suscripción correctamente.

### Consideraciones críticas {#critical-considerations}

{% alert warning %}
Si seleccionaste **Send opt-out instructions**, **no** configures tu mensaje de cancelación de suscripción difusa para confirmar una cancelación de suscripción. Tu mensaje de cancelación de suscripción difusa no debe contener lenguaje que implique que el usuario ya ha cancelado su suscripción correctamente. Por ejemplo, **no** uses "Se ha cancelado tu suscripción", "No recibirás más mensajes de este número" ni "Ahora estás dado de baja".
{% endalert %}

El mensaje de cancelación de suscripción difusa se envía antes de que el usuario haya cancelado su suscripción correctamente. Usar un lenguaje de confirmación (como "Se ha cancelado tu suscripción") induce al suscriptor a creer que se ha dado de baja cuando no es así, lo que provoca la recepción continuada de mensajes no deseados, frustración del suscriptor y riesgos significativos de cumplimiento normativo.

Para cancelar la suscripción de los usuarios de inmediato ante una coincidencia difusa, usa en su lugar el ajuste **Automatically unsubscribe**.

{% alert warning %}
**NO** configures tu mensaje de cancelación de suscripción difusa para que sea idéntico o similar a tu palabra clave exacta de cancelación de suscripción.
{% endalert %}

Si tu mensaje difuso es igual o demasiado parecido a tu palabra clave exacta de cancelación de suscripción (por ejemplo, si "STOP" es tu palabra clave exacta y tu mensaje difuso es "Envía STOP para cancelar la suscripción"), puede generar confusión sobre si el mensaje inicial del usuario realmente resultó en una cancelación de suscripción o si necesita realizar otra acción. El mensaje difuso siempre debe aclarar qué acción debe tomar el usuario.

### Ejemplos de mensajes de cancelación de suscripción difusa {#examples-of-fuzzy-opt-out-messages}

Si eliges **Send opt-out instructions**, centra tu mensaje en guiar al usuario. Por ejemplo, si tu palabra clave de cancelación de suscripción es "STOP", estos son buenos y malos ejemplos de mensajes de cancelación de suscripción difusa que podrías crear:

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Buenos ejemplos <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Malos ejemplos <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Para cancelar la suscripción a todos los mensajes, responde con la palabra STOP."</td>
      <td>"Se ha cancelado tu suscripción correctamente. No recibirás más mensajes de este número. Responde START para volver a suscribirte." (Esto es una confirmación directa de cancelación de suscripción, lo cual es engañoso en un escenario de cancelación de suscripción difusa.)</td>
    </tr>
    <tr>
      <td>"Hemos recibido tu mensaje. Si deseas dejar de recibir mensajes de texto, envía STOP."</td>
      <td>"STOP." (Esto es simplemente la palabra clave exacta, lo cual no guía al usuario.)</td>
    </tr>
    <tr>
      <td>"¿Querías cancelar tu suscripción? Responde STOP para dejar de recibir todos los mensajes futuros."</td>
      <td>"Envía STOP para cancelar la suscripción." (Si "STOP" también es tu palabra clave exacta, esto es redundante y no aclara la acción si el mensaje inicial fue difuso.)</td>
    </tr>
  </tbody>
</table>