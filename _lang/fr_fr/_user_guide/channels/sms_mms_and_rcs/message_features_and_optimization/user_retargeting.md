---
nav_title: "Reciblage des utilisateurs"
article_title: "Reciblage des utilisateurs"
description: "Cet article de référence explique comment les utilisateurs peuvent recibler leurs messages en fonction des interactions SMS et RCS d'un utilisateur."
page_type: reference
page_order: 4
alias: /sms_mms_rcs_user_retargeting/
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS

---

# Reciblage des utilisateurs {#user-retargeting}

> En plus de modifier l'état d'abonnement de l'utilisateur et d'envoyer des réponses automatiques basées sur les mots-clés entrants, Braze enregistre également les interactions dans le profil utilisateur à des fins de filtrage et de déclenchement de messages.<br><br>Ces filtres et déclencheurs vous permettent de filtrer les actions en fonction des utilisateurs qui ont reçu ou répondu à des Campaigns SMS, MMS et RCS, ou d'interagir davantage avec les utilisateurs qui ont cliqué sur des URL raccourcies.

{% alert tip %}
Pour en savoir plus sur les mots-clés personnalisés et comment configurer la messagerie bidirectionnelle pour tirer parti de ces options de reciblage, consultez notre article sur les [mots-clés personnalisés]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling).
{% endalert %}

## Options de reciblage {#retargeting-options}

{% alert note %}
Lors de la création d'audiences avec le reciblage des utilisateurs, vous pouvez souhaiter inclure ou exclure certains utilisateurs en fonction de leurs préférences, et afin de respecter les lois sur la confidentialité, telles que le droit « Ne pas vendre ou partager » en vertu du CUP. Les marketeurs doivent mettre en œuvre les filtres pertinents pour l'éligibilité des utilisateurs dans les critères d'entrée de leur Canvas et/ou Campaign.
{% endalert %}

### Filtrer les utilisateurs par SMS, MMS et RCS {#filter-users-by-sms-mms-and-rcs}

Les utilisateurs peuvent être filtrés en fonction de la date de leur dernière réception d'un SMS, MMS ou RCS, ou s'ils ont reçu un SMS, MMS ou RCS provenant d'une Campaign spécifique. Les filtres peuvent être définis à l'étape **Audiences cibles** du générateur de Campaign.

{% alert note %}
Lorsqu'un message est reçu, ouvert ou cliqué, Braze met à jour les données de tous les profils qui partagent le même numéro de téléphone que le profil ayant enregistré l'interaction. Les utilisateurs qui partagent un numéro de téléphone avec quelqu'un qui a reçu, ouvert ou cliqué le message peuvent correspondre à ce filtre même s'ils ne faisaient pas partie à l'origine de la Campaign ou n'ont pas reçu directement le message.
{% endalert %}

#### Filtrer par dernier SMS/MMS/RCS reçu {#filter-by-last-received-smsmmsrcs}

![Filtre de segmentation Dernier SMS reçu après le 8 décembre 2020.]({% image_buster /assets/img/sms/filter2.png %})

#### Filtrer par messages reçus d'une Campaign SMS/MMS/RCS {#filter-by-received-messages-from-smsmmsrcs-campaign}

Filtre les utilisateurs qui ont reçu un message d'une Campaign spécifique. Avec ce filtre, vous avez également la possibilité de filtrer ceux qui n'ont pas reçu de messages d'une Campaign.

![Filtre de segmentation A reçu un message de la Campaign « Reciblage SMS ».]({% image_buster /assets/img/sms/filter1.png %})

### Déclencher des messages lorsque les utilisateurs reçoivent un SMS, MMS ou RCS {#trigger-messages}

Pour déclencher des messages lorsque les utilisateurs reçoivent des messages SMS, MMS ou RCS provenant d'une Campaign spécifique, sélectionnez **Interagir avec une Campaign** comme action de déclenchement pour une Campaign basée sur les actions. Ensuite, sélectionnez **Recevoir un SMS** et la Campaign que vous souhaitez utiliser.

