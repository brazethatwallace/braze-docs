---
nav_title: Mesurer la taille d'un segment
article_title: Mesurer la taille d'un segment
page_order: 5
page_type: reference
tool:
- Segments
description: "Cette page explique comment surveiller l'appartenance et la taille de votre segment."
---

# Mesurer la taille d'un segment {#measure-segment-size}

> Cette page explique comment surveiller l'appartenance et la taille de votre segment.

## Calcul de l'appartenance à un segment {#segment-membership-calculation}

Braze met à jour l'appartenance d'un utilisateur à un segment au fur et à mesure que les données sont renvoyées à nos serveurs et traitées, généralement de manière instantanée. L'appartenance d'un utilisateur à un segment ne changera pas tant que cette session n'aura pas été traitée. Par exemple, un utilisateur qui fait partie d'un segment d'utilisateurs dormants au début de la session sera immédiatement retiré de ce segment une fois la session traitée.

### Calcul du nombre total d'utilisateurs pouvant être atteints {#total-reachable-users-calculation}

Chaque segment affiche le nombre total d'utilisateurs qui en sont membres. Lors du filtrage par **Utilisateurs de toutes les applications**, il affiche également certains des canaux de communication les plus fréquemment utilisés (tels que la notification push Web ou l'e-mail) et le nombre d'utilisateurs pouvant être atteints pour ces canaux spécifiques.

Il est possible que le nombre total d'utilisateurs soit différent du nombre d'utilisateurs pouvant être atteints par chaque canal. De plus, tous les canaux ne sont pas répertoriés dans le tableau des utilisateurs pouvant être atteints. Par exemple, les Content Cards, les webhooks et WhatsApp ne sont pas affichés dans la répartition. Cela signifie que le nombre total d'utilisateurs pouvant être atteints peut être supérieur à la somme des utilisateurs pour chaque canal affiché.

![Un tableau affichant le nombre total d'utilisateurs pouvant être atteints, réparti par utilisateurs pouvant être atteints par e-mail, notification push iOS, notification push Android, notification push Web et notification push Kindle.]({% image_buster /assets/img_archive/segmenter_reachable_users.png %})

Pour qu'un utilisateur soit répertorié comme pouvant être atteint via un certain canal, il doit remplir les deux conditions suivantes :
* Avoir une adresse e-mail valide ou un jeton de notification push associé à son profil, et
* Avoir accepté ou être abonné à votre application.

Un même utilisateur peut appartenir à différents groupes d'utilisateurs pouvant être atteints. Par exemple, un utilisateur peut avoir à la fois une adresse e-mail valide et un jeton de notification push Android valide et avoir accepté les deux, mais ne pas avoir de jeton de notification push iOS associé. L'écart entre le nombre total d'utilisateurs pouvant être atteints et la somme des différents canaux correspond au nombre d'utilisateurs qui remplissent les critères du segment mais qui ne sont pas joignables via ces canaux de communication.

{% alert note %}
Le **nombre total d'utilisateurs pouvant être atteints** inclut tous les utilisateurs correspondant aux filtres de votre segment, même s'ils ne sont plus abonnés à un canal. Les lignes de canaux telles que **iOS** comptent les utilisateurs joignables uniquement sur ce canal selon les règles décrites dans [Utilisateurs pouvant être atteints par canal](#reachable-users-by-channel). Pour aligner les totaux du segment avec les utilisateurs abonnés, ajoutez des filtres comme **Push enabled for iOS** est vrai (ou l'équivalent pour votre canal).
{% endalert %}

## Statistiques sur la taille du segment {#statistics-for-segment-size}

Les statistiques estimées sont approximées en échantillonnant uniquement une partie de votre segment. Vous devez donc vous attendre à voir des tailles estimées supérieures ou inférieures à la valeur réelle, les espaces de travail plus importants présentant potentiellement des marges d'erreur plus grandes. Pour obtenir un décompte précis des utilisateurs dans votre segment, sélectionnez **Calculate Exact Statistics**. L'appartenance exacte au segment sera toujours calculée avant qu'un segment ne soit affecté par un message envoyé dans une campagne ou un Canvas.

Braze fournit les statistiques suivantes sur la taille des segments.

### Statistiques de filtre {#filter-statistics}

Pour chaque groupe de filtres, vous pouvez voir les utilisateurs pouvant être atteints estimés. Sélectionnez **Expand extra funnel statistics** pour voir une répartition par canal.

![Un groupe de filtres avec un filtre pour les utilisateurs ayant exactement un nombre de sessions égal à un.]({% image_buster /assets/img_archive/segment_filter_stats.png %})

## Estimation des utilisateurs pouvant être atteints {#reachable-users-estimate}

Vous pouvez consulter l'estimation des utilisateurs pouvant être atteints pour l'ensemble d'un segment, y compris les estimations du nombre d'utilisateurs pour chaque canal, dans le panneau latéral **Reachable users**. Cette **estimation** vous montre une plage approximative pour la taille de votre segment, ainsi qu'une estimation du pourcentage de votre base d'utilisateurs globale qui fait partie de ce segment. Notez que les statistiques estimées sont mises en cache pendant 15 minutes, sauf si vous apportez des modifications à votre segment, auquel cas les statistiques estimées seront automatiquement mises à jour. Vous pouvez également consulter un décompte exact des utilisateurs pouvant être atteints (pour le segment dans son ensemble et par canal) en sélectionnant **Calculate exact statistics**.


![Le panneau « Reachable users » indiquant qu'il y a entre 2,3 M et 2,4 M d'utilisateurs estimés.]({% image_buster /assets/img_archive/reachable_users_side_panel.png %})

### Considérations relatives aux estimations {#considerations-for-estimate-counts}

Braze mesure le nombre d'utilisateurs estimés en interrogeant un sous-ensemble de vos utilisateurs, puis en extrapolant ces résultats à l'ensemble de votre audience. Étant donné que le sous-ensemble d'utilisateurs interrogé par Braze peut différer à chaque calcul de cette estimation, l'estimation peut également changer dans les cas où l'appartenance à votre audience n'aurait techniquement pas dû varier. Par exemple, si vous réorganisez vos filtres ou vérifiez le même segment à un moment différent, il est possible que le décompte estimé change (même si **Calculate exact stats** révélerait les mêmes résultats si votre segment n'a pas changé).

Si vous avez une population d'utilisateurs importante dans votre espace de travail, vous pouvez constater davantage de variations entre vos décomptes estimés et vos décomptes exacts, en particulier dans les cas où votre segment représente un très faible pourcentage de la population globale de votre espace de travail. Cela s'explique par le fait que Braze mesure l'estimation en interrogeant un sous-ensemble de vos utilisateurs et en extrapolant les résultats à l'ensemble de votre base d'utilisateurs. Pour les bases d'utilisateurs plus importantes, des différences plus grandes entre les décomptes estimés et exacts sont à prévoir.

Les très petits segments auront une plage estimée qui inclut 0, ce qui signifie que le pourcentage du nombre total d'utilisateurs peut être arrondi à 0. Dans ces cas, **Calculate exact stats** vous aidera à obtenir un décompte précis de la taille de votre segment, qui peut ne pas être réellement 0.

![Le panneau latéral « Reachable users » affichant un décompte exact d'utilisateurs de « 31 ».]({% image_buster /assets/img_archive/reachable_users_panel.png %})

### Utilisateurs pouvant être atteints par canal {#reachable-users-by-channel}

Pour consulter le nombre d'utilisateurs pouvant être atteints pour chaque canal de communication, sélectionnez **Show breakdown** dans le panneau **Reachable users**. Cela affiche certains des canaux de communication les plus fréquemment utilisés (tels que la notification push Web ou l'e-mail) et le nombre d'utilisateurs pouvant être atteints pour ces canaux spécifiques.

L'indicateur _Total_ représente les utilisateurs uniques. Par exemple, si un utilisateur dispose à la fois d'une notification push Android et d'une notification push iOS, il sera comptabilisé dans ces deux lignes, mais ne comptera qu'une seule fois dans la ligne _Total_.

Cependant, il est possible que le nombre total d'utilisateurs soit différent de la somme des utilisateurs pouvant être atteints par chaque canal, car un même utilisateur peut appartenir à différents groupes d'utilisateurs pouvant être atteints. Par exemple, un utilisateur peut avoir à la fois une adresse e-mail valide et un jeton de notification push Android valide et avoir accepté les deux, mais ne pas avoir de jeton de notification push iOS associé.

Gardez à l'esprit que tous les canaux ne sont pas répertoriés dans le tableau **Reachable users** (tels que les Content Cards, les webhooks et WhatsApp). Par exemple, si vous avez des utilisateurs uniquement joignables via WhatsApp, ils seront reflétés dans le _Total_ mais pas dans les lignes spécifiques à chaque canal. Cela signifie que le nombre total d'utilisateurs pouvant être atteints peut être différent de la somme des utilisateurs pour chaque canal affiché.

Dans les cas où le _Total_ est supérieur à la somme des canaux, l'écart représente le nombre d'utilisateurs qui remplissent les critères du segment mais qui ne sont pas joignables via ces canaux de communication.

Pour qu'un utilisateur soit répertorié comme pouvant être atteint via un certain canal, il doit avoir :
- Une adresse e-mail valide ou un jeton de notification push associé à son profil, et
- Avoir accepté ou être abonné à votre application.

#### Filtres appliqués pour les utilisateurs pouvant être atteints par canal {#applied-filters-for-channel-specific-reachable-users}

Les filtres suivants sont appliqués pour chaque canal lors de la détermination des utilisateurs pouvant être atteints.

| Canal | Filtre |
| --- | --- |
| E-mail | **Email Available** est vrai. |
| Push | **Foreground Push Enabled** est vrai. |
| SMS | **Subscription Group** est n'importe quel groupe d'abonnement SMS. **Invalid Phone Number** est faux. |
{: .reset-td-br_1 .reset-td-br_2 aria-label="Filtres appliqués pour les utilisateurs pouvant être atteints par canal" }

## Calcul des statistiques exactes {#calculating-exact-statistics}

Pour consulter un décompte précis du nombre d'utilisateurs dans votre segment, sélectionnez **Calculate exact stats** dans le panneau **Reachable users**.

Pour mettre à jour les statistiques d'un calcul que vous avez précédemment effectué, sélectionnez **Refresh exact statistics**. La date du dernier calcul sera automatiquement mise à jour.

Notez que la précision d'un calcul n'est que de 99,999 % ou plus. Ainsi, pour les grands segments, vous pouvez constater de légères variations&#8212;même lors du calcul des statistiques exactes&#8212;ce qui est un comportement normal. De plus, les résultats des statistiques exactes sont mis en cache pendant 24 heures, sauf si vous apportez des modifications à votre segment, auquel cas vous pouvez recalculer les statistiques exactes.

{% alert note %}
Les segments divisés de manière égale par des [numéros de compartiment aléatoires]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) n'auront pas la même taille. Par exemple, si vous créez un segment avec le filtre **Random Bucket # less than 5000** et un segment avec le filtre **Random Bucket # at least 5000**, il est possible et attendu que les tailles des segments varient de quelques points de pourcentage. Cela est dû à des situations telles que la suppression d'utilisateurs inactifs et des utilisateurs ne pouvant pas être atteints.
{% endalert %}

![Capture d'écran du panneau Reachable users affichant les statistiques exactes et un menu de répartition développé.]({% image_buster /assets/img_archive/reachable_users_breakdown.png %})

Les statistiques au niveau de chaque filtre seront toujours estimées, même si vous calculez les statistiques exactes. **Calculate exact stats** ne calcule les statistiques exactes qu'au niveau du segment, pas au niveau du filtre ou du groupe de filtres. Ce calcul peut prendre quelques minutes. Les espaces de travail plus importants en particulier peuvent nécessiter des périodes plus longues pour terminer les calculs. Vous pouvez suivre votre progression sur la barre de progression dans le panneau **Reachable users**. Lorsqu'un calcul devrait prendre plus de cinq minutes, Braze vous enverra les résultats par e-mail.

Braze donne la priorité à un calcul à la fois par espace de travail, donc l'exécution de plusieurs calculs simultanément entraînera des retards. Vous pouvez sélectionner **View calculation queue** pour voir quels segments sont avant le vôtre, leur progression et leur initiateur, et avoir une idée du moment où votre calcul pourra être priorisé.

![Une file d'attente de calculs avec un calcul.]({% image_buster /assets/img_archive/calculation_queue.png %})

Vous pouvez annuler un calcul de statistiques exactes en sélectionnant **Cancel**. Cela peut être utile s'il y a plusieurs calculs dans la file d'attente et que vous souhaitez donner la priorité à un autre calcul.


## Consulter l'historique de la taille d'appartenance au segment {#viewing-historical-segment-membership-size}

Pour tous les segments, vous pouvez consulter un graphique d'appartenance historique qui montre l'appartenance estimée au segment pour chaque jour. Ce graphique montre comment la taille de votre segment a évolué au fil du temps. Utilisez le menu déroulant pour filtrer l'appartenance au segment par plage de dates.

![Utilisez le menu déroulant Historical Membership pour filtrer l'appartenance au segment par plage de dates.]({% image_buster /assets/img_archive/historical_membership2.png %})

L'objectif de ce graphique étant de vous donner une idée des tendances globales d'appartenance au segment, le décompte quotidien est une estimation, similaire à la façon dont la taille du segment est une estimation avant que vous ne sélectionniez **Calculate Exact Statistics**. Et comme ce graphique affiche des estimations, il est possible que la taille de votre segment apparaisse comme « 0 » dans ce graphique, même si sa taille réelle (qui peut être déterminée après avoir sélectionné **Calculate Exact Stats**) n'est pas « 0 ». Il est particulièrement probable que le graphique affiche une estimation de « 0 » si votre segment est très petit par rapport à la taille de la population de votre espace de travail.

Par exemple, supposons que votre espace de travail contient 100 millions d'utilisateurs et que votre segment compte environ 700 utilisateurs. Il est possible que certains jours, aucun utilisateur ne se trouve dans le segment, et qu'aucun utilisateur ne tombe dans la plage de compartiments aléatoires utilisée pour l'estimation de l'appartenance historique, ce qui donne un décompte d'appartenance de 0 pour ce jour.

Braze estime le décompte d'appartenance au segment en interrogeant un sous-ensemble de vos utilisateurs, puis en extrapolant ces résultats à l'ensemble de votre audience. Cela signifie que les résultats du graphique ne fournissent qu'une estimation de ce que pourrait être l'appartenance au segment ce jour-là, et qu'il est attendu que les résultats fluctuent d'un jour à l'autre car un échantillon différent d'utilisateurs peut être interrogé pour cette estimation chaque jour.

{% alert note %}
Toutes les estimations peuvent être supérieures ou inférieures à la valeur affichée d'environ 1 % de la taille totale de la population de votre espace de travail. Les espaces de travail plus importants avec plus d'utilisateurs sont plus susceptibles d'avoir des estimations qui peuvent différer des calculs exacts d'un montant numérique plus élevé, même si la différence reste de 1 % de la population d'utilisateurs de l'espace de travail. Cela signifie que des différences plus importantes entre les estimations et les décomptes exacts parmi les grands espaces de travail sont à prévoir.
{% endalert %}

### Raisons des changements significatifs {#reasons-for-significant-changes}

Le décompte d'appartenance peut changer de manière significative pour plusieurs raisons, telles que celles présentées dans ce tableau.

| Raison | Exemple |
| --- | --- |
| Comportement normal des utilisateurs | Des utilisateurs s'abonnent après une campagne particulièrement réussie. |
| Des utilisateurs sont importés par CSV | Un fichier CSV d'utilisateurs a été importé, ce qui a considérablement augmenté l'appartenance au segment. |
| Les critères d'audience du segment sont modifiés | Les règles d'audience d'un segment existant (telles que les filtres) ont été modifiées, entraînant des changements significatifs dans l'appartenance au segment. |
| Des utilisateurs sont supprimés | Un nombre significatif d'utilisateurs a été supprimé. |
| Une intégration partenaire s'est synchronisée avec Braze | Un tiers a envoyé des données à Braze qui ont significativement influencé l'appartenance au segment. |
| Des utilisateurs dormants sont archivés | Un nombre significatif de profils inactifs a été archivé. Par exemple, un grand nombre d'utilisateurs importés par CSV n'enregistrent jamais d'activité et sont archivés en même temps. |
{: .reset-td-br_1 .reset-td-br_2 aria-label="Raisons des changements significatifs" }