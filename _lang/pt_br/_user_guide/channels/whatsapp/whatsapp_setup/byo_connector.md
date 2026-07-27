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
| Conta Infobip | É necessário ter uma conta Infobip para usar o conector BYO WhatsApp. |
| Créditos de mensagem ou ação | Você consome Créditos de Ação da Braze ao enviar mensagens do WhatsApp. |
| Requisitos do WhatsApp | Conclua todos os [requisitos do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup#prerequisites). |
| Número de telefone | Sugerimos que você [adquira um número de telefone pela Infobip](https://www.infobip.com/docs/numbers/getting-started) por conveniência. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Configuração {#set-up}

Antes de configurar o conector BYO WhatsApp, confirme que os envios anteriores da sua conta do WhatsApp Business não foram feitos por meio da Infobip.

### Casos compatíveis {#supported-cases}

- A conta do WhatsApp Business e o número de telefone nunca foram conectados a um parceiro antes
- A conta do WhatsApp Business está conectada diretamente à Braze por meio da integração nativa.
    - Siga as etapas em [Migrar entre contas do WhatsApp Business]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number#migrate-between-whatsapp-business-accounts) para migrar seus números de telefone para uma nova conta do WhatsApp Business, um número de telefone por vez.
- A conta do WhatsApp Business está conectada a um provedor de solução diferente da Braze e da Infobip
    - Siga as etapas em [Migrar entre contas do WhatsApp Business]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number#migrate-between-whatsapp-business-accounts) para migrar seus números de telefone para uma nova conta do WhatsApp Business, um número de telefone por vez.

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

## Etapa 2: Iniciar o cadastro integrado {#step-2-start-the-embedded-signup}

1. Na Braze, acesse **Integrações com Parceiros** > **Parceiros de Tecnologia** > **WhatsApp**
2. Selecione a guia **BYO Connector - Infobip**.

![A página de parceiros de tecnologia do WhatsApp.]({% image_buster /assets/img/whatsapp/byo_connector/byo_tab_tech_parners.png %})

{: start="3"}
3. Insira a chave de API e a URL base da [Etapa 1](#step-1).
4. Selecione **Connect**.
5. Prossiga pelo [fluxo de trabalho de cadastro integrado]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup#whatsapp-embedded-signup-workflow) com as seguintes considerações:
- Você não pode selecionar o mesmo portfólio de negócios que é usado por outro provedor de soluções de negócios.
- Você não pode selecionar um número de telefone que é usado por outro provedor de soluções de negócios.
- Você deve criar uma nova WABA, e não selecionar uma existente.

{% alert note %}
Para receber o código de verificação, acesse o dashboard da Infobip > **Analyze** > **Logs** e obtenha o código a partir da mensagem SMS recebida.
{% endalert %}

![Registros de mensagens mostrando uma mensagem SMS recebida com o código de verificação.]({% image_buster /assets/img/whatsapp/byo_connector/verification_code.png %})

Após concluir a configuração, seu número de telefone será listado como um grupo de inscrições no seu WhatsApp Business Group. O WhatsApp Business Group contém o nome da conta Infobip e a URL base da API à qual está conectado. Contas conectadas por meio da integração nativa não possuem um nome de conta Infobip.

{% alert note %}
Conecte cada WhatsApp Business Account a uma única conta Infobip. Cada vez que você conectar um número de telefone ou grupo de inscrições adicional, se a WhatsApp Business Account já estiver conectada a uma conta Infobip, será necessário reinserir as credenciais de API da conta existente.
{% endalert %}

## Etapa 3: Envio de mensagens {#step-3-sending-messages}

Siga o processo de envio da integração nativa, incluindo:
- [Inscrever usuários no grupo de inscrições]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)
- [Criar uma mensagem de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message)

## Solução de problemas de configuração {#troubleshooting-setup}

### Não foi possível recuperar o ID da conta do WhatsApp Business {#couldnt-retrieve-whatsapp-business-account-id}

Confirme que sua conta do WhatsApp Business não está conectada a um espaço de trabalho diferente da Braze.

### Não foi possível compartilhar o ID da conta do WhatsApp Business com a Infobip {#couldnt-share-whatsapp-business-account-id-with-infobip}

1. Confirme que sua conta do WhatsApp Business não está conectada à Braze ou a outro parceiro.
2. Confirme que nenhum número de telefone na sua conta do WhatsApp Business está conectado a uma conta diferente da Infobip. Para números importados, você pode encontrar o número na Infobip e selecionar **Cancel number**.

## Considerações {#considerations}

Embora todas as funcionalidades existentes da Braze sejam compatíveis, estes casos de uso não são suportados atualmente.

| Caso de uso | Motivo |
| --- | --- |
| Processamento de mensagens de entrada na Braze e na Infobip | Isso evita cadeias lógicas disparadas por qualquer um dos sistemas, gerando consequentemente threads de mensagens duplicadas e potencialmente contraditórias. |
| Envio de mensagens pela Braze e pela Infobip | Para contas do WhatsApp Business conectadas à Braze, todo o envio é originado pela Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Considerações" }