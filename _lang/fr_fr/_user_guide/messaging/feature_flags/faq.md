---
nav_title: FAQ
article_title: Questions fréquemment posées
page_order: 50
description: "Cette page fournit des réponses aux questions fréquemment posées sur les indicateurs de fonctionnalité."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web
---

# Questions fréquemment posées {#frequently-asked-questions}

> Cet article fournit des réponses aux questions fréquemment posées sur les indicateurs de fonctionnalité.

## Fonctionnalités et support {#functionality-and-support}

### Quelles plateformes prennent en charge les feature flags de Braze ? {#platforms}

Braze prend en charge les feature flags sur les plateformes iOS, Android et Web avec les versions minimum de SDK suivantes :

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

Vous avez besoin d'un support sur d'autres plateformes ? Contactez notre équipe par e-mail : [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

### Quel est le niveau d'effort nécessaire pour implémenter un feature flag ? {#level-of-effort}

Un feature flag peut être créé et intégré en quelques minutes.

La majeure partie de l'effort sera liée au développement par votre équipe d'ingénierie de la nouvelle fonctionnalité que vous prévoyez de déployer. Mais en ce qui concerne l'ajout d'un feature flag, c'est aussi simple qu'une instruction `IF`/`ELSE` dans le code de votre application ou site web :

{% tabs %}
{% tab JavaScript %}

```javascript
import { getFeatureFlag } from "@braze/web-sdk";

if (getFeatureFlag("new_shopping_cart").enabled) {
    // Show the new homepage your team has built
}
else {
    // Show the old homepage
}
```

{% endtab %}
{% tab Java %}

```java
if (braze.getFeatureFlag("new_shopping_cart").getEnabled()) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
if (braze.getFeatureFlag("new_shopping_cart")?.enabled == true) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% endtabs %}

### Comment les feature flags peuvent-ils bénéficier aux équipes Marketing ? {#marketing-teams}

Les équipes Marketing peuvent utiliser les feature flags pour coordonner les annonces produit (comme les e-mails de lancement de produit) lorsqu'une fonctionnalité n'est activée que pour un faible pourcentage d'utilisateurs.

Par exemple, avec les feature flags de Braze, vous pouvez déployer un nouveau programme de fidélité client auprès de 10 % des utilisateurs de votre application, puis envoyer un e-mail, une notification push ou tout autre message à ces mêmes 10 % d'utilisateurs activés à l'aide de l'étape Feature Flag dans Canvas.

### Comment les feature flags peuvent-ils bénéficier aux équipes Produit ? {#product-teams}

Les équipes Produit peuvent utiliser les feature flags pour effectuer des déploiements progressifs ou des lancements en douceur de nouvelles fonctionnalités, afin de suivre les indicateurs clés de performance et les retours clients avant de les rendre disponibles à tous les utilisateurs.

Les équipes Produit peuvent utiliser les [propriétés de feature flag]({{site.baseurl}}/developer_guide/feature_flags/create#accessing-properties) pour alimenter à distance le contenu d'une application, comme des deep links, du texte, des images ou tout autre contenu dynamique.

En utilisant l'étape Feature Flag de Canvas, les équipes Produit peuvent également réaliser un test A/B pour mesurer l'impact d'une nouvelle fonctionnalité sur les taux de conversion par rapport aux utilisateurs pour lesquels la fonctionnalité est désactivée.

### Comment les feature flags peuvent-ils bénéficier aux équipes d'ingénierie ? {#engineering-teams}

Les équipes d'ingénierie peuvent utiliser les feature flags pour réduire les risques inhérents au lancement de nouvelles fonctionnalités et éviter de se précipiter pour déployer des correctifs de code en pleine nuit.

En publiant du nouveau code masqué derrière un feature flag, votre équipe peut activer ou désactiver la fonctionnalité à distance depuis le tableau de bord de Braze, en évitant le délai lié à la publication de nouveau code ou à l'attente d'une approbation de mise à jour sur la boutique d'applications.

## Déploiement des fonctionnalités et ciblage {#feature-rollouts-and-targeting}

### Un feature flag peut-il être déployé uniquement pour un groupe restreint d'utilisateurs ? {#target-users}

Oui, créez un Segment dans Braze qui cible des utilisateurs spécifiques, par adresse e-mail, `user_id` ou tout autre attribut de vos profils utilisateur. Ensuite, déployez le feature flag pour 100 % de ce Segment.

### Comment l'ajustement du pourcentage de déploiement affecte-t-il les utilisateurs qui avaient été précédemment placés dans le groupe activé ? {#random-buckets}

Les déploiements de feature flags restent cohérents pour les utilisateurs entre les appareils et les sessions.

- Lorsqu'un feature flag est déployé pour 10 % d'utilisateurs aléatoires, ces 10 % restent activés et persistent pendant toute la durée de vie de ce feature flag.
- Si vous augmentez le déploiement de 10 % à 20 %, les mêmes 10 % restent activés, et 10 % d'utilisateurs supplémentaires sont ajoutés au groupe activé.
- Si vous réduisez le déploiement de 20 % à 10 %, seuls les 10 % d'utilisateurs initiaux restent activés.

Cette stratégie permet de garantir que les utilisateurs bénéficient d'une expérience cohérente dans votre application et ne basculent pas d'un état à l'autre d'une session à l'autre. Bien entendu, désactiver une fonctionnalité à 0 % supprimera tous les utilisateurs du feature flag, ce qui est utile si vous découvrez un bug ou si vous devez désactiver complètement la fonctionnalité.

## Sujets techniques {#technical-topics}

### Les feature flags peuvent-ils être utilisés pour contrôler le moment où le SDK Braze est initialisé ? {#initialization}

Non, le SDK doit être initialisé pour télécharger et synchroniser les feature flags pour l'utilisateur actuel. Cela signifie que vous ne pouvez pas utiliser les feature flags pour limiter les utilisateurs créés ou suivis dans Braze.

### À quelle fréquence le SDK actualise-t-il les feature flags ? {#refresh-frequency}

Les feature flags sont actualisés au démarrage de la session et lors du changement d'utilisateur actif. Les feature flags peuvent également être actualisés manuellement à l'aide de la [méthode d'actualisation]({{site.baseurl}}/developer_guide/feature_flags/create#refreshing) du SDK. L'actualisation des feature flags est soumise à une limite de débit d'une fois toutes les cinq minutes (sous réserve de modification).

Gardez à l'esprit que de bonnes pratiques en matière de données recommandent de ne pas actualiser les feature flags trop rapidement (avec une potentielle limitation du débit si c'est le cas). Il est donc préférable de n'actualiser qu'avant qu'un utilisateur interagisse avec de nouvelles fonctionnalités ou périodiquement dans l'application si nécessaire.

### Les feature flags sont-ils disponibles lorsqu'un utilisateur est hors ligne ? {#offline}

Oui, après l'actualisation des feature flags, ils sont stockés localement sur l'appareil de l'utilisateur et sont accessibles hors connexion.

### Que se passe-t-il si les feature flags sont actualisés en cours de session ? {#listen-for-updates}

Les feature flags peuvent être actualisés en cours de session. Il existe des scénarios dans lesquels vous souhaiterez peut-être mettre à jour votre application si certaines variables ou votre configuration doivent changer. Il existe d'autres scénarios dans lesquels vous ne souhaiterez pas mettre à jour votre application, afin d'éviter un changement brusque dans le rendu de votre interface utilisateur.

Pour contrôler cela, [écoutez les mises à jour]({{site.baseurl}}/developer_guide/feature_flags/create#updates) des feature flags et déterminez s'il faut effectuer un nouveau rendu de votre application en fonction des feature flags qui ont changé.

### Pourquoi les utilisateurs de mon groupe de contrôle global ne reçoivent-ils pas les expériences de feature flags ? {#why-arent-users-in-my-global-control-group-receiving-feature-flags-experiments}

Vous ne pouvez pas activer les feature flags pour les utilisateurs de votre [groupe de contrôle global]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts). Cela signifie que les utilisateurs de votre groupe de contrôle global ne peuvent pas non plus participer aux expériences de feature flags.

### L'identification des destinataires par e-mail fait-elle partie des feature flags Braze ? {#is-email-based-recipient-identification-part-of-braze-feature-flags}

Non. L'identification des destinataires par e-mail lors de l'envoi d'un message ne fait pas partie du produit Feature Flags décrit sur cette page. Les feature flags contrôlent les expériences in-app ou sur site via le SDK Braze.

Les envois de Campaign et de Canvas déclenchés par API peuvent inclure `email` dans l'[objet destinataires]({{site.baseurl}}/api/objects_filters/recipient_object) à la place d'un `external_user_id`. Lorsque vous utilisez `email`, incluez `prioritization` afin que Braze puisse sélectionner le profil utilisateur correspondant. Cette option d'envoi n'est pas disponible sur tous les espaces de travail.

Pour le format de la requête, consultez [POST : Envoyer des Campaigns via une distribution déclenchée par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) et [POST : Envoyer des messages Canvas via une distribution déclenchée par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).

## Des questions supplémentaires ? {#additional-questions}

Vous avez des questions ou des commentaires ? Envoyez un e-mail à notre équipe : [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).