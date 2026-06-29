---
nav_title: Editor de arrastrar y soltar
article_title: Crear un mensaje dentro de la aplicación en el editor de arrastrar y soltar
alias: /iam_drag_and_drop/
page_order: 1
description: "Este artículo de referencia cubre la creación de un mensaje dentro de la aplicación con el editor de arrastrar y soltar, los requisitos previos, los detalles creativos y más."
local_redirect: #set-message-level-styles, #add-a-custom-font, #drag-and-drop-in-app-message-components, #creative-details
  set-message-level-styles: '/docs/user_guide/channels/in_app_messages/customize/style_settings#message-level-styles'
  add-a-custom-font: '/docs/user_guide/channels/in_app_messages/customize/style_settings#custom-fonts'
  drag-and-drop-in-app-message-components: '/docs/user_guide/channels/in_app_messages/customize/style_settings#message-components'
  creative-details: '/docs/user_guide/channels/in_app_messages/customize/style_settings#creative-details'
---

# Crear un mensaje dentro de la aplicación con arrastrar y soltar {#create-an-in-app-message-with-drag-and-drop}

> Con el editor de arrastrar y soltar, puedes crear mensajes dentro de la aplicación completamente personalizados en Campaigns o Canvas usando la experiencia de edición de arrastrar y soltar. Para más información sobre los bloques de construcción disponibles en el editor, consulta [Bloques de editor]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages).


{% multi_lang_include video.html id="j94omgo73o" align="right" source="wistia" %}

Si quieres usar tus plantillas HTML personalizadas existentes o plantillas creadas por terceros, deben recrearse en el editor de arrastrar y soltar.

¿No tienes claro si tu mensaje dentro de la aplicación debe enviarse usando una campaña o un [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/)? Las campañas son mejores para envíos de mensajería únicos y dirigidos, mientras que los Canvas son mejores para recorridos de usuario de varios pasos. Después de seleccionar dónde construir tu mensaje, veamos los pasos para crear un mensaje dentro de la aplicación con arrastrar y soltar.

## Requisitos previos {#prerequisites}

### Requisitos del SDK {#sdk-requirements}

| Versión mínima del SDK                                                       | Versión recomendada del SDK                                                   |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}{:/} | {::nomarkdown}{% sdk_min_versions swift:6.5.0 android:26.0.0 web:4.8.1 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos del SDK" }

{% details Más información sobre los SDK mínimos %}

Los mensajes creados con el editor de arrastrar y soltar solo pueden enviarse a usuarios con las versiones mínimas del SDK (consulta la tabla anterior). Si un usuario no ha actualizado su aplicación (es decir, está en una versión anterior del SDK), no recibirá el mensaje dentro de la aplicación.

Para aprovechar todas las características disponibles en el editor de arrastrar y soltar, actualiza tus SDK a las versiones recomendadas. Esto te permite aprovechar las siguientes características adicionales:

- Enlaces de texto que no descartan el mensaje
- Acción de botón para solicitar push primer

A continuación se describen los requisitos mínimos individuales del SDK para estas características:

| Enlaces de texto*                                                   | Solicitar push primer                                                         |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:6.2.0 android:26.0.0 %}{:/} | {::nomarkdown}{% sdk_min_versions web:4.8.1 swift:6.5.0 android:26.0.0 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos del SDK" }

*Si incluyes un enlace en tu mensaje dentro de la aplicación que redirige a una URL y el usuario final no está en las versiones mínimas del SDK especificadas, al seleccionar el enlace se cerrará el mensaje y el usuario no podrá volver al mensaje para enviar el formulario.

{% enddetails %}

### Requisitos previos adicionales {#additional-prerequisites}

- Para el SDK web, la opción de inicialización [`allowUserSuppliedJavascript`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) debe establecerse en `true`. La opción `enableHtmlInAppMessages` también permitirá que estos mensajes funcionen, pero está obsoleta y debe actualizarse a `allowUserSuppliedJavascript`.
- Si estás usando Google Tag Manager, debes habilitar "Allow HTML In-App Messages" en la configuración de GTM.

## Paso 1: Crear un mensaje dentro de la aplicación {#step-1-create-an-in-app-message}

Crea un nuevo mensaje dentro de la aplicación o paso en Canvas, luego selecciona **Drag-And-Drop Editor** como tu experiencia de edición.

## Paso 2: Seleccionar tu plantilla {#step-2-select-your-template}

Después de seleccionar el editor de arrastrar y soltar como tu experiencia de edición, puedes elegir:

- Empezar con una plantilla modal en blanco
- Usar una plantilla de mensaje dentro de la aplicación de arrastrar y soltar de Braze
- Seleccionar una plantilla guardada de mensaje dentro de la aplicación de arrastrar y soltar

Selecciona **Build message** para comenzar a diseñar tu mensaje dentro de la aplicación en el editor de arrastrar y soltar.

![La sección de plantillas de Braze donde puedes elegir una plantilla básica, de imagen de fondo, de captura de número de teléfono o en blanco.]({% image_buster /assets/img_archive/dnd_iam_select_template.png %})

También puedes acceder a todas las plantillas desde la sección **Templates** del dashboard.

## Paso 3: Agregar páginas adicionales (opcional) {#multi-page}

Agregar páginas a tu mensaje dentro de la aplicación te permite guiar a los usuarios a través de un flujo secuencial, como un flujo de incorporación o un recorrido de bienvenida. Puedes administrar las páginas desde la sección **Pages** de la pestaña **Build**.

![Un mensaje dentro de la aplicación para una empresa de salud compuesto por tres páginas.]({% image_buster /assets/img_archive/dnd_iam_mockup.png %})

{% tabs %}
{% tab Agregar páginas %}

Los mensajes dentro de la aplicación comienzan con una página de forma predeterminada. Para agregar una nueva página:

1. Selecciona **+ Add page**.
2. Selecciona de la lista de plantillas personalizadas o proporcionadas por Braze.
3. Dale a la página un nombre significativo. Esto te ayudará cuando conectes las páginas entre sí.

{% alert tip %}
Puedes agregar hasta 10 páginas por mensaje dentro de la aplicación.
{% endalert %}

Para duplicar una página existente:

1. Pasa el cursor sobre la página en la lista y selecciona <i class="fas fa-ellipsis-vertical"></i> **More options**.
2. Selecciona **Duplicate**.
3. Dale a la página un nombre significativo. Esto te ayudará cuando conectes las páginas entre sí.

{% endtab %}
{% tab Eliminar o renombrar páginas %}

Para eliminar o renombrar una página:

1. Pasa el cursor sobre la página en la lista y selecciona <i class="fas fa-ellipsis-vertical"></i> **More options**.
2. Selecciona **Rename** o **Delete**.

{% endtab %}
{% endtabs %}

### Paso 3a: Conectar páginas entre sí {#step-3a-connect-pages-together}

Los mensajes dentro de la aplicación de varias páginas son secuenciales, lo que significa que los usuarios interactúan con el mensaje tocando o haciendo clic para pasar a la siguiente página del flujo.

Para conectar páginas entre sí:

1. Selecciona tu página de inicio.
2. Selecciona un elemento de botón o imagen en el canvas.
3. Establece **On-click behavior** en **Go to page**.
4. Selecciona la página a la que quieres enlazar desde la página de inicio.
5. Continúa hasta que todas las páginas estén enlazadas.

![Un usuario está editando el botón de acción principal para ir a la página 2 del mensaje dentro de la aplicación.]({% image_buster/assets/img_archive/dnd_iam_multipage.gif %})

Si una página no está enlazada a ninguna otra página, el mensaje no puede lanzarse.

{% alert note %}
Los usuarios pueden seleccionar el botón de cierre X para salir del mensaje en cualquier momento. Este botón no puede eliminarse.
{% endalert %}

## Paso 4: Construir y diseñar tu mensaje dentro de la aplicación {#step-4-build-and-design-your-in-app-message}

Aquí es donde tu mensaje puede lucirse, vestido con el estilo distintivo de tu marca. Usando una combinación de bloques de editor y configuraciones de estilo, puedes personalizar y diseñar tu mensaje dentro de la aplicación.

- Para una lista de los bloques de editor disponibles y sus propiedades, consulta [Bloques de editor]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages).
- Para ayuda personalizando la apariencia de tu mensaje, consulta [Configuración de estilo]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/).
- Para mejores prácticas al crear mensajes de derecha a izquierda, consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/).

## Paso 5: Probar tu mensaje dentro de la aplicación {#step-5-test-your-in-app-message}

La sección **Preview & Test** te permite previsualizar tus mensajes dentro de la aplicación en diferentes dispositivos y enviar un mensaje de prueba a tu dispositivo. Aquí puedes asegurarte de que los detalles estén alineados en todas tus plataformas para tu campaña de mensaje dentro de la aplicación de arrastrar y soltar.

