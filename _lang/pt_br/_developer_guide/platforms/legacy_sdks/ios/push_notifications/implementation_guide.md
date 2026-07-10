---
nav_title: Implementação avançada (opcional)
article_title: Implementação avançada de notificações por push para iOS (opcional)
platform: iOS
page_order: 28
description: "Este guia de implementação avançada aborda como aproveitar as extensões de app de conteúdo de notificação por push do iOS para obter o máximo de suas mensagens push. Também estão incluídos três casos de uso criados por nossa equipe, trechos de código de acompanhamento e orientações sobre o registro de análise de dados."
channel:
  - push
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

<br>
{% alert important %}
Está procurando o guia básico de integração de desenvolvedores de notificações por push? Encontre [aqui]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration).
{% endalert %}

# Guia de implementação de notificações por push {#push-notification-implementation-guide}

> Este guia de implementação opcional e avançado aborda maneiras de aproveitar as extensões de app de conteúdo de notificação por push para obter o máximo de suas mensagens push. Incluídos estão três casos de uso personalizados criados por nossa equipe, trechos de código de acompanhamento e orientações sobre o registro de análise de dados. Consulte o [Repositório de Demonstrações da Braze](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)! Note que este guia de implementação está centrado em uma implementação Swift, mas são fornecidos trechos em Objective-C para os interessados.

## Extensões de app de conteúdo de notificação {#notification-content-app-extensions}

![Duas mensagens push mostradas lado a lado. A mensagem à esquerda mostra como é um push com a interface padrão. A mensagem à direita mostra um push de cartão perfurado de café feito com a implementação de uma UI de push personalizada.]({% image_buster /assets/img/push_implementation_guide/push1.png %}){: style="max-width:65%;border:0;margin-top:10px"}

Notificações por push, embora aparentemente padrão em diferentes plataformas, oferecem imensas opções de personalização além do que é normalmente implementado na interface padrão. Quando uma notificação por push é expandida, as extensões de conteúdo de notificação ativam uma visualização personalizada da notificação por push expandida.

As notificações por push podem ser expandidas de três maneiras diferentes: <br>- Manter o banner de push pressionado<br>- Deslizar para baixo no banner de push<br>- Deslizar o banner para a esquerda e selecionar "Exibir"

Essas visualizações personalizadas oferecem maneiras inteligentes de engajar os clientes, permitindo que você exiba muitos tipos distintos de conteúdo, incluindo notificações interativas, notificações preenchidas com dados de usuários e até mensagens push que podem capturar informações como números de telefone e e-mail. Embora implementar push dessa maneira possa ser desconhecido para alguns, um dos nossos recursos bem conhecidos na Braze, [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories), é um exemplo perfeito de como pode ser uma visualização personalizada para uma extensão de app de conteúdo de notificação!

### Requisitos {#requirements}
![Tela "Choose a template for your new target" do Xcode com "Notification Content Extension" selecionado em Application Extension.]({% image_buster /assets/img/push_implementation_guide/push15.png %}){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- [Notificações por push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) integradas com sucesso em seu app
- iOS 10 ou superior
- Os seguintes arquivos gerados pelo Xcode com base na sua linguagem de codificação:

Swift<br>
&#45; `NotificationViewController.swift`<br>
&#45; `MainInterface.storyboard`<br><br>
Objective-C<br>
&#45; `NotificationViewController.h`<br>
&#45; `NotificationViewController.m`<br>
&#45; `MainInterface.storyboard`

### Configuração de categoria personalizada {#custom-category-configuration}

Para configurar uma visualização personalizada no dashboard, você deve ativar os botões de notificação e inserir sua categoria personalizada. A categoria iOS personalizada pré-registrada que você fornece é então verificada em relação ao `UNNotificationExtensionCategory` no `.plist` do seu Alvo de Extensão de Conteúdo de Notificação. O valor fornecido aqui deve corresponder ao que está definido no dashboard da Braze.

![As opções do botão de notificação encontradas nas configurações do criador de mensagens push.]({% image_buster /assets/img/push_implementation_guide/push16.png %}){: style="max-width:75%;border:0;margin-top:10px"}
![Um plist mostrando NSExtension com UNNotificationExtensionCategory definido como "your_custom_category", UNNotificationExtensionDefaultContentHidden definido como 1 e UNNotificationExtensionInitialContentSizeRatio definido como 1.]({% image_buster /assets/img/push_implementation_guide/push17.png %}){: style="max-width:75%;border:0;margin-top:10px"}

{% alert tip %}
Como as notificações por push com extensões de conteúdo nem sempre são aparentes, é recomendável incluir um call to action para incentivar seus usuários a expandirem suas notificações por push.
{% endalert %}

## Caso de uso e passo a passo de implementação {#use-case-and-implementation-walkthrough}

Existem três tipos de extensão de app de conteúdo de notificação por push fornecidos. Cada tipo tem uma explicação do conceito, casos de uso potenciais e uma visão de como as variáveis de notificação por push podem parecer e ser usadas no dashboard da Braze:
- [Notificação por push interativa](#interactive-push-notification)
- [Notificações por push personalizadas](#personalized-push-notifications)
- [Notificação por push de captura de informações](#information-capture-push-notification)

### Notificação por push interativa {#interactive-push-notification}

Notificações por push podem responder às ações do usuário dentro de uma extensão de conteúdo. Para usuários com iOS 12 ou posterior, isso significa que você pode transformar suas mensagens push em notificações por push totalmente interativas! Essa interatividade oferece muitas possibilidades para engajar seus usuários em suas notificações. O exemplo a seguir mostra um push onde os usuários podem jogar um jogo de correspondência dentro da notificação expandida.

![Um diagrama de como as fases de uma notificação por push interativa poderiam ser. As imagens mostram um usuário pressionando uma notificação por push que exibe um jogo de correspondência interativo.]({% image_buster /assets/img/push_implementation_guide/push12.png %}){: style="border:0"}

#### Configuração do dashboard {#dashboard-configuration}

Para configurar uma visualização personalizada no dashboard, nas configurações do botão de notificação, insira a categoria específica que você deseja exibir. Em seguida, no `.plist` da sua Extensão de Conteúdo de Notificação, você também deve definir a categoria personalizada para o atributo `UNNotificationExtensionCategory`. O valor fornecido aqui deve corresponder ao que está definido no dashboard da Braze. Por fim, para ativar as interações do usuário em uma notificação por push, defina a chave `UNNotificationExtensionInteractionEnabled` como true.

![A seção de botões de notificação no dashboard da Braze com o campo iOS Notification Category definido como "match_game".]({% image_buster /assets/img/push_implementation_guide/push3.png %}){: style="float:right;max-width:45%;"}

![As opções do botão de notificação encontradas nas configurações do criador de mensagens push.]({% image_buster /assets/img/push_implementation_guide/push14.png %}){: style="max-width:50%;"}

#### Outros casos de uso {#other-use-cases}
Extensões de conteúdo push são uma opção empolgante para introduzir interatividade às suas promoções e aplicativos. Alguns exemplos incluem um jogo para os usuários jogarem, uma roleta de descontos ou um botão de "curtir" para salvar uma lista ou música.

##### Pronto para registrar análise de dados? {#ready-to-log-analytics}
Consulte a [seção a seguir](#logging-analytics) para entender melhor como o fluxo de dados deve ser.

### Notificações por push personalizadas {#personalized-push-notifications}
![Dois iPhones exibidos lado a lado. O primeiro iPhone mostra a visualização não expandida da mensagem push. O segundo iPhone mostra a versão expandida da mensagem push, exibindo uma foto do "progresso" de quanto avançaram em um curso, a próxima sessão e quando a próxima sessão deve ser concluída.]({% image_buster /assets/img/push_implementation_guide/push6.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

As notificações por push podem exibir informações específicas do usuário dentro de uma extensão de conteúdo. O exemplo à direita mostra uma notificação por push após um usuário ter concluído uma tarefa específica (curso do Braze Learning) e agora é incentivado a expandir essa notificação para verificar seu progresso. As informações fornecidas aqui são específicas do usuário e podem ser disparadas quando uma sessão é concluída ou quando uma ação específica do usuário é realizada, aproveitando um disparo da API.

#### Configuração do dashboard

Para configurar um push personalizado no dashboard, você deve registrar a categoria específica que deseja exibir e, em seguida, dentro dos pares chave-valor usando Liquid padrão, definir os atributos de usuário apropriados que você deseja que a mensagem mostre. Essas visualizações podem ser personalizadas com base em atributos específicos de um perfil de usuário específico.

![Quatro conjuntos de pares chave-valor, onde "next_session_name" e "next_session_complete_date" são definidos como uma propriedade de disparo da API usando Liquid, e "completed_session count" e "total_session_count" são definidos como um atributo de usuário personalizado usando Liquid.]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

#### Manuseio de pares chave-valor {#handling-key-value-pairs}

O método `didReceive` é chamado quando a extensão de conteúdo recebe uma notificação e pode ser encontrado em `NotificationViewController`. Os pares chave-valor fornecidos no dashboard são representados no código através do uso de um dicionário `userInfo`.

**Analisando pares chave-valor de notificações por push**<br>

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

#### Outros casos de uso

As ideias para extensões de conteúdo push baseadas em progresso e focadas no usuário são infinitas. Alguns exemplos incluem adicionar a opção de compartilhar seu progresso em diferentes plataformas, expressar conquistas desbloqueadas, cartões de fidelidade ou até mesmo listas de verificação de integração.

##### Pronto para registrar análise de dados?
Consulte a [seção a seguir](#logging-analytics) para entender melhor como o fluxo de dados deve ser.

### Notificação por push de captura de informações {#information-capture-push-notification}

Notificações por push podem capturar informações do usuário dentro de uma extensão de conteúdo, permitindo que você amplie os limites do que é possível com um push. Examinando o fluxo a seguir, a visualização é capaz de responder às mudanças de estado. Esses componentes de mudança de estado estão representados em cada imagem.

1. O usuário recebe uma notificação por push.
2. O push é aberto e solicita informações ao usuário.
3. As informações são fornecidas e, se forem válidas, o botão de registro é exibido.
3. A visualização de confirmação é exibida e o push é dispensado.


Note que as informações solicitadas aqui podem ser variadas, como captura de número de SMS; não precisam ser específicas para e-mail.

#### Configuração do dashboard

Para configurar um push capaz de capturar informações no dashboard, você deve registrar e definir sua categoria personalizada e fornecer os pares chave-valor necessários. Como visto no exemplo, você também pode incluir uma imagem em seu push. Para fazer isso, você deve integrar [notificações Rich]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/rich_notifications), definir o estilo da notificação em sua Campaign como notificação Rich e incluir uma imagem de push Rich.

![Uma mensagem push com três conjuntos de pares chave-valor. 1. "Braze_id" definido como uma chamada Liquid para recuperar o ID da Braze. 2. "cert_title" definido como "Braze Marketer Certification". 3. "Cert_description" definido como "Certified Braze marketers drive...".]({% image_buster /assets/img/push_implementation_guide/push9.png %})

#### Manipulação de ações de botões {#handling-button-actions}

Cada botão de ação é identificado de forma exclusiva. O código verifica se o identificador da resposta é igual ao `actionIdentifier` e, em caso afirmativo, sabe que o usuário clicou no botão de ação.

**Manipulação de respostas de botões de ação de notificações por push**<br>

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

##### Dispensando pushes {#dismissing-pushes}

As notificações por push podem ser automaticamente descartadas ao pressionar um botão de ação. Recomendamos três opções pré-definidas para descarte de push:

1. `completion(.dismiss)` - Dispensa a notificação
2. `completion(.doNotDismiss)` - A notificação permanece aberta
3. `completion(.dismissAndForward)` - O push é descartado e o usuário é encaminhado para o aplicativo.

#### Outros casos de uso

Solicitar a entrada do usuário por meio de notificações por push é uma oportunidade empolgante que muitas empresas não aproveitam. Nessas mensagens push, você pode não apenas solicitar informações básicas como nome, e-mail ou número, mas também pode solicitar que os usuários completem um perfil de usuário se estiver incompleto, ou até mesmo enviem feedback.

##### Pronto para registrar análise de dados?
Consulte a [seção a seguir](#logging-analytics) para entender melhor como o fluxo de dados deve ser.

## Registro de análise de dados {#logging-analytics}

### Registro com a API da Braze (recomendado) {#logging-with-the-braze-api-recommended}

O registro de análise de dados só pode ser feito em tempo real com a ajuda do servidor do cliente acessando nosso [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Para registrar análise de dados, envie o valor `braze_id` no campo de pares chave-valor (como visto na captura de tela a seguir) para identificar qual perfil de usuário deve ser atualizado.

![Uma mensagem push com três conjuntos de pares chave-valor. 1. "Braze_id" definido como uma chamada Liquid para recuperar o ID da Braze. 2. "cert_title" definido como "Braze Marketer Certification". 3. "Cert_description" definido como "Certified Braze marketers drive...".]({% image_buster /assets/img/push_implementation_guide/push18.png %}){: style="max-width:80%;"}

### Registro manual {#logging-manually}

O registro manual exigirá primeiro a configuração dos grupos de apps no Xcode e, em seguida, a criação, o salvamento e a recuperação da análise de dados. Isso exigirá algum trabalho de desenvolvimento personalizado da sua parte. Os trechos de código a seguir ajudarão a resolver isso.

Também é importante notar que a análise de dados não é enviada à Braze até que o aplicativo móvel seja iniciado posteriormente. Isso significa que, dependendo das configurações de dispensa, muitas vezes existe um período indeterminado de tempo entre o momento em que uma notificação por push é dispensada e o aplicativo móvel é iniciado e a análise de dados é recuperada. Embora esse intervalo de tempo possa não afetar todos os casos de uso, os usuários devem considerar o impacto e, se necessário, ajustar sua jornada do usuário para incluir a abertura do aplicativo para resolver essa questão.

![Um gráfico que descreve como a análise de dados é processada na Braze. 1. Os dados de análise são criados. 2. Os dados de análise são salvos. 3. A notificação por push é dispensada. 4. Período indeterminado de tempo entre o momento em que a notificação por push é descartada e o app móvel é iniciado. 5. O app móvel é lançado. 6. Os dados de análise são recebidos. 7. Os dados de análise são enviados à Braze.]({% image_buster /assets/img/push_implementation_guide/push13.png %})

#### Etapa 1: Configurar grupos de apps no Xcode {#step-1-configure-app-groups-within-xcode}
Adicione a capacidade `App Groups`. Se você não tiver nenhum grupo de apps no seu app, acesse a capacidade do alvo principal do app, ative o `App Groups` e clique no "+". Use o ID do pacote do seu app para criar o grupo de apps. Por exemplo, se o ID do pacote do seu app for `com.company.appname`, você poderá nomear o grupo de apps como `group.com.company.appname.xyz`. Certifique-se de que o `App Groups` esteja ativado tanto para o alvo principal do app quanto para o alvo da extensão de conteúdo.

![A caixa de diálogo "Add a new container" no Xcode para configurar um grupo de apps, com um campo de texto pré-preenchido com "group.".]({% image_buster /assets/img/ios/push_story/add_app_groups.png %})

#### Etapa 2: Integrar trechos de código {#step-2-integrate-code-snippets}
Os trechos de código a seguir são uma referência útil sobre como salvar e enviar eventos personalizados, atributos personalizados e atributos de usuário. Este guia falará em termos de UserDefaults, mas a representação do código será feita na forma do arquivo auxiliar `RemoteStorage`. Há arquivos auxiliares adicionais, `UserAttributes` e `EventName Dictionary`, que são usados ao enviar e salvar atributos do usuário. Todos os arquivos auxiliares podem ser encontrados no final deste guia.

{% tabs local %}
{% tab Custom Events %}

##### Salvando eventos personalizados {#saving-custom-events}

Para salvar eventos personalizados, você deve criar a análise de dados do zero. Isso é feito criando um dicionário, preenchendo-o com metadados e salvando os dados através do uso de um arquivo auxiliar.

1. Inicializar um dicionário com metadados de eventos
2. Inicializar `userDefaults` para recuperar e armazenar os dados do evento
3. Se houver um array existente, acrescentar novos dados ao array existente e salvar
4. Se não houver um array existente, salvar o novo array em `userDefaults`

{% subtabs global %}
{% subtab Swift %}
``` swift
func saveCustomEvent(with properties: [String: Any]? = nil) {
  // 1
  let customEventDictionary = Dictionary(eventName: "YOUR-EVENT-NAME", properties: properties)

  // 2
  let remoteStorage = RemoteStorage(storageType: .suite)

  // 3
  if var pendingEvents = remoteStorage.retrieve(forKey: .pendingCustomEvents) as? [[String: Any]] {
    pendingEvents.append(contentsOf: [customEventDictionary])
    remoteStorage.store(pendingEvents, forKey: .pendingCustomEvents)
  } else {
  // 4
    remoteStorage.store([customEventDictionary], forKey: .pendingCustomEvents)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)saveCustomEvent:(NSDictionary<NSString *, id> *)properties {
  // 1
  NSDictionary<NSString *, id> *customEventDictionary = [[NSDictionary alloc] initWithEventName:@"YOUR-EVENT-NAME" properties:properties];

  // 2
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingEvents = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomEvents] mutableCopy];

  // 3
  if (pendingEvents) {
    [pendingEvents addObject:customEventDictionary];
    [remoteStorage store:pendingEvents forKey:RemoteStorageKeyPendingCustomAttributes];
  } else {
  // 4
    [remoteStorage store:@[ customEventDictionary ] forKey:RemoteStorageKeyPendingCustomAttributes];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

##### Enviando eventos personalizados para a Braze {#sending-custom-events-to-braze}

O melhor momento para registrar qualquer análise de dados salva de uma extensão de app de conteúdo de notificação é logo após a inicialização do SDK. Isso pode ser feito percorrendo quaisquer eventos pendentes, verificando a chave "Event Name", definindo os valores apropriados na Braze e, em seguida, limpando o armazenamento para a próxima vez que essa função for necessária.

1. Percorrer o array de eventos pendentes
2. Percorrer cada par chave-valor no dicionário `pendingEvents`
3. Verificar explicitamente a chave "Event Name" para definir o valor de acordo
4. Todos os outros pares chave-valor serão adicionados ao dicionário `properties`
5. Registrar eventos personalizados individuais
6. Remover todos os eventos pendentes do armazenamento

{% subtabs global %}
{% subtab Swift %}
``` swift
func logPendingCustomEventsIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingEvents = remoteStorage.retrieve(forKey: .pendingCustomEvents) as? [[String: Any]] else { return }

  // 1
  for event in pendingEvents {
    var eventName: String?
    var properties: [AnyHashable: Any] = [:]

  // 2
    for (key, value) in event {
      if key == PushNotificationKey.eventName.rawValue {
  // 3
        if let eventNameValue = value as? String {
          eventName = eventNameValue
        } else {
          print("Invalid type for event_name key")
        }
      } else {
  // 4
        properties[key] = value
      }
    }
  // 5
    if let eventName = eventName {
      logCustomEvent(eventName, withProperties: properties)
    }
  }

  // 6
  remoteStorage.removeObject(forKey: .pendingCustomEvents)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingEventsIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingEvents = [remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomEvents];

  // 1
  for (NSDictionary<NSString *, id> *event in pendingEvents) {
    NSString *eventName = nil;
    NSMutableDictionary *properties = [NSMutableDictionary dictionary];

  // 2
    for (NSString* key in event) {
      if ([key isEqualToString:@"event_name"]) {
  // 3
        if ([[event objectForKey:key] isKindOfClass:[NSString class]]) {
          eventName = [event objectForKey:key];
        } else {
          NSLog(@"Invalid type for event_name key");
        }
      } else {
  // 4
        properties[key] = event[key];
      }
    }
  // 5
    if (eventName != nil) {
      [[Appboy sharednstance] logCustomEvent:eventName withProperties:properties];
    }
  }

  // 6
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingCustomEvents];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Custom Attributes %}

##### Salvando atributos personalizados {#saving-custom-attributes}

Para salvar atributos personalizados, você deve criar a análise de dados do zero. Isso é feito criando um dicionário, preenchendo-o com metadados e salvando os dados através do uso de um arquivo auxiliar.

1. Inicializar um dicionário com metadados de atributos
2. Inicializar `userDefaults` para recuperar e armazenar os dados de atributos
3. Se houver um array existente, acrescentar novos dados ao array existente e salvar
4. Se não houver um array existente, salvar o novo array em `userDefaults`

{% subtabs global %}
{% subtab Swift %}
``` swift
func saveCustomAttribute() {
  // 1
  let customAttributeDictionary: [String: Any] = ["YOUR-CUSTOM-ATTRIBUTE-KEY": "YOUR-CUSTOM-ATTRIBUTE-VALUE"]

  // 2
  let remoteStorage = RemoteStorage(storageType: .suite)

  // 3
  if var pendingAttributes = remoteStorage.retrieve(forKey: .pendingCustomAttributes) as? [[String: Any]] {
    pendingAttributes.append(contentsOf: [customAttributeDictionary])
    remoteStorage.store(pendingAttributes, forKey: .pendingCustomAttributes)
  } else {
  // 4
    remoteStorage.store([customAttributeDictionary], forKey: .pendingCustomAttributes)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
``` objc
- (void)saveCustomAttribute {
  // 1
  NSDictionary<NSString *, id> *customAttributeDictionary = @{ @"YOUR-CUSTOM-ATTRIBUTE-KEY": @"YOUR-CUSTOM-ATTRIBUTE-VALUE" };

  // 2
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingAttributes = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomAttributes] mutableCopy];

  // 3
  if (pendingAttributes) {
    [pendingAttributes addObject:customAttributeDictionary];
    [remoteStorage store:pendingAttributes forKey:RemoteStorageKeyPendingCustomAttributes];
  } else {
  // 4
    [remoteStorage store:@[ customAttributeDictionary ] forKey:RemoteStorageKeyPendingCustomAttributes];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

##### Enviando atributos personalizados para a Braze {#sending-custom-attributes-to-braze}

O melhor momento para registrar qualquer análise de dados salva de uma extensão de app de conteúdo de notificação é logo após a inicialização do SDK. Isso pode ser feito percorrendo os atributos pendentes, definindo o atributo personalizado apropriado na Braze e, em seguida, limpando o armazenamento para a próxima vez que essa função for necessária.

1. Percorrer o array de atributos pendentes
2. Percorrer cada par chave-valor no dicionário `pendingAttributes`
3. Registrar o atributo personalizado individual com a chave e o valor correspondentes
4. Remover todos os atributos pendentes do armazenamento

{% subtabs global %}
{% subtab Swift %}
``` swift
func logPendingCustomAttributesIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingAttributes = remoteStorage.retrieve(forKey: .pendingCustomAttributes) as? [[String: Any]] else { return }

  // 1
  pendingAttributes.forEach { setCustomAttributesWith(keysAndValues: $0) }

  // 4
  remoteStorage.removeObject(forKey: .pendingCustomAttributes)
}

func setCustomAttributesWith(keysAndValues: [String: Any]) {
  // 2
  for (key, value) in keysAndValues {
  // 3
    if let value = value as? [String] {
      setCustomAttributeArrayWithKey(key, andValue: value)
    } else {
      setCustomAttributeWithKey(key, andValue: value)
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingCustomAttributesIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingAttributes = [remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomAttributes];

  // 1
  for (NSDictionary<NSString*, id> *attribute in pendingAttributes) {
    [self setCustomAttributeWith:attribute];
  }

  // 4
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingCustomAttributes];
}

- (void)setCustomAttributeWith:(NSDictionary<NSString *, id> *)keysAndValues {
  // 2
  for (NSString *key in keysAndValues) {
  // 3
    [self setCustomAttributeWith:key andValue:[keysAndValues objectForKey:key]];
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab User Attributes %}

##### Salvando atributos do usuário {#saving-user-attributes}

Ao salvar atributos de usuário, é recomendável criar um objeto personalizado para decifrar que tipo de atributo está sendo atualizado (`email`, `first_name`, `phone_number`, etc.). O objeto deve ser compatível com o armazenamento/recuperação de `UserDefaults`. Consulte o arquivo auxiliar `UserAttribute` para obter um exemplo de como fazer isso.

1. Inicializar um objeto `UserAttribute` codificado com o tipo correspondente
2. Inicializar `userDefaults` para recuperar e armazenar os dados do evento
3. Se houver um array existente, acrescentar novos dados ao array existente e salvar
4. Se não houver um array existente, salvar o novo array em `userDefaults`

{% subtabs global %}
{% subtab Swift %}
``` swift
func saveUserAttribute() {
  // 1
  guard let data = try? PropertyListEncoder().encode(UserAttribute.userAttributeType("USER-ATTRIBUTE-VALUE")) else { return }

  // 2
  let remoteStorage = RemoteStorage(storageType: .suite)

  // 3
  if var pendingAttributes = remoteStorage.retrieve(forKey: .pendingUserAttributes) as? [Data] {
    pendingAttributes.append(contentsOf: [data])
    remoteStorage.store(pendingAttributes, forKey: .pendingUserAttributes)
  } else {
  // 4
    remoteStorage.store([data], forKey: .pendingUserAttributes)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)saveUserAttribute {
  // 1
  UserAttribute *userAttribute = [[UserAttribute alloc] initWithUserField:@"USER-ATTRIBUTE-VALUE" attributeType:UserAttributeTypeEmail];

  NSError *error;
  NSData *data = [NSKeyedArchiver archivedDataWithRootObject:userAttribute requiringSecureCoding:YES error:&error];

  if (error != nil) {
    // log error
  }
  // 2
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingAttributes = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingUserAttributes] mutableCopy];

  // 3
  if (pendingAttributes) {
    [pendingAttributes addObject:data];
    [remoteStorage store:pendingAttributes forKey:RemoteStorageKeyPendingUserAttributes];
  } else {
  // 4
    [remoteStorage store:@[data] forKey:RemoteStorageKeyPendingUserAttributes];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

##### Enviando atributos do usuário para a Braze {#sending-user-attributes-to-braze}

O melhor momento para registrar qualquer análise de dados salva de uma extensão de app de conteúdo de notificação é logo após a inicialização do SDK. Isso pode ser feito percorrendo os atributos pendentes, definindo o atributo personalizado apropriado na Braze e, em seguida, limpando o armazenamento para a próxima vez que essa função for necessária.

1. Percorrer o array de dados `pendingAttributes`
2. Inicializar um objeto `UserAttribute` codificado a partir dos dados de atributos
3. Definir um campo de usuário específico com base no tipo de atributo do usuário (e-mail)
4. Remover todos os atributos de usuário pendentes do armazenamento

{% subtabs global %}
{% subtab Swift %}
``` swift
func logPendingUserAttributesIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingAttributes = remoteStorage.retrieve(forKey: .pendingUserAttributes) as? [Data] else { return }

  // 1
  for attributeData in pendingAttributes {
  // 2
    guard let userAttribute = try? PropertyListDecoder().decode(UserAttribute.self, from: attributeData) else { continue }

  // 3
    switch userAttribute {
    case .email(let email):
      user?.email = email
    }
  }
  // 4
  remoteStorage.removeObject(forKey: .pendingUserAttributes)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingUserAttributesIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingAttributes = [remoteStorage retrieveForKey:RemoteStorageKeyPendingUserAttributes];

  // 1
  for (NSData *attributeData in pendingAttributes) {
    NSError *error;

  // 2
    UserAttribute *userAttribute = [NSKeyedUnarchiver unarchivedObjectOfClass:[UserAttribute class] fromData:attributeData error:&error];

    if (error != nil) {
      // log error
    }

  // 3
    if (userAttribute) {
      switch (userAttribute.attributeType) {
        case UserAttributeTypeEmail:
          [self user].email = userAttribute.userField;
          break;
      }
    }
  }
  // 4
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingUserAttributes];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Helper Files %}

##### Arquivos auxiliares {#helper-files}

{% details Arquivo auxiliar RemoteStorage %}
{% subtabs global %}
{% subtab Swift %}
```swift
enum RemoteStorageKey: String, CaseIterable {

  // MARK: - Notification Content Extension Analytics
  case pendingCustomEvents = "pending_custom_events"
  case pendingCustomAttributes = "pending_custom_attributes"
  case pendingUserAttributes = "pending_user_attributes"
}

enum RemoteStorageType {
  case standard
  case suite
}

class RemoteStorage: NSObject {
  private var storageType: RemoteStorageType = .standard
  private lazy var defaults: UserDefaults = {
    switch storageType {
    case .standard:
      return .standard
    case .suite:
      return UserDefaults(suiteName: "YOUR-DOMAIN-IDENTIFIER")!
    }
  }()

  init(storageType: RemoteStorageType = .standard) {
    self.storageType = storageType
  }

  func store(_ value: Any, forKey key: RemoteStorageKey) {
    defaults.set(value, forKey: key.rawValue)
  }

  func retrieve(forKey key: RemoteStorageKey) -> Any? {
    return defaults.object(forKey: key.rawValue)
  }

  func removeObject(forKey key: RemoteStorageKey) {
    defaults.removeObject(forKey: key.rawValue)
  }

  func resetStorageKeys() {
    for key in RemoteStorageKey.allCases {
      defaults.removeObject(forKey: key.rawValue)
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@interface RemoteStorage ()

@property (nonatomic) StorageType storageType;
@property (nonatomic, strong) NSUserDefaults *defaults;

@end

@implementation RemoteStorage

- (id)initWithStorageType:(StorageType)storageType {
  if (self = [super init]) {
    self.storageType = storageType;
  }
  return self;
}

- (void)store:(id)value forKey:(RemoteStorageKey)key {
  [[self defaults] setValue:value forKey:[self rawValueForKey:key]];
}

- (id)retrieveForKey:(RemoteStorageKey)key {
  return [[self defaults] objectForKey:[self rawValueForKey:key]];
}

- (void)removeObjectForKey:(RemoteStorageKey)key {
  [[self defaults] removeObjectForKey:[self rawValueForKey:key]];
}

- (void)resetStorageKeys {
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingCustomEvents]];
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingCustomAttributes]];
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingUserAttributes]];
}

- (NSUserDefaults *)defaults {
  if (!self.defaults) {
    switch (self.storageType) {
      case StorageTypeStandard:
        return [NSUserDefaults standardUserDefaults];
        break;
      case StorageTypeSuite:
        return [[NSUserDefaults alloc] initWithSuiteName:@"YOUR-DOMAIN-IDENTIFIER"];
    }
  } else {
    return self.defaults;
  }
}

- (NSString*)rawValueForKey:(RemoteStorageKey)remoteStorageKey {
    switch(remoteStorageKey) {
    case RemoteStorageKeyPendingCustomEvents:
      return @"pending_custom_events";
    case RemoteStorageKeyPendingCustomAttributes:
      return @"pending_custom_attributes";
    case RemoteStorageKeyPendingUserAttributes:
      return @"pending_user_attributes";
    default:
      [NSException raise:NSGenericException format:@"Unexpected FormatType."];
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
{% details Arquivo auxiliar UserAttribute %}
{% subtabs global %}
{% subtab Swift %}
```swift
enum UserAttribute: Hashable {
  case email(String?)
}

// MARK: - Codable
extension UserAttribute: Codable {
  private enum CodingKeys: String, CodingKey {
    case email
  }

  func encode(to encoder: Encoder) throws {
    var values = encoder.container(keyedBy: CodingKeys.self)

    switch self {
    case .email(let email):
      try values.encode(email, forKey: .email)
    }
  }

  init(from decoder: Decoder) throws {
    let values = try decoder.container(keyedBy: CodingKeys.self)

    let email = try values.decode(String.self, forKey: .email)
    self = .email(email)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation UserAttribute

- (id)initWithUserField:(NSString *)userField attributeType:(UserAttributeType)attributeType {
  if (self = [super init]) {
    self.userField = userField;
    self.attributeType = attributeType;
  }
  return self;
}

- (void)encodeWithCoder:(NSCoder *)encoder {
  [encoder encodeObject:self.userField forKey:@"userField"];
  [encoder encodeInteger:self.attributeType forKey:@"attributeType"];
}

- (id)initWithCoder:(NSCoder *)decoder {
  if (self = [super init]) {
    self.userField = [decoder decodeObjectForKey:@"userField"];

    NSInteger attributeRawValue = [decoder decodeIntegerForKey:@"attributeType"];
    self.attributeType = (UserAttributeType) attributeRawValue;
  }
  return self;
}

@end
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
{% details Arquivo auxiliar EventName Dictionary %}
{% subtabs global %}
{% subtab Swift %}
```swift
extension Dictionary where Key == String, Value == Any {
  init(eventName: String, properties: [String: Any]? = nil) {
    self.init()
    self[PushNotificationKey.eventName.rawValue] = eventName

    if let properties = properties {
      for (key, value) in properties {
        self[key] = value
      }
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation NSDictionary (Helper)

- (id)initWithEventName:(NSString *)eventName properties:(NSDictionary *)properties {
  self = [self init];
  if (self) {
    dict[@"event_name"] = eventName;

    for(id key in properties) {
      dict[key] = properties[key];
    }
  }
  return self;
}

@end
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
<br>
{% endtab %}
{% endtabs %}