---
nav_title: リンクエイリアス
article_title: リンクエイリアス
alias: /link_aliasing/
page_order: 3
description: "この記事では、リンクエイリアスの仕組みと、リンクがどのように表示されるかの例について説明します。"
channel:
  - email

---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/link-aliasing){: style="float:right;width:120px;border:0;" class="noimgborder"}リンクエイリアス {#braze-learning-course-imagebuster-assetsimgblicon3png-httpslearningbrazecomlink-aliasing-stylefloatrightwidth120pxborder0-classnoimgborderlink-aliasing}

> リンクエイリアスを使用して、Brazeから送信されるメールメッセージ内のリンクを識別するための、認識しやすいユーザー生成名を作成できます。これらのリンクは、セグメンテーションのリターゲティング、アクションベースのトリガー、およびリンク分析に利用できます。

## リンクエイリアスについて {#about-link-aliasing}

リンクエイリアスを使用すると、メールで送信されるリンクを識別・追跡するためのユーザー生成名を作成できます。これにより、完全なリンクを参照することなく、認識しやすいリンクエイリアスをメールで効率的に使用して、エンゲージメントを追跡し、Campaignのパフォーマンスを分析できます。

リンクエイリアスを使用すると、以下のことが可能です。

- **特定のリンクをクリックしたユーザーをリターゲティングする:** リンクをクリックしたユーザーを特定してターゲティングします。
- **アクションベースのトリガーを作成する:** ユーザーがリンクをクリックしたときにメールを送信します。
- **指標を分析する:** リンクAとリンクBのクリック数を比較します。

### 仕組み {#how-it-works}

Brazeは、すべてのリンクURLに`lid`（リンク識別子とも呼ばれる）という追加パラメーターを付加することで、メール内のリンクを一意に識別します。この`lid`値により、URLの他のパラメーターが異なる場合でも、Brazeはリンクに対するユーザーインタラクションを追跡、監視、集計できます。これにより、メールCampaignのコンテンツに対するユーザーのエンゲージメントに関するインサイトが得られます。

リンク識別子は、メールCampaign、メールメッセージを含むCanvas、またはContent Blocksが複製された場合にも更新されます。

## リンクエイリアスの作成 {#creating-a-link-alias}

リンクエイリアスを作成するには、以下の手順に従います。

1. CampaignまたはCanvasコンポーネントで、メール本文に移動します。
2. **リンク管理**タブを選択します。
3. Brazeが各リンクに対して一意のデフォルトリンクエイリアスを自動的に生成します。
4. エイリアスに名前を付けます。エイリアスは、メールCampaignバリアントまたはCanvasコンポーネントごとに一意の名前を付ける必要があります。

レポートやセグメンテーションで特定のリンクを参照するために使用するエイリアスを設定することもできます。

![4つのリンクエイリアスが表示されたリンク管理ページ。]({% image_buster /assets/img/link_aliasing_composer.png %})

{% alert note %}
リンクエイリアスは、クエリパラメーターを安全に付加できるHTMLアンカータグ内の`href`属性でのみサポートされています。Brazeが`lid`値を簡単に付加できるように、リンクの末尾に疑問符（?）を含めることがベストプラクティスです。`lid`値を付加しないと、BrazeはリンクエイリアスのためにそのURLを認識しません。
{% endalert %}

## リンクエイリアスの管理 {#managing-link-aliases}

追跡されているすべてのリンクエイリアスを表示するには、以下の手順に従います。

1. **設定** > **ワークスペース設定**の**メール設定**に移動します。
2. **リンクエイリアス設定**タブを選択します。

{% alert important %}
[旧ナビゲーション]({{site.baseurl}}/user_guide/administer/personal/the_braze_dashboard/)を使用している場合、これらの設定は**設定の管理**にあります。
{% endalert %}

ここでは、リンクエイリアスの並べ替え、検索、およびトラッキングのオン/オフを切り替えることができます。

![さまざまなCampaignに関連付けられたアクティブおよび非アクティブなリンクエイリアスが表示された追跡リンクエイリアスページ。]({% image_buster /assets/img/tracked_aliases.png %})

{% alert tip %}
[Campaignのリンクエイリアス一覧]({{site.baseurl}}/get_campaign_link_alias/)および[Canvasのリンクエイリアス一覧]({{site.baseurl}}/get_canvas_link_alias/)エンドポイントを使用して、CampaignまたはメールのCanvasコンポーネントの各メッセージバリアントに設定された`alias`を抽出できます。
{% endalert %}

Brazeでは、メール内のリンクを評価し、リンクテンプレートを追加し、セグメンテーションやレポートに適した命名規則を設定することを推奨しています。これにより、すべてのリンクを把握しやすくなります。

リンクエイリアスがオンになっている場合、メッセージ、Content Blocks、およびリンクテンプレートは変更されません。リンクテンプレートやContent Blocksを使用している既存のメッセージはそのままです。ただし、メッセージを更新すると、リンクエイリアスのマークアップがすべてのリンクに適用されるため、リンクを表示するにはリンクテンプレートを再適用する必要があります。

## リンクエイリアスによるリンクの更新方法 {#how-links-are-updated-with-link-aliasing}

以下の表は、メール本文内のリンク、リンクエイリアスの結果、および元のリンクがリンクエイリアスによってどのように更新されるかの説明の例を示しています。

### パーマリンク {#permalink}

**ロジック:** Brazeは疑問符（?）を挿入し、URLに最初のクエリパラメーターを追加します。

| メール本文内のリンク    | エイリアス付きリンク                     |
|-----------------------|----------------------------------------|
| `https://www.braze.com` | `https://www.braze.com?lid=slfdldtqdhdk` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 追加のクエリパラメーターを含むリンク {#link-with-more-query-parameters}

**ロジック:** Brazeは他のクエリパラメーターを検出し、URLの末尾に`lid=`を付加します。

| メール本文内のリンク                                            | エイリアス付きリンク                                                             |
|---------------------------------------------------------------|--------------------------------------------------------------------------------|
| `https://www.braze.com?utm_campaign=retention&utm_source=email` | `https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### HTMLリンク {#html-link}

**ロジック:** Brazeはリンクがすでに疑問符（?）を含むURLであることを認識し、疑問符の後に`lid`クエリパラメーターを付加します。

| メール本文内のリンク                                                | エイリアス付きリンク                                                                |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### アンカー付きリンク {#link-with-anchor}

**ロジック:** Brazeは、アンカー（#）が疑問符（?）の後に配置される標準的なURL構造を想定しています。Brazeは左から右に読み取るため、疑問符と`lid`値はアンカーの前に付加されます。

| メール本文内のリンク                               | エイリアス付きリンク                                                |
|--------------------------------------------------|-------------------------------------------------------------------|
| `https://www.braze.com#bookmark1?utm_source=email` | `https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### アンカーとキャプチャタグ付きリンク {#link-with-anchor-and-capture-tag}

**ロジック:** リンクエイリアスをアンカー（#）を含むURLで使用する場合、Brazeはアンカーがクエリパラメーターの後に配置されることを想定しています。つまり、適切なトラッキングのために`lid`値はアンカーの**前に**付加される必要があり、Brazeは左から右にURLを読み取るため、疑問符（?）と`lid`はアンカーの前に配置されます。

| メール本文内のリンク                                                                        | エイリアス付きリンク                                                                                           |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| {%raw%}`<a href="https://www.braze.com/promotions#special-offer">Check out our special offer!</a>`{%endraw%}  | {%raw%}`<a href="https://www.braze.com/promotions?lid={{link_alias}}#special-offer">Check out our special offer!</a>` {%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## リンクエイリアスのトラッキング {#tracking-link-aliases}

**リンク管理**タブで、セグメンテーション目的で「追跡」するエイリアスを選択し、セグメンテーションフィルターに表示されるようにします。追跡されるエイリアスはセグメンテーション目的のみであり、レポート目的のリンクトラッキングには影響しません。

{% alert tip %}
リンクのエンゲージメント指標を追跡するには、リンクがHTTPまたはHTTPSで始まることを確認してください。特定のリンクのクリックトラッキングをオフにするには、[ユニバーサルリンクとアプリリンク]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/#turning-off-click-tracking-on-a-link-to-link-basis)を参照してください。
{% endalert %}

Brazeでは無制限のリンクを追跡できますが、リターゲティングできるのはユーザーが最近開いたリンクのみです。ユーザープロファイルには、最近クリックされた100件のリンクが含まれます。たとえば、500件のリンクを追跡し、ユーザーがそのすべてをクリックした場合、最近クリックされた100件のリンクに基づいてリターゲティングまたはSegmentを作成できます。

![2つのリンクが選択されたリンク管理タブ。]({% image_buster /assets/img/link_management_dnd.png %})

{% alert note %}
Brazeは、プロファイルレベルで最後にクリックされた100件のリンクエイリアスのみを追跡します。
{% endalert %}

### アクションベースのフィルター {#action-based-filters}

任意のリンク（追跡または未追跡）をターゲットとするアクションベースのメッセージを作成したり、メールCampaignまたはCanvasコンポーネント全体でエイリアスをクリックしたかどうかに基づいてユーザーをリターゲティングしたりできます。

![CanvasコンポーネントでエイリアスをクリックしたユーザーまたはCampaignとインタラクションしたユーザーをターゲットにするアクションベースのオプション。]({% image_buster /assets/img/link_aliasing_action_based_filters.png %})

### セグメンテーションフィルター {#segmentation-filters}

Brazeでは、メールにリンクエイリアスがあり、ユーザーがそれをクリックすると、そのイベントがエイリアスとともにユーザーのプロファイルに記録されます。

「任意のCampaignまたはキャンバスステップでエイリアスをクリック」セグメンテーションフィルターを使用し、後でこのリンクエイリアスの名前を変更した場合、ユーザープロファイル内の以前のクリックデータは**更新されません**。つまり、以前のリンクエイリアスとして表示されたままです。そのため、新しいリンクエイリアスに基づいてユーザーをターゲティングしても、以前のリンクエイリアスのデータは含まれません。

「Campaignでエイリアスをクリック」または「Canvasでエイリアスをクリック」セグメンテーションフィルターを使用すると、特定のCampaignまたはCanvasで特定のエイリアスをクリックしたかどうかでユーザーをフィルタリングします。複数のユーザーが同じメールアドレスを共有しており、リンクエイリアスがクリックされた場合、そのメールアドレスを共有する他のすべてのユーザーのプロファイルも更新されます。これらのプロファイルは、クリックイベントだけでなく、配信イベントや開封イベントによっても更新されます。

以下のセグメンテーションフィルターは、イベントが処理された時点で追跡されるクリックイベントに適用されます。つまり、未追跡のリンクは既存のデータを削除せず、リンクの追跡はデータをバックフィルしません。詳細については、[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/)を参照してください。

#### リンクの追跡解除 {#untracking-links}

リンクの追跡を解除しても、フィルターを使用している既存のSegmentが追跡解除されたエイリアスに再割り当てされることはありません。古いデータは、新しいデータに置き換えられるまでユーザープロファイルに残ります。

アーカイブされたメッセージ内のリンクは自動的に追跡解除されます。ただし、アーカイブされたメッセージがアーカイブ解除された場合、リンクを再度追跡する必要があります。リンクエイリアスが追跡されている場合、リンクレポートはトップレベルドメインや完全なURLではなく、エイリアスによってインデックスされます。

メールCampaign内のすべてのリンクとそれぞれの合計クリック数を表示するには、**メッセージ分析** > **メールのパフォーマンス** > **プレビューとヒートマップ**に移動し、**ヒートマップを表示**トグルを選択します。

![リンクエイリアスとその合計クリック数が表示された合計クリック数別リンクテーブルパネル。]({% image_buster /assets/img/link_alias_total_clicks.png %}){: style="max-width:60%;"}

### メールクリックイベント {#email-clicks-event}

エンゲージメントデータをCurrentsでエクスポートする場合、リンクエイリアスが有効になっていると、メールクリックイベントは若干異なります。リンクエイリアスがオンの場合、[メールクリックイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-clicks-events/)に`link_id`と`link_alias`の2つの追加フィールドがあります。

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
`dispatch_id`の動作は、CanvasとCampaignで異なります。Brazeは、Canvasステップ（エントリステップを除く。エントリステップはスケジュール可能）を、「スケジュール済み」であってもトリガーイベントとして扱います。CanvasおよびCampaignにおける[`dispatch_id`の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)の詳細をご覧ください。

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

HTMLまたはContent Blocksの`assign`ステートメントなど、Liquidで生成されるURLの場合、Liquidタグに疑問符（`?`）を追加する必要があります。これにより、Brazeがクエリパラメーター（`lid=somevalue`）を付加でき、リンクエイリアスが正しく機能するようになります。

クエリパラメーターの付加場所を特定できない場合、リンクエイリアスはこれらのURLを認識せず、リンクテンプレートも適用されません。

### 例 {#example}

リンクの推奨フォーマットについて、以下のリンクエイリアスの例をご確認ください。

{% raw %}
```liquid
{% assign link1 = "https://www.braze1.com" %}

<a href="{{link1}}?">Click Here</a>
```
{% endraw %}

リンク内に疑問符（`?`）を含むパラメーターがある場合、以下の例のようにアンカータグ内でアンパサンド（`&`）に置き換えることができます。

{% raw %}
```liquid
{% assign link_with_params = "https://www.braze1.com?param_1&param_2" %}

<a href="{{link_with_params}}&">Click Here</a>
```
{% endraw %}

### 条件付きLiquidを含むURL {#urls-with-conditional-liquid}

条件付きLiquidタグが`href`内で使用されている場合（たとえば、{% raw %}`{% if %}`、`{% unless %}`{% endraw %}を使用してURLを条件付きで設定する場合）、リンクエイリアスはそれらのリンクに適用されません。つまり、これらのリンクは**リンク管理**に表示されず、クリックトラッキング用の`lid`も付与されません。

{% raw %}`{% capture %}`{% endraw %}ブロックを使用して`href`の外でURLを構築し、以下の例のように変数として参照できます。

{% raw %}
```liquid
  {%- if condition -%}
    https://example.com/url1
  {%- else -%}
    https://example.com/url2
  {%- endif -%}
{%- endcapture -%}

<a href="{{ url }}?">Click here</a>
```
{% endraw %}