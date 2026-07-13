---
nav_title: Nift
article_title: Nift
description: "Cet article de référence présente le partenariat entre Braze et Nift, une plateforme bilatérale qui aide les entreprises à acquérir, engager et fidéliser leurs clients."
alias: /partners/nift/
page_type: partner
search_tag: Partner

---

# Nift

> [Nift](https://gonift.com/) aide les entreprises à acquérir, engager et fidéliser leurs clients. La plateforme bilatérale aide les partenaires à remercier leurs clients avec des cartes-cadeaux Nift. Remercier les clients augmente leur valeur vie client et génère un chiffre d'affaires supplémentaire.

_Cette intégration est maintenue par Nift._

## À propos de l'intégration {#about-the-integration}

L'intégration entre Braze et Nift vous permet de déclencher automatiquement des « remerciements » contenant des cadeaux Nift à des moments clés du cycle de vie du client et d'identifier les clients qui ont utilisé leur cadeau. Les cartes-cadeaux Nift peuvent être utilisées pour accéder à des produits et services fournis par des marques qui s'appuient sur la technologie de mise en relation de Nift pour acquérir de nouveaux clients de manière rentable à grande échelle.

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte Nift | Un compte Nift est nécessaire pour profiter de ce partenariat. |
| Clé API REST de Braze | Une clé API REST de Braze avec toutes les autorisations relatives aux données utilisateur. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | L'URL de votre endpoint REST. Votre endpoint dépendra de l'URL de Braze pour [votre instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Se connecter à Braze dans Nift {#step-1-connect-to-braze-in-nift}

Rendez-vous sur votre [tableau de bord Nift](https://www.gonift.com/users/sign_in), naviguez vers **Accounts** > **Integrations** > **Braze**, puis cliquez sur **Connect**.

### Étape 2 : Ajouter les informations d'identification de Braze {#step-2-add-braze-credentials}

Sur la page **Link your Braze Account**, indiquez votre clé API REST de Braze et sélectionnez votre endpoint Braze, qui dépendra de l'URL de Braze pour [votre instance]({{site.baseurl}}/api/basics/#endpoints).

Vous pouvez modifier le nom du paramètre d'ID client dans le lien de recommandation envoyé à vos clients. Nift l'utilisera pour marquer vos clients comme traités dans Braze lorsqu'ils auront choisi un cadeau de l'une de nos marques.

Cliquez sur **Link Account**.

!["Page d'intégration du service Nift demandant à l'utilisateur la clé API de Braze et l'URL du tableau de bord de Braze.]({% image_buster /assets/img/nift/link_your_braze_account.png %})

## Utiliser l'intégration {#using-the-integration}

Pour utiliser l'intégration, distribuez le lien de recommandation dans vos messages. Lorsque votre client utilise le lien de recommandation et sélectionne un cadeau de l'une de nos marques, Nift le marque comme traité dans Braze.

Après l'intégration avec Braze, Nift transmettra automatiquement les événements vers l'enregistrement Braze du client existant avec les données suivantes :

- Nom de l'événement : `nift_processed`
- Heure : le moment où le client a choisi/utilisé le cadeau