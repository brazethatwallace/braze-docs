---
nav_title: Tealium pour Currents
article_title: Tealium pour Currents
page_order: 3
alias: /partners/tealium_for_currents/
description: "Cet article de référence présente le partenariat entre Braze Currents et Tealium, une plateforme de données client qui collecte et achemine les informations entre les sources de votre pile marketing."
page_type: partner
tool: Currents
search_tag: Partner

---

# Tealium pour Currents {#tealium-for-currents}

> [Tealium](https://www.tealium.com) est une plateforme de données client qui collecte et achemine des informations provenant de sources multiples vers divers autres emplacements de votre pile marketing.

L'intégration de Braze et Tealium vous permet de contrôler de façon fluide le flux d'informations entre les deux systèmes. Avec Currents, vous pouvez également connecter des données à Tealium afin de les exploiter dans l'ensemble des outils de croissance.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Tealium EventStream ou Tealium AudienceStream | Un [compte Tealium](https://my.tealiumiq.com/) est nécessaire pour bénéficier de ce partenariat. |
| Currents | Pour pouvoir exporter des données vers Tealium, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
| URL Tealium | Vous pouvez l'obtenir en vous rendant sur votre tableau de bord Tealium et en copiant l'URL d'ingestion.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Créer une source de données pour Braze dans Tealium {#step-1-create-a-data-source-for-braze-within-tealium}

Les instructions pour créer une source de données sont disponibles sur le site de [Tealium](https://docs.tealium.com/server-side/data-sources/webhooks/braze-currents/). Une fois l'opération terminée, Tealium vous fournira une URL de source de données à copier, que vous utiliserez à l'étape suivante.

### Étape 2 : Créer un Current {#step-2-create-current}

Dans Braze, accédez à **Currents** > **+ Create Current** > **Exportation Tealium**. Indiquez un nom d'intégration, un e-mail de contact et votre URL Tealium.

Sélectionnez ensuite les événements que vous souhaitez suivre dans la liste des événements disponibles. Par défaut, tous les événements envoyés à Tealium incluent l'`external_user_id` de l'utilisateur. Cependant, vous pouvez cocher la case **Include events from anonymous users** pour envoyer également à Tealium les événements qui n'ont pas d'`external_user_id`.

Après avoir configuré votre intégration, sélectionnez **Launch Current**.

{% alert important %}
Il est important de maintenir votre URL Tealium à jour. Si l'URL de votre connecteur est incorrecte, Braze ne pourra pas envoyer d'événements. Si cette situation persiste pendant plus de **5 jours**, les événements du connecteur seront abandonnés et les données seront définitivement perdues.
{% endalert %}

## Détails de l'intégration {#integration-details}

Braze prend en charge l'exportation vers Tealium de toutes les données répertoriées dans les [glossaires d'événements de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) (y compris toutes les propriétés des événements d'[engagement par message]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) et de [comportement des clients]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)).

La structure des payloads exportés est la même que celle des connecteurs HTTP personnalisés, consultable dans le [dépôt d'exemples de connecteurs HTTP personnalisés](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).