---
nav_title: Cibler les utilisateurs
article_title: Cibler les utilisateurs
page_order: 12
page_type: reference
description: "Cet article de référence explique comment cibler votre audience dans les éditeurs de Campaign et de Canvas."
tool:
    - Campaigns
    - Canvas
---

# Cibler les utilisateurs {#target-users}

> Déterminer comment cibler vos utilisateurs est l'une des étapes les plus cruciales lors de la création d'une Campaign ou d'un Canvas. En comprenant comment segmenter votre audience en fonction de ses comportements, préférences et données démographiques, vous pouvez adapter et personnaliser vos messages.

## Créer une audience cible {#creating-a-target-audience}

### Étape 1 : Choisir les utilisateurs {#step-1-choose-users}

Sous **Options de ciblage**, vous pouvez utiliser les options suivantes pour choisir les utilisateurs que vous souhaitez cibler pour votre Campaign ou Canvas. Seuls les utilisateurs correspondant à vos critères définis recevront le message. Gardez à l'esprit que l'appartenance exacte à un Segment est toujours calculée juste avant l'envoi du message.

{% tabs local %}
{% tab Segment unique %}
Pour cibler les membres d'un Segment précédemment créé, sélectionnez un Segment dans le menu déroulant sous **Cibler des utilisateurs par segment**.
{% endtab %}

{% tab Segments multiples %}
Pour cibler les utilisateurs appartenant à plusieurs Segments précédemment créés, ajoutez plusieurs Segments depuis le menu déroulant sous **Cibler des utilisateurs par segment**. L'audience cible résultante sera composée des utilisateurs appartenant à la fois au premier Segment, au deuxième Segment, au troisième Segment, etc.
{% endtab %}

{% tab Filtres multiples %}
Pour cibler des utilisateurs sans ajouter de Segment, vous pouvez utiliser une série de filtres. Il s'agit d'une audience ad hoc créée lors de la composition du message, ce qui vous permet de ne pas avoir à créer de Segment pour les envois ponctuels.

