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

# Informes de correo electrónico

> Este artículo cubre los diferentes componentes de tus informes de correo electrónico y dónde encontrarlos en el dashboard.

{% multi_lang_include analytics/campaign_analytics.md channel="email" %}

## Solución de problemas

### Correos electrónicos rebotados

- **554 5.7.1 [internal] recipient address was suppressed due to customer policy:** Prueba con otra dirección, vuelve a interactuar a través de otro canal o quita la dirección de la lista de supresión solo para tus propias direcciones de prueba. Evita quitar supresiones de usuarios reales, ya que esto puede perjudicar la reputación.
- **Mailbox full / invalid account:** A menudo es una señal de calidad de la lista. Prioriza a los usuarios que abrieron o hicieron clic recientemente (por ejemplo, en los últimos 30–60 días) mientras limpias las direcciones inactivas o incorrectas.

### Dominios no válidos

Errores como `unable to get mx info` suelen significar que muchos objetivos usan dominios incorrectos (por ejemplo, errores tipográficos). Segmenta, exporta, corrige y vuelve a importar esos perfiles.

### IP con limitación de velocidad

Si un servidor de destinatario limita la velocidad de tu IP, reduce el volumen hacia ese dominio, mejora la interacción y contacta con el soporte de capacidad de entrega si la limitación persiste.