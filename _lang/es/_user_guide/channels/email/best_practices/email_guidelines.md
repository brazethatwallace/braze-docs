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

A continuación se ofrecen algunos consejos rápidos que debes tener en cuenta al crear tu contenido:

- Al dar formato a tu correo electrónico, utiliza hojas de estilo en línea como CSS.
- Para usar una plantilla de correo electrónico tanto para versiones de escritorio como móviles, mantén el ancho por debajo de 500 píxeles.
- Las imágenes deben pesar menos de 5&nbsp;MB. Recomendamos utilizar PNG, JPEG o GIF para una compatibilidad máxima. Evita SVG y WebP, ya que muchos clientes de correo electrónico importantes aún no los admiten.
- No establezcas alturas ni anchos para las imágenes, ya que esto puede causar espacios en blanco innecesarios en un correo electrónico degradado.
- No deben usarse etiquetas `div`, ya que la mayoría de los clientes de correo electrónico no admiten su uso. En su lugar, utiliza tablas anidadas.
- Evita usar JavaScript porque no funciona con ningún ESP.
- Evita `position: absolute` y `position: relative` de CSS en las plantillas de correo electrónico. La mayoría de los clientes de correo electrónico no admiten el posicionamiento CSS, lo que causa discrepancias de diseño entre la vista previa de Braze y los correos electrónicos entregados. Usa diseños basados en tablas para lograr efectos de capas o superposición.
- Braze mejora los tiempos de carga utilizando una CDN global para alojar todas las imágenes de correo electrónico.
- En dispositivos móviles, las columnas de imágenes son estrechas (~100 px cada una), por lo que las filas con varias imágenes siguen encajando (por ejemplo, cuatro imágenes ≈ cuatro columnas utilizables).

## Texto alternativo {#alternative-text}

Dado que los filtros de correo no deseado vigilan tanto la versión HTML como la de texto sin formato de un mensaje, utilizar alternativas de texto sin formato es una excelente manera de reducir tu puntuación de correo no deseado. Además, el texto alternativo `(alt="")` puede servir para complementar y, en algunos casos, sustituir las imágenes incluidas en el cuerpo de tu correo electrónico que pueden haber sido filtradas por el proveedor de correo electrónico del usuario. Los lectores de pantalla anuncian el texto alternativo para explicar las imágenes, por lo que esta es una oportunidad para usar un lenguaje sencillo y proporcionar información clave sobre una imagen.

El cliente de correo electrónico del destinatario, no Braze, controla cómo se muestra el texto alternativo. Para obtener más información sobre este comportamiento en clientes como Gmail, Outlook y Apple Mail, consulta [Cómo muestran el texto alternativo los clientes de correo electrónico]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text).

{% alert note %}
Si tu texto alternativo contiene comillas, usa comillas simples (`'`) en lugar de comillas dobles (`"`). Las comillas dobles pueden hacer que el HTML cierre prematuramente el atributo, cortando el texto. Por ejemplo, `alt="Product 'Premium' Edition"` funciona correctamente, pero `alt="Product "Premium" Edition"` se trunca.
{% endalert %}

## Validación de correo electrónico {#email-validation}

{% alert important %}
La validación se utiliza para las direcciones de correo electrónico del panel, las direcciones de correo electrónico de los usuarios finales (tus clientes) y las direcciones de remitente y responder a de un mensaje de correo electrónico.
{% endalert %}

La validación de correo electrónico ocurre cuando la dirección de correo electrónico de un usuario se actualiza o se importa a Braze mediante la API, la carga de CSV, el SDK, o se modifica en el panel. Ten en cuenta que las direcciones de correo electrónico no pueden incluir espacios en blanco, y si se envían a través de la API, los espacios en blanco pueden generar un error `400`.

Las direcciones de correo electrónico dirigidas a través de los servidores de Braze deben validarse según los estándares [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822). Braze no acepta ciertos caracteres y los reconoce como no válidos. Si un correo electrónico rebota, Braze marca el correo electrónico como no válido y el estado de suscripción no se modifica.

Para obtener información sobre los caracteres no permitidos y las reglas de validación de correo electrónico, consulta [Validación de correo electrónico]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation#how-it-works).

## Direcciones de remitente y responder a {#from-and-reply-to-addresses}

Al configurar tus direcciones de remitente, asegúrate de que el dominio de correo electrónico del remitente coincida con tu dominio de envío (como `marketing.yourdomain.com`). No hacerlo puede provocar una desalineación de SPF y DKIM. Todas las direcciones de responder a pueden configurarse en tu dominio raíz.

{% alert note %}
La codificación Unicode no es compatible en las direcciones de remitente.
{% endalert %}


### Dominios de envío y correo entrante {#sending-domains-and-inbound-mail}

Braze solo entrega correo electrónico saliente. Los dominios y subdominios de envío se configuran para la capacidad de entrega (SPF, DKIM y registros de DNS relacionados), pero no son buzones de entrada.

No puedes reenviar respuestas enviadas a un subdominio de envío a un buzón de entrada personal a través de Braze. Para recibir respuestas de los usuarios, configura una dirección de responder a independiente en un dominio que controles con un buzón de entrada. Consulta [Direcciones de remitente y responder a](#from-and-reply-to-addresses).

## Archivos adjuntos en correo electrónico {#attachments}

Cuando añadas archivos adjuntos a los mensajes de correo electrónico, sigue estas prácticas recomendadas de capacidad de entrega:

- Los filtros de correo no deseado analizan los archivos adjuntos y pueden marcar tu mensaje.
- Los proveedores de correo a veces tardan más en aceptar mensajes que incluyen archivos adjuntos.
- Fuera de los mensajes individuales, los archivos adjuntos pueden hacer que tu mensaje parezca sospechoso en el buzón de entrada.
- Mantén cada archivo adjunto por debajo de 2&nbsp;MB.
- No envíes información confidencial como archivo adjunto. En su lugar, dirige a los usuarios a tu portal seguro para que la consulten allí.

## Diseño (arrastrar y soltar y HTML personalizado) {#layout-drag-and-drop-and-custom-html}

El diseño puede fallar cuando el HTML/CSS generado por Braze entra en conflicto con el HTML personalizado. Si esto ocurre, haz lo siguiente:

- Elimina primero el HTML/CSS personalizado
- Valida que las fuentes personalizadas se carguen correctamente en la vista previa
- Comprueba el relleno de filas y columnas
- Usa diseños basados en tablas y no excedas el ancho del editor.

Los Content Blocks que incorporan HTML desde fuera del editor también pueden romper el diseño.

## Parámetros UTM en URLs de correo electrónico {#utm-parameters-in-email-urls}

Los parámetros UTM etiquetan las URL para análisis. Puedes construirlos con Liquid y atributos personalizados.

- Usa solo un signo de interrogación `?` en la URL final (los caracteres `?` adicionales pueden interrumpir las solicitudes).
- Evita espacios y caracteres especiales en los valores (usa `_` o `-`).
- Confirma que tu herramienta de análisis procesa los UTM. Elimina los espacios finales dentro de los bloques Liquid `capture`. Los UTM distinguen entre mayúsculas y minúsculas.

### Revisa los detalles del HTML {#check-html-details}

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

## Solución de problemas de correos electrónicos duplicados {#troubleshooting-duplicate-emails}

Si los usuarios informan que reciben correos electrónicos duplicados, los siguientes escenarios pueden ayudarte a identificar la causa:

### Error de configuración en la creación de la Campaign o Canvas {#configuration-error-at-campaign-or-canvas-creation}

Es posible que los usuarios no reciban el mismo correo electrónico dos veces, sino que reciban dos correos electrónicos separados con la misma línea del asunto. Cuando se duplica una Campaign o un Canvas, es fácil pasar por alto detalles básicos de la configuración del correo electrónico, como las imágenes o la línea del asunto.

Para investigar:

1. Revisa el perfil de usuario y examina cada Canvas y Campaign que el usuario recibió.
2. Revisa los registros de cambios para ver si la Campaign o el Canvas se modificaron después del lanzamiento. Es posible que la Campaign o el Canvas tuvieran la misma línea del asunto que el original cuando el usuario lo recibió.

### Campaign enviada varias veces {#campaign-sent-multiple-times}

Si el número de mensajes enviados es significativamente mayor que el número de usuarios en la audiencia, esto puede indicar que la Campaign se lanzó varias veces.

Para obtener más información sobre cómo Braze gestiona las direcciones de correo electrónico duplicadas y la deduplicación, consulta las [preguntas frecuentes sobre correo electrónico]({{site.baseurl}}/user_guide/channels/email/faq#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address).