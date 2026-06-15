---
nav_title: Solución de problemas
article_title: Solución de problemas de Segments
page_order: 9
page_type: reference
tool:
  - Segments
description: "Este artículo de referencia cubre pasos de solución de problemas y consideraciones a tener en cuenta al utilizar Segments."
---

# Solución de problemas de Segments {#troubleshoot-segments}

> Esta página cubre problemas comunes y preguntas que pueden surgir al crear y administrar Segments en Braze.

## Errores {#errors}

### La audiencia objetivo es demasiado compleja para lanzar {#target-audience-is-too-complex-to-launch}

Este error poco frecuente ocurre si tu audiencia objetivo contiene demasiados valores regex, valores regex excesivamente largos, filtros excesivamente detallados (como "es cualquiera de 30.000 códigos postales") o demasiados filtros. Esto incluye todos los filtros en la audiencia de una Campaign o Canvas, ya sea que los filtros estén ubicados dentro de los Segments referenciados o añadidos como filtros en el paso **Target Audience**.

![Error para una audiencia objetivo que alcanza el umbral de complejidad.]({% image_buster /assets/img/segment/target_audience_too_complex_error.png %})

Cuando añades filtros de Segment a una Campaign o Canvas, esos filtros se traducen en consultas en Braze (el recuento de caracteres de estas consultas no es 1:1 con el número de caracteres que un usuario del dashboard ve). Cuando Braze envía una Campaign o Canvas, ejecuta una consulta que combina todos los filtros en la audiencia objetivo. Aplicamos un umbral que limita el número de caracteres en la consulta resultante para una audiencia objetivo. Para una Campaign o Canvas determinado, sumamos el recuento de caracteres de todos los Segments referenciados, incluyendo todos los filtros adicionales. Para un Segment determinado, sumamos el recuento de caracteres de todos los filtros y valores de filtro.

Tu dashboard mostrará un error cuando una Campaign, Canvas o Segment exceda el umbral y no pueda lanzarse. Si recibes este error, simplifica tu audiencia objetivo antes de lanzar de nuevo, incluyendo:

- Si tu audiencia hace referencia a múltiples Segments, asegúrate de que los Segments no tengan redundancias, como los mismos filtros apareciendo en múltiples Segments.
- Asegúrate de que no estés haciendo referencia a datos obsoletos en los filtros de Segment. Por ejemplo, un filtro obsoleto podría buscar usuarios que no hayan recibido un determinado paso en Canvas en la última semana, aunque el Canvas haya estado detenido durante meses.
- Los Segments que son simplemente listas de ID de usuario o correos electrónicos (que a menudo usan un filtro regex) pueden convertirse a una [importación CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/) y simplificarse en un único filtro CSV.
- Si tienes CDI, es posible que puedas crear un Segment CDI que extraiga el grupo directamente de tu almacén de datos.

También puedes [ponerte en contacto con Soporte]({{site.baseurl}}/braze_support/) para obtener asistencia adicional con la optimización de filtros.

{% alert note %}
Comenzamos a limitar los recuentos de caracteres en abril de 2025. Las Campaigns y Canvas que se lanzaron antes de abril de 2025 estaban exentos, lo que significa que pueden seguir excediendo el límite, mientras que las Campaigns y Canvas recién creados no pueden exceder el límite. Si editas o clonas una Campaign o Canvas exento, **no podrás** lanzarlo hasta que la audiencia se actualice para estar por debajo del límite.
{% endalert %}

### X Campaigns o Canvas activos o detenidos exceden el umbral de complejidad de audiencia {#x-active-or-stopped-campaigns-or-canvases-exceed-the-audience-complexity-threshold}

