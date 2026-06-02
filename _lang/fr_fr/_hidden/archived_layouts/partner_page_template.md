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

## Exigences ou conditions préalables {#requirements-or-prerequisites}

Cette section détaille tout ce dont vous avez besoin pour intégrer ce partenaire et commencer à utiliser ses services. La meilleure façon de fournir ces informations est de rédiger un paragraphe d'instructions rapides qui décrit tous les détails non techniques importants ou les informations à connaître, comme le fait de savoir si votre intégration sera soumise ou non à des contrôles de sécurité ou à des habilitations supplémentaires. Utilisez ensuite un tableau pour décrire les exigences techniques de l'intégration.

{% alert important %}
Les exigences suivantes sont des exigences générales dont vous pourriez avoir besoin pour Braze. Nous vous recommandons d'utiliser le titrage, l'origine, les liens et le phrasé attribués dans le tableau suivant. Assurez-vous de modifier la description pour vous souvenir de ce que chacune de ces exigences permet de faire.
{% endalert %}

| Condition | Origine | Accès | Description |
|---|---|---|---|
| Clé REST API de l'espace de travail Braze | Plateforme Braze | Page **Settings** > **API Key** | Cette description devrait vous indiquer comment procéder avec la clé REST API de l'espace de travail. |
| Endpoint de l'API Braze | Plateforme Braze | Consultez la [liste de nos endpoints]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) ou créez un [ticket d'assistance]({{site.baseurl}}/braze_support/). | Description en attente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Intégration [type d'intégration] {#type-of-integration-integration}

C'est ici que vous décomposez l'intégration en étapes. N'écrivez pas de paragraphes sans fin : il s'agit de documents techniques qui seront utilisés par des marketeurs et des développeurs à des fins d'intégration et d'exécution. Dans cette section, votre seul objectif est d'écrire une documentation descriptive qui aide l'utilisateur de Braze à accomplir sa tâche. Par « type d'intégration » dans le titre de la section, nous entendons indiquer s'il s'agit d'une intégration côte à côte, serveur à serveur ou par défaut. Cela vous permet d'avoir plusieurs sections d'intégration s'il existe plus d'une méthode d'intégration pour ce partenaire.

S'il s'agit d'une intégration Currents, cette page doit se trouver dans la section Currents et vous devrez créer une page de navigation qui redirige vers cet emplacement dans Currents.

### Étape 1 : brève description de la première étape {#step-1-this-is-a-short-description-of-step-one}

Décomposez l'étape en incluant du code si nécessaire. N'oubliez pas que vous pouvez proposer plusieurs jeux de code : rien ne vous oblige à ne proposer qu'un seul moyen d'intégration.

### Étape 2 : cette étape décrit les images {#step-2-this-step-will-describe-images}

Vous avez la possibilité d'ajouter des images dans votre documentation. Nous vous recommandons de le faire, et de le faire avec attention.

### Étape 3 : combien d'étapes {#step-3-how-many-steps}

Décrivez l'utilisation de l'intégration, surtout si elle inclut l'insertion de Liquid dans notre éditeur de messages.

## Personnalisation {#customization}

Cette section est **facultative**. Ici, vous pouvez présenter des manières spécifiques de personnaliser votre intégration entre les deux partenaires.

## Comment utiliser cette intégration {#using-this-integration}

Expliquez ici comment utiliser l'intégration en indiquant à vos lecteurs s'ils doivent cliquer sur quelques boutons ou s'ils n'ont rien besoin de faire après l'intégration.

### Étape 1 : brève description de la première étape

Décrivez simplement le processus étape par étape.

## Cas d'utilisation {#use-cases}

Il s'agit de l'une des parties les plus importantes de votre documentation. Bien que ce ne soit pas obligatoire, vous pouvez définir à cet endroit les cas d'utilisation types ou même inédits de l'intégration. Cela peut servir à vendre ou à proposer une montée en gamme de la relation. Ces explications apportent du contexte, des idées et, surtout, un moyen de mieux comprendre les capacités de l'intégration.