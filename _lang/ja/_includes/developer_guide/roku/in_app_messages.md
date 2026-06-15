{% multi_lang_include developer_guide/prerequisites/roku.md %} また、アプリ内メッセージは、最低限サポートされているSDKバージョンを実行しているRokuデバイスにのみ送信されます。

{% sdk_min_versions roku:0.1.2 %}

## メッセージタイプ {#message-types}

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## アプリ内メッセージを有効にする {#enabling-in-app-messages}

### ステップ 1: オブザーバーを追加する {#step-1-add-an-observer}

アプリ内メッセージを処理するために、`BrazeTask.BrazeInAppMessage`にオブザーバーを追加できます。

```brightscript
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

### ステップ 2: トリガーメッセージにアクセスする {#step-2-access-triggered-messages}

次に、ハンドラ内で、キャンペーンによってトリガーされた最も優先度の高いアプリ内メッセージにアクセスできます。

`````````brightscript
sub onInAppMessageReceived()
  in_app_message = m.BrazeTask.BrazeInAppMessage
  ...
end sub
```

## メッセージフィールド {#message-fields}

### ハンドリング {#handling}

以下は、アプリ内メッセージを処理するために必要なフィールドの一覧です。

| フィールド | 説明 |
| ------ | ----------- |
| `buttons` | ボタンのリスト（空のリストの場合もあります）。 |
| `click_action` | `"URI"`または`"NONE"`。このフィールドを使用して、アプリ内メッセージがクリック時にURIリンクを開くか、メッセージを閉じるかを指定します。ボタンがない場合、アプリ内メッセージが表示されているときにユーザーが「OK」をクリックすると、この動作が発生します。 |
| `dismiss_type` | `"AUTO_DISMISS"`または`"SWIPE"`。このフィールドを使用して、アプリ内メッセージが自動的に閉じられるか、スワイプで閉じる必要があるかを指定します。 |
| `display_delay` | アプリ内メッセージを表示するまでの待機時間（秒）。 |
| `duration` | `dismiss_type`が`"AUTO_DISMISS"`に設定されている場合、メッセージが表示される時間（ミリ秒）。 |
| `extras` | キーと値のペア。 |
| `header` | ヘッダーテキスト。 |
| `id` | インプレッションやクリックを記録するために使用されるID。 |
| `image_url` | アプリ内メッセージの画像URL。 |
| `message` | メッセージ本文テキスト。 |
| `uri` | `click_action`に基づいてユーザーが遷移するURI。このフィールドは`click_action`が`"URI"`のときに含める必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Handling" }

{% alert important %}
ボタンを含むアプリ内メッセージの場合、ボタンテキストを追加する前にクリックアクションが追加されると、メッセージの`click_action`も最終ペイロードに含まれます。
{% endalert %}

### スタイリング {#styling}

ダッシュボードから使用できるさまざまなスタイル指定フィールドもあります。

| フィールド | 説明 |
| ------ | ----------- |
| `bg_color` | 背景色。 |
| `close_button_color` | 閉じるボタンの色。 |
| `frame_color` | バックグラウンド画面オーバーレイの色。 |
| `header_text_color` | ヘッダーテキストの色。 |
| `message_text_color` | メッセージテキストの色。 |
| `text_align` | 「START」、「CENTER」、または「END」。選択したテキストの配置。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Styling" }

また、アプリ内メッセージを実装し、Rokuアプリケーション内で標準パレットを使用してスタイルを設定することもできます。

### ボタン {#buttons}

| フィールド | 説明 |
| ------ | ----------- |
| `click_action` | `"URI"`または`"NONE"`。このフィールドを使用して、アプリ内メッセージがクリック時にURIリンクを開くか、メッセージを閉じるかを指定します。 |
| `id` | ボタン自体のID値。 |
| `text` | ボタンに表示するテキスト。 |
| `uri` | `click_action`に基づいてユーザーが遷移するURI。このフィールドは`click_action`が`"URI"`のときに含める必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Buttons" }