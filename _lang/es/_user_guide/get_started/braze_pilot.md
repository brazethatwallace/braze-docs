---
nav_title: Braze Pilot
page_order: 10.5
layout: dev_guide
guide_top_header: "Braze Pilot"
guide_top_text: "Braze Pilot es una aplicación móvil diseñada para conectarse fácilmente con tu panel de Braze. Esto te permite lanzar campañas y Canvas a la aplicación, dando vida a los mensajes de Braze en tu propio teléfono. Braze Pilot incluye una biblioteca de simulaciones de aplicaciones para marcas ficticias que representan diferentes sectores, lo que te permite experimentar cómo se verían tus mensajes desde la perspectiva de tus clientes."
description: "Descubre las diferentes formas en que puedes utilizar Braze para enviar mensajes desde el panel de Braze a tu teléfono."

guide_featured_title: "Artículos de sección"
guide_featured_list:
  - name: Empieza a utilizar Braze Pilot
    link: /docs/user_guide/get_started/braze_pilot/getting_started
    image: /assets/img/braze_icons/brush-02.svg
  - name: Diccionario de datos
    link: /docs/user_guide/get_started/braze_pilot/data_dictionary
    image: /assets/img/braze_icons/book-closed.svg
  - name: Vínculos profundos
    link: /docs/user_guide/get_started/braze_pilot/deep_links
    image: /assets/img/braze_icons/link-03.svg

---

## Simulaciones de aplicaciones de Pilot {#pilot-app-simulations}

El núcleo de Braze Pilot es su biblioteca de simulaciones de aplicaciones. Cada aplicación es una simulación realista de una marca ficticia específica del sector, equipada para registrar una amplia variedad de eventos y atributos que crean infinitas oportunidades para impulsar los casos de uso habituales de Braze.

{% tabs local %}
{% tab Fitness %}

### Steppington

Steppington es una aplicación de fitness con entrenamientos, objetivos de ejercicio y un servicio premium Steppington+. Ofrece varios lugares para mostrar [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards), una sección que se puede revelar con [conmutadores de características]({{site.baseurl}}/developer_guide/feature_flags) y una sólida biblioteca de registro de eventos personalizados que permite ilustrar muchos recorridos del cliente para este sector.

![La página de inicio de Steppington con iconos para entrenamiento de maratón, yoga, ciclismo y pesas.]({% image_buster /assets/img/braze_pilot/steppington_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab Comercio electrónico %}

### PantsLabyrinth

PantsLabyrinth es una aplicación de comercio electrónico que vende (¡lo has adivinado!) ¡pantalones! La aplicación PantsLabyrinth incluye una experiencia completa de pago con carrito de la compra, una característica opcional de lista de deseos que se puede habilitar con un conmutador de características y muchas oportunidades para hacer bromas ingeniosas con amigos del Reino Unido.

![Página de producto de PantsLabyrinth con opciones para añadir vaqueros al carrito.]({% image_buster /assets/img/braze_pilot/pantslabyrinth_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab Streaming %}

### MovieCanon

MovieCanon es un servicio de streaming perfectamente diseñado para ilustrar los casos de uso habituales de Braze en torno a la interacción con el contenido.

![La aplicación MovieCanon con diferentes thrillers para ver.]({% image_buster /assets/img/braze_pilot/moviecanon_app.png %}){:style="max-width:50%"}

{% endtab %}
{% endtabs %}

## Cómo se conecta Pilot con tu panel de Braze {#how-pilot-connects-with-your-braze-dashboard}

El SDK de Braze es un paquete de código que recopila datos de tus usuarios una vez que se integra con tu aplicación o sitio web. Cuando conectas Pilot a tu panel de Braze, inicializas esta conexión entre la aplicación Pilot de tu teléfono y el SDK de Braze, y estableces una conexión única con tu instancia de Braze al proporcionar a Pilot el identificador de tu clave de API para tu panel de Braze.

![El primer paso para la configuración de Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Una vez que Pilot se conecta a tu panel de Braze, el SDK de Braze funciona en la aplicación igual que lo hará una vez que integres el SDK en tu propia aplicación o sitio web. Esto significa que Braze:

- Almacenará datos sobre tu actividad de usuario en Pilot, incluidos datos personalizados específicos de las marcas ficticias de la aplicación.
- Recopilará automáticamente datos de sesión, información del dispositivo y tokens de notificaciones push.
- Habilitará notificaciones push, mensajes dentro de la aplicación y canales de mensajería de Content Cards que requieren la integración del SDK para funcionar.

Para obtener más información sobre el SDK de Braze, consulta [Integración]({{site.baseurl}}/user_guide/get_started/integrations).

![La pila de interacción con los clientes de Braze, que incluye integraciones, API, SDK para la ingesta de datos, clasificación, orquestación, personalización y acción con canales de mensajería para un bucle de retroalimentación interactivo con tus clientes.]({% image_buster /assets/img/braze_pilot/braze_sdk_diagram.png %}){:style="max-width:70%"}

## Perfiles de usuario en Braze {#user-profiles-in-braze}

Todos los datos enviados a Braze se almacenan en un perfil de usuario dedicado a un usuario concreto de tu aplicación o sitio web. Una vez que conectes Pilot con tu panel de Braze, Braze comenzará a registrar datos sobre ti como usuario de Pilot. Hay dos tipos de usuarios que se pueden crear para ti a través de esta conexión: anónimos e identificados.

### Anónimo {#anonymous}

Este estado de conexión representa la experiencia de un visitante de tu aplicación o sitio web que aún no ha iniciado sesión. Si inicializas Pilot como usuario anónimo, Braze crea un [perfil de usuario anónimo]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users) para ti y registra allí los datos sobre tu actividad. Los usuarios anónimos pueden seguir siendo objetivo de campañas, pero no podrás consultar su perfil de usuario directamente en tu panel de Braze.

### Identificado {#identified}

Este estado de conexión significa que Braze reconoce tu perfil de usuario a través de un identificador único que se te ha asignado, conocido como identificador externo. Puedes buscar este identificador externo en la página **Búsqueda de usuarios** de tu panel de Braze para localizar tu perfil de usuario, que almacena todos los atributos de usuario y eventos registrados desde Pilot en función de tu actividad en la aplicación. En el panel de Braze, ve a **Audiencia** > **Búsqueda de usuarios**, introduce tu **ID externo** de Pilot y abre el perfil para revisar atributos y eventos.

### Tipo de conexión {#connection-type}

Para saber qué tipo de conexión tienes, revisa el indicador de estado de conexión en la esquina superior derecha de la aplicación Pilot.

{% tabs local %}
{% tab Anonymous user  %}

**Anónimo** indica que estás registrando datos como usuario anónimo. El área de estado muestra la etiqueta **Anónimo** (por ejemplo, un icono de máscara o de incógnito).

{% endtab %}
{% tab Identified user %}

Si estás registrando datos como usuario identificado, el área de estado muestra **Usuario identificado** y tu ID externo.

{% endtab %}
{% tab Not connected %}

**No conectado** indica que aún no has inicializado la conexión del SDK de Braze con Pilot. El área de estado indica que Pilot aún no está conectado a tu espacio de trabajo de Braze.

{% endtab %}
{% endtabs %}

## Campaigns y Canvas {#campaigns-and-canvases}

Campaigns y Canvas son la forma en que envías mensajes a tus usuarios.

- Las campañas son ideales para mensajes únicos enviados a un segmento de audiencia específico a través de varios canales.
- Los Canvas son flujos de trabajo avanzados que te permiten automatizar y orquestar recorridos personalizados del cliente a través de múltiples canales. Dentro de un Canvas, puedes configurar lógica de ramificación, retrasos, puntos de decisión y eventos de conversión para guiar a los clientes a través de una serie de interacciones. Los Canvas ayudan a garantizar una comunicación coherente y fluida entre los diferentes puntos de contacto, lo que aumenta las posibilidades de interacción con los clientes y conversión.

## Canales de mensajería compatibles {#supported-messaging-channels}

Braze Pilot actualmente admite [In-App Messages]({{site.baseurl}}/in-app_messages), que aparecen en tu aplicación y entregan mensajes oportunos mientras el usuario está interactuando activamente.

![Un mensaje dentro de la aplicación en MovieCanon: "¿Te gusta MovieCanon? ¡Recomienda a tus amigos!", con la opción de introducir tu dirección de correo electrónico para enviar un referido.]({% image_buster /assets/img/braze_pilot/moviecanon_iam.png %}){:style="max-width:40%"}