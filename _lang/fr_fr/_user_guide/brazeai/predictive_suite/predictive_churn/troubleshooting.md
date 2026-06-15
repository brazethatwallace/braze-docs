---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes de Predictive Churn
description: "Cet article de référence couvre certaines étapes de résolution des problèmes et les considérations à garder à l'esprit lors de l'utilisation de Predictive Churn."
page_order: 3

---

# Résolution des problèmes {#troubleshooting}

> Predictive Churn (et tout modèle de machine learning) est aussi performant que les données disponibles pour le modèle. Il dépend également fortement de la disponibilité de certains volumes de données avec lesquels travailler.

## Erreurs potentielles {#potential-errors}

### Pas assez de données pour l'entraînement {#not-enough-data-to-train}

Ce message d'erreur s'affiche lorsque votre définition d'attrition est trop limitée et renvoie trop peu d'utilisateurs désabonnés.

Pour résoudre ce problème, vous devrez modifier le nombre de jours ou les actions qui définissent l'attrition afin de capturer plus d'utilisateurs. Assurez-vous d'utiliser les filtres `AND/OR` correctement pour ne pas créer de définitions trop restrictives.

{% alert important %}
Bien que Predictive Churn soit activé au niveau de la société, certains espaces de travail peuvent ne pas compter suffisamment d'utilisateurs pour créer des prédictions. En règle générale, vous avez besoin de 300 000 utilisateurs actifs par mois dans un seul espace de travail.
{% endalert %}

### Problèmes avec la taille de l'audience de prédiction {#problems-with-prediction-audience-size}

Lorsque vous créez votre audience de prédiction pour affiner le type d'utilisation sur lequel vous souhaitez que votre modèle soit entraîné, vous pouvez rencontrer ce message vous informant que votre audience de prédiction compte trop peu d'utilisateurs :

« Il n'y a pas assez de non-désabonnés passés pour créer la prédiction de manière fiable »

![Les données requises pour la prédiction montrent 31 désabonnés passés (conforme aux exigences) et 0 non-désabonné passé (inférieur au minimum). Un message d'avertissement indique qu'il n'y a pas suffisamment de non-désabonnés pour créer la prédiction.]({% image_buster /assets/img/churn/audience_size_error.png %})

Si la définition de votre audience de prédiction est trop stricte, vous risquez de ne pas disposer d'un vivier suffisamment important d'utilisateurs historiques et actifs. Pour y remédier, vous devrez soit modifier le nombre de jours et le type d'attributs utilisés dans cette définition, soit changer les actions qui définissent l'attrition, soit les deux.

Si votre audience de prédiction continue à poser problème même après avoir modifié vos définitions, il se peut que vous ayez trop peu d'utilisateurs pour prendre en charge cette fonctionnalité optionnelle. Nous vous suggérons d'essayer de créer une prédiction sans les couches et filtres supplémentaires.

### La taille de l'audience de prédiction est trop grande {#prediction-audience-size-is-too-big}

La définition d'une audience de prédiction ne peut pas dépasser 100 millions d'utilisateurs. Si un message vous indique que votre audience est trop importante, nous vous recommandons d'ajouter des couches à votre audience ou de modifier la fenêtre de temps sur laquelle elle est basée.

### La prédiction a une qualité médiocre {#prediction-has-poor-quality}

![]({% image_buster /assets/img/churn/churn3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}
Si votre modèle a une [qualité de prédiction]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics/) de 40 % ou plus, vous êtes en bonne posture ! Mais si la qualité de votre prédiction tombe à 39 % ou moins, vous devrez peut-être modifier vos définitions d'attrition et d'audience de prédiction pour qu'elles soient plus spécifiques ou qu'elles aient des fenêtres temporelles différentes.

Si vous n'êtes pas en mesure de respecter à la fois l'exigence relative à la taille de l'audience lors de l'élaboration de vos définitions de prédiction et d'obtenir une qualité de prédiction supérieure à 40 %, cela signifie probablement que les données envoyées à Braze ne sont pas idéales pour ce cas d'utilisation, qu'il n'y a pas suffisamment d'utilisateurs pour créer un modèle ou que le cycle de vie de votre produit est plus long que ce que notre fenêtre rétrospective de 60 jours permet actuellement de prendre en charge.

## Considérations relatives aux données {#data-considerations}

Voici les questions à vous poser lorsque vous configurez Predictive Churn. Les modèles de machine learning sont aussi performants que les données qui les entraînent. Avoir de bonnes pratiques en matière d'hygiène des données et comprendre ce qui alimente le modèle fera une grande différence.

- Quelles sont les actions à forte valeur ajoutée qui conduisent à la rétention et à la fidélisation ?
- Avez-vous mis en place des événements personnalisés qui correspondent à ces actions spécifiques ? Predictive Churn fonctionne avec des événements personnalisés plutôt que des attributs personnalisés.
- Raisonnez-vous en termes de fenêtres temporelles pour définir l'attrition ? Vous pouvez définir l'attrition comme quelque chose qui se produit en 60 jours maximum.
- Avez-vous pris en compte les périodes de l'année qui donnent lieu à des comportements atypiques de la part des utilisateurs, comme les vacances ? Des changements rapides dans le comportement des consommateurs auront un impact sur vos prédictions.