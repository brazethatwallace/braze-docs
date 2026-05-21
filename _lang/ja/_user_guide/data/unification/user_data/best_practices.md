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

## Webフォームを使用したユーザーデータのキャプチャ {#capturing-user-data-through-a-web-form}

### ステップ1: ユーザーが存在するかどうかの確認 {#step-1-check-if-user-exists}

ユーザーがWebフォームからコンテンツを入力したら、そのメールアドレスを持つユーザーがデータベース内にすでに存在するかどうかを確認します。これは、次の2つの方法のいずれかで実行できます。

- **内部データベースのチェック（推奨）：** 提供されたユーザー情報を含む外部レコードまたはデータベースがBrazeの外部に存在する場合は、メール送信時またはアカウント作成時にそれを参照して、情報がまだキャプチャされていないことを確認してください。
- **[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)：** 識別子として`email`を使用します。メールアドレスがまだ存在しない場合は、新しいユーザープロファイルが作成されます。

### ステップ2: ユーザーの記録または更新 {#step-2-log-or-update-user}

- **ユーザーが存在する場合：**
  - 新しいプロファイルを作成しないでください。
  - ユーザーのプロファイルにカスタム属性（例：`newsletter_subscribed: true`）を記録して、ユーザーがニュースレターのサブスクリプションを通じてメールを送信したことを示します。同じメールアドレスを持つ複数のBrazeユーザープロファイルが存在する場合、すべてのプロファイルがエクスポートされます。<br><br>
- **ユーザーが存在しない場合：**
  - [`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を使用してエイリアスのみのプロファイルを作成します。このエンドポイントは[`user_alias`オブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object/)を受け入れ、`update_existing_only`が`false`に設定されている場合にエイリアスのみのプロファイルを作成します。ユーザーのメールアドレスをユーザーエイリアスとして設定し、今後そのユーザーを参照できるようにします（ユーザーには`external_id`がないため）。

![エイリアスのみのユーザープロファイルを更新するプロセスを示す図。ユーザーがマーケティングのランディングページでメールアドレスとカスタム属性（郵便番号）を送信します。ランディングページの収集からエイリアスのみのユーザープロファイルを指す矢印は、ユーザー追跡エンドポイントに対するBraze APIリクエストを示しています。リクエスト本文にはユーザーのエイリアス名、エイリアスラベル、メールアドレス、および郵便番号が含まれます。プロファイルには「Brazeで作成されたエイリアスのみのユーザー」というラベルとリクエスト本文の属性があり、新規作成されたプロファイルに反映されるデータを示しています。]({% image_buster /assets/img/user_profile_process3.png %}){: style="max-width:90%;"}

## メールキャプチャフォームを使用したユーザーメールアドレスのキャプチャ {#capturing-user-emails-through-an-email-capture-form}

メールキャプチャフォームを使用して、ユーザーにメールアドレスの送信を促し、ユーザープロファイルに追加します。このフォームの設定方法の詳細については、[メールキャプチャフォーム]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/email_capture_form/)を参照してください。

## エイリアスのみのユーザーの識別 {#identifying-alias-only-users}

アカウント作成時にユーザーを識別する場合、[`/users/identify`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)を使用して、エイリアスのみのユーザーを既知のプロファイルとマージすることにより、エイリアスのみのユーザーを識別してexternal IDを割り当てることができます。

ユーザーがエイリアスのみかどうかを確認するには、データベース内に[ユーザーが存在するかどうかを確認](#step-1-check-if-user-exists)します。
- 外部レコードが存在する場合は、`/users/identify/`エンドポイントを呼び出すことができます。
- [`/users/export/id`エンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)が`external_id`を返す場合、`/users/identify/`エンドポイントを呼び出すことができます。
- エンドポイントが何も返さない場合、`/users/identify/`呼び出しを行うべきではありません。

## エイリアスのみのユーザー情報がすでに存在する場合のユーザーデータのキャプチャ {#capturing-user-data-when-alias-only-user-information-is-already-present}

ユーザーがアカウントを作成したり、メールサインアップで身元を明らかにしたりした場合、プロファイルをマージできます。マージできるフィールドのリストについては、[マージ更新の動作]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior)を参照してください。

### 重複するユーザープロファイルのマージ {#merging-duplicate-user-profiles}

ユーザーデータが増加するにつれて、Brazeダッシュボードから重複するユーザープロファイルをマージできます。これらの重複するプロファイルは、同じ検索クエリを使用して検出する必要があります。ユーザープロファイルの重複をマージする方法の詳細については、[プロファイルのマージ]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/#merge-profiles)を参照してください。

また、[ユーザーマージエンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)を使用して、あるユーザープロファイルを別のユーザープロファイルにマージすることもできます。

{% alert note %}
ユーザープロファイルがマージされた後、この操作を元に戻すことはできません。
{% endalert %}

## その他のリソース {#additional-resources}
- 追加のコンテキストについては、Brazeの[ユーザープロファイルのライフサイクル]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/)に関する記事を参照してください。<br>
- [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android)、[iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#suggested-user-id-naming-convention)、および[Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web)でのユーザーIDの設定と`changeUser()`メソッドの呼び出しに関するドキュメントを参照してください。