---
nav_title: Mapeador visual
article_title: "Ingesta de datos en la nube: Mapeador visual"
description: "Aprende a sincronizar una tabla o vista de tu almacén de datos con el mapeador visual de la ingesta de datos en la nube, sin escribir SQL."
page_order: 12
page_type: reference
toc_headers: h2
---

# Ingesta de datos en la nube: Mapeador visual {#cloud-data-ingestion-visual-mapper}

> Esta página explica cómo usar el mapeador visual para sincronizar una tabla o vista de tu almacén de datos con Braze sin escribir SQL ni reestructurar tus datos.

{% alert important %}
El mapeador visual se encuentra actualmente en fase beta. El mapeador visual está disponible para sincronizaciones de atributos de usuario desde todos los orígenes de datos de almacén de datos de la ingesta de datos en la nube, y se irán añadiendo tipos de sincronización adicionales a lo largo de la fase beta. Ponte en contacto con tu CSM or administrador de éxito de cliente or administrador de éxito de cliente o director de cuentas para obtener acceso.
{% endalert %}

Con el mapeador visual, puedes sincronizar una tabla o vista existente de tu almacén de datos sin escribir SQL ni reestructurar tus datos. En lugar de crear una tabla específica de Braze con las columnas `EXTERNAL_ID`, `UPDATED_AT` y `PAYLOAD`, mapeas las columnas de tu tabla existente a campos de Braze directamente en el panel.

## Requisitos previos {#prerequisites}

Antes de crear una sincronización con el mapeador visual, necesitarás:

- Un origen de datos de almacén de datos de ingesta de datos en la nube activo. Si aún no has configurado uno, consulta [Integraciones de almacén de datos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).
- El nombre de la tabla o vista que deseas sincronizar, tal como aparece en tu almacén de datos.
- Una columna en tu tabla que contenga un identificador de usuario compatible y una columna con una marca de tiempo que Braze pueda usar para la sincronización incremental.

{% alert note %}
Braze solo ejecuta consultas de solo lectura contra tus datos y no modifica tus tablas subyacentes. Es posible que se creen objetos temporales durante la ejecución de la consulta, pero no se conservan.
{% endalert %}

## Crear una sincronización con el mapeador visual {#creating-a-sync-with-the-visual-mapper}

### Paso 1: Configurar la sincronización {#step-1-configure-the-sync}

1. Ve a **Configuración de datos** > **Ingesta de datos en la nube** > **Sincronizaciones** y selecciona **Crear sincronización de datos**.
2. Elige un nombre para tu sincronización y selecciona un origen de datos activo. Solo se pueden usar orígenes activos.
3. En **Destino de datos**, selecciona **Braze Data Platform**.
4. En **Tipo de datos**, selecciona **Atributos de usuario**.
5. Selecciona **Siguiente: Definición de datos**.

### Paso 2: Mapear el esquema de origen {#step-2-map-your-source-schema}

1. En el paso **Definición de datos**, selecciona **Mapeador visual**.
2. En el campo **Tabla**, introduce el nombre de la tabla o vista tal como aparece en tu almacén de datos.
3. Selecciona **Mapear esquema de origen**. Braze lee el esquema de tu tabla o vista y muestra cada columna con su tipo de datos detectado.

### Paso 3: Revisar los mapeados {#step-3-review-your-mappings}

La sección **Revisar mapeado** registra dos mapeados obligatorios. Tu sincronización no se puede crear hasta que ambos estén completos:

- Mapea una columna a un identificador de usuario compatible: `external_id`, `braze_id`, `email`, `phone` o un alias de usuario. Las opciones de identificador aparecen en **Identificadores** en el menú desplegable del campo de destino.
- Mapea una columna a `updated_at`. Braze usa esta marca de tiempo para la sincronización incremental en sincronizaciones recurrentes, donde cada ejecución de sincronización importa las filas en las que `updated_at` es posterior al último valor sincronizado.

Para cada columna restante, puedes:

- **Mantener el mapeado predeterminado.** Cada columna se mapea a un campo de Braze con el mismo nombre. Si el campo aún no existe en tu espacio de trabajo, se marca como **Nuevo atributo** y se crea durante la primera ejecución de la sincronización.
- **Mapear a un campo existente.** Busca en el menú desplegable del campo de destino para mapear una columna a un atributo predeterminado o personalizado existente en tu espacio de trabajo.
- **Mapear a un campo nuevo.** Escribe directamente en el menú desplegable del campo de destino para mapear una columna a un nuevo atributo personalizado.
- **Excluir la columna.** Desmarca la casilla **Importar** para dejar una columna fuera de la sincronización.

