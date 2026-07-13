---
nav_title: Grupos de inscrições
article_title: Grupos de inscrições
page_order: 1
description: "Este artigo aborda os grupos de inscrições de mensagens LINE."
page_type: reference
channel:
 - LINE
alias: /line/subscription_groups/
---

# Grupos de inscrições LINE {#line-subscription-groups}

> Existem dois estados de inscrição para usuários LINE: inscrito e cancelado. O LINE pode ter até 100 grupos de inscrições por espaço de trabalho, com cada grupo de inscrições conectado ao seu próprio canal LINE.

| Estado | Definição |
| --- | --- |
| Inscrito | O usuário seguiu o canal LINE de dentro do app LINE. Os usuários são automaticamente inscritos quando seguem o canal após você ter concluído as etapas de integração. |
| Cancelou inscrição | O usuário não seguiu o canal LINE de dentro do app LINE, ou o usuário deixou de seguir explicitamente o canal LINE. <br><br> Usuários que cancelarem a inscrição de um grupo de inscrições LINE não receberão mais nenhuma mensagem LINE dos canais de envio que pertencem ao grupo de inscrições. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINE subscription groups" }

## Definindo o grupo de inscrições LINE de um usuário {#setting-a-users-line-subscription-group}

O LINE hospeda o status de inscrição dos usuários. A Braze processa os eventos de seguir e deixar de seguir que atualizam o status de inscrição.