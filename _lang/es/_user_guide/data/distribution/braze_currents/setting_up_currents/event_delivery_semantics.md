---
nav_title: Semántica de la entrega de eventos
article_title: Semántica de la entrega de eventos
page_order: 2
page_type: reference
description: "Este artículo de referencia describe y define cómo Currents gestiona los datos de eventos de archivos planos que enviamos a los socios de almacenamiento de almacén de datos."
tool: Currents

---

# Semántica de la entrega de eventos {#event-delivery-semantics}

> Esta página describe y define cómo Currents gestiona los datos de eventos de archivos planos que enviamos a los socios de almacenamiento de almacén de datos.

Currents para almacenamiento de datos es una transmisión continua de datos desde nuestra plataforma a un contenedor de almacenamiento en una de las [conexiones de nuestros socios]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) de almacén de datos. Currents escribe archivos Avro en tu contenedor de almacenamiento en umbrales regulares, lo que te permite procesar y analizar los datos de eventos con tu propio conjunto de herramientas de inteligencia empresarial (BI).

{% alert important %}
Este contenido **solo se aplica a los datos de eventos de archivos planos que enviamos a los socios de almacenamiento de almacén de datos (Google Cloud Storage, Amazon S3 y Microsoft Azure Blob Storage)**. <br><br>Para el contenido que se aplica a otros socios, consulta nuestra lista de [socios disponibles]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) y revisa sus respectivas páginas.
{% endalert %}

## Eventos de prueba {#test-events}

Cuando configures una integración de Currents, haz clic en **Send Test Events** para verificar la conexión con tu contenedor de almacenamiento. Estos eventos de prueba validan que tu integración puede recibir y procesar datos correctamente.

{% alert important %}
**Formato de datos de eventos de prueba:** Los eventos de prueba contienen valores de marcador de posición que coinciden con los tipos de datos correctos para cada campo, pero no contienen datos realistas ni precisos. Por ejemplo, un campo `timezone` puede contener una cadena similar a un UUID en lugar de un identificador de zona horaria válido (como "America/Chicago"), y otros campos como `campaign_name` e `ip_pool` también pueden contener valores de marcador de posición en lugar de datos reales.<br>

Este es el comportamiento esperado. Los eventos de prueba sirven principalmente para probar la conexión y la configuración de la integración, no para validar la precisión de los datos. Para ver eventos reales con datos precisos, usa una integración de Currents de prueba para enviar datos de eventos reales a través de tu pipeline.
{% endalert %}

## Entrega "al menos una vez" {#at-least-once-delivery}

Como sistema de alto rendimiento, Currents proporciona una entrega de eventos "al menos una vez", lo que significa que ocasionalmente se pueden escribir eventos duplicados en tu contenedor de almacenamiento. Esto puede ocurrir cuando los eventos se reprocesan desde nuestra cola por cualquier motivo.

Si tus casos de uso requieren una entrega "exactamente una vez", puedes usar el campo de identificador único que se envía con cada evento (`id`) para deduplicar eventos. Dado que el archivo sale de nuestro control cuando se escribe en tu contenedor de almacenamiento, no tenemos forma de garantizar la deduplicación desde nuestro lado.

## Marcas de tiempo {#timestamps}

Todas las marcas de tiempo exportadas por Currents se envían en la zona horaria UTC. Para algunos eventos en los que está disponible, también se incluye un campo de zona horaria, que entrega el formato de la Autoridad de Números Asignados de Internet (IANA) de la zona horaria local del usuario en el momento del evento.

### Latencia {#latency}

Los eventos enviados a Braze a través del SDK or kit de desarrollo de software o la API pueden incluir una marca de tiempo del pasado. El ejemplo más notable es cuando los datos del SDK or kit de desarrollo de software se ponen en cola, como cuando no hay conectividad móvil. En ese caso, la marca de tiempo del evento reflejará cuándo se generó el evento. Esto significa que un porcentaje de eventos parecerá tener una latencia alta.

## Formato Apache Avro {#apache-avro-format}

