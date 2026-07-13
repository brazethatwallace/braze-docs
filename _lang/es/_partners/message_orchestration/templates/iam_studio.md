---
nav_title: IAM Studio
article_title: IAM Studio
description: "Este artículo de referencia describe la asociación entre Braze e IAM Studio, una plataforma de personalización de mensajes que permite crear experiencias personalizadas y enriquecidas dentro de la aplicación y entregarlas a través de Braze."
alias: /partners/iam_studio/
page_type: partner
search_tag: Partner

---

# IAM Studio

> [IAM Studio](https://www.inappmessage.com) es una plataforma de personalización de mensajes sin código que permite crear experiencias personalizadas y enriquecidas dentro de la aplicación y entregarlas a través de Braze.

_Esta integración está mantenida por IAM Studio._

## Sobre la integración {#about-the-integration}

Con la integración de Braze e IAM Studio, puedes insertar fácilmente plantillas de mensajes dentro de la aplicación personalizables en tus mensajes dentro de la aplicación de Braze, que ofrecen sustitución de imágenes, modificación de texto, configuración de vínculos profundos, atributos personalizados y configuración de eventos. Con IAM Studio, puedes reducir el tiempo de producción de mensajes y dedicar más tiempo a la planificación de contenidos.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de IAM Studio | Se necesita una [cuenta de IAM Studio](https://www.inappmessage.com/register) para beneficiarse de esta asociación. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Ejemplos {#use-cases}

- Fomentar la compra de productos
- Recopilación de información de los usuarios
- Aumentar la inscripción de miembros
- Información sobre la emisión de cupones

## Integración {#integration}

### Paso 1: Elegir una plantilla {#step-1-choose-a-template}

Elige una plantilla de mensaje dentro de la aplicación que quieras utilizar de la galería de plantillas de mensajes dentro de la aplicación.

![La galería de plantillas de IAM Studio muestra diferentes plantillas como "carousel slide modal", "simple icon modal", "modal full image", y más.]({% image_buster /assets/img/iam_studio/iam_template_gallery.png %})

### Paso 2: Personalizar la plantilla {#step-2-customize-the-template}

En primer lugar, personaliza la imagen, el texto y el botón para tu contenido. Asegúrate de conectar **Deeplink** para la imagen y el botón.

{% tabs local %}
{% tab Image %}
![La interfaz de usuario de IAM Studio muestra las opciones para personalizar la imagen. Estas opciones incluyen la imagen, el radio de la imagen y la imagen atenuada.]({% image_buster /assets/img/iam_studio/iam_customize_image.png %})
{% endtab %}
{% tab Text %}
![La interfaz de usuario de IAM Studio muestra las opciones para personalizar el título y el subtítulo del mensaje. Estas opciones incluyen texto, formato y fuente.]({% image_buster /assets/img/iam_studio/iam_customize_text.png %})
{% endtab %}
{% tab Button %}
![La interfaz de usuario de IAM Studio muestra las opciones para personalizar el botón principal, izquierdo y derecho. Estas opciones incluyen el color, el vínculo profundo, el texto y el formato.]({% image_buster /assets/img/iam_studio/iam_customize_button.png %})
{% endtab %}
{% endtabs %}

A continuación, crea tu mensaje personalizado dentro de la aplicación añadiendo fuentes personalizadas y utilizando etiquetas de Liquid. Para habilitar el registro y el seguimiento, selecciona **Log data and track user behavior**.

{% tabs local %}
{% tab Fonts %}
![La interfaz de usuario de IAM Studio muestra las opciones para añadir Liquid. Estas opciones incluyen crear una frase personalizada.]({% image_buster /assets/img/iam_studio/iam_custom_font.png %})
{% endtab %}
{% tab Liquid %}
![La interfaz de usuario de IAM Studio muestra las opciones para personalizar el registro de eventos y atributos. Estas opciones incluyen el registro del comportamiento del usuario.]({% image_buster /assets/img/iam_studio/iam_liquid.png %})
{% endtab %}
{% tab Logging and Tracking %}
![La interfaz de usuario de IAM Studio muestra las opciones para personalizar la fuente. Estas opciones incluyen que el usuario pueda personalizar el estilo de la fuente.]({% image_buster /assets/img/iam_studio/iam_tracking_logging.png  %})
{% endtab %}
{% endtabs %}

### Paso 3: Exportar la plantilla {#step-3-export-the-template}

Una vez finalizada la edición, exporta la plantilla haciendo clic en **Export**. Tras la exportación, se generará el código HTML del mensaje dentro de la aplicación. Copia este código haciendo clic en el botón **Copy code**.

![Diálogo de exportación de IAM Studio con el código HTML del mensaje dentro de la aplicación generado y la acción de copiar código.]({% image_buster /assets/img/iam_studio/export_iam_code.png %}){: style="max-width:45%;"}

### Paso 4: Utilizar el código en Braze {#step-4-use-code-in-braze}

Ve a Braze y, en tu mensaje dentro de la aplicación, pega el código personalizado en el cuadro de **HTML Input**. Asegúrate de probar tu mensaje para comprobar que se muestra correctamente.

![Editor de Campaign de mensajes dentro de la aplicación de Braze con el HTML de IAM Studio pegado en el cuadro HTML Input.]({% image_buster /assets/img/iam_studio/braze_campaign_editor.png %}){: style="max-width:85%;"}