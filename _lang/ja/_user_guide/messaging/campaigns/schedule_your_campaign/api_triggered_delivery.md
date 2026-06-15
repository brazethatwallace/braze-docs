---
nav_title: API トリガー配信
article_title: API トリガー配信
page_order: 2
page_type: reference
description: "このリファレンス記事では、API トリガーキャンペーンのスケジュール設定と構成方法について説明します。"
tool: Campaigns
platform: API

---

# API トリガー配信 {#api-triggered-delivery}

> API トリガーキャンペーン（サーバートリガーキャンペーン）は、より高度なトランザクションユースケースに最適です。Brazeの API トリガーキャンペーンを使用すると、マーケターはキャンペーンのコピー、多変量テスト、再適格性ルールをBrazeダッシュボード内で管理しながら、自社のサーバーやシステムからコンテンツの配信をトリガーできます。メッセージをトリガーする API リクエストには、リアルタイムでメッセージにテンプレート化される追加データを含めることもできます。

## API トリガーキャンペーンの設定 {#setting-up-an-api-triggered-campaign}

API トリガーキャンペーンの設定にはいくつかのステップが必要です。まず、マルチチャネルまたは単一チャネルのキャンペーン（多変量テスト付き）を新規作成します。

{% alert note %}
API トリガーキャンペーンは [API キャンペーン]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns)とは異なります。
{% endalert %}

次に、スケジュールされた通知の場合と同様にコピーと通知を設定し、**API-Triggered Delivery** を選択します。サーバーからこれらのキャンペーンをトリガーする方法の詳細については、[API トリガーキャンペーンの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)の記事をご覧ください。

![]({% image_buster /assets/img_archive/api_triggered_campaign_delivery.png %})

## API リクエストに含まれるテンプレートコンテンツの使用 {#using-the-templated-content-included-with-an-api-request}

メッセージのトリガーに加えて、API リクエストにコンテンツを含めて `trigger_properties` オブジェクト内でメッセージにテンプレート化することもできます。このコンテンツはメッセージ本文で参照できます。`trigger_properties` とメッセージコピーでは、Liquid タグごとに中括弧を2つずつ使用してください。例: {% raw %}`{{api_trigger_properties.${your_property}}}`{% endraw %}。`{` や `}` の余分な追加は、[API トリガーのパーソナライゼーション失敗]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/faq/#why-is-my-api-triggered-liquid-failing-in-braze)の一般的な原因です。

追加のコンテキストについては、以下のソーシャル通知の例をご覧ください。

![前述のトリガープロパティがメッセージに含まれ、ユーザー名が自動入力された後に「liked your photo! Click here to see what they've been up to.」というテキストが続きます。]({% image_buster /assets/img_archive/api_triggered_photo_social_example_1.png %}){: style="max-width:70%;"}

## API トリガーキャンペーンの再適格性 {#re-eligibility-with-api-triggered-campaigns}

ユーザーが API トリガーキャンペーンを受信する回数は、再適格性設定を使用して制限できます。これにより、API トリガーが何回発火されたかに関係なく、ユーザーはキャンペーンを1回のみ、または指定された時間枠内で1回のみ受信します。

たとえば、API トリガーキャンペーンを使用して、ユーザーが最近閲覧したアイテムに関するキャンペーンを送信するとします。この場合、各アイテムに対して API トリガーを発火しながらも、閲覧したアイテム数に関係なく、1日に最大1通のメッセージを送信するようにキャンペーンを制限できます。一方、API トリガーキャンペーンがトランザクション目的の場合は、遅延をゼロ分に設定して、ユーザーがトランザクションを行うたびにキャンペーンを受信できるようにする必要があります。

![]({% image_buster /assets/img_archive/api_triggered_reeligible.png %})