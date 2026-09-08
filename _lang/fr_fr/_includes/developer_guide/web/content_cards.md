{% multi_lang_include archive/web-v4-rename.md %}

## Prérequis {#prerequisites}

Avant de pouvoir utiliser les Content Cards, vous devez [intégrer le SDK Web de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) dans votre application. Cependant, aucune configuration supplémentaire n'est requise. Pour créer votre propre interface utilisateur, consultez le [guide de personnalisation des Content Cards]({{site.baseurl}}/developer_guide/content_cards).

{% alert note %}
Certains bloqueurs de publicités et extensions de confidentialité de navigateur peuvent bloquer le script du SDK Web de Braze ou les requêtes réseau associées, ce qui peut empêcher le chargement des Content Cards. Si vous utilisez la méthode d'intégration par CDN, envisagez de passer à la [méthode d'intégration par NPM]({{site.baseurl}}/developer_guide/sdk_integration/?subtab=package%20manager&sdktab=web), qui stocke les bibliothèques du SDK localement sur votre site web et peut éviter certains problèmes liés aux bloqueurs de publicités.
{% endalert %}

## Interface utilisateur standard du flux {#standard-feed-ui}

Pour utiliser l'interface utilisateur intégrée des Content Cards, vous devez spécifier où afficher le flux sur votre site web.

Dans cet exemple, nous avons un `<div id="feed"></div>` dans lequel nous souhaitons placer le flux de Content Cards. Nous utiliserons trois boutons pour masquer, afficher ou basculer (masquer ou afficher selon l'état actuel) le flux.

```html

<button id="toggle" type="button">Toggle Cards Feed</button>
<button id="hide" type="button">Hide Cards Feed</button>
<button id="show" type="button">Show Cards Feed</button>

<nav>
    <h1>Your Personalized Feed</h1>
    <div id="feed"></div>
</nav>

<script>
   const toggle = document.getElementById("toggle");
   const hide = document.getElementById("hide");
   const show = document.getElementById("show");
   const feed = document.getElementById("feed");

   toggle.onclick = function(){
      braze.toggleContentCards(feed);
   }

   hide.onclick = function(){
      braze.hideContentCards();
   }

   show.onclick = function(){
      braze.showContentCards(feed);
   }
</script>
```

Lorsque vous utilisez les méthodes `toggleContentCards(parentNode, filterFunction)` et `showContentCards(parentNode, filterFunction)`, si aucun argument n'est fourni, toutes les Content Cards seront affichées dans une barre latérale à position fixe sur la page. Sinon, le flux sera placé dans l'option `parentNode` spécifiée.

| Paramètres | Description |
|---|---|
| `parentNode` | Le nœud HTML dans lequel afficher les Content Cards. Si le nœud parent possède déjà une vue de Content Cards Braze en tant que descendant direct, les Content Cards existantes seront remplacées. Par exemple, vous devez passer `document.querySelector(".my-container")`. |
| `filterFunction` | Une fonction de filtre ou de tri pour les cartes affichées dans cette vue. Invoquée avec le tableau d'objets `Card`, triés par `{pinned, date}`. Cette fonction doit retourner un tableau trié d'objets `Card` à afficher pour cet utilisateur. Si elle est omise, toutes les cartes seront affichées. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Interface utilisateur standard du flux" }

[Consultez la documentation de référence du SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards) pour plus d'informations sur le basculement des Content Cards.

## Tester les Content Cards sur le web {#testing-content-cards-on-the-web}

Vous pouvez tester votre intégration des Content Cards à l'aide des outils de développement de votre navigateur.

1. Créez une campagne de Content Cards et ciblez votre utilisateur test.
2. Connectez-vous au site web qui contient votre intégration du SDK Web.
3. Ouvrez la console de votre navigateur. Pour Chrome, faites un clic droit sur la page, sélectionnez **Inspecter**, puis sélectionnez l'onglet **Console**.
4. Exécutez ces commandes dans la console :
   - `window.braze.getCachedContentCards()`
   - `window.braze.toggleContentCards()`

## Types de cartes et propriétés {#card-types-and-properties}

Le modèle de donnée des Content Cards est disponible dans le SDK Web et propose les types de Content Cards suivants : [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) et [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html). Chaque type hérite des propriétés communes d'un modèle de base [Card](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) et possède les propriétés supplémentaires suivantes.

{% alert tip %}
Pour enregistrer les données des Content Cards, consultez la section [Enregistrement des analyses]({{site.baseurl}}/developer_guide/content_cards/logging_analytics).
{% endalert %}

### Modèle de carte de base {#base-card-model}

Toutes les Content Cards partagent ces propriétés communes :

| Propriété | Description |
|---|---|
| `expiresAt` | L'horodatage UNIX de l'expiration de la carte. |
| `extras` | (Facultatif) Données de paire clé-valeur formatées en objet chaîne de caractères avec une valeur de type chaîne de caractères. |
| `id` | (Facultatif) L'identifiant de la carte. Il sera renvoyé à Braze avec les événements à des fins d'analyse. |
| `pinned` | Cette propriété indique si la carte a été définie comme « épinglée » dans le tableau de bord. |
| `updated` | L'horodatage UNIX de la dernière modification de cette carte. |
| `viewed` | Cette propriété indique si l'utilisateur a consulté la carte ou non. |
| `isControl` | Cette propriété est `true` lorsqu'une carte est un groupe de « contrôle » dans un test A/B. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modèle de carte de base" }

### Image uniquement {#image-only}

Les cartes [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) sont des images plein format cliquables.

| Propriété | Description |
|---|---|
| `aspectRatio` | Le rapport hauteur/largeur de l'image de la carte, servant d'indication avant la fin du chargement de l'image. Notez que cette propriété peut ne pas être fournie dans certaines circonstances. |
| `categories` | Cette propriété sert uniquement à l'organisation dans votre implémentation personnalisée ; ces catégories peuvent être définies dans le compositeur du tableau de bord. |
| `clicked` | Cette propriété indique si cette carte a déjà été cliquée sur cet appareil. |
| `created` | L'horodatage UNIX de la création de la carte depuis Braze. |
| `dismissed` | Cette propriété indique si cette carte a été fermée. |
| `dismissible` | Cette propriété indique si l'utilisateur peut fermer la carte, la retirant de la vue. |
| `imageUrl` | L'URL de l'image de la carte. |
| `linkText` | Le texte d'affichage pour l'URL. |
| `url` | L'URL qui sera ouverte après un clic sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Image uniquement" }

### Image avec légende {#captioned-image}

Les cartes [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) sont des images plein format cliquables accompagnées d'un texte descriptif.

| Propriété | Description |
|---|---|
| `aspectRatio` | Le rapport hauteur/largeur de l'image de la carte, servant d'indication avant la fin du chargement de l'image. Notez que cette propriété peut ne pas être fournie dans certaines circonstances. |
| `categories` | Cette propriété sert uniquement à l'organisation dans votre implémentation personnalisée ; ces catégories peuvent être définies dans le compositeur du tableau de bord. |
| `clicked` | Cette propriété indique si cette carte a déjà été cliquée sur cet appareil. |
| `created` | L'horodatage UNIX de la création de la carte depuis Braze. |
| `dismissed` | Cette propriété indique si cette carte a été fermée. |
| `dismissible` | Cette propriété indique si l'utilisateur peut fermer la carte, la retirant de la vue. |
| `imageUrl` | L'URL de l'image de la carte. |
| `linkText` | Le texte d'affichage pour l'URL. |
| `title` | Le texte du titre de cette carte. |
| `url` | L'URL qui sera ouverte après un clic sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Image avec légende" }

### Classique {#classic}

Le modèle [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html) peut contenir une image sans texte ou un texte avec image.

| Propriété | Description |
|---|---|
| `aspectRatio` | Le rapport hauteur/largeur de l'image de la carte, servant d'indication avant la fin du chargement de l'image. Notez que cette propriété peut ne pas être fournie dans certaines circonstances. |
| `categories` | Cette propriété sert uniquement à l'organisation dans votre implémentation personnalisée ; ces catégories peuvent être définies dans le compositeur du tableau de bord. |
| `clicked` | Cette propriété indique si cette carte a déjà été cliquée sur cet appareil. |
| `created` | L'horodatage UNIX de la création de la carte depuis Braze. |
| `description` | Le corps du texte de cette carte. |
| `dismissed` | Cette propriété indique si cette carte a été fermée. |
| `dismissible` | Cette propriété indique si l'utilisateur peut fermer la carte, la retirant de la vue. |
| `imageUrl` | L'URL de l'image de la carte. |
| `linkText` | Le texte d'affichage pour l'URL. |
| `title` | Le texte du titre de cette carte. |
| `url` | L'URL qui sera ouverte après un clic sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Classique" }

### Formats d'image {#image-formats}

Les images des Content Cards (y compris les GIF) sont rendues à l'aide de balises HTML standard `<img>`. La prise en charge des GIF dépend des capacités du navigateur de l'utilisateur et ne nécessite pas de version minimale du SDK Web. Tous les navigateurs modernes prennent en charge la lecture des GIF de manière native.

## Groupe de contrôle {#control-group}

Si vous utilisez le flux de Content Cards par défaut, les impressions et les clics sont automatiquement suivis.

Si vous utilisez une intégration personnalisée pour les Content Cards, vous devez [enregistrer les impressions]({{site.baseurl}}/developer_guide/content_cards/logging_analytics) lorsqu'une carte de contrôle aurait été vue. Dans le cadre de cet effort, assurez-vous de gérer les cartes de contrôle lors de l'enregistrement des impressions dans un test A/B. Ces cartes sont vierges et, bien qu'elles ne soient pas vues par les utilisateurs, vous devez quand même enregistrer les impressions afin de comparer leurs performances par rapport aux cartes hors contrôle.

Pour déterminer si une Content Card fait partie du groupe de contrôle d'un test A/B, vérifiez la propriété `card.isControl` (SDK Web v4.5.0+) ou vérifiez si la carte est une instance de `ControlCard` (`card instanceof braze.ControlCard`).

## Méthodes de carte {#card-methods}

### Méthodes de flux par défaut {#default-feed-methods}

Utilisez ces méthodes lorsque vous affichez des Content Cards en utilisant l'interface utilisateur de flux par défaut de Braze :

| Méthode | Description |
|---|---|
| [`showContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards) | Affiche le flux de Content Cards par défaut. Effectue le rendu des cartes dans un élément HTML `parentNode` fourni, ou sous forme de barre latérale à position fixe si aucun élément n'est spécifié. Accepte une fonction `filterFunction` facultative pour trier ou filtrer les cartes avant l'affichage. |
| [`hideContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#hidecontentcards) | Masque le flux de Content Cards par défaut s'il est actuellement affiché. |
| [`toggleContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards) | Affiche le flux de Content Cards par défaut s'il est masqué, ou le masque s'il est visible. Si vous devez afficher plusieurs flux de Content Cards simultanément, utilisez `showContentCards` et `hideContentCards` à la place. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Méthodes de flux par défaut" }

### Méthodes de flux personnalisé {#custom-feed-methods}

Utilisez ces méthodes lorsque vous créez votre propre interface utilisateur de Content Cards :

| Méthode | Description |
|---|---|
| [`subscribeToContentCardsUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsupdates) | Enregistre une fonction de rappel qui est invoquée chaque fois que les Content Cards sont mises à jour pour l'utilisateur actuel, par exemple au démarrage de la session. Utilisez cette méthode comme moyen principal de recevoir les données des cartes pour votre flux personnalisé. Doit être appelée avant `openSession()` pour recevoir les mises à jour lors de la session initiale. |
| [`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards) | Renvoie toutes les cartes actuellement disponibles à partir de la dernière actualisation des Content Cards. Utilisez cette méthode pour afficher immédiatement les cartes au chargement de la page sans attendre une nouvelle requête serveur, par exemple lorsque l'utilisateur revient sur une page pendant une session active. |
| [`requestContentCardsRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh) | Demande une actualisation immédiate des Content Cards auprès des serveurs Braze. Par défaut, les cartes sont actualisées au démarrage de la session et lorsque le flux par défaut est rouvert. Utilisez cette méthode pour forcer une actualisation à d'autres moments, par exemple après une action spécifique de l'utilisateur. Tenez compte des [limites de débit]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed#rate-limit). |
| [`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions) | Enregistre des événements d'impression pour un tableau de cartes. Appelez cette méthode lorsque les cartes sont rendues et visibles par l'utilisateur. Nécessaire pour des rapports de Campaign précis lorsque vous utilisez une interface personnalisée, car les impressions ne sont pas suivies automatiquement en dehors du flux par défaut. |
| [`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick) | Enregistre un événement de clic pour une seule carte. Appelez cette méthode lorsqu'un utilisateur interagit avec une carte dans votre interface personnalisée. Nécessaire pour des rapports de Campaign précis, car les clics ne sont pas suivis automatiquement en dehors du flux par défaut. |
| [`handleBrazeAction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#handlebrazeaction) | Traite l'URL d'une carte et exécute l'action au clic configurée, y compris les actions Braze (URL `brazeActions://`) et la navigation URL standard. Appelez cette méthode dans votre gestionnaire de clic de carte pour vous assurer que les comportements au clic configurés dans le tableau de bord de Braze sont exécutés. |
| [`dismissCard`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#dismisscard) | Rejette une carte de manière programmatique, la retirant du flux de l'utilisateur. Utilisez cette méthode pour permettre aux utilisateurs de rejeter des cartes dans votre interface personnalisée. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Méthodes de flux personnalisé" }

Pour plus de détails, consultez la [documentation de référence du SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

## Bonnes pratiques {#best-practices}

### Appeler les méthodes dans le bon ordre {#call-methods-in-the-correct-order}

Pour les flux personnalisés, les Content Cards ne s'actualisent au démarrage de la session que si `subscribeToContentCardsUpdates()` est appelé avant `openSession()`. Appelez vos méthodes Braze dans cet ordre :

```javascript
import * as braze from "@braze/web-sdk";

// Step 1: Initialize the SDK
braze.initialize("YOUR-API-KEY", { baseUrl: "YOUR-SDK-ENDPOINT" });

// Step 2: Subscribe to card updates
braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
  renderCards(cards);
});

// Step 3: Identify the user
braze.changeUser("USER_ID");

// Step 4: Start the session
braze.openSession();
```

### Utiliser les cartes en cache pour conserver le contenu entre les chargements de page {#use-cached-cards-to-persist-content-across-page-loads}

Étant donné que `subscribeToContentCardsUpdates()` n'invoque son rappel que lorsqu'il y a de nouvelles mises à jour (par exemple au démarrage de la session), les cartes peuvent disparaître de votre flux personnalisé si un utilisateur actualise la page en cours de session. Pour éviter cela, utilisez `getCachedContentCards()` pour afficher immédiatement les cartes à partir du cache local, en complément de votre abonnement pour les nouvelles mises à jour :

```javascript
import * as braze from "@braze/web-sdk";

function renderCards(cards) {
  const container = document.getElementById("content-cards");
  container.textContent = "";
  const displayedCards = [];

  cards.forEach(card => {
    if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
      const cardElement = document.createElement("div");

      const h3 = document.createElement("h3");
      h3.textContent = card.title || "";
      cardElement.appendChild(h3);

      const p = document.createElement("p");
      p.textContent = card.description || "";
      cardElement.appendChild(p);

      if (card.imageUrl) {
        const img = document.createElement("img");
        img.src = card.imageUrl;
        img.alt = card.title || "";
        cardElement.appendChild(img);
      }

      if (card.url) {
        cardElement.addEventListener("click", () => {
          braze.logContentCardClick(card);
          braze.handleBrazeAction(card.url);
        });
      }

      container.appendChild(cardElement);
      displayedCards.push(card);
    }
  });

  if (displayedCards.length > 0) {
    braze.logContentCardImpressions(displayedCards);
  }
}

// Display cached cards immediately
const cached = braze.getCachedContentCards();
if (cached && cached.cards.length > 0) {
  renderCards(cached.cards);
}

// Subscribe to future updates
braze.subscribeToContentCardsUpdates((updates) => {
  renderCards(updates.cards);
});
```

### Enregistrer les analyses pour les flux personnalisés {#log-analytics-for-custom-feeds}

Lorsque vous utilisez une interface utilisateur personnalisée, les impressions, les clics et les fermetures ne sont pas suivis automatiquement. Vous devez enregistrer chaque événement manuellement :

- **Impressions :** Appelez `logContentCardImpressions([card1, card2, ...])` avec un tableau d'objets de cartes lorsque les cartes deviennent visibles pour l'utilisateur.
- **Clics :** Appelez `logContentCardClick(card)` lorsqu'un utilisateur interagit avec une carte.
- **Comportement au clic :** Appelez `handleBrazeAction(card.url)` pour exécuter l'action configurée au clic de la carte (par exemple, naviguer vers une URL ou enregistrer un événement personnalisé).

{% alert warning %}
L'argument transmis à `logContentCardClick()` doit être un objet `Card` Braze d'origine. Si vous transformez ou reconstituez les données de la carte (par exemple, en les sérialisant puis en les désérialisant), les clics ne sont pas enregistrés et vous obtenez l'erreur : « card must be a Card object. »
{% endalert %}

## Utiliser Google Tag Manager {#using-google-tag-manager}

Google Tag Manager fonctionne en injectant le [CDN Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn) (une version de notre SDK Web) directement dans le code de votre site web, ce qui signifie que toutes les méthodes du SDK sont disponibles exactement comme si vous aviez intégré le SDK sans Google Tag Manager, sauf lors de l'implémentation des Content Cards.

### Configurer les Content Cards {#setting-up-content-cards}

{% tabs local %}
{% tab Google Tag Manager %}
Pour une intégration standard du flux de Content Cards, vous pouvez utiliser une balise **Custom HTML** dans Google Tag Manager. Ajoutez le code suivant à votre balise Custom HTML, ce qui activera le flux standard de Content Cards :

```html
<script>
   window.braze.showContentCards();
</script>
```

![Configuration de la balise dans Google Tag Manager d'une balise Custom HTML qui affiche le flux de Content Cards.]({% image_buster /assets/img/web-gtm/gtm_content_cards.png %})
{% endtab %}

{% tab Manuel %}
Pour plus de liberté dans la personnalisation de l'apparence des Content Cards et de leur flux, vous pouvez intégrer directement les Content Cards dans votre site web natif. Deux approches sont possibles : utiliser l'interface standard du flux ou créer une interface de flux personnalisée.

{% subtabs local %}
{% subtab Flux standard %}
Lors de l'implémentation de l'[interface standard du flux]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration#standard-feed-ui), les méthodes Braze doivent être précédées de `window.`. Par exemple, `braze.showContentCards` doit être remplacé par `window.braze.showContentCards`.
{% endsubtab %}

{% subtab Flux personnalisé %}
Pour le style d'un [flux personnalisé]({{site.baseurl}}/developer_guide/content_cards/creating_cards), les étapes sont les mêmes que si vous aviez intégré le SDK sans GTM. Par exemple, si vous souhaitez personnaliser la largeur du flux de Content Cards, vous pouvez coller le code suivant dans votre fichier CSS :

{% raw %}
```css
body .ab-feed {
    width: 800px;
}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Mettre à jour les modèles {#upgrading}

Pour passer à la dernière version du SDK Web Braze, suivez les trois étapes suivantes dans votre tableau de bord Google Tag Manager :

1. **Mettre à jour le modèle de balise**<br>Accédez à la page **Templates** dans votre espace de travail. Vous devriez voir une icône indiquant qu'une mise à jour est disponible.<br><br>![Page Templates indiquant qu'une mise à jour est disponible]({% image_buster /assets/img/web-gtm/gtm-update-available.png %})<br><br>Cliquez sur cette icône et, après avoir examiné les modifications, cliquez sur **Accept Update**.<br><br>![Un écran comparant l'ancien et le nouveau modèle de balise avec un bouton « Accept Update »]({% image_buster /assets/img/web-gtm/gtm-accept-update.png %})<br><br>
2. **Mettre à jour le numéro de version**<br>Une fois votre modèle de balise mis à jour, modifiez la balise d'initialisation Braze et mettez à jour la version du SDK vers la version `major.minor` la plus récente. Par exemple, si la dernière version est `4.1.2`, saisissez `4.1`. Vous pouvez consulter la liste des versions du SDK dans notre [journal des modifications](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md).<br><br>![Modèle d'initialisation Braze avec un champ de saisie pour modifier la version du SDK]({% image_buster /assets/img/web-gtm/gtm-version-number.png %})<br><br>
3. **Assurance qualité et publication**<br>Vérifiez que la nouvelle version du SDK fonctionne correctement à l'aide de l'[outil de débogage](https://support.google.com/tagmanager/answer/6107056?hl=en) de Google Tag Manager avant de publier une mise à jour de votre conteneur de balises.

### Résolution des problèmes {#troubleshooting}

#### Activer le débogage des balises {#debugging}

Chaque modèle de balise Braze dispose d'une case à cocher facultative **GTM Tag Debugging** qui peut être utilisée pour enregistrer des messages de débogage dans la console JavaScript de votre page web.

![Outil de débogage de Google Tag Manager]({% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %})

#### Passer en mode débogage {#enter-debug-mode}

Une autre façon d'aider à déboguer votre intégration Google Tag Manager est d'utiliser la fonctionnalité [mode Aperçu](https://support.google.com/tagmanager/answer/6107056) de Google.

Cela vous aidera à identifier quelles valeurs sont envoyées depuis la couche de données de votre page web vers chaque balise Braze déclenchée, et expliquera également quelles balises ont été déclenchées ou non.

![La page de résumé de la balise d'initialisation Braze fournit un aperçu de la balise, y compris des informations sur les balises qui ont été déclenchées.]({% image_buster /assets/img/web-gtm/gtm-debug-mode.png %})

#### Vérifier le séquencement des balises pour les événements personnalisés {#tag-sequencing}

Si les événements personnalisés ou d'autres actions ne sont pas enregistrés dans Braze, une cause fréquente est une condition de concurrence où une balise d'action (telle que **Custom Event** ou **Purchase**) se déclenche avant que la balise **Braze Initialization** ne soit terminée. Pour résoudre ce problème, configurez le [séquencement des balises](https://support.google.com/tagmanager/answer/6238868) dans GTM :

1. Ouvrez la balise d'action qui ne s'enregistre pas correctement.
2. Sous **Advanced Settings** > **Tag Sequencing**, sélectionnez **A tag that fires before \[this tag\]**.
3. Choisissez votre balise **Braze Initialization** comme balise de configuration.

Cela garantit que le SDK est entièrement initialisé avant que les balises d'action ne tentent d'envoyer des données à Braze.

#### Activer la journalisation détaillée {#enable-verbose-logging}

Pour capturer des journaux détaillés à des fins de résolution des problèmes, vous pouvez activer la journalisation détaillée sur votre intégration Google Tag Manager. Ces journaux apparaîtront dans l'onglet **Console** des [outils de développement](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools) de votre navigateur.

Dans votre intégration Google Tag Manager, accédez à votre balise d'initialisation Braze et sélectionnez **Enable Web SDK Logging**.

![La page de résumé de la balise d'initialisation Braze avec l'option Enable Web SDK Logging activée.]({% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %})

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md