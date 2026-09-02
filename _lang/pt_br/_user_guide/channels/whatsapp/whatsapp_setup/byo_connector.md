---
nav_title: Conector BYO WhatsApp
article_title: Conector Bring Your Own WhatsApp
page_order: 2
description: "Este artigo de referência fornece um passo a passo para configurar um conector Bring Your Own WhatsApp, que dá à Braze acesso ao seu Infobip WhatsApp Business Manager."
page_type: reference
channel:
  - WhatsApp
---

# Conector Bring Your Own WhatsApp {#bring-your-own-whatsapp-connector}

> O conector Bring Your Own (BYO) WhatsApp oferece uma parceria entre a Braze e a Infobip, na qual você dá à Braze acesso ao seu Infobip WhatsApp Business Manager (WABA). Isso permite que você gerencie e pague pelos custos de envio de mensagens diretamente com a Infobip, enquanto usa a Braze para segmentação, personalização e orquestração de campanhas. A Braze mantém todas as funcionalidades existentes que o canal WhatsApp oferece, como mensagens de saída, processamento de mensagens de entrada, fluxos do WhatsApp e análise de dados.

{% alert note %}
Para migrar de outros provedores de soluções de negócios (BSPs) para a integração com a Braze, consulte [Migrar de outro provedor de soluções de negócios]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number#migrate-from-another-business-solution-provider).
{% endalert %}

## Requisitos {#requirements}

