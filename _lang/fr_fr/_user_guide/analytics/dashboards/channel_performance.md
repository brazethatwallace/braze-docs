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

Sélectionnez un onglet pour afficher les détails des tableaux de bord de performance des canaux disponibles.

{% tabs %}
{% tab Performance e-mail %}

### Tableau de bord de performance e-mail {#email-performance-dashboard}

Consultez votre tableau de bord de performance e-mail en accédant à **Analytics** > **Email Performance**, puis en sélectionnant la plage de dates pour la période dont vous souhaitez afficher les données. Votre plage de dates peut remonter jusqu'à un an dans le passé.

{% alert note %}
Pour afficher le tableau de bord **Email Performance**, vous devez disposer de la permission « View Usage Data » ou « View Dashboard Reports ».
{% endalert %}

![Tableau de bord de performance e-mail affichant l'engagement du canal e-mail au cours des trente derniers jours.]({% image_buster /assets/img_archive/email_performance_dashboard_1.png %})

![Un exemple de campagne e-mail avec 335 630 envois, soit une moyenne de 11 187,667 par jour.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### Comment les indicateurs sont calculés {#how-metrics-are-calculated}

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="email" %}

| Indicateur | Type | Calcul |
| --- | --- | ---- |
| Envois | Nombre | Nombre total d'envois pour chaque jour de la plage de dates |
| Taux de distribution | Taux | (Nombre total de distributions pour chaque jour de la plage de dates) / (Nombre total d'envois pour chaque jour de la plage de dates) |
| Taux de rebond | Taux | (Nombre total de rebonds pour chaque jour de la plage de dates) / (Nombre total d'envois pour chaque jour de la plage de dates) |
| Taux de désabonnement | Taux | (Nombre total de désabonnements uniques pour chaque jour de la plage de dates) / (Nombre total de distributions pour la plage de dates)<br><br>Ce calcul utilise les désabonnements uniques, qui sont également utilisés dans Campaign Analytics, l'aperçu et le générateur de rapports. Ces désabonnements sont enregistrés à partir de toutes les sources (telles que la REST API, les importations CSV, les e-mails et les désabonnements par liste). Les taux de désabonnement dans les analyses de Campaign et Canvas correspondent aux désabonnements résultant d'un clic de désabonnement sur un e-mail distribué par Braze. |
| Taux d'ouverture unique | Taux | (Nombre total d'ouvertures uniques pour chaque jour de la plage de dates) / (Nombre total de distributions pour la plage de dates) |
| Taux d'autres ouvertures | Taux | (Nombre total d'autres ouvertures pour chaque jour de la plage de dates) / (Nombre total de distributions pour la plage de dates)<br><br>Les autres ouvertures incluent les e-mails qui n'ont pas été identifiés comme des ouvertures automatiques, par exemple lorsqu'un utilisateur ouvre un e-mail. Cet indicateur n'est pas unique et constitue un sous-indicateur du total des ouvertures. |
| Taux de clics uniques | Taux | (Nombre total de clics uniques pour chaque jour de la plage de dates) / (Nombre total de distributions pour la plage de dates) |
| Taux de clics par ouverture unique | Taux | (Nombre total de clics uniques pour chaque jour de la plage de dates) / (Nombre total d'ouvertures uniques pour chaque jour de la plage de dates) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Comment les indicateurs sont calculés" }

{% endtab %}
{% tab Informations e-mail %}

### Tableau de bord des informations e-mail {#email-insights-dashboard}

Le tableau de bord des informations e-mail suit où et quand vos clients interagissent avec vos e-mails. Ces rapports peuvent fournir des données riches et détaillées sur la manière d'optimiser vos e-mails pour générer un engagement plus élevé. Le tableau de bord des informations e-mail inclut jusqu'à six mois de données. Pour accéder au tableau de bord, rendez-vous dans **Analytics** > **Email Performance** > **Email Insights**.

#### Engagement par appareil {#engagement-by-device}

Le rapport **Engagement by Device** fournit une répartition des appareils que vos utilisateurs emploient pour interagir avec vos e-mails. Ces données suivent l'engagement e-mail sur mobile, ordinateur, tablette et autres types d'appareils. Ces données sont basées sur la chaîne user agent transmise par les appareils de vos utilisateurs.

{% alert note %}
Si vous utilisez CloudFront comme CDN, assurez-vous que le user agent de vos utilisateurs est transmis au fournisseur de services e-mail. Sinon, chaque user agent sera « Amazon Cloudfront ».
{% endalert %}

La catégorie « Other » inclut toute chaîne user agent qui ne peut pas être identifiée comme ordinateur, mobile ou tablette. Par exemple, télévision, voiture, console de jeux vidéo, OTT (over-the-top ou streaming) et similaires. Cela peut également inclure des valeurs nulles ou vides.

Pour mieux comprendre le contenu de cette catégorie « Other », vous pouvez extraire les user agents en utilisant l'une de ces options :

1. [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) vous enverra la chaîne user agent exacte récupérée depuis les appareils de vos utilisateurs.
2. Exploitez notre [générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder) pour utiliser SQL ou notre [générateur de requêtes IA]({{site.baseurl}}/user_guide/analytics/reports/query_builder#generating-sql-with-the-ai-query-builder) pour afficher les user agents.

![Rapport Engagement by Device montrant le nombre de clics pour les appareils mobiles, ordinateurs, tablettes et autres. Le plus grand nombre de clics provient des appareils mobiles.]({% image_buster /assets/img/engagement_by_device_type.png %}){: style="max-width:70%;"}

Pour les ouvertures d'e-mails, Braze distingue Google Image Proxy, Apple Image Proxy et Yahoo Mail Proxy. Ces services mettent en cache et chargent toutes les images intégrées dans un e-mail avant qu'il ne soit distribué au destinataire. Par conséquent, cela déclenche une ouverture d'e-mail depuis les serveurs du fournisseur de messagerie plutôt que depuis le serveur du destinataire, ce qui peut entraîner des ouvertures d'e-mails gonflées. Ces services sont conçus pour améliorer la confidentialité, la sécurité, les performances et l'efficacité lors du chargement des images. Ils peuvent également contenir de véritables ouvertures de la part des destinataires, car ces services proxy masquent le user agent, et Braze catégorise les données proxy en utilisant le user agent.

![Rapport Engagement by Device montrant le nombre de clics pour Mobile, Desktop, Tablet, Apple Privacy Proxy, Google Image Proxy, Yahoo Mail Proxy et Other. Le plus grand nombre d'ouvertures provient des appareils mobiles.]({% image_buster /assets/img/engagement_by_device_type_proxy.png %}){: style="max-width:70%;"}

#### Engagement par fournisseur de messagerie {#engagement-by-mailbox-provider}

Le rapport **Engagement by Mailbox Provider** affiche les principaux fournisseurs de messagerie contribuant à vos clics ou ouvertures. Vous pouvez cliquer sur des fournisseurs de messagerie spécifiques pour accéder aux détails des domaines de réception. Par exemple, si Microsoft figure dans ce rapport parmi vos principaux indicateurs de fournisseur de messagerie, vous pouvez afficher les détails de leurs domaines de réception, tels que « outlook.com », « hotmail.com », « live.com », et plus encore.

![Un exemple de rapport Engagement by Mailbox Provider avec Google, Apple iCloud, Yahoo, Microsoft et Mail.Ru Group et leur nombre de clics correspondant.]({% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}){: style="max-width:70%;"}

#### Moment de l'engagement {#time-of-engagement}

Le rapport **Time of Engagement** affiche des données sur le moment où les utilisateurs interagissent avec vos e-mails. Cela peut aider à répondre à des questions telles que quel jour de la semaine ou quelle heure génère le plus d'engagement de la part de vos clients. Grâce à ces informations, vous pouvez expérimenter le meilleur jour ou la meilleure heure pour envoyer vos messages afin de générer un engagement plus élevé. Notez que ces horaires sont basés sur le fuseau horaire de votre entreprise.

Le rapport d'engagement **Day of the week** répartit les ouvertures ou les clics par jour de la semaine.

![Un exemple de rapport d'engagement Day of the week avec le plus de clics le lundi et le mercredi.]({% image_buster /assets/img_archive/time_engagement.png %})

Le rapport d'engagement **Time of the day** répartit les ouvertures ou les clics par heure sur une fenêtre de 24 heures.

![Un exemple de rapport d'engagement Time of the day avec les ouvertures ou clics de minuit à 23 h.]({% image_buster /assets/img_archive/time_engagement_day.png %})

Pour plus d'informations sur l'analyse de vos e-mails, consultez [Rapports e-mail]({{site.baseurl}}/user_guide/channels/email/reporting).

{% endtab %}
{% tab Performance SMS %}

### Tableau de bord de performance SMS {#sms-performance-dashboard}

Pour utiliser votre tableau de bord de performance SMS, accédez à **Analytics** > **SMS Performance**, puis sélectionnez la plage de dates pour la période dont vous souhaitez afficher les données. Votre plage de dates peut remonter jusqu'à un an dans le passé.

![Un exemple de campagne SMS avec 335 630 envois, soit une moyenne de 11 187,667 par jour.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### Comment les indicateurs sont calculés

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="SMS" %}

| Indicateur | Type | Calcul |
| --- | --- | ---- |
| Envois | Nombre | Nombre total d'envois pour chaque jour de la plage de dates |
| Taux de distributions confirmées | Taux | (Nombre total de distributions pour chaque jour de la plage de dates) / (Nombre total d'envois pour chaque jour de la plage de dates) |
| Taux d'échecs de distribution | Taux | (Nombre total d'échecs pour chaque jour de la plage de dates) / (Nombre total d'envois pour chaque jour de la plage de dates) |
| Taux de rejets | Taux | (Nombre total de rejets pour chaque jour de la plage de dates) / (Nombre total d'envois pour chaque jour de la plage de dates) |
| Taux de clics | Taux | (Nombre total de clics pour chaque jour de la plage de dates) / (Nombre total de distributions pour chaque jour de la plage de dates) |
| Total des abonnements | Taux | Nombre total d'abonnements par messages entrants pour chaque jour de la plage de dates |
| Total des désabonnements | Taux | Nombre total de désabonnements par messages entrants pour chaque jour de la plage de dates |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Comment les indicateurs sont calculés" }

{% endtab %}
{% tab Performance push %}

### Tableau de bord de performance push {#push-performance-dashboard}

Le tableau de bord **Push Performance** vous offre une vue unique au niveau du canal de l'engagement push, incluant les envois, les rebonds, les distributions et les taux d'ouverture directe, influencée et totale sur une fenêtre temporelle configurable. Utilisez-le pour comprendre la santé globale de votre canal de notifications push sans avoir à agréger les données de Campaigns ou Canvas individuels.

Pour ouvrir le tableau de bord, accédez à **Analytics** > **Dashboard Builder**, puis sélectionnez **Push Channel Dashboard**. Votre plage de dates peut remonter jusqu'à un an dans le passé.

![Un exemple de campagne push avec plus de 63 millions d'envois.]({% image_buster /assets/img_archive/push_performance_dashboard.png %})

#### Comment les indicateurs sont calculés

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="push" %}

| Indicateur | Type | Calcul |
| --- | --- | ---- |
| Envois | Nombre | Nombre total d'envois pour chaque jour de la plage de dates |
| Taux de rebond | Taux | (Nombre total de rebonds pour chaque jour de la plage de dates) / (Nombre total d'envois pour chaque jour de la plage de dates) |
| Taux de distribution | Taux | (Nombre total de distributions pour chaque jour de la plage de dates) / (Nombre total d'envois pour chaque jour de la plage de dates) |
| Taux d'ouverture directe | Taux | (Nombre total d'ouvertures directes pour chaque jour de la plage de dates) / (Nombre total de distributions pour chaque jour de la plage de dates) |
| Taux d'ouverture influencée | Taux | (Nombre total d'ouvertures influencées pour chaque jour de la plage de dates) / (Nombre total de distributions pour chaque jour de la plage de dates) |
| Taux d'ouverture total | Taux | (Nombre total d'ouvertures pour chaque jour de la plage de dates) / (Nombre total de distributions pour chaque jour de la plage de dates)<br><br>Le total des ouvertures inclut à la fois les ouvertures directes et les ouvertures influencées. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Comment les indicateurs sont calculés" }

{% endtab %}
{% endtabs %}

## Filtres du tableau de bord {#dashboard-filters}

Vous pouvez filtrer les données de votre tableau de bord à l'aide des options de filtre suivantes :

- **Étiquette :** Choisissez une étiquette. Une fois appliquée, votre tableau de bord affichera les indicateurs uniquement pour l'étiquette sélectionnée.
- **Plateformes :** (Tableau de bord des performances push uniquement) Choisissez une plateforme de notification push, telle que **All Push**, **Android**, **iOS**, **Mobile combined**, **Kindle** ou **Web**. Une fois appliquée, votre tableau de bord affichera les indicateurs uniquement pour la plateforme sélectionnée.
- **Canvas :** Choisissez jusqu'à 10 Canvas. Une fois appliqué, votre tableau de bord affichera les indicateurs uniquement pour les Canvas sélectionnés. Si vous sélectionnez d'abord un filtre par étiquette, les options de filtres Canvas n'incluront que les Canvas associés à l'étiquette sélectionnée.
- **Campaign :** Choisissez jusqu'à 10 Campaigns. Une fois appliqué, votre tableau de bord affichera les indicateurs uniquement pour les Campaigns sélectionnées. Si vous sélectionnez d'abord un filtre par étiquette, les options de filtres Campaign n'incluront que les Campaigns associées à l'étiquette sélectionnée.

![Options de filtre sur le tableau de bord des performances par canal, où vous pouvez sélectionner une étiquette et une liste de Canvas pour filtrer les résultats.]({% image_buster /assets/img_archive/dashboard_filters.png %})

## Comparaison des périodes {#comparing-time-periods}

Le tableau de bord de performance des canaux compare automatiquement la période que vous avez sélectionnée dans la plage de dates avec la période précédente, en totalisant le même nombre de jours. Par exemple, si vous choisissez « 7 derniers jours » comme plage de dates dans le tableau de bord, la comparaison avec la période précédente comparera les indicateurs des sept derniers jours avec ceux des sept jours précédents. Si vous sélectionnez une plage de dates personnalisée — disons du 10 au 15 mai, soit six jours de données — le tableau de bord comparera les indicateurs de ces jours avec ceux du 4 au 9 mai.

La comparaison correspond au pourcentage de variation entre la période précédente et la période actuelle, calculé en prenant la différence entre les deux périodes et en la divisant par l'indicateur de la période précédente.

### Afficher les variations des totaux et des taux {#viewing-changes-in-total-counts-and-rates}

Vous pouvez basculer entre **Show Change in Totals** — qui compare les totaux (comme le nombre d'e-mails distribués) entre les deux périodes — et **Show Change in Rates** — qui compare les taux (comme le taux de distribution).

![Boutons radio permettant de basculer entre l'affichage des variations des totaux ou des taux pour le tableau de bord de performance des canaux.]({% image_buster /assets/img_archive/email_performance_dashboard_3.png %}){: style="max-width:60%"}

## Questions fréquentes {#frequently-asked-questions}

### Pourquoi mon tableau de bord affiche-t-il des valeurs vides ? {#why-is-my-dashboard-displaying-empty-values}

Plusieurs scénarios peuvent entraîner des valeurs vides pour un indicateur :

- Braze a enregistré des zéros pour cet indicateur particulier dans la plage de dates sélectionnée.
- Vous n'avez envoyé aucun message pendant la plage de dates sélectionnée.
- Bien qu'il y ait eu des indicateurs tels que des ouvertures, des clics ou des désabonnements pour une plage de dates sélectionnée, il n'y a eu aucune distribution ni aucun envoi. Dans ce cas, Braze ne calculera pas d'indicateur de taux.

Pour voir plus d'indicateurs, essayez d'élargir la plage de dates.

### Pourquoi mon tableau de bord d'e-mail affiche-t-il plus d'Autres ouvertures que d'Ouvertures uniques ? {#why-does-my-email-dashboard-display-more-other-opens-than-unique-opens}

Pour l'indicateur _Ouvertures uniques_, Braze déduplique toutes les ouvertures répétées enregistrées par un utilisateur donné (qu'elles incluent des _Ouvertures automatiques_ ou des _Autres ouvertures_) de sorte qu'une seule _Ouverture unique_ est comptabilisée si un utilisateur ouvre plusieurs fois. Pour les _Autres ouvertures_, Braze ne procède pas à la déduplication.

<!---Temporarily hidden until functionality is added

## Valeurs vides dans vos données {#empty-values-in-your-data}

### Si un indicateur affiche « 0 % » ou « 0 » {#if-a-metric-displays-0-or-0}

Cela signifie que Braze a enregistré zéro pour cet indicateur particulier pendant la période que vous avez sélectionnée.

#### Si un indicateur affiche « N/A » {#if-a-metric-displays-na}

Cela signifie que, bien que Braze ait enregistré des valeurs positives pour un indicateur particulier pendant la période que vous avez sélectionnée, le dénominateur pour le calcul du taux (soit les envois, soit les réceptions dans la plupart des cas) était égal à zéro. Cela peut se produire lorsque des e-mails sont envoyés un jour donné et que les ouvertures et les clics sont enregistrés les jours suivants, si la période sélectionnée n'inclut pas la date d'envoi des messages.

#### Si un indicateur affiche « -- » {#if-a-metric-displays}

Cela signifie que Braze n'a enregistré aucune donnée pour cet indicateur pendant la période que vous avez sélectionnée. Si vous n'avez pas encore configuré ou envoyé d'e-mails, consultez notre section dédiée [E-mail]({{site.baseurl}}/user_guide/channels/email) pour en savoir plus.

--->