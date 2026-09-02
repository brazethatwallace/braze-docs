---
nav_title: Remerge
article_title: Remerge
alias: /partners/remerge/
description: "Este artigo de referência descreve a parceria entre a Braze e a Remerge, um app criado especificamente para redirecionamento em grande escala, fornecendo ferramentas para segmentar eficientemente os públicos do app e redirecionar os usuários."
page_type: partner
search_tag: Partner

---

# Remerge

> A [Remerge](https://www.remerge.io/) é criada para o redirecionamento de apps em larga escala, oferecendo ferramentas para segmentar públicos do app e redirecionar usuários de forma eficiente.

_Esta integração é mantida pela Remerge._

## Sobre a integração {#about-the-integration}

A integração da Braze com a Remerge ajuda você a desenvolver campanhas robustas de marketing de ciclo de vida em múltiplos canais, enviando dados de usuários para a Remerge via eventos de webhook para ajudar a redirecionar os usuários por meio de sua plataforma de demanda móvel.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta da Remerge | É necessário ter uma conta da Remerge para aproveitar esta parceria. |
| Chave de webhook da Remerge | Esta chave será fornecida pela Remerge. |
| ID do app para Android | Seu identificador exclusivo do aplicativo Braze para Android (como "com.example"). |
| ID do app para iOS | Seu identificador exclusivo do aplicativo Braze para iOS (como "012345678"). |
| Ativar a coleta de IDFA no SDK or kit de desenvolvimento de software da Braze | A coleta de IDFA é opcional no SDK or kit de desenvolvimento de software da Braze e fica desativada por padrão. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Crie seu modelo de webhook da Braze {#step-1-create-your-braze-webhook-template}

Para criar um modelo de webhook da Remerge para futuras campanhas ou Canvas, acesse **Conteúdo** > **Webhook** na plataforma Braze. Em seguida, selecione **Criar modelo de webhook**.


Se você quiser criar uma campanha de webhook única da Remerge ou usar um modelo existente, selecione **Webhook** na Braze ao criar uma nova campanha.

No seu novo modelo de webhook, preencha os seguintes campos:
- **Corpo da solicitação**: Texto bruto
- **URL do webhook**:
{% raw %}
```liquid
{% assign event_name = 'your_remerge_event_name' %}
{% assign android_app_id = 'your_android_app_id' %}
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'event_name','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

https://remerge.events/event?partner=braze&app_id=\{% if most_recently_used_device.${idfa} == blank %}android_app_id{% else %}iOS_app_id{% endif %}&key=1cs3p12k&ts='now' | date: '%s' }}&{% if {{most_recently_used_device.${idfa} == blank%}aaid=custom_attribute.${aaid}{% else %}idfa=most_recently_used_device.${idfa{%endif%}&event=event_name&non_app_event=true&data=json | url_param_escape

{% if most_recently_used_device.${idfa} == blank and custom_attribute.${aaid} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

Na URL do webhook, você precisa:
- Usar a API or interface de programação do aplicativo (API) `https://remerge.events/event` para enviar seus eventos de webhook.
- Definir o nome do evento. Esse nome aparecerá no seu dashboard da [remerge.io](https://www.remerge.io/).
- Passar o identificador exclusivo do aplicativo do seu app para Android (como "com.example") e iOS (como "012345678") para a Remerge.
- Definir uma chave; a Remerge a fornecerá.

![A URL do webhook e a pré-visualização da mensagem exibidos no construtor de webhook da Braze.]({% image_buster /assets/img_archive/webhook_remerge_preview.png %})

{% alert important %}
A Braze não coleta automaticamente o IDFA/AAID do dispositivo, então você deve armazenar esses valores por conta própria. Esteja ciente de que pode ser necessário obter o consentimento do usuário para coletar esses dados.
{% endalert %}

#### Cabeçalhos de solicitação e método {#request-headers-and-method}

O webhook da Remerge requer um método HTTP e um cabeçalho de solicitação.

- **Método HTTP**: GET
- **Cabeçalhos de solicitação**:
  - **Content-Type**: application/json

![Os cabeçalhos da solicitação, o método HTTP e a pré-visualização da mensagem exibidos no construtor de webhook da Braze.]({% image_buster /assets/img_archive/httpmethod_remerge.png %})

#### Corpo da solicitação {#request-body}

Você não precisa definir um corpo de solicitação para este webhook.

## Etapa 2: Visualize sua solicitação {#step-2-preview-your-request}

Visualize a mensagem para garantir que a solicitação esteja sendo renderizada corretamente para diferentes usuários. Recomendamos visualizar e enviar solicitações de teste para usuários de Android e iOS. Se a solicitação for bem-sucedida, a API or interface de programação do aplicativo (API) responderá com `HTTP 204`.

{% alert important %}
Lembre-se de salvar seu modelo antes de sair da página! <br>Os modelos de webhook atualizados podem ser encontrados na lista **Modelos de webhooks salvos** ao criar uma nova [campanha de webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/).
{% endalert %}