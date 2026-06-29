---
nav_title: トラブルシューティング
article_title: トラブルシューティング
page_order: 9
description: "このヘルプ記事では、HTMLメールに関する問題のトラブルシューティング方法について説明します。"
channel: email
---

# トラブルシューティング {#troubleshooting}

> この記事では、HTMLメールに関するよくある問題と、拡張機能の競合、レンダリングの違い、CSSインライン化を含む解決方法について説明します。

## テストメールでHTMLが正しくレンダリングされない {#html-renders-incorrectly-in-test-emails}

[テストメール]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa)の表示がおかしい場合は、まずHTMLの設定を確認することをお勧めします。次に、以下の問題を確認してください。
* [拡張機能の競合](#check-conflicts)
* [メールのレンダリング](#check-rendering)
* [CSSインライン化](#switch-css-inlining)

### 拡張機能の競合 {#check-conflicts}

特定のブラウザ拡張機能がメールエディターで問題を引き起こすことがあります。例えば、Google Chromeで使用する[Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en)がその一例です。これらの拡張機能を使用している場合は、以下のいずれかを行ってください。
- Grammarlyがブラウザ拡張機能としてインストールされていないブラウザでBrazeメールを編集する
- Brazeアカウントマネージャーに連絡して、メールエディターをHTMLのみまたはプレーンテキストに切り替えるよう依頼する

プレーンテキストビューでは`WYSIWYG`（見たままが得られる）エディターが削除されるため、このリクエストを行う前に、すべてのチームメンバーがHTMLに慣れていることを確認してください。

### メールのレンダリング {#check-rendering}

メールはブラウザやメールクライアントによってレンダリングが異なるため、問題が発生しているブラウザやメールクライアントを記録しておいてください。

- [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision#inbox-vision)を使用してメールをプレビューし、さまざまなブラウザやメールクライアントでメールがどのように表示されるかを確認してください。
- 問題を引き起こしているブラウザやメールクライアントを特定したら、開発者チームにHTMLを修正し、それらのブラウザやメールクライアントに対応するための編集が必要であることを伝えてください。

### CSSインライン化 {#switch-css-inlining}

Inbox Visionのプレビューが、Brazeで送信されたものと一致しない場合があります。これは、Brazeと他のツールで実行されるCSSインライン化の違いが原因である可能性があります。これが原因と思われる場合は、CSSインライン化をオフにしてください。

まだサポートが必要ですか？[サポートチケット]({{site.baseurl}}/braze_support)を開いてください。