---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre correo electrónico
page_order: 30
description: "Esta página ofrece respuestas a preguntas frecuentes sobre la mensajería por correo electrónico."
channel: email

---

# Preguntas frecuentes

> Este artículo ofrece respuestas a algunas preguntas frecuentes sobre los correos electrónicos.

### ¿Qué ocurre cuando se envía un correo electrónico y varios perfiles tienen la misma dirección de correo electrónico?

Si varios usuarios con direcciones de correo electrónico coincidentes están en un segmento que va a recibir una campaña, se selecciona un perfil de usuario aleatorio con esa dirección de correo electrónico en el momento del envío. De esta forma, el correo electrónico se envía solo una vez y se deduplica, lo que garantiza que no llegue a la misma dirección de correo electrónico varias veces.

Si varios perfiles comparten una dirección de correo electrónico y uno de ellos cancela la suscripción, Braze actualiza otros perfiles (hasta 100) con esa dirección al mismo estado de suscripción. Esto se aplica a las cancelaciones de suscripción y a otros cambios, como el estado de suscripción global y los estados individuales de los grupos de suscripción.

Los siguientes escenarios pueden hacer que parezca que un usuario recibió un correo electrónico dos veces:

- **Se produjo un error durante la creación de la campaña o el Canvas:** Es posible que el usuario no reciba literalmente el mismo envío dos veces, pero puede recibir dos correos electrónicos separados con la misma línea del asunto. Cuando se duplica una campaña o un Canvas, verifica los detalles de configuración del correo electrónico, como las imágenes o las líneas del asunto. También puedes consultar los registros de cambios para ver si la campaña o el Canvas se modificó después del lanzamiento; un duplicado puede compartir la misma línea del asunto que el original cuando el usuario lo recibió.
- **Varios perfiles de usuario tienen reenvío de correo electrónico:** Si un usuario tiene varias cuentas en una aplicación determinada pero una cuenta reenvía el correo, el usuario recibe la campaña una vez por buzón de entrada; el correo puede aparecer dos veces en el buzón de entrada donde se reenvían los mensajes. Solo algunos proveedores indican cuándo un correo electrónico fue reenviado desde otra cuenta.
- **Configuración del correo electrónico en el destinatario:** Algunos clientes fusionan buzones de entrada ("buzón de entrada universal"). Si la misma campaña se dirige a varias cuentas que comparten un buzón de entrada, puede parecer que una persona recibió la campaña dos veces cuando en realidad se enviaron mensajes a dos perfiles distintos. El destinatario puede confirmar si varias cuentas están combinadas en un solo buzón de entrada.

Ten en cuenta que esta deduplicación ocurre cuando los usuarios objetivo están incluidos en el mismo envío. Las campañas desencadenadas (excluyendo las campañas desencadenadas por API) y los Canvas pueden resultar en múltiples envíos a la misma dirección de correo electrónico (incluso dentro de un período en el que los usuarios podrían ser excluidos debido a la reelegibilidad) si diferentes usuarios con direcciones de correo electrónico coincidentes registran el evento desencadenante en momentos diferentes. Por ejemplo, si el usuario A y el usuario B comparten el correo electrónico `johndoe@example.com` pero sus perfiles están en zonas horarias diferentes, cuando el evento desencadenante de la campaña incluye el envío en la zona horaria del usuario, el correo electrónico `johndoe@example.com` recibe dos correos electrónicos.

Los usuarios no se deduplican por correo electrónico en la entrada al Canvas, por lo que es posible que no se dedupliquen más allá del primer paso de un Canvas si avanzan en momentos ligeramente diferentes debido a la entrada con límite de velocidad. Cuando un usuario asociado a una dirección de correo electrónico determinada abre o hace clic en un correo electrónico, todos los perfiles de usuario que comparten esa dirección de correo electrónico se marcan como que abrieron o hicieron clic en la campaña.

#### Excepción: campañas desencadenadas por API

Las campañas desencadenadas por API deduplicarán o enviarán duplicados dependiendo de dónde se defina la audiencia. Los correos electrónicos duplicados deben dirigirse por separado en la llamada a la API utilizando `user_ids` distintos para recibir múltiples detalles. Estos son tres posibles escenarios para las campañas desencadenadas por API:

