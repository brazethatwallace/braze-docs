---
nav_title: "AMP para correo electrónico"
article_title: "AMP para correo electrónico"
alias: /amphtml/
page_order: 11
description: "Este artículo de referencia ofrece un resumen de AMP para correo electrónico y casos de uso comunes."
channel:
  - email

---

# AMP para correo electrónico {#amp-for-email}

> Con [AMP para correo electrónico](https://amp.dev/about/email), puedes añadir elementos interactivos a tus correos electrónicos y mejorar las comunicaciones con tus clientes, ofreciendo una experiencia completa directamente en el buzón de entrada de tu usuario. AMP lo hace posible mediante el uso de varios componentes que pueden utilizarse para crear ofertas de correo electrónico atractivas, como cuestionarios, formularios de opinión, campañas de votación, reseñas, centros de suscripción y mucho más. Herramientas como estas pueden ofrecer oportunidades para aumentar la interacción y la retención.

## Requisitos {#requirements}

Braze no es responsable de que los usuarios se registren en Google ni de que cumplan los requisitos de seguridad necesarios. AMP para correo electrónico solo está disponible para SparkPost y SendGrid.

| Requisito   | Descripción |
| --------------| ----------- |
| AMP para correo electrónico activado | AMP está disponible para todos los usuarios. |
| Habilitación de cuenta de Gmail | Consulta [Habilitar cuenta de Gmail](#enabling-gmail-account). |
| Autenticación de remitente de Google | Gmail [autentica al remitente](https://developers.google.com/gmail/ampemail/security-requirements#sender_authentication) de los correos electrónicos AMP con DKIM, SPF y DMARC. Estos deben estar configurados para tu cuenta. <br><br>- [Domain Keys Identified Mail](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) (DKIM) <br>- [Sender Policy Framework](https://en.wikipedia.org/wiki/Sender_Policy_Framework)(SPF)<br>- [Domain-based Message Authentication, Reporting, and Conformance](https://en.wikipedia.org/wiki/DMARC)(DMARC)
| Elementos de correo electrónico AMP | Un correo electrónico AMP atractivo incluye el uso estratégico de varios componentes. Consulta la pestaña Esenciales en la sección [Componentes](#components) a continuación. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

### Clientes de correo electrónico compatibles {#supported-email-clients}

Antes de poder enviar correos electrónicos AMP a los usuarios, debes registrarte con nuestros clientes de correo electrónico. El proceso de registro implica enviar un correo electrónico de prueba en AMP HTML para obtener la aprobación. Los tiempos de aprobación varían según el cliente. Sigue los enlaces de registro para obtener más información.

| Cliente | Enlace de registro |
| ------ | -------- |
| Gmail | [Google](https://developers.google.com/gmail/ampemail/register) |
| FairEmail | [FairEmail](https://email.faircode.eu/) |
| Yahoo | [Yahoo](https://senders.yahooinc.com/amp/) |
| Mail.ru | [Mail.ru](https://postmaster.mail.ru/amp/) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Clientes de correo electrónico compatibles" }

Para obtener una lista completa de clientes de correo electrónico compatibles, consulta la [documentación de AMP](https://amp.dev/support/faq/email-support).

### Habilitar cuenta de Gmail {#enabling-gmail-account}

Ve a la configuración de Gmail y selecciona **Enable dynamic email** en la pestaña **General**.

![Un ejemplo de la configuración de Gmail con la casilla "Enable dynamic email" seleccionada.]({% image_buster /assets/img/dynamic-content.png %})

## Uso de la API {#api-usage}

También puedes usar AMP para correo electrónico con nuestra API. Si utilizas cualquiera de los [puntos de conexión de mensajería]({{site.baseurl}}/api/endpoints/messaging) de Braze para enviar un correo electrónico, añade `amp_body` como especificación de objeto como se muestra a continuación.

### Especificación del objeto de correo electrónico {#email-object-specification}

```json
{
  "app_id": (required, string) see app identifier above,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <user@example.com>"),
  "reply_to": (optional, valid email address in the format "user@example.com" - defaults to your workspace's default reply to if not set),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "amp_body": (optional, updates the text-amp-html MIME type) the email body in AMP HTML. The MIME (Multipurpose Internet Mail Extensions) type to be referenced is "text/x-amp-html",
  "body": (required unless email_template_id is given, valid HTML),
  "preheader": (optional*, string) Recommended length 50-100 characters,
  "email_template_id": (optional, string) If provided, we will use the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case we will override the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid key-value hash), extra hash - for SendGrid customers, this will be passed to SendGrid as Unique Arguments,
  "headers": (optional, valid key-value hash), hash of custom extensions headers. Currently, only supported for SendGrid customers,
  "should_inline_css": (optional, boolean), whether to inline CSS on the body. If not provided, falls back to the default CSS inlining value for the workspace,
  "attachments": (optional, array), array of JSON objects like [{"file_name","url"}] that define the files you need attached. Your file name's extension will be detected automatically from the URL, which should return the appropriate `Content-Type` as a response header,
}
```

## Crear tu correo electrónico AMP {#create-your-amp-email}

Primero, crea tu correo electrónico AMP usando [componentes](#components). A continuación, usa la [API de Braze](#api-usage) para enviar tu mensaje, asegurándote de incluir `amp_body` para tu AMP HTML.

Además del AMP HTML, requerimos una versión HTML regular del `body` y sugerimos una versión `plaintext_body` de tu correo electrónico AMP. Todos los correos electrónicos AMP se envían en formato multipart, lo que significa que Braze envía un correo electrónico que admite HTML, texto plano y AMP HTML. Esto resulta útil en caso de que tu correo electrónico se envíe a través de un proveedor que aún no admita AMP para correo electrónico, ya que el correo electrónico se ajustará automáticamente a la versión apropiada según el usuario y su dispositivo.

{% alert note %}
Cuando estés creando un correo electrónico AMP, comprueba que estás en el editor AMP, ya que el código AMP no debe añadirse al editor HTML.
{% endalert %}

Consulta estos recursos adicionales:

- [Tutorial de AMP](https://amp.dev/documentation/guides-and-tutorials/start/create_email?format=email)
- [Código de ejemplo](https://gist.github.com/CrystalOnScript/988c3f0a2eb406da27e9d9bf13a8bf73) para ver cómo debería lucir el producto final.
- [Biblioteca de componentes de correo electrónico AMP](https://amp.dev/documentation/components/?format=email/)

### Componentes {#components}

Al crear los elementos AMP, te recomendamos consultar con tu equipo de ingeniería e incluir recursos y elementos de diseño para un nivel adicional de acabado.

{% tabs %}
  {% tab Esenciales %}

Cada uno de estos elementos es obligatorio en el cuerpo de tu correo electrónico AMP.

| Componente | Descripción | Ejemplo |
|---------|--------------|---------|
| Identificación <br><br> `⚡4email` o `amp4email`| Identifica tu correo electrónico como un correo electrónico AMP HTML. | `<!doctype html>` <br> `<html ⚡4email>` <br> `<head>` |
| Cargar el runtime de AMP <br><br> `<script>` | Permite que AMP se ejecute en tu correo electrónico usando JavaScript. | `<script async src="https://cdn.ampproject.org/v0.js"></script>`|
| Plantilla CSS | Oculta el contenido hasta que AMP se haya cargado. <br> Los proveedores de correo electrónico que admiten correos electrónicos AMP aplican comprobaciones de seguridad que solo permiten la ejecución de scripts AMP verificados en sus clientes. | `<style amp4email-boilerplate>body{visibility:hidden}</style>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Componentes" }

  {% endtab %}
  {% tab Dinámicos %}

Usa estos componentes para crear diseños y comportamientos dinámicos en tus correos electrónicos.

| Componente | Descripción | Script requerido |
|---------|--------------|---------|
| [Acordeón](https://amp.dev/documentation/components/amp-accordion?format=email) <br><br> `amp-accordion`| Permite a los usuarios ver el esquema del contenido y saltar a cualquier sección. | `<script async custom-element="amp-accordion" src="https://cdn.ampproject.org/v0/amp-accordion-0.1.js"></script>` |
| [Formularios](https://amp.dev/documentation/components/amp-form?format=email) <br><br> `amp-form`| Crea formularios para enviar campos de entrada en un documento AMP. | `<script async custom-element="amp-form" src="https://cdn.ampproject.org/v0/amp-form-0.1.js"></script>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Componentes" }

{% alert note %}
Cualquier componente que requiera autenticar al usuario debe usar [tokens de acceso de Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) o [tokens de aserción proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}
  {% endtab %}
  {% tab Creativos %}

  Dale un toque especial con los componentes de AMP que pueden ayudarte a adaptar tu correo electrónico a tu audiencia.

| Componente | Descripción | Script requerido |
|---------|--------------|---------|
| [Imagen animada](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-anim`| Muestra una imagen animada (generalmente un GIF) gestionada a través del runtime. | `<script async custom-element="amp-anim" src="https://cdn.ampproject.org/v0/amp-anim-0.1.js"></script>` |
| [Carrusel](https://amp.dev/documentation/components/amp-carousel?format=email) <br><br> `amp-carousel`| Muestra múltiples piezas de contenido similares a lo largo de un eje horizontal. | `<script async custom-element="amp-carousel" src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>` |
| [Imagen](https://amp.dev/documentation/components/amp-img?format=email) | Un reemplazo gestionado por el runtime para la etiqueta HTML `img`. <br>  También puedes crear un [lightbox para tu imagen](https://amp.dev/documentation/components/amp-image-lightbox?format=email). | `<amp-img alt="A view of the sea"` <br> `src="images/sea.jpg"` <br> `width="900"` <br>  `height="675"` <br>  `layout="responsive">`  <br> `</amp-img>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Componentes" }

{% alert note %}
Cualquier componente que requiera autenticar al usuario debe usar [tokens de acceso de Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) o [tokens de aserción proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}

  {% endtab %}
  {% tab Otros %}

| Componente | Descripción |
|---------|--------------|
| [Enlace de datos y expresiones](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-bind`| Añade interactividad personalizada con estado a tus páginas AMP mediante enlace de datos y expresiones similares a JavaScript. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Componentes" }

{% alert note %}
Cualquier componente que requiera autenticar al usuario debe usar [tokens de acceso de Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) o [tokens de aserción proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}

{% endtab %}
{% endtabs %}

Para obtener una lista completa de componentes AMP, consulta la [documentación de AMP](https://amp.dev/documentation/components/?format=email).

### Casos de uso {#use-cases}

{% tabs local %}
{% tab Cuestionarios interactivos %}

Usando el componente `<amp-form>`, puedes crear cuestionarios interactivos que se pueden completar sin salir del buzón de entrada del correo electrónico. Esto se puede hacer usando `<amp-form>` para enviar la respuesta del cuestionario y luego hacer que tu backend proporcione estos datos agregados.

Algunos ejemplos incluyen:
* Correo electrónico de cuestionario de conferencia
* Actualización dinámica de elementos en la fuente
* Correo electrónico de marcadores de artículos

Usando este componente, los usuarios pueden enviar o borrar valores de campos. Además, dependiendo de cómo configures tu correo electrónico, puedes dar indicaciones adicionales a los usuarios, como si el envío del cuestionario fue exitoso o no, o mostrar las respuestas de tus usuarios con los resultados del cuestionario (como una campaña de votación).

{% endtab %}
{% tab Contenido plegable %}

Amplía las secciones de tu contenido usando el componente `<amp-accordion>`. Este componente te permite mostrar secciones de contenido plegables y expandibles, proporcionando una forma para que los lectores echen un vistazo al esquema del contenido y salten a cualquier sección.

Si sueles enviar artículos educativos largos o recomendaciones personalizadas, esto proporciona una forma para que los lectores echen un vistazo al esquema del contenido y salten a cualquier sección o recomendación de productos específica para obtener más detalles. Esto puede ser particularmente útil para usuarios móviles, donde incluso unas pocas frases en una sección requieren desplazamiento.
{% endtab %}
{% tab Correos electrónicos con muchas imágenes %}

Si sueles enviar correos electrónicos con muchas fotos profesionales, como las marcas de comercio minorista, puedes usar el componente `<amp-image-lightbox>` que permite a los usuarios interactuar con una imagen que les resulte atractiva. Cuando el usuario hace clic en la imagen, este componente muestra la imagen en el centro del mensaje creando un efecto lightbox.

Además, el componente `<amp-image-lightbox>` permite al usuario ver una descripción detallada de la imagen. Puedes usar el mismo componente para más de una imagen. Por ejemplo, si tienes varias imágenes incluidas en tu correo electrónico, cuando el usuario haga clic en cualquiera de ellas, la imagen se mostrará en el lightbox.

{% endtab %}
{% tab Correos electrónicos basados en texto %}

Para correos electrónicos que dependen principalmente de texto, el componente `<amp-fit-text>` te permite gestionar el tamaño y el ajuste del texto dentro de un área especificada.

Los ejemplos incluyen:

- Escalar el texto para que se ajuste a un área
- Escalar el texto para que se ajuste al área usando un tamaño de fuente máximo, donde puedes establecer el tamaño de fuente máximo
- Truncar el texto cuando el contenido desborda el área

{% endtab %}
{% endtabs %}

### Uso de amp-mustache {#use-amp-mustache}

De forma similar a Liquid, AMP admite un lenguaje de scripting para casos de uso más avanzados. Este componente se llama [`amp-mustache`](https://amp.dev/documentation/components/amp-mustache/?format=email). Al incluir cualquier lenguaje de marcado Mustache, necesitarás envolverlo con la etiqueta [`raw`](https://shopify.github.io/liquid/tags/raw/) de Liquid. Ten en cuenta que Liquid y Mustache comparten estilos de sintaxis.

Al envolver tu contenido con la etiqueta `raw`, el motor de procesamiento de Braze ignorará cualquier contenido entre las etiquetas `raw` y enviará la variable Mustache que tu equipo necesita.

## Métricas y análisis {#metrics-and-analytics}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Métricas y análisis">
  <caption>Métricas y análisis</caption>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Detalles</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">Total Opens</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Opens' %} Para correos electrónicos AMP, este es el total de aperturas de las versiones HTML y texto plano.</td>
        </tr>
        <tr>
            <td class="no-split">Total Clicks</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Clicks' %} Para correos electrónicos AMP, este es el total de clics en las versiones HTML y texto plano.</td>
        </tr>
        <tr>
            <td class="no-split">AMP Opens</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='AMP Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split">AMP Clicks</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='AMP Clicks' %}</td>
        </tr>
    </tbody>
</table>

## Pruebas y solución de problemas {#test-and-troubleshoot}


Antes de enviar tu correo electrónico AMP, te recomendamos:

- Realizar pruebas según estas [directrices de Gmail](https://developers.google.com/gmail/ampemail/testing-dynamic-email).
- Usar el [Gmail AMP for Email Playground](https://amp.gmail.dev/playground/) para validar el marcado AMP.
  - Si tu correo electrónico AMP usa etiquetas de Liquid, reemplázalas con valores estáticos de marcador de posición antes de pegarlas en el Gmail AMP for Email Playground. Las etiquetas de Liquid sin renderizar provocan errores de validación.

Para que tu correo electrónico AMP se entregue a cualquier cuenta de Gmail, el correo electrónico debe cumplir las siguientes condiciones:

- Se deben cumplir los requisitos de seguridad de AMP para correo electrónico.
- La parte MIME de AMP debe contener un documento AMP válido.
- El correo electrónico debe incluir la parte MIME de AMP antes de la parte MIME de HTML.
- La parte MIME de AMP debe ser menor de 100&nbsp;KB.

Ten en cuenta que los clics totales y los clics únicos no tienen en cuenta los clics que ocurren desde un mensaje AMP (solo HTML y texto plano). Los clics específicos de AMP se atribuyen a la métrica *amp_click*.

Si ninguna de estas condiciones está causando el error, ponte en contacto con [Soporte]({{site.baseurl}}/support_contact).

### Configurar el buzón de entrada de Gmail para renderizar correos electrónicos AMP {#configure-gmail-inbox-to-render-amp-emails}

Puedes configurar tu buzón de entrada de Gmail para renderizar correos electrónicos AMP con fines de prueba haciendo lo siguiente:

1. En Gmail, selecciona **Settings** en la esquina superior derecha de tu buzón de entrada.
2. Selecciona **See all settings**.
3. En la pestaña **General**, ve a la sección **Dynamic email** y confirma que la casilla **Enable dynamic email** está seleccionada.
4. A continuación, selecciona **Developer Settings** y marca la casilla **Always allow dynamic emails from this sender:**.
5. Introduce el mismo dominio que aparece en la dirección De de tu mensaje de prueba.
6. Guarda los cambios.

Ahora puedes enviar el correo electrónico de prueba a tu cuenta de Gmail, y los correos electrónicos AMP deberían renderizarse en Gmail.

### Preguntas frecuentes {#frequently-asked-questions}

#### ¿Debería segmentar con correos electrónicos AMP? {#should-i-segment-with-amp-emails}

Recomendamos no segmentar para enviar a todos los diferentes tipos de usuarios. Esto se debe a que enviamos los mensajes AMP en formato multipart, incluyendo diferentes versiones en el correo electrónico original. Si un usuario no puede ver la versión AMP, se mostrará por defecto la versión HTML.