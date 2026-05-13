---
nav_title: Créer une prédiction d'attrition
article_title: Créer une prédiction d'attrition
description: "Cet article explique comment créer une prédiction d'attrition dans le tableau de bord de Braze."
page_order: 1.1

---

# Créer une prédiction d'attrition {#create-a-churn-prediction}

> Découvrez comment créer une prédiction d'attrition dans le tableau de bord de Braze.

## Étape 1 : Créer une nouvelle prédiction {#step-1-create-a-new-prediction}

Dans Braze, accédez à **Analytics** > **Predictive Churn**.

Une prédiction est une instance d'un modèle de machine learning entraîné, ainsi que l'ensemble des paramètres et données qu'il utilise. Sur cette page, vous trouverez une liste des prédictions actives actuelles accompagnées d'informations de base les concernant. Vous pouvez y renommer, archiver et créer de nouvelles prédictions. Les prédictions archivées sont inactives et ne mettent pas à jour les scores des utilisateurs.

Pour créer une nouvelle prédiction, choisissez **Create Prediction** et sélectionnez une nouvelle **Churn Prediction**.

{% alert note %}
Le nombre de prédictions d'attrition actives simultanément est limité à cinq. Avant l'achat de Predictive Churn, la limite est d'une prédiction d'attrition en prévisualisation. Une prédiction d'attrition en prévisualisation ne met pas régulièrement à jour les scores et ne vous permet pas de cibler les utilisateurs sur la base des résultats de la prédiction. Contactez votre gestionnaire de compte pour plus de détails.
{% endalert %}

Sur la page **Basics**, donnez un nom unique à votre nouvelle prédiction. Vous pouvez également fournir une description facultative pour prendre des notes sur cette prédiction particulière.

Sélectionnez **Forward** pour passer à l'étape suivante. Vous pouvez également sélectionner **Élaborer maintenant** pour utiliser tous les paramètres par défaut et passer directement à la dernière étape de la création. Vous aurez la possibilité de vérifier les paramètres avant de lancer le processus de création. Vous pouvez revenir à n'importe quelle étape ultérieurement en la sélectionnant dans le suivi de progression.

## Étape 2 : Définir l'attrition {#step-2-define-churn}

Dans le panneau **Définition de l'attrition**, utilisez les filtres fournis pour spécifier la manière dont vous définissez l'attrition des utilisateurs pour votre entreprise. En d'autres termes, qu'est-ce qu'un utilisateur doit faire, et dans quel délai, pour que vous le considériez comme ayant abandonné ?

N'oubliez pas que vous n'avez pas besoin d'expliquer les comportements qui peuvent précéder l'attrition, seulement ce qui fait d'un utilisateur un utilisateur désabonné. Pensez à cela en termes de ce qu'un utilisateur fait une fois (`do`) ou arrête de faire (`do not`) qui constitue l'attrition. Par exemple, vous pouvez considérer les utilisateurs qui n'ont pas ouvert votre application depuis 7 jours comme ayant abandonné. Vous pourriez considérer que la désinstallation, ou des événements personnalisés comme le désabonnement, la désactivation d'un compte ou d'autres actions, entraînent l'attrition d'un utilisateur.

#### Fenêtre d'attrition {#churn-window}

La fenêtre d'attrition est la période pendant laquelle l'activité d'un utilisateur répond aux critères d'attrition. Vous pouvez la configurer pour une durée maximale de 60 jours, en fonction des données disponibles. Cette fenêtre est utilisée pour extraire des données historiques afin d'entraîner votre prédiction. Une fois la prédiction créée, vous pourrez déterminer si les données étaient suffisantes pour obtenir des résultats précis.

Une fois la prédiction créée et les scores attribués aux utilisateurs, le _score de risque d'attrition_ indique la probabilité qu'un utilisateur se désabonne au cours de la période que vous avez définie dans la fenêtre d'attrition.

Voici un exemple de définition simple basée sur l'inactivité des sessions au cours des 7 derniers jours.

![Définition de l'attrition dans laquelle un utilisateur est considéré comme ayant abandonné s'il ne démarre pas une session pendant 7 jours]({% image_buster /assets/img/churn/churn1.png %})

