---
nav_title: ワークスペース間でコピー
article_title: ワークスペース間でコピー
page_order: 3
alias: "/copying_to_workspaces/"
page_type: reference
description: "このリファレンス記事では、キャンペーンやキャンバスを異なるワークスペースにコピーする方法の概要を説明します。"
tool:
    - キャンペーン
    - キャンバス
---

# キャンペーンやキャンバスをワークスペース間でコピーする {#copy-campaigns-and-canvases-across-workspaces}

> ワークスペース間でキャンペーンをコピーすると、別のワークスペースにあるキャンペーンのコピーから始めることで、メッセージ作成をすばやく開始できます。このページでは、キャンペーンを異なるワークスペースにコピーする方法と、コピーされるものとされないものについて説明します。

キャンペーンやキャンバスを別のワークスペースにコピーすると、コピーは編集して起動するまで下書きのままになるため、成功したメッセージング戦略を維持し、それを基に構築できます。

{% tabs local %}
{% tab campaigns %}

{% alert important %}
ワークスペース間でのキャンペーンのコピーは一般提供されています。Content Cardsのチャネルサポートは現在利用できません。
{% endalert %}

以下のサポートされているチャネルでワークスペース間でキャンペーンをコピーできます：SMS、アプリ内メッセージ、プッシュ通知、メール、webhook。また、メールテンプレート、フィーチャーフラグ、Content Blocksもコピーできます。サポートされていないチャネルを含むマルチチャネルキャンペーンは、別のワークスペースにコピーできないことに注意してください。

キャンペーンを別のワークスペースにコピーするには：

1. 選択したキャンペーンの横にある<i class="fas fa-cog"></i>歯車アイコンを選択します。
2. **ワークスペースにコピー**を選択します。
3. コピー後、キャンペーンを確認してテストし、すべてのフィールドが正しく機能することを確認します。

{% endtab %}
{% tab canvas %}

{% alert important %}
ワークスペース間でのキャンバスのコピーは一般提供されています。LINE、Content Cards、WhatsAppのチャネルは現在サポートされていません。
{% endalert %}

以下のサポートされているチャネルでワークスペース間でキャンバスをコピーできます：メール、アプリ内メッセージ、プッシュ、webhook、SMS。

キャンバスを別のワークスペースにコピーするには：

1. 選択したキャンバスの横にある<i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;メニューを選択します。
2. **ワークスペースにコピー**を選択します。
3. コピー後、キャンバスを確認してテストし、すべてのフィールドが正しく機能することを確認します。

Audience Syncステップを含むキャンバスをコピーする場合、設定はコピー先のワークスペースにコピーされませんが、ジャーニー内のステップはコピーされます。

{% endtab %}
{% endtabs %}

## ワークスペース間でコピーされるもの {#whats-copied-across-workspaces}

以下は、ワークスペース間でコピーされるものと省略されるものの包括的なリストではないことに注意してください。ベストプラクティスとして、キャンペーンとキャンバスの詳細を確認し、テストしてメッセージが期待どおりに機能することを確認してください。

### 詳細 {#details}

{% tabs local %}
{% tab campaigns %}

| コピーされる | 省略される |
|---|---|
| 説明 | テリトリー |
| タイプ | タグ |
| アクション（ネスト） | セグメントとフィルター |
| コンバージョン動作（ネスト） | [承認]({{site.baseurl}}/user_guide/messaging/governance/approvals/) |
| サイレント時間の設定 | トリガースケジュール |
| フリークエンシーキャップの設定 | キャンペーンサマリー |
| 受信者のサブスクリプション状態 |  |
| 繰り返しスケジュール |  |
| トランザクション |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Details" }

{% endtab %}
{% tab canvas %}

