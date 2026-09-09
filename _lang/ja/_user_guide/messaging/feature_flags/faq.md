---
nav_title: FAQ
article_title: よくある質問
page_order: 50
description: "このページでは、フィーチャーフラグに関するよくある質問への回答を提供します。"
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web
---

# よくある質問 {#frequently-asked-questions}

> この記事では、フィーチャーフラグに関するよくある質問への回答を提供します。

## 機能とサポート {#functionality-and-support}

### Brazeのフィーチャーフラグはどのプラットフォームでサポートされていますか？ {#platforms}

Brazeは、iOS、Android、Webプラットフォームで以下のSDKバージョン要件によりフィーチャーフラグをサポートしています。

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

他のプラットフォームのサポートが必要ですか？チームまでメールでお問い合わせください：[feature-flags-フィードバック@braze.com](mailto:feature-flags-feedback@braze.com)。

### フィーチャーフラグの実装にはどの程度の工数がかかりますか？ {#level-of-effort}

フィーチャーフラグは数分で作成・統合できます。

工数の大部分は、ロールアウトを計画している新機能を開発チームが構築することに関連します。しかし、フィーチャーフラグの追加に関しては、アプリやWebサイトのコードに`IF`/`ELSE`ステートメントを追加するだけのシンプルな作業です。

{% tabs %}
{% tab JavaScript %}

```javascript
import { getFeatureFlag } from "@braze/web-sdk";

if (getFeatureFlag("new_shopping_cart").enabled) {
    // Show the new homepage your team has built
}
else {
    // Show the old homepage
}
```

{% endtab %}
{% tab Java %}

```java
if (braze.getFeatureFlag("new_shopping_cart").getEnabled()) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
if (braze.getFeatureFlag("new_shopping_cart")?.enabled == true) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% endtabs %}

### フィーチャーフラグはマーケティングチームにどのようなメリットがありますか？ {#marketing-teams}

マーケティングチームは、機能が少数のユーザーにのみ有効化されている場合に、製品発表（製品ローンチメールなど）を調整するためにフィーチャーフラグを使用できます。

例えば、Brazeのフィーチャーフラグを使用すると、アプリ内のユーザーの10%に新しい顧客ロイヤルティプログラムをロールアウトし、キャンバスのフィーチャーフラグステップを使用して、その同じ10%の有効化されたユーザーにメール、プッシュ、またはその他のメッセージングを送信できます。

### フィーチャーフラグはプロダクトチームにどのようなメリットがありますか？ {#product-teams}

プロダクトチームは、フィーチャーフラグを使用して新機能の段階的ロールアウトやソフトローンチを行い、すべてのユーザーに公開する前にKPIや顧客フィードバックを監視できます。

プロダクトチームは、[フィーチャーフラグプロパティ]({{site.baseurl}}/developer_guide/feature_flags/create#accessing-properties)を使用して、ディープリンク、テキスト、画像、その他のダイナミックなコンテンツなど、アプリ内のコンテンツをリモートで配信できます。

また、キャンバスのフィーチャーフラグステップを使用することで、プロダクトチームはA/Bスプリットテストを実行し、新機能がコンバージョン率に与える影響を、機能が無効化されているユーザーと比較して測定できます。

### フィーチャーフラグは開発チームにどのようなメリットがありますか？ {#engineering-teams}

開発チームは、フィーチャーフラグを使用して新機能のローンチに伴うリスクを軽減し、深夜にコード修正を急いでデプロイする必要性を回避できます。

フィーチャーフラグの背後に隠された新しいコードをリリースすることで、チームはBrazeダッシュボードからリモートで機能のオン・オフを切り替えられ、新しいコードのプッシュやアプリストアの更新承認を待つ遅延を回避できます。

## 機能のロールアウトとターゲティング {#feature-rollouts-and-targeting}

### フィーチャーフラグを特定のユーザーグループにのみロールアウトできますか？ {#target-users}

はい、Brazeでメールアドレス、`user_id`、またはユーザープロファイルの任意の属性に基づいて特定のユーザーをターゲットとするセグメントを作成してください。その後、そのセグメントの100%に対してフィーチャーフラグをデプロイします。

### ロールアウト割合を調整すると、以前に有効グループに割り当てられたユーザーにどのような影響がありますか？ {#random-buckets}

フィーチャーフラグのロールアウトは、デバイスやセッションをまたいでユーザーに対して一貫性が維持されます。

- フィーチャーフラグがランダムなユーザーの10%にロールアウトされた場合、その10%は有効なままとなり、そのフィーチャーフラグの存続期間中維持されます。
- ロールアウトを10%から20%に増やした場合、同じ10%は有効なままとなり、さらに新たな10%のユーザーが有効グループに追加されます。
- ロールアウトを20%から10%に下げた場合、元の10%のユーザーのみが有効なままとなります。

この戦略により、アプリ内でユーザーに一貫したエクスペリエンスが表示され、セッションをまたいで有効と無効が切り替わることがなくなります。もちろん、機能を0%に無効化すると、すべてのユーザーがフィーチャーフラグから除外されます。これはバグを発見した場合や、機能を完全に無効化する必要がある場合に役立ちます。

## 技術的なトピック {#technical-topics}

### フィーチャーフラグを使ってBraze SDKの初期化タイミングを制御できますか？ {#initialization}

いいえ、SDKは現在のユーザーのフィーチャーフラグをダウンロードおよび同期するために初期化する必要があります。つまり、フィーチャーフラグを使用して、Brazeで作成またはトラッキングされるユーザーを制限することはできません。

### SDKはどのくらいの頻度でフィーチャーフラグを更新しますか？ {#refresh-frequency}

フィーチャーフラグはセッション開始時およびアクティブユーザーの切り替え時に更新されます。また、SDKの[更新メソッド]({{site.baseurl}}/developer_guide/feature_flags/create#refreshing)を使用して手動で更新することもできます。フィーチャーフラグの更新は5分に1回にレート制限されています（変更される場合があります）。

適切なデータプラクティスとして、フィーチャーフラグを頻繁に更新しすぎないことが推奨されます（頻繁すぎるとレート制限がかかる可能性があります）。ユーザーが新しい機能を操作する前、またはアプリ内で必要に応じて定期的に更新するのが最善です。

### ユーザーがオフラインのときにフィーチャーフラグは利用できますか？ {#offline}

はい、フィーチャーフラグが更新された後はユーザーのデバイスにローカルに保存され、オフライン中でもアクセスできます。

### セッション中にフィーチャーフラグが更新された場合はどうなりますか？ {#listen-for-updates}

フィーチャーフラグはセッション中に更新される場合があります。特定の変数や設定が変更された場合にアプリを更新したいシナリオがあります。一方で、UIの表示が急に変わることを避けるために、アプリを更新したくないシナリオもあります。

これを制御するには、フィーチャーフラグの[更新をリッスン]({{site.baseurl}}/developer_guide/feature_flags/create#updates)し、どのフィーチャーフラグが変更されたかに基づいてアプリを再レンダリングするかどうかを判断します。

### グローバルコントロールグループのユーザーがフィーチャーフラグ実験を受信しないのはなぜですか？ {#why-arent-users-in-my-global-control-group-receiving-feature-flags-experiments}

[グローバルコントロールグループ]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts)のユーザーに対してフィーチャーフラグを有効にすることはできません。そのため、グローバルコントロールグループのユーザーはフィーチャーフラグ実験に参加することもできません。

### メールベースの受信者識別はBrazeフィーチャーフラグの一部ですか？ {#is-email-based-recipient-identification-part-of-braze-feature-flags}

いいえ。メッセージ送信時にメールで受信者を識別する機能は、このページのフィーチャーフラグ製品の一部ではありません。フィーチャーフラグは、Braze SDKを通じてアプリ内またはサイト上のエクスペリエンスを制御するものです。

APIトリガーのキャンペーンおよびキャンバス送信では、`external_user_id`の代わりに[受信者オブジェクト]({{site.baseurl}}/api/objects_filters/recipient_object)に`email`を含めることができます。`email`を使用する場合は、Brazeが一致するユーザープロファイルを選択できるように`prioritization`を含めてください。この送信オプションはすべてのワークスペースで利用できるわけではありません。

リクエスト形式については、[POST: APIトリガー配信を使用してキャンペーンを送信する]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)および[POST: APIトリガー配信を使用してキャンバスメッセージを送信する]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)を参照してください。

## その他のご質問は？ {#additional-questions}

ご質問やフィードバックがありましたら、チームまでメールでお問い合わせください：[feature-flags-フィードバック@braze.com](mailto:feature-flags-feedback@braze.com)。