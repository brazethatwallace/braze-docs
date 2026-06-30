---
nav_title: Linkverkürzung
article_title: Linkverkürzung
page_order: 1
description: "Dieser Referenzartikel beschreibt, wie Sie die Linkverkürzung in Ihren SMS-Nachrichten aktivieren, und beantwortet einige häufig gestellte Fragen."
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
---

# Linkverkürzung {#link-shortening}

> Diese Seite beschreibt, wie Sie die Linkverkürzung in Ihren SMS- und RCS-Nachrichten aktivieren, verkürzte Links testen, Ihre angepasste Domain in verkürzten Links verwenden und mehr.

{% alert important %}
Braze führt schrittweise die [einheitliche Linkverkürzung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening?sdktab=unified) ein, die alle verkürzten SMS- und RCS-Links in ein einziges personalisiertes Linkformat zusammenführt (zum Beispiel `brz.ai/abcdefgh`).
{% endalert %}

{% sdktabs %}
{% sdktab Legacy %}

{% multi_lang_include channels/sms/legacy_link_shortening.md %}

{% endsdktab %}
{% sdktab Unified %}

{% multi_lang_include channels/sms/unified_link_shortening.md %}

{% endsdktab %}
{% endsdktabs %}