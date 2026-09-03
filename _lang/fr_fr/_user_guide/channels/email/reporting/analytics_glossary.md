---
nav_title: Glossaire analytique pour l'e-mail
article_title: Glossaire analytique pour l'e-mail
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "Ce glossaire inclut les termes que vous trouverez dans la section d'analyse de votre campagne par e-mail ou de votre Canvas, après son lancement. Ce glossaire n'inclut pas les indicateurs Currents."
channel:
  - email
---

> Ce glossaire définit les indicateurs de l'onglet **Analytics** pour les campagnes par e-mail et les Canvas. Braze ne propose pas de page hébergée « afficher cet e-mail dans un navigateur » — consultez [Puis-je ajouter un lien « afficher cet e-mail dans un navigateur » à mes e-mails ?]({{site.baseurl}}/user_guide/channels/email/faq#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails) pour une solution de contournement. Pour d'autres questions de résolution des problèmes couvrant plusieurs indicateurs, consultez la [FAQ e-mail]({{site.baseurl}}/user_guide/channels/email/faq).

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### Variante {#variation}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Joignable par e-mail {#emailable}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### % d'audience {#audience}

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Calcul : (Nombre de destinataires dans la variante) / (Destinataires uniques)</span>

{% endapi %}

{% api %}

### Destinataires uniques {#unique-recipients}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} Ce nombre est fourni par Braze.

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Envois {#sends}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %}  Cet indicateur est fourni par Braze.

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Messages envoyés {#messages-sent}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  Cet indicateur est fourni par Braze.

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Livraisons {#deliveries}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %} Pour les e-mails, *Livraisons* correspond au nombre total de messages (Envois) envoyés avec succès et reçus par les destinataires joignables par e-mail.

<span class="calculation-line">Calcul : (Envois) - (Rebonds) </span>

{% alert note %}
Pour l'état **reçu** au niveau de l'utilisateur et la logique associée (comme la limite de fréquence), Braze marque généralement un utilisateur lorsque l'envoi est traité et transmis pour livraison, et non lorsque le fournisseur de services d'e-mailing (ESP) confirme la livraison finale dans la boîte de réception. Cela évite les décalages temporels entre la confirmation de l'ESP et les règles internes au produit. Les résultats peuvent différer des rapports de livraison de l'ESP ou de tiers.
{% endalert %}

{% endapi %}

{% api %}

### % de livraisons

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries %' %}

<span class="calculation-line">Calcul : (Envois - Rebonds) / (Envois) </span>

{% endapi %}

{% api %}

### Rebonds {#bounces}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %}

Pour les e-mails, le *% de rebonds* ou le *taux de rebond* correspond au pourcentage de messages qui n'ont pas été envoyés avec succès ou qui ont été désignés comme « retournés » ou « non reçus » par les services d'envoi utilisés, ou qui n'ont pas été reçus par les destinataires joignables par e-mail visés.

Un rebond d'e-mail pour les clients utilisant SendGrid comprend les échecs d'envoi définitifs, le spam (`spam_report_drops`) et les e-mails envoyés à des adresses invalides (`invalid_emails`).

{% alert note %}
Dans [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), les reports temporaires de l'ESP sont souvent représentés comme des échecs provisoires d'envoi. Les outils de livrabilité (par exemple, les rapports natifs de SendGrid ou les modèles Looker) peuvent utiliser les reports pour la même situation. Les reports sont généralement temporaires et le courrier est souvent livré après de nouvelles tentatives. Après des tentatives prolongées (jusqu'à environ 72 heures pour les échecs provisoires d'envoi dans l'analyse des campagnes), un message peut être considéré comme non livrable selon votre ESP. Les événements e-mail de Currents sont en ajout uniquement : un échec provisoire d'envoi enregistré n'est pas supprimé ultérieurement si le message finit par être livré.
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Rebonds</i> :</b> Total</li>
        <li><b><i>% de rebonds</i> ou <i>Taux de rebond %</i> :</b> (Rebonds) / (Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Échec d'envoi définitif {#hard-bounce}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}

Lorsqu'un e-mail subit un échec d'envoi définitif ou est marqué comme spam, Braze marque l'adresse e-mail comme invalide mais ne met pas à jour le [statut d'abonnement]({{site.baseurl}}/user_guide/channels/email/subscriptions) de l'utilisateur. Braze cesse tout envoi futur à cette adresse e-mail. Pour supprimer une adresse e-mail de votre liste d'échecs d'envoi définitifs, utilisez l'[endpoint de suppression des e-mails en échec d'envoi définitif]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces).

<span class="calculation-line">Calcul : Total </span>

{% endapi %}

{% api %}

### Échec provisoire d'envoi {#soft-bounce}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Si un e-mail subit un échec provisoire d'envoi, une nouvelle tentative est généralement effectuée dans les 72 heures, mais le nombre de tentatives varie selon le destinataire.

Bien que les échecs provisoires d'envoi ne soient pas suivis dans l'analyse de votre campagne, vous pouvez les surveiller dans le [Journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) ou exclure ces utilisateurs de vos envois avec le [filtre de segment Échec provisoire d'envoi]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#soft-bounced). Dans le Journal d'activité des messages, vous pouvez également voir la raison des échecs provisoires d'envoi et comprendre les éventuels écarts entre les « envois » et les « livraisons » de vos campagnes par e-mail.

<span class="calculation-line">Calcul : Total </span>

{% endapi %}

{% api %}

### Spam {#spam}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Spam</i> :</b> Total</li>
        <li><b><i>% de spam</i> ou <i>Taux de spam %</i> :</b> (Marqué comme spam) / (Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Ouvertures uniques {#unique-opens}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} Pour les e-mails, le suivi s'effectue sur une période de sept jours. Cela signifie qu'un même utilisateur qui ouvre à nouveau le même e-mail après sept jours est comptabilisé comme une nouvelle ouverture unique. Par conséquent, le nombre d'ouvertures uniques affiché dans le tableau de bord peut être supérieur à celui obtenu par une simple requête `DISTINCT user_id` sur les données Currents. Pour faire correspondre les chiffres du tableau de bord à partir de Currents, filtrez les événements où `is_unique` est `true`.

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Ouvertures uniques</i> :</b> Total</li>
        <li><b><i>% d'ouvertures uniques</i> ou <i>Taux d'ouverture unique</i> :</b> (Ouvertures uniques) / (Livraisons)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Clics uniques {#unique-clicks}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Le suivi s'effectue sur une période de sept jours pour les e-mails et est mesuré par <a href='/docs/user_guide/messaging/messaging_fundamentals/dispatch_id'>dispatch_id</a> (une seule tentative d'envoi). Cela inclut les clics sur les liens de désabonnement fournis par Braze. Les URL de désabonnement personnalisées suivies sont également comptabilisées dans les *Clics uniques* lorsqu'un utilisateur sélectionne le lien. Après sept jours, un nouveau clic unique est comptabilisé pour le même utilisateur s'il clique à nouveau. Les indicateurs d'engagement e-mail du tableau de bord, y compris les _Clics uniques_, sont calculés dans Braze et ne sont pas réconciliés à partir des rapports agrégés de l'ESP. Pour faire correspondre les chiffres du tableau de bord à partir de Currents, filtrez les événements où `is_unique` est `true`.

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Clics uniques</i> :</b> Total</li>
        <li><b><i>% de clics uniques</i> ou <i>Taux de clics</i> :</b> (Clics uniques) / (Livraisons)</li>
    </ul>
</span>
{:/}

#### Liens inattendus sur la carte de chaleur des e-mails {#unexpected-links-on-the-email-heatmap}

Lorsque la [carte de chaleur des e-mails]({{site.baseurl}}/user_guide/channels/email/reporting) affiche des liens que vous n'attendez pas, inspectez le HTML du message à la recherche de [blocs de contenu]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/dnd_editor_blocks) ou d'espaces entre les mots qui créent des URL suivies. Utilisez le **tableau des liens par nombre total de clics** dans la vue de la carte de chaleur pour identifier les URL qui ne correspondent pas au texte visible.

Braze ne développe pas les étiquettes Liquid dans l'aperçu du message, de sorte que le moteur de rendu de la carte de chaleur ne peut pas faire correspondre le lien cliqué dans l'aperçu. Il s'agit d'un comportement attendu. Le moteur de rendu de la carte de chaleur tente de faire correspondre les URL cliquées avec celles du message. Lorsque l'URL est significativement différente, par exemple lorsque l'URL entière est transmise en tant que propriété d'événement, la carte de chaleur ne peut pas l'identifier.

{% endapi %}

{% api %}

### Clics totaux {#total-clicks}

{% apitags %}
Count, Percentage
{% endapitags %}

<i>Clics totaux</i> correspond au nombre total de fois où les utilisateurs ont cliqué sur des liens dans l'e-mail livré, y compris les clics multiples du même utilisateur. Cela inclut les clics sur les liens de désabonnement Braze et les URL de désabonnement personnalisées suivies.

Lorsque les *Clics totaux* sont nettement supérieurs aux *Clics uniques*, des outils de sécurité ou des fournisseurs de messagerie analysent les liens sans que les utilisateurs n'ouvrent le message. Comparez les *Clics uniques* lorsque vous évaluez l'engagement en interne.

{% endapi %}

{% api %}

### Désabonnements {#unsubscribers-or-unsub}

{% apitags %}
Count, Percentage
{% endapitags %}

Les _désabonnements_ reflètent le lien de désabonnement standard de Braze. Les pages de désabonnement personnalisées n'incrémentent pas cet indicateur, sauf si vous mettez à jour les utilisateurs via l'API. La **chronologie des groupes d'abonnement** reflète toujours les modifications effectuées via l'API.

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Désabonnements</i> :</b> Total</li>
        <li><b><i>% de désabonnements</i> ou <i>Taux de désabonnement</i> :</b> (Désabonnements) / (Livraisons)</li>
    </ul>
</span>
{:/}

#### Pourquoi les *désabonnements* et les clics sur le lien de désabonnement peuvent différer {#why-unsubscribes-and-unsubscribe-link-clicks-can-differ}

Sur la page **Analytics** d'une campagne par e-mail ou d'un Canvas, comparez le nombre de *désabonnements* aux clics sur l'URL de désabonnement Braze dans le détail par lien lorsque vous développez **Total Clicks** ou **Unique Clicks**. Les deux correspondent souvent, mais peuvent différer :

- **Plus de *désabonnements* que de clics sur l'URL de désabonnement dans le corps du message :** Le [list-unsubscribe]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#list-unsubscribe) est un chemin de désabonnement supplémentaire dans l'en-tête de l'e-mail (et non le lien dans le corps de votre message). Lorsqu'un utilisateur se désabonne de cette manière, cela est comptabilisé dans les *désabonnements* mais ne compte pas comme un clic sur l'URL de désabonnement suivie dans le corps du message.
- **Plus de clics sur l'URL de désabonnement dans le corps du message que de *désabonnements* :** Un utilisateur peut cliquer sur ce lien plusieurs fois. S'il se désabonne, se réabonne, puis se désabonne à nouveau, l'analyse des e-mails peut enregistrer plusieurs clics (par exemple, deux) dans le détail des clics.

Pour en savoir plus, consultez [Pourquoi le nombre de désabonnements diffère-t-il du nombre de clics sur mon lien de désabonnement ?]({{site.baseurl}}/user_guide/channels/email/faq#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link).

{% endapi %}

{% api %}

### Chiffre d'affaires {#revenue}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

<span class="calculation-line">Calcul : Total </span>

{% endapi %}

{% api %}

### Conversions principales (A) ou événement de conversion principal {#primary-conversions-a-or-primary-conversion-event}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} Pour les e-mails, les notifications push et les webhooks, le suivi des conversions commence après l'envoi initial.

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Conversions principales (A)</i> ou <i>Événement de conversion principal</i> :</b> Total</li>
        <li><b><i>% de conversions principales (A)</i> ou <i>Taux d'événement de conversion principal</i> :</b> (Conversions principales) / (Destinataires uniques)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Confiance {#confidence}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Ouvertures automatiques {#machine-opens}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Cet indicateur est suivi depuis le 11 novembre 2021 pour SendGrid et le 2 décembre 2021 pour SparkPost.

<span class="calculation-line">Calcul : Total </span>

{% endapi %}

{% api %}

### Autres ouvertures {#other-opens}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Notez qu'un utilisateur peut également ouvrir un e-mail (cette ouverture étant comptabilisée dans les <i>Autres ouvertures</i>) avant qu'un comptage d'<i>Ouvertures automatiques</i> ne soit enregistré. Si un utilisateur ouvre un e-mail une ou plusieurs fois après un événement d'ouverture automatique depuis une boîte de réception autre qu'Apple Mail, le nombre de fois où l'utilisateur ouvre l'e-mail est comptabilisé dans les <i>Autres ouvertures</i> et une seule fois dans les <i>Ouvertures uniques</i>.

<span class="calculation-line">Calcul : Total </span>

{% endapi %}

{% api %}

### Ouvertures réelles estimées {#estimated-real-opens}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %} Braze recalcule cette estimation à mesure que de nouvelles données d'ouverture et de clic arrivent. La valeur se stabilise généralement quelques jours après l'envoi, mais continue de se mettre à jour lorsque de nouveaux événements qualifiants surviennent.

{% endapi %}

{% api %}

### Taux de clics par ouverture {#click-to-open-rate}

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Calcul : (Clics uniques) / (Ouvertures uniques) (pour les e-mails)</span>

#### Scores de probabilité d'ouverture de message (segmentation) {#message-open-likelihood-scores-segmentation}

Le filtre de segment [`Message Open Likelihood`]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#message-open-likelihood) évalue la probabilité qu'un utilisateur ouvre un e-mail sur une échelle de 0 à 100 %. Les utilisateurs sans historique d'envoi ou d'ouverture suffisant pour le canal apparaissent comme vides. Pour les e-mails, les ouvertures automatiques sont exclues du calcul, qui utilise l'historique récent des messages sur ce canal (voir [Filtre de probabilité d'ouverture de message pour les canaux individuels]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel#individual-channels)).

{% endapi %}

## Résolution des problèmes et FAQ sur les rapports e-mail {#email-reporting-troubleshooting-and-faqs}

### Liens de désabonnement et clics uniques {#unsubscribe-links-and-unique-clicks}

Lorsqu'un destinataire clique sur un lien de désabonnement, Braze le comptabilise comme un clic, car l'action utilise une URL. Cela s'applique aux liens de désabonnement fournis par Braze et aux liens de désabonnement personnalisés dans le corps de votre message. Ces clics contribuent aux *clics uniques* et aux *clics totaux* au même titre que les autres clics sur des liens. Pour les définitions des indicateurs, consultez [Clics uniques](#unique-clicks) et [Pourquoi le nombre de désabonnements diffère-t-il du nombre de clics sur mon lien de désabonnement ?]({{site.baseurl}}/user_guide/channels/email/faq#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link).

### Afficher dans le navigateur {#view-in-browser}

Braze ne propose pas de fonctionnalité intégrée « Afficher cet e-mail dans un navigateur ». Hébergez le contenu de l'e-mail sur une page de destination externe (comme votre site web) et ajoutez un lien depuis le message à l'aide de l'outil **Lien** de l'éditeur d'e-mail. Pour en savoir plus, consultez [Puis-je ajouter un lien « afficher cet e-mail dans un navigateur » à mes e-mails ?]({{site.baseurl}}/user_guide/channels/email/faq#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails).

### Mises à jour de la page de désabonnement personnalisée {#custom-unsubscribe-page-updates}

Les modifications apportées à votre [page de désabonnement personnalisée]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences) apparaissent en quelques minutes. Les envois en cours utilisent un cache de courte durée de la page, qui est actualisé lorsque vous enregistrez vos modifications.

### Rebonds pour dépassement de quota et boîte de réception pleine {#over-quota-and-full-mailbox-bounces}

Un rebond pour dépassement de quota ou boîte de réception pleine signifie que la boîte de réception du destinataire ne peut pas accepter de nouveaux messages. Vous pouvez observer ces adresses parmi les nouvelles inscriptions comportant des adresses invalides ou à risque, ou parmi les profils inactifs depuis longtemps dont les boîtes de réception se sont remplies pendant leur période d'inactivité.

Examinez les taux de rebond par Segment et par source, supprimez ou désactivez les adresses qui génèrent des échecs d'envoi définitifs de manière répétée, et utilisez l'abonnement confirmé ou le double opt-in pour les nouveaux abonnés. Pour les bonnes pratiques d'hygiène de liste, consultez [Pièges de livrabilité et spam traps]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps) et [Rapports e-mail]({{site.baseurl}}/user_guide/channels/email/reporting#troubleshooting).

### 550 5.7.1 courrier non sollicité {#550-571-unsolicited-mail}

Une réponse `550 5.7.1` telle que « Our system has detected that this message is likely unsolicited mail » provient souvent de fournisseurs de messagerie stricts (par exemple, Gmail) lorsque les signaux de réputation ou d'engagement sont faibles. Les causes courantes incluent les plaintes pour spam, un faible engagement, les listes achetées ou louées, et les pics de volume soudains.

Concentrez-vous sur une croissance de liste basée sur le consentement, désactivez les abonnés inactifs, et surveillez les taux de plaintes et de rebonds. Pour en savoir plus, consultez [Pièges de livrabilité et spam traps]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps).

### Bons taux de livrabilité des e-mails {#good-email-deliverability-rates}

La **distribution** indique si le serveur destinataire accepte votre message ; vous pouvez la mesurer à l'aide d'indicateurs tels que les *distributions* et le taux de rebond. La **livrabilité** (placement en boîte de réception) dépend du filtrage du fournisseur et n'est pas représentée par un indicateur unique dans Braze.

En règle générale, visez un taux de distribution proche de 99 % avec des échecs d'envoi définitifs inférieurs à environ 1 %, et surveillez les ouvertures et les clics pour détecter les tendances d'engagement. Les objectifs exacts varient selon le secteur d'activité et le rythme d'envoi. Pour les pratiques qui soutiennent la réputation, consultez [Améliorer la livrabilité des e-mails]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability) et [Pièges de livrabilité et spam traps]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps).

### « Campaign is already in delay window, so not enqueueing another »

Dans le journal d'activité des messages ou les journaux de diagnostic des [Campaigns déclenchées par une action]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery), ce résultat de traitement signifie que Braze a bloqué un envoi en double alors qu'un déclencheur précédent pour le même utilisateur se trouve encore dans la fenêtre de distribution de la Campaign. Un verrou anti-rebond empêche la mise en file d'attente multiple pour la même rafale de déclencheurs.

Vous pouvez observer ce résultat même lorsque la Campaign affiche **Envoyer immédiatement** si l'une des conditions suivantes s'applique :

- La Campaign utilise un [événement d'exception]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events) ou un délai d'envoi qui affecte le timing.
- Les utilisateurs ont une période de [rééligibilité]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility), de sorte qu'ils ne peuvent pas recevoir le message à nouveau tant que cette fenêtre n'est pas écoulée.
- Une autre Campaign ou une étape de message Canvas avec une priorité plus élevée a consommé le créneau d'envoi lorsque les déclencheurs se chevauchent.

Si un utilisateur aurait dû recevoir le message mais ne l'a pas reçu, vérifiez les résultats précédents pour le même déclencheur (par exemple, rebond d'e-mail ou canal non activé). Un autre message dans le même workflow peut avoir empêché cet envoi.

### Comment Braze calcule-t-il les clics uniques pour les e-mails ? {#how-does-braze-calculate-unique-clicks-for-email}

Braze comptabilise les *clics uniques* sur une fenêtre de sept jours par destinataire et par [`dispatch_id`]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id). Pour la définition complète, les formules, le comportement des liens de désabonnement et l'alignement avec Currents, consultez [Clics uniques](#unique-clicks).