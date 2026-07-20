---
nav_title: Simon AI
article_title: Simon AI
description: "BrazeとSimon AIの統合を使用して、高度なオーディエンスを作成し、リアルタイムかつノーコードでBrazeに同期してオーケストレーションを行います。"
alias: /partners/simon_data/
page_type: partner
search_tag: Partner
---

# Simon AI

> [Simon AI][1]のエージェンティックマーケティングプラットフォームは、マーケティングチームが真の1対1パーソナライゼーションを実現するのを支援します。コンポーザブルな顧客データプラットフォームと、Snowflake AIデータクラウド上で直接動作するAIエージェントを組み合わせ、マーケターのデータおよび実行チームとして機能します。

BrazeとSimon AIの統合を使用して、高度なオーディエンスを構築し、リアルタイムかつノーコードのオーケストレーションのためにBrazeに同期できます。この統合により、Simon AIのID解決、顧客データ統合、AI駆動のセグメンテーションを活用して、よりパーソナライズされた効果的なBrazeキャンペーンを下流で実行できます。

## 前提条件 {#prerequisites}

開始するには、Simon AIアカウント内でBrazeアカウントを認証する必要があります。

| 要件 | 説明 |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Simon AI | Simon AI内からBraze統合を利用するには、既存のSimon AIアカウントが必要です。 |
| Braze REST APIキー | `users.track`、`campaigns.trigger.schedule.create`、および`campaigns.trigger.send`の権限を持つBraze REST APIキー。<br><br>これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| BrazeダッシュボードURL | [RESTエンドポイントURL][3]。エンドポイントは、お使いのインスタンスのBraze URLによって異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

- Brazeキャンバスまたはメールをトリガーする
- セグメントプロパティを渡して維持する
- トレイトとコンタクトプロパティを同期する

{% alert note %}
SimonとBrazeの統合を使用する場合、Simonは各同期時にデルタのみをBrazeに送信し、不要なデータに対するコストを回避します。詳細については、[トレイトとコンタクトプロパティの同期](#sync-traits-and-contact-properties)を参照してください。
{% endalert %}

## 統合 {#integration}

### Simon AIでBrazeアカウントを認証する {#authenticate-your-braze-account-in-simon-ai}

Braze統合を使用するには、まずSimonでBrazeアカウントを認証します。

1. ナビゲーションメニューから**Integrations**をクリックし、Brazeまでスクロールします。
2. Braze [REST APIキー][2]と[ダッシュボードURL][3]を入力します。
3. **Save Changes**をクリックします。

接続に成功すると、ウィンドウに**Connected**と表示されます。

![Simon AIの統合画面][8]{: style="max-width:70%"}

### Simon AIのフローまたはジャーニーにBrazeアクションを追加する {#add-braze-actions-to-flows-or-journeys-in-simon-ai}

Simon AIでBrazeアカウントを認証した後、[フロー][4]と[ジャーニー][5]にBrazeアクションを追加できます。

3つのアクションが利用可能です。

- **Sync Simon segment attribute**：セグメントの詳細をBrazeの新規または既存のカスタム属性と同期します。
- **Trigger a Braze キャンバス**：Simonのセグメントデータを活用するBrazeキャンバスをトリガーします。
- **Send a Braze campaign**：SimonからBrazeキャンペーン全体を起動します。

![Simon AIで利用可能なBrazeアクションのリストを表示するドロップダウン][9]{: style="max-width:60%"}

一部のアクションは、特定のフロータイプまたはジャーニーのみで利用可能です。詳細については、[docs.simondata.com][6]を参照してください。

### トレイトとコンタクトプロパティの同期 {#sync-traits-and-contact-properties}

データ消費を最小限に抑えるために、セグメント内のすべての顧客のすべてのフィールドを更新するのではなく、デフォルトで同期する特定のトレイトを選択できます。

{% alert note %}
トレイト同期を開始するには、[Simonサポートセンター](https://docs.simondata.com/docs/support-center)でリクエストを送信してください。アカウントマネージャーが、以下のステップに進める準備ができたらお知らせします。
{% endalert %}

アカウントマネージャーがコンタクトトレイトを有効化した後：

1. Simonで、左側のナビゲーションの**Admin Center**を展開し、**Sync Contact Traits**を選択します。
2. **Braze**を選択します。コンタクトプロパティがデータセットごとにネストされて表示されます。
3. SimonとBrazeの統合を使用する際に同期したいフィールドを選択します。
   1. **Number of traits**は、そのデータセットで選択可能なトレイトの数を示します。すべてを選択するか、行を展開して個別のフィールドを選択できます。
   2. Brazeに到着した際にフィールド名を異なる表示にしたい場合は、**Downstream name**を編集します。
   3. SimonからBrazeへの統合が初めての場合は、**Backfill all contacts**をクリックします。バックフィルは、フローまたはジャーニーでアクションを初めて使用する際にすべてのデータポイントをBrazeに送信し、すべてのデータが完全に同期されていることを確認します。その後の同期では、この画面で選択したトレイトのみがBrazeに送信されます。これにより、必要なデータに対してのみ課金されるようになります。

![Simon AIでの同期トレイトの選択][10]

[1]: https://www.simon.ai/
[2]: {{site.baseurl}}/api/basics#creating-rest-api-keys
[3]: {{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints
[4]: https://docs.simondata.com/docs/campaigns-flows
[5]: https://docs.simondata.com/docs/campaigns-journeys-two
[6]: https://docs.simondata.com
[7]: https://docs.simondata.com/docs/support-center
[8]: {% image_buster /assets/img/simon_data/ConnecttoBraze.png %}
[9]: {% image_buster /assets/img/simon_data/BrazeActions.png %}
[10]: {% image_buster /assets/img/simon_data/BrazeTraitSyncing.png %}