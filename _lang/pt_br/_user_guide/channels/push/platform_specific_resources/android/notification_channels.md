---
nav_title: "Canais de notificação"
article_title: Canais de notificação por push
page_order: 4
page_type: reference
description: "Este artigo de referência aborda tópicos sobre canais de notificação por push para Android, como a transição para o Android O, como adicionar um canal à Braze, configurar um canal de fallback e mais."
platform: Android
channel:
  - Push
---

# Canais de notificação {#notification-channels}

> Os [canais de notificação](https://www.braze.com/blog/android-o-push-notifications-channels/) são uma forma de organizar notificações por push que foram adicionadas com o Android O. A partir do O, todas as notificações por push devem ter um canal de notificação que indique o tipo de mensagem (por exemplo, "notificações de chat" ou "notificações de seguidores"). Seus usuários podem então controlar aspectos de suas notificações (por exemplo, adiar, configurações de som/vibração ou desativar, etc.) com base em canais individuais.

Os canais de notificação só podem ser criados no código do seu app e não podem ser criados programaticamente no dashboard da Braze. Recomendamos que sua equipe de engenharia trabalhe com seus profissionais de marketing para garantir que os canais de notificação desejados sejam adicionados corretamente ao dashboard.

A partir do nível de API 26 (Android O), as notificações por push exigem um canal válido para serem exibidas. Se o seu app tem como alvo o Android O ou posterior, você deve usar a versão 2.1.0 ou posterior do SDK da Braze. Sua equipe de desenvolvimento deve definir os canais que você deseja usar, bem como as configurações de notificação sugeridas (por exemplo, importância, som, luzes) para cada canal no código do seu app. Para mais informações, consulte a [documentação para desenvolvedores do Android](https://developer.android.com/preview/features/notification-channels.html) e a [documentação para desenvolvedores da Braze]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android).

{% alert note %}
O Android suporta localização para nomes de canais, então no código do seu app, você pode associar um ID de canal a múltiplas traduções de um nome de canal.
{% endalert %}

Depois que esses canais forem criados, seus engenheiros precisarão repassar os IDs de canal associados para sua equipe de marketing. Sua equipe deve inserir os nomes e IDs dos canais no dashboard da Braze para uso em suas Campaigns e Canvas.

Para adicionar um canal ao dashboard da Braze, acesse o criador de push para Android, selecione o campo de canais de notificação e então selecione **Gerenciar canais**.
{% alert important %}
Somente usuários com permissões que incluem "gerenciar apps" poderão gerenciar canais.
{% endalert %}

## Canal padrão do SDK {#sdk-default-channel}

O Android requer um canal válido para exibir notificações por push no nível de API 26 (Android O) ou posterior. O SDK para Android da Braze 2.1.0 inclui um canal padrão chamado "General", que será criado e usado caso você não especifique canais adicionais no dashboard ou tente enviar para um canal inválido. Você pode renomear esse rótulo no SDK e fornecer uma descrição do canal. Recomendamos que considere isso para proporcionar uma melhor experiência do usuário.

Depois que um canal for adicionado ao seu app, você pode optar por removê-lo. No entanto, os consumidores sempre poderão ver o número de canais que você [removeu].[3] O dashboard da Braze não inclui suporte para a criação programática de canais. Os canais devem ser criados e definidos no código do seu app para proporcionar uma experiência consistente.

Novamente, recomendamos que você se coordene com sua equipe de engenharia para garantir uma transição tranquila para o direcionamento ao Android O.

## Canal de fallback do dashboard {#dashboard-fallback-channel}

A Braze permite que você especifique um canal de fallback do dashboard. O objetivo do canal de fallback do dashboard é fornecer um ID de canal para mensagens push legadas que não possuem uma seleção explícita de canal. Definimos uma seleção de canal como a escolha de um canal no nosso criador de push para Android.

As mensagens que não tiverem um canal selecionado serão enviadas com o ID do canal de fallback do dashboard. Quando você altera o canal de fallback do dashboard, qualquer mensagem que não tenha um canal explicitamente selecionado será enviada com o ID do novo canal de fallback.

Veja um exemplo do comportamento esperado do canal de fallback do dashboard:

Seu canal de fallback do dashboard se chama "Marketing" e você tem 10 mensagens push para Android para as quais nunca selecionou um canal. Essas campanhas estão sendo enviadas pelo canal "Marketing" porque o canal "Marketing" é o canal de fallback do dashboard.

Além disso, você tem 15 mensagens que selecionou para enviar pelo canal "Social Notifications" e cinco mensagens que selecionou para enviar pelo canal "Marketing".

Então, você decide alterar o canal padrão do dashboard de "Marketing" para "Updates".

Nessa situação, todas as 10 campanhas sem seleção de canal que anteriormente eram enviadas pelo canal "Marketing" agora serão enviadas pelo canal "Updates", pois essas mensagens são enviadas pelo canal de fallback. As 15 mensagens que eram enviadas pelo canal "Social Notifications" continuarão sendo enviadas pelo canal "Social Notifications". As cinco mensagens que eram enviadas pelo canal "Marketing" continuarão sendo enviadas pelo canal "Marketing".

Caso um ID de canal inválido seja fornecido à Braze (por exemplo, se você fornecer um ID de canal que seus desenvolvedores não criaram no SDK), a notificação será entregue pelo canal padrão do SDK. Por isso, recomendamos fortemente que você teste seus canais de notificação no dashboard da Braze durante o desenvolvimento.

Para entender melhor o comportamento esperado dos canais, consulte a tabela a seguir:

| Cenário | Resultado |
| ---|-------------
| **Empresa ABC** atualiza para um SDK que suporta Android O<br>**Empresa ABC** não adiciona nenhum canal ao dashboard da Braze<br>**Empresa ABC** não renomeia o canal padrão do SDK | As notificações por push enviadas para dispositivos Android O criarão um canal chamado "General" e as notificações serão enviadas pelo canal "General"
| **Empresa XYZ** atualiza para um SDK que suporta Android O<br>**Empresa XYZ** não adiciona nenhum canal ao dashboard da Braze<br>**Empresa XYZ** renomeia o canal padrão do SDK para "Marketing" | As notificações por push enviadas para dispositivos Android O criarão um canal chamado "Marketing" e as notificações serão enviadas pelo canal "Marketing"
| **Empresa LMN** atualiza para um SDK que suporta Android O<br>**Empresa LMN** define dois canais no código da aplicação, "Promotions" e "Order Updates"<br>**Empresa LMN** adiciona os IDs de canal para "Promotions" e "Order Updates" ao dashboard da Braze<br>**Empresa LMN** designa "Promotions" como o canal de fallback do dashboard<br>**Empresa LMN** renomeia o canal padrão do SDK para "Marketing" | As notificações por push enviadas para dispositivos Android O não criarão um canal<br><br>A menos que o profissional de marketing especifique explicitamente que as notificações devem ser enviadas pelo canal "Order Updates" ou "Marketing", todas as notificações criadas antes dos canais serem adicionados ao dashboard serão enviadas pelo canal "Promotions"<br><br>O canal padrão do SDK, "Marketing", só será criado e utilizado se a empresa tentar enviar uma notificação por um ID de canal inválido ou se for explicitamente selecionado
| **Empresa HIJ** atualiza para Android O, mas não atualiza para o SDK Android da Braze versão 2.1.0 ou posterior | As notificações enviadas para usuários com Android O ou posterior não aparecem |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canal de fallback do dashboard" }

## Adicionando canais ao dashboard da Braze {#adding-channels-to-the-braze-dashboard}

1. Abra ou crie qualquer Campaign ou Canvas que inclua um push Android.
2. Navegue até o criador de mensagem de push Android.
3. Selecione **Manage Notification Channels**. Todos os canais adicionados aqui estarão disponíveis globalmente para todos os Campaigns e Canvas. Você precisa ter [permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) de "Manage Apps" no seu espaço de trabalho para gerenciar canais.

Quando você aplica um canal de notificação a um Campaign ou etapa do Canvas específico, a contagem de **Usuários contatáveis** (localizada na etapa de público-alvo) para push Android não parecerá mudar. No entanto, apenas os usuários inscritos no canal de notificação selecionado verão a mensagem, e a análise de dados do Campaign (como cliques) será medida com base nesse público.

![Criador de push Android com a opção Manage Notification Channels e uma lista de canais configurados.]({% image_buster /assets/img_archive/push_notification_channels.png %})

{:start="4"}
4. Selecione **Add Notification Channel**.
5. Insira o nome e o ID do canal de notificação que você deseja adicionar.<br><br>![Caixa de diálogo Add Notification Channel com campos para nome do canal e ID do canal.]({% image_buster /assets/img_archive/push_notifications_channels_manage.png %})<br><br>
6. Repita as etapas 4 e 5 para cada canal de notificação que você deseja adicionar.
7. Selecione **Save** para salvar suas alterações.

## Especificando o canal de fallback {#specifying-your-fallback-channel}

O canal de fallback é o canal que a Braze tentará usar para enviar sua mensagem Android caso você não tenha selecionado um canal para a mensagem. As únicas Campaigns e Canvas que terão mensagens Android sem uma seleção de canal são Campaigns e Canvas criados antes de sua equipe adicionar canais ao dashboard da Braze. Se você alterar o canal de fallback, a mudança será aplicada globalmente a todas as Campaigns e Canvas sem uma seleção explícita de canal.

1. Abra qualquer Campaign ou Canvas existente.
2. Navegue até o criador de push Android.
3. Selecione **Gerenciar canais de notificação** após expandir as opções de canal de notificação.
4. Adicione o canal ao dashboard (caso ainda não tenha sido adicionado).
5. Selecione o botão de opção ao lado do canal que você deseja designar como canal de fallback.
6. Salve suas alterações. Suas alterações serão aplicadas globalmente.

## Adicionando canais às suas mensagens push do Android {#adding-channels-to-your-android-push-messages}

1. Acesse o criador de push do Android em qualquer Campaign ou Canvas.
2. Selecione o canal que deseja usar no menu suspenso. Se você não tiver um menu suspenso e sim a visualização a seguir, será necessário adicionar canais antes de selecioná-los para Campaigns.

![Criador de canais de notificações por push.]({% image_buster /assets/img_archive/push_notifications_channels_composer.png %})

[3]: https://developer.android.com/preview/features/notification-channels.html#DeletingChannels