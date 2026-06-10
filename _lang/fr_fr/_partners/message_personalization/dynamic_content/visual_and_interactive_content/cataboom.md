---
nav_title: CataBoom
article_title: CataBoom
description: "Découvrez comment connecter les expériences gamifiées de CataBoom à Braze en utilisant Catapult, l'API Request Unique URL et le Contenu connecté."
alias: /partners/cataboom/
page_type: partner
search_tag: Partner
---

# CataBoom

> [CataBoom](https://www.cataboom.com/) est une plateforme de gamification. Les marques l'utilisent pour créer et lancer des expériences numériques interactives, notamment des jeux de type roue de la fortune, des quiz et des jeux à gain instantané. Ces expériences renforcent l'engagement et collectent des données first-party.

*Cette intégration est maintenue par CataBoom.*

## À propos de cette intégration {#about-this-integration}

Utilisez l'intégration Braze et CataBoom pour ajouter des liens de jeu personnalisés à vos messages. Vous pouvez transmettre des identifiants et des attributs utilisateur entre les campagnes Catapult et Braze en temps réel. Vous pouvez ensuite alimenter des Campaigns personnalisées, des déclencheurs et des parcours de suivi avec ces données.

## Conditions préalables {#prerequisites}

Avant de commencer, vous avez besoin des éléments suivants :

| Condition préalable | Description |
| --- | --- |
| Compte Catapult | Un compte Catapult est requis pour utiliser cette intégration. |
| Clé API REST Braze (facultatif) | Si vous utilisez les webhooks Catapult, vous avez besoin d'une clé API REST Braze avec les autorisations de données utilisateur requises par votre cas d'utilisation. Créez la clé dans Braze sous **Paramètres** > **API et identifiants** > **Clés API**. |
| Endpoint REST Braze (facultatif) | Si vous utilisez les webhooks Catapult, utilisez l'URL de l'endpoint REST correspondant à l'URL Braze de [votre instance Braze]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Étape 1 : Créer votre expérience de jeu {#step-1-create-your-game-experience}

Créez votre expérience de jeu dans la plateforme Catapult. Les étapes suivantes montrent une configuration simple de roue de la fortune qui utilise l'API Request Unique URL sur la page **Link Configuration**. CataBoom propose plus de 200 options de jeu, notamment des mécaniques basées sur le hasard, des mécaniques basées sur l'habileté et des utilitaires tels que les cartes à tamponner et les jeux de collection. Vous pouvez suivre un flux similaire pour d'autres types de jeux. Pour plus d'informations sur CataBoom et Catapult, consultez [le site web de CataBoom](https://www.cataboom.com).

1. Créez la campagne.

Sélectionnez **New Campaign** en haut à droite. Saisissez un nom de campagne, choisissez un slug d'URL, puis sélectionnez votre catégorie de jeu et votre type de jeu.

![Formulaire New Campaign du tableau de bord CataBoom avec les champs nom de la campagne, URL, catégorie de jeu et type de jeu.]({% image_buster /assets/img/cataboom/new_campaign.png %})

{: start="2"}
2. Activez l'API Request Unique URL.

Dans le menu de gauche, sélectionnez **Link Configuration**.

Sur la page **Link Configuration**, activez **Request Unique URL API**. Cette option crée une URL système à système que vous pouvez utiliser ultérieurement dans Braze, par exemple dans une carte de contenu.

![Page Link Configuration de CataBoom avec l'API Request Unique URL activée et l'URL de l'API visible.]({% image_buster /assets/img/cataboom/link_configuration.png %})

{: start="3"}
3. Définissez le suivi des parties sur Account ID.

Dans le menu de gauche, sélectionnez **Play Control**.

Sur la page **Play Control**, sous **Play Tracking**, définissez **Play Count Tracked By** sur **Account ID Parameter**.

Vous pouvez transmettre un Account ID pour chaque joueur à des fins de suivi, de limites de parties, de webhooks et d'autres comportements spécifiques au joueur. D'autres systèmes appellent souvent l'Account ID « member ID », « player ID », « loyalty ID » ou un nom similaire.

![Page Play Control de CataBoom avec Play Count Tracked By défini sur Account ID Parameter.]({% image_buster /assets/img/cataboom/play_control.png %})

Vous avez maintenant suffisamment d'éléments configurés pour effectuer un test dans Braze. Les étapes facultatives ci-dessous complètent une configuration de jeu complète typique. Catapult propose également de nombreux autres paramètres que vous pouvez utiliser pour personnaliser le gameplay.

{: start="4"}
4. Ajoutez vos éléments créatifs (facultatif).

Dans le menu de gauche, sélectionnez **Creative**.

Téléversez vos ressources. Catapult prend en charge un contrôle complet de l'image de marque pour votre expérience de jeu.

![Page Creative de CataBoom avec les actions de téléchargement et de téléversement de graphiques et un aperçu du jeu.]({% image_buster /assets/img/cataboom/creative.png %})

{: start="5"}
5. Configurez les lots pour les jeux basés sur le hasard (facultatif).

Dans le menu de gauche, sélectionnez **Summary**.

Sur la page **Summary**, développez **Prize Options**.

Catapult prend en charge les lots programmés, les lots basés sur les probabilités, ou les deux. Pour les configurer, utilisez **Timed Prizes and Codes**, **Prize Control and Odds Setup**, ou les deux, selon vos besoins.

Les captures d'écran suivantes montrent les **Prize Options** sur le résumé de la campagne et une configuration simple de probabilités avec une probabilité de gain de 50 % au niveau 1.

![Page Summary de CataBoom avec la section Prize Options développée.]({% image_buster /assets/img/cataboom/prize_options_summary.png %})

![Page Odds de CataBoom avec les niveaux de lots, les pourcentages et les contrôles de niveau.]({% image_buster /assets/img/cataboom/prize_odds.png %})

## Étape 2 : Créer un message dans Braze {#step-2-create-a-message-in-braze}

Cet exemple montre comment créer une **carte de contenu** qui utilise l'URL Request Unique URL de la page **Link Configuration**.

1. Ajoutez du Contenu connecté pour l'URL de jeu.

Dans votre carte de contenu, ajoutez du texte et du contenu dynamique selon vos besoins. Encapsulez votre URL Request Unique URL CataBoom dans une balise de [Contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/). Ajoutez un paramètre de requête `AccountID` qui utilise une balise de personnalisation Braze correspondant à l'identifiant que vous utilisez dans Catapult. L'exemple utilise {% raw %}`{{${user_id}}}`{% endraw %}.

Remplacez l'URL de base et les paramètres de requête `username` et `password` par les valeurs de la page **Link Configuration** de votre campagne dans Catapult.

{% raw %}
```liquid
{% connected_content https://secure.cataboom.com/dplayurl/YOUR_CAMPAIGN_SLUG?username=YOUR_API_USERNAME&password=YOUR_API_PASSWORD&AccountID={{${user_id}}} :save result %}
```
{% endraw %}

Utilisez le `result` enregistré dans votre carte (par exemple, comme URL de lien ou dans le corps du message). Suivez le format de réponse de l'API de CataBoom pour votre campagne. Pour plus d'informations sur les paramètres de requête et Liquid dans les URL, consultez [Effectuer un appel API]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/).

![Compositeur de carte de contenu Braze montrant du Contenu connecté dans le champ de message et un aperçu mobile de la carte.]({% image_buster /assets/img/cataboom/braze_content_card.png %})

Le Contenu connecté demande un lien de jeu unique lorsque l'utilisateur ouvre la carte de contenu. Vous pouvez ajouter d'autres paramètres de requête pour des expériences plus personnalisées.