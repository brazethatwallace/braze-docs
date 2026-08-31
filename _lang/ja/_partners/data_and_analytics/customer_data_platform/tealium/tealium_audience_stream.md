---
nav_title: Tealium AudienceStream
article_title: Tealium AudienceStream
page_order: 2
alias: /partners/tealium_audience_stream/
description: "このリファレンス記事では、BrazeとTealiumのパートナーシップについて説明します。Tealiumは、モバイルデータ、Webデータ、代替データを他のサードパーティソースに接続できるユニバーサルデータハブです。"
page_type: partner
search_tag: Partner

---

# Tealium AudienceStream

> Tealium [AudienceStream](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/introduction/)は、オムニチャネルの顧客セグメンテーションおよびリアルタイムアクションエンジンです。AudienceStreamはEventStreamに流入するデータを取得し、ブランドとの顧客エンゲージメントの最も重要な属性を表す訪問者プロファイルを作成します。

BrazeとTealiumの統合では、AudienceStreamの訪問者プロファイルを活用します。共有された行動によりこれらのプロファイルがセグメント化され、オーディエンスと呼ばれる共通の特徴を持つ訪問者のセットが作成されます。これらのオーディエンスは、コネクターを介してリアルタイムでマーケティングテクノロジースタックにデータを提供できます。

{% alert important %}
TealiumのAudienceStreamsとEventStreamsは、バッチと非バッチの両方のコネクターアクションを提供します。非バッチコネクターは、リアルタイムリクエストがユースケースにとって重要であり、BrazeのAPIレート制限仕様に達する懸念がない場合に使用してください。ご質問がある場合は、Braze[サポート]({{site.baseurl}}/braze_support)またはカスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## 前提条件 {#prerequisites}

| 名前 | 説明 |
| ---- | ----------- |
| Tealiumアカウント | サーバーサイドアクセスが可能な[Tealiumアカウント](https://my.tealiumiq.com/)が必要です。このパートナーシップを最大限に活用するために、クライアントサイドのインテグレーションも併用することをお勧めします。 |
| REST APIキー | `users.track`、`users.delete`、`subscription.status.set`の権限を持つBraze REST APIキー。<br><br>これは、**Brazeダッシュボード > 開発者コンソール > REST APIキー > 新しいAPIキーを作成**で作成できます。|
| [Braze RESTエンドポイント]({{site.baseurl}}/api/basics#endpoints) | RESTエンドポイントURL。エンドポイントは、[お使いのインスタンスのBraze URL]({{site.baseurl}}/api/basics#endpoints)に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## インテグレーション {#integration}

### ステップ1:属性とバッジを設定する {#step-1-set-up-attributes-and-badges}

#### 属性について {#understanding-attributes}

AudienceStream を使用する最初のステップは、属性を作成することです。属性を使用すると、訪問者の習慣、好み、アクション、ブランドとのエンゲージメントを表す重要な特性を定義できます。

**訪問属性**:訪問属性は、ユーザーの現在の訪問（またはセッション）に関連します。これらの属性に保存されたデータは、訪問の期間中保持されます。訪問属性の例を以下に示します:
- 訪問時間 (Number)
- 現在のブラウザー (String)
- 現在のデバイス (String)
- ページビュー数 (Number)

**訪問者属性**:訪問者属性は、現在のユーザーに関連します。これらの属性に保存されたデータは、ユーザーの生涯を通じて保持されます。訪問者属性の例を以下に示します:
- 生涯注文額 (Number)
- 名 (String)
- 生年月日 (Date)
- 購入ブランド (Tally)

利用可能なデータタイプの完全なリストについては、[Tealium](https://docs.tealium.com/server-side/attributes/about/) をご覧ください。

##### 属性エンリッチメント {#attribute-enrichment}

目的の属性を特定したら、[エンリッチメント](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/attributes-enrichments/)を使用してそれらを構成できます。エンリッチメントは、属性の値をいつ、どのように更新するかを決定するビジネスルールです。各データタイプには、属性の値を操作するためのエンリッチメントの選択肢が用意されています。これは「WHEN」設定に関連付けられています。各訪問属性および訪問者属性で使用できるオプションは以下のとおりです:

- New Visitor: 訪問者が初めてサイトにアクセスしたときに発生します。
- New Visit: 訪問者による新しい訪問時に発生します。
- Any Event: 任意のイベントで発生します。
- Visit Ended: 訪問が終了したときに発生します。

エンリッチメントがいつ発生するかを決定するカスタム条件（ルールと呼ばれます）を作成することもできます。

#### バッジ {#badges}

バッジは、価値のある行動パターンを表す特別な訪問者属性です。バッジは、エンリッチメントのロジックに基づいて訪問者に割り当てまたは削除されます。このロジックは通常、訪問者セグメントをキャプチャするための複数の条件を組み合わせたり、特定の値に達したときのしきい値を設定したりします。

#### 属性とバッジの例 {#attribute-and-badge-example}

{% tabs local %}
{% tab 属性 %}

訪問者属性「Lifetime Order Value」を作成し、完了したすべての注文（購入イベント）について顧客が支出した累計金額（`order_total`）を計算します。Tealium アカウントで生涯注文額を設定するには、以下の手順に従ってください:

1. **AudienceStream > Visitor/Visit Attributes** に移動し、**Add Attribute** をクリックします。
2. スコープとして **Visitor** を選択し、**Continue** をクリックします。
3. データタイプ **Number** を選択し、**Continue** をクリックします。
4. 属性の名前「Lifetime Order Value」を入力します。
5. **Add Enrichment** をクリックし、**Increment or Decrement Number** を選択します。
6. インクリメントする値を含む属性（`order_total`）を選択します。
7. 「WHEN」を「Any Event」のままにして、**Create a New Rule** をクリックします。
8. 購入イベントが発生したことを識別するルールを作成します。
9. **Save** をクリックし、次に **Finish** をクリックします。

これで、すべての顧客に生涯注文額の属性が紐付けられます。

{% endtab %}
{% tab バッジ %}

バッジを作成して、共有する特定の属性によってユーザーを分類およびターゲティングできます。以下の例では、「Lifetime Order Value」が500ドル以上のユーザーに対して VIP バッジを作成します。

1. **AudienceStream > Visitor/Visit Attributes** に移動し、**Add Attribute** をクリックします。
2. スコープとして **Visitor** を選択し、**Continue** をクリックします。
3. データタイプ **Badge** を選択し、**Continue** をクリックします。
4. バッジの名前「VIP」を入力します。
5. **Add Enrichment** をクリックし、**Assign Badge** を選択します。
6. 「WHEN」を「Any Event」のままにします。
7. **Create Rule** を選択してバッジ割り当てのルールを作成します。このルールにタイトルを割り当て、前に作成した属性を使用して、ルールを「...has attribute "Lifetime Order Value greater than 500"」に設定します。
8. **Save** をクリックし、次に **Finish** をクリックします。

{% endtab %}
{% endtabs %}

### ステップ2:オーディエンスを作成する {#step-2-create-an-audience}

Tealium のホームページで、サイドバーナビゲーションから **AudienceStream** の下にある **Audiences** を選択します。ここで、共通の属性を持つユーザーのオーディエンスを作成できます。このオーディエンスへのユーザーの入退出が、次のステップで設定するコネクターアクションのトリガーとなり、この情報を Braze のユーザープロファイルに渡します。

まず、オーディエンスに名前を付け、作成しようとしているオーディエンスのタイプに適用される属性を検討します。たとえば、VIP ユーザーのオーディエンスを作成するには、**VIP バッジ**を持つ訪問者のオーディエンスを作成できます。

完了したら、オーディエンスを **Save / Publish** してください。

### ステップ3:イベントコネクターを作成する {#step-3-create-an-event-connector}

コネクターは、Tealium と別のベンダー間のインテグレーションであり、データの送信に使用されます。これらのコネクターには、パートナーがサポートする API を表すアクションが含まれています。

1. Tealium のサイドバーで **Server-Side** の下にある **AudienceStream > Audience Connectors** に移動します。
2. 青い **+ Add Connector** ボタンを選択して、コネクターマーケットプレイスを参照します。表示される新しいダイアログボックスで、スポットライト検索を使用して **Braze** コネクターを見つけます。
3. このコネクターを追加するには、**Braze** コネクタータイルをクリックします。クリックすると、接続の概要、必要な情報のリスト、サポートされているアクション、および設定手順を確認できます。設定は、ソース、設定、アクションの3つのステップで構成されます。

#### ソース {#source}

表示される **Source** ダイアログで、前のステップで作成したオーディエンスと、状況に適したトリガーを選択します。また、頻度キャップをオンに切り替えて、このアクションがトリガーされる頻度を制御することもできます。

![オーディエンスとトリガーの選択を含む Tealium AudienceStream コネクターのソース設定。]({% image_buster /assets/img/tealium/create_source.png %}){: style="max-width:90%;"}

#### 設定 {#configuration}

次に、**Configuration** ダイアログが表示されます。ページ下部の **Add Connector** を選択します。コネクターに名前を付け、Braze API エンドポイントと Braze REST APIキーを入力します。

![Braze エンドポイントと REST APIキーのフィールドを含む Tealium コネクター設定ダイアログ。]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

以前にコネクターを作成したことがある場合は、利用可能なコネクターリストから既存のものを使用し、鉛筆アイコンでニーズに合わせて変更するか、ゴミ箱アイコンで削除できます。

このオーディエンスにリンクするコネクターを作成または選択した後、Done をクリックして続行します。

#### アクション {#action}

次に、コネクターアクションに名前を付け、設定するマッピングに従ってデータを送信するアクションタイプを選択します。ここで、Braze の属性を Tealium の属性名にマッピングします。選択するアクションタイプによって、Tealium が必要とするフィールドの選択肢が異なります。以下に、これらのフィールドの例と説明を示します。

{% alert important %}
提供されるすべてのフィールドが必須というわけではありません。

![最小化できるオプションフィールドを表示する Tealium のアクションマッピングパネル。]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab ユーザーの追跡 - バッチおよび非バッチ %}

このアクションでは、ユーザー、イベント、および購入属性を1つのアクションですべて追跡できます。Track User アクションは AudienceStream と EventStream の両方で同じですが、Tealium ではユーザー属性マッピングを AudienceStream アクションで設定し、イベントおよび購入マッピングを EventStream アクションで設定することを推奨しています。

| パラメーター | 説明 |
| ---------- | ----------- |
| ユーザー ID | このフィールドを使用して、Tealium のユーザー ID フィールドを Braze の対応するフィールドにマッピングします。1つ以上のユーザー ID 属性をマッピングします。複数の ID が指定された場合、最初の空でない値が以下の優先順位に基づいて選択されます: External ID、Braze ID、Alias Name、Alias Label。<br><br>- プッシュトークンをインポートする場合、External ID と Braze ID は指定しないでください。<br>- ユーザーエイリアスを指定する場合は、エイリアス名とエイリアスラベルの両方を設定する必要があります。<br><br>詳細については、Braze の[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)をご覧ください。 |
| ユーザー属性 | 既存の Braze ユーザープロファイルフィールド名を使用して、Braze ダッシュボードのユーザープロファイル値を更新するか、独自のカスタム[ユーザー属性]({{site.baseurl}}/api/objects_filters/user_attributes_object)データをユーザープロファイルに追加します。<br><br>- デフォルトでは、ユーザーが存在しない場合、新しいユーザーが作成されます。<br>- **Update Existing Only** を `true` に設定すると、既存のユーザーのみが更新され、新しいユーザーは作成されません。<br>- Tealium 属性が空の場合、null に変換され、Braze ユーザープロファイルから削除されます。ユーザー属性を削除するために null 値を Braze に送信すべきでない場合は、エンリッチメントを使用する必要があります。 |
| ユーザー属性の変更 | このフィールドを使用して、特定のユーザー属性をインクリメントまたはデクリメントします。<br><br>- 整数属性は、正または負の整数でインクリメントできます。<br>- 配列属性は、既存の配列に値を追加または削除することで変更できます。 |
| イベント | イベントは、特定のユーザーによるカスタムイベントの単一のオカレンスをタイムスタンプとともに表します。このフィールドを使用して、Braze の[イベントオブジェクト]({{site.baseurl}}/api/objects_filters/event_object)にあるようなイベント属性を追跡およびマッピングします。<br><br>- イベント属性 `Name` は、マッピングされたすべてのイベントに必須です。<br>- イベント属性 `Time` は、明示的にマッピングされない限り、自動的に現在時刻に設定されます。<br>- デフォルトでは、イベントが存在しない場合、新しいイベントが作成されます。`Update Existing Only` を `true` に設定すると、既存のイベントのみが更新され、新しいイベントは作成されません。<br>- 配列タイプの属性をマッピングして、複数のイベントを追加します。配列タイプの属性は同じ長さである必要があります。<br>- 単一値の属性を使用でき、各イベントに適用されます。 |
| イベントテンプレート | ボディデータで参照されるイベントテンプレートを提供します。テンプレートを使用して、Braze にデータを送信する前にデータを変換できます。詳細については、Tealium の[テンプレートガイド](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/)をご覧ください。 |
| イベントテンプレート変数 | データ入力としてイベントテンプレート変数を提供します。詳細については、Tealium の[テンプレート変数ガイド](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/)をご覧ください。 |
| 購入 | このフィールドを使用して、Braze の[購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object)にあるようなユーザー購入属性を追跡およびマッピングします。<br><br>- 購入属性 `Product ID`、`Currency`、`Price` は、マッピングされたすべての購入に必須です。<br>- 購入属性 `Time` は、明示的にマッピングされない限り、自動的に現在時刻に設定されます。<br>- デフォルトでは、購入が存在しない場合、新しい購入が作成されます。`Update Existing Only` を `true` に設定すると、既存の購入のみが更新され、新しい購入は作成されません。<br>- 配列タイプの属性をマッピングして、複数の購入アイテムを追加します。配列タイプの属性は同じ長さである必要があります。<br>- 単一値の属性を使用でき、各アイテムに適用されます。 |
| 購入テンプレート | テンプレートを使用して、Braze に送信する前にデータを変換できます。<br>- ネストされたオブジェクトのサポートが必要な場合は、購入テンプレートを定義します。<br>- 購入テンプレートが定義されている場合、アクションの購入セクションで設定した構成は無視されます。<br>- 詳細については、Tealium の[テンプレートガイド](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/)をご覧ください。 |
| 購入テンプレート変数 | データ入力として製品テンプレート変数を提供します。詳細については、Tealium の[テンプレート変数ガイド](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/)をご覧ください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="アクション" }

![マッピングされたユーザー属性とイベントフィールドを含む Tealium Track User アクションの例。]({% image_buster /assets/img/tealium/track_user_example2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab ユーザーの削除 - 非バッチ %}

このアクションでは、Braze ダッシュボードからユーザーを削除できます。

| パラメーター | 説明 |
| ---------- | ----------- |
| ユーザー ID | このフィールドを使用して、Tealium のユーザー ID フィールドを Braze の対応するフィールドにマッピングします。<br><br>- 1つ以上のユーザー ID 属性をマッピングします。複数の ID が指定された場合、最初の空でない値が以下の優先順位に基づいて選択されます: External ID、Braze ID、Alias Name、Alias Label。<br>- ユーザーエイリアスを指定する場合は、Alias Name と Alias Label の両方を設定する必要があります。<br><br>詳細については、Braze の[`/users/delete` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)をご覧ください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="アクション" }

![Braze ユーザー ID マッピングが設定された Tealium のユーザー削除アクション。]({% image_buster /assets/img/tealium/track_user_delete2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab ユーザーの購読グループステータスの更新 - 非バッチ %}
このアクションでは、Braze の SMS またはメール購読グループにユーザーを追加または削除できます。

| パラメーター | 説明 |
| ---------- | ----------- |
| グループタイプ | このフィールドを使用して、これが SMS またはメールの購読グループであるかを示します。 |
| 更新タイプ | このアクションを購読解除または購読イベントにマッピングします。 |
| 属性 | - 購読グループ ID（必須）: 前のフィールドでマッピングされたグループタイプに関連する購読グループの ID。<br>- External ID: ユーザーの external ID。<br><br>メールグループ固有:<br>- メール: ユーザーのメールアドレス。<br>**external ID が定義されていない場合、メールが必須となります。**<br><br>SMS グループ固有:<br>- 電話番号: E.164 形式の電話番号。たとえば、+14155552671。<br>**external ID が定義されていない場合、電話番号が必須となります。** |
{: .reset-td-br-1 .reset-td-br-2 aria-label="アクション" }

![グループタイプと更新タイプのマッピングを含む Tealium の購読グループステータス更新アクション。]({% image_buster /assets/img/tealium/update_subscription.png %}){: style="max-width:90%"}

{% endtab %}
{% endtabs %}

**Finish** を選択します。

#### サマリー {#summary}

作成したコネクターのサマリーを確認します。選択したオプションを変更する場合は、**Back** を選択して編集するか、**Finish** を選択して完了します。

コネクターは、Tealium ホームページのコネクターリストに表示されるようになります。

完了したら、コネクターを保存または公開してください。設定したアクションは、トリガー条件が満たされたときに実行されます。

### ステップ4:Tealium コネクターをテストする {#step-4-test-your-tealium-connector}

コネクターが稼働したら、正常に動作していることを確認するためにテストする必要があります。最も簡単なテスト方法は、Tealium の **Trace Tool** を使用することです。Trace の使用を開始するには、Tealium Tools ブラウザー拡張機能を追加していることを確認してください。

1. 新しいトレースを開始するには、サイドバーで **Server-Side** オプションの下にある **Trace** を選択します。**Start** をクリックし、Trace ID をキャプチャします。
2. ブラウザー拡張機能を開き、AudienceStream Trace に Trace ID を入力します。
3. リアルタイムログを確認します。
4. 検証したいアクションを、**Actions Triggered** エントリをクリックして展開することで確認します。
5. 検証したいアクションを探し、ログステータスを確認します。

Tealium の Trace ツールの実装に関する詳細な手順については、Tealium の [Trace ドキュメント](https://docs.tealium.com/server-side/connectors/trace/about/)を参照してください。

## 連携デモ {#integration-demo}

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" title="Tealium AudienceStream連携デモ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## データポイント超過の可能性 {#potential-data-point-overages}

Tealiumを通じてBrazeを統合する際に、意図せずデータの超過が発生する主な原因は3つあります。

### 重複データの送信 - Braze属性の差分のみを送信する {#sending-duplicate-data-only-send-braze-deltas-of-attributes}
Tealiumはユーザー属性のBraze差分を送信しません。たとえば、ユーザーの名、メール、携帯電話番号を追跡するEventStreamアクションがある場合、Tealiumはアクションがトリガーされるたびに3つの属性すべてをBrazeに送信します。Tealiumは、何が変更または更新されたかを確認し、その情報のみを送信するという動作は行いません。<br><br>
**ソリューション**: <br>バックエンドを確認して属性が変更されたかどうかを評価し、変更があった場合はTealiumの関連メソッドを呼び出してユーザープロファイルを更新します。**これは、Brazeを直接統合するユーザーが通常行う方法です。** <br>**または**<br> バックエンドにユーザープロファイルの独自バージョンを保存しておらず、属性が変更されたかどうかを判断できない場合は、AudienceStreamを使用して[エンリッチメントを作成](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/)し、値が変更された場合にのみユーザー属性を送信することができます。

#### 不要なデータの送信やデータの不必要な上書き {#sending-irrelevant-data-or-needlessly-overwriting-data}
同じイベントフィードを対象とする複数のEventStreamがある場合、1つのアクションがトリガーされるたびに**そのコネクターで有効化されたすべてのアクション**が自動的に実行されます。**これにより、Brazeのデータが上書きされる可能性もあります。**<br><br>
**ソリューション**: <br>各アクションを追跡するために、個別のイベント仕様またはフィードを設定します。<br>**または**<br> Tealiumダッシュボードのトグルを使用して、実行させたくないアクション（またはコネクター）を無効にします。

#### Brazeの初期化が早すぎる {#initializing-braze-too-early}
Braze Web SDKタグを使用してTealiumと統合している場合、MAUが大幅に増加する可能性があります。**Brazeがページ読み込み時に初期化されると、WebユーザーがWebサイトに初めてアクセスするたびにBrazeは匿名プロファイルを作成します。**これにはボットトラフィックも含まれるため、アクティブユーザー数が膨らむ可能性があります。MAU数を抑えるために、「サインイン済み」や「動画視聴済み」など、ユーザーが何らかのアクションを完了した場合にのみユーザー行動を追跡したい場合もあるでしょう。<br><br>
**ソリューション**: <br>[読み込みルール](https://docs.tealium.com/iq-tag-management/load-rules/about/)を設定して、サイト上でタグがいつどこで読み込まれるかを正確に制御します。ボットトラフィックのフィルタリングやSDKの条件付き初期化に関するより包括的なガイダンスについては、[ボットトラフィックのフィルタリング]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_bot-filtering)を参照してください。