![Pour déclencher des messages lorsque les utilisateurs reçoivent des messages SMS, MMS ou RCS provenant d'une Campaign spécifique, sélectionnez Interagir avec une Campaign comme action de déclenchement pour une Campaign basée sur les actions. Ensuite, sélectionnez Recevoir un SMS et la Campaign SMS, MMS ou RCS que vous souhaitez utiliser.]({% image_buster /assets/img/sms/trigger.png %})

### Filtrer par liens de suivi avancés {#filter-by-advanced-tracking-links}

Reciblez les utilisateurs qui ont cliqué sur des Campaigns avec des [liens de suivi avancés]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening).
Seules les Campaigns pour lesquelles le suivi avancé est activé apparaissent dans les menus déroulants suivants :

#### Recibler les utilisateurs qui ont cliqué sur une Campaign SMS, MMS ou RCS spécifique {#retarget-users-who-have-clicked-a-specific-sms-mms-or-rcs-campaign}

1. Créez un Segment à l'aide du filtre **A cliqué/ouvert une Campaign**.
2. Sélectionnez **a cliqué sur un lien SMS raccourci**.
3. Choisissez la Campaign souhaitée.

![Capture d'écran relative au reciblage des utilisateurs ayant cliqué sur une Campaign SMS, MMS ou RCS spécifique.]({% image_buster /assets/img/sms/retargeting5.png %})

#### Recibler les utilisateurs qui ont cliqué sur une étape de Canvas spécifique {#retarget-users-who-have-clicked-a-specific-canvas-step}

1. Créez un Segment à l'aide du filtre **A cliqué/ouvert une étape**.
2. Sélectionnez **a cliqué sur un lien SMS raccourci**.
3. Choisissez le Canvas et l'étape du Canvas souhaités.

![Capture d'écran relative au reciblage des utilisateurs ayant cliqué sur une étape de Canvas spécifique.]({% image_buster /assets/img/keyword_example1.jpg %})

## Reciblage par catégorie de mots-clés spécifique {#keyword-category-specific-retargeting}

En plus des trois catégories de mots-clés par défaut (Abonnement, Désabonnement et Aide), vous pouvez également créer jusqu'à 25 catégories de mots-clés personnalisées, ce qui vous permet d'identifier des mots-clés et des réponses arbitraires. Ces catégories peuvent être utilisées pour le filtrage et le reciblage. Pour en savoir plus sur les catégories de mots-clés globales et comment les configurer, consultez la section [Traitement des mots-clés]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing).

### Filtrer par récence {#filter-by-recency}

Filtrez en fonction de la récence de la réponse d'un utilisateur à votre programme SMS, MMS ou RCS. Ce filtre évalue la dernière date à laquelle un utilisateur a envoyé un message entrant correspondant à l'une des catégories de mots-clés.

![Filtre de segmentation « Dernier SMS envoyé au groupe d'abonnement « Marketing SMS » avec le mot-clé « Opt-in » après le 11 août 2020.]({% image_buster /assets/img/sms/retargeting1.png %})

### Filtrer par attribution de Campaign ou de Canvas {#filter-by-campaign-or-canvas-attribution}

Filtrez les utilisateurs qui ont répondu à une Campaign SMS, MMS ou RCS spécifique, à un composant Canvas, à une catégorie de mots-clés ou à une étiquette.

{% alert note %}
Ces filtres utilisent les [données d'interaction de messagerie]({{site.baseurl}}/messaging_interaction_data). Pour les Campaigns et Canvas arrêtés, ces données expirent après trois mois si elles ne sont pas utilisées dans un filtre de reciblage actif. Les données expirées peuvent être restaurées. La fenêtre de rétention de votre espace de travail peut différer de la valeur par défaut.
{% endalert %}

#### Filtrer par réponse à une Campaign spécifique avec catégorie de mots-clés {#filter-by-replied-to-a-specific-campaign-with-keyword-category}

![Campaign avec le filtre « A répondu au SMS » pour la Campaign « SMS-283 » « Promotion ».]({% image_buster /assets/img/sms/clicked_opened_campaign.png %})

#### Filtrer par réponse à une Campaign ou un Canvas avec une étiquette spécifique {#filter-by-replied-to-a-campaign-or-canvas-with-a-specific-tag}

![Campaign avec le filtre « A répondu au SMS » pour une Campaign ou un Canvas avec l'étiquette « Curbside Messaging Service C ».]({% image_buster /assets/img/sms/clicked_opened_campaign_canvas_tag.png %})

#### Filtrer par réponse à une étape spécifique {#filter-by-replied-to-a-specific-step}

![Campaign avec le filtre « A répondu au SMS » pour l'étape « SMS Double Opt » « Step - Help ».]({% image_buster /assets/img/sms/clicked_opened_step.png %})

### Déclencher des messages par mot-clé {#trigger-messages-by-keyword}

Les messages peuvent être déclenchés lorsque les utilisateurs envoient des messages entrants en fonction des catégories de mots-clés (l'utilisateur a envoyé l'un des mots-clés) ou d'autres mots-clés (l'utilisateur a envoyé un mot-clé qui ne correspond à aucune des catégories existantes). Ces déclencheurs sont configurés à l'étape Réception du générateur de Campaign.

Lors de l'évaluation d'un message entrant par rapport à un événement déclencheur défini, les espaces en début et en fin de message sont supprimés avant le début de l'évaluation.

{% alert tip %}
Si un Canvas basé sur une action est déclenché par un message SMS ou MMS entrant, vous pouvez référencer les [propriétés Liquid SMS prises en charge]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) dans n'importe quelle étape du Canvas jusqu'au prochain parcours d'action.
{% endalert %}

#### Déclencher par catégorie de mots-clés entrants {#trigger-by-inbound-keyword-category}

![Campaign SMS basée sur une action avec le filtre de segmentation « A envoyé le mot-clé « Opt-in » au groupe d'abonnement « Marketing SMS ».]({% image_buster /assets/img/sms/retargeting2.png %}){: style="margin-top:10px;"}

#### Déclencher par mots-clés arbitraires {#trigger-by-arbitrary-keywords}

Notez que lorsque vous déclenchez un message sur une réponse par mot-clé « Autre », vous avez la possibilité d'évaluer le corps du mot-clé sur une correspondance exacte du texte. Cette correspondance suit les mêmes règles que celles indiquées : seul le **message exact composé d'un seul mot** est traité (insensible à la _casse_). Un mot-clé envoyé `Hello Braze!` ne correspondrait pas aux critères affichés dans l'exemple suivant.

![Campaign SMS basée sur une action avec la catégorie de mots-clés « Autre » où le corps du message est exactement « Hello » ou « Hey ».]({% image_buster /assets/img/sms/retargeting3.png %}){: style="margin-top:10px;"}

#### Modèles de mots-clés {#template-keywords}

Lorsque vous déclenchez une Campaign ou un composant Canvas à partir d'un SMS ou MMS entrant, vous pouvez éventuellement intégrer le texte ou les pièces jointes multimédias envoyés par l'utilisateur dans le corps de votre Campaign ou Canvas avec Liquid. Cela vous permet d'accéder à la réponse de l'utilisateur, que vous pouvez ensuite inclure dans votre réponse, appliquer une logique conditionnelle, ou toute autre action réalisable avec Liquid.

{% raw %}

```liquid
Sorry, we didn't recognize {{sms.${inbound_message_body}}}. Text HELP for help or STOP to stop.
```

```liquid
{% if {{sms.${inbound_message_body}}} == "SNEAKERS" %}
OK, you're subscribed to updates on all our sneaker deals!
{% elsif {{sms.${inbound_message_body}}} == "SHIRTS" %}
Shirt deals coming up for you!
{% else %}
Want to receive a specific deal? Just text us the category you're interested in. For example SHIRTS or SNEAKERS.
{% endif %}
```

{% endraw %}