---
nav_title: Microsoft Foundry
article_title: Microsoft Foundry
description: "Este artículo de referencia describe la integración entre Braze y Microsoft Foundry, que te permite conectar modelos de IA gestionados en Foundry a Braze para usarlos con agentes de IA personalizados."
alias: /partners/microsoft_foundry/
page_type: partner
search_tag: Partner

---

# Microsoft Foundry

> [Microsoft Foundry](https://azure.microsoft.com/en-us/products/ai-foundry) es una plataforma como servicio unificada de Azure para operaciones de IA empresarial, creadores de modelos y desarrollo de aplicaciones.

## Acerca de la integración {#about-the-integration}

La integración de Braze y Microsoft Foundry te permite usar modelos de IA generativa gestionados en Microsoft Foundry al crear agentes de IA personalizados. La integración actualmente admite dos modelos: gpt-5.4-mini y gpt-5.4-nano. Con esta integración, tus agentes pueden generar textos personalizados, tomar decisiones en tiempo real o actualizar campos de catálogo usando modelos gestionados por Foundry.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

## Requisitos previos {#prerequisites}

| Requisitos | Descripción |
|---|---|
| Una cuenta de Azure con una suscripción activa | Para obtener ayuda, contacta a tu administrador o consulta las [opciones de cuenta de Azure](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account). |
| Instancia de Microsoft Foundry | Una instancia de Microsoft Foundry para crear un proyecto. |
| Proyecto de Microsoft Foundry | Un proyecto dentro de tu instancia de Foundry para alojar los modelos desplegados. |
| Modelos desplegados | Al menos uno de los modelos compatibles desplegado dentro del proyecto de Foundry. |
| Instancia de Braze | Puedes encontrar tu instancia de Braze en la [página de resumen de la API]({{site.baseurl}}/api/basics#endpoints) o a través de tu administrador de incorporación de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Despliega modelos compatibles en Foundry {#deploy-supported-models-in-foundry}

La integración de Braze con Microsoft Foundry es compatible con dos modelos: gpt-5.4-mini y gpt-5.4-nano. Ambos deben desplegarse en un proyecto de Foundry dentro de la instancia de Foundry que estés integrando.

Para crear el proyecto de Foundry y desplegar los modelos, sigue la [documentación de Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/tutorials/quickstart-create-foundry-resources?tabs=portal):

1. Inicia sesión en Microsoft Foundry a través de tu portal de Azure.
2. En Microsoft Foundry, crea un proyecto para alojar los modelos que quieras integrar con Braze.
3. Decide si quieres usar gpt-5.4-mini, gpt-5.4-nano o ambos.
4. Para cada modelo que quieras usar, despliégalo siguiendo la documentación de Microsoft Foundry. No cambies el nombre de despliegue predeterminado, o la integración de ese modelo podría fallar.

## Integración {#integration}

Para conectar tu instancia de Foundry a Braze:

1. Ve a **Partner Integrations** > **Technology Partners** en el panel de Braze y busca **Microsoft Foundry**.
2. Introduce tu **clave de API de Microsoft Foundry**.
3. Introduce el **nombre de tu instancia de Microsoft Foundry**. Este es el subdominio antes de `.services.ai.azure.com`.
4. Selecciona **Save**.

Después de guardar, Braze muestra un estado de conexión con la fecha y hora de la conexión. Puedes seleccionar modelos de Foundry al [crear un agente personalizado]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) en la consola de agentes.

{% alert important %}
Para usar gpt-5.4-mini o gpt-5.4-nano, debes desplegar cada modelo en tu proyecto de Foundry sin cambiar el nombre de despliegue predeterminado.
{% endalert %}

Para confirmar que la integración funciona, ve a la consola de agentes y crea un agente de prueba usando uno de tus modelos desplegados. Introduce una instrucción sencilla, como "Cuéntame un chiste", y ejecuta una invocación de prueba para verificar que el modelo responde como se espera.

Para eliminar la integración, selecciona **Disconnect** en la página de **Microsoft Foundry Integration**.

Contacta con el [soporte de Azure](https://azure.microsoft.com/en-us/support/options/) si tienes problemas o preguntas sobre tu integración.