---
nav_title: Raccourcissement de liens
article_title: Raccourcissement de liens
page_order: 1
description: "Cet article de référence explique comment activer le raccourcissement de liens dans vos messages SMS et répond à quelques questions fréquentes."
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
---

# Raccourcissement de liens {#link-shortening}

> Cette page explique comment activer le raccourcissement de liens dans vos messages SMS et RCS, tester les liens raccourcis, utiliser votre domaine personnalisé dans les liens raccourcis, et plus encore.

{% alert important %}
Braze déploie progressivement le [raccourcissement de liens unifié]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening?sdktab=unified), qui consolide tous les liens raccourcis SMS et RCS en un format de lien personnalisé unique (par exemple, `brz.ai/abcdefgh`).
{% endalert %}

{% sdktabs %}
{% sdktab Legacy %}

Le raccourcissement de liens et le suivi des clics vous permettent de raccourcir automatiquement les URL contenues dans les messages SMS ou RCS et de collecter des analyses de taux de clics, fournissant des indicateurs d'engagement supplémentaires pour vous aider à comprendre comment les utilisateurs interagissent avec vos Campaigns.

Le raccourcissement de liens et le suivi des clics peuvent être activés au [niveau de la variante du message]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#step-1-create-your-campaign) dans les Campaigns et les Canvas.

{% multi_lang_include channels/sms/rcs_link_shortening_note.md %}

La longueur de l'URL est déterminée par le type de suivi activé :
- **Le suivi basique** permet le suivi des clics au niveau de la Campaign. Les URL statiques ont une longueur de 20 caractères, et les URL personnalisées ont une longueur de 25 caractères.
- **Le suivi avancé** permet le suivi des clics au niveau de la Campaign et au niveau de l'utilisateur, et active l'utilisation des fonctionnalités de segmentation et de reciblage qui reposent sur les clics. Les clics génèrent également un [événement de clic SMS]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) envoyé via Currents. Les URL statiques avec suivi avancé ont une longueur de 27 à 28 caractères, vous permettant de créer des segments d'utilisateurs ayant cliqué sur des URL. Les URL personnalisées ont une longueur de 32 à 33 caractères.

Les liens sont raccourcis à l'aide de notre domaine court partagé (`brz.ai`) ou de votre domaine personnalisé de raccourcissement de liens. Un exemple d'URL pourrait ressembler à ceci : `https://brz.ai/8jshX` (basique, statique) ou `https://brz.ai/p/8jshX/2dj8d` (avancé, personnalisé). Consultez la section [Test](#legacy_testing) pour plus d'informations.

Toutes les URL statiques commençant par `http://` ou `https://` sont raccourcies. Les URL statiques raccourcies sont valides pendant un an à compter de leur date de création. Les URL raccourcies contenant une personnalisation Liquid sont valides pendant deux mois.

{% alert note %}
Les liens raccourcis de Braze incluent toujours le protocole `https://` et ne peuvent pas être configurés pour utiliser un protocole différent.
{% endalert %}

## Utiliser le raccourcissement de liens {#using-link-shortening}

Pour utiliser le raccourcissement de liens, assurez-vous que le bouton bascule de raccourcissement de liens dans le composeur de messages est activé. Ensuite, choisissez d'utiliser le suivi basique ou avancé.

![Composeur de messages avec un bouton bascule pour le raccourcissement de liens.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening1.png %}){: width="1614" height="994"}

Braze ne reconnaît que les URL commençant par `http://` ou `https://`. Lorsqu'une URL est reconnue, la section **Aperçu** se met à jour avec une URL de substitution. Braze estime la longueur de l'URL après raccourcissement, mais un avertissement vous invite à sélectionner un utilisateur test et à enregistrer le message en tant que brouillon pour une estimation plus précise.

![Composeur de messages avec une longue URL dans le champ « Message » et un lien raccourci généré dans l'aperçu.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening3.png %}){: width="1569" height="516"}

{% alert note %}
Si vous prévoyez d'utiliser le [filtre de canal intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel) BrazeAI<sup>TM</sup> et souhaitez que les canaux SMS et RCS soient sélectionnables, activez le raccourcissement de liens avec le suivi avancé.
{% endalert %}

### Ajouter des paramètres UTM {#adding-utm-parameters}

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## Personnalisation Liquid dans les URL {#liquid-personalization-in-urls}

Vous pouvez construire dynamiquement votre URL directement dans le composeur Braze, ce qui vous permet d'ajouter des paramètres UTM dynamiques à vos URL ou d'envoyer aux utilisateurs des liens uniques (comme diriger les utilisateurs vers leur panier abandonné ou vers un produit spécifique de nouveau en stock).

### Créer une URL avec des balises de personnalisation Liquid prises en charge {#create-a-url-with-supported-liquid-personalization-tags}

Les URL peuvent être générées dynamiquement grâce à l'utilisation de n'importe quelle [balise de personnalisation Liquid prise en charge]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Braze prend également en charge le raccourcissement de variables Liquid personnalisées, comme dans les exemples suivants :

### Créer une URL à l'aide de variables Liquid {#create-a-url-using-liquid-variables}

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Raccourcir les URL rendues par des variables Liquid {#shorten-urls-rendered-by-liquid-variables}

**Canaux pris en charge :** KakaoTalk, LINE, SMS, RCS, WhatsApp

Braze raccourcit les URL rendues par Liquid, y compris celles incluses dans les propriétés de déclenchement API. Par exemple, si {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} représente une URL valide, Braze raccourcit et suit cette URL avant d'envoyer le message.

### Raccourcir les URL dans l'endpoint `/messages/send` {#shorten-urls-in-messagessend-endpoint}

Le raccourcissement de liens est également activé pour les messages API uniquement via l'[endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages). Pour activer également le suivi basique ou avancé, utilisez les paramètres de requête `link_shortening_enabled` ou `user_click_tracking_enabled`.

| Paramètre | Obligatoire | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `link_shortening_enabled` | Facultatif | Booléen | Définissez `link_shortening_enabled` sur `true` pour activer le raccourcissement de liens et le suivi des clics au niveau de la Campaign. Pour utiliser le suivi, un `campaign_id` et un `message_variation_id` doivent être présents. |
| `user_click_tracking_enabled` | Facultatif | Booléen | Définissez `user_click_tracking_enabled` sur `true` pour activer le raccourcissement de liens, ainsi que le suivi des clics au niveau de la Campaign et au niveau de l'utilisateur. Vous pouvez utiliser les données suivies pour créer des segments d'utilisateurs ayant cliqué sur des URL.<br><br> Pour utiliser ce paramètre, `link_shortening_enabled` doit être `true`, et un `campaign_id` et un `message_variation_id` doivent être présents. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Raccourcir les URL dans l'endpoint /messages/send" }

Pour une liste complète des paramètres de requête, consultez les [paramètres de requête]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters).

## Test {#legacy_testing}

Avant de lancer votre Campaign ou Canvas, il est recommandé de prévisualiser et de tester votre message au préalable. Pour ce faire, accédez à l'onglet **Test** pour prévisualiser et envoyer un message SMS ou RCS à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) ou à un utilisateur individuel.

Cet aperçu se met à jour avec la personnalisation pertinente et l'URL raccourcie. Le nombre de caractères et les [segments facturables]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator) se mettent également à jour pour refléter la personnalisation rendue et l'URL raccourcie.

Assurez-vous d'enregistrer la Campaign ou le Canvas avant d'envoyer un message de test pour recevoir une représentation de l'URL raccourcie qui est envoyée dans votre message. Si la Campaign ou le Canvas n'est pas enregistré avant un envoi de test, l'envoi de test inclut une URL de substitution.

Pour que les Canvas apparaissent dans le filtre « A cliqué sur un lien SMS raccourci », l'étape du Canvas contenant le lien court doit également être activée avec le suivi avancé, qui permet le suivi des clics au niveau de l'utilisateur. Si le lien court est configuré avec le suivi basique, l'option de filtrer les événements de clic sur les liens SMS courts n'est pas disponible. La même exigence de suivi avancé s'applique lorsque vous configurez des entrées Canvas ou des parcours d'action qui dépendent de liens SMS raccourcis cliqués.

{% alert important %}
Si un brouillon est créé au sein d'un Canvas actif, une URL raccourcie ne sera pas générée. L'URL raccourcie réelle est générée lorsque le brouillon du Canvas est rendu actif.
{% endalert %}

![Onglet « Test » du message avec des champs pour sélectionner les destinataires de test.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening2.png %}){: width="1569" height="947"}

{% alert note %}
La personnalisation Liquid et les URL raccourcies sont modélisées dans l'onglet **Test** après qu'un utilisateur a été sélectionné. Assurez-vous qu'un utilisateur est sélectionné pour recevoir un décompte de caractères précis.
{% endalert %}

## Suivi des clics {#click-tracking}

Lorsque le raccourcissement de liens est activé, le tableau **Performances SMS/MMS/RCS** inclut une colonne intitulée **Total des clics** qui affiche un décompte des événements de clic par variante et un taux de clics associé. Le **Total des clics** exclut les clics suspects de bots des décomptes du tableau de bord. Pour plus de détails sur les indicateurs, consultez [Performances des messages]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting) et [Filtrage des clics de bots]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/bot_click_filtering).

![Tableau des indicateurs de performances SMS et MMS.]({% image_buster /assets/img/link_shortening/shortening4.png %}){: width="1586" height="191"}

Les tableaux **Performances historiques** et **Performances SMS/MMS/RCS** incluent également une option pour le **Total des clics** et affichent une série temporelle quotidienne des événements de clic. Les clics sont incrémentés lors de la redirection (par exemple lorsqu'un utilisateur visite un lien) et peuvent être incrémentés plus d'une fois par utilisateur.

## Recibler les utilisateurs {#retargeting-users}

Pour des conseils sur le reciblage, consultez [Reciblage]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting#filter-by-advanced-tracking-links).

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### Puis-je savoir quels utilisateurs individuels cliquent sur une URL ? {#do-i-know-which-individual-users-are-clicking-on-a-url}

Oui. Lorsque le **suivi avancé** est activé, vous pouvez recibler les utilisateurs ayant cliqué sur des URL en exploitant les [filtres de reciblage SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting) ou les événements de clic SMS (`users.messages.sms.ShortLinkClick`) envoyés par Currents.

### Le raccourcissement de liens fonctionne-t-il avec les deep links ou les liens universels ? {#does-link-shortening-work-with-deep-links-or-universal-links}

Le raccourcissement de liens ne fonctionne pas avec les deep links. Vous pouvez toutefois raccourcir les liens universels provenant de fournisseurs tiers tels que Branch or branche ou Appsflyer, mais les utilisateurs peuvent rencontrer une brève redirection ou un effet de « scintillement ». Cela se produit parce que le lien raccourci passe d'abord par le web avant de résoudre vers le lien universel qui prend en charge l'ouverture de l'application. De plus, Braze n'est pas en mesure de résoudre les problèmes pouvant survenir lors du raccourcissement de liens universels, tels que la rupture de l'attribution ou des redirections inattendues.

{% alert note %}
Testez l'expérience utilisateur avant de mettre en œuvre le raccourcissement de liens avec des liens universels pour confirmer qu'il répond à vos attentes.
{% endalert %}

### Les `send_ids` sont-ils associés aux événements de clic SMS ? {#are-send_ids-associated-with-sms-click-events}

Non. Cependant, si le suivi avancé est activé, vous pouvez généralement attribuer les `send_ids` aux événements de clic en utilisant le [générateur de requêtes]({{site.baseurl}}/query_builder) pour interroger les données Currents avec cette requête :

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL;
```


{% endsdktab %}
{% sdktab Unified %}

{% multi_lang_include channels/sms/unified_link_shortening.md %}

{% endsdktab %}
{% endsdktabs %}