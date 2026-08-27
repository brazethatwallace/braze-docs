---
nav_title: Puntos de datos
article_title: Puntos de datos
page_order: 3
page_type: reference
description: "Este artículo de referencia describe qué son los puntos de datos en Braze y cómo puedes estar al tanto de su uso."
search_rank: 6
---

# Puntos de datos {#data-points}

> En Braze, los datos significan acción: cada dato que llega a Braze actualiza la pertenencia a un segmento, puede desencadenar y cancelar la mensajería, está disponible inmediatamente para la personalización de la mensajería, y mucho más. Los puntos de datos te ayudan a definir la información más impactante para tu negocio. Al considerar cuidadosamente qué información rastrear, te aseguras de que estás apuntando a los datos de mayor impacto para la experiencia de tus usuarios.

Los puntos de datos se basan en la información registrada en los perfiles de usuario. Puedes encontrar un desglose más detallado de esta definición en tu contrato con Braze. Nuestro equipo de éxito del cliente puede ayudarte a recomendar las mejores prácticas de datos que se ajusten a tus necesidades.

## Definición {#definition}

"Puntos de datos" se refiere a una unidad facturable de uso de los servicios de Braze, medida por un inicio de sesión, un fin de sesión, un evento personalizado o una compra registrada, así como cualquier atributo establecido en el perfil de un usuario final. Para mayor claridad, cada uno de los datos mencionados anteriormente en esta sección (como inicio de sesión, fin de sesión, evento personalizado o compra registrada, así como cualquier atributo) establecido en el perfil de un usuario final en un momento dado contará como un único punto de datos.

Los datos y eventos recopilados de forma predeterminada por los servicios de Braze, incluidos, por ejemplo, los tokens de notificaciones push, la información del dispositivo y todos los eventos de seguimiento de participación en Campaigns, como las aperturas de correo electrónico y los clics en notificaciones push, *no* se cuentan como puntos de datos.

