---
nav_title: Objetos anidados
article_title: Objetos anidados en eventos personalizados
page_order: 1
page_type: reference
description: "En este artículo se describe cómo enviar datos JSON anidados como propiedades de eventos personalizados y compras, y cómo utilizar esos objetos anidados en tu mensajería."
---

# Objetos anidados en eventos personalizados {#nested-objects-in-custom-events}

> Esta página explica cómo enviar datos JSON anidados como propiedades de eventos personalizados y compras, y cómo utilizar esos objetos anidados en tu mensajería.

Puedes usar objetos anidados —objetos que están dentro de otro objeto— para enviar datos JSON anidados como propiedades de eventos personalizados y compras. Estos datos anidados se pueden utilizar para crear plantillas con información personalizada en mensajes, desencadenar envíos de mensajes y segmentar usuarios.

## Consideraciones {#considerations}

- Los datos anidados son compatibles tanto con [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events) como con [eventos de compra]({{site.baseurl}}/user_guide/data/activation/events/purchase_events), pero no con otros tipos de eventos.
- Los objetos de propiedades de eventos que contienen valores de array u objeto pueden tener una carga útil de propiedades del evento de hasta 100 KB.
- No se pueden generar esquemas de propiedades de eventos para eventos de compra.
- Los esquemas de propiedades de eventos se generan mediante el muestreo de eventos personalizados de las últimas 24 horas.

### Versiones mínimas del SDK or kit de desarrollo de software {#minimum-sdk-versions}

Las siguientes versiones del SDK or kit de desarrollo de software admiten objetos anidados:

{% sdk_min_versions swift:5.0.0 android:20.0.0 web:3.3.0 %}

## Paso 1: Generar un esquema {#step-1-generate-a-schema}

Puedes acceder a los datos anidados en tu evento personalizado generando un esquema para cada evento con propiedades de eventos anidados. Para generar un esquema:

1. Ve a **Configuración de datos** > **Eventos personalizados**.
2. Selecciona **Administrar propiedades** para los eventos con propiedades anidadas.
3. Selecciona el botón <i class="fas fa-arrows-rotate"></i> para generar el esquema. Para ver el esquema, selecciona el botón de <i class="fas fa-plus"></i> más.

![Selecciona el botón para generar el esquema. Para ver el esquema, selecciona el botón de más.]({% image_buster /assets/img_archive/schema_generation_example.png %}){: style="max-width:80%;"}

Si se envían nuevas propiedades en el futuro, no estarán en el esquema hasta que se regenere. Los esquemas se pueden regenerar cada 24 horas.

## Paso 2: Usar el objeto anidado {#step-2-use-the-nested-object}

Puedes hacer referencia a los datos anidados durante la segmentación y la personalización. Ten en cuenta que no se requiere un esquema. Consulta las siguientes secciones para ver ejemplos de uso:

