---
nav_title: Personalizar pie de página
article_title: Personalizar pie de página de correo electrónico
page_order: 6.5
description: "Este artículo describe cómo configurar un pie de página de correo electrónico personalizado para todo el espacio de trabajo."
channel:
  - email

---

# Personalizar pie de página de correo electrónico {#custom-email-footer}

> Puedes configurar un pie de página de correo electrónico personalizado para todo el espacio de trabajo, que puedes incluir como plantilla en cada correo electrónico usando el atributo Liquid {% raw %}`{{${email_footer}}}`{% endraw %}.

Al usar pies de página de correo electrónico personalizados, ya no necesitas crear un nuevo pie de página para cada plantilla de correo electrónico o Campaign que utilices. Todas las Campaigns de correo electrónico nuevas y existentes reflejan los cambios que realices en tu pie de página personalizado. Recuerda que el cumplimiento de la [Ley CAN-SPAM de 2003](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business) requiere que incluyas una dirección física de tu empresa y un enlace para cancelar suscripción en tus correos electrónicos.

{% alert warning %}
Es tu responsabilidad asegurarte de que tu pie de página personalizado cumpla con los requisitos mencionados anteriormente.
{% endalert %}

## Crear tu pie de página personalizado {#create-your-custom-footer}

Para crear o editar tu pie de página personalizado, haz lo siguiente:

1. Ve a **Settings** > **Email Preferences** > **Subscription Pages and Footers**.
2. Ve a la sección **Custom footer** y activa los pies de página personalizados.
3. Selecciona **Edit** y luego edita tu pie de página en la sección **Compose**.
4. Selecciona **Preview** para previsualizar cómo aparecerá tu pie de página de correo electrónico en el buzón de entrada de un cliente. Opcionalmente, puedes seleccionar **Copy preview link** para generar y copiar un enlace de vista previa que se puede compartir y que muestra cómo se verá el correo electrónico para un usuario aleatorio. El enlace durará siete días antes de que sea necesario regenerarlo.
5. Envía un mensaje de prueba.

![Un ejemplo de un pie de página personalizado.]({% image_buster /assets/img_archive/custom_footer.png %})

El pie de página predeterminado usa el atributo {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} y nuestra dirección postal física. Si estás usando este pie de página predeterminado, asegúrate de seleccionar **&#60;other&#62;** para el **Protocol**.

{% alert important %}
Para cumplir con las regulaciones CAN-SPAM, tu pie de página personalizado debe incluir un enlace para cancelar suscripción. Puedes usar este atributo Liquid {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} o tu propia URL personalizada para cancelar suscripción. No podrás guardar un pie de página personalizado sin un enlace para cancelar suscripción.
{% endalert %}

![Valores de protocolo y URL necesarios para el pie de página personalizado.]({% image_buster /assets/img_archive/email_unsub_protocol.png %}){: style="max-width:50%;"}

## Pies de página sin enlaces para cancelar suscripción {#footers-without-unsubscribe-links}

Ten mucho cuidado al usar una plantilla con el pie de página personalizado {% raw %}`{{${email_footer}}}` pero sin la etiqueta de enlace para cancelar suscripción `{{${set_user_to_unsubscribed_url}}}`{% endraw %}. Aparecerá una advertencia, pero será tu decisión enviar un correo electrónico con o sin un enlace para cancelar suscripción.

Aquí hay una advertencia en el compositor de correo electrónico:

![Ejemplo de correo electrónico redactado sin pie de página.]({% image_buster /assets/img_archive/no_unsub_link_warning.png %})

Aquí hay una advertencia en el compositor de Campaign:

![Composición de Campaign sin pie de página.]({% image_buster /assets/img_archive/no_footer_test.png %})

### Agregar un enlace personalizado para cancelar suscripción {#adding-a-custom-unsubscribe-link}

