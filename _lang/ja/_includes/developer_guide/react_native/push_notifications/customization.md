{% multi_lang_include developer_guide/prerequisites/react_native.md %} また、[プッシュ通知を設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native)する必要があります。

## React Nativeでのプッシュ通知カスタマイズ {#push-customization-in-react-native}

Braze React Native SDKは、JavaScript APIを通じてプッシュ通知のカスタマイズ（アクションボタン、カテゴリ、カスタム通知ファクトリ）を公開していません。これらの機能には、iOSおよびAndroidプロジェクトでのネイティブ設定が必要です。

以下の表は、どの機能にネイティブ設定が必要かを示しています。

| 機能 | iOS | Android |
| --- | --- | --- |
| アクションボタン | ネイティブのSwift/Objective-Cで設定 | ネイティブのJava/Kotlinで設定 |
| プッシュカテゴリ | ネイティブのSwift/Objective-Cで設定 | ネイティブのJava/Kotlinで設定 |
| カスタム通知ファクトリ | N/A | ネイティブのJava/Kotlinで設定 |
| バッジのカスタマイズ | ネイティブのSwift/Objective-Cで設定 | N/A |
| カスタムサウンド | ネイティブのSwift/Objective-Cで設定 | ネイティブのJava/Kotlinで設定 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="React Nativeでのプッシュ通知カスタマイズ" }

### iOSのカスタマイズ {#ios-customization}

iOSでプッシュアクションボタン、カテゴリ、バッジ、またはカスタムサウンドを追加するには、`AppDelegate`（SwiftまたはObjective-C）でネイティブ設定を実装します。ステップバイステップの手順については、[プッシュ通知をカスタマイズする – Swift]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift)を参照してください。

### Androidのカスタマイズ {#android-customization}

Androidでプッシュアクションボタン、カテゴリ、またはカスタム通知ファクトリを追加するには、Androidプロジェクト内でネイティブ設定を実装します。ステップバイステップの手順については、[プッシュ通知をカスタマイズする – Android]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android)を参照してください。