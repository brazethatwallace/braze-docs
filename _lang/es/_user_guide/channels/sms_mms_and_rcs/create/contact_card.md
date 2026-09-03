---
nav_title: Tarjetas de contacto
article_title: Tarjetas de contacto
page_order: 3
description: "Este artículo de referencia explica cómo crear una tarjeta de contacto para incluir en tus mensajes MMS y SMS."
page_type: reference
alias: /mms_contact_cards/
channel:
  - MMS

---

# Tarjetas de contacto {#contact-cards}

> Las tarjetas de contacto (a veces conocidas como vCard o archivos de contacto virtual (VCF)) son un formato de archivo estandarizado para enviar información empresarial y de contacto que puedes importar fácilmente en libretas de direcciones o agendas de contactos.

{% alert note %}
El envío de una tarjeta de contacto se cobra como un MMS. Revisa tu volumen esperado de MMS y el uso de créditos de mensajes o de acción cuando crees tarjetas de contacto, y confirma los costos en tu [página de facturación]({{site.baseurl}}/user_guide/administer/global/billing) de Braze.
{% endalert %}

Las tarjetas de contacto se pueden crear [programáticamente](https://www.twilio.com/blog/send-vcard-twilio-sms) y cargar en la [biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) de Braze, o crearse a través de nuestro generador de tarjetas de contacto integrado. A estas tarjetas se les pueden asignar propiedades comunes como el nombre de tu empresa, número de teléfono, dirección, correo electrónico y una foto pequeña. Para empezar a crear tarjetas de contacto, primero asegúrate de tener configurado MMS en Braze.

## Generador de tarjetas de contacto {#contact-card-generator}

### Paso 1: Asignar nombre {#step-1-assign-name}

Las tarjetas de contacto se pueden crear desde el creador de mensajes SMS y MMS. Selecciona la pestaña **Contact Card Generator** para comenzar.

A continuación, se te pedirá que introduzcas el nombre o apodo de tu empresa. Este es el nombre que tus usuarios verán cuando guarden la tarjeta. Se aplica un límite de 20 caracteres para asegurar que el usuario pueda ver el nombre completo de tu empresa o alias en sus contactos y aplicación de mensajería.

![La pestaña del generador de tarjetas de contacto.]({% image_buster /assets/img/sms/contact_card1.png %}){: style="max-width:60%" }

### Paso 2: Asignar número de teléfono {#step-2-assign-phone-number}

Selecciona el grupo de suscripción y el número de teléfono deseado de las opciones desplegables disponibles. Este número aparecerá en tu tarjeta de contacto y estará disponible en el teléfono del usuario para enviar mensajes de texto una vez guardado.

Ten en cuenta que los códigos alfanuméricos no son compatibles con la mensajería bidireccional y no son compatibles con las tarjetas de contacto.

### Paso 3: Campos opcionales {#step-3-optional-fields}

![Campos opcionales para el generador de tarjetas de contacto.]({% image_buster /assets/img/sms/contact_card2.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

#### Cargar foto de contacto de la tarjeta {#upload-contact-card-contact-photo}

Puedes cargar una foto de contacto opcional para tu tarjeta de contacto. Recomendamos una imagen JPEG o PNG de 240 x 240&nbsp;px. Cualquier imagen de alta resolución que se cargue se redimensionará a 240 x 240&nbsp;px para asegurar la capacidad de entrega del mensaje, ya que los mensajes MMS de más de 5&nbsp;MB pueden fallar.

{% alert note %}
La imagen cargada aparece en la tarjeta de contacto cuando el destinatario la abre; el [campo **Full Name**](#add-more-information) determina lo que aparece en la miniatura del chat de mensajes.
{% endalert %}

#### Añadir más información {#add-more-information}

Otros campos te permiten insertar tu nombre, subtítulo, dirección y otra información de contacto que tu usuario pueda querer tener disponible.

El campo **Full Name** determina las iniciales que aparecen en la miniatura del chat de mensajes. Cuando el campo está marcado como opcional y se deja en blanco, los destinatarios ven un círculo blanco en lugar de las iniciales.

### Paso 4: Guardar tu tarjeta de contacto {#step-4-saving-your-contact-card}

Una vez que hayas introducido todos los campos necesarios, selecciona **Generate Contact Card** y se adjuntará automáticamente a tu campaña o Canvas. Desde aquí, puedes añadir un mensaje, probar tu tarjeta de contacto y lanzar tu campaña o Canvas.

La tarjeta de contacto también se guardará en la [biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) para reutilizarla fácilmente en futuras campañas y Canvas.

## Añadir una tarjeta de contacto existente {#adding-an-existing-contact-card}

Para añadir una tarjeta de contacto existente, crea una campaña o Canvas y selecciona el grupo de suscripción deseado. A continuación, aparecerá una opción **Add Media** en la ventana del creador de mensajes. Aquí puedes cargar un archivo de tarjeta de contacto existente o localizar uno a través de la biblioteca de medios.