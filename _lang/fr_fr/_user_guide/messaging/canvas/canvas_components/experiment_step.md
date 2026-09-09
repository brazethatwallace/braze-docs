---
nav_title: Chemins d'expérience
article_title: Chemins d'expérience
alias: /experiment_step/
page_order: 4
page_type: reference
description: "Cet article présente les Chemins d'expérience, un composant qui vous permet de tester plusieurs parcours Canvas les uns par rapport aux autres et par rapport à un groupe de contrôle, à n'importe quel moment du parcours utilisateur."
tool: Canvas
---

# Chemins d'expérience {#experiment-paths}

> Les Chemins d'expérience vous permettent de tester plusieurs parcours Canvas les uns par rapport aux autres et par rapport à un groupe de contrôle, à n'importe quel moment du parcours utilisateur. Grâce à ce composant, vous pouvez suivre les performances de chaque parcours pour prendre des décisions éclairées concernant votre Canvas.

Lorsque vous incluez une étape des Chemins d'expérience dans votre parcours utilisateur, elle affecte aléatoirement les utilisateurs aux différents parcours (ou à un groupe de contrôle facultatif) que vous créez. Des portions de l'audience sont affectées aux différents parcours selon les pourcentages que vous définissez, ce qui vous permet de tester différents messages ou parcours les uns par rapport aux autres et de déterminer lequel est le plus efficace.

![Une étape de chemin d'expérience qui se divise en Parcours 1, Parcours 2 et Contrôle.]({% image_buster /assets/img/experiment_step/experiment_step.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

## Prérequis {#prerequisites}

Pour utiliser les chemins d'expérience, votre Canvas doit inclure des événements de conversion. Bien que vous ne puissiez pas ajouter d'événements de conversion après le lancement d'un Canvas, vous pouvez cloner le Canvas lancé et ajouter des événements de conversion pour inclure des chemins d'expérience.

## Cas d'usage {#use-cases}

Les chemins d'expérience sont particulièrement adaptés pour tester la réception, la cadence, le contenu des messages et les combinaisons de canaux.

- **Réception :** Comparez les résultats entre des messages envoyés avec différents [délais]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) temporels, basés sur les actions des utilisateurs ([parcours d'action]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)), et en utilisant le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#step-1-add-intelligent-timing-1).<br><br>
- **Cadence :** Testez plusieurs flux de communication sur une période donnée. Par exemple, vous pourriez tester deux cadences d'onboarding différentes :
    - Cadence 1 : Envoyer 2 messages au cours des 2 premières semaines de l'utilisateur
    - Cadence 2 : Envoyer 3 messages au cours des 2 premières semaines de l'utilisateur

    Lorsque vous ciblez des utilisateurs sur le point de devenir inactifs, vous pouvez tester l'efficacité de l'envoi de deux messages de reconquête en une semaine par rapport à l'envoi d'un seul.
- **Contenu des messages :** Comme pour un [test A/B]({{site.baseurl}}/user_guide/messaging/ab_testing) standard, vous pouvez tester différentes formulations de messages pour identifier celle qui génère le taux de conversion le plus élevé.<br><br>
- **Combinaisons de canaux :** Testez l'efficacité de différentes combinaisons de canaux de communication. Par exemple, vous pouvez comparer l'impact d'un e-mail seul par rapport à un e-mail combiné à une notification push.

## Créer un chemin d'expérience {#creating-an-experiment-path}

Pour créer un composant Chemins d'expérience, commencez par ajouter une étape à votre Canvas. Glissez-déposez le composant depuis la barre latérale, ou cliquez sur le bouton <i class="fas fa-plus-circle"></i> plus en bas d'une étape et sélectionnez **Chemins d'expérience**.

Dans la configuration par défaut de ce composant, il existe deux chemins par défaut, **Path 1** et **Path 2**, avec 50 % de l'audience envoyée dans chaque chemin. Cliquez sur le composant pour développer le panneau **Experiment Settings**, et vous verrez les options de configuration du composant.

### Étape 1 : Choisir le nombre de chemins et la répartition de l'audience {#step-1-choose-the-number-of-paths-and-audience-distribution}

Vous pouvez ajouter jusqu'à quatre chemins en cliquant sur **Add Path** et un groupe de contrôle optionnel en cochant **Add a Control Group**. À l'aide des champs de pourcentage pour chaque chemin, vous pouvez spécifier le pourcentage de l'audience qui doit emprunter chaque chemin et le groupe de contrôle. Les pourcentages fournis doivent totaliser 100 % pour continuer. Si vous souhaitez rapidement attribuer le même pourcentage à tous les chemins disponibles (et au groupe de contrôle), cliquez sur **Distribute Paths Evenly**.

Vous pouvez également choisir si les utilisateurs du groupe de contrôle doivent continuer dans le Canvas ou en sortir après la fenêtre de suivi des conversions pour le **Control Group Behavior**. Vous pouvez également ajouter une description pour expliquer aux autres ce que ce chemin d'expérience a pour objectif de tester ou inclure des informations supplémentaires qui pourraient être utiles à noter.

![Paramètres d'expérience où vous pouvez ajouter des chemins et répartir le pourcentage d'utilisateurs dans chaque chemin.]({% image_buster /assets/img/experiment_step/exp_settings.png %})

{% alert note %}
Si la rééligibilité au Canvas est activée, les utilisateurs qui entrent dans le Canvas et empruntent un chemin choisi aléatoirement empruntent le même chemin s'ils redeviennent éligibles et entrent à nouveau dans le Canvas. Cela maintient la validité de l'expérience et des analyses associées. Pour randomiser l'attribution du chemin à chaque nouvelle entrée des utilisateurs, sélectionnez **Randomized Paths in Experiment Paths**. Cette option n'est pas disponible lors de l'utilisation du Chemin gagnant.
{% endalert %}

### Étape 2 : Activer le Chemin gagnant (optionnel) {#step-2}

Pour optimiser votre expérience, activez le [Chemin gagnant]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path). Le Chemin gagnant teste initialement vos chemins avec une partie de l'audience. Une fois l'expérience terminée, Braze envoie les utilisateurs restants et suivants sur le chemin le plus performant.

{% alert note %}
Les Chemins personnalisés ne sont pas disponibles pour les nouvelles étapes de Chemin d'expérience. Les étapes existantes qui utilisent les Chemins personnalisés continuent de fonctionner.
{% endalert %}

### Étape 3 : Créer les chemins {#step-3-create-paths}

Enfin, vous devez construire vos chemins en aval. Sélectionnez **Done** et revenez au générateur de Canvas. Cliquez sur le bouton <i class="fas fa-plus-circle"></i> plus sous chaque chemin pour commencer à créer des parcours à l'aide des outils Canvas habituels selon vos besoins, et lancez le Canvas lorsque vous êtes prêt.

![Ajout d'étapes à chaque chemin qui se ramifie à partir d'un composant Chemin d'expérience.]({% image_buster /assets/img/experiment_step/experiment_downstream_paths.gif %}){: style="max-width:75%"}

Gardez à l'esprit que les chemins et leurs étapes en aval ne peuvent pas être supprimés d'un Canvas après leur création. Cependant, une fois lancé, vous pouvez modifier la répartition de l'audience entre les chemins selon vos besoins. Par exemple, si un jour après le lancement d'un Canvas, vous concluez qu'un chemin est supérieur aux autres en vous basant sur les analyses, vous pouvez définir ce chemin à 100 % et les autres à 0 %. Ou, en fonction de vos besoins, vous pouvez continuer à envoyer des utilisateurs sur plusieurs chemins.

{% alert important %}
Pour éviter la contamination de l'expérience, la mise à jour d'un Canvas actif avec une expérience de Chemin gagnant en cours met fin à l'expérience. Cela s'applique même si vous ne mettez pas à jour l'étape du Chemin d'expérience. Pour relancer l'expérience, déconnectez le Chemin d'expérience existant et lancez-en un nouveau, ou dupliquez le Canvas et lancez le duplicata. Vous ne pouvez pas activer le Chemin gagnant pour un Canvas déjà actif avec une étape de Chemin d'expérience.<br><br>Pour plus d'informations, consultez [Modifier les Canvas après le lancement]({{site.baseurl}}/post-launch_edits).
{% endalert %}

## Suivi des performances {#tracking-performance}

Depuis la page **Canvas Analytics**, sélectionnez le chemin d'expérience pour ouvrir un [tableau détaillé]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch) identique à l'onglet **Analyze Variants** afin de comparer les performances détaillées et les statistiques de conversion entre les chemins. Vous pouvez également exporter le tableau au format CSV et comparer les variations en pourcentage des indicateurs qui vous intéressent par rapport au chemin ou au groupe de contrôle que vous sélectionnez.

Chaque étape de chaque chemin affiche des statistiques dans la vue [Canvas Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics), comme n'importe quelle étape Canvas. Cependant, gardez à l'esprit que les analyses des étapes individuelles et les analyses des chemins d'expérience mesurent les conversions différemment :

- **Les analyses des chemins d'expérience** comptabilisent les conversions à partir du moment où l'utilisateur entre dans l'étape du chemin d'expérience. C'est la vue recommandée pour comparer les performances entre les chemins, car tous les chemins partagent le même point de départ.
- **Les analyses des étapes individuelles** (comme les analyses d'une étape Message) comptabilisent les conversions à partir du moment où l'utilisateur reçoit cette étape spécifique (par exemple, quand le message est envoyé).

Comme ces fenêtres de conversion ont des points de départ différents, elles peuvent afficher des taux de conversion différents pour un même chemin, en particulier lorsqu'il y a des délais entre l'étape d'expérience et un message en aval. Pour la comparaison la plus fiable entre les chemins, utilisez les analyses des chemins d'expérience.

### Performance du chemin gagnant {#winning-path-performance}

Utilisez le chemin gagnant pour suivre les performances au fil du temps et envoyer automatiquement les utilisateurs suivants sur le chemin le plus performant. Pour plus d'informations, consultez [Analyses du chemin gagnant]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path#analytics).

L'indicateur gagnant et les analyses affichées dans les chemins d'expérience peuvent différer :

- L'événement de conversion que vous configurez pour le **Chemin gagnant** détermine la manière dont Braze compare les chemins et sélectionne un gagnant pendant la fenêtre d'expérience.
- Les analyses des chemins d'expérience suivent le même cadre d'[événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) Canvas que le reste du Canvas, y compris votre [événement de conversion principal]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#primary-conversion-event). Par conséquent, les indicateurs mis en avant dans le tableau de bord peuvent ne pas correspondre à l'indicateur gagnant.
- Pour les notifications push, les *ouvertures directes* et les *ouvertures totales* diffèrent. Pour plus d'informations, consultez [Ouvertures influencées]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens).

### Paramètres supplémentaires {#additional-settings}

Les chemins d'expérience enregistrent les utilisateurs qui entrent dans chaque étape et convertissent pendant qu'ils se trouvent sur le chemin assigné. Cela comptabilise tous les événements de conversion spécifiés dans la configuration du Canvas. Dans l'onglet **Additional Settings**, indiquez le nombre de jours (entre 1 et 30) pendant lesquels vous souhaitez que cette expérience suive les conversions. La fenêtre temporelle que vous spécifiez ici détermine la durée pendant laquelle les événements de conversion (choisis dans la configuration du Canvas) sont suivis pour l'expérience. Les fenêtres de conversion par événement spécifiées dans la configuration du Canvas ne s'appliquent pas au suivi de cette étape et sont remplacées par cette fenêtre de conversion.

La fenêtre de conversion commence lorsque l'utilisateur entre dans l'étape du chemin d'expérience, et non lorsqu'un message en aval est envoyé. Si un chemin inclut des délais, comme une étape de délai ou le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing), ces délais consomment une partie de la fenêtre de conversion.

{% alert important %}
Si vous utilisez le timing intelligent sur une étape Message au sein d'un chemin d'expérience, le temps écoulé entre l'entrée dans l'expérience et l'envoi effectif du message réduit la fenêtre de conversion effective pour ce chemin. Par exemple, si votre expérience a une fenêtre de conversion de 5 jours et que le timing intelligent retarde le message de 2 jours, les utilisateurs de ce chemin ne disposent que de 3 jours après la réception du message pour convertir dans la fenêtre d'expérience, même si les analyses propres à l'étape Message comptabilisent les conversions à partir du moment de l'envoi du message.<br><br>Pour des analyses d'expérience plus claires, placez les délais éventuels (comme les étapes de délai) **avant** l'étape du chemin d'expérience plutôt qu'à l'intérieur d'un chemin d'expérience. De cette façon, tous les chemins partent du même point et les délais ne consomment aucune partie de la fenêtre de conversion.
{% endalert %}

## Questions fréquemment posées {#frequently-asked-questions}

### Pourquoi les envois diffèrent-ils entre les chemins alors que la répartition de l'expérience semble équitable ? {#why-do-sends-differ-across-paths-when-the-experiment-split-looks-even}

Les _envois_ en aval dépendent des étapes, des délais, de l'éligibilité aux canaux et du contenu de chaque chemin, et pas uniquement du pourcentage de répartition au niveau du chemin d'expérience. Par exemple, des délais différents, le timing intelligent ou le statut d'abonnement peuvent modifier le nombre d'utilisateurs qui reçoivent un message, même lorsque l'attribution des chemins était équilibrée. Pour comparer les résultats des chemins, utilisez l'[analyse du chemin d'expérience](#tracking-performance), qui mesure les conversions à partir d'un point d'entrée commun.

### Quelle est la durée de la fenêtre de conversion de l'expérience ? {#how-long-does-the-experiment-conversion-window-last}

La fenêtre de conversion dans les **Additional Settings** (1 à 30 jours) commence lorsque l'utilisateur entre dans l'étape de chemin d'expérience. Le temps passé dans les étapes de délai en aval ou en attente du timing intelligent est décompté de cette fenêtre. Consultez [Suivi des performances](#tracking-performance) pour plus de détails.