---
nav_title: Importar usuarios
article_title: Importar usuarios
page_order: 3
description: "Conoce las distintas opciones de importación de usuarios de Braze, como la importación por CSV, REST API, Ingesta de datos de Cloud y más."

---
# Importar usuarios {#import-users}

> Conoce las distintas opciones de importación de usuarios de Braze, como la importación por CSV, REST API, Ingesta de datos de Cloud y más.

## Opciones de importación {#import-options}

Puedes cargar atributos de usuario y eventos a través de una importación CSV en Braze, un script de importación CSV Lambda S3 sin servidor, llamadas directas a la API o la ingesta de datos en la nube desde tu almacén de datos.

### Importación CSV de Braze {#braze-csv-import}

Puedes utilizar la importación CSV para registrar y actualizar los siguientes atributos de usuario y eventos personalizados. Para comenzar, consulta [Importación CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import).

| Tipo | Definición | Ejemplo | Tamaño máximo de archivo |
|---|---|---|---|
| Atributos predeterminados | Atributos de usuario reservados reconocidos por Braze. | `first_name`, `email` | 500 MB |
| Atributos personalizados | Atributos de usuario exclusivos de tu negocio. | `last_destination_searched` | 500 MB |
| Eventos personalizados | Eventos exclusivos de tu negocio que representan acciones del usuario. | `trip_booked` | 50 MB |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Importación CSV de Braze" }

#### Construir tu CSV {#constructing-your-csv}

Braze acepta datos de usuario en formato CSV estándar. Las importaciones de atributos predeterminados y personalizados admiten archivos de hasta 500 MB; las importaciones de eventos personalizados admiten archivos de hasta 50 MB. Para obtener información sobre identificadores, encabezados de columna, reglas de validación y ejemplos, consulta [Importación CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import).

Cuando cargas un CSV grande a través de **Import Users** en el panel, la página puede parecer que no responde o responder lentamente mientras Braze recibe el archivo y ejecuta el paso de cálculo. Deja que la carga y el cálculo finalicen: el tiempo total varía de unos pocos minutos a unas pocas horas dependiendo del tamaño del archivo, y los archivos más grandes tardan más en calcularse.

{% alert note %}
Al importar eventos personalizados con propiedades, debes utilizar la notación de punto en los encabezados de columna de tu CSV. Para obtener más información sobre el formato de eventos personalizados, consulta [Comprender el formato de eventos personalizados]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import?tab=custom%20events#understanding-custom-event-formatting).
{% endalert %}

### Importación CSV Lambda de usuarios {#lambda-user-csv-import}

Utiliza nuestro script de importación CSV Lambda S3 sin servidor para cargar atributos de usuario en Braze. Esta solución funciona como un cargador de CSV en el que depositas tus archivos CSV en un contenedor de S3, y los scripts los cargan a través de nuestra API.

Los tiempos estimados de ejecución para un archivo con 1 000 000 de filas deberían ser de aproximadamente cinco minutos. Consulta [Importación CSV de atributos de usuario a Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) para obtener más información.

### REST API

Utiliza el [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para registrar eventos personalizados, atributos de usuario y compras de usuarios.

### Ingesta de datos en la nube {#cloud-data-ingestion}

Utiliza la [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) de Braze para importar y mantener atributos de usuario.

## Validación de HTML {#html-validation}

Ten en cuenta que Braze no sanea, valida ni reformatea los datos HTML durante la importación, lo que significa que las etiquetas de script deben eliminarse de todos los datos de importación que utilices para la personalización web.

Al importar datos en Braze destinados específicamente a la personalización en un navegador web, asegúrate de que estén libres de HTML, JavaScript o cualquier otra etiqueta de script que pueda aprovecharse de forma malintencionada al renderizarse en un navegador web.

Alternativamente, para HTML, puedes utilizar los filtros Liquid de Braze (`strip_html`) para eliminar el HTML del texto renderizado. Por ejemplo:

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