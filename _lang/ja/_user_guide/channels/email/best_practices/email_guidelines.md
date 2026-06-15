---
nav_title: "メールガイドライン"
article_title: "メールガイドライン"
page_order: 1
page_type: reference
description: "この記事では、さまざまなユースケースやトピックに対応するメールキャンペーンを作成する際に覚えておくべき一般的なヒントやコツについて説明します。"
channel: email

---

# メールガイドライン {#email-guidelines}

> メールキャンペーンを作成する際には、さまざまなユーザーやメールサービスプロバイダー (ESP) でメールメッセージがどのように受信されるかを念頭に置くことが重要です。

## 一般 {#general}

コンテンツを作成する際に覚えておくべきヒントをいくつかご紹介します。

- メールのフォーマットには、インラインスタイルシートとしてCSSを使用してください。
- モバイルとデスクトップの両方で1つのメールテンプレートを使用するには、幅を500ピクセル未満に抑えてください。
- 画像は5&nbsp;MB未満にする必要があります。最大限の互換性を確保するために、PNG、JPEG、またはGIFの使用を推奨します。SVGやWebPは、多くの主要なメールクライアントがまだサポートしていないため、避けてください。
- 画像に高さと幅を設定しないでください。劣化したメールで不要な余白が生じる可能性があります。
- `div` タグは使用しないでください。ほとんどのメールクライアントがその使用をサポートしていません。代わりに、ネストされたテーブルを使用してください。
- JavaScriptはどのESPでも動作しないため、使用を避けてください。
- Brazeはグローバルなを使用してすべてのメール画像をホストすることで、読み込み時間を改善しています。
- モバイルでは、画像カラムは狭い（各約100px）ため、複数画像の行でも収まります（例：4つの画像 ≈ 4つの使用可能なカラム）。

## 代替テキスト {#alternative-text}

スパムフィルターはHTMLとプレーンテキストの両方のバージョンを監視するため、プレーンテキストの代替を活用することはスパムスコアを下げる優れた方法です。さらに、代替テキスト `(alt="")` は、ユーザーのメールプロバイダーによってフィルタリングされた可能性のあるメール本文の画像を補完したり、場合によっては代替したりすることができます。スクリーンリーダーは画像を説明するために代替テキストを読み上げるため、これは平易な言葉で画像に関する重要な情報を提供する機会です。

## メールバリデーション {#email-validation}

{% alert important %}
バリデーションは、ダッシュボードのメールアドレス、エンドユーザー（顧客）のメールアドレス、およびメールメッセージの差出人アドレスと返信先アドレスに対して使用されます。
{% endalert %}

メールバリデーションは、ユーザーのメールアドレスが更新されたとき、またはAPI、CSVアップロード、SDKによってBrazeにインポートされたとき、あるいはダッシュボードで変更されたときに行われます。メールアドレスには空白を含めることはできず、APIを使用して送信した場合、空白があると `400` エラーが発生する可能性があります。

Brazeサーバー経由でターゲットされるメールアドレスは、[RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822) 標準に従ってバリデーションされる必要があります。Brazeは特定の文字を受け付けず、無効として認識します。メールがバウンスした場合、Brazeはそのメールを無効としてマークし、サブスクリプションステータスは変更されません。

許可されていない文字やメールバリデーションルールについては、[メールバリデーション]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation/#how-it-works)を参照してください。

## 差出人アドレスと返信先アドレス {#from-and-reply-to-addresses}

「差出人」アドレスを設定する際は、「差出人」メールドメインが送信ドメインと一致していることを確認してください（例：`marketing.yourdomain.com`）。一致しない場合、SPFとDKIMの不整合が発生する可能性があります。すべての返信先メールはルートドメインに設定できます。

{% alert note %}
「差出人」アドレスではUnicodeエンコーディングはサポートされていません。
{% endalert %}

## メールの添付ファイル {#attachments}

メールメッセージに添付ファイルを追加する際は、以下の配信性に関するベストプラクティスに従ってください。

- スパムフィルターは添付ファイルをスキャンし、メッセージにフラグを立てる場合があります
- メールプロバイダーは添付ファイルを含むメッセージの受信に時間がかかることがあります
- 1対1のメッセージ以外では、添付ファイルがあると受信トレイでメッセージがリスクのあるものに見える場合があります
- 各添付ファイルは2&nbsp;MB未満に抑えてください
- 機密情報を添付ファイルとして送信しないでください。代わりに、ユーザーをセキュアなポータルに誘導して閲覧してもらいましょう

## レイアウト（ドラッグアンドドロップおよびカスタムHTML） {#layout-drag-and-drop-and-custom-html}

Brazeが生成したHTML/CSSがカスタムHTMLと競合すると、レイアウトが崩れることがあります。この場合は、以下を行ってください。

- まずカスタムHTML/CSSを削除します
- プレビューでカスタムフォントが正しく読み込まれることを確認します
- 行とカラムのパディングを確認します
- テーブルベースのレイアウトを優先し、エディターの幅内に収めてください。

エディター外からHTMLを取り込むContent Blocksもレイアウトを崩す可能性があります。

## メールURLでのUTMパラメーター {#utm-parameters-in-email-urls}

UTMパラメーターは分析のためにURLにタグを付けます。Liquidやカスタム属性を使用して構築できます。

- 最終URLにはクエスチョンマーク `?` を1つだけ使用してください（追加の `?` はリクエストを壊す可能性があります）。
- 値にスペースや特殊文字を使用しないでください（`_` または `-` を使用してください）。
- 分析ツールがUTMを取り込むことを確認してください。Liquidの `capture` ブロック内の末尾のスペースをトリミングしてください。UTMは大文字と小文字を区別します。

### HTMLの詳細確認 {#check-html-details}

一部のHTMLタグや属性は、ブラウザで悪意のあるコードが実行される可能性があるため、許可されていません。

メールで許可されていないHTMLタグと属性については、以下のリストを確認してください。
{% details 許可されていないHTMLタグを展開 %}
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

{% details 許可されていないHTML属性を展開 %}
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