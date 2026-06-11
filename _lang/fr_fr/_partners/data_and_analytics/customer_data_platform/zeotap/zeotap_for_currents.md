---
nav_title: Zeotap pour Currents
article_title: Zeotap pour Currents
description: "Cet article de référence présente le partenariat entre Braze Currents et Zeotap, une plateforme de données client de nouvelle génération qui vous aide à découvrir et à comprendre votre audience mobile en fournissant une résolution d'identité, des informations et un enrichissement des données."
page_type: partner
tool: Currents
search_tag: Partner
---

# Zeotap pour Currents {#zeotap-for-currents}

> [Zeotap](https://zeotap.com/) est une plateforme de données client de nouvelle génération qui vous aide à découvrir et à comprendre votre audience mobile grâce à des outils de résolution d'identité, des informations exploitables et un enrichissement des données.

L'intégration entre Braze et Zeotap vous permet d'étendre l'échelle et la portée de vos campagnes en synchronisant les segments de clients Zeotap avec les profils utilisateur de Braze. Avec [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/), vous pouvez également connecter les données à Zeotap pour les rendre exploitables dans l'ensemble des outils de croissance.

## Conditions préalables {#prerequisites}

| Condition | Description |
| --- | --- |
| Compte Zeotap | Un [compte Zeotap](https://zeotap.com/) est nécessaire pour bénéficier de ce partenariat. |
| Currents | Pour exporter des données vers Zeotap, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Mise en œuvre {#implementation}

### Étape 1 : Créer une source Currents {#step-1-create-a-currents-source}

1. Dans Zeotap, accédez à **Sources** sous **Integrate**.
2. Sélectionnez **Create Source**.
3. Sélectionnez **Customer Engagement Channels** comme catégorie.<br><br>![Une fenêtre « Create Source » répertoriant différentes catégories, dont « Customer Engagement Channels ».]({% image_buster /assets/img/zeotap/cec.png %}){: style="max-width:70%;"}<br><br>
4. Sélectionnez **Braze** comme source de données.
5. Saisissez un nom de source.
6. Sélectionnez votre région.<br><br>![Fenêtre avec des options pour sélectionner votre région et l'entité de données.]({% image_buster /assets/img/zeotap/select_region.png %}){: style="max-width:70%;"}<br><br>
7. Sélectionnez **Create Source**.
8. Accédez à l'onglet **Implementation Details** et notez l'**API URL** et la **Write Key**.<br><br>![Détails de mise en œuvre pour Braze Currents contenant l'URL de l'API et la clé d'écriture.]({% image_buster /assets/img/zeotap/implementation_details.png %})

### Étape 2 : Configurer le flux de données dans Currents {#step-2-configure-data-streaming-in-currents}

1. Dans Braze, accédez à **Intégrations partenaires** > **Exportation de données**.
2. Sélectionnez **Create New Current** puis **Custom Currents Export**.<br><br>![Le bouton « Create New Current » avec un menu déroulant contenant « Custom Currents Export ».]({% image_buster /assets/img/zeotap/custom_currents_export.png %}){: style="max-width:60%;"}<br><br>
3. Saisissez un nom d'intégration et une adresse e-mail pour être contacté en cas d'erreurs avec l'intégration.
4. Sous **Credentials**, entrez les informations suivantes que vous avez notées à l'[étape 1](#step-1-create-a-currents-source) :
- L'URL de l'API comme **Endpoint**
- La Write Key comme **Bearer Token**<br><br>![Sections permettant de saisir les détails de l'intégration et les identifiants.]({% image_buster /assets/img/zeotap/credentials.png %})<br><br>
5. Sélectionnez les événements d'engagement liés aux messages que vous souhaitez envoyer à Zeotap.<br><br>![L'onglet « General Settings » avec une section permettant de sélectionner les événements d'engagement liés aux messages.]({% image_buster /assets/img/zeotap/message_engagement_events.png %})
6. Sélectionnez **Launch Current** pour enregistrer les modifications et commencer à envoyer des événements à Zeotap.

{% alert important %}
Le connecteur Currents ne prend pas en charge les utilisateurs anonymes (utilisateurs sans `external_id`).
{% endalert %}