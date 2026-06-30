---
nav_title: ディープリンク
article_title: Content Cardsのディープリンク
page_order: 4
description: "Braze SDKを使用して、Content Cards内でディープリンクを行う方法について説明します。"
channel:
  - content cards
platform:
  - Android
  - Swift
  - Web
  - FireOS
---

# Content Cardsのディープリンク {#deep-linking-in-content-cards}

> Braze SDKを使用して、Content Cards内でディープリンクを行う方法について説明します。ディープリンクの詳細については、[ディープリンクとは]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#what-is-deep-linking)を参照してください。

{% sdktabs %}
{% sdktab web %}
現時点では、Web Braze SDKではContent Cardsのディープリンクはサポートされていません。
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/_global/deep_linking.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/deep_linking.md %}
{% endsdktab %}
{% endsdktabs %}