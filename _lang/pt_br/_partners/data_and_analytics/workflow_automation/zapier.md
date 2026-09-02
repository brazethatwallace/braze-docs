---
nav_title: Zapier
article_title: Zapier
alias: /partners/zapier/
description: "Este artigo de referência descreve a parceria entre a Braze e o Zapier, uma ferramenta da web de automação que permite compartilhar dados entre apps da web e usar essas informações para automatizar ações."
page_type: partner
search_tag: Partner

---
# Integração com o Zapier {#zapier-integration}

> [O Zapier](https://zapier.com/) é uma ferramenta da web de automação que permite compartilhar dados entre apps da web e, em seguida, usar essas informações para automatizar ações.

A parceria entre a Braze e o Zapier alavanca a API e os [webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook#creating-a-webhook) da Braze para se conectar a aplicativos de terceiros, como Google Workplace, Slack, Salesforce, WordPress etc., para automatizar várias ações.

## Pré-requisitos {#prerequisites}

| Requisitos | Descrição |
|---|---|
| Conta Zapier | É necessário ter uma conta do Zapier para usar essa parceria. |
| Endpoint REST da Braze | Sua URL de endpoint REST. Seu endpoint dependerá da [URL da Braze para sua instância]({{site.baseurl}}/api/basics#api-definitions). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

No exemplo do Zapier a seguir, enviaremos informações do WordPress para a Braze usando um webhook POST. Essas informações poderão ser usadas para criar um Canvas na Braze.

### Etapa 1: Criar um gatilho do Zapier {#step-1-create-a-zapier-trigger}

Usando a terminologia do Zapier, um "zap" é um fluxo de trabalho automatizado que conecta seus apps e serviços. A primeira parte de qualquer zap é designar um gatilho. Depois que seu zap for ativado, o Zapier executará automaticamente as respectivas ações sempre que seu gatilho for detectado.

Usando nosso exemplo do WordPress, na plataforma Zapier, configuraremos nosso zap para disparar quando uma nova postagem do WordPress for adicionada e selecionaremos **Published** e **Posts** como **Post Status** e **Post Type**.

![Na plataforma Zapier, em um zap, selecione o gatilho para ser um "novo comentário", "qualquer webhook" ou "nova postagem". Para este exemplo, "nova postagem" está selecionado.][5]

![Na plataforma Zapier, em um zap, configure o gatilho selecionando o status e o tipo de postagem desejados. Para este exemplo, "Published" e "Posts" estão selecionados.][6]

### Etapa 2: Adicionar um webhook de ação {#step-2-add-an-action-webhook}

Em seguida, defina a ação do zap. Quando seu zap estiver ativado e seu gatilho for detectado, a ação ocorrerá automaticamente.

Continuando com nosso exemplo, queremos enviar uma solicitação POST como JSON para um endpoint da Braze. Isso pode ser feito selecionando a opção **Webhooks** em **Apps**.

![Etapa de Apps do Zapier com Webhooks selecionado para a ação.]({% image_buster /assets/img_archive/zapier3.png %})

### Etapa 3: Configurar o POST da Braze {#step-3-set-up-braze-post}

Ao configurar seu webhook, use as seguintes configurações e forneça seu endpoint REST da Braze na URL do webhook. Quando terminar, selecione **Publish**.

- **Method**: POST
- **Webhook URL**: `https://rest.iad-01.braze.com/canvas/trigger/send`
- **Data Pass-Through**: False
- **Unflatten**: No
- **Request Header**:
  - **Content-Type**: application/json
  - **Authorization**: Bearer YOUR-API-KEY
- **Data**:

```json
{
  "canvas_id": "your_canvas_identifier",
  "recipients": [
    {
      "external_user_id": "external_user_identifier",
      "context":{
        "string_property": "Your example string",
        "example_integer_property": 1
      }
    }
  ]
}
```

![Configuração do webhook do Zapier com endpoint da Braze, cabeçalhos e campos de carga útil.]({% image_buster /assets/img/zapier.png %}){: style="max-width:70%;"}

### Etapa 4: Criar uma Campaign na Braze {#step-4-create-a-braze-campaign}

Depois de configurar seu zap com êxito, você poderá personalizar suas Campaigns ou Canvas na Braze com dados do WordPress usando a formatação Liquid para exibir as informações em suas mensagens.

## Usando o Zapier com o endpoint `/users/track` {#using-zapier-with-the-userstrack-endpoint}

Para enviar dados ao endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) da Braze (por exemplo, ao usar um gatilho como **New or Updated Spreadsheet Row** no Google Sheets), use **Webhooks by Zapier** com uma **Custom Request** — não use a ação padrão **POST**. A ação POST padrão formata a solicitação de uma maneira que não é compatível com o endpoint `/users/track`.

1. No Zapier, escolha seu gatilho (por exemplo, **New or Updated Spreadsheet Row** no Google Sheets).
2. Para a ação, selecione **Webhooks by Zapier** e escolha **Custom Request** (não POST).
3. Defina **Method** como POST, insira a URL do endpoint REST da Braze (por exemplo, `https://rest.iad-01.braze.com/users/track`) e formate o corpo da solicitação com aspas duplas ao redor de cada elemento, como faria em uma chamada no Postman ou na API. Mapeie os campos do seu gatilho (por exemplo, colunas da planilha) no corpo JSON conforme apropriado.
4. Adicione os cabeçalhos obrigatórios:
   - **Content-Type**: `application/json`
   - **Authorization**: `Bearer YOUR-REST-API-KEY` (use sua chave da API REST da Braze sem colchetes ou aspas)
5. Teste a etapa e ative seu zap.

[5]: {% image_buster /assets/img_archive/zapier1.png %}
[6]: {% image_buster /assets/img_archive/zapier2.png %}