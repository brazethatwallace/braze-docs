---
nav_title: API REST
article_title: API REST
page_order: 1
description: "Aprende a usar Contenido conectado para extraer datos de las API REST e incluirlos en tus mensajes para personalización en tiempo real."
---

# API REST

> Extrae datos de API REST externas directamente en tus mensajes en el momento del envío usando [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/). Esto te permite personalizar mensajes con información en tiempo real de tus propios servidores, servicios de terceros o cualquier punto de conexión de API accesible públicamente.

## Cómo funciona

{% raw %}
Contenido conectado realiza una solicitud HTTP a la URL que especifiques y luego almacena la respuesta para que puedas referenciarla con Liquid. Añade una etiqueta `{% connected_content %}` a tu mensaje, y Braze llamará al punto de conexión cuando se envíe el mensaje.

```liquid
{% connected_content https://api.example.com/user/{{${user_id}}}/recommendations :save recs %}
We think you'll love {{recs.top_pick}}!
```
{% endraw %}

Contenido conectado admite solicitudes GET y POST. Braze requiere que el servidor responda en un máximo de dos segundos, así que diseña tus puntos de conexión para baja latencia.

## Casos de uso comunes

| Caso de uso | Descripción |
| --- | --- |
| Recomendaciones de productos | Obtener selecciones de productos personalizadas de una herramienta de recomendaciones |
| Precios o inventario en tiempo real | Mostrar precios actuales o niveles de stock en el momento del envío |
| Contenido basado en el clima | Extraer datos meteorológicos locales para adaptar la mensajería |
| Saldos de puntos de fidelización | Mostrar recompensas o saldos de cuenta actualizados |
| Fuentes de contenido | Insertar las últimas publicaciones de blog, artículos o noticias |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Autenticación

Braze admite autenticación básica, autenticación por token y OAuth para las solicitudes de Contenido conectado. Puedes almacenar credenciales de forma segura en el panel de Braze en **Configuración** > **Contenido conectado** y referenciarlas en tus llamadas a la API.

Para más información, consulta [Realizar una llamada a la API de Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/#authentication-types).

## Manejo de errores

Si el punto de conexión devuelve un error o se agota el tiempo de espera, Braze muestra una cadena vacía en lugar de la respuesta de Contenido conectado. Puedes detectar fallos comprobando si la variable guardada es nula y, de forma condicional, cancelar el mensaje o mostrar contenido alternativo.

Para más información, consulta [Cancelar Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content/).

## Consideraciones de rendimiento

Dado que Braze entrega mensajes en gran volumen, tu servidor debe manejar miles de conexiones simultáneas. Usa almacenamiento en caché cuando sea apropiado y establece límites de velocidad en tus mensajes para evitar sobrecargar los puntos de conexión externos.

Para la referencia completa de Contenido conectado, consulta [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/).