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
- モバイルとデスクトップの両方で1つのメールテンプレートを使用する場合は、幅を500ピクセル未満に保ってください。
- 画像は5&nbsp;MB未満にする必要があります。互換性を最大限に高めるため、PNG、JPEG、またはGIFの使用を推奨します。SVGとWebPは、多くの主要なメールクライアントがまだサポートしていないため避けてください。
- 画像に高さと幅を設定しないでください。劣化したメールで不要な余白が生じる可能性があります。
- ほとんどのメールクライアントが`div`タグの使用をサポートしていないため、使用しないでください。代わりに、ネストされたテーブルを使用してください。
- JavaScriptはどのメールサービスプロバイダー (ESP) でも動作しないため、使用を避けてください。
- メールテンプレートでCSS `position: absolute`や`position: relative`の使用は避けてください。ほとんどのメールクライアントはCSSのポジショニングをサポートしていないため、Brazeのプレビューと配信されたメールの間でレイアウトに差異が生じます。レイヤードや重なり合う効果を実現するには、テーブルベースのレイアウトを使用してください。
- BrazeはグローバルなCDNを使用してすべてのメール画像をホストすることで、読み込み時間を改善しています。
- モバイルでは画像列の幅が狭くなりますが（各列約100px）、複数画像の行でも収まります（例：4つの画像 ≈ 4つの使用可能な列）。

## 代替テキスト {#alternative-text}

スパムフィルターはメッセージのHTML版とプレーンテキスト版の両方を監視するため、プレーンテキストの代替を活用することはスパムスコアを下げる優れた方法です。さらに、代替テキスト `(alt="")` は、ユーザーのメールプロバイダーによってフィルタリングされた可能性のあるメール本文に含まれる画像を補完したり、場合によっては画像の代わりとして機能したりします。スクリーンリーダーは画像を説明するために代替テキストを読み上げるため、平易な言葉で画像に関する重要な情報を提供する機会となります。

代替テキストの表示方法は、Brazeではなく受信者のメールクライアントによって制御されます。Gmail、Outlook、Apple Mailなどのクライアントにおけるこの動作の詳細については、[メールクライアントが代替テキストを表示する方法]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text)を参照してください。

{% alert note %}
代替テキストに引用符が含まれる場合は、ダブルクォート（`"`）ではなくシングルクォート（`'`）を使用してください。ダブルクォートを使用すると、HTMLが属性を途中で閉じてしまい、テキストが途切れる原因となります。例えば、`alt="Product 'Premium' Edition"` は正しく動作しますが、`alt="Product "Premium" Edition"` は途中で切れてしまいます。
{% endalert %}

## メール検証 {#email-validation}

{% alert important %}
検証は、ダッシュボードのメールアドレス、エンドユーザー（顧客）のメールアドレス、およびメールメッセージの差出人アドレスと返信先アドレスに対して使用されます。
{% endalert %}

メール検証は、ユーザーのメールアドレスが更新された場合、またはAPI、CSVアップロード、SDK経由でBrazeにインポートされた場合、あるいはダッシュボードで変更された場合に行われます。メールアドレスに空白を含めることはできません。APIを使用して送信した場合、空白があると`400`エラーが発生する可能性があります。

Brazeサーバーを通じてターゲットとなるメールアドレスは、[RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822)標準に従って検証される必要があります。Brazeは特定の文字を受け付けず、それらを無効として認識します。メールがバウンスされた場合、Brazeはそのメールを無効としてマークし、購読ステータスは変更されません。

許可されていない文字やメール検証ルールの詳細については、[メール検証]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation#how-it-works)を参照してください。

## 差出人アドレスと返信先アドレス {#from-and-reply-to-addresses}

差出人アドレスを設定する際は、差出人メールドメインが送信ドメイン（`marketing.yourdomain.com` など）と一致していることを確認してください。一致していない場合、SPFとDKIMの整合性が取れなくなる可能性があります。すべての返信先メールアドレスには、ルートドメインを設定できます。

{% alert note %}
差出人アドレスではUnicodeエンコーディングはサポートされていません。
{% endalert %}


### 送信ドメインと受信メール {#sending-domains-and-inbound-mail}

Brazeはメールの送信のみを行います。送信ドメインとサブドメインは配信性（SPF、DKIM、および関連するDNSレコード）のために設定されますが、受信メールボックスとしては機能しません。

送信サブドメインに送られた返信を、Brazeを通じて個人の受信トレイに転送することはできません。ユーザーの返信を受信するには、受信メールボックスを持つ自社管理ドメインに別の返信先アドレスを設定してください。[差出人アドレスと返信先アドレス](#from-and-reply-to-addresses)を参照してください。

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
- プレビューでカスタムフォントが正しく読み込まれることを確認します
- 行と列のパディングを確認します
- テーブルベースのレイアウトを優先し、エディターの幅内に収めます

エディター外からHTMLを取り込むContent Blocksもレイアウトを崩す可能性があります。

## メールURLのUTMパラメーター {#utm-parameters-in-email-urls}

UTMパラメーターは分析のためにURLにタグを付けます。Liquidとカスタム属性を使用して構築できます。

- 最終的なURLにはクエスチョンマーク`?`を1つだけ使用してください（追加の`?`はリクエストを壊す可能性があります）。
- 値にスペースや特殊文字を使用しないでください（`_`または`-`を使用してください）。
- 分析ツールがUTMを取り込めることを確認してください。Liquidの`capture`ブロック内の末尾のスペースをトリミングしてください。UTMは大文字と小文字を区別します。

### HTMLの詳細を確認する {#check-html-details}

一部のHTMLタグと属性は、ブラウザで悪意のあるコードが実行される可能性があるため、許可されていないことに注意してください。

メールで許可されていないHTMLタグと属性について、以下のリストをご確認ください：
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

## メール重複のトラブルシューティング {#troubleshooting-duplicate-emails}

ユーザーからメールが重複して届くという報告を受けた場合、以下のシナリオを参考に原因を特定できます。

### キャンペーンまたはキャンバス作成時の設定エラー {#configuration-error-at-campaign-or-canvas-creation}

ユーザーは同じメールを2回受信しているのではなく、同じ件名で2通の別々のメールを受信している可能性があります。キャンペーンやキャンバスが複製された場合、画像や件名などの基本的なメール設定の詳細を見落としがちです。

調査するには:

1. ユーザープロファイルを確認し、そのユーザーが受信した各キャンバスとキャンペーンを確認します。
2. 変更ログを確認し、キャンペーンやキャンバスが配信後に変更されたかどうかを確認します。ユーザーが受信した時点で、キャンペーンやキャンバスがオリジナルと同じ件名だった可能性があります。

### キャンペーンが複数回送信された {#campaign-sent-multiple-times}

送信メッセージ数がオーディエンス内のユーザー数を大幅に上回っている場合、キャンペーンが複数回配信された可能性があります。

Brazeにおけるメールアドレスの重複処理と重複排除の詳細については、[メールFAQ]({{site.baseurl}}/user_guide/channels/email/faq#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address)を参照してください。