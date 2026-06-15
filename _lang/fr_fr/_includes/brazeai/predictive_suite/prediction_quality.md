Pour mesurer la précision de votre modèle, l'indicateur de _qualité de la prédiction_ vous montrera à quel point ce modèle de machine learning particulier semble efficace lorsqu'il est testé sur des données historiques. Braze extrait les données selon les groupes que vous avez spécifiés dans la page de création du modèle. Le modèle est entraîné à l'aide d'un ensemble de données (l'ensemble « entraînement ») puis testé sur un nouveau jeu de données distinct (l'ensemble « test »).

La prédiction sera à nouveau entraînée toutes les deux semaines et mise à jour parallèlement à l'indicateur de _qualité de la prédiction_ afin que vos prédictions soient toujours actualisées en fonction des comportements utilisateurs les plus récents. En outre, à chaque occurrence, les deux dernières semaines de prédictions seront testées par rapport aux résultats réels des utilisateurs. La _qualité de la prédiction_ sera alors calculée sur la base de ces résultats réels (plutôt que sur des estimations). Il s'agit d'un backtest automatique (c'est-à-dire le test d'un modèle prédictif sur des données historiques) qui permet de s'assurer que la prédiction est exacte dans des scénarios réels. La date du dernier réentraînement et du dernier backtest sera affichée sur la page **Predictions** et sur la page d'analyse d'une prédiction individuelle. Même une prédiction de prévisualisation effectuera ce backtest une fois après sa création. Ainsi, vous pouvez être sûr de l'exactitude de vos prédictions personnalisées, même avec la version gratuite de la fonctionnalité.

{% details Exemple de qualité de prédiction %}

Par exemple, si 20 % de vos utilisateurs sont habituellement désabonnés en moyenne et que vous choisissez un sous-ensemble aléatoire de 20 % de vos utilisateurs en les qualifiant de désabonnés au hasard (qu'ils le soient réellement ou non), vous ne devriez identifier correctement que 20 % des véritables désabonnés. C'est une estimation aléatoire. Si le modèle ne faisait que cela, le lift serait de 1 dans ce cas.

Si le modèle, en revanche, vous permettait d'envoyer des messages à 20 % des utilisateurs et, ce faisant, de cibler tous les « vrais » désabonnés et personne d'autre, le lift serait de 100 % / 20 % = 5. Si vous reportez ce ratio pour chaque proportion des utilisateurs les plus susceptibles de se désabonner à qui vous pourriez envoyer un message, vous obtenez la [courbe de lift](https://en.wikipedia.org/wiki/Lift_(data_mining)).

Une autre façon d'appréhender la qualité du lift (et aussi la _qualité de la prédiction_) est de voir à quel point la courbe de lift de la prédiction se situe entre l'estimation aléatoire (0 %) et la perfection (100 %) dans l'identification des désabonnés sur l'ensemble de test. Pour consulter l'article original sur la qualité du lift, voir [Measuring lift quality in database marketing](https://dl.acm.org/doi/10.1145/380995.381018).

{% enddetails %}

### Comment est-elle mesurée {#how-its-measured}

Notre mesure de la _qualité de la prédiction_ est la [qualité du lift](https://dl.acm.org/doi/10.1145/380995.381018). De manière générale, le terme « lift » fait référence à l'augmentation du ratio ou du pourcentage d'un résultat positif, tel qu'une conversion. Dans ce cas, le résultat positif consiste à identifier correctement un utilisateur qui se serait désabonné. La qualité du lift correspond au lift moyen que la prédiction fournit sur toutes les tailles d'audience possibles pour l'envoi de messages sur l'ensemble de test. Cette approche mesure l'efficacité du modèle par rapport à une estimation aléatoire. Avec cette mesure, 0 % signifie que le modèle n'est pas meilleur qu'une estimation aléatoire des personnes qui vont se désabonner, et 100 % indique une connaissance parfaite de l'attrition.

### Plages recommandées {#recommended-ranges}

Voici ce que nous recommandons pour différentes plages de _qualité de la prédiction_ :

| Plage de qualité de prédiction (%) | Recommandation |
| ---------------------- | -------------- |
| 60 - 100 | Excellent. Précision de premier ordre. La modification des définitions d'audience est peu susceptible de fournir un avantage supplémentaire. |
| 40 - 60 | Bon. Ce modèle produira des prédictions précises, mais essayer différents paramètres d'audience peut permettre d'obtenir de meilleurs résultats. |
| 20 - 40 | Correct. Ce modèle peut fournir une certaine précision et de la valeur, mais envisagez d'essayer différentes définitions d'audience pour voir si elles améliorent les performances. |
| 0 - 20 | Faible. Nous vous recommandons de modifier les définitions de votre audience et de réessayer. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Recommended ranges" }