Para agregar un enlace personalizado para cancelar suscripción, puedes cambiar el enlace para cancelar suscripción en el pie de página personalizado de {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} a un enlace a tu propio sitio web con un parámetro de consulta que incluya el ID de usuario. Un ejemplo es:
{% raw %}
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

A continuación, llama al [punto de conexión `/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) para actualizar el estado de suscripción del usuario. Para más detalles, consulta nuestra documentación sobre [cambiar las suscripciones de correo electrónico]({{site.baseurl}}/user_guide/channels/email/subscriptions/#changing-email-subscriptions).

Luego, guarda este nuevo enlace. La etiqueta predeterminada de cancelación de suscripción de Braze {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} debe estar en el pie de página. Esto significa que necesitas incluir el enlace predeterminado "ocultándolo", ya sea colocando la etiqueta en un comentario o en una etiqueta `<div>` oculta.

## Mejores prácticas {#best-practices}

Sugerimos las siguientes mejores prácticas al crear y usar pies de página personalizados.

### Personalizar con atributos {#personalizing-with-attributes}

Al crear un pie de página personalizado, Braze sugiere usar [atributos para la personalización]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/). El conjunto completo de atributos predeterminados y personalizados está disponible, pero aquí hay algunos que pueden resultarte útiles:

| Atributo | Etiqueta |
| --------- | --- |
| Dirección de correo electrónico del usuario | {% raw %}`{{${email_address}}}`{% endraw %} |
| URL personalizada de cancelación de suscripción del usuario | {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} <br><br>Esta etiqueta reemplaza la etiqueta anterior {% raw %}`{{${unsubscribe_url}}}`{% endraw %}. Te recomendamos que uses la etiqueta más reciente {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} en su lugar. |
| URL personalizada de adhesión voluntaria del usuario | {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} |
| URL personalizada de suscripción del usuario | {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}|
| URL del centro de preferencias de Braze del usuario | {% raw %}`{{${preference_center_url}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Personalizar con atributos" }

### Incluir un enlace para cancelar suscripción y un enlace de adhesión voluntaria {#including-an-unsubscribe-link-and-opt-in-link}

{% raw  %}
Como mejor práctica, Braze recomienda incluir tanto un enlace para cancelar suscripción (como ``{{${set_user_to_unsubscribed_url}}}``) como un enlace de adhesión voluntaria (como ``{{${set_user_to_opted_in_url}}}``) en tu pie de página personalizado. De esta manera, los usuarios podrán tanto cancelar su suscripción como adherirse voluntariamente, y podrás recopilar datos de adhesión voluntaria de forma pasiva para una parte de tus usuarios.
{% endraw %}

### Configurar pies de página personalizados para correos electrónicos de texto sin formato {#setting-custom-footers-for-plaintext-emails}

También puedes optar por configurar un pie de página personalizado para correos electrónicos de texto sin formato desde la pestaña **Subscription Pages and Footers** en la página **Email Preferences**, que sigue las mismas reglas que el pie de página personalizado para correos electrónicos HTML.

Si no incluyes un pie de página de texto sin formato, Braze creará uno automáticamente a partir del pie de página HTML. Cuando tus pies de página personalizados estén a tu gusto, selecciona **Save**.

![Correo electrónico con la opción Establecer pie de página personalizado de texto sin formato seleccionada.]({% image_buster /assets/img_archive/custom_footer_save_changes.png %}){: style="max-width:70%" }

## Consideraciones {#considerations}

Si estás usando [BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/), ten en cuenta que {% raw %}`{{${email_footer}}}`{% endraw %} no es una etiqueta de Liquid estándar. Se procesa previamente antes de que Liquid se ejecute, por lo que usar {% raw %}`{{${email_footer}}}`{% endraw %} como valor de variable de contexto y llamar a la marca `:rerender` falla silenciosamente. En su lugar, usa un [bloque de contenido]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/#email-footers) para un pie de página de correo electrónico.