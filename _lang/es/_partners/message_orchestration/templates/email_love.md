---
nav_title: "Email Love"
article_title: "Email Love"
description: "Aprende a integrar Braze con Email Love, un complemento de Figma que te permite diseñar y exportar correos electrónicos HTML receptivos y accesibles directamente desde Figma."
alias: /partners/email_love/
page_type: partner
search_tag: Partner

---

# Email Love

> [Email Love](https://emaillove.com/) es un complemento de Figma que te permite diseñar y exportar correos electrónicos HTML receptivos y accesibles directamente desde Figma. La característica Exportar a Braze de Email Love utiliza la API de Braze para cargar fácilmente tus plantillas de correo electrónico en Braze.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|------------------------|------------------------------------------------------------------|
| **Cuenta de Email Love** | Se necesita una cuenta de Email Love para beneficiarse de esta asociación. |
| **Clave de API REST de Braze** | Una clave de API REST de Braze con el permiso completo de `Templates` habilitado. Puede crearse en el dashboard de Braze desde **Settings** > **API Keys**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Utilizar Email Love con Braze {#using-email-love-with-braze}

### Paso 1: Ejecuta el complemento {#step-1-run-the-plugin}

Para diseñar tu plantilla de correo electrónico, primero tendrás que cargar el complemento. Para obtener instrucciones más detalladas, consulta la documentación de Email Love para [cargar tu correo electrónico en Braze](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm).

### Paso 2: Crea tu primer marco {#step-2-create-your-first-frame}

En el complemento, selecciona el botón **[+ No Template Selected]** para crear un nuevo marco para el diseño de tu correo electrónico.

### Paso 3: Diseña la plantilla con los componentes preconstruidos de Email Love {#step-3-design-the-template-with-email-loves-pre-built-components}

Selecciona el marco que creaste y empieza a añadir componentes (encabezados, bloques de contenido, CTA y pies de página) de la biblioteca de **Assets** del complemento para estructurar tu correo electrónico.

![Componentes preconstruidos de Email Love.]({% image_buster /assets/img/email_love/emaillove1_content.png %})

### Paso 4: Personaliza los componentes {#step-4-customize-the-components}

Modifica los componentes utilizando las herramientas de Figma para ajustar el texto, las imágenes, los colores y los elementos de diseño para alinear el diseño de la plantilla con tu marca. Si añades un componente de pie de página, al exportar se incluirá automáticamente un enlace de Braze para cancelar suscripción.

![Personaliza los componentes en Figma.]({% image_buster /assets/img/email_love/emaillove2_components.png %})

### Paso 5: Exporta tu plantilla de correo electrónico a Braze {#step-5-export-your-email-template-to-braze}

1. Cuando hayas terminado, selecciona el marco que quieras exportar. Ten en cuenta que tendrás que utilizar un pie de página de Email Love que contenga un enlace para cancelar suscripción para que la exportación funcione.
2. Selecciona el botón **Export** en el complemento y selecciona **Braze** en el menú desplegable.
3. Copia y pega tu clave de API en la casilla **Braze API Key** dentro del complemento de Email Love en Figma.
4. Selecciona el botón **Set API Key**.
5. Selecciona **Change Instance ID** y, a continuación, selecciona el ID de tu instancia de Braze.

![Exportar una plantilla a Braze desde el complemento de Email Love.]({% image_buster /assets/img/email_love/emaillove3_exportbraze.png %}){: style="max-width:50%;"}

### Paso 6: Edita tu correo electrónico en Braze {#step-6-edit-your-email-in-braze}

En Braze, ve a **Templates** > **Edit Templates** > **Edit Message**. Dentro del editor de plantillas, puedes editar el HTML de tu correo electrónico o utilizar el **Rich Text editor** en la pestaña **Classic**.

## Soporte y solución de problemas {#support-and-troubleshooting}

Para obtener instrucciones más detalladas, consulta la documentación de Email Love sobre la [exportación de un diseño de correo electrónico](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm). Para obtener más ayuda, ponte en contacto con el equipo de soporte de Email Love.