---
nav_title: スタイリング例
article_title: スタイリング例
description: "これは、ヘッダー、タブ、コードブロックなど、Braze Docsでページがスタイル設定される方法です。"
page_order: 8
noindex: true
---

# スタイリング例 {#styling-examples}

これは、ヘッダー、タブ、コードブロックなど、Braze Docsでページがスタイル設定される方法です。

## ヘッダーテスト {#header-test}

{% tabs %}
{% tab Styling %}

# H1バナー {#h1-banner}
H1テキスト

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

## H2バナー {#h2-banner}
H2テキスト

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

### H3バナー {#h3-banner}
H3テキスト

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

#### H4バナー {#h4-banner}
H4テキスト

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

##### H5バナー {#h5-banner}
H5テキスト

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

###### H6バナー {#h6-banner}
H6テキスト

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

{% endtab %}
{% tab Markdown %}

```
# H1 Banner

## H2 Banner

### H3 Banner

#### H4 Banner

##### H5 Banner

###### H6 Banner
```
{% endtab %}
{% endtabs %}

## カスタムヘッダーアンカー {#custom-header-anchor}

ヘッダーにアンカーを追加するには、ヘッダーがある行の末尾に次のコードを追加します。`anchor-text`をこの見出しのアンカーに置き換えます。小文字を使用し、単語間にハイフンを入れてください。

```
# Heading Text {#anchor-text}
```

番号記号`#`の後にカスタムアンカーが続く標準リンクを作成することで、カスタムアンカーを持つ見出しにリンクできます。

{% raw %}
```
Here is my [link](#anchor-text)
```
{% endraw %}

## フォントテスト {#font-test}

{% tabs %}
{% tab Styling %}

通常テキスト

*強調テキスト*

**太字**

_**太字強調**_

~~取り消し線~~

{% endtab %}
{% tab Markdown %}
```
Normal Text

*Emphasize Text*

**Bold**

_**Bold Emphasize**_

~~Strikethrough~~
```
{% endtab %}
{% endtabs %}

## 引用テスト {#quote-test}

{% tabs %}
{% tab Styling %}
> 引用テキスト

#### インライン引用 {#inline-quote}
Lorem ipsum dolor ``sit amet, consectetur adipiscing elit``. Sed nec tortor at lectus tempus tempor.

#### 引用ブロック {#quote-chunk}
```
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor.
```
{% endtab %}
{% tab Markdown %}
```
> Quoted Text

Lorem ipsum dolor ``sit amet, consectetur adipiscing elit``. Sed nec tortor at lectus tempus tempor.

````````` Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. ```
```
{% endtab %}
{% endtabs %}

## テーブルテスト

{% tabs %}
{% tab Styling %}
| インスタンス | ダッシュボードURL                                                         | RESTエンドポイント                   |
| -------- | --------------------------------------------------------------------- | ------------------------------- |
| US-01    | `https://dashboard.braze.com` or<br> `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` |
| US-02    | `https://dashboard-02.braze.com`                                      | `https://rest.iad-02.braze.com` |
| US-03    | `https://dashboard-03.braze.com`                                      | `https://rest.iad-03.braze.com` |
| US-04    | `https://dashboard-04.braze.com`                                      | `https://rest.iad-04.braze.com` |
| US-05    | `https://dashboard-05.braze.com`                                      | `https://rest.iad-05.braze.com` |
| US-06    | `https://dashboard-06.braze.com`                                      | `https://rest.iad-06.braze.com` |
| US-07    | `https://dashboard-07.braze.com`                                      | `https://rest.iad-07.braze.com` |
| US-08    | `https://dashboard-08.braze.com`                                      | `https://rest.iad-08.braze.com` |
| EU-01    | `https://dashboard.braze.eu` or<br> `https://dashboard-01.braze.eu`   | `https://rest.fra-01.braze.eu`  |
| AU-01    | `https://dashboard.au-01.braze.com/`                                  | `https://rest.au-01.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Table Test" }
{% endtab %}
{% tab Markdown %}
```
| Instance | Dashboard URL                                                         | REST Endpoint                   |
|----------|-----------------------------------------------------------------------|---------------------------------|
| US-01    | `https://dashboard.braze.com` or<br> `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` |
| US-02    | `https://dashboard-02.braze.com`                                      | `https://rest.iad-02.braze.com` |
| US-03    | `https://dashboard-03.braze.com`                                      | `https://rest.iad-03.braze.com` |
| US-04    | `https://dashboard-04.braze.com`                                      | `https://rest.iad-04.braze.com` |
| US-05    | `https://dashboard-05.braze.com`                                      | `https://rest.iad-05.braze.com` |
| US-06    | `https://dashboard-06.braze.com`                                      | `https://rest.iad-06.braze.com` |
| US-07    | `https://dashboard-07.braze.com`                                      | `https://rest.iad-07.braze.com` |
| US-08    | `https://dashboard-08.braze.com`                                      | `https://rest.iad-08.braze.com` |
| EU-01    | `https://dashboard.braze.eu` or<br> `https://dashboard-01.braze.eu`   | `https://rest.fra-01.braze.eu`  |
| EU-02    | `https://dashboard-02.braze.eu`                                       | `https://rest.fra-02.braze.eu`  |
| AU-01    | `https://dashboard.au-01.braze.com/`                                  | `https://rest.au-01.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Table Test" }
```
{% endtab %}
{% endtabs %}

#### テーブルの列ごとのワードブレークのリセット

テーブルの列ごとのワードブレークをリセットするには、次の構文を使用します。

`````````markdown
{: .reset-td-br-NUM .reset-td-br-NUM .reset-td-br-NUM .reset-td-br-NUM aria-label="Resetting Table word-break by column" }
```

`NUM`を対応する列番号に置き換えます（最大4列まで）。4列未満の場合は、余分な`.reset-td-br-NUM`プレースホルダーを削除してください。テーブルは次のようになります。

`````````markdown
| Event Name                                                       | Feed Type              | Description                                                  | Custom Attributes                                                             |
| ---------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG             | Unbound Feed           | An email was successfully delivered to a User's mail server. | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Unbound Feed           | User opened an email.                                        | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| In-App Message Impression                                        | Platform-specific Feed | User viewed an In-App Message.                               | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Resetting Table word-break by column" }

```
{% tabs local %}
{% tab 導入前 %}

| イベント名                                                       | フィードタイプ              | 説明                                                  | カスタム属性                                                             |
| ---------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG             | Unbound Feed           | メールがユーザーのメールサーバーに正常に配信されました。 | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Unbound Feed           | ユーザーがメールを開封しました。                                        | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| In-App-Message-Impression                                        | Platform-specific Feed | ユーザーがアプリ内メッセージを閲覧しました。                               | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |

{% endtab %}
{% tab 適用後 %}

| イベント名                                                       | フィードタイプ              | 説明                                                  | カスタム属性                                                             |
| ---------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG             | Unbound Feed           | メールがユーザーのメールサーバーに正常に配信されました。 | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Unbound Feed           | ユーザーがメールを開封しました。                                        | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| In-App-Message-Impression                                        | Platform-specific Feed | ユーザーがアプリ内メッセージを閲覧しました。                               | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Resetting Table word-break by column" }
{% endtab %}
{% endtabs %}

## リンクテスト
{% tabs %}
{% tab Styling %}
リンクはこちら: [Braze.com](https://www.braze.com){: height="36px" width="36px"}
{% endtab %}
{% tab Markdown %}
```
[Braze.com](https://www.braze.com)
```
{% endtab %}
{% endtabs %}

## 画像テスト
{% tabs %}
{% tab Styling %}
画像: ![ロゴ]({% image_buster /assets/img/braze-logo-mark.png %}){: style="max-width:30%;"}

#### リンク付き画像テスト

リンク付き画像: [![Braze]({% image_buster /assets/img/braze-logo-mark.png %}){: style="max-width:30%;"}](https://www.braze.com)

#### 画像のスタイリング

![テキスト]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="max-width:30%; color: green" }

#### 画像のアンカリング

![テキスト]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="float:right;max-width:30%; color: green" }
<br><br><br><br><br>
{% endtab %}
{% tab Markdown %}

```
![Logo]({% image_buster /assets/img/braze-logo-mark.png %}){: style="max-width:30%;"}

[![Braze]({% image_buster /assets/img/braze-logo-mark.png %})](https://www.braze.com)

![Text]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="max-width:30%; color: green" }

![Text]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="float:right;max-width:30%;" }
```
{% endtab %}
{% endtabs %}

## ギャラリーテスト
{% tabs %}
{% tab Styling %}
{% gallery %}
{{site.baseurl}}/assets/img_archive/EBTH_Email.png?bf892368baf287cba5ab9a6e3b09431d <br> これは[リンク](https://www.braze.com)です。
{{site.baseurl}}/assets/img_archive/iHeartRadio_Email.png?ecd2c8fe148939b7de957fe85cd6317e <br> これは別の`comment`です。
{{site.baseurl}}/assets/img_archive/Saucey_Email.png?b9768937a1cc12d4c08e55a52e700d68 <br> これはさらに別の**comment**です。
{{site.baseurl}}/assets/img/schellman_iso27001_seal_grey_CMYK_300dpi_jpg.png?1b1fb9dbb80b0332c62512dcf9c83258 <br> **画像タイトル** <br> これは改行されるかどうかのテストです。
{{site.baseurl}}/assets/img/SOC2.png?6338040be8e98c4c9abe1f35b3e43e3a <br> これは通常のコメントです。
{% endgallery %}
{% endtab %}
{% tab Markdown %}
{% raw %}
```
{% gallery %}
{{site.baseurl}}/assets/img_archive/EBTH_Email.png?bf892368baf287cba5ab9a6e3b09431d  <br> This is a [link](https://www.braze.com).
{{site.baseurl}}/assets/img_archive/iHeartRadio_Email.png?ecd2c8fe148939b7de957fe85cd6317e  <br> This is another `comment`.
{{site.baseurl}}/assets/img_archive/Saucey_Email.png?b9768937a1cc12d4c08e55a52e700d68  <br> This is yet another **comment**.
{{site.baseurl}}/assets/img/schellman_iso27001_seal_grey_CMYK_300dpi_jpg.png?1b1fb9dbb80b0332c62512dcf9c83258 <br> **IMAGE TITLE** <br> This is a test to see if it will line break.
{{site.baseurl}}/assets/img/SOC2.png?6338040be8e98c4c9abe1f35b3e43e3a  <br> This is a regular comment.
{% endgallery %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## インタラクティブ画像テスト
{% tabs %}
{% tab Styling %}
<div class="iactiveImg" data-ii="6967"></div><script src="https://interactive-img.com/js/include.js"></script>
{% endtab %}
{% tab Markdown %}
```
<div class="iactiveImg" data-ii="6967"></div><script src="https://interactive-img.com/js/include.js"></script>
```
{% endtab %}
{% endtabs %}
<!--- Leaving formatting here just in case it's important...
<div style="position: relative; padding-bottom: 83%; padding-top: 0; height: 0;"><iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border-width:0px; max-width:100%; overflow-y:auto;" width="100%" height="100%" src="https://interactive-img.com/view?id=6967&iframe=true"></iframe></div>
-->

## コードスニペットテスト

{% tabs %}
{% tab Styling %}
#### コードテスト Objective C
`````````objc
- (void)submitFeedback:(ABKFeedback * )feedback
 withCompletionHandler:(nullable void (^)(ABKFeedbackSentResult feedbackSentResult))completionHandler;
```

#### コードテスト Swift
`````````swift
Appboy.sharedInstance()?.submitFeedback(feedback) { (feedbackSentResult) in
      print("Feedback sent: (feedbackSentResult)")
    }
```

#### コードテスト Java
`````````java
@Override
public void onResume() {
  super.onResume();
  // Registers the BrazeInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(activity);
}
```

#### コードテスト json
```json
{
   "attributes" : "Attributes" ,
   "events" : ["Array", "Of", "Object"],
   "purchases" : ["Array" ,"Of" ,"Purchase" ,"Object"]
}
```

#### コードテスト JavaScript
`````````javascript
braze.subscribeToFeedUpdates(function(feed) {
  var cards = feed.cards;
  braze.showFeed(undefined, cards);
});
braze.requestFeedRefresh();
```

#### Pygmentsテスト
`````````python
#!/usr/bin/python3

from engine import RunForrestRun

"""Test code for syntax highlighting!"""

class Foo:
	def __init__(self, var):
		self.var = var
		self.run()

	def run(self):
		RunForrestRun()  # run along!

```
{% endtab %}
{% tab Markdown %}
![Markdownの例]({% image_buster /assets/img_archive/code_snippet.png %})
{% endtab %}
{% endtabs %}

## アラートテスト

{% tabs %}
{% tab Styling %}

{% alert tip %}これはヒントです{% endalert %}

{% alert note %}これはメモです{% endalert %}

{% alert important %}これは重要なアラートです{% endalert %}

{% alert warning %}これは警告です{% endalert %}

{% alert update %}これはアップデートです{% endalert %}

{% endtab %}
{% tab Markdown %}
{% raw %}
```
{% alert tip %}
This is a tip
{% endalert %}

{% alert note %}
This is a note
{% endalert %}

{% alert important %}
This is a important alert
{% endalert %}

{% alert warning %}
This is a warning
{% endalert %}

{% alert update %}
This is a update
{% endalert %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 埋め込み動画テスト
{% tabs %}
{% tab Styling %}
#### 埋め込み動画/YouTube
デフォルトではYouTubeが埋め込まれます。
{% multi_lang_include video.html id="9SrKbY4BV2E" source="youtube" %}

#### 埋め込み動画/Wistia
Wistia動画を埋め込みます。
{% multi_lang_include video.html id="c5lgi4xnvo" source="wistia" %}

#### 埋め込み動画 右寄せ
{% multi_lang_include video.html id="9SrKbY4BV2E" align="right" source="youtube" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

#### 埋め込み動画 左寄せ
{% multi_lang_include video.html id="9SrKbY4BV2E" align="left" source="youtube" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.
<br /><br />

#### Loomの例
* `source="loom"`を使用します
{% multi_lang_include video.html id="c1d3199463c448e8918f046265b54eb2" source="loom" %}

{% endtab %}
{% tab Markdown %}

YouTube動画を埋め込むには、YouTube IDが必要です。URLの`v=`の後に表示されます。たとえば、`https://www.youtube.com/watch?v=VR1qn1OBP7k`のIDは`VR1qn1OBP7k`です。

{% raw %}
`````````html
{% multi_lang_include video.html id="[youtube_id]" source="youtube" %}
```
{% endraw %}

右寄せまたは左寄せにし、最大幅を50%に制限するには、`align`パラメーターに`left`または`right`を使用します。
{% raw %}
`````````html
{% multi_lang_include video.html id="[youtube_id]" align="left" source="youtube" %}

{% multi_lang_include video.html id="[youtube_id]" align="right" source="youtube" %}
```
{% endraw %}

Loomの例:
{% raw %}
`````````html
{% multi_lang_include video.html id="[lid]" source="loom" %}
```
{% endraw %}

{% endtab %}
{% endtabs %}

#### 高解像度向けステータス配置付きフィーチャー動画レイアウト

高解像度表示用に左側に静的動画を配置するフィーチャー動画レイアウトを使用するには、ページのYAMLヘッダーに`video_id`と`video_type`（`youtube`など）を追加します。デフォルトでは`video_source`は`youtube`に設定されています。

{% raw %}
`````````yaml
layout: featured_video
video_id: [video_id]
video_source: youtube
```
{% endraw %}

## リストテスト
{% tabs %}
{% tab Styling %}
#### 箇条書き

- リスト1
  - サブリスト1
- リスト2
  - サブリスト2a
    - サブサブリスト2
- リスト3

#### 番号付き

1. リスト1
   - サブリスト1
2. リスト2
3. リスト3
   - サブリスト3a
   - サブリスト3b
     - サブサブリスト3
4. リスト4
    1. サブリスト4a
        1. サブサブリスト4
    2. サブリスト4b
        1. サブサブリスト4

{% endtab %}
{% tab Markdown %}
```
#### Bullet

- List 1
  - Sub List 1
- List 2
  - Sub List 2a
    - Sub Sub List 2
- List 3

#### Numbered

1. List 1
   - Sub List 1
2. List 2
3. List 3
   - Sub List 3a
   - Sub List 3b
     - Sub Sub List 3
4. List 4
    1. Sub list 4a
        1. Sub Sub List 4
    2. Sub list 4b
        1. sub sub list 4
```
{% endtab %}
{% endtabs %}

## 折りたたみコンテンツテスト {#collapsible-content}
{% tabs %}
{% tab Styling %}
{% details クリックして展開 %}
#### 隠しコードブロックがあります！

`````````python
print("hello world!")
```
{% enddetails %}
{% endtab %}
{% tab Markdown %}
{% raw %}
`````````liquid
{% details Click me to Expand %}
...
{% enddetails %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## タブテスト

#### カスタムタブ

{% tabs local %}
{% tab OBJECTIVE-C %}

`AppDelegate.m`ファイルに次のコード行を追加します。

`````````objc
{% if include.platform == 'iOS' %}#import "Appboy-iOS-SDK/AppboyKit.h"{% else %}#import <AppboyTVOSKit/AppboyKit.h>{% endif %}
```

`AppDelegate.m`ファイル内の`application:didFinishLaunchingWithOptions`メソッドに次のスニペットを追加します。

`````````objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

{% endtab %}
{% tab swift %}

Braze SDKをCocoaPodsまたはCarthageで統合する場合は、`AppDelegate.swift`ファイルに次のコード行を追加します。

`````````swift
{% if include.platform == 'iOS' %}#import Appboy_iOS_SDK{% else %}#import AppboyTVOSKit{% endif %}
```

SwiftプロジェクトでObjective-Cコードを使用する方法の詳細については、[Apple Developer Docs][apple_initial_setup_19]を参照してください。

`AppDelegate.swift`の`application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`に次のスニペットを追加します。

`````````swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```
{% endtab %}
{% endtabs %}

#### 使い方
{% raw %}
**tabs**を`{% tabs %}`と`{% endtabs %}`で囲みます。
個々の**tab**をLiquidコードとタブ名`{% tab [タブ名] %}`と`{% endtab %}`で囲みます。
{% endraw %}

{% alert important %}
 ページ上のタブの数は一貫している必要があります。そうでないと、タブのコンテンツが非表示になる場合があります。
 たとえば、あるタブセットに`C++`、`C-Sharp`、`JS`があり、別のタブセットに`C-Sharp`と`JS`がある場合、
誰かが`C++`をクリックすると、もう一方のセクションには何も表示されません。回避策については、以下のローカルタブオプションを参照してください。
{% endalert %}

{% raw %}
`````````liquid
{% tabs %}
{% tab objective-c %}
Content of objective-c
{% endtab %}
{% tab swift %}
Content of swift
{% endtab %}
{% endtabs %}
```
{% endraw %}

#### ローカルタブ
特定のセクションのタブコンテンツのみを変更する自己完結型タブの場合は、親タブブロックでlocalパラメーターを使用します。

{% raw %}
`````````liquid
{% tabs local %}
...
{% endtabs %}
```
{% endraw %}

#### サブタブ
タブ内のタブには、`subtabs`と`subtab`を使用できます。デフォルト設定は`local`です。
グローバルな`subtabs`には、`global`オプションを使用します: {% raw %}`{% subtabs global %}`{% endraw %}

{% tabs local %}
{% tab Tab 1 %}
タブコンテンツ1
{% subtabs %}
{% subtab Subtab 1a %}
サブタブ1aのコンテンツ
{% endsubtab %}
{% subtab Subtab 2a %}
サブタブ2aのコンテンツ
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Tab 2 %}
タブコンテンツ2
{% subtabs %}
{% subtab Subtab 1b %}
サブタブ1bのコンテンツ
{% endsubtab %}
{% subtab Subtab 2b %}
サブタブ2bのコンテンツ
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

##### Markdown
{% raw %}
```
{% tabs local %}
{% tab Tab 1 %}
tab content 1
{% subtabs %}
{% subtab Subtab 1a %}
Subtab 1a content
{% endsubtab %}
{% subtab Subtab 2a %}
Subtab 2a content
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Tab 2 %}
tab content 2
{% subtabs %}
{% subtab Subtab 1b %}
Subtab 1a content
{% endsubtab %}
{% subtab Subtab 2b %}
Subtab 2a content
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
```
{% endraw %}

[1]: {% image_buster /assets/img_archive/code_snippet.png %}