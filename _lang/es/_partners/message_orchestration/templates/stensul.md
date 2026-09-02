---
nav_title: Stensul
article_title: Stensul
alias: /partners/stensul
description: "Este artículo de referencia describe la asociación entre Braze y Stensul, una plataforma de correo electrónico empresarial para crear plantillas de correo electrónico adaptadas a dispositivos móviles en todos los canales."
page_type: partner
search_tag: Partner

---

# Stensul

> [Stensul](https://stensul.com/) proporciona a los especialistas en marketing por correo electrónico herramientas para crear en Stensul mensajes de correo electrónico adaptados a dispositivos móviles y alineados con la marca, antes de enviarlos a Braze en tiempo real para la creación de campañas.

_Esta integración está mantenida por Stensul._

## Sobre la integración {#about-the-integration}

La integración de Braze y Stensul te permite exportar tus correos electrónicos con formato HTML de Stensul y cargarlos como plantillas dentro de Braze.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ------------| ----------- |
| Cuenta Stensul | Se necesita una cuenta Stensul para beneficiarse de esta asociación. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con permisos completos de **Templates**. <br><br> Se puede crear en el panel de Braze desde **Settings** > **API Keys**. |
| Instancia de clúster | Tu [instancia de clúster]({{site.baseurl}}/api/basics/#endpoints) de Braze se corresponde con tu panel de Braze y tu punto de conexión REST or transferencia de estado representacional. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Proporciona tu clave de API REST or transferencia de estado representacional de Braze y tu instancia de clúster a tu equipo de éxito del cliente de Stensul. El equipo se encargará de la integración inicial.

{% alert important %}
Esta es una configuración única y cualquier exportación en el futuro utilizará automáticamente esta clave de API.
{% endalert %}

### Paso 1: Crear correo electrónico en Stensul {#step-1-create-stensul-email}

Crea un correo electrónico en la plataforma Stensul y haz clic en **Complete**.

![Opciones de guardado de Stensul]({% image_buster /assets/img_archive/stensul_save_options.png %})

### Paso 2: Exportar plantilla a Braze {#step-2-export-template-to-braze}
En el nuevo cuadro de diálogo que aparece en la página de finalización, selecciona **Upload to ESP**.

![Opciones de carga de Stensul]({% image_buster /assets/img_archive/stensul_upload_options.png %})

A continuación, introduce el **template name**, el **subject** y el **preheader** de tu correo electrónico y selecciona **Upload**. Recibirás una confirmación de que la carga se ha realizado correctamente y un historial de cargas anteriores del archivo, si procede.

![Carga exitosa de Stensul]({% image_buster /assets/img_archive/stensul_upload_success.png %})

## Uso {#usage}

Encuentra tu plantilla de Stensul cargada en la sección **Templates & Media > Email Templates** de tu cuenta de Braze. Ya puedes utilizar esta plantilla de correo electrónico para empezar a enviar mensajes atractivos a tus clientes.