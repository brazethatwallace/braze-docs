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

現在のメジャーバージョン（16.x以降）が、継続的なサポート、バグ修正、新機能の対象です。古いマイナーバージョンは継続的なメンテナンスを受けられない場合があります。

## 互換性ライブラリ {#compatibility-libraries}

### BrazeKitCompatとBrazeUICompatはSwift SDK 17.xで本番環境での使用がサポートされていますか？ {#are-brazekitcompat-and-brazeuicompat-supported-for-production-use-on-swift-sdk-17x}

はい、`BrazeKitCompat`と`BrazeUICompat`は移行期間中の本番環境での使用がサポートされています。これらは、最小限のコード変更でAppboy SDKからSwift SDKへ移行するための「踏み台」として位置づけられており、長期的な利用を目的としたものではありません。正式にサポートされておりバグ修正も引き続き行われていますが、最終的にはこれらの互換性ライブラリからモダンなSwift SDK APIへ移行することが意図されています。

### BrazeKitCompatとBrazeUICompatはいつ削除されますか？ {#when-will-brazekitcompat-and-brazeuicompat-be-removed}

Swift SDKチームは`BrazeKitCompat`ライブラリの廃止を計画していますが、具体的なタイムラインはまだ発表されていません。互換性ライブラリに無期限に依存するのではなく、モダンなSwift SDK API（`BrazeKit`、`BrazeUI`）への完全な移行を計画することをお勧めします。

## 遅延初期化 {#delayed-initialization}

### ユーザーの同意を得るまでSDKの初期化を遅延できますか？ {#can-i-delay-sdk-initialization-until-after-user-consent}

はい。Swift SDKは遅延初期化をサポートしており、SDKを開始する前にユーザーの同意を待つ必要があるアプリに便利です。`application(_:didFinishLaunchingWithOptions:)`の早い段階で`Braze.prepareForDelayedInitialization()`（オプションで`analyticsBehavior`パラメーターを指定）を呼び出し、同意を取得した後に標準のBrazeイニシャライザーを呼び出してSDKを初期化します。

詳細な実装については、[遅延初期化の設定]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift#step-2-set-up-delayed-initialization-optional)を参照してください。

### 遅延初期化に必要なSwift SDKの最小バージョンは何ですか？ {#what-is-the-minimum-swift-sdk-version-required-for-delayed-initialization}

Swift SDK 11.2.0が遅延初期化の最小バージョンです。遅延初期化におけるプッシュとディープリンクの堅牢性は、バージョン14.1.0でさらに改善されました。Swift SDK 17.0.0はこれらの両方のしきい値を十分に超えています。

### SDKが初期化される前に受信したイベントはどうなりますか？ {#what-happens-to-events-received-before-the-sdk-is-initialized}

SDKが初期化されると、キューに入れられたアイテムが処理されます。ただし、動作はチャネルによって異なります。

| チャネル | 初期化前の動作 |
|---------|----------------------------|
| プッシュトークン | キューに入れられ、初期化時に処理されます |
| プッシュの開封/分析 | デフォルトでキューに入れられます（`analyticsBehavior`でドロップするよう設定可能） |
| ディープリンク | キューに入れられ、初期化時に処理されます |
| アプリ内メッセージ | 初期化前にはバッファされません。SDKが実行中である必要があります |
| Content Cards | 初期化前にはバッファされません。初期化後にサーバーから同期されます |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
初期化前に受信したアプリ内メッセージとContent Cardsは、配信が保証されません。これらのチャネルを表示する前に、SDKが初期化されていることを確認してください。
{% endalert %}

## リソースバンドルとSPMインテグレーション {#resource-bundles-and-spm-integration}

### `braze-swift-sdk_BrazeUI.bundle`が見つからないというランタイムエラーが表示されるのはなぜですか？ {#why-am-i-seeing-a-runtime-error-about-missing-braze-swift-sdk_brazeuibundle}

これは既知のSDKバグではなく、インテグレーションの設定ミスが原因と考えられます。Swift SDK 12.0.0以降、静的XCFrameworksは外部リソースバンドルに依存する代わりに、リソースを直接含むようになっています。

### リソース埋め込みのSPM/Xcode/アーカイブ要件は何ですか？ {#what-are-the-spmxcodearchive-requirements-for-resource-embedding}

Swift SDK 12.0.0以降、Xcodeプロジェクト設定でBraze XCFrameworksに対して**Embed & Sign**を選択する必要があります。これは静的バリアントと動的バリアントの両方に適用されます。これが、アーカイブ時やリリース時にバンドルが見つからないエラーの最も一般的な原因です。

### 非標準のビルドシステムでリソースバンドルをオーバーライドするにはどうすればよいですか？ {#how-do-i-override-resource-bundles-for-non-standard-build-systems}

非標準のビルドシステム（Tuist、Bazel、Buck、CI）の場合は、承認済みのオーバーライドAPIを使用してください。

- `BrazeKit.overrideResourcesBundle`（複数形の「Resources」に注意）
- `BrazeUI.overrideResourcesBundle`（複数形の「Resources」に注意）

単数形の`overrideResourceBundle`はSwift SDK 8.1.0で非推奨となっており、使用すべきではありません。

## ユーザーIDとプッシュトークン {#user-identity-and-push-tokens}

### プロファイル、デバイスの関連付け、プッシュトークンを保持するための検証チェックリストはありますか？ {#is-there-a-validation-checklist-for-preserving-profiles-device-associations-and-push-tokens}

ドキュメントには移行専用の公式チェックリストは存在しません。以下の検証ステップを実行することをお勧めします。

1. 移行後に`registerDeviceToken`またはプッシュオートメーションが正しく接続されていることを確認します。
2. ロールアウトの前後でダッシュボードのプッシュ登録済みユーザー数を確認します。
3. いくつかの特定のexternal IDをスポットチェックして、デバイスの関連付けが維持されていることを確認します。

### `changeUser`はプッシュトークンが新しいユーザーに引き継がれることを保証しますか？ {#does-changeuser-guarantee-that-push-tokens-follow-the-new-user}

明示的な保証は文書化されていません。ただし、設計上の意図として、プッシュトークンはユーザーではなくデバイスに紐づきます。`changeUser`を呼び出すと、既存のデバイストークンが新しいユーザープロファイルに再関連付けされるはずです。大規模なロールアウトの前に、`changeUser`をテストし、ダッシュボードを確認して、トークンが新しいプロファイルに表示されることを確認してください。