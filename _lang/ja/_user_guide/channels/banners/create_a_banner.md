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

バナーを公開する前に、開発チームが[アプリまたはWebサイトにプレースメントを設定する]({{site.baseurl}}/developer_guide/banners/placements)必要があります。その間にバナーキャンペーンの下書きを作成することはできますが、プレースメントが設定されるまでキャンペーンを公開することはできません。

## バナーメッセージの作成 {#create-a-banner-message}

{% multi_lang_include banners/creating_placements.md section="user" %}

### ステップ2:メッセージの作成場所を選択する {#step-2-choose-where-to-build-your-message}

メッセージをキャンペーンで送信するか、キャンバスで送信するかお悩みですか？キャンペーンは単一のターゲットメッセージングに適しており、キャンバスは複数ステップのユーザージャーニーに適しています。

{% tabs %}
{% tab キャンペーン %}

1. **メッセージング** > **キャンペーン** に移動し、**キャンペーンを作成** を選択します。
2. **バナー** を選択します。
3. キャンペーンに明確でわかりやすい名前を付けます。
4. 必要に応じて[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)と[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)を追加します。タグを使うとキャンペーンの検索やレポート作成が容易になります。たとえば、レポートビルダーを使用する際に関連するタグでフィルターできます。
5. 事前に作成したプレースメントを選択して、キャンペーンに関連付けます。
6. 必要に応じてバリアントを追加します。各バリアントに異なるメッセージタイプとレイアウトを選択できます。バリアントの詳細については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。
7. バナーキャンペーンの開始日時を選択します。デフォルトでは、バナーは無期限に継続します。**終了時間** を選択して終了日時を指定することで変更できます。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似している、または同じコンテンツを持つ場合は、追加のバリアントを加える前にメッセージを作成してください。その後、**バリアントを追加** ドロップダウンから **バリアントからコピー** を選択できます。
{% endalert %}

{% endtab %}
{% tab キャンバス %}

1. キャンバスコンポーザーを使用して[キャンバスを作成]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)します。
2. キャンバスの設定が完了したら、キャンバスビルダーでメッセージステップを追加します。ステップに明確でわかりやすい名前を付けます。
3. メッセージングチャネルとして **バナー** を選択します。
4. バナーのプレースメントを選択します。
5. 優先度を設定します。[バナーの優先度]({{site.baseurl}}/user_guide/channels/banners#priority)は、同じプレースメントを共有するバナーの表示順序を決定します。
6. バナーの有効期限を設定します。ステップが利用可能になってからの期間、または特定の日時で設定できます。最大有効期限はステップがユーザーに利用可能になってから31日間です。

{% endtab %}
{% endtabs %}

### ステップ3:バナーを作成する {#compose-a-banner}

次に、作成方法を選択します。

- **ドラッグ＆ドロップエディター:** 空白のバナーから始めて、ブロックと行を使ってビジュアルに構築します。
- **HTMLエディター:** 空白のバナーから始めて、HTMLで直接作業します。
- **テンプレート:** テンプレートライブラリを開き、**Brazeテンプレート** または **マイテンプレート** からデザインを選択します。テンプレートはドラッグ＆ドロップエディターで開かれ、カスタマイズできます。

![バナーのドラッグ＆ドロップエディター、HTMLエディター、またはテンプレートを選択するオプション。]({% image_buster /assets/img/banners/choose_banner_editing_experience.png %})

#### ステップ3.1:バナーのスタイルを設定する {#step-31-style-the-banner}

{% tabs %}
{% tab ドラッグ＆ドロップエディター %}

ブロックと行をキャンバスエリアにドラッグ＆ドロップしてメッセージの構築を開始します。バナーエディターのブロックと共有プロパティの詳細についてのリファレンスは、[エディターブロック（バナー）]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=banners)を参照してください。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

メッセージの背景プロパティ、ボーダー設定などをカスタマイズするには、**スタイル** を選択します。特定のブロックまたは行のスタイルのみをカスタマイズしたい場合は、それを選択して変更を行います。

