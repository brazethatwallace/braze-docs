---
nav_title: "バナーを作成"
article_title: "バナーを作成"
page_order: 1
description: "このリファレンス記事では、Brazeのキャンペーンとキャンバスを使用してバナーを作成、構成、設定、送信する方法について説明します。"
tool:
  - Campaigns
channel:
  - banners
---

# バナーを作成 {#create-a-banner}

> Brazeでキャンペーンやキャンバスを構築する際にバナーを作成する方法を説明します。一般的な情報については、[バナーについて]({{site.baseurl}}/user_guide/channels/banners)を参照してください。

## 前提条件 {#prerequisites}

バナーを起動する前に、開発チームが[アプリまたはWebサイトにプレースメントを設定する]({{site.baseurl}}/developer_guide/banners/placements)必要があります。その間にバナーキャンペーンの下書きを作成することはできますが、プレースメントが設定されるまでキャンペーンを起動することはできません。

## バナーメッセージを作成する {#create-a-banner-message}

{% multi_lang_include banners/creating_placements.md section="user" %}

### ステップ2: メッセージの作成場所を選択する {#step-2-choose-where-to-build-your-message}

メッセージをキャンペーンとキャンバスのどちらで送信すべきかわからない場合は、キャンペーンは単一のターゲットメッセージングキャンペーンに適しており、キャンバスはマルチステップのユーザージャーニーに適しています。

{% tabs %}
{% tab キャンペーン %}

1. **メッセージング** > **キャンペーン**に移動し、**キャンペーンを作成**を選択します。
2. **Banner**を選択します。
3. キャンペーンにわかりやすく意味のある名前を付けます。
4. 必要に応じて[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)と[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)を追加します。タグを使用すると、キャンペーンを見つけやすくなり、レポートを作成しやすくなります。たとえば、レポートビルダーを使用する際に、関連するタグでフィルタリングできます。
5. 以前に作成したプレースメントを選択して、キャンペーンに関連付けます。
6. 必要に応じてバリアントを追加します。各バリアントに異なるメッセージタイプとレイアウトを選択できます。バリアントの詳細については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。
7. バナーキャンペーンの開始日時を選択します。デフォルトでは、バナーは無期限に継続します。**End Time**を選択して終了日時を指定することで、これを変更できます。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似している、または同じコンテンツを持つ場合は、追加のバリアントを追加する前にメッセージを作成してください。その後、**バリアントを追加**ドロップダウンから**バリアントからコピー**を選択できます。
{% endalert %}

{% endtab %}
{% tab キャンバス %}

1. キャンバスコンポーザーを使用して[キャンバスを作成]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)します。
2. キャンバスを設定した後、キャンバスビルダーでメッセージステップを追加します。ステップにわかりやすく意味のある名前を付けます。
3. メッセージングチャネルとして**Banner**を選択します。
4. バナーのプレースメントを選択します。
5. 優先度を設定します。[バナーの優先度]({{site.baseurl}}/user_guide/channels/banners#priority)は、同じプレースメントを共有するバナーの表示順序を決定します。
6. バナーの有効期限を設定します。ステップが利用可能になってからの期間、または特定の日時で設定できます。最大有効期限は、ステップがユーザーに利用可能になってから31日間です。

{% endtab %}
{% endtabs %}

### ステップ3: バナーを作成する {#compose-a-banner}

次に、作成方法を選択します。

- **ドラッグ＆ドロップエディター:** 空白のバナーから開始し、ブロックと行を使用して視覚的に構築します。
- **HTMLエディター:** 空白のバナーから開始し、HTMLで直接作業します。
- **テンプレート:** テンプレートライブラリを開き、**Brazeテンプレート**または**あなたのテンプレート**からデザインを選択します。テンプレートはドラッグ＆ドロップエディターで開き、カスタマイズできます。

![バナーのドラッグ＆ドロップエディター、HTMLエディター、またはテンプレートを選択するオプション。]({% image_buster /assets/img/banners/choose_banner_editing_experience.png %})

#### ステップ3.1: バナーのスタイルを設定する {#step-31-style-the-banner}

{% tabs %}
{% tab ドラッグ＆ドロップエディター %}

ブロックと行をキャンバスエリアにドラッグ＆ドロップして、メッセージの作成を開始できます。バナーエディターのブロックと共有プロパティの詳細へのリンクについては、[エディターブロック（バナー）]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=banners)を参照してください。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

メッセージの背景プロパティ、ボーダー設定などをカスタマイズするには、**Styles**を選択します。特定のブロックまたは行のスタイルのみをカスタマイズしたい場合は、それを選択して変更を加えます。

![バナーコンポーザーのスタイルパネル。]({% image_buster /assets/img/banners/banner_card_styles.png %})

{% endtab %}
{% tab HTMLエディター %}

HTMLエディターは、独自のHTMLテンプレートをすでに管理しているチームや、マークアップとスタイリングを完全にコントロールしたいチームに最適です。カスタムHTMLをエディターに直接記述または貼り付けることができます。Liquidパーソナライゼーションタグは完全にサポートされているため、ユーザー属性、カスタム属性、カタログアイテムなどを参照できます。

