---
nav_title: Numéros de compartiment aléatoire
article_title: Numéros de compartiment aléatoire
page_order: 2
page_type: reference
description: "Cet article couvre le concept de numéros de compartiment aléatoire et la manière de les utiliser pour créer des variantes et des groupes de contrôle."
page_type: reference
tool:
  - Campaign
  - Canvas

---

# Numéros de compartiment aléatoire {#random-bucket-numbers}

> Un numéro de compartiment aléatoire est un attribut utilisateur qui peut être utilisé pour créer des segments distribués uniformément d'utilisateurs aléatoires.

## Aperçu {#overview}

Lorsqu'un profil utilisateur est créé dans Braze, un numéro de compartiment aléatoire compris entre 0 et 9999 (inclus) lui est automatiquement attribué. Vous pouvez utiliser ces segments pour tester l'efficacité de plusieurs campagnes ou Canvas sur des groupes d'utilisateurs au fil du temps.

### Utilisation du Groupe de contrôle global {#global-control-group-usage}

Les numéros de compartiment aléatoire sont utilisés dans votre Groupe de contrôle global&#8212;un groupe d'utilisateurs qui ne reçoit aucune campagne ni aucun Canvas. Braze sélectionne aléatoirement plusieurs plages de numéros de compartiment aléatoire et inclut les utilisateurs des compartiments sélectionnés. Les numéros de compartiment aléatoire sont attribués sans pondération ni prise en compte des numéros récemment alloués.

{% alert note %}
Lorsqu'un utilisateur est supprimé puis recréé, un nouveau numéro de compartiment aléatoire lui est attribué, car il est considéré comme un nouvel utilisateur.
{% endalert %}

Si vous avez configuré un Groupe de contrôle global et souhaitez utiliser les numéros de compartiment aléatoire pour d'autres cas d'utilisation, consultez [Points de vigilance]({{site.baseurl}}/user_guide/audience/global_control_group#things-to-watch-for).

### Quand utiliser les numéros de compartiment aléatoire {#when-to-use-random-bucket-numbers}

Si vous souhaitez effectuer des tests à long terme sur l'efficacité de plusieurs campagnes ou Canvas au fil du temps, vous pouvez utiliser les numéros de compartiment aléatoire pour segmenter vos utilisateurs.

### Quand utiliser une autre méthode {#when-to-use-something-else}

Si vous souhaitez segmenter les utilisateurs pour des tests au sein d'une seule campagne ou d'un seul Canvas, utilisez le [test A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests) pour les campagnes. Pour les Canvas, vous pouvez créer différentes [variantes]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-21-add-a-variant) pour des tests au niveau du parcours, ou utiliser les [Chemins d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) pour des tests au niveau des étapes.

## Créer des segments à l'aide des numéros de compartiment aléatoire {#create-segments-using-random-bucket-numbers}

Lors de la [création d'un segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), ajoutez le filtre « Random Bucket # ». Spécifiez ensuite un numéro ou une plage de numéros à inclure dans votre segment.

![Un filtre de segment pour les numéros de compartiment aléatoire inférieurs ou égaux à « 3000 ».]({% image_buster /assets/img_archive/random_buckets_filterexample.png %})

Vous pouvez utiliser ce type de segments si vous souhaitez exécuter un test avec trois variantes différentes et inclure également un groupe de contrôle. Voici un exemple de plan pour créer des segments de taille égale pour trois variantes et un groupe de contrôle :

- Les numéros de compartiment 0 à 2499 correspondent au segment de contrôle
- Les numéros de compartiment 2500 à 4999 correspondent au segment qui recevra la variante 1
- Les numéros de compartiment 5000 à 7499 correspondent au segment qui recevra la variante 2
- Les numéros de compartiment 7500 à 9999 correspondent au segment qui recevra la variante 3

Selon le nombre de segments souhaités et la répartition des utilisateurs dans chaque segment, votre plan peut être différent.

Pour chacun de vos segments de numéros de compartiment aléatoire, y compris le groupe de contrôle, activez le [suivi analytique]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking). Pour évaluer la réussite des variantes par rapport au groupe de contrôle, rendez-vous sur la page des [événements personnalisés]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report) et observez la fréquence à laquelle chaque segment a réalisé certains événements personnalisés.

{% alert tip %}
Lorsque vous utilisez des segments de numéros de compartiment aléatoire dans un Canvas, par exemple comme filtre dans une étape [Arbre décisionnel]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split), assurez-vous que les [critères de sortie]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria) de votre Canvas, les filtres d'audience et les étapes en amont ne ciblent pas des segments qui chevauchent l'une de vos plages de compartiments. Si c'est le cas, les utilisateurs de cette plage risquent d'être retirés de manière disproportionnée avant d'atteindre la division, ce qui entraînerait une répartition inégale entre les chemins.
{% endalert %}

### Réentrée aléatoire de l'audience à l'aide des numéros de compartiment aléatoire {#random-audience-re-entry-using-random-bucket-numbers}

La réentrée aléatoire de l'audience peut être utile pour les [tests A/B]({{site.baseurl}}/user_guide/messaging/ab_testing#what-are-multivariate-and-ab-testing) ou le ciblage de groupes d'utilisateurs spécifiques dans vos campagnes. Pour effectuer une réentrée aléatoire de l'audience avec les numéros de compartiment aléatoire, procédez comme suit :

1. [Créez votre segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).
2. Définissez les compartiments aléatoires. Dans votre campagne ou Canvas, utilisez le filtre de compartiment aléatoire pour diviser votre audience en différents groupes. Par exemple, vous pouvez spécifier exactement deux compartiments aléatoires pour diviser votre audience en deux (50 % des utilisateurs par compartiment).
3. Dans la section **Target Audiences** de votre campagne ou Canvas, spécifiez les paramètres de compartiment aléatoire. Cela permet à Braze d'attribuer automatiquement les utilisateurs aux compartiments appropriés en fonction des pourcentages définis.
4. Mettez en place une logique permettant aux utilisateurs de réintégrer le segment. Par exemple, vous pouvez autoriser les utilisateurs à réintégrer le segment s'ils n'ont pas interagi avec une application depuis 15 jours.
5. Lancez votre campagne et surveillez les performances de chaque compartiment. Vous pouvez analyser des indicateurs tels que les taux d'engagement et les taux de conversion pour déterminer l'efficacité de la réentrée aléatoire de l'audience dans votre cas d'utilisation.