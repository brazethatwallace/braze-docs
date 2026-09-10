---
nav_title: APIと識別子
article_title: APIと識別子
page_order: 0
page_type: reference
description: "この記事では、ワークスペースのAPI識別子を表示する「APIと識別子」ページについて説明します。"
---

# APIと識別子 {#apis-and-identifiers}

> **APIと識別子**ページは、すべてのREST APIキーを一元管理するためのハブです。ここでは、各ワークスペースのAPIキーセットとアプリ識別子にアクセスできます。

**APIと識別子**は、**設定** > **セットアップとテスト** > **APIと識別子**から確認できます。

## APIキー {#api-keys}

このセクションでは、ワークスペースのREST APIキーを提供します。REST APIキーは、ワークスペースのデータにアクセスするための一意の識別子です。Braze APIへのすべてのリクエストにはREST APIキーが必要です。APIキーの作成と使用に関する詳細については、[REST APIキーの概要]({{site.baseurl}}/api/basics)を参照してください。

### API IP許可リスト {#api-ip-allowlisting}

セキュリティを強化するために、特定のREST APIキーに対してREST APIリクエストを行うことが許可されるIPアドレスとサブネットのリストを指定できます。これはIP許可リストと呼ばれます。特定のIPアドレスまたはサブネットを許可するには、新しいREST APIキーを作成する際に**Allowlist IPs**セクションに追加してください。

![新しいREST APIキー作成時のAPI IP許可リストセクション]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

何も指定しない場合、任意のIPアドレスからリクエストを送信できます。

{% alert tip %}
Braze間Webhookを作成し、許可リストを使用していますか？[ホワイトリストに登録するIP]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting)のリストをご確認ください。
{% endalert %}

### API使用状況アラート {#api-usage-alerts}

API使用状況アラートを設定して、主要なAPIアクティビティを監視し、問題を早期に発見しましょう。これらのアラートは、予期しないトラフィックパターンが体験に影響を与える前に検出するのに役立ちます。

2種類のAPIアクティビティを追跡できます。

- **REST APIエンドポイント：**メッセージの送信、キャンペーンの作成、データのエクスポートなどのアクション。
- **SDK APIリクエスト：**アプリ内メッセージのトリガーやユーザープロファイルの同期など、顧客体験からのイベント。*この機能は月間アクティブユーザー（CY 24–25）を購入している場合に利用できます。*

追跡する対象を選択したら、アラート条件を定義できます。たとえば、1時間以内にエラーレスポンスが20%増加した場合に通知を受け取ることができます。設定に応じて、メール、Webhook、またはその両方で通知を受け取ります。始めるには、[API使用状況アラート]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts)を参照してください。

## アプリ識別子 {#app-identifiers}

このセクションには、Braze APIへのリクエストで特定のアプリを参照するために使用される識別子のリストが含まれています。アプリケーション識別子の詳細については、[アプリ識別子APIキー]({{site.baseurl}}/api/identifier_types)を参照してください。

## その他の識別子 {#other-identifiers}

Braze の外部APIと連携するために、セグメント、キャンペーン、Content Cardsなど、アクセスしたい項目に関連する識別子を検索できます。すべてのメッセージは [UTF-8](https://en.wikipedia.org/wiki/UTF-8) エンコーディングに準拠している必要があります。いずれかを選択すると、ドロップダウンメニューの下に識別子が表示されます。

詳細については、[API識別子のタイプ]({{site.baseurl}}/api/identifier_types)を参照してください。