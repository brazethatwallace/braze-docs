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

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

## Requisitos previos {#prerequisites}

| Requisitos | Descripción |
|---|---|
| Una cuenta de AWS con acceso a Amazon Bedrock | Una cuenta de AWS con acceso a Amazon Bedrock en la región de AWS donde están alojados tus modelos. Para obtener ayuda, contacta a tu administrador o al [soporte de AWS](https://aws.amazon.com/support). |
| Acceso a modelos de Amazon Bedrock | Acceso en tu cuenta de AWS a los modelos de Bedrock que planeas usar. Algunos modelos, como los de Anthropic, requieren que se otorgue acceso en tu cuenta de AWS. No todos los modelos están disponibles en todas las regiones de AWS. |
| Credenciales de autenticación | Una [clave de API de Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html) de largo plazo, o, cuando la autenticación por rol IAM está habilitada para tu espacio de trabajo, un rol IAM que Braze pueda asumir. |
| Instancia de Braze | Puedes encontrar tu instancia de Braze en la [página de resumen de la API]({{site.baseurl}}/api/basics#endpoints) o a través de tu administrador de incorporación de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Para conectar Amazon Bedrock a Braze:

1. Ve a **Integraciones de partners** > **Partners tecnológicos** en el panel de Braze, luego busca y selecciona **Amazon Bedrock**.
2. En **Método de autenticación**, elige **Clave de API** o **Rol IAM de AWS** (cuando esté disponible).
3. Completa la configuración para el método elegido:
   - **Clave de API:** Ingresa tu **clave de API de Amazon Bedrock** de largo plazo. Selecciona la **región de AWS** donde están alojados tus modelos de Bedrock. Selecciona **Guardar**.
   - **Rol IAM de AWS:** Usa los valores que Braze muestra para configurar la política de confianza de tu rol IAM, luego ingresa los detalles del rol en Braze:
     1. Copia el **ID de cuenta de AWS de Braze** y confía en esa cuenta en la política de confianza de tu rol IAM.
     2. Copia el **ID externo de Braze** y requiérelo en la política de confianza de tu rol con una condición `sts:ExternalId`. Selecciona **Generar nuevo ID externo** si necesitas un nuevo valor.
     3. Ingresa el **ARN del rol de AWS** para el rol IAM que tiene permisos de Amazon Bedrock. El ARN debe coincidir con `arn:aws:iam::<account-id>:role/<role-name>`.
     4. Selecciona la **región de AWS** donde están alojados tus modelos de Bedrock.
     5. Selecciona **Guardar**.

{% alert note %}
**Rol IAM de AWS** aparece solo para espacios de trabajo donde esta opción de autenticación está habilitada. Con la autenticación por rol IAM, Braze asume tu rol para generar credenciales de Amazon Bedrock de corta duración y no almacena una clave de API de largo plazo.
{% endalert %}

Después de guardar, Braze muestra un estado de conexión con la fecha y hora de la conexión. Puedes seleccionar modelos de Amazon Bedrock al [crear un agente personalizado]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) en la consola de agentes.

{% alert note %}
No todos los modelos de Amazon Bedrock están disponibles en todas las regiones de AWS. Elige una región que sea compatible con los modelos que planeas usar. Los modelos que no están disponibles en tu región conectada devuelven errores durante la invocación del agente.
{% endalert %}

Para confirmar que la integración funciona, ve a la consola de agentes y crea un agente de prueba usando uno de tus modelos de Bedrock. Ingresa una instrucción como "Cuéntame un chiste" y ejecuta una invocación de prueba para verificar que el modelo responde como se espera.

Para eliminar la integración, selecciona **Desconectar** en la página de **integración de Amazon Bedrock**.

Si tienes problemas con tu cuenta o credenciales de Amazon Bedrock, contacta al [soporte de AWS](https://aws.amazon.com/support).