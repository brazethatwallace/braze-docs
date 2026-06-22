---
nav_title: Extole
article_title: Extole
description: "この記事では、BrazeとExtoleのパートナーシップについて説明します。Extoleはリファラルマーケティング企業であり、友人紹介プログラムと成長プログラムから顧客イベントと属性をBrazeに取り込むことができます。"
alias: /partners/extole/
page_type: partner
search_tag: Partner

---

# Extole

> SaaS企業である[Extole](https://www.extole.com/)は、友達紹介マーケティングの業界リーダーであり、顧客獲得を増やすための効果的な紹介マーケティングプログラムの作成と最適化を支援しています。

_この統合はExtoleによって管理されています。_

## 統合について {#about-the-integration}

BrazeとExtoleの統合により、Extoleの友人紹介プログラムや成長プログラムから顧客イベントや属性をBrazeに取り込むことができ、顧客の獲得、エンゲージメント、ロイヤルティを高める、よりパーソナライズされたマーケティングキャンペーンを作成できるようになります。パーソナライズされた共有コードやリンクなど、Extoleのコンテンツ属性をBrazeのコミュニケーションにダイナミックに取り込むこともできます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Extoleアカウント | このパートナーシップを活用するには、Extoleアカウントが必要です。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze API URL | Braze API URLは、お使いの[Brazeインスタンス]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)に固有です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## ユースケース {#use-cases}

以下のユースケースは、ExtoleとBrazeの統合を使用するいくつかの方法を示しています。Extoleの実装マネージャーおよびカスタマーサクセスマネージャーと協力して、お客様の自社固有のニーズに対応するオプションを開発してください。

- 紹介プログラムやエンゲージメントプログラムのカスタムイベントを使用して、Braze キャンペーンやキャンバスをトリガーする
- Extoleを使用したプログラムのデータを使用して、カスタムセグメント、ダッシュボード、レポートを作成する
- Brazeでユーザーをマーケティングリストに自動的に登録または登録解除する

## 統合 {#integration}

統合を迅速に起動して実行するには、以下のステップを完了してください。Extoleの実装およびカスタマーサクセスマネージャーがこのプロセスを支援し、ご質問に回答します。

### Brazeアカウントに接続する {#connect-to-your-braze-account}

