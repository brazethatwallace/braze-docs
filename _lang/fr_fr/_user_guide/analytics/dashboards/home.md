---
nav_title: Accueil
article_title: Tableau de bord Accueil (anciennement Aperçu)
page_order: 1
page_type: reference
description: "Cet article de référence décrit votre tableau de bord Accueil et fournit les définitions des statistiques disponibles sur cette page."
tool:
  - Reports

---

# Tableau de bord Accueil {#home-dashboard}

> La page **Accueil** du tableau de bord fournit des indicateurs clés pour suivre et comprendre les performances de votre application ou site web, et vous offre une vue d'ensemble de votre base d'utilisateurs.

La page **Accueil** comporte deux sections principales :
- [Reprendre là où vous vous étiez arrêté](#pick-up-where-you-left-off)
- [Aperçu des performances](#performance-overview)


## Reprendre là où vous vous étiez arrêté {#pick-up-where-you-left-off}

Vous pouvez reprendre là où vous vous étiez arrêté dans le tableau de bord de Braze grâce à un accès direct aux fichiers que vous avez récemment modifiés ou créés. Cette section apparaît en haut de la page **Accueil** du tableau de bord de Braze.

Vous pouvez revenir aux Campaigns, Canvas et Segments récemment modifiés ou créés. Chaque carte est accompagnée d'étiquettes indiquant le type de contenu (Campaign, Canvas, Segment) et l'état (actif, brouillon, archivé, arrêté).

{% alert note %}
La section **Reprendre là où vous vous étiez arrêté** apparaît après que vous avez modifié ou créé une Campaign, un Canvas ou un Segment.
{% endalert %}

![Un brouillon de Canvas, un Segment actif et un brouillon de Campaign dans la section « Reprendre là où vous vous étiez arrêté ».]({% image_buster /assets/img/pick_up_where_you_left_off.png %})

## Aperçu des performances {#performance-overview}

Par défaut, la section **Aperçu des performances** affiche les données des 30 derniers jours pour l'ensemble des applications et sites. Tous vos indicateurs sont calculés en fonction de la plage de dates sélectionnée.

Les pourcentages sont calculés en comparant la plage de dates actuelle à la plage de dates précédente, à l'exception des *utilisateurs actifs par mois* (MAU), qui utilisent le dernier jour de la période précédente plutôt qu'une plage.

Par exemple, si vous définissez votre plage de dates sur **7 derniers jours** et que vos *utilisateurs actifs quotidiens* affichent une augmentation de 1,8 %, cela signifie que vous avez eu 1,8 % d'utilisateurs actifs quotidiens de plus cette semaine par rapport à la semaine précédente.

![Tuile d'indicateur pour les utilisateurs actifs quotidiens affichant une moyenne de 22,2 milliers avec un badge d'augmentation de 7,1 % et une courbe de tendance.]({% image_buster /assets/img_archive/home_dashboard_metric_tile.png %}){: style="max-width:60%;"}

### Afficher le détail {#show-breakdown}

Sélectionnez **Show Breakdown** pour chaque ligne des statistiques de l'aperçu des performances afin de visualiser la valeur de chaque statistique par jour pour la plage de dates spécifiée.

### Performances dans le temps {#performance-over-time}

Le graphique **Performance Over Time** affiche la valeur de chaque statistique sur la plage de dates spécifiée pour les applications sélectionnées.

![Le graphique Performances dans le temps montrant les statistiques des nouveaux utilisateurs sur 30 jours.]({% image_buster /assets/img/dashboards/performance_over_time.png %})

Vous pouvez tracer des statistiques pour :
- Bannières
- Content Cards
- Utilisateurs actifs quotidiens
  - (Facultatif) Répartition par segment
- E-mail
- Messages in-app
- Formules d'indicateurs clés de performance
  - Sélectionnez **Manage KPI Formulas** pour créer une formule ou modifier une formule existante.
- LINE
- Utilisateurs actifs par mois (MAU)
- Nouveaux utilisateurs
- Notifications push
  - (Facultatif) Répartition par segment
- Sessions
  - (Facultatif) Répartition par segment ou version de l'application
- Sessions par heure
- Sessions par MAU
- SMS
- Adhérence
- Désinstallations
  - (Facultatif) Répartition par segment
- Utilisateurs
- Webhooks
- WhatsApp

## Statistiques disponibles {#available-statistics}

Voici les définitions des statistiques disponibles, leur mode de calcul et leur importance pour vous.

### Utilisateurs {#users}

*Utilisateurs* correspond au nombre total d'utilisateurs créés dans cet espace de travail. Cela inclut tous les utilisateurs ayant utilisé votre application ou site web à un moment donné, ainsi que ceux qui ne sont pas nécessairement associés à une application ou un site web spécifique. Ce nombre représente le pourcentage de vos utilisateurs à vie qui sont des *utilisateurs actifs par mois* (MAU), ce qui est utile pour observer la rétention des utilisateurs sur une longue période.

Un faible ratio MAU/utilisateurs peut indiquer que vous devez diversifier vos canaux de communication ou intensifier vos efforts pour atteindre les utilisateurs en perte d'engagement. Consultez notre guide rapide sur la [reconquête des utilisateurs en perte d'engagement]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/capturing_lapsing_users#capture-lapsing-users) pour en savoir plus. De manière générale, le ratio MAU/utilisateurs à vie diminuera inévitablement au fil du temps en raison de l'attrition, mais les outils de Braze peuvent vous aider à minimiser cet effet en maintenant l'engagement de vos utilisateurs plus longtemps.

### Sessions à vie {#lifetime-sessions}

*Sessions à vie* correspond au nombre total de sessions enregistrées par Braze depuis l'intégration. Une session correspond à chaque utilisation de l'application ou visite de votre site web par un utilisateur. Pour une définition plus précise de la manière dont les sessions sont définies par plateforme, consultez les articles développeur correspondants sur le suivi des sessions pour [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=swift), [Android et FireOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=android) ou [Web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=web).

### Utilisateurs actifs par mois {#monthly-active-users}

*Utilisateurs actifs par mois* (MAU) correspond au nombre d'utilisateurs ayant enregistré une session dans votre application ou site au cours des 30 derniers jours. Les MAU sont calculés chaque nuit avec une fenêtre glissante de 30 jours. Les MAU vous offrent une bonne compréhension de la santé d'une application ou d'un site sur une période prolongée, car ils lissent les incohérences entre les jours d'intensité d'utilisation variable.

Le pourcentage affiché à côté du nombre de MAU indique l'évolution des MAU pour cette période par rapport à la période précédente.

$$\text{Change in MAU} = \frac{\text{MAU of last date in range} - \text{MAU of day before start date}}{\text{MAU of day before start date}}$$

#### Règles de calcul des MAU {#mau-calculation-rules}

Le calcul des MAU suit des règles spécifiques pour garantir une facturation précise et cohérente :

- **Moment du calcul** : calculé une fois par jour à 12h05 UTC sous forme d'instantané sur 30 jours ; les comptages ne changent jamais rétroactivement.
- **Profils anonymes** : comptabilisés **uniquement** lorsqu'au moins une session est enregistrée.
- **Profils identifiés** : comptabilisés uniquement lorsque `date_of_last_session` se situe dans la fenêtre glissante de 30 jours.
- **Profils orphelins** : les doublons fusionnés avec un autre utilisateur ne sont **pas** comptabilisés.
- **Imports CSV et imports via la REST API** : les utilisateurs importés par CSV ou via la REST API sont comptabilisés dans les MAU lorsque vous fournissez `date_of_last_session` dans la fenêtre glissante de 30 jours, ou lorsqu'ils enregistrent ultérieurement une session. Fournir uniquement `date_of_first_session` n'affecte pas les MAU.
- **Suppressions via API** : la suppression d'un utilisateur via l'API ne met pas à jour les MAU immédiatement ; le comptage se corrige automatiquement lors du cycle mensuel suivant.

{% alert note %}
Les utilisateurs anonymes comptent également dans vos MAU. Pour les appareils mobiles, les utilisateurs anonymes dépendent de l'appareil. Pour les utilisateurs web, les utilisateurs anonymes dépendent du cache du navigateur. <br><br> Les comptages de MAU dans Braze peuvent différer de ceux d'outils tels qu'Amplitude lorsque chaque produit utilise une définition différente d'un utilisateur actif. Comparez la configuration dans Amplitude (et vos [règles de calcul des MAU](#mau-calculation-rules)) avant d'investiguer un écart comme un problème de pipeline de données.
{% endalert %}

#### Exemple de calcul des MAU {#mau-calculation-example}

L'exemple suivant illustre le fonctionnement du calcul des MAU à travers différentes actions utilisateur :

| Étape | Action | Variation immédiate des MAU | Total résultant |
|-------|--------|----------------------------|-----------------|
| 1 | Création de l'**Utilisateur anonyme 1** et enregistrement d'une session | +1 | 1 |
| 2 | Identification de l'**Utilisateur anonyme 1** (le profil devient identifié) | 0 | 1 |
| 3 | Création de l'**Utilisateur anonyme 2** et enregistrement d'une session | +1 | 2 |
| 4 | Identification de l'**Utilisateur anonyme 2** comme étant la **même personne** que l'Utilisateur 1 (l'Utilisateur 2 devient orphelin) | –1 | 1 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Exemple de calcul des MAU" }

Les instantanés de MAU sont calculés une fois par jour et ne changent jamais rétroactivement. Dans cet exemple, le nombre de MAU pour le jour suivant l'étape 3 reste définitivement à 2, même si l'Utilisateur 2 devient orphelin par la suite. Cependant, le nombre de MAU pour les jours suivants ne reflète que l'utilisateur non orphelin. Sur une fenêtre de 30 jours, ce flux consomme au final 1 MAU puisqu'il ne reste qu'un seul utilisateur distinct et non orphelin.

##### Considérations relatives au comptage des MAU {#mau-count-considerations}

Les comptages de MAU dans Braze dépendent de l'endroit où vous les consultez. Le total des MAU est calculé au niveau de l'utilisateur, indépendamment des applications et plateformes, de sorte que chaque utilisateur n'est compté qu'une seule fois. Cependant, lorsque vous consultez les comptages de MAU par application, la somme des MAU de toutes les applications peut dépasser votre total de MAU ; un utilisateur qui utilise plusieurs applications dans votre espace de travail est comptabilisé dans l'indicateur MAU individuel de chaque application.

### Utilisateurs actifs quotidiens {#daily-active-users}

*Utilisateurs actifs quotidiens* (DAU) affiche le nombre d'utilisateurs uniques qui enregistrent au moins une session dans votre application ou site un jour donné. Les DAU peuvent être une statistique utile pour examiner la variabilité quotidienne de l'utilisation de votre application ou site et adapter vos campagnes pour qu'elles soient aussi efficaces que possible. Par exemple, l'utilisation de votre application peut connaître un pic notable le week-end, ce qui vous indiquerait que vous pourriez toucher davantage d'utilisateurs avec des messages in-app ces jours-là plutôt qu'en semaine.

### Nouveaux utilisateurs {#new-users}

*Nouveaux utilisateurs* indique le nombre d'utilisateurs qui n'avaient jamais enregistré de session auparavant et qui ont commencé à utiliser votre application ou site. Ce nombre correspond au total des nouveaux utilisateurs sur la période donnée. Cette statistique peut être très utile pour évaluer l'efficacité de vos efforts publicitaires.

{% alert note %}
Lors de l'intégration initiale de Braze, tous les utilisateurs apparaîtront comme de nouveaux utilisateurs, car Braze n'a jamais enregistré de session pour eux auparavant. <br><br> Contrairement aux MAU, le nombre de *Nouveaux utilisateurs* peut diminuer rétroactivement lorsque Braze fusionne un profil anonyme avec un profil identifié et rend le profil anonyme orphelin. Braze retire le profil orphelin des totaux d'utilisation de l'application, ce qui peut réduire le nombre de *Nouveaux utilisateurs* pour des dates que vous avez déjà consultées. Pour en savoir plus sur le comportement de liaison des profils, consultez [Cycle de vie du profil utilisateur]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle).
{% endalert %}

{% alert important %}
Les utilisateurs associés à plusieurs applications sont comptabilisés séparément pour chaque application. Cela signifie qu'un même utilisateur peut contribuer plusieurs fois au nombre de *Nouveaux utilisateurs* s'il démarre des sessions dans différentes applications de votre espace de travail.
{% endalert %}

### Adhérence {#stickiness}

La valeur d'*adhérence* est le ratio entre les DAU et les MAU pour une période donnée. Concrètement, l'adhérence mesure le pourcentage de vos MAU qui reviennent quotidiennement.

Par exemple, si la plage de dates est définie sur 30 jours, un ratio de 50 % indique qu'en moyenne, un utilisateur actif utilise l'application ou le site web 15 jours sur 30, ou qu'environ la moitié de vos utilisateurs actifs reviennent quotidiennement. L'adhérence est un indicateur important de réussite, car la plupart des utilisateurs n'arrêtent pas d'utiliser une application parce qu'ils la détestent, mais plutôt parce qu'elle ne fait pas partie de leur routine quotidienne. Vous pouvez donc utiliser l'adhérence comme indicateur indirect de la qualité de l'engagement de vos utilisateurs.

Le pourcentage affiché à côté du ratio d'adhérence indique l'évolution de l'adhérence pour cette période par rapport à la période précédente.

$$\text{Change in stickiness} = \frac{\text{Stickiness of last period} - \text{Stickiness of this period}}{\text{Stickiness of last period}}$$

Les périodes « précédente » et « actuelle » sont déterminées par la plage de dates que vous sélectionnez.

{% alert important %}
La valeur des MAU est calculée chaque nuit et ne sera mise à jour que le lendemain.
{% endalert %}

### Sessions quotidiennes {#daily-sessions}

*Sessions quotidiennes* correspond au nombre de sessions enregistrées un jour donné. En comparant cette valeur à votre nombre de DAU, vous pouvez déterminer combien de fois vos utilisateurs ouvrent l'application ou visitent votre site web les jours où ils enregistrent au moins une session.

{% alert note %}
Le *nombre de sessions quotidiennes* pour une date donnée peut varier lorsque vous consultez le tableau de bord Accueil à des jours différents. Si un utilisateur démarre une session hors ligne, celle-ci peut ne pas parvenir à Braze tant qu'il n'ouvre pas à nouveau l'application. Lorsque cette session est transmise, Braze l'attribue à la date de début de la session, ce qui peut augmenter rétroactivement le comptage pour cette date.
{% endalert %}

### Sessions quotidiennes par MAU {#daily-sessions-per-mau}

*Sessions quotidiennes par MAU* est le ratio entre les *sessions quotidiennes* et les MAU pour un jour donné. Cette statistique vous indique combien de sessions par jour vous pouvez vous attendre à enregistrer par MAU. Une fois agrégée et moyennée, elle vous donne une idée de la fréquence relative à laquelle vos utilisateurs utilisent votre application ou site. Autrement dit, si vos *sessions quotidiennes par MAU* étaient en moyenne de 0,5, vous pourriez vous attendre à ce que chaque MAU enregistre une session environ tous les 2 jours.