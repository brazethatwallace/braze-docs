# Remitentes de SMS y RCS {#sms-and-rcs-senders}

> Este artículo ofrece un resumen de los códigos y remitentes disponibles para enviar mensajes SMS y RCS.

## Tipos de remitentes de SMS y RCS {#types-of-sms-and-rcs-senders}

{% tabs %}
{% tab Remitente verificado RCS %}

### Remitente verificado RCS {#rcs-verified-sender}

RCS es un sistema de mensajería moderno que ofrece más características que el SMS tradicional, introduciendo capacidades como IDs de remitente de marca, contenido multimedia enriquecido y contenido interactivo, como carruseles desplazables, respuestas rápidas, botones de CTA y más. Está diseñado para ofrecer una experiencia de usuario más elegante y atractiva.

{% alert important %}
Los mensajes RCS no pueden enviarse a través de servicios de mensajería de Twilio. Los grupos de suscripción que usan Twilio para SMS deben utilizar un remitente RCS compatible con Infobip (u otro proveedor RCS compatible) para el tráfico RCS. De lo contrario, los envíos RCS se cancelarán en el momento del envío.
{% endalert %}

#### Detalles {#details}

| Componentes visuales | Acceso | Rendimiento | MMS habilitado | Unidireccional vs. bidireccional |
| --- | --- | --- | --- | --- |
| - Nombre de marca<br>- logotipo<br>- subtítulo opcional<br> - señal de verificación | 4 a 6 semanas para aprobación del operador | El rendimiento y la entrega dependen de que el destinatario tenga una conexión de datos activa (datos móviles o Wi-Fi). RCS no depende de límites fijos impuestos por la red como lo hace SMS; los mensajes RCS se envían a través de redes de datos en lugar de los canales de señalización celular tradicionales utilizados por SMS. | N/A | Bidireccional |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Detalles" }

#### Pros y contras {#pros-and-cons}

| Pros |
| ---- |
| **Confianza verificada y marca**<br> A diferencia del SMS tradicional, donde tu marca aparece como un código abreviado aleatorio de 5 dígitos o un código largo, RCS permite perfiles de remitente verificados. Estos perfiles incluyen el logotipo de tu marca, el nombre y una marca de verificación. |
| **Características de mensajería enriquecida**<br> RCS admite carruseles, videos de alta resolución y botones de acción sugerida (como "Reservar ahora", "Rastrear paquete" o "Pagar factura"). Los usuarios pueden completar tareas complejas sin salir de su aplicación de mensajería, lo que puede generar tasas de conversión más altas que un enlace de texto simple. |
{: .reset-td-br-1 aria-label="Pros y contras" }

| Contras |
| ---- |
| **Soporte fragmentado**<br> Aunque Google ha impulsado RCS fuertemente para Android, y Apple ha introducido recientemente soporte para RCS en iOS, la implementación aún puede ser desigual en diferentes operadores y regiones. Si el teléfono o el operador de un usuario no admite RCS, el mensaje generalmente se envía como un SMS simple, perdiendo consecuentemente todas las características "enriquecidas" de RCS. |
| **Inconsistencias de plataforma**<br> La experiencia de usuario de RCS varía dependiendo del operador del destinatario, el modelo del dispositivo y la aplicación de mensajería que utilicen (por ejemplo, Google Messages o iMessage). |
{: .reset-td-br-1 aria-label="Pros y contras" }

{% endtab %}
{% tab Códigos abreviados SMS %}

#### Códigos abreviados SMS {#sms-short-codes}

Un código abreviado es un número de 5 a 6 dígitos que puede enviar y recibir SMS hacia y desde teléfonos móviles a velocidades más rápidas que los códigos largos. Los códigos abreviados se recomiendan para envíos de alto volumen y sensibles al tiempo.

Algunos países te permiten elegir un número específico por una tarifa adicional. Estos códigos abreviados se llaman códigos abreviados personalizados (vanity). Si te interesan los códigos abreviados personalizados, contacta a tu representante de cuenta de Braze para obtener más detalles.

##### Detalles

| Longitud | Acceso | Rendimiento | MMS habilitado | Unidireccional vs. bidireccional |
| --- | --- | --- | --- | --- |
| 5-6 dígitos | 4-12 semanas de solicitud | 100 MPS o más | Sí | Bidireccional |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Detalles" }

##### Pros y contras

| Pros |
| ---- |
| **Velocidad y escalabilidad**<br> Los códigos abreviados están diseñados específicamente para tráfico de alto volumen. Pueden enviar mensajes a velocidades más rápidas que los códigos largos y, como están previamente verificados directamente por los operadores, tienen el menor riesgo de ser marcados por filtros automáticos de correo no deseado. |
| **Fácil de recordar para "llamadas a la acción"**<br> Para Campaigns de marketing (por ejemplo, "Envía GANAR al 55555"), un código abreviado es mucho más fácil de recordar y escribir para los usuarios que un número de 10 dígitos. Esto convierte a los códigos abreviados en el estándar de oro para anuncios de radio, TV y vallas publicitarias, donde el usuario solo tiene unos segundos para ver o escuchar el número. |
{: .reset-td-br-1 aria-label="Pros y contras" }

| Contras |
| ---- |
| **Los códigos abreviados están disponibles en menos países**<br> Los códigos abreviados no están disponibles en todos los países. Contacta a tu equipo de cuenta de Braze para consultar sobre los países en los que planeas enviar mensajes. |
| **Proceso de solicitud más largo**<br> A diferencia de los códigos largos y los IDs de remitente alfanuméricos, que pueden aprovisionarse en 1 a 2 semanas en algunos casos, un código abreviado puede tardar de 4 a 12 semanas o más en aprovisionarse. Cada operador principal debe aprobar manualmente tu solicitud específica antes de que el código esté activo en su red. Si tienes un lanzamiento de marketing la próxima semana, un código abreviado no es una opción. |
| **Mayor costo**<br> Los códigos abreviados tienden a ser el tipo de remitente más costoso debido a las tarifas de configuración y arrendamiento anual. |
{: .reset-td-br-1 aria-label="Pros y contras" }

{% endtab %}
{% tab Códigos largos SMS %}

#### Códigos largos SMS {#sms-long-codes}

Un código largo es un número de teléfono estándar utilizado para enviar y recibir mensajes SMS. Estos números de teléfono se suelen llamar "códigos largos" (números de 10 dígitos en muchos países) en comparación con los códigos abreviados SMS (números de 5-6 dígitos).

##### Detalles

| Longitud | Acceso | Rendimiento | MMS habilitado | Unidireccional vs. bidireccional |
| --- | --- | --- | --- | --- |
| 10 dígitos | 4-6 semanas de solicitud (puede ser más corto o más largo en diferentes países) | En Estados Unidos, el rendimiento de códigos largos depende de tu puntuación de confianza 10DLC; en mercados internacionales, el rendimiento puede variar o aumentar en algunas circunstancias, pero generalmente comienza alrededor de 10 segmentos de mensaje por segundo (MPS). | Sí | Bidireccional (dependiendo de dónde envíes) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Detalles" }

##### Pros y contras

| Pros |
| ---- |
| **Familiaridad y confianza**<br> Los códigos largos se ven como números de teléfono personales, a menudo incluyendo un código de área local. Para las marcas, esto representa un equilibrio entre presencia profesional y un toque personal y accesible. |
| **Mayor disponibilidad mundial**<br> Los códigos largos están disponibles en más de 100 países principales en todo el mundo. Contacta a tu CSM o a [soporte de Braze]({{site.baseurl}}/braze_support) para obtener una lista de países disponibles. |
{: .reset-td-br-1 aria-label="Pros y contras" }

| Contras |
| --- |
| **Velocidades de envío más lentas y límites diarios de mensajería**<br> Los códigos largos no están diseñados para marketing masivo de la manera en que lo están los códigos abreviados. Si intentas enviar una venta flash sensible al tiempo a 100,000 personas a la vez desde un código largo, podría tomar horas para que todos los mensajes se entreguen. En EE. UU., operadores como T-Mobile también pueden imponer límites de envío diarios para 10DLC basados en la puntuación de confianza de tu marca. |
| **Mayor riesgo de filtrado**<br> Dado que los códigos largos se ven como números de teléfono personales, los operadores los monitorean de cerca para evitar que los números "de persona a persona" se usen para correo no deseado. Incluso con una campaña 10DLC registrada, si el contenido de tu mensaje es demasiado "spam" o no sigue un formato estricto, tienes un riesgo mucho mayor de ser bloqueado por los operadores en comparación con un código abreviado preaprobado. |
{: .reset-td-br-1 aria-label="Pros y contras" }

{% endtab %}
{% tab ID de remitente alfanumérico SMS %}

#### ID de remitente alfanumérico SMS {#sms-alphanumeric-sender-id}

Un ID de remitente alfanumérico (a menudo llamado "alfa") es una cadena reconocible compuesta por cualquier combinación de letras y números (a menudo el nombre de tu empresa o marca) que se muestra como el ID de remitente para mensajería de texto unidireccional.

Pueden tener hasta 11 caracteres y contener letras mayúsculas (A-Z) y minúsculas (a-z), espacios y dígitos (0-9). **No pueden** contener solo números.

##### Detalles

| Longitud | Acceso | Rendimiento | MMS habilitado | Unidireccional vs. bidireccional |
| --- | --- | --- | --- | --- |
| Hasta 11 caracteres | Disponible inmediatamente si no se requiere prerregistro. De lo contrario, de 1 a 4 semanas en la mayoría de los países donde se requiere registro. | Varía según el país | No | Unidireccional |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Detalles" }

##### Pros y contras

| Pros | Contras |
| ---- | ---- |
| {::nomarkdown} <ul><li> Mejor reconocimiento de marca </li><li> En muchos mercados internacionales, los operadores locales prerregistran y verifican los remitentes alfanuméricos, por lo que tus mensajes tienen menos probabilidades de ser atrapados por filtros agresivos de correo no deseado del operador que podrían bloquear códigos largos aleatorios </li><li> Disponible en 1 semana si no se requiere prerregistro </li></ul> {:/} | {::nomarkdown} <ul><li> La <a href='/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling#two-way-messaging-custom-keyword-responses'>mensajería bidireccional</a> no es compatible </li><li> No todos los países admiten esta característica. Por ejemplo, es compatible en el Reino Unido pero está bloqueada en los EE. UU. </li><li> Algunos países tienen un proceso extenso de prerregistro que requiere la presentación de documentación legal y plazos de entrega más largos. </li></ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pros y contras" }

Para más información sobre los IDs de remitente alfanuméricos, contacta a tu CSM.
{% endtab %}
{% tab Números gratuitos SMS %}

#### Números gratuitos habilitados para SMS {#sms-enabled-toll-free-numbers}

Los números gratuitos tienen códigos de área distintos de tres dígitos (por ejemplo, 800, 888, 877 y 866), lo que permite a los usuarios comunicarse con las empresas sin que se les cobre. Ampliamente utilizados para servicio al cliente, también pueden manejar todos los tipos de mensajería A2P (aplicación a persona), incluido el marketing.

##### Detalles

| Longitud | Acceso | Rendimiento | MMS habilitado | Unidireccional vs. bidireccional |
| --- | --- | --- | --- | --- |
| 10 dígitos | 2-4 semanas de solicitud | Comienza en 3 MPS (segmentos por segundo), se puede aumentar por tarifas adicionales | Sí | Bidireccional |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Detalles" }

##### Pros y contras

| Pros |
| ---- |
| **Imagen profesional**<br> Los números gratuitos son ampliamente reconocidos y de confianza en América del Norte para la comunicación empresarial, proporcionando un toque profesional y con autoridad. |
| **Rendimiento flexible; sin límites de envío del operador**<br> A diferencia de los códigos largos estándar, que pueden establecer límites de rendimiento o de envío del operador según el país, los números gratuitos pueden aumentar su rendimiento para admitir volúmenes más altos y no tienen límites diarios de envío del operador en EE. UU. |
{: .reset-td-br-1 aria-label="Pros y contras" }

| Contras |
| --- |
| **Impersonal y neutralidad geográfica**<br> Dado que los números gratuitos carecen de un código de área local, pueden resultar demasiado "corporativos" o anónimos. Para un negocio de servicios local, un número gratuito puede funcionar peor que un código largo estándar porque carece de la conexión con la comunidad y a veces puede confundirse con una línea de telemarketing aleatoria. |
| **Capa adicional de filtrado STOP**<br> Los números gratuitos tienen una capa de manejo de exclusión fuera de Braze que no se puede eliminar ni personalizar. Cuando un usuario envía "STOP" a tu número gratuito, será excluido de recibir más mensajes desde tu número y recibirá una respuesta automática generada por la red. No recibirá más mensajes de tu número gratuito hasta que envíe "START" para ser eliminado de la lista de bloqueo del número gratuito. |
{: .reset-td-br-1 aria-label="Pros y contras" }

{% endtab %}
{% endtabs %}

## Uso combinado de códigos abreviados y códigos largos {#using-short-codes-and-long-codes-together}

Si tu grupo de suscripción incluye tanto códigos abreviados como códigos largos, los códigos abreviados suelen tener prioridad para los mensajes salientes. Sin embargo, algunos proveedores ofrecen la funcionalidad de remitente persistente (sticky sender), que puede provocar que un código largo siga utilizándose para determinados usuarios incluso después de añadir un código abreviado al conjunto de remitentes.

El remitente persistente mantiene la continuidad de los mensajes enrutando todos los mensajes a un usuario específico desde el mismo número de teléfono. Si un usuario recibió un mensaje desde un código largo antes de que se añadiera un código abreviado a tu grupo de suscripción, tu proveedor puede seguir utilizando ese código largo para los mensajes futuros a ese usuario, aunque normalmente el código abreviado tendría prioridad.

Este comportamiento lo controlan los proveedores y no se puede modificar en Braze.

## Configuración {#setup}

Los requisitos y los plazos de configuración varían según el tipo de remitente y el país en el que se está aprovisionando el remitente.

{% tabs local %}
{% tab Remitente verificado RCS %}

### Remitente verificado RCS

Los remitentes verificados RCS se aprovisionan país por país. El proceso de verificación y configuración se centra en tu agente o remitente, es decir, la persona digital que interactúa con los usuarios. Proporcionarás activos de marca y detalles de verificación.

#### Activos de marca {#brand-assets}

- **Nombre verificado:** El nombre que los usuarios ven en la parte superior del hilo de mensajes. Debe ser un nombre comercial reconocible, no necesariamente el nombre legal de tu empresa.
- **Logotipo:** Una imagen de alta resolución de 224x224px. Se muestra en un marco circular, así que mantén los elementos importantes centrados.
- **Banner (imagen principal):** Una imagen de fondo para la tarjeta de perfil de tu negocio (similar a una foto de portada de Facebook o LinkedIn).
- **Color de marca:** Un valor hexadecimal para los botones y elementos de la interfaz de usuario que coincida con el estilo de tu empresa.

#### Detalles de verificación {#verification-details}

- **Punto de contacto (POC):** Esto es fundamental. Debes proporcionar una dirección de correo electrónico de un empleado/a directo/a de la marca (no un correo electrónico de una agencia). Google o el operador enviará un correo electrónico a esta persona para confirmar que ha autorizado a Braze a actuar en tu nombre.
- **Sitio web y política de privacidad:** Un sitio web activo y una política de privacidad que explique cómo manejas los datos de usuario y la mensajería.
- **Descripción del caso de uso:** Una explicación clara de lo que vas a enviar (por ejemplo, "Actualizaciones de entrega de pedidos y soporte al cliente para compras de comercio minorista").

Los plazos de RCS fluctúan según el país y a medida que más operadores adoptan el canal. Actualmente, puedes esperar que un remitente RCS sea aprobado por los operadores en un plazo de 3 a 6 semanas después de solicitar el lanzamiento.

{% endtab %}
{% tab Códigos abreviados SMS %}

### Códigos abreviados SMS

Los códigos abreviados se aprovisionan país por país. Dependiendo del país, el proceso de solicitud de un código abreviado es conocido por ser impredecible. Braze está aquí para ayudarte en cada paso, así que si deseas un código abreviado, contacta a tu administrador de incorporación u otro representante de Braze.

