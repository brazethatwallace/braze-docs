---
nav_title: Google Gemini
article_title: Google Gemini
description: "Este artículo de referencia describe la asociación entre Braze y Google Gemini, que te permite conectar modelos Gemini a Braze para utilizarlos con agentes de IA personalizados."
alias: /partners/gemini/
page_type: partner
search_tag: Partner

---

# Google Gemini

> [Google Gemini](https://deepmind.google/technologies/gemini/) es la familia de modelos de IA de Google que combina el razonamiento avanzado en texto, código e imágenes para ayudar a las marcas a ofrecer experiencias más inteligentes y personalizadas.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

_Esta integración está mantenida por Google._

## Sobre la integración {#about-the-integration}

La integración de Braze y Google Gemini te permite conectar Gemini a Braze mediante una clave de API o iniciando sesión con tu cuenta de Google, para que puedas utilizar los modelos de Gemini al crear agentes de IA personalizados. Con esta integración, tus agentes pueden generar textos personalizados, tomar decisiones en tiempo real o actualizar los campos del catálogo utilizando los modelos Gemini de Google.

## Requisitos previos {#prerequisites}

| Requisitos | Descripción |
|---|---|
| Cuenta de Google Cloud | Una cuenta de Google Cloud con acceso a la API de Gemini. Puedes autenticarte con una clave de API o conectando tu cuenta de Google y seleccionando un proyecto de GCP en el panel de Braze. Para obtener ayuda, ponte en contacto con tu administrador o con [el soporte de Google Cloud](https://cloud.google.com/support). |
| Instancia de Braze | Puedes encontrar tu instancia de Braze en la [página de resumen de la API]({{site.baseurl}}/api/basics#endpoints) o a través de tu administrador de incorporación de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Para conectar Google Gemini a Braze:

1. Ve a **Integraciones de socios** > **Socios tecnológicos** en el panel de Braze y busca Google Gemini.
2. En **Método de autenticación**, elige **Clave de API** o **Conectar cuenta de Google**.
3. Completa la configuración del método elegido:
   - **Clave de API:** En **Tipo de API**, selecciona **Gemini API** o **Gemini Enterprise Agent Platform (anteriormente Vertex AI)**. Introduce tu clave de API. Si seleccionaste Gemini Enterprise Agent Platform, introduce también tu **ID de proyecto**. Selecciona **Guardar**.
   - **Conectar cuenta de Google:** Selecciona **Conectar cuenta de Google**, luego selecciona **Conectar Google** e inicia sesión con tu cuenta de Google. Selecciona tu **Proyecto de GCP** en el menú desplegable. Si tanto Gemini API como Gemini Enterprise Agent Platform están habilitados en ese proyecto, elige el **Tipo de API** que Braze debe utilizar. Selecciona **Guardar**.

{% alert note %}
**Conectar cuenta de Google** solo aparece en los espacios de trabajo donde esta opción de autenticación está habilitada.
{% endalert %}

Después de guardar, puedes seleccionar los modelos Gemini al [crear un agente personalizado]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) en la consola de agentes.

Ponte en contacto con [el soporte de Google Cloud](https://cloud.google.com/support) si tienes algún problema o pregunta sobre tu integración.