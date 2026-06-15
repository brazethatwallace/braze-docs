---
nav_title: RudderStack pour Currents
article_title: RudderStack pour Currents
description: "Cet article présente le partenariat entre Braze Currents et RudderStack, une infrastructure de données client open-source qui offre une intégration fluide de Braze pour vos applications Android, iOS et web."
page_type: partner
tool: Currents
search_tag: Partner

---

# RudderStack pour Currents {#rudderstack-for-currents}

> [RudderStack](https://www.rudderstack.com/) vous permet de collecter, de transformer et d'activer les données de vos clients dans l'ensemble de votre pile, en exploitant votre entrepôt de données dans le cloud comme source centrale de vérité. Cet article donne un aperçu de la configuration d'une connexion entre Braze Currents et RudderStack.

L'intégration Braze et RudderStack vous permet de tirer parti de Braze Currents pour exporter vos événements Braze vers RudderStack afin de réaliser des analyses plus approfondies.

## Conditions préalables {#prerequisites}

| Condition | Description |
| --- | --- |
| Compte RudderStack | Un [compte RudderStack](https://app.rudderstack.com/login) est nécessaire pour bénéficier de ce partenariat. |
| Destination Braze | Nous vous suggérons d'avoir [configuré Braze comme destination]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/rudderstack/rudderstack/#integration) dans RudderStack. |
| Currents | Pour exporter des données vers RudderStack, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Créer une source de données pour Braze dans RudderStack {#step-1-create-a-data-source-for-braze-within-rudderstack}

Tout d'abord, vous devez créer une source Braze dans l'application web RudderStack. Les instructions relatives à la création d'une source de données sont disponibles sur le site de [RudderStack](https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/braze-currents/).

Une fois l'opération terminée, RudderStack fournira une URL de webhook, y compris la clé d'écriture, que vous devrez utiliser à l'étape suivante. Vous trouverez l'URL du webhook dans l'onglet **Settings** de votre source Braze.

### Étape 2 : Créer un flux Current {#step-2-create-current}

Dans Braze, naviguez vers **Currents > + Create Current > RudderStack Export**. Indiquez le nom de l'intégration, l'e-mail du contact, l'URL du webhook de RudderStack (qui va dans le champ de la clé) et la région de RudderStack.

### Étape 3 : Exporter des événements {#step-3-export-events}

Sélectionnez ensuite les événements que vous souhaitez exporter. Enfin, cliquez sur **Launch Current**.

Tous les événements envoyés à RudderStack comprendront l'`external_user_id` de l'utilisateur. À l'heure actuelle, Braze n'envoie pas de données d'événement à RudderStack pour les utilisateurs dont l'`external_user_id` n'est pas configuré.

## Détails de l'intégration {#integration-details}

Braze permet d'exporter vers RudderStack toutes les données figurant dans les [glossaires des événements de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/).

La structure du payload des données exportées est la même que celle des connecteurs HTTP personnalisés, qui peut être consultée dans le [référentiel d'exemples de connecteurs HTTP personnalisés](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).