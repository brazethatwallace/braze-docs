---
nav_title: Bloque Gestionar suscripciones
article_title: Bloque Gestionar suscripciones
description: "Este artículo explica cómo añadir y configurar el bloque de formulario Gestionar suscripciones en una página de destino de Braze, para que los consumidores puedan adherirse voluntariamente a sus grupos de suscripción de correo electrónico, servicio de mensajes cortos o WhatsApp y gestionarlos."
page_order: 5
---

# Bloque Gestionar suscripciones {#manage-subscriptions-block}

> Añade un bloque **Gestionar suscripciones** a una página de destino para que los usuarios puedan ver, adherirse voluntariamente a y actualizar sus grupos de suscripción de correo electrónico, servicio de mensajes cortos o WhatsApp.

El bloque **Gestionar suscripciones** admite dos ejemplos principales:

- **[Gestionar suscripciones existentes](#update-existing-subscriptions):** Comparte la [etiqueta de Liquid]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) de la página de destino en un correo electrónico, servicio de mensajes cortos, WhatsApp u otro mensaje de canal. Cuando un usuario identificado abre la página, el bloque rellena automáticamente la casilla de verificación de cada grupo de suscripción con su estado de suscripción actual, para que pueda revisar y actualizar sus preferencias.
- **[Captar nuevas adhesiones voluntarias](#capture-new-subscribers):** Añade el bloque a una página de destino de generación de leads, junto con un bloque **Email Capture** o **Phone Capture**, para que los nuevos visitantes puedan elegir a qué grupos de suscripción unirse cuando envíen el formulario.

{% alert important %}
Cada bloque **Gestionar suscripciones** es para un solo canal: [correo electrónico]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups), [servicio de mensajes cortos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states) o [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-subscription-states). Para recopilar más de un canal, añade un bloque para cada uno. Para el consentimiento de RCS, utiliza un bloque [Phone Capture]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages) en su lugar.
{% endalert %}

## Requisitos previos {#prerequisites}

| Requisitos | Descripción |
| --- | --- |
| Grupos de suscripción de correo electrónico, servicio de mensajes cortos o WhatsApp | Al menos un [grupo de suscripción de correo electrónico]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups), [grupo de suscripción de servicio de mensajes cortos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states) o [grupo de suscripción de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-subscription-states) para el canal que añadas al bloque. Crea grupos de correo electrónico desde el panel o los [endpoints de grupos de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups). Los grupos de servicio de mensajes cortos se aprovisionan durante la [configuración de servicio de mensajes cortos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#enable-subscription-groups). Los grupos de WhatsApp se crean cuando [integras WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) con tu espacio de trabajo. |
| Permisos de página de destino | Los mismos [permisos]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites) necesarios para crear y editar cualquier página de destino. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Paso 1: Añadir el bloque Gestión de suscripciones {#step-1-add-the-manage-subscriptions-block}

En el editor de páginas de destino de arrastrar y soltar, ve a la sección **Crear** y selecciona **Bloques de formulario**. Arrastra **Gestión de suscripciones** a una fila de tu página; se ajusta automáticamente al ancho de la columna.

El bloque está vacío hasta que le añadas grupos de suscripción. Para mostrar grupos de más de un canal, añade un bloque **Gestión de suscripciones** para cada canal.

## Paso 2: Seleccionar el canal y los grupos de suscripción {#step-2-select-the-channel-and-subscription-groups}

Con el bloque **Manage Subscriptions** seleccionado, selecciona **+ Add subscription groups** en el panel **Block properties** de la derecha. Se abre el modal **Add subscription groups**.

1. En **Select channel**, elige **Email**, **servicio de mensajes cortos** o **WhatsApp**. Cada bloque admite un canal. Si un canal ya tiene un bloque **Manage Subscriptions** en la página, la tarjeta de ese canal estará deshabilitada y etiquetada como **Added**.
2. En **Select subscription groups**, selecciona los grupos que deseas incluir. El encabezado de la lista coincide con el canal (**Email subscription groups**, **servicio de mensajes cortos subscription groups** o **WhatsApp subscription groups**).
3. Selecciona **Add selected**.

Cada grupo de suscripción aparece como su propia casilla de verificación seleccionable en la página de destino.

Si seleccionas **servicio de mensajes cortos** y tu espacio de trabajo aún no tiene grupos de suscripción de servicio de mensajes cortos, el modal muestra **No servicio de mensajes cortos subscription groups yet**. Completa la [configuración de grupos de suscripción de servicio de mensajes cortos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states) y luego regresa al bloque.

Si seleccionas **WhatsApp** y tu espacio de trabajo aún no tiene grupos de suscripción de WhatsApp, el modal muestra **No WhatsApp subscription groups yet**. Completa la [configuración de grupos de suscripción de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-subscription-states) y luego regresa al bloque.

{% alert note %}
El bloque **Manage Subscriptions** solo muestra los grupos que agregas de forma explícita. Agregar un grupo de suscripción al bloque no suscribe automáticamente a los visitantes a ese grupo: un visitante debe marcar la casilla del grupo y enviar el formulario.
{% endalert %}

## Paso 3: Configura los ajustes del bloque {#step-3-configure-the-block-settings}

Usa el panel **Propiedades del bloque** para ajustar cómo se comporta y aparece el bloque.

### Grupos de suscripción {#subscription-groups}

- **Reordenar grupos:** Arrastra un grupo de suscripción por su asa para cambiar el orden en que aparece en el bloque.
- **Añadir o eliminar grupos:** Selecciona **+ Añadir grupos de suscripción** para incluir más grupos, o selecciona el icono de eliminar junto a un grupo para quitarlo del bloque.

### Incluir descripciones {#include-descriptions}

Activa **Incluir descripciones** para mostrar el texto de descripción de cada grupo de suscripción junto a su nombre, dando a los visitantes más contexto sobre a qué se están suscribiendo. Los grupos de correo electrónico pueden incluir una descripción en gestión de suscripciones. Los grupos de servicio de mensajes cortos y WhatsApp en este bloque no muestran texto de descripción.

### Casilla de verificación "Suscribirse a todos" {#subscribe-to-all-checkbox}

Activa el ajuste **Casilla de verificación "Suscribirse a todos"** para añadir una casilla de verificación adicional al bloque. Cuando un visitante la selecciona, se marcan todas las casillas de verificación de los grupos de suscripción en el bloque, lo cual es útil para una adhesión voluntaria rápida a todos los grupos listados.

## Actualizar suscripciones existentes {#update-existing-subscriptions}

Para permitir que los usuarios existentes revisen y actualicen sus suscripciones de correo electrónico, servicio de mensajes cortos o WhatsApp, comparte la página de destino usando su [etiqueta de Liquid]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) en un correo electrónico, servicio de mensajes cortos, WhatsApp, paso en Canvas u otro mensaje. Cuando un usuario abre la página a través de ese enlace, Braze lo identifica y completa previamente de forma automática cada casilla de verificación de grupo de suscripción en el bloque **Manage Subscriptions** para que coincida con su estado de suscripción actual, de manera similar a un [centro de preferencias de correo electrónico]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center).

