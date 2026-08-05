---
nav_title: "Filtro y objeto de audiencia conectada"
article_title: Objeto de audiencia conectada de API
page_order: 3
page_type: reference
description: "Este artículo explica el objeto de audiencia conectada, incluyendo cómo funciona, casos de uso y los diferentes filtros que lo crean."

---

# Objeto de audiencia conectada {#connected-audience-object}

> Una audiencia conectada es un filtro de audiencia dinámico que defines en línea dentro de tu solicitud de API, para que puedas dirigirte a los usuarios correctos en el momento del envío sin crear ni gestionar segmentos en el panel de Braze.

En lugar de crear previamente un segmento para cada posible combinación de audiencia, pasas los criterios de filtro directamente en tu llamada a la API. Dependiendo del endpoint, este objeto se pasa como `audience` o `custom_audience`. Braze evalúa a cada usuario contra esos criterios en tiempo real y entrega el mensaje solo a los usuarios que coincidan. Esto significa que una sola Campaign, Canvas o definición de mensaje solo de API puede servir a un número ilimitado de variaciones de audiencia, impulsadas completamente por tu lógica de negocio.

## Cómo funciona {#how-it-works}

1. Define tu mensaje creando una Campaign o un Canvas activados por API en el panel de Braze, o define el contenido del mensaje completamente en línea usando los [objetos de mensajería]({{site.baseurl}}/api/objects_filters#messaging-objects) en tu solicitud de API. Usa las [propiedades de activación]({{site.baseurl}}/api/objects_filters/trigger_properties_object) o el [contexto de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) para la personalización dinámica.
2. Llama a un endpoint compatible e incluye tus filtros de audiencia conectada en el parámetro `audience`, o en `custom_audience` para `/messages/live_activity/start`. Puedes filtrar por atributos personalizados, estado de suscripción push, estado de suscripción de correo electrónico y hora de último uso de la aplicación.
3. Braze evalúa los filtros en el momento del envío, entregando el mensaje solo a los usuarios que coincidan con tus criterios.

{% alert tip %}
No se requiere un `campaign_id` cuando se usa el parámetro `audience`. Los endpoints [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) y [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages) te permiten definir el contenido del mensaje en línea sin una Campaign creada previamente. Sin embargo, si deseas rastrear métricas a nivel de Campaign (como envíos, clics o rebotes) en el panel, incluye un `campaign_id`.
{% endalert %}

Dado que la audiencia se define por solicitud, tus sistemas de backend pueden activar mensajes contextualmente relevantes en respuesta a cualquier evento de negocio (un cambio de precio, una alerta meteorológica, una actualización de puntuación en vivo) sin intervención del panel.

### Endpoints compatibles {#compatible-endpoints}

Puedes usar el objeto de audiencia conectada en estos endpoints:

- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)
- [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)
- [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages)
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns)
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases)
- [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start) (usa `custom_audience`)

Ten en cuenta que el parámetro `audience` no admite matriz de objetos.

## Ejemplos {#use-cases}

Usa audiencias conectadas en escenarios donde tus sistemas de backend detectan un evento y necesitan notificar a un conjunto de usuarios determinado dinámicamente:

| Categoría | Ejemplo |
| --- | --- |
| Alertas meteorológicas | Un proveedor de datos meteorológicos detecta un evento climático severo y envía notificaciones push a los usuarios cuyo atributo `preferred_city` coincide con el área afectada. |
| Deportes y eventos en vivo | Una aplicación deportiva envía actualizaciones de puntuación en tiempo real o alertas de partidos a los usuarios cuyo atributo `favorite_team` coincide con uno de los equipos que están jugando. |
| Contenido y entretenimiento | Un servicio de streaming notifica a los usuarios cuya matriz `favorite_shows` incluye el título de una serie cada vez que se estrena un nuevo episodio. |
| Comercio electrónico | Un comercio minorista en línea envía alertas de bajada de precio o de reposición de stock a los usuarios cuya matriz `wishlisted_products` incluye el ID del producto relevante. |
| Viajes | Una aplicación de viajes envía notificaciones de retraso de vuelo a los usuarios cuyo atributo `booked_flight` coincide con el número de vuelo afectado. |
| Servicios financieros | Una plataforma de trading alerta a los usuarios cuya matriz `watchlist` incluye un símbolo bursátil que ha cruzado un umbral de precio. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ejemplos" }

