---
nav_title: Dyspatch
article_title: Dyspatch
alias: /partners/dyspatch
description: "Este artículo de referencia describe la asociación entre Braze y Dyspatch, un creador de correo electrónico de arrastrar y soltar que te permite crear correos electrónicos atractivos, responsivos y con interacción sin necesidad de escribir código."
page_type: partner
search_tag: Partner

---

# Dyspatch

> [Dyspatch](https://www.dyspatch.io) ofrece un intuitivo creador de correo electrónico de arrastrar y soltar que se utiliza para crear correos electrónicos atractivos, responsivos y con interacción sin necesidad de escribir código. Colabora con tu equipo para crear y aprobar correos electrónicos dentro de Dyspatch y luego expórtalos a Braze, ¡todo en unos pocos pasos!

_Esta integración está mantenida por Dyspatch._

## Sobre la integración {#about-the-integration}

La integración de Dyspatch y Braze te permite simplificar el ciclo de vida de creación de correo electrónico exportando plantillas de correo electrónico de Dyspatch directamente a Braze.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Dyspatch | Para beneficiarte de esta asociación, es necesario disponer de una [cuenta de Dyspatch](https://www.dyspatch.io/login/) con un [rol de propietario o administrador](https://docs.dyspatch.io/administration/dyspatch_roles/). |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos completos de **Templates**. <br><br> Puede crearse en el panel de Braze desde **Settings** > **API Keys**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integración {#integration}

La integración de Braze y Dyspatch te permite exportar plantillas de correo electrónico de Dyspatch directamente a tu Biblioteca de medios de Braze o descargar tu plantilla y cargarla manualmente.

### Paso 1: Crear la integración de Braze {#step-1-create-the-braze-integration}

En el portal de administración de Dyspatch, abre el menú desplegable de tu nombre de usuario y selecciona **Integrations**. Crea una nueva integración, selecciona **Braze** e introduce tu clave de API de Braze.

En el campo **Localize Exports By**, puedes elegir cómo deseas gestionar la localización. Este campo te permite [localizar tus plantillas de correo electrónico](https://docs.dyspatch.io/localization/localizing_a_template/) y exportarlas a Braze para enviar fácilmente correos personalizados por idioma o configuración regional.

![Plantilla de exportación de Dyspatch]({% image_buster /assets/img/dyspatch/dyspatch_integration_create.png %}){: style="max-width:50%;"}

### Paso 2: Exportar plantilla a Braze {#step-2-export-template-to-braze}

Después de completar un correo electrónico en Dyspatch, para enviar tu plantilla a Braze, visualiza la plantilla de correo electrónico publicada y haz clic en **Download/Export** y luego en **Export to Integration**.

Si deseas cargar tu plantilla manualmente, visualiza la plantilla de correo electrónico publicada y haz clic en **Download/Export** y, a continuación, en **Download HTML**. Después, en la sección **Templates & Media > Email Templates** de tu cuenta de Braze, selecciona **From File** para cargar tu plantilla.

![Plantilla de exportación de Dyspatch]({% image_buster /assets/img/dyspatch/dyspatch_export.gif %})

{% alert important %}
No selecciones **Inline CSS** en la sección **Sending Info** de ninguna plantilla de correo electrónico de Dyspatch en Braze. Dyspatch se encarga de ello asegurándose de que tus correos electrónicos sean sólidos, responsivos y estén listos para ser enviados.
{% endalert %}

### Uso {#usage}

Encuentra tu plantilla de Dyspatch cargada en la sección **Templates & Media > Email Templates** de tu cuenta de Braze. Ya puedes utilizar esta plantilla de correo electrónico para empezar a enviar mensajes atractivos a tus clientes.