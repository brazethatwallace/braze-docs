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

Consulta [Campaigns multicanal]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#create-a-multichannel-campaign) en **Crear una Campaign** para ver los pasos de configuración y los canales compatibles.

### ¿Puedo añadir un grupo de control a mi campaña multicanal? {#can-i-add-a-control-group-to-my-multichannel-campaign}

Consulta [Grupos de control]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#multichannel-control-groups) en **Crear una Campaign**. Para pruebas multicanal, usa [Canvas]({{site.baseurl}}/user_guide/messaging/canvas).

### ¿Cuáles son algunas formas de empezar a probar y optimizar Campaigns? {#what-are-some-ways-i-can-start-testing-and-optimizing-campaigns}

Las Campaigns multivariante y ejecutar Canvas con múltiples variantes son una excelente manera de empezar. Por ejemplo, puedes ejecutar una [Campaign multivariante]({{site.baseurl}}/user_guide/messaging/ab_testing) para probar un mensaje que tiene diferentes textos o líneas del asunto. Los Canvas con múltiples variantes pueden ayudar a probar flujos de trabajo completos.

### ¿Por qué disminuyó la tarifa abierta de mi Campaign? {#why-did-the-open-rate-for-my-campaign-decrease}

Las tarifas abiertas bajas no siempre están correlacionadas con un problema técnico. Puede haber problemas con el recorte del correo electrónico, lo que resulta en un píxel de seguimiento faltante. Sin embargo, también es posible que menos usuarios estén abriendo sus correos electrónicos debido al contenido o cambios en el tamaño de la audiencia.

### ¿Cómo se evalúan las audiencias de las Campaigns? {#how-are-campaign-audiences-evaluated}

De forma predeterminada, las Campaigns comprueban los filtros de audiencia en el momento de la entrada. Para las Campaigns con entrega basada en acciones que tienen un retraso, existe una opción para reevaluar los criterios de Segment en el momento del envío para asegurar que los usuarios sigan formando parte del público objetivo cuando se envía el mensaje.

### ¿Por qué hay una diferencia entre el número de destinatarios únicos y el número de envíos para una Campaign o Canvas determinado? {#why-is-there-a-difference-between-the-number-of-unique-recipients-and-the-number-of-sends-for-a-given-campaign-or-canvas}

Una posible explicación podría ser que la Campaign o el Canvas tiene activada la reelegibilidad, lo que significa que los usuarios que cumplan con los criterios de Segment y la configuración de entrega podrán recibir el mensaje más de una vez. Si la reelegibilidad no está activada, entonces la explicación probable de la diferencia entre envíos y destinatarios únicos puede deberse a que los usuarios tienen múltiples dispositivos, en distintas plataformas, asociados a sus perfiles.

Por ejemplo, si tienes un Canvas que tiene tanto notificaciones push de iOS como push web, un usuario determinado con dispositivos móviles y de escritorio podría recibir más de un mensaje.

### ¿Por qué *Destinatarios únicos* es mayor que el número de usuarios que segmenté? {#why-is-_unique-recipients_-higher-than-the-number-of-users-i-targeted}

*Destinatarios únicos* puede ser mayor que la audiencia que esperabas porque Braze rastrea los destinatarios únicos diarios para la generación de informes. Esto permite a Braze atribuir conversiones dentro de la ventana de conversión cada vez que un usuario recibe el mensaje, en lugar de condensar múltiples recepciones en un solo conteo de por vida (lo que sesgaría las matemáticas de conversión).

Por ejemplo, si un usuario recibe una Campaign el lunes y de nuevo el viernes y convierte después de cada envío, Braze puede reportar eso como dos recepciones y dos conversiones. Si Braze solo contara un "único" de por vida en ambos envíos, perderías una conversión válida o contarías doble contra un destinatario, lo que dificulta la lectura del rendimiento de la Campaign.

El mismo patrón aplica a las Campaigns recurrentes y a la reelegibilidad: si dos usuarios reciben un envío recurrente hoy y de nuevo mañana, *Destinatarios únicos* cuenta cuatro filas de destinatarios diarios, no dos perfiles.

### ¿Por qué el número de conversiones puede superar el número de usuarios únicos en las Campaigns multicanal? {#why-can-the-number-of-conversions-exceed-the-number-of-unique-users-for-multichannel-campaigns}

Consulta [Conversiones e informes]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#multichannel-conversions) en **Crear una Campaign** y [Reglas de seguimiento de conversiones]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#conversion-tracking-rules) en **Eventos de conversión**.

### ¿Por qué mi Campaign tiene una base de usuarios alcanzable más pequeña que el Segment que estoy usando para la Campaign? {#why-does-my-campaign-have-a-smaller-reachable-user-base-than-the-segment-that-im-using-for-the-campaign}

Si tienes un [grupo de control global]({{site.baseurl}}/user_guide/audience/global_control_group) configurado, esto evitará que un porcentaje de tu audiencia alcanzable reciba Campaigns. Esto significa que el número de usuarios alcanzables para tu Segment puede ser a veces mayor que el número de usuarios alcanzables para tu Campaign, incluso si la Campaign está usando ese mismo Segment.

### ¿Qué ofrece la entrega en zona horaria local? {#what-does-local-time-zone-delivery-offer}

La entrega en zona horaria local te permite enviar Campaigns de mensajería a un Segment basándose en la zona horaria individual de cada usuario. Sin la entrega en zona horaria local, las Campaigns se programarán según la configuración de zona horaria de tu empresa en Braze.

Por ejemplo, una empresa con sede en Londres que envía una Campaign a las 12 pm llegará a los usuarios en la costa oeste de América a las 4 am. Si tu aplicación solo está disponible en ciertos países, esto puede no ser un riesgo para ti. De lo contrario, te recomendamos encarecidamente evitar enviar notificaciones push a primera hora de la mañana a tu base de usuarios.

### ¿Cómo reconoce Braze la zona horaria de un usuario? {#how-does-braze-recognize-a-users-time-zone}

Braze determinará automáticamente la zona horaria del usuario a partir de su dispositivo. Esto garantiza la precisión de la zona horaria y la cobertura completa de tus usuarios. Los usuarios creados a través de la API de usuario o de otro modo sin una zona horaria tendrán la zona horaria de tu empresa como su zona horaria predeterminada hasta que sean reconocidos en tu aplicación por el SDK or kit de desarrollo de software.

Puedes comprobar la zona horaria de tu empresa en la [configuración de la empresa]({{site.baseurl}}/user_guide/administer/global/admin_settings) en el panel.

### ¿Cuándo evalúa Braze a los usuarios para la entrega en zona horaria local? {#when-does-braze-evaluate-users-for-local-time-zone-delivery}

Braze evalúa a los usuarios para su elegibilidad de entrada en:

- La hora de Samoa (UTC+13) en el día programado
- La hora local del día programado

Para que un usuario sea elegible para la entrada, debe ser elegible en ambas comprobaciones. Por ejemplo, si un Canvas está programado para lanzarse el 7 de agosto de 2021 a las 2 pm en zona horaria local, entonces segmentar a un usuario ubicado en Nueva York requeriría las siguientes comprobaciones de elegibilidad:

- Nueva York el 6 de agosto de 2021 a las 9 pm
- Nueva York el 7 de agosto de 2021 a las 2 pm

Para entrar, un usuario debe coincidir con tu audiencia y filtros en ambos momentos de evaluación. Si el usuario no es elegible en la primera comprobación, Braze no ejecuta la segunda. No hay una duración mínima de tiempo que un usuario deba haber estado en el Segment antes del lanzamiento. Solo importa la elegibilidad en cada comprobación.

Este comportamiento de evaluación es independiente de [con cuánta anticipación programas la Campaign en el panel](#how-do-i-schedule-a-local-time-zone-campaign). Programar con al menos 24 horas de antelación es una recomendación porque ayuda a que los mensajes se entreguen a lo largo de toda la ventana de 24 horas de zona horaria local, no un requisito de que cada usuario haya estado en la audiencia durante 24 horas.

#### Ejemplos {#examples}

Por ejemplo, si una Campaign está programada para entregarse a las 7 pm UTC, comenzamos a poner en cola los envíos de la Campaign tan pronto como se identifica una zona horaria (como Samoa). Esto significa que estamos preparándonos para enviar el mensaje, no enviando la Campaign. Si los usuarios no coinciden con ningún filtro cuando comprobamos la elegibilidad, no entrarán en el público objetivo.

Como otro ejemplo, supongamos que quieres crear dos Campaigns programadas para enviarse el mismo día: una por la mañana y otra por la noche, y añadir un filtro para que los usuarios solo puedan recibir la segunda Campaign si ya han recibido la primera. Con la entrega en zona horaria local, algunos usuarios pueden no recibir la segunda Campaign. Esto se debe a que comprobamos la elegibilidad cuando se identifica la zona horaria del usuario, así que si la hora programada aún no ha ocurrido en su zona horaria, no han recibido la primera Campaign, lo que significa que no serán elegibles para la segunda.

La siguiente línea de tiempo asume una definición de Segment que incluye una ventana de membresía limitada en el tiempo. En este ejemplo, los usuarios salen del Segment 24 horas después de unirse. Ese comportamiento de filtro es una razón por la que un usuario puede pasar la primera comprobación y fallar la segunda.

![Línea de tiempo de un usuario que entra al Segment antes de la primera comprobación y luego sale antes de la segunda.]({% image_buster /assets/img/local_time_zone_diagram.png %})

{% details Descripción de la línea de tiempo %}

1. El usuario A entra al Segment a las 6:59 PST (4:59 hora de Samoa).
2. Braze comprueba la membresía del Segment a las 7 hora de Samoa para determinar qué usuarios son elegibles para recibir la Campaign en las siguientes 24 horas. El usuario A está en el Segment en este momento.
3. El Segment tiene una ventana de 24 horas, por lo que el usuario A sale del Segment 24 horas después de unirse: 6:59 PST (4:59 hora de Samoa).
4. La Campaign de hora local se envía a las 7 PST, pero el usuario A ya ha salido del Segment.

{% enddetails %}

### ¿Cómo programo una Campaign en zona horaria local? {#how-do-i-schedule-a-local-time-zone-campaign}

La sección anterior describe cuándo Braze evalúa la elegibilidad para la entrega en zona horaria local (las dos comprobaciones). Esta sección describe cuándo configuras la programación de la Campaign en el panel (tiempo de anticipación de la programación) y qué usuarios aún reciben el mensaje si programas con menos de 24 horas de aviso.

Al programar una Campaign, elige enviarla a una hora designada y luego selecciona **Enviar Campaign a los usuarios en su zona horaria local**.

Braze recomienda encarecidamente que todas las Campaigns de zona horaria local se programen con 24 horas de antelación. Dado que dicha Campaign necesita enviarse a lo largo de un día completo, programarla con 24 horas de antelación garantiza que tu mensaje llegue a todo tu Segment. Sin embargo, puedes programar estas Campaigns con menos de 24 horas de antelación si es necesario. Ten en cuenta que Braze no enviará mensajes a ningún usuario que haya pasado la hora de envío por más de 1 hora.

Por ejemplo, si son las 1 pm y programas una Campaign de zona horaria local para las 3 pm, la Campaign se enviará inmediatamente a todos los usuarios cuya hora local esté entre las 3 pm y las 4 pm, pero no a los usuarios cuya hora local sea las 5 pm. Además, la hora de envío que elijas para tu Campaign no debe haber ocurrido ya en la zona horaria de tu empresa.

Editar una Campaign de zona horaria local que está programada con menos de 24 horas de antelación no alterará la programación del mensaje. Si decides editar una Campaign de zona horaria local para enviarla a una hora posterior (por ejemplo, 7 pm en lugar de 6 pm), los usuarios que estaban en el Segment segmentado cuando se eligió la hora de envío original seguirán recibiendo el mensaje a la hora original (6 pm). Si editas una Campaign de zona horaria local para enviarla a una hora anterior (por ejemplo, 4 pm en lugar de 5 pm), entonces la Campaign se enviará a todos los miembros del Segment a la hora original (5 pm).

{% alert note %}
Para los componentes de Canvas, los usuarios no necesitan estar en el componente durante 24 horas para recibir el siguiente componente en el recorrido del usuario para la entrega en zona horaria local.
{% endalert %}

Si has permitido que los usuarios vuelvan a ser reelegibles para la Campaign, la recibirán de nuevo a la hora original (5 pm). Sin embargo, para todas las ocurrencias posteriores de tu Campaign, tus mensajes solo se enviarán a la hora actualizada.

### ¿Cuándo surten efecto los cambios en las Campaigns de zona horaria local? {#when-do-changes-to-local-time-zone-campaigns-take-effect}

Los Segments objetivo para las Campaigns de zona horaria local deben incluir al menos una ventana de 48 horas para cualquier filtro basado en el tiempo para garantizar la entrega a todo el Segment. Por ejemplo, considera un Segment que segmenta usuarios en su segundo día con los siguientes filtros:

- Usó la aplicación por primera vez hace más de 1 día
- Usó la aplicación por primera vez hace menos de 2 días

La entrega en zona horaria local puede no alcanzar a usuarios en este Segment según la hora de entrega y la zona horaria local de los usuarios. Esto se debe a que un usuario puede salir del Segment para cuando su zona horaria active la entrega.

### ¿Qué cambios puedo hacer a las Campaigns programadas antes del lanzamiento? {#what-changes-can-i-make-to-scheduled-campaigns-ahead-of-launch}

Cuando la Campaign está programada, debes hacer ediciones a cualquier cosa que no sea la composición del mensaje antes de que pongamos los mensajes en cola para enviar. Como con todas las Campaigns, no puedes editar los eventos de conversión después del lanzamiento.

### Actualicé mi Campaign programada. ¿Por qué no se lanzó? {#i-updated-my-scheduled-campaign-why-didnt-it-launch}

Esto puede ocurrir cuando una Campaign está programada para lanzarse a la hora exacta en que fue actualizada. Por ejemplo, si actualmente son las 3:10 pm y cambiaste la Campaign para lanzarse a las 3:10 pm y seleccionaste **Actualizar Campaign**, ya ha pasado de las 3:10 pm, lo que significa que la hora programada para el lanzamiento ya pasó. En lugar de programar la Campaign para la misma hora, selecciona **Enviar tan pronto como se lance la Campaign**.

### ¿Cuál es la "zona segura" antes de que los mensajes de una Campaign programada se pongan en cola? {#what-is-the-safe-zone-before-messages-on-a-scheduled-campaign-are-enqueued}

Recomendamos hacer cambios a los mensajes dentro de los siguientes tiempos:

- **Campaigns programadas de una sola vez:** Edita hasta la hora de envío programada.
- **Campaigns programadas recurrentes:** Edita hasta la hora de envío programada.
- **Campaigns de envío en hora local:** Edita hasta 24 horas antes de la hora de envío programada.
- **Campaigns de hora de envío óptima:** Edita hasta 24 horas antes del día en que la Campaign está programada para enviarse.

Si haces cambios a tu mensaje fuera de estas recomendaciones, puede que no veas las actualizaciones reflejadas en el mensaje enviado. Por ejemplo, si editas la hora de envío tres horas antes de que una Campaign esté programada para enviarse a las 12 pm en hora local, puede ocurrir lo siguiente:

- Braze no envía mensajes a ningún usuario que haya pasado la hora de envío por más de una hora.
- Los mensajes previamente puestos en cola pueden seguir enviándose a la hora en que fueron puestos en cola originalmente, en lugar de la hora ajustada.

Si necesitas hacer cambios, te recomendamos detener la Campaign actual (esto cancela cualquier mensaje en cola). Luego puedes duplicar la Campaign, hacer los cambios necesarios y lanzar la nueva Campaign. Puede que necesites excluir de esta Campaign a los usuarios que ya han recibido la primera Campaign. Asegúrate de reajustar los tiempos de programación de la Campaign para permitir el envío por zona horaria.

### ¿Por qué no entraron usuarios a mi Campaign programada diaria el día del cambio de horario? {#why-did-no-users-enter-my-daily-scheduled-campaign-on-daylight-saving-time-day}

En los días de transición del horario de verano (DST), las Campaigns programadas diarias pueden ejecutarse hasta una hora antes o después de lo habitual, dependiendo de si los relojes se adelantan o atrasan. Si tu Segment depende de atributos personalizados o eventos con marcas de tiempo que caen dentro de una hora de la hora de envío programada, esos usuarios pueden no cumplir los criterios aún cuando la Campaign evalúa la elegibilidad en el día del DST.

Por ejemplo, supongamos que los usuarios típicamente reciben una actualización de atributo personalizado a las 3 pm UTC, y tu Campaign se ejecuta diariamente a las 10:30 am en Nueva York (hora del este). Mientras Nueva York está en horario estándar (UTC-5), las 10:30 am ET corresponden a las 3:30 pm UTC, por lo que la Campaign se ejecuta después de que se registra el atributo. Cuando Nueva York pasa al horario de verano (UTC-4), las 10:30 am ET corresponden a las 2:30 pm UTC, así que en el día del cambio de primavera la Campaign puede ejecutarse antes de la actualización del atributo a las 3 pm UTC. Como el atributo que los califica aún no existe, esos usuarios quedan filtrados. Si la reelegibilidad está desactivada, los usuarios que entraron en días anteriores no pueden volver a entrar, resultando en cero entradas para ese día.

Para evitar esto, asegúrate de que las actualizaciones de atus atributos personalizados o eventos ocurran más de una hora antes de la hora de envío programada de la Campaign.

### ¿Por qué el número de usuarios que entran a una Campaign no coincide con el número esperado? {#why-does-the-number-of-users-entering-a-campaign-not-match-the-expected-number}

El número de usuarios que entran a una Campaign puede diferir del número esperado debido a cómo se evalúan las audiencias y los desencadenantes. En Braze, la audiencia se evalúa antes del desencadenante (a menos que se use un desencadenante de [cambio en atributo]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Esto hará que los usuarios salgan de la Campaign si inicialmente no forman parte de la audiencia seleccionada antes de que se evalúen las acciones desencadenantes.

{% alert tip %}
Para obtener asistencia adicional con la solución de problemas de Campaigns, asegúrate de contactar a soporte de Braze dentro de los 30 días posteriores a la ocurrencia del problema, ya que solo tenemos los últimos 30 días de registros de diagnóstico.
{% endalert %}

### ¿Por qué los usuarios recibieron mi Campaign dos veces después de editarla? {#why-did-users-receive-my-campaign-twice-after-i-edited-it}

Si editas una Campaign en vivo sin detenerla primero, los usuarios pueden recibir el mensaje dos veces. Esto sucede porque editar una Campaign en vivo vuelve a poner en cola a los usuarios para la versión actualizada mientras la cola original aún se está procesando. Los usuarios que aún no han recibido el mensaje original pueden terminar en ambas colas. Para evitar esto, siempre [detén la Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/change_your_campaign_after_launch#stopping-your-campaign) antes de hacer cambios.

### ¿Cuál es la diferencia entre las opciones de Exportar datos de usuario en CSV y Exportar direcciones de correo electrónico en CSV en la página de análisis de mi Campaign? {#what-is-the-difference-between-the-csv-export-user-data-and-csv-export-email-address-options-on-my-campaign-analytics-page}

Seleccionar la opción **Exportar direcciones de correo electrónico en CSV** descarga datos solo para los usuarios con direcciones de correo electrónico. Por ejemplo, si tienes un Segment de 100,000 usuarios, pero solo 50,000 de esos usuarios tienen direcciones de correo electrónico, y haces clic en **Exportar direcciones de correo electrónico en CSV**, la exportación contiene solo 50,000 filas de datos. En comparación, seleccionar **Exportar datos de usuario en CSV** exporta todos los datos de usuario.

### ¿Puedo buscar una Campaign por su identificador de API? {#can-i-search-for-a-campaign-by-its-api-identifier}

Sí, usa el filtro `api_id:YOUR_API_ID` en la página de **Campaigns** para buscar una Campaign por su identificador de API. Consulta [buscar Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/search_campaigns) para obtener más información.

### ¿Por qué los espacios en blanco aparecen de manera diferente en los campos de entrada frente al texto mostrado? {#why-does-whitespace-appear-differently-in-input-fields-versus-displayed-text}

El manejo de los espacios en blanco difiere entre los campos de entrada y los componentes de texto mostrado debido al estilo CSS. En los componentes de texto con el CSS predeterminado `white-space: normal`, múltiples espacios consecutivos se colapsan en un solo espacio al mostrarse. Este es el comportamiento estándar de HTML para texto renderizado.

Los campos de entrada preservan múltiples espacios exactamente como los ingresas, porque necesitas ver y editar el espaciado exacto para la entrada precisa de datos. Esto significa que el texto con múltiples espacios puede aparecer de manera diferente cuando se ve en un campo de entrada (donde todos los espacios se preservan) versus cuando se muestra en otras partes del panel (donde el CSS puede colapsar múltiples espacios).

Por ejemplo, si ingresas un nombre de Campaign o un parámetro UTM con múltiples espacios en un campo de entrada, ves todos los espacios preservados. Sin embargo, cuando ese mismo texto aparece en resultados de búsqueda, listas de Campaigns u otros componentes de texto, múltiples espacios pueden aparecer como un solo espacio debido al manejo de espacios en blanco del CSS.

### ¿Cuál es la diferencia entre Campaigns de API y Campaigns activadas por API? {#what-is-the-difference-between-api-campaigns-and-api-triggered-campaigns}

Las Campaigns activadas por API te permiten gestionar el texto de la Campaign, las pruebas multivariante y las reglas de reelegibilidad dentro del panel de Braze mientras activas la entrega de ese contenido desde tus propios servidores y sistemas. Estos mensajes también pueden incluir datos adicionales para ser plantillados en los mensajes en tiempo real.

Las Campaigns de API se usan para rastrear los mensajes enviados usando la API. A diferencia de la mayoría de las Campaigns, no especificas el mensaje, los destinatarios ni la programación, sino que pasas los identificadores en tus llamadas de API.

### ¿Cómo puedo confirmar si mis usuarios recibieron una Campaign activada por API? {#how-can-i-confirm-if-my-users-received-an-api-triggered-campaign}

Puedes [crear un Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) usando el filtro **Received Campaign** y luego seleccionar la Campaign activada por API específica que deseas verificar. Después de guardar el Segment, usa el [endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) para exportar los usuarios en ese Segment.

### ¿Puedo eliminar una Campaign? {#can-i-delete-a-campaign}

No, pero puedes [archivar una Campaign]({{site.baseurl}}/user_guide/messaging/governance/archiving).

### ¿Cuál es la diferencia entre las Campaigns basadas en acciones y las activadas por API? {#what-is-the-difference-between-action-based-and-api-triggered-campaigns}

<style>
table th:nth-child(1) {
    width: 50%;
}
table th:nth-child(3) {
    width: 50%;
}
</style>

#### Basadas en acciones {#action-based}

Las Campaigns con entrega basada en acciones o activadas por eventos son muy efectivas para mensajes transaccionales o basados en logros y te permiten activarlas para que se envíen después de que un usuario complete un determinado evento.

| Ventajas | Desventajas |
| ---- | ---- |
| • Visibilidad de las cargas útiles JSON entrantes en la plataforma (si el evento es activado por un usuario de prueba) a través del **Registro de actividad de mensajes**<br><br>• Los elementos de personalización están incluidos en las propiedades del evento personalizado<br><br>• El evento personalizado se puede usar para crear Segments de usuarios elegibles para el mensaje | • Consume puntos de datos |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Basadas en acciones" }

#### Activadas por API {#api-triggered}

Las Campaigns activadas por API y por servidor son ideales para manejar transacciones más avanzadas, lo que te permite activar la entrega del contenido de la Campaign desde tus propios servidores y sistemas. La solicitud de API para activar el mensaje también puede incluir datos adicionales para ser plantillados en el mensaje en tiempo real.

| Beneficios | Consideraciones |
| ---- | ---- |
| • No registra puntos de datos<br><br>• Los elementos de personalización están incluidos en las propiedades de la carga útil JSON | • No te permite crear un Segment de usuarios elegibles para el mensaje en las propiedades de la carga útil JSON<br><br>• No es posible ver las cargas útiles JSON entrantes con el **Registro de actividad de mensajes** |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Activadas por API" }

### ¿Qué debo incluir al enviar un ticket de soporte por un error de "Se agotó el tiempo de espera de la solicitud"? {#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error}

Si encuentras un error de "Se agotó el tiempo de espera de la solicitud" al crear o editar una Campaign o Canvas y necesitas contactar a [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support), incluye la siguiente información para ayudar a acelerar la resolución:

{% multi_lang_include messaging/support_ticket_request_timed_out_details.md context='campaign' %}

### ¿Por qué mis análisis de envío no coinciden con el límite máximo de destinatarios que configuré? {#why-dont-my-send-analytics-match-the-maximum-recipient-limit-i-set}

Si añades o cambias un límite máximo de destinatarios en una Campaign activa, el límite puede no verse reflejado en tus análisis de envío por las siguientes razones:

- **Límite añadido después del lanzamiento:** Si el límite máximo de destinatarios no se establece cuando la Campaign se lanza, los mensajes que ya están en cola antes de aplicar el límite se envían de todas formas. El límite solo surte efecto para los envíos que pones en cola después de guardar el cambio.
- **Interacción con el límite de velocidad:** Si una Campaign también tiene un límite de velocidad, los mensajes pueden distribuirse en una ventana de tiempo más larga. El límite máximo de destinatarios se evalúa cuando los mensajes se ponen en cola, no cuando se entregan. Si el límite se cambia mientras los mensajes ya están en la cola, el límite original se aplica a esos mensajes.
- **Campaigns recurrentes:** Para las Campaigns recurrentes, cada envío programado evalúa el límite máximo de destinatarios de forma independiente. Cambiar el límite entre envíos no ajusta retroactivamente los conteos de envíos anteriores.

Para evitar desajustes, establece el límite máximo de destinatarios antes de lanzar la Campaign y evita modificarlo mientras los envíos están en progreso.

### ¿Por qué los envíos son menores que el tamaño estimado de la audiencia? {#why-are-sends-lower-than-the-estimated-audience-size}

Varios factores pueden hacer que el número de envíos sea menor que el tamaño estimado de la audiencia:

- **Entrega basada en acciones:** Los usuarios solo generan envíos después de realizar el desencadenante, por lo que los envíos se acumulan con el tiempo y pueden quedarse por detrás de la estimación inicial mostrada cuando construiste la Campaign por primera vez.
- **Ediciones de audiencia después del lanzamiento:** Cambiar los filtros de entrada o de segmentación después del lanzamiento puede dejar la instantánea de **Audiencia estimada** fuera de sincronización con quién realmente califica en envíos posteriores (por ejemplo, cuando los usuarios no son elegibles para volver a entrar).
- **Paso de rutas de audiencia:** Para Canvas, un paso de [Rutas de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) solo envía mensajes a los usuarios que coinciden con la rama de mayor prioridad para la que califican, lo que puede reducir los envíos en comparación con un conteo de Segment plano.
- **Grupos de control:** Si un [grupo de control global]({{site.baseurl}}/user_guide/audience/global_control_group) o un grupo de control a nivel de Campaign está en uso, una porción de la audiencia se retiene de la entrega.
- **Tiempo y ventanas de entrega:** Para Campaigns de zona horaria local o programadas, los usuarios deben calificar tanto en el momento de entrada como en el momento de envío; los usuarios en ciertas zonas horarias pueden quedar fuera de la ventana de entrega.
- **Deduplicación de correo electrónico:** Tu Campaign o Canvas segmenta a múltiples usuarios con correos electrónicos coincidentes, por lo que se elige un usuario aleatorio con esa dirección de correo electrónico en el momento del envío. El mensaje se envía solo una vez y se deduplica para que no llegue a la misma dirección de correo electrónico varias veces, pero el tamaño estimado de tu audiencia incluye a todos los usuarios.
- **Filtros de capacidad de entrega de correo electrónico:** Para Campaigns de correo electrónico, Braze excluye a los usuarios que han tenido rebotes permanentes, cancelado su suscripción a correos electrónicos, sido marcados como correo no deseado, no tienen dirección de correo electrónico en su perfil o no están suscritos a un grupo de suscripción requerido. Estas comprobaciones se ejecutan en el momento del envío, por lo que un usuario presente en tu Segment puede ser excluido del conteo real de envíos.
- **Tiempo de importación de CSV:** Cuando la membresía del Segment se mantiene por [importación de CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import), las direcciones de correo electrónico añadidas después de que se envía una Campaign programada no son alcanzadas por ese envío. Dado que Braze no retiene una instantánea de la membresía del Segment en el momento del envío, el tamaño actual del Segment puede exceder el número de usuarios que realmente recibieron el mensaje.
- **Limitación de frecuencia global:** Los topes a nivel de espacio de trabajo pueden evitar que usuarios elegibles reciban otro mensaje en la misma ventana, lo que reduce los envíos realizados.
- **Usuarios recién importados:** Los perfiles que acaban de volverse elegibles pueden no recibir hasta la siguiente evaluación o pasada de envío, así que los conteos se ponen al día en una ejecución posterior.
- **Alcanzabilidad push:** Para Campaigns push, confirma que la audiencia esté habilitada para push en la aplicación correcta. Si no filtras por usuarios habilitados para push, la audiencia estimada puede incluir perfiles que no pueden recibir push. Verifica **Usuarios alcanzables** en el paso **Usuarios objetivo** para una estimación operativa más cercana.
- **Límite de velocidad:** Un [límite de velocidad de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) limita cuántos mensajes envía Braze por minuto durante una sola ocurrencia de envío. Braze distribuye la entrega en una ventana más larga, por lo que algunos envíos pueden aplazarse, no reflejarse aún en el conteo o no completarse si el límite es bajo en relación con la audiencia elegible.
- **Ventanas de reelegibilidad:** Los usuarios que aún no son reelegibles no recibirán de nuevo durante el periodo de espera, por lo que los envíos quedan por debajo del tamaño estimado de la audiencia para ese periodo.
- **Ventana de informes:** El rango de tiempo de análisis puede no incluir todos los envíos.
- **Reevaluación de Segment:** Para Campaigns basadas en acciones o programadas que reevalúan en el momento del envío, los usuarios que estaban en el Segment cuando la Campaign se puso en cola pueden ya no calificar cuando el mensaje se envía realmente.
- **Topes de envío:** Un número máximo de usuarios (o tope similar) en **Públicos objetivo** detiene la entrega cuando se alcanza el tope.
- **Filtros estrictos de dispositivo o navegador:** Los filtros que solo coinciden con las versiones más recientes de la aplicación o navegadores reducen el conjunto alcanzable en el momento del envío en comparación con una vista previa amplia del Segment.

### ¿Dónde están las preguntas frecuentes sobre la limitación de frecuencia global? {#where-are-frequently-asked-questions-about-global-frequency-capping}

Para preguntas sobre días del calendario, push silencioso, webhooks, comportamiento de Canvas y temas relacionados, consulta las [Preguntas frecuentes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/faq) de [Límite de velocidad y limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

### ¿Por qué mi Campaign está experimentando tasas de envío más bajas? {#why-is-my-campaign-experiencing-lower-send-rates}

Si descubres que tus Campaigns programadas diarias envían a menos usuarios con el tiempo, verifica lo siguiente:

- **Comprueba si la reelegibilidad está activada:** Sin reelegibilidad, Braze envía un mensaje a cada usuario solo una vez. En las Campaigns programadas diarias, solo los usuarios que coinciden con la audiencia y que aún no han recibido el mensaje son elegibles para cada envío. A medida que más usuarios reciben el mensaje, cada envío posterior tiene menos usuarios elegibles, por lo que el volumen de envíos disminuye.
- **Comprueba si la audiencia tiene membresía fija:** Las audiencias construidas a partir de una lista fija de usuarios (como una [importación de CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) usada como filtro de Segment) no ganan nuevos miembros automáticamente. Sin nuevos entrantes, el volumen de envíos no puede recuperarse a medida que los usuarios reciben el mensaje.

Para [límites de velocidad de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) y otros factores que reducen los envíos para una sola ocurrencia, consulta [¿Por qué los envíos son menores que el tamaño estimado de la audiencia?](#why-are-sends-lower-than-the-estimated-audience-size).

### ¿Por qué los destinatarios únicos pueden superar los envíos para correo electrónico y servicio de mensajes cortos? {#why-can-unique-recipients-exceed-sends-for-email-and-sms}

Para correo electrónico y servicio de mensajes cortos, Braze incrementa **Destinatarios únicos** antes del intento de envío del ESP e incrementa **Envíos** después de una respuesta exitosa del ESP. Los errores permanentes (como direcciones de correo electrónico inválidas) o direcciones duplicadas hacen que los destinatarios únicos superen los envíos.

### ¿Por qué **Último envío** no coincide con mi hora de envío programada? {#why-doesnt-last-sent-match-my-scheduled-send-time}

Para una Campaign con un solo envío programado, **Último envío** coincide con la hora de lanzamiento. Para Campaigns recurrentes con **Enviar en zona horaria local** habilitado, **Último envío** puede aparecer antes de la hora programada porque los envíos a usuarios en zonas horarias más tempranas (por ejemplo, GMT frente a PST) se completan antes de la hora de programación de tu espacio de trabajo.

### ¿Por qué una Campaign histórica detenida ya no muestra métricas en la página de **Analytics**? {#why-does-a-stopped-historical-campaign-no-longer-show-metrics-on-the-analytics-page}

La pestaña **Analytics** muestra de forma predeterminada los últimos 90 días. Si la Campaign envió por última vez fuera de esa ventana, las métricas pueden aparecer como cero hasta que ajustes el rango de fechas en la página de **Analytics** para incluir cuándo se envió la Campaign. Para más información, consulta [Análisis de Campaigns]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics).

**Restaurar datos de interacción** no restaura los análisis de la Campaign. Solo se aplica a los filtros de retargeting y al historial de interacción de usuarios. Para más información, consulta [Datos de interacción de mensajería]({{site.baseurl}}/messaging_interaction_data).