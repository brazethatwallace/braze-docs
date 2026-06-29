---
nav_title: Segment pour Currents
article_title: Segment pour Currents
page_order: 2
alias: /partners/segment_for_currents/
description: "Cet article de référence décrit le partenariat entre Braze Currents et Segment, une plateforme de données clients qui collecte et achemine des informations entre les sources de votre stack marketing."
page_type: partner
tool: Currents
search_tag: Partner

---

# Segment pour Currents {#segment-for-currents}

> [Segment](https://segment.com) est une plateforme de données clients qui vous aide à collecter, nettoyer et activer vos données clients. Cet article de référence donne un aperçu de la connexion entre Braze Currents et Segment et décrit les exigences et les processus pour une mise en œuvre et une utilisation appropriées.

L'intégration de Braze et de Segment vous permet de tirer parti de Braze Currents pour exporter vos événements Braze vers Segment afin d'approfondir les analyses sur les conversions, la rétention et l'utilisation des produits.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Segment | Un [compte Segment](https://app.segment.com/login) est nécessaire pour bénéficier de ce partenariat. |
| Destination Braze | Vous devez déjà avoir [configuré Braze comme destination]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) dans votre intégration Segment.<br><br>Cela inclut la fourniture du centre de données Braze et de la clé REST API appropriés dans vos [paramètres de connexion]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings). |
| Currents | Pour réexporter les données vers Segment, [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) doit être configuré pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Intégration {#integration}

### Étape 1 : Obtenir la clé d'écriture Segment {#step-1-obtain-segment-write-key}

Dans votre tableau de bord Segment, sélectionnez votre source Segment. Ensuite, accédez à **Settings > API keys**. Vous trouverez ici la **Segment Write Key**.

{% alert warning %}
Il est important de maintenir à jour votre clé d'écriture Segment. Si les informations d'identification de votre connecteur expirent, le connecteur cessera d'envoyer des événements. Si cette situation persiste pendant plus de **5 jours**, les événements du connecteur seront abandonnés et les données seront définitivement perdues.
{% endalert %}

### Étape 2 : Créer un nouveau connecteur Currents {#step-2-create-a-new-currents-connector}

1. Dans Braze, accédez à **Partner Integrations** > **Data Export**.
2. Cliquez sur **+ Create New Current** > **Segment Data Export**.
3. Indiquez ensuite le nom de l'intégration, l'e-mail de contact, la clé d'écriture Segment et la région Segment.

![La page Segment Currents dans Braze. Cette page contient des champs permettant de spécifier le nom de l'intégration, l'e-mail de contact, la région Segment et la clé API.]({% image_buster /assets/img/segment/segment_currents_integration_config.png %})

### Étape 3 : Exporter les événements d'engagement des messages {#step-3-export-message-engagement-events}

Sélectionnez ensuite les événements d'engagement des messages que vous souhaitez exporter. Consultez le tableau des événements et propriétés d'exportation ci-dessous. Tous les événements envoyés à Segment incluront le `external_user_id` de l'utilisateur en tant que `userId` et le `braze_id` de l'utilisateur en tant que `anonymousId`.

N'oubliez pas que Braze n'envoie les données d'événements que pour les utilisateurs sans `external_user_id` si l'option **Include events from anonymous users** est cochée.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Anonymous user export' %}

![Liste de tous les événements d'engagement de messages disponibles sur la page Segment Currents de Braze.]({% image_buster /assets/img/segment/segment_currents_data_config.png %})

Enfin, sélectionnez **Launch Current**.

{% multi_lang_include alerts/warning_alerts.md alert='Segment Currents multiple connectors' %}

Pour en savoir plus, consultez la [documentation](https://segment.com/docs/connections/sources/catalog/cloud-apps/braze/) de Segment.

## Mettre à jour votre Current {#updating-your-current}

{% multi_lang_include currents/updating_currents.md %}

## Événements Currents pris en charge {#supported-currents-events}

Braze prend en charge l'exportation des événements suivants vers Segment :

- [Événements d'engagement des messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)
- [Événements de comportement client]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)

Pour connaître la structure du payload de chaque événement, sélectionnez l'onglet **Segment** dans le [glossaire des événements d'engagement des messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) et le [glossaire des événements de comportement client]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/).