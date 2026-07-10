{% multi_lang_include developer_guide/prerequisites/swift.md %} Você também precisará [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

{% alert note %}
Este guia de implementação é centrado em uma implementação Swift, mas trechos em Objective-C são fornecidos para quem tiver interesse.
{% endalert %}

## Extensões de app de conteúdo de notificação {#notification-content-app-extensions}

![Duas mensagens push mostradas lado a lado. A mensagem à esquerda mostra a aparência de um push com a UI padrão. A mensagem à direita mostra um push de cartão fidelidade de café feito com a implementação de uma UI de push personalizada.]({% image_buster /assets/img/push_implementation_guide/push1.png %}){: style="max-width:65%;border:0;margin-top:10px"}

As extensões de app de conteúdo de notificação oferecem uma ótima opção para personalizar notificações por push. Elas exibem uma interface personalizada para as notificações do seu app quando uma notificação por push é expandida.

As notificações por push podem ser expandidas de três maneiras diferentes:
- Pressionando longamente o banner de push
- Deslizando para baixo no banner de push
- Deslizando o banner para a esquerda e selecionando "View"

Essas visualizações personalizadas oferecem maneiras inteligentes de engajar clientes, exibindo tipos distintos de conteúdo, incluindo notificações interativas, notificações preenchidas com dados de usuários e até mesmo mensagens push que podem capturar informações como números de telefone e e-mail. Um dos nossos recursos mais conhecidos na Braze, o [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories), é um excelente exemplo de como uma extensão de app de conteúdo de notificação por push pode ser!

### Pré-requisitos {#requirements}

![Tela "Choose a template for your new target" do Xcode com "Notification Content Extension" selecionado em Application Extension.]({% image_buster /assets/img/push_implementation_guide/push15.png %}){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- [Notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) integradas com sucesso no seu app
- Os seguintes arquivos gerados pelo Xcode com base na sua linguagem de codificação:

**Swift**<br>
- `NotificationViewController.swift`
- `MainInterface.storyboard`

**Objective-C**<br>
- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

## Notificações por push interativas {#interactive-push-notification}

As notificações por push podem responder a ações do usuário dentro de uma extensão de app de conteúdo. Para usuários com iOS 12 ou posterior, isso significa que você pode transformar suas notificações por push em mensagens totalmente interativas! Essa é uma opção empolgante para introduzir interatividade nas suas promoções e aplicativos. Por exemplo, sua notificação por push pode incluir um jogo para os usuários jogarem, uma roleta de descontos ou um botão "curtir" para salvar um anúncio ou música.

O exemplo a seguir mostra uma notificação por push em que os usuários podem jogar um jogo de combinação dentro da notificação expandida.

![Um diagrama de como as fases de uma notificação por push interativa podem ser. Uma sequência mostra um usuário pressionando uma notificação por push que exibe um jogo de combinação interativo.]({% image_buster /assets/img/push_implementation_guide/push12.png %}){: style="border:0"}

### Configuração do dashboard {#dashboard-configuration}

Para criar uma notificação por push interativa, você deve definir uma visualização personalizada no seu dashboard.

1. Na página **Campaigns**, clique em **Create Campaign** para iniciar uma nova campanha de notificação por push.
2. Na guia **Compose**, ative os **Notification Buttons**.
3. Insira uma categoria personalizada do iOS no campo **iOS Notification Category**.
4. No `.plist` do seu Notification Content Extension Target, defina o atributo `UNNotificationExtensionCategory` para a sua categoria personalizada do iOS. O valor fornecido aqui deve corresponder ao que está definido no dashboard da Braze em **iOS Notification Category**.
5. Defina a chave `UNNotificationExtensionInteractionEnabled` como `true` para ativar as interações do usuário em uma notificação por push.

![As opções de botão de notificação encontradas nas configurações do criador de mensagens push.]({% image_buster /assets/img/push_implementation_guide/push16.png %}){: style="max-width:75%;border:0;margin-top:10px"}
![Um plist mostrando NSExtension com UNNotificationExtensionCategory definido como "your_custom_category", UNNotificationExtensionDefaultContentHidden definido como 1 e UNNotificationExtensionInitialContentSizeRatio definido como 1.]({% image_buster /assets/img/push_implementation_guide/push17.png %}){: style="max-width:75%;border:0;margin-top:10px"}

## Notificações por push personalizadas {#personalized-push-notifications}

![Dois iPhones exibidos lado a lado. O primeiro iPhone mostra a visualização não expandida da mensagem push. O segundo iPhone mostra a versão expandida da mensagem push, exibindo uma foto do "progresso" do curso, o nome da próxima sessão e quando a próxima sessão deve ser concluída.]({% image_buster /assets/img/push_implementation_guide/push6.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

As notificações por push podem exibir informações específicas do usuário dentro de uma extensão de conteúdo. Isso permite criar conteúdo push focado no usuário, como adicionar a opção de compartilhar seu progresso em diferentes plataformas, mostrar conquistas desbloqueadas ou exibir checklists de integração. Este exemplo mostra uma notificação por push exibida a um usuário após ele ter concluído uma tarefa específica no curso do Braze Learning. Ao expandir a notificação, o usuário pode ver seu progresso na jornada de aprendizagem. As informações fornecidas aqui são específicas do usuário e podem ser disparadas quando uma sessão é concluída ou quando uma ação específica do usuário é realizada, utilizando um gatilho de API.

### Configuração do dashboard

Para criar uma notificação por push personalizada, você deve definir uma visualização personalizada no seu dashboard.

1. Na página **Campaigns**, clique em **Create Campaign** para iniciar uma nova campanha de notificação por push.
2. Na guia **Compose**, ative os **Notification Buttons**.
3. Insira uma categoria personalizada do iOS no campo **iOS Notification Category**.
4. Na guia **Settings**, crie pares de chave-valor usando Liquid padrão. Defina os atributos de usuário apropriados que deseja que a mensagem exiba. Essas visualizações podem ser personalizadas com base em atributos específicos de um perfil de usuário específico.
5. No `.plist` do seu Notification Content Extension Target, defina o atributo `UNNotificationExtensionCategory` para a sua categoria personalizada do iOS. O valor fornecido aqui deve corresponder ao que está definido no dashboard da Braze em **iOS Notification Category**.

![Quatro conjuntos de pares de chave-valor, onde "next_session_name" e "next_session_complete_date" são definidos como uma propriedade de gatilho de API usando Liquid, e "completed_session count" e "total_session_count" são definidos como um atributo de usuário personalizado usando Liquid.]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

### Manipulação de pares de chave-valor {#handling-key-value-pairs}

O método `didReceive` é chamado quando a extensão de app de conteúdo de notificação recebe uma notificação. Esse método pode ser encontrado no `NotificationViewController`. Os pares de chave-valor fornecidos no dashboard são representados no código por meio de um dicionário `userInfo`.

#### Analisando pares de chave-valor de notificações por push {#parsing-key-value-pairs-from-push-notifications}

{% tabs %}
{% tab Swift %}
``` swift
func didReceive(_ notification: UNNotification) {
  let userInfo = notification.request.content.userInfo

  guard let value = userInfo["YOUR-KEY-VALUE-PAIR"] as? String,
        let otherValue = userInfo["YOUR-OTHER-KEY-VALUE-PAIR"] as? String,
  else { fatalError("Key-Value Pairs are incorrect.")}

  ...
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotification:(nonnull UNNotification *)notification {
  NSDictionary *userInfo = notification.request.content.userInfo;

  if (userInfo[@"YOUR-KEY-VALUE-PAIR"] && userInfo[@"YOUR-OTHER-KEY-VALUE-PAIR"]) {

  ...

  } else {
    [NSException raise:NSGenericException format:@"Key-Value Pairs are incorrect"];
  }
}
```
{% endtab %}
{% endtabs %}

## Notificação por push de captura de informações {#information-capture-push-notification}

As notificações por push podem capturar informações do usuário dentro de uma extensão de app de conteúdo, expandindo os limites do que é possível com um push. Solicitar entrada do usuário por meio de notificações por push permite não apenas pedir informações básicas como nome ou e-mail, mas também solicitar que os usuários enviem feedback ou completem um perfil de usuário inacabado.

{% alert tip %}
Para saber mais, consulte [Registro de dados de notificação por push]({{site.baseurl}}/developer_guide/analytics/logging_channel_data/push_notifications).
{% endalert %}

No fluxo a seguir, a visualização personalizada é capaz de responder a mudanças de estado. Esses componentes de mudança de estado são representados em cada imagem.

1. O usuário recebe uma notificação por push.
2. O push é aberto. Depois de expandido, o push solicita informações ao usuário. Neste exemplo, o endereço de e-mail do usuário é solicitado, mas você pode solicitar qualquer tipo de informação.
3. As informações são fornecidas e, se estiverem no formato esperado, o botão de registro é exibido.
3. A visualização de confirmação é exibida e o push é dispensado.


### Configuração do dashboard

Para criar uma notificação por push de captura de informações, você deve definir uma visualização personalizada no seu dashboard.

1. Na página **Campaigns**, clique em **Create Campaign** para iniciar uma nova campanha de notificação por push.
2. Na guia **Compose**, ative os **Notification Buttons**.
3. Insira uma categoria personalizada do iOS no campo **iOS Notification Category**.
4. Na guia **Settings**, crie pares de chave-valor usando Liquid padrão. Defina os atributos de usuário apropriados que deseja que a mensagem exiba.
5. No `.plist` do seu Notification Content Extension Target, defina o atributo `UNNotificationExtensionCategory` para a sua categoria personalizada do iOS. O valor fornecido aqui deve corresponder ao que está definido no dashboard da Braze em **iOS Notification Category**.

Como visto no exemplo, você também pode incluir uma imagem na sua notificação por push. Para isso, você deve integrar [notificações Rich]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift), definir o estilo de notificação na sua campanha como notificação Rich e incluir uma imagem de push Rich.

![Uma mensagem push com três conjuntos de pares de chave-valor. 1. "Braze_id" definido como uma chamada Liquid para recuperar o ID da Braze. 2. "cert_title" definido como "Braze Marketer Certification". 3. "Cert_description" definido como "Certified Braze marketers drive...".]({% image_buster /assets/img/push_implementation_guide/push9.png %})

### Manipulação de ações de botões {#handling-button-actions}

Cada botão de ação é identificado de forma exclusiva. O código verifica se o identificador da resposta é igual ao `actionIdentifier` e, em caso afirmativo, sabe que o usuário clicou no botão de ação.

**Manipulação de respostas de botões de ação de notificação por push**<br>

{% tabs %}
{% tab Swift %}
``` swift
func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
  if response.actionIdentifier == "YOUR-REGISTER-IDENTIFIER" {
    // do something
  } else {
    // do something else
  }
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response completionHandler:(void (^)(UNNotificationContentExtensionResponseOption))completion {
  if ([response.actionIdentifier isEqualToString:@"YOUR-REGISTER-IDENTIFIER"]) {
    completion(UNNotificationContentExtensionResponseOptionDismiss);
  } else {
    completion(UNNotificationContentExtensionResponseOptionDoNotDismiss);
  }
}
```
{% endtab %}
{% endtabs %}

### Dispensando pushes {#dismissing-pushes}

As notificações por push podem ser automaticamente dispensadas ao pressionar um botão de ação. Existem três opções pré-construídas de dispensa de push que recomendamos:

1. `completion(.dismiss)` - Dispensa a notificação
2. `completion(.doNotDismiss)` - A notificação permanece aberta
3. `completion(.dismissAndForward)` - O push é dispensado e o usuário é encaminhado para o aplicativo