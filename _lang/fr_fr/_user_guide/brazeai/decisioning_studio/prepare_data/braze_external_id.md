---
nav_title: Utiliser l'ID externe Braze
article_title: Utiliser l'ID externe Braze
page_order: 5
page_type: reference
description: "Cet article de référence explique pourquoi Decisioning Studio utilise l'ID externe Braze comme unité d'identité client et ce qui se passe si une structure d'identifiant différente est utilisée."
---

# Utiliser l'ID externe Braze {#use-braze-external-id}

> Decisioning Studio nécessite un identifiant client unique et stable, cohérent à travers toutes les ressources de données. La recommandation est d'utiliser l'ID externe Braze comme identifiant. Cet article explique pourquoi, et quels risques apparaissent lorsque d'autres structures d'identifiants sont utilisées à la place.

## Pourquoi utiliser l'ID externe Braze ? {#why-use-braze-external-id}

Decisioning Studio fonctionne exclusivement en utilisant l'ID externe Braze comme unité d'identité client. Toutes les ressources de données (profils clients, caractéristiques, activations, engagements, conversions) doivent référencer l'ID externe Braze comme identifiant client principal.

Au-delà d'une exigence technique, imposer l'ID externe Braze est un choix de conception délibéré qui protège la fiabilité de l'entraînement du modèle et de ses recommandations.

### Défis liés aux autres identifiants {#challenges-of-other-identifiers}

De nombreuses organisations maintiennent deux systèmes d'identifiants clients différents :

- **Un ID d'entrepôt de données ou de système de référence** (parfois appelé « ID canonique » ou « ID physique ») : la source de vérité pour des indicateurs comme la valeur vie client, les retours et la fidélité. Il réside dans votre entrepôt de données ou votre ERP.
- **Un ID de plateforme :** l'identifiant utilisé par des outils comme Braze, généralement lié à une adresse e-mail, un jeton d'appareil ou un canal d'activation similaire.

La tentation est d'utiliser l'ID d'entrepôt de données pour construire les caractéristiques client (puisque c'est là que résident les données) et l'ID Braze pour l'activation (puisque c'est ce que Braze utilise). Mais cela nécessite une couche de traduction entre les deux systèmes, et cette couche de traduction introduit de la fragilité.

#### Dérive d'identité {#identity-drift}

Même si le mappage entre votre ID d'entrepôt de données et votre ID Braze est actuellement de type un-vers-plusieurs (un client physique correspond à plusieurs profils Braze), ce mappage peut se déstabiliser au fil du temps pour devenir plusieurs-vers-plusieurs. Si un seul ID d'entrepôt de données est réattribué à différents clients au fil du temps, ou si le même profil Braze devient associé à plusieurs ID d'entrepôt de données, le résultat est une **dérive d'identité**.

La dérive d'identité provoque :

- **Des échecs d'entraînement du modèle :** si le client auquel le modèle pensait recommander est en réalité une personne différente, le signal d'entraînement est corrompu.
- **Des inexactitudes dans les rapports :** les indicateurs perdent leur sens lorsque le mappage d'identité sous-jacent est instable.
- **Des erreurs d'attribution :** les conversions sont associées aux mauvaises recommandations.

### Comment l'ID externe Braze répond à ces risques {#how-braze-external-id-addresses-these-risks}

#### Prêt pour l'activation dès la conception {#activation-ready-by-design}

Les recommandations générées à partir d'un ID externe Braze peuvent être injectées directement dans les messages via Liquid ou le Contenu connecté, sans aucune étape de traduction d'identifiant. L'élimination de la couche de traduction supprime une source significative de complexité opérationnelle et de défaillance.

#### Isolé des changements en amont {#isolated-from-upstream-changes}

En opérant sur l'ID externe Braze, Decisioning Studio est protégé des changements dans vos systèmes en amont. Si votre ID d'entrepôt de données interne change en raison d'une migration de système, d'une correction de qualité des données ou d'une mise à jour ERP, l'ID externe Braze, et tout ce qui y est associé, reste stable.

#### Séparation nette des canaux {#clean-channel-separation}

Dans Braze, un profil utilisateur correspond à un canal de communication joignable. Si un client enregistre deux adresses e-mail, il dispose de deux profils Braze distincts avec deux ID externes Braze distincts. Decisioning Studio les traite comme deux entités séparées, ce qui signifie que les recommandations et l'historique des événements pour un e-mail ne sont pas contaminés par l'activité associée à l'autre.

Cela empêche ce que l'on pourrait appeler le « glissement de contexte ». Le moteur de recommandation ne mélangerait pas, par exemple, un comportement d'achat professionnel dans des recommandations envoyées à un compte e-mail personnel.

## Considérations multi-entités {#multi-entity-considerations}

### Entreprises multi-magasins ou hiérarchiques {#multi-store-or-hierarchical-businesses}

Pour les entreprises qui exploitent plusieurs points de vente ou sous-marques (par exemple, un franchiseur avec de nombreux franchisés), le concept de « client » peut être ambigu. Un client qui achète dans plusieurs emplacements peut avoir des enregistrements séparés à chaque emplacement, mais devrait être traité comme une seule personne à des fins de recommandation.

Si votre entreprise a cette structure, discutez avec votre équipe Decisioning Studio de la manière de modéliser la hiérarchie client avant de finaliser votre stratégie d'identifiant.

### Fragmentation d'identité B2C {#b2c-identity-fragmentation}

Une seule personne physique peut accumuler plusieurs profils Braze au fil du temps, par exemple en s'inscrivant avec différentes adresses e-mail ou en se connectant sur différents appareils avant la fusion des comptes. Decisioning Studio traite chaque ID externe Braze comme un client distinct.

C'est un choix de conception : chaque profil représente un canal d'activation distinct. Cependant, cela signifie que la qualité de vos recommandations dépend de la qualité de votre résolution d'identité Braze. Si votre implémentation Braze ne fusionne pas de manière fiable les profils en double, certains clients peuvent recevoir une personnalisation de moindre qualité parce que leur historique est fragmenté sur plusieurs profils.