---
nav_title: Chemins personnalisés
article_title: Chemins personnalisés dans les Chemins d'expérience
page_type: reference
description: "Les Chemins personnalisés vous permettent de personnaliser n'importe quel point d'un parcours Canvas pour chaque utilisateur en fonction de sa probabilité de conversion."
tool: Canvas
---

# Chemins personnalisés dans les Chemins d'expérience

> Les Chemins personnalisés fonctionnent de manière similaire à la [variante personnalisée]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations#personalized-variant) dans les campagnes et vous permettent de personnaliser n'importe quel point d'un parcours Canvas pour chaque utilisateur en fonction de sa probabilité de conversion.

## Fonctionnement des Chemins personnalisés

Lorsque les Chemins personnalisés sont activés dans une étape Chemin d'expérience, le comportement diffère légèrement selon que votre Canvas est configuré pour un envoi unique ou récurrent :

- **Canvas à envoi unique :** Un groupe d'utilisateurs est retenu dans un groupe de délai. Les utilisateurs restants passent par un test initial pour entraîner un modèle prédictif pendant une durée que vous configurez — au moins 24 heures pour de meilleurs résultats. Après le test, un modèle est créé pour identifier quels comportements utilisateurs étaient associés à une plus grande probabilité de conversion sur un chemin donné. Enfin, chaque utilisateur du groupe de délai est envoyé sur le chemin le plus susceptible de générer une conversion pour lui, en fonction des comportements qu'il présente et de ce que le modèle prédictif a appris pendant le test initial.
- **Canvas récurrents, déclenchés par une action et déclenchés par l'API :** Une expérience initiale est réalisée sur tous les utilisateurs qui entrent dans le Chemin d'expérience pendant une fenêtre spécifiée. Pour préserver l'intégrité de l'expérience, si un utilisateur reçoit plusieurs messages avant la fin de la fenêtre, il sera affecté à la même variante à chaque fois. Après la fenêtre d'expérience, chaque utilisateur est envoyé sur le chemin le plus susceptible de générer une conversion pour lui.

## Utiliser les Chemins personnalisés

### Étape 1 : Ajouter un Chemin d'expérience

Ajoutez un [Chemin d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/) à votre Canvas, puis activez **Chemins personnalisés**.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_path.png %})

### Étape 2 : Configurer les paramètres des Chemins personnalisés

Spécifiez l'événement de conversion qui déterminera le gagnant. Si aucun événement de conversion n'est disponible, revenez à la première étape de la configuration du Canvas et [affectez des événements de conversion]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#choose-conversion-events).

Si vous choisissez les ouvertures ou les clics comme événement de conversion, assurez-vous que la première étape du chemin est une [étape Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/). Braze ne comptabilise l'engagement qu'à partir de la première étape Message de chaque chemin respectif. Si le chemin commence par une étape différente (comme une étape Délai ou Parcours d'audience) et que le message arrive plus tard, ce message ne sera pas pris en compte lors de l'évaluation des performances.

Définissez ensuite la **Fenêtre d'expérience**. La **Fenêtre d'expérience** détermine pendant combien de temps les utilisateurs seront envoyés sur tous les chemins avant de choisir le meilleur chemin pour chaque utilisateur du groupe de délai. La fenêtre commence lorsque le premier utilisateur entre dans l'étape.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_settings.png %})

### Étape 3 : Déterminer le comportement de repli

Par défaut, si les résultats du test ne sont pas suffisants pour déterminer un gagnant statistiquement significatif, tous les futurs utilisateurs seront envoyés sur le chemin le plus performant.

Vous pouvez également sélectionner **Continuer à envoyer tous les futurs utilisateurs sur le mix de chemins**.

![]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

Cette option enverra les futurs utilisateurs sur le mix de chemins selon les pourcentages spécifiés dans la distribution du chemin d'expérience.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_percentages.png %})

### Étape 4 : Ajouter vos chemins et lancer le Canvas

{% tabs local %}
{% tab Canvas à envoi unique %}

Un seul composant Chemin d'expérience peut contenir jusqu'à quatre chemins. Cependant, pour les Canvas à envoi unique, vous pouvez ajouter jusqu'à trois chemins lorsque les Chemins personnalisés sont activés. Le quatrième chemin doit être réservé au groupe de délai que Braze ajoute automatiquement à votre expérience.

Terminez la configuration de votre Canvas selon vos besoins, puis lancez-le. Lorsque le premier utilisateur est entré dans l'expérience, vous pouvez consulter le Canvas pour voir les analyses au fur et à mesure et [suivre les performances de votre expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#tracking-performance).

![]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_pending.png %}){: style="max-width:75%;" }