![バナーコンポーザーのスタイルパネル。]({% image_buster /assets/img/banners/banner_card_styles.png %})

{% multi_lang_include drag_and_drop/hide_rows_and_blocks_by_device.md channel='banner' %}

{% endtab %}
{% tab HTMLエディター %}

HTMLエディターは、すでに独自のHTMLテンプレートを管理しているチームや、マークアップとスタイリングを完全にコントロールしたいチームに最適です。カスタムHTMLを直接エディターに記述またはペーストできます。Liquidパーソナライゼーションタグは完全にサポートされているため、ユーザー属性、カスタム属性、カタログアイテムなどを参照できます。

{% alert tip %}
バナーHTMLの構築にサポートが必要ですか？HTMLエディターで **Ask Operator** を選択し、必要なバナーを説明してください。[BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator)がHTMLを生成し、レビューしてエディターに挿入できます。詳細については、[メッセージを生成する]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-messages)を参照してください。
{% endalert %}

カスタムHTMLでのクリックおよび閉じるアクションのトラッキングには、JavaScriptブリッジメソッドを明示的に呼び出す必要があります。完全なリファレンスについては、[バナーのカスタムコードとJavaScriptブリッジ]({{site.baseurl}}/user_guide/channels/banners/custom_code)を参照してください。

{% endtab %}
{% endtabs %}

{% alert note %}
単一のバナーキャンペーン内で異なる言語のユーザーをターゲットにするには、[多言語メッセージ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)を参照してください。
{% endalert %}

#### ステップ3.2:クリック時の動作を定義する（オプション） {#step-32-define-on-click-behavior-optional}

{% tabs %}
{% tab ドラッグ＆ドロップエディター %}

ユーザーがバナー内のリンクをクリックすると、アプリ内のより深い階層に誘導したり、別のWebページにリダイレクトしたりすることを選択できます。さらに、[カスタム属性またはイベントを記録する]({{site.baseurl}}/developer_guide/analytics)ことを選択でき、ユーザーがバナーをクリックした際にカスタムデータでユーザーのプロファイルを更新します。より詳細なクリックトラッキングを行うには、プロパティパネルの **レポート用識別子** フィールドを使用して、各インタラクティブ要素にカスタム識別子を割り当てます。

{% alert important %}
{::nomarkdown}
特定の要素（バナーのボタン、リンク、画像など）に独自のクリック時の動作がある場合、クリック時の動作はオーバーライドされることがあります。たとえば、以下のクリック時の動作が設定されている場合:<br><ul><li>バナーには、Webサイトのホームページにリダイレクトするクリック時の動作があります。</li><li>バナー内の画像には、Webサイトの商品ページにリダイレクトするクリック時の動作があります。</li></ul>ユーザーが画像をクリックすると、商品ページにリダイレクトされます。ただし、バナーの周囲のエリアをクリックすると、ホームページにリダイレクトされます。
{:/}
{% endalert %}

{% endtab %}
{% tab HTMLエディター %}

HTMLエディターでは、クリックトラッキングは自動ではありません。トラッキングしたいクリック可能な要素ごとに、HTML内から `brazeBridge.logClick()` を呼び出す必要があります。例:

```html
<a href="https://example.com" onclick="brazeBridge.logClick()">Shop now</a>
```

完全なJavaScriptブリッジリファレンスについては、[バナーのカスタムコードとJavaScriptブリッジ]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge)を参照してください。

{% endtab %}
{% endtabs %}

#### ステップ3.3:閉じる動作を設定する（オプション）{#dismiss-behavior}

{% alert important %}
バナーの閉じる機能には、以下の最小SDKバージョンが必要です。古いSDKバージョンでは、閉じる機能が有効なバナーはレンダリングされません。
{% sdk_min_versions swift:14.1.0 android:42.1.0 web:6.7.1 reactnative:22.0.0 flutter:20.0.0 %}
{% endalert %}

{% tabs %}
{% tab ドラッグ＆ドロップエディター %}

**閉じる動作** セクションで **バナーを閉じることができる** チェックボックスを選択すると、ユーザーがバナーを閉じることを許可できます。これは、期間限定オファーを広いオーディエンスに宣伝しつつ、興味のないユーザーにはメッセージを非表示にさせたい場合に便利です。

閉じる機能がオンの場合、**閉じる動作** セクションで閉じるボタンをカスタマイズできます。

| 設定 | 説明 |
|---------|-------------|
| **ボタンサイズ** | バナーに表示される閉じるボタンのサイズ。 |
| **ボタンの色** | 閉じるボタンの色。 |
| **ARIAラベル** | 閉じるボタンのアクセシブルなラベルで、スクリーンリーダーが使用します。空白の場合、デフォルトは「Close」です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="閉じるボタンの設定" }

ユーザーがバナーを閉じると、キャンペーンのターゲット条件に引き続き該当していても、そのユーザーにはバナーが再度表示されません。

{% endtab %}
{% tab HTMLエディター %}

HTMLエディターでは、閉じる動作はHTML内で `brazeBridge.closeMessage()` を使用して処理されます。閉じるアクションをクリックイベントとしてもトラッキングするには、`brazeBridge.logClick()` と組み合わせます。例:

```html
<a href="#" onclick="brazeBridge.logClick(); brazeBridge.closeMessage();">&#x2715; Close</a>
```

この方法でユーザーがバナーを閉じると、キャンペーンのターゲット条件に引き続き該当していても、そのユーザーにはバナーが再度表示されません。

完全なJavaScriptブリッジリファレンスについては、[バナーのカスタムコードとJavaScriptブリッジ]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge)を参照してください。

{% endtab %}
{% endtabs %}

#### ステップ3.4:カスタムプロパティを追加する（オプション）{#custom-properties}

バナーにカスタムプロパティを追加して、文字列やJSONオブジェクトなどの構造化メタデータを付与できます。これらのプロパティはバナーの表示には影響しませんが、[Braze SDKを通じてアクセス]({{site.baseurl}}/developer_guide/banners/placements)してアプリの動作や外観を変更できます。たとえば、以下のようなことが可能です。

{% multi_lang_include banners/metadata_use_cases.md %}

カスタムプロパティはドラッグ＆ドロップエディターとHTMLエディターの両方で同じように機能します。カスタムプロパティを追加するには、**設定** > **プロパティ** > **プロパティを追加** を選択します。

![最初のカスタムプロパティをバナーキャンペーンに追加するオプションが表示されているプロパティページ。]({% image_buster /assets/img/banners/add_property.png %})

追加したい各プロパティについて、以下を入力します。

| フィールド | 説明 | 例 |
|-------|-------------|---------|
| プロパティタイプ | プロパティのデータ型。サポートされる型には、文字列、ブール値、数値、タイムスタンプ、画像URL、JSONオブジェクトがあります。 | 文字列 |
| プロパティキー | プロパティの一意の識別子。このキーはSDKでプロパティにアクセスする際に使用されます。 | `color` |
| 値 | プロパティに割り当てられた値。選択したプロパティタイプと一致する必要があります。 | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ3.4:カスタムプロパティを追加する（オプション）" }

完了したら、**完了** を選択します。

![colorというキーと#FF0000という値を持つ文字列プロパティが表示されているプロパティページ。]({% image_buster /assets/img/banners/example_property.png %})

#### ステップ3.5:Connected Contentでパーソナライズする（オプション） {#step-35-personalize-with-connected-content-optional}

{% multi_lang_include alerts/early_access_beta_alert.md feature='Connected Content for Banners' %}

バナーはセッションリフレッシュ時にインラインでレンダリングされるため、このチャネルのConnected Contentは他のチャネルとは異なる動作をします。

- GETリクエストのみサポートされています。
- 1回のリフレッシュ内のすべてのプレースメント（最大10）は、約2秒のレンダリング予算を共有します。呼び出しが遅い場合、タイムアウトした場合、または予算を超過した場合、そのプレースメントのConnected Contentの結果はnullとして扱われます。バナーはリトライしません。

最良の結果を得るために:

- エンドポイントを高速に保ち、可能な限り[レスポンスをキャッシュ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses)してください。
- 同時にレンダリングされるプレースメント全体で、一意のConnected Content URLの数を制限してください。
- あるConnected Contentのレスポンスが次のURLを決定するような呼び出しのチェーンは避けてください。追加の呼び出しごとに共有予算が消費されます。
- Liquidガードステートメントまたは[`default`フィルター]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values)を使用して、null結果を処理し、空のバナーを避けてください。

