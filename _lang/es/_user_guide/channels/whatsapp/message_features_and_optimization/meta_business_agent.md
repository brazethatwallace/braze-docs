---
nav_title: Meta Business Agent
article_title: Meta Business Agent y Braze WhatsApp
page_order: 8
description: "Esta guía explica cómo Meta Business Agent interactúa con un número de teléfono de WhatsApp Business conectado a Braze, y qué esperar si lo habilitas."
page_type: reference
channel:
  - WhatsApp
alias: /meta_business_agent/
hidden: true
noindex: true
---

# Meta Business Agent y Braze WhatsApp {#meta-business-agent-and-braze-whatsapp}

> Meta Business Agent puede responder a mensajes entrantes de WhatsApp en un número que también está conectado a Braze. Este artículo cubre cómo ambos sistemas comparten la visibilidad de los mensajes, cómo habilitar el agente en las herramientas de Meta y cómo se divide la facturación. Refleja la funcionalidad y la documentación del producto Meta Business Agent a agosto de 2026.

Meta continúa desarrollando activamente Meta Business Agent, por lo que algunos detalles pueden cambiar; consulta la [documentación de Meta Business Agent](https://developers.facebook.com/documentation/meta-business-agent/overview) para obtener la información más reciente.

## ¿Qué es Meta Business Agent? {#what-is-meta-business-agent}

Meta Business Agent es un respondedor impulsado por IA que Meta opera directamente en un número de teléfono de WhatsApp Business. Cuando se habilita para un número elegible, puede responder a mensajes entrantes de los usuarios en nombre de la empresa, utilizando conocimiento (información del negocio, preguntas frecuentes, archivos, contenido del sitio web) y conectores configurados en las herramientas de Meta.

La habilitación de Meta Business Agent se configura completamente en WhatsApp Manager y Meta Business Suite, y es independiente de tu espacio de trabajo de Braze. Braze no es necesario para la configuración, y actualmente no existe un control en el panel de Braze para ello.

## Cómo interactúa con tu número conectado a Braze {#how-it-interacts-with-your-braze-connected-number}

Meta Business Agent y Braze pueden coexistir en el mismo número de teléfono de WhatsApp Business, pero actualmente no comparten visibilidad de todos los mensajes.

- **Los mensajes salientes iniciados por Braze no se ven afectados.** Braze continúa enviando mensajes de plantilla de WhatsApp y mensajes de respuesta a través de Campaigns y Canvas exactamente como lo hace hoy, independientemente de si Meta Business Agent está habilitado.
- **Los mensajes entrantes son enrutados por Meta Business Agent.** Para cada mensaje entrante de un usuario, Meta Business Agent decide si pasarlo a Braze o manejarlo por sí mismo.
  - **Si Meta enruta el mensaje a Braze:** Se procesa de la misma manera que cualquier mensaje entrante de WhatsApp hoy en día. Los desencadenadores basados en acciones de Campaigns y Canvas existentes, así como las Rutas de Acción, se activan según la lógica que ya hayas construido.
  - **Si Meta Business Agent maneja el mensaje por sí mismo:** Braze actualmente no procesa el canal separado (mensajes en espera y ecos de mensajes) que llevaría esa actividad. Los mensajes entrantes que el agente decide manejar, y sus propias respuestas a esos mensajes, actualmente no son visibles en ninguna superficie de Braze.

| Flujo de mensajes | Qué sucede hoy |
| --- | --- |
| Mensajes de plantilla de WhatsApp y mensajes de respuesta enviados a través de Campaigns o pasos en Canvas | Sin cambios; Braze continúa enviando según la configuración |
| Mensaje entrante que Meta enruta a Braze | Se procesa normalmente; se aplican los desencadenadores y las Rutas de Acción existentes |
| Mensaje entrante que Meta Business Agent maneja por sí mismo | Actualmente no es visible para Braze; los desencadenadores y las Rutas de Acción existentes para mensajes entrantes no se activan |
| Mensaje saliente enviado por Meta Business Agent | Actualmente no es visible para Braze |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Flujo de mensajes" }

## Habilitar Meta Business Agent {#enable-meta-business-agent}

Meta Business Agent se habilita por número de teléfono en las herramientas de Meta, no en Braze:

1. Verifica la elegibilidad y habilítalo para un número de teléfono en [WhatsApp Manager](https://business.facebook.com/wa/manage/home/), aceptando los Términos de servicio de Meta Business Agent.
2. Configura el conocimiento y las habilidades del agente (información del negocio, preguntas frecuentes, archivos, conectores) a través de las [API de configuración del agente](https://developers.facebook.com/documentation/meta-business-agent/reference/configure/agent-skills) de Meta.
3. Activa el agente usando la [Configuración del agente](https://developers.facebook.com/documentation/meta-business-agent/reference/onboard/agent-settings).

## Aspectos a considerar antes de habilitarlo {#things-to-weigh-before-enabling-it}

- **Sin control del lado de Braze:** Habilitar, configurar y deshabilitar Meta Business Agent se realiza completamente en las herramientas de Meta; no hay nada que activar o desactivar en Braze.
- **Facturación:** Con la introducción de Meta Business Agent, los mensajes sin plantilla ahora se clasifican en una de dos categorías: servicio (categoría existente) o Meta Business Agent (categoría nueva).
  - Las respuestas sin plantilla manejadas por Braze se cobran como mensajes de servicio a partir del 1 de octubre de 2026.
    - Si respondes a un mensaje entrante con una plantilla de marketing, utilidad o autenticación, se factura como tal.
  - Los mensajes de Meta Business Agent son facturados directamente por Meta a partir del 1 de agosto de 2026. Consulta sus precios para más detalles.
  - Los mensajes se clasifican en una sola categoría, por lo que nunca se te cobra dos veces por el mismo mensaje.