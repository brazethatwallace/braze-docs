---
page_order: 1.1
nav_title: iOSディープリンクガイド
article_title: iOSディープリンクガイド
description: "iOSアプリでどのタイプのディープリンクを使用すべきか、AASAファイルが必要な場合、および実装すべきアプリデリゲートメソッドについて説明します。"
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# iOSディープリンクガイド {#ios-deep-linking-guide}

> このガイドでは、使用するメッセージングチャネルやBranchなどのサードパーティリンクプロバイダーの利用有無に応じて、iOSアプリに適したディープリンク戦略を選択する方法を説明します。

実装の詳細については、[ディープリンク]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=swift)を参照してください。トラブルシューティングについては、[ディープリンクのトラブルシューティング]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting)を参照してください。

## リンクの種類を選ぶ {#choosing-a-link-type}

iOSアプリでBrazeメッセージからのリンクを処理する方法は3つあります。それぞれ動作が異なり、適したチャネルやユースケースも異なります。

| リンクの種類 | 例 | 最適な用途 | アプリ未インストールでも開けるか？ |
|---|---|---|---|
| **カスタムスキーム** | `myapp://products/123` | プッシュ通知、アプリ内メッセージ、Content Cards | いいえ — リンクは失敗します |
| **ユニバーサルリンク** | `https://myapp.com/products/123` | メール、SMS、クリックトラッキング付きチャネル | はい — Webにフォールバックします |
| **アプリ内でWeb URLを開く** | 任意の `https://` URL | モーダルWebViewでWebコンテンツを表示する | N/A — WebViewに表示されます |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="リンクの種類を選ぶ" }

### カスタムスキームディープリンク {#custom-scheme-deep-links}

カスタムスキームディープリンク（例：`myapp://products/123`）は、アプリを特定の画面に直接開きます。リンクがサードパーティによって変更されないチャネルにおいて、最もシンプルな選択肢です。

**カスタムスキームディープリンクを使用する場合：**
- プッシュ通知、アプリ内メッセージ、またはContent Cardsを送信する場合
- アプリがインストールされていない場合にリンクが機能する必要がない場合
- クリックトラッキング（メールESPリンクラッピング）が不要な場合

**カスタムスキームディープリンクを使用しない場合：**
- メールを送信する場合 — メールサービスプロバイダー (ESP)がクリックトラッキングのためにリンクをラップするため、カスタムスキームが機能しなくなります
- アプリがインストールされていない場合にWebページへフォールバックするリンクが必要な場合

### ユニバーサルリンク {#universal-links}

ユニバーサルリンク（例：`https://myapp.com/products/123`）は標準的なHTTPS URLであり、iOSはブラウザで開く代わりにアプリにルーティングできます。サーバー側の設定（AASAファイル）とアプリ側の設定（Associated Domainsエンタイトルメント）が必要です。

**ユニバーサルリンクを使用する場合：**
- メールを送信する場合。メールサービスプロバイダー (ESP)がクリックトラッキングのためにリンクをラップするため、リンクはHTTPSである必要があります。
- SMSやその他のチャネルで、リンクがラップまたは短縮される場合。
- アプリがインストールされていない場合にWebページへフォールバックするリンクが必要な場合。
- BranchやAppsFlyerなどのサードパーティリンクプロバイダーを使用している場合。

**ユニバーサルリンクを使用しない場合：**
- プッシュ通知、アプリ内メッセージ、またはContent Cardsからのディープリンクのみが必要な場合。カスタムスキームの方がシンプルです。

### 「アプリ内でWeb URLを開く」 {#open-web-url-inside-app}

このオプションは、アプリ内のモーダルWebViewでWebページを開きます。Braze SDKの`Braze.WebViewController`によって完全に処理されるため、URL処理コードを記述する必要はありません。

**「アプリ内でWeb URLを開く」を使用する場合：**
- アプリを離れることなくWebページ（プロモーションや記事など）を表示したい場合。
- URLが標準的なHTTPS Webページであり、特定のアプリ画面へのディープリンクではない場合。

**「アプリ内でWeb URLを開く」を使用しない場合：**
- アプリ内の特定のビューに移動する必要がある場合。代わりにカスタムスキームまたはユニバーサルリンクを使用してください。
- Webページが認証を必要とする場合、または埋め込みをブロックするContent Security Policyヘッダーがある場合。

## 各リンクタイプに必要なもの {#what-you-need-for-each-link-type}

### カスタムスキームディープリンク

| 要件 | 詳細 |
|---|---|
| AASAファイル | 不要 |
| `Info.plist` | `CFBundleURLTypes`にスキームを登録し、`LSApplicationQueriesSchemes`に追加します |
| アプリデリゲートメソッド | `application(_:open:options:)`を実装してURLを解析しナビゲーションします |
| Braze SDKの設定 | なし — SDKはデフォルトでカスタムスキームURLを開きます |
{: .reset-td-br-1 .reset-td-br-2 aria-label="カスタムスキームディープリンク" }

