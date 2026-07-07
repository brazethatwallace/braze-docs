## À propos des Content Cards React Native {#about-react-native-content-cards}

Les SDK Braze incluent un flux de cartes par défaut pour vous permettre de démarrer avec les Content Cards. Pour afficher le flux de cartes, vous pouvez utiliser la méthode `Braze.launchContentCards()`. Le flux de cartes par défaut inclus avec le SDK Braze gère l'ensemble du suivi analytique, des masquages et du rendu des Content Cards d'un utilisateur.

{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Méthodes pour les cartes {#cards-methods}

Pour créer votre propre interface utilisateur, vous pouvez obtenir une liste des cartes disponibles et écouter les mises à jour des cartes :

```javascript
// Set initial cards
const [cards, setCards] = useState([]);

// Listen for updates as a result of card refreshes, such as:
// a new session, a manual refresh with `requestContentCardsRefresh()`, or after the timeout period
Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, async (update) => {
    setCards(update.cards);
});

// Manually trigger a refresh of cards
Braze.requestContentCardsRefresh();
```

{% alert important %}
Si vous choisissez de créer votre propre interface utilisateur pour afficher les cartes, vous devez appeler `logContentCardImpression` afin de recevoir les analyses pour ces cartes. Ceci inclut les cartes `control`, qui doivent faire l'objet d'un suivi même si elles ne sont pas affichées à l'utilisateur.
{% endalert %}

Vous pouvez utiliser ces méthodes supplémentaires pour créer un flux de Content Cards personnalisé dans votre application :

| Méthode                                  | Description                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `launchContentCards()`                   | Lance l'élément d'interface utilisateur Content Cards.                                                                 |
| `requestContentCardsRefresh()`           | Demande les dernières Content Cards au serveur du SDK Braze. La liste de cartes qui en résulte est transmise à chacun des [récepteurs d'événements de carte de contenu](#reactnative_cards-methods) précédemment enregistrés. |
| `getContentCards()`                      | Récupère les Content Cards du SDK Braze. Ceci renvoie une promesse qui se résout avec la dernière liste de cartes du serveur. |
| `getCachedContentCards()`                | Renvoie le tableau de Content Cards le plus récent du cache.                                            |
| `logContentCardClicked(cardId)`          | Enregistre un clic pour l'ID de carte de contenu donné. Cette méthode est uniquement utilisée pour les analyses. Pour exécuter l'action de clic, appelez `processContentCardClickAction(cardId)` en plus.                                                        |
| `logContentCardImpression(cardId)`       | Enregistre une impression pour l'ID de carte de contenu donné.                                                      |
| `logContentCardDismissed(cardId)`        | Enregistre un rejet pour l'ID de carte de contenu donné.                                                        |
| `processContentCardClickAction(cardId)`  | Effectue l'action d'une carte particulière.                                                               |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cards methods" }

## Types de cartes et propriétés {#card-types-and-properties}

Le modèle de données Content Cards est disponible dans le SDK React Native et propose les types de cartes Content Cards suivants : [Image seule](#image-only), [Image légendée](#captioned-image) et [Classique](#classic). Il existe également un type de carte spécial [Contrôle](#control), qui est renvoyé aux utilisateurs faisant partie du groupe de contrôle pour une carte donnée. Chaque type hérite des propriétés communes d'un modèle de base en plus de ses propres propriétés uniques.

{% alert tip %}
Pour une référence complète du modèle de données Content Cards, consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard).
{% endalert %}

### Modèle de carte de base {#base-card-model}

Le modèle de carte de base fournit un comportement fondamental pour toutes les cartes.

| Propriété      | Description                                                                                                            |
|--------------|------------------------------------------------------------------------------------------------------------------------|
| `id`          | L'ID de la carte défini par Braze.                                                                                            |
| `created`     | L'horodatage UNIX du moment de création de la carte depuis Braze.                                                             |
| `expiresAt`   | L'horodatage UNIX du moment d'expiration de la carte. Lorsque la valeur est inférieure à 0, cela signifie que la carte n'expire jamais.      |
| `viewed`      | Indique si la carte est lue ou non par l'utilisateur. Ceci n'enregistre pas les analyses.                                           |
| `clicked`     | Indique si la carte a été cliquée par l'utilisateur.                                                                         |
| `pinned`      | Indique si la carte est épinglée.                                                                                            |
| `dismissed`   | Indique si l'utilisateur a fermé cette carte. Marquer comme rejetée une carte qui l'a déjà été n'aura aucun effet. |
| `dismissible` | Détermine si la carte peut être rejetée par l'utilisateur.                                                                           |
| `url`         | (Facultatif) La chaîne de caractères de l'URL associée à l'action de clic sur la carte.                                                       |
| `openURLInWebView` | Indique si les URL de cette carte doivent être ouvertes dans le WebView de Braze ou non.                                            |
| `isControl`   | Indique si cette carte est une carte de contrôle. Les cartes de contrôle ne doivent pas être affichées à l'utilisateur.                                |
| `extras`      | Le mappage des suppléments clé-valeur pour cette carte.                                                                             |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Base card model" }

Pour une référence complète de la carte de base, consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct).

### Image seule {#image-only}

Les cartes image seule sont des images cliquables en taille réelle.

| Propriété           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `type`             | Le type de Content Card, `IMAGE_ONLY`.                                                                              |
| `image`            | L'URL de l'image de la carte.                                                                                      |
| `imageAspectRatio` | Le rapport hauteur/largeur de l'image de la carte. Il sert d'indication avant que le chargement de l'image ne soit terminé. Veuillez noter que la propriété peut ne pas être fournie dans certaines circonstances. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Image only" }

Pour une référence complète de la carte image seule, consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct).

### Image légendée {#captioned-image}

Les cartes d'images légendées sont des images cliquables en taille réelle accompagnées d'un texte descriptif.

| Propriété           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `type`             | Le type de Content Card, `CAPTIONED`.                                                                               |
| `image`            | L'URL de l'image de la carte.                                                                                      |
| `imageAspectRatio` | Le rapport hauteur/largeur de l'image de la carte. Il sert d'indication avant que le chargement de l'image ne soit terminé. Veuillez noter que la propriété peut ne pas être fournie dans certaines circonstances. |
| `title`            | Le texte du titre de la carte.                                                                                      |
| `cardDescription`  | Le texte de description de la carte.                                                                                |
| `domain`           | (Facultatif) Le texte du lien pour l'URL de propriété, par exemple, `"braze.com/resources/"`. Il peut être affiché sur l'interface utilisateur de la carte pour indiquer l'action ou la direction du clic sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Captioned image" }

Pour une référence complète de la carte d'image légendée, consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct).

### Classique {#classic}

Les cartes classiques comportent un titre, une description et une image facultative à gauche du texte.

| Propriété           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `type`             | Le type de Content Card, `CLASSIC`.                                                                                 |
| `image`            | (Facultatif) L'URL de l'image de la carte.                                                                           |
| `title`            | Le texte du titre de la carte.                                                                                      |
| `cardDescription`  | Le texte de description de la carte.                                                                                |
| `domain`           | (Facultatif) Le texte du lien pour l'URL de propriété, par exemple, `"braze.com/resources/"`. Il peut être affiché sur l'interface utilisateur de la carte pour indiquer l'action ou la direction du clic sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Classic" }

Pour une référence complète de la Content Card classique (annonce textuelle), consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct). Pour la carte image classique (nouvelles brèves), consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct).

### Contrôle {#control}

Les cartes de contrôle incluent toutes les propriétés de base, avec quelques différences importantes. Et surtout :

- La propriété `isControl` est garantie à `true`.
- La propriété `extras` est garantie vide.

Pour une référence complète de la carte de contrôle, consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-control-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control-swift.struct).