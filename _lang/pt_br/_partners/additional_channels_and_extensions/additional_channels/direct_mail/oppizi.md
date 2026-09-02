---
nav_title: Oppizi
article_title: Oppizi
alias: /partners/oppizi/
description: "Este artigo de referência descreve a parceria entre a Braze e a Oppizi."
page_type: partner
search_tag: Partner
---

# Oppizi

> [Oppizi](https://www.oppizi.com/) é a líder global em marketing offline, fornecendo uma solução completa para empresas realizarem campanhas de mala direta e panfletagem mensuráveis e direcionadas.

_Esta integração é mantida pela Oppizi._

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ------------------------------ | ----------------------------------------------------------------------------- |
| Conta Oppizi | Uma conta Oppizi ativa é necessária para usar esta integração. |
| Chave de API or interface de programação do aplicativo (API) Oppizi | Encontrada na sua conta Oppizi em **Integrations** > **Braze**. |
| ID do fluxo de trabalho de mala direta Oppizi | Crie um fluxo de trabalho na Oppizi na página **Direct Mail Workflow** para obter um ID. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

Com a integração Oppizi, você pode:

* **Enviar postais de mala direta automatizados** usando gatilhos da Braze conectados ao webhook da Oppizi e fluxos de trabalho de mala direta.
* **Configurar limites, ondas e restrições** nos fluxos de trabalho de mala direta da Oppizi para controlar o envio das suas campanhas.
* **Criar postais profissionais** com a ferramenta de design integrada da Oppizi — sem experiência em design necessária.
* **Acompanhar o desempenho da campanha** em tempo real com o dashboard da Oppizi.

## Integração {#integration}

### Etapa 1: Gere sua chave de API or interface de programação do aplicativo (API) Oppizi {#step-1-generate-your-oppizi-api-key}

Para usar seu modelo de webhook na Braze, você primeiro precisará gerar sua chave de API or interface de programação do aplicativo (API) Oppizi.

1. Faça login na Oppizi.
2. Acesse **Integrations** > **Braze**.
3. Gere sua chave de API or interface de programação do aplicativo (API).

Você pode gerenciar, revogar e criar suas chaves a partir desta página conforme necessário.

### Etapa 2: Crie um modelo de webhook na Braze {#step-2-create-a-braze-webhook-template}

Em seguida, crie um modelo de webhook para Oppizi na Braze para usar em futuras campanhas ou Canvas:

1. Na Braze, acesse **Content** > **Webhook**.
2. Selecione **Create webhook template**.
3. Dê um nome ao modelo.
4. No seu modelo de webhook, preencha os seguintes campos:

- **Webhook URL:** `https://webhooks.oppizi.com/events`
- **Request Body:** **Raw Text**

Para o método de solicitação e cabeçalhos, a Oppizi requer um método HTTP juntamente com os seguintes cabeçalhos HTTP a serem incluídos no modelo. Preencha os seguintes campos:

- **HTTP Method:** POST
- **Request Headers:**
  - **Authorization:** `Bearer <oppiziAPIKey>`
  - **Content-Type:** `application/json`

![Um exemplo do cabeçalho do webhook Oppizi na Braze.]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_headers.png %})

Para o **Request Body**, você deve incluir o campo **oppiziWorkflowID**. Esse ID é gerado quando um fluxo de trabalho é criado na Oppizi e é necessário para especificar a qual fluxo de trabalho de mala direta seus destinatários devem ser adicionados. Cada fluxo de trabalho de mala direta na Oppizi tem um ID exclusivo, então, se você criar um modelo de webhook Oppizi na Braze, certifique-se de sempre atualizar o ID do fluxo de trabalho para o correto.

{% alert note %}
Verifique se os atributos personalizados necessários estão configurados na sua conta Braze para os endereços postais dos seus destinatários, pois eles são necessários para o envio de mala direta.
{% endalert %}

![Um exemplo de um modelo de webhook Oppizi na Braze.]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_example.png %})

A seguir, um exemplo de corpo de solicitação:

{% raw %}
```json
{
    "event" : "workflow.addRecipient",
    "oppiziWorkflowID" : "<oppiziWorkflowID>",
    "requestType" : "live",
    "recipient" : {
        "recipientID" : "{{${braze_id}}}",
        "firstName" : "{{${first_name}}}",
        "lastName" : "{{${last_name}}}",
        "address1" : "{{custom_attribute.${address1}}}",
        "address2" : "{{custom_attribute.${address2}}}",
        "city" : "{{custom_attribute.${city}}}",
        "country" : "{{${country}}}",
        "zipCode" : "{{custom_attribute.${zipCode}}}",
        "state" : "{{custom_attribute.${state}}}"
    }
}
```
{% endraw %}

### Etapa 3: Crie um fluxo de trabalho de mala direta na Oppizi {#step-3-create-a-direct-mail-workflow-in-oppizi}

1. Na Oppizi, acesse **Direct Mail Workflow** > **Create workflow**.
2. Configure os detalhes do fluxo de trabalho, incluindo limites, ondas, formato do cartão postal e arte.
3. Na seção de detalhes do webhook, você encontrará um corpo de solicitação pronto para uso, incluindo seu ID de fluxo de trabalho, que pode colar diretamente na Braze.

### Etapa 4: Pré-visualize e teste sua solicitação na Braze {#step-4-preview-and-test-your-request-in-braze}

Após adicionar seu corpo de solicitação com o ID de fluxo de trabalho da Oppizi, execute um teste para confirmar que sua configuração está funcionando como esperado.

Para executar o teste, atualize `requestType` de `live` para `test` no corpo da solicitação. Esse passo é crucial para evitar adicionar destinatários de teste ao seu público de mala direta.

Depois de terminar os testes, atualize `requestType` de volta para `live` e salve seu Canvas. Agora, você está pronto para lançar suas campanhas automatizadas de mala direta.