---
nav_title: Stayfilm
article_title: Stayfilm
description: "Saiba como integrar a renderização de vídeos personalizados da Stayfilm com a Braze usando webhook campaigns, Connected Content e Data Transformation."
alias: /partners/stayfilm/
page_type: partner
search_tag: Partner
---

# Stayfilm

> A [Stayfilm](https://www.stayfilm.com/) é uma REST API para produção automatizada e personalizada de vídeos em escala. A plataforma integra dados, imagens, texto, trilhas sonoras, narração e efeitos visuais para gerar conteúdo de vídeo personalizado para eCommerce, marketplaces, fluxos de CRM e campanhas de marketing.
>
> Essa integração envia trabalhos de renderização da Braze para a API da Stayfilm, recebe retornos de chamada quando os vídeos estão prontos e armazena URLs de vídeo e status nos perfis de usuário para uso em Campaigns e Canvas.

_Essa integração é mantida pela Stayfilm._

## Casos de uso {#use-cases}

A Stayfilm oferece suporte à entrega de vídeos personalizados em todo o ciclo de vida do cliente, incluindo:

- **Jornadas de integração e boas-vindas:** receba novos usuários com vídeos personalizados de acordo com o perfil ou contexto de cadastro
- **Conteúdo de produtos e marketplace:** gere vídeos focados em produtos a partir de catálogos ou mídias fornecidas pelo usuário
- **Conversão e ativação:** reforce ações importantes com mensagens de vídeo contextuais
- **Fidelidade e upsell:** destaque ofertas personalizadas ou marcos de uso em formato de vídeo
- **Recuperação e prevenção de churn:** reengaje usuários inativos com conteúdo de vídeo personalizado

## Pré-requisitos {#prerequisites}

Antes de começar, confirme que você tem o seguinte:

| Requisito | Descrição |
| ----------- | ----------- |
| Acesso à API da Stayfilm | Entre em contato com a Stayfilm para obter as credenciais do seu projeto, incluindo `idproject`, `Subscription-Key`, credenciais de cliente OAuth e a URL base da API da Stayfilm. Para detalhes de autenticação e endpoints, consulte a [documentação da API da Stayfilm](https://apidoc.stayfilm.com). |
| Braze Data Transformation | Use o [Braze Data Transformation]({{site.baseurl}}/user_guide/data/unification/data_transformation) para receber retornos de chamada da Stayfilm e mapeá-los para perfis de usuário da Braze por meio do [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). |
| Identificador de usuário da Braze | Este passo a passo usa `external_id` para correlacionar trabalhos da Stayfilm com perfis de usuário da Braze. O valor que você passa em `CallbackRelayData` deve corresponder ao `external_id` do usuário na Braze. |
| Sandbox da Braze (recomendado) | Teste a integração em um espaço de trabalho sandbox da Braze antes de implantar em produção. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Como a integração funciona {#how-the-integration-works}

Essa integração usa um fluxo de webhook bidirecional:

1. **Saída:** Uma [webhook campaign]({{site.baseurl}}/user_guide/channels/webhooks) da Braze envia um trabalho de renderização para o endpoint `POST /Job` da Stayfilm. A solicitação inclui mídia do usuário, configuração do modelo e `CallbackRelayData` definido como o `external_id` do usuário da Braze.
2. **Entrada:** Quando a Stayfilm termina a renderização, ela envia um retorno de chamada para a URL do webhook do seu Braze Data Transformation. A transformação mapeia a resposta para [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) e eventos personalizados no perfil de usuário correspondente.
3. **Entrega:** Use o atributo `stayfilm_video_url` armazenado em canais de envio de mensagens, como uma [mensagem no app]({{site.baseurl}}/user_guide/channels/in_app_messages) com HTML personalizado.

O Data Transformation neste passo a passo grava os seguintes atributos personalizados:

| Atributo | Descrição |
| --------- | ----------- |
| `stayfilm_video_status` | `ready` quando a renderização é bem-sucedida, ou `failed` quando a Stayfilm reporta um erro |
| `stayfilm_video_url` | URL do vídeo MP4 renderizado |
| `stayfilm_job_id` | Identificador do trabalho da Stayfilm |
| `stayfilm_render_error` | Mensagem de erro quando a renderização falha |
| `stayfilm_callback_received_at` | Timestamp ISO do retorno de chamada |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atributos personalizados" }

A transformação também registra eventos personalizados chamados `stayfilm_video_ready` ou `stayfilm_video_failed`.

## Integração {#integration}

As etapas a seguir orientam uma prova de conceito. Após validar o fluxo, adapte o payload do trabalho, os atributos e o envio de mensagens ao seu caso de uso.

### Etapa 1: Criar um usuário teste {#step-1-create-a-test-user}

Crie um perfil de usuário teste para usar enquanto você constrói e valida a integração. Para saber mais, consulte [Importar usuários]({{site.baseurl}}/user_guide/audience/manage_audience/import_users).

1. Acesse **Audience** > **Import Users**.
2. Selecione **Quick User Add**.
3. Insira um `external_id` e quaisquer outros campos obrigatórios, depois selecione **Create new user**.

{% alert important %}
Não use dados pessoais — como e-mail, número de telefone, nome completo, documento de identidade, endereço ou detalhes de pedidos — como `external_id`. Trate o `external_id` como sensível a maiúsculas e minúsculas em toda essa integração.
{% endalert %}

Este passo a passo usa `stayfilm-poc-001` como exemplo de `external_id`. Anote o valor que você escolher, pois ele será usado nas etapas seguintes.

### Etapa 2: Criar um Data Transformation {#step-2-create-a-data-transformation}

Crie um Data Transformation para receber retornos de chamada da Stayfilm e atualizar perfis de usuário.

1. Acesse **Data Settings** > **Data Transformation**.
2. Selecione **Create transformation**.
3. Insira um nome, como `Stayfilm Callback Data Transformation`.
4. Em **Editing experience**, selecione **Start from scratch**.
5. Em **Select destination** > **Destination**, selecione **POST: Track users**.
6. Selecione **Create transformation**.
7. Substitua o código de transformação padrão pelo seguinte:

```javascript
const brazeExternalId = payload.RelayedData;
if (!brazeExternalId) {
  throw new Error("Missing RelayedData. Expected Stayfilm callback to relay the Braze external_id from CallbackRelayData.");
}

const idJob = payload.IdJob || null;
const producedFiles = payload.ProducedFiles || {};
const videoUrl = producedFiles?.Videos?.VideoMP4?.Url || null;
const errorMessage = payload.ErrorMessage || null;
const hasError = payload.HasError === true || Boolean(errorMessage);
const isReady = !hasError && Boolean(videoUrl);
const now = new Date().toISOString();

let brazecall = {
  attributes: [
    {
      external_id: brazeExternalId,
      _update_existing_only: true,
      stayfilm_video_status: isReady ? "ready" : "failed",
      stayfilm_video_url: videoUrl || null,
      stayfilm_job_id: idJob,
      stayfilm_render_error: errorMessage,
      stayfilm_callback_received_at: now
    }
  ],
  events: [
    {
      external_id: brazeExternalId,
      _update_existing_only: true,
      name: isReady ? "stayfilm_video_ready" : "stayfilm_video_failed",
      time: now,
      properties: {
        stayfilm_job_id: idJob,
        stayfilm_video_url: videoUrl || null,
        stayfilm_render_error: errorMessage,
        stayfilm_status: payload.Status || payload.status || null
      }
    }
  ]
};

return brazecall;
```

{: start="8"}
8. Selecione **Save** e copie a URL do webhook gerada.
9. Envie uma solicitação `POST` de teste para a URL do webhook com o seguinte JSON de retorno de chamada de exemplo da Stayfilm. Defina `RelayedData` como o `external_id` do usuário teste que você criou na etapa 1.

```json
{
  "IdJob": "debug-job-001",
  "HasError": false,
  "Status": "DRAFT_DONE",
  "ProducedFiles": {
    "Videos": {
      "VideoMP4": {
        "Url": "https://example.com/stayfilm-poc-video.mp4"
      }
    }
  },
  "RelayedData": "stayfilm-poc-001"
}
```

Envie a solicitação com cURL, Postman ou uma ferramenta similar. Uma resposta bem-sucedida retorna o status HTTP `201` com `{"message": "success"}`.

{: start="10"}
10. Acesse **Data Settings** > **Data Transformation** e recarregue a página se a sua transformação não aparecer na lista.
11. Abra a transformação e selecione **Validate**. Confirme que a validação foi bem-sucedida em **Output**.
12. Selecione **Activate**.
13. Forneça a URL do webhook copiada para a Stayfilm como sua URL de retorno de chamada.

{% alert note %}
Se você armazenar mais do que o `external_id` da Braze em `CallbackRelayData`, atualize o código de transformação para analisar `RelayedData` adequadamente.
{% endalert %}

### Etapa 3: Criar uma webhook campaign para enviar trabalhos à Stayfilm {#step-3-create-a-webhook-campaign-to-send-jobs-to-stayfilm}

Crie uma [webhook campaign]({{site.baseurl}}/user_guide/channels/webhooks) que envia trabalhos de renderização para a Stayfilm.

{% alert important %}
Antes de testar a campaign, confirme que a Stayfilm configurou seu projeto com a URL de retorno de chamada do Data Transformation da etapa 2.
{% endalert %}

1. Acesse **Messaging** > **Campaigns**.
2. Selecione **Create campaign** > **Webhook**.
3. Insira um nome para a campaign, como `Stayfilm Webhook Integration`.
4. Selecione **Compose webhook** > **Start from scratch**.
5. Em **Compose Webhook** > **Webhook URL**, insira a URL do endpoint `POST /Job` da Stayfilm fornecida pela Stayfilm. Substitua *`{BASE_URL}`* no exemplo a seguir: `https://{BASE_URL}/stg/v3/job`
6. Defina **HTTP method** como **POST**.
7. Em **Request Body**, selecione **Raw Text** e cole o payload do trabalho fornecido pela Stayfilm. Você pode usar [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) para tornar o corpo dinâmico.

Inclua `CallbackRelayData` definido como o `external_id` do usuário da Braze. A Stayfilm retorna esse valor no retorno de chamada como `RelayedData`.

{% raw %}
```json
{
  "SmartTags": ["Setup-Template"],
  "Medias": [
    {
      "Group": "userMedia",
      "URL": "https://{BASE_URL}/some_media.png"
    }
  ],
  "Videos": [{}],
  "CallbackRelayData": "stayfilm-poc-001"
}
```
{% endraw %}

Adicione os seguintes cabeçalhos de solicitação:

| Chave | Valor |
| --- | ----- |
| `idproject` | O valor de `idproject` fornecido pela Stayfilm |
| `Subscription-Key` | A `Subscription-Key` fornecida pela Stayfilm |
| `Content-Type` | `application/json` |
| `Authorization` | Token bearer OAuth obtido via Connected Content (veja o exemplo a seguir) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cabeçalhos de solicitação" }

No bloco de Connected Content a seguir, substitua *`{TENANT_ID}`*, *`{CLIENT_ID}`*, *`{CLIENT_SECRET_URL_ENCODED}`* e *`{SCOPE_URL_ENCODED}`* pelos valores fornecidos pela Stayfilm. Codifique em URL *`{CLIENT_SECRET_URL_ENCODED}`* e *`{SCOPE_URL_ENCODED}`* antes de colá-los no bloco. Para requisitos de OAuth, consulte a [documentação da API da Stayfilm](https://apidoc.stayfilm.com).

{% raw %}
```
{% connected_content https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token
  :method post
  :body grant_type=client_credentials&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET_URL_ENCODED}&scope={SCOPE_URL_ENCODED}
  :content_type application/x-www-form-urlencoded
  :cache_max_age 3000
  :save stayfilm_auth
%}Bearer {{stayfilm_auth.access_token}}
```
{% endraw %}

{: start="8"}
8. Selecione **Save Draft**.

{% alert note %}
Se você sair da página de Campaigns e retornar, defina **Status** como **All** para encontrar Campaigns que ainda estão em **Draft**.
{% endalert %}

### Etapa 4: Testar a webhook campaign {#step-4-test-the-webhook-campaign}

1. No criador de webhook, selecione a guia **Test**.
2. Em **Preview message as user**, selecione **Select existing user** e busque seu usuário teste (por exemplo, `stayfilm-poc-001`).
3. Selecione **Send test**.

Uma resposta bem-sucedida retorna o status HTTP `201` com um corpo JSON semelhante ao seguinte:

```json
{
  "IdJob": "4557a77e-f56c-48be-81f7-2d8c5e558cb1",
  "Videos": [
    {
      "IdVideo": "87287b25-7814-4fa1-ad1a-f2ea89822d0f",
      "IdGenre": "f07a1334-5904-420a-9f31-92644f245c5a",
      "IdVideoTemplate": "7b77c3df-12a1-4636-a9b4-bc227f4c233f",
      "IdProject": "73ea3e73-b41e-4676-b674-51731d3bf49c",
      "Status": "DRAFT_RENDERING_PENDING",
      "DurationInSeconds": null,
      "URL": null,
      "ErrorMessage": null,
      "CreatedAt": "2026-06-16T00:35:28.7736263Z",
      "UpdatedAt": "2026-06-16T00:35:28.7736264Z",
      "IdVideoFather": null,
      "IdVideoSon": null,
      "ProducingStatus": "PENDING"
    }
  ],
  "Images": []
}
```

### Etapa 5: Confirmar o retorno de chamada da Stayfilm {#step-5-confirm-the-stayfilm-callback}

A Stayfilm renderiza o vídeo de forma assíncrona e envia um retorno de chamada para o seu Data Transformation quando o processamento é concluído. Monitore o status do trabalho por meio dos endpoints da API da Stayfilm descritos na [documentação da API da Stayfilm](https://apidoc.stayfilm.com).

1. Acesse **Data Settings** > **Data Transformation**.
2. Selecione a guia **Logs** da sua transformação.
3. Confirme que um retorno de chamada aparece com o status **Success**.

### Etapa 6: Exibir o vídeo em uma mensagem no app {#step-6-display-the-video-in-an-in-app-message}

Depois que `stayfilm_video_url` estiver preenchido no perfil do usuário, exiba o vídeo renderizado em uma Campaign ou Canvas.

1. Acesse **Messaging** > **Campaigns**.
2. Selecione **Create campaign** > **In-app message**.
3. Insira um nome para a campaign, como `Stayfilm Video Show`.
4. No criador de mensagem, selecione o **Traditional Editor**.
5. Em **Send To**, selecione **Web Browsers**.
6. Defina **Message Type** como **Custom Code**.
7. Cole o seguinte HTML no campo **HTML**:

{% raw %}
```html
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body>
<div id="stayfilm-video-url" style="display: none;">{{custom_attribute.${stayfilm_video_url}}}</div>
<video id="stayfilm-video" controls preload="metadata" playsinline style="width: 100%; max-width: 420px; border-radius: 12px; background: #000;">
Your browser does not support HTML5 video.
</video>
<script>
(function () {
  var urlElement = document.getElementById("stayfilm-video-url");
  var video = document.getElementById("stayfilm-video");
  var videoUrl = urlElement ? urlElement.textContent.trim() : "";
  if (!videoUrl || videoUrl.indexOf("http") !== 0) {
    return;
  }
  var source = document.createElement("source");
  source.src = videoUrl;
  source.type = "video/mp4";
  video.appendChild(source);
  video.load();
})();
</script>
</body>
</html>
```
{% endraw %}

{: start="8"}
8. Selecione **Save Draft**.
9. Selecione a guia **Test**.
10. Em **Preview message as user**, selecione **Select existing user** e busque o `external_id` do seu usuário teste.

O vídeo renderizado aparece e é reproduzido na prévia quando `stayfilm_video_url` está definido no perfil.

## Estender a integração {#extend-the-integration}

Este passo a passo cobre um subconjunto da API da Stayfilm. Para adaptar modelos de trabalho, entradas de mídia ou envio de mensagens downstream, consulte a [documentação da API da Stayfilm](https://apidoc.stayfilm.com) e atualize o payload do webhook, o mapeamento do Data Transformation e a lógica da campaign conforme necessário.

## Considerações {#considerations}

- **Renderização assíncrona:** a geração de vídeo não é imediata. Dispare mensagens de acompanhamento a partir do evento personalizado `stayfilm_video_ready` ou de um segmento baseado em `stayfilm_video_status`, em vez de enviar a mensagem no app no mesmo fluxo do webhook.
- **Consistência do identificador:** o valor em `CallbackRelayData` deve corresponder exatamente ao `external_id` do usuário da Braze.
- **Cache do token OAuth:** o exemplo de Connected Content armazena em cache o token OAuth por 3000 segundos. Ajuste `cache_max_age` se a Stayfilm alterar os requisitos de tempo de vida do token.
- **Teste em sandbox:** valide o loop completo de retorno de chamada em um sandbox da Braze antes do lançamento em produção.
- **Capacidade de atributos personalizados:** confirme que seu espaço de trabalho tem capacidade para os atributos personalizados e eventos que essa integração cria.

## Solução de problemas {#troubleshooting}

Consulte a tabela a seguir se você tiver problemas com a integração da Stayfilm.

| Problema | Resolução |
| ----- | ---------- |
| A validação do Data Transformation falha | Confirme que `RelayedData` no seu payload de teste corresponde a um `external_id` válido da Braze, depois recarregue a página **Data Transformation** antes de selecionar **Validate**. |
| O teste do webhook retorna uma resposta diferente de 201 | Verifique as credenciais da Stayfilm nos cabeçalhos da solicitação, confirme que o bloco de Connected Content OAuth usa valores codificados em URL e verifique se a URL do `POST /Job` está correta. |
| O retorno de chamada não aparece nos logs da transformação | Confirme que a Stayfilm tem a URL ativa do webhook do seu Data Transformation e aguarde o tempo necessário para a renderização do vídeo ser concluída. |
| A prévia no app não exibe o vídeo | Confirme que `stayfilm_video_url` está definido no perfil do usuário teste e que a mensagem no app tem como alvo **Web Browsers** com **Custom Code**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solução de problemas" }