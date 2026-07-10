---
nav_title: Refiner
article_title: Refiner
alias: /partners/refiner/
description: "このリファレンス記事では、BrazeとRefinerのパートナーシップについて説明します。このパートナーシップにより、アンケートイベントと回答データをBrazeに送信して、キャンペーンのトリガー、ユーザーのセグメント化、ユーザープロファイルの更新が可能になります。"
page_type: partner
search_tag: Partner

---

# Refiner

> [Refiner](https://refiner.io)は、SaaSおよびモバイルアプリ向けのアプリ内アンケートプラットフォームです。プロダクトチームやVoC（顧客の声）チームが、ターゲットを絞ったアプリ内アンケートを配信し、NPS、CSAT、CES、製品フィードバック、ゼロパーティユーザーデータを継続的に収集できます。

*このインテグレーションはRefinerによって管理されています。*

## インテグレーションについて {#about-the-integration}

RefinerとBrazeのインテグレーションを使用して、Refinerからアンケートイベントと回答データをBrazeアカウントに送信します。このデータを使用して、アンケートのインタラクション（アンケート完了など）に基づいてBrazeキャンペーンをトリガーしたり、回答に基づいてユーザーをセグメント化したり、アンケートの回答から得られた特性でBrazeユーザープロファイルを更新したりできます。

## ユースケース {#use-cases}

- NPSスコアやCSAT評価などのアンケート回答に基づいてユーザーをセグメント化します。
- アンケート結果に基づいて、Brazeでパーソナライズされたキャンペーンをトリガーします。
- Brazeキャンバスやその他のオーケストレーションツールを使用して、クロスチャネルのジャーニーを推進します。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| Refinerアカウント | このインテグレーションを使用するには、[Refiner](https://refiner.io)アカウントが必要です。 |
| Braze REST APIキー | `users.track`権限を持つBraze REST APIキー。これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | RESTエンドポイントURL。エンドポイントは、[お使いのインスタンスのBraze URL]({{site.baseurl}}/api/basics#endpoints)によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## インテグレーション {#integration}

### ステップ1：Brazeアカウントを接続する {#step-1-connect-your-braze-account}

Refinerプロジェクトの**Integrations**セクションで、**Connect Braze**を選択します。Braze REST APIキーとBrazeインスタンス識別子を入力します。

### ステップ2：ユーザー識別子をマッピングする {#step-2-map-user-identifiers}

Refinerのユーザー識別子を、Brazeの`external_id`やメールアドレスなど、使用しているBraze識別子にマッピングします。これにより、イベントがBraze内の正しいユーザーに関連付けられます。

### ステップ3：同期するデータを選択する {#step-3-choose-data-to-sync}

- Brazeに同期するアンケートのデータを選択します。
- **Survey Seen**、**Survey Dismissed**、**Survey Completed**など、Brazeに送信するRefinerイベントを選択します。

![アンケートの選択とイベントマッピングオプションを表示するRefinerインテグレーション設定パネル。]({% image_buster /assets/img/refiner.jpg %})

## Refinerをカスタマイズする {#customize-refiner}

- Brazeに送信するデータに、アンケートの回答のみを含めるか、追加の連絡先データフィールドも含めるかを選択します。
- 同期されたデータフィールドに`refiner_`プレフィックスを付けて、Brazeアカウント内で識別しやすくするかどうかを選択します。

## Brazeでアンケートデータを使用する {#use-survey-data-in-braze}

BrazeとRefinerを接続すると、**Saw Survey**や**Completed Survey**などのアンケートイベントが、Brazeアカウントのユーザープロファイルに表示されます。これらのイベントを使用して、Brazeでメッセージをトリガーおよびパーソナライズしたり、アンケートの回答データを使用してユーザーをセグメント化したりできます。

{% alert note %}
Brazeを通じてメールでRefinerアンケートを送信することもできます。詳細については、[Refinerのインテグレーションドキュメント](https://refiner.io/docs/kb/integrations/braze-integration/)を参照してください。
{% endalert %}

## トラブルシューティング {#troubleshooting}

インテグレーションに問題が発生した場合は、以下のリソースを参照してください。

- [RefinerとBrazeのインテグレーションガイド](https://refiner.io/docs/kb/integrations/braze-integration/)
- [Refinerサポートに問い合わせる](https://refiner.io/docs/kb/getting-started/contact-support/)