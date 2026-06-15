---
nav_title: Filtros
article_title: Filtros de Liquid
page_order: 3
description: "Esta página de referencia enumera los filtros que se pueden usar para reformatear contenido estático o dinámico."

---

# Filtros {#filters}

> Este artículo de referencia ofrece un resumen de los filtros en Liquid y cubre qué filtros son compatibles con Braze. ¿Buscas ideas sobre cómo puedes usar estos filtros? Consulta nuestra [biblioteca de casos de uso de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases/).

Los filtros son la forma de modificar la salida de números, cadenas, variables y objetos en Liquid. Puedes usar filtros para reformatear texto estático o dinámico, como cambiar una cadena de minúsculas a mayúsculas o para realizar operaciones matemáticas, como sumas o divisiones.

{% alert important %}
Braze no es compatible con todos los filtros de Liquid de Shopify. Esta página intenta describir los filtros de Liquid que Braze ha probado, pero puede que no sea una lista completa. Siempre prueba tu Liquid antes de enviar cualquier mensaje. <br><br>Si tienes alguna pregunta sobre un filtro que no aparece aquí, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

## Sintaxis de filtros {#filter-syntax}

{% raw %}

Los filtros deben colocarse dentro de una etiqueta de salida `{{ }}` y se indican con un carácter de barra vertical `|`.

{% endraw %}

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{"Big Sale" | upcase}}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
BIG SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

En este ejemplo, `Big Sale` es una cadena y `upcase` es el filtro que se aplica.

{% alert note %}
Los filtros se pueden usar en sentencias `assign` y etiquetas de salida {% raw %}(`{{ }}`){% endraw %}, pero no en condicionales (`if`, `elsif`, `unless`), `case`/`when`, bucles `for` ni corchetes de acceso a arrays. Para usar un valor filtrado en uno de esos contextos, primero asigna el resultado a una variable. Para más detalles, consulta [Dónde usar operadores y filtros]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid/#where-to-use-operators-and-filters).
{% endalert %}

### Sintaxis para múltiples filtros {#syntax-for-multiple-filters}

