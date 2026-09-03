---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre el uso compartido de datos de Snowflake
page_order: 50
page_type: FAQ
description: "Este artículo responde a las preguntas más frecuentes sobre el uso compartido de datos de Snowflake."

---

# Preguntas más frecuentes {#frequently-asked-questions}

## ¿Es posible ofuscar datos PII a través del uso compartido de datos de Snowflake? {#is-it-possible-to-obfuscate-pii-data-via-snowflake-data-sharing}
No, por el momento eso no es compatible.

## ¿Necesito compartir datos en la misma región o entre regiones? {#do-i-need-data-share-for-the-same-region-or-cross-region}
Usa el uso compartido de datos en la misma región en los siguientes escenarios:
- Tu cuenta de Snowflake está en US-EAST-1 (AWS) y la región de tu panel de Braze está en EE. UU.
- Tu región de Snowflake está en EU-CENTRAL-1 (AWS) y la región de tu panel de Braze está en la UE.
- Tu región de Snowflake está en AP-Northeast-1 (AWS) y la región de tu panel de Braze está en Japón.
- Tu región de Snowflake está en AP-Southeast-2 (AWS) y la región de tu panel de Braze está en Australia.
- Tu región de Snowflake está en AP-Southeast-3 (AWS) y la región de tu panel de Braze está en Indonesia.

De lo contrario, usa el uso compartido de datos entre regiones.

## ¿Qué debo hacer con mi recurso compartido de datos cuando cambio a una nueva cuenta de Snowflake? {#what-should-i-do-with-my-data-share-when-i-switch-to-a-new-snowflake-account}
Puedes eliminar el recurso compartido de datos antiguo asociado a tu cuenta de Snowflake anterior y luego crear uno nuevo para la nueva cuenta. Todos los datos históricos estarán disponibles en el nuevo recurso compartido.

## ¿Qué ocurre si cambio mi recurso compartido de datos a un nuevo espacio de trabajo de Braze? {#what-happens-if-i-switch-my-data-share-to-a-new-braze-workspace}

Si reconfiguras una integración de recurso compartido de datos existente para usar un espacio de trabajo de Braze diferente, es posible que veas este error en Snowflake al consultar tablas:

> Shared database is no longer available for use. It will need to be re-created if and when the publisher makes it available again.

Para resolver esto, necesitas eliminar y recrear el recurso compartido dentro de Snowflake:

1. Elimina la base de datos que se creó con el recurso compartido anterior.
2. Crea la base de datos de nuevo siguiendo las [instrucciones de integración]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake#step-2-create-the-database-in-snowflake).
3. Vuelve a otorgar los privilegios de acceso necesarios a la nueva base de datos.
4. Recrea cualquier vista (si aplica) que hiciera referencia a la base de datos anterior.

{% alert note %}
En la nueva interfaz de Snowflake, puedes encontrar el recurso compartido de Braze en **Data Products** > **Private Sharing** > **Shared with you**.
{% endalert %}

## ¿Por qué no veo datos en mi recurso compartido de datos? {#why-dont-i-see-data-in-my-data-share}
Es posible que hayas utilizado el ID de cuenta de Snowflake incorrecto al crear tu recurso compartido de datos. El ID de cuenta en el panel de uso compartido de datos debe coincidir con la salida de `CURRENT_ACCOUNT()` de tu cuenta de Snowflake.

Si tu recurso compartido es entre regiones, es posible que los datos no estén disponibles de inmediato. Dependiendo del volumen de tus datos, la sincronización a tu región podría tardar unas horas.

## ¿Por qué recibo un error de cumplimiento HIPAA al crear un recurso compartido de datos? {#why-am-i-receiving-a-hipaa-compliance-error-when-creating-a-data-share}

