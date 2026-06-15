---
nav_title: Directrices de marca
article_title: Directrices de marca generadas por IA
page_order: 2.2
description: "Este artículo de referencia cubre las directrices de marca para el asistente de redacción con inteligencia artificial, una característica que te permite adaptar el estilo del texto generado por el asistente de redacción con inteligencia artificial a la voz y el estilo de tu marca."
---

# Genera directrices de marca con BrazeAI {#generate-brand-guidelines-with-brazeai}

> Adapta el estilo de tus textos generados por IA para que coincidan con la voz y la personalidad de tu marca con directrices de marca personalizadas.

## Creación de directrices de marca {#steps}

Sigue estos pasos para crear directrices de marca en el asistente de redacción con inteligencia artificial. También puedes crear directrices de marca en la página de configuración de [Directrices de marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/).

### Paso 1: Crear una directriz de marca {#step-1-create-a-brand-guideline}

1. En el creador de mensajes, busca y selecciona <i class="fa-solid fa-wand-magic-sparkles" title="Redactor de inteligencia artificial"></i> **AI Copywriter** para [abrir el asistente de redacción con inteligencia artificial]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/#access).
2. Selecciona **Apply brand guideline** y luego **Create a brand guideline**.

![Menú desplegable de «Apply brand guidelines» expandido con el botón «Create a brand guideline» en primer plano.]({% image_buster /assets/img/ai_copywriter/create_brand_guideline_button.png %}){:style="max-width:75%"}

{: start="3"}

3. Introduce un nombre para esta directriz. Será la etiqueta que ves en la selección anterior.
4. Para **When will you use these brand guidelines?**, añade detalles para ayudar a tus colegas (y a ti en el futuro) a comprender el contexto de utilización de esta directriz.
5. Si quieres que esta sea la directriz de marca predeterminada para el espacio de trabajo actual, marca **Use as default brand guideline**.

![Vista de la creación de la directriz de marca.]({% image_buster /assets/img/ai_copywriter/manual_brand_guidelines.png %} "Brand Guidelines")

### Paso 2: Describe la personalidad de tu marca {#step-2-describe-your-brand-personality}

Para **Brand personality**, piensa en lo que hace única a tu marca. Incluye rasgos, valores, voz y cualquier arquetipo que defina tu marca. Aquí tienes algunas características a tener en cuenta:

| **Característica**       | **Definición**                                                                       | **Ejemplo**                                                        |
|--------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Reputación               | Cómo quieres que se perciba tu marca en el mercado.                               | Somos conocidos por ser la marca más fiable y orientada al cliente de nuestro sector. |
| Rasgos de personalidad       | Características similares a las humanas que describen el carácter de tu marca.                     | Nuestra marca es amable, accesible y siempre optimista.          |
| Valores                   | Valores fundamentales que guían las acciones y decisiones de tu marca.                           | Valoramos la sostenibilidad, la transparencia y la comunidad.            |
| Diferenciación          | Cualidades únicas que diferencian tu marca de la competencia.                         | Nos distinguimos por ofrecer un servicio al cliente personalizado que va más allá. |
| Voz de marca              | El tono y el estilo de comunicación que utiliza tu marca.                                 | Nuestra voz es informal pero informativa, garantizando la claridad sin ser demasiado formal. |
| Arquetipo de marca          | El arquetipo que representa la personalidad de tu marca (el héroe, el creador, etc.).    | Encarnamos el arquetipo del «explorador», siempre en busca de nuevos retos y aventuras. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 2: Describe la personalidad de tu marca" }

### Paso 3: Definir el lenguaje que debe evitarse (opcional) {#step-3-define-language-that-should-be-avoided-optional}

En **Exclusions**, enumera cualquier lenguaje o estilo que no se ajuste a tu marca. Por ejemplo, quizá quieras evitar el «sarcasmo», las «actitudes negativas» o los tonos «condescendientes».

### Paso 4: Prueba tus directrices {#step-4-test-your-guidelines}

Pon a prueba tus directrices para ver cómo funcionan. Expande **Test your guidelines** para generar un texto de ejemplo y ajústalo según sea necesario.

![Prueba de directrices de marca con una promoción sobre rebajas de primavera para líneas del asunto de correos electrónicos.]({% image_buster /assets/img/ai_copywriter/test_brand_guidelines.png %})

### Paso 5: Guarda tus directrices {#step-5-save-your-guidelines}

Cuando estés satisfecho con tus directrices, selecciona **Save brand guideline**. Tus nuevas directrices se guardarán en tu espacio de trabajo para utilizarlas en el futuro.

{% alert important %}
Puedes cambiar el idioma de salida independientemente del idioma en que esté tu texto, pero ni Braze ni OpenAI garantizan la calidad de la traducción. Prueba y verifica siempre las traducciones antes de utilizarlas.
{% endalert %}

## Edición de las directrices existentes {#editing-existing-guidelines}

Para editar tus directrices de marca existentes:

1. Abre el asistente de redacción con inteligencia artificial.
2. Aplica las directrices de marca que quieras cambiar. Aparecerá un botón cerca del campo.
3. Selecciona **Edit guideline**.

{% multi_lang_include brazeai/generative_ai/policy.md %}