---
nav_title: Performances des canaux
article_title: Tableaux de bord des performances des canaux
page_order: 2
page_type: reference
description: "Cet article de référence présente le tableau de bord des performances des canaux, qui vous permet de consulter les indicateurs de performance pour des canaux entiers, aussi bien pour les Campaigns que pour les Canvas."
tool:
  - Reports
toc_headers: h2
---

# Tableaux de bord des performances des canaux {#channel-performance-dashboards}

> Les tableaux de bord des performances des canaux affichent les indicateurs de performance agrégés pour un canal entier, à la fois pour les Campaigns et les Canvas. Ces tableaux de bord sont actuellement disponibles pour l'e-mail, le push et le SMS.

## Tableaux de bord {#dashboards}

Sélectionnez un onglet pour afficher les détails des tableaux de bord de performance disponibles par canal.

{% tabs %}
{% tab Performance e-mail %}

### Tableau de bord de performance e-mail {#email-performance-dashboard}

Consultez votre tableau de bord de performance e-mail en accédant à **Analytics** > **Email Performance**, puis en sélectionnant la plage de dates pour la période dont vous souhaitez afficher les données. Votre plage de dates peut remonter jusqu'à un an en arrière.

{% alert note %}
Pour afficher le tableau de bord **Email Performance**, vous devez disposer de l'autorisation « View Usage Data » ou « View Dashboard Reports ».
{% endalert %}

