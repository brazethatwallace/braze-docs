---
nav_title: Informes
article_title: Informes de correo electrónico
page_order: 21
description: "Este artículo de referencia cubre los diferentes componentes de los informes de correo electrónico y dónde encontrarlos en el dashboard."
tool:
  - Reports
channel:
  - email

---

# Informes de correo electrónico {#email-reporting}

> Este artículo cubre los diferentes componentes de tus informes de correo electrónico y dónde encontrarlos en el dashboard.

{% multi_lang_include analytics/campaign_analytics.md channel="email" %}

## Solución de problemas {#troubleshooting}

### Correos electrónicos rebotados {#bounced-emails}

- **554 5.7.1 [internal] recipient address was suppressed due to customer policy:** Prueba con otra dirección, vuelve a interactuar a través de otro canal o elimina la dirección de la lista de supresión solo para tus propias direcciones de prueba. Evita eliminar supresiones de usuarios reales, ya que eso puede perjudicar la reputación.
- **Mailbox full / invalid account:** A menudo es una señal de calidad de la lista. Prioriza a los usuarios que abrieron o hicieron clic recientemente (por ejemplo, en los últimos 30-60 días) mientras limpias las direcciones inactivas o incorrectas.

#### Comportamiento de reintento de rebote blando {#soft-bounce-retry-behavior}

Cuando un correo electrónico tiene un rebote blando debido a problemas temporales (como buzón lleno, servidor temporalmente no disponible u otros fallos transitorios de capacidad de entrega), Braze reintenta automáticamente la entrega durante un máximo de 72 horas. El número de intentos de reintento varía según el receptor.

Si el correo electrónico no se entrega correctamente después del período de reintento, Braze registra un evento de rebote blando para ese envío de campaña. Estos rebotes blandos no aparecen en los análisis de la campaña, pero puedes:
- Supervisarlos en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) para ver los motivos de rebote
- Usar el [filtro de Segment de rebote blando]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#soft-bounced) para excluir a estos usuarios de envíos futuros

Debido a este período de reintento, las métricas de entrega de correo electrónico (entregas, rebotes y tasa de correo no deseado) pueden no sumar el 100 % en Campaigns donde los correos electrónicos con rebote blando finalmente no se entregan.

Para más información sobre los rebotes blandos, consulta el [Glosario de análisis de correo electrónico]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#soft-bounce).

### Dominios no válidos {#invalid-domains}

Errores como `unable to get mx info` a menudo significan que muchos destinatarios usan dominios incorrectos (por ejemplo, errores tipográficos). Segmenta, exporta, corrige y vuelve a importar esos perfiles.

### IPs limitadas {#throttled-ips}

Es posible que veas el mensaje `Email was deferred due to the following reason(s): [IPs were throttled by recipient server]` en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) si un proveedor de buzón ralentiza o bloquea temporalmente la entrega desde tu IP debido al volumen, la reputación o ambos. Braze reintenta los mensajes diferidos; si los aplazamientos se agrupan a partir de esto, a menudo verás rebotes blandos elevados junto a ellos.

Este patrón generalmente significa que estás enviando más rápido de lo que el proveedor de buzón acepta para tu reputación actual. Además de mejorar la participación y la calidad de la lista, usa el [límite de velocidad de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) para limitar la rapidez con la que los mensajes salen de Braze para una Campaign o Canvas. Esto ayuda a reducir la limitación mientras trabajas con tu equipo de capacidad de entrega en soluciones a largo plazo.

Si la limitación persiste para dominios específicos, reduce el volumen hacia esos dominios y contacta con el soporte de capacidad de entrega de Braze para obtener orientación.

### Estado de reputación de IP desconocido {#unknown-ip-reputation-status}

Si tu informe de rendimiento de correo electrónico muestra un valor "desconocido" para la reputación de IP, esto puede estar relacionado con una interrupción de Google Postmaster Tools. Google Postmaster Tools proporciona datos de reputación para la capacidad de entrega de Gmail, y las interrupciones temporales del servicio pueden dar lugar a valores de reputación faltantes o desconocidos.

Si ves un estado de reputación desconocido y tienes preguntas sobre la capacidad de entrega de tu correo electrónico, contacta con [soporte de Braze]({{site.baseurl}}/support_contact).