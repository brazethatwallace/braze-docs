---
nav_title: "Objeto del evento"
article_title: "Objeto del evento"
page_order: 6
page_type: reference
description: "Este artículo de referencia repasa el objeto del evento, qué es y cómo es una parte crucial de las estrategias de Campaign basadas en eventos."
---

# Objeto del evento {#event-object}

> Este artículo explica los distintos componentes de un objeto del evento, cómo puedes utilizarlo y ejemplos en los que inspirarte.

## ¿Qué es un objeto de evento? {#what-is-an-event-object}

Un objeto de evento es un objeto que se pasa a través de la API cuando ocurre un evento específico. Los objetos de evento se alojan en una matriz de eventos. Cada objeto de evento en la matriz de eventos representa una única ocurrencia de un evento personalizado por parte de un usuario particular en el valor de tiempo designado. El objeto de evento tiene muchos campos diferentes que te permiten personalizar configurando y utilizando propiedades del evento en mensajes, recopilación de datos y personalización.

Para conocer los pasos para configurar eventos personalizados para una plataforma específica, consulta la Guía de integración de plataforma en la [Guía del desarrollador]({{site.baseurl}}/developer_guide/home). Consulta el artículo correspondiente según tu plataforma:

- [Android]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=web)

### Cuerpo del objeto {#object-body}

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  "app_id" : (optional, string) see App Identifier,
  "name" : (required, string) the name of the event,
  "time" : (required, datetime as string in ISO 8601 or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format),
  "properties" : (optional, Properties Object) properties of the event
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
  // See following notes regarding anonymous push token imports
}
```

{% alert note %}
Los eventos con marcas de tiempo en el futuro se registran de forma predeterminada con la hora actual. Esto garantiza que los eventos personalizados se registren con una temporización precisa.
{% endalert %}

- [ID de usuario externo]({{site.baseurl}}/api/basics#user-ids)
- [Identificador de aplicación]({{site.baseurl}}/api/identifier_types)
- [Código de tiempo ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)

{% alert note %}
Algunos pares de identificadores no se pueden usar juntos en una sola solicitud. Cuando se proporcionan tanto `email` como `phone`, `email` tiene prioridad sobre `phone`. Para obtener más detalles, consulta [Resolución de identificadores]({{site.baseurl}}/api/objects_filters/user_attributes_object#identifier-resolution).
{% endalert %}

#### Actualizar solo perfiles existentes {#update-existing-profiles-only}

Para actualizar solo perfiles de usuario existentes en Braze, debes pasar la clave `_update_existing_only` con un valor de `true` dentro del cuerpo de tu solicitud. Si se omite este valor, Braze creará un nuevo perfil de usuario si el `external_id` aún no existe.

{% alert note %}
Si estás creando un perfil de usuario de solo alias a través del endpoint `/users/track`, `_update_existing_only` debe establecerse en `false`. Si se omite este valor, el perfil de solo alias no se creará.
{% endalert %}

## Objeto de propiedades del evento {#event-properties-object}

Los eventos personalizados y las compras pueden tener propiedades del evento. Los valores de "properties" deben ser un objeto donde las claves son los nombres de las propiedades y los valores son los valores de las propiedades. Los nombres de las propiedades deben ser cadenas no vacías de 255 caracteres o menos, sin signos de dólar ($) al inicio.

Los valores de las propiedades pueden ser cualquiera de los siguientes tipos de datos:

| Tipo de datos | Descripción |
| --- | --- |
| Números | Como [enteros](https://en.wikipedia.org/wiki/Integer) o [flotantes](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Booleanos | `true` o `false` |
| Fechas y horas | Deben tener formato de cadenas en el formato [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) o en cualquiera de los siguientes formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>No se admiten dentro de arrays. <br><br>Ten en cuenta que "T" es un designador de hora, no un marcador de posición, y no debe cambiarse ni eliminarse. <br><br> Los atributos de hora sin zona horaria se establecerán de forma predeterminada a medianoche UTC (y se mostrarán en el panel como el equivalente de medianoche UTC en la zona horaria de la empresa). <br><br> Los eventos con marcas de tiempo en el futuro se establecerán de forma predeterminada a la hora actual.  |
| Cadenas | 255 caracteres o menos. |
| Arrays | Los arrays no pueden incluir fechas y horas. |
| Objetos | Los objetos se procesarán como cadenas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Objeto de propiedades del evento" }

Los objetos de propiedades del evento que contienen valores de array u objeto pueden tener una carga útil de propiedades del evento de hasta 100&nbsp;KB.

### Claves reservadas {#reserved-keys}

Las siguientes claves están reservadas y no pueden usarse como propiedades de eventos personalizados:

- `time`
- `event_name`

{% alert important %}
Usar claves reservadas como nombres de propiedades de eventos personalizados provocará errores de API al enviar solicitudes al endpoint `/users/track`.
{% endalert %}

### Persistencia de las propiedades del evento {#event-property-persistence}

Las propiedades del evento están diseñadas para el filtrado y la personalización con Liquid en los mensajes desencadenados por sus eventos principales. De forma predeterminada, no se conservan en el perfil de usuario de Braze. Para usar valores de propiedades del evento en la segmentación, consulta [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events), donde se detallan los diversos enfoques para almacenar valores de propiedades del evento a largo plazo.

#### Ejemplo de solicitud de evento {#event-example-request}

```http
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "events" : [
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:30+01:00"
    },
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "rented_movie",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "movie": "The Sad Egg",
        "director": "Alex Smith"
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:50+01:00"
    }
  ]
}
```
- [Wiki del código de hora ISO 8601](http://en.wikipedia.org/wiki/ISO_8601)

## Objetos de evento {#event-objects}

Usando el ejemplo proporcionado, podemos ver que alguien vio un tráiler recientemente y luego alquiló una película. Aunque no podemos entrar en una Campaign y segmentar a los usuarios en función de estas propiedades, podemos usarlas estratégicamente en forma de recibo, para enviar un mensaje personalizado a través de un canal utilizando Liquid. Por ejemplo, "Hola **Alex**, gracias por alquilar **The Sad Egg** de **Alex Smith**, aquí tienes algunas películas recomendadas basadas en tu alquiler..."