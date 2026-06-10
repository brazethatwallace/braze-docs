---
nav_title: Judo
article_title: Judo
description: "Cet article de référence décrit le partenariat entre Braze et Judo, une plateforme d'interface utilisateur sans code pilotée par serveur qui vous permet d'ajouter un contexte de localisation et un suivi à vos applications iOS et Android."
alias: /partners/judo/
page_type: partner
search_tag: Partner

---

# Judo

> [Judo](https://judo.app) est une plateforme d'interface utilisateur pilotée par serveur qui permet aux éditeurs de fournir efficacement des expériences utilisateur riches et engageantes dans l'application, sans mise à jour de l'application.

_Cette intégration est maintenue par Judo._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Judo offre des expériences sur mesure dans vos Campaigns et Canvas. Au lieu d'une simple expérience de page de destination modélisée, une Campaign Braze peut incorporer du contenu comprenant plusieurs écrans, fenêtres modales, vidéos, polices personnalisées et des paramètres tels que le mode sombre et l'accessibilité, le tout créé sans code et déployé sans mise à jour de l'application. Les données de Braze peuvent également être utilisées pour alimenter le contenu personnalisé dans une expérience Judo. Les événements utilisateur et les données de l'expérience peuvent être réinjectés dans Braze pour l'attribution et le ciblage.

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte Judo | Un compte [Judo](https://www.judo.app/) est requis pour profiter de ce partenariat. |
| SDK Judo | Le SDK Judo doit être intégré dans vos applications [iOS](https://github.com/judoapp/judo-ios/) et/ou [Android](https://github.com/judoapp/judo-android). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'utilisation {#use-cases}

**Onboarding** : Les éditeurs d'applications utilisant Judo créent et déploient des expériences d'onboarding riches et natives. Ces expériences peuvent désormais constituer un élément d'un parcours d'onboarding cross-canal personnalisé coordonné via Braze. Les expériences peuvent être personnalisées et rapidement mises à jour sans aucune mise à jour de l'application pour tester l'efficacité des différents flux in-app.

**Conversion** : Les éditeurs d'applications peuvent utiliser les données de Braze pour créer une expérience riche et personnalisée dans l'application afin de stimuler les achats intégrés, les abonnements payants ou le merchandising contextuel en utilisant des hooks d'intégration dans Judo. L'accès à ces expériences peut être déclenché via des Campaigns de marketing d'engagement créées dans Braze.

**Contenu piloté par les événements** : L'une des principales utilisations de Judo dans le sport et le divertissement est de créer des expériences riches pour prévisualiser, promouvoir et récapituler des événements. Cette capacité peut être largement appliquée dans d'autres secteurs pour le contenu saisonnier et axé sur l'actualité. Lier l'envoi de messages pour promouvoir ou mettre en avant des événements en temps opportun à des expériences riches dans l'application permet aux éditeurs de stimuler l'engagement en étant contextuellement pertinents.

## Intégration SDK côte à côte {#side-by-side-sdk-integration}

Judo propose des bibliothèques supplémentaires qui automatisent une partie de l'effort nécessaire pour intégrer les SDK Judo et Braze côte à côte dans vos applications mobiles.

### Étape 1 : Installer la bibliothèque d'intégration Judo-Braze {#step-1-install-the-judo-braze-integration-library}

Installez et configurez la bibliothèque d'intégration Judo-Braze dans vos applications. Cela activera automatiquement le suivi des événements.

- [Instructions d'installation
iOS](https://github.com/judoapp/judo-braze-ios/wiki#installation)
- [Instructions d'installation
Android](https://github.com/judoapp/judo-braze-android/wiki#installation).

### Étape 2 : Configurer les messages in-app {#step-2-configure-in-app-messaging}

Cette étape implique la création d'implémentations personnalisées de `ABKInAppMessageControllerDelegate` et `IInAppMessageManagerListener` pour iOS et Android.

Consultez la documentation de configuration des messages in-app fournie pour chacune des bibliothèques d'intégration :

- [Configuration des messages in-app
iOS](https://github.com/judoapp/judo-braze-ios/wiki#in-app-messaging-setup)
- [Configuration des messages in-app
Android](https://github.com/judoapp/judo-braze-android/wiki#in-app-messaging-setup).

## Utiliser cette intégration {#using-this-integration}

Une fois l'intégration côté application terminée, vous pouvez la tester en lançant une Campaign de message in-app de test dans Braze pour une expérience Judo afin de vérifier qu'elle fonctionne comme prévu.

### Étape 1 : Créer une Campaign de message in-app avec code personnalisé {#step-1-create-a-custom-code-in-app-message-campaign}

Depuis la plateforme Braze, créez une Campaign de message in-app Braze avec un type de message **Custom Code**. Ensuite, sélectionnez **HTML Upload** comme type personnalisé. Assurez-vous de remplir le contenu du message avec les champs de base des messages in-app ; ce contenu ne sera pas affiché à l'utilisateur.

![Image montrant l'apparence du tableau de bord lors de la sélection du type de message « Custom Code ».]({% image_buster /assets/img/judo/braze-campaign-select-custom-type.png %})

Ensuite, utilisez l'extrait de code HTML minimal suivant pour satisfaire la validation du formulaire :
```
<a href="appboy://close">X</a>
```

Notez que cela ne sera pas affiché en production sur votre appareil, car Judo réécrira et remplacera ce contenu par une expérience Judo.

![Image montrant le code de validation de formulaire ajouté à l'étape de rédaction de votre Campaign.]({% image_buster /assets/img/judo/braze-html-boilerplate.png %})

### Étape 2 : Définir une paire clé-valeur pour Judo {#step-2-set-a-key-value-pair-for-judo}
![Cette image montre la seule paire clé-valeur nécessaire pour cette intégration, avec la « clé » étant « judo-experience » et la « valeur » étant votre lien Judo.]({% image_buster /assets/img/judo/braze-campaign-extras-judo-experience.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Définissez une [paire clé-valeur personnalisée]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs/) sur la Campaign avec une clé `judo-experience`. Fournissez l'URL de l'expérience Judo que vous souhaitez afficher ici. La bibliothèque d'intégration Judo-Braze détectera alors cette paire clé-valeur dans le gestionnaire et l'utilisera pour injecter votre expérience Judo à la place de l'interface utilisateur standard du message in-app de Braze.
<br><br>
### Étape 3 : Terminer la Campaign {#step-3-finishing-the-campaign}

Enfin, terminez la Campaign, configurez un déclencheur pour la Campaign et sélectionnez les utilisateurs via les Segments dans les sections **Delivery** et **Target User**. Consultez notre [article]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/) sur les messages in-app pour en savoir plus sur les différents composants d'un message in-app Braze.