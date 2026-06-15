---
page_order: 5
nav_title: Términos que debes conocer
article_title: Términos que debes conocer sobre SMS, MMS y RCS
alias: /sms_terms_to_know/

layout: glossary_page
glossary_top_header: "Términos que debes conocer"
glossary_top_text: "Consulta los siguientes términos para obtener más información sobre los ecosistemas, tecnologías y procesos de SMS, MMS y RCS."
page_type: glossary
description: "Este glosario define varios términos de SMS, MMS y RCS que debes conocer."
channel:
  - SMS
  - MMS
  - RCS

glossaries:
  - name: SMS (Short Message Service)
    display_name: "SMS (servicio de mensajes cortos)"
    description: Un canal de mensajería creado en 1980 y una de las tecnologías de mensajería de texto más antiguas. También es uno de los canales de mensajería de texto más extendidos y utilizados. Este canal es una forma más directa de llegar a tus usuarios y clientes que la mayoría de los demás canales de mensajería, ya que utiliza su número de teléfono personal para contactarlos. Por ello, el SMS tiene más reglas y regulaciones que otros canales de mensajería.
  - name: Short Code
    display_name: "Código abreviado"
    description: Se trata de una secuencia corta y fácil de recordar de 5-6 dígitos que permite a los remitentes enviar más mensajes a tasas más consistentes que los números largos (un mensaje por segundo).<br><br>Se requiere un código abreviado o un código largo.
  - name: Long Code
    display_name: "Código largo"
    description: Es el número de teléfono estándar de 10 dígitos (en la mayoría de los países) que permite a los remitentes enviar más mensajes a una tasa de un mensaje por segundo.<br><br>Se requiere un código abreviado o un código largo.
  - name: Encoding
    display_name: "Codificación"
    description: La conversión de cualquier cosa en una forma codificada. El contenido de SMS puede codificarse en GSM-7 o UCS-2.
  - name: GSM-7 Encoding (Global System for Mobile Communications)
    display_name: "Codificación GSM-7 (Global System for Mobile Communications)"
    description: GSM-7 es el estándar de codificación más común para la mayoría de los mensajes SMS. Utiliza la mayor parte de los alfabetos griego e inglés, así como algunos caracteres adicionales. Puedes obtener más información sobre la codificación GSM-7 y los conjuntos de caracteres que puedes usar en <a href='https://en.wikipedia.org/wiki/GSM_03.38#GSM_7-bit_default_alphabet_and_extension_table_of_3GPP_TS_23.038_.2F_GSM_03.38' title="Alfabeto predeterminado GSM de 7 bits y tabla de extensión">Wikipedia</a>. Los idiomas como el chino, el coreano o el japonés deben transferirse utilizando la codificación de caracteres UCS-2 de 16 bits. <br> <br> Puedes estimar que el límite de caracteres por segmento del mensaje para este tipo de codificación es de 128 caracteres.
  - name: UCS-2 Encoding (Universal Coded Character Set)
    display_name: "Codificación UCS-2 (Universal Coded Character Set)"
    description: La codificación UCS-2 es un estándar de codificación alternativa, especialmente cuando un mensaje no puede codificarse usando GSM-7 o cuando un idioma necesita más de 128 caracteres para representarse. UCS-2 se mide mejor por <a href='https://en.wikipedia.org/wiki/Code_point'>puntos de código</a>, en lugar de "caracteres". Independientemente, puedes estimar que el límite de caracteres por segmento del mensaje para este tipo de codificación es de 67 caracteres.
  - name: Subscription Groups for SMS
    display_name: "Grupos de suscripción para SMS"
    description: Los grupos de suscripción son una herramienta de Braze que te permite dirigirte a niveles de suscripción específicos de usuarios o clientes. Los grupos de suscripción para SMS se construyen internamente en función de tu servicio de mensajería y no se pueden compartir entre espacios de trabajo.
  - name: Message Segments
    display_name: "Segmentos del mensaje"
    description: Un segmento del mensaje es una agrupación de hasta un número definido de caracteres (160 para codificación GSM-7; 67 para codificación UCS-2) que se enviará en un único envío de SMS. Si envías un SMS con 161 caracteres usando codificación GSM-7, verás que se enviaron dos (2) segmentos del mensaje. Enviar múltiples segmentos del mensaje puede generar cargos adicionales.
  - name: Message Service
    display_name: "Servicio de mensajería"
    description: Una colección de códigos largos, códigos abreviados e ID alfanuméricos utilizados para enviar tu mensaje SMS con Braze.
  - name: Keyword
    display_name: "Palabra clave"
    description: "Una palabra corta que se envía a un código abreviado o largo para interactuar con un programa de SMS predefinido o para solicitar la CANCELACIÓN DE SUSCRIPCIÓN de un programa específico o de todos los programas en un código. Por ejemplo, <code>STOP</code>. Las palabras clave deben <br> - ser alfanuméricas <br> - no tener espacios <br> - tener menos de 10 caracteres. <br> <br> Una combinación específica de palabra clave y código abreviado solo puede usarse en un programa activo a la vez. Si se ingresa una palabra clave que ya está en uso por otro programa, aparecerá un error de validación. <br> <br> Hay dos categorías obligatorias de palabras clave que todos los proveedores de contenido SMS deben cumplir: <code>STOP</code> y <code>HELP</code>."
  - name: Mandatory Keyword HELP
    display_name: "Palabra clave obligatoria HELP"
    description: Para cada programa que se crea en la plataforma SMS Campaign Manager, se debe proporcionar contenido para esta palabra clave y debe cumplir con las mejores prácticas y el cumplimiento del operador por país o región en la que se envía y recibe el tráfico de SMS. En la mayoría de los casos, este contenido debe incluir una breve explicación del programa de SMS y cómo cancelar la suscripción.
  - name: Global STOP Keywords
    display_name: "Palabras clave globales STOP"
    description: Las variaciones incluyen <code>STOP</code>, <code>END</code>, <code>QUIT</code>, <code>UNSUBSCRIBE</code>, <code>CANCEL</code>, <code>STOPALL</code>. Estas se conocen como <code>Global-Stop-Keywords</code>. Si cualquiera de estas palabras clave se envía por mensaje de texto a un código abreviado o largo, el número móvil (el número de teléfono móvil de origen) se excluye de todos los programas de SMS activos en ese código con el que está asociado.
  - name: Vanity Code
    display_name: "Código personalizado"
    description: Un código abreviado personalizado es un número de teléfono de 5-6 dígitos seleccionado específicamente por una marca. Los códigos abreviados personalizados son de marca y más fáciles de recordar para los consumidores.
  - name: Shared Short Code
    display_name: "Código abreviado compartido"
    description: Cuando se usa un código abreviado compartido, todos los mensajes de texto, sin importar qué empresa u organización los envíe, llegan al dispositivo móvil del consumidor desde el mismo número de teléfono de 5-6 dígitos. Aunque los códigos abreviados compartidos son relativamente económicos y están disponibles de inmediato, esto significa que tu empresa no tendrá un código abreviado dedicado y estará sujeta a que otras empresas sigan el protocolo correcto con tu código abreviado compartido.
  - name: Alphanumeric Sender ID
    display_name: "ID de remitente alfanumérico"
    description: El ID de remitente alfanumérico te permite establecer el nombre de tu empresa o marca como el ID de remitente utilizando caracteres alfanuméricos al enviar mensajes unidireccionales a países compatibles.
  - name: Toll-Free Number
    display_name: "Número gratuito"
    description: Un número de teléfono gratuito es un número de teléfono en el que se facturan todas las llamadas entrantes en lugar de generar cargos al suscriptor telefónico de origen. Los números gratuitos en EE. UU. y Canadá están habilitados para SMS, donde a los suscriptores se les cobra por los mensajes de texto entrantes y salientes.<br><br>La mensajería con número gratuito funciona mejor cuando tu caso de uso es de persona a persona, como atención al cliente o ventas, donde tanto el remitente como el destinatario mantienen una conversación por mensaje de texto.
  - name: One-Way Messaging
    display_name: "Mensajería unidireccional"
    description: La mensajería unidireccional te permite comunicarte con tus clientes enviando mensajes de texto. La mensajería unidireccional es útil si estás implementando un ID de remitente alfanumérico en mercados donde los códigos largos y abreviados no están disponibles.
  - name: Two-Way Messaging
    display_name: "Mensajería bidireccional"
    description: La mensajería bidireccional te permite mantener una conversación enviando y recibiendo mensajes de texto.
  - name: MMS (Multimedia Message Service)
    display_name: "MMS (servicio de mensajes multimedia)"
    description: MMS se utiliza para enviar mensajes que contienen activos multimedia (JPEG, GIF, PNG) a teléfonos móviles. Al igual que SMS, MMS es un canal de mensajería de alta urgencia que te permite comunicarte con los clientes de inmediato. MMS amplía las capacidades de SMS al darte la posibilidad de agregar contenido multimedia a los SMS que de otro modo serían solo texto.
  - name: RCS (Rich Communication Services)
    display_name: "RCS (Rich Communication Services)"
    description: Rich Communication Services (RCS) mejora el SMS tradicional al permitir que las marcas entreguen mensajes que no solo son informativos, sino también mucho más atractivos. RCS incorpora características como contenido multimedia de alta calidad, botones interactivos y perfiles de remitente con marca directamente en las aplicaciones de mensajería preinstaladas de los usuarios.
  - name: RCS-Verified Sender
    display_name: "Remitente verificado de RCS"
    description: La entidad remitente de un mensaje RCS, o lo que el destinatario ve en su dispositivo para identificar de dónde proviene el mensaje. Los remitentes verificados de RCS contienen un nombre de empresa, un subtítulo, marca visual y una señal de verificación. Después de que proporcionas la información de registro de remitente RCS necesaria a Braze, Braze se encarga del registro y la configuración del grupo de suscripción.
  - name: SMS Fallback
    display_name: "Alternativa de SMS"
    description: Si un mensaje RCS no puede entregarse (por ejemplo, por falta de soporte del operador en la región), Braze aún intentará entregar el mensaje a través de SMS cuando exista un código SMS dentro del grupo de suscripción.
  - name: Basic RCS
    display_name: "RCS básico"
    description: Mensajes RCS de solo texto de hasta 160 caracteres. Se facturan como un único mensaje. Esta categoría solo se utiliza en el modelo global.
  - name: Single RCS
    display_name: "RCS único"
    description: Mensajes RCS de solo texto que superan los 160 caracteres o incluyen elementos enriquecidos, como botones o contenido multimedia. Se facturan como un único mensaje. Esta categoría solo se utiliza en el modelo global.
  - name: Rich RCS
    display_name: "RCS enriquecido"
    description: Mensajes RCS de solo texto, con o sin sugerencias o botones limitados. Se facturan por segmento del mensaje (160 bytes UTF-8). Esta categoría solo se utiliza en el modelo de Estados Unidos.
  - name: Rich Media RCS
    display_name: "RCS de contenido multimedia enriquecido"
    description: Mensajes RCS que incluyen un archivo multimedia (imagen, video) o una tarjeta enriquecida. Se facturan como un único mensaje, independientemente de la longitud del mensaje. Esta categoría solo se utiliza en el modelo de Estados Unidos.
---