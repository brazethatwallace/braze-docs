---
nav_title: Acerca del seguimiento de datos
article_title: Acerca del seguimiento de datos de páginas de inicio
description: "Obtén información sobre el seguimiento y los datos anonimizados de las páginas de inicio en Braze."
page_order: 10
alias: /landing_pages/data_tracking/
---

# Acerca del seguimiento de datos de páginas de inicio {#about-landing-page-tracking-data}

> Obtén información sobre el seguimiento y los datos anonimizados de las páginas de inicio en Braze.

## Métodos de seguimiento {#tracking-methods}

### SDK Web {#web-sdk}

El SDK Web de Braze se inicializa cuando un usuario envía un formulario en una página de inicio. Antes del envío del formulario, no se recopilan datos personales y el SDK no realiza un seguimiento activo de los usuarios. Una vez completada la inicialización, el SDK no almacena ningún dato en el navegador (como cookies, almacenamiento local u otros).

El SDK Web de Braze se inicializa inmediatamente cuando un usuario navega a la página de inicio a través de un enlace generado por una etiqueta de Liquid {% raw %}`{% landing_page_url %}`{% endraw %} en un mensaje de Braze.

Cuando se envía un formulario, el SDK recopilará los siguientes datos:

- Evento de envío de formulario (nombre del evento y hora del envío)
- Datos especificados por tu equipo en el formulario (como nombre, correo electrónico y número de teléfono)
- Hora de inicio de sesión
- ID de dispositivo (un ID único que se genera, pero no se almacena, para el dispositivo)
- País determinado por la dirección IP

### Datos anonimizados {#anonymized-data}

Antes de que un usuario envíe un formulario, los datos rastreados en una página de inicio consisten únicamente en información anonimizada y no identificable. Esto incluye métricas agregadas estándar del sitio web, como el número de visualizaciones de página (impresiones) y clics que recibe una página de inicio.

Dado que estos datos no están vinculados a usuarios identificables, no se pueden utilizar para reorientar ni rastrear el comportamiento individual de los usuarios.

## Fusión de perfiles de usuario duplicados {#merging-duplicate-user-profiles}

Braze no fusiona automáticamente usuarios basándose en atributos, como correo electrónico o teléfono, cuando se envía un formulario de página de inicio. Si se envía un formulario con un correo electrónico o número de teléfono que coincide con un perfil de usuario existente, Braze crea un perfil de usuario independiente.

Para fusionar perfiles de usuario duplicados, puedes:

- Desencadenar el [punto de conexión `/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) cuando se envía un formulario de página de inicio para fusionar el nuevo perfil con un perfil existente.
- Programar una [fusión masiva]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/#bulk-merging) para fusionar periódicamente perfiles duplicados basándose en identificadores coincidentes.