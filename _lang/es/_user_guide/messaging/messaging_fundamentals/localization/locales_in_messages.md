---
nav_title: Mensajes multilingües
article_title: Mensajes multilingües
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "Este artículo proporciona los pasos para usar configuraciones regionales en tus mensajes."
---

# Mensajes multilingües {#multi-language-messages}

> Después de añadir configuraciones regionales a tu espacio de trabajo, puedes dirigirte a usuarios en diferentes idiomas, todo dentro de un solo push, correo electrónico, banner, mensaje dentro de la aplicación o Content Block.

## Requisitos previos {#prerequisites}

{% tabs %}
{% tab Configuraciones regionales multilingües %}

{% multi_lang_include messaging/localization/locales.md section='multi-language prerequisites' %}

{% endtab %}
{% tab Tipos de mensaje %}

| Característica | Permisos de usuario requeridos |
| --- | --- |
| Tipos&nbsp;de&nbsp;mensaje | Necesitas estos permisos para añadir configuraciones regionales y traducciones a Campaigns y Canvas:<br><br> {::nomarkdown} <ul><li>Edit Campaigns</li><li>Edit Canvases</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos"}

{% endtab %}
{% tab Plantillas %}

| Característica | Permisos de usuario requeridos |
| --- | --- |
| Plantillas | Necesitas estos permisos para el tipo de plantilla al que deseas añadir configuraciones regionales y traducciones:<br><br> {::nomarkdown} <ul><li>Edit Email Templates</li><li>Edit IAM Templates</li><li>Edit Content Block Templates</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

{% endtab %}
{% endtabs %}

## Usar locales {#use-locales}

### Paso 1: Configurar locales {#step-1-set-up-locales}

Antes de poder añadir traducciones a un mensaje, primero debes [crear los locales que deseas admitir]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings). Los locales definen las variantes de idioma (y opcionalmente de región) disponibles para la mensajería.

### Paso 2: Marcar contenido para traducción {#step-2-mark-content-for-translation}

Envuelve el texto que deseas traducir con las etiquetas de traducción de Liquid {% raw %}`{% translation your_id_here %}` y `{% endtranslation %}`{% endraw %} y asigna un ID de etiqueta. Los ID de las etiquetas de traducción deben ser únicos dentro de un mensaje. Considera usar nombres de ID semánticos que describan claramente el texto, como {% raw %}`{% translation header %}`{% endraw %}.

Aquí tienes un ejemplo de mensaje marcado para traducción: {% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

{% alert tip %}
Resalta el texto que deseas traducir y usa el atajo de teclado **Cmd + Alt + L** (macOS) o **Ctrl + Alt + L** (Windows) para envolverlo en etiquetas de traducción.<br><br> Este atajo funciona en todos los canales que admiten mensajería multilingüe, excepto en los editores de arrastrar y soltar para correo electrónico y Content Blocks. Para esos, usa el botón **Añadir personalización** para agregar etiquetas de traducción.
{% endalert %}

#### Localizar URLs {#localize-urls}

Al traducir contenido, las URLs requieren un manejo especial para evitar enlaces rotos.

##### URLs estándar (estáticas) {#standard-static-urls}

Las URLs estáticas se introducen manualmente en el editor (por ejemplo, `https://example.com`). También recomendamos lo siguiente:

| Recomendación | Motivo |
| --- | --- |
| Mantén el protocolo (`https://`) fuera de las etiquetas de traducción. Envuelve solo el dominio y la ruta (por ejemplo, `example.com/en`). | Los traductores pueden alterar o eliminar accidentalmente caracteres especiales, causando enlaces rotos. |
| No incluyas parámetros de consulta dentro de las etiquetas de traducción (por ejemplo, `?utm_source=promo`). | Los traductores pueden alterar o eliminar accidentalmente caracteres especiales, lo que resulta en enlaces rotos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URLs estándar (estáticas)" }

Una URL estándar que sigue ambas recomendaciones es:

{% raw %}
```
<a href="https://{% translation id_1 %}example.shop.com{% endtranslation %}">Visit our store</a>
```
{% endraw %}

##### URLs generadas con Liquid {#liquid-generated-urls}

Si tu URL se genera con Liquid (por ejemplo, {% raw %}`{% landing_page_url %}`{% endraw %}), recomendamos lo siguiente:

| Recomendación | Motivo |
| --- | --- |
| Envuelve la URL generada con Liquid en etiquetas de traducción solo si debe ser localizada. | La sintaxis de Liquid debe preservarse cuidadosamente para que se renderice correctamente. |
| No incluyas parámetros de consulta (por ejemplo, `?utm_source=promo`) dentro de las etiquetas de traducción. | Los traductores pueden alterar o eliminar accidentalmente caracteres especiales, lo que resulta en enlaces rotos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URLs generadas con Liquid" }

Una URL generada con Liquid que sigue ambas recomendaciones es:

{% raw %}
```
<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}">View details</a>
```
{% endraw %}

{% alert important %}
Si estás usando [seguimiento de enlaces de correo electrónico](#email-link-tracking) (aliasing de enlaces o plantillas de enlaces), se requiere configuración adicional cuando las URLs están envueltas en etiquetas de traducción.
{% endalert %}

#### Atributos y estructura HTML {#html-attributes-and-structure}

Solo envuelve texto legible por humanos en etiquetas de traducción. Evita envolver atributos HTML (como `class`, `style` o `id`) u otro código estructural. Los atributos HTML controlan el diseño, el estilo y la funcionalidad. Envolverlos en etiquetas de traducción puede romper el formato o los estilos en las versiones localizadas de tu mensaje.

Este texto está correctamente envuelto:

{% raw %}
```
<p class="headline" style="color: red;">
  {% translation id_1 %}Welcome to our sale{% endtranslation %}
</p>
```
{% endraw %}

{% details Texto envuelto incorrectamente %}

Este texto está envuelto **incorrectamente**:

{% raw %}
```
{% translation id_1 %}
<p class="headline" style="color: red;">
  Welcome to our sale
</p>
{% endtranslation %}
```
{% endraw %}

{% enddetails %}

### Paso 3: Añadir locales a tu mensaje {#step-3-add-locales-to-your-message}

Después de añadir etiquetas de traducción a tu mensaje, selecciona **Administrar idiomas** en el editor (**Idiomas** en los editores de arrastrar y soltar para correo electrónico y Content Blocks) y selecciona al menos un locale para el que deseas añadir traducciones.

![El desplegable Añadir locale con opciones para seleccionar el locale predeterminado o atributos personalizados.]({% image_buster /assets/img/multi-language_support/select_locale_type.png %}){: style="max-width:70%;"}

#### Content Blocks que contienen traducciones {#content-blocks-containing-translation}

Si tu mensaje contiene Content Blocks que ya tienen traducciones guardadas, no necesitas volver a cargar esas traducciones. Las traducciones guardadas se aplican automáticamente cuando el Content Block se añade a tu mensaje.

En el modal **Administrar idiomas**, los Content Blocks con traducciones guardadas aparecen en la lista, junto con los locales que admiten. Esto te permite ver qué partes de tu mensaje ya están localizadas antes de añadir nuevas traducciones.

![La sección Administrar idiomas con una lista de Content Blocks que tienen traducciones guardadas.]({% image_buster /assets/img/multi-language_support/content_blocks_translations.png %}){: style="max-width:70%;"}

{% alert important %}
Asegúrate de que cada Content Block incluya traducciones para cada locale añadido a tu mensaje. Si a un Content Block le faltan traducciones para uno de los locales que añadiste, se mostrará en su idioma original para los usuarios en ese locale.
{% endalert %}

### Paso 4: Añadir traducciones {#step-4-add-translations}

Después de seleccionar los locales, añade traducciones a tu mensaje usando uno de los siguientes métodos:

![La pestaña Añadir traducciones con opciones para cargar traducciones por CSV o conectándose con partners de traducción.]({% image_buster /assets/img/multi-language_support/add_translations.png %}){: style="max-width:70%;"}

{% tabs %}
{% tab Cargar plantilla CSV %}

Selecciona **Descargar plantilla** para descargar un CSV que contiene una matriz de tus ID de traducción y locales seleccionados. Introduce las traducciones para cada locale. Carga el archivo completado y las traducciones se aplicarán a tu mensaje.

{% alert important %}
Para evitar problemas de visualización con caracteres no ingleses, evita usar Excel para tu CSV de traducción.
{% endalert %}

![CSV con etiquetas de traducción para un título, texto de oferta, monto de oferta y CTA.]({% image_buster /assets/img/multi-language_support/csv_template_example.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Usar la API de traducción %}

Usa una API de traducción de un partner para administrar y actualizar traducciones en tus Campaigns y Canvas. Esto es útil si usas un sistema externo para localización o deseas conectarte directamente con un partner de traducción.

Para usar los endpoints de traducciones con Canvas, incluye los siguientes parámetros:
  - `workflow_id`
  - `step_id`
  - `message_variation_id`

{% alert note %}
Al usar la API de traducción con pasos en Canvas que se crearon después de que el Canvas se lanzó, el `message_variation_id` que pases a la API estará vacío o en blanco.
{% endalert %}

{% endtab %}
{% endtabs %}

### Paso 5: Previsualizar traducciones {#step-5-preview-translations}

Para previsualizar tu mensaje, selecciona la opción **Usuario multilingüe** en el desplegable **Previsualizar como usuario**. Esto te permite alternar entre diferentes definiciones de locale para previsualizar todas las traducciones de tu mensaje.

![Previsualizaciones de locales]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

## Gestionar traducciones {#manage-translations}

### Duplicar pasos en Canvas o Campaigns, y traducciones {#duplicate-canvas-steps-or-campaigns-and-translations}

Cuando duplicas un paso en Canvas, una Campaign o una variante, las traducciones se incluyen. Esto también aplica al copiar entre espacios de trabajo, siempre que los locales estén definidos en ese espacio de trabajo de destino. Asegúrate de revisar y actualizar las traducciones en consecuencia cuando realices modificaciones en tu Canvas o Campaign.

### Guardar traducciones en Content Blocks {#save-translations-in-content-blocks}

Los Content Blocks admiten multilenguaje de la misma manera que los mensajes. Al crear o editar Content Blocks, puedes etiquetar contenido para traducción, agregar locales y cargar traducciones usando un CSV o la [API de traducciones]({{site.baseurl}}/api/endpoints/translations).

Las traducciones guardadas permanecen asociadas con el Content Block. Cuando el bloque se agrega a un mensaje, sus traducciones se incluyen automáticamente.

### Mensajes de derecha a izquierda {#right-to-left-messages}

Al completar el archivo de traducción para idiomas que se escriben de derecha a izquierda (como el árabe), envuelve la traducción con `span` para que tenga el formato adecuado:

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

### Seguimiento de enlaces en correo electrónico {#email-link-tracking}

En las Campaigns de correo electrónico, Braze realiza el seguimiento de enlaces agregando información de seguimiento (parámetros de consulta) a cada URL. Este comportamiento es compatible tanto con el [aliasing de enlaces]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing) como con las [plantillas de enlaces]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template).

Cuando una URL está envuelta en etiquetas de traducción, es posible que Braze no pueda determinar dónde agregar esta información de seguimiento. Para asegurarte de que esto funcione correctamente, debes incluir un carácter especial al final de la URL para indicar dónde se debe agregar el seguimiento.

Las URLs usan dos caracteres especiales para controlar cómo funciona esto:
  - `?` agrega seguimiento a una URL que aún no lo tiene.
  - `&` agrega seguimiento adicional si ya hay un `?` presente en la URL. Una URL solo puede contener un `?`.

| URL | Contiene&nbsp;`?` | Descripción | Ejemplo |
| --- | --- | --- | --- |
| URL estándar | No | Agrega `?` después de la etiqueta de traducción de cierre si la URL aún no contiene uno. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?">Shop Now</a>```{% endraw %} |
| URL estándar | Sí | Usa `&` al final de la URL (después de la etiqueta de traducción de cierre) si ya contiene `?`. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?ref=4&">Shop Now</a>```{% endraw %} |
| Generada con Liquid | No | Usa `?` después de las etiquetas de traducción de cierre si la URL generada aún no contiene uno. | {% raw %}```<a href="{% translation id_1 %}{{ product_url }}{% endtranslation %}?">Shop Now</a>``` {% endraw %} |
| Generada con Liquid | Sí | Usa `&` después de la etiqueta de traducción de cierre si la URL generada ya contiene un `?`. | {% raw %}```<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}&">Shop Now</a>```{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Seguimiento de enlaces en correo electrónico" }

### Configuración de idioma y accesibilidad {#language-settings-and-accessibility}

Comienza con [Idioma de accesibilidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language) en [Accesibilidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility) para el contexto de WCAG, el comportamiento de canales y editores (incluidas las páginas de destino) y la configuración de **Accesibilidad** a nivel de mensaje.

Cuando usas **mensajes multilenguaje**, alinea el idioma de accesibilidad con cada locale para que los envíos localizados declaren el idioma apropiado.

#### Configurar el idioma de accesibilidad {#configuring-the-accessibility-language}

Puedes establecer el idioma de accesibilidad en dos niveles:

##### Nivel de mensaje {#message-level}

A nivel de mensaje, establece el idioma de accesibilidad en la sección **Accesibilidad** de la configuración de tu mensaje. Para seleccionar un idioma, usar Liquid y conocer las limitaciones por canal, consulta [Idioma de accesibilidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language).

##### Nivel de locale {#locale-level}

Para mensajes multilenguaje, establece el idioma de accesibilidad para cada locale en **Configuración de localización**. Puedes usar {% raw %}`{{accessibility_language}}`{% endraw %} en la sección **Accesibilidad** para que el idioma del documento o la tarjeta se mapee a esos valores de locale.

Si ese token aparece de forma predeterminada para mensajes nuevos depende del canal y el editor. Por ejemplo, los mensajes dentro de la aplicación y los Banners se comportan de manera diferente a las páginas de destino y los correos electrónicos de arrastrar y soltar. Consulta [Idioma de accesibilidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language) para más detalles.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cuáles son los límites para las etiquetas de traducción? {#what-are-the-limits-for-translation-tags}

Al utilizar etiquetas de traducción, se aplican los siguientes límites:

- Cada mensaje puede tener hasta 200 etiquetas de traducción.
- Cada texto predeterminado (el contenido entre las etiquetas de traducción) puede tener hasta 2000 caracteres.
- Las traducciones por configuración regional pueden tener hasta 409 600 bytes (aproximadamente 409,6&nbsp;KB).

#### ¿Puedo hacer un cambio en la copia traducida en una de mis configuraciones regionales? {#can-i-make-a-change-to-the-translated-copy-in-one-of-my-locales}

Sí. Primero, haz la edición en el CSV y luego sube el archivo de nuevo para hacer un cambio en la copia traducida.

### ¿Braze proporciona traducciones? {#does-braze-provide-translations}

No. Debes [proporcionar tus propias traducciones](#step-4-add-translations) ya sea subiendo un CSV o usando la API de traducción.

### ¿Puedo anidar etiquetas de traducción? {#can-i-nest-translation-tags}

No.

#### ¿Puedo envolver mensajes HTML completos en una etiqueta de traducción? {#can-i-wrap-entire-html-messages-in-a-translation-tag}

No. Como práctica recomendada, solo debes envolver texto legible por humanos o contenido que deba ser localizado. Esto ayuda a prevenir formatos rotos, enlaces u otros elementos que no son texto.

Además, considera envolver piezas de texto más pequeñas y semánticamente relacionadas para crear traducciones precisas y evitar limitaciones de rendimiento o tamaño.

#### ¿Puedo hacer un cambio en la copia traducida en una de mis configuraciones regionales?

Sí. Si usas un CSV, primero haz la edición en el archivo y luego súbelo de nuevo para hacer un cambio en la copia traducida. Si usas la [API de traducción]({{site.baseurl}}/api/endpoints/translations), utiliza los endpoints de actualización para hacer cambios.

#### ¿Qué validaciones o comprobaciones adicionales realiza Braze? {#what-validations-or-extra-checks-does-braze-do}

| Escenario | Validación en Braze |
| --- | --- |
| Un mensaje contiene dos o más ID de traducción coincidentes que se asignan a textos diferentes. | Este archivo de traducción no se descargará. |
| A un archivo de traducción le faltan uno o más ID de etiquetas de traducción. | Este archivo de traducción no se subirá. |
| Un archivo de traducción contiene configuraciones regionales que faltan en el mensaje. | Este archivo de traducción no se subirá. |
| Las etiquetas de traducción deben añadirse a un mensaje antes de descargar la plantilla de traducción. | Este archivo de traducción no se descargará. |
| Las etiquetas de traducción encontradas en tu archivo subido faltan en tu mensaje. | Las traducciones adicionales no se guardarán en el mensaje. |
| {% raw %}Un mensaje contiene una o más etiquetas de Liquid rotas. Para abrir etiquetas usa `{% translation your_id_here %}`, cierra las etiquetas de traducción con `{% endtranslation %}`.{% endraw %} | Este archivo de traducción no se descargará. |
| Un archivo de traducción contiene texto predeterminado que no coincide con lo que hay en el mensaje. | Las traducciones se añaden, pero el texto original del mensaje no se actualiza. |
| Una o más de las configuraciones regionales en un mensaje han sido eliminadas en la configuración y ya no existen. | Las traducciones que ya se han añadido siguen existiendo dentro del mensaje. Si se eliminan del mensaje, las traducciones se pierden. |
| Las etiquetas de traducción contienen URL completas o URL generadas por Liquid. | Las etiquetas de traducción que contienen URL se identifican en caso de que ocurran problemas con enlaces rotos o seguimiento de enlaces. |
| Las etiquetas de traducción incluyen parámetros de consulta. | Las etiquetas de traducción que contienen parámetros de consulta se identifican en caso de que ocurran problemas con enlaces rotos o seguimiento de enlaces. |
| Las etiquetas de traducción contienen atributos o estructuras HTML. | Las etiquetas de traducción que contienen atributos o estructuras HTML se identifican en caso de que ocurran problemas con estilos y formato. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="¿Qué validaciones o comprobaciones adicionales realiza Braze?" }