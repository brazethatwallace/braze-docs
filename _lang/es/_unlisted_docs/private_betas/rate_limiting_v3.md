---
article_title: Límites de velocidad para Campaigns push y Canvas multicanal
permalink: /rate_limiting_v3/
page_type: reference
description: "Este artículo describe los límites de velocidad de entrega para Campaigns push y Canvas multicanal."
---

# Límites de velocidad para Campaigns push y Canvas multicanal {#rate-limiting-for-push-campaigns-and-multichannel-canvases}

> Esta página cubre los límites de velocidad para Campaigns push y Canvas multicanal, incluidas las consideraciones que debes tener en cuenta a la hora de regular tus mensajes.

Al configurar los límites de velocidad de entrega para Campaigns push y Canvas multicanal, ahora puedes elegir entre establecer:

- Límites de velocidad por canal
- Un límite de velocidad general compartido entre todos los canales de mensajes.

{% alert important %}
Los límites de velocidad para Campaigns push y Canvas multicanal se encuentran en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si te interesa participar en este acceso anticipado.
{% endalert %}

Las siguientes funcionalidades **no están** incluidas en este acceso anticipado:

- Establecer límites de velocidad por canal en Campaigns multicanal de cualquier tipo y Canvas desencadenados por API
- Establecer un límite de velocidad global
- Establecer límites de velocidad por paso de mensaje en Canvas

## Consideraciones {#considerations}

- Esta actualización de los límites de velocidad no te impide establecer un límite de velocidad muy bajo. Esto significa que, sin esta prevención, podrías establecer un límite de velocidad que, dependiendo del tamaño de la audiencia, podría provocar que tus mensajes se envíen a una tasa extremadamente lenta.
- Los resúmenes de **Ajustes de envío** para Campaigns y Canvas pueden contener descripciones inexactas de los límites de velocidad que se han configurado: <br><br>![Ajustes de envío para Campaigns donde no hay limitaciones en la tasa a la que los usuarios recibirán mensajes.]({% image_buster /assets/unlisted_docs/img/send_settings_example.png %}){: style="max-width:65%"}<br><br>
- Los límites de velocidad para Campaigns multicanal (no Canvas ni Campaigns push) reflejarán el [comportamiento no actualizado de los límites de velocidad para Campaigns multicanal](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting). Recomendamos evitar la creación de Campaigns multicanal con límites de velocidad mientras formes parte de esta etapa de acceso anticipado.