1. My Extoleアカウントの[パートナー](https://my.extole.com/partners)ページでBraze統合を選択します。
2. Braze統合で**Install**を選択し、ExtoleとBrazeの接続を開始します。
3. Braze REST APIキーをはじめとする必須フィールドを入力します。
4. Braze API URLを入力します。このURLは、Brazeアカウントがどのインスタンスにプロビジョニングされているかによって異なります。
5. Brazeに送信したいExtoleイベントを追加します。デフォルトのイベント、イベントプロパティ、およびユーザー属性は、[Extoleイベントの表](https://dev.extole.com/docs/braze#extole-program-events)で説明されています。
6. `FULFILLED` 状態以外に、Brazeに送信するリワードの状態を追加します。利用可能なリワードの状態の説明については、[Extoleリワードの表](https://dev.extole.com/docs/braze#extole-rewards)を参照してください。
7. Braze外部IDキーマッピングを選択します。これが、ExtoleがBrazeでユーザープロファイルを更新する方法です。Brazeのexternal IDキーをExtoleのユーザーの`email_address`または`partner_user_id`にマッピングできます。より安全なので、`email_address`の代わりに`external_id`を使用することをお勧めします。
8. 設定を保存して接続を完了します。これで、ExtoleのイベントがBrazeアカウントに流れるようになります。

### Extoleプログラムイベント {#extole-program-events}

以下は、ExtoleがBrazeに送信するデフォルトのイベント、イベントプロパティ、ユーザー属性です。Extoleの実装またはカスタマーサクセスマネージャーに連絡し、追加のExtoleイベントを特定して統合に追加してください。

| イベント | 説明 | イベントプロパティ | ユーザー属性 |
| ----------- | ----------- | ----------- | ----------- |
| `extole_created_share_link` | 参加者がExtole Share Experienceにメールを入力して、共有リンクを作成します。 | イベント名  <br>イベント時間  <br>パートナー（Extole）  <br>ファネル（アドボケイトまたは友人）  <br>プログラム | <br>External ID <br>メール  <br>共有リンク |
| `extole_shared` | 参加者が自分の紹介リンクを友人にシェアします。 | イベント名  <br>イベント時間  <br>パートナー（Extole）  <br>External ID  <br>ファネル（アドボケイトまたは友人）  <br>プログラム  <br>シェアチャネル | メール <br>名 <br>姓 |
| `outcome` - 結果は、プログラムの設定（`extole_shipped`や`extole_converted`など）に基づいてダイナミックに変化します。| 参加者が、プログラムに設定されている目的の成果イベントをコンバージョンまたは完了しました。 | プログラムごとにダイナミック | メール <br>名 <br>姓 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Extole program events" }

### Extoleのサブスクリプション状態 {#extole-subscription-states}

| サブスクリプションの状態 | 説明 | イベントプロパティ | ユーザー属性 |
| ----------- | ----------- | ----------- | ----------- |
| `subscribed` | 参加者がマーケティングメッセージの受信をオプトインしました。 | 該当なし | メール  <br>リストのタイプ  <br>External ID  <br>メール購読（オプトイン） |
| `unsubscribed` | 参加者がExtoleメールコミュニケーションの受信をオプトアウトしました。| メール  <br>External ID  <br>サブスクリプション状態（配信停止）  <br>サブスクリプショングループID  | リストのタイプ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Extole subscription states" }

### Extoleのリワード {#extole-rewards}

デフォルトでは、Extoleは`FULFILLED`状態のリワードイベントをBrazeに送信します。このため、Braze キャンペーンまたはキャンバスを通じてリワード通知をトリガーできます。その他のリワード状態については、以下の表を参照してください。

| リワード状態 | 説明 | イベントプロパティ | ユーザー属性 |
| ----------- | ----------- | ----------- | ----------- |
| `FULFILLED` | デフォルトの状態です。リワードには、Extoleリワードサプライヤーによって価値（クーポンやギフトカードなど）が割り当てられています。 | メール <br>額面  <br>クーポンコード  <br>額面タイプ  | メール <br>名  <br>姓 |
| `EARNED` | リワードが作成され、人物に関連付けられています。 | メール <br>額面  <br>クーポンコード  <br>額面タイプ  | メール <br>名  <br>姓 |
| `SENT` | リワードが履行され、受信者にメールまたはデバイスで送信されました。 | メール <br>額面  <br>クーポンコード  <br>額面タイプ  | メール <br>名  <br>姓 |
| `REDEEMED` | リワードは、Extoleに送信されたコンバージョンイベントまたは引き換えイベントで証明されているように、受信者によって使用されました。| メール <br>額面  <br>クーポンコード  <br>額面タイプ  | メール <br>名  <br>姓 |
| `FAILED` | 問題が発生したため、リワードを発行または送付できませんでした。対応が必要です。 | メール <br>額面  <br>クーポンコード  <br>額面タイプ  | メール <br>名  <br>姓 |
| `CANCELED` | リワードは無効化され、インベントリに戻されます。 | メール <br>額面  <br>額面タイプ  | メール <br>名  <br>姓 |
| `REVOKED` | 履行されたリワードが無効化されました。たとえば、Extoleがサプライヤーギフトカードを依頼したが、カードが誤って送付されたと判断した場合などです。サプライヤーがリワードの取り消しに対応している場合、Extoleは資金の払い戻しを依頼し、リワードは無効になります。 | メール <br>額面   <br>額面タイプ  | メール <br>名  <br>姓 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Extole rewards" }


## カスタマイズ {#customization}

### Brazeでユーザーを検索し作成する {#find-and-create-users-in-braze}

Extoleにexternal ID（ユーザーID）がない新しいメールやSMSサブスクリプションなどの特定のユースケースでは、Extoleは Brazeの[識別子によるユーザープロファイルのエクスポートエンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)を使用して、ユーザーの識別子を確認できます。ユーザーがBrazeに存在する場合、Extoleはプロファイル属性を追加・更新します。リクエストがユーザープロファイルを返さない場合、Extoleは`/users/track`エンドポイントを使用して、ユーザーのメールアドレスをエイリアス名とするユーザーエイリアスを作成します。

## この統合を使う {#using-this-integration}

アカウントを接続すると、何もしなくても自動的にExtoleからBrazeにイベントが流れ始めます。Brazeに送信されるイベントのライブビューは、ExtoleのOutbound Webhook Centerでトラブルシューティングのために参照できます。