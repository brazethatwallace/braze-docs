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
Braze déploie progressivement le [raccourcissement de liens unifié]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening/?sdktab=unified), qui consolide tous les liens raccourcis SMS et RCS en un format de lien personnalisé unique (par exemple, `brz.ai/abcdefgh`).
{% endalert %}

{% sdktabs %}
{% sdktab Legacy %}

{% multi_lang_include link_shortening_temp/legacy_link_shortening.md %}

{% endsdktab %}
{% sdktab Unified %}

{% multi_lang_include link_shortening_temp/unified_link_shortening.md %}

{% endsdktab %}
{% endsdktabs %}