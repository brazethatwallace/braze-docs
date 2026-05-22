---
nav_title: Flybuy
article_title: Flybuy
alias: /partners/flybuy/
description: "このリファレンス記事では、BrazeとロケーションサービスプラットフォームであるFlybuyとのパートナーシップについて説明します。このパートナーシップにより、オペレーションやマーケティング機能にロケーションインテリジェンスを追加できます。"
page_type: partner
search_tag: Partner

---

# Flybuy

> Radius Networksの[Flybuy](https://www.flybuy.com/)は、AI搭載テクノロジーを活用してピックアップ、デリバリー、ドライブスルー、店内飲食のサービス速度を最適化する、業界をリードするオムニチャネルロケーションプラットフォームです。統合されたMarketing Suiteを通じて、Flybuyはブランドがハイパーターゲティングされたモーメントベースのメッセージを配信できるようにし、エンゲージメントの促進、注文単価の向上、より広範なロイヤルティ施策のサポートを実現します。

_このインテグレーションはFlybuyによって管理されています。_

## インテグレーションについて {#about-the-integration}

FlybuyはリッチなユーザーインテリジェンスイベントをBrazeに配信し、ブランドが最高レベルのパーソナライゼーションでハイパーレレバントなロケーション対応メッセージを送信できるようにします。ユーザーがFlybuyでイベントを生成すると、リッチなユーザー属性を含むカスタムイベントがBrazeに配信されます。これらのイベントと属性を使用して、オムニチャネルオペレーションを強化し、近接ベースのメッセージをトリガーできます。

## 前提条件 {#prerequisites}

インテグレーションを有効にする前に、以下が必要です。

| 要件 | 説明 |
|---|---|
| Flybuyアカウント | 少なくとも1つのプロジェクトを持つFlybuyアカウント。 |
| Braze REST APIキー | `users.track`権限を持つBraze REST APIキー。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## インテグレーション {#integration}

インテグレーションを有効にするには、以下のステップを完了してください。

1. Flybuy Merchantポータルで、**Project Info**に移動し、**Events Engine**をクリックします。
2. **Add a Destination**をクリックし、**Braze**を選択します。
3. Braze APIキーとエンドポイントを追加し、有効にしたいイベントを選択します。
4. **Finish Setup**をクリックします。

{% alert important %}
Flybuyは、ログイン済みユーザーの`loyalty_id`をBrazeの`external_id`にマッピングします。
{% endalert %}

## ユースケース {#use-cases}

- [ピックアップ](https://www.flybuy.com/flybuypickup)
- [デリバリー](https://www.flybuy.com/flybuydelivery)
- [ドライブスルー](https://www.flybuy.com/flybuydrivethru)
- [テーブルサービス](https://www.flybuy.com/flybuytableservice)
- [ホテルモバイルチェックインとオーダリング](https://www.flybuy.com/industries/hospitality)
- [Marketing Suite](https://www.flybuy.com/flybuy-marketing-suite)

## イベントおよび属性ベースのトリガー例 {#event-and-attribute-based-trigger-examples}

カスタムイベントとカスタム属性を使用して、さまざまなパーソナライズ体験を実現できます。

### ピックアップ体験が悪かった顧客のオーディエンスセグメントを構築する {#build-an-audience-segment-of-customers-who-had-a-bad-pickup-experience}

たとえば、ピックアップ体験を5つ星未満と評価した顧客をターゲットにします。

![ピックアップ体験が悪かった場合のセグメント]({% image_buster /assets/img/flybuy/flybuy1.png %})

### 顧客が仮想ピックアップエリアに入ったときにアラートをトリガーする {#trigger-an-alert-when-a-customer-enters-a-virtual-pickup-area}

ロイヤルティアカウントを持っていない顧客をターゲットに、アプリのダウンロードとロイヤルティアカウントの作成を促すパーソナライズSMSを送信します。

![顧客が仮想ピックアップエリアに入ったときにアラートをトリガーする]({% image_buster /assets/img/flybuy/flybuy2.png %})

![顧客が仮想ピックアップエリアに入ったときのアラートメッセージ]({% image_buster /assets/img/flybuy/flybuy2a.png %})

### 待ち時間が長かった顧客のオーディエンスセグメントを構築する {#build-an-audience-segment-of-customers-who-had-a-long-wait-time}

たとえば、仮想店舗エリアを退出する際に2分以上の待ち時間があった顧客をターゲットにします。

![待ち時間が長かった顧客のオーディエンスセグメント]({% image_buster /assets/img/flybuy/flybuy3.png %})

### 顧客が間違った場所に向かっているときにコース修正アラートをトリガーする {#trigger-a-course-correction-alert-when-a-customer-is-headed-to-the-wrong-location}

顧客が注文した場所とは異なるロケーションに向かっている、または到着した場合にプッシュ通知を送信します。

### トリップマイルストーンに基づいて特別オファーを配信する {#deliver-special-offers-based-on-trip-milestones}

たとえば、VIP顧客がお気に入りのロケーションに到着したときに特別オファーを送信します。

### 注文に商品が不足していた顧客のオーディエンスセグメントを構築する {#build-an-audience-segment-of-customers-who-were-missing-items-in-their-order}

たとえば、デジタル注文で商品が不足していたとコメントした顧客をターゲットにします。

APIとSDKの詳細については、[Flybuy開発者ドキュメント](https://www.radiusnetworks.com/developers/flybuy/#/)を参照してください。