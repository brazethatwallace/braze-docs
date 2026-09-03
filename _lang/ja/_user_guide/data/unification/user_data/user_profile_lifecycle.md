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

最初にSDKがユーザーを認識すると、関連付けられた`braze_id`を持つ匿名ユーザープロファイルが作成されます。`braze_id`はBrazeによって自動的に割り当てられる一意の識別子で、編集することはできず、デバイス固有のものです。この識別子は、[API]({{site.baseurl}}/api/endpoints/user_data)を通じてユーザープロファイルを更新するために使用できます。

## 識別済みユーザープロファイル {#identified-user-profiles}

アプリでユーザーを認識できるようになったら（ユーザーIDやメールアドレスなどの情報を提供した場合）、`changeUser`メソッド（[Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)、[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:))、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html)）を使用して、そのユーザーのプロファイルに`external_id`を割り当てることをお勧めします。`external_id`を使用すると、複数のデバイス間で同じユーザープロファイルを識別できます。

`external_id`を使用するその他のメリットには、以下のようなものがあります。

- 複数のデバイスやプラットフォーム間で一貫したユーザー体験を提供できます（例えば、iPhoneアプリのロイヤルユーザーに対して、AndroidタブレットでユーザーのRest離脱通知を送信しないなど）。
- ユーザーがアプリをアンインストールして再インストールしたり、別のデバイスにインストールしたりするたびに新しいユーザープロファイルを作成していないことを確認し、分析の精度を向上させます。
- [ユーザーデータエンドポイント]({{site.baseurl}}/api/endpoints/user_data)を使用してアプリ外のソースからユーザーデータをインポートしたり、[メッセージングエンドポイント]({{site.baseurl}}/api/endpoints/messaging)を使用してトランザクションメッセージでユーザーをターゲットにしたりできます。
- セグメンターの「テスト」[フィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)や、[**ユーザー検索**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles)ページで個々のユーザーを検索できます。

### external IDに関する考慮事項 {#considerations-for-external-ids}

{% multi_lang_include alerts/warning_alerts.md alert='User profile external_id' %}

#### メールまたはハッシュ化されたメールをexternal IDとして使用するリスク {#risk-of-using-an-email-or-hashed-email-as-an-external-id}

メールアドレスまたはハッシュ化されたメールアドレスをBrazeのexternal IDとして使用すると、データソース間のID管理を簡素化できます。ただし、ユーザーのプライバシーとデータセキュリティに対する潜在的なリスクを考慮することが重要です。

- **推測可能な情報:** メールアドレスは容易に推測できるため、攻撃に対して脆弱です。
- **悪用のリスク:** 悪意のあるユーザーがWebブラウザーを変更して、他人のメールアドレスを自分のexternal IDとして送信した場合、機密性の高いメッセージやアカウント情報にアクセスできる可能性があります。

### 匿名ユーザーを識別した場合の動作 {#what-happens-when-you-identify-anonymous-users}

匿名ユーザーを識別する際には、以下の2つのシナリオのいずれかが発生する可能性があります。

1) **匿名ユーザーが新しい識別済みユーザーになる:** <br>Brazeに`external_id`がまだ存在しない場合、匿名ユーザーは新しい識別済みユーザーになり、匿名ユーザーのすべての属性と履歴をそのまま保持します。

2) **匿名ユーザーが既存のユーザーとして識別される:** <br>Brazeに`external_id`がすでに存在する場合、そのユーザーは別のデバイス（タブレットなど）やインポートされたユーザーデータなど、他の方法でシステム内ですでに識別されています。

つまり、そのユーザーのユーザープロファイルはすでに存在しています。この場合、Brazeは以下の処理を行います。
1. 匿名ユーザーをオーファン化する
2. 匿名プロファイルから、識別済みユーザープロファイルにまだ存在しない[特定のユーザープロファイルフィールド]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior)をマージする
3. ユーザー数が膨らまないように、匿名プロファイルをユーザー群から削除する

匿名ユーザーと既知のユーザーの両方に名がある場合、既知のユーザーの名が維持されます。既知のユーザーの値がnullで匿名ユーザーに値がある場合、その値がこれらの[特定のユーザープロファイルフィールド]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior)に該当する場合、匿名ユーザーの値が既知のユーザーのプロファイルにマージされます。

{% alert important %}
匿名プロファイルからすべてのデータがマージされるわけではありません。プッシュトークンとメッセージング履歴は引き継がれ、匿名プロファイルのカスタム属性、カスタムイベント、購入履歴は、識別済みユーザープロファイルにそれらのフィールドがまだ存在しない場合にのみマージされます。データが競合する場合は、識別済みユーザーの値が保持されます。転送されるフィールドと転送されないフィールドの完全なリストについては、[マージ動作]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior)を参照してください。
{% endalert %}

ユーザープロファイルに`external_id`を設定する方法については、ドキュメント（[iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift)、[Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android)、[Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web)）を参照してください。

### レポートとマージされたプロファイル {#reporting-and-merged-profiles}

送信後に匿名プロファイルと識別済みプロファイルがマージされた場合、ダッシュボードのキャンペーンサマリーはその送信を存続する（識別済み）プロファイルに帰属させます。[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)、[クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder)、および[メッセージング履歴]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab)タブでは、送信はオーファン化されたプロファイルのユーザーID（送信時のID）に帰属されたままです。これは想定される動作です。転送されるフィールドの完全なリストについては、[マージ動作]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior)を参照してください。

Currents、クエリビルダー、またはメッセージング履歴でその送信を見つけるには、オーファン化されたプロファイルの`braze_id`で検索してください。識別済みユーザーの`braze_id`のみを使用するクエリでは、マージ前の送信は返されません。

{% alert note %}
オーファン化されたユーザーはメッセージを受信する資格がありません。
{% endalert %}

### 重複ユーザーのマージ {#merging-duplicate-users}

ワークスペースで重複するユーザープロファイルを特定した場合、REST APIを使用してそれらをマージできます。ユーザーのマージと利用可能な方法の詳細については、[重複ユーザーのマージ]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users)を参照してください。

## ユーザーエイリアス {#user-aliases}

Brazeの`external_id`以外の識別子でユーザーを参照するには、ユーザープロファイルにユーザーエイリアスを設定します。ユーザープロファイルに設定されたエイリアスは、ユーザーの`braze_id`や`external_id`を置き換えるのではなく、それらに加えて機能します。ユーザープロファイルに設定できるエイリアスの数に制限はありません。

各エイリアスはキーと値のペアとして機能し、2つの部分で構成されます。エイリアスのキーを定義する`alias_label`と、値を定義する`alias_name`です。任意のラベルに対する`alias_name`は、ユーザー群全体で一意でなければなりません（`external_id`と同様です）。既存のラベルと名前の組み合わせを使用して2番目のユーザープロファイルを更新しようとしても、そのユーザープロファイルは更新されません。

### ユーザーエイリアスの更新 {#updating-user-aliases}

エイリアスは、設定後に[ユーザーデータエンドポイント]({{site.baseurl}}/api/endpoints/user_data)を使用するか、SDKを通じて新しい名前を渡すことで、特定のラベルに対して新しい名前に更新できます。その後、ユーザーのデータをエクスポートする際にユーザーエイリアスが表示されます。

![同じユーザーエイリアスラベルを持ちながら異なるエイリアス名が設定されている、異なるユーザーの2つのユーザープロファイル]({% image_buster /assets/img_archive/Braze_User_aliases.png %})

### 匿名ユーザーへのタグ付け {#tagging-anonymous-users}

ユーザーエイリアスを使用すると、匿名ユーザーに識別子をタグ付けすることもできます。たとえば、ユーザーがeコマースサイトにメールアドレスを提供したもののまだサインアップしていない場合、そのメールアドレスを匿名ユーザーのエイリアスとして使用できます。これらのユーザーは、エイリアスを使用してエクスポートしたり、APIで参照したりできます。

### 匿名ユーザープロファイルでのエイリアスの動作 {#behavior-of-aliases-on-anonymous-user-profiles}

エイリアスを持つ匿名ユーザープロファイルが後で`external_id`で識別された場合、通常の識別済みユーザープロファイルとして扱われますが、既存のエイリアスは保持され、引き続きそのエイリアスで参照できます。

