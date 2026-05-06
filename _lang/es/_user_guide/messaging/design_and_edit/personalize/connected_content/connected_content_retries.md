---
nav_title: Reintentos de Contenido conectado
article_title: Reintentos de Contenido conectado
page_order: 5
description: "Este artículo de referencia cubre cómo gestionar los reintentos de Contenido conectado."

---

# Usar lógica de reintentos para Contenido conectado

> Esta página cubre cómo agregar reintentos a tus llamadas de Contenido conectado.

## Cómo funcionan los reintentos

Dado que el Contenido conectado depende de recibir datos de API, una API puede no estar disponible de forma intermitente mientras Braze realiza la llamada. En este caso, Braze admite lógica de reintentos para volver a intentar la solicitud usando retirada exponencial.

{% alert note %}
El `:retry` de Contenido conectado no está disponible para mensajes dentro de la aplicación.
{% endalert %}

## Usar la lógica de reintentos

Para usar la lógica de reintentos, agrega la etiqueta `:retry` a la llamada de Contenido conectado, como se muestra en el siguiente fragmento de código:

{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

Cuando se incluye una etiqueta `:retry` en la llamada de Contenido conectado, Braze intentará reintentar la llamada hasta cinco veces.

### Resultados de los reintentos

#### Cuando un reintento tiene éxito

Si un intento reintentado tiene éxito, el mensaje se envía y no se realizan más reintentos para ese mensaje.

#### Cuando la llamada a la API falla y los reintentos están habilitados

Si la llamada a la API falla y esta opción está habilitada, Braze reintentará la llamada respetando el [límite de velocidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-speed-rate-limiting) que configuraste para cada reenvío. Braze moverá los mensajes fallidos al final de la cola y agregará minutos adicionales, si es necesario, al total de minutos que tomaría enviar tu mensaje.

Si la llamada de Contenido conectado falla más de cinco veces, el mensaje se cancela, de manera similar a cómo se desencadena una [etiqueta de cancelación de mensaje]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content/).

{% multi_lang_include connected_content/abort_and_retry_logic.md %}