Los valores de `properties` deben ser un objeto de hasta 50&nbsp;KB, donde las claves son los nombres de las propiedades y los valores son los valores de las propiedades. Los nombres de las propiedades deben ser cadenas de 255 caracteres o menos, sin signos de dólar (`$`) al inicio.

Los valores de las propiedades pueden ser cualquiera de los siguientes tipos de datos:

| Tipo de datos | Descripción |
| --- | --- |
| Número | Entero o flotante |
| Booleano | Valor `true` o `false` |
| Datetime | Cadena en formato [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) o `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. No compatible en arrays. |
| Cadena | 255 caracteres o menos |
| Array | Compatible; los datetimes no son compatibles en arrays. |
| Objeto | Se ingestan como cadenas (no como objetos anidados). Para datos anidados, usa un valor de cadena (por ejemplo, JSON serializado). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Table" }

Las siguientes claves están reservadas y no pueden usarse como nombres de propiedades: `time`, `product_id`, `quantity`, `event_name`, `price` y `currency`. Usar una clave reservada en el objeto `properties` devuelve el error "Invalid 'properties' field".