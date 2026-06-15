---
nav_title: Control de calidad del contenido
article_title: Control de calidad del contenido con inteligencia artificial
page_order: 4
description: "Este artículo de referencia explica cómo realizar un control de calidad del contenido de tus mensajes con IA directamente desde el creador de mensajes."
---

# Control de calidad del contenido con BrazeAI {#content-qa-with-brazeai}

> Aprende a revisar tu contenido con BrazeAI<sup>TM</sup>, para que puedas detectar errores ortográficos, gramaticales, tonos inapropiados o lenguaje ofensivo antes de enviarlo.

## Características compatibles {#supported-features}

Se admiten las siguientes características para ayudar a mejorar la calidad de tu contenido:

| Característica                     | Descripción |
|----------------------------|-------------|
| Revisión ortográfica y gramatical | Comprueba automáticamente si hay errores ortográficos y gramaticales en tu mensaje. Sugiere correcciones y proporciona recomendaciones para mejorar la exactitud general del contenido. |
| Análisis del tono              | Evalúa el tono del mensaje para identificar posibles problemas. Ayuda a garantizar que el tono pretendido se alinea con el estilo de comunicación deseado y ayuda a evitar malentendidos u ofensas involuntarias. |
| Detección de lenguaje ofensivo | Analiza tu mensaje en busca de lenguaje potencialmente ofensivo o inapropiado, permitiéndote revisar el contenido y mantener una comunicación respetuosa. |
| Comprobación de contenido accidental   | Detecta cualquier inclusión de código, lenguaje de marcado o mensajes de prueba que puedan haberse añadido de forma involuntaria, incluido cualquier código Liquid que no se haya renderizado para un usuario de prueba. |
| Asistencia en varios idiomas     | Aunque no cuenta con el apoyo oficial de OpenAI, GPT puede entender [varios idiomas](https://openai.com/research/gpt-4#:~:text=GPT%2D4%203%2Dshot%20accuracy%20on%20MMLU%20across%20languages). Ten en cuenta que Braze no transmite ninguna información sobre el idioma o la configuración regional de tu texto cuando se envía a OpenAI, por lo que los resultados pueden variar en función del idioma en el que escribas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Características compatibles" }

## Uso de BrazeAI<sup>TM</sup> para el control de calidad del contenido {#using-brazeaitm-to-qa-content}

{% alert note %}
Por el momento, esta característica solo está disponible para SMS, push de Android, push de iOS y mensajes tradicionales dentro de la aplicación.
{% endalert %}

1. Después de redactar un mensaje push para móviles, un SMS o un mensaje tradicional dentro de la aplicación, ve a la pestaña **Test**.
2. Localiza la sección **Content QA with AI**.
3. Haz clic en **Test Content**.

![Sección de control de calidad del contenido con IA en la pestaña Test.]({% image_buster /assets/img/content_qa_ai.png %})

## Buenas prácticas {#best-practices}

Ten en cuenta lo siguiente para sacar el máximo partido al control de calidad de contenidos con IA:

- **Corrige tu mensaje:** Aunque el corrector de contenido puede ayudar a identificar errores, sigue siendo esencial corregir tu contenido manualmente. Confía en las sugerencias generadas por la IA como una guía útil, pero utiliza tu criterio para garantizar la precisión.
- **Comprende el análisis del tono:** Los resultados del análisis del tono son subjetivos y se basan en la comprensión del modelo de IA. Aunque pueden aportar información útil, ten en cuenta el tono que pretendes utilizar y el contexto de la conversación para hacer los ajustes oportunos.
- **Comprueba dos veces el lenguaje ofensivo marcado:** La detección de lenguaje ofensivo está diseñada para ser robusta, pero ocasionalmente puede marcar falsos positivos. Revisa detenidamente las secciones marcadas y haz los cambios necesarios.

{% multi_lang_include brazeai/generative_ai/policy.md %}