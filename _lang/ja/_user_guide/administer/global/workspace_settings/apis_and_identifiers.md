---
nav_title: APIと識別子
article_title: APIと識別子
page_order: 0
page_type: reference
description: "この記事では、ワークスペースのAPI識別子を表示する「APIと識別子」ページについて説明します。"
---

# APIキー {#api-keys}

> **APIと識別子**ページは、すべてのREST APIキーを一元管理するためのハブです。ここでは、各ワークスペースのAPIキーセットとアプリ識別子にアクセスできます。

**APIと識別子**ページは**設定**の下にあります。

## APIキー

このセクションでは、ワークスペースのREST APIキーを提供します。REST APIキーは、ワークスペースのデータにアクセスするための一意の識別子です。Braze APIへのすべてのリクエストにはREST APIキーが必要です。APIキーの作成と使用の詳細については、[REST APIキーの概要]({{site.baseurl}}/api/basics)を参照してください。

### API IP許可リスト {#api-ip-allowlisting}

セキュリティを強化するために、特定のREST APIキーに対してREST APIリクエストを行うことが許可されるIPアドレスとサブネットのリストを指定できます。これは許可リスト（ホワイトリスト）と呼ばれます。特定のIPアドレスまたはサブネットを許可するには、新しいREST APIキーの作成時に **Whitelist IPs** セクションに追加します。

![新しいAPIキー作成時のAPI IPホワイトリストセクション]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

指定しない場合、任意のIPアドレスからリクエストを送信できます。

{% alert tip %}
BrazeからBrazeへのWebhookを作成する際に許可リストを使用していますか？[ホワイトリストに登録するIP]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting)のリストを確認してください。
{% endalert %}

### API使用状況アラート {#api-usage-alerts}

API使用状況アラートを設定して、主要なAPIアクティビティを監視し、問題を早期に発見できます。これらのアラートは、予期しないトラフィックパターンが体験に影響を与える前に検出するのに役立ちます。

2種類のAPIアクティビティを追跡できます。

- **REST APIエンドポイント：** メッセージの送信、キャンペーンの作成、データのエクスポートなどのアクション。
- **SDK APIリクエスト：** アプリ内メッセージのトリガーやユーザープロファイルの同期など、顧客体験に関連するイベント。*この機能は、月間アクティブユーザー（CY 24–25）を購入している場合に利用できます。*

追跡対象を選択したら、アラート条件を定義できます。たとえば、1時間以内にエラーレスポンスが20%増加した場合に通知を受け取ることができます。設定に応じて、メール、Webhook、またはその両方で通知を受け取ります。開始するには、[API使用状況アラート]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts)を参照してください。

## アプリ識別子 {#app-identifiers}

このセクションには、Braze APIへのリクエストで特定のアプリを参照するために使用される識別子のリストが含まれています。アプリケーション識別子の詳細については、[アプリ識別子APIキー]({{site.baseurl}}/api/identifier_types)を参照してください。

## その他の識別子 {#other-identifiers}

APIと連携するために、Braze外部APIからアクセスしたいセグメント、キャンペーン、Content Cardsなどに関連する識別子を検索できます。すべてのメッセージは[UTF-8](https://en.wikipedia.org/wiki/UTF-8)エンコーディングに従う必要があります。いずれかを選択すると、ドロップダウンメニューの下に識別子が表示されます。

詳しくは、[API識別子の種類]({{site.baseurl}}/api/identifier_types)を参照してください。