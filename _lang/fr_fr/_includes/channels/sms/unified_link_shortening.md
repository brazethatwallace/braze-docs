Le raccourcissement de liens vous permet de raccourcir automatiquement les URL contenues dans les messages SMS ou RCS et de collecter des données analytiques sur le taux de clics, fournissant ainsi des indicateurs d'engagement supplémentaires pour mieux comprendre comment les utilisateurs interagissent avec vos Campaigns.

Le raccourcissement de liens peut être activé au [niveau de la variante du message]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#step-1-create-your-campaign) dans les Campaigns comme dans les Canvas. Lorsque le raccourcissement de liens est activé, les clics génèrent un [événement de clic SMS]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) envoyé via Currents.

{% multi_lang_include channels/sms/rcs_link_shortening_note.md %}

Les liens sont raccourcis à l'aide de notre domaine court partagé (`brz.ai`) ou de votre domaine de raccourcissement de liens personnalisé, et sont valides pendant 9 semaines à compter de leur date de création. Un exemple d'URL raccourcie ressemble à `https://brz.ai/8jshX2dj`.

## Utilisation du raccourcissement de liens {#using-link-shortening}

Pour utiliser le raccourcissement de liens, assurez-vous que la case correspondante est cochée dans le compositeur de messages.

{% tabs %}
{% tab Compositeur SMS %}

![Compositeur de messages SMS avec une case cochée pour le raccourcissement de liens.]({% image_buster /assets/img/link_shortening/shortening1.png %}){: width="1562" height="1068"}

{% endtab %}
{% tab Compositeur RCS %}

![Compositeur de messages RCS avec une case cochée pour le raccourcissement de liens.]({% image_buster /assets/img/link_shortening/shortening1_rcs.png %}){: width="1476" height="1222"}

{% endtab %}
{% endtabs %}

Braze ne reconnaît que les URL commençant par `http://` ou `https://`. Lorsqu'une URL est reconnue, la section **Aperçu** se met à jour avec une URL de marque substitutive. Braze estime la longueur du message après raccourcissement, mais un avertissement vous invite à sélectionner un utilisateur test et à enregistrer le message en tant que brouillon pour obtenir une estimation plus précise.

![Compositeur de messages avec une URL longue dans le champ « Message » et un lien raccourci généré dans l'aperçu.]({% image_buster /assets/img/link_shortening/shortening3.png %}){: width="1552" height="612"}

### Ajout de paramètres UTM {#adding-utm-parameters}

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## Personnalisation Liquid dans les URL {#liquid-personalization-in-urls}

Pour savoir comment construire dynamiquement des URL directement dans le composeur Braze, vous permettant d'ajouter des paramètres UTM dynamiques à vos URL ou d'envoyer des liens uniques aux utilisateurs, consultez [Utiliser la personnalisation Liquid dans les URL]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#use-liquid-personalization-in-urls).

## Tests {#testing}

Avant de lancer votre Campaign ou votre Canvas, il est recommandé de prévisualiser et de tester votre message au préalable. Pour ce faire, accédez à l'onglet **Test** pour prévisualiser et envoyer un SMS ou un message RCS à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) ou à un utilisateur individuel.

Cette prévisualisation se met à jour avec la personnalisation pertinente et l'URL raccourcie. Le nombre de caractères et les [segments facturables]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator) se mettent également à jour pour refléter la personnalisation rendue et l'URL raccourcie.

Assurez-vous d'enregistrer la Campaign ou le Canvas avant d'envoyer un message test afin de recevoir une représentation de l'URL raccourcie envoyée dans votre message. Si la Campaign ou le Canvas n'est pas enregistré avant un envoi test, l'envoi test inclut une URL de marque substitutive.

{% alert important %}
Si un brouillon est créé au sein d'un Canvas actif, une URL raccourcie ne sera pas générée. L'URL raccourcie réelle est générée lorsque le brouillon du Canvas est activé.
{% endalert %}

![Onglet « Test » du message avec des champs pour sélectionner les destinataires du test.]({% image_buster /assets/img/link_shortening/shortening2.png %}){: width="1544" height="1140"}

{% alert note %}
La personnalisation Liquid et les URL raccourcies sont générées dans l'onglet **Test** après la sélection d'un utilisateur. Assurez-vous qu'un utilisateur est sélectionné pour obtenir un décompte de caractères précis.
{% endalert %}

## Suivi des clics {#click-tracking}

Lorsque le raccourcissement de liens est activé, le tableau **Performances SMS/MMS/RCS** inclut une colonne intitulée **Total Clicks** qui affiche le nombre d'événements de clics par variante ainsi que le taux de clics associé. Pour plus de détails sur les indicateurs, consultez [Performances des messages]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting).

![Tableau des indicateurs de performances SMS et MMS.]({% image_buster /assets/img/link_shortening/shortening4.png %}){: width="1586" height="191"}

Les tableaux **Historical Performance** et **Performances SMS/MMS/RCS** incluent également une option pour **Total Clicks** et affichent une série temporelle quotidienne des événements de clics. Les clics sont incrémentés lors de la redirection (par exemple, lorsqu'un utilisateur visite un lien) et peuvent être incrémentés plus d'une fois par utilisateur.

## Recibler les utilisateurs {#retargeting-users}

Pour des conseils sur le reciblage, consultez [Reciblage]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting#filter-by-advanced-tracking-links).

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### Puis-je savoir quels utilisateurs individuels cliquent sur une URL ? {#do-i-know-which-individual-users-are-clicking-on-a-url}

Oui. Vous pouvez recibler les utilisateurs qui ont cliqué sur des URL en utilisant les [filtres de reciblage SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting) ou les événements de clic SMS (`users.messages.sms.ShortLinkClick`) envoyés par Currents.

### Le raccourcissement de liens fonctionne-t-il avec les deep links ou les liens universels ? {#does-link-shortening-work-with-deep-links-or-universal-links}

Le raccourcissement de liens ne fonctionne pas avec les deep links. Vous pouvez toutefois raccourcir des liens universels provenant de fournisseurs tiers tels que Branch or branche ou Appsflyer, mais les utilisateurs risquent de subir une brève redirection ou un effet de « scintillement ». Cela se produit parce que le lien raccourci passe d'abord par le web avant de se résoudre vers le lien universel qui prend en charge l'ouverture de l'application. De plus, Braze n'est pas en mesure de résoudre les problèmes qui peuvent survenir lors du raccourcissement des liens universels, comme la rupture de l'attribution ou des redirections inattendues.

{% alert note %}
Testez l'expérience utilisateur avant d'implémenter le raccourcissement de liens avec des liens universels afin de confirmer qu'il répond à vos attentes.
{% endalert %}

### Les `send_ids` sont-ils associés aux événements de clic SMS ? {#are-send_ids-associated-with-sms-click-events}

Non. Cependant, vous pouvez généralement attribuer des `send_ids` aux événements de clic en utilisant le [générateur de requêtes]({{site.baseurl}}/query_builder) pour interroger les données Currents avec cette requête :

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL;
```