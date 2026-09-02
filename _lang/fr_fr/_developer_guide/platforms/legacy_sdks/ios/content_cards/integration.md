---
nav_title: Intégration
article_title: Intégration du contrôleur de vue Content Cards pour iOS
platform: iOS
page_order: 1
description: "Cet article de référence couvre les étapes d'intégration, les modèles de données et les propriétés spécifiques aux cartes disponibles pour votre application iOS."
channel:
  - content cards
search_rank: 3
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Intégration des Content Cards {#content-card-integration}

## Modèle de données des Content Cards {#content-cards-data-model}

Le modèle de données des Content Cards est disponible dans le SDK iOS.

### Obtenir les données {#getting-the-data}

Pour accéder au modèle de données des Content Cards, abonnez-vous aux événements de mise à jour des Content Cards :

{% tabs %}
{% tab OBJECTIVE-C %}
```objc
// Subscribe to Content Cards updates
// Note: you should remove the observer where appropriate
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(contentCardsUpdated:)
                                             name:ABKContentCardsProcessedNotification
                                           object:nil];
```

```objc
// Called when Content Cards are refreshed (via `requestContentCardsRefresh`)
- (void)contentCardsUpdated:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification.userInfo[ABKContentCardsProcessedIsSuccessfulKey] boolValue];
  if (updateIsSuccessful) {
    // get the cards using [[Appboy sharedInstance].contentCardsController getContentCards];
  }
}
```
{% endtab %}
{% tab swift %}
```swift
// Subscribe to content card updates
// Note: you should remove the observer where appropriate
NotificationCenter.default.addObserver(self, selector:
  #selector(contentCardsUpdated),
  name:NSNotification.Name.ABKContentCardsProcessed, object: nil)
```

```swift
// Called when the Content Cards are refreshed (via `requestContentCardsRefresh`)
@objc private func contentCardsUpdated(_ notification: Notification) {
  if let updateIsSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] as? Bool {
    if (updateIsSuccessful) {
      // get the cards using Appboy.sharedInstance()?.contentCardsController.contentCards
    }
  }
}
```
{% endtab %}
{% endtabs %}

Si vous souhaitez modifier les données de la carte après qu'elles ont été envoyées par Braze, nous vous recommandons de stocker localement une copie complète des données de la carte, de mettre les données à jour et de les afficher vous-même. Les cartes sont accessibles via [`ABKContentCardsController`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_cards_controller.html).

## Modèle de carte de contenu {#content-card-model}

Braze propose trois types de Content Cards : bannière, image légendée et classique. Chaque type hérite des propriétés communes d'une classe `ABKContentCard` de base et possède les propriétés supplémentaires suivantes.

### Propriétés du modèle de carte de contenu de base — ABKContentCard {#base-content-card-model-properties-abkcontentcard}

| Propriété | Description |
|---|---|
| `idString` | (Lecture seule) L'ID de la carte défini par Braze. |
| `viewed` | Cette propriété indique si l'utilisateur a vu la carte ou non. |
| `created` | (Lecture seule) Cette propriété est l'horodatage unix de la date de création de la carte par Braze. |
| `expiresAt` | (Lecture seule) Cette propriété est l'horodatage unix de la date d'expiration de la carte. |
| `dismissible` | Cette propriété indique si l'utilisateur peut fermer la carte. |
| `pinned` | Cette propriété indique si la carte a été définie comme « épinglée » dans le tableau de bord. |
| `dismissed` | Cette propriété indique si l'utilisateur a fermé la carte. |
| `url` | L'URL qui sera ouverte après un clic sur la carte. Il peut s'agir d'une URL HTTP(S) ou d'une URL de protocole. |
| `openURLInWebView` | Cette propriété détermine si l'URL sera ouverte dans l'application ou dans un navigateur web externe. |
| `extras` | Un `NSDictionary` facultatif de valeurs `NSString`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Base Content Card model properties - ABKContentCard" }

### Propriétés de la CCI or carte de contenu de type bannière or carte de contenu de type bannière — ABKBannerContentCard {#banner-content-card-properties-abkbannercontentcard}

| Propriété | Description |
|---|---|
| `image` | Cette propriété est l'URL de l'image de la carte. |
| `imageAspectRatio` | Cette propriété est le rapport hauteur/largeur de l'image de la carte et sert d'indication avant que le chargement de l'image ne soit terminé. Notez que cette propriété peut ne pas être fournie dans certaines circonstances. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CCI or carte de contenu de type bannière or carte de contenu de type bannière properties - ABKBannerContentCard" }

### Propriétés de la carte de contenu avec image légendée — ABKCaptionedImageCard {#captioned-image-content-card-properties-abkcaptionedimagecard}

| Propriété | Description |
|---|---|
| `image` | Cette propriété est l'URL de l'image de la carte. |
| `imageAspectRatio` | Cette propriété est le rapport hauteur/largeur de l'image de la carte. |
| `title` | Le texte du titre de la carte. |
| `cardDescription` | Le texte du corps de la carte. |
| `domain` | Le texte du lien pour l'URL de la propriété, par exemple @"blog.braze.com". Il peut être affiché dans l'interface de la carte pour indiquer l'action et la direction du clic sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Captioned image Content Card properties - ABKCaptionedImageCard" }

### Propriétés de la carte de contenu classique — ABKClassicContentCard {#classic-content-card-properties-abkclassiccontentcard}

| Propriété | Description |
|---|---|
| `image` | (Facultatif) Cette propriété est l'URL de l'image de la carte. |
| `title` | Le texte du titre de la carte. |
| `cardDescription` | Le texte du corps de la carte. |
| `domain` | Le texte du lien pour l'URL de la propriété, par exemple @"blog.braze.com". Il peut être affiché dans l'interface de la carte pour indiquer l'action et la direction du clic sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Classic Content Card properties - ABKClassicContentCard" }

## Méthodes de carte {#card-methods}

| Méthode | Description |
|---|---|
| `logContentCardImpression` | Enregistrer manuellement une impression sur Braze pour une carte particulière. |
| `logContentCardClicked` | Enregistrer manuellement un clic sur Braze pour une carte particulière. Le SDK n'enregistre un clic de carte que lorsque la carte possède la propriété `url` avec une valeur valide. |
| `logContentCardDismissed` | Enregistrer manuellement une fermeture sur Braze pour une carte particulière. Le SDK n'enregistre une fermeture de carte que si la propriété `dismissed` de la carte n'est pas déjà définie sur `true`. |
| `isControlCard` | Déterminer si une carte est la carte de contrôle pour un test A/B. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Card methods" }

Pour plus de détails, reportez-vous à la [documentation de référence de classe](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html).

## Intégration du contrôleur de vue des Content Cards {#content-cards-view-controller-integration}

Les Content Cards peuvent être intégrées avec deux contextes de contrôleur de vue : navigation ou modal.

### Contexte de navigation {#navigation-context}

Exemple d'ajout d'une instance `ABKContentCardsTableViewController` dans un contrôleur de navigation :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKContentCardsTableViewController *contentCards = [[ABKContentCardsTableViewController alloc] init];
contentCards.title = @"Content Cards Title";
contentCards.disableUnreadIndicator = YES;
[self.navigationController pushViewController:contentCards animated:YES];
```

{% endtab %}
{% tab swift %}

```swift
let contentCards = ABKContentCardsTableViewController()
contentCards.title = "Content Cards Title"
contentCards.disableUnreadIndicator = true
navigationController?.pushViewController(contentCards, animated: true)
```

{% endtab %}
{% endtabs %}

{% alert note %}
Pour personnaliser le titre de la barre de navigation, définissez la propriété de titre du `navigationItem` de l'instance `ABKContentCardsTableViewController`.
{% endalert %}

### Contexte modal {#modal-context}

Cette fenêtre modale est utilisée pour présenter le contrôleur de vue dans une vue modale, avec une barre de navigation en haut et un bouton **Done** sur le côté de la barre.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKContentCardsViewController *contentCards = [[ABKContentCardsViewController alloc] init];
contentCards.contentCardsViewController.title = @"Content Cards Title";
contentCards.contentCardsViewController.disableUnreadIndicator = YES;
[self.navigationController presentViewController:contentCards animated:YES completion:nil];
```

{% endtab %}
{% tab swift %}

```swift
let contentCards = ABKContentCardsViewController()
contentCards.contentCardsViewController.title = "Content Cards Title"
contentCards.contentCardsViewController.disableUnreadIndicator = true
self.present(contentCards, animated: true, completion: nil)
```

{% endtab %}
{% endtabs %}

Pour des exemples de contrôleurs de vue, consultez notre [exemple d'application Content Cards](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp).

{% alert note %}
Pour personnaliser l'en-tête, définissez la propriété de titre du `navigationItem` appartenant à l'instance `ABKContentCardsTableViewController` intégrée dans l'instance parente `ABKContentCardsViewController`.
{% endalert %}