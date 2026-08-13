---
nav_title: Solución de problemas
article_title: Solución de problemas de Segments
page_order: 9
page_type: reference
tool:
  - Segments
description: "Este artículo de referencia cubre la solución de problemas para errores de Segments, elegibilidad de usuarios, problemas con filtros y discrepancias en los análisis. Para definiciones de filtros, consulta Filtros de segmentación. Para estimaciones de tamaño de Segments y recuentos exactos, consulta Medir el tamaño de un Segment."
---

# Solución de problemas de Segments {#troubleshoot-segments}

> Busca tu síntoma en la siguiente lista para encontrar la sección correcta. Esta página cubre errores de lanzamiento, elegibilidad de usuarios, problemas con filtros y discrepancias en los análisis. Para definiciones de filtros, consulta [Filtros de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters). Para estimaciones de tamaño de Segments, recuentos exactos y gráficos de membresía histórica, consulta [Medir el tamaño de un Segment]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size).

## Empieza aquí: identifica tu síntoma {#start-here-match-your-symptom}

| Síntoma | Ir a |
|---------|-------|
| La audiencia es demasiado compleja | [El público objetivo es demasiado complejo para lanzar](#target-audience-is-too-complex-to-launch) |
| El filtro no se guarda | [El filtro supera los 10.000 bytes](#filter-exceeds-10000-bytes-or-is-too-long-to-save) |
| El Segment no tiene usuarios | [El Segment muestra cero usuarios](#segment-shows-zero-users) |
| El usuario no está en el Segment | [Ruta de investigación estándar](#standard-investigation-path) |
| El Segment es más grande de lo esperado | [El Segment es mucho más grande de lo esperado](#segment-is-much-larger-than-expected) |
| El recuento del Segment no coincide con los análisis de Campaign | [Discrepancia en *Mensajes enviados* o *Destinatarios únicos*](#message-sent-or-unique-recipients-in-campaign-analytics-doesnt-match-segment-count) |
| Las opciones de filtro cambiaron | [Las opciones de filtro cambiaron](#filter-options-changed) |
| El atributo personalizado anidado no está disponible como filtro | [El atributo personalizado anidado no está disponible como opción de filtro](#nested-custom-attribute-not-available-as-a-filter-option) |
| El usuario está en la aplicación incorrecta | [Se muestra información de usuarios de otras aplicaciones](#info-displays-for-users-of-other-apps-when-i-filter-for-a-specific-app) |
| ¿Estaba un usuario en este Segment en un momento pasado? | [Pertenencia retroactiva al Segment](#retroactive-segment-membership) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Empieza aquí: identifica tu síntoma" }

## Ruta de investigación estándar {#standard-investigation-path}

Usa este flujo de trabajo cuando un usuario debería estar en un segmento pero no lo está, o cuando el recuento de un segmento parece incorrecto.

1. **Lanzamiento bloqueado:** Si ves un error de complejidad de audiencia o de filtro de 10.000 bytes en una Campaign o Canvas, empieza por [Errores](#errors) (solución alternativa con CSV, simplificación de filtros).
2. **Vista previa de usuario o búsqueda de usuario:** Prueba un usuario específico contra los filtros de tu segmento. Cuando un usuario no coincide con parte o la totalidad de los criterios, los criterios faltantes se enumeran para la solución de problemas. Para ver los pasos, consulta [Probar segmentos]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments) en Crear un segmento.
3. **Calcular estadísticas exactas:** Si la estimación del segmento muestra 0 usuarios o parece incorrecta, selecciona **Calculate exact stats** en el panel **Reachable users**. Guarda tu segmento antes de calcular. Si ya hay un cálculo en curso, espera a que termine; los números obsoletos pueden mostrarse hasta que se complete el nuevo cálculo. Para más detalles, consulta [Calcular estadísticas exactas]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#calculating-exact-statistics).
4. **Comprobar valores de filtro:** Busca errores tipográficos, discrepancias de tipo de datos, referencias obsoletas a pasos en Canvas y [lógica de filtro negativo + OR](#segment-is-much-larger-than-expected).
5. **Comprobar complejidad:** Si el lanzamiento está bloqueado, consulta [El público objetivo es demasiado complejo para lanzar](#target-audience-is-too-complex-to-launch).
6. **Contactar con soporte:** Si sigues bloqueado, ponte en contacto con [soporte de Braze]({{site.baseurl}}/braze_support).

## El Segment muestra cero usuarios {#segment-shows-zero-users}

El tamaño de un Segment en el panel suele ser una estimación basada en una muestra de usuarios. Los Segments muy pequeños pueden mostrar un rango estimado que incluye 0, incluso cuando hay usuarios que coinciden con tus filtros.

- Selecciona **Calculate exact stats** en el panel **Reachable users** para obtener un recuento preciso. Guarda primero el Segment. Para más información, consulta [Consideraciones sobre los recuentos estimados]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#considerations-for-estimate-counts).
- Si **User Preview** devuelve cero usuarios para un Segment pequeño, eso no significa necesariamente que el Segment esté vacío. Ejecuta **Calculate exact stats** para confirmarlo. Para más información, consulta [Vista previa de usuarios]({{site.baseurl}}/user_guide/audience/segments/segment_data#user-preview).

## Pertenencia retroactiva a Segments {#retroactive-segment-membership}

Braze no almacena el historial de pertenencia a Segments por usuario. No puedes consultar si un usuario específico estaba en un Segment en un momento de envío pasado.

Para capturar la pertenencia en un momento determinado, exporta los usuarios del Segment en el panel o llama al endpoint [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) antes de enviar una Campaign o un Canvas. Para más información, consulta [Filtros de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) (filtro de pertenencia a Segment) y [Exportar datos de Segment a CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv).

## Errores {#errors}

### El público objetivo es demasiado complejo para lanzar {#target-audience-is-too-complex-to-launch}

Este error poco frecuente ocurre si tu público objetivo contiene demasiados valores regex, valores regex excesivamente largos, filtros excesivamente detallados (como "es cualquiera de 30.000 códigos postales") o demasiados filtros. Esto incluye todos los filtros en la audiencia de una Campaign o Canvas, ya sea que los filtros estén ubicados dentro de los Segments referenciados o añadidos como filtros en el paso **Target Audience**.

![Error para un público objetivo que alcanza el umbral de complejidad.]({% image_buster /assets/img/segment/target_audience_too_complex_error.png %})

Cuando añades filtros de Segment a una Campaign o Canvas, esos filtros se traducen en consultas en Braze (el recuento de caracteres de estas consultas no es 1:1 con el número de caracteres que un usuario del panel ve). Cuando Braze envía una Campaign o Canvas, ejecutamos una consulta que combina todos los filtros en la audiencia objetivo. Aplicamos un umbral que limita el número de caracteres en la consulta resultante para un público objetivo. Para una Campaign o Canvas determinado, sumamos el recuento de caracteres en todos los Segments referenciados, incluyendo todos los filtros adicionales. Para un Segment determinado, sumamos el recuento de caracteres en todos los filtros y valores de filtro.

Tu panel mostrará un error cuando una Campaign, Canvas o Segment supere el umbral y no pueda lanzarse. Si recibes este error, simplifica tu público objetivo antes de volver a lanzar, incluyendo:

- Si tu audiencia hace referencia a múltiples Segments, asegúrate de que los Segments no tengan redundancias, como los mismos filtros apareciendo en múltiples Segments.
- Asegúrate de que no estés haciendo referencia a datos obsoletos en los filtros de Segment. Por ejemplo, un filtro obsoleto podría buscar usuarios que no hayan recibido un determinado paso en Canvas en la última semana, aunque el Canvas haya estado detenido durante meses.
- Los Segments que son solo listas de ID de usuario o correos electrónicos (que a menudo usan un filtro regex) pueden convertirse en una [importación CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) y simplificarse en un único filtro CSV.
- Si tienes CDI, es posible que puedas crear un Segment CDI que extraiga el grupo directamente de tu almacén de datos.

También puedes [contactar con soporte]({{site.baseurl}}/braze_support) para obtener más ayuda con la optimización de filtros.

{% alert note %}
Comenzamos a limitar los recuentos de caracteres en abril de 2025. Las Campaigns y Canvas que se lanzaron antes de abril de 2025 estaban exentos, lo que significa que pueden seguir superando el límite, mientras que las Campaigns y Canvas recién creados no pueden superar el límite. Si editas o clonas una Campaign o Canvas exento, no podrás lanzarlo hasta que la audiencia se actualice para estar por debajo del límite.
{% endalert %}

### X Campaigns o Canvas activos o detenidos superan el umbral de complejidad de audiencia {#x-active-or-stopped-campaigns-or-canvases-exceed-the-audience-complexity-threshold}

Este banner se muestra en la parte superior de una lista de Campaigns o Canvas siempre que las Campaigns o Canvas activos o detenidos tengan audiencias que superen el umbral de complejidad de audiencia. Selecciona el banner para filtrar la lista y mostrar solo las Campaigns o Canvas que superan el umbral, luego sigue los pasos de solución de problemas en [El público objetivo es demasiado complejo para lanzar](#target-audience-is-too-complex-to-launch).

![Banner de error que dice que 4 Canvas activos o detenidos superan el umbral de complejidad de audiencia.]({% image_buster /assets/img/segment/audience_complexity_threshold_banner.png %})

### El filtro supera los 10.000 bytes o es demasiado largo para guardar {#filter-exceeds-10000-bytes-or-is-too-long-to-save}

Braze limita los filtros individuales de Segment a un máximo de 10.000 bytes, lo que equivale a 10.000 caracteres en inglés o 3.333 caracteres en japonés. Aparece una advertencia siempre que un filtro individual supere los 10.000 bytes, ya sea que el filtro esté dentro de un Segment o añadido directamente a una Campaign o Canvas.

![Banner de error para un filtro que tiene un valor que supera los 10.000 caracteres.]({% image_buster /assets/img/segment/filter_error.png %})

![Error para un filtro de atributo personalizado, `menu_item`, que tiene un valor de atributo que supera los 10.000 caracteres.]({% image_buster /assets/img/segment/segment_filter_error.png %})

Este error ocurre muy raramente, pero cuando ocurre, suele ser con filtros regex que apuntan a una lista de ID de usuario o direcciones de correo electrónico. En ese caso, puedes seguir estos pasos para convertir los filtros a un CSV:

1. Exporta los usuarios del Segment afectado o del filtro regex específico.
2. Limpia el CSV según sea necesario. Necesitas el ID de Braze o el ID de Appboy, pero puedes eliminar todas las demás columnas si no son necesarias. También recomendamos revisar tus datos para confirmar que son recientes (por ejemplo, elimina usuarios a los que ya no intentas dirigirte).
3. [Importa]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) el archivo CSV de nuevo, lo que agrupa automáticamente a los usuarios en un único filtro basado en CSV altamente eficiente.

## Comportamiento del usuario {#user-behavior}

### El usuario ya no está en un segmento {#user-is-no-longer-in-a-segment}

Si un usuario no está disponible al crear un segmento, es posible que sus datos de usuario que determinan su elegibilidad para el segmento hayan cambiado como resultado de su propia actividad u otras Campaigns y Canvas con los que haya interactuado previamente. Si la reelegibilidad está activada, su perfil de usuario muestra los datos más recientes de la Campaign recibida.

Para comprobar si un usuario específico coincide con tu segmento hoy, utiliza [la vista previa de usuario o la búsqueda de usuarios]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments).

### Se muestra información de usuarios de otras aplicaciones cuando filtro por una aplicación específica {#info-displays-for-users-of-other-apps-when-i-filter-for-a-specific-app}

Los usuarios pueden tener varias aplicaciones, por lo que seleccionar una aplicación específica en la sección **Aplicaciones utilizadas** de la página de segmentación mostrará resultados de usuarios que al menos tienen esa aplicación. El filtro no muestra resultados de los usuarios que tienen exclusivamente esa aplicación.

## Filtrado {#filtering}

### Las opciones de filtro cambiaron {#filter-options-changed}

Tus opciones de filtro están relacionadas con el formato (tipo de datos) que estás pasando a Braze para tu atributo personalizado. Para revisar el tipo de datos que Braze está reconociendo para tus atributos personalizados, ve a **Configuración de datos** > **Atributos personalizados**.

Si tus opciones de filtro han cambiado, esto indica que tus datos se están pasando a Braze en un formato (tipo de datos) diferente al anterior. Para descripciones detalladas de los diferentes tipos de datos y sus opciones de filtrado, consulta [tipos de datos de atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types).

Ten en cuenta que cambiar el tipo de datos de un atributo personalizado en el panel rechaza los datos que se envían a Braze en un formato diferente. No puedes cambiar el tipo de datos de un atributo personalizado mientras ese atributo esté referenciado en Campaigns, Canvas o Segments activos; el panel muestra un error y bloquea el cambio.

La pestaña **Valores** de un atributo personalizado muestra resultados de una muestra de aproximadamente 250.000 usuarios. No uses la pestaña **Valores** para confirmar si existe un valor de atributo específico para la solución de problemas. Para más información, consulta [Pestaña de valores]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#values-tab).

### El atributo personalizado anidado no está disponible como opción de filtro {#nested-custom-attribute-not-available-as-a-filter-option}

Si tu atributo personalizado anidado no aparece como opción de filtro al crear un segmento, primero genera su esquema. Ve a **Configuración de datos** > **Atributos personalizados**, busca el atributo y selecciona **Generar esquema**. Una vez generado, el atributo estará disponible en el menú desplegable de filtros del segmento. Para más información, consulta [Generar un esquema usando el explorador de objetos anidados]({{site.baseurl}}/user_guide/audience/segments/segment_with_nested_custom_attributes#generate-schema).

### El segmento es mucho más grande de lo esperado {#segment-is-much-larger-than-expected}

Si tu segmento parece mucho más grande de lo que esperas a pesar de que los filtros parecen restrictivos, comprueba si estás usando filtros negativos (`is not`, `does not equal`, `does not match regex` o `not included`) con el operador **OR** en el mismo atributo más de una vez. Esa combinación puede dirigirse a usuarios con todos los valores del atributo.

Para orientación sobre cuándo usar **AND** en lugar de **OR**, consulta [Cuándo evitar el operador OR]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#segmentation-logic-using-and-and-or) en Crear un segmento.

## Análisis e informes {#analytics-and-reporting}

### *Mensajes enviados* o *Destinatarios únicos* en los análisis de Campaign no coincide con el recuento del segmento {#message-sent-or-unique-recipients-in-campaign-analytics-doesnt-match-segment-count}

Si el recuento de los análisis de tu Campaign para *Mensajes enviados* o *Destinatarios únicos* no coincide con el número de usuarios en el filtro de segmento `Has received message from campaign X`, podría haber tres posibles razones.

1. **Es posible que los usuarios hayan sido archivados, huérfanos o eliminados desde el lanzamiento de la Campaign**<br><br>Por ejemplo, supongamos que 1000 usuarios reciben una Campaign y haces una exportación CSV el mismo día. Verás 1000 usuarios reportados. Durante el mes siguiente, 50 de esos 1000 usuarios son eliminados (por ejemplo, mediante el endpoint `users/delete`). Cuando hagas otra exportación CSV, verás 950 usuarios reportados, mientras que el recuento de *Destinatarios únicos* en **Campaign Analytics** sigue siendo 1000.<br><br>En otras palabras, la métrica *Destinatarios únicos* es un recuento incremental, mientras que el segmentador y la exportación CSV proporcionan un recuento de los usuarios que existen actualmente.<br><br>

2. **La Campaign tiene configurada la reelegibilidad, por lo que los usuarios pueden volver a entrar en la Campaign varias veces**<br><br>Por ejemplo, supongamos que una Campaign de correo electrónico tiene la reelegibilidad configurada en cero minutos (los usuarios pueden volver a entrar en la Campaign siempre que cumplan los requisitos del segmento de audiencia), y la Campaign ha estado activa durante más de un mes. El número de *Mensajes enviados* en **Campaign Analytics** no coincidiría con el número en el segmento porque este campo incluiría mensajes enviados a usuarios duplicados.<br><br>Esto se debe a que Braze cuenta los usuarios únicos como *Destinatarios únicos diarios*, o el número de usuarios que recibieron un mensaje particular en un día. Esto significa que los usuarios reelegibles se cuentan más de una vez como destinatario único porque la ventana de "unicidad" solo dura un día. Esto puede hacer que el número de *Destinatarios únicos diarios* sea mayor que el número de perfiles de usuario en la exportación CSV. Los perfiles de usuario en el archivo CSV son verdaderamente únicos.<br><br>

3. **Usuarios que comparten un identificador de canal coincidieron con el filtro**<br><br> El filtro `Has received message from campaign X` (y otros filtros de "recibido") puede coincidir con usuarios que comparten un identificador de canal, como el mismo token de notificaciones push o dirección de correo electrónico, con otro perfil de usuario que recibió, abrió o hizo clic en el mensaje.

### Un usuario está asignado a dos aplicaciones a pesar de haber registrado una sesión en solo una aplicación {#user-is-assigned-to-two-apps-despite-logging-a-session-in-only-one-app}

Al crear un segmento, puedes dirigirte a usuarios que han [utilizado aplicaciones específicas]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#step-3-choose-your-app-or-platform). Un usuario necesita haber tenido una sesión en una aplicación específica para ser asignado a esa aplicación; sin embargo, hay dos escenarios en los que un usuario puede ser asignado a una aplicación específica sin haber registrado sesiones en ella.

El primer escenario es si el campo `app_id` está completado al usar el endpoint `/users/track`, específicamente al usar un [objeto de evento]({{site.baseurl}}/api/objects_filters/event_object) o un [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object), como en este ejemplo:

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

El segundo escenario es si el campo `app_id` está completado al usar el endpoint `/users/track` para migrar tokens de notificaciones push, como en este ejemplo:

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
