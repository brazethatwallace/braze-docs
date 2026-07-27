---
nav_title: コンテキスト変数
article_title: コンテキスト変数
page_type: reference
description: "このリファレンス記事では、Brazeキャンバスのコンテキスト変数について、そのタイプ、使用方法、ベストプラクティスを説明します。"
---

# コンテキスト変数 {#context-variables}

> コンテキスト変数は、特定のキャンバスにおけるユーザーのジャーニー内で作成・使用できる一時的なデータです。コンテキスト変数を使用すると、ユーザーのプロファイル情報を恒久的に変更することなく、遅延のパーソナライズ、ユーザーのダイナミックなセグメント化、メッセージングの充実化が可能になります。コンテキスト変数はキャンバスセッション内にのみ存在し、異なるキャンバス間やセッション外では保持されません。

## コンテキスト変数の仕組み {#how-context-variables-work}

コンテキスト変数は、次の2つの方法で設定できます。

- **キャンバスエントリ時：**ユーザーがキャンバスに入ると、イベントまたはAPIトリガーからのデータが自動的にコンテキスト変数に入力されます。
- **コンテキストステップ内：**[コンテキストステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)を追加することで、キャンバス内でコンテキスト変数を手動で定義または更新できます。

各コンテキスト変数には以下が含まれます。

- 名前（`flight_time` や `subscription_renewal_date` など）
- データ型（数値、文字列、時間、配列など）
- [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)または**パーソナライゼーションを追加**ツールを使用して割り当てる値

定義すると、次の形式で参照することで、キャンバス全体でコンテキスト変数を使用できます。{% raw %}`{{context.${example_variable_name}}}`{% endraw %}

たとえば、{% raw %}`{{context.${flight_time}}}`{% endraw %} はユーザーの予定されたフライト時刻を返すことができます。

ユーザーがキャンバスに入るたびに（以前に入ったことがある場合でも）、コンテキスト変数は最新のエントリデータとキャンバスの設定に基づいて再定義されます。このステートフルなアプローチにより、各キャンバスエントリは独自のコンテキストを維持でき、ユーザーは同じジャーニー内で複数のアクティブな状態を持ちながら、各状態に固有のコンテキストを保持できます。

たとえば、顧客に今後2つのフライトがある場合、2つの別々のジャーニー状態が同時に実行され、それぞれに出発時刻や目的地などのフライト固有のコンテキスト変数が含まれます。これにより、午後2時のニューヨーク行きフライトに関するパーソナライズされたリマインダーを送信しながら、翌日の午前8時のロサンゼルス行きフライトに関する別の更新情報を送信でき、各メッセージが特定の予約に関連した内容になります。

## 考慮事項 {#considerations}

[コンテキストステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)ごとに最大10個のコンテキスト変数を定義できます。各変数名は最大100文字で、文字、数字、またはアンダースコアのみを使用する必要があります。

コンテキスト変数の定義は最大10,240文字です。APIトリガーのキャンバスにコンテキスト変数を渡す場合、それらはコンテキストステップで作成された変数と同じ名前空間を共有します。たとえば、[`/canvas/trigger/send` エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)のコンテキストオブジェクトで変数 `purchased_item` を送信した場合、{% raw %}`{{context.${purchased_item}}}`{% endraw %} として参照できます。コンテキストステップでその変数を再定義すると、新しい値がそのユーザーのジャーニーにおけるAPIの値を上書きします。

コンテキストステップごとに最大50 KBを保存でき、最大10個の変数に分散されます。ステップ内のすべての変数の合計サイズが50 KBを超えた場合、制限を超えた変数は評価も保存もされません。たとえば、コンテキストステップに3つの変数がある場合：

- 変数1：30 KB
- 変数2：19 KB
- 変数3：2 KB

変数3は評価も保存もされません。これは、前の変数の合計が50 KBを超えているためです。

## データ型 {#data-types}

ステップで作成または更新されるコンテキスト変数には、以下のデータ型を割り当てることができます。

{% alert note %}
コンテキスト変数のデータ型には、[イベントプロパティ]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#expected-format)と同じ形式が期待されます。<br><br>配列型を使用する場合、Brazeは値をJSONとして解析しようとするため、オブジェクトの配列を正常に作成できます。配列内のオブジェクトが有効なJSONでない場合、結果は単純な文字列の配列になります。<br><br>ネストされたオブジェクトやオブジェクトの配列には、[`as_json_string` Liquidフィルター](#converting-connected-content-strings-to-json)を使用してください。コンテキストステップで同じオブジェクトを作成する場合は、`as_json_string`を使用してオブジェクトをレンダリングする必要があります。例: {%raw%}`{{context.${object_array} | as_json_string }}`{%endraw%}
{% endalert %}

