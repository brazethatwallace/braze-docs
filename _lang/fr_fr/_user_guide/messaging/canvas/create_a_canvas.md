---
nav_title: Créer un Canvas
article_title: Créer un Canvas
page_order: 1
description: "Découvrez comment créer et lancer un Canvas : configurez les bases, la planification d'entrée, l'audience cible, les paramètres d'envoi, construisez votre parcours, et bien plus encore."
tool: Canvas
search_rank: 1
---

# Créer un Canvas {#create-a-canvas}

> Cet article de référence couvre les étapes nécessaires à la création, la gestion et le test d'un Canvas. Suivez ce guide ou consultez notre [cours d'apprentissage Canvas sur Braze Learning](https://learning.braze.com/quick-overview-canvas-setup). Vous pouvez également partir d'un [modèle de Canvas Braze]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) pour accélérer votre configuration. Pour en savoir plus, consultez [Modèles de Canvas]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates). Pour ébaucher un Canvas à partir d'une description en langage naturel, utilisez [Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#canvases).

{% details Développer pour les détails de l'éditeur Canvas d'origine %}
Vous ne pouvez plus créer ni dupliquer de Canvas avec l'éditeur Canvas d'origine. Braze recommande de [cloner vos Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases) vers l'éditeur le plus récent.
{% enddetails %}

## Étape 1 : Configurer un nouveau Canvas {#step-1-set-up-a-new-canvas}

Commencez par accéder à **Messaging** > **Canvas**, puis sélectionnez **Créer un Canvas**.

Le générateur de Canvas vous guidera étape par étape dans la configuration de votre Canvas, de la dénomination à la définition des événements de conversion, en passant par l'intégration des utilisateurs ciblés dans votre parcours client. Sélectionnez chacun des onglets suivants pour voir les paramètres que vous pouvez ajuster à chaque étape du générateur.

{% tabs local %}
  {% tab Fondamentaux %}
    Ici, vous configurerez les fondamentaux de votre Canvas :
    - Nommez votre Canvas
    - Ajoutez des équipes
    - Ajoutez des tags
    - Attribuez des événements de conversion et choisissez leurs types d'événements et délais

    En savoir plus sur l'[étape Fondamentaux](#step-11-start-with-your-canvas-basics).
  {% endtab %}
  {% tab Planification d'entrée %}
    Ici, vous déciderez comment et quand vos utilisateurs entreront dans votre Canvas :
    - Planifiée : il s'agit d'une entrée dans le Canvas basée sur le temps
    - Par événement : votre utilisateur entrera dans votre Canvas après avoir effectué une action définie
    - Déclenchée par API : utilisez une requête API pour faire entrer des utilisateurs dans votre Canvas

    En savoir plus sur l'[étape Planification d'entrée](#step-12-determine-your-canvas-entry-schedule).
  {% endtab %}
  {% tab Audience cible %}
    Ici, vous sélectionnerez votre audience cible :
    - Créez votre audience en ajoutant des segments et des filtres
    - Affinez la rééligibilité et les limites d'entrée du Canvas
    - Consultez un résumé de votre audience cible

    En savoir plus sur l'[étape Audience cible](#step-13-set-your-target-entry-audience).
  {% endtab %}
  {% tab Paramètres d'envoi %}
    Ici, vous sélectionnerez vos paramètres d'envoi Canvas :
    - Sélectionnez vos paramètres d'abonnement
    - Définissez une limite de débit pour les messages de votre Canvas
    - Activez et configurez les heures calmes

    En savoir plus sur l'[étape Paramètres d'envoi](#step-14-select-your-send-settings).
  {% endtab %}
  {% tab Créer le Canvas %}
    Ici, vous créerez votre Canvas.

    Découvrez comment [créer votre Canvas](#step-2-build-your-canvas) à l'aide du générateur de Canvas.
  {% endtab %}
  {% tab Résumé %}
    Ici, vous trouverez le résumé des détails de votre Canvas. Si le [workflow d'approbation de Canvas]({{site.baseurl}}/user_guide/messaging/governance/approvals) est activé, vous pouvez approuver les détails répertoriés du Canvas avant le lancement.

  {% endtab %}
{% endtabs %}

### Étape 1.1 : Commencer par les fondamentaux de votre Canvas {#step-11-start-with-your-canvas-basics}

Ici, vous nommerez votre Canvas, assignerez des [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) et créerez ou ajouterez des [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags). Vous pouvez également attribuer des événements de conversion au Canvas.

{% alert tip %}
Ajoutez des tags à vos Canvas pour les retrouver facilement et créer des rapports. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reports/report_builder), vous pouvez filtrer par tags spécifiques.
{% endalert %}

![La page de détails du Canvas, avec des champs pour le nom du Canvas, la description, l'emplacement et les tags.]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

#### Choisir les événements de conversion {#choose-conversion-events}

Choisissez votre type d'événement de conversion, puis sélectionnez les conversions à enregistrer. Ces [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) permettront de mesurer l'efficacité de votre Canvas.

![Événement de conversion principal A avec le type d'événement de conversion « Effectue un achat » pour enregistrer les conversions des utilisateurs qui effectuent un achat dans un délai de conversion de trois jours.]({% image_buster /assets/img/add_canvas_conversions.png %})

Si votre Canvas comporte plusieurs variantes ou un groupe de contrôle, Braze utilisera cet événement de conversion pour déterminer la meilleure variation permettant d'atteindre cet objectif de conversion. En utilisant la même logique, vous pouvez créer plusieurs événements de conversion.

### Étape 1.2 : Déterminer la planification d'entrée de votre Canvas {#step-12-determine-your-canvas-entry-schedule}

Vous pouvez choisir l'une des trois méthodes par lesquelles les utilisateurs peuvent entrer dans votre Canvas.

#### Types de planification d'entrée {#entry-schedule-types}

{% tabs local %}
{% tab Livraison planifiée %}
Avec la livraison planifiée, les utilisateurs entreront selon un calendrier défini, de la même manière que vous planifieriez une campagne. Vous pouvez inscrire des utilisateurs dans un Canvas dès son lancement, les faire entrer dans votre parcours à un moment donné dans le futur, ou de manière récurrente (quotidienne, hebdomadaire ou mensuelle).

Si vous sélectionnez une planification récurrente mensuelle, notez que certains mois peuvent ne pas avoir le jour sélectionné. Par exemple, imaginons que vous configurez un Canvas pour envoyer mensuellement le 31e jour. Dans ce scénario, Braze envoie le dernier jour de ce mois, comme le 30 avril, car le 31 avril n'existe pas.

Dans cet exemple, en fonction des options temporelles, les utilisateurs entrent dans ce Canvas chaque mardi à 12 h dans leur fuseau horaire local, chaque semaine, à partir du 14 novembre 2025 jusqu'au 31 décembre 2025.

![La page « Planification d'entrée » avec le type défini sur « Planifiée ». En raison de la sélection, des options temporelles sont affichées, notamment la fréquence, l'heure de début, la récurrence, les jours et plus encore.]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})

Lorsque vous utilisez la livraison selon le fuseau horaire local, Braze évalue l'éligibilité à l'entrée deux fois : d'abord à l'heure de Samoa (UTC+13) le jour planifié, puis à l'heure locale de l'utilisateur. Un utilisateur doit être éligible pour les deux vérifications afin d'entrer dans le Canvas. Si vos filtres d'entrée utilisent des fenêtres temporelles relatives (par exemple, « il y a plus de 2 jours »), la période de 24 heures peut ne pas s'être écoulée au moment de la première vérification, ce qui entraîne l'entrée des utilisateurs avec un jour de retard. Pour éviter cela, utilisez une fenêtre temporelle plus large, par exemple d'au moins deux jours. Pour plus de détails, consultez [Quand Braze évalue-t-il les utilisateurs pour la livraison selon le fuseau horaire local ?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#when-does-braze-evaluate-users-for-local-time-zone-delivery)
{% endtab %}
{% tab Livraison par événement %}
Avec la livraison par événement, les utilisateurs entreront dans le Canvas et commenceront à recevoir des messages lorsqu'ils effectuent des actions spécifiques, comme ouvrir votre application, effectuer un achat ou déclencher un événement personnalisé.

Vous pouvez contrôler d'autres aspects du comportement du Canvas depuis la fenêtre **Audience d'entrée**, y compris les règles de rééligibilité et les paramètres de limite de fréquence. Notez que la livraison par événement n'est pas disponible pour les composants Canvas contenant des messages in-app.

![Un exemple de livraison par événement. Les utilisateurs entreront dans le Canvas s'ils effectuent un achat avec une fenêtre d'entrée commençant à 13 h 30 le 10 juin 2025.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

{% alert note %}
L'option **Interagir avec une étape Canvas** n'est pas disponible en tant que déclencheur d'entrée par événement pour les Canvas. Elle ne peut être utilisée que comme déclencheur pour les Campaigns. Pour déclencher un Canvas depuis un autre, utilisez le composant Canvas [Envoyer vers une destination]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination), ou créez un [webhook Braze-to-Braze]({{site.baseurl}}/user_guide/channels/webhooks/use_case_create_a_braze_to_braze_webhook#trigger-a-second-canvas-from-an-initial-canvas) qui appelle l'endpoint `/canvas/trigger/send`.
{% endalert %}

{% alert important %}
Si votre Canvas basé sur des événements envoie des messages plus tôt que prévu, vérifiez que l'horodatage de votre événement personnalisé est envoyé avec l'heure actuelle et non une heure antérieure. Par exemple, si un Canvas basé sur des événements a un délai de trois heures après qu'un utilisateur effectue un événement personnalisé, Braze utilise l'horodatage envoyé avec l'événement personnalisé pour évaluer ce délai. Si l'horodatage est antidaté de plus de trois heures, Braze considère le délai comme déjà écoulé et envoie le message immédiatement.
{% endalert %}
{% endtab %}
{% tab Livraison déclenchée par API %}
Avec la livraison déclenchée par API, les utilisateurs entreront dans votre Canvas et commenceront à recevoir des messages après avoir été ajoutés via l'[endpoint `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) par l'API. Dans le tableau de bord, vous pouvez trouver un exemple de requête cURL qui effectue cette opération, ainsi qu'attribuer un [`context`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) optionnel à l'aide de l'[objet context]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context).

![Un exemple de livraison déclenchée par API avec un Canvas ID et un exemple de requête cURL.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

Vous pouvez utiliser les endpoints suivants pour la livraison déclenchée par API :
- [POST : Envoyer des messages Canvas via livraison déclenchée par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)
- [POST : Planifier des Canvas déclenchés par API]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases)
- [POST : Mettre à jour des Canvas déclenchés par API planifiés]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases)
{% endtab %}
{% endtabs %}

Après avoir sélectionné votre méthode de livraison, ajustez les paramètres en fonction de votre cas d'usage, puis continuez à définir votre audience cible.

{% details Comportement de déduplication pour les Canvas utilisant l'éditeur d'origine %}
Si la fenêtre de rééligibilité est inférieure à la durée maximale du Canvas, un utilisateur pourra y entrer à nouveau et recevoir les messages de plusieurs composants. Dans le cas particulier où la nouvelle entrée d'un utilisateur atteint le même composant que son entrée précédente, Braze dédupliquera les messages de ce composant.

Si un utilisateur entre à nouveau dans le Canvas, atteint le même composant que lors de son entrée précédente et est éligible à un message in-app pour chaque entrée, l'utilisateur recevra le message deux fois (en fonction de la priorité des messages in-app) à condition qu'il rouvre une session deux fois.
{% enddetails %}

### Étape 1.3 : Définir l'audience d'entrée cible {#step-13-set-your-target-entry-audience}

Seuls les utilisateurs correspondant à vos critères définis peuvent entrer dans le parcours à l'étape **Audience cible**, ce qui signifie que Braze évalue l'audience cible pour l'éligibilité **avant** que les utilisateurs n'entrent dans le parcours Canvas. Par exemple, si vous souhaitez cibler de nouveaux utilisateurs, vous pouvez sélectionner un segment d'utilisateurs ayant utilisé votre application pour la première fois il y a moins d'une semaine.

{% alert important %}
Dans les espaces de travail comportant plusieurs applications, l'éligibilité de l'audience d'entrée Canvas (y compris les segments et les filtres) est évaluée uniquement lorsque les utilisateurs entrent dans le Canvas, et non aux étapes de message individuelles. Si votre espace de travail comporte plusieurs applications et que vous devez vous assurer que les étapes de message ne ciblent que les utilisateurs d'une application spécifique, utilisez l'une des approches suivantes dans chaque étape de message :
- Activez **Valider l'audience à l'envoi du message** dans les [validations de livraison]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations) de l'étape de message et ajoutez des segments ou des filtres spécifiques à l'application.
- Utilisez Liquid pour vérifier l'appareil ou l'application ciblée au moment de l'envoi.

Sans ces mesures de protection, les utilisateurs qualifiés pour le parcours dans une application peuvent recevoir des messages destinés à une autre application s'ils utilisent également d'autres applications dans votre espace de travail.
{% endalert %}

Dans **Contrôles d'entrée**, vous pouvez limiter le nombre d'utilisateurs à chaque exécution planifiée du Canvas. Pour les Canvas déclenchés par API et par événement, cette limite s'applique à chaque heure UTC.

{% multi_lang_include alerts/warning_alerts.md alert='Canvas race condition audience trigger' %}

#### Tester votre audience {#testing-your-audience}

Après avoir ajouté des segments et des filtres à votre audience cible, vous pouvez vérifier si votre audience est configurée comme prévu en [recherchant un utilisateur]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) pour confirmer s'il correspond aux critères d'audience.

![Le champ « Recherche d'utilisateur », qui vous permet de rechercher par ID utilisateur externe ou ID Braze.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### Sélectionner les contrôles d'entrée {#selecting-entry-controls}

Les contrôles d'entrée déterminent si les utilisateurs sont autorisés à entrer de nouveau dans un Canvas. Vous pouvez également limiter le nombre de personnes qui pourraient potentiellement entrer dans ce Canvas selon une cadence sélectionnée en fonction de votre type de planification d'entrée :

- **Planifiée :** durée de vie du Canvas ou à chaque exécution planifiée du Canvas
- **Par événement :** par heure, par jour ou durée de vie du Canvas
- **Déclenchée par API :** par heure, par jour ou durée de vie du Canvas

Par exemple, si vous avez un Canvas planifié et que vous sélectionnez **Limiter le volume d'entrées** et définissez le champ **Nombre maximal d'entrées** à 500 000 utilisateurs avec **À chaque exécution planifiée du Canvas** comme cadence limite, alors le Canvas n'enverra qu'à 500 000 utilisateurs par envoi planifié.

![La page « Contrôles d'entrée » affichant des cases à cocher pour « Autoriser les utilisateurs à entrer de nouveau dans le Canvas » et « Limiter le volume d'entrées ».]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
Braze ne recommande pas de sélectionner **À chaque exécution planifiée du Canvas** pour l'IP warming, car cela peut entraîner une augmentation des volumes d'envoi.
{% endalert %}

#### Définir les critères de sortie {#setting-exit-criteria}

La définition des [critères de sortie]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria) détermine quels utilisateurs vous souhaitez faire sortir d'un Canvas. Si un utilisateur effectue l'événement d'exception ou correspond aux segments et filtres, il ne recevra plus aucun message.

#### Calculer la population cible {#calculating-target-population}

Dans la section **Population cible**, vous pouvez consulter un résumé de votre audience, comme vos segments sélectionnés et les filtres supplémentaires, ainsi qu'une répartition du nombre d'utilisateurs joignables par canal de communication. Pour calculer le nombre exact d'utilisateurs joignables dans votre audience cible plutôt que l'estimation par défaut, sélectionnez [Calculer les statistiques exactes]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#calculating-exact-statistics).

Notez que :

- Le calcul des statistiques exactes peut prendre quelques minutes. Cette fonction ne calcule les statistiques exactes qu'au niveau du segment, et non au niveau du filtre ou du groupe de filtres.
- Pendant le chargement des statistiques exactes, une estimation arrondie peut apparaître. Le chiffre exact apparaît dans la section **Utilisateurs joignables** une fois le chargement terminé. Vous pouvez sélectionner **Afficher les statistiques supplémentaires** pour une répartition détaillée.
- Pour les segments importants, il est normal d'observer de légères variations même lors du calcul des statistiques exactes. La précision de cette fonctionnalité est de 99,999 % ou plus.

Pour afficher des statistiques supplémentaires, telles que le chiffre d'affaires moyen sur la durée de vie des utilisateurs ciblés, sélectionnez **Afficher les statistiques supplémentaires**.

![Répartition de la population cible avec l'option de calculer les statistiques exactes.]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

#### Pourquoi le nombre de l'audience cible peut différer du nombre d'utilisateurs joignables {#why-the-target-audience-count-could-differ-from-the-reachable-users-count}

{% multi_lang_include audience/segments.md section='Differing audience size' %}

### Étape 1.4 : Sélectionner vos paramètres d'envoi {#step-14-select-your-send-settings}

Sélectionnez **Paramètres d'envoi** pour modifier vos paramètres d'abonnement, activer la limitation du débit et activer les [heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours). En activant la [limitation du débit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-rate-limiting) ou la [limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping), vous pouvez réduire la pression marketing exercée sur vos utilisateurs et vous assurer de ne pas les sur-solliciter.

Pour les Canvas ciblant les canaux e-mail et push, vous pouvez limiter votre Canvas pour que seuls les utilisateurs explicitement abonnés reçoivent le message (en excluant les utilisateurs inscrits ou désabonnés). Par exemple, imaginons que vous avez trois utilisateurs avec des statuts d'abonnement différents :

{% multi_lang_include messaging/intelligent_channel_user_examples.md %}

Pour ce faire, définissez les **Paramètres d'abonnement** pour envoyer ce Canvas aux « utilisateurs abonnés uniquement ». Cette option garantira que seuls les utilisateurs abonnés recevront votre e-mail, et Braze n'enverra vos notifications push qu'aux utilisateurs ayant activé les push par défaut.

Ces paramètres d'abonnement sont appliqués par étape, ce qui signifie qu'ils n'ont aucun effet sur l'audience d'entrée. Ainsi, ce paramètre est utilisé pour évaluer l'éligibilité d'un utilisateur à recevoir chaque étape du Canvas.

{% alert important %}
Avec cette configuration, n'incluez aucun filtre dans l'étape **Audience cible** qui limite l'audience à un seul canal (par exemple, `Foreground Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

Vous pouvez choisir de définir des [heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) (la période pendant laquelle vos messages ne sont pas envoyés) pour votre Canvas. Cochez **Activer les heures calmes** dans vos **Paramètres d'envoi**. Sélectionnez ensuite vos heures calmes dans le fuseau horaire local de votre utilisateur et choisissez si le message doit être abandonné ou envoyé au prochain moment disponible.

Lorsque **Envoyer au prochain moment disponible** est sélectionné, les heures calmes suppriment le message et l'envoient au prochain moment disponible en dehors des heures calmes. Par exemple, imaginons que les heures calmes sont configurées pour empêcher l'envoi de messages entre 11 h 30 et 14 h 30 dans le fuseau horaire local de l'utilisateur, et qu'un utilisateur atteint une étape de message à 11 h 35. Comme cette heure se situe dans les heures calmes, le message n'est pas encore envoyé, et l'utilisateur reçoit l'étape de message à 14 h 30, après la fin des heures calmes.

![La page « Heures calmes » affichant une case à cocher pour activer les heures calmes. Si activée, l'heure de début, l'heure de fin et le comportement de repli peuvent être définis.]({% image_buster /assets/img/quiet_hours.png %})

## Étape 2 : Créer votre Canvas {#step-2-build-your-canvas}

{% alert tip %}
Gagnez du temps et simplifiez la création de votre Canvas en utilisant les [modèles Canvas de Braze]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) ! Parcourez notre bibliothèque de modèles prédéfinis pour trouver celui qui correspond à votre cas d'usage et personnalisez-le selon vos besoins spécifiques. Pour plus d'informations, consultez [Modèles Canvas]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates).
{% endalert %}

### Étape 2.1 : Ajouter une variante {#step-21-add-a-variant}

![Le bouton « Ajouter une variante » sélectionné affichant un menu contextuel avec l'option « Ajouter une variante ».]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

Sélectionnez **Ajouter une variante**, puis ajoutez une nouvelle variante à votre Canvas. Les variantes représentent un parcours que vos utilisateurs emprunteront et peuvent contenir plusieurs étapes et branches.

Vous pouvez ajouter des variantes supplémentaires en sélectionnant le bouton plus <i class="fas fa-plus-circle"></i>. Lorsque vous ajoutez de nouvelles variantes, vous pourrez ajuster la répartition de vos utilisateurs entre elles afin de comparer et d'analyser l'efficacité de différentes stratégies d'engagement.

![Deux exemples de variantes dans un Canvas Braze.]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
Par défaut, l'attribution des variantes Canvas est déterminée par un hachage déterministe de l'ID utilisateur et de l'ID Canvas (et non par le [numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) d'un utilisateur), ce qui signifie qu'un utilisateur donné est systématiquement attribué à la même variante lors d'une nouvelle entrée, tant que les pourcentages de répartition des variantes restent inchangés. Si vous modifiez la répartition des variantes après le lancement, les utilisateurs peuvent être attribués à des variantes différentes lorsqu'ils entrent à nouveau dans le Canvas. <br><br>Si vous avez besoin d'une attribution qui reste fixe lorsque les pourcentages de répartition changent, utilisez une seule variante Canvas et orientez les utilisateurs avec une étape [Parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths). Au début du parcours, utilisez une étape [Mise à jour utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) pour stocker un nombre aléatoire dans un attribut personnalisé, puis filtrez sur cet attribut dans les parcours d'audience.

{% details Développer pour voir les étapes %}

1. Créez un attribut personnalisé de type **Nombre** pour stocker votre nombre aléatoire. Donnez-lui un nom facile à retrouver, comme `lottery_number` ou `random_assignment`. Dans votre tableau de bord, accédez à **Paramètres des données** > **Attributs personnalisés**.<br><br>
2. Utilisez une seule variante Canvas (ou ajoutez la même étape de mise à jour utilisateur à chaque variante). Ajoutez une étape [Mise à jour utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) au début du parcours. Cette étape génère et stocke le nombre aléatoire avant que les utilisateurs n'atteignent votre étape de parcours d'audience.<br><br>
3. Dans l'étape Mise à jour utilisateur, sélectionnez l'[Éditeur JSON avancé]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#advanced-json-editor). Utilisez la balise {% raw %}{% random %}{% endraw %} pour générer le nombre. Pour plus de détails, consultez [Envoyer des messages avec un nombre aléatoire]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#send-messages-with-a-random-number). Par exemple, {% raw %}`{% random 10 %}`{% endraw %} renvoie un entier de 0 à 9. Définissez l'attribut personnalisé de l'étape 1 en utilisant un JSON comme celui-ci :<br><br>{% raw %}
```json
{% if {{custom_attribute.${lottery_number}}} == blank %}
{% capture lottery_number_str %}{% random 10 %}{% endcapture %}
{
  "attributes": [
    {
      "lottery_number": {{ lottery_number_str | plus: 0 }}
    }
  ]
}
{% endif %}
```
{% endraw %}
<br><br>
Le bloc {% raw %}`{% if %}`{% endraw %} définit le nombre uniquement lorsque l'attribut est vide, afin que les utilisateurs conservent la même attribution lorsqu'ils entrent à nouveau dans le Canvas.<br><br>

{: start="4"}
4. Ajoutez une étape [Parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) après l'étape Mise à jour utilisateur. Dans chaque groupe d'audience, ajoutez des filtres basés sur votre attribut personnalisé au lieu d'utiliser des pourcentages de répartition des variantes.<br><br>Par exemple, si vous avez utilisé {% raw %}`{% random 10 %}`{% endraw %}, un groupe pourrait utiliser `lottery_number` **est inférieur à 4**, un autre **est supérieur à 3 et inférieur à 7**, et un troisième **est supérieur à 6 et inférieur à 10**.

{% enddetails %}
{% endalert %}

### Étape 2.2 : Ajouter des étapes Canvas {#step-22-add-canvas-steps}

Vous pouvez ajouter des étapes supplémentaires à votre workflow Canvas en faisant glisser et en déposant des composants depuis la barre latérale **Composants**. Ou sélectionnez le bouton plus <i class="fas fa-plus-circle"></i> pour ajouter un composant via le menu contextuel.

{% alert tip %}
Au fur et à mesure que vous ajoutez des étapes, vous pouvez modifier le niveau de zoom pour vous concentrer sur les détails ou visualiser l'ensemble du parcours utilisateur. Zoomez avec <kbd>Shift</kbd> + <kbd>+</kbd> ou dézoomez avec <kbd>Shift</kbd> + <kbd>-</kbd>.
{% endalert %}

![La fenêtre de recherche de composants ajoutant une étape de délai au Canvas Braze.]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert important %}
Vous pouvez ajouter jusqu'à 200 étapes dans un Canvas. Si votre Canvas dépasse 200 étapes, des problèmes de chargement peuvent survenir.
{% endalert %}

#### Durée maximale {#maximum-duration}

Au fur et à mesure que votre parcours Canvas s'enrichit en étapes, la durée maximale correspond au temps le plus long qu'un utilisateur peut mettre pour terminer ce Canvas. Elle est calculée en additionnant les délais et les fenêtres de déclenchement de chaque étape pour chaque variante sur le chemin le plus long. Par exemple, si votre Canvas comporte une étape de délai de 3 jours et une étape de message, la durée maximale de votre Canvas sera de 3 jours.

#### Modifier une étape {#editing-a-step}

Vous souhaitez modifier une étape dans votre parcours utilisateur ? Découvrez comment faire en fonction de votre workflow Canvas !

Vous pouvez modifier n'importe quelle étape de votre workflow Canvas en sélectionnant l'un des composants. Par exemple, imaginons que vous souhaitiez modifier votre première étape, un composant [Délai]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step), dans votre workflow pour une date spécifique. Sélectionnez l'étape pour afficher ses paramètres et ajustez votre délai au 1er mars. Cela signifie que le 1er mars, vos utilisateurs passeront à l'étape suivante de votre Canvas.

![Un exemple d'étape « Délai » avec le délai configuré sur « Jusqu'à un jour spécifique ».]({% image_buster /assets/img_archive/edit_delay_flow.png %})

Vous pouvez également modifier et ajuster rapidement les **Paramètres d'action** de votre étape [Parcours d'action]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) pour maintenir les utilisateurs pendant une fenêtre de temps. Cela priorise leur prochain parcours en fonction des actions effectuées durant cette période d'évaluation.

![La deuxième étape du Canvas, « Paramètres d'action », avec une fenêtre d'évaluation définie à 1 jour.]({% image_buster /assets/img_archive/action_paths_flow.png %})

Les composants légers de Canvas permettent une expérience d'édition simple, facilitant ainsi l'ajustement des détails de votre Canvas.

#### Messages dans Canvas {#messages-in-canvas}

Modifiez les messages dans un composant Canvas pour contrôler les messages qu'une étape particulière enverra. Canvas peut envoyer des e-mails, des notifications push mobiles et Web, ainsi que des webhooks pour s'intégrer à d'autres systèmes. Comme pour les Campaigns, vous pouvez utiliser certains modèles [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) pour personnaliser vos messages.

{% alert tip %}
Saviez-vous que vous pouvez inclure les noms des composants Canvas dans vos messages et modèles de liens ?<br>
Utilisez la balise Liquid `campaign.${name}` dans Canvas pour afficher le nom du composant Canvas actuel.
{% endalert %}

Le composant Message gère les messages envoyés aux utilisateurs. Vous pouvez sélectionner vos **Canaux de communication** et ajuster les **Paramètres de réception** pour optimiser la communication de votre Canvas. Pour plus de détails sur ce composant, consultez [Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step).

![L'étape « Configurer les messages », avec « Canaux de communication » sélectionné, affichant la liste des canaux de communication disponibles, tels que la notification push Android, les Content Cards, l'e-mail, et plus encore.]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

Sélectionnez **Terminé** une fois que vous avez fini de configurer votre composant Canvas.

{% tabs local %}
{% tab Propriétés d'entrée Canvas %}

L'[objet `context`]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) est configuré dans l'étape **Planification de l'entrée** lors de la création d'un Canvas et indique le déclencheur qui fait entrer un utilisateur dans un Canvas. Ces propriétés peuvent également accéder aux propriétés des payloads d'entrée dans les Canvas déclenchés par API. Notez que l'objet `context` peut atteindre 50 Ko.

Utilisez le Liquid suivant pour référencer ces propriétés créées lors de l'entrée dans le Canvas : {% raw %} ``context.${property_name}`` {% endraw %}. Notez que les événements doivent être des événements personnalisés ou des événements d'achat pour être utilisés de cette manière.

{% raw %}
Par exemple, considérez la requête suivante : `"context" : {"product_name" : "shoes", "product_price" : 79.99}`. Vous pourriez ajouter le mot « shoes » à un message avec ce Liquid ``{{context.${product_name}}}``.
{% endraw %}

{% endtab %}

{% tab Propriétés d'événement %}
Les propriétés d'événement sont les propriétés que vous définissez sur les événements personnalisés et les achats. Ces `event_properties` peuvent être utilisées dans les Campaigns avec livraison par événement ainsi que dans les Canvas.

Dans Canvas, les propriétés d'événements personnalisés et d'achats peuvent être utilisées en Liquid dans toute étape de message qui suit une étape Parcours d'action. Utilisez ce Liquid {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %} pour référencer ces `event_properties`. Ces événements doivent être des événements personnalisés ou des événements d'achat pour être utilisés de cette manière dans le composant Message.

Dans la première étape de message suivant un parcours d'action, vous pouvez utiliser les `event_properties` liées à l'événement référencé dans ce parcours d'action. Vous pouvez avoir d'autres étapes (qui ne sont pas une autre étape Parcours d'action ou Message) entre cette étape Parcours d'action et l'étape Message. Notez que vous n'aurez accès aux `event_properties` que si votre étape Message peut être rattachée à un chemin autre que « Tous les autres » dans une étape Parcours d'action.

{% endtab %}
{% endtabs %}

### Étape 2.3 : Modifier les connexions {#step-23-edit-connections}

Pour déplacer une connexion entre des étapes, sélectionnez la flèche reliant les deux composants et sélectionnez un autre composant. Pour supprimer la connexion, sélectionnez la flèche puis **Annuler la connexion** dans le pied de page du compositeur Canvas.

Si une seule variante comporte plusieurs branches avec la même audience et le même horaire d'envoi, Braze ne garantit pas une répartition équitable entre ces branches. La répartition peut favoriser la branche créée en premier. Pour une répartition équitable, utilisez des filtres [Numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) sur chaque branche. Pour plus d'informations, consultez [Que se passe-t-il si l'audience et l'horaire d'envoi sont identiques pour un Canvas ayant une variante, mais plusieurs branches ?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches).

## Étape 3 : Ajouter un groupe de contrôle {#step-3-add-a-control-group}

Vous pouvez ajouter un groupe de contrôle à votre Canvas en sélectionnant le bouton plus <i class="fas fa-plus-circle"></i> pour ajouter une nouvelle variante.

Braze suivra les conversions des utilisateurs placés dans le groupe de contrôle, même s'ils ne recevront aucun message. Pour garantir un test précis, nous suivrons le nombre de conversions pour vos variantes et le groupe de contrôle pendant exactement la même durée, comme indiqué sur l'écran de sélection des événements de conversion.

Vous pouvez ajuster la répartition entre vos messages en double-cliquant sur les en-têtes **Nom de la variante**.

Dans cet exemple, notre Canvas est divisé en deux variantes. La variante 1 reçoit 70 % des utilisateurs. La deuxième variante est un groupe de contrôle avec les 30 % d'utilisateurs restants.

![Un exemple de variante dans un Canvas Braze, où 70 % vont vers « Variante 1 », qui impose un délai d'un jour à la première étape, puis envoie un message à la deuxième étape. Les 30 % restants vont vers un « Contrôle » qui ne comporte aucune étape de suivi.]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

### Optimiser les variantes de Canvas avec BrazeAI {#optimize-canvas-variants-with-brazeai}

Pour un Canvas comportant plusieurs variantes de niveau supérieur, activez **Optimize with BrazeAI<sup>TM</sup>** pour ajuster automatiquement le pourcentage d'utilisateurs entrant dans chaque variante. BrazeAI<sup>TM</sup> utilise les performances des variantes pour maximiser le nombre attendu de conversions.

Ajoutez au moins deux variantes et un événement de conversion. Ensuite, sélectionnez un pourcentage de variante pour ouvrir **Edit Variant Distribution** et activez **Optimize with BrazeAI<sup>TM</sup>**.

Après la date limite de conversion initiale, BrazeAI<sup>TM</sup> examine les performances toutes les 12 heures et redirige davantage d'utilisateurs vers la variante qui génère le plus de conversions. Lorsque l'optimisation identifie un gagnant décisif, tous les futurs utilisateurs éligibles entrent dans cette variante.

Cette optimisation fonctionne le mieux pour les Canvas qui accueillent fréquemment de nouveaux utilisateurs.

## Étape 4 : Enregistrer et lancer {#step-4-save-and-launch}

Lorsque vous avez fini de créer votre Canvas, sélectionnez **Lancer le Canvas** pour enregistrer et lancer votre Canvas. Une fois votre Canvas lancé, vous pourrez consulter les analyses de votre parcours au fur et à mesure qu'elles arrivent sur la page **Détails du Canvas**.

Vous pouvez également enregistrer votre Canvas en tant que brouillon si vous devez y revenir ultérieurement.

![Un exemple de Canvas dans Braze.]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
Besoin de modifier votre Canvas après le lancement ? C'est possible ! Consultez [Modifier des Canvas après le lancement]({{site.baseurl}}/post-launch_edits) pour plus d'informations.
{% endalert %}