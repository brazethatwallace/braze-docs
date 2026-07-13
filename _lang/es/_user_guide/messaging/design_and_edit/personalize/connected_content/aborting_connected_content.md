---
nav_title: Cancelar Contenido conectado
article_title: Cancelar Contenido conectado
page_order: 2
description: "Este artículo de referencia cubre algunas prácticas recomendadas para cancelar mensajes con Contenido conectado."
---

# Cancelar Contenido conectado {#aborting-connected-content}

> Cuando usas plantillas Liquid, tienes la opción de cancelar mensajes con lógica condicional. Esta página cubre las prácticas recomendadas para hacerlo.

En el siguiente ejemplo, las condiciones `connected.recommendations.size < 5` y `connected.foo.bar == nil` especifican situaciones que provocarían la cancelación del mensaje.

{% raw %}
```
{% connected_content https://example.com/webservice.json :save connected %}
   {% if connected.recommendations.size < 5 or connected.foo.bar == nil %}
     {% abort_message() %}
   {% endif %}
```
{% endraw %}

## Especificar un motivo de cancelación {#specify-an-abort-reason}

También puedes especificar un motivo de cancelación, que se guardará en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log). Este motivo de cancelación debe ser una cadena y no puede contener Liquid.

{% raw %}
`{% abort_message('Could not get enough recommendations') %}`
{% endraw %}

{% alert important %}
Braze no cuenta los mensajes cancelados en el recuento de envíos de tu cuenta de Braze ni en Currents.
{% endalert %}

{% multi_lang_include connected_content/abort_and_retry_logic.md %}