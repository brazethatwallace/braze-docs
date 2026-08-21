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

## Temas de preguntas frecuentes {#faq-topics}
- [Cuentas de WhatsApp Business](#whatsapp-business-accounts)
- [Número de teléfono de la cuenta de WhatsApp Business](#whatsapp-business-account-phone-numbers)
- [Adhesión voluntaria y gestión de suscripciones](#opt-in-and-subscription-management)
- [Límites de mensajería y calificación de calidad](#messaging-limits-and-quality-rating)
- [Plantillas y creador de WhatsApp](#whatsapp-templates-and-composer)
- [Capacidad de entrega y facturación](#deliverability-and-billing)
- [Integraciones, datos e informes](#integrations-data-and-reporting)
- [Medios e imágenes](#media-and-images)

### Cuentas de WhatsApp Business {#whatsapp-business-accounts}

#### ¿Cómo creo una cuenta de WhatsApp Business? {#how-do-i-create-a-whatsapp-business-account}
Recomendamos crear tu cuenta de WhatsApp Business (WABA) a través del flujo de registro integrado en el panel de Braze.

#### Ya tengo una cuenta de Meta Business. ¿Aún necesito una cuenta de WhatsApp Business? {#i-already-have-a-meta-business-account-do-i-still-need-a-whatsapp-business-account}
Sí, aún necesitas crear una cuenta de WhatsApp Business. Te recomendamos [anidar tu WABA dentro de tu cuenta principal de Meta Business]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup).

#### ¿Cómo accedo a mi cuenta de WhatsApp Business? {#how-do-i-access-my-whatsapp-business-account}
Después de completar el flujo de registro integrado, puedes acceder a tu cuenta en business.facebook.com navegando a la [sección de WhatsApp](https://business.facebook.com/wa/manage/home).

#### ¿Puedo conectar múltiples WABA a Braze? {#can-i-connect-multiple-wabas-to-braze}
Sí, puedes añadir hasta 10 cuentas de WhatsApp Business por espacio de trabajo, y cada cuenta de negocio puede estar anidada bajo un Meta Business Manager diferente.

![Diagrama del ecosistema de Braze y WhatsApp, que muestra cómo los espacios de trabajo y las cuentas de WhatsApp Business se conectan entre sí: puedes conectar un grupo de suscripción a un número de teléfono, múltiples cuentas de WhatsApp Business a un espacio de trabajo, y un espacio de trabajo a múltiples Meta Business Portfolios.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %})

#### ¿Puedo cambiar la moneda de mi cuenta de WhatsApp Business? {#can-i-change-my-whatsapp-business-account-currency}
No. Meta controla la moneda de tu cuenta de WhatsApp Business, y Braze no puede cambiarla ni convertirla. Para usar una moneda diferente, [crea una cuenta de WhatsApp Business separada]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) con esa moneda, o contacta con el soporte de Meta para preguntar si pueden actualizar la moneda en tu cuenta existente.

#### ¿Qué es la verificación de negocio? {#what-is-business-verification}
La verificación de negocio es un concepto de WhatsApp utilizado para asegurar que la marca es un negocio legítimo. Se puede completar en el WhatsApp Manager. La verificación de negocio también es necesaria para escalar la mensajería. Sin la verificación de negocio, los clientes solo pueden enviar mensajes a un máximo de 250 usuarios finales únicos en un período continuo de 24 horas.

#### ¿Qué es una cuenta de negocio oficial? {#what-is-an-official-business-account}
OBA te da la marca de verificación verde junto a tu nombre para mostrar y es opcional. Puedes solicitar una cuenta de negocio oficial después de completar la verificación de negocio. Ten en cuenta que la verificación de negocio y una cuenta de negocio oficial son conceptos diferentes de WhatsApp.

#### ¿Por qué podría ser rechazado mi nombre para mostrar de WhatsApp Business? {#why-might-my-whatsapp-business-display-name-be-rejected}
Los rechazos del nombre para mostrar de WhatsApp Business son gestionados por Meta. Si tu nombre para mostrar es rechazado, consulta las [directrices de nombre para mostrar de WhatsApp](https://faq.whatsapp.com/793641088597363) para conocer sus pautas.

Si tu nombre para mostrar cumple con las directrices y sigue siendo rechazado, Braze no puede ver las razones específicas. Sin embargo, la razón más común de rechazo es que la presencia en línea del negocio es demasiado baja, o que el negocio está comercializando [productos regulados o restringidos](https://business.whatsapp.com/policy#further-guidance).

Para más orientación sobre rechazos de nombres para mostrar, consulta [Recursos de Meta]({{site.baseurl}}/user_guide/channels/whatsapp/meta_resources).

### Números de teléfono de la cuenta de WhatsApp Business {#whatsapp-business-account-phone-numbers}
#### ¿Necesito un número de teléfono para mi cuenta de WhatsApp Business? {#do-i-need-a-phone-number-for-my-whatsapp-business-account}
Sí, necesitas un número al que tengas acceso. Se te pedirá que verifiques tu número de teléfono con autenticación de 2 factores cuando pases por el flujo de registro integrado. El número de teléfono no puede usarse para otras cuentas de WhatsApp (de negocio o personales).

#### ¿Qué tipos de números de teléfono son compatibles con WhatsApp? {#what-types-of-phone-numbers-are-supported-with-whatsapp}
Consulta los requisitos de Meta para [números de teléfono](https://developers.facebook.com/docs/whatsapp/phone-numbers) para más información.

#### ¿Puedo usar un número de teléfono en múltiples WABA? {#can-i-use-one-phone-number-across-multiple-wabas}
No. Un número de teléfono no puede compartirse entre múltiples WABA.

#### ¿Necesito un tipo específico de número de teléfono para enviar mensajes a países específicos? {#do-i-need-a-specific-type-of-phone-number-to-send-messages-to-specific-countries}
No. WhatsApp te permite enviar mensajes a usuarios finales desde cualquier número de teléfono compatible en cualquier país. Consulta los requisitos de Meta para [números de teléfono](https://developers.facebook.com/docs/whatsapp/phone-numbers) para más información.

#### ¿Cómo deben almacenarse los números de teléfono de los usuarios en Braze? {#how-do-user-phone-numbers-need-to-be-stored-in-braze}
Los números de teléfono de los usuarios deben almacenarse en [formato E.164]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers#formatting).

#### ¿Puedo importar números de teléfono de usuarios? {#can-i-import-user-phone-numbers}
Sí. Puedes [importar números de teléfono de usuarios]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers).

### Adhesión voluntaria y gestión de suscripciones {#opt-in-and-subscription-management}

#### ¿Necesito recopilar la adhesión voluntaria para enviar mensajes de marketing a usuarios finales en WhatsApp? {#do-i-need-to-collect-opt-in-to-send-marketing-messages-to-end-users-on-whatsapp}
Sí, WhatsApp requiere que las empresas [recopilen el consentimiento de adhesión voluntaria](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) para enviar mensajes de marketing a usuarios finales.

#### ¿Puedo enviar mensajes proactivamente a usuarios finales en WhatsApp para recopilar el consentimiento de adhesión voluntaria? {#can-i-proactively-message-end-users-on-whatsapp-to-collect-opt-in-consent}
Si eliges enviar mensajes proactivamente a usuarios finales, tu primer mensaje iniciado por el negocio debe preguntar al usuario si desea recibir mensajes de marketing de tu negocio y debe cumplir con los requisitos de Meta para [obtener la adhesión voluntaria](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Ten en cuenta que WhatsApp monitoreará la reputación de tu negocio en el canal, por lo que la mejor práctica recomendada es ser explícito con los usuarios finales y enviar solo mensajes que hayan indicado que desean recibir.

#### ¿Necesito recopilar el número de teléfono del usuario final cuando recopilo la adhesión voluntaria? {#do-i-need-to-collect-the-end-users-phone-number-when-i-collect-opt-in}
Necesitas tener el número de teléfono del usuario final en el perfil de Braze para enviarle mensajes.
- Si ya tienes su número, no necesitas recopilarlo durante la adhesión voluntaria.
- Si no tienes el número del usuario final, tu método de adhesión voluntaria debe incluir la captura del número de teléfono.

#### ¿Cómo actualizo el estado de suscripción de los usuarios finales que se adhieren? {#how-do-i-update-the-subscription-status-of-end-users-who-opt-in}
La gestión de suscripciones del canal de WhatsApp funciona de manera similar a como funciona en otros canales de Braze. Consulta [Gestión de suscripciones de usuarios]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups) para más información.

#### Si ya tengo una lista de usuarios que se han adherido para recibir mensajes de marketing en WhatsApp, ¿cómo actualizo su estado de suscripción en Braze? {#if-i-already-have-a-list-of-users-who-have-opted-in-to-receive-marketing-messages-on-whatsapp-how-do-i-update-their-subscription-status-in-braze}
Puedes actualizar su estado de suscripción mediante [importación de usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import#updating-subscription-group-status-optional).

#### ¿Qué métodos debo usar para recopilar adhesiones voluntarias? {#what-methods-should-i-use-to-collect-opt-ins}
Braze recomienda consultar las [directrices de Meta para métodos de adhesión voluntaria](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) para mantener el cumplimiento. Consulta [Adhesión voluntaria y cancelación de suscripción]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs) para métodos de configuración de Canvas y Campaigns.

#### ¿Se requiere doble adhesión voluntaria para WhatsApp? {#is-double-opt-in-required-for-whatsapp}
No, la doble adhesión voluntaria no es obligatoria.

#### ¿Cómo cancelan la suscripción mis usuarios a los mensajes de WhatsApp? {#how-do-my-users-opt-out-of-whatsapp-messages}
Tus usuarios pueden cancelar la suscripción de dos maneras:
1. Configura un mensaje entrante de WhatsApp con una palabra específica de cancelación de suscripción y usa un webhook para actualizar el estado de suscripción del usuario.
2. Añade una respuesta rápida de cancelación de suscripción dentro de la plantilla de WhatsApp, con un webhook correspondiente para actualizar.

#### ¿Puedo usar un grupo de suscripción de WhatsApp de Braze si envío mensajes de WhatsApp a través de un tercero? {#can-i-use-a-braze-whatsapp-subscription-group-if-i-send-whatsapp-messages-through-a-third-party}
No. Los grupos de suscripción de WhatsApp de Braze se aplican a los mensajes enviados a través del canal de WhatsApp de Braze. Si envías mensajes de WhatsApp a través de un proveedor externo o integraciones personalizadas fuera de las Campaigns y Canvas de WhatsApp de Braze, puedes almacenar el consentimiento de adhesión voluntaria en un atributo personalizado (o tu propio modelo de suscripción) y usar ese atributo para segmentación y elegibilidad. Para patrones relacionados cuando Braze es propietario del número de WhatsApp, consulta [¿Cómo conecto el soporte y el marketing de WhatsApp en Braze?](#how-do-i-connect-whatsapp-support-and-marketing-in-braze).

### Límites de mensajería y calificación de calidad {#messaging-limits-and-quality-rating}

#### ¿Qué son los límites de mensajería? {#what-are-messaging-limits}
Los límites de mensajería son un concepto de integridad de WhatsApp. Determinan el número máximo de conversaciones iniciadas por el negocio que cada número de teléfono puede iniciar en un período continuo de 24 horas. Hay cuatro niveles de límite de mensajería: 1k, 10k, 100k e ilimitado.

#### ¿Cómo aumento mi límite de mensajería? {#how-do-i-increase-my-messaging-limit}
WhatsApp aumentará tu límite de mensajería si cumples las siguientes condiciones:
1. El [estado del número de teléfono](https://www.facebook.com/business/help/896873687365001) es **Connected**
2. La [calificación de calidad del número de teléfono](https://www.facebook.com/business/help/896873687365001) es **Medium** o **High**
3. En los últimos siete días, has iniciado X o más conversaciones con usuarios únicos, donde X es tu límite de mensajería actual dividido entre 2

Entonces, para pasar de 100k a ilimitado, debes enviar al menos 50 000 conversaciones iniciadas por el negocio en un período de 7 días.

#### ¿Cuánto tiempo tarda en aumentar mis límites de mensajería? {#how-long-does-it-take-to-increase-my-messaging-limits}
Si se cumplen todas las condiciones anteriores, puedes aumentar tu límite de mensajería de 1k a ilimitado en 4 días.

#### ¿Dónde puedo ver mi límite de mensajería actual? {#where-can-i-see-my-current-messaging-limit}
Puedes verificar tus límites de mensajería actuales en la pestaña **WhatsApp Manager > Overview Dashboard > Insights**.

#### ¿Qué sucede si intento enviar mensajes cuando ya he alcanzado mi límite de mensajería? {#what-happens-if-i-attempt-to-send-messages-when-i-have-already-reached-my-messaging-limit}
Si intentas enviar una Campaign o Canvas a más usuarios únicos de los que permite tu límite actual, los mensajes no se enviarán. Braze seguirá intentando reenviar los mensajes si/cuando tu límite de mensajería aumente durante un máximo de un día.

#### ¿Puede disminuir mi límite de mensajería? {#can-my-messaging-limit-decrease}
Sí, si la calificación de calidad de tu número de teléfono baja demasiado, corres el riesgo de que WhatsApp disminuya tu límite de mensajería. Braze recomienda que te suscribas y recibas notificaciones de actualizaciones relacionadas con la calidad de WhatsApp, incluyendo actualizaciones del estado de tu número de teléfono y el nivel de límite de mensajería. Puedes suscribirte a las notificaciones directamente en el panel de WhatsApp Manager.

#### ¿Qué factores afectan la calificación de calidad del número de teléfono, y qué sucede cuando mi calificación de calidad baja demasiado? {#what-factors-affect-phone-number-quality-rating-and-what-happens-when-my-quality-rating-drops-too-low}
Los factores que afectan la calificación de calidad del número de teléfono incluyen que un usuario final bloquee un negocio (y las razones que proporciona al bloquearlo) y que un usuario final reporte un negocio.

Cuando una calificación de calidad es baja, el estado del número de teléfono cambia de **Connected** a **Flagged**. Si la calidad no mejora en siete días, el estado vuelve a **Connected**. Sin embargo, el límite de mensajería disminuirá al siguiente nivel. Por ejemplo, un número de teléfono que solía tener un límite de mensajería de 100 000 ahora tiene un límite de mensajería de 10 000.

#### ¿Cuál es el límite de rendimiento de Meta? {#what-is-the-meta-throughput-limit}
Meta tiene su propio límite de rendimiento separado del límite de mensajería de WABA. El límite predeterminado que admite la API en la nube es de 80 mensajes por segundo. Si crees que tus Campaigns superarán este límite, puedes [solicitar](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/#throughput) que se aumente tu límite. Meta recomienda que envíes esta solicitud al menos tres días antes de los envíos de la Campaign.

### Plantillas y creador de WhatsApp {#whatsapp-templates-and-composer}

#### ¿Qué es una plantilla de WhatsApp? {#what-is-a-whatsapp-template}
WhatsApp requiere que todos los mensajes iniciados por el negocio comiencen usando una plantilla aprobada. La plantilla incluye el texto del mensaje, junto con medios enriquecidos opcionales como imágenes, llamadas a la acción y botones de respuesta rápida. Después de que WhatsApp aprueba las plantillas, se pueden usar para componer un mensaje de WhatsApp en Braze.

#### ¿Dónde creo, edito y gestiono mis plantillas de WhatsApp? {#where-do-i-create-edit-and-manage-my-whatsapp-templates}
Puedes crear y enviar plantillas en Braze usando el [Constructor de plantillas de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder), o en el WhatsApp Manager de Meta. Las plantillas creadas en cualquiera de las dos ubicaciones aparecen en el panel de Braze con un indicador de estado. Después del envío, los campos bloqueados requieren la re-aprobación de Meta; consulta las [limitaciones de edición en las preguntas frecuentes del Constructor de plantillas]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder#can-i-edit-a-template-after-its-been-approved) para más detalles.

#### ¿Cuánto tiempo tarda WhatsApp en revisar el envío de una plantilla? {#how-long-does-it-take-whatsapp-to-review-a-template-submission}
El proceso de aprobación puede tardar hasta 24 horas, pero a menudo las plantillas se procesan en cuestión de horas o minutos.

#### ¿Cuántas plantillas puedo tener en un momento dado? {#how-many-templates-can-i-have-at-a-given-time}
Tu límite de plantillas de mensaje depende de tu estado de verificación de negocio. Puedes verificar tu límite en la página **WhatsApp Manager > Message Templates**.

#### ¿Cómo personalizo el texto de la plantilla y los medios enriquecidos en Braze? {#how-do-i-personalize-template-copy-and-rich-media-in-braze}
WhatsApp permite insertar parámetros variables en las plantillas de mensaje. Los mensajes no pueden comenzar ni terminar con un parámetro variable. Los parámetros variables se pueden rellenar con lógica Liquid en la plataforma Braze. Consulta [componer un mensaje de WhatsApp en Braze]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message) para aprender más sobre los parámetros variables.

#### Mi plantilla fue rechazada. ¿Puede Braze ayudarme a que sea aprobada? {#my-template-got-rejected-can-braze-help-me-get-it-approved}
El equipo de Braze no tiene visibilidad sobre los rechazos de plantillas. Debes trabajar directamente con tu WhatsApp Business Manager para editar y reenviar la plantilla. Asegúrate de proporcionar una plantilla de ejemplo cuando sea necesario. Verifica que tu plantilla cumple con las políticas de [negocio](https://www.whatsapp.com/legal/business-policy/?fbclid=IwAR2qWg6yFKdyjDMxJkbNSM38FLGsxXxffC1qStY2gaHOyp-gl_8g72rZNIw) o [comercio](https://www.whatsapp.com/legal/commerce-policy/?fbclid=IwAR3bzN3LTZ-7kO-wnO7X3smtPKGy0asxaFod-U1Ub8B9JUpnrfy1_y7LpAQ) de Meta.

#### ¿Se pueden segmentar o personalizar los medios enriquecidos en Braze? {#can-rich-media-be-targeted-or-personalized-in-braze}
Sí. Puedes subir imágenes estáticas desde la biblioteca de medios, o añadir imágenes por URL y personalizarlas con [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) o [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content). Las URL de imágenes admiten lógica Liquid completa en cualquier parte de la URL. Esto se aplica a mensajes de plantilla y mensajes de respuesta (mensajes de medios y diseños de respuesta rápida). Para más detalles, consulta [Imágenes dinámicas]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#dynamic-images).

#### ¿Qué tipo de medios enriquecidos son compatibles en las plantillas de WhatsApp? {#what-kind-of-rich-media-is-supported-in-whatsapp-templates}
Puedes añadir imágenes, llamadas a la acción (URL o número de teléfono) y botones de respuesta rápida a las plantillas de WhatsApp. Puedes añadir estos elementos cuando construyes plantillas directamente en WhatsApp.

#### ¿Qué pasa si mi plantilla fue marcada erróneamente por violar la política de comercio de WhatsApp? {#what-if-my-template-was-falsely-flagged-for-violating-whatsapps-commerce-policy}
Si crees que Meta marcó erróneamente tu plantilla, usa el enlace de revisión en el correo electrónico de WhatsApp para solicitar una re-revisión. El equipo de WhatsApp Business revisa la decisión y la revierte si corresponde.

#### ¿Por qué mi plantilla de WhatsApp importada muestra "Message Incomplete" en el creador? {#why-does-my-imported-whatsapp-template-show-message-incomplete-in-the-composer}
La advertencia "Message Incomplete" aparece cuando los espacios de variables requeridos de la plantilla no están rellenados con valores válidos en el creador.

Cuando creas plantillas usando el [Constructor de plantillas de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder), Braze renumera las variables en marcadores de posición secuenciales ({% raw %}`{{1}}`, `{{2}}`, `{{3}}`{% endraw %}, y así sucesivamente). Las plantillas creadas externamente en el WhatsApp Manager de Meta pueden incluir patrones que hacen que el mapeo de variables sea propenso a errores, como:

- Numeración no secuencial (por ejemplo, {% raw %}`{{1}}`, `{{3}}`, `{{5}}`{% endraw %})
- Variables faltantes en la secuencia (por ejemplo, omitir {% raw %}`{{2}}`{% endraw %})
- Variables que comienzan en un número diferente a 1

Para resolver esto, edita tu plantilla en el WhatsApp Manager de Meta para usar formato de marcadores de posición secuenciales, luego vuelve a importarla en Braze. En Braze, confirma que cada campo de variable requerido esté rellenado con un valor Liquid válido.

#### ¿Por qué mi Campaign de WhatsApp no se envía a pesar de que la plantilla se previsualiza correctamente? {#why-is-my-whatsapp-campaign-not-sending-despite-template-previewing}
Si tu plantilla se previsualiza correctamente pero el registro de procesamiento muestra **Abort** con detalles "Param text cannot have new-line/tab characters or more than 4 consecutive spaces", verifica los valores de parámetros con plantillas Liquid en tu mensaje. WhatsApp requiere que los valores de texto de los parámetros no contengan:

- Caracteres de nueva línea
- Caracteres de tabulación
- Más de 4 espacios consecutivos

Confirma que cualquier lógica Liquid que rellene los parámetros de la plantilla elimine estos caracteres o formatee el texto adecuadamente antes del envío.

### Capacidad de entrega y facturación {#deliverability-and-billing}

#### ¿Por qué no se entregaría un mensaje? {#why-would-a-message-not-be-delivered}
Hay varias razones por las que un mensaje podría no entregarse, incluyendo problemas de red y que el dispositivo esté apagado.

#### Si un mensaje no se entrega, ¿se me cobrará? {#if-a-message-is-not-delivered-will-i-be-billed}
No. Si un mensaje no se entrega, no se te cobra.

#### ¿Qué sucede si un usuario bloquea mi negocio? {#what-happens-if-a-user-blocks-my-business}
Si un usuario bloquea tu negocio, los mensajes posteriores que intentes enviar no se entregan, y no se te cobra. El estado de suscripción del usuario no se actualiza.

#### ¿Qué sucede si un usuario reporta un mensaje? {#what-happens-if-a-user-reports-a-message}
Si un usuario reporta un mensaje, aún puedes enviar mensajes posteriores. Sin embargo, los reportes pueden afectar tu calificación de calidad en el canal. El estado de suscripción del usuario no se actualiza.

#### ¿Cómo puedo excluir a los usuarios que reportan mi cuenta de WhatsApp de futuros lanzamientos? {#how-can-i-exclude-users-who-report-my-whatsapp-account-from-upcoming-launches}
Braze no recibe notificaciones de WhatsApp cuando tu cuenta es marcada o reportada, por lo que no puedes identificar ni excluir automáticamente a esos usuarios en Braze. Los usuarios que reportan tu cuenta pueden permanecer en tu grupo de suscripción de WhatsApp y seguir siendo elegibles para futuros mensajes.

Sin embargo, puedes configurar una Campaign que se desencadene cuando un usuario responda con una palabra clave de cancelación de suscripción, lo que automáticamente cancela su suscripción usando el [endpoint `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status). Para más información, consulta [Proceso de adhesión voluntaria y cancelación de suscripción de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-opt-in-and-opt-out-process).

#### ¿Braze admite respaldo automático por SMS cuando falla la entrega de WhatsApp? {#does-braze-support-automatic-sms-fallback-when-whatsapp-delivery-fails}

No. Braze no ofrece una ruta nativa de respaldo de WhatsApp a SMS. Para reintentar en otro canal, segmenta a los usuarios con envíos fallidos de WhatsApp (por ejemplo, a través de eventos de fallo de Currents) y dirige una Campaign de SMS o correo electrónico.

#### ¿Son gratuitos los mensajes de respuesta de WhatsApp? {#are-whatsapp-response-messages-free}

Los mensajes de respuesta compuestos en el editor de Campaign o Canvas de Braze (no plantillas aprobadas de WhatsApp) son tratados como mensajes de servicio por Meta. Los mensajes de servicio enviados a través de la integración nativa de WhatsApp de Braze no consumen créditos de acción cuando se envían como [mensajes de respuesta]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages) dentro de una ventana abierta de servicio al cliente.

| Tipo de mensaje | Créditos de acción | Notas |
|---|---|---|
| Mensaje de respuesta (respuesta entrante) | No se consumen | Compuesto en Braze; no es una plantilla aprobada por Meta. |
| Mensaje de plantilla | Se consumen | Las plantillas de marketing, utilidad, autenticación y oferta por tiempo limitado se facturan por envío. |
| Plantilla de utilidad en ventana de servicio | No se consumen por Meta | Meta no cobra por plantillas de utilidad enviadas dentro de las 24 horas de un mensaje iniciado por el usuario. El consumo de créditos de acción sigue tu contrato. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Créditos de acción de mensajes de respuesta" }

Para flujos de Canvas donde los usuarios tocan respuestas rápidas después de la ventana original de 24 horas, consulta [Respuestas rápidas y mensajes entrantes fuera de la ventana de 24 horas]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window).

#### ¿Qué sucede si un usuario responde o toca una respuesta rápida después de que se cierra la ventana de 24 horas? {#what-happens-if-a-user-replies-or-taps-a-quick-reply-after-the-24-hour-window-closes}
Se abre una nueva ventana de servicio al cliente de 24 horas. Consulta [Respuestas rápidas y mensajes entrantes fuera de la ventana de 24 horas]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window).

#### ¿Necesito configurar mi Action Path de Canvas a 31 días para las respuestas rápidas de WhatsApp? {#do-i-need-to-set-my-canvas-action-path-to-31-days-for-whatsapp-quick-replies}
No. La duración predeterminada del Action Path es suficiente. Consulta [Respuestas rápidas y mensajes entrantes fuera de la ventana de 24 horas]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window).

#### ¿Puedo ver cuántos créditos de WhatsApp consumió una Campaign o Canvas específico? {#can-i-see-how-many-whatsapp-credits-a-specific-campaign-or-canvas-consumed}
No en el panel de Braze actualmente. Los análisis de Campaign y Canvas muestran envíos, entregas y fallos, pero no el consumo de créditos por mensaje. Los conteos de envíos no se alinean uno a uno con el uso de créditos porque la categoría de la plantilla y el tipo de mensaje afectan la facturación de manera diferente. Para detalles de facturación, consulta [¿Son gratuitos los mensajes de respuesta de WhatsApp?](#are-whatsapp-response-messages-free).

### Integraciones, datos e informes {#integrations-data-and-reporting}

#### ¿Por qué WhatsApp no aparece en Technology Partners? {#why-isnt-whatsapp-listed-under-technology-partners}
WhatsApp aparece en la página de **Technology Partners** cuando WhatsApp está habilitado para tu empresa. Si no ves WhatsApp en esa página, contacta a tu equipo de cuenta de Braze para confirmar que WhatsApp está aprovisionado para tu panel.

#### ¿Braze admite casos de uso de soporte al cliente como chatbots y chat asistido por humanos para WhatsApp? {#does-braze-support-customer-support-use-cases-like-chatbots-and-human-assisted-chat-for-whatsapp}
No admitimos chatbots ni chat asistido por humanos dentro de Braze ni a través de integraciones directas.

Si ya usas WhatsApp como canal de soporte al cliente, te recomendamos mantener tu configuración actual y crear una nueva WABA a través de Braze para mensajería de marketing. Esta WABA requerirá un nuevo número de teléfono.

#### ¿Cómo conecto el soporte y el marketing de WhatsApp en Braze? {#how-do-i-connect-whatsapp-support-and-marketing-in-braze}

Puedes usar las propiedades Liquid de WhatsApp para reenviar el contenido de mensajes entrantes de WhatsApp (incluyendo el cuerpo del mensaje y las URL de medios) desde Braze a otras plataformas, incluyendo cualquier herramienta de soporte al cliente. Para más detalles, consulta nuestras [Etiquetas de personalización compatibles]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

Para enviar información a Braze, por ejemplo, para indicar que un usuario está en una conversación de soporte activa, puedes registrar un atributo personalizado (como un booleano "has existing support chat = true/false") y usarlo como criterio de segmentación en sus Campaigns de marketing. También puedes crear vínculos profundos entre dos hilos de chat para dirigir a los usuarios al hilo de soporte desde el hilo de marketing y viceversa.

#### ¿Braze almacena las respuestas de los usuarios? {#does-braze-store-user-responses}
Los mensajes solo se almacenan el tiempo suficiente para procesarlos. Para acceder a los mensajes de los usuarios, usa Currents.

#### ¿Qué métricas están disponibles en el panel de Braze? {#what-metrics-are-available-in-the-braze-dashboard}
Puedes ver destinatarios únicos, envíos, entregas, lecturas y fallos en el panel de Braze. Ten en cuenta que los recibos de lectura del usuario deben estar activados para que Braze rastree las lecturas. También puedes configurar eventos de conversión para monitorear el rendimiento de la Campaign, de manera similar a otros canales.

#### ¿Qué es una conversación de WhatsApp? {#what-is-a-whatsapp-conversation}
WhatsApp es un canal enfocado en la mensajería bidireccional y por lo tanto se basa en conversaciones (en lugar del número de mensajes individuales). Una conversación es un hilo de 24 horas entre un negocio y un usuario final.

- **Conversación iniciada por el negocio**: una conversación donde el negocio comienza enviando un mensaje de plantilla aprobado al usuario final. Tan pronto como el negocio envía un mensaje, comienza la ventana de 24 horas.
- **Conversación iniciada por el usuario**: una conversación donde el usuario final envía un mensaje al negocio. Cuando el negocio envía un mensaje en respuesta, comienza la ventana de 24 horas.

### Medios e imágenes {#media-and-images}

#### ¿Por qué no se cargan las imágenes cuando se envían como mensaje de WhatsApp? {#why-wont-images-load-when-sent-as-a-whatsapp-message}
Si los usuarios reportan que las imágenes en los mensajes de WhatsApp no se descargan o el ícono de descarga no responde, esto probablemente se debe a un problema conocido en versiones anteriores de la aplicación de WhatsApp. Este problema generalmente se puede resolver actualizando el dispositivo a la versión más reciente de WhatsApp.