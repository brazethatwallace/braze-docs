---
nav_title: Conjunto de objetos
article_title: Conjunto de objetos
alias: "/array_of_objects/"
page_order: 2
page_type: reference
description: "Este artículo de referencia cubre el uso de un conjunto de objetos como tipo de datos para atributos personalizados, incluyendo limitaciones y ejemplos de uso."
---

# Conjunto de objetos {#array-of-objects}

> Esta página explica cómo utilizar un conjunto de objetos para agrupar atributos relacionados. Por ejemplo, puedes tener un grupo de objetos mascota, objetos canción y objetos cuenta que pertenezcan todos a un usuario. Estos conjuntos de objetos pueden utilizarse para personalizar tus mensajes con Liquid, o crear segmentos de audiencia si algún elemento de un objeto coincide con los criterios.

{% multi_lang_include nested_attribute_objects/supported_data_types.md %}

## Consideraciones {#considerations}

- Los conjuntos de objetos están pensados para atributos personalizados enviados a través de la API. No es posible cargar archivos CSV. Esto se debe a que las comas en el archivo CSV se interpretarán como un separador de columna, y las comas en los valores causarán errores de análisis.
- Los conjuntos de objetos no tienen límite en el número de elementos, pero sí un tamaño máximo de 100&nbsp;KB. Si una actualización (como `$add` o `$update`) hace que el conjunto supere este límite, Braze descarta la actualización y el atributo permanece sin cambios. La solicitud de API aún devuelve una respuesta de éxito. Para mantener el conjunto por debajo del límite y poder agregar nuevos elementos, usa `$remove` para eliminar elementos del conjunto primero.
- No todos los partners de Braze admiten conjuntos de objetos. Consulta la [documentación del partner]({{site.baseurl}}/partners/home) para confirmar si la integración admite esta característica.

Actualizar o eliminar elementos de un conjunto requiere identificar el elemento por clave y valor, así que considera incluir un identificador único para cada elemento del conjunto. La unicidad se aplica solo al conjunto y es útil si deseas actualizar y eliminar objetos específicos de tu conjunto. Esto no es aplicado por Braze.

{% alert important %}
Cuando un atributo personalizado anidado en tu solicitud contiene valores no válidos (como formatos de hora no válidos o valores `null`), Braze descarta todas las actualizaciones de atributos personalizados anidados en la solicitud del procesamiento. Esto se aplica a todas las estructuras anidadas dentro de ese atributo específico. Verifica que todos los valores dentro de los atributos personalizados anidados sean válidos antes de enviar. Para más información, consulta [Crear y actualizar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_track#how-does-userstrack-handle-invalid-nested-custom-attributes).
{% endalert %}

{% alert tip %}
Para más información sobre el uso de conjuntos de objetos para objetos de atributos de usuario, consulta [Objeto de atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens).
{% endalert %}

## Ejemplo de API {#api-example}

Usa estos ejemplos cuando envíes solicitudes `/users/track` que creen o actualicen atributos personalizados anidados almacenados como conjuntos de objetos. La carga útil usa los operadores `$add`, `$remove` y `$update` para que puedas cambiar objetos específicos sin reconstruir el conjunto completo en cada solicitud.

{% tabs local %}
{% tab Crear %}

El siguiente es un ejemplo de `/users/track` con un conjunto `pets`. Para capturar las propiedades de las mascotas, envía una solicitud de API que liste `pets` como un conjunto de objetos. Ten en cuenta que a cada objeto se le ha asignado un `id` único que puede referenciarse más tarde al realizar actualizaciones.

Usa este formato cuando quieras crear el atributo por primera vez o reemplazar el conjunto completo con un nuevo conjunto base de objetos.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Mochi"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Pixel"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab Agregar %}

Agrega otro elemento al conjunto usando el operador `$add`. El siguiente ejemplo muestra cómo agregar tres objetos de mascotas más al conjunto `pets` del usuario.

Usa `$add` cuando necesites añadir uno o más objetos nuevos y mantener los objetos existentes sin cambios.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$add": [
          {
            "id": 3,
            "type": "dog",
            "breed": "corgi",
            "name": "Biscuit"
          },
          {
            "id": 4,
            "type": "fish",
            "breed": "salmon",
            "name": "Pepper"
          },
           {
            "id": 5,
            "type": "bird",
            "breed": "parakeet",
            "name": "Noodle"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab Actualizar %}

Actualiza valores para objetos específicos dentro de un conjunto usando el parámetro `_merge_objects` y el operador `$update`. De manera similar a las actualizaciones de otros objetos de [atributos personalizados anidados]({{site.baseurl}}/nested_custom_attribute_support#api-request-body), esto realiza una fusión profunda.

Ten en cuenta que `$update` no se puede usar para eliminar una propiedad anidada de un objeto dentro de un conjunto. Para hacer esto, necesitarás eliminar el elemento completo del conjunto y luego agregar el objeto sin esa clave específica (usando una combinación de `$remove` y `$add`).

Usa `$update` cuando el objeto ya exista y quieras cambiar uno o más campos haciendo coincidir `$identifier_key` y `$identifier_value`.

El siguiente ejemplo muestra cómo actualizar la propiedad `breed` a `goldfish` para el objeto con un `id` de `4`. Este ejemplo de solicitud también actualiza el objeto con `id` igual a `5` con un nuevo `name` de `Annette`. Dado que el parámetro `_merge_objects` está configurado como `true`, todos los demás campos de estos dos objetos permanecen iguales.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```

{% alert warning %}
Debes configurar `_merge_objects` como true, o tus objetos serán sobrescritos. `_merge_objects` es false de forma predeterminada.
{% endalert %}

{% endtab %}
{% tab Eliminar %}

Elimina objetos de un conjunto usando el operador `$remove` en combinación con una clave coincidente (`$identifier_key`) y un valor (`$identifier_value`).

Usa `$remove` cuando quieras eliminar todos los objetos coincidentes para un par de identificador conocido, como `id = 2` o `type = dog`.

El siguiente ejemplo muestra cómo eliminar cualquier objeto en el conjunto `pets` que tenga un `id` con valor `1`, un `id` con valor `2` y un `type` con valor `dog`. Si hay múltiples objetos con el valor de `type` `dog`, todos los objetos coincidentes serán eliminados.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

### Orden de procesamiento {#processing-order}

Cuando una sola solicitud `/users/track` incluye operaciones `$add`, `$remove` y `$update` para el mismo atributo de conjunto, Braze las procesa en este orden:

1. `$add`
2. `$remove`
3. `$update`

Este orden se aplica dentro de un solo objeto de actualización de atributo en una solicitud y determina el estado final del conjunto después de que se evalúan todas las operaciones.

Dado que `$add` se ejecuta antes que `$remove`, no puedes usar un `$remove` seguido de `$add` como mecanismo de upsert dentro de una sola solicitud. El `$add` se procesa primero, luego el `$remove` elimina el elemento. Para hacer un upsert, envía el `$remove` en una solicitud separada antes del `$add`.

### Marcas de tiempo {#timestamps}

Al incluir campos como marcas de tiempo en un conjunto de objetos, usa el formato `$time` en lugar de cadenas simples o enteros de época unix.

```json
{
  "attributes": [
    {
      "external_id": "user123",
      "purchases": [
        {
          "item_name": "T-shirt",
          "price": 19.99,
          "purchase_time": {
            "$time": "2020-05-28"
          }
        }
      ]
    }
  ]
}
```

{% alert tip %}
Para más información, consulta [Atributos personalizados anidados]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support).
{% endalert %}

## Ejemplo de SDK {#sdk-example}

{% tabs local %}
{% tab Android SDK %}
{% subtabs %}
{% subtab Crear %}
```kotlin
val json = JSONArray()
    .put(JSONObject()
        .put("id", 1)
        .put("type", "dog")
        .put("breed", "beagle")
        .put("name", "Gus"))
    .put(JSONObject()
        .put("id", 2)
        .put("type", "cat")
        .put("breed", "calico")
        .put("name", "Pixel")
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json)
}
```
{% endsubtab %}

{% subtab Agregar %}
```kotlin
val json = JSONObject()
    .put("\$add", JSONArray()
        .put(JSONObject()
            .put("id", 3)
            .put("type", "dog")
            .put("breed", "corgi")
            .put("name", "Doug"))
        .put(JSONObject()
            .put("id", 4)
            .put("type", "fish")
            .put("breed", "salmon")
            .put("name", "Pepper"))
        .put(JSONObject()
            .put("id", 5)
            .put("type", "bird")
            .put("breed", "parakeet")
            .put("name", "Noodle")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}

{% subtab Actualizar %}
```kotlin
val json = JSONObject()
    .put("\$update", JSONArray()
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 4)
            .put("\$new_object", JSONObject()
                .put("breed", "goldfish")
            )
        )
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 5)
            .put("\$new_object", JSONObject()
                .put("name", "Annette")
            )
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}

{% subtab Eliminar %}
```kotlin
val json = JSONObject()
    .put("\$remove", JSONArray()
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 1)
        )
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 2)
        )
        .put(JSONObject()
            .put("\$identifier_key", "type")
            .put("\$identifier_value", "dog")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Swift SDK %}
{% subtabs %}
{% subtab Crear %}
```swift
let json: [[String: Any?]] = [
  [
    "id": 1,
    "type": "dog",
    "breed": "beagle",
    "name": "Mochi"
  ],
  [
    "id": 2,
    "type": "cat",
    "breed": "calico",
    "name": "Pixel"
  ]
]

braze.user.setCustomAttribute(key: "pets", array: json)
```
{% endsubtab %}

