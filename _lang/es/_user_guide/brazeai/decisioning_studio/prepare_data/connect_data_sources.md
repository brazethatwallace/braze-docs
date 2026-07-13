---
nav_title: Conectar tus datos
article_title: Conectar tus datos
page_order: 6
description: "Descubre cómo conectar orígenes de datos de clientes a BrazeAI Decisioning Studio para la toma de decisiones con IA personalizada."
---

# Conectar tus datos {#connect-your-data}

> Los agentes de BrazeAI Decisioning Studio™ necesitan comprender completamente el contexto del cliente para tomar decisiones eficaces. Este artículo explica cómo conectar orígenes de datos de clientes a Decisioning Studio.

{% alert tip %}
Tu equipo de AI Decisioning Services te ayudará a configurar las conexiones de datos para un rendimiento óptimo.
{% endalert %}

## Patrones de integración compatibles {#supported-integration-patterns}

Decisioning Studio admite múltiples patrones de integración para conectar datos de clientes:

| Patrón de integración | Ideal para | Complejidad de configuración |
|---------------------|----------|------------------|
| **Braze Data Platform** | Clientes que ya utilizan Braze | Baja |
| **Ingesta de datos de Cloud de Braze (CDI)** | Conectar almacenes de datos externos | Media |
| **Almacenamiento en la nube (GCS, AWS, Azure)** | Exportaciones directas de datos desde otras plataformas | Media |
| **Integraciones CEP** | Extensiones de datos de SFMC, Klaviyo | Media |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Patrones de integración compatibles" }

## Tipos de datos de clientes {#customer-data-types}

Los siguientes activos de datos de clientes ayudan a los agentes a personalizar de forma más eficaz:

| Tipo de datos | Descripción | Ejemplos |
|-----------|-------------|----------|
| **Perfil de cliente** | Atributos estáticos y de cambio lento | Años como cliente, geografía, canal de adquisición, nivel de satisfacción, estimación del valor de duración del ciclo de vida |
| **Comportamiento del cliente** | Patrones de actividad e interacción | Inicios de sesión en la cuenta, tipo de dispositivo, interacciones con atención al cliente, uso del producto |
| **Historial de transacciones** | Datos de compras y conversiones | Productos comprados, importes de transacciones, métodos de pago, canales de compra |
| **Interacción de marketing** | Respuestas a comunicaciones | Aperturas/clics de correo electrónico, interacción con SMS, actividad web y móvil, respuestas a cuestionarios |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tipos de datos de clientes" }

{% alert tip %}
Cuanta más información tengan los agentes sobre tus clientes, mejor será su rendimiento. Considera incluir datos sobre cualquier información que sea especialmente importante para tu negocio (por ejemplo, ¿quieres ver cómo la IA trata de forma diferente a tus clientes de fidelización? Asegúrate de que el estado de fidelización esté incluido en los datos de clientes).
{% endalert %}

## Conectar datos por plataforma {#connect-data-by-platform}

{% tabs %}
{% tab Braze %}

### Enviar datos de clientes a través de Braze {#send-customer-data-through-braze}

BrazeAI Decisioning Studio puede utilizar todos los datos que ya estés enviando a Braze Data Platform.

Si hay datos de clientes que quieres utilizar para Decisioning Studio que actualmente no están almacenados en el perfil de usuario o en atributos personalizados, el enfoque recomendado es usar la [Ingesta de datos de Cloud de Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) para ingerir datos de otros orígenes.

CDI admite integraciones directas con:

- Snowflake
- Redshift
- BigQuery
- Databricks
- Microsoft Fabric
- AWS S3

Para consultar la lista completa de orígenes compatibles, consulta [Ingesta de datos de Cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

Una vez que estés satisfecho con los datos que envías a Braze Data Platform, ponte en contacto con tu equipo de AI Decisioning Services para analizar qué campos del perfil de usuario o atributos personalizados deben utilizarse para la toma de decisiones con IA.

Para agilizar este proceso, crea una lista de atributos del perfil de usuario de Braze que consideres que mejor representan los comportamientos de tus clientes y que deberían utilizarse en Decisioning Studio (consulta la [lista de campos disponibles]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment#fields-to-export)). Tu equipo de servicios también puede ayudarte a realizar sesiones de descubrimiento para decidir qué campos son los más adecuados para la toma de decisiones con IA.

Otras opciones para enviar datos incluyen:

- Enviar eventos personalizados de Braze a través del SDK
- Enviar eventos utilizando el punto de conexión REST ([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track))

Estos patrones requieren más esfuerzo de ingeniería, pero a veces son preferibles dependiendo de tu configuración actual de Braze. Ponte en contacto con el equipo de AI Decisioning Services para obtener más información.

{% endtab %}
{% tab SFMC %}

### Enviar datos de clientes a través de SFMC {#send-customer-data-through-sfmc}

Para integraciones con Salesforce Marketing Cloud:

1. Configura las extensiones de datos (Data Extensions) de SFMC para tus datos de clientes.
2. Configura el paquete instalado (Installed Package) de SFMC para la integración con la API con los permisos adecuados requeridos por Decisioning Studio.
3. Asegúrate de que las extensiones de datos se actualicen diariamente, ya que Decisioning Studio extraerá los últimos datos incrementales disponibles.

Proporciona el ID de la extensión y la clave de API a tu equipo de AI Decisioning Services. Ellos te ayudarán con los siguientes pasos para la ingesta de datos de clientes.

{% endtab %}
{% tab Klaviyo %}

### Enviar datos de clientes a través de Klaviyo {#send-customer-data-through-klaviyo}

Para integraciones con Klaviyo:

1. Confirma que los datos del perfil de cliente estén disponibles en los perfiles de Klaviyo.
2. Genera una clave de API privada con acceso completo a perfiles.
3. Proporciona la clave de API a tu equipo de AI Decisioning Services.

Consulta la [documentación de Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237908) para obtener más información sobre la configuración de claves de API.

{% endtab %}
{% tab Cloud Storage %}

### Otras soluciones en la nube (Google Cloud Storage, Azure, AWS) {#other-cloud-solutions-google-cloud-storage-azure-aws}

Si los datos de clientes no están almacenados actualmente en Braze, SFMC o Klaviyo, el siguiente mejor paso es configurar una exportación automatizada directamente a un contenedor de Google Cloud Storage controlado por Braze. También podemos admitir exportaciones a AWS o Azure (aunque GCS es preferible). Para estas plataformas, exporta a su almacenamiento en la nube interno y Braze podrá extraer esos datos.

Para determinar si esto es viable, consulta la documentación de tu plataforma MarTech. Por ejemplo:

- mParticle ofrece una [integración nativa con Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/)
- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

Si esto es viable, podemos proporcionarte un contenedor de GCS para exportar datos de clientes que esté aislado para Decisioning Studio.

{% endtab %}
{% endtabs %}

## Prácticas recomendadas {#best-practices}

- **Nombres de columna descriptivos:** Los datos de clientes deben tener nombres de columna claros y descriptivos. Idealmente, se debe proporcionar un diccionario de datos.
- **Actualizaciones incrementales:** Los archivos incrementales son preferibles frente a instantáneas de todo el historial de clientes cada día.
- **Identificadores consistentes:** Cada registro debe contener un identificador de cliente único que sea consistente en todos los activos de datos.
- **Incluir marcas de tiempo:** Los registros deben tener marcas de tiempo asociadas para una atribución precisa y el entrenamiento de los agentes.

## Integraciones personalizadas {#custom-integrations}

Otras opciones o canalizaciones de datos completamente personalizadas son posibles. Estas pueden requerir trabajo adicional de servicios o de ingeniería por parte de tu equipo. Para determinar qué es viable y óptimo, trabaja con tu equipo de AI Decisioning Services.

{% alert important %}
Esta guía explica los patrones de integración más comunes. El equipo de seguridad de la información aún deberá evaluar todos los puntos de conexión y los consultores de soluciones estarán disponibles para asesorar sobre la implementación.
{% endalert %}

## Próximos pasos {#next-steps}

Después de conectar tus orígenes de datos, procede a configurar la orquestación:

- [Configurar la orquestación]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/orchestration_setup)