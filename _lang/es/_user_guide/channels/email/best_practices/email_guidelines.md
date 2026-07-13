---
nav_title: "Directrices de correo electrónico"
article_title: "Directrices de correo electrónico"
page_order: 1
page_type: reference
description: "Este artículo cubre consejos generales y trucos a tener en cuenta al crear campañas de correo electrónico para diversos casos de uso y temas."
channel: email

---

# Directrices de correo electrónico {#email-guidelines}

> Al crear tu campaña de correo electrónico, es importante tener en cuenta cómo tus mensajes de correo electrónico son recibidos por tus distintos usuarios y proveedores de servicios de correo electrónico (ESP).

## General {#general}

Aquí tienes algunos consejos rápidos a tener en cuenta mientras construyes tu contenido:

- Al dar formato a tu correo electrónico, utiliza hojas de estilo en línea como CSS.
- Para usar una sola plantilla de correo electrónico tanto para versiones móviles como de escritorio, mantén el ancho por debajo de 500 píxeles.
- Las imágenes deben pesar menos de 5&nbsp;MB. Recomendamos usar PNG, JPEG o GIF para máxima compatibilidad. Evita SVG y WebP, ya que muchos clientes de correo electrónico importantes aún no los admiten.
- No establezcas alturas y anchos para las imágenes, ya que esto puede causar espacios en blanco innecesarios en un correo electrónico degradado.
- No se deben usar etiquetas `div`, ya que la mayoría de los clientes de correo electrónico no admiten su uso. En su lugar, utiliza tablas anidadas.
- Evita usar JavaScript porque no funciona con ningún ESP.
- Braze mejora los tiempos de carga utilizando un CDN global para alojar todas las imágenes de correo electrónico.
- En dispositivos móviles, las columnas de imágenes son estrechas (~100px cada una), por lo que las filas con múltiples imágenes siguen encajando (por ejemplo, cuatro imágenes ≈ cuatro columnas utilizables).

## Texto alternativo {#alternative-text}

Dado que los filtros de correo no deseado verifican tanto la versión HTML como la versión de texto plano de un mensaje, utilizar alternativas de texto plano es una excelente manera de reducir tu puntuación de correo no deseado. Además, el texto alternativo `(alt="")` puede servir para complementar y, en algunos casos, sustituir las imágenes incluidas en el cuerpo de tu correo electrónico que pueden haber sido filtradas por el proveedor de correo electrónico del usuario. Los lectores de pantalla anuncian el texto alternativo para explicar las imágenes, por lo que esta es una oportunidad para usar un lenguaje sencillo y proporcionar información clave sobre una imagen.

## Validación de correo electrónico {#email-validation}

{% alert important %}
La validación se utiliza para las direcciones de correo electrónico del dashboard, las direcciones de correo electrónico de los usuarios finales (tus clientes) y las direcciones de remitente y responder a de un mensaje de correo electrónico.
{% endalert %}

La validación de correo electrónico ocurre cuando la dirección de correo electrónico de un usuario se actualiza o se importa a Braze mediante la API, carga de CSV, SDK, o se modifica en el dashboard. Ten en cuenta que tus direcciones de correo electrónico no pueden incluir espacios en blanco, y si se envían mediante la API, los espacios en blanco pueden resultar en un error `400`.

Las direcciones de correo electrónico dirigidas a través de los servidores de Braze deben validarse según los estándares [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822). Braze no acepta ciertos caracteres y los reconoce como no válidos. Si un correo electrónico rebota, Braze marca el correo electrónico como no válido y el estado de suscripción no se modifica.

Para obtener información sobre los caracteres no permitidos y las reglas de validación de correo electrónico, consulta [Validación de correo electrónico]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation#how-it-works).

## Direcciones de remitente y responder a {#from-and-reply-to-addresses}

Al configurar tus direcciones de remitente, asegúrate de que el dominio del correo electrónico de remitente coincida con tu dominio de envío (como `marketing.yourdomain.com`). No hacerlo puede resultar en una desalineación de SPF y DKIM. Todas las direcciones de responder a pueden configurarse con tu dominio raíz.

{% alert note %}
La codificación Unicode no es compatible en las direcciones de remitente.
{% endalert %}

## Archivos adjuntos en correo electrónico {#attachments}

Cuando añadas archivos adjuntos a los mensajes de correo electrónico, sigue estas prácticas recomendadas de capacidad de entrega:

- Los filtros de correo no deseado analizan los archivos adjuntos y pueden marcar tu mensaje.
- Los proveedores de correo a veces tardan más en aceptar mensajes que incluyen archivos adjuntos.
- Fuera de los mensajes individuales, los archivos adjuntos pueden hacer que tu mensaje parezca sospechoso en el buzón de entrada.
- Mantén cada archivo adjunto por debajo de 2&nbsp;MB.
- No envíes información confidencial como archivo adjunto. En su lugar, dirige a los usuarios a tu portal seguro para que la consulten allí.

## Diseño (arrastrar y soltar y HTML personalizado) {#layout-drag-and-drop-and-custom-html}

El diseño puede romperse cuando el HTML/CSS generado por Braze entra en conflicto con el HTML personalizado. Si esto ocurre, haz lo siguiente:

- Elimina primero el HTML/CSS personalizado.
- Valida que las fuentes personalizadas se carguen correctamente en la vista previa.
- Verifica el relleno de filas y columnas.
- Prefiere diseños basados en tablas y mantente dentro del ancho del editor.

