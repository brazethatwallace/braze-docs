---
nav_title: Lidar com números de telefone desconhecidos
article_title: Lidar com números de telefone desconhecidos
page_order: 3
description: "Este artigo de referência aborda como a Braze processa números de telefone desconhecidos de novos usuários."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS

---

# Lidar com números de telefone desconhecidos - novos usuários {#handle-unknown-phone-numbers-new-users}

> Você pode perceber que, depois de colocar SMS, MMS e RCS em funcionamento com a Braze, recebe mensagens de usuários desconhecidos. As etapas a seguir descrevem como um usuário e número não identificados são processados.

## Fluxo de trabalho de opt-in/descadastramento e palavras-chave personalizadas para números desconhecidos {#opt-inout-and-custom-keyword-workflow-for-unknown-numbers}

A Braze lida automaticamente com um número desconhecido de uma das três formas a seguir:

1. Se uma palavra-chave de opt-in for enviada por mensagem de texto:
  * A Braze cria um perfil anônimo
  * Nosso sistema define o atributo de telefone
  * Inscreve o usuário no grupo de inscrições correspondente com base na palavra-chave de opt-in recebida pela Braze.<br><br>
2. Se uma palavra-chave de descadastramento for enviada por mensagem de texto:
  * A Braze cria um perfil anônimo
  * Nosso sistema define o atributo de telefone
  * Cancela a inscrição do usuário no grupo de inscrições correspondente com base na palavra-chave de descadastramento recebida pela Braze.<br><br>
3. Se qualquer outra palavra-chave personalizada for enviada por mensagem de texto:
  * A Braze ignora a mensagem de texto e não faz nada.