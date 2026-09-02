---
nav_title: Comparar opciones de ingesta de datos
article_title: Comparar opciones de ingesta de datos persistentes y de copia cero
page_order: 1
page_type: reference
description: "Compara las sincronizaciones estándar de ingesta de datos en la nube, los CDI Segments, los activadores CDI de Canvas y la API /users/track para elegir cómo los datos de tu almacén o aplicación llegan a los perfiles, Segments y Canvas de Braze."
---

# Comparar opciones de ingesta de datos persistentes y de copia cero {#compare-persistent-and-zero-copy-data-ingestion-options}

> Elige cómo los datos de tu almacén o aplicaciones llegan a Braze, ya sea que se copien en los perfiles de usuario, se consulten en su lugar para la segmentación o se pasen de forma transitoria a un Canvas, antes de diseñar tus pipelines de ingesta.

## Acerca de este ejemplo {#about-this-example}

MovieCanon es un servicio ficticio de streaming de películas. Centraliza los datos de clientes, entradas y visualizaciones en un almacén. El equipo de datos debe decidir cómo alimentar Braze para tres necesidades comunes:

- **Datos de perfil:** nivel de fidelización, LTV y atributos de preferencia de género o formato que persisten en los perfiles de usuario de Braze.
- **Creación de audiencias:** segmentos basados en SQL a partir de tablas del almacén sin copiar cada columna en Braze.
- **Mensajería activada:** filas del almacén que deben entrar en un Canvas con personalización a nivel de fila que no necesita vivir en el perfil.

Braze ofrece cuatro rutas principales de ingesta. Las sincronizaciones estándar de ingesta de datos en la nube (CDI) y la API [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) persisten datos en los perfiles. Los CDI Segments (fuentes conectadas) y los activadores CDI de Canvas son opciones de copia cero: los datos del almacén permanecen en tu almacén y no se escriben en los perfiles de usuario de Braze.

Utiliza esta comparación cuando estés planificando la arquitectura, dimensionando el rendimiento o explicando las ventajas y desventajas a las partes interesadas de ingeniería y marketing. No reemplaza las guías de configuración de integración de cada opción.

## Consideraciones {#considerations}

- La ingesta de datos en la nube es una característica general. Las sincronizaciones CDI estándar copian datos en los perfiles de Braze (similar a `/users/track`). Los CDI Segments y los activadores CDI de Canvas mantienen los datos del almacén en su lugar sin escribirlos en los perfiles de usuario de Braze.
- Las sincronizaciones CDI recurrentes pueden ejecutarse desde cada 15 minutos hasta una vez al mes. Si necesitas una cadencia superior a 15 minutos, contacta a tu CSM o utiliza la ingesta por REST API. Consulta [Ingesta de datos en la nube de Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).
- Los activadores CDI de Canvas comparten el límite de velocidad de la REST API [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) con otro tráfico hacia ese endpoint. `/users/track` tiene sus propios límites y reglas de procesamiento por lotes. Los límites predeterminados pueden aumentarse. Ve a **Configuración** > **API e identificadores** > **Límites de API** y consulta [Límites de velocidad de API]({{site.baseurl}}/api/api_limits).
- Las fuentes conectadas y las extensiones de segmento CDI ejecutan consultas en tu almacén. Incurres en costos de computación del almacén; Braze no registra puntos de datos para esas consultas. Consulta [Fuentes conectadas]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources).

## Configuración {#setup}

### Paso 1: Mapea tu caso de uso a una ruta de ingesta {#step-1-map-your-use-case-to-an-ingestion-path}

Relaciona tu objetivo con la ruta de ingesta recomendada y si esa ruta escribe en los perfiles de Braze.

| Tu objetivo | Ruta recomendada | ¿Escribe en perfiles? |
| --- | --- | --- |
| Persistir atributos, eventos, compras o elementos de catálogo desde el almacén | Sincronización CDI estándar | Sí (los datos se copian en los perfiles o catálogos de Braze) |
| Crear audiencias a partir de SQL del almacén sin copiar las tablas de origen en Braze | CDI Segments (fuentes conectadas) | No (solo membresía) |
| Hacer que los usuarios entren en un Canvas con contexto de fila del almacén que no debe persistir en el perfil | Activadores CDI de Canvas | No (propiedades de contexto de Canvas transitorias) |
| Enviar datos desde aplicaciones, servidores o pipelines de streaming en tiempo casi real | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) (o SDK) | Sí (los datos persisten en los perfiles) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mapea tu caso de uso a una ruta de ingesta" }

### Paso 2: Compara persistencia, latencia y rendimiento {#step-2-compare-persistence-latency-and-throughput}

Compara cómo cada ruta gestiona la residencia de datos, la latencia, el rendimiento y la creación de usuarios.

