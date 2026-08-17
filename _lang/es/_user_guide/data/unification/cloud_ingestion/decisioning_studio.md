---
nav_title: Sincronizar datos de Decisioning Studio
article_title: "Sincronizar datos de BrazeAI Decisioning Studio"
description: "Aprende a sincronizar tablas de almacén de datos con BrazeAI Decisioning Studio mediante la ingesta de datos en la nube."
page_order: 6.5
page_type: reference
toc_headers: h2
---

# Sincronizar datos de BrazeAI Decisioning Studio {#sync-brazeai-decisioning-studio-data}

> Esta página explica cómo sincronizar datos de tu almacén de datos directamente con BrazeAI Decisioning Studio™ mediante la ingesta de datos en la nube (CDI).

Con el destino de Decisioning Studio de CDI, CDI también puede sincronizar datos del almacén directamente con BrazeAI Decisioning Studio. Los datos de estas sincronizaciones se ponen a disposición de Decisioning Studio para su activación, pero tus perfiles de usuario y espacios de trabajo de Braze permanecen sin cambios.

{% alert important %}
Esta característica se encuentra en acceso anticipado. Ponte en contacto con tu administrador de éxito de cliente o director de cuentas para obtener acceso.
{% endalert %}

## Cómo funciona {#how-it-works}

Cuando creas una sincronización, elige Decisioning Studio como destino y escribe una consulta SQL que devuelva los datos que deseas sincronizar. CDI ejecuta esa consulta según la programación que configures y entrega los resultados como un activo de Decisioning Studio. Cada sincronización se asigna a un único activo, por lo que no puedes apuntar más de una sincronización al mismo activo.

A diferencia de las sincronizaciones con la plataforma de datos de Braze, las sincronizaciones de Decisioning Studio no asignan tus datos a perfiles de usuario, eventos ni catálogos.

Para conocer otras formas de poner datos a disposición de Decisioning Studio, consulta [Conectar tus datos]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/connect_data_sources).

## Requisitos previos {#prerequisites}

- Acceso a Braze y BrazeAI Decisioning Studio.
- Un origen de datos de almacén de datos de ingesta de datos en la nube activo. Si aún no has configurado uno, consulta [Integraciones de almacén de datos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).
- La tabla o vista que deseas sincronizar.
- Una columna (o columnas) en esa tabla para usar como clave primaria, y una columna de marca de tiempo que CDI pueda usar para la sincronización incremental.

## Crear una sincronización de Decisioning Studio {#create-a-decisioning-studio-sync}

### Paso 1: Crear la sincronización y seleccionar el destino {#step-1-create-the-sync-and-select-the-destination}

1. Ve a **Data Settings** > **Cloud Data Ingestion** > **Syncs**.
2. Selecciona **Create data sync**.
3. Introduce un **Integration Name** y luego selecciona tu origen en **Data sources**.
4. En **Destination**, establece **Data destination** en **BrazeAI Decisioning Studio™**.
5. En **Data category**, selecciona el tipo de **Decisioning Studio data** que mejor se ajuste a tu tabla. Elige entre **Customer profile**, **Message engagement events**, **Conversion events** u **Other**. Esto etiqueta los datos para Decisioning Studio y no cambia la forma en que CDI procesa tus filas.

### Paso 2: Escribir tu consulta SQL {#step-2-write-your-sql-query}

En el paso **Data definition**, escribe una consulta SQL que devuelva los datos de la tabla o vista que deseas sincronizar. El resultado de la consulta se convierte en el esquema de tu sincronización.

Puedes usar el explorador de orígenes para examinar las tablas y vistas disponibles, o el generador de SQL con IA para obtener ayuda al escribir tu consulta.

Tu consulta debe devolver una columna `UPDATED_AT`, ya que CDI utiliza `UPDATED_AT` para la sincronización incremental y el seguimiento de cambios. En cada ejecución de sincronización, CDI sincroniza solo las filas en las que `UPDATED_AT` es posterior al último valor sincronizado. Si la columna de marca de tiempo que identificaste no se llama `UPDATED_AT`, puedes asignarle un alias en tu consulta:

```sql
SELECT *, LAST_MODIFIED AS UPDATED_AT FROM my_table
```

Para más información sobre cómo `UPDATED_AT` controla la sincronización incremental, incluido lo que sucede cuando lo retrocedes, consulta [Comprender la columna UPDATED_AT]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices#understanding-the-updated_at-column).

{% alert note %}
Solo se admiten consultas de lectura de una sola sentencia, incluidas las cláusulas `JOIN`. CDI ejecuta consultas de solo lectura y no modifica tus tablas subyacentes.
{% endalert %}

### Paso 3: Previsualizar y validar tu consulta {#step-3-preview-and-validate-your-query}

Selecciona **Preview and validate** para ejecutar tu consulta. La sección **Query preview (first 10 rows)** muestra las primeras 10 filas devueltas desde tu origen, junto con el tipo de datos detectado de cada columna, para que puedas confirmar que los datos son correctos antes de continuar.

### Paso 4: Seleccionar una clave primaria {#step-4-select-a-primary-key}

Cada sincronización de Decisioning Studio necesita una clave primaria o compuesta: una o más columnas que identifiquen de forma única cada fila. Después de que la validación sea exitosa, abre el desplegable **Primary key** y selecciona una columna que sirva como clave primaria. Seleccionar varias columnas forma una clave compuesta.

{% alert tip %}
Una buena clave primaria es única para cada fila, nunca está vacía y es estable entre ejecuciones de sincronización. Evita valores generados en el momento de la consulta, como `UUID()` o `CURRENT_TIMESTAMP`, ya que pueden causar filas duplicadas o eliminadas.
{% endalert %}

### Paso 5: Configurar notificaciones, programación y crear la sincronización {#step-5-set-notifications-schedule-and-create-the-sync}

1. En el paso **Notifications**, introduce uno o más **Contact Email(s)** para recibir notificaciones de errores de sincronización. También puedes activar las notificaciones de **Row Error** y **Sync success**.
2. En el paso **Schedule**, activa **Recurring sync** para ejecutar la sincronización automáticamente según una programación. Con **Recurring sync** desactivado, la sincronización se ejecuta solo cuando la activas, ya sea manualmente desde el panel o a través del endpoint [Trigger a sync]({{site.baseurl}}/api/endpoints/cdi/post_job_sync).
3. Revisa el **Summary** y luego crea la sincronización.

## Editar una sincronización {#editing-a-sync}

Cuando editas una sincronización existente, cualquier cambio en tu consulta SQL requiere revalidación antes de que puedas guardar. Las claves primarias y compuestas no se pueden cambiar y deben seguir devolviéndose.

Los cambios válidos surten efecto en la siguiente ejecución de sincronización.

## Gestión de cambios de esquema {#handling-schema-changes}

CDI gestiona los cambios de esquema del origen de forma aditiva. En cada ejecución de sincronización, CDI compara el esquema de tu origen con el activo existente de Decisioning Studio y añade cualquier columna nueva mientras conserva las que ya existen.

| Cambio en tu tabla de origen | Comportamiento de la sincronización |
|---|---|
| Se añade una nueva columna | CDI añade la columna al activo de Decisioning Studio. Las filas entregadas antes de que existiera la columna muestran `null` para ella. |
| Se elimina una columna | CDI deja de actualizar esa columna, pero la columna y sus datos existentes permanecen en el activo. Las demás columnas siguen sincronizándose. |
| Se renombra una columna | Se trata como una columna eliminada más una columna nueva. La columna original permanece en el activo y la nueva columna se añade. |
| Cambia el tipo de datos de una columna | CDI convierte los valores cuando puede. Las filas que no puede convertir se reportan como errores de fila en los detalles de ejecución de la sincronización. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gestión de cambios de esquema" }

Cuando CDI detecta un cambio de esquema, se muestra en los detalles de ejecución de la sincronización y en la página de edición de la sincronización, y tus contactos de notificación reciben una alerta por correo electrónico. Para cambiar qué columnas se entregan, actualiza tu consulta SQL y vuelve a validar.