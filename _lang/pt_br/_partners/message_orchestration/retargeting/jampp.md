---
nav_title: Jampp
article_title: Jampp
alias: /partners/jampp/
description: "Este artigo de referência descreve a parceria entre a Braze e a Jampp, uma plataforma de marketing de performance usada para aquisição e redirecionamento de clientes móveis."
page_type: partner
search_tag: Partner

---

# Jampp

> A [Jampp](https://www.jampp.com/) é uma plataforma de marketing de performance usada para aquisição e redirecionamento de clientes móveis. A Jampp combina dados comportamentais com tecnologia preditiva e programática para gerar receita para os anunciantes, exibindo anúncios pessoais e relevantes que inspiram os consumidores a comprar pela primeira vez ou com mais frequência.

_Essa integração é mantida pela Jampp._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Jampp permite que os usuários da empresa sincronizem eventos na Jampp via eventos de webhook da Braze. Como resultado, os clientes podem adicionar conjuntos de dados mais ricos às suas iniciativas de redirecionamento dentro de seus ecossistemas de publicidade móvel.

Alguns exemplos de quando pode ser recomendável redirecionar clientes com um anúncio:
- Quando o estado de inscrição de e-mail ou push de um cliente muda.
- Como um cliente interagiu com uma campanha de mensagens da Braze.
- Se o cliente tiver acionado uma geofence específica.

## Pré-requisitos {#prerequisites}

Esta integração suporta apps iOS e Android.

| Requisito | Descrição |
|---|---|
| Conta da Jampp | Uma [conta Jampp](https://www.jampp.com/) é necessária para aproveitar esta parceria. |
| ID do app para Android | Seu identificador exclusivo do aplicativo Braze para Android (como "com.example"). |
| ID do app para iOS | Seu identificador exclusivo do aplicativo Braze para iOS (como "012345678"). |
| Ativar a coleta de IDFA no SDK da Braze | A coleta de IDFA é opcional no SDK da Braze e fica desativada por padrão. |
| Coleta de ID de publicidade do Google via atributo personalizado | A coleta de ID de publicidade do Google é opcional para os clientes e pode ser coletada como um [atributo personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types).
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integração {#integration}

### Etapa 1: Crie um modelo de webhook na Braze {#step-1-create-a-webhook-template-in-braze}

Para criar um modelo de webhook da Jampp para usar em futuras campanhas ou Canvas, acesse **Conteúdo** > **Webhook** no dashboard da Braze. Em seguida, selecione **Criar modelo de webhook**.

Se você quiser criar uma campanha de webhook única da Jampp ou usar um modelo existente, selecione **Webhook** na Braze ao criar uma nova campanha.

No seu novo modelo de webhook, preencha os seguintes campos:
- **Request Body**: Raw Text
- **Webhook URL**:
{% raw %}
```liquid
{% assign event_name = 'your_jampp_event_name' %}
{% assign android_app_id = 'your_android_app_id' %}
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'{{event_name}}','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

http://tracking.jampp.com/event?kind={{event_name}}&rnd={{rnd}}&app={% if {{most_recently_used_device.${idfa}}} == blank %}{{android_app_id}}{% else %}{{iOS_app_id}}{% endif %}&apple_ifa={{most_recently_used_device.${idfa}}}&google_advertising_id={{custom_attribute.${aaid}}}&user_agent={user-agent}&prtnr=braze

{% if {{most_recently_used_device.${idfa}}} == blank and {{custom_attribute.${aaid}}} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

Na URL do webhook, você precisa:
- Definir o nome do evento. Esse nome aparecerá no seu dashboard da Jampp.
- Passar o identificador exclusivo do aplicativo do seu app para Android (como "com.example") e iOS (como "012345678").
- Inserir [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid) para o atributo personalizado apropriado que você está rastreando como o ID de publicidade do Google. Observe que o ID de publicidade do Google está listado como `aaid` neste exemplo, mas você precisará substituí-lo pelo nome do atributo personalizado que seus desenvolvedores definiram.

![A URL do webhook e a pré-visualização da mensagem mostrados no construtor de webhook da Braze.]({% image_buster /assets/img/jampp_webhook.png %})

{% alert important %}
A Braze não coleta automaticamente o IDFA/AAID do dispositivo, então você deve armazenar esses valores. Esteja ciente de que você pode precisar do consentimento do usuário para coletar esses dados.
{% endalert %}

#### Cabeçalhos de solicitação e método {#request-headers-and-method}

O webhook da Jampp requer um método HTTP e um cabeçalho de solicitação.

- **HTTP Method**: GET
- **Request Headers**:
  - **Content-Type**: application/json

![Os cabeçalhos da solicitação, o método HTTP e a pré-visualização da mensagem mostrados no construtor de webhook da Braze.]({% image_buster /assets/img/jampp_method.png %})

#### Corpo da solicitação {#request-body}

Você não precisa definir um corpo de solicitação para este webhook.

### Etapa 2: Visualize sua solicitação {#step-2-preview-your-request}

Visualize a mensagem para garantir que a solicitação esteja sendo renderizada corretamente para diferentes usuários. Recomendamos visualizar e enviar solicitações de teste para usuários de Android e iOS. Se a solicitação for bem-sucedida, a API responderá com `HTTP 204`.

{% alert important %}
Lembre-se de salvar seu modelo antes de sair da página! <br>Os modelos de webhook atualizados podem ser encontrados na lista **Modelos de webhooks salvos** ao criar uma nova [campanha de webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/).
{% endalert %}