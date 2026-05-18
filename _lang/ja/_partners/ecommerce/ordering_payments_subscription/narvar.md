---
nav_title: Narvar
article_title: Narvar
description: "NarvarとBrazeを統合する方法について説明します。"
alias: /partners/narvar/
page_type: partner
search_tag: Partner
---

# Narvar

> Narvarは、注文の追跡、配送の更新、返品管理を通じて顧客ロイヤルティを高める購入後のプラットフォームです。BrazeとNarvarの統合により、ブランドはNarvarの通知イベントを活用してBrazeから直接メッセージをトリガーし、顧客にタイムリーな更新情報を提供し続けることができます。

## 前提条件 {#prerequisites}

| 必要条件           | 説明                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------|
| Narvarアカウント        | このパートナーシップを活用するには、Narvarアカウントが必要です。                           |
| Braze REST APIキー    | `messages.send` 権限を持つBraze REST APIキー。これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。                                            |
| Braze RESTエンドポイント   | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。これはBrazeインスタンスのURLに応じて異なります。         |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## サポートされている機能 {#supported-features}

| タイプ | サポートされている機能 |
|-------|----------|
| 通知 | - Delivery Anticipation<br>- Carrier Delay<br>- Delivered Standard |
| チャネル | プッシュ通知 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Supported features" }

{% alert note %}
その他の通知タイプやチャネルに興味がある場合は、BrazeおよびNarvarのカスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## 統合の詳細 {#integration-details}

通知イベントごとに、NarvarはBrazeの[`/messaging/send`]({{site.baseurl}}/api/endpoints/messaging/)エンドポイントへリクエストを送信し、オプトインした各消費者にプッシュメッセージを配信します。

Narvarは、各メッセージのプッシュ通知ペイロードを設定する責任を担います。現在、Narvarにはプッシュ通知用のビルトインデザインインターフェイスがないため、Narvarのチームがお客様のチームと協力してペイロードの要件を決定し、定義します。これらのペイロードは、注文データや消費者の詳細などの変数コンテンツプレースホルダーのサポートを含め、お客様独自のシステムを介して送信されるものと同じ範囲でカスタマイズできます。

## BrazeとNarvarの統合を始める {#getting-started-with-the-braze-narvar-integration}

1. **Narvarのカスタマーサクセスマネージャーに連絡し**、統合への関心を伝えてください。
2. ステージングとプロダクション用に**Braze環境を指定します**。
3. BrazeでNarvar用の**APIキーを生成します**。
4. 必要に応じてBrazeで**キャンペーンキーを生成します**。
5. 安全なワンタイムリンクを介して**APIキーとキャンペーンキーをNarvarに提供します**。
6. **プッシュ通知ペイロードの詳細を共有**して設定を完了します。