---
nav_title: ユーザーのリターゲティング
article_title: ユーザーのリターゲティング
description: "ランディングページのフォームを送信したユーザーをリターゲティングする方法を説明します。"
page_order: 3
---

# ランディングページによるユーザーのリターゲティング {#retarget-users-through-a-landing-page}

> ランディングページのフォームを送信したユーザーを、専用のセグメントを作成するか、フォーム送信時にメッセージをトリガーすることでリターゲティングする方法を説明します。

## 前提条件 {#prerequisites}

始める前に、[ランディングページ]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)を作成してください。

## ユーザーのリターゲティング {#retargeting-users}

Brazeは、ユーザーがランディングページフォームを送信すると自動的に追跡します。フォームの送信総数は[ランディングページ分析]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#view-analytics)で確認できます。ユーザー固有のリターゲティングについては、以下のいずれかの方法でランディングページフォームを通じてユーザーをリターゲティングできます。

{% tabs local %}
{% tab セグメントを使用する %}

新しいセグメントを作成して、ランディングページフォームを送信したユーザーまたは送信していないユーザーを自動的に識別します。[セグメントを作成]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)する際、「リターゲティング」グループで**Submitted Form on Landing Page**を選択します。

![フィルターグループが「Submitted Form on Landing Page」に設定されたセグメント作成画面。]({% image_buster /assets/img/landing_pages/segmentation_selected.png %})

ここから、ランディングページのフォームを送信したかどうかに基づいてユーザーをセグメント化できます。
{% endtab %}

{% tab メッセージトリガーを使用する %}

メッセージトリガーを設定して、フォーム送信後にユーザーに自動的にメッセージを送信したり、キャンバスに登録したりできます。[キャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns)または[キャンバス]({{site.baseurl}}/user_guide/messaging/canvas)の配信オプションを選択する際、**Action Based Delivery**を選択し、次に**Submitted a Landing Page form**を選択します。

このランディングページフォームからフォームを送信したすべてのユーザーは、選択したメッセージングチャネルを通じてメッセージが送信されるか、選択したキャンバスに登録されます。

![メッセージングにおけるランディングページのトリガーアクション。]({% image_buster /assets/img/landing_pages/trigger.png %})

{% alert note %}
ランディングページのアクションベース配信オプションは、アプリ内メッセージでは利用できません。ランディングページでフォームを送信したユーザーをアプリ内メッセージでターゲティングするには、キャンペーンの**Targeting Options**で**Submitted Form on Landing Page**フィルターを選択してください。
{% endalert %}

{% endtab %}
{% endtabs %}

### マルチステップフォーム {#multi-step-form}

[マルチステップフォーム]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms)の場合、両方のリターゲティング方法は**Submitted a Landing Page form**イベントに依存しており、このイベントはユーザーがすべてのステップを完了した後にのみ記録されます。一部のステップのみを送信したユーザーのデータはプロファイルに保存されますが、フォーム全体を完了するまでどちらの方法にも含まれません。詳細については、[部分的に完了したフォームからデータを追跡する]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms#track-data-from-partially-completed-forms)を参照してください。