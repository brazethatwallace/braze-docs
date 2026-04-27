---
nav_title: Datos personalizados
article_title: Datos personalizados
page_order: 0
page_type: landing
description: "Los datos personalizados impulsan tu estrategia de interacción en Braze. Aprende sobre atributos personalizados, eventos, catálogos, tipos de datos y cómo gestionar la integridad de tus datos."
---

# Datos personalizados {#custom-data}

> Los datos personalizados son el combustible de tu estrategia de interacción. Mientras que los atributos estándar como el nombre y el país vienen integrados, los datos personalizados te permiten capturar los detalles únicos que definen tu relación con tus clientes, desde su género cinematográfico favorito hasta el momento exacto en que completaron una compra.

Al incorporar esta información en Braze, puedes ir más allá de la mensajería genérica para crear experiencias que se sientan personales, oportunas y relevantes. Puedes usar estos datos para crear segmentos precisos, personalizar el contenido de los mensajes con Liquid y desencadenar recorridos automatizados basados en el comportamiento en tiempo real.

## Atributos y eventos {#attributes-and-events}

La decisión más importante que tomarás al configurar tus datos es elegir entre un atributo y un evento.

### Atributos personalizados: quiénes son tus usuarios {#custom-attributes-who-your-users-are}

Piensa en los atributos personalizados como los rasgos o propiedades persistentes de tus usuarios. Son ideales para almacenar información que representa un estado actual o que cambia con poca frecuencia.

- **Caso de uso:** Podrías usar un atributo `loyalty_tier` para distinguir entre tus miembros "Silver" y "Gold".
- **Personalización:** Los atributos son perfectos para la personalización. Puedes incluir la `favorite_category` de un usuario en la línea del asunto de un correo electrónico para captar su atención.
- **Almacenamiento:** Estos datos permanecen en el perfil de usuario de forma indefinida mientras el perfil siga activo.

Para más información, consulta [Atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/).

### Eventos personalizados: qué hacen tus usuarios {#custom-events-what-your-users-do}

Los eventos personalizados rastrean acciones específicas que tus usuarios realizan en un momento determinado. Son interacciones de alto valor que te ayudan a entender el "cuándo" y el "con qué frecuencia" del comportamiento de los usuarios.

- **Caso de uso:** Cuando un usuario completa un registro, puedes registrar un evento `completed_registration`.
- **Desencadenamiento:** Los eventos son la forma principal de desencadenar la entrega basada en acciones. Puedes enviar una notificación push de "Bienvenida" en el momento en que se registra el evento `completed_registration`.
- **Metadatos:** Puedes añadir detalles adicionales a un evento usando propiedades del evento, como el nombre del artículo añadido a un carrito.
- **Análisis:** Los eventos potencian la segmentación, los informes y los análisis para que puedas medir la interacción y optimizar tu mensajería.

Para más información, consulta [Eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/).

## Catálogos {#catalogs}

Mientras que los atributos y eventos se centran en tus usuarios, los catálogos te permiten incorporar datos que no son de usuario, como inventarios de productos, detalles de cursos o listados de eventos.

Al importar estos metadatos a través de CSV o API, puedes enriquecer tus mensajes con información que no está almacenada en el perfil de usuario. Por ejemplo, puedes usar un catálogo para notificar automáticamente a los clientes cuando un artículo que vieron anteriormente vuelve a estar disponible o ha bajado de precio.

Para más información, consulta [Catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/).

## Tipos de datos {#data-types}

Braze admite varios tipos de datos para tus datos personalizados —incluyendo booleano, número, cadena, array, hora y tipos de objeto— cada uno con comportamientos y opciones de segmentación específicos. El tipo de datos que elijas afecta cómo puedes filtrar y personalizar en campañas y segmentos.

Para una referencia completa de los tipos de datos admitidos para atributos personalizados, propiedades del evento y catálogos, consulta [Tipos de datos]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/).

## Gestionar la integridad de tus datos {#managing-your-data-integrity}

Braze proporciona varias herramientas para ayudarte a gestionar tus datos personalizados a medida que tu estrategia evoluciona.

### Detección y cambios de tipo de datos {#data-type-detection-and-changes}

Braze reconoce automáticamente el tipo de datos (como un número o una cadena) del primer valor que recibe para un atributo. Para mantener la precisión, asegúrate de que tu equipo envíe tipos de datos consistentes en todos tus entornos. Si necesitas cambiar un tipo de datos, ten en cuenta que los datos existentes en los perfiles de usuario no se actualizarán retroactivamente, lo que puede afectar a tus segmentos.

### Bloqueo y eliminación {#blocklist-and-delete}

Si descubres que ciertos atributos o eventos ya no son útiles o se añadieron por error, puedes eliminarlos de tu espacio de trabajo.

- **Bloqueo:** Esto impide que Braze recopile nuevos datos para ese objeto. Evita que los datos aparezcan en filtros o gráficos, pero mantiene los datos existentes en los perfiles.
- **Eliminación:** Esto elimina permanentemente los datos de todos los perfiles de usuario. Debes bloquear un objeto de datos durante 7 días antes de que sea elegible para su eliminación.

Para más información, consulta [Administrar datos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/) y [Bloquear datos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data/).