| データ型 | 変数名の例 | 値の例 |
|---|---|---|
|Boolean| loyalty_program |{% raw %}<code>true</code>{% endraw %}|
|Number| credit_score |{% raw %}<code>740</code>{% endraw %}|
|String| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|Array| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|Array (of objects)| pet_details |{% raw %}<code>[<br>&emsp;{ "id": 1, "type": "dog", "breed": "beagle", "name": "Gus" }<br>&emsp;,<br>&emsp;{ "id": 2, "type": "cat", "breed": "calico", "name": "Gerald" }<br>]</code>{% endraw %}|
|Time (in UTC) | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|Object (flattened) | user_profile|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="データ型" }

デフォルトでは、時間データ型はUTCです。文字列データ型を使用して時間値を保存する場合は、PSTなど別のタイムゾーンとして時間を定義できます。

例えば、ユーザーの誕生日の前日にメッセージを送信する場合、前日に送信するためのLiquidロジックが関連付けられているため、コンテキスト変数を時間データ型として保存します。しかし、クリスマス（12月25日）にホリデーメッセージを送信する場合は、時間をダイナミックな変数として参照する必要がないため、文字列データ型を使用する方が適切です。

オブジェクトデータ型の場合、ドット表記を使用してデータ内のパスを指定できます。例えば、コンテキストステップでコンテキスト変数 `order_summary` を以下の構造で定義した場合:

```json
{
  "shipping": {
    "carrier": "overnight"
  }
}
```

[オーディエンスパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)または[条件分岐]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)フィルターで、ドット表記を使用してコンテキスト変数名としてパスを入力します（例: `order_summary.shipping.carrier`）。フィルターが評価されると、Brazeはそのパスを値 `overnight` に解決します。

Liquid（[メッセージ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)ステップなど）では、代わりに {% raw %}`{{context.${order_summary}.shipping.carrier}}`{% endraw %} を使用してください。

## コンテキスト変数の使用 {#using-context-variables}

コンテキスト変数は、キャンバスで Liquid を使用するあらゆる場所で使用できます。たとえば、[メッセージ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)ステップや[ユーザー更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)ステップで**パーソナライゼーションを追加**を選択して使用できます。メッセージステップのアプリ内メッセージやバナーでは、コンテキスト変数を選択してメッセージの有効期限を決定できます。

たとえば、搭乗予定のフライト前に、乗客にVIPラウンジへのアクセスについて通知したいとします。このメッセージは、ファーストクラスのチケットを購入した乗客にのみ送信する必要があります。コンテキスト変数は、この情報を追跡する柔軟な方法です。

ユーザーは航空券を購入するとキャンバスにエントリします。ラウンジアクセスの資格を判定するために、コンテキストステップで `lounge_access_granted` というコンテキスト変数を作成し、ユーザージャーニーの後続のステップでそのコンテキスト変数を参照します。

![乗客がVIPラウンジアクセスの資格があるかどうかを追跡するために設定されたコンテキスト変数。]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

このコンテキストステップでは、{% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} を使用して、購入したフライトの種類が `first_class` かどうかを判定します。

次に、{% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} が `true` であるユーザーをターゲットにするメッセージステップを作成します。このメッセージは、パーソナライズされたラウンジ情報を含むプッシュ通知になります。このコンテキスト変数に基づいて、対象の乗客はフライト前に関連するメッセージを受け取ります。

- ファーストクラスのチケットを持つ乗客は次のメッセージを受け取ります：「限定VIPラウンジアクセスをお楽しみください！」
- ビジネスクラスおよびエコノミークラスのチケットを持つ乗客は次のメッセージを受け取ります：「フライトをアップグレードして、限定VIPラウンジアクセスを手に入れましょう。」

![購入した航空券の種類に応じて異なるメッセージを送信するメッセージステップ。]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
コンテキストステップの情報を使用して[パーソナライズされた遅延オプション]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step#personalized-delays)を追加できます。つまり、ユーザーを遅延させる変数を選択できます。
{% endalert %}

### アクションパスと終了条件での使用 {#for-action-paths-and-exit-criteria}

これらのトリガーアクションでは、プロパティフィルターをコンテキスト変数またはカスタム属性と比較できます：**カスタムイベントを実行**および**購入する**。これらのアクショントリガーは、基本プロパティとネストされたプロパティの両方のプロパティフィルターもサポートしています。

- 基本プロパティと比較する場合、利用可能な比較はカスタムイベントで定義されたプロパティの型と一致します。たとえば、文字列プロパティには完全一致や正規表現一致があります。ブールプロパティは true または false になります。
- ネストされたプロパティと比較する場合、型は事前定義されていないため、階層化カスタム属性の比較と同様に、ブール値、数値、文字列、時間、年間日付の複数のデータ型にわたる比較を選択できます。比較時にネストされたプロパティの実際のデータ型と一致しないデータ型を選択した場合、ユーザーはアクションパスまたは終了条件に一致しません。

#### アクションパスの例 {#action-path-examples}

{% alert important %}
カスタム属性の比較では、アクションが実行された時点のカスタム属性値を使用します。つまり、比較時にユーザーがこのカスタム属性を設定していない場合、またはカスタム属性値が定義されたプロパティ比較と一致しない場合、ユーザーはアクションパスグループに一致しません。これは、ユーザーがアクションパスステップにエントリした時点では一致していた場合でも同様です。
{% endalert %}

{% tabs %}
{% tab カスタムイベントを実行 %}

以下のアクションパスは、基本プロパティ `source` を持つカスタムイベント `Account_Created` を実行したユーザーを、コンテキスト変数 `app_source_variable` に基づいて振り分けるように設定されています。

![カスタムイベント実行時にコンテキスト変数を参照するアクションパスの例。]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab 購入する %}

以下のアクションパスは、特定の商品名 `shoes` の基本プロパティ `brand` をコンテキスト変数 `promoted_shoe_brand` と一致させるように設定されています。

![購入時にコンテキスト変数を参照するアクションパスの例。]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### 終了条件の例 {#exit-criteria-examples}

{% tabs %}
{% tab カスタムイベントを実行 %}

終了条件は、キャンバス内のユーザージャーニーのどの時点でも、以下の場合にユーザーがキャンバスから退出することを示しています：

- カスタムイベント **Abandon Cart** を実行し、かつ
- 基本プロパティ **Item in Cart** がコンテキスト変数 `cart_item_threshold` の文字列値と一致する場合。

![コンテキスト変数に基づいてカスタムイベントを実行した場合にユーザーを退出させるように設定された終了条件。]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab 購入する %}

終了条件は、キャンバス内のユーザージャーニーのどの時点でも、以下の場合にユーザーがキャンバスから退出することを示しています：

- 商品名「book」の特定の購入を行い、かつ
- その購入のネストされたプロパティ「loyalty_program」がユーザーのカスタム属性「VIP」と等しい場合。

![購入を行った場合にユーザーを退出させるように設定された終了条件。]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### 有効期限の設定 {#set-an-expiration}

キャンバスの[メッセージ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)ステップ内の[バナー]({{site.baseurl}}/user_guide/channels/banners)および[アプリ内メッセージ]({{site.baseurl}}/user_guide/channels/in_app_messages)では、有効期限として**ステップが利用可能になってからの期間**を選択し、**期間をパーソナライズ**をオンにすることで、コンテキスト変数から利用可能期間を制御できます。たとえば、コンテキストステップのプロモーションや予約期間に合わせることができます。

**期間をパーソナライズ**は、その期間ベースの有効期限オプションに適用されます。代わりに**特定の日時**を選択した場合は、日時コントロールを使用して有効期限を設定します。

### アクションパスの遅延 {#action-path-delays}

[アクションパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)ステップの**評価ウィンドウ**で、**遅延をパーソナライズ**をオンにすると、コンテキスト変数からユーザーがステップに保持される期間を設定できます。ティアやリージョンなどの詳細に基づいて、ユーザーごとに待機期間を変える必要がある場合に使用します。

### コンテキスト変数フィルター {#context-variable-filters}

[オーディエンスパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)および[条件分岐]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)ステップで、以前に宣言されたコンテキスト変数を使用するフィルターを作成できます。

{% alert note %}
コンテキスト変数フィルターは、オーディエンスパスと条件分岐ステップでのみ使用できます。
{% endalert %}

コンテキスト変数はキャンバスのスコープ内でのみ宣言およびアクセスできるため、セグメントでは参照できません。コンテキスト変数フィルターは、オーディエンスパスと条件分岐ステップで同様に機能します。オーディエンスパスステップは複数のグループを表し、条件分岐ステップはバイナリの判定を表します。

![コンテキスト変数を使用してフィルターを作成するオプションがある条件分岐ステップの例。]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

キャンバスのコンテキスト変数に事前定義された型があるのと同様に、コンテキスト変数と静的値の比較には[一致するデータ型]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)が必要です。コンテキスト変数フィルターでは、[階層化カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)の比較と同様に、ブール値、数値、文字列、時間、年間日付の複数のデータ型にわたる比較が可能です。

