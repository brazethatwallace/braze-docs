---
nav_title: RudderStack
article_title: RudderStack
description: "Este artículo describe la asociación entre Braze y RudderStack, una infraestructura de datos de clientes de código abierto que ofrece una integración perfecta de Braze para tus aplicaciones Android, iOS y web. Con RudderStack, puedes enviar los datos de eventos de tus clientes dentro de la aplicación directamente a Braze para un análisis contextual."
page_type: partner
search_tag: Partner

---

# RudderStack

> [RudderStack](https://rudderstack.com/) es una infraestructura de datos de clientes de código abierto para recopilar y enrutar datos de eventos de clientes a tu almacén de datos preferido y a docenas de otros proveedores de análisis, como Braze. Está preparado para la empresa y ofrece un sólido marco de transformación para procesar tus datos de eventos sobre la marcha.

La integración de Braze y RudderStack ofrece una integración de SDK nativa para tus aplicaciones Android, iOS y web, y una integración de servidor a servidor desde tus servicios backend.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Cuenta de RudderStack | Se requiere una [cuenta de RudderStack](https://app.rudderstack.com/) para beneficiarse de esta asociación. |
| Fuente configurada | Una [fuente](https://www.rudderstack.com/docs/dashboard-guides/sources/) es esencialmente el origen de cualquier dato enviado a RudderStack, como sitios web, aplicaciones móviles o servidores backend. Es necesario configurar la fuente antes de configurar Braze como destino en RudderStack. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`, `users.identify`, `users.delete` y `users.alias.new`.<br><br>Se puede crear en el panel de Braze desde **Configuración** > **Claves de API**. |
| Clave de la aplicación Braze | Para obtener la clave de tu aplicación en el panel de Braze, ve a **Configuración** > **Configuración de la aplicación** > **Identificación** y busca el nombre de tu aplicación. Guarda la cadena de identificador asociada.
| Centro de datos | Tu centro de datos se alinea con tu [instancia]({{site.baseurl}}/api/basics#endpoints) del panel de Braze.  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Añadir una fuente {#step-1-add-a-source}

Para empezar a enviar datos a Braze, primero debes asegurarte de que se ha configurado una fuente en tu aplicación RudderStack. Visita [RudderStack](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#getting-started) para saber cómo configurar tu origen de datos.

### Paso 2: Configurar destino {#step-2-configure-destination}

Ahora que tu fuente de datos está configurada, en el dashboard de RudderStack, selecciona **ADD DESTINATION** en **Destinations**. En la lista de destinos disponibles, selecciona **Braze** y haz clic en **Next**.

En el destino Braze, proporciona la clave de la aplicación, la clave de API REST de Braze, el clúster de datos y la opción de SDK nativo (solo en modo dispositivo). La opción de SDK nativo utilizará el SDK nativo de Braze para enviar eventos si está activada.

### Paso 3: Elige el tipo de integración {#step-3-choose-the-type-of-integration}

Puedes elegir integrar las bibliotecas web y nativas del lado del cliente de RudderStack con Braze utilizando uno de los siguientes enfoques:

- [Integración en paralelo / modo dispositivo](#device-mode)**:** RudderStack enviará los datos de eventos a Braze directamente desde tu cliente (navegador o aplicación móvil).
- [Servidor a servidor / modo nube](#cloud-mode)**:** El SDK de Braze envía los datos de los eventos directamente a RudderStack, que los transforma y enruta a Braze.
- [Modo híbrido](#hybrid-mode)**:** Utiliza el modo híbrido para enviar eventos autogenerados y generados por el usuario de iOS y Android a Braze utilizando una única conexión.

{% alert note %}
Obtén más información sobre los [modos de conexión](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/) de RudderStack y las ventajas de cada uno.
{% endalert %}

#### Integración en paralelo (modo dispositivo) {#device-mode}

Con este modo, puedes enviar tus eventos a Braze utilizando el SDK de Braze configurado en tu sitio web o aplicación móvil.

Configura los mapeados al SDK de RudderStack para tu plataforma en el repositorio de Braze en GitHub, como se describe en [métodos compatibles](#supported-methods):

- [Android](https://github.com/rudderlabs/rudder-integration-braze-android)
- [iOS](https://github.com/rudderlabs/rudder-integration-braze-ios/tree/master)
- [Swift](https://github.com/rudderlabs/rudder-integration-braze-swift)
- [Web](https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/Braze)
- [React Native](https://github.com/rudderlabs/rudder-sdk-react-native/tree/develop/libs/rudder-integration-braze-react-native)
- [Flutter](https://github.com/rudderlabs/rudder-sdk-flutter/tree/develop/packages/integrations/rudder_integration_braze_flutter)

Para completar la integración del modo dispositivo, consulta las instrucciones detalladas de RudderStack para [añadir Braze a tu proyecto](https://rudderstack.com/docs/destinations/marketing/braze/#adding-device-mode-integration).

#### Integración de servidor a servidor (modo nube) {#cloud-mode}

En este modo, el SDK envía los datos del evento directamente al servidor de RudderStack. A continuación, RudderStack transforma estos datos y los enruta al destino deseado. Esta transformación se realiza en el backend de RudderStack mediante el módulo transformador de RudderStack.

Para habilitar la integración, tendrás que asignar los métodos de RudderStack a Braze, como se describe en [métodos compatibles](#supported-methods).

{% alert note %}
Los SDK del lado del servidor de RudderStack (Java, Python, Node.js, Go, Ruby) solo admiten el modo nube. Esto se debe a que sus SDK del lado del servidor funcionan en el backend de RudderStack y no pueden cargar ningún SDK específico de Braze.
{% endalert %}

{% alert important %}
La integración de servidor a servidor no es compatible con las funciones de la interfaz de Braze, como las notificaciones push o los mensajes dentro de la aplicación. Sin embargo, estas funciones sí son compatibles con la integración del modo dispositivo.
{% endalert %}

#### Modo híbrido {#hybrid-mode}

Utiliza el modo híbrido para enviar todos los eventos a Braze desde tus fuentes iOS y Android.

Cuando eliges el modo híbrido para enviar eventos a Braze, RudderStack:
1. Inicializa el SDK de Braze.
2. Envía todos los eventos generados por el usuario (identify, track, page, screen y group) a Braze solo a través del modo nube y bloquea su envío a través del modo dispositivo.
3. Envía los eventos autogenerados (mensajes dentro de la aplicación, notificaciones push que requieren el SDK de Braze) a través del modo dispositivo.

Para [enviar eventos a través del modo híbrido](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-events-in-hybrid-mode), utiliza la opción de modo híbrido mientras conectas tu fuente al destino Braze. A continuación, añade la integración de Braze a tu proyecto.

## Paso 4: Configurar ajustes adicionales {#step-4-configure-additional-settings}

Tras completar la configuración inicial, configura los siguientes ajustes para recibir correctamente tus datos en Braze:

- **Enable subscription groups in group call**: Habilita esta configuración para enviar el estado del grupo de suscripción en tus eventos de grupo. Para más información, consulta [Group](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#group).
- **Use Custom Attributes Operation**: Habilita esta configuración si deseas utilizar la funcionalidad de [atributos personalizados anidados]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects) en Braze para crear segmentos y personalizar tus mensajes utilizando un objeto de atributo personalizado. Para más información, consulta [Send user traits as nested custom attributes](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-user-traits-as-nested-custom-attributes).
- **Track events for anonymous users**: Habilita esta configuración para realizar un seguimiento de la actividad de usuarios anónimos y enviar esta información a Braze.

### Configuración del modo dispositivo {#device-mode-settings}

La siguiente configuración solo es aplicable si envías eventos a Braze a través del [modo dispositivo](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode):

- **Client-side Events Filtering**: Esta configuración te permite especificar qué eventos deben bloquearse o permitirse en Braze. Para obtener más información sobre esta configuración, consulta [Client-side Events Filtering](https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/).
- **Deduplicate Traits**: Habilita esta configuración para deduplicar los rasgos del usuario en la llamada [`identify`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#identify).
- **Show Braze logs**: Esta configuración solo es aplicable cuando se utiliza el [SDK de JavaScript](https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/) como fuente. Actívala para mostrar los registros de Braze a tus usuarios.
- **OneTrust Cookie Categories**: Esta configuración te permite asociar los grupos de consentimiento de cookies de [OneTrust](https://www.rudderstack.com/docs/sources/event-streams/sdks/onetrust/javascript/) a Braze.

## Métodos compatibles {#supported-methods}

Braze admite los métodos de RudderStack identify, track, screen, page, group y alias.

{% tabs %}
{% tab Identify %}

El [método `identify`](https://rudderstack.com/docs/destinations/marketing/braze/#identify) de RudderStack asocia a los usuarios con sus acciones. RudderStack captura un ID de usuario único y rasgos opcionales asociados a ese usuario, como nombre, correo electrónico, dirección IP, etc.

**Gestión de deltas para llamadas identify**<br>
Si envías eventos a Braze a través del modo dispositivo, puedes ahorrar costes deduplicando tus llamadas `identify`. Para ello, habilita la configuración **Deduplicate Traits** en el dashboard. RudderStack envía entonces solo los atributos (traits) cambiados o modificados a Braze.

**Eliminar un usuario**<br>
Puedes eliminar un usuario en Braze utilizando la [regulación de supresión con eliminación](https://www.rudderstack.com/docs/api/data-regulation-api/#adding-a-suppression-with-delete-regulation) de la [API de regulación de datos](https://www.rudderstack.com/docs/api/data-regulation-api/) de RudderStack.

{% endtab %}
{% tab Track %}

El [método `track`](https://rudderstack.com/docs/destinations/marketing/braze/#track) de RudderStack captura todas las actividades del usuario y las propiedades asociadas a dichas actividades.

**Pedido completado**<br>
Al utilizar la [API de comercio electrónico de RudderStack](https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/) para llamar al método track de un evento con el nombre `Order Completed`, RudderStack envía los productos incluidos en ese evento a Braze como [`purchases`]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data).

{% endtab %}
{% tab Screen %}

El [método `screen`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#screen) de RudderStack te permite registrar las vistas de pantalla móvil de tus usuarios con cualquier información adicional sobre la pantalla vista.

{% endtab %}
{% tab Page %}

El [método `page`](https://rudderstack.com/docs/destinations/marketing/braze/#page) de RudderStack te permite registrar las páginas vistas de tu sitio web. También captura cualquier otra información relevante sobre esa página.

{% endtab %}
{% tab Group %}

El [método `group`](https://rudderstack.com/docs/destinations/marketing/braze/#group) de RudderStack te permite asociar un usuario a un grupo.

**Estado del grupo de suscripción**<br>
Para actualizar el estado del grupo de suscripción, habilita el ajuste "Enable subscription groups in group call" en el dashboard de RudderStack y envía el estado del grupo de suscripción en la llamada de grupo.

{% endtab %}
{% tab Alias %}

El [método `alias`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#alias) de RudderStack te permite fusionar diferentes identidades de un usuario conocido. Ten en cuenta que RudderStack solo admite la llamada alias para Braze en modo nube.

{% endtab %}
{% endtabs %}

## Enviar rasgos de usuario como atributos personalizados anidados {#send-user-traits-as-nested-custom-attributes}

Puedes enviar los rasgos de usuario a Braze como atributos personalizados anidados y realizar operaciones de adición, actualización y eliminación en ellos. Para ello, habilita el ajuste "Use Custom Attributes Operation dashboard" en RudderStack mientras configuras el destino Braze. Esta función solo está disponible en modo nube.

Puedes enviar los rasgos de usuario como atributos personalizados anidados en tus eventos `identify` con el siguiente formato:
```javascript
rudderanalytics.identify("1hKOmRA4GRlm", {
  "cars": {
    "add": [{
      "age": 27,
      "id": 1,
      "name": "Alex Keener"
    }],
    "update": [{
        "age": 30,
        "id": 2,
        "identifier": "id",
        "name": "Rowan"
      },
      {
        "age": 27,
        "id": 1,
        "identifier": "id",
        "name": "Alex"
      }
    ]
  },
  "country": "USA",
  "email": "alex@example.com",
  "firstName": "Alex",
  "gender": "M",
  "pets": [{
      "breed": "beagle",
      "id": 1,
      "name": "Scooby",
      "type": "dog"
    },
    {
      "breed": "calico",
      "id": 2,
      "name": "Garfield",
      "type": "cat"
    }
  ]
})
```

Para enviar los rasgos de usuario como atributos de usuario personalizados a través de las llamadas `track`, `page` o `screen`, pasa `traits` como campo contextual en el evento:
```javascript
rudderanalytics.track("Product Viewed", {
    revenue: 8.99,
    currency: "USD",
 },{
  "traits": {
    "cars": {
      "add": [{
        "age": 27,
        "id": 1,
        "name": "Alex Keener"
      }],
      "update": [{
          "age": 30,
          "id": 2,
          "identifier": "id",
          "name": "Alex"
        },
        {
          "age": 27,
          "id": 1,
          "identifier": "id",
          "name": "Rowan"
        }
      ]
    },
    "city": "Disney",
    "country": "USA",
    "email": "alexa@example.com",
    "firstName": "Alexa",
    "gender": "woman",
    "pets": [{
        "breed": "beagle",
        "id": 1,
        "name": "Scooby",
        "type": "dog"
      },
      {
        "breed": "calico",
        "id": 2,
        "name": "Garfield",
        "type": "cat"
      }
    ]
  }
});
```

{% alert note %}
Para las operaciones de actualización y eliminación, `identifier` es una clave obligatoria. Si las operaciones add, update o remove no están presentes en el array anidado, RudderStack utiliza por defecto la operación create para crear las propiedades. Consulta [Matriz de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects) para obtener más información sobre el envío de atributos personalizados anidados.
{% endalert %}