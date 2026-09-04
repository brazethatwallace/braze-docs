{% comment %}
  Documentation partagée sur les enquêtes Braze.
  Paramètres :
  - channel (requis) : "in_app_message" ou "landing_page"
{% endcomment %}

Pour un aperçu des enquêtes et des fonctionnalités partagées entre les canaux, consultez [Enquêtes]({{site.baseurl}}/user_guide/messaging/surveys).

## Prérequis {#prerequisites}

Avant de créer un sondage, vous devez :

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

## Créer un sondage {#create-a-survey}

Les sondages sont créés au sein de votre flux de composition de messages existant.

{% if include.channel == 'in_app_message' %}
1. Créez un [message in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) dans une Campaign ou un Canvas.
2. Sélectionnez **Sondage** comme type de message.
{% elsif include.channel == 'landing_page' %}
1. Accédez à **Envoi de messages** > **Pages de destination**.
2. Créez une nouvelle page de destination.
3. Sélectionnez **Sondage** comme type de message.
{% else %}
1. Accédez à **Envoi de messages** > **Pages de destination**, ou créez un [message in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) dans une Campaign ou un Canvas.
2. Créez un nouveau message.
3. Sélectionnez **Sondage** comme type de message.
{% endif %}

{% if include.channel == 'in_app_message' %}

## Composer un sondage de message in-app {#compose-an-in-app-message-survey}

Les sondages de messages in-app contiennent deux pages par défaut :

- **Page 1**, où les utilisateurs répondent aux questions
- **Page de confirmation**, où le sondage est soumis

Par défaut, les boutons sont liés à **Page suivante**. Pour modifier ce comportement, mettez à jour chaque bouton dans le panneau **Actions**.

