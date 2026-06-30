---
nav_title: チャネル
article_title: チャネル
page_order: 5
layout: dev_guide
guide_top_header: "チャネル"
guide_top_text: "適切なタイミングで適切なチャネルを通じてユーザーにリーチしましょう。アプリ内メッセージ、Content Cards、バナーなどのプロダクト内チャネルや、プッシュ、メール、SMS、WhatsAppなどのプロダクト外チャネルから選択できます。"

page_type: landing
description: "Brazeのプロダクト内およびプロダクト外のメッセージングチャネルを通じてユーザーにリーチしましょう。"

guide_featured_title: "プロダクト内チャネル"
guide_featured_list:
  - name: アプリ内メッセージ
    link: /docs/user_guide/channels/in_app_messages
    image: /assets/img/braze_icons/phone-02.svg
  - name: Content Cards
    link: /docs/user_guide/channels/content_cards
    image: /assets/img/braze_icons/sticker-square.svg
  - name: バナー
    link: /docs/user_guide/channels/banners
    image: /assets/img/braze_icons/layout-top.svg

guide_menu_title: "プロダクト外チャネル"
guide_menu_list:
  - name: メール
    link: /docs/user_guide/channels/email
    image: /assets/img/braze_icons/mail-01.svg
  - name: トランザクションメール
    link: /docs/user_guide/channels/transactional_email
    image: /assets/img/braze_icons/bank-note-02.svg
  - name: ランディングページ
    link: /docs/user_guide/messaging/landing_pages
    image: /assets/img/braze_icons/file-02.svg
  - name: LINE
    link: /docs/user_guide/channels/line
    image: /assets/img/braze_icons/message-chat-circle.svg
  - name: ライブ通知
    link: /docs/developer_guide/live_notifications
    image: /assets/img/braze_icons/phone-02.svg
  - name: プッシュ
    link: /docs/user_guide/channels/push
    image: /assets/img/braze_icons/marker-pin-05.svg
  - name: "SMS、MMS、RCS"
    link: /docs/user_guide/channels/sms_mms_and_rcs
    image: /assets/img/braze_icons/message-text-circle-01.svg
  - name: Webhook
    link: /docs/user_guide/channels/webhooks
    image: /assets/img/braze_icons/brackets.svg
  - name: WhatsApp
    link: /docs/user_guide/channels/whatsapp
    image: /assets/img/braze_icons/whatsapp.svg
---

## メッセージチャネルの選択 {#choosing-a-message-channel}

キャンペーンやキャンバスに最適なメッセージチャネルを決定する際は、メッセージのコンテンツと緊急性を常に考慮してください。

- **コンテンツ**は、メッセージの視覚的な訴求力を表します。マルチメディアやその他のアセットをコピーに追加することで、コンテンツをよりリッチにすることができます。
- **緊急性**は、メッセージがどれだけ迅速にユーザーに通知し、注意を引くことができるかを示す指標です。ユーザーがすぐに確認できる通知は緊急性が高く、アプリへのログインが必要なメッセージは緊急性が低くなります。

Brazeメッセージングマトリクスは、**コンテンツの複雑さ**と**配信の緊急性**を対応させることで、チャネル選択を効率化します。この2つの要素のバランスを取ることで、メッセージが中断ではなく共感を生むようにすることができます。

![モバイル/Webプッシュはシンプルなコンテンツで高い緊急性、メールはリッチなコンテンツで高い緊急性、アプリ内/ブラウザメッセージはシンプルなコンテンツで低い緊急性、Content Cardsは低い緊急性でリッチなコンテンツ]({% image_buster /assets/img_archive/messaging_matrix.png %})

このマトリクスは主要なチャネルを示していますが、柔軟に応用できます。たとえば、SMSやWhatsAppは緊急性の高いツールですが、マルチメディア形式を活用することでリッチなコンテンツにも対応できます。このマトリクスの活用方法について詳しくは、Brazeラーニングコースの[クロスチャネルメッセージング](https://learning.braze.com/cross-channel-messaging)をご覧ください。

## アクセシビリティリソース {#accessibility-resources}

Brazeを使用して、各チャネルでアクセシブルなメッセージングキャンペーンを作成できます。エンジニアと協力して、実装においてアクセシビリティ基準を満たすようにしてください。追加のガイダンスが必要な場合は、以下をお勧めします。

- [Accessible Messaging Foundations](https://learning.braze.com/accessible-messaging-foundations): このBrazeラーニングコースで、ブランドコミュニケーションに適用される基本的なアクセシビリティの原則を学びましょう。
- [アクセシブルなメッセージの構築]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility): Braze内で直接、代替テキストの追加や支援技術向けのコンテンツ構造化の方法を学びましょう。

Brazeのアクセシビリティや、Brazeから送信されるメッセージについてフィードバックがある場合は、ぜひお聞かせください。グローバルヘッダーの**サポート**メニューを開き、**フィードバックを共有**を選択してご意見をお送りください。