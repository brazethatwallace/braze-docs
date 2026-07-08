---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre Campaigns
page_order: 10
page_type: FAQ
description: "Esta página ofrece respuestas a preguntas frecuentes sobre Campaigns."
tool: Campaigns

---

# Preguntas frecuentes {#frequently-asked-questions}

> Este artículo ofrece respuestas a algunas preguntas frecuentes sobre Campaigns.

## ¿Cómo creo una campaña multicanal? {#how-do-i-create-a-multichannel-campaign}

Consulta [Campañas multicanal]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#multichannel-campaigns) en **Crear una campaña** para los pasos de configuración y los canales compatibles.

### ¿Puedo añadir un grupo de control a mi campaña multicanal? {#can-i-add-a-control-group-to-my-multichannel-campaign}

Consulta [Grupos de control]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#multichannel-control-groups) en **Crear una campaña**. Para pruebas multicanal, usa [Canvas]({{site.baseurl}}/user_guide/messaging/canvas).

### ¿Cuáles son algunas formas de empezar a probar y optimizar campañas? {#what-are-some-ways-i-can-start-testing-and-optimizing-campaigns}

Las campañas multivariantes y la ejecución de Canvas con múltiples variantes son una excelente forma de empezar. Por ejemplo, puedes ejecutar una [campaña multivariante]({{site.baseurl}}/user_guide/messaging/ab_testing) para probar un mensaje con diferentes textos o líneas del asunto. Los Canvas con múltiples variantes pueden ayudar a probar flujos de trabajo completos.

### ¿Por qué disminuyó la tasa de apertura de mi campaña? {#why-did-the-open-rate-for-my-campaign-decrease}

Las tasas de apertura bajas no siempre están relacionadas con un problema técnico. Puede haber problemas con el recorte de correos electrónicos, lo que resulta en un píxel de seguimiento faltante. Sin embargo, también es posible que menos usuarios estén abriendo sus correos electrónicos debido al contenido o a cambios en el tamaño de la audiencia.

### ¿Cómo se evalúan las audiencias de las campañas? {#how-are-campaign-audiences-evaluated}

De forma predeterminada, las campañas verifican los filtros de audiencia en el momento de la entrada. Para campañas basadas en acciones con un retraso, existe la opción de reevaluar los criterios del segmento en el momento del envío para asegurar que los usuarios sigan siendo parte de la audiencia objetivo cuando se envíe el mensaje.

### ¿Por qué hay una diferencia entre el número de destinatarios únicos y el número de envíos para una campaña o Canvas determinado? {#why-is-there-a-difference-between-the-number-of-unique-recipients-and-the-number-of-sends-for-a-given-campaign-or-canvas}

Una posible explicación podría ser que la campaña o Canvas tiene la reelegibilidad activada, lo que significa que los usuarios que cumplan con los criterios del segmento y la configuración de entrega podrán recibir el mensaje más de una vez. Si la reelegibilidad no está activada, entonces la explicación probable de la diferencia entre envíos y destinatarios únicos puede deberse a que los usuarios tienen múltiples dispositivos, en diferentes plataformas, asociados a sus perfiles.

Por ejemplo, si tienes un Canvas que tiene notificaciones push tanto para iOS como para web, un usuario determinado con dispositivos móviles y de escritorio podría recibir más de un mensaje.

### ¿Por qué *Destinatarios únicos* es mayor que el número de usuarios a los que me dirigí? {#why-is-_unique-recipients_-higher-than-the-number-of-users-i-targeted}

*Destinatarios únicos* puede ser mayor que la audiencia que esperabas porque Braze rastrea destinatarios únicos diarios para los informes. Esto permite que Braze atribuya conversiones dentro de la ventana de conversión cada vez que un usuario recibe el mensaje, en lugar de colapsar múltiples recepciones en un solo recuento de por vida (lo que distorsionaría las matemáticas de conversión).

Por ejemplo, si un usuario recibe una campaña el lunes y nuevamente el viernes y convierte después de cada envío, Braze puede informar eso como dos recepciones y dos conversiones. Si Braze solo contara un "único" de por vida en ambos envíos, perderías una conversión válida o contarías doble contra un destinatario, lo que dificulta la lectura del rendimiento de la campaña.

El mismo patrón se aplica a las campañas recurrentes y a la reelegibilidad: si dos usuarios reciben cada uno un envío recurrente hoy y nuevamente mañana, *Destinatarios únicos* cuenta cuatro filas de destinatarios diarios, no dos perfiles.

