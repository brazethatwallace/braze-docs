---
nav_title: リンクエイリアス
article_title: リンクエイリアス
alias: /link_aliasing/
page_order: 3
description: "この記事では、リンクエイリアスの仕組みと、リンクがどのように表示されるかの例について説明します。"
channel:
  - email

---

# [![Braze Learningコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/link-aliasing){: style="float:right;width:120px;border:0;" class="noimgborder"}リンクエイリアス {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomlink-aliasing-stylefloatrightwidth120pxborder0-classnoimgborderlink-aliasing}

> リンクエイリアスを使用して、Brazeから送信されるメールメッセージ内のリンクを識別するための、認識しやすいユーザー生成名を作成できます。これらのリンクは、セグメンテーションのリターゲティング、アクションベースのトリガー、およびリンク分析に利用できます。

## リンクエイリアスについて {#about-link-aliasing}

リンクエイリアスを使用すると、メールで送信されるリンクを識別・追跡するためのユーザー生成名を作成できます。これにより、完全なリンクを参照することなく、認識しやすいリンクエイリアスをメールで効率的に使用して、エンゲージメントを追跡し、キャンペーンのパフォーマンスを分析できます。

リンクエイリアスを使用すると、以下のことが可能です。

- **特定のリンクをクリックしたユーザーをリターゲティングする:** リンクをクリックしたユーザーを特定してターゲティングします。
- **アクションベースのトリガーを作成する:** ユーザーがリンクをクリックしたときにメールを送信します。
- **指標を分析する:** リンクAとリンクBのクリック数を比較します。

### 仕組み {#how-it-works}

Brazeは、すべてのリンクURLに`lid`（リンク識別子とも呼ばれる）という追加パラメーターを付加することで、メール内のリンクを一意に識別します。この`lid`値により、URLの他のパラメーターが異なる場合でも、Brazeはリンクに対するユーザーインタラクションを追跡、監視、集計できます。これにより、メールキャンペーンのコンテンツに対するユーザーのエンゲージメントに関するインサイトが得られます。

リンク識別子は、メールキャンペーン、メールメッセージを含むキャンバス、またはContent Blocksが複製された場合にも更新されます。

## リンクエイリアスの作成 {#creating-a-link-alias}

{% alert important %}
**リンク管理**は、Brazeがアカウントのリンク管理を有効にすると、キャンペーンまたはキャンバスのメールコンポーザーに表示されます。**リンクエイリアス**を作成・編集するには、リンクエイリアスをオンにする必要があります。**リンク管理**が表示されない場合は、アカウントマネージャーに連絡してリンクエイリアスをオンにしてください。
{% endalert %}

リンクエイリアスを作成するには、キャンペーンまたはキャンバスコンポーネントでメール本文を開き、**コンテンツ**エリアから**リンク管理**を開きます。ドラッグ＆ドロップエディターとHTMLエディターは同じサイドバーレイアウトを使用します。

### ドラッグ＆ドロップエディター {#drag-and-drop-editor}

1. **メール本文を編集**を選択して、ドラッグ＆ドロップコンポーザーを開きます。
2. コンポーザーのサイドバーで、**コンテンツ**（**送信設定**および**プレビューとテスト**の横）を選択します。このレイアウトの詳細については、[ドラッグ＆ドロップでメールを作成する]({{site.baseurl}}/user_guide/channels/email/drag_and_drop)を参照してください。
3. **コンテンツ**サブメニューで、**リンク管理**（**デザインとビルド**の下に表示）を選択します。サブメニューが折りたたまれている場合は、サイドバーの矢印コントロールを使用して展開します。

### HTMLエディター {#html-editor}

1. コンポーザーでメール本文に移動します。
2. コンポーザーのサイドバーで、**コンテンツ**を選択します。
3. **コンテンツ**サブメニューで、**デザインとビルド**の下にある**リンク管理**を選択します。

**リンク管理**では以下の操作を行います。

1. Brazeが各リンクに対して一意のデフォルトリンクエイリアスを自動的に生成します。
2. エイリアスに名前を付けます。エイリアスは、メールキャンペーンバリアントまたはキャンバスコンポーネントごとに一意の名前を付ける必要があります。

レポートやセグメンテーションで特定のリンクを参照するために使用するエイリアスを設定することもできます。

![4つのリンクエイリアスが表示されたリンク管理ページ。]({% image_buster /assets/img/link_aliasing_composer.png %})

{% alert note %}
リンクエイリアスは、クエリパラメーターを安全に付加できるHTMLアンカータグ内の`href`属性でのみサポートされています。Brazeが`lid`値を簡単に付加できるように、リンクの末尾に疑問符（?）を含めることがベストプラクティスです。`lid`値を付加しないと、BrazeはリンクエイリアスのためにそのURLを認識しません。
{% endalert %}

{% alert important %}
ドラッグ＆ドロップエディターでは、リンクエイリアスが**リンク管理**タブに表示されるためには、URL内のハッシュ記号（`#`）の前に疑問符（`?`）を含める必要があります。
{% endalert %}

## リンクエイリアスの管理 {#managing-link-aliases}

追跡されているすべてのリンクエイリアスを表示するには、以下の手順に従います。

1. **設定** > **ワークスペース設定**の**メール設定**に移動します。
2. **リンクエイリアス設定**タブを選択します。

ここでは、リンクエイリアスの並べ替え、検索、およびトラッキングのオン/オフを切り替えることができます。

![さまざまなキャンペーンに関連付けられたアクティブおよび非アクティブなリンクエイリアスが表示された追跡リンクエイリアスページ。]({% image_buster /assets/img/tracked_aliases.png %})

{% alert tip %}
[キャンペーンのリンクエイリアス一覧]({{site.baseurl}}/get_campaign_link_alias)および[キャンバスのリンクエイリアス一覧]({{site.baseurl}}/get_canvas_link_alias)エンドポイントを使用して、キャンペーンまたはメールのキャンバスコンポーネントの各メッセージバリアントに設定された`alias`を抽出できます。
{% endalert %}

Brazeでは、メール内のリンクを評価し、リンクテンプレートを追加し、セグメンテーションやレポートに適した命名規則を設定することを推奨しています。これにより、すべてのリンクを把握しやすくなります。

リンクエイリアスがオンになっている場合、メッセージ、Content Blocks、およびリンクテンプレートは変更されません。リンクテンプレートやContent Blocksを使用している既存のメッセージはそのままです。ただし、メッセージを更新すると、リンクエイリアスのマークアップがすべてのリンクに適用されるため、リンクを表示するにはリンクテンプレートを再適用する必要があります。

## リンクエイリアスによるリンクの更新方法 {#how-links-are-updated-with-link-aliasing}

以下の表は、メール本文内のリンク、リンクエイリアスの結果、および元のリンクがリンクエイリアスによってどのように更新されるかの説明の例を示しています。

### パーマリンク {#permalink}

**ロジック:** Brazeは疑問符（?）を挿入し、URLに最初のクエリパラメーターを追加します。

| メール本文内のリンク | エイリアス付きリンク |
|-----------------------|----------------------------------------|
| `https://www.braze.com` | `https://www.braze.com?lid=slfdldtqdhdk` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="パーマリンク" }

### 追加のクエリパラメーターを含むリンク {#link-with-more-query-parameters}

**ロジック:** Brazeは他のクエリパラメーターを検出し、URLの末尾に`lid=`を付加します。

| メール本文内のリンク | エイリアス付きリンク |
|---------------------------------------------------------------|--------------------------------------------------------------------------------|
| `https://www.braze.com?utm_campaign=retention&utm_source=email` | `https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="追加のクエリパラメーターを含むリンク" }

### HTMLリンク {#html-link}

**ロジック:** Brazeはリンクがすでに疑問符（?）を含むURLであることを認識し、疑問符の後に`lid`クエリパラメーターを付加します。

| メール本文内のリンク | エイリアス付きリンク |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTMLリンク" }

### アンカー付きリンク {#link-with-anchor}

**ロジック:** Brazeは、アンカー（#）が疑問符（?）の後に配置される標準的なURL構造を想定しています。Brazeは左から右に読み取るため、疑問符と`lid`値はアンカーの前に付加されます。

| メール本文内のリンク | エイリアス付きリンク |
|--------------------------------------------------|-------------------------------------------------------------------|
| `https://www.braze.com#bookmark1?utm_source=email` | `https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="アンカー付きリンク" }

### アンカーとキャプチャタグ付きリンク {#link-with-anchor-and-capture-tag}

**ロジック:** リンクエイリアスをアンカー（#）を含むURLで使用する場合、Brazeはアンカーがクエリパラメーターの後に配置されることを想定しています。つまり、適切なトラッキングのために`lid`値はアンカーの**前に**付加される必要があり、Brazeは左から右にURLを読み取るため、疑問符（?）と`lid`はアンカーの前に配置されます。

| メール本文内のリンク | エイリアス付きリンク |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| {%raw%}`<a href="https://www.braze.com/promotions#special-offer">Check out our special offer!</a>`{%endraw%}  | {%raw%}`<a href="https://www.braze.com/promotions?lid={{link_alias}}#special-offer">Check out our special offer!</a>` {%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="アンカーとキャプチャタグ付きリンク" }

## リンクエイリアスのトラッキング {#tracking-link-aliases}

コンポーザーのサイドバーで、**コンテンツ** > **リンク管理**（**デザインとビルド**の下）を選択し、**追跡**するエイリアスを選択します。追跡されたエイリアスは、リンクエイリアスを参照するセグメンテーションフィルターで利用できます（[セグメンテーションフィルター](#segmentation-filters)を参照）。また、ユーザーがメール内のリンクエイリアスをクリックしたときに、アクションベースのメッセージを送信したり、キャンバス内でユーザーを移動させたりすることもできます（[アクションベースのフィルター](#action-based-filters)を参照）。**追跡**設定は、そのリンクのクリックがメールパフォーマンスレポートでカウントされるかどうかには影響しません。

{% alert tip %}
リンクのエンゲージメント指標を追跡するには、リンクがHTTPまたはHTTPSで始まることを確認してください。特定のリンクのクリックトラッキングをオフにするには、[ユニバーサルリンクとアプリリンク]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#turning-off-click-tracking-on-a-link-to-link-basis)を参照してください。
{% endalert %}

Brazeでは無制限のリンクを追跡できますが、リターゲティングできるのはユーザーが最近開いたリンクのみです。ユーザープロファイルには、最近クリックされた100件のリンクが含まれます。たとえば、500件のリンクを追跡し、ユーザーがそのすべてをクリックした場合、最近クリックされた100件のリンクに基づいてリターゲティングまたはセグメントを作成できます。

![2つのリンクが選択されたリンク管理タブ。]({% image_buster /assets/img/link_management_dnd.png %})

{% alert note %}
Brazeは、プロファイルレベルで最後にクリックされた100件のリンクエイリアスのみを追跡します。
{% endalert %}

### アクションベースのフィルター {#action-based-filters}

ワークスペースでリンクエイリアスが有効になっている場合、任意のリンク（追跡または未追跡）をターゲットとするアクションベースのメッセージを作成したり、メールキャンペーンまたはキャンバスコンポーネント全体でエイリアスをクリックしたかどうかに基づいてユーザーをリターゲティングしたりできます。

![キャンバスコンポーネントでエイリアスをクリックしたユーザーまたはキャンペーンとインタラクションしたユーザーをターゲットにするアクションベースのオプション。]({% image_buster /assets/img/link_aliasing_action_based_filters.png %})

- キャンペーンがアーカイブされると、リンクトラッキングはオフになり、そのリンクエイリアスは別のフィルターで使用できなくなります。
- リンクのトラッキングがオンになっており、キャンペーンでクリックされた場合、リンクトラッキングがその後オフになっていても、そのメッセージ上の少なくとも1つのリンクがまだ追跡されている限り、セグメントフィルターで利用可能なオプションとしてキャンペーンを見つけることができます。
- 追跡されたリンクをフィルターとして選択できるのは、**キャンバスステップでエイリアスをクリック**フィルタードロップダウンを使用して、アクティブ（起動済み）のキャンバスにある場合のみです。リンクがキャンバスの下書きで追跡されている場合、追跡されたリンクをフィルターとして選択することはできません。

リンクを未追跡に設定するには、**設定** > **メール設定** > **リンクエイリアス設定**に移動します。

### セグメンテーションフィルター {#segmentation-filters}

Brazeでは、メールにリンクエイリアスがあり、ユーザーがそれをクリックすると、そのイベントがエイリアスとともにユーザーのプロファイルに記録されます。

「任意のキャンペーンまたはキャンバスステップでエイリアスをクリック」セグメンテーションフィルターを使用し、後でこのリンクエイリアスの名前を変更した場合、ユーザープロファイル内の以前のクリックデータは**更新されません**。つまり、以前のリンクエイリアスとして表示されたままです。そのため、新しいリンクエイリアスに基づいてユーザーをターゲティングしても、以前のリンクエイリアスのデータは含まれません。

「キャンペーンでエイリアスをクリック」または「キャンバスでエイリアスをクリック」セグメンテーションフィルターを使用すると、特定のキャンペーンまたはキャンバスで特定のエイリアスをクリックしたかどうかでユーザーをフィルタリングします。複数のユーザーが同じメールアドレスを共有しており、リンクエイリアスがクリックされた場合、そのメールアドレスを共有する他のすべてのユーザーのプロファイルも更新されます。これらのプロファイルは、クリックイベントだけでなく、配信イベントや開封イベントによっても更新されます。

以下のセグメンテーションフィルターは、イベントが処理された時点で追跡されるクリックイベントに適用されます。つまり、未追跡のリンクは既存のデータを削除せず、リンクの追跡はデータをバックフィルしません。詳細については、[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)を参照してください。

#### リンクの追跡解除 {#untracking-links}

リンクの追跡を解除しても、フィルターを使用している既存のセグメントが追跡解除されたエイリアスに再割り当てされることはありません。古いデータは、新しいデータに置き換えられるまでユーザープロファイルに残ります。

アーカイブされたメッセージ内のリンクは自動的に追跡解除されます。ただし、アーカイブされたメッセージがアーカイブ解除された場合、リンクを再度追跡する必要があります。リンクエイリアスが追跡されている場合、リンクレポートはトップレベルドメインや完全なURLではなく、エイリアスによってインデックスされます。

メールキャンペーン内のすべてのリンクとそれぞれの合計クリック数を表示するには、**メッセージ分析** > **メールのパフォーマンス** > **プレビューとヒートマップ**に移動し、**ヒートマップを表示**トグルを選択します。

![リンクエイリアスとその合計クリック数が表示された合計クリック数別リンクテーブルパネル。]({% image_buster /assets/img/link_alias_total_clicks.png %}){: style="max-width:60%;"}

### メールクリックイベント {#email-clicks-event}

エンゲージメントデータをCurrentsでエクスポートする場合、リンクエイリアスが有効になっていると、メールクリックイベントは若干異なります。リンクエイリアスがオンの場合、[メールクリックイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-clicks-events)に`link_id`と`link_alias`の2つの追加フィールドがあります。

```json
// Email Click: users.messages.email.Click
{
  "id": (string) unique ID of this event,
  "user_id": (string) Braze user ID of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) ID of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) ID of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) ID of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "url": (string) the URL that was clicked (Email Click events only),
  "user_agent": (string) description of the user's system and browser for the event (Email Click and Open events only),
  "ip_pool": (string) IP pool used for message sending,
  "link_id": (string) unique value generated by Braze for the URL,
  "link_alias": (string) alias name set when the message was sent
}
```

{% alert update %}
`dispatch_id`の動作は、キャンバスとキャンペーンで異なります。Brazeは、キャンバスステップ（エントリステップを除く。エントリステップはスケジュール可能）を、「スケジュール済み」であってもトリガーイベントとして扱います。キャンバスおよびキャンペーンにおける[`dispatch_id`の動作]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id)の詳細をご覧ください。

_2019年8月に更新。_
{% endalert %}

## Content Blocksでのリンクエイリアス {#link-aliasing-in-content-blocks}

新しいContent Blocksでは、該当する場合、各リンクに`lid={{placeholder}}`が付加されるようにリンクが変更されます。このプレースホルダー値は、メールメッセージバリアントに挿入されたときに解決されます。

Brazeがリンクエイリアスを有効にする前に作成された既存のContent Blocks内のリンクを変更するには、既存のContent Blocksを複製し、複製されたContent Blocks内のリンクを変更してください。

`lid`値のないContent Blocksが新しいメッセージに挿入された場合、そのContent Blocksのリンクはエイリアスで追跡されません。新しいContent Blocksが「古い」メッセージバリアントに挿入された場合、そのメッセージバリアントのリンクはリンクエイリアスによって認識されます。Content Blocksのリンクも認識されます。ただし、「古い」Content Blocksは「新しい」Content Blocksをネストできません。

{% alert tip %}
Content Blocksについては、新しいメッセージで使用するために既存のContent Blocksのコピーを作成することをBrazeは推奨しています。これは一括複製で行うことができ、リンクエイリアスが有効になっていないContent Blocksを新しいメッセージで参照するシナリオを防ぐことができます。
{% endalert %}

## Liquidで生成されるURLのリンクエイリアス {#link-aliasing-for-urls-generated-by-liquid}

HTMLの`assign`ステートメント、Content Blocksから取得した値、カスタム属性内のLiquidなど、Liquidで生成されるURLの場合、Brazeは`lid`クエリパラメーターを挿入する明確な場所を必要とします。ほとんどの場合、LiquidがURL内に残っていると、Brazeは`?`で新しいクエリ文字列を開始するか`&`で既存のクエリに結合するかを推測しません（デリミタを自分で追加しない限り）。

以下の手順に従ってください。

- URLにまだクエリ文字列が含まれて**いない**場合は、Liquidの後に`?`を追加します（例: `{{my_url}}?`）。
- URLに**すでに**`?`とクエリパラメーターが含まれている場合は、Liquidの後に`&`を追加します（例: `{{my_url}}&`）。

{% alert note %}
Liquidで生成されたURLで[リンクテンプレート]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template)を使用する場合、Brazeは、Liquid実行後にレンダリングされたURLがクエリセパレーターとして使用される`?`を正確に2つ含む場合、保守的にURLを正規化することがあります。2つ目の`?`は`&`に書き換えられ、BrazeはURLをできるだけ変更しないようにします。<br><br>Brazeはすべての重複`?`パターンを修正しようとするわけではなく、より複雑なURLの処理は意図的に制限されています。まずマークアップで正しい`?`または`&`を追加し、正規化は限定的なセーフガードとして扱ってください。整形されたURLの代替や、デリミタがない場合に**リンク管理**でリンクを認識させるための代替手段ではありません。
{% endalert %}

末尾に`?`または`&`（またはその他のサポートされている挿入ポイント）がない場合、リンクエイリアスはURLを認識せず、**リンク管理**にリストされず、リンクテンプレートも適用されません。

### URLフラグメント（`#`）とトラッキングパラメーター {#url-fragments-and-tracking-parameters}

フラグメント（`#`とそれ以降のすべて）は、通常のリンクリクエストではサーバーに送信されません。Brazeは`lid`をクエリ文字列に挿入しますが、これは`#`の前に配置される必要があります。`href`にLiquidと`#`フラグメントがあるが、`#`の前に`?`または`&`がない場合、Brazeは安全に`lid`を付加できないため、リンクが**リンク管理**に表示されなかったり、リンクエイリアスとして追跡されなかったりする場合があります。

これは、ドラッグ＆ドロップエディターでボタンURLがLiquidとハッシュベースのパターンを組み合わせている場合（たとえば、静的パスの後に`#`、その後にキーと値のペアが続く場合）に特によく見られます。その場合、`#`の直前に`?`を追加して、クエリ文字列（`lid`を含む）がフラグメントの前に解析されるようにします。

{% raw %}
```text
https://example.com/campaign/to/abc123?#user_id={{${user_id}}}&source=email
```
{% endraw %}

上記の例では、`#`の前の`?`により、Brazeが`lid`を付加するクエリセグメントが提供されます。これがないと、リンクが**リンク管理**に表示されない場合があります。

クエリパラメーターを付加する場所を特定できない場合、リンクエイリアスはこれらのURLを認識せず、リンクテンプレートも適用されません。動的URLで**LIDの割り当てに失敗しました**などのエラーが表示される場合は、`href`がこのセクションの例に示されている`?`または`&`パターンを使用していることを確認してください。

### ドラッグ＆ドロップエディターに関する注意事項 {#drag-and-drop-editor-considerations}

ドラッグ＆ドロップエディターでは、リンクを保持するフィールド（ボタンの**URL**など）は、Liquidが実行される前に基になる`href`を検証します。スペース、改行、およびURLセーフでないその他の文字は、Brazeがリンクテンプレートやリンクエイリアスパラメーターを付加する際に予期しない動作を引き起こす可能性があります。送信先に分岐Liquidが必要な場合は、HTMLブロックで`assign`を使用してURLを設定し（次のセクションを参照）、複雑なLiquidを直接そのフィールドに入力する代わりに、ドラッグ＆ドロップのURLフィールドで単一の変数を参照してください。

### Content Blocksの例 {#content-block-example}

{% raw %}
Content Blocksに`https://www.braze.com/{{custom_attribute.${offer_id}}}`のようなリンクが含まれており、末尾に`?`または`&`がない場合、Brazeは`lid`を付加する場所がわからないため、リンクは**リンク管理**に取得されません。Content Block内のURLの末尾に`?`または`&`を追加し（クエリ文字列がすでに存在するかどうかに応じて）、Content Blocksを保存すると、リンクが認識されるようになります。
{% endraw %}

### ユーザーごとにURLが異なる場合のレポート {#reporting-when-the-url-varies-per-user}

メッセージ内の各固有の`href`は、**リンク管理**およびエイリアスベースのレポートにおいて、**1つの**リンクIDと1つのリンクエイリアスにマッピングされます。リンクエイリアスが追跡されている場合、ダッシュボード内のメールレポートは、解決される可能性のあるすべてのURLではなく、エイリアスによってインデックスされます。

まず、Brazeで以下のアプローチを使用してください。

