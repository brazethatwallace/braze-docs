---
nav_title: Hightouch
article_title: Hightouch
description: "Cet article de référence présente le partenariat entre Braze et Hightouch, une plateforme permettant de synchroniser les données de vos clients depuis votre entrepôt vers les outils commerciaux."
page_type: partner
search_tag: Partner

---

# Hightouch

> [Hightouch](https://hightouch.io) est une plateforme d'intégration de données moderne qui vous permet de synchroniser les données clients, produits ou propriétaires de votre entrepôt ou lac de données avec n'importe quelle application de votre choix, le tout sans l'aide de vos équipes informatiques ou d'ingénierie.

L'intégration de Braze et Hightouch vous permet de créer de meilleures campagnes sur Braze avec des données clients actualisées provenant de votre entrepôt de données. En synchronisant automatiquement les données clients dans Braze, vous n'avez plus à vous soucier de la cohérence des données et pouvez vous concentrer sur la création d'expériences clients exceptionnelles.

Cette intégration vous permet également d'[importer des cohortes d'utilisateurs dans Braze]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/hightouch_cohort_import/), en envoyant des campagnes ciblées basées sur des données qui peuvent n'exister que dans votre entrepôt.

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte Hightouch | Un compte Hightouch est nécessaire pour profiter de ce partenariat.
| Clé API REST de Braze | Une clé API REST de Braze avec les autorisations `users.track` et `users.export.ids`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Endpoint REST de Braze  | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).<br><br>Hightouch nécessite le nom du cluster sur lequel se trouve votre instance Braze. Par exemple, si votre endpoint Braze est `https://rest.iad-01.braze.com`, vous n'avez besoin que de `iad-01`.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Cas d'utilisation {#use-cases}

* Synchronisez les données sur les utilisateurs et les comptes dans Braze pour créer des campagnes hyperpersonnalisées.
* Mettez automatiquement à jour vos segments Braze avec des données fraîches provenant de votre entrepôt.
* Proposez de meilleures expériences en intégrant à Braze des données provenant d'autres points de contact avec les clients.
* Importez des cohortes d'utilisateurs dans Braze, ce qui vous permet d'envoyer des campagnes ciblées et des Canvas.

## Intégration {#integration}

### Étape 1 : Créez votre destination Hightouch Braze {#step-1-create-your-hightouch-braze-destination}

1. Sur la plateforme Hightouch, dans la section **Destinations**, cliquez sur **Add destination**.
2. Sélectionnez **Braze** dans la liste des destinations disponibles.
3. Indiquez votre endpoint REST de Braze (à l'exclusion de « https://rest. ») et votre clé API REST de Braze.<br><br>![]({% image_buster /assets/img/hightouch/hightouch_braze_setup.png %})

### Étape 2 : Synchronisation des objets et des événements {#step-2-object-and-event-syncing}

Hightouch prend en charge la synchronisation à la fois des objets utilisateurs et des événements.

| Destination | Description | Modes pris en charge |
|---|---|---|
| Objet | Synchronise les enregistrements avec des objets tels que des utilisateurs ou des organisations dans votre destination. | Upsert ou mise à jour |
| Événements | Synchronise les enregistrements en tant qu'événements vers votre destination, souvent sous la forme d'un appel de suivi. | Suivi des événements ou des achats |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Step 2: Object and event syncing" }

{% alert note %}
Reportez-vous à la [documentation Hightouch](https://hightouch.com/docs/destinations/braze#syncing-and-data-point-consumption) pour plus d'informations sur la manière dont les synchronisations affectent la consommation de points de données.
{% endalert %}

#### Synchronisation des objets Braze {#syncing-braze-objects}

Vous pouvez synchroniser les objets Hightouch (champs utilisateur) avec les champs par défaut ou personnalisés équivalents de Braze. Vous pouvez également effectuer des rapprochements d'enregistrements pour unifier les données entre les deux plateformes.

#### Synchronisation des événements Braze {#syncing-braze-events}

Hightouch vous permet de suivre les données relatives aux événements et aux achats et de les synchroniser avec Braze. Plusieurs options peuvent être définies dans Hightouch pour ajuster le comportement de synchronisation, telles que la configuration des données de suivi et la définition du comportement pour les utilisateurs inexistants.

{% alert important %}
Vous trouverez de plus amples instructions sur la synchronisation des objets et des événements dans la [documentation Hightouch](https://hightouch.io/docs/destinations/braze/).
{% endalert %}



## Démonstration de l'intégration {#integration-demo}

<div class="video-container">
    <iframe width="560" height="315" src="https://drive.google.com/file/d/1KQdCwZzV88hXMx7AMWgh8izqkldtNv5p/preview" title="Hightouch integration demo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>