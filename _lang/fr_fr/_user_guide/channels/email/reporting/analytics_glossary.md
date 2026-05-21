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

Lorsqu'un e-mail subit un échec d'envoi définitif ou est marqué comme spam, Braze marque l'adresse e-mail comme invalide mais ne met pas à jour le [statut d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) de l'utilisateur. Braze cesse tout envoi futur à cette adresse e-mail. Pour supprimer une adresse e-mail de votre liste d'échecs d'envoi définitifs, utilisez l'[endpoint de suppression des e-mails en échec d'envoi définitif]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/).

<span class="calculation-line">Calcul : Total </span>

{% endapi %}

{% api %}

### Échec provisoire d'envoi {#soft-bounce}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Si un e-mail subit un échec provisoire d'envoi, une nouvelle tentative est généralement effectuée dans les 72 heures, mais le nombre de tentatives varie selon le destinataire.

Bien que les échecs provisoires d'envoi ne soient pas suivis dans l'analyse de votre campagne, vous pouvez les surveiller dans le [Journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/) ou exclure ces utilisateurs de vos envois avec le [filtre de segment Échec provisoire d'envoi]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#soft-bounced). Dans le Journal d'activité des messages, vous pouvez également voir la raison des échecs provisoires d'envoi et comprendre les éventuels écarts entre les « envois » et les « livraisons » de vos campagnes par e-mail.

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

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Le suivi s'effectue sur une période de sept jours pour les e-mails et est mesuré par <a href='/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>. Cela inclut les clics sur les liens de désabonnement fournis par Braze. Après sept jours, un nouveau clic unique peut être comptabilisé pour le même utilisateur s'il clique à nouveau. Pour faire correspondre les chiffres du tableau de bord à partir de Currents, filtrez les événements où `is_unique` est `true`.

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Clics uniques</i> :</b> Total</li>
        <li><b><i>% de clics uniques</i> ou <i>Taux de clics</i> :</b> (Clics uniques) / (Livraisons)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Désabonnements {#unsubscribers-or-unsub}

{% apitags %}
Count, Percentage
{% endapitags %}

Les *désabonnements* reflètent le lien de désabonnement standard de Braze. Les pages de désabonnement personnalisées n'incrémentent pas cet indicateur, sauf si vous mettez à jour les utilisateurs via l'API. La **chronologie des groupes d'abonnement** reflète toujours les modifications effectuées via l'API.

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

- **Plus de *désabonnements* que de clics sur l'URL de désabonnement dans le corps du message :** Le [list-unsubscribe]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/#list-unsubscribe) est un chemin de désabonnement supplémentaire dans l'en-tête de l'e-mail (et non le lien dans le corps de votre message). Lorsqu'un utilisateur se désabonne de cette manière, cela est comptabilisé dans les *désabonnements* mais ne compte pas comme un clic sur l'URL de désabonnement suivie dans le corps du message.
- **Plus de clics sur l'URL de désabonnement dans le corps du message que de *désabonnements* :** Un utilisateur peut cliquer sur ce lien plusieurs fois. S'il se désabonne, se réabonne, puis se désabonne à nouveau, l'analyse des e-mails peut enregistrer plusieurs clics (par exemple, deux) dans le détail des clics.

Pour en savoir plus, consultez [Pourquoi le nombre de désabonnements diffère-t-il du nombre de clics sur mon lien de désabonnement ?]({{site.baseurl}}/user_guide/channels/email/faq/#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link).

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

### Taux de clics par ouverture {#click-to-open-rate}

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Calcul : (Clics uniques) / (Ouvertures uniques) (pour les e-mails)</span>

{% endapi %}