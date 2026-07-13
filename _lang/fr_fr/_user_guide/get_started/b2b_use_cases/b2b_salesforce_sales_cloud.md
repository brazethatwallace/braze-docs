---
nav_title: Salesforce Sales Cloud
article_title: Gérer les prospects avec Salesforce Sales Cloud
page_order: 3
page_type: reference
description: "Découvrez comment utiliser les webhooks de Braze pour créer et mettre à jour des prospects dans Salesforce Sales Cloud via l'endpoint Salesforce sobjects/Lead."
---

# Gérer les prospects avec Salesforce Sales Cloud {#manage-leads-with-salesforce-sales-cloud}

> [Salesforce](https://www.salesforce.com/) est l'une des principales plateformes de gestion de la relation client (CRM) basées sur le cloud, conçue pour aider les entreprises à gérer l'ensemble de leur processus de vente, notamment la génération de prospects, le suivi des opportunités et la gestion des comptes.<br><br>Cette page montre comment utiliser les webhooks de Braze pour créer et mettre à jour des prospects dans Salesforce Sales Cloud via une intégration soumise par la communauté.

{% alert important %}
Il s'agit d'une intégration proposée par la communauté qui n'est pas directement prise en charge par Braze. Seuls les modèles de webhook officiels fournis par Braze sont pris en charge par Braze.
{% endalert %}

## Fonctionnement {#how-it-works}

L'intégration de Braze avec Salesforce Sales Cloud utilise les webhooks de Braze pour créer et mettre à jour des prospects dans Salesforce Sales Cloud via l'endpoint Salesforce [sobjects/Lead](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_lead.html).

Braze propose actuellement deux intégrations avec Salesforce Sales Cloud pour les cas d'usage suivants :
1. [Créer un prospect dans Salesforce Sales Cloud](#creating-lead)
2. [Mettre à jour un prospect dans Salesforce Sales Cloud](#updating-lead)

{% alert note %}
Cette intégration sert uniquement à mettre à jour Salesforce depuis Braze dans le cadre de vos efforts d'acquisition et de maturation de prospects. Pour synchroniser les données de Salesforce vers Braze, consultez le [modèle de données B2B]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/b2b_data_models) ou contactez l'un de nos [partenaires technologiques]({{site.baseurl}}/partners/home).
{% endalert %}

## Conditions préalables {#prerequisites}

Avant de pouvoir procéder à cette intégration, l'assistance Salesforce doit vous accorder la possibilité de créer des applications connectées. Vous pouvez en faire la demande en soumettant une [demande d'assistance Salesforce](https://help.salesforce.com/s/articleView?id=005167035&type=1).

Une fois que l'assistance Salesforce vous a accordé la possibilité de créer une application connectée dans Salesforce Sales Cloud, suivez les étapes de la documentation Salesforce : [Configure a Connected App for the OAuth 2.0 Client Credentials Flow](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5).

Lorsque vous configurez les paramètres OAuth nécessaires pour l'application connectée, conservez tous les paramètres OAuth avec leurs valeurs et sélections par défaut, à l'exception des éléments suivants :
1. Sélectionnez **Enable for device flow**. Vous pouvez laisser le champ **Callback URL** vide, car il sera remplacé par défaut par une marque substitutive.
2. Pour les **OAuth Scopes** sélectionnées, ajoutez **Manage user data via APIs (api)**.
3. Sélectionnez **Enable Client Credentials Flow**.

## Créer un prospect dans Salesforce Sales Cloud {#creating-lead}

En tant que plateforme d'engagement client, Braze peut générer de nouveaux prospects en fonction des flux utilisateurs, par exemple lorsqu'un formulaire est rempli sur une page de destination. Lorsque cela se produit, vous pouvez utiliser un webhook Braze Salesforce Sales Cloud pour créer un prospect correspondant dans Salesforce.

### Étape 1 : Récupérez vos `client_id` et `client_secret` {#step-1-collect-your-client_id-and-client_secret}

1. Dans Salesforce, accédez à **Platform Tools** > **Apps** > **App Manager**.
2. Recherchez votre application Braze nouvellement créée et sélectionnez **View**.
3. Sous **Consumer Key and Secret**, sélectionnez **Manage Consumer Details**.
4. Sur la page qui s'affiche, notez votre **Consumer Key** et votre **Consumer Secret**. La **Consumer Key** correspond à votre `client_id`, et le **Consumer Secret** correspond à votre `client_secret`.

### Étape 2 : Configurez votre modèle de webhook {#step-2-set-up-your-webhook-template}

Utilisez des modèles pour réutiliser rapidement ce webhook sur la plateforme Braze.

1. Dans Braze, accédez à **Modèles**, sélectionnez **Modèles de webhook**, puis sélectionnez **+ Create Webhook Template**.
2. Donnez un nom au modèle, par exemple « Salesforce Sales Cloud > Créer un prospect ».
3. Dans l'onglet **Rédiger**, saisissez les informations suivantes :

#### Rédiger le webhook {#compose-webhook}

| Champ | Détails |
| --- | --- |
| URL du webhook | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/`{% endraw %} |
| Méthode HTTP | `POST` |
| Corps de la requête | Paires clé/valeur JSON |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rédiger le webhook" }

#### Valeurs clés des propriétés du corps {#body-property-key-values}

Sélectionnez **+ Add New Body Property** pour chacune des paires clé/valeur que vous souhaitez mapper de Braze vers Salesforce. Vous pouvez mapper n'importe quel champ ; le tableau suivant n'est qu'un exemple.

| Clé | Valeur |
| --- | --- |
| firstName | {% raw %}`{{${first_name}}}`{% endraw %} |
| lastName | {% raw %}`{{${last_name}}}`{% endraw %} |
| email | {% raw %}`{{${email_address}}}`{% endraw %} |
| company | {% raw %}`{{custom_attribute.${company}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Valeurs clés des propriétés du corps" }

#### En-têtes de requête {#request-headers}

Sélectionnez **+ Add New Header** pour chacun des en-têtes de requête suivants.

| Clé | Valeur |
| --- | --- |
| Authorization | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Content-Type | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="En-têtes de requête" }

{: start="4" }
4. Sélectionnez **Save Template**.

![Un modèle de webhook rempli pour créer un prospect.]({% image_buster /assets/img/b2b/create_lead_webhook.png %}){: style="max-width:70%;"}

## Mettre à jour un prospect dans Salesforce Sales Cloud {#updating-lead}

Pour configurer un webhook Braze Salesforce Sales Cloud qui met à jour les prospects dans Salesforce, vous avez besoin d'un identifiant commun entre Salesforce Sales Cloud et Braze. L'exemple de la section suivante utilise le `lead_id` de Salesforce comme `external_id` dans Braze, mais vous pouvez également utiliser un `user_alias`. Pour plus de détails, consultez la section [Données B2B]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/b2b_data_models).

Cet exemple montre spécifiquement comment mettre à jour le stade d'un prospect en « MQL » (Marketing Qualified Lead) après qu'il a franchi un certain seuil de score. Il s'agit d'un élément central de notre cas d'usage de [workflow de scoring des prospects B2B]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/lead_scoring).

### Étape 1 : Récupérez vos `client_id` et `client_secret`

1. Dans Salesforce, accédez à **Platform Tools** > **Apps** > **App Manager**.
2. Recherchez votre application Braze nouvellement créée et sélectionnez **View**.
3. Sous **Consumer Key and Secret**, sélectionnez **Manage Consumer Details**.
4. Sur la page qui s'affiche, notez votre **Consumer Key** et votre **Consumer Secret**.
    - La **Consumer Key** correspond à votre `client_id`, et le **Consumer Secret** correspond à votre `client_secret`.

### Étape 2 : Configurez votre modèle de webhook

1. Dans Braze, accédez à **Modèles**, sélectionnez **Modèles de webhook**, puis sélectionnez **+ Create Webhook Template**.
2. Donnez un nom au modèle, par exemple « Salesforce Sales Cloud > Mettre à jour le prospect en MQL ».
3. Dans l'onglet **Rédiger**, saisissez les informations suivantes :

#### Rédiger le webhook

| Champ | Détails |
| --- | --- |
| URL du webhook | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %} |
| Méthode HTTP | `PATCH` |
| Corps de la requête | Paires clé/valeur JSON |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rédiger le webhook" }

#### Valeurs clés des propriétés du corps

Sélectionnez **+ Add New Body Property** pour la paire clé/valeur suivante. Notez que `Lead_Stage__c` est un exemple de nom. Le champ personnalisé que vous utilisez pour suivre les MQL dans Salesforce peut avoir un nom différent ; assurez-vous qu'ils correspondent.

| Clé | Valeur |
| --- | --- |
| `Lead_Stage__c` | `MQL` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Valeurs clés des propriétés du corps" }

#### En-têtes de requête

Sélectionnez **+ Add New Header** pour chacun des en-têtes de requête suivants.

| Clé | Valeur |
| --- | --- |
| Authorization | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Content-Type | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="En-têtes de requête" }

{: start="4"}
4. Sélectionnez **Save Template**.

![Un modèle de webhook rempli pour mettre à jour un prospect.]({% image_buster /assets/img/b2b/update_lead_webhook.png %}){: style="max-width:70%;"}

## Utiliser ces webhooks dans un flux de travail opérationnel {#using-these-webhooks-in-an-operational-workflow}

Vous pouvez rapidement ajouter vos modèles à vos flux de travail opérationnels dans Braze, par exemple :

1. Dans le cadre d'une [Campaign pour les nouveaux prospects](#new-lead) qui crée un prospect dans Salesforce.
2. Dans le cadre d'un [Canvas de scoring des prospects](#lead-scoring) qui met à jour les utilisateurs ayant franchi votre seuil MQL en « MQL » et qui met à jour Salesforce Sales Cloud avec les mêmes informations.

### Campaign pour les nouveaux prospects {#new-lead}

Pour créer un prospect dans Salesforce lorsqu'un utilisateur fournit son adresse e-mail, vous pouvez créer une Campaign qui utilise le modèle de webhook « Update Lead » et se déclenche lorsqu'un utilisateur ajoute son adresse e-mail (par exemple, lorsqu'il remplit un formulaire web).

![Étape 2 de la création d'une Campaign basée sur des actions dont l'action de déclenchement est « Ajouter une adresse e-mail ».]({% image_buster /assets/img/b2b/salesforce_create_campaign.png %}){: style="max-width:70%;"}

### Canvas de scoring des prospects pour le franchissement du seuil MQL (Marketing Qualified Lead) {#lead-scoring}

Ce webhook est abordé dans le cas d'usage du [lead scoring]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/lead_scoring#lead-handoff), mais vous pouvez également vérifier les MQL et mettre directement à jour Salesforce dans le Canvas de scoring des prospects (au lieu de créer une Campaign webhook distincte) :

Ajoutez une étape supplémentaire à votre mise à jour utilisateur pour vérifier si un utilisateur a franchi le seuil MQL que vous avez défini. Si c'est le cas, mettez à jour le statut de l'utilisateur en « MQL », puis mettez à jour Salesforce avec le même statut « MQL » à l'aide de ce modèle de webhook. Salesforce s'occupe du reste en acheminant ce prospect vers les équipes commerciales appropriées selon vos règles de routage des prospects.

#### Ajouter une étape Canvas pour vérifier les utilisateurs ayant franchi le seuil MQL {#adding-canvas-step-to-check-for-users-who-passed-the-mql-threshold}

1. Ajoutez une étape de **parcours d'audience** avec deux groupes : « MQL Threshold » et « Everyone Else ».
2. Dans le groupe « MQL Threshold », recherchez les utilisateurs dont le statut n'est pas « MQL » (par exemple, `lead_stage` est égal à « Lead »), mais dont le score de prospect dépasse le seuil que vous avez défini (par exemple, `lead_score` supérieur à 50). Si c'est le cas, ils passent à l'étape suivante ; sinon, ils sortent du flux.

![Le groupe de parcours d'audience « MQL Threshold » avec des filtres pour un `lead_stage` égal à « Lead » et un `lead_score` supérieur à « 50 ».]({% image_buster /assets/img/b2b/salesforce_check_mql.png %}){: style="max-width:70%;"}

{: start="3" }
3. Ajoutez une étape de **mise à jour utilisateur** qui met à jour la valeur de l'attribut `lead_stage` de l'utilisateur en « MQL ».

![L'étape de mise à jour utilisateur « Update to MQL » qui met à jour l'attribut `lead_stage` avec la valeur « MQL ».]({% image_buster /assets/img/b2b/salesforce_update_mql.png %}){: style="max-width:70%;"}

{: start="4" }
4. Ajoutez une étape webhook qui met à jour Salesforce avec le nouveau stade MQL.

![L'étape webhook « Update Salesforce » avec les détails renseignés.]({% image_buster /assets/img/b2b/salesforce_webhook.png %}){: style="max-width:70%;"}

Votre flux Canvas mettra désormais à jour les utilisateurs ayant franchi votre seuil MQL !

![Une étape de mise à jour utilisateur dans un Canvas qui vérifie si un utilisateur franchit le seuil MQL et, le cas échéant, met à jour Salesforce.]({% image_buster /assets/img/b2b/salesforce_canvas.png %}){: style="max-width:50%;"}

## Résolution des problèmes {#troubleshooting}

Ces flux de travail offrent des capacités de débogage limitées dans Salesforce. Nous vous recommandons donc de consulter le [journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log#message-activity-log) de Braze pour comprendre pourquoi un webhook a échoué et si des erreurs se sont produites.

Par exemple, une erreur causée par une URL invalide utilisée pour la récupération du jeton OAuth s'affichera sous la forme `https://[insert_instance_name].my.salesforce.com/services/oauth2/token is not a valid URL`.

![Un corps de réponse d'erreur indiquant que l'URL n'est pas valide.]({% image_buster /assets/img/b2b/error_message_invalid_url.png %})