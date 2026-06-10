---
nav_title: メッセージ
article_title: メッセージ
alias: "/message_step/"
page_order: 11
page_type: reference
description: "このリファレンス記事では、メッセージステップを使用してスタンドアロンメッセージを作成する方法について説明します。"
tool: Canvas

---

# メッセージ {#message}

> メッセージステップを使用すると、Canvas内の任意の場所にスタンドアロンメッセージを追加できます。

![プッシュチャネルを使用した「Lunch promo」という名前のメッセージステップ。]({% image_buster /assets/img/canvas_components/message_step1.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

## メッセージの作成 {#create-a-message}

メッセージコンポーネントを作成するには、まずCanvasにステップを追加します。サイドバーからコンポーネントをドラッグ＆ドロップするか、ステップの下部にある<i class="fas fa-plus-circle"></i>プラスボタンを選択して**メッセージ**を選択します。

### ステップ 1: メッセージングチャネルの選択 {#step-1-select-your-messaging-channel}

以下のメッセージングチャネルから選択できます。
- バナー
- Content Cards
- メール
- LINE
- プッシュ通知
- SMS/MMS/RCS
- アプリ内メッセージ
- Webhook
- WhatsApp

![メッセージステップで選択可能なメッセージングチャネルのリスト。]({% image_buster /assets/img/canvas_components/message_step2.png %})

### ステップ 2: 配信設定の編集 {#step-2-edit-delivery-settings}

次に、インテリジェントタイミング、サイレント時間の上書き、配信バリデーションの設定を編集できます。

#### インテリジェントタイミング {#intelligent-timing}

ユーザーのプロファイルに最適な時間を計算するための十分なデータがない場合のフォールバックオプションとともに、[インテリジェントタイミング]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/)を有効にできます。ユーザーがメッセージステップに入ってから実際にメッセージが送信されるまでの遅延に対する追加チェックとして、インテリジェントタイミングと[レート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#rate-limiting-and-frequency-capping/)を有効にすることをお勧めします。

**配信設定**タブで**インテリジェントタイミングを使用**を選択します。ここでは、最も人気のある時間または特定のフォールバック時間のいずれかを選択できます。サイレント時間が有効になっている場合、メッセージステップではこの設定を上書きすることもできます。

![メッセージコンポーネント設定の配信設定タブ。サイレント時間が有効になっており、インテリジェントタイミングを使用のチェックボックスが選択されて、最適な時間にメッセージを配信します。]({% image_buster /assets/img/canvas_components/message_step4.png %}){: style="max-width:90%;"}

#### 配信バリデーション {#delivery-validations}

配信バリデーションは、メッセージ送信時にオーディエンスが配信基準を満たしていることを確認するための追加チェックを提供します。この設定は、サイレント時間、インテリジェントタイミング、またはレート制限が有効になっている場合に推奨されます。**メッセージ送信時にオーディエンスを検証**を選択し、Segmentまたは追加のフィルターを追加します。ユーザーがバリデーションを満たさない場合、Canvasを終了するか次のステップに進むかを選択します。

配信バリデーションは、送信時にユーザープロファイルの基準を評価します。アプリ関連のフィルターは、ユーザーが最近特定のアプリを使用したか、またはこれまでに使用したことがあるかをチェックしますが、現在のセッションでユーザーがどのアプリを使用しているかは確認しません。

ワークスペースに複数のアプリがあり、メッセージステップが特定のアプリをターゲットにする必要がある場合は、代わりに以下のいずれかのアプローチを使用してください。

- メッセージの作成時に、**モバイルアプリ**や**Webブラウザー**などの[配信プラットフォームを指定]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/#step-2-specify-delivery-platforms)します。
- Liquidを使用して、送信時にターゲットデバイスまたはアプリを確認します。
  - {% raw %}`{{targeted_device.${platform}}}`{% endraw %}は、ユーザーの現在のセッションのプラットフォームを評価します。詳細については、[ターゲットデバイス情報]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/#targeted-device-information)を参照してください。
  - {% raw %}`{{app.${api_id}}}`{% endraw %}は、メッセージをリクエストしているアプリを評価します。このタグを`abort_message()`と組み合わせて、誤ったアプリへの送信を防止します。詳細については、[ターゲットアプリ情報]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/#targeted-app-information)を参照してください。

![配信バリデーションが有効になっており、メッセージ送信時にオーディエンスを検証します。配信バリデーションの進行動作は、配信バリデーションが満たされない場合にユーザーをCanvasの次のステップに進めるように設定されています。]({% image_buster /assets/img/canvas_components/message_step5.png %}){: style="max-width:90%;"}

## ユーザーの進行方法 {#how-users-advance}

メッセージステップに入ったすべてのユーザーは、以下のいずれかの条件が満たされると次のステップに進みます。

- いずれかのメッセージが送信された
- メッセージがフリークエンシーキャップにより送信されなかった
- メッセージが中止された
- ユーザーがチャネルで到達不可能なため、メッセージが送信されなかった
- ユーザーが**配信バリデーション**の基準を満たさなかった

{% raw %}
アクションベースのCanvasが受信SMSメッセージによってトリガーされた場合、最初のステップ（メッセージステップ）またはアクションパスステップの下にネストされたメッセージステップでSMSプロパティを参照できます。例えば、メッセージステップでは`{{sms.${inbound_message_body}}}`や`{{sms.${inbound_media_urls}}}`を使用できます。
{% endraw %}

## コンテキストプロパティの参照 {#reference-context-properties}

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

エントリプロパティは、Canvas作成の**エントリスケジュール**ステップで設定され、ユーザーをCanvasに入れるトリガーを示します。これらのプロパティは、APIトリガーのCanvasesにおけるエントリペイロードのプロパティにもアクセスできます。`context`オブジェクトの最大サイズ制限は50 KBです。

エントリプロパティは、任意のメッセージステップのLiquidで使用できます。これらのエントリプロパティを参照する場合は、次のLiquidを使用します: {% raw %}``{context.${property_name}}``{% endraw %}。イベントは、この方法で使用するにはカスタムイベントまたは購入イベントである必要があります。

{% alert note %}
アプリ内メッセージチャネルの場合、`context`はCanvasでのみ参照できます。
{% endalert %}

これらのエントリプロパティを参照する場合は、次のLiquidを使用します: {% raw %}``context.${property_name}``{% endraw %}。イベントは、この方法で使用するにはカスタムイベントまたは購入イベントである必要があります。

{% raw %}
例えば、次のリクエストを考えてみましょう: `"context" : {"product_name" : "shoes", "product_price" : 79.99}`。Liquid `{{context.${product_name}}}` を使用して、メッセージに「shoes」という単語を追加できます。
{% endraw %}

また、[永続的なエントリプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties/)を任意のメッセージステップで活用して、Canvasワークフロー全体でパーソナライズされたステップにユーザーを誘導することもできます。

### イベントプロパティ {#event-properties}

イベントプロパティとは、カスタムイベントおよび購入イベントに設定するプロパティのことです。これらのイベントプロパティは、アクションベースの配信を使用するCampaignsやCanvasesで使用できます。

Canvasでは、カスタムイベントおよび購入イベントのプロパティは、[アクションパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths/)ステップに続く任意のメッセージステップのLiquidで使用できます。例えば、`event_properties`を参照する場合は、次のLiquidスニペットを使用します: {% raw %}``{{event_properties.${property_name}}}``{% endraw %}

{% alert important %}
`event_properties`はアクションパスステップなしでは単独で使用できません。
{% endalert %}

アクションパスに続く最初のメッセージステップでは、そのアクションパスで参照されているイベントに関連する`event_properties`を使用できます。このアクションパスステップとメッセージステップの間に他のステップ（別のアクションパスやメッセージステップ以外）を配置することができます。`event_properties`にアクセスできるのは、メッセージステップがアクションパスステップのその他のユーザー以外のパスに遡れる場合のみです。

{% alert important %}
先頭のメッセージステップでは`event_properties`を使用できません。代わりに、`context`を使用するか、`event_properties`を含むメッセージステップの前に対応するイベントを持つアクションパスステップを追加する必要があります。
{% endalert %}

{% details 元のCanvasエディターの場合はこちらを展開 %}

元のエディターを使用してCanvasesを作成または複製することはできなくなりました。このセクションは参照用としてのみ提供されています。

- `event_properties`はスケジュールされたフルステップでは使用できません。ただし、アクションベースのCanvasの最初のフルステップでは、そのフルステップがスケジュールされている場合でも`event_properties`を使用できます。
- `context`はCanvasの最初のフルステップでのみ参照できます。
- アプリ内メッセージチャネルの場合、以前の早期アクセスの一部として永続的なエントリプロパティが有効になっている場合、元のCanvasエディターで`context`を参照できます。

{% enddetails %}

## 分析 {#analytics}

メッセージコンポーネントの指標の定義については、以下の表を参照してください。

| 指標 | 説明 |
| --- | --- |
| *エントリ* | ステップに入った回数です。Canvasに再エントリ資格があり、ユーザーがメッセージステップに2回入った場合、2つのエントリが記録されます。 |
| *次のステップに進んだ* | Canvasの次のステップに進んだエントリの数です。 |
| *送信数* | ステップが送信したメッセージの合計数です。Canvasに再エントリ資格があり、ユーザーがメッセージステップに2回入った場合、2つのエントリが記録されます。 |
| *ユニーク受信者* | このステップからメッセージを受信したユーザーの数です。 |
| *1次コンバージョンイベント* | Braze Campaignから受信したメッセージを操作または閲覧した後に、定義されたイベントが発生した回数です。このイベントはCampaign作成時に定義します。 |
| *収益* | 設定された1次コンバージョン期間内のCampaign受信者からの合計収益（ドル）です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }