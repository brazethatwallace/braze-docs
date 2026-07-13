---
nav_title: Bloquear datos personalizados
article_title: Bloquear datos personalizados
page_order: 3
page_type: reference
description: "Este artículo de referencia explica cómo bloquear y eliminar eventos personalizados y atributos personalizados en Braze."
---

# Bloquear datos personalizados {#blocklist-custom-data}

> Usa el bloqueo para dejar de rastrear datos personalizados que ya no son útiles. Usa la eliminación para quitar permanentemente eventos personalizados y atributos de los perfiles de usuario después de bloquearlos. Para prepoblar, administrar propiedades y configurar tipos de datos, consulta [Administrar datos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data).

## Bloquear datos personalizados {#blocklisting-custom-data}

Es posible que ocasionalmente identifiques atributos personalizados, eventos personalizados o eventos de compra que registran demasiados puntos de datos, ya no son útiles para tu estrategia de marketing o se registraron por error.

Para evitar que estos datos se envíen a Braze, puedes bloquear un objeto de datos personalizados mientras tu equipo de ingeniería trabaja en eliminarlo del backend de tu aplicación o sitio web. El bloqueo impide que Braze registre un objeto de datos personalizados en particular de ahora en adelante, lo que significa que no aparecerá al buscar un usuario específico.

### Elegir entre bloqueo o eliminación {#choosing-blocklisting-or-deletion}

- **Bloqueo**: conserva los atributos personalizados, eventos o compras existentes en los perfiles de usuario, pero Braze ya no procesa datos nuevos para esos objetos.
- **Eliminación**: quita esos datos de los perfiles de usuario. Los atributos personalizados y eventos eliminados pasan al estado **Trashed** durante siete días, durante los cuales puedes restaurarlos. Después de siete días, Braze los elimina permanentemente. La eliminación no impide que lleguen datos nuevos, así que confirma que tu SDK, API o importaciones CSV ya no envían esos datos antes de eliminarlos.

El bloqueo envía la información de bloqueo al dispositivo de cada usuario y puede consumir muchos datos. Bloquear una cantidad muy grande de atributos, eventos o compras (por ejemplo, más de 100) puede afectar el rendimiento de la aplicación. Si ya no planeas enviar esos datos a Braze, la eliminación suele ser el mejor enfoque después de haber detenido la integración que los envía.

Independientemente de si bloqueas o eliminas, esos atributos personalizados, eventos y compras ya no aparecen en la página **Manage Workspace** y se quitan como filtros de Segments. Si eliminas datos personalizados, Braze quita esos datos a nivel de usuario de los perfiles según [Cómo funciona la eliminación](#how-deletion-works).

Para bloquear datos personalizados, necesitas los [permisos de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) del siguiente desplegable para tu espacio de trabajo.

{% details Permisos de usuario para bloquear datos personalizados %}

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
- Ver plantillas de Webhook
- Editar plantillas de Webhook
- Ver plantillas de enlace
- Editar plantillas de enlace
- Ver activos de la biblioteca de medios
- Editar activos de la biblioteca de medios
- Eliminar activos de la biblioteca de medios
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

Los datos bloqueados no son enviados por el SDK, y el dashboard de Braze no procesa datos bloqueados de otras fuentes (por ejemplo, la API). Sin embargo, el bloqueo no elimina datos de los perfiles de usuario ni reduce retroactivamente la cantidad de puntos de datos generados por ese objeto de datos personalizados. Los datos bloqueados están ocultos y aún pueden usarse para plantillas Liquid.

### Bloquear atributos personalizados, eventos personalizados y productos {#blocklisting-custom-attributes-custom-events-and-products}

{% alert important %}
Cuando un evento o atributo se bloquea, cualquier Segment, Campaign o Canvas que use ese evento o atributo se archiva.
{% endalert %}

Para dejar de rastrear un atributo personalizado, evento o producto específico, sigue estos pasos:

1. Búscalo en las páginas **Custom Attributes**, **Custom Events** o **Products**.
2. Selecciona el atributo personalizado, evento o producto. Para atributos personalizados y eventos, puedes seleccionar hasta 100 para bloquear a la vez.
3. Selecciona **Blocklist**.

![Múltiples atributos personalizados seleccionados que están bloqueados en la página de atributos personalizados.]({% image_buster /assets/img_archive/blocklist_custom_attr.png %})

Puedes bloquear hasta 300 atributos personalizados y 300 eventos personalizados. Para evitar la recopilación de ciertos atributos de dispositivo, consulta nuestra [guía del SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer#blocking-data-collection).

{% alert important %}
Los atributos personalizados o eventos personalizados con estado **Trashed** cuentan para el límite de bloqueo hasta que se eliminen.
{% endalert %}

Cuando un evento personalizado o atributo se bloquea, se aplica lo siguiente:

- Los datos enviados a Braze no se procesan, y los eventos y atributos bloqueados ya no cuentan como puntos de datos
- Los datos existentes no están disponibles a menos que se reactiven
- Los eventos y atributos bloqueados no aparecen en filtros ni gráficos
- Las referencias a datos bloqueados dentro de borradores de Canvas activos se cargan como valores no válidos, lo que puede causar errores
- Todo lo que use el evento o atributo bloqueado se archiva

Para lograr esto, Braze envía la información de bloqueo a cada dispositivo. Esto es importante al considerar bloquear una gran cantidad de eventos y atributos (cientos de miles o millones), ya que es una operación intensiva en datos.

### Consideraciones para el bloqueo {#considerations-for-blocklisting}

Bloquear un gran número de eventos y atributos es posible, pero no recomendable. Esto se debe a que cada vez que se realiza un evento o se envía (potencialmente) un atributo a Braze, ese evento o atributo debe verificarse contra toda la lista de bloqueo.

Se envían hasta 300 elementos al SDK para el bloqueo. Si bloqueas más de 300 elementos, estos datos se envían desde el SDK. Si no necesitas usar el evento o atributo en el futuro, considera eliminarlo del código de tu aplicación en tu próxima versión. Los cambios en la lista de bloqueo pueden tardar unos minutos en propagarse. Puedes volver a habilitar cualquier evento o atributo bloqueado en cualquier momento.

## Eliminar datos personalizados {#deleting-custom-data}

A medida que construyes Campaigns y Segments dirigidos, es posible que descubras que ya no necesitas un evento personalizado o un atributo personalizado. Por ejemplo, si usaste un atributo personalizado específico como parte de una Campaign única, puedes eliminar estos datos después de [bloquearlos](#blocklisting-custom-attributes-custom-events-and-products) y quitar sus referencias de tu aplicación. Puedes eliminar cualquier tipo de datos (como cadenas, números y atributos personalizados anidados).

{% alert important %}
Debes ser [administrador de Braze]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#admin) para eliminar datos personalizados.
{% endalert %}

Para eliminar un evento personalizado o un atributo personalizado, haz lo siguiente:

1. Ve a **Configuración de datos** > **Custom Attributes** o **Custom Events**, según el tipo de datos que quieras eliminar.
2. Ve al dato personalizado y selecciona <i class="fa-solid fa-ellipsis-vertical" aria-label="Más opciones"></i>&nbsp;**Acciones** > **Blocklist**.
3. Después de que tus datos personalizados hayan estado bloqueados durante 7 días, selecciona <i class="fa-solid fa-ellipsis-vertical" aria-label="Más opciones"></i>&nbsp;**Acciones** > **Delete**.

### Cómo funciona la eliminación {#how-deletion-works}

Cuando eliminas datos personalizados, ocurre lo siguiente:

- **Para atributos personalizados:** elimina permanentemente los datos del atributo del perfil de cada usuario.
- **Para eventos personalizados:** elimina permanentemente los metadatos del evento del perfil de cada usuario.

Cuando se selecciona un atributo o evento para eliminación, su estado cambia a **Trashed**. Durante los siguientes siete días, es posible restaurar el atributo o evento. Si no lo restauras después de siete días, los datos se eliminan permanentemente. Si restauras el atributo o evento, vuelve al estado de bloqueado.

La eliminación no impide el registro adicional de los objetos de datos personalizados en los perfiles de usuario, así que asegúrate de que los datos personalizados ya no se estén registrando antes de eliminar el evento o atributo.

### Cosas que debes saber {#things-to-know}

Al eliminar datos personalizados, ten en cuenta los siguientes detalles:

* **La eliminación es permanente**. Los datos no se pueden recuperar.
* Los datos se eliminan de la plataforma Braze y de los perfiles de usuario.
* Puedes "reutilizar" el nombre del atributo personalizado o del evento personalizado después de la eliminación. Esto significa que si notas que los datos personalizados "reaparecen" en Braze después de la eliminación, puede deberse a una integración que no se ha detenido y está enviando datos con el mismo nombre de datos personalizados.
* Es posible que necesites bloquear un elemento nuevamente si tu eliminación resulta en la reaparición de datos personalizados. El estado de bloqueo no se conserva porque los datos personalizados se eliminan.
* Eliminar datos personalizados no registra ningún [punto de datos]({{site.baseurl}}/user_guide/data/infrastructure/data_points) y tampoco genera nuevos puntos de datos para usar.