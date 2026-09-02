---
nav_title: Évaluation des prospects
article_title: Créer un workflow d'évaluation des prospects
page_order: 1
page_type: reference
description: "Découvrez comment utiliser Braze pour réaliser une évaluation simple des prospects, une évaluation externe des prospects et des transferts de prospects."
---

# Créer un workflow d'évaluation des prospects {#create-a-lead-scoring-workflow}

> Ce cas d'usage montre comment utiliser Braze pour mettre à jour les scores des prospects en temps réel et transmettre automatiquement les prospects qualifiés à vos équipes commerciales.

La création d'un workflow d'évaluation des prospects dans Braze repose sur deux étapes clés :

1. Créer un Canvas d'évaluation des prospects dans Braze ou intégrer un outil externe d'évaluation des prospects :
- [Évaluation simple des prospects](#simple-lead-scoring)
- [Évaluation externe des prospects](#external-lead-scoring)

2. Créer une Campaign webhook pour envoyer les prospects qualifiés à votre équipe commerciale :
- [Transfert de prospects : Marketing Qualified Lead (MQL) vers les ventes](#lead-handoff)

## Évaluation simple des prospects {#simple-lead-scoring}

### Étape 1 : Créer un Canvas {#step-1-create-a-canvas}

1. Accédez à **Messaging** > **Canvas** et sélectionnez **Create Canvas**, puis renseignez les informations de base de votre Canvas.

2. Donnez à votre Canvas un nom pertinent, tel que « Canvas d'évaluation des prospects » et, pour le retrouver facilement, attribuez-lui une étiquette comme « Gestion des prospects ».<br><br>![Étape 1 de la création d'un Canvas avec le nom « Canvas d'évaluation des prospects » et l'étiquette « Gestion des prospects ».]({% image_buster /assets/img/b2b/step_1_simple.png %}){: style="max-width:80%;"}

### Étape 2 : Définir vos critères d'entrée {#step-2-set-up-your-entry-criteria}

1. Passez à l'étape **Entry Schedule** et sélectionnez une planification d'entrée **Action-Based**. Les utilisateurs entreront ainsi dans le Canvas lorsqu'ils effectueront des actions spécifiques.

2. Dans **Action-Based Options**, ajoutez ces deux actions :
    - **Change Custom Attribute Value** avec le nom de votre attribut d'évaluation des prospects (par exemple `lead score`). Si vous n'avez pas encore créé d'attribut d'évaluation des prospects, suivez les étapes décrites dans [Attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes). Les utilisateurs entreront ainsi dans le Canvas chaque fois que leur score de prospect change.
    - **Add an Email Address**

![Étape 2 de la création d'un Canvas avec la planification d'entrée « Action-Based » et les options basées sur l'action de modification d'un attribut personnalisé « lead score » et d'ajout d'une adresse e-mail.]({% image_buster /assets/img/b2b/step_2_simple.png %}){: style="max-width:80%;"}

### Étape 3 : Identifier votre audience cible {#step-3-identify-your-target-audience}

#### Étape 3a : Sélectionner des segments {#step-3a-select-segments}

Tous les utilisateurs sont éligibles à l'évaluation des prospects. Vous pouvez donc ajouter des règles spécifiques à votre entreprise pour déterminer qui évaluer en sélectionnant les [segments]({{site.baseurl}}/user_guide/audience/segments) d'utilisateurs à cibler et en appliquant des [filtres]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) supplémentaires. Par exemple, vous pouvez exclure les employé or salariés, les utilisateurs déjà clients, etc.

![Étape 3 de la création d'un Canvas avec des options de sélection de segments et de filtres pour affiner l'audience d'entrée.]({% image_buster /assets/img/b2b/step_3_simple.png %}){: style="max-width:80%;"}

#### Étape 3b : Configurer la rééligibilité du Canvas {#step-3b-set-canvas-re-eligibility}

Un utilisateur passera par ce Canvas de nombreuses fois au cours de son cycle de vie. Assurez-vous donc qu'il puisse y entrer à nouveau aussi rapidement qu'il en est sorti la fois précédente, grâce aux paramètres de rééligibilité.

Dans **Entry Controls**, procédez comme suit :
- Sélectionnez **Allow users to re-enter this Canvas**.
- Sélectionnez **Specified Window**.
- Définissez la rééligibilité sur « 0 » **secondes**.

![Section « Entry Controls » avec les options « Allow users to re-enter this Canvas » dans une « Specified Window » de 0 seconde.]({% image_buster /assets/img/b2b/entry_controls_simple.png %}){: style="max-width:80%;"}

#### Étape 3c : Mettre à jour les paramètres d'envoi {#step-3c-update-send-settings}

Étant donné la nature opérationnelle de ce Canvas et le fait qu'aucun message ne sera envoyé à ces utilisateurs, vous n'avez pas besoin de respecter les statuts d'abonnement.

Sous **Subscription Settings**, pour **Send to these users:** sélectionnez **all users including unsubscribed users**.

![Étape 4 de la création d'un Canvas pour la définition des options d'envoi des messages.]({% image_buster /assets/img/b2b/step_4_simple.png %}){: style="max-width:80%;"}

### Étape 4 : Construire votre Canvas {#step-4-build-your-canvas}

#### Étape 4a : Ajouter un parcours d'action {#step-4a-add-an-action-path}

Sous votre variante, sélectionnez <i class="fas fa-plus" aria-label="Ajouter"></i> **Ajouter**, puis sélectionnez **Action Paths**.

![Canvas avec « Action Paths » affiché dans le menu ouvert par l'icône plus.]({% image_buster /assets/img/b2b/action_paths_simple.png %}){: style="max-width:60%;"}

#### Étape 4b : Créer des groupes d'action {#step-4b-create-action-groups}

Chaque groupe d'action représente l'ensemble des actions qui conduisent à la même incrémentation ou décrémentation de points. Vous pouvez définir jusqu'à huit groupes d'action. Dans ce scénario, nous allons en créer quatre.

Ajoutez les groupes suivants à votre parcours d'action :

- **Groupe 1 :** Tous les événements comptant pour une incrémentation de 1 point.
- **Groupe 2 :** Tous les événements comptant pour une incrémentation de 5 points.
- **Groupe 3 :** Tous les événements comptant pour une décrémentation de 1 point.
- **Everyone Else :** Les parcours d'action vous permettent de définir une fenêtre d'attente pour voir si un utilisateur effectue une action, avant de le placer dans un groupe « Everyone Else ». Pour l'évaluation des prospects, c'est l'occasion de diminuer le score pour cause d'« inactivité ».

![Parcours d'action contenant des groupes d'action pour ajouter un point, cinq points et dix points ; soustraire un point et dix points ; et « Everyone Else ».]({% image_buster /assets/img/b2b/action_paths_selected_simple.png %}){: style="max-width:20%;"}

#### Étape 4c : Configurer chaque groupe pour inclure les événements pertinents {#step-4c-configure-each-group-to-include-the-relevant-events}

Dans chaque groupe d'action, sélectionnez **Select trigger** et choisissez l'événement qui ajoutera le nombre de points correspondant à ce groupe d'action. Ajoutez d'autres déclencheurs pour inclure tous les événements qui incrémenteront le score du prospect d'un point. Par exemple, un utilisateur pourrait incrémenter son score d'un point lorsqu'il démarre une session dans n'importe quelle application ou effectue un événement personnalisé (comme s'inscrire ou participer à un webinaire).

![Groupe d'action pour l'ajout d'un point avec les déclencheurs « Starting Session in Any App » et « Performing Custom Event ».]({% image_buster /assets/img/b2b/action_groups_simple.png %}){: style="max-width:80%;"}

#### Étape 4d : Ajouter des étapes User Update {#step-4d-add-user-update-steps}

Ajoutez une étape User Update à chaque parcours du Canvas créé sous votre parcours d'action.

![Canvas affichant le parcours d'action avec des chemins User Update ramifiés pour chaque groupe d'action.]({% image_buster /assets/img/b2b/user_update_paths_simple.png %}){: style="max-width:80%;"}

{: start="2"}
Dans l'onglet **Compose** de chaque étape User Update, procédez comme suit pour les champs correspondants :

| Champ | Action |
| --- | --- |
| **Attribute Name** | Sélectionnez l'attribut d'évaluation des prospects choisi à l'étape 2 (`lead score`). |
| **Action** | Changez l'action en **Increment By** si le parcours augmente le score ou **Decrement By** si le parcours diminue le score. |
| **Increment By** ou **Decrement By** | Saisissez le nombre de points à ajouter ou à retrancher du score du prospect. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 4d : Ajouter des étapes User Update" }

### Étape 5 : Lancer votre Canvas {#step-5-launch-your-canvas}

C'est tout ! Votre Canvas d'évaluation des prospects est prêt à être lancé.

## Évaluation externe des prospects {#external-lead-scoring}

Que vous utilisiez l'un de nos [partenaires technologiques]({{site.baseurl}}/partners/home), votre propre modèle interne d'évaluation des prospects, le machine learning ou un autre outil d'évaluation, nous avons plusieurs options à votre disposition.

### Partenaires externes {#external-partners}

Consultez la page [Partenaires technologiques]({{site.baseurl}}/partners/home) pour en savoir plus sur nos partenaires B2B proposant des fonctionnalités d'évaluation des prospects. Votre outil n'y figure pas ? Vous pouvez l'intégrer en appelant notre endpoint d'API [`users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

### Modèles de données internes pour l'évaluation des prospects {#internal-lead-scoring-data-models}

Vous pouvez intégrer Braze à vos modèles de données internes, y compris les modèles d'évaluation des prospects, de différentes manières. Voici quelques exemples courants d'intégrations réalisées par nos clients.

#### Entrepôt de données cloud intégré {#integrated-cloud-data-warehouse}

{% tabs %}
{% tab Braze comme source de données %}

En tant qu'outil marketing, Braze contient des données extrêmement pertinentes qui peuvent enrichir le modèle interne d'évaluation des prospects de votre équipe.

Par exemple, les données d'engagement des messages (ouvertures et clics d'e-mails, engagement sur les pages de destination, etc.) peuvent déterminer le niveau d'engagement d'un prospect. Vous pouvez transmettre ces données à votre entrepôt de données cloud et les rendre disponibles en entrée de vos modèles d'évaluation des prospects grâce aux solutions d'export de données en continu de Braze :

- [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)
- [Partage sécurisé des données Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)

{% endtab %}
{% tab Braze comme destination %}

Une fois que vos équipes internes ont créé et exécuté votre modèle d'évaluation des prospects, vous pouvez réintégrer ces données dans Braze afin de mieux segmenter et cibler les prospects avec des messages pertinents. Pour cela, utilisez l'[ingestion de données cloud de Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

Avec l'ingestion de données cloud, vos équipes internes créeront une nouvelle table ou vue contenant vos identifiants utilisateur, les derniers scores des prospects et les horodatages de mise à jour des scores. Braze récupérera la table ou la vue et ajoutera les scores des prospects aux profils utilisateurs.

{% endtab %}
{% endtabs %}

## Transfert de prospects : Marketing Qualified Lead (MQL) vers les ventes {#lead-handoff}

L'approche recommandée pour les transferts de prospects consiste à associer un prospect ou un contact à chaque utilisateur dans Braze. Ces prospects entrent dans la file d'attente de vos équipes commerciales lorsque leur statut passe à l'étape MQL, moment auquel Salesforce déclenche un workflow d'acheminement ou d'affectation des prospects.

Pour mettre à jour l'enregistrement du prospect dans Salesforce avec le statut provenant de Braze, nous recommandons d'utiliser un modèle de webhook déclenché.

### Étape 1 : Créer une Campaign webhook {#step-1-create-a-webhook-campaign}

### Étape 2 : Configurer votre webhook {#step-2-configure-your-webhook}

#### Étape 2a : Composer le webhook {#step-2a-compose-webhook}

1. Donnez un nom à votre Campaign webhook, par exemple « Salesforce > Mise à jour du prospect en MQL ».

2. Saisissez l'URL de votre webhook au format {% raw %}`https://YOUR_SALESFORCE_INSTANCE.my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %}. L'ID utilisateur Braze {% raw %}`{{${user_id}}}`{% endraw %} doit correspondre à votre ID de contact Salesforce. Si ce n'est pas le cas, utilisez un alias à la place de {% raw %}`{{${user_id}}}`{% endraw %}.

3. Modifiez la **HTTP Method** en **PATCH**.

4. Configurez votre payload pour ne mettre à jour l'enregistrement du prospect dans Salesforce que si le score de ce prospect dépasse votre seuil prédéfini. Consultez l'exemple de corps de requête ci-dessous pour un score de prospect supérieur à 100.

{% raw %}
```liquid
{% assign threshold = 100%}
{% if custom_attribute.${lead score} > threshold %}
{
"lead_status": "MQL"
}
{% else %}{% abort_message('not at threshold')%}
{% endif %}
```
{% endraw %}

{: start="5"}
5. Incluez les en-têtes suivants :

| En-tête | Contenu |
| --- | --- |
| Authorization | {% raw %}`Bearer {{result.access_token}}`{% endraw %}<br><br>Pour récupérer un jeton, [configurez une application connectée](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5) pour le flux d'identifiants client OAuth 2.0, puis utilisez le contenu connecté pour récupérer le bearer depuis Salesforce : <br><br>{% raw %}<code>{% connected_content https://[instance].my.salesforce.com/services/oauth2/token <br>:method post <br> :body client_id=[client_id]&client_secret=[client_secret]&grant_type=client_credentials <br>:save result %}{% endraw %} <br> Bearer {% raw %}{{result.access_token}}</code>{% endraw %} |
| Content-Type | application/json |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 2a : Composer le webhook" }

![Webhook composé avec une URL de webhook Salesforce, une méthode HTTP PATCH, un corps de requête en texte brut et des en-têtes de requête.]({% image_buster /assets/img/b2b/webhook.png %}){: style="max-width:80%;"}

#### Étape 2b : Planifier les envois du webhook {#step-2b-schedule-webhook-sends}

La Campaign doit se déclencher chaque fois que le score du prospect change. Elle se déclenchera pour tout utilisateur dont le score évolue, mais n'affectera que les utilisateurs qui ne sont pas encore MQL et qui ont franchi le seuil défini à l'étape précédente.

Dans l'étape **Schedule Delivery**, sélectionnez les éléments suivants :
- Un type de distribution **Action-Based**
- Une action de déclenchement **Change Custom Attribute Value** avec le nom de votre attribut d'évaluation des prospects et une action **any new value**

#### Étape 2c : Identifier l'audience cible {#step-2c-identify-target-audience}

Dans l'étape **Target Audiences**, incluez un filtre qui exclut les utilisateurs dont le statut de prospect est déjà au niveau MQL ou au-delà, par exemple « `lead_status` `is none of` `MQL` ».

![Options de ciblage du webhook avec le filtre « lead_status » n'est pas « MQL ».]({% image_buster /assets/img/b2b/step_3_webhook.png %}){: style="max-width:80%;"}

### Étape 3 : Lancer la Campaign {#step-3-launch-campaign}

Sélectionnez **Launch** et observez l'évolution du statut de vos prospects dans Salesforce à mesure que vos clients franchissent le seuil du score MQL.