### ステップ4:キャンペーンまたはキャンバスの残りの部分を構築する {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab キャンペーン %}

#### バナーの優先度を設定する（オプション） {#set-banner-priority-optional}

[バナーの優先度]({{site.baseurl}}/user_guide/channels/banners#priority)は、同じプレースメントを共有するバナーの表示順序を決定します。優先度を手動で設定するには:

1. **正確な優先度を設定** を選択します。
2. キャンペーンをドラッグ＆ドロップして正しい優先順位に並べ替えます。
3. **ソートを適用** を選択します。

{% alert tip %}
同じプレースメントIDを使用する複数のバナーキャンペーンがある場合は、ドラッグ＆ドロップの優先度ソーターを使用して正確な優先度を定義することをお勧めします。
{% endalert %}

#### 再適格性を設定する（オプション）{#re-eligibility}

デフォルトでは、バナーを閉じたユーザーはそのキャンペーンに対して再適格になりません。閉じたユーザーにバナーを再度表示させるには、**配信制御** ステップに移動し、**ユーザーがキャンペーンを再度受信できるようにする** を選択します。有効にした場合は、分、時間、日、または週単位でクールダウン期間を設定します。

カウントダウンはユーザーがバナーを閉じた時点から開始されます。期間が終了すると、ユーザーは自動的に再適格になります。キャンペーンの再起動は不要です。再適格性はユーザーごと、キャンペーンごとにトラッキングされます。

#### オーディエンスを選択する {#choose-your-audience}

1. **ターゲットオーディエンス** で、セグメントまたはフィルターを選択してオーディエンスを絞り込みます。おおよそのセグメント人数のプレビューが自動的に表示されます。正確なセグメントメンバーシップは、メッセージの送信前に計算されます。

{% multi_lang_include audience/target_audiences.md %}

{:start="2"}
2. **コンバージョンの割り当て** で、コンバージョンイベントを定義して、ユーザーがキャンペーンを受信した後に特定のアクションを実行する頻度をトラッキングします。アクションをコンバージョンとしてカウントするために最大30日間の期間を設定できます。

#### コンバージョンイベントを選択する {#choose-conversion-events}

Brazeでは、[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)、つまりユーザーがキャンペーンを受信した後に特定のアクションを実行する頻度をトラッキングできます。ユーザーが指定されたアクションを取った場合にコンバージョンとしてカウントする最大30日間の期間を設定するオプションがあります。

{% endtab %}

{% tab キャンバス %}

まだ完了していない場合は、キャンバスコンポーネントの残りのセクションを完成させてください。キャンバスの残りの部分の構築（多変量テストや[BrazeAI<sup>TM</sup>で最適化]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai)を含む）の詳細については、[キャンバスを構築する]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas)を参照してください。

キャンバスのバナーステップの再適格性を制御するには、キャンバスの再エントリ設定を使用します。詳細については、[キャンペーンとキャンバスの再適格性]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)を参照してください。

{% endtab %}
{% endtabs %}

### ステップ5:メッセージをテストする（オプション） {#step-5-test-your-message-optional}

{% multi_lang_include banners/testing.md page="campaigns" %}

### ステップ6:確認してデプロイする {#step-6-review-and-deploy}

キャンペーンまたはキャンバスの構築が完了したら、詳細を確認し、[テスト]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages)を行い、準備ができたら送信します。