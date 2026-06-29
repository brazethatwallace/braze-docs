---
nav_title: API キー
article_title: API キー
page_order: 0
page_type: reference
description: "この記事では、ワークスペースの API 識別子を表示する「API キー」ページについて説明します。"

---

# API キー

> **API キー**ページは、すべての REST API キーを一元管理するためのハブです。ここでは、各ワークスペースの API キーセットとアプリ識別子にアクセスできます。

**API キー**ページは**設定**の下にあります。

## API キー {#api-keys}

このセクションでは、ワークスペースの REST API キーを提供します。これは、ワークスペースのデータにアクセスするための一意の識別子です。REST API キーは、Braze API へのすべてのリクエストに必要です。API キーの作成と使用の詳細については、[REST API キーの概要]({{site.baseurl}}/api/api_key/)を参照してください。

### API IP 許可リスト

セキュリティを強化するために、特定の REST API キーに対して REST API リクエストを行うことが許可される IP アドレスとサブネットのリストを指定できます。これは許可リスト（ホワイトリスト）と呼ばれます。特定の IP アドレスまたはサブネットを許可するには、新しい REST API キーを作成する際に **Whitelist IPs** セクションに追加します。

![新しい API キー作成時の API IP ホワイトリストセクション]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

何も指定しない場合、任意の IP アドレスからリクエストを送信できます。

{% alert tip %}
Braze 間の Webhook を作成し、許可リストを使用していますか？[ホワイトリストに登録する IP]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/#ip-whitelisting) のリストをご確認ください。
{% endalert %}

### API 使用量アラート

API 使用量アラートを設定して、主要な API アクティビティを監視し、問題を早期に発見しましょう。これらのアラートは、カスタマーエクスペリエンスに影響を与える前に、予期しないトラフィックパターンを検出するのに役立ちます。

2種類の API アクティビティを追跡できます。

- **REST API エンドポイント：**メッセージの送信、キャンペーン の作成、データのエクスポートなどのアクション。
- **SDK API リクエスト：**アプリ内メッセージのトリガーやユーザープロファイルの同期など、カスタマーエクスペリエンスからのイベント。*この機能は、月間アクティブユーザー（CY 24–25）を購入している場合に利用できます。*

追跡対象を選択したら、アラート条件を定義できます。たとえば、1時間以内にエラー応答が20%増加した場合に通知を受け取ることができます。設定に応じて、メール、Webhook、またはその両方で通知を受け取ります。開始するには、[API 使用量アラート]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts/)を参照してください。

## アプリ識別子

このセクションには、Braze API へのリクエストで特定のアプリを参照するために使用される識別子のリストが含まれています。アプリケーション識別子の詳細については、[アプリ識別子 API キー]({{site.baseurl}}/api/identifier_types/)を参照してください。

## その他の識別子

API と統合するために、Braze 外部 API からアクセスしたい セグメント、キャンペーン、Content Cards などに関連する識別子を検索できます。すべてのメッセージは [UTF-8](https://en.wikipedia.org/wiki/UTF-8) エンコーディングに従う必要があります。いずれかを選択すると、ドロップダウンメニューの下に識別子が表示されます。

詳細については、[API 識別子タイプ]({{site.baseurl}}/api/identifier_types/)を参照してください。