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

## Fonctionnalités et prise en charge {#functionality-and-support}

### Sur quelles plateformes les feature flags de Braze sont-ils pris en charge ? {#platforms}

Braze prend en charge les feature flags sur les plateformes iOS, Android et Web, avec les versions minimales de SDK suivantes :

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

Vous avez besoin d'une prise en charge sur d'autres plateformes ? Contactez notre équipe par e-mail : [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

### Quel est le niveau d'effort nécessaire pour implémenter un feature flag ? {#level-of-effort}

Un feature flag peut être créé et intégré en quelques minutes.

L'essentiel de l'effort sera lié au développement de la nouvelle fonctionnalité que vous prévoyez de déployer. Mais en ce qui concerne l'ajout d'un feature flag, c'est aussi simple qu'une instruction `IF`/`ELSE` dans le code de votre application ou de votre site web :

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

### Comment les feature flags peuvent-ils bénéficier aux équipes marketing ? {#marketing-teams}

Les équipes marketing peuvent utiliser les feature flags pour coordonner les annonces produit (comme les e-mails de lancement de produit) lorsqu'une fonctionnalité n'est activée que pour un faible pourcentage d'utilisateurs.

Par exemple, avec les feature flags de Braze, vous pouvez déployer un nouveau programme de fidélité client auprès de 10 % des utilisateurs de votre application, et envoyer un e-mail, une notification push ou tout autre message à ces mêmes 10 % d'utilisateurs activés à l'aide de l'étape Feature Flag dans Canvas.

### Comment les feature flags peuvent-ils bénéficier aux équipes produit ? {#product-teams}

Les équipes produit peuvent utiliser les feature flags pour effectuer des déploiements progressifs ou des lancements en douceur de nouvelles fonctionnalités afin de surveiller les indicateurs clés de performance et les retours clients avant de les rendre disponibles à tous les utilisateurs.

Les équipes produit peuvent utiliser les [propriétés de feature flags]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#properties) pour alimenter du contenu à distance dans une application, comme des deep links, du texte, des images ou d'autres contenus dynamiques.

Grâce à l'étape Feature Flag dans Canvas, les équipes produit peuvent également réaliser un test A/B pour mesurer l'impact d'une nouvelle fonctionnalité sur les taux de conversion par rapport aux utilisateurs pour lesquels la fonctionnalité est désactivée.

### Comment les feature flags peuvent-ils bénéficier aux équipes d'ingénierie ? {#engineering-teams}

Les équipes d'ingénierie peuvent utiliser les feature flags pour réduire les risques inhérents au lancement de nouvelles fonctionnalités et éviter de devoir déployer des correctifs de code en urgence en pleine nuit.

En publiant du nouveau code masqué derrière un feature flag, votre équipe peut activer ou désactiver la fonctionnalité à distance depuis le tableau de bord de Braze, sans attendre le déploiement d'une nouvelle version du code ni l'approbation d'une mise à jour par la boutique d'applications.

## Déploiement des fonctionnalités et ciblage {#feature-rollouts-and-targeting}

### Un feature flag peut-il être déployé uniquement pour un groupe restreint d'utilisateurs ? {#target-users}

Oui, créez un Segment dans Braze qui cible des utilisateurs spécifiques — par adresse e-mail, `user_id` ou tout autre attribut de vos profils utilisateur. Ensuite, déployez le feature flag pour 100 % de ce Segment.

### Comment l'ajustement du pourcentage de déploiement affecte-t-il les utilisateurs qui faisaient déjà partie du groupe activé ? {#random-buckets}

Les déploiements de feature flags restent cohérents pour les utilisateurs, quels que soient les appareils et les sessions.

- Lorsqu'un feature flag est déployé pour 10 % d'utilisateurs aléatoires, ces 10 % restent activés et persistent pendant toute la durée de vie de ce feature flag.
- Si vous augmentez le déploiement de 10 % à 20 %, les mêmes 10 % restent activés, et 10 % supplémentaires d'utilisateurs sont ajoutés au groupe activé.
- Si vous réduisez le déploiement de 20 % à 10 %, seuls les 10 % d'utilisateurs initiaux restent activés.

Cette stratégie permet de garantir que les utilisateurs bénéficient d'une expérience cohérente dans votre application et ne voient pas la fonctionnalité s'activer et se désactiver d'une session à l'autre. Bien entendu, désactiver une fonctionnalité en descendant à 0 % supprimera tous les utilisateurs du feature flag, ce qui est utile si vous découvrez un bug ou si vous devez désactiver complètement la fonctionnalité.

## Sujets techniques {#technical-topics}

### Les feature flags peuvent-ils être utilisés pour contrôler le moment où le SDK Braze est initialisé ? {#initialization}

Non, le SDK doit être initialisé pour télécharger et synchroniser les feature flags de l'utilisateur actuel. Cela signifie que vous ne pouvez pas utiliser les feature flags pour limiter les utilisateurs qui sont créés ou suivis dans Braze.

### À quelle fréquence le SDK actualise-t-il les feature flags ? {#refresh-frequency}

Les feature flags sont actualisés au démarrage de la session et lors du changement d'utilisateur actif. Les feature flags peuvent également être actualisés manuellement à l'aide de la [méthode d'actualisation]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#refreshing) du SDK. L'actualisation des feature flags est soumise à une limitation du débit d'une fois toutes les cinq minutes (susceptible de changer).

Gardez à l'esprit que les bonnes pratiques en matière de données recommandent de ne pas actualiser les feature flags trop rapidement (avec une limitation du débit potentielle le cas échéant). Il est donc préférable de ne les actualiser qu'avant qu'un utilisateur interagisse avec de nouvelles fonctionnalités ou périodiquement dans l'application si nécessaire.

### Les feature flags sont-ils disponibles lorsqu'un utilisateur est hors ligne ? {#offline}

Oui, une fois les feature flags actualisés, ils sont stockés localement sur l'appareil de l'utilisateur et sont accessibles hors connexion.

### Que se passe-t-il si les feature flags sont actualisés en cours de session ? {#listen-for-updates}

Les feature flags peuvent être actualisés en cours de session. Il existe des scénarios dans lesquels vous souhaiterez peut-être mettre à jour votre application si certaines variables ou votre configuration doivent changer. Il existe d'autres scénarios dans lesquels vous ne souhaiterez peut-être pas mettre à jour votre application, afin d'éviter un changement inattendu dans le rendu de votre interface utilisateur.

Pour contrôler ce comportement, [écoutez les mises à jour]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#updates) des feature flags et déterminez s'il est nécessaire de rafraîchir le rendu de votre application en fonction des feature flags qui ont changé.

### Pourquoi les utilisateurs de mon groupe de contrôle global ne reçoivent-ils pas les expériences de feature flags ? {#why-arent-users-in-my-global-control-group-receiving-feature-flags-experiments}

Vous ne pouvez pas activer les feature flags pour les utilisateurs de votre [groupe de contrôle global]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts). Cela signifie que les utilisateurs de votre groupe de contrôle global ne peuvent pas non plus participer aux expériences de feature flags.

### L'identification des destinataires par e-mail fait-elle partie des feature flags de Braze ? {#is-email-based-recipient-identification-part-of-braze-feature-flags}

Non. L'identification des destinataires par e-mail lors de l'envoi d'un message ne fait pas partie du produit Feature Flags présenté sur cette page. Les Feature Flags contrôlent les expériences in-app ou on-site via le SDK Braze.

Les envois de Campaign et de Canvas déclenchés par API peuvent inclure `email` dans l'[objet recipients]({{site.baseurl}}/api/objects_filters/recipient_object) au lieu d'un `external_user_id`. Lorsque vous utilisez `email`, incluez `prioritization` afin que Braze puisse sélectionner le profil utilisateur correspondant. Cette option d'envoi n'est pas disponible sur tous les espaces de travail.

Pour la structure de la requête, consultez [POST : Envoyer des Campaigns via une distribution déclenchée par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) et [POST : Envoyer des messages Canvas via une distribution déclenchée par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).

## Questions supplémentaires ? {#additional-questions}

Vous avez des questions ou des commentaires ? Envoyez un e-mail à notre équipe : [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).