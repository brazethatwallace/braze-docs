---
nav_title: "ユニバーサルリンクとApp Links"
article_title: "ユニバーサルリンクとApp Links"
page_order: 6.4
page_type: reference
description: "この記事では、Appleユニバーサルリンクと Android App Linksの設定方法について説明します。"
channel: email
---

# ユニバーサルリンクとApp Links {#universal-links-and-app-links}

> この記事では、Appleユニバーサルリンクと Android App Linksの設定方法について説明します。

{% alert tip %}
すべてのメッセージングチャネルにおけるリンクタイプの比較と、AASAファイルが必要なタイミングに関するガイダンスについては、[iOSディープリンクガイド]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide)を参照してください。
{% endalert %}

Appleユニバーサルリンクと Android App Linksは、Webコンテンツとモバイルアプリ間のシームレスな遷移を提供するために考案されたメカニズムです。ユニバーサルリンクはiOS固有のものですが、Android App LinksはAndroidアプリケーションで同じ目的を果たします。

## ユニバーサルリンクとApp Linksの仕組み {#how-universal-links-and-app-links-work}

ユニバーサルリンク（iOS）とApp Links（Android）は、Webページとアプリ内のコンテンツの両方を指す標準的なWebリンク（`http://mydomain.com`）です。

ユニバーサルリンクまたはApp Linksが開かれると、オペレーティングシステムは、そのドメインに登録されたインストール済みアプリがあるかどうかを確認します。アプリが見つかった場合、Webページを読み込むことなく、すぐにアプリが起動します。アプリが見つからない場合は、ユーザーのデフォルトWebブラウザーでWeb URLが読み込まれます。このとき、App StoreまたはGoogle Play Storeへのリダイレクトが設定されている場合もあります。

簡単に言うと、ユニバーサルリンクを使うことで、Webサイトのページを特定のアプリ画面に関連付けることができます。ユーザーがアプリ画面に対応するWebページのリンクをクリックすると、（アプリがインストールされている場合は）アプリを直接開くことができます。

