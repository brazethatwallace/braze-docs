---
page_order: 2.2
nav_title: Content Cards
article_title: Content Cards
description: "Découvrez comment implémenter les Content Cards avec le SDK de Braze, notamment les modèles de données, les types de cartes et les options de personnalisation pour vos applications mobiles et web."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Content Cards {#content-cards}

> Découvrez les Content Cards pour le SDK de Braze, notamment les différents modèles de données et les propriétés spécifiques aux cartes disponibles pour votre application.

{% multi_lang_include banners/content_card_alert.md %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/content_cards.md %}
{% endsdktab %}

{% sdktab android %}
## Conditions préalables {#prerequisites}

Avant de pouvoir utiliser les Content Cards de Braze, vous devez intégrer le [SDK Android de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) dans votre application. Cependant, aucune configuration supplémentaire n'est requise.

## Fragments Google {#google-fragments}

Sur Android, le flux de Content Cards est implémenté sous forme de [fragment](https://developer.android.com/guide/components/fragments.html) disponible dans le projet d'interface utilisateur Android de Braze. La classe [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) actualise et affiche automatiquement le contenu des Content Cards et enregistre les données d'analytique d'utilisation. Les cartes qui peuvent apparaître dans les `ContentCards` d'un utilisateur sont créées dans le tableau de bord de Braze.

Pour savoir comment ajouter un fragment à une activité, consultez la [documentation Google sur les fragments](https://developer.android.com/guide/fragments#Adding).

## Types de cartes et propriétés {#card-types-and-properties}

Le modèle de données des Content Cards est disponible dans le SDK Android et propose les types de Content Cards uniques suivants. Chaque type partage un modèle de base, ce qui lui permet d'hériter des propriétés communes du modèle de base, en plus de posséder ses propres propriétés uniques. Pour la documentation de référence complète, consultez [`com.braze.models.cards`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html).

### Modèle de carte de base {#base-card-for-android}

Le modèle de [carte de base](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) fournit le comportement fondamental pour toutes les cartes.

| Propriété | Description |
|---|---|
| `getId()` | Renvoie l'ID de la carte défini par Braze. |
| `getViewed()` | Renvoie un booléen indiquant si la carte a été lue ou non par l'utilisateur. |
| `getExtras()` | Renvoie une map de paires clé-valeur supplémentaires pour cette carte. |
| `getCreated()` | Renvoie l'horodatage unix de la date de création de la carte depuis Braze. |
| `isPinned` | Renvoie un booléen indiquant si la carte est épinglée. |
| `getOpenUriInWebView()` | Renvoie un booléen indiquant si les URI de cette carte doivent être ouverts <br> dans la WebView de Braze ou non. |
| `getExpiredAt()` | Obtient la date d'expiration de la carte. |
| `isRemoved()` | Renvoie un booléen indiquant si l'utilisateur final a rejeté cette carte. |
| `isDismissibleByUser()` | Renvoie un booléen indiquant si la carte peut être rejetée par l'utilisateur. |
| `isClicked()` | Renvoie un booléen reflétant l'état de clic de cette carte. |
| `isDismissed` | Renvoie un booléen indiquant si la carte a été rejetée. Définissez sur `true` pour marquer la carte comme rejetée. Si une carte est déjà marquée comme rejetée, elle ne peut pas être marquée comme rejetée à nouveau. |
| `isControl()` | Renvoie un booléen indiquant si cette carte est une carte de contrôle et ne doit pas être affichée. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Base card model #base-card-for-android" }

### Image uniquement {#banner-image-card-for-android}

Les [cartes image uniquement](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) sont des images cliquables en taille réelle.

| Propriété | Description |
|---|---|
| `getImageUrl()` | Renvoie l'URL de l'image de la carte. |
| `getUrl()` | Renvoie l'URL qui est ouverte après un clic sur la carte. Il peut s'agir d'une URL HTTP(s) ou d'une URL de protocole. |
| `getDomain()` | Renvoie le texte du lien pour l'URL de la propriété. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Image only #banner-image-card-for-android" }

### Image avec légende {#captioned-image-card-for-android}

Les [cartes image avec légende](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) sont des images cliquables en taille réelle accompagnées d'un texte descriptif.

| Propriété | Description |
|---|---|
| `getImageUrl()` | Renvoie l'URL de l'image de la carte. |
| `getTitle()` | Renvoie le texte du titre de la carte. |
| `getDescription()` | Renvoie le texte du corps de la carte. |
| `getUrl()` | Renvoie l'URL qui est ouverte après un clic sur la carte. Il peut s'agir d'une URL HTTP(s) ou d'une URL de protocole. |
| `getDomain()` | Renvoie le texte du lien pour l'URL de la propriété. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Captioned image #captioned-image-card-for-android" }

### Classique {#text-Announcement-card-for-android}

Une carte classique sans image donne une [carte d'annonce textuelle](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html). Si une image est incluse, vous recevez une [carte d'actualité courte](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html).

| Propriété | Description |
|---|---|
| `getTitle()` | Renvoie le texte du titre de la carte. |
| `getDescription()` | Renvoie le texte du corps de la carte. |
| `getUrl()` | Renvoie l'URL qui est ouverte après un clic sur la carte. Il peut s'agir d'une URL HTTP(s) ou d'une URL de protocole. |
| `getDomain()` | Renvoie le texte du lien pour l'URL de la propriété. |
| `getImageUrl()` | Renvoie l'URL de l'image de la carte, s'applique uniquement à la carte classique d'actualité courte. |
| `isDismissed` | Renvoie un booléen indiquant si la carte a été rejetée. Définissez sur `true` pour marquer la carte comme rejetée. Si une carte est déjà marquée comme rejetée, elle ne peut pas être marquée comme rejetée à nouveau. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Classic #text-Announcement-card-for-android" }

## Méthodes de carte {#card-methods}

Tous les objets du modèle de données [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) offrent les méthodes d'analytique suivantes pour enregistrer les événements utilisateur sur les serveurs de Braze.

| Méthode | Description |
|---|---|
| `logImpression()` | Enregistre manuellement une impression sur Braze pour une carte particulière. |
| `logClick()` | Enregistre manuellement un clic sur Braze pour une carte particulière. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Card methods" }

{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/content_cards.md %}
{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/content_cards.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/content_cards.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/content_cards.md %}
{% endsdktab %}

{% sdktab tvos %}
## Conditions préalables

Avant de pouvoir utiliser les Content Cards, intégrez le [SDK Swift de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) dans votre application. Ensuite, suivez les étapes de configuration de votre application tvOS.

{% alert important %}
Implémentez votre propre interface utilisateur personnalisée, car les Content Cards sont prises en charge via une interface sans affichage (headless UI) à l'aide du SDK Swift&#8212;qui n'inclut aucune interface utilisateur ni vue par défaut pour tvOS.
{% endalert %}

## Configuration de votre application tvOS {#setting-up-your-tvos-app}

### Étape 1 : Créer une nouvelle application iOS {#step-1-create-a-new-ios-app}

Dans Braze, sélectionnez **Settings** > **App Settings**, puis sélectionnez **Add App**. Saisissez un nom pour votre application tvOS, sélectionnez **iOS**&#8212;_pas tvOS_&#8212;puis sélectionnez **Add App**.

![Boîte de dialogue d'ajout d'application dans Braze avec la plateforme iOS sélectionnée pour enregistrer une application tvOS.]({% image_buster /assets/img/tvos.png %}){: style="width:70%"}

{% alert warning %}
Si vous cochez la case **tvOS**, vous ne pourrez pas personnaliser les Content Cards pour tvOS.
{% endalert %}

### Étape 2 : Obtenir la clé API de votre application {#step-2-get-your-apps-api-key}

Dans les paramètres de votre application, sélectionnez votre nouvelle application tvOS, puis notez la clé API de votre application. Utilisez cette clé pour configurer votre application dans Xcode.

![Paramètres de l'application pour une application tvOS affichant la clé API utilisée pour l'intégration SDK.]({% image_buster /assets/img/tvos1.png %}){: style="width:70%"}

### Étape 3 : Intégrer BrazeKit {#step-3-integrate-brazekit}

Utilisez la clé API de votre application pour intégrer le [SDK Swift de Braze](https://github.com/braze-inc/braze-swift-sdk) dans votre projet tvOS dans Xcode. Vous devez uniquement intégrer BrazeKit à partir du SDK Swift de Braze.

### Étape 4 : Créer votre interface utilisateur personnalisée {#step-4-create-your-custom-ui}

Étant donné que Braze ne fournit pas d'interface utilisateur par défaut pour les Content Cards sur tvOS, personnalisez-la vous-même. Pour un guide complet étape par étape, consultez notre tutoriel : [Personnalisation des Content Cards pour tvOS](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/content-cards-customization/). Pour un projet d'exemple, consultez les [exemples du SDK Swift de Braze](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#contentcards-custom-ui).

{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/content_cards.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
{% multi_lang_include developer_guide/xamarin/content_cards.md %}
{% endsdktab %}
{% endsdktabs %}