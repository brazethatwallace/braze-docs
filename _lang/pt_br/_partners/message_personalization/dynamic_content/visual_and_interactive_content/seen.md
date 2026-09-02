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
> Essa integração envia dados de usuários da Braze para a Seen, gera vídeos personalizados e retorna ativos — como uma URL de player única e miniatura — para a Braze para uso em Campaigns e Canvas.


## Casos de uso {#use-cases}

A Seen suporta entrega automatizada de vídeo personalizado ao longo do ciclo de vida do cliente, incluindo:

- **Integração**: dê as boas-vindas a novos usuários com vídeos personalizados para seu perfil ou contexto de inscrição
- **Conversão e ativação**: reforce ações-chave com mensagens de vídeo contextuais
- **Fidelidade e upsell**: destaque ofertas personalizadas ou marcos de uso
- **Recuperação e prevenção de churn**: reengaje usuários inativos com conteúdo de vídeo personalizado


## Pré-requisitos {#prerequisites}

Antes de começar, certifique-se de que você tem o acesso e os dados descritos na tabela a seguir.

| Pré-requisito | Descrição |
|--------------|-------------|
| Acesso à plataforma Seen | Você precisa de uma assinatura da plataforma Seen com um projeto publicado, ou de uma Campaign ativa da Seen. Você também precisa de acesso ao seu projeto para recuperar o endpoint do projeto e gerar um token de API or interface de programação do aplicativo (API). |
| URL do webhook de Transformação de dados da Braze | Use a Transformação de dados da Braze para reformatar os dados recebidos da Seen para que possam ser aceitos pelo [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) da Braze. |
| Dados de usuários da Braze | A personalização de vídeo requer dados em nível de usuário. Certifique-se de que os atributos relevantes estejam disponíveis na Braze e passe **`braze_id`** como o identificador único. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }




## Como funcionam os projetos da Seen {#how-seen-projects-work}

A Seen usa a guia [Run](https://docs.seen.io/run) em um projeto para controlar como os dados recebidos são processados e como os vídeos são gerados.

Um fluxo de trabalho de projeto:

- Recebe dados de sistemas externos (como a Braze)
- Aplica lógica e regras de personalização
- Gera um vídeo e ativos associados
- Retorna uma carga útil de resposta configurável

A guia Run inclui o seguinte:

- **Create via API or interface de programação do aplicativo (API)**: abre os detalhes da API or interface de programação do aplicativo (API) do projeto.
- **Import CSV**: importa dados de personalização manualmente (não utilizado neste passo a passo).
- **Add webhook**: define a carga útil de resposta enviada de volta para a Braze.
- **View videos**: exibe os vídeos gerados e o status dos dados recebidos.

As respostas de webhook são configuráveis, então alinhe os campos de saída que a Seen retorna com os atributos que sua Transformação de dados da Braze espera.


## Limite de taxa {#rate-limit}

A API or interface de programação do aplicativo (API) da Seen aceita 100 chamadas a cada 10 segundos.


## Integração {#integration}

Neste exemplo, a Braze envia dados de usuários para a Seen para gerar um vídeo personalizado. A Seen então retorna uma URL única do player de vídeo e uma URL de miniatura, que são armazenadas como [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) na Braze para uso no [envio de mensagens]({{site.baseurl}}/user_guide/messaging/).

Se você tiver várias campanhas de vídeo com a Seen, repita esse processo para cada campanha.

### Etapa 1: Crie uma Campaign de webhook para enviar dados para a Seen {#step-1-create-a-webhook-campaign-to-send-data-to-seen}

Crie uma nova [Campaign de webhook]({{site.baseurl}}/user_guide/channels/webhooks/) na Braze.

Configure o webhook da seguinte forma:

- **URL do webhook**:
  `https://next.seen.io/v1/projects/{PROJECT_ID}/data`
  Encontre o endpoint do seu projeto na guia Run do seu projeto na plataforma Seen.

- **Método HTTP**: POST

- **Corpo da requisição**: Raw Text
  Use o exemplo a seguir como ponto de partida. Para opções de campos e limites, consulte a [documentação de criação de dados da Seen](https://docs.seen.io/create-data).

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

- **Cabeçalhos da requisição**:
  - `Authorization`: Bearer `{Seen_API_TOKEN}`
  - `Content-Type`: `application/json`

  Gere um [token de API or interface de programação do aplicativo (API)](https://docs.seen.io/authorization) na guia Run do seu projeto na plataforma Seen. Entre em contato com seu gerente de sucesso do cliente da Seen se precisar de ajuda.

- Teste o webhook com um usuário na guia **Test**.
- Após um teste bem-sucedido, conclua a configuração do webhook.


### Etapa 2: Configure um projeto na plataforma Seen {#step-2-configure-a-project-in-the-seen-platform}

No seu projeto da Seen, use a guia [Run](https://docs.seen.io/run) para publicar seu vídeo e registrar o webhook de saída. Para uma visão geral conceitual da guia Run, consulte [Como funcionam os projetos da Seen](#how-seen-projects-work).

1. Na plataforma Seen, crie um projeto, construa seu vídeo e selecione **Publish**. Os vídeos começam a ser gerados a partir dos dados recebidos assim que o projeto é publicado.
2. Na guia Run, selecione **Add a webhook**.

#### Requisitos de resposta do webhook {#webhook-response-requirements}

A carga útil da resposta é configurável. Retorne os campos da tabela a seguir para que a Transformação de dados da Braze na próxima etapa possa mapeá-los.

| Campo | Descrição |
|-------|-------------|
| `id` | Deve corresponder ao `braze_id` enviado pela Braze |
| `player_url` | URL única para o player de vídeo personalizado |
| `email_thumbnail_url` | URL da miniatura do vídeo personalizado |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos de resposta do webhook" }

Se você precisar de atributos adicionais, inclua-os na resposta e mapeie-os na Braze.


### Etapa 3: Crie uma Transformação de dados para receber dados da Seen {#step-3-create-a-data-transformation-to-receive-data-from-seen}

Use as Transformações de dados da Braze para processar a resposta da Seen e armazenar ativos de vídeo no perfil do usuário.

1. Crie os seguintes [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) na Braze:
   - `player_url`
   - `email_thumbnail_url`

2. Acesse **Configurações de dados** > **Transformação de dados** e selecione **Create transformation**.

3. Configure a transformação:
   - **Start from scratch**
   - **Destination** > POST: Track users

4. Compartilhe a URL do webhook gerada com a Seen, ou adicione-a ao **Webhook** na guia Run do seu projeto.

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
6. Envie uma carga útil de teste para o endpoint fornecido. Você pode enviar dados para o seu projeto na plataforma Seen (publique o projeto primeiro), ou enviar uma carga útil diretamente para a Braze usando o [Postman](https://www.postman.com/) ou uma ferramenta similar.
7. Selecione **Validate** para verificar se a transformação funciona como esperado.
8. Selecione **Save** e **Activate**.