---
nav_title: Databricks Mosaic
article_title: Databricks Mosaic
description: "Este artículo de referencia describe la asociación entre Braze y Databricks Mosaic, que te permite conectar modelos de Databricks a Braze para usarlos con agentes de IA personalizados."
alias: /partners/databricks_mosaic/
page_type: partner
search_tag: Partner

---

# Databricks Mosaic

> [Databricks Mosaic AI](https://www.databricks.com/product/artificial-intelligence) es la plataforma unificada de Databricks para crear, desplegar y administrar modelos de IA y aprendizaje automático a escala en la plataforma de inteligencia de datos de Databricks.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

_Esta integración es mantenida por Databricks._

## Acerca de la integración {#about-the-integration}

La integración de Braze y Databricks Mosaic te permite conectar tu token y espacio de trabajo de Databricks a Braze para que puedas usar modelos de Databricks al crear agentes de IA personalizados. Braze utiliza tus credenciales de Databricks Mosaic para generar contenido para tus clientes. Con esta integración, tus agentes pueden generar textos personalizados, tomar decisiones en tiempo real o actualizar campos de catálogo usando modelos de Databricks.

## Requisitos previos {#prerequisites}

| Requisitos | Descripción |
|---|---|
| Cuenta de Databricks con token de acceso personal | Una cuenta de Databricks con un [token de acceso personal](https://docs.databricks.com/en/dev-tools/auth/pat.html). Si necesitas ayuda, ponte en contacto con tu administrador o con el [soporte de Databricks](https://help.databricks.com/). |
| Nombre del espacio de trabajo de Databricks | El nombre del espacio de trabajo (o instancia) de tu cuenta de Databricks. Es el subdominio antes de `.cloud.databricks.com` o `.azuredatabricks.net` (por ejemplo, `dbc-eb57d699-f22c`). |
| Instancia de Braze | Puedes encontrar tu instancia de Braze en la [página de resumen de la API]({{site.baseurl}}/api/basics/#endpoints) o a través de tu administrador de incorporación de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Para conectar tus credenciales de Databricks Mosaic a Braze:

1. Ve a **Integraciones de socios** > **Socios tecnológicos** en el panel de Braze y busca **Databricks Mosaic Integration**.
2. Introduce tu **Databricks Token**.
3. Introduce tu **Databricks Workspace Name**. Es el subdominio antes de `.cloud.databricks.com` o `.azuredatabricks.net`.
4. Selecciona **Guardar**.

Después de guardar, Braze muestra un estado de conexión con la fecha y hora de la conexión. Puedes seleccionar modelos de Databricks al [crear un agente personalizado]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/) en la Consola de Agente.

Para eliminar la integración, selecciona **Desconectar** en la página de **Databricks Mosaic Integration**.

Ponte en contacto con el [soporte de Databricks](https://help.databricks.com/) si tienes problemas o preguntas sobre tu integración.