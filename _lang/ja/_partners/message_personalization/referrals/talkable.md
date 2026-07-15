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

Talkableは、Brazeが推進するカスタマージャーニーにアドボケイト主導のアクイジションをもたらします。この連携は、Talkableが取得したすべてのリファラルオプトインを、対応するBrazeプロファイルにリアルタイムで移動させます。これにより、ウェルカムフロー、リファラルジャーニー、セグメンテーション、ライフサイクルメッセージングを、信頼できる同意とリファラルコンテキストから起動できます。手動のリストエクスポートやバッチ同期は不要です。

Talkableは2つのシナリオでマーケティングオプトインを取得します。

* **アドボケイトのサインアップ：** アドボケイトがTalkableリファラルキャンペーンにサインアップし、マーケティングメールの受信に同意します。
* **フレンドのメールゲーティング：** フレンドがTalkableのメールゲーティングステップを完了し、マーケティングメールにオプトインします。

いずれの場合も、Talkableは対応するBrazeユーザープロファイルをリアルタイムで作成または更新し、ユーザーのメールサブスクリプション状態を**オプトイン**に設定します。

### デフォルトの動作 {#default-behavior}

Talkableは、Talkableで明示的に同意した人からの個別のオプトインイベント（キャンペーンにサインアップしたアドボケイト、またはメールゲーティング中にオプトインしたフレンド）に対してのみ、Brazeにデータを送信します。Talkableは夜間バッチ、フル同期、暗黙的なプロファイル更新を実行しません。TalkableはオプトインしていないプロファイルをBrazeに送信することはありません。

## ユースケース {#use-cases}

- アドボケイトがTalkableリファラルキャンペーンにサインアップした瞬間に、Brazeウェルカムキャンバスをトリガーします。
- フレンドがオプトインした直後に、フレンド専用のキャンバスとパーソナライズされた初回購入オファーで紹介されたフレンドをアクティベートします。
- Brazeカスタム属性として送信されるアドボケイトおよびフレンドフラグとキャンペーンメタデータを使用して、リファラルコンテキストでセグメント化します。
- コンプライアンスに準拠したニュースレター送信のために、リファラルオプトインを指定されたBrazeサブスクリプショングループにルーティングします。

## 前提条件 {#prerequisites}

開始する前に、以下が必要です。

