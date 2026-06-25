---
nav_title: "バナーを作成"
article_title: "バナーを作成"
page_order: 1
description: "このリファレンス記事では、BrazeのCampaignsとCanvasesを使用してバナーを作成、構成、設定、送信する方法について説明します。"
tool:
  - Campaigns
channel:
  - banners
---

# バナーを作成 {#create-a-banner}

> BrazeでCampaignsやCanvasesを構築する際にバナーを作成する方法を説明します。一般的な情報については、[バナーについて]({{site.baseurl}}/user_guide/channels/banners/)を参照してください。

## 前提条件 {#prerequisites}

バナーを起動する前に、開発チームが[アプリまたはWebサイトにプレースメントを設定する]({{site.baseurl}}/developer_guide/banners/placements/)必要があります。その間にバナーCampaignの下書きを作成することはできますが、プレースメントが設定されるまでCampaignを起動することはできません。

## バナーメッセージを作成する {#create-a-banner-message}

{% multi_lang_include banners/creating_placements.md section="user" %}

### ステップ2: メッセージの作成場所を選択する {#step-2-choose-where-to-build-your-message}

メッセージをCampaignとCanvasのどちらで送信すべきかわからない場合は、Campaignsは単一のターゲットメッセージングキャンペーンに適しており、Canvasesはマルチステップのユーザージャーニーに適しています。

{% tabs %}
{% tab Campaign %}

1. **Messaging** > **Campaigns** に移動し、**Create Campaign** を選択します。
2. **Banner** を選択します。
3. Campaignにわかりやすく意味のある名前を付けます。
4. 必要に応じて[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams/)と[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/)を追加します。タグを使用すると、Campaignsを見つけやすくなり、レポートを作成しやすくなります。たとえば、レポートビルダーを使用する際に、関連するタグでフィルタリングできます。
5. 以前に作成したプレースメントを選択して、Campaignに関連付けます。
6. 必要に応じてバリアントを追加します。各バリアントに異なるメッセージタイプとレイアウトを選択できます。バリアントの詳細については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing/)を参照してください。
7. バナーCampaignの開始日時を選択します。デフォルトでは、バナーは無期限に継続します。**End Time** を選択して終了日時を指定することで、これを変更できます。

{% alert tip %}
Campaign内のすべてのメッセージが類似している、または同じコンテンツを持つ場合は、追加のバリアントを追加する前にメッセージを作成してください。その後、**Add Variant** ドロップダウンから **Copy from Variant** を選択できます。
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. Canvasコンポーザーを使用して[Canvasを作成]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/)します。
2. Canvasを設定した後、Canvasビルダーでメッセージステップを追加します。ステップにわかりやすく意味のある名前を付けます。
3. メッセージングチャネルとして **Banner** を選択します。
4. バナーのプレースメントを選択します。
5. バナーの優先度を設定します。[バナーの優先度]({{site.baseurl}}/user_guide/channels/banners/#priority)は、同じプレースメントを共有するバナーの表示順序を決定します。
6. バナーの有効期限を設定します。ステップが利用可能になってからの期間、または特定の日時で設定できます。

{% endtab %}
{% endtabs %}

### ステップ3: バナーを作成する {#compose-a-banner}

バナーを作成するには、以下のいずれかを選択できます。

- 空白のテンプレートから開始する
- Brazeバナーテンプレートを使用する
- 保存済みのバナーテンプレートを選択する

![空白のバナーまたはテンプレートを選択するオプション。]({% image_buster /assets/img/banners/choose_banner_composer.png %})

#### ステップ3.1: バナーのスタイルを設定する {#step-31-style-the-banner}

ブロックと行をキャンバスエリアにドラッグ＆ドロップして、メッセージの作成を開始できます。バナーエディターのブロックと共有プロパティの詳細へのリンクについては、[エディターブロック（バナー）]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=banners)を参照してください。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

