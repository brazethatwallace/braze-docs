---
nav_title: 準備ガイド
article_title: アプリ内メッセージ準備ガイド
page_order: 0.5

page_type: reference
description: "この記事では、アプリ内メッセージを作成する前に検討すべき質問やベストプラクティスについて、ターゲティング、スケジュール、コンテンツ、パフォーマンス、コンバージョンの観点から説明します。"
channel: in-app messages
toc_headers: h2
---

# アプリ内メッセージ準備ガイド {#in-app-message-prep-guide}

> アプリ内メッセージを作成する前に、以下のトピックを検討しておくと、作成プロセスをより効率的に進めることができます。

## 一般的な考慮事項 {#general-considerations}

- キャンペーンを作成する場合、このメッセージのバリアントをいくつ表示しますか？バリアントテストのアイデアについては、[さまざまなチャネルのヒント]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#tips-different-channels)をご覧ください。
- キャンバスを作成する場合、このメッセージはそのステップ内の他のメッセージングチャネルと組み合わせますか？
- [メッセージの有効期限]({{site.baseurl}}/canvas_in-app_messages)はいつに設定しますか？

## ターゲティングの考慮事項 {#targeting-considerations}

- アプリ内メッセージは、アプリを定期的に訪問するユーザーに最適です。このオーディエンスを含めていますか？
- ユーザーにメッセージをどこで表示させたいですか？Webアプリですか？モバイルアプリですか？
- どのイベントがこのメッセージをトリガーすべきですか？
- 古いバージョンのアプリを使用しているユーザーはいますか？その場合、メッセージの一部の要素が表示されない可能性があります。
- どのタイプのデバイスに対してこのメッセージを作成していますか？**プレビュー**ボックスまたは**テスト**タブを使用してメッセージをプレビューできることを覚えておいてください。詳細については、[テストメッセージを送信する]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message)を参照してください。

## スケジュール、遅延、セッション開始 {#scheduling-delays-and-session-starts}

アプリ内メッセージキャンペーンで、セッション開始をトリガーとする**スケジュール遅延**が設定されている場合、セッションを開始した後、アプリ内メッセージが表示される前にアプリを閉じたユーザーは、遅延が満了した後の次のセッション開始時にそのメッセージを受け取ることができます。

アプリ内メッセージキャンペーンでは、トリガー後最大2時間の配信遅延が可能です。より長い待機時間が必要な場合は、キャンバスのアプリ内メッセージステップの前に[遅延]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)ステップを追加してください。遅延の設定については、[アクションベース配信]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#step-2-select-delay-length)を参照してください。

このタイミングにより、予期しない表示動作が発生する場合があります。特に、キャンペーンで**表示前にキャンペーン適格性を再評価する**が選択されていない場合に顕著です。

たとえば、キャンペーンの開始から1か月後に、8秒の遅延が設定されたアプリ内メッセージをユーザーが受け取ることがあります。これは、ユーザーがセッションを開始し、すぐにセッションを終了し、1か月後にセッションを再度開始し、その8秒後にアプリ内メッセージを受信した場合に発生する可能性があります。アプリを閉じずに別の画面に移動した場合、アプリに戻った際にアプリ内メッセージが表示されます。

## コンテンツに関する考慮事項 {#content-considerations}

- このメッセージでどの言語を使用しますか？
- ヘッダーと本文のコピーはどのようなものですか？ユーザーの目を引く、関連性のある内容になっていますか？
- アプリ内メッセージは一定時間しか表示されません。コピーは簡潔で印象に残るものですか？
- [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid)を使用してカスタムコピーを追加しますか？
- ユーザーがメッセージテキスト（割引コードやバウチャーコードなど）をコピーする必要がありますか？iOSとAndroidでは、テキストやテキスト入力フィールドを長押しすることでコンテンツをコピーできます。画像では長押しが機能しないため、コードやその他のユーザーがコピーする必要のある内容を含む画像ではなく、テキストまたはテキスト入力フィールドを使用してください。
- フルスクリーンのアプリ内メッセージの場合、画像やその他のメディアは[セーフゾーン]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/fullscreen#image-safe-zone)内に収まっていますか？
- 調査アプリ内メッセージの場合、属性や送信内容を記録しますか？確認ページは設定済みですか？
- カスタムHTMLアプリ内メッセージの場合、特殊文字を正しく表示するためにHTMLにUTF-8エンコーディングが含まれていますか？詳しくは[カスタムHTMLアプリ内メッセージ]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#character-encoding)をご覧ください。
- アプリ内メッセージに動画を含める場合：Brazeはデバイスでのローカル再生における動画ファイルサイズに技術的な制限を設けていませんが、ユーザーの接続速度が遅い場合や、データプランが高額な場合、またはストレージが限られている場合があることに留意してください。品質とファイルサイズのバランスを取るよう、動画ファイルを最適化してください。

