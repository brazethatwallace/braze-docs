---
nav_title: Reglas de mensajería
article_title: Reglas de mensajería
page_order: 1
page_type: reference
description: "Esta página explica cómo usar las reglas de mensajería en el flujo de trabajo de aprobación para Campaigns y Canvas con un gran volumen de envío."
---

# Reglas de mensajería {#messaging-rules}

> Usa las reglas de mensajería en tu flujo de trabajo de aprobación para limitar el número de usuarios alcanzables antes de que se requiera una aprobación adicional&#8212;de esta forma, puedes revisar tus Campaigns y Canvas antes de dirigirte a una audiencia más grande.

## Requisitos previos {#prerequisites}

Solo los administradores de Braze pueden establecer reglas de mensajería, pero cualquier usuario de Braze puede ser un aprobador de reglas de mensajería (incluidos los usuarios sin permisos generales de aprobación).

## Cómo funciona {#how-it-works}

Las reglas de mensajería se aplican a un espacio de trabajo y están compuestas por un tipo de mensaje y un número máximo de usuarios alcanzables.

- **Tipo de mensaje:** Define a qué tipo de mensaje se aplica la regla: Campaign, Canvas, o tanto Canvas como Campaigns.
- **Máximo de usuarios alcanzables:** Determina qué tamaño de audiencia requiere una aprobación adicional.

### Aprobadores separados {#separate-approvers}

Dos reglas pueden compartir el mismo máximo de usuarios para que puedas organizar y separar tus reglas por aprobadores. Por ejemplo, creas las siguientes dos reglas:

- Regla A para Canvas con un máximo de 100,000 usuarios con aprobadores en tu equipo legal
- Regla B para Canvas con un máximo de 100,000 usuarios con aprobadores en tu equipo de marketing

### Sin superposición de usuarios alcanzables {#no-overlapping-reachable-users}

Para evitar confusiones, no puedes establecer reglas idénticas con un número superpuesto de usuarios para el mismo tipo de mensaje y aprobadores. Por ejemplo, la siguiente regla de mensajería **no se puede** establecer:

- Regla C para Canvas con un máximo de 10,000 usuarios
- Regla D para Canvas con un máximo de 1,000,000 usuarios

## Crear una regla de mensajería {#creating-a-messaging-rule}

### Paso 1: Añadir una regla {#step-1-add-a-rule}

{% alert note %}
Puedes crear hasta cinco reglas de mensajería.
{% endalert %}

1. Ve a **Configuración** > **Flujo de trabajo de aprobación** > **Reglas de mensajería**.
2. Selecciona **Crear regla**.
3. Dale un nombre a esta regla (por ejemplo, "Todas las suscripciones de usuarios").
4. Para **Tipo de mensaje**, selecciona **Campaign**, **Canvas** o **Both Canvas and Campaigns** para aplicar la regla de aprobación.
5. Introduce un número para **Máximo de usuarios alcanzables**. Para más información, consulta [Estadísticas de audiencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users#audience-statistics).
6. Selecciona **Guardar**.

![Un ejemplo de regla de mensajería "Rule 1" para Campaigns con 100,000 usuarios como máximo. Hay un usuario que puede aprobar el Canvas y la campaña para su lanzamiento.]({% image_buster /assets/img/target_population_approval_example.png %}){: style="max-width:90%;"}

### Paso 2: Determinar el lanzamiento con aprobación (opcional) {#step-2-determine-launching-with-approval-optional}

Selecciona **Permitir lanzamiento con aprobación**. A continuación, para **Con aprobación de**, selecciona los aprobadores que tienen permiso para aprobar el Canvas o la campaña si se alcanza el máximo.

Ten en cuenta los siguientes detalles sobre el lanzamiento de mensajes con aprobación:

- Si se alcanza el máximo y se selecciona un aprobador, el usuario de Braze con el permiso de aprobación puede seleccionar **Aprobado** en el menú desplegable de aprobación de **Público objetivo**.
- Si se alcanza el máximo y no se selecciona un aprobador, se impide el lanzamiento del Canvas o la campaña.

![El paso "Resumen" del flujo de trabajo de Canvas que muestra que necesitas una aprobación para lanzar.]({% image_buster /assets/img/non_approver_banner.png %}){: style="max-width:90%;"}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Tengo que reconfigurar mis permisos para usar las reglas de mensajería? {#do-i-have-to-reconfigure-my-permissions-to-use-messaging-rules}

No. Cualquier usuario, independientemente de sus permisos actuales, puede ser seleccionado como aprobador de población objetivo.

### ¿Cómo se relacionan las reglas de mensajería con el paso de público objetivo? {#how-do-messaging-rules-relate-to-the-target-audience-step}

Las reglas de mensajería no tienen en cuenta detalles como los eventos desencadenantes. Por ejemplo, una campaña podría dirigirse a todos tus usuarios. Sin embargo, la campaña se desencadena por evento, por lo que los usuarios reales que la reciben son menos.

### ¿Cambiará algo automáticamente cuando se activen las reglas de mensajería? {#will-anything-automatically-change-when-messaging-rules-are-turned-on}

No. Después de activar esta característica, debes introducir manualmente el número máximo de usuarios y seleccionar aprobadores para usar la característica.