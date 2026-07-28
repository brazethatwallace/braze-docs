## À propos des Content Cards .NET MAUI {#about-net-maui-content-cards}

Le SDK Braze .NET MAUI (anciennement Xamarin) comprend un flux de cartes par défaut pour vous aider à démarrer avec les Content Cards. Le flux de cartes par défaut inclus avec le SDK Braze gère l'ensemble du suivi analytique, des rejets et du rendu des Content Cards d'un utilisateur.

{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## Types et propriétés des cartes {#card-types-and-properties}

Le SDK Braze .NET MAUI propose trois types de Content Cards uniques qui partagent un modèle de base : [Bannière](#xamarin_banner), [Image avec légende](#xamarin_captioned-image) et [Classique](#xamarin_classic). Chaque type hérite des propriétés communes d'un modèle de base et possède les propriétés supplémentaires suivantes.

### Modèle de carte de base {#base-card-model}

| Propriété | Description |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
| `idString` | L'ID de la carte défini par Braze. |
| `created` | L'horodatage UNIX du moment de création de la carte depuis Braze. |
| `expiresAt` | L'horodatage UNIX du moment d'expiration de la carte. Lorsque la valeur est inférieure à 0, cela signifie que la carte n'expire jamais. |
| `viewed` | Indique si la carte est lue ou non par l'utilisateur. Ceci n'enregistre pas d'analyse. |
| `clicked` | Indique si la carte a été cliquée par l'utilisateur. |
| `pinned` | Indique si la carte est épinglée. |
| `dismissed` | Indique si l'utilisateur a rejeté cette carte. Marquer comme rejetée une carte qui l'a déjà été sera sans effet. |
| `dismissible` | Indique si la carte peut être rejetée par l'utilisateur. |
| `urlString` | (Facultatif) La chaîne de caractères d'URL associée à l'action de clic sur la carte. |
| `openUrlInWebView` | Indique si les URL de cette carte doivent être ouvertes dans la WebView Braze ou non. |
| `isControlCard` | Indique si cette carte est une carte de contrôle. Les cartes de contrôle ne doivent pas être affichées à l'utilisateur. |
| `extras` | Le mappage des suppléments clé-valeur pour cette carte. |
| `isTest` | Indique si cette carte est une carte de test. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Base card model" }

Pour une référence complète de la carte de base, consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct).

### Bannière {#banner}

Les cartes de type bannière sont des images cliquables en taille réelle.

| Propriété | Description |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `image` | L'URL de l'image de la carte. |
| `imageAspectRatio` | Le rapport hauteur/largeur de l'image de la carte. Il sert d'indication avant que le chargement de l'image ne soit terminé. Notez que cette propriété peut ne pas être fournie dans certaines circonstances. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Banner" }

Pour une référence complète de la carte bannière, consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct) (désormais renommée en image uniquement).

### Image avec légende {#captioned-image}

Les cartes d'image avec légende sont des images cliquables en taille réelle accompagnées d'un texte descriptif.

| Propriété | Description |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `image` | L'URL de l'image de la carte. |
| `imageAspectRatio` | Le rapport hauteur/largeur de l'image de la carte. Il sert d'indication avant que le chargement de l'image ne soit terminé. Notez que cette propriété peut ne pas être fournie dans certaines circonstances. |
| `title` | Le texte du titre de la carte. |
| `cardDescription` | Le texte de description de la carte. |
| `domain` | (Facultatif) Le texte du lien pour l'URL de propriété, par exemple, `"braze.com/resources/"`. Il peut être affiché sur l'interface utilisateur de la carte pour indiquer l'action ou la direction du clic sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Captioned image" }

Pour une référence complète de la carte d'image avec légende, consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct).

### Classique {#classic}

Les cartes classiques comportent un titre, une description et une image facultative avant le texte.

| Propriété | Description |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `image` | (Facultatif) L'URL de l'image de la carte. |
| `title` | Le texte du titre de la carte. |
| `cardDescription` | Le texte de description de la carte. |
| `domain` | (Facultatif) Le texte du lien pour l'URL de propriété, par exemple, `"braze.com/resources/"`. Il peut être affiché sur l'interface utilisateur de la carte pour indiquer l'action ou la direction du clic sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Classic" }

Pour une référence complète de la Content Card classique (annonce textuelle), consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct). Pour une référence complète de la carte d'image classique (courte nouvelle), consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct).

## Méthodes de carte {#card-methods}

Vous pouvez utiliser ces méthodes supplémentaires pour créer un flux de Content Cards personnalisé dans votre application :

| Méthode | Description |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `requestContentCardsRefresh()` | Demande les dernières Content Cards au serveur du SDK Braze. |
| `getContentCards()` | Récupère les Content Cards depuis le SDK Braze. Cela renverra la dernière liste de cartes du serveur. |
| `logContentCardClicked(cardId)` | Enregistre un clic pour l'ID de Content Card donné. Cette méthode est uniquement utilisée pour l'analytique. |
| `logContentCardImpression(cardId)` | Enregistre une impression pour l'ID de Content Card donné. |
| `logContentCardDismissed(cardId)` | Enregistre un rejet pour l'ID de Content Card donné. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Card methods" }