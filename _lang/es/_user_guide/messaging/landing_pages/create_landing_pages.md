---
nav_title: Crear páginas de inicio
article_title: Crear páginas de inicio
description: "Este artículo explica cómo crear y personalizar páginas de inicio de Braze con el editor de arrastrar y soltar."
page_order: 0
---

# Crear páginas de inicio {#create-landing-pages}

> Aprende a crear y personalizar una página de inicio con el editor de arrastrar y soltar, para que puedas ampliar tu audiencia y recopilar preferencias directamente en Braze.

## Requisitos previos {#prerequisites}

Para acceder al creador de páginas de inicio, necesitas [ciertos permisos]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites). Si no tienes acceso, pide ayuda a tu administrador de Braze.

## Crear una página de inicio {#create-a-landing-page}

Una página de inicio es una página web en vivo y publicada con una URL compartible que tus clientes pueden visitar.

{% alert note %}
Las plantillas de páginas de inicio son puntos de partida de diseño sin publicar y sin URL pública, lo que significa que no se pueden compartir con tus clientes. Para crear una página a partir de una plantilla, consulta [Uso de plantillas](#using-templates).
{% endalert %}

### Paso 1: Crear un nuevo borrador {#step-1-create-a-new-draft}

Ve a **Mensajería** > **Páginas de inicio** y selecciona **Crear página de inicio**. También puedes seleccionar el nombre de una página de inicio existente para duplicarla o realizar cambios.

### Paso 2: Introducir los detalles de la página {#step-2-enter-the-page-details}

Añade detalles internos y públicos que te ayuden a organizar, personalizar la marca y compartir tu página de inicio.

#### Detalles generales {#general-details}

Introduce un nombre y una descripción para la página de inicio. Estos detalles se utilizan para buscar la página en tu espacio de trabajo interno. No serán visibles para tus clientes.

#### Detalles del sitio {#site-details}

Configura las metaetiquetas para personalizar cómo aparece tu página en la pestaña del navegador y optimizar los resultados de los motores de búsqueda. Serán visibles para tus clientes.

Te sugerimos seguir estas buenas prácticas:

| Campo | Descripción | Recomendaciones |
| --- | --- | --- |
| Título del sitio | El título que se muestra en la pestaña del navegador. | Usa hasta 60 caracteres. |
| Meta descripción | Un fragmento de texto que se muestra en los resultados de búsqueda. | Usa entre 140 y 160 caracteres. |
| Favicon | El icono que aparece junto al título del sitio en la pestaña del navegador. | Usa una relación de aspecto de 1:1 y un tipo de archivo compatible: PNG, JPEG o ICO. |
| URL de la página | Esta es la ruta URL de tu página de inicio. Este valor también se referencia al usar [etiquetas de Liquid de páginas de inicio]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) que puedes incrustar en un mensaje para identificar automáticamente cuándo envían tu formulario. | Este valor debe ser único en tu espacio de trabajo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Detalles del sitio" }

### Paso 3: Personalizar la página {#step-3-customize-the-page}

Si aún no lo has hecho, selecciona **Guardar como borrador**. Para empezar a personalizar tu página, selecciona **Editar página de inicio**. El editor de arrastrar y soltar precargará una plantilla predeterminada que puedes personalizar para adaptarla a tu caso de uso.

![Un ejemplo de página de inicio creándose en el editor de arrastrar y soltar.]({% image_buster /assets/img/landing_pages/template.png %})

El editor utiliza dos tipos de componentes para la composición de páginas de inicio: bloques básicos y bloques de formulario. Todos los bloques deben colocarse en una fila. Para una referencia dedicada de cada bloque y sus propiedades, consulta [Bloques de editor (páginas de inicio)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).

![La sección "Construir" que contiene "Filas" y "Bloques de formulario".]({% image_buster /assets/img/landing_pages/dnd.png %}){: style="max-width:35%;"}

{% tabs %}
{% tab Bloques básicos %}

Puedes usar estos bloques para añadir contenido y personalizar el diseño de tu página de inicio.

