---
nav_title: Incorporación
article_title: Incorporación
page_order: 5
page_type: reference
description: "Este artículo describe cómo usar una plantilla de Braze Canvas para crear recorridos de incorporación que promuevan una adopción inicial sólida y fomenten relaciones duraderas con tus usuarios."
tool: Canvas
---

# Incorporación {#onboarding}

> Inicia el recorrido de tus usuarios con esta plantilla de incorporación. Esta plantilla está diseñada para promover una adopción inicial sólida y fomentar relaciones duraderas con tus usuarios. Al aprovechar la comunicación personalizada y un conjunto estructurado de mensajes, puedes presentar fácilmente tu marca a tus usuarios e iniciar el comienzo de una relación duradera.

En este artículo, te guiaremos a través de un caso de uso para la plantilla de **Incorporación**, que está pensada para la etapa de consideración del ciclo de vida del usuario, para crear un recorrido de incorporación fluido para nuevos usuarios. Después de este artículo, habrás personalizado esta plantilla de Braze Canvas con mensajes personalizados para estos nuevos usuarios.

## Requisitos previos {#prerequisites}

Antes de usar esta plantilla, necesitas crear las siguientes [plantillas de correo electrónico]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template/) para hacer referencia en el Canvas:

- Un correo electrónico de bienvenida para todos los usuarios de tu aplicación
- Un correo electrónico con consejos sobre cómo usar tu aplicación
- Un correo electrónico de retroalimentación que incluya un cuestionario para el usuario

## Adaptar la plantilla a tus necesidades {#tailoring-the-template-to-your-needs}

Supongamos que trabajamos en PantsLabyrinth y nuestro objetivo es mejorar la interacción de los usuarios, generar confianza y fidelización con ellos, y animarlos a mantenerse comprometidos. Para ello, queremos centrarnos en crear mensajes dirigidos a nuevos usuarios que aún no han interactuado con la aplicación.

Para acceder a la plantilla de incorporación, al crear un nuevo Canvas, selecciona **Use a Canvas template** > **Braze templates**. Luego, junto a **Onboarding**, selecciona **Apply Template**. Comencemos a personalizar esta plantilla para adaptarla a nuestro caso de uso.

### Paso 1: Configura los detalles {#step-1-set-up-the-details}

Ajustemos los detalles del Canvas para reflejar nuestro objetivo.

1. Selecciona **Edit** junto al nombre de la plantilla.

![El título y la descripción actuales del Canvas.]({% image_buster /assets/img/canvas_templates/onboarding_old_name_description.png %}){: style="max-width:60%;"}

{:start="2"}
2. Actualiza el nombre del Canvas para especificar que es para la incorporación de nuevos usuarios.
3. Actualiza la descripción para especificar que el Canvas traza un recorrido de usuario que promueve la confianza y la fidelización con los usuarios.
4. Añade la etiqueta **Onboarding** para poder filtrar por ella en la página de inicio de Canvas.

![El nuevo nombre, descripción y etiqueta del Canvas.]({% image_buster /assets/img/canvas_templates/onboarding_new_name_description.png %}){: style="max-width:60%;"}

### Paso 2: Asigna tus eventos de conversión {#step-2-assign-your-conversion-events}

A continuación, asignemos nuestros eventos de conversión. Los eventos de conversión son un tipo de métrica que se puede usar para medir el éxito del Canvas. Para **Custom event name**, selecciona **Email Click** como el evento personalizado.

![Evento de conversión primaria - A con el tipo de conversión "Realiza evento personalizado" con el nombre de evento personalizado "Email Click". Hay un plazo de conversión de 4 días.]({% image_buster /assets/img/canvas_templates/onboarding1.png %})

Esto significa que los nuevos usuarios tienen hasta cuatro días para hacer clic en el correo electrónico de bienvenida. En este caso, queremos que nuestros nuevos usuarios sientan una sensación de urgencia para interactuar con PantsLabyrinth y suscribirse a una entrega recurrente de ropa de temporada.

### Paso 3: Establece un horario de entrada {#step-3-set-an-entry-schedule}

