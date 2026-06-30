---
nav_title: Registro de correo electrónico con doble adhesión voluntaria
article_title: Registro de correo electrónico con doble adhesión voluntaria
page_order: 2
page_type: reference
description: "Este artículo describe cómo usar una plantilla de Braze Canvas para ampliar tu alcance con registros de correo electrónico verificados."
tool: Canvas
---

# Registro de correo electrónico con doble adhesión voluntaria {#email-sign-up-with-double-opt-in}

> Usa la plantilla de registro de correo electrónico con doble adhesión voluntaria para ampliar tu alcance con registros de correo electrónico verificados. Dirígete a nuevos usuarios para capturar su correo electrónico, confirmar su suscripción y recibir un código promocional, todo en un recorrido fluido.

Este artículo te guiará a través de un caso de uso de la plantilla **Registro de correo electrónico con doble adhesión voluntaria**, diseñada para la etapa de consideración del ciclo de vida del usuario. Cuando termines, habrás creado un Canvas que envía correos electrónicos y mensajes dentro de la aplicación a los usuarios cuando inician una sesión o cuando no han completado su incorporación.

## Requisitos previos {#prerequisites}

Para usar esta plantilla con éxito, necesitas lo siguiente:

- Un [mensaje dentro de la aplicación de varias páginas]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop#multi-page) con una página para capturar los correos electrónicos de tus usuarios y otra para comunicar un mensaje de éxito.
- Un correo electrónico de confirmación para que los usuarios verifiquen su dirección de correo electrónico.
- Un correo electrónico de bienvenida con un código promocional exclusivo para los usuarios que completen la doble adhesión voluntaria.

## Adaptar la plantilla a tus necesidades {#tailoring-the-template-to-your-needs}

Supongamos que trabajas para Steppington, una aplicación de salud conocida por sus características como el seguimiento de calorías, clases de ejercicio digitales y maratones flash mob. Antes de crear el Canvas, [configuras mensajes dentro de la aplicación y en el explorador de varias páginas]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop#multi-page) que incluyen una serie de preguntas atractivas para determinar la experiencia e impresión de la primera interacción de un usuario con la aplicación.

Para acceder a la plantilla, al crear un nuevo Canvas, selecciona **Use a Canvas template** > **Braze templates**. Luego, junto a **Email sign-up with double opt-in**, selecciona **Apply Template**. Ahora podemos recorrer la plantilla para adaptarla a nuestras necesidades.

### Paso 1: Configurar los detalles {#step-1-set-up-the-details}

Ajusta los detalles del Canvas para reflejar tu objetivo.

1. Selecciona **Edit** junto al nombre de la plantilla.

![El título y la descripción actuales del Canvas.]({% image_buster /assets/img/canvas_templates/email_signup1.png %}){: style="max-width:50%;"}

{:start="2"}
2. Actualiza el nombre del Canvas para especificar que está dirigido a nuevos usuarios cuando usan la aplicación por primera vez.
3. Actualiza la descripción para explicar que este Canvas contiene mensajería personalizada para que los usuarios completen la doble adhesión voluntaria.
4. Añade la etiqueta **Email** para poder filtrarlo en la página de inicio de Canvas.

![El nuevo nombre, descripción y etiqueta del Canvas.]({% image_buster /assets/img/canvas_templates/email_signup2.png %}){: style="max-width:90%;"}

### Paso 2: Asignar eventos de conversión {#step-2-assign-conversion-events}

A continuación, asigna los eventos de conversión. Los eventos de conversión son un tipo de métrica que puedes usar para medir el éxito del Canvas. Para **Conversion event type**, selecciona **Performs Custom Event**. Luego, selecciona **email_opt_in** para el **Custom event name**.

![Sección "Assign Conversion Events" para el tipo de evento de conversión de adhesión voluntaria al correo electrónico.]({% image_buster /assets/img/canvas_templates/email_signup3.png %}){: style="max-width:90%;"}

Mantén la fecha límite de conversión de la plantilla de tres días, ya que quieres dirigirte a tus usuarios más recientes.

### Paso 3: Adaptar el horario de entrada {#step-3-tailor-the-entry-schedule}

Mantén el horario de entrada como **Action-Based** para que los usuarios entren en tu Canvas cuando inicien una sesión en la aplicación. De esta manera, puedes comenzar a construir tu relación con una interacción oportuna.

Además, considera mantener las **Action Based Options** tal como están para que los usuarios entren en el Canvas solo cuando inicien una sesión.