Los Content Blocks que incorporan HTML externo al editor también pueden romper el diseño.

## Parámetros UTM en URLs de correo electrónico {#utm-parameters-in-email-urls}

Los parámetros UTM etiquetan URLs para análisis. Puedes construirlos con Liquid y atributos personalizados.

- Usa solo un signo de interrogación `?` en la URL final (los caracteres `?` adicionales pueden romper las solicitudes).
- Evita espacios y caracteres especiales en los valores (usa `_` o `-`).
- Confirma que tu herramienta de análisis ingiere los UTM. Elimina los espacios finales dentro de los bloques Liquid `capture`. Los UTM distinguen entre mayúsculas y minúsculas.

### Verificar los detalles del HTML {#check-html-details}

Ten en cuenta que algunas etiquetas y atributos HTML no están permitidos, ya que podrían permitir que código malicioso se ejecute en el navegador.

Consulta las siguientes listas de etiquetas y atributos HTML que no están permitidos en tus correos electrónicos:
{% details Expandir para ver las etiquetas HTML no permitidas %}
- `<!doctype>`
- `<applet>`
- `<bgsound>`
- `<embed>`
- `<frameset>`
- `iframe`
- `<ilayer>`
- `<layer>`
- `<link>`
- `<meta>`
- `<object>`
- `<script>`
- `<title>`
- `<xml>`
- `<svg>`
{% enddetails %}

{% details Expandir para ver los atributos HTML no permitidos %}
- `<animationend>`
- `<animationiteration>`
- `<animationstart>`
- `<data-bind>`
- `<fscommand>`
- `<onabort>`
- `<onabort>`
- `<onactivate>`
- `<onafterprint>`
- `<onafterupdate>`
- `<onbeforeactivate>`
- `<onbeforecopy>`
- `<onbeforecut>`
- `<onbeforedeactivate>`
- `<onbeforeeditfocus>`
- `<onbeforepaste>`
- `<onbeforeprint>`
- `<onbeforeunload>`
- `<onbeforeupdate>`
- `<onbegin>`
- `<onblur>`
- `<onbounce>`
- `<oncanplay>`
- `<oncanplaythrough>`
- `<oncellchange>`
- `<onchange>`
- `<onclick>`
- `<oncontextmenu>`
- `<oncontrolselect>`
- `<oncopy>`
- `<oncut>`
- `<ondataavailable>`
- `<ondatasetchanged>`
- `<ondatasetcomplete>`
- `<ondblclick>`
- `<ondeactivate>`
- `<ondrag>`
- `<ondragdrop>`
- `<ondragend>`
- `<ondragenter>`
- `<ondragleave>`
- `<ondragover>`
- `<ondragstart>`
- `<ondrop>`
- `<ondurationchange>`
- `<onemptied>`
- `<onend>`
- `<onended>`
- `<onerror>`
- `<onerror>`
- `<onerrorupdate>`
- `<onfilterchange>`
- `<onfinish>`
- `<onfocus>`
- `<onfocusin>`
- `<onfocusout>`
- `<onhashchange>`
- `<onhelp>`
- `<oninput>`
- `<oninvalid>`
- `<onkeydown>`
- `<onkeypress>`
- `<onkeyup>`
- `<onlayoutcomplete>`
- `<onload>`
- `<onloadeddata>`
- `<onloadedmetadata>`
- `<onloadstart>`
- `<onlosecapture>`
- `<onmediacomplete>`
- `<onmediaerror>`
- `<onmessage>`
- `<onmousedown>`
- `<onmouseenter>`
- `<onmouseleave>`
- `<onmousemove>`
- `<onmouseout>`
- `<onmouseover>`
- `<onmouseup>`
- `<onmousewheel>`
- `<onmove>`
- `<onmoveend>`
- `<onmovestart>`
- `<onoffline>`
- `<ononline>`
- `<onopen>`
- `<onoutofsync>`
- `<onpagehide>`
- `<onpageshow>`
- `<onpaste>`
- `<onpause>`
- `<onplay>`
- `<onplaying>`
- `<onpopstate>`
- `<onprogress>`
- `<onpropertychange>`
- `<onratechange>`
- `<onreadystatechange>`
- `<onredo>`
- `<onrepeat>`
- `<onreset>`
- `<onresize>`
- `<onresizeend>`
- `<onresizestart>`
- `<onresume>`
- `<onreverse>`
- `<onrowdelete>`
- `<onrowexit>`
- `<onrowinserted>`
- `<onrowsenter>`
- `<onscroll>`
- `<onsearch>`
- `<onseek>`
- `<onseeked>`
- `<onseeking>`
- `<onselect>`
- `<onselectionchange>`
- `<onselectstart>`
- `<onshow>`
- `<onstalled>`
- `<onstart>`
- `<onstop>`
- `<onstorage>`
- `<onsubmit>`
- `<onsuspend>`
- `<onsyncrestored>`
- `<ontimeerror>`
- `<ontimeupdate>`
- `<ontoggle>`
- `<ontouchcancel>`
- `<ontouchend>`
- `<ontouchmove>`
- `<ontouchstart>`
- `<ontrackchange>`
- `<onundo>`
- `<onunload>`
- `<onurlflip>`
- `<onvolumechange>`
- `<onwaiting>`
- `<onwheel>`
- `<seeksegmenttime>`
- `<transitionend>`
{% enddetails %}