### ¿Por qué el número de conversiones puede superar el número de usuarios únicos en campañas multicanal? {#why-can-the-number-of-conversions-exceed-the-number-of-unique-users-for-multichannel-campaigns}

Consulta [Conversiones e informes]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#multichannel-conversions) en **Crear una campaña** y [Reglas de seguimiento de conversiones]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#conversion-tracking-rules) en **Eventos de conversión**.

### ¿Por qué mi campaña tiene una base de usuarios alcanzables más pequeña que el segmento que estoy usando para la campaña? {#why-does-my-campaign-have-a-smaller-reachable-user-base-than-the-segment-that-im-using-for-the-campaign}

Si tienes configurado un [grupo de control global]({{site.baseurl}}/user_guide/audience/global_control_group), esto evitará que un porcentaje de tu audiencia alcanzable reciba campañas. Esto significa que el número de usuarios alcanzables para tu segmento a veces puede ser mayor que el número de usuarios alcanzables para tu campaña, incluso si la campaña está usando ese mismo segmento.

### ¿Qué ofrece la entrega en zona horaria local? {#what-does-local-time-zone-delivery-offer}

La entrega en zona horaria local te permite entregar campañas de mensajería a un segmento basándose en la zona horaria individual de cada usuario. Sin la entrega en zona horaria local, las campañas se programarán según la configuración de zona horaria de tu empresa en Braze.

Por ejemplo, una empresa con sede en Londres que envía una campaña a las 12 pm llegará a los usuarios en la costa oeste de Estados Unidos a las 4 am. Si tu aplicación solo está disponible en ciertos países, esto puede no ser un riesgo para ti. De lo contrario, recomendamos encarecidamente evitar enviar notificaciones push a primera hora de la mañana a tu base de usuarios.

### ¿Cómo reconoce Braze la zona horaria de un usuario? {#how-does-braze-recognize-a-users-time-zone}

Braze determinará automáticamente la zona horaria de un usuario a partir de su dispositivo. Esto garantiza la precisión de la zona horaria y la cobertura completa de tus usuarios. Los usuarios creados a través de la API de usuario o sin una zona horaria tendrán la zona horaria de tu empresa como su zona horaria predeterminada hasta que sean reconocidos en tu aplicación por el SDK.

Puedes verificar la zona horaria de tu empresa en la [configuración de empresa]({{site.baseurl}}/user_guide/administer/global/admin_settings) en el panel.

### ¿Cuándo evalúa Braze a los usuarios para la entrega en zona horaria local? {#when-does-braze-evaluate-users-for-local-time-zone-delivery}

Braze evalúa a los usuarios para su elegibilidad de entrada en:

- La hora de Samoa (UTC+13) en el día programado
- La hora local del día programado

Para que un usuario sea elegible para la entrada, debe ser elegible en ambas verificaciones. Por ejemplo, si un Canvas está programado para lanzarse el 7 de agosto de 2021 a las 2 pm en zona horaria local, entonces dirigirse a un usuario ubicado en Nueva York requeriría las siguientes verificaciones de elegibilidad:

- Nueva York el 6 de agosto de 2021 a las 9 pm
- Nueva York el 7 de agosto de 2021 a las 2 pm

Para entrar, un usuario debe coincidir con tu audiencia y filtros en ambos momentos de evaluación. Si el usuario no es elegible en la primera verificación, Braze no ejecuta la segunda verificación. No hay una duración mínima de tiempo que un usuario deba haber estado en el segmento antes del lanzamiento. Solo importa la elegibilidad en cada verificación.