Este banner se muestra en la parte superior de una lista de Campaigns o Canvas siempre que las Campaigns o Canvas activos o detenidos tengan audiencias que excedan el umbral de complejidad de audiencia. Selecciona el banner para filtrar la lista y mostrar solo las Campaigns o Canvas que exceden el umbral, luego sigue los pasos de solución de problemas en [La audiencia objetivo es demasiado compleja para lanzar](#target-audience-is-too-complex-to-launch).

![Banner de error que dice que 4 Canvas activos o detenidos exceden el umbral de complejidad de audiencia.]({% image_buster /assets/img/segment/audience_complexity_threshold_banner.png %})

### El filtro excede 10.000 bytes o es demasiado largo para guardar {#filter-exceeds-10000-bytes-or-is-too-long-to-save}

Braze limita los filtros individuales de Segment a un máximo de 10.000 bytes, lo que equivale a 10.000 caracteres en inglés o 3.333 caracteres japoneses. Aparece una advertencia siempre que un filtro individual excede 10.000 bytes, ya sea que el filtro esté dentro de un Segment o añadido directamente a una Campaign o Canvas.

![Banner de error para un filtro que tiene un valor que excede 10.000 caracteres.]({% image_buster /assets/img/segment/filter_error.png %})

![Error para un filtro de atributo personalizado, `menu_item`, que tiene un valor de atributo que excede 10.000 caracteres.]({% image_buster /assets/img/segment/segment_filter_error.png %})

Este error ocurre muy raramente, pero cuando ocurre, suele ser con filtros regex que apuntan a una lista de ID de usuario o direcciones de correo electrónico. En ese caso, puedes seguir estos pasos para convertir los filtros a un CSV:

1. Exporta los usuarios del Segment afectado o del filtro regex específico.
2. Limpia el CSV según sea necesario. Necesitas el ID de Braze o el ID de Appboy, pero puedes eliminar todas las demás columnas si no son necesarias. También recomendamos revisar tus datos para confirmar que son recientes (por ejemplo, elimina usuarios que ya no estés intentando segmentar).
3. [Importa]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/) el archivo CSV de nuevo, lo que agrupa automáticamente a los usuarios en un único filtro basado en CSV altamente eficiente.

## Comportamiento del usuario {#user-behavior}

### El usuario ya no está en un Segment {#user-is-no-longer-in-a-segment}

Si un usuario no está disponible al crear un Segment, sus datos de usuario que determinan su elegibilidad para el Segment podrían haber cambiado como resultado de su propia actividad u otras Campaigns y Canvas con los que haya interactuado previamente. Si la reelegibilidad está activada, su perfil de usuario mostrará los datos más recientes de la Campaign recibida.

### Se muestra información de usuarios de otras aplicaciones cuando filtro por una aplicación específica {#info-displays-for-users-of-other-apps-when-i-filter-for-a-specific-app}

Los usuarios pueden tener múltiples aplicaciones, por lo que seleccionar una aplicación específica en la sección **Aplicaciones utilizadas** de la página de segmentación arrojará resultados para usuarios que al menos tengan esa aplicación. El filtro no arroja resultados para los usuarios que exclusivamente tienen esa aplicación.

## Filtrado {#filtering}

### Las opciones de filtro cambiaron {#filter-options-changed}

Tus opciones de filtro están relacionadas con el formato (tipo de datos) que estás pasando a Braze para tu atributo personalizado. Para revisar el tipo de datos que Braze está reconociendo para tus atributos personalizados, ve a **Configuración de datos** > **Atributos personalizados**.

