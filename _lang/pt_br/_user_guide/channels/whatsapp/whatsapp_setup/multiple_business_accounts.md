---
nav_title: "Múltiplas contas comerciais"
article_title: "Múltiplas contas comerciais"
page_order: 5
description: "Este artigo de referência aborda as etapas para adicionar contas do WhatsApp Business e números de telefone."
page_type: reference
channel:
  - WhatsApp
---

# Múltiplas contas do WhatsApp Business e números de telefone {#multiple-whatsapp-business-accounts-and-phone-numbers}

> Você pode adicionar múltiplas contas do WhatsApp Business e grupos de inscrições (e números de telefone) a cada espaço de trabalho. <br><br>Cada grupo de inscrições está conectado a um único número de telefone, então você não pode conectar o mesmo número de telefone a múltiplos grupos de inscrições nem conectar múltiplos números de telefone a um grupo de inscrições.

## Múltiplas contas do WhatsApp Business {#multiple-whatsapp-business-accounts}

Ter múltiplas contas do WhatsApp Business é útil quando você deseja enviar mensagens do WhatsApp para usuários em um espaço de trabalho da Braze que possui múltiplas marcas. Isso porque cada conta comercial opera separadamente dentro do WhatsApp e possui seu próprio número de telefone, modelo de mensagem e classificação de qualidade.

Contas comerciais que estão aninhadas dentro do mesmo Meta Business Manager também compartilham o gerenciamento de permissões de acesso de usuários e catálogos (ainda não suportado na Braze).

![Diagrama do ecossistema da Braze e do WhatsApp, mostrando como espaços de trabalho e contas do WhatsApp Business se conectam entre si: você pode conectar um grupo de inscrições a um número de telefone, múltiplas contas do WhatsApp Business a um espaço de trabalho e um espaço de trabalho a múltiplos Meta Business Portfolios.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %})

### Adicionando uma conta do WhatsApp Business {#adding-a-whatsapp-business-account}

Você pode adicionar até 10 contas do WhatsApp Business por espaço de trabalho. As contas comerciais podem estar aninhadas em diferentes Meta Business Managers. Para adicionar uma conta:

1. Acesse **Parceiros de tecnologia** > **WhatsApp** e selecione **Add WhatsApp Business Account**.

![Seção de integração de mensagens do WhatsApp com opções para adicionar uma conta comercial ou adicionar um grupo de inscrições e número.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2. Siga o fluxo de cadastro. Para um passo a passo detalhado, consulte [Cadastro integrado do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup).

{% alert important %}
Seu número de telefone deve seguir todos os requisitos de qualquer número de telefone do WhatsApp, incluindo não estar registrado em nenhuma outra conta do WhatsApp.
{% endalert %}

## Múltiplos grupos de inscrições e números de telefone {#multiple-subscription-groups-and-phone-numbers}

Os modelos de mensagem são compartilhados entre todos os números de telefone na mesma conta do WhatsApp Business. Para mais detalhes sobre grupos de inscrições do WhatsApp, consulte [Grupos de inscrições]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups).

Cada número de telefone do WhatsApp aparecerá como um chat separado do WhatsApp para os usuários. Cada número de telefone dentro de uma conta do WhatsApp Business opera independentemente dos demais, então eles podem ter os mesmos ou diferentes valores para o seguinte:
- Nome de exibição
- Status
- Classificação de qualidade
- Limite de mensagens

### Adicionando um grupo de inscrições e número de telefone {#adding-a-subscription-group-and-phone-number}

Você pode adicionar até 20 grupos de inscrições (e números de telefone de envio) por conta do WhatsApp Business. Para adicionar um grupo de inscrições e número de telefone:

1. Acesse **Parceiros de tecnologia** > **WhatsApp** e selecione **Add Subscription Group and Number**.

![Seção de integração de mensagens do WhatsApp com opções para adicionar uma conta comercial ou adicionar um grupo de inscrições e número.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2. Siga o fluxo de cadastro. <br><br> Na etapa **Select your WhatsApp Business Account**, selecione sua conta do WhatsApp Business existente e adicione um novo número de telefone. Esse número deve seguir todos os requisitos de qualquer número de telefone do WhatsApp, incluindo não estar registrado em nenhuma outra conta do WhatsApp.

### Removendo um grupo de inscrições e número de telefone {#removing-a-subscription-group-and-phone-number}

1. Acesse **Público** > **Inscrições** e arquive o grupo de inscrições.
2. Acesse seu Meta Business Manager e exclua o número de telefone.