El usuario puede seleccionar o desmarcar casillas de verificación para actualizar sus suscripciones y luego enviar el formulario para guardar sus cambios.

{% alert note %}
La función de completar previamente el estado de suscripción actual de un usuario en el bloque **Manage Subscriptions** está incluida de forma predeterminada y no requiere el [nivel Landing Pages Pro]({{site.baseurl}}/user_guide/messaging/landing_pages#plan-tiers). Esto difiere del [prellenado basado en Liquid]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages#pre-fill-form-fields) para otros campos de formulario, que requiere Landing Pages Pro.
{% endalert %}

## Capturar nuevos suscriptores {#capture-new-subscribers}

Para recopilar nuevos suscriptores, combina el bloque **Manage Subscriptions** con un campo de captura para ese canal:

- **Correo electrónico:** Agrega un bloque [Email Capture]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages) para que la página capture la dirección de correo electrónico del visitante junto con sus selecciones de grupo de suscripción de correo electrónico.
- **servicio de mensajes cortos o WhatsApp:** Agrega un bloque [Phone Capture]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages) para que la página capture el número de teléfono del visitante junto con sus selecciones de grupo de suscripción de servicio de mensajes cortos o WhatsApp.

Si el visitante no está identificado (por ejemplo, si llega sin una etiqueta de Liquid de landing page), las casillas de verificación comienzan sin seleccionar. Cuando envía el formulario, se suscribe a los grupos de suscripción que haya seleccionado.

## Cosas que debes saber {#things-to-know}

- **Un canal por bloque:** Puedes añadir un bloque **Manage Subscriptions** por canal en una página (uno para correo electrónico, uno para servicio de mensajes cortos y uno para WhatsApp).
- **RCS:** Este bloque no muestra los grupos de suscripción de RCS. Para recopilar el consentimiento para RCS, usa un bloque [Phone Capture]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).
- **Experiencia de confirmación:** Las páginas de destino con bloques de formulario, incluido **Manage Subscriptions**, necesitan una experiencia de confirmación después del envío. [Crea una página de confirmación]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-4-create-a-confirmation-page-optional) y enlázala desde tu botón **Submit**.
- **Referencia de bloques de editor:** Para una referencia completa de cada bloque de página de destino y sus propiedades, consulta [Bloques de editor (páginas de destino)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).