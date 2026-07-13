---
nav_title: Jebbit
article_title: Jebbit
description: "この参考記事では、BrazeとJebbitのパートナーシップについて概説しています。JebbitはPaaSであり、Jebbitキャンペーンからユーザーメールや属性をユーザーデータとしてリアルタイムでBrazeに渡すことができます。"
alias: /partners/jebbit/
page_type: partner
search_tag: Partner

---

# Jebbit

> [Jebbit](https://www.jebbit.com/) は、ユーザーがファーストパーティデータを取得するための魅力的なエクスペリエンスを構築できる PaaS です。

_この統合は Jebbit によって管理されています。_

## 統合について {#about-the-integration}

BrazeとJebbitの統合により、Jebbitキャンペーンのユーザーメールと属性をユーザーデータとしてBrazeにリアルタイムで渡すことができます。その後、パーソナライズされたメールキャンペーンやトリガーなどのマーケティングイニシアチブを推進するためにこのデータを利用できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Jebbitアカウント | このパートナーシップを活用するには、Jebbitアカウントが必要です。 |
| Braze REST APIキー | すべてのユーザーデータ権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントは、[インスタンス]({{site.baseurl}}/api/basics/#endpoints)のBraze URLによって異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

Jebbitとの統合をリクエストする際は、厳しい納期がある場合はその旨を伝えてください。さらに、Brazeに渡したい属性がJebbitエクスペリエンスにマッピングされていることを確認してください。

### ステップ 1: API認証情報を提供する {#step-1-provide-api-credentials}

API認証情報をテキストファイルでDropboxファイルリクエスト経由でJebbitに提供してください。
以下の[Dropbox URL](https://www.dropbox.com/request/RqKQHkJHXw1cFBKbXpZx)を使用してファイルを送信してください。

### ステップ 2: テスト送信を確認する {#step-2-confirm-test-submission}

統合を担当するJebbitエンジニアが、JebbitからBrazeへのテスト送信を実行します。これにより、Braze環境でデータがどのように表示されるかを確認できます。これが統合を有効化する最後のステップです。Jebbitのデータがセットアップされたので、それを使ってマーケティングイニシアチブを推進しましょう。

{% alert note %}
Jebbitで設定した属性IDが、Brazeでの属性フィールド名の表示名になります。
{% endalert %}

## カスタマイズ {#customization}

現在、[ユーザーデータ]({{site.baseurl}}/api/endpoints/user_data/)エンドポイントを特にサポートしていますが、異なるエンドポイントへのリクエストもサポート可能です。

属性フィールド名もお好みに応じてカスタマイズできます。

BrazeでJebbitから追加の属性が必要な場合は、Jebbitアカウントで新しい属性をマッピングしてください。その属性のデータを収集すると、Brazeにその属性が自動的に表示されます。