| Tipo de bloque | Descripción |
|-------------|-------------|
| Título | Un bloque de texto para añadir un encabezado o título a tu contenido. Útil para estructurar secciones y mejorar la legibilidad. |
| Párrafo | Un bloque de texto para descripciones más largas o contexto adicional. Admite formato de texto enriquecido. |
| Botón | Un elemento clicable que dirige a los usuarios a una acción específica, como abrir un enlace o enviar un formulario. |
| Botón de opción | Añade una lista de opciones de las cuales los usuarios deben seleccionar una. Al enviarse, el perfil de usuario registra el atributo personalizado asociado. |
| Imagen | Un bloque para mostrar imágenes. Puedes subir una imagen o proporcionar una URL para referenciar una fuente externa. |
| Enlace | Un hipervínculo en el que los usuarios pueden hacer clic para navegar a una URL específica. Puede incrustarse dentro del texto o ser independiente. |
| Espaciador | Un bloque invisible que añade espacio vertical entre elementos para mejorar el diseño y la legibilidad. |
| Código personalizado | Un bloque que te permite insertar y ejecutar HTML, CSS o JavaScript personalizado para una personalización avanzada. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 3: Personalizar la página" }

#### Texto con span {#span-text}

Para aplicar estilos específicos a bloques de texto sin código personalizado, resalta el texto que deseas estilizar y luego selecciona **Envolver con span para estilo**.

![Cuadro de texto con diferentes secciones de texto estilizadas, como diferentes tamaños de fuente y colores, y una sección resaltada que muestra una barra de herramientas con la opción de "Envolver con span para estilo".]({% image_buster /assets/img/landing_pages/wrap_with_span.png %}){: style="max-width:50%;"}

Ajusta las propiedades del span para actualizar el estilo de tu texto, que incluye:

- Familia, peso y tamaño de fuente
- Altura de línea
- Espaciado entre letras
- Alineación y color del texto
- Relleno del bloque

![Panel de propiedades del span con diferentes opciones para actualizar.]({% image_buster /assets/img/landing_pages/span_properties.png %}){: style="max-width:35%;"}


{% endtab %}
{% tab Bloques de formulario %}

Puedes usar estos bloques para crear un formulario que vincule los datos enviados por el usuario a su perfil en Braze. Ten en cuenta que, si usas bloques de formulario, también necesitarás crear una página de inicio adicional para el estado de confirmación.

![Un bloque de formulario que registra un nuevo cliente y enviará un código de descuento a su correo electrónico.]({% image_buster /assets/img/landing_pages/form.png %}){: style="max-width:70%;"}

| Tipo de bloque | Descripción |
|---------------|-------------|
| Captura de correo electrónico | Un campo de formulario para direcciones de correo electrónico. Al enviarse, la dirección de correo electrónico se añade al perfil de ese usuario en Braze. |
| Captura de teléfono | Un campo de formulario para números de teléfono. Al enviarse, el usuario se suscribe a tu grupo de suscripción de SMS o WhatsApp. |
| Campo de entrada | Un campo de formulario que admite atributos estándar (como nombre y apellido) o una cadena de atributo personalizado de tu elección. |
| Desplegable | Los usuarios pueden seleccionar un elemento de una lista predefinida. Puedes añadir cualquier cadena de atributo personalizado a la lista. |
| Casilla de verificación | Si un usuario marca la casilla, el atributo del bloque se establece en `true`. Si se deja sin marcar, su atributo se establece en `false`. |
| Grupo de casillas de verificación | Los usuarios pueden seleccionar entre múltiples opciones presentadas. Los valores se establecen o se añaden a un atributo personalizado de tipo array definido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Texto con span" }

{% alert important %}
Después de crear una página de inicio con un formulario, asegúrate de incrustar su [etiqueta de Liquid de página de inicio]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) en tu mensaje. Con esta etiqueta, Braze puede identificar y actualizar automáticamente los perfiles de usuario existentes cuando envían el formulario.
{% endalert %}

{% endtab %}
{% endtabs %}

#### Estilos del contenedor de página {#page-container-styles}

Puedes establecer estilos que se apliquen a todos los bloques de componentes relevantes en tu página de inicio desde la pestaña **Contenedor de página**. Estos estilos se aplican en toda tu página excepto donde los anules con un bloque específico.

Te recomendamos configurar los estilos a nivel del contenedor de página antes de personalizar los estilos a nivel de bloque. También puedes añadir una imagen de fondo para toda la página.

![La sección "Contenedor de página" con opciones para personalizar imágenes de fondo, colores, detalles de borde y estilo de contenido.]({% image_buster /assets/img/landing_pages/page_container.png %}){: style="max-width:40%;"}

#### Adaptable a los dispositivos del usuario {#responsive-to-user-devices}

Puedes hacer que tu página de inicio sea adaptable al tamaño del dispositivo del usuario apilando columnas verticalmente en pantallas más pequeñas. Para habilitar esto, añade una columna a la fila que deseas hacer adaptable y luego activa **Apilar verticalmente en pantallas más pequeñas** en la sección **Personalizar columnas**.

Cuando está habilitado, también puedes invertir el apilamiento de columnas para controlar el orden vertical del contenido multicolumna en pantallas más pequeñas. Esto hace que las páginas se vean y se sientan mejor en dispositivos móviles sin código personalizado.

![El interruptor "Apilar verticalmente en pantallas más pequeñas" en la sección "Personalizar columnas".]({% image_buster /assets/img/landing_pages/device_responsive_toggle.png %}){: style="max-width:50%;"}

{% multi_lang_include drag_and_drop/hide_rows_and_blocks_by_device.md channel='landing_page' %}

#### Campos opcionales y obligatorios {#optional-and-required-fields}

Puedes elegir si ciertos campos de formulario son obligatorios u opcionales. Los campos obligatorios deben completarse antes de que se pueda enviar el formulario. Los campos opcionales pueden dejarse en blanco o sin seleccionar por el usuario.

{% alert note %}
Los botones de opción siempre son obligatorios y no se pueden establecer como opcionales. Si necesitas un campo de selección única opcional, considera usar un desplegable en su lugar.
{% endalert %}

Por ejemplo, para exigir la captura de consentimiento antes del envío del formulario, puedes activar **Entrada de campo obligatoria** para establecer una casilla de verificación como obligatoria con el texto de descargo de responsabilidad apropiado.

![Un campo de formulario de casilla de verificación con el interruptor "Entrada de campo obligatoria" seleccionado.]({% image_buster /assets/img/landing_pages/lp-optional-required.png %}){: style="max-width:50%;"}

### Paso 4: Crear una página de confirmación (opcional) {#step-4-create-a-confirmation-page-optional}

Si tu página de inicio no incluye un formulario, continúa con el siguiente paso.

Si tu página de inicio incluye un [formulario](#form-blocks), crea una segunda página de inicio que sirva como experiencia de confirmación. Esta página debe agradecer a los usuarios o proporcionar un siguiente paso después del envío del formulario.

Para vincular la página de confirmación:
- Selecciona el botón **Enviar** en tu formulario
- Usa la acción **Abrir URL web** para vincular a tu página de confirmación

Si no incluyes una página de confirmación, es posible que los usuarios no sepan que su formulario se envió correctamente. Siempre incluye una experiencia de confirmación para completar el recorrido.

{% alert note %}
Si tu página de confirmación se abre en una nueva pestaña, un usuario que regrese a la página de inicio original y vuelva a enviar con información actualizada puede sobrescribir el envío anterior, lo que resulta en datos inconsistentes.
{% endalert %}

### Paso 5: Previsualizar la página {#step-5-preview-the-page}

Puedes previsualizar tu página de inicio en la pestaña **Vista previa** del editor. Después de guardar tu página de inicio como borrador, puedes visitar la URL yendo a **Páginas de inicio** y seleccionando **Copiar URL** junto a tu página de inicio.

![Una página de inicio con el menú abierto mostrando la opción "Copiar URL".]({% image_buster /assets/img/landing_pages/copy-url.png %})

#### Compartir un enlace de vista previa {#sharing-a-preview-link}

En el editor, también puedes seleccionar **Copiar enlace de vista previa** para compartir la página con revisores que no tienen acceso al panel.

- Si tu página de inicio no usa Liquid, este enlace es el mismo que la URL directa de **Copiar URL**, abierta en modo de vista previa.
- Si tu página de inicio usa Liquid y tienes el derecho Landing Pages Pro, el enlace en su lugar renderiza la página en vivo bajo demanda y refleja tus cambios actuales en lugar de una instantánea de cuando generaste el enlace. El contenido se personaliza por usuario.

Para enlaces de vista previa en otros canales, consulta [vista previa compartible]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview).

