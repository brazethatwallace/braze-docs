---
nav_title: Page partenaire

page_order: 4

#Required
description: "Il s'agit de la description Google Search. Les phrases de plus de 160 caractères seront tronquées, soyez concis."
page_type: partner
tool:
  - Dashboard
  - Docs
  - Canvas
  - Campaigns
  - Segments
  - Templates
  - Media
  - Location
  - Currents
  - Reports

platform:
  - iOS
  - Android
  - Web
  - API

channel:
  - Content Cards
  - Email
  - News Feed
  - In-App Messages
  - Push
  - SMS
  - Webhooks


noindex: true
#ATTENTION: remove noindex and this alert from template

---

# [Nom du partenaire] {#partner-name}

> Bienvenue dans le modèle de la page partenaire ! Ici, vous trouverez tout ce dont vous avez besoin pour créer votre propre page partenaire. Dans cette première section, ajoutez une phrase ou deux pour décrire le partenaire dans le premier paragraphe. Pensez également à ajouter un lien vers le site principal du partenaire.

Dans le second paragraphe, explorez et expliquez la relation entre Braze et ce partenaire. Ce paragraphe doit expliquer comment Braze et ce partenaire collaborent pour resserrer le lien entre l'utilisateur de Braze et son client. Expliquez la « valeur ajoutée » qui se produit lorsqu'un utilisateur de Braze s'intègre ou tire parti de ce partenaire et des services qu'il propose.

## Conditions requises ou prérequis {#requirements-or-prerequisites}

Cette section concerne tout ce dont vous avez besoin pour intégrer le partenaire et commencer à utiliser ses services. La meilleure façon de présenter ces informations est d'utiliser un court paragraphe d'instructions décrivant les détails non techniques importants à connaître, par exemple si votre intégration sera soumise à des vérifications de sécurité ou des autorisations supplémentaires. Ensuite, vous devriez utiliser un tableau pour décrire les exigences techniques de l'intégration.

{% alert important %}
Les conditions suivantes sont des exigences typiques que vous pourriez rencontrer de la part de Braze. Nous vous recommandons d'utiliser les titres, origines, liens et formulations indiqués dans le tableau suivant. Veillez à adapter la description afin de savoir à quoi chacune de ces exigences est utilisée.
{% endalert %}

| Condition | Origine | Accès | Description |
|---|---|---|---|
| Clé API REST de l'espace de travail Braze | Plateforme Braze | Page **Paramètres** > **Clé API** | Cette description devrait vous indiquer quoi faire avec la clé API REST de l'espace de travail. |
| Endpoint de l'API Braze | Plateforme Braze | Consultez nos [endpoints répertoriés]({{site.baseurl}}/api/basics#endpoints) ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support). | Description en attente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Conditions requises ou prérequis" }

## Intégration [type d'intégration] {#type-of-integration-integration}

C'est ici que vous décomposez l'intégration en étapes. N'écrivez pas simplement des paragraphes interminables : il s'agit de documents techniques qui seront utilisés aussi bien par les marketeurs que par les développeurs pour mettre en place l'intégration. Votre seul objectif pour cette section est de rédiger une documentation descriptive qui aide l'utilisateur de Braze à accomplir sa tâche. Par « type d'intégration » dans le titre de la section, nous entendons indiquer s'il s'agit d'une intégration côte à côte, serveur à serveur ou par défaut. Cela vous permet d'avoir plusieurs sections d'intégration s'il existe plus d'une façon de s'intégrer avec ce partenaire.

S'il s'agit d'une intégration Currents, cette page devrait se trouver dans la section Currents, et une page de navigation correspondante devrait être créée pour rediriger vers cet emplacement dans Currents.

### Étape 1 : Ceci est une brève description de la première étape {#step-1-this-is-a-short-description-of-step-one}

Décomposez simplement le processus, en incluant tout code nécessaire. N'oubliez pas que vous pouvez proposer plusieurs ensembles de code différents : il n'est pas nécessaire de n'offrir qu'une seule façon de s'intégrer.

### Étape 2 : Cette étape décrit les images {#step-2-this-step-will-describe-images}

Vous avez la possibilité d'inclure des images dans votre documentation, nous vous recommandons donc de le faire et de le faire de manière réfléchie.

### Étape 3 : Combien d'étapes {#step-3-how-many-steps}

Décrivez le processus d'utilisation de l'intégration, en particulier s'il implique l'insertion de Liquid dans notre composeur de messages.

## Personnalisation {#customization}

Il s'agit d'une section **facultative**. Ici, vous pouvez décrire les moyens spécifiques de personnaliser votre intégration entre les deux partenaires.

## Utiliser cette intégration {#using-this-integration}

Cette section décrit comment utiliser l'intégration. Indiquez à votre lecteur s'il doit appuyer sur quelques boutons ou s'il n'a rien à faire après l'intégration.

### Étape 1 : Brève description de la première étape

Un guide classique, étape par étape.

## Cas d'usages {#use-cases}

Cela peut constituer une partie essentielle de votre documentation. Bien que cette section soit facultative, c'est un excellent endroit pour présenter des cas d'usages typiques, voire innovants, de l'intégration. Elle peut servir à valoriser ou renforcer la relation partenaire : elle fournit du contexte, des idées, et surtout un moyen de visualiser les capacités de l'intégration.