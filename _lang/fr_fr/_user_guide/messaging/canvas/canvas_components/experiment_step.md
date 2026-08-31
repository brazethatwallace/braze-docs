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

Pour utiliser les Chemins d'expérience, votre Canvas doit inclure des événements de conversion. Bien que vous ne puissiez pas ajouter d'événements de conversion après le lancement d'un Canvas, vous pouvez cloner le Canvas lancé et ajouter des événements de conversion pour intégrer des Chemins d'expérience.

## Cas d'usage {#use-cases}

Les chemins d'expérience sont particulièrement adaptés pour tester la réception, la cadence, le contenu des messages et les combinaisons de canaux.

- **Réception :** Comparez les résultats entre les messages envoyés avec différents [délais]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) temporels, basés sur les actions des utilisateurs ([parcours d'action]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)), et en utilisant le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#step-1-add-intelligent-timing-1).<br><br>
- **Cadence :** Testez plusieurs flux de communication sur une période spécifique. Par exemple, vous pourriez tester deux cadences d'onboarding différentes :
    - Cadence 1 : Envoyer 2 messages au cours des 2 premières semaines de l'utilisateur
    - Cadence 2 : Envoyer 3 messages au cours des 2 premières semaines de l'utilisateur

    Lorsque vous ciblez des utilisateurs inactifs, vous pouvez tester l'efficacité de l'envoi de deux messages de reconquête en une semaine par rapport à un seul envoi.
- **Contenu des messages :** De manière similaire à un [test A/B]({{site.baseurl}}/user_guide/messaging/ab_testing) standard, vous pouvez tester différents contenus de messages pour déterminer quelle formulation génère un taux de conversion plus élevé.<br><br>
- **Combinaisons de canaux :** Testez l'efficacité de différentes combinaisons de canaux de communication. Par exemple, vous pouvez comparer l'impact de l'utilisation d'un e-mail seul par rapport à un e-mail combiné avec une notification push.

## Créer un chemin d'expérience {#creating-an-experiment-path}

Pour créer un composant Chemin d'expérience, commencez par ajouter une étape à votre Canvas. Faites glisser et déposez le composant depuis la barre latérale, ou cliquez sur le bouton plus <i class="fas fa-plus-circle"></i> en bas d'une étape et sélectionnez **Chemins d'expérience**.

Dans la configuration par défaut de ce composant, il y a deux chemins par défaut, **Path 1** et **Path 2**, avec 50 % de l'audience envoyée vers chaque chemin. Cliquez sur le composant pour développer le panneau **Paramètres de l'expérience**, et vous verrez les options de configuration du composant.

### Étape 1 : Choisir le nombre de chemins et la répartition de l'audience {#step-1-choose-the-number-of-paths-and-audience-distribution}

Vous pouvez ajouter jusqu'à quatre chemins en cliquant sur **Add Path** et un groupe de contrôle optionnel en cochant **Add a Control Group**. À l'aide des cases de pourcentage pour chaque chemin, vous pouvez spécifier le pourcentage de l'audience qui doit emprunter chaque chemin et le groupe de contrôle. Les pourcentages fournis doivent totaliser 100 % pour pouvoir continuer. Si vous souhaitez répartir rapidement tous les chemins disponibles (et le groupe de contrôle) avec le même pourcentage, cliquez sur **Distribute Paths Evenly**.

Vous pouvez également choisir si les utilisateurs du groupe de contrôle doivent continuer dans le Canvas ou en sortir après la fenêtre de suivi de conversion pour le **Comportement du groupe de contrôle**. Optionnellement, vous pouvez ajouter une description pour expliquer aux autres ce que ce chemin d'expérience vise à tester ou inclure des informations supplémentaires qui pourraient être utiles à noter.

![Paramètres de l'expérience où vous pouvez ajouter des chemins et répartir le pourcentage d'utilisateurs dans chaque chemin.]({% image_buster /assets/img/experiment_step/exp_settings.png %})

{% alert note %}
Si la rééligibilité au Canvas est activée, les utilisateurs qui entrent dans le Canvas et empruntent un chemin choisi aléatoirement emprunteront le même chemin s'ils redeviennent éligibles et entrent à nouveau dans le Canvas. Cela maintient la validité de l'expérience et des analyses associées. Si vous souhaitez que l'étape randomise toujours l'attribution des chemins, sélectionnez **Chemins aléatoires dans les chemins d'expérience**. Cette option n'est pas disponible lorsque vous utilisez le Chemin gagnant ou les Chemins personnalisés.
{% endalert %}

### Étape 2 : Activer le Chemin gagnant ou les Chemins personnalisés (optionnel) {#step-2}

Vous pouvez choisir d'optimiser votre expérience en activant le [Chemin gagnant]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path) ou les [Chemins personnalisés]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/personalized_paths). Les deux options fonctionnent en testant d'abord vos chemins avec une portion de votre audience. Une fois l'expérience terminée, les utilisateurs restants et suivants sont envoyés vers le chemin le plus performant dans l'ensemble (Chemin gagnant) ou le chemin le plus performant pour chaque utilisateur (Chemins personnalisés).

### Étape 3 : Créer les chemins {#step-3-create-paths}

Enfin, vous devez construire vos chemins en aval. Sélectionnez **Done** et revenez au générateur de Canvas. Cliquez sur le bouton plus <i class="fas fa-plus-circle"></i> sous chaque chemin pour commencer à créer des parcours à l'aide des outils habituels de Canvas, puis lancez le Canvas lorsque vous êtes prêt.

![Ajout d'étapes à chaque chemin qui se divise à partir d'un composant Chemin d'expérience.]({% image_buster /assets/img/experiment_step/experiment_downstream_paths.gif %}){: style="max-width:75%"}

Gardez à l'esprit que les chemins et leurs étapes en aval ne peuvent pas être supprimés d'un Canvas après leur création. Cependant, une fois lancé, vous pouvez modifier la répartition de l'audience entre les chemins comme bon vous semble. Par exemple, si un jour après le lancement d'un Canvas, vous concluez qu'un chemin est supérieur aux autres en fonction des analyses, vous pouvez définir ce chemin à 100 % et les autres à 0 %. Ou, selon vos besoins, vous pouvez continuer à envoyer des utilisateurs vers plusieurs chemins.

{% alert important %}
Pour éviter la contamination de l'expérience, si votre Canvas a une expérience de Chemin gagnant ou de Chemin personnalisé active ou en cours et que vous mettez à jour le Canvas actif, que vous modifiiez ou non l'étape du Chemin d'expérience elle-même, l'expérience en cours prendra fin et l'étape d'expérience ne déterminera pas de chemin gagnant ni de chemins personnalisés. Pour relancer l'expérience, vous pouvez déconnecter le Chemin d'expérience existant et en lancer un nouveau, ou dupliquer le Canvas et lancer un nouveau Canvas. Sinon, les utilisateurs passeront par le chemin d'expérience comme si aucune méthode d'optimisation n'avait été sélectionnée. Vous ne pouvez pas non plus activer les Chemins personnalisés ou le Chemin gagnant pour un Canvas déjà actif comportant une étape de Chemin d'expérience.<br><br>Pour plus d'informations, consultez [Modifier des Canvas après le lancement]({{site.baseurl}}/post-launch_edits).
{% endalert %}

## Suivi des performances {#tracking-performance}

Depuis la page **Canvas Analytics**, sélectionnez le chemin d'expérience pour ouvrir un [tableau détaillé]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch) identique à l'onglet **Analyze Variants** pour comparer les statistiques détaillées de performance et de conversion entre les chemins. Vous pouvez également exporter le tableau au format CSV et comparer les variations en pourcentage des indicateurs qui vous intéressent par rapport au chemin ou au contrôle que vous sélectionnez.

Chaque étape de chaque chemin affiche des statistiques dans la vue [Canvas Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics), comme n'importe quelle étape de Canvas. Cependant, gardez à l'esprit que les analyses au niveau de chaque étape et les analyses du chemin d'expérience mesurent les conversions différemment :

- **Les analyses du chemin d'expérience** comptabilisent les conversions à partir du moment où l'utilisateur entre dans l'étape du chemin d'expérience. C'est la vue recommandée pour comparer les performances entre les chemins, car tous les chemins partagent le même point de départ.
- **Les analyses au niveau de chaque étape** (comme les analyses d'une étape de message) comptabilisent les conversions à partir du moment où l'utilisateur reçoit cette étape spécifique (par exemple, lorsque le message est envoyé).

Étant donné que ces fenêtres de conversion ont des points de départ différents, elles peuvent afficher des taux de conversion différents pour un même chemin, en particulier lorsqu'il y a des délais entre l'étape d'expérience et un message en aval. Pour une comparaison plus fiable entre les chemins, utilisez les analyses du chemin d'expérience.

### Performances du Chemin gagnant et des Chemins personnalisés {#winning-path-and-personalized-paths-performance}

Tirez parti des Chemins gagnants pour suivre les performances sur une période donnée, puis envoyer automatiquement les utilisateurs suivants sur le chemin le plus performant. Pour en savoir plus sur les analyses lorsque le **Chemin gagnant** ou les **Chemins personnalisés** sont activés pour votre expérience, consultez :

- [Chemin gagnant]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path#analytics)
- [Chemins personnalisés]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/personalized_paths#analytics)

L'indicateur gagnant et les analyses affichées dans les chemins d'expérience peuvent différer :

- L'événement de conversion que vous configurez pour le **Chemin gagnant** ou les **Chemins personnalisés** détermine comment Braze compare les chemins et sélectionne un gagnant pendant la fenêtre d'expérience.
- Les analyses du chemin d'expérience suivent le même cadre d'[événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) du Canvas que le reste du Canvas, y compris votre [événement de conversion principal]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events#primary-conversion-event). Par conséquent, les indicateurs mis en avant dans le tableau de bord peuvent ne pas correspondre à l'indicateur gagnant.
- Pour les notifications push, les *ouvertures directes* et les *ouvertures totales* diffèrent. Pour en savoir plus, consultez [Ouvertures influencées]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens).

### Paramètres supplémentaires {#additional-settings}

Les chemins d'expérience enregistrent les utilisateurs qui entrent dans chaque étape et convertissent tout au long du chemin attribué. Cela permet de suivre tous les événements de conversion spécifiés dans la configuration du Canvas. Dans l'onglet **Additional Settings**, saisissez le nombre de jours (entre 1 et 30) pendant lesquels vous souhaitez que cette expérience suive les conversions. La fenêtre temporelle que vous spécifiez ici détermine la durée pendant laquelle les événements de conversion (choisis dans la configuration du Canvas) sont suivis pour l'expérience. Les fenêtres de conversion par événement spécifiées dans la configuration du Canvas ne s'appliquent pas au suivi de cette étape et sont remplacées par cette fenêtre de conversion.

La fenêtre de conversion commence lorsque l'utilisateur entre dans l'étape du chemin d'expérience, et non lorsqu'un message en aval est envoyé. Si un chemin inclut des délais — tels qu'une étape de délai ou le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) — ces délais consomment une partie de la fenêtre de conversion.

{% alert important %}
Si vous utilisez le timing intelligent sur une étape de message au sein d'un chemin d'expérience, le temps écoulé entre l'entrée dans l'expérience et l'envoi effectif du message réduit la fenêtre de conversion effective pour ce chemin. Par exemple, si votre expérience a une fenêtre de conversion de 5 jours et que le timing intelligent retarde le message de 2 jours, les utilisateurs de ce chemin ne disposent que de 3 jours après la réception du message pour convertir dans la fenêtre de l'expérience, même si les analyses propres à l'étape de message comptabilisent les conversions à partir du moment de l'envoi du message.<br><br>Pour des analyses d'expérience plus claires, placez les éventuels délais (tels que les étapes de délai) **avant** l'étape du chemin d'expérience plutôt qu'au sein d'un chemin d'expérience. De cette façon, tous les chemins démarrent au même point et les délais ne consomment aucune partie de la fenêtre de conversion.
{% endalert %}

## Questions fréquentes {#frequently-asked-questions}

### Pourquoi les envois diffèrent-ils d'un chemin à l'autre alors que la répartition de l'expérience semble équilibrée ? {#why-do-sends-differ-across-paths-when-the-experiment-split-looks-even}

Les _envois_ en aval dépendent des étapes, des délais, de l'éligibilité au canal et du contenu de chaque chemin, et non uniquement du pourcentage de répartition au niveau du Chemin d'expérience. Par exemple, des délais différents, des heures d'envoi intelligentes ou le statut d'abonnement peuvent modifier le nombre d'utilisateurs qui reçoivent un message, même lorsque l'affectation aux chemins était équilibrée. Pour comparer les résultats des chemins, utilisez l'[analyse des Chemins d'expérience](#tracking-performance), qui mesure les conversions à partir d'un point d'entrée commun.

### Quelle est la durée de la fenêtre de conversion de l'expérience ? {#how-long-does-the-experiment-conversion-window-last}

La fenêtre de conversion des **Paramètres supplémentaires** (1 à 30 jours) commence lorsque l'utilisateur entre dans l'étape Chemin d'expérience. Le temps passé dans les étapes de délai en aval ou en attente du timing intelligent est décompté de cette fenêtre. Consultez [Suivi des performances](#tracking-performance) pour plus de détails.