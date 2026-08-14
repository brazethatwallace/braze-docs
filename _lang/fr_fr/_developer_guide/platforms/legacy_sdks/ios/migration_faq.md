---
nav_title: FAQ sur la migration
article_title: FAQ sur la migration du SDK iOS
platform: iOS
page_order: 12
description: "Cette page répond aux questions fréquemment posées sur la migration du SDK iOS Appboy (Objective-C) vers le SDK Swift de Braze."
noindex: true
---

# FAQ sur la migration du SDK iOS {#ios-sdk-migration-faq}

> Cette page répond aux questions fréquemment posées sur la migration de l'ancien SDK iOS Appboy (également connu sous le nom de SDK Objective-C) vers le SDK Swift de Braze.

{% multi_lang_include deprecations/objective-c.md %}

## Prise en charge des versions et fin de vie {#version-support-and-end-of-life}

### Le SDK iOS Appboy 4.7.0 est-il en fin de vie ? {#is-appboy-ios-sdk-470-end-of-life}

Oui, le SDK iOS Appboy 4.7.0 (ainsi que toutes les versions 4.x) a atteint sa fin de vie. Aucun correctif de sécurité ni correctif de bogue critique n'est fourni. Bien que la communication et l'analyse continuent de fonctionner normalement, la version 4.7.0 doit être considérée comme non prise en charge du point de vue de la sécurité.

### Quelle est la version minimale du SDK Swift pour la prise en charge en production ? {#what-is-the-minimum-swift-sdk-version-for-production-support}

Les versions majeures actuelles (16.x et ultérieures) sont celles visées par la prise en charge continue, les correctifs de bogues et les nouvelles fonctionnalités. Les versions mineures plus anciennes peuvent ne pas bénéficier d'une maintenance continue.

## Bibliothèques de compatibilité {#compatibility-libraries}

### BrazeKitCompat et BrazeUICompat sont-elles prises en charge pour une utilisation en production avec le SDK Swift 17.x ? {#are-brazekitcompat-and-brazeuicompat-supported-for-production-use-on-swift-sdk-17x}

Oui, `BrazeKitCompat` et `BrazeUICompat` sont prises en charge pour une utilisation en production pendant la migration. Elles sont conçues comme un « tremplin » de migration minimale pour vous aider à passer du SDK Appboy au SDK Swift avec un minimum de modifications de code, et non comme une solution à long terme. Bien qu'elles soient officiellement prises en charge et continuent de recevoir des correctifs, l'intention est de migrer à terme de ces bibliothèques de compatibilité vers les API modernes du SDK Swift.

### Quand BrazeKitCompat et BrazeUICompat seront-elles supprimées ? {#when-will-brazekitcompat-and-brazeuicompat-be-removed}

L'équipe du SDK Swift prévoit de mettre fin à la bibliothèque `BrazeKitCompat`, mais aucun calendrier précis n'a encore été annoncé. Il est recommandé de planifier une migration complète vers les API modernes du SDK Swift (`BrazeKit`, `BrazeUI`) plutôt que de dépendre indéfiniment des bibliothèques de compatibilité.

## Initialisation différée {#delayed-initialization}

### Puis-je retarder l'initialisation du SDK jusqu'à ce que l'utilisateur ait donné son consentement ? {#can-i-delay-sdk-initialization-until-after-user-consent}

Oui. Le SDK Swift prend en charge l'initialisation différée, ce qui est utile pour les applications qui doivent attendre le consentement de l'utilisateur avant de démarrer le SDK. Appelez `Braze.prepareForDelayedInitialization()` (éventuellement avec un paramètre `analyticsBehavior`) au début de `application(_:didFinishLaunchingWithOptions:)`, puis initialisez le SDK ultérieurement en appelant l'initialiseur standard de Braze une fois le consentement recueilli.