Lorsque la fenêtre d'expérience est écoulée et que l'expérience est terminée, Braze envoie les utilisateurs du groupe de délai sur leurs chemins respectifs présentant la plus forte probabilité personnalisée de conversion, selon la recommandation du modèle prédictif.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_complete.png %}){: style="max-width:75%;" }

{% endtab %}
{% tab Canvas récurrent, déclenché par une action ou déclenché par l'API %}

Vous pouvez tester jusqu'à quatre chemins dans un seul Chemin d'expérience. Ajoutez vos chemins et terminez la configuration de votre Canvas selon vos besoins, puis lancez-le.

Lorsque le premier utilisateur est entré dans l'expérience, vous pouvez consulter le Canvas pour voir les analyses au fur et à mesure et [suivre les performances de votre expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#tracking-performance).

Lorsque la fenêtre d'expérience est écoulée et que l'expérience est terminée, tous les utilisateurs suivants qui entrent dans le Canvas seront envoyés sur le chemin le plus susceptible de générer une conversion pour eux.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_recurring_analytics.png %}){: style="max-width:75%;" }

{% endtab %}
{% endtabs %}

## Analyses {#analytics}

Si les Chemins personnalisés ont été activés, votre vue d'analyse est séparée en deux onglets : **Expérience initiale** et **Chemins personnalisés**.

{% tabs local %}
{% tab Expérience initiale %}

L'onglet **Expérience initiale** affiche les indicateurs de chaque chemin pendant la fenêtre d'expérience. Vous pouvez voir un résumé des performances de tous les chemins pour les événements de conversion spécifiés.

