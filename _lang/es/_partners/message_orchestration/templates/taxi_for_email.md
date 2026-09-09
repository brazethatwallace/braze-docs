---
nav_title: Taxi for Email for Email
article_title: Taxi for Email for Email
alias: /partners/taxi_for_email
description: "Este artículo de referencia describe la asociación entre Braze y Taxi for Email for Email, una herramienta de marketing por correo electrónico en línea que permite a los clientes de Braze crear plantillas de correo electrónico inteligentes utilizando su interfaz de arrastrar y soltar y una sintaxis sencilla pero potente."
page_type: partner
search_tag: Partner

---

# Taxi for Email for Email

> [Taxi for Email for Email](http://taxiforemail.com/) es una herramienta de marketing por correo electrónico en línea que ofrece un editor visual de correo electrónico intuitivo con función de arrastrar y soltar. Taxi for Email anima a los equipos a colaborar fácilmente en campañas de correo electrónico, permitiendo a redactores y editores el acceso y los recursos que necesitan para crear correos electrónicos, todo ello sin código.

_Esta integración la mantiene Taxi for Email for Email._

## Sobre la integración {#about-the-integration}

La integración de Braze y Taxi for Email utiliza la sencilla pero potente sintaxis de Taxi for Email para crear y exportar plantillas de correo electrónico inteligentes a Braze.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ------------| ----------- |
| Cuenta Taxi for Email for Email | Se necesita una cuenta de Taxi for Email for Email para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos completos de **Plantillas**. <br><br> Puede crearse en el panel de Braze desde **Configuración** > **Claves de API**. |
| Punto de conexión de Braze | [Tu punto de conexión de Braze]({{site.baseurl}}/api/basics/#endpoints) se corresponde con la URL de tu panel de Braze.<br><br> Por ejemplo, si la URL de tu panel es `https://dashboard-03.braze.com`, tu punto de conexión será `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Crear una plantilla de correo electrónico en Taxi for Email {#step-1-create-a-taxi-email-template}

Crea una plantilla de Taxi for Email en la plataforma Taxi for Email. Una vez creada la plantilla, ve a la **Configuración de tu organización** y selecciona la pestaña **ESP Connectors**.

### Paso 2: Crear el conector de Braze {#step-2-create-braze-connector}

1. En el cuadro de diálogo que aparece, selecciona el botón **Add New** y, a continuación, selecciona **Braze** en el menú desplegable.
2. Selecciona **Braze** para editar la configuración del conector de Braze.
3. Introduce tu punto de conexión de Braze y tu clave de API de Braze.

El campo de tu conector cambiará de color una vez que se hayan proporcionado los datos con los permisos correctos. Si este campo no cambia, comprueba que tus campos se ajustan a los requisitos indicados.

## Uso {#usage}

Encuentra tu plantilla de Taxi for Email cargada en la sección **Plantillas y medios > Plantillas de correo electrónico** de tu cuenta de Braze. Ya puedes utilizar esta plantilla de correo electrónico para empezar a enviar mensajes atractivos a tus clientes.