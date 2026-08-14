---
nav_title: ユーザープロファイルのライフサイクル
article_title: ユーザープロファイルのライフサイクル
page_order: 2
page_type: reference
description: "このリファレンス記事では、Brazeのユーザープロファイルのライフサイクルと、ユーザープロファイルを識別して参照するさまざまな方法について説明します。"

---

# ユーザープロファイルのライフサイクル {#user-profile-lifecycle}

> この記事では、Brazeユーザープロファイルのライフサイクルと、ユーザープロファイルを識別および参照するさまざまな方法について説明します。カスタマーライフサイクルをより詳しく理解したい場合は、[ユーザーライフサイクルのマッピング](https://learning.braze.com/mapping-customer-lifecycles)に関するBrazeラーニングコースをご覧ください。

ユーザーに関連付けられるすべての永続データは、そのユーザープロファイルに保存されます。APIを使用してユーザープロファイルが作成された後、またはSDKによりユーザーが認識された後に、そのユーザーを識別および参照するために、そのプロファイルに多数のパラメーターを割り当てることができます。

これらのパラメーターには以下のものが含まれます。

* `braze_id`（Brazeにより割り当て）
* `external_id`
* `email`
* `phone`
* 設定した任意の数のカスタムユーザーエイリアス

## 匿名ユーザープロファイル {#anonymous-user-profiles}

`external_id`が指定されていないユーザーは、[匿名ユーザー]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users)と呼ばれます。例えば、Webサイトを訪問したがサインアップしなかったユーザーや、モバイルアプリをダウンロードしたがプロファイルを作成しなかったユーザーが該当します。

最初にSDKがユーザーを認識すると、関連する`braze_id`を持つ匿名ユーザープロファイルが作成されます。`braze_id`はBrazeによって自動的に割り当てられる一意の識別子で、編集できず、デバイス固有のものです。この識別子は、[API]({{site.baseurl}}/api/endpoints/user_data)を通じてユーザープロファイルを更新するために使用できます。

## 識別済みユーザープロファイル {#identified-user-profiles}

アプリ内でユーザーが認識可能になった後（ユーザーIDやメールアドレスなどの形式を提供することで）、`changeUser`メソッド（[Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)、[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:))、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html)）を使用して、そのユーザーのプロファイルに`external_id`を割り当てることをお勧めします。`external_id`を使用すると、複数のデバイスにわたって同じユーザープロファイルを識別できます。

`external_id`を使用する追加のメリットには、以下が含まれます。

- 複数のデバイスやプラットフォームにわたって一貫したユーザー体験を提供します（例えば、iPhoneアプリのロイヤルユーザーに対して、Androidタブレットに離脱ユーザー向け通知を送信しないなど）。
- ユーザーがアプリをアンインストールして再インストールしたり、別のデバイスにインストールしたりするたびに新しいユーザープロファイルを作成していないことを確認し、分析の精度を向上させます。
- [ユーザーデータエンドポイント]({{site.baseurl}}/api/endpoints/user_data)を使用してアプリ外のソースからユーザーデータをインポートしたり、[メッセージングエンドポイント]({{site.baseurl}}/api/endpoints/messaging)を使用してトランザクションメッセージでユーザーをターゲットにしたりできます。
- セグメンターの「テスト」[フィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)や、[**ユーザー検索**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles)ページで個々のユーザーを検索できます。

### external IDに関する考慮事項 {#considerations-for-external-ids}

{% multi_lang_include alerts/warning_alerts.md alert='User profile external_id' %}

#### メールアドレスまたはハッシュ化されたメールアドレスをexternal IDとして使用するリスク {#risk-of-using-an-email-or-hashed-email-as-an-external-id}

メールアドレスまたはハッシュ化されたメールアドレスをBrazeのexternal IDとして使用すると、データソース間のID管理を簡素化できます。ただし、ユーザーのプライバシーとデータセキュリティに対する潜在的なリスクを考慮することが重要です。

- **推測可能な情報：**メールアドレスは容易に推測できるため、攻撃に対して脆弱です。
- **悪用のリスク：**悪意のあるユーザーがWebブラウザを改変して他人のメールアドレスを自分のexternal IDとして送信した場合、機密性の高いメッセージやアカウント情報にアクセスされる可能性があります。

### 匿名ユーザーを識別した場合の動作 {#what-happens-when-you-identify-anonymous-users}

匿名ユーザーを識別する際には、2つのシナリオのいずれかが発生する可能性があります。

1) **匿名ユーザーが新しい識別済みユーザーになる場合：**<br>Brazeに`external_id`がまだ存在しない場合、匿名ユーザーは新しい識別済みユーザーになり、匿名ユーザーのすべての属性と履歴がそのまま保持されます。

2) **匿名ユーザーが既存のユーザーとして識別される場合：**<br>Brazeに`external_id`がすでに存在する場合、そのユーザーは別のデバイス（タブレットなど）やインポートされたユーザーデータなど、他の方法でシステム内のユーザーとして以前に識別されています。

つまり、このユーザーのユーザープロファイルはすでに存在しています。この場合、Brazeは以下の処理を行います。
1. 匿名ユーザーを孤立させる
2. 匿名プロファイルから、識別済みユーザープロファイルにまだ存在しない[特定のユーザープロファイルフィールド]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior)をマージする
3. ユーザー数が水増しされないように、匿名プロファイルをユーザー群から削除する

匿名ユーザーと既知のユーザーの両方に名がある場合、既知のユーザーの名が維持されます。既知のユーザーの値がnullで匿名ユーザーに値がある場合、その値がこれらの[特定のユーザープロファイルフィールド]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior)に該当する場合は、匿名ユーザーの値が既知のユーザーのプロファイルにマージされます。

{% alert important %}
匿名プロファイルからすべてのデータがマージされるわけではありません。プッシュトークンとメッセージング履歴は引き継がれ、匿名プロファイルのカスタム属性、カスタムイベント、購入履歴は、識別済みユーザープロファイルにそれらのフィールドがまだ存在しない場合にのみマージされます。データが競合する場合は、識別済みユーザーの値が保持されます。転送されるフィールドと転送されないフィールドの完全なリストについては、[マージの動作]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior)を参照してください。
{% endalert %}

ユーザープロファイルに`external_id`を設定する方法については、ドキュメント（[iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift)、[Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android)、[Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web)）を参照してください。

{% alert note %}
孤立したユーザーはメッセージを受信する資格がありません。
{% endalert %}

### 重複ユーザーのマージ {#merging-duplicate-users}

ワークスペース内で重複するユーザープロファイルを特定した場合、REST APIを使用してマージできます。ユーザーのマージと利用可能な方法の詳細については、[重複ユーザーのマージ]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users)を参照してください。

## ユーザーエイリアス {#user-aliases}

Brazeの`external_id`以外の識別子でユーザーを参照するには、ユーザープロファイルに対してユーザーエイリアスを設定します。ユーザープロファイルに設定されたエイリアスは、ユーザーの`braze_id`や`external_id`を置き換えるのではなく、それらに加えて機能します。ユーザープロファイルに設定できるエイリアスの数に制限はありません。

各エイリアスはキーと値のペアとして機能し、2つの部分で構成されます。エイリアスのキーを定義する`alias_label`と、値を定義する`alias_name`です。任意の単一ラベルに対する`alias_name`は、ユーザー群全体で一意でなければなりません（`external_id`と同様です）。既存のラベルと名前の組み合わせで2番目のユーザープロファイルを更新しようとしても、そのユーザープロファイルは更新されません。

### ユーザーエイリアスの更新 {#updating-user-aliases}

エイリアスは、設定後に[ユーザーデータエンドポイント]({{site.baseurl}}/developer_guide/rest_api/user_data#new-user-alias-endpoint)を使用するか、SDKを通じて新しい名前を渡すことで、指定されたラベルに対して新しい名前に更新できます。更新されたユーザーエイリアスは、そのユーザーのデータをエクスポートする際に表示されます。

![同じユーザーエイリアスラベルを持つが、異なるエイリアス名を持つ別々のユーザーの2つの異なるユーザープロファイル]({% image_buster /assets/img_archive/Braze_User_aliases.png %})

### 匿名ユーザーへのタグ付け {#tagging-anonymous-users}

ユーザーエイリアスを使用すると、匿名ユーザーに識別子をタグ付けすることもできます。たとえば、ユーザーがeコマースサイトにメールアドレスを提供したがまだサインアップしていない場合、そのメールアドレスをその匿名ユーザーのエイリアスとして使用できます。これらのユーザーは、エイリアスを使用してエクスポートしたり、APIで参照したりできます。

### 匿名ユーザープロファイルでのエイリアスの動作 {#behavior-of-aliases-on-anonymous-user-profiles}

エイリアスを持つ匿名ユーザープロファイルが後で`external_id`で識別された場合、通常の識別済みユーザープロファイルとして扱われますが、既存のエイリアスは保持され、引き続きそのエイリアスで参照できます。

### ユーザーエイリアスの検索 {#searching-for-a-user-alias}

ユーザーのエイリアス名とラベルがわかっている場合、**ユーザー検索**で`alias_label:alias_name`の形式を使用してユーザーを見つけることができます。たとえば、名前が`alias_name: bobby_alias`でラベルが`alias_label: m4pzOndtA-CnO0u`のエイリアスのみのプロファイルがある場合、`m4pzOndtA-CnO0u:bobby_alias`と入力してこのユーザーを見つけることができます。

この情報がわからない場合は、[`Export user profile by identifier`エンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)を呼び出し、APIレスポンスでユーザーエイリアスを確認できます。

### 既知のユーザープロファイルへのエイリアスの設定 {#setting-aliases-on-known-user-profiles}

ユーザーエイリアスは、既知のユーザープロファイルにも設定でき、既知のユーザーを別の外部既知IDで参照できます。たとえば、ユーザーがBraze内で参照したいビジネスインテリジェンスツールID（Amplitude IDなど）を持っている場合があります。

ユーザーエイリアスの設定方法については、各プラットフォームのドキュメントを参照してください（[iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids#aliasing-users)、[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids#aliasing-users)、[Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#aliasing-users)）。

![Brazeにおけるユーザープロファイルのライフサイクルのフローチャート。匿名ユーザーに対してchangeUser()が呼び出されると、そのユーザーは識別済みユーザーとなり、データは識別済みユーザープロファイルに移行されます。識別済みユーザーにはBraze IDとexternal IDがあります。この時点で、2番目の匿名ユーザーに対してchangeUser()が呼び出されると、識別済みユーザーにまだ存在しないユーザーデータフィールドがマージされます。識別済みユーザーの既存のユーザープロファイルにエイリアスが追加された場合、データには影響しませんが、エイリアス付きの識別済みユーザーとなります。識別済みユーザーと同じエイリアスラベルを持つが異なるエイリアス名を持つ3番目の匿名ユーザーに対してchangeUser()が呼び出されると、識別済みユーザーに存在しないフィールドがマージされ、識別済みユーザープロファイルのエイリアスラベルは維持されます。]({% image_buster /assets/img_archive/Braze_User_flowchart.png %})

{% alert tip %}
顧客のユーザープロファイルライフサイクルでこれがどのように見えるかイメージしにくい場合は、[ベストプラクティス]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices)にアクセスして、ユーザーデータ収集のベストプラクティスをご確認ください。
{% endalert %}

## 高度なユースケース {#advanced-use-case}

SDKおよびAPIの[ユーザーデータエンドポイント]({{site.baseurl}}/developer_guide/rest_api/user_data#new-user-alias-endpoint)を使用して、既存の識別済みユーザープロファイルに新しいユーザーエイリアスを設定できます。ただし、既存の不明なユーザープロファイルに対しては、APIを通じてユーザーエイリアスを設定することはできません。

ユーザーエイリアスもマージプロセスで統合されます。ただし、孤立させるユーザーとターゲットユーザーの両方が同じラベルのエイリアスを持っている場合、ターゲットユーザーのエイリアスのみが維持されます。

アプリをアンインストールして再インストールすると、そのユーザーに対して新しい匿名の`braze_id`が生成されます。

### ユーザーIDによるトラブルシューティング {#troubleshooting-with-user-ids}

すべてのユーザーIDを使用して、テスト目的でダッシュボード内のユーザーを検索および識別できます。Brazeダッシュボードでユーザーを検索するには、[テストユーザーの追加]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users)を参照してください。

{% alert important %}
Brazeは、異常に大きくなったユーザープロファイル（「ダミーユーザー」）をブロックします。これらのプロファイルは通常、統合の誤りが原因です。プロファイルは、以下のいずれかのしきい値を超えるとブロックされます。

- セッション数が5,000,000を超える
- 個別のカスタムイベント名が20,000を超える
- 購入における個別の商品名が20,000を超える

プロファイルがブロックされると、BrazeはSDKおよびREST APIの両方からそのプロファイルへのすべての受信データの取り込みを停止します。正当なユーザーにこの問題が発生した場合は、Brazeアカウントマネージャーにお問い合わせください。詳細については、[スパムブロック]({{site.baseurl}}/user_archival)を参照してください。
{% endalert %}