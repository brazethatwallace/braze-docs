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

リンクエイリアスを使用すると、メールで送信されるリンクを識別・トラッキングするためのユーザー定義の名前を作成できます。これにより、完全なリンクを参照することなく、わかりやすいリンクエイリアスをメール内で効率的に使用して、エンゲージメントをトラッキングし、キャンペーンのパフォーマンスを分析できます。

リンクエイリアスでは、以下のことが可能です。

- **特定のリンクをクリックしたユーザーをリターゲティングする:** リンクをクリックしたユーザーを特定してターゲティングします。
- **アクションベースのトリガーを作成する:** ユーザーがリンクをクリックしたときにメールを送信します。
- **指標を分析する:** リンク A とリンク B をクリックしたユーザー数を比較します。

### 仕組み {#how-it-works}

Brazeは、すべてのリンク URL に `lid`（リンク識別子とも呼ばれます）という追加パラメーターを付加することで、メール内のリンクを一意に識別します。この `lid` 値により、他の URL パラメーターが異なっていても、Brazeはリンクに対するユーザーインタラクションをトラッキング、モニタリング、および集計できます。これにより、メールキャンペーンのコンテンツに対するユーザーのエンゲージメントに関するインサイトを得ることができます。

リンク識別子は、メールキャンペーン、メールメッセージを含むキャンバス、またはContent Blocksが複製された場合にも更新されます。

## リンクエイリアスの作成 {#creating-a-link-alias}

{% alert important %}
**Link Management**は、Brazeがアカウントのリンク管理を有効にすると、キャンペーンまたはキャンバスのメールコンポーザーに表示されます。**リンクエイリアス**を作成および編集するには、リンクエイリアスを有効にする必要があります。**Link Management**が表示されない場合は、アカウントマネージャーに連絡してリンクエイリアスを有効にしてください。
{% endalert %}

リンクエイリアスを作成するには、キャンペーンまたはキャンバスコンポーネントでメール本文を開き、**Content**エリアから**Link Management**を開きます。ドラッグ＆ドロップエディターとHTMLエディターは同じサイドバーレイアウトを使用します。

### ドラッグ＆ドロップエディター {#drag-and-drop-editor}

1. **Edit Email Body**を選択して、ドラッグ＆ドロップコンポーザーを開きます。
2. コンポーザーのサイドバーで、**Content**（**Sending Settings**および**Preview & Test**の横）を選択します。このレイアウトの詳細については、[ドラッグ＆ドロップでメールを作成する]({{site.baseurl}}/user_guide/channels/email/drag_and_drop)を参照してください。
3. **Content**サブメニューで、**Link Management**（**Design and Build**の下に表示）を選択します。サブメニューが折りたたまれている場合は、サイドバーの矢印コントロールを使用して展開してください。

### HTMLエディター {#html-editor}

1. コンポーザーでメール本文に移動します。
2. コンポーザーのサイドバーで、**Content**を選択します。
3. **Content**サブメニューで、**Design and Build**の下にある**Link Management**を選択します。

**Link Management**では以下を行います。

1. Brazeが各リンクに対して一意のデフォルトリンクエイリアスを自動生成します。
2. エイリアスに名前を付けます。エイリアスは、メールキャンペーンのバリアントまたはキャンバスコンポーネントごとに一意の名前を付ける必要があります。

また、レポートやセグメンテーションで特定のリンクを参照する際に使用するエイリアスを設定することもできます。

![4つのリンクエイリアスが表示されたLink Managementページ。]({% image_buster /assets/img/link_aliasing_composer.png %})

{% alert note %}
リンクエイリアスは、クエリパラメーターを安全に追加できるHTMLアンカータグ内の`href`属性でのみサポートされています。Brazeが`lid`値を簡単に追加できるように、リンクの末尾に疑問符（?）を含めることがベストプラクティスです。`lid`値を追加しないと、BrazeはリンクエイリアスのためにそのURLを認識しません。
{% endalert %}

