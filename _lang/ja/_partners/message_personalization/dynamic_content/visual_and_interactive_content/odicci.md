---
nav_title: Odicci
article_title: Odicci
description: "パーソナライズされたマーケティングキャンペーンのためにOdicciとBrazeを統合するためのステップバイステップガイド"
alias: /partners/odicci/
page_type: partner
search_tag: Partner
---

# OdicciとBrazeを統合する {#integrate-odicci-with-braze}

> ロイヤルティ主導のオムニチャネルエクスペリエンスを通じて顧客の獲得、エンゲージメント、維持を可能にするプラットフォームである[Odicci](https://www.odicci.com/)とBrazeを統合する方法を説明します。

{% alert tip %}
その他のリソースやFAQについては、[Odicciヘルプセンター](https://help.odicci.com)を参照してください。
{% endalert %}

## ユースケース {#use-cases}

OdicciプラットフォームをBrazeと接続することで、シームレスなデータ共有とCampaign管理が可能になります。具体的には以下が含まれます。

- Odicciエクスペリエンスで収集したオーディエンスデータを自動的にBrazeに送信する。
- ユーザーとのインタラクションに基づいてパーソナライズされたマーケティングキャンペーンをトリガーする。
- OdicciとBraze間のフィールドをマッピングし、正確なデータ同期を確保する。

## 例 {#example}

ある小売店が、マーケティングキャンペーン用のメールアドレスを収集するためにOdicciのゲーミフィケーションエクスペリエンスを使用しています。

1. 顧客がOdicciでゲームを完了し、メールアドレスを提供します。
2. Odicciはこのデータを自動的にBrazeに同期します。
3. Brazeがパーソナライズされた「Thank You」メールをトリガーし、割引コードを含めます。

## 前提条件 {#prerequisites}

開始する前に、以下が必要です。

| 要件 | 説明 |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Odicciアカウント | このパートナーシップを利用するには、**統合**セクションへのアクセス権があるOdicciアカウントが必要です。|
| Braze REST APIキー | `users.track`および`campaigns.list`権限を持つBraze REST APIキー。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## Odicciの統合 {#integrating-odicci}

### ステップ1: Odicciで統合を有効にする {#step-1-enable-the-integration-in-odicci}

1. Odicciアカウントにログインします。
2. **設定 > 統合**セクションに移動します。
3. **Braze**統合を見つけ、**接続**をクリックします。

   ![Braze統合の接続画面]({% image_buster /assets/img/odicci/braze_connect.png %})

4. Braze REST APIキーを所定のフィールドに入力します。
5. 設定を保存して、アカウントレベルで統合を有効にします。

### ステップ2: Braze REST APIキーを取得する {#step-2-obtain-your-braze-rest-api-key}

1. Brazeアカウントにログインします。
2. **開発者コンソール > REST APIキー**に移動します。
3. 新しいAPIキーを作成するか、`users.track`権限がある既存のAPIキーをコピーします。

### ステップ3: エクスペリエンスレベルで統合をアクティブ化する {#step-3-activate-the-integration-at-the-experience-level}

1. Odicci Studioで**エクスペリエンス**を作成するか、開きます。
2. **Studio > 設定 > 統合**に移動します。
3. **Braze**チェックボックスを探し、チェックを入れてエクスペリエンスの統合をアクティブ化します。
4. 変更を保存します。

### ステップ4: フィールドをマッピングする {#step-4-map-fields}

1. 統合をアクティブ化した後、**Studio > 設定 > 統合**セクションにとどまります。
2. Odicciエクスペリエンスのフィールド（例: `Email`、`Name`）をBrazeの対応するフィールドにマッピングします。
3. 設定を保存します。

   ![フィールドマッピングの設定画面]({% image_buster /assets/img/odicci/braze_field_mapping.png %})

### ステップ5: 統合をテストする {#step-5-test-the-integration}

1. Odicciでエクスペリエンスを実行し、テストデータを収集します。
2. Brazeのダッシュボードまたはデータログを確認して、データがBrazeに正しく同期されていることを確認します。
3. マッピングされたフィールドがBrazeに正しく入力されていることを確認します。

## トラブルシューティング {#troubleshooting}

統合に問題が発生した場合は、以下のソリューションを検討してください。詳細なサポートが必要な場合は、[Odicciサポート](https://help.odicci.com)にお問い合わせください。

### APIキーが有効ではない {#api-key-not-valid}

Braze APIキーを再確認し、必要な権限を保持していることを確認します。その後、Odicciの統合設定にAPIキーを入力しなおしてください。

### データが同期されない {#data-not-syncing}

**フィールドマッピング**セクションのフィールドが正しく設定されていることを確認します。次に、APIキーにユーザーデータのインポート権限があることを確認します。

### Campaignがトリガーされない {#campaign-not-triggering}

BrazeのCampaign設定を確認し、正しいオーディエンスまたはトリガー条件が設定されていることを確認します。