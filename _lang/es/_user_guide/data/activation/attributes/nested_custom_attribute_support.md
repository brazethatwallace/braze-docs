---
nav_title: Atributos personalizados anidados
article_title: Atributos personalizados anidados
alias: "/nested_custom_attribute_support/"
page_order: 3
page_type: reference
description: "Este artículo de referencia cubre el uso de atributos personalizados anidados como tipo de datos para atributos personalizados, incluyendo limitaciones y ejemplos de uso."
---

# Atributos personalizados anidados {#nested-custom-attributes}

> Esta página trata de los atributos personalizados anidados, que te permiten definir un conjunto de atributos como propiedad de otro atributo. En otras palabras, cuando defines un objeto de atributo personalizado, puedes definir un conjunto de atributos adicionales para ese objeto.

{% multi_lang_include nested_attribute_objects/about_nested_attributes.md %}

{% multi_lang_include nested_attribute_objects/supported_data_types.md %}

## Consideraciones {#considerations}

- Los atributos personalizados anidados están pensados para atributos personalizados enviados a través del SDK o la API de Braze.
- Los objetos tienen un tamaño máximo de 100&nbsp;KB. Si una actualización hace que el objeto supere los 100&nbsp;KB, Braze descarta la actualización y el atributo permanece sin cambios.
- Los nombres de las claves y los valores de cadena tienen un límite de tamaño de 255 caracteres.
- Los nombres de las claves no pueden contener espacios.
- Los puntos (`.`) y los signos de dólar (`$`) no son caracteres compatibles en una carga útil de API si intentas enviar un atributo personalizado anidado a un perfil de usuario.
- No todos los partners de Braze admiten atributos personalizados anidados. Consulta la [documentación del partner]({{site.baseurl}}/partners/home) para confirmar si determinadas integraciones de partners admiten esta característica.
- Los atributos personalizados anidados no se pueden utilizar como filtro al realizar una llamada a la API de Connected Audience.
- De forma predeterminada, el filtro de segmentación **Atributos personalizados anidados** incluye atributos personalizados de tipo objeto, atributos de matriz de objetos y atributos personalizados de tipo matriz. Cuando seleccionas un atributo, el selector de esquema de propiedades incluye rutas de matriz (usando la notación `[]`) para campos de matriz anidados. Para ocultar los atributos personalizados de matriz de nivel superior de ese filtro, ponte en contacto con [soporte de Braze]({{site.baseurl}}/braze_support).
- Al previsualizar mensajes en el panel usando **Preview as a Custom User**, solo puedes introducir datos simulados como cadena o matriz de cadenas; los objetos anidados no son compatibles. Para previsualizar un mensaje que hace referencia a atributos personalizados anidados, selecciona un usuario existente que ya tenga el atributo anidado en su perfil. Para propiedades de eventos personalizados anidados, debes lanzar una campaña en vivo dirigida a un usuario de prueba para verificar la representación.

## Ejemplo de API {#api-example}

{% tabs local %}
{% tab Crear %}
El siguiente es un ejemplo de `/users/track` con un objeto "Most Played Song". Para capturar las propiedades de la canción, enviaremos una solicitud de API que lista `most_played_song` como un objeto, junto con un conjunto de propiedades del objeto.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab Actualizar %}
Para actualizar un objeto existente, envía un POST a `users/track` con el parámetro `_merge_objects` en la solicitud. Esto realizará una fusión profunda de tu actualización con los datos del objeto existente. La fusión profunda asegura que todos los niveles de un objeto se fusionen con otro objeto en lugar de solo el primer nivel. En este ejemplo, ya tenemos un objeto `most_played_song` en Braze, y ahora estamos añadiendo un nuevo campo, `year_released`, al objeto `most_played_song`.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "most_played_song": {
          "year_released": 1960
      }
    }
  ]
}
```

Después de recibir esta solicitud, el objeto de atributo personalizado se verá así:

```json
{"most_played_song": {
  "song_name": "Solea",
  "artist_name" : "Miles Davis",
  "album_name": "Sketches of Spain",
  "year_released": 1960,
  "genre": "Jazz",
  "play_analytics": {
     "count": 1000,
     "top_10_listeners": true
  }
}}
```

{% alert warning %}
Debes establecer `_merge_objects` en `true`, o tus objetos se sobrescribirán. `_merge_objects` es `false` de forma predeterminada.
{% endalert %}

{% endtab %}
{% tab Eliminar %}
Para eliminar un objeto de atributo personalizado, envía un POST a `users/track` con el objeto de atributo personalizado establecido en `null`.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": null
    }
  ]
}
```

