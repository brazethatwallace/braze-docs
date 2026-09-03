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

### Brazeフィーチャーフラグはどのプラットフォームでサポートされていますか？ {#platforms}

Brazeは、iOS、Android、Webプラットフォームで、以下のSDKバージョン要件を満たすフィーチャーフラグをサポートしています。

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

他のプラットフォームでのサポートが必要ですか？チームにメールでお問い合わせください：[feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com)。

### フィーチャーフラグの実装にはどの程度の工数がかかりますか？ {#level-of-effort}

フィーチャーフラグは数分で作成・統合できます。

工数の大部分は、ロールアウトを計画している新機能を開発チームが構築することに関連しています。しかし、フィーチャーフラグの追加に関しては、アプリやWebサイトのコードで`IF`/`ELSE`ステートメントを記述するだけのシンプルな作業です。

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

### マーケティングチームはフィーチャーフラグをどのように活用できますか？ {#marketing-teams}

マーケティングチームは、機能がユーザーの一部にのみ有効化されている場合に、製品のお知らせ（製品ローンチメールなど）を調整するためにフィーチャーフラグを使用できます。

例えば、Brazeフィーチャーフラグを使用すると、アプリ内のユーザーの10%に新しい顧客ロイヤルティプログラムをロールアウトし、キャンバスのフィーチャーフラグステップを使用して、同じ10%の有効化されたユーザーにメール、プッシュ、またはその他のメッセージングを送信できます。

### プロダクトチームはフィーチャーフラグをどのように活用できますか？ {#product-teams}

プロダクトチームは、新機能の段階的なロールアウトやソフトローンチを行い、すべてのユーザーに提供する前にKPIや顧客フィードバックを監視するためにフィーチャーフラグを使用できます。

プロダクトチームは[フィーチャーフラグのプロパティ]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#properties)を使用して、ディープリンク、テキスト、画像、その他のダイナミックなコンテンツなど、アプリ内のコンテンツをリモートで更新できます。

キャンバスのフィーチャーフラグステップを使用すると、プロダクトチームはA/Bスプリットテストを実施し、新機能がコンバージョン率に与える影響を、機能が無効化されたユーザーと比較して測定できます。

### 開発チームはフィーチャーフラグをどのように活用できますか？ {#engineering-teams}

開発チームは、新機能のリリースに伴うリスクを軽減し、深夜にコード修正を急いでデプロイすることを避けるためにフィーチャーフラグを使用できます。

フィーチャーフラグの背後に隠して新しいコードをリリースすることで、チームはBrazeダッシュボードからリモートで機能のオン・オフを切り替えることができ、新しいコードのプッシュやアプリストアの更新承認を待つ遅延を回避できます。

## フィーチャーフラグのロールアウトとターゲティング {#feature-rollouts-and-targeting}

### フィーチャーフラグを特定のユーザーグループにのみロールアウトできますか？ {#target-users}

はい。Brazeで特定のユーザーをターゲットとするセグメントを作成します。メールアドレス、`user_id`、またはユーザープロファイルのその他の属性を使用してターゲティングできます。その後、そのセグメントの100%に対してフィーチャーフラグをデプロイします。

### ロールアウトのパーセンテージを調整すると、以前に有効グループに割り当てられたユーザーにどのような影響がありますか？ {#random-buckets}

フィーチャーフラグのロールアウトは、デバイスやセッションをまたいでユーザーに対して一貫性を保ちます。

- フィーチャーフラグがランダムなユーザーの10%にロールアウトされた場合、その10%は有効なまま維持され、そのフィーチャーフラグの存続期間中持続します。
- ロールアウトを10%から20%に増やした場合、同じ10%は引き続き有効のままで、さらに新たに10%のユーザーが有効グループに追加されます。
- ロールアウトを20%から10%に下げた場合、元の10%のユーザーのみが有効のまま維持されます。

この戦略により、ユーザーにはアプリ内で一貫した体験が提供され、セッション間で有効・無効が切り替わることがなくなります。もちろん、機能を0%に無効化すれば、フィーチャーフラグからすべてのユーザーが削除されます。これは、バグを発見した場合や機能全体を無効にする必要がある場合に役立ちます。

## 技術的なトピック {#technical-topics}

### フィーチャーフラグを使用してBraze SDKの初期化タイミングを制御できますか？ {#initialization}

いいえ、SDKは現在のユーザーのフィーチャーフラグをダウンロードおよび同期するために初期化される必要があります。つまり、フィーチャーフラグを使用して、Brazeで作成またはトラッキングされるユーザーを制限することはできません。

### SDKはどのくらいの頻度でフィーチャーフラグを更新しますか？ {#refresh-frequency}

フィーチャーフラグはセッション開始時およびアクティブユーザーの切り替え時に更新されます。また、SDKの[更新メソッド]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#refreshing)を使用して手動で更新することもできます。フィーチャーフラグの更新は5分に1回にレート制限されています（変更される場合があります）。

適切なデータプラクティスとして、フィーチャーフラグを頻繁に更新しすぎないことが推奨されます（頻繁に更新するとレート制限がかかる可能性があります）。ユーザーが新しい機能を利用する前、または必要に応じてアプリ内で定期的に更新するのが最善です。

### ユーザーがオフラインの場合、フィーチャーフラグは利用できますか？ {#offline}

はい、フィーチャーフラグは更新後にユーザーのデバイスにローカルに保存されるため、オフライン中でもアクセスできます。

### セッション中にフィーチャーフラグが更新された場合はどうなりますか？ {#listen-for-updates}

フィーチャーフラグはセッション中に更新される場合があります。特定の変数や設定が変更された場合にアプリを更新したいシナリオもあります。一方で、UIの表示が急激に変わるのを避けるために、アプリを更新したくないシナリオもあります。

これを制御するには、フィーチャーフラグの[更新をリッスン]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#updates)し、どのフィーチャーフラグが変更されたかに基づいてアプリを再レンダリングするかどうかを判断してください。

### グローバルコントロールグループのユーザーがフィーチャーフラグの実験を受信しないのはなぜですか？ {#why-arent-users-in-my-global-control-group-receiving-feature-flags-experiments}

[グローバルコントロールグループ]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts)のユーザーに対してフィーチャーフラグを有効にすることはできません。つまり、グローバルコントロールグループのユーザーはフィーチャーフラグの実験に参加することもできません。

### メールベースの受信者識別はBrazeフィーチャーフラグの一部ですか？ {#is-email-based-recipient-identification-part-of-braze-feature-flags}

いいえ。メッセージ送信時にメールで受信者を識別する機能は、このページのフィーチャーフラグ製品には含まれていません。フィーチャーフラグは、Braze SDKを通じてアプリ内またはサイト上のエクスペリエンスを制御します。

APIトリガーのキャンペーンおよびキャンバスの送信では、`external_user_id`の代わりに[受信者オブジェクト]({{site.baseurl}}/api/objects_filters/recipient_object)に`email`を含めることができます。`email`を使用する場合は、Brazeが一致するユーザープロファイルを選択できるように`prioritization`を含めてください。この送信オプションはすべてのワークスペースで利用できるわけではありません。

リクエストの形式については、[POST: APIトリガー配信を使用したキャンペーンの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)および[POST: APIトリガー配信を使用したキャンバスメッセージの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)を参照してください。

## その他のご質問がありますか？ {#additional-questions}

ご質問やフィードバックがありましたら、チームまでメールでお問い合わせください：[feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com)。