Puedes usar múltiples filtros en una sola salida. Se aplican de izquierda a derecha.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
 {{ "Big Sale" | upcase | remove: "BIG" }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Filtros de arrays {#array-filters}

Los filtros de arrays se usan para cambiar la salida de arrays.

| Filtro               | Definición                                                                                                         | Compatible |
| :------------------- | :----------------------------------------------------------------------------------------------------------------- | :-------- |
| [join](https://shopify.dev/docs/api/liquid/filters/join)          | Une los elementos de un array con el carácter pasado como parámetro. El resultado es una sola cadena.          | ✅  Sí   |
| [first](https://shopify.dev/docs/api/liquid/filters/first)         | Devuelve el primer elemento de un array. En un array de atributos personalizados, este es el valor más antiguo añadido.                | ✅  Sí   |
| [last](https://shopify.dev/docs/api/liquid/filters/last)          | Devuelve el último elemento de un array. En un array de atributos personalizados, este es el valor añadido más recientemente.          | ✅  Sí   |
| [compact](https://shopify.dev/api/liquid/filters/compact)       | Elimina cualquier elemento `nil` de un array.                                                                             | ✅  Sí   |
| [concat](https://shopify.dev/api/liquid/filters/concat)        | Combina un array con otro array.                                                                              | ✅  Sí   |
| [find_index](https://shopify.dev/docs/api/liquid/filters/find_index)         | Devuelve el elemento en la posición de índice especificada en un array. El primer elemento de un array se referencia con `[0]`. | ⛔  No   |
| [map](https://shopify.dev/api/liquid/filters/map)           | Acepta un atributo de un elemento del array como parámetro y crea un array a partir del valor de cada elemento del array.        | ✅  Sí   |
| [reverse](https://shopify.dev/api/liquid/filters/reverse)       | Invierte el orden de los elementos en un array.                                                                       | ✅  Sí   |
| [size](https://shopify.dev/api/liquid/filters/size)          | Devuelve el tamaño de una cadena (el número de caracteres) o de un array (el número de elementos).                      | ✅  Sí   |
| [slice](https://shopify.dev/api/liquid/filters/slice)        | Devuelve una subcadena de una cadena o un subconjunto de un array, comenzando en el índice especificado.                          | ✅  Sí   |
| [sort](https://shopify.dev/api/liquid/filters/sort)         | Ordena los elementos de un array por un atributo dado de un elemento en el array.                                    | ✅  Sí   |
| [sort_natural](https://shopify.dev/api/liquid/sort_natural) | Ordena los elementos de un array en orden alfabético sin distinguir entre mayúsculas y minúsculas.                                                | ✅  Sí   |
| [uniq](https://shopify.dev/api/liquid/filters/uniq)         | Elimina cualquier instancia duplicada de elementos en un array.                                                           | ✅  Sí   |
| [where](https://shopify.dev/api/liquid/where)        | Filtra un array para incluir solo elementos con un valor de propiedad específico.                                             | ✅  Sí   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Array filters" }

## Filtros de color {#color-filters}

Los [filtros de color](https://shopify.dev/api/liquid/filters/color-filters) no son compatibles con Braze.

## Filtros de fuentes {#font-filters}

Los [filtros de fuentes](https://shopify.dev/api/liquid/filters/font-filters) no son compatibles con Braze.

## Filtros matemáticos {#math-filters}

Los filtros matemáticos te permiten realizar operaciones matemáticas. Si usas múltiples filtros en una sola salida, se aplicarán de izquierda a derecha.

| Filtro  | Definición      | Compatible |
| :------ |:----------------| :-------- |
| [abs](https://shopify.dev/api/liquid/filters/abs)        | Devuelve el valor absoluto de un número.     | ✅  Sí   |
| [at_most](https://shopify.dev/api/liquid/filters/at_most)    | Limita un número a un valor máximo.   | ✅  Sí   |
| [at_least](https://shopify.dev/api/liquid/filters/at_least)   | Limita un número a un valor mínimo.   | ✅  Sí   |
| [ceil](https://shopify.dev/api/liquid/filters/ceil)       | Redondea una salida hacia arriba al entero más cercano.  | ✅  Sí   |
| [divided_by](https://shopify.dev/api/liquid/filters/divided_by) | Divide una salida entre un número. La salida se redondea hacia abajo al entero más cercano. Consulta el siguiente consejo para evitar el redondeo. | ✅  Sí   |
| [floor](https://shopify.dev/api/liquid/filters/floor)      | Redondea una salida hacia abajo al entero más cercano.        | ✅  Sí   |
| [minus](https://shopify.dev/api/liquid/filters/minus)      | Resta un número de una salida.          | ✅  Sí   |
| [plus](https://shopify.dev/api/liquid/filters/plus)       | Suma un número a una salida.     | ✅  Sí   |
| [round](https://shopify.dev/api/liquid/filters/round)      | Redondea la salida al entero más cercano o al número de decimales especificado.  | ✅  Sí   |
| [times](https://shopify.dev/api/liquid/filters/times)     | Multiplica una salida por un número.       | ✅  Sí   |
| [modulo](https://shopify.dev/api/liquid/filters/modulo)    | Divide una salida entre un número y devuelve el resto.   | ✅  Sí   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Math filters" }

{% alert tip %}
Al dividir enteros (números enteros) entre enteros en Liquid, si el resultado es un flotante (número con decimal), Liquid redondeará automáticamente hacia abajo al entero más cercano. Sin embargo, dividir enteros entre flotantes siempre te dará un flotante. Esto significa que puedes convertir tus enteros en flotantes (1.0, 2.0, 3.0) para obtener un flotante como resultado.
{% raw %}
<br><br>Por ejemplo, `{{15 | divided_by: 2}}` dará como salida `7`, mientras que `{{15 | divided_by: 2.0}}` dará como salida `7.5`.
{% endraw %}
{% endalert %}

### Operaciones matemáticas con atributos personalizados {#mathematical-operations-with-custom-attributes}

Ten en cuenta que no puedes realizar operaciones matemáticas entre dos atributos personalizados.

{% raw %}

```liquid
{{custom_attribute.${current_rewards_balance} | plus: {{custom_attribute.${giftcard_balance}}}}}
```

Este ejemplo no funcionaría porque no puedes referenciar múltiples atributos personalizados en una sola línea de Liquid. En su lugar, necesitarías asignar una variable a al menos uno de estos valores antes de que se realicen las funciones matemáticas. Sumar dos atributos personalizados requeriría dos líneas de Liquid:

1. Una para asignar el atributo personalizado a una variable,
2. Una para realizar la suma.

#### Caso de uso: calcular el saldo actual {#use-case-calculate-current-balance}

Supongamos que queremos calcular el saldo actual de un usuario sumando su saldo de tarjeta de regalo y su saldo de recompensas.

1. Usa la etiqueta `assign` para sustituir el atributo personalizado de `current_rewards_balance` con el término "balance". Esto significa que ahora tienes una variable llamada `balance`, que puedes manipular.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

{: start="2"}
2. Usa el filtro `plus` para combinar el saldo de tarjeta de regalo de cada usuario con su saldo de recompensas, representado por el objeto `{{balance}}`.
{% endraw %}
{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
You have $35 to spend!
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Filtros de dinero {#money-filters}

Si estás actualizando a un usuario sobre su compra, un saldo de cuenta o cualquier cosa relacionada con dinero, deberías usar filtros de dinero. Los filtros de dinero aseguran que tus decimales estén en el lugar correcto y que ninguna parte de tu actualización se pierda (como ese molesto `0` al final).

| Filtro         | Definición          | Compatible |
| :--------------- | :--------------- | :-------- |
| [money](https://shopify.dev/api/liquid/filters/money)      | Formatea números para asegurar que los decimales estén en el lugar correcto y que los ceros no se eliminen del final de ningún número.   | ✅  Sí   |
| [money_with_currency](https://shopify.dev/api/liquid/filters/money_with_currency)    | Formatea números con el símbolo de moneda.     | ⛔  No    |
| [money_without_currency](https://shopify.dev/api/liquid/filters/money_without_currency)     | Formatea números sin el símbolo de moneda.      | ⛔  No    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Money filters" }

{% alert important %}
Para formatear correctamente un número con el filtro `money`, elimina cualquier coma en el número y añade el filtro `plus: 0` antes del filtro `money`. Por ejemplo, consulta el siguiente Liquid:<br><br>
{% raw %}
```liquid
{% assign my_int = "350000.25" | plus: 0 %}
{{ my_int | money }}
```
{% endraw %}
{% endalert %}

### Filtro money de Shopify versus filtro money de Braze {#shopify-money-filter-versus-braze-money-filter}

{% alert warning %}
El comportamiento del filtro `money` de Shopify difiere de cómo se usa en Braze. Consulta los siguientes ejemplos para una representación precisa del comportamiento esperado.
{% endalert %}

{% raw %}
En caso de que estés ingresando un atributo personalizado (como `account_balance`), siempre deberías usar el filtro `money` para colocar tus decimales en el lugar correcto y evitar que los ceros se eliminen del final de cualquier número:

```liquid
${{custom_attribute.${account_balance} | money}}
```
{% endraw %}

| CON EL FILTRO MONEY                       | SIN EL FILTRO MONEY                    |
| :------------------------------------------ | :------------------------------------------ |
| ![Con filtro money]({% image_buster /assets/img/with_money_filter.png %})                     | ![Sin filtro money]({% image_buster /assets/img/without_money_filter.png %})                  |
| Donde `account_balance` se ingresa como `17.8`. | Donde `account_balance` se ingresa como `17.8`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Shopify money filter versus Braze money filter" }

El filtro `money` en Braze difiere de Shopify porque no aplica automáticamente puntos decimales según una configuración preestablecida. Por ejemplo, toma el siguiente escenario donde `rewards_redeemed` contiene un valor de `145`:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | money }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
$145.00
```
{% endraw %}
{% endtab %}
{% endtabs %}

Según el filtro [money](https://shopify.dev/api/liquid/filters/money) de Shopify, esto debería tener una salida de `$1.45`, sin embargo en Braze, esto tendrá una salida de `$145.00`. Como solución alternativa, podemos usar el filtro `divided_by` para manipular el número a un decimal, antes de aplicar el filtro money:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | divided_by: 100.00 | money }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
$1.45
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Filtros de cadenas {#string-filters}

Los filtros de cadenas se usan para manipular las salidas y variables de cadenas. Las cadenas son una combinación de caracteres alfanuméricos y deben estar envueltas en comillas rectas.

{% alert note %}
Las comillas rectas son diferentes de las comillas tipográficas en Liquid. Ten cuidado al copiar y pegar Liquid desde un editor de texto a Braze, ya que las comillas tipográficas causarán errores con tu Liquid. Si escribes tu Liquid directamente en Braze, las comillas rectas se aplicarán automáticamente.
{% endalert %}

| Filtro          | Descripción     | Compatible |
| :--------------- | ------------- | --------- |
| [append](https://shopify.dev/api/liquid/filters/append)     | Añade caracteres a una cadena.           | ✅  Sí   |
| [camelize](https://shopify.dev/docs/api/liquid/filters/camelize)     | Convierte una cadena a CamelCase.             | ⛔  No    |
| [capitalize](https://shopify.dev/api/liquid/filters/capitalize)     | Pone en mayúscula la primera palabra de una cadena y convierte a minúsculas los caracteres restantes.         | ✅  Sí   |
| [downcase](https://shopify.dev/api/liquid/filters/downcase)      | Convierte una cadena a minúsculas.         | ✅  Sí   |
| [escape](https://shopify.dev/api/liquid/filters/escape)    | Escapa una cadena.             | ✅  Sí   |
| [handleize](https://shopify.dev/api/liquid/filters/handleize)        | Formatea una cadena como un handle.        | ⛔  No    |
| [md5](https://shopify.dev/api/liquid/filters/md5)    | Convierte una cadena en un hash MD5. Consulta [Filtros de codificación]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/#encoding-filters) para más información.   | ✅  Sí   |
| [sha1](https://shopify.dev/api/liquid/filters/sha1)    | Convierte una cadena en un hash SHA-1. Consulta [Filtros de codificación]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/#encoding-filters) para más información.  | ✅  Sí   |
| hmac_sha1_hex<br>(anteriormente [hmac_sha_1](https://shopify.dev/api/liquid/filters/string-filters#hmac_sha1)) | Convierte una cadena en un hash SHA-1 usando un código de autenticación de mensajes basado en hash (HMAC). Pasa la clave secreta del mensaje como parámetro al filtro. Consulta [Filtros de codificación]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/#encoding-filters) para más información. | ✅  Sí   |
| [hmac_sha256](https://shopify.dev/api/liquid/filters/hmac_sha256)    | Convierte una cadena en un hash SHA-256 usando un código de autenticación de mensajes basado en hash (HMAC). Pasa la clave secreta del mensaje como parámetro al filtro.       | ✅  Sí   |
| hmac_sha512 | Convierte una cadena en un hash SHA-512 usando un código de autenticación de mensajes basado en hash (HMAC). Pasa la clave secreta del mensaje como parámetro al filtro. | ✅  Sí  |
| [newline_to_br](https://shopify.dev/api/liquid/filters/newline_to_br)     | Inserta una etiqueta HTML de salto de línea `<br>` delante de cada salto de línea en una cadena.        | ✅  Sí   |
| [pluralize](https://shopify.dev/api/liquid/filters/pluralize)   | Muestra la versión singular o plural de una cadena en inglés basándose en el valor de un número.      | ⛔  No    |
| [prepend](https://shopify.dev/api/liquid/filters/prepend)     | Antepone caracteres a una cadena.      | ✅  Sí   |
| [remove](https://shopify.dev/api/liquid/filters/remove)      | Elimina todas las ocurrencias de una subcadena de una cadena.       | ✅  Sí   |
| [remove_first](https://shopify.dev/api/liquid/filters/remove_first)    | Elimina solo la primera ocurrencia de una subcadena de una cadena.      | ✅  Sí   |
| [replace](https://shopify.dev/api/liquid/filters/replace)        | Reemplaza todas las ocurrencias de una cadena con una subcadena.   | ✅  Sí   |
| [replace_first](https://shopify.dev/api/liquid/filters/replace_first)        | Reemplaza la primera ocurrencia de una cadena con una subcadena.      | ✅  Sí   |
| [slice](https://shopify.dev/api/liquid/filters/slice)       | El filtro slice devuelve una subcadena, comenzando en el índice especificado.       | ✅  Sí   |
| [split](https://shopify.dev/api/liquid/filters/split)  | El filtro split toma una subcadena como parámetro. La subcadena se usa como delimitador para dividir una cadena en un array.            | ✅  Sí   |
| [strip](https://shopify.dev/api/liquid/filters/strip)   | Elimina tabulaciones, espacios y saltos de línea (todos los espacios en blanco) del lado izquierdo y derecho de una cadena.                                                                                                    | ✅  Sí   |
| [lstrip](https://shopify.dev/api/liquid/filters/lstrip)     | Elimina tabulaciones, espacios y saltos de línea (todos los espacios en blanco) del lado izquierdo de una cadena.    | ⛔  No    |
| [rstrip](https://shopify.dev/api/liquid/filters/rstrip)             | Elimina tabulaciones, espacios y saltos de línea (todos los espacios en blanco) del lado derecho de una cadena.          | ⛔  No    |
| [strip_html](https://shopify.dev/api/liquid/filters/strip_html)         | Elimina todas las etiquetas HTML de una cadena.        | ✅  Sí   |
| [strip_newlines](https://shopify.dev/api/liquid/filters/strip_newlines)  | Elimina cualquier salto de línea de una cadena.        | ✅  Sí   |
| [truncate](https://shopify.dev/api/liquid/filters/truncate)    | Trunca una cadena al número de caracteres pasado como primer parámetro. Se añaden puntos suspensivos (...) a la cadena truncada y se incluyen en el conteo de caracteres.    | ✅  Sí   |
| [truncatewords](https://shopify.dev/api/liquid/filters/truncatewords)   | Trunca una cadena al número de palabras pasado como primer parámetro. Se añaden puntos suspensivos (...) a la cadena truncada.    | ✅  Sí   |
| [upcase](https://shopify.dev/api/liquid/filters/upcase)   | Convierte una cadena a mayúsculas.      | ✅  Sí   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="String filters" }

## Filtros adicionales {#additional-filters}

Los siguientes filtros generales sirven para muchos propósitos, incluyendo formatear o convertir contenido.

| Filtro                | Descripción                                                                                                                      | Compatible |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| [date](https://shopify.dev/api/liquid/filters/date)           | Convierte una marca de tiempo a otro formato de fecha. Consulta [Filtro de fecha](#date-filter) para más información.         | ✅  Sí   |
| [default](https://shopify.dev/api/liquid/filters/default)        | Establece un valor predeterminado para cualquier variable sin valor asignado. Se puede usar con cadenas, arrays y hashes.      | ✅  Sí   |
| [format_address](https://shopify.dev/api/liquid/filters/format_address) | Formatea una dirección para imprimir los elementos de la dirección en orden según su configuración regional.        | ⛔  No    |
| [highlight](https://shopify.dev/api/liquid/filters/highlight)      | Envuelve palabras dentro de los resultados de búsqueda con una etiqueta HTML `<strong>` con la clase highlight si coincide con los términos de búsqueda enviados. | ⛔  No    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Additional filters" }

Puedes encontrar más filtros compatibles, como filtros de codificación y URL, en nuestra página de [Filtros avanzados]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/).

### Filtro de fecha {#date-filter}

El filtro `date` se puede usar para convertir una marca de tiempo a un formato de fecha diferente. Puedes pasar parámetros al filtro `date` para reformatear la marca de tiempo. Para ejemplos de estos parámetros, consulta [strfti.me](http://www.strfti.me/).

Por ejemplo, supongamos que el valor de `date_attribute` es la marca de tiempo `2021-06-03 17:13:41 UTC`.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%b %d'}}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
03 June
```
{% endraw %}
{% endtab %}
{% endtabs %}

Además de las opciones de formato `strftime`, Braze también permite convertir una marca de tiempo a tiempo Unix con el filtro de fecha `%s`. Por ejemplo, para obtener `date_attribute` en tiempo Unix:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%s' }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
1433351621
```
{% endraw %}
{% endtab %}
{% endtabs %}