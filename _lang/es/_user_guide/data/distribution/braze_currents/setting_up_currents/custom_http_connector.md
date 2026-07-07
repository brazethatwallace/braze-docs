---
nav_title: Exportación de Currents personalizada
article_title: Exportación de Currents personalizada
alias: /currents/custom_http_connector/
page_order: 3
page_type: reference
tool: Currents
description: "Este artículo de referencia describe cómo configurar una exportación de Currents personalizada para transmitir datos de eventos de Braze Currents directamente a tu propio punto de conexión HTTP en tiempo real."
---

# Exportación de Currents personalizada {#custom-currents-export}

> Aprende a integrar un conector de Currents personalizado para obtener datos de eventos de Braze en tiempo real, lo que permite análisis, informes y automatización más personalizados.

{% alert note %}
Esta característica también se conoce como conector HTTP personalizado en la documentación técnica y las referencias de API.
{% endalert %}

## Requisitos previos {#prerequisites}

Para integrar un conector de Currents personalizado en Braze, necesitarás proporcionar una URL de punto de conexión y un [token de autenticación opcional](#authentication).

Además, si tienes más de un grupo de aplicaciones en Braze, necesitarás configurar un conector de Currents personalizado para cada grupo. Sin embargo, puedes apuntar todos los grupos de aplicaciones al mismo punto de conexión, o a un punto de conexión con un parámetro `GET` adicional, como `your_app_group_key="Brand A"`.

## Integración {#integration}

### Paso 1: Configura tu punto de conexión {#step-1-set-up-your-endpoint}

Necesitarás una URL de punto de conexión para configurar esta integración. Tu punto de conexión debe poder recibir solicitudes HTTP POST y devolver un código de estado `2XX` para confirmar la recepción correcta de los eventos. Si deseas autenticar las solicitudes de Braze, también necesitarás un token bearer.

### Paso 2: Configura Braze Currents {#step-2-configure-braze-currents}

En Braze, ve a **Integraciones de socios** > **Exportación de datos**, haz clic en **Crear nuevo Current** y selecciona **Exportación de Currents personalizada**.

Asigna un nombre a tu exportación y un correo electrónico de contacto, luego continúa a la página **Detalles del Current**. En esta página, introduce la URL de tu punto de conexión y el token bearer opcional.

Después de configurar tus credenciales, marca todos los eventos de interacción con mensajes, comportamiento del cliente y eventos de usuario que desees exportar, y haz clic en **Lanzar Current**.

## Eventos de Currents compatibles {#supported-currents-events}

Braze admite la exportación de los siguientes datos a tu conector HTTP personalizado:

- [Eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events?tab=custom%20http%20connector)
- [Eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events?tab=custom%20http%20connector)

Para ver la estructura de la carga útil de cada evento, selecciona la pestaña **Custom HTTP Connector** en el glosario de eventos.

## Prevención de pérdida de datos {#preventing-data-loss}

### Monitoreo de errores {#error-monitoring}

Para evitar la pérdida de datos y la interrupción del servicio, es esencial que monitorees tus puntos de conexión en todo momento y abordes rápidamente cualquier error o tiempo de inactividad.

Para la mayoría de los tipos de error (como errores del servidor y errores de conexión de red), Braze reintentará activamente las transmisiones de eventos. Si el problema persiste durante más de 5 días, la integración se deshabilitará automáticamente. Los nuevos eventos entrantes se descartarán y se perderán permanentemente.

### Resiliencia ante cambios {#change-resilience}

Ocasionalmente, realizaremos cambios no disruptivos en los esquemas de Braze Currents. Los cambios no disruptivos son nuevas columnas con valores nulos permitidos o nuevos tipos de eventos.

Normalmente damos un aviso de dos semanas para estos cambios, pero a veces esto no es posible. Es esencial que diseñes tu integración para manejar campos o tipos de eventos no reconocidos; de lo contrario, es probable que se produzca pérdida de datos.

{% alert tip %}
Para ver la lista completa de esquemas de eventos de Currents, consulta [Eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) y [Eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).
{% endalert %}

## Agrupación en lotes y serialización {#batching-and-serialization}

El formato de datos de destino es JSON sobre HTTPS. De forma predeterminada, los eventos se envían a tu punto de conexión en lotes de hasta 100 eventos cada uno.

Los eventos se envían al punto de conexión como un array JSON de todos los eventos en el siguiente formato:

```json
{"events": [event1, event2, event3, etc...]}
```

Habrá un objeto JSON de nivel superior con la clave `"events"` que se asigna a un array de objetos JSON adicionales, cada uno representando un evento individual. Cada evento contiene dos subobjetos:

| Nombre | Descripción |
|----|-----------|
| `"user"` | Contiene propiedades del usuario como `user_id`, `external_user_id`, `device_id` y `timezone`. |
| `"properties"` | Contiene atributos de un evento, como la `app/campaign/canvas/platform` a la que se aplica. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Si un punto de conexión posterior recibe una carga útil con cero eventos o un cuerpo de solicitud vacío, el resultado debe considerarse una operación nula, lo que significa que no deben producirse efectos posteriores a partir de esta llamada. Sin embargo, aún debes verificar el encabezado `Authorization` (como lo harías con una llamada API normal) y dar una respuesta HTTP apropiada para [credenciales no válidas](#authentication), como `401` o `403`. Esto permite a Braze saber que las credenciales del conector son válidas.

## Autenticación {#authentication}

Los tokens de autenticación en tu carga útil son opcionales. Se pueden pasar a través de un encabezado HTTP `Authorization` utilizando el esquema de autorización `Bearer`, como se especifica en [RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1). Aunque son opcionales, si se pasa un token de autenticación, Braze siempre lo validará primero&#8212;incluso si no hay eventos en la carga útil.

Según RFC 6750, los tokens deben ser valores codificados en Base64 con al menos un carácter. Ten en cuenta que RFC 6750 permite que los tokens contengan los siguientes caracteres además de los caracteres normales de Base64: `-`, `.`, `_` y `~`. Puedes elegir si deseas incluir estos caracteres en tu token o no&#8212;sin embargo, debe estar en formato Base64.

Además, si el encabezado `Authorization` está presente, se construirá utilizando el siguiente formato:

```plaintext
"Authorization: Bearer " + <token>
```

Por ejemplo, si tu token de autenticación es `0p3n5354m3==`, tu encabezado `Authorization` debería ser similar al siguiente:

```plaintext
Authorization: Bearer 0p3n5354m3==
```

{% alert note %}
En el futuro, es posible que utilicemos encabezados `Authorization` para implementar un esquema de autorización personalizado de pares clave-valor que sea exclusivo de Braze. Esto se ajustaría a la especificación [RFC 7235](https://tools.ietf.org/html/rfc7235), que es la forma en que algunas empresas implementan sus esquemas de autenticación, como Amazon Web Services (AWS).
{% endalert %}

## Versionado {#versioning}

Todas las solicitudes de nuestra integración de conector HTTP se enviarán con un encabezado personalizado que designa la versión de la solicitud de Currents que se está realizando:

```plaintext
Braze-Currents-Version: 1
```

La versión siempre será `1`, ya que no esperamos incrementar este número con mucha frecuencia, si es que alguna vez lo hacemos.

Al igual que nuestros [esquemas de almacenamiento en almacén de datos]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics?redirected=1), cada campo de evento en un evento individual tiene garantizada la compatibilidad con versiones anteriores de la carga útil del evento, según la definición de compatibilidad hacia atrás de [Apache Avro](https://avro.apache.org/):

1. Se garantiza que los campos de eventos específicos siempre tendrán el mismo tipo de datos a lo largo del tiempo.
2. Cualquier campo nuevo que se agregue a la carga útil con el tiempo debe ser considerado opcional por todas las partes.
3. Los campos obligatorios nunca se eliminarán.

## Manejo de errores y mecanismo de reintentos {#error-handling-and-retry-mechanism}

Si se produce un error, Braze pondrá en cola y reintentará la solicitud en función del código de retorno HTTP recibido. Si el problema persiste durante más de 5 días, la integración se deshabilitará automáticamente: los nuevos eventos entrantes se descartarán y se perderán permanentemente, y los eventos ya en cola se descartarán permanentemente después de retenerlos durante 7 días. Si los datos están atascados durante más de 24 horas, nuestros ingenieros de guardia recibirán una alerta automáticamente. Para un desglose completo de cómo se maneja cada código de estado, consulta la tabla a continuación.

Si tu integración de Currents está devolviendo errores de autenticación, Braze te enviará automáticamente un correo electrónico de notificación.

Cualquier código de error HTTP no listado a continuación se tratará como un error HTTP `5XX`.

{% alert warning %}
Si el problema persiste durante más de 5 días, la integración se deshabilitará. Los nuevos eventos entrantes se descartarán y se perderán permanentemente, y los eventos ya en cola se descartarán permanentemente después de retenerlos durante 7 días.
{% endalert %}

Los siguientes códigos de estado HTTP serán reconocidos por nuestro cliente conector:

<table aria-label="Manejo de errores y mecanismo de reintentos">
  <thead>
    <tr>
      <th>Código de estado</th>
      <th>Respuesta</th>
      <th>Descripción</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2XX</code></td>
      <td>Correcto</td>
      <td>Los datos del evento no se reenviarán.</td>
    </tr>
    <tr>
      <td><code>5XX</code></td>
      <td>Error del lado del servidor</td>
      <td>Los datos del evento se reenviarán con un patrón de retirada exponencial con fluctuación. Si el problema persiste durante más de 5 días, la integración se deshabilitará y los eventos ya en cola se retendrán durante 7 días.</td>
    </tr>
    <tr>
      <td><code>400</code></td>
      <td>Error del lado del cliente</td>
      <td>El conector envió al menos un evento con formato incorrecto. Los datos del evento se dividirán en lotes de tamaño 1 y se reenviarán. Cualquier evento en estos lotes de tamaño 1 que reciba otra respuesta <code>400</code> se descartará permanentemente.</td>
    </tr>
    <tr>
      <td><code>401</code></td>
      <td>No autorizado</td>
      <td>El conector se configuró con credenciales no válidas. Los eventos fallidos no se reenviarán. Corrige tus credenciales y vuelve a habilitar la integración para reanudar. Si el problema persiste durante más de 5 días, la integración se deshabilitará y los eventos ya en cola se retendrán durante 7 días.</td>
    </tr>
    <tr>
      <td><code>403</code></td>
      <td>Prohibido</td>
      <td>El conector se configuró con credenciales no válidas. Los eventos fallidos no se reenviarán. Corrige tus credenciales y vuelve a habilitar la integración para reanudar. Si el problema persiste durante más de 5 días, la integración se deshabilitará y los eventos ya en cola se retendrán durante 7 días.</td>
    </tr>
    <tr>
      <td><code>404</code></td>
      <td>No encontrado</td>
      <td>El conector se configuró con una URL de punto de conexión incorrecta o credenciales no válidas. Verifica que la URL de tu punto de conexión sea correcta y accesible. Corrige tu configuración y vuelve a habilitar la integración para reanudar. Si el problema persiste durante más de 5 días, la integración se deshabilitará y los eventos ya en cola se retendrán durante 7 días.</td>
    </tr>
    <tr>
      <td><code>413</code></td>
      <td>Carga útil demasiado grande</td>
      <td>Los datos del evento se dividirán en lotes más pequeños y se reenviarán.</td>
    </tr>
    <tr>
      <td><code>429</code></td>
      <td>Demasiadas solicitudes</td>
      <td>Indica limitación de velocidad. Los datos del evento se reenviarán con un patrón de retirada exponencial con fluctuación. Si el problema persiste durante más de 5 días, la integración se deshabilitará y los eventos ya en cola se retendrán durante 7 días.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }