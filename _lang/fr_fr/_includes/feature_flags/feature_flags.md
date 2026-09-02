# Indicateurs de fonctionnalité {#feature-flags}

> Les indicateurs de fonctionnalité vous permettent d'activer ou de désactiver à distance des fonctionnalités pour une sélection spécifique ou aléatoire d'utilisateurs. Point essentiel : ils vous permettent d'activer et de désactiver une fonctionnalité en production sans déploiement de code supplémentaire ni mise à jour sur les boutiques d'applications. Vous pouvez ainsi déployer de nouvelles fonctionnalités en toute sécurité et en toute confiance.

{% alert tip %}
Lorsque vous êtes prêt à créer vos propres indicateurs de fonctionnalité, consultez la rubrique [Créer des indicateurs de fonctionnalité]({{site.baseurl}}/developer_guide/feature_flags/create).
{% endalert %}

## Prérequis {#prerequisites}

Voici les versions minimales du SDK nécessaires pour commencer à utiliser les indicateurs de fonctionnalité :

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

## Cas d'usage {#use-cases}

### Déploiements progressifs {#gradual-rollouts}

Utilisez les indicateurs de fonctionnalité pour activer progressivement des fonctionnalités auprès d'un échantillon de population. Par exemple, vous pouvez lancer en douceur une nouvelle fonctionnalité auprès de vos utilisateurs VIP en premier. Cette stratégie permet d'atténuer les risques liés au déploiement de nouvelles fonctionnalités auprès de tous les utilisateurs en même temps et de détecter les bugs rapidement.

![Image animée d'un curseur de trafic de déploiement passant de 0 % à 100 %.]({% image_buster /assets/img/feature_flags/feature-flags-rollout.gif %})

Par exemple, imaginons que nous avons décidé d'ajouter un nouveau lien « Assistance par chat en direct » à notre application pour un service client plus rapide. Nous pourrions publier cette fonctionnalité à tous les clients en même temps. Cependant, une publication à grande échelle comporte des risques, tels que :

* Notre équipe d'assistance est encore en formation, et les clients peuvent ouvrir des tickets d'assistance dès la publication. Cela ne nous laisse aucune marge si l'équipe d'assistance a besoin de plus de temps.
* Nous ne connaissons pas le volume réel de nouveaux cas d'assistance que nous recevrons, et nous pourrions donc ne pas avoir les effectifs appropriés.
* Si notre équipe d'assistance est submergée, nous n'avons aucune stratégie pour désactiver rapidement cette fonctionnalité.
* Il pourrait y avoir des bugs dans le widget de chat, et nous ne voulons pas que les clients aient une expérience négative.

Avec les indicateurs de fonctionnalité de Braze, nous pouvons déployer progressivement la fonctionnalité et atténuer tous ces risques :

* Nous activerons la fonctionnalité « Assistance par chat en direct » lorsque l'équipe d'assistance confirmera qu'elle est prête.
* Nous activerons cette nouvelle fonctionnalité pour seulement 10 % des utilisateurs afin de déterminer si nous avons les effectifs appropriés.
* En cas de bugs, nous pouvons rapidement désactiver la fonctionnalité au lieu de nous précipiter pour publier une nouvelle version.

Pour déployer progressivement cette fonctionnalité, nous pouvons [créer un indicateur de fonctionnalité]({{site.baseurl}}/developer_guide/feature_flags/create) nommé « Live Chat Widget ».

![Détails de l'indicateur de fonctionnalité pour un exemple nommé Live Chat Widget. L'ID est enable_live_chat. La description de cet indicateur de fonctionnalité indique que le widget de chat en direct s'affichera sur la page d'assistance.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-livechat-1.png %})

Dans le code de notre application, nous n'afficherons le bouton **Start Live Chat** que lorsque l'indicateur de fonctionnalité Braze est activé :

{% tabs %}
{% tab JavaScript %}

```javascript
import {useState} from "react";
import * as braze from "@braze/web-sdk";

// Get the initial value from the Braze SDK
const featureFlag = braze.getFeatureFlag("enable_live_chat");
const [liveChatEnabled, setLiveChatEnabled] = useState(featureFlag.enabled);

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(() => {
    const newValue = braze.getFeatureFlag("enable_live_chat").enabled;
    setLiveChatEnabled(newValue);
});

// Only show the Live Chat if the Braze SDK determines it is enabled
return (<>
  Need help? <button>Email Our Team</button>
  {liveChatEnabled && <button>Start Live Chat</button>}
</>)
```

{% endtab %}
{% tab Java %}

