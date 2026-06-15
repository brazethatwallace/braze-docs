---
nav_title: Transferir entre espaços de trabalho
article_title: Transferir números de telefone e grupos de inscrições entre espaços de trabalho
page_order: 3
description: "Este artigo de referência aborda como transferir seu número de telefone do WhatsApp e grupos de inscrições entre espaços de trabalho."
page_type: reference
channel:
  - WhatsApp
---

# Transferir números de telefone do WhatsApp e grupos de inscrições entre espaços de trabalho {#transfer-whatsapp-phone-numbers-and-subscription-groups-between-workspaces}

> Esta página aborda como você pode mover um número de telefone de uma Conta WhatsApp Business (WABA) e seu grupo de inscrições associado de um espaço de trabalho para outro na Braze. Esse processo simplifica sua experiência ao usar o WhatsApp com a Braze e reduz a necessidade de ajuda de engenharia.

## Pré-requisitos {#prerequisites}

- Confirme que você tem a [permissão de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#list-of-permissions) "Manage Subscription Groups" em ambos os espaços de trabalho, o original e o novo.
- A WABA não pode cruzar múltiplos [clusters da Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/). É improvável que isso aconteça se você estiver trabalhando dentro de uma mesma empresa.

## Transferindo um número de telefone e grupo de inscrições {#transferring-a-phone-number-and-subscription-group}

### Etapa 1: Arquivar o grupo de inscrições {#step-1-archive-the-subscription-group}

Para arquivar um grupo de inscrições do WhatsApp, siga estas etapas:

1. Acesse o espaço de trabalho onde o grupo de inscrições existe atualmente.
2. Acesse **Audience** > **Gerenciamento de grupos de inscrições** e encontre o grupo de inscrições associado ao número de telefone do WhatsApp que você deseja mover.
3. Passe o cursor sobre o status do grupo de inscrições e selecione <i class="fa-solid fa-box-archive"></i> **Arquivar**, o que marcará o grupo de inscrições como inativo, mas não o excluirá.

![Botão "Arquivar" aparecendo ao passar o cursor sobre o status "Ativo" de um grupo de inscrições.]({% image_buster /assets/img/whatsapp/archive_subscription_group.png %}){: style="max-width:70%;"}

### Etapa 2: Integrar o número de telefone do WhatsApp no novo espaço de trabalho {#step-2-integrate-the-whatsapp-phone-number-into-the-new-workspace}

1. Acesse o espaço de trabalho para onde você deseja mover o número de telefone do WhatsApp.
2. Acesse **Integrações de parceiros** > **Parceiros de tecnologia** > **WhatsApp** e role até a seção **WhatsApp Messaging Integration**.
3. Selecione a opção **Criar novo grupo de inscrições e número de telefone**.
4. Inicie o processo de integração, durante o qual você poderá selecionar o número de telefone do grupo de inscrições arquivado.

### Etapa 3: Verificar a integração {#step-3-verify-the-integration}

1. Após concluir a integração, confirme que o número de telefone do WhatsApp agora está associado ao grupo de inscrições no novo espaço de trabalho.
2. Teste para confirmar que as mensagens podem ser enviadas e recebidas por meio desse número de telefone do WhatsApp.

## Considerações {#considerations}

- Se você precisar transferir o número de telefone do WhatsApp de volta para o espaço de trabalho original, repita as etapas. Arquive o grupo de inscrições no espaço de trabalho de destino e, em seguida, integre-o no espaço de trabalho original.
- Você não precisa remover o número de telefone do WhatsApp do seu Meta Business Manager durante a transferência.