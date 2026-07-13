---
nav_title: Survicate
article_title: Survicate
description: "Cet article de référence présente le partenariat entre Braze et Survicate, une plateforme de feedback client qui vous aide à collecter, analyser et agir sur les informations clients sur plusieurs canaux et tout au long du parcours utilisateur."
alias: /partners/survicate/
page_type: partner
search_tag: Partner

---

# Survicate

> [Survicate](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter) est une plateforme de feedback client qui recueille, analyse et exploite les informations clients à travers plusieurs canaux et tout au long du parcours utilisateur. [Regardez une démonstration rapide](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter)

_Cette intégration est maintenue par Survicate._

## À propos de l'intégration {#about-the-integration}

Utilisez l'intégration native de Survicate et Braze pour synchroniser les réponses aux enquêtes par e-mail, in-app, sur mobile ou sur le web avec les profils des clients Braze. Les réponses aux enquêtes se synchronisent automatiquement avec les profils utilisateurs Braze sous forme d'attributs personnalisés ou d'événements. Les informations de feedback en temps réel facilitent le suivi et l'analyse des commentaires parallèlement aux données clients, et permettent de créer des suivis ciblés et des segments hyper-personnalisés.

## Cas d'usage {#use-cases}

Braze et Survicate fonctionnent ensemble pour couvrir un large éventail de cas d'usage liés au feedback, vous aidant à collecter des informations exploitables sur les utilisateurs et à améliorer l'expérience client :

- Améliorez les taux de réponse aux enquêtes grâce à des enquêtes intégrées auxquelles il est possible de répondre directement depuis une boîte de réception e-mail.
- Recueillez des informations aux étapes critiques du parcours client via les In-App Messages de Braze.
- Utilisez le feedback stocké dans Survicate pour créer des segments plus intelligents dans Braze.
- Automatisez les Campaigns de suivi en fonction des commentaires des clients.
- Utilisez les informations clients pour déclencher des flux de travail personnalisés.
- Touchez une audience plus large grâce à des enquêtes traduites automatiquement.
- Envoyez des événements aux profils de contact Braze lorsque quelqu'un répond à votre enquête.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Survicate | Vous devez disposer d'un compte Survicate pour activer cette intégration. |
| Clé API REST Braze | Une clé API REST Braze avec la permission `users.track`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **API et identifiants**. |
| Endpoint REST Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Principales fonctionnalités de l'intégration {#key-features-of-the-integration}

L'intégration de Survicate et Braze offre une synchronisation des données en temps réel, de sorte que les informations les plus récentes des enquêtes Survicate sont immédiatement disponibles dans Braze. En fonction des réponses à l'enquête, vous pouvez utiliser ces données pour prendre des mesures personnalisées en temps voulu.

- **Envoyez les réponses à l'enquête à Braze sous forme d'attributs personnalisés** : enrichissez les profils utilisateurs Braze avec des données issues des réponses aux enquêtes.
- **Déclenchez des événements personnalisés dans Braze** : utilisez les événements basés sur les réponses à l'enquête pour cibler des groupes spécifiques ou lancer des Campaigns de suivi.
- **Créez des segments détaillés** : créez des segments Braze en utilisant les données des enquêtes Survicate pour personnaliser davantage vos actions.

## Intégration {#integration}

### Créer vos enquêtes dans Survicate {#creating-your-surveys-in-survicate}

#### Intégrer votre enquête dans un e-mail ou créer un lien d'enquête partageable {#embed-your-survey-in-an-email-or-create-a-shareable-link-survey}

1.  Dans Survicate, cliquez sur **+ Create new survey**, sélectionnez n'importe quelle méthode de création (un modèle, la création d'enquête par IA ou l'ajout de vos propres questions), puis le type d'enquête par e-mail ou par lien partageable :
![Braze est sélectionné dans le créateur d'enquête.]({% image_buster /assets/img/survicate/survicate_1.gif %})

{: start="2"}
2. Dans l'onglet Configure de l'enquête, sélectionnez **Braze** comme outil d'identification des répondants :
![Braze est sélectionné dans l'onglet Configure de l'enquête.]({% image_buster /assets/img/survicate/survicate_2.png %})

{: start="3"}
3. Après avoir configuré votre enquête, rendez-vous dans l'onglet Share et décidez de la manière d'envoyer votre enquête par e-mail. Deux options s'offrent à vous : vous pouvez envoyer votre **enquête sous forme de lien** ou **intégrer la première question dans l'e-mail** afin que les répondants commencent à répondre directement depuis l'e-mail.

{% details Survey link option %}

1. Récupérez un lien vers votre enquête à l'aide du bouton Copy survey link :

![Récupérez un lien vers votre enquête à l'aide du bouton Copy survey link.]({% image_buster /assets/img/survicate/survicate_3.png %})

{: start="2"}
2. Masquez le lien de l'enquête derrière un bouton CTA ou un lien hypertexte dans votre e-mail Braze.

![Masquez le lien de l'enquête derrière un bouton CTA ou un lien hypertexte dans votre e-mail Braze.]({% image_buster /assets/img/survicate/survicate_4.png %})

{% enddetails %}

{% details Email embed option %}

Affichez la première question directement dans le corps de l'e-mail pour lancer l'enquête depuis l'e-mail. Les répondants sont ensuite redirigés vers une page de destination pour répondre au reste de l'enquête.

1. Cliquez sur **Get email code**, puis sur **Copy the HTML code** :

![Obtenir le code e-mail]({% image_buster /assets/img/survicate/survicate_5.gif %})

{: start="2"}
2. Accédez à la Campaign Braze que vous souhaitez utiliser pour l'enquête, cliquez sur **Edit email body** et ajoutez un bloc HTML à votre modèle :

![Obtenir le code du bloc HTML]({% image_buster /assets/img/survicate/survicate_6.png %})

{: start="3"}
3. Remplacez le code par celui que vous avez copié depuis votre enquête Survicate. La première question de l'enquête apparaît alors dans le modèle :

![Remplacez le code par celui que vous avez copié depuis votre enquête Survicate.]({% image_buster /assets/img/survicate/survicate_7.png %})

{: start="4"}
4. Planifiez l'e-mail, choisissez votre groupe cible et votre Campaign est prête à être envoyée.

{% enddetails %}

### Enquête In-App Message de Braze {#braze-in-app-message-survey}

1. Cliquez sur **+ Create new survey**, sélectionnez n'importe quelle méthode de création (un modèle, la création d'enquête par IA ou l'ajout de vos propres questions), puis choisissez les enquêtes In-platform et le type d'enquête Braze In-App Message :

![Cliquez sur + Create new survey, sélectionnez la méthode de création de votre choix.]({% image_buster /assets/img/survicate/survicate_8.gif %})

{: start="2"}
2. Lancez votre enquête In-App Message de Braze en accédant à votre compte Braze, puis à **Messaging > Campaigns > Create campaign > In-app message** :
![Lancez votre enquête In-App Message de Braze.]({% image_buster /assets/img/survicate/survicate_9.gif %})

### Lancer votre enquête Braze In-App Messenger via l'éditeur traditionnel {#launch-your-braze-in-app-messenger-survey-via-the-traditional-editor}

1. Si vous utilisez l'éditeur traditionnel, dans le type de message, choisissez **Custom code** :

![Choisissez Custom code.]({% image_buster /assets/img/survicate/survicate_10.gif %})

{: start="2"}
2. Collez ensuite le code de l'onglet Launch de votre enquête dans le champ HTML :

![Collez le code de l'onglet Launch de votre enquête dans le champ HTML.]({% image_buster /assets/img/survicate/survicate_11.gif %})

{% alert note %}
Braze affiche par défaut les messages in-app dans une iframe tandis que l'arrière-plan de l'application est bloqué. Pour permettre l'interaction avec votre application lorsque les enquêtes Survicate apparaissent, vous devez :<br><br>

- Ajouter `opts.useBrazeIframeClipper = true` à votre extrait de code Survicate-Braze.
- Installer le [package](https://www.npmjs.com/package/@survicate/braze-bridge-npm) `@survicate/braze-bridge-npm` dans le fichier où vous initialisez Braze et utiliser la fonction `initBrazeBridge`.

Vous trouverez un extrait de code et une implémentation React [sur le site des développeurs de Survicate](https://developers.survicate.com/javascript/installation/#braze).
{% endalert %}

{: start="3"}
3. Dans votre Campaign Braze, configurez les étapes Target et Assign. Une fois terminé, votre Campaign est prête à être lancée. À l'étape Review, vous pouvez voir à quoi ressemble la Campaign. L'enquête apparaît sur votre site web à l'endroit spécifié dans le panneau Survicate, comme décrit à l'étape 1.

### Activer l'intégration Braze {#enabling-the-braze-integration}

1. Pour activer l'intégration Braze, accédez à **Integrations**, puis recherchez et sélectionnez « Braze ».

![Sélectionnez Braze.]({% image_buster /assets/img/survicate/survicate_12.gif %})

{: start="2"}
2. Cliquez sur **Connect** pour configurer l'autorisation.

3. Insérez la clé API de l'espace de travail de votre compte Braze et l'URL de l'instance Braze :

![Insérez la clé API de l'espace de travail de votre compte Braze et l'URL de l'instance Braze.]({% image_buster /assets/img/survicate/survicate_13.png %})

{% alert important %}
Pour connecter Survicate à Braze, la clé API Braze doit disposer des permissions `users.track`.
{% endalert %}

### Connecter vos enquêtes à Braze {#connecting-your-surveys-to-braze}

Maintenant que l'intégration Braze est connectée, vous pouvez définir des paramètres individuels pour chaque enquête. Accédez à votre enquête, sélectionnez l'onglet **Connect** et choisissez **Braze** dans la liste des intégrations disponibles.

![Accédez à votre enquête, sélectionnez l'onglet Connect et choisissez Braze.]({% image_buster /assets/img/survicate/survicate_14.png %})

### Envoyer les réponses à Braze sous forme d'attributs personnalisés {#sending-responses-to-braze-as-custom-attributes}

Configurez les réponses à l'enquête pour qu'elles soient transmises à Braze en tant qu'attributs personnalisés, ce qui enrichit vos profils utilisateurs Braze avec les données collectées.

1. Dans l'onglet Settings de l'intégration Braze, repérez la section **Update fields**.

![Sélectionnez la section Update fields.]({% image_buster /assets/img/survicate/survicate_15.png %})

{: start="2"}
2. Sélectionnez la question pour laquelle vous souhaitez mettre à jour les champs. Pour éviter de surcharger les profils utilisateurs Braze avec des données, vous pouvez envoyer les réponses uniquement pour certaines questions.

![Sélectionnez la question pour laquelle vous souhaitez mettre à jour les champs.]({% image_buster /assets/img/survicate/survicate_16.png %})

{% alert note %}
Les questions de classement et de matrice ne sont pas prises en charge par cette intégration Braze.
{% endalert %}

{: start="3"}
3. Ajoutez le nom de l'attribut personnalisé que vous souhaitez mettre à jour sous le champ **User** :

![Ajoutez le nom de l'attribut personnalisé que vous souhaitez mettre à jour sous le champ User.]({% image_buster /assets/img/survicate/survicate_17.png %})

Par défaut, Survicate envoie le contenu d'une réponse à l'enquête en tant que valeur d'attribut. Vous pouvez modifier l'étiquette pour la rendre plus courte ou l'adapter à la structure de vos données en cliquant sur **Edit mapping** :

![Réponse à l'enquête en tant que valeur d'attribut.]({% image_buster /assets/img/survicate/survicate_18.png %})

![Cliquez sur Edit mapping pour modifier ces valeurs.]({% image_buster /assets/img/survicate/survicate_19.png %})

{% alert note %}
Pour le NPS, Survicate envoie des valeurs mappées en fonction du groupe de réponse à la question NPS®. Toutefois, si vous souhaitez recevoir des valeurs numériques, vous pouvez activer l'option Send Answers as 0-10 values.
{% endalert %}

![Survicate envoie des valeurs mappées en fonction du groupe de réponse.]({% image_buster /assets/img/survicate/survicate_20.png %})

{: start="4"}
4. Connectez d'autres questions à votre intégration en cliquant sur **+ Add new** et en appliquant les mêmes étapes.

![Connectez d'autres questions à votre intégration.]({% image_buster /assets/img/survicate/survicate_21.png %})

### Envoyer des événements aux profils des contacts Braze {#sending-events-to-braze-contacts-profiles}

Outre les paramètres précédents, chaque fois qu'un répondant répond à une question de l'enquête, Survicate peut envoyer un événement personnalisé dans Braze nommé `survicate-question-answered`.
Dans le panneau Survicate, sous Send responses as custom attributes, vous pouvez choisir d'envoyer l'événement pour toutes les questions, uniquement pour les questions sélectionnées dans l'onglet Update fields, ou pas du tout :

![Vous pouvez choisir d'envoyer l'événement pour toutes les questions.]({% image_buster /assets/img/survicate/survicate_22.png %})

Si vous choisissez d'envoyer les événements, vous pouvez voir dans les profils des utilisateurs combien de fois ils ont répondu aux enquêtes Survicate et quand ils ont répondu pour la dernière fois :

![Réponses.]({% image_buster /assets/img/survicate/survicate_23.png %})

L'événement contient des propriétés d'événement avec la réponse à la question et des informations sur l'enquête, la question et le répondant. Vous pouvez utiliser cet événement pour créer des segments. Par exemple, créez un segment d'utilisateurs qui ont répondu à une enquête après une date donnée ou un certain nombre de fois :

![L'événement contient des propriétés d'événement avec la réponse.]({% image_buster /assets/img/survicate/survicate_24.png %})

Vous pouvez également utiliser ces données lors de la création d'une Campaign dans Braze.

![Vous pouvez également utiliser ces données lors de la création d'une Campaign dans Braze.]({% image_buster /assets/img/survicate/survicate_25.png %})

### Tester l'intégration {#test-the-integration}

Lorsque votre enquête est prête et que l'intégration est configurée, vous pouvez la tester sans quitter Survicate en cliquant sur le bouton Test Integration à côté de n'importe quel attribut, étiquette ou configuration de nouveau contact que vous avez créé. Survicate crée un contact test (`braze-test@survicate.com`) dans votre compte Braze. Le profil du contact comprend des champs mis à jour conformément à la configuration.

![Cliquez sur le bouton Test Integration.]({% image_buster /assets/img/survicate/survicate_26.png %})

Dans Braze, vous voyez des exemples de données provenant des champs mappés dans le contact fictif Survicate :

![Exemples de données provenant des champs mappés dans le contact fictif Survicate.]({% image_buster /assets/img/survicate/survicate_27.png %})

### Analyser les résultats de votre enquête {#analyzing-your-survey-results}

Après avoir recueilli des réponses via votre enquête Braze, il est temps d'examiner le feedback et les informations que vos répondants ont partagés. Survicate vous permet de consulter facilement les résultats, les statistiques et les tendances afin de prendre des mesures supplémentaires.

### Le feedback dans Survicate {#feedback-in-survicate}

Dès que votre enquête commence à recueillir des réponses, vous les voyez immédiatement dans l'onglet Analyze de l'enquête.

![Réponses dans l'onglet Analyze.]({% image_buster /assets/img/survicate/survicate_28.png %})

L'onglet Analyze vous présente les résultats globaux avec des statistiques et des données dans le temps, ainsi que les réponses individuelles pour examiner en détail chaque soumission d'enquête.

### Le feedback dans Braze {#feedback-in-braze}

Si vous mettez à jour les champs utilisateur avec les réponses à l'enquête ou si vous envoyez les réponses en tant qu'événements personnalisés, vous pouvez voir les données de l'enquête synchronisées en temps réel. Dans Braze, accédez à un contact spécifique qui a répondu à votre enquête. Les données basées sur les réponses et les événements sont affichées dans la vue principale du contact.

![Données d'enquête synchronisées en temps réel.]({% image_buster /assets/img/survicate/survicate_29.png %})