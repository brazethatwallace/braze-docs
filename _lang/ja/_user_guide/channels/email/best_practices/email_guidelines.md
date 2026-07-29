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

## 全般 {#general}

コンテンツを作成する際に覚えておくべきヒントをいくつか紹介します。

- メールのフォーマットには、インラインスタイルシートをCSSとして使用してください。
- モバイルとデスクトップの両方で1つのメールテンプレートを使用するには、幅を500ピクセル未満に保ってください。
- 画像は5&nbsp;MB未満にする必要があります。互換性を最大限に高めるために、PNG、JPEG、またはGIFの使用を推奨します。SVGやWebPは、多くの主要なメールクライアントがまだサポートしていないため、避けてください。
- 画像に高さや幅を設定しないでください。劣化したメールで不要な余白が生じる可能性があります。
- ほとんどのメールクライアントが`div`タグの使用をサポートしていないため、`div`タグは使用しないでください。代わりに、ネストされたテーブルを使用してください。
- JavaScriptはどのメールサービスプロバイダー (ESP) でも動作しないため、使用を避けてください。
- メールテンプレートでは、CSS `position: absolute` や `position: relative` の使用を避けてください。ほとんどのメールクライアントはCSSポジショニングをサポートしておらず、Brazeのプレビューと配信されたメールの間でレイアウトの不一致が生じます。レイヤーや重なりの効果を実現するには、テーブルベースのレイアウトを使用してください。
- Brazeはグローバルなコンテンツ配信ネットワーク（CDN）を使用してすべてのメール画像をホストすることで、読み込み時間を改善しています。
- モバイルでは、画像カラムは狭く（各約100px）なりますが、複数画像の行は収まります（例：4つの画像 ≈ 4つの使用可能なカラム）。

## 代替テキスト {#alternative-text}

スパムフィルターはメッセージのHTMLバージョンとプレーンテキストバージョンの両方を監視するため、プレーンテキストの代替を活用することはスパムスコアを下げる優れた方法です。さらに、代替テキスト `(alt="")` は、ユーザーのメールプロバイダーによってフィルタリングされた可能性のあるメール本文内の画像を補完し、場合によっては画像の代わりとして機能します。スクリーンリーダーは画像を説明するために代替テキストを読み上げるため、わかりやすい言葉で画像に関する重要な情報を伝える機会となります。

{% alert note %}
代替テキストに引用符が含まれる場合は、ダブルクォート (`"`) ではなくシングルクォート (`'`) を使用してください。ダブルクォートを使用すると、HTMLが属性を途中で閉じてしまい、テキストが切り捨てられる可能性があります。たとえば、`alt="Product 'Premium' Edition"` は正しく動作しますが、`alt="Product "Premium" Edition"` は切り捨てられます。
{% endalert %}

## メールのバリデーション {#email-validation}

{% alert important %}
バリデーションは、ダッシュボードのメールアドレス、エンドユーザー（顧客）のメールアドレス、およびメールメッセージの差出人アドレスと返信先アドレスに対して使用されます。
{% endalert %}

メールのバリデーションは、ユーザーのメールアドレスが更新されたとき、またはAPI、CSVアップロード、SDK経由でBrazeにインポートされたとき、もしくはダッシュボードで変更されたときに行われます。メールアドレスに空白を含めることはできません。APIを使用して送信した場合、空白があると`400`エラーが発生する可能性があります。

Brazeサーバーを通じて送信されるメールアドレスは、[RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822)標準に従ってバリデーションされる必要があります。Brazeは特定の文字を受け付けず、無効として認識します。メールがバウンスされた場合、Brazeはそのメールを無効としてマークしますが、購読ステータスは変更されません。

許可されていない文字やメールバリデーションルールについては、[メールのバリデーション]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation#how-it-works)を参照してください。

## 差出人アドレスと返信先アドレス {#from-and-reply-to-addresses}

差出人アドレスを設定する際は、差出人メールドメインが送信ドメイン（`marketing.yourdomain.com` など）と一致していることを確認してください。一致していない場合、SPFとDKIMの整合性が失われる可能性があります。すべての返信先メールアドレスは、ルートドメインに設定できます。

{% alert note %}
差出人アドレスではUnicodeエンコーディングはサポートされていません。
{% endalert %}

## メールの添付ファイル {#attachments}

メールメッセージに添付ファイルを追加する際は、以下の配信性に関するベストプラクティスに従ってください。

- スパムフィルターは添付ファイルをスキャンし、メッセージにフラグを立てる場合があります
- メールプロバイダーは添付ファイルを含むメッセージの受信に時間がかかることがあります
- 1対1のメッセージ以外では、添付ファイルがあると受信トレイでメッセージがリスクのあるものに見える場合があります
- 各添付ファイルは2&nbsp;MB未満に抑えてください
- 機密情報を添付ファイルとして送信しないでください。代わりに、ユーザーをセキュアなポータルに誘導して閲覧してもらいましょう

## レイアウト（ドラッグ＆ドロップとカスタムHTML） {#layout-drag-and-drop-and-custom-html}

Brazeが生成したHTML/CSSがカスタムHTMLと競合すると、レイアウトが崩れることがあります。この場合は、以下を行ってください。

- まずカスタムHTML/CSSを削除します
- カスタムフォントがプレビューで正しく読み込まれることを確認します
- 行と列のパディングを確認します
- テーブルベースのレイアウトを使用し、エディターの幅内に収めるようにします

エディター外からHTMLを取り込むContent Blocksも、レイアウトを崩す原因になることがあります。

## メールURLのUTMパラメーター {#utm-parameters-in-email-urls}

UTMパラメーターは分析用にURLをタグ付けします。Liquidやカスタム属性を使用して構築できます。

- 最終URLには疑問符 `?` を1つだけ使用してください（追加の `?` はリクエストを壊す可能性があります）。
- 値にスペースや特殊文字を使用しないでください（`_` または `-` を使用してください）。
- 分析ツールがUTMを取り込むことを確認してください。Liquidの `capture` ブロック内の末尾のスペースを削除してください。UTMは大文字と小文字を区別します。

### HTMLの詳細を確認する {#check-html-details}

一部のHTMLタグや属性は、ブラウザで悪意のあるコードが実行される可能性があるため、許可されていないことに注意してください。

メールで許可されていないHTMLタグと属性については、以下のリストを確認してください。
{% details 許可されていないHTMLタグを展開 %}
- `<!doctype>`
- `<applet>`
- `<bgsound>`
- `<embed>`
- `<frameset>`
- `iframe`
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