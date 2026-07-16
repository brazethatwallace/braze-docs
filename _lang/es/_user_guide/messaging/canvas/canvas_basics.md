---
nav_title: Conceptos básicos de Canvas
article_title: Conceptos básicos de Canvas
page_order: 0
page_type: reference
description: "Este artículo de referencia cubre los conceptos básicos de Canvas, abordando varias preguntas que deberías hacerte al configurar tu primer Canvas."
tool: Canvas

---

# Conceptos básicos de Canvas {#canvas-basics}

> Este artículo de referencia cubre los conceptos básicos de Canvas, abordando varias preguntas que deberías hacerte al configurar tu primer Canvas. También explicaremos las cinco preguntas clave (qué, cuándo, quién, por qué y dónde) de la visualización y cómo esto puede dar forma y definir la manera en que construyes tu Canvas.

## Comprender la estructura de Canvas {#understanding-canvas-structure}

Antes de entrar en los detalles más específicos de la [configuración de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas), identifiquemos las partes clave que componen un Canvas.

{% tabs %}
  {% tab Canvas %}
  Canvas es una interfaz unificada donde los especialistas en marketing crean campañas con múltiples mensajes. Es algo parecido a una herramienta de programación visual, que te permite construir un recorrido del usuario cohesivo a partir de una serie de pasos.

  ![Un ejemplo de un Canvas con un paso de división de decisiones en dos recorridos de usuario diferentes dependiendo de si un usuario tiene push habilitado.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %})

  {% endtab %}

  {% tab Recorrido %}

  Un recorrido, o comúnmente conocido como recorrido del usuario, es la experiencia individual de un usuario dentro del Canvas.<br><br> ![Un gráfico con el recorrido del cliente para un nuevo usuario. Un usuario anónimo instala una aplicación, Kat crea una cuenta, Kat no abre la aplicación durante una semana, una notificación push trae a Kat de vuelta a la aplicación, luego Kat usa la aplicación regularmente.]({% image_buster /assets/img_archive/Journey_2.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Constructor de Canvas %}
  El constructor de Canvas traza los pasos a seguir al crear tu Canvas. Esto incluye aspectos básicos como nombrar tu Canvas y añadir equipos. Esencialmente, el constructor de Canvas es la configuración crucial requerida antes de comenzar a construir tu Canvas. Aquí puedes controlar la forma en que tus usuarios comienzan y completan su recorrido del cliente con opciones para editar el [horario de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule), la [audiencia objetivo]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-13-set-your-target-entry-audience) y los [ajustes de envío]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings).<br><br> ![El constructor de Canvas en la sección Básicos para un Canvas llamado "New Canvas".]({% image_buster /assets/img_archive/canvas_flow_entry_wizard.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Variantes %}
  Una variante es el camino que cada cliente sigue en su recorrido. Canvas admite hasta ocho variantes con un grupo de control. Tú controlas qué segmento de tu audiencia seguirá cada variante.<br><br> ![Seleccionando el botón "Añadir variante".]({% image_buster /assets/img/canvas_intro/add_canvas_variant.gif %})

  {% endtab %}

  {% tab Pasos %}
  Un paso en Canvas es un punto de decisión de marketing: "si esto, entonces aquello." Aprovecha los [componentes de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components#about-canvas-components) para construir los pasos de un recorrido del usuario.<br><br> ![Ejemplo de cómo añadir un paso de retraso a un Canvas.]({% image_buster /assets/img/canvas_intro/add_canvas_step.gif %}) <br><br> Cuando un usuario entra en un Canvas, comienza en el primer paso. Cada paso tiene condiciones que determinan si un usuario puede avanzar al siguiente paso. Dentro de un paso, puedes configurar desencadenantes o planificar la entrega, refinar la segmentación añadiendo filtros o marcando eventos de excepción, y especificar diferentes canales como notificaciones push o eventos webhook. En Canvas, los pasos ocurren en secuencia, lo que significa que el primer paso ocurre antes de que pueda ocurrir el segundo. Digamos que tenemos un Canvas con los siguientes pasos: paso de retraso A con un retraso de 24 horas, paso de mensaje A con un mensaje push y paso de mensaje B con un mensaje dentro de la aplicación. El usuario A se mantiene en un retraso de 24 horas, luego, después de 24 horas, recibirá un mensaje push y después un mensaje dentro de la aplicación.

  {% endtab %}
{% endtabs %}

## Construir el recorrido del cliente {#building-the-customer-journey}

Usar las cinco preguntas clave (qué, cuándo, quién, por qué y dónde) de la visualización puede ayudarte a identificar tus estrategias de interacción con los clientes para crear un recorrido de mensajes personalizado para cada uno de tus usuarios.

### El "qué": Nombra tu Canvas {#the-what-name-your-canvas}

*¿Qué estás intentando ayudar al usuario a hacer o entender?*

Nunca subestimes el poder del nombre. Braze está diseñado para la colaboración, así que este es un buen momento para establecer cómo comunicarás los objetivos con tu equipo.

Puedes añadir etiquetas y nombrar los pasos y variantes en un Canvas. Para más información sobre recorridos del cliente, consulta nuestro curso de Braze Learning sobre [mapeo de ciclos de vida del usuario](https://learning.braze.com/mapping-customer-lifecycles).

### El "por qué": Identifica los eventos de conversión {#the-why-identify-conversion-events}

*Partiendo del "qué", ¿por qué estás construyendo este Canvas?*

Siempre es importante tener un objetivo definido en mente, y Canvas te ayuda a entender cómo estás rindiendo en relación con KPI como la participación en sesiones, compras y eventos personalizados.

Seleccionar al menos un [evento de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) te dará la capacidad de entender cómo optimizar el rendimiento dentro del Canvas. Y si tu Canvas tiene múltiples variantes o un grupo de control, Braze usará el evento de conversión para determinar la mejor variación para alcanzar este objetivo.

* **Iniciar sesión**: Quiero que mis usuarios vuelvan e interactúen con la aplicación.
* **Realizar compra**: Quiero que mis usuarios compren.
* **Realizar evento personalizado**: Quiero que mis usuarios realicen una acción específica que estoy rastreando como un evento personalizado.
* **Actualizar aplicación**: Quiero que mis usuarios actualicen la versión de su aplicación.

### El "cuándo": Crea las condiciones de inicio {#the-when-create-starting-conditions}

*¿Cuándo comenzará un usuario esta experiencia?*

Tu respuesta determinará los detalles de cuándo y cómo se entrega tu Canvas a tu cliente. Los usuarios pueden entrar en tu Canvas de dos maneras: mediante entrega planificada o desencadenantes basados en acciones.

{% alert tip %}
Consulta [Funcionalidades basadas en el tiempo]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types) para Canvas para más estrategias y respuestas a preguntas frecuentes.
{% endalert %}

La entrega planificada te permite enviar un Canvas inmediatamente a tu audiencia objetivo. También puedes hacer que se envíe regularmente, o planificarlo para un momento específico en el futuro. Los Canvas basados en acciones responden a comportamientos específicos del cliente a medida que ocurren. Por ejemplo, un desencadenante basado en acciones puede incluir abrir una aplicación, realizar una compra, interactuar con otra Campaign o desencadenar cualquier evento personalizado. En el momento en que ocurre la acción, puedes hacer que el Canvas se envíe a tus usuarios.

### El "quién": Selecciona una audiencia {#the-who-select-an-audience}

*¿A quién estás intentando llegar?*

Para definir tu "quién", puedes usar segmentos predefinidos disponibles en Canvas. También puedes añadir más filtros para enfocarte aún más en conectar con tu audiencia objetivo. Después de construir estos segmentos, solo los usuarios que cumplan con los criterios de la audiencia objetivo podrán entrar en el recorrido del Canvas, lo que lleva a una experiencia más personalizada. Consulta esta tabla para ver los filtros disponibles y cómo segmentan a tus usuarios para adaptarse a tu caso de uso.

| Filtro | Descripción |
|---------------------|-----------------------------------------------------------------------------------------------------|
| Datos personalizados | Segmenta usuarios basándote en eventos y atributos que tú defines. Puede usar características específicas de tu producto. |
| Actividad del usuario | Segmenta clientes basándote en sus acciones y compras. |
| Reorientación | Segmenta clientes que han recibido, se les ha enviado o han interactuado con Canvas anteriores. |
| Actividad de marketing | Segmenta clientes basándote en comportamientos universales como la última participación. |
| Atributos del usuario | Segmenta clientes por sus atributos y características constantes. |
| Atribución de instalación | Segmenta clientes por su primera fuente, grupo de anuncios, Campaign o anuncio. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="El \"quién\": Selecciona una audiencia" }

### El "dónde": Encuentra mi audiencia {#the-where-find-my-audience}

*¿Dónde puedo llegar mejor a mi audiencia?*

Aquí es donde determinamos qué canales de mensajería tienen más sentido para tu recorrido del usuario. Idealmente, querrás llegar a tus usuarios donde sean más accesibles. Con eso en mente, puedes usar cualquiera de los siguientes canales con Canvas:
* [Correo electrónico]({{site.baseurl}}/user_guide/channels/email)
* [Push]({{site.baseurl}}/user_guide/channels/push)
* [Mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages)
* [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)
* [SMS o MMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs)
* [Webhook]({{site.baseurl}}/user_guide/channels/webhooks)

### El "cómo": Construye la experiencia completa {#the-how-build-the-complete-experience}

*¿Cómo construyo mi recorrido de Canvas después de identificar las cinco preguntas clave?*

El "cómo" resume colectivamente cómo crearás tu Canvas y cómo llegarás a tus usuarios con tu mensaje. Por ejemplo, para que un mensaje sea efectivo, deberías optimizar el momento de tu mensajería con respecto a las zonas horarias de tus diferentes usuarios.

Responder al "cómo" también determina la cadencia de envío de un Canvas a tu audiencia (como una vez a la semana o cada dos semanas), y qué canales de mensajería aprovechar para cada Canvas que construyas, como se describe con el "dónde".

## Caso de uso: Flujo de incorporación de clientes {#use-case-customer-onboarding-flow}

Por ejemplo, digamos que eres especialista en marketing para MovieCanon, una empresa de servicios de streaming en línea, y estás a cargo de crear un flujo de incorporación para nuevos usuarios de tu aplicación. Haciendo referencia a las cinco preguntas clave, podríamos construir el Canvas de la siguiente manera.

* **Qué**: El nombre de nuestro Canvas será "Nuevo recorrido de incorporación".
* **Por qué**: El objetivo de nuestro Canvas es dar la bienvenida a nuestros usuarios y hacer que sigan interactuando con la aplicación.
* **Cuándo**: Después de que un usuario abra la aplicación por primera vez, queremos enviarle un correo electrónico de bienvenida.
* **Quién**: Nos dirigimos a nuevos usuarios que están usando nuestra aplicación por primera vez.
* **Dónde**: Estamos seguros de que podemos llegar a los nuevos usuarios a través de su correo electrónico, que es como hemos hecho toda nuestra mensajería anterior.
* **Cómo**: Queremos establecer un retraso de un día para no abrumar a nuestros nuevos usuarios con notificaciones. Después de este retraso, enviaremos un correo electrónico con una lista de las películas y programas de TV más populares para motivarlos a seguir usando la aplicación.

## Consejos generales {#general-tips}

### Determina cuándo y cómo usar pasos y variantes {#determine-when-and-how-to-use-steps-and-variants}

Cada Canvas debe tener al menos una variante y al menos un paso. A partir de ahí, el cielo es el límite, así que ¿cómo decides la forma de tu Canvas? Aquí es donde entran en juego tus objetivos, datos e hipótesis. La lluvia de ideas del "cómo" y el "dónde" te ayudará a trazar la forma y estructura correctas de tu Canvas.

### Trabaja hacia atrás {#work-backwards}

Algunos objetivos tienen sub-objetivos más pequeños. Por ejemplo, si tu meta es convertir a un usuario gratuito en una suscripción, puede que necesites una página con tus servicios de suscripción detallados. Un visitante puede necesitar ver las opciones antes de comprar. Puedes enfocar tus esfuerzos de mensajería en mostrarles esta página antes de una página de pago. Trabajar hacia atrás para entender el recorrido que un cliente debe seguir para llegar a tu objetivo es clave para guiarlo hacia la conversión.

### Varía tu mensajería {#mix-up-your-messaging}

¿Has ejecutado una Campaign similar en el pasado? ¿O hay una ejecutándose actualmente? Intenta usar ese mensaje y añadirle más personalización. Prueba un nuevo filtro o añade un mensaje de seguimiento. A medida que varíes tus técnicas de mensajería, monitorea tu rendimiento y sigue optimizando haciendo cambios incrementales.