![Résultats d'une expérience initiale envoyée pour déterminer le chemin le plus performant pour chaque utilisateur. Un tableau montre les performances de chaque chemin en fonction de divers indicateurs pour le canal ciblé.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1.png %})

Par défaut, le test recherche des associations entre les Événements personnalisés des utilisateurs et leurs préférences de chemin, c'est-à-dire la variante de message à laquelle un utilisateur répond le mieux. Cette analyse détecte si les Événements personnalisés augmentent ou diminuent la probabilité de répondre à un chemin particulier. Ces relations sont ensuite utilisées pour déterminer quel utilisateur est affecté à quel chemin après la fin de la fenêtre d'expérience.

Les relations entre les Événements personnalisés et les préférences de chemin sont affichées dans le tableau de l'onglet **Expérience initiale**.

![]({% image_buster /assets/img_archive/experiment_personalized_analytics_custom_data.png %})

Si le test ne parvient pas à trouver de relation significative entre les Événements personnalisés et les préférences de chemin, il se rabat sur une méthode d'analyse basée sur les sessions, et aucun tableau de données d'Événements personnalisés n'est affiché.

{% details Méthode d'analyse de repli %}

**Méthode d'analyse basée sur les sessions**<br>
Si la méthode de repli est utilisée pour déterminer les Chemins personnalisés, l'onglet **Expérience initiale** affiche une répartition des variantes préférées des utilisateurs en fonction d'une combinaison de certaines caractéristiques.

Ces caractéristiques sont :

- **Récence :** Date de leur dernière session
- **Fréquence :** Fréquence de leurs sessions
- **Ancienneté :** Depuis combien de temps ils sont utilisateurs

![Le tableau des caractéristiques utilisateurs, qui montre quels utilisateurs sont prédits comme préférant le Chemin 1 et le Chemin 2 en fonction des trois compartiments dans lesquels ils se trouvent pour la récence, la fréquence et l'ancienneté.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1_2.png %})

La récence correspond à la date de leur dernière interaction avec vous, la fréquence à la régularité de leur engagement, et l'ancienneté à la durée totale de leur engagement avec vous. Nous regroupons les utilisateurs dans des « compartiments » en fonction de ces trois critères (comme expliqué dans le tableau **Caractéristiques utilisateurs**), puis nous observons quel compartiment préfère quel chemin. C'est comme trier les utilisateurs dans des centaines de listes différentes en fonction de la date de leur dernier achat, de la fréquence de leurs achats et de leur ancienneté en tant que clients.

Lorsqu'il s'agit de choisir un message pour un utilisateur, Braze examine les compartiments auxquels il appartient. Chaque compartiment exerce une influence distincte sur la sélection du chemin pour les utilisateurs. Nous quantifions cette influence à l'aide d'une méthode statistique appelée [régression logistique](https://en.wikipedia.org/wiki/Logistic_regression), qui permet de prédire le comportement futur en fonction des actions passées. Cette méthode prend en compte les interactions des utilisateurs lors de l'envoi initial du message. Ce tableau ne fait que résumer les résultats en affichant le chemin avec lequel les utilisateurs de chaque compartiment ont eu tendance à interagir.

Au final, Braze combine toutes ces données pour sélectionner un chemin de message adapté à chaque utilisateur, afin de le rendre aussi engageant et pertinent que possible.

{% alert note %}
Les intervalles de temps pour chaque compartiment sont déterminés en fonction des données utilisateurs spécifiques au Canvas, et peuvent varier d'un Canvas à l'autre.
{% endalert %}

**Comment les Chemins personnalisés sont sélectionnés**<br>
Avec cette méthode, le message recommandé pour un utilisateur individuel est la somme des effets de sa récence, sa fréquence et son ancienneté spécifiques. La récence, la fréquence et l'ancienneté sont réparties en compartiments, comme illustré dans le tableau **Caractéristiques utilisateurs**. La plage temporelle de chaque compartiment est déterminée par les données des utilisateurs de chaque Canvas individuel et varie d'un Canvas à l'autre.

Chaque compartiment peut avoir une contribution ou une « impulsion » différente vers chaque chemin. La force de l'impulsion pour chaque compartiment est déterminée à partir des réponses des utilisateurs lors de l'expérience initiale en utilisant la [régression logistique](https://en.wikipedia.org/wiki/Logistic_regression). Ce tableau ne fait que résumer les résultats en affichant le chemin avec lequel les utilisateurs de chaque compartiment ont eu tendance à interagir. Le Chemin personnalisé réel d'un utilisateur individuel dépend de la somme des effets des trois compartiments auxquels il appartient — un pour chaque caractéristique.

{% enddetails %}

{% endtab %}
{% tab Chemins personnalisés %}

L'onglet **Chemins personnalisés** affiche les résultats de l'expérience finale, où les utilisateurs du groupe de délai ont été envoyés sur le chemin le plus performant pour eux.

Les trois cartes de cette page montrent votre gain projeté, les résultats globaux et les résultats projetés si vous aviez envoyé uniquement le Chemin gagnant. Même s'il n'y a pas de gain, ce qui peut parfois arriver, le résultat est le même que l'envoi uniquement du Chemin gagnant (un test A/B traditionnel).

- **Gain projeté :** L'amélioration de votre événement de conversion sélectionné grâce à l'utilisation des Chemins personnalisés au lieu d'envoyer tous les utilisateurs sur le chemin globalement le plus performant.
- **Résultats globaux :** Les résultats du second envoi basés sur votre événement de conversion.
- **Résultats projetés :** Les résultats projetés du second envoi basés sur votre indicateur d'optimisation choisi si vous aviez envoyé uniquement la variante gagnante.

![Onglet Chemins personnalisés pour un Canvas. Les cartes montrent le Gain projeté, les Conversions globales (avec Chemins personnalisés) et les Ouvertures uniques projetées (avec Chemin gagnant).]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab2.png %})

{% endtab %}
{% endtabs %}

## Utiliser les Chemins personnalisés avec la diffusion selon l'heure locale

Nous ne recommandons pas d'utiliser la diffusion selon l'heure locale dans les Canvas avec des Chemins personnalisés. En effet, les fenêtres d'expérience commencent lorsque le premier utilisateur passe par l'étape. Les utilisateurs situés dans des fuseaux horaires très en avance peuvent entrer dans l'étape et déclencher le début de la fenêtre d'expérience bien plus tôt que prévu, ce qui peut entraîner la fin de l'expérience avant que la majorité de vos utilisateurs dans des fuseaux horaires plus courants aient eu suffisamment de temps pour entrer dans le Canvas et convertir.

Si vous souhaitez tout de même utiliser la diffusion selon l'heure locale, utilisez une fenêtre d'expérience de 24 à 48 heures ou plus. Ainsi, les utilisateurs dans les fuseaux horaires en avance entrent dans le Canvas et déclenchent le début de l'expérience, mais il reste suffisamment de temps dans la fenêtre d'expérience. Les utilisateurs dans les fuseaux horaires en retard auront encore assez de temps pour entrer dans le Canvas et dans l'étape Chemin d'expérience avec Chemins personnalisés, et éventuellement convertir avant l'expiration de la fenêtre d'expérience.