![Un horario de entrada basado en acciones para que los usuarios que inicien cualquier sesión entren en el Canvas.]({% image_buster /assets/img/canvas_templates/email_signup4.png %}){: style="max-width:90%;"}

Para la **Entry Window**, actualiza la **Started Time (Required)** a la fecha y hora deseadas.

![Una ventana de entrada con la hora de inicio 16 de enero de 2025 a las 12:30 pm. Los usuarios entrarán en este mensaje en su zona horaria local.]({% image_buster /assets/img/canvas_templates/email_signup5.png %}){: style="max-width:90%;"}

### Paso 4: Seleccionar la audiencia objetivo {#step-4-select-the-target-audience}

Define tu audiencia objetivo como usuarios de Steppington que no tienen una dirección de correo electrónico en su perfil de usuario manteniendo el [filtro de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) predeterminado de la plantilla `Email Available is false`.

![Audiencia de entrada con el filtro "Email Available is false".]({% image_buster /assets/img/canvas_templates/email_signup6.png %}){: style="max-width:90%;"}

### Paso 5: Seleccionar los ajustes de envío {#step-5-select-your-send-settings}

Mantén los ajustes de suscripción predeterminados para enviar solo a usuarios que se hayan suscrito o hayan optado por recibir mensajes o notificaciones, y omite los demás ajustes (limitación de frecuencia, horas tranquilas y grupos semilla).

![Opciones de envío predeterminadas para enviar solo a usuarios que estén suscritos o hayan optado por recibir.]({% image_buster /assets/img/canvas_templates/email_signup7.png %}){: style="max-width:90%;"}

### Paso 6: Personalizar tu Canvas {#step-6-customize-your-canvas}

A continuación, construye el Canvas personalizando los canales y el contenido que quieres enviar a los usuarios. Como te estás enfocando en verificar los registros de correo electrónico, no necesitas añadir ni eliminar ninguno de los pasos en Canvas ni canales de la plantilla.

1. Selecciona el primer paso de mensaje llamado **Email Sign-up**. Aquí es donde actualizas la plantilla para usar nuestro mensaje dentro de la aplicación (y en el explorador) de varias páginas.

- La página 1 captura los correos electrónicos.
- La página 2 muestra un mensaje de confirmación.

![Dos páginas de un mensaje dentro de la aplicación para capturar correos electrónicos de usuarios y mostrar un mensaje de éxito.]({% image_buster /assets/img/canvas_templates/email_signup8.png %}){: style="max-width:90%;"}

{:start="2"}
2. Desde aquí, mantén el paso de ruta de acción **Subscribed** tal como está. Este paso divide a nuestros usuarios en dos grupos en una ventana de un día:

- Usuarios que se han suscrito a Steppington con su correo electrónico
- Usuarios que no se han suscrito a Steppington con su correo electrónico

{:start="3"}
3. A continuación, reemplaza el cuerpo del correo electrónico con nuestro correo electrónico de confirmación de marca para el paso de mensaje **Verify Email**. Esto enviará un correo electrónico a nuestros usuarios suscritos y les pedirá que confirmen su dirección de correo electrónico y opten por recibir nuestra mensajería.
4. Mantén el paso de ruta de acción **Confirm Subscription** tal como está. Este paso divide aún más a nuestros usuarios entre aquellos que han confirmado su correo electrónico y aquellos que no, con una ventana de una semana.
5. Por último, actualiza el paso de mensaje **Welcome + Discount** con nuestro correo electrónico de confirmación que incluye un código promocional exclusivo.

{% alert note %}
El paso de mensaje **Verify Email** se desencadena en la segunda sesión del usuario. Esto se debe a que el primer evento de inicio de sesión desencadenaría el Canvas, pero se requiere un segundo inicio de sesión después de que el usuario haya alcanzado el primer paso de mensaje **Email Sign-up** para que el usuario sea elegible para desencadenar el segundo mensaje dentro de la aplicación.
{% endalert %}

### Paso 7: Probar y lanzar tu Canvas {#step-7-test-and-launch-your-canvas}

Después de probar y revisar tu Canvas para asegurarte de que funciona como se espera, lánzalo seleccionando **Launch Canvas**.

{% alert tip %}
Consulta nuestra [lista de verificación previa y posterior al lanzamiento]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#things-to-consider-before-launch) para conocer las cosas a considerar antes y después de lanzar un Canvas.
{% endalert %}