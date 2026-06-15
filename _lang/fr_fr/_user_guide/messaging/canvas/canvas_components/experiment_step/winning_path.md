---
nav_title: Chemin gagnant
article_title: Chemin gagnant dans les Chemins d'expérience
page_type: reference
description: "Cet article de référence présente le Chemin gagnant, une fonctionnalité qui vous permet d'automatiser vos tests A/B lorsqu'elle est activée pour une étape de Chemin d'expérience."
tool: Canvas
---

# Chemin gagnant dans les Chemins d'expérience

> Le Chemin gagnant fonctionne de manière similaire à la [variante gagnante]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations/) dans les campagnes, et vous permet d'automatiser vos tests A/B.

Lorsque le Chemin gagnant est activé dans une étape de Chemin d'expérience, après une période définie, tous les utilisateurs suivants sont dirigés vers le chemin ayant le taux de conversion le plus élevé.

## Utiliser le Chemin gagnant

### Étape 1 : Ajouter une étape de Chemin d'expérience

Ajoutez un [Chemin d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/) à votre Canvas, puis activez le **Chemin gagnant**.

![Paramètres du Chemin d'expérience intitulés « Distribuer les utilisateurs suivants vers le Chemin gagnant ». La section comprend un bouton pour activer le Chemin gagnant, ainsi que des options pour configurer l'événement de conversion et la fenêtre d'expérience.]({% image_buster /assets/img/experiment_step/experiment_winning_path_recurring.png %})

### Étape 2 : Configurer les paramètres du Chemin gagnant

Spécifiez l'événement de conversion qui déterminera le gagnant. Si aucun événement de conversion n'est disponible, revenez à la première étape de la configuration du Canvas et [affectez des événements de conversion]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#choose-conversion-events).

Si vous choisissez les ouvertures ou les clics comme événement de conversion, assurez-vous que la première étape du chemin est une [étape de message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/). Braze ne comptabilise l'engagement qu'à partir de la première étape de message dans chaque chemin respectif. Si le chemin commence par une étape différente (comme une étape de délai ou de parcours d'audience) et que le message arrive plus tard, ce message ne sera pas pris en compte lors de l'évaluation des performances.

Ensuite, définissez la **Fenêtre d'expérience**. La **Fenêtre d'expérience** détermine la durée de l'expérience avant que le Chemin gagnant ne soit désigné et que tous les utilisateurs suivants soient dirigés vers ce chemin. La fenêtre commence lorsque le premier utilisateur entre dans l'étape.

![Paramètres du Chemin gagnant avec l'événement de conversion « Clics » sélectionné pour une fenêtre d'expérience de 12 heures.]({% image_buster /assets/img/experiment_step/experiment_winning_settings.png %})

### Étape 3 : Déterminer le comportement par défaut {#statistical-significance}

Par défaut, si les résultats du test ne suffisent pas à déterminer un gagnant statistiquement significatif, tous les futurs utilisateurs sont dirigés vers le chemin le plus performant. Vous pouvez également sélectionner **Continuer à envoyer tous les futurs utilisateurs dans le mix de chemins**. Cette option dirige les futurs utilisateurs vers le mix de chemins selon les pourcentages définis dans la distribution du chemin d'expérience.

En cas d'égalité, Braze sélectionne le chemin qui apparaît en premier.

![« Continuer à envoyer tous les futurs utilisateurs dans le mix de chemins » sélectionné comme comportement à adopter si le résultat du test n'est pas statistiquement significatif.]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

{% alert note %}
Un groupe de délai apparaît dans la distribution de vos chemins uniquement si votre Canvas est configuré pour une entrée unique et que votre étape d'expérience comporte trois chemins ou moins. Les Canvas récurrents et déclenchés ne disposent pas de groupe de délai lorsque le Chemin gagnant est activé.
{% endalert %}

### Étape 4 : Ajouter vos chemins et lancer le Canvas

Un seul composant de Chemin d'expérience peut contenir jusqu'à quatre chemins. Cependant, si votre Canvas est configuré pour une [entrée unique](#one-time-entry), un chemin doit être réservé au groupe de délai que Braze ajoute automatiquement lorsque le Chemin gagnant est activé. Cela signifie que pour les Canvas à entrée unique, vous pouvez ajouter jusqu'à trois chemins à votre expérience.

Terminez la configuration de votre Canvas selon vos besoins, puis lancez-le. Lorsque le premier utilisateur est entré dans l'expérience, vous pouvez consulter le Canvas pour voir les analyses au fur et à mesure et [suivre les performances de votre expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#tracking-performance).

Une fois le Chemin gagnant déterminé, tous les utilisateurs suivants qui entrent dans le Canvas empruntent le Chemin gagnant, y compris les utilisateurs qui sont entrés à nouveau et qui faisaient précédemment partie du groupe de contrôle de l'étape de Chemin d'expérience.

## Analytique {#analytics}

Si le Chemin gagnant est activé, votre vue analytique est séparée en deux onglets : **Expérience initiale** et **Chemin gagnant**.

- **Expérience initiale :** Affiche les indicateurs de chaque chemin pendant la fenêtre d'expérience, le chemin sélectionné comme gagnant et les indicateurs de conversion du Canvas. L'événement de conversion utilisé pour désigner le gagnant, configuré dans les paramètres du Chemin gagnant, peut différer de l'indicateur de conversion mis en avant dans l'analytique du Canvas. Pour en savoir plus sur la relation entre l'analytique des Chemins d'expérience, les événements de conversion du Canvas et l'indicateur gagnant, consultez [Chemins d'expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#winning-path-and-personalized-paths-performance).
- **Chemin gagnant :** Affiche uniquement les indicateurs du Chemin gagnant à partir du moment où l'expérience initiale s'est terminée.

## Bon à savoir

### Entrée unique {#one-time-entry}

Lorsque vous utilisez les Chemins gagnants dans un Canvas où les utilisateurs ne peuvent entrer qu'une seule fois, un groupe de délai est automatiquement inclus. Pendant la durée de l'expérience, un pourcentage d'utilisateurs est maintenu dans le groupe de délai tandis que les utilisateurs restants entrent dans vos Chemins d'expérience.

![Étape d'expérience avec un groupe de délai pour le Chemin gagnant]({% image_buster /assets/img/experiment_step/experiment_one_time.png %}){: style="max-width:75%"}

Lorsque le test est terminé et qu'un Chemin gagnant est déterminé, les utilisateurs affectés au groupe de délai sont dirigés vers le chemin choisi et poursuivent leur parcours dans le Canvas.

![Étape d'expérience avec un groupe de délai dirigé vers le Chemin gagnant]({% image_buster /assets/img/experiment_step/experiment_one_time_results.png %}){: style="max-width:75%"}

### Diffusion selon l'heure locale

Nous déconseillons d'utiliser la diffusion selon l'heure locale dans les Canvas avec des Chemins gagnants. En effet, les fenêtres d'expérience commencent lorsque le premier utilisateur passe par l'étape. Les utilisateurs situés dans des fuseaux horaires très en avance peuvent entrer dans l'étape et déclencher le début de la fenêtre d'expérience bien plus tôt que prévu, ce qui peut entraîner la fin de l'expérience avant que la majorité de vos utilisateurs dans des fuseaux horaires plus courants n'aient eu suffisamment de temps pour entrer dans le Canvas, convertir, ou les deux.

Si vous souhaitez tout de même utiliser la diffusion selon l'heure locale, optez pour une fenêtre d'expérience de 24 à 48 heures ou plus. Ainsi, les utilisateurs dans les fuseaux horaires en avance entrent dans le Canvas et déclenchent le début de l'expérience, mais il reste suffisamment de temps dans la fenêtre d'expérience. Les utilisateurs dans les fuseaux horaires plus tardifs disposent encore d'assez de temps pour entrer dans le Canvas et dans l'étape d'expérience avec les Chemins gagnants, et éventuellement convertir avant l'expiration de la fenêtre d'expérience.

### Variantes basées sur les clics

Si vous configurez une variante de Chemin gagnant basée sur les clics, notez que les définitions des ouvertures et des clics diffèrent selon le canal. Pour connaître les indicateurs et définitions spécifiques par canal, consultez le [Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics) et le [Glossaire des indicateurs de rapport e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary).