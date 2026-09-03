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

Para crear un formulario de varios pasos, añade una fila **Form** desde la sección **Layout** del panel **Build**. La fila **Form** incluye botones de acción integrados y compatibilidad con varios pasos, por lo que no necesitas ensamblar la estructura de la fila tú mismo.

Solo puedes añadir una fila **Form** por página de destino. Cuando la arrastras a tu página, comienza con un solo paso y un paso de confirmación bloqueado que se ejecuta después del envío.

{% alert note %}
Dado que la fila **Form** gestiona su propia navegación de varios pasos, todos tus pasos se encuentran dentro de esa única fila en una sola página. Esto es diferente del enfoque estándar de crear un formulario de un solo paso y vincular su botón **Submit** a una página de destino de confirmación independiente. Para más información, consulta [Paso 4: Crear una página de confirmación]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-4-create-a-confirmation-page-optional).
{% endalert %}

![Un formulario de varios pasos en una página de destino dentro del creador de páginas de destino.]({% image_buster /assets/img/landing_pages/multi_step_form.png %})

## Añadir un formulario de varios pasos {#add-a-multi-step-form}

1. En el editor de páginas de destino, ve al panel **Build** y selecciona **Layout**.
2. Arrastra la fila **Form** a tu página.
3. Con la fila **Form** seleccionada, usa la sección **Steps** en el panel de propiedades del lado derecho para construir tu formulario:
   - Añade [bloques de formulario]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-3-customize-the-page) (como **Email Capture**, **Phone Capture**, **Input Field**, **Dropdown**, **Checkbox** o **Checkbox Group**) al **Step 1**.
   - Selecciona **Add step** para crear pasos adicionales y añade bloques de formulario a cada uno.

Por ejemplo, un formulario de tres pasos podría pedir un nombre en el **Step 1**, un número de teléfono en el **Step 2** y luego llegar al paso de **Confirmation** para agradecer al usuario por enviar.

## Navegar entre pasos durante la edición {#navigate-between-steps-while-editing}

Muévete entre pasos en el editor de dos formas:

| Método | Cómo hacerlo |
|--------|--------|
| Navegador de pasos | En el lienzo, usa el control **Step X of Y** para ir al paso anterior o siguiente. |
| Panel de pasos | Selecciona la fila **Form** y luego usa la sección **Steps** en el panel de propiedades del lado derecho para ir directamente a un paso, incluido el paso de **Confirmation**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Navegar entre pasos durante la edición" }

## Gestionar pasos {#manage-steps}

Usa la sección **Steps** en el panel de propiedades de la fila **Form** para añadir, eliminar y reordenar pasos:

| Acción | Cómo hacerlo |
|--------|--------|
| Añadir un paso | Selecciona **Add step**. Los nuevos pasos se añaden después de los pasos existentes y antes del paso de **Confirmation**. |
| Eliminar un paso | Selecciona el icono de papelera junto al paso que deseas eliminar.<br><br>Ten en cuenta que el paso de **Confirmation** no tiene un icono de papelera y no se puede eliminar ni reordenar. Siempre se ejecuta en último lugar, después de que un usuario completa los pasos anteriores. |
| Reordenar pasos | Usa el controlador de arrastre junto a un paso para cambiar su orden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gestionar pasos" }

## Personalizar el paso de confirmación {#customize-the-confirmation-step}

Cada formulario de varios pasos incluye un paso de **Confirmation** que aparece en **After submission** en la sección **Steps**. Este paso está bloqueado para que no pueda eliminarse, lo que significa que los usuarios siempre ven una experiencia de confirmación después de enviar tu formulario.

Aunque el paso de **Confirmation** no se puede eliminar, puedes personalizarlo como cualquier otro paso: selecciónalo en la sección **Steps** y luego añade y estiliza bloques para construir tu mensaje de confirmación.

## Rastrear datos de formularios parcialmente completados {#track-data-from-partially-completed-forms}

Si un usuario abandona tu formulario antes de llegar al paso de **Confirmation**, Braze aún guarda los datos de los pasos que completó en su perfil de usuario. El evento **Submitted a Landing Page form** no se registra hasta que el usuario completa todos los pasos y llega al paso de **Confirmation**.

{% alert note %}
La [reorientación y la entrega desencadenada]({{site.baseurl}}/user_guide/messaging/landing_pages/retargeting_users) dependen del evento **Submitted a Landing Page form**. Un usuario que envía algunos pasos pero no todos se guarda en su perfil, pero no se incluye en ese evento, aunque sus datos parciales hayan sido capturados.
{% endalert %}

Esto difiere de los [cuestionarios de páginas de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys), donde un usuario que no llega al paso final se rastrea como un envío parcial.

## Limitaciones y consideraciones {#limitations-and-considerations}

- Una página de destino admite una sola fila **Form**, por lo que todos tus pasos y tu paso de confirmación se encuentran en esa única fila.
- Puedes añadir hasta 10 pasos de recopilación de datos. El paso de **Confirmation** no cuenta para ese límite.
- Cada paso incluye un botón predeterminado con la acción de clic configurada para ir al siguiente paso. Esa acción valida y guarda las entradas del paso actual; en el último paso de recopilación de datos, también registra el evento **Submitted a Landing Page form** y avanza a **Confirmation**. Si un paso no está conectado, añade un comportamiento de clic para que el botón vaya al siguiente paso. Para más información, consulta [Button]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=landing%20pages) en bloques de editor.
- No necesitas crear ni vincular a una segunda página de destino para servir como tu experiencia de confirmación, porque el paso de **Confirmation** está integrado en la fila **Form**.
- Si no ves la fila **Form** en **Layout**, contacta a tu director de cuentas de Braze.