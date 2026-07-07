---
nav_title: El dashboard
article_title: El dashboard de Braze
page_order: 1
page_type: reference
description: "El dashboard de Braze es tu espacio de trabajo central para crear, gestionar y analizar la interacción con los clientes. Reúne herramientas de mensajería, información sobre la audiencia, segmentación y datos de rendimiento en tiempo real en un solo lugar."

---

# El dashboard de Braze {#the-braze-dashboard}

> El dashboard de Braze es tu espacio de trabajo central para crear, gestionar y analizar la interacción con los clientes. Accede a él en [dashboard.braze.com](https://dashboard.braze.com/) o [dashboard.braze.eu](https://dashboard.braze.eu/).

Utiliza el dashboard de Braze para planificar campañas, lanzar y gestionar mensajes, explorar información sobre la audiencia, ajustar la segmentación y revisar métricas de rendimiento e interacción en tiempo real desde una única interfaz.

## Resumen del dashboard {#dashboard-overview}

Cuando inicias sesión, el dashboard te ofrece una vista centralizada de tus herramientas de interacción y datos:

- **Página de inicio:** Muestra tu [contenido editado recientemente](#pick-up-where-you-left-off) y las métricas de rendimiento clave de un vistazo
- **Navegación lateral:** Organiza las herramientas por función (mensajería, audiencia, análisis, configuración)
- **Encabezado global:** Proporciona acceso rápido a la búsqueda, soporte, configuración de idioma, notificaciones y tu cuenta

Tu experiencia en el dashboard se organiza por [espacios de trabajo]({{site.baseurl}}/user_guide/get_started/workspaces), que te ayudan a gestionar contenido para diferentes marcas, regiones o equipos. Puedes [cambiar entre espacios de trabajo](#workspace-switcher) en cualquier momento desde la navegación lateral.

## Accede a tu dashboard {#access-your-dashboard}

Para empezar, [inicia sesión en tu cuenta de Braze]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account). Tu acceso a las páginas del dashboard y los permisos para realizar determinadas acciones se basan en tus [permisos de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions) asignados. Si necesitas ayuda con tus permisos, ponte en contacto con los administradores de Braze.

## Navega por Braze {#navigate-braze}

La navegación de Braze está diseñada para ayudarte a acceder de forma eficiente a las características y el contenido en todos los dispositivos. Hay dos niveles de navegación en el dashboard de Braze: el encabezado global y la navegación lateral.

El encabezado global es casi siempre visible en la parte superior de la pantalla. Proporciona acceso rápido a herramientas y configuraciones esenciales, incluyendo:

- [Búsqueda](#search-your-dashboard)
- Enlaces de soporte y comunidad
- [Idioma del dashboard]({{site.baseurl}}/user_guide/administer/personal/language_settings)
- Notificaciones
- Configuración de cuenta
- [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator)

### Usa la navegación lateral {#use-the-side-navigation}

El menú vertical de la izquierda organiza las herramientas de Braze por función y mantiene los elementos más utilizados al alcance. Selecciona un elemento del menú principal para ver sus opciones en un diseño vertical apilado.

![Selector de espacio de trabajo en el dashboard de Braze]({% image_buster /assets/img/workspace_switcher.png %}){: style="max-width:35%;float:right;margin-left:15px"}

#### Selector de espacio de trabajo {#workspace-switcher}

Ubicado en la parte superior de la navegación lateral, el selector de espacio de trabajo te permite moverte entre diferentes espacios de trabajo en tu instancia de Braze. El espacio de trabajo activo aparece resaltado.

Los [espacios de trabajo]({{site.baseurl}}/user_guide/get_started/workspaces) ayudan a organizar el contenido por marca, región, línea de producto o equipo. Cada espacio de trabajo incluye sus propios datos, Campaigns y configuración. Tu acceso puede variar entre espacios de trabajo. Por ejemplo, podrías tener acceso de edición en un espacio de trabajo y acceso de solo lectura en otro.

Para cambiar de espacio de trabajo, selecciona el menú desplegable de espacio de trabajo en la parte superior de la navegación lateral y elige el espacio de trabajo al que deseas acceder. También puedes [añadir espacios favoritos](#favorite-workspaces) para acceder más rápido a los que usas con más frecuencia.

#### Minimizar la navegación lateral {#minimize-the-side-navigation}

Para reducir el desorden visual, especialmente durante tareas como diseñar un Canvas, puedes minimizar el panel de navegación lateral. Pulsa **Minimizar menú** para contraerlo. Incluso cuando está minimizado, pasa el cursor sobre cualquier icono para ver información emergente con los nombres de los elementos del menú. Esto te ayuda a moverte rápidamente entre herramientas mientras mantienes tu espacio de trabajo limpio.

![Iconos de minimizar y maximizar menú]({% image_buster /assets/img/minimize_expand_menu.png %}){: style="max-width:60%;border:none"}

#### Navegación adaptable {#responsive-navigation}

La navegación se adapta fácilmente a diferentes tamaños de pantalla. En pantallas más pequeñas, la navegación lateral se contrae automáticamente. Pulsa <i class="fa-solid fa-bars" aria-label="Abrir menú de navegación"></i> para abrir el menú cuando lo necesites.

![En pantallas más pequeñas, la navegación lateral se contrae automáticamente. Tocar el icono del menú abre las opciones de navegación.]({% image_buster /assets/img/navigation/navigation_small_screens.png %}){: style="max-width: 80%;border:none"}

## Busca en tu dashboard {#search-your-dashboard}

La barra de búsqueda global, ubicada en el encabezado, es la forma más rápida de encontrar contenido en tu dashboard de Braze. Selecciónala para abrir la interfaz de búsqueda e ir directamente a lo que necesitas.

![Búsqueda global abierta sin términos de búsqueda introducidos, mostrando las páginas abiertas recientemente.]({% image_buster /assets/img/navigation/search_recently_opened.png %})

Tu contenido abierto recientemente aparece debajo de la barra de búsqueda. Esto incluye cualquier Campaign, Canvas, plantilla o página con la que hayas interactuado recientemente, lo que facilita volver a tu trabajo.

### ¿Qué puedes buscar? {#what-can-you-search-for}

Puedes buscar los siguientes elementos y acciones:

- Nombres de Campaigns
- Nombres de Canvas
- Content Blocks
- Nombres de Segments
- Nombres de plantillas de correo electrónico
- Páginas dentro de Braze (incluidos sinónimos)

{% alert tip %}
Para buscar texto exacto, pon tu término de búsqueda entre comillas (""). Por ejemplo, buscar ["all users"] devolverá todos los elementos que contengan la frase exacta "all users" en su nombre.
{% endalert %}

### Etiquetas de tipo de contenido y estado {#content-type-and-status-tags}

Cada resultado está etiquetado con una indicación de su tipo de contenido, como Campaign, Canvas o Segment, y su estado (activo, archivado, detenido).

### Filtrar por contenido activo y en borrador {#filter-for-active-and-draft-content}

De forma predeterminada, la búsqueda incluye elementos activos, en borrador y archivados. Usa el interruptor **Show active and draft only** para acotar tus resultados.

![El interruptor "Show active and draft only".]({% image_buster /assets/img/navigation/show_active_draft_new.png %})

### Atajos de teclado {#keyboard-shortcuts}

Puedes moverte por los resultados de búsqueda usando tu teclado.

<style>
  div.small_table + table {
    max-width: 60%;
  }
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2) {
    width:20%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

| Acción                      | Atajo de teclado                                                             |
| --------------------------- | ----------------------------------------------------------------------------- |
| Abrir el menú de búsqueda        | {::nomarkdown} <ul> <li> Mac: <kbd>⌘</kbd>&nbsp;+&nbsp;<kbd>K</kbd> </li> <li>Windows: <kbd>Ctrl</kbd>&nbsp;+&nbsp;<kbd>K</kbd> </li> </ul> {:/}  |
| Moverse entre resultados de búsqueda | <kbd>⬆</kbd> / <kbd>⬇</kbd>  |
| Seleccionar un resultado de búsqueda      | <kbd>Enter</kbd>    |
| Cerrar el menú de búsqueda       | <kbd>Esc</kbd>  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atajos de teclado" }

## Características de productividad {#productivity-features}

El dashboard de Braze incluye varias características para ayudarte a trabajar de forma más eficiente y acceder rápidamente a las herramientas y el contenido que más utilizas.

### BrazeAI Operator

BrazeAI Operator™ es un asistente impulsado por IA integrado en el dashboard. Úsalo para obtener respuestas, recorrer la configuración, solucionar problemas y generar ideas. Ábrelo desde **BrazeAI Operator™** en el encabezado global junto a tu perfil. Para más información, consulta [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator).

### Retoma donde lo dejaste {#pick-up-where-you-left-off}

En la página de **Home**, el dashboard muestra tus Campaigns, Canvas y Segments editados o creados recientemente. Esto facilita volver al trabajo en curso sin necesidad de buscar. Cada elemento incluye etiquetas que muestran el tipo de contenido y el estado (como borrador, activo o detenido).

![Un borrador de Canvas, un Segment activo y un borrador de Campaign en la sección "Retoma donde lo dejaste".]({% image_buster /assets/img/pick_up_where_you_left_off.png %})

Para más información, consulta [Dashboard de inicio]({{site.baseurl}}/user_guide/analytics/dashboards/home#pick-up-where-you-left-off).

### Espacios favoritos {#favorite-workspaces}

Si trabajas en varios espacios de trabajo, puedes marcar los que usas con más frecuencia como favoritos. Los espacios favoritos aparecen en la parte superior del selector de espacio de trabajo para un acceso más rápido.

Para añadir espacios favoritos:

1. [Accede a la configuración de tu perfil](#access-your-profile-settings).
2. En la sección **Perfil de cuenta**, localiza el campo **Espacios favoritos**.
3. Selecciona los espacios de trabajo que deseas marcar como favoritos.

### Accede a la configuración de tu perfil {#access-your-profile-settings}

Para gestionar la configuración de tu cuenta, las preferencias de notificación y la información personal:

1. Selecciona el icono de tu perfil en el encabezado global.
2. Selecciona **Gestiona tu cuenta** para acceder a tu página de perfil.

Desde tu página de perfil, puedes actualizar la configuración de correo electrónico, configurar la autenticación de dos factores, ver tus claves de API y gestionar otros detalles de la cuenta.

## Accesibilidad en el dashboard {#accessibility-in-the-dashboard}

El dashboard de Braze utiliza colores de marca que cumplen con los estándares WCAG AA de contraste de color. Esto favorece una experiencia inclusiva para todos los usuarios y se alinea con las mejores prácticas de accesibilidad.

## Compartir comentarios {#sharing-feedback}

¿Quieres contarnos lo que piensas? Puedes compartir comentarios sobre navegación, accesibilidad, usabilidad, diseño visual y más. Abre el menú de **Support** en el encabezado global y selecciona **Share feedback**. Revisamos todos los comentarios para ayudar a mejorar tu experiencia con Braze.

## Recursos relacionados {#related-resources}

### Tareas administrativas {#administrative-tasks}

- [Crear y gestionar espacios de trabajo]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces)
- [Gestionar usuarios de Braze]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users)
- [Permisos de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)
- [Equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams)

### Tareas clave y próximos pasos {#key-tasks-and-next-steps}

- **Crear Campaigns**: [Crear una Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign)
- **Crear recorridos**: [Crear un Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)
- **Definir audiencias**: [Crear un Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)
- **Revisar el rendimiento**: [Resumen de análisis]({{site.baseurl}}/user_guide/analytics/dashboards/home)
- **Configurar ajustes**: [Configuración de la aplicación]({{site.baseurl}}/user_guide/administer/global/workspace_settings)