Pour une mise en œuvre détaillée, consultez [Configurer l'initialisation différée]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift#swift_step-2-set-up-delayed-initialization-optional).

### Quelle est la version minimale du SDK Swift requise pour l'initialisation différée ? {#what-is-the-minimum-swift-sdk-version-required-for-delayed-initialization}

Le SDK Swift 11.2.0 est la version minimale pour l'initialisation différée. La robustesse des notifications push et des deep links pour l'initialisation différée a été améliorée dans la version 14.1.0. Le SDK Swift 17.0.0 dépasse largement ces deux seuils.

### Que se passe-t-il pour les événements reçus avant l'initialisation du SDK ? {#what-happens-to-events-received-before-the-sdk-is-initialized}

Lorsque le SDK est initialisé, les éléments en file d'attente sont traités. Cependant, le comportement varie selon le canal :

| Canal | Comportement avant l'initialisation |
|-------|--------------------------------------|
| Jetons push | Mis en file d'attente ; traités à l'initialisation |
| Ouvertures push / analyse | Mis en file d'attente par défaut (configurable pour être ignorés via `analyticsBehavior`) |
| Deep links | Mis en file d'attente ; traités à l'initialisation |
| In-App Messages | Non mis en mémoire tampon avant l'initialisation ; nécessitent que le SDK soit en cours d'exécution |
| Content Cards | Non mises en mémoire tampon avant l'initialisation ; synchronisées depuis le serveur après l'initialisation |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
La livraison des In-App Messages et des Content Cards reçus avant l'initialisation n'est pas garantie. Assurez-vous que le SDK est initialisé avant de tenter d'afficher ces canaux.
{% endalert %}

## Bundles de ressources et intégration SPM {#resource-bundles-and-spm-integration}

### Pourquoi est-ce que je vois une erreur d'exécution concernant `braze-swift-sdk_BrazeUI.bundle` manquant ? {#why-am-i-seeing-a-runtime-error-about-missing-braze-swift-sdk_brazeuibundle}

Il ne s'agit pas d'un bug connu du SDK, mais probablement d'une mauvaise configuration de l'intégration. À partir du SDK Swift 12.0.0, les XCFrameworks statiques incluent les ressources directement au lieu de s'appuyer sur des bundles de ressources externes.

### Quelles sont les exigences SPM/Xcode/archive pour l'intégration des ressources ? {#what-are-the-spmxcodearchive-requirements-for-resource-embedding}

À partir du SDK Swift 12.0.0, vous devez sélectionner **Embed & Sign** pour les XCFrameworks Braze dans les paramètres de votre projet Xcode — cela s'applique aux variantes statiques comme dynamiques. C'est la cause la plus fréquente des erreurs de bundle manquant lors de l'archivage ou de la mise en production.

### Comment remplacer les bundles de ressources pour les systèmes de build non standard ? {#how-do-i-override-resource-bundles-for-non-standard-build-systems}

Pour les systèmes de build non standard (Tuist, Bazel, Buck, CI), utilisez les API de remplacement approuvées :

- `BrazeKit.overrideResourcesBundle` (notez le pluriel « Resources »)
- `BrazeUI.overrideResourcesBundle` (notez le pluriel « Resources »)

La version au singulier `overrideResourceBundle` a été dépréciée dans le SDK Swift 8.1.0 et ne doit plus être utilisée.

## Identité utilisateur et jetons push {#user-identity-and-push-tokens}

### Existe-t-il une checklist de validation pour préserver les profils, les associations d'appareils et les jetons push ? {#is-there-a-validation-checklist-for-preserving-profiles-device-associations-and-push-tokens}

Il n'existe pas de checklist officielle spécifique à la migration dans la documentation. Nous vous recommandons d'effectuer les étapes de validation suivantes :

1. Confirmez que `registerDeviceToken` ou l'automatisation push est correctement configurée après la migration.
2. Vérifiez le nombre d'utilisateurs enregistrés pour les notifications push dans le tableau de bord avant et après le déploiement.
3. Effectuez des vérifications ponctuelles sur quelques ID externes spécifiques pour confirmer que les associations d'appareils sont toujours intactes.

### `changeUser` garantit-il que les jetons push suivent le nouvel utilisateur ? {#does-changeuser-guarantee-that-push-tokens-follow-the-new-user}

Il n'existe aucune garantie explicite documentée par écrit. Cependant, l'intention de conception est que les jetons push suivent l'appareil, et non l'utilisateur. L'appel à `changeUser` devrait réassocier le jeton d'appareil existant au nouveau profil utilisateur. Vous devriez tester `changeUser`, vérifier le tableau de bord et confirmer que le jeton apparaît sur le nouveau profil avant tout déploiement à grande échelle.