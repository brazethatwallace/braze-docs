---
nav_title: Page partenaire avec vidéo

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

{% multi_lang_include video.html id="XY5uXoKIvFY" align="right" %}

> Bienvenue dans le modèle de page partenaire ! Ici, vous trouverez tout ce dont vous avez besoin pour créer votre propre page partenaire. Dans cette première section, décrivez le partenaire en une ou deux phrases dans le premier paragraphe. Pensez également à ajouter un lien vers le site principal du partenaire.

Dans le second paragraphe, explorez et expliquez la relation entre Braze et ce partenaire. Ce paragraphe doit expliquer comment Braze et ce partenaire collaborent pour resserrer le lien entre l'utilisateur de Braze et son client. Expliquez la « valeur ajoutée » qui se produit lorsqu'un utilisateur de Braze intègre ou exploite ce partenaire et ses services.

## Exigences ou conditions préalables {#requirements-or-prerequisites}

Cette section détaille tout ce dont vous avez besoin pour intégrer ce partenaire et commencer à utiliser ses services. La meilleure façon de fournir ces informations est de rédiger un court paragraphe d'instructions décrivant tous les détails non techniques importants ou les informations à connaître, comme le fait de savoir si votre intégration sera soumise ou non à des contrôles de sécurité ou à des habilitations supplémentaires. Utilisez ensuite un tableau pour décrire les exigences techniques de l'intégration.

{% alert important %}
Les exigences suivantes sont des exigences types dont vous pourriez avoir besoin pour Braze. Nous vous recommandons d'utiliser le titrage, l'origine, les liens et le phrasé attribués dans le tableau suivant. Assurez-vous d'ajuster la description afin de savoir à quoi sert chacune de ces exigences.
{% endalert %}

| Condition | Origine | Accès | Description |
|---|---|---|---|
| Clé API REST de l'espace de travail Braze | Plateforme Braze | Page **Settings** > **App Settings** | Cette description devrait vous indiquer comment procéder avec la clé API REST de l'espace de travail. |
| Endpoint de l'API Braze | Plateforme Braze | Consultez la [liste de nos endpoints]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/). | Description en attente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Exigences ou conditions préalables" }

## Intégration [type d'intégration] {#type-of-integration-integration}

C'est ici que vous décomposez l'intégration en étapes. N'écrivez pas de paragraphes interminables : il s'agit de documents techniques qui seront utilisés aussi bien par des marketeurs que par des développeurs pour mettre en place et faire fonctionner l'intégration. Votre seul objectif dans cette section est de rédiger une documentation descriptive qui aide l'utilisateur de Braze à accomplir sa tâche. Par « type d'intégration » dans le titre de la section, nous entendons indiquer s'il s'agit d'une intégration côte à côte, serveur à serveur ou par défaut. Cela vous permet d'avoir plusieurs sections d'intégration s'il existe plus d'une méthode d'intégration avec ce partenaire.

S'il s'agit d'une intégration Currents, cette page doit se trouver dans la section Currents et une page de navigation correspondante doit être créée pour rediriger vers cet emplacement dans Currents.

### Étape 1 : brève description de la première étape {#step-1-this-is-a-short-description-of-step-one}

Décomposez simplement l'étape, en incluant du code si nécessaire. N'oubliez pas que vous pouvez proposer plusieurs jeux de code : rien ne vous oblige à ne proposer qu'un seul moyen d'intégration.

### Étape 2 : cette étape décrit les images {#step-2-this-step-will-describe-images}

Vous avez la possibilité d'ajouter des images dans votre documentation. Nous vous recommandons de le faire, et de le faire avec attention.

### Exemple de code {#code-sample}

Si vous expliquez un concept technique, notez-le ici et présentez un exemple de code.

```html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
```

Pensez à définir les paramètres ou éléments que les utilisateurs devront ajuster dans l'exemple de code. De nombreux utilisateurs se contenteront de le copier-coller.

| Variable | Description |
| -------- | ----------- |
| Titre de la page | Choisissez le nom que vous voulez pour votre page. Ce champ est obligatoire. |
| Mon premier titre | Nous recommandons de le mettre en majuscules. Ce champ est toutefois facultatif. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exemple de code" }


### Étape 3 : combien d'étapes {#step-3-how-many-steps}

Décrivez l'utilisation de l'intégration, surtout si elle implique l'insertion de Liquid dans notre éditeur de messages.

## Personnalisation {#customization}

Cette section est **facultative**. Vous pouvez y présenter des manières spécifiques de personnaliser votre intégration entre les deux partenaires.

## Utiliser cette intégration {#using-this-integration}

Expliquez ici comment utiliser l'intégration en indiquant à vos lecteurs s'ils doivent cliquer sur quelques boutons ou s'ils n'ont rien à faire après l'intégration.

### Étape 1 : brève description de la première étape

Décrivez simplement le processus étape par étape.

### Exemple de code

Si vous expliquez un concept technique, notez-le ici et présentez un exemple de code.

```html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
```

Pensez à définir les paramètres ou éléments que les utilisateurs devront ajuster dans l'exemple de code. De nombreux utilisateurs se contenteront de le copier-coller.

| Variable | Description |
| -------- | ----------- |
| Titre de la page | Choisissez le nom que vous voulez pour votre page. Ce champ est obligatoire. |
| Mon premier titre | Nous recommandons de le mettre en majuscules. Ce champ est toutefois facultatif. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exemple de code" }


## Cas d'utilisation {#use-cases}

Il s'agit d'une partie essentielle de votre documentation. Bien que cette section soit facultative, c'est l'endroit idéal pour présenter les cas d'utilisation types ou même innovants de l'intégration. Cela peut servir à valoriser ou à proposer une montée en gamme de la relation : ces explications apportent du contexte, des idées et, surtout, un moyen de visualiser les capacités de l'intégration.