| 前提条件 | 説明 |
| --- | --- |
| Talkableアカウント | このパートナーシップを利用するには、少なくとも1つのキャンペーンが設定されたTalkableサイトが必要です。 |
| Braze REST APIキー | `users.track`権限を持つBraze REST APIキー。このキーはBrazeダッシュボードの**設定** > **APIキー**から作成します。詳細については、[REST APIキーの作成]({{site.baseurl}}/api/basics/#creating-rest-api-keys)を参照してください。 |
| Braze RESTエンドポイント | Braze RESTエンドポイントURL（例：`https://rest.iad-01.braze.com`）。US（`.com`）およびEU（`.eu`）のBrazeクラスターの両方がサポートされています。詳細については、[REST APIエンドポイント]({{site.baseurl}}/api/basics/#endpoints)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

### ステップ 1:TalkableにBrazeアプリをインストールする {#step-1-install-the-braze-app-in-talkable}

1. Talkable管理画面にサインインしてメニューを開き、**All Site Settings** > **App Store**に移動します。
2. **Braze**を見つけて**Install**を選択します。
3. Braze RESTエンドポイントと`users.track`権限を持つREST APIキーを入力し、**Save**を選択します。

### ステップ 2:メールオプトインアクションを設定する {#step-2-configure-the-email-opt-in-action}

1. Talkable Brazeアプリで、**Email opt-in**アクションを開きます。
2. （オプション）Brazeサブスクリプショングループ識別子を入力し、カスタム属性を追加し、ユーザーエイリアスを設定します。詳細については、[Talkableのカスタマイズ](#customizing-talkable)を参照してください。
3. **Save**を選択します。ライブのオプトインイベントが同期を開始する前にテストペイロードで設定を確認できるよう、アクションは無効のままにしておきます。

### ステップ 3:サンプルペイロードでテストする {#step-3-test-with-a-sample-payload}

1. Talkableで、**Email opt-in**アクションの**Send sample payload**を選択して、Brazeにテストリクエストを送信します。
2. Brazeで、**オーディエンス** > **ユーザー検索**に移動し、テストメールアドレスで検索します。
3. プロファイルが存在し、**メール購読**が**オプトイン**に設定されていること、および設定したカスタム属性、サブスクリプショングループ登録、またはユーザーエイリアスが期待どおりに表示されていることを確認します。

### ステップ 4:ライブトラフィックに対してアクションを有効にする {#step-4-enable-the-action-for-live-traffic}

Brazeでテストプロファイルが正しく表示されたら、Talkableに戻り、**Email opt-in**アクションを有効にします。

この時点から、すべてのTalkableオプトインイベントが対応するプロファイルをリアルタイムでBrazeに同期します。

## Brazeに送信されるデフォルトのユーザー属性 {#default-user-attributes-sent-to-braze}

すべてのオプトインイベントで、Talkableは以下の標準Brazeユーザー属性を使用して、対応するBrazeユーザープロファイルを作成または更新します。空の値は省略されます。

| Braze属性 | タイプ | 備考 |
| --- | --- | --- |
| `email_subscribe` | 文字列 | すべてのTalkableオプトインイベントで**オプトイン**に設定されます。 |
| `email` | 文字列 | Brazeプロファイルの照合に使用されるプライマリ識別子です。 |
| `phone` | 文字列 | ユーザー属性としてのみ取得されます。BrazeはE.164形式を想定しています。Talkableに保存されたとおりに送信されます。 |
| `first_name` | 文字列 | 名です。 |
| `last_name` | 文字列 | 姓です。 |
| サブスクリプショングループ登録 | 該当なし | サブスクリプショングループが設定されている場合にのみ追加されます。ユーザーは購読済みとして登録されます。 |
| ユーザーエイリアス | 該当なし | ユーザーエイリアスが設定されている場合にのみ追加されます。詳細については、[Talkableのカスタマイズ](#customizing-talkable)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Brazeに送信されるデフォルトのユーザー属性" }

## Talkableのカスタマイズ {#customizing-talkable}

以下のオプションのカスタマイズが利用可能です。任意の組み合わせで設定できます。それぞれ独立しています。

### オプトインをBrazeサブスクリプショングループに登録する {#enroll-opt-ins-in-a-braze-subscription-group}

1. Brazeで、**オーディエンス** > **購読グループ管理**からサブスクリプショングループIDをコピーします。詳細については、[ユーザーサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/)を参照してください。
2. Talkableの**Email opt-in**アクションで、**Subscription group identifier**フィールドに貼り付けます。

Talkableは各オプトインをそのサブスクリプショングループに購読済みとして登録し、リファラルオプトインをグローバルサブスクリプションではなくそのグループにスコープします。Talkableはサブスクリプションの追加のみを行い、削除は行いません。

### カスタム属性を送信する {#send-custom-attributes}

アクションのペイロードエディターに任意のキーと値のペアを追加します。入力したキーがBrazeユーザープロファイルの属性名になります。

値はLiquidテンプレートです。以下の変数が利用可能です。

{% raw %}
| 変数 | 内容 |
| --- | --- |
| `{{ person }}` | オプトインしたアドボケイトまたはフレンド（`email`、`first_name`、`last_name`、`phone_number`、`username`、`is_advocate`、`custom_properties`など）。 |
| `{{ ip }}` | オプトインが発生したIPアドレス。 |
| `{{ campaign }}` | 元のTalkableキャンペーン（`name`、`type`、`tag_names`など）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquidテンプレート変数" }
{% endraw %}

{% raw %}
例：`talkable_is_advocate` = `{{ person.is_advocate }}`と`talkable_campaign_name` = `{{ campaign.name }}`を追加して、Brazeでリファラルコンテキストによるセグメント化を行います。
{% endraw %}

### Brazeユーザーエイリアスでユーザーを識別する {#identify-users-with-braze-user-aliases}

ペイロードエディターで、`user_alias.alias_name`（例：{% raw %}`{{ person.username }}`{% endraw %}）と`user_alias.alias_label`（例：`username`）を追加します。詳細については、[ユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object/)を参照してください。

両方のフィールドが存在する場合、システムはメールに加えてエイリアスでもユーザーを識別し、一致するものがない場合はBrazeが新しいエイリアス付きプロファイルを作成します。

{% alert note %}
両方のエイリアスフィールドが必須です。`alias_name`または`alias_label`のいずれか一方のみが設定されている場合、Talkableはユーザーエイリアスを送信せず、プロファイルはメールのみで照合されます。
{% endalert %}

## Brazeでのユーザーの検索と作成 {#find-and-create-users-in-braze}

* デフォルトでは、Brazeはメールアドレスでプロファイルを照合します。一致するプロファイルが存在しない場合、Brazeは新しいプロファイルを作成します。
* ユーザーエイリアスが設定されている場合、Brazeはそのエイリアスでも照合し、一致するものがない場合は新しいエイリアス付きプロファイルを作成します。
* この連携ではexternal IDは使用されません。Talkableオプトインを既存の外部識別済みプロファイルに紐付けるには、そのプロファイルの既知のエイリアスと一致するラベルを持つユーザーエイリアスを設定してください。

## BrazeでTalkableを使用する {#use-talkable-with-braze}

### 同期されたユーザーを検索する {#find-a-synced-user}

**オーディエンス** > **ユーザー検索**に移動し、メールで検索して、Talkableが作成または更新したプロファイルを表示します。

標準フィールド（メール、電話番号、名、姓）および設定したカスタム属性がプロファイルに表示されます。**メール購読**は**オプトイン**と表示されます。

### リファラルセグメントを構築する {#build-a-referral-segment}

1. **メール購読**が**オプトイン**であるフィルターでセグメントを作成します。
2. Talkableが送信するカスタム属性で絞り込みます。例えば、`talkable_is_advocate`が`true`に等しい場合はアドボケイトをターゲットにし、`talkable_campaign_name`がキャンペーン名に等しい場合は特定のリファラルプログラムをターゲットにします。

### ライフサイクルメッセージングをトリガーする {#trigger-lifecycle-messaging}

1. アクションベースの配信でキャンバスまたはキャンペーンを構築します。この連携では以下のBrazeトリガータイプが機能します。
* **サブスクリプションステータスの更新**（例：メールサブスクリプションが**オプトイン**になった場合）
* **サブスクリプショングループステータスの更新**（サブスクリプショングループが設定されている場合）
* **カスタム属性値の変更**（送信するTalkableカスタム属性に対して）。
2. プロファイル上のTalkableカスタム属性（キャンペーン名、報酬値、紹介者など）でメッセージをパーソナライズします。

## 考慮事項 {#considerations}

* **メールオプトインのみ：** 電話番号は標準ユーザー属性として取得されますが、この連携ではSMSサブスクリプション状態は設定されません。TalkableはSMSオプトインを同期しません。
* **電話番号の形式：** Brazeは国際（E.164）形式の電話番号を想定しています。
* **リアルタイムのイベント駆動型同期：** Talkableはオプトインイベントごとに1つのリクエストを送信します（リクエストごとに1ユーザー）。バッチ処理や定期的なフル同期はありません。ボリュームはリファラルオプトインのボリュームに連動します。
* **信頼性の高い配信：** Brazeが一時的にエラーを返した場合、Talkableは自動的にリトライします。永続的な障害が発生した場合、サイト管理者にメールアラートが送信されます。

## トラブルシューティング {#troubleshooting}

| エラー | 考えられる原因 | 修正方法 |
| --- | --- | --- |
| 401 Unauthorized | REST APIキーに`users.track`権限がないか、エンドポイントが間違ったクラスターを指しています。 | `users.track`権限を持つキーを再発行し、RESTエンドポイントがBrazeクラスターと一致していることを確認してください。 |
| インストール時にRESTエンドポイントが拒否された | URLがBraze RESTエンドポイントではありません。 | クラスターのRESTエンドポイントを使用してください（例：`https://rest.iad-01.braze.com`）。ダッシュボードURLは機能しません。 |
| プロファイルは作成されたがサブスクリプショングループに含まれていない | サブスクリプショングループIDが設定されていません。 | **Email opt-in**アクションにサブスクリプショングループIDを入力してください。 |
| ユーザーエイリアスが適用されない | 2つのエイリアスフィールド（名前またはラベル）のうち1つのみが入力されています。 | アクションに両方のフィールド（エイリアス名とエイリアスラベル）を入力してください。 |
| プロファイルが表示されない | サンプルリクエストがまだ送信されていないか、アクションが無効になっています。 | Talkableで**Send sample payload**を選択し、**Email opt-in**アクションが有効になっていることを確認してください。 |
| キーのローテーション後にリクエストの送信が停止した | 保存されたAPIキーがBrazeで取り消されたか置き換えられました。 | Talkableの**App Store**でBrazeアプリを開き、新しいREST APIキーを貼り付けて**Save**を選択し、**Send sample payload**で再テストしてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="トラブルシューティング" }

Talkable連携の詳細については、[Talkable Braze連携ドキュメント](https://docs.talkable.com/email_marketing_and_automation/braze/)を参照してください。Talkableサポートへのお問い合わせは、[support@talkable.com](mailto:support@talkable.com)までメールしてください。