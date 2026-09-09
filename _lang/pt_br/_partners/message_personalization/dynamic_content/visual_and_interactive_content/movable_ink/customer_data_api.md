---
nav_title: Conexão com a API de dados de cliente
article_title: Conecte-se à API de dados de clientes da Movable Ink
description: "Este artigo de referência descreve como se conectar para ativar os dados de eventos de clientes armazenados na Braze para gerar conteúdo personalizado na Movable Ink usando a API de dados de clientes."
page_type: partner
search_tag: Partner
---

# Conecte-se à API de dados de clientes da Movable Ink {#connect-to-the-movable-ink-customer-data-api}

> A integração da API de dados de clientes da Braze e da Movable Ink permite que os profissionais de marketing ativem os dados de eventos de clientes armazenados na Braze para gerar conteúdo personalizado na Movable Ink.

A Movable Ink é capaz de ingerir eventos comportamentais da Braze por meio da API de dados de clientes. Os eventos serão armazenados nos perfis de usuário com base no ID de usuário exclusivo (UUID) que é passado para a Movable Ink.

Para saber mais sobre o Stories, a API de dados de clientes da Movable Ink e como a Movable Ink aproveita os dados comportamentais, visite os seguintes artigos da central de suporte:

- [Potencialize o conteúdo com dados comportamentais](https://support.movableink.com/hc/en-us/sections/360001239453-Power-content-with-behavioral-data)
- [Introdução e guia da API de dados de clientes](https://support.movableink.com/hc/en-us/articles/13815957200663-Customer-Data-API-introduction-and-guide)
- [Perguntas frequentes: API de dados de clientes](https://support.movableink.com/hc/en-us/articles/12423178752279-FAQ-Customer-Data-API)

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta da Movable Ink | É necessário ter uma conta da Movable Ink para aproveitar essa parceria. |
| Credenciais da API da Movable Ink | A equipe de soluções da Movable Ink gerará credenciais de API para você. As credenciais da API consistem em:{::nomarkdown}<ul><li>Um URL de endpoint (para onde os dados serão enviados)</li><li>Nome de usuário e senha (usados para autenticar a API)</li></ul>{:/} Se desejar, a Movable Ink poderá fornecer o nome de usuário e a senha como um valor codificado em base64 a ser usado como um valor de cabeçalho de autorização básica. |
| Cargas úteis de eventos comportamentais | Será necessário compartilhar as cargas úteis do evento com a equipe de experiência do cliente da Movable Ink. Consulte [Compartilhamento de cargas úteis de eventos](#event-payloads) com a Movable Ink para obter detalhes. |
| Ativos criativos e lógica de negócios | Será necessário compartilhar ativos criativos com a Movable Ink, incluindo arquivos do Adobe Photoshop (PSD) que orientem a Movable Ink sobre como criar o bloco e uma imagem de fallback. Você também precisará fornecer a lógica de negócios para saber como e quando exibir o bloco de conteúdo ativado pelo parceiro. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Criar uma campanha de webhook na Braze {#step-1-create-a-webhook-campaign-in-braze}

#### Etapa 1a: Criar uma nova campanha {#step-1a-create-a-new-campaign}

1. Na Braze, [crie uma campanha de webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook).
2. Dê um nome e uma descrição opcional à sua campanha.
3. Selecione **Blank Template** como seu modelo.

#### Etapa 1b: Adicione suas credenciais da API de dados de clientes {#step-1b-add-your-customer-data-api-credentials}

1. No campo **Webhook URL**, insira o URL do endpoint da Movable Ink.

![Guia Redigir do criador do webhook na Braze com o URL do endpoint da Movable Ink e o corpo da solicitação definido como pares de chave/valor JSON.]({% image_buster /assets/img/movable_ink/cd_api_webhook_url.png %}){: style="max-width:75%" }

{:start="2"}
2. Selecione a guia **Settings**.
3. Adicione os seguintes cabeçalhos de solicitação como pares de chave-valor:

| Chave | Valor |
| --- | --- |
| Content-Type | application/json |
| Authorization | Insira a autenticação básica que você recebeu da Movable Ink. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 1b: Adicione suas credenciais da API de dados de clientes" }

![Guia Configurações do criador do webhook na Braze com pares de chave-valor para Content-Type e Authorization.]({% image_buster /assets/img/movable_ink/cd_api_webhook_settings.png %}){: style="max-width:75%" }

#### Etapa 1c: Configure sua carga útil {#step-1c-configure-your-payload}

1. Retorne à guia **Compose**.
2. Para o **Request Body**, crie seu próprio corpo de solicitação com pares de chave-valor JSON ou insira a carga útil do evento como texto bruto. Consulte as [cargas úteis de exemplo](#sample-payloads) para ver exemplos de eventos padrão de e-commerce.

![Guia Redigir do criador do webhook na Braze com pares de chave-valor JSON para ID, registro de data e hora, ID do usuário e tipo de evento.]({% image_buster /assets/img/movable_ink/cd_api_webhook_kvp.png %}){: style="max-width:75%" }

#### Etapa 1d: Teste seu webhook {#step-1d}

Será necessário compartilhar uma carga útil de exemplo com a equipe de experiência do cliente da Movable Ink. Você pode gerar essa carga útil na guia **Test** com base na carga útil que você construiu.

{% alert important %}
A Movable Ink recomenda esperar para testar seu webhook na Braze até que a equipe de experiência do cliente da Movable Ink tenha confirmado que concluiu o mapeamento e está pronta para receber um teste. Se esse mapeamento não estiver completo, você provavelmente receberá um erro ao testar.
{% endalert %}

Para testar seu webhook, faça o seguinte:

1. Selecione a guia **Test**.
2. Pré-visualize a mensagem como um usuário para ver uma amostra da carga útil do evento para esse usuário. Você pode escolher entre pré-visualizar como usuário aleatório, usuário específico ou usuário personalizado.
3. Se tudo estiver correto, clique em **Send test** para enviar uma solicitação de teste.

![Mensagem de resposta do webhook na Braze mostrando uma resposta 200 OK.]({% image_buster /assets/img/movable_ink/cd_api_webhook_response.png %}){: style="max-width:75%" }

### Etapa 2: Finalize a configuração da sua campanha {#step-2-finalize-your-campaign-setup}

#### Etapa 2a: Agende sua campanha {#step-2a-schedule-your-campaign}

Quando terminar de redigir e testar o webhook, [agende sua campanha]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

A Braze oferece suporte a entregas agendadas, baseadas em ação e disparadas por API. A [entrega baseada em ação]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) é geralmente a melhor opção para a maioria dos casos de uso de eventos comportamentais. Em caso de dúvidas sobre o que faz sentido para o seu caso de uso, entre em contato com os gerentes de sucesso do cliente da Braze e da Movable Ink.

Para entrega baseada em ação:

1. Especifique a ação-gatilho. Esse é o evento que disparará o webhook para a Movable Ink.
2. Certifique-se de que a **agendar/cronograma Delay** esteja definida como **Immediately**. Os dados do evento devem ser enviados à Movable Ink imediatamente após a ocorrência do evento, sem postergação.
3. Defina a duração da campanha especificando uma hora de início. É provável que um horário de término não seja aplicável, mas ele pode ser definido se necessário para o caso de uso.

{% alert note %}
Para garantir que os dados sejam transmitidos para a Movable Ink em tempo real, não selecione **Send campaign to users in their local time zone**.
{% endalert %}

#### Etapa 2b: Especifique seu público {#step-2b-specify-your-audience}

Em seguida, determine quais usuários você deseja direcionar para essa campanha. Para obter detalhes, consulte [Direcionamento de usuários]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users).

Certifique-se de não usar testes A/B em sua campanha, desmarcando a caixa de seleção **Control Group**. Se um grupo de controle for incluído, uma porcentagem dos usuários não terá dados enviados para a Movable Ink. Todo o seu público deve ir para a variante em vez do grupo de controle.

![Painel de testes A/B em uma Campaign da Braze com 100% de distribuição de variantes atribuída à Variante 1 e nenhum grupo de controle.]({% image_buster /assets/img/movable_ink/cd_api_webhook_ab.png %})

#### Etapa 2c: Escolha eventos de conversão (opcional) {#step-2c-choose-conversion-events-optional}

Se desejar, você pode atribuir eventos de conversão a essa campanha na Braze.

No entanto, como o webhook destina-se apenas ao envio de dados, a atribuição nesse nível é provavelmente menos útil do que analisar a atribuição no nível da campanha depois que os dados comportamentais da Braze são usados para personalizar o conteúdo.

### Etapa 3: Lance a campanha {#step-3-launch-the-campaign}

Revise a configuração do webhook e lance sua campanha.

## Considerações {#considerations}

### Alinhamento em um identificador de usuário exclusivo {#aligning-on-a-unique-user-identifier}

Certifique-se de que o valor do identificador exclusivo de usuário (UUID) que você está usando como `mi_u` esteja disponível na Braze e possa ser incluído nas cargas úteis do evento enviadas à Movable Ink.

Isso garante que os eventos comportamentais que a Movable Ink referencia ao gerar uma imagem sejam associados ao mesmo cliente para o qual receberam os eventos comportamentais. Se o valor do UUID não for o mesmo que o `external_id` da Braze, o UUID deverá ser capturado e passado para a Braze como atributo ou nas propriedades de um evento da Braze para aproveitar esse identificador.

A Braze rastreia o comportamento do usuário em várias plataformas (como web e app para dispositivos móveis), portanto, um único usuário pode ter várias IDs anônimas distintas. Essas IDs podem ser mescladas no perfil de usuário único conhecido do Stories quando um evento `identify` é enviado à Movable Ink, desde que o evento `identify` inclua um identificador anônimo e o identificador único conhecido.

Quando a Movable Ink receber um `user_id` para um único usuário, todos os eventos futuros desse usuário deverão incluir o mesmo `user_id`.

### Compartilhamento de cargas úteis de eventos com a Movable Ink {#event-payloads}

Antes de configurar o conector para a API de dados de clientes da Movable Ink, compartilhe as cargas úteis do evento com a equipe de experiência do cliente da Movable Ink. Isso permite que a Movable Ink mapeie seus eventos para o esquema de eventos deles e evitará qualquer chamada de API rejeitada ou com falha.

Você pode gerar uma carga útil de evento na Braze usando qualquer propriedade de evento. Gere uma carga útil de exemplo para um usuário aleatório ou pesquisando um ID de usuário específico. Consulte a [Etapa 1d](#step-1d) para obter detalhes.

Compartilhe essa carga útil de exemplo com a equipe de experiência do cliente da Movable Ink. Verifique se não há informações confidenciais de identificação pessoal na carga útil de exemplo (como endereço de e-mail, número de telefone ou datas de nascimento completas).

Para saber mais sobre as propriedades de eventos personalizados e o formato esperado dos dados contidos nas propriedades, consulte [Propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties).

### Usuários conhecidos versus anônimos {#known-versus-anonymous-users}

Na Braze, os eventos podem ser registrados em um perfil de usuário anônimo. Os identificadores vinculados ao perfil do usuário durante o registro de eventos dependem de como o usuário foi criado (por meio do SDK da Braze ou das APIs) e do estágio atual do ciclo de vida do usuário.

#### Encaminhar eventos da Braze apenas para usuários conhecidos {#only-forwarding-braze-events-for-known-users}

Na sua campanha de webhook, use o filtro `External User ID` para direcionar apenas os usuários que tenham um `external_id` com o filtro `External User ID` `is not blank`.

#### Encaminhar eventos da Braze para usuários anônimos e conhecidos {#forwarding-braze-events-for-anonymous-and-known-users}

Se quiser encaminhar eventos da Braze de usuários anônimos (usuários antes que um `external_id` seja atribuído ao perfil deles), será necessário decidir qual identificador usar como `anonymous_id` para a Movable Ink até que um `external_id` fique disponível. Escolha um `anonymous_id` que permanecerá constante no seu perfil de usuário da Braze. Você pode usar a lógica Liquid no corpo do webhook para decidir se deve passar um `anonymous_id` ou um `user_id`.

Para saber mais, consulte os exemplos de webhooks em [cargas úteis de exemplo](#sample-payloads).

## Exemplos de cargas úteis {#example-payloads}

### Evento de visualização de produto {#product-view-event}

{% tabs local %}
{% tab Example Braze Trigger Event %}

{% raw %}

```json
{
  "events": [
    {
      "email": "test@example.com",
      "name": "Product Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "categories": [
          {
            "id": "Bathroom",
            "url": "https://example.com/cat/bathroom"
          }
        ],
        "meta": {
          "color": "green"
        },
        "title": "All-Purpose Cleaning Wipes",
        "price": 1.99,
        "id": "56544",
        "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab Expected Movable Ink Request Payload %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "Bathroom",
        "url": "https://example.com/cat/bathroom"
      }
    ],
    "meta": {
      "color": "green"
    },
    "title": "All-Purpose Cleaning Wipes",
    "price": 1.99,
    "id": "56544",
    "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'

```

{% endraw %}
{% endtab %}
{% tab Example webhook %}

Neste exemplo, um endereço de e-mail com hash é usado como `anonymous_id` para usuários sem `external_id`.

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

// Condition logic to determine which identifier to use. If an external_id is available use that, otherwise use the anonymous_id
{% if {{${user_id}}} %}
{% capture user_identifier %}"user_id": "{{${user_id}}}"{% endcapture %}
{% else %}
{% capture user_identifier %}"anonymous_id": "{{anon_id}}"{% endcapture %}
{% endif %}

{
  {{user_identifier}}
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "{{event_properties.${categories}[0].id}}",
        "url": "{{event_properties.${categories}[0].url}}"
      }
    ],
    "meta": {
      "color": "{{event_properties.${meta}.color}}"
    },
    "title": "{{event_properties.${title}}}",
    "price": "{{event_properties.${price}}}",
    "id": "{{event_properties.${id}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
}

```

{% endraw %}
{% endtab %}
{% endtabs %}

### Evento de visualização de categoria {#category-view-event}

{% tabs local %}
{% tab Example Braze Trigger Event %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Category Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "id": "bathroom-1",
        "title": "Bathroom Stuff",
        "url": "https://www.example.com/categories/bathroom"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab Expected Movable Ink Request Payload %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "category_viewed",
  "properties": {
    "id": "bathroom-1",
    "title": "Bathroom Stuff",
    "url": "https://www.example.com/categories/bathroom"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'
```

{% endraw %}

{% endtab %}
{% tab Example webhook %}

Este exemplo mostra um webhook que rastreia eventos apenas para usuários conhecidos (usuários com `external_id`).

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

{
  "event": "category_viewed",
  "properties": {
    "id": "{{event_properties.${id}}}",
    "title": "{{event_properties.${title}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}

### Evento de identificação {#identify-event}

{% tabs local %}
{% tab Example Braze Trigger Event %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Account Created",
      "time": "2023-12-06T19:20:45+01:00"
    }
  ]
}
```

{% endraw %}
{% endtab %}
{% tab Expected Movable Ink Request Payload %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "jg0iq5gd30dqpwn8zmx05p06mzjmjir4r8",
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "identify",
  "user_id": "mycustomerid123"
}'
```

{% endraw %}
{% endtab %}
{% tab Example webhook %}

Neste exemplo, um endereço de e-mail com hash é usado como `anonymous_id` para usuários sem `external_id`.

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

{
  "anonymous_id": "{{anon_id}}",
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "identify",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}