---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes de Predictive Churn
description: "Diagnostiquez les erreurs d'entraînement et d'audience de Predictive Churn à l'aide d'un index des symptômes et des exigences en matière de données."
page_order: 3

---

# Résolution des problèmes de Predictive Churn {#troubleshoot-predictive-churn}

> Utilisez cette page pour résoudre les erreurs d'entraînement et d'audience de Predictive Churn. Pour l'analyse et la qualité du modèle, consultez [Analyse de Predictive Churn]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics).

Predictive Churn (et tout modèle de machine learning) est aussi performant que les données disponibles pour le modèle. Il dépend également d'un volume d'utilisateurs suffisant dans l'espace de travail.

## Commencez ici : identifiez votre symptôme {#start-here-match-your-symptom}

Identifiez le message d'erreur, l'avertissement ou le résultat que vous rencontrez lors de la création d'une prédiction, puis accédez à la section correspondante pour le résoudre.

| Symptôme | Aller à |
| --- | --- |
| Erreur « Pas assez de données pour l'entraînement » | [Pas assez de données pour l'entraînement](#not-enough-data-to-train) |
| Avertissement « Pas assez de non-désabonnés passés » | [Audience de prédiction trop petite](#problems-with-prediction-audience-size) |
| L'audience de prédiction dépasse la limite de taille | [Audience de prédiction trop grande](#prediction-audience-size-is-too-big) |
| Qualité de la prédiction inférieure à 40 % | [La prédiction est de mauvaise qualité](#prediction-has-poor-quality) |
| Vous ne savez pas si vos données conviennent au modèle | [Considérations sur les données](#data-considerations) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Symptôme de prédiction du taux d'attrition" }

## Parcours d'investigation standard {#standard-investigation-path}

Utilisez ce flux de travail lorsque la création d'une prédiction échoue ou que vous êtes bloqué par des exigences liées aux données ou à l'audience. Commencez à l'étape 1.

1. Vérifiez que la prédiction du taux d'attrition est activée pour votre entreprise et que l'espace de travail dispose d'un nombre suffisant d'utilisateurs actifs mensuels (MAU) — généralement 300 000 MAU dans un seul espace de travail.
2. Vérifiez votre définition de l'attrition. Des filtres trop restrictifs réduisent le nombre d'utilisateurs désabonnés disponibles pour l'entraînement.
3. Vérifiez la définition de votre audience de prédiction. Un nombre insuffisant d'utilisateurs historiques non désabonnés empêche l'entraînement du modèle.
4. Confirmez que ce sont des événements personnalisés (et non des attributs personnalisés seuls) qui capturent les actions à forte valeur ajoutée indiquant un risque d'attrition.
5. Si les erreurs persistent après avoir élargi les définitions, contactez l'[Assistance Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## Pas assez de données pour l'entraînement {#not-enough-data-to-train}

**Symptôme :** vous voyez une erreur « Not enough data to train » lors de la création d'une prédiction.

Cette erreur apparaît lorsque votre définition de l'attrition est trop restrictive et ne renvoie pas assez d'utilisateurs désabonnés.

Pour résoudre ce problème, modifiez le nombre de jours, les actions qui définissent l'attrition afin de capturer davantage d'utilisateurs, ou les deux. Assurez-vous d'utiliser correctement les filtres `AND/OR` pour ne pas créer de définitions trop restrictives.

{% alert important %}
Bien que la prédiction du taux d'attrition soit activée au niveau de l'entreprise, certains espaces de travail peuvent ne pas avoir suffisamment d'utilisateurs pour créer des prédictions. En général, vous avez besoin de 300 000 utilisateurs actifs mensuels dans un seul espace de travail.
{% endalert %}

## Problèmes liés à la taille de l'audience de prédiction {#problems-with-prediction-audience-size}

**Symptôme :** Vous voyez le message « Not enough past non-churners to reliably build the Prediction. »

![Exigences de données de prédiction affichant 31 anciens désabonnés (exigence satisfaite) et 0 anciens non-désabonnés (en dessous du minimum). Un message d'avertissement indique qu'il n'y a pas assez de non-désabonnés pour créer la prédiction.]({% image_buster /assets/img/churn/audience_size_error.png %})

Lorsque vous créez votre audience de prédiction pour affiner le type d'usage contre lequel vous souhaitez entraîner votre modèle, vous pouvez rencontrer ce message vous informant que votre audience de prédiction contient trop peu d'utilisateurs.

Si la définition de votre audience de prédiction est trop stricte, vous risquez de ne pas disposer d'un nombre suffisant d'utilisateurs historiques et actifs. Pour résoudre ce problème, modifiez le nombre de jours et le type d'attributs utilisés dans cette définition, changez les actions qui définissent l'attrition, ou les deux.

Si votre audience de prédiction continue de poser problème même après avoir modifié vos définitions, il se peut que vous ayez trop peu d'utilisateurs pour prendre en charge cette fonctionnalité optionnelle. Essayez plutôt de créer une prédiction sans les couches et filtres supplémentaires.

## La taille de l'audience de prédiction est trop grande {#prediction-audience-size-is-too-big}

**Symptôme :** La définition de votre audience de prédiction dépasse la taille maximale autorisée.

Une définition d'audience de prédiction ne peut pas dépasser 100 millions d'utilisateurs. Si un message indique que votre audience est trop grande, ajoutez des couches supplémentaires à votre audience ou modifiez la fenêtre temporelle sur laquelle elle est basée.

## La prédiction est de mauvaise qualité {#prediction-has-poor-quality}

**Symptôme :** la [qualité de la prédiction]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics) est de 39 % ou moins.

![Capture d'écran liée à une prédiction de mauvaise qualité.]({% image_buster /assets/img/churn/churn3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Si votre modèle a une qualité de prédiction de 40 % ou plus, vous êtes en bonne position. Mais si votre qualité de prédiction tombe à 39 % ou moins, vous devrez peut-être modifier vos définitions d'audience d'attrition et de prédiction pour les rendre plus spécifiques ou utiliser des fenêtres temporelles différentes.

Si vous ne parvenez pas à satisfaire à la fois l'exigence de taille d'audience lors de la création de vos définitions de prédiction et à atteindre une qualité de prédiction supérieure à 40 %, cela signifie probablement que les données envoyées à Braze ne sont pas idéales pour ce cas d'usage, qu'il n'y a pas suffisamment d'utilisateurs pour construire un modèle, ou que le cycle de vie de votre produit est plus long que ce que notre fenêtre rétrospective actuelle de 60 jours permet.

## Considérations relatives aux données {#data-considerations}

Voici les questions à vous poser lorsque vous configurez la prédiction du taux d'attrition. Les modèles de machine learning sont aussi performants que les données qui les entraînent. Avoir de bonnes pratiques en matière d'hygiène des données et comprendre ce qui alimente le modèle fera une grande différence.

- Quelles sont les actions à forte valeur ajoutée qui conduisent à la rétention et à la fidélisation ?
- Avez-vous mis en place des événements personnalisés qui correspondent à ces actions spécifiques ? La prédiction du taux d'attrition fonctionne avec des événements personnalisés plutôt que des attributs personnalisés.
- Raisonnez-vous en termes de fenêtres temporelles pour définir l'attrition ? Vous pouvez définir l'attrition comme quelque chose qui se produit en 60 jours maximum.
- Avez-vous pris en compte les périodes de l'année qui donnent lieu à des comportements atypiques de la part des utilisateurs, comme les vacances ? Des changements rapides dans le comportement des consommateurs auront un impact sur vos prédictions.