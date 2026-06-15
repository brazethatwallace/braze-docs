---
nav_title: Regras de envio de mensagens
article_title: Regras de envio de mensagens
page_order: 1
page_type: reference
description: "Esta página aborda como usar regras de envio de mensagens no fluxo de aprovação para Campaigns e Canvas com um grande volume de envio."
---

# Regras de envio de mensagens {#messaging-rules}

> Use regras de envio de mensagens no seu fluxo de aprovação para limitar o número de usuários contatáveis antes que uma aprovação adicional seja necessária — dessa forma, você pode revisar suas Campaigns e Canvas antes de atingir um público maior.

## Pré-requisitos {#prerequisites}

Somente administradores da Braze podem definir regras de envio de mensagens, mas qualquer usuário da Braze pode ser um aprovador de regras de envio de mensagens (incluindo usuários sem permissões gerais de aprovação).

## Como funciona {#how-it-works}

As regras de envio de mensagens se aplicam a um espaço de trabalho e são compostas por um tipo de mensagem e um número máximo de usuários contatáveis.

- **Tipo de mensagem:** Define a qual tipo de mensagem a regra se aplica: Campaign, Canvas ou ambos (Canvas e Campaigns).
- **Máximo de usuários contatáveis:** Determina qual tamanho de público requer uma aprovação adicional.

### Aprovadores separados {#separate-approvers}

Duas regras podem compartilhar o mesmo máximo de usuários para que você possa organizar e separar suas regras por aprovadores. Por exemplo, você cria as duas regras a seguir:

- Regra A para Canvas com um máximo de 100.000 usuários com aprovadores da sua equipe jurídica
- Regra B para Canvas com um máximo de 100.000 usuários com aprovadores da sua equipe de marketing

### Sem sobreposição de usuários contatáveis {#no-overlapping-reachable-users}

Para evitar confusão, não é possível definir regras idênticas com um número sobreposto de usuários para o mesmo tipo de mensagem e aprovadores. Por exemplo, a seguinte regra de envio de mensagens **não pode** ser definida:

- Regra C para Canvas com um máximo de 10.000 usuários
- Regra D para Canvas com um máximo de 1.000.000 de usuários

## Criando uma regra de envio de mensagens {#creating-a-messaging-rule}

### Etapa 1: Adicionar uma regra {#step-1-add-a-rule}

{% alert note %}
Você pode criar até cinco regras de envio de mensagens.
{% endalert %}

1. Acesse **Settings** > **Approval Workflow** > **Messaging Rules**.
2. Selecione **Create rule**.
3. Dê um nome a essa regra (por exemplo, "Todas as inscrições de usuários").
4. Em **Message type**, selecione **Campaign**, **Canvas** ou **Both Canvas and Campaigns** para aplicar a regra de aprovação.
5. Insira um número em **Maximum reachable users**. Para saber mais, consulte [Estatísticas de público]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/#audience-statistics).
6. Selecione **Save**.

![Um exemplo de regra de envio de mensagens "Rule 1" para Campaigns com 100.000 usuários como máximo. Há um usuário que pode aprovar o Canvas e a Campaign para lançamento.]({% image_buster /assets/img/target_population_approval_example.png %}){: style="max-width:90%;"}

### Etapa 2: Determinar lançamento com aprovação (opcional) {#step-2-determine-launching-with-approval-optional}

Selecione **Allow launching with approval**. Em seguida, em **With Approval From**, selecione os aprovadores que têm permissão para aprovar o Canvas ou a Campaign se o máximo for atingido.

Observe os seguintes detalhes sobre o lançamento de mensagens com aprovação:

- Se o máximo for atingido e um aprovador estiver selecionado, o usuário da Braze com a permissão de aprovação pode selecionar **Approved** no menu suspenso de aprovação de **Target Audience**.
- Se o máximo for atingido e um aprovador não estiver selecionado, o Canvas ou a Campaign será impedido de ser lançado.

![A etapa "Summary" do fluxo de trabalho do Canvas mostrando que você precisa de uma aprovação para lançar.]({% image_buster /assets/img/non_approver_banner.png %}){: style="max-width:90%;"}

## Perguntas frequentes {#frequently-asked-questions}

### Preciso reconfigurar minhas permissões para usar regras de envio de mensagens? {#do-i-have-to-reconfigure-my-permissions-to-use-messaging-rules}

Não. Qualquer usuário, independentemente de suas permissões atuais, pode ser selecionado como aprovador de público-alvo.

### Como as regras de envio de mensagens se relacionam com a etapa de público-alvo? {#how-do-messaging-rules-relate-to-the-target-audience-step}

As regras de envio de mensagens não levam em conta detalhes como eventos de gatilho. Por exemplo, uma Campaign pode ter como alvo todos os seus usuários. No entanto, a Campaign é disparada por evento, então o número real de usuários que a recebem é menor.

### Algo mudará automaticamente quando as regras de envio de mensagens forem ativadas? {#will-anything-automatically-change-when-messaging-rules-are-turned-on}

Não. Depois que esse recurso for ativado, você deve inserir manualmente o número máximo de usuários e selecionar aprovadores para usar o recurso.