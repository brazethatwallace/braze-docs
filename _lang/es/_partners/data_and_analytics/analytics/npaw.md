---
nav_title: NPAW
article_title: NPAW
alias: /partners/npaw/
description: "Este artículo de referencia describe la asociación entre Braze y NPAW, una plataforma inteligente de análisis de datos que proporciona información accionable a los principales profesionales de los medios de comunicación en línea."
page_type: partner
search_tag: Partner
hidden: true

---

# NPAW

> [NPAW](https://nicepeopleatwork.com/), también conocida como _Nice People at Work_, es una plataforma inteligente de análisis de datos que proporciona información accionable a los principales profesionales de los medios de comunicación en línea. Con la línea de productos YOUBORA de NPAW, los clientes de Braze ahora pueden aprovechar una IA predictiva y robusta para comprender mejor el comportamiento del cliente e impulsar la interacción en todas las plataformas.

# Requisitos previos {#prerequisites}

| Requisito | Origin | Descripción |
| --------------|------|-------------|
| Clave de API de YOUBORA | [Configuración de YOUBORA](https://youbora.nicepeopleatwork.com/users/login) | Una clave de API generada al registrarse el usuario y que puede encontrarse en **Settings** |
| ID | [Configuración de Braze](https://dashboard.braze.com/sign_in) | YOUBORA te da la opción de vincular el software a Braze a través de un ***Braze ID***, un ***ID de usuario externo*** o un ***ID de usuario*** |
| Punto de conexión | [Configuración de Braze](https://dashboard.braze.com/sign_in) | Un punto de conexión de URL totalmente personalizable y configurable a través de tu panel de Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prerequisites" }

# Integración de análisis {#analytics-integration}

## Acceso a la página de integraciones {#accessing-the-integrations-page}

Tras iniciar sesión en tu cuenta de la línea de productos YOUBORA, ve a la página de integraciones seleccionando la opción **Integrations** en el menú desplegable de la cuenta.

![Menú desplegable de NPAW]({% image_buster /assets/img/npaw_dropdown.png %})

## Configuración de la integración {#configuring-your-integration}

Una vez que hayas accedido a la página de integración, desplázate hacia abajo hasta que
veas la opción de integración de **Braze**. Tras hacer clic en ella, se expandirá y mostrará una serie de parámetros obligatorios que debes completar:

![Integración de NPAW]({% image_buster /assets/img/npaw_integration.png %})

Rellena los datos con la información adecuada reunida en la sección de requisitos previos, donde:
* **Connector Name** es una cadena **alfanumérica** que se utilizará para referirse a esta integración en el futuro. Este valor puede ser cualquier cosa que desees, siempre que contenga **solamente** letras y números.
* **User ID** es el ID elegido previamente para vincular tu software YOUBORA con tu cuenta de Braze. Por ejemplo, si decides realizar el enlace a través de tu **Braze ID**, selecciona **Braze ID** en el menú desplegable para asignar el valor al campo adecuado.
* **API Key** es tu clave de API de la línea de productos YOUBORA, que encontraste anteriormente en la sección **API** dentro de **Settings**.
* **Endpoint** es el punto de conexión de URL personalizable previamente configurado en tu panel de Braze.

Una vez rellenados todos los campos, simplemente haz clic en el botón **Connect** para establecer la conexión y guardar los cambios realizados.

## Uso de la integración de NPAW {#using-your-npaw-integration}

Una vez que hayas terminado de configurar tu integración con Braze, ve al producto **Users** y selecciona el **Sample Manager** dentro del **Sections Manager**.

Después de crear una muestra en el **Sample Manager**, podrás hacer clic en el icono de tres puntos de la derecha para enviar todos los usuarios de tu muestra a Braze.

![Administrador de muestras de NPAW]({% image_buster /assets/img/npaw_sample_manager.png %})

Ahora, una vez enviados tus usuarios a Braze, puedes actuar y centrar tus campañas en segmentos de usuarios para volver a captar a los usuarios inactivos, ponerte en contacto con tus usuarios más fieles o realizar cualquier acción en cualquier segmento de usuarios.