## アプリ内メッセージのパフォーマンスを最適化する {#optimize-in-app-message-performance}

Brazeは、セッション開始時にユーザーに対して条件を満たすアプリ内メッセージトリガーを配信します。Liquidを使用した多数のメッセージを準備すると、セッション開始が遅延し、アプリのパフォーマンスに影響を与える可能性があります。

この処理に数秒以上かかる場合、Brazeは残りのLiquidレンダリングを延期することがあります。その場合、各メッセージはトリガーされた時点でレンダリングされ、オンデマンドで取得されます。この[テンプレート配信]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages)は、レスポンスレイテンシの増加によるアプリパフォーマンスの低下からユーザーを保護します。

メッセージ配信を高速化するために、以下のベストプラクティスを活用してください。

- キャンペーンのトリガーを実行できるユーザーのみをターゲットにしてください。ターゲティングが広すぎると、ユーザーが一度も起動できないアプリ内メッセージトリガーを受け取ってしまう場合があります。例えば、特定のプッシュキャンペーンによってトリガーされるアプリ内メッセージは、同じターゲットオーディエンスを使用するようにスコープを絞ることができます。これは、他のキャンペーンタイプ、キャンバス、特定のユーザーのみがトリガーできるカスタムイベントなどにも同様に適用できます。
- 期限のあるキャンペーンには終了日を設定してください。インプレッションの受信が見込めなくなったキャンペーンは停止してください。
- 大きな静的スタイルシート、スクリプト、base64エンコードされたメディアアセットをメッセージ内やコンテンツブロックを通じて直接挿入することは避けてください。代わりに[メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)を使用して、メッセージのレンダリングにかかる時間を短縮してください。
- 複雑な分岐やループのLiquidロジックを削減してください。
- ユーザーが複数回メッセージを受け取るべき場合にのみ、再適格性を有効にしてください。再適格性がオフのままの場合、Brazeはユーザーがメッセージを表示した後、アプリ内メッセージトリガーの配信を停止します。詳細については、[再適格性]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)を参照してください。
- 重要なキャンペーンには高い優先度を設定してください。Brazeは優先度の高い適格なメッセージから先にレンダリングするため、ユーザーが多くのキャンペーンに該当する場合でもテンプレート配信が発生しにくくなります。詳細については、[優先度を選択する]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#choose-a-priority)を参照してください。

### 静的コードとアセットを分離する {#separate-static-code-and-assets}

パーソナライズされた値と条件ルールはメッセージ内に残してください。再利用可能なCSS、JavaScript、メディアアセットは[メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)にホストし、そこからリンクしてください。

これをすべてのスクリプトやスタイルに対して行う必要はありません。これは主に、共有ブランドスタイルやインタラクティブウィジェットのような複雑なスクリプトなど、大きなアセットによる肥大化を軽減するのに役立ちます。

メディアライブラリのスタイルシートとスクリプトはLiquidを評価しないため、ユーザーのデバイスでキャッシュできます。以下の例では、動的な値をインラインに保持し、再利用可能なコードを静的ファイルから読み込みます。

{% raw %}

```liquid
<head>
  <style>
    /* Select a hero image URL based on the user's subscription tier. */
    {% capture hero_image_url %}
      {% if custom_attribute.${subscription_tier} == 'premium' %}
        https://braze-images.com/path/to/premium/hero.jpg
      {% else %}
        https://braze-images.com/path/to/standard/hero.jpg
      {% endif %}
    {% endcapture %}
    /* Assigning to a CSS variable so it can be used inside our stylesheet. */
    :root {
      --hero-image: url("{{ hero_image_url | url_escape }}");
    }
  </style>
  <script>
    // Assigning to the global window object so the value can be referenced in our script.
    window.brandConfig = {
      subscriptionTier: "{{custom_attribute.${subscription_tier} | json_escape }}"
    };
  </script>
  <!-- Linking to a stylesheet from the Braze media library. -->
  <link rel="stylesheet" href="https://braze-images.com/path/to/media/library/asset.css">
  <!-- Linking to a script from the Braze media library. -->
  <script src="https://braze-images.com/path/to/other/media/library/asset.js" defer></script>
</head>

<body>
  <div class="hero"></div>
  <div class="user-styles" data-subscription-tier="{{custom_attribute.${subscription_tier} | escape}}">
    ...
  </div>
</body>
```

{% endraw %}

メディアライブラリのスタイルシートでは、CSS変数を参照し、その他の再利用可能なスタイルを定義できます。

```css
.hero {
  background-image: var(--hero-image);
}

.user-styles {
  /* styles for all users */
}

.user-styles[data-subscription-tier="premium"] {
  /* premium subscription tier user styles, color scheme, etc */
}

.user-styles[data-subscription-tier="standard"] {
  /* standard subscription tier user styles, color scheme, etc */
}
```

メディアライブラリのスクリプトでは、インラインのJavaScript変数を使用して、再利用可能な動作を追加できます。

```javascript
const config = window.brandConfig || {};

if (config.subscriptionTier === "standard") {
  // add some sort of logic to show a "subscribe to premium" button
} else if (config.subscriptionTier === "premium") {
  // thank the user for being a premium user
}
```

## コンバージョンに関する考慮事項 {#conversion-considerations}

- このメッセージの目的は何ですか？それをメッセージの中でどのように表現できますか？
- ボタンはユーザーにとって意味のある選択肢を提供していますか？[主要なコールトゥアクション]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#buttons)は何ですか？
- [他のアプリ内コンテンツにディープリンク]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content)していますか？このアプリ内メッセージを使って、[許可リクエストやプッシュの事前確認リクエスト]({{site.baseurl}}/user_guide/channels/push/best_practices)を送信および受け入れていますか？
- メッセージの終了オプションはありますか？ない場合は、以下のスニペットをコピー＆ペーストして、簡単なボタンを作成できます。
  ```html
  <a href="appboy://close">X</a>
  ```

## ドラッグ＆ドロップエディターに関する考慮事項 {#drag-and-drop-editor-considerations}

### デバイスごとに異なるディープリンクを追加する {#adding-deep-links-for-different-devices}

ドラッグ＆ドロップエディターでは、デバイスごとに異なるディープリンクを追加することはサポートされていません（従来のエディターとは異なります）。

### バックグラウンド画像の不透明度を調整する {#adjusting-background-image-opacity}

不透明度の設定では、バックグラウンド画像を完全に透明にすることはできません（従来のIAMエディターとは異なります）。不透明度の設定を使用して、メッセージのバックグラウンドカラーを完全に透明にすることは可能です。

### 最大幅を設定する {#setting-the-maximum-width}

ドラッグ＆ドロップエディターの最大幅は325pxに制限されています。これは主にダッシュボードのプレビューに対応するためです。メッセージは小さな画面のデバイスでも正しく表示されます。

### プラットフォームごとに異なるバックグラウンドを選択する {#selecting-different-backgrounds-for-different-platforms}

同じメッセージに対して、異なるプラットフォーム（Webやモバイルなど）で2つの異なるバックグラウンドを表示することはできません。

### メッセージスタイルを適用する {#applying-message-styles}

バックグラウンド画像はメッセージ全体に適用され、ページごとにカスタマイズすることはできません。メッセージスタイルは、個々のページではなく、メッセージ全体に適用されます。

### スペーサーブロックの高さを測定する {#measuring-spacer-blocks-height}

スペーサーブロックの測定単位はピクセル（px）であり、変更することはできません。

### サポートされているフォーマット {#supported-formats}

現在、ドラッグ＆ドロップエディターでは、モーダルおよびフルスクリーンのアプリ内メッセージのみがサポートされています。

### サイズとアスペクト比に合わせて調整する {#adjusting-to-size-and-aspect-ratio}

モーダルがバックグラウンド画像のサイズとアスペクト比に合わせて調整されるため、バックグラウンド画像はアプリ内メッセージを引き伸ばします。必要に応じて比率を調整できます。

### バックグラウンド画像とクリック時の動作 {#background-images-and-on-click-behavior}

これらはページ間で保持されます。各ページに異なるフル画像を持つ複数ページのアプリ内メッセージの場合は、ユーザーが次のページにクリックして移動できるようにボタンを追加してください。