### ユニバーサルリンク

| 要件 | 詳細 |
|---|---|
| AASAファイル | 必須 — `https://yourdomain.com/.well-known/apple-app-site-association`にホストします |
| Associated Domains | Xcodeの**Signing & Capabilities**で`applinks:yourdomain.com`を追加します |
| アプリデリゲートメソッド | `application(_:continue:restorationHandler:)`を実装して`NSUserActivity`を処理します |
| Braze SDKの設定 | `configuration.forwardUniversalLinks = true`を設定します |
| BrazeDelegate（オプション） | カスタムルーティング（例：Branch）のために`braze(_:shouldOpenURL:)`を実装します |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユニバーサルリンク" }

{% alert important %}
Braze経由でメールを送信する場合、メールサービスプロバイダー (ESP)（SendGrid、SparkPost、またはAmazon SES）がリンクをクリックトラッキングドメインでラップします。AASAファイルは、メインドメインだけでなくクリックトラッキングドメインにもホストする必要があります。完全な設定については、[ユニバーサルリンクとアプリリンク]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links)を参照してください。
{% endalert %}

### 「アプリ内でWeb URLを開く」

| 要件 | 詳細 |
|---|---|
| AASAファイル | 不要 |
| アプリデリゲートメソッド | 不要 — SDKが自動的に処理します |
| Braze SDKの設定 | なし — キャンペーンコンポーザーで**Open Web URL Inside App**を選択します |
{: .reset-td-br-1 .reset-td-br-2 aria-label="アプリ内でWeb URLを開く" }

## AASAファイルが必要な場合 {#when-aasa}

Apple App Site Association（AASA）ファイルは、**ユニバーサルリンク**を使用する場合にのみ必要です。AASAファイルは、アプリが処理できるURLをiOSに伝えます。

AASAファイルが必要な場合：

- メールキャンペーンでディープリンクを送信する場合（メールサービスプロバイダー (ESP)がリンクをHTTPSクリックトラッキングURLでラップするため）。
- SMSキャンペーンでディープリンクを送信する場合（リンクがHTTPS URLに短縮される可能性があるため）。
- Branch、AppsFlyer、またはその他のリンクプロバイダーを使用する場合（独自のHTTPSドメインを使用するため）。
- プッシュ通知、アプリ内メッセージ、またはContent Cardsからユニバーサルリンクを使用する場合（一般的ではありませんが、`forwardUniversalLinks = true`で可能です）。

AASAファイルが不要な場合：

- プッシュ通知、アプリ内メッセージ、またはContent Cardsからカスタムスキームディープリンク（例：`myapp://`）のみを使用する場合。
- **Open Web URL Inside App**オプションを使用する場合。

AASAの設定手順については、[ユニバーサルリンクとアプリリンク]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links#setting-up-universal-links-and-app-links)を参照してください。

## リンクを処理するためにアプリコードが必要な場合 {#when-app-code}

実装するデリゲートメソッドは、使用するリンクの種類によって異なります。

| デリゲートメソッド | 処理対象 | 実装するタイミング |
|---|---|---|
| `application(_:open:options:)` | カスタムスキームディープリンク（`myapp://`） | 任意のチャネルからカスタムスキームディープリンクを使用する場合 |
| `application(_:continue:restorationHandler:)` | ユニバーサルリンク（`https://`） | メール、SMSから、または`forwardUniversalLinks = true`でユニバーサルリンクを使用する場合 |
| `BrazeDelegate.braze(_:shouldOpenURL:)` | SDKによって開かれるすべてのURL | カスタムルーティングロジックが必要な場合（例：Branch、条件分岐処理、分析） |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="リンクを処理するためにアプリコードが必要な場合" }

{% alert tip %}
Branchなどのサードパーティリンクプロバイダーを使用する場合は、`BrazeDelegate.braze(_:shouldOpenURL:)`を実装してURLをインターセプトし、プロバイダーのSDKに転送します。完全な例については、[ディープリンク用のBranch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking)を参照してください。
{% endalert %}

## BrazeとBranchを併用する {#branch}

[Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking)をリンクプロバイダーとして使用する場合、標準的なユニバーサルリンクの設定に加えて、いくつかの追加ステップが必要です。

1. **Branch SDK**：[Branchのドキュメント](https://help.branch.io/developers-hub/docs/native-sdks-overview)に従ってBranch SDKを統合します。
2. **Associated Domains**：Xcodeの**Signing & Capabilities**でBranchドメイン（例：`applinks:yourapp.app.link`）を追加します。
3. **BrazeDelegate**：BranchリンクをBrazeが直接処理するのではなく、Branch SDKにルーティングするために`braze(_:shouldOpenURL:)`を実装します。
4. **ユニバーサルリンクの転送**：Braze SDKの設定で`configuration.forwardUniversalLinks = true`を設定します。

実装の詳細とデバッグのガイダンスについては、[ディープリンク用のBranch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking)を参照してください。