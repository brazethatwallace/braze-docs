---
nav_title: Plantillas de Webhook
article_title: Plantillas de Webhook
page_order: 5
tool:
  - Templates
channel:
  - webhooks
description: "Aprende a crear y personalizar plantillas de webhook para usarlas posteriormente en la plataforma Braze."

---

# Crear una plantilla de webhook {#create-a-webhook-template}

> A medida que construyes y personalizas tus webhooks, puedes crear y aprovechar plantillas de webhook para usarlas posteriormente en la plataforma Braze. De esta forma, puedes construir de manera consistente una variedad de webhooks en tus diferentes Campaigns.

## Paso 1: Ve al editor de plantillas de webhook {#step-1-go-to-the-webhook-template-editor}

En el panel de Braze, ve a **Contenido** > **Webhook**.

![La página "Plantillas de Webhook" con plantillas de webhook prediseñadas y guardadas.]({% image_buster /assets/img_archive/webhook_template_campaign.png %})

## Paso 2: Elige tu plantilla {#step-2-choose-your-template}

Desde aquí, puedes elegir crear una nueva plantilla, usar una de las plantillas de webhook prediseñadas o editar una plantilla existente.

Por ejemplo, si estás usando [LINE]({{site.baseurl}}/user_guide/channels/line) como canal de mensajería, puedes configurar varios webhooks usando las plantillas prediseñadas para **LINE Carousel** o **LINE Image**.

## Paso 3: Completa los detalles de la plantilla {#step-3-fill-out-template-details}

1. Dale a tu plantilla de webhook un nombre único.
2. (Opcional) Añade una descripción de la plantilla para explicar cómo se pretende usar esta plantilla.
3. Añade [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams) y [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) según sea necesario para ayudar a encontrar y filtrar tu plantilla.

## Paso 4: Construye tu plantilla {#step-4-build-your-template}

1. Introduce la URL del webhook.
2. Selecciona el método HTTP.
3. Añade un cuerpo de solicitud. Puede ser **JSON Key/Value Pairs** o **Raw Text**.
4. (Opcional) Añade un encabezado de solicitud. Esto puede ser requerido por el destino de tu webhook.

![La pestaña "Redactar" al crear una plantilla de webhook. Los campos disponibles son URL del webhook, método HTTP, cuerpo de solicitud y encabezados de solicitud. También puedes añadir idiomas.]({% image_buster /assets/img_archive/Webhook_template_test.png %}){: style="max-width:90%"}

## Paso 5: Prueba tu plantilla {#step-5-test-your-template}

Para ver cómo se ve tu webhook antes de enviarlo a tus usuarios, puedes enviar un webhook de prueba usando la pestaña **Test**. Aquí, puedes seleccionar previsualizar el mensaje como un usuario aleatorio, un usuario existente o un usuario personalizado.

## Paso 6: Guarda tu plantilla {#step-6-save-your-template}

Asegúrate de guardar tu plantilla seleccionando **Save Template**. Ahora estás listo para usar esta plantilla en cualquier Campaign que elijas.

{% alert note %}
Las ediciones realizadas a una plantilla existente no se reflejan en las Campaigns que fueron creadas usando versiones anteriores de esa plantilla.
{% endalert %}

## Administrar tus plantillas {#managing-your-templates}

Puedes [duplicar y archivar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates) plantillas de webhook para ayudar a organizar y administrar mejor tu lista de plantillas.