### Paso 6: Publicar {#step-6-publish}

Antes de publicar, asegúrate de que:

- No hayas excedido el límite de páginas de inicio publicadas de tu plan
- Cada página basada en formulario esté vinculada a una [página de confirmación](#step-4-create-a-confirmation-page) usando la acción **Abrir URL web**
- Todos los campos obligatorios de la página (como la ruta URL y el título) estén completos

Cuando estés listo, selecciona **Publicar página de inicio**.

{% alert note %}
Los bloqueadores de ventanas emergentes agresivos y los bloqueadores de anuncios en iOS y en Safari (incluidos los controles integrados de Safari y las extensiones de terceros) pueden afectar negativamente el comportamiento de las páginas de inicio cuando un botón **Enviar** de formulario también abre otra URL, ya sea que esa URL se abra en la misma pestaña o en una nueva pestaña.
{% endalert %}

## Usar plantillas {#use-templates}

Las plantillas de páginas de inicio son puntos de partida de diseño reutilizables que te ayudan a crear páginas de inicio más rápido. Una plantilla no tiene URL pública y los clientes no pueden visitarla. Para crear una página de inicio en vivo a partir de una plantilla, selecciona la plantilla al crear una nueva página de inicio, personalízala según sea necesario y luego publícala.

Puedes acceder a las plantillas y gestionarlas tanto en el editor de páginas de inicio como desde la página **Landing Page Templates** (**Content** > **Landing Page**). Las plantillas de páginas de inicio requieren un nombre y una descripción opcional.

## Gestionar plantillas {#manage-templates}

Puedes previsualizar, archivar o editar plantillas de páginas de inicio. Puedes duplicar tus propias plantillas de páginas de inicio (ubicadas en **Tus plantillas**), pero no las plantillas de Braze. Al editar una página de inicio, puedes guardar tu página de inicio como plantilla, hacer cambios en la plantilla o eliminar el contenido de la página de inicio.

![Un menú desplegable con opciones para guardar, cambiar y eliminar una página de inicio.]({% image_buster /assets/img/landing_pages/manage-lp-template.png %}){: style="max-width:60%;"}

## Ver análisis {#view-analytics}

Para analizar la eficacia de tu página de inicio, ve a **Mensajería** > **Páginas de inicio** y selecciona una página de inicio que hayas publicado. Aquí puedes hacer seguimiento del número de vistas de página, clics en la página, envíos de página y las tasas de envío de tu página de inicio.

![La sección de análisis de una página de inicio.]({% image_buster /assets/img/landing_pages/analytics.png %})

## Gestionar errores de envío de formulario {#handling-form-submission-errors}

Si un usuario intenta enviar un formulario con datos faltantes o no compatibles, verá un mensaje de error genérico y no podrá enviarlo.

Causas comunes:

- Los campos obligatorios se dejan en blanco
- Se usan caracteres especiales en los campos de texto
- Una casilla de verificación obligatoria no está seleccionada

Los mensajes de error que se muestran a los usuarios no se pueden personalizar. Previsualiza tu página de inicio para confirmar el comportamiento de los campos antes de publicar.