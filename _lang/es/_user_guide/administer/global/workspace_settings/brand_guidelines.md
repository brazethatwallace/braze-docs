---
nav_title: Directrices de marca
article_title: Directrices de marca
page_order: 1
page_type: reference
description: "Este artículo de referencia describe cómo crear, administrar y utilizar directrices de marca que Operator aplica al generar textos, plantillas e imágenes."
---

# Directrices de marca {#brand-guidelines}

> Adapta el estilo de tus textos generados por IA para que coincidan con la voz, el tono y la personalidad de tu marca con directrices de marca personalizadas.

Crea y administra directrices de marca desde **Contenido** > **Directrices de marca**.

## Creación de directrices de marca {#creating-brand-guidelines}

### Paso 1: Crear una directriz de marca {#step-1-create-a-brand-guideline}

En la página **Directrices de marca**, selecciona **Crear nuevo**. Si quieres que esta directriz de marca sea la predeterminada para el espacio de trabajo, marca **Use as default brand guideline**. Puedes tener una predeterminada por espacio de trabajo.

### Paso 2: Describe la personalidad de tu marca {#step-2-describe-your-brand-personality}

Para **Brand personality**, piensa en lo que hace única a tu marca. Incluye rasgos, valores, voz y cualquier arquetipo que defina tu marca. Aquí tienes algunas características a tener en cuenta:

| **Característica**       | **Definición**                                                                       | **Ejemplo**                                                        |
|--------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Reputación               | Cómo quieres que tu marca sea percibida en el mercado.                               | Somos conocidos por ser la marca más confiable y centrada en el cliente de nuestra industria. |
| Rasgos de personalidad   | Características humanas que describen el carácter de tu marca.                       | Nuestra marca es amigable, accesible y siempre optimista.        |
| Valores                  | Valores fundamentales que guían las acciones y decisiones de tu marca.               | Valoramos la sostenibilidad, la transparencia y la comunidad.    |
| Diferenciación           | Cualidades únicas que distinguen a tu marca de la competencia.                       | Nos destacamos al ofrecer un servicio al cliente personalizado que va más allá de lo esperado. |
| Voz de marca             | El tono y estilo de comunicación que utiliza tu marca.                               | Nuestra voz es informal pero informativa, garantizando claridad sin ser demasiado formal. |
| Arquetipo de marca       | El arquetipo que representa la personalidad de tu marca (el héroe, el creador, etc.).| Encarnamos el arquetipo del «Explorador», siempre buscando nuevos desafíos y aventuras. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 2: Describe la personalidad de tu marca" }

### Paso 3: Define el lenguaje que debe evitarse (opcional) {#step-3-define-language-that-should-be-avoided-optional}

Para **Exclusions**, enumera cualquier lenguaje o estilo que no se alinee con tu marca. Por ejemplo, podrías querer evitar el «sarcasmo», las «actitudes negativas» o los tonos «condescendientes».

![La ventana «Create brand guideline» con campos para introducir el nombre, la descripción, la personalidad, las exclusiones y el tono.]({% image_buster /assets/img/guidelines_create.png %})

### Paso 4: Prueba tus directrices {#step-4-test-your-guidelines}

Prueba tus directrices para ver cómo funcionan. Expande **Test your guidelines** para generar textos de ejemplo y ajústalos según sea necesario.

### Paso 5: Guarda tus directrices {#step-5-save-your-guidelines}

Cuando estés conforme con tus directrices, selecciona **Save brand guideline**. Tus directrices se guardarán en tu espacio de trabajo para uso futuro.

{% alert important %}
Puedes cambiar el idioma de salida independientemente del idioma en el que esté tu texto, pero ni Braze ni OpenAI garantizan la calidad de la traducción. Siempre prueba y verifica las traducciones antes de usarlas.
{% endalert %}

## Administrar directrices de marca {#managing-brand-guidelines}

Puedes editar las directrices de marca seleccionándolas en la página **Directrices de marca**. Archiva una directriz de marca para desactivarla y que no esté disponible en los creadores de mensajes. Para activarla y que sea seleccionable de nuevo, puedes filtrar por directrices de marca archivadas y luego desarchivarla.

![La página «Directrices de marca» filtrada por directrices de marca archivadas.]({% image_buster /assets/img/unarchive_brand_guideline.png %})

## Usar directrices de marca {#using-brand-guidelines}

Al redactar un mensaje, abre Operator para [generar texto]({{site.baseurl}}/user_guide/brazeai/operator/capabilities/#generate-copy) y selecciona tu directriz de marca en el menú desplegable **Apply brand guideline**. Si designas una directriz de marca específica como predeterminada, Braze la selecciona automáticamente en el menú desplegable, pero puedes elegir una directriz diferente.

![Operator con «Important Alerts!!» seleccionado como directriz de marca.]({% image_buster /assets/img/guidelines_ai_assistant.png %})

{% multi_lang_include brazeai/generative_ai/policy.md %}