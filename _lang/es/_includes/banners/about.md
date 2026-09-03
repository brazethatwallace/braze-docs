# Banners

> Con Banners, puedes crear mensajes personalizados para tus usuarios, al tiempo que amplías el alcance de tus otros canales, como el correo electrónico o las notificaciones push. Puedes integrar Banners directamente en tu aplicación o sitio web, lo que te permite interactuar con los usuarios a través de una experiencia que resulta natural.

## Requisitos previos {#prerequisites}

La disponibilidad de los Banners depende de tu paquete de Braze. Ponte en contacto con tu director de cuentas o administrador de éxito de cliente para empezar.

Antes de empezar, asegúrate de tener [ubicaciones de Banner]({{site.baseurl}}/developer_guide/banners/placements) creadas en tu aplicación o sitio web.

![Un ejemplo de Banner renderizado en un dispositivo.]({% image_buster /assets/img/banners/sample_banner.png %})

## ¿Por qué usar Banners? {#why-use-banners}

Los Banners permiten a los equipos de marketing y producto personalizar el contenido de aplicaciones o sitios web de forma dinámica, reflejando la elegibilidad y el comportamiento del usuario en tiempo real. Muestran mensajes en línea de forma persistente, proporcionando experiencias no intrusivas y contextualmente relevantes que pueden actualizarse al inicio de una sesión o a mitad de sesión cuando tu aplicación o sitio web lo solicita explícitamente.

Una vez que los Banners están integrados en una aplicación o sitio web, los especialistas en marketing pueden diseñar y lanzar Banners utilizando un editor de arrastrar y soltar o un editor HTML completo, eliminando la necesidad de asistencia continua del desarrollador, reduciendo la complejidad y mejorando la eficiencia.

| Caso de uso | Explicación |
| --- | --- |
| Anuncios | Mantén los anuncios como próximos eventos o cambios de políticas en primer plano de tu experiencia de la aplicación. |
| Personalización de ofertas | Muestra promociones e incentivos personalizados basados en el historial de navegación, el contenido del carrito, el nivel de suscripción y el estado de fidelización de cada usuario. |
| Segmentación de la participación de nuevos usuarios | Guía a los nuevos usuarios a través de flujos de incorporación y configuración de cuentas. |
| Ventas y promociones | Destaca contenido destacado, productos en tendencia y campañas de marca en curso de forma persistente y directamente en tu página de inicio sin interrumpir la experiencia del usuario. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="¿Por qué usar Banners?" }

## Características {#features}

Las características de los Banners incluyen:

- **Creación de contenido sencilla:** Crea y previsualiza tu Banner usando un editor visual de arrastrar y soltar con soporte para imágenes, texto, botones, formularios de captura de correo electrónico, código personalizado y más. Los equipos que prefieran gestionar su propio marcado pueden usar el editor HTML en su lugar para tener control total sobre el HTML y los estilos del Banner, o pedir a [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-messages) que genere HTML a partir de una descripción.
- **Ubicaciones flexibles:** Define múltiples ubicaciones dentro de tu aplicación o sitio web donde pueden aparecer los Banners, lo que permite una segmentación precisa para contextos específicos o experiencias de usuario.
- **Personalización dinámica:** Los Banners recalculan la personalización (lógica Liquid) y la segmentación cada vez que se actualiza el banner. Si un usuario actualiza su perfil o cambia un atributo personalizado, la siguiente actualización del Banner reflejará esos cambios.
- **Priorización nativa:** Establece la prioridad de visualización para cuando varios Banners apuntan a la misma ubicación, asegurando que el mensaje correcto llegue a los usuarios en el momento adecuado.
- **Bloque de editor de código personalizado:** Usa el bloque de editor de código personalizado para añadir HTML personalizado para una personalización avanzada o una integración fluida con tus estilos web existentes.

## Acerca de los Banners {#about-banners}

### ID de ubicación {#placement-id}

Las ubicaciones de Banner son ubicaciones específicas de tu aplicación o sitio web [que creas con el SDK de Braze]({{site.baseurl}}/developer_guide/banners/placements) y que designan dónde pueden aparecer los Banners.

Las ubicaciones más habituales son la parte superior de la página de inicio, las páginas de detalles de los productos y los procesos de pago. Una vez creadas las ubicaciones, los Banners se pueden [asignar en tu campaña de Banner]({{site.baseurl}}/user_guide/channels/banners/create_a_banner).

No hay un límite fijo en el número de ubicaciones que puedes crear por espacio de trabajo, y puedes crear tantos ID de ubicación como requiera tu experiencia. Cada ubicación debe ser única dentro de un espacio de trabajo. Un único ID de ubicación puede ser referenciado por hasta 25 mensajes activos al mismo tiempo.

{% alert important %}
Evita modificar los ID de ubicación después de lanzar una campaña de Banner.
{% endalert %}

### Prioridad del Banner {#priority}

Cuando varios mensajes de Banner hacen referencia al mismo ID de ubicación, los Banners se muestran por orden de prioridad: alta, media o baja. De forma predeterminada, los Banners están configurados en media, pero puedes [establecer manualmente la prioridad]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#set-banner-priority-optional) cuando crees o edites tu campaña de Banner.

Si varios Banners tienen la misma prioridad, se mostrará primero el Banner más reciente para el que el usuario sea elegible.

### Solicitudes de ubicación {#requests}

{% multi_lang_include banners/placement_requests.md %}

### Entrega de mensajes {#message-delivery}

Los mensajes de Banner se entregan a tu aplicación o sitio web como contenido HTML, normalmente representado dentro de un iframe. Esto garantiza que tus Banners se muestren de forma coherente en todos los dispositivos y te ayuda a mantener sus estilos y scripts separados del resto del código.

Los iframes permiten actualizaciones de contenido dinámicas y personalizadas que no requieren cambios en tu código base. Cada iframe recupera y muestra el HTML de cada sesión de usuario utilizando la lógica de segmentación y personalización de la campaña.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

### Dimensiones y tamaños {#dimensions-and-sizing}

Esto es lo que debes saber sobre las dimensiones y el tamaño de los Banners:

- Aunque el creador te permite previsualizar los Banners en diferentes dimensiones, esa información no se guarda ni se envía al SDK.
- El HTML ocupa todo el ancho del contenedor en el que se representa.
- Recomendamos crear un elemento de dimensiones fijas y probar esas dimensiones en el creador.

### Contenido conectado {#connected-content}

{% multi_lang_include alerts/early_access_beta_alert.md feature='Connected Content for Banners' %}

Puedes utilizar [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) para obtener datos en tiempo real de API externas en tu Banner. Dado que los Banners se representan en línea durante la actualización de una sesión, el contenido conectado tiene limitaciones específicas en este canal:

- **Solo solicitudes GET:** Los Banners solo representan solicitudes de contenido conectado de tipo `GET`. Las solicitudes `POST` no son compatibles.
- **Presupuesto de representación compartido:** Todas las ubicaciones devueltas en una única solicitud de actualización (hasta 10) comparten un presupuesto de representación de aproximadamente dos segundos. Cada llamada de contenido conectado cuenta contra este presupuesto compartido, por lo que una ubicación con llamadas lentas o numerosas puede consumir el tiempo que otras ubicaciones necesitan.
- **Sin reintentos:** Si una llamada de contenido conectado falla, se agota el tiempo de espera o se excede el presupuesto de representación, el resultado del contenido conectado para esa ubicación se trata como nulo. A diferencia de otros canales, los Banners no reintentan la solicitud ni retrasan la entrega.

## Limitaciones {#limitations}

Cada espacio de trabajo puede admitir hasta 200 Campaigns de Banner activas. Si se alcanza este límite, tendrás que [archivar o desactivar]({{site.baseurl}}/user_guide/messaging/governance/statuses#changing-the-status) una Campaign existente antes de crear una nueva.

Además, los mensajes de Banner no son compatibles con las siguientes características:

- Campaigns activadas por API y basadas en acciones
- [Contenido conectado](#connected-content) (en acceso anticipado)
- Códigos promocionales
- `catalog_items` que utilizan la [etiqueta `:rerender`]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs#using-liquid)

## Próximos pasos {#next-steps}

- [Crear ubicaciones de Banner en tu aplicación o sitio web]({{site.baseurl}}/developer_guide/banners/placements)
- [Crear una Campaign de Banner en Braze]({{site.baseurl}}/user_guide/channels/banners/create_a_banner)
- [Tutorial: Mostrar un Banner por ID de ubicación]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)

{% alert tip %}
¿Quieres ayudar a priorizar lo que viene después? Contacta a [banners-feedback@braze.com](mailto:banners-feedback@braze.com).
{% endalert %}