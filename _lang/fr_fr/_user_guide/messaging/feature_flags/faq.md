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

## Fonctionnalités et assistance {#functionality-and-support}

### Sur quelles plateformes les indicateurs de fonctionnalité Braze sont-ils pris en charge ? {#platforms}

Braze prend en charge les indicateurs de fonctionnalité sur les plateformes iOS, Android et Web avec les versions minimales de SDK suivantes :

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

Vous avez besoin d'une prise en charge sur d'autres plateformes ? Contactez notre équipe par e-mail : [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

### Quel est le niveau d'effort nécessaire pour implémenter un indicateur de fonctionnalité ? {#level-of-effort}

Un indicateur de fonctionnalité peut être créé et intégré en quelques minutes.

La majeure partie de l'effort sera liée au développement par votre équipe d'ingénierie de la nouvelle fonctionnalité que vous prévoyez de déployer. Mais en ce qui concerne l'ajout d'un indicateur de fonctionnalité, c'est aussi simple qu'une instruction `IF`/`ELSE` dans le code de votre application ou de votre site web :

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

### En quoi les indicateurs de fonctionnalité sont-ils utiles aux équipes marketing ? {#marketing-teams}

Les équipes marketing peuvent utiliser les indicateurs de fonctionnalité pour coordonner les annonces produit (comme les e-mails de lancement de produit) lorsqu'une fonctionnalité n'est activée que pour un faible pourcentage d'utilisateurs.

Par exemple, avec les indicateurs de fonctionnalité de Braze, vous pouvez déployer un nouveau programme de fidélité client auprès de 10 % des utilisateurs de votre application, et envoyer un e-mail, une notification push ou tout autre message à ces mêmes 10 % d'utilisateurs activés grâce à l'étape Indicateur de fonctionnalité de Canvas.

### En quoi les indicateurs de fonctionnalité sont-ils utiles aux équipes produit ? {#product-teams}

Les équipes produit peuvent utiliser les indicateurs de fonctionnalité pour effectuer des déploiements progressifs ou des lancements en douceur de nouvelles fonctionnalités, afin de surveiller les KPI et les retours clients avant de les rendre disponibles à tous les utilisateurs.

Les équipes produit peuvent utiliser les [propriétés des indicateurs de fonctionnalité]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#properties) pour alimenter à distance le contenu d'une application, comme des liens profonds, du texte, des images ou tout autre contenu dynamique.

Grâce à l'étape Indicateur de fonctionnalité de Canvas, les équipes produit peuvent également réaliser un test A/B pour mesurer l'impact d'une nouvelle fonctionnalité sur les taux de conversion par rapport aux utilisateurs pour lesquels la fonctionnalité est désactivée.

### En quoi les indicateurs de fonctionnalité sont-ils utiles aux équipes d'ingénierie ? {#engineering-teams}

Les équipes d'ingénierie peuvent utiliser les indicateurs de fonctionnalité pour réduire les risques inhérents au lancement de nouvelles fonctionnalités et éviter de devoir déployer des correctifs de code en urgence au milieu de la nuit.

En publiant du nouveau code masqué derrière un indicateur de fonctionnalité, votre équipe peut activer ou désactiver la fonctionnalité à distance depuis le tableau de bord de Braze, sans avoir à attendre la publication d'une nouvelle version du code ou l'approbation d'une mise à jour sur l'app store.

## Déploiement de fonctionnalités et ciblage {#feature-rollouts-and-targeting}

### Un indicateur de fonctionnalité peut-il être déployé uniquement auprès d'un groupe spécifique d'utilisateurs ? {#target-users}

Oui, créez un segment dans Braze qui cible des utilisateurs spécifiques&mdash;par adresse e-mail, `user_id` ou tout autre attribut de vos profils utilisateur. Ensuite, déployez l'indicateur de fonctionnalité pour 100 % de ce segment.

### Comment l'ajustement du pourcentage de déploiement affecte-t-il les utilisateurs qui étaient précédemment placés dans le groupe activé ? {#random-buckets}

Les déploiements d'indicateurs de fonctionnalité restent cohérents pour les utilisateurs, quel que soit l'appareil ou la session.

- Lorsqu'un indicateur de fonctionnalité est déployé auprès de 10 % d'utilisateurs aléatoires, ces 10 % restent activés pendant toute la durée de vie de cet indicateur de fonctionnalité.
- Si vous augmentez le déploiement de 10 % à 20 %, les mêmes 10 % restent activés, et 10 % supplémentaires d'utilisateurs sont ajoutés au groupe activé.
- Si vous réduisez le déploiement de 20 % à 10 %, seuls les 10 % d'utilisateurs d'origine restent activés.

Cette stratégie garantit que les utilisateurs bénéficient d'une expérience cohérente dans votre application et ne voient pas la fonctionnalité apparaître et disparaître d'une session à l'autre. Bien entendu, désactiver une fonctionnalité à 0 % supprimera tous les utilisateurs de l'indicateur de fonctionnalité, ce qui est utile si vous découvrez un bug ou si vous devez désactiver complètement la fonctionnalité.

## Sujets techniques {#technical-topics}

### Les indicateurs de fonctionnalité peuvent-ils être utilisés pour contrôler le moment où le SDK Braze est initialisé ? {#initialization}

Non, le SDK doit être initialisé pour télécharger et synchroniser les indicateurs de fonctionnalité pour l'utilisateur actuel. Cela signifie que vous ne pouvez pas utiliser les indicateurs de fonctionnalité pour limiter les utilisateurs qui sont créés ou suivis dans Braze.

### À quelle fréquence le SDK actualise-t-il les indicateurs de fonctionnalité ? {#refresh-frequency}

Les indicateurs de fonctionnalité sont actualisés au démarrage de la session et lors du changement d'utilisateur actif. Ils peuvent également être actualisés manuellement à l'aide de la [méthode d'actualisation]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#refreshing) du SDK. L'actualisation des indicateurs de fonctionnalité est soumise à une limite de débit d'une fois toutes les cinq minutes (susceptible de changer).

Gardez à l'esprit que les bonnes pratiques en matière de données recommandent de ne pas actualiser les indicateurs de fonctionnalité trop fréquemment (avec un risque de limitation de débit le cas échéant). Il est donc préférable de n'actualiser qu'avant qu'un utilisateur interagisse avec de nouvelles fonctionnalités, ou périodiquement dans l'application si nécessaire.

### Les indicateurs de fonctionnalité sont-ils disponibles lorsqu'un utilisateur est hors ligne ? {#offline}

Oui, une fois les indicateurs de fonctionnalité actualisés, ils sont stockés localement sur l'appareil de l'utilisateur et restent accessibles hors ligne.

### Que se passe-t-il si les indicateurs de fonctionnalité sont actualisés en cours de session ? {#listen-for-updates}

Les indicateurs de fonctionnalité peuvent être actualisés en cours de session. Dans certains cas, vous souhaiterez mettre à jour votre application si certaines variables ou votre configuration changent. Dans d'autres cas, vous préférerez ne pas la mettre à jour, afin d'éviter un changement brusque dans le rendu de votre interface utilisateur.

Pour contrôler ce comportement, [écoutez les mises à jour]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#updates) des indicateurs de fonctionnalité et déterminez s'il faut effectuer un nouveau rendu de votre application en fonction des indicateurs de fonctionnalité qui ont changé.

### Pourquoi les utilisateurs de mon Groupe de contrôle global ne reçoivent-ils pas les expériences d'indicateurs de fonctionnalité ? {#why-arent-users-in-my-global-control-group-receiving-feature-flags-experiments}

Vous ne pouvez pas activer les indicateurs de fonctionnalité pour les utilisateurs de votre [Groupe de contrôle global]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts). Cela signifie que les utilisateurs de votre Groupe de contrôle global ne peuvent pas non plus participer aux expériences d'indicateurs de fonctionnalité.

## D'autres questions ? {#additional-questions}

Vous avez des questions ou des commentaires ? Contactez notre équipe par e-mail : [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).