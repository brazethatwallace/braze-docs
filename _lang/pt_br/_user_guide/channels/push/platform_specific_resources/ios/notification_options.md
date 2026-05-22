---
nav_title: "Opções de notificação"
article_title: Opções de notificação do iOS
page_order: 2
page_layout: reference
description: "Este artigo de referência aborda as opções de notificação do iOS, como alertas críticos, notificações silenciosas, notificações por push provisórias e mais."

platform: iOS
channel:
  - Push
---

# Opções de notificação {#notification-options}

> Com o lançamento do iOS 12 da Apple, a Braze oferece suporte a vários de seus recursos, incluindo [Grupos de notificação](#notification-groups), [Notificações silenciosas/Autorização provisória](#provisional-push-authentication--quiet-notifications) e [Alertas críticos](#critical-alerts).

## Grupos de notificação {#notification-groups}

Se você deseja categorizar suas mensagens e agrupá-las na bandeja de notificações do usuário, pode utilizar o recurso de grupos de notificação do iOS por meio da Braze.

Crie sua Campaign de push para iOS e acesse a guia **Settings**. Em seguida, abra o menu suspenso **Notification group**.

![A guia "Settings" com um menu suspenso "Notification group" que selecionou o valor "Coupons".]({% image_buster /assets/img_archive/notification_group_dropdown.png %}){: style="max-width:50%;" }

Selecione seus grupos de notificação no menu suspenso. Se as configurações do grupo de notificação apresentarem problemas ou se você selecionar **None** no menu suspenso, a mensagem será enviada automaticamente de forma normal para todos os usuários definidos no espaço de trabalho.

Se você não tiver nenhum grupo de notificação listado aqui, pode adicionar um usando o iOS Thread ID. Você precisará de um iOS Thread ID para cada grupo de notificação que deseja adicionar. Em seguida, adicione-o aos seus grupos de notificação clicando em **Manage Notification Groups** no menu suspenso e preenchendo os campos obrigatórios na janela **Manage iOS Push Notification Groups** que aparece.

![Janela para gerenciar grupos de notificação por push do iOS.]({% image_buster /assets/img_archive/managenotgroups.png %}){: style="max-width:70%;" }

Crie sua Campaign de push para iOS e procure no topo do criador. Lá, você verá um menu suspenso chamado **Notification Groups**.

### Argumentos de resumo {#summary-arguments}

Além de agrupar notificações por Thread IDs, a Apple permite que você edite os resumos que aparecem quando as notificações são agrupadas. Os usuários da Braze podem especificar a categoria de resumo, a contagem de resumo e o argumento de resumo ao compor uma Campaign de push usando nossa ferramenta.

{% alert tip %}
Observe que a forma como as notificações com o mesmo Thread ID são agrupadas na bandeja de notificações é controlada pelo sistema operacional. O iOS pode optar por exibir notificações com o mesmo Thread ID separadamente ou em grupos, dependendo do que considerar ideal.
{% endalert %}

Marque a caixa **Alert Options** no **Push Composer**.

Em seguida, selecione `summary-arg` e `summary-arg-count` como chaves e insira esses valores na coluna correspondente. Se você não definir um valor para `summary-arg`, o padrão será 1.

### Categorias de resumo {#summary-categories}

As categorias de resumo permitem que você personalize todo o resumo que aparece quando as notificações são agrupadas. Você pode criar e aplicar várias categorias.

Para usar uma categoria em sua mensagem, trabalhe com seus desenvolvedores para implementar usando o seguinte exemplo:

```
UNNotificationCategory *newsCategory = [UNNotificationCategory categoryWithIdentifier:@"news"
                                                      actions:@[likeAction, unlikeAction]
                                                      intentIdentifiers:@[]
                                                      hiddenPreviewsBodyPlaceholder:@""
                                                      categorySummaryFormat:@"%u more news articles from %@"
                                                       Options:0];
```

{% alert important %}
Isso não exigirá uma atualização do SDK.
{% endalert %}

{% alert tip %}
Observe que `%u` e `%@` são strings de formatação para a contagem de resumo e o argumento de resumo, respectivamente. Quando o resumo é exibido, esses espaços reservados serão substituídos pelos valores de `summary-count` e `summary-arg`.
{% endalert %}

Depois que isso estiver configurado no seu app, use a categoria de resumo marcando a caixa **Notification Buttons** e selecionando **Enter Pre-registered iOS Category**.

Em seguida, insira o identificador da categoria de resumo que você definiu no seu app.

### Autenticação provisória de push e notificações silenciosas {#provisional-push}

A Apple permite que as marcas enviem notificações por push silenciosas para as centrais de notificações dos usuários antes que eles oficialmente e explicitamente façam opt-in, dando a você a chance de demonstrar o valor de suas mensagens antecipadamente. Tudo o que você precisa fazer é [configurar notificações por push provisórias](#set-up-provisional-push-notifications) no seu app, e qualquer usuário que tenha um token de push provisório receberá suas mensagens.

Diferentemente de um token de push tradicional do iOS, um token de push provisório funciona como um "passe de teste" que permite que as marcas alcancem novos usuários antes que eles tenham visto e clicado no prompt nativo de opt-in de push da Apple. Com esse recurso, sua notificação por push será entregue diretamente na bandeja de notificações do novo usuário com a opção de "Manter" ou "Desativar" notificações futuras. Em vez de experimentar uma jornada de "opt-in", os usuários experimentarão algo mais parecido com uma jornada de "descadastramento".

{% alert tip %}
A autorização provisória tem o potencial de aumentar drasticamente sua taxa de opt-in, mas apenas se os usuários perceberem valor em suas mensagens. Certifique-se de usar nossos recursos de [segmentação de usuários]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/), [direcionamento por local]({{site.baseurl}}/user_guide/audience/locations_and_geofences/) e [personalização]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/) para garantir que os usuários apropriados recebam essas notificações de "teste" no momento certo. Então, você pode incentivar os usuários a fazer opt-in completo nas suas notificações por push, sabendo que elas agregam valor à experiência dos usuários com o seu app.
{% endalert %}

Qualquer que seja a opção escolhida pelo usuário, o token ou [status de inscrição]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states/) apropriado será adicionado às [Configurações de contato]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/#engagement-tab) na guia **Engajamento** do perfil de usuário.

![Configurações de contato com um status de inscrição de push.]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

Você poderá direcionar seus usuários com base em se eles estão provisoriamente autorizados ou não usando nossos [filtros de segmentação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/).

![Painel de detalhes do Segment com o filtro de exemplo "Provisionally Authorized on iOS Stopwatch (iOS) is true" para direcionar usuários.]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
Se os usuários optarem por "Desativar" o push provisório de você, eles não verão mais nenhuma mensagem de push provisória sua. Seja cuidadoso com o conteúdo e a cadência das mensagens enviadas usando essa funcionalidade!
{% endalert %}

{% alert important %}
Se você usar prompts de push adicionais ou [primers de push no app](https://www.braze.com/resources/glossary/priming-for-push/) (uma mensagem no app que incentiva os usuários a fazer opt-in para notificações por push), entre em contato com seu representante da Braze para orientação adicional.
{% endalert %}

#### Configurar notificações por push provisórias {#set-up-provisional-push-notifications}

A Braze permite que você se registre para autenticação provisória atualizando seu código no trecho de registro de token dentro da implementação do SDK da Braze para iOS usando os seguintes trechos como exemplo (envie-os para seus desenvolvedores ou certifique-se de que eles [implementem a autenticação provisória de push durante o processo de integração]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10)).

{% alert warning %}
A implementação da autenticação provisória de push suporta apenas iOS 12+ e apresentará erro se o alvo de implantação for anterior a isso. Você pode saber mais sobre isso [em nossa documentação de implementação mais detalhada aqui]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10).
{% endalert %}

{% tabs local %}
  {% tab Swift %}
**Swift**

```
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
```
  {% endtab %}
  {% tab Objective-C %}

**Objective-C**

```
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
    options = options | UNAuthorizationOptionProvisional;
}
```
  {% endtab %}
{% endtabs %}

### Nível de interrupção (iOS 15+) {#interruption-level}

Com o novo Modo de Foco do iOS 15, os usuários têm mais controle sobre quando as notificações de apps podem "interrompê-los" com um som ou vibração.

![Página de configurações de notificação do iOS mostrando notificações ativadas para entrega imediata e com notificações sensíveis ao tempo ativadas.]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="max-width:40%"}

Os apps agora podem especificar qual nível de interrupção uma notificação deve incluir, com base em sua urgência.

Para alterar o nível de interrupção de uma notificação por push do iOS, selecione a guia **Settings** e escolha o nível desejado no menu suspenso **Interruption Level**.

![Menu suspenso para selecionar o nível de interrupção.]({% image_buster /assets/img/ios/interruption_level.png %}){: style="max-width:50%"}

Esse recurso não tem requisitos mínimos de versão do SDK, mas é aplicado apenas para dispositivos com iOS 15+.

Tenha em mente que os usuários são, em última instância, os que controlam seu foco, e mesmo que uma notificação sensível ao tempo seja entregue, eles podem especificar quais apps não têm permissão para interromper seu foco.

Consulte a tabela a seguir para os níveis de interrupção e suas descrições.

| Nível de interrupção | Descrição | Quando usar | Interrompe o Modo de Foco |
|--|--|--|--|
| [Passive](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive) | Envia uma notificação sem som, vibração ou ativação da tela. | Notificações que não exigem atenção imediata. | Não |
| [Active](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active) (padrão) | Só emitirá som, vibração e ativará a tela se o usuário não estiver no Modo de Foco. | Notificações que exigem atenção imediata, a menos que o usuário tenha o Modo de Foco ativado. | Não |
| [Time Sensitive](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive) | Emitirá som, vibrará e ativará a tela mesmo durante o Modo de Foco. Isso requer que a capacidade **Time Sensitive Notifications** seja adicionada ao seu app no Xcode. | Notificações oportunas que devem interromper os usuários independentemente do Modo de Foco, como uma notificação de carona ou entrega. | Sim |
| [Critical](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical) | Emitirá som, vibrará e ativará a tela mesmo se o botão **Não Perturbe** do telefone estiver ativado. Isso [requer aprovação explícita da Apple](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/). | Emergências como alertas de clima severo ou segurança. | Sim |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Interruption level (iOS 15+) #interruption-level" }

### Pontuação de relevância (iOS 15+) {#relevance-score}

![Um resumo de notificações do iOS intitulado "Your Evening Summary" com três notificações.]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

O iOS 15 também introduziu uma nova forma para os usuários agendarem opcionalmente um agrupamento resumido de várias notificações em horários designados ao longo do dia. Isso é feito para evitar interrupções constantes ao longo do dia para notificações que não precisam de atenção imediata.

Os apps podem especificar quais notificações por push são mais relevantes definindo uma **Relevance Score**. A Apple usará essa pontuação para determinar quais notificações devem ser destacadas no resumo de notificações agendado, enquanto outras ficarão disponíveis quando os usuários clicarem no resumo.

Todas as notificações ainda estarão acessíveis na central de notificações do usuário.

Para definir a pontuação de relevância de uma notificação do iOS, insira um valor entre `0.0` e `1.0` na guia **Settings**. Por exemplo, a mensagem mais importante deve ser enviada com `1.0`, enquanto uma mensagem de importância média pode ser enviada com `0.5`.

![Pontuação de relevância de "0.5".]({% image_buster /assets/img/ios/relevance-score.png %}){: style="max-width:80%;"}

Esse recurso não tem requisitos mínimos de versão do SDK, mas é aplicado apenas para dispositivos com iOS 15+.

Para saber mais sobre os comprimentos máximos de mensagem para diferentes tipos de mensagem, consulte os seguintes recursos:

- [Especificações de imagem e texto]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats/)
- [Diretrizes de contagem de caracteres do iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/#character-count)