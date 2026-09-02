---
nav_title: Glosario de capacidad de entrega de correo electrónico
article_title: Glosario de capacidad de entrega de correo electrónico
layout: glossary_page
glossary_top_header: "Glosario de capacidad de entrega de correo electrónico"
glossary_top_text: "Este glosario define términos comunes de capacidad de entrega de correo electrónico e infraestructura de correo electrónico que puedes encontrar al enviar correos electrónicos a través de Braze."
page_order: 1
page_type: glossary
description: "Este glosario define términos comunes de capacidad de entrega de correo electrónico e infraestructura de correo electrónico que puedes encontrar al enviar correos electrónicos a través de Braze."
channel:
  - email

glossaries:
  - name: Lista de permitidos
    description: Una lista de contactos que el usuario considera aceptables para recibir correo electrónico y que no deben filtrarse ni enviarse a la papelera o a la carpeta de correo no deseado.
  - name: Bloqueo
    description: Un rebote de bloqueo es el resultado de que un correo electrónico no sea aceptado para su entrega por el proveedor de buzón. Muchos proveedores de buzón bloquean correos electrónicos de direcciones IP o dominios que han sido reportados por enviar correo no deseado o virus, o que tienen contenido que viola las políticas de correo electrónico o los filtros de correo no deseado. SendGrid usa "bloqueo" para referirse a lo que normalmente se llama rebote blando. En SendGrid, un bloqueo ocurre cuando un correo electrónico no es aceptado para su entrega debido a una razón técnica o temporal.
  - name: Lista de bloqueo
    description: Listas de direcciones IP que han sido reportadas y catalogadas como fuentes conocidas de correo no deseado. Existen listas de bloqueo públicas y privadas. Las listas de bloqueo públicas se publican y están disponibles para el público, muchas veces como un servicio gratuito y a veces por una tarifa.
  - name: Rebote
    description: "También conocido como rebote duro, una dirección que ha rebotado es permanentemente no entregable y se suprime de envíos posteriores. Para más información sobre rebotes en Braze, consulta <a href=\"/docs/user_guide/channels/email/reporting/analytics_glossary#bounces\">Rebotes</a> en el glosario de análisis de correo electrónico."
  - name: Carpeta de correo masivo
    description: También conocida como carpeta de correo no deseado o spam en algunos clientes de correo electrónico.
  - name: Ley CAN-SPAM
    description: "Ley estadounidense que regula el correo electrónico comercial (nombre completo: Controlling the Assault of Non-Solicited Pornography and Marketing Act de 2003)."
  - name: Tasa de clics
    description: "La tasa a la que los destinatarios han hecho clic en un enlace dentro del mensaje. Para más información, consulta <a href=\"/docs/user_guide/channels/email/reporting/analytics_glossary#unique-clicks\">Unique Clicks</a> en el glosario de análisis de correo electrónico."
  - name: Filtros de contenido
    description: Filtros de software que bloquean correos electrónicos basándose en texto, palabras, frases o información de encabezado dentro del propio correo electrónico.
  - name: Diferido
    description: Si un mensaje no puede entregarse en su primer intento, se considera diferido. La mayoría del correo diferido finalmente se entrega.
  - name: Capacidad de entrega
    description: En la comunidad de capacidad de entrega, esta se centra principalmente en la capacidad de llegar al buzón de entrada. Esta tasa no es algo que Braze pueda rastrear directamente, por lo que necesitas usar otros datos disponibles para hacer inferencias sobre la ubicación en el buzón de entrada.
  - name: Tasa de entrega
    description: "La tasa de entregas exitosas, independientemente de la ubicación en el buzón de entrada o de si el correo se abre. Para más información, consulta <a href=\"/docs/user_guide/channels/email/reporting/analytics_glossary#deliveries\">Entregas %</a> en el glosario de análisis de correo electrónico."
  - name: DKIM
    description: DomainKeys Identified Mail permite a una organización asumir la responsabilidad de un mensaje mientras está en tránsito. La organización es un controlador del mensaje, ya sea como su originador o como intermediario. Su reputación es la base para evaluar si se debe confiar en el mensaje para su entrega.
  - name: DMARC
    description: Domain-based Message Authentication, Reporting & Conformance es una especificación técnica creada por organizaciones para reducir el phishing y el fraude por correo electrónico. Actualmente es utilizada por todos los principales proveedores de buzón, incluyendo Google, Yahoo y Microsoft.
  - name: Descarte
    description: SendGrid mantiene listas de correo electrónico para rastrear rebotes, informes de correos no deseados y cancelaciones de suscripción para cada uno de sus usuarios. Si un usuario envía un mensaje a una dirección de correo electrónico que existe en una de estas listas dentro de su cuenta, SendGrid descarta automáticamente el mensaje (es decir, no lo envía a la dirección).
  - name: ESP (proveedor de servicios de correo electrónico)
    description: Empresa que proporciona capacidad de envío y transporte de correo electrónico a especialistas en marketing por correo electrónico. Muchas de las plataformas actuales de marketing, CRM or administración de las relaciones con el cliente e interacción con los clientes incluyen un componente de envío de correo electrónico y comúnmente se denominan ESP en referencia a la capacidad de envío de correo electrónico. Ejemplos incluyen ConstantContact, MailChimp, Emarsys, Salesforce Marketing Cloud, Cheetah Digital y Sailthru.
  - name: Bucle de retroalimentación (FBL)
    description: El mecanismo mediante el cual se notifica a los remitentes sobre informes de correo no deseado para que puedan calcular una tasa de informes de correo no deseado y eliminar la dirección de envíos futuros.
  - name: Rebote duro
    description: "Mensaje enviado a una cuenta de correo electrónico inválida, cerrada o inexistente. Normalmente, los correos electrónicos con rebote duro pueden identificarse con un código de respuesta SMTP de la serie 500. Para más información, consulta <a href=\"/docs/user_guide/channels/email/reporting/analytics_glossary#hard-bounce\">Rebote duro</a> en el glosario de análisis de correo electrónico."
  - name: IP
    description: Un número único asignado a cada dispositivo conectado a Internet.
  - name: ISP (proveedor de servicios de Internet)
    description: Empresa que proporciona servicios de Internet a consumidores como AT&T, British Telecom, Comcast (Xfinity), Cox, Orange, Sky, Spectrum, Tiscali, TalkTalk y Virgin. También incluye coloquialmente a proveedores de buzón como Gmail, Yahoo y Microsoft.
  - name: Higiene de listas
    description: El acto de mantener una lista para que los rebotes duros y los nombres con suscripción cancelada se eliminen de los envíos.
  - name: List-Unsubscribe
    description: El encabezado List-Unsubscribe es texto que puedes incluir en la parte del encabezado de tus mensajes, permitiendo a los destinatarios ver un botón de cancelación de suscripción que pueden seleccionar para dejar de recibir mensajes futuros automáticamente.
  - name: Proveedor de buzón (MBP)
    description: El proveedor de acceso al correo electrónico para los destinatarios, como Gmail, Yahoo y Microsoft.
  - name: Registro MX
    description: Un registro MX es un tipo de registro de recursos en el Sistema de Nombres de Dominio (DNS) que especifica cómo debe enrutarse el correo electrónico de Internet utilizando el Protocolo Simple de Transferencia de Correo (SMTP).
  - name: NDR (informe de no entrega)
    description: Retroalimentación de un receptor de correo electrónico cuando elige no aceptar un correo electrónico para su entrega, en forma de una respuesta SMTP. Los NDR a menudo se denominan rebotes.
  - name: Tasa de aperturas únicas
    description: "La tasa a la que se cargó el píxel de seguimiento de apertura, contando solo destinatarios únicos (sin duplicados). Para más información, consulta <a href=\"/docs/user_guide/channels/email/reporting/analytics_glossary#unique-opens\">Unique Opens</a> en el glosario de análisis de correo electrónico."
  - name: Phishing
    description: Una forma de robo de identidad en la que un estafador utiliza un correo electrónico de apariencia auténtica para engañar a los destinatarios y hacer que proporcionen información personal confidencial, como números de tarjetas de crédito o cuentas bancarias, números de Seguro Social y otra información de identificación personal (PII).
  - name: Campaña de reactivación
    description: Una campaña de correo electrónico enviada a usuarios inactivos o que no responden en un intento de recuperarlos y lograr que interactúen nuevamente con tus correos electrónicos en forma de aperturas, clics y conversiones. Una campaña de reactivación puede enviarse a usuarios inactivos como una campaña independiente o como una serie de campañas.
  - name: DNS inverso (rDNS)
    description: El proceso en el que una dirección IP se asocia correctamente a un nombre de dominio, en lugar de que un nombre de dominio se asocie a una dirección IP. Si un filtro o programa de correo no deseado no puede asociar la dirección IP con el nombre de dominio, puede rechazar el correo electrónico.
  - name: Smart Network Data Services (SNDS)
    description: Ofrecido por Windows Live Hotmail, SNDS proporciona datos a los remitentes basados en el correo real enviado a suscriptores de Hotmail. Las métricas reportadas incluyen quejas, resultados del filtro SmartScreen e impactos en trampas de correo no deseado.
  - name: Rebote blando
    description: "Cualquier rebote debido a un problema temporal o transitorio como \"buzón lleno\", \"usuario excedió la cuota\", \"correo bloqueado por características similares al correo no deseado\", \"mensaje rechazado porque viola las políticas de la organización\" o \"servidor temporalmente no disponible\". SendGrid los llama \"bloqueos\".<br><br>La entrega a cualquier rebote blando que se crea que es un problema temporal (generalmente aquellos con un código SMTP 4xx) se intenta nuevamente hasta que el mensaje se entrega o transcurren 72 horas. Si un mensaje con rebote blando no puede entregarse después de 72 horas, se detienen los intentos de entrega adicionales y la entrega fallida del mensaje se cuenta como un rebote. Para más información, consulta <a href=\"/docs/user_guide/channels/email/reporting/analytics_glossary#soft-bounce\">Rebote blando</a> en el glosario de análisis de correo electrónico."
  - name: Correo no deseado
    description: "Correo electrónico no deseado. En las métricas, los usuarios deben marcar estos correos electrónicos como correo no deseado (por lo que este recuento los incluye en las entregas, ya que el correo electrónico necesita entregarse primero). Para más información, consulta <a href=\"/docs/user_guide/channels/email/reporting/analytics_glossary#spam\">Correo no deseado</a> en el glosario de análisis de correo electrónico."
  - name: SpamCop
    description: Una lista de bloqueo y base de datos de direcciones IP, anteriormente de propiedad privada pero ahora parte del proveedor de correo electrónico Ironport. Muchos proveedores de buzón verifican las direcciones IP de los correos electrónicos entrantes contra los registros de SpamCop para determinar si la dirección ha sido incluida en la lista de bloqueo debido a quejas de correo no deseado.
  - name: Tasa de correo no deseado
    description: "La tasa a la que los destinatarios han marcado un mensaje como correo no deseado mientras lo visualizaban. Esta tasa no incluye el correo que llega a la carpeta de correo no deseado. Tampoco incluye quejas de proveedores de buzón que no tienen un bucle de retroalimentación, como Gmail e iCloud. Para más información, consulta <a href=\"/docs/user_guide/channels/email/reporting/analytics_glossary#spam\">Correo no deseado</a> en el glosario de análisis de correo electrónico."
  - name: Trampa de correo no deseado
    description: "Un correo electrónico utilizado para recopilar y detectar correo no deseado por ISP or proveedor de servicios de Internet y organizaciones antispam. También conocida como spamtrap. Para más información, consulta <a href=\"/docs/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps\">Problemas de capacidad de entrega y trampas de correo no deseado</a>."
  - name: Lista de supresión
    description: "Braze no tiene listas de supresión; sin embargo, puedes crear una política de desactivación como se documenta en <a href=\"/docs/user_guide/channels/email/best_practices/sunset_policies\">Políticas de desactivación</a>. Para más información sobre la gestión de suscripciones de correo electrónico, consulta <a href=\"/docs/user_guide/channels/email/subscriptions\">Suscripciones</a>."
  - name: Limitación de velocidad
    description: La práctica de regular cuántos mensajes de correo electrónico envía un emisor a un proveedor de buzón o servidor de correo a la vez. Algunos proveedores de buzón rebotan correos electrónicos si reciben demasiados mensajes.
  - name: Correo transaccional
    description: "Los mensajes transaccionales se definen bajo CAN-SPAM como cualquier correo electrónico que \"facilita, completa o confirma una transacción previamente acordada\". A diferencia de los mensajes comerciales, los mensajes transaccionales no requieren una dirección del Servicio Postal de EE. UU. ni un enlace de cancelación de suscripción."

---