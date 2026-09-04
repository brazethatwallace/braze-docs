---
nav_title: Calentamiento de IP automatizado
article_title: Calentamiento de IP automatizado
page_order: 1
page_type: reference
description: "Este artículo de referencia trata sobre el calentamiento de IP automatizado y cómo supervisar tu calentamiento de IP."
channel: email
---

# Calentamiento de IP automatizado {#automated-ip-warming}

> Utiliza el calentamiento de IP automatizado para aumentar gradualmente el volumen de correos electrónicos desde nuevas IP dedicadas y construir la reputación del remitente ante los proveedores de buzón de entrada. Para preguntas frecuentes, consulta las [Preguntas frecuentes sobre el calentamiento de IP automatizado]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/faq).

## Cómo funciona {#how-it-works}

Puedes usar el calentamiento de IP automatizado para aumentar gradualmente tu volumen de envío diario, permitiendo que los proveedores de buzón de entrada aprendan y confíen en tus patrones de envío. Cuando agregas un dominio a tu espacio de trabajo, puedes seleccionar el mosaico **Automated IP Warming** en la sección **Pick up where you left off** del panel de inicio. Este mosaico permanece durante 60 días mientras tu espacio de trabajo se encuentra en el período de incorporación de nuevo remitente, y se oculta después de completar al menos un plan.

Cada plan de calentamiento de IP automatizado está vinculado a una dirección de remitente. Esa dirección de remitente se asigna a un subdominio de envío y un grupo de IP. Si el grupo contiene múltiples IP dedicadas, Braze las calienta juntas en un solo plan.

Braze envía primero a tus suscriptores con mayor participación, lo que permite que el volumen diario crezca a un ritmo que coincide con las mejores prácticas. Luego, Braze rastrea las señales de participación y capacidad de entrega. Si Braze detecta algún problema, el sistema ajusta tu programa automáticamente.

Después de completar al menos un plan, puedes ver los planes completados en **Settings** > **Email Preferences** > **Automated IP warming**.

## Requisitos previos {#prerequisites}

Para realizar un calentamiento de IP automatizado, debes contar con lo siguiente:

- Subdominio verificado y direcciones IP activas
- Permisos para ver y configurar un plan:
    - "View Email Settings" para ver los planes de calentamiento de IP y el widget del panel de inicio
    - "View Email Templates" para seleccionar plantillas de correo electrónico
    - "View Segments" para seleccionar Segments
- Permisos para lanzar un plan:
    - "Edit Email Settings"
    - "Edit Campaigns"
    - "Launch Campaigns"
    - "Approve Campaigns"

{% alert note %}
Si el flujo de trabajo de aprobación de campañas está activado, Braze aprueba automáticamente en tu nombre las campañas creadas por el calentamiento de IP automatizado.
{% endalert %}

## Configura un plan automatizado de calentamiento de IP {#set-up-an-automated-ip-warming-plan}

### Paso 1: Establece un calendario {#step-1-set-a-schedule}

1. Introduce un **Nombre de plan** único. Los nombres de plan solo pueden contener letras, números, guiones y guiones bajos, y deben ser únicos en tu espacio de trabajo. Es necesario un nombre de plan antes de poder lanzarlo.
2. En la sección **Información de envío**, selecciona la **Dirección de remitente** para calentar las direcciones IP. Braze muestra el **Grupo de IP** asociado y el número de **Direcciones IP en el grupo** para esa dirección de remitente.
3. Introduce el **Volumen de envío diario actual** y el **Volumen de envío objetivo**. Braze sugiere un volumen de envío objetivo de hasta 2 millones de envíos por IP en el grupo seleccionado. Si tu volumen de envío diario actual es 0, el primer día de tu calendario comienza con hasta 50 envíos por IP, con un tope de 500 en total.
4. Selecciona la fecha de inicio para el calentamiento de IP automatizado. Esta fecha debe ser al menos un día después de que se lance el plan.
5. Introduce la hora de envío. Esto envía los mensajes en la zona horaria del espacio de trabajo (o la zona horaria de la empresa si el espacio de trabajo no tiene una configuración personalizada).
6. Selecciona **Siguiente: Segments** para continuar con la configuración.

