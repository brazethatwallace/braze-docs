---
nav_title: JustAI
article_title: JustAI
description: "Este artículo de referencia describe la asociación entre Braze y JustAI, una plataforma empresarial SaaS basada en IA que crea versiones personalizadas de las campañas existentes y optimiza las líneas del asunto, el contenido creativo y los diseños de correo electrónico HTML a lo largo del tiempo."
alias: ["/partners/just_ai/", "/partners/just_words/"]
page_type: partner
---

# Guía de integración de JustAI {#justai-integration-guide}

> [JustAI](https://www.getjust.ai/) hiperpersonaliza la mensajería a escala en canales de marketing del ciclo de vida, permitiéndote probar dinámicamente cientos de variaciones y actualizar automáticamente el contenido de bajo rendimiento.

Cuando usas JustAI con [Contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) de Braze para personalizar tus Campaigns y Canvas existentes en Braze, JustAI utilizará Braze Currents para optimizar el contenido de forma dinámica, así no tienes que hacerlo tú.

## ¿Cuáles son los beneficios? {#what-are-the-benefits}

Una vez completada tu integración, puedes aprovechar la plataforma JustAI para:

- Ver resultados de experimentos en tiempo real
- Editar textos de forma dinámica
- Consultar información sobre el rendimiento

{% alert note %}
¿Tienes preguntas? Ponte en contacto con JustAI a través de su [página de reservas](https://www.getjust.ai/book-demo) o del canal compartido de Slack.
{% endalert %}

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta de JustAI | Se requiere una cuenta de [JustAI](https://www.getjust.ai/) para aprovechar esta asociación. Si no tienes una cuenta de JustAI, [programa una llamada de incorporación de 30 minutos](https://www.getjust.ai/book-demo). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración de JustAI con Braze {#integrating-justai-with-braze}

### Paso 1: Crear una plantilla de JustAI {#step-1-create-a-justai-template}

1. Ve a tu consola de JustAI y [crea una nueva plantilla](https://console.getjust.ai/new).
2. Elige un ID fácil de recordar que use solo letras, números y guiones bajos.
3. Completa los detalles básicos de la campaña.
4. Usa la IA para generar variaciones personalizadas.

![La plataforma de creación de plantillas de JustAI.]({% image_buster /assets/img/just_words/creation_interface.png %}){: style="max-width:80%;"}

### Paso 2: Crear una clave de API de JustAI {#step-2-create-a-justai-api-key}

1. Ve a **Org Settings** > **API Keys** > **Generate API Key**.
2. Copia y guarda la clave de API en un lugar seguro.

![El formulario de clave de API de JustAI.]({% image_buster /assets/img/just_words/api_key_form.png %}){: style="max-width:80%;"}

### Paso 3: Usar JustAI en tu contenido de Braze {#step-3-use-justai-in-your-braze-content}

JustAI funciona con Canvas y Campaigns mediante Contenido conectado. Si estás creando un Canvas, cada paso de correo electrónico debe corresponder a una plantilla única de JustAI.

#### Paso 3.1: Configurar tu prueba A/B {#step-31-set-up-your-ab-test}

{% tabs %}
{% tab Canvas %}

1. En un Canvas, selecciona **Añadir variante** > **Añadir variante** hasta tener el número deseado de variantes, y añade pasos a cada variante (como un paso de mensaje de correo electrónico).
2. Divide el tráfico de la audiencia como desees. Por ejemplo, si tienes dos variantes, podrías asignar un 50 % a cada una. O podrías tener dos variantes con un 40 % cada una y un grupo de control con un 20 %. Para más información sobre pruebas A/B en Canvas, consulta [Crear un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
3. En los editores de los pasos de mensaje que quieras usar con Contenido conectado, pega el fragmento de código de Contenido conectado de la consola de JustAI, como el siguiente ejemplo.

{% raw %}
```liquid
{% connected_content https://worker.getjust.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

![Configuración de prueba A/B en Canvas de Braze.]({% image_buster /assets/img/just_words/braze_canvas.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Campaign %}

1. En el paso **Redactar mensajes** de tu Campaign, crea dos variantes.
2. En el paso **Target Audience**, ve a la sección **A/B Testing** y modifica los porcentajes de usuarios que recibirán cada una de tus variantes (y tu grupo de control opcional). Puedes personalizar aún más tu prueba seleccionando una opción de optimización. Para más información sobre pruebas A/B en Campaigns, consulta [Crear pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/).
3. En el creador de mensajes, pega el fragmento de código de Contenido conectado de la consola de JustAI. El siguiente fragmento de código Liquid muestra un ejemplo de esto.

{% raw %}
```liquid
{% connected_content https://worker.getjust.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

{% endtab %}
{% endtabs %}

#### Paso 3.2: Añadir personalización con atributos personalizados (opcional) {#step-32-add-personalization-with-custom-attributes-optional}

Para personalizar tus mensajes con atributos personalizados (como `industry`), usa el siguiente formato Liquid:

{% raw %}
```liquid
{% connected_content https://worker.getjust.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}&attrs.industry={{ custom_attribute.industry }}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

Ten en cuenta que el atributo personalizado de `industry` se indica mediante {% raw %}`&attrs.industry={{ custom_attribute.industry }}`{% endraw %}.

![Lógica Liquid de Braze en un creador de mensajes HTML.]({% image_buster /assets/img/just_words/just_words_personalization.png %}){: style="max-width:80%;"}

### Paso 4: Previsualizar el correo electrónico {#step-4-preview-the-email}

Asegúrate de previsualizar el correo electrónico en Braze para confirmar que el contenido personalizado se muestra correctamente.

![Vista previa de mensaje de Braze para un correo electrónico de JustAI.]({% image_buster /assets/img/just_words/just_words_preview.png %}){: style="max-width:80%;"}

### Paso 5: Configurar Braze Currents {#step-5-set-up-braze-currents}

Braze Currents permite el seguimiento del rendimiento y la optimización a lo largo del tiempo.

1. En Braze, ve a **Integraciones de socios** > **Exportación de datos**.
2. Selecciona **Create New Test Current** y luego selecciona **Test Amazon S3 Data Export**.

![Menú desplegable "Create New Test Current" con la opción "Test Amazon S3 Data Export".]({% image_buster /assets/img/just_words/test_amazon_s3.png %}){: style="max-width:80%;"}

{: start="3" }
3. Introduce el ID de acceso S3, la clave de acceso secreta de AWS, el nombre de contenedor y la carpeta proporcionados por JustAI durante la incorporación.

![Sección de credenciales para la clave de acceso secreta de AWS.]({% image_buster /assets/img/just_words/aws_secret_access_key.png %}){: style="max-width:80%;"}

{: start="4" }
4. Selecciona los eventos a rastrear, como envíos, aperturas, clics, cancelaciones de suscripción, conversiones y otros.

![Sección de eventos de interacción de mensajes con eventos para seleccionar.]({% image_buster /assets/img/just_words/message_engagement_events.png %}){: style="max-width:80%;"}

{: start="5" }
5. Lanza el Braze Current.

¡Todo listo! Ahora puedes usar JustAI con Contenido conectado de Braze.