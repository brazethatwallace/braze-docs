---
nav_title: Seen
article_title: Seen
description: "A Seen permite experiências de vídeo personalizadas em grande escala, ajudando marcas a aumentar o engajamento ao longo da jornada do cliente."
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# Seen

> A [Seen](https://seen.io) permite que marcas criem e entreguem experiências de vídeo personalizadas em grande escala. Com a Seen, você pode projetar um vídeo em torno dos seus dados, personalizá-lo em grande escala na nuvem e distribuí-lo onde funciona melhor.
>
> A integração entre a Braze e a Seen permite que você envie dados de usuários da Braze para a Seen, gere vídeos personalizados dinamicamente e retorne ativos de vídeo — como uma URL de player única e miniatura — de volta para a Braze para uso em Campaigns e Canvas.


## Casos de uso {#use-cases}

A Seen suporta entrega automatizada de vídeo personalizado ao longo do ciclo de vida do cliente, incluindo:

- **Integração**: dê as boas-vindas a novos usuários com vídeos personalizados para seu perfil ou contexto de inscrição
- **Conversão e ativação**: reforce ações-chave com mensagens de vídeo contextuais
- **Fidelidade e upsell**: destaque ofertas personalizadas ou marcos de uso
- **Recuperação e prevenção de churn**: reengaje usuários inativos com conteúdo de vídeo personalizado


## Pré-requisitos {#prerequisites}

Antes de começar, você precisa do seguinte:

| Pré-requisito | Descrição |
|--------------|-------------|
| Acesso à plataforma Seen | Você precisa de uma assinatura da plataforma Seen ou de uma Campaign ativa da Seen. Você precisa de acesso às configurações do seu espaço de trabalho para recuperar seu ID de espaço de trabalho e gerar um token de API. |
| URL do webhook de Transformação de dados da Braze | A Transformação de dados da Braze reformata os dados recebidos da Seen para que possam ser aceitos pelo endpoint /users/track da Braze. |
| Dados de usuários da Braze | A personalização de vídeo requer dados em nível de usuário. Certifique-se de que os atributos relevantes estejam disponíveis na Braze e que você passe **braze_id** como o identificador único. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }




## Como funcionam as Journeys da Seen {#how-seen-journeys-work}

