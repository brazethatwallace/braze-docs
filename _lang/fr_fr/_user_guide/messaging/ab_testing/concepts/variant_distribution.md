---
nav_title: Distribution des variantes
article_title: Distribution des variantes
page_order: 1
page_type: reference
description: "Cet article de référence explique comment Braze répartit les utilisateurs entre les variantes dans les tests A/B et multivariés."
tool:
  - Campaign
  - Canvas
---

# Distribution des variantes {#variant-distribution}

> Lorsque vous configurez un test A/B ou multivarié, chaque envoi affecte indépendamment les utilisateurs aux variantes en fonction des pourcentages que vous avez définis. L'affectation étant aléatoire, la distribution réelle peut ne pas correspondre exactement à vos pourcentages, en particulier avec des échantillons de petite taille.

## Fonctionnement {#how-it-works}

La distribution entre les variantes n'est pas toujours uniforme. À chaque envoi de message dans une campagne multivariée, Braze sélectionne indépendamment une option aléatoire en fonction des pourcentages que vous avez définis et affecte une variante en fonction du résultat. C'est comme un tirage à pile ou face : des anomalies sont possibles. Si vous lancez une pièce 100 fois, vous n'obtiendrez probablement pas une répartition exacte de 50-50 entre pile et face, même avec seulement deux possibilités. Vous pourriez obtenir 52 fois pile et 48 fois face.

De même, si vous souhaitez répartir plusieurs variantes de manière égale en utilisant des pourcentages entiers, assurez-vous que le nombre de variantes divise 100 de manière égale. Dans le cas contraire, certaines variantes auront un pourcentage d'utilisateurs plus élevé que d'autres. Par exemple, si votre campagne comporte sept variantes, il ne peut pas y avoir de distribution égale, car sept ne divise pas 100 en un nombre entier. Dans ce cas, vous auriez deux variantes à 15 % et cinq variantes à 14 %.

{% alert tip %}
Pour répartir les utilisateurs dans un Canvas, vous pouvez ajouter une [étape de l'arbre décisionnel]({{site.baseurl}}/decision_split/) et séparer les utilisateurs en fonction de leurs [numéros de compartiment aléatoires]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/).
{% endalert %}

## Distribution des messages in-app {#in-app-message-distribution}

Lors d'un test A/B sur des messages in-app, vos données analytiques peuvent sembler montrer une distribution plus élevée entre une variante et une autre, même si elles ont un pourcentage de répartition égal. Prenons par exemple le graphique suivant des *destinataires uniques* pour la variante A et la variante C.

![Graphique des destinataires uniques montrant que la variante A a un nombre systématiquement plus élevé que la variante C, malgré un pourcentage de répartition égal.]({% image_buster /assets/img/variant_distribution_iam.png %})

La variante A a un nombre de *destinataires uniques* systématiquement plus élevé que la variante C. Cela n'est pas dû à la distribution des variantes, mais plutôt à la façon dont les *destinataires uniques* sont calculés pour les messages in-app. Pour les messages in-app, les *destinataires uniques* correspondent en réalité aux *impressions uniques*, c'est-à-dire le nombre total de personnes qui ont reçu et consulté le message in-app. Cela signifie que si un utilisateur ne reçoit pas le message pour une raison quelconque ou choisit de ne pas le consulter, il n'est pas comptabilisé dans les *destinataires uniques*, et la distribution des variantes peut sembler biaisée.