---
nav_title: Bloquear datos personalizados
article_title: Bloquear datos personalizados
page_order: 3
page_type: reference
description: "Este artículo de referencia explica cómo bloquear y eliminar eventos personalizados y atributos personalizados en Braze."
---

# Bloquear datos personalizados

> Usa el bloqueo para dejar de rastrear datos personalizados que ya no son útiles. Usa la eliminación para quitar permanentemente eventos personalizados y atributos de los perfiles de usuario después de bloquearlos. Para prepoblar, administrar propiedades y configurar tipos de datos, consulta [Administrar datos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/).

## Bloquear datos personalizados

Es posible que ocasionalmente identifiques atributos personalizados, eventos personalizados o eventos de compra que registran demasiados puntos de datos, ya no son útiles para tu estrategia de marketing o se registraron por error.

Para evitar que estos datos se envíen a Braze, puedes bloquear un objeto de datos personalizados mientras tu equipo de ingeniería trabaja en eliminarlo del backend de tu aplicación o sitio web. El bloqueo impide que Braze registre un objeto de datos personalizados en particular de ahora en adelante, lo que significa que no aparecerá al buscar un usuario específico.

Para bloquear datos personalizados, necesitas los [permisos de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) del siguiente desplegable para tu espacio de trabajo.

{% details Permisos de usuario para bloquear datos personalizados %}

{% multi_lang_include deprecations/user_permissions.md %}

- Ver campañas
- Editar campañas
- Archivar campañas
- Ver Canvas
- Editar Canvas
- Archivar Canvas
- Ver reglas de limitación de frecuencia
- Editar reglas de limitación de frecuencia
- Ver priorización de mensajes
- Editar priorización de mensajes
- Ver Bloques de contenido
- Ver conmutadores de características
- Editar conmutadores de características
- Archivar conmutadores de características
- Ver segmentos
- Editar segmentos
- Ver plantillas IAM
- Editar plantillas IAM
- Archivar plantillas IAM
- Ver plantillas de correo electrónico
- Editar plantillas de correo electrónico
- Archivar plantillas de correo electrónico
- Ver plantillas de Webhook
- Editar plantillas de Webhook
- Ver plantillas de enlaces
- Editar plantillas de enlaces
- Ver activos de la Biblioteca de medios
- Editar activos de la Biblioteca de medios
- Eliminar activos de la Biblioteca de medios
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

### Bloquear atributos personalizados, eventos personalizados y productos

{% alert important %}
Cuando un evento o atributo se bloquea, cualquier segmento, campaña o Canvas que use ese evento o atributo se archiva.
{% endalert %}

Para dejar de rastrear un atributo personalizado, evento o producto específico, sigue estos pasos:

1. Búscalo en las páginas **Atributos personalizados**, **Eventos personalizados** o **Productos**.
2. Selecciona el atributo personalizado, evento o producto. Para atributos personalizados y eventos, puedes seleccionar hasta 100 para bloquear a la vez.
3. Selecciona **Bloquear**.

![Múltiples atributos personalizados seleccionados que están bloqueados en la página de Atributos personalizados.]({% image_buster /assets/img_archive/blocklist_custom_attr.png %})

Puedes bloquear hasta 300 atributos personalizados y 300 eventos personalizados. Para evitar la recopilación de ciertos atributos de dispositivo, consulta nuestra [guía del SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection).

{% alert important %}
Los atributos personalizados o eventos personalizados con estado **Descartado** cuentan para el límite de bloqueo hasta que se eliminen.
{% endalert %}

Cuando un evento personalizado o atributo se bloquea, se aplica lo siguiente:

- Los datos enviados a Braze no se procesan, y los eventos y atributos bloqueados ya no cuentan como puntos de datos
- Los datos existentes no están disponibles a menos que se reactiven
- Los eventos y atributos bloqueados no aparecen en filtros ni gráficos
- Las referencias a datos bloqueados dentro de borradores de Canvas activos se cargan como valores no válidos, lo que puede causar errores
- Todo lo que use el evento o atributo bloqueado se archiva

