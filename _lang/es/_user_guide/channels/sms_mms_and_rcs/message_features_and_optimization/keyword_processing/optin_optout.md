---
nav_title: Palabras clave de adhesión y cancelación
article_title: Palabras clave de adhesión y cancelación de servicio de mensajes cortos
page_order: 0
description: "Este artículo de referencia cubre cómo Braze procesa las palabras clave básicas de adhesión voluntaria y cancelación de suscripción para la mensajería servicio de mensajes cortos."
page_type: reference
alias: /optin_optout/
tool:
  - Dashboard

channel:
  - SMS
---

# Palabras clave de adhesión y cancelación {#opt-in-and-opt-out-keywords}

> Las regulaciones exigen que haya respuestas a todas las palabras clave de adhesión voluntaria, cancelación de suscripción y ayuda/información. Braze procesa automáticamente los siguientes mensajes _exactos, de una sola palabra y sin distinción de mayúsculas y minúsculas_, actualizando automáticamente el [estado del grupo de suscripción]({{site.baseurl}}/sms_rcs_subscription_groups) del usuario y su número de teléfono asociado en todas las solicitudes de entrada.

## Palabras clave predeterminadas {#default-keywords}

Braze procesa automáticamente las siguientes palabras clave y actualiza el estado del grupo de suscripción del número de teléfono en todas las solicitudes de entrada. Ten en cuenta que estas palabras clave y respuestas predeterminadas también pueden personalizarse, y puedes añadir [palabras clave personalizadas]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling).

{% alert tip %}
¿Te interesa ampliar tu procesamiento de cancelación de suscripción? Prueba la [cancelación aproximada]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/fuzzy_opt_out), una característica que intenta reconocer cuándo un mensaje de entrada no coincide con una palabra clave de cancelación, pero indica intención de cancelar la suscripción.
{% endalert %}

| Tipo | Palabra clave | Cambio |
|-|-------|---|
| Adhesión voluntaria | `START`<br> `YES`<br> `UNSTOP` | Cualquier solicitud de entrada con una de estas palabras clave de `Opt-In` resultará en un cambio de estado del grupo de suscripción a `subscribed`. Además, el conjunto de remitentes asociados con ese grupo de suscripción podrá enviar un mensaje servicio de mensajes cortos, MMS o RCS a ese cliente (dependiendo del tipo de mensajería que admitan los remitentes). <br><br>El usuario recibirá tu respuesta automática de adhesión voluntaria definida.  |
| Cancelación de suscripción | `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | Cualquier solicitud de entrada con una de estas palabras clave de `Opt-Out` resultará en un cambio de estado del grupo de suscripción a `unsubscribed`. Además, el conjunto de números asociados con ese grupo de suscripción ya no podrá enviar mensajes a ese cliente.<br><br>El usuario recibirá tu respuesta automática de cancelación de suscripción definida. |
| Ayuda | `HELP`<br> `INFO` | El usuario recibirá tu respuesta automática de ayuda definida. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Palabras clave predeterminadas" }

Solo se procesará el **mensaje exacto de una sola palabra** (sin distinción de mayúsculas y minúsculas). Palabras clave como `STOP PLEASE` se ignorarán a menos que la [cancelación aproximada]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/fuzzy_opt_out) esté activada.

Si un destinatario usa las palabras clave `HELP` o `INFO`, se desencadenará una respuesta automáticamente. La respuesta predeterminada para estos mensajes de respuesta automática se establecerá durante tu periodo de [incorporación]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups) y adquisición de números de teléfono. Ten en cuenta que puedes seguir actualizando estas respuestas después del periodo de incorporación inicial.

{% alert tip %}
¿Te interesa ampliar tu procesamiento de cancelación de suscripción? Prueba la [cancelación aproximada]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/fuzzy_opt_out), una característica que intenta reconocer cuándo un mensaje de entrada no coincide con una palabra clave de cancelación, pero indica intención de cancelar la suscripción.
{% endalert %}

## Gestionar cancelaciones de suscripción en lenguaje natural {#handle-natural-language-opt-outs}

Puedes crear un [Braze Agent]({{site.baseurl}}/user_guide/brazeai/agents) que utilice análisis de sentimiento para ayudar a capturar la intención de cancelación de suscripción que queda fuera de las palabras clave estándar o personalizadas (como "Por favor, no me envíes más mensajes"). Consulta [Gestionar cancelaciones de suscripción en lenguaje natural en la Consola de Agente]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#handle-natural-language-opt-outs-in-the-agent-console) para ver los pasos.