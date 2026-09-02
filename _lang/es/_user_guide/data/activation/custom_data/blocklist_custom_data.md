---
nav_title: Bloquear datos personalizados
article_title: Bloquear datos personalizados
page_order: 3
page_type: reference
description: "Este artículo de referencia explica cómo bloquear y eliminar eventos personalizados y atributos personalizados en Braze."
---

# Bloquear datos personalizados {#blocklist-custom-data}

> Usa el bloqueo para dejar de rastrear datos personalizados que ya no son útiles. Usa la eliminación para quitar permanentemente eventos personalizados y atributos de los perfiles de usuario después de bloquearlos. Para prepoblar, administrar propiedades y configurar tipos de datos, consulta [Administrar datos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data).

## Incluir datos personalizados en la lista de bloqueo {#blocklisting-custom-data}

Es posible que en algún momento identifiques atributos personalizados, eventos personalizados o eventos de compra que registran demasiados puntos de datos, ya no son útiles para tu estrategia de marketing o se registraron por error.

Para evitar que estos datos se envíen a Braze, puedes incluir un objeto de datos personalizado en la lista de bloqueo mientras tu equipo de ingeniería trabaja en eliminarlo del backend de tu aplicación o sitio web. Incluir en la lista de bloqueo evita que Braze registre un objeto de datos personalizado en particular de ahí en adelante, lo que significa que no aparecerá cuando busques un usuario específico.

### Elegir entre lista de bloqueo o eliminación {#choosing-blocklisting-or-deletion}

- **Lista de bloqueo** mantiene los atributos personalizados, eventos o compras existentes en los perfiles de usuario, pero Braze ya no procesa datos nuevos para esos objetos.
- **Eliminación** borra esos datos de los perfiles de usuario. Los atributos personalizados y eventos eliminados pasan al estado **Papelera** durante siete días, período en el que puedes restaurarlos. Después de siete días, Braze los elimina de forma permanente. La eliminación no impide que lleguen datos nuevos, así que confirma que tu SDK or kit de desarrollo de software, API o importaciones CSV ya no envíen esos datos antes de eliminarlos.

La lista de bloqueo envía información de bloqueo al dispositivo de cada usuario y puede consumir muchos datos. Incluir en la lista de bloqueo una cantidad muy grande de atributos, eventos o compras (por ejemplo, más de 100) puede afectar el rendimiento de la aplicación. Si ya no planeas enviar esos datos a Braze, la eliminación suele ser el enfoque más adecuado después de que hayas detenido el envío desde la integración.

Independientemente de si incluyes en la lista de bloqueo o eliminas, esos atributos personalizados, eventos y compras ya no aparecen en la página **Gestionar espacio de trabajo** y se eliminan como filtros de segmento. Si eliminas datos personalizados, Braze elimina esos datos a nivel de usuario de los perfiles según lo descrito en [Cómo funciona la eliminación](#how-deletion-works).

Para incluir datos personalizados en la lista de bloqueo, necesitas los [permisos de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) del siguiente desplegable para tu espacio de trabajo.

{% details Permisos de usuario para incluir datos personalizados en la lista de bloqueo %}

- Ver Campaigns
- Editar Campaigns
- Archivar Campaigns
- Ver Canvas
- Editar Canvas
- Archivar Canvas
- Ver reglas de limitación de frecuencia
- Editar reglas de limitación de frecuencia
- Ver priorización de mensajes
- Editar priorización de mensajes
- Ver Content Blocks
- Ver conmutadores de características
- Editar conmutadores de características
- Archivar conmutadores de características
- Ver Segments
- Editar Segments
- Ver plantillas de IAM
- Editar plantillas de IAM
- Archivar plantillas de IAM
- Ver plantillas de correo electrónico
- Editar plantillas de correo electrónico
- Archivar plantillas de correo electrónico
- Ver plantillas de webhook
- Editar plantillas de webhook
- Ver plantillas de enlace
- Editar plantillas de enlace
- Ver activos de la biblioteca multimedia
- Editar activos de la biblioteca multimedia
- Eliminar activos de la biblioteca multimedia
- Ver ubicaciones
- Editar ubicaciones
- Archivar ubicaciones
- Ver códigos promocionales
- Editar códigos promocionales
- Exportar códigos promocionales
- Ver centros de preferencias
- Editar centros de preferencias
- Ver informes
- Editar informes

{% enddetails %}

Los datos incluidos en la lista de bloqueo no son enviados por el SDK or kit de desarrollo de software, y el panel de Braze no procesa datos bloqueados de otras fuentes (por ejemplo, la API). Sin embargo, incluir en la lista de bloqueo no elimina datos de los perfiles de usuario ni reduce retroactivamente la cantidad de puntos de datos generados por ese objeto de datos personalizado. Los datos bloqueados están ocultos y aún pueden usarse para la creación de plantillas Liquid.

### Incluir en la lista de bloqueo atributos personalizados, eventos personalizados y productos {#blocklisting-custom-attributes-custom-events-and-products}

{% alert important %}
Cuando un evento o atributo se incluye en la lista de bloqueo, cualquier segmento, Campaign o Canvas que utilice ese evento o atributo se archiva.
{% endalert %}

Para dejar de rastrear un atributo personalizado, evento o producto específico, sigue estos pasos:

1. Búscalo en las páginas **Atributos personalizados**, **Eventos personalizados** o **Productos**.
2. Selecciona el atributo personalizado, evento o producto. Para atributos personalizados y eventos, puedes seleccionar hasta 100 para incluir en la lista de bloqueo a la vez.
3. Selecciona **Incluir en lista de bloqueo**.

![Varios atributos personalizados seleccionados que se incluyen en la lista de bloqueo en la página de atributos personalizados.]({% image_buster /assets/img_archive/blocklist_custom_attr.png %})

Puedes incluir en la lista de bloqueo hasta 300 atributos personalizados y 300 eventos personalizados. Para evitar la recopilación de ciertos atributos de dispositivo, consulta nuestra [guía del SDK or kit de desarrollo de software]({{site.baseurl}}/developer_guide/getting_started/sdk_overview#blocking-data-collection).

{% alert important %}
Los atributos personalizados o eventos personalizados con estado **Papelera** cuentan para el límite de la lista de bloqueo hasta que se eliminen.
{% endalert %}

Cuando un evento o atributo personalizado se incluye en la lista de bloqueo, se aplica lo siguiente:

- Los datos enviados a Braze no se procesan, y los eventos y atributos bloqueados ya no cuentan como puntos de datos
- Los datos existentes no están disponibles a menos que se reactiven
- Los eventos y atributos bloqueados no aparecen en filtros ni gráficos
- Las referencias a datos bloqueados en borradores de Canvas activos se cargan como valores no válidos, lo que puede provocar errores
- Todo lo que utilice el evento o atributo bloqueado se archiva

Para lograr esto, Braze envía la información de bloqueo a cada dispositivo. Esto es importante a la hora de pensar en incluir en la lista de bloqueo una gran cantidad de eventos y atributos (cientos de miles o millones), ya que es una operación que consume muchos datos.

### Consideraciones para la lista de bloqueo {#considerations-for-blocklisting}

Incluir en la lista de bloqueo una gran cantidad de eventos y atributos es posible, pero no recomendable. Esto se debe a que cada vez que se realiza un evento o se envía (potencialmente) un atributo a Braze, ese evento o atributo debe verificarse contra toda la lista de bloqueo.

Se envían hasta 300 elementos al SDK or kit de desarrollo de software para la lista de bloqueo. Si incluyes en la lista de bloqueo más de 300 elementos, estos datos se envían desde el SDK or kit de desarrollo de software. Si no necesitas usar el evento o atributo en el futuro, considera eliminarlo del código de tu aplicación en la próxima versión. Los cambios en la lista de bloqueo pueden tardar unos minutos en propagarse. Puedes volver a habilitar cualquier evento o atributo bloqueado en cualquier momento.

## Eliminar datos personalizados {#deleting-custom-data}

A medida que creas Campaigns y Segments segmentados, es posible que ya no necesites un evento personalizado o un atributo personalizado. Por ejemplo, si utilizaste un atributo personalizado específico como parte de una Campaign única, puedes eliminar estos datos después de [añadirlos a la lista de bloqueo](#blocklisting-custom-attributes-custom-events-and-products) y quitar sus referencias de tu aplicación. Puedes eliminar cualquier tipo de dato (como cadenas, números y atributos personalizados anidados).

{% alert important %}
Debes ser un [administrador de Braze]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#admin) para eliminar datos personalizados.
{% endalert %}

Para eliminar un evento personalizado o un atributo personalizado, haz lo siguiente:

1. Ve a **Configuración de datos** > **Atributos personalizados** o **Eventos personalizados**, dependiendo del tipo de dato que quieras eliminar.
2. Ve al dato personalizado y selecciona <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**Acciones** > **Añadir a lista de bloqueo**.
3. Después de que tu dato personalizado haya estado en la lista de bloqueo durante 7 días, selecciona <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**Acciones** > **Eliminar**.

### Cómo funciona la eliminación {#how-deletion-works}

Cuando eliminas datos personalizados, ocurre lo siguiente:

- **Para atributos personalizados:** Se eliminan permanentemente los datos del atributo del perfil de cada usuario.
- **Para eventos personalizados:** Se eliminan permanentemente los metadatos del evento del perfil de cada usuario.

Cuando un atributo o evento se selecciona para su eliminación, su estado cambia a **En papelera**. Durante los siguientes siete días, es posible restaurar el atributo o evento. Si no lo restauras después de siete días, los datos se eliminan permanentemente. Si restauras el atributo o evento, vuelve al estado de lista de bloqueo.

La eliminación no impide el registro adicional de los objetos de datos personalizados en los perfiles de usuario, así que asegúrate de que el dato personalizado ya no se esté registrando antes de eliminar el evento o atributo.

### Consideraciones importantes {#things-to-know}

Al eliminar datos personalizados, ten en cuenta los siguientes detalles:

* **La eliminación es permanente**. Los datos no se pueden recuperar.
* Los datos se eliminan de la plataforma Braze y de los perfiles de usuario.
* Puedes "reutilizar" el nombre del atributo personalizado o del evento personalizado después de la eliminación. Esto significa que si notas que los datos personalizados "reaparecen" en Braze después de la eliminación, puede deberse a una integración que no se ha detenido y que sigue enviando datos con el mismo nombre de dato personalizado.
* Es posible que necesites añadir un elemento a la lista de bloqueo de nuevo si tu eliminación provoca que los datos personalizados reaparezcan. El estado de la lista de bloqueo no se conserva porque el dato personalizado se ha eliminado.
* Eliminar datos personalizados no registra ningún [punto de datos]({{site.baseurl}}/user_guide/data/infrastructure/data_points) y tampoco genera nuevos puntos de datos para usar.