- [Cuerpo de la solicitud API](#api-request-body)
- [Plantillas Liquid](#liquid-templating)
- [Desencadenamiento de mensajes](#message-triggering)
- [Segmentación](#segmentation)
- [Personalización](#personalization)

### Cuerpo de la solicitud API {#api-request-body}

{% tabs %}
{% tab Music Example %}

El siguiente es un ejemplo de `/users/track` con un evento personalizado "Created Playlist". Después de que se haya creado una lista de reproducción, captura las propiedades de la lista de reproducción enviando:
- Una solicitud API que lista "songs" como propiedad
- Un array de las propiedades anidadas de las canciones

```
...
"properties": {
  "songs": [
    {
      "title": "Smells Like Teen Spirit",
      "artist": "Nirvana",
      "album": {
        "name": "Nevermind",
        "yearReleased": "1991"
      }
    },
    {
      "title": "While My Guitar Gently Weeps",
      "artist": "the Beatles",
      "album": {
        "name": "The Beatles",
        "yearReleased": "1968"
      }
    }
  ]
}
...
```
{% endtab %}
{% tab Restaurant Example%}

El siguiente es un ejemplo de `/users/track` con un evento personalizado "Ordered". Después de que se haya completado un pedido, captura las propiedades de ese pedido enviando:
- Una solicitud API que lista `r_details` como propiedad
- Las propiedades anidadas de ese pedido

```
...
"properties": {
  "r_details": {
    "name": "SandwichEmperor",
    "identifier": "12345678",
    "location" : {
      "city": "Montclair",
      "state": "NJ"
    }
  }
}
...
```
{% endtab %}
{% endtabs %}

{% alert note %}
Para las propiedades de eventos personalizados anidados, si el año es menor que 0 o mayor que 3000, Braze no almacena estos valores en el usuario.
{% endalert %}

### Plantillas Liquid {#liquid-templating}

A continuación se muestra cómo crear una plantilla Liquid que haga referencia a las propiedades anidadas solicitadas en la [solicitud API anterior](#api-request-body).

{% tabs %}
{% tab Music Example %}
Plantilla en Liquid en un mensaje desencadenado por el evento "Created Playlist":

{% raw %}
`{{event_properties.${songs}[0].album.name}}`: "Nevermind"<br>
`{{event_properties.${songs}[1].title}}`: "While My Guitar Gently Weeps"
{% endraw %}

{% endtab %}
{% tab Restaurant Example %}
Plantilla en Liquid en un mensaje desencadenado por el evento "Ordered":

{% raw %}
`{{event_properties.${r_details}.location.city}}`: "Montclair"
{% endraw %}

{% endtab %}
{% endtabs %}

### Desencadenamiento de mensajes {#message-triggering}

Para usar estas propiedades para desencadenar una campaña, selecciona tu evento personalizado o compra, y luego añade un filtro de **Nested Property**. Ten en cuenta que el desencadenamiento de mensajes aún no es compatible con mensajes dentro de la aplicación, pero las propiedades anidadas en la personalización Liquid de los mensajes se seguirán mostrando.

{% tabs %}
{% tab Music Example %}

Desencadenar una campaña con propiedades anidadas del evento "Created Playlist":

![Un usuario eligiendo una propiedad anidada para filtros de propiedades en un evento personalizado.]({% image_buster /assets/img/nested_object2.png %})

La condición de desencadenamiento `songs[].album.yearReleased` "is" "1968" coincidirá con un evento en el que cualquiera de las canciones tenga un álbum lanzado en 1968. Usamos la notación de corchetes `[]` para recorrer arrays, y coincide si **cualquier** elemento del array recorrido coincide con la propiedad del evento.

{% alert important %}
El filtro **does not equal** solo coincide si ninguna de las propiedades en tu array es igual al valor proporcionado. <br><br>Por ejemplo, supongamos que el Canvas A tiene el filtro de propiedad anidada de evento personalizado basado en acción **equals** "smartwatch", y el Canvas B tiene el filtro de propiedad anidada de evento personalizado basado en acción **does not equal** "simphone". Si tienes "smartwatch" y "simphone" en tus propiedades, ambos Canvas se desencadenarán. Pero si tienes "simphone" o "sim only" en cualquier propiedad, ningún Canvas se desencadenará.
{% endalert %}

{% endtab %}
{% tab Restaurant Example %}

Desencadenar una campaña con propiedades anidadas del evento "Ordered":

![Un usuario añadiendo el filtro de propiedad r_details.name is SandwichEmperor para un evento personalizado.]({% image_buster /assets/img/nested_object1.png %})

`r_details.name`: "SandwichEmperor"<br>
`r_details.location.city`: "Montclair"
{% endtab %}
{% endtabs %}

{% alert note %}
Si tu propiedad de evento contiene los caracteres `[]` o `.`, escápalos envolviéndolos entre comillas dobles. Por ejemplo, `"songs[].album".yearReleased` coincidirá con un evento con la propiedad literal `"songs[].album"`.
{% endalert %}

### Segmentación {#segmentation}

Para segmentar usuarios basándote en propiedades de eventos anidados, debes usar [Extensiones de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension). Después de haber generado un esquema, el explorador de objetos anidados aparecerá en la sección de segmentación.

![Captura de pantalla relacionada con la segmentación.]({% image_buster /assets/img_archive/nested_event_properties_segmentation.png %})

La segmentación usa la misma notación que el desencadenamiento (consulta [Desencadenamiento de mensajes](#message-triggering)).

Para editar o crear Extensiones de segmento, necesitarás el permiso "Edit Segments".

### Personalización {#personalization}

Usando el modal **Add Personalization**, selecciona **Advanced Event Properties** como tipo de personalización. Esto permite añadir propiedades de eventos anidados después de que se haya generado un esquema.

![Usando el modal Add Personalization, selecciona Advanced Event Properties como tipo de personalización. Esto permite añadir propiedades de eventos anidados después de que se haya generado un esquema.]({% image_buster /assets/img_archive/nested_event_properties_personalization.png %}){: style="max-width:70%;"}

## Probar objetos anidados en mensajes {#testing-nested-objects-in-messages}

La herramienta **vista previa & Test** del dashboard no admite añadir datos simulados para objetos anidados o atributos personalizados anidados. Para probar mensajes que hacen referencia a datos anidados a través de Liquid, puedes previsualizar mensajes con atributos anidados como un usuario existente que tenga ese atributo anidado, o previsualizar mensajes con propiedades de eventos personalizados lanzando una campaña en vivo a usuarios de prueba.

### Atributos personalizados anidados {#nested-custom-attributes}

1. Importa los atributos anidados al perfil del usuario de prueba a través de la API.
2. En tu campaña o Canvas, ve a **vista previa & Test**.
3. Selecciona **vista previa as user** y busca al usuario de prueba. El Liquid se resolverá usando los atributos anidados reales del perfil de ese usuario.

### Propiedades de eventos anidados {#nested-event-properties}

Las propiedades de eventos anidados no se pueden previsualizar en el dashboard porque requieren un desencadenamiento de evento en vivo. Para probar:

1. Crea una campaña o paso en Canvas que se dirija solo a tus usuarios de prueba y que sea desencadenada por (o haga referencia a) el evento personalizado con propiedades anidadas.
2. Lanza la campaña a tu audiencia de prueba.
3. Registra el evento personalizado con la carga útil del objeto anidado en el perfil de tu usuario de prueba (usando la API o el SDK or kit de desarrollo de software).
4. Verifica que el mensaje se renderice correctamente con los valores de las propiedades anidadas.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿El uso de objetos anidados registra puntos de datos adicionales? {#does-using-nested-objects-log-additional-data-points}

No hay cambios en cómo registramos puntos de datos como resultado de añadir esta capacidad. La segmentación basada en objetos anidados usa Extensiones de segmento, lo cual no consume puntos de datos adicionales.

### ¿Cuántos datos anidados se pueden enviar? {#how-much-nested-data-can-be-sent}

Si una o más de las propiedades del evento contienen datos anidados, la carga útil máxima para todas las propiedades combinadas de un evento es de 100 KB. Cualquier solicitud que supere ese límite de tamaño será rechazada.