| コピーされる | 省略される |
|---|---|
| 説明 | テリトリー |
| タイプ | タグ |
| アクション（ネスト） | セグメントとフィルター |
| コンバージョン動作（ネスト） | [承認]({{site.baseurl}}/user_guide/messaging/governance/approvals/) |
| サイレント時間の設定 | トリガースケジュール |
| フリークエンシーキャップの設定 | キャンバスサマリー |
| 受信者のサブスクリプション状態 |  |
| 繰り返しスケジュール | 離脱条件 |
| トランザクション |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Details" }

キャンバスステップのフィルター条件（例：[条件分岐]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/)ステップ）はコピー先のワークスペースにコピーされません。コピー後にこれらのフィルターを再設定してください。

{% endtab %}
{% endtabs %}

### コンバージョン動作 {#conversion-behaviors}

{% tabs local %}
{% tab campaigns %}

| コピーされる | 省略される |
|---|---|
| タイプ動作 | ワークスペースID |
| キャンペーンインタラクション |  キャンペーン ID |
| カスタムイベント名 |  |
| 製品名 |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conversion behaviors" }

{% endtab %}
{% tab canvas %}

| コピーされる | 省略される |
|---|---|
| タイプ動作 | ワークスペースID |
| キャンバスインタラクション |  キャンバス ID |
| カスタムイベント名 |  |
| 製品名 |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conversion behaviors" }

{% endtab %}
{% endtabs %}

### アクション {#actions}

{% tabs local %}
{% tab campaigns %}

| コピーされる | 省略される |
|---|---|
| タイプ動作 | ワークスペースID |
| キャンペーンインタラクション |  キャンペーン ID |
| カスタムイベント名 |  |
| 製品名 |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Actions" }

{% endtab %}
{% tab canvas %}

| コピーされる | 省略される |
|---|---|
| タイプ動作 | ワークスペースID |
| キャンバスインタラクション |  キャンバス ID |
| カスタムイベント名 |  |
| 製品名 |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Actions" }

{% endtab %}
{% endtabs %}

### メッセージバリエーション {#message-variations}

{% tabs local %}
{% tab campaigns %}

| コピーされる | 省略される |
|---|---|
| 送信割合 | API ID |
| タイプ |  シードグループID |
|  |  リンクテンプレートID |
|  |  内部ユーザーグループID |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Message variations" }

{% endtab %}
{% tab canvas %}

| コピーされる | 省略される |
|---|---|
| 送信割合 | API ID |
| タイプ |  シードグループID |
|  |  リンクテンプレートID |
|  |  内部ユーザーグループID |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Message variations" }

{% endtab %}
{% endtabs %}


### メールメッセージバリエーション {#email-message-variation}

{% tabs local %}
{% tab campaigns %}

| コピーされる | 省略される |
|---|---|
| メール本文 | 送信元アドレス |
| メッセージエクストラ |  返信先 |
| タイトル |  BCC |
| 件名 |  リンクテンプレート |
|  |  リンクエイリアス |
|  | 翻訳 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email message variation" }

{% endtab %}
{% tab canvas %}

| コピーされる | 省略される |
|---|---|
| メール本文 | 送信元アドレス |
| メッセージエクストラ |  返信先 |
| タイトル |  BCC |
| 件名 |  リンクテンプレート |
|  |  リンクエイリアス |
|  | 翻訳 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email message variation" }

{% endtab %}
{% endtabs %}

### メール本文 {#email-body}

{% tabs local %}
{% tab campaigns %}

| コピーされる | 省略される |
|---|---|
| プレーンテキスト | リンクエイリアス |
| HTMLおよびドラッグ＆ドロップコンテンツ | 翻訳 |
| プリヘッダー |  |
| インラインCSS |  |
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email body" }

{% endtab %}
{% tab canvas %}

| コピーされる | 省略される |
|---|---|
| プレーンテキスト | リンクエイリアス |
| HTMLおよびドラッグ＆ドロップコンテンツ | 翻訳 |
| プリヘッダー |  |
| インラインCSS |  |
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email body" }

{% endtab %}
{% endtabs %}

### メールテンプレート {#email-templates}

{% tabs local %}
{% tab campaigns %}

