---
nav_title: メール
article_title: メール
page_order: 3
page_type: landing
description: "Brazeのドラッグ＆ドロップエディターやHTMLエディター、購読管理などを使って、カスタマイズされたパーソナライズ済みメールキャンペーンを作成できます。"
channel:
  - email
search_rank: 2
---

# メール {#email}

> Brazeのメール機能を使えば、キャンペーンやキャンバスでカスタマイズされたパーソナライズ済みメールメッセージを作成し、アプリやWebサイトの外にいるユーザーにリーチできます。このハブでは、メールの設定、ドラッグ＆ドロップエディターおよびHTMLエディター、購読管理、テンプレート、テストについて説明しています。コンプライアンスに準拠し、ブランドに沿ったメールプログラムを立ち上げましょう。BrazeのメールテンプレートやカスタムHTMLを使用して、ブランドのトーンやレイアウトに合わせることができます。新しい送信ドメインを設定する場合は、[メールセットアップ]({{site.baseurl}}/user_guide/channels/email/email_setup)から始めてください。メールキャンペーンの例については、Brazeの[ケーススタディ](https://www.braze.com/customers/)を参照してください。

## 前提条件 {#prerequisites}

Brazeでメールを送信する前に、専用IP、ドメイン、メール認証、およびIPウォームアップを設定する必要があります。詳細な手順については、[メールセットアップ]({{site.baseurl}}/user_guide/channels/email/email_setup)を参照してください。

## メールのカスタマイズ {#customize-your-emails}

メールメッセージングは、以下のようなさまざまな方法でカスタマイズできます。

- [Brazeメールテンプレート]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template)
- [カスタムHTMLテンプレート]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template)
- [エディターブロック（メール）]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email)
- [ユーザーの購読]({{site.baseurl}}/user_guide/channels/email/subscriptions)
- [購読グループ]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups)

## メールをテストする {#test-your-emails}

[シードグループ]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups)は、品質保証を行うためにメールキャンペーンのコピーを内部ユーザーに自動的に送信します。シードメールには、識別しやすいように件名の先頭に`[SEED]`が付加されます。

## ユースケース {#use-cases}

| ユースケース | 説明 |
| --- | --- |
| 再エンゲージメント | アプリをインストールしていないユーザーを含め、アプリ外のユーザーにリーチします。 |
| オンボーディング | 新規ユーザーのオンボーディングを行い、プッシュ通知の有効化やソーシャルネットワークでのアプリ共有を促します。 |
| リッチメッセージ | リッチでダイナミックなHTMLメッセージを配信できます。 |
| マルチメディアコンテンツ | 動画や画像など、ユーザーのエンゲージメントを高めるマルチメディアコンテンツを簡単に配置できます。 |
| ニュースレター | ユーザーのエンゲージメントを維持するために、月次または週次のニュースレターを手軽に送信できます。 |
| トランザクション | 最近の購入をユーザーに通知し、[トランザクションメール]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email)を使用して重要な商品情報や配送情報を届けます。
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユースケース" }

## メールサービス {#email-services}

メールプログラムに追加のサポートが必要な場合、Brazeは追加費用で定期的および単発のサービスを提供しています。詳細については、Brazeアカウントマネージャーにお問い合わせください。

### メール到達性サービス {#email-deliverability-services}

Brazeは2つのティアの定期メールサポートを提供しています。
1. デラックス
2. スタンダード

これらのサービスには以下が含まれます。

- ターゲティング、配信頻度、メッセージング戦略のレビューを含む、過去および現在のメール送信プラクティスの監査
- メール到達性の専門家が作成する許可リストの設定とカスタマイズされたIPウォーミングプラン
  - 最初の1か月間の定期チェックインコール（デラックスは週3回、スタンダードは週1回）
- 到達性の専門家との定期コール（デラックスは月2回、スタンダードは月1回）で以下を提供します。
  - ドメインごとの到達性パフォーマンスの監視
  - データと確立されたベストプラクティスを活用した、メールプログラムのパフォーマンスと結果を改善するための推奨事項
- ブロックリスト登録などの到達性に関する問題につながるイベントに対する危機対応の軽減と修復

## よくある質問 {#frequently-asked-questions}

### Brazeでメール送信を設定するにはどうすればよいですか？ {#how-do-i-set-up-email-sending-in-braze}

最初の送信前に、専用IP、ドメイン、認証、IPウォームアップを設定してください。完全なチェックリストについては、[メールセットアップ]({{site.baseurl}}/user_guide/channels/email/email_setup)を参照してください。

### ユーザー購読と購読グループの違いは何ですか？ {#what-is-the-difference-between-user-subscriptions-and-subscription-groups}

ユーザー購読は、チャネル（メールの購読済みまたは購読解除など）に対するグローバルなオプトインステータスを管理します。購読グループでは、ユーザーがそのチャネル内の特定のメッセージカテゴリを選択できます。詳しくは、[ユーザー購読]({{site.baseurl}}/user_guide/channels/email/subscriptions)および[購読グループ]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups)を参照してください。

### キャンペーンを送信する前にメールをテストするにはどうすればよいですか？ {#how-can-i-test-an-email-before-i-send-a-campaign}

[シードグループ]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups)を使用して、内部レビュアーにプレビューコピーを送信し、さまざまなクライアントでのレンダリングを確認してください。

## 次のステップ {#next-steps}

{% article_tiles %}
- name: メールセットアップ
  link: /docs/user_guide/channels/email/email_setup
- name: ドラッグ＆ドロップエディターでメールを作成する
  link: /docs/user_guide/channels/email/drag_and_drop
- name: HTMLエディターでメールを作成する
  link: /docs/user_guide/channels/email/html_editor
{% endarticle_tiles %}