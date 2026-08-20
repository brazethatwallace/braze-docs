---
nav_title: Rapports d'engagement
article_title: Rapports d'engagement
page_order: 5
local_redirect:
  report-glossary: '/docs/user_guide/analytics/metrics_glossary'
page_type: tutorial
description: "Cet article pratique vous guide dans la création, la personnalisation et la planification de rapports d'engagement pour les Campaigns et les Canvas."
tool:
  - Campaigns
  - Canvas
  - Reports
---

# Rapports d'engagement {#engagement-reports}

> Les rapports d'engagement vous permettent d'extraire des statistiques d'engagement pour des messages spécifiques provenant de Campaigns et de Canvas, et de les recevoir par e-mail à l'heure de votre choix.

{% alert note %}
Vous devez disposer de l'autorisation « Export User Data » pour exécuter des rapports d'engagement.
{% endalert %}

Avec les rapports d'engagement, vous pouvez sélectionner manuellement les Campaigns et les Canvas à inclure dans votre rapport par e-mail, ou définir des règles pour sélectionner automatiquement les Campaigns et Canvas pertinents.

Quel que soit le nombre de Campaigns ou de Canvas sélectionnés, jusqu'à deux fichiers CSV sont générés : un pour toutes les données de Campaign et un pour toutes les données de Canvas. Vous pouvez accéder à ces fichiers CSV via le lien intégré dans l'e-mail de votre rapport. Les rapports d'engagement ne sont pas enregistrés dans le tableau de bord de Braze.

Certaines données sont agrégées au niveau de la Campaign ou du Canvas plutôt qu'au niveau de la variante de campagne individuelle ou de l'étape du Canvas. Si vous [supprimez une étape du Canvas après le lancement]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch#canvas-details), cela supprimera également les données des rapports d'engagement.

{% alert tip %}
Vous pouvez relancer le rapport pour générer des statistiques mises à jour.
{% endalert %}

## Créer un nouveau rapport {#creating-a-new-report}

### Étape 1 : Créer un rapport {#step-1-create-a-report}

Dans votre compte du tableau de bord, accédez à **Analytics** > **Rapports d'engagement**. Sélectionnez **+ Créer un rapport**.

### Étape 2 : Ajouter des messages {#step-2-add-messages}

Ajoutez les Campaigns et les messages Canvas que vous souhaitez compiler dans votre rapport. Vous pouvez sélectionner vos messages de deux manières :

- Sélectionner manuellement les Campaigns et les Canvas
- Sélectionner automatiquement les Campaigns et les Canvas en fonction de règles spécifiques

![Sélection des messages pour le rapport d'engagement]({% image_buster /assets/img_archive/engagement_report_add_messages.png %})

#### Sélectionner manuellement les Campaigns ou les Canvas {#manually-select-campaigns-or-canvases}

Cette option vous donne la liberté de choisir les Campaigns ou les Canvas que vous souhaitez inclure dans ce rapport.

#### Sélectionner automatiquement les Campaigns ou les Canvas {#automatically-select-campaigns-or-canvases}

Cette option vous permet d'inclure automatiquement tous les messages qui contiennent une [étiquette]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) spécifique. Vous pouvez cibler les messages qui possèdent une ou toutes les étiquettes répertoriées. Cette option est utile si vous configurez des rapports récurrents et que vous étiquetez régulièrement vos messages d'engagement.

{% alert important %}
Les étiquettes doivent correspondre à au moins une Campaign ou un Canvas pour qu'un rapport soit généré. Si vous utilisez **Sélectionner automatiquement les Campaigns et les Canvas en fonction de règles spécifiques** et que vous voyez une erreur, confirmez qu'au moins une Campaign ou un Canvas correspond à vos étiquettes et autres filtres (par exemple, lorsque vous exigez toutes les étiquettes répertoriées, chaque message correspondant doit posséder chaque étiquette).
{% endalert %}

### Étape 3 : Ajouter des statistiques {#add-statistics-to-your-reports}

L'étape **Ajouter des statistiques** vous présente les statistiques correspondant aux types de Campaigns ou de Canvas que vous avez sélectionnés. Par exemple, si vous avez sélectionné des e-mails, vous ne pouvez consulter que les statistiques pertinentes pour les e-mails. Si vous avez choisi une combinaison d'e-mails et de notifications push, vous pouvez consulter les statistiques de ces deux canaux.

![Ajout de statistiques au rapport d'engagement]({% image_buster /assets/img_archive/engagement_report_add_stats.png %})

Les rapports d'engagement agrègent les données par Campaign ou Canvas, et non au niveau de l'espace de travail. Pour surveiller le volume total d'envois ou d'impressions sur l'ensemble des Campaigns et Canvas actifs, comme les envois et impressions par canal sur un espace de travail entier, utilisez le [générateur de rapports]({{site.baseurl}}/report_builder).

{% alert note %}
*Envois au transporteur* est obsolète, mais continuera d'être pris en charge pour les utilisateurs qui l'utilisent déjà.
{% endalert %}

| Canal | Statistiques disponibles |
| ------| --------------|
| E-mail | Envois, Ouvertures, Ouvertures uniques, Clics, Clics uniques, Taux de clics par ouverture, Désabonnements, Rebonds, Réceptions, Signalements comme spam |
| Push  | Envois, Ouvertures, Ouvertures influencées, Rebonds, Clics sur le corps |
| Notification push Web | Envois, Ouvertures, Rebonds, Clics sur le corps |
| Message in-app | Impressions, Clics, Clics sur le premier bouton, Clics sur le deuxième bouton |
| Webhook  |  Envois, Erreurs |
| SMS | Envois, Envois au transporteur, Réceptions confirmées, Échecs de réception, Rejets |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 3 : Ajouter des statistiques" }

### Étape 4 : Finaliser la configuration du rapport {#step-4-complete-report-setup}

Donnez un nom à votre rapport, choisissez le format de votre rapport et sélectionnez vos destinataires. Par défaut, les rapports d'engagement sont envoyés sous forme de fichier ZIP où les données sont délimitées par des virgules (chaque élément de données est séparé par une virgule).

Vous pouvez choisir parmi les options de compression et de délimiteur suivantes :

- **Compression :** ZIP, Non compressé ou gzip
- **Délimiteur :** Virgule (`,`), Deux-points (`:`), Point-virgule (`;`) ou Barre verticale (`|`)

{% alert note %}
Les statistiques ne sont collectées que pour la plage de dates spécifiée par le rapport. Pour obtenir des statistiques précises sur les taux d'ouverture et de clics, sélectionnez une plage de dates qui inclut le moment où les événements d'envoi ont été effectués pour vos Campaigns et Canvas.
{% endalert %}

#### Sélectionner la période {#select-time-frame}

Par défaut, la plage de données affichée est basée sur le fuseau horaire de votre entreprise et s'étend du message le plus ancien sélectionné jusqu'à la date actuelle. Vous pouvez personnaliser cela en sélectionnant le menu déroulant des dates et en utilisant la sélection de plage personnalisée OU en sélectionnant le bouton radio suivant et en définissant votre plage de dates avec les options déroulantes disponibles.

#### Sélectionner l'affichage des données {#select-data-display}

Par défaut, les données affichées dans les rapports d'engagement sont quotidiennes (un jour). Pour visualiser ces données sur différents intervalles, choisissez un nombre explicite de jours ou de semaines pour agréger les données du rapport. Ainsi, au lieu de voir des indicateurs quotidiens, vous pouvez visualiser votre engagement par semaine, mois, trimestre ou similaire. Si une agrégation temporelle ne suffit pas, vous pouvez également choisir d'exporter les données au niveau de la Campaign ou du Canvas.

![Couverture des données du rapport d'engagement]({% image_buster /assets/img_archive/engagement_report_datacoverage.png %})

##### Afficher les données par Campaign ou Canvas entier {#show-data-by-entire-campaign-or-canvas}

Lorsque vous sélectionnez **Afficher les données par Campaign ou Canvas entier**, Braze agrège les indicateurs par blocs de 1 825 jours (cinq ans) sur la plage temporelle du rapport.

Si la plage temporelle s'étend sur plus d'un bloc, vous pouvez voir plusieurs lignes pour la même Campaign ou le même Canvas avec des dates différentes dans la colonne de date. Certaines lignes peuvent inclure uniquement des indicateurs enregistrés plus tard dans la plage (par exemple, les désabonnements). Les dates peuvent également remonter à des années avant que vous n'ayez commencé à envoyer dans l'espace de travail, car elles reflètent les limites des blocs dans l'export, et pas uniquement votre premier envoi.

Pour aligner la colonne de date avec le moment où vos Campaigns et Canvas sélectionnés ont réellement été envoyés, définissez la [date de début du rapport dans **Sélectionner la période**](#select-time-frame) à la date la plus ancienne que vous souhaitez dans le fichier — généralement le moment où ces messages ont commencé à être envoyés — plutôt que de laisser la plage par défaut qui remonte au message sélectionné le plus ancien.

Dans le fichier CSV exporté, la première colonne est la date :

- **Afficher les données par Campaign ou Canvas entier :** la date correspond au début de la plage de dates du rapport ou à une limite de bloc au sein de celle-ci, et non à la date de début de la Campaign ou du Canvas.
- **Afficher les données par X jours ou semaines :** la date de chaque ligne reflète le moment où les événements de cette fenêtre d'agrégation se sont produits.

#### Planifier votre rapport {#schedule-your-report}

Il existe deux options pour planifier votre rapport :

- **Envoyer immédiatement :** une fois le rapport lancé, Braze enverra ce rapport immédiatement.
- **Envoyer à un moment désigné :** cette option vous offre la flexibilité de choisir la fréquence à laquelle vous recevez ce rapport. Vous pouvez choisir d'envoyer ce rapport tous les X jours, semaines ou mois. Vous pouvez également définir quand arrêter l'envoi du rapport.

![Planification du rapport d'engagement]({% image_buster /assets/img_archive/engagement_report_reportschedule.png %}){: style="max-width:65%;" }

### Étape 5 : Vérifier et lancer {#step-5-review-and-launch}

La dernière étape de la configuration de votre rapport affiche un aperçu en lecture seule de vos options configurées. Vérifiez votre rapport et, lorsque vous êtes satisfait, sélectionnez **Lancer le rapport**.

### Étape 6 : Vérifier votre e-mail {#step-6-check-your-email}

Vous recevrez un e-mail contenant des liens vers vos rapports à l'heure ou selon la planification choisie. **Ces liens expirent 1 heure après l'envoi du rapport.** Lorsque vous sélectionnez les liens fournis, vous téléchargerez automatiquement un fichier ZIP contenant vos fichiers CSV — un pour toutes les Campaigns.

Le rapport contient toutes les statistiques sélectionnées dans la section [Ajouter des statistiques](#add-statistics-to-your-reports) du processus de configuration.

## Résolution des problèmes {#troubleshooting}

### Les indicateurs du rapport d'engagement diffèrent du tableau de bord de performance des e-mails {#engagement-report-metrics-differ-from-the-email-performance-dashboard}

Les rapports d'engagement et le [tableau de bord de performance des e-mails]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance) utilisent les mêmes définitions d'indicateurs e-mail. Les deux attribuent les ouvertures et les clics au jour où chaque événement **s'est produit**, et les deux calculent les *ouvertures uniques* et les *clics uniques* comme des comptages uniques sur sept jours par jour, additionnés sur la plage de dates sélectionnée. Pour les définitions, consultez [Indicateurs e-mail]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary) et [Comment les indicateurs sont calculés]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#how-metrics-are-calculated) sur la page des tableaux de bord de performance des canaux.

Si les totaux diffèrent toujours pour les mêmes Campaigns et la même période, vérifiez les points suivants :

| Vérification | Pourquoi c'est important |
| --- | --- |
| Plage de dates et fuseau horaire | Les deux surfaces doivent couvrir les mêmes jours calendaires dans le même fuseau horaire. |
| Sélection de Campaign ou Canvas | Le tableau de bord de performance des e-mails agrège l'activité e-mail à l'échelle de l'espace de travail. Un rapport d'engagement inclut uniquement les Campaigns ou Canvas que vous avez sélectionnés. |
| Lignes quotidiennes versus totaux du rapport | Si **Data Display** divise l'export en lignes quotidiennes, additionnez ces lignes pour les comparer aux totaux du tableau de bord pour la même plage. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vérifications lorsque les indicateurs e-mail du rapport d'engagement diffèrent du tableau de bord de performance des e-mails" }

Les différences sont plus fréquentes lorsque les chiffres du rapport d'engagement sont comparés aux analyses de **Campaign** ou de **Canvas** plutôt qu'au tableau de bord de performance des e-mails. Les pages Campaign et Canvas peuvent afficher des indicateurs basés sur la date d'envoi (par exemple, les envois ou les conversions attribués à la date d'envoi) aux côtés des ouvertures et des clics basés sur la date de l'événement. Consultez [Le rapport d'engagement ne correspond pas aux indicateurs du Canvas ou de la Campaign](#engagement-report-doesnt-match-metrics-from-the-canvas-or-campaign).

### Le rapport d'engagement ne correspond pas aux indicateurs du Canvas ou de la Campaign {#engagement-report-doesnt-match-metrics-from-the-canvas-or-campaign}

#### Plage de dates incohérente {#mismatched-time-range}

Assurez-vous que les dates du rapport d'engagement correspondent aux dates des analyses du Canvas ou de la Campaign (par exemple, les deux couvrent du 1er au 15 décembre), même si le Canvas n'a envoyé qu'une seule fois. Dans les paramètres du rapport d'engagement, vérifiez **Data Display** pour confirmer que vous consultez le bon Canvas ou la bonne Campaign. Si **Data Display** est configuré pour afficher les données tous les *X* jours, vous obtenez une ligne par date à laquelle des indicateurs ont été enregistrés pour chaque étape.

Si les totaux semblent incorrects dans un tableur, supprimez les filtres supplémentaires sur l'export. Vous pouvez additionner les lignes quotidiennes pour les réconcilier avec les totaux du Canvas ou de la Campaign pour la même plage de dates.

{% alert note %}
Si vous souhaitez que les lignes soient agrégées par Campaign ou Canvas entier plutôt que par compartiments quotidiens, hebdomadaires ou récurrents, définissez **Data Display** sur **Show Data by Entire Campaign or Canvas**. Si le nombre de lignes ou les dates semblent incorrects dans le CSV, consultez [Show Data by Entire Campaign or Canvas](#show-data-by-entire-campaign-or-canvas).
{% endalert %}

#### Clics de bouton en double dans les messages in-app HTML {#duplicate-button-clicks-in-html-in-app-messages}

Si vous utilisez des messages in-app HTML et que les **clics sur le corps** semblent élevés dans le rapport d'engagement, il est possible que vous déclenchiez la journalisation des clics deux fois — par exemple en appelant `brazeBridge.logClick()` pour un clic générique sur le corps et aussi `brazeBridge.logClick('body click')` (ou un autre ID) sur la même interaction. Recherchez `brazeBridge.logClick(` dans votre code et harmonisez avec un seul modèle par contrôle. Pour l'utilisation recommandée, consultez [Suivi des boutons]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#button-tracking-improvements).

#### Liens cassés dans les rapports d'engagement envoyés par e-mail {#broken-links-in-emailed-engagement-reports}

Si les liens d'un rapport d'engagement planifié envoyé par e-mail ne s'ouvrent pas correctement dans votre client de messagerie, essayez les étapes suivantes :

1. Transférez le rapport vers une boîte de réception Gmail et ouvrez les liens dans Google Chrome.
2. Dans les paramètres du rapport d'engagement, confirmez que **Report Schedule** est configuré pour envoyer au moment prévu (par exemple, immédiatement après la génération du rapport plutôt que selon un calendrier différé).