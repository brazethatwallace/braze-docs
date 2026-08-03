---
nav_title: Talkable
article_title: Talkable
description: "このリファレンス記事では、BrazeとTalkableのパートナーシップについて説明します。Talkableはリファラルマーケティングプラットフォームであり、リファラルキャンペーンからのマーケティングメールオプトインをリアルタイムでBrazeに同期します。"
alias: /partners/talkable/
page_type: partner
search_tag: Partner
---

# Talkable

> [Talkable](https://www.talkable.com/)は、消費者ブランドが満足した顧客をスケーラブルなリファラルチャネルに変えることを支援します。Brazeとの連携により、Talkableリファラルキャンペーンで取得されたマーケティングメールオプトインがリアルタイムでBrazeに流れ込み、新しいアドボケイトやフレンドをウェルカム、セグメント化、エンゲージするために必要な同意、コンテキスト、キャンペーンデータをチームに提供します。

_この連携はTalkableによって管理されています。_

## 連携について {#about-the-integration}

Talkableは、Brazeが支えるカスタマージャーニーにアドボケート主導の獲得を組み込みます。この連携により、Talkableが取得したすべてのリファラルオプトインが、リアルタイムで対応するBrazeプロファイルに反映されます。これにより、ウェルカムフロー、リファラルジャーニー、セグメンテーション、ライフサイクルメッセージングを、信頼できる同意とリファラルコンテキストに基づいて開始できます。手動のリストエクスポートやバッチ同期は不要です。

Talkableは、以下の2つのシナリオでマーケティングオプトインを取得します。

* **アドボケートのサインアップ：** アドボケートがTalkableのリファラルキャンペーンにサインアップし、マーケティングメールの受信に同意します。
* **フレンドのメールゲーティング：** フレンドがTalkableのメールゲーティングステップを完了し、マーケティングメールにオプトインします。

いずれの場合も、Talkableは対応するBrazeユーザープロファイルをリアルタイムで作成または更新し、ユーザーのメール購読ステータスを **Opted In** に設定します。

### デフォルトの動作 {#default-behavior}

Talkableは、Talkable内で明示的に同意したユーザーからの個別のオプトインイベントが発生した場合にのみ、Brazeにデータを送信します。これは、アドボケートがキャンペーンにサインアップした場合、またはフレンドがメールゲーティング中にオプトインした場合のいずれかです。Talkableは、夜間バッチ処理、フル同期、暗黙的なプロファイル更新を実行しません。Talkableは、オプトインしていないプロファイルをBrazeに送信することはありません。

## ユースケース {#use-cases}

- 支持者がTalkableの紹介キャンペーンに登録した瞬間に、Brazeのウェルカムキャンバスをトリガーします。
- 紹介された友人がオプトインした直後に、友人専用のキャンバスとパーソナライズされた初回購入オファーでアクティベートします。
- Brazeのカスタム属性として送信される支持者フラグ、友人フラグ、キャンペーンメタデータを使用して、紹介コンテキストでセグメントを作成します。
- コンプライアンスに準拠したニュースレター配信のために、紹介オプトインを指定されたBrazeの購読グループにルーティングします。

## 前提条件 {#prerequisites}

始める前に、以下が必要です。

| 前提条件 | 説明 |
| --- | --- |
| Talkable アカウント | このパートナーシップを活用するには、少なくとも1つのキャンペーンが設定された Talkable サイトが必要です。 |
| Braze REST APIキー | `users.track` 権限を持つ Braze REST APIキー。このキーは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。詳細については、[REST APIキーの作成]({{site.baseurl}}/api/basics#creating-rest-api-keys)を参照してください。 |
| Braze REST エンドポイント | Braze REST エンドポイントURL（例: `https://rest.iad-01.braze.com`）。US（`.com`）および EU（`.eu`）の Braze クラスターの両方がサポートされています。詳細については、[REST APIエンドポイント]({{site.baseurl}}/api/basics#endpoints)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

### ステップ1：TalkableにBrazeアプリをインストールする {#step-1-install-the-braze-app-in-talkable}

1. Talkable管理画面にサインインしてメニューを開き、**All Site Settings** > **App Store** に移動します。
2. **Braze** を見つけて **Install** を選択します。
3. BrazeのRESTエンドポイントと`users.track`権限を持つREST APIキーを入力し、**Save** を選択します。

### ステップ2：メールオプトインアクションを設定する {#step-2-configure-the-email-opt-in-action}

1. TalkableのBrazeアプリで、**Email opt-in** アクションを開きます。
2. （任意）Brazeの購読グループ識別子を入力し、カスタム属性を追加したり、ユーザーエイリアスを設定したりします。詳細については、[Talkableのカスタマイズ](#customizing-talkable)を参照してください。
3. **Save** を選択します。ライブのオプトインイベントが同期される前にテストペイロードで設定を確認できるよう、アクションは無効のままにしておきます。

### ステップ3：サンプルペイロードでテストする {#step-3-test-with-a-sample-payload}

1. Talkableで、**Email opt-in** アクションの **Send sample payload** を選択し、Brazeにテストリクエストを送信します。
2. Brazeで **Audience** > **User Search** に移動し、テスト用のメールアドレスで検索します。
3. プロファイルが存在し、**Email Subscribe** が **Opted In** に設定されていること、また設定したカスタム属性、購読グループの登録、ユーザーエイリアスが期待どおりに表示されていることを確認します。

### ステップ4：ライブトラフィック用にアクションを有効にする {#step-4-enable-the-action-for-live-traffic}

Brazeでテストプロファイルが正しく表示されていることを確認したら、Talkableに戻り、**Email opt-in** アクションを有効にします。

この時点から、Talkableのすべてのオプトインイベントが、対応するプロファイルをリアルタイムでBrazeに同期します。

## Brazeに送信されるデフォルトのユーザー属性 {#default-user-attributes-sent-to-braze}

オプトインイベントが発生するたびに、Talkableは対応するBrazeユーザープロファイルを作成または更新し、以下の標準的なBrazeユーザー属性を設定します。空の値は省略されます。

| Braze属性 | タイプ | 備考 |
| --- | --- | --- |
| `email_subscribe` | String | Talkableのオプトインイベントが発生するたびに**Opted In**に設定されます。 |
| `email` | String | Brazeプロファイルの照合に使用されるプライマリ識別子です。 |
| `phone` | String | ユーザー属性としてのみ取得されます。BrazeはE.164形式を想定していますが、Talkableに保存されたままの形式で送信されます。 |
| `first_name` | String | ユーザーの名です。 |
| `last_name` | String | ユーザーの姓です。 |
| 購読グループへの登録 | 該当なし | 購読グループが設定されている場合、Talkableはユーザーを購読済みとして登録します。 |
| ユーザーエイリアス | 該当なし | ユーザーエイリアスが設定されている場合にのみ追加されます。詳細については、[Talkableのカスタマイズ](#customizing-talkable)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Brazeに送信されるデフォルトのユーザー属性" }

## Talkableのカスタマイズ {#customize-talkable}

以下のオプションのカスタマイズが利用可能です。これらは独立しているため、任意の組み合わせで設定できます。

### オプトインをBraze購読グループに登録する {#enroll-opt-ins-in-a-braze-subscription-group}

1. Brazeで、**オーディエンス** > **購読グループ管理**から購読グループIDをコピーします。詳細については、[ユーザー購読の管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions)を参照してください。
2. Talkableの**メールオプトイン**アクションで、**購読グループ識別子**フィールドにそのIDを貼り付けます。

Talkableは各オプトインを購読済みとしてその購読グループに登録し、リファラルオプトインをグローバル購読ではなくそのグループにスコープします。Talkableは購読の追加のみを行い、削除は行いません。

### カスタム属性を送信する {#send-custom-attributes}

アクションのペイロードエディターに任意のキーと値のペアを追加します。入力したキーがBrazeユーザープロファイルの属性名になります。

値はLiquidテンプレートに対応しています。以下の変数が利用可能です。

{% raw %}
| 変数 | 内容 |
| --- | --- |
| `{{ person }}` | オプトインした推奨者またはフレンド（`email`、`first_name`、`last_name`、`phone_number`、`username`、`is_advocate`、`custom_properties`など）。 |
| `{{ ip }}` | オプトインが発生したIPアドレス。 |
| `{{ campaign }}` | 元のTalkableキャンペーン（`name`、`type`、`tag_names`など）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquidテンプレート変数" }
{% endraw %}

{% raw %}
例：`talkable_is_advocate` = `{{ person.is_advocate }}` と `talkable_campaign_name` = `{{ campaign.name }}` を追加すると、Brazeでリファラルコンテキストによるセグメンテーションが可能になります。
{% endraw %}

### Brazeユーザーエイリアスでユーザーを識別する {#identify-users-with-braze-user-aliases}

ペイロードエディターで、`user_alias.alias_name`（例：{% raw %}`{{ person.username }}`{% endraw %}）と `user_alias.alias_label`（例：`username`）を追加します。詳細については、[ユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object)を参照してください。

両方のフィールドが存在する場合、システムはメールに加えてエイリアスでユーザーを識別し、一致するものがない場合はBrazeが新しいエイリアス付きプロファイルを作成します。

{% alert note %}
両方のエイリアスフィールドが必須です。`alias_name` または `alias_label` のいずれか一方のみが設定されている場合、Talkableはユーザーエイリアスを送信せず、プロファイルはメールのみで照合されます。
{% endalert %}

## Brazeでのユーザーの検索と作成 {#find-and-create-users-in-braze}

* デフォルトでは、Brazeはメールアドレスでプロファイルを照合します。一致するプロファイルが存在しない場合、Brazeは新しいプロファイルを作成します。
* ユーザーエイリアスが設定されている場合、Brazeはそのエイリアスでも照合を行い、一致するものがなければ新しいエイリアス付きプロファイルを作成します。
* このインテグレーションではexternal IDは使用されません。Talkableのオプトインを既存の外部識別済みプロファイルに紐付けるには、そのプロファイルの既知のエイリアスと一致するラベルを持つユーザーエイリアスを設定してください。

## BrazeでTalkableを使用する {#use-talkable-with-braze}

### 同期されたユーザーを見つける {#find-a-synced-user}

**オーディエンス** > **ユーザー検索**に移動し、メールで検索して、Talkableが作成または更新したプロファイルを表示します。

標準フィールド（メール、電話番号、名、姓）および設定したカスタム属性がプロファイルに表示されます。**メール購読**には**オプトイン済み**と表示されます。

### リファラルセグメントを作成する {#build-a-referral-segment}

1. **メール購読**が**オプトイン済み**でフィルタリングしたセグメントを作成します。
2. Talkableが送信するカスタム属性で絞り込みます。たとえば、`talkable_is_advocate` が `true` に等しい場合はアドボケイトをターゲットにし、`talkable_campaign_name` がキャンペーン名に等しい場合は特定のリファラルプログラムをターゲットにします。

### ライフサイクルメッセージングをトリガーする {#trigger-lifecycle-messaging}

1. アクションベースの配信でキャンバスまたはキャンペーンを作成します。この連携では、以下のBrazeトリガータイプが使用できます。
* **購読ステータスの更新**（たとえば、メール購読が**オプトイン済み**になった場合）
* **購読グループステータスの更新**（購読グループが設定されている場合）
* **カスタム属性値の変更**（送信するTalkableカスタム属性に対して）
2. プロファイル上のTalkableカスタム属性（キャンペーン名、リワード値、紹介者など）を使用してメッセージをパーソナライズします。

## 考慮事項 {#considerations}

* **メールオプトインのみ:** 電話番号は標準のユーザー属性として取得されますが、この連携ではSMS購読ステータスは設定されません。TalkableはSMSオプトインを同期しません。
* **電話番号の形式:** Brazeでは電話番号を国際（E.164）形式で指定する必要があります。
* **リアルタイムのイベント駆動型同期:** Talkableはオプトインイベントごとに1件のリクエスト（1リクエストにつき1ユーザー）を送信します。バッチ処理や定期的なフル同期はなく、ボリュームはリファラルオプトインのボリュームに連動します。
* **信頼性の高い配信:** Brazeが一時的にエラーを返した場合、Talkableは自動的にリトライします。永続的な失敗が発生した場合は、サイト管理者にメールアラートが送信されます。

## トラブルシューティング {#troubleshooting}

| エラー | 考えられる原因 | 修正方法 |
| --- | --- | --- |
| 401 Unauthorized | REST APIキーに `users.track` 権限がないか、エンドポイントが間違ったクラスターを指しています。 | `users.track` 権限を持つキーを再発行し、RESTエンドポイントがBrazeクラスターと一致していることを確認してください。 |
| インストール時にRESTエンドポイントが拒否される | URLがBraze RESTエンドポイントではありません。 | クラスターのRESTエンドポイントを使用してください（例: `https://rest.iad-01.braze.com`）。ダッシュボードのURLは使用できません。 |
| プロファイルは作成されたが購読グループに含まれていない | 購読グループIDが設定されていません。 | **Email opt-in** アクションに購読グループIDを入力してください。 |
| ユーザーエイリアスが適用されない | 2つのエイリアスフィールド（名前またはラベル）のうち1つしか入力されていません。 | アクションで両方のフィールド（エイリアス名とエイリアスラベル）を入力してください。 |
| プロファイルが表示されない | サンプルリクエストがまだ送信されていないか、アクションが無効になっています。 | Talkableで **Send sample payload** を選択し、**Email opt-in** アクションが有効になっていることを確認してください。 |
| キーのローテーション後にリクエストの送信が停止した | 保存されたAPIキーがBrazeで取り消されたか、置き換えられました。 | Talkableの **App Store** でBrazeアプリを開き、新しいREST APIキーを貼り付けて **Save** を選択し、**Send sample payload** で再テストしてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="トラブルシューティング" }

Talkable連携の詳細については、[Talkable Braze連携ドキュメント](https://docs.talkable.com/email_marketing_and_automation/braze/)を参照してください。Talkableサポートへのお問い合わせは、[support@talkable.com](mailto:support@talkable.com) までメールでご連絡ください。