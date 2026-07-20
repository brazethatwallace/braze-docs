---
nav_title: トラブルシューティング
article_title: HTMLメールのトラブルシューティング
page_order: 9
description: "症状インデックスと標準的なトラブルシューティング手順を使用して、HTMLメールのレンダリングやエディターの問題を診断します。"
channel: email
---

# HTMLメールのトラブルシューティング {#troubleshoot-html-emails}

> このページでは、HTMLメールエディターやテスト送信に関するよくある問題を解決します。Inbox Visionや到達性については、[Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision)および[メール設定]({{site.baseurl}}/user_guide/channels/email/email_setup)を参照してください。

## まずはここから：症状を確認する {#start-here-match-your-symptom}

以下の表から該当する症状を見つけて、適切なセクションに移動してください。

| 症状 | 参照先 |
| --- | --- |
| テストメールのHTMLの表示がおかしい | [テストメールでHTMLが正しくレンダリングされない](#html-renders-incorrectly-in-test-emails) |
| Chromeでエディターの動作がおかしい | [拡張機能の競合](#extension-conflicts) |
| クライアントによってメールの表示が異なる | [メールのレンダリング](#email-rendering) |
| Inbox Visionのプレビューが送信済みメールと一致しない | [CSSインライン化](#css-inlining) |
| テストメールで画像の後に余白や線が表示される | [画像下の余白](#white-space-under-images) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTMLメールの症状" }

## 標準的な調査パス {#standard-investigation-path}

HTMLメールのレンダリングやエディターの動作が期待どおりでない場合は、このワークフローを使用してください。ステップ1から始めます。

1. エディターまたは外部バリデーターでHTMLマークアップを検証します。
2. [テストメール]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa)を送信し、どのメールクライアントやブラウザで問題が発生しているかを記録します。
3. [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision)でプレビューし、クライアント間のレンダリングを比較します。
4. エディター自体の動作がおかしい場合は、[ブラウザ拡張機能の競合](#extension-conflicts)を除外します。
5. 問題が解決しない場合は、Inbox Visionのスクリーンショットと影響を受けたクライアントの情報を添えて[サポートチケット]({{site.baseurl}}/braze_support)を開いてください。

## テストメールでHTMLが正しくレンダリングされない {#html-renders-incorrectly-in-test-emails}

**症状：**[テストメール]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa)の表示がエディターでの見た目と一致しない。

まずHTMLの設定を確認し、次に[拡張機能の競合](#extension-conflicts)、[メールのレンダリング](#email-rendering)、[CSSインライン化](#css-inlining)、[画像下の余白](#white-space-under-images)を確認してください。

### 拡張機能の競合 {#extension-conflicts}

特定のブラウザ拡張機能がメールエディターで問題を引き起こすことがあります。例えば、Google Chromeで使用する[Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en)がその一例です。これらの拡張機能を使用している場合は、以下のいずれかを行ってください。

- Grammarlyがブラウザ拡張機能としてインストールされていないブラウザでBrazeメールを編集する
- Brazeアカウントマネージャーに連絡して、メールエディターをHTMLのみまたはプレーンテキストに切り替えるよう依頼する

プレーンテキストビューでは`WYSIWYG`（見たままが得られる）エディターが削除されるため、このリクエストを行う前に、すべてのチームメンバーがHTMLに慣れていることを確認してください。

### メールのレンダリング {#email-rendering}

メールはブラウザやメールクライアントによってレンダリングが異なるため、問題が発生しているブラウザやメールクライアントを記録しておいてください。

- [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision)を使用してメールをプレビューし、さまざまなブラウザやメールクライアントでメールがどのように表示されるかを確認してください。
- 問題を引き起こしているブラウザやメールクライアントを特定したら、開発者チームにHTMLを修正し、それらのブラウザやメールクライアントに対応するための編集が必要であることを伝えてください。

### CSSインライン化 {#css-inlining}

Inbox Visionのプレビューが、Brazeで送信されたものと一致しない場合があります。これは、Brazeと他のツールで実行されるCSSインライン化の違いが原因である可能性があります。これが原因と思われる場合は、CSSインライン化をオフにしてください。

### 画像下の余白 {#white-space-under-images}

**症状：**テストメールで画像の後に余白や線が表示される。

テストメールで画像の下に余白や線が表示される場合、これは通常、メールクライアントがインラインレベル要素をレンダリングする方法が原因です。画像はデフォルトでインラインレベルであり、ベースラインに揃えられます。これにより、ブラウザがディセンダー（「g」や「y」のようにベースラインより下に伸びる文字の部分）に対応できるようになりますが、余白として表示される小さな隙間が生じます。

これを修正するには、画像のCSSに`display: block;`を追加します。

```html
<style>
  img {
    display: block;
  }
</style>
```

または、特定の画像にスタイルを直接適用することもできます。

```html
<img src="https://example.com/image.jpg" style="display: block;" alt="Image description" />
```
