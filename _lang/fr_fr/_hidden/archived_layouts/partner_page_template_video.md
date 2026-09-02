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

## Conditions préalables {#requirements-or-prerequisites}

Cette section présente tout ce dont vous avez besoin pour intégrer le partenaire et commencer à utiliser ses services. La meilleure façon de communiquer ces informations est d'utiliser un court paragraphe explicatif qui décrit les détails importants non techniques à connaître, comme le fait que votre intégration sera soumise ou non à des vérifications de sécurité ou des autorisations supplémentaires. Ensuite, vous devriez utiliser un tableau pour décrire les exigences techniques de l'intégration.

{% alert important %}
Les exigences suivantes sont des exigences typiques que vous pourriez rencontrer avec Braze. Nous vous recommandons d'utiliser les titres, origines, liens et formulations indiqués dans le tableau suivant. Veillez à ajuster la description afin de savoir à quoi chacune de ces exigences est utilisée.
{% endalert %}

| Exigence | Origine | Accès | Description |
|---|---|---|---|
| Clé API REST de l'espace de travail Braze | Plateforme Braze | Page **Paramètres** > **Paramètres de l'application** | Cette description devrait vous indiquer quoi faire avec la clé API REST de l'espace de travail. |
| Endpoint API Braze | Plateforme Braze | Consultez nos [endpoints répertoriés]({{site.baseurl}}/api/basics#endpoints) ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support). | Description en attente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Conditions préalables" }

## Intégration [Type d'intégration] {#type-of-integration-integration}

C'est ici que vous décomposez l'intégration en étapes. N'écrivez pas simplement des paragraphes interminables : il s'agit de documents techniques qui seront utilisés aussi bien par les marketeurs que par les développeurs pour mettre en place l'intégration. Votre seul objectif pour cette section est de rédiger une documentation descriptive qui aide l'utilisateur de Braze à accomplir sa tâche. Par « Type d'intégration » dans le titre de la section, nous souhaitons indiquer s'il s'agit d'une intégration côte à côte, serveur à serveur ou par défaut. Cela vous permet d'avoir plusieurs sections d'intégration s'il existe plus d'une façon de s'intégrer avec ce partenaire.

S'il s'agit d'une intégration Currents, cette page doit se trouver dans la section Currents, et une page de navigation correspondante doit être créée pour rediriger vers cet emplacement dans Currents.

### Étape 1 : Brève description de la première étape {#step-1-this-is-a-short-description-of-step-one}

Décomposez simplement le processus, en incluant tout le code nécessaire. N'oubliez pas que vous pouvez proposer plusieurs ensembles de code différents : il n'est pas nécessaire de n'offrir qu'une seule façon de s'intégrer.

### Étape 2 : Cette étape décrit les images {#step-2-this-step-will-describe-images}

Vous avez la possibilité d'inclure des images dans votre documentation, nous vous recommandons donc de le faire de manière réfléchie.

### Exemple de code {#code-sample}

Si vous expliquez un concept technique, notez-le ici et montrez un exemple de code.

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

Assurez-vous de définir les paramètres ou les éléments que les utilisateurs pourraient avoir à ajuster dans l'exemple de code. De nombreux utilisateurs se contenteront de copier-coller.

| Variable | Description |
| -------- | ----------- |
| Page Title | Vous pouvez donner n'importe quel titre à votre page. C'est obligatoire. |
| My First Heading | Nous recommandons de le mettre en majuscules. C'est également facultatif. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exemple de code" }


### Étape 3 : Combien d'étapes {#step-3-how-many-steps}

Décrivez l'utilisation de l'intégration, en particulier si cela implique d'insérer du Liquid dans notre composeur de messages.

## Personnalisation {#customization}

Il s'agit d'une section **facultative**. Ici, vous pouvez décrire les différentes façons de personnaliser votre intégration entre les deux partenaires.

## Utilisation de cette intégration {#using-this-integration}

Cette section décrit comment utiliser l'intégration. Indiquez à votre lecteur s'il doit appuyer sur quelques boutons ou s'il n'a rien à faire après l'intégration.

### Étape 1 : Brève description de la première étape

Il s'agit d'un guide classique, étape par étape.

### Exemple de code

Si vous expliquez un concept technique, précisez-le ici et montrez un exemple de code.

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

Veillez à définir les paramètres ou les éléments que les utilisateurs pourraient devoir adapter à partir de l'exemple de code. De nombreux utilisateurs se contenteront de copier-coller.

| Variable | Description |
| -------- | ----------- |
| Page Title | Vous pouvez donner le titre de votre choix à votre page. Ce champ est obligatoire. |
| My First Heading | Nous recommandons de l'écrire en majuscules. Ce champ est facultatif. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exemple de code" }

## Cas d'usages {#use-cases}

Cela peut constituer une partie essentielle de votre documentation. Bien que cette section soit facultative, c'est un bon endroit pour présenter les cas d'usages typiques, voire inédits, de l'intégration. Cela peut servir à promouvoir ou à renforcer la relation partenaire : cette section fournit du contexte, des idées et, surtout, un moyen de visualiser les capacités de l'intégration.