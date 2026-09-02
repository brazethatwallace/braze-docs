---
article_title: Límites de velocidad del espacio de trabajo
description: "Aprende a configurar los límites de velocidad del espacio de trabajo para controlar cómo se distribuye el límite de velocidad general de la API de tu empresa entre los espacios de trabajo individuales, evitando que una sola integración o equipo realice demasiadas solicitudes a un punto de conexión específico."
permalink: /workspace_rate_limits/
---

# Límites de velocidad del espacio de trabajo {#workspace-rate-limits}

> Aprende a configurar los límites de velocidad del espacio de trabajo para controlar cómo se distribuye el límite de velocidad general de la API de tu empresa entre los espacios de trabajo individuales, evitando que una sola integración o equipo realice demasiadas solicitudes a un punto de conexión específico.

## Requisitos previos {#prerequisites}

Los límites de velocidad del espacio de trabajo solo están disponibles para contratos de Braze sin puntos de datos. Además, necesitarás [permisos de administrador]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para gestionar los límites de velocidad.

## Acerca de los límites de velocidad del espacio de trabajo {#about-workspace-rate-limits}

De forma predeterminada, los límites de velocidad a nivel de empresa se comparten entre tus espacios de trabajo.

Con los límites de velocidad del espacio de trabajo, puedes establecer un número máximo de solicitudes de API que un espacio de trabajo puede realizar a un endpoint de ingesta específico, como `/users/track` o datos del SDK or kit de desarrollo de software. También puedes aplicar límites de velocidad a un grupo de espacios de trabajo, lo que significa que el límite se comparte entre todos los espacios de trabajo de ese grupo.

Por ejemplo, si tu endpoint `/users/track` tiene un límite de velocidad a nivel de empresa de 500 000 solicitudes por hora, podrías establecer los siguientes límites de velocidad del espacio de trabajo:

- Un límite de velocidad de 10 000 solicitudes por hora aplicado al _Espacio de trabajo 1_
- Un límite de velocidad compartido de 200 000 solicitudes por hora aplicado al _Espacio de trabajo 2_ y al _Espacio de trabajo 3_
- Ningún límite de velocidad aplicado al _Espacio de trabajo 4_, lo que significa que se utiliza el límite de velocidad predeterminado a nivel de empresa

## Gestión de los límites de velocidad del espacio de trabajo {#managing-workspace-rate-limits}

### Asignar un límite {#assigning-a-limit}

Para asignar un nuevo límite de velocidad a uno o más espacios de trabajo, ve a **Configuración** > **Configuración de administrador** > **Límites de velocidad del espacio de trabajo** y selecciona **Asignar límites de velocidad**.

![La página 'Límites de velocidad del espacio de trabajo' en el panel de Braze.]({% image_buster /assets/unlisted_docs/img/workspace_rate_limits/settings.png %}){: style="max-width:85%;"}

A continuación, elige un endpoint y uno o más espacios de trabajo, y luego introduce tu límite de velocidad. El límite puede ser cualquier número entero mayor que 1.000 que no exceda tu límite de velocidad a nivel de empresa.

Cuando hayas terminado, selecciona **Actualizar límite de velocidad**.

![La ventana emergente 'Límite de velocidad' con opciones para elegir un endpoint, espacios de trabajo y límite de velocidad.]({% image_buster /assets/unlisted_docs/img/workspace_rate_limits/update_rate_limit.png %}){: style="max-width:45%;"}

{% alert note %}
Si eliges más de un espacio de trabajo, el límite de velocidad se compartirá entre ese grupo de espacios de trabajo.
{% endalert %}

### Editar un límite {#editing-a-limit}

Para editar un límite de velocidad de espacio de trabajo existente, ve a **Configuración** > **Configuración de administrador** > **Límites de velocidad del espacio de trabajo** y selecciona los <i class="fas fa-ellipsis-vertical" aria-label="Puntos suspensivos verticales"></i> puntos suspensivos verticales y elige **Editar**. Tu nuevo límite de velocidad puede tardar unos minutos en entrar en vigor.

### Restablecer un límite {#resetting-a-limit}

Para restablecer un límite de velocidad existente de modo que vuelva a tu límite de velocidad a nivel de empresa, ve a **Configuración** > **Configuración de administrador** > **Límites de velocidad del espacio de trabajo** y selecciona los <i class="fas fa-ellipsis-vertical" aria-label="Puntos suspensivos verticales"></i> puntos suspensivos verticales y elige **Restablecer**.

## Monitoreo del uso {#monitoring-usage}

### Encabezados de respuesta {#response-headers}

De forma predeterminada, todas las respuestas de ingesta incluyen los siguientes encabezados, que reflejan tu límite de velocidad estable a nivel de empresa.

Te recomendamos utilizar estos encabezados en tu lógica de integración para gestionar los límites de velocidad de manera efectiva. Por ejemplo, puedes reducir el volumen de solicitudes a medida que te acerques a estos límites y usar el encabezado `Retry-After` para determinar cuándo reintentar.

| Nombre del encabezado | Descripción |
| ----- | ----- |
| `X-RateLimit-Limit` | El número máximo de solicitudes permitidas en la ventana de límite de velocidad actual. |
| `X-RateLimit-Remaining` | El número de solicitudes restantes en la ventana actual. |
| `X-RateLimit-Reset` | Cuándo se reinicia la ventana de límite de velocidad actual (segundos epoch UTC). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Códigos de error {#error-codes}

Si se alcanza un límite de velocidad del espacio de trabajo, tu solicitud devolverá un código de respuesta `429` y los encabezados incluirán un valor `Retry-After`. Este representa el número de segundos hasta que se reinicie el límite de velocidad.

El valor `Retry-After` refleja el número de segundos hasta el inicio de la siguiente hora, cuando el límite de velocidad del espacio de trabajo se reinicia.

### Panel de uso de API {#api-usage-dashboard}

Para monitorear el volumen de solicitudes, los códigos de respuesta y el comportamiento de ingesta en los espacios de trabajo, también puedes utilizar el [panel de uso de API]({{site.baseurl}}/user_guide/analytics/dashboards/api_usage).

Puedes filtrar el panel para mostrar `429 Workspace Rate Limited` o `429 Company Rate Limited`, de modo que puedas identificar rápidamente si una solicitud fue limitada por el límite de velocidad de la empresa o del espacio de trabajo.