| Dimensión | Sincronización CDI estándar | CDI Segments | Activadores CDI de Canvas | `/users/track` |
| --- | --- | --- | --- | --- |
| Qué hace | Lectura programada de una tabla del almacén; escribe atributos, eventos, compras, eliminaciones de usuarios o catálogos | Braze consulta tu almacén para extensiones de segmento SQL | Las filas del almacén desencadenan la entrada a un Canvas con contexto de fila como propiedades de contexto de Canvas | Las aplicaciones, servidores o pipelines de streaming escriben atributos, eventos y compras en los perfiles |
| Residencia de datos | Copiados y persistidos en los perfiles de Braze | Permanecen en tu almacén; nada se escribe en los perfiles | Las propiedades de contexto de Canvas son transitorias; no persisten en los perfiles | Copiados y persistidos en los perfiles de Braze |
| Latencia típica | No es en tiempo real; cadencia mínima de sincronización de 15 minutos (también aplica la frescura del almacén) | No es en tiempo real; se actualiza según el programa de tu extensión de segmento (la membresía no se actualiza con cada cambio del almacén) | No es en tiempo real; limitada por el programa de sincronización (mínimo 15 minutos) | Casi en tiempo real (procesamiento asíncrono) |
| Notas de rendimiento | Resultado completo de la consulta por sincronización; Braze procesa internamente por lotes hacia `/users/track`, `/users/delete` o endpoints de catálogos | Límite de tiempo de ejecución de consulta de 60 minutos por fuente conectada; sin límite de objetos por solicitud | Comparte el límite de velocidad de `/canvas/trigger/send`; aproximadamente 3,75 millones de entradas a Canvas por hora por ejecución de sincronización | Hasta 75 objetos combinados por solicitud; consulta [Límites de velocidad de API]({{site.baseurl}}/api/api_limits) |
| Tamaño de lote | Sin límite de objetos en el lado CDI para lecturas del almacén | N/A (la salida de la consulta define la membresía) | Una entrada a Canvas por fila del almacén por ejecución de sincronización | 75 atributos, eventos y compras combinados por solicitud (predeterminado) |
| Creación de usuarios | Sí, a menos que se configure solo actualizar existentes | No (los usuarios desconocidos en los resultados de la consulta se ignoran) | No (solo usuarios existentes de Braze) | Sí, a menos que `_update_existing_only` sea true |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Compara persistencia, latencia y rendimiento" }

### Paso 3: Compara los requisitos de esquema e identificadores {#step-3-compare-schema-and-identifier-requirements}

Compara las columnas requeridas y los identificadores soportados para cada ruta. Configura un tipo de datos por sincronización CDI estándar (por ejemplo, atributos en una integración y eventos en otra).

| Dimensión | Sincronización CDI estándar | CDI Segments | Activadores CDI de Canvas | `/users/track` |
| --- | --- | --- | --- | --- |
| Columnas requeridas / formato | Identificador de usuario + `UPDATED_AT` + `PAYLOAD` (JSON) por fila | El SQL debe devolver solo `external_user_id` | Identificador + `UPDATED_AT` + `PROPERTIES` (JSON; usa `{}` cuando esté vacío) | Cuerpo de solicitud estándar de `/users/track` |
| Identificadores soportados | `external_id`, alias de usuario, `braze_id`, correo electrónico o teléfono | Solo `external_user_id` (cadena) | Solo `external_id` o alias de usuario | `external_id`, alias de usuario, `braze_id`, correo electrónico o teléfono |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Compara los requisitos de esquema e identificadores" }

### Paso 4: Implementa la ruta que seleccionaste {#step-4-implement-the-path-you-selected}

- **Sincronización CDI estándar:** Crea una tabla o vista del almacén y luego sigue [Integraciones de ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations) y [Configuración de tablas]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup).
- **CDI Segments:** Agrega una [fuente conectada]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) y luego crea una [extensión de segmento CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments).
- **Activadores CDI de Canvas:** Configura una tabla de origen con `PROPERTIES`, crea y lanza un Canvas de destino y luego crea una sincronización siguiendo [Personalización de copia cero usando CDI]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync).
- **`/users/track`:** Envía solicitudes desde tu aplicación o middleware. Formatea las cargas útiles según [POST: Crear y actualizar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

Para MovieCanon, un patrón común es: sincronizaciones CDI estándar para el enriquecimiento nocturno de perfiles, CDI Segments para reglas de audiencia exclusivas del almacén, activadores de Canvas para recorridos de estado de entradas o visualización con contexto a nivel de fila, y `/users/track` para eventos de aplicación en tiempo real.

## Artículos relacionados {#related-articles}

- [Ingesta de datos en la nube de Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)
- [Fuentes conectadas]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources)
- [Personalización de copia cero usando CDI]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync)
- [Extensiones de segmento CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments)
- [Configuración de tablas para ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup)
- [POST: Crear y actualizar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_track)
- [Límites de velocidad de API]({{site.baseurl}}/api/api_limits)