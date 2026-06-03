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

Sélectionnez un onglet pour consulter les détails des tableaux de bord de performances des canaux disponibles.

{% tabs %}
{% tab Performances des e-mails %}

### Tableau de bord des performances des e-mails {#email-performance-dashboard}

Consultez votre tableau de bord des performances des e-mails en accédant à **Analytics** > **Email Performance**, puis sélectionnez la plage de dates pour la période souhaitée. Votre plage de dates peut remonter jusqu'à un an en arrière.

![Tableau de bord des performances des e-mails affichant l'engagement du canal e-mail au cours des trente derniers jours.]({% image_buster /assets/img_archive/email_performance_dashboard_1.png %})

![Un exemple de Campaign e-mail avec 335 630 envois, soit une moyenne de 11 187,667 par jour.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### Comment les indicateurs sont calculés {#how-metrics-are-calculated}

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="email" %}

| Indicateur | Type | Calcul |
| --- | --- | ---- |
| Envois | Nombre | Nombre total d'envois pour chaque jour de la plage de dates |
| Taux de distribution | Taux | (Nombre total de distributions pour chaque jour de la plage de dates) / (Nombre total d'envois pour chaque jour de la plage de dates) |
| Taux de rebond | Taux | (Nombre total de rebonds pour chaque jour de la plage de dates) / (Nombre total d'envois pour chaque jour de la plage de dates) |
| Taux de désabonnement | Taux | (Nombre total de désabonnements uniques pour chaque jour de la plage de dates) / (Nombre total de distributions pour la plage de dates)<br><br>Ce calcul utilise les désabonnements uniques, également utilisés dans l'analytique de Campaign, l'aperçu et le Générateur de rapports. Ces désabonnements sont enregistrés depuis toutes les sources (telles que le tableau de bord, la REST API, les imports CSV, les e-mails et les désabonnements par liste). Les taux de désabonnement dans l'analytique des Campaigns et Canvas correspondent aux désabonnements résultant d'un clic sur le lien de désabonnement dans un e-mail envoyé par Braze.  |
| Taux d'ouvertures uniques | Taux | (Nombre total d'ouvertures uniques pour chaque jour de la plage de dates) / (Nombre total de distributions pour la plage de dates) |
| Taux d'autres ouvertures | Taux | (Nombre total d'autres ouvertures pour chaque jour de la plage de dates) / (Nombre total de distributions pour la plage de dates)<br><br>Les autres ouvertures incluent les e-mails qui n'ont pas été identifiés comme des ouvertures automatiques, par exemple lorsqu'un utilisateur ouvre un e-mail. Cet indicateur n'est pas unique et constitue un sous-indicateur du total des ouvertures.  |
| Taux de clics uniques | Taux | (Nombre total de clics uniques pour chaque jour de la plage de dates) / (Nombre total de distributions pour la plage de dates) |
| Taux de clics par ouverture unique | Taux | (Nombre total de clics uniques pour chaque jour de la plage de dates) / (Nombre total d'ouvertures uniques pour chaque jour de la plage de dates) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Comment les indicateurs sont calculés" }

{% endtab %}
{% tab Informations e-mail %}

### Tableau de bord des informations e-mail {#email-insights-dashboard}

Le tableau de bord des informations e-mail indique où et quand vos clients interagissent avec vos e-mails. Ces rapports fournissent des données riches et détaillées pour vous aider à optimiser vos e-mails et générer davantage d'engagement. Ce tableau de bord couvre jusqu'à six mois de données. Pour y accéder, rendez-vous dans **Analytics** > **Email Performance** > **Email Insights**.

#### Engagement par appareil {#engagement-by-device}

Le rapport **Engagement by Device** fournit une répartition des appareils utilisés par vos utilisateurs pour interagir avec vos e-mails. Ces données suivent l'engagement e-mail sur les appareils mobiles, les ordinateurs de bureau, les tablettes et les autres types d'appareils. Elles sont basées sur la chaîne user agent transmise par les appareils de vos utilisateurs.

{% alert note %}
Si vous utilisez CloudFront comme réseau de diffusion de contenu, assurez-vous que le user agent de vos utilisateurs est bien transmis à l'ESP. Sinon, chaque user agent apparaîtra comme « Amazon Cloudfront ».
{% endalert %}

La catégorie « Other » inclut toute chaîne user agent qui ne peut pas être identifiée comme ordinateur de bureau, appareil mobile ou tablette. Par exemple : télévision, voiture, console de jeux vidéo, OTT (over-the-top ou streaming) et similaires. Cela peut également inclure des valeurs nulles ou vides.

Pour mieux comprendre le contenu de cette catégorie « Other », vous pouvez extraire les user agents en utilisant l'une de ces options :

1. [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) vous enverra la chaîne user agent exacte récupérée depuis les appareils de vos utilisateurs.
2. Utilisez notre [Générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder/) pour écrire du SQL ou notre [Générateur de requêtes par intelligence artificielle]({{site.baseurl}}/user_guide/analytics/reports/query_builder/#generating-sql-with-the-ai-query-builder) pour consulter les user agents.

![Rapport Engagement par appareil affichant le nombre de clics pour les appareils mobiles, les ordinateurs de bureau, les tablettes et les autres appareils. Le plus grand nombre de clics provient des appareils mobiles.]({% image_buster /assets/img/engagement_by_device_type.png %}){: style="max-width:70%;"}

Pour les ouvertures d'e-mails, Braze distingue Google Image Proxy, Apple Image Proxy et Yahoo Mail Proxy. Ces services mettent en cache et chargent toutes les images intégrées dans un e-mail avant sa distribution au destinataire. Par conséquent, cela déclenche une ouverture d'e-mail depuis les serveurs du fournisseur de messagerie plutôt que depuis le serveur du destinataire, ce qui peut entraîner un gonflement des ouvertures d'e-mails. Ces services sont conçus pour améliorer la confidentialité, la sécurité, les performances et l'efficacité lors du chargement des images. Ils peuvent également contenir de véritables ouvertures de la part des destinataires, car ces services proxy masquent le user agent, et Braze catégorise les données proxy en utilisant le user agent.

![Rapport Engagement par appareil affichant le nombre d'ouvertures pour les appareils mobiles, les ordinateurs de bureau, les tablettes, Apple Privacy Proxy, Google Image Proxy, Yahoo Mail Proxy et Autre. Le plus grand nombre d'ouvertures provient des appareils mobiles.]({% image_buster /assets/img/engagement_by_device_type_proxy.png %}){: style="max-width:70%;"}

#### Engagement par fournisseur de messagerie {#engagement-by-mailbox-provider}

Le rapport **Engagement by Mailbox Provider** affiche les principaux fournisseurs de messagerie contribuant à vos clics ou ouvertures. Vous pouvez cliquer sur un fournisseur de messagerie spécifique pour afficher le détail des domaines de réception. Par exemple, si Microsoft figure dans ce rapport parmi vos principaux fournisseurs, vous pouvez consulter les détails de leurs domaines de réception, tels que « outlook.com », « hotmail.com », « live.com », et d'autres.

![Un exemple de rapport Engagement par fournisseur de messagerie avec Google, Apple iCloud, Yahoo, Microsoft et Mail.Ru Group et leur nombre de clics correspondant.]({% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}){: style="max-width:70%;"}

#### Moment de l'engagement {#time-of-engagement}

Le rapport **Time of Engagement** affiche les données sur le moment où les utilisateurs interagissent avec vos e-mails. Il peut vous aider à déterminer quel jour de la semaine ou quelle heure génère le plus d'engagement de la part de vos clients. Grâce à ces informations, vous pouvez expérimenter le meilleur jour ou la meilleure heure pour envoyer vos messages et obtenir un engagement plus élevé. Notez que ces horaires sont basés sur le fuseau horaire de votre société.

Le rapport d'engagement **Day of the week** répartit les ouvertures ou les clics par jour de la semaine.

![Un exemple de rapport d'engagement par jour de la semaine avec le plus grand nombre de clics le lundi et le mercredi.]({% image_buster /assets/img_archive/time_engagement.png %})

Le rapport d'engagement **Time of the day** répartit les ouvertures ou les clics par heure sur une fenêtre de 24 heures.

![Un exemple de rapport d'engagement par heure de la journée avec les ouvertures ou clics de minuit à 23 h.]({% image_buster /assets/img_archive/time_engagement_day.png %})

Pour plus d'informations sur l'analytique de vos e-mails, consultez [Rapports e-mail]({{site.baseurl}}/user_guide/channels/email/reporting/).

{% endtab %}
{% tab Performances SMS %}

### Tableau de bord des performances SMS {#sms-performance-dashboard}

Pour utiliser votre tableau de bord des performances SMS, accédez à **Analytics** > **SMS Performance**, puis sélectionnez la plage de dates pour la période souhaitée. Votre plage de dates peut remonter jusqu'à un an en arrière.

![Un exemple de Campaign SMS avec 335 630 envois, soit une moyenne de 11 187,667 par jour.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### Comment les indicateurs sont calculés

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="SMS" %}

| Indicateur | Type | Calcul |
| --- | --- | ---- |
| Envois | Nombre | Nombre total d'envois pour chaque jour de la plage de dates |
| Taux de distributions confirmées | Taux | (Nombre total de distributions pour chaque jour de la plage de dates) / (Nombre total d'envois pour chaque jour de la plage de dates) |
| Taux d'échecs de distribution | Taux | (Nombre total d'échecs pour chaque jour de la plage de dates) / (Nombre total d'envois pour chaque jour de la plage de dates) |
| Taux de rejets | Taux | (Nombre total de rejets pour chaque jour de la plage de dates) / (Nombre total d'envois pour chaque jour de la plage de dates) |
| Taux de clics | Taux | (Nombre total de clics pour chaque jour de la plage de dates) / (Nombre total de distributions pour chaque jour de la plage de dates) |
| Total des abonnements | Taux | Nombre total d'abonnements par message entrant pour chaque jour de la plage de dates |
| Total des désabonnements | Taux | Nombre total de désabonnements par message entrant pour chaque jour de la plage de dates |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Comment les indicateurs sont calculés" }

{% endtab %}
{% tab Performances push %}

### Tableau de bord des performances push {#push-performance-dashboard}

Le tableau de bord **Push Performance** offre une vue unique au niveau du canal de l'engagement push, incluant les envois, les rebonds, les distributions et les taux d'ouvertures directes, influencées et totales sur une fenêtre temporelle configurable. Utilisez-le pour comprendre la santé globale de votre canal push sans avoir à agréger les données de Campaigns ou Canvas individuels.

Pour ouvrir le tableau de bord, accédez à **Analytics** > **Dashboard Builder**, puis sélectionnez **Push Channel Dashboard**. Votre plage de dates peut remonter jusqu'à un an en arrière.

![Un exemple de Campaign push avec plus de 63 millions d'envois.]({% image_buster /assets/img_archive/push_performance_dashboard.png %})

#### Comment les indicateurs sont calculés

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="push" %}

| Indicateur | Type | Calcul |
| --- | --- | ---- |
| Envois | Nombre | Nombre total d'envois pour chaque jour de la plage de dates |
| Taux de rebond | Taux | (Nombre total de rebonds pour chaque jour de la plage de dates) / (Nombre total d'envois pour chaque jour de la plage de dates) |
| Taux de distribution | Taux | (Nombre total de distributions pour chaque jour de la plage de dates) / (Nombre total d'envois pour chaque jour de la plage de dates) |
| Taux d'ouvertures directes | Taux | (Nombre total d'ouvertures directes pour chaque jour de la plage de dates) / (Nombre total de distributions pour chaque jour de la plage de dates) |
| Taux d'ouvertures influencées | Taux | (Nombre total d'ouvertures influencées pour chaque jour de la plage de dates) / (Nombre total de distributions pour chaque jour de la plage de dates) |
| Taux d'ouvertures totales | Taux | (Nombre total d'ouvertures totales pour chaque jour de la plage de dates) / (Nombre total de distributions pour chaque jour de la plage de dates)<br><br>Les ouvertures totales incluent à la fois les ouvertures directes et les ouvertures influencées. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Comment les indicateurs sont calculés" }

{% endtab %}
{% endtabs %}

## Filtres du tableau de bord {#dashboard-filters}

Vous pouvez filtrer les données de votre tableau de bord à l'aide des options suivantes :

- **Étiquette :** Choisissez une étiquette. Une fois appliqué, votre tableau de bord affichera les indicateurs uniquement pour l'étiquette sélectionnée.
- **Plateformes :** (Tableau de bord des performances push uniquement) Choisissez une plateforme push, telle que **All Push**, **Android**, **iOS**, **Mobile combined**, **Kindle** ou **Web**. Une fois appliqué, votre tableau de bord affichera les indicateurs uniquement pour la plateforme sélectionnée.
- **Canvas :** Choisissez jusqu'à 10 Canvas. Une fois appliqué, votre tableau de bord affichera les indicateurs uniquement pour les Canvas sélectionnés. Si vous sélectionnez d'abord un filtre par étiquette, les options de filtres Canvas ne proposeront que les Canvas associés à l'étiquette sélectionnée.
- **Campaign :** Choisissez jusqu'à 10 Campaigns. Une fois appliqué, votre tableau de bord affichera les indicateurs uniquement pour les Campaigns sélectionnées. Si vous sélectionnez d'abord un filtre par étiquette, les options de filtres de Campaign ne proposeront que les Campaigns associées à l'étiquette sélectionnée.

![Options de filtre sur le tableau de bord des performances des canaux, où vous pouvez sélectionner une étiquette et une liste de Canvas pour filtrer les résultats.]({% image_buster /assets/img_archive/dashboard_filters.png %})

## Comparaison des périodes {#comparing-time-periods}

Le tableau de bord des performances des canaux compare automatiquement la période sélectionnée dans la plage de dates avec la période précédente de même durée. Par exemple, si vous choisissez « 7 derniers jours » comme plage de dates, la comparaison confrontera les indicateurs des sept derniers jours avec ceux des sept jours précédents. Si vous sélectionnez une plage de dates personnalisée — disons du 10 au 15 mai, soit six jours de données — le tableau de bord comparera les indicateurs de ces jours avec ceux du 4 au 9 mai.

La comparaison correspond au pourcentage de variation entre la période précédente et la période actuelle, calculé en prenant la différence entre les deux périodes et en la divisant par l'indicateur de la période précédente.

### Afficher les variations en totaux et en taux {#viewing-changes-in-total-counts-and-rates}

Vous pouvez basculer entre **Show Change in Totals** — qui compare les totaux (comme le nombre d'e-mails distribués) entre les deux périodes — et **Show Change in Rates** — qui compare les taux (comme le taux de distribution).

![Boutons radio pour basculer entre l'affichage des variations en totaux ou en taux pour le tableau de bord des performances des canaux.]({% image_buster /assets/img_archive/email_performance_dashboard_3.png %}){: style="max-width:60%"}

## Questions fréquentes {#frequently-asked-questions}

### Pourquoi mon tableau de bord affiche-t-il des valeurs vides ? {#why-is-my-dashboard-displaying-empty-values}

Plusieurs scénarios peuvent entraîner des valeurs vides pour un indicateur :

- Braze a enregistré des zéros pour cet indicateur particulier dans la plage de dates sélectionnée.
- Vous n'avez envoyé aucun message pendant la plage de dates sélectionnée.
- Bien qu'il y ait eu des indicateurs tels que des ouvertures, des clics ou des désabonnements pour la plage de dates sélectionnée, il n'y a eu aucune distribution ni aucun envoi. Dans ce cas, Braze ne calculera pas de taux.

Pour voir davantage d'indicateurs, essayez d'élargir la plage de dates.

### Pourquoi mon tableau de bord e-mail affiche-t-il plus d'autres ouvertures que d'ouvertures uniques ? {#why-does-my-email-dashboard-display-more-other-opens-than-unique-opens}

Pour l'indicateur _Ouvertures uniques_, Braze déduplique les ouvertures répétées enregistrées par un même utilisateur (qu'il s'agisse d'_ouvertures automatiques_ ou d'_autres ouvertures_) de sorte qu'une seule _ouverture unique_ est comptabilisée même si un utilisateur ouvre le message plusieurs fois. Pour les _autres ouvertures_, Braze ne procède pas à cette déduplication.

<!---Temporarily hidden until functionality is added

## Empty values in your data

#### If a metric displays "0%" or "0"

This means Braze recorded zero for that particular metric during the time frame you've selected.

#### If a metric displays "N/A"

This means that while Braze recorded positive counts for a particular metric for the time frame you've selected, the denominator for the rate calculation (either sends or deliveries in most cases) was zero. This can occur when emails are sent out on one day and opens and clicks are recorded the following days if your selected time frame does not include the date the messages were sent.

#### If a metric displays "--"

This means Braze hasn't recorded any data for that metric during the time you selected. If you haven't set up or sent any emails yet, learn more about how to do so in our dedicated [Email]({{site.baseurl}}/user_guide/channels/email/) section.

--->