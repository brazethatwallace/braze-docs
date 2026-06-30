---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes
page_order: 30
description: "Este artículo aborda algunas de las preguntas más frecuentes que surgen al configurar campañas de WhatsApp."
page_type: FAQ
channel:
  - WhatsApp

---

# Preguntas frecuentes {#frequently-asked-questions}

> En esta página, intentaremos responder a tus preguntas más importantes sobre WhatsApp.<br><br>Estas preguntas frecuentes no pretenden proporcionar, ni se puede confiar en ellas como fuente de asesoramiento legal. El uso del canal de WhatsApp está sujeto a requisitos específicos de Meta Platforms, Inc. Para asegurarte de que estás utilizando el canal de WhatsApp en cumplimiento con todos los requisitos aplicables y cualquier ley a la que puedas estar sujeto, debes buscar el asesoramiento de tu equipo legal.

## Temas de las preguntas frecuentes {#faq-topics}
- [Cuentas de WhatsApp Business](#whatsapp-business-accounts)
- [Número de teléfono de la cuenta de WhatsApp Business](#whatsapp-business-account-phone-numbers)
- [Adhesión voluntaria y gestión de suscripciones](#opt-in-and-subscription-management)
- [Límites de mensajería](#messaging-limits)
- [Plantillas de WhatsApp](#whatsapp-templates)
- [Capacidad de entrega](#deliverability)
- [Varios](#miscellaneous)

### Cuentas de WhatsApp Business {#whatsapp-business-accounts}

#### ¿Cómo creo una cuenta de WhatsApp Business? {#how-do-i-create-a-whatsapp-business-account}
Te recomendamos crear tu cuenta de WhatsApp Business (WABA) a través del flujo de registro integrado en el dashboard de Braze.

#### Ya tengo una cuenta de Meta Business. ¿Aún necesito una cuenta de WhatsApp Business? {#i-already-have-a-meta-business-account-do-i-still-need-a-whatsapp-business-account}
Sí, aún necesitas crear una cuenta de WhatsApp Business. Te recomendamos [anidar tu WABA dentro de tu cuenta principal de Meta Business]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup).

#### ¿Cómo accedo a mi cuenta de WhatsApp Business? {#how-do-i-access-my-whatsapp-business-account}
Después de completar el flujo de registro integrado, puedes acceder a tu cuenta en business.facebook.com navegando a la [sección de WhatsApp](https://business.facebook.com/wa/manage/home).

#### ¿Puedo conectar múltiples WABA a Braze? {#can-i-connect-multiple-wabas-to-braze}
Sí, puedes añadir hasta 10 cuentas de WhatsApp Business por espacio de trabajo, y cada cuenta de negocio puede estar anidada bajo un Meta Business Manager diferente.

![Diagrama del ecosistema de Braze y WhatsApp, que muestra cómo los espacios de trabajo y las cuentas de WhatsApp Business se conectan entre sí: puedes conectar un grupo de suscripción a un número de teléfono, múltiples cuentas de WhatsApp Business a un espacio de trabajo, y un espacio de trabajo a múltiples Meta Business Portfolios.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %})

#### ¿Puedo cambiar la moneda de mi cuenta de WhatsApp Business? {#can-i-change-my-whatsapp-business-account-currency}
No. Meta controla la moneda de tu cuenta de WhatsApp Business, y Braze no puede cambiarla ni convertirla. Para usar una moneda diferente, [crea una cuenta de WhatsApp Business separada]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) con esa moneda, o ponte en contacto con el soporte de Meta para preguntar si pueden actualizar la moneda de tu cuenta existente.

### Números de teléfono de la cuenta de WhatsApp Business {#whatsapp-business-account-phone-numbers}

#### ¿Necesito un número de teléfono para mi cuenta de WhatsApp Business? {#do-i-need-a-phone-number-for-my-whatsapp-business-account}
Sí, necesitas un número al que tengas acceso. Se te pedirá que verifiques tu número de teléfono con autenticación de 2 factores cuando pases por el flujo de registro integrado. El número de teléfono no puede usarse para otras cuentas de WhatsApp (de negocio o personales).

#### ¿Qué tipos de números de teléfono son compatibles con WhatsApp? {#what-types-of-phone-numbers-are-supported-with-whatsapp}
Consulta los requisitos de Meta para [números de teléfono](https://developers.facebook.com/docs/whatsapp/phone-numbers) para más información.

#### ¿Puedo usar un número de teléfono en múltiples WABA? {#can-i-use-one-phone-number-across-multiple-wabas}
No. Un número de teléfono no puede compartirse entre múltiples WABA.

#### ¿Necesito un tipo específico de número de teléfono para enviar mensajes a países específicos? {#do-i-need-a-specific-type-of-phone-number-to-send-messages-to-specific-countries}
No. WhatsApp te permite enviar mensajes a usuarios finales desde cualquier número de teléfono compatible en cualquier país. Consulta los requisitos de Meta para [números de teléfono](https://developers.facebook.com/docs/whatsapp/phone-numbers) para más información.

#### ¿Necesito usar un número de teléfono específico de un país para enviar a ciertos países? {#do-i-need-to-use-a-country-specific-phone-number-to-send-to-certain-countries}
No. Con WhatsApp, cualquier número de teléfono compatible puede enviar a usuarios finales en cualquier país compatible.

### Adhesión voluntaria y gestión de suscripciones {#opt-in-and-subscription-management}

#### ¿Necesito recopilar la adhesión voluntaria para enviar mensajes de marketing a usuarios finales en WhatsApp? {#do-i-need-to-collect-opt-in-to-send-marketing-messages-to-end-users-on-whatsapp}
Sí, WhatsApp requiere que las empresas [recopilen el consentimiento de adhesión voluntaria](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) para enviar mensajes de marketing a usuarios finales.

#### ¿Puedo enviar mensajes proactivamente a usuarios finales en WhatsApp para recopilar el consentimiento de adhesión voluntaria? {#can-i-proactively-message-end-users-on-whatsapp-to-collect-opt-in-consent}
Si decides enviar mensajes proactivamente a usuarios finales, tu primer mensaje iniciado por la empresa debe preguntar al usuario si desea recibir mensajes de marketing de tu empresa y debe cumplir con los requisitos de Meta para [obtener la adhesión voluntaria](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Ten en cuenta que WhatsApp monitorizará la reputación de tu empresa en el canal, por lo que la mejor práctica recomendada es ser explícito con los usuarios finales y enviar solo mensajes que hayan indicado que desean recibir.

#### ¿Necesito recopilar el número de teléfono del usuario final cuando recopilo la adhesión voluntaria? {#do-i-need-to-collect-the-end-users-phone-number-when-i-collect-opt-in}
Necesitas tener el número de teléfono del usuario final en el perfil de Braze para enviarle mensajes.
- Si ya tienes su número, no necesitas recopilarlo durante la adhesión voluntaria.
- Si no tienes el número del usuario final, tu método de adhesión voluntaria debe incluir la captura del número de teléfono.

#### ¿Cómo actualizo el estado de suscripción de los usuarios finales que se adhieren? {#how-do-i-update-the-subscription-status-of-end-users-who-opt-in}
La gestión de suscripciones del canal de WhatsApp funciona de manera similar a como funciona en otros canales de Braze. Consulta [Gestión de suscripciones de usuarios]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups) para más información.

#### Si ya tengo una lista de usuarios que se han adherido para recibir mensajes de marketing en WhatsApp, ¿cómo actualizo su estado de suscripción en Braze? {#if-i-already-have-a-list-of-users-who-have-opted-in-to-receive-marketing-messages-on-whatsapp-how-do-i-update-their-subscription-status-in-braze}
Puedes actualizar su estado de suscripción mediante la [importación de usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#importing-custom-data).

#### ¿Qué métodos debo usar para recopilar adhesiones voluntarias? {#what-methods-should-i-use-to-collect-opt-ins}
Braze recomienda consultar las [directrices de Meta para métodos de adhesión voluntaria](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) para mantener el cumplimiento. Consulta el siguiente recurso para [ideas y sugerencias de canales y adhesión voluntaria de Braze](https://docs.google.com/document/d/1rNKnKN2oIn-e9bXdYEvnwdlzlCsEOKs-xREcdVvPBE8/edit).

#### ¿Se requiere la doble adhesión voluntaria para WhatsApp? {#is-double-opt-in-required-for-whatsapp}
No, la doble adhesión voluntaria no es obligatoria.

#### ¿Cómo cancelan la suscripción mis usuarios a los mensajes de WhatsApp? {#how-do-my-users-opt-out-of-whatsapp-messages}
Tus usuarios pueden cancelar la suscripción de dos maneras:
1. Configura un mensaje entrante de WhatsApp con una palabra específica de cancelación y usa un webhook para actualizar el estado de suscripción del usuario.
2. Añade una respuesta rápida de cancelación dentro de la plantilla de WhatsApp, con un webhook correspondiente para actualizar.

### Límites de mensajería {#messaging-limits}

#### ¿Qué son los límites de mensajería? {#what-are-messaging-limits}
Los límites de mensajería son un concepto de integridad de WhatsApp. Determinan el número máximo de conversaciones iniciadas por la empresa que cada número de teléfono puede iniciar en un período continuo de 24 horas. Hay cuatro niveles de límite de mensajería: 1k, 10k, 100k e ilimitado.

#### ¿Cómo aumento mi límite de mensajería? {#how-do-i-increase-my-messaging-limit}
WhatsApp aumentará tu límite de mensajería si cumples las siguientes condiciones:
1. El [estado del número de teléfono](https://www.facebook.com/business/help/896873687365001) es **Connected**
2. La [calificación de calidad del número de teléfono](https://www.facebook.com/business/help/896873687365001) es **Medium** o **High**
3. En los últimos siete días, has iniciado X o más conversaciones con usuarios únicos, donde X es tu límite de mensajería actual dividido entre 2

Entonces, para pasar de 100k a ilimitado, debes enviar al menos 50 000 conversaciones iniciadas por la empresa en un período de 7 días.

#### ¿Cuánto tiempo tarda en aumentar mis límites de mensajería? {#how-long-does-it-take-to-increase-my-messaging-limits}
Si se cumplen todas las condiciones anteriores, puedes aumentar tu límite de mensajería de 1k a ilimitado en 4 días.

#### ¿Dónde puedo ver mi límite de mensajería actual? {#where-can-i-see-my-current-messaging-limit}
Puedes consultar tus límites de mensajería actuales en la pestaña **WhatsApp Manager > Overview Dashboard > Insights**.

#### ¿Qué sucede si intento enviar mensajes cuando ya he alcanzado mi límite de mensajería? {#what-happens-if-i-attempt-to-send-messages-when-i-have-already-reached-my-messaging-limit}
Si intentas enviar una Campaign o Canvas a más usuarios únicos de los que permite tu límite actual, los mensajes no se enviarán. Braze seguirá intentando reenviar los mensajes si/cuando tu límite de mensajería aumente durante un máximo de un día.

#### ¿Puede disminuir mi límite de mensajería? {#can-my-messaging-limit-decrease}
Sí, si la calificación de calidad de tu número de teléfono baja demasiado, corres el riesgo de que WhatsApp disminuya tu límite de mensajería. Braze recomienda que te suscribas y recibas notificaciones de actualizaciones relacionadas con la calidad de WhatsApp, incluyendo actualizaciones del estado de tu número de teléfono y el nivel del límite de mensajería. Puedes suscribirte a las notificaciones directamente en el dashboard de WhatsApp Manager.

#### ¿Cuál es el límite de rendimiento de Meta? {#what-is-the-meta-throughput-limit}
Meta tiene su propio límite de rendimiento separado del límite de mensajería de WABA. El límite predeterminado que admite la API en la nube es de 80 mensajes por segundo. Si crees que tus campañas superarán este límite, puedes [solicitar](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/#throughput) que se aumente tu límite. Meta recomienda que envíes esta solicitud con al menos tres días de antelación a los envíos de la campaña.

### Plantillas de WhatsApp {#whatsapp-templates}

#### ¿Qué es una plantilla de WhatsApp? {#what-is-a-whatsapp-template}
WhatsApp requiere que todos los mensajes iniciados por la empresa comiencen usando una plantilla aprobada. La plantilla incluye el texto del mensaje, junto con medios enriquecidos opcionales como imágenes, llamadas a la acción y botones de respuesta rápida. Después de que WhatsApp apruebe las plantillas, se pueden usar para redactar un mensaje de WhatsApp en Braze.

#### ¿Dónde creo, edito y gestiono mis plantillas de WhatsApp? {#where-do-i-create-edit-and-manage-my-whatsapp-templates}
Crearás, editarás, gestionarás y enviarás plantillas para aprobación directamente en WhatsApp Manager. Después de que tu WABA esté conectada a Braze, verás todas tus plantillas en el dashboard con un indicador de estado. Si una plantilla es rechazada, la reenviarás directamente a través de WhatsApp Manager. **Las plantillas no se pueden crear ni editar directamente en Braze.**

#### ¿Cuánto tiempo tarda WhatsApp en revisar el envío de una plantilla? {#how-long-does-it-take-whatsapp-to-review-a-template-submission}
El proceso de aprobación puede tardar hasta 24 horas, pero a menudo las plantillas se procesan en cuestión de horas o minutos.

#### ¿Cuántas plantillas puedo tener en un momento dado? {#how-many-templates-can-i-have-at-a-given-time}
Tu límite de plantillas de mensaje depende del estado de verificación de tu empresa. Puedes consultar tu límite en la página **WhatsApp Manager > Message Templates**.

#### ¿Cómo personalizo el texto de la plantilla y los medios enriquecidos en Braze? {#how-do-i-personalize-template-copy-and-rich-media-in-braze}
WhatsApp permite insertar parámetros variables en las plantillas de mensaje. Los mensajes no pueden comenzar ni terminar con un parámetro variable. Los parámetros variables se pueden rellenar con lógica Liquid en la plataforma Braze. Consulta [redactar un mensaje de WhatsApp en Braze]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message) para obtener más información sobre los parámetros variables.

#### Mi plantilla fue rechazada. ¿Puede Braze ayudarme a que sea aprobada? {#my-template-got-rejected-can-braze-help-me-get-it-approved}
El equipo de Braze no tiene visibilidad sobre los rechazos de plantillas. Debes trabajar directamente con tu WhatsApp Business Manager para editar y reenviar la plantilla. Asegúrate de proporcionar una plantilla de ejemplo cuando sea necesario. Verifica que tu plantilla cumpla con las políticas de [negocio](https://www.whatsapp.com/legal/business-policy/?fbclid=IwAR2qWg6yFKdyjDMxJkbNSM38FLGsxXxffC1qStY2gaHOyp-gl_8g72rZNIw) o [comercio](https://www.whatsapp.com/legal/commerce-policy/?fbclid=IwAR3bzN3LTZ-7kO-wnO7X3smtPKGy0asxaFod-U1Ub8B9JUpnrfy1_y7LpAQ) de Meta.

#### ¿Se pueden segmentar o personalizar los medios enriquecidos en Braze? {#can-the-rich-media-be-targeted-or-personalized-in-braze}
Las imágenes se pueden cargar desde la biblioteca de medios, pero no se pueden segmentar dinámicamente. Para las URL, la última parte del enlace se puede [rellenar dinámicamente usando Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#use-liquid-personalization-in-urls).

### Capacidad de entrega {#deliverability}

#### ¿Por qué no se entregaría un mensaje? {#why-would-a-message-not-be-delivered}
Hay varias razones por las que un mensaje podría no entregarse, incluyendo problemas de red y que el dispositivo esté apagado.

#### Si un mensaje no se entrega, ¿se me cobrará? {#if-a-message-is-not-delivered-will-i-be-billed}
No. Si un mensaje no se entrega, no se te cobrará.

#### ¿Qué sucede si un usuario final bloquea mi empresa? {#what-happens-if-an-end-user-blocks-my-business}
Si un usuario final bloquea tu empresa, los mensajes posteriores que intentes enviar no se entregarán y no se te cobrará.

#### ¿Qué sucede si un usuario final reporta un mensaje? {#what-happens-if-an-end-user-reports-a-message}
Si un usuario final reporta un mensaje, aún puedes enviar mensajes posteriores a este usuario. Sin embargo, los reportes pueden afectar tu calificación de calidad en el canal.

#### Si un usuario final bloquea o reporta mi empresa, ¿se actualizará su estado de suscripción en Braze? {#if-an-end-user-blocks-or-reports-my-business-will-their-subscription-status-be-updated-in-braze}
No. Su estado de suscripción en Braze no se actualizará.

### Varios {#miscellaneous}

#### ¿Braze admite casos de uso de atención al cliente como chatbots y chat asistido por humanos para WhatsApp? {#does-braze-support-customer-support-use-cases-like-chatbots-and-human-assisted-chat-for-whatsapp}
No admitimos chatbots ni chat asistido por humanos dentro de Braze ni a través de integraciones directas.

Si ya usas WhatsApp como canal de atención al cliente, te recomendamos mantener tu configuración actual y crear una nueva WABA a través de Braze para mensajería de marketing. Esta WABA requerirá un nuevo número de teléfono.

#### ¿Cómo puedo "cerrar la brecha" entre mi mensajería de atención al cliente y mi mensajería de marketing a través de Braze? {#how-can-i-bridge-the-gap-between-my-customer-support-messaging-and-my-marketing-messaging-via-braze}
Puedes usar las propiedades Liquid de WhatsApp para reenviar el contenido de mensajes entrantes de WhatsApp (incluyendo el cuerpo del mensaje y las URL de medios) desde Braze a otras plataformas, incluyendo cualquier herramienta de atención al cliente. Para más detalles, consulta nuestras [etiquetas de personalización compatibles]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

Para enviar información a Braze, por ejemplo, para indicar que un usuario está en una conversación de soporte activa, puedes registrar un atributo personalizado (como un booleano "tiene chat de soporte existente = verdadero/falso") y usarlo como criterio de segmentación en sus campañas de marketing. También puedes crear vínculos profundos entre dos hilos de chat para dirigir a los usuarios al hilo de soporte desde el hilo de marketing y viceversa.

#### ¿Braze almacena las respuestas de los usuarios? {#does-braze-store-user-responses}
Los mensajes solo se almacenan el tiempo suficiente para procesarlos. Para acceder a los mensajes de los usuarios, usa Currents.

#### ¿Cómo deben almacenarse los números de teléfono de los usuarios en Braze? {#how-do-user-phone-numbers-need-to-be-stored-in-braze}
Los números de teléfono de los usuarios deben almacenarse en [formato E.164]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers#formatting).

#### ¿Qué tipo de medios enriquecidos son compatibles en las plantillas de WhatsApp? {#what-kind-of-rich-media-is-supported-in-whatsapp-templates}
Puedes añadir imágenes, llamadas a la acción (URL o número de teléfono) y botones de respuesta rápida a las plantillas de WhatsApp. Puedes añadir estos elementos cuando construyes plantillas directamente en WhatsApp.

#### ¿Puedo importar números de teléfono de usuarios? {#can-i-import-user-phone-numbers}
Sí. Puedes [importar números de teléfono de usuarios]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers).

#### ¿Qué es la verificación de empresa? {#what-is-business-verification}
La verificación de empresa es un concepto de WhatsApp utilizado para asegurar que la marca es un negocio legítimo. Se puede completar en WhatsApp Manager. La verificación de empresa también es necesaria para escalar la mensajería. Sin la verificación de empresa, los clientes solo pueden enviar hasta 250 usuarios finales únicos en un período continuo de 24 horas.

#### ¿Qué es una cuenta de empresa oficial? {#what-is-an-official-business-account}
OBA te da la marca de verificación verde junto a tu nombre de visualización y es opcional. Puedes solicitar una cuenta de empresa oficial después de completar la verificación de empresa. Ten en cuenta que la verificación de empresa y una cuenta de empresa oficial son conceptos diferentes de WhatsApp.

#### ¿Qué métricas están disponibles en el dashboard de Braze? {#what-metrics-are-available-in-the-braze-dashboard}
Puedes ver destinatarios únicos, envíos, entregas, lecturas y fallos en el dashboard de Braze. Ten en cuenta que los recibos de lectura de los usuarios finales deben estar "activados" para que Braze pueda rastrear las lecturas. También puedes configurar eventos de conversión para monitorizar el rendimiento de la Campaign, de manera similar a otros canales.

#### ¿Qué es una conversación de WhatsApp? {#what-is-a-whatsapp-conversation}
WhatsApp es un canal enfocado en la mensajería bidireccional y, por lo tanto, se basa en conversaciones (en lugar del número de mensajes individuales). Una conversación es un hilo de 24 horas entre una empresa y un usuario final.

- **Conversación iniciada por la empresa**: una conversación en la que la empresa comienza enviando un mensaje de plantilla aprobado al usuario final. Tan pronto como la empresa envía un mensaje, comienza la ventana de 24 horas.
- **Conversación iniciada por el usuario**: una conversación en la que el usuario final envía un mensaje a la empresa. Cuando la empresa envía un mensaje en respuesta, comienza la ventana de 24 horas.

#### ¿Qué factores afectan la calificación de calidad del número de teléfono y qué sucede cuando mi calificación de calidad baja demasiado? {#what-factors-affect-phone-number-quality-rating-and-what-happens-when-my-quality-rating-drops-too-low}
Los factores que afectan la calificación de calidad del número de teléfono incluyen que un usuario final bloquee una empresa (y las razones que proporciona al bloquearla) y que un usuario final reporte una empresa.

Cuando una calificación de calidad es baja, el estado del número de teléfono cambia de **Connected** a **Flagged**. Si la calidad no mejora en siete días, el estado vuelve a **Connected**. Sin embargo, el límite de mensajería disminuirá al siguiente nivel. Por ejemplo, un número de teléfono que solía tener un límite de mensajería de 100 000 ahora tiene un límite de mensajería de 10 000.

#### ¿Qué pasa si mi plantilla fue marcada erróneamente por violar la política de comercio de WhatsApp? {#what-if-my-template-was-falsely-flagged-for-violating-whatsapps-commerce-policy}

Si crees que Meta marcó tu plantilla erróneamente, usa el enlace de revisión en el correo electrónico de WhatsApp para solicitar una nueva revisión. El equipo de WhatsApp Business revisa la decisión y la revierte si corresponde.