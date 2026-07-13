---
nav_title: B.Layer
article_title: B.Layer
description: "Cet article de référence décrit le partenariat entre Braze et B.Layer, un générateur de messages in-app, que vous pouvez utiliser pour créer des messages in-app personnalisés simplement, rapidement et sans codage."
alias: /partners/blayer-inapps/
page_type: partner
search_tag: Partner

---

# B.Layer

> [B.Layer](https://blayer.phiture.com) est le générateur de messages in-app de Phiture qui aide les équipes CRM des applications mobiles à créer des messages in-app personnalisés de manière simple, rapide et sans codage.

_Cette intégration est maintenue par B.Layer._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et de B.Layer vous permet d'utiliser le générateur de messages in-app B.Layer pour créer des messages in-app à votre image, exportables sous forme de fichier ZIP ou de HTML en ligne vers Braze. Cette intégration ne nécessite pas de ressources de développement supplémentaires, ce qui vous permet d'économiser du temps et de l'argent.

![Interface du générateur B.Layer affichant un aperçu d'un message in-app personnalisé.]({% image_buster /assets/img/blayer/blayer2.png %})

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte B.Layer | Un compte [B.Layer](https://blayer.phiture.com) est nécessaire pour bénéficier de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'usage {#use-cases}

Avec B.Layer, les possibilités de création et d'expérimentation sont infinies : curseurs de recommandation produit, onboarding multi-écrans ou enquêtes, NPS, capture d'e-mails, offres spéciales, et bien plus encore.

Ils travaillent avec des marques telles que Lifesum, Blinkist, OnX Hunt et bien d'autres pour améliorer l'expérience utilisateur sans ressources supplémentaires. Nous figurons également parmi les finalistes des APS Awards 2022 dans la catégorie innovation en matière d'applications.

## Intégration {#integration}

### Étape 1 : Créez votre message in-app {#step-1-create-your-in-app-message}

#### Définissez les couleurs et les polices de la marque {#set-brand-colors-and-fonts}

Dans B.Layer, dans le menu hamburger en haut de la page, cliquez sur **Brand assets > add your brand assets**. Vous pouvez y attribuer les couleurs et les polices de votre marque.
Tout est prêt. Vous pouvez maintenant commencer à concevoir votre message in-app.

![Écran des ressources de marque B.Layer pour configurer les couleurs et les polices.]({% image_buster /assets/img/blayer/blayer4.png %})

#### Concevez votre message in-app {#design-your-in-app-message}

Pour concevoir votre message in-app, sélectionnez un seul message in-app. Ensuite, mettez en forme votre message et ajoutez les composants dont vous avez besoin. Chaque composant peut être ajusté.

![Éditeur de messages B.Layer avec les composants et les contrôles de style.]({% image_buster /assets/img/blayer/blayer5.png %})

### Téléchargez votre message in-app {#download-your-in-app-message}

Une fois que vous avez terminé, téléchargez votre message. Votre message peut être téléchargé au format ZIP ou HTML en ligne.

### Étape 2 : Ajoutez le code personnalisé B.Layer {#step-2-add-blayer-custom-code}

Dans Braze, créez un message in-app avec code personnalisé. Si vous possédez un fichier ZIP, faites-le glisser et déposez-le dans la zone de téléchargement de cette section. Si vous avez un fichier HTML en ligne, collez-le dans la section HTML.

![Éditeur de messages in-app avec code personnalisé dans Braze avec le contenu exporté depuis B.Layer.]({% image_buster /assets/img/blayer/blayer6.png %})

## Suivi des boutons {#button-tracking}

Avec B.Layer, vous pouvez enregistrer les interactions avec les boutons ou la saisie de texte en tant qu'attribut Braze. Cela peut être fait directement dans l'éditeur. Un exemple courant est une enquête NPS.

B.Layer utilise le suivi des boutons Braze ajouté aux liens que vous saisissez (par exemple, `?button=0`). Vous pouvez ainsi voir les clics sur les boutons dans la section d'analyse de votre Campaign.