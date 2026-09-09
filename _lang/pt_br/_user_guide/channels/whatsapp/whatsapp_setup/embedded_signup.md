---
nav_title: Cadastro integrado
article_title: Cadastro integrado do WhatsApp
page_order: 1
description: "Este artigo de referência aborda como acessar o fluxo de cadastro integrado do WhatsApp na Braze, o que preparar antes do cadastro na Meta e o que acontece após a conclusão do cadastro."
page_type: reference
channel:
  - WhatsApp
---

# Cadastro integrado do WhatsApp {#whatsapp-embedded-signup}

> Use o cadastro integrado para conectar a Braze a uma conta do WhatsApp Business (WABA) por meio do fluxo de cadastro hospedado pela Meta.

O fluxo de cadastro integrado do WhatsApp é acessado quando você [integra o WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) ao seu espaço de trabalho da Braze pela primeira vez, e quando você [adiciona uma conta do WhatsApp Business ou um número de telefone]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups) a uma integração existente.

{% alert note %}
Você pode adicionar [múltiplas contas do WhatsApp Business]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/multiple_business_accounts) a um espaço de trabalho da Braze. No entanto, cada conta específica do WhatsApp Business pode ser adicionada a apenas um espaço de trabalho da Braze.
{% endalert %}

## Acessando o fluxo de trabalho {#accessing-the-workflow}

1. Acesse **Integrações com Parceiros** > **Parceiros de Tecnologia**.
2. Pesquise e selecione **WhatsApp**.
3. Selecione a opção que corresponde ao seu caso de uso:
   - **Primeira integração:** Selecione **Begin Integration**.
   - **Conta ou número adicional:** Na página **WhatsApp Messaging Integration**, selecione **Add account or number** ou **Add WhatsApp Business Account**.

O fluxo de inscrição incorporado da Meta é o mesmo, independentemente do ponto de entrada a partir do qual você o inicia. Seu espaço de trabalho também pode exibir guias de integração, como **Native Integration** ou **BYO Connector - Infobip**, dependendo da sua configuração. Selecione a guia que corresponde à sua configuração antes de começar.

## Preparação para a inscrição {#prepare-for-signup}

Ao selecionar **Begin Integration**, a Braze abre uma janela de integração. Revise cada slide e selecione **Begin Integration** novamente para iniciar a inscrição incorporada do Meta.

Antes de começar, prepare o seguinte:

- **Acesso ao Meta Business Manager:** A maioria das empresas usa o Meta Business Manager para gerenciar páginas do Facebook, anúncios e ativos de negócios relacionados. Se você não tiver acesso, peça a um administrador para conceder permissões ou crie uma conta do Business Manager durante a inscrição.
- **Número de telefone:** Use um número que atenda aos [requisitos de número de telefone do WhatsApp da Meta](https://developers.facebook.com/docs/whatsapp/phone-numbers). Você receberá um código de verificação único por mensagem de texto ou ligação durante a inscrição.

{% alert important %}
Você só concluirá a inscrição incorporada inicial uma vez por jornada de integração, então insira os dados da sua empresa com a maior precisão possível.
{% endalert %}

## Fluxo de cadastro integrado do WhatsApp {#whatsapp-embedded-signup-workflow}

Depois que a Braze iniciar o cadastro integrado da Meta, faça login com uma conta Meta que tenha acesso ao Business Manager da sua empresa. A Meta hospeda as telas de cadastro; a Braze não controla o layout nem os rótulos dessas telas.

{% alert note %}
A Meta pode alterar as telas do cadastro integrado sem aviso prévio. Se o fluxo for diferente do descrito neste artigo, siga as instruções da Meta e consulte a [documentação de cadastro integrado da Meta](https://developers.facebook.com/docs/whatsapp/embedded-signup/embed-the-flow).
{% endalert %}

De modo geral, a Meta orienta você nas seguintes etapas:

1. **Fazer login e conceder permissões.** Autentique-se com a Meta e permita que a Braze se conecte à sua conta do WhatsApp Business.
2. **Selecionar seu portfólio de negócios.** Conecte o portfólio do Business Manager que será proprietário da conta do WhatsApp Business. Se você não encontrar o portfólio esperado, verifique suas permissões na Meta.
3. **Conectar ou criar uma conta do WhatsApp Business.** Crie uma nova conta ou selecione uma conta não utilizada quando solicitado. Não selecione uma conta do WhatsApp Business que já esteja conectada a outro provedor de envio de mensagens; essa conexão não será bem-sucedida na Braze. Para [migrar um número de outro provedor]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number), entre em contato com a equipe da sua conta Braze antes de começar.
4. **Fornecer detalhes do negócio e de exibição.** Insira o nome da conta, o nome de exibição e a categoria que a Meta solicita para a sua conta do WhatsApp Business.
5. **Verificar seu número de telefone.** Adicione o número que você deseja usar para o envio de mensagens pelo WhatsApp e conclua a verificação por mensagem de texto ou chamada telefônica.

Quando a Meta finalizar o cadastro integrado, o controle retorna para a Braze.

## Concluir a integração com a Braze {#complete-the-braze-integration}

Após a inscrição incorporada, a Braze executa as etapas de configuração automaticamente. Na página **WhatsApp Messaging Integration**, você pode ver mensagens de progresso como **Sign-up flow completed, integration with WhatsApp in progress** enquanto a Braze realiza o seguinte:

- Recupera o ID da sua conta WhatsApp Business e os números de telefone do Meta
- Adiciona o usuário de sistema da Braze à sua conta WhatsApp Business
- Registra números de telefone e faz a inscrição em eventos de webhook
- Cria um [grupo de inscrições]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups) da Braze para cada número conectado

Aguarde a conclusão da integração antes de enviar mensagens. Se a configuração falhar, revise o erro na página de integração e consulte [Configuração do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) para orientações gerais.

## Próximos passos {#next-steps}

- [Adquirir ou migrar um número de telefone do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers)
- [Criar uma mensagem do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message)
- [Gerenciar grupos de inscrições]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)