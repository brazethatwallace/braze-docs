---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre el uso compartido de datos de Snowflake
page_order: 50
page_type: FAQ
description: "Este artículo responde a las preguntas más frecuentes sobre el uso compartido de datos de Snowflake."

---

# Preguntas más frecuentes {#frequently-asked-questions}

### ¿Es posible ofuscar datos PII mediante el uso compartido de datos de Snowflake? {#is-it-possible-to-obfuscate-pii-data-via-snowflake-data-sharing}
No, por ahora no se admite.

### ¿Necesito compartir datos de la misma región o de otras regiones? {#do-i-need-data-share-for-the-same-region-or-cross-region}
Utiliza el uso compartido de datos para la misma región en los siguientes escenarios:
- Tu cuenta de Snowflake está en US-EAST-1 (AWS) y la región de tu panel de Braze está en EE. UU.
- Tu región de Snowflake está en EU-CENTRAL-1 (AWS) y la región de tu panel de Braze está en la UE.
- Tu región de Snowflake está en AP-Northeast-1 (AWS) y la región de tu panel de Braze está en Japón.
- Tu región de Snowflake está en AP-Southeast-2 (AWS) y la región de tu panel de Braze está en Australia.
- Tu región de Snowflake está en AP-Southeast-3 (AWS) y la región de tu panel de Braze está en Indonesia.

Si no, utiliza el uso compartido de datos entre regiones.

### ¿Qué debo hacer con mi recurso compartido de datos cuando cambie a una nueva cuenta de Snowflake? {#what-should-i-do-with-my-data-share-when-i-switch-to-a-new-snowflake-account}
Puedes eliminar el antiguo recurso compartido de datos asociado a tu antigua cuenta de Snowflake y, a continuación, crear un nuevo recurso compartido para la nueva cuenta. Todos los datos históricos estarán disponibles en el nuevo recurso compartido.

### ¿Por qué no veo datos en mi recurso compartido de datos? {#why-dont-i-see-data-in-my-data-share}
Puede que hayas utilizado un ID de cuenta de Snowflake incorrecto al crear tu recurso compartido de datos. El ID de cuenta del dashboard de uso compartido de datos debe coincidir con la salida de `CURRENT_ACCOUNT()` de tu cuenta de Snowflake.

Si tu recurso compartido es entre regiones, puede que los datos no estén disponibles de inmediato. Dependiendo de tu volumen de datos, la sincronización de datos a tu región puede tardar unas horas.

### ¿Por qué recibo un error de cumplimiento de la HIPAA al crear un recurso compartido de datos? {#why-am-i-receiving-a-hipaa-compliance-error-when-creating-a-data-share}

La cuenta especificada no cumple la HIPAA o está en [ediciones de Snowflake](https://docs.snowflake.com/en/user-guide/intro-editions) inferiores a Business Critical. Tu cuenta de Snowflake debe actualizarse a la edición Business Critical para cumplir con la HIPAA y poder compartir datos. Ponte en contacto con el soporte de Snowflake si necesitas ayuda para actualizar tu cuenta.

### ¿Por qué no puedo volver a crear un recurso compartido de datos después de eliminar uno? {#why-cant-i-recreate-a-data-share-after-deleting-one}

Es posible que el sistema aún esté procesando la eliminación de tu anterior recurso compartido de datos. Espera unos minutos a que finalice el proceso de desaprovisionamiento y vuelve a intentar crear el nuevo recurso compartido de datos.

### ¿Cuántas veces tengo que ejecutar `CREATE DATABASE` cuando tengo varios espacios de trabajo que comparten datos con la misma cuenta de Snowflake? {#how-many-times-do-i-need-to-run-create-database-when-i-have-multiple-workspaces-sharing-data-to-the-same-snowflake-account}

Solo tienes que ejecutar `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` una vez. Cuando se comparten varios recursos compartidos de datos de diferentes espacios de trabajo de Braze a la misma cuenta de Snowflake, se combinan automáticamente en el mismo recurso compartido. Después de crear la base de datos inicial, los datos de los espacios de trabajo adicionales se añaden automáticamente a la base de datos existente sin necesidad de solicitudes de uso compartido adicionales ni pasos de creación de bases de datos.

Por ejemplo, si creas un recurso compartido de datos a la cuenta 123 de Snowflake desde el espacio de trabajo A, aceptas la solicitud de uso compartido y creas una base de datos. Cuando más tarde crees un recurso compartido de datos a la misma cuenta 123 de Snowflake desde el espacio de trabajo B, no se enviará ninguna nueva solicitud de recurso compartido: los datos se añadirán inmediatamente al recurso compartido existente y estarán disponibles en la base de datos creada anteriormente.

### Si tengo varios espacios de trabajo, ¿una sola base de datos contiene los datos de todos ellos? {#if-i-have-multiple-workspaces-does-a-single-database-contain-data-from-all-of-them}

Sí. Cuando compartes datos de varios espacios de trabajo de Braze a la misma cuenta de Snowflake, todos los datos se combinan en un único recurso compartido y están disponibles en la misma base de datos. Puedes filtrar los datos por `app_group_id` para distinguir entre espacios de trabajo.

Como práctica recomendada, filtra siempre por `app_group_id` en tus consultas para que estén preparadas para el futuro. Esto garantiza que tus dashboards e informes sigan siendo precisos si añades espacios de trabajo adicionales en el futuro. Sin este filtro, tus métricas pueden incluir inesperadamente datos de espacios de trabajo recién añadidos.

### ¿Cuál es el enfoque recomendado para gestionar los datos de varios espacios de trabajo en Snowflake? {#what-is-the-recommended-approach-for-managing-data-from-multiple-workspaces-in-snowflake}

Envía todos los datos de Braze a la misma base de datos y filtra por `app_group_id` para distinguir entre espacios de trabajo. Este enfoque simplifica la gestión de los datos y garantiza la coherencia de los informes en toda la organización.

### ¿Cuántos conectores de Snowflake Data Share necesito para varios espacios de trabajo? {#how-many-snowflake-data-share-connectors-do-i-need-for-multiple-workspaces}

El número de conectores que necesitas depende de tu configuración específica y de tus derechos. Ponte en contacto con tu equipo de cuentas de Braze para obtener más información sobre qué derechos son adecuados para tu caso de uso.

### ¿Qué opciones existen para aislar los datos de diferentes espacios de trabajo dentro de la misma cuenta de Snowflake? {#what-options-exist-for-isolating-data-from-different-workspaces-within-the-same-snowflake-account}

Puedes aislar lógicamente utilizando la columna `app_group_id`, que identifica a qué espacio de trabajo pertenece cada fila de datos. Los enfoques más comunes son:

- **Vistas (recomendado):** Crea una vista para cada espacio de trabajo filtrada por `app_group_id`. Esto evita duplicar datos y al mismo tiempo ofrece a cada equipo o caso de uso una vista limpia y delimitada de los datos de su espacio de trabajo.
- **Copias de tablas locales:** Copia los datos en tablas separadas filtradas por `app_group_id`. Esto duplica los datos, por lo que generalmente se prefiere el enfoque de vistas.
- **Políticas de acceso a filas y roles:** Utiliza las políticas de acceso a filas nativas de Snowflake combinadas con roles para restringir qué filas puede consultar cada rol. Esto mantiene los datos en una sola tabla mientras aplica el control de acceso en el momento de la consulta.

Configuras todo esto dentro de tu cuenta de Snowflake.

### ¿Puedo usar una cuenta de Snowflake diferente para aislar los datos de diferentes espacios de trabajo? {#can-i-use-a-different-snowflake-account-to-isolate-data-from-different-workspaces}

Sí. Si el espacio de trabajo A comparte con la cuenta X y el espacio de trabajo B comparte con la cuenta Y, cada cuenta recibe un recurso compartido independiente con datos separados. Sin embargo, la mayoría de las organizaciones utilizan una sola cuenta de Snowflake para todos los datos empresariales. Por lo tanto, este enfoque puede añadir sobrecarga operativa. Considera esta compensación antes de elegirlo en lugar de los enfoques de aislamiento lógico descritos en la sección anterior.

### ¿Es el aislamiento de datos por espacio de trabajo un caso de uso compatible con el uso compartido de datos de Snowflake? {#is-workspace-data-isolation-a-supported-use-case-for-snowflake-data-sharing}

Sí, a través de los enfoques de aislamiento lógico descritos en las secciones anteriores. Braze no crea recursos compartidos separados para cada espacio de trabajo, por lo que gestionas el aislamiento a nivel de Snowflake utilizando vistas, políticas de acceso a filas o cuentas separadas.