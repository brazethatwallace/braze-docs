---
nav_title: "メールガイドライン"
article_title: "メールガイドライン"
page_order: 1
page_type: reference
description: "この記事では、さまざまなユースケースやトピックに対応するメールキャンペーンを作成する際に覚えておくべき一般的なヒントやコツについて説明します。"
channel: email

---

# メールガイドライン

> メールキャンペーンを作成する際には、さまざまなユーザーやメールサービスプロバイダー (ESP) でメールメッセージがどのように受信されるかを念頭に置くことが重要です。

コンテンツを作成する際に覚えておくべきヒントをいくつかご紹介します。

- メールのフォーマットには、インラインスタイルシートとして CSS を使用してください。
- モバイルとデスクトップの両方で1つのメールテンプレートを使用するには、幅を500ピクセル未満に抑えてください。
- 画像は5&nbsp;MB未満にする必要があります。最大限の互換性を確保するために、PNG、JPEG、または GIF の使用を推奨します。SVG や WebP は、多くの主要なメールクライアントがまだサポートしていないため、避けてください。
- 画像に高さと幅を設定しないでください。劣化したメールで不要な余白が生じる可能性があります。
- `div` タグは使用しないでください。ほとんどのメールクライアントがその使用をサポートしていません。代わりに、ネストされたテーブルを使用してください。
- JavaScript はどの ESP でも動作しないため、使用を避けてください。
- Braze はグローバル CDN を使用してすべてのメール画像をホストすることで、読み込み時間を改善しています。
- モバイルでは、画像カラムは狭い（各約100px）ため、複数画像の行でも収まります（例：4つの画像 ≈ 4つの使用可能なカラム）。

### 代替テキストの実装

スパムフィルターは HTML とプレーンテキストの両方のバージョンを監視するため、プレーンテキストの代替を活用することはスパムスコアを下げる優れた方法です。さらに、代替テキスト `(alt="")` は、ユーザーのメールプロバイダーによってフィルタリングされた可能性のあるメール本文の画像を補完したり、場合によっては代替したりすることができます。スクリーンリーダーは画像を説明するために代替テキストを読み上げるため、これは平易な言葉で画像に関する重要な情報を提供する機会です。

### メールバリデーション

{% alert important %}
バリデーションは、ダッシュボードのメールアドレス、エンドユーザー（顧客）のメールアドレス、およびメールメッセージの差出人アドレスと返信先アドレスに対して使用されます。
{% endalert %}

メールバリデーションは、ユーザーのメールアドレスが更新されたとき、または API、CSV アップロード、SDK によって Braze にインポートされたとき、あるいはダッシュボードで変更されたときに行われます。メールアドレスには空白を含めることはできず、API を使用して送信した場合、空白があると `400` エラーが発生する可能性があります。

Braze サーバー経由でターゲットされるメールアドレスは、[RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822) 標準に従ってバリデーションされる必要があります。Braze は特定の文字を受け付けず、無効として認識します。メールがバウンスした場合、Braze はそのメールを無効としてマークし、サブスクリプションステータスは変更されません。

許可されていない文字やメールバリデーションルールについては、[メールバリデーション]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation/#how-it-works)を参照してください。

### 差出人アドレスと返信先アドレスの設定

「差出人」アドレスを設定する際は、「差出人」メールドメインが送信ドメインと一致していることを確認してください（例：`marketing.yourdomain.com`）。一致しない場合、SPF と DKIM の不整合が発生する可能性があります。すべての返信先メールはルートドメインに設定できます。

{% alert note %}
「差出人」アドレスでは Unicode エンコーディングはサポートされていません。
{% endalert %}

## レイアウト（ドラッグ＆ドロップおよびカスタム HTML）

Braze が生成した HTML/CSS がカスタム HTML と競合すると、レイアウトが崩れることがあります。この場合は、以下を行ってください。

- まずカスタム HTML/CSS を削除します
- プレビューでカスタムフォントが正しく読み込まれることを確認します
- 行とカラムのパディングを確認します
- テーブルベースのレイアウトを優先し、エディターの幅内に収めてください。

エディター外から HTML を取り込む Content Blocks もレイアウトを崩す可能性があります。

## メール URL での UTM パラメーターの使用

UTM パラメーターは分析のために URL にタグを付けます。Liquid やカスタム属性を使用して構築できます。

- 最終 URL にはクエスチョンマーク `?` を1つだけ使用してください（追加の `?` はリクエストを壊す可能性があります）。
- 値にスペースや特殊文字を使用しないでください（`_` または `-` を使用してください）。
- 分析ツールが UTM を取り込むことを確認してください。Liquid の `capture` ブロック内の末尾のスペースをトリミングしてください。UTM は大文字と小文字を区別します。

