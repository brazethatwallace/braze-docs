---
nav_title: "ユニバーサルリンクとApp Links"
article_title: "ユニバーサルリンクとApp Links"
page_order: 6.4
page_type: reference
description: "この記事では、Apple ユニバーサルリンクと Android App Links の設定方法について説明します。"
channel: email
---

# ユニバーサルリンクとApp Links

> この記事では、Apple ユニバーサルリンクと Android App Links の設定方法について説明します。

{% alert tip %}
すべてのメッセージングチャネルにおけるリンクタイプの比較と、AASA ファイルが必要なタイミングに関するガイダンスについては、[iOS ディープリンクガイド]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide/)を参照してください。
{% endalert %}

Apple ユニバーサルリンクと Android App Links は、Web コンテンツとモバイルアプリ間のシームレスな遷移を提供するために考案されたメカニズムです。ユニバーサルリンクは iOS 固有のものですが、Android App Links は Android アプリケーションで同じ目的を果たします。

## ユニバーサルリンクと App Links の仕組み

ユニバーサルリンク（iOS）と App Links（Android）は、Web ページとアプリ内のコンテンツの両方を指す標準的な Web リンク（`http://mydomain.com`）です。

ユニバーサルリンクまたは App Link が開かれると、オペレーティングシステムはそのドメインに登録されたインストール済みアプリがあるかどうかを確認します。アプリが見つかった場合、Web ページを読み込むことなく即座にアプリが起動されます。アプリが見つからない場合、Web URL がユーザーのデフォルト Web ブラウザーで読み込まれ、それぞれ App Store または Google Play Store にリダイレクトするように設定することもできます。

簡単に言えば、ユニバーサルリンクにより、Web サイトはその Web ページを特定のアプリ画面に関連付けることができます。そのため、ユーザーがアプリ画面に対応する Web ページへのリンクをクリックすると、アプリを直接開くことができます（アプリが現在インストールされている場合）。

次の表は、ユニバーサルリンクと従来のディープリンクの主な違いをまとめたものです。

|                        | ユニバーサルリンクと App Links                                  | ディープリンク                   |
| ---------------------- | -------------------------------------------------------------- | ---------------------------- |
| プラットフォーム互換性 | iOS（バージョン 9 以降）および Android（バージョン 6.0 以降）  | さまざまなモバイル OS で使用    |
| 目的                | iOS および Android デバイスで Web とアプリのコンテンツをシームレスにリンク | 特定のアプリコンテンツにリンク |
| 機能               | コンテキストに基づいて Web ページまたはアプリコンテンツに誘導           | 特定のアプリ画面を開く   |
| アプリのインストール       | アプリがインストールされている場合はアプリを開き、それ以外の場合は Web コンテンツを開く | アプリのインストールが必要 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## ユースケース

ユニバーサルリンクと App Links は、メール Campaign で最も一般的に使用されます。メールはデスクトップとモバイルデバイスの両方から開いてクリックできるためです。

一部のチャネルはこれらのリンクとうまく連携しません。たとえば、プッシュ通知、アプリ内メッセージ、Content Cards では、スキームベースのディープリンク（`mydomain://`）を使用する必要があります。

{% alert note %}
Android App Links には、そのドメインからのリンクを他の Web URL とは別に処理するロジックを持つカスタム `IBrazeDeeplinkHandler` が必要です。代わりにディープリンクを使用し、メール以外のチャネルではリンクの方法を統一する方が簡単な場合があります。
{% endalert %}

## 前提条件

ユニバーサルリンクと App Links を使用するには、以下が必要です。

- Web サイトが HTTPS 経由でアクセス可能であること
- アプリが App Store（iOS）または Google Play Store（Android）で利用可能であること

## ユニバーサルリンクと App Links の設定

アプリがユニバーサルリンクまたは App Links をサポートするには、iOS と Android の両方で、リンクドメインに特別な権限ファイルをホストする必要があります。このファイルには、そのドメインからのリンクを開くことができるアプリの定義と、iOS の場合はそれらのアプリが開くことを許可されるパスが含まれています。

- **iOS:** Apple App Site Association（AASA）ファイル
- **Android:** Digital Asset Links ファイル

この権限ファイルに加えて、アプリが開くことを許可されるリンクドメインのハードコードされた定義がアプリ内に設定されます。

- **iOS:** Xcode で「Associated Domains」として設定
- **Android:** アプリの `AndroidManifest.xml` ファイルで定義

この2つのパートからなるドメインとアプリの関連付けは、ユニバーサルリンクまたは App Link が機能するために必要であり、任意のアプリが特定のドメインからのリンクを乗っ取ったり、任意のドメインが特定のアプリを開いたりすることを防ぎます。

{% tabs %}
<!--iOS instructions-->
{% tab iOS %}

これらの手順は Apple 開発者ドキュメントから適応されたものです。詳細については、[Allowing apps and websites to link to your content](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc) を参照してください。

### ステップ 1:アプリのエンタイトルメントを設定する

{% alert note %}
[Xcode 13 以降](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/)では、Xcode がエンタイトルメントのプロビジョニングを自動的に処理できます。[ステップ 1c](#step-1c) に進み、問題が発生した場合にこれらの手順を参照してください。
{% endalert %}

#### ステップ 1a:アプリを登録する {#step-1a}

1. developer.apple.com にアクセスしてログインします。
2. **Certificates, Identifiers & Profiles** をクリックします。
3. **Identifiers** をクリックします。
4. 登録済みの App Identifier がまだない場合は、+ をクリックして作成します。
   a. **Name** を入力します。任意の名前を設定できます。
   b. **Bundle ID** を入力します。Bundle ID は、適切なビルドターゲットの Xcode プロジェクトの **General** タブから確認できます。

#### ステップ 1b:App Identifier で Associated Domains を有効にする

1. 既存または新しく作成した App Identifier で、**App Services** セクションを見つけます。
2. **Associated Domains** を選択します。
3. **Save** をクリックします。

![]({% image_buster /assets/img_archive/universal_links_1b.png %}){: style="max-width:75%;"}

#### ステップ 1c:Xcode プロジェクトで Associated Domains を有効にする {#step-1c}

続行する前に、Xcode プロジェクトで App Identifier を登録した場所と同じチームが選択されていることを確認してください。

1. Xcode で、プロジェクトファイルの **Capabilities** タブに移動します。
2. **Associated Domains** を有効にします。

##### トラブルシューティングのヒント

「An App ID with Identifier 'your-app-id' is not available. Please enter a different string」というエラーが表示された場合は、以下を行ってください。

1. 正しいチームが選択されていることを確認します。
2. Xcode プロジェクトの Bundle ID（[ステップ 1a](#step-1a)）が、App Identifier の登録に使用したものと一致していることを確認します。

#### ステップ 1d:ドメインエンタイトルメントを追加する

ドメインセクションで、適切なドメインタグを追加します。`applinks:` をプレフィックスとして付ける必要があります。この例では、`applinks:yourdomain.com` を追加しています。

![]({% image_buster /assets/img_archive/universal_links_1d.png %})

#### ステップ 1e:エンタイトルメントファイルがビルドに含まれていることを確認する

プロジェクトブラウザーで、新しいエンタイトルメントファイルが **Target Membership** で選択されていることを確認します。

Xcode はこれを自動的に処理します。

### ステップ 2:AASA ファイルをホストするように Web サイトを設定する

Web サイトのドメインを iOS のネイティブアプリに関連付けるには、Web サイトに Apple App Site Association（AASA）ファイルをホストする必要があります。このファイルは、iOS に対してドメインの所有権を安全に検証する方法として機能します。iOS 9 より前は、開発者は検証なしで任意の URI スキームを登録してアプリを開くことができました。しかし、AASA により、このプロセスはより安全で信頼性の高いものになりました。

AASA ファイルには、アプリのリストと、ユニバーサルリンクとして含めるまたは除外するドメイン上の URL パスを含む JSON オブジェクトが含まれています。以下は AASA ファイルのサンプルです。

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

- `appID`: アプリの **Team ID**（`https://developer.apple.com/account/#/membership/` にアクセスして Team ID を取得）と **Bundle Identifier** を組み合わせて構築されます。上記の例では、「JHGFJHHYX」が Team ID で、「com.facebook.ios」が Bundle ID です。
- `paths`: 関連付けに含めるまたは除外するパスを指定する文字列の配列です。パスの前に `NOT` を使用してパスを無効にできます。この例では、このパス上のすべてのリンクはアプリを開く代わりに Web に移動します。`*` をワイルドカードとして使用してディレクトリ内のすべてのパスを有効にしたり、`?` を使用して単一の文字に一致させたりできます（例：/archives/201?/ で 2010〜2019 のすべての数字に一致）。

{% alert note %}
これらの文字列は大文字と小文字が区別され、クエリ文字列とフラグメント識別子は無視されます。
{% endalert %}

### ステップ 3:ドメインに AASA ファイルをホストする

AASA ファイルの準備ができたら、`https://<<yourdomain>>/apple-app-site-association` または `https://<<yourdomain>>/.well-known/apple-app-site-association` のいずれかでドメインにホストできます。

`apple-app-site-association` ファイルを HTTPS Web サーバーにアップロードします。ファイルはサーバーのルートまたは `.well-known` サブディレクトリに配置できます。ファイル名に `.json` を追加しないでください。

{% alert important %}
iOS は HTTPS による安全な接続経由でのみ AASA ファイルの取得を試みます。
{% endalert %}

AASA ファイルをホストする際は、ファイルが以下のガイドラインに従っていることを確認してください。

- HTTPS 経由で提供されていること。
- `application/json` MIME タイプを使用していること。
- 128 KB を超えないこと（iOS 9.3.1 以降の要件）

### ステップ 4:ユニバーサルリンクを処理するようにアプリを準備する

ユーザーが iOS デバイスでユニバーサルリンクをタップすると、デバイスはアプリを起動し、[NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity) オブジェクトを送信します。アプリは NSUserActivity オブジェクトをクエリして、どのように起動されたかを判断できます。

アプリでユニバーサルリンクをサポートするには、以下の手順を実行します。

1. アプリがサポートするドメインを指定するエンタイトルメントを追加します。
2. NSUserActivity オブジェクトを受信したときに適切に応答するようにアプリデリゲートを更新します。

Xcode で、**Capabilities** タブの **Associated Domains** セクションを開き、アプリがサポートする各ドメインのエントリを `applinks:` をプレフィックスとして追加します。例：`applinks:www.mywebsite.com`。

{% alert note %}
Apple はこのリストを 20〜30 ドメイン以内に制限することを推奨しています。
{% endalert %}

### ステップ 5:ユニバーサルリンクをテストする

ユニバーサルリンクをメールに追加し、テストデバイスに送信します。Safari の URL フィールドにユニバーサルリンクを直接貼り付けても、アプリは自動的に開きません。その場合は、Web サイトを手動で下にプルして、該当するアプリを開くかどうかを尋ねるプロンプトが上部に表示されるようにする必要があります。

{% endtab %}

<!--Android instructions-->
{% tab Android %}

これらの手順は Android 開発者ドキュメントから適応されたものです。詳細については、[Add Android App Links](https://developer.android.com/training/app-links#add-app-links) および [Create Deep Links to App Content](https://developer.android.com/training/app-links/deep-linking) を参照してください。

{% alert note %}
Android App Links には、そのドメインからのリンクを他の Web URL とは別に処理するロジックを持つカスタム `IBrazeDeeplinkHandler` が必要です。代わりにディープリンクを使用し、メール以外のチャネルではリンクの方法を統一する方が簡単な場合があります。
{% endalert %}

### ステップ 1:ディープリンクを作成する

まず、Android アプリのディープリンクを作成する必要があります。これは、`AndroidManifest.xml` ファイルに[インテントフィルター](https://developer.android.com/guide/components/intents-filters)を追加することで行えます。インテントフィルターには、`VIEW` アクションと `BROWSABLE` カテゴリ、およびデータ要素に Web サイトの URL を含める必要があります。

### ステップ 2:アプリを Web サイトに関連付ける

アプリを Web サイトに関連付ける必要があります。これは、Digital Asset Links ファイルを作成することで行えます。このファイルは JSON 形式で、Web サイトへのリンクを開くことができる Android アプリの詳細が含まれています。Web サイトの `.well-known` ディレクトリに配置する必要があります。

### ステップ 3:アプリのマニフェストファイルを更新する

`AndroidManifest.xml` ファイルで、application 要素内に meta-data 要素を追加します。meta-data 要素には、`android:name` 属性に「asset_statements」を、`android:resource` 属性に Web サイトの URL を含む文字列配列を持つリソースファイルを指定する必要があります。

### ステップ 4:ディープリンクを処理するようにアプリを準備する

Android アプリで、受信するディープリンクを処理する必要があります。これは、アクティビティを開始したインテントを取得し、そこからデータを抽出することで行えます。

### ステップ 5:ディープリンクをテストする

最後に、ディープリンクをテストできます。メッセージングアプリまたはメールを通じて自分にリンクを送信し、クリックします。すべてが正しく設定されていれば、アプリが開くはずです。

{% endtab %}
{% endtabs %}

## ユニバーサルリンク、App Links、およびクリックトラッキング

{% alert note %}
クリックトラッキングリンクは通常、メールのオンボーディングの一環として設定されます。顧客のオンボーディング中に完了しなかった場合は、アカウントマネージャーにお問い合わせください。
{% endalert %}

メール送信パートナーである SendGrid と SparkPost は、クリックトラッキングドメインを使用してすべてのリンクをラップし、Braze メールのクリックトラッキング用の URL パラメーターを含めます。

たとえば、`https://www.example.com` のようなリンクは `https://links.email.example.com/uni/wf/click?upn=abcdef123456…` のようになります。

クリックトラッキング付きのメールリンクをユニバーサルリンクまたは App Links として機能させるには、追加の設定が必要です。クリックトラッキングドメイン（`links.email.example.com`）を、アプリが開くことを許可されるドメインとして追加してください。さらに、クリックトラッキングドメインは AASA（iOS）または Digital Asset Links（Android）ファイルを提供する必要があります。これにより、クリックトラッキング付きのメールリンクがシームレスに機能するようになります。

すべてのクリックトラッキングリンクをユニバーサルリンクまたは App Link にしたくない場合は、メール送信パートナーに基づいてどのリンクをユニバーサルリンクにするかを指定できます。詳細については、以下のセクションを参照してください。

### SendGrid

SendGrid のクリックトラッキングリンクをユニバーサルリンクとして扱うには、以下を行います。

1. AASA または AndroidManifest の pathPrefix 値を設定して、URL パスに `/uni/` を含むリンクのみをユニバーサルリンクとして扱うようにします。
2. リンクのアンカータグ（`<a>`）に属性 `universal="true"` を追加します。これにより、ラップされたリンクの URL パスに `/uni/` が含まれるようになります。

{% alert note %}
AMP メールの場合、この属性は data-universal="true" にする必要があります。
{% endalert %}

例：

```html
<a href=”https://www.example.com” universal="true">
```

{:start="3"}
3. アプリがラップされたリンクを適切に処理するように設定されていることを確認します。SendGrid の記事 [Resolving SendGrid Click Tracking Links](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-sendgrid-click-tracking-links) を参照し、お使いのオペレーティングシステムの手順に従ってください。この記事には [iOS](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-ios) と [Android](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-android) のサンプルコードが含まれています。

この設定により、URL パスに `/uni/` を含むリンクはユニバーサルリンクとして機能し、その他のすべてのリンクは Web リンクとして機能します。

### SparkPost

SparkPost のクリックトラッキングリンクをユニバーサルリンクとして扱うには、メールのドラッグ＆ドロップエディターの属性セクションに以下の属性を追加するか、リンクの HTML を手動で編集してリンクのアンカータグに以下の属性を含めます：`data-msys-sublink="custom_path"`。

このカスタムパスにより、その値を持つ URL を選択的にユニバーサルリンクとして扱うことができます。

例：

```html
<a href=”https://www.example.com” data-msys-sublink="open-in-app">
```

次に、アプリがカスタムパスを適切に処理するように設定されていることを確認します。SparkPost の記事 [Using SparkPost click tracking on deep links](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#preferred-solution-using-sparkpost-click-tracking-on-deep-links) を参照してください。この記事には [iOS](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#ios-swift-forwarding-clicks-to-sparkpost) と [Android](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#forwarding-clicks-from-android-to-sparkpost) のサンプルコードが含まれています。

### リンクごとのクリックトラッキングの無効化

特定のリンクのクリックトラッキングを無効にするには、HTML エディターのメールメッセージに HTML コードを追加するか、ドラッグ＆ドロップエディターの HTML ブロックに追加します。

#### SendGrid

メールサービスプロバイダー (ESP) が SendGrid の場合、次のように HTML コード `clicktracking=off` を使用します。

```HTML
<a clicktracking=off href="[INSERT https LINK HERE]">click here</a>
```

#### SparkPost

メールサービスプロバイダー (ESP) が SparkPost の場合、次のように HTML コード `data-msys-clicktrack="0"` を使用します。

```HTML
<a data-msys-clicktrack="0" href="[INSERT https LINK HERE]">click here</a>
```

#### Amazon SES

メールサービスプロバイダー (ESP) が Amazon SES の場合、次のように HTML コード `ses:no-track` を使用します。

```HTML
<a ses:no-track href="[INSERT https LINK HERE]">click here</a>
```

#### ドラッグ＆ドロップエディター

ドラッグ＆ドロップメールエディターを使用する場合、リンクがテキスト、ボタン、または画像に添付されている場合は、HTML コードをカスタム属性として入力します。

##### テキストリンクのカスタム属性

#### SendGrid

カスタム属性に以下を選択します。

- **Name:** `clicktracking`
- **Value:** `off`

#### SparkPost

カスタム属性に以下を選択します。

- **Name:** `data-msys-clicktrack`
- **Value:** `0`

![テキストリンクのカスタム属性。]({% image_buster /assets/img/text_click_tracking_off.png %}){: style="max-width:60%;"}

##### ボタンまたは画像のカスタム属性

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

![ボタンのカスタム属性。]({% image_buster /assets/img/button_click_tracking_off.png %}){: style="max-width:60%;"}

### クリックトラッキング付きユニバーサルリンクのトラブルシューティング

メール内のユニバーサルリンクが期待どおりに機能しない場合（受信者がメールアプリから Web ブラウザーに移動し、最終的にアプリにリダイレクトされるなど）、以下のヒントを参照してユニバーサルリンクの設定をトラブルシューティングしてください。

#### リンクファイルの場所を確認する

AASA ファイル（iOS）または Digital Asset Links ファイル（Android）が正しい場所にあることを確認します。

- **iOS:** `https://click.tracking.domain/.well-known/apple-app-site-association`
- **Android:** `https://click.tracking.domain/.well-known/assetlinks.json`

これらのファイルが常に公開アクセス可能であることを確認することが重要です。アクセスできない場合は、メール用のユニバーサルリンクの設定手順を見落としている可能性があります。

#### ドメイン定義を確認する

アプリが開くことを許可されるドメインの定義が正しいことを確認します。

- **iOS:** Xcode でアプリに設定された Associated Domains を確認します（[ステップ 1c]({{site.baseurl}}/help/help_articles/email/universal_links/?tab=ios#step-1c)）。クリックトラッキングドメインがそのリストに含まれていることを確認します。
- **Android:** アプリ情報ページを開きます（アプリアイコンを長押しして ⓘ をクリック）。アプリ情報メニュー内で **Open by default** を見つけてタップします。アプリが開くことを許可されているすべての検証済みリンクが表示される画面が表示されます。クリックトラッキングドメインがそのリストに含まれていることを確認します。