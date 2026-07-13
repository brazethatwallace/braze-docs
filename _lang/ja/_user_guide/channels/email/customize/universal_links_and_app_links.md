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

ユニバーサルリンクまたはApp Linkが開かれると、オペレーティングシステムはそのドメインに登録されたインストール済みアプリがあるかどうかを確認します。アプリが見つかった場合、Webページを読み込むことなく即座にアプリが起動されます。アプリが見つからない場合、Web URLがユーザーのデフォルトWebブラウザーで読み込まれ、それぞれApp StoreまたはGoogle Play Storeにリダイレクトするように設定することもできます。

簡単に言えば、ユニバーサルリンクにより、WebサイトはそのWebページを特定のアプリ画面に関連付けることができます。そのため、ユーザーがアプリ画面に対応するWebページへのリンクをクリックすると、アプリを直接開くことができます（アプリが現在インストールされている場合）。

{% alert important %}
Firebase Dynamic Linksは非推奨になりました。BrazeはFirebaseとの直接的な統合を持っておらず、ディープリンクはBrazeプラットフォームの外部で管理されます。プラットフォームネイティブのソリューション（この記事で説明するAppleユニバーサルリンクとAndroid App Links）または代替のディープリンクサービスプロバイダーに移行してください。移行のガイダンスについては、[Firebaseの移行FAQ](https://firebase.google.com/support/dynamic-links-faq)を参照してください。
{% endalert %}

次の表は、ユニバーサルリンクと従来のディープリンクの主な違いをまとめたものです。

|                        | ユニバーサルリンクとApp Links                                  | ディープリンク                   |
| ---------------------- | -------------------------------------------------------------- | ---------------------------- |
| プラットフォーム互換性 | iOS（バージョン9以降）およびAndroid（バージョン6.0以降）  | さまざまなモバイルOSで使用    |
| 目的                | iOSおよびAndroidデバイスでWebとアプリのコンテンツをシームレスにリンク | 特定のアプリコンテンツにリンク |
| 機能               | コンテキストに基づいてWebページまたはアプリコンテンツに誘導           | 特定のアプリ画面を開く   |
| アプリのインストール       | アプリがインストールされている場合はアプリを開き、それ以外の場合はWebコンテンツを開く | アプリのインストールが必要 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ユニバーサルリンクとApp Linksの仕組み" }

## ユースケース {#use-cases}

ユニバーサルリンクとApp Linksは、メールキャンペーンで最も一般的に使用されます。メールはデスクトップとモバイルデバイスの両方から開いてクリックできるためです。

一部のチャネルはこれらのリンクとうまく連携しません。たとえば、プッシュ通知、アプリ内メッセージ、Content Cardsでは、スキームベースのディープリンク（`mydomain://`）を使用する必要があります。

{% alert note %}
Android App Linksには、そのドメインからのリンクを他のWeb URLとは別に処理するロジックを持つカスタム`IBrazeDeeplinkHandler`が必要です。代わりにディープリンクを使用し、メール以外のチャネルではリンクの方法を統一する方が簡単な場合があります。
{% endalert %}

## 前提条件 {#prerequisites}

ユニバーサルリンクとApp Linksを使用するには、以下が必要です。

- WebサイトがHTTPS経由でアクセス可能であること
- アプリがApp Store（iOS）またはGoogle Play Store（Android）で利用可能であること

## ユニバーサルリンクとApp Linksの設定 {#setting-up-universal-links-and-app-links}

アプリがユニバーサルリンクまたはApp Linksをサポートするには、iOSとAndroidの両方で、リンクドメインに特別な権限ファイルをホストする必要があります。このファイルには、そのドメインからのリンクを開くことができるアプリの定義と、iOSの場合はそれらのアプリが開くことを許可されるパスが含まれています。

- **iOS:** Apple App Site Association（AASA）ファイル
- **Android:** Digital Asset Linksファイル

この権限ファイルに加えて、アプリが開くことを許可されるリンクドメインのハードコードされた定義がアプリ内に設定されます。

- **iOS:** Xcodeで「Associated Domains」として設定
- **Android:** アプリの`AndroidManifest.xml`ファイルで定義

この2つのパートからなるドメインとアプリの関連付けは、ユニバーサルリンクまたはApp Linkが機能するために必要であり、任意のアプリが特定のドメインからのリンクを乗っ取ったり、任意のドメインが特定のアプリを開いたりすることを防ぎます。

{% tabs %}
<!--iOS instructions-->
{% tab iOS %}

これらの手順はApple開発者ドキュメントから適応されたものです。詳細については、[Allowing apps and websites to link to your content](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc)を参照してください。

### ステップ1:アプリのエンタイトルメントを設定する {#step-1-configure-your-app-entitlements}

{% alert note %}
[Xcode 13以降](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/)では、Xcodeがエンタイトルメントのプロビジョニングを自動的に処理できます。[ステップ&nbsp;1c](#step-1c)に進み、問題が発生した場合にこれらの手順を参照してください。
{% endalert %}

#### ステップ1a:アプリを登録する {#step-1a}

1. developer.apple.comにアクセスしてログインします。
2. **Certificates, Identifiers & Profiles**をクリックします。
3. **Identifiers**をクリックします。
4. 登録済みのApp Identifierがまだない場合は、+をクリックして作成します。
   a. **Name**を入力します。任意の名前を設定できます。
   b. **Bundle ID**を入力します。Bundle IDは、適切なビルドターゲットのXcodeプロジェクトの**General**タブから確認できます。

#### ステップ1b:App IdentifierでAssociated Domainsを有効にする {#step-1b-turn-on-associated-domains-in-your-app-identifier}

1. 既存または新しく作成したApp Identifierで、**App Services**セクションを見つけます。
2. **Associated Domains**を選択します。
3. **Save**をクリックします。

![App Servicesセクション]({% image_buster /assets/img_archive/universal_links_1b.png %}){: style="max-width:75%;"}

#### ステップ1c:XcodeプロジェクトでAssociated Domainsを有効にする {#step-1c}

続行する前に、XcodeプロジェクトでApp Identifierを登録した場所と同じチームが選択されていることを確認してください。

1. Xcodeで、プロジェクトファイルの**Capabilities**タブに移動します。
2. **Associated Domains**を有効にします。

##### トラブルシューティングのヒント {#troubleshooting-tip}

「An App ID with Identifier 'your-app-id' is not available. Please enter a different string」というエラーが表示された場合は、以下を行ってください。

1. 正しいチームが選択されていることを確認します。
2. Xcodeプロジェクトの Bundle ID（[ステップ1a](#step-1a)）が、App Identifierの登録に使用したものと一致していることを確認します。

#### ステップ1d:ドメインエンタイトルメントを追加する {#step-1d-add-the-domain-entitlement}

ドメインセクションで、適切なドメインタグを追加します。`applinks:`をプレフィックスとして付ける必要があります。この例では、`applinks:yourdomain.com`を追加しています。

![Associated Domainsセクション]({% image_buster /assets/img_archive/universal_links_1d.png %})

#### ステップ1e:エンタイトルメントファイルがビルドに含まれていることを確認する {#step-1e-confirm-that-the-entitlements-file-is-included-at-build}

プロジェクトブラウザーで、新しいエンタイトルメントファイルが**Target Membership**で選択されていることを確認します。

Xcodeはこれを自動的に処理します。

### ステップ2:AASAファイルをホストするようにWebサイトを設定する {#step-2-configure-your-website-to-host-the-aasa-file}

WebサイトのドメインをiOSのネイティブアプリに関連付けるには、WebサイトにApple App Site Association（AASA）ファイルをホストする必要があります。このファイルは、iOSに対してドメインの所有権を安全に検証する方法として機能します。iOS 9より前は、開発者は検証なしで任意のURIスキームを登録してアプリを開くことができました。しかし、AASAにより、このプロセスはより安全で信頼性の高いものになりました。

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

- `appID`: アプリの**Team ID**（`https://developer.apple.com/account/#/membership/`にアクセスしてTeam IDを取得）と**Bundle Identifier**を組み合わせて構築されます。上記の例では、「JHGFJHHYX」がTeam IDで、「com.facebook.ios」がBundle IDです。
- `paths`: 関連付けに含めるまたは除外するパスを指定する文字列の配列です。パスの前に`NOT`を使用してパスを無効にできます。この例では、このパス上のすべてのリンクはアプリを開く代わりにWebに移動します。`*`をワイルドカードとして使用してディレクトリ内のすべてのパスを有効にしたり、`?`を使用して単一の文字に一致させたりできます（例：/archives/201?/ で2010〜2019のすべての数字に一致）。

{% alert note %}
これらの文字列は大文字と小文字が区別され、クエリ文字列とフラグメント識別子は無視されます。
{% endalert %}

### ステップ3:ドメインにAASAファイルをホストする {#step-3-host-the-aasa-file-on-your-domain}

AASAファイルの準備ができたら、`https://<<yourdomain>>/apple-app-site-association`または`https://<<yourdomain>>/.well-known/apple-app-site-association`のいずれかでドメインにホストできます。

`apple-app-site-association`ファイルをHTTPS Webサーバーにアップロードします。ファイルはサーバーのルートまたは`.well-known`サブディレクトリに配置できます。ファイル名に`.json`を追加しないでください。

{% alert important %}
iOSはHTTPSによる安全な接続経由でのみAASAファイルの取得を試みます。
{% endalert %}

AASAファイルをホストする際は、ファイルが以下のガイドラインに従っていることを確認してください。

- HTTPS経由で提供されていること。
- `application/json` MIMEタイプを使用していること。
- 128 KBを超えないこと（iOS 9.3.1以降の要件）

### ステップ4:ユニバーサルリンクを処理するようにアプリを準備する {#step-4-prepare-your-app-to-handle-universal-links}

ユーザーがiOSデバイスでユニバーサルリンクをタップすると、デバイスはアプリを起動し、[NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity)オブジェクトを送信します。アプリはNSUserActivityオブジェクトをクエリして、どのように起動されたかを判断できます。

アプリでユニバーサルリンクをサポートするには、以下のステップを実行します。

1. アプリがサポートするドメインを指定するエンタイトルメントを追加します。
2. NSUserActivityオブジェクトを受信したときに適切に応答するようにアプリデリゲートを更新します。

Xcodeで、**Capabilities**タブの**Associated Domains**セクションを開き、アプリがサポートする各ドメインのエントリを`applinks:`をプレフィックスとして追加します。例：`applinks:www.mywebsite.com`。

{% alert note %}
Appleはこのリストを20〜30ドメイン以内に制限することを推奨しています。
{% endalert %}

### ステップ5:ユニバーサルリンクをテストする {#step-5-test-your-universal-link}

ユニバーサルリンクをメールに追加し、テストデバイスに送信します。SafariのURLフィールドにユニバーサルリンクを直接貼り付けても、アプリは自動的に開きません。その場合は、Webサイトを手動で下にプルして、該当するアプリを開くかどうかを尋ねるプロンプトが上部に表示されるようにする必要があります。

{% endtab %}

<!--Android instructions-->
{% tab Android %}

これらの手順はAndroid開発者ドキュメントから適応されたものです。詳細については、[Add Android App Links](https://developer.android.com/training/app-links#add-app-links)および[Create Deep Links to App Content](https://developer.android.com/training/app-links/deep-linking)を参照してください。

{% alert note %}
Android App Linksには、そのドメインからのリンクを他のWeb URLとは別に処理するロジックを持つカスタム`IBrazeDeeplinkHandler`が必要です。代わりにディープリンクを使用し、メール以外のチャネルではリンクの方法を統一する方が簡単な場合があります。
{% endalert %}

### ステップ1:ディープリンクを作成する {#step-1-create-deep-links}

まず、Androidアプリのディープリンクを作成する必要があります。これは、`AndroidManifest.xml`ファイルに[インテントフィルター](https://developer.android.com/guide/components/intents-filters)を追加することで行えます。インテントフィルターには、`VIEW`アクションと`BROWSABLE`カテゴリ、およびデータ要素にWebサイトのURLを含める必要があります。

### ステップ2:アプリをWebサイトに関連付ける {#step-2-associate-your-app-with-your-website}

アプリをWebサイトに関連付ける必要があります。これは、Digital Asset Linksファイルを作成することで行えます。このファイルはJSON形式で、Webサイトへのリンクを開くことができるAndroidアプリの詳細が含まれています。Webサイトの`.well-known`ディレクトリに配置する必要があります。

### ステップ3:アプリのマニフェストファイルを更新する {#step-3-update-your-app-manifest-file}

`AndroidManifest.xml`ファイルで、application要素内にmeta-data要素を追加します。meta-data要素には、`android:name`属性に「asset_statements」を、`android:resource`属性にWebサイトのURLを含む文字列配列を持つリソースファイルを指定する必要があります。

### ステップ4:ディープリンクを処理するようにアプリを準備する {#step-4-prepare-your-app-to-handle-deep-links}

Androidアプリで、受信するディープリンクを処理する必要があります。これは、アクティビティを開始したインテントを取得し、そこからデータを抽出することで行えます。

### ステップ5:ディープリンクをテストする {#step-5-testing-your-deep-links}

最後に、ディープリンクをテストできます。メッセージングアプリまたはメールを通じて自分にリンクを送信し、クリックします。すべてが正しく設定されていれば、アプリが開くはずです。

{% endtab %}
{% endtabs %}

## ユニバーサルリンク、App Links、およびクリックトラッキング {#universal-links-app-links-and-click-tracking}

{% alert note %}
クリックトラッキングリンクは通常、メールのオンボーディングの一環として設定されます。顧客のオンボーディング中に完了しなかった場合は、アカウントマネージャーにお問い合わせください。
{% endalert %}

メール送信パートナーは、クリックトラッキングドメインを使用してすべてのリンクをラップし、BrazeメールのクリックトラッキングのURLパラメーターを含めます。

たとえば、`https://www.example.com`のようなリンクは`https://links.email.example.com/uni/wf/click?upn=abcdef123456…`のようになります。

クリックトラッキング付きのメールリンクをユニバーサルリンクまたはApp Linksとして機能させるには、追加の設定が必要です。クリックトラッキングドメイン（`links.email.example.com`）を、アプリが開くことを許可されるドメインとして追加してください。さらに、クリックトラッキングドメインはAASA（iOS）またはDigital Asset Links（Android）ファイルを提供する必要があります。これにより、クリックトラッキング付きのメールリンクがシームレスに機能するようになります。

すべてのクリックトラッキングリンクをユニバーサルリンクまたはApp Linkにしたくない場合は、メール送信パートナーに基づいてどのリンクをユニバーサルリンクにするかを指定できます。詳細については、以下のタブを参照してください。

{% tabs %}
{% tab SendGrid %}

SendGridのクリックトラッキングリンクをユニバーサルリンクとして扱うには、以下を行います。

1. AASAまたはAndroidManifestのpathPrefix値を設定して、URLパスに`/uni/`を含むリンクのみをユニバーサルリンクとして扱うようにします。
2. リンクのアンカータグ（`<a>`）に属性`universal="true"`を追加します。これにより、ラップされたリンクのURLパスに`/uni/`が含まれるようになります。

{% alert note %}
AMPメールの場合、この属性はdata-universal="true"にする必要があります。
{% endalert %}

例：

```html
<a href=”https://www.example.com” universal="true">
```

{:start="3"}
3. アプリがラップされたリンクを適切に処理するように設定されていることを確認します。SendGridの記事[Resolving SendGrid Click Tracking Links](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-sendgrid-click-tracking-links)を参照し、お使いのオペレーティングシステムの手順に従ってください。この記事には[iOS](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-ios)と[Android](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-android)のサンプルコードが含まれています。

この設定により、URLパスに`/uni/`を含むリンクはユニバーサルリンクとして機能し、その他のすべてのリンクはWebリンクとして機能します。

{% endtab %}
{% tab SparkPost %}

SparkPostのクリックトラッキングリンクをユニバーサルリンクとして扱うには、メールのドラッグ＆ドロップエディターの属性セクションに以下の属性を追加するか、リンクのHTMLを手動で編集してリンクのアンカータグに以下の属性を含めます：`data-msys-sublink="custom_path"`。

このカスタムパスにより、その値を持つURLを選択的にユニバーサルリンクとして扱うことができます。

例：

```html
<a href=”https://www.example.com” data-msys-sublink="open-in-app">
```

次に、アプリがカスタムパスを適切に処理するように設定されていることを確認します。SparkPostの記事[Using SparkPost click tracking on deep links](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#preferred-solution-using-sparkpost-click-tracking-on-deep-links)を参照してください。この記事には[iOS](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#ios-swift-forwarding-clicks-to-sparkpost)と[Android](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#forwarding-clicks-from-android-to-sparkpost)のサンプルコードが含まれています。

{% endtab %}
{% tab Amazon SES %}

カスタムパスを使用して、メールのクリックトラッキングURLにパスセグメントを追加します。これにより、モバイルオペレーティングシステムがユニバーサルリンクやApp Linksとして認識できる予測可能なURLパターンが作成されます。

ユーザーがモバイルデバイスでメールリンクをタップした際、カスタムパスを使用することで、リンクをメインのモバイルアプリ、専用アプリ、またはモバイルブラウザー（たとえば商品ページ、ロイヤルティプログラム、購読解除リンク、法的ページなど）のいずれで開くかを制御できます。

Amazon SESのクリックトラッキングリンクをユニバーサルリンクまたはApp Linkとして扱うには、以下を行います。

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

カスタムパスが以下の要件に従っていることを確認してください。

- **形式:** 英数字、ドット、アンダースコア、ハイフンのみ
- **長さ:** 1〜32文字
- **大文字と小文字の区別:** パスはモバイルOSの要件に合わせて大文字と小文字が区別されます

{:start="2"}
2. ラップされたトラッキングURLにカスタムパスセグメントが含まれていることを確認します。リンクは次の形式に従います：`track.yourstore.com/L1/{customPath}/...`

例：

- `track.yourstore.com/L1/shop/...`
- `track.yourstore.com/L1/rewards/...`

{:start="3"}
3. クリックトラッキングドメインのサイトアソシエーションファイルを設定して、パスが`/L1/{customPath}/`に一致するようにします。

**iOS（Apple App Site Association）：**

```json
{
  "applinks": {
    "apps": [],
    "details": [{
      "appID": "TEAMID.com.yourcompany.mainapp",
      "paths": ["/L1/shop/*", "/L1/rewards/*"]
    }, {
      "appID": "TEAMID.com.yourcompany.limitedapp",
      "paths": ["/L1/limited/*"]
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
  },
  "include": ["/L1/shop/*", "/L1/rewards/*"]
}]
```

アプリがこれらのラップされたリンクを処理するように設定されていることを確認してください。クリックトラッキングドメインをアプリのAssociated Domains（iOS）またはインテントフィルター（Android）に追加し、この記事で前述したとおりにAASAまたはDigital Asset Linksファイルをそのドメインにホストしてください。

{% endtab %}
{% endtabs %}

### リンクごとのクリックトラッキングの無効化 {#turning-off-click-tracking-on-a-link-to-link-basis}

特定のリンクのクリックトラッキングを無効にするには、HTMLエディターのメールメッセージにHTMLコードを追加するか、ドラッグ＆ドロップエディターのHTMLブロックに追加します。

#### SendGrid

メールサービスプロバイダー（ESP）がSendGridの場合、次のようにHTMLコード`clicktracking=off`を使用します。

```HTML
<a clicktracking=off href="[INSERT https LINK HERE]">click here</a>
```

#### SparkPost

メールサービスプロバイダー（ESP）がSparkPostの場合、次のようにHTMLコード`data-msys-clicktrack="0"`を使用します。

```HTML
<a data-msys-clicktrack="0" href="[INSERT https LINK HERE]">click here</a>
```

#### Amazon SES

メールサービスプロバイダー（ESP）がAmazon SESの場合、次のようにHTMLコード`ses:no-track`を使用します。

```HTML
<a ses:no-track href="[INSERT https LINK HERE]">click here</a>
```

#### ドラッグ＆ドロップエディター {#drag-and-drop-editor}

ドラッグ＆ドロップメールエディターを使用する場合、リンクがテキスト、ボタン、または画像に添付されている場合は、HTMLコードをカスタム属性として入力します。

##### テキストリンクのカスタム属性 {#custom-attribute-for-a-text-link}

#### SendGrid

カスタム属性に以下を選択します。

- **Name:** `clicktracking`
- **Value:** `off`

#### SparkPost

カスタム属性に以下を選択します。

- **Name:** `data-msys-clicktrack`
- **Value:** `0`

![テキストリンクのカスタム属性]({% image_buster /assets/img/text_click_tracking_off.png %}){: style="max-width:60%;"}

##### ボタンまたは画像のカスタム属性 {#custom-attribute-for-a-button-or-image}

#### SendGrid

カスタム属性に以下を選択します。

- **Name:** `clicktracking`
- **Value:** `off`
- **Type:** Link

#### SparkPost

カスタム属性に以下を選択します。

- **Name:** `data-msys-clicktrack`
- **Value:** `0`
- **Type:** Link

![ボタンのカスタム属性]({% image_buster /assets/img/button_click_tracking_off.png %}){: style="max-width:60%;"}

### クリックトラッキング付きユニバーサルリンクのトラブルシューティング {#troubleshooting-universal-links-with-click-tracking}

メール内のユニバーサルリンクが期待どおりに機能しない場合（受信者がメールアプリからWebブラウザーに移動し、最終的にアプリにリダイレクトされるなど）、以下のヒントを参照してユニバーサルリンクの設定をトラブルシューティングしてください。

#### Outlookでボタンの代わりに`[?it=`や生のURLテキストが表示される {#outlook-shows-it-or-raw-url-text-instead-of-a-button}

Outlookでは、リンクが有効な**`http://`または`https://`** URLスキームを使用していない場合、コールトゥアクションテキストとして`[?it=`が表示されたり、`href`の一部が印刷されたりすることがあります。カスタムスキーム、スキームの欠落、または不正なURLはハイパーリンクとして扱われないため、クライアントは属性テキストを代わりに表示します。すべてのボタン、画像リンク、およびトラッキングURLが完全な`https://`（または`http://`）の送信先を使用していることを確認してください。これはユニバーサルリンクと標準的なWebリンクの両方に適用されます。

#### リンクファイルの場所を確認する {#verify-link-file-location}

AASAファイル（iOS）またはDigital Asset Linksファイル（Android）が正しい場所にあることを確認します。

- **iOS:** `https://click.tracking.domain/.well-known/apple-app-site-association`
- **Android:** `https://click.tracking.domain/.well-known/assetlinks.json`

これらのファイルが常に公開アクセス可能であることを確認することが重要です。アクセスできない場合は、メール用のユニバーサルリンクの設定手順を見落としている可能性があります。

#### ドメイン定義を確認する {#verify-domain-definitions}

アプリが開くことを許可されるドメインの定義が正しいことを確認します。

- **iOS:** XcodeでアプリのAssociated Domainsを確認します（[ステップ1c:XcodeプロジェクトでAssociated Domainsを有効にする]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links?tab=ios#step-1c)）。クリックトラッキングドメインがそのリストに含まれていることを確認します。
- **Android:** アプリ情報ページを開きます（アプリアイコンを長押しして ⓘ をクリック）。アプリ情報メニュー内で**Open by default**を見つけてタップします。アプリが開くことを許可されているすべての検証済みリンクが表示される画面が表示されます。クリックトラッキングドメインがそのリストに含まれていることを確認します。

#### トラッキングドメインが.well-knownファイルを提供できない場合 {#tracking-domain-cant-serve-well-known-files}

場合によっては、ESPの制限やインフラの制約により、クリックトラッキングドメインが必要な`.well-known`ファイルをホストできないことがあります。トラッキングドメインにAASAまたはDigital Asset Linksファイルをホストできない場合は、以下のオプションを検討してください。

- **ディープリンクURLのクリックトラッキングを選択的に無効にする:** 特定のユニバーサルリンクのクリックトラッキングを無効にして、メインドメイン（AASAまたはDigital Asset Linksファイルをホストできる場所）に直接移動するようにできます。この方法では、それらの特定のリンクのクリック分析が失われる可能性があることに注意してください。手順については、[リンクごとのクリックトラッキングの無効化](#turning-off-click-tracking-on-a-link-to-link-basis)を参照してください。
- **トラッキングサブドメインの前にCDNを配置する:** 完全なクリックトラッキングカバレッジとディープリンクの両方が必要な場合は、トラッキングサブドメインの前にCDN（CloudflareやCloudFrontなど）を配置できます。CDNを設定して`.well-known`ファイルをローカルで提供し、その他のすべてのトラフィックをESPにプロキシします。このアプローチはより複雑ですが、クリックトラッキングとユニバーサルリンクの両方を完全に制御できます。