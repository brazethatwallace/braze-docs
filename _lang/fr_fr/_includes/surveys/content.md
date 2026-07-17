{% comment %}
  Documentation partagée sur les enquêtes Braze.
  Paramètres :
  - channel (requis) : "in_app_message" ou "landing_page"
{% endcomment %}

{% multi_lang_include alerts/early_access_beta_alert.md feature='Braze surveys' %}

## Conditions préalables {#prerequisites}

Avant de créer une enquête, vous devez :

{% if include.channel == 'in_app_message' %}
- Avoir accès aux messages in-app dans votre espace de travail Braze
- Être familiarisé avec la [création de messages in-app dans l'éditeur par glisser-déposer]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)
{% elsif include.channel == 'landing_page' %}
- Avoir accès aux pages de destination dans votre espace de travail Braze
- Être familiarisé avec la [création de pages de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)
{% else %}
- Avoir accès aux pages de destination, aux messages in-app, ou aux deux dans votre espace de travail Braze
- Être familiarisé avec la [création de pages de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages) et la [création de messages in-app dans l'éditeur par glisser-déposer]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)
{% endif %}

## Créer une enquête {#create-a-survey}

Pendant l'accès anticipé, les enquêtes sont créées dans votre flux de composition de messages existant.

{% if include.channel == 'in_app_message' %}
1. Créez un [message in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) dans une Campaign ou un Canvas.
2. Sélectionnez **Survey** comme type de message.
{% elsif include.channel == 'landing_page' %}
1. Accédez à **Messaging** > **Landing Pages**.
2. Créez une nouvelle page de destination.
3. Sélectionnez **Survey** comme type de message.
{% else %}
1. Accédez à **Messaging** > **Landing Pages**, ou créez un [message in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) dans une Campaign ou un Canvas.
2. Créez un nouveau message.
3. Sélectionnez **Survey** comme type de message.
{% endif %}

{% if include.channel == 'in_app_message' %}

## Composer une enquête par message in-app {#compose-an-in-app-message-survey}

Les enquêtes par message in-app contiennent deux pages par défaut :

- **Page 1**, où les utilisateurs répondent aux questions
- **Page de confirmation**, où l'enquête est soumise

Par défaut, les boutons sont liés à **Next page**. Pour modifier ce comportement, mettez à jour chaque bouton dans le panneau **Actions**.

![Flux de pages d'une enquête par message in-app et paramètres d'action.]({% image_buster /assets/img/surveys/iam-survey-nav.png %}){: style="max-width:40%;"}

{% endif %}

## Utiliser les blocs de formulaire d'enquête {#use-survey-form-blocks}

Pour les contrôles de style et de composition partagés, consultez :

{% if include.channel == 'in_app_message' %}
- [Blocs de l'éditeur par glisser-déposer pour les messages in-app]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
{% elsif include.channel == 'landing_page' %}
- [Blocs de formulaire pour les pages de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)
{% else %}
- [Blocs de l'éditeur par glisser-déposer pour les messages in-app]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
- [Blocs de formulaire pour les pages de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)
{% endif %}

Vous pouvez ajouter les blocs de formulaire suivants aux enquêtes :

- Capture de numéro de téléphone
- Capture d'e-mail
- Groupe de boutons radio
- Capture de texte court
- Capture de texte long
- Menu déroulant
- Case à cocher unique
- Groupe de cases à cocher

### Randomiser les choix de réponse {#randomize-answer-choices}

Les blocs de groupe de boutons radio, de groupe de cases à cocher et de menu déroulant prennent en charge la randomisation des choix de réponse. Activez **Randomize choice order** pour mélanger les choix à chaque chargement de l'enquête. Utilisez ce paramètre pour réduire le biais d'ordre lorsque la même première option pourrait fausser les réponses.

La randomisation ne modifie que l'ordre d'affichage pour chaque répondant. Les libellés et valeurs de reporting restent associés aux choix que vous avez configurés, de sorte que les analyses, les exports CSV et la segmentation utilisent les mêmes données de réponse.

### Capture de texte long {#long-text-capture}

La capture de texte long est utile pour recueillir des retours qualitatifs.

Vous pouvez configurer :

- Le nombre minimum et maximum de caractères (jusqu'à 1 000)
- L'affichage ou non des limites de caractères pendant la composition
- La hauteur de la zone de texte (lignes)
- Le texte de marque substitutive

Pendant l'accès anticipé, les réponses en texte long sont disponibles dans les rapports et les exports, mais elles ne peuvent pas être enregistrées comme attributs personnalisés du profil utilisateur.

![Paramètres du bloc de capture de texte long.]({% image_buster /assets/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

## Configurer les champs requis et les attributs {#configure-required-fields-and-attributes}

Pour chaque bloc de formulaire, saisissez un **identifiant pour le reporting** dans le panneau de paramètres à droite. Cet identifiant apparaît dans les rapports d'enquête et les exports CSV.

Pendant l'accès anticipé :

- Vous pouvez enregistrer la plupart des réponses d'enquête comme attributs personnalisés du profil utilisateur.
- Les réponses en texte long ne peuvent pas être enregistrées comme attributs personnalisés.
- Si vous choisissez de ne pas enregistrer une réponse comme attribut utilisateur, vous ne pourrez pas segmenter les utilisateurs en fonction de cette valeur de réponse.

![Paramètres de l'identifiant pour le reporting et de l'enregistrement des attributs.]({% image_buster /assets/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## Consulter les rapports et les analyses {#view-reporting-and-analytics}

Après le lancement, consultez les résultats dans :

{% if include.channel == 'in_app_message' %}
- L'onglet **Responses** pour les enquêtes par message in-app
{% elsif include.channel == 'landing_page' %}
- La vue analytique de la page de destination pour les enquêtes sur les pages de destination
{% else %}
- L'onglet **Responses** pour les enquêtes par message in-app
- La vue analytique de la page de destination pour les enquêtes sur les pages de destination
{% endif %}

Les analyses de haut niveau incluent :

- **All responses :** total des réponses complètes et incomplètes
- **Completed :** utilisateurs ayant répondu à toutes les questions requises
- **Partially complete :** utilisateurs ayant soumis certaines données, mais n'ayant pas répondu à toutes les questions requises
- **Unique impressions :** total des vues de page

{% if include.channel == 'landing_page' %}
{% alert note %}
Les enquêtes sur les pages de destination ne suivent pas les réponses partiellement complètes pendant l'accès anticipé.
{% endalert %}
{% endif %}

Vous pouvez également consulter les ventilations de réponses par question et exporter les données au format CSV.

### Choisir un type de graphique {#choose-a-chart-type}

Pour les blocs de formulaire à boutons radio, menus déroulants et cases à cocher, vous pouvez choisir parmi trois types de graphiques dans la vue analytique de l'enquête. Cela vous offre plus de flexibilité pour interpréter et partager des informations sans avoir à exporter vers un outil tiers.

| Type de graphique | Idéal pour |
| --- | --- |
| Graphique à barres | La vue horizontale par défaut des nombres et pourcentages de réponses. |
| Graphique en colonnes | Une vue verticale des nombres et pourcentages de réponses. Utilisez ce graphique pour comparer les réponses côte à côte, en particulier pour les questions à sélection multiple ou les questions avec davantage d'options de réponse. |
| Graphique circulaire | Une répartition proportionnelle des réponses. Utilisez ce graphique pour les questions à sélection unique lorsque vous souhaitez voir comment les réponses se répartissent entre les options. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Types de graphiques d'enquête" }

Chaque graphique se met à jour en temps réel à mesure que les réponses arrivent. Vous pouvez changer de type de graphique à tout moment sans affecter les données sous-jacentes.

![Ventilation par question de l'enquête avec un graphique à barres.]({% image_buster /assets/img/surveys/bar-charts-1.png %})

## Recibler et déclencher {#retarget-and-trigger}

Pendant l'accès anticipé, vous pouvez :

- Segmenter les utilisateurs par réponses d'enquête enregistrées comme attributs utilisateur.
- Segmenter les utilisateurs par statut de complétion de l'enquête.

{% if include.channel == 'in_app_message' %}

![Configuration du déclencheur et filtres de segmentation pour le suivi d'enquête.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Déclencher des Campaigns et des Canvas lorsqu'un utilisateur complète une enquête dans une Campaign de message in-app.

![Configuration du déclencheur et filtre de segmentation pour le suivi d'enquête par Campaign de message in-app.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% elsif include.channel == 'landing_page' %}

![Configuration du déclencheur et filtre de segmentation pour le suivi d'enquête sur page de destination.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

- Déclencher des Campaigns et des Canvas lorsqu'un utilisateur complète une enquête sur une page de destination.

{% else %}

![Configuration du déclencheur et filtres de segmentation pour le suivi d'enquête.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Déclencher des Campaigns et des Canvas lorsqu'un utilisateur complète une enquête sur une page de destination ou dans une Campaign de message in-app.

![Configuration du déclencheur et filtre de segmentation pour le suivi d'enquête sur page de destination.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

![Configuration du déclencheur et filtre de segmentation pour le suivi d'enquête par Campaign de message in-app.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% endif %}

### Limitations

Pendant l'accès anticipé, les restrictions suivantes s'appliquent :

- Vous ne pouvez pas segmenter les utilisateurs par réponses en texte long.
- Le déclenchement par question-réponse qui ne repose pas sur des attributs utilisateur enregistrés n'est pas disponible.