- **キャンペーンおよびキャンバスのメール分析:** [リンクの追跡解除](#untracking-links)で説明されているように、**メッセージ分析** > **メールのパフォーマンス** > **プレビューとヒートマップ**で**ヒートマップを表示**をオンにして、リンクごとの集計クリック数を確認します。
- **クエリビルダーでの受信者ごとのクリック:** キャンペーンまたはキャンバスの**メールURLクリック**[クエリビルダーテンプレート]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates#email-templates)を実行します。テンプレートは、サマリーカウント用に非パーソナライズされたリンクを表示します。CSVエクスポートには、クリックしたユーザーのユーザーID、クリックしたリンク、およびタイムスタンプが含まれます。（非パーソナライズされたURLは、サマリービュー用にLiquidタグを除去します。詳細はテンプレートの説明を参照してください。）
- **コンポーザーでのエイリアスレベルの内訳:** 各送信先（たとえば、各`offer_id`）を**リンク管理**およびエイリアスベースのレポートで個別の行として表示する必要がある場合は、ユーザーごとにパスが変わる1つのリンクではなく、個別の`href`値（したがって個別のエイリアス）を使用してください。たとえば、ブランチごとに異なるリンクを使用します。

ストリーミングエンゲージメントエクスポートも使用している場合、メールクリックイベントには**`url`**フィールドが含まれます。そのペイロードとリンクエイリアスの関係については、このページの[メールクリックイベント](#email-clicks-event)を参照してください。

### 例 {#example}

割り当てられたURLにクエリパラメーターがない場合は、このパターンを使用します。

{% raw %}
```liquid
{% assign link1 = "https://www.braze1.com" %}

<a href="{{link1}}?">Visit Braze</a>
```
{% endraw %}

割り当てられたURLにすでに`?`とクエリパラメーターが含まれている場合は、`?`の代わりにLiquidの後に`&`を追加します。

{% raw %}
```liquid
{% assign link_with_params = "https://www.braze1.com?campaign=test" %}

<a href="{{link_with_params}}&">Visit Braze</a>
```
{% endraw %}

### 条件付きLiquidを含むURL {#urls-with-conditional-liquid}

条件付きLiquidタグが`href`内で使用されている場合（たとえば、{% raw %}`{% if %}`、`{% elsif %}`、または`{% unless %}`{% endraw %}を使用してURLを設定する場合）、リンクエイリアスはそれらのリンクに適用されません。つまり、これらのリンクは**リンク管理**に表示されず、クリックトラッキング用の`lid`も付与されません。

**推奨:** HTMLブロックで`assign`（または{% raw %}`{% capture %}`{% endraw %}）を使用して最終URLを構築し、リンクが必要な場所でその変数を参照します。ドラッグ＆ドロップエディターでは、ボタンの**URL**フィールドに末尾の`?`または`&`を適切に付けて変数を貼り付けます。たとえば、`{{url}}?`のようにします。

{% raw %}
```liquid
{% if {{custom_attribute.${account_tier}}} == "pro" %}
{% assign url = "https://example.com/pro/verify" %}
{% else %}
{% assign url = "https://example.com/retail/account" %}
{% endif %}
```
{% endraw %}

ボタンの**URL**フィールド（ドラッグ＆ドロップ）またはHTMLで、デリミタ付きの変数に`href`を向けます。

{% raw %}
```liquid
<a href="{{ url }}?">Go to account</a>
```
{% endraw %}

または、URLを1つの変数にキャプチャすることもできます。

{% raw %}
```liquid
{% capture url %}
  {%- if condition -%}
    https://example.com/url1
  {%- else -%}
    https://example.com/url2
  {%- endif -%}
{% endcapture %}

<a href="{{ url }}?">Go to account</a>
```
{% endraw %}

## トラブルシューティング {#troubleshooting}

### `lid`パラメーターを受け付けない送信先 {#destinations-that-dont-accept-the-lid-parameter}

メールエディターからテストメッセージを送信すると、Brazeはリンクに{% raw %}`lid={{placeholder}}`{% endraw %}を付加します（プレースホルダーは送信時に一意の値になります）。送信先のサイトやAPIが追加のクエリパラメーターを許容しない場合、エディターではリンクが機能しても、メールから開いたときに失敗する可能性があります。

`lid`値がないと、BrazeはそのURLをトラッキングやセグメンテーションのためのリンクエイリアスとして扱いません。バックエンドやサイトを更新して、`lid`クエリパラメーターが存在する場合に無視するようにすることを推奨します。これにより、この記事で説明されているリンクエイリアス、レポート、およびセグメントのユースケースが維持されます。

または、バックエンドの変更を計画している間、ダッシュボードでリンクエイリアスをオフにすることもできます。**設定** > **メール設定** > **リンクエイリアス設定**に移動してください。

送信先のシステムを変更できない場合は、[Brazeサポート]({{site.baseurl}}/braze_support)に連絡して、ワークスペースのリンクエイリアスを無効にしてください。ワークスペースでリンクエイリアスがオフになった場合、以下の点に注意してください。

- 新しいメールメッセージやContent Blocksには、通常、新しいリンクエイリアスマークアップ（`lid`クエリパラメーターなど）が付与されません。
- リンクエイリアスがオンの状態で作成された既存のメッセージには、HTML内にリンクエイリアスマークアップが残っている場合があります。不要な場所の残存する`lid`パラメーターを手動で削除する必要がある場合があります。
- 既存のキャンペーン、キャンバスのメールステップ、またはContent Blocksを編集する場合、テンプレート化されたリンクが正しく表示されるように、リンクテンプレートを再度追加する必要がある場合があります。
- リンクエイリアスがオンの状態で送信されたクリックレポートは、機能がオフになった後のレポートときれいに一致しない場合があります。
- リンクエイリアスベースのフィルター（たとえば、**エイリアスをクリック**フィルター）を使用するセグメントは、期待するオーディエンスを返さなくなる可能性があります。