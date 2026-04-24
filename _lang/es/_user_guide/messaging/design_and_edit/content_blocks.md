---
nav_title: Bloques de contenido
article_title: Bloques de contenido
alias: "/dnd/content_blocks/"
page_order: 4
description: "Aprende a crear, usar y administrar Bloques de contenido reutilizables en tus campañas y Canvas de Braze."
page_type: reference
tool:
  - Templates
  - Media

---

# Bloques de contenido

> Los Bloques de contenido te permiten administrar contenido reutilizable de canales cruzados en una única ubicación centralizada. Úsalos para crear una apariencia consistente en tus campañas, distribuir los mismos códigos de oferta a través de diferentes canales o crear activos predefinidos para una mensajería consistente a escala. También puedes crear y administrar tus Bloques de contenido [usando la API]({{site.baseurl}}/api/endpoints/templates/).

## Crear un bloque de contenido

Hay dos tipos de Bloques de contenido: arrastrar y soltar y HTML. Cada tipo corresponde a su editor.

{% tabs %}
{% tab Arrastrar y soltar %}

{% multi_lang_include create_content_block.md location="dnd" %}

{% alert important %}
Cada bloque de contenido de arrastrar y soltar está limitado a una fila. Sin embargo, puedes usar bloques de editor de arrastrar y soltar para crear y personalizar el bloque de contenido según tus necesidades de mensajería por correo electrónico.
{% endalert %}

{% endtab %}
{% tab HTML %}

{% multi_lang_include create_content_block.md location="html" %}

{% endtab %}
{% endtabs %}

### Especificaciones de los Bloques de contenido

| Atributo del bloque de contenido | Especificaciones |
|---|---|
| Nombre | Campo obligatorio con un máximo de 100 caracteres. No se puede renombrar después de que el bloque de contenido haya sido guardado. Además, no puedes nombrar un nuevo bloque de contenido con el mismo nombre que uno anterior, incluso si el anterior ha sido archivado. |
| Descripción | (opcional) Máximo de 250 caracteres. Describe el bloque de contenido para que otros usuarios de Braze sepan para qué sirve y dónde se usa. |
| Tamaño del contenido | Máximo de 50 KB. |
| Ubicación | Los Bloques de contenido no se pueden usar dentro de un pie de página de correo electrónico, pero puedes [crear un bloque de contenido que incluya un pie de página](#email-footers) para usarlo en tus correos electrónicos. |
| Creación | Editor HTML o editor de arrastrar y soltar. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Al crear Bloques de contenido, puede ser útil visualizar HTML y Liquid añadiendo saltos de línea. Si estos saltos de línea se dejan durante el envío, corres el riesgo de tener espacios innecesarios que pueden afectar cómo se renderizará el bloque. Para evitar esto, usa la etiqueta **Capture** en tu bloque junto con el filtro **&#124; strip**.
{% raw %}
```
{% capture your_variable %}
{{content_blocks.${your_content_block}}}
{% endcapture %}{{your_variable | strip}}
```
{% endraw %}
{% endalert %}

## Usar Bloques de contenido

Después de crear tu bloque de contenido, puedes insertarlo en tus mensajes usando el editor o Liquid.

### Usar el editor de arrastrar y soltar {#using-the-editor}

Para añadir un bloque de contenido en el editor de arrastrar y soltar:

1. Ve a la pestaña **Filas** en el editor y selecciona **Bloques de contenido**.
2. Arrastra y suelta tu bloque de contenido en el editor de correo electrónico.
3. (Opcional) Ajusta el ancho de tu bloque de contenido seleccionando el botón en el menú de navegación. El ancho predeterminado es 100 % cuando no se especifica en la configuración global de estilo de tu correo electrónico; de lo contrario, se respetará la configuración global. <br><br>![Una flecha de doble sentido con una opción para editar el ancho.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }<br><br>

{% alert note %}
Los Bloques de contenido añadidos mediante arrastrar y soltar **no están vinculados** al bloque de contenido original. Para ver los cambios realizados en el original, arrástralo de nuevo al editor de correo electrónico.
{% endalert %}

Pueden producirse desalineaciones en el editor de arrastrar y soltar cuando se añaden múltiples Bloques de contenido a un único bloque de fila. Intenta usar bloques de fila separados para mantener la alineación en tu contenido a nivel de fila.

### Usar Liquid

Para insertar un bloque de contenido usando Liquid:

1. Copia la **etiqueta de Liquid del bloque de contenido** de la sección **Detalles del bloque de contenido**.
2. Inserta la etiqueta de Liquid del bloque de contenido en el mensaje. También puedes empezar a escribir el Liquid y dejar que la etiqueta se autocomplete.

En el editor de arrastrar y soltar, también puedes añadir un bloque de contenido a través del panel de **personalización**:

1. Ve a tu campaña de correo electrónico y selecciona **Editar cuerpo del correo electrónico**.
2. Haz clic en <i class="fas fa-plus"></i> **Personalización**.
3. Selecciona **Bloques de contenido** en el desplegable **Tipo de personalización**.
4. Selecciona el nombre de tu bloque de contenido en el campo **Atributo**.
5. Copia y pega el fragmento de Liquid en un bloque de editor de texto. <br>![La pestaña Añadir personalización con opciones.]({% image_buster /assets/img_archive/dnd_content_block_personalization.png %}){: style="max-width:30%;"}

{% alert important %}
Los Bloques de contenido insertados mediante Liquid **están vinculados** al bloque de contenido original y reflejarán cualquier cambio en la plantilla.
{% endalert %}

### Cosas que debes saber

- Usar Bloques de contenido HTML en correos electrónicos de arrastrar y soltar **o** Bloques de contenido de arrastrar y soltar en correos electrónicos HTML puede provocar problemas de renderizado inesperados. Esto se debe a que el editor de arrastrar y soltar genera HTML y CSS que renderizan el contenido de forma dinámica, mientras que el editor HTML es más estático.
- Las propiedades del evento de Canvas solo son compatibles en un Canvas. Si haces referencia a un bloque de contenido con propiedades de entrada de Canvas en una campaña, no se completarán.

## Vista previa de Bloques de contenido

Después de añadir un bloque de contenido en una campaña o Canvas activo, puedes previsualizarlo desde la Biblioteca de bloques de contenido pasando el cursor sobre el bloque de contenido y seleccionando el icono <i class="fa fa-eye preview-icon"></i> **Vista previa**.

Esta vista previa incluye información sobre el bloque de contenido, como quién lo creó, etiquetas, fecha de creación, fecha de última edición, descripción, tipo de editor, recuento de inclusiones con detalles (una lista clicable de mensajes o Bloques de contenido que usan el bloque de contenido) y una vista previa real del bloque de contenido.

![Una vista previa de un bloque de contenido "Workout_Promo" para ciclismo y baile que tiene una inclusión.]({% image_buster /assets/img/preview_tab_content_block.png %}){: style="max-width:60%;"}

## Anidar Bloques de contenido

Los Bloques de contenido se pueden anidar, pero solo una vez. Puedes anidar el bloque de contenido A dentro del bloque de contenido B, pero no podrás anidar el bloque de contenido B dentro del bloque de contenido C.

{% alert warning %}
Nada te impedirá anidar un tercer nivel de bloque de contenido, pero no verás que el contenido se expanda en anidaciones más allá del segundo nivel. El contenido y el fragmento de Liquid se eliminan del mensaje.
{% endalert %}

## Actualizar y copiar Bloques de contenido

Si decides actualizar un bloque de contenido, se actualizará en todos los mensajes donde el bloque de contenido esté insertado mediante Liquid. Si el bloque de contenido se importó usando el desplegable **Bloques de contenido** en **Filas** en el editor de arrastrar y soltar, no se actualizará en todos los mensajes.

Si quieres actualizar un bloque de contenido para un solo mensaje o hacer una copia para usarla en otros mensajes, puedes copiar el HTML del mensaje original al nuevo, o editar el bloque de contenido original (debe haber sido usado en un mensaje previamente) y guardarlo. Recibirás un aviso que te permitirá guardarlo como un nuevo bloque de contenido.

Después de realizar ediciones en un bloque de contenido, puedes guardar y lanzar el bloque de contenido actualizado seleccionando **Lanzar bloque de contenido**. O puedes seleccionar **Más** > **Duplicar** para crear un duplicado de tu bloque de contenido.

![Un bloque de contenido que dice "Welcome to our newsletter".]({% image_buster /assets/img/copy-content-block.png %})

## Usar pies de página de correo electrónico en Bloques de contenido {#email-footers}

Los Bloques de contenido no se pueden usar dentro de un pie de página de correo electrónico, pero puedes crear un bloque de contenido que incluya contenido de pie de página para usarlo en tus correos electrónicos. Para hacerlo:

1. Ve a **Configuración** > **Preferencias de correo electrónico** > **Personalizar pie de página** y crea el pie de página.
2. Añade el pie de página a un bloque de contenido en la **Biblioteca de bloques de contenido**.
3. Añade ese bloque de contenido a tus plantillas de correo electrónico o mensajes.

## Archivar Bloques de contenido

![Menú desplegable de configuración expandido que muestra tres opciones: Archivar, Duplicar y Copiar al espacio de trabajo.]({% image_buster /assets/img/template_archive_cog.png %}){: style="max-width:20%;float:right;margin-left:15px;" }

Una vez que hayas terminado de usar un bloque de contenido, puedes archivarlo desde la página de **Plantillas**. Los Bloques de contenido archivados son de solo lectura, así que desarchiva el bloque de contenido antes de editarlo. Los Bloques de contenido no se pueden archivar si se están usando en algún mensaje.

### Mejores prácticas

- Cuando tu bloque solo se usa en unos pocos correos electrónicos, te recomendamos archivar el bloque obsoleto y actualizar tus mensajes en vivo con un bloque más nuevo que no haya sido archivado.
- Cuando tu bloque solo tiene un error tipográfico o necesita un cambio menor, no recomendamos archivar el bloque. En su lugar, ¡actualiza el bloque y sigue enviando!
- Cuando tu bloque se usa en más mensajes de los que puedes administrar razonablemente con la primera sugerencia de esta lista, te recomendamos eliminar todo el contenido del bloque. Esto evita la inclusión de información obsoleta en cualquier mensaje.
- Si archivas accidentalmente un bloque de contenido, puedes desarchivarlo.

![Panel de Bloques de contenido guardados donde el menú desplegable de configuración de "Test_32" está expandido para mostrar tres opciones: Desarchivar, Duplicar y Copiar al espacio de trabajo]({% image_buster /assets/img/unarchive-content-block.png %})