```java
// Get the initial value from the Braze SDK
FeatureFlag featureFlag = braze.getFeatureFlag("enable_live_chat");
Boolean liveChatEnabled = featureFlag != null && featureFlag.getEnabled();

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(event -> {
  FeatureFlag newFeatureFlag = braze.getFeatureFlag("enable_live_chat");
  Boolean newValue = newFeatureFlag != null && newFeatureFlag.getEnabled();
  liveChatEnabled = newValue;
});

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
// Get the initial value from the Braze SDK
val featureFlag = braze.getFeatureFlag("enable_live_chat")
var liveChatEnabled = featureFlag?.enabled

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates() { event ->
  val newValue = braze.getFeatureFlag("enable_live_chat")?.enabled
  liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}

```

{% endtab %}
{% tab Swift %}

{% alert note %}
La lecture de `braze.featureFlags.featureFlags` ou `braze.featureFlags.featureFlag(id:)` bloque le thread appelant jusqu'à ce que le SDK ait terminé ses opérations post-initialisation. Pour les contextes sur le thread principal ou sensibles à la latence, utilisez [`getAllFeatureFlags(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/featureflags-swift.class/getallfeatureflags(_:)) à la place.

```swift
// Non-blocking — completion handler always delivers on the main thread.
braze.featureFlags.getAllFeatureFlags { flags in
  let liveChatEnabled = flags.first(where: { $0.id == "enable_live_chat" })?.enabled ?? false
  liveChatView.isHidden = !liveChatEnabled
}
```

En Objective-C :

```objc
[braze.featureFlags getAllFeatureFlagsWithCompletion:^(NSArray<BRZFeatureFlag *> *flags) {
  // Use `flags` here.
}];
```
{% endalert %}

```swift
// Get the initial value from the Braze SDK
let featureFlag = braze.featureFlags.featureFlag(id: "enable_live_chat")
var liveChatEnabled = featureFlag?.enabled ?? false

// Listen for updates from the Braze SDK
braze.featureFlags.subscribeToUpdates() { _ in
  let newValue = braze.featureFlags.featureFlag(id: "enable_live_chat")?.enabled ?? false
  liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
liveChatView.isHidden = !liveChatEnabled
```

{% endtab %}
{% endtabs %}

### Contrôler à distance les variables de l'application {#remotely-control-app-variables}

Utilisez les indicateurs de fonctionnalité pour modifier le comportement de votre application en production. Cela peut être particulièrement important pour les applications mobiles, où les validations des boutiques d'applications empêchent de déployer rapidement des modifications auprès de tous les utilisateurs.

Par exemple, imaginons que notre équipe marketing souhaite afficher nos ventes et promotions en cours dans la navigation de notre application. Normalement, nos ingénieurs ont besoin d'une semaine de délai pour toute modification et de trois jours pour une validation par la boutique d'applications. Mais avec Thanksgiving, Black Friday, Cyber Monday, Hanoukka, Noël et le Nouvel An répartis sur deux mois, nous ne pourrons pas respecter ces délais serrés.

Avec les indicateurs de fonctionnalité, nous pouvons laisser Braze alimenter le contenu du lien de navigation de notre application, permettant à notre responsable marketing d'effectuer des modifications en quelques minutes plutôt qu'en plusieurs jours.

Pour configurer cette fonctionnalité à distance, nous allons créer un nouvel indicateur de fonctionnalité appelé `navigation_promo_link` et définir les propriétés initiales suivantes :

![Indicateur de fonctionnalité avec des propriétés de lien et de texte redirigeant vers une page de ventes générique.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-1.png %})

Dans notre application, nous utiliserons les méthodes getter de Braze pour récupérer les propriétés de cet indicateur de fonctionnalité et construire les liens de navigation en fonction de ces valeurs :

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";
import {useState} from "react";

const featureFlag = braze.getFeatureFlag("navigation_promo_link");
// Check if the feature flag is enabled
const [promoEnabled, setPromoEnabled] = useState(featureFlag.enabled);
// Read the "link" property
const [promoLink, setPromoLink] = useState(featureFlag.getStringProperty("link"));
// Read the "text" property
const [promoText, setPromoText] = useState(featureFlag.getStringProperty("text"));

return (<>
  <div>
    <a href="/">Home</a>
    { promoEnabled && <a href={promoLink}>{promoText}</a> }
    <a href="/products">Products</a>
    <a href="/categories">Categories
  </div>
</>)
```

{% endtab %}
{% tab Java %}

```java
// liveChatView is the View container for the Live Chat UI
FeatureFlag featureFlag = braze.getFeatureFlag("navigation_promo_link");
if (featureFlag != null && featureFlag.getEnabled()) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
liveChatView.setPromoLink(featureFlag.getStringProperty("link"));
liveChatView.setPromoText(featureFlag.getStringProperty("text"));

```

{% endtab %}
{% tab Kotlin %}

```kotlin
// liveChatView is the View container for the Live Chat UI
val featureFlag = braze.getFeatureFlag("navigation_promo_link")
if (featureFlag?.enabled == true) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}
liveChatView.promoLink = featureFlag?.getStringProperty("link")
liveChatView.promoText = featureFlag?.getStringProperty("text")
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "navigation_promo_link")
if let featureFlag {
  liveChatView.isHidden = !featureFlag.enabled
} else {
  liveChatView.isHidden = true
}
liveChatView.promoLink = featureFlag?.stringProperty("link")
liveChatView.promoText = featureFlag?.stringProperty("text")
```

{% endtab %}
{% endtabs %}

Désormais, la veille de Thanksgiving, il nous suffit de modifier ces valeurs de propriété dans le tableau de bord de Braze.

![Indicateur de fonctionnalité avec des propriétés de lien et de texte redirigeant vers une page de ventes pour Thanksgiving.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-2.png %})

Ainsi, la prochaine fois qu'un utilisateur chargera l'application, il verra les nouvelles offres de Thanksgiving.

### Coordination des messages {#message-coordination}

Utilisez les indicateurs de fonctionnalité pour synchroniser le déploiement d'une fonctionnalité et la communication associée, et renforcer la collaboration entre les équipes produit et marketing. En coordonnant les lancements de fonctionnalités et la communication via les indicateurs de fonctionnalité, les deux équipes peuvent aligner leurs stratégies et créer des expériences utilisateur cohérentes.

Par exemple, imaginons que nous lançons un nouveau programme de fidélité pour nos utilisateurs. Il peut être difficile pour les équipes marketing et produit de coordonner parfaitement le timing des messages promotionnels avec le déploiement d'une fonctionnalité. Cependant, avec les indicateurs de fonctionnalité dans Canvas, notre équipe produit peut appliquer une logique sophistiquée pour activer une fonctionnalité auprès d'une audience spécifique, tandis que notre équipe marketing contrôle les messages associés envoyés à ces mêmes utilisateurs.

Pour coordonner efficacement le déploiement de la fonctionnalité et la communication, nous allons créer un nouvel indicateur de fonctionnalité appelé `show_loyalty_program`. Pour notre déploiement initial par phases, nous laisserons Canvas contrôler quand et pour qui l'indicateur de fonctionnalité est activé. Pour l'instant, nous laisserons le pourcentage de déploiement à 0 % et ne sélectionnerons aucun Segment cible.

![Un indicateur de fonctionnalité nommé Loyalty Rewards Program. L'ID est show_loyalty_program, et la description indique que cet indicateur affiche le nouveau programme de fidélité sur l'écran d'accueil et la page de profil.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-loyalty.png %})

Ensuite, dans Canvas, nous allons créer une [étape Indicateur de fonctionnalité]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/feature_flags) qui active l'indicateur de fonctionnalité `show_loyalty_program` pour notre Segment « Clients à forte valeur » :

![Exemple d'un Canvas avec une étape de répartition d'audience où le Segment des clients à forte valeur active l'indicateur de fonctionnalité show_loyalty_program.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-flow.png %})

Désormais, les utilisateurs de ce Segment commencent à voir le nouveau programme de fidélité, et une fois celui-ci activé, un e-mail et un sondage sont envoyés automatiquement pour aider nos équipes à recueillir des retours.

### Expérimentation de fonctionnalités {#feature-experimentation}

Utilisez les indicateurs de fonctionnalité pour expérimenter et confirmer vos hypothèses concernant votre nouvelle fonctionnalité. En répartissant le trafic en deux groupes ou plus, vous pouvez comparer l'impact d'un indicateur de fonctionnalité entre les groupes et déterminer la meilleure marche à suivre en fonction des résultats.

Pour les expériences d'indicateurs de fonctionnalité, vous pouvez avoir jusqu'à neuf groupes au total : un groupe de contrôle et jusqu'à huit variantes.

Un [test A/B]({{site.baseurl}}/user_guide/messaging/ab_testing) est un outil puissant qui compare les réponses des utilisateurs à plusieurs versions d'une variable.

Dans cet exemple, notre équipe a développé un nouveau flux de paiement pour notre application eCommerce. Même si nous sommes convaincus qu'il améliore l'expérience utilisateur, nous voulons effectuer un test A/B pour mesurer son impact sur le chiffre d'affaires de notre application.

Pour commencer, nous allons créer un nouvel indicateur de fonctionnalité appelé `enable_checkout_v2`. Nous n'ajouterons pas d'audience ni de pourcentage de déploiement. Au lieu de cela, nous utiliserons une expérience d'indicateur de fonctionnalité pour répartir le trafic, activer la fonctionnalité et mesurer les résultats.

Dans notre application, nous vérifierons si l'indicateur de fonctionnalité est activé ou non et remplacerons le flux de paiement en fonction de la réponse :

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

const featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag?.enabled) {
  return <NewCheckoutFlow />
} else {
  return <OldCheckoutFlow />
}
```

{% endtab %}
{% tab Java %}

```java
FeatureFlag featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag != null && featureFlag.getEnabled()) {
  return new NewCheckoutFlow();
} else {
  return new OldCheckoutFlow();
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("enable_checkout_v2")
braze.logFeatureFlagImpression("enable_checkout_v2")
if (featureFlag?.enabled == true) {
  return NewCheckoutFlow()
} else {
  return OldCheckoutFlow()
}
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "enable_checkout_v2")
braze.featureFlags.logFeatureFlagImpression(id: "enable_checkout_v2")
if let featureFlag, featureFlag.enabled {
  return NewCheckoutFlow()
} else {
  return OldCheckoutFlow()
}
```

{% endtab %}
{% endtabs %}

Nous configurerons notre test A/B dans une [expérience d'indicateur de fonctionnalité]({{site.baseurl}}/developer_guide/feature_flags/experiments).

Désormais, 50 % des utilisateurs verront l'ancienne expérience, tandis que les 50 % restants verront la nouvelle. Nous pourrons ensuite analyser les deux variantes pour déterminer quel flux de paiement a généré un taux de conversion plus élevé. {% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

![Une expérience d'indicateur de fonctionnalité répartissant le trafic en deux groupes de 50 pour cent.]({% image_buster /assets/img/feature_flags/feature-flag-use-case-campaign-experiment.png %})

Une fois que nous aurons déterminé le gagnant, nous pourrons arrêter cette Campaign et augmenter le pourcentage de déploiement de l'indicateur de fonctionnalité à 100 % pour tous les utilisateurs pendant que notre équipe d'ingénierie intègre cela en dur dans notre prochaine version de l'application.

### Segmentation

Utilisez le filtre **Indicateur de fonctionnalité** pour créer un Segment ou cibler la communication vers les utilisateurs en fonction de l'activation ou non d'un indicateur de fonctionnalité. Par exemple, supposons que vous ayez un indicateur de fonctionnalité qui contrôle le contenu premium de votre application. Vous pourriez créer un Segment qui filtre les utilisateurs pour lesquels l'indicateur de fonctionnalité n'est pas activé, puis envoyer à ce Segment un message les incitant à mettre à niveau leur compte pour accéder au contenu premium.

1. Ouvrez votre Segment ou l'audience de votre message.
2. Ajoutez le filtre **Indicateur de fonctionnalité**.
3. Sélectionnez l'indicateur de fonctionnalité.
4. Définissez le comparateur sur **est** pour inclure les utilisateurs pour lesquels l'indicateur de fonctionnalité est activé, ou **n'est pas** pour inclure les utilisateurs pour lesquels il ne l'est pas.
![Générateur de Segments Braze utilisant un filtre de valeur activée d'indicateur de fonctionnalité.]({% image_buster /assets/img/feature_flags/feature_flag_segmentation_filter.png %})

Pour plus d'informations sur le filtrage des Segments, consultez [Créer un Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

{% alert note %}
Pour éviter les Segments récursifs, il n'est pas possible de créer un Segment qui référence d'autres indicateurs de fonctionnalité.
{% endalert %}

## Limitations du forfait {#plan-limitations}

Voici les limitations des indicateurs de fonctionnalité pour les forfaits gratuits et payants.

| Fonctionnalité                                                                                                   | Version gratuite     | Version payante      |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| [Indicateurs de fonctionnalité actifs](#active-feature-flags)                                                                     | 10 par espace de travail | 110 par espace de travail |
| [Expériences de Campaign actives]({{site.baseurl}}/developer_guide/feature_flags/experiments)          | 1 par espace de travail  | 100 par espace de travail |
| [Étapes Indicateur de fonctionnalité dans Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/feature_flags) | Illimité        | Illimité         |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limitations du forfait" }

Un indicateur de fonctionnalité est considéré comme actif et sera comptabilisé dans votre limite si l'une des conditions suivantes s'applique :

- Le déploiement est supérieur à 0 %
- Utilisé dans un Canvas actif
- Utilisé dans une expérience active

Même si le même indicateur de fonctionnalité correspond à plusieurs critères, par exemple s'il est utilisé dans un Canvas et que le déploiement est à 50 %, il ne comptera que comme 1 indicateur de fonctionnalité actif dans votre limite.

{% alert note %}
Pour acheter la version payante des indicateurs de fonctionnalité, contactez votre gestionnaire de compte Braze ou demandez une mise à niveau dans le tableau de bord de Braze.
{% endalert %}