![Flux de pages du sondage de message in-app et paramètres d'action.]({% image_buster /assets/img/surveys/iam-survey-nav.png %}){: style="max-width:40%;"}

{% endif %}

## Utiliser les blocs de formulaire d'enquête {#use-survey-form-blocks}

Pour les contrôles partagés de style et de composition, consultez :

{% if include.channel == 'in_app_message' %}
- [Blocs éditeur du message in-app en glisser-déposer]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
{% elsif include.channel == 'landing_page' %}
- [Blocs de formulaire de page de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)
{% else %}
- [Blocs éditeur du message in-app en glisser-déposer]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
- [Blocs de formulaire de page de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)
{% endif %}

Vous pouvez ajouter les blocs de formulaire suivants aux enquêtes :

- Capture de numéro de téléphone
- Capture d'e-mail
- Groupe de boutons radio
- Capture de texte court
- Capture de texte long
- Liste déroulante
- Case à cocher unique
- Groupe de cases à cocher
- Échelle de notation
- NPS

### Ordre aléatoire des choix de réponse {#randomize-answer-choices}

Les blocs de groupe de boutons radio, de groupe de cases à cocher et de liste déroulante prennent en charge l'ordre aléatoire des choix de réponse. Activez **Randomize choice order** pour mélanger les choix à chaque chargement de l'enquête. Pour en savoir plus, consultez [Ordre aléatoire des choix]({{site.baseurl}}/user_guide/messaging/surveys#randomized-choice-order).

### Capture de texte long {#long-text-capture}

La capture de texte long est utile pour recueillir des retours qualitatifs, jusqu'à 1 000 caractères. Pour en savoir plus, consultez [Capture de texte long]({{site.baseurl}}/user_guide/messaging/surveys#long-form-text-capture).

### Échelle de notation {#rating-scale}

L'échelle de notation (aussi appelée question à échelle numérique) est utile pour capturer un sentiment, un niveau de satisfaction ou la probabilité de recommandation sous forme d'un seul nombre. Pour en savoir plus, consultez [Questions à échelle numérique]({{site.baseurl}}/user_guide/messaging/surveys#number-scale-questions).

{% if include.channel == 'in_app_message' %}
![Échelle de notation pour évaluer votre expérience en magasin de 1 à 5.]({% image_buster /assets/img/surveys/iam_rating_scale_example.png %}){: style="max-width:40%;"}
{% elsif include.channel == 'landing_page' %}
![Échelle de notation pour indiquer la probabilité de recommander un produit à un ami de 1 à 10.]({% image_buster /assets/img/surveys/landing_page_rating_scale_example.png %}){: style="max-width:70%;"}
{% else %}
![Échelle de notation pour indiquer la probabilité de recommander un produit à un ami de 1 à 10.]({% image_buster /assets/img/surveys/landing_page_rating_scale_example.png %}){: style="max-width:70%;"}
{% endif %}

## Configurer les champs et attributs obligatoires {#configure-required-fields-and-attributes}

Pour chaque bloc de formulaire, saisissez un **Identifier for Reporting** dans le panneau de paramètres situé à droite. Cet identifiant apparaît dans les rapports d'enquête et les exports CSV.

À garder à l'esprit :

- Vous pouvez enregistrer la plupart des réponses d'enquête dans des attributs personnalisés du profil utilisateur.
- Les réponses en texte long ne peuvent pas être enregistrées en tant qu'attributs personnalisés.
- Si vous choisissez de ne pas enregistrer une réponse en tant qu'attribut utilisateur, vous ne pourrez pas segmenter les utilisateurs en fonction de la valeur de cette réponse.

![Paramètres d'identifiant de rapport et d'enregistrement des attributs.]({% image_buster /assets/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## Consulter les rapports et l'analyse {#view-reporting-and-analytics}

Après le lancement, consultez les résultats dans :

{% if include.channel == 'in_app_message' %}
- L'onglet **Responses** pour les enquêtes par message in-app
{% elsif include.channel == 'landing_page' %}
- La vue d'analyse de la page de destination pour les enquêtes par page de destination
{% else %}
- L'onglet **Responses** pour les enquêtes par message in-app
- La vue d'analyse de la page de destination pour les enquêtes par page de destination
{% endif %}

Pour les définitions des analyses de haut niveau disponibles pour chaque enquête (toutes les réponses, complétées, partiellement complétées et impressions uniques), consultez [Analyse]({{site.baseurl}}/user_guide/messaging/surveys#analytics).

{% if include.channel == 'landing_page' %}
{% alert note %}
Les enquêtes par page de destination suivent les réponses partiellement complétées lorsque l'enquête utilise des [formulaires multi-étapes]({{site.baseurl}}/user_guide/messaging/surveys#multi-step-landing-page-forms).
{% endalert %}
{% endif %}

Vous pouvez également consulter les répartitions des réponses par question, choisir parmi trois types de graphiques et exporter les données au format CSV. Pour plus d'informations, consultez [Types de graphiques]({{site.baseurl}}/user_guide/messaging/surveys#chart-types).

## Recibler et déclencher {#retarget-and-trigger}

Vous pouvez :

- Segmenter les utilisateurs en fonction des réponses au sondage enregistrées comme attributs utilisateur.
- Segmenter les utilisateurs en fonction du statut de complétion du sondage.

{% if include.channel == 'in_app_message' %}

![Configuration du déclencheur et filtres de segmentation pour le suivi du sondage.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Déclencher des Campaigns et des Canvas lorsqu'un utilisateur complète un sondage dans une Campaign de message in-app.

![Configuration du déclencheur et filtre de segmentation pour le suivi du sondage d'une Campaign de message in-app.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% elsif include.channel == 'landing_page' %}

![Configuration du déclencheur et filtre de segmentation pour le suivi du sondage d'une page de destination.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

- Déclencher des Campaigns et des Canvas lorsqu'un utilisateur complète un sondage sur une page de destination.

{% else %}

![Configuration du déclencheur et filtres de segmentation pour le suivi du sondage.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Déclencher des Campaigns et des Canvas lorsqu'un utilisateur complète un sondage sur une page de destination ou dans une Campaign de message in-app.

![Configuration du déclencheur et filtre de segmentation pour le suivi du sondage d'une page de destination.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

![Configuration du déclencheur et filtre de segmentation pour le suivi du sondage d'une Campaign de message in-app.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% endif %}

### Limitations

Vous êtes soumis aux restrictions suivantes :

- Vous ne pouvez pas segmenter les utilisateurs en fonction des réponses en texte long.
- Le déclenchement par question-réponse ne reposant pas sur des attributs utilisateur enregistrés n'est pas disponible.