Dado que el objetivo es dirigirse a nuevos usuarios de PantsLabyrinth, mantendremos el Canvas como basado en acciones. Para **Start Session**, selecciona **Start Session in Any App** para permitir que los usuarios que inicien una sesión en cualquier aplicación entren al Canvas.

A continuación, ajusta la **Entry Window** para determinar cuándo los usuarios pueden entrar al Canvas. Supongamos que hay un próximo lanzamiento de suscripción de PantsLabyrinth a finales de octubre. Aquí es donde estableceremos la hora de inicio como **2024/10/28 8:00 am**. Opcionalmente, también podemos permitir que los usuarios entren al Canvas en su zona horaria local.

![Una ventana de entrada con la hora de inicio el 28 de octubre de 2024 a las 8 am. Los usuarios entrarán a este mensaje en su zona horaria local.]({% image_buster /assets/img/canvas_templates/onboarding4.png %})

### Paso 4: Segmenta tu audiencia {#step-4-target-your-audience}

Al dirigirnos a la audiencia correcta, podemos interactuar eficazmente con los nuevos usuarios. Por ejemplo, esta plantilla se dirige a todos los usuarios que usaron una aplicación por primera vez hace menos de un día, lo cual es preciso para nuestro caso de uso. Así que dejaremos esta sección tal como está.

### Paso 5: Configura los ajustes de envío {#step-5-set-send-settings}

De forma predeterminada, este Canvas se envía a los usuarios que están suscritos u optados y sigue las reglas de limitación de frecuencia. Mantendremos estos ajustes tal como están.

### Paso 6: Personaliza tu Canvas {#step-6-customize-your-canvas}

Ahora, construyamos el Canvas personalizando los pasos de la plantilla.

#### Configura el correo electrónico de bienvenida {#set-up-the-welcome-email}

1. Selecciona el paso de mensaje llamado "Welcome Email".
2. Selecciona **Edit message** para reemplazar el correo electrónico de la plantilla con nuestro correo electrónico de bienvenida.
3. Selecciona **Done**.

Ahora, nuestros usuarios recibirán este correo electrónico de bienvenida después de haber iniciado una sesión en nuestra aplicación. Para no abrumar a los usuarios con mensajes repetidos, recomendamos usar el paso de retraso como parte del recorrido del usuario.

#### Personaliza la ruta de audiencia {#customize-the-audience-path}

En el paso de ruta de audiencia llamado **Audience Split**, podemos personalizar el filtro para nuestros usuarios comprometidos. En la plantilla, el filtro es **Has clicked email for step Welcome Email**, lo que significa que los usuarios se dividen en dos grupos: los que han hecho clic en el correo electrónico de bienvenida y los que no.

![Un paso de división de audiencia con una ruta para usuarios comprometidos y otra ruta para el resto.]({% image_buster /assets/img/canvas_templates/onboarding2.png %}){: style="max-width:70%;"}

Como minorista de ropa en línea, PantsLabyrinth también tiene un grupo activo de usuarios móviles. Así que, en un Canvas de incorporación separado, también podemos seleccionar el siguiente filtro para identificar y dividir a nuestros usuarios móviles en estos segmentos:

- **Has clicked content card for step Welcome Content Card**
- **Everyone Else**

#### Dirige a más usuarios con rutas de audiencia {#target-more-users-with-audience-paths}

Del conjunto de usuarios que no han interactuado con nuestra aplicación, podemos dirigirnos aún más a estos usuarios editando el paso "Check for Clicks" y el paso "Winback Nudge".

### Paso 7: Prueba y lanza tu Canvas {#step-7-test-and-launch-your-canvas}

Después de probar y revisar nuestro Canvas para asegurarnos de que funciona como se espera, selecciona **Launch Canvas** para lanzar el Canvas. ¡Ahora podemos ofrecer a nuestros nuevos usuarios una experiencia de incorporación personalizada para fomentar una relación duradera!

{% alert tip %}
Consulta nuestra [Lista de verificación previa y posterior al lanzamiento]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para conocer las cosas a considerar antes y después de lanzar un Canvas.
{% endalert %}