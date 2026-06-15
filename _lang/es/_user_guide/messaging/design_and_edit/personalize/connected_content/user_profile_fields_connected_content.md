---
nav_title: Obtención de datos del perfil del usuario
article_title: Extraer datos de perfil de usuario en llamadas de contenido conectado
page_order: 3
description: "En este artículo se explica cómo incluir perfiles de usuario en las llamadas a Connected Content, así como las mejores prácticas en relación con las plantillas Liquid."
toc_headers: h2
---

# Extraer datos de perfil de usuario en llamadas de contenido conectado {#pull-user-profile-data-in-connected-content-calls}

> Esta página explica cómo introducir perfiles de usuario en tus llamadas de contenido conectado y las mejores prácticas de plantillas Liquid.

## Requisitos previos {#prerequisites}

Si una respuesta de contenido conectado contiene campos de perfil de usuario (dentro de una etiqueta de personalización de Liquid), estos valores deben definirse antes en el mensaje con Liquid, antes de la llamada de contenido conectado, para que el passback de Liquid se represente correctamente. De igual forma, la bandera `:rerender` debe incluirse en la solicitud. Ten en cuenta que el indicador `:rerender` solo tiene un nivel de profundidad, lo que significa que no se aplicará a ninguna etiqueta de contenido conectado anidada.

## Plantillas Liquid en llamadas de contenido conectado {#liquid-templating-in-connected-content-calls}

Para la personalización, Braze obtiene los campos de perfil de usuario antes de pasar ese campo a Liquid, por lo que si la respuesta de contenido conectado contiene campos de perfil de usuario, estos deben definirse de antemano.

Por ejemplo, si esta fuera la llamada de contenido conectado:
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}

La respuesta de contenido conectado es {% raw %}`Your language is ${language}`{% endraw %}. El contenido mostrado en este ejemplo es `Hi Jon, your language is`.

El idioma en sí no se procesará como plantilla. Esto se debe a que Braze necesita saber qué campos recuperar del usuario antes de realizar la llamada de contenido conectado.

Para renderizar correctamente el passback de Liquid, debes incluir la etiqueta {% raw %}`${language}`{% endraw %} en cualquier parte de la solicitud, como se muestra en el siguiente fragmento de código. El preprocesador de Liquid sabrá que debe obtener el atributo "language" del usuario para tenerlo listo para procesar la plantilla de la respuesta.

{%raw%}
```liquid
Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}

{% alert important %}
Recuerda que la opción del indicador `:rerender` solo funciona a un nivel de profundidad. Si la respuesta de contenido conectado contiene a su vez más etiquetas de contenido conectado o etiquetas de catálogo, Braze no volverá a renderizar esas etiquetas adicionales.
{% endalert %}

## Mejores prácticas {#best-practices}

### Usa `json_escape` con etiquetas de Liquid que puedan romper el formato JSON {#use-jsonescape-with-liquid-tags-that-could-break-the-json-format}

Al usar `:rerender`, agrega el filtro `json_escape` a cualquier etiqueta de Liquid que pueda potencialmente romper el formato JSON. Si tus etiquetas de Liquid contienen caracteres que rompen el formato JSON, toda la respuesta de contenido conectado se interpretará como texto y se procesará como plantilla en el mensaje, y ninguna de las variables se guardará.

Por ejemplo, si la propiedad de evento `message` en el ejemplo a continuación contiene caracteres que podrían romper el formato JSON, agrega el filtro `json_escape` como en este ejemplo:

{% raw %}
```liquid
[{
"message":"{{event_properties.${message} | json_escape}}"
}]
```
{% endraw %}