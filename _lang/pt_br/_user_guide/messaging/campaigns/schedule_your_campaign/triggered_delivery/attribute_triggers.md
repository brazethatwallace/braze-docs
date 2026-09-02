---
nav_title: Gatilhos de atributo
article_title: Gatilhos de atributo
page_order: 1
alias: /attribute_triggers/
page_type: reference
description: "Este artigo de referência oferece uma visão geral dos gatilhos de atributo e como você pode usá-los para enviar mensagens baseadas em ação aos usuários."
tool:
  - Campaigns

---

# Gatilhos de atributo {#attribute-triggers}

> Os gatilhos de atributo permitem enviar mensagens baseadas em ação quando o estado de inscrição ou os valores de atributos personalizados de um usuário mudam.

Os gatilhos de atributo estão disponíveis para os seguintes cenários:

- Atualizações do estado de inscrição.
- Valores de atributos personalizados do tipo booleano, Número, string ou data/hora mudam para qualquer valor.
- Valores de atributos personalizados do tipo booleano, Número ou string mudam para um valor específico.

{% alert important %}
No dashboard, atributos de números inteiros usam o tipo **Number**, e datas ou timestamps usam o tipo **Time** (eles não são rotulados como "integer" ou "date" na interface). Atributos do tipo **Time** suportam **Change Custom Attribute Value** apenas com a opção **any new value** — eles não suportam a opção **specific value**.
{% endalert %}

Para começar a usar gatilhos de atributo, crie uma Campaign ou um componente do Canvas e selecione **Entrega baseada em ação** como método de entrega. Em seguida, selecione o gatilho de atributo que deseja usar.

![Seção "Entrega baseada em ação" com um menu suspenso para selecionar um gatilho.]({% image_buster /assets/img_archive/trigger_attribute.png %})

## Atualizar status de inscrição {#update-subscription-status}

Use o gatilho `Update Subscription Status` para direcionar usuários quando o status de inscrição deles for atualizado.

Por exemplo, você pode direcionar usuários quando o status de inscrição de e-mail ou push mudar para opted in e agradecê-los por terem optado por receber comunicações. Você também pode enviar um webhook para seus sistemas sempre que um usuário cancelar a inscrição de e-mail, para que seus sistemas internos estejam atualizados com as informações mais recentes do status de inscrição.

{% alert important %}
Esse gatilho não se aplica quando um novo usuário é criado com o estado global de e-mail padrão `subscribed` e há uma solicitação subsequente para atualizar o estado para `subscribed`, já que o status de inscrição não foi alterado.
{% endalert %}

## Atualizar status do grupo de inscrições {#update-subscription-group-status}

Use o gatilho `Update Subscription Group Status` para direcionar usuários quando o status do grupo de inscrições de e-mail, SMS ou WhatsApp for atualizado.

Por exemplo, você pode direcionar usuários com uma mensagem SMS de boas-vindas quando eles optarem por participar do seu programa. Você também pode especificar a origem da atualização para ter um controle mais preciso sobre quando uma mensagem é disparada.

As origens de atualização disponíveis variam por canal:
- Etapa de Atualização de usuário do Canvas
- Importação de CSV
- List-Unsubscribe
- Central de Preferências
- REST or transferir estado representacional API or interface de programação do aplicativo (API)
- SDK or kit de desenvolvimento de software
- Shopify (e-mail, SMS)
- Mensagem de entrada (SMS)

Por exemplo, você pode querer enviar seu SMS de boas-vindas apenas quando a atualização vier da REST or transferir estado representacional API or interface de programação do aplicativo (API) e não de uma mensagem de entrada, já que a Braze já responde automaticamente a determinadas mensagens SMS de entrada.

## Alterar valor de atributo personalizado {#change-custom-attribute-value}

Para alteração de atributo, o gatilho é avaliado primeiro e depois os critérios de público. Isso difere do comportamento padrão, em que os critérios de público são avaliados primeiro e depois o gatilho. Para evitar uma condição de corrida, certifique-se de que o atributo usado como gatilho não seja o mesmo atributo usado para qualificar seu público.

### Opção de qualquer novo valor {#any-new-value-option}

Use o gatilho `Change Custom Attribute Value` com a opção `any new value` para direcionar usuários quando um valor booleano, Número, string ou do tipo data/hora mudar para qualquer novo valor.

Por exemplo, direcione usuários quando o número de pontos de recompensa mudar para informá-los quantos pontos eles têm agora. Neste exemplo, digamos que um usuário tem 85 pontos de recompensa e você configurou uma Campaign para ser disparada quando o atributo de pontos de recompensa mudar para qualquer novo valor. Se o valor do atributo de pontos de recompensa desse usuário mudar para qualquer novo valor (como 83, 84, 86 e assim por diante), a Campaign será disparada.

Considere o próximo exemplo de caso de uso com uma notificação de atualização de nível. Você pode querer alertar os usuários se o nível de recompensas deles mudar. Para isso, configure uma Campaign que seja disparada por `Change Custom Attribute Value` e defina-a para ser acionada quando o atributo personalizado de nível de recompensas mudar para qualquer novo valor.

{% alert important %}
Os gatilhos de atributo não estão disponíveis atualmente para atributos do tipo array.
{% endalert %}

![Um gatilho "Change Custom Attribute Value" para "AA_current_rewards_tier" mudando para qualquer valor.]({% image_buster /assets/img_archive/any_value.png %})

Você também pode usar Liquid para personalizar o corpo da mensagem com o novo nível de recompensas do cliente e fornecer mais informações sobre a mudança.

{% raw %}
```liquid
Your rewards tier was just changed to {{custom_attribute.${AA_current_rewards_tier}}}
```
{% endraw %}

### Valor específico {#specific-value}

Use o gatilho `Change Custom Attribute Value` com a opção `specific value` para direcionar usuários quando um atributo personalizado do tipo booleano, Número ou string mudar para um valor específico.

Por exemplo, direcione usuários quando o nível de recompensas deles mudar para o melhor nível. Neste exemplo, digamos que o melhor nível de recompensas é Super VIP. Você pode configurar uma Campaign para ser disparada quando o atributo personalizado de nível de recompensas de um usuário mudar para `Super VIP`, para que você possa parabenizá-lo por se tornar um Super VIP.

![Um gatilho "Change Custom Attribute Value" para "AA_current_rewards_tier" mudando para o valor específico "super vip".]({% image_buster /assets/img_archive/super_vip.png %})

{% alert important %}
- Os gatilhos de atributo para valores específicos de atributos personalizados não estão disponíveis para atributos personalizados do tipo array e data/hora.
- O gatilho de alteração de valores de atributos personalizados não é disparado quando o valor do atributo personalizado é atualizado para null.
- O gatilho de alteração de valores de atributos personalizados só será disparado quando o valor de um atributo personalizado mudar. Se o valor atual de um atributo personalizado for reenviado para a Braze (por exemplo, o valor do atributo de cor favorita é vermelho e você reenvia o valor vermelho para a Braze), o gatilho de alteração de valores de atributos personalizados não será acionado.
- O gatilho de alteração de valores de atributos personalizados também se aplica a novos usuários criados.
{% endalert %}