Dans ce cas, nous sélectionnons `do not` et `start a session`. Vous pouvez combiner d'autres filtres avec `AND` et `OR` comme vous le souhaitez pour créer la définition dont vous avez besoin. Vous cherchez des définitions d'attrition à envisager ? Vous pouvez trouver de l'inspiration dans la section suivante sur les [exemples de définitions d'attrition](#sample-definitions).

{% alert note %}
Pour `do`, nous supposons que les utilisateurs actifs n'ont pas effectué l'action que vous spécifiez pour cette ligne avant de se désabonner. Effectuer l'action entraîne leur attrition. <br><br>Pour `do not`, nous considérons comme utilisateurs actifs ceux qui ont effectué cette action au cours des jours précédents, puis ont cessé de le faire. <br><br>**Exemple :** Si l'attrition est définie comme « n'a pas démarré de session au cours des 60 derniers jours », nous considérons comme utilisateurs actifs ceux qui ont démarré une session au cours des 60 derniers jours. Par conséquent, toute personne n'ayant pas démarré de session au cours des 60 derniers jours n'est pas considérée comme un utilisateur actif. Cela signifie qu'une audience d'attrition créée à partir de cette définition ne comprendrait que les utilisateurs ayant démarré une session au cours des 60 derniers jours. L'audience de prédiction d'attrition résultante peut ainsi sembler nettement plus réduite que la population d'origine, car la plupart des utilisateurs d'un espace de travail pourraient déjà répondre à la définition d'utilisateur désabonné et ne pas être actifs dans la prédiction d'attrition.
{% endalert %}

Sous la définition, vous verrez les estimations du nombre d'utilisateurs disponibles (qui ont abandonné ou non par le passé selon votre définition). Vous verrez également les valeurs minimales requises. Braze doit disposer de ce nombre minimum d'utilisateurs dans les données historiques afin que la prédiction dispose de suffisamment de données pour apprendre.

## Étape 3 : Filtrer votre audience de prédiction {#step-3-filter-your-prediction-audience}

Votre audience de prédiction est le groupe d'utilisateurs pour lequel vous souhaitez prédire le risque d'attrition. L'audience de prédiction définit le groupe d'utilisateurs que le modèle de machine learning examine afin de tirer des enseignements du passé. Par défaut, cette option est définie sur **All Users**, ce qui signifie que cette prédiction créera des scores de risque d'attrition pour tous vos utilisateurs actifs (reportez-vous à la note précédente pour savoir qui est considéré comme actif pour un modèle d'attrition).

En fonction de votre cas d'utilisation, vous pouvez utiliser des filtres pour spécifier les utilisateurs que vous souhaitez évaluer pour le modèle. Pour ce faire, sélectionnez **Définir ma propre audience de prédiction** et choisissez vos filtres d'audience. Par exemple, si vous êtes une application de covoiturage dont la base d'utilisateurs comprend des chauffeurs et des passagers, et que vous créez un modèle d'attrition pour les passagers, il serait judicieux de filtrer votre audience de prédiction afin de ne retenir que les passagers. Gardez à l'esprit que de nombreux cas d'utilisation ne nécessitent pas la sélection d'une audience de prédiction spécifique. Par exemple, si votre objectif est de cibler les utilisateurs de la région UE les plus susceptibles de se désabonner, vous pouvez appliquer votre modèle à tous les utilisateurs, puis simplement inclure un filtre pour la région UE dans le Segment de la Campaign.