{% alert important %}
Firebase Dynamic Linksは非推奨です。BrazeはFirebaseと直接統合しておらず、ディープリンクはBrazeプラットフォームの外部で管理されます。プラットフォームネイティブのソリューション（この記事で説明しているAppleユニバーサルリンクとAndroid App Links）、または代替のディープリンクサービスプロバイダーに移行してください。移行ガイダンスについては、[Firebaseの移行FAQ](https://firebase.google.com/support/dynamic-links-faq)を参照してください。
{% endalert %}

次の表は、ユニバーサルリンクと従来のディープリンクの主な違いをまとめたものです。

|                        | ユニバーサルリンクとApp Links                                  | ディープリンク                   |
| ---------------------- | -------------------------------------------------------------- | ---------------------------- |
| プラットフォームの互換性 | iOS（バージョン9以降）およびAndroid（バージョン6.0以降）  | さまざまなモバイルOSで使用    |
| 目的                | iOSおよびAndroidデバイスでWebとアプリのコンテンツをシームレスにリンク | 特定のアプリコンテンツへのリンク |
| 機能               | コンテキストに基づいてWebページまたはアプリコンテンツに誘導           | 特定のアプリ画面を開く   |
| アプリのインストール       | アプリがインストールされている場合はアプリを開き、それ以外の場合はWebコンテンツを開く | アプリがインストールされている必要がある |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ユニバーサルリンクとApp Linksの仕組み" }

## ユースケース {#use-cases}

ユニバーサルリンクとApp Linksは、メールキャンペーンで最もよく使用されます。メールはデスクトップとモバイルデバイスの両方から開封およびクリックできるためです。

一部のチャネルでは、これらのリンクがうまく機能しません。たとえば、プッシュ通知、アプリ内メッセージ、Content Cardsでは、スキームベースのディープリンク（`mydomain://`）を使用する必要があります。

{% alert note %}
Android App Linksでは、ドメインからのリンクを他のWeb URLとは別に処理するロジックを持つカスタム`IBrazeDeeplinkHandler`が必要です。ディープリンクを使用し、メール以外のチャネルではリンクの方法を統一する方が簡単な場合があります。
{% endalert %}

## 前提条件 {#prerequisites}

ユニバーサルリンクとApp Linksを使用するには、以下が必要です。

- Webサイトが HTTPS 経由でアクセスできること
- アプリがApp Store (iOS) または Google Play Store (Android) で入手可能であること

## ユニバーサルリンクとApp Linksの設定 {#setting-up-universal-links-and-app-links}

アプリでユニバーサルリンクまたはApp Linksをサポートするには、iOSとAndroidの両方で、リンクドメインに特別なパーミッションファイルをホストする必要があります。このファイルには、そのドメインからのリンクを開くことができるアプリの定義と、iOSの場合はそのアプリが開くことを許可されるパスの定義が含まれています。

- **iOS:** Apple App Site Association (AASA) ファイル
- **Android:** Digital Asset Links ファイル

このパーミッションファイルに加えて、アプリ内で設定される、アプリが開くことを許可されるリンクドメインのハードコードされた定義があります。

- **iOS:** Xcodeで「Associated Domains」として設定
- **Android:** アプリの`AndroidManifest.xml`ファイルで定義

この2つの部分で構成されるドメインとアプリの関連付けは、ユニバーサルリンクまたはApp Linkが機能するために必要であり、任意のアプリが特定のドメインからのリンクを乗っ取ったり、任意のドメインが特定のアプリを開いたりすることを防ぎます。

{% tabs %}
<!--iOS instructions-->
{% tab iOS %}

これらのステップは、Apple開発者ドキュメントを参考にしています。詳細については、[アプリとWebサイトのコンテンツへのリンクを許可する](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc)を参照してください。

### ステップ1:アプリのエンタイトルメントを設定する {#step-1-configure-your-app-entitlements}

{% alert note %}
[Xcode 13以降](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/)では、Xcodeがエンタイトルメントのプロビジョニングを自動的に処理できます。[ステップ1c](#step-1c)にスキップして、問題が発生した場合にこれらの手順を参照することができます。
{% endalert %}

#### ステップ1a:アプリを登録する {#step-1a}

1. developer.apple.comにアクセスしてログインします。
2. **Certificates, Identifiers & Profiles**をクリックします。
3. **Identifiers**をクリックします。
4. まだ登録済みのApp Identifierがない場合は、+をクリックして作成します。
   a. **Name**を入力します。任意の名前を入力できます。
   b. **Bundle ID**を入力します。適切なビルドターゲットのXcodeプロジェクトの**General**タブからBundle IDを確認できます。

#### ステップ1b:App IdentifierでAssociated Domainsを有効にする {#step-1b-turn-on-associated-domains-in-your-app-identifier}

1. 既存または新しく作成したApp Identifierで、**App Services**セクションを見つけます。
2. **Associated Domains**を選択します。
3. **Save**をクリックします。

![App Servicesセクション]({% image_buster /assets/img_archive/universal_links_1b.png %}){: style="max-width:75%;"}

#### ステップ1c:XcodeプロジェクトでAssociated Domainsを有効にする {#step-1c}

続行する前に、XcodeプロジェクトでApp Identifierを登録したのと同じチームが選択されていることを確認してください。

1. Xcodeで、プロジェクトファイルの**Capabilities**タブに移動します。
2. **Associated Domains**を有効にします。

##### トラブルシューティングのヒント {#troubleshooting-tip}

「An App ID with Identifier 'your-app-id' is not available. Please enter a different string」というエラーが表示された場合は、次の手順を実行してください。

1. 正しいチームが選択されていることを確認します。
2. Xcodeプロジェクトの Bundle ID（[ステップ1a](#step-1a)）が、App Identifierの登録時に使用したものと一致していることを確認します。

#### ステップ1d:ドメインエンタイトルメントを追加する {#step-1d-add-the-domain-entitlement}

domainsセクションで、適切なドメインタグを追加します。`applinks:`というプレフィックスを付ける必要があります。この例では、`applinks:yourdomain.com`を追加しています。

![Associated Domainsセクション]({% image_buster /assets/img_archive/universal_links_1d.png %})

#### ステップ1e:エンタイトルメントファイルがビルドに含まれていることを確認する {#step-1e-confirm-that-the-entitlements-file-is-included-at-build}

プロジェクトブラウザで、新しいエンタイトルメントファイルが**Target Membership**の下で選択されていることを確認します。

Xcodeはこれを自動的に処理します。

### ステップ2:AASAファイルをホストするようにWebサイトを設定する {#step-2-configure-your-website-to-host-the-aasa-file}

iOSでWebサイトのドメインをネイティブアプリに関連付けるには、WebサイトにApple App Site Association (AASA) ファイルをホストする必要があります。このファイルは、iOSに対してドメインの所有権を安全に検証する方法として機能します。iOS 9以前は、開発者は検証なしで任意のURIスキームを登録してアプリを開くことができました。しかし、AASAの導入により、このプロセスははるかに安全で信頼性の高いものになりました。

AASAファイルには、アプリのリストと、ユニバーサルリンクとして含めるまたは除外するドメイン上のURLパスを含むJSONオブジェクトが含まれています。以下はAASAファイルのサンプルです。

```json
{
  "applinks": {
    "apps": [],
    "details": [
      {
        "appID": "JHGFJHHYX.com.facebook.ios",
        "paths": [
          "*"
        ]
      }
    ]
  }
}
```

- `appID`: アプリの**Team ID**（Team IDを取得するには`https://developer.apple.com/account/#/membership/`にアクセスしてください）と**Bundle Identifier**を組み合わせて構築します。この例では、「JHGFJHHYX」がTeam ID、「com.facebook.ios」がBundle IDです。
- `paths`: 関連付けに含めるまたは除外するパスを指定する文字列の配列です。パスの前に`NOT`を使用してパスを無効にできます。この例では、このパス上のすべてのリンクはアプリを開く代わりにWebに移動します。`*`をワイルドカードとして使用してディレクトリ内のすべてのパスを有効にしたり、`?`を使用して1文字に一致させたりできます（/archives/201?/ のように2010年から2019年のすべての数字に一致させるなど）。

{% alert note %}
これらの文字列は大文字小文字を区別し、クエリ文字列とフラグメント識別子は無視されます。
{% endalert %}

### ステップ3:ドメインにAASAファイルをホストする {#step-3-host-the-aasa-file-on-your-domain}

AASAファイルの準備ができたら、`https://<<yourdomain>>/apple-app-site-association`または`https://<<yourdomain>>/.well-known/apple-app-site-association`のいずれかでドメインにホストできます。

`apple-app-site-association`ファイルをHTTPS Webサーバーにアップロードします。ファイルはサーバーのルートまたは`.well-known`サブディレクトリに配置できます。ファイル名に`.json`を追加しないでください。

{% alert important %}
iOSはセキュアな接続（HTTPS）経由でのみAASAファイルの取得を試みます。
{% endalert %}

AASAファイルをホストする際は、ファイルが以下のガイドラインに従っていることを確認してください。

- HTTPS経由で提供されている。
- `application/json` MIMEタイプを使用している。
- 128 KBを超えない（iOS 9.3.1以降の要件）

### ステップ4:ユニバーサルリンクを処理するようにアプリを準備する {#step-4-prepare-your-app-to-handle-universal-links}

ユーザーがiOSデバイスでユニバーサルリンクをタップすると、デバイスはアプリを起動し、[NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity)オブジェクトを送信します。アプリはNSUserActivityオブジェクトにクエリを実行して、起動方法を判断できます。

アプリでユニバーサルリンクをサポートするには、以下のステップを実行してください。

1. アプリがサポートするドメインを指定するエンタイトルメントを追加します。
2. NSUserActivityオブジェクトを受信したときに適切に応答するようにアプリデリゲートを更新します。

Xcodeで、**Capabilities**タブの**Associated Domains**セクションを開き、アプリがサポートする各ドメインのエントリを追加します。プレフィックスとして`applinks:`を付けます。例：`applinks:www.mywebsite.com`

{% alert note %}
Appleは、このリストを20〜30ドメイン以内に制限することを推奨しています。
{% endalert %}

### ステップ5:ユニバーサルリンクをテストする {#step-5-test-your-universal-link}

ユニバーサルリンクをメールに追加し、テストデバイスに送信します。ユニバーサルリンクをSafariのURLフィールドに直接貼り付けても、アプリは自動的に開きません。その場合は、Webサイトを手動で下にプルする必要があり、上部に該当するアプリを開くかどうかのプロンプトが表示されます。

{% endtab %}

<!--Android instructions-->
{% tab Android %}

これらのステップは、Android開発者ドキュメントを参考にしています。詳細については、[Android App Linksを追加する](https://developer.android.com/training/app-links#add-app-links)と[アプリコンテンツへのディープリンクを作成する](https://developer.android.com/training/app-links/deep-linking)を参照してください。

{% alert note %}
Android App Linksには、ドメインからのリンクを他のWeb URLとは別に処理するロジックを持つカスタム`IBrazeDeeplinkHandler`が必要です。代わりにディープリンクを使用して、メール以外のチャネルでリンクの運用を統一する方が簡単な場合があります。
{% endalert %}

### ステップ1:ディープリンクを作成する {#step-1-create-deep-links}

まず、Androidアプリのディープリンクを作成する必要があります。これは、`AndroidManifest.xml`ファイルに[インテントフィルター](https://developer.android.com/guide/components/intents-filters)を追加することで行えます。インテントフィルターには、`VIEW`アクションと`BROWSABLE`カテゴリ、およびデータ要素にWebサイトのURLを含める必要があります。

### ステップ2:アプリをWebサイトに関連付ける {#step-2-associate-your-app-with-your-website}

アプリをWebサイトに関連付ける必要があります。これは、Digital Asset Linksファイルを作成することで行えます。このファイルはJSON形式で、Webサイトへのリンクを開くことができるAndroidアプリに関する詳細が含まれます。WebサイトのWell `.well-known`ディレクトリに配置する必要があります。

### ステップ3:アプリのマニフェストファイルを更新する {#step-3-update-your-app-manifest-file}

`AndroidManifest.xml`ファイルで、application要素内にmeta-data要素を追加します。meta-data要素には、`android:name`属性として「asset_statements」と、WebサイトのURLを含む文字列配列のリソースファイルを指す`android:resource`属性を設定する必要があります。

### ステップ4:ディープリンクを処理するようにアプリを準備する {#step-4-prepare-your-app-to-handle-deep-links}

Androidアプリで、受信するディープリンクを処理する必要があります。これは、アクティビティを開始したインテントを取得し、そこからデータを抽出することで行えます。

### ステップ5:ディープリンクをテストする {#step-5-testing-your-deep-links}

最後に、ディープリンクをテストできます。メッセージングアプリまたはメール経由でリンクを自分に送信し、クリックしてください。すべてが正しく設定されていれば、アプリが開きます。

{% endtab %}
{% endtabs %}

## ユニバーサルリンク、App Links、クリックトラッキング {#universal-links-app-links-and-click-tracking}

{% alert note %}
クリックトラッキングリンクは、通常、メールのオンボーディングの一環として設定されます。顧客のオンボーディング時に設定が完了していない場合は、アカウントマネージャーにお問い合わせください。
{% endalert %}

メール送信パートナーはクリックトラッキングドメインを使用して、すべてのリンクをラップし、Brazeメールでのクリックトラッキング用のURLパラメーターを含めます。

たとえば、`https://www.example.com` のようなリンクは `https://links.email.example.com/uni/wf/click?upn=abcdef123456…` のようになります。

クリックトラッキング付きのメールリンクをユニバーサルリンクまたはApp Linksとして機能させるには、追加の設定が必要です。アプリが開くことを許可されているドメインとして、クリックトラッキングドメイン（`links.email.example.com`）を必ず追加してください。さらに、クリックトラッキングドメインはAASA（iOS）またはDigital Asset Links（Android）ファイルを配信する必要があります。これにより、クリックトラッキング付きのメールリンクがシームレスに動作します。

すべてのクリックトラッキングリンクをユニバーサルリンクまたはApp Linkにしたくない場合は、メール送信パートナーに基づいてどのリンクをユニバーサルリンクにするかを指定できます。詳細については、以下のタブを参照してください。

{% tabs %}
{% tab SendGrid %}

SendGridのクリックトラッキングリンクをユニバーサルリンクとして扱うには：

1. AASAまたはAndroidManifestのpathPrefix値を設定し、URLパスに`/uni/`を含むリンクのみをユニバーサルリンクとして扱うようにします。
2. リンクのアンカータグ（`<a>`）に属性`universal="true"`を追加します。これにより、ラップされたリンクのURLパスに`/uni/`が含まれるようになります。

{% alert note %}
AMPメールの場合、この属性は data-universal="true" にする必要があります。
{% endalert %}

例：

```html
<a href=”https://www.example.com” universal="true">
```

{:start="3"}
3. ラップされたリンクをアプリが適切に処理できるよう設定されていることを確認してください。SendGridの記事[Resolving SendGrid Click Tracking Links](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-sendgrid-click-tracking-links)を参照し、お使いのオペレーティングシステムの手順に従ってください。この記事には[iOS](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-ios)と[Android](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-android)のサンプルコードが含まれています。

この設定により、URLパスに`/uni/`を含むリンクはユニバーサルリンクとして機能し、それ以外のリンクはWebリンクとして動作します。

{% endtab %}
{% tab SparkPost %}

SparkPostのクリックトラッキングリンクをユニバーサルリンクとして扱うには、メールのドラッグ＆ドロップエディターの「属性」セクションに以下の属性を追加するか、リンクHTMLを手動で編集してリンクのアンカータグに`data-msys-sublink="custom_path"`属性を含めます。

このカスタムパスにより、その値を持つURLを選択的にユニバーサルリンクとして扱うことができます。

例：

```html
<a href=”https://www.example.com” data-msys-sublink="open-in-app">
```

次に、アプリがカスタムパスを適切に処理できるよう設定されていることを確認してください。SparkPostの記事[Using SparkPost click tracking on deep links](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#preferred-solution-using-sparkpost-click-tracking-on-deep-links)を参照してください。この記事には[iOS](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#ios-swift-forwarding-clicks-to-sparkpost)と[Android](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#forwarding-clicks-from-android-to-sparkpost)のサンプルコードが含まれています。

{% endtab %}
{% tab Amazon SES %}

カスタムパスを使用して、メールのクリックトラッキングURLにパスセグメントを追加します。これにより、モバイルオペレーティングシステムがユニバーサルリンクやApp Linksとして認識できる予測可能なURLパターンが作成されます。

ユーザーがモバイルデバイスでメールリンクをタップした際、カスタムパスにより、リンクをメインのモバイルアプリ、専用アプリ、またはモバイルブラウザー（例：商品ページ、ロイヤルティプログラム、購読解除リンク、法的ページ）のいずれで開くかを制御できます。

Amazon SESのクリックトラッキングリンクをユニバーサルリンクまたはApp Linkとして扱うには：

1. メールHTMLのアンカータグに`ses:custom-path`属性を追加するか、メールのドラッグ＆ドロップエディターの**属性**セクションで属性を追加します。カスタムパスはラップされたクリックトラッキングURLに挿入されます。

例：

```html
<!-- Opens main shopping app -->
<a href="https://yourstore.com/product" ses:custom-path="shop">Shop Now</a>
<!-- Opens loyalty app -->
<a href="https://yourstore.com/rewards" ses:custom-path="rewards">My Rewards</a>
<!-- Opens specialized app -->
<a href="https://yourstore.com/limited" ses:custom-path="limited">Limited Edition</a>
<!-- Stays in browser -->
<a href="https://yourstore.com/unsubscribe" ses:no-track>Unsubscribe</a>
```

カスタムパスが以下の要件に従っていることを確認してください：

- **形式：** 英数字、ドット、アンダースコア、ハイフンのみ
- **長さ：** 1〜32文字
- **大文字小文字の区別：** パスはモバイルOSの要件に合わせて大文字小文字が区別されます

{:start="2"}
2. ラップされたトラッキングURLにカスタムパスセグメントが含まれていることを確認します。属性がない場合、トラッキングされたリンクは`track.yourstore.com/CL0/{encodedUrl}/...`を使用します。属性がある場合は、次の形式になります：`track.yourstore.com/CL1/{customPath}/{encodedUrl}/...`

例：

- `track.yourstore.com/CL1/shop/...`
- `track.yourstore.com/CL1/rewards/...`

{:start="3"}
3. クリックトラッキングドメイン上のサイトアソシエーションファイルを設定し、パスが`/CL1/{customPath}/`に一致するようにします。

**iOS（Apple App Site Association）：**

```json
{
  "applinks": {
    "apps": [],
    "details": [{
      "appID": "TEAMID.com.yourcompany.mainapp",
      "paths": ["/CL1/shop/*", "/CL1/rewards/*"]
    }, {
      "appID": "TEAMID.com.yourcompany.limitedapp",
      "paths": ["/CL1/limited/*"]
    }]
  }
}
```

**Android（Digital Asset Links）：**

```json
[{
  "relation": ["delegate_permission/common.handle_all_urls"],
  "target": {
    "namespace": "android_app",
    "package_name": "com.yourcompany.mainapp",
    "sha256_cert_fingerprints": ["..."]
  }
}]
```

Androidでは`assetlinks.json`ではなくアプリ内でパスを照合します。アプリが処理するカスタムパスごとに、`AndroidManifest.xml`のインテントフィルターで`android:pathPrefix="/CL1/{customPath}/"`を設定してください。

アプリがこれらのラップされたリンクを処理できるよう設定されていることを確認してください。クリックトラッキングドメインをアプリのassociated domains（iOS）またはインテントフィルター（Android）に追加し、この記事で前述したように、そのドメインでAASAまたはDigital Asset Linksファイルをホストしてください。

{% endtab %}
{% endtabs %}

### リンクごとのクリックトラッキングの無効化 {#turning-off-click-tracking-on-a-link-to-link-basis}

特定のリンクのクリックトラッキングを無効にするには、HTMLエディター用のメールメッセージ、またはドラッグ＆ドロップエディター用のHTMLブロックにHTMLコードを追加します。

#### SendGrid

メールサービスプロバイダー (ESP)がSendGridの場合、次のようにHTMLコード`clicktracking=off`を使用します：

```HTML
<a clicktracking=off href="[INSERT https LINK HERE]">click here</a>
```

#### SparkPost

メールサービスプロバイダー (ESP)がSparkPostの場合、次のようにHTMLコード`data-msys-clicktrack="0"`を使用します：

```HTML
<a data-msys-clicktrack="0" href="[INSERT https LINK HERE]">click here</a>
```

#### Amazon SES

メールサービスプロバイダー (ESP)がAmazon SESの場合、次のようにHTMLコード`ses:no-track`を使用します：

```HTML
<a ses:no-track href="[INSERT https LINK HERE]">click here</a>
```

#### ドラッグ＆ドロップエディター {#drag-and-drop-editor}

ドラッグ＆ドロップメールエディターを使用する場合、リンクがテキスト、ボタン、または画像に関連付けられている場合は、HTMLコードをカスタム属性として入力します。

##### テキストリンクのカスタム属性 {#custom-attribute-for-a-text-link}

#### SendGrid

カスタム属性に以下を選択します：

- **Name：** `clicktracking`
- **Value：** `off`

#### SparkPost

カスタム属性に以下を選択します：

- **Name：** `data-msys-clicktrack`
- **Value：** `0`

![テキストリンクのカスタム属性。]({% image_buster /assets/img/text_click_tracking_off.png %}){: style="max-width:60%;"}

##### ボタンまたは画像のカスタム属性 {#custom-attribute-for-a-button-or-image}

#### SendGrid

カスタム属性に以下を選択します：

- **Name：** `clicktracking`
- **Value：** `off`
- **Type：** Link

#### SparkPost

カスタム属性に以下を選択します：

- **Name：** `data-msys-clicktrack`
- **Value：** `0`
- **Type：** Link

![ボタンのカスタム属性。]({% image_buster /assets/img/button_click_tracking_off.png %}){: style="max-width:60%;"}

### クリックトラッキング付きユニバーサルリンクのトラブルシューティング {#troubleshooting-universal-links-with-click-tracking}

ユニバーサルリンクがメールで期待どおりに動作しない場合（例：受信者がメールアプリからWebブラウザーに移動した後、最終的にアプリにリダイレクトされるなど）、以下のヒントを参考にユニバーサルリンクの設定をトラブルシューティングしてください。

#### Outlookで`[?it=`や生のURLテキストがボタンの代わりに表示される {#outlook-shows-it-or-raw-url-text-instead-of-a-button}

リンクが有効な**`http://`または`https://`**のURLスキームを使用していない場合、Outlookは`[?it=`のようなコールトゥアクションテキストを表示したり、`href`の一部を出力したりすることがあります。カスタムスキーム、スキームの欠落、または不正なURLはハイパーリンクとして扱われないため、クライアントは属性テキストを代わりに表示します。すべてのボタン、画像リンク、およびトラッキングされたURLが完全な`https://`（または`http://`）の宛先を使用していることを確認してください。これはユニバーサルリンクと標準のWebリンクの両方に適用されます。

#### リンクファイルの場所を確認する {#verify-link-file-location}

AASAファイル（iOS）またはDigital Asset Linksファイル（Android）が正しい場所にあることを確認してください：

- **iOS：** `https://click.tracking.domain/.well-known/apple-app-site-association`
- **Android：** `https://click.tracking.domain/.well-known/assetlinks.json`

これらのファイルが常に一般公開されていることを確認することが重要です。アクセスできない場合は、メール用のユニバーサルリンクの設定ステップを見落としている可能性があります。

#### ドメイン定義を確認する {#verify-domain-definitions}

アプリが開くことを許可されているドメインの定義が正しいことを確認してください。

- **iOS：** アプリのXcodeで設定されたAssociated Domainsを確認します（[ステップ1c：XcodeプロジェクトでAssociated Domainsを有効にする]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links?tab=ios#step-1c)）。クリックトラッキングドメインがそのリストに含まれていることを確認してください。
- **Android：** アプリ情報ページを開きます（アプリアイコンを長押しして ⓘ をクリック）。アプリ情報メニュー内で**デフォルトで開く**を見つけてタップします。アプリが開くことを許可されているすべての確認済みリンクが表示されるはずです。クリックトラッキングドメインがそのリストに含まれていることを確認してください。

#### すべてのメールリンクがアプリを開いてしまう {#every-email-link-opens-the-app}

ブラウザーで開くことを期待しているリンクを含め、メール内のすべてのリンクがアプリを開いてしまう場合、クリックトラッキングドメインのAASA `paths`（iOS）またはAndroidの`pathPrefix`の値がドメイン全体に一致しています（例：`*`や`/*`）。

これらのパターンをアプリで開くべきURLに限定してください。SendGridの場合は、`/uni/`に一致させ、該当するリンクにのみ`universal="true"`を追加します。[ユニバーサルリンク、App Links、クリックトラッキング](#universal-links-app-links-and-click-tracking)を参照してください。

#### トラッキングドメインが.well-knownファイルを配信できない {#tracking-domain-cant-serve-well-known-files}

ESPの制限やインフラの制約により、クリックトラッキングドメインが必要な`.well-known`ファイルをホストできない場合があります。トラッキングドメインでAASAまたはDigital Asset Linksファイルをホストできない場合は、以下のオプションを検討してください：

- **ディープリンクURLのクリックトラッキングを選択的に無効にする：** 特定のユニバーサルリンクのクリックトラッキングを無効にして、メインドメイン（AASAまたはDigital Asset Linksファイルをホストできる場所）に直接リンクするようにできます。ただし、この方法では該当リンクのクリック分析データが失われる可能性があることに注意してください。手順については[リンクごとのクリックトラッキングの無効化](#turning-off-click-tracking-on-a-link-to-link-basis)を参照してください。
- **トラッキングサブドメインの前にCDNを配置する：** フルのクリックトラッキングとディープリンクの両方が必要な場合は、トラッキングサブドメインの前にCDN（CloudflareやCloudFrontなど）を配置できます。CDNを設定して`.well-known`ファイルをローカルで配信し、その他のすべてのトラフィックをESPにプロキシします。このアプローチはより複雑ですが、クリックトラッキングとユニバーサルリンクの両方を完全に制御できます。

#### あるワークスペースでは動作するが別のワークスペースでは動作しない {#links-working-in-one-workspace-but-not-another}

ユニバーサルリンクまたはApp Linksが本番ワークスペースでは正常に動作するが、開発またはテストワークスペースでは失敗する場合は、送信メールアドレスのドメインが各ワークスペースのメール設定で構成されているトラッキングドメインと一致していることを確認してください。ワークスペース間で設定が一致していないと、同じメールテンプレートとAASAまたはDigital Asset Linksファイルを使用していても、リンクの動作が異なる場合があります。

メール設定を確認するには：

1. Brazeダッシュボードで**設定** > **メール設定**に移動します。
2. **送信設定**の下にある**送信メール設定**を確認します。
3. リンクが動作していないワークスペースで、送信ドメインとトラッキングドメインが適切に整合していることを確認します。

送信ドメインがワークスペース間で異なる場合は、各ワークスペースに適切なDNSレコードが設定されていること、および各トラッキングドメインからAASA（iOS）またはDigital Asset Links（Android）ファイルにアクセスできることを確認してください。