---
page_order: 1.3
nav_title: デバッグ
article_title: Braze SDKのデバッグ
description: "Braze SDKデバッガーの使用方法について説明します。これにより、アプリの詳細ログを手動で有効にせずに、SDK対応チャネルの問題をトラブルシューティングできます。"
---

# Braze SDKのデバッグ {#debugging-the-braze-sdk}

> Braze SDKの組み込みデバッガーを使用する方法を説明します。これにより、アプリで詳細ログを有効にする必要なく、SDK対応チャネルの問題をトラブルシューティングできます。

{% alert tip %}
より詳細な調査のために、[詳細ログを有効にして]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)詳細なSDK出力をキャプチャしたり、特定のチャネルに関する[詳細ログの読み方を学習]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs)したりすることもできます。
{% endalert %}

## 前提条件 {#prerequisites}

Braze SDKデバッガーを使用するには、「View PII」および「View User Profiles (PII Redacted)」の権限が必要です。デバッグセッションのログをダウンロードするには、「Export User Data」権限も必要です。さらに、Braze SDKは以下の最小バージョンを満たしているか、参照している必要があります。

{% sdk_min_versions swift:10.2.0 android:32.1.0 %}

`Braze.configuration.logger.level`が`.disabled`の場合にデバッガーログを収集するには、Swift SDK 11.9.0以降を使用してください。詳細については、[Swift変更ログ]({{site.baseurl}}/developer_guide/changelogs#swift_fixed-12)を参照してください。

## Braze SDKのデバッグ

{% alert tip %}
Braze Web SDKのデバッグを有効にするには、[URLパラメーターを使用]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#logging)します。
{% endalert %}

### ステップ 1: アプリを閉じる {#step-1-close-your-app}

デバッグセッションを開始する前に、現在問題が発生しているアプリを閉じます。セッションの開始時にアプリを再起動できます。

### ステップ 2: デバッグセッションを作成する {#step-2-create-a-debugging-session}

Brazeで**設定**に移動し、**設定およびテスト**で**SDKデバッガー**を選択します。

![「SDKデバッガー」がハイライトされた「設定およびテスト」セクション。]({% image_buster /assets/img/sdk_debugger/select_sdk_debugger.png %})

**デバッグセッションを作成**を選択します。

![「SDKデバッガー」ページ。]({% image_buster /assets/img/sdk_debugger/select_create_debugging_session.png %})

### ステップ 3: ユーザーを選択する {#step-3-select-a-user}

メールアドレス、`external_id`、ユーザーエイリアス、またはプッシュトークンを使用してユーザーを検索します。セッションを開始する準備ができたら、**ユーザーを選択**を選択します。

![選択したユーザーのデバッグページ。]({% image_buster /assets/img/sdk_debugger/search_and_select_user.png %}){: style="max-width:85%;"}

### ステップ 4: アプリを再起動する {#step-4-relaunch-the-app}

まずアプリを起動し、デバイスがペアリングされていることを確認します。ペアリングが成功した場合は、アプリを再起動します&#8212;これにより、アプリの初期化ログが完全にキャプチャされます。

### ステップ 5: 再現ステップを完了する {#step-5-complete-the-reproduction-steps}

アプリを再起動した後、手順に従ってエラーを再現します。

{% alert tip %}
エラーを再現する際は、[高品質なログ](#step-6-export-your-session-logs-optional)を作成できるように、再現手順をできるだけ正確に実行してください。
{% endalert %}

### ステップ 6: セッションを終了する {#step-6-end-your-session}

再現手順が完了したら、**End Session** > **Close**を選択します。

![「End Session」ボタンが表示されているデバッグセッション。]({% image_buster /assets/img/sdk_debugger/close_debugging_session.png %}){: style="max-width:85%;"}

{% alert note %}
セッションの長さとネットワーク接続状況に応じて、ログの生成に数分かかる場合があります。
{% endalert %}

### ステップ 7: セッションを共有またはエクスポートする（オプション） {#step-7-share-or-export-your-session-optional}

セッション終了後、セッションログをCSVファイルとしてエクスポートできます。また、他のユーザーは**Session ID**を使用してデバッグセッションを検索できるため、ログを直接送信する必要はありません。

![セッション終了後に「Export Logs」と「Copy Session ID」が表示されたデバッグページ。]({% image_buster /assets/img/sdk_debugger/copy_id_and_export_logs.png %})