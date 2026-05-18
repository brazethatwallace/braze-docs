---
nav_title: "AMP for email"
article_title: "AMP for email"
alias: /amphtml/
page_order: 11
description: "このリファレンス記事では、AMP for Emailの概要と一般的なユースケースについて説明します。"
channel:
  - email

---

# AMP for email {#amp-for-email}

> [AMP for email](https://amp.dev/about/email)を使用すると、メールにインタラクティブな要素を追加し、顧客とのコミュニケーションを強化して、ユーザーの受信トレイに直接フル体験を届けることができます。AMPは、アンケート、フィードバック質問票、投票キャンペーン、レビュー、サブスクリプションセンターなど、魅力的なメールコンテンツの構築に役立つさまざまなコンポーネントを活用することでこれを実現します。これらのツールは、エンゲージメント向上とリテンションの機会を提供します。

## 要件 {#requirements}

Brazeは、ユーザーがGoogleに登録したり、必要なセキュリティ要件を満たしたりすることについて責任を負いません。AMP for emailはSparkPostとSendGridでのみ利用可能です。

| 要件   | 説明 |
| --------------| ----------- |
| AMP for emailの有効化 | AMPはすべてのユーザーが利用できます。 |
| Gmailアカウントのイネーブルメント | [Gmailアカウントの有効化](#enabling-gmail-account)を参照してください。 |
| Google送信者認証 | GmailはDKIM、SPF、DMARCを使用してAMPメールの[送信者を認証](https://developers.google.com/gmail/ampemail/security-requirements#sender_authentication)します。これらをアカウントに設定する必要があります。<br><br>- [DomainKeys Identified Mail](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) (DKIM) <br>- [Sender Policy Framework](https://en.wikipedia.org/wiki/Sender_Policy_Framework)(SPF)<br>- [Domain-based Message Authentication, Reporting, and Conformance](https://en.wikipedia.org/wiki/DMARC)(DMARC)
| AMPメール要素 | 魅力的なAMPメールには、さまざまなコンポーネントの戦略的な使用が含まれます。以下の[コンポーネント](#components)セクションの「必須要素」タブを参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements" }

### サポートされているメールクライアント {#supported-email-clients}

ユーザーにAMPメールを送信する前に、メールクライアントに登録する必要があります。登録プロセスでは、承認を得るためにテスト用のAMP HTMLメールを送信します。承認にかかる時間はクライアントによって異なります。詳細については、登録リンクをご確認ください。

| クライアント | 登録リンク |
| ------ | -------- |
| Gmail | [Google](https://developers.google.com/gmail/ampemail/register) |
| FairEmail | [FairEmail](https://email.faircode.eu/) |
| Yahoo | [Yahoo](https://senders.yahooinc.com/amp/) |
| Mail.ru | [Mail.ru](https://postmaster.mail.ru/amp/) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Supported email clients" }

サポートされているメールクライアントの完全なリストについては、[AMPドキュメント](https://amp.dev/support/faq/email-support)を参照してください。

### Gmailアカウントの有効化 {#enabling-gmail-account}

Gmailの設定に移動し、**全般**タブの**ダイナミックメールを有効にする**を選択します。

![「ダイナミックメールを有効にする」チェックボックスが選択されたGmail設定の例。]({% image_buster /assets/img/dynamic-content.png %})

## APIの使用 {#api-usage}

APIを使用してAMP for emailを利用することもできます。Brazeの[メッセージングエンドポイント]({{site.baseurl}}/api/endpoints/messaging/)のいずれかを使用してメールを送信する場合、以下に示すようにオブジェクト仕様として`amp_body`を追加します。

### メールオブジェクト仕様 {#email-object-specification}

```json
{
  "app_id": (required, string) see app identifier above,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <email@address.com>"),
  "reply_to": (optional, valid email address in the format "email@address.com" - defaults to your workspace's default reply to if not set),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "amp_body": (optional, updates the text-amp-html MIME type) the email body in AMP HTML. The MIME (Multipurpose Internet Mail Extensions) type to be referenced is "text/x-amp-html",
  "body": (required unless email_template_id is given, valid HTML),
  "preheader": (optional*, string) Recommended length 50-100 characters,
  "email_template_id": (optional, string) If provided, we will use the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case we will override the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid key-value hash), extra hash - for SendGrid customers, this will be passed to SendGrid as Unique Arguments,
  "headers": (optional, valid key-value hash), hash of custom extensions headers. Currently, only supported for SendGrid customers,
  "should_inline_css": (optional, boolean), whether to inline CSS on the body. If not provided, falls back to the default CSS inlining value for the workspace,
  "attachments": (optional, array), array of JSON objects like [{"file_name","url"}] that define the files you need attached. Your file name's extension will be detected automatically from the URL, which should return the appropriate `Content-Type` as a response header,
}
```

## AMPメールの作成 {#create-your-amp-email}

まず、[コンポーネント](#components)を使用してAMPメールを作成します。次に、[Braze API](#api-usage)を使用してメッセージを送信し、AMP HTML用の`amp_body`を必ず含めます。

AMP HTMLに加えて、通常のHTML `body`バージョンが必要であり、AMPメールの`plaintext_body`バージョンも推奨されます。すべてのAMPメールはマルチパートで送信されます。つまり、BrazeはHTML、プレーンテキスト、AMP HTMLをサポートするメールを送信します。これは、AMP for emailをまだサポートしていないプロバイダー経由でメールが送信された場合に便利です。メールはユーザーとそのデバイスに基づいて適切なバージョンに自動的にデフォルト設定されます。

{% alert note %}
AMPメールを作成する際は、AMPエディターで作業していることを確認してください。AMPコードはHTMLエディターに追加しないでください。
{% endalert %}

以下の追加リソースを参照してください:

- [AMPチュートリアル](https://amp.dev/documentation/guides-and-tutorials/start/create_email?format=email)
- 最終的な仕上がりを確認するための[サンプルコード](https://gist.github.com/CrystalOnScript/988c3f0a2eb406da27e9d9bf13a8bf73)。
- [AMPメールコンポーネントライブラリー](https://amp.dev/documentation/components/?format=email/)

### コンポーネント {#components}

AMP要素を構築する際は、エンジニアリングチームに確認し、デザインリソースや要素を含めて仕上がりの質を高めることをお勧めします。

{% tabs %}
  {% tab 必須要素 %}

以下の各要素は、AMPメールの本文に必須です。

| コンポーネント | 説明 | 例 |
|---------|--------------|---------|
| 識別子 <br><br> `⚡4email` または `amp4email`| メールをAMP HTMLメールとして識別します。 | `<!doctype html>` <br> `<html ⚡4email>` <br> `<head>` |
| AMPランタイムの読み込み <br><br> `<script>` | JavaScriptを使用してメール内でAMPを実行できるようにします。 | `<script async src="https://cdn.ampproject.org/v0.js"></script>`|
| CSSボイラープレート | AMPが読み込まれるまでコンテンツを非表示にします。<br> AMPメールをサポートするメールプロバイダーは、検証済みのAMPスクリプトのみがクライアントで実行されるようにセキュリティチェックを実施します。 | `<style amp4email-boilerplate>body{visibility:hidden}</style>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Components" }

  {% endtab %}
  {% tab ダイナミック %}

これらのコンポーネントを使用して、メール内にダイナミックなレイアウトと動作を作成します。

| コンポーネント | 説明 | 必要なスクリプト |
|---------|--------------|---------|
| [アコーディオン](https://amp.dev/documentation/components/amp-accordion?format=email) <br><br> `amp-accordion`| ユーザーがコンテンツの概要を表示し、任意のセクションにジャンプできるようにします。 | `<script async custom-element="amp-accordion" src="https://cdn.ampproject.org/v0/amp-accordion-0.1.js"></script>` |
| [フォーム](https://amp.dev/documentation/components/amp-form?format=email) <br><br> `amp-form`| AMPドキュメント内で入力フィールドを送信するフォームを作成します。 | `<script async custom-element="amp-form" src="https://cdn.ampproject.org/v0/amp-form-0.1.js"></script>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Components" }

{% alert note %}
ユーザーの認証が必要なコンポーネントは、[Googleアクセストークン](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens)または[プロキシアサーショントークン](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens)を使用する必要があります。
{% endalert %}
  {% endtab %}
  {% tab クリエイティブ %}

  AMPのコンポーネントを活用して、オーディエンスに合わせたメールを作成しましょう。

| コンポーネント | 説明 | 必要なスクリプト |
|---------|--------------|---------|
| [アニメーション画像](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-anim`| ランタイムで管理されるアニメーション画像（通常はGIF）を表示します。 | `<script async custom-element="amp-anim" src="https://cdn.ampproject.org/v0/amp-anim-0.1.js"></script>` |
| [カルーセル](https://amp.dev/documentation/components/amp-carousel?format=email) <br><br> `amp-carousel`| 類似した複数のコンテンツを水平軸に沿って表示します。 | `<script async custom-element="amp-carousel" src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>` |
| [画像](https://amp.dev/documentation/components/amp-img?format=email) | HTMLの`img`タグに代わるランタイム管理の要素です。<br>  [画像のライトボックス](https://amp.dev/documentation/components/amp-image-lightbox?format=email)を作成することもできます。 | `<amp-img alt="A view of the sea"` <br> `src="images/sea.jpg"` <br> `width="900"` <br>  `height="675"` <br>  `layout="responsive">`  <br> `</amp-img>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Components" }

{% alert note %}
ユーザーの認証が必要なコンポーネントは、[Googleアクセストークン](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens)または[プロキシアサーショントークン](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens)を使用する必要があります。
{% endalert %}

  {% endtab %}
  {% tab その他 %}

| コンポーネント | 説明 |
|---------|--------------|
| [データバインディングと式](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-bind`| データバインディングとJavaScriptライクな式を使用して、AMPページにカスタムのステートフルなインタラクティビティを追加します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Components" }

{% alert note %}
ユーザーの認証が必要なコンポーネントは、[Googleアクセストークン](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens)または[プロキシアサーショントークン](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens)を使用する必要があります。
{% endalert %}

{% endtab %}
{% endtabs %}

AMPコンポーネントの完全なリストについては、[AMPドキュメント](https://amp.dev/documentation/components/?format=email)をご確認ください。

### ユースケース {#use-cases}

{% tabs local %}
{% tab インタラクティブアンケート %}

`<amp-form>`コンポーネントを使用すると、メールの受信トレイを離れることなく完了できるインタラクティブなアンケートを作成できます。これは、`<amp-form>`を使用してアンケートの回答を送信し、バックエンドでこの集計データを提供することで実現できます。

例:
* カンファレンスアンケートメール
* フィード内のアイテムのダイナミックな更新
* 記事ブックマークメール

このコンポーネントを使用すると、ユーザーはフィールドの値を送信またはクリアできます。また、メールの設定方法に応じて、アンケートの送信が成功したかどうかなどの追加プロンプトをユーザーに表示したり、アンケート結果（投票キャンペーンなど）を表示してユーザーの回答をレンダリングしたりできます。

{% endtab %}
{% tab 折りたたみ可能なコンテンツ %}

`<amp-accordion>`コンポーネントを使用して、コンテンツセクションを展開できます。このコンポーネントを使用すると、折りたたみ可能で展開可能なコンテンツセクションを表示でき、閲覧者がコンテンツの概要を一目で確認し、任意のセクションにジャンプできるようになります。

長い教育記事やパーソナライズ済みのおすすめを送信する場合、閲覧者がコンテンツの概要を一目で確認し、任意のセクションや特定の製品のおすすめにジャンプして詳細を確認できるようになります。これは、セクション内の数文でもスクロールが必要になるモバイルユーザーにとって特に便利です。
{% endtab %}
{% tab 画像が多いメール %}

小売ブランドのように多くのプロフェッショナルな写真を含むメールを送信する場合、`<amp-image-lightbox>`コンポーネントを使用すると、ユーザーが気に入った画像を操作できるようになります。ユーザーが画像をクリックすると、このコンポーネントはメッセージの中央に画像を表示し、ライトボックス効果を作成します。

さらに、`<amp-image-lightbox>`コンポーネントを使用すると、ユーザーは詳細な画像の説明を表示できます。同じコンポーネントを複数の画像に使用できます。たとえば、メールに複数の画像が含まれている場合、ユーザーがいずれかの画像をクリックすると、その画像がライトボックスに表示されます。

{% endtab %}
{% tab テキスト重視のメール %}

主にテキストコピーに依存するメールの場合、`<amp-fit-text>`コンポーネントを使用すると、指定された領域内のテキストのサイズとフィットを管理できます。

例:

- テキストを領域に合わせてスケーリング
- 最大フォントサイズを使用してテキストを領域に合わせてスケーリング（最大フォントサイズを設定可能）
- コンテンツが領域をオーバーフローした場合にテキストを切り詰め

{% endtab %}
{% endtabs %}

### amp-mustacheの使用 {#use-amp-mustache}

Liquidと同様に、AMPはより高度なユースケース向けのスクリプト言語をサポートしています。このコンポーネントは[`amp-mustache`](https://amp.dev/documentation/components/amp-mustache/?format=email)と呼ばれます。Mustacheマークアップ言語を含める場合は、Liquidの[`raw`](https://shopify.github.io/liquid/tags/raw/)タグで囲む必要があります。LiquidとMustacheは構文スタイルを共有していることに注意してください。

コンテンツを`raw`タグで囲むと、Brazeの処理エンジンは`raw`タグ間のコンテンツを無視し、チームが必要とするMustache変数を送信します。

## 指標と分析 {#metrics-and-analytics}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Metrics and analytics">
  <caption>指標と分析</caption>
    <thead>
        <tr>
            <th>指標</th>
            <th>詳細</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">開封数合計</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Opens' %} AMPメールの場合、これはHTMLバージョンとプレーンテキストバージョンの合計開封数です。</td>
        </tr>
        <tr>
            <td class="no-split">クリック数合計</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Clicks' %} AMPメールの場合、これはHTMLバージョンとプレーンテキストバージョンの合計クリック数です。</td>
        </tr>
        <tr>
            <td class="no-split">AMP開封数</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='AMP Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split">AMPクリック数</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='AMP Clicks' %}</td>
        </tr>
    </tbody>
</table>

## テストとトラブルシューティング {#test-and-troubleshoot}


AMPメールを送信する前に、以下をお勧めします:

- これらの[Gmailガイドライン](https://developers.google.com/gmail/ampemail/testing-dynamic-email)に従ってテストすること。
- [Gmail AMP for Email Playground](https://amp.gmail.dev/playground/)を使用してAMPマークアップを検証すること。
  - AMPメールでLiquidタグを使用している場合は、Gmail AMP for Email Playgroundに貼り付ける前に、静的なプレースホルダー値に置き換えてください。レンダリングされていないLiquidタグはバリデーションエラーの原因になります。

AMPメールがGmailアカウントに配信されるためには、メールが以下の条件を満たす必要があります:

- AMP for emailのセキュリティ要件を満たしていること。
- AMP MIMEパートに有効なAMPドキュメントが含まれていること。
- メールにHTML MIMEパートの前にAMP MIMEパートが含まれていること。
- AMP MIMEパートが100&nbsp;KB未満であること。

合計クリック数とユニーククリック数には、AMPメッセージから発生したクリック（HTMLとプレーンテキストのみ）は含まれないことに注意してください。AMP固有のクリックは*amp_click*指標に帰属されます。

これらの条件のいずれもエラーの原因でない場合は、[サポート]({{site.baseurl}}/support_contact/)にお問い合わせください。

### Gmailの受信トレイでAMPメールをレンダリングするように設定する {#configure-gmail-inbox-to-render-amp-emails}

以下の手順で、テスト目的でAMPメールをレンダリングするようにGmailの受信トレイを設定できます:

1. Gmailで、受信トレイの右上にある**設定**を選択します。
2. **すべての設定を表示**を選択します。
3. **全般**タブで、**ダイナミックメール**セクションに移動し、**ダイナミックメールを有効にする**チェックボックスが選択されていることを確認します。
4. 次に、**デベロッパー設定**を選択し、**この送信者からのダイナミックメールを常に許可する:**チェックボックスを選択します。
5. テストメッセージの差出人アドレスと同じドメインを入力します。
6. 変更を保存します。

これで、テストメールをGmailアカウントに送信でき、AMPメールがGmailでレンダリングされるようになります。

### よくある質問 {#frequently-asked-questions}

#### AMPメールでセグメンテーションを使用すべきですか？ {#should-i-segment-with-amp-emails}

さまざまなタイプのユーザーに送信するためにセグメンテーションを使用しないことをお勧めします。これは、AMPメッセージをマルチパートで送信し、元のメールに異なるバージョンが含まれているためです。ユーザーがAMPバージョンを表示できない場合、HTMLにデフォルトで戻ります。