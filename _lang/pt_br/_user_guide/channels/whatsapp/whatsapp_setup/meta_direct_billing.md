---
nav_title: Meta Direct Billing
article_title: Meta Direct Billing
page_order: 7
description: "Este artigo de referência aborda como configurar o Meta Direct Billing para que você pague pelos custos de envio de mensagens do WhatsApp com seu próprio cartão de débito ou crédito, em vez de usar uma linha de crédito da Braze ou de um parceiro."
page_type: reference
channel:
  - WhatsApp
alias: /whatsapp_meta_direct_billing/
hidden: true
noindex: true
---

# Meta Direct Billing {#meta-direct-billing}

> O Meta Direct Billing permite que você pague pelos custos de envio de mensagens do WhatsApp diretamente com seu próprio cartão de débito ou crédito, em vez de cobrar por meio de uma linha de crédito da Braze ou de um parceiro.

## Pré-requisitos {#prerequisites}

Antes de configurar o Meta Direct Billing, verifique se você tem o seguinte:

| Requisito | Descrição |
| --- | --- |
| Acesso ao espaço de trabalho da Braze | Você precisa de acesso a **Partner Integrations** > **Technology Partners** na Braze para iniciar o fluxo de inscrição incorporado. |
| Conta no Meta Business Manager | O faturamento é configurado no Meta Business Manager, em **Billing & payments**. |
| Cartão de débito ou crédito | É necessário um cartão válido para concluir a configuração. O faturamento mensal pode aparecer como opção em algumas contas, mas não é garantido. |
| Informações comerciais completas | O nome da empresa, endereço e moeda devem estar preenchidos e corretos. A Meta analisa essas informações antes de habilitar o envio de mensagens. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Configuração {#setup}

### Etapa 1: Selecionar Meta Direct Billing {#step-1-select-meta-direct-billing}

1. Na Braze, acesse **Partner Integrations** > **Technology Partners**, pesquise por **WhatsApp** e abra a página **WhatsApp Messaging Integration**.
2. Selecione a guia **Meta Direct Billing**. Isso significa que seu relacionamento de faturamento é diretamente com a Meta, e não por meio da Braze ou de uma linha de faturamento da Infobip. Por isso, é importante selecionar essa guia antes de continuar, em vez de tentar alterar depois.
3. Em **Add a WhatsApp Business Account or phone number**, selecione **Add account or number**. Isso inicia a inscrição incorporada da Meta, onde você fará login na Meta, selecionará seu portfólio de negócios, criará ou selecionará sua WhatsApp Business Account (WABA) e verificará seu número de telefone.

### Etapa 2: Acessar Billing & payments {#step-2-go-to-billing-payments}

Após concluir a inscrição incorporada da Meta, faça uma das seguintes ações:

- Selecione **Add payment method**, que leva você ao Meta Business Manager.
- No Meta Business Manager, acesse **Billing & payments** > **Accounts** e selecione sua WABA.

### Etapa 3: Adicionar um método de pagamento {#step-3-add-a-payment-method}

1. Selecione **Add payment method**.
2. Na janela que se abre, confirme o **Business location and currency** (por exemplo, **Canada, US Dollars USD**), que determina a moeda em que você será cobrado. Selecione **Edit** se precisar alterar.
3. Em **Select payment method**, você pode ver linhas de crédito existentes. Elas não estão disponíveis para seu uso; não as selecione. Para mais detalhes, consulte [restrições de linha de faturamento](#billing-line-restrictions).

![A janela Select payment method com Debit or credit card selecionado e as linhas de crédito existentes da Infobip e da Braze deixadas sem seleção.]({% image_buster /assets/img/whatsapp/payment_methods.png %}){: style="max-width:40%;"}

{: start="4"}
4. Em **Add payment method**, selecione **Debit or credit card** e depois selecione **Next**.
5. Insira os dados do seu cartão e selecione **Save**.
6. Seu cartão aparece em **Payment methods**, marcado como **Default**, com o número mascarado do cartão e a data de expiração exibidos.

{% alert note %}
Fechar a janela de configuração após adicionar seu método de pagamento não desconecta seu número de telefone. O número vinculado é mantido.
{% endalert %}

### Etapa 4: Confirmar suas informações comerciais {#step-4-confirm-your-business-information}

A Meta analisa o nome da empresa, endereço e moeda antes de habilitar o envio de mensagens. Informações comerciais incompletas ou incorretas podem resultar em falha no envio de mensagens ou em um erro de informações comerciais inválidas.

## Restrições de linha de faturamento {#billing-line-restrictions}

As linhas de crédito exibidas na lista de métodos de pagamento (por exemplo, "Infobip Limited" ou "BRAZE INC.") pertencem a essa empresa específica, não a você. Elas aparecem por causa da forma como sua conta está conectada, mas não podem ser selecionadas.

## Recursos da Meta {#meta-resources}

- [Central de Ajuda do Meta Business: Faturamento e pagamentos](https://business.facebook.com/business/help/535561817791563)
- [Central de Ajuda do Meta Business: Como adicionar um método de pagamento](https://www.facebook.com/business/help/832746984379005)