{% alert note %}
Este enfoque no se puede usar para eliminar una clave anidada dentro de una [matriz de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects).
{% endalert %}

{% endtab %}
{% endtabs %}

## Ejemplo de SDK {#sdk-example}

{% sdk_min_versions android:25.0.0 ios:6.1.0 web:4.7.0 %}

{% tabs local %}
{% tab Android SDK %}

**Crear**
```kotlin
val json = JSONObject()
    .put("song_name", "Solea")
    .put("artist_name", "Miles Davis")
    .put("album_name", "Sketches of Spain")
    .put("genre", "Jazz")
    .put(
        "play_analytics",
        JSONObject()
            .put("count", 1000)
            .put("top_10_listeners", true)
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json)
}
```

**Actualizar**
```kotlin
val json = JSONObject()
    .put("year_released", 1960)

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json, true)
}
```

**Eliminar**
```kotlin
braze.getCurrentUser { user ->
    user.unsetCustomUserAttribute("most_played_song")
}
```

{% endtab %}
{% tab Swift SDK %}

**Crear**
```swift
let json: [String: Any?] = [
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": [
    "count": 1000,
    "top_10_listeners": true,
  ],
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json)
```

**Actualizar**
```swift
let json: [String: Any?] = [
  "year_released": 1960
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json, merge: true)
```

**Eliminar**
```swift
braze.user.unsetCustomAttribute(key: "most_played_song")
```

{% endtab %}
{% tab Web SDK %}

**Crear**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": {
    "count": 1000,
    "top_10_listeners": true
  }
};
braze.getUser().setCustomUserAttribute("most_played_song", json);
```

**Actualizar**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "year_released": 1960
};
braze.getUser().setCustomUserAttribute("most_played_song", json, true);

```

**Eliminar**
```javascript
import * as braze from "@braze/web-sdk";
braze.getUser().setCustomUserAttribute("most_played_song", null);
```

{% endtab %}
{% endtabs %}

## Capturar fechas como propiedades de objeto {#capturing-dates-as-object-properties}

Para capturar fechas como propiedades de objeto, debes usar la clave `$time`. En el siguiente ejemplo, se usa un objeto "Important Dates" para capturar el conjunto de propiedades de objeto, `birthday` y `wedding_anniversary`. Los valores de estas fechas son un objeto con una clave `$time`, que no puede ser un valor nulo.

{% alert note %}
Si no capturaste fechas como propiedades de objeto inicialmente, te recomendamos reenviar estos datos usando la clave `$time` para todos los usuarios. De lo contrario, esto puede resultar en segmentos incompletos al usar el atributo `$time`. Sin embargo, si el valor de `$time` en un atributo personalizado anidado no tiene el formato correcto, el atributo personalizado anidado completo no se actualizará.
{% endalert %}

```json
{
  "attributes": [
    {
      "external_id": "time_with_nca_test",
      "important_dates": {
        "birthday": {"$time" : "1980-01-01"},
        "wedding_anniversary": {"$time" : "2020-05-28"}
      }
    }
  ]
}
```

{% alert note %}
Para atributos personalizados anidados, si el año es menor que 0 o mayor que 3000, Braze no almacena estos valores en el usuario.
{% endalert %}

## Plantillas Liquid {#liquid-templating}

El siguiente ejemplo de plantilla Liquid muestra cómo hacer referencia a las propiedades del objeto de atributo personalizado guardadas desde la solicitud de API anterior y usarlas en tu mensajería.

Usa la etiqueta de personalización `custom_attribute` y la notación de punto para acceder a las propiedades de un objeto. Especifica el nombre del objeto (y la posición en la matriz si haces referencia a una matriz de objetos), seguido de un punto, seguido del nombre de la propiedad.

