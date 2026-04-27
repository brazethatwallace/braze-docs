---
nav_title: Obtener datos del perfil de usuario
article_title: Obtener datos del perfil de usuario en llamadas de Contenido conectado
page_order: 3
description: "Este artículo explica cómo obtener perfiles de usuario en tus llamadas de Contenido conectado, así como las mejores prácticas relacionadas con las plantillas de Liquid."
toc_headers: h2
---

# Obtener datos del perfil de usuario en llamadas de Contenido conectado

> Esta página explica cómo obtener perfiles de usuario en tus llamadas de Contenido conectado y las mejores prácticas relacionadas con las plantillas de Liquid.

## Requisitos previos

Si una respuesta de Contenido conectado contiene campos del perfil de usuario (dentro de una etiqueta de personalización de Liquid), estos valores deben definirse antes en el mensaje con Liquid, antes de la llamada de Contenido conectado, para que el retorno de Liquid se renderice correctamente. De igual forma, el indicador `:rerender` debe incluirse en la solicitud. Ten en cuenta que el indicador `:rerender` solo funciona a un nivel de profundidad, lo que significa que no se aplicará a ninguna etiqueta de Contenido conectado anidada.

## Plantillas de Liquid en llamadas de Contenido conectado

Para la personalización, Braze obtiene los campos del perfil de usuario antes de pasar ese campo a Liquid, por lo que si la respuesta de Contenido conectado contiene campos del perfil de usuario, estos deben definirse de antemano.

Por ejemplo, si esta fuera la llamada de Contenido conectado:
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}

La respuesta de Contenido conectado es {% raw %}`Your language is ${language}`{% endraw %}. El contenido mostrado en este ejemplo es `Hi Jon, your language is`.

El idioma en sí no se procesará como plantilla. Esto se debe a que Braze necesita saber qué campos recuperar del usuario antes de realizar la llamada de Contenido conectado.

Para renderizar correctamente el retorno de Liquid, debes incluir la etiqueta {% raw %}`${language}`{% endraw %} en cualquier parte de la solicitud, como se muestra en el siguiente fragmento de código. El preprocesador de Liquid sabrá que debe obtener el atributo "language" del usuario para tenerlo listo para procesar la plantilla de la respuesta.

{%raw%}
```liquid
Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}

{% alert important %}
Recuerda que la opción del indicador `:rerender` solo funciona a un nivel de profundidad. Si la respuesta de Contenido conectado contiene a su vez más etiquetas de Contenido conectado o etiquetas de catálogo, Braze no volverá a renderizar esas etiquetas adicionales.
{% endalert %}

## Mejores prácticas

### Usa `json_escape` con etiquetas de Liquid que puedan romper el formato JSON

Al usar `:rerender`, agrega el filtro `json_escape` a cualquier etiqueta de Liquid que pueda potencialmente romper el formato JSON. Si tus etiquetas de Liquid contienen caracteres que rompen el formato JSON, toda la respuesta de Contenido conectado se interpretará como texto y se procesará como plantilla en el mensaje, y ninguna de las variables se guardará.

Por ejemplo, si la propiedad de evento `message` en el ejemplo a continuación contiene caracteres que podrían romper el formato JSON, agrega el filtro `json_escape` como en este ejemplo:

{% raw %}
```liquid
[{
"message":"{{event_properties.${message} | json_escape}}"
}]
```
{% endraw %}