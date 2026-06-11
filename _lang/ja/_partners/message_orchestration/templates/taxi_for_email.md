---
nav_title: Taxi for Email
article_title: Taxi for Email
alias: /partners/taxi_for_email
description: "このリファレンス記事では、BrazeとTaxi for Emailのパートナーシップについて説明します。Taxi for Emailは、Brazeのお客様がドラッグアンドドロップインターフェイスとシンプルで強力な構文を使用してインテリジェントなメールテンプレートを作成できるオンラインメールマーケティングツールです。"
page_type: partner
search_tag: Partner

---

# Taxi for Email

> [Taxi for Email](http://taxiforemail.com/)は、直感的なドラッグアンドドロップのビジュアルメールエディターを提供するオンラインメールマーケティングツールです。Taxiを使用すると、チームがメールキャンペーンで簡単にコラボレーションでき、コピーライターや編集者がコードなしでメールを作成するために必要なアクセスとリソースを利用できます。

_この統合は、Taxi for Emailによって管理されています。_

## 統合について {#about-the-integration}

BrazeとTaxiの統合では、Taxiのシンプルで強力な構文を使用して、インテリジェントなメールテンプレートを作成しBrazeにエクスポートします。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ------------| ----------- |
| Taxi for Emailアカウント | このパートナーシップを活用するには、Taxi for Emailアカウントが必要です。 |
| Braze REST APIキー | 完全な**テンプレート**権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Brazeエンドポイント | [Brazeエンドポイント]({{site.baseurl}}/api/basics/#endpoints)は、BrazeダッシュボードのURLに対応しています。<br><br> たとえば、ダッシュボードURLが`https://dashboard-03.braze.com`の場合、エンドポイントは`dashboard-03`になります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

### ステップ 1: Taxiメールテンプレートを作成する {#step-1-create-a-taxi-email-template}

Taxiプラットフォームでテンプレートを作成します。テンプレートが作成されたら、**Organization Settings**に移動して**ESP Connectors**タブを選択します。

### ステップ 2: Brazeコネクターを作成する {#step-2-create-braze-connector}

1. 表示されるダイアログで、**Add New**ボタンを選択し、ドロップダウンから**Braze**を選択します。
2. **Braze**を選択して、Brazeコネクターの設定を編集します。
3. BrazeエンドポイントとBraze APIキーを入力します。

正しい権限を含む詳細が入力されると、コネクターフィールドの色が変わります。このフィールドの色が変わらない場合は、入力内容がリストされている要件に合っていることを確認してください。

## 使用方法 {#usage}

アップロードされたTaxiテンプレートは、Brazeアカウントの**テンプレートとメディア > メールテンプレート**セクションで確認できます。このメールテンプレートを使用して、顧客に魅力的なメールメッセージを送信しましょう！