{% subtab Agregar %}
```swift
let json: [String: Any?] = [
  "$add": [
    [
      "id": 3,
      "type": "dog",
      "breed": "corgi",
      "name": "Biscuit"
    ],
    [
      "id": 4,
      "type": "fish",
      "breed": "salmon",
      "name": "Pepper"
    ],
    [
      "id": 5,
      "type": "bird",
      "breed": "parakeet",
      "name": "Noodle"
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}

{% subtab Actualizar %}
```swift
let json: [String: Any?] = [
  "$update": [
    [
      "$identifier_key": "id",
      "$identifier_value": 4,
      "$new_object": [
        "breed": "goldfish"
      ]
    ],
    [
      "$identifier_key": "id",
      "$identifier_value": 5,
      "$new_object": [
        "name": "Annette"
      ]
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}

{% subtab Eliminar %}
```swift
let json: [String: Any?] = [
  "$remove": [
    [
      "$identifier_key": "id",
      "$identifier_value": 1,
    ],
    [
      "$identifier_key": "id",
      "$identifier_value": 2,
    ],
    [
      "$identifier_key": "type",
      "$identifier_value": "dog",
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Los atributos personalizados anidados no son compatibles con AppboyKit.
{% endalert %}
{% endtab %}

{% tab Web SDK %}
{% subtabs local %}
{% subtab Crear %}
```javascript
import * as braze from "@braze/web-sdk";
const json = [{
  "id": 1,
  "type": "dog",
  "breed": "beagle",
  "name": "Mochi"
}, {
  "id": 2,
  "type": "cat",
  "breed": "calico",
  "name": "Pixel"
}];
braze.getUser().setCustomUserAttribute("pets", json);
```
{% endsubtab %}

{% subtab Agregar %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$add": [{
    "id":  3,
    "type":  "dog",
    "breed":  "corgi",
    "name":  "Doug",
  }, {
    "id":  4,
    "type":  "fish",
    "breed":  "salmon",
    "name":  "Pepper",
  }, {
    "id":  5,
    "type":  "bird",
    "breed":  "parakeet",
    "name":  "Noodle",
  }]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}

{% subtab Actualizar %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$update": [
    {
      "$identifier_key": "id",
      "$identifier_value": 4,
      "$new_object": {
        "breed": "goldfish"
      }
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 5,
      "$new_object": {
        "name": "Annette"
      }
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}

{% subtab Eliminar %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$remove": [
    {
      "$identifier_key": "id",
      "$identifier_value": 1,
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 2,
    },
    {
      "$identifier_key": "type",
      "$identifier_value": "dog",
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Plantillas Liquid {#liquid-templating}

Puedes usar este conjunto `pets` para personalizar un mensaje. El siguiente ejemplo de plantilla Liquid muestra cómo hacer referencia a las propiedades del objeto de atributo personalizado guardadas de la solicitud de API anterior y usarlas en tu mensajería.

{% raw %}
```liquid
{% assign pets = {{custom_attribute.${pets}}} %}

{% for pet in pets %}
I have a {{pet.type}} named {{pet.name}}! They are a {{pet.breed}}.
{% endfor %}
```
{% endraw %}

En este escenario, puedes usar Liquid para recorrer el conjunto `pets` e imprimir una declaración para cada mascota. [Asigna una variable]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/dashboard_tools#assign-variables) al atributo personalizado `pets` y usa la notación de punto para acceder a las propiedades de un objeto. Especifica el nombre del objeto, seguido de un punto `.`, seguido del nombre de la propiedad.

## Segmentación {#segmentation}

Al segmentar usuarios basándote en conjuntos de objetos, un usuario calificará para el segmento si algún objeto en el conjunto coincide con los criterios.

Crea un nuevo segmento y selecciona **Atributo personalizado anidado** como tu filtro. Luego busca y selecciona el nombre de tu conjunto de objetos.

![Filtrar por conjunto de objetos.]({% image_buster /assets/img_archive/array_of_objects_segmenting_1.gif %})

Usa la notación de punto para especificar qué campo en el conjunto de objetos deseas usar. Comienza el campo de texto con un conjunto vacío de corchetes `[]` para indicarle a Braze que estás buscando dentro de un conjunto de objetos. Después, agrega un punto `.`, seguido del nombre del campo que deseas usar.

Por ejemplo, si deseas filtrar un conjunto de objetos `top_3_movies` basándote en el campo `type`, ingresa `[].type` y elige las películas por las que filtrar, como `Fantasy Movie`.


### Niveles de anidamiento {#levels-of-nesting}

Puedes crear un segmento con hasta un nivel de anidamiento de conjunto (conjunto dentro de otro conjunto). Por ejemplo, dados los siguientes atributos, puedes crear un segmento para `pets[].name` contiene `Mochi`, pero no puedes crear un segmento para `pets[].nicknames[]` contiene `Gugu`.

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Mochi",
          "nicknames": [
            "MoMo",
            "Mochi"
          ]
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Pixel",
          "nicknames": [
            "PiPi",
            "Pixel"
          ]
        }
      ]
    }
  ]
}
```
{% endraw %}

## Puntos de datos {#data-points}

Los puntos de datos se registran de manera diferente dependiendo de si creas, actualizas o eliminas una propiedad.

{% tabs local %}
{% tab Crear %}

Crear un nuevo conjunto registra un punto de datos por cada atributo en un objeto. Este ejemplo cuesta ocho puntos de datos: cada objeto de mascota tiene cuatro atributos y hay dos objetos.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Mochi"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Pixel"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab Actualizar %}

Actualizar un conjunto existente registra un punto de datos por cada propiedad agregada. Este ejemplo cuesta dos puntos de datos, ya que solo actualiza una propiedad en cada uno de los dos objetos.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab Eliminar %}

Eliminar un objeto de un conjunto registra un punto de datos por cada criterio de eliminación que envíes. Este ejemplo cuesta tres puntos de datos, aunque puedas estar eliminando múltiples perros con esta declaración.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}