En cada caso, una sola Campaign o una definición de mensaje solo por API maneja todas las variaciones. Tu backend determina los valores de filtro y los pasa en la solicitud de API, por lo que no necesitas crear un Segment o una Campaign independiente para cada producto, programa, equipo o ubicación.

## Ejemplo de solicitud {#example-request}

El siguiente ejemplo utiliza el endpoint [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) para dirigirse a los usuarios que han marcado como favorito un programa específico y han optado por recibir notificaciones push:

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_shows",
          "comparison": "includes_value",
          "value": "Example Show"
        }
      },
      {
        "push_subscription_status": {
          "comparison": "is",
          "value": "opted_in"
        }
      }
    ]
  },
  "trigger_properties": {
    "show_title": "Example Show",
    "episode_title": "Season 3, Episode 1",
    "deep_link": "https://example.com/shows/example-show/s3e1"
  },
  "broadcast": false
}
```

## Cuerpo del objeto {#object-body}

El objeto de audiencia conectada se compone de un único filtro de audiencia conectada o de varios filtros de audiencia conectada combinados con los operadores `AND` y `OR`.

**Ejemplo con múltiples filtros:**

```json
{
  "AND":
    [
      Connected Audience Filter,
      {
        "OR" :
          [
            Connected Audience Filter,
            Connected Audience Filter
          ]
      },
      Connected Audience Filter
    ]
}
```

## Filtros de audiencia conectada {#connected-audience-filters}

Combina múltiples filtros con los operadores `AND` y `OR` para crear un filtro de audiencia conectada.

### Consideraciones {#considerations}

Las audiencias conectadas no pueden filtrar usuarios por:

 - Atributos predeterminados
 - Eventos personalizados
 - Segments
 - Eventos de participación con mensajes
 - Atributos personalizados anidados

Para utilizar estos filtros, te recomendamos incorporarlos en un Segment de audiencia y luego especificar ese Segment en el parámetro `segment_id` del [endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters). Cuando utilices otros endpoints, primero debes añadir el Segment a la Campaign o Canvas activado por API en el panel de Braze. Si necesitas filtrar por atributos anidados, utiliza un [Segment estándar]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) en su lugar.


### Filtro de atributo personalizado {#custom-attribute-filter}

Este filtro te permite segmentar en función de un atributo personalizado de un usuario. Estos filtros contienen hasta tres campos:

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": (String) the name of the custom attribute to filter on,
      "comparison": (String) one of the allowed comparisons to make against the provided value,
      "value": (String, Numeric, Boolean) the value to be compared using the provided comparison
    }
}
```

#### Comparaciones permitidas por tipo de datos {#allowed-comparisons-by-data-type}

El tipo de datos del atributo personalizado determina las comparaciones que son válidas para un filtro determinado.

| Tipo de atributo personalizado | Comparaciones permitidas |
| ---------------------| --------------- |
| Cadena | `equals`, `not_equal`, `matches_regex`, `does_not_match_regex`, `exists`, `does_not_exist`, `is_any_of`, `is_none_of` |
| Matriz | `includes_value`, `does_not_include_value`, `exists`, `does_not_exist`, `is_any_of`, `is_none_of` |
| Numérico | `equals`, `not_equal`, `greater_than`, `greater_than_or_equal_to`, `less_than`, `less_than_or_equal_to`, `exists`, `does_not_exist` |
| Booleano | `equals`, `not_equal`, `exists`, `does_not_exist` |
| Hora | `less_than_x_days_ago`, `greater_than_x_days_ago`, `less_than_x_days_in_the_future`, `greater_than_x_days_in_the_future`, `after`, `before`, `exists`, `does_not_exist` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comparaciones permitidas por tipo de datos" }

#### Advertencias sobre la comparación de atributos {#attribute-comparison-caveats}