### ユーザーエイリアスの検索 {#searching-for-a-user-alias}

ユーザーのエイリアス名とラベルがわかっている場合、**ユーザー検索**で`alias_label:alias_name`の形式を使用してユーザーを検索できます。たとえば、名前が`alias_name: bobby_alias`でラベルが`alias_label: m4pzOndtA-CnO0u`のエイリアスのみのプロファイルがある場合、`m4pzOndtA-CnO0u:bobby_alias`と入力することでこのユーザーを見つけることができます。

この情報がわからない場合は、[`Export user profile by identifier`エンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)を呼び出し、APIレスポンスからユーザーエイリアスを確認できます。

### 既知のユーザープロファイルへのエイリアスの設定 {#setting-aliases-on-known-user-profiles}

ユーザーエイリアスは、既知のユーザープロファイルにも設定して、外部で既知の別のIDで既知のユーザーを参照できます。たとえば、ユーザーがBraze内で参照したいビジネスインテリジェンスツールのID（Amplitude IDなど）を持っている場合があります。

ユーザーエイリアスの設定方法については、各プラットフォームのドキュメントを参照してください（[iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift)、[Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android)、[Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web)）。

![Brazeにおけるユーザープロファイルのライフサイクルを示すフローチャート。匿名ユーザーに対してchangeUser()が呼び出されると、そのユーザーは識別済みユーザーとなり、データは識別済みユーザープロファイルに移行されます。識別済みユーザーにはBraze IDとexternal IDがあります。この時点で、2番目の匿名ユーザーにchangeUser()が呼び出された場合、識別済みユーザーにまだ存在しないユーザーデータフィールドがマージされます。識別済みユーザーの既存のユーザープロファイルにエイリアスが追加された場合、データには影響しませんが、エイリアス付きの識別済みユーザーとなります。識別済みユーザーと同じエイリアスラベルを持つが異なるエイリアス名を持つ3番目の匿名ユーザーにchangeUser()が呼び出された場合、識別済みユーザーに存在しないフィールドがマージされ、識別済みユーザープロファイルのエイリアスラベルは維持されます。]({% image_buster /assets/img_archive/Braze_User_flowchart.png %})

{% alert tip %}
お客様のユーザープロファイルのライフサイクルでこれがどのように見えるかイメージしにくい場合は、[ベストプラクティス]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices)でユーザーデータ収集のベストプラクティスをご確認ください。
{% endalert %}

## 高度なユースケース {#advanced-use-case}

SDKおよびAPIの[ユーザーデータエンドポイント]({{site.baseurl}}/api/endpoints/user_data)を使用して、既存の識別済みユーザープロファイルに新しいユーザーエイリアスを設定できます。ただし、既存の不明なユーザープロファイルに対してAPIを介してユーザーエイリアスを設定することはできません。

ユーザーエイリアスもマージプロセスで統合されます。ただし、孤立化されるユーザーとターゲットユーザーの両方が同じラベルのエイリアスを持っている場合、ターゲットユーザーのエイリアスのみが維持されます。

アプリをアンインストールして再インストールすると、そのユーザーに対して新しい匿名の`braze_id`が生成されます。

### ユーザーIDによるトラブルシューティング {#troubleshooting-with-user-ids}

すべてのユーザーIDは、テストのためにダッシュボード内でユーザーを検索・識別するために使用できます。Brazeダッシュボードでユーザーを検索するには、[テストユーザーの追加]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users)を参照してください。

{% alert important %}
Brazeは、異常に大きくなったユーザープロファイル（「ダミーユーザー」）をブロックします。これらのプロファイルは通常、統合の不備によるものです。プロファイルが以下のいずれかのしきい値を超えるとブロックされます。

- セッション数が5,000,000を超える
- 一意のカスタムイベント名が20,000を超える
- 購入における一意の製品名が20,000を超える

プロファイルがブロックされると、Brazeはそのプロファイルへのすべてのインバウンドデータ（SDKおよびREST APIの両方から）の取り込みを停止します。これが正当なユーザーに発生した場合は、Brazeアカウントマネージャーにお問い合わせください。詳細については、[スパムブロック]({{site.baseurl}}/user_archival)を参照してください。
{% endalert %}