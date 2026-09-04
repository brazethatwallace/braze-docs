---
nav_title: Enquêtes
article_title: Enquêtes
page_order: 9
page_type: reference
channel:
  - landing pages
  - in-app messages
description: "Découvrez comment les enquêtes Braze vous permettent de recueillir des retours de première partie sur les pages de destination et les messages in-app, y compris l'analyse, les blocs de formulaire et l'exportation Currents."
---

# Enquêtes {#surveys}

> Les enquêtes Braze vous permettent de recueillir des retours de première partie directement auprès de vos utilisateurs et d'agir en conséquence dans vos messages de suivi, sans quitter le tableau de bord de Braze. Utilisez les enquêtes pour comprendre le ressenti des utilisateurs, capturer leurs préférences et créer des segments et des déclencheurs à partir des réponses recueillies.

## Disponibilité par canal {#channel-availability}

Les enquêtes sont disponibles sur deux canaux. Chaque page de canal couvre le flux de création, la composition et l'emplacement des rapports propres au canal, tandis que cette page couvre les concepts et les fonctionnalités qui s'appliquent aux deux.

| Canal | Créer des enquêtes dans |
| --- | --- |
| Pages de destination | [Enquêtes sur les pages de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys) |
| Messages in-app | [Enquêtes par message in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Disponibilité des enquêtes par canal" }

## Page des enquêtes {#surveys-page}

Accédez à **Messaging** > **Enquêtes** pour retrouver les enquêtes de vos pages de destination, Campaigns et Canvas au même endroit. Utilisez cette page comme point d'entrée pour examiner les performances de vos enquêtes sur l'ensemble des canaux.

{% alert note %}
Si vous ne voyez pas **Enquêtes** sous **Messaging**, contactez votre gestionnaire de compte Braze.
{% endalert %}

## Analyse {#analytics}

Chaque type de question d'enquête inclut des rapports enrichis par défaut, ce qui vous permet de consulter les données de réponse en un coup d'œil sans avoir à créer un Segment ou à exporter vers un outil séparé au préalable.

Les analyses de haut niveau incluent :

- **Toutes les réponses :** Total des réponses complètes et incomplètes
- **Terminées :** Utilisateurs ayant répondu à toutes les questions obligatoires
- **Partiellement terminées :** Utilisateurs ayant soumis certaines données, mais n'ayant pas répondu à toutes les questions obligatoires
- **Impressions uniques :** Total des vues de page

![Page des réponses à l'enquête affichant les analyses de score NPS avec les pourcentages de promoteurs, passifs et détracteurs ainsi qu'un graphique à barres horizontales de la distribution des scores.]({% image_buster /assets/img/surveys/survey_responses.png %})

### Types de graphiques {#chart-types}

Pour les blocs de formulaire de type boutons radio, menu déroulant et cases à cocher, vous pouvez choisir parmi trois types de graphiques dans la vue d'analyse de l'enquête. Cela vous offre davantage de flexibilité pour interpréter et partager des informations sans avoir à exporter vers un outil tiers.

| Type de graphique | Idéal pour |
| --- | --- |
| **Graphique à barres** | La vue horizontale par défaut des nombres et pourcentages de réponses. |
| **Graphique en colonnes** | Une vue verticale des nombres et pourcentages de réponses. Utilisez ce graphique pour comparer les réponses côte à côte, en particulier pour les questions à choix multiples ou les questions comportant davantage d'options de réponse. |
| **Graphique circulaire** | Une répartition proportionnelle des réponses. Utilisez ce graphique pour les questions à choix unique lorsque vous souhaitez voir comment les réponses sont distribuées entre les options. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Types de graphiques d'enquête" }

Chaque graphique affiche des données en temps réel à mesure que les réponses arrivent. Vous pouvez changer de type de graphique à tout moment sans affecter les données sous-jacentes.

![Détail par question de l'enquête utilisant un graphique à barres.]({% image_buster /assets/img/surveys/bar-charts-1.png %})

## Formulaires de page de destination à plusieurs étapes {#multi-step-landing-page-forms}

Créez une enquête sous forme de page de destination unique comportant plusieurs étapes automatiquement reliées entre elles, au lieu de créer plusieurs pages de destination indépendantes et de les relier manuellement. Par exemple, vous pouvez définir des étapes distinctes pour chaque question de l'enquête, ainsi qu'une étape de confirmation à la fin.

Cette fonctionnalité est spécifique au canal des pages de destination. Les enquêtes par message in-app prennent également en charge un gestionnaire de pages pour naviguer entre les étapes ; consultez [Composer une enquête par message in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#compose-an-in-app-message-survey) pour plus de détails.

![Éditeur de page de destination avec un aperçu de formulaire à plusieurs étapes et le panneau de propriétés du formulaire listant les étapes ainsi qu'une étape de confirmation verrouillée.]({% image_buster /assets/img/surveys/multi_step.png %})

## Blocs de questions et de formulaires {#question-and-form-blocks}

Les pages de destination et les messages in-app prennent en charge tous leurs blocs de formulaire standard dans les enquêtes, y compris le groupe de boutons radio, la case à cocher, le groupe de cases à cocher, le menu déroulant, la capture de numéro de téléphone, la capture d'e-mail et la capture de texte court. Cette section met en avant les trois blocs de formulaire dotés de rapports conçus spécifiquement pour les enquêtes : NPS, échelle numérique et texte long.

{% tabs local %}
{% tab NPS %}
### Bloc NPS autonome {#standalone-nps-block}

Le bloc **NPS** est un bloc de formulaire distinct du bloc **Évaluation** (échelle numérique), et non une option de configuration au sein de celui-ci. Ajoutez-le à une enquête pour poser la question standard du Net Promoter Score (0–10) et obtenir des rapports conçus spécifiquement pour ce cas d'usage.

Le bloc **NPS** vous offre de meilleurs rapports dans le tableau de bord qu'une simple question d'évaluation utilisée dans le même but. Au lieu d'un simple décompte des réponses par valeur, Braze regroupe automatiquement les réponses en promoteurs (9–10), passifs (7–8) et détracteurs (0–6), et affiche ces segments — ainsi que le score NPS qui en résulte — directement dans la vue d'analyse de l'enquête.

Currents exporte le score numérique (et, s'il a été ajouté, le champ de commentaire libre) dans l'événement **Survey Response**. Les segments de promoteurs, passifs et détracteurs ne sont pas des champs Currents distincts.

![Une enquête NPS mobile à côté du tableau de bord des réponses à l'enquête, qui affiche un score NPS avec la répartition entre promoteurs, passifs et détracteurs ainsi qu'un graphique de distribution des réponses.]({% image_buster /assets/img/surveys/survey_and_chart.png %})
{% endtab %}

{% tab Échelle numérique %}
### Questions à échelle numérique {#number-scale-questions}

Également appelée échelle d'évaluation sur les pages de canal ; les deux termes désignent le même bloc de formulaire **Évaluation**. Capturez des questions à échelle numérique de 1 à 5, de 1 à 10 ou de 0 à 10 pour répondre à différents besoins d'enquête et de reporting, des simples évaluations de satisfaction aux scores de probabilité de recommandation. Pour des captures d'écran de composition propres à chaque canal, consultez la section Échelle d'évaluation sur la page des [enquêtes sur les pages de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#rating-scale) ou des [enquêtes par message in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#rating-scale).

Vous pouvez collecter une évaluation en tant que réponse à l'enquête, l'enregistrer comme attribut personnalisé de type entier, ou les deux. Associez une question à échelle numérique à un bloc de [capture de texte long](#long-form-text-capture) pour collecter un score numérique accompagné de commentaires qualitatifs dans la même enquête.

![Éditeur d'enquête de page de destination avec une question d'évaluation de 1 à 5 sélectionnée et le panneau des propriétés d'évaluation ouvert à droite.]({% image_buster /assets/img/surveys/rating_block.png %})
{% endtab %}

{% tab Texte long %}
### Capture de texte long {#long-form-text-capture}

La capture de texte long est utile pour recueillir des retours qualitatifs. Vous pouvez configurer le nombre minimum et maximum de caractères (jusqu'à 1 000 caractères), l'affichage ou non de la limite de caractères pendant la composition, la hauteur de la zone de texte et le texte de marque substitutive.

![Paramètres du bloc de capture de texte long.]({% image_buster /assets/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

{% alert important %}
Les champs de texte long dans les enquêtes par message in-app sur iOS sont temporairement limités à 250 caractères. Cette limitation sera corrigée dans une prochaine mise à jour du SDK iOS. En attendant, envisagez de maintenir votre nombre maximum de caractères à 250 ou moins pour les enquêtes présentées aux utilisateurs iOS.
{% endalert %}

Les réponses en texte long sont disponibles dans les rapports et les exports, mais elles ne peuvent pas être enregistrées comme attributs personnalisés du profil utilisateur — vous ne pouvez donc pas segmenter les utilisateurs par la valeur d'une réponse en texte long directement. Consultez les [Limitations]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#limitations) sur la page de chaque canal pour en savoir plus.

Dans Currents, les réponses en texte long utilisent `answer_type = 'free_form_text'` avec le texte dans `answer_long_string`.
{% endtab %}
{% endtabs %}

## Ordre aléatoire des choix {#randomized-choice-order}

Les blocs de groupe de boutons radio, de groupe de cases à cocher et de liste déroulante prennent en charge la randomisation des choix de réponse. Activez **Randomiser l'ordre des choix** pour mélanger les choix à chaque chargement de l'enquête, ce qui réduit le biais d'ordre lorsque la même première option risquerait sinon de fausser les réponses.

La randomisation modifie uniquement l'ordre d'affichage pour chaque répondant à l'enquête. Les libellés et les valeurs des rapports restent associés aux choix que vous avez configurés. Ainsi, les analyses, les exports CSV et la segmentation utilisent les mêmes données de réponse, quel que soit l'ordre dans lequel un utilisateur donné les a vues.

## Modèles d'enquête {#survey-templates}

Enregistrez une enquête en tant que modèle à partir de la bibliothèque de modèles de pages de destination ou de messages in-app afin que les créateurs puissent s'en servir comme point de départ au lieu de recréer les mêmes questions et blocs de formulaire à chaque fois. Lorsque les modèles d'enquête sont activés pour votre espace de travail, filtrez la bibliothèque par **Enquête** pour trouver et réutiliser les structures d'enquête enregistrées dans vos Campaigns, Canvas et pages de destination.

## Événements de réponse aux enquêtes {#survey-response-events}

Les réponses aux enquêtes sont transmises à [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) afin que vous puissiez exporter les données d'enquête vers votre entrepôt de données ou un outil de BI tiers pour des analyses en aval, des jointures avec d'autres données d'engagement et des rapports personnalisés allant au-delà des analyses intégrées du tableau de bord.

Braze exporte les réponses individuelles aux enquêtes vers Currents via l'événement **Survey Response** (`users.messages.survey.Response`). Chaque événement représente la réponse d'un répondant à une question d'enquête. Pour la référence complète des champs, consultez [Événements de réponse aux enquêtes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#survey-response-events) dans le glossaire des événements Currents.

## Entonnoir d'engagement des pages de destination {#landing-page-engagement-funnel}

Les enquêtes sur les pages de destination génèrent également des événements **Landing Page Impression** et **Landing Page Click** pour les vues de page et les clics suivis. La complétion d'une enquête sur une page de destination enregistre un événement **Survey Response** ; elle ne déclenche pas l'événement générique **Landing Page Form Submission**, qui est réservé aux formulaires standard (hors enquêtes) des pages de destination. Pour la référence complète des champs de ces événements, consultez le [glossaire des événements Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

## Articles connexes {#related-articles}

- [Enquêtes sur les pages de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys) : flux de création, composition et rapports pour le canal des pages de destination
- [Enquêtes par message in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys) : flux de création, composition et rapports pour le canal des messages in-app
- [Blocs de l'éditeur par glisser-déposer]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks) : référence complète des blocs de formulaire que vous pouvez ajouter à une enquête
- [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) : configurez l'exportation de données vers votre entrepôt de données ou votre outil de BI