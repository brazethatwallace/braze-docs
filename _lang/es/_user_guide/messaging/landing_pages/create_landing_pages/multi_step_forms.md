---
nav_title: Formularios de varios pasos
article_title: Formularios de varios pasos en páginas de destino
page_order: 2
page_type: reference
description: "Aprende a crear un formulario de varios pasos en una página de destino de Braze, a gestionar los pasos en el editor de arrastrar y soltar y a personalizar el paso de confirmación integrado."
---

# Formularios de varios pasos en páginas de destino {#multi-step-landing-page-forms}

> Divide un formulario largo de página de destino en varios pasos, cada uno con sus propios campos, para que los usuarios avancen por tu formulario un paso a la vez. Cada formulario de varios pasos incluye un paso de confirmación bloqueado, de modo que los usuarios siempre ven una confirmación después de enviar.

## Requisitos previos {#prerequisites}

Para acceder al creador de páginas de destino, necesitas [ciertos permisos]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites). Si no tienes acceso, pide ayuda a tu administrador de Braze.

También deberías estar familiarizado con los [bloques de formulario de páginas de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-3-customize-the-page).

## Cómo funcionan los formularios de varios pasos {#how-multi-step-forms-work}

Para crear un formulario de varios pasos, añade una fila de **Formulario** desde la sección **Diseño** del panel **Crear**. La fila de **Formulario** incluye botones de acción integrados y compatibilidad con varios pasos, por lo que no necesitas montar la estructura de la fila tú mismo.

Solo puedes añadir una fila de **Formulario** por página de destino. Cuando la arrastras a tu página, comienza con un solo paso y un paso de confirmación bloqueado que se ejecuta tras el envío.

{% alert note %}
Dado que la fila de **Formulario** gestiona su propia navegación de varios pasos, todos tus pasos se encuentran dentro de esa única fila en una sola página. Esto es diferente del enfoque estándar de crear un formulario de un solo paso y vincular su botón **Enviar** a una página de destino de confirmación independiente. Para más información, consulta [Paso 4: Crear una página de confirmación]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-4-create-a-confirmation-page-optional).
{% endalert %}

![Un formulario de página de destino de varios pasos en el creador de páginas de destino.]({% image_buster /assets/img/landing_pages/multi_step_form.png %})

## Añadir un formulario de varios pasos {#add-a-multi-step-form}

1. En el editor de la página de destino, ve al panel **Crear** y selecciona **Diseño**.
2. Arrastra la fila **Formulario** a tu página.
3. Con la fila **Formulario** seleccionada, usa la sección **Pasos** en el panel de propiedades del lado derecho para construir tu formulario:
   - Añade [bloques de formulario]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-3-customize-the-page) (como **Captura de correo electrónico**, **Captura de teléfono**, **Campo de entrada**, **Desplegable**, **Casilla de verificación** o **Grupo de casillas de verificación**) al **Paso 1**.
   - Selecciona **Añadir paso** para crear pasos adicionales y añade bloques de formulario a cada uno.

Por ejemplo, un formulario de tres pasos podría solicitar un nombre en el **Paso 1**, un número de teléfono en el **Paso 2** y luego llegar al paso de **Confirmación** para agradecer al usuario por enviar el formulario.

## Navega entre pasos durante la edición {#navigate-between-steps-while-editing}

Muévete entre los pasos en el editor de dos formas:

| Método | Cómo hacerlo |
|--------|--------|
| Navegador de pasos | En el canvas, usa el control **Paso X de Y** para moverte al paso anterior o siguiente. |
| Panel de pasos | Selecciona la fila **Form**, luego usa la sección **Steps** en el panel de propiedades del lado derecho para ir directamente a un paso, incluido el paso **Confirmation**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Navega entre pasos durante la edición" }

## Gestionar pasos {#manage-steps}

Usa la sección **Steps** en el panel de propiedades de la fila **Form** para añadir, eliminar y reordenar pasos:

| Acción | Cómo hacerlo |
|--------|--------|
| Añadir un paso | Selecciona **Add step**. Los nuevos pasos se añaden después de los pasos existentes y antes del paso **Confirmation**. |
| Eliminar un paso | Selecciona el icono de papelera junto al paso que deseas eliminar.<br><br>Ten en cuenta que el paso **Confirmation** no tiene icono de papelera y no se puede eliminar ni reordenar. Siempre se ejecuta en último lugar, después de que un usuario complete los pasos anteriores. |
| Reordenar pasos | Usa el controlador de arrastre junto a un paso para cambiar su orden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gestionar pasos" }

## Personalizar el paso de confirmación {#customize-the-confirmation-step}

Cada formulario de varios pasos incluye un paso de **Confirmación** que aparece en **Después del envío** en la sección **Pasos**. Este paso está bloqueado para que no pueda eliminarse, lo que significa que los usuarios siempre ven una experiencia de confirmación después de enviar tu formulario.

Aunque el paso de **Confirmación** no puede eliminarse, puedes personalizarlo como cualquier otro paso: selecciónalo en la sección **Pasos** y luego añade y da estilo a los bloques para crear tu mensaje de confirmación.

## Personalizar el estilo del bloque de formulario {#style-the-form-block}

Con la fila **Formulario** seleccionada, usa la sección **Estilos** en el panel **Formulario de varios pasos** para personalizar el contenedor del formulario:

| Control | Descripción |
|---|---|
| Imagen de fondo | Añade una imagen detrás del formulario. También puedes ajustar el tamaño, la posición y la configuración de repetición de la imagen. |
| Color de fondo | Establece el color de fondo del contenedor del formulario. |
| Estilo del borde | Elige un borde sólido, discontinuo o punteado para el contenedor del formulario. |
| Color del borde | Establece el color del borde del contenedor del formulario. |
| Radio del borde | Redondea las esquinas del contenedor del formulario. |
| Relleno | Ajusta el espacio entre el borde del contenedor del formulario y su contenido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Controles de estilo del formulario de varios pasos" }

Estos estilos se aplican al contenedor del formulario en todos los pasos, incluido el paso de **Confirmación**.

## Rastrear datos de formularios completados parcialmente {#track-data-from-partially-completed-forms}

Si un usuario abandona tu formulario antes de llegar al paso de **Confirmación**, Braze aún guarda los datos de cualquier paso que haya completado en su perfil de usuario. El evento **Submitted a Landing Page form** no se registra hasta que el usuario completa todos los pasos y llega al paso de **Confirmación**.

{% alert note %}
La [reorientación y la entrega por desencadenante]({{site.baseurl}}/user_guide/messaging/landing_pages/retargeting_users) dependen del evento **Submitted a Landing Page form**. Un usuario que envía algunos pasos pero no todos se guarda en su perfil, pero no se incluye en ese evento, aunque sus datos parciales hayan sido capturados.
{% endalert %}

Esto difiere de los [cuestionarios de páginas de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys), donde un usuario que no llega al paso final se rastrea como un envío parcial.

## Limitaciones y consideraciones {#limitations-and-considerations}

- Una página de destino admite una sola fila de **Formulario**, por lo que todos tus pasos y tu paso de confirmación se encuentran en esa única fila.
- Puedes añadir hasta 10 pasos de recopilación de datos. El paso de **Confirmación** no cuenta para ese límite.
- Cada paso incluye un botón predeterminado con la acción de clic configurada para ir al siguiente paso. Esa acción valida y guarda las entradas del paso actual; en el último paso de recopilación de datos, también registra el evento **Submitted a Landing Page form** y avanza a **Confirmación**. Si un paso no está conectado, añade un comportamiento de clic para que el botón vaya al siguiente paso. Para más información, consulta [Botón]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=landing%20pages) en Bloques de editor.
- No necesitas crear ni enlazar a una segunda página de destino para que sirva como tu experiencia de confirmación, porque el paso de **Confirmación** está integrado en la fila de **Formulario**.
- Si no ves la fila de **Formulario** en **Diseño**, ponte en contacto con tu director de cuentas de Braze.