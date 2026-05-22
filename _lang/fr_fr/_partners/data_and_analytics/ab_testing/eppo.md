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

## Conditions préalables {#prerequisites}

| Condition | Description |
|------------------------------------|-------------------------------------------------------------------------------------|
| Compte Eppo | Un compte Eppo est nécessaire pour bénéficier de ce partenariat. |
| Currents ou partage de données Snowflake | Currents ou le partage de données Snowflake est nécessaire pour qu'Eppo puisse analyser les données des expériences. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Configurer Currents ou le partage de données Snowflake dans Braze {#step-1-configure-currents-or-snowflake-data-sharing-in-braze}

Eppo analyse les expériences directement dans votre entrepôt de données. Pour activer l'intégration, les données d'engagement des messages de Braze doivent être disponibles dans l'entrepôt connecté à Eppo. Vous pouvez exporter les données de campagne depuis Braze à l'aide de Currents, ou accéder aux données de Braze dans votre instance Snowflake à l'aide du [partage de données Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/).

### Étape 2 : Configurer votre expérience dans une campagne ou un Canvas Braze {#step-2-set-up-your-experiment-in-a-braze-campaign-or-canvas}

Vous pouvez utiliser les fonctionnalités natives de test A/B dans vos campagnes et Canvas. Pour en savoir plus, consultez la rubrique [Test multivarié et test A/B](https://www.braze.com/docs/user_guide/engagement_tools/testing/multivariant_testing#what-are-multivariate-and-ab-testing).

### Étape 3 : Configurer Eppo pour mesurer les expériences Braze {#step-3-set-up-eppo-to-measure-braze-experiments}

Pour réaliser des expériences à l'aide des données de Braze dans Eppo, créez dans votre entrepôt des [tables d'affectations](https://docs.geteppo.com/data-management/definitions/assignment-sql/) basées sur les données d'événements de messages au niveau de l'utilisateur exportées depuis Braze. Il est recommandé d'utiliser des tables distinctes pour les expériences Canvas et les expériences de campagne, car elles reposent sur des métadonnées différentes.

{% tabs local %}
{% tab canvas experiments %}
Pour les expériences Canvas, les affectations peuvent être créées soit :

- Au niveau de l'entrée dans le Canvas (`users.canvas.Entry`)
- Soit dans une étape d'expérience Canvas (`users.canvas.experimentstep.SplitEntry`)

Dans ces cas, des champs tels que `canvas_name`, `experiment_step_id`, `canvas_variation_name` et `experiment_split_id` sont utilisés pour définir le nom et la variante de l'expérience.

{% endtab %}

{% tab campaign experiments %}
Pour les expériences de campagne, utilisez des événements d'envoi (tels que push, e-mail, SMS) pour déterminer quand un utilisateur est entré dans l'expérience. `campaign_name`, `message_variation_name` et `time` sont utilisés pour remplir la table d'affectation.

{% endtab %}
{% endtabs %}

Pour suivre les indicateurs spécifiques aux messages (comme les clics ou les ouvertures), incluez une **entité secondaire** en créant un `combined_id` qui associe l'ID utilisateur au nom de la campagne ou du Canvas. Ce `combined_id` est également utilisé dans vos tables de faits pour aligner les indicateurs sur l'expérience et la variante correctes.

Eppo utilise ces affectations et ces tables de faits pour analyser les résultats. Il est recommandé de mettre en place un **protocole** dans Eppo afin de standardiser la configuration des expériences futures. Pour plus d'informations, reportez-vous à la [documentation d'Eppo](https://docs.geteppo.com/guides/marketing/integrating-with-braze/).

## Assistance {#support}

Pour toute question concernant la configuration de Braze Currents, le partage de données Snowflake ou la mise en place de campagnes multivariées, contactez votre gestionnaire de la satisfaction client Braze.

Pour obtenir de l'aide sur la configuration d'Eppo afin de mesurer les expériences Braze, contactez l'équipe d'assistance d'Eppo.