{% raw %}
`{{custom_attribute.${most_played_song}[0].artist_name}}` — "Miles Davis"
<br> `{{custom_attribute.${most_played_song}[0].song_name}}` — "Solea"
<br> `{{custom_attribute.${most_played_song}[0].play_analytics.count}}` — "1000"
{% endraw %}

Para usar Liquid de atributos personalizados anidados en tu mensaje:

1. Ve a una Campaign o Canvas, luego abre el paso de mensaje donde quieras añadir personalización.
2. En el creador de mensajes, inserta el fragmento de código Liquid donde quieras que aparezca el valor.
3. Usa **Preview & Test** con un usuario existente que ya tenga el atributo personalizado anidado en su perfil para confirmar que el valor se muestra como se espera.

### Personalización {#personalization}

Puedes usar **Add Personalization** para insertar un atributo personalizado anidado en tu mensaje.

Para abrir **Add Personalization**:

1. Ve a una Campaign o Canvas, luego abre el paso de mensaje donde quieras añadir personalización.
2. En el creador de mensajes, selecciona **Personalization** para abrir la barra lateral **Add Personalization**, donde puedes elegir opciones de personalización.

Para configurar la personalización de atributos personalizados anidados:

1. En **Personalization Type**, selecciona **Nested Custom Attributes**.
2. En **Top Level Attribute**, selecciona la ruta del atributo personalizado anidado que quieras insertar.
   Por ejemplo, selecciona `preferences.neighborhood_office`.
3. Opcional: En **Default value**, introduce un valor alternativo para los usuarios que no tengan su propio valor para ese atributo.
4. Revisa el **Liquid Snippet** generado para confirmar que coincide con la ruta esperada.
5. Selecciona **Insert**.

En este ejemplo, Braze inserta el valor anidado de `preferences.neighborhood_office` en tu mensaje. Los valores predeterminados son alternativas que tu mensaje incluye para los usuarios que no tienen su propio valor para un atributo.

{% alert tip %}
Verifica que se haya generado un esquema si no ves la opción de insertar atributos personalizados anidados.
{% endalert %}

## Regenerar esquemas {#regenerate-schema}

