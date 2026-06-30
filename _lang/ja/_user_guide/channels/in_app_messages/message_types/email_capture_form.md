---
nav_title: メールキャプチャフォーム
article_title: メールキャプチャフォーム
page_order: 5
page_type: reference
description: "この記事では、メールキャプチャのアプリ内メッセージタイプの概要について説明します。"
channel:
  - in-app messages
---

# メールキャプチャフォーム {#email-capture-form}

> メールキャプチャメッセージを使用すると、サイトのユーザーにメールアドレスの送信を促すことができます。Brazeは送信されたメールアドレスをユーザープロファイルに追加し、すべてのメッセージングキャンペーンで使用できるようにします。

このメッセージタイプは、[従来のエディター]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)で利用できます。

## 仕組み {#how-it-works}

エンドユーザーがこのフォームにメールアドレスを入力すると、Brazeはそのメールアドレスをユーザープロファイルに追加します。

- まだアカウントを持っていない[匿名ユーザー]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles)の場合、メールアドレスはユーザーのデバイスに紐づけられた匿名ユーザープロファイルに保存されます。
- ユーザープロファイルにすでにメールアドレスが存在する場合、新しく入力されたメールアドレスで既存のメールアドレスが上書きされます。
- 既知のユーザーのメールアドレスが[ハードバウンス]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#hard-bounce)としてフラグ付けされている場合、Brazeは新しく入力されたメールアドレスがBrazeプロファイルに登録されているものと異なるかどうかを確認します。メールアドレスが異なる場合、Brazeはメールアドレスを更新し、ハードバウンスのステータスを削除します。
- ユーザーが無効なメールアドレスを入力した場合、「Please enter a valid email.」というエラーメッセージが表示されます。
    - 無効なメールアドレスの例:
        - `example`
        - `example@`
        - `@gmail.com`
        - `example@gmail`
    - 有効なメールアドレスの例:
        - `example@gmail.com`
        - `example@gnail.com`（タイプミスあり）
    - Brazeでのメール検証の詳細については、[メールの技術ガイドラインと注意事項]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation)を参照してください。

{% details 識別済みユーザーと匿名ユーザーの詳細 %}

メールキャプチャフォームは、Brazeで現在アクティブなユーザープロファイルにメールアドレスを設定します。ユーザーが識別済み（ログイン済み、`changeUser`が呼び出された状態）かどうかによって動作が異なります。

匿名ユーザーがフォームにメールを入力して送信すると、Brazeはそのメールアドレスをプロファイルに追加します。その後のWebジャーニーで`changeUser`が呼び出され、新しい`external_id`が割り当てられた場合（新規ユーザーがサービスに登録した場合など）、メールアドレスを含むすべての匿名ユーザープロファイルデータがマージされます。

既存の`external_id`で`changeUser`が呼び出された場合、匿名ユーザープロファイルは孤立し、識別済みユーザーにまだ存在しない[特定のユーザープロファイルデータフィールド]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge_updates-behavior)はマージされますが、すでに存在するフィールド（メールアドレスを含む）は失われます。

詳細については、[ユーザープロファイルのライフサイクル]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)を参照してください。

{% enddetails %}

## ステップ 1: アプリ内メッセージキャンペーンを作成する {#step-1-create-an-in-app-message-campaign}

このオプションに移動するには、アプリ内メッセージングキャンペーンを作成する必要があります。そこから、ユースケースに応じて、**Send To**を**Web Browsers**、**Mobile Apps**、または**Both Mobile Apps & Web Browsers**に設定し、**Message Type**として**Email Capture Form**を選択します。

{% alert note %}
**Webユーザーをターゲットにしますか？**<br>Web SDKを通じてHTMLアプリ内メッセージを有効にするには、Brazeに`allowUserSuppliedJavascript`初期化オプションを指定する必要があります（例：`braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`）。これはセキュリティ上の理由によるもので、HTMLアプリ内メッセージはJavaScriptを実行できるため、サイト管理者が有効にする必要があります。
{% endalert %}

## ステップ 2: フォームをカスタマイズする {#customizable-features}

次に、必要に応じてフォームをカスタマイズします。メールキャプチャフォームでは、以下の機能をカスタマイズできます。

- ヘッダー、本文、送信ボタンのテキスト
- オプションの画像
- オプションの「利用規約」リンク
- ヘッダーと本文テキスト、ボタン、背景の色
- キーと値のペア
- ヘッダーと本文テキスト、ボタン、ボタンの枠線の色、背景、オーバーレイのスタイル
- 送信ボタン
    - 送信ボタンは、ユーザーが有効なメールアドレスを入力した後にのみ表示されます。これにより、完全なメールアドレスを収集できます。

![メールキャプチャフォームのコンポーザー。]({% image_buster /assets/img/email_capture.png %})

さらにカスタマイズが必要な場合は、**Message Type**として**Custom Code**を選択してください。GitHubリポジトリの[Braze Templates](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates)にある[メールキャプチャモーダルテンプレート](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/5-email-capture-modal)をスターターコードとして使用できます。

## ステップ 3: エントリオーディエンスを設定する {#step-3-set-your-entry-audience}

アプリ内メッセージを使用してユーザーのメールをキャプチャする場合、まだこの情報を提供していないユーザーにオーディエンスを限定することをお勧めします。

- **メールアドレスを持っていないユーザーをターゲットにする場合：** フィルター`Email Available`が`false`を使用します。これにより、メールが登録されていないユーザーにのみフォームが表示され、既知のユーザーへの冗長なプロンプトを回避できます。
- **external IDを持たない匿名ユーザーをターゲットにする場合：** フィルター`External User ID`が`is blank`を使用します。これは、まだ認証または登録されていないユーザーを特定したい場合に便利です。

必要に応じて、`AND`ロジックを使用して2つのフィルターを組み合わせることもできます。これにより、メールアドレスとexternal IDの両方が欠けているユーザーにのみフォームが表示されます。新規リードの獲得やアカウント作成の促進に最適です。

## ステップ 4: フォームに入力したユーザーをターゲットにする（オプション） {#step-4-target-users-who-filled-out-the-form-optional}

メールキャプチャフォームを起動し、ユーザーからメールアドレスを収集した後、フォームに入力したユーザーをターゲットにすることができます。

1. Brazeの任意のセグメントフィルターで、フィルター`Clicked/Opened Campaign`を選択します。
2. ドロップダウンから`clicked in-app message button 1`を選択します。
3. メールキャプチャフォームのキャンペーンを選択します。