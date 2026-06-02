## Conditions préalables {#prerequisites}

Avant de pouvoir utiliser les Content Cards de Braze, vous devez intégrer le [SDK Android de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) dans votre application. Cependant, aucune configuration supplémentaire n'est requise.

## Fragments Google {#google-fragments}

Dans Android, le flux de Content Cards est implémenté en tant que [fragment](https://developer.android.com/guide/components/fragments.html) disponible dans le projet d'interface utilisateur Braze pour Android. La classe [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) actualise et affiche automatiquement le contenu des Content Cards et enregistre les données d'analyse d'utilisation. Les cartes qui peuvent apparaître dans le `ContentCards` d'un utilisateur sont créées sur le tableau de bord de Braze.

Pour savoir comment ajouter un fragment à une activité, consultez la [documentation de Google sur les fragments](https://developer.android.com/guide/fragments#Adding).

## Types et propriétés des cartes {#card-types-and-properties}

Le modèle de données des Content Cards est disponible dans le SDK Android et propose les types de Content Cards uniques suivants. Chaque type partage un modèle de base, ce qui leur permet d'hériter des propriétés communes du modèle de base, en plus de posséder leurs propres propriétés uniques. Pour la documentation de référence complète, consultez [`com.braze.models.cards`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html).

### Modèle de carte de base {#base-card-for-android}

Le modèle de [carte de base](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) fournit le comportement fondamental pour toutes les cartes.

| Propriété | Description |
|---|---|
| `getId()` | Renvoie l'ID de la carte défini par Braze. |
| `getViewed()` | Renvoie un booléen indiquant si la carte a été lue ou non par l'utilisateur. |
| `getExtras()` | Renvoie un mappage des compléments clé-valeur de cette carte. |
| `getCreated()` | Renvoie le timestamp unix de l'heure de création de la carte depuis Braze. |
| `isPinned` | Renvoie un booléen indiquant si la carte est épinglée. |
| `getOpenUriInWebView()` | Renvoie un booléen indiquant si les URI de cette carte doivent être ouverts <br> dans la WebView de Braze ou non. |
| `getExpiredAt()` | Récupère la date d'expiration de la carte. |
| `isRemoved()` | Renvoie un booléen indiquant si l'utilisateur final a rejeté cette carte. |
| `isDismissibleByUser()` | Renvoie un booléen indiquant si la carte peut être fermée par l'utilisateur. |
| `isClicked()` | Renvoie un booléen indiquant si cette carte a été cliquée. |
| `isDismissed` | Renvoie un booléen indiquant si la carte a été rejetée. Définissez sur `true` pour marquer la carte comme rejetée. Si une carte est déjà marquée comme rejetée, elle ne peut pas être marquée comme rejetée à nouveau. |
| `isControl()` | Renvoie un booléen indiquant si cette carte est une carte de contrôle et ne doit pas être affichée. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Base card model #base-card-for-android" }

### Image uniquement {#banner-image-card-for-android}

Les [cartes avec image uniquement](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) sont des images cliquables en taille réelle.

| Propriété | Description |
|---|---|
| `getImageUrl()` | Renvoie l'URL de l'image de la carte. |
| `getUrl()` | Renvoie l'URL qui sera ouverte après un clic sur la carte. Il peut s'agir d'une URL HTTP(s) ou d'une URL de protocole. |
| `getDomain()` | Renvoie le texte de lien pour l'URL de propriété. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Image only #banner-image-card-for-android" }

### Image légendée {#captioned-image-card-for-android}

Les [cartes d'images légendées](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) sont des images cliquables en taille réelle accompagnées d'un texte descriptif.

| Propriété | Description |
|---|---|
| `getImageUrl()` | Renvoie l'URL de l'image de la carte. |
| `getTitle()` | Renvoie le texte du titre de la carte. |
| `getDescription()` | Renvoie le texte du corps de la carte. |
| `getUrl()` | Renvoie l'URL qui sera ouverte après un clic sur la carte. Il peut s'agir d'une URL HTTP(s) ou d'une URL de protocole. |
| `getDomain()` | Renvoie le texte de lien pour l'URL de propriété. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Captioned image #captioned-image-card-for-android" }

### Classique {#text-Announcement-card-for-android}

Une carte classique sans image donnera lieu à une [carte d'annonce textuelle](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html). Si une image est incluse, vous obtiendrez une [carte d'actualités brèves](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html).

| Propriété | Description |
|---|---|
| `getTitle()` | Renvoie le texte du titre de la carte. |
| `getDescription()` | Renvoie le texte du corps de la carte. |
| `getUrl()` | Renvoie l'URL qui sera ouverte après un clic sur la carte. Il peut s'agir d'une URL HTTP(s) ou d'une URL de protocole. |
| `getDomain()` | Renvoie le texte de lien pour l'URL de propriété. |
| `getImageUrl()` | Renvoie l'URL de l'image de la carte. S'applique uniquement à la carte classique d'actualités brèves. |
| `isDismissed` | Renvoie un booléen indiquant si la carte a été rejetée. Définissez sur `true` pour marquer la carte comme rejetée. Si une carte est déjà marquée comme rejetée, elle ne peut pas être marquée comme rejetée à nouveau. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Classic #text-Announcement-card-for-android" }

## Méthodes de carte {#card-methods}

Tous les objets de modèle de données [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) proposent les méthodes d'analyse suivantes pour enregistrer les événements utilisateur sur les serveurs Braze.

| Méthode | Description |
|---|---|
| `logImpression()` | Enregistre manuellement une impression sur Braze pour une carte donnée. |
| `logClick()` | Enregistre manuellement un clic sur Braze pour une carte donnée. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Card methods" }