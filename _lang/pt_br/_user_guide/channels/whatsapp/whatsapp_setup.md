---
nav_title: "Configuração"
article_title: "Configuração do WhatsApp"
alias: /partners/whatsapp/
description: "Este artigo aborda como configurar o canal de WhatsApp da Braze, incluindo pré-requisitos e próximas etapas sugeridas."
page_type: partner
search_tag: Partner
page_order: 0
channel:
  - WhatsApp
search_rank: 2
---

# Configuração do WhatsApp {#whatsapp-setup}

> O [WhatsApp](https://www.whatsapp.com/) Business messaging é uma plataforma popular de envio de mensagens ponto a ponto usada em todo o mundo, que oferece envio de mensagens baseado em conversas para empresas.

## Pré-requisitos {#prerequisites}

Reconheça os seguintes pontos antes de prosseguir com a integração:

- **Política de aceitação:** O WhatsApp exige que as empresas obtenham a aceitação dos clientes para o envio de mensagens.
- **Regras de conteúdo do WhatsApp:** O WhatsApp possui diversas [regras de conteúdo](https://www.whatsapp.com/legal/commerce-policy?l=en) que precisam ser seguidas.
- **Conformidade:** Esteja em conformidade com toda a documentação aplicável da Braze e da Meta, bem como com quaisquer [políticas da Meta](https://www.whatsapp.com/legal/?lang=en) aplicáveis.
- **Limite de conversa de 24 horas:** Após uma empresa enviar uma mensagem inicial com modelo ou um usuário enviar uma mensagem, uma janela de 24 horas será aberta, durante a qual ambas as partes podem trocar mensagens.
- **Início de conversa:** Os usuários podem iniciar uma conversa a qualquer momento. Uma empresa só pode iniciar uma conversa por meio de um modelo de mensagem aprovado.
<br><br>

| Requisito | Descrição |
| --- | --- |
| Conta do Meta Business Manager | Uma conta do Meta Business é necessária para aproveitar este canal de envio de mensagens. |
| Conta do WhatsApp Business | Uma conta do WhatsApp Business é necessária para aproveitar este canal de envio de mensagens. |
| Número de telefone do WhatsApp | Você deve adquirir um número de telefone que atenda aos requisitos do WhatsApp para a [API or interface de programação do aplicativo (API) Cloud](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) ou [API or interface de programação do aplicativo (API) On-Premises](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers) para uso do canal de envio de mensagens. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Conectar o WhatsApp Messenger à Braze {#step-1-connect-whatsapp-messenger-to-braze}

Na Braze, acesse **Integrações de parceiros** > **Parceiros de tecnologia** e pesquise **WhatsApp**.

Na página de parceiro do WhatsApp, selecione **Begin Integration**.

![Página de parceiro do WhatsApp com um botão para iniciar a integração.]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:70%;"}

Na janela aberta, selecione **Next** até o botão **Begin Integration** aparecer. Selecione o botão para iniciar o processo de integração.

![Instruções para conectar a Braze ao WhatsApp.]({% image_buster /assets/img/whatsapp/instructions.png %}){: style="max-width:50%;"}

### Etapa 2: Configuração do WhatsApp {#step-2-whatsapp-setup}

Em seguida, você será direcionado pelo fluxo de configuração da Braze. Para um passo a passo detalhado, consulte [Cadastro integrado do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup).

Nesse fluxo, você irá:
1. Criar ou selecionar suas contas Meta e WhatsApp Business. Certifique-se de revisar as [diretrizes de nome de exibição do WhatsApp](https://www.facebook.com/business/help/757569725593362). <br><br>É provável que você já tenha pelo menos uma conta Meta Business existente na sua empresa. Se for o caso, selecione aquela em que deseja que sua conta do WhatsApp Business esteja vinculada. As permissões de usuário e a verificação de negócios para o WhatsApp serão controladas centralmente na sua conta Meta Business.<br><br>
2. Criar seu perfil do WhatsApp Business.
3. Verificar seu número do WhatsApp Business.<br><br>

Após a conclusão da configuração, um [grupo de inscrições do WhatsApp]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#whatsapp-subscription-groups) dedicado será criado para seus usuários.

### Etapa 3: Criar modelos do WhatsApp {#step-3-create-whatsapp-templates}

Somente modelos de mensagem do WhatsApp aprovados podem ser usados para iniciar conversas com clientes. Os modelos do WhatsApp podem ser criados no [Meta Business Manager](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343). Para uma lista dos recursos de envio de mensagens do WhatsApp suportados pela Braze, confira [Recursos suportados do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#supported-whatsapp-features).

1. **Navegue até o [gerenciador de modelos](https://business.facebook.com/wa/manage/message-templates)**<br>
No Meta Business Manager, em **Account Tools**, selecione **Message Templates**.
Em seguida, selecione **Create Templates**.<br><br>![Gerenciador do WhatsApp com uma lista de modelos de mensagem.]({% image_buster /assets/img/whatsapp/whatsapp2.png %}){: style="max-width:100%;"}<br><br>
2. **Configurações da mensagem**<br>
No criador de novo modelo de mensagem, selecione a categoria da sua mensagem, nomeie seu modelo e escolha os idiomas que deseja suportar. Você pode excluir ou adicionar mais idiomas depois.<br><br>
	As categorias de modelo de mensagem disponíveis incluem as seguintes:
	- Marketing: envie ofertas promocionais, anúncios de produtos e mais para aumentar o reconhecimento e o engajamento
	- Utilidade: envie atualizações de conta, atualizações de pedidos, alertas e mais para compartilhar informações importantes
	- Autenticação: envie códigos que permitam que seus clientes acessem suas contas<br><br>
	![Criador de modelo de mensagem com categorias para marketing, utilidade e autenticação.]({% image_buster /assets/img/whatsapp/whatsapp3.png %}){: style="max-width:100%;"}<br><br>
3. **Editar modelo**<br>
Em seguida, crie seu modelo de mensagem. <br><br>Você pode fornecer um cabeçalho de texto ou mídia, o corpo do texto, um rodapé de mensagem e botões. Observe que cabeçalhos de vídeo e documento não estão disponíveis atualmente, e os cabeçalhos devem ser do tipo texto ou imagem. Qualquer mídia adicionada serve como exemplo para o processo de revisão e **não é** incluída no modelo de mensagem. A mídia precisa ser adicionada na Braze. Uma prévia da sua mensagem será exibida em um painel. <br><br>Embora a Meta não suporte Liquid, você pode inserir variáveis no modelo que posteriormente podem ser substituídas na Braze por variáveis Liquid. Selecione o botão **+ Add variable** para fazer isso.<br><br>![Criador de modelo.]({% image_buster /assets/img/whatsapp/whatsapp4.png %}){: style="max-width:100%;"}

Depois de concluir seu modelo, pressione **Submit**.

#### Tempo de aprovação do modelo {#template-approval-time}

Você pode verificar o status de aprovação do seu modelo de mensagem na página **Message Template** no Meta Business Manager ou ao criar uma campanha ou Canvas na Braze. Além disso, você pode ser notificado por e-mail pela equipe do WhatsApp, dependendo das suas permissões de notificação.

{% alert note %}
Modelos aprovados podem ser usados em quantas Campaigns e Canvas você quiser. Eles também podem ser enviados para quantos usuários com aceitação você desejar. Isso é válido, a menos que a qualidade do modelo diminua.
{% endalert %}

### Etapa 4: Criar uma campanha do WhatsApp {#step-4-create-a-whatsapp-campaign}

Depois que os modelos do WhatsApp forem aprovados, você pode ir ao dashboard para criar uma [campanha ou Canvas do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message).

{% alert note %}
Após a criação da sua conta do WhatsApp Business, a Meta determinará seu limite inicial de envio de mensagens. Para saber mais, confira [taxa de transferência]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup/10dlc#throughput).
{% endalert %}

## Próximos passos {#next-steps}

Após concluir a integração, recomendamos completar os dois processos Meta a seguir:
- [Verificação de negócios](https://www.facebook.com/business/help/2058515294227817?id=180505742745347)
	- Você pode já ter a verificação de negócios se tiver usado um Meta Business Manager existente.
- [Conta comercial oficial](https://www.facebook.com/business/help/604726921052590?ref=search_new_0)

Também recomendamos a leitura sobre [números de telefone dos usuários]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers) e adicionar quaisquer usuários que precisarão de acesso para criar [modelos de mensagem na sua organização](https://www.facebook.com/business/help/2169003770027706?id=2190812977867143).

### Armazenamento local da Cloud API or interface de programação do aplicativo (API) do WhatsApp {#whatsapp-cloud-api-local-storage}

A Braze oferece suporte ao [Armazenamento local da Cloud API or interface de programação do aplicativo (API)](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/local-storage?content_id=ka6F9gESPqhQpm5) do WhatsApp. Para ativar esse recurso, entre em contato com o gerente de suporte ao cliente da Braze.