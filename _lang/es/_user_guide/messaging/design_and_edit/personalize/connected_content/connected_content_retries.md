---
nav_title: Reintentos de Contenido conectado
article_title: Reintentos de Contenido conectado
page_order: 5
description: "Este artículo de referencia cubre cómo gestionar los reintentos de Contenido conectado."

---

# Usar lógica de reintentos para Contenido conectado {#use-retry-logic-for-connected-content}

> Esta página cubre cómo agregar reintentos a tus llamadas de Contenido conectado.

## Cómo funcionan los reintentos {#how-retries-work}

Dado que el contenido conectado depende de la recepción de datos de las API, es posible que una API no esté disponible de forma intermitente mientras Braze realiza la llamada. En este caso, Braze admite lógica de reintentos para volver a intentar la solicitud utilizando retirada exponencial.

{% alert note %}
El `:retry` de contenido conectado no está disponible para mensajes dentro de la aplicación.
{% endalert %}

## Uso de la lógica de reintento {#using-retry-logic}

Para usar la lógica de reintento, añade la etiqueta `:retry` a la llamada de contenido conectado, como se muestra en el siguiente fragmento de código:

{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

Cuando se incluye una etiqueta `:retry` en la llamada de contenido conectado, Braze intenta reintentar la llamada hasta cinco veces.

### Comportamiento de la vista previa {#preview-behavior}

La lógica de reintento se aplica solo a los envíos en vivo (incluidos los envíos de prueba), no a las vistas previas. Si una llamada de contenido conectado con `:retry` falla durante la vista previa, esta puede mostrar el mensaje "This message would not have been shown because retry functionality was triggered" en lugar de renderizar el contenido. Este es el comportamiento esperado y no indica un problema dentro de Braze.

### Resultados de los reintentos {#retry-outcomes}

#### Cuando un reintento tiene éxito {#when-a-retry-succeeds}

Si un intento reintentado tiene éxito, el mensaje se envía y no se realizan más reintentos para ese mensaje.

#### Cuando la llamada a la API falla y los reintentos están habilitados {#when-the-api-call-fails-and-retries-are-enabled}

Si la llamada a la API falla y esta opción está habilitada, Braze reintentará la llamada respetando el [límite de velocidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) que hayas establecido para cada reenvío. Braze moverá los mensajes fallidos al final de la cola y añadirá minutos adicionales, si es necesario, al total de minutos que tardaría en enviar tu mensaje.

Si la llamada de contenido conectado falla más de cinco veces, el mensaje se cancela, de forma similar a como se desencadena una [etiqueta de cancelación de mensaje]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content).

{% multi_lang_include connected_content/abort_and_retry_logic.md %}