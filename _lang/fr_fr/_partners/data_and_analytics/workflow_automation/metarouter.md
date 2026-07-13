---
nav_title: MetaRouter
article_title: MetaRouter
description: "Améliorez la gestion des données de vos clients dans Braze grâce à MetaRouter. Cette solution performante de gestion des balises côté serveur offre une conformité et un contrôle optimaux grâce à des options de déploiement fluides, que ce soit sur un cloud privé hébergé par MetaRouter ou sur votre propre infrastructure."
alias: /partners/metarouter/
page_type: partner
search_tag: Partner
---

# MetaRouter

> [MetaRouter](https://www.metarouter.io/) améliore votre expérience Braze en s'intégrant de façon fluide en tant que puissante plateforme de gestion des balises côté serveur. Il vous permet d'orchestrer un parcours complet de données clients au sein de Braze, depuis la collecte fiable de données first-party enrichies jusqu'à 30 %, jusqu'à l'activation du flux d'événements en temps réel pour des parcours personnalisés. De plus, MetaRouter simplifie la mise en œuvre en éliminant le besoin de balises Braze ou d'autres balises tierces, ce qui vous permet de contrôler de manière granulaire, paramètre par paramètre, les données circulant dans Braze.

_Cette intégration est maintenue par Metarouter._

## Fonctionnalités prises en charge {#supported-features}

- Les nouvelles tentatives peuvent être intégrées.
- Les requêtes sont groupées.
- Les problèmes de limite de débit sont gérés par une nouvelle tentative.
- L'ID externe et les données personnelles sont pris en charge. MetaRouter transmet son identifiant anonyme et toutes les informations personnelles (e-mail, numéro de téléphone, nom) souhaitées par les clients.
- Vous pouvez envoyer des données d'achats et d'événements personnalisés à Braze.
  - Les propriétés d'événement sont prises en charge.
  - Les propriétés de l'événement imbriqué ne sont pas prises en charge.

## Conditions préalables {#prerequisites}

Avant de commencer, vous aurez besoin des éléments suivants :

| Exigence | Description |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Un compte MetaRouter | Un compte [MetaRouter Enterprise](https://enterprise.metarouter.io/). |
| Clé API REST Braze | Une clé API REST Braze avec les autorisations `users.track`. Pour en créer une, accédez à **Settings** > **API Keys**. |
| Un endpoint REST Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Configuration de MetaRouter {#setting-up-metarouter}

Pour configurer MetaRouter pour votre intégration à Braze :

1. Accédez à MetaRouter et créez un nouveau cluster.
2. Choisissez les événements que vous souhaitez suivre.
3. Installez un SDK MetaRouter et intégrez des événements à votre site web.
4. Connectez votre cluster à l'interface utilisateur de votre site web.
5. Créez un nouveau pipeline.
6. Vérifiez que votre site web envoie des événements à MetaRouter.

## Intégrer Braze {#integrating-braze}

### Étape 1 : Ajouter l'intégration Braze {#step-1-add-the-braze-integration}

Dans Enterprise MetaRouter, sélectionnez **Integrations** > **New Integration** > **Braze**, puis donnez un nom à votre intégration. Entrez ensuite l'URL de votre instance et votre clé API, puis sélectionnez **Apply Changes**.

![Ajout de Braze comme intégration dans MetaRouter.]({% image_buster /assets/img/metarouter/img1.png %}){: style="max-width:50%;"}

### Étape 2 : Ajouter un mappage d'événements {#step-2-add-event-mapping}

Ajoutez un mappage d'événements pour chaque sortie d'identité, puis configurez les événements que vous souhaitez envoyer à Braze. Lorsque vous avez terminé, sélectionnez **Save as New Revision**.

![Ajout d'un mappage d'événements pour chacune des sorties d'identité.]({% image_buster /assets/img/metarouter/img2.png %})