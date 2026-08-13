---
nav_title: Zendesk
article_title: Zendesk
description: "Este artigo de referência descreve a parceria entre a Braze e a Zendesk, um pacote de suporte popular que permite utilizar webhooks da Braze para sincronizar dados de suporte entre as duas plataformas."
alias: /partners/zendesk/
page_type: partner
search_tag: Partner

---

# Zendesk

> Com o [Zendesk Support Suite](https://www.zendesk.com/support-suite/) (ZSS), as empresas podem ter conversas naturais com seus clientes por meio de atendimento omnicanal, usando e-mail, chat na web, voz ou apps de mensagens em redes sociais. A Zendesk oferece um sistema de criação de tickets simplificado que valoriza o rastreamento e a priorização das interações, permitindo que as empresas tenham uma visão histórica unificada de seus clientes.

A integração de servidor para servidor entre a Braze e a Zendesk permite usar:
- Webhooks da Braze para automatizar a criação de tickets de suporte no Zendesk devido ao engajamento com mensagens nas jornadas dos usuários na Braze. Por exemplo, após implementar e testar com sucesso uma integração, a Braze pode criar um ticket de suporte a partir de um usuário que respondeu negativamente a uma mensagem no app "Gostando do nosso app?", permitindo que sua equipe de suporte acompanhe o cliente.
- Webhooks do Zendesk para suportar casos de uso bidirecionais, como atualizar o perfil do usuário na Braze devido a atividades no Zendesk. Por exemplo, após um ticket ser resolvido, registre um evento no perfil do usuário na Braze.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta do Zendesk | Uma [conta de administrador do Zendesk](https://`<your-zendesk-instance>`.zendesk.com/agent/admin) é necessária para aproveitar esta parceria. |
| Token de API do Zendesk | Um [token de API](https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-\) do Zendesk é necessário para enviar solicitações da Braze para o endpoint de tickets do Zendesk. |
| Identificador comum (recomendado) | É recomendável um [identificador comum](#common-identifier) entre a Braze e o Zendesk. |
| Chave de API da Braze | Uma chave de API da Braze é necessária para enviar solicitações do Zendesk para um endpoint da Braze. Certifique-se de que a chave de API que você usa tem as permissões corretas para o endpoint da Braze que seu webhook do Zendesk está usando. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração da Braze com o Zendesk {#braze-to-zendesk-integration}

### Etapa 1: Crie seu webhook da Braze {#step-1-create-your-braze-webhook}

Para criar um webhook:

- **Campaigns:** Acesse a página **Campaigns** no dashboard da Braze. Clique em **Create Campaign** e selecione **Webhook**.
- **Canvas:** Em um Canvas novo ou existente, crie uma etapa completa ou de mensagem no construtor de Canvas. Em seguida, clique em **Messages** e selecione **Webhook** nas opções de mensagem.

No seu webhook, preencha os seguintes campos:
- **URL do webhook**: `<your-zendesk-instance>.zendesk.com/api/v2/tickets.json`
- **Corpo da solicitação**: Texto bruto

Outros casos de uso podem ser tratados por meio das [APIs de suporte do Zendesk](https://developer.zendesk.com/rest_api/docs/support/introduction), que alterariam o endpoint `/api/v2/` adequadamente no final da URL do webhook.

#### Cabeçalho e método da solicitação {#request-header-and-method}

O Zendesk requer um cabeçalho HTTP para autorização e um método HTTP. Na guia **Settings**, substitua <email_address> pelo seu e-mail de administrador do Zendesk e <api_token> pelo seu token de API do Zendesk.

- **Método HTTP**: POST
- **Cabeçalhos da solicitação**:
  - **Authorization**: Basic {% raw %} `{{ '<email_address>/token:<api_token>' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

![Configurações de webhook da Braze com cabeçalho de autorização do Zendesk e método POST configurados.]({% image_buster /assets/img_archive/zendesk_step1.gif %}){: style="max-width:70%;"}

#### Corpo da solicitação {#request-body}

Defina os detalhes do ticket, como tipo, assunto e status, na carga útil do webhook. Os detalhes do ticket são extensíveis e personalizáveis com base na [API de tickets do Zendesk](https://developer.zendesk.com/rest_api/docs/support/tickets#create-ticket). Use o exemplo a seguir para ajudar a estruturar sua carga útil e inserir os campos desejados.

{% raw %}
```json
{% assign ticket_type = 'question/incident/task/problem' %} << Choose one >>
{% assign ticket_subject = '' %}
{% capture ticket_body %}
<< Your message here >>
{% endcapture %}
{% assign ticket_subject_tag = '' %}
{% assign ticket_status = 'New' %}

{
"ticket": {
"requester_id": "{{${user_id}}}",
"requester": { "name": "{{${first_name}}} {{${last_name}}}", "email": "{{${email_address}}}", "phone": "{{${phone_number}}}"},
"type": "{{ ticket_type }}",
"subject":  "{{ticket_subject}}",
"comment":  { "body": "{{ticket_body}}" },
"priority": "urgent",
"status": "{{ ticket_status }}"
  }
}
```
{% endraw %}

### Etapa 2: Pré-visualize sua solicitação {#step-2-preview-your-request}

Seu texto bruto será automaticamente destacado se for uma tag Braze aplicável.

Pré-visualize a solicitação no painel **Preview** ou navegue até a guia **Test**, onde é possível selecionar um usuário aleatório, um usuário existente ou personalizar o seu próprio usuário para testar o webhook.

Por fim, verifique se o ticket foi criado no lado do Zendesk.

## Identificador comum {#common-identifier}

Se você tem um identificador comum entre a Braze e o Zendesk, é recomendável utilizá-lo como o `requester_id`. Isso ajudará a unificar os dois conjuntos de usuários. Caso contrário, recomendamos passar um conjunto de atributos identificadores, como nome, endereço de e-mail, número de telefone ou outros.

## Integração do Zendesk com a Braze {#zendesk-to-braze-integration}

### Etapa 1: Crie um webhook {#step-1-create-a-webhook}

1. No [Centro de Administração](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), clique em **Apps and integrations** na barra lateral e selecione **Webhooks > Webhooks**.<br><br>
2. Clique em **Create webhook**.<br><br>
3. Selecione **Trigger** ou **Automation** e clique em **Next**.<br>![Tela de criação de webhook do Zendesk com opções de Trigger e Automation.]({% image_buster /assets/img_archive/zendesk2.png %}){: style="max-width:70%;"}<br><br>
4. Forneça as seguintes informações no seu webhook:
- Digite um nome e uma descrição para o webhook.
- Insira a URL do endpoint da Braze que seu webhook usará. {% raw %}Nosso exemplo usará `https://{{instance_url}}/users/track`.{% endraw %}
- Selecione POST como o método de solicitação do webhook e defina o formato da solicitação para JSON.
- Selecione o método de autenticação por bearer token para o webhook e forneça sua [chave de API da Braze]({{site.baseurl}}/api/basics#creating-rest-api-keys).
  - Certifique-se de que a chave de API que você está usando tem as [permissões corretas]({{site.baseurl}}/api/basics#rest-api-key-permissions) para o endpoint da Braze que seu webhook está usando.<br><br>
5. (Recomendado) Teste o webhook para verificar se está funcionando corretamente.<br><br>
6. Para webhooks de gatilho e automação, você deve conectar o webhook a um gatilho ou automação antes de finalizar a configuração. Consulte a etapa seguinte para ver nosso exemplo de criação de um gatilho para o webhook. Depois que o gatilho for criado, você pode voltar a esta página e selecionar **Finish setup**.

### Etapa 2: Crie um gatilho ou automação {#step-2-create-a-trigger-or-automation}

[Siga as instruções do Zendesk](https://support.zendesk.com/hc/en-us/articles/4408839108378#topic_bwm_1tv_dpb) sobre como conectar seu webhook a um gatilho ou automação.

O exemplo a seguir usa um gatilho para invocar o webhook quando o status de um caso de suporte for alterado para "Resolvido" ou "Fechado".

1. No **Centro de Administração**, clique em **Objects and rules** na barra lateral e selecione **Business rules > Triggers**.<br><br>
2. Selecione **Add trigger**.<br><br>
3. Nomeie seu gatilho e selecione uma categoria.<br><br>
4. Selecione **Add condition** para configurar quais condições devem acionar o webhook. Por exemplo, "Categoria de status alterada para fechada" ou "Categoria de status alterada para resolvida".![Construtor de condições de gatilho do Zendesk mostrando condições de categoria de status.]({% image_buster /assets/img_archive/zendesk1.png %}){: style="max-width:70%;"}<br><br>
5. Selecione **Add action**, escolha **Notify active webhook** e selecione no menu suspenso o webhook criado na etapa anterior.<br><br>
6. Defina o corpo JSON para estar em conformidade com seu endpoint da Braze, usando os placeholders de variáveis do Zendesk para preencher dinamicamente os campos relevantes.<br>![Editor de carga útil da ação de webhook do Zendesk com variáveis de corpo JSON.]({% image_buster /assets/img_archive/zendesk3.png %}){: style="max-width:70%;"}<br><br>
7. Selecione **Create**.<br><br>
8. Retorne ao seu webhook e clique em **Finish setup**.