A Seen usa [Journeys](https://docs.seen.io/journey) para controlar como os dados recebidos são processados e como os vídeos são gerados.

Uma Journey é um fluxo de trabalho configurável que:
- Recebe dados de sistemas externos (como a Braze)
- Aplica lógica e regras de personalização
- Gera um vídeo e ativos associados
- Retorna uma carga útil de resposta configurável

As Journeys são compostas por **nós**, cada um com uma função específica:

- **Nó de gatilho**: define como e quando uma Journey começa (para integrações com a Braze, use um gatilho `On Create`)
- **Nó condicional**: roteia usuários através de diferentes caminhos lógicos com base nos valores dos dados
- **Nó de projeto**: aplica personalização dinâmica de vídeo usando os dados recebidos
- **Nó de player**: gera uma URL de player de vídeo única
- **Nó de webhook**: define a carga útil de resposta enviada de volta para a Braze

Como as respostas da Journey são configuráveis, certifique-se de que os campos de saída retornados pela Seen correspondam aos atributos esperados pela sua Transformação de dados da Braze.


## Limite de taxa {#rate-limit}
A API da Seen aceita até 100 chamadas a cada 10 segundos.


## Integração {#integration}

Neste exemplo, a Braze envia dados de usuários para a Seen para gerar um vídeo personalizado. A Seen então retorna uma URL única do player de vídeo e uma URL de miniatura, que são armazenadas como atributos personalizados na Braze para uso no envio de mensagens.

Se você tiver várias campanhas de vídeo com a Seen, repita o processo para conectar a Braze com todas as campanhas de vídeo.

### Etapa 1: Crie uma Campaign de webhook para enviar dados para a Seen {#step-1-create-a-webhook-campaign-to-send-data-to-seen}

Crie uma nova [Campaign de webhook]({{site.baseurl}}/user_guide/channels/webhooks/) na Braze.

Configure o webhook da seguinte forma:

- **Webhook URL**:
  `https://next.seen.io/v1/workspaces/{WORKSPACE_ID}/data`
  Encontre seu ID de espaço de trabalho nas configurações da plataforma Seen.

- **HTTP Method**: POST
- **Request body**: Raw Text
  Use o seguinte exemplo como ponto de partida. Consulte a [documentação de criação de dados da Seen](https://docs.seen.io/create-data) para mais informações.

{% raw %}
```json
{
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "id": "{{${braze_id}}}"
}
```
{% endraw %}
- **Request headers**:
  - `Authorization`: Bearer `{Seen_API_TOKEN}`
  - `Content-Type`: `application/json`

  > Gere um [token de API](https://docs.seen.io/authorization) na plataforma Seen nas configurações do espaço de trabalho. Você pode entrar em contato com seu gerente de sucesso do cliente da Seen para obter assistência.

- Para testar o webhook com um usuário, mude para a guia **Test**.
- Após confirmar que o teste funciona como esperado, conclua a configuração do webhook.


### Etapa 2: Configure uma Journey na plataforma Seen {#step-2-configure-a-journey-in-the-seen-platform}

A Seen usa [Journeys](https://docs.seen.io/journey) para definir como os dados recebidos são processados, personalizados e retornados para a Braze.
Cada Journey é um fluxo de trabalho configurável composto por nós que permitem controlar tanto a lógica de geração de vídeo quanto a carga útil da resposta.

Para configurar sua Journey:

1. Crie uma nova Journey na plataforma Seen
2. Adicione um **nó de gatilho** e selecione o gatilho `On Create`
   Isso garante que a Journey comece quando a Braze enviar dados para a Seen. Crie e adicione qualquer lógica de [segmentação](https://docs.seen.io/segments) dentro do seu espaço de trabalho, se necessário.
3. Construa sua lógica usando os seguintes nós conforme necessário:
   - **Nó condicional**: roteie usuários com base nos valores de atributo (por exemplo, tipo de plano ou região)
   - **Nó de projeto**: aplique personalização dinâmica de vídeo usando os dados recebidos
   - **Nó de player**: gere uma URL única do player de vídeo
4. Adicione um **nó de webhook** para definir a resposta enviada de volta para a Braze

#### Requisitos de resposta do nó de webhook {#webhook-node-response-requirements}

Como a carga útil da resposta é configurável, certifique-se de que os seguintes campos sejam retornados para suportar a Transformação de dados da Braze descrita na próxima etapa:

| Campo | Descrição |
|------|-------------|
| `id` | Deve corresponder ao `braze_id` enviado pela Braze |
| `player_url` | URL única para o player de vídeo personalizado |
| `email_thumbnail_url` | URL da miniatura do vídeo gerado |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webhook node response requirements" }

Se o seu caso de uso exigir atributos adicionais, inclua-os na resposta e mapeie-os na Braze.


### Etapa 3: Crie uma Transformação de dados para receber dados da Seen {#step-3-create-a-data-transformation-to-receive-data-from-seen}

Use as Transformações de dados da Braze para ingerir a resposta da Journey da Seen e armazenar ativos de vídeo no perfil do usuário.

1. Crie os seguintes [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) na Braze:
   - `player_url`
   - `email_thumbnail_url`
2. Navegue até **Data Settings** → **Data Transformation** e clique em **Create transformation**
3. Configure a transformação:
   - **Start from scratch**
   - **Destination** → POST: Track users
4. Compartilhe a URL do webhook gerada com a Seen, ou adicione-a diretamente ao **nó de webhook** da Journey
5. Use o seguinte código de transformação:

```javascript
let brazecall = {
  "attributes": [
    {
      "braze_id": payload.id,
      "_update_existing_only": true,
      "player_url": payload.player_url,
      "email_thumbnail_url": payload.email_thumbnail_url
    }
  ]
};
return brazecall;
```

{: start="6"}
6. Envie uma carga útil de teste para o endpoint fornecido. Envie dados para a plataforma Seen para executar sua Journey, ou envie a carga útil diretamente para a Braze com o [Postman](https://www.postman.com/) ou outro serviço similar.
7. Selecione **Validate** para garantir que tudo funcione como esperado.
8. Selecione **Save** e **Activate**.