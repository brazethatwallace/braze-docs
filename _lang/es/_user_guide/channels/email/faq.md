---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre correo electrónico
page_order: 30
description: "Esta página ofrece respuestas a preguntas frecuentes sobre la mensajería por correo electrónico."
channel: email

---

# Preguntas frecuentes {#frequently-asked-questions}

> Este artículo ofrece respuestas a algunas preguntas frecuentes sobre los correos electrónicos.

## ¿Qué pasa cuando se envía un correo electrónico y varios perfiles tienen la misma dirección de correo electrónico? {#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address}

Si varios usuarios con direcciones de correo electrónico coincidentes están en un Segment para recibir una Campaign, se selecciona un único perfil de usuario con esa dirección de correo electrónico en el momento del envío. De esta forma, el correo electrónico se envía solo una vez y se deduplica, asegurando que no llegue a la misma dirección de correo electrónico varias veces.

**Direcciones de correo electrónico únicas:** Braze no aplica unicidad de las direcciones de correo electrónico entre perfiles. Si dependes de una relación uno a uno entre una dirección de correo electrónico y un perfil, monitoriza internamente la existencia de duplicados al crear usuarios.

**Deduplicación antes de Liquid:** Para envíos en los que Braze deduplica por dirección de correo electrónico dentro de un mismo despacho (por ejemplo, Campaigns programadas donde varios miembros del Segment con la misma dirección se procesan juntos), esa deduplicación ocurre antes de que Liquid se ejecute para el perfil elegido para representar esa dirección. Si Liquid aborta para ese perfil (por ejemplo, con [`abort_message()`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)), esa dirección no recibe el mensaje en ese despacho, incluidos los perfiles ya omitidos por la deduplicación. Los envíos disparados no aplican esa misma deduplicación de direcciones dentro del despacho; varios perfiles que comparten una dirección pueden seguir siendo elegibles en un mismo lote, por lo que este comportamiento de aborto no se aplica de la misma manera (consulta el siguiente párrafo).

Si varios perfiles comparten una dirección de correo electrónico y un perfil cancela su suscripción, Braze actualiza otros perfiles (hasta 100) con esa dirección al mismo estado de suscripción. Esto se aplica a cancelaciones de suscripción y otros cambios como el estado de suscripción global y los estados individuales de los grupos de suscripción.

**Grupos semilla:** Para Campaigns con [grupos semilla]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups), Braze selecciona un perfil para la entrega principal cuando varios perfiles comparten una dirección. Ese destinatario principal podría no estar en tu grupo semilla, incluso cuando otro perfil con la misma dirección sí lo está.

Los siguientes escenarios pueden hacer parecer que un usuario recibió un correo electrónico dos veces:

- **Listas semilla o destinatarios de prueba:** Las direcciones semilla y los destinatarios de prueba internos pueden recibir un envío además de tu audiencia principal, lo que puede parecer un duplicado cuando un buzón de entrada coincide tanto con un perfil como con una entrada semilla.
- **Ocurrió un error durante la creación de la Campaign o Canvas:** El usuario puede no recibir el mismo envío dos veces, pero puede recibir dos correos electrónicos separados con la misma línea del asunto. Cuando una Campaign o Canvas se duplica, verifica los detalles de configuración del correo electrónico, como las imágenes o las líneas del asunto. También puedes consultar los registros de cambios para ver si la Campaign o Canvas fue modificado después del lanzamiento; un duplicado puede compartir la misma línea del asunto que el original cuando el usuario lo recibió.
- **Varios perfiles de usuario tienen reenvío de correo electrónico:** Si un usuario tiene varias cuentas en una aplicación determinada pero una cuenta reenvía correos, el usuario recibe la Campaign una vez por buzón de entrada; el correo puede aparecer dos veces en el buzón de entrada donde se reenvían los mensajes. Solo algunos proveedores indican cuándo un correo electrónico fue reenviado desde otra cuenta.
- **Configuración del correo electrónico en el destinatario:** Algunos clientes fusionan buzones de entrada ("buzón universal"). Si la misma Campaign se dirige a varias cuentas que comparten un buzón de entrada, puede parecer que una persona recibió la Campaign dos veces cuando en realidad se enviaron mensajes a dos perfiles distintos. El destinatario puede confirmar si varias cuentas están combinadas en un solo buzón de entrada.

Esta deduplicación se aplica cuando los usuarios segmentados están en el mismo despacho. La reelegibilidad se evalúa por perfil, no por dirección de correo electrónico.

La reelegibilidad de Campaigns de correo electrónico y pasos en Canvas utiliza el perfil de cada usuario, no el buzón de entrada, por lo que varios perfiles pueden calificar para envíos separados mientras se cumple esa lógica. Combinado con disparadores, esto puede entregar más de un mensaje al mismo buzón de entrada incluso cuando intentas respetar un período de inelegibilidad único a nivel de dirección. Las Campaigns disparadas (excluyendo las Campaigns disparadas por API) y Canvas también pueden enviar dos veces a una dirección cuando diferentes perfiles con direcciones de correo electrónico coincidentes cumplen el disparador en diferentes momentos, por ejemplo, si el usuario A y el usuario B comparten `johndoe@example.com` pero están en diferentes zonas horarias mientras la entrega utiliza zonas horarias locales.

Los usuarios no se deduplican por correo electrónico en la entrada al Canvas, por lo que pueden no deduplicarse más allá del primer paso de un Canvas si progresan en momentos ligeramente diferentes debido a una entrada con límite de velocidad. Cuando un usuario asociado con una dirección de correo electrónico determinada abre o hace clic en un correo electrónico, todos los perfiles de usuario que comparten esa dirección de correo electrónico se marcan como que abrieron o hicieron clic en la Campaign.

### Excepción: Campaigns disparadas por API {#exception-api-triggered-campaigns}

Las Campaigns disparadas por API deduplicarán o enviarán duplicados dependiendo de dónde se defina la audiencia. Los correos electrónicos duplicados deben ser segmentados por separado en la llamada a la API usando `user_ids` distintos para recibir múltiples entregas. Aquí hay tres posibles escenarios para Campaigns disparadas por API:

- **Escenario 1: Correos electrónicos duplicados en el Segment objetivo:** Si el mismo correo electrónico aparece en varios perfiles de usuario que están agrupados en los filtros de audiencia del panel para una Campaign disparada por API, solo uno de los perfiles recibe el correo electrónico.
- **Escenario 2: Correos electrónicos duplicados en diferentes `user_ids` dentro del objeto recipients:** Si el mismo correo electrónico aparece dentro de múltiples valores `external_user_id` referenciados por el objeto `recipients`, el correo electrónico se envía dos veces.
- **Escenario 3: Correos electrónicos duplicados debido a `user_ids` duplicados dentro del objeto recipients:** Si intentas agregar el mismo perfil de usuario dos veces, solo uno de los perfiles recibe el correo electrónico.

{% alert important %}
Si envías una Campaign de API a través de una llamada a la API (excluyendo las Campaigns disparadas por API), y se especifican varios usuarios en la audiencia del Segment con la misma dirección de correo electrónico, se envía a esa dirección tantas veces como esté listada en la llamada. Esto se debe a que se asume que las llamadas a la API son construidas intencionalmente.
{% endalert %}

#### Pruebas A/B con direcciones de correo electrónico duplicadas {#ab-testing-with-duplicate-email-addresses}

Evita las [pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing) en correo electrónico cuando varios perfiles pueden compartir la misma dirección de correo electrónico. Las variantes se asignan por perfil, lo que puede producir más de un mensaje al mismo buzón de entrada. Si necesitas hacer pruebas en esa situación, no combines un paso de **variante ganadora** con [entrega en zona horaria local]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns) de una manera que retrase la selección del ganador; esas opciones juntas pueden aumentar la probabilidad de envíos duplicados.

#### Canvas y direcciones de correo electrónico duplicadas {#canvas-and-duplicate-email-addresses}

Para recorridos en Canvas, que las direcciones de correo electrónico duplicadas reciban un envío o más de uno puede depender del lote de entrada, la temporización de los pasos y otros factores. Considera el comportamiento como indefinido hasta que lo valides para tu recorrido. Cuando sea posible, fusiona o consolida los perfiles duplicados. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="deterministic deduplication for duplicate email addresses in Canvas" %}

### ¿Qué pasa con el estado de suscripción cuando la dirección de correo electrónico de un usuario cambia a una compartida por otro usuario? {#what-happens-to-the-subscription-state-when-a-users-email-address-changes-to-one-shared-by-another-user}

Si configuras o actualizas la dirección de correo electrónico del usuario A a otra dirección de correo electrónico que es compartida por un usuario B existente, el usuario A hereda el estado de suscripción que ya existe del usuario B, a menos que la configuración **Resuscribir usuarios cuando actualicen su correo electrónico** esté activada.

### ¿Las actualizaciones en mi configuración de correo electrónico saliente se aplicarán retroactivamente? {#will-updates-to-my-outbound-email-settings-apply-retroactively}

No. Las actualizaciones realizadas en la configuración de correo electrónico saliente no afectan retroactivamente a los envíos existentes. Por ejemplo, cambiar tu nombre para mostrar predeterminado en la configuración de correo electrónico no reemplazará automáticamente el nombre para mostrar predeterminado existente en tus Campaigns o Canvas activos.

### ¿Qué es una "buena" tasa de entrega de correo electrónico? {#what-is-a-good-email-delivery-rate}

Normalmente, el "número mágico" es alrededor del 98 % de los mensajes entregados con una tasa de rebote no superior al 3 %. Si menos del 98 % de los mensajes se entregan, normalmente hay motivo de preocupación.

Sin embargo, una tasa de entrega del 98 % o superior aún puede tener problemas de capacidad de entrega. Por ejemplo, si todos tus rebotes provienen de un solo dominio, eso es una señal clara de un problema de reputación con ese proveedor.

Además, los mensajes pueden estar siendo entregados y terminando en correo no deseado, lo que indica problemas de reputación potencialmente graves. Es importante monitorizar no solo el número de mensajes que se entregan, sino también las tasas de apertura y clics para determinar si los usuarios realmente están viendo los mensajes en sus buzones de entrada. Dado que los proveedores normalmente no reportan cada instancia de correo no deseado, una tasa de correo no deseado incluso del 1 % podría ser motivo de preocupación y análisis adicional.

Finalmente, tu negocio y los tipos de correos electrónicos que envías también pueden afectar la entrega. Por ejemplo, alguien que envía principalmente [correos transaccionales]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email) debería esperar ver una tasa mejor que alguien que envía muchos mensajes de marketing.

### ¿Por qué mis métricas de entrega de correo electrónico no suman el 100 %? {#why-are-my-email-delivery-metrics-not-adding-up-to-100}

Las métricas de entrega de correo electrónico (entregas, rebotes y tasa de correo no deseado) pueden no sumar el 100 % debido a los correos electrónicos que sufren rebote blando y luego no se entregan después del período de reintento de hasta 72 horas.

Los rebotes blandos son correos electrónicos que rebotan debido a un problema temporal o transitorio, como "buzón de entrada lleno", "servidor temporalmente no disponible" y más. Si un correo electrónico con rebote blando aún no se entrega después de 72 horas, este correo electrónico no se contabilizará en las métricas de entrega de la Campaign.

### ¿Qué es un bucle de retroalimentación de correo electrónico? {#what-is-an-email-feedback-loop}

Un bucle de retroalimentación de correo electrónico (FBL) permite a los remitentes monitorizar su reputación identificando Campaigns que reciben un alto volumen de quejas. Para conocer los pasos para implementar un bucle de retroalimentación de Gmail, consulta el artículo [Bucle de retroalimentación de Google](https://support.google.com/a/answer/6254652).

### ¿Qué son los píxeles de seguimiento de apertura? {#what-are-open-tracking-pixels}

Los [píxeles de seguimiento de apertura]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#update-the-placement) aprovechan el dominio de seguimiento de clics de correo electrónico del remitente para rastrear eventos de apertura de correo electrónico. El píxel es una etiqueta de imagen adjunta al HTML del correo electrónico. Es más comúnmente el último elemento HTML dentro de la etiqueta body. Cuando un usuario carga su correo electrónico, se realiza una solicitud para completar la imagen desde el dominio de seguimiento con marca, lo que registra un evento de apertura.

### ¿Puedo rastrear aperturas de correos electrónicos renderizados en texto plano? {#can-i-track-opens-for-emails-rendered-in-plain-text}

No. Braze rastrea las aperturas de correo electrónico usando un [píxel de seguimiento de apertura]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#open-tracking-pixel) incrustado en el HTML del correo electrónico. Cuando el cliente de correo electrónico del destinatario carga el correo, solicita esta imagen y Braze registra un evento de apertura.

Debido a que los correos electrónicos de texto plano no pueden contener imágenes, el píxel de seguimiento de apertura no se incluye, por lo que las aperturas no se pueden rastrear para correos electrónicos renderizados en texto plano. Los clics aún se pueden rastrear, ya que los hipervínculos siguen siendo funcionales en texto plano.

Este es el comportamiento esperado. Para la precisión de la tasa de apertura, diseña los correos electrónicos como HTML y ten en cuenta que las aperturas no se contarán cuando los destinatarios vean la versión de texto plano.

### ¿Cómo funciona el seguimiento de correo electrónico cuando los destinatarios reenvían correos? {#how-does-email-tracking-work-when-recipients-forward-emails}

Cuando un destinatario reenvía un correo electrónico, el correo reenviado incluye el mismo píxel de seguimiento de apertura y los mismos enlaces de seguimiento de clics que el original. Esto significa:

- Si alguien que no estaba en tu audiencia original de la Campaign recibe un correo reenviado y lo abre, Braze registra un evento de apertura.
- Si hace clic en un enlace del correo reenviado, Braze registra un evento de clic.
- Estos eventos se atribuyen al perfil del destinatario original, no a la persona que recibió el correo reenviado, porque el píxel de seguimiento y los enlaces están vinculados al destinatario original.

Braze no puede distinguir entre aperturas y clics del destinatario original y los de personas que recibieron una copia reenviada. Este es el comportamiento estándar para los píxeles de seguimiento de correo electrónico y afecta a todos los proveedores de servicios de correo electrónico.

Al analizar las métricas de correo electrónico, ten en cuenta que la actividad de reenvío puede contribuir a los conteos de aperturas y clics. Si notas tasas de participación inusualmente altas o actividad repetida del mismo perfil a lo largo del tiempo, el reenvío puede ser un factor.

### ¿Se puede retirar una Campaign o Canvas de correo electrónico ya enviado? {#can-a-sent-email-campaign-or-canvas-be-recalled}

No. Una vez que Braze entrega una solicitud de envío a tu proveedor de servicios de correo electrónico (ESP), ese envío no se puede retirar. Después de que el mensaje está en el buzón de entrada del destinatario, tampoco se puede eliminar.

Para detener envíos adicionales, selecciona **Detener Campaign** o **Detener Canvas**. Los mensajes que ya fueron entregados al ESP aún pueden ser distribuidos. Para más detalles, consulta [¿Qué pasa cuando una Campaign o Canvas de correo electrónico se detiene?](#what-happens-when-an-email-campaign-or-canvas-is-stopped).

### ¿Qué pasa cuando una Campaign o Canvas de correo electrónico se detiene? {#what-happens-when-an-email-campaign-or-canvas-is-stopped}

Se impide que los usuarios entren al Canvas y no se envían más mensajes.

Para Campaigns de correo electrónico y Canvas, el botón de detener no detiene inmediatamente el envío. Cuando las solicitudes de envío se han enviado, no se puede evitar que se entreguen al usuario, lo que puede ocurrir después de cierta demora.

Aunque Braze no enviará más solicitudes una vez que la Campaign o Canvas se haya detenido, los análisis aún pueden aumentar mientras el ESP termina de procesar las solicitudes que ya están en tránsito.

### ¿Por qué veo más _clics totales_ que _aperturas totales_ en mis análisis de correo electrónico? {#why-am-i-seeing-more-_total-clicks_-than-_total-opens_-in-my-email-analytics}

_Aperturas totales_ es el conteo de cuántas veces el correo electrónico fue abierto por los usuarios, mientras que _Clics totales_ es el conteo de cuántas veces los usuarios hicieron clic dentro del correo electrónico entregado, incluyendo cualquier tipo de clics como clics en enlaces. Puede que veas más clics que aperturas por cualquiera de las siguientes razones:

- Los usuarios realizan múltiples clics en el cuerpo del correo electrónico dentro de una sola apertura.
- Los usuarios hacen clic en algunos enlaces del correo electrónico dentro del panel de vista previa de sus teléfonos. En este caso, Braze registra este correo electrónico como con clic pero no abierto.
- Los usuarios reabren un correo electrónico que previsualizaron anteriormente.

### ¿Por qué mis conteos de clics son más altos que mi Segment de usuarios que hicieron clic? {#why-are-my-click-counts-higher-than-my-segment-of-users-who-clicked}

Los análisis de Campaign muestran el número total de eventos de clic, mientras que los Segments devuelven el número de usuarios únicos que realizaron esos clics. Debido a que cada usuario puede hacer clic varias veces, el total de clics en los análisis suele ser más alto que el conteo de usuarios que hicieron clic cuando creas un Segment.

Por ejemplo, si 100 usuarios hacen clic en un enlace 3 veces cada uno, los análisis de la Campaign muestran 300 clics totales, pero un Segment filtrado por "Correo electrónico con clic" para esa Campaign devuelve 100 usuarios.

### ¿Por qué veo cero aperturas y clics en correos electrónicos? {#why-am-i-seeing-zero-email-opens-and-clicks}

Puede que no veas aperturas ni clics en correos electrónicos si hay una mala configuración en tu dominio de seguimiento. Esto puede deberse a cualquiera de las siguientes razones:
- Hay un problema de SSL donde las URL de seguimiento son `http` en lugar de `https`.
- Hay un problema con tu CDN donde la cadena de agente de usuario en los eventos de apertura, eventos de clic, o ambos, no se está completando.

### ¿Por qué veo un comportamiento inusual de apertura o clic de correo electrónico? {#why-am-i-seeing-unusual-email-open-or-click-behavior}

Si notas patrones inesperados en tus métricas de apertura o clic de correo electrónico, como un solo usuario que parece hacer clic en cada enlace inmediatamente, o aperturas que no se registran como se esperaba, revisa las siguientes causas comunes:

#### El recorte de correo electrónico elimina el píxel de seguimiento {#email-clipping-removes-the-tracking-pixel}

Cuando un correo electrónico es recortado por el proveedor de correo electrónico del destinatario (como Gmail recortando mensajes de más de aproximadamente 102 KB), el contenido en la parte inferior del correo puede ser truncado. Debido a que el píxel de seguimiento de apertura normalmente se inserta en la parte inferior del correo, el recorte puede impedir que funcione el seguimiento de apertura.

**Cómo identificarlo:** Verifica si el correo electrónico muestra un enlace de "Ver mensaje completo" o similar en la parte inferior. Puedes usar [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) para previsualizar el correo electrónico completo con desplazamiento y verificar si el mensaje está siendo recortado.

**Cómo resolverlo:** Puedes configurar Braze para colocar el píxel de seguimiento en la parte superior del correo electrónico en lugar de la parte inferior. Mover el píxel de seguimiento puede afectar cómo algunos clientes de correo electrónico renderizan tu HTML, así que prueba tus correos electrónicos en Inbox Vision después de realizar este cambio. Ten en cuenta que si el destinatario tiene las imágenes deshabilitadas, las aperturas no se pueden rastrear independientemente de la ubicación del píxel.

#### El píxel de seguimiento causa un espacio blanco en la parte superior del correo electrónico {#tracking-pixel-causes-white-gap-at-top-of-email}

Cuando el píxel de seguimiento de apertura se posiciona en la parte superior de un correo electrónico, puede aparecer una línea blanca o espacio visible en la parte superior del cuerpo del correo, particularmente en dispositivos móviles.

**Cómo identificarlo:** En Braze, ve a **Configuración** > **Preferencias de correo electrónico** y selecciona la sección **Píxel de seguimiento de apertura**. Si **Mover para SendGrid**, **Mover para SparkPost**, o **Mover para Amazon SES** está habilitado para tu proveedor de envío, el píxel está posicionado en la parte superior del HTML de tu correo electrónico. Si notas un espacio o línea blanca en la parte superior de tu correo electrónico renderizado, esta configuración puede ser la causa.

**Cómo resolverlo:** Desactiva el conmutador correspondiente de **Mover para SendGrid**, **Mover para SparkPost**, o **Mover para Amazon SES** en la sección **Píxel de seguimiento de apertura** para tu proveedor de envío. El píxel de seguimiento suele ser menos visible en la parte inferior de un correo electrónico. Prueba tus correos electrónicos en [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) después de cambiar la ubicación. Para más información, consulta [Actualizar la ubicación]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#update-the-placement).

#### Estadísticas retrasadas o clics sin aperturas {#delayed-stats-or-clicks-without-opens}

El seguimiento de apertura depende de que el destinatario cargue el correo electrónico con las imágenes habilitadas. En algunos casos, las estadísticas pueden parecer retrasadas o los clics pueden registrarse sin aperturas correspondientes debido a:

- El destinatario visualiza el correo electrónico en un panel de vista previa sin abrirlo completamente, y luego hace clic en los enlaces directamente desde la vista previa.
- El cliente de correo electrónico no carga las imágenes (y por lo tanto el píxel de seguimiento) hasta después de que el destinatario haya interactuado con los enlaces.

#### El software de seguridad simula clics en enlaces {#security-software-simulates-link-clicks}

Algunas herramientas de seguridad de correo electrónico corporativo (como Barracuda, Proofpoint y servicios similares) escanean los correos electrónicos entrantes haciendo clic automáticamente en todos los enlaces del mensaje para verificar que son seguros. Esto puede resultar en eventos de clic que aparecen en cuestión de segundos después del envío, a menudo con todos los enlaces del correo electrónico clicados en rápida sucesión.

Este comportamiento es más común con dominios de correo electrónico institucionales (como escuelas secundarias, universidades y entornos corporativos) y es más probable cuando tu dominio de envío difiere significativamente de tu dominio de seguimiento. Configurar un [dominio de seguimiento personalizado con marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences) puede reducir la frecuencia de estos clics automatizados.

**Cómo identificarlo:** Busca la dirección IP del evento de clic (disponible en los datos de Currents) en un motor de búsqueda. Si la IP está asociada con un proveedor de seguridad conocido (como Barracuda Networks), los clics probablemente son automatizados. También puedes ver un encabezado User-Agent consistente en múltiples clics automatizados.

Para contexto adicional sobre cómo el escaneo de seguridad afecta las métricas de correo electrónico, consulta [Gestión de aumentos en tasas de clics]({{site.baseurl}}/user_guide/channels/email/reporting).

### ¿Cuáles son los riesgos potenciales de provocar clics del servidor? {#what-are-the-potential-risks-of-triggering-server-clicks}

Ciertos elementos de un mensaje de correo electrónico, como mensajes excesivamente largos o demasiados signos de exclamación, pueden desencadenar respuestas de seguridad del correo electrónico. Estas respuestas pueden afectar los informes y la reputación de la IP y llevar a los usuarios a cancelar su suscripción.

Para las mejores prácticas sobre cómo gestionar estas respuestas, consulta [Gestión de aumentos en tasas de clics]({{site.baseurl}}/user_guide/channels/email/reporting).

### ¿Puede Braze rastrear los enlaces de cancelación de suscripción contabilizados en la métrica "Cancelaciones de suscripción"? {#can-braze-track-unsubscribe-links-counted-toward-the-unsubscribe-metric}

Braze rastrea los enlaces de cancelación de suscripción si se usa el siguiente Liquid en los correos electrónicos: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### ¿Por qué veo un número diferente de cancelaciones de suscripción que clics en mi enlace de cancelación de suscripción? {#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link}

Si hay más _Cancelaciones de suscripción_ que usuarios que hicieron clic en el enlace de cancelación de suscripción en el cuerpo del correo electrónico, [**List-unsubscribe**]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#list-unsubscribe) a menudo explica la diferencia. List-unsubscribe es una ruta de cancelación de suscripción adicional en el encabezado del correo electrónico (no el enlace en el cuerpo de tu mensaje). Cuando un usuario cancela su suscripción de esa manera, se contabiliza en _Cancelaciones de suscripción_ pero no se cuenta como un clic en la URL de cancelación de suscripción rastreada en el cuerpo.

Si el número total de clics en el enlace de cancelación de suscripción del cuerpo es mayor que el número de _Cancelaciones de suscripción_, los usuarios pueden haber hecho clic en el enlace más de una vez; por ejemplo, si cancelan su suscripción, se resuscriben y cancelan su suscripción de nuevo, los análisis del correo electrónico pueden registrar múltiples clics en el desglose de clics.

Si un usuario hace clic en el enlace de cancelación de suscripción dos veces (por ejemplo, si canceló su suscripción, se suscribió de nuevo y luego canceló su suscripción otra vez), esto cuenta dos veces en los análisis del correo electrónico.

### ¿Puedo agregar un enlace de "ver este correo electrónico en un navegador" a mis correos electrónicos? {#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails}

No. Braze no ofrece esta funcionalidad. Esto se debe a que una creciente mayoría del correo electrónico se abre en dispositivos móviles y en clientes de correo electrónico modernos, que renderizan imágenes y contenido sin problemas.

**Solución alternativa:** Para lograr este mismo resultado, puedes alojar el contenido de tu correo electrónico en una página de destino externa (como tu sitio web), que luego puede vincularse desde la Campaign de correo electrónico que estás construyendo usando la herramienta **Enlace** al editar el cuerpo del correo electrónico.

### ¿Braze convierte automáticamente las URL de texto plano o el texto con "www." en enlaces? {#does-braze-automatically-turn-plain-text-urls-or-www-text-into-links}

No. Braze no escanea tu mensaje ni convierte texto plano, como texto que comienza con `www.` o que parece una URL, en hipervínculos. Solo los enlaces que defines con etiquetas de ancla HTML (`<a href="...">`) se procesan a través del renderizado normal y las funciones de enlace en Braze.

Si un destinatario ve texto plano mostrado como un enlace clicable, ese comportamiento normalmente proviene de su cliente de correo electrónico (por ejemplo, Gmail, Outlook o Apple Mail). Muchos clientes detectan cadenas que parecen URL después de que el mensaje se entrega y las convierten en enlaces en el dispositivo del destinatario. Braze no controla ese comportamiento y no puede desactivarlo para el destinatario.

Para una apariencia, seguimiento y estilo de enlace predecibles, usa etiquetas `<a href>` explícitas en lugar de URL de texto plano.

### ¿Puedo controlar el atributo `target` en los enlaces de correo electrónico? {#can-i-control-the-target-attribute-on-email-links}

Aunque puedes establecer el atributo `target` (como `target="_blank"` o `target="_top"`) en los enlaces de tu HTML de correo electrónico, la mayoría de los clientes de correo electrónico ignoran o anulan este atributo. Por ejemplo, Gmail efectivamente fuerza un comportamiento similar a `_blank` independientemente de lo que especifiques.

Debido a que el comportamiento de los clientes de correo electrónico varía, no se debe confiar en el atributo `target` para controlar cómo se abren los enlaces. Para obtener detalles sobre qué clientes de correo electrónico soportan el atributo `target`, consulta [caniemail.com](https://www.caniemail.com/features/html-target/).

### ¿Por qué un signo más `+` en el enlace de mi correo electrónico se convierte en un espacio? {#why-does-a-plus-sign-in-my-email-link-turn-into-a-space}

Algunos analizadores de consultas tratan un signo más `+` no codificado como un espacio. Si tu URL de destino necesita un signo más en un parámetro de consulta, codifícalo como porcentaje usando `%2B` antes de agregar el enlace a tu correo electrónico.

### ¿Por qué mis usuarios están siendo desuscritos automáticamente por software de seguridad de correo electrónico? {#why-are-my-users-being-auto-unsubscribed-by-email-security-software}

Algunas herramientas de seguridad de correo electrónico corporativo (como Barracuda, Proofpoint y servicios similares) precargan o escanean todas las URL en los correos electrónicos entrantes, incluyendo los enlaces de cancelación de suscripción. Esto puede causar cancelaciones de suscripción no deseadas cuando la herramienta de seguridad sigue el enlace de cancelación de suscripción de un solo clic (list-unsubscribe).

Para mitigar esto:

- **Recomienda a los destinatarios agregar tu dominio de envío a la lista blanca:** Trabaja con los equipos de TI de los destinatarios afectados para agregar tu dominio de envío y los dominios de seguimiento de Braze a la lista de permitidos de seguridad de correo electrónico.
- **Usa un centro de preferencias:** En lugar de un enlace directo de cancelación de suscripción, usa un [centro de preferencias]({{site.baseurl}}/user_guide/channels/email/subscriptions) que requiera interacción del usuario para confirmar la acción de cancelación de suscripción. Los escáneres de seguridad normalmente no completan formularios de múltiples pasos.
- **Revisa los registros de cancelación de suscripción:** Verifica el encabezado `User-Agent` y la dirección IP en tus datos de eventos de cancelación de suscripción de Currents para identificar patrones consistentes con el escaneo automatizado (como encabezados `User-Agent` consistentes en múltiples cancelaciones de suscripción).

Para más detalles sobre cómo el escaneo del lado del servidor puede afectar las métricas de correo electrónico, consulta [Gestión de aumentos en tasas de clics]({{site.baseurl}}/user_guide/channels/email/reporting).

### ¿Por qué ha cambiado inesperadamente mi tasa de apertura por máquina? {#why-has-my-machine-open-rate-changed-unexpectedly}

Las [aperturas por máquina]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens) son desencadenadas por funciones de seguridad de correo electrónico como la protección de privacidad de correo de Apple (MPP), que precarga el contenido del correo electrónico (incluyendo el píxel de seguimiento) sin que el usuario abra físicamente el correo. Las tasas de apertura por máquina pueden fluctuar según:

- Cambios en la proporción de tu audiencia que usa Apple Mail u otros clientes de correo electrónico con privacidad habilitada.
- Actualizaciones en las funciones de privacidad del proveedor de correo electrónico o los comportamientos de detección de bots.
- Cambios en la segmentación o la orientación de tu audiencia.

Los porcentajes de apertura por máquina no son una medida confiable de la participación real. Para una vista más precisa del rendimiento del correo electrónico, concéntrate en *Otras aperturas* (aperturas no realizadas por máquina) y *Clics únicos*. También puedes comparar estas métricas a lo largo del tiempo usando el [panel de rendimiento de correo electrónico]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance).

### ¿Por qué mis vínculos profundos no funcionan en Gmail? {#why-are-my-deep-links-not-working-in-gmail}

Gmail elimina todos los enlaces que no son HTTP/HTTPS de los mensajes de correo electrónico. Si tu vínculo profundo usa un esquema personalizado (como `myapp://path/to/content`), Gmail lo eliminará y el enlace no funcionará para los destinatarios que lean el correo electrónico en Gmail. Esta es una limitación de Gmail, no de Braze.

Para solucionar esto:

- **Usa Universal Links (iOS) o App Links (Android).** Estos usan URL `https://` estándar que abren tu aplicación cuando está instalada y recurren a una página web en caso contrario. Consulta [Universal Links y App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links) para instrucciones de configuración.
- **Usa un proveedor de vinculación en profundidad.** Servicios como [Branch](https://www.branch.io/) generan vínculos profundos en formato HTTP que son compatibles con los clientes de correo electrónico, incluyendo Gmail.
- **Configura un endpoint de redirección.** Aloja un endpoint `https://` en tu servidor que redirija a la URL de esquema personalizado de tu aplicación. Los clientes de correo electrónico preservarán el enlace `https://` y la redirección se encarga de abrir la aplicación.

### ¿La métrica *Unique Opens* incluye *aperturas por máquina*? {#does-the-unique-opens-metric-include-machine-opens}

Sí. *Unique Opens* incluye *aperturas por máquina*. Puedes ver ambas métricas en la vista **Análisis de Campaign** y en el **generador de informes**.

Para conocer cómo esto afecta la atribución del **panel de conversiones**, consulta [¿Por qué los totales de apertura de correo electrónico no coinciden con los análisis de Campaign?]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#why-dont-email-open-totals-match-campaign-analytics) en [Solución de problemas]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#troubleshooting) en la página del panel de conversiones.

### ¿Por qué mi volumen de entrega de correo electrónico no coincide con mi volumen de envío? {#why-does-my-email-delivery-volume-not-match-my-send-volume}

Después de enviar un correo electrónico, el buzón de entrada del destinatario decide cuándo se entrega. Los mensajes pueden ser diferidos durante horas o días debido a un buzón de entrada lleno, limitación de velocidad del ESP desde una IP determinada y razones similares.

Cuando los mensajes diferidos se entregan en un día calendario diferente al día del envío, las _Entregas_ pueden superar los _Envíos_ para el mismo rango de fechas. Cuando muchos diferimientos se concentran en un solo día, los _Envíos_ pueden superar las _Entregas_ para ese rango.

### ¿Por qué veo una advertencia para incluir un enlace de cancelación de suscripción cuando mi correo electrónico ya tiene uno? {#why-am-i-seeing-a-warning-to-include-an-unsubscribe-link-when-my-email-already-has-one}

Esta advertencia puede persistir para Campaigns duplicadas desde una Campaign que no tenía un enlace de cancelación de suscripción. Para eliminarla:

- Para correos electrónicos HTML, ve a la pestaña **Texto plano** y selecciona **Regenerar desde HTML**.
- Después de duplicar, duplica la variante y luego elimina la variante original. **No** selecciones la variante original, o la advertencia puede persistir.

### ¿Por qué un usuario recibió un correo electrónico que no debería haber recibido? {#why-did-a-user-receive-an-email-they-shouldnt-have}

La entrega puede parecer incorrecta incluso cuando Braze se comportó según lo configurado. Revisa lo siguiente:

- **Perfiles duplicados** que comparten un buzón de entrada (consulta [¿Qué pasa cuando se envía un correo electrónico y varios perfiles tienen la misma dirección de correo electrónico?](#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address)).
- **Listas semilla, destinatarios de prueba o direcciones internas** incluidas en la audiencia o en un envío como CC/BCC.
- **Temporización del Segment o Canvas:** el usuario coincidió con la audiencia o el paso en Canvas cuando Braze evaluó la elegibilidad, y luego los atributos o el estado de suscripción cambiaron antes de que leyeran el mensaje.
- **Grupos de suscripción:** el usuario permaneció suscrito a un grupo al que se dirigió tu mensaje, incluso si su estado de suscripción global sugería lo contrario.
- **Importaciones de API o archivos** que actualizaron al usuario después de la segmentación pero antes de que esperaras que el cambio se aplicara.

Revisa el [registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), los registros de cambios de la Campaign o Canvas y la definición del Segment. Si aún no puedes reconciliar el envío, contacta a soporte de Braze con los identificadores del usuario, `dispatch_id` (si está disponible) y las marcas de tiempo.

### ¿Por qué un usuario no ha recibido mi mensaje de correo electrónico? {#why-hasnt-a-user-received-my-email-message}

Hay varias razones por las que un usuario no recibe un correo electrónico que esperabas que recibiera, incluyendo:

- No era elegible para recibir el correo electrónico.
- Su dirección de correo electrónico es inválida o no existe.
- Puede que haya perdido o eliminado el mensaje.
- El mensaje puede estar en su carpeta de correo no deseado.

{% alert tip %}
Un evento de entrega en Braze significa que el correo electrónico fue aceptado por el servidor del proveedor de buzón de entrada. Sin embargo, esto no garantiza que el mensaje aparezca en el buzón de entrada del usuario. El proveedor de buzón de entrada puede dirigir el mensaje a correo no deseado o, en casos raros, impedir silenciosamente la visualización del mensaje.
{% endalert %}

Usa las siguientes tablas para identificar la causa.

#### El correo electrónico no se envió {#the-email-wasnt-sent}

| Causa posible | Qué verificar |
|---|---|
| El usuario no era elegible para la Campaign o Canvas | Verifica la configuración de **Target Audiences** (para Campaigns) o **Target Audience** (para Canvas) en la [configuración]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) para confirmar que el usuario cumplió con todos los filtros de audiencia, criterios de Segment y reglas de entrega en el momento del envío. |
| El mensaje fue abortado | Verifica el [registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) para conocer las razones de aborto, como errores de Liquid o campos obligatorios faltantes. |
| La dirección de correo electrónico del usuario era inválida o estaba ausente | En **Búsqueda de usuarios**, verifica el perfil del usuario para confirmar que una dirección de correo electrónico válida estaba registrada en el momento del envío. |
| La dirección de correo electrónico del usuario previamente tuvo un rebote duro | Un rebote duro marca la dirección de correo electrónico como inválida y previene futuros envíos a esa dirección. De manera similar, si un destinatario marca tu correo electrónico como correo no deseado, Braze solo envía correos transaccionales a ese usuario, no Campaigns estándar. Verifica la pestaña **Participación** del usuario en su perfil. Para más información, consulta [Direcciones de correo electrónico desuscritas]({{site.baseurl}}/user_guide/channels/email/subscriptions#unsubscribed-email-addresses) y [Rebotes y correos electrónicos inválidos]({{site.baseurl}}/user_guide/channels/email/subscriptions#bounces-and-invalid-emails). |
| El usuario está desuscrito del correo electrónico | Verifica el estado de suscripción del usuario en **Configuración de contacto** en la pestaña **Participación**. Braze no envía correos electrónicos a usuarios que están desuscritos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Causa de que el correo electrónico no se envió" }

#### El correo electrónico se envió, pero no llegó a su buzón de entrada {#the-email-was-sent-but-didnt-arrive-in-their-inbox}

| Causa posible | Qué verificar |
|---|---|
| El proveedor de buzón de entrada (MBP) no estaba accesible | Un problema temporal impidió que el correo electrónico llegara al MBP del destinatario. Esto normalmente se resuelve solo con reintentos. Los proveedores de servicios de correo electrónico reintentan los rebotes blandos durante hasta 72 horas. |
| El MBP rechazó el correo electrónico | El servidor de correo del destinatario rechazó el correo electrónico. Revisa el [registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) para conocer los detalles del rebote. |
| El MBP descartó silenciosamente el correo electrónico | El MBP aceptó el correo electrónico pero no lo mostró al usuario y no devolvió un rebote. Esto está fuera del control de Braze y no se puede detectar en los registros de Braze. |
| El correo electrónico fue a la carpeta de correo no deseado | El MBP identificó el mensaje como correo no deseado y lo dirigió a la carpeta de correo no deseado del usuario. Pide al usuario que revise su carpeta de correo no deseado. |
| El destinatario tiene filtrado de correo personalizado | El usuario o su administrador de TI pueden haber configurado reglas de buzón de entrada que filtran, redirigen o eliminan los mensajes entrantes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Causa de que el correo electrónico no llegó al buzón de entrada" }

### ¿Cómo puedo eliminar una dirección de correo electrónico de la lista de rebotes? {#how-can-i-remove-an-email-address-from-the-bounce-list}

Si una dirección de correo electrónico válida aparece como inválida en Braze (normalmente después de un rebote duro de tu proveedor de servicios de correo electrónico), usa el endpoint [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces). Esto elimina la dirección de tu lista de rebotes de Braze y de la lista de rebotes mantenida por tu proveedor de correo electrónico. Braze entonces reanuda los envíos a esa dirección.

Si la dirección fue marcada como correo no deseado en lugar de rebote duro, usa el endpoint [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam) en su lugar.

Para más información, consulta [Rebotes y correos electrónicos inválidos]({{site.baseurl}}/user_guide/channels/email/subscriptions#bounces-and-invalid-emails) y [Eliminar una dirección de correo electrónico de tu lista de rebotes o correo no deseado]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps#remove-an-email-address-from-your-bounce-or-spam-list).

### ¿Cómo soluciono los problemas de capacidad de entrega de correo electrónico? {#how-do-i-troubleshoot-email-deliverability-issues}

Si tus correos electrónicos se retrasan, se difieren o rebotan, revisa el [registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) para conocer los detalles de rebotes y diferimientos, y luego identifica dónde ocurre el problema en la cadena de entrega. Los problemas comunes de capacidad de entrega se dividen en cuatro categorías:

#### Lectura de respuestas de límite de velocidad del ESP {#reading-esp-rate-limit-responses}

Tu proveedor de servicios de correo electrónico (ESP), como Amazon SES, SparkPost o SendGrid, devuelve códigos de respuesta SMTP al aceptar o diferir mensajes. Las respuestas de límite de velocidad normalmente usan códigos 4xx, que indican fallos temporales:

- **421:** Servicio temporalmente no disponible, a menudo debido a alto volumen, límites de conexión o restricciones de recursos del servidor. El mensaje permanece en cola y tu ESP reintenta la entrega automáticamente.
- **429:** Límite de velocidad de API excedido. Has enviado demasiadas solicitudes dentro de la ventana de tiempo permitida.
- **450 / 451:** Diferimiento temporal debido a volumen o conexiones. El servidor del destinatario te pide que reduzcas la velocidad.

Cuando veas estos códigos en el [registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) o en el panel de tu ESP, reduce el volumen de envío al dominio afectado y usa intervalos de reintento progresivamente más largos. Continuar a volumen completo mientras tienes límite de velocidad puede escalar diferimientos temporales a rechazos permanentes.

#### Límites de velocidad del proveedor de buzón de entrada {#mailbox-provider-rate-limits}

Los proveedores de buzón de entrada aplican sus propios límites de velocidad al correo entrante, separados de los controles de envío de Braze. Estos límites pueden ser estrictos y están fuera de tu control directo:

- Virgin Media / NTL (UK): Usa limitación de velocidad por hora que activa errores `421 4.1.1 MXIN503 Hourly ratelimit for your IP exceeded`. Estos límites pueden afectar incluso a remitentes de bajo volumen. Se aplican a nivel de IP en todos los remitentes que comparten esa IP.
- Gmail, Yahoo, iCloud, Microsoft: Cada proveedor tiene umbrales de limitación propietarios basados en tu reputación de remitente, volumen y patrones de participación.

Si encuentras limitación de velocidad específica del proveedor, considera agrupar tus envíos durante un período de tiempo más largo o segmentar por proveedor de buzón de entrada para distribuir el volumen de manera más gradual. Verifica tu lista de destinatarios para detectar concentración en un proveedor; si la mayoría de los destinatarios usan un dominio, escalona la entrega.

#### Retrasos en correo electrónico corporativo por escaneo de antivirus {#corporate-email-delays-from-antivirus-scanning}

Las direcciones de correo electrónico empresariales a menudo pasan por puertas de seguridad corporativas que escanean los mensajes antes de la entrega. Esto puede retrasar los correos electrónicos de 15 a 20 minutos o más, especialmente para mensajes con:

- Archivos adjuntos grandes
- Enlaces a dominios desconocidos
- Contenido que se asemeja a patrones de phishing

Estos retrasos ocurren porque los sistemas de seguridad ponen en cola los mensajes para análisis de comportamiento en entornos aislados de sandbox. Si un gran volumen de correo llega simultáneamente, los mensajes se ponen en cola para análisis y el retraso se extiende aún más. Este es un comportamiento normal de la seguridad de correo electrónico empresarial y no es algo que puedas eludir. Al enviar mensajes urgentes a destinatarios corporativos, ten en cuenta esta ventana de procesamiento en tu cronograma de comunicación.

#### Solución de errores de límite de velocidad 421 4.7.28 de Google {#troubleshooting-google-421-4728-rate-limit-errors}

Gmail devuelve un error `421-4.7.28` cuando detecta una tasa inusual de correo electrónico no solicitado desde tu dirección IP, rango de IP de envío, dominio SPF, dominio DKIM o dominio de URL. Este es un limitador temporal, no un bloqueo permanente, pero señala que tu volumen de envío, velocidad o reputación no cumple con las expectativas actuales de Gmail.

Si recibes este error:

1. Pausa los envíos no esenciales inmediatamente durante 24 a 48 horas. Continuar enviando mientras tienes limitación escala el problema y puede llevar a rechazos permanentes 550.
2. Confirma que SPF, DKIM y DMARC estén correctamente configurados y que tu encabezado From: se alinee con tu autenticación.
3. Verifica [Google Postmaster Tools](https://postmaster.google.com/) y el [Centro de capacidad de entrega]({{site.baseurl}}/user_guide/analytics/dashboards/deliverability_center) de Braze (después de conectar Google Postmaster) para el estado de cumplimiento de tu dominio y las tasas de quejas de correo no deseado. Tu tasa de correo no deseado reportada por usuarios debe mantenerse por debajo del 0.1 % (el techo máximo es del 0.3 %).
4. Después de la pausa, reanuda el envío al 10 a 20 % del volumen anterior solo a tus destinatarios más participativos. Aumenta el volumen lentamente durante varias semanas solo si no ocurren más errores 4xx.

Para orientación adicional, consulta las [Directrices para remitentes de correo masivo de Google](https://support.google.com/mail/answer/81126).

### ¿Cómo puedo optimizar las imágenes en Outlook? {#how-can-i-optimize-images-in-outlook}

Outlook a menudo usa el renderizado de Microsoft Word en lugar del renderizado estándar del navegador, lo que puede causar que las imágenes se rendericen incorrectamente o agregar bordes alrededor de las imágenes. Este mismo renderizado específico del cliente también afecta [cómo se muestra el texto alternativo]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text) en diferentes clientes de correo electrónico.

Si las imágenes se muestran más grandes que su ancho esperado en Outlook, agrega el siguiente CSS a la imagen:

```css
max-width: 100%;
```

Por ejemplo:

```html
<img src="your-image.png" style="max-width: 100%;" alt="Description">
```

También puedes envolver contenido para que se oculte en Outlook de escritorio usando comentarios condicionales:

```html
<!--[if !mso]><!-- -->
<span>Content hidden in Outlook desktop</span>
<!--<![endif]-->
```

### ¿Puedo usar imágenes SVG o WebP en mis mensajes de correo electrónico? {#can-i-use-svg-or-webp-images-in-my-email-messages}

Las imágenes SVG no se recomiendan para correo electrónico debido al soporte limitado en los clientes de correo electrónico. Gmail y varios otros proveedores de correo electrónico importantes no renderizan imágenes SVG, lo que puede resultar en imágenes rotas o faltantes para los destinatarios. WebP no tiene soporte consistente en todos los clientes.

En su lugar, usa formatos ampliamente soportados como PNG o JPEG para que las imágenes se rendericen de manera confiable.

### ¿Puedo incrustar videos en correos electrónicos? {#can-i-embed-videos-in-emails}

Los videos incrustados no son soportados nativamente por muchos clientes de correo electrónico populares como Gmail, Outlook y Yahoo. Como resultado, los elementos de video incrustados pueden no mostrarse como se pretende o pueden no aparecer en absoluto. Además, incrustar video directamente en un correo electrónico puede aumentar significativamente el tamaño del correo electrónico, lo que aumenta la probabilidad de que el mensaje sea marcado como correo no deseado.

En su lugar, puedes crear un GIF o imagen estática que se asemeje a un video en un reproductor de video, y luego vincular esa imagen a tu video. Cuando los usuarios hacen clic en la imagen, son dirigidos al video alojado en tu sitio web o una plataforma de video. Braze también admite la integración con [Playable]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/playable), que proporciona contenido de video optimizado que se reproduce automáticamente en los clientes de correo electrónico compatibles.

### ¿Se pueden usar variables de Liquid asignadas en una parte del creador de mensajes en otra? {#can-liquid-variables-assigned-in-one-part-of-the-message-composer-be-used-in-another}

No. Cada parte del correo electrónico (asunto, cuerpo, encabezados, botones, etc.) se genera por separado, por lo que las variables de Liquid asignadas en un campo no están disponibles en otro. Asigna las variables en cada campo que las necesite.

### Mi plantilla de correo electrónico no aparece. ¿Dónde está? {#my-email-template-is-missing-where-is-it}

Primero, confirma que tienes los [permisos de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para ver plantillas. Para ver las plantillas de correo electrónico guardadas, ve a **Contenido** > **Correo electrónico**. Puedes filtrar las plantillas por estado y tipo (HTML o arrastrar y soltar).

### ¿Necesito registrar dominios para correos electrónicos de relay o enmascarados? {#do-i-need-to-register-domains-for-relay-or-masked-emails}

[Private Email Relay de Apple]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/email_private_relay_apple_SSO) requiere que registres tus dominios de envío en el Apple Developer Portal para prevenir rebotes. Google Shielded Email no requiere un proceso manual de registro de dominio o inclusión en lista de permitidos.

### ¿Puedo agregar hipervínculos en las líneas del asunto o preencabezados del correo electrónico? {#can-i-add-hyperlinks-in-email-subject-lines-or-preheaders}

No. Agregar hipervínculos en las líneas del asunto del correo electrónico no es soportado por los proveedores de buzón de entrada. Aunque algunos proveedores de buzón de entrada escanean automáticamente las líneas del asunto y convierten direcciones físicas, fechas u horas en enlaces clicables, esto sucede automáticamente en el dispositivo del destinatario y está fuera del control de Braze (o de cualquier ESP).

De manera similar, agregar hipervínculos dentro del preencabezado no es soportado en toda la industria del correo electrónico.

Si necesitas funcionalidad similar a contenido clicable en la línea del asunto o el área del preencabezado, considera usar [Gmail Promotions]({{site.baseurl}}/user_guide/channels/email/html_editor/gmail_promotions_tab) para agregar anotaciones interactivas a tus correos electrónicos para usuarios de Gmail.

### ¿Qué significa la razón de rebote `unable to get mx info` o `failed to get IPs from PTR record`? {#what-does-the-bounce-reason-unable-to-get-mx-info-or-failed-to-get-ips-from-ptr-record-mean}

En el [registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), una razón de rebote similar a la siguiente indica un problema al resolver la configuración de correo del dominio receptor (el dominio después del `@` en la dirección), no en la composición del mensaje de Braze:

Las causas típicas incluyen:

- **Registros MX** faltantes, incorrectos o inalcanzables para ese dominio
- Nombres de host de correo entrante que no se resuelven o que fallan en las verificaciones de **PTR (DNS inverso)** esperadas por la infraestructura receptora
- Dominios inválidos o mal escritos en la dirección de correo electrónico

**Próximos pasos:**

- Confirma la ortografía de la dirección y el dominio.
- Si la dirección es correcta, contacta al propietario del buzón de entrada o al equipo de TI de ese dominio.
- Pídeles que auditen los registros MX y los registros DNS relacionados, incluyendo los registros PTR para sus servidores de correo, con su proveedor de DNS.

Otros destinatarios generalmente no se ven afectados. Para conocer cómo los rebotes blandos aparecen en los informes, consulta [Rebote blando]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#soft-bounce).

### ¿Por qué recibo una alerta de correo no deseado al enviarme un correo electrónico desde Braze a mí mismo? {#why-do-i-get-a-spam-alert-when-sending-an-email-from-braze-to-myself}

Si envías un correo electrónico de prueba desde Braze a tu propia dirección de correo electrónico y ves una advertencia de correo no deseado o alerta de phishing, como "el dominio de envío es similar al dominio de tu empresa, pero no lo reconocemos", esto es una función de seguridad antiphishing común, no un error en tu configuración de Braze.

Esta alerta normalmente aparece cuando el dominio de envío del correo electrónico coincide con el dominio del destinatario (por ejemplo, ambos son `@tuempresa.com`). Los sistemas de seguridad de correo electrónico marcan esto porque los estafadores a menudo falsifican dominios que se parecen al dominio de la empresa del destinatario.

Para verificar que tu correo electrónico está configurado correctamente:

1. Visualiza el mensaje original (encabezados sin procesar del correo electrónico) en tu cliente de correo electrónico.
2. Verifica que la autenticación SPF, DKIM y DMARC pasen correctamente.
3. Si los tres pasan, tu envío de correo electrónico desde Braze está configurado correctamente.

Para evitar que aparezca esta alerta:

Pide a tu equipo de TI que agregue tu dominio de envío de Braze y las direcciones IP a la lista de permitidos en los servicios de seguridad de correo electrónico o la puerta de enlace de correo de tu empresa. Esto le dice a tu sistema de seguridad que confíe en los correos electrónicos de tu infraestructura de envío de Braze.