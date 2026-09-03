---
nav_title: 収集のベストプラクティス
article_title: 収集のベストプラクティス
page_order: 4
page_type: reference
description: "この記事では、新規および既存のユーザーデータを収集するためのさまざまな方法とベストプラクティスについて説明します。"

---

# 収集のベストプラクティス {#collection-best-practices}

> 顧客のユーザープロファイルのライフサイクルを想定する際に、既知および未知のユーザーについてユーザーデータをいつ、どのように収集すべきかを判断するのは難しい場合があります。この記事では、ユースケースを通じて、新規および既存のユーザーデータを収集するためのさまざまな方法とベストプラクティスを説明します。

以下の例はメール収集のユースケースですが、このロジックはさまざまなデータ収集シナリオに適用できます。この例では、サインアップフォームまたはユーザー情報を収集する方法がすでに連携されていることを前提としています。

ユーザーが記録するための情報を提供した後、そのデータがデータベースにすでに存在するかどうかを確認し、必要に応じてユーザーエイリアスプロファイルを作成するか、既存のユーザープロファイルを更新することをお勧めします。

未知のユーザーがサイトを閲覧し、後日アカウントを作成したり、メールサインアップで身元を明らかにした場合、プロファイルのマージは慎重に処理する必要があります。マージ方法によっては、エイリアスのみのユーザー情報や匿名データが上書きされる場合があります。

## Webフォームによるユーザーデータの取得 {#capturing-user-data-through-a-web-form}

### ステップ1：ユーザーが存在するか確認する {#step-1-check-if-the-user-exists}

ユーザーがWebフォームからコンテンツを入力した際に、そのメールアドレスを持つユーザーがデータベースに既に存在するかどうかを確認します。以下のいずれかの方法で確認できます。

- **内部データベースを確認する（推奨）：** Braze以外に提供されたユーザー情報を含む外部レコードやデータベースがある場合、メール送信やアカウント作成の時点でこれを参照し、情報が既に取得済みでないことを確認します。
- **[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)：** `email`を識別子として使用すると、そのメールアドレスがまだ存在しない場合に新しいユーザープロファイルが作成されます。
- **[`/subscription/status/get`エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status)：** カスタムフォームでメールを収集し、その後REST APIで購読グループのメンバーシップを設定する場合、まずこのエンドポイントを呼び出します。一致するプロファイルが存在しない場合は、[`/subscription/status/set`エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)でユーザーを作成または購読登録します。既にプロファイルが存在する場合は、重複を作成せず既存のプロファイルを更新します。

### ステップ2：ユーザーを記録または更新する {#step-2-log-or-update-user}

- **ユーザーが存在する場合：**
  - 新しいプロファイルを作成しないでください。
  - ユーザーのプロファイルにカスタム属性（例：`newsletter_subscribed: true`）を記録し、ユーザーがニュースレター購読フォームからメールを送信したことを示します。同じメールアドレスを持つBrazeユーザープロファイルが複数存在する場合、すべてのプロファイルがエクスポートされます。<br><br>
- **ユーザーが存在しない場合：**
  - [`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を通じてエイリアスのみのプロファイルを作成します。このエンドポイントは[`user_alias`オブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object)を受け入れ、`update_existing_only`が`false`に設定されている場合にエイリアスのみのプロファイルを作成します。ユーザーのメールアドレスをユーザーエイリアスとして設定し、将来そのユーザーを参照できるようにします（そのユーザーには`external_id`がないため）。

![エイリアスのみのユーザープロファイルを更新するプロセスを示す図。ユーザーがマーケティングランディングページでメールアドレスとカスタム属性（郵便番号）を送信します。ランディングページのデータ収集からエイリアスのみのユーザープロファイルへの矢印は、ユーザー追跡エンドポイントへのBraze APIリクエストを示しており、リクエストボディにはユーザーのエイリアス名、エイリアスラベル、メール、郵便番号が含まれています。プロファイルには「Brazeで作成されたエイリアスのみのユーザー」というラベルが付いており、リクエストボディの属性が新しく作成されたプロファイルに反映されていることを示しています。]({% image_buster /assets/img/user_profile_process3.png %}){: style="max-width:90%;"}

## メールキャプチャフォームによるユーザーメールの取得 {#capturing-user-emails-through-an-email-capture-form}

メールキャプチャフォームを使用して、ユーザーにメールアドレスの送信を促すことができます。送信されたメールアドレスはユーザープロファイルに追加されます。このフォームの設定方法について詳しくは、[メールキャプチャフォーム]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/email_capture_form)をご覧ください。

カスタムフォームを使用し、REST APIを通じて購読グループのメンバーシップを設定する場合は、ユーザーを作成する前にプロファイルがすでに存在するかどうかを確認してください。[ステップ1：ユーザーが存在するか確認する](#step-1-check-if-user-exists)を参照してください。

## エイリアスのみのユーザーを識別する {#identifying-alias-only-users}

アカウント作成時にユーザーを識別する際、エイリアスのみのユーザーは[`/users/identify`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)を使用して、エイリアスのみのユーザーを既知のプロファイルとマージすることで、識別してexternal IDを割り当てることができます。

ユーザーがエイリアスのみかどうかを確認するには、データベース内に[ユーザーが存在するかどうかを確認](#step-1-check-if-user-exists)します。
- 外部レコードが存在する場合は、`/users/identify/`エンドポイントを呼び出すことができます。
- [`/users/export/id`エンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)が`external_id`を返す場合は、`/users/identify/`エンドポイントを呼び出すことができます。
- エンドポイントが何も返さない場合は、`/users/identify/`の呼び出しは行わないでください。

## エイリアスのみのユーザー情報がすでに存在する場合のユーザーデータの取得 {#capturing-user-data-when-alias-only-user-information-is-already-present}

ユーザーがアカウントを作成したり、メール登録を通じて自身を識別したりすると、プロファイルを統合できます。統合可能なフィールドの一覧については、[統合の更新動作]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior)を参照してください。

### 重複するユーザープロファイルの統合 {#merging-duplicate-user-profiles}

ユーザーデータが増加するにつれて、Brazeダッシュボードから重複するユーザープロファイルを統合できます。これらの重複プロファイルは、同じ検索クエリを使用して見つける必要があります。ユーザープロファイルの重複を統合する方法の詳細については、[重複ユーザーの統合]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users)を確認してください。

また、[ユーザー統合エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_users_merge)を使用して、あるユーザープロファイルを別のユーザープロファイルに統合することもできます。

{% alert note %}
ユーザープロファイルが統合された後、このアクションを元に戻すことはできません。
{% endalert %}

## その他のリソース {#additional-resources}
- Brazeの[ユーザープロファイルのライフサイクル]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)に関する記事で、追加のコンテキストを確認してください。<br>
- ユーザーIDの設定と`changeUser()`メソッドの呼び出しに関するドキュメントを参照してください：[Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android)、[iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift#naming-best-practices)、[Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web)。