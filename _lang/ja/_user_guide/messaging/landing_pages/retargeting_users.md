---
nav_title: ユーザーのリターゲティング
article_title: ユーザーのリターゲティング
description: "ランディングページのフォームを送信したユーザーをリターゲティングする方法を説明します。"
page_order: 3
---

# ランディングページによるユーザーのリターゲティング {#retarget-users-through-a-landing-page}

> ランディングページのフォームを送信したユーザーを、専用のセグメントを作成するか、フォーム送信時にメッセージをトリガーすることでリターゲティングする方法を説明します。

## 前提条件 {#prerequisites}

始める前に、[ランディングページ]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)を作成する必要があります。

## ユーザーのリターゲティング {#retargeting-users}

Brazeは、ユーザーがランディングページのフォームを送信すると自動的に追跡します。フォームの送信総数は[ランディングページの分析]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#viewing-analytics)で確認できます。ただし、ユーザー固有のリターゲティングを行うには、以下のいずれかの方法でランディングページのフォームを通じてユーザーをリターゲティングする必要があります。

- **セグメントを使用する:** 新しいセグメントを作成して、ランディングページのフォームを送信したユーザーまたは送信していないユーザーを自動的に識別できます。
- **メッセージトリガーを使用する:** メッセージトリガーを設定して、フォーム送信後にユーザーに自動的にメッセージを送信したり、キャンバスに登録したりできます。

{% tabs local %}
{% tab セグメントを使用する %}
[セグメントを作成]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)する際、「リターゲティング」グループで**Submitted form on Landing Page**を選択します。

![フィルターグループが「Submitted Form on Landing Page」に選択されたセグメント作成画面。]({% image_buster /assets/img/landing_pages/segmentation_selected.png %})

ここから、ランディングページのフォームを送信したかどうかに基づいてユーザーをセグメンテーションできます。
{% endtab %}

{% tab メッセージトリガーを使用する %}
[キャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns)または[キャンバス]({{site.baseurl}}/user_guide/messaging/canvas)の配信オプションを選択する際、**Action Based Delivery**を選択し、次に**Submitted Landing Page form**を選択します。

このランディングページのフォームを通じてフォームを送信したすべてのユーザーは、選択したメッセージングチャネルでメッセージを受信するか、選択したキャンバスに登録されます。

![メッセージングにおけるランディングページのトリガーアクション。]({% image_buster /assets/img/landing_pages/trigger.png %})

{% alert note %}
ランディングページのアクションベースの配信オプションは、アプリ内メッセージでは利用できません。ランディングページでフォームを送信したユーザーをアプリ内メッセージでターゲットするには、キャンペーンの**ターゲティングオプション**で**Submitted Form on Landing Page**フィルターを選択してください。
{% endalert %}

{% endtab %}
{% endtabs %}