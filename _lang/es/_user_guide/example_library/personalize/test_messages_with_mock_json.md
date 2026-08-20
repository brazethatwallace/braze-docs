---
nav_title: Probar mensajes con JSON simulado
article_title: Probar mensajes con JSON simulado en la vista previa
page_order: 1
page_type: reference
description: "Usa capture y json_parse de Liquid para simular contenido conectado o JSON de tipo entrada en la vista previa del creador de mensajes sin lanzar una campaña ni enviar mensajes de prueba."
---

# Probar mensajes con JSON simulado en la vista previa {#test-messages-with-mock-json-in-preview}

> Simula JSON de API o de tipo entrada dentro de tu mensaje con `capture` y `json_parse` para que puedas validar Liquid y el diseño en la vista previa del creador antes de lanzar una campaña, desencadenar un Canvas o llamar a contenido conectado en vivo.

## Acerca de este ejemplo {#about-this-example}

Flash & Thread, una marca ficticia de comercio minorista de ropa, crea mensajes que dependen de respuestas de contenido conectado, variables de contexto de Canvas o datos de perfil con arrays de objetos. Desencadenar llamadas reales a la API o lanzar Campaigns para cada iteración ralentiza el desarrollo.

Este patrón incorpora una carga útil JSON simulada en el cuerpo del mensaje, la almacena con `capture` y luego la analiza con `json_parse` para que Liquid pueda hacer referencia a campos estructurados en la sección de **vista previa**, sin necesidad de una llamada en vivo de contenido conectado, una entrada de Canvas desencadenada por API o un envío de prueba.

Usa esto durante el desarrollo de mensajes. No sustituye las pruebas de extremo a extremo con desencadenadores reales, envíos de prueba o [rutas de usuario en vista previa]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths) en Canvas.

## Consideraciones {#considerations}

- Este enfoque admite la vista previa del creador durante el desarrollo. Ejecuta envíos de prueba y verificaciones de ruta en vivo antes de lanzar a los clientes.
- Un bloque `capture` por sí solo almacena JSON como una cadena. Haz referencia a los campos solo después de aplicar **`json_parse`**; de lo contrario, la salida de la vista previa puede estar en blanco.
- El JSON simulado debe ser válido. Un JSON no válido provoca que `json_parse` falle o devuelva estructuras inesperadas.
- Elimina o quita los bloques simulados antes del lanzamiento, o protege el Liquid de producción para que los datos simulados se utilicen solo en la vista previa (por ejemplo, con un indicador de comentario que elimines antes de la puesta en marcha).
- Los fragmentos de código de Liquid en este artículo son ejemplos. Pruébalos en tus canales y con las formas reales de tu carga útil.
- Para el contenido conectado en producción, elimina el bloque simulado y utiliza tu etiqueta de URL en vivo. Consulta [Realizar una llamada a la API]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call).

## Configuración {#setup}

Este ejemplo simula una respuesta de listado de productos al estilo de contenido conectado para un correo electrónico que itera sobre `listings`.

### Paso 1: Captura el JSON simulado en el mensaje {#step-1-capture-mock-json-in-the-message}

Usa `capture` para almacenar la cadena JSON. Utiliza sintaxis JSON válida dentro del bloque (comillas dobles en las claves y los valores de cadena).

{% raw %}
```liquid
{% capture mock_response %}
{
  "success": true,
  "listings": [
    {
      "id": 45731,
      "name": "Summit Trail Jacket",
      "image_url": "https://example.com/images/trail-jacket.png",
      "price": {
        "actual": "89.00",
        "currency": "USD"
      },
      "link": "https://example.com/products/trail-jacket",
      "product_category": "Outerwear",
      "properties": {
        "size": "L",
        "colour": "Navy",
        "limited_edition": false
      },
      "out_of_stock": false
    }
  ]
}
{% endcapture %}
```
{% endraw %}

### Paso 2: Analiza el JSON con json_parse {#step-2-parse-json-with-json_parse}

Asigna la estructura analizada a una variable que puedas referenciar en el resto del mensaje.

{% raw %}
```liquid
{% assign response_json = mock_response | json_parse %}
```
{% endraw %}

Sin `json_parse`, la notación de punto sobre la cadena capturada (por ejemplo {% raw %}`{{ mock_response.listings }}`{% endraw %}) normalmente se muestra en blanco en la vista previa.

### Paso 3: Referencia los campos analizados en Liquid {#step-3-reference-parsed-fields-in-liquid}

Itera sobre el arreglo analizado y renderiza los campos como lo harías con una respuesta de API en vivo.

{% raw %}
```liquid
{% for listing in response_json.listings %}
{{ listing.name }} — {{ listing.price.actual }} {{ listing.price.currency }}
{% endfor %}
```
{% endraw %}

Ve a la sección **Preview** en el creador de mensajes y confirma que los campos se renderizan.

### Paso 4: Aplica el mismo patrón a otras estructuras JSON {#step-4-apply-the-same-pattern-to-other-json-shapes}

Usa el mismo flujo de `capture` + `json_parse` para simular:

| Datos que quieres probar | Estructura JSON simulada |
| --- | --- |
| Variables de contexto de Canvas | Objeto con las claves de propiedad que tu mensaje espera |
| Arreglo de objetos en un perfil | Arreglo JSON de objetos con las mismas claves que tu atributo personalizado |
| Respuesta de contenido conectado | JSON de API de ejemplo guardado de una llamada exitosa anterior |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Datos que quieres probar y estructura JSON" }

Reemplaza las variables simuladas por Liquid de producción (variables de contexto de Canvas, atributos personalizados o etiquetas de contenido conectado) antes de lanzar.

## Artículos relacionados {#related-articles}

- [Enviar mensajes de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages)
- [Vista previa de rutas de usuario en Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths)
- [Filtros avanzados de Liquid (`json_parse`)]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters)
- [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [Matriz de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)
- [Variables de contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables)