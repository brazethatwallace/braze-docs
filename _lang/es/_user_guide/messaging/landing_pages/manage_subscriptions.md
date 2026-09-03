---
nav_title: Bloque Gestionar suscripciones
article_title: Bloque Gestionar suscripciones
description: "Este artículo explica cómo añadir y configurar el bloque de formulario Gestionar suscripciones en una página de destino de Braze, para que los consumidores puedan adherirse voluntariamente a sus grupos de suscripción de correo electrónico y gestionarlos."
page_order: 5
---

# Bloque Gestionar suscripciones {#manage-subscriptions-block}

> Añade un bloque **Gestionar suscripciones** a una página de destino para que los usuarios puedan ver, adherirse voluntariamente a y actualizar sus grupos de suscripción de correo electrónico.

El bloque **Gestionar suscripciones** admite dos ejemplos principales:

- **[Gestionar suscripciones existentes](#update-existing-subscriptions):** Comparte la [etiqueta de Liquid]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) de la página de destino en un correo electrónico u otro mensaje de canal. Cuando un usuario identificado abre la página, el bloque rellena automáticamente la casilla de verificación de cada grupo de suscripción con su estado de suscripción actual, para que pueda revisar y actualizar sus preferencias.
- **[Captar nuevas adhesiones voluntarias](#capture-new-subscribers):** Añade el bloque a una página de destino de generación de leads, junto con un bloque **Email Capture**, para que los nuevos visitantes puedan elegir a qué grupos de suscripción unirse cuando envíen el formulario.

{% alert important %}
El bloque **Gestionar suscripciones** solo admite [grupos de suscripción de correo electrónico]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups). No admite grupos de suscripción de SMS, RCS ni WhatsApp.
{% endalert %}

## Requisitos previos {#prerequisites}

| Requisitos | Descripción |
| --- | --- |
| Grupos de suscripción de correo electrónico | Al menos un [grupo de suscripción de correo electrónico]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups), [creado desde el panel]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#create-a-subscription-group) o mediante los [endpoints de grupo de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups). |
| Permisos de landing page | Los mismos [permisos]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites) necesarios para crear y editar cualquier landing page. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Paso 1: Agregar el bloque Gestionar suscripciones {#step-1-add-the-manage-subscriptions-block}

En el editor de páginas de destino de arrastrar y soltar, ve a la sección **Crear** y selecciona **Bloques de formulario**. Arrastra **Gestionar suscripciones** a una fila de tu página; se ajusta automáticamente al ancho de la columna.

El bloque está vacío hasta que le agregues grupos de suscripción.

## Paso 2: Selecciona los grupos de suscripción {#step-2-select-the-subscription-groups}

Con el bloque **Manage Subscriptions** seleccionado, selecciona **+ Add subscription groups** en el panel **Block properties** del lado derecho. Esto abre una lista de los [grupos de suscripción de correo electrónico]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups) disponibles en tu espacio de trabajo.

Selecciona la casilla junto a cada grupo de suscripción que quieras incluir y, a continuación, confirma tu selección para añadirlos al bloque. Cada grupo de suscripción aparece como su propia casilla seleccionable en la página de destino.

{% alert note %}
El bloque **Manage Subscriptions** solo muestra los grupos que añades de forma explícita. Añadir un grupo de suscripción al bloque no suscribe automáticamente a los visitantes a él: el visitante debe seleccionar la casilla del grupo y enviar el formulario.
{% endalert %}

## Paso 3: Configurar los ajustes del bloque {#step-3-configure-the-block-settings}

Usa el panel **Propiedades del bloque** para ajustar cómo se comporta y aparece el bloque.

### Grupos de suscripción {#subscription-groups}

- **Reordenar grupos:** Arrastra un grupo de suscripción por su asa para cambiar el orden en que aparece en el bloque.
- **Agregar o eliminar grupos:** Selecciona **+ Agregar grupos de suscripción** para incluir más grupos, o selecciona el icono de eliminar junto a un grupo para quitarlo del bloque.

### Incluir descripciones {#include-descriptions}

Activa **Incluir descripciones** para mostrar el texto de descripción de cada grupo de suscripción junto a su nombre, lo que da a los visitantes más contexto sobre a qué se están suscribiendo.

### Casilla "Suscribirse a todos" {#subscribe-to-all-checkbox}

Activa el ajuste **Casilla "Suscribirse a todos"** para agregar una casilla adicional al bloque. Cuando un visitante la selecciona, se marcan todas las casillas de grupos de suscripción en el bloque, lo que resulta útil para una adhesión voluntaria rápida a todos los grupos listados.

## Actualizar suscripciones existentes {#update-existing-subscriptions}

Para permitir que los usuarios existentes revisen y actualicen sus suscripciones de correo electrónico, comparte la página de destino usando su [etiqueta de Liquid]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) en un correo electrónico, paso en Canvas u otro mensaje. Cuando un usuario abre la página a través de ese enlace, Braze lo identifica y rellena previamente de forma automática cada casilla de verificación de grupo de suscripción en el bloque **Manage Subscriptions** para que coincida con su estado de suscripción actual, de manera similar a un [centro de preferencias de correo electrónico]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center).

El usuario puede seleccionar o desmarcar casillas de verificación para actualizar sus suscripciones y, a continuación, enviar el formulario para guardar los cambios.

{% alert note %}
El rellenado previo del estado de suscripción actual de un usuario en el bloque **Manage Subscriptions** está incluido de forma predeterminada y no requiere el [nivel Landing Pages Pro]({{site.baseurl}}/user_guide/messaging/landing_pages#plan-tiers). Esto difiere del [rellenado previo basado en Liquid]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages#pre-fill-form-fields) para otros campos de formulario, que sí requiere Landing Pages Pro.
{% endalert %}

## Captar nuevos suscriptores {#capture-new-subscribers}

Para recopilar nuevos suscriptores, por ejemplo en una página de destino para generación de leads, combina el bloque **Manage Subscriptions** con un [bloque de captura de correo electrónico]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages) para que la página capture la dirección de correo electrónico del consumidor junto con sus selecciones de grupo de suscripción.

Si el consumidor no está identificado (por ejemplo, llega sin una etiqueta de Liquid de página de destino), las casillas de verificación aparecen sin seleccionar. Cuando envía el formulario, se suscribe a los grupos de suscripción que haya seleccionado.

## Aspectos a tener en cuenta {#things-to-know}

- **Consentimiento de SMS, RCS y WhatsApp:** Para recopilar el consentimiento de estos canales en una página de destino en lugar de correo electrónico, usa un [bloque de captura de teléfono]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).
- **Experiencia de confirmación:** Las páginas de destino con bloques de formulario, incluido **Gestionar suscripciones**, necesitan una experiencia de confirmación tras el envío. [Crea una página de confirmación]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-4-create-a-confirmation-page-optional) y enlázala desde tu botón **Enviar**.
- **Referencia de bloques de editor:** Para una referencia completa de cada bloque de página de destino y sus propiedades, consulta [Bloques de editor (páginas de destino)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).