Después de que se haya generado un esquema, puedes regenerarlo **una vez por día calendario** (según la zona horaria de tu empresa). Esta sección describe cómo regenerar tu esquema. Para información más detallada sobre esquemas, consulta [Generar un esquema usando el explorador de objetos anidados]({{site.baseurl}}/user_guide/audience/segments/segment_with_nested_custom_attributes#generate-schema).

Para regenerar el esquema de tu atributo personalizado anidado:

1. Ve a **Configuración de datos** > **Atributos personalizados**.
2. Busca tu atributo personalizado anidado.
3. En la columna **Attribute Name** de tu atributo, selecciona <i class="fas fa-plus" aria-label="Administrar esquema"></i> **Administrar esquema** para administrar el esquema.
4. Aparecerá un modal. Selecciona **Regenerar esquema**.

La acción **Regenerar esquema** está limitada a **una vez por día calendario** en la zona horaria de tu empresa. No puedes iniciar otra regeneración mientras un trabajo de esquema ya está **en progreso** (la opción no está disponible mientras el estado es **Generating**). Regenerar el esquema solo detecta nuevos objetos y no elimina objetos que actualmente existen en el esquema.

{% alert important %}
Para restablecer el esquema de una matriz de objetos con un objeto existente, necesitas crear un nuevo atributo personalizado. La regeneración del esquema no elimina objetos existentes.
{% endalert %}

Si los datos no aparecen como se esperaba después de regenerar el esquema, es posible que el atributo no se ingiera con suficiente frecuencia. Los datos de usuario se muestrean a partir de datos anteriores enviados a Braze para el atributo anidado dado. Si el atributo no se ingiere lo suficiente, no será recogido para el esquema.

## Desencadenar cambios en atributos personalizados anidados {#trigger-nested-custom-attribute-changes}

Puedes desencadenar acciones cuando un objeto de atributo personalizado anidado cambia. Esta opción no está disponible para cambios en matrices de objetos. Si no ves una opción para ver el explorador de rutas, verifica que hayas generado un esquema.

Por ejemplo, en una campaña basada en acciones, puedes añadir una nueva acción desencadenante para **Change Custom Attribute Value** para dirigirte a usuarios que hayan cambiado sus preferencias de oficina de barrio.

Para configurar este desencadenador en una campaña basada en acciones:

1. Crea o edita una campaña, luego establece el tipo de entrega en **Entrega basada en acciones**.
2. En la configuración de desencadenadores, selecciona **Change Custom Attribute Value**.
3. Selecciona la ruta del atributo personalizado anidado que quieras monitorear.
   Por ejemplo, selecciona `preferences.neighborhood_office`.
4. Selecciona la condición de desencadenamiento que desees, como **any new value**.
5. Termina de configurar el mensaje y la audiencia de tu campaña, luego lánzala.

## Solución de problemas {#troubleshooting}

### Valores de atributos personalizados anidados no aplicados de forma consistente {#nested-custom-attribute-values-not-applied-consistently}

Si notas que los valores de atributos personalizados anidados no se están añadiendo a los perfiles de usuario de forma consistente, el problema suele estar relacionado con discrepancias en el tipo de datos.

Para diagnosticar y resolver este problema:

1. **Compara ejemplos de usuarios:** Obtén un ejemplo de usuario exitoso y uno no exitoso donde el atributo personalizado anidado debería haberse establecido.
2. **Revisa la estructura de datos:** Visualiza y compara los valores de atributos personalizados en ambos perfiles:
   - ¿Las propiedades están almacenadas bajo un objeto?
   - ¿Las propiedades están almacenadas como una matriz de propiedades?
3. **Verifica el filtro de segmentación:** Compara la estructura de datos almacenada con la forma en que el atributo personalizado anidado se referencia en tus filtros de segmentación.
4. **Verifica el tipo de datos:** Para identificar el tipo de datos de un atributo personalizado:
   - Ve a **Configuración de datos** > **Atributos personalizados**.
   - Busca el atributo personalizado de nivel superior que contiene el atributo anidado que quieras verificar.
   - Si la fila muestra **Generate Schema**, selecciónalo para generar el esquema primero.
   - Después de que se genere el esquema, selecciona el ícono de más en la columna **Attribute Name** de ese atributo.
   - En el modal **Edit schema**, revisa los atributos anidados y sus valores correspondientes en la columna **Data type**.

Si encuentras que el tipo de datos no coincide con el formato previsto en los perfiles de usuario, elimina el valor con formato incorrecto de los perfiles de usuario afectados y reenvía el atributo en el formato correcto usando la solicitud de API o el método de SDK apropiado.

## Comportamiento de segmentación con matrices de objetos {#segmentation-behavior-with-arrays-of-objects}

Cuando usas múltiples filtros de `Nested Custom Attribute` con lógica AND para segmentar en una matriz de objetos, cada filtro se evalúa de forma independiente en todos los elementos de la matriz. Un usuario califica para el segmento si _cualquier_ elemento de la matriz satisface cada filtro individual; los filtros no tienen que coincidir con el _mismo_ elemento.

Por ejemplo, supongamos que un usuario tiene la siguiente matriz:

```json
{
  "orders": [
    {"product": "Shoes", "price": 80},
    {"product": "Hat", "price": 25}
  ]
}
```

Un segmento con los siguientes filtros AND:

- `orders[].price` es mayor que 50
- `orders[].price` es menor que 30

Este usuario calificaría porque el primer filtro coincide con el elemento "Shoes" (80 > 50) y el segundo filtro coincide con el elemento "Hat" (25 < 30). Aunque ningún elemento individual satisface ambas condiciones, el usuario aún entra en el segmento.

Si necesitas que todas las condiciones coincidan con el mismo elemento dentro de una matriz, usa [segmentación multicriterio]({{site.baseurl}}/user_guide/audience/segments/segment_with_nested_custom_attributes#use-multi-criteria-segmentation) en la misma ruta, o reestructura tus datos para evitar la coincidencia entre elementos.

## Puntos de datos {#data-points}

Cualquier clave que se envíe consume un punto de datos. Por ejemplo, este objeto inicializado en el perfil de usuario cuenta como siete (7) puntos de datos:

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "year_released": 1960,
        "genre": "Jazz",
        "play_analytics": {
          "count": 1000,
          "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% alert note %}
Actualizar un objeto de atributo personalizado a `null` también consume un punto de datos.
{% endalert %}