Para lograr esto, Braze envía la información de bloqueo a cada dispositivo. Esto es importante al considerar bloquear una gran cantidad de eventos y atributos (cientos de miles o millones), ya que sería una operación intensiva en datos.

### Consideraciones para el bloqueo

Bloquear un gran número de eventos y atributos es posible, pero no recomendable. Esto se debe a que cada vez que se realiza un evento o se envía (potencialmente) un atributo a Braze, ese evento o atributo debe verificarse contra toda la lista de bloqueo.

Se envían hasta 300 elementos al SDK para el bloqueo. Si bloqueas más de 300 elementos, estos datos se envían desde el SDK. Si no necesitas usar el evento o atributo en el futuro, considera eliminarlo del código de tu aplicación en tu próxima versión. Los cambios en la lista de bloqueo pueden tardar unos minutos en propagarse. Puedes volver a habilitar cualquier evento o atributo bloqueado en cualquier momento.

## Eliminar datos personalizados

A medida que construyes campañas y segmentos dirigidos, es posible que descubras que ya no necesitas un evento personalizado o un atributo personalizado. Por ejemplo, si usaste un atributo personalizado específico como parte de una campaña única, puedes eliminar estos datos después de [bloquearlos](#blocklisting-custom-attributes-custom-events-and-products) y quitar sus referencias de tu aplicación. Puedes eliminar cualquier tipo de datos (como cadenas, números y atributos personalizados anidados).

{% alert important %}
Debes ser [administrador de Braze]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#admin) para eliminar datos personalizados.
{% endalert %}

Para eliminar un evento personalizado o un atributo personalizado, haz lo siguiente:

1. Ve a **Configuración de datos** > **Atributos personalizados** o **Eventos personalizados**, según el tipo de datos que quieras eliminar.
2. Ve al dato personalizado y selecciona <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**Acciones** > **Bloquear**.
3. Después de que tus datos personalizados hayan estado bloqueados durante 7 días, selecciona <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**Acciones** > **Eliminar**.

### Cómo funciona la eliminación

Cuando eliminas datos personalizados, ocurre lo siguiente:

- **Para atributos personalizados:** Elimina permanentemente los datos del atributo del perfil de cada usuario.
- **Para eventos personalizados:** Elimina permanentemente los metadatos del evento del perfil de cada usuario.

Cuando se selecciona un atributo o evento para eliminación, su estado cambia a **Descartado**. Durante los siguientes siete días, es posible restaurar el atributo o evento. Si no lo restauras después de siete días, los datos se eliminan permanentemente. Si restauras el atributo o evento, vuelve al estado de bloqueado.

La eliminación no impide el registro adicional de los objetos de datos personalizados en los perfiles de usuario, así que asegúrate de que los datos personalizados ya no se estén registrando antes de eliminar el evento o atributo.

### Cosas que debes saber

Al eliminar datos personalizados, ten en cuenta los siguientes detalles:

* **La eliminación es permanente**. Los datos no se pueden recuperar.
* Los datos se eliminan de la plataforma Braze y de los perfiles de usuario.
* Puedes "reutilizar" el nombre del atributo personalizado o del evento personalizado después de la eliminación. Esto significa que si notas que los datos personalizados "reaparecen" en Braze después de la eliminación, puede deberse a una integración que no se ha detenido y está enviando datos con el mismo nombre de datos personalizados.
* Es posible que necesites bloquear un elemento nuevamente si tu eliminación resulta en la reaparición de datos personalizados. El estado de bloqueo no se conserva porque los datos personalizados se eliminan.
* Eliminar datos personalizados no registra ningún [punto de datos]({{site.baseurl}}/user_guide/data/infrastructure/data_points) y tampoco genera nuevos puntos de datos para usar.