Las integraciones de almacenamiento de datos de Braze Currents generan datos en formato `.avro`. Elegimos [Apache Avro](https://avro.apache.org/) porque es un formato de datos flexible que admite de forma nativa la evolución de esquemas y es compatible con una amplia variedad de productos de datos:

- Avro es compatible con casi todos los principales almacenes de datos.
- En caso de que desees dejar tus datos en S3, Avro comprime mejor que CSV y JSON, por lo que pagas menos por almacenamiento y potencialmente puedes usar menos CPU para analizar los datos.
- Avro requiere esquemas cuando se escriben o leen datos. Los esquemas pueden evolucionar con el tiempo para manejar la adición de campos sin interrupciones.

Currents creará un archivo para cada tipo de evento usando el siguiente formato:

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>/event_type=<event-type>/date=<date>/version=<currents_version>/<environment>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>+<partition>+<offset>.avro
```

{% alert tip %}
¿No puedes ver el código por la barra de desplazamiento? Aprende cómo solucionarlo [en la página de inicio de la guía del usuario de Braze]({{site.baseurl}}/user_guide).
{% endalert %}

Por ejemplo, la ruta de un evento de envío push puede verse así:

```
currents-export/dataexport.prod-01.S3.integration.69cadaaed2d51b7c75b1a3e5/event_type=users.messages.pushnotification.Send/date=2025-04-01-17/version=6/us-01/dataexport.prod-01.S3.integration.69cadaaed2d51b7c75b1a3e5+0+123456.avro
```

El segmento de ruta `version` es un valor entero simple de la versión de Currents, como `version=6`.

| Segmento del nombre de archivo | Definición |
|---|---|
| `<your-bucket-prefix>` | El prefijo configurado para esta integración de Currents. |
| `<cluster-identifier>` | Para uso interno de Braze. Será una cadena como "prod-01", "prod-02", "prod-03" o "prod-04". Todos los archivos tendrán el mismo identificador de clúster. |
| `<connection-type-identifier>` | El identificador del tipo de conexión. Las opciones son "S3", "AzureBlob" o "GCS". |
| `<integration-id>` | El ID único para esta integración de Currents. |
| `<event-type>` | El tipo de evento en el archivo. |
| `<date>` | La hora en que los eventos se ponen en cola en nuestro sistema para su procesamiento en la zona horaria UTC. Formato YYYY-MM-DD-HH. |
| `version=<currents_version>` | La versión de Currents para la ruta del pipeline. Este valor es un entero simple como `6`. |
| `<environment>` | Para uso interno de Braze. |
| `<partition>` | Para uso interno de Braze. Entero. |
| `<offset>` | Para uso interno de Braze. Entero. Ten en cuenta que diferentes archivos enviados dentro de la misma hora tendrán un parámetro `<offset>` diferente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Formato Apache Avro" }

{% alert tip %}
Las convenciones de nomenclatura de archivos pueden cambiar. Braze recomienda buscar todas las claves en tu contenedor que tengan el prefijo &lt;your-bucket-prefix&gt;.
{% endalert %}

### Umbral de escritura de Avro {#avro-write-threshold}

En circunstancias normales, Braze escribirá archivos de datos en tu contenedor de almacenamiento cada 5 minutos o cada 15,000 eventos, lo que ocurra primero. Bajo carga pesada, podemos escribir archivos de datos más grandes con hasta 100,000 eventos por archivo.

{% alert important %}
Currents nunca escribirá archivos vacíos.
{% endalert %}

### Cambios en el esquema de Avro {#avro-schema-changes}

De vez en cuando, Braze puede realizar cambios en el esquema de Avro cuando se agregan, cambian o eliminan campos. Para nuestros propósitos aquí, hay dos tipos de cambios: con ruptura y sin ruptura. Todos los cambios de esquema se agrupan en versiones de Currents, y cada versión avanza el segmento `version=<currents_version>` en la ruta de almacenamiento (por ejemplo, de `version=6` a `version=7`). Los eventos de Currents escritos en Azure Blob Storage, Google Cloud Storage y Amazon S3 usan el siguiente formato de ruta:

```
<your-bucket-prefix>/<currents-integration-id>/event_type=<event-type>/date=<date>/version=<currents_version>/<environment>/<avro-file>
```

#### Cambios sin ruptura {#non-breaking-changes}

Cuando se agrega un campo al esquema de Avro, lo consideramos un cambio sin ruptura. Los campos agregados siempre serán campos Avro "opcionales" (como con un valor predeterminado de `null`), por lo que "coincidirán" con esquemas más antiguos según la [especificación de resolución de esquemas de Avro](http://avro.apache.org/docs/current/spec.html#schema+resolution). Estas adiciones no deberían afectar los procesos existentes de extracción, transformación y carga (ETL or extraer, transformar, cargar), ya que el campo simplemente se ignorará hasta que se agregue a tu proceso ETL or extraer, transformar, cargar.

{% alert important %}
Recomendamos que tu configuración de ETL or extraer, transformar, cargar sea explícita sobre los campos que procesa para evitar interrupciones en el flujo cuando se agregan nuevos campos.
{% endalert %}

#### Cambios con ruptura {#breaking-changes}

Cuando se elimina o cambia un campo en el esquema de Avro, lo consideramos un cambio con ruptura. Los cambios con ruptura pueden requerir modificaciones en los procesos ETL or extraer, transformar, cargar existentes, ya que los campos que estaban en uso pueden dejar de registrarse como se esperaba.

Todos los cambios con ruptura se comunicarán con anticipación antes del lanzamiento.

Para un historial completo de cambios por versión, consulta el [registro de cambios de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs).