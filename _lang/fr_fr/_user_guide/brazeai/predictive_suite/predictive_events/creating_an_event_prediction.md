---
nav_title: "Créer une prédiction d'événement"
article_title: "Créer une prédiction d'événement"
page_order: 1.1
description: "Cet article explique comment créer une prédiction d'événement dans le tableau de bord de Braze."

---

# Créer une prédiction d'événement {#create-an-event-prediction}

> Une prédiction est une instance d'un modèle de machine learning entraîné, ainsi que l'ensemble des paramètres et données qu'il utilise. Pour en savoir plus sur Predictive Events, consultez l'[aperçu de Predictive Events]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/).

Dans Braze, accédez à **Analytics** > **Predictive Events**.

Sur cette page, vous trouverez une liste des prédictions d'événements actives et quelques informations de base à leur sujet. Vous pouvez y renommer, archiver et créer de nouvelles prédictions. Les prédictions archivées sont inactives et ne mettent pas à jour les scores des utilisateurs.

## Étape 1 : Créer une nouvelle prédiction {#step-1-create-a-new-prediction}

1. Choisissez **Create Prediction** et sélectionnez une nouvelle **Event Prediction**.

{% alert note %}
Le nombre de prédictions actives simultanément est limité à cinq. Avant l'achat de Predictive Events, la limite est d'une seule prévisualisation de prédiction active. Une prévisualisation de prédiction ne mettra pas régulièrement à jour les scores et ne ciblera pas les utilisateurs en fonction des résultats de la prédiction. Contactez votre gestionnaire de compte pour plus de détails.
{% endalert %}

{: start="2"}
2. Donnez à votre prédiction un nom unique. Vous pouvez également fournir une description pour enregistrer des remarques pertinentes.

![]({% image_buster /assets/img/purchasePrediction/purchases_step1.png %})

{: start="3"}
3. Cliquez sur **Forward** pour passer à l'étape suivante. <br><br>Vous pouvez également cliquer sur **Élaborer maintenant** pour utiliser tous les paramètres par défaut et passer directement à la dernière étape de la création. Vous aurez la possibilité de vérifier les paramètres avant de lancer le processus de création. Vous pouvez aussi revenir à n'importe quelle étape ultérieurement en cliquant dessus dans la barre supérieure.

## Étape 2 : Spécifier le suivi des événements {#event-tracking}

Indiquez si les événements de vos utilisateurs sont stockés dans Braze en tant qu'[événements d'achat]({{site.baseurl}}/user_guide/data/activation/events/purchase_events/), [événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) ou [événement de commande passée]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/?tab=ecommerce.order_placed).

Ici, vous verrez si la méthode sélectionnée fournit suffisamment de données pour que Braze puisse créer un modèle de machine learning. Si l'exigence n'est pas satisfaite, essayez de sélectionner l'autre méthode d'enregistrement si elle est également utilisée par votre application. Malheureusement, si ce n'est pas le cas, Braze n'est pas en mesure de créer une prédiction avec la quantité de données disponibles. Si vous pensez que cette erreur n'a pas lieu d'être, contactez votre gestionnaire de la satisfaction client.

#### Fenêtre d'événement {#event-window}

La fenêtre d'événement est le laps de temps pendant lequel vous souhaitez prédire si un utilisateur effectuera l'événement. Elle peut être configurée jusqu'à 60 jours. Cette fenêtre est utilisée pour interroger les données historiques afin d'entraîner la prédiction. De plus, une fois la prédiction créée et les scores attribués aux utilisateurs, le score de probabilité indique dans quelle mesure un utilisateur est susceptible de réaliser l'événement dans le nombre de jours spécifié par la fenêtre d'événement.

### Étape 3 : Filtrer votre audience de prédiction (facultatif) {#audience}

Votre audience de prédiction est le groupe d'utilisateurs dont vous souhaitez prédire le score de probabilité. Si vous le souhaitez, vous pouvez effectuer une prédiction sur l'ensemble de votre population d'utilisateurs. Pour ce faire, laissez l'option par défaut **Tous les utilisateurs** sélectionnée.

En fonction de votre cas d'utilisation, vous pouvez utiliser des filtres pour spécifier les utilisateurs que vous souhaitez évaluer pour le modèle. Pour ce faire, sélectionnez **Définir ma propre audience de prédiction** et choisissez vos filtres d'audience. Par exemple, vous souhaiterez peut-être vous concentrer sur les utilisateurs qui utilisent votre application depuis au moins 30 jours en réglant le filtre « First Used App » sur 30 jours. La configuration de cette audience indique à Braze que vous souhaitez que votre modèle apprenne spécifiquement à partir des utilisateurs qui (au moment où le modèle est exécuté) ont utilisé l'application pendant au moins 30 jours.

{% alert important %}
Concentrez vos filtres sur les caractéristiques des utilisateurs pertinentes pour votre cas d'utilisation, telles que les utilisateurs actifs, les nouveaux utilisateurs, les utilisateurs à forte valeur ajoutée ou les utilisateurs d'un pays spécifique. Évitez de filtrer votre audience de prédiction en fonction du fait que les utilisateurs aient déjà réalisé l'événement que vous prédisez. L'audience de prédiction définit les utilisateurs à partir desquels vous souhaitez que le modèle apprenne, et non le résultat de l'événement en lui-même. Le modèle doit observer à la fois les utilisateurs qui ont réalisé l'événement et ceux qui ne l'ont pas fait afin d'apprendre et de prédire avec précision la probabilité de réalisation future de l'événement.
{% endalert %}

L'audience de prédiction définit le groupe d'utilisateurs que le modèle de machine learning examine pour tirer des enseignements du passé. Braze vous indiquera la taille estimée de votre audience de prédiction. Si vous spécifiez votre audience souhaitée et que vous ne répondez pas aux critères minimaux requis pour exécuter le modèle, essayez de définir un filtre plus large ou d'utiliser l'option **Tous les utilisateurs**. Gardez à l'esprit que de nombreux cas d'utilisation ne nécessitent pas la sélection d'une audience de prédiction spécifique. Par exemple, si votre cas d'utilisation consiste à cibler les utilisateurs de la région UE les plus susceptibles de se désabonner, vous pouvez appliquer votre modèle à tous les utilisateurs, puis inclure un filtre pour la région UE dans le segment de la campagne.

{% alert note %}
L'audience de prédiction ne peut pas dépasser 100 millions d'utilisateurs.
{% endalert %}

Lorsque la fenêtre d'événement est de 14 jours ou moins, la fenêtre temporelle pour les filtres qui commencent par « Last… », tels que « Last Used App » et « Last placed an order », **ne peut pas dépasser la fenêtre d'événement définie dans le [suivi des événements](#event-tracking)**. Par exemple, si la fenêtre d'événement est définie sur 14 jours, la fenêtre temporelle pour les filtres « Last… » ne peut pas dépasser 14 jours.

#### Mode de filtrage complet {#full-filter-mode}

Afin de créer immédiatement une nouvelle prédiction, seul un sous-ensemble de filtres de segmentation de Braze est pris en charge. Le mode de filtrage complet vous permet d'utiliser tous les filtres Braze, mais nécessite une fenêtre d'événement pour créer la prédiction.

Par exemple, si la fenêtre d'événement est définie sur 14 jours, il faudra 14 jours pour collecter les données utilisateur et créer la prédiction lors de l'utilisation de filtres uniquement pris en charge en mode de filtrage complet. De plus, certaines estimations concernant la taille des audiences ne seront pas disponibles en mode de filtrage complet.

### Étape 4 : Choisir la planification de la mise à jour {#step-4-choose-the-update-schedule}

Le modèle de machine learning générera des scores de probabilité d'événement pour les utilisateurs, et ces scores seront mis à jour en fonction de la planification que vous sélectionnez ici. Vous pourrez cibler les utilisateurs en fonction de leur score de probabilité d'événement.

Sélectionnez la **fréquence maximale des mises à jour** que vous jugerez utile. Par exemple, si vous prévoyez des commandes et envisagez d'envoyer une promotion hebdomadaire, définissez la fréquence de mise à jour sur **Weekly**, à la date et à l'heure de votre choix.

{% alert note %}
Les prédictions de prévisualisation et de démonstration ne mettront jamais à jour les scores de probabilité des utilisateurs.
{% endalert %}

### Étape 5 : Créer la prédiction {#step-5-build-prediction}

Vérifiez que les informations que vous avez fournies sont correctes, puis choisissez **Créer la prédiction**. Vous pouvez également enregistrer vos modifications sous forme de brouillon en sélectionnant **Enregistrer en tant que brouillon** pour revenir à cette page et créer le modèle ultérieurement.

Une fois que vous avez cliqué sur **Créer la prédiction**, le processus de génération du modèle commence. Cela peut prendre entre 30 minutes et quelques heures en fonction du volume de données. Pour cette prédiction, vous verrez une page expliquant que l'entraînement est en cours pendant toute la durée du processus de création du modèle. Le modèle Braze prend en compte les événements personnalisés, les événements d'achat, les événements eCommerce, les événements d'interaction avec les campagnes et les données de session.

Une fois terminé, la page basculera automatiquement vers la vue analytique et vous recevrez un e-mail vous informant que la prédiction et les résultats sont prêts. En cas d'erreur, la page reviendra en mode édition avec une explication de ce qui s'est mal passé.

La prédiction sera automatiquement reconstruite (« réentraînée ») toutes les **deux semaines** afin de la maintenir à jour sur la base des données les plus récentes disponibles. Notez qu'il s'agit d'un processus distinct de la production des scores de probabilité des utilisateurs, qui constituent le résultat de la prédiction. Ces derniers sont déterminés par la fréquence de mise à jour que vous avez choisie à l'étape 4.

## Prédictions archivées {#archived-predictions}

Les prédictions archivées cesseront de mettre à jour les scores des utilisateurs. Toute prédiction archivée qui est désarchivée continuera à mettre à jour les scores des utilisateurs selon sa planification prédéterminée. Les prédictions archivées ne sont jamais supprimées et restent dans la liste.