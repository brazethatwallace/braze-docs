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

## Migrando seu número de telefone do WhatsApp {#migrating-your-whatsapp-phone-number}

1. No WhatsApp Manager, selecione a conta do WhatsApp Business (WABA) associada ao seu número de telefone e acesse **Account tools** > **Phone numbers**.
2. Selecione **Turn off two-step verification** e conclua as etapas seguintes.<br><br>![WhatsApp Business Manager aberto na página "Phone numbers".]({% image_buster /assets/img/whatsapp/waba_manager.png %}){: style="max-width:80%;"} <br><br> Se você está migrando um número de telefone para um grupo diferente do WhatsApp Business e o Embedded Signup da Meta exige que o nome de exibição seja o mesmo, anote o nome de exibição existente na página **Phone Numbers**. Você vai inserir esse nome durante a próxima etapa.<br><br>![Página Phone Numbers do WhatsApp Business Manager com o nome de exibição "Braze" listado ao lado de um número de telefone.]({% image_buster /assets/img/whatsapp/phone_numbers.png %}){: style="max-width:80%;"}<br><br>
3. Continue o fluxo do Embedded Signup da Meta até a conclusão.