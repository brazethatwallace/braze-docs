---
nav_title: Enquêtes
article_title: Enquêtes Braze
description: "Découvrez comment créer des enquêtes dans les messages in-app et les pages d'accueil, consulter les réponses et recibler les utilisateurs pendant la bêta fermée."
permalink: /braze_surveys/
hidden: true
---

# Enquêtes Braze {#braze-surveys}

> Les enquêtes Braze recueillent des retours dans les messages in-app et les pages d'accueil que vous pouvez analyser et utiliser dans vos messages de suivi.

{% alert important %}
Les enquêtes Braze sont en bêta fermée. Envoyez vos commentaires sur la bêta à [surveys-feedback@braze.com](mailto:surveys-feedback@braze.com).
{% endalert %}

## Conditions préalables {#prerequisites}

Avant de créer une enquête, vous devez :

- Avoir accès aux pages d'accueil, aux messages in-app, ou aux deux dans votre espace de travail Braze
- Être familiarisé avec la [création de pages d'accueil](https://braze.com/docs/user_guide/engagement_tools/landing_pages/creating_pages/)
- Être familiarisé avec la [création de messages in-app par glisser-déposer](https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/)

## Créer une enquête {#create-a-survey}

Pendant la bêta, les enquêtes sont créées dans votre flux de composition de messages existant.

1. Accédez à **Messaging** > **Landing Pages**, ou créez un [message in-app](https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/) dans une campagne ou un Canvas.
2. Créez un nouveau message.
3. Sélectionnez **Survey** comme type de message.

## Composer une enquête par message in-app {#compose-an-in-app-message-survey}

Les enquêtes par message in-app contiennent deux pages par défaut :

- **Page 1**, où les utilisateurs répondent aux questions
- **Page de confirmation**, où l'enquête est soumise

Par défaut, les boutons sont liés à **Next page**. Pour modifier ce comportement, mettez à jour chaque bouton dans le panneau **Actions**.

![Flux de pages d'une enquête par message in-app et paramètres d'action.]({% image_buster /assets/unlisted_docs/img/surveys/iam-survey-nav.png %}){: style="max-width:40%;"}

## Utiliser les blocs de formulaire d'enquête {#use-survey-form-blocks}

Pour les contrôles de style et de composition partagés, consultez :

- [Blocs éditeur du message in-app par glisser-déposer](https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/)
- [Blocs de formulaire des pages d'accueil](https://braze.com/docs/user_guide/engagement_tools/landing_pages/creating_pages/#form-blocks)

Vous pouvez ajouter les blocs de formulaire suivants aux enquêtes :

- Capture de numéro de téléphone
- Capture d'e-mail
- Groupe de boutons radio
- Capture de texte court
- Capture de texte long
- Liste déroulante
- Case à cocher unique
- Groupe de cases à cocher

### Capture de texte long {#long-text-capture}

La capture de texte long est utile pour les retours qualitatifs.

Vous pouvez configurer :

- Le nombre minimum et maximum de caractères (jusqu'à 1 000)
- L'affichage ou non des limites de caractères pendant la composition
- La hauteur de la zone de texte (lignes)
- Le texte de la marque substitutive

Pendant la bêta, les réponses en texte long sont disponibles dans les rapports et les exports, mais elles ne peuvent pas être enregistrées en tant qu'attributs personnalisés du profil utilisateur.

![Paramètres du bloc de capture de texte long.]({% image_buster /assets/unlisted_docs/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

## Configurer les champs requis et les attributs {#configure-required-fields-and-attributes}

Pour chaque bloc de formulaire, saisissez un **identifiant pour le reporting** dans le panneau de paramètres situé à droite. Cet identifiant apparaît dans les rapports d'enquête et les exports CSV.

Pendant la bêta :

- Vous pouvez enregistrer la plupart des réponses d'enquête en tant qu'attributs personnalisés du profil utilisateur.
- Les réponses en texte long ne peuvent pas être enregistrées en tant qu'attributs personnalisés.
- Si vous choisissez de ne pas enregistrer une réponse en tant qu'attribut utilisateur, vous ne pourrez pas segmenter les utilisateurs en fonction de la valeur de cette réponse.

![Paramètres de l'identifiant pour le reporting et de l'enregistrement des attributs.]({% image_buster /assets/unlisted_docs/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## Consulter les rapports et les analyses {#view-reporting-and-analytics}

Après le lancement, consultez les résultats dans :

- L'onglet **Responses** pour les enquêtes par message in-app
- La vue analytique de la page d'accueil pour les enquêtes sur les pages d'accueil

![Onglet d'analyse de la page d'accueil.]({% image_buster /assets/unlisted_docs/img/surveys/survey-analytics-1.png %})

Les analyses de haut niveau comprennent :

- **All responses :** total des réponses complètes et incomplètes
- **Completed :** utilisateurs ayant répondu à toutes les questions requises
- **Partially complete :** utilisateurs ayant soumis certaines données, mais n'ayant pas répondu à toutes les questions requises
- **Unique impressions :** nombre total de vues de la page

{% alert note %}
Les enquêtes sur les pages d'accueil ne suivent pas les réponses partiellement complètes pendant la bêta.
{% endalert %}

Vous pouvez également consulter les répartitions des réponses par question et exporter les données au format CSV.

![Aperçu des analyses d'enquête et répartition par question.]({% image_buster /assets/unlisted_docs/img/surveys/survey-analytics-text.png %})

![Graphiques en barres de la répartition par question de l'enquête.]({% image_buster /assets/unlisted_docs/img/surveys/bar-charts-1.png %})

## Recibler et déclencher {#retarget-and-trigger}

Pendant la bêta, vous pouvez :

- Segmenter les utilisateurs en fonction des réponses d'enquête enregistrées en tant qu'attributs utilisateur.
- Segmenter les utilisateurs en fonction de l'état de complétion de l'enquête. <br><br>![Configuration du déclencheur et filtres de segmentation pour le suivi d'enquête.]({% image_buster /assets/unlisted_docs/img/surveys/submit-survey-segment.png %})<br><br>
- Déclencher des campagnes et des Canvas lorsqu'un utilisateur complète une enquête dans une page d'accueil ou une campagne de message in-app. <br><br>![Configuration du déclencheur et filtre de segmentation pour le suivi d'enquête sur page d'accueil.]({% image_buster /assets/unlisted_docs/img/surveys/trigger_landing_page_survey.png %}) <br><br>![Configuration du déclencheur et filtre de segmentation pour le suivi d'enquête de campagne de message in-app.]({% image_buster /assets/unlisted_docs/img/surveys/interact-campaign-step.png %})

### Limitations

Pendant la bêta, les restrictions suivantes s'appliquent :

- Vous ne pouvez pas segmenter les utilisateurs en fonction des réponses en texte long.
- Le déclenchement par question-réponse qui ne repose pas sur des attributs utilisateur enregistrés n'est pas disponible.