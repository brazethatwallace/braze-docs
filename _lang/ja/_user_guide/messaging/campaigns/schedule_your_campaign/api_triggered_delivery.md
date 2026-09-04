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

> API トリガーキャンペーン（サーバートリガーキャンペーン）は、より高度なトランザクションユースケースに最適です。BrazeのAPIトリガーキャンペーンを使用すると、マーケターはキャンペーンのコピー、多変量テスト、再適格性ルールをBrazeダッシュボード内で管理しながら、自社のサーバーやシステムからコンテンツの配信をトリガーできます。メッセージをトリガーするAPIリクエストには、リアルタイムでメッセージにテンプレート化される追加データを含めることもできます。

## APIトリガーキャンペーンの設定 {#setting-up-an-api-triggered-campaign}

APIトリガーキャンペーンの設定にはいくつかのステップが必要です。まず、新しいマルチチャネルまたはシングルチャネルのキャンペーン（多変量テスト付き）を作成します。

{% alert note %}
APIトリガーキャンペーンは[APIキャンペーン]({{site.baseurl}}/api/api_campaigns)とは異なります。
{% endalert %}

次に、スケジュールされた通知の場合と同様にコピーと通知を設定し、**API-Triggered Delivery** を選択します。サーバーからこれらのキャンペーンをトリガーする方法の詳細については、[APIトリガーキャンペーンの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)の記事をご確認ください。

![スケジュールされた通知の場合と同様にコピーと通知を設定し、API-Triggered Deliveryを選択します。サーバーからこれらのキャンペーンをトリガーする方法の詳細については、APIトリガーキャンペーンの送信の記事をご確認ください。]({% image_buster /assets/img_archive/api_triggered_campaign_delivery.png %})

## APIトリガーと送信間の遅延を削減する {#reducing-delay-between-your-api-trigger-and-send}

トリガーエンドポイントを呼び出した後、メッセージの送信が想定より長くかかる場合は、トリガー時にユーザープロファイルが準備できているかどうかを確認してください。

デフォルトでは、[`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)で `send_to_existing_only` は `true` に設定されています。Brazeは既存のユーザーにのみ送信し、その呼び出しで新規プロファイルを作成しません。ユーザーの作成や更新と送信を同じリクエストで行うには、`send_to_existing_only` を `false` に設定し、各受信者に `attributes` オブジェクトを含めてください。

メールキャンペーンの場合は、`attributes` 内に `email`（およびその他の必要な配信フィールド）も含めてください。送信をトリガーする時点でプロファイルにメールアドレスがない場合、Brazeはプロファイルデータの到着を待ちながら最大約2時間リトライします。同じ呼び出しに `email` を含めることで、この遅延を回避できます。

リクエストパラメーター、例、リトライ動作の詳細については、[APIトリガーキャンペーンの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#recipient-limits-and-profile-creation)および[受信者オブジェクト]({{site.baseurl}}/api/objects_filters/recipient_object)を参照してください。

{% alert note %}
このガイダンスはAPIトリガーキャンペーン（`/campaigns/trigger/send`）に適用されます。[トランザクションメールエンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message)は異なるリクエスト形式（`recipient`、単数形）を使用し、`send_to_existing_only` をサポートしていません。トランザクション送信でインラインでユーザーを作成するには、代わりに `recipient` オブジェクトに `attributes` を渡してください。
{% endalert %}

## APIリクエストに含まれるテンプレートコンテンツの使用 {#using-the-templated-content-included-with-an-api-request}

メッセージのトリガーに加えて、APIリクエストにコンテンツを含めて、`trigger_properties`オブジェクト内のメッセージにテンプレートとして適用することもできます。このコンテンツはメッセージ本文で参照できます。

`trigger_properties`とメッセージコピーでは、Liquidタグごとに正確に2つの中括弧を使用してください。例: {% raw %}`{{api_trigger_properties.${your_property}}}`.{% endraw %} 余分な`{`や`}`は、[APIトリガーによるパーソナライゼーションの失敗]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/faq#why-is-my-api-triggered-liquid-failing-in-braze)のよくある原因です。

追加のコンテキストについては、以下のソーシャル通知の例を参照してください。

![メッセージに含まれた前述のトリガープロパティがユーザー名を自動入力し、その後に「liked your photo! Click here to see what they've been up to.」というテキストが続いている様子。]({% image_buster /assets/img_archive/api_triggered_photo_social_example_1.png %}){: style="max-width:70%;"}

## APIトリガーキャンペーンの再適格性 {#re-eligibility-with-api-triggered-campaigns}

ユーザーがAPIトリガーキャンペーンを受信する回数は、再適格性の設定を使用して制限できます。これにより、APIトリガーが何回発火されたかに関係なく、ユーザーはキャンペーンを1回のみ、または指定された期間内に1回のみ受信します。

たとえば、APIトリガーキャンペーンを使用して、ユーザーが最近閲覧したアイテムに関するキャンペーンを送信しているとします。この場合、各アイテムに対してAPIトリガーを発火しながらも、ユーザーが閲覧したアイテム数に関係なく、1日に最大1通のメッセージを送信するようにキャンペーンを制限できます。APIトリガーキャンペーンがトランザクション型の場合は、ユーザーがトランザクションを行うたびにキャンペーンを受信できるように、遅延を0分に設定してください。

![APIトリガーキャンペーンの再適格性に関連する設定画面のスクリーンショット。]({% image_buster /assets/img_archive/api_triggered_reeligible.png %})