Braze vous indiquera la taille estimée de votre audience de prédiction. Si vous spécifiez votre audience souhaitée et que vous ne répondez pas aux critères minimaux requis pour exécuter le modèle, essayez de définir un filtre plus large ou d'utiliser l'option **All Users**. Notez que la taille de votre groupe « tous les utilisateurs » n'est pas fixe et varie d'un modèle à l'autre, car elle tient compte de votre définition de l'attrition. Par exemple, supposons que la définition de l'attrition soit **l'absence** de démarrage de session pendant 30 jours. Dans ce cas, Braze applique le modèle aux utilisateurs qui **ont** démarré une session au cours des 30 derniers jours (et prédit la probabilité qu'ils **ne** démarrent **pas** de session au cours des 30 prochains jours). Ces utilisateurs sont donc pris en compte dans l'indicateur « tous les utilisateurs ».

{% alert note %}
L'audience de prédiction ne peut pas dépasser 100 millions d'utilisateurs.
{% endalert %}

Lorsque la fenêtre de prédiction est de 14 jours ou moins, la fenêtre temporelle pour les filtres commençant par « Last… », tels que « Last Used App » et « Last placed an order », **ne peut pas dépasser la fenêtre d'attrition spécifiée** dans la définition de l'attrition. Par exemple, si votre définition de l'attrition dispose d'une fenêtre de 14 jours, la fenêtre temporelle des filtres « Last… » ne peut pas dépasser 14 jours.

La fenêtre d'attrition est évaluée en examinant le nombre de jours écoulés depuis la dernière exécution du modèle. Ainsi, si la fenêtre d'attrition est de 15 jours et que le modèle a été exécuté pour la dernière fois le 1er décembre, le modèle analyse la période du 16 au 30 novembre afin de comprendre l'activité des utilisateurs pour déterminer leur éligibilité et l'entraînement.

#### Mode de filtrage complet {#full-filter-mode}

Afin de créer immédiatement une nouvelle prédiction, seul un sous-ensemble de filtres de segmentation Braze est pris en charge. Le mode de filtrage complet vous permet d'utiliser tous les filtres Braze, mais nécessite une fenêtre d'attrition pour créer la prédiction. Par exemple, si la fenêtre d'attrition est définie sur 15 jours, il faudra 15 jours pour collecter les données utilisateur et créer la prédiction lors de l'utilisation de filtres uniquement pris en charge en mode de filtrage complet. En outre, certaines estimations concernant la taille des audiences ne seront pas disponibles en mode de filtrage complet.

Pour obtenir une liste d'exemples de définitions d'audience de prédiction, consultez nos exemples de définitions dans la section suivante sur les [exemples de définitions d'attrition](#sample-definitions).

![]({% image_buster /assets/img/churn/churn5.png %})

Tout comme la page précédente, le panneau inférieur vous indique le nombre estimé d'utilisateurs historiques résultant de votre définition de l'attrition et de la définition de l'audience de prédiction. Ces estimations doivent répondre aux exigences minimales indiquées afin de créer une prédiction.

## Étape 4 : Choisir la fréquence de mise à jour de la prédiction d'attrition {#step-4-choose-the-update-frequency-for-churn-prediction}

Le modèle de machine learning générera des scores de probabilité d'événement pour les utilisateurs, et ces scores seront mis à jour en fonction de la planification que vous sélectionnez ici. Vous pourrez cibler les utilisateurs en fonction de leur score de probabilité d'événement.

Sélectionnez la **fréquence maximale des mises à jour** que vous jugerez utile. Par exemple, si vous comptez envoyer une promotion hebdomadaire pour empêcher les utilisateurs de se désabonner, définissez la fréquence de mise à jour sur **Weekly** au jour et à l'heure de votre choix.

![Planification de mise à jour de la prédiction définie quotidiennement à 17 h.]({% image_buster /assets/img/churn/churn2.png %})

{% alert note %}
Les prédictions en prévisualisation et en démo ne mettront jamais à jour le risque d'attrition des utilisateurs. En outre, les mises à jour quotidiennes des prédictions nécessitent un achat supplémentaire par rapport aux mises à jour hebdomadaires ou mensuelles avec Predictive Churn. Pour acheter cette fonctionnalité, contactez votre gestionnaire de compte.
{% endalert %}

## Étape 5 : Créer la prédiction {#step-5-build-prediction}

Vérifiez que les informations que vous avez fournies sont correctes, puis choisissez **Build Prediction**. Vous pouvez également enregistrer vos modifications sous forme de brouillon en sélectionnant **Enregistrer en tant que brouillon** pour revenir à cette page et créer le modèle ultérieurement. Une fois que vous avez sélectionné **Build Prediction**, le processus de génération du modèle commence. Cela peut prendre entre 30 minutes et quelques heures en fonction du volume de données. Pour cette prédiction, une page s'affichera pour vous informer que l'entraînement est en cours pendant toute la durée du processus de création du modèle. Le modèle Braze prend en compte les événements personnalisés, les événements d'achat, les événements eCommerce, les événements d'interaction avec les Campaign et les données de session.

Une fois cette opération terminée, la page passera automatiquement à la vue analytique et vous recevrez également un e-mail vous informant que la prédiction et les résultats sont prêts. En cas d'erreur, la page revient en mode édition avec une explication de ce qui s'est mal passé.

La prédiction sera reconstruite (« réentraînée ») **automatiquement toutes les deux semaines** afin de la maintenir à jour sur la base des données les plus récentes disponibles. Notez qu'il s'agit d'un processus distinct de la production des _scores de risque d'attrition_ des utilisateurs, qui sont le résultat de la prédiction. Ces derniers sont déterminés par la fréquence de mise à jour que vous avez choisie à l'étape 4.

## Exemples de définitions d'attrition et d'audience de prédiction {#sample-definitions}

**Exemples de définitions d'attrition**<br>
- « Dans les 7 jours, effectue l'événement personnalisé "Annulation d'abonnement". »<br>
- « Dans les 30 jours, effectue l'événement personnalisé "Essai expiré". »<br>
- « Dans un délai d'un jour, effectue une désinstallation. » <br>
- « Dans les 14 jours, ne réalise pas d'achat. » <br>

Pour les définitions d'attrition que nous avons présentées, il pourrait y avoir des définitions correspondantes de l'audience de prédiction :<br>
- **A commencé l'abonnement il y a plus de 2 semaines OU A commencé l'abonnement il y a moins de 2 semaines**<br>Vous pourriez créer 2 prédictions dans ce cas, puis contacter les nouveaux utilisateurs abonnés différemment des anciens. Vous pouvez également définir cela comme « Premier achat réalisé il y a plus de 30 jours ».<br>
- **Désinstallateurs**<br>Vous pourriez vous concentrer sur les clients qui ont acheté quelque chose récemment ou utilisé l'application très récemment.<br>
- **Les personnes à risque de ne pas acheter en tant que définition de l'attrition**<br>Vous pouvez choisir de vous concentrer sur les clients qui ont récemment consulté, recherché ou interagi avec votre application. Peut-être qu'une remise appropriée empêchera ce groupe plus engagé d'abandonner.

## Prédictions archivées {#archived-predictions}

Les prédictions archivées cesseront de mettre à jour les scores des utilisateurs. Toute prédiction archivée qui est désarchivée continuera à mettre à jour les scores des utilisateurs selon sa planification prédéterminée. Les prédictions archivées ne sont jamais supprimées et restent dans la liste.