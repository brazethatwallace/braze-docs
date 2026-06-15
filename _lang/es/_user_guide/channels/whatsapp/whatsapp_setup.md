---
nav_title: "Configuración"
article_title: "Configuración de WhatsApp"
alias: /partners/whatsapp/
description: "Este artículo explica cómo configurar el canal de WhatsApp en Braze, incluidos los requisitos previos y los próximos pasos sugeridos."
page_type: partner
search_tag: Partner
page_order: 0
channel:
  - WhatsApp
search_rank: 2
---

# Configuración de WhatsApp {#whatsapp-setup}

> [WhatsApp](https://www.whatsapp.com/) Business messaging es una popular plataforma de mensajería entre pares utilizada en todo el mundo que ofrece mensajería basada en conversaciones para empresas.

## Requisitos previos {#prerequisites}

Revisa lo siguiente antes de proceder con la integración:

- **Política de adhesión voluntaria:** WhatsApp requiere que las empresas cuenten con la adhesión voluntaria de los clientes para recibir mensajes.
- **Reglas de contenido de WhatsApp:** WhatsApp tiene varias [reglas de contenido](https://www.whatsapp.com/legal/commerce-policy?l=en) que deben cumplirse.
- **Cumplimiento:** Cumple con toda la documentación aplicable de Braze y Meta, así como con cualquier [política de Meta](https://www.whatsapp.com/legal/?lang=en) aplicable.
- **Límites de conversación de 24 horas:** Después de que una empresa envíe un mensaje inicial con plantilla o un usuario envíe un mensaje, se abrirá una ventana de 24 horas en la que ambas partes pueden intercambiar mensajes.
- **Inicio de conversación:** Los usuarios pueden iniciar una conversación en cualquier momento. Una empresa solo puede iniciar una conversación a través de una plantilla de mensaje aprobada.
<br><br>

| Requisito | Descripción |
| --- | --- |
| Cuenta de Meta Business Manager | Se requiere una cuenta de Meta Business para aprovechar este canal de mensajería. |
| Cuenta de WhatsApp Business | Se requiere una cuenta de WhatsApp Business para aprovechar este canal de mensajería. |
| Número de teléfono de WhatsApp | Debes adquirir un número de teléfono que cumpla con los requisitos de WhatsApp para la [API en la nube](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) o la [API local](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers) para el uso del canal de mensajería. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Conectar WhatsApp Messenger a Braze {#step-1-connect-whatsapp-messenger-to-braze}

En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y busca **WhatsApp**.

En la página del socio de WhatsApp, selecciona **Begin Integration**.

![Página del socio de WhatsApp con un botón para iniciar la integración.]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:70%;"}

En la ventana abierta, selecciona **Next** hasta que aparezca el botón **Begin Integration**. Selecciona el botón para iniciar el proceso de integración.

![Instrucciones para conectar Braze a WhatsApp.]({% image_buster /assets/img/whatsapp/instructions.png %}){: style="max-width:50%;"}

### Paso 2: Configuración de WhatsApp {#step-2-whatsapp-setup}

A continuación, el flujo de trabajo de configuración de Braze te guiará. Para un recorrido paso a paso, consulta [Registro integrado de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup/).

Dentro de este flujo, podrás:
1. Crear o seleccionar tus cuentas de Meta y WhatsApp Business. Asegúrate de revisar las [directrices de nombre para mostrar de WhatsApp](https://www.facebook.com/business/help/757569725593362). <br><br>Es probable que ya tengas al menos una cuenta de Meta Business existente en tu empresa. Si es así, selecciona aquella en la que deseas que resida tu cuenta de WhatsApp Business. Los permisos de usuario y la verificación empresarial para WhatsApp se controlarán de forma centralizada en tu cuenta de Meta Business.<br><br>
2. Crear tu perfil de WhatsApp Business.
3. Verificar tu número de WhatsApp Business.<br><br>

Una vez completada la configuración, se creará un grupo de suscripción de WhatsApp dedicado para tus usuarios.

### Paso 3: Crear plantillas de WhatsApp {#step-3-create-whatsapp-templates}

Solo las plantillas de mensajes de WhatsApp aprobadas pueden utilizarse para iniciar conversaciones con los clientes. Las plantillas de WhatsApp se pueden crear en el [Meta Business Manager](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343). Para ver una lista de las funciones de mensajería de WhatsApp compatibles con Braze, consulta [Funciones de WhatsApp compatibles]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/#supported-whatsapp-features).

1. **Navega al [administrador de plantillas](https://business.facebook.com/wa/manage/message-templates)**<br>
En el Meta Business Manager, en **Account Tools**, selecciona **Message Templates**.
A continuación, selecciona **Create Templates**.<br><br>![Administrador de WhatsApp con una lista de plantillas de mensajes.]({% image_buster /assets/img/whatsapp/whatsapp2.png %}){: style="max-width:100%;"}<br><br>
2. **Configuración del mensaje**<br>
En el nuevo compositor de plantillas de mensajes, selecciona la categoría de tu mensaje, asigna un nombre a tu plantilla y elige los idiomas que deseas admitir. Puedes eliminar o agregar más idiomas después.<br><br>
	Las categorías de plantillas de mensajes disponibles incluyen las siguientes:
	- Marketing: envía ofertas promocionales, anuncios de productos y más para aumentar el conocimiento y la interacción
	- Utilidad: envía actualizaciones de cuenta, actualizaciones de pedidos, alertas y más para compartir información importante
	- Autenticación: envía códigos que permiten a tus clientes acceder a sus cuentas<br><br>
	![Compositor de plantillas de mensajes con categorías para marketing, utilidad y autenticación.]({% image_buster /assets/img/whatsapp/whatsapp3.png %}){: style="max-width:100%;"}<br><br>
3. **Editar plantilla**<br>
A continuación, crea tu plantilla de mensaje. <br><br>Puedes proporcionar un encabezado de texto o multimedia, el cuerpo del texto, un pie de mensaje y botones. Ten en cuenta que los encabezados de video y documento no están disponibles actualmente, y los encabezados deben ser de tipo texto o imagen. Cualquier contenido multimedia que agregues sirve como ejemplo para el proceso de revisión y **no se incluye** en el mensaje de la plantilla. El contenido multimedia debe agregarse en Braze. Se mostrará una vista previa de tu mensaje en un panel. <br><br>Aunque Meta no admite Liquid, puedes incluir variables en la plantilla que luego se pueden reemplazar en Braze por variables de Liquid. Selecciona el botón **+ Add variable** para hacerlo.<br><br>![Compositor de plantillas.]({% image_buster /assets/img/whatsapp/whatsapp4.png %}){: style="max-width:100%;"}

Una vez que hayas completado tu plantilla, presiona **Submit**.

#### Tiempo de aprobación de plantillas {#template-approval-time}

Puedes verificar el estado de aprobación de tu plantilla de mensaje en la página **Message Template** del Meta Business Manager, o al crear una campaña o Canvas en Braze. Además, puedes recibir notificaciones por correo electrónico del equipo de WhatsApp según tus permisos de notificación.

{% alert note %}
Las plantillas aprobadas se pueden utilizar en tantas campañas y Canvas como desees. También se pueden enviar a tantos usuarios con adhesión voluntaria como desees. Esto es válido a menos que la calidad de la plantilla disminuya.
{% endalert %}

### Paso 4: Crear una campaña de WhatsApp {#step-4-create-a-whatsapp-campaign}

Una vez que las plantillas de WhatsApp hayan sido aprobadas, puedes ir al dashboard para crear una [campaña o Canvas de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/).

{% alert note %}
Después de que se cree tu cuenta de WhatsApp Business, Meta determinará tu límite de mensajería inicial. Para obtener más información, consulta [rendimiento]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup/10dlc/#throughput).
{% endalert %}

## Próximos pasos {#next-steps}

Después de completar la integración, te recomendamos completar los dos siguientes procesos de Meta:
- [Verificación empresarial](https://www.facebook.com/business/help/2058515294227817?id=180505742745347)
	- Es posible que ya tengas la verificación empresarial si has utilizado un Meta Business Manager existente.
- [Cuenta empresarial oficial](https://www.facebook.com/business/help/604726921052590?ref=search_new_0)

También te recomendamos leer sobre los [números de teléfono de los usuarios]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers/) y agregar a cualquier usuario que necesite acceso para crear [plantillas en tu organización](https://www.facebook.com/business/help/2169003770027706?id=2190812977867143).

### Almacenamiento local de la API en la nube de WhatsApp {#whatsapp-cloud-api-local-storage}

Braze es compatible con el [almacenamiento local de la API en la nube](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/local-storage?content_id=ka6F9gESPqhQpm5) de WhatsApp. Para habilitarlo, ponte en contacto con tu administrador de soporte al cliente de Braze.