Braze te asistirá en la recopilación de todos los materiales e información necesarios para presentar una solicitud y configurar un nuevo código abreviado. Los requisitos varían según el país, pero muchos requieren al menos lo siguiente:

| Material de la solicitud | Descripción | Requisitos |
|----------------------|----------------|-----------------|
| Llamada a la acción (adhesión voluntaria) | El propósito principal de las divulgaciones es confirmar que el usuario consiente en recibir mensajes de texto y comprende la naturaleza del programa. | {::nomarkdown}<ul><li>Descripción del producto</li><li>Divulgación de frecuencia de mensajes</li><li>Términos y condiciones completos O enlace a los términos y condiciones completos</li><li>Política de privacidad O enlace a la política de privacidad</li><li>Palabra clave STOP</li><li>Divulgación de "Pueden aplicarse tarifas de mensajes y datos".</li></ul>{:/} |
| Términos y condiciones | Los términos y condiciones completos pueden presentarse completamente debajo de la llamada a la acción o ser accesibles a través de un enlace cerca de la llamada a la acción. | {::nomarkdown}<ul><li>Nombre del programa (marca)</li><li>Divulgación de frecuencia de mensajes</li><li>Descripción del producto</li><li>Información de contacto de atención al cliente</li><li>Información de cancelación</li><li>Divulgación de "Pueden aplicarse tarifas de mensajes y datos".</li></ul>{:/} |
| Flujo de mensajes | Los programas de mensajes recurrentes deben confirmar la adhesión voluntaria con un solo mensaje de texto que indique explícitamente a qué programa se inscribió el usuario y proporcione instrucciones claras de cancelación.<br><br> Braze procesa los mensajes de adhesión voluntaria, cancelación y ayuda, actualizando automáticamente el estado del grupo de suscripción del usuario y su número de teléfono asociado en todas las solicitudes entrantes.<br><br> Ten en cuenta que estas palabras clave y respuestas predeterminadas también se pueden personalizar. | {::nomarkdown}<ul><li>Confirmación de adhesión voluntaria:<ul><li>Nombre del programa (marca) O descripción del producto</li><li>Información de cancelación</li><li>Información de contacto de atención al cliente</li><li>Divulgación de frecuencia de mensajes</li><li>Divulgación de "Pueden aplicarse tarifas de mensajes y datos".</li></ul></li><li>Respuesta de HELP:<ul><li>Nombre del programa (marca) O descripción del producto</li><li>Información de contacto de atención al cliente (correo electrónico de soporte o número de teléfono).</li></ul></li><li>Respuesta de cancelación (STOP):<ul><li>Nombre del programa (marca) O descripción del producto</li><li>Confirmación de que no se enviarán más mensajes.</li></ul></li></ul>{:/} |
| Mensajes del programa | Los mensajes del programa se envían en el curso normal del programa de código abreviado, después de que el usuario haya recibido una confirmación de adhesión voluntaria. | {::nomarkdown}<ul><li>Las instrucciones de cancelación deben proporcionarse a intervalos regulares y al menos una vez al mes.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Códigos abreviados SMS" }

Cuando todos tus materiales de solicitud estén listos, Braze presenta la solicitud a nuestros proveedores en tu nombre. Luego, la solicitud es revisada y aprobada por los operadores locales, quienes pueden proporcionar comentarios adicionales o solicitar información adicional. Después de que todos los operadores den su aprobación, puedes configurar inmediatamente el código abreviado para su uso en Braze.

El plazo de revisión y aprobación de códigos abreviados varía, pero generalmente toma de 4 a 12 semanas dependiendo del país y la naturaleza del programa.

{% alert important %}
Si ya tienes tu propio código abreviado, contacta a tu CSM durante el proceso de incorporación para discutir la migración o transferencia de tu código abreviado.
{% endalert %}

{% endtab %}
{% tab Códigos largos SMS y números gratuitos %}

### Códigos largos SMS (10DLC) y números gratuitos {#sms-long-codes-10dlc-and-toll-free-numbers}

