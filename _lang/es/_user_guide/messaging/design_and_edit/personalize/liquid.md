---
nav_title: Referencia de Liquid
article_title: Referencia de Liquid
page_order: 3
layout: dev_guide
alias: /liquid/
search_rank: 3
guide_top_header: "Referencia de Liquid"
guide_top_text: "Liquid es un lenguaje de plantillas de código abierto creado por Shopify y utilizado por Braze para potenciar la personalización dinámica. En lugar de enviar un mensaje estático a todos, Liquid te permite crear plantillas que cambian su contenido en función de los datos del perfil, el comportamiento o el idioma de cada destinatario. Usa los artículos de esta sección para conocer las etiquetas compatibles, los filtros, la lógica condicional, los valores predeterminados y los patrones de personalización comunes."
description: "Esta página de inicio cubre todo lo relacionado con Liquid, como las etiquetas de personalización compatibles, los filtros, la configuración de valores predeterminados y más."

guide_featured_title: "Artículos de la sección"
guide_featured_list:
- name: Usar Liquid
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid
  image: /assets/img/braze_icons/beaker-02.svg
- name: Etiquetas de personalización compatibles
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags
  image: /assets/img/braze_icons/tag-01.svg
- name: Operadores
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/operators
  image: /assets/img/braze_icons/code-02.svg
- name: Filtros
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/filters
  image: /assets/img/braze_icons/flag-02.svg
- name: Filtros avanzados
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters
  image: /assets/img/braze_icons/settings-01.svg
- name: Establecer valores predeterminados
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values
  image: /assets/img/braze_icons/table.svg
- name: Lógica condicional de mensajería
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic
  image: /assets/img/braze_icons/columns-01.svg
- name: Cancelar mensajes
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: Biblioteca de casos de uso de Liquid
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases
  image: /assets/img/braze_icons/list.svg
- name: Tutoriales
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/tutorials
  image: /assets/img/braze_icons/book-open-01.svg
- name: Preguntas frecuentes
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/faq
  image: /assets/img/braze_icons/annotation-question.svg

---

## Acerca de Liquid {#about-liquid}

Liquid actúa como un puente entre tu mensaje y los datos de usuario. Cuando envías un mensaje, Braze escanea el texto en busca de sintaxis Liquid. Cuando la encuentra, extrae los datos relevantes de ese usuario específico y reemplaza el código con el valor real antes de enviar el mensaje.

Por ejemplo, puedes recuperar un atributo personalizado de un perfil de usuario que sea de tipo de datos entero y redondear ese valor al número entero más cercano. Para más información sobre la sintaxis y el uso de Liquid, consulta [**Etiquetas de personalización compatibles**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

El lenguaje de plantillas Liquid admite el uso de objetos, etiquetas y filtros.

- [**Objetos**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) te permiten insertar atributos personalizados en tus mensajes.
- [**Etiquetas**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) te permiten insertar datos en la mensajería y usar lógica condicional para enviar mensajes si se cumplen ciertas condiciones. Por ejemplo, puedes usar etiquetas para incluir lógica inteligente, como sentencias "if", en tus campañas.
- [**Filtros**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters) te permiten reformatear atributos personalizados y contenido dinámico. Por ejemplo, podrías usar el [filtro `date`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters#date-filter) para convertir una marca de tiempo, como *2016-09-07 08:43:50 UTC*, en una fecha, como *7 de septiembre de 2016*.

{% alert warning %}
Actualmente, Braze no es compatible con el 100% del Liquid de Shopify, solo con ciertas partes que hemos intentado describir en nuestra documentación. Recomendamos encarecidamente probar todos los mensajes que usen Liquid antes de enviarlos para reducir el riesgo de errores o de usar Liquid no compatible.
{% endalert %}

### Compatibilidad con Liquid 5 {#liquid-5-support}

Braze es compatible con Liquid hasta **Liquid 5 de Shopify** inclusive. La implementación de Liquid admite tipos de etiquetas de personalización de sintaxis y control de espacios en blanco. Para más información sobre etiquetas específicas, consulta [etiquetas de sintaxis]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#syntax-tags).

Los siguientes filtros nuevos de arrays y matemáticos están disponibles para usar en tu Liquid mientras construyes tu mensajería.
- `at_least`
- `at_most`
- `compact`
- `concat`
- `sort_natural`
- `where`

Consulta [Filtros]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters) para ver las definiciones.

## Términos que debes conocer {#terms-to-know}

Estos términos se reinterpretan a partir de la [**documentación de Shopify**](https://shopify.github.io/liquid/basics/introduction/) en función de nuestro nivel de compatibilidad.

{% raw %}

| Término | Definición | Ejemplo |
|---|---|---|
| Liquid | Un lenguaje de plantillas de uso común y orientado al cliente, creado por Shopify y escrito en Ruby, que se utiliza para cargar y extraer contenido dinámico. | `{{${first_name}}}` insertará el nombre de un usuario en un mensaje. |
| Objeto | Una denotación de una variable y la ubicación del nombre de variable deseado que indica a Liquid dónde mostrar contenido en el mensaje. | `{{${city}}}` insertará la ciudad de un usuario en un mensaje. |
| Etiqueta de lógica condicional | Se utiliza para crear lógica y controlar el flujo del contenido del mensaje. En Braze, las etiquetas de lógica condicional se usan para crear excepciones y variaciones en los mensajes basándose en ciertos criterios predefinidos. | ```{% if ${language} == 'en' %}``` activará tu mensaje de una forma determinada en caso de que un usuario haya indicado "English" como su idioma. |
| Filtros | Se utilizan para cambiar, acotar o reformatear la salida del objeto de Liquid. A menudo se usan para crear operaciones matemáticas. | ```{{"Big Sale" | upcase}}``` hará que las palabras "Big Sale" aparezcan como "BIG SALE" en el mensaje. |
| Operadores | Se utilizan en los mensajes para crear dependencias o criterios que pueden afectar qué mensaje recibe tu usuario. | Si un usuario cumple los criterios definidos en un mensaje etiquetado con `{% custom_attribute.${Total_Revenue} > 0%}`, recibirá el mensaje. Si no, recibirá otro mensaje designado (o no), dependiendo de lo que configures. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Términos que debes conocer" }

{% endraw %}

<br>