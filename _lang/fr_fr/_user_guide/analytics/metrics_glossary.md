---
nav_title: Glossaire des indicateurs
article_title: Glossaire des indicateurs
layout: report_metrics
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Ce glossaire définit les termes que vous trouverez dans vos rapports au sein de votre compte Braze."
tool: Reports
---

<style>
  .calculation-line {
    color: #5B6B75;
    font-size: 14px;
  }
</style>

{% api %}

## Clics AMP {#amp-clicks}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Clicks' %}

{% endapi %}

{% api %}

## Ouvertures AMP {#amp-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Opens' %}

{% endapi %}

{% api %}

## Audience {#audience}

{% apitags %}
All
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Calcul : (Nombre de destinataires dans la variante) / (Destinataires uniques)</span>

{% endapi %}

{% api %}

## Rebonds {#bounces}

{% apitags %}
Email, Web Push, iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} Cela peut se produire parce qu'il n'y a pas de jeton de notification push valide, que l'utilisateur s'est désabonné après le lancement de la campagne, ou que l'adresse e-mail est incorrecte ou désactivée.

| Canal | Informations complémentaires |
|-------|-----------------------|
| E-mail | Un rebond d'e-mail pour les clients utilisant SendGrid comprend les échecs d'envoi définitifs, le spam (`spam_report_drops`) et les e-mails envoyés à des adresses invalides (`invalid_emails`).<br><br>Pour les e-mails, le *% de rebonds* ou le *taux de rebond* est le pourcentage de messages qui n'ont pas été envoyés avec succès ou qui ont été désignés comme « retournés » ou « non reçus » par les services d'envoi utilisés, ou qui n'ont pas été reçus par les utilisateurs joignables par e-mail visés. |
| Push | Ces utilisateurs ont été automatiquement désabonnés de toutes les futures notifications push. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rebonds" }

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Rebonds</i> : Nombre</li>
        <li><i>% de rebonds</i> ou <i>Taux de rebond %</i> : (Rebonds) / (Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Clic sur le corps {#body-click}

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Click' %}

<span class="calculation-line">Calcul : (Clics sur le corps) / (Impressions)</span>

{% endapi %}

{% api %}

## Clics sur le corps {#body-clicks}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Clicks' %}

<span class="calculation-line">Calcul : (Clics sur le corps) / (Impressions)</span>

{% endapi %}

{% api %}

## Clics sur le bouton 1 {#button-1-clicks}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %} Le suivi des _clics sur le bouton 1_ ne fonctionne que si vous spécifiez l'**Identifier for Reporting** comme « 0 » dans le message in-app.

<span class="calculation-line">Calcul : (Clics sur le bouton 1) / (Impressions)</span>

{% endapi %}

{% api %}

## Clics sur le bouton 2 {#button-2-clicks}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %} Le suivi des _clics sur le bouton 2_ ne fonctionne que si vous spécifiez l'**Identifier for Reporting** comme « 1 » dans le message in-app.

<span class="calculation-line">Calcul : (Clics sur le bouton 2) / (Impressions)</span>

{% endapi %}

{% api %}

## Analyses de Campaign {#campaign-analytics}

{% apitags %}
Feature Flags
{% endapitags %}

La performance du message à travers les différents canaux. Les indicateurs affichés dépendent du canal de communication sélectionné et du fait que l'[expérience d'indicateur de fonctionnalité]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments#campaign-analytics) est un test multivarié ou non.

{% endapi %}

{% api %}

## Choix soumis {#choices-submitted}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Choices Submitted' %}

{% endapi %}

{% api %}

## Taux de clic par ouverture {#click-to-open-rate}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Calcul : (Clics uniques) / (Ouvertures uniques) (pour les e-mails)</span>

{% endapi %}

{% api %}

## Livraisons confirmées RCS ou livraisons confirmées SMS {#rcs-confirmed-deliveries-or-sms-confirmed-deliveries}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %} En tant que client Braze, les livraisons sont déduites de votre allocation SMS.

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Livraisons confirmées</i> : Nombre</li>
        <li><i>Taux de livraison confirmée</i> : (Livraisons confirmées) / (Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Confiance {#confidence}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

## Bouton de la page de confirmation {#confirmation-page-button}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Button' %}

{% endapi %}

{% api %}

## Fermetures de la page de confirmation {#confirmation-page-dismissals}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Dismissals' %}

{% endapi %}

{% api %}

## Conversions (B, C, D) {#conversions-b-c-d}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %} Cet événement défini est déterminé par vous lors de la création de la campagne.

| Canal | Informations complémentaires |
|-------|-----------------------|
| E-mail, push, webhooks | Les conversions sont suivies après l'envoi initial. |
| Content Cards | Les conversions sont comptabilisées lorsque l'utilisateur consulte une Content Card pour la première fois. |
| Messages in-app | Une conversion est comptabilisée si l'utilisateur a reçu et consulté la campagne de message in-app, puis effectue l'événement de conversion spécifique dans la fenêtre de conversion définie, qu'il ait cliqué ou non sur le message.<br><br>Les conversions sont attribuées au dernier message reçu. Si la rééligibilité est activée, la conversion sera attribuée au dernier message in-app reçu, à condition qu'elle se produise dans la fenêtre de conversion définie. Cependant, si le message in-app a déjà été associé à une conversion, la nouvelle conversion ne pourra pas être enregistrée pour ce message spécifique. Cela signifie que chaque livraison de message in-app est associée à une seule conversion. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conversions (B, C, D)" }

{% endapi %}

{% api %}

## Conversions totales {#total-conversions}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}

Lorsqu'un utilisateur consulte une campagne de message in-app une seule fois, une seule conversion est comptabilisée, même s'il effectue l'événement de conversion plusieurs fois par la suite. Cependant, si la rééligibilité est activée et que l'utilisateur voit la campagne de message in-app plusieurs fois, les *conversions totales* peuvent augmenter d'une unité à chaque fois que l'utilisateur enregistre une impression pour une nouvelle instance de la campagne de message in-app.

Par exemple, si un utilisateur déclenche un message in-app deux fois et convertit après chaque impression du message in-app (ce qui donne deux conversions), les *conversions totales* augmenteront de deux. Cependant, s'il n'y a eu qu'une seule impression de message in-app suivie de deux événements de conversion, une seule conversion sera enregistrée et les *conversions totales* augmenteront d'une unité.

{% endapi %}

{% api %}

## Fermeture du message {#close-message}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Close Message' %}

{% endapi %}

{% api %}

## Taux de conversion {#conversion-rate}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

| Canal | Informations complémentaires |
|-------|-----------------------|
| Messages in-app | L'indicateur des <i>impressions uniques</i> quotidiennes totales est utilisé pour calculer le <i>taux de conversion</i> des messages in-app.<br><br>Les <i>impressions uniques</i> pour les messages in-app ne peuvent être comptabilisées qu'une seule fois par jour calendaire dans le fuseau horaire de votre espace de travail. Le nombre de fois qu'un utilisateur effectue une action souhaitée (une « conversion ») peut augmenter au cours de ce même jour calendaire. Bien que les conversions puissent se produire plus d'une fois par jour, les <i>impressions uniques</i> ne le peuvent pas. Par conséquent, si un utilisateur effectue une conversion plusieurs fois dans une journée, le <i>taux de conversion</i> peut augmenter en conséquence, mais les <i>impressions uniques</i> ne sont comptabilisées qu'une seule fois pour ce jour calendaire. Pour plus de détails, consultez <a href="/docs/user_guide/channels/in_app_messages/reporting">Reporting des messages in-app</a>. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Taux de conversion" }

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b>Messages in-app</b> : (Conversions principales) / (Impressions uniques)</li>
        <li><b>Autres canaux</b> : (Conversions principales) / (Destinataires uniques)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Fenêtre de conversion {#conversion-window}

{% apitags %}
All
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Window' %}

{% endapi %}

{% api %}

## Livraisons {#deliveries}

{% apitags %}
Email, Web Push, iOS Push, Android Push, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %}

| Canal | Informations complémentaires |
|-------|-----------------------|
| E-mail | Désigne le nombre total de messages (envois) envoyés avec succès et reçus par les parties joignables par e-mail. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Livraisons" }

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Livraisons</i> : Nombre</li>
        <li><i>% de livraisons</i> : (Envois - Rebonds) / (Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Échecs de livraison RCS ou échecs de livraison SMS {#rcs-delivery-failures-or-sms-delivery-failures}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}

Contactez l'<a href="/docs/braze_support">assistance Braze</a> pour obtenir de l'aide afin de comprendre les raisons des échecs de livraison.

<span class="calculation-line">Calcul : (Envois) - (Envois à l'opérateur)</span>

{% endapi %}

{% api %}

## Échecs de livraison {#delivery-failures}

{% apitags %}
RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures RCS' %}

Contactez l'<a href="/docs/braze_support">assistance Braze</a> pour obtenir de l'aide afin de comprendre les raisons des échecs de livraison.

<span class="calculation-line">Calcul : (Envois) - (Envois à l'opérateur)</span>

{% endapi %}

{% api %}

## Taux d'échec de livraison {#failed-delivery-rate}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failed Delivery Rate' %}

Contactez l'<a href="/docs/braze_support">assistance Braze</a> pour obtenir de l'aide afin de comprendre les raisons des échecs de livraison.

<span class="calculation-line">Calcul : (Échecs de livraison) / (Envois)</span>

{% endapi %}

{% api %}

## Ouvertures directes {#direct-opens}

{% apitags %}
iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}

<span class="calculation-line">Calcul : (Ouvertures directes) / (Livraisons)</span>

{% endapi %}

{% api %}

## Joignable par e-mail {#emailable}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Calcul : Nombre</span>

{% endapi %}

{% api %}

## Erreurs {#errors}

{% apitags %}
Webhook
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Errors' %} Les erreurs sont incluses dans le nombre d'<i>envois</i> mais ne sont pas incluses dans le nombre de <i>destinataires uniques</i>.

{% endapi %}

{% api %}

## Ouvertures réelles estimées {#estimated-real-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %}

{% endapi %}

{% api %}

## Échecs {#failures}

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failures' %} Les échecs sont inclus dans le nombre d'<i>envois</i> mais pas dans le nombre de <i>livraisons</i>.</td>

<span class="calculation-line">Calcul (<i>taux d'échec</i>) : (Échecs) / (Envois)</span>

{% endapi %}

{% api %}

## Performance de l'expérience d'indicateur de fonctionnalité {#feature-flag-experiment-performance}

{% apitags %}
Feature Flags
{% endapitags %}

Indicateurs de performance pour le message dans une expérience d'indicateur de fonctionnalité. Les indicateurs spécifiques affichés varient en fonction du canal de communication et selon que l'expérience est un test multivarié ou non.

{% endapi %}

{% api %}

## Échec d'envoi définitif {#hard-bounce}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}

Lorsque cela se produit, Braze marque l'adresse e-mail comme invalide mais ne met pas à jour le [statut d'abonnement]({{site.baseurl}}/user_guide/channels/email/subscriptions) de l'utilisateur. Si un e-mail reçoit un échec d'envoi définitif, Braze cesse toute future demande vers cette adresse e-mail.

{% endapi %}

{% api %}

## Aide {#help}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Help' %} La réponse d'un utilisateur est mesurée chaque fois qu'un utilisateur envoie un message entrant dans les quatre heures suivant la réception de votre message.

{% endapi %}

{% api %}

## Ouvertures influencées {#influenced-opens}

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}

<span class="calculation-line">Calcul : (Ouvertures influencées) / (Livraisons)</span>

{% endapi %}

{% api %}

## Chiffre d'affaires à vie {#lifetime-revenue}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}

{% endapi %}

{% api %}

## Valeur vie client par utilisateur {#lifetime-value-per-user}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}

{% endapi %}

{% api %}

## Chiffre d'affaires quotidien moyen {#average-daily-revenue}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}

{% endapi %}

{% api %}

## Achats quotidiens {#daily-purchases}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}

{% endapi %}

{% api %}

## Chiffre d'affaires quotidien par utilisateur {#daily-revenue-per-user}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}

{% endapi %}

{% api %}

## Ouvertures automatiques {#machine-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Cet indicateur est suivi depuis le 11 novembre 2021 pour SendGrid et le 2 décembre 2021 pour SparkPost. Pour Amazon SES, les analyses s'afficheront sous la forme d'_ouvertures_. Cependant, le filtrage des bots pour les clics sera pris en charge.

{% endapi %}

{% api %}

## Ouvertures {#opens}

{% apitags %}
Web Push, iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opens' %}

{% endapi %}

{% api %}

## Désinscription {#opt-out}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opt-Out' %} La réponse d'un utilisateur est mesurée chaque fois qu'un utilisateur envoie un message entrant dans les quatre heures suivant la réception de votre message.

{% endapi %}

{% api %}

## Autres ouvertures {#other-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Notez qu'un utilisateur peut également ouvrir un e-mail (cette ouverture étant comptabilisée dans les Other Opens) avant qu'un comptage de Machine Opens ne soit enregistré. Si un utilisateur ouvre un e-mail une fois (ou plus) après un événement de Machine Opens depuis une boîte de réception autre qu'Apple Mail, le nombre de fois que l'utilisateur ouvre l'e-mail est comptabilisé dans les Other Opens et une seule fois dans les Unique Opens.

{% endapi %}

{% api %}

## Nouvelle tentative en attente {#pending-retry}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Pending Retry' %}

{% endapi %}

{% api %}

## Conversions principales (A) ou événement de conversion principal {#primary-conversions-a-or-primary-conversion-event}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}

| Canal | Informations complémentaires |
|-------|-----------------------|
| E-mail, push, webhooks | Après l'envoi initial. |
| Content Cards, messages in-app | Lorsque l'utilisateur consulte la Content Card ou le message pour la première fois. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conversions principales (A) ou événement de conversion principal" }

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Conversions principales (A) ou événement de conversion principal</i> : Nombre</li>
        <li><i>% de conversions principales (A)</i> ou <i>taux de l'événement de conversion principal</i> : (Conversions principales) / (Destinataires uniques)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Lectures {#reads}

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Reads' %}

{% endapi %}

{% api %}

## Taux de lecture {#read-rate}

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Read Rate' %}

<span class="calculation-line">Calcul : (Lectures avec accusés de lecture) / (Envois)</span>

{% endapi %}

{% api %}

## Reçu {#received}

{% apitags %}
Email, Content Cards, In-App Message, Web Push, iOS Push, Android Push, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Received' %}

| Canal | Informations complémentaires |
|-------|-------|
| Content Cards | Reçu lorsque les utilisateurs consultent la carte dans l'application. |
| Push | Reçu lorsque les messages sont envoyés du serveur Braze au fournisseur de notifications push. |
| E-mail | Reçu lorsque les messages sont envoyés du serveur Braze au fournisseur de services d'e-mailing. |
| SMS/MMS | « Livré » après que le fournisseur SMS reçoit la confirmation de l'opérateur en amont et de l'appareil de destination. |
| Message in-app | Reçu au moment de l'affichage en fonction de l'action de déclenchement définie. |
| WhatsApp | Reçu au moment de l'affichage en fonction de l'action de déclenchement définie. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Reçu" }

{% endapi %}

{% api %}

## Rejets RCS ou rejets SMS {#rcs-rejections-or-sms-rejections}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Rejections' %} En tant que client Braze, les rejets sont déduits de votre allocation SMS.

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Rejets</i> : Nombre</li>
        <li><i>Taux de rejet</i> : (Rejets) / (Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Chiffre d'affaires {#revenue}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

{% endapi %}

{% api %}

## Envoyé {#sent}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sent' %}

<span class="calculation-line">Calcul : Nombre</span>

{% endapi %}

{% api %}

## Envois {#sends}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, RCS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %} Cet indicateur est fourni par Braze. Notez que lors du lancement d'une campagne planifiée, cet indicateur inclura tous les messages envoyés, qu'ils aient déjà été effectivement envoyés ou non en raison de la limite de débit.

{% alert tip %}
Pour les Content Cards, cet indicateur est calculé différemment selon ce que vous avez sélectionné pour la [création de carte]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation) :

- **Au lancement ou à l'entrée dans l'étape :** le nombre de cartes créées et disponibles pour être consultées. Cela ne tient pas compte du fait que les utilisateurs aient consulté la carte ou non.
- **À la première impression :** le nombre de cartes affichées aux utilisateurs.
{% endalert %}

<span class="calculation-line">Calcul : Nombre</span>

{% endapi %}

{% api %}

## Messages envoyés {#messages-sent}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  Cet indicateur est fourni par Braze. Notez que lors du lancement d'une campagne planifiée, cet indicateur inclura tous les messages envoyés, qu'ils aient déjà été effectivement envoyés ou non en raison de la limite de débit.

{% alert tip %}
Pour les Content Cards, cet indicateur est calculé différemment selon ce que vous avez sélectionné pour la [création de carte]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation) :

- **Au lancement ou à l'entrée dans l'étape :** le nombre de cartes créées et disponibles pour être consultées. Cela ne tient pas compte du fait que les utilisateurs aient consulté la carte ou non.
- **À la première impression :** le nombre de cartes affichées aux utilisateurs.
{% endalert %}

<span class="calculation-line">Calcul : Nombre</span>

{% endapi %}

{% api %}

## Envois à l'opérateur {#sends-to-carrier}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Envois à l'opérateur</i> : Nombre</li>
        <li><i>Taux d'envois à l'opérateur</i> : (Envois à l'opérateur) / (Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Échec provisoire d'envoi {#soft-bounce}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Si un e-mail reçoit un échec provisoire d'envoi, une nouvelle tentative est généralement effectuée dans les 72 heures, mais le nombre de tentatives varie d'un destinataire à l'autre.

Notez que les *échecs provisoires d'envoi* diffèrent des *reports*. Si aucun e-mail n'est livré avec succès pendant cette période de nouvelle tentative, Braze envoie un seul événement d'échec provisoire d'envoi par tentative d'envoi de campagne. Avant le 25 février 2025, ces nouvelles tentatives étaient comptabilisées comme plusieurs échecs provisoires d'envoi pour un seul envoi de campagne.

Bien que les échecs provisoires d'envoi ne soient pas suivis dans les analyses de votre campagne, vous pouvez les surveiller dans le [journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log). Vous pouvez également exclure ces utilisateurs de vos envois ou consulter le nombre d'échecs provisoires d'envoi des 30 derniers jours avec le [filtre de segment « Échec provisoire d'envoi »]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#soft-bounced). Dans le journal d'activité des messages, vous pouvez également voir la raison des échecs provisoires d'envoi et comprendre les éventuels écarts entre les « envois » et les « livraisons » de vos campagnes e-mail.

{% endapi %}

{% api %}

## Spam {#spam}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{% alert note %}
Les plaintes pour spam sont traitées directement par les fournisseurs de services d'e-mailing, puis relayées à Braze via une boucle de rétroaction. La plupart des boucles de rétroaction ne signalent qu'une partie des plaintes réelles, de sorte que l'indicateur _Spam_ représente souvent une fraction du total réel. Seuls les fournisseurs de services d'e-mailing peuvent voir le volume réel des plaintes pour spam, ce qui signifie que _Spam_ doit être considéré comme un indicateur indicatif et non exhaustif.
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Spam</i> : Nombre</li>
        <li><i>% de spam</i> ou <i>Taux de spam %</i> : (Marqué comme spam) / (Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Fermetures de la page de sondage {#survey-page-dismissals}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Page Dismissals' %}

{% endapi %}

{% api %}

## Soumissions de sondage {#survey-submissions}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Submissions' %}

{% endapi %}

{% api %}

## Clics totaux {#total-clicks}

{% apitags %}
Email, Content Cards, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}

| Canal | Informations complémentaires |
|-------|-------|
| LINE | Suivi après qu'un seuil minimum de 20 messages par jour a été atteint. Les e-mails AMP incluent les clics enregistrés dans les versions HTML et texte brut. Ce nombre peut être artificiellement gonflé par les outils anti-spam. |
| Bannières | Le nombre total (et le pourcentage) d'utilisateurs qui ont cliqué dans le message livré, qu'un même utilisateur clique plusieurs fois ou non. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Clics totaux" }

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b>E-mail :</b> (Clics totaux) / (Livraisons)</li>
        <li><b>Content Cards :</b> (Clics totaux) / (Impressions totales)</li>
        <li><b>SMS :</b> (Ouvertures par clic) / (Livraisons)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Fermetures totales {#total-dismissals}

{% apitags %}
Content Cards, Banners
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Dismissals' %} Pour les Content Cards, si un utilisateur reçoit deux cartes différentes de la même campagne et ferme les deux, ce compteur augmentera de deux. La rééligibilité vous permet d'incrémenter les *fermetures totales* une fois à chaque fois qu'un utilisateur reçoit une carte ; chaque carte est un message différent. Pour les bannières, chaque fermeture est comptabilisée lorsque le comportement de fermeture est activé.

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Fermetures totales :</i> Nombre</li>
        <li><i>Taux de fermeture total :</i> Fermetures totales / Impressions totales</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Impressions totales {#total-impressions}

{% apitags %}
In-App Message, Content Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} Ce nombre est la somme des événements d'impression que Braze reçoit des SDK.

| Canal | Informations complémentaires |
|-------|-----------------------|
| Content Cards | Le nombre total d'impressions enregistrées pour une Content Card donnée. Ce nombre peut être incrémenté plusieurs fois pour le même utilisateur. |
| Messages in-app | S'il y a plusieurs appareils et que la rééligibilité est désactivée, l'utilisateur ne devrait voir le message in-app qu'une seule fois. Même si l'utilisateur utilise plusieurs appareils, il ne le verra que sur le premier appareil ciblé. Cela suppose que le profil a des appareils consolidés et qu'un utilisateur a un seul identifiant utilisateur avec lequel il est connecté sur tous les appareils. Si la rééligibilité est activée, une impression est enregistrée à chaque fois que l'utilisateur voit le message in-app. Pour plus de détails, consultez <a href="/docs/user_guide/channels/in_app_messages/reporting">Reporting des messages in-app</a>. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Impressions totales" }

<span class="calculation-line">Calcul : Nombre</span>

{% endapi %}

{% api %}

## Ouvertures totales {#total-opens}

{% apitags %}
Email, iOS Push, Android Push, Web Push, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Opens' %}

| Canal | Informations complémentaires |
|-------|-----------------------|
| LINE | Suivi après qu'un seuil minimum de 20 messages par jour a été atteint. |
| E-mails AMP | Le total des ouvertures pour les versions HTML et texte brut. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ouvertures totales" }

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b>E-mail <i>Ouvertures totales</i> :</b> Nombre</li>
        <li><b>E-mail <i>Taux d'ouverture total</i> :</b> (Ouvertures) / (Livraisons)</li>
        <li><b>Notification push Web <i>Ouvertures totales</i> :</b> Nombre d'<i>ouvertures directes</i></li>
        <li><b>Notification push Web <i>Taux d'ouverture total</i> :</b> (Ouvertures totales) / (Livraisons)</li>
        <li><b>Notification push iOS, Android et Kindle <i>Ouvertures totales</i> :</b> (Ouvertures directes) + (Ouvertures influencées)</li>
        <li><b>Notification push iOS, Android et Kindle <i>Taux d'ouverture total</i> :</b> (Ouvertures totales) / (Livraisons)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Chiffre d'affaires total {#total-revenue}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Revenue' %} Cet indicateur n'est disponible que dans les rapports de comparaison de Campaigns via le <a href='/docs/user_guide/analytics/reports/report_builder'>générateur de rapports</a>.

{% endapi %}

{% api %}

## Clics uniques {#unique-clicks}

{% apitags %}
Email, Content Cards, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}

Cela inclut les clics sur les liens de désabonnement fournis par Braze.

| Canal | Informations complémentaires |
|-------|-----------------------|
| E-mail | Suivi sur une période de sept jours. |
| LINE | Suivi après qu'un seuil minimum de 20 messages par jour a été atteint. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Clics uniques" }

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Clics uniques</i> : Nombre</li>
        <li><b>Content Cards</b> <i>% de clics uniques</i> ou <i>taux de clics uniques</i> : (Clics uniques) / (Impressions uniques)</li>
        <li><b>E-mail</b> <i>% de clics uniques</i> ou <i>taux de clics uniques</i> : (Clics uniques) / (Livraisons)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Fermetures uniques {#unique-dismissals}

{% apitags %}
Content Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}

<span class="calculation-line">Calcul : (Fermetures uniques) / (Impressions uniques)</span>

{% endapi %}

{% api %}

## Impressions quotidiennes uniques {#unique-daily-impressions}

{% apitags %}
Content Cards, Banners
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Daily Impressions' %}

Ce nombre est reçu de Braze et est basé sur le `user_id`. Les impressions quotidiennes uniques sont comptabilisées au niveau de la campagne ou de l'étape du Canvas.

<span class="calculation-line">Calcul : Nombre</span>

{% endapi %}

{% api %}

## Impressions uniques {#unique-impressions}

{% apitags %}
In-App Message, Content Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %}

| Canal | Informations complémentaires |
|-------|-----------------------|
| Messages in-app | Les impressions uniques peuvent être incrémentées à nouveau un nouveau jour calendaire dans le fuseau horaire de votre espace de travail si la rééligibilité est activée et que l'utilisateur effectue l'action de déclenchement. Si la rééligibilité est activée, <i>impressions uniques</i> = <i>destinataires uniques</i>. Pour plus de détails, consultez <a href="/docs/user_guide/channels/in_app_messages/reporting">Reporting des messages in-app</a>. |
| Content Cards | Le compteur ne devrait pas être incrémenté la deuxième fois qu'un utilisateur consulte une carte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Impressions uniques" }

<span class="calculation-line">Calcul : Nombre</span>

{% endapi %}

{% api %}

## Ouvertures uniques {#unique-opens}

{% apitags %}
Email, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %}

| Canal | Informations complémentaires |
|-------|-----------------------|
| E-mail | Suivi sur une période de 7 jours. |
| LINE | Suivi après qu'un seuil minimum de 20 messages par jour a été atteint. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ouvertures uniques" }

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Ouvertures uniques</i> : Nombre</li>
        <li><i>% d'ouvertures uniques</i> ou <i>taux d'ouverture unique</i> : (Ouvertures uniques) / (Livraisons)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Destinataires uniques {#unique-recipients}

{% apitags %}
Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, RCS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}

Étant donné qu'un lecteur peut être un destinataire unique chaque jour, vous devez vous attendre à ce que ce nombre soit supérieur aux <i>impressions uniques</i>. Ce nombre est reçu de Braze et est basé sur le `user_id`. Les destinataires uniques sont comptabilisés au niveau de la campagne ou de l'étape du Canvas, et non au niveau de l'<a href='{{ site.homeurl }}{{ site.baseurl }}/api/identifier_types/#send-identifier'>identifiant d'envoi</a>.

<span class="calculation-line">Calcul : Nombre</span>

{% endapi %}

{% api %}

## Désabonnés {#unsubscribers-or-unsub}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Désabonnés</i> : Nombre</li>
        <li><i>% de désabonnés</i> ou <i>taux de désabonnement</i> : (Désabonnements) / (Livraisons)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Désabonnements {#unsubscribes}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribes' %}

<span class="calculation-line">Calcul : (Désabonnements) / (Livraisons)</span>

{% endapi %}

{% api %}

## Variante {#variation}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Calcul : Nombre</span>

{% endapi %}