---
nav_title: Stripo
article_title: Stripo
alias: /partners/stripo
description: "Este artículo de referencia describe la asociación entre Braze y Stripo, un creador de plantillas de correo electrónico de arrastrar y soltar para crear sofisticados correos electrónicos con elementos interactivos."
page_type: partner
search_tag: Partner

---

# Stripo

> [Stripo](https://stripo.email/) es un creador de plantillas de correo electrónico de arrastrar y soltar para diseñar correos electrónicos receptivos con elementos interactivos. Los usuarios de Stripo también pueden editar en HTML y decidir qué elementos mostrar u ocultar en los distintos dispositivos a través del editor de Stripo.

_Esta integración está mantenida por Stripo._

## Sobre la integración {#about-the-integration}

La integración de Braze y Stripo te permite exportar tus correos electrónicos personalizados de Stripo y cargarlos como plantillas dentro de Braze.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ------------| ----------- |
| Cuenta Stripo | Se requiere una cuenta Stripo para beneficiarse de esta asociación. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con permisos completos de **Templates**. <br><br> Puede crearse en el panel de Braze desde **Settings** > **API Keys**. |
| Instancia de clúster | Tu [instancia de clúster]({{site.baseurl}}/api/basics/#endpoints) de Braze se alinea con tu panel de Braze y tu punto de conexión REST or transferencia de estado representacional.  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Crear correo electrónico Stripo {#step-1-create-stripo-email}

Crea un correo electrónico Stripo en la plataforma Stripo y haz clic en **Export**.

![Exportación de Stripo]({% image_buster /assets/img_archive/stripo_export.png %})

### Paso 2: Exportar plantilla a Braze {#step-2-export-template-to-braze}

En el cuadro de diálogo que aparece, selecciona **Braze** como método de exportación.

A continuación, introduce el **nombre de tu cuenta** (como el nombre del espacio de trabajo), la **clave de API** y tu **instancia de clúster**.

![Formulario de Stripo]({% image_buster /assets/img_archive/stripo_form.png %})

{% alert important %}
Se trata de una configuración única, y cualquier exportación en el futuro utilizará automáticamente esta clave de API.
{% endalert %}

## Uso {#usage}

Encuentra tu plantilla Stripo cargada en la sección **Templates & Media > Email Templates** de tu cuenta de Braze. Ya puedes utilizar esta plantilla de correo electrónico para empezar a enviar mensajes atractivos a tus clientes.