Consulta la sección [Recuento de consumo](#consumption-count) de este artículo para comprender qué datos se contabilizan en tu asignación de puntos de datos.

## Visualización del uso de puntos de datos {#viewing-data-point-usage}

Para ver el uso de tus puntos de datos, ve a **Configuración** > **Facturación** y selecciona la pestaña **Uso total de puntos de datos**.

### Programación de actualización de puntos de datos {#data-point-refresh-schedule}

El uso de puntos de datos se almacena en caché (no es en tiempo real) cada 24 horas, aproximadamente a las 2 a. m. ET. Hasta que se actualice la caché, los distintos usuarios del panel pueden ver los mismos totales aunque abran la pestaña en momentos diferentes del mismo día. Para conocer el mismo comportamiento de almacenamiento en caché en otras vistas de facturación, consulta [Panel de puntos de datos totales]({{site.baseurl}}/user_guide/administer/global/billing#total-data-points-dashboard).

Para obtener más información sobre los componentes del panel de puntos de datos, consulta [Facturación]({{site.baseurl}}/user_guide/administer/global/billing).

{% alert tip %}
**¡No desperdicies puntos de datos! ¡Actualiza solo los datos que cambian!**<br><br>
Para minimizar el uso de puntos de datos, te recomendamos configurar un programa que evite enviar los mismos datos sin cambios y que solo pase datos nuevos y relevantes a Braze. Braze trabajará contigo para establecer esta práctica recomendada durante la incorporación.
{% endalert %}

## Recuento de consumo {#consumption-count}

En resumen, los puntos de datos se acumulan cuando se actualizan los datos del perfil de un usuario o cuando este realiza acciones específicas. Básicamente, los puntos de datos son recuentos de los `session starts`, `session ends`, `events` y `purchases` de cada usuario.

Puedes encontrar un desglose de cómo Braze acumula puntos de datos en las siguientes secciones. Si alguna vez tienes preguntas sobre los matices de los puntos de datos de Braze, tu director de cuentas de Braze puede resolverlas.

Para la ingesta por API, cada actualización facturable a través de [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) sigue las mismas reglas que otras actualizaciones de perfil: por ejemplo, cada **evento personalizado** registrado cuenta como un punto de datos, y los **atributos personalizados** generalmente cuentan por atributo actualizado en esa solicitud (consulta las tablas de facturación en la siguiente sección y las [circunstancias especiales](#special-circumstances)).

Las siguientes acciones no registran puntos de datos:
- Eliminar usuarios de Braze
- Usar contenido conectado en la mensajería
- Cambios de estado de suscripción a nivel global y en los grupos de suscripción
- Renombrar los ID externos de tus usuarios mediante [llamadas a la API]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename)
- Bloquear eventos, atributos o propiedades del evento

### Circunstancias especiales {#special-circumstances}

#### Arrays {#arrays}

Un array es una colección ordenada de elementos almacenados dentro de un atributo personalizado. Actualizar un array cuesta un punto de datos por llamada a la API, incluso si el array no cambia realmente. Por ejemplo, enviar una operación `remove` para un valor que no existe en el array aún consume un punto de datos. De manera similar, establecer un atributo personalizado como `null` para eliminarlo del perfil consume un punto de datos. Si agregas valores a un array de forma incremental, contará como un punto de datos por valor.

{% alert tip %}
Para arrays simples, si estableces el array completo de una sola vez, contará como un único punto de datos. Por lo tanto, los arrays son una gran herramienta para mantener los perfiles de usuario actualizados con información relevante y reducir costos. <br><br> Los arrays de objetos consumen un punto de datos por cada clave que se actualiza. Reduce el consumo innecesario de puntos de datos enviando solo las actualizaciones a Braze.
{% endalert %}

#### Atributos personalizados anidados {#nested-custom-attributes}

Los atributos personalizados anidados hacen referencia a un objeto que define un conjunto de atributos como propiedad de otro atributo. Cada clave del objeto contará como un punto de datos.

{% alert note %}
Actualizar un objeto de atributo personalizado a `null` también consume un punto de datos.
{% endalert %}

#### CSV

Los atributos personalizados cargados mediante importación de CSV cuentan para tus puntos de datos. Sin embargo, las importaciones de CSV con fines de segmentación (importaciones realizadas con `external_id`, `braze_id` o `user_alias_name` como único campo) no registrarán puntos de datos.

Además, como los cambios de estado de suscripción no registran puntos de datos, actualizar los campos `email_subscribe`, `push_subscribe`, `subscription_group_id` o `subscription_state` en tu archivo CSV no generará cargos.

## Puntos de datos

{% alert note %}
Las siguientes tablas son ilustrativas. Para conocer las convenciones exactas de nomenclatura, uso de mayúsculas y valores aceptados para determinados campos, consulta la documentación correspondiente a tu método de ingesta.
{% endalert %}

{% tabs %}
{% tab No facturables %}

### Puntos de datos no facturables (predeterminados) {#non-billable-data-points-default}

<div class="small_table"></div>

| Tipo de datos | Punto de datos |
| --------- | ---------- |
| Datos de perfil | País |
| Datos de perfil | Idioma |
| Datos de perfil | ID de usuario |
| Datos de perfil | Alias de usuario |
| Dispositivos recientes | Número de dispositivos |
| Dispositivos recientes | Reloj más reciente |
| Dispositivos recientes | Versión de la aplicación |
| Dispositivos recientes | Dispositivo |
| Dispositivos recientes | SO del dispositivo |
| Configuración de contacto | Suscrito a correo electrónico |
| Configuración de contacto | Suscrito a push |
| Configuración de contacto | Aplicaciones registradas para push |
| Configuración de contacto | Grupo de suscripción |
| Campaigns recibidas | Dirección de correo electrónico |
| Atribución de instalación | Fuente de instalación |
| Atribución de instalación | Campaign |
| Atribución de instalación | Grupo de anuncios |
| Atribución de instalación | Anuncio |
| Otros | Número de contenedor aleatorio |
| Mensajes de Canvas recibidos | Mensajes de Canvas recibidos |
| Participación en mensajes | Todos los eventos de participación (como aperturas, clics, impresiones y descartes) |
| Twitter | Seguidores |
| Twitter | Siguiendo |
| Twitter | Número de tweets |
| Facebook | Me gusta |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Puntos de datos no facturables (predeterminados)" }

{% endtab %}
{% tab Facturables %}

### Puntos de datos facturables {#billable-data-points}

{% alert important %}
Agregar, eliminar o actualizar los siguientes tipos de datos generará un punto de datos facturable.
{% endalert %}

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 30%;
}
table th:nth-child(3) {
    width: 50%;
}
table td {
    word-break: break-word;
}
</style>

| Tipo de datos | Punto de datos | Notas |
| --------- | ---------- | ----- |
| Datos de perfil | Nombre | |
| Datos de perfil | Apellido | |
| Datos de perfil | Dirección de correo electrónico | |
| Datos de perfil | Género | |
| Datos de perfil | Grupo de edad | |
| Datos de perfil | País | Cuando se recopila manualmente. No se contabiliza en el consumo cuando se recopila automáticamente. |
| Datos de perfil | Ciudad | |
| Datos de perfil | Idioma | Cuando se recopila manualmente. No se contabiliza en el consumo cuando se recopila automáticamente. |
| Datos de perfil | Configuración regional del dispositivo más reciente | |
| Datos de perfil | Zona horaria | |
| Datos de perfil | Fecha de nacimiento (DOB) | |
| Datos de perfil | Biografía | |
| Datos de perfil | Número de teléfono | |
| Datos de uso de la aplicación | Inicio de sesión | |
| Datos de uso de la aplicación | Fin de sesión | |
| Atributos personalizados | Todos los atributos personalizados | |
| Eventos personalizados | Todos los eventos personalizados | |
| Propiedades del evento personalizado | Todas las propiedades del evento personalizado | Las propiedades del evento personalizado habilitadas para la segmentación con los filtros `X Custom Event Property in Y Days` o `X Purchase Property in Y Days` se contabilizan como puntos de datos independientes, además del punto de datos contabilizado por el propio evento personalizado. |
| Compras | Todas las compras | |
| Propiedades de la compra | Todas las propiedades de la compra | |
| Asignación de cohorte de Amplitude | Todas las asignaciones | |
| Asignación de cohorte de Mixpanel | Todas las asignaciones | |
| Asignación de cohorte de Hightouch | Todas las asignaciones | |
| Asignación de cohorte de Appsflyer | Todas las asignaciones | |
| Ubicación más reciente | Todas las ubicaciones más recientes | Entrar o salir de geovallas no registra puntos de datos, ya que los datos de geovallas no se almacenan en el perfil de usuario. Las geovallas son supervisadas por los servicios de ubicación de Apple y Google; Braze solo recibe una notificación cuando un usuario activa una geovalla. |
| Twitter | Nombre de usuario | |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Puntos de datos facturables" }

{% endtab %}
{% endtabs %}