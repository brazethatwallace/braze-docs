---
nav_title: Branch (ディープリンク)
article_title: Branch (ディープリンク)
alias: /partners/branch_for_deeplinking/
page_type: partner
description: "このリファレンス記事では、BrazeとBranchのパートナーシップと、これを利用してディープリンクをサポートする方法について説明します。"
search_tag: Partner

---

# Branch (ディープリンク) {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch](https://branch.io/)は、ユーザーのタッチポイントを包括的に把握することで、デバイス、チャネル、プラットフォームを横断して獲得、エンゲージメント、測定を行うためのモバイルリンクプラットフォームです。

*この統合はBranchによって管理されます。*

## 統合について {#about-the-integration}

BrazeとBranchの統合により、ユーザージャーニーの開始を適切に[アトリビューション]({{site.baseurl}}/partners/message_orchestration/attribution/branch_for_attribution/)し、ディープリンクを使用して目的のロケーションに顧客を接続することで、より優れたエクスペリエンスを顧客に提供できます。

{% alert tip %}
ユースケースに適したディープリンクのアプローチを選択するには、[iOSディープリンクガイド]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide/)を参照してください。
{% endalert %}

## 統合 {#integration}

[BranchのSDK統合ガイド](https://help.branch.io/developers-hub/docs/native-sdks-overview)に従って、Branch統合を稼働させます。その他のユースケースについては以下を参照してください。

### iOSユニバーサルリンクのサポート {#support-ios-universal-links}

BrazeからiOSユニバーサルリンクをディープリンクとして送信できるようにするには：

#### ステップ 1:Branchユニバーサルリンクの設定 {#step-1-set-up-branch-universal-links}

Branchのドキュメントに従って[ユニバーサルリンク](https://help.branch.io/developers-hub/docs/ios-universal-links)を設定します。この設定の一環として、BranchはAASAファイルをBranchリンクドメイン（例：`yourapp.app.link`）に自動的にホストします。

#### ステップ 2:Associated Domainsの設定 {#step-2-configure-associated-domains}

Xcodeで、アプリターゲット > **Signing & Capabilities** に移動し、**Associated Domains**にBranchリンクドメインを追加します：

```
applinks:yourapp.app.link
applinks:yourapp-alternate.app.link
```

カスタムBranchドメインを使用している場合は、それも追加してください。

#### ステップ 3:Brazeでユニバーサルリンクを転送する {#step-3-forward-universal-links-in-braze}

Braze SDKの設定で`forwardUniversalLinks`を`true`に設定し、SDKがユニバーサルリンクをアプリの`AppDelegate`に転送するようにします：

{% tabs %}
{% tab swift %}
`````````swift
let configuration = Braze.Configuration(apiKey: "<BRAZE_API_KEY>", endpoint: "<BRAZE_ENDPOINT>")
configuration.forwardUniversalLinks = true
let braze = Braze(configuration: configuration)
```
{% endtab %}
{% tab OBJECTIVE-C %}
`````````objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                                                  endpoint:@"<BRAZE_ENDPOINT>"];
configuration.forwardUniversalLinks = YES;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```
{% endtab %}
{% endtabs %}

#### ステップ 4:BrazeDelegateでBranchリンクをルーティングする {#step-4-route-branch-links-with-brazedelegate}

[`BrazeDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate)を実装して、Brazeが処理する前にBranchリンクをインターセプトします。これにより、Branchがリンクを処理し、独自のルーティングを実行できるようになります：

{% tabs %}
{% tab swift %}
`````````swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if let host = context.url.host,
     host.contains("app.link") || host.contains("yourdomain.com") {
    // Let Branch handle this link
    Branch.getInstance.handleDeepLink(context.url)
    return false
  }
  // Let Braze handle all other links
  return true
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
`````````objc
- (BOOL)braze:(Braze *)braze shouldOpenURL:(BRZURLContext *)context {
  NSString *host = context.url.host;
  if (host && ([host containsString:@"app.link"] || [host containsString:@"yourdomain.com"])) {
    [[Branch getInstance] handleDeepLink:context.url];
    return NO;
  }
  return YES;
}
```
{% endtab %}
{% endtabs %}

該当する場合は、`yourdomain.com`をカスタムBranchドメインに置き換えてください。

### メールでのディープリンク {#deep-linking-in-email}

[ユニバーサルリンクとアプリリンク]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/)に関するドキュメントを参照するか、[Branchのドキュメント](https://help.branch.io/developers-hub/docs/ios-universal-links#apps-that-always-work)を参照して、Braze経由で送信されるメールからのディープリンクを設定します。

ユーザーがアプリにコール権限を付与しない限り、iOS用のGmailアプリでは電話番号へのリンク（`href`に`tel`を付加）はサポートされません。

メールサービスプロバイダー (ESP) によっては、クリックトラッキングされたユニバーサルリンクをサポートするために追加のカスタマイズが必要になる場合があります。この情報については、専用の記事で紹介しています。詳しくは以下のリファレンスを参照してください：

- [SendGrid](https://help.branch.io/using-branch/page/braze-sendgrid)
- [SparkPost](https://help.branch.io/using-branch/page/braze-sparkpost)

## トラブルシューティング {#troubleshooting}

BrazeのキャンペーンからBranchリンクが期待どおりに動作しない場合は、以下のステップに従ってください。

### Braze外でリンクが動作するか確認する {#verify-the-link-works-outside-of-braze}

物理的なiOSデバイスのメモアプリからBranchリンクを開きます。アプリが開かない場合：

- 問題はBranchまたはAASAの設定にあり、Brazeの問題ではありません。
- `https://yourapp.app.link/.well-known/apple-app-site-association`でBranchのAASAを検証してください。
- BranchダッシュボードでBundle IDとTeam IDが一致していることを確認してください。

### デュアルロギングを有効にする {#enable-dual-logging}

1. **Braze**：[詳細ログを有効にし]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/)、`Opening '<URL>':`エントリを探します。これにより、SDKがリンクを受信したことが確認できます。
2. **Branch**：[Branchテストモード](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking)を有効にし、Branchダッシュボードでリンククリックイベントを確認します。
3. **比較**：Brazeがリンクをログに記録しているがBranchがクリックを検出していない場合、`BrazeDelegate`のルーティングロジックがリンクを正しくインターセプトしていない可能性があります。`shouldOpenURL`のドメインマッチにBranchドメインが含まれていることを確認してください。

### よくある問題 {#common-issues}

| 症状 | 考えられる原因 | 修正方法 |
|---|---|---|
| BranchリンクがSafariで開く | BranchドメインのAASAが無効または欠落 | Associated DomainsとAASAファイルを確認する |
| Branchリンクは開くが間違った画面に遷移する | Branchリンクデータの設定ミス | Branchダッシュボードでルーティングルールを確認する |
| プッシュからは動作するがメールからは動作しない | クリックトラッキングドメインにAASAが欠落 | メールサービスプロバイダー (ESP) のクリックトラッキングドメインにAASAをホストする。[メール設定](#deep-linking-in-email)を参照 |
| `shouldOpenURL`がBranchリンクに対して発火しない | `forwardUniversalLinks`が有効になっていない | `configuration.forwardUniversalLinks = true`を設定する |
| Branchリンクがメモアプリからは動作するがBrazeからは動作しない | `BrazeDelegate`がBranch URLに対して`true`を返している | `shouldOpenURL`のドメインチェックがBranchドメインと一致しているか確認する |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Common issues" }

その他のディープリンクのトラブルシューティングシナリオについては、[ディープリンクのトラブルシューティング]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting/)を参照してください。