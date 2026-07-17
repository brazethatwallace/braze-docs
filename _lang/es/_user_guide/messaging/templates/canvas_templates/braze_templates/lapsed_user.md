---
nav_title: Usuario inactivo
article_title: Usuario inactivo
page_order: 4
page_type: reference
description: "Este artículo describe cómo usar una plantilla de Braze Canvas para traer de vuelta a los usuarios a tu aplicación con incentivos basados en sus interacciones pasadas."
tool: Canvas
---

# Usuario inactivo {#lapsed-user}

> Usa la plantilla de usuario inactivo para recordar a los usuarios el valor que tu marca les aporta, y fomenta su regreso con ofertas emocionantes e incentivos basados en sus interacciones pasadas.

Este artículo te guiará a través de un caso de uso de la plantilla **Usuario inactivo**, diseñada para la etapa de retención y fidelización del ciclo de vida del usuario. Cuando termines, habrás creado un Canvas que anima a los usuarios a volver a tu aplicación con promociones que varían según su comportamiento, como si iniciaron una sesión en tu aplicación después de recibir un mensaje promocional.

## Requisitos previos {#prerequisites}

Para usar con éxito la plantilla de usuario inactivo, necesitas configurar [Braze Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync) con los partners y audiencias que utilizas.

## Adaptar la plantilla a tus necesidades {#tailoring-the-template-to-your-needs}

Imagina que trabajas para MovieCanon, un servicio de streaming con contenido exclusivo de películas y series. Puedes usar la plantilla de usuario inactivo para promocionar ventajas y contenido premium para usuarios que no han visitado tu aplicación en 30 días.

Antes de crear el Canvas, configura la integración de [Braze Audience Sync con Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync) para poder añadir datos de usuario de Braze a Google Audiences y enviar anuncios basados en desencadenantes de comportamiento, segmentación y más.

Para acceder a la plantilla de usuario inactivo, al crear un nuevo Canvas, selecciona **Use a Canvas template** > **Braze templates**. Luego, junto a **Lapsing User**, selecciona **Apply Template**. Ahora puedes revisar la plantilla para adaptarla a tus necesidades.

### Paso 1: Configura los detalles {#step-1-set-up-the-details}

Ajusta los detalles del Canvas para reflejar tu objetivo.

1. Selecciona **Edit** junto al nombre de la plantilla.

{:start="2"}
2. Actualiza el nombre del Canvas para especificar que este Canvas envía mensajes a los usuarios con promociones y realiza una sincronización de audiencia para aquellos que inicien una sesión.
3. Actualiza la descripción para explicar que este Canvas contiene ventajas y promociones.
4. Añade la etiqueta **Lapsing/Retention** para poder filtrar este Canvas en la página de inicio de Canvas.

### Paso 2: Asigna tus eventos de conversión {#step-2-assign-your-conversion-events}

Actualiza **Primary Conversion Event - A** para dirigirte a los usuarios de tu aplicación (MovieCanon), y deja **Primary Conversion Event - B** con el valor predeterminado de realizar cualquier compra.

### Paso 3: Adapta el horario de entrada {#step-3-tailor-the-entry-schedule}

Mantén el horario de entrada como **Scheduled** y las opciones predeterminadas basadas en tiempo, para que el Canvas busque usuarios inactivos diariamente.

Realiza dos ajustes en este paso:

1. Selecciona una fecha y hora de inicio.
2. Selecciona los parámetros de finalización de **On a specific date** y una fecha dos meses en el futuro. En este ejemplo, hay otro Canvas de usuario inactivo que comienza después de que este termine.

### Paso 4: Selecciona tu público objetivo {#step-4-select-your-target-audience}

Mantén la configuración predeterminada para el público de entrada, que se dirige a usuarios que no han usado tu aplicación en más de 30 días. También mantén los controles de entrada predeterminados para que los usuarios puedan volver a entrar en el Canvas después de cuatro semanas. Esto significa que cada vez que un usuario no visite tu aplicación durante más de 30 días seguidos, entrará en el Canvas.

### Paso 5: Selecciona tus ajustes de envío {#step-5-select-your-send-settings}

Mantén la mayoría de los ajustes de suscripción predeterminados:

- Enviar solo a usuarios que se hayan suscrito u optado por recibir mensajes o notificaciones.
- Aplica tus [reglas de limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping) para no abrumar a tu audiencia con la cantidad de mensajes que reciben. En este caso, configura tu limitación de frecuencia para limitar el número de campañas o pasos en Canvas etiquetados con "Lapsing/Retention" que un usuario puede recibir a dos por semana.
- No enviar mensajes durante las horas tranquilas en la hora local del usuario (de 12 am a 8 am).

El único ajuste que debes cambiar es qué sucede cuando un mensaje se desencadena durante las horas tranquilas. En lugar de cancelar el mensaje, selecciona **Send at next available time** para que tus usuarios no se pierdan ninguna promoción.

### Paso 6: Personaliza tu Canvas {#step-6-customize-your-canvas}

Ahora construye tu Canvas personalizando los pasos de la plantilla:

1. Personaliza el primer correo electrónico que se envía a todos los usuarios que no han visitado tu aplicación en más de 30 días. En este caso de uso, personaliza un correo electrónico que les diga a los usuarios que desbloquean nuevas ventajas cuando visiten tu aplicación hoy.

{: start="2"}
2. Personaliza el componente de ruta de acción llamado "Start Session?" seleccionando tu aplicación para la ruta **Started Session**.

{: start="3"}
3. Mantén el valor predeterminado para el paso de división de decisiones llamado "Sessions?", que define el grupo ">1 Session" como usuarios que han usado tu aplicación más de una vez en el último día del calendario.
4. Personaliza el paso de mensaje para los usuarios que caen en el grupo ">1 Session". En este caso de uso, agradece a los usuarios por visitar tu aplicación y destaca las ventajas que han desbloqueado.
5. Asegúrate de que tu sincronización con Google Audience esté configurada en el paso de actualización de audiencia de anuncios, para que actualices y sincronices los datos de usuario de los usuarios que tuvieron múltiples sesiones después de recibir el primer correo electrónico.
6. Mantén el valor predeterminado para el componente de [recorrido de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#experiment-paths) llamado "A/B Test". Esto envía aleatoriamente una de dos promociones (que personalizas en el siguiente paso) a los usuarios que hayan tenido menos de dos sesiones.
7. Personaliza las dos promociones que se envían a los usuarios como parte del recorrido de experimentos. En este caso de uso, haz que una sea una promoción del 20 % para una suscripción de tres meses y la otra una promoción del 10 % para una suscripción de un mes.

![Pasos en Canvas con rutas ramificadas basadas en cuántas sesiones tuvo un usuario.]({% image_buster /assets/img/canvas_templates/lapsing_user_8.png %}){: style="max-width:70%;"}

### Paso 7: Prueba y lanza el Canvas {#step-7-test-and-launch-the-canvas}

Después de probar y revisar tu Canvas para asegurarte de que funciona como se espera, lánzalo seleccionando **Launch Canvas**. ¡Los usuarios que no han visitado tu aplicación en más de 30 días y se han suscrito a tus canales de mensajería ahora recibirán correos electrónicos animándolos a volver!

{% alert tip %}
Consulta nuestra [lista de verificación previa y posterior al lanzamiento]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#things-to-consider-before-launch) para conocer las cosas a considerar antes y después de lanzar un Canvas.
{% endalert %}