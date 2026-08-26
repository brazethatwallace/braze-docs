---
nav_title: Buenas prácticas
article_title: Buenas prácticas de Ingesta de datos de Cloud
toc_headers: h2
page_order: 1
page_type: reference
description: "Esta página ofrece un resumen de la Ingesta de datos de Cloud, buenas prácticas y limitaciones del producto."

---

# Buenas prácticas {#best-practices}

> La Ingesta de datos de Cloud de Braze te permite configurar una conexión directa desde tu almacén de datos o sistema de almacenamiento de archivos a Braze para sincronizar datos relevantes de usuarios o catálogos. Al sincronizar estos datos con Braze, puedes aprovecharlos para casos de uso como la personalización, el desencadenamiento o la segmentación.

## Comprender la columna `UPDATED_AT` {#understanding-the-updated_at-column}

{% alert note %}
`UPDATED_AT` es relevante solo para integraciones de almacén de datos, no para sincronizaciones con S3.
{% endalert %}

Cuando se ejecuta una sincronización, Braze se conecta directamente a tu instancia de almacén de datos, recupera todos los datos nuevos de la tabla especificada y actualiza los datos correspondientes en tu panel de Braze. Cada vez que se ejecuta la sincronización, Braze refleja cualquier dato actualizado.

{% alert important %}
Braze CDI sincronizará las filas estrictamente en función del valor de `UPDATED_AT`, independientemente de si el contenido de la fila es el mismo que el que está actualmente en Braze. Por eso, recomendamos usar `UPDATED_AT` correctamente para sincronizar solo datos nuevos o actualizados y evitar un uso innecesario de puntos de datos.
{% endalert %}

### Ejemplo: sincronización recurrente {#example-recurring-sync}

Para ilustrar cómo se utiliza `UPDATED_AT` en una sincronización CDI, considera este ejemplo de sincronización recurrente para actualizar atributos de usuario:

- Fuentes de almacenamiento de archivos
   - Amazon S3

## Tipos de datos compatibles {#supported-data-types}

La ingesta de datos en la nube es compatible con los siguientes tipos de datos:
- Atributos de usuario, incluyendo:
   - Atributos personalizados anidados
   - Matrices de objetos
   - Estados de suscripción
- Eventos personalizados
- Eventos de compra
- Elementos de catálogo
- Solicitudes de eliminación de usuarios

### Evitar problemas con los tipos de datos {#avoiding-data-type-issues}

Al utilizar CDI para sincronizar datos de fuentes externas (como Databricks o Snowflake), asegúrate de que las columnas de origen utilicen los tipos de datos correctos antes de la sincronización. Los problemas más comunes incluyen:

- **Marcas de tiempo almacenadas como cadenas:** Asegúrate de que tus columnas de fecha utilicen un tipo timestamp o datetime en tu base de datos de origen, no un varchar o string.
- **Números almacenados como cadenas:** Convierte las columnas numéricas a tipos integer o float en tu consulta de origen antes de sincronizar.
- **Tipos inconsistentes entre sincronizaciones:** Si el tipo de una columna cambia entre sincronizaciones, Braze puede rechazar los nuevos datos. Verifica que el esquema de origen se mantenga consistente.

Para forzar o cambiar los tipos de datos de atributos personalizados en el panel de Braze, consulta [Gestionar datos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data#forcing-data-type-comparisons).

Puedes actualizar los datos de usuario por ID externo, alias de usuario, ID de Braze, correo electrónico o número de teléfono. Puedes eliminar usuarios por ID externo, alias de usuario o ID de Braze.

## Qué se sincroniza {#what-gets-synced}

Cada vez que se ejecuta una sincronización, Braze busca las filas que no se han sincronizado previamente. Esto se comprueba mediante la columna `UPDATED_AT` en tu tabla o vista. Braze selecciona e importa cualquier fila en la que `UPDATED_AT` sea posterior al último valor de `UPDATED_AT` sincronizado. Las filas que se encuentran exactamente en la marca de tiempo límite también pueden volver a sincronizarse si se añaden nuevas filas con esa misma marca de tiempo entre ejecuciones.

{% alert important %}
CDI rastrea el número de filas en el último valor de `UPDATED_AT` sincronizado. Si se añaden nuevas filas con esa misma marca de tiempo entre ejecuciones, CDI cambia a un límite inclusivo (`>=`) y vuelve a sincronizar todas las filas con esa marca de tiempo, incluidas las ya procesadas. Para evitar sincronizaciones duplicadas y un consumo innecesario de puntos de datos, utiliza valores de `UPDATED_AT` únicos entre ejecuciones de sincronización. Para más información, consulta [Evitar resincronizar filas con marcas de tiempo duplicadas](#avoid-resyncing-rows-with-duplicate-timestamps).
{% endalert %}

En tu almacén de datos, añade los siguientes usuarios y atributos a tu tabla, configurando la hora de `UPDATED_AT` como el momento en que añades estos datos:

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_1",
        "attribute_b":"example_value_1"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

Durante la siguiente sincronización programada, Braze sincroniza todas las filas con una marca de tiempo de `UPDATED_AT` posterior a la marca de tiempo sincronizada más reciente. Braze actualiza o añade campos, por lo que no necesitas sincronizar el perfil de usuario completo cada vez. Después de la sincronización, los perfiles de usuario reflejan las nuevas actualizaciones:

**Sincronización recurrente, segunda ejecución el 20 de julio de 2022 a las 12 pm**

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_2",
        "attribute_b":"example_value_2"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-16 00:25:30</code></td>
      <td><code>customer_9012</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":false,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

Se añadió una nueva fila para `customer_9012`, pero su valor de `UPDATED_AT` (`2022-07-16 00:25:30`) es anterior a la marca de tiempo almacenada (`2022-07-19 09:07:23`), por lo que no se sincronizará. Sin embargo, la fila existente de `customer_5678` tiene un valor de `UPDATED_AT` igual a la marca de tiempo almacenada, por lo que se vuelve a sincronizar debido al límite inclusivo. Para más detalles sobre este comportamiento, consulta [Asegúrate de que la hora de UPDATED_AT no sea la misma que la de tu sincronización](#make-sure-the-updated_at-time-isnt-the-same-time-as-your-sync). El `UPDATED_AT` almacenado permanece en `2022-07-19 09:07:23`.

**Sincronización recurrente, tercera ejecución el 21 de julio de 2022 a las 12 pm**

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_1",
        "attribute_b":"example_value_1"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-16 00:25:30</code></td>
      <td><code>customer_9012</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"xyz",
    "attribute_4":false,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-21 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_2",
        "attribute_b":"example_value_2"
    },
    "attribute_3":"2019-07-20T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

En esta tercera ejecución, se añadió otra nueva fila para `customer_1234` con un valor de `UPDATED_AT` (`2022-07-21 08:30:00`) posterior a la marca de tiempo almacenada. Esta nueva fila y la fila existente de `customer_5678` (que tiene un `UPDATED_AT` igual a la marca de tiempo almacenada) se sincronizan ambas. El `UPDATED_AT` almacenado ahora se establece como `2022-07-21 08:30:00`.

{% alert note %}
Los valores de `UPDATED_AT` pueden incluso ser posteriores a la hora de inicio de la ejecución de una sincronización determinada. Sin embargo, esto no se recomienda, ya que empuja la última marca de tiempo de `UPDATED_AT` "hacia el futuro" y las sincronizaciones posteriores no sincronizarán valores anteriores.
{% endalert %}

## Usa una marca de tiempo UTC para la columna `UPDATED_AT` {#use-a-utc-timestamp-for-the-updated_at-column}

La columna `UPDATED_AT` debe estar en UTC para evitar problemas con el horario de verano. Siempre que sea posible, utiliza funciones exclusivas de UTC, como `SYSDATE()` en lugar de `CURRENT_DATE()`.

## Evitar la resincronización de filas con marcas de tiempo duplicadas {#avoid-resyncing-rows-with-duplicate-timestamps}

CDI registra el número de filas en la última marca de tiempo de `UPDATED_AT` sincronizada. Si CDI detecta que se han añadido nuevas filas con esa misma marca de tiempo desde la última ejecución, utiliza un límite inclusivo (`>=`) para volver a seleccionar todas las filas con esa marca de tiempo, incluidas las ya procesadas. De lo contrario, CDI utiliza un límite exclusivo (`>`) y solo selecciona filas estrictamente posteriores al último valor sincronizado.

Por ejemplo, si una sincronización procesa cinco filas con `UPDATED_AT = 2025-04-01 00:00:00`, y posteriormente se añade una sexta fila con la misma marca de tiempo, la siguiente sincronización detecta el cambio en el recuento y vuelve a sincronizar las seis filas. Esto puede resultar en datos duplicados y consumo innecesario de puntos de datos.

Para evitar esto:

- Si estás configurando una sincronización contra un `VIEW`, no utilices `CURRENT_TIMESTAMP` como valor predeterminado. Esto hace que todos los datos se sincronicen cada vez que se ejecuta la sincronización, porque el campo `UPDATED_AT` se evalúa a la hora en que se ejecuta la consulta.
- Si tienes pipelines o consultas de larga duración que escriben datos en tu tabla de origen, evita ejecutarlos simultáneamente con una sincronización, o evita utilizar la misma marca de tiempo para cada fila insertada.
- Utiliza una transacción para escribir todas las filas que compartan la misma marca de tiempo.
- Utiliza valores de `UPDATED_AT` únicos y monótonamente crecientes para evitar que las filas se vuelvan a seleccionar después de haber sido procesadas.

### Ejemplo: administración de actualizaciones posteriores {#example-managing-subsequent-updates}

Este ejemplo muestra el proceso general para sincronizar datos por primera vez y luego solo actualizar los datos cambiantes (deltas) en las actualizaciones posteriores. Supongamos que tenemos una tabla `EXAMPLE_DATA` con algunos datos de usuario. El día 1 tiene los siguientes valores:

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>

<table aria-label="Ejemplo: administración de actualizaciones posteriores">
  <caption>Ejemplo: administración de actualizaciones posteriores</caption>
    <thead>
        <tr>
            <th>external_id</th>
            <th>attribute_1</th>
            <th>attribute_2</th>
            <th>attribute_3</th>
            <th>attribute_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td>823</td>
            <td>blue</td>
            <td>380</td>
            <td>FALSE</td>
        </tr>
        <tr>
            <td>23456</td>
            <td>28</td>
            <td>blue</td>
            <td>823</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>blue</td>
            <td>384</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td>red</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>red</td>
            <td>813</td>
            <td>FALSE</td>
        </tr>
    </tbody>
</table>

Para obtener estos datos en el formato que espera CDI, puedes ejecutar la siguiente consulta:

```sql
SELECT
    CURRENT_TIMESTAMP AS UPDATED_AT,
    EXTERNAL_ID AS EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT(
            'attribute_1', attribute_1,
            'attribute_2', attribute_2,
            'attribute_3', attribute_3,
            'attribute_4', attribute_4
        )
    ) AS PAYLOAD
FROM EXAMPLE_DATA;
```

Nada de esto se ha sincronizado antes con Braze, así que añádelo todo a la tabla de origen para CDI:

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
  </tbody>
</table>

Se ejecuta una sincronización y Braze registra que has sincronizado todos los datos disponibles hasta "2023-03-16 15:00:00". A continuación, en la mañana del día 2, se ejecuta un ETL y se actualizan algunos campos de la tabla de usuarios (marcados con *):

<table aria-label="Ejemplo: administración de actualizaciones posteriores">
  <caption>Ejemplo: administración de actualizaciones posteriores. * indica un campo actualizado desde la última sincronización.</caption>
    <thead>
        <tr>
            <th>external_id</th>
            <th>attribute_1</th>
            <th>attribute_2</th>
            <th>attribute_3</th>
            <th>attribute_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td style="background-color: #FFFF00;">145*</td>
            <td style="background-color: #FFFF00;">red*</td>
            <td>380</td>
            <td style="background-color: #FFFF00;">TRUE*</td>
        </tr>
        <tr>
            <td>23456</td>
            <td style="background-color: #FFFF00;">15*</td>
            <td>blue</td>
            <td>823</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>blue</td>
            <td style="background-color: #FFFF00;">495*</td>
            <td style="background-color: #FFFF00;">FALSE*</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td style="background-color: #FFFF00;">green*</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>red</td>
            <td style="background-color: #FFFF00;">693*</td>
            <td>FALSE</td>
        </tr>
    </tbody>
</table>

Ahora solo necesitas añadir los valores modificados a la tabla de origen de CDI. Estas filas pueden añadirse en lugar de actualizar las filas antiguas. Esa tabla ahora tiene este aspecto:

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "145", "ATTRIBUTE_2":"red", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "15"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_3":"495", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_2":"green"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_3":"693"}</code></td>
    </tr>
  </tbody>
</table>

CDI solo sincronizará las nuevas filas, por lo que la próxima sincronización que se ejecute solo sincronizará las últimas cinco filas.

## Consejos adicionales {#additional-tips}

### Escribe solo atributos nuevos o actualizados para minimizar el consumo {#only-write-new-or-updated-attributes-to-minimize-consumption}

Cada vez que se ejecuta una sincronización, Braze busca filas que no se hayan sincronizado previamente. Verificamos esto usando la columna `UPDATED_AT` en tu tabla o vista. Braze selecciona e importa cualquier fila donde `UPDATED_AT` sea posterior al último valor sincronizado de `UPDATED_AT`, independientemente de si son iguales a lo que está actualmente en el perfil de usuario. Las filas en la marca de tiempo límite también pueden resincronizarse si nuevas filas comparten esa marca de tiempo. Dado esto, recomendamos sincronizar solo los atributos que deseas agregar o actualizar.

El uso de puntos de datos es idéntico al usar CDI que con otros métodos de ingesta como REST API o SDK, por lo que depende de ti asegurarte de que solo estés agregando atributos nuevos o actualizados a tus tablas de origen.

### Separa `EXTERNAL_ID` de la columna `PAYLOAD` {#separate-external_id-from-payload-column}

El objeto `PAYLOAD` no debe incluir un ID externo ni otro tipo de ID.

### Elimina un atributo {#remove-an-attribute}

Puedes establecerlo como `null` si deseas omitir un atributo del perfil de un usuario. Si quieres que un atributo permanezca sin cambios, no lo envíes a Braze hasta que se haya actualizado. Para eliminar completamente un atributo, usa `TO_JSON(OBJECT_CONSTRUCT_KEEP_NULL(...))`.

### Realiza actualizaciones incrementales {#make-incremental-updates}

Realiza actualizaciones incrementales a tus datos para evitar sobrescrituras no intencionales cuando se hacen actualizaciones simultáneas.

{% alert important %}
* **Actualizaciones a distintos atributos:** En la gran mayoría de los casos, si dos actualizaciones no afectan los mismos atributos de un usuario, tienen resultados completamente independientes. Por ejemplo, si actualizas el atributo `Color` de un usuario y por separado actualizas su atributo `Size`, ambas actualizaciones deberían aplicarse correctamente, incluso si ocurren con segundos de diferencia.
* **Actualizaciones al mismo atributo:** Pueden ocurrir condiciones de carrera cuando múltiples actualizaciones apuntan al mismo atributo dentro de una sola ejecución de sincronización. En estos casos poco frecuentes, una actualización puede sobrescribir a otra. La mejor forma de prevenir este comportamiento es asegurarte de que los datos de origen de tu sincronización CDI reflejen solo el estado más reciente de cada usuario, o que todas las actualizaciones para un usuario dado o par usuario+atributo estén contenidas en una sola fila.
* **Operadores de matriz de objetos:** Las únicas excepciones a las actualizaciones independientes son con los operadores `$add`, `$remove` y `$update` para matrices de objetos, donde las actualizaciones a la misma matriz pueden interactuar entre sí.
* **Eventos:** Las condiciones de carrera no afectan a los eventos porque cada evento es único y tiene una marca de tiempo asociada.
{% endalert %}

La mejor forma de prevenir este comportamiento es asegurarte de que los datos de origen de tu sincronización CDI reflejen solo el estado más reciente de cada usuario, o que todas las actualizaciones para un usuario dado o par usuario+atributo estén contenidas en una sola fila.

### Crea una cadena JSON a partir de otra tabla {#create-a-json-string-from-another-table}

Si prefieres almacenar cada atributo en su propia columna internamente, necesitas convertir esas columnas a una cadena JSON para completar la sincronización con Braze. Para hacerlo, puedes usar una consulta como:

{% tabs local %}
{% tab Snowflake %}
Usa esta consulta en Snowflake para dar formato a las columnas de origen en campos CDI.
```sql
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    )as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% tab Redshift %}
Usa esta consulta en Redshift para dar formato a las columnas de origen en campos CDI.
```sql
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    ) as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% tab BigQuery %}
Usa esta consulta en BigQuery para dar formato a las columnas de origen en campos CDI.
```sql
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (attribute_1 string,
     attribute_2 STRING,
     attribute_3 NUMERIC,
     my_user_id STRING);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        'attribute_1' AS attribute_1,
        'attribute_2'AS attribute_2,
        'yet_another_attribute'AS attribute_3
      )
    ) as PAYLOAD
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Databricks %}
Usa esta consulta en Databricks para dar formato a las columnas de origen en campos CDI.
```sql
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (
    attribute_1 string,
    attribute_2 STRING,
    attribute_3 NUMERIC,
    my_user_id STRING
);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        attribute_1,
        attribute_2,
        attribute_3
      )
    ) as PAYLOAD
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Microsoft Fabric %}
Usa esta consulta en Microsoft Fabric para dar formato a las columnas de origen en campos CDI.
```sql
CREATE TABLE [braze].[users] (
    attribute_1 VARCHAR,
    attribute_2 VARCHAR,
    attribute_3 VARCHAR,
    attribute_4 VARCHAR,
    user_id VARCHAR
)
GO

CREATE VIEW [braze].[user_update_example]
AS SELECT
    user_id as EXTERNAL_ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[users] ;
```
{% endtab %}

