{% multi_lang_include developer_guide/prerequisites/swift.md %} Vous devrez également [configurer les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

{% alert note %}
Ce guide d'implémentation est centré sur une implémentation Swift, mais des extraits de code Objective-C sont fournis pour les personnes intéressées.
{% endalert %}

## Extensions d'application de contenu de notification {#notification-content-app-extensions}

![Deux notifications push affichées côte à côte. Le message de gauche montre une notification push avec l'interface par défaut. Le message de droite montre une notification push de carte de fidélité café créée en implémentant une interface push personnalisée.]({% image_buster /assets/img/push_implementation_guide/push1.png %}){: style="max-width:65%;border:0;margin-top:10px"}

Les extensions d'application de contenu de notification vous offrent une excellente option pour personnaliser les notifications push. Les extensions d'application de contenu de notification affichent une interface personnalisée pour les notifications de votre application lorsqu'une notification push est développée.

Les notifications push peuvent être développées de trois manières différentes :
- Un appui long sur la bannière de notification push
- Un balayage vers le bas sur la bannière de notification push
- Un balayage horizontal de la bannière et la sélection de « Afficher »

Ces vues personnalisées offrent des moyens intelligents d'interagir avec les clients en affichant des types de contenu distincts, notamment des notifications interactives, des notifications remplies avec les données utilisateur, et même des notifications push capables de capturer des informations comme des numéros de téléphone et des adresses e-mail. L'une de nos fonctionnalités bien connues chez Braze, les [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories), est un excellent exemple de ce à quoi peut ressembler une extension d'application de contenu de notification push !

### Prérequis {#requirements}

![L'écran « Choose a template for your new target » de Xcode avec « Notification Content Extension » sélectionné sous Application Extension.]({% image_buster /assets/img/push_implementation_guide/push15.png %}){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- Les [notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) correctement intégrées dans votre application
- Les fichiers suivants générés par Xcode en fonction de votre langage de programmation :

**Swift**<br>
- `NotificationViewController.swift`
- `MainInterface.storyboard`

**Objective-C**<br>
- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

## Notification push interactive {#interactive-push-notification}

Les notifications push peuvent répondre aux actions des utilisateurs à l'intérieur d'une extension de contenu d'application. Pour les utilisateurs exécutant iOS 12 ou une version ultérieure, cela signifie que vous pouvez transformer vos notifications push en messages entièrement interactifs ! Cela offre une option intéressante pour introduire de l'interactivité dans vos promotions et applications. Par exemple, votre notification push peut inclure un jeu auquel les utilisateurs peuvent jouer, une roue de la chance pour des réductions, ou un bouton « j'aime » pour enregistrer une annonce ou une chanson.

L'exemple suivant montre une notification push dans laquelle les utilisateurs peuvent jouer à un jeu de correspondance à l'intérieur de la notification étendue.

![Un diagramme illustrant les différentes phases d'une notification push interactive. Une séquence montre un utilisateur appuyant sur une notification push qui affiche un jeu de correspondance interactif.]({% image_buster /assets/img/push_implementation_guide/push12.png %}){: style="border:0"}

### Configuration du tableau de bord {#dashboard-configuration}

Pour créer une notification push interactive, vous devez définir une vue personnalisée dans votre tableau de bord.

1. Depuis la page **Campaigns**, cliquez sur **Create Campaign** pour lancer une nouvelle campagne de notification push.
2. Dans l'onglet **Compose**, activez **Notification Buttons**.
3. Saisissez une catégorie iOS personnalisée dans le champ **iOS Notification Category**.
4. Dans le `.plist` de votre cible Notification Content Extension, définissez l'attribut `UNNotificationExtensionCategory` sur votre catégorie iOS personnalisée. La valeur indiquée ici doit correspondre à ce qui est défini dans le tableau de bord de Braze sous **iOS Notification Category**.
5. Définissez la clé `UNNotificationExtensionInteractionEnabled` sur `true` pour activer les interactions utilisateur dans une notification push.

![Les options de bouton de notification disponibles dans les paramètres du composeur de messages push.]({% image_buster /assets/img/push_implementation_guide/push16.png %}){: style="max-width:75%;border:0;margin-top:10px"}
![Un fichier plist affichant NSExtension avec UNNotificationExtensionCategory défini sur « your_custom_category », UNNotificationExtensionDefaultContentHidden défini sur 1 et UNNotificationExtensionInitialContentSizeRatio défini sur 1.]({% image_buster /assets/img/push_implementation_guide/push17.png %}){: style="max-width:75%;border:0;margin-top:10px"}

## Notifications push personnalisées {#personalized-push-notifications}

![Deux iPhones affichés côte à côte. Le premier iPhone montre la vue réduite du message push. Le second iPhone montre la version étendue du message push affichant une capture de la progression dans un cours, le nom de la prochaine session et la date limite pour la compléter.]({% image_buster /assets/img/push_implementation_guide/push6.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

Les notifications push peuvent afficher des informations spécifiques à l'utilisateur au sein d'une extension de contenu. Cela vous permet de créer du contenu push centré sur l'utilisateur, comme l'ajout d'une option pour partager votre progression sur différentes plateformes, afficher des réalisations débloquées ou présenter des listes de contrôle d'onboarding. Cet exemple montre une notification push affichée à un utilisateur après qu'il a terminé une tâche spécifique dans le cours d'apprentissage Braze. En développant la notification, l'utilisateur peut voir sa progression dans son parcours d'apprentissage. Les informations fournies ici sont spécifiques à l'utilisateur et peuvent être déclenchées lorsqu'une session est terminée ou qu'une action utilisateur spécifique est effectuée en utilisant un déclencheur API.

### Configuration du tableau de bord

Pour créer une notification push personnalisée, vous devez définir une vue personnalisée dans votre tableau de bord.

1. Depuis la page **Campaigns**, cliquez sur **Create Campaign** pour démarrer une nouvelle campagne de notification push.
2. Dans l'onglet **Compose**, activez **Notification Buttons**.
3. Saisissez une catégorie iOS personnalisée dans le champ **iOS Notification Category**.
4. Dans l'onglet **Settings**, créez des paires clé-valeur en utilisant le Liquid standard. Définissez les attributs utilisateur appropriés que vous souhaitez afficher dans le message. Ces vues peuvent être personnalisées en fonction d'attributs utilisateur spécifiques d'un profil utilisateur donné.
5. Dans le `.plist` de votre cible Notification Content Extension, définissez l'attribut `UNNotificationExtensionCategory` sur votre catégorie iOS personnalisée. La valeur indiquée ici doit correspondre à ce qui est défini dans le tableau de bord de Braze sous **iOS Notification Category**.

![Quatre ensembles de paires clé-valeur, où « next_session_name » et « next_session_complete_date » sont définis comme propriété de déclencheur API à l'aide de Liquid, et « completed_session count » et « total_session_count » sont définis comme attribut utilisateur personnalisé à l'aide de Liquid.]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

### Gestion des paires clé-valeur {#handling-key-value-pairs}

La méthode `didReceive` est appelée lorsque l'extension d'application de contenu de notification a reçu une notification. Cette méthode se trouve dans le `NotificationViewController`. Les paires clé-valeur fournies dans le tableau de bord sont représentées dans le code via l'utilisation d'un dictionnaire `userInfo`.

#### Analyse des paires clé-valeur à partir des notifications push {#parsing-key-value-pairs-from-push-notifications}

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

## Notification push de capture d'informations {#information-capture-push-notification}

Les notifications push peuvent capturer des informations utilisateur dans une extension de contenu d'application, repoussant les limites de ce qui est possible avec une notification push. Demander des informations aux utilisateurs via les notifications push permet non seulement de recueillir des données de base comme le nom ou l'e-mail, mais aussi d'inviter les utilisateurs à soumettre des commentaires ou à compléter un profil utilisateur inachevé.

{% alert tip %}
Pour plus d'informations, consultez [Enregistrement des données de notification push]({{site.baseurl}}/developer_guide/analytics/logging_channel_data/push_notifications).
{% endalert %}

Dans le flux suivant, la vue personnalisée peut répondre aux changements d'état. Ces composants de changement d'état sont représentés dans chaque image.

1. L'utilisateur reçoit une notification push.
2. La notification push est ouverte. Une fois développée, elle invite l'utilisateur à fournir des informations. Dans cet exemple, l'adresse e-mail de l'utilisateur est demandée, mais vous pouvez demander tout type d'information.
3. L'information est fournie et, si elle est dans le format attendu, le bouton d'inscription s'affiche.
3. La vue de confirmation s'affiche et la notification push est fermée.


### Configuration du tableau de bord

Pour créer une notification push de capture d'informations, vous devez définir une vue personnalisée dans votre tableau de bord.

1. Depuis la page **Campaigns**, cliquez sur **Create Campaign** pour lancer une nouvelle campagne de notification push.
2. Dans l'onglet **Compose**, activez **Notification Buttons**.
3. Saisissez une catégorie iOS personnalisée dans le champ **iOS Notification Category**.
4. Dans l'onglet **Settings**, créez des paires clé-valeur en utilisant le Liquid standard. Définissez les attributs utilisateur appropriés que vous souhaitez que le message affiche.
5. Dans le fichier `.plist` de votre cible Notification Content Extension, définissez l'attribut `UNNotificationExtensionCategory` sur votre catégorie iOS personnalisée. La valeur fournie ici doit correspondre à ce qui est défini dans le tableau de bord de Braze sous **iOS Notification Category**.

Comme illustré dans l'exemple, vous pouvez également inclure une image dans votre notification push. Pour cela, vous devez intégrer les [notifications enrichies]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift), définir le style de notification dans votre campagne sur Rich Notification, et inclure une image de push riche.

![Un message push avec trois ensembles de paires clé-valeur. 1. « Braze_id » défini comme un appel Liquid pour récupérer l'identifiant Braze. 2. « cert_title » défini comme « Braze Marketer Certification ». 3. « Cert_description » défini comme « Certified Braze marketers drive... ».]({% image_buster /assets/img/push_implementation_guide/push9.png %})

### Gestion des actions des boutons {#handling-button-actions}

Chaque bouton d'action est identifié de manière unique. Le code vérifie si l'identifiant de votre réponse est égal à l'`actionIdentifier` et, si c'est le cas, sait que l'utilisateur a cliqué sur le bouton d'action.

**Gestion des réponses aux boutons d'action des notifications push**<br>

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

### Fermeture des notifications push {#dismissing-pushes}

Les notifications push peuvent être automatiquement fermées par un appui sur un bouton d'action. Il existe trois options de fermeture de notification push préconstruites que nous recommandons :

1. `completion(.dismiss)` - Ferme la notification
2. `completion(.doNotDismiss)` - La notification reste ouverte
3. `completion(.dismissAndForward)` - La notification push se ferme et l'utilisateur est redirigé vers l'application