![Ejemplo de detalles del calendario.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### Paso 2: Selecciona y clasifica los segmentos {#step-2-select-and-rank-segments}

1. A continuación, selecciona los segmentos a los que dirigirte. Durante el calentamiento de IP, Braze comienza enviando a tus usuarios con mayor participación y aumenta gradualmente el volumen de envío con el tiempo, incorporando lentamente segmentos con menor participación.
2. Luego, arrastra y suelta los segmentos para clasificarlos de mayor a menor participación. Alta participación incluye destinatarios que abren y hacen clic en tus correos electrónicos de forma constante. Baja participación incluye destinatarios que son inconsistentes en su interacción con tus correos electrónicos o que no han interactuado con ellos en mucho tiempo.
3. Selecciona **Siguiente: Mensajes** para continuar con la configuración.

{% alert important %}
Asegúrate de que el número total de usuarios con correo electrónico habilitado en todos los segmentos seleccionados sea mayor o igual a tu **Volumen de envío objetivo**. Cuando tu audiencia es menor que tu volumen objetivo, algunos usuarios reciben más de una plantilla de correo electrónico el mismo día. Para más información, consulta [Tamaño de la audiencia y múltiples envíos por usuario](#audience-size-and-multiple-sends-per-user).
{% endalert %}

![Dos segmentos seleccionados como objetivo para el calentamiento de IP automatizado.]({% image_buster /assets/img/automated_ip_warming_segment.png %})

### Paso 3: Selecciona los mensajes a enviar {#step-3-select-the-messages-to-send}

1. Selecciona **Seleccionar plantillas de correo electrónico**.
2. Elige las plantillas de correo electrónico para los mensajes a enviar. El contenido que envíes durante el calentamiento de IP debe fomentar las aperturas y los clics. Recomendamos elegir contenido que haya tenido buena recepción en el pasado. Por ejemplo, puedes usar ofertas promocionales para fomentar la participación inmediata y las compras.
3. Selecciona **Seleccionar plantillas**. Braze calcula el número de plantillas necesarias antes de que puedas lanzar. Recomendamos proporcionar más plantillas que el mínimo requerido para permitir que el sistema se ajuste ante problemas de capacidad de entrega sin detenerse.
4. Después de agregar el número requerido de plantillas, selecciona **Siguiente: Resumen**.

{% alert important %}
Los cambios realizados en las Campaigns creadas desde la herramienta de calentamiento de IP (como cambiar la fecha programada, el segmento o el volumen) no se reflejan en la página de **Resumen** del calentamiento de IP.
{% endalert %}

### Paso 4: Selecciona los eventos de conversión {#step-4-select-conversion-events}

Puedes definir hasta cuatro de los siguientes eventos de conversión para realizar un seguimiento. Estos eventos de conversión no se pueden actualizar después de que se haya lanzado el plan automatizado de calentamiento de IP.

- Inicia sesión
- Realiza un pedido
- Realiza un evento personalizado
- Actualiza la aplicación
- Abre un correo electrónico
- Hace clic en un correo electrónico

A continuación, selecciona el plazo de conversión, que es el tiempo máximo que puede transcurrir entre que un usuario entra en una Campaign y el evento de conversión.

![Configuración de conversiones que muestra la selección de eventos de conversión y el plazo de conversión.]({% image_buster /assets/img/automated_ip_warming_conversions.png %})

### Paso 5: Revisa y lanza {#step-5-review-and-launch}

Revisa los detalles de tu plan de calentamiento de IP. Luego, selecciona **Lanzar**.

## Calentamiento de IP múltiples {#multiple-ip-warming}

Usa múltiples planes de calentamiento de IP automatizado cuando necesites calentar más de una dirección de remitente o grupo de IP.

| Escenario | Recomendación |
| --- | --- |
| Múltiples IP dedicadas en un grupo de IP | Crea un plan y selecciona la dirección de remitente para ese grupo |
| Múltiples grupos de IP o direcciones de remitente | Crea un plan separado para cada dirección de remitente |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Escenarios de calentamiento de IP múltiples" }

### Calentar múltiples IP en un grupo {#warm-multiple-ips-in-one-pool}

Cuando seleccionas una dirección de remitente en el [Paso 1: Establecer un calendario](#step-1-set-a-schedule), Braze muestra el grupo de IP asociado y las direcciones IP en el grupo. Braze utiliza el número de IP cuando construye tu calendario de incremento y sugiere tu volumen de envío objetivo.

Si tu **Volumen de envío diario actual** es 0, el primer día programado comienza con hasta 50 envíos por IP en el grupo, con un máximo de 500 en total. Braze sugiere un **Volumen de envío objetivo** de hasta 2 millones de envíos por IP en el grupo.

### Calentar múltiples grupos de IP {#warm-multiple-ip-pools}

Para calentar más de una dirección de remitente o grupo de IP:

1. Ve a **Configuración** > **Preferencias de correo electrónico** > **Calentamiento de IP automatizado**.
2. Selecciona **Nuevo plan de calentamiento de IP**.
3. Ingresa un **Nombre de plan** único.
4. Completa la configuración para esa dirección de remitente.
5. Repite para cada dirección de remitente o grupo de IP adicional que necesites calentar.

Haz seguimiento de cada plan desde la tabla de **Calentamiento de IP automatizado**. Cada plan tiene su propio calendario, Segments, plantillas, Campaigns y rastreador. Los planes pueden estar en estado **Borrador**, **En progreso**, **Completado** o **Detenido**.

{% alert important %}
Evita enviar Campaigns grandes que no sean de calentamiento desde la misma dirección de remitente o grupo de IP mientras un plan de calentamiento de IP automatizado esté activo. Los envíos adicionales durante el calentamiento pueden afectar las señales de capacidad de entrega y dificultar el aislamiento de problemas.
{% endalert %}

## Durante el calentamiento de IP activo {#during-active-ip-warming}

Las campañas de calentamiento de IP se crean a medianoche en la zona horaria efectiva para el día actual y el día siguiente (de 0 a 1 días antes del envío). Al lanzar un plan también se crean las próximas campañas de inmediato. Estas campañas se nombran automáticamente con el siguiente formato: `IP Warming Day [X] - [Date] - [Template Name]`.

Cuando se alcanza el objetivo diario de envío, el sistema deja de enviar ese día para proteger tu reputación.

Braze evalúa la capacidad de entrega de las campañas enviadas entre 12 y 20 horas antes. Si se supera alguno de los siguientes umbrales, Braze mantiene el volumen para el siguiente día de envío en lugar de aumentarlo:

- Tasa de entrega inferior al 90 %
- Tarifa abierta inferior al 10 %
- Tasa de rebote superior al 5 %
- Tasa de quejas por correo no deseado superior al 0,04 %

Para saber qué sucede cuando se mantiene el volumen, consulta [¿Qué sucede cuando se mantiene el volumen?]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/faq#what-happens-when-volume-is-held).

## Tamaño de la audiencia y múltiples envíos por usuario {#audience-size-and-multiple-sends-per-user}

Para alcanzar el objetivo de envío de cada día, Braze recorre las plantillas de correo electrónico que seleccionaste. Dentro de un plan, Braze excluye a los usuarios que ya recibieron una plantilla determinada, pero los usuarios que recibieron una plantilla diferente siguen siendo elegibles. Cuando se agota la audiencia disponible para el calendario de ese día, el plan vuelve a recorrer tus plantillas, por lo que algunos usuarios reciben una segunda plantilla el mismo día.

Si el número total de usuarios a los que se puede enviar correo electrónico en los Segments seleccionados es menor que tu **Volumen de envío objetivo**, este resultado es inevitable en el último día o días del plan, cuando el volumen diario está en su punto más alto. Por ejemplo, si tus Segments contienen 400,000 usuarios a los que se puede enviar correo electrónico y tu volumen de envío objetivo es de 600,000, aproximadamente 200,000 usuarios reciben dos plantillas el último día y los 200,000 usuarios restantes reciben una.

Los usuarios también pueden recibir diferentes plantillas en diferentes días, incluso cuando tu audiencia es mayor que tu volumen de envío objetivo. Debido a que Braze divide la audiencia de cada día entre tus plantillas sin tener en cuenta qué plantilla recibió un usuario previamente, un usuario que recibió una plantilla puede ser seleccionado para una plantilla diferente más adelante en el plan.

Braze no te impide lanzar un plan cuando tu volumen de envío objetivo es mayor que tu audiencia disponible. Para limitar a cada usuario a una plantilla por día de envío, haz una de las siguientes acciones antes de lanzar:

- Agrega Segments de modo que el número total de usuarios a los que se puede enviar correo electrónico sea mayor o igual a tu volumen de envío objetivo.
- Reduce tu **Volumen de envío objetivo** para que no sea mayor que tu número total de usuarios a los que se puede enviar correo electrónico.

## Detener un plan de calentamiento de IP {#stop-an-ip-warmup-plan}

Puedes detener un plan de calentamiento de IP para evitar la creación de futuras campañas. Detener un plan también desactiva todas las campañas asociadas. Después de detener un plan, no puedes reanudarlo. Configura un nuevo plan para retomar donde lo dejaste:

- Descarga los datos existentes de tu plan detenido para conservarlos en tus registros
- Actualiza el **Volumen de envío diario actual** al volumen más reciente
- Agrega un filtro a un Segment si planeas usar el mismo Segment del último calentamiento de IP excluyendo a los usuarios que ya recibieron campañas anteriores

## Cuándo se completa un calentamiento de IP {#when-an-ip-warming-completes}

El calentamiento de IP se marca como completado cuando el último día del calentamiento de IP finaliza a medianoche en la zona horaria de tu espacio de trabajo (o la zona horaria de la empresa si el espacio de trabajo no tiene una anulación). Por ejemplo, si la última Campaign del plan se envía a las 8 pm, el plan se marca como completado a medianoche, cuatro horas después.

Los planes completados permanecen disponibles en **Configuración** > **Preferencias de correo electrónico** > **Calentamiento de IP automatizado**. El rastreador también permanece en el panel de inicio durante 90 días después de que finaliza el plan. Después de 90 días, el rastreador del panel de inicio se elimina.

La descarga de datos incluye estas métricas estándar de correo electrónico:

- _Enviados_
- _Entregados_
- _Rebotes_
- _Informes de correos no deseados_
- _Aperturas totales_
- _Unique Opens_
- _Clics_
- _Cancelaciones de suscripción_

Si un día incluye múltiples Campaigns utilizadas para cumplir con los requisitos de volumen, estas se agregan en la vista diaria.

![Rastreador de calentamiento de IP con volumen de envío para la semana del 16 de enero.]({% image_buster /assets/img/automated_ip_warming_example.png %})