Este comportamiento de evaluación es independiente de [con cuánta anticipación programas la campaña en el panel](#how-do-i-schedule-a-local-time-zone-campaign). Programar con al menos 24 horas de anticipación es una recomendación porque ayuda a que los mensajes se entreguen a lo largo de toda la ventana de 24 horas de zona horaria local, no un requisito de que cada usuario haya estado en la audiencia durante 24 horas.

#### Ejemplos {#examples}

Por ejemplo, si una campaña está programada para entregarse a las 7 pm UTC, comenzamos a poner en cola los envíos de la campaña tan pronto como se identifica una zona horaria (como Samoa). Esto significa que estamos preparándonos para enviar el mensaje, no enviando la campaña. Si los usuarios no coinciden con ningún filtro cuando verificamos la elegibilidad, no entrarán en la audiencia objetivo.

Como otro ejemplo, supongamos que quieres crear dos campañas programadas para enviarse el mismo día, una por la mañana y otra por la noche, y añadir un filtro para que los usuarios solo puedan recibir la segunda campaña si ya recibieron la primera. Con la entrega en zona horaria local, algunos usuarios podrían no recibir la segunda campaña. Esto se debe a que verificamos la elegibilidad cuando se identifica la zona horaria del usuario, así que si la hora programada aún no ha ocurrido en su zona horaria, no han recibido la primera campaña, lo que significa que no serán elegibles para la segunda campaña.

La siguiente línea de tiempo asume una definición de segmento que incluye una ventana de pertenencia limitada en el tiempo. En este ejemplo, los usuarios salen del segmento 24 horas después de unirse. Ese comportamiento de filtro es una razón por la que un usuario puede pasar la primera verificación y fallar en la segunda.

![Línea de tiempo de un usuario que entra al segmento antes de la primera verificación y luego sale antes de la segunda.]({% image_buster /assets/img/local_time_zone_diagram.png %})

{% details Descripción de la línea de tiempo %}

1. El usuario A entra al segmento a las 6:59 PST (4:59 hora de Samoa).
2. Braze verifica la pertenencia al segmento a las 7 hora de Samoa para determinar qué usuarios son elegibles para recibir la campaña en las próximas 24 horas. El usuario A está en el segmento en este momento.
3. El segmento tiene una ventana de 24 horas, por lo que el usuario A sale del segmento 24 horas después de unirse: 6:59 PST (4:59 hora de Samoa).
4. La campaña en hora local se envía a las 7 PST, pero el usuario A ya ha salido del segmento.

{% enddetails %}

### ¿Cómo programo una campaña en zona horaria local? {#how-do-i-schedule-a-local-time-zone-campaign}

La sección anterior describe cuándo Braze evalúa la elegibilidad para la entrega en zona horaria local (las dos verificaciones). Esta sección describe cuándo configuras la programación de la campaña en el panel (tiempo de anticipación de programación) y qué usuarios aún reciben el mensaje si programas con menos de 24 horas de aviso.

Al programar una campaña, elige enviarla a una hora designada y luego selecciona **Send campaign to users in their local time zone**.

Braze recomienda encarecidamente que todas las campañas en zona horaria local se programen con 24 horas de anticipación. Dado que dicha campaña necesita enviarse durante un día entero, programarla con 24 horas de anticipación garantiza que tu mensaje llegue a todo tu segmento. Sin embargo, puedes programar estas campañas con menos de 24 horas de anticipación si es necesario. Ten en cuenta que Braze no enviará mensajes a ningún usuario que haya pasado la hora de envío por más de 1 hora.

Por ejemplo, si es la 1 pm y programas una campaña en zona horaria local para las 3 pm, entonces la campaña se enviará inmediatamente a todos los usuarios cuya hora local esté entre las 3 pm y las 4 pm, pero no a los usuarios cuya hora local sea las 5 pm. Además, la hora de envío que elijas para tu campaña no debe haber ocurrido aún en la zona horaria de tu empresa.

Editar una campaña en zona horaria local que está programada con menos de 24 horas de anticipación no alterará la programación del mensaje. Si decides editar una campaña en zona horaria local para enviarla a una hora posterior (por ejemplo, 7 pm en lugar de 6 pm), los usuarios que estaban en el segmento objetivo cuando se eligió la hora de envío original seguirán recibiendo el mensaje a la hora original (6 pm). Si editas una zona horaria local para enviar a una hora anterior (por ejemplo, 4 pm en lugar de 5 pm), entonces la campaña seguirá enviándose a todos los miembros del segmento a la hora original (5 pm).

{% alert note %}
Para los componentes de Canvas, los usuarios no necesitan estar en el componente durante 24 horas para recibir el siguiente componente en el recorrido del usuario para la entrega en zona horaria local.
{% endalert %}

Si has permitido que los usuarios sean reelegibles para la campaña, entonces la recibirán nuevamente a la hora original (5 pm). Sin embargo, para todas las ocurrencias posteriores de tu campaña, tus mensajes solo se enviarán a la hora actualizada.

### ¿Cuándo surten efecto los cambios en las campañas de zona horaria local? {#when-do-changes-to-local-time-zone-campaigns-take-effect}

Los segmentos objetivo para campañas en zona horaria local deben incluir al menos una ventana de 48 horas para cualquier filtro basado en tiempo para garantizar la entrega a todo el segmento. Por ejemplo, considera un segmento que se dirige a usuarios en su segundo día con los siguientes filtros:

- Usó la aplicación por primera vez hace más de 1 día
- Usó la aplicación por primera vez hace menos de 2 días

La entrega en zona horaria local puede omitir usuarios en este segmento según la hora de entrega y la zona horaria local de los usuarios. Esto se debe a que un usuario puede salir del segmento para cuando su zona horaria active la entrega.

### ¿Qué cambios puedo hacer a las campañas programadas antes del lanzamiento? {#what-changes-can-i-make-to-scheduled-campaigns-ahead-of-launch}

Cuando la campaña está programada, debes hacer ediciones a cualquier cosa que no sea la composición del mensaje antes de que pongamos los mensajes en cola para enviar. Como en todas las campañas, no puedes editar los eventos de conversión después del lanzamiento.

### Actualicé mi campaña programada. ¿Por qué no se lanzó? {#i-updated-my-scheduled-campaign-why-didnt-it-launch}

Esto puede suceder cuando una campaña está programada para lanzarse en el momento exacto en que fue actualizada. Por ejemplo, si actualmente son las 3:10 pm y cambiaste la campaña para lanzarse a las 3:10 pm y seleccionaste **Update campaign**, ya pasaron las 3:10 pm, lo que significa que la hora programada para el lanzamiento ya pasó. En lugar de programar la campaña para la misma hora, selecciona **Send as soon as campaign launch**.

### ¿Cuál es la "zona segura" antes de que los mensajes de una campaña programada se pongan en cola? {#what-is-the-safe-zone-before-messages-on-a-scheduled-campaign-are-enqueued}

Recomendamos hacer cambios a los mensajes dentro de los siguientes tiempos:

- **Campañas programadas de una sola vez:** Edita hasta la hora de envío programada.
- **Campañas programadas recurrentes:** Edita hasta la hora de envío programada.
- **Campañas en hora local de envío:** Edita hasta 24 horas antes de la hora de envío programada.
- **Campañas de hora de envío óptima:** Edita hasta 24 horas antes del día en que la campaña está programada para enviarse.

Si haces cambios a tu mensaje fuera de estas recomendaciones, es posible que no veas las actualizaciones reflejadas en el mensaje enviado. Por ejemplo, si editas la hora de envío tres horas antes de que una campaña esté programada para enviarse a las 12 pm en hora local, puede ocurrir lo siguiente:

- Braze no envía mensajes a ningún usuario que haya pasado la hora de envío por más de una hora.
- Los mensajes previamente puestos en cola pueden seguir enviándose a la hora originalmente programada, en lugar de la hora ajustada.

Si necesitas hacer cambios, recomendamos detener la campaña actual (esto cancela cualquier mensaje en cola). Luego puedes duplicar la campaña, hacer los cambios necesarios y lanzar la nueva campaña. Es posible que necesites excluir de esta campaña a los usuarios que ya recibieron la primera campaña. Asegúrate de reajustar los tiempos de programación de la campaña para permitir el envío por zona horaria.

### ¿Por qué no entraron usuarios a mi campaña diaria programada en el día del cambio de horario? {#why-did-no-users-enter-my-daily-scheduled-campaign-on-daylight-saving-time-day}

En los días de transición del horario de verano (DST), las campañas diarias programadas pueden ejecutarse hasta una hora antes o después de lo habitual, dependiendo de si los relojes se adelantan o atrasan. Si tu segmento depende de atributos personalizados o eventos con marcas de tiempo que caen dentro de una hora de la hora de envío programada, esos usuarios pueden no cumplir los criterios cuando la campaña evalúa la elegibilidad en el día del DST.

Por ejemplo, supongamos que los usuarios normalmente reciben una actualización de atributo personalizado a las 3 pm UTC, y tu campaña se ejecuta diariamente a las 10:30 am en Nueva York (hora del este). Mientras Nueva York está en horario estándar (UTC-5), las 10:30 am ET corresponden a las 3:30 pm UTC, por lo que la campaña se ejecuta después de que se registra el atributo. Cuando Nueva York cambia al horario de verano (UTC-4), las 10:30 am ET corresponden a las 2:30 pm UTC, por lo que en el día del cambio de primavera la campaña puede ejecutarse antes de la actualización del atributo a las 3 pm UTC. Debido a que el atributo que califica aún no existe, esos usuarios son filtrados. Si la reelegibilidad está desactivada, los usuarios que entraron en días anteriores no pueden volver a entrar, lo que resulta en cero entradas para ese día.

Para evitar esto, asegúrate de que las actualizaciones de atributos personalizados o eventos ocurran más de una hora antes de la hora de envío programada de la campaña.

### ¿Por qué el número de usuarios que entran a una campaña no coincide con el número esperado? {#why-does-the-number-of-users-entering-a-campaign-not-match-the-expected-number}

El número de usuarios que entran a una campaña puede diferir de tu número esperado debido a cómo se evalúan las audiencias y los desencadenantes. En Braze, una audiencia se evalúa antes del desencadenante (a menos que se use un desencadenante de [cambio en atributo]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Esto hará que los usuarios salgan de la campaña si no son inicialmente parte de tu audiencia seleccionada antes de que se evalúen las acciones desencadenantes.

{% alert tip %}
Para obtener más ayuda con la solución de problemas de campañas, asegúrate de contactar a soporte de Braze dentro de los 30 días posteriores a la ocurrencia de tu problema, ya que solo tenemos los últimos 30 días de registros de diagnóstico.
{% endalert %}

### ¿Por qué los usuarios recibieron mi campaña dos veces después de editarla? {#why-did-users-receive-my-campaign-twice-after-i-edited-it}

Si editas una campaña en vivo sin detenerla primero, los usuarios pueden recibir el mensaje dos veces. Esto sucede porque editar una campaña en vivo vuelve a poner en cola a los usuarios para la versión actualizada mientras la cola original aún se está procesando. Los usuarios que aún no han recibido el mensaje original pueden terminar en ambas colas. Para evitar esto, siempre [detén la campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch#stopping-your-campaign) antes de hacer cambios.

### ¿Cuál es la diferencia entre las opciones Exportación de datos de usuario a CSV y Exportación de direcciones de correo electrónico a CSV en mi página de análisis de campaña? {#what-is-the-difference-between-the-csv-export-user-data-and-csv-export-email-address-options-on-my-campaign-analytics-page}

Seleccionar la opción **CSV Export Email Addresses** descarga datos solo para los usuarios con direcciones de correo electrónico. Por ejemplo, si tienes un segmento de 100,000 usuarios, pero solo 50,000 de esos usuarios tienen direcciones de correo electrónico, y haces clic en **CSV Export Email Addresses**, la exportación contiene solo 50,000 filas de datos. En comparación, seleccionar **CSV Export User Data** exporta todos los datos de usuario.

### ¿Puedo buscar una campaña por su identificador de API? {#can-i-search-for-a-campaign-by-its-api-identifier}

Sí, usa el filtro `api_id:YOUR_API_ID` en la página de **Campaigns** para buscar una campaña por su identificador de API. Consulta [buscar campañas]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/search_campaigns) para obtener más información.

### ¿Por qué los espacios en blanco aparecen de forma diferente en los campos de entrada frente al texto mostrado? {#why-does-whitespace-appear-differently-in-input-fields-versus-displayed-text}

El manejo de espacios en blanco difiere entre los campos de entrada y los componentes de texto mostrado debido al estilo CSS. En los componentes de texto con el CSS predeterminado `white-space: normal`, múltiples espacios consecutivos se colapsan en un solo espacio al mostrarse. Este es el comportamiento estándar de HTML para texto renderizado.

Los campos de entrada preservan múltiples espacios exactamente como los introduces, porque necesitas ver y editar el espaciado exacto para una entrada de datos precisa. Esto significa que el texto con múltiples espacios puede aparecer de forma diferente cuando se ve en un campo de entrada (donde todos los espacios se preservan) frente a cuando se muestra en otras partes del panel (donde el CSS puede colapsar múltiples espacios).

Por ejemplo, si introduces un nombre de campaña o un parámetro UTM con múltiples espacios en un campo de entrada, verás todos los espacios preservados. Sin embargo, cuando ese mismo texto aparece en resultados de búsqueda, listas de campañas u otros componentes de texto, múltiples espacios pueden aparecer como un solo espacio debido al manejo de espacios en blanco del CSS.

### ¿Cuál es la diferencia entre campañas de API y campañas activadas por API? {#what-is-the-difference-between-api-campaigns-and-api-triggered-campaigns}

Las campañas activadas por API te permiten gestionar el texto de la campaña, las pruebas multivariantes y las reglas de reelegibilidad dentro del panel de Braze mientras activas la entrega de ese contenido desde tus propios servidores y sistemas. Estos mensajes también pueden incluir datos adicionales para ser plantillados en los mensajes en tiempo real.

Las campañas de API se usan para rastrear los mensajes enviados usando la API. A diferencia de la mayoría de las campañas, no especificas el mensaje, los destinatarios ni la programación, sino que pasas los identificadores en tus llamadas a la API.

### ¿Cómo puedo confirmar si mis usuarios recibieron una campaña activada por API? {#how-can-i-confirm-if-my-users-received-an-api-triggered-campaign}

Puedes [crear un segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) usando el filtro **Received Campaign** y luego seleccionar la campaña activada por API específica que deseas verificar. Después de guardar el segmento, usa el [endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) para exportar los usuarios en ese segmento.

### ¿Puedo eliminar una campaña? {#can-i-delete-a-campaign}

No, pero puedes [archivar una campaña]({{site.baseurl}}/user_guide/messaging/governance/archiving).

### ¿Cuál es la diferencia entre campañas basadas en acciones y campañas activadas por API? {#what-is-the-difference-between-action-based-and-api-triggered-campaigns}

<style>
table th:nth-child(1) {
    width: 50%;
}
table th:nth-child(3) {
    width: 50%;
}
</style>

#### Basadas en acciones {#action-based}

Las campañas de entrega basada en acciones o campañas activadas por eventos son muy efectivas para mensajes transaccionales o basados en logros y te permiten activarlas para que se envíen después de que un usuario complete un evento determinado.

| Ventajas | Desventajas |
| ---- | ---- |
| • Visibilidad de las cargas útiles JSON entrantes en la plataforma (si el evento es activado por un usuario de prueba) a través del **Registro de actividad de mensajes**<br><br>• Los elementos de personalización se incluyen en las propiedades del evento personalizado<br><br>• El evento personalizado se puede usar para crear Segments de usuarios elegibles para el mensaje | • Consume puntos de datos |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Basadas en acciones" }

#### Activadas por API {#api-triggered}

Las campañas activadas por API y activadas por servidor son ideales para manejar transacciones más avanzadas, permitiéndote activar la entrega del contenido de la campaña desde tus propios servidores y sistemas. La solicitud de API para activar el mensaje también puede incluir datos adicionales para ser plantillados en el mensaje en tiempo real.

| Beneficios | Consideraciones |
| ---- | ---- |
| • No registra puntos de datos<br><br>• Los elementos de personalización se incluyen en las propiedades de la carga útil JSON | • No te permite crear un segmento de usuarios elegibles para el mensaje en las propiedades de la carga útil JSON<br><br>• No es posible ver las cargas útiles JSON entrantes con el **Registro de actividad de mensajes** |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Activadas por API" }

### ¿Qué debo incluir al enviar un ticket de soporte por un error de "Tiempo de solicitud agotado"? {#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error}

Si encuentras un error de "Tiempo de solicitud agotado" al crear o editar una campaña o Canvas y necesitas contactar a [soporte de Braze]({{site.baseurl}}/braze_support), incluye la siguiente información para ayudar a acelerar la resolución:

- **Grabación de pantalla:** Una grabación de los pasos que seguiste antes de ver el error, incluyendo cualquier transición de página.
- **Marca de tiempo y zona horaria:** La hora exacta en que ocurrió el error y tu zona horaria.
- **Navegador y versión:** El navegador que estás usando (por ejemplo, Chrome 120, Safari 17) y si has intentado reproducir el error en un navegador diferente.
- **Pasos para reproducir:** Una descripción clara de las acciones que desencadenan el error, incluyendo cualquier configuración específica de campaña o Canvas involucrada.
- **Registros de red (opcional):** Abre las herramientas de desarrollador de tu navegador (pestaña **Network**), reproduce el error y exporta el registro de red como un archivo HAR (HTTP Archive). Esto ayuda al equipo de soporte a identificar qué llamada de API está agotando el tiempo.

### ¿Por qué mis análisis de envío no coinciden con el límite máximo de destinatarios que establecí? {#why-dont-my-send-analytics-match-the-maximum-recipient-limit-i-set}

Si añades o cambias un límite máximo de destinatarios en una campaña activa, es posible que el límite no se refleje en tus análisis de envío por las siguientes razones:

- **Límite añadido después del lanzamiento:** Si el límite máximo de destinatarios no se establece cuando la campaña se lanza, los mensajes que ya están en cola antes de que apliques el límite se envían de todos modos. El límite solo surte efecto para los envíos que pongas en cola después de guardar el cambio.
- **Interacción con el límite de velocidad:** Si una campaña también tiene límite de velocidad, los mensajes pueden distribuirse durante una ventana de tiempo más larga. El límite máximo de destinatarios se evalúa cuando los mensajes se ponen en cola, no cuando se entregan. Si el límite se cambia mientras los mensajes ya están en la cola, el límite original se aplica a esos mensajes.
- **Campañas recurrentes:** Para campañas recurrentes, cada envío programado evalúa el límite máximo de destinatarios de forma independiente. Cambiar el límite entre envíos no ajusta retroactivamente los recuentos de envíos anteriores.

Para evitar desajustes, establece el límite máximo de destinatarios antes de lanzar la campaña y evita modificarlo mientras los envíos están en progreso.

### ¿Por qué los envíos son menores que el tamaño estimado de la audiencia? {#why-are-sends-lower-than-the-estimated-audience-size}

Varios factores pueden causar que el número de envíos sea menor que el tamaño estimado de la audiencia:

- **Entrega basada en acciones:** Los usuarios solo generan envíos después de realizar el desencadenante, por lo que los envíos se acumulan con el tiempo y pueden quedar por detrás de la estimación inicial que se muestra cuando creaste la campaña.
- **Ediciones de audiencia después del lanzamiento:** Cambiar los filtros de entrada u objetivo después del lanzamiento puede dejar la instantánea de **Audiencia estimada** desincronizada con quiénes aún cumplen los criterios en envíos posteriores (por ejemplo, cuando los usuarios no son elegibles para volver a entrar).
- **Paso de rutas de audiencia:** Para Canvas, un paso de [Rutas de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) solo envía mensajes a los usuarios que coinciden con la rama de mayor prioridad para la que califican, lo que puede reducir los envíos en comparación con un recuento de segmento plano.
- **Grupos de control:** Si un [grupo de control global]({{site.baseurl}}/user_guide/audience/global_control_group) o un grupo de control a nivel de campaña está en uso, una parte de la audiencia se retiene de la entrega.
- **Tiempos y ventanas de entrega:** Para campañas en zona horaria local o programadas, los usuarios deben cumplir los criterios tanto en el momento de entrada como en el de envío; los usuarios en ciertas zonas horarias pueden quedar fuera de la ventana de entrega.
- **Deduplicación de correo electrónico:** Tu campaña o Canvas se dirige a múltiples usuarios con correos electrónicos coincidentes, por lo que se elige un usuario aleatorio con esa dirección de correo electrónico en el momento del envío. El mensaje solo se envía una vez y se deduplica para que no se envíe a la misma dirección de correo electrónico varias veces, pero el tamaño estimado de tu audiencia incluye a todos los usuarios.
- **Filtros de capacidad de entrega de correo electrónico:** Para campañas de correo electrónico, Braze excluye a los usuarios que han tenido rebotes duros, se han dado de baja de correos electrónicos, han sido marcados como correo no deseado, no tienen dirección de correo electrónico en su perfil o no están suscritos a un grupo de suscripción requerido. Estas verificaciones se ejecutan en el momento del envío, por lo que un usuario presente en tu segmento aún puede ser excluido del recuento real de envíos.
- **Limitación de frecuencia global:** Los límites a nivel de espacio de trabajo pueden evitar que usuarios elegibles reciban otro mensaje en la misma ventana, lo que reduce los envíos realizados.
- **Usuarios recién importados:** Los perfiles que acaban de volverse elegibles pueden no recibir hasta la siguiente evaluación o pasada de envío, por lo que los recuentos se actualizan en una ejecución posterior.
- **Alcanzabilidad push:** Para campañas push, confirma que la audiencia tiene push habilitado para la aplicación correcta. Si no filtras por usuarios con push habilitado, la audiencia estimada puede incluir perfiles que no pueden recibir push. Verifica **Usuarios alcanzables** en el paso **Público objetivo** para una estimación operativa más cercana.
- **Límite de velocidad:** Un [límite de velocidad de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) limita cuántos mensajes envía Braze por minuto durante una única ocurrencia de envío. Braze distribuye la entrega a lo largo de una ventana más larga, por lo que algunos envíos pueden diferirse, no reflejarse aún en el recuento o no completarse si el límite es bajo en relación con la audiencia elegible.
- **Ventanas de reelegibilidad:** Los usuarios que aún no son reelegibles no recibirán nuevamente durante el período de espera, por lo que los envíos quedan por debajo del tamaño estimado de la audiencia para ese período.
- **Ventana de informes:** El rango de tiempo de los análisis puede no incluir todos los envíos.
- **Reevaluación del segmento:** Para campañas basadas en acciones o programadas que reevalúan en el momento del envío, los usuarios que estaban en el segmento cuando la campaña se puso en cola pueden ya no cumplir los criterios cuando el mensaje se envía realmente.
- **Límites de envío:** Un número máximo de usuarios (o límite similar) en **Target Audiences** detiene la entrega cuando se alcanza el límite.
- **Filtros estrictos de dispositivo o navegador:** Los filtros que solo coinciden con las versiones más recientes de aplicaciones o navegadores reducen el conjunto alcanzable en el momento del envío en comparación con una vista previa de segmento amplia.

### ¿Dónde están las preguntas frecuentes sobre la limitación de frecuencia global? {#where-are-frequently-asked-questions-about-global-frequency-capping}

Para preguntas sobre días calendario, push silencioso, webhooks, comportamiento de Canvas y temas relacionados, consulta las [Preguntas frecuentes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/faq) de [Límite de velocidad y limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

### ¿Por qué mi campaña está experimentando tasas de envío más bajas? {#why-is-my-campaign-experiencing-lower-send-rates}

Si notas que tus campañas diarias programadas envían a menos usuarios con el tiempo, verifica lo siguiente:

- **Verifica si la reelegibilidad está activada:** Sin reelegibilidad, Braze envía el mensaje a cada usuario solo una vez. En campañas diarias programadas, solo los usuarios que coinciden con la audiencia y que aún no han recibido el mensaje son elegibles para cada envío. A medida que más usuarios reciben el mensaje, cada envío posterior tiene menos usuarios elegibles, por lo que el volumen de envíos disminuye.
- **Verifica si la audiencia tiene membresía fija:** Las audiencias construidas a partir de una lista fija de usuarios (como una [importación CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) usada como filtro de segmento) no ganan nuevos miembros automáticamente. Sin nuevos participantes, el volumen de envíos no puede recuperarse a medida que los usuarios son contactados.

Para [límites de velocidad de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) y otros factores que reducen los envíos en una única ocurrencia, consulta [¿Por qué los envíos son menores que el tamaño estimado de la audiencia?](#why-are-sends-lower-than-the-estimated-audience-size).

### ¿Por qué los destinatarios únicos pueden superar los envíos en correo electrónico y SMS? {#why-can-unique-recipients-exceed-sends-for-email-and-sms}

Para correo electrónico y SMS, Braze incrementa **Destinatarios únicos** antes del intento de envío al ESP e incrementa **Envíos** después de una respuesta exitosa del ESP. Los errores permanentes (como direcciones de correo electrónico no válidas) o direcciones duplicadas hacen que los destinatarios únicos superen los envíos.

### ¿Por qué **Último envío** no coincide con mi hora de envío programada? {#why-doesnt-last-sent-match-my-scheduled-send-time}

Para una campaña con un único envío programado, **Último envío** coincide con la hora de lanzamiento. Para campañas recurrentes con **Send in local time zone** habilitado, **Último envío** puede aparecer antes de la hora programada porque los envíos a usuarios en zonas horarias más tempranas (por ejemplo, GMT frente a PST) se completan antes de la hora programada de tu espacio de trabajo.

### ¿Por qué una campaña histórica detenida ya no muestra métricas en la página de **Analytics**? {#why-does-a-stopped-historical-campaign-no-longer-show-metrics-on-the-analytics-page}

La pestaña **Analytics** muestra de forma predeterminada los últimos 90 días. Si la campaña se envió por última vez fuera de esa ventana, las métricas pueden aparecer como cero hasta que ajustes el rango de fechas en la página de **Analytics** para incluir el período en que la campaña se envió. Para más información, consulta [Análisis de campaña]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics).

**Restaurar datos de interacción** no restaura los análisis de campaña. Solo se aplica a los filtros de retargeting y al historial de interacciones del usuario. Para más información, consulta [Datos de interacción de mensajería]({{site.baseurl}}/messaging_interaction_data).