{% endtabs %}

### Usa la marca de tiempo `UPDATED_AT` {#use-the-updated_at-timestamp}

Braze usa la marca de tiempo `UPDATED_AT` para rastrear qué datos se han sincronizado exitosamente. CDI también rastrea el número de filas en la última marca de tiempo sincronizada. Si se agregan nuevas filas con esa misma marca de tiempo entre ejecuciones, CDI resincroniza todas las filas en esa marca de tiempo, lo que puede llevar a datos duplicados. Para más detalles y consejos, consulta [Evitar resincronizar filas con marcas de tiempo duplicadas](#avoid-resyncing-rows-with-duplicate-timestamps).

### Configuración de la tabla {#table-configuration}

Tenemos un [repositorio público de GitHub](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion) para que los clientes compartan buenas prácticas o fragmentos de código. Para contribuir con tus propios fragmentos, ¡crea un pull request!

### Formato de datos {#data-formatting}

Los requisitos de configuración de tablas de ingesta de datos en la nube y los requisitos de formato de la carga útil están documentados en [Configuración de tablas para la ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup).

Usa esa página para distinguir:

- Requisitos de la tabla de origen (columnas requeridas, columnas de identificadores y comportamiento de `UPDATED_AT`)
- Requisitos de la carga útil (qué campos deben coincidir con el formato del objeto `/users/track` para cada tipo de datos)

### Evita tiempos de espera en las consultas del almacén de datos {#avoid-timeouts-for-data-warehouse-queries}

Recomendamos que las consultas se completen en una hora para un rendimiento óptimo y evitar posibles errores. Si las consultas superan este plazo, considera revisar la configuración de tu almacén de datos. Optimizar los recursos asignados a tu almacén puede ayudar a mejorar la velocidad de ejecución de las consultas.

## Limitaciones del producto {#product-limitations}

| Limitación            | Descripción                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Número de integraciones | No hay límite en la cantidad de integraciones que puedes configurar. Sin embargo, solo podrás configurar una integración por tabla o vista.                                             |
| Número de filas         | De forma predeterminada, cada ejecución puede sincronizar hasta 500 millones de filas. Braze detiene cualquier sincronización con más de 500 millones de filas nuevas. Si necesitas un límite superior, ponte en contacto con tu administrador de éxito de cliente o con soporte de Braze. |
| Atributos por fila     | Cada fila debe contener un único ID de usuario y un objeto JSON con hasta 250 atributos. Cada clave del objeto JSON cuenta como un atributo (es decir, una matriz cuenta como un atributo). |
| Tamaño de la carga útil           | Cada fila puede contener una carga útil de hasta 1 MB. Braze rechaza las cargas útiles superiores a 1&nbsp;MB y registra el error "Payload was greater than 1MB" en el registro de sincronización junto con el ID externo asociado y la carga útil truncada. |
| Tipo de datos              | Puedes sincronizar atributos de usuario, eventos y compras a través de la ingesta de datos en la nube.                                                                                                  |
| Región de Braze           | Este producto está disponible en todas las regiones de Braze. Cualquier región de Braze puede conectarse a cualquier región de datos de origen.                                                                              |
| Región de origen       | Braze se conectará a tu almacén de datos o entorno en la nube en cualquier región o proveedor de nube.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limitaciones del producto" }

<br><br>