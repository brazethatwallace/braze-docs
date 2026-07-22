{% comment %}
  Documentation partagée sur les enquêtes Braze.
  Paramètres :
  - channel (requis) : "in_app_message" ou "landing_page"
{% endcomment %}

{% multi_lang_include alerts/early_access_beta_alert.md feature='Braze surveys' %}

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

Pendant l'accès anticipé, les sondages sont créés dans votre flux de composition de messages existant.

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

## Composer un sondage par message in-app {#compose-an-in-app-message-survey}

Les sondages par message in-app contiennent deux pages par défaut :

- **Page 1**, où les utilisateurs répondent aux questions
- **Page de confirmation**, où le sondage est soumis

Par défaut, les boutons sont liés à **Next page**. Pour modifier ce comportement, mettez à jour chaque bouton dans le panneau **Actions**.

![Flux de pages et paramètres d'action du sondage par message in-app.]({% image_buster /assets/img/surveys/iam-survey-nav.png %}){: style="max-width:40%;"}

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

### Randomiser les choix de réponse {#randomize-answer-choices}

Les blocs de groupe de boutons radio, de groupe de cases à cocher et de liste déroulante prennent en charge la randomisation des choix de réponse. Activez **Randomize choice order** pour mélanger les choix à chaque chargement de l'enquête. Utilisez ce paramètre pour réduire le biais d'ordre lorsque la même première option pourrait fausser les réponses.

La randomisation ne modifie que l'ordre d'affichage pour chaque répondant. Les libellés et les valeurs de reporting restent associés aux choix que vous avez configurés, de sorte que l'analyse, les exports CSV et la segmentation utilisent les mêmes données de réponse.

### Capture de texte long {#long-text-capture}

La capture de texte long est utile pour recueillir des retours qualitatifs.

Vous pouvez configurer :

- Le nombre minimum et maximum de caractères (jusqu'à 1 000)
- L'affichage ou non des limites de caractères pendant la composition
- La hauteur de la zone de texte (lignes)
- Le texte de la marque substitutive

Pendant l'accès anticipé, les réponses en texte long sont disponibles dans les rapports et les exports, mais elles ne peuvent pas être enregistrées en tant qu'attributs personnalisés du profil utilisateur.

![Paramètres du bloc de capture de texte long.]({% image_buster /assets/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

### Échelle de notation {#rating-scale}

L'échelle de notation est utile pour capturer le sentiment, la satisfaction ou la probabilité de recommandation sous forme d'un nombre unique.

Dans le panneau de paramètres, sélectionnez une échelle dans la liste déroulante :

- **1–10**
- **1–5**
- **0–10** (plage standard du Net Promoter Score (NPS))

Vous pouvez collecter une note en tant que réponse d'enquête, l'enregistrer en tant qu'attribut personnalisé de type entier, ou les deux. Associez un bloc d'échelle de notation à un bloc de [capture de texte long](#long-text-capture) pour recueillir un score numérique accompagné de retours qualitatifs dans la même enquête.

{% if include.channel == 'in_app_message' %}
![Échelle de notation pour évaluer votre expérience en magasin de 1 à 5.]({% image_buster /assets/img/surveys/iam_rating_scale_example.png %}){: style="max-width:40%;"}
{% elsif include.channel == 'landing_page' %}
![Échelle de notation pour indiquer la probabilité de recommander un produit à un ami de 1 à 10.]({% image_buster /assets/img/surveys/landing_page_rating_scale_example.png %}){: style="max-width:70%;"}
{% else %}
![Échelle de notation pour indiquer la probabilité de recommander un produit à un ami de 1 à 10.]({% image_buster /assets/img/surveys/landing_page_rating_scale_example.png %}){: style="max-width:70%;"}
{% endif %}

## Configurer les champs et attributs requis {#configure-required-fields-and-attributes}

Pour chaque bloc de formulaire, saisissez un **Identifier for Reporting** dans le panneau de paramètres sur le côté droit. Cet identifiant apparaît dans les rapports d'enquête et les exports CSV.

Pendant l'accès anticipé :

- Vous pouvez enregistrer la plupart des réponses d'enquête dans des attributs personnalisés du profil utilisateur.
- Les réponses en texte long ne peuvent pas être enregistrées en tant qu'attributs personnalisés.
- Si vous choisissez de ne pas enregistrer une réponse en tant qu'attribut utilisateur, vous ne pourrez pas segmenter les utilisateurs en fonction de la valeur de cette réponse.

![Paramètres d'identifiant pour le reporting et d'enregistrement des attributs.]({% image_buster /assets/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## Consulter les rapports et les analyses {#view-reporting-and-analytics}

Après le lancement, consultez les résultats dans :

{% if include.channel == 'in_app_message' %}
- L'onglet **Responses** pour les enquêtes par message in-app
{% elsif include.channel == 'landing_page' %}
- La vue d'analyse de la page de destination pour les enquêtes sur page de destination
{% else %}
- L'onglet **Responses** pour les enquêtes par message in-app
- La vue d'analyse de la page de destination pour les enquêtes sur page de destination
{% endif %}

Les analyses de haut niveau comprennent :

- **All responses :** Total des réponses complètes et incomplètes
- **Completed :** Utilisateurs ayant répondu à toutes les questions obligatoires
- **Partially complete :** Utilisateurs ayant soumis certaines données, mais n'ayant pas répondu à toutes les questions obligatoires
- **Unique impressions :** Total des vues de page

{% if include.channel == 'landing_page' %}
{% alert note %}
Les enquêtes sur page de destination ne suivent pas les réponses partiellement complètes pendant l'accès anticipé.
{% endalert %}
{% endif %}

Vous pouvez également consulter les répartitions de réponses par question et exporter les données au format CSV.

### Choisir un type de graphique {#choose-a-chart-type}

Pour les blocs de formulaire à boutons radio, listes déroulantes et cases à cocher, vous pouvez choisir parmi trois types de graphiques dans la vue d'analyse de l'enquête. Cela vous offre plus de flexibilité pour interpréter et partager des informations sans avoir à exporter vers un outil tiers.

| Type de graphique | Idéal pour |
| --- | --- |
| Graphique à barres | La vue horizontale par défaut des nombres et pourcentages de réponses. |
| Graphique en colonnes | Une vue verticale des nombres et pourcentages de réponses. Utilisez ce graphique pour comparer les réponses côte à côte, en particulier pour les questions à sélection multiple ou les questions comportant davantage d'options de réponse. |
| Graphique circulaire | Une répartition proportionnelle des réponses. Utilisez ce graphique pour les questions à sélection unique lorsque vous souhaitez voir comment les réponses sont distribuées entre les options. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Types de graphiques d'enquête" }

Chaque graphique se met à jour en temps réel à mesure que les réponses arrivent. Vous pouvez changer de type de graphique à tout moment sans affecter les données sous-jacentes.

![Répartition par question de l'enquête à l'aide d'un graphique à barres.]({% image_buster /assets/img/surveys/bar-charts-1.png %})

## Recibler et déclencher {#retarget-and-trigger}

Pendant l'accès anticipé, vous pouvez :

- Segmenter les utilisateurs en fonction des réponses aux enquêtes enregistrées comme attributs utilisateur.
- Segmenter les utilisateurs en fonction du statut de complétion de l'enquête.

{% if include.channel == 'in_app_message' %}

![Configuration du déclencheur et filtres de segmentation pour le suivi d'enquête.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Déclencher des Campaigns et des Canvas lorsqu'un utilisateur complète une enquête dans une Campaign de message in-app.

![Configuration du déclencheur et filtre de segmentation pour le suivi d'enquête d'une Campaign de message in-app.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% elsif include.channel == 'landing_page' %}

![Configuration du déclencheur et filtre de segmentation pour le suivi d'enquête d'une page de destination.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

- Déclencher des Campaigns et des Canvas lorsqu'un utilisateur complète une enquête sur une page de destination.

{% else %}

![Configuration du déclencheur et filtres de segmentation pour le suivi d'enquête.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Déclencher des Campaigns et des Canvas lorsqu'un utilisateur complète une enquête sur une page de destination ou dans une Campaign de message in-app.

![Configuration du déclencheur et filtre de segmentation pour le suivi d'enquête d'une page de destination.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

![Configuration du déclencheur et filtre de segmentation pour le suivi d'enquête d'une Campaign de message in-app.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% endif %}

### Limitations

Pendant l'accès anticipé, les restrictions suivantes s'appliquent :

- Vous ne pouvez pas segmenter les utilisateurs en fonction des réponses en texte long.
- Le déclenchement par question-réponse qui ne repose pas sur des attributs utilisateur enregistrés n'est pas disponible.