Es importante siempre probar tus mensajes dentro de la aplicación antes de enviar tus campañas para ayudarte a visualizar cómo se verá tu mensaje final desde la perspectiva de tu usuario.

### Previsualizar el mensaje como un usuario {#preview-message-as-a-user}

{% alert warning %}
Para enviar una prueba a grupos de prueba de contenido o a usuarios individuales, push debe estar habilitado en tus dispositivos de prueba antes de enviar.
{% endalert %}

Puedes previsualizar mensajes desde la pestaña **Preview & Test**, como si fueras un usuario. Puedes seleccionar un usuario específico, un usuario aleatorio o crear un usuario personalizado:

- **Random User:** Braze seleccionará aleatoriamente un usuario de la base de datos y previsualizará el mensaje dentro de la aplicación basándose en sus atributos o información de eventos.
- **Select User:** Puedes seleccionar un usuario específico basándote en su dirección de correo electrónico o `external_id`. El mensaje dentro de la aplicación se previsualizará basándose en los atributos e información de eventos de ese usuario.
- **Custom User:** Puedes personalizar un usuario. Braze ofrecerá campos de entrada para todos los atributos y eventos disponibles. Ingresa cualquier información que desees ver en la vista previa del correo electrónico.

### Lista de verificación de pruebas {#test-checklist}

Considera las siguientes preguntas mientras pruebas tu mensaje dentro de la aplicación:

- ¿Has probado el mensaje en diferentes dispositivos?
- ¿Las imágenes y los medios se muestran y funcionan como se espera?
- ¿Liquid funciona como se espera? ¿Has considerado un valor de atributo predeterminado en caso de que Liquid no devuelva información?
- ¿Tu texto es claro, conciso y correcto?
- ¿Tus botones dirigen al usuario a donde deben ir?

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Por qué los clics en el cuerpo no aparecen en mi página de análisis? {#why-are-body-clicks-not-appearing-on-my-analytics-page}

Los clics en el cuerpo no se recopilan automáticamente para los mensajes dentro de la aplicación creados con el editor de arrastrar y soltar. Para más detalles, consulta los registros de cambios del SDK para [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) y [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100).

### ¿Puedo segmentar basándome en los clics de botones? {#can-i-segment-based-on-button-clicks}

Sí, puedes segmentar basándote en los clics de botones para hasta dos botones en tu mensaje. Para hacerlo, establece el **Identifier for Reporting** de tus botones en "0" y "1", que corresponderán a los filtros de segmentación "Clicked in-app message button 1" y "Clicked in-app message button 2" respectivamente.

![El campo "Identifier for Reporting" con un valor de "0".]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}

### ¿Puedo personalizar mi mensaje dentro de la aplicación usando HTML o JavaScript personalizado, o transferir mensajes HTML existentes al editor? {#can-i-customize-my-in-app-message-using-custom-html-or-javascript-or-transfer-existing-html-messages-into-the-editor}

No puedes transferir directamente mensajes HTML existentes al editor, pero puedes insertar HTML sin procesar, CSS y JavaScript en un bloque de código personalizado. Puedes usar bloques de código personalizado para incrustar videos de terceros y Liquid avanzado, como contenido conectado o sentencias condicionales.

### ¿Cómo puedo crear un mensaje dentro de la aplicación de deslizamiento hacia arriba? {#how-can-i-create-a-slideup-in-app-message}

Actualmente, el editor está limitado solo a mensajes modales y de pantalla completa. Puedes cambiar entre tipos de visualización en la sección **Message container** del panel **Message styles**.

### ¿Puedo guardar mi mensaje dentro de la aplicación como plantilla después de construirlo dentro de mi campaña o Canvas? {#can-i-save-my-in-app-message-as-a-template-after-i-build-it-within-my-campaign-or-canvas}

Sí. Para cualquier mensaje dentro de la aplicación que quieras reutilizar en una futura campaña o paso en Canvas, puedes guardarlo como plantilla personalizada usando el botón **Save as template**, disponible después de salir del editor. Antes de poder guardarlo como plantilla, primero debes lanzar la campaña O guardarlo como borrador.

![Una vista previa de un mensaje dentro de la aplicación para un recorrido de producto.]({% image_buster /assets/img_archive/dnd_iam_save_as_template.png %})

También puedes crear y guardar plantillas de mensajes dentro de la aplicación navegando a **Content** > **In-App Message Templates**.