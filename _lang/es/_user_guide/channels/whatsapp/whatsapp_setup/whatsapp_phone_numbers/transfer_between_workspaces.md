---
nav_title: Transferir entre espacios de trabajo
article_title: Transferir números de teléfono y grupos de suscripción entre espacios de trabajo
page_order: 3
description: "Este artículo de referencia explica cómo transferir tu número de teléfono de WhatsApp y los grupos de suscripción entre espacios de trabajo."
page_type: reference
channel:
  - WhatsApp
---

# Transferir números de teléfono de WhatsApp y grupos de suscripción entre espacios de trabajo {#transfer-whatsapp-phone-numbers-and-subscription-groups-between-workspaces}

> Esta página explica cómo puedes mover un número de teléfono de una cuenta de WhatsApp Business (WABA) y su grupo de suscripción asociado de un espacio de trabajo a otro dentro de Braze. Este proceso simplifica tu experiencia de uso de WhatsApp con Braze y reduce la necesidad de ayuda de ingeniería.

## Requisitos previos {#prerequisites}

- Confirma que tienes el [permiso de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions) "Manage Subscription Groups" en ambos espacios de trabajo, el original y el nuevo.
- La WABA no puede cruzar múltiples [clústeres de Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). Es poco probable que esto ocurra si trabajas dentro de una misma empresa.

## Transferir un número de teléfono y un grupo de suscripción {#transferring-a-phone-number-and-subscription-group}

### Paso 1: Archivar el grupo de suscripción {#step-1-archive-the-subscription-group}

Para archivar un grupo de suscripción de WhatsApp, sigue estos pasos:

1. Ve al espacio de trabajo donde existe actualmente el grupo de suscripción.
2. Ve a **Audiencia** > **Administración del grupo de suscripción** y busca el grupo de suscripción asociado al número de teléfono de WhatsApp que deseas mover.
3. Pasa el cursor sobre el estado del grupo de suscripción y selecciona <i class="fa-solid fa-box-archive"></i> **Archivar**, lo que marcará el grupo de suscripción como inactivo pero no lo eliminará.

![Botón "Archivar" que aparece al pasar el cursor sobre el estado "Activos" de un grupo de suscripción.]({% image_buster /assets/img/whatsapp/archive_subscription_group.png %}){: style="max-width:70%;"}

### Paso 2: Integrar el número de teléfono de WhatsApp en el nuevo espacio de trabajo {#step-2-integrate-the-whatsapp-phone-number-into-the-new-workspace}

1. Ve al espacio de trabajo donde deseas mover el número de teléfono de WhatsApp.
2. Ve a **Integraciones de socios** > **Socios tecnológicos** > **WhatsApp**, luego desplázate hasta la sección **WhatsApp Messaging Integration**.
3. Selecciona la opción **Crear nuevo grupo de suscripción y número de teléfono**.
4. Inicia el proceso de integración, durante el cual puedes seleccionar el número de teléfono del grupo de suscripción archivado.

### Paso 3: Verificar la integración {#step-3-verify-the-integration}

1. Después de completar la integración, confirma que el número de teléfono de WhatsApp está ahora asociado al grupo de suscripción en el nuevo espacio de trabajo.
2. Realiza una prueba para confirmar que los mensajes se pueden enviar y recibir a través de ese número de teléfono de WhatsApp.

## Consideraciones {#considerations}

- Si necesitas transferir el número de teléfono de WhatsApp de vuelta al espacio de trabajo original, repite los pasos. Archiva el grupo de suscripción en el espacio de trabajo de destino y luego intégralo en el espacio de trabajo original.
- No necesitas eliminar el número de teléfono de WhatsApp de tu Meta Business Manager durante la transferencia.