---
nav_title: Encurtamento de links
article_title: Encurtamento de links
page_order: 1
description: "Este artigo de referência aborda como ativar o encurtamento de links nas suas mensagens SMS e algumas perguntas frequentes."
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
---

# Encurtamento de links {#link-shortening}

> Esta página aborda como ativar o encurtamento de links nas suas mensagens SMS e RCS, testar links encurtados, usar seu domínio personalizado em links encurtados e mais.

{% alert important %}
A Braze está implementando gradualmente o [encurtamento de links unificado]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening/?sdktab=unified), que consolida todos os links encurtados de SMS e RCS em um único formato de link personalizado (por exemplo, `brz.ai/abcdefgh`).
{% endalert %}

{% sdktabs %}
{% sdktab Legacy %}

{% multi_lang_include link_shortening_temp/legacy_link_shortening.md %}

{% endsdktab %}
{% sdktab Unified %}

{% multi_lang_include link_shortening_temp/unified_link_shortening.md %}

{% endsdktab %}
{% endsdktabs %}