# Banners

> Con Banners, puedes crear mensajes personalizados para tus usuarios, al tiempo que amplías el alcance de tus otros canales, como el correo electrónico o las notificaciones push. Puedes integrar Banners directamente en tu aplicación o sitio web, lo que te permite interactuar con los usuarios a través de una experiencia que resulta natural.

## Requisitos previos {#prerequisites}

La disponibilidad de los Banners depende de tu paquete de Braze. Ponte en contacto con tu director de cuentas o administrador de éxito de cliente para empezar.

Antes de empezar, asegúrate de haber [creado ubicaciones de Banner]({{site.baseurl}}/developer_guide/banners/placements) en tu aplicación o sitio web.

![Ejemplo de Banner mostrado en un dispositivo.]({% image_buster /assets/img/banners/sample_banner.png %})

## ¿Por qué utilizar Banners? {#why-use-banners}

Los Banners permiten a los equipos de marketing y de producto personalizar de forma dinámica el contenido de las aplicaciones o los sitios web, reflejando la elegibilidad y el comportamiento de los usuarios en tiempo real. Muestran mensajes de forma persistente en línea, proporcionando experiencias no intrusivas y contextualmente relevantes que pueden actualizarse al inicio de una sesión o a mitad de sesión cuando tu aplicación o sitio web lo solicita explícitamente.

Una vez que los Banners están integrados en una aplicación o sitio web, los especialistas en marketing pueden diseñarlos y lanzarlos utilizando un sencillo editor de arrastrar y soltar, lo que elimina la necesidad de asistencia continua por parte de los desarrolladores, reduce la complejidad y mejora la eficiencia.

| Caso de uso | Explicación |
| --- | --- |
| Anuncios | Mantén los anuncios, como los próximos eventos o los cambios en las políticas, en un lugar destacado de la experiencia de la aplicación. |
| Personalización de ofertas | Muestra promociones e incentivos personalizados basados en el historial de navegación, el contenido del carrito, el nivel de suscripción y el estado de fidelización de cada usuario. |
| Interacción con nuevos usuarios | Guía a los nuevos usuarios a través de los flujos de incorporación y la configuración de la cuenta. |
| Ventas y promociones | Destaca el contenido destacado, los productos de tendencia y las campañas de marca en curso de forma persistente y directa en tu página de inicio sin interrumpir la experiencia del usuario. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="¿Por qué utilizar Banners?" }

## Características {#features}

Las características de los Banners incluyen:

- **Creación sencilla de contenido:** Crea y previsualiza tu Banner utilizando un editor visual de arrastrar y soltar compatible con imágenes, texto, botones, formularios de captura de correo electrónico, código personalizado y mucho más.
- **Ubicaciones flexibles:** Define múltiples ubicaciones dentro de tu aplicación o sitio web donde puedan aparecer los Banners, lo que permite una segmentación precisa a contextos específicos o experiencias de usuario.
- **Personalización dinámica:** Los Banners recalculan la personalización (lógica Liquid) y la segmentación cada vez que se actualiza el Banner. Si un usuario actualiza su perfil o cambia un atributo personalizado, la siguiente actualización del Banner reflejará esos cambios.
- **Priorización nativa:** Establece la prioridad de visualización cuando varios Banners se dirigen a la misma ubicación, asegurándote de que el mensaje adecuado llegue a los usuarios en el momento adecuado.
- **Bloque de editor de código personalizado:** Utiliza el bloque de editor de código personalizado para añadir HTML personalizado y así realizar personalizaciones avanzadas o integrarlo fácilmente con tus estilos web actuales.

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

## Limitaciones {#limitations}

Cada espacio de trabajo puede admitir hasta 200 campañas de Banner activas. Si se alcanza este límite, tendrás que [archivar o desactivar]({{site.baseurl}}/user_guide/messaging/governance/statuses#changing-the-status) una campaña existente antes de crear una nueva.

Además, los mensajes de Banner no admiten las siguientes características:

- Campaigns desencadenadas por API y basadas en acciones
- Contenido conectado
- Códigos promocionales
- `catalog_items` usando la [etiqueta `:rerender`]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs#using-liquid)

## Próximos pasos {#next-steps}

- [Crear ubicaciones de Banner en tu aplicación o sitio web]({{site.baseurl}}/developer_guide/banners/placements)
- [Crear una campaña de Banner en Braze]({{site.baseurl}}/user_guide/channels/banners/create_a_banner)
- [Tutorial: Mostrar un Banner por ID de ubicación]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)

{% alert tip %}
¿Quieres ayudar a priorizar lo que viene después? Contacta con [banners-feedback@braze.com](mailto:banners-feedback@braze.com).
{% endalert %}