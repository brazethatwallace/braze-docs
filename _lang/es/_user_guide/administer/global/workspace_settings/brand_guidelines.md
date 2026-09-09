---
nav_title: Directrices de marca
article_title: Directrices de marca
page_order: 1
page_type: reference
description: "Este artículo de referencia describe cómo crear, administrar y añadir directrices de marca como contexto para Operator y los agentes."
---

# Directrices de marca {#brand-guidelines}

> Adapta el estilo de tus textos generados por IA para que coincidan con la voz, el tono y la personalidad de tu marca con directrices de marca personalizadas.

Crea y administra directrices de marca desde **Contenido** > **Directrices de marca**.

## Crear directrices de marca {#creating-brand-guidelines}

### Paso 1: Crea una directriz de marca {#step-1-create-a-brand-guideline}

En la página **Brand Guidelines**, selecciona **Create new**. Si deseas que esta directriz de marca sea la predeterminada para el espacio de trabajo, selecciona **Use as default brand guideline**. Puedes tener una predeterminada por espacio de trabajo.

### Paso 2: Describe la personalidad de tu marca {#step-2-describe-your-brand-personality}

En **Brand personality**, piensa en lo que hace única a tu marca. Incluye rasgos, valores, voz y cualquier arquetipo que defina tu marca. Mantén este campo en 10.000 caracteres o menos. Si generas este texto con un LLM, incluye ese límite de caracteres en tu prompt para que el resultado se ajuste al campo.

Aquí tienes algunas características a considerar:

| Característica | Definición | Ejemplo |
|--------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Reputación | Cómo quieres que tu marca sea percibida en el mercado. | Somos conocidos por ser la marca más confiable y centrada en el cliente de nuestra industria. |
| Rasgos de personalidad | Características humanas que describen el carácter de tu marca. | Nuestra marca es amigable, accesible y siempre optimista. |
| Valores | Valores fundamentales que guían las acciones y decisiones de tu marca. | Valoramos la sostenibilidad, la transparencia y la comunidad. |
| Diferenciación | Cualidades únicas que distinguen a tu marca de la competencia. | Nos destacamos al ofrecer un servicio al cliente personalizado que va más allá. |
| Voz de marca | El tono y estilo de comunicación que usa tu marca. | Nuestra voz es casual pero informativa, asegurando claridad sin ser demasiado formal. |
| Arquetipo de marca | El arquetipo que representa la personalidad de tu marca (el Héroe, el Creador, etc.). | Encarnamos el arquetipo del "Explorador", siempre buscando nuevos desafíos y aventuras. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 2: Describe la personalidad de tu marca" }

### Paso 3: Define el lenguaje que debe evitarse (opcional) {#step-3-define-language-that-should-be-avoided-optional}

En **Exclusions**, enumera cualquier lenguaje o estilo que no se alinee con tu marca. Por ejemplo, podrías querer evitar el "sarcasmo", las "actitudes negativas" o los tonos "condescendientes". Mantén este campo en 300 caracteres o menos.

![La ventana "Create brand guideline" con campos para ingresar el nombre, la descripción, la personalidad, las exclusiones y el tono.]({% image_buster /assets/img/guidelines_create.png %})

### Paso 4: Prueba tus directrices {#step-4-test-your-guidelines}

Prueba tus directrices para ver cómo funcionan. Expande **Test your guidelines** para generar texto de ejemplo y ajústalo según sea necesario.

### Paso 5: Guarda tus directrices {#step-5-save-your-guidelines}

Cuando estés conforme con tus directrices, selecciona **Save brand guideline**. Tus directrices se guardan en tu espacio de trabajo para uso futuro.

{% alert important %}
Puedes cambiar el idioma de salida independientemente del idioma en el que esté tu texto, pero ni Braze ni OpenAI garantizan la calidad de la traducción. Siempre prueba y verifica las traducciones antes de usarlas.
{% endalert %}

## Gestión de directrices de marca {#managing-brand-guidelines}

Puedes editar las directrices de marca seleccionándolas en la página **Brand Guidelines**. Archiva una directriz de marca para desactivarla y que deje de estar disponible en los creadores de mensajes. Para activarla de nuevo y que sea seleccionable, puedes filtrar por directrices de marca archivadas y luego desarchivarla.

## Uso de directrices de marca {#using-brand-guidelines}

En el panel de chat de Operator, selecciona <i class="fa-regular fa-plus"></i>&nbsp;**Add context for Operator** y luego elige una o más directrices en **Brand guidelines**. Operator aplica las directrices que selecciones al texto generado, las plantillas y las imágenes. De forma predeterminada, no hay nada seleccionado.

![Selección de directrices de marca en el panel de chat de Operator.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

Cuando configures un agente, selecciona directrices de marca en [Agregar contexto]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#add-resources) para que el agente siga esa voz y ese estilo. Agent Console selecciona la opción predeterminada del espacio de trabajo por ti.

{% multi_lang_include brazeai/generative_ai/policy.md %}