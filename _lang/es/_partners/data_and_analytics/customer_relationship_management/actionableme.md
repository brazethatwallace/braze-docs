---
nav_title: actionable.me
article_title: actionable.me
description: "Este artículo de referencia describe la asociación entre Braze y actionable.me, un software y unos procesos patentados, que te permiten sacar el máximo partido a tu inversión en Braze de inmediato."
alias: /partners/actionableme/
page_type: partner
search_tag: Partner

---

# actionable.me

> [actionable.me](https://actionable.me), desarrollado por el equipo de Massive Rocket, una agencia de datos y CRM or administración de las relaciones con el cliente, es un enfoque estandarizado y automatizado para ejecutar programas de CRM or administración de las relaciones con el cliente, que proporciona herramientas y procesos diseñados para que los clientes de Braze obtengan valor de forma rápida, consistente y predecible.

_Esta integración está mantenida por actionable.me._

## Sobre la integración {#about-the-integration}

La integración de Braze y actionable.me te permite desplegar un servicio para supervisar tu progreso en la utilización de Braze. Mediante una combinación de herramientas y procesos, evaluarán rápidamente el rendimiento de tu CRM or administración de las relaciones con el cliente, identificarán nuevas oportunidades y proporcionarán recomendaciones sobre cómo obtener mejores resultados.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Cuenta actionable.me | Se necesita una cuenta en actionable.me para beneficiarse de esta asociación. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con los permisos enumerados en la siguiente sección.<br><br> Se puede crear en el dashboard de Braze desde **Settings** > **API Keys**. |
| Punto de conexión REST or transferencia de estado representacional de Braze | [La URL de tu punto de conexión REST or transferencia de estado representacional]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto de conexión dependerá de la URL de Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Para integrar Braze y actionable.me, hay que configurar la plataforma actionable.me, y crear una clave de API de Braze en Braze y configurarla en el dashboard de actionable.me.

### Paso 1: Crea tu clave de API de Braze {#step-1-create-your-braze-api-key}

En Braze, ve a **Settings** > **API Keys**. Selecciona **Create New API Key** y asegúrate de que se añaden los siguientes permisos:

- `campaigns.list`
- `campaigns.data_series`
- `campaigns.details`
- `sends.data_series`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `events.list`
- `canvas.list`
- `canvas.data_series`
- `canvas.details`
- `canvas.data_summary`
- `kpi.mau.data_series`
- `kpi.dau.data_series`
- `kpi.new_users.data_series`
- `kpi.uninstalls.data_series`

### Paso 2: Proporciona información al equipo de actionable.me {#step-2-provide-information-to-the-actionableme-team}

Para completar la integración, debes proporcionar tu clave de API REST or transferencia de estado representacional y [la URL del punto de conexión REST or transferencia de estado representacional]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) a tu equipo de operaciones de actionable.me. A continuación, actionable.me establecerá la conexión y se pondrá en contacto contigo una vez finalizada la configuración para empezar a compartir información.

![La página "añadir plataforma" de actionable.me que configurará el equipo de operaciones de actionable.me.]({% image_buster /assets/img/actionableme/image2.png %})

## Solución de problemas {#troubleshooting}

Ponte en contacto con el equipo de actionable.me o Massive Rocket para obtener ayuda adicional: [info@massiverocket.com](mailto:info@massiverocket.com)