| コピーされる | 省略される |
|---|---|
| メール本文 | API ID |
| 説明 | 画像ID |
| 件名 | テリトリー |
| ヘッダー | タグ |
| | 翻訳 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email templates" }

{% endtab %}
{% tab canvas %}

| コピーされる | 省略される |
|---|---|
| メール本文 | API ID |
| 説明 | 画像ID |
| 件名 | テリトリー |
| ヘッダー | タグ |
| | 翻訳 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email templates" }

{% endtab %}
{% endtabs %}

### Content Blocks

{% tabs local %}
{% tab campaigns %}

| コピーされる | 省略される |
|---|---|
| 名前 | リンクエイリアス |
| 説明 | APIキー |
| コンテンツ | テリトリー |
| HTMLおよびドラッグ＆ドロップコンテンツ | タグ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Blocks" }

{% endtab %}
{% tab canvas %}

| コピーされる | 省略される |
|---|---|
| 名前 | リンクエイリアス |
| 説明 | APIキー |
| コンテンツ | テリトリー |
| HTMLおよびドラッグ＆ドロップコンテンツ | タグ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Blocks" }

{% endtab %}
{% endtabs %}

### SMSメッセージバリエーション {#sms-message-variation}

{% tabs local %}
{% tab campaigns %}

| コピーされる | 省略される |
|---|---|
| 本文 | メッセージングサービス |
| リンク短縮 | VCFメディアアイテム |
| クリックトラッキング |  |
| メディアアイテム |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMS message variation" }

{% endtab %}
{% tab canvas %}

| コピーされる | 省略される |
|---|---|
| 本文 | メッセージングサービス |
| リンク短縮 | VCFメディアアイテム |
| クリックトラッキング |  |
| メディアアイテム |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMS message variation" }

{% endtab %}
{% endtabs %}

## Liquidを含むメッセージのコピー {#copying-messages-that-contain-liquid}

メッセージ本文内のLiquid参照はコピー先のワークスペースにコピーされますが、参照が期待どおりに機能しない場合があります。つまり、ワークスペースAのキャンバスをワークスペースBにコピーした場合、ワークスペースBはLiquid参照を含むワークスペースAの詳細を参照できません。例えば、トリガーアクション、オーディエンスフィルター、[条件分岐]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/)のフィルター条件などのフィールドはコピーされません。

ワークスペース間でキャンペーンやキャンバスをコピーする際は、依存関係のある以下のLiquid参照に注意してください：

- カタログアイテムタグ
- コネクテッドコンテンツタグ
- Content Blocks
- カスタム属性
- ユーザー設定センター
- 製品のおすすめ
- サブスクリプション状態タグ
- バウチャーおよびプロモーションタグ

## フィーチャーフラグを含むメッセージのコピー {#copying-messages-with-feature-flags}

フィーチャーフラグキャンペーンやフィーチャーフラグステップを含むキャンバスをワークスペース間でコピーするには、コピー先のワークスペースに、元のキャンペーンで参照されているフィーチャーフラグまたは元のキャンバスで参照されているフィーチャーフラグステップと一致するIDを持つ[フィーチャーフラグ実験]({{site.baseurl}}/developer_guide/feature_flags/experiments/)が設定されていることを確認してください。

コピー先のワークスペースに存在しないフィーチャーフラグIDを持つフィーチャーフラグステップを含むキャンペーンやキャンバスをコピーした場合、フィーチャーフラグステップはコピーされますが、その内容はコピーされません。

## Content Blocksを含むメッセージのコピー {#copying-messages-with-content-blocks}

ワークスペース間でキャンペーンをコピーする場合、Content Blocksはコピーされません。ただし、同じ名前のブロックがコピー先のワークスペースに存在する場合、そのContent Blockを参照できます。または、キャンペーンを起動する際のエラーを回避するために、コピー先のワークスペースでContent Block（またはこれらのLiquid参照）を作成できます。

Content Blockを参照するキャンバスの場合、Content Blockを最初にコピー先のワークスペースにコピーする必要があります。