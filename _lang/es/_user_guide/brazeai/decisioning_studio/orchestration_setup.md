---
nav_title: Configurar la orquestación
article_title: Configurar la orquestación
page_order: 4
page_type: reference
description: "Este artículo explica cómo configurar la orquestación para BrazeAI Decisioning Studio, incluyendo cómo elegir tu plataforma de interacción con los clientes, reunir las credenciales necesarias y configurar tu integración."
toc_headers: h2
---

# Configurar la orquestación {#set-up-orchestration}

> Los agentes de toma de decisiones necesitan conectarse a una plataforma de interacción con los clientes (CEP) para orquestar las comunicaciones una vez que han ingerido los datos de clientes y personalizado a nivel 1:1. Este artículo cubre lo que necesitas preparar y cómo configurar la integración para cada CEP compatible.

## ¿Qué es la orquestación? {#what-is-orchestration}

La orquestación es la conexión entre Decisioning Studio y tu plataforma de interacción con los clientes (CEP). Una vez que tu agente de toma de decisiones determina la acción óptima para cada cliente, la orquestación ejecuta esas decisiones desencadenando comunicaciones personalizadas a través de tu CEP.

Piénsalo de esta manera:

- **Decisioning Studio** decide *qué* enviar y *cuándo* enviarlo
- **Tu CEP** se encarga de *cómo* enviarlo

## Elige tu CEP {#choose-your-cep}

El primer paso es elegir qué CEP usar con Decisioning Studio. Tu elección afecta la complejidad de la configuración y las características disponibles.

### CEP compatibles {#supported-ceps}

| CEP | Tipo de integración | Complejidad de configuración |
|-----|---------------------|------------------------------|
| **Braze** | Integración nativa con API (recomendada) | Baja |
| **Salesforce Marketing Cloud** | Eventos de API + Journey Builder | Media |
| **Otras CEP** | Personalizada (archivo de recomendaciones) | Alta |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CEP compatibles" }

{% alert tip %}
Si ya estás usando Braze como tu CEP, te recomendamos usar la integración nativa de Braze para la experiencia de configuración más fluida.
{% endalert %}

## Requisitos previos {#prerequisites}

Antes de configurar la orquestación, reúne los siguientes elementos según la CEP que hayas elegido.

{% tabs %}
{% tab Braze %}

| Requisito | Descripción |
|-----------|-------------|
| **Clave de API REST** | Una nueva clave de API con permisos para datos de usuario, mensajes, Campaigns, Canvas, Segments y plantillas. |
| **URL del panel de Braze** | La URL de tu instancia de Braze (por ejemplo, `https://dashboard-01.braze.com`). |
| **ID de la aplicación** | La clave de API asociada con la aplicación que deseas rastrear (se encuentra en **Configuración** > **Configuración de la aplicación**). |
| **Nombre y dirección del remitente de correo electrónico** | La información del remitente que se usará para tus campañas (se encuentra en **Configuración** > **Preferencias de correo electrónico**). |
| **Plantillas base** | Las plantillas de mensaje que tu agente usará para la orquestación. Crearás Campaigns activadas por API para cada plantilla. |
| **ID de usuario de prueba** | Un ID de usuario para probar la integración antes del lanzamiento. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

{% endtab %}
{% tab Salesforce Marketing Cloud %}

| Requisito | Descripción |
|-----------|-------------|
| **Credenciales del paquete de aplicación** | Client ID, Client Secret, Authentication Base URI, REST Base URI y SOAP Base URI de un paquete instalado con integración de API servidor a servidor. |
| **Permisos de API** | Alcances para canales, activos, automatizaciones, journeys, contactos, extensiones de datos y eventos de seguimiento. |
| **Extensiones de datos** | Necesitarás extensiones de datos para datos de suscriptores, datos de interacción y recomendaciones. |
| **Plantillas de correo electrónico** | Las plantillas que deseas que Decisioning Studio use, con los ID de plantilla para cada una. |
| **Acceso a Journey Builder** | Acceso para crear y activar journeys de múltiples pasos con fuentes de entrada de eventos de API. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

{% endtab %}
{% tab Otras CEP %}

Si estás usando una CEP distinta a Braze o Salesforce Marketing Cloud, Decisioning Studio puede integrarse mediante un enfoque de archivo de recomendaciones:

