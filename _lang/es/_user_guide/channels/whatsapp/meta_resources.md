---
nav_title: Recursos de Meta
article_title: Recursos de Meta
page_order: 6
description: "Este artículo proporciona documentación, información y recursos útiles de Meta para mejorar tu comprensión de la integración de WhatsApp."
alias: /meta_resources/
page_type: reference
channel:
  - WhatsApp

---

# Recursos de Meta {#meta-resources}

> Esta página proporciona documentación útil de Meta, actualizaciones de productos y preguntas frecuentes para mejorar tu comprensión de la integración de WhatsApp con Braze.

## Documentación de Meta {#meta-documentation}

Consulta la siguiente documentación de Meta para obtener orientación sobre nombres de visualización, números de teléfono y más.

- [Orientación sobre nombres de visualización](https://www.facebook.com/business/help/757569725593362)
- [Habilitar Meta Insights](https://www.facebook.com/business/help/218116047387456)
- [Requisitos de números de teléfono](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)
- [Límites de mensajería](https://developers.facebook.com/docs/whatsapp/messaging-limits)
- [Calificación de calidad](https://www.facebook.com/business/help/896873687365001)

## Actualizaciones de producto de WhatsApp {#whatsapp-product-updates}

### 2026: Nombres de usuario empresariales {#2026-business-usernames}
*Última actualización: mayo de 2026*

Meta está introduciendo nombres de usuario empresariales para WhatsApp, un nombre de visualización opcional que las empresas pueden adoptar para su número de teléfono de WhatsApp. Cuando se establece un nombre de usuario, aparece en las ventanas de chat de la aplicación de WhatsApp y WhatsApp Business en lugar del número de teléfono. Ten en cuenta que adoptar un nombre de usuario no oculta tu número de teléfono; siempre permanece visible en tu perfil empresarial.

Los nombres de usuario son únicos en todos los números de teléfono de WhatsApp: no pueden compartir el mismo nombre de usuario dos números, ya sean de consumidor o empresariales. No distinguen entre mayúsculas y minúsculas a efectos de unicidad, pero los puntos y los guiones bajos se tratan como caracteres distintos. Por ejemplo, `myid`, `my.id` y `my_id` se consideran nombres de usuario diferentes, mientras que `myID` y `myid` se tratan como el mismo.

Los nombres de usuario empresariales deben cumplir los siguientes requisitos de formato:

- Contener solo letras en inglés (a–z), dígitos (0–9), puntos (`.`) o guiones bajos (`_`)
- Tener entre 3 y 35 caracteres de longitud
- Contener al menos una letra en inglés
- No comenzar ni terminar con un punto, y no contener dos puntos consecutivos
- No comenzar con `www`
- No terminar con un sufijo de dominio común (como `.com`, `.org` o `.net`)

#### Reclamar un nombre de usuario reservado {#claiming-a-reserved-username}

Antes de que la función de nombres de usuario esté ampliamente disponible, es posible que Meta haya prerreservado un nombre de usuario para tu empresa, generalmente coincidiendo con un nombre de usuario existente de Facebook Page o Instagram. Puedes reclamar este nombre de usuario reservado o elegir uno diferente a través de [WhatsApp Manage](https://business.facebook.com/wa/manage/). Los nombres de usuario reclamados no se activan hasta que Meta haga disponible la función.

Si el nombre de usuario reservado coincide con uno ya asociado a tu Facebook Page o cuenta de Instagram, primero debes vincular tu número de teléfono empresarial a esa Page o cuenta. Puedes hacerlo mientras reclamas el nombre de usuario en WhatsApp Manager o Meta Business Suite, o agregando tu número de teléfono directamente desde la Page o cuenta correspondiente. La vinculación requiere control total de la Page o cuenta, o acceso parcial básico con el permiso `manage_phone`.

#### Prioridad de visualización en las ventanas de chat {#display-priority-in-chat-windows}

Cuando tu perfil empresarial aparece en una ventana de chat, WhatsApp utiliza el siguiente orden de prioridad (de mayor a menor):

1. Nombre del contacto guardado
2. Nombre de empresa verificado o nombre de cuenta empresarial oficial (OBA)
3. Nombre de usuario
4. Número de teléfono

Para más información, consulta la documentación de Meta sobre [nombres de usuario empresariales](https://developers.facebook.com/documentation/business-messaging/whatsapp/business-scoped-user-ids/#business-usernames).

### Abril de 2026: Archivado automático de plantillas inactivas {#april-2026-automatic-archival-of-inactive-templates}
*Última actualización: abril de 2026*

- Meta archiva automáticamente las plantillas que han estado inactivas durante 12 meses o más.
- El archivado automático está habilitado para todas las cuentas de WhatsApp Business y no se puede desactivar.
- La actividad de la plantilla incluye crear, editar, enviar, apelar o desarchivar una plantilla.
- Las plantillas archivadas no se pueden enviar y están programadas para eliminación permanente después de 28 días.
- Puedes desarchivar plantillas dentro del período de 28 días para restaurarlas y cancelar la eliminación programada.
- Las notificaciones se envían a través del webhook `message_template_status_update`, correo electrónico y un banner único en WhatsApp Manager.

Para más información, consulta la documentación de Meta sobre [archivado de plantillas](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-archival).

### Junio de 2026: IDs de usuario con alcance empresarial {#june-2026-business-scoped-user-ids}
*Última actualización: marzo de 2026*

- Meta está introduciendo IDs de usuario para reemplazar el intercambio de números de teléfono por privacidad
- Braze está trabajando en una solución antes del despliegue
- Despliegue esperado de Meta en junio de 2026

### Noviembre de 2025: [API de mensajes de marketing para WhatsApp](https://developers.facebook.com/documentation/business-messaging/whatsapp/marketing-messages/overview/) (anteriormente Marketing Messages Lite API) {#november-2025-marketing-messages-api-for-whatsapp-formerly-marketing-messages-lite-api}
*Última actualización: marzo de 2026*

- Reemplaza los límites estáticos de Cloud API con límites dinámicos basados en la participación
- No disponible en EMEA, Japón ni Corea del Sur para entrega optimizada
- Los mensajes de utilidad/autenticación continúan a través de Cloud API automáticamente

### Octubre de 2025: Cambio en el proceso de aprobación de cuentas empresariales oficiales (OBA) {#october-2025-official-business-account-oba-approval-process-changed}
*Última actualización: marzo de 2026*

- Anteriormente abierto a todos los clientes a través de WhatsApp Manager
- Ahora restringido a: gobierno/grandes anunciantes de Meta, anunciantes directos, o a través de un BSP como Braze (hasta 5 por semana)
- Nuevos prerrequisitos: verificación empresarial, verificación en dos pasos, nombre de visualización aprobado, notabilidad
- Comunícate con tu administrador de éxito de cliente para obtener asistencia

### Octubre de 2025: Reducciones de tarifas de precios regionales {#october-2025-regional-pricing-rate-cuts}
*Última actualización: marzo de 2026*

- Tarifas más bajas de utilidad/autenticación en Argentina, Egipto, México y Norteamérica
- Tarifas de marketing más bajas en México (vigentes a partir del 1 de octubre de 2025)

### Octubre de 2025: Los límites de mensajería cambian de por teléfono a por portafolio empresarial {#october-2025-messaging-limits-change-from-per-phone-to-per-business-portfolio}
*Última actualización: marzo de 2026*

- Los límites ahora se comparten entre todos los números de teléfono de un portafolio
- Los portafolios heredan el límite existente más alto
- Acceso más rápido a límites superiores (en 6 horas)
- Riesgo: las empresas sin un número "ilimitado" pueden ver una disminución en sus límites agregados

### 1 de julio de 2025: Revisión de precios {#july-1-2025-pricing-overhaul}
*Última actualización: marzo de 2026*

- La facturación por mensaje reemplazó la facturación por conversación
- Los mensajes de utilidad enviados en una ventana de servicio de 24 horas pasaron a ser gratuitos
- Tarifas actualizadas de utilidad/autenticación en múltiples mercados, con nuevos niveles de volumen
- Nuevas reglas sobre la categorización incorrecta de plantillas de utilidad: las empresas pueden enfrentar rechazo de plantillas y restricciones de envío

### Abril de 2025: Pausa de mensajes de marketing a números de teléfono de EE. UU. {#april-2025-pause-of-marketing-messages-to-us-phone-numbers}
*Última actualización: agosto de 2026*

Meta pausa las nuevas conversaciones de marketing iniciadas por empresas con usuarios de WhatsApp que tienen un número de teléfono de Estados Unidos (un número compuesto por un código de marcación `+1` y un código de área de EE. UU.). Actualmente no hay una fecha programada para cuando se levante esta pausa.

Las plantillas de marketing aún se pueden entregar durante una ventana de conversación abierta iniciada por el usuario, como una ventana de servicio al cliente de 24 horas o una ventana de punto de entrada gratuita de 72 horas abierta por un [anuncio que dirige a WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/use_cases/ads_that_click_to_whatsapp#considerations). Fuera de estas ventanas, los intentos de enviar plantillas de marketing a números de teléfono de EE. UU. generan el error `131049`. Los mensajes de utilidad, autenticación, servicio y respuesta siguen disponibles.

### Marzo de 2025: Restricciones por uso indebido de categorías de plantillas {#march-2025-template-category-misuse-restrictions}
*Última actualización: marzo de 2026*

- Meta introdujo medidas de aplicación para empresas que hacen un uso indebido de la categorización de utilidad/marketing
- Puede resultar en restricciones de 7 a 30 días en la creación de plantillas y revisiones de categorías

### Marzo de 2025: Límites de mensajes de plantillas de marketing por usuario {#march-2025-per-user-marketing-template-message-limits}
*Última actualización: agosto de 2025*

Meta limitará la cantidad de mensajes de plantillas de marketing que un usuario puede recibir de todas las empresas en un período de tiempo determinado, comenzando con los mensajes que tienen menos probabilidad de ser leídos.

Una excepción es que si una persona responde a un mensaje de marketing, se abrirá una ventana de servicio al cliente de 24 horas. Los mensajes de marketing enviados dentro de esta ventana no contarán para el límite de esa persona.

El límite específico varía según el usuario, dependiendo de su nivel de participación. Obtén más información sobre los límites de mensajes de plantillas de marketing por usuario de WhatsApp en la [documentación de límites de mensajes de plantillas de marketing por usuario de WhatsApp](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates#per-user-marketing-template-message-limits).

### Enero de 2025: WhatsApp pausará el envío de mensajes de marketing a usuarios de EE. UU. a partir del 1 de abril {#january-2025-whatsapp-pausing-marketing-message-sending-to-us-users-starting-april-1}
*Última actualización: enero de 2025*

WhatsApp pausará el envío de mensajes de marketing a usuarios de EE. UU. (personas con números de teléfono de EE. UU.) a partir del 1 de abril de 2025. Los [mensajes de utilidad, servicio y autenticación](https://developers.facebook.com/docs/whatsapp/pricing/) y los [mensajes de respuesta]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message) seguirán estando permitidos en EE. UU.

El envío de mensajes de marketing (junto con todos los demás tipos de mensaje) a todos los demás países o regiones seguirá estando permitido y no se verá afectado.

Meta nos informó que está realizando esta actualización para mantener la salud del ecosistema de WhatsApp en EE. UU., donde WhatsApp está creciendo rápidamente pero todavía se encuentra en una etapa temprana (por ejemplo, los mensajes de marketing tienen menor participación que en otras regiones). Seguirán evaluando cuándo el mercado estadounidense esté listo para reanudar los mensajes de marketing.

La entrega de mensajes de marketing a números de teléfono con códigos de área de EE. UU. será rechazada por WhatsApp y devolverá un código de error 131049.

### Noviembre de 2024: Cambios en la política de adhesión voluntaria de WhatsApp {#november-2024-changes-to-whatsapp-opt-in-policy}
*Última actualización: enero de 2025*

Meta actualizó recientemente su [política de adhesión voluntaria](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). En lugar de requerir consentimiento específico del canal, las empresas ahora pueden enviar mensajes a los usuarios en la plataforma si:

1. La persona ha proporcionado su número de teléfono.
2. La persona dio permiso de adhesión voluntaria para mensajería general, no solo para WhatsApp.

Las empresas aún deben cumplir con todas las leyes locales y seguir los siguientes requisitos al obtener la adhesión voluntaria:

- Las empresas deben indicar claramente que una persona está optando por recibir comunicación de la empresa
- Las empresas deben indicar claramente el nombre de la empresa de la cual la persona está optando por recibir mensajes
- Las empresas deben cumplir con la legislación aplicable

Aunque WhatsApp ha flexibilizado su política, Braze sigue recomendando recopilar la adhesión voluntaria específica del canal de WhatsApp para fomentar la mejor experiencia del cliente y las mejores tasas de participación. Como siempre, consulta con tu equipo legal para determinar qué tiene sentido para tu marca.

### Noviembre de 2024: Actualizaciones al límite de plantillas de marketing por usuario para personas en EE. UU., antes de la temporada de fiestas {#november-2024-updates-to-the-per-user-marketing-template-limit-for-people-in-the-us-ahead-of-the-holiday-season}
*Última actualización: diciembre de 2024*

Desde que Meta implementó el límite de plantillas de marketing por usuario, Meta ha observado mejoras significativas en las tasas de lectura y la percepción de los usuarios.

A partir de ahora, antes de la temporada de fiestas, las personas en EE. UU. recibirán menos conversaciones de marketing nuevas. Meta espera que este cambio genere audiencias más comprometidas, lo que en última instancia conduce a mejores resultados para las empresas. Esto puede resultar en tasas de entrega más bajas para tu empresa si envías mensajes de marketing a números de teléfono de EE. UU., lo cual puede monitorearse con el código de error `131049` a través de Braze Currents y el registro de actividad de mensajes.

Las empresas en EE. UU. aún pueden entregar mensajes de marketing en otras geografías, y no hay impacto en los mensajes de utilidad, autenticación o servicio, ni en los mensajes de plantillas de marketing enviados dentro de una ventana de conversación iniciada por el usuario (por ejemplo, un anuncio de clic a WhatsApp o un carrusel de productos o una plantilla de cupón enviada como parte de una conversación).

### Noviembre de 2024: WhatsApp amplía las medidas de calidad a nivel de cuenta para incluir tasas de lectura {#november-2024-whatsapp-expanding-quality-based-account-enforcements-to-include-read-rates}
*Última actualización: diciembre de 2024*

WhatsApp invierte continuamente en nuevas formas de ayudar a las empresas a crear experiencias de calidad para sus clientes, como reducir el comportamiento de correo no deseado en su plataforma.

El 22 de noviembre, WhatsApp comenzó a ampliar sus medidas de calidad a nivel de cuenta existentes en las cuentas de WhatsApp Business (WABAs) con tasas de lectura extremadamente bajas. Este cambio se implementará a nivel global.

Cuando la tasa de lectura de una cuenta cae significativamente (por ejemplo, la mayoría de los mensajes enviados por la cuenta no se leen), se aplicarán bloqueos de mensajería en la cuenta. La severidad del bloqueo aumentará si hay tasas de lectura consistentemente bajas a gran escala.

Si la tasa de lectura de la cuenta es extremadamente baja, se tomarán las siguientes acciones:

- La cuenta será bloqueada para enviar mensajes iniciados por la empresa. Aún podrá responder a mensajes iniciados por el cliente. Este bloqueo inicial es un "bloqueo suave" y puede ser reconocido seleccionando el botón de reconocimiento en Calidad de cuenta para comenzar a enviar mensajes nuevamente.
- Si la tasa de lectura continúa cayendo o permanece baja después del bloqueo suave, las empresas pueden enfrentar un aumento gradual en las acciones de aplicación (por ejemplo, unos días de restricciones de mensajería).
- Las empresas tendrán que esperar a que expire el límite impuesto para comenzar a enviar mensajes nuevamente. Si la tasa de lectura continúa permaneciendo baja después de bloqueos suaves repetidos, la cuenta eventualmente será dada de baja.

#### Cómo mantenerte actualizado sobre estas advertencias y medidas {#how-to-stay-updated-on-these-warnings-and-enforcements}

De manera similar a las medidas de plataforma existentes, las empresas serán notificadas sobre estas acciones y podrán reconocerlas utilizando la página de Calidad de cuenta en WhatsApp Business Manager. Confirma que tienes los datos de contacto correctos listados en WhatsApp Business Manager para todos los administradores necesarios, ya que los correos electrónicos de notificación de medidas se enviarán según esa información.

Las notificaciones sobre violaciones severas de correo no deseado serán:

- Mostradas en el Centro de notificaciones de WhatsApp Business Manager
- Mostradas en un banner en WhatsApp Manager
- Enviadas como correo electrónico a todos los administradores configurados en WhatsApp Business Manager

### Mayo de 2024: Cloud API entra en funcionamiento en Türkiye {#may-2024-cloud-api-going-live-in-trkiye}
*Última actualización: mayo de 2024*

Meta ahora proporciona a las empresas de Cloud API acceso a Türkiye para mensajería empresarial. Anteriormente, WhatsApp Cloud API estaba disponible para que las empresas en Turquía la utilizaran, pero los usuarios de WhatsApp con números turcos no podían enviar ni recibir mensajes enviados a través de Cloud API.

Meta siempre deja claro a los usuarios cuándo están chateando con una empresa alojada por Meta, y todos los usuarios deben aceptar los Términos de servicio y la Política de privacidad de WhatsApp correspondientes para proceder con la mensajería empresarial. La actualización de los Términos de servicio y la Política de privacidad de 2021 en Turquía se había pausado, pero ahora se está implementando. No cambia el compromiso de Meta con la privacidad: las conversaciones personales siguen protegidas por cifrado de extremo a extremo, lo que significa que solo tú y el destinatario previsto pueden verlas. La actualización permite a los usuarios turcos acceder a funciones empresariales opcionales si así lo desean y proporciona más transparencia sobre cómo funciona WhatsApp.

Las empresas de Cloud API ahora pueden iniciar conversaciones con usuarios de WhatsApp con números turcos, que ahora devolverán un webhook como conversación "enviada", en lugar del código de error 131026 actual.

Para que un mensaje empresarial sea "entregado" o "leído", se requiere que el usuario acepte los términos de WhatsApp. Una empresa no será cobrada a menos que el mensaje sea entregado.

Los usuarios que reciban o intenten enviar un mensaje a una empresa de Cloud API verán una notificación dentro de la aplicación sobre la actualización de los términos, que deja claro que no pueden enviar mensajes a una empresa de Cloud API hasta que hayan aceptado la actualización de WhatsApp. Además, los usuarios que registren o vuelvan a registrar la aplicación en su teléfono serán invitados a aceptar la actualización de WhatsApp.

Cuando un usuario acepte la actualización, verá el aviso de mensaje del sistema de Cloud API existente cuando chatee con una empresa de Cloud API.

### Mayo de 2024: Límites de mensajes de plantillas de marketing por usuario {#may-2024-per-user-marketing-template-message-limits}
*Última actualización: mayo de 2024*

Meta está implementando nuevos enfoques para mantener experiencias de usuario de alta calidad y maximizar la participación con los mensajes de plantillas de marketing en la plataforma de WhatsApp. A partir del 23 de mayo de 2024, limitarán la cantidad de mensajes de plantillas de marketing que cada usuario individual puede recibir de todas las empresas con las que interactúa durante un período de tiempo determinado, comenzando con un pequeño número de conversaciones que tienen menos probabilidad de ser leídas. Ten en cuenta que el límite se determina en función de la cantidad de mensajes de plantillas de marketing que esa persona ya ha recibido de cualquier empresa, y no está relacionado específicamente con tu marca. Sin embargo, esto puede afectar la capacidad de entrega de tus mensajes de plantillas de marketing.

El límite solo se aplica a los mensajes de plantillas de marketing que normalmente abrirían una nueva conversación de marketing. Si ya hay una conversación de marketing abierta entre tu marca y un usuario de WhatsApp, los mensajes de plantillas de marketing enviados al usuario no se verán afectados.

Si un mensaje de plantilla de marketing no se entrega a un usuario determinado debido al límite, Cloud API devolverá el código de error 131026. Sin embargo, ten en cuenta que estos códigos de error cubren una amplia gama de problemas que pueden resultar en la no entrega de un mensaje, y por razones de privacidad, Meta no revelará si el mensaje efectivamente no fue entregado debido al límite. Consulta el [documento de solución de problemas](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting) de Cloud API para descripciones de las razones de no entrega y lo que puedes hacer para determinar su causa subyacente.

Si recibes uno de estos códigos de error y sospechas que se debe al límite, evita reenviar inmediatamente el mensaje de plantilla, ya que solo resultará en otra respuesta de error.

Para más información sobre esta actualización de capacidad de entrega, incluidos detalles sobre cómo monitorear tu capacidad de entrega y otras prácticas recomendadas para la mensajería de marketing en WhatsApp, consulta nuestra reciente [publicación en el blog](https://www.braze.com/resources/articles/meta-introduces-deliverability-updates-for-whatsapp?utm_campaign=fy25-q2-global-customer-customer-meta-deliverability-updates-for-whatsapp&utm_medium=email-cdb&utm_source=braze&utm_content=blog-meta-deliverability-updates-for-wa-blog).

### Abril de 2024: Ritmo de plantillas para plantillas de utilidad {#april-2024-template-pacing-for-utility-templates}
*Última actualización: abril de 2024*

El año pasado, WhatsApp introdujo el ritmo de plantillas para mensajes de marketing como una nueva forma de ayudar a las empresas a mejorar la participación de sus plantillas y crear experiencias valiosas para los usuarios. A partir del 30 de abril, están expandiendo el ritmo de plantillas a los mensajes de utilidad. Si una plantilla de utilidad de una cuenta se pausa debido a los comentarios de los usuarios, aplicarán el ritmo a las nuevas plantillas de utilidad que se creen durante los siguientes siete días.

### Abril de 2024: Las tasas de lectura afectarán la calificación de calidad de las plantillas de marketing {#april-2024-read-rates-will-affect-quality-rating-for-marketing-templates}
*Última actualización: marzo de 2024*

WhatsApp está probando nuevos enfoques, comenzando con consumidores en India, para crear experiencias más valiosas y maximizar la participación con las conversaciones de marketing de las empresas. Esto puede incluir limitar la cantidad de conversaciones de marketing que una persona recibe de cualquier empresa en un período determinado, comenzando con un pequeño número de conversaciones que tienen menos probabilidad de ser leídas. Braze recibirá un código de error si un mensaje no se entrega.

WhatsApp comenzará a considerar las tasas de lectura como parte de la calificación de calidad de las plantillas de marketing, junto con las métricas tradicionales como bloqueos e informes. WhatsApp puede pausar temporalmente las Campaigns de mensajes de marketing con tasas de lectura bajas, dando a las empresas tiempo para iterar en las plantillas con menor participación antes de escalar el volumen a partir del 1 de abril de 2024.

### Febrero de 2024: Experimentación con conversaciones de marketing {#february-2024-marketing-conversations-experimentation}
*Última actualización: febrero de 2024*

A partir del 6 de febrero de 2024, WhatsApp está probando nuevos enfoques, comenzando con consumidores en India, para crear experiencias más valiosas y maximizar la participación de los clientes con las conversaciones de marketing de tu marca. Esto puede incluir limitar la cantidad de conversaciones de marketing que un usuario recibe de tu marca en un período determinado, comenzando con un pequeño número de conversaciones que tienen menos probabilidad de ser leídas.

### Octubre de 2023: Ritmo de plantillas {#october-2023-template-pacing}
*Última actualización: octubre de 2023*

A partir del 12 de octubre de 2023, WhatsApp está introduciendo un concepto llamado "ritmo de plantillas" para mensajes de marketing. En lugar de enviar tu mensaje a toda la audiencia de tu Campaign simultáneamente, el "ritmo de plantillas" entrega inicialmente el mensaje a un subconjunto más pequeño de usuarios para recopilar comentarios en tiempo real de los destinatarios de la Campaign antes de enviar los mensajes restantes.

El "límite de ritmo" (el subconjunto inicial de mensajes enviados) es variable dependiendo de la plantilla. Después del envío inicial, WhatsApp retendrá los mensajes restantes durante un máximo de 30 minutos. Durante este período de retención, evalúan la calidad de la plantilla basándose en los comentarios de los clientes. Si los comentarios son positivos, indicativos de una plantilla de alta calidad, entregan los mensajes restantes. Si los comentarios son negativos, descartan los mensajes restantes no entregados, evitando más comentarios negativos de una porción mayor de tus clientes y ayudándote a evitar posibles problemas de aplicación de calidad (como impactos en la calificación de calidad del número de teléfono).

Ten en cuenta que WhatsApp utiliza el mismo sistema para evaluar la calidad de la plantilla en el ritmo de plantillas que el que usa para la pausa de plantillas. Por lo tanto, los mensajes no entregados durante el ritmo de plantillas (debido a plantillas de baja calidad) son los mismos que se habrían pausado a mayor escala.

En última instancia, esta actualización te proporciona un ciclo de retroalimentación más rápido (30 minutos en comparación con horas o días con la pausa de plantillas), para que puedas ajustar tus plantillas y brindar una mejor experiencia al cliente.

**Si tienes más preguntas sobre esta actualización, contacta a tu representante de Meta partner.**

### Junio de 2023: Experimentación de mensajería {#june-2023-messaging-experimentation}
*Última actualización: junio de 2023*

A partir del 14 de junio de 2023, Meta está introduciendo nuevas prácticas de experimentación en la plataforma de WhatsApp para evaluar cómo los mensajes de marketing impactan la experiencia y participación de los consumidores. Este experimento puede afectar tus mensajes de marketing enviados a través de WhatsApp Business API con Braze.

Meta tiene la intención de continuar con esta experimentación en la plataforma de WhatsApp. Consulta la [documentación de Meta](https://developers.facebook.com/docs/whatsapp/on-premises/guides/experiments?content_id=86oue5PtwEgcBJl) para más información.

**La experimentación de WhatsApp afecta solo a los mensajes de marketing.** Este experimento tiene el potencial de impactar la entrega de mensajes de plantillas de marketing. Las plantillas de utilidad y autenticación seguirán entregándose sin ningún impacto de la experimentación.

En el experimento, Meta selecciona aleatoriamente aproximadamente el 1 % de los consumidores de WhatsApp como participantes. Si son seleccionados, Meta no entregará plantillas de mensajes de marketing a estos consumidores a menos que se cumpla una de las siguientes condiciones:

- Si un consumidor te ha respondido en las últimas 24 horas;
- Si hay una conversación de marketing existente abierta; o
- Si el consumidor hizo clic en un anuncio de WhatsApp en las últimas 72 horas.

## Preguntas frecuentes {#faq}

### ¿Cómo sabré si mi mensaje de marketing fue afectado por el experimento de Meta? {#how-will-i-know-if-my-marketing-message-was-impacted-by-metas-experiment}

Si un mensaje no se entrega debido al experimento, se mostrará un código de error específico en el Registro de actividad y dentro de Currents. El mensaje también se contará como un fallo y se incorporará en tus métricas de fallos de WhatsApp en todos los informes dentro del panel de Braze. No se te cobrará por estos mensajes.

Este código de error 130472 indicará "User's number is part of an experiment." Consulta la [documentación de Meta](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes?content_id=8SJRLBEjYGvXO9k) para obtener más información sobre los códigos de error de WhatsApp Cloud API.

### ¿Puedo excluirme del experimento de Meta? {#can-i-opt-out-of-metas-experiment}

No, Meta no permite la exclusión de ningún experimento. Todos los proveedores y usuarios de WhatsApp Business API están sujetos a este experimento de Meta.

### ¿Puedo intentar reenviar una plantilla más tarde? {#can-i-try-to-resend-a-template-later}

No hay un tiempo fijo para este experimento. Como tal, un consumidor puede seguir estando sujeto al experimento.

### ¿Qué puedo hacer si mis mensajes de marketing no se entregan debido al experimento de Meta? {#what-can-i-do-if-my-marketing-messages-are-not-delivered-due-to-metas-experiment}

Recomendamos usar otros canales de Braze, como correo electrónico, SMS, notificaciones push o In-App Messages para enviar un mensaje con contenido similar a tus usuarios previstos.