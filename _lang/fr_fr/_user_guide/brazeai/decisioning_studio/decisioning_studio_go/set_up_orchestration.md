---
nav_title: "Configurer l'orchestration"
article_title: "Configurer l'orchestration"
page_order: 2
description: "Découvrez comment connecter BrazeAI Decisioning Studio Go à votre plateforme d'engagement client pour permettre des communications personnalisées."
toc_headers: h2
---

# Configurer l'orchestration {#set-up-orchestration}

> BrazeAI Decisioning Studio™ Go doit se connecter à votre plateforme d'engagement client (CEP) pour orchestrer des communications personnalisées. Cet article explique comment configurer l'intégration pour chaque CEP pris en charge.

## CEP pris en charge {#supported-ceps}

Decisioning Studio Go prend en charge les plateformes d'engagement client suivantes :

| CEP | Type d'intégration | Fonctionnalités clés |
|-----|-----------------|--------------|
| **Braze** | Campaigns déclenchées par API | Intégration native, déclenchement en temps réel |
| **Salesforce Marketing Cloud** | Journey Builder avec événements API | Automatisation des requêtes SQL, extensions de données |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CEP pris en charge" }

Sélectionnez votre CEP dans cette liste pour commencer la configuration de l'intégration.

{% tabs %}
{% tab Braze %}

## Configurer l'intégration Braze {#set-up-braze-integration}

Pour intégrer Decisioning Studio Go avec Braze, vous allez créer une clé API, configurer une campagne déclenchée par API et fournir les identifiants nécessaires au portail Decisioning Studio Go.

### Étape 1 : Créer une clé API REST {#step-1-create-a-rest-api-key}

1. Dans le tableau de bord de Braze, accédez à **Paramètres** > **API et identifiants** > **Clés API**.
2. Sélectionnez **Créer une clé API**.
3. Saisissez un nom pour votre clé API. Par exemple : « DecisioningStudioGoEmail ».
4. Sélectionnez les autorisations en fonction des catégories suivantes :
    - **Données utilisateur :** sélectionnez `users.track`, `users.delete`, `users.export.ids`, `users.export.segment`
    - **Messages :** sélectionnez `messages.send`, `messages.schedule.create`, `messages.schedule.update`, `messages.schedule.delete`
    - **Campaigns :** sélectionnez toutes les autorisations répertoriées
    - **Canvas :** sélectionnez toutes les autorisations répertoriées
    - **Segments :** sélectionnez toutes les autorisations répertoriées
    - **Modèles :** sélectionnez toutes les autorisations répertoriées

{: start="5"}
5. Sélectionnez **Créer une clé API**.
6. Copiez la clé API et collez-la dans votre portail BrazeAI Decisioning Studio™ Go.

### Étape 2 : Identifier le nom d'affichage de votre e-mail {#step-2-locate-your-email-display-name}

1. Dans le tableau de bord de Braze, accédez à **Paramètres** > **Préférences des e-mails**.
2. Identifiez le nom d'affichage à utiliser avec BrazeAI Decisioning Studio™ Go.
3. Copiez et collez le **From Display Name** dans le portail BrazeAI Decisioning Studio™ Go en tant que **Email Display Name**.
4. Copiez et collez l'adresse e-mail associée dans votre portail BrazeAI Decisioning Studio™ Go en tant qu'**adresse e-mail d'expéditeur** (From email address), en combinant la partie locale et le domaine.

### Étape 3 : Trouver votre URL Braze et votre ID d'application {#step-3-find-your-braze-url-and-app-id}

**Pour trouver votre URL Braze :**
1. Accédez au tableau de bord de Braze.
2. Dans la fenêtre de votre navigateur, votre URL Braze commence par `https://` et se termine par `braze.com`. Exemple d'URL Braze : `https://dashboard-01.braze.com`.

**Pour trouver votre ID d'application (clé API) :**

{% alert note %}
Braze fournit des ID d'application (appelés clés API dans le tableau de bord de Braze) que vous pouvez utiliser à des fins de suivi, par exemple pour associer une activité à une application spécifique dans votre espace de travail. Si vous utilisez des ID d'application, BrazeAI Decisioning Studio™ Go prend en charge l'association d'un ID d'application à chaque expérimentateur.<br><br>Si vous n'utilisez pas d'ID d'application, vous pouvez saisir n'importe quelle chaîne de caractères comme marque substitutive.
{% endalert %}