メッセージのバックグラウンドプロパティ、ボーダー設定などをカスタマイズするには、**Styles** を選択します。特定のブロックまたは行のスタイルのみをカスタマイズしたい場合は、それを選択して変更を加えます。

![バナーコンポーザーのスタイルパネル。]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### ステップ3.2: クリック時の動作を定義する（オプション） {#step-32-define-on-click-behavior-optional}

ユーザーがバナー内のリンクをクリックした際に、アプリ内のより深い場所に移動させるか、別のWebページにリダイレクトさせるかを選択できます。さらに、[カスタム属性またはイベントを記録する]({{site.baseurl}}/developer_guide/analytics/)ことを選択でき、ユーザーがバナーをクリックした際にカスタムデータでユーザーのプロファイルを更新します。より詳細なクリックトラッキングのために、プロパティパネルの **Identifier for Reporting** フィールドを使用して、各インタラクティブ要素にカスタム識別子を割り当てます。

{% alert important %}
{::nomarkdown}
特定の要素（バナーのボタン、リンク、画像など）に独自のクリック時の動作がある場合、クリック時の動作はオーバーライドされることがあります。たとえば、以下のクリック時の動作がある場合：<br><ul><li>バナーにはWebサイトのホームページにリダイレクトするクリック時の動作があります。</li><li>バナー内の画像にはWebサイトの製品ページにリダイレクトするクリック時の動作があります。</li></ul>ユーザーが画像をクリックすると、製品ページにリダイレクトされます。ただし、バナーの周囲のエリアをクリックすると、ホームページにリダイレクトされます。
{:/}
{% endalert %}

#### ステップ3.3: 非表示の動作を設定する（オプション） {#dismiss-behavior}

**Dismiss behavior** セクションの **Banner can be dismissed** チェックボックスを選択すると、ユーザーがバナーを非表示にできるようになります。このオプションは、幅広いオーディエンスに期間限定のオファーを宣伝したいが、興味のないユーザーにはメッセージを非表示にできるようにしたい場合に便利です。

非表示が有効になっている場合、**Dismiss behavior** セクションで非表示ボタンをカスタマイズできます。

| 設定 | 説明 |
|---------|-------------|
| **ボタンサイズ** | バナーに表示される非表示ボタンのサイズです。 |
| **ボタンの色** | 非表示ボタンの色です。 |
| **ARIAラベル** | スクリーンリーダーが使用する非表示ボタンのアクセシブルラベルです。空白の場合、デフォルトで「Close」になります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="非表示ボタンの設定" }

ユーザーがバナーを非表示にすると、Campaignのターゲティング条件に引き続き該当していても、そのユーザーにはバナーが再度表示されません。

#### ステップ3.4: カスタムプロパティを追加する（オプション） {#custom-properties}

バナーにカスタムプロパティを追加して、文字列やJSONオブジェクトなどの構造化メタデータを添付できます。これらのプロパティはバナーの表示方法には影響しませんが、[Braze SDKを通じてアクセス]({{site.baseurl}}/developer_guide/banners/placements/)して、アプリの動作や外観を変更できます。たとえば、以下のことが可能です。

- サードパーティの分析や統合のためにメタデータを送信する。
- `timestamp`やJSONオブジェクトなどのメタデータを使用して条件付きロジックをトリガーする。
- `ratio`や`format`などの含まれるメタデータに基づいてバナーの動作を制御する。

カスタムプロパティを追加するには、**Settings** > **Properties** > **Add property** を選択します。

![バナーCampaignに最初のカスタムプロパティを追加するオプションを表示するプロパティページ。]({% image_buster /assets/img/banners/add_property.png %})

追加したいプロパティごとに、以下の項目を入力します。

