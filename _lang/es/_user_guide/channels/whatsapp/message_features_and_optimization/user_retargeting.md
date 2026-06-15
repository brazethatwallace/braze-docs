---
nav_title: Reorientación de usuarios
article_title: Reorientación de usuarios
page_order: 5
description: "Este artículo de referencia cubre cómo los usuarios pueden reorientar sus mensajes según las interacciones de WhatsApp."
page_type: reference
channel:
  - WhatsApp
---

# Reorientación de usuarios {#user-retargeting}

> Además de cambiar el estado de suscripción del usuario, Braze también registrará las interacciones en el perfil de usuario para filtrar y desencadenar mensajes.<br><br>Estos filtros y desencadenadores te permiten filtrar usuarios que han recibido mensajes de WhatsApp o que han recibido mensajes de WhatsApp de una Campaign o un paso en Canvas de WhatsApp específico.

## Opciones de reorientación {#retargeting-options}

{% alert note %}
Al crear audiencias con reorientación de usuarios, es posible que desees incluir o excluir a ciertos usuarios en función de sus preferencias y para cumplir con las leyes de privacidad, como el derecho de "No vender ni compartir" bajo la CCPA. Los especialistas en marketing deben implementar los filtros relevantes para la elegibilidad de los usuarios dentro de los criterios de entrada de su Canvas o Campaign.
{% endalert %}

### Filtrar usuarios por WhatsApp {#filter-users-by-whatsapp}

Los usuarios pueden filtrarse por la última vez que recibieron un mensaje de WhatsApp o si han recibido un mensaje de WhatsApp de una Campaign de WhatsApp específica. Los filtros se pueden configurar en el paso Usuarios objetivo del creador de campañas.

#### Filtrar por último WhatsApp recibido {#filter-by-last-received-whatsapp}

![Filtro para la última recepción de un mensaje de WhatsApp el 22 de abril de 2025.]({% image_buster /assets/img/whatsapp/whatsapp23.png %}){: style="max-width:75%"}

#### Filtrar por mensajes recibidos de una Campaign de WhatsApp {#filter-by-received-messages-from-whatsapp-campaign}

Filtra a los usuarios que han recibido un mensaje de una Campaign de WhatsApp específica. Con este filtro, también tienes la opción de filtrar a aquellos que no han recibido mensajes de una Campaign de WhatsApp.

{% alert note %}
Cuando un mensaje de WhatsApp se entrega, se abre o se hace clic en él, Braze actualiza los datos de todos los perfiles que comparten el mismo número de teléfono que el perfil que registró la interacción, por lo que los usuarios que comparten ese número con alguien que recibió, abrió o hizo clic en el mensaje pueden coincidir con los filtros de "recibido" aunque no se les haya enviado directamente.
{% endalert %}

![Filtro para recibir una Campaign de WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp22.png %}){: style="max-width:75%"}

### Filtrar por interacción {#filter-by-engagement}

Reorienta a los usuarios que han leído, o no han leído, una Campaign o un paso en Canvas de WhatsApp.

#### Reorientar usuarios que han abierto/leído una Campaign de WhatsApp específica {#retarget-users-who-have-openedread-a-specific-whatsapp-campaign}

1. Crea un segmento usando el filtro **Clicked/Opened Campaign**.
2. Selecciona **read WhatsApp message**.
3. Elige la Campaign deseada.

![Filtro para haber leído un mensaje de WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp21.png %}){: style="max-width:75%"}

#### Reorientar usuarios que han abierto/leído un paso en Canvas específico {#retarget-users-who-have-openedread-a-specific-canvas-step}

1. Crea un segmento usando el filtro **Clicked/Opened Step**.
2. Selecciona **read WhatsApp message**.
3. Elige el Canvas y los pasos en Canvas deseados.

![Filtro para leer un paso de WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp20.png %}){: style="max-width:75%"}

#### Filtrar por atribución de Campaign o Canvas {#filter-by-campaign-or-canvas-attribution}

Filtra a los usuarios que han abierto/leído una Campaign o componente de Canvas de WhatsApp específico, o una etiqueta.

![Filtro para abrir un mensaje de WhatsApp específico.]({% image_buster /assets/img/whatsapp/whatsapp19.png %}){: style="max-width:75%"}