{% alert tip %}
バナーHTMLの作成にサポートが必要ですか？HTMLエディターで**Ask Operator**を選択し、作成したいバナーを説明してください。[BrazeAI<sup>TM</sup> Operator]({{site.baseurl}}/user_guide/brazeai/operator)がHTMLを生成し、確認してエディターに挿入できます。詳細については、[メッセージを生成する]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-messages)を参照してください。
{% endalert %}

カスタムHTMLでのクリックおよび非表示のトラッキングには、JavaScriptブリッジメソッドを明示的に呼び出す必要があります。完全なリファレンスについては、[バナーのカスタムコードとJavaScriptブリッジ]({{site.baseurl}}/user_guide/channels/banners/custom_code)を参照してください。

{% endtab %}
{% endtabs %}

{% alert note %}
単一のバナーキャンペーン内で異なる言語のユーザーをターゲットにするには、[多言語メッセージ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)を参照してください。
{% endalert %}

#### ステップ3.2: クリック時の動作を定義する（オプション） {#step-32-define-on-click-behavior-optional}

{% tabs %}
{% tab ドラッグ＆ドロップエディター %}

ユーザーがバナー内のリンクをクリックした際に、アプリ内のより深い場所に移動させるか、別のWebページにリダイレクトさせるかを選択できます。さらに、[カスタム属性またはイベントを記録する]({{site.baseurl}}/developer_guide/analytics)ことを選択でき、ユーザーがバナーをクリックした際にカスタムデータでユーザーのプロファイルを更新します。より詳細なクリックトラッキングのために、プロパティパネルの**Identifier for Reporting**フィールドを使用して、各インタラクティブ要素にカスタム識別子を割り当てます。

{% alert important %}
{::nomarkdown}
特定の要素（バナーのボタン、リンク、画像など）に独自のクリック時の動作がある場合、クリック時の動作はオーバーライドされることがあります。たとえば、以下のクリック時の動作がある場合：<br><ul><li>バナーにはWebサイトのホームページにリダイレクトするクリック時の動作があります。</li><li>バナー内の画像にはWebサイトの製品ページにリダイレクトするクリック時の動作があります。</li></ul>ユーザーが画像をクリックすると、製品ページにリダイレクトされます。ただし、バナーの周囲のエリアをクリックすると、ホームページにリダイレクトされます。
{:/}
{% endalert %}

{% endtab %}
{% tab HTMLエディター %}

HTMLエディターでは、クリックトラッキングは自動ではありません。トラッキングしたい各クリック可能な要素に対して、HTML内から`brazeBridge.logClick()`を呼び出す必要があります。例：

```html
<a href="https://example.com" onclick="brazeBridge.logClick()">Shop now</a>
```

完全なJavaScriptブリッジリファレンスについては、[バナーのカスタムコードとJavaScriptブリッジ]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge)を参照してください。

{% endtab %}
{% endtabs %}

#### ステップ3.3: 非表示の動作を設定する（オプション） {#dismiss-behavior}

{% tabs %}
{% tab ドラッグ＆ドロップエディター %}

**Dismiss behavior**セクションの**Banner can be dismissed**チェックボックスを選択すると、ユーザーがバナーを非表示にできるようになります。このオプションは、幅広いオーディエンスに期間限定のオファーを宣伝したいが、興味のないユーザーにはメッセージを非表示にできるようにしたい場合に便利です。

非表示が有効になっている場合、**Dismiss behavior**セクションで非表示ボタンをカスタマイズできます。

| 設定 | 説明 |
|---------|-------------|
| **ボタンサイズ** | バナーに表示される非表示ボタンのサイズです。 |
| **ボタンの色** | 非表示ボタンの色です。 |
| **ARIAラベル** | スクリーンリーダーが使用する非表示ボタンのアクセシブルラベルです。空白の場合、デフォルトで「Close」になります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="非表示ボタンの設定" }

ユーザーがバナーを非表示にすると、キャンペーンのターゲティング条件に引き続き該当していても、そのユーザーにはバナーが再度表示されません。

{% endtab %}
{% tab HTMLエディター %}

HTMLエディターでは、非表示はHTML内で`brazeBridge.closeMessage()`を使用して処理されます。`brazeBridge.logClick()`と組み合わせることで、非表示アクションをクリックイベントとしてもトラッキングできます。例：

```html
<a href="#" onclick="brazeBridge.logClick(); brazeBridge.closeMessage();">&#x2715; Close</a>
```

この方法でユーザーがバナーを非表示にすると、キャンペーンのターゲティング条件に引き続き該当していても、そのユーザーにはバナーが再度表示されません。

完全なJavaScriptブリッジリファレンスについては、[バナーのカスタムコードとJavaScriptブリッジ]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge)を参照してください。

{% endtab %}
{% endtabs %}

#### ステップ3.4: カスタムプロパティを追加する（オプション） {#custom-properties}

