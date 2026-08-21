---
nav_title: Rastrear usuarios
article_title: Rastrear usuarios a través de un formulario
description: "Aprende a identificar a los usuarios que envían un formulario a través de tu página de inicio añadiendo una etiqueta de Liquid a tus mensajes."
page_order: 2
---

# Rastrear usuarios a través de un formulario {#track-users-through-a-form}

> Aprende a rastrear a los usuarios que envían un formulario a través de tu página de inicio añadiendo una etiqueta de Liquid de página de inicio a tus mensajes. Esta etiqueta de Liquid es compatible con todos los canales de mensajería de Braze, incluidos correo electrónico, SMS, mensajes dentro de la aplicación y más. Para obtener más información sobre el seguimiento de datos, consulta [Acerca de los datos de seguimiento de páginas de inicio]({{site.baseurl}}/user_guide/messaging/landing_pages/about_tracking_data).

## Requisitos previos {#prerequisites}

Antes de empezar, tendrás que crear una [página de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages) y una [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign).

## Cómo funciona {#how-it-works}

Puedes añadir una etiqueta de Liquid {% raw %}`{% landing_page_url %}`{% endraw %} a cualquiera de tus mensajes de canal único o multicanal en Braze. Cuando un usuario visita esa página de destino y envía el formulario, Braze vinculará automáticamente esos datos a su perfil existente, en lugar de crear un nuevo perfil para ese usuario. En el siguiente ejemplo, se utiliza la etiqueta de Liquid de la página de destino para vincular a los clientes con un cuestionario:

{% raw %}
```html
<a href="{% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

{% alert tip %}
También puedes utilizar las páginas de destino para la generación de leads incrustando la URL de la página en tus canales externos. Después de crear una página de destino, ve a **Landing Page Details** para obtener la URL única de tu página de destino.
{% endalert %}

## Uso de etiquetas de Liquid de páginas de destino {#using-landing-page-liquid-tags}

### Paso 1: Verificar la URL de la página {#page-url}

Braze utilizará la URL de tu página de destino para generar su etiqueta de Liquid única. Si deseas cambiar la URL de la página actual, ve a **Mensajería** > **Páginas de destino** y abre tu página de destino. En **URL de la página**, puedes introducir una nueva URL de página.

{% alert warning %}
Si cambias la URL de la página después de enviar tu mensaje, cualquier usuario que intente visitar tu página de destino utilizando la URL antigua será redirigido a una página `404`.
{% endalert %}

![Un ejemplo de URL de página para una página de destino en Braze.]({% image_buster /assets/img/landing_pages/url-handle-example.png %}){: style="max-width:80%;"}

### Paso 2: Generar la etiqueta de Liquid {#step-2-generate-the-liquid-tag}

Ve a **Mensajería** > **Campaigns** y elige una Campaign. En tu editor de mensajes, selecciona **Personalización**.

![El botón "Añadir personalización" en el editor de arrastrar y soltar.]({% image_buster /assets/img/landing_pages/select-personalization.png %}){: style="max-width:75%;"}

Braze generará automáticamente una etiqueta de Liquid utilizando la [URL de tu página de destino](#page-url). Consulta la siguiente tabla para generar tu etiqueta:

| **Tipo de personalización** | Elige **Página de destino**. |
| **Página de destino** | Elige la página de destino [que creaste anteriormente](#prerequisites). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Generar la etiqueta de Liquid" }

Para añadir la etiqueta de Liquid a tu mensaje, puedes seleccionar **Insertar** o copiar el fragmento de código a tu portapapeles y añadirlo manualmente.

![Una etiqueta de Liquid generada automáticamente para la página de destino seleccionada.]({% image_buster /assets/img/landing_pages/get-snippet.png %}){: style="max-width:40%;"}

Tu fragmento de código será similar al siguiente:

{% raw %}
```ruby
{% landing_page_url custom-url-handle %}
```
{% endraw %}

### Paso 3: Finalizar y enviar tu mensaje {#step-3-finalize-and-send-your-message}

Incrusta el fragmento de código de Liquid en tu mensaje y finaliza el resto de tu mensaje. Por ejemplo:

{% raw %}
```html
<a href="{% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

Cuando estés listo, puedes enviar el mensaje para empezar a rastrear usuarios a través de tu página de destino.

### Uso de URLs de páginas de destino en Content Cards {#use-landing-page-urls-in-content-cards}

Content Cards tiene un [límite de carga útil de 2&nbsp;KB]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#size-limitations-for-content-cards) que se aplica a la tarjeta completa después de que se renderiza Liquid. Cuando incluyes una etiqueta de Liquid {% raw %}`{% landing_page_url %}`{% endraw %}, Braze cuenta el token de seguimiento de la página de destino como un valor fijo de 32&nbsp;bytes dentro de ese límite, no la longitud completa del token. El resto de la URL y el título, cuerpo y demás campos de la tarjeta siguen contando dentro del límite de la forma habitual.