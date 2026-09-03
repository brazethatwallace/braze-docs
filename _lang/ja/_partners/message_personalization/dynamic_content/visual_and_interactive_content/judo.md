---
nav_title: Judo
article_title: Judo
description: "このリファレンス記事では、BrazeとJudoのパートナーシップについて説明します。Judoは、iOSおよびAndroidアプリにロケーションコンテキストとトラッキングを追加できる、コード不要のサーバー駆動型UIプラットフォームです。"
alias: /partners/judo/
page_type: partner
search_tag: Partner

---

# Judo

> [Judo](https://judo.app)はサーバー駆動型UIプラットフォームであり、パブリッシャーがアプリを更新せずに、リッチで魅力的なアプリ内ユーザーエクスペリエンスを効率的に提供できるようにします。

_この統合はJudoによって管理されています。_

## 統合について {#about-the-integration}

BrazeとJudoの統合により、キャンペーンとキャンバスで特別にカスタマイズされたエクスペリエンスが実現します。Braze キャンペーンには、シンプルなテンプレート化されたランディングページエクスペリエンスの代わりに、複数の画面、モーダル、動画、カスタムフォント、サポート設定（コードを使わず作成され、アプリ更新なしでデプロイされるダークモードやアクセシビリティなど）からなるコンテンツを組み込むことができます。Judoエクスペリエンスでパーソナライズされたコンテンツをサポートするために、Brazeのデータを使用することもできます。ユーザーイベントとエクスペリエンスからのデータは、アトリビューションとターゲティングのためにBrazeにフィードバックできます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Judoアカウント | このパートナーシップを活用するには、[Judo](https://www.judo.app/)アカウントが必要です。 |
| Judo SDK | Judo SDKは、[iOS](https://github.com/judoapp/judo-ios/)アプリおよび/または[Android](https://github.com/judoapp/judo-android)アプリに統合する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

**オンボーディング**：Judoを使用するアプリパブリッシャーは、リッチでネイティブなオンボーディングエクスペリエンスを構築、デプロイします。これらのエクスペリエンスを、Brazeにより調整されるパーソナライズされたクロスチャネルのオンボーディングジャーニーの要素として利用できるようになりました。さまざまなアプリ内フローの有効性をテストするために、エクスペリエンスをパーソナライズし、アプリの更新なしで迅速に更新できます。

**コンバージョン**：アプリパブリッシャーはBrazeのデータを使用して、パーソナライズされたリッチなアプリ内エクスペリエンスを作成し、Judoの統合フックを使用して、アプリ内購入、有料サブスクリプション、または文脈に応じたマーチャンダイジングを促進することができます。これらのエクスペリエンスへのアクセスは、Brazeで作成されたエンゲージメントマーケティングキャンペーンによってトリガーできます。

**イベント駆動型コンテンツ**：スポーツやエンターテイメント分野では、Judoは主として、イベントのプレビュー、プロモーション、要約のためのリッチなエクスペリエンスを構築する目的で使用されています。この機能は、他の業種でも季節的なコンテンツやニュースに基づくコンテンツに幅広く応用できます。イベントをタイムリーに宣伝またはハイライトするメッセージングをリッチなアプリ内エクスペリエンスにリンクすることで、パブリッシャーは状況に即した対応によりエンゲージメントを促進できます。

## サイドバイサイドのSDK統合 {#side-by-side-sdk-integration}

Judoは、モバイルアプリにJudoとBraze SDKを並べて統合するために必要な作業の一部を自動化する追加ライブラリーを提供しています。

### ステップ1：Judo-Braze統合ライブラリーをインストールする {#step-1-install-the-judo-braze-integration-library}

アプリにJudo-Braze統合ライブラリーをインストールしてセットアップします。これにより、イベントトラッキングが自動的に有効になります。

- [iOSのインストール
手順](https://github.com/judoapp/judo-braze-ios/wiki#installation)
- [Androidのインストール
手順](https://github.com/judoapp/judo-braze-android/wiki#installation)

### ステップ2：アプリ内メッセージングを設定する {#step-2-configure-in-app-messaging}

このステップでは、iOSおよびAndroid用のカスタム`ABKInAppMessageControllerDelegate`および`IInAppMessageManagerListener`実装を作成します。

各統合ライブラリーに同梱されているアプリ内メッセージ設定ドキュメントを参照してください：

- [iOSアプリ内メッセージ
セットアップ](https://github.com/judoapp/judo-braze-ios/wiki#in-app-messaging-setup)
- [Androidアプリ内メッセージ
セットアップ](https://github.com/judoapp/judo-braze-android/wiki#in-app-messaging-setup)

## この統合を使う {#using-this-integration}

アプリ側の統合が完了したら、Judoエクスペリエンス用のBrazeアプリ内メッセージキャンペーンをテスト実行して、期待どおりに動作することを確認できます。

### ステップ1：カスタムコードのアプリ内メッセージキャンペーンを作成する {#step-1-create-a-custom-code-in-app-message-campaign}

Brazeプラットフォームから、**Custom Code**メッセージタイプでBrazeアプリ内メッセージキャンペーンを作成します。次に、カスタムタイプとして**HTML Upload**を選択します。メッセージのコンテンツに、ベースのアプリ内メッセージングのフィールドが取り込まれていることを確認してください。このコンテンツはユーザーには表示されません。

![「Custom Code」メッセージタイプを選択したときのダッシュボードの画像。]({% image_buster /assets/img/judo/braze-campaign-select-custom-type.png %})

次に、以下の最小限のHTMLスニペットを使って、フォームのバリデーションを満たします：
```
<a href="appboy://close">X</a>
```

JudoがこれをJudoエクスペリエンスに書き換えて置き換えるため、これはデバイスの本番環境では表示されないことに注意してください。

![キャンペーンの作成ステップに追加されたフォーム検証コードを示す画像。]({% image_buster /assets/img/judo/braze-html-boilerplate.png %})

### ステップ2：Judo用のキーバリューペアを設定する {#step-2-set-a-key-value-pair-for-judo}
![この統合に必要な1つのキーバリューペアを示す画像。「key」は「judo-experience」、「value」はJudoリンクです。]({% image_buster /assets/img/judo/braze-campaign-extras-judo-experience.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

キャンペーンに[カスタムキーバリューペア]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs/)を設定します。キーは`judo-experience`です。ここに表示したいJudoエクスペリエンスのURLを入力します。その後、Judo-Braze統合ライブラリーはハンドラーでこのキーバリューペアを検出し、Judoエクスペリエンスを標準のBrazeアプリ内メッセージUIの代わりに挿入します。
<br><br>
### ステップ3：キャンペーンを完了する {#step-3-finishing-the-campaign}

最後に、キャンペーンを完了し、キャンペーンのトリガーを設定し、**配信**セクションと**ターゲットユーザー**セクションでセグメントからユーザーを選択します。Brazeアプリ内メッセージのさまざまなコンポーネントについては、アプリ内メッセージの[記事]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/)を参照してください。