| Elemento | Descripción |
|----------|-------------|
| **Capacidad de ingesta de datos** | Tu CEP debe poder ingerir archivos de recomendaciones (normalmente CSV o JSON) que contengan decisiones personalizadas para cada cliente. |
| **Soporte de contenido dinámico** | Tus campañas deben admitir la población de campos de forma dinámica basándose en los datos de recomendaciones. |
| **Recursos de ingeniería personalizados** | Tu equipo necesitará construir la integración para leer los archivos de recomendaciones y desencadenar las comunicaciones. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

{% endtab %}
{% endtabs %}

## Planifica tus campañas {#plan-your-campaigns}

Antes de configurar la orquestación, considera los siguientes detalles:

### Plantillas base {#base-templates}

Una plantilla base es cualquier plantilla de mensaje que tu agente de toma de decisiones podría usar. Considera:

- **¿Cuántas plantillas?** Tu agente puede trabajar con una plantilla o con varias. Si son varias, el agente puede personalizar qué plantilla recibe cada cliente.
- **¿Qué canales?** Correo electrónico, push, SMS o una combinación. Cada canal puede requerir plantillas y campañas separadas.
- **¿Qué elementos dinámicos?** Identifica qué partes de tu mensaje personalizará el agente (líneas del asunto, CTA, ofertas, horarios, etc.). Estos se convertirán en propiedades de activación de API o marcadores de posición dinámicos.

### Configuración de reelegibilidad {#re-eligibility-settings}

Tus campañas deben permitir que los usuarios reciban mensajes varias veces:

- Para pruebas, querrás enviar la misma campaña al mismo usuario repetidamente
- En producción, el agente puede determinar que la misma campaña es óptima para un usuario en días consecutivos

{% alert note %}
Aunque configures la reelegibilidad para pruebas, los agentes de Decisioning Studio están diseñados para respetar los límites de frecuencia y no enviarán la misma campaña a un usuario más de una vez al día en producción.
{% endalert %}

### Propiedades de activación de API {#api-trigger-properties}

Para integraciones con Braze, planifica qué dimensiones optimizará tu agente. Estas se convierten en propiedades de activación de API que pasan valores dinámicos a tus campañas:

| Dimensión de ejemplo | Propiedad de activación de API |
|----------------------|-------------------------------|
| Línea del asunto | {% raw %}`{{api_trigger_properties.${subject_line}}}`{% endraw %} |
| Llamada a la acción | {% raw %}`{{api_trigger_properties.${cta_message}}}`{% endraw %} |
| Oferta | {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %} |
| Monto de descuento | {% raw %}`{{api_trigger_properties.${discount}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Propiedades de activación de API" }

## Configuración de la integración {#integration-setup}

Selecciona tu CEP de esta lista para comenzar con la configuración de la integración.

{% tabs %}
{% tab Braze %}

## Configurar la integración con Braze {#set-up-braze-integration}

Sigue estos pasos para integrar un agente de Decisioning Studio con las capacidades de orquestación de Braze (el equipo de servicios de Braze estará disponible para ayudarte):

### Paso 1: Crear una clave de API {#step-1-create-an-api-key}

Ve a **Configuración** > **Claves de API** y crea una nueva clave con los siguientes permisos:

{% multi_lang_include decisioning_studio/api_key_permissions.md %}

### Paso 2: Configurar Campaigns activadas por API {#step-2-set-up-api-triggered-campaigns}

Configura una Campaign activada por API para cada plantilla base con propiedades de activación de API para todas las dimensiones optimizadas.

Una plantilla base es cualquier plantilla que el agente de toma de decisiones podría usar para orquestar mensajes. Un agente de toma de decisiones puede tener 1 plantilla base o varias, en cuyo caso elegir la plantilla base correcta para cada cliente será una de las decisiones que el agente personaliza.

### Paso 3: Configurar la reelegibilidad {#step-3-configure-re-eligibility}

Asegúrate de que todas las Campaigns activadas por API permitan que los usuarios vuelvan a ser elegibles en un plazo de 15 minutos.

![Diagrama de configuración de límite de frecuencia en Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_frequency_cap.png %})

{% alert note %}
Aunque el agente de Decisioning Studio nunca enviará la misma campaña más de una vez al día, querrás tener la capacidad de enviar las mismas campañas varias veces al día con fines de prueba.
{% endalert %}

### Paso 4: Agregar marcadores de posición dinámicos {#step-4-add-dynamic-placeholders}

Estos sirven como marcadores de posición dinámicos para las decisiones que el agente de Decisioning Studio está optimizando.

#### Ejemplo 1: Campaign de correo electrónico {#example-1-email-campaign}

Supongamos que el agente de Decisioning Studio está optimizando una Campaign de correo electrónico. Esto podría configurarse así:

![Ejemplo de configuración de Campaign de correo electrónico en Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_1.png %})

Suponiendo que el agente está optimizando la elección de plantillas y el mensaje de llamada a la acción (CTA), se debería crear una Campaign activada por API para cada plantilla, y la sección de CTA de una plantilla podría verse así:

![Ejemplo de sección CTA en una plantilla de correo electrónico de Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_braze_email_example_2.png %})

#### Ejemplo 2: Campaign de push {#example-2-push-campaign}

Supongamos que un agente de Decisioning Studio está optimizando el mensaje de una Campaign de push. Esto podría configurarse así:

![Ejemplo de configuración de Campaign de push en Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_1.png %})

![Ejemplo de contenido dinámico en Campaign de push de Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_2.png %})

Resultando en el siguiente mensaje:

![Resultado del mensaje push optimizado por Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_3.png %})

#### Ejemplo 3: Campaign de SMS {#example-3-sms-campaign}

Supongamos que el agente de Decisioning Studio está optimizando campos en una Campaign de SMS. Esto podría configurarse así:

![Ejemplo de configuración de Campaign de SMS en Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_1.png %})

![Ejemplo de contenido dinámico en Campaign de SMS de Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_2.png %})

Resultando en el siguiente mensaje:

![Resultado del mensaje SMS optimizado por Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_3.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Configurar la integración con SFMC {#set-up-sfmc-integration}

Decisioning Studio admite integración nativa con Salesforce Marketing Cloud. Decisioning Studio desencadena eventos de API en un journey con los datos necesarios para poblar los elementos dinámicos.

{% endtab %}
{% tab Otras CEP %}

## Configurar integraciones con otras CEP {#set-up-other-cep-integrations}

Decisioning Studio puede integrarse con cualquier plataforma de interacción con los clientes. Sin embargo, esto puede requerir algo de trabajo de ingeniería personalizado por parte de tu equipo, ya que Decisioning Studio no puede desencadenar comunicaciones directamente.

En este escenario, el agente entregará un "archivo de recomendaciones". Este archivo contiene filas para cada cliente, con columnas que indican todas las decisiones personalizadas para ese cliente.

Por ejemplo, el siguiente archivo de recomendaciones:

![Ejemplo de archivo de recomendaciones con decisiones personalizadas por cliente]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_2.png %})

Podría usarse para optimizar una Campaign de correo electrónico que se vea así:

![Ejemplo de Campaign de correo electrónico optimizada con archivo de recomendaciones]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_1.png %})

{% endtab %}
{% endtabs %}

## Mejores prácticas {#best-practices}

Ten en cuenta estas mejores prácticas mientras te preparas para la orquestación:

1. **Comienza con un alcance reducido:** usa un canal y una o dos plantillas al principio. Puedes expandir después a medida que aprendas qué funciona.
2. **Prueba a fondo:** antes de lanzar, prueba tu integración con un conjunto pequeño de usuarios para verificar que el contenido dinámico se rellena correctamente.
3. **Documenta tu configuración:** lleva un registro de los ID de Campaign, ID de plantilla, claves de API y otros identificadores. Necesitarás consultarlos en el portal de Decisioning Studio.
4. **Coordina con tu equipo:** la configuración de la orquestación puede involucrar a los equipos de marketing, ingeniería y datos. Asegúrate de que todos entiendan su rol en el proceso.
5. **Planifica para los datos de retroalimentación:** la orquestación incluye enviar mensajes y recopilar los datos de interacción y conversión que ayudan a tu agente a aprender. Consulta [Prepara tus datos]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data) para más detalles.

## Próximos pasos {#next-steps}

Después de configurar la orquestación, procede a diseñar tu agente:

- [Diseñar agentes de toma de decisiones]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/design_agents)