---
nav_title: Incorporación con cuestionario de preferencias
article_title: Incorporación con cuestionario de preferencias
page_order: 5.5
page_type: reference
description: "Este artículo describe cómo usar una plantilla de Canvas de Braze para impulsar la adopción temprana con un flujo de incorporación guiado que presenta tu marca a los nuevos usuarios y recopila sus preferencias para mantenerlos comprometidos a largo plazo."
tool: Canvas
---

# Incorporación con cuestionario de preferencias {#onboarding-with-preferences-survey}

> Usa la plantilla de incorporación con cuestionario de preferencias para crear un flujo de trabajo de incorporación guiado dirigido a nuevos usuarios. Preséntalos a tu marca, ayúdalos a empezar y recopila sus preferencias para mantenerlos comprometidos a largo plazo.

Este artículo te guiará a través de un caso de uso de la plantilla **Onboarding with preferences survey**, diseñada para la etapa de consideración del ciclo de vida del usuario. Cuando termines, habrás creado un Canvas que envía correos electrónicos y mensajes dentro de la aplicación a los usuarios cuando inician una sesión y cuando no han completado su incorporación.

## Requisitos previos {#prerequisites}

Para usar esta plantilla con éxito, necesitarás lo siguiente:

- Un correo electrónico de bienvenida que invite a los usuarios a comenzar la incorporación.
- Un correo electrónico de seguimiento que incluya consejos para empezar a usar la aplicación para los usuarios que completaron la incorporación.
- Un correo electrónico de seguimiento para invitar a los usuarios a completar su incorporación.
- Un [cuestionario]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/simple_survey/) con múltiples preguntas para determinar las preferencias de los usuarios.

## Adaptar la plantilla a tus necesidades {#tailoring-the-template-to-your-needs}

Supongamos que trabajamos para StyleRyde, una aplicación de transporte compartido bajo demanda que lleva a las personas a donde necesitan ir. Antes de crear el Canvas, [configuramos un cuestionario sencillo]({{site.baseurl}}/user_guide/data/activation/catalogs/create/) que incluye una serie de preguntas atractivas para determinar la experiencia e impresión del primer viaje de un usuario con la aplicación.

Para acceder a la plantilla, al crear un nuevo Canvas, selecciona **Use a Canvas template** > **Braze templates**. Luego, junto a **Onboarding with preferences survey**, selecciona **Apply Template**. Ahora podemos revisar la plantilla para adaptarla a nuestras necesidades.

### Paso 1: Configurar los detalles {#step-1-set-up-the-details}

Ajustemos los detalles del Canvas para reflejar nuestro objetivo.

1. Selecciona **Edit** junto al nombre de la plantilla.

![El título y la descripción actuales del Canvas.]({% image_buster /assets/img/canvas_templates/preference_survey1.png %}){: style="max-width:50%;"}

{:start="2"}
2. Actualiza el nombre del Canvas para especificar que está dirigido a nuevos usuarios cuando usan la aplicación por primera vez.
3. Actualiza la descripción para explicar que este Canvas contiene mensajería personalizada.
4. Añade la etiqueta **Onboarding** para poder filtrarlo en la página de inicio de Canvas.

![El nuevo nombre, descripción y etiqueta del Canvas.]({% image_buster /assets/img/canvas_templates/preference_survey2.png %}){: style="max-width:90%;"}

### Paso 2: Asignar eventos de conversión {#step-2-assign-conversion-events}

Actualiza el **Primary Conversion Event - A** a **Performs Custom Event**. Luego, selecciona **Last Used App** como el evento personalizado.

![Last Used App como el nombre del evento personalizado seleccionado para el evento de conversión.]({% image_buster /assets/img/canvas_templates/preference_survey3.png %}){: style="max-width:90%;"}

### Paso 3: Adaptar el horario de entrada {#step-3-tailor-the-entry-schedule}

Mantengamos el horario de entrada como **Action-Based** para que los usuarios entren a nuestro Canvas cuando inicien una sesión en la aplicación. De esta manera, podemos comenzar a construir nuestra relación con una interacción oportuna.

Haremos una actualización en esta sección ajustando la **Entry Window** a la fecha y hora deseadas.

![Sección "Entry Window" con la hora de inicio el 30 de enero de 2025 a las 12 pm.]({% image_buster /assets/img/canvas_templates/preference_survey4.png %}){: style="max-width:90%;"}

### Paso 4: Seleccionar la audiencia objetivo {#step-4-select-the-target-audience}

Mantendremos la audiencia objetivo tal como está para dirigirnos a los usuarios que usaron la aplicación StyleRyde por primera vez hace menos de un día.

![El filtro "First used these apps less than 1 days ago" seleccionado para dirigirse a la audiencia de entrada.]({% image_buster /assets/img/canvas_templates/preference_survey5.png %}){: style="max-width:90%;"}

### Paso 5: Seleccionar los ajustes de envío {#step-5-select-your-send-settings}

Mantendremos la configuración de suscripción predeterminada, de modo que solo enviemos a los usuarios que se han suscrito u optado por recibir mensajes o notificaciones con las horas tranquilas activadas, y omitiremos los demás ajustes (limitación de frecuencia y grupos semilla).

![Sección "Send Settings" con la configuración de suscripción para usuarios suscritos u optados con horas tranquilas activadas entre las 12 am y las 8 pm.]({% image_buster /assets/img/canvas_templates/preference_survey6.png %}){: style="max-width:90%;"}

### Paso 6: Personalizar tu Canvas {#step-6-customize-your-canvas}

Ahora construiremos nuestro Canvas personalizando el contenido que se enviará a los usuarios.

1. Para el primer paso de mensaje **Welcome Email**, actualizaremos este paso para incluir nuestro correo electrónico de bienvenida de StyleRyde.
2. A continuación, mantendremos el paso de ruta de acción tal como está. Este paso divide a nuestros usuarios en dos grupos en una ventana de tres días:

- Usuarios que han iniciado una sesión o hicieron clic en el correo electrónico de incorporación
- Usuarios que no han iniciado una sesión ni hicieron clic en el correo electrónico de incorporación

![Un paso de ruta de acción dividido en dos rutas, una para los usuarios que han iniciado una sesión y otra para el resto.]({% image_buster /assets/img/canvas_templates/preference_survey8.png %}){: style="max-width:50%;"}

A partir de aquí, dirigiremos nuestros usuarios y mensajería según los grupos mencionados anteriormente.

#### Dirigirse a los usuarios comprometidos {#target-your-engaged-users}

Para nuestros usuarios que han iniciado una sesión o interactuado con nuestro correo electrónico de incorporación del primer paso de mensaje, actualizaremos el paso de mensaje **Getting Started Tips** para incluir los consejos esenciales de viaje y seguridad para nuestros nuevos usuarios de StyleRyde.

Después de que un usuario complete su incorporación, saldrá del Canvas.

A continuación, actualiza el paso de mensaje **Content Preferences Survey** para incluir nuestro cuestionario de preferencias que invita a los usuarios a seleccionar los temas sobre los que les interesa recibir información en el futuro.

![Una vista previa del cuestionario de preferencias que invita a los usuarios a seleccionar todos los intereses que apliquen.]({% image_buster /assets/img/canvas_templates/preference_survey7.png %}){: style="max-width:90%;"}

#### Animar a los usuarios que no han comenzado la incorporación {#nudge-users-who-havent-started-onboarding}

Para nuestros otros usuarios, actualizaremos el paso de mensaje **Winback Nudge** con nuestro correo electrónico de seguimiento para invitar a los usuarios a completar su incorporación.

Como último paso de reactivación de la interacción, renombraremos **Step 2** a **Final Winback Nudge** y actualizaremos el paso con nuestro mensaje dentro de la aplicación para invitar a nuestros nuevos usuarios a completar su incorporación.

### Paso 7: Probar y lanzar tu Canvas {#step-7-test-and-launch-your-canvas}

Después de probar y revisar nuestro Canvas para asegurarnos de que funciona como se espera, lo lanzaremos seleccionando **Launch Canvas**.

{% alert tip %}
Consulta nuestra [lista de verificación previa y posterior al lanzamiento]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para conocer los aspectos a considerar antes y después de lanzar un Canvas.
{% endalert %}