---
nav_title: Acortamiento de enlaces
article_title: Acortamiento de enlaces
page_order: 1
description: "Este artículo de referencia explica cómo activar el acortamiento de enlaces en tus mensajes SMS y algunas preguntas frecuentes."
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
---

# Acortamiento de enlaces {#link-shortening}

> Esta página explica cómo activar el acortamiento de enlaces en tus mensajes SMS y RCS, probar enlaces acortados, usar tu dominio personalizado en enlaces acortados y más.

{% alert important %}
Braze está implementando gradualmente el [acortamiento de enlaces unificado]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening?sdktab=unified), que consolida todos los enlaces acortados de SMS y RCS en un único formato de enlace personalizado (por ejemplo, `brz.ai/abcdefgh`).
{% endalert %}

{% sdktabs %}
{% sdktab Legacy %}

{% multi_lang_include channels/sms/legacy_link_shortening.md %}

{% endsdktab %}
{% sdktab Unified %}

{% multi_lang_include channels/sms/unified_link_shortening.md %}

{% endsdktab %}
{% endsdktabs %}