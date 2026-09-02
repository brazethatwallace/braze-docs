---
nav_title: アンインストール追跡
article_title: iOS のアンインストール追跡
platform: iOS
page_order: 7
description: "この記事では、iOSアプリケーションのアンインストール追跡を構成する方法について説明します。"

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# iOSのアンインストール追跡 {#uninstall-tracking-for-ios}

> この記事では、iOSアプリケーションのアンインストール追跡を構成する方法と、Brazeのアンインストール追跡プッシュの受信時にアプリで不要な自動アクションが実行されないことを確認するためのテスト方法について説明します。

アンインストール追跡では、ペイロードにBrazeフラグを含むバックグラウンドプッシュ通知を利用します。詳細については、ユーザーガイドの[アンインストール追跡]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking)を参照してください。

## ステップ1：バックグラウンドプッシュを有効にする {#step-1-enabling-background-push}

Xcodeプロジェクトの**Capabilities**タブの**Background Modes**セクションで、**Remote notifications**オプションが有効になっていることを確認してください。詳細については、[サイレントプッシュ通知]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications)のドキュメントを参照してください。

## ステップ2: Brazeバックグラウンドプッシュの確認 {#step-2-checking-for-braze-background-push}

Brazeはアンインストール追跡の分析データを収集するために、バックグラウンドプッシュ通知を使用します。アプリケーションがアンインストール追跡通知を受信した際に、[不要なアクションを実行しない]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/ignoring_internal_push)ようにしてください。

## ステップ3：ダッシュボードからテストする {#step-3-test-from-the-dashboard}

次に、ダッシュボードからテストプッシュを自分自身に送信します。このテストプッシュではユーザープロファイルは更新されません。

1. **キャンペーン**ページで、プッシュ通知キャンペーンを作成し、プラットフォームとして**iOSプッシュ**を選択します。<br><br>
2. **設定**ページで、キー`appboy_uninstall_tracking`に対応する値`true`を追加し、**Add Content-Available Flag**にチェックを入れます。<br><br>
3. **プレビュー**ページを使用して、アンインストール追跡テストプッシュを自分自身に送信します。<br><br>
4. プッシュを受信した際に、アプリが意図しない自動アクションを実行しないことを確認します。

{% alert important %}
これらのテストステップは、Brazeからアンインストール追跡プッシュを送信する代わりのテスト方法です。バッジカウントを有効にしている場合、テストプッシュと一緒にバッジ番号が送信されますが、Brazeのアンインストール追跡プッシュではアプリケーションにバッジ番号は設定されません。
{% endalert %}

## ステップ4：アンインストール追跡を有効にする {#step-4-enable-uninstall-tracking}

[アンインストール追跡の有効化]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking)の手順に従ってください。