En muchos países, configurar códigos largos (también llamados "10DLC" o "códigos largos de 10 dígitos") y números gratuitos para el envío de SMS ha pasado de ser un proceso "plug and play" a un sistema de verificación regulado. Los operadores quieren saber exactamente quién eres y qué planeas decir antes de que envíes.

Durante el proceso de configuración de códigos largos, puedes esperar compartir detalles sobre la identidad de tu marca y la intención de tu campaña.

#### Identidad de marca {#brand-identity}

- **Nombre de la entidad legal:** Debe coincidir exactamente con tus documentos fiscales (por ejemplo, "Acme Corp LLC", no "Acme").
- **ID fiscal:** En EE. UU., este es tu número de identificación del empleador (EIN). A nivel internacional, necesitarás un número de impuesto al valor agregado (IVA) o un número de registro empresarial local (BRN).
- **Presencia digital:** Un sitio web activo y funcional. Los operadores pueden verificarlo para confirmar que no eres una empresa "fantasma".
- **Contacto autorizado:** Nombre, correo electrónico y número de teléfono de una persona responsable de la cuenta.

#### Intención de la campaña {#campaign-intent}

- **Caso de uso:** Indica si estás enviando códigos 2FA, recordatorios de citas, promociones de marketing u otros.
- **Mensajes de ejemplo:** Proporciona de 2 a 5 ejemplos de lo que enviarás.
- **Prueba de adhesión voluntaria:** Describe (y a menudo muestra una captura de pantalla de) cómo un usuario se registra. Los ejemplos incluyen un formulario web con una casilla de verificación o una palabra clave "Text START" en un póster.

Braze trabajará contigo para recopilar todos los detalles necesarios para aprovisionar tu código largo o número gratuito, y luego enviará los detalles a nuestro proveedor para su revisión y aprobación. Después de que nuestro proveedor apruebe el programa, configuramos inmediatamente el código largo o número gratuito en Braze.

El plazo de configuración depende del país de aprovisionamiento. Generalmente, los códigos largos y los números gratuitos tardan entre 1 y 4 semanas en ser aprobados.

{% alert important %}
Todos los clientes que actualmente tienen y/o usan códigos largos de EE. UU. para enviar a clientes de EE. UU. deben registrar sus códigos largos. Para leer más sobre los detalles del registro A2P 10DLC en EE. UU. y por qué es obligatorio, visita nuestro [artículo dedicado sobre 10DLC]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup/10dlc).
{% endalert %}

{% endtab %}
{% tab ID de remitente alfanumérico SMS %}

### ID de remitente alfanumérico SMS

Los ID de remitente alfanuméricos están altamente regulados porque pueden ser fácilmente suplantados para phishing. Mientras que algunos países permiten que cualquiera configure y envíe desde un nombre, en muchos países primero debes demostrar que eres propietario de la marca.

Es posible que se te soliciten los siguientes datos para configurar un ID de remitente alfanumérico.

- **ID preferido:** Una cadena de hasta 11 caracteres. Contiene al menos una letra y no puede ser una palabra genérica como "BANK" o "INFO".
- **Prueba de propiedad de marca:** Tu certificado de marca registrada o un documento de registro empresarial (por ejemplo, un certificado de constitución emitido en los últimos 12 meses).
- **Carta de autorización:** Una carta firmada en papel membretado de tu empresa que autorice a Braze y a nuestro proveedor a enviar mensajes en tu nombre usando ese ID específico.
- **Plantillas de mensajes de ejemplo:** En varias regiones, debes registrar las "plantillas" exactas de los mensajes que planeas enviar. Las desviaciones en los mensajes reales pueden causar fallos en la entrega en esos países.

El plazo para configurar un ID de remitente alfanumérico depende en gran medida de si el país permite la configuración "dinámica" (inmediata, sin registro requerido) o requiere "preinscripción". En los países que requieren preinscripción, el plazo de configuración varía, pero generalmente toma entre 1 y 4 semanas.

{% endtab %}
{% endtabs %}

## Preguntas frecuentes {#frequently-asked-questions}

Para obtener respuestas a las preguntas frecuentes sobre remitentes de SMS y RCS, consulta nuestra página de [preguntas frecuentes sobre SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs).