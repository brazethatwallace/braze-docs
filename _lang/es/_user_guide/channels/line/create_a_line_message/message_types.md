---
nav_title: Tipos de mensaje
article_title: Tipos de mensaje de LINE
page_order: 0
description: "Este artículo cubre los diferentes tipos de mensajes de LINE."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/message_types/
---

# Tipos de mensaje de LINE {#line-message-types}

> Este artículo cubre los tipos de mensajes de LINE que puedes redactar, incluyendo aspectos y limitaciones.

Cuando redactas un mensaje de LINE, puedes arrastrar y soltar tipos de mensaje en el editor del compositor y luego personalizarlos.

![Panel de tipos de mensaje con tipos de mensaje para arrastrar al editor del compositor, incluyendo texto, imagen, mensaje enriquecido y mensaje basado en tarjetas.]({% image_buster /assets/img/line/line_message_types.png %}){: style="max-width:40%;"}

## Texto {#text}

Un mensaje de texto de LINE puede contener hasta 5000 caracteres e incluir emojis y personalización con Liquid.

Los casos de uso incluyen:
- Anunciar una promoción por tiempo limitado para existencias en liquidación
- Enviar felicitaciones de cumpleaños personalizadas con tarjetas de promoción únicas
- Compartir actualizaciones rápidas sobre próximos eventos

![Un mensaje de texto que recuerda al usuario que no se olvide de una fiesta de Black Friday y la posibilidad de ahorrar hasta un 80 % antes de medianoche.]({% image_buster /assets/img/line/line_text_message.png %}){: style="max-width:40%;"}

## Imagen {#image}

Un mensaje de imagen de LINE se puede añadir a través de la [biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library), una URL o Liquid. Estas imágenes son independientes y no contienen enlaces clicables.

Los casos de uso incluyen:
- Mostrar un destino vacacional para inspirar a los usuarios a buscar la compra de boletos de avión
- Destacar promociones de fin de temporada para animar a los usuarios a abastecerse de ropa de invierno del próximo año con grandes ofertas
- Iniciar una cuenta regresiva visual para una venta anual en toda la tienda

![Un mensaje de imagen que promociona una oferta de tostadoras.]({% image_buster /assets/img/line/line_image_message.png %}){: style="max-width:40%;"}

### Imagen por URL {#url-image}

Usa imágenes por URL para casos de uso que incorporen:
- Imágenes dinámicas con Liquid incluyendo Liquid en el atributo de fuente de tu imagen. Por ejemplo, puedes insertar {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} como la URL de la imagen para incluir el nombre del usuario en la imagen
- [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) extrayendo imágenes directamente de tu servidor web o API de acceso público
- [Catálogos de Braze]({{site.baseurl}}/user_guide/data/activation/catalogs) accediendo a imágenes desde archivos CSV importados y puntos de conexión de API

| **Especificaciones** | **Propiedades recomendadas** |
|--------------------------|----------------------------|
| Longitud de URL del archivo de imagen | 2000 caracteres máximo  |
| Formato de imagen          | PNG, JPEG             |
| Tamaño de archivo     |  10&nbsp;MB máximo |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Imagen por URL" }

## Mensajes enriquecidos (mapa de imagen) {#rich-messages-image-map}

Un mensaje enriquecido de LINE es una imagen que contiene uno o más enlaces que se abren al seleccionar áreas específicas de la imagen. Selecciona una plantilla de mensaje enriquecido para elegir cómo se mapean los enlaces sobre la imagen.

Los casos de uso incluyen:
- Mostrar una cuadrícula de bolsos recién llegados con enlaces a la página de producto de cada bolso
- Presentar un menú interactivo que inicia un pedido combinado al seleccionar un artículo
- Disponer múltiples promociones para que los usuarios elijan seleccionando un cuadro de la cuadrícula

![Un mensaje enriquecido de seis cuadros con una foto de una cuadrícula en blanco y negro que los usuarios pueden tocar para recibir una oferta aleatoria.]({% image_buster /assets/img/line/line_rich_message.png %})

### Mapa de imagen {#image-map}

| **Especificaciones** | **Propiedades recomendadas** |
|--------------------------|----------------------------|
| Longitud de URL del archivo de imagen | 2000 caracteres máximo  |
| Formato de imagen          | PNG (puede ser transparente), JPEG             |
| Relación de aspecto          | 1:1 (ancho:alto)
| Tamaño de archivo     |  10&nbsp;MB máximo |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Mapa de imagen" }

### Enlace URI {#uri-link}

| **Especificaciones** | **Propiedades recomendadas** |
|--------------------------|----------------------------|
| Cantidad de caracteres      | 1000 máximo |
| Esquemas              | HTTP, HTTPS, LINE, tel |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Enlace URI" }

### Texto

Un mensaje enriquecido de texto puede contener hasta 400 caracteres.

## Basado en tarjetas (carrusel) {#card-based-carousel}

Un mensaje basado en tarjetas de LINE permite a los usuarios desplazarse por múltiples mensajes, como un carrusel, y tomar acción en los mensajes más relevantes para ellos seleccionando una tarjeta o los botones de una tarjeta.

Los casos de uso incluyen:
- Mostrar promociones para artículos específicos del menú
- Destacar las chaquetas más vendidas de la temporada
- Presentar una muestra de utensilios y accesorios de cocina incluidos en un kit

![Un mensaje basado en tarjetas con al menos dos tarjetas que promocionan sándwiches en el editor del compositor.]({% image_buster /assets/img/line/line_card_message.png %})

### Mensaje {#message}

| **Especificaciones** | **Propiedades recomendadas** |
|--------------------------|----------------------------|
| Columnas                  | 10 máximo |
| Relación de aspecto             | Rectángulo: 1.51:1 <br> Cuadrado: 1:1  |
| Título                    | 40 caracteres máximo
{: .reset-td-br-1 .reset-td-br-2 aria-label="Mensaje" }


### Imagen

| **Especificaciones** | **Propiedades recomendadas** |
|--------------------------|----------------------------|
| URL de imagen                 | 2000 caracteres máximo |
| Formato de imagen              | JPEG o PNG |
| Ancho                     | 1024 píxeles  |
| Tamaño de archivo                 | 1 MB |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Imagen" }


### Texto

| **Especificaciones** | **Propiedades recomendadas** |
|-------------------------|----------------------------|
| Caracteres              | 120 máximo (sin imagen ni título) <br> 60 máximo (mensaje con imagen o título)  |
| Acciones                 | 3 máximo |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Texto" }