| フィールド | 説明 | 例 |
|-------|-------------|---------|
| プロパティタイプ | プロパティのデータタイプです。サポートされるタイプには、文字列、ブール値、数値、タイムスタンプ、画像URL、JSONオブジェクトがあります。 | 文字列 |
| プロパティキー | プロパティの一意の識別子です。このキーはSDKでプロパティにアクセスするために使用されます。 | `color` |
| 値 | プロパティに割り当てられた値です。選択したプロパティタイプと一致する必要があります。 | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ3.4: カスタムプロパティを追加する（オプション）" }

完了したら、**Done** を選択します。

![キーがcolor、値が#FF0000の文字列プロパティを持つプロパティページ。]({% image_buster /assets/img/banners/example_property.png %})

### ステップ4: CampaignまたはCanvasの残りの部分を構築する {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

#### バナーの優先度を設定する（オプション） {#set-banner-priority-optional}

[バナーの優先度]({{site.baseurl}}/user_guide/channels/banners/#priority)は、同じプレースメントを共有するバナーの表示順序を決定します。優先度を手動で設定するには：

1. **正確な優先度を設定**を選択します。
2. Campaignsをドラッグ＆ドロップして正しい優先度に並べ替えます。
3. **Apply Sort** を選択します。

{% alert tip %}
同じプレースメントIDを使用する複数のバナーCampaignsがある場合は、ドラッグ＆ドロップの優先度ソーターを使用して正確な優先度を定義することをお勧めします。
{% endalert %}

#### 再適格性を設定する（オプション） {#re-eligibility}

デフォルトでは、バナーを非表示にしたユーザーはそのCampaignに再適格になることはありません。非表示にしたユーザーにバナーを再度表示させるには、**配信コントロール**ステップに移動し、**Allow users to become re-eligible to receive campaign** を選択します。有効にした場合、分、時間、日、または週単位でクールダウン期間を設定します。

カウントダウンは、ユーザーがバナーを非表示にした時点から開始されます。期間が経過すると、ユーザーは自動的に再適格になります。Campaignの再起動は不要です。再適格性はユーザーごと、Campaignごとに追跡されます。

#### オーディエンスを選択する {#choose-your-audience}

1. **ターゲットオーディエンス**で、Segmentsまたはフィルターを選択してオーディエンスを絞り込みます。おおよそのセグメント人口のプレビューが自動的に表示されます。正確なセグメントメンバーシップは、メッセージが送信される前に計算されます。

{% multi_lang_include target_audiences.md %}

{:start="2"}
2. **Assign Conversions** で、コンバージョンイベントを定義して、Campaignを受信した後にユーザーが特定のアクションを実行する頻度を追跡します。アクションをコンバージョンとしてカウントするための最大30日間の時間枠を設定できます。

#### コンバージョンイベントを選択する {#choose-conversion-events}

Brazeでは、Campaignを受信した後にユーザーが特定のアクションを実行する頻度である[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/)を追跡できます。ユーザーが指定されたアクションを実行した場合にコンバージョンとしてカウントされる最大30日間の時間枠を設定するオプションがあります。

{% endtab %}

{% tab Canvas %}

まだ完了していない場合は、Canvasコンポーネントの残りのセクションを完了してください。Canvasの残りの部分の構築方法、[多変量テスト]({{site.baseurl}}/user_guide/messaging/ab_testing/)や[インテリジェントセレクション]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/)の実装などの詳細については、Canvasドキュメントの[Canvasを構築する]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-3-build-your-canvas)ステップを参照してください。

CanvasバナーステップのCampaign再適格性を制御するには、Canvasの再エントリ設定を使用します。詳細については、[CampaignsとCanvasの再適格性]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/)を参照してください。

{% endtab %}
{% endtabs %}

### ステップ5: メッセージをテストする（オプション） {#step-5-test-your-message-optional}

{% multi_lang_include banners/testing.md page="campaigns" %}

### ステップ6: 確認してデプロイする {#step-6-review-and-deploy}

CampaignまたはCanvasの構築が完了したら、詳細を確認し、[テスト]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/)を行い、準備ができたら送信します。