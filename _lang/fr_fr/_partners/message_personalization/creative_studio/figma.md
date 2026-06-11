---
nav_title: Figma
article_title: Figma
description: "Cet article de référence décrit le partenariat entre Braze et Figma qui vous permet d'envoyer des images et des ressources visuelles dans la bibliothèque multimédia de Braze."
alias: /partners/figma/
page_type: partner
search_tag: Partner
---

# Figma

> [Figma](https://www.figma.com/) est une plateforme de conception collaborative qui vous permet de créer, concevoir et prototyper des produits.

## À propos de l'intégration {#about-the-integration}

L'intégration entre Braze et Figma vous permet d'envoyer des images et des ressources visuelles depuis Figma directement dans la bibliothèque multimédia de Braze.

Regardez cette vidéo pour un aperçu du fonctionnement de l'intégration.

{% multi_lang_include video.html id="ab5ywsi72n" source="wistia" %}

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte Figma | Un compte Figma est requis pour bénéficier de ce partenariat. |
| Accès à la bibliothèque multimédia de Braze | Vous devez disposer de la permission « Manage Media Library Assets » pour ajouter, modifier et supprimer des ressources de la bibliothèque multimédia dans Braze. |
| Accès à l'espace de travail Braze | Vous devez avoir accès aux espaces de travail dans lesquels vous souhaitez importer ces images et ressources visuelles Figma dans Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Installer le plugin Figma to Braze Export {#step-1-install-the-figma-to-braze-export-plugin}

Rendez-vous sur la communauté Figma pour accéder au [plugin Braze Export](https://www.figma.com/community/plugin/1606726267245196698/figma-to-braze-export). Sélectionnez **Open In** pour charger le plugin dans votre fichier Figma.

Dans Figma, vous pouvez également trouver le plugin Figma to Braze Export dans la section **Plugins**.

### Étape 2 : Se connecter à Braze {#step-2-connect-to-braze}

Après l'installation, sélectionnez **Connect to Braze** pour connecter votre compte Braze, puis sélectionnez **Continue**.

Ensuite, sélectionnez votre espace de travail Braze dans le menu déroulant **Braze workspace** ou saisissez le nom de l'espace de travail.

### Étape 3 : Sélectionner vos ressources Figma {#step-3-select-your-figma-assets}

Sélectionnez les images et les ressources visuelles à exporter vers Braze. Pour sélectionner plusieurs ressources, vous pouvez appuyer sur <kbd>Shift</kbd> ou faire glisser votre curseur sur les ressources.

Le nom de l'image ou de la ressource visuelle exportée correspond au nom du cadre sélectionné dans Figma.

### Étape 4 : Exporter vers Braze {#step-4-export-to-braze}

Sélectionnez **Export to Braze**. Vos images et ressources visuelles sont importées dans la bibliothèque multimédia de Braze. Toutes les images importées via cette intégration ont leur source définie sur **Figma**.