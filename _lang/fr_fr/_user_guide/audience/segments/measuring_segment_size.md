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

## Calcul de l'appartenance à un Segment {#segment-membership-calculation}

Braze met à jour l'appartenance d'un utilisateur à un Segment au fur et à mesure que les données sont renvoyées à nos serveurs et traitées, généralement de manière instantanée. L'appartenance d'un utilisateur à un Segment ne changera pas tant que cette session n'aura pas été traitée. Par exemple, un utilisateur qui fait partie d'un Segment d'utilisateurs dormants au début de la session sera immédiatement retiré de ce Segment d'utilisateurs dormants une fois la session traitée.

### Calcul du nombre total d'utilisateurs joignables {#total-reachable-users-calculation}

Chaque Segment affiche le nombre total d'utilisateurs qui en sont membres. Lors du filtrage par **Utilisateurs de toutes les applications**, il affiche également certains des canaux de communication les plus fréquemment utilisés (tels que la notification push Web ou l'e-mail) et le nombre d'utilisateurs joignables pour ces canaux spécifiques.

Il est possible que le nombre total d'utilisateurs soit différent du nombre d'utilisateurs joignables par chaque canal. De plus, tous les canaux ne sont pas répertoriés dans le tableau des utilisateurs joignables. Par exemple, les Content Cards, les webhooks et WhatsApp ne sont pas affichés dans la ventilation. Cela signifie que le nombre total d'utilisateurs joignables peut être supérieur à la somme des utilisateurs pour chaque canal affiché.

![Un tableau affichant le nombre total d'utilisateurs joignables, ventilé par utilisateurs joignables par e-mail, notification push iOS, notification push Android, notification push Web et notification push Kindle.]({% image_buster /assets/img_archive/segmenter_reachable_users.png %})

Pour qu'un utilisateur soit répertorié comme joignable via un certain canal, il doit remplir ces deux conditions :
* Disposer d'une adresse e-mail valide ou d'un jeton de notification push associé à son profil, et
* Avoir accepté de recevoir des communications ou être abonné à votre application.

Un même utilisateur peut appartenir à différents groupes d'utilisateurs joignables. Par exemple, un utilisateur peut avoir à la fois une adresse e-mail valide et un jeton de notification push Android valide, et avoir accepté les deux, mais ne pas avoir de jeton de notification push iOS associé. L'écart entre le nombre total d'utilisateurs joignables et la somme des différents canaux correspond au nombre d'utilisateurs qui remplissent les critères du Segment mais qui ne sont pas joignables via ces canaux de communication.

{% alert note %}
Le **nombre total d'utilisateurs joignables** inclut toutes les personnes correspondant aux filtres de votre Segment, même si elles ne sont plus abonnées à un canal. Les lignes de canaux telles que **iOS** comptent les utilisateurs joignables uniquement sur ce canal selon les règles décrites dans [Utilisateurs joignables par canal](#reachable-users-by-channel). Pour aligner les totaux du Segment avec les utilisateurs abonnés, ajoutez des filtres tels que **Push activé pour iOS** est vrai (ou l'équivalent pour votre canal).
{% endalert %}

## Statistiques sur la taille des segments {#statistics-for-segment-size}

Les statistiques estimées sont approximées en échantillonnant uniquement une partie de votre segment. Vous devez donc vous attendre à des tailles estimées supérieures ou inférieures à la valeur réelle, les espaces de travail plus importants présentant potentiellement des marges d'erreur plus grandes. Pour obtenir un décompte précis des utilisateurs de votre segment, sélectionnez **Calculer les statistiques exactes**. L'appartenance exacte au segment est toujours calculée avant qu'un segment ne soit affecté par un message envoyé dans une Campaign ou un Canvas.

Braze fournit les statistiques suivantes sur la taille des segments.

### Statistiques de filtre {#filter-statistics}

Pour chaque groupe de filtres, vous pouvez consulter le nombre estimé d'utilisateurs joignables. Sélectionnez **Développer les statistiques d'entonnoir supplémentaires** pour afficher une répartition par canal.

![Un groupe de filtres avec un filtre pour les utilisateurs ayant exactement un nombre de sessions égal à un.]({% image_buster /assets/img_archive/segment_filter_stats.png %})

## Estimation des utilisateurs joignables {#reachable-users-estimate}

Vous pouvez consulter l'estimation des utilisateurs joignables pour l'ensemble d'un Segment, y compris les estimations du nombre d'utilisateurs par canal, dans le panneau latéral **Utilisateurs joignables**. Cette estimation vous indique une fourchette approximative de la taille de votre Segment, ainsi qu'une estimation du pourcentage de votre base d'utilisateurs globale qui appartient à ce Segment. Notez que les statistiques estimées sont mises en cache pendant 15 minutes, sauf si vous apportez des modifications à votre Segment, auquel cas les statistiques estimées se mettront automatiquement à jour. Vous pouvez également consulter un décompte exact des utilisateurs joignables (pour le Segment dans son ensemble et par canal) en sélectionnant **Calculer les statistiques exactes**.

{% alert note %}
Les espaces de travail comptant plus de 50 000 utilisateurs affichent **Utilisateurs estimés** ; les espaces de travail plus petits affichent **Utilisateurs exacts**.
{% endalert %}

![Le panneau « Utilisateurs joignables » indiquant qu'il y a entre 2,3 M et 2,4 M d'utilisateurs estimés.]({% image_buster /assets/img_archive/reachable_users_side_panel.png %})

### Considérations relatives aux estimations {#considerations-for-estimate-counts}

Braze mesure le nombre d'utilisateurs estimés en interrogeant un sous-ensemble de vos utilisateurs, puis en extrapolant ces résultats à l'ensemble de votre audience. Étant donné que le sous-ensemble d'utilisateurs interrogé par Braze peut varier à chaque calcul de cette estimation, l'estimation peut également changer dans les cas où la composition de votre audience n'aurait techniquement pas dû évoluer. Par exemple, si vous réorganisez vos filtres ou vérifiez le même Segment à un moment différent, il est possible que le décompte estimé change (même si **Calculer les statistiques exactes** révélerait les mêmes résultats si votre Segment n'a pas changé).

Si vous disposez d'une population d'utilisateurs importante dans votre espace de travail, vous pourriez observer davantage de variations entre vos décomptes estimés et vos décomptes exacts, en particulier dans les cas où votre Segment représente un très faible pourcentage de la population globale de votre espace de travail. Cela s'explique par le fait que Braze mesure l'estimation en interrogeant un sous-ensemble de vos utilisateurs et en extrapolant les résultats à l'ensemble de votre base d'utilisateurs. Pour les bases d'utilisateurs plus importantes, des écarts plus marqués entre les décomptes estimés et exacts sont à prévoir.

Les très petits Segments auront une fourchette estimée incluant 0, ce qui signifie que le pourcentage du total des utilisateurs peut être arrondi à 0. Dans ces cas, **Calculer les statistiques exactes** vous aidera à obtenir un décompte précis de la taille de votre Segment, qui peut ne pas être réellement de 0.

![Le panneau latéral « Utilisateurs joignables » affichant un décompte exact d'utilisateurs de « 31 ».]({% image_buster /assets/img_archive/reachable_users_panel.png %})

### Utilisateurs joignables par canal {#reachable-users-by-channel}

Pour consulter le nombre d'utilisateurs joignables pour chaque canal de communication, sélectionnez **Afficher le détail** dans le panneau **Utilisateurs joignables**. Cela affiche certains des canaux de communication les plus fréquemment utilisés (tels que la notification push Web ou l'e-mail) ainsi que le nombre d'utilisateurs joignables pour ces canaux spécifiques.

La métrique _Total_ représente les utilisateurs uniques. Par exemple, si un utilisateur dispose à la fois de la notification push Android et de la notification push iOS, il sera comptabilisé dans ces deux lignes, mais ne comptera qu'une seule fois dans la ligne _Total_.

Cependant, il est possible que le nombre total d'utilisateurs diffère de la somme des utilisateurs joignables par chaque canal, car un même utilisateur peut appartenir à différents groupes d'utilisateurs joignables. Par exemple, un utilisateur peut disposer à la fois d'une adresse e-mail valide et d'un jeton de notification push Android valide, être abonné aux deux, mais ne pas avoir de jeton de notification push iOS associé.

Gardez à l'esprit que tous les canaux ne sont pas répertoriés dans le tableau **Utilisateurs joignables** (comme les Content Cards, les webhooks et WhatsApp). Par exemple, si certains de vos utilisateurs ne sont joignables que via WhatsApp, ils seront reflétés dans le _Total_ mais pas dans les lignes spécifiques à un canal. Cela signifie que le nombre total d'utilisateurs joignables peut être différent de la somme des utilisateurs pour chaque canal affiché.

Dans les cas où le _Total_ est supérieur à la somme des canaux, l'écart représente le nombre d'utilisateurs qui remplissent les critères du Segment mais ne sont pas joignables via ces canaux de communication.

Pour qu'un utilisateur soit considéré comme joignable via un canal donné, il doit :
- Disposer d'une adresse e-mail ou d'un jeton de notification push valide associé à son profil, et
- Avoir accepté de recevoir des communications ou être abonné à votre application.

#### Filtres appliqués pour les utilisateurs joignables par canal {#applied-filters-for-channel-specific-reachable-users}

Les filtres suivants sont appliqués pour chaque canal lors de la détermination des utilisateurs joignables.

| Canal | Filtre |
| --- | --- |
| E-mail | **Email Available** est vrai. |
| Notification push | **Foreground Push Enabled** est vrai. |
| SMS | **Subscription Group** correspond à n'importe quel groupe d'abonnement SMS. **Invalid Phone Number** est faux. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Filtres appliqués pour les utilisateurs joignables par canal" }

## Calcul des statistiques exactes {#calculating-exact-statistics}

Pour afficher un décompte précis du nombre d'utilisateurs dans votre segment, sélectionnez **Calculer les statistiques exactes** dans le volet **Utilisateurs joignables**.

Pour mettre à jour les statistiques d'un calcul que vous avez précédemment effectué, sélectionnez **Actualiser les statistiques exactes**. La date du dernier calcul sera automatiquement mise à jour.

Notez que la précision d'un calcul n'est que de 99,999 % ou plus. Ainsi, pour les grands Segments, vous pouvez constater de légères variations — même lors du calcul des statistiques exactes — ce qui est un comportement normal. De plus, les résultats des statistiques exactes sont mis en cache pendant 24 heures, sauf si vous apportez des modifications à votre Segment, auquel cas vous pouvez recalculer les statistiques exactes.

{% alert note %}
Les Segments divisés de manière égale par des [numéros de compartiment aléatoires]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) n'auront pas la même taille. Par exemple, si vous créez un Segment avec le filtre **Numéro de compartiment aléatoire inférieur à 5000** et un Segment avec le filtre **Numéro de compartiment aléatoire supérieur ou égal à 5000**, il est possible et attendu que les tailles des Segments varient de quelques points de pourcentage. Cela est dû à des situations telles que la suppression d'utilisateurs inactifs et des utilisateurs injoignables.
{% endalert %}

![Capture d'écran du volet Utilisateurs joignables affichant les statistiques exactes et un menu de répartition développé.]({% image_buster /assets/img_archive/reachable_users_breakdown.png %})

Les statistiques au niveau de chaque filtre seront toujours estimées, même si vous calculez les statistiques exactes. **Calculer les statistiques exactes** ne calcule les statistiques exactes qu'au niveau du Segment, et non au niveau du filtre ou du groupe de filtres. Ce calcul peut prendre quelques minutes. Les espaces de travail plus importants peuvent nécessiter des périodes plus longues pour terminer les calculs. Vous pouvez suivre votre progression sur la barre de progression dans le volet **Utilisateurs joignables**. Lorsqu'un calcul devrait prendre plus de cinq minutes, Braze vous enverra les résultats par e-mail.

Braze priorise un calcul à la fois par espace de travail, donc l'exécution de plusieurs calculs simultanément entraînera des retards. Vous pouvez sélectionner **Afficher la file d'attente des calculs** pour voir quels Segments sont devant le vôtre, leur progression et leur initiateur, et avoir une idée du moment où votre calcul pourra être priorisé.

![Une file d'attente de calculs avec un seul calcul.]({% image_buster /assets/img_archive/calculation_queue.png %})

Vous pouvez annuler un calcul de statistiques exactes en sélectionnant **Annuler**. Cela peut être utile s'il y a plusieurs calculs dans la file d'attente et que vous souhaitez prioriser un autre calcul en premier.

## Consultation de l'historique de la taille d'un Segment {#viewing-historical-segment-membership-size}

Pour tous les Segments, vous pouvez consulter un graphique d'historique des membres qui affiche l'estimation du nombre de membres du Segment pour chaque jour. Ce graphique montre comment la taille de votre Segment a évolué au fil du temps. Utilisez le menu déroulant pour filtrer les membres du Segment par plage de dates.

![Utilisez le menu déroulant Historique des membres pour filtrer les membres du Segment par plage de dates.]({% image_buster /assets/img_archive/historical_membership2.png %})

L'objectif de ce graphique étant de vous donner une vue d'ensemble des tendances de l'effectif du Segment, le décompte quotidien est une estimation, de la même manière que la taille du Segment est une estimation avant que vous ne sélectionniez **Calculer les statistiques exactes**. Et comme ce graphique affiche des estimations, il est possible que la taille de votre Segment apparaisse comme « 0 » dans ce graphique, même si sa taille réelle (qui peut être déterminée après avoir sélectionné **Calculer les statistiques exactes**) n'est pas « 0 ». Il est particulièrement probable que le graphique affiche une estimation de « 0 » si votre Segment est très petit par rapport à la taille de la population de votre espace de travail.

Par exemple, supposons que votre espace de travail contienne 100 millions d'utilisateurs et que votre Segment compte environ 700 utilisateurs. Il est possible que certains jours, aucun utilisateur ne se trouve dans le Segment et qu'aucun utilisateur ne tombe dans la plage de numéros de compartiment aléatoires utilisée pour l'estimation de l'historique des membres, ce qui donne un décompte de 0 membre pour cette journée.

Braze estime le nombre de membres du Segment en interrogeant un sous-ensemble de vos utilisateurs, puis en extrapolant ces résultats à l'ensemble de votre audience. Cela signifie que les résultats du graphique ne fournissent qu'une estimation de ce que pourrait être l'effectif du Segment ce jour-là, et il est normal que cette estimation fluctue d'un jour à l'autre, car un échantillon différent d'utilisateurs peut être interrogé chaque jour.

{% alert note %}
Toutes les estimations peuvent être supérieures ou inférieures à la valeur affichée d'environ 1 % de la taille totale de la population de votre espace de travail. Les espaces de travail plus importants, avec davantage d'utilisateurs, sont plus susceptibles de présenter des estimations qui diffèrent des calculs exacts d'un montant numérique plus élevé, même si la différence reste de 1 % de la population d'utilisateurs de l'espace de travail. Cela signifie que des écarts plus importants entre les estimations et les décomptes exacts dans les grands espaces de travail sont à prévoir.
{% endalert %}

### Raisons de changements significatifs {#reasons-for-significant-changes}

Le nombre de membres peut changer de manière significative pour plusieurs raisons, comme celles présentées dans ce tableau.

| Raison | Exemple |
| --- | --- |
| Comportement normal des utilisateurs | Des utilisateurs s'abonnent après une Campaign particulièrement réussie. |
| Importation d'utilisateurs par fichier CSV | Un fichier CSV d'utilisateurs a été importé, augmentant considérablement le nombre de membres du Segment. |
| Modification des critères d'audience du Segment | Les règles d'audience d'un Segment existant (telles que les filtres) ont été modifiées, entraînant des changements significatifs dans l'effectif du Segment. |
| Suppression d'utilisateurs | Un nombre important d'utilisateurs a été supprimé. |
| Synchronisation d'une intégration partenaire avec Braze | Un tiers a envoyé des données à Braze qui ont significativement influencé l'effectif du Segment. |
| Archivage des utilisateurs dormants | Un nombre important de profils inactifs a été archivé. Par exemple, un grand nombre d'utilisateurs importés par fichier CSV n'enregistrent jamais d'activité et sont archivés en même temps. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Raisons de changements significatifs" }