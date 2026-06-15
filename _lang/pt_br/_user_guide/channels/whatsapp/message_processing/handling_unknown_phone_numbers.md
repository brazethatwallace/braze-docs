---
nav_title: "Lidar com números de telefone desconhecidos"
article_title: "Lidar com números de telefone desconhecidos"
description: "Este artigo de referência aborda como a Braze lida com números de telefone desconhecidos para usuários do WhatsApp."
page_type: reference
channel:
  - WhatsApp
page_order: 50
---

# Lidar com números de telefone desconhecidos {#handle-unknown-phone-numbers}

> Você pode perceber que, depois de colocar o WhatsApp em funcionamento com a Braze, recebe mensagens de usuários desconhecidos. As etapas a seguir descrevem como um usuário e número não identificados são processados.

## Fluxo de opt-in/out e palavras-chave personalizadas para números desconhecidos {#opt-inout-and-custom-keyword-workflow-for-unknown-numbers}

A Braze primeiro tentará encontrar um usuário com um número correspondente. Se nenhum for encontrado, a Braze automaticamente lida com um número desconhecido de uma das duas formas:

1. **Se uma palavra-gatilho com um [Canvas de opt-in]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs/) estiver configurada:**
- A Braze cria um perfil anônimo
- Atribuímos um alias de usuário ao perfil com os seguintes detalhes:
  - Um `alias_name` com o valor sendo o número de telefone fornecido pelo usuário
  - Um `alias_label` com o valor `phone`
- Nosso sistema define o atributo de telefone
- O usuário é inscrito no grupo de inscrições correspondente com base na lógica configurada dentro do Canvas<br><br>
2. **Se nenhum Canvas de opt-in estiver configurado:**
- A Braze cria um perfil anônimo
- Atribuímos um alias de usuário ao perfil com os seguintes detalhes:
  - Um `alias_name` com o valor sendo o número de telefone fornecido pelo usuário
  - Um `alias_label` com o valor `phone`
- Nosso sistema define o atributo de telefone
- O status de inscrição do usuário será definido como padrão `unsubscribed` para todos os grupos de inscrições do WhatsApp<br><br>