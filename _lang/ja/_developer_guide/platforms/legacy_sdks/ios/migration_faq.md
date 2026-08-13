---
nav_title: 移行に関するFAQ
article_title: iOS SDK移行FAQ
platform: iOS
page_order: 12
description: "このページでは、Appboy iOS SDK（Objective-C）からBraze Swift SDKへの移行に関するよくある質問にお答えします。"
noindex: true
---

# iOS SDK移行FAQ {#ios-sdk-migration-faq}

> このページでは、レガシーのAppboy iOS SDK（Objective-C SDKとも呼ばれます）からBraze Swift SDKへの移行に関するよくある質問にお答えします。

{% multi_lang_include deprecations/objective-c.md %}

## バージョンサポートとサポート終了 {#version-support-and-end-of-life}

### Appboy iOS SDK 4.7.0はサポート終了ですか？ {#is-appboy-ios-sdk-470-end-of-life}

はい、Appboy iOS SDK 4.7.0（およびすべての4.xバージョン）はサポート終了となっています。セキュリティ修正や重大なバグ修正は提供されません。メッセージングと分析は引き続き正常に機能しますが、バージョン4.7.0はセキュリティの観点からサポート対象外として扱う必要があります。

### 本番環境でサポートされるSwift SDKの最小バージョンは何ですか？ {#what-is-the-minimum-swift-sdk-version-for-production-support}

現在のメジャーバージョン（16.x以降）が、継続的なサポート、バグ修正、および新機能の対象です。古いマイナーバージョンは、継続的なメンテナンスを受けられない場合があります。

## 互換性ライブラリ {#compatibility-libraries}

### BrazeKitCompatとBrazeUICompatはSwift SDK 17.xで本番環境での使用がサポートされていますか？ {#are-brazekitcompat-and-brazeuicompat-supported-for-production-use-on-swift-sdk-17x}

はい、`BrazeKitCompat`と`BrazeUICompat`は移行期間中の本番環境での使用がサポートされています。これらは、Appboy SDKからSwift SDKへ最小限のコード変更で移行するための「踏み台」として位置づけられており、長期的な利用を想定したものではありません。正式にサポートされておりバグ修正も引き続き行われていますが、最終的にはこれらの互換性ライブラリからモダンなSwift SDK APIへ移行することが意図されています。

### BrazeKitCompatとBrazeUICompatはいつ削除されますか？ {#when-will-brazekitcompat-and-brazeuicompat-be-removed}

Swift SDKチームは`BrazeKitCompat`ライブラリのサンセット（提供終了）を計画していますが、具体的なタイムラインはまだ発表されていません。互換性ライブラリに無期限に依存するのではなく、モダンなSwift SDK API（`BrazeKit`、`BrazeUI`）への完全な移行を計画することをお勧めします。

## 初期化の遅延 {#delayed-initialization}

### SDKの初期化をユーザーの同意後まで遅らせることはできますか？ {#can-i-delay-sdk-initialization-until-after-user-consent}

はい。Swift SDKは初期化の遅延をサポートしており、SDKを開始する前にユーザーの同意を待つ必要があるアプリに便利です。`application(_:didFinishLaunchingWithOptions:)` の早い段階で `Braze.prepareForDelayedInitialization()`（オプションで `analyticsBehavior` パラメーターを指定可能）を呼び出し、同意が得られた後に標準のBraze初期化メソッドを呼び出してSDKを初期化します。

詳細な実装については、[初期化の遅延を設定する]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift#swift_step-2-set-up-delayed-initialization-optional)を参照してください。

### 初期化の遅延に必要なSwift SDKの最小バージョンは何ですか？ {#what-is-the-minimum-swift-sdk-version-required-for-delayed-initialization}

Swift SDK 11.2.0が初期化の遅延に必要な最小バージョンです。初期化の遅延におけるプッシュおよびディープリンクの堅牢性は、バージョン14.1.0でさらに改善されました。Swift SDK 17.0.0はこれらの両方のしきい値を十分に超えています。

### SDKが初期化される前に受信したイベントはどうなりますか？ {#what-happens-to-events-received-before-the-sdk-is-initialized}

SDKが初期化されると、キューに入れられたアイテムが処理されます。ただし、動作はチャネルによって異なります。

| チャネル | 初期化前の動作 |
|---------|----------------------------|
| プッシュトークン | キューに入れられ、初期化時に処理されます |
| プッシュの開封/分析 | デフォルトでキューに入れられます（`analyticsBehavior` でドロップするように設定可能） |
| ディープリンク | キューに入れられ、初期化時に処理されます |
| アプリ内メッセージ | 初期化前にはバッファリングされません。SDKが実行中である必要があります |
| Content Cards | 初期化前にはバッファリングされません。初期化後にサーバーから同期されます |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
初期化前に受信したアプリ内メッセージとContent Cardsは、配信が保証されません。これらのチャネルを表示する前に、SDKが初期化されていることを確認してください。
{% endalert %}

## リソースバンドルとSPMの統合 {#resource-bundles-and-spm-integration}

### `braze-swift-sdk_BrazeUI.bundle`が見つからないというランタイムエラーが表示されるのはなぜですか？ {#why-am-i-seeing-a-runtime-error-about-missing-braze-swift-sdk_brazeuibundle}

これは既知のSDKバグではなく、統合の設定ミスが原因である可能性が高いです。Swift SDK 12.0.0以降、静的XCFrameworksは外部リソースバンドルに依存する代わりに、リソースを直接含むようになりました。

### SPM/Xcode/アーカイブにおけるリソース埋め込みの要件は何ですか？ {#what-are-the-spmxcodearchive-requirements-for-resource-embedding}

Swift SDK 12.0.0以降、Xcodeプロジェクト設定でBraze XCFrameworksに対して**Embed & Sign**を選択する必要があります。これは静的バリアントとダイナミックバリアントの両方に適用されます。アーカイブ時やリリース時にバンドルが見つからないエラーが発生する最も一般的な原因です。

### 非標準のビルドシステムでリソースバンドルをオーバーライドするにはどうすればよいですか？ {#how-do-i-override-resource-bundles-for-non-standard-build-systems}

非標準のビルドシステム（Tuist、Bazel、Buck、CI）では、承認済みのオーバーライドAPIを使用してください：

- `BrazeKit.overrideResourcesBundle`（複数形の「Resources」であることに注意）
- `BrazeUI.overrideResourcesBundle`（複数形の「Resources」であることに注意）

単数形の`overrideResourceBundle`はSwift SDK 8.1.0で非推奨となっており、使用しないでください。

## ユーザーIDとプッシュトークン {#user-identity-and-push-tokens}

### プロファイル、デバイスの関連付け、プッシュトークンを保持するための検証チェックリストはありますか？ {#is-there-a-validation-checklist-for-preserving-profiles-device-associations-and-push-tokens}

ドキュメントには、移行に特化した公式チェックリストは存在しません。以下の検証ステップを実施することをお勧めします。

1. 移行後に`registerDeviceToken`またはプッシュのオートメーションが正しく接続されていることを確認します。
2. ロールアウトの前後で、ダッシュボードのプッシュ登録済みユーザー数を確認します。
3. いくつかの特定のexternal IDをスポットチェックして、デバイスの関連付けが維持されていることを確認します。

### `changeUser`はプッシュトークンが新しいユーザーに引き継がれることを保証しますか？ {#does-changeuser-guarantee-that-push-tokens-follow-the-new-user}

ドキュメントに明示的な保証は記載されていません。ただし、設計上の意図として、プッシュトークンはユーザーではなくデバイスに紐づきます。`changeUser`を呼び出すと、既存のデバイストークンが新しいユーザープロファイルに再関連付けされます。大規模なロールアウトの前に、`changeUser`をテストし、ダッシュボードを確認して、新しいプロファイルにトークンが表示されることを確認してください。