| Comparación | Consideraciones adicionales |
| --- | --- |
| `value` | El `value` no es obligatorio cuando se utilizan las comparaciones `exists` o `does_not_exist`. `value` debe ser una cadena de fecha y hora en formato ISO 8601 cuando se utilizan las comparaciones `before` y `after`. |
| `matches_regex` | Cuando se utiliza la comparación `matches_regex`, el valor proporcionado debe ser una cadena. Para obtener más información sobre el uso de expresiones regulares con Braze, consulta [Expresiones regulares]({{site.baseurl}}/user_guide/engagement_tools/segments/regex#regex-with-braze) y [Tipos de datos de atributos personalizados]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview#custom-attribute-data-types). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Advertencias sobre la comparación de atributos" }

#### Comparaciones de múltiples valores {#multi-value-comparisons}

Tanto `is_any_of` como `is_none_of` admiten la coincidencia con múltiples valores en una sola comparación. Estas comparaciones funcionan tanto con atributos personalizados de tipo cadena como de tipo matriz.

- `is_any_of`: Coincide con los usuarios cuyo valor de atributo es igual a cualquiera de los valores proporcionados. El `value` puede ser una sola cadena o una matriz de cadenas.
- `is_none_of`: Coincide con los usuarios cuyo valor de atributo no coincide con ninguno de los valores proporcionados. El `value` puede ser una sola cadena o una matriz de cadenas. Ten en cuenta que los usuarios que no tienen el atributo en su perfil siempre califican para esta comparación.

Para atributos de tipo matriz:

- `includes_value` también puede aceptar una matriz de valores para comprobar si la matriz del usuario contiene alguno de los valores especificados.
- Cuando se utilizan `is_any_of` o `is_none_of` con atributos de tipo matriz, funcionan de la misma manera que `includes_value` y `does_not_include_value` respectivamente.

{% alert tip %}
Para la coincidencia de múltiples valores, utiliza `is_any_of` en lugar de `includes_value`.
{% endalert %}

#### Ejemplos de atributos personalizados {#custom-attribute-examples}

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": "eye_color",
      "comparison": "equals",
      "value": "blue"
    }
}
```

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_foods",
    "comparison": "includes_value",
    "value": "pizza"
  }
}
```

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "last_purchase_time",
    "comparison": "less_than_x_days_ago",
    "value": 2
  }
}
```

#### Ejemplos de comparaciones de múltiples valores {#multi-value-comparison-examples}

##### `is_any_of` con una matriz de cadenas {#is_any_of-with-an-array-of-strings}

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_color",
    "comparison": "is_any_of",
    "value": ["red", "blue", "green"]
  }
}
```

##### `is_none_of` con una matriz de cadenas {#is_none_of-with-an-array-of-strings}

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "subscription_tier",
    "comparison": "is_none_of",
    "value": ["bronze", "silver"]
  }
}
```

##### `includes_value` con una matriz (atributo de tipo matriz) {#includes_value-with-an-array-array-attribute}

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "subscribed_products",
    "comparison": "includes_value",
    "value": ["1001", "1002", "1003"]
  }
}
```

Esto coincide con los usuarios cuya matriz `subscribed_products` contiene cualquiera de los valores `"1001"`, `"1002"` o `"1003"`.

### Filtro de suscripción push {#push-subscription-filter}

Este filtro te permite segmentar en función del estado de suscripción push de un usuario.

#### Cuerpo del filtro {#filter-body}

```json
{
  "push_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Comparaciones permitidas:** `is`, `is_not`
- **Valores permitidos:** `opted_in`, `subscribed`, `unsubscribed`

### Filtro de suscripción de correo electrónico {#email-subscription-filter}

Este filtro te permite segmentar en función del estado de suscripción de correo electrónico de un usuario.

#### Cuerpo del filtro

```json
{
  "email_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Comparaciones permitidas:** `is`, `is_not`
- **Valores permitidos:** `opted_in`, `subscribed`, `unsubscribed`

### Filtro de última aplicación utilizada {#last-used-app-filter}

Este filtro te permite segmentar en función de cuándo el usuario utilizó la aplicación por última vez. Estos filtros contienen dos campos:

#### Cuerpo del filtro

```json
{
  "last_used_app":
  {
    "comparison": (String) one of the allowed comparisons listed,
    "value": (String) the value to be compared using the provided comparison
  }
}
```

- **Comparaciones permitidas:** `after`, `before`
- **Valores permitidos:** fecha y hora (cadena ISO 8601)