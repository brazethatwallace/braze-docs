---
nav_title: "Migrar um número"
article_title: "Migrar um número de telefone do WhatsApp"
page_order: 2
description: "Este artigo de referência aborda como migrar seu número de telefone do WhatsApp."
page_type: reference
channel:
  - WhatsApp
---

# Migrar um número de telefone do WhatsApp {#migrate-a-whatsapp-phone-number}

> Migre seu número de telefone do WhatsApp entre contas do WhatsApp Business usando o Embedded Signup da Meta.

## Pré-requisitos {#prerequisites}

Seu número de telefone deve atender aos requisitos da Meta para ser elegível para migração:

- Sua conta Meta Business está verificada.
- Sua conta existente do WhatsApp Business está aprovada.
- Sua conta existente do WhatsApp Business tem um método de pagamento válido em **Payment Settings**.
- Seu número de telefone comercial está com a verificação em duas etapas desativada. Se você é proprietário da sua conta do WhatsApp Business, pode desativar a verificação em duas etapas no número pelo WhatsApp Manager. Caso contrário, você deve solicitar ao seu provedor de soluções que desative para você.

Para informações sobre como migrar seu número de telefone do WhatsApp, consulte a documentação da Meta sobre [Migração de números de telefone entre contas do WhatsApp Business via Embedded Signup](https://developers.facebook.com/docs/whatsapp/business-management-api/guides/migrate-phone-to-different-waba/).

## Migrar entre contas do WhatsApp Business {#migrate-between-whatsapp-business-accounts}

1. No WhatsApp Manager, selecione a conta do WhatsApp Business (WABA) associada ao seu número de telefone e acesse **Account tools** > **Phone numbers**.
2. Selecione **Turn off two-step verification** e conclua as etapas seguintes.<br><br>![WhatsApp Business Manager aberto na página "Phone numbers".]({% image_buster /assets/img/whatsapp/waba_manager.png %}){: style="max-width:80%;"} <br><br> Se você está migrando um número de telefone para um grupo diferente do WhatsApp Business e o Embedded Signup da Meta exige que o nome de exibição seja o mesmo, anote o nome de exibição existente na página **Phone Numbers**. Você vai inserir esse nome durante a próxima etapa.<br><br>![Página Phone Numbers do WhatsApp Business Manager com o nome de exibição "Braze" listado ao lado de um número de telefone.]({% image_buster /assets/img/whatsapp/phone_numbers.png %}){: style="max-width:80%;"}<br><br>
3. Continue o fluxo do Embedded Signup da Meta até a conclusão.

## Migrar de outro provedor de soluções de negócios (BSP) {#migrate-from-another-business-solution-provider}

Se o seu número de telefone do WhatsApp está registrado em outro BSP, você precisa migrar o número para uma conta do WhatsApp Business conectada à Braze antes que a Braze possa enviar mensagens por esse número.

### Antes de migrar {#before-you-migrate}

- Saiba que um número de telefone pode estar ativo em apenas um BSP por vez. A migração transfere o envio para a Braze; seu BSP anterior perde o acesso ao número.
- Revise contratos e cobranças com seu provedor atual. O histórico de mensagens e os modelos podem não ser transferidos automaticamente.
- Desative a verificação em duas etapas no número conforme os requisitos da Meta.
- Se você precisa de números separados para suporte e marketing, consulte [Integrações, dados e relatórios]({{site.baseurl}}/user_guide/channels/whatsapp/faq#integrations-data-and-reporting) no FAQ do WhatsApp.

### Jornadas de migração {#migration-paths}

| Configuração atual | Jornada recomendada |
|---|---|
| Número em outro BSP, migrando totalmente para a Braze | Migrar pelo [Embedded Signup]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup) para uma WABA nova ou existente na Braze |
| Número na integração nativa da Braze, migrando para cobrança pela Infobip | [Conector BYO WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/byo_connector) (somente Infobip) |
| Marketing na Braze, suporte em outra WABA | Manter WABAs e números de telefone separados; consulte o [FAQ do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/faq#integrations-data-and-reporting) e [WhatsApp e sistemas externos]({{site.baseurl}}/user_guide/channels/whatsapp/use_cases/whatsapp_and_external_systems) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Jornadas de migração" }

## Espaços de trabalho de desenvolvimento e produção {#development-and-production-workspaces}

A Braze recomenda contas do WhatsApp Business separadas para desenvolvimento e produção sempre que possível:

- Não vincule seu número de telefone de produção a um sandbox ou espaço de trabalho de desenvolvimento.
- Use uma WABA de teste dedicada e um número de telefone para testes de integração.
- As aprovações de modelos são aplicadas por WABA; aprove os modelos na WABA vinculada ao espaço de trabalho onde você envia.