![Tableau de bord de performance e-mail affichant l'engagement du canal e-mail au cours des trente derniers jours.]({% image_buster /assets/img_archive/email_performance_dashboard_1.png %})

![Exemple de campagne e-mail avec 335 630 envois, soit une moyenne de 11 187,667 par jour.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### Comment les indicateurs sont calculés {#how-metrics-are-calculated}

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="email" %}

| Indicateur | Type | Calcul |
| --- | --- | ---- |
| Envois | Nombre | Nombre total d'envois pour chaque jour de la plage de dates |
| Taux de réception | Taux | (Nombre total de réceptions pour chaque jour de la plage de dates) / (Nombre total d'envois pour chaque jour de la plage de dates) |
| Taux de rebond | Taux | (Nombre total de rebonds pour chaque jour de la plage de dates) / (Nombre total d'envois pour chaque jour de la plage de dates) |
| Taux de désabonnement | Taux | (Nombre total de désabonnements uniques pour chaque jour de la plage de dates) / (Nombre total de réceptions pour la plage de dates)<br><br>Ce calcul utilise les désabonnements uniques, comme dans Campaign Analytics, Overview et le générateur de rapports. Ces désabonnements sont enregistrés depuis toutes les sources (telles que la REST API, les importations CSV, les e-mails et les désabonnements de liste). Les taux de désabonnement dans les analyses de Campaign et Canvas correspondent aux désabonnements résultant d'un clic de désabonnement dans un e-mail envoyé par Braze. |
| Taux d'ouverture unique | Taux | (Nombre total d'ouvertures uniques pour chaque jour de la plage de dates) / (Nombre total de réceptions pour la plage de dates) |
| Taux d'autres ouvertures | Taux | (Nombre total d'autres ouvertures pour chaque jour de la plage de dates) / (Nombre total de réceptions pour la plage de dates)<br><br>Les autres ouvertures correspondent aux e-mails qui n'ont pas été identifiés comme des ouvertures automatiques, par exemple lorsqu'un utilisateur ouvre un e-mail. Cet indicateur n'est pas unique et constitue un sous-indicateur du total des ouvertures. |
| Taux de clics uniques | Taux | (Nombre total de clics uniques pour chaque jour de la plage de dates) / (Nombre total de réceptions pour la plage de dates) |
| Taux de clics par ouverture unique | Taux | (Nombre total de clics uniques pour chaque jour de la plage de dates) / (Nombre total d'ouvertures uniques pour chaque jour de la plage de dates) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Comment les indicateurs sont calculés" }

{% endtab %}
{% tab Informations e-mail %}

### Tableau de bord d'informations e-mail {#email-insights-dashboard}

Le tableau de bord d'informations e-mail suit où et quand vos clients interagissent avec vos e-mails. Ces rapports peuvent fournir des données riches et détaillées sur la manière d'optimiser vos e-mails pour générer davantage d'engagement. Le tableau de bord d'informations e-mail inclut jusqu'à six mois de données. Pour y accéder, rendez-vous dans **Analytics** > **Email Performance** > **Email Insights**.

#### Engagement par appareil {#engagement-by-device}

Le rapport **Engagement by Device** fournit une répartition des appareils que vos utilisateurs emploient pour interagir avec vos e-mails. Ces données suivent l'engagement e-mail sur mobile, ordinateur de bureau, tablette et autres types d'appareils. Ces données reposent sur la chaîne d'agent utilisateur transmise par les appareils de vos utilisateurs.

{% alert note %}
Si vous utilisez CloudFront comme CDN, assurez-vous que l'agent utilisateur de vos utilisateurs est bien transmis au fournisseur de services e-mail (fournisseur de services d'e-mailing). Sinon, chaque agent utilisateur sera « Amazon Cloudfront ».
{% endalert %}

La catégorie « Other » inclut toute chaîne d'agent utilisateur qui ne peut être identifiée comme ordinateur de bureau, mobile ou tablette. Par exemple : télévision, voiture, console de jeux vidéo, OTT (over-the-top ou streaming), et similaires. Cette catégorie peut également inclure des valeurs nulles ou vides.

Pour mieux comprendre le contenu de cette catégorie « Other », vous pouvez extraire les agents utilisateurs à l'aide de l'une de ces options :

1. [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) vous enverra la chaîne d'agent utilisateur exacte récupérée depuis les appareils de vos utilisateurs.
2. Exploitez notre [générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder) pour utiliser SQL ou notre [générateur de requêtes IA]({{site.baseurl}}/user_guide/analytics/reports/query_builder#generating-sql-with-the-ai-query-builder) afin de consulter les agents utilisateurs.

![Rapport Engagement by Device affichant le nombre de clics pour mobile, ordinateur de bureau, tablette et autres appareils. Le plus grand nombre de clics provient des appareils mobiles.]({% image_buster /assets/img/engagement_by_device_type.png %}){: style="max-width:70%;"}

Pour les ouvertures d'e-mails, Braze distingue Google Image Proxy, Apple Image Proxy et Yahoo Mail Proxy. Ces services mettent en cache et chargent toutes les images intégrées dans un e-mail avant sa livraison au destinataire. En conséquence, cela déclenche une ouverture d'e-mail depuis les serveurs du fournisseur de messagerie plutôt que depuis le serveur du destinataire, ce qui peut entraîner un gonflement des ouvertures d'e-mails. Ces services visent à améliorer la confidentialité, la sécurité, la performance et l'efficacité lors du chargement des images. Ils peuvent également contenir de réelles ouvertures de la part des destinataires, car ces services proxy masquent l'agent utilisateur, et Braze catégorise les données proxy à partir de l'agent utilisateur.

![Rapport Engagement by Device affichant le nombre de clics pour Mobile, Desktop, Tablet, Apple Privacy Proxy, Google Image Proxy, Yahoo Mail Proxy et Other. Le plus grand nombre d'ouvertures provient des appareils mobiles.]({% image_buster /assets/img/engagement_by_device_type_proxy.png %}){: style="max-width:70%;"}

#### Engagement par fournisseur de messagerie {#engagement-by-mailbox-provider}

Le rapport **Engagement by Mailbox Provider** affiche les principaux fournisseurs de messagerie contribuant à vos clics ou ouvertures. Vous pouvez cliquer sur des fournisseurs de messagerie spécifiques pour accéder aux détails de domaines de réception spécifiques. Par exemple, si Microsoft figure dans ce rapport parmi vos principaux fournisseurs de messagerie, vous pouvez consulter les détails de leurs domaines de réception, tels que « outlook.com », « hotmail.com », « en direct.com », et bien d'autres.

![Exemple de rapport Engagement by Mailbox Provider avec Google, Apple iCloud, Yahoo, Microsoft et Mail.Ru Group et leur nombre de clics correspondant.]({% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}){: style="max-width:70%;"}

#### Moment de l'engagement {#time-of-engagement}

Le rapport **Time of Engagement** affiche des données sur le moment où les utilisateurs interagissent avec vos e-mails. Cela peut aider à répondre à des questions telles que quel jour de la semaine ou quelle heure génère le plus d'engagement de la part de vos clients. Grâce à ces informations, vous pouvez expérimenter pour trouver le meilleur jour ou la meilleure heure pour envoyer vos messages et générer davantage d'engagement. Notez que ces horaires sont basés sur le fuseau horaire de votre entreprise.

Le rapport d'engagement **Day of the week** répartit les ouvertures ou les clics par jour de la semaine.

![Exemple de rapport d'engagement par jour de la semaine avec le plus de clics le lundi et le mercredi.]({% image_buster /assets/img_archive/time_engagement.png %})

Le rapport d'engagement **Time of the day** répartit les ouvertures ou les clics par heure sur une fenêtre de 24 heures.

![Exemple de rapport d'engagement par heure de la journée avec les ouvertures ou clics de 0 h à 23 h.]({% image_buster /assets/img_archive/time_engagement_day.png %})

Pour en savoir plus sur les analyses de vos e-mails, consultez [Rapports e-mail]({{site.baseurl}}/user_guide/channels/email/reporting).

{% endtab %}
{% tab Performance SMS %}

### Tableau de bord de performance SMS {#sms-performance-dashboard}

Pour utiliser votre tableau de bord de performance SMS, accédez à **Analytics** > **SMS Performance**, puis sélectionnez la plage de dates pour la période dont vous souhaitez afficher les données. Votre plage de dates peut remonter jusqu'à un an en arrière.

![Exemple de campagne SMS avec 335 630 envois, soit une moyenne de 11 187,667 par jour.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### Comment les indicateurs sont calculés

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="SMS" %}

| Indicateur | Type | Calcul |
| --- | --- | ---- |
| Envois | Nombre | Nombre total d'envois pour chaque jour de la plage de dates |
| Taux de réceptions confirmées | Taux | (Nombre total de réceptions pour chaque jour de la plage de dates) / (Nombre total d'envois pour chaque jour de la plage de dates) |
| Taux d'échecs de réception | Taux | (Nombre total d'échecs pour chaque jour de la plage de dates) / (Nombre total d'envois pour chaque jour de la plage de dates) |
| Taux de rejets | Taux | (Nombre total de rejets pour chaque jour de la plage de dates) / (Nombre total d'envois pour chaque jour de la plage de dates) |
| Taux de clics | Taux | (Nombre total de clics pour chaque jour de la plage de dates) / (Nombre total de réceptions pour chaque jour de la plage de dates) |
| Total des abonnements | Taux | Nombre total d'abonnements par message entrant pour chaque jour de la plage de dates |
| Total des désabonnements | Taux | Nombre total de désabonnements par message entrant pour chaque jour de la plage de dates |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Comment les indicateurs sont calculés" }

{% endtab %}
{% tab Performance push %}

### Tableau de bord de performance push {#push-performance-dashboard}

Le tableau de bord **Push Performance** vous offre une vue au niveau du canal de l'engagement push pour toutes vos Campaigns et Canvas, afin que vous puissiez comprendre la santé du canal sans avoir à agréger les données de messages individuels.

Pour ouvrir le tableau de bord, accédez à **Analytics** > **Push Performance**, puis sélectionnez la plage de dates pour la période dont vous souhaitez afficher les données. Votre plage de dates peut remonter jusqu'à un an en arrière.

![Tableau de bord de performance push affichant l'engagement du canal de notification push au cours des trente derniers jours.]({% image_buster /assets/img_archive/push_performance_dashboard_performance_tab.png %})

#### Aperçu {#overview}

La bannière d'aperçu résume quatre indicateurs principaux pour la plage de dates sélectionnée : *Envois*, *Taux de réception*, *Taux d'ouverture* et *Taux de conversion*. Chaque vignette affiche une valeur principale, un nombre complémentaire et une infobulle contenant des détails statistiques supplémentaires.

Le taux de conversion de ce tableau de bord est limité à votre événement de conversion principal uniquement. Pour analyser les événements de conversion secondaires, utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reports/report_builder).

#### Engagement au fil du temps {#engagement-over-time}

Dans la section Engagement au fil du temps, chaque indicateur est représenté sous forme de graphique linéaire sur la plage de dates sélectionnée :

- Envois
- Total des ouvertures
- Ouvertures directes
- Ouvertures influencées
- Taux d'ouverture directe
- Taux de conversion
- Rebonds

Vous pouvez activer un benchmark sectoriel sur le graphique du taux d'ouverture directe. Les benchmarks sont désactivés par défaut. Pour en savoir plus, consultez [Benchmarking](#benchmarking).

#### Comment les indicateurs sont calculés

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="push" %}

| Indicateur | Type | Calcul |
| --- | --- | ---- |
| Envois | Nombre | Nombre total d'envois pour chaque jour de la plage de dates |
| Taux de réception | Taux | (Nombre total de réceptions pour chaque jour de la plage de dates) / (Nombre total d'envois pour chaque jour de la plage de dates) |
| Taux de rebond | Taux | (Nombre total de rebonds pour chaque jour de la plage de dates) / (Nombre total d'envois pour chaque jour de la plage de dates) |
| Taux d'ouverture directe | Taux | (Nombre total d'ouvertures directes pour chaque jour de la plage de dates) / (Nombre total de réceptions pour chaque jour de la plage de dates) |
| Taux d'ouverture influencée | Taux | (Nombre total d'ouvertures influencées pour chaque jour de la plage de dates) / (Nombre total de réceptions pour chaque jour de la plage de dates) |
| Taux d'ouverture total | Taux | (Nombre total d'ouvertures pour chaque jour de la plage de dates) / (Nombre total de réceptions pour chaque jour de la plage de dates)<br><br>Le total des ouvertures comprend les ouvertures directes et les ouvertures influencées. |
| Taux de conversion | Taux | (Nombre total de conversions principales pour chaque jour de la plage de dates) / (Nombre total de destinataires pour chaque jour de la plage de dates) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Comment les indicateurs sont calculés" }

{% endtab %}
{% tab Informations push %}

### Tableau de bord d'informations push {#push-insights-dashboard}

Le tableau de bord d'informations push met en lumière les tendances dans la façon dont votre audience réagit aux notifications push, afin que vous puissiez ajuster ce que vous envoyez et à quelle fréquence. Pour y accéder, rendez-vous dans **Analytics** > **Push Performance** > **Insights**.

#### Fréquence {#frequency}

Le rapport de fréquence montre la relation entre le nombre de notifications push qu'un utilisateur reçoit et son taux d'ouverture, afin que vous puissiez identifier le seuil au-delà duquel les envois supplémentaires cessent de générer de l'engagement. Le graphique met en évidence un volume d'envoi recommandé basé sur les données de benchmark pour votre secteur.

{% alert important %}
Les rapports de fréquence et de cadence utilisent une fenêtre d'analyse minimale de trois mois. Si vous sélectionnez une plage de dates plus courte, Braze peut étendre la date de début pour inclure jusqu'à trois mois de données lorsqu'elles sont disponibles. Ces rapports ne sont pas affectés par les filtres de tags, de Campaigns, de Canvas ou de plateforme : ils reflètent toujours l'intégralité de votre volume push pour la plage de dates sélectionnée.
{% endalert %}

#### Cadence {#cadence}

Alors que le rapport de fréquence vous indique combien de messages envoyer, le rapport de cadence vous indique comment les espacer. Il trace le taux d'ouverture en fonction de la cadence d'envoi, afin que vous puissiez voir si le regroupement de vos envois — par exemple, trois notifications push arrivant toutes le week-end — nuit à votre engagement par rapport à une répartition sur la semaine.

Utilisez-le conjointement avec le rapport de fréquence : la fréquence définit votre objectif de volume, la cadence définit la distribution.

#### Distribution des performances des Campaigns {#campaign-performance-distribution}

Ce rapport trace chaque Campaign push dans votre plage de dates en fonction du taux d'ouverture et du taux de conversion, afin que vous puissiez comparer vos meilleures et plus faibles performances côte à côte et identifier leurs points communs.

Sur le graphique de distribution des performances des Campaigns, cliquez sur l'icône à trois points et sélectionnez **View data table**, ce qui affiche un tableau triable répertoriant les mêmes Campaigns. Vous pouvez trier par taux d'ouverture ou taux de conversion pour classer les performances, et l'utiliser pour ouvrir les analyses d'une Campaign individuelle.

{% endtab %}
{% tab Livrabilité push %}

### Tableau de bord de livrabilité push {#push-deliverability-dashboard}

Le tableau de bord de livrabilité push suit la santé de votre audience push au fil du temps, afin que vous puissiez voir comment votre communication affecte votre base atteignable. Pour y accéder, rendez-vous dans **Analytics** > **Push Performance** > **Deliverability**.

Ce tableau de bord est filtré uniquement par plage de dates, et chaque indicateur est ventilé par plateforme.

#### Taux de rebond {#bounce-rate}

Les rebonds sur votre plage de dates sélectionnée, ventilés par plateforme. Vous pouvez activer un benchmark sectoriel sur ce graphique. Il est désactivé par défaut.

#### Taux de désinstallation {#uninstall-rate}

Les désinstallations sur votre plage de dates sélectionnée, ventilées par plateforme. Utilisez cet indicateur pour voir si une période d'envoi intensif a coïncidé avec la perte d'utilisateurs. Les données de désinstallation dépendent de votre configuration de suivi des désinstallations. Consultez [Suivi des désinstallations]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking). Le suivi des désinstallations est pris en charge pour iOS, Android (hors Huawei) et Kindle. Si le suivi des désinstallations est désactivé, les données de taux de désinstallation sont moins complètes et peuvent être moins précises. Selon le système d'exploitation, les rapports de désinstallation peuvent arriver avec un délai ou par lots, de sorte que le graphique peut ne pas refléter la date exacte de désinstallation.

#### Comment les indicateurs sont calculés

| Indicateur | Type | Calcul |
| --- | --- | ---- |
| Taux de désinstallation | Taux | (Nombre total d'appareils pour lesquels Braze a reçu un signal de désinstallation pour chaque jour de la plage de dates) / (Nombre total d'appareils avec des jetons valides pour chaque jour de la plage de dates) |
| Taux de rebond | Taux | (Nombre total de rebonds pour chaque jour de la plage de dates) / (Nombre total d'envois pour chaque jour de la plage de dates) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Comment les indicateurs sont calculés" }

{% endtab %}
{% endtabs %}

## Filtres du tableau de bord {#dashboard-filters}

Vous pouvez filtrer les données de votre tableau de bord à l'aide des options de filtre suivantes :

- **Étiquette :** Choisissez une étiquette. Une fois appliquée, votre tableau de bord affichera les indicateurs uniquement pour l'étiquette sélectionnée. Notez que le tableau de bord Push prend en charge plusieurs étiquettes.
- **Plateformes :** (Tableaux de bord Push uniquement) Choisissez une plateforme push, telle que **All Push**, **Android**, **iOS**, **Mobile combined**, **Kindle** ou **Web**. Une fois appliquée, votre tableau de bord affiche les indicateurs uniquement pour la plateforme sélectionnée.
- **Canvas :** Choisissez jusqu'à 10 Canvas. Une fois appliqué, votre tableau de bord affichera les indicateurs uniquement pour les Canvas sélectionnés. Si vous sélectionnez d'abord un filtre par étiquette, les options de filtre Canvas n'incluront que les Canvas possédant l'étiquette sélectionnée.
- **Campaign :** Choisissez jusqu'à 10 Campaigns. Une fois appliqué, votre tableau de bord affichera les indicateurs uniquement pour les Campaigns sélectionnées. Si vous sélectionnez d'abord un filtre par étiquette, les options de filtre Campaign n'incluront que les Campaigns possédant l'étiquette sélectionnée.

{% alert note %}
Les filtres s'appliquent différemment selon les tableaux de bord push. Le tableau de bord de performance push prend en charge tous les filtres. Le tableau de bord de livrabilité push prend en charge uniquement la plage de dates, avec une répartition par plateforme affichée sur chaque graphique. Les rapports de fréquence et de cadence du tableau de bord d'informations push prennent en charge uniquement la plage de dates.
{% endalert %}

![Options de filtre sur le tableau de bord de performance des canaux, où vous pouvez sélectionner une étiquette et une liste de Canvas pour filtrer les résultats.]({% image_buster /assets/img_archive/dashboard_filters.png %})

## Comparaison des périodes {#comparing-time-periods}

Le tableau de bord de performance des canaux compare automatiquement la période que vous avez sélectionnée dans la plage de dates avec la période précédente, en totalisant le même nombre de jours. Par exemple, si vous choisissez « 7 derniers jours » comme plage de dates dans le tableau de bord, la comparaison avec la période précédente comparera les indicateurs des sept derniers jours avec ceux des sept jours précédents. Si vous sélectionnez une plage de dates personnalisée — disons du 10 au 15 mai, soit six jours de données — le tableau de bord comparera les indicateurs de ces jours avec ceux du 4 au 9 mai.

La comparaison représente la variation en pourcentage entre la période précédente et la période actuelle, calculée en prenant la différence entre les deux périodes et en la divisant par l'indicateur de la période précédente.

### Afficher les variations des totaux et des taux {#viewing-changes-in-total-counts-and-rates}

Vous pouvez basculer entre **Show Change in Totals** — qui compare les totaux (comme le nombre d'e-mails distribués) entre les deux périodes — et **Show Change in Rates** — qui compare les taux (comme le taux de distribution).

![Boutons radio pour basculer entre l'affichage des variations de totaux ou des variations de taux dans le tableau de bord de performance des canaux.]({% image_buster /assets/img_archive/email_performance_dashboard_3.png %}){: style="max-width:60%"}

## Évaluation comparative {#benchmarking}

Sur les tableaux de bord push, vous pouvez comparer vos performances par rapport à des données agrégées et anonymisées provenant de Braze.

### Évaluations comparatives disponibles {#available-benchmarks}

| Évaluation comparative | Où elle apparaît | Par défaut |
| --- | --- | ---- |
| Taux d'ouverture directe | Performance push | Désactivé |
| Taux de rebond | Livrabilité push | Désactivé |
| Fréquence | Informations push | Activé |
| Cadence | Informations push | Activé |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Évaluations comparatives disponibles" }

Les évaluations comparatives du taux d'ouverture directe et du taux de rebond sont ventilées par plateforme. Toutes les évaluations comparatives push sont mesurées par rapport au taux d'ouverture, et non au taux de conversion.

### Comparaison par secteur d'activité {#comparing-verticals}

Les données d'évaluation comparative sont réparties par secteur d'activité. Votre tableau de bord affiche par défaut le secteur de votre compte, et vous pouvez utiliser le menu déroulant pour comparer avec un autre secteur.

### Comparaison par région {#comparing-regions}

Les données d'évaluation comparative sont réparties par région. Votre tableau de bord affiche par défaut la région de votre compte, et vous pouvez utiliser le menu déroulant pour comparer avec une autre région.

{% alert note %}
Si les dernières données d'évaluation comparative ne sont pas disponibles pour la plage temporelle sélectionnée, Braze affiche une évaluation comparative prédictive.

Les données d'évaluation comparative sont actualisées mensuellement.
{% endalert %}

## Questions fréquentes {#frequently-asked-questions}

### Pourquoi mon tableau de bord affiche-t-il des valeurs vides ? {#why-is-my-dashboard-displaying-empty-values}

Plusieurs scénarios peuvent entraîner des valeurs vides pour un indicateur :

- Braze a enregistré des zéros pour cet indicateur particulier dans la plage de dates sélectionnée.
- Vous n'avez envoyé aucun message pendant la plage de dates sélectionnée.
- Bien qu'il y ait eu des indicateurs tels que des ouvertures, des clics ou des désabonnements pour une plage de dates sélectionnée, il n'y a eu aucune distribution ni aucun envoi. Dans ce cas, Braze ne calculera pas d'indicateur de taux.

Pour voir plus d'indicateurs, essayez d'élargir la plage de dates.

### Pourquoi mon tableau de bord e-mail affiche-t-il plus d'Other Opens que d'Unique Opens ? {#why-does-my-email-dashboard-display-more-other-opens-than-unique-opens}

Pour l'indicateur _Unique Opens_, Braze déduplique toute ouverture répétée enregistrée par un utilisateur donné (qu'elle inclue des _Machine Opens_ ou des _Other Opens_) de sorte qu'une seule _Unique Open_ est incrémentée si un utilisateur ouvre plusieurs fois. Pour les _Other Opens_, Braze ne déduplique pas.

### Pourquoi mes rapports de fréquence et de cadence sont-ils vides ? {#why-are-my-frequency-and-cadence-reports-empty}

Ces rapports utilisent une fenêtre d'analyse de trois mois. Si la plage sélectionnée est plus courte, Braze peut élargir la plage pour inclure des dates antérieures lorsque des données sont disponibles.

Si votre plage de dates est suffisamment longue et que les rapports sont toujours vides, les données de référence ne sont peut-être pas encore disponibles pour votre espace de travail. Contactez le support Braze si vous avez des questions.

### Pourquoi mes filtres ne modifient-ils pas les rapports de fréquence et de cadence ? {#why-dont-my-filters-change-the-frequency-and-cadence-reports}

Les rapports de fréquence et de cadence reflètent toujours l'intégralité de votre volume de notifications push, car leur valeur provient de la mesure de la charge totale de messages pour un utilisateur. Filtrer sur un sous-ensemble de Campaigns sous-estimerait le nombre de messages que cet utilisateur a réellement reçus. Seul le filtre de plage de dates s'applique.
<!---Temporarily hidden until functionality is added

## Valeurs vides dans vos données {#empty-values-in-your-data}

### Si un indicateur affiche « 0 % » ou « 0 » {#if-a-metric-displays-0-or-0}

Cela signifie que Braze a enregistré zéro pour cet indicateur particulier pendant la période que vous avez sélectionnée.

#### Si un indicateur affiche « N/A » {#if-a-metric-displays-na}

Cela signifie que, bien que Braze ait enregistré des valeurs positives pour un indicateur particulier pendant la période que vous avez sélectionnée, le dénominateur du calcul du taux (soit les envois, soit les réceptions dans la plupart des cas) était égal à zéro. Cela peut se produire lorsque des e-mails sont envoyés un jour donné et que les ouvertures et les clics sont enregistrés les jours suivants, si la période sélectionnée n'inclut pas la date d'envoi des messages.

#### Si un indicateur affiche « -- » {#if-a-metric-displays}

Cela signifie que Braze n'a enregistré aucune donnée pour cet indicateur pendant la période que vous avez sélectionnée. Si vous n'avez pas encore configuré ou envoyé d'e-mails, consultez notre section dédiée [E-mail]({{site.baseurl}}/user_guide/channels/email) pour en savoir plus.

--->