Si tus opciones de filtro han cambiado, esto es una indicación de que tus datos se están pasando a Braze en un formato (tipo de datos) diferente al anterior. Para descripciones detalladas de los diferentes tipos de datos y sus opciones de filtrado, consulta [tipos de datos de atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#custom-attribute-data-types).

Ten en cuenta que cambiar el tipo de datos de un atributo personalizado en el dashboard rechazará los datos que se envíen a Braze en un formato diferente.

## Análisis e informes {#analytics-and-reporting}

### *Mensajes enviados* o *Destinatarios únicos* en los análisis de Campaign no coincide con el recuento del Segment {#message-sent-or-unique-recipients-in-campaign-analytics-doesnt-match-segment-count}

Si el recuento de análisis de tu Campaign para *Mensajes enviados* o *Destinatarios únicos* no coincide con el número de usuarios en el filtro de Segment `Has received message from campaign X`, podría haber tres posibles razones.

1. **Los usuarios pueden haber sido archivados, huérfanos o eliminados desde el lanzamiento de la Campaign**<br><br>Por ejemplo, supongamos que 1.000 usuarios reciben una Campaign y haces una exportación CSV el mismo día. Verás 1.000 usuarios reportados. Durante el mes siguiente, 50 de esos 1.000 usuarios son eliminados (por ejemplo, mediante el punto de conexión `users/delete`). Cuando hagas otra exportación CSV, verás 950 usuarios reportados, mientras que el recuento de *Destinatarios únicos* en **Análisis de Campaign** sigue siendo 1.000.<br><br>En otras palabras, la métrica de *Destinatarios únicos* es un recuento incremental, mientras que el segmentador y la exportación CSV proporcionan un recuento de usuarios existentes actualmente.<br><br>

2. **La Campaign tiene la reelegibilidad configurada, por lo que los usuarios pueden volver a entrar en la Campaign múltiples veces**<br><br>Por ejemplo, supongamos que una Campaign de correo electrónico tiene la reelegibilidad configurada en cero minutos (los usuarios pueden volver a entrar en la Campaign siempre que cumplan con los requisitos del Segment de audiencia), y la Campaign ha estado ejecutándose durante más de un mes. El número de *Mensajes enviados* en **Análisis de Campaign** no coincidiría con el número en el Segment porque este campo incluiría mensajes enviados a usuarios duplicados.<br><br>Esto se debe a que Braze cuenta los usuarios únicos como *Destinatarios diarios únicos*, o el número de usuarios que recibieron un mensaje particular en un día. Esto significa que los usuarios reelegibles se cuentan más de una vez como destinatario único porque la ventana de "unicidad" solo dura un día. Esto puede resultar en que el número de *Destinatarios diarios únicos* sea mayor que el número de perfiles de usuario en la exportación CSV. Los perfiles de usuario en el archivo CSV son verdaderamente únicos.<br><br>

3. **Usuarios que comparten un identificador de canal coincidieron con el filtro**<br><br>El filtro `Has received message from campaign X` (y otros filtros de "recibido") puede coincidir con usuarios que comparten un identificador de canal con alguien que recibió, abrió o hizo clic en el mensaje.

### El usuario está asignado a dos aplicaciones a pesar de haber registrado una sesión en solo una aplicación {#user-is-assigned-to-two-apps-despite-logging-a-session-in-only-one-app}

Al crear un Segment, puedes segmentar usuarios que hayan [utilizado aplicaciones específicas]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#step-3-choose-your-app-or-platform). Un usuario necesita haber tenido una sesión en una aplicación específica para ser asignado a esa aplicación; sin embargo, hay dos escenarios en los que un usuario puede ser asignado a una aplicación específica sin haber registrado sesiones en la aplicación.

El primer escenario es si el campo `app_id` está poblado al usar el punto de conexión `/users/track`, específicamente al usar un [objeto de evento]({{site.baseurl}}/api/objects_filters/event_object/) o un [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/), como en este ejemplo:

```json
{
    "events": [
    {
      "external_id": "john_doe123",
      "app_id": "my_web_app_id",
      "name": "Custom Event",
      "time": "2025-08-17T19:20:30+1:00"
    }
  ]
}
```

El segundo escenario es si el campo `app_id` está poblado al usar el punto de conexión `/users/track` para migrar tokens push, como en este ejemplo:

```json
{
"app_group_id": "{YOUR_APP_GROUP_ID}",
"attributes": [
{
      "push_token_import": false,
      "external_id": "external_id1",
      "country": "US",
      "language": "en",
      "{YOUR_CUSTOM_ATTRIBUTE}": "{YOUR_VALUE}",
      "push_tokens": [
        {"app_id": "{APP_ID_OF_OS}", "token": "{PUSH_TOKEN_STRING}"}
      ]
  }
]
}
```
