---
nav_title: Cancelar Conteúdo conectado
article_title: Cancelar Conteúdo conectado
page_order: 2
description: "Este artigo de referência aborda algumas práticas recomendadas para cancelamento de mensagens com Conteúdo conectado."
---

# Cancelar Conteúdo conectado {#aborting-connected-content}

> Ao usar templates com Liquid, você tem a opção de cancelar mensagens com lógica condicional. Esta página aborda as práticas recomendadas para isso.

No exemplo a seguir, as condições `connected.recommendations.size < 5` e `connected.foo.bar == nil` especificam situações em que a mensagem seria cancelada.

{% raw %}
```
{% connected_content https://example.com/webservice.json :save connected %}
   {% if connected.recommendations.size < 5 or connected.foo.bar == nil %}
     {% abort_message() %}
   {% endif %}
```
{% endraw %}

## Especificar um motivo de cancelamento {#specify-an-abort-reason}

Você também pode especificar um motivo de cancelamento, que será salvo no [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log). Esse motivo de cancelamento deve ser uma string e não pode conter Liquid.

{% raw %}
`{% abort_message('Could not get enough recommendations') %}`
{% endraw %}

{% alert important %}
A Braze não contabiliza mensagens canceladas na contagem de envios da sua conta da Braze nem no Currents.
{% endalert %}

{% multi_lang_include connected_content/abort_and_retry_logic.md %}