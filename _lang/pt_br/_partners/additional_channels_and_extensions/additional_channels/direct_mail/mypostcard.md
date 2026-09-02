---
nav_title: MyPostcard
article_title: MyPostcard
page_order: 1
description: "Este artigo de referência descreve a parceria entre a Braze e o MyPostcard, que permite usar mala direta como um canal adicional para o seu fluxo de trabalho de CRM."
alias: /partners/mypostcard/
page_type: partner
search_tag: Partner

---

# MyPostcard

> O [MyPostcard](https://www.mypostcard.com), um app global líder em cartões postais, capacita você a executar campanhas de mala direta com facilidade, proporcionando uma maneira simples e lucrativa de se conectar com seus clientes.

Use a integração do MyPostcard com a Braze para enviar facilmente correspondências impressas aos seus clientes.

## Pré-requisitos {#prerequisites}

| Requisito                        | Descrição                                                                                                               |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Conta MyPostcard B2B             | O registro no MyPostcard é necessário para aproveitar esta integração.                                                  |
| Chave de API or interface de programação do aplicativo (API) B2B e credenciais   | Você pode encontrar sua chave de API or interface de programação do aplicativo (API) e as credenciais na ferramenta de administração B2B do MyPostcard.                 |
| Campanha B2B MyPostcard aprovada | Para aproveitar esta integração, você precisa configurar uma campanha de mala direta impressa na ferramenta B2B do MyPostcard. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

Para elevar suas campanhas de mala direta, é crucial ir além dos envios em massa tradicionais e integrar a correspondência impressa de forma fluida em seus fluxos de trabalho. Essa abordagem permite que você alcance clientes específicos que optaram por não receber seus e-mails informativos ou cujos e-mails estão marcados como spam. Com o MyPostcard, você pode enviar campanhas de mala direta impressas diretamente pela Braze.

- Construa fluxos de trabalho intuitivos na Braze, incorporando correspondência impressa como um novo canal poderoso, sem nenhuma experiência técnica.
- Desbloqueie o potencial de correspondências impressas personalizadas com alguns passos simples.
- Beneficie-se de uma implementação simples que é apoiada por suporte personalizado de uma equipe dedicada.

## Integração {#integration}

Para integrar com o MyPostcard, [faça login ou inscreva-se](https://www.mypostcard.com/b2b/admin/) e crie sua primeira campanha para usá-la por meio de [webhooks da Braze]({{site.baseurl}}/user_guide/channels/webhooks/).

### Etapa 1: Crie seu modelo de webhook da Braze {#step-1-create-your-braze-webhook-template}

Para criar um modelo de webhook do MyPostcard para usar em futuras Campaigns ou Canvas, acesse **Conteúdo** > **Webhook** na plataforma Braze. Em seguida, selecione **Create webhook template**.

Se você quiser criar uma campanha de webhook do MyPostcard única ou usar um modelo existente, selecione **Webhook** na Braze ao criar uma nova campanha. Preencha os seguintes campos:

| Campo           | Descrição                                                 |
|-----------------|-----------------------------------------------------------|
| **Webhook URL** | A URL do webhook conforme mostrada na ferramenta de administração B2B. |
| **Request Body** | Texto bruto (formato JSON encontrado na ferramenta de administração B2B). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 1: Crie seu modelo de webhook da Braze" }

#### Método de solicitação e cabeçalhos {#request-method-and-headers}

O MyPostcard requer um método HTTP juntamente com os seguintes cabeçalhos HTTP a serem incluídos no modelo.

{% raw %}
<table aria-label="Método de solicitação e cabeçalhos">
  <caption>Método de solicitação e cabeçalhos</caption>
  <thead>
    <tr>
      <th><strong>Campo</strong></th>
      <th><strong>Informações</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>HTTP Method</strong></td>
      <td><code>POST</code></td>
    </tr>
    <tr>
      <td><strong>Username</strong></td>
      <td><code>{{ '&lt;username&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>Password</strong></td>
      <td><code>{{ '&lt;password&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>Content-Type</strong></td>
      <td><code>application/json</code></td>
    </tr>
  </tbody>
</table>
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 aria-label="Método de solicitação e cabeçalhos" }

#### Corpo da solicitação {#request-body}

Copie o corpo da solicitação exibido na ferramenta de administração B2B e preencha os espaços reservados com conteúdo usando quaisquer tags de personalização Liquid.

![Guia Redigir mostrando o corpo JSON e informações do webhook.]({% image_buster /assets/img/mypostcard/mypostcard_compose.jpg %})

### Etapa 2: Visualize sua solicitação {#step-2-preview-your-request}

Em seguida, visualize sua solicitação no painel **prévia** ou acesse a guia **Test**, onde é possível selecionar um usuário aleatório, um usuário existente ou criar um usuário personalizado para testar seu webhook. Não se esqueça de salvar seu modelo antes de sair da página!

![Guia de teste de webhook com diferentes campos para validar a implementação.]({% image_buster /assets/img/mypostcard/mypostcard_test.jpg %})

{% alert important %}
Lembre-se de salvar seu modelo antes de sair da página! <br>Os modelos de webhook atualizados podem ser encontrados na lista **Modelos de webhooks salvos** ao criar uma nova [campanha de webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/).
{% endalert %}