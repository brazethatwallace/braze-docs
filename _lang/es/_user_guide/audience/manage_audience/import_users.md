---
nav_title: Importar usuarios
article_title: Importar usuarios
page_order: 3
description: "Conoce las distintas opciones de importación de usuarios de Braze, como la importación por CSV, REST API, Ingesta de datos de Cloud y más."

---
# Importar usuarios {#import-users}

> Conoce las distintas opciones de importación de usuarios de Braze, como la importación por CSV, REST API, Ingesta de datos de Cloud y más.

## Opciones de importación {#import-options}

Puedes cargar atributos de usuario y eventos a través de una importación CSV en Braze, un script de importación CSV Lambda S3 sin servidor, llamadas directas a la API o Ingesta de datos de Cloud desde tu almacén de datos.

### Importación CSV de Braze {#braze-csv-import}

Puedes usar la importación CSV para registrar y actualizar los siguientes atributos de usuario y eventos personalizados. Para empezar, consulta [Importación CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/).

| Tipo | Definición | Ejemplo | Tamaño máximo de archivo |
|---|---|---|---|
| Atributos predeterminados | Atributos de usuario reservados reconocidos por Braze. | `first_name`, `email` | 500 MB |
| Atributos personalizados | Atributos de usuario exclusivos de tu empresa. | `last_destination_searched` | 500 MB |
| Eventos personalizados | Eventos exclusivos de tu empresa que representan acciones de los usuarios. | `trip_booked` | 50 MB |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Importación CSV de Braze" }

#### Construir tu CSV {#constructing-your-csv}

Braze acepta datos de usuario en formato CSV estándar. Las importaciones de atributos predeterminados y personalizados admiten archivos de hasta 500 MB; las importaciones de eventos personalizados admiten archivos de hasta 50 MB. Para identificadores, encabezados de columna, reglas de validación y ejemplos, consulta [Importación CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import/).

Cuando cargas un CSV grande a través de **Import Users** en el dashboard, la página puede parecer que no responde o responder lentamente mientras Braze recibe el archivo y ejecuta el paso de cálculo. Deja que la carga y el cálculo terminen; el tiempo total varía de unos minutos a unas horas dependiendo del tamaño del archivo, y los archivos más grandes tardan más en calcularse.

{% alert note %}
Al importar eventos personalizados con propiedades, debes usar la notación de punto en los encabezados de columna de tu CSV. Para más información sobre el formato de eventos personalizados, consulta [Comprender el formato de eventos personalizados]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/?tab=custom%20events#understanding-custom-event-formatting).
{% endalert %}

### Importación CSV Lambda de usuarios {#lambda-user-csv-import}

Usa nuestro script de importación CSV Lambda S3 sin servidor para cargar atributos de usuario a Braze. Esta solución funciona como un cargador de CSV donde depositas tus archivos CSV en un contenedor de S3, y los scripts los cargan a través de nuestra API.

Los tiempos de ejecución estimados para un archivo con 1 000 000 de filas deberían ser de alrededor de cinco minutos. Consulta [Importación de atributos de usuario CSV a Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/) para más información.

### REST API

Usa el [punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para registrar eventos personalizados, atributos de usuario y compras para los usuarios.

### Ingesta de datos de Cloud {#cloud-data-ingestion}

Usa la [Ingesta de datos de Cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/) de Braze para importar y mantener atributos de usuario.

## Validación de HTML {#html-validation}

Ten en cuenta que Braze no sanea, valida ni reformatea los datos HTML durante la importación, lo que significa que las etiquetas de script deben eliminarse de todos los datos de importación que uses para personalización web.

Al importar datos a Braze que están específicamente destinados a la personalización en un navegador web, asegúrate de que estén libres de HTML, JavaScript o cualquier otra etiqueta de script que potencialmente pueda aprovecharse de forma maliciosa cuando se renderice en un navegador web.

Alternativamente, para HTML, puedes usar los filtros Liquid de Braze (`strip_html`) para eliminar el HTML del texto renderizado. Por ejemplo:

{% tabs local %}
{% tab Entrada %}
{% raw %}
```liquid
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
```
{% endraw %}
{% endtab %}
{% tab Salida %}
{% raw %}
```liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}