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

- **554 5.7.1 [internal] recipient address was suppressed due to customer policy:** Prueba con otra dirección, vuelve a interactuar a través de otro canal o quita la dirección de la lista de supresión solo para tus propias direcciones de prueba. Evita quitar supresiones de usuarios reales, ya que esto puede perjudicar la reputación.
- **Mailbox full / invalid account:** A menudo es una señal de calidad de la lista. Prioriza a los usuarios que abrieron o hicieron clic recientemente (por ejemplo, en los últimos 30–60 días) mientras limpias las direcciones inactivas o incorrectas.

### Dominios no válidos {#invalid-domains}

Errores como `unable to get mx info` suelen significar que muchos destinatarios usan dominios incorrectos (por ejemplo, errores tipográficos). Segmenta, exporta, corrige y vuelve a importar esos perfiles.

### IP con limitación de velocidad {#throttled-ips}

Es posible que veas el mensaje `Email was deferred due to the following reason(s): [IPs were throttled by recipient server]` en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/) si un proveedor de correo reduce temporalmente la velocidad o bloquea la entrega desde tu IP debido al volumen, la reputación o ambos. Braze reintenta los mensajes diferidos; si los aplazamientos se acumulan por esta causa, a menudo verás rebotes blandos elevados junto a ellos.

Este patrón suele significar que estás enviando más rápido de lo que el proveedor de correo acepta para tu reputación actual. Además de mejorar la interacción y la calidad de la lista, usa la [limitación de velocidad de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-speed-rate-limiting) para limitar la rapidez con la que los mensajes salen de Braze en una campaña o Canvas. Esto ayuda a reducir la limitación de velocidad mientras trabajas con tu equipo de capacidad de entrega en soluciones a largo plazo.

Si la limitación de velocidad persiste para dominios específicos, reduce el volumen hacia esos dominios y ponte en contacto con el soporte de capacidad de entrega de Braze para obtener orientación.