---
nav_title: Évaluation des prospects
article_title: Créer un workflow de notation des prospects
page_order: 1
page_type: reference
description: "Découvrez comment utiliser Braze pour réaliser une évaluation simple des prospects, une évaluation externe des prospects et des transferts de prospects."
---

# Créer un workflow de notation des prospects

> Ce cas d'utilisation montre comment utiliser Braze pour mettre à jour les scores des prospects en temps réel et transmettre automatiquement les prospects qualifiés à vos équipes commerciales.

La création d'un workflow de notation des prospects dans Braze repose sur deux étapes clés :

1. Créer un Canvas de notation des prospects dans Braze ou intégrer un outil externe de notation des prospects :
- [Évaluation simple des prospects](#simple-lead-scoring)
- [Évaluation externe des prospects](#external-lead-scoring)

2. Créer une campagne webhook pour envoyer les prospects qualifiés à votre équipe commerciale :
- [Transfert de prospects : Marketing Qualified Lead (MQL) vers les ventes](#lead-handoff)

## Évaluation simple des prospects

### Étape 1 : Créer un Canvas

1. Accédez à **Messagerie** > **Canvas** et sélectionnez **Créer un Canvas**, puis renseignez les informations de base de votre Canvas.

2. Donnez à votre Canvas un nom pertinent, tel que « Canvas de notation des prospects » et, pour le retrouver facilement, attribuez-lui une étiquette comme « Gestion des prospects ».<br><br>![Étape 1 de la création d'un Canvas avec le nom « Canvas de notation des prospects » et l'étiquette « Gestion des prospects ».]({% image_buster /assets/img/b2b/step_1_simple.png %}){: style="max-width:80%;"}

### Étape 2 : Définir vos critères d'entrée

1. Passez à l'étape **Planification d'entrée** et sélectionnez une planification d'entrée **par événement**. Les utilisateurs entreront ainsi dans le Canvas lorsqu'ils effectueront des actions spécifiques.

2. Dans **Options basées sur l'action**, ajoutez ces deux actions :
    - **Modifier la valeur de l'attribut personnalisé** avec le nom de votre attribut de notation des prospects (par exemple `lead score`). Si vous n'avez pas encore créé d'attribut de notation des prospects, suivez les étapes décrites dans [Attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/). Les utilisateurs entreront ainsi dans le Canvas chaque fois que leur score de prospect change.
    - **Ajouter une adresse e-mail**

![Étape 2 de la création d'un Canvas avec la planification d'entrée « Par événement » et les options basées sur l'action de modification d'un attribut personnalisé « lead score » et d'ajout d'une adresse e-mail.]({% image_buster /assets/img/b2b/step_2_simple.png %}){: style="max-width:80%;"}

### Étape 3 : Identifier votre audience cible

#### Étape 3a : Sélectionner des segments

Tous les utilisateurs sont éligibles à la notation des prospects. Vous pouvez donc ajouter des règles spécifiques à votre entreprise pour déterminer qui évaluer en sélectionnant les [segments]({{site.baseurl}}/user_guide/audience/segments/) d'utilisateurs à cibler et en appliquant des [filtres]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/) supplémentaires. Par exemple, vous pouvez exclure les employés, les utilisateurs déjà clients, etc. 

![Étape 3 de la création d'un Canvas avec des options de sélection de segments et de filtres pour affiner l'audience d'entrée.]({% image_buster /assets/img/b2b/step_3_simple.png %}){: style="max-width:80%;"}

#### Étape 3b : Configurer la rééligibilité du Canvas

Un utilisateur passera par ce Canvas de nombreuses fois au cours de son cycle de vie. Assurez-vous donc qu'il puisse y entrer à nouveau aussi rapidement qu'il en est sorti la fois précédente, grâce aux paramètres de rééligibilité. 

Dans **Contrôles d'entrée**, procédez comme suit :
- Sélectionnez **Autoriser les utilisateurs à entrer à nouveau dans ce Canvas**.
- Sélectionnez **Fenêtre spécifiée**.
- Définissez la rééligibilité sur « 0 » **secondes**.

![Section « Contrôles d'entrée » avec les options « Autoriser les utilisateurs à entrer à nouveau dans ce Canvas » dans une « Fenêtre spécifiée » de 0 seconde.]({% image_buster /assets/img/b2b/entry_controls_simple.png %}){: style="max-width:80%;"}

#### Étape 3c : Mettre à jour les paramètres d'envoi

Étant donné la nature opérationnelle de ce Canvas et le fait qu'aucun message ne sera envoyé à ces utilisateurs, vous n'avez pas besoin de respecter les statuts d'abonnement.

Sous **Paramètres d'abonnement**, pour **Envoyer à ces utilisateurs :** sélectionnez **tous les utilisateurs, y compris les utilisateurs désabonnés**. 

![Étape 4 de la création d'un Canvas pour la définition des options d'envoi des messages.]({% image_buster /assets/img/b2b/step_4_simple.png %}){: style="max-width:80%;"}

### Étape 4 : Construire votre Canvas

#### Étape 4a : Ajouter un parcours d'action

Sous votre variante, cliquez sur l'icône plus, puis sélectionnez **Parcours d'actions**.

![Canvas avec « Parcours d'actions » affiché dans le menu ouvert par l'icône plus.]({% image_buster /assets/img/b2b/action_paths_simple.png %}){: style="max-width:60%;"}

#### Étape 4b : Créer des groupes d'action

Chaque groupe d'action représente l'ensemble des actions qui conduisent à la même incrémentation ou décrémentation de points. Vous pouvez définir jusqu'à huit groupes d'action. Dans ce scénario, nous allons en créer quatre.

Ajoutez les groupes suivants à votre parcours d'action :

- **Groupe 1 :** Tous les événements comptant pour une incrémentation de 1 point.
- **Groupe 2 :** Tous les événements comptant pour une incrémentation de 5 points.
- **Groupe 3 :** Tous les événements comptant pour une décrémentation de 1 point.
- **Tous les autres :** Les Parcours d'actions vous permettent de définir une fenêtre d'attente pour voir si un utilisateur effectue une action, avant de le placer dans un groupe « Tous les autres ». Pour la notation des prospects, c'est l'occasion de diminuer le score pour cause d'« inactivité ».

![Parcours d'action contenant des groupes d'actions pour ajouter un point, cinq points et dix points ; soustraire un point et dix points ; et « Tous les autres ».]({% image_buster /assets/img/b2b/action_paths_selected_simple.png %}){: style="max-width:20%;"}

#### Étape 4c : Configurer chaque groupe pour inclure les événements pertinents

Dans chaque groupe d'action, sélectionnez **Sélectionner un déclencheur** et choisissez l'événement qui ajoutera le nombre de points correspondant à ce groupe d'action. Ajoutez d'autres déclencheurs pour inclure tous les événements qui incrémenteront le score du prospect d'un point. Par exemple, un utilisateur pourrait incrémenter son score d'un point lorsqu'il démarre une session dans n'importe quelle application ou effectue un événement personnalisé (comme s'inscrire ou participer à un webinaire). 

![Groupe d'action pour l'ajout d'un point avec les déclencheurs « Démarrer une session dans n'importe quelle application » et « Effectuer un événement personnalisé ».]({% image_buster /assets/img/b2b/action_groups_simple.png %}){: style="max-width:80%;"}

#### Étape 4d : Ajouter des étapes Mise à jour utilisateur

Ajoutez une étape Mise à jour utilisateur à chaque parcours du Canvas créé sous votre parcours d'action. 

![Canvas affichant le parcours d'action avec des chemins de Mise à jour utilisateur ramifiés pour chaque groupe d'action.]({% image_buster /assets/img/b2b/user_update_paths_simple.png %}){: style="max-width:80%;"}

{: start="2"}
Dans l'onglet **Rédiger** de chaque étape Mise à jour utilisateur, procédez comme suit pour les champs correspondants :

| Champ | Action |
| --- | --- |
| **Nom de l'attribut** | Sélectionnez l'attribut de notation des prospects choisi à l'étape 2 (`lead score`).|
| **Action** | Changez l'action en **Incrémenter par** si le parcours augmente le score ou **Décrémenter par** si le parcours diminue le score. |
| **Incrémenter par** ou **Décrémenter par** | Saisissez le nombre de points à ajouter ou à retrancher du score du prospect.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Étape 5 : Lancer votre Canvas

C'est tout ! Votre Canvas de notation des prospects est prêt à être lancé.

## Évaluation externe des prospects

Que vous utilisiez l'un de nos [partenaires technologiques]({{site.baseurl}}/partners/home/), votre propre modèle interne de notation des prospects, le machine learning ou un autre outil de notation, nous avons plusieurs options à votre disposition.

### Partenaires externes

Consultez la page [Partenaires technologiques]({{site.baseurl}}/partners/home) pour en savoir plus sur nos partenaires B2B proposant des fonctionnalités de notation des prospects. Votre outil n'y figure pas ? Vous pouvez l'intégrer en appelant notre endpoint d'API [`users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users). 

### Modèles de données internes pour la notation des prospects

Vous pouvez intégrer Braze à vos modèles de données internes, y compris les modèles de notation des prospects, de différentes manières. Voici quelques exemples courants d'intégration réalisées par nos clients.

#### Entrepôt de données cloud intégré

{% tabs %}
{% tab Braze as a data source %}

En tant qu'outil marketing, Braze contient des données extrêmement pertinentes qui peuvent enrichir le modèle interne de notation des prospects de votre équipe. 

Par exemple, les données d'engagement des messages (ouvertures et clics d'e-mails, engagement sur les pages d'accueil, etc.) peuvent déterminer le niveau d'engagement d'un prospect. Vous pouvez transmettre ces données à votre entrepôt de données cloud et les rendre disponibles en entrée de vos modèles de notation des prospects grâce aux solutions d'export de données en continu de Braze :

- [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)
- [Partage sécurisé des données Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)

{% endtab %}
{% tab Braze as a destination %}

Une fois que vos équipes internes ont créé et exécuté votre modèle de notation des prospects, vous pouvez réintégrer ces données dans Braze afin de mieux segmenter et cibler les prospects avec des messages pertinents. Pour cela, utilisez l'[Ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/) de Braze. 

Avec l'Ingestion de données cloud, vos équipes internes créeront une nouvelle table ou vue contenant vos identifiants utilisateur, les derniers scores des prospects et les horodatages de mise à jour des scores. Braze récupérera la table ou la vue et ajoutera les scores des prospects aux profils utilisateurs.

{% endtab %}
{% endtabs %}

## Transfert de prospects : Marketing Qualified Lead (MQL) vers les ventes {#lead-handoff}

L'approche recommandée pour les transferts de prospects consiste à associer un prospect ou un contact à chaque utilisateur dans Braze. Ces prospects entrent dans la file d'attente de vos équipes commerciales lorsque leur statut passe à l'étape MQL, moment auquel Salesforce déclenche un workflow d'acheminement ou d'affectation des prospects. 

Pour mettre à jour l'enregistrement du prospect dans Salesforce avec le statut provenant de Braze, nous recommandons d'utiliser un modèle de webhook déclenché.

### Étape 1 : Créer une campagne webhook

### Étape 2 : Configurer votre webhook

#### Étape 2a : Composer le webhook

1. Donnez un nom à votre campagne webhook, par exemple « Salesforce > Mise à jour du prospect en MQL ».

2. Saisissez l'URL de votre webhook au format {% raw %}`https://YOUR_SALESFORCE_INSTANCE.my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %}. L'ID utilisateur Braze {% raw %}`{{${user_id}}}`{% endraw %} doit correspondre à votre ID de contact Salesforce. Si ce n'est pas le cas, utilisez un alias à la place de {% raw %}`{{${user_id}}}`{% endraw %}.

3. Modifiez la **méthode HTTP** en **PATCH**.

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
| Content_Type | application/json |
{: .reset-td-br-1 reset-td-br-2}

![Webhook composé avec une URL de webhook Salesforce, une méthode HTTP PATCH, un corps de requête en texte brut et des en-têtes de requête.]({% image_buster /assets/img/b2b/webhook.png %}){: style="max-width:80%;"}

#### Étape 2b : Planifier les envois du webhook

La campagne doit se déclencher chaque fois que le score du prospect change. Elle se déclenchera pour tout utilisateur dont le score évolue, mais n'affectera que les utilisateurs qui ne sont pas encore MQL et qui ont franchi le seuil défini à l'étape précédente.

Dans l'étape **Planifier la réception/distribution**, sélectionnez les éléments suivants :
- Un type de réception/distribution **par événement**
- Une action de déclenchement **Modifier la valeur de l'attribut personnalisé** avec le nom de votre attribut de notation des prospects et une action de **toute nouvelle valeur**

#### Étape 2c : Identifier l'audience cible

Dans l'étape **Audiences cibles**, incluez un filtre qui exclut les utilisateurs dont le statut de prospect est déjà au niveau MQL ou au-delà, par exemple « `lead_status` `is none of` `MQL` ».

![Options de ciblage du webhook avec le filtre « lead_status » n'est pas « MQL ».]({% image_buster /assets/img/b2b/step_3_webhook.png %}){: style="max-width:80%;"}

### Étape 3 : Lancer la campagne

Sélectionnez **Lancer** et observez l'évolution du statut de vos prospects dans Salesforce à mesure que vos clients franchissent le seuil du score MQL.