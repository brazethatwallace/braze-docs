---
nav_title: SessionM
article_title: SessionM
description: "Este artigo de referência descreve a parceria entre a Braze e a SessionM, uma plataforma de engajamento com clientes e fidelidade."
alias: /partners/sessionm/
page_type: partner
search_tag: Partner
---

# Plataforma de fidelidade SessionM {#sessionm-loyalty-platform}

> A [SessionM](https://sessionm.com/) é uma plataforma de engajamento com clientes e fidelidade, parte da Capillary Technologies, que oferece recursos de gerenciamento de campanhas e soluções de gerenciamento de fidelidade para ajudar os profissionais de marketing a impulsionar o direcionamento para aumentar o engajamento e a lucratividade.

## Pré-requisitos {#prerequisites}

| Origem | Requisito | Descrição |
| --- | --- | --- |
| Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com permissões `trigger_send`. Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. |
| Braze | Um endpoint REST or transferir estado representacional da Braze | Sua URL de endpoint REST or transferir estado representacional. Seu endpoint dependerá da URL da Braze para [sua instância]({{site.baseurl}}/api/basics#endpoints). |
| Braze e SessionM | Identificador correspondente | Para usar a integração, certifique-se de que tanto a SessionM quanto a Braze tenham um registro dos identificadores usados por cada plataforma. As referências a `user_id` correspondem ao identificador de usuário da SessionM gerado no momento da criação do perfil na SessionM. |
| SessionM | Uma conta SessionM | É necessário ter uma conta SessionM para aproveitar essa parceria. |
| SessionM | Um endpoint REST or transferir estado representacional do SessionM Core | Seu endpoint dependerá da URL da SessionM da sua instância. Isso pode ser criado no dashboard da SessionM em **Digital Properties**. |
| SessionM | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional do SessionM Core | A chave da API or interface de programação do aplicativo (API) da SessionM associada à sua instância e à integração da Braze. Essa chave pode ser usada para todas as chamadas baseadas em core, inclusive tags. Isso pode ser criado no dashboard da SessionM em **Digital Properties**. |
| SessionM | Um segredo da API or interface de programação do aplicativo (API) REST or transferir estado representacional do SessionM Core | O segredo da API or interface de programação do aplicativo (API) da SessionM associado à sua instância e à integração da Braze. Essa chave pode ser usada para todas as chamadas baseadas em core, inclusive tags. Isso pode ser criado no dashboard da SessionM em **Digital Properties**. |
| SessionM | Um endpoint REST or transferir estado representacional do SessionM Connect | Seu endpoint dependerá da URL da SessionM da sua instância. Entre em contato com o gerente técnico de conta da SessionM ou com a equipe de Delivery para obter. |
| SessionM | Uma string de autorização REST or transferir estado representacional do SessionM Connect | A string de autorização básica do SessionM Connect associada à sua instância. Essa string de autenticação pode ser usada para todas as chamadas baseadas em connect, incluindo get_user_offers. Entre em contato com o gerente técnico de conta da SessionM ou com a equipe de Delivery para obter. |
| SessionM | Um ID de varejista do SessionM Connect REST or transferir estado representacional | Um GUID de identificação exclusivo para o cliente específico associado à sua instância. Entre em contato com o gerente técnico de conta da SessionM ou com a equipe de Delivery para obter. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

Os casos de uso a seguir mostram algumas maneiras de aproveitar a integração da SessionM com a Braze.

- Crie uma segmentação que incorpore dados de todas as plataformas de fidelidade, gestão de clientes e envio de mensagens.
- Use a segmentação robusta para direcionar conjuntos específicos de usuários com ofertas e promoções.
- Aproveite as informações mais atualizadas sobre usuários, ofertas e fidelidade ao enviar mensagens.
- Forneça notificações detalhadas aos clientes sobre o progresso e a conclusão das atividades promocionais e de fidelidade.
- Notifique os clientes quando uma nova oferta for concedida e forneça os detalhes da oferta.

## Integração da SessionM com a Braze {#integrating-sessionm-with-braze}

### Etapa 1: Criar um Segment or segmento or segmento na Braze {#step-1-create-a-segment-in-braze}

Na Braze, crie um Segment or segmento or segmento de usuários para direcionar com promoções e ofertas da SessionM.

![Criador de segmentos com o filtro "Atributos personalizados" selecionado.]({% image_buster /assets/img/sessionm/CreateSegment.png %})

### Etapa 2: Importar segmentos da Braze para a SessionM {#step-2-import-braze-segments-into-sessionm}

#### Opção 1: Exportar para o endpoint SessionM Tag (recomendado) {#option-1-export-to-the-sessionm-tag-endpoint-recommended}

Primeiro, crie uma campanha de webhook na Braze e defina a URL do webhook como {% raw %}`{{endpoint_core}}/priv/v1/apps/{{appkey_core}}/users/{{${user_id}}}/tags`{% endraw %}. Use Liquid para definir o `user_id` na URL.

Usando um **corpo de solicitação** de texto bruto, crie o corpo do webhook para incluir as tags desejadas a serem adicionadas ao perfil do usuário na SessionM e o TTL desejado. Um exemplo é:

 ```
 {
   "tags":[
    "braze_test"
   ],
   "ttl":2592000
}
 ```

![Criador de webhook da SessionM com carga útil JSON para configuração de disparo de Campaign na Braze.]({% image_buster /assets/img/sessionm/SessionMWebhookComposer.png %}){: style="max-width:85%;"}

Na guia **Configurações**, adicione os pares de chave-valor para cada campo de cabeçalho de solicitação:
    - Crie uma chave `Content-Type` com o valor correspondente `application/json`
    - Crie uma chave `Authorization` com o valor correspondente `Basic YOUR-ENCODED-STRING-KEY`. Entre em contato com a equipe da SessionM para obter a chave de string codificada para o seu endpoint.

![Configurações de webhook.]({% image_buster /assets/img/sessionm/SessionMWebhookSettings.png %}){: style="max-width:85%;"}

Programe sua entrega, defina seu **Público-alvo** para direcionar ao Segment or segmento or segmento [que você criou anteriormente](#step-1-create-a-segment-in-braze) e, em seguida, lance sua campanha.

{% alert important %}
Esse processo também pode ser feito por meio de um cliente de API or interface de programação do aplicativo (API), como o Postman, fazendo uma solicitação diretamente ao [endpoint SessionM Tag](https://docs.sessionm.com/developer/APIs/Core/Customers/customers_tags.htm#create-or-increment-a-customer-tag), especificando o cliente, o nome da tag e um TTL para cada usuário na chamada (um único usuário por chamada).
<br><br>
O exemplo de solicitação a seguir usa cURL.

{% raw %}
```bash
curl --location -g --request POST '{{endpoint_core}}/priv/v1/apps/{{apikey_core}}/users/{{user_id}}/tags' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic {{base64_encoded_string}}' \
--data-raw '{
"tags":[
"tagname1",
"tagname2"
],
"ttl":20000
}'
```
{% endraw %}
{% endalert %}

#### Opção 2: Importação de CSV {#option-2-csv-import}

Exporte seu Segment or segmento or segmento da Braze usando o segmentador da Braze e forneça um arquivo CSV à SessionM que contenha os clientes a serem marcados, o nome da tag e um TTL para cada usuário no arquivo.

## Recuperação da carteira de ofertas em tempo real com a Braze {#retrieving-real-time-offer-wallet-with-braze}

A integração da SessionM com a Braze permite a extração em tempo real dos dados de usuários da SessionM no momento do envio da mensagem, usando Conteúdo Conectado, para eliminar o risco de comunicar aos clientes ofertas de fidelidade desatualizadas, expiradas ou já resgatadas.

O exemplo a seguir mostra o Conteúdo Conectado sendo usado para modelar dados da carteira de ofertas em uma mensagem. No entanto, o Conteúdo Conectado pode ser usado com qualquer um dos endpoints Connect da SessionM.

### Etapa 1: Emitir oferta na SessionM {#step-1-issue-offer-in-sessionm}

A SessionM emite ofertas para os clientes a partir de várias alavancas internas diferentes que podem ser configuradas. Após serem emitidas, as ofertas são movidas para um estado que a SessionM chama de "carteira de ofertas".

O cliente deve concluir a ação necessária ou atender ao direcionamento, e a oferta é emitida na SessionM.

Em seguida, a SessionM adiciona a oferta à carteira do cliente no estado emitido.

### Etapa 2: Chamar a API or interface de programação do aplicativo (API) SessionM Offer Wallet {#step-2-call-sessionm-offer-wallet-api}

Na etapa da Campaign ou do Canvas com as ofertas da SessionM, use o [Conteúdo Conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call) para fazer uma chamada de API or interface de programação do aplicativo (API) para o [endpoint `get_user_offers` da SessionM](https://domains-connecteast1.ent-sessionm.com/offers/swagger/ui/index#!/InfoV232583210323232323232323232323232This32API32allows32for32the32querying32of32information32about32offers32in32a32read45only32fashion4610323232323232323232323232May32be32initiated32by32the32dashboard32or32the32mobile32app4610323232323232323232323232/InfoV2_GetUserOffers/).

Na solicitação de Conteúdo Conectado, especifique o `user_id` da SessionM do usuário e seu `retailer_id` para recuperar a lista completa de ofertas ativas que o cliente tem em sua carteira. Cada solicitação a esse endpoint pode incluir um único usuário. Entre em contato com a equipe da SessionM para obter a chave de string codificada para o cabeçalho de autorização básica na sua chamada de Conteúdo Conectado.

No corpo da solicitação, `culture` tem como padrão `en-US`, mas é possível usar Liquid para modelar o idioma de um usuário para ofertas multilíngues da SessionM (por exemplo, usando {% raw %}`"culture":"{{${language}}}"`{% endraw %}).

{% raw %}
```
{% capture postbody %}
{"retailer_id":"YOUR-RETAIL-ID","user_id":"{{${user_id}}}","skip":0,"take":1000,"include_pending_extended_data":false,"culture":"en-US"}
{% endcapture %}

{% connected_content
     {{endpoint_connect}}/offers/api/2.0/offers/get_user_offers
:method post
:headers {
       "Content-Type": "application/json",
       "Authorization": "Basic YOUR-BASE64-ENCODED-KEY"
  }
     :body {{postbody}}
     :save wallet
%}
```
{% endraw %}

### Etapa 3: Preencher a carteira de ofertas para envio de mensagens da Braze {#step-3-populate-offer-wallet-to-braze-messaging}

Depois que uma solicitação é feita ao endpoint, a SessionM retorna a lista completa de ofertas no estado emitido, juntamente com os detalhes completos de cada oferta. Este é um exemplo de resposta retornada:

{% raw %}
```
{
    "status": "ok",
    "payload": {
      "user": {
        "opted_in": false,
        "activated": false,
        ...
      },
      "user_id": "00000000-0000-0000-0000-000000000000",
      "user_offers": [
        {
          "offer_id": "1a2b3324-1da6-4e49-b921-afc386dabb60",
          "offer_group_id": "00000000-0000-0000-0000-000000000000",
          "offer_type": "manual_fulfillment",
          ...
        }
      ],
      "total_records": 1,
      "offer_groups": [
        {
          "id": "00000000-0000-0000-0000-000000000000",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "offer_categories": [
        {
          "id": "9a82f973-aae6-4e10-839b-7117a852cf9e",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "total_points": 1000,
      "available_points": 100
    }
}
```
{% endraw %}

Usando a notação de ponto Liquid, isso pode ser preenchido na mensagem. Por exemplo, para personalizar a mensagem com o `offer_id` resultante, você pode aproveitar a carga útil de retorno usando {% raw %}`{{wallet.payload.available_points}}`{% endraw %}, que retorna `100`.

{% alert note %}
Essa é uma API or interface de programação do aplicativo (API) individual. Se pretender enviar um lote de mais de 500 usuários, entre em contato com a equipe da conta SessionM para saber como incorporar dados em massa na integração.
{% endalert %}

## Configuração do envio de mensagens disparadas {#setting-up-triggered-messaging}

A integração entre a SessionM e a Braze permite que os dados do perfil do usuário, os detalhes da oferta e os saldos de pontos sejam preenchidos dinamicamente no envio de mensagens e enviados em tempo real para o cliente no ponto de ação.

### Etapa 1: A equipe de Delivery da SessionM configura os modelos {#step-1-sessionm-delivery-team-configures-templates}

Colabore com a equipe de Delivery da SessionM para desenvolver modelos a serem usados no envio de mensagens disparadas. A SessionM inserirá dados do perfil do usuário, detalhes da oferta e saldos de pontos nas mensagens e as disparará na Braze para envio de mensagens em tempo real para o cliente.

Os campos padrão presentes em todos os modelos da SessionM incluem:
- `canvas_id`
- `campaign_id`
- `broadcast flag`
- `customer identifier`
- `email address`

{% alert note %}
Ao definir o `broadcast flag` como `true`, a mensagem será enviada para todo o Segment or segmento or segmento que a Campaign ou o Canvas direciona na Braze.
{% endalert %}

Campos adicionais podem ser configurados com base em necessidades específicas:

- **Dados da oferta:** `offer_id`, `offer title`, `user offer id`, `description`, `terms and conditions`, `logo`, `pos discount id`, `expiration date`
- **Dados do prêmio por pontos:** `point award amount`, `point account name`
- **Dados do evento-gatilho:** qualquer dado no evento-gatilho que utilize o resultado do webhook de disparo/envio
- **Dados específicos da campanha:** `campaign runtime`, `campaign_id`, `campaign name`, `campaign custom data`

Campos adicionais são enviados à Braze como `trigger_properties` para personalizar a mensagem.

### Etapa 2: Criar uma Campaign ou Canvas na Braze {#step-2-create-a-braze-campaign-or-canvas}

Crie uma Campaign disparada por API or interface de programação do aplicativo (API) ou um Canvas na Braze para ser disparado pela SessionM. Se campos adicionais tiverem sido configurados, como `offer_id` ou `offer title`, use Liquid (como {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %}) para adicionar os campos personalizados ao seu envio de mensagens.

![Propriedades do disparador da API.]({% image_buster /assets/img/sessionm/apiTriggerProperties.png %})

Na guia **Agendar entrega**, anote o ID da Campaign ou do Canvas, pois ele será adicionado às **Configurações avançadas** da campanha SessionM.

![Campaign disparada por API.]({% image_buster /assets/img/sessionm/apiTriggerCampaign.png %})

Finalize os detalhes da sua Campaign ou Canvas e selecione **Lançar**.

### Etapa 3: Criar uma campanha promocional ou de envio de mensagens da SessionM {#step-3-create-a-sessionm-promotional-or-messaging-campaign}

Em seguida, crie sua campanha na SessionM.

![Criação de campanha da SessionM.]({% image_buster /assets/img/sessionm/SessionMCampaignCreation.png %})

Atualize as configurações avançadas na campanha da SessionM para incluir a seguinte carga útil JSON contendo `braze_campaign_id` ou `braze_canvas_id`.

{% raw %}
```
{
"braze_campaign_id": "{{CAMPAIGN ID}}",
"braze_canvas_id": "{{CANVAS ID}}",
}
```
{% endraw %}

![Configurações avançadas da SessionM.]({% image_buster /assets/img/sessionm/SessionMAdvancedSettings.png %}){: style="max-width:85%;"}

Crie um disparo de mensagem com a programação ou o comportamento desejado. Em seguida, selecione **Braze Messaging Variant** como a **Messaging Variant** no menu **External Message** para usar o modelo.

![Mensagem externa da SessionM.]({% image_buster /assets/img/sessionm/SessionMExternalMessage.png %})

Esse modelo extrai os atributos estáticos e dinâmicos relevantes e faz a chamada ao endpoint da Braze.

![Modelo SessionM Braze.]({% image_buster /assets/img/sessionm/SessionMBrazeTemplate.png %}){: style="max-width:85%;"}