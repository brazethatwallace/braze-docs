---
nav_title: Vista previa del enlace SMS dinámico
article_title: Vista previa del enlace SMS dinámico
description: "Este artículo de referencia describe cómo activar y utilizar la característica de vista previa de enlaces SMS de Movable Ink."
page_type: partner
search_tag: Partner
---

# Vista previa del enlace SMS dinámico {#dynamic-sms-link-preview}

> Con la vista previa dinámica de enlaces SMS de Movable Ink, puedes aprovechar la inmersión de los MMS al mismo coste que los SMS. Esto te permite utilizar Braze y Movable Ink para entregar experiencias de mensajería enriquecida rentables y personalizadas.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Cuenta de Movable Ink | Se necesita una cuenta de Movable Ink para beneficiarse de esta asociación. |
| Origen de datos | Necesitas conectar un origen de datos a Movable Ink. Esto puede hacerse mediante CSV, importación del sitio web o API. |
| Capacidad de envío de MMS | Confirma que estás configurado para MMS a través de Braze.
| [Acortamiento de enlaces]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening) | Confirma que el acortamiento de enlaces está activado. |
| Tarjeta de contacto | Tu marca (el remitente) debe estar guardada como contacto en el teléfono del usuario para que la vista previa del enlace funcione con iOS. Esto puede hacerse con una tarjeta de contacto u otro método. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Sigue los pasos que se indican a continuación para enviar enlaces SMS dinámicos para los sistemas operativos iOS y Android.

### iOS

{% alert important %}
Para permitir imágenes de vista previa de enlaces en iOS, los usuarios deben añadir tu marca (el remitente) como contacto.
{% endalert %}

#### Paso 1: Crea una campaña de tarjetas de contacto {#step-1-create-a-contact-card-campaign}

Después de que los usuarios guarden tu marca como contacto, ya sea a través de una [tarjeta de contacto]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card) o de otro método, podrán ver las indicaciones de **Tap to Load Preview** y los enlaces de Movable Ink.

![Un usuario de iOS toca para cargar la vista previa del enlace][1]{: style="max-width:30%;"}

#### Paso 2: Envía enlaces de Movable Ink {#step-2-send-movable-ink-links}

1. Crea una campaña SMS en Movable Ink y genera tu URL de click-through.
2. En el panel de Braze, ve a **Campaigns** y configura una nueva campaña SMS/MMS desde el desplegable **Crear Campaign**.
3. En el creador de la campaña SMS:
    - Configura tu grupo de suscripción.
    - Introduce tu mensaje.
    - Añade tu enlace de Movable Ink **en último lugar**, después del resto del texto del cuerpo del mensaje. <br><br>![Creador de la campaña SMS con el enlace de Movable Ink al final del mensaje][2]{: style="max-width:50%;"}

{% alert tip %}
Echa un vistazo a [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) para repasar la personalización con Liquid.
{% endalert %}

{: start="4"}
4. Ya estás listo para probar y lanzar tu campaña de vista previa de enlaces SMS dinámicos.

![Pantalla de prueba y lanzamiento de la campaña SMS dinámica][3]{: style="max-width:70%;"}

Cuando los usuarios carguen la vista previa del enlace, se mostrará una imagen personalizada con la posibilidad de enlazar con tu sitio web, aplicación o página de inicio.

![Ejemplo de imagen personalizada renderizada tras cargar la vista previa][4]{: style="max-width:30%;"}

### Android (dispositivos Google y Samsung) {#android-google-and-samsung-devices}

Los usuarios de Android no necesitan guardar tu marca como contacto para recibir vistas previas de enlaces SMS dinámicos. Sin embargo, sigue siendo recomendable para que el dispositivo pueda cargar automáticamente las vistas previas de los enlaces.

![Vista previa de enlace cargada automáticamente en un dispositivo Android][5]{: style="max-width:30%;"}

Los usuarios que no hayan guardado tu marca como contacto y hayan activado las vistas previas automáticas tendrán que seleccionar **Tap to load preview** para cargar la imagen de vista previa.

![Indicación para tocar y cargar la vista previa en Android][6]{: style="max-width:30%;"}

## Consideraciones {#considerations}

- Incluye solo un enlace de vista previa en tu mensaje. No se generará contenido con varios enlaces en el cuerpo de tu SMS.
- No incluyas ningún carácter después de tu enlace de vista previa o la experiencia podría romperse.


[1]: {% image_buster /assets/img/movable_ink/ios_link.png %}
[2]: {% image_buster /assets/img/movable_ink/ios_message.png %}
[3]: {% image_buster /assets/img/movable_ink/ios_test_launch.png %}
[4]: {% image_buster /assets/img/movable_ink/ios_example.png %}
[5]: {% image_buster /assets/img/movable_ink/android_automatic.png %}
[6]: {% image_buster /assets/img/movable_ink/android_tap.png %}