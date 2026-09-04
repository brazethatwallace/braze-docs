---
nav_title: トラブルシューティング
article_title: HTMLメールのトラブルシューティング
page_order: 9
description: "症状インデックスと標準的なトラブルシューティング手順を使用して、HTMLメールのレンダリングやエディターの問題を診断します。"
channel: email
---

# HTMLメールのトラブルシューティング {#troubleshoot-html-emails}

> このページでは、HTMLメールエディターやテスト送信に関するよくある問題を解決します。Inbox Visionや到達性については、[Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision)および[メール設定]({{site.baseurl}}/user_guide/channels/email/email_setup)を参照してください。

## まずはここから：症状を確認する {#start-here-match-your-symptom}

以下の表から該当する症状を見つけて、適切なセクションに移動してください。

| 症状 | 参照先 |
| --- | --- |
| テストメールのHTMLが正しく表示されない | [テストメールでHTMLが正しくレンダリングされない](#html-renders-incorrectly-in-test-emails) |
| Chromeでエディターが正しく動作しない | [拡張機能の競合](#extension-conflicts) |
| メールクライアントによって表示が異なる | [メールのレンダリング](#email-rendering) |
| メールにLiquidコードや壊れたリンクが表示される | [LiquidテンプレートのHTML不均衡](#unbalanced-html-in-liquid-templates) |
| Inbox Visionのプレビューが送信済みメールと一致しない | [CSSインライン化](#css-inlining) |
| テストメールで画像の後に余白や線が表示される | [画像下の余白](#white-space-under-images) |
| クリック分析にクエリパラメーターが含まれない | [リンククリック分析の制限事項](#link-click-analytics-limitations) |
| 上付き文字により行間が不均一になる | [上付き文字の行の高さの問題](#superscript-line-height-issues) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTMLメールの症状" }

## 標準的な調査パス {#standard-investigation-path}

HTMLメールのレンダリングやエディターの動作が期待どおりでない場合は、このワークフローを使用してください。ステップ1から始めてください。

1. エディターまたは外部バリデーターでHTMLマークアップを検証します。
2. [テストメール]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages)を送信し、どのメールクライアントまたはブラウザーで問題が発生するかを確認します。
3. [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision)でプレビューし、クライアント間のレンダリングを比較します。
4. エディター自体が正常に動作しない場合は、[ブラウザー拡張機能の競合](#extension-conflicts)を除外します。
5. 問題が解消されない場合は、Inbox Visionのスクリーンショットと影響を受けたクライアントの情報を添えて、[サポートチケット]({{site.baseurl}}/user_guide/administer/personal/braze_support)を提出してください。

## テストメールでHTMLが正しくレンダリングされない {#html-renders-incorrectly-in-test-emails}

### 症状 {#symptom}

[テストメール]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages)の表示がエディターでの見た目と一致しません。

まずHTMLの設定を確認し、次に[拡張機能の競合](#extension-conflicts)、[メールのレンダリング](#email-rendering)、[CSSインライン化](#css-inlining)、[画像下の余白](#white-space-under-images)を確認してください。

### 拡張機能の競合 {#extension-conflicts}

特定のブラウザ拡張機能がメールエディターで問題を引き起こすことがあります。例えば、Google Chromeで使用する[Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en)がその一例です。これらの拡張機能を使用している場合は、以下のいずれかを行ってください。

- Grammarlyがブラウザ拡張機能としてインストールされていないブラウザでBrazeメールを編集する
- Brazeアカウントマネージャーに連絡して、メールエディターをHTMLのみまたはプレーンテキストに切り替えるよう依頼する

プレーンテキストビューでは`WYSIWYG`（見たままが得られる）エディターが削除されるため、このリクエストを行う前に、すべてのチームメンバーがHTMLに慣れていることを確認してください。

### メールのレンダリング {#email-rendering}

メールはブラウザやメールクライアントによってレンダリングが異なるため、問題が発生しているブラウザやメールクライアントを記録しておいてください。

- [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision)を使用してメールをプレビューし、さまざまなブラウザやメールクライアントでメールがどのように表示されるかを確認してください。
- 問題を引き起こしているブラウザやメールクライアントを特定したら、開発者チームにHTMLを修正し、それらのブラウザやメールクライアントに対応するための編集が必要であることを伝えてください。
- 問題が[代替テキストの表示方法]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text)に関するものである場合、この動作はBrazeではなく受信者のメールクライアントによって制御されることに留意してください。

### LiquidテンプレートでのHTMLの不均衡 {#unbalanced-html-in-liquid-templates}

#### 症状

一部のユーザーが、Liquidコードがメッセージ内に表示されたり、リンクが壊れたり、間隔が正しくなかったりする、変更されたバージョンのメールを受信します。

Brazeは送信前にメールを準備するために内部HTMLパーサーを使用しています。このパーサーは、プリヘッダーの生成、トラッキングピクセルの配置、リンクテンプレート、リンクエイリアスなどの機能をサポートしています。HTMLタグが対応するLiquidロジックブロックやContent Blocks内でバランスが取れていない場合、パーサーが基盤となるHTMLを予期しない方法で変更することがあります。これにより、以下のような問題が発生する可能性があります。

- 一部のメールクライアントでLiquidレンダリングによる改行が表示される
- メール本文に追加された`<p>`タグによる不自然な間隔
- `<head>`タグのコンテンツがプリヘッダーに移動する
- モバイルオペレーティングシステム間でのレンダリングの不一致
- AMPメール本文からAMP固有のコードが削除され、バリデーションエラーが発生する
- 多数の異なるクエリパラメーターやメディアクエリが使用されている場合にリンクが壊れる

#### Liquidブロック内でHTMLのバランスを取る {#balance-html-within-liquid-blocks}

すべてのHTMLタグが、対応するLiquidロジックブロックまたはContent Blocks内で開閉されるようにしてください。これにより、内部パーサーがHTMLを無効と解釈して変更することを防ぎます。

#### 不均衡な例 {#unbalanced-example}

{% raw %}
```liquid
<img src={% if ${language} == 'en' %}"https://example.com/images/banner-en.png" style="width: 100%"{% elsif ${language} == 'de' %}"https://example.com/images/banner-de.png"{% else %}"https://example.com/images/banner-default.png" {% endif %} />
```
{% endraw %}

この例では、開始の`<img`タグがLiquidブロックの外側で始まり、タグの属性のさまざまな部分がLiquid条件文に分割されています。この構造はパーサーを混乱させ、タグの開始位置と終了位置を判断できなくなります。

#### バランスの取れた例 {#balanced-example}

{% raw %}
```liquid
{% if ${language} == 'en' %}
  <img src="https://example.com/images/banner-en.png" style="width: 100%;" />
{% elsif ${language} == 'de' %}
  <img src="https://example.com/images/banner-de.png" style="width: 100%;" />
{% else %}
  <img src="https://example.com/images/banner-default.png" style="width: 100%;" />
{% endif %}
```
{% endraw %}

バランスの取れたバージョンでは、各Liquidブランチに完全で自己完結した`<img>`タグが含まれています。このアプローチにより、パーサーが各ブランチを正しく処理できます。

#### その他の修正方法 {#additional-fixes}

メディアクエリや多数のクエリパラメーターでレンダリングの問題が発生している場合は、メール設定でCSSインライン化をオフにしてみてください。これにより、HTMLパーサーと複雑なCSSルール間の競合を解決できる場合があります。

### CSSインライン化 {#css-inlining}

Inbox Visionのプレビューが、Brazeで送信されたものと一致しない場合があります。これは、Brazeと他のツールで実行されるCSSインライン化の違いが原因である可能性があります。これが原因と思われる場合は、CSSインライン化をオフにしてください。

### 画像下の余白 {#white-space-under-images}

#### 症状

テストメールで画像の後に余白や線が表示されます。

テストメールで画像の下に余白や線が表示される場合、これは通常、メールクライアントがインラインレベル要素をレンダリングする方法が原因です。画像はデフォルトでインラインレベルであり、ベースラインに揃えられます。これにより、ブラウザがディセンダー（「g」や「y」のようにベースラインより下に伸びる文字の部分）に対応できるようになりますが、余白として表示される小さな隙間が生じます。

これを修正するには、画像のCSSに`display: block;`を追加します。

```html
<style>
  img {
    display: block;
  }
</style>
```

または、特定の画像にスタイルを直接適用することもできます。

```html
<img src="https://example.com/image.jpg" style="display: block;" alt="Image description" />
```

## リンククリック分析の制限事項 {#link-click-analytics-limitations}

### 症状

一意のクエリパラメーターが多数含まれるメールのクリック分析が、期待どおりの結果と一致しません。最初の100個の一意のリンクを超えると、パラメーターが除去されたURLに対して集計されたクリック数が表示されることがあります。

### リンククリックトラッキングの仕組み {#how-link-click-tracking-works}

Brazeは、パラメーター付きURL（クエリパラメーターあり）とパラメーターが除去されたベースURLの両方でクリックをトラッキングします。メールキャンペーンまたはキャンバスでクリックされた最初の100個の一意のパラメーター付きリンクについて、Brazeは以下の両方のデータを収集してレポートします。

- 完全なパラメーター付きURL（例：`https://example.com?user_id=12345`）
- パラメーターが除去されたベースURL（例：`https://example.com`）

最初の100個の一意のパラメーター付きリンクがクリックされた後、Brazeはパラメーターが除去されたベースURLのクリック数のみを増加させます。これは以下を意味します。

- クリック分析は、個々のクエリパラメーターの組み合わせではなく、ベースドメインとパスで集計されます
- リンクパスに基づいて有意義なエンゲージメントをトラッキングすることは引き続き可能です
- 個々のユーザーレベルのクリックトラッキングは引き続き正常に機能します

この動作により、全体的なリンクエンゲージメントパターンをキャプチャしながら、数千の一意のクエリパラメーターの組み合わせによって分析が肥大化するのを防ぎます。

### キャンペーンへの影響 {#what-this-means-for-your-campaigns}

外部プラットフォームでユーザー固有の行動をトラッキングするために一意のクエリパラメーターに依存している場合（例：`https://example.com?user_id=USER_ID`）、Brazeのクリック分析ではクリックされた最初の100個の一意のリンクについてのみそれらのパラメーターが保持されることに注意してください。そのしきい値を超えた後もクリックは分析に記録されますが、パラメーターが除去されたURLに帰属されます。

ユーザーレベルのクリックデータは、クリックされた一意のパラメーター付きリンクの数に関係なく、[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)または[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)を通じて引き続き利用可能です。

### 上付き文字の行の高さの問題 {#superscript-line-height-issues}

#### 症状

上付き文字を含むテキストで、行間が意図したよりも近くなったり離れたりして、一貫性のない行間隔で表示されます。これはメールクライアント全般で見られる一般的なレンダリングの問題であり、Braze固有のものではありません。

メールで上付き文字を使用すると、メールクライアントごとに上付き文字テキストの処理方法が異なるため、予期しない行の高さの動作が発生する可能性があります。

#### 解決方法 {#resolution}

HTMLエディターを使用して、上付き文字と周囲の要素のスタイルを制御します。

行の高さを明示的に定義するには、インラインCSSを追加してテキストの`line-height`を設定します。

```html
<p style="line-height: 1.5;">Example text with superscript<sup style="line-height: inherit;">1</sup></p>
```

垂直方向の配置を調整するには、`vertical-align`プロパティを使用して、行の高さを乱さずに上付き文字を配置します。

```html
<sup style="vertical-align: top; font-size: smaller;">1</sup>
```

上付き文字が引き続き問題を引き起こす場合は、より細かい制御のために`<sup>`の代わりに`<span>`を使用します。

```html
<span style="font-size: smaller; vertical-align: top;">1</span>
```