| Requisito | Descrição |
| --- | --- |
| Conta Infobip | Uma conta Infobip é necessária para usar o conector BYO WhatsApp. |
| Créditos de mensagem ou ação | Você consome créditos de ação da Braze ao enviar mensagens pelo WhatsApp. |
| Requisitos do WhatsApp | Conclua todos os [requisitos do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup#prerequisites). |
| Número de telefone | Sugerimos que você [adquira um número de telefone pela Infobip](https://www.infobip.com/docs/numbers/getting-started) por conveniência. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Configuração {#set-up}

Antes de configurar o conector BYO WhatsApp, confirme que os envios anteriores da sua conta WhatsApp Business não foram feitos pela Infobip.

### Casos suportados {#supported-cases}

- A conta WhatsApp Business e o número de telefone nunca foram conectados a um parceiro antes
- A conta WhatsApp Business está conectada diretamente à Braze pela integração nativa.
    - Siga as etapas em [Migrar entre contas WhatsApp Business]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number#migrate-between-whatsapp-business-accounts) para migrar seus números de telefone para uma nova conta WhatsApp Business, um número de telefone por vez.
- A conta WhatsApp Business está conectada a um provedor de soluções diferente da Braze e da Infobip
    - Siga as etapas em [Migrar entre contas WhatsApp Business]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number#migrate-between-whatsapp-business-accounts) para migrar seus números de telefone para uma nova conta WhatsApp Business, um número de telefone por vez.

## Etapa 1: Recuperar informações da conta Infobip {#step-1}

1. Na Infobip, identifique a conta que você deseja usar com sua conta WhatsApp Business.
2. Acesse **Developer Tools** > **API Keys** e selecione **Create API Key**.

![Página "Create API key" com data de criação "16/12/2025" e data de expiração "16/12/36".]({% image_buster /assets/img/whatsapp/byo_connector/create_api_key.png %})

{: start="3"}
3. Dê à chave um nome significativo, como "Braze - Meu Nome de Espaço de Trabalho - Meu Nome WABA".
4. Adicione uma data de vencimento bem distante no futuro para evitar problemas com a expiração do token.
    - Anote para gerar uma nova chave de API e reconectar seu WABA antes da data de vencimento.
5. Selecione estes escopos:
- `Message:send`
- `Whatsapp:manage`
- `Whatsapp:message:send`
- `Account-management:manage`
- `Subscriptions:manage`
- `Metrics:manage`
6. Após criar a chave, copie a chave de API.
    - A chave só pode ser copiada por um tempo limitado após a criação. Você pode repetir essas etapas para criar uma nova chave se precisar conectar outra conta WhatsApp Business no futuro.

![Exemplo de chave de API da Braze com 6 escopos adicionados.]({% image_buster /assets/img/whatsapp/byo_connector/api_key.png %})

{: start="7"}
7. Copie a URL base da API da conta.

![Página "API keys" com a URL base da API destacada.]({% image_buster /assets/img/whatsapp/byo_connector/api_base_url.png %})

## Etapa 2: Iniciar o cadastro incorporado {#step-2-start-the-embedded-signup}

1. Na Braze, acesse **Integrações de parceiros** > **Parceiros de tecnologia** > **WhatsApp**
2. Selecione a guia **BYO Connector - Infobip**.

![A página de parceiros de tecnologia do WhatsApp.]({% image_buster /assets/img/whatsapp/byo_connector/byo_tab_tech_parners.png %})

{: start="3"}
3. Insira a chave de API e a URL base da [Etapa 1](#step-1).
4. Selecione **Connect**.
5. Prossiga pelo [fluxo de trabalho de cadastro incorporado]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup#whatsapp-embedded-signup-workflow) com estas considerações:
- Você não pode selecionar o mesmo portfólio de negócios que é usado por um provedor de soluções de negócios diferente.
- Você não pode selecionar um número de telefone que está sendo usado por outro provedor de soluções de negócios.
- Você deve criar um novo WABA, não selecionar um existente.

{% alert note %}
Para receber o código de verificação, acesse o dashboard da Infobip > **Analyze** > **Logs** e obtenha o código da mensagem SMS de entrada.
{% endalert %}

![Registros de mensagens mostrando uma mensagem SMS de entrada com o código de verificação.]({% image_buster /assets/img/whatsapp/byo_connector/verification_code.png %})

Após concluir a configuração, seu número de telefone é listado como um grupo de inscrições no seu grupo WhatsApp Business. O grupo WhatsApp Business contém o nome da conta Infobip e a URL base da API à qual está conectado. Contas conectadas pela integração nativa não possuem um nome de conta Infobip.

{% alert note %}
Conecte cada conta WhatsApp Business a uma única conta Infobip. Cada vez que você conectar um número de telefone ou grupo de inscrições adicional, se a conta WhatsApp Business já estiver conectada a uma conta Infobip, você deverá inserir novamente as credenciais de API da conta existente.
{% endalert %}

## Etapa 3: Envio de mensagens {#step-3-sending-messages}

Siga o processo de envio da integração nativa, incluindo:
- [Inscrever usuários no grupo de inscrições]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)
- [Criar uma mensagem do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message)

## Solução de problemas de configuração {#troubleshooting-setup}

### Não foi possível recuperar o ID da conta WhatsApp Business {#couldnt-retrieve-whatsapp-business-account-id}

Confirme que sua conta WhatsApp Business não está conectada a um espaço de trabalho diferente da Braze.

### Não foi possível compartilhar o ID da conta WhatsApp Business com a Infobip {#couldnt-share-whatsapp-business-account-id-with-infobip}

1. Confirme que sua conta WhatsApp Business não está conectada à Braze ou a outro parceiro.
2. Confirme que nenhum número de telefone na sua conta WhatsApp Business está conectado a uma conta Infobip diferente. Para números importados, você pode encontrar o número na Infobip e selecionar **Cancel number**.

## Considerações {#considerations}

Embora todas as funcionalidades existentes com a Braze sejam suportadas, estes casos de uso atualmente não são suportados.

| Caso de uso | Motivo |
| --- | --- |
| Processar mensagens de entrada na Braze e na Infobip | Isso impede cadeias lógicas que são disparadas por qualquer um dos sistemas, consequentemente gerando threads de mensagens duplicadas e potencialmente contraditórias. |
| Enviar mensagens pela Braze e pela Infobip | Para contas WhatsApp Business conectadas à Braze, todo o envio é originado pela Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Considerações" }