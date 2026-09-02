---
nav_title: EmailShepherd
article_title: EmailShepherd
alias: /partners/emailshepherd/
description: "Este artículo de referencia describe la integración entre Braze y EmailShepherd, una plataforma de creación de correo electrónico basada en agentes que se construye sobre tu sistema de diseño de correo electrónico y publica correos aprobados en tu espacio de trabajo de Braze."
page_type: partner
search_tag: Partner
---

# EmailShepherd

> [EmailShepherd](https://emailshepherd.com/) es una plataforma de creación de correo electrónico basada en agentes que se construye sobre tu sistema de diseño de correo electrónico y permite a todo tu equipo de marketing —y a los agentes de IA— producir correos electrónicos alineados con la marca y listos para producción, sin cuellos de botella. La integración con Braze publica los correos aprobados directamente en tu espacio de trabajo de Braze, para que los especialistas en marketing puedan escalar la producción de correo electrónico en Braze sin sacrificar la consistencia de marca.

_Esta integración es mantenida por EmailShepherd._

## Acerca de la integración {#about-the-integration}

La integración de Braze y EmailShepherd te permite crear correos electrónicos basados en tu sistema de diseño de correo electrónico en EmailShepherd y exportarlos a Braze como plantillas de correo electrónico. Tu equipo crea y aprueba los correos en EmailShepherd y luego publica plantillas listas para producción en Braze sin necesidad de transferir HTML manualmente.

## Requisitos previos {#prerequisites}

Los siguientes elementos son necesarios para utilizar esta integración:

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de EmailShepherd | Se requiere una cuenta de EmailShepherd para utilizar esta integración. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con permisos completos de "Templates". <br><br>Se puede crear en el dashboard de Braze desde **Configuración** > **Claves de API**. |
| Instancia de Braze | Tu [instancia de clúster]({{site.baseurl}}/api/basics/#endpoints) de Braze se alinea con tu dashboard de Braze y tu punto de conexión REST or transferencia de estado representacional. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

EmailShepherd está diseñado para equipos que quieren escalar la producción de correo electrónico manteniendo cada envío alineado con la marca. Es una buena opción si quieres:

- **Garantizar la consistencia de marca a escala:** Tu sistema de diseño de correo electrónico define los componentes, colores y diseños aprobados. Cada correo publicado en Braze está alineado con la marca por construcción.
- **Abrir la producción de correo electrónico a todo tu equipo:** Un constructor de arrastrar y soltar basado en tu sistema de diseño de correo electrónico permite a cualquier persona crear correos listos para producción.
- **Usar la creación de campañas basada en agentes:** Los agentes de IA trabajan dentro de las directrices de tu sistema de diseño de correo electrónico, por lo que las campañas que producen están alineadas con la marca y listas para enviar.

## Integración {#integration}

### Paso 1: Crear tu conector de EmailShepherd {#step-1-create-your-emailshepherd-connector}

{% alert note %}
Esta es una configuración única. Después de crear el conector, EmailShepherd utiliza estas credenciales para todas las exportaciones futuras a Braze.
{% endalert %}

1. En EmailShepherd, ve a **Connectors** > **Add connector**.
2. Selecciona **Braze** e introduce un nombre para el conector.
3. Introduce tu clave de API y selecciona tu instancia de Braze.
4. Selecciona **Create Connector** para guardar la conexión.

![Formulario de conector de EmailShepherd con campos de instancia de Braze y clave de API]({% image_buster /assets/img_archive/emailshepherd_step1.png %}){: style="max-width:60%;"}

### Paso 2: Exportar un correo electrónico desde EmailShepherd {#step-2-export-an-email-from-emailshepherd}

En EmailShepherd, localiza el correo electrónico que deseas exportar a Braze. Asegúrate de que esté publicado y luego selecciona **Export**.

![Editor de correo electrónico de EmailShepherd con la acción de exportar]({% image_buster /assets/img_archive/emailshepherd_step2.png %}){: style="max-width:60%;"}

### Paso 3: Configurar y publicar en Braze {#step-3-configure-and-publish-to-braze}

1. En la página de exportación, selecciona tu conector de Braze en **Connectors** (por ejemplo, **Braze Prod**).
2. Elige una opción de **Image hosting** para las imágenes de tu biblioteca de imágenes de EmailShepherd. Las imágenes introducidas por URL no se modifican durante la exportación.
3. Confirma el **Locale** e introduce un **Template name** para el correo electrónico en Braze.
4. Selecciona **Start export**.

![Página de exportación de EmailShepherd con campos de conector de Braze, alojamiento de imágenes y nombre de plantilla]({% image_buster /assets/img_archive/emailshepherd_step3.png %}){: style="max-width:60%;"}

## Usar la integración {#use-the-integration}

En Braze, encuentra tus correos electrónicos exportados en **Content** > **Email**. Puedes usar estas plantillas en tus Campaigns y Canvas de Braze.

## Soporte {#support}

Para más información sobre las integraciones de EmailShepherd, consulta la [documentación de EmailShepherd](https://emailshepherd.com/docs/).