- **Escenario 1: Correos electrónicos duplicados en el segmento objetivo:** Si el mismo correo electrónico aparece en varios perfiles de usuario que están agrupados en los filtros de audiencia del dashboard para una campaña desencadenada por API, solo uno de los perfiles recibe el correo electrónico.
- **Escenario 2: Correos electrónicos duplicados en diferentes `user_ids` dentro del objeto de destinatarios:** Si el mismo correo electrónico aparece dentro de múltiples valores de `external_user_id` referenciados por el objeto `recipients`, el correo electrónico se envía dos veces.
- **Escenario 3: Correos electrónicos duplicados debido a `user_ids` duplicados dentro del objeto de destinatarios:** Si intentas añadir el mismo perfil de usuario dos veces, solo uno de los perfiles recibe el correo electrónico.

{% alert important %}
Si envías una campaña de API a través de una llamada a la API (excluyendo las campañas desencadenadas por API), y se especifican múltiples usuarios en la audiencia del segmento con la misma dirección de correo electrónico, se envía a esa dirección tantas veces como aparezca en la llamada. Esto se debe a que se asume que las llamadas a la API están construidas intencionalmente.
{% endalert %}

### ¿Qué ocurre con el estado de suscripción cuando la dirección de correo electrónico de un usuario cambia a una compartida por otro usuario?

Si estableces o actualizas la dirección de correo electrónico del usuario A a otra dirección de correo electrónico que comparte un usuario B existente, el usuario A hereda el estado de suscripción que ya existe del usuario B, a menos que la configuración **Resuscribir usuarios cuando actualicen su correo electrónico** esté activada.

### ¿Las actualizaciones de mi configuración de correo electrónico saliente se aplican retroactivamente?

No. Las actualizaciones realizadas en la configuración de correo electrónico saliente no afectan retroactivamente a los envíos existentes. Por ejemplo, cambiar el nombre de visualización predeterminado en la configuración del correo electrónico no reemplazará automáticamente el nombre de visualización predeterminado existente en tus campañas o Canvas activos.

### ¿Qué es una "buena" tasa de entrega de correo electrónico?

Normalmente, el "número mágico" es alrededor del 98 % de mensajes entregados con una tasa de rebote no superior al 3 %. Si tu entrega cae por debajo de eso, generalmente hay motivo de preocupación.

Sin embargo, una tasa superior al 98 % aún puede tener problemas de capacidad de entrega. Por ejemplo, si todos tus rebotes provienen de un solo dominio, eso es una señal clara de un problema de reputación con ese proveedor.

Además, los mensajes pueden estar siendo entregados y terminando en correo no deseado, lo que indica problemas de reputación potencialmente graves. Es importante monitorear no solo la cantidad de mensajes que se entregan, sino también las tasas de apertura y clics para determinar si los usuarios realmente están viendo los mensajes en sus buzones de entrada. Dado que los proveedores generalmente no informan de cada instancia de correo no deseado, una tasa de correo no deseado de incluso el 1 % podría ser motivo de preocupación y análisis adicional.

Finalmente, tu negocio y los tipos de correos electrónicos que envías también pueden afectar la entrega. Por ejemplo, alguien que envía principalmente [correos electrónicos transaccionales]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/) debería esperar ver una mejor tasa que alguien que envía muchos mensajes de marketing.

### ¿Por qué mis métricas de entrega de correo electrónico no suman el 100 %?

Las métricas de entrega de correo electrónico (entregas, rebotes y tasa de correo no deseado) pueden no sumar el 100 % debido a los correos electrónicos que tuvieron un rebote blando y luego no se entregaron después del período de reintento de hasta 72 horas.

Los rebotes blandos son correos electrónicos que rebotan debido a un problema temporal o transitorio, como "buzón de entrada lleno", "servidor temporalmente no disponible" y más. Si un correo electrónico con rebote blando aún no se entrega después de 72 horas, este correo electrónico no se contabilizará en las métricas de entrega de la campaña.

### ¿Qué es un bucle de retroalimentación de correo electrónico?

