---
nav_title: Chemins d'expérience
article_title: Chemins d'expérience
alias: /experiment_step/
page_order: 4
page_type: reference
description: "Cet article présente les chemins d'expérience, un composant qui vous permet de tester plusieurs parcours Canvas les uns par rapport aux autres et par rapport à un groupe de contrôle, à n'importe quel moment du parcours utilisateur."
tool: Canvas
---

# Chemins d'expérience

> Les chemins d'expérience vous permettent de tester plusieurs parcours Canvas les uns par rapport aux autres et par rapport à un groupe de contrôle, à n'importe quel moment du parcours utilisateur. Grâce à ce composant, vous pouvez suivre les performances de chaque parcours pour prendre des décisions éclairées concernant votre Canvas.

Lorsque vous incluez une étape des chemins d'expérience dans votre parcours utilisateur, elle affecte aléatoirement les utilisateurs aux différents parcours (ou à un groupe de contrôle facultatif) que vous créez. Des portions de l'audience sont affectées aux différents parcours selon les pourcentages que vous définissez, ce qui vous permet de tester différents messages ou parcours les uns par rapport aux autres et de déterminer lequel est le plus efficace.

![Une étape de chemin d'expérience qui se divise en Parcours 1, Parcours 2 et Contrôle.]({% image_buster /assets/img/experiment_step/experiment_step.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

## Conditions préalables

Pour utiliser les chemins d'expérience, votre Canvas doit inclure des événements de conversion. Bien que vous ne puissiez pas ajouter d'événements de conversion après le lancement d'un Canvas, vous pouvez cloner le Canvas lancé et y ajouter des événements de conversion pour intégrer des chemins d'expérience.

## Cas d'utilisation

Les chemins d'expérience sont particulièrement adaptés pour tester la réception, la cadence, le contenu des messages et les combinaisons de canaux.

- **Réception :** Comparez les résultats entre des messages envoyés avec différents [délais]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step/), basés sur les actions des utilisateurs ([Parcours d'actions]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths/)), et en utilisant le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#canvas).<br><br>
- **Cadence :** Testez plusieurs flux de messages sur une période donnée. Par exemple, vous pourriez tester deux cadences d'onboarding différentes :
    - Cadence 1 : Envoyer 2 messages pendant les 2 premières semaines de l'utilisateur
    - Cadence 2 : Envoyer 3 messages pendant les 2 premières semaines de l'utilisateur
    
    Pour cibler les utilisateurs inactifs, vous pouvez tester l'efficacité de l'envoi de deux messages de reconquête en une semaine par rapport à un seul message.
- **Contenu des messages :** De manière similaire à un [test A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/) standard, vous pouvez tester différents contenus de messages pour déterminer quelle formulation génère un taux de conversion plus élevé.<br><br>
- **Combinaisons de canaux :** Testez l'efficacité de différentes combinaisons de canaux de messages. Par exemple, vous pouvez comparer l'impact d'un e-mail seul par rapport à un e-mail combiné avec une notification push.

## Créer un chemin d'expérience

Pour créer un composant de chemins d'expérience, commencez par ajouter une étape à votre Canvas. Glissez-déposez le composant depuis la barre latérale, ou cliquez sur le bouton <i class="fas fa-plus-circle"></i> plus en bas d'une étape et sélectionnez **Chemins d'expérience**.

Dans la configuration par défaut de ce composant, il y a deux parcours par défaut, **Parcours 1** et **Parcours 2**, avec 50 % de l'audience envoyée dans chaque parcours. Cliquez sur le composant pour développer le panneau **Paramètres de l'expérience**, et vous verrez les options de configuration du composant.

### Étape 1 : Choisir le nombre de parcours et la répartition de l'audience

Vous pouvez ajouter jusqu'à quatre parcours en cliquant sur **Ajouter un parcours** et un groupe de contrôle facultatif en cochant **Ajouter un groupe de contrôle**. À l'aide des champs de pourcentage pour chaque parcours, vous pouvez spécifier le pourcentage de l'audience qui doit emprunter chaque parcours et le groupe de contrôle. Les pourcentages fournis doivent totaliser 100 % pour pouvoir continuer. Si vous souhaitez répartir rapidement tous les parcours disponibles (et le contrôle) de manière égale, cliquez sur **Répartir les parcours équitablement**.

Vous pouvez également choisir si les utilisateurs du groupe de contrôle doivent continuer dans le Canvas ou en sortir après la fenêtre de suivi des conversions pour le **Comportement du groupe de contrôle**. Vous pouvez aussi ajouter une description pour expliquer aux autres ce que ce chemin d'expérience vise à tester ou inclure des informations supplémentaires utiles.

![Paramètres de l'expérience où vous pouvez ajouter des parcours et répartir le pourcentage d'utilisateurs dans chaque parcours.]({% image_buster /assets/img/experiment_step/exp_settings.png %})

{% alert note %}
Si la rééligibilité au Canvas est activée, les utilisateurs qui entrent dans le Canvas et empruntent un parcours choisi aléatoirement emprunteront le même parcours s'ils redeviennent éligibles et réintègrent le Canvas. Cela préserve la validité de l'expérience et des analyses associées. Si vous souhaitez que l'étape randomise toujours l'affectation des parcours, sélectionnez **Parcours aléatoires dans les chemins d'expérience**. Cette option n'est pas disponible lorsque vous utilisez les parcours gagnants ou personnalisés.
{% endalert %}

### Étape 2 : Activer le parcours gagnant ou les parcours personnalisés (facultatif) {#step-2}

Vous pouvez choisir d'optimiser votre expérience en activant le [parcours gagnant]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path) ou les [parcours personnalisés]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/personalized_paths). Ces deux options fonctionnent en testant d'abord vos parcours avec une portion de votre audience. Une fois l'expérience terminée, les utilisateurs restants et suivants sont envoyés dans le parcours le plus performant globalement (parcours gagnant) ou dans le parcours le plus performant pour chaque utilisateur (parcours personnalisés).

### Étape 3 : Créer les parcours

Enfin, vous devez construire vos parcours en aval. Sélectionnez **Terminé** et revenez au générateur de Canvas. Cliquez sur le bouton <i class="fas fa-plus-circle"></i> plus sous chaque parcours pour commencer à créer des parcours en utilisant les outils Canvas habituels selon vos besoins, puis lancez le Canvas lorsque vous êtes prêt.

![Ajout d'étapes à chaque parcours qui se divise à partir d'un composant de chemin d'expérience.]({% image_buster /assets/img/experiment_step/experiment_downstream_paths.gif %}){: style="max-width:75%"}

Gardez à l'esprit que les parcours et leurs étapes en aval ne peuvent pas être supprimés d'un Canvas après leur création. Cependant, une fois le Canvas lancé, vous pouvez modifier la répartition de l'audience entre les parcours comme vous le souhaitez. Par exemple, si un jour après le lancement d'un Canvas, vous concluez qu'un parcours est supérieur aux autres sur la base des analyses, vous pouvez définir ce parcours à 100 % et les autres à 0 %. Ou, selon vos besoins, vous pouvez continuer à envoyer des utilisateurs dans plusieurs parcours.

{% alert important %}
Pour éviter la contamination de l'expérience, si votre Canvas a une expérience de parcours gagnant ou de parcours personnalisés active ou en cours et que vous mettez à jour le Canvas actif, que vous modifiiez ou non l'étape des chemins d'expérience elle-même, l'expérience en cours prendra fin et l'étape d'expérience ne déterminera pas de parcours gagnant ni de parcours personnalisés. Pour relancer l'expérience, vous pouvez déconnecter le chemin d'expérience existant et en lancer un nouveau, ou dupliquer le Canvas et lancer un nouveau Canvas. Sinon, les utilisateurs passeront par le chemin d'expérience comme si aucune méthode d'optimisation n'avait été sélectionnée. Vous ne pouvez pas non plus activer les parcours personnalisés ou le parcours gagnant pour un Canvas déjà actif avec une étape des chemins d'expérience.<br><br>Pour en savoir plus, consultez [Modifier les Canvas après le lancement]({{site.baseurl}}/post-launch_edits/).
{% endalert %}

## Suivi des performances

Depuis la page **Analyse du Canvas**, sélectionnez le chemin d'expérience pour ouvrir un [tableau détaillé]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch/#performance-breakdown-by-variant) identique à l'onglet **Analyser les variantes** pour comparer les performances détaillées et les statistiques de conversion entre les parcours. Vous pouvez également exporter le tableau au format CSV et comparer les variations en pourcentage pour les indicateurs qui vous intéressent par rapport au parcours ou au contrôle que vous sélectionnez.

Chaque étape de chaque parcours affiche des statistiques dans la vue [Analyse du Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/), comme n'importe quelle étape de Canvas. Cependant, gardez à l'esprit que les analyses des étapes individuelles et les analyses des chemins d'expérience mesurent les conversions différemment :

- **Analyses des chemins d'expérience** : les conversions sont comptabilisées à partir du moment où l'utilisateur entre dans l'étape des chemins d'expérience. C'est la vue recommandée pour comparer les performances entre les parcours, car tous les parcours partagent le même point de départ.
- **Analyses des étapes individuelles** (comme les analyses d'une étape de message) : les conversions sont comptabilisées à partir du moment où l'utilisateur reçoit cette étape spécifique (par exemple, lorsque le message est envoyé).

Comme ces fenêtres de conversion ont des points de départ différents, elles peuvent afficher des taux de conversion différents pour le même parcours, en particulier lorsqu'il y a des délais entre l'étape d'expérience et un message en aval. Pour la comparaison la plus fiable entre les parcours, utilisez les analyses des chemins d'expérience.

### Performances du parcours gagnant et des parcours personnalisés

Tirez parti des parcours gagnants pour suivre les performances sur une période donnée, puis envoyer automatiquement les utilisateurs suivants dans le parcours le plus performant. Pour en savoir plus sur les analyses lorsque le **parcours gagnant** ou les **parcours personnalisés** sont activés pour votre expérience, consultez :

- [Parcours gagnant]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path/#analytics)
- [Parcours personnalisés]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/personalized_paths/#analytics)

L'indicateur gagnant et les analyses affichées dans les chemins d'expérience peuvent différer :

- L'événement de conversion que vous configurez pour le **parcours gagnant** ou les **parcours personnalisés** détermine comment Braze compare les parcours et sélectionne un gagnant pendant la fenêtre d'expérience.
- Les analyses des chemins d'expérience suivent le même cadre d'[événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) du Canvas que le reste du Canvas, y compris votre [événement de conversion principal]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/#primary-conversion-event). Par conséquent, les indicateurs mis en avant dans le tableau de bord peuvent ne pas correspondre à l'indicateur gagnant.
- Pour les notifications push, les *Ouvertures directes* et les *ouvertures totales* diffèrent. Pour en savoir plus, consultez [Ouvertures influencées]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/).

### Paramètres supplémentaires

Les chemins d'expérience enregistrent les utilisateurs qui entrent dans chaque étape et convertissent dans le parcours qui leur est affecté. Cela suit tous les événements de conversion spécifiés dans la configuration du Canvas. Dans l'onglet **Paramètres supplémentaires**, saisissez le nombre de jours (entre 1 et 30) pendant lesquels vous souhaitez que cette expérience suive les conversions. La fenêtre temporelle que vous spécifiez ici détermine la durée pendant laquelle les événements de conversion (choisis dans la configuration du Canvas) sont suivis pour l'expérience. Les fenêtres de conversion par événement spécifiées dans la configuration du Canvas ne s'appliquent pas au suivi de cette étape et sont remplacées par cette fenêtre de conversion.

La fenêtre de conversion commence lorsque l'utilisateur entre dans l'étape des chemins d'expérience, et non lorsqu'un message en aval est envoyé. Si un parcours inclut des délais, comme une étape de délai ou le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/), ces délais consomment une partie de la fenêtre de conversion.

{% alert important %}
Si vous utilisez le timing intelligent sur une étape de message au sein d'un chemin d'expérience, le temps écoulé entre l'entrée dans l'expérience et l'envoi effectif du message réduit la fenêtre de conversion effective pour ce parcours. Par exemple, si votre expérience a une fenêtre de conversion de 5 jours et que le timing intelligent retarde le message de 2 jours, les utilisateurs de ce parcours n'ont que 3 jours après la réception du message pour convertir dans la fenêtre de l'expérience, même si les analyses propres à l'étape de message suivent les conversions à partir du moment de l'envoi du message.<br><br>Pour des analyses d'expérience plus claires, placez les délais (comme les étapes de délai) **avant** l'étape des chemins d'expérience plutôt qu'à l'intérieur d'un chemin d'expérience. Ainsi, tous les parcours partent du même point et les délais ne consomment aucune partie de la fenêtre de conversion.
{% endalert %}