---
nav_title: "Pestaña Promociones de Gmail"
article_title: "Pestaña Promociones de Gmail"
page_order: 8
description: "Este artículo de referencia explica cómo utilizar Braze para ayudarte a crear la tarjeta de promociones para móviles de Gmail a partir de tu campaña de correo electrónico."
channel:
  - email
toc_headers: h2
---

# Pestaña Promociones de Gmail {#gmail-promotions-tab}

> La [pestaña Promociones de Gmail para móviles](https://developers.google.com/gmail/promotab/) permite a los especialistas en marketing enviar más información mediante anotaciones en una "tarjeta", en lugar de limitarse a la línea del asunto o a la información del preencabezado. Braze tiene una herramienta integrada que te ayuda a crear la tarjeta a partir de tu campaña de correo electrónico.

## Requisitos previos {#prerequisites}

Primero, envía tus dominios y subdominios al equipo de difusión de la pestaña Promociones de Google a la dirección <a href="mailto:p-promo-outreach@google.com">p-promo-outreach@google.com</a> para añadirlos a la lista de permitidos de Gmail. Esto te permite utilizar cualquier característica que muestre imágenes enriquecidas, como el carrusel de productos de la pestaña Promociones de Gmail.

## Construir la tarjeta con Braze {#build-the-card-with-braze}

Sigue estos pasos para crear una tarjeta promocional de Gmail para una campaña de correo electrónico. Ten en cuenta que al salir de la sección **Contenido** del editor se restablecerán los campos y la información de la pestaña **Gmail Promotion**. Completa la configuración de tu tarjeta promocional y copia el HTML generado para no perder tu código HTML.

### Paso 1: Crea una campaña de correo electrónico {#step-1-create-an-email-campaign}

Primero, [crea tu campaña de correo electrónico]({{site.baseurl}}/user_guide/channels/email/html_editor) y selecciona el **editor de código HTML** como tu experiencia de edición.

### Paso 2: Añade detalles a la tarjeta de promoción de Gmail {#step-2-add-details-to-gmail-promotion-card}

A continuación, ve a la sección **Contenido** del editor HTML y selecciona la pestaña **Gmail Promotion**. Completa los campos en **Basic Information** y luego selecciona **Generate HTML Code**. Esto generará el script para tu tarjeta de la pestaña Promociones de Gmail en la sección **Copy and Paste HTML code into `<Head>`**.

![Un ejemplo de cómo crear una tarjeta.]({% image_buster /assets/img/create-gmail-promo.png %})

### Paso 3: Personaliza tu tarjeta de promoción de Gmail {#step-3-customize-your-gmail-promotion-card}

Elige si deseas incluir una oferta de descuento, tarjeta de oferta, tarjeta de promoción o todas las opciones para tu tarjeta de promoción de Gmail.

{% tabs %}
{% tab Oferta de descuento %}

Configurar una oferta de descuento te permite especificar las fechas válidas para un descuento.

1. Selecciona el interruptor **Discount Offer**.
2. En **Offer**, introduce un breve resumen del descuento. Un ejemplo es "20% off".
3. En **Code**, añade el código promocional que un usuario necesita aplicar al finalizar la compra.
4. Luego, selecciona la fecha y hora de inicio de la oferta de descuento.
5. Determina si la oferta de descuento debe terminar en un momento específico o no terminar nunca.

![Opciones para especificar el valor de la oferta, el código y la fecha y hora de inicio de una oferta de descuento.]({% image_buster /assets/img/gmail_promo_discount_details.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Tarjetas de oferta %}

Usa las tarjetas de oferta para proporcionar información clave de la oferta directamente en la parte superior del cuerpo del correo electrónico. Esto permite a los destinatarios comprender rápidamente los detalles de la oferta y tomar acción. Por ejemplo, puedes usar las tarjetas de oferta para promocionar ofertas por tiempo limitado y reducir la necesidad de que los usuarios busquen detalles dentro de los correos electrónicos.

1. Selecciona el interruptor **Deal Card**.
2. En **Offer**, introduce un breve resumen del descuento. Un ejemplo es "20% off all shoes".
3. (opcional) En **Code**, añade el código promocional que un usuario necesita aplicar al finalizar la compra.
4. Introduce al menos una de las siguientes URL.
-  **Offer Page URL:** La URL de la página de destino específica de la oferta. Esto crea un botón "Shop now" (o similar). Recomendamos proporcionar esta URL para tu tarjeta de oferta.
- **Merchant Homepage URL:** La URL de tu página principal. Usa este campo solo si no hay disponible una URL de página de oferta específica.
5. (opcional) Añade una fecha de inicio para la oferta.
6. Determina si la oferta debe terminar en un momento específico o no terminar nunca.

![Opciones para especificar el valor de la oferta, el código y la fecha y hora de inicio de una tarjeta de oferta.]({% image_buster /assets/img/gmail_promo_deal_cards.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Tarjetas de promoción %}

Las tarjetas de promoción en tu carrusel de productos son útiles para proporcionar imágenes a tu oferta. También puedes personalizar variables en tu carrusel de productos e incluir hasta diez vistas previas de imágenes, donde cada imagen es única.

1. Selecciona el interruptor **Promotion Cards**.
2. Selecciona **Add promotion card**. Cada imagen en tu carrusel de productos debe tener una URL única y usar la misma relación de aspecto (4:5, 1:1, 1.91:1).
3. Incluye una URL de imagen.
4. En **Target URL**, añade el enlace para tu promoción.

{% alert tip %}
Recomendamos cargar las imágenes de tus productos en la Biblioteca de medios y luego copiar y pegar las URL en los campos correspondientes. Solo se aceptan formatos de imagen estáticos (PNG y JPEG). Algunos formatos de imagen (GIF) se cargarán pero no se mostrarán como se espera.
{% endalert %}

{: start="5"}
5. Personaliza tu tarjeta de promoción añadiendo un titular, moneda, precio y valor de descuento.

| Propiedad personalizable | Descripción |
|---|---|
| Titular | (opcional) Una o dos frases de descripción para la promoción. Se muestra debajo de la imagen de vista previa. |
| Moneda | (opcional) La moneda del precio. |
| Precio | El precio de la promoción. |
| Valor de descuento | El monto descontado del precio original. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 3: Personaliza tu tarjeta de promoción de Gmail" }

![Un ejemplo de un carrusel de productos de una empresa llamada Motto con el encabezado de correo electrónico "Our best-selling socks are on sale", con tres imágenes de calcetines y sus precios con descuento.]({% image_buster /assets/img_archive/product_carousel.png %}){: style="max-width:40%;"}

{% endtab %}
{% endtabs %}

### Paso 4: Genera y pega el código HTML {#step-4-generate-and-paste-html-code}

Después de crear tu tarjeta de promoción de Gmail, selecciona **Generate HTML Code**. Copia y pega el script en el elemento `<head>` del HTML de tu correo electrónico.

{% alert tip %}
Para el editor de arrastrar y soltar, copia y pega el código HTML generado en la sección de [etiquetas head personalizadas]({{site.baseurl}}/user_guide/channels/email/drag_and_drop#custom-head-tags) en **Configuración de envío**.
{% endalert %}

{% alert warning %}
El script de Promociones solo aparece si tu correo electrónico llega a la pestaña Promociones de Gmail. Actualmente, Gmail usa algoritmos para determinar dónde llegará tu correo electrónico. Sin embargo, si un usuario alguna vez marca tu correo electrónico como promoción, el algoritmo de Gmail será ignorado y tu correo electrónico llegará automáticamente a la pestaña Promociones en adelante.
{% endalert %}

### Paso 5: Prueba usando la herramienta de vista previa de Gmail {#step-5-test-using-gmails-preview-tool}

Para probar anotaciones en envíos de bajo volumen, debes usar la [herramienta de vista previa](https://developers.google.com/workspace/gmail/promotab/preview) de Gmail para validar las anotaciones primero. Si omites este paso, el carrusel de productos y la vista previa de imagen única solo se activarán con volúmenes de envío más altos.

## Medir las tarjetas de Gmail {#measure-gmail-cards}

Gmail no devuelve análisis sobre estas tarjetas, y los proveedores de servicios de correo electrónico (ESP) como Braze no pueden insertar su propio seguimiento de enlaces en los enlaces de la sección del encabezado (incluidas las tarjetas de promoción y los carruseles de productos). Sin embargo, puedes añadir parámetros UTM o códigos únicos a las URL durante la configuración. Estos parámetros te permiten rastrear la interacción usando los análisis de tu propio sitio web o el seguimiento de conversiones, ya que el seguimiento es parte de la URL en sí, no insertado por el ESP. El seguimiento de clics a nivel de ESP no está disponible para estos enlaces.

### Incorporar imágenes {#incorporate-images}

Gmail ha visto mejores resultados con imágenes impactantes relacionadas con el mensaje del correo electrónico. Gmail no recomienda usar un diseño de solo texto, ya que este espacio fue diseñado para aportar lenguaje visual, que es vital para el marketing por correo electrónico, a la vista previa. No uses imágenes con texto cortado ni repitas imágenes en múltiples campañas.

### Describir ofertas {#describe-offers}

Gmail no sugiere usar oraciones o frases, como "Puedes comprar 1 y llevarte 1 gratis o descuentos en todos los shorts y camisas", ya que puede cortarse, dejar de llamar la atención y competir con la línea del asunto. Este espacio solo debe usarse para captar la atención de tus clientes con tu mensajería, así que evita cualquier lenguaje similar a "Abre este correo electrónico ahora" o "Haz clic aquí para ofertas". Es mejor evitar repetir tu línea del asunto.

## Mejores prácticas {#best-practices}

En general, sigue las [mejores prácticas de la pestaña Promociones de Gmail](https://developers.google.com/gmail/promotab/best-practices).

Al crear tu tarjeta, considera las siguientes preguntas:

- ¿Es válido el script de anotación? [Previsualiza con Google](https://developers.google.com/workspace/gmail/promotab/preview).
- ¿**Show original** en Gmail muestra el script en el mensaje sin procesar?
- ¿El correo electrónico llega a **Promotions**? Las tarjetas solo aplican allí.
- ¿Has probado en escritorio y móvil?

{% alert tip %}
Aunque se admite Liquid en el script, recomendamos probar exhaustivamente para evitar errores.
{% endalert %}

### Previsualizar tu anotación {#preview-your-annotation}

Usa la [herramienta de vista previa](https://developers.google.com/workspace/gmail/promotab/preview) para previsualizar tu anotación. Ten en cuenta que enviarte un correo electrónico de prueba no funcionará para las anotaciones, ya que tu anotación solo se renderiza si el correo electrónico se envía a un número significativo de destinatarios. Asegúrate de enviar el correo electrónico final (con sus URL de imágenes) a al menos 100 destinatarios de Gmail.

No uses Google Workspace para enviar correos electrónicos con anotaciones. Solo usa dominios de correo electrónico en la lista de permitidos para enviar anotaciones a un grupo grande de destinatarios.

### Cumplir con las directrices de imágenes {#adhere-to-image-guidelines}

Verifica que tus imágenes cumplan con estas directrices:
- Usa imágenes de alta calidad y alta resolución.
- Todas las imágenes anotadas deben usar la misma relación de aspecto. Las relaciones de aspecto admitidas incluyen: 4:5, 1:1, 1.91:1.
- Usa tamaños de imagen correctos. El mínimo es 256x256; el máximo es 4096x4096 píxeles.

Gmail recomienda evitar:
- Usar demasiado texto en tus imágenes
- Usar imágenes que sean solo íconos
- Usar imágenes con máscaras redondas
- Usar URL de imágenes personalizadas

### Registrarse con DMARC {#register-with-dmarc}

Para que tus anotaciones se rendericen correctamente, confirma que los dominios enviados estén registrados con DMARC y que todas las políticas estén habilitadas.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cómo añado un logotipo de remitente? {#how-do-i-add-a-sender-logo}

Usa [Google Annotations](https://developers.google.com/workspace/gmail/promotab/overview) para añadir tu logotipo y tarjeta de promoción en la aplicación de Gmail. La renderización es controlada por Gmail, no por Braze.

### ¿Por qué mi mensaje promocional no muestra la tarjeta de promoción o el carrusel de productos en el buzón de entrada del usuario final? {#why-is-my-promotional-message-not-displaying-the-promotion-card-or-product-carousel-in-the-end-users-inbox}

Hay muchos factores que determinan si el carrusel de productos se mostrará en la pestaña Promociones de Gmail.

Todas las imágenes en la anotación aún deben pasar un filtro de calidad. Para que el carrusel de productos se muestre, todas las imágenes en la anotación deben estar en la relación de aspecto de imagen recomendada y ser imágenes de productos en primer plano de alta calidad y alta resolución. Las imágenes deben contener poco o ningún texto. El filtro de calidad también filtra contenido inapropiado, por lo que las imágenes deben ser aptas para toda la familia, usuarios y niños.

Además, Gmail tiene un límite de densidad sobre cuántos carruseles de productos aparecen en la pestaña Promociones de Gmail de un usuario. Por ejemplo, si un usuario está suscrito a muchas marcas que usan carruseles de productos en sus correos electrónicos de promoción, Gmail eventualmente pone un límite en cuántos carruseles de productos se muestran.

Debido a las regulaciones de privacidad y seguridad de Google, los correos electrónicos con anotaciones deben enviarse ampliamente para que la anotación funcione. Se recomienda lanzar una Campaign y enviarla a al menos 100 destinatarios para que el sistema de Google la detecte como un "envío masivo". Las URL de imágenes no pueden variar entre destinatarios.

### ¿Cómo se rastrean los clics en una tarjeta de promoción o carrusel de productos? {#how-are-clicks-on-a-promotion-card-or-product-carousel-tracked}

Ni Braze ni ningún otro ESP pueden insertar seguimiento de enlaces en los enlaces de la sección del encabezado. Esto significa que los clics no se pueden rastrear en una tarjeta de promoción o carrusel de productos.

### ¿Hay alguna forma de ver cuántos usuarios recibieron un carrusel de productos? {#is-there-a-way-to-see-how-many-users-received-a-product-carousel}

Gmail determina cuándo y a quién mostrar la tarjeta, por lo que no hay garantía de que cada destinatario vea el carrusel de productos.

### ¿Por qué no veo anotaciones en mi pestaña Promociones de Gmail? {#why-dont-i-see-annotations-in-my-gmail-promotions-tab}

Las anotaciones no son compatibles con Google Workspace. Para previsualizar anotaciones, puedes crear una dirección de correo electrónico personal con Gmail.

Ten en cuenta que las anotaciones no se renderizan en la pestaña **Primary** ni en ninguna otra pestaña en la aplicación móvil de Gmail. Las anotaciones no se mostrarán después de que un usuario abra un correo electrónico o si estás usando el tipo de anotación `DiscountOffer` y la fecha y hora ya han expirado.

{% alert tip %}
Para más información sobre solución de problemas, consulta la [guía de solución de problemas de Google para promociones por correo electrónico](https://developers.google.com/workspace/gmail/promotab/troubleshooting).
{% endalert %}