{% alert important %}
ドラッグ＆ドロップエディターでは、リンクエイリアスが**Link Management**タブに表示されるように、URL内のハッシュ記号（`#`）の前に疑問符（`?`）を含める必要があります。
{% endalert %}

## リンクエイリアスの管理 {#managing-link-aliases}

トラッキング対象のすべてのリンクエイリアスを表示するには、以下の手順に従ってください。

1. **ワークスペース設定**の**設定** > **メール設定**に移動します。
2. **リンクエイリアス設定**タブを選択します。

ここでは、リンクエイリアスの並べ替え、検索、トラッキングの無効化を行うことができます。

![さまざまなキャンペーンに関連付けられたアクティブおよび非アクティブなリンクエイリアスを表示するトラッキング対象リンクエイリアスページ。]({% image_buster /assets/img/tracked_aliases.png %})

{% alert tip %}
[キャンペーンのリンクエイリアスを一覧表示]({{site.baseurl}}/get_campaign_link_alias)および[キャンバスのリンクエイリアスを一覧表示]({{site.baseurl}}/get_canvas_link_alias)エンドポイントを使用して、キャンペーンの各メッセージバリアントまたはメール固有のキャンバスコンポーネントに設定された`alias`を抽出できます。
{% endalert %}

Brazeでは、メール内のリンクを評価し、リンクテンプレートを追加し、セグメンテーションやレポート作成に適した命名規則を設定することをお勧めします。これにより、すべてのリンクを把握しやすくなります。

リンクエイリアスが有効になっている場合、メッセージ、Content Blocks、リンクテンプレートは変更されません。リンクテンプレートやContent Blocksを使用している既存のメッセージもそのまま維持されます。ただし、メッセージを更新すると、リンクエイリアスのマークアップがすべてのリンクに適用されるため、リンクを表示するにはリンクテンプレートを再適用する必要があります。

## リンクエイリアスによるリンクの更新方法 {#how-links-are-updated-with-link-aliasing}

以下の表は、メール本文中のリンク、リンクエイリアスの結果、およびリンクエイリアスによって元のリンクがどのように更新されるかの説明例を示しています。

### パーマリンク {#permalink}

**ロジック：** Brazeはクエスチョンマーク（?）を挿入し、URLに最初のクエリパラメーターを追加します。

| メール本文中のリンク    | エイリアス付きリンク                     |
|-----------------------|----------------------------------------|
| `https://www.braze.com` | `https://www.braze.com?lid=slfdldtqdhdk` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="パーマリンク" }

### 複数のクエリパラメーターを含むリンク {#link-with-more-query-parameters}

**ロジック：** Brazeは他のクエリパラメーターを検出し、URLの末尾に `lid=` を追加します。

| メール本文中のリンク                                            | エイリアス付きリンク                                                             |
|---------------------------------------------------------------|--------------------------------------------------------------------------------|
| `https://www.braze.com?utm_campaign=retention&utm_source=email` | `https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="複数のクエリパラメーターを含むリンク" }

### HTMLリンク {#html-link}

**ロジック：** BrazeはリンクがURLであり、すでにクエスチョンマーク（?）が存在することを認識するため、`lid` クエリパラメーターはクエスチョンマークの後に追加されます。

| メール本文中のリンク                                                | エイリアス付きリンク                                                                |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTMLリンク" }

### アンカー付きリンク {#link-with-anchor}

**ロジック：** BrazeはURLが標準的な構造を使用し、アンカー（#）がクエスチョンマーク（?）の後に存在することを想定しています。Brazeは左から右に読み取るため、クエスチョンマークと `lid` 値はアンカーの前に追加されます。

| メール本文中のリンク                               | エイリアス付きリンク                                                |
|--------------------------------------------------|-------------------------------------------------------------------|
| `https://www.braze.com#bookmark1?utm_source=email` | `https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="アンカー付きリンク" }

### アンカーとキャプチャタグ付きリンク {#link-with-anchor-and-capture-tag}

**ロジック：** アンカー（#）を含むURLでリンクエイリアスを使用する場合、Brazeはアンカーがクエリパラメーターの後に配置されることを想定しています。つまり、適切なトラッキングのために `lid` 値はアンカーの**前に**追加される必要があり、Brazeは左から右にURLを読み取るため、クエスチョンマーク（?）と `lid` はアンカーの前に配置されます。

| メール本文中のリンク                                                                        | エイリアス付きリンク                                                                                           |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| {%raw%}`<a href="https://www.braze.com/promotions#special-offer">Check out our special offer!</a>`{%endraw%}  | {%raw%}`<a href="https://www.braze.com/promotions?lid={{link_alias}}#special-offer">Check out our special offer!</a>` {%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="アンカーとキャプチャタグ付きリンク" }

## リンクエイリアスのトラッキング {#tracking-link-aliases}

コンポーザーのサイドバーで、**コンテンツ** > **リンク管理**（**デザインとビルド**の下）を選択し、**トラッキング**したいエイリアスを選択します。トラッキングされたエイリアスは、リンクエイリアスを参照するセグメンテーションフィルターで使用できます（[セグメンテーションフィルター](#segmentation-filters)を参照）。また、ユーザーがメール内のリンクエイリアスをクリックした際に、アクションベースのメッセージを送信したり、ユーザーをキャンバスに進めたりすることもできます。[アクションベースのフィルター](#action-based-filters)を参照してください。**トラッキング**設定は、そのリンクのクリックがメールパフォーマンスレポートにカウントされるかどうかには影響しません。

{% alert tip %}
リンクエンゲージメント指標をトラッキングするには、リンクの先頭にHTTPまたはHTTPSを付けてください。特定のリンクのクリックトラッキングをオフにするには、[ユニバーサルリンクとApp Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#turning-off-click-tracking-on-a-link-to-link-basis)を参照してください。
{% endalert %}

Brazeでは無制限のリンクをトラッキング対象として選択できますが、リターゲティングできるのは、ユーザーが最近開いたリンクのみです。ユーザープロファイルには、最近クリックされた100件のリンクが含まれます。たとえば、500件のリンクをトラッキングし、ユーザーが500件すべてをクリックした場合、最近クリックされた100件のリンクに基づいてリターゲティングやセグメント作成ができます。

![2つのリンクが選択されたリンク管理タブ。]({% image_buster /assets/img/link_management_dnd.png %})

{% alert note %}
Brazeは、プロファイルレベルで最後にクリックされた100件のリンクエイリアスまでしかトラッキングしません。
{% endalert %}

### アクションベースのフィルター {#action-based-filters}

ワークスペースでリンクエイリアスが有効になっている場合、任意のリンク（トラッキング済みまたは未トラッキング）をターゲットとするアクションベースのメッセージを作成したり、ユーザーがメールキャンペーンやキャンバスコンポーネントでエイリアスをクリックしたかどうかに基づいてリターゲティングしたりできます。

![キャンバスコンポーネントでエイリアスをクリックしたユーザーやキャンペーンとインタラクションしたユーザーをターゲットとするアクションベースのオプション。]({% image_buster /assets/img/link_aliasing_action_based_filters.png %})

- キャンペーンがアーカイブされると、リンクトラッキングはオフになり、そのリンクエイリアスは別のフィルターで使用できなくなります。
- リンクのトラッキングがオンになっていてキャンペーンでクリックされた場合、リンクトラッキングがその後オフになっていても、そのメッセージ上の少なくとも1つのリンクがまだトラッキングされている限り、セグメントフィルターで利用可能なオプションとしてそのキャンペーンを見つけることができます。
- トラッキングされたリンクをフィルターとして選択できるのは、**キャンバスステップでエイリアスをクリック**フィルタードロップダウンを使用して、アクティブ（開始済み）のキャンバス内にある場合のみです。リンクがキャンバスの下書きでトラッキングされている場合、そのトラッキングされたリンクをフィルターとして選択することはできません。

リンクを未トラッキングに設定するには、**設定** > **メール設定** > **リンクエイリアス設定**に移動します。

### セグメンテーションフィルター {#segmentation-filters}

Brazeでは、メール内にリンクエイリアスがあり、ユーザーがそれをクリックすると、そのイベントがエイリアスとともにユーザーのプロファイルに記録されます。

「任意のキャンペーンまたはキャンバスステップでエイリアスをクリック」セグメンテーションフィルターを使用した後、このリンクエイリアスの名前を変更した場合、ユーザープロファイル内の以前のクリックデータは**更新されません**。つまり、以前のリンクエイリアスとして表示されたままです。そのため、新しいリンクエイリアスに基づいてユーザーをターゲットにしても、以前のリンクエイリアスのデータは含まれません。

「キャンペーンでエイリアスをクリック」または「キャンバスでエイリアスをクリック」セグメンテーションフィルターを使用すると、特定のキャンペーンまたはキャンバスで特定のエイリアスをクリックしたかどうかでユーザーをフィルタリングします。複数のユーザーが同じメールアドレスを共有しており、そのリンクエイリアスがクリックされた場合、そのメールアドレスを共有する他のすべてのユーザーのプロファイルも更新されます。これらのプロファイルは、クリックイベントだけでなく、配信イベントや開封イベントによっても更新されます。

以下のセグメンテーションフィルターは、イベントが処理される時点でトラッキングされているクリックイベントに適用されます。つまり、未トラッキングのリンクは既存のデータを削除せず、リンクをトラッキングしてもデータがバックフィルされることはありません。詳細については、[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)を参照してください。

#### リンクのトラッキング解除 {#untracking-links}

リンクのトラッキングを解除しても、フィルターを持つ既存のセグメントは未トラッキングのエイリアスに再割り当てされません。古いデータは、新しいデータに置き換えられるまでユーザープロファイルに残ります。

アーカイブされたメッセージ内のリンクは自動的にトラッキング解除されます。ただし、アーカイブされたメッセージのアーカイブが解除された場合、リンクを再度トラッキングする必要があります。リンクエイリアスがトラッキングされている場合、リンクレポートはトップレベルドメインや完全なURLではなく、エイリアスでインデックスされます。

メールキャンペーン内のすべてのリンクとそれぞれの合計クリック数を表示するには、**メッセージ分析** > **メールパフォーマンス** > **プレビュー＆ヒートマップ**に移動し、**ヒートマップを表示**トグルを選択します。

![リンクエイリアスとその合計クリック数が表示された合計クリック数別リンクテーブルパネル。]({% image_buster /assets/img/link_alias_total_clicks.png %}){: style="max-width:60%;"}

### メールクリックイベント {#email-clicks-event}

Currentsを使用してエンゲージメントデータをエクスポートする場合、リンクエイリアスが有効になっていると、メールクリックイベントが若干異なります。リンクエイリアスがオンの場合、[メールクリックイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-click-events)に`link_id`と`link_alias`の2つの追加フィールドがあります。

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
`dispatch_id`の動作は、キャンバスとキャンペーンで異なります。Brazeはキャンバスステップ（エントリステップを除く。エントリステップはスケジュール可能）を、「スケジュール済み」であってもトリガーイベントとして扱うためです。キャンバスとキャンペーンにおける[`dispatch_id`の動作]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id)について詳しくはこちらをご覧ください。

_2019年8月に更新。_
{% endalert %}

## Content Blocksでのリンクエイリアス {#link-aliasing-in-content-blocks}

新しいContent Blocksでは、リンクが変更され、Brazeが該当する各リンクに `lid={{placeholder}}` を付加します。このプレースホルダー値は、メールメッセージバリアントに挿入されるときに解決されます。

Brazeがリンクエイリアスを有効にする前に作成された既存のContent Blocks内のリンクを変更するには、既存のContent Blocksを複製してから、複製したContent Blocks内のリンクを変更してください。

`lid` 値のないContent Blocksが新しいメッセージに挿入された場合、そのContent Blocksのリンクはエイリアスでトラッキングされません。新しいContent Blocksが「古い」メッセージバリアントに挿入された場合、そのメッセージバリアントのリンクはリンクエイリアスによって認識されます。Content Blocksのリンクも認識されます。ただし、「古い」Content Blocksに「新しい」Content Blocksをネストすることはできません。

{% alert tip %}
Content Blocksについては、新しいメッセージで使用するために既存のContent Blocksのコピーを作成することをBrazeは推奨しています。これは一括複製で行うことができ、リンクエイリアスが有効になっていないContent Blocksを新しいメッセージで参照してしまうシナリオを防ぐことができます。
{% endalert %}

## Liquid で生成される URL のリンクエイリアス {#link-aliasing-for-urls-generated-by-liquid}

Liquid で生成される URL（たとえば、HTML 内の `assign`、Content Blocks から取得される値、カスタム属性内の Liquid など）に対して、Braze は `lid` クエリパラメーターを挿入する明確な場所を必要とします。多くの場合、URL に Liquid が残っていると、デリミターを自分で追加しない限り、Braze は新しいクエリ文字列を `?` で開始するか、既存のクエリに `&` で結合するかを推測しません。

以下を行ってください：

- URL にクエリ文字列が**まだ含まれていない**場合は、Liquid の後に `?` を追加します（たとえば、`{{my_url}}?`）。
- URL に `?` とクエリパラメーターが**すでに含まれている**場合は、Liquid の後に `&` を追加します（たとえば、`{{my_url}}&`）。

{% alert note %}
Liquid で生成された URL で[リンクテンプレート]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template)を使用する場合、Braze は Liquid 実行後にレンダリングされた URL にクエリセパレーターとして使用される `?` が正確に2つ含まれていると、保守的に正規化することがあります。2つ目の `?` は `&` に書き換えられ、Braze が URL をできるだけ変更しないようにします。<br><br>Braze はすべての重複 `?` パターンを修正しようとするわけではなく、より複雑な URL の処理は意図的に制限されています。まずマークアップで正しい `?` または `&` を追加し、正規化は限定的なセーフガードとして扱ってください。整形された URL の代わりとしてや、デリミターがない場合に**リンク管理**でリンクを認識させるための代替手段としては使用しないでください。
{% endalert %}

末尾に `?` または `&`（またはその他のサポートされた挿入ポイント）がない場合、リンクエイリアスは URL を認識せず、**リンク管理**にはリストされず、リンクテンプレートも適用されません。

### URL フラグメント（`#`）とトラッキングパラメーター {#url-fragments-and-tracking-parameters}

フラグメント（`#` とその後のすべて）は、通常のリンクリクエストでサーバーに送信されません。Braze は `lid` をクエリ文字列に挿入しますが、これは `#` の前に配置される必要があります。`href` に Liquid と `#` フラグメントがあるが、`#` の前に `?` または `&` がない場合、Braze は安全に `lid` を追加できないため、リンクが**リンク管理**に表示されなかったり、リンクエイリアスとしてトラッキングされなかったりすることがあります。

これは、ドラッグ＆ドロップエディターでボタン URL が Liquid とハッシュベースのパターンを組み合わせている場合（たとえば、静的パスの後に `#`、その後に追加のキーと値のペアが続く場合）に特によく発生します。その場合は、`#` の直前に `?` を追加して、クエリ文字列（`lid` を含む）がフラグメントの前に解析されるようにします。

{% raw %}
```text
https://example.com/campaign/to/abc123?#user_id={{${user_id}}}&source=email
```
{% endraw %}

上記の例では、`#` の前の `?` により、Braze は `lid` を追加するクエリセグメントを得られます。これがないと、リンクが**リンク管理**に表示されない場合があります。

