## À propos des cartes de contenu Flutter {#about-flutter-content-cards}

Le SDK Braze comprend un flux de cartes par défaut pour vous permettre de démarrer avec les Content Cards. Pour afficher ce flux, utilisez la méthode `braze.launchContentCards()`. Le flux de cartes par défaut inclus avec le SDK Braze gère l'ensemble du suivi analytique, des masquages et du rendu des Content Cards d'un utilisateur.

{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Méthodes de carte {#card-methods}

Vous pouvez utiliser ces méthodes supplémentaires pour créer un flux de Content Cards personnalisé dans votre application, disponibles sur l'[interface publique du plugin](https://github.com/braze-inc/braze-flutter-sdk/blob/master/lib/braze_plugin.dart) :

| Méthode                                         | Description                                                                                            |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `braze.requestContentCardsRefresh()`     | Demande les dernières Content Cards au serveur du SDK Braze.                                           |
| `braze.logContentCardClicked(contentCard)`    | Enregistre un clic pour l'objet Content Card donné.                                                            |
| `braze.logContentCardImpression(contentCard)` | Enregistre une impression pour l'objet Content Card donné.                                                      |
| `braze.logContentCardDismissed(contentCard)`  | Enregistre un masquage pour l'objet Content Card donné.                                                        |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Méthodes de carte" }

## Réception des données de Content Cards {#receiving-content-card-data}

Pour recevoir des données de Content Cards dans votre application Flutter, le `BrazePlugin` prend en charge l'envoi de données de Content Cards à l'aide de [Dart Streams](https://dart.dev/tutorials/language/streams).

L'[objet](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazeContentCard-class.html) `BrazeContentCard` prend en charge un sous-ensemble de champs disponibles dans les objets du modèle natif, notamment `description`, `title`, `image`, `url`, `extras`, et plus encore.

### Écouter les données de Content Cards dans la couche Dart {#listen-for-content-card-data-in-the-dart-layer}

Pour recevoir les données de Content Cards dans la couche Dart, utilisez le code ci-dessous pour créer un `StreamSubscription` et appeler `braze.subscribeToContentCards()`. N'oubliez pas d'appeler `cancel()` sur l'abonnement au flux lorsqu'il n'est plus nécessaire.

```dart
// Create stream subscription
StreamSubscription contentCardsStreamSubscription;

contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Handle Content Cards
}

// Cancel stream subscription
contentCardsStreamSubscription.cancel();
```

Pour un exemple, consultez [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) dans l'application exemple du SDK Flutter de Braze.

### Transférer les données de Content Cards depuis la couche native iOS {#forward-content-card-data-from-the-native-ios-layer}

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

Les données de Content Cards sont automatiquement transférées depuis les couches natives Android et iOS. Aucune configuration supplémentaire n'est requise.

{% endtab %}
{% tab Flutter SDK 17.1.0 et antérieur %}

Si vous utilisez le SDK Flutter 17.1.0 ou une version antérieure, le transfert des données de Content Cards depuis la couche native iOS nécessite une configuration manuelle. Votre application contient probablement un rappel `contentCards.subscribeToUpdates` qui appelle `BrazePlugin.processContentCards(contentCards)`. Pour migrer vers le SDK Flutter 18.0.0, supprimez l'appel à `BrazePlugin.processContentCards(_:)` — le transfert des données est désormais géré automatiquement.

Pour un exemple, consultez [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) dans l'application exemple du SDK Flutter de Braze.

{% endtab %}
{% endtabs %}

#### Rejouer le rappel pour les Content Cards {#replaying-the-callback-for-content-cards}

Pour stocker les Content Cards déclenchées avant que le rappel soit disponible et les rejouer une fois celui-ci défini, ajoutez l'entrée suivante à la map `customConfigs` lors de l'initialisation du `BrazePlugin` :
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