以下は、コンテキスト変数 `product_name` を正規表現 `/braze/` と比較するコンテキスト変数フィルターの例です。

![コンテキスト変数「product_name」を正規表現「/braze/」と一致させるフィルター設定。]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### 日付コンテキスト変数の年間日付フィルターと時間フィルター {#day-of-year-and-time-filters-for-date-context-variables}

コンテキスト変数で**年間日付**または**時間**の比較フィルターを使用するには：

1. コンテキスト変数をカレンダー日付（たとえば、2025年10月23日）に設定する[コンテキストステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)を追加します。
2. コンテキストステップの後に[オーディエンスパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)ステップを追加します。
3. オーディエンスパスステップで、そのコンテキスト変数に基づいてユーザーを分割するフィルターを追加します。
4. **年間日付**または**時間**カテゴリから比較を選択します。

コンテキスト変数に宣言された型がない場合、Brazeはドロップダウンに**年間日付**と**時間**の両方を含むすべての利用可能な比較型を表示します。変数がコンテキストステップで**時間**型として宣言されている場合、**年間日付**と**時間**の比較のみが表示されます。既知の型を持つ他のデータ型（たとえば、時間型の階層化カスタム属性）の場合、その型に適用される比較のみが表示されます。

{% alert note %}
コンテキスト変数と比較には同じデータ型を使用してください。たとえば、コンテキスト変数が時間データ型の場合、時間の比較（「前」や「後」など）を使用します。一致しないデータ型（時間コンテキスト変数に対する文字列比較など）を使用すると、予期しない動作が発生する可能性があります。
{% endalert %}

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

#### コンテキスト変数またはカスタム属性との比較 {#comparing-to-context-variables-or-custom-attributes}

**コンテキスト変数またはカスタム属性と比較**トグルを選択すると、以前に定義されたコンテキスト変数やユーザーのカスタム属性と比較するコンテキスト変数フィルターを構築できます。これは、APIトリガーの `context` のようにユーザーごとにダイナミックな比較を行う場合や、コンテキスト変数にわたって定義された複雑な比較ロジックを集約する場合に便利です。

{% tabs %}
{% tab 例 1 %}

ダイナミックな非アクティブ期間の後にユーザーにパーソナライズされたリマインダーを送信したいとします。過去3日間にアプリにログインしていないユーザーがメッセージを受け取る対象です。

コンテキスト変数 `re_engagement_date` は {% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %} として定義されています。`3 days` はユーザーのカスタム属性として保存される可変量にすることもできます。したがって、`re_engagement_date` が `last_login_date`（ユーザープロファイルにカスタム属性として保存）より後の場合、メッセージが送信されます。

![コンテキスト変数「re_engagement_date」がカスタム属性「last_login_date」より後であるパーソナライゼーションタイプとしてカスタム属性を使用したフィルター設定。]({% image_buster /assets/img/context_variable_filter2.png %})

{% endtab %}
{% tab 例 2 %}

以下のフィルターは、コンテキスト変数 `reminder_date` がコンテキスト変数 `appointment_deadline` より前であることを比較します。これにより、オーディエンスパスステップでユーザーをグループ化し、予約期限前に追加のリマインダーを受け取るべきかどうかを判定できます。

![コンテキスト変数「reminder_date」をコンテキスト変数「appointment_deadline」と比較するパーソナライゼーションタイプとしてコンテキスト変数を使用したフィルター設定。]({% image_buster /assets/img/context_variable_filter3.png %})

{% endtab %}
{% endtabs %}

## タイムゾーンの一貫性の標準化 {#time-zone-consistency-standardization}

キャンバスでは、タイムスタンプ型を使用するほとんどのイベントプロパティはすでにUTCですが、いくつかの例外があります。キャンバスコンテキストの追加により、アクションベースのキャンバスにおけるすべてのデフォルトのタイムスタンプイベントプロパティは、一貫してUTCになります。この変更は、キャンバスのステップやメッセージを編集する際に、より予測可能で一貫性のある体験を確保するための広範な取り組みの一環です。この変更は、特定のキャンバスがコンテキストステップを使用しているかどうかにかかわらず、すべてのアクションベースのキャンバスに影響することに注意してください。

{% alert important %}
すべての状況において、タイムスタンプを目的のタイムゾーンで表示するために、[Liquid time_zone フィルター]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties#things-to-know)を使用することを強くお勧めします。例については、[コンテキストステップの記事にあるよくある質問]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#faq-example)を参照してください。
{% endalert %}

## 関連記事 {#related-articles}

- [コンテキストステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)
- [Liquidによるパーソナライゼーションとダイナミックコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)