### HTML の詳細確認

一部の HTML タグや属性は、ブラウザで悪意のあるコードが実行される可能性があるため、許可されていません。

メールで許可されていない HTML タグと属性については、以下のリストを確認してください。
{% details 許可されていない HTML タグを展開 %}
- `<!doctype>`
- `<applet>`
- `<bgsound>`
- `<embed>`
- `<frameset>`
- `<iframe>`
- `<ilayer>`
- `<layer>`
- `<link>`
- `<meta>`
- `<object>`
- `<script>`
- `<title>`
- `<xml>`
- `<svg>`
{% enddetails %}

{% details 許可されていない HTML 属性を展開 %}
- `<animationend>`
- `<animationiteration>`
- `<animationstart>`
- `<data-bind>`
- `<fscommand>`
- `<onabort>`
- `<onabort>`
- `<onactivate>`
- `<onafterprint>`
- `<onafterupdate>`
- `<onbeforeactivate>`
- `<onbeforecopy>`
- `<onbeforecut>`
- `<onbeforedeactivate>`
- `<onbeforeeditfocus>`
- `<onbeforepaste>`
- `<onbeforeprint>`
- `<onbeforeunload>`
- `<onbeforeupdate>`
- `<onbegin>`
- `<onblur>`
- `<onbounce>`
- `<oncanplay>`
- `<oncanplaythrough>`
- `<oncellchange>`
- `<onchange>`
- `<onclick>`
- `<oncontextmenu>`
- `<oncontrolselect>`
- `<oncopy>`
- `<oncut>`
- `<ondataavailable>`
- `<ondatasetchanged>`
- `<ondatasetcomplete>`
- `<ondblclick>`
- `<ondeactivate>`
- `<ondrag>`
- `<ondragdrop>`
- `<ondragend>`
- `<ondragenter>`
- `<ondragleave>`
- `<ondragover>`
- `<ondragstart>`
- `<ondrop>`
- `<ondurationchange>`
- `<onemptied>`
- `<onend>`
- `<onended>`
- `<onerror>`
- `<onerror>`
- `<onerrorupdate>`
- `<onfilterchange>`
- `<onfinish>`
- `<onfocus>`
- `<onfocusin>`
- `<onfocusout>`
- `<onhashchange>`
- `<onhelp>`
- `<oninput>`
- `<oninvalid>`
- `<onkeydown>`
- `<onkeypress>`
- `<onkeyup>`
- `<onlayoutcomplete>`
- `<onload>`
- `<onloadeddata>`
- `<onloadedmetadata>`
- `<onloadstart>`
- `<onlosecapture>`
- `<onmediacomplete>`
- `<onmediaerror>`
- `<onmessage>`
- `<onmousedown>`
- `<onmouseenter>`
- `<onmouseleave>`
- `<onmousemove>`
- `<onmouseout>`
- `<onmouseover>`
- `<onmouseup>`
- `<onmousewheel>`
- `<onmove>`
- `<onmoveend>`
- `<onmovestart>`
- `<onoffline>`
- `<ononline>`
- `<onopen>`
- `<onoutofsync>`
- `<onpagehide>`
- `<onpageshow>`
- `<onpaste>`
- `<onpause>`
- `<onplay>`
- `<onplaying>`
- `<onpopstate>`
- `<onprogress>`
- `<onpropertychange>`
- `<onratechange>`
- `<onreadystatechange>`
- `<onredo>`
- `<onrepeat>`
- `<onreset>`
- `<onresize>`
- `<onresizeend>`
- `<onresizestart>`
- `<onresume>`
- `<onreverse>`
- `<onrowdelete>`
- `<onrowexit>`
- `<onrowinserted>`
- `<onrowsenter>`
- `<onscroll>`
- `<onsearch>`
- `<onseek>`
- `<onseeked>`
- `<onseeking>`
- `<onselect>`
- `<onselectionchange>`
- `<onselectstart>`
- `<onshow>`
- `<onstalled>`
- `<onstart>`
- `<onstop>`
- `<onstorage>`
- `<onsubmit>`
- `<onsuspend>`
- `<onsyncrestored>`
- `<ontimeerror>`
- `<ontimeupdate>`
- `<ontoggle>`
- `<ontouchcancel>`
- `<ontouchend>`
- `<ontouchmove>`
- `<ontouchstart>`
- `<ontrackchange>`
- `<onundo>`
- `<onunload>`
- `<onurlflip>`
- `<onvolumechange>`
- `<onwaiting>`
- `<onwheel>`
- `<seeksegmenttime>`
- `<transitionend>`
{% enddetails %}