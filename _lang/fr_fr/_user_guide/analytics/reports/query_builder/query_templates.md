---
nav_title: Modèles de requêtes
article_title: Modèles du Générateur de requêtes
page_order: 1
page_type: reference
toc_headers: h2
description: "Cet article de référence répertorie les types de rapports que vous pouvez créer à l'aide des données Braze provenant de Snowflake dans le Générateur de requêtes."
tool: Reports
---

# Modèles du Générateur de requêtes {#query-builder-templates}

> Accédez aux modèles du [Générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder/) en sélectionnant **Query Template** lors de la création d'un rapport. Tous les modèles affichent des données remontant jusqu'aux 60 derniers jours, mais vous pouvez modifier directement cette valeur ainsi que d'autres paramètres dans l'éditeur.<br><br>Pour les définitions des indicateurs susceptibles d'apparaître dans vos rapports du Générateur de requêtes, consultez le [Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/analytics/metrics_glossary/) et filtrez par le canal correspondant.

## Modèles par canal {#channel-templates}

<style>
table th:nth-child(1) {
    width: 30%;
}
table th:nth-child(2) {
    width: 70%;
}
table td {
    word-break: break-word;
}
</style>

| Nom de la requête | Description |
| --- | --- |
| Engagement et chiffre d'affaires par canal | Ce rapport affiche, pour chaque canal, tous les indicateurs d'engagement (tels que les ouvertures et les clics), le chiffre d'affaires, le nombre de transactions et le prix moyen. {::nomarkdown} <ul> <li> <i>Nombre de transactions :</i> Nombre d'événements d'achat </li> <li> <i>Prix moyen :</i> Chiffre d'affaires divisé par les transactions </li> </ul> {:/} ![]({% image_buster /assets/img_archive/channel_engagement_revenue.png %}) |
| Achats et chiffre d'affaires par segment | Ce rapport affiche les indicateurs pour les messages envoyés à un segment spécifique. <br><br> Les indicateurs d'achat sont uniques sur l'ensemble de la période de rapport. Un utilisateur peut générer au maximum un achat. Le chiffre d'affaires prend en compte chaque achat de la période de rapport. |
| Achats et chiffre d'affaires par variantes ou étapes, par segment | Ce rapport affiche les indicateurs pour les variantes ou les étapes Canvas des messages envoyés à chaque segment. <br><br> Les indicateurs d'achat sont uniques sur l'ensemble de la période de rapport. Un utilisateur peut générer au maximum un achat. Le chiffre d'affaires prend en compte chaque achat de la période de rapport. |
| Meilleurs/moins bons messages pour les achats | Ce rapport affiche les indicateurs d'achat pour les meilleures ou les moins bonnes Campaigns, Canvas ou étapes Canvas. Chaque ligne correspond à une Campaign, un Canvas ou une étape Canvas. Vous devez indiquer si vous souhaitez afficher les meilleurs ou les moins bons résultats, ainsi que l'indicateur spécifique sur lequel effectuer cette analyse (par exemple *Achats uniques à la réception*, *Chiffre d'affaires à la réception*, *Destinataires uniques*). <br><br> Les lignes des rapports des meilleurs résultats sont classées du meilleur au moins bon, tandis que les lignes des rapports des moins bons résultats sont classées du moins bon au meilleur. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Channel templates" }

## Modèles Campaign {#campaign-templates}

| Nom de la requête | Description |
| --- | --- |
| Chiffre d'affaires de la Campaign par pays | Ce rapport affiche le chiffre d'affaires par pays pour une Campaign spécifique. Pour exécuter ce rapport, vous devez spécifier l'identifiant API d'une Campaign. Vous trouverez l'identifiant API d'une Campaign en bas de la page de détails de cette Campaign. <br><br> Ce rapport affiche, pour chaque pays, le montant du chiffre d'affaires généré, le nombre de commandes, le nombre de retours, le chiffre d'affaires net et le chiffre d'affaires brut.<br><br> {::nomarkdown} <ul> <li> <i>Commandes :</i> Nombre d'événements d'achat </li> <li><i> Retours :</i> Nombre d'événements d'achat avec des valeurs de chiffre d'affaires négatives </li> <li><i> Chiffre d'affaires net :</i> Chiffre d'affaires de tous les achats hors retours </li> <li><i> Chiffre d'affaires brut :</i> Chiffre d'affaires incluant la valeur des retours </li></ul>{:/} ![]({% image_buster /assets/img_archive/campaign_revenue_country.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaign templates" }

## Modèles Canvas {#canvas-templates}

| Nom de la requête | Description |
| --- | --- |
| Chiffre d'affaires du Canvas par pays | Ce rapport affiche le chiffre d'affaires par pays pour un Canvas spécifique. Pour exécuter ce rapport, vous devez spécifier l'identifiant API d'un Canvas. Vous trouverez l'identifiant API du Canvas sous **Analyze Variants**. <br><br> Ce rapport affiche, pour chaque pays, le montant du chiffre d'affaires généré, le nombre de commandes, le nombre de retours, le chiffre d'affaires net et le chiffre d'affaires brut.<br><br> {::nomarkdown} <ul> <li> <i>Commandes :</i> Nombre d'événements d'achat </li> <li><i> Retours :</i> Nombre d'événements d'achat avec des valeurs de chiffre d'affaires négatives </li> <li><i> Chiffre d'affaires net :</i> Chiffre d'affaires de tous les achats hors retours </li> <li><i> Chiffre d'affaires brut :</i> Chiffre d'affaires incluant la valeur des retours </li></ul>{:/} ![]({% image_buster /assets/img_archive/canvas_revenue_country.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvas templates" }

## Modèles e-mail {#email-templates}

| Nom de la requête | Description |
| --- | --- |
| Rebonds d'e-mails par domaine | Le nombre de rebonds par domaine e-mail, ventilé en rebonds totaux, échecs d'envoi définitifs et échecs provisoires d'envoi. <br> ![]({% image_buster /assets/img_archive/query_builder_q4.png %}){: style="max-width:60%;"} |
| Indicateurs de distribution des e-mails par jour | Ce rapport affiche les indicateurs pour les messages envoyés chaque jour, tels que le nombre d'e-mails envoyés, distribués, ayant subi un échec provisoire d'envoi ou un échec d'envoi définitif. <br><br> Tous les indicateurs sont uniques sur l'ensemble de la période de rapport. Par exemple, si un e-mail de bienvenue a subi un échec provisoire d'envoi une fois le 21 novembre, deux fois le 22 novembre, et n'a jamais été distribué : {::nomarkdown} <ul><li> L'indicateur <i>Échecs provisoires d'envoi</i> du 21 novembre augmente de un.</li><li> L'indicateur <i>Échecs provisoires d'envoi</i> du 22 novembre n'est pas affecté. </li></ul>{:/} ![]({% image_buster /assets/img_archive/email_delivery_day.png %})|
| Indicateurs d'engagement e-mail par segment | Ce rapport affiche les indicateurs pour les messages envoyés à chaque segment, tels que le nombre d'e-mails envoyés, distribués, ayant subi un échec provisoire d'envoi ou un échec d'envoi définitif. <br><br> Tous les indicateurs sont uniques sur l'ensemble de la période de rapport. Par exemple, si un e-mail de bienvenue a subi un échec provisoire d'envoi une fois le 21 novembre, deux fois le 22 novembre, et n'a jamais été distribué : {::nomarkdown} <ul><li> L'indicateur <i>Échecs provisoires d'envoi</i> du 21 novembre augmente de un. </li><li> L'indicateur <i>Échecs provisoires d'envoi</i> du 22 novembre n'est pas affecté.</li></ul>{:/} ![]({% image_buster /assets/img_archive/email_engagement_segment.png %}) |
| Indicateurs d'engagement e-mail par variantes ou étapes, par segment | Ce rapport affiche les indicateurs pour les variantes ou les étapes Canvas des messages envoyés à chaque segment. Ces indicateurs incluent le nombre d'e-mails envoyés, distribués, ayant subi un échec provisoire d'envoi ou un échec d'envoi définitif. <br><br> Tous les indicateurs sont uniques sur l'ensemble de la période de rapport. Par exemple, si un e-mail de bienvenue a subi un échec provisoire d'envoi une fois le 21 novembre, deux fois le 22 novembre, et n'a jamais été distribué : {::nomarkdown} <ul><li> L'indicateur <i>Échecs provisoires d'envoi</i> du 21 novembre augmente de un. </li> <li> L'indicateur <i>Échecs provisoires d'envoi</i> du 22 novembre n'est pas affecté.</li></ul> {:/} |
| Performances des e-mails par pays | Ce rapport affiche les indicateurs suivants pour chaque pays : envois, taux d'ouverture indirect et taux d'ouverture direct. Le pays correspond au pays de l'utilisateur au moment de l'envoi push. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q3.png %}) |
| Journaux de modification d'abonnement e-mail | Ce rapport affiche les indicateurs enregistrés concernant chaque modification d'abonnement d'un utilisateur, tels que son adresse e-mail, son état d'abonnement, l'heure à laquelle son état a été modifié et la Campaign ou le Canvas associé. |
| Abonnements et désabonnements aux groupes d'abonnement e-mail | Ce rapport affiche le nombre d'abonnements et de désabonnements uniques pour chaque groupe d'abonnement e-mail par semaine. Vous devez disposer d'au moins un [groupe d'abonnement e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions/) dans l'espace de travail pour exécuter cette requête. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q2.png %}){: style="max-width:70%;"} |
| URL cliquées dans les e-mails | Ce rapport affiche le nombre de clics pour chaque lien d'un e-mail. Pour exécuter ce rapport, vous devez spécifier l'identifiant API d'une Campaign ou d'un Canvas. Vous trouverez l'identifiant API d'une Campaign en bas de la page de détails de cette Campaign et l'identifiant API du Canvas sous **Analyze Variants**. <br><br> Ce rapport affiche les liens dépersonnalisés et le nombre de clics pour chaque lien. Votre téléchargement CSV inclura les ID utilisateur de tous les utilisateurs ayant cliqué, le lien sur lequel ils ont cliqué et un horodatage du moment où ils ont cliqué. <br><br> *URL dépersonnalisées :* URL dont les étiquettes Liquid ont été retirées. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q5.png %}){: style="max-width:70%;"} |
| Meilleurs/moins bons messages pour l'engagement e-mail | Ce rapport affiche les indicateurs d'engagement e-mail pour les meilleures ou les moins bonnes Campaigns, Canvas ou étapes Canvas. Vous devez indiquer si vous souhaitez afficher les meilleurs ou les moins bons résultats, ainsi que l'indicateur spécifique sur lequel effectuer cette analyse (par exemple *Envoyés*, *Échecs provisoires d'envoi* et *Ouvertures uniques*). <br><br> Les lignes des rapports des meilleurs résultats sont classées du meilleur au moins bon, tandis que les lignes des rapports des moins bons résultats sont classées du moins bon au meilleur. <br><br> ![]({% image_buster /assets/img_archive/top-bottom-email.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email templates" }

## Modèles mobile {#mobile-templates}

| Nom de la requête | Description |
| --- | --- |
| Opérateurs d'appareils | Le nombre d'utilisateurs par opérateur d'appareil, comme Verizon et T-Mobile. <br><br> ![]({% image_buster /assets/img_archive/device_carriers.png %}){: style="max-width:50%;"} |
| Modèles d'appareils | Le nombre d'utilisateurs par modèle d'appareil, comme iPhone 15 Pro et Pixel 7. <br><br> ![]({% image_buster /assets/img_archive/device_models.png %}){: style="max-width:50%;"} |
| Systèmes d'exploitation des appareils | Le nombre d'utilisateurs par système d'exploitation, comme 17.4 et Android 14. <br><br> ![]({% image_buster /assets/img_archive/os_version.png %}){: style="max-width:50%;"} |
| Résolutions d'écran des appareils | Le nombre d'utilisateurs par résolution d'écran d'appareil, comme 1179x2556 et 750x1334. <br><br> ![]({% image_buster /assets/img_archive/device_screen_resolutions.png %}){: style="max-width:40%;"} |
| Codes d'erreur SMS | Ce rapport affiche le type d'erreur et le nombre d'erreurs pour chaque code d'erreur SMS. <br><br>![]({% image_buster /assets/img_archive/sms_errors.png %}){: style="max-width:50%;"} |
| Erreurs du fournisseur SMS par utilisateur | Ce rapport affiche les codes d'erreur SMS pour un utilisateur spécifique. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Mobile templates" }

## Modèles push {#push-templates}

| Nom de la requête | Description |
| --- | --- |
| Performances push par pays | Ce rapport affiche les indicateurs suivants pour chaque pays : distributions, taux d'ouverture et taux de clics. Le pays correspond au pays de l'utilisateur au moment de l'envoi de l'e-mail. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q7.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push templates" }

## Ventilation par segment {#segment-breakdown}

| Nom de la requête | Description |
| -- | -- |
| Indicateurs d'engagement e-mail par segment | Ce rapport affiche les indicateurs de performance des e-mails ventilés par segment au niveau de la Campaign ou du Canvas. |
| Achats et chiffre d'affaires par segment | Ce rapport affiche les indicateurs d'achat et de chiffre d'affaires ventilés par segment pour une Campaign ou un Canvas spécifique. |
| Meilleurs/moins bons messages pour l'engagement e-mail | Ce rapport affiche les Campaigns, Canvas ou étapes Canvas ayant obtenu les meilleurs ou les moins bons résultats pour un indicateur d'engagement e-mail spécifié. |
| Meilleurs/moins bons messages pour les achats | Ce rapport affiche les Campaigns, Canvas ou étapes Canvas ayant obtenu les meilleurs ou les moins bons résultats pour un indicateur d'achat ou de chiffre d'affaires spécifié. |
| Performances push par segment | Ce rapport affiche les indicateurs push ventilés par segment. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Segment breakdown" }