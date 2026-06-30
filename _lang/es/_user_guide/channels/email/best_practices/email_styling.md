---
nav_title: Estilo del correo electrónico
article_title: Estilo de correo electrónico
page_order: 2
page_type: reference
description: "En este artículo se describen las mejores prácticas de estilo de correo electrónico a las que puedes recurrir al crear tus campañas de correo electrónico."
channel: email

---

# Estilo de correo electrónico {#email-styling}

> En este artículo se describen las mejores prácticas de estilo de correo electrónico, incluyendo líneas del asunto, texto de preencabezado, tamaño del correo electrónico y recomendaciones de imágenes.

## Estilo de dirección {#address-styling}

La línea del asunto es una de las primeras cosas que verán los destinatarios al recibir tu mensaje. Si la limitas a entre 6 y 10 palabras, obtendrás las tasas de apertura más altas.

También hay distintos enfoques para crear una buena línea del asunto, desde formular una pregunta para despertar el interés del lector o ser más directo, hasta personalizarla para captar la atención de tu clientela. No te quedes con una sola línea del asunto, aprovecha las [pruebas A/B]({{site.baseurl}}/user_guide/messaging/ab_testing#what-are-multivariate-and-ab-testing) para probar otras nuevas y medir su eficacia. Las líneas del asunto no deben tener más de 35 caracteres para que se muestren correctamente en dispositivos móviles.

El campo "De" debe mostrar claramente quién es el remitente. Procura no utilizar el nombre de una persona o una abreviatura poco común. En su lugar, utiliza un nombre reconocible como el de tu marca. Si utilizar el nombre de una persona se ajusta a los métodos de personalización del correo electrónico de tu marca, mantén la coherencia para desarrollar una relación con el destinatario. El nombre "De" no debe tener más de 25 caracteres para que se muestre correctamente en el móvil.

### Direcciones sin respuesta {#no-reply-addresses}

Por lo general, no se recomienda utilizar direcciones de correo electrónico sin respuesta por múltiples razones, ya que desvinculan a tus lectores. Muchos destinatarios responden al correo electrónico para cancelar su suscripción, por lo que si no se les permite hacerlo, la siguiente acción más común es marcar el correo electrónico como correo no deseado.

Recibir respuestas de fuera de oficina puede proporcionar información valiosa, aumentando las tasas de apertura y reduciendo los informes de correos no deseados (al eliminar a quienes no desean recibir correos). A nivel personal, una dirección sin respuesta puede parecer impersonal para los destinatarios y puede disuadirlos de recibir más correos electrónicos de tu empresa.

## Texto de preencabezado {#preheader-text}

El texto de preencabezado en un correo electrónico comunica el punto principal del mensaje de manera eficiente para captar el interés del lector y fomentar las aperturas. El texto de preencabezado también es utilizado frecuentemente por los especialistas en marketing de correo electrónico para proporcionar información adicional sobre el contenido de un correo. Un preencabezado es el texto de vista previa que se muestra inmediatamente después del asunto de un correo electrónico. En el siguiente ejemplo, el preencabezado es `- Brand. New. Lounge Shorts`.

![Texto de preencabezado en un buzón de entrada de Gmail con el texto "Brand. New. Lounge Shorts".]({% image_buster /assets/img_archive/preheader_example.png %})

La cantidad de texto de preencabezado visible depende del cliente de correo electrónico del usuario y de la longitud de la línea del asunto del correo. Generalmente, sugerimos que los preencabezados de correo electrónico tengan entre 50 y 100 caracteres.

{% alert note %}
El preencabezado puede hacer referencia a Liquid en el cuerpo del correo electrónico, y el cuerpo del correo electrónico puede hacer referencia a Liquid en el preencabezado. Esto se debe a que el texto de preencabezado es parte del cuerpo del correo electrónico cuando envías mensajes a los destinatarios.
{% endalert %}

Aquí tienes algunas mejores prácticas a tener en cuenta al escribir tus preencabezados:

1. Las llamadas a la acción entran en juego después de que los lectores hayan abierto tu correo electrónico.
  - Dirige a tus lectores en la dirección correcta, ya sea que quieras que se suscriban, compren un producto o visiten tu sitio web.
  - Usa palabras contundentes para que el lector sepa exactamente lo que le estás pidiendo, pero asegúrate de que refleje la voz de marca de tu empresa y que cada llamada a la acción muestre algún tipo de valor para el consumidor.
  - El preencabezado no debe superar los 85 caracteres y debe tener algún tipo de llamada a la acción descriptiva que respalde la línea del asunto.

2. Los correos electrónicos y las páginas de destino a las que diriges a tus usuarios deben estar optimizados para dispositivos móviles:
  - Sin cuadros intersticiales
  - Campos de formulario grandes
  - Navegación sencilla
  - Texto grande
  - Espacios en blanco generosos
  - Texto del cuerpo breve y conciso
  - Llamadas a la acción claras

### Límites de caracteres del preencabezado {#preheader-character-limits}

  |   Cliente de correo móvil  |  Límite  |
  |:----------------------:|:-------:|
  | iOS Outlook            | 74      |
  | Android nativo         | 43      |
  | Android Gmail          | 24      |
  | iOS nativo             | 82      |
  | iOS Gmail              | 30      |
  {: .reset-td-br-1 .reset-td-br-2 aria-label="Límites de caracteres del preencabezado" }

  |  Cliente de correo de escritorio  |  Límite  |
  |:----------------------:|:-------:|
  | Apple Mail             | 33      |
  | Outlook '13            | 38      |
  | Outlook para Mac '15   | 53      |
  | Outlook '16            | 50      |
  {: .reset-td-br-1 .reset-td-br-2 aria-label="Límites de caracteres del preencabezado" }


  |  Cliente de correo web  |  Límite  |
  |:----------------------:|:-------:|
  | AOL Mail               | 81      |
  | Gmail                  | 119     |
  | Outlook.com            | 49      |
  | Office 365             | 40      |
  | Mail.ru                | 64      |
  {: .reset-td-br-1 .reset-td-br-2 aria-label="Límites de caracteres del preencabezado" }

## Tamaño del correo electrónico {#email-size}

El tamaño del correo electrónico se refiere al tamaño del HTML de tu mensaje en Braze (el cuerpo que construyes y lo que Braze añade cuando se envía el mensaje).

- Asegúrate de limitar el tamaño de tu correo electrónico. Los cuerpos de correo electrónico mayores de 102&nbsp;KB no solo son extremadamente exigentes para los servidores de Braze, sino que también son recortados por Gmail y otros clientes de correo electrónico.
- Las imágenes alojadas que referencias por URL no se incrustan en el HTML de la misma manera que al pegar grandes activos en línea. Recomendamos usar la [Biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) y vincular mediante `href`, lo que ayuda a mantener el mensaje más pequeño.

|   Solo texto   | Texto con imágenes |     Ancho del correo    |
|:-------------:|:----------------:|:------------------:|
| 25&nbsp;KB máximo |   60&nbsp;KB máximo   | 600 píxeles máximo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tamaño del correo electrónico" }

Para reducir el riesgo de recorte:

- Acorta el texto y los enlaces.
- Coloca el CSS crítico en línea donde sea necesario. Elimina los espacios en blanco adicionales en el HTML.
- Comprime las imágenes y los activos HTML.

{% alert note %}
Para guardar tu campaña de correo electrónico o plantilla, asegúrate de que el cuerpo del correo electrónico no supere los 400&nbsp;KB.
{% endalert %}

### ¿Qué puede añadir al tamaño final del correo electrónico? {#what-can-add-to-the-final-email-size}

Estas características aumentan el tamaño del mensaje renderizado en pequeñas cantidades:

- Píxel de seguimiento de apertura: añade una etiqueta de imagen de 1 x 1&nbsp;px al cuerpo del mensaje
- Preencabezado: añade un `<div>` oculto en la parte superior del cuerpo
- Aliasing de enlaces: añade un parámetro de consulta de 16 caracteres (`lid=`) a cada URL rastreada
- Plantillas de enlaces: añade cualquier parámetro de consulta configurado en el dashboard a las URL coincidentes
- CSS en línea (opcional): aplica las reglas de la hoja de estilos incrustada en línea a los elementos HTML, lo que puede añadir CSS redundante dependiendo de la complejidad de la hoja de estilos

El preencabezado y el píxel de seguimiento añaden aproximadamente 600 caracteres (menos de 1&nbsp;KB). Braze normalmente añade entre 0&nbsp;KB y 5&nbsp;KB dependiendo del número de enlaces, la complejidad de la plantilla de enlaces y si el CSS en línea está habilitado. Si el tamaño de tu correo electrónico está cerca del límite, recomendamos probar los correos electrónicos antes de enviarlos, ya que el tamaño final renderizado depende de estos factores.

## Longitud del texto {#text-length}

Consulta la siguiente tabla para conocer las longitudes de texto recomendadas.

| Especificaciones de texto | Propiedades recomendadas |
| --- | --- |
| Longitud de la línea del asunto | 35 caracteres máximo (para una visualización óptima en móvil) (6 a 10 palabras) |
| Longitud del nombre del remitente | 25 caracteres máximo (para una visualización óptima en móvil) |
| Longitud del preencabezado | 85 caracteres máximo |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Longitud del texto" }

## Tamaño de imagen {#image-size}

Consulta la siguiente tabla para conocer los tamaños de imagen recomendados. Las imágenes más pequeñas y de alta calidad se cargan más rápido, así que usa el activo más pequeño posible para lograr el resultado deseado.

|     Tamaño    | Ancho de imagen de encabezado |  Ancho de imagen del cuerpo  |   Tipos de archivo  |
|:-----------:|:------------------:|:------------------:|:-------------:|
| 5&nbsp;MB máximo | 600 píxeles máximo | 480 píxeles máximo | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Tamaño de imagen" }

{% alert note %}
Gmail web y la aplicación móvil de Gmail generalmente no renderizan SVG (y la compatibilidad con WEBP es inconsistente). Usa PNG o JPEG para imágenes que deban mostrarse de forma fiable en Gmail.
{% endalert %}

## Vinculación en profundidad {#deep-linking}

Con las notificaciones push y los In-App Messages, un [vínculo profundo]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls) lleva a los usuarios directamente a un destino específico dentro de una aplicación. Sin embargo, los vínculos profundos requieren que la aplicación esté instalada, y los correos electrónicos no proporcionan una forma de saber si los destinatarios tienen la aplicación. Esto significa que los vínculos profundos en correos electrónicos pueden generar errores para los destinatarios que no tienen la aplicación instalada.

En su lugar, usa [enlaces universales y App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links), que funcionan como URL estándar. Puedes configurarlos para abrir la aplicación o dirigir a los usuarios a una página específica. También pueden redirigir a la tienda de aplicaciones o recurrir a una página web cuando la aplicación no está instalada.

## Content Blocks con imágenes transparentes {#content-blocks-with-transparent-images}

Cuando un Content Block contiene una imagen con fondo transparente (por ejemplo, un logotipo) y se inserta mediante una etiqueta de Liquid, es posible que veas un color de fondo detrás de la imagen. Este color proviene de la [configuración de estilo global del correo electrónico]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings) del editor de arrastrar y soltar, específicamente del **Color de fondo del correo electrónico**. Si tu configuración de estilo global usa un color diferente al blanco, ese color aparecerá en su lugar.

Para mostrar el Content Block como se pretende:

- Establece el color de fondo de la columna del Content Block para que coincida con el fondo del correo electrónico o la plantilla.
- Alternativamente, convierte el Content Block de arrastrar y soltar en un Content Block HTML y establece su fondo como transparente.

Si necesitas usar el mismo Content Block en áreas con diferentes fondos (por ejemplo, cuerpo y pie de página), crea dos versiones del bloque, cada una con el color de fondo de columna apropiado.

Si prefieres arrastrar el Content Block al correo electrónico como una fila, puedes establecer el fondo de la columna de la fila como transparente para anular el fondo global.

{% alert note %}
Arrastrar un Content Block como una fila inserta una instantánea prerenderizada, que no se actualiza automáticamente si el Content Block de origen cambia.
{% endalert %}