{% alert tip %}
Antes de crear un nuevo atributo, busca uno existente en el menú desplegable de destino. Por ejemplo, si tu tabla tiene una columna `fav_color` pero tu espacio de trabajo ya registra `favorite_color`, considera mapear `fav_color` a `favorite_color` en lugar de crear otro atributo.
{% endalert %}

{% alert note %}
Los campos cuyo tipo de datos no coincide con el tipo detectado de tu columna muestran una advertencia de **Tipo no coincidente**. Puedes continuar de todos modos, pero los valores no coincidentes pueden fallar en la sincronización como errores de fila. Puedes ver los errores de fila en los detalles de ejecución de una sincronización.
{% endalert %}

### Paso 4: Vista previa y validación {#step-4-preview-and-validate}

Selecciona **Vista previa y validar** para ejecutar una comprobación de solo lectura contra tu tabla o vista. La vista previa muestra las primeras 10 filas usando los nombres de campo mapeados, e incluye solo las columnas que estás importando.

### Paso 5: Finalizar la creación de la sincronización {#step-5-finish-creating-the-sync}

1. En el paso **Notificaciones**, introduce al menos un correo electrónico de contacto para las notificaciones de errores de sincronización. Opcionalmente, puedes activar las alertas de **Error de fila** (enviadas cuando un porcentaje de filas no se actualiza) y las notificaciones de **Sincronización exitosa**.
2. En el paso **Programación**, activa **Sincronización recurrente** para ejecutar la sincronización según una programación, o déjala desactivada para una sincronización única.
3. Revisa el paso **Resumen**. Muestra tu configuración, qué atributos son nuevos frente a existentes, y cualquier columna excluida de la importación debido a problemas de tipo de datos o tus selecciones.
4. Selecciona **Crear sincronización**. También puedes seleccionar **Guardar como borrador** en cualquier paso para terminar más tarde.

## Gestión de cambios de esquema {#handling-schema-changes}

El mapeador visual comprueba el esquema de tu tabla o vista en cada ejecución de sincronización y responde según el tipo de cambio:

| Cambio en tu tabla de origen | Comportamiento de la sincronización |
|---|---|
| Se añade una nueva columna | La sincronización continúa, pero las nuevas columnas no se sincronizan automáticamente. Para incluir una, edita la sincronización y mapéala. |
| Se elimina una columna mapeada | La ejecución de la sincronización falla y la sincronización se pausa. El cambio de esquema se muestra en los detalles de ejecución de la sincronización, y tus contactos de notificación reciben una alerta por correo electrónico. |
| Se renombra una columna mapeada | Se trata como una columna eliminada más una columna nueva. |
| Cambia el tipo de datos de una columna | No se detecta como un cambio de esquema. Los valores incompatibles se reportan como errores de fila en los registros de sincronización. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gestión de cambios de esquema" }

Para reanudar una sincronización pausada después de que se elimine una columna, selecciona **Editar sincronización** y revisa tus mapeados. La columna eliminada se marca y ya no aparece en el mapeador. Guardar tus mapeados confirma que la sincronización debe continuar sin esa columna. Alternativamente, si los datos se movieron a una columna diferente, mapea la nueva columna antes de guardar.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Puedo editar mis mapeados después de crear una sincronización? {#can-i-edit-my-mappings-after-a-sync-is-created}

Sí. Edita la sincronización y selecciona **Ver y editar mapeado**. Se carga el esquema actual de la tabla de origen, con tus mapeados anteriores de la creación de la sincronización guardados. Puedes editar tus mapeados desde ahí.

### ¿Puedo transformar mis datos en el mapeador visual? {#can-i-transform-my-data-in-the-visual-mapper}

No. El mapeador visual sincroniza los valores de las columnas exactamente como aparecen en tu origen. No admite transformaciones, lógica condicional ni uniones entre tablas. Para esos casos de uso, usa la opción SQL en el paso de definición de datos para dar forma a tus datos con una consulta. Para más información, consulta [Ingesta de datos en la nube: Editor SQL]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sql_editor).

### ¿Cambian mis sincronizaciones CDI existentes? {#do-my-existing-cdi-syncs-change}

No. Las sincronizaciones que usan el formato de tabla existente con las columnas `EXTERNAL_ID`, `UPDATED_AT` y `PAYLOAD` siguen funcionando, y puedes seguir creándolas seleccionando **Tabla** en el paso **Definición de datos**. No se requiere migración.

### ¿Cómo se ve afectado mi uso de Braze? {#how-is-my-braze-usage-affected}

Cada columna que importas se escribe como una actualización de atributo, y la facturación de puntos de datos funciona igual que en otras sincronizaciones de datos de usuario de CDI. Excluir las columnas que no necesitas mantiene tus sincronizaciones eficientes. Para más información, consulta [Mejores prácticas de ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices).