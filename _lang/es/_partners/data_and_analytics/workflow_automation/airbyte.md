---
nav_title: Airbyte
article_title: Airbyte
description: "Este artículo de referencia cubre la integración de Braze y Airbyte. Airbyte es un motor de integración de datos de código abierto que te ayuda a consolidar tus datos en tus almacenes de datos, lagos y bases de datos, reenviando eventos en tiempo real desde Airbyte a Braze."
alias: /partners/airbyte/
page_type: partner
search_tag: Airbyte

---

# Airbyte

> [Airbyte](https://airbyte.com/) es un motor de integración de datos de código abierto que te ayuda a consolidar tus datos en tus almacenes de datos, lagos y bases de datos.

_Esta integración está mantenida por Airbyte._

## Sobre la integración {#about-the-integration}

La integración de Braze y Airbyte permite a los usuarios crear una canalización de datos para recopilar y analizar datos de Braze conectando todas tus aplicaciones y bases de datos a un almacén central. Una vez recopilados los datos en el almacén central, los equipos de datos pueden explorar los datos de Braze de forma eficaz utilizando sus herramientas de inteligencia empresarial preferidas.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Airbyte Cloud | Se requiere una cuenta de [Airbyte Cloud](https://cloud.airbyte.io/workspaces) para aprovechar esta integración. |
| Clave de API REST de Braze | Una clave de API REST de Braze con todos los permisos. <br><br> Se puede crear en el panel de Braze desde **Settings** > **API Keys**. |
| Punto de conexión REST de Braze | Tu punto de conexión dependerá de la URL de Braze para tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

1. En tu cuenta de Airbyte Cloud, ve a **Sources > + New Source > Set up the Source**.
2. Introduce "Braze" como nombre de la fuente y selecciona **Braze** en el desplegable de fuentes.
3. Proporciona la URL de tu punto de conexión, la clave de API REST de Braze y la fecha de inicio. Haz clic en **Set up Source**.

### Modos de sincronización admitidos {#supported-sync-modes}

El conector de fuente Braze de Airbyte admite los siguientes [modos de sincronización](https://docs.airbyte.com/cloud/core-concepts#connection-sync-modes):
- **Full Refresh | Overwrite**: sincroniza todos los registros del origen y sustituye los datos en el destino sobrescribiéndolos.
- **Incremental Sync | Append**: sincroniza nuevos registros desde el origen y los añade al destino sin borrar ningún dato.

### Flujos admitidos {#supported-streams}

- [`campaigns`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f3b0b3ef-04fb-4a31-8570-e6ad88dacb18)
- [`campaigns_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c07b5ebd-0246-471e-b154-416d63ae28a1)
- [`canvases`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e6c150d7-fceb-4b10-91e2-a9ca4d5806d1)
- [`canvases_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0fd61e93-7edf-4d87-a8dc-052420aefb73)
- [`events`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#93ecd8a5-305d-4b72-ae33-2d74983255c1)
- [`events_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bd1ab63-d1a5-4301-8d17-246cf24a178c)
- [`kpi_daily_new_users`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#07756c39-cfa0-40a0-8101-03f8791cec01)
- [`kpi_daily_active_users`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#90a64560-65aa-4f71-a8ef-1edf49321986)
- [`kpi_daily_app_uninstalls`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#59c4d592-3e77-42f8-8ff1-d5d250acbeae)
- [`cards`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9fa7a3bc-4a02-4de2-bc4c-8f111750665e)
- [`cards_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9cdc3b1e-641e-4d62-b9e8-42d04ee9d4d8)
- [`segments`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f)
- [`segments_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#62d9d142-cdec-4aea-a287-c13efea7415e)

{% alert note %}
Los límites de velocidad varían en función del flujo. Visita la [tabla de límites de velocidad]({{site.baseurl}}/api/api_limits/#rate-limits-by-request-type) para obtener más información.
{% endalert %}