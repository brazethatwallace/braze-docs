---
nav_title: Inkit
article_title: Inkit
alias: /partners/inkit/
description: "Este artigo de referência descreve a parceria entre a Braze e a Inkit, que permite a você economizar tempo e esforço com a automatização de campanhas de mala direta e recuperação de clientes offline."
page_type: partner
search_tag: Partner

---

# Inkit

> A [Inkit](https://www.inkit.com) e a Braze ajudam organizações a gerar e distribuir documentos de forma segura, tanto em meio digital quanto por mala direta.

_Essa integração é mantida pela Inkit._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Inkit permite gerar documentos e enviá-los por mala direta aos usuários da Braze com webhooks da Braze.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| Conta da Inkit | É necessário ter uma [conta Inkit](https://www.inkit.com/) para aproveitar essa parceria. |
| Chave de API da Inkit<br><br>`<INKIT_API_TOKEN>` | Essa chave pode ser encontrada no [dashboard da Inkit](https://app.inkit.io/#/account/integrations), na guia **Development**, e permitirá a conexão das contas da Braze e da Inkit. |
| ID de modelo da Inkit<br><br>`<INKIT_TEMPLATE_ID>` | Depois de criar um modelo, você pode copiar o ID do modelo na guia **Templates** para usá-lo em seu modelo na Braze.<br><br>Por exemplo, você pode criar um modelo chamado `invoice_template` no ambiente da Inkit com o ID de modelo: `tmpl_3bDScFl9cwr3OAVR1RSdEC`. |
| Cabeçalho HTTP | O cabeçalho HTTP faz parte da solicitação de API que você envia da Braze para a Inkit. Nele, você incluirá sua chave de API da Inkit para autenticar e autorizar chamadas para a API da Inkit. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integração {#integration}

### Etapa 1: crie um modelo da Inkit {#step-1-create-an-inkit-template}

Na plataforma da Inkit, crie um modelo para ser usado na sua Campaign da Braze em HTML, Word, PowerPoint, Excel ou PDF. Consulte a [documentação da Inkit](https://docs.inkit.com/docs/create-a-template) para saber mais.

### Etapa 2: crie seu modelo de webhook da Braze {#step-2-create-your-braze-webhook-template}

Para criar um modelo de webhook da Inkit a ser usado em futuras Campaigns ou Canvas, acesse **Conteúdo** > **Webhook** na plataforma Braze. Em seguida, selecione **Create webhook template**.

Se você quiser criar uma Campaign única de webhook da Inkit ou usar um modelo existente, selecione **Webhook** na Braze ao criar uma nova Campaign.

![Uma seleção de modelos de webhook predefinidos disponíveis na guia Modelos de webhook da seção Modelos e mídia.]({% image_buster /assets/img/inkit-webhook-template.png %})

Depois de selecionar o modelo de webhook da Inkit, você verá o seguinte:
- **Webhook URL**: em branco
- **Request Body**: texto bruto

No campo Webhook URL, [crie](https://docs.inkit.com/docs/set-up-a-webhook-to-an-event) e insira uma URL de webhook da Inkit.

![Código do corpo da solicitação e URL do webhook exibidos na guia de composição do criador de webhooks da Braze.]({% image_buster /assets/img/inkit-integration.png %})

#### Cabeçalhos de solicitação e método {#request-headers-and-method}

A Inkit requer um `HTTP Header` para autorização que inclua sua chave de API da Inkit codificada em base 64. O seguinte já estará incluído no modelo como um par chave-valor, mas na guia **Settings**, você deve substituir o `<INKIT_API_TOKEN>` pela sua chave de API da Inkit.

{% raw %}
- **HTTP Method**: POST
- **Request Header**:
  - **Authorization**: Basic `{{ '<INKIT_API_TOKEN>' | base64_encode }}`
  - **Content-Type**: application/json
{% endraw %}

#### Corpo da solicitação {#request-body}

Certifique-se de que seu Liquid corresponda aos atributos personalizados adequados associados aos seguintes campos obrigatórios e opcionais. Você também pode adicionar campos de dados personalizados a qualquer solicitação.

```json
{% raw %}{
  "api_token": "<INKIT_API_TOKEN>",
  "template_id": "<INKIT_TEMPLATE_ID>",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "company": "{{custom_attribute.${company_name}}}",
  "phone" : "{{${phone_number}}}",
  "address_line_1": "{{custom_attribute.${address}}}",
  "address_line_2": "{{custom_attribute.${address2}}}",
  "address_city": "{{${city}}}",
  "address_state": "{{custom_attribute.${state}}}",
  "address_zip": "{{custom_attribute.${zip}}}",
  "address_country": "{{${country}}}",
  "source" : "Braze"
}{% endraw %}
```

### Etapa 3: pré-visualize sua solicitação {#step-3-preview-your-request}

Seu texto bruto será automaticamente destacado se for uma tag Braze aplicável. Os campos `street`, `unit`, `state` e `zip` devem ser configurados como [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes) para enviar esse webhook.

Pré-visualize a solicitação no painel **prévia** ou navegue até a guia **Test**, onde é possível selecionar um usuário aleatório, um usuário existente ou personalizar o seu próprio usuário para testar o webhook.

{% alert important %}
Lembre-se de salvar seu modelo antes de sair da página! <br>Os modelos de webhook atualizados podem ser encontrados na lista **Modelos de webhooks salvos** ao criar uma nova [Campaign de webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/).
{% endalert %}