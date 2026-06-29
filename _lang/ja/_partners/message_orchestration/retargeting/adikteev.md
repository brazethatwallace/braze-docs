---
nav_title: Adikteev
article_title: Adikteev 解約予測
description: "この参考記事では、Brazeと、解約予測とサービス全般を取り扱うアプリリターゲティングを組み合わせたユーザーリテンションエンジンであるAdikteevの提携について概説しています。"
alias: /partners/adikteev/
page_type: partner
search_tag: Partner

---

# Adikteev 解約予測 {#adikteev-churn-prediction}

> [Adikteev](https://www.adikteev.com/churn-prediction) は、解約予測とサービス全般を取り扱うアプリリターゲティングを組み合わせたユーザーリテンションエンジンです。

_この統合は Adikteev によって管理されています。_

## 統合について {#about-the-integration}

BrazeとAdikteevの統合により、Braze CRM キャンペーン内でAdikteevの解約予測技術を活用し、リスクの高いユーザーセグメントを優先的にターゲットにすることで、ユーザーリテンションを高めることができます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| --- | --- |
| Adikteev アカウント | このパートナーシップを活用するには、Adikteevアカウントが必要です。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze REST エンドポイント | [REST エンドポイント URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、お使いのインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

{% tabs %}
{% tab オーディエンスフィルタリング %}
解約リスクに基づいてオーディエンスセグメントを絞り込みます。<br> Adikteevにより送信されるカスタム属性の名前と値は設定可能です。

![Adikteevから送信されたカスタム属性をオーディエンスセグメントフィルターとして使用する方法の例を示すスクリーンショット。]({% image_buster /assets/img/adikteev/audience.png %})
{% endtab %}
{% tab メッセージターゲティング %}
受信者の解約リスクに基づいてBrazeメッセージングキャンペーンをカスタマイズします。

![Adikteevから送信されたカスタム属性をキャンペーンターゲティングフィルターとして使用する例を示すスクリーンショット。]({% image_buster /assets/img/adikteev/campaign.png %})
{% endtab %}
{% endtabs %}

## 統合 {#integration}

### ステップ1:アプリのイベントストリームを共有する {#step-1-share-the-event-stream-of-your-app}

アプリオーディエンスの解約予測を開始するには、Adikteevでモバイル計測プラットフォームからのイベントのポストバックをオンにする必要があります。設定方法については、[Adikteev サポートWebサイト](https://help.adikteev.com/hc/en-us/sections/8185123408914-Data-stream-activation)のガイドラインに従ってください。

### ステップ2:Braze REST APIキーを作成する {#step-2-create-your-braze-rest-api-key}

Brazeで**設定** > **APIキー**に移動します。**新しいAPIキーを作成**を選択して使用するAPIキー名を入力し、次の権限が追加されていることを確認します。

- `users.track`

### ステップ3:Adikteev チームに情報を提供する {#step-3-provide-information-to-the-adikteev-team}

統合を完了するには、REST APIキーとRESTエンドポイントURLをAdikteevアカウントマネージャーに提供する必要があります。Adikteevは接続を確立し、セットアップ完了後に統合を確認するためにご連絡します。

## バッチ処理とレート制限 {#batching-and-rate-limits}

`user.track` エンドポイントは、ユーザーの詳細を更新するために使用されます。エンドポイントのレート制限、リクエストのバッチ処理、リクエストの詳細については、[APIドキュメント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を参照してください。

{% alert tip %}
API呼び出しの総数を削減するため、変更されたデータを更新する目的でのみAPI呼び出しを実行すべきであることを覚えておいてください。つまり、解約セグメントが変更されたユーザーだけを更新してください。
{% endalert %}

## ユーザーとデバイスの識別子 {#user-and-device-identifiers}

Brazeのユーザープロファイルは、任意のタイプのユーザーまたはデバイス識別子に関連付けることができます。使用できるオプションのリストは、データ収集をBrazeとどのように統合したかに応じて異なります。Adikteevでは、解約セグメント情報を正しく送信するために、MMPとBrazeのユーザープロファイルの間で共通の識別子を見つける必要があります。

## データの保持と削除 {#data-retention-and-deletion}

更新が行われない場合、属性とその値はBrazeユーザープロファイルに無期限に保持されます。

プロファイル属性を削除するには、`null` に設定します。

## リクエストペイロード {#request-payloads}

AdikteevからBrazeに送信されるペイロードはカスタマイズ可能であり、顧客のニーズに合わせて設定できます。これには、使用する識別子、カスタム属性の名前、AdikteevがBrazeで新しいユーザーを作成できるかまたは既存のユーザーのみを更新するかの設定が含まれます。


## サポートとトラブルシューティング {#support-and-troubleshooting}

統合に関するご質問や、ユースケースに関するサポートについては、Adikteevアカウントマネージャーにお問い合わせください。