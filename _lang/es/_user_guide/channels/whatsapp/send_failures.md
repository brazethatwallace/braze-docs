---
nav_title: Fallos de envío
article_title: Investigar fallos de envío de WhatsApp
page_order: 22
page_type: reference
description: "Usa los análisis de Campaign, el registro de actividad de mensajes y Currents para investigar fallos de envío de WhatsApp y códigos de error comunes de Meta."
tool:
  - Reports
channel:
  - WhatsApp
---

# Investigar fallos de envío de WhatsApp {#investigate-whatsapp-send-failures}

> Usa esta página cuando las entregas o lecturas de WhatsApp sean inferiores a lo esperado, o cuando los **Fallos** en los análisis de Campaign parezcan elevados.

## Flujo de trabajo de investigación {#investigation-workflow}

Sigue los pasos a continuación en orden.

1. **Confirma los fallos en los análisis de Campaign o Canvas.** Abre el paso del mensaje y revisa el recuento de **Fallos** y la tasa de fallos. Si los fallos parecen elevados en comparación con los envíos o las entregas, continúa con el siguiente paso.
2. **Encuentra el código de error en el registro de actividad de mensajes.** Abre el [registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) para el mismo envío, filtra por mensajes fallidos y anota el código de error del proveedor (por ejemplo, `131049` para límites de marketing por usuario). Usa [Códigos de error comunes](#common-failure-codes) para interpretar el código y decidir los próximos pasos.
3. **Exporta los fallos con Currents para análisis o reorientación.** Una vez que conozcas el código de error, exporta los eventos de fallo de envío de WhatsApp a través de Currents. Usa esos datos para analizar tendencias de fallos en tu almacén de datos o para crear segmentos y reorientar a los usuarios en otro canal.

## Códigos de error comunes {#common-failure-codes}

| Código de error | Causa típica | Siguiente paso |
|---|---|---|
| `131049` | Límite de frecuencia de marketing por usuario de Meta o pausa de marketing en EE. UU. | Consulta [Recursos de Meta]({{site.baseurl}}/user_guide/channels/whatsapp/meta_resources) y [Reorientar usuarios en otros canales de Braze]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/optimized_delivery#retargeting-users-on-other-braze-channels) |
| `130472` | Grupo de exclusión de experimento de marketing de Meta | Consulta [Preguntas frecuentes sobre recursos de Meta]({{site.baseurl}}/user_guide/channels/whatsapp/meta_resources#faq) |
| `131026` | Diversas razones de no entrega (Meta no revela los detalles específicos) | Evita reintentos inmediatos; revisa la [solución de problemas de la API en la nube de Meta](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Códigos de error comunes de WhatsApp" }