![Filtres supplémentaires pour un message ciblant les utilisateurs ayant ouvert une application pour la dernière fois dans la journée, n'ayant jamais reçu de Campaign ou d'étape du Canvas, et ayant effectué un achat il y a moins de 30 jours.]({% image_buster /assets/img_archive/additional_filters.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab Segments et filtres %}
Vous pouvez également cibler les utilisateurs d'un ou plusieurs Segments précédemment créés qui correspondent aussi à des filtres supplémentaires. Après avoir sélectionné vos Segments, vous pouvez affiner davantage votre audience dans la section **Filtres supplémentaires**. Ceci est illustré dans la capture d'écran suivante, qui cible les utilisateurs appartenant au Segment « Utilisateurs actifs quotidiens », au Segment « N'a jamais ouvert d'e-mail » et ayant effectué un achat il y a plus de 30 jours.

![Options de ciblage pour un message incluant deux Segments et un filtre supplémentaire pour un dernier achat effectué il y a moins de 30 jours.]({% image_buster /assets/img_archive/target_segmenter.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab Applications spécifiques %}

Vous pouvez envoyer un message de Campaign ou une étape du Canvas à des applications spécifiques, par exemple en envoyant un message in-app ou une notification push uniquement aux applications Android ou iOS.

Cependant, n'oubliez pas qu'il est possible qu'un utilisateur utilise plusieurs applications. Le filtre « Possède l'application » identifie tous les utilisateurs disposant de l'application sélectionnée, mais ne contrôle pas quelles applications reçoivent les messages. Par exemple, si vous appliquez un filtre de Segment où « Possède l'application » est défini sur Android, tout utilisateur possédant également l'application iOS recevra aussi le message sur son application iOS.

![Un filtre pour les utilisateurs possédant l'application « Hello, World (Android) ».]({% image_buster /assets/img_archive/has_app_hello_world.png %}){: style="max-width:60%;"}

Supposons que vous souhaitiez envoyer un message in-app uniquement aux applications Android.

1. Créez un Segment et définissez **Applications et sites web ciblés** sur **Utilisateurs d'applications spécifiques**, puis sélectionnez votre application Android.

![Un Segment ciblant les utilisateurs d'une application spécifique, « Test_Android ».]({% image_buster /assets/img_archive/app_test_android.png %}){: style="max-width:60%;"}

{: start="2"}
2. Dans l'étape **Audiences cibles**, confirmez que votre Segment est ajouté dans la section **Cibler des utilisateurs par segment**.

![L'étape « Audiences cibles » avec un exemple de Segment sélectionné.]({% image_buster /assets/img_archive/target_users_by_segment_example.png %})

{% alert note %}
Cela ne fonctionnera pas si vous ajoutez votre Segment dans la section **Filtres supplémentaires** via un filtre d'appartenance à un Segment. Vous devez référencer directement votre Segment dans **Cibler des utilisateurs par segment** pour envoyer votre message uniquement à cette application.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert tip %}
Pour les Campaigns par e-mail, vous pouvez cibler des groupes initiateurs dans la section **Groupes initiateurs**. Notez que les groupes initiateurs ne sont pas disponibles pour les Campaigns API, bien que vous puissiez inclure des groupes initiateurs via une entrée déclenchée par API dans une Campaign. Pour plus d'informations, consultez [Groupes initiateurs]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups).
{% endalert %}

### Étape 2 : Tester votre audience {#step-2-test-your-audience}

Après avoir ajouté des Segments et des filtres à votre audience, vous pouvez vérifier si votre audience est configurée comme prévu en [recherchant un utilisateur]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) pour confirmer s'il correspond aux critères de l'audience.

![La section « Recherche d'utilisateur » avec un bouton « Rechercher un utilisateur ».]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

#### Résumé de l'audience {#audience-summary}

Le **Résumé de l'audience** affiche un aperçu des personnes composant votre audience cible. Ici, vous pouvez limiter davantage votre audience en définissant un plafond maximum d'utilisateurs ou en [limitant le débit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) de distribution.

![La section « Résumé de l'audience » avec des options pour définir un plafond maximum d'utilisateurs ou limiter le débit de distribution.]({% image_buster /assets/img_archive/audience_summary.png %})

#### Test A/B {#ab-testing}

Dans la section **Test A/B**, vous pouvez configurer un test pour comparer les réponses des utilisateurs à plusieurs versions de la même Campaign marketing. Ces versions partagent des objectifs marketing similaires mais diffèrent par la formulation et le style. L'objectif est d'identifier la version de la Campaign qui accomplit le mieux vos objectifs marketing.

Pour plus d'informations et de bonnes pratiques, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

#### Statistiques de l'audience {#audience-statistics}

Braze fournit des statistiques détaillées sur l'audience des canaux ciblés dans le pied de page. Plus votre base d'utilisateurs est importante, plus le nombre d'**utilisateurs pouvant être atteints** est susceptible d'être une estimation approximative. Le nombre d'utilisateurs pouvant être atteints peut diminuer si vous utilisez un [groupe de contrôle global]({{site.baseurl}}/user_guide/audience/global_control_group) ou si vous configurez des critères d'éligibilité aux messages.

- Pour déterminer un nombre précis d'utilisateurs pouvant être atteints, sélectionnez [Calculer les statistiques exactes]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#calculating-exact-statistics), car cette fonction parcourt chaque utilisateur de votre base.
- Pour voir quel pourcentage de votre base d'utilisateurs est ciblé ou la valeur vie client (LTV) pour ce Segment, sélectionnez **Afficher les statistiques supplémentaires**.

##### Pourquoi le nombre de l'audience cible peut différer du nombre d'utilisateurs pouvant être atteints {#why-the-target-audience-count-could-differ-from-the-reachable-users-count}

{% multi_lang_include audience/segments.md section='Differing audience size' %}

![La section « Population totale » avec des estimations du nombre d'utilisateurs pouvant être atteints pour chaque canal ciblé.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

{% alert note %}
Le calcul des statistiques exactes peut prendre quelques minutes. Cette fonction calcule uniquement les statistiques exactes au niveau du Segment, et non au niveau du filtre ou du groupe de filtres.<br><br>
Pour les Segments volumineux, il est normal d'observer de légères variations même lors du calcul des statistiques exactes. La précision de cette fonctionnalité est estimée à 99,999 % ou plus.
{% endalert %}

## Comment l'audience cible et les critères d'entrée fonctionnent ensemble {#how-target-audience-and-entry-criteria-work-together}

Lorsque vous créez une Campaign ou un Canvas dans Braze, le ciblage s'effectue en deux parties :

1. **Audience cible :** qui est éligible
2. **Critères d'entrée :** ce qui déclenche la distribution

L'ordre est important : Braze vérifie si une personne fait partie de l'audience cible avant d'évaluer les critères d'entrée. Si un utilisateur n'est pas déjà éligible pour l'audience à ce moment-là, il n'entrera pas dans la Campaign ou le Canvas, même s'il déclenche ultérieurement l'événement d'entrée. Considérez l'audience cible comme une salle d'attente : seuls les utilisateurs qui s'y trouvent déjà lorsque le déclencheur se produit peuvent avancer.

### Exemple 1 {#example-1}

Vous souhaitez envoyer une notification push lors de la première session d'un utilisateur.

Vous définissez :

- **Audience cible :** utilisateurs avec un nombre de sessions = 0
- **Événement d'entrée :** début de session

Lorsque l'utilisateur ouvre votre application, Braze constate que son nombre de sessions est désormais de 1 et qu'il ne remplit plus les critères de l'audience. L'événement d'entrée se produit après qu'il soit devenu éligible, donc le message ne sera pas envoyé.

Pour que cela fonctionne, l'utilisateur doit être éligible pour l'audience avant le début de la session (inversez l'audience cible et le déclencheur d'entrée).

### Exemple 2 {#example-2}

Vous souhaitez envoyer un e-mail aux utilisateurs ayant dépensé plus de 10 $ au cours des 7 derniers jours.

Vous définissez :

- **Audience cible :** utilisateurs ayant dépensé plus de 10 $ au cours des 7 derniers jours
- **Événement d'entrée :** tout achat

Imaginons maintenant qu'un utilisateur dépense 12 $ aujourd'hui. Cela ne déclenche pas le message — cela le rend simplement éligible pour entrer dans l'audience. Il ne recevra l'e-mail que s'il effectue un autre achat ultérieurement.

Une meilleure approche consisterait à utiliser une audience plus large et à déplacer le filtre dans les critères d'entrée :

- **Audience :** tous les utilisateurs (ou votre audience de base)
- **Événement d'entrée :** effectuer un achat
- **Filtre d'entrée :** dépenses totales au cours des 7 derniers jours > 10 $

De cette façon, un achat éligible remplit à la fois le filtre et déclenche le message — aucune action supplémentaire n'est requise.

## Bonnes pratiques {#best-practices}

- Assurez-vous que le Segment d'audience inclut les utilisateurs avant que les critères d'entrée ne se produisent.
- Évitez d'utiliser des filtres d'audience qui ne s'appliquent qu'après votre événement. Si un filtre dépend de quelque chose qui se produit au moment du déclencheur (comme « nombre de sessions = 0 »), l'utilisateur peut ne plus être éligible au moment où Braze effectue la vérification.
- Utilisez la logique temporelle de manière réfléchie. Par exemple, si vous souhaitez cibler de nouveaux utilisateurs :
    - Définissez votre audience cible sur « a utilisé l'application pour la première fois au cours des 7 derniers jours ».
    - Définissez votre événement d'entrée sur « début de session ».
    - Ainsi, seuls les utilisateurs encore dans leur première semaine seront éligibles et entreront lorsqu'ils démarreront une session.