1. Dans le tableau de bord de Braze, accédez à **Paramètres** > **Paramètres des applications**.
2. Accédez à l'application que vous souhaitez suivre.
3. Copiez et collez la **clé API** dans votre portail BrazeAI Decisioning Studio™ Go.

### Étape 4 : Créer une campagne déclenchée par API {#step-4-create-an-api-triggered-campaign}

1. Dans le tableau de bord de Braze, accédez à **Messaging** > **Campaigns**.
2. Sélectionnez **Create Campaign**.
3. Pour le type de campagne, sélectionnez **API Campaign**.
4. Saisissez un nom pour votre campagne. Par exemple : « Decisioning Studio Go Email ».

![Une campagne API intitulée « Decisioning Studio Go Email ».]({% image_buster /assets/img/decisioning_studio_go/api_campaign_name.png %})

{: start="5"}
5. Pour votre canal de communication, sélectionnez **Email**.

![Option permettant de sélectionner votre canal de communication pour la campagne API.]({% image_buster /assets/img/decisioning_studio_go/select_api_campaign.png %})

{: start="6"}
6. Dans **Additional Options**, cochez la case **Allow users to become re-eligible to receive campaign**.
7. Pour le délai de rééligibilité, saisissez **1** et sélectionnez **Hours** dans le menu déroulant.

![Rééligibilité sélectionnée pour la campagne API.]({% image_buster /assets/img/decisioning_studio_go/additional_options.png %})

{: start="8"}
8. Sélectionnez **Save Campaign**.

### Étape 5 : Copier les ID de votre campagne et de votre message {#step-5-copy-your-campaign-and-message-ids}

1. Dans votre campagne API, copiez le **Campaign ID**. Ensuite, accédez au portail BrazeAI Decisioning Studio™ Go et collez le **Campaign ID**.

![Exemple d'ID de variante de message à copier-coller.]({% image_buster /assets/img/decisioning_studio_go/campaign_id.png %})

{: start="2"}
2. Copiez le **Message Variation ID**. Ensuite, accédez au portail BrazeAI Decisioning Studio™ Go et collez le **Message Variation ID**.

### Étape 6 : Identifier un ID d'utilisateur test {#step-6-locate-a-test-user-id}

Pour tester votre intégration, vous aurez besoin d'un ID utilisateur :

Si votre espace de travail utilise le [chiffrement au niveau des champs d'identification]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption), tout nouvel utilisateur test créé avec l'endpoint `/users/track` doit respecter les exigences relatives aux e-mails pour les espaces de travail chiffrés. Envoyez le champ `email` sous forme de hachage HMAC-SHA256 encodé en Base64 de la valeur de l'e-mail en minuscules, et envoyez `email_encrypted` comme valeur d'e-mail chiffrée générée avec vos clés de chiffrement PII configurées.

1. Dans le tableau de bord de Braze, accédez à **Audience** > **Rechercher des utilisateurs**.
2. Recherchez l'utilisateur par son ID externe, son alias d'utilisateur, son e-mail, son numéro de téléphone ou son jeton de notification push.
3. Copiez l'ID utilisateur pour le référencer dans votre configuration.

![Exemple de profil utilisateur obtenu en recherchant un utilisateur par son ID.]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Configurer l'intégration SFMC {#set-up-sfmc-integration}

Pour intégrer Decisioning Studio Go avec Salesforce Marketing Cloud, vous allez configurer un package d'application, créer une automatisation de requête de données et construire un parcours pour gérer les envois déclenchés.

### Partie 1 : Configurer un package d'application SFMC {#part-1-set-up-an-sfmc-app-package}

1. Accédez à la page d'accueil de Marketing Cloud.
2. Ouvrez le menu dans l'en-tête global et sélectionnez **Setup**.
3. Accédez à **Apps** sous **Platform Tools** dans le panneau de navigation latéral, puis sélectionnez **Installed Packages**.
4. Sélectionnez **New** pour créer un package d'application.
5. Attribuez un nom et une description au package d'application.

![Un package d'application nommé « Experimenter 1 - Test 5 ».]({% image_buster /assets/img/decisioning_studio_go/sfmc_app_package1.png %})

{: start="6"}
6. Sélectionnez **Add Component**.
7. Pour le **Component Type**, sélectionnez **API Integration**. Puis sélectionnez **Next**.
8. Pour l'**Integration Type**, sélectionnez **Server-to-server**. Puis sélectionnez **Next**.
9. Sélectionnez uniquement les portées recommandées suivantes pour votre package d'application :
    - Channels > Email > Read, Write, Send
    - Channels > OTT > Read
    - Channels > Push > Read
    - Channels > SMS > Read
    - Channels > Social > Read
    - Channels > Web > Read
    - Assets > Documents and Images > Read, Write
    - Assets > Saved Content > Read, Write
    - Automation > Automations > Read, Write, Execute
    - Automation > Journeys > Read, Write, Execute, Activate/Stop/Pause/Send/Schedule
    - Contacts > Audiences > Read
    - Contacts > List and Subscribers > Read, Write
    - Cross Cloud Platform > Market Audience > View
    - Cross Cloud Platform > Market Audience Member > View
    - Cross Cloud Platform > Marketing Cloud Connect > Read
    - Data > Data Extensions > Read, Write
    - Data > File Locations > Read
    - Data > Tracking Events > Read, Write
    - Event notifications > Callbacks > Read
    - Event notifications > Subscriptions > Read

{% details Afficher l'image des portées recommandées %}

![Portées recommandées pour le package d'application Salesforce Marketing Cloud.]({% image_buster /assets/img/decisioning_studio_go/app_package_scopes.png %})

{% enddetails %}

{: start="10"}
10. Sélectionnez **Save**.
11. Copiez et collez les champs suivants dans le portail BrazeAI Decisioning Studio™ Go : **Client Id**, **Client Secret**, **Authentication Base URI**, **REST Base URI**, **SOAP Base URI**.

### Partie 2 : Configurer l'automatisation des requêtes de données {#part-2-set-up-a-data-query-automation}

#### Étape 1 : Créer une nouvelle automatisation {#step-1-create-a-new-automation}

1. Depuis la page d'accueil de Salesforce Marketing Cloud, accédez à **Journey Builder** et sélectionnez **Automation Studio**.

![Option Automation Studio dans la navigation de Journey Builder.]({% image_buster /assets/img/decisioning_studio_go/query13.png %})

{: start="2"}
2. Sélectionnez **New Automation**.
3. Glissez-déposez un nœud **Schedule** comme **Starting Source**.

![« Schedule » comme source de départ d'un parcours.]({% image_buster /assets/img/decisioning_studio_go/query14.png %})

{: start="4"}
4. Dans le nœud **Schedule**, sélectionnez **Configure**.
5. Définissez les paramètres suivants pour la planification :
    - **Start Date :** le jour calendaire de demain
    - **Time :** **12:00 AM**
    - **Time Zone :** **(GMT-05:00) Eastern (US & Canada)**
6. Pour **Repeat**, sélectionnez **Daily**.
7. Configurez cette planification pour qu'elle ne se termine jamais.
8. Sélectionnez **Done** pour enregistrer la planification.

![Exemple de planification défini pour le 25 janvier 2024 à minuit (heure de l'Est), à répéter quotidiennement.]({% image_buster /assets/img/decisioning_studio_go/query12.png %})

#### Étape 2 : Créer vos requêtes SQL {#step-2-create-your-sql-queries}

Ensuite, créez deux requêtes SQL : une requête sur les utilisateurs abonnés et une requête sur l'engagement. Ces requêtes permettent à BrazeAI Decisioning Studio™ Go de récupérer les données nécessaires pour constituer l'audience et ingérer les événements d'engagement.

**Requête des utilisateurs abonnés :**

1. Glissez-déposez une **SQL Query** dans le canvas.
2. Sélectionnez **Choose**.
3. Sélectionnez **Create New Query Activity**.
4. Attribuez un nom et une clé externe à la requête. Nous recommandons d'utiliser le nom et la clé externe suggérés pour la requête des utilisateurs abonnés dans votre portail BrazeAI Decisioning Studio™ Go.

![Exemple « OFE_Subscribers_query_Test5 » et la clé externe.]({% image_buster /assets/img/decisioning_studio_go/query11.png %})

{: start="5"}
5. Sélectionnez **Next**.
6. Dans votre portail BrazeAI Decisioning Studio™ Go, localisez la requête SQL des données système sous **Subscriber Query Resources**.
7. Copiez et collez la requête dans la zone de texte, puis sélectionnez **Next**.

![Exemple de requête dans la section SQL Query.]({% image_buster /assets/img/decisioning_studio_go/query10.png %})

{: start="8"}
8. Dans votre portail BrazeAI Decisioning Studio™ Go, dans la section **Resources to use**, localisez la clé externe de l'extension de données cible. Collez-la ensuite dans la barre de recherche.

![Une clé externe collée dans la barre de recherche.]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9. Sélectionnez l'extension de données correspondant à la clé externe recherchée. Le nom de l'extension de données cible est également fourni dans votre portail BrazeAI Decisioning Studio™ Go pour référence croisée. La **Data Extension** pour la requête des utilisateurs abonnés doit se terminer par le suffixe `BASE_AUDIENCE_DATA`.

![Nom de l'extension de données correspondant à la clé externe de l'exemple.]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10. Sélectionnez **Overwrite**, puis **Next**.

**Requête d'engagement :**

1. Glissez-déposez une **SQL Query** dans le canvas.

![« SQL Query » ajoutée comme activité dans le parcours.]({% image_buster /assets/img/decisioning_studio_go/query7.png %})

{: start="2"}
2. Sélectionnez **Choose**.
3. Sélectionnez **Create New Query Activity**.
4. Attribuez un nom et une clé externe à la requête. Nous recommandons d'utiliser le nom et la clé externe suggérés pour la requête d'engagement dans votre portail BrazeAI Decisioning Studio™ Go.

![Exemple « OFE_Engagement_query » et la clé externe.]({% image_buster /assets/img/decisioning_studio_go/query6.png %})

{: start="5"}
5. Sélectionnez **Next**.
6. Dans votre portail BrazeAI Decisioning Studio™ Go, localisez la requête SQL des données système sous **Engagement Query Resources**.
7. Copiez et collez la requête dans la zone de texte, puis sélectionnez **Next**.

![Exemple de requête dans la section SQL Query.]({% image_buster /assets/img/decisioning_studio_go/query5.png %})

{: start="8"}
8. Localisez et sélectionnez l'extension de données cible pour la requête d'engagement spécifiée dans votre portail BrazeAI Decisioning Studio™ Go.

{% alert tip %}
Le nom de l'extension de données cible est également fourni dans votre portail BrazeAI Decisioning Studio™ Go pour référence croisée. Assurez-vous de bien consulter l'extension de données cible pour la requête d'engagement. La **Data Extension** pour la requête d'engagement doit se terminer par le suffixe ENGAGEMENT_DATA.
{% endalert %}

{: start="9"}
9. Sélectionnez **Overwrite**, puis **Next**.

![Nom de l'extension de données correspondant à la clé externe de l'exemple.]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

#### Étape 3 : Exécuter l'automatisation {#step-3-run-the-automation}

1. Attribuez un nom à l'automatisation et sélectionnez **Save**.

![Exemple d'automatisation « OFE_Experimenter_Test5_Automation ».]({% image_buster /assets/img/decisioning_studio_go/query3.png %})

{: start="2"}
2. Ensuite, sélectionnez **Run Once** pour vérifier que tout fonctionne correctement.
3. Sélectionnez les deux requêtes et cliquez sur **Run**.

![Une automatisation « OFE_Experimenter_Test5_Automation » avec une liste d'activités de requêtes SQL sélectionnées à exécuter.]({% image_buster /assets/img/decisioning_studio_go/query2.png %})

{: start="4"}
4. Sélectionnez **Run Now**.

![Une activité de requête SQL sélectionnée.]({% image_buster /assets/img/decisioning_studio_go/query1.png %})

Vous pouvez maintenant vérifier que l'automatisation fonctionne correctement. Contactez l'assistance Braze pour obtenir de l'aide si votre automatisation ne fonctionne pas comme prévu.

### Partie 3 : Créer votre parcours SFMC {#part-3-create-your-sfmc-journey}

#### Étape 1 : Configurer le parcours {#step-1-set-up-the-journey}

1. Dans Salesforce Marketing Cloud, accédez à **Journey Builder** > **Journey Builder**.
2. Sélectionnez **Create New Journey**.
3. Pour le type de parcours, sélectionnez **Multi-Step Journey**, puis **Create**.

![Une source d'entrée API Event connectée à un nœud Decision Split et à plusieurs nœuds Email.]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

#### Étape 2 : Construire le parcours {#step-2-build-the-journey}

**Créer une source d'entrée :**

1. Pour votre source d'entrée, glissez **API Event** vers le Journey Builder.

![« API Event » sélectionné comme source d'entrée.]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

{: start="2"}
2. Dans l'**API Event**, sélectionnez **Create an event**.

![L'option « create an event » dans l'API Event.]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3. Sélectionnez **Select Data Extension**. Localisez et sélectionnez l'extension de données dans laquelle BrazeAI Decisioning Studio™ Go écrira les recommandations.
4. Sélectionnez **Summary** pour enregistrer vos modifications.
5. Sélectionnez **Done** pour enregistrer l'événement API.

![Résumé de l'événement API.]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

**Ajouter un arbre décisionnel :**

1. Glissez-déposez un **Decision Split** après l'**API Entry Event**.
2. Dans les détails du **Decision Split**, sélectionnez **Edit** pour le premier chemin.

![Détails de l'arbre décisionnel avec le bouton « Edit ».]({% image_buster /assets/img/decisioning_studio_go/journey5.png %})

{: start="3"}
3. Mettez à jour le **Decision Split** pour utiliser l'ID de modèle transmis par l'extension de données de recommandations. Localisez le champ approprié sous **Journey Data**.

![La section Journey Data dans le chemin 1 de l'arbre décisionnel.]({% image_buster /assets/img/decisioning_studio_go/journey6.png %})

{: start="4"}
4. Sélectionnez votre événement d'entrée et localisez le champ d'ID de modèle souhaité, puis glissez-le dans l'espace de travail.

![L'ID du modèle d'e-mail à inclure.]({% image_buster /assets/img/decisioning_studio_go/journey7.png %})

{: start="5"}
5. Saisissez l'ID de votre premier modèle d'e-mail, puis sélectionnez **Done**.
6. Sélectionnez **Summary** pour enregistrer ce chemin.
7. Ajoutez un chemin pour chacun de vos modèles d'e-mail, puis répétez les étapes 4 à 6 ci-dessus pour définir les critères de filtrage afin que l'ID de modèle corresponde à la valeur ID de chaque modèle.
8. Sélectionnez **Done** pour enregistrer le nœud **Decision Split**.

![Deux chemins dans un arbre décisionnel pour chaque ID de modèle d'e-mail.]({% image_buster /assets/img/decisioning_studio_go/journey10.png %}){: style="max-width:65%;"}

**Ajouter un e-mail pour chaque arbre décisionnel :**

1. Glissez un nœud **Email** dans chaque chemin du **Decision Split**.
2. Sélectionnez **Email**, puis choisissez le modèle approprié pour chaque chemin (c'est-à-dire que la valeur d'ID du modèle doit correspondre à la logique de votre arbre décisionnel).

![Un nœud Email ajouté au parcours.]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

#### Étape 3 : Activer le parcours {#step-3-activate-the-journey}

Après avoir configuré votre parcours, activez-le et partagez les informations suivantes avec l'équipe BrazeAI Decisioning Studio™ Go :

* ID du parcours
* Nom du parcours
* Clé de définition de l'événement API
* Clé externe de l'extension de données de recommandations

{% alert note %}
Le portail BrazeAI Decisioning Studio™ Go vous montre l'automatisation SFMC qu'il a provisionnée pour exporter les données des utilisateurs abonnés et d'engagement une fois par jour. Si vous ouvrez cette automatisation dans SFMC, assurez-vous de la réactiver et de la remettre en production.
{% endalert %}

1. Dans le portail BrazeAI Decisioning Studio™ Go, copiez le **nom du parcours**.
2. Ensuite, dans Salesforce Marketing Cloud Journey Builder, collez le nom du parcours dans la barre de recherche.
3. Sélectionnez le nom du parcours. Notez que le parcours est actuellement à l'état de brouillon.
4. Sélectionnez **Validate**.

![Le parcours terminé prêt à être activé.]({% image_buster /assets/img/decisioning_studio_go/activate3.png %})

{: start="5"}
5. Examinez les résultats de la validation et sélectionnez **Activate**.

![Recommandations listées dans la section Validation Rules.]({% image_buster /assets/img/decisioning_studio_go/activate1.png %}){: style="max-width:60%;"}

{: start="6"}
6. Dans le résumé **Activate Journey**, sélectionnez à nouveau **Activate**.

![Résumé du parcours.]({% image_buster /assets/img/decisioning_studio_go/activate2.png %}){: style="max-width:85%;"}

C'est terminé ! Vous pouvez maintenant commencer à déclencher des envois via BrazeAI Decisioning Studio™ Go.

{% endtab %}
{% endtabs %}

## Étapes suivantes {#next-steps}

Maintenant que vous avez configuré l'orchestration, passez à la conception de votre agent :

- [Concevoir votre agent]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent)