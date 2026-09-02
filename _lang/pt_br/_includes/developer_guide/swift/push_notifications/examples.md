{% multi_lang_include developer_guide/prerequisites/swift.md %} Você também precisará [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

{% alert note %}
Este guia de implementação é centrado em uma implementação Swift, mas trechos em Objective-C são fornecidos para quem tiver interesse.
{% endalert %}

## Extensões de app para conteúdo de notificação {#notification-content-app-extensions}

![Duas mensagens push exibidas lado a lado. A mensagem à esquerda mostra como um push aparece com a UI padrão. A mensagem à direita mostra um push com cartão fidelidade de café, criado implementando uma UI de push personalizada.]({% image_buster /assets/img/push_implementation_guide/push1.png %}){: style="max-width:65%;border:0;margin-top:10px"}

As extensões de app para conteúdo de notificação oferecem uma ótima opção para personalização de notificações por push. Elas exibem uma interface personalizada para as notificações do seu app quando uma notificação por push é expandida.

As notificações por push podem ser expandidas de três formas diferentes:
- Pressionando e segurando o banner de push
- Deslizando para baixo no banner de push
- Deslizando o banner horizontalmente e selecionando "Visualizar"

Essas visualizações personalizadas oferecem formas inteligentes de engajar clientes ao exibir tipos distintos de conteúdo, incluindo notificações interativas, notificações preenchidas com dados do usuário e até mensagens push que podem capturar informações como números de telefone e e-mails. Um dos nossos recursos mais conhecidos na Braze, [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories), é um ótimo exemplo de como uma extensão de app para conteúdo de notificação por push pode ser!

### Requisitos {#requirements}

![Tela do Xcode para escolher um modelo para o novo target, com 'Notification Content Extension' selecionado em Application Extension.]({% image_buster /assets/img/push_implementation_guide/push15.png %}){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- [Notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) integradas com sucesso no seu app
- Os seguintes arquivos gerados pelo Xcode com base na sua linguagem de programação:

**Swift**<br>
- `NotificationViewController.swift`
- `MainInterface.storyboard`

**Objective-C**<br>
- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

## Notificação por push interativa {#interactive-push-notification}

As notificações por push podem responder às ações do usuário dentro de uma extensão de conteúdo do app. Para usuários com iOS 12 ou posterior, isso significa que você pode transformar suas notificações por push em mensagens totalmente interativas! Essa é uma opção empolgante para introduzir interatividade em suas promoções e aplicativos. Por exemplo, sua notificação por push pode incluir um jogo para os usuários jogarem, uma roleta de descontos ou um botão "curtir" para salvar um anúncio ou uma música.

O exemplo a seguir mostra uma notificação por push em que os usuários podem jogar um jogo da memória dentro da notificação expandida.

![Um diagrama mostrando como podem ser as fases de uma notificação por push interativa. Uma sequência mostra um usuário pressionando uma notificação por push que exibe um jogo interativo da memória.]({% image_buster /assets/img/push_implementation_guide/push12.png %}){: style="border:0"}

### Configuração no dashboard {#dashboard-configuration}

Para criar uma notificação por push interativa, você deve definir uma visualização personalizada no seu dashboard.

1. Na página **Campaigns**, clique em **Create Campaign** para iniciar uma nova campanha de notificação por push.
2. Na guia **Compose**, ative **Notification Buttons**.
3. Insira uma categoria iOS personalizada no campo **iOS Notification Category**.
4. No `.plist` do seu Notification Content Extension Target, defina o atributo `UNNotificationExtensionCategory` para a sua categoria iOS personalizada. O valor fornecido aqui deve corresponder ao que está definido no dashboard da Braze em **iOS Notification Category**.
5. Defina a chave `UNNotificationExtensionInteractionEnabled` como `true` para ativar as interações do usuário em uma notificação por push.

![As opções de botões de notificação encontradas nas configurações do criador de mensagem push.]({% image_buster /assets/img/push_implementation_guide/push16.png %}){: style="max-width:75%;border:0;margin-top:10px"}
![Um plist mostrando NSExtension com UNNotificationExtensionCategory definido como "your_custom_category", UNNotificationExtensionDefaultContentHidden definido como 1 e UNNotificationExtensionInitialContentSizeRatio definido como 1.]({% image_buster /assets/img/push_implementation_guide/push17.png %}){: style="max-width:75%;border:0;margin-top:10px"}

## Notificações por push personalizadas {#personalized-push-notifications}

![Dois iPhones exibidos lado a lado. O primeiro iPhone mostra a visualização não expandida da mensagem push. O segundo iPhone mostra a versão expandida da mensagem push, exibindo um indicador de "progresso" de quanto o usuário avançou em um curso, o nome da próxima sessão e quando ela deve ser concluída.]({% image_buster /assets/img/push_implementation_guide/push6.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

As notificações por push podem exibir informações específicas do usuário dentro de uma extensão de conteúdo. Isso permite criar conteúdo de push focado no usuário, como adicionar a opção de compartilhar seu progresso em diferentes plataformas, mostrar conquistas desbloqueadas ou exibir checklists de integração. Este exemplo mostra uma notificação por push exibida a um usuário depois de concluir uma tarefa específica no curso do Braze Learning. Ao expandir a notificação, o usuário pode ver seu progresso ao longo da jornada de aprendizado. As informações fornecidas aqui são específicas do usuário e podem ser disparadas quando uma sessão é concluída ou quando uma ação específica do usuário é realizada, usando um disparo via API or interface de programação do aplicativo (API).

### Configuração no dashboard

Para criar uma notificação por push personalizada, você deve definir uma visualização personalizada no dashboard.

1. Na página **Campaigns**, clique em **Create Campaign** para iniciar uma nova Campaign de notificação por push.
2. Na guia **Compose**, ative os **Notification Buttons**.
3. Insira uma categoria iOS personalizada no campo **iOS Notification Category**.
4. Na guia **Settings**, crie pares de chave-valor usando Liquid padrão. Defina os atributos de usuário apropriados que você deseja que a mensagem exiba. Essas visualizações podem ser personalizadas com base em atributos específicos de um perfil de usuário específico.
5. No `.plist` do seu Notification Content Extension Target, defina o atributo `UNNotificationExtensionCategory` com a sua categoria iOS personalizada. O valor fornecido aqui deve corresponder ao que está definido no dashboard da Braze em **iOS Notification Category**.

![Quatro conjuntos de pares de chave-valor, em que "next_session_name" e "next_session_complete_date" são definidos como uma propriedade de disparo via API usando Liquid, e "completed_session count" e "total_session_count" são definidos como atributos personalizados do usuário usando Liquid.]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

### Tratamento de pares de chave-valor {#handling-key-value-pairs}

O método `didReceive` é chamado quando a extensão de conteúdo de notificação do app recebe uma notificação. Esse método pode ser encontrado dentro do `NotificationViewController`. Os pares de chave-valor fornecidos no dashboard são representados no código por meio do uso de um dicionário `userInfo`.

#### Parsing de pares de chave-valor de notificações por push {#parsing-key-value-pairs-from-push-notifications}

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

Notificações por push podem capturar informações do usuário dentro de uma extensão de conteúdo do app, expandindo os limites do que é possível com um push. Solicitar entrada do usuário por meio de notificações por push permite não apenas solicitar informações básicas como nome ou e-mail, mas também incentivar os usuários a enviar feedback ou completar um perfil de usuário incompleto.

{% alert tip %}
Para saber mais, consulte [Registrando dados de notificações por push]({{site.baseurl}}/developer_guide/analytics/logging_channel_data/push_notifications).
{% endalert %}

No fluxo a seguir, a visualização personalizada é capaz de responder a mudanças de estado. Esses componentes de mudança de estado são representados em cada imagem.

1. O usuário recebe uma notificação por push.
2. O push é aberto. Após expandido, o push solicita informações ao usuário. Neste exemplo, o endereço de e-mail do usuário é solicitado, mas você pode solicitar qualquer tipo de informação.
3. As informações são fornecidas e, se estiverem no formato esperado, o botão de registro é exibido.
3. A visualização de confirmação é exibida e o push é dispensado.


### Configuração no dashboard

Para criar uma notificação por push de captura de informações, você deve definir uma visualização personalizada no seu dashboard.

1. Na página **Campaigns**, clique em **Create Campaign** para iniciar uma nova Campaign de notificação por push.
2. Na guia **Compose**, ative **Notification Buttons**.
3. Insira uma categoria iOS personalizada no campo **iOS Notification Category**.
4. Na guia **Settings**, crie pares chave-valor usando Liquid padrão. Defina os atributos de usuário apropriados que você deseja que a mensagem exiba.
5. No `.plist` do seu Notification Content Extension Target, defina o atributo `UNNotificationExtensionCategory` para a sua categoria iOS personalizada. O valor fornecido aqui deve corresponder ao que está definido no dashboard da Braze em **iOS Notification Category**.

Como mostrado no exemplo, você também pode incluir uma imagem na sua notificação por push. Para isso, você deve integrar [notificações Rich]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift), definir o estilo da notificação na sua Campaign como notificação Rich e incluir uma imagem de push Rich.

![Uma mensagem push com três conjuntos de pares chave-valor. 1. "Braze_id" definido como uma chamada Liquid para obter o Braze ID. 2. "cert_title" definido como "Braze Marketer Certification". 3. "Cert_description" definido como "Certified Braze marketers drive...".]({% image_buster /assets/img/push_implementation_guide/push9.png %})

### Tratando ações de botões {#handling-button-actions}

Cada botão de ação é identificado de forma única. O código verifica se o identificador de resposta é igual ao `actionIdentifier` e, se for, sabe que o usuário clicou no botão de ação.

**Tratando respostas de botões de ação de notificações por push**<br>

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

### Dispensando pushs {#dismissing-pushes}

Notificações por push podem ser dispensadas automaticamente ao pressionar um botão de ação. Existem três opções pré-construídas de dispensa de push que recomendamos:

1. `completion(.dismiss)` - Dispensa a notificação
2. `completion(.doNotDismiss)` - A notificação permanece aberta
3. `completion(.dismissAndForward)` - O push é dispensado e o usuário é redirecionado para o aplicativo