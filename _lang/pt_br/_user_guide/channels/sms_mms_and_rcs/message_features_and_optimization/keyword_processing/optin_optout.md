---
nav_title: Palavras-chave de opt-in e descadastramento
article_title: Palavras-chave de opt-in e descadastramento de SMS
page_order: 0
description: "Este artigo de referência aborda como a Braze processa palavras-chave básicas de opt-in e descadastramento para envio de mensagens SMS."
page_type: reference
alias: /optin_optout/
tool:
  - Dashboard

channel:
  - SMS
---

# Palavras-chave de opt-in e descadastramento {#opt-in-and-opt-out-keywords}

> As regulamentações exigem que haja respostas para todas as palavras-chave de opt-in, descadastramento e ajuda/informações. A Braze processa automaticamente as seguintes mensagens _exatas, de uma única palavra e sem distinção entre maiúsculas e minúsculas_, atualizando automaticamente o [estado do grupo de inscrições]({{site.baseurl}}/sms_rcs_subscription_groups/) do usuário e do número de telefone associado em todas as solicitações recebidas.

## Palavras-chave padrão {#default-keywords}

A Braze processa automaticamente as seguintes palavras-chave e atualiza o estado do grupo de inscrições para o número de telefone em todas as solicitações recebidas. Observe que essas palavras-chave e respostas padrão também podem ser personalizadas, e você pode adicionar [palavras-chave personalizadas]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling/).

{% alert tip %}
Quer expandir o processamento de descadastramento? Experimente o [descadastramento aproximado]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/fuzzy_opt_out/), um recurso que tenta reconhecer quando uma mensagem recebida não corresponde a uma palavra-chave de descadastramento, mas indica intenção de descadastramento.
{% endalert %}

| Tipo | Palavra-chave | Alteração |
|-|-------|---|
| Opt-in | `START`<br> `YES`<br> `UNSTOP` | Qualquer solicitação recebida com uma dessas palavras-chave de `Opt-In` resultará em uma alteração do estado do grupo de inscrições para `subscribed`. Além disso, o conjunto de remetentes associados a esse grupo de inscrições poderá enviar mensagens SMS, MMS ou RCS para esse cliente (dependendo do tipo de envio de mensagens compatível com os remetentes). <br><br>O usuário receberá sua resposta automática de opt-in definida. |
| Descadastramento | `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | Qualquer solicitação recebida com uma dessas palavras-chave de `Opt-Out` resultará em uma alteração do estado do grupo de inscrições para `unsubscribed`. Além disso, o conjunto de números associados a esse grupo de inscrições não poderá mais enviar mensagens para esse cliente.<br><br>O usuário receberá sua resposta automática de descadastramento definida. |
| Ajuda | `HELP`<br> `INFO` | O usuário receberá sua resposta automática de ajuda definida. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Default keywords" }

Apenas a **mensagem exata de uma única palavra** será processada (sem distinção entre maiúsculas e minúsculas). Palavras-chave como `STOP PLEASE` serão ignoradas, a menos que o [descadastramento aproximado]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/fuzzy_opt_out/) esteja ativado.

Se um destinatário usar as palavras-chave `HELP` ou `INFO`, uma resposta será disparada automaticamente. A resposta padrão para essas mensagens de resposta automática será definida durante o período de [integração]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/) e aquisição de número de telefone. Observe que você pode continuar atualizando essas respostas após o período inicial de integração.

{% alert tip %}
Quer expandir o processamento de descadastramento? Experimente o [descadastramento aproximado]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/fuzzy_opt_out/), um recurso que tenta reconhecer quando uma mensagem recebida não corresponde a uma palavra-chave de descadastramento, mas indica intenção de descadastramento.
{% endalert %}

## Lidar com descadastramentos em linguagem natural {#handle-natural-language-opt-outs}

Você pode criar um [Braze Agent]({{site.baseurl}}/user_guide/brazeai/agents/) que usa análise de sentimento para ajudar a capturar a intenção de descadastramento que não se enquadra nas palavras-chave padrão ou personalizadas (como "Por favor, não me mande mais mensagens"). Consulte [Lidar com descadastramentos em linguagem natural no Console do agente]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/#handle-natural-language-opt-outs-in-the-agent-console) para ver as etapas.