クエリパラメーターの追加先を特定できない場合、リンクエイリアスはこれらの URL を認識せず、リンクテンプレートも適用されません。ダイナミック URL で **LID の割り当てに失敗しました**などのエラーが表示された場合は、`href` がこのセクションの例に示されている `?` または `&` パターンを使用していることを確認してください。

### ドラッグ＆ドロップエディターに関する注意事項 {#drag-and-drop-editor-considerations}

ドラッグ＆ドロップエディターでは、リンクを保持するフィールド（ボタンの **URL** など）は、Liquid が実行される前に基になる `href` を検証します。スペース、改行、その他の URL セーフでない文字があると、Braze がリンクテンプレートやリンクエイリアスパラメーターを追加する際に予期しない動作を引き起こす可能性があります。リンク先に分岐 Liquid が必要な場合は、HTML ブロックで URL を `assign` で設定し（次のセクションを参照）、複雑な Liquid を直接そのフィールドに入力するのではなく、ドラッグ＆ドロップの URL フィールドで単一の変数を参照してください。

### Content Blocks の例 {#content-block-example}

{% raw %}
Content Blocks に `https://www.braze.com/{{custom_attribute.${offer_id}}}` のような末尾に `?` または `&` のないリンクが含まれている場合、Braze は `lid` をどこに追加すればよいかわからないため、リンクは**リンク管理**に認識されません。Content Blocks 内の URL の末尾に `?` または `&` を追加し（クエリ文字列が既に存在するかどうかに応じて）、Content Blocks を保存すると、リンクが認識されるようになります。
{% endraw %}