バナーにカスタムプロパティを追加して、文字列やJSONオブジェクトなどの構造化メタデータを添付できます。これらのプロパティはバナーの表示方法には影響しませんが、[Braze SDKを通じてアクセス]({{site.baseurl}}/developer_guide/banners/placements)して、アプリの動作や外観を変更できます。たとえば、以下のことが可能です。

- サードパーティの分析や統合のためにメタデータを送信する。
- `timestamp`やJSONオブジェクトなどのメタデータを使用して条件付きロジックをトリガーする。
- `ratio`や`format`などの含まれるメタデータに基づいてバナーの動作を制御する。

カスタムプロパティはドラッグ＆ドロップエディターとHTMLエディターの両方で同じように機能します。カスタムプロパティを追加するには、**設定** > **Properties** > **Add property**を選択します。

![バナーキャンペーンに最初のカスタムプロパティを追加するオプションを表示するプロパティページ。]({% image_buster /assets/img/banners/add_property.png %})

追加したいプロパティごとに、以下の項目を入力します。

| フィールド | 説明 | 例 |
|-------|-------------|---------|
| プロパティタイプ | プロパティのデータタイプです。サポートされるタイプには、文字列、ブール値、数値、タイムスタンプ、画像URL、JSONオブジェクトがあります。 | 文字列 |
| プロパティキー | プロパティの一意の識別子です。このキーはSDKでプロパティにアクセスするために使用されます。 | `color` |
| 値 | プロパティに割り当てられた値です。選択したプロパティタイプと一致する必要があります。 | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="カスタムプロパティの追加" }

完了したら、**Done**を選択します。

![キーがcolor、値が#FF0000の文字列プロパティを持つプロパティページ。]({% image_buster /assets/img/banners/example_property.png %})

### ステップ4: キャンペーンまたはキャンバスの残りの部分を構築する {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab キャンペーン %}

#### バナーの優先度を設定する（オプション） {#set-banner-priority-optional}

[バナーの優先度]({{site.baseurl}}/user_guide/channels/banners#priority)は、同じプレースメントを共有するバナーの表示順序を決定します。優先度を手動で設定するには：

1. **Set exact priority**を選択します。
2. キャンペーンをドラッグ＆ドロップして正しい優先度に並べ替えます。
3. **Apply Sort**を選択します。

{% alert tip %}
同じプレースメントIDを使用する複数のバナーキャンペーンがある場合は、ドラッグ＆ドロップの優先度ソーターを使用して正確な優先度を定義することをお勧めします。
{% endalert %}

#### 再適格性を設定する（オプション） {#re-eligibility}

デフォルトでは、バナーを非表示にしたユーザーはそのキャンペーンに再適格になることはありません。非表示にしたユーザーにバナーを再度表示させるには、**配信コントロール**ステップに移動し、**ユーザーがキャンペーンを再度受信できるようにする**を選択します。有効にした場合、分、時間、日、または週単位でクールダウン期間を設定します。

カウントダウンは、ユーザーがバナーを非表示にした時点から開始されます。期間が経過すると、ユーザーは自動的に再適格になります。キャンペーンの再起動は不要です。再適格性はユーザーごと、キャンペーンごとに追跡されます。

#### オーディエンスを選択する {#choose-your-audience}

1. **ターゲットオーディエンス**で、セグメントまたはフィルターを選択してオーディエンスを絞り込みます。おおよそのセグメント人口のプレビューが自動的に表示されます。正確なセグメントメンバーシップは、メッセージが送信される前に計算されます。

{% multi_lang_include audience/target_audiences.md %}

{:start="2"}
2. **コンバージョンの割り当て**で、コンバージョンイベントを定義して、キャンペーンを受信した後にユーザーが特定のアクションを実行する頻度を追跡します。アクションをコンバージョンとしてカウントするための最大30日間の時間枠を設定できます。

#### コンバージョンイベントを選択する {#choose-conversion-events}

Brazeでは、キャンペーンを受信した後にユーザーが特定のアクションを実行する頻度である[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)を追跡できます。ユーザーが指定されたアクションを実行した場合にコンバージョンとしてカウントされる最大30日間の時間枠を設定するオプションがあります。

{% endtab %}

{% tab キャンバス %}

まだ完了していない場合は、キャンバスコンポーネントの残りのセクションを完了してください。キャンバスの残りの部分の構築方法、[多変量テスト]({{site.baseurl}}/user_guide/messaging/ab_testing)や[インテリジェントセレクション]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection)の実装などの詳細については、キャンバスドキュメントの[キャンバスを構築する]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-3-build-your-canvas)ステップを参照してください。

キャンバスのバナーステップの再適格性を制御するには、キャンバスの再エントリ設定を使用します。詳細については、[キャンペーンとキャンバスの再適格性]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)を参照してください。

{% endtab %}
{% endtabs %}

### ステップ5: メッセージをテストする（オプション） {#step-5-test-your-message-optional}

{% multi_lang_include banners/testing.md page="campaigns" %}

### ステップ6: 確認してデプロイする {#step-6-review-and-deploy}

キャンペーンまたはキャンバスの構築が完了したら、詳細を確認し、[テスト]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages)を行い、準備ができたら送信します。