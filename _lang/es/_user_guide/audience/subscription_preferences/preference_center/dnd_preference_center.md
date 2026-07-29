---
nav_title: Centro de preferencias de correo electrónico con arrastrar y soltar
article_title: Centro de preferencias de correo electrónico con arrastrar y soltar
alias: "/dnd_preference_center/"
description: "Esta página de referencia explica cómo crear un centro de preferencias de correo electrónico con el editor de arrastrar y soltar."
page_order: 2
---

# Crear un centro de preferencias de correo electrónico con arrastrar y soltar {#create-an-email-preference-center-with-drag-and-drop}

> Usando el editor de arrastrar y soltar, puedes crear y personalizar un centro de preferencias para ayudar a gestionar qué usuarios reciben ciertos tipos de comunicación. Puedes tener hasta 100 centros de preferencias por espacio de trabajo.

Puedes administrar los centros de preferencias de arrastrar y soltar existentes desde **Audiencia** > **Centro de preferencias de correo electrónico**:

- Para cambiar el nombre o el contenido de un centro de preferencias, ábrelo desde el panel.
- Los centros de preferencias de arrastrar y soltar no se pueden eliminar desde el panel. Para quitar uno, primero elimina su etiqueta de Liquid de cualquier Campaign de correo electrónico o paso en Canvas, y luego ponte en contacto con [soporte de Braze]({{site.baseurl}}/support_contact).
- Si un centro de preferencias eliminado se utilizó en mensajes enviados anteriormente, dejará de funcionar en esos correos electrónicos entregados.
{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## Paso 1: Crear un centro de preferencias de correo electrónico {#step-1-create-an-email-preference-center}

Crea un centro de preferencias navegando a **Audiencia** > **Centro de preferencias de correo electrónico**. Aquí se mostrará una lista de centros de preferencias personalizados. Selecciona **Crear nuevo** para crear un nuevo centro de preferencias, o selecciona el nombre de uno existente para realizar cambios.

## Paso 2: Nombrar el centro de preferencias de correo electrónico {#step-2-name-the-email-preference-center}

Los nombres de los centros de preferencias solo pueden contener caracteres alfanuméricos, guiones o guiones bajos. El nombre que proporciones determinará la sintaxis de la etiqueta de Liquid generada.

Esta etiqueta de Liquid se puede incluir en cualquier Campaign de correo electrónico saliente o paso en Canvas y dirigirá a los usuarios al centro de preferencias.

## Paso 3: Añadir grupos de suscripción al centro de preferencias {#step-3-add-subscription-groups-to-the-preference-center}

Selecciona **Lanzar editor** para comenzar a diseñar tu centro de preferencias en el editor de arrastrar y soltar.

### Definir los grupos de suscripción disponibles {#define-available-subscription-groups}

Para determinar qué grupos de suscripción deben mostrarse en el centro de preferencias, selecciona el botón **+ Añadir grupos de suscripción** para abrir un modal donde se pueden seleccionar los grupos de suscripción deseados. Después de seleccionarlos, selecciona el botón **Añadir grupos de suscripción** para agregarlos al centro de preferencias.

Puedes configurar aún más los grupos de suscripción seleccionados seleccionando el bloque inteligente y ajustando las propiedades del bloque.

- Ajustar el orden de los grupos de suscripción
- Añadir o quitar grupos de suscripción adicionales
- Incluir descripciones
- Añadir o quitar una casilla de verificación **Suscribirse a todos** que suscribirá al usuario a todos los grupos de suscripción mostrados en este bloque
- Añadir o quitar una casilla de verificación **Cancelar suscripción de todos** que cancelará la suscripción del usuario de todos los grupos de suscripción mostrados en este bloque

El botón **Cancelar suscripción de todos** en la parte inferior de la plantilla no se puede eliminar y [cancelará globalmente la suscripción]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) del usuario para que no reciba ningún mensaje de correo electrónico.

## Paso 4: Personalizar el centro de preferencias usando el editor de arrastrar y soltar {#step-4-customize-the-preference-center-using-the-drag-and-drop-editor}

### Establecer estilos comunes {#set-common-styles}

Puedes establecer ciertos estilos que se apliquen a todos los bloques relevantes en tu centro de preferencias desde la pestaña **Estilos comunes**. Los estilos establecidos en esta sección se utilizan en todas partes de tu mensaje, excepto donde los anules para un bloque específico. Para una experiencia de diseño más sencilla, te recomendamos configurar los estilos a nivel de página antes de personalizar los estilos a nivel de bloque.

![Un ejemplo de configuración de estilos comunes para texto, botones y enlaces.]({% image_buster /assets/img/preference_center/preference_center5.png %}){: style="max-width:45%;"}

{% alert tip %}
Para volver a los estilos comunes, selecciona el botón "X" en las propiedades de bloques individuales. A continuación, selecciona el contenedor del mensaje, el botón "X" del mensaje o el fondo del editor.
{% endalert %}

## Componentes del centro de preferencias de arrastrar y soltar {#drag-and-drop-preference-center-components}

El editor de arrastrar y soltar utiliza dos componentes clave para que la composición del centro de preferencias sea rápida y sencilla: filas y bloques. Todos los bloques deben colocarse en una fila.

{% tabs %}
{% tab Filas %}

Las filas son unidades estructurales que definen la composición horizontal de una sección del mensaje mediante celdas.

![Opción para seleccionar el tipo de fila en tu mensaje.]({% image_buster /assets/img/preference_center/preference_center6.png %}){: style="max-width:45%;"}

Cuando se selecciona una fila, puedes añadir o quitar el número de columnas que necesites desde la sección de personalización de columnas para colocar diferentes elementos de contenido uno al lado del otro. También puedes deslizar para ajustar el tamaño de las columnas existentes.

![Opciones para personalizar las propiedades de tu columna, incluyendo color de fondo, estilo de borde, radio de borde y relleno.]({% image_buster /assets/img/preference_center/preference_center7.png %}){: style="max-width:45%;"}

Como práctica recomendada, da formato a las propiedades de fila y columna antes de dar formato a cualquier bloque dentro de las filas. Puedes ajustar el espaciado y la alineación en muchos lugares, así que empezar desde la base facilita la edición a medida que avanzas.

{% endtab %}
{% tab Bloques %}

Los bloques representan diferentes tipos de contenido que puedes usar en tu mensaje. Arrastra uno dentro de un segmento de fila existente, que se ajustará automáticamente al ancho de la celda.

![Opción para seleccionar bloques, incluyendo título, párrafo, botón, imagen y espaciador.]({% image_buster /assets/img/preference_center/preference_center8.png %}){: style="max-width:45%;"}

Cada bloque tiene su propia configuración, como control granular del relleno. El panel del lado derecho cambia automáticamente a un panel de estilos para el elemento de contenido seleccionado. Para más información, consulta [Bloques del editor (centro de preferencias)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=preference%20center).

Si estás usando el bloque de código personalizado en tu centro de preferencias, es posible que los marcos en línea no se generen en el código personalizado cuando se entregue a tus usuarios.

{% alert note %}
Los Content Blocks con enlaces no se pueden usar en el centro de preferencias de arrastrar y soltar. Los enlaces dentro de los Content Blocks no son clicables.
{% endalert %}

{% endtab %}
{% endtabs %}

## Paso 5: Personalizar tu página de confirmación {#step-5-customize-your-confirmation-page}

A continuación, personaliza la página de confirmación seleccionando **Página de confirmación**. Esta página se mostrará a los usuarios después de actualizar sus preferencias usando el centro de preferencias. Las mismas capacidades de estilo de [Establecer estilos comunes](#set-common-styles) y [Componentes del centro de preferencias de arrastrar y soltar](#drag-and-drop-preference-center-components) también se aplican a esta página.

![Un ejemplo de una página de confirmación para comunicar que las preferencias del usuario han sido actualizadas.]({% image_buster /assets/img/preference_center/preference_center9.png %}){: style="max-width:65%;"}

## Paso 6: Previsualizar y lanzar tu centro de preferencias {#step-6-preview-and-launch-your-preference-center}

Puedes previsualizar tu centro de preferencias seleccionando la pestaña **Vista previa** dentro del editor. La vista previa muestra tanto el centro de preferencias como la página de confirmación.

Sin embargo, la funcionalidad de prueba está deshabilitada. Además, los envíos de prueba de Campaigns o pasos en Canvas que incluyan la etiqueta de Liquid del centro de preferencias no generarán un enlace válido. Esta vista previa no te permite guardar cambios de suscripción, solo muestra cómo se ve la página. Para probar el guardado de preferencias, consulta [Probar centros de preferencias](#testing-preference-centers). Después de editar tu centro de preferencias, puedes cerrar el editor seleccionando el botón **Listo**.

Selecciona **Guardar como borrador** para volver a este centro de preferencias más tarde, o si estás satisfecho, selecciona **Lanzar centro de preferencias**.

Al lanzar el centro de preferencias, se te pedirá que confirmes el nombre, ya que no se puede editar después del lanzamiento. Después de confirmar el nombre, el centro de preferencias se lanzará y estará listo para usar.

## Usar el centro de preferencias {#use-the-preference-center}

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

Para colocar un enlace al centro de preferencias en tus correos electrónicos, copia la etiqueta de Liquid del centro de preferencias deseado seleccionando el icono **Copiar Liquid**.

![La opción Copiar Liquid en la fila de un centro de preferencias.]({% image_buster /assets/img/preference_center/preference_center10.png %}){: style="max-width:75%;"}

Añade la etiqueta de Liquid en el lugar deseado de tu correo electrónico, de manera similar a cómo se insertan las [URL de cancelación de suscripción]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer#adding-a-custom-unsubscribe-link).

{% multi_lang_include preference_center/testing.md %}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Por qué mi centro de preferencias no funciona en un envío de prueba? {#why-doesnt-my-preference-center-work-in-a-test-send}

Los enlaces del centro de preferencias requieren un contexto de envío en vivo. Los envíos de prueba no generan URL válidas del centro de preferencias, y el botón **Guardar preferencias** está deshabilitado si la página se carga. Este es el comportamiento esperado. Para probar de extremo a extremo, lanza una Campaign o un paso en Canvas a un usuario de prueba o a un segmento interno pequeño. Para más detalles, consulta [Probar centros de preferencias](#testing-preference-centers).

## Manejo de errores {#handle-errors}

Si ocurre un error cuando un usuario selecciona **Guardar** en un centro de preferencias, se le presentará el siguiente mensaje de error predeterminado, que no se puede personalizar ni estilizar en el editor. Sin embargo, la localización de los mensajes de error sigue siendo compatible en estas páginas.

![Un error que indica "Hubo un problema al guardar tus preferencias. Por favor, inténtalo de nuevo."]({% image_buster /assets/img/preference_center/preference_center11.png %}){: style="max-width:55%;"}