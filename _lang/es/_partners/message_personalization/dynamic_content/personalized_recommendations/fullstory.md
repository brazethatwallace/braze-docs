---
nav_title: Fullstory
article_title: Fullstory
description: "Este artículo de referencia describe la asociación entre Braze y Fullstory."
alias: /partners/fullstory/
page_type: partner
search_tag: Partner
---

# Fullstory

> La plataforma de datos de comportamiento de [Fullstory](https://www.fullstory.com/) ayuda a los líderes tecnológicos a tomar decisiones mejores y más informadas. Al inyectar datos de comportamiento digital en su pila de análisis, la tecnología patentada de Fullstory libera el poder de los datos de comportamiento de calidad a escala, transformando cada visita digital en análisis accionables.

*Esta integración está mantenida por Fullstory*

## Acerca de esta integración {#about-this-integration}

Puedes aprovechar la información de Fullstory en Braze para crear imágenes momento a momento de la experiencia de un usuario en el sitio web o la aplicación y entregar mensajería hipercontextual. La API de resumen de sesión de Fullstory permite capturar metadatos detallados sobre el comportamiento de navegación de un usuario para utilizarlos en la mensajería de Braze, lo cual es especialmente potente cuando se aprovecha en un recorrido de mensajería de varios pasos como un Canvas.

El valor en tiempo real de los datos de resumen de sesión de Fullstory se aprovecha mejor a través del contenido conectado. Al utilizar contenido conectado en un paso de contexto de Canvas, puedes almacenar los datos de Fullstory a lo largo del recorrido de un usuario en Canvas para utilizarlos en cualquier paso posterior de Canvas. Esto también evita la necesidad de escribir estos datos en un perfil de usuario de Braze a través de eventos personalizados o atributos.

En el siguiente ejemplo, se aprovechan los datos de contexto de Canvas en un paso de Canvas de agente de IA para generar el mensaje óptimo que anime a un usuario a retomar un carrito abandonado. Sin embargo, puedes aprovechar los datos para personalizar el mensaje directamente, para determinar el recorrido del usuario con rutas de audiencia, o para determinar el texto o los activos utilizados en los pasos posteriores de mensajería.

## Requisitos previos {#prerequisites}

Antes de empezar, necesitas lo siguiente:

| Requisito | Descripción |
|-----------------------|-----------------|
| Un token de autorización de la API de sesión de Fullstory | Consulta el paso 1 de esta guía. |
| Un token de autorización de contenido conectado de Braze habilitado | Consulta la nota de acceso anticipado en esta sección. |
| Un paso de contexto de Canvas en Braze | Consulta la nota de acceso anticipado en esta sección. |
| Paso de agente de BrazeAI habilitado | Consulta la nota de acceso anticipado en esta sección. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

{% alert important %}
Los agentes de Braze, el contexto de Canvas y los tokens de autorización de contenido conectado están en acceso anticipado. Si te interesa aprovechar esta solución, habla con tu CSM de Braze para habilitar estas herramientas.
{% endalert %}

## Integrar Fullstory {#integrate-fullstory}

### Paso 1: Configurar Fullstory para la habilitación de la API de resumen de sesión {#step-1}

#### Paso 1.1: Recuperar el token de autenticación para el endpoint de la API de resumen de sesión {#step-11-retrieve-the-authentication-token-for-the-session-summary-api-endpoint}

Para crear una [clave de API de Fullstory](https://developer.fullstory.com/server/authentication/):

1. En Fullstory, ve a **Settings** > **API Keys**.
2. Selecciona el nivel de permiso **Standard**.
3. Copia el valor de la clave inmediatamente, ya que solo aparece una vez.

#### Paso 1.2: Crear un ID de perfil de resumen de sesión {#step-12-create-a-session-summary-profile-id}

Siguiendo [las indicaciones de Fullstory](https://developer.fullstory.com/anywhere/activation/ai-session-summary-api/#step-1-creating-and-managing-summary-profiles), crea un perfil de resumen de sesión utilizando el endpoint dedicado. Aquí es donde defines qué tipo de datos quieres que la respuesta de resumen de sesión proporcione a Braze.

En la respuesta a esta solicitud, Fullstory proporciona un ID de perfil de sesión. Este ID de perfil es un componente clave del cuerpo de la solicitud de contenido conectado que se utiliza en el siguiente caso de uso.

### Paso 2: Crear la autenticación del token de contenido conectado {#step-2-create-the-connected-content-token-authentication}

1. En Braze, ve a **Configuración** > **Configuración del espacio de trabajo** > **Contenido conectado** > **Añadir credencial** > **Autenticación por token**.
2. Nombra la autenticación `fullstory`.
3. Añade la clave de encabezado "Authorization". Proporciona el valor de encabezado que Fullstory facilitó en el paso anterior.
4. En **Dominio permitido**, introduce **api.fullstory.com**.

![Captura de pantalla de Braze mostrando los campos de edición de credenciales]({% image_buster /assets/img/fullstory/1.png %}){: style="max-width:50%;"}

## Ejemplos {#use-cases}

### Crear recorridos de mensajes dinámicos {#create-dynamic-message-journeys}

Utilizando los [flujos de activación](https://help.fullstory.com/hc/en-us/articles/360045134554-Streams) de Fullstory, puedes desencadenar Canvas de Braze inmediatamente después de las interacciones clave de los usuarios. El poder de esta integración reside en el `client_session_id` único (accesible a través de {% raw %}`{{canvas_entry_properties.${client_session_id}}}`{% endraw %}), que el sistema pasa automáticamente de Fullstory a Braze. Este ID actúa como clave, permitiendo a Braze obtener el resumen de sesión completo de lo que experimentó exactamente el usuario.

Aprovechando los pasos de contexto de Canvas y el contenido conectado, puedes utilizar este ID para realizar una solicitud de API a Fullstory, recuperar los datos de la sesión y almacenarlos como una variable para utilizarlos más adelante en el recorrido.

![Paso de contexto de Canvas en Braze mostrando la variable de contexto "summary_result" creada y rellenada con una llamada de contenido conectado a Fullstory para recuperar un resumen de sesión]({% image_buster /assets/img/fullstory/2.png %})

Con el token de autorización creado anteriormente, utiliza la siguiente estructura de solicitud para obtener los datos del resumen de sesión.

{% raw %}
```bash
{% connected_content https://api.fullstory.com/v2/sessions/{{canvas_entry_properties.${client_session_id} | url_encode}}/summary?config_profile=[YOUR-FULLSTORY-PROFILE-ID] :auth_credentials fullstory :save summary_result %}
{{summary_result | as_json_string }}
```
{% endraw %}

{% alert note %}
La respuesta se almacena como la etiqueta de Liquid {% raw %}`{{context.${summary_result}.response}}`{% endraw %}. Utiliza esta etiqueta de contexto en los pasos posteriores de Canvas.
{% endalert %}

En esta fase, el Canvas puede acceder a la respuesta de la llamada de contenido conectado, que contiene toda la carga útil del mensaje para la sesión de un usuario.

{% details Ejemplo de carga útil de la API de resumen de sesión %}

{% raw %}
```bash
{
    "response": {
        "primary_goal": "User attempted to update payment method.",
        "issues_encountered": [
            "Received 'invalid card number' error twice.",
            "Clicked 'Submit' button multiple times with apparent frustration (based on event patterns)."
        ],
        "final_action": "Navigated away from payment page to dashboard.",
        "reason_for_termination_suggestion": "Could not update payment method successfully.",
        "help_pages_visited": [
            "/help/payment-errors"
        ]
    },
    "response_schema": {
        "type": "OBJECT",
        "properties": {
            "primary_goal": {
                "type": "STRING",
                "description": "A summary of the user's main objective during the session."
            },
            "issues_encountered": {
                "type": "ARRAY",
                "description": "A list of problems or errors the user faced.",
                "items": {
                    "type": "STRING",
                    "description": "A description of a single issue."
                }
            },
            "final_action": {
                "type": "STRING",
                "description": "The last significant action the user took before the session ended."
            },
            "reason_for_termination_suggestion": {
                "type": "STRING",
                "description": "A suggested reason for why the user ended their session."
            },
            "help_pages_visited": {
                "type": "ARRAY",
                "description": "A list of URLs for help or documentation pages the user visited.",
                "items": {
                    "type": "STRING",
                    "description": "The URL of a help page."
                }
            }
        },
        "required": [
            "primary_goal",
            "issues_encountered",
            "final_action",
            "reason_for_termination_suggestion",
            "help_pages_visited"
        ]
    }
}
```
{% endraw %}
{% enddetails %}

Puedes aprovechar cualquiera de los datos disponibles en el objeto anterior utilizando la etiqueta de contexto Liquid más adelante en el recorrido del usuario por el Canvas. Los pasos siguientes muestran cómo puedes utilizar estos datos en un paso de [agente]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step).

{% alert note %}
Para evitar comportamientos inesperados, incluye un paso de ruta de audiencia después del paso de contexto, que puede sacar a los usuarios del contexto si su etiqueta de contexto está vacía, lo que indica que la llamada de contenido conectado falló o no devolvió información.

![El paso de ruta de audiencia en Braze]({% image_buster /assets/img/fullstory/3.png %})

{% endalert %}

### Producir el texto adecuado {#produce-appropriate-copy}

Al crear un [paso de agente]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) en un Canvas desencadenado por Fullstory, e incluir el paso de contexto descrito en esta sección, puedes hacer referencia a los datos de resumen de sesión de Fullstory en el agente.

En este ejemplo, utilizas estos datos para permitir que el agente de Braze genere un texto de mensaje adecuado para su uso en una tarjeta de contenido, que puede animar al usuario a volver a su cesta abandonada.

![Captura de pantalla del creador de contexto del agente de Braze con la instrucción]({% image_buster /assets/img/fullstory/4.png %})

Utiliza el mismo nombre para la etiqueta de contexto Liquid creada en este paso que la etiqueta de contexto Liquid utilizada en el paso de agente de IA creado anteriormente.

La instrucción necesaria para tu caso de uso varía. Para conocer las mejores prácticas sobre cómo crear instrucciones eficaces para los agentes, consulta [Escribir instrucciones]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions).

En tu Canvas, selecciona un paso de agente de IA y, a continuación, selecciona el agente **Session Context** en el menú desplegable. Guarda el resultado como una variable, en este caso "message", que puedes colocar en el texto del mensaje utilizando la etiqueta de Liquid {% raw %}`{{context.${message}.message}}`{% endraw %}.

![Captura de pantalla del paso de Canvas del agente de Braze con la instrucción]({% image_buster /assets/img/fullstory/5.png %})

Crea un paso de mensaje que aproveche el texto creado por el agente de IA. Utiliza la etiqueta de Liquid en este paso.

{% alert important %}
La API de resumen de sesión de Fullstory puede devolver datos de usuario identificables sensibles. Para garantizar el cumplimiento al manejar PII (información de identificación personal), asegúrate de que tus reglas de captura de datos de Fullstory excluyan la PII antes de aprovechar este caso de uso.
{% endalert %}