### URL がユーザーごとに異なる場合のレポート {#reporting-when-the-url-varies-per-user}

メッセージ内の各固有の `href` は、**リンク管理**とエイリアスベースのレポートで**1つ**のリンク ID と1つのリンクエイリアスにマッピングされます。リンクエイリアスがトラッキングされている場合、ダッシュボード内のメールレポートは、解決される可能性のあるすべての URL ではなく、エイリアスによってインデックスされます。

まず、Braze で以下のアプローチを使用してください：

- **キャンペーンとキャンバスのメール分析：** [リンクのトラッキング解除](#untracking-links)で説明されているように、**メッセージ分析** > **メールパフォーマンス** > **プレビューとヒートマップ**で**ヒートマップを表示**をオンにして、リンクごとの集計クリック数を確認します。
- **クエリビルダーでの受信者ごとのクリック：** キャンペーンまたはキャンバスに対して**メール URL クリック済み**の[クエリビルダーテンプレート]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates#email-templates)を実行します。テンプレートは要約カウント用に非パーソナライズされたリンクを表示します。CSV エクスポートにはクリックしたユーザーのユーザー ID、クリックしたリンク、タイムスタンプが含まれます。（非パーソナライズされた URL は要約ビューで Liquid タグを除去します。詳細はテンプレートの説明を参照してください。）
- **コンポーザーでのエイリアスレベルの内訳：** 各リンク先（たとえば、各 `offer_id`）を**リンク管理**とエイリアスベースのレポートで個別の行として表示する必要がある場合は、パスがユーザーごとに変わる1つのリンクではなく、個別の `href` 値（つまり個別のエイリアス）を使用してください。たとえば、ブランチごとに異なるリンクを使用します。

ストリーミングエンゲージメントエクスポートも使用している場合、メールクリックイベントには **`url`** フィールドが含まれます。このペイロードがリンクエイリアスとどのように関連するかについては、このページの[メールクリックイベント](#email-clicks-event)を参照してください。

### 例 {#example}

割り当てられた URL にクエリパラメーターがない場合は、このパターンを使用します：

{% raw %}
```liquid
{% assign link1 = "https://www.braze1.com" %}

<a href="{{link1}}?">Visit Braze</a>
```
{% endraw %}

割り当てられた URL に既に `?` とクエリパラメーターが含まれている場合は、`?` の代わりに Liquid の後に `&` を追加します：

{% raw %}
```liquid
{% assign link_with_params = "https://www.braze1.com?campaign=test" %}

<a href="{{link_with_params}}&">Visit Braze</a>
```
{% endraw %}

### 条件付き Liquid を含む URL {#urls-with-conditional-liquid}

条件付き Liquid タグが `href` 内で使用されている場合（たとえば、{% raw %}`{% if %}`、`{% elsif %}`、または `{% unless %}`{% endraw %} で URL を設定する場合）、リンクエイリアスはそれらのリンクに適用されません。つまり、これらのリンクは**リンク管理**に表示されず、クリックトラッキング用の `lid` も付与されません。

**推奨：** HTML ブロックで `assign`（または {% raw %}`{% capture %}`{% endraw %}）を使用して最終的な URL を構築し、リンクが必要な場所でその変数を参照します。ドラッグ＆ドロップエディターでは、複雑な Liquid を直接そのフィールドに入力するのではなく、必要に応じて末尾に `?` または `&` を付けた変数をボタンの **URL** フィールドに貼り付けます。たとえば、`{{url}}?` のようにします。

{% raw %}
```liquid
{% if {{custom_attribute.${account_tier}}} == "pro" %}
{% assign url = "https://example.com/pro/verify" %}
{% else %}
{% assign url = "https://example.com/retail/account" %}
{% endif %}
```
{% endraw %}

ボタンの **URL** フィールド（ドラッグ＆ドロップ）または HTML で、デリミター付きの変数を `href` に指定します：

{% raw %}
```liquid
<a href="{{ url }}?">Go to account</a>
```
{% endraw %}

または、URL を1つの変数にキャプチャすることもできます：

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

### `lid` パラメーターを受け付けない送信先 {#destinations-that-dont-accept-the-lid-parameter}

メールエディターからテストメッセージを送信すると、Brazeはリンクに {% raw %}`lid={{placeholder}}`{% endraw %} を付加します（プレースホルダーは送信時にユニークな値に置き換わります）。送信先のサイトやAPIが追加のクエリパラメーターを許容しない場合、エディター上ではリンクが正常に動作しても、メールから開いた際に失敗することがあります。

`lid` の値がないと、BrazeはそのURLをリンクエイリアスとしてトラッキングやセグメンテーションの対象として扱いません。バックエンドやサイトを更新して、`lid` クエリパラメーターが存在する場合は無視するようにすることをお勧めします。これにより、この記事で説明されているリンクエイリアス、レポート、セグメントのユースケースが維持されます。

別の方法として、バックエンドの変更を計画する間、ダッシュボードでリンクエイリアスをオフにすることもできます。**設定** > **メール設定** > **リンクエイリアス設定**に移動してください。

送信先のシステムを変更できない場合は、[Brazeサポート]({{site.baseurl}}/user_guide/administer/personal/braze_support)に連絡して、ワークスペースのリンクエイリアスを無効にしてもらってください。ワークスペースでリンクエイリアスがオフになった場合、以下の点にご注意ください。

- 新しいメールメッセージやContent Blocksには、通常、新しいリンクエイリアスのマークアップ（`lid` クエリパラメーターなど）が付加されません。
- リンクエイリアスが有効な状態で作成された既存のメッセージには、HTML内にリンクエイリアスのマークアップが残っている場合があります。不要な箇所に残っている `lid` パラメーターは手動で削除する必要があるかもしれません。
- 既存のキャンペーン、キャンバスのメールステップ、またはContent Blockを編集する場合、テンプレート化されたリンクが正しく表示されるように、リンクテンプレートを再度追加する必要があるかもしれません。
- リンクエイリアスが有効な状態で送信されたメッセージのクリックレポートは、機能がオフになった後のレポートと整合しない場合があります。
- リンクエイリアスベースのフィルター（例：**Clicked Alias** フィルター）を使用するセグメントは、期待するオーディエンスを返さなくなる可能性があります。