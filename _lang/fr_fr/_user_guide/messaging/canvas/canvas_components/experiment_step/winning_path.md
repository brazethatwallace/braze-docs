---
nav_title: Chemin gagnant
article_title: Chemin gagnant dans les chemins d'expérience
page_type: reference
description: "Cet article de référence présente le Chemin gagnant, une fonctionnalité qui vous permet d'automatiser vos tests A/B lorsqu'elle est activée pour une étape de chemin d'expérience."
tool: Canvas
---

# Chemin gagnant dans les chemins d'expérience {#winning-path-in-experiment-paths}

> Le Chemin gagnant teste automatiquement les chemins d'un Canvas et dirige les utilisateurs suivants vers le chemin le plus performant.

Lorsque le Chemin gagnant est activé dans une étape de chemin d'expérience, après une période définie, tous les utilisateurs suivants sont dirigés vers le chemin ayant le taux de conversion le plus élevé.

## Utiliser le chemin gagnant {#using-winning-path}

### Étape 1 : Ajouter une étape de chemin d'expérience {#step-1-add-an-experiment-path-step}

Ajoutez un [chemin d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) à votre Canvas, puis activez **Chemin gagnant**.

![Paramètres du chemin d'expérience intitulés « Distribuer les utilisateurs suivants vers le chemin gagnant ». La section comprend une bascule pour le chemin gagnant, ainsi que des options pour configurer l'événement de conversion et la fenêtre d'expérience.]({% image_buster /assets/img/experiment_step/experiment_winning_path_recurring.png %})

### Étape 2 : Configurer les paramètres du chemin gagnant {#step-2-configure-winning-path-settings}

Spécifiez l'événement de conversion qui doit déterminer le gagnant. Si aucun événement de conversion n'est disponible, revenez à la première étape de la configuration du Canvas et [attribuez des événements de conversion]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#choose-conversion-events).

Si vous choisissez les ouvertures ou les clics comme événement de conversion, assurez-vous que la première étape du parcours est une [étape de message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step). Braze ne comptabilise l'engagement qu'à partir de la première étape de message dans chaque parcours respectif. Si le parcours commence par une étape différente (comme une étape de délai ou de parcours d'audience) et que le message arrive plus tard, ce message ne sera pas pris en compte lors de l'évaluation des performances.

Ensuite, définissez la **fenêtre d'expérience**. La **fenêtre d'expérience** spécifie la durée de l'expérience avant que le chemin gagnant ne soit déterminé et que tous les utilisateurs suivants soient envoyés sur ce parcours. La fenêtre commence lorsque le premier utilisateur entre dans l'étape.

![Paramètres du chemin gagnant avec l'événement de conversion « Clics » sélectionné pour une fenêtre d'expérience de 12 heures.]({% image_buster /assets/img/experiment_step/experiment_winning_settings.png %})

### Étape 3 : Déterminer le comportement de secours {#statistical-significance}

Par défaut, si les résultats du test ne suffisent pas à déterminer un gagnant statistiquement significatif, tous les futurs utilisateurs sont envoyés sur le parcours le plus performant. Vous pouvez également sélectionner **Continuer à envoyer tous les futurs utilisateurs sur le mix de parcours**. Cette option envoie les futurs utilisateurs sur le mix de parcours selon les pourcentages spécifiés dans la distribution du chemin d'expérience.

En cas d'égalité, Braze sélectionne le parcours qui apparaît en premier.

![« Continuer à envoyer tous les futurs utilisateurs sur le mix de parcours » sélectionné comme comportement lorsque le résultat du test n'est pas statistiquement significatif.]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

{% alert note %}
Un groupe de délai apparaît dans votre distribution de parcours uniquement si votre Canvas est configuré pour une entrée unique et que votre étape d'expérience comporte trois parcours ou moins. Les Canvas récurrents et déclenchés n'ont pas de groupe de délai lorsque le chemin gagnant est activé.
{% endalert %}

### Étape 4 : Ajouter vos parcours et lancer le Canvas {#step-4-add-your-paths-and-launch-the-canvas}

Un seul composant de chemin d'expérience peut contenir jusqu'à quatre parcours. Cependant, si votre Canvas est configuré pour une [entrée unique](#one-time-entry), un parcours doit être réservé au groupe de délai que Braze ajoute automatiquement lorsque le chemin gagnant est activé. Cela signifie que pour les Canvas avec entrée unique, vous pouvez ajouter jusqu'à trois parcours à votre expérience.

Terminez la configuration de votre Canvas selon vos besoins, puis lancez-le. Lorsque le premier utilisateur est entré dans l'expérience, vous pouvez consulter le Canvas pour voir les analyses au fur et à mesure qu'elles arrivent et [suivre les performances de votre expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#tracking-performance).

Une fois qu'un chemin gagnant est déterminé, tous les utilisateurs suivants qui entrent dans le Canvas empruntent le chemin gagnant, y compris les utilisateurs qui sont entrés à nouveau et qui faisaient précédemment partie du groupe de contrôle de l'étape de chemin d'expérience.

## Analytique {#analytics}

Si le Chemin gagnant est activé, votre vue analytique est séparée en deux onglets : **Expérience initiale** et **Chemin gagnant**.

- **Expérience initiale :** Affiche les indicateurs de chaque chemin pendant la fenêtre d'expérience, le chemin sélectionné comme gagnant et les indicateurs de conversion du Canvas. L'événement de conversion utilisé pour désigner le gagnant, configuré dans les paramètres du Chemin gagnant, peut différer de l'indicateur de conversion mis en avant dans l'analytique du Canvas. Pour en savoir plus sur la relation entre l'analytique des Chemins d'expérience, les événements de conversion du Canvas et l'indicateur gagnant, consultez [Chemins d'expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step#winning-path-and-personalized-paths-performance).
- **Chemin gagnant :** Affiche uniquement les indicateurs du Chemin gagnant à partir du moment où l'expérience initiale s'est terminée.

## Points importants {#things-to-know}

### Entrée unique {#one-time-entry}

Lorsque vous utilisez les chemins gagnants dans un Canvas où les utilisateurs ne peuvent entrer qu'une seule fois, un groupe de délai est automatiquement inclus. Pendant la durée de l'expérience, un pourcentage d'utilisateurs est retenu dans le groupe de délai tandis que les utilisateurs restants entrent dans vos chemins d'expérience.

![Étape d'expérience avec un groupe de délai pour le chemin gagnant]({% image_buster /assets/img/experiment_step/experiment_one_time.png %}){: style="max-width:75%"}

Lorsque le test est terminé et qu'un chemin gagnant est déterminé, les utilisateurs assignés au groupe de délai sont dirigés vers le chemin choisi et continuent à travers le Canvas.

![Étape d'expérience avec un groupe de délai envoyé vers le chemin gagnant]({% image_buster /assets/img/experiment_step/experiment_one_time_results.png %}){: style="max-width:75%"}

### Diffusion selon l'heure locale {#local-time-delivery}

Nous ne recommandons pas d'utiliser la diffusion selon l'heure locale dans les Canvas avec des chemins gagnants. En effet, les fenêtres d'expérience commencent lorsque le premier utilisateur passe par l'étape. Les utilisateurs qui se trouvent dans des fuseaux horaires très en avance peuvent entrer dans l'étape et déclencher le début de la fenêtre d'expérience bien plus tôt que prévu, ce qui peut entraîner la conclusion de l'expérience avant que la majorité de vos utilisateurs dans des fuseaux horaires plus courants n'aient eu suffisamment de temps pour entrer dans le Canvas ou convertir, voire les deux.

Alternativement, si vous souhaitez utiliser la diffusion selon l'heure locale, utilisez une fenêtre d'expérience de 24 à 48 heures ou plus. Ainsi, les utilisateurs dans les fuseaux horaires en avance entrent dans le Canvas et déclenchent le début de l'expérience, mais il reste suffisamment de temps dans la fenêtre d'expérience. Les utilisateurs dans les fuseaux horaires plus tardifs disposent encore d'assez de temps pour entrer dans le Canvas et dans l'étape d'expérience avec les chemins gagnants, et éventuellement convertir avant l'expiration de la fenêtre d'expérience.

### Variantes basées sur les clics {#variants-based-on-clicks}

Si vous configurez une variante de chemin gagnant basée sur les clics, notez que les définitions des ouvertures et des clics diffèrent selon le canal. Pour les indicateurs et définitions spécifiques par canal, consultez le [Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/analytics/metrics_glossary) et le [Glossaire des indicateurs de rapport e-mail]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary).