---
nav_title: Normativa sobre correo no deseado
article_title: Normativa sobre correo no deseado
page_order: 0
page_type: reference
description: "Este artículo ofrece resúmenes y recursos sobre diversas normativas en materia de correo no deseado que pueden afectarte a ti o a tus usuarios."
channel:
- email
- push
- SMS

---

# Normativa sobre correo no deseado {#spam-regulations}

> Hay una serie de leyes que regulan a los remitentes de comunicaciones electrónicas, incluidos el correo electrónico, las notificaciones push y los SMS. Siempre debes conocer las [normativas locales](https://en.wikipedia.org/wiki/Email_spam_legislation_by_country) que puedan afectarte a ti o a tus usuarios.

Braze proporciona información relevante basada en nuestra propia investigación, pero también debes consultar el texto completo de estas leyes para obtener detalles completos y actualizados.

- [CAN-SPAM](#can-spam)
- [Ley canadiense contra el correo no deseado](#casl)

## CAN-SPAM {#can-spam}

La Ley CAN-SPAM de 2003 regula a los remitentes de correo electrónico en EE. UU. que envíen "cualquier mensaje de correo electrónico cuyo propósito principal sea la publicidad comercial o la promoción de un producto o servicio comercial". Puedes obtener más información en el sitio web oficial de la [Comisión Federal de Comercio](http://www.business.ftc.gov/documents/bus61-can-spam-act-compliance-guide-business).

Hay siete requisitos clave para CAN-SPAM:

1. No utilices información falsa o engañosa en el encabezado (como "De", "Para" y "Responder a")
2. No utilices líneas de asunto engañosas
3. Identifica el mensaje como un anuncio
4. Indica a los destinatarios dónde te encuentras (por ejemplo, tu dirección física)
5. Indica a los destinatarios cómo cancelar la suscripción para dejar de recibir correos electrónicos tuyos en el futuro
6. Atiende las solicitudes de cancelación de suscripción con prontitud
7. Supervisa lo que otros hacen en tu nombre

Los correos electrónicos transaccionales están exentos de estas reglas, con la excepción del punto n.º 1.

## Ley canadiense contra el correo no deseado (CASL) {#casl}

El 1 de julio de 2014, la Ley canadiense contra el correo no deseado (CASL) entró en vigor para los correos electrónicos enviados a residentes canadienses. Puedes leer el texto completo de la ley en el [sitio web de leyes de justicia](http://laws-lois.justice.gc.ca/eng/annualstatutes/2010_23/FullText.html) del Gobierno de Canadá. La ley establece esencialmente que los destinatarios canadienses tanto de correo electrónico como de notificaciones push deben proporcionar un consentimiento "expreso o implícito" para que te comuniques con ellos.

### CASL frente a CAN-SPAM {#casl-versus-can-spam}

Hay un par de diferencias clave entre CASL y CAN-SPAM, sobre todo:

- CASL se aplica en función de dónde se recibe el mensaje, por lo que los remitentes fuera de Canadá también se ven afectados
- Los destinatarios del mensaje deben dar su adhesión voluntaria, en lugar de cancelar la suscripción

### Responsabilidad {#liability}

Aunque CASL tiene un período de transición de tres años, que finaliza el 1 de julio de 2017, la Comisión Canadiense de Radiodifusión y Telecomunicaciones (CRTC), la Oficina de Competencia y la Oficina del Comisionado de Privacidad de Canadá pueden iniciar investigaciones y litigios durante este período. Al final del período de transición, las personas también pueden litigar contra las entidades que consideren que envían correo no deseado.

### Mensajes exentos {#exempt-messages}

Los siguientes tipos de mensajes están exentos de los requisitos de CASL:

- Mensajes abiertos fuera de Canadá
- Mensajes a familiares u otras relaciones personales
- Mensajes a personas asociadas con tu empresa, incluidos empleados o contratistas
- Mensajes que proporcionan información de garantía, información de retirada de productos o información de seguridad sobre un producto o servicio que el destinatario ha utilizado o comprado
- Mensajes que proporcionan notificación de información factual sobre una suscripción, membresía o cuenta
- Mensajes que entregan un producto o servicio, incluidas actualizaciones o mejoras del producto

{% alert note %}
Esta no es la lista completa de exenciones. Consulta el [texto completo de la ley](http://laws-lois.justice.gc.ca/eng/annualstatutes/2010_23/FullText.html) para obtener más detalles.
{% endalert %}

### Consentimiento del mensaje {#message-consent}

Braze requiere consentimiento explícito para todos los mensajes de correo electrónico y SMS/MMS.

#### Consentimiento implícito {#implied-consent}

El consentimiento implícito puede estar legalmente permitido en algunas jurisdicciones, pero no es suficiente para enviar correos electrónicos a través de Braze. Nuestra Política de uso aceptable va más allá de los requisitos legales.

#### Consentimiento expreso {#express-consent}

El consentimiento expreso es una confirmación escrita u oral del destinatario del mensaje y solo es válido si el mensaje incluye una descripción clara y sencilla de:

- Por qué se solicita el consentimiento
- La persona u organización que solicita el consentimiento

## Filtros de correo no deseado {#spam-filters}

El hecho de que tus correos electrónicos se hayan enviado correctamente no significa que necesariamente se hayan visto. No existe una solución universal para evitar todos los filtros de correo no deseado, ya que cada filtro es único en la forma en que evalúa la "puntuación de spam" de un correo electrónico. Sin embargo, aquí tienes algunos consejos para evitar que tus correos electrónicos se etiqueten como "correo no deseado".

### Obtén permiso {#get-permission}

Un proceso de doble adhesión voluntaria consiste en enviar un correo electrónico de seguimiento con un enlace de confirmación después de una adhesión voluntaria inicial. Esto proporciona validación de que los destinatarios desean recibir tu contenido. Incluso puedes ir un paso más allá pidiendo a los usuarios que te añadan a su libreta de direcciones. Además, asegúrate de hacer crecer tus listas de correo electrónico de forma orgánica&#8212;¡las listas compradas tienden a estar desactualizadas!


### Construye tu reputación {#build-your-reputation}

Asegúrate de establecer expectativas cuando las personas se registren para recibir tus correos electrónicos. Sé explícito sobre lo que enviarás y con qué frecuencia lo harás. Luego, anima a los usuarios a interactuar con tus campañas de correo electrónico proporcionando contenido valioso. Tener contenido personalizado y relevante disminuye la probabilidad de que tus destinatarios marquen los mensajes como correo no deseado.

### Mantén tu reputación {#maintain-your-reputation}

Mantente en contacto constante con tus usuarios para evitar que tus listas de correo electrónico se vuelvan obsoletas. Esperar demasiado tiempo para enviar un mensaje puede hacer que el destinatario se olvide de ti y te marque como correo no deseado. Mantén tus listas de correo electrónico actualizadas implementando una política de caducidad para eliminar las direcciones de correo electrónico que rebotan. Las tasas de rebote son un factor clave que utilizan los ISP para evaluar la reputación de un remitente.

### Verifica y prueba {#check-and-test}

Asegúrate de que tu mensaje no contenga nada que pueda activar los filtros de correo no deseado. Esto incluye etiquetas superfluas de editores de texto externos como Microsoft Word, formato de texto anormal, uso excesivo de signos de exclamación (!) y signos de interrogación (?) como puntuación, escribir TODO EN MAYÚSCULAS y palabras que activan los filtros de correo no deseado. Envía correos electrónicos con contenido variado utilizando las capacidades de pruebas multivariante para asegurarte de que tus correos electrónicos no vayan a la carpeta de correo no deseado.

## Canal de mensajería {#messaging-channel}

### Correo electrónico {#spam-email}

La calidad de tu lista de correo electrónico es especialmente importante. Un puñado de correos electrónicos incorrectos en tu lista puede arruinar la entrega para un millón de usuarios válidos. Recopilar una lista de correos electrónicos incorrectos genera rebotes, inclusión en listas de bloqueo, activación de trampas de correo no deseado y hunde tus tasas de respuesta. Eliminar los correos electrónicos que no tienen actividad de forma regular y quitar los rebotes obvios son el primer paso. Ya sea que implementes una adhesión voluntaria (marcar la casilla), una cancelación de suscripción (desmarcar la casilla), una confirmación de adhesión voluntaria (un correo electrónico que dice gracias por registrarte y proporciona un enlace para cancelar la suscripción) o una doble adhesión voluntaria (un correo electrónico que requiere un clic para confirmar), lo que debes considerar es la calidad de la lista.

### iOS {#spam-ios-windows}

En iOS, siempre se ha pedido a los usuarios que den su adhesión voluntaria a las notificaciones push. El cuadro de diálogo de iOS simplemente aparece al entrar en la aplicación y pide al usuario que acepte las notificaciones de tu aplicación. El usuario de la aplicación ve el mismo mensaje emergente en el momento en que abre una aplicación por primera vez, por lo que todos los que están en tu lista de iOS para notificaciones push han dado, por definición, su adhesión voluntaria.

### Android {#spam-android}

En Android, se puede asumir que tus usuarios han dado su adhesión voluntaria mediante el consentimiento implícito que se establece en tu política de privacidad o acuerdo de licencia de usuario final. Es posible que desees implementar un proceso de adhesión voluntaria expresa, quizás en una pantalla inicial justo cuando el usuario inicia la aplicación por primera vez. Visita el artículo sobre [mejores prácticas de push]({{site.baseurl}}/user_guide/channels/push/best_practices/) para obtener más detalles. También puedes orientar al usuario sobre qué tipos de notificaciones push recibirá, aumentando así la tasa de adhesión voluntaria.