Un bucle de retroalimentación de correo electrónico (FBL) permite a los remitentes monitorear su reputación identificando campañas que reciben un alto volumen de quejas. Para conocer los pasos para implementar un bucle de retroalimentación de Gmail, consulta el artículo [Bucle de retroalimentación de Google](https://support.google.com/a/answer/6254652).

### ¿Qué son los píxeles de seguimiento de apertura?

Los [píxeles de seguimiento de apertura]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/#changing-location-of-tracking-pixel) utilizan el dominio de seguimiento de clics del remitente para rastrear los eventos de apertura de correo electrónico. El píxel es una etiqueta de imagen que se añade al HTML del correo electrónico. Generalmente es el último elemento HTML dentro de la etiqueta body. Cuando un usuario carga su correo electrónico, se realiza una solicitud para cargar la imagen desde el dominio de seguimiento de marca, lo que registra un evento de apertura.

### ¿Qué ocurre cuando se detiene una campaña de correo electrónico o un Canvas?

Se impide que los usuarios entren al Canvas y no se envían más mensajes.

Para las campañas de correo electrónico y los Canvas, el botón de detener no detiene inmediatamente el envío. Cuando las solicitudes de envío ya se han enviado, no se pueden detener para que no se entreguen al usuario, lo que puede ocurrir después de cierto retraso.

Aunque Braze no enviará más solicitudes una vez que la campaña o el Canvas se haya detenido, los análisis aún pueden aumentar mientras el ESP termina de procesar las solicitudes que ya están en curso.

### ¿Por qué veo más *Clics totales* que *Aperturas totales* en mis análisis de correo electrónico?

*Aperturas totales* es el recuento de cuántas veces los usuarios abrieron el correo electrónico, mientras que *Clics totales* es el recuento de cuántas veces los usuarios hicieron clic dentro del correo electrónico entregado, incluyendo cualquier tipo de clics como clics en enlaces. Puedes estar viendo más clics que aperturas por cualquiera de las siguientes razones:

- Los usuarios realizan múltiples clics en el cuerpo del correo electrónico dentro de una sola apertura.
- Los usuarios hacen clic en algunos enlaces del correo electrónico dentro del panel de vista previa de sus teléfonos. En este caso, Braze registra este correo electrónico como clicado pero no abierto.
- Los usuarios vuelven a abrir un correo electrónico que previsualizaron anteriormente.

### ¿Por qué veo cero aperturas y clics en correos electrónicos?

Puedes no ver aperturas ni clics en correos electrónicos si hay una configuración incorrecta en tu dominio de seguimiento. Esto puede deberse a cualquiera de las siguientes razones:
- Hay un problema de SSL donde las URL de seguimiento son `http` en lugar de `https`.
- Hay un problema con tu CDN donde la cadena de agente de usuario en los eventos de apertura, los eventos de clic o ambos no se están completando.

### ¿Cuáles son los riesgos potenciales de desencadenar clics del servidor?

Ciertos elementos de un mensaje de correo electrónico, como mensajes excesivamente largos o demasiados signos de exclamación, pueden desencadenar respuestas de seguridad del correo electrónico. Estas respuestas pueden afectar los informes y la reputación de la IP y llevar a los usuarios a cancelar su suscripción.

Para conocer las mejores prácticas sobre cómo manejar estas respuestas, consulta [Gestión de aumentos en las tasas de clics]({{site.baseurl}}/user_guide/channels/email/reporting/).

### ¿Puede Braze rastrear los enlaces de cancelación de suscripción contabilizados en la métrica "Cancelaciones de suscripción"?

Braze rastrea los enlaces de cancelación de suscripción si se utiliza el siguiente Liquid dentro de los correos electrónicos: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### ¿Por qué veo un número diferente de cancelaciones de suscripción que de clics en mi enlace de cancelación de suscripción?

Si hay más *Cancelaciones de suscripción* que usuarios que hicieron clic en el enlace de cancelación de suscripción en el cuerpo del correo electrónico, las acciones del encabezado list-unsubscribe a menudo explican la diferencia: un clic en el encabezado list-unsubscribe cuenta como una *Cancelación de suscripción* pero no como un *Clic* en el enlace del cuerpo.

Si el número total de clics en el enlace de cancelación de suscripción del cuerpo es mayor que el número de *Cancelaciones de suscripción*, es posible que los usuarios hayan hecho clic en el enlace más de una vez.

### ¿Puedo añadir un enlace de "ver este correo electrónico en un navegador" a mis correos electrónicos?

No. Braze no ofrece esta funcionalidad. Esto se debe a que la gran mayoría de los correos electrónicos se abren en dispositivos móviles y en clientes de correo electrónico modernos, que renderizan imágenes y contenido sin problemas.

**Solución alternativa:** Para lograr este mismo resultado, puedes alojar el contenido de tu correo electrónico en una página de inicio externa (como tu sitio web), que luego se puede enlazar desde la campaña de correo electrónico que estás creando usando la herramienta **Enlace** al editar el cuerpo del correo electrónico.

### ¿Braze convierte automáticamente las URL en texto plano o el texto "www." en enlaces?

No. Braze no escanea tu mensaje ni convierte texto plano, como texto que comienza con `www.` o que parece una URL, en hipervínculos. Solo los enlaces que defines con etiquetas de anclaje HTML (`<a href="...">`) se procesan a través del renderizado normal y las funciones de enlaces en Braze.

Si un destinatario ve texto plano mostrado como un enlace clicable, ese comportamiento generalmente proviene de su cliente de correo electrónico (por ejemplo, Gmail, Outlook o Apple Mail). Muchos clientes detectan cadenas similares a URL después de que el mensaje se entrega y las convierten en enlaces en el dispositivo del destinatario. Braze no controla ese comportamiento y no puede desactivarlo para el destinatario.

Para una apariencia, seguimiento y estilo de enlaces predecibles, usa etiquetas `<a href>` explícitas en lugar de URL en texto plano.

### ¿Por qué el software de seguridad de correo electrónico está cancelando automáticamente la suscripción de mis usuarios?

Algunas herramientas de seguridad de correo electrónico corporativo (como Barracuda, Proofpoint y servicios similares) precargan o escanean todas las URL en los correos electrónicos entrantes, incluidos los enlaces de cancelación de suscripción. Esto puede causar cancelaciones de suscripción no deseadas cuando la herramienta de seguridad sigue el enlace de cancelación de suscripción con un solo clic (list-unsubscribe).

Para mitigar esto:

- **Recomienda a los destinatarios que añadan tu dominio de envío a la lista de permitidos:** Trabaja con los equipos de TI de los destinatarios afectados para añadir tu dominio de envío y los dominios de seguimiento de Braze a su lista de permitidos de seguridad de correo electrónico.
- **Usa un centro de preferencias:** En lugar de un enlace directo de cancelación de suscripción, usa un [centro de preferencias]({{site.baseurl}}/user_guide/channels/email/subscriptions/) que requiera la interacción del usuario para confirmar la acción de cancelación de suscripción. Los escáneres de seguridad normalmente no completan formularios de varios pasos.
- **Revisa los registros de cancelación de suscripción:** Verifica el encabezado `User-Agent` y la dirección IP en los datos de eventos de cancelación de suscripción de Currents para identificar patrones consistentes con el escaneo automatizado (como encabezados `User-Agent` consistentes en múltiples cancelaciones de suscripción).

Para más detalles sobre cómo el escaneo del lado del servidor puede afectar las métricas de correo electrónico, consulta [Gestión de aumentos en las tasas de clics]({{site.baseurl}}/user_guide/channels/email/reporting/#handling-increases-in-click-rates).

### ¿Por qué mi tasa de aperturas por máquina ha cambiado inesperadamente?

Las [aperturas por máquina]({{site.baseurl}}/user_guide/analytics/metrics_glossary/#machine-opens) se desencadenan por funciones de seguridad de correo electrónico como la protección de la privacidad en los correos electrónicos de Apple Mail (MPP), que precarga el contenido del correo electrónico (incluido el píxel de seguimiento) sin que el usuario abra físicamente el correo electrónico. Las tasas de aperturas por máquina pueden fluctuar según:

- Cambios en la proporción de tu audiencia que usa Apple Mail u otros clientes de correo electrónico con funciones de privacidad habilitadas.
- Actualizaciones en las funciones de privacidad del proveedor de correo electrónico o en los comportamientos de detección de bots.
- Cambios en la segmentación o el direccionamiento de tu audiencia.

Los porcentajes de aperturas por máquina no son una medida fiable de la interacción real. Para una visión más precisa del rendimiento del correo electrónico, concéntrate en *Otras aperturas* (aperturas no realizadas por máquina) y *Clics únicos*. También puedes comparar estas métricas a lo largo del tiempo usando el [Panel de rendimiento del correo electrónico]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance/).

### ¿Por qué mis vínculos profundos no funcionan en Gmail?

Gmail elimina todos los enlaces que no son HTTP/HTTPS de los mensajes de correo electrónico. Si tu vínculo profundo usa un esquema personalizado (como `myapp://path/to/content`), Gmail lo eliminará y el enlace no funcionará para los destinatarios que lean el correo electrónico en Gmail. Esta es una limitación de Gmail, no de Braze.

Para solucionar esto:

- **Usa Universal Links (iOS) o App Links (Android).** Estos usan URL estándar `https://` que abren tu aplicación cuando está instalada y recurren a una página web en caso contrario. Consulta [Universal Links y App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/) para obtener instrucciones de configuración.
- **Usa un proveedor de vinculación en profundidad.** Servicios como [Branch](https://www.branch.io/) generan vínculos profundos con formato HTTP que son compatibles con clientes de correo electrónico, incluido Gmail.
- **Configura un punto de conexión de redirección.** Aloja un punto de conexión `https://` en tu servidor que redirija a la URL de esquema personalizado de tu aplicación. Los clientes de correo electrónico preservarán el enlace `https://`, y la redirección se encargará de abrir la aplicación.

### ¿La métrica *Aperturas únicas* incluye las *Aperturas por máquina*?

No. *Aperturas únicas* cuenta solo las [Otras aperturas]({{site.baseurl}}/user_guide/analytics/metrics_glossary/#other-opens), que excluyen los correos electrónicos identificados como aperturas por máquina. Las *Aperturas por máquina* se rastrean por separado. En la vista de **Análisis de campaña** y el **Generador de informes**, puedes ver ambas métricas de forma independiente.

### ¿Por qué mi volumen de entrega de correo electrónico no coincide con mi volumen de envío?

Después de que se envía un correo electrónico, el buzón de entrada del destinatario decide cuándo se entrega. Los mensajes pueden diferirse durante horas o días debido a un buzón de entrada lleno, la limitación del ESP desde una IP determinada y razones similares.

Cuando los mensajes diferidos se entregan en un día calendario diferente al día de envío, las *Entregas* pueden superar a los *Envíos* para el mismo rango de fechas. Cuando muchos aplazamientos se acumulan en un día, los *Envíos* pueden superar a las *Entregas* para ese rango.

### ¿Por qué veo una advertencia para incluir un enlace de cancelación de suscripción cuando mi correo electrónico ya tiene uno?

Esta advertencia puede persistir en campañas duplicadas a partir de una campaña que no tenía un enlace de cancelación de suscripción. Para eliminarla:

- Para correos electrónicos HTML, ve a la pestaña **Texto plano** y luego selecciona **Regenerar desde HTML**.
- Después de duplicar, duplica la variante y luego elimina la variante original. **No** selecciones la variante original, o la advertencia puede trasladarse.

### ¿Cuáles son las razones por las que mi usuario no ha recibido una campaña de correo electrónico?

Las razones por las que un usuario no ha recibido una campaña de correo electrónico incluyen:

- No era elegible para recibir el correo electrónico.
- Su dirección de correo electrónico no es válida o no existe.
- Es posible que haya perdido o eliminado el mensaje.
- El mensaje puede estar en su carpeta de correo no deseado.

### ¿Cómo puedo optimizar las imágenes en Outlook?

Outlook a menudo usa un renderizado al estilo de Microsoft Word, que puede añadir un borde alrededor de las imágenes. Puedes envolver el contenido para que se oculte en los clientes de Office usando comentarios condicionales estándar, por ejemplo:

```html
<!--[if !mso]><!-- -->
<span>Content hidden in Outlook desktop</span>
<!--<![endif]-->
```

### ¿Puedo usar imágenes SVG o WEBP en mis mensajes de correo electrónico?

Las imágenes SVG no se renderizan en Gmail web ni en Gmail iOS. WEBP no tiene soporte consistente en todos los clientes. En su lugar, usa formatos ampliamente compatibles como PNG o JPEG para que las imágenes se rendericen de forma fiable.

### ¿Se pueden usar variables Liquid asignadas en una parte del creador de mensajes en otra?

No. Cada parte del correo electrónico (asunto, cuerpo, encabezados, botones, etc.) se genera por separado, por lo que las variables Liquid asignadas en un campo no están disponibles en otro. Asigna las variables en cada campo que las necesite.

### Mi plantilla de correo electrónico no aparece. ¿Dónde está?

Ve a **Plantillas** > **Plantillas de correo electrónico**. Puedes filtrar por tipo (HTML o arrastrar y soltar).

Confirma que tienes permiso para ver plantillas; consulta [Permisos de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/).

### ¿Necesito registrar dominios para correos electrónicos de retransmisión o enmascarados?

El [servicio de retransmisión de correo electrónico privado de Apple]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/email_private_relay_apple_SSO/) requiere que registres tus dominios de envío en el Portal de Desarrolladores de Apple para evitar rebotes. Google Shielded Email no requiere un proceso manual de registro de dominio ni de lista de permitidos.