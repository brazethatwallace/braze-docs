---
nav_title: Eppo
article_title: Eppo
description: "Découvrez comment intégrer Eppo à Braze."
alias: /partners/eppo/
page_type: partner
search_tag: Partner
---

# Eppo

> [Eppo](https://www.geteppo.com/) est une plateforme d'expérimentation de nouvelle génération qui permet aux équipes d'effectuer des tests A/B, de gérer les fonctionnalités à grande échelle et d'exploiter les informations basées sur l'intelligence artificielle pour prendre des décisions fondées sur les données.

*Cette intégration est maintenue par Eppo.*

L'intégration de Braze et d'Eppo vous permet de mettre en place des tests A/B dans Braze et d'analyser les résultats dans Eppo pour découvrir des informations et lier la performance des messages à des indicateurs commerciaux à long terme tels que le chiffre d'affaires ou la fidélisation.

## Prérequis {#prerequisites}

| Condition requise                        | Description                                                                         |
|------------------------------------|-------------------------------------------------------------------------------------|
| Compte Eppo                       | Un compte Eppo est nécessaire pour bénéficier de ce partenariat.                   |
| Currents ou Snowflake Data Sharing | Currents ou Snowflake Data Sharing est nécessaire pour qu'Eppo puisse analyser les données d'expérimentation. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration {#integration}

### Étape 1 : Configurer Currents ou le partage de données Snowflake dans Braze {#step-1-configure-currents-or-snowflake-data-sharing-in-braze}

Eppo analyse les expériences directement dans votre entrepôt de données. Pour activer l'intégration, les données d'engagement des messages Braze doivent être disponibles dans l'entrepôt connecté à Eppo. Vous pouvez exporter les données de Campaign depuis Braze à l'aide de Currents, ou accéder aux données Braze dans votre instance Snowflake via le [partage de données Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake).

### Étape 2 : Configurer votre expérience dans une Campaign ou un Canvas Braze {#step-2-set-up-your-experiment-in-a-braze-campaign-or-canvas}

Vous pouvez utiliser les fonctionnalités natives de test A/B dans vos Campaigns et Canvas. Pour en savoir plus, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

### Étape 3 : Configurer Eppo pour mesurer les expériences Braze {#step-3-set-up-eppo-to-measure-braze-experiments}

Pour exécuter des expériences à l'aide des données Braze dans Eppo, créez des [tables d'assignation](https://docs.geteppo.com/data-management/definitions/assignment-sql/) dans votre entrepôt de données en vous basant sur les données d'événements de messages au niveau utilisateur exportées depuis Braze. Il est recommandé de créer des tables séparées pour les expériences Canvas et les expériences Campaign, car elles reposent sur des métadonnées différentes.

{% tabs local %}
{% tab expériences Canvas %}
Pour les expériences Canvas, les assignations peuvent être créées soit :

- Au niveau de l'entrée du Canvas (`users.canvas.Entry`)
- Soit dans une étape d'expérience Canvas (`users.canvas.experimentstep.SplitEntry`)

Dans ces cas, des champs tels que `canvas_name`, `experiment_step_id`, `canvas_variation_name` et `experiment_split_id` sont utilisés pour définir le nom de l'expérience et la variante.

{% endtab %}

{% tab expériences Campaign %}
Pour les expériences Campaign, utilisez les événements d'envoi (tels que notification push, e-mail, SMS) pour déterminer quand un utilisateur est entré dans l'expérience. `campaign_name`, `message_variation_name` et `time` sont utilisés pour remplir la table d'assignation.

{% endtab %}
{% endtabs %}

Pour suivre les indicateurs spécifiques aux messages (comme les clics ou les ouvertures), incluez une **entité secondaire** en créant un `combined_id` qui associe l'identifiant utilisateur au nom de la Campaign ou du Canvas. Ce `combined_id` est également utilisé dans vos tables de faits pour aligner les indicateurs avec l'expérience et la variante appropriées.

Eppo utilise ces tables d'assignation et de faits pour analyser les résultats. Il est recommandé de configurer un **protocole** dans Eppo afin de standardiser la mise en place des futures expériences. Pour plus d'informations, consultez la [documentation d'Eppo](https://docs.geteppo.com/guides/marketing/integrating-with-braze/).

## Assistance {#support}

Pour toute question concernant la configuration de Braze Currents, le partage de données Snowflake ou la configuration de campagnes multivariées, contactez votre gestionnaire du succès des clients Braze.

Pour obtenir de l'aide concernant la configuration d'Eppo pour mesurer les expériences Braze, contactez l'équipe d'assistance Eppo.