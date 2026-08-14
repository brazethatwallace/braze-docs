---
nav_title: Amazon Bedrock
article_title: Amazon Bedrock
description: "Este artículo de referencia describe la integración entre Braze y Amazon Bedrock, que te permite conectar modelos de Bedrock a Braze para usarlos con agentes de IA personalizados."
alias: /partners/amazon_bedrock/
page_type: partner
search_tag: Partner

---

# Amazon Bedrock

> [Amazon Bedrock](https://aws.amazon.com/bedrock/) es un servicio de AWS totalmente administrado que proporciona acceso a modelos fundacionales de empresas líderes en IA a través de una API unificada, para que las marcas puedan crear y escalar aplicaciones de IA generativa en AWS.

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Amazon Bedrock integration' %}

## Acerca de la integración {#about-the-integration}

La integración de Braze y Amazon Bedrock te permite conectar tus credenciales de Amazon Bedrock a Braze para que puedas usar modelos alojados en Bedrock al crear agentes de IA personalizados. Con esta integración, tus agentes pueden generar textos personalizados, tomar decisiones en tiempo real o actualizar campos de catálogo usando modelos disponibles a través de Amazon Bedrock.

Cuando conectas Amazon Bedrock, Braze muestra un conjunto seleccionado de modelos de Bedrock para agentes personalizados. Los modelos disponibles en Braze pueden diferir del catálogo completo en tu cuenta de AWS.

Braze usa el endpoint `bedrock-mantle` de Amazon Bedrock para esta integración. Amazon Bedrock también documenta un endpoint `bedrock-runtime` separado con diferente compatibilidad de modelos y características, así que cuando revises la documentación de AWS sobre disponibilidad o comportamiento, sigue la guía para [`bedrock-mantle`](https://docs.aws.amazon.com/bedrock/latest/userguide/endpoints.html).

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

## Requisitos previos {#prerequisites}

| Requisitos | Descripción |
|---|---|
| Una cuenta de AWS con acceso a Amazon Bedrock | Una cuenta de AWS con acceso a Amazon Bedrock en la región de AWS donde se alojan tus modelos. Si necesitas ayuda, contacta a tu administrador o al [soporte de AWS](https://aws.amazon.com/support). |
| Acceso a modelos de Amazon Bedrock | Acceso en tu cuenta de AWS a los modelos de Bedrock que planeas usar. Algunos modelos, como los de Anthropic, requieren que se otorgue acceso en tu cuenta de AWS. No todos los modelos están disponibles en todas las regiones de AWS; verifica la disponibilidad regional de cada modelo en la consola de Amazon Bedrock o en [Disponibilidad regional por modelos](https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html) antes de conectarte. |
| Credenciales de autenticación | Una [clave de API de Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html) de largo plazo o, cuando la autenticación por rol de IAM está habilitada para tu espacio de trabajo, un rol de IAM que Braze pueda asumir. |
| Instancia de Braze | Puedes encontrar tu instancia de Braze en la [página de resumen de la API]({{site.baseurl}}/api/basics#endpoints) o a través de tu administrador de incorporación de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Para conectar Amazon Bedrock a Braze:

1. Ve a **Partner Integrations** > **Technology Partners** en el panel de Braze, luego busca y selecciona **Amazon Bedrock**.
2. En **Authentication method**, elige **API key** o **AWS IAM role** (cuando esté disponible).
3. Completa la configuración del método elegido:
   - **API key:** Introduce tu **clave de API de Amazon Bedrock** de larga duración. Selecciona la **región de AWS** donde están alojados tus modelos de Bedrock. Selecciona **Save**.
   - **AWS IAM role:** Usa los valores que Braze muestra para configurar la política de confianza de tu rol de IAM, luego introduce los detalles del rol en Braze:
     1. Copia el **ID de cuenta de AWS de Braze** y confía en esa cuenta en la política de confianza de tu rol de IAM.
     2. Copia el **ID externo de Braze** y requiérelo en la política de confianza de tu rol con una condición `sts:ExternalId`. Selecciona **Generate new external ID** si necesitas un nuevo valor.
     3. Introduce el **ARN del rol de AWS** para el rol de IAM que tiene permisos de Amazon Bedrock. El ARN debe coincidir con `arn:aws:iam::<account-id>:role/<role-name>`.
     4. Selecciona la **región de AWS** donde están alojados tus modelos de Bedrock.
     5. Selecciona **Save**.

{% alert note %}
**AWS IAM role** aparece solo para espacios de trabajo donde esta opción de autenticación está habilitada. Con la autenticación por rol de IAM, Braze asume tu rol para generar credenciales de Amazon Bedrock de corta duración y no almacena una clave de API de larga duración.
{% endalert %}

Después de guardar, Braze muestra un estado de conexión con la fecha y hora de la conexión. Puedes seleccionar modelos de Amazon Bedrock al [crear un agente personalizado]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) en la consola de agentes.

{% alert important %}
No todos los modelos de Amazon Bedrock están disponibles en todas las regiones de AWS. Antes de seleccionar una **región de AWS** en Braze, abre los detalles del modelo en Amazon Bedrock y confirma que el modelo incluye esa región en su lista. Los modelos que no están disponibles en tu región conectada devuelven errores durante la invocación del agente (por ejemplo, que el modelo no existe o ya no está disponible). Consulta [Models at a glance](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html) para más detalles.
{% endalert %}

Para confirmar que la integración funciona, ve a la consola de agentes y crea un agente de prueba usando uno de tus modelos de Bedrock. Introduce una instrucción como "Cuéntame un chiste" y ejecuta una invocación de prueba para verificar que el modelo responde como se espera.

Para eliminar la integración, selecciona **Disconnect** en la página de **integración de Amazon Bedrock**.

Si tienes problemas con tu cuenta o credenciales de Amazon Bedrock, contacta con [AWS Support](https://aws.amazon.com/support).