La cuenta especificada no cumple con HIPAA o se encuentra en [ediciones de Snowflake](https://docs.snowflake.com/en/user-guide/intro-editions) inferiores a Business Critical. Tu cuenta de Snowflake debe actualizarse a la edición Business Critical para cumplir con HIPAA en el uso compartido de datos. Contacta con el soporte de Snowflake para obtener más ayuda con la actualización de tu cuenta.

## ¿Por qué no puedo recrear un recurso compartido de datos después de eliminar uno? {#why-cant-i-recreate-a-data-share-after-deleting-one}

El sistema puede estar aún procesando la eliminación de tu recurso compartido de datos anterior. Espera unos minutos a que se complete el proceso de desaprovisionamiento y luego intenta crear el nuevo recurso compartido de datos de nuevo.

## ¿Cuántas veces necesito ejecutar `CREATE DATABASE` cuando tengo varios espacios de trabajo compartiendo datos en la misma cuenta de Snowflake? {#how-many-times-do-i-need-to-run-create-database-when-i-have-multiple-workspaces-sharing-data-to-the-same-snowflake-account}

Solo necesitas ejecutar `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` una vez. Cuando varios data shares de diferentes espacios de trabajo de Braze se comparten en la misma cuenta de Snowflake, se combinan automáticamente en el mismo share. Después de crear la base de datos inicial, los datos de espacios de trabajo adicionales se añaden automáticamente a la base de datos existente sin necesidad de solicitudes de share adicionales ni pasos de creación de bases de datos.

Por ejemplo, si creas un data share en la cuenta de Snowflake 123 desde el espacio de trabajo A, aceptas la solicitud de share y creas una base de datos. Cuando más adelante creas un data share en la misma cuenta de Snowflake 123 desde el espacio de trabajo B, no se envía ninguna nueva solicitud de share: los datos se añaden inmediatamente al share existente y quedan disponibles en la base de datos creada previamente.

## Si tengo varios espacios de trabajo, ¿una sola base de datos contiene datos de todos ellos? {#if-i-have-multiple-workspaces-does-a-single-database-contain-data-from-all-of-them}

Sí. Cuando compartes datos de varios espacios de trabajo de Braze con la misma cuenta de Snowflake, todos los datos se combinan en un único recurso compartido y están disponibles en la misma base de datos. Puedes filtrar los datos por `app_group_id` para distinguir entre espacios de trabajo.

Como práctica recomendada, filtra siempre por `app_group_id` en tus consultas para prepararlas de cara al futuro. Esto garantiza que tus paneles e informes sigan siendo precisos si añades espacios de trabajo adicionales en el futuro. Sin este filtro, tus métricas podrían incluir inesperadamente datos de espacios de trabajo recién añadidos.

## ¿Cuál es el enfoque recomendado para gestionar datos de múltiples espacios de trabajo en Snowflake? {#what-is-the-recommended-approach-for-managing-data-from-multiple-workspaces-in-snowflake}

Envía todos los datos de Braze a la misma base de datos y filtra por `app_group_id` para distinguir entre espacios de trabajo. Este enfoque simplifica la gestión de datos y garantiza informes consistentes en toda tu organización.

## ¿Cuántos conectores de Snowflake Data Share necesito para varios espacios de trabajo? {#how-many-snowflake-data-share-connectors-do-i-need-for-multiple-workspaces}

El número de conectores que necesitas depende de tu configuración y derechos específicos. Contacta con tu equipo de cuenta de Braze para obtener más información sobre qué derechos son los adecuados para tu caso de uso.

## ¿Qué opciones existen para aislar datos de diferentes espacios de trabajo dentro de la misma cuenta de Snowflake? {#what-options-exist-for-isolating-data-from-different-workspaces-within-the-same-snowflake-account}

Puedes aislar lógicamente usando la columna `app_group_id`, que identifica a qué espacio de trabajo pertenece cada fila de datos. Los enfoques más comunes son:

- **Vistas (recomendado):** Crea una vista para cada espacio de trabajo filtrada por `app_group_id`. Esto evita duplicar datos y al mismo tiempo ofrece a cada equipo o caso de uso una vista limpia y delimitada de los datos de su espacio de trabajo.
- **Copias de tablas locales:** Copia los datos en tablas separadas filtradas por `app_group_id`. Esto duplica los datos, por lo que generalmente se prefiere el enfoque de vistas.
- **Políticas de acceso a filas y roles:** Usa políticas de acceso a filas nativas de Snowflake combinadas con roles para restringir qué filas puede consultar cada rol. Esto mantiene los datos en una sola tabla mientras aplica el control de acceso en el momento de la consulta.

Configuras estas opciones dentro de tu cuenta de Snowflake.

## ¿Puedo usar una cuenta de Snowflake diferente para aislar datos de distintos espacios de trabajo? {#can-i-use-a-different-snowflake-account-to-isolate-data-from-different-workspaces}

Sí. Si el espacio de trabajo A comparte con la cuenta X y el espacio de trabajo B comparte con la cuenta Y, cada cuenta recibe un recurso compartido independiente con datos separados. Sin embargo, la mayoría de las organizaciones utilizan una única cuenta de Snowflake para todos los datos del negocio. Por lo tanto, este enfoque puede añadir sobrecarga operativa. Considera esta compensación antes de elegirlo en lugar de los enfoques de aislamiento lógico descritos en la sección anterior.

## ¿El aislamiento de datos del espacio de trabajo es un caso de uso compatible con Snowflake Data Sharing? {#is-workspace-data-isolation-a-supported-use-case-for-snowflake-data-sharing}

Sí, a través de los enfoques de aislamiento lógico descritos en las secciones anteriores. Braze no crea recursos compartidos separados para cada espacio de trabajo, por lo que gestionas el aislamiento a nivel de Snowflake utilizando vistas, políticas de acceso a filas o cuentas separadas.