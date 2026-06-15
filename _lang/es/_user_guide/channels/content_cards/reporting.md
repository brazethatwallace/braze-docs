---
nav_title: Informes
article_title: Informes de tarjetas de contenido
page_order: 21
description: "Este artículo de referencia ofrece un resumen de las diferentes métricas de informes y opciones de análisis de tarjetas de contenido disponibles en el dashboard de Braze."
channel:
  - content cards
tool:
  - Reports

---

# Informes de tarjetas de contenido {#content-card-reporting}

> Este artículo de referencia ofrece un resumen de las diferentes métricas de informes y opciones de análisis de tarjetas de contenido disponibles en el dashboard de Braze.

## Cuándo se registran los envíos {#when-sends-are-logged}

El momento en que se registra un evento _Enviado_ para las Content Cards depende del tipo de entrega y de la configuración de **Creación de tarjeta**.

### Entrega planificada {#scheduled-delivery}

Para las Content Cards planificadas, el momento del evento _Enviado_ depende de la configuración de **Creación de tarjeta**:

- **Al lanzar la campaña:** El envío se registra en el momento de envío planificado, cuando la tarjeta se escribe en la fuente del usuario. Esto ocurre independientemente de si el usuario ha abierto la aplicación o ha visto la tarjeta.
- **En la primera impresión:** El envío se registra la primera vez que la aplicación solicita la tarjeta después del momento de envío planificado, cuando la tarjeta se crea bajo demanda.

Si tu campaña está configurada para usar **En la primera impresión** (recomendado), el recuento de _Enviados_ en los análisis de la campaña crece gradualmente a medida que las aplicaciones individuales solicitan la tarjeta. Si la aplicación nunca solicita una tarjeta (por ejemplo, si un usuario nunca abre la aplicación) antes de que la tarjeta expire, no se registra ningún envío y la tarjeta nunca se entrega. Si tu campaña está configurada para usar **Al lanzar la campaña**, el recuento de _Enviados_ en los análisis de la campaña aumenta de golpe en el momento planificado.

### Entrega basada en acciones {#action-based-delivery}

Para las Content Cards basadas en acciones, el envío se registra poco después de que el usuario realice la acción desencadenante, cuando la tarjeta se escribe en su fuente. Esto ocurre independientemente de si el usuario ha visto la tarjeta.

### Filtros de Campaigns recibidas y reorientación {#campaigns-received-and-retargeting-filters}

Independientemente del tipo de entrega o de la configuración de **Creación de tarjeta**, una campaña de tarjeta de contenido aparece en el perfil del usuario en **Campaigns recibidas** solo después de que haya visto la tarjeta en la aplicación. Los filtros de reorientación **Último mensaje recibido** y **Última Campaign recibida** se actualizan en el momento de la visualización por la misma razón.

{% multi_lang_include analytics/campaign_analytics.md channel="Content Card" %}