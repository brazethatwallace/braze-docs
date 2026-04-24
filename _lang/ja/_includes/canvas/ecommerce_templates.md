{% tabs %}
{% tab Abandoned browse %}

### 閲覧の放棄

製品を閲覧したが、カートへの追加や注文を行わなかったユーザーにエンゲージするには、**閲覧の放棄**テンプレートを使用します。

![「閲覧の放棄」キャンバステンプレートが適用され、「エントリルール」が展開された状態。]({% image_buster /assets/img_archive/abandoned_browse.png %})

#### 設定

キャンバスページで [**キャンバステンプレートを使用**] > [**Braze テンプレート**] を選択し、**閲覧の放棄**テンプレートを適用します。 

##### デフォルト設定

キャンバスでは、以下の設定が事前に構成されています。
- 基本情報 
    - キャンバス名: **閲覧の放棄**
    - コンバージョンイベント: `ecommerce.order placed`
        - コンバージョン期限: 3日間 
- エントリスケジュール 
    - ユーザーが `ecommerce.product_viewed` イベントを実行した場合のアクションベース
    - 開始時刻はキャンバステンプレートを作成した時点です<br><br>![キャンバスの「アクションベースのオプション」。]({% image_buster /assets/img/ecommerce/abandoned_browse_entry.png %})<br><br> 
- ターゲットオーディエンス 
    - エントリオーディエンス 
        - メールが**空白ではない**
        - ビジネスニーズに合わせてエントリオーディエンスの条件を変更することもできます
    - エントリコントロール
        - キャンバスの全期間が完了した後、ユーザーはこのキャンバスに再エントリできます
    - 終了条件 
        - `ecommerce.cart_updated`、`ecommerce.checkout_started`、または `ecommerce.order_placed` を実行<br><br>![キャンバスのエントリコントロールと終了条件。]({% image_buster /assets/img/ecommerce/abandoned_browse_entry_exit.png %})<br><br> 
- 送信設定 
    - 購読中またはオプトイン済みのユーザー 
- 遅延ステップ
    - 1時間の遅延
- メッセージステップ 
    - メールテンプレートと HTML ブロックを確認し、Liquid テンプレートの例を使用して事前構築済みテンプレートのメッセージに製品を追加します。独自のメールテンプレートを使用する場合は、次のセクションで示すように [Liquid 変数](#message-personalization)を参照することもできます。

#### メール向けの閲覧放棄の製品パーソナライゼーション 

閲覧放棄メール用の HTML 製品ブロックを追加する方法の例を以下に示します。 

{% raw %}
```java
<table style="width:100%">
  <tr>
    <th><img src="{{context.${image_url}}}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{context.${product_name}}}</li>
        <li>Price: ${{context.${price}}}</li>
      </ul>
    </th>
  </tr>
</table>
```
{% endraw %}

##### 製品 URL

{% raw %}
```liquid
{{context.${product_url}}}
```
{% endraw %}    

{% endtab %}
{% tab Abandoned cart %}

### カート放棄

カートに製品を追加したが、購入手続きや注文に進まなかった顧客からの潜在的な売上損失に対応するには、**カート放棄**テンプレートを使用します。 

![「放棄カート」キャンバステンプレートが適用され、「エントリルール」が展開された状態。]({% image_buster /assets/img_archive/abandoned_cart.png %})

#### 設定

キャンバスページで [**キャンバステンプレートを使用**] > [**Braze テンプレート**] を選択し、**カート放棄**テンプレートを適用します。 

##### デフォルト設定

キャンバスでは、以下の設定が事前に構成されています。
- 基本情報 
    - キャンバス名: **カート放棄**
    - コンバージョンイベント: `ecommerce.order_placed`
        - コンバージョン期限: 3日間 
- エントリスケジュール 
    - ユーザーが（ドロップダウンにある）**カート更新イベントの実行**をトリガーした場合のアクションベースのトリガー
    - 開始時刻はキャンバステンプレートを作成した時点です<br><br>![キャンバスの「アクションベースのオプション」。]({% image_buster /assets/img/ecommerce/abandoned_cart_entry.png %})<br><br> 
- ターゲットオーディエンス 
    - エントリオーディエンス 
        - これらのアプリを **1回以上**使用したことがある 
        - メールが**空白ではない**
    - エントリコントロール
        - ユーザーは即時にキャンバスへの再エントリが可能です
    - 終了条件 
        - `ecommerce.cart_updated`、`ecommerce.checkout_started`、または `ecommerce.order_placed` を実行<br><br>![キャンバスのエントリコントロールと終了条件。]({% image_buster /assets/img/ecommerce/abandoned_cart_entry_exit.png %})<br><br> 
- 送信設定 
    - 購読中またはオプトイン済みのユーザー 
- 遅延ステップ
     - 4時間の遅延
- メッセージステップ 
    - メールテンプレートと HTML ブロックを確認し、Liquid テンプレートの例を使用して事前構築済みテンプレートのメッセージに製品を追加します。独自のメールテンプレートを使用する場合は、次のセクションで示すように [Liquid 変数](#message-personalization)を参照することもできます。

#### カート放棄の再エントリロジックの仕組み

ユーザーがチェックアウトプロセスを開始すると、そのカートは `checkout_started` としてマークされます。その時点以降、同じカート ID によるカート更新では、ユーザーはカート放棄のユーザージャーニーに再エントリする資格を得られません。

1. ユーザーが商品をカートに追加すると、キャンバスにエントリします。
2. 商品を追加または更新するたびに、キャンバスに再エントリします。これにより、カートデータとメッセージングが常に最新の状態に保たれます。
3. ユーザーがチェックアウトプロセスを開始すると、そのカートは `checkout_started` としてタグ付けされ、ユーザーはキャンバスを退出します。
4. 同じカート ID を使用した以降のカート更新は、このカートがすでにチェックアウト段階に移行しているため、再エントリをトリガーしません。

ユーザーがチェックアウトのユーザージャーニーに移行すると、代わりに[購入手続き放棄キャンバス](#abandoned-checkout)のターゲットになります。これは購入プロセスのより先の段階にいるユーザー向けに設計されています。

#### メール向けのカート放棄の製品パーソナライゼーション {#abandoned-cart-checkout}

カート放棄のユーザージャーニーでは、製品のパーソナライゼーションに特別な `shopping_cart` Liquid タグが必要です。 

以下の例は、`shopping_cart` Liquid タグを使用して HTML ブロックを追加し、製品をメールに追加する方法を示しています。 

{% raw %}
```java
<table style="width:100%">
  {% shopping_cart {{context.${cart_id}}} %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

{% alert note %}
Shopify を使用する場合は、カタログ名を追加してバリアント画像 URL を取得します。 
{% endalert %}

##### HTML カート URL

ユーザーをカートに戻したい場合は、メタデータオブジェクトの下にネストされたイベントプロパティを追加できます。例:

{% raw %}
```liquid
{{context.${metadata}.cart_url}}
```
{% endraw %}

Shopify を使用する場合は、次の Liquid テンプレートを使用してカート URL を作成します。

{% raw %}
```liquid
{{context.${source}}}/checkouts/cn/{{context.${cart_id}}} 
```
{% endraw %}

{% endtab %}
{% tab Abandoned checkout %}

### 購入手続き放棄

**購入手続き放棄**テンプレートを使用して、チェックアウトプロセスを開始したが注文前に離脱した顧客をターゲットにします。 

![「購入手続き放棄」キャンバステンプレートが適用され、「エントリルール」が展開された状態。]({% image_buster /assets/img_archive/abandoned_checkout.png %})

#### 設定

キャンバスページで [**キャンバステンプレートを使用**] > [**Braze テンプレート**] を選択し、**購入手続き放棄**テンプレートを適用します。 

##### デフォルト設定

キャンバスでは、以下の設定が事前に構成されています。

- 基本情報 
    - キャンバス名: **購入手続き放棄**
    - コンバージョンイベント: `ecommerce.order_placed`
        - コンバージョン期限: 3日間 
- エントリスケジュール 
    - ユーザーが `ecommerce.checkout_started` イベントを実行した場合のアクションベースのトリガー
    - 開始時刻はキャンバステンプレートを作成した時点です<br><br>![キャンバスの「アクションベースのオプション」。]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry.png %})
- ターゲットオーディエンス 
    - エントリオーディエンス 
        - これらのアプリを **1回以上**使用したことがある 
        - メールが**空白ではない**
    - エントリコントロール
        - ユーザーは即時にキャンバスへの再エントリが可能です
        - 終了条件 
            - `ecommerce.order_placed` イベントを実行<br><br>![キャンバスのエントリコントロールと終了条件。]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry_exit.png %})<br><br>
- 送信設定 
    - 購読中またはオプトイン済みのユーザー 
- 遅延ステップ
    - 4時間の遅延
- メッセージステップ 
    - メールテンプレートと HTML ブロックを確認し、Liquid テンプレートの例を使用して事前構築済みテンプレートのメッセージに製品を追加します。独自のメールテンプレートを使用する場合は、次のセクションで示すように [Liquid 変数](#message-personalization)を参照することもできます。

#### メール向けの購入手続き放棄のパーソナライゼーション

購入手続き放棄のユーザージャーニーでは、製品のパーソナライゼーションに特別な `shopping_cart` Liquid タグが必要です。 

以下の例は、`shopping_cart` Liquid タグを使用して HTML ブロックを追加し、製品をメールに追加する方法を示しています。 

{% raw %}
```java
<table style="width:100%">
  {% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
    {% endfor %}
</table>
```
{% endraw %}

##### `abort_if_not_abandoned` {#abort-if-not-abandoned}

`abort_if_not_abandoned` パラメーターは購入手続き放棄のユースケースに固有のもので、`ecommerce.checkout_started` イベントと組み合わせて `shopping_cart` Liquid タグでのみ使用されます。

| 値 | 動作 |
| ----- | -------- |
| `true`（デフォルト） | カートが放棄されていない場合（つまり、ユーザーがその後注文を完了した場合）、メッセージは中止されます。 |
| `false` | カートが放棄状態でなくてもメッセージが送信され、現在のチェックアウトステータスに関係なくメールにカートの詳細を含めることができます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

送信時にカートがまだ放棄状態と見なされているかどうかに関係なくチェックアウトリマインダーを送信したい場合は、`abort_if_not_abandoned` を `false` に設定します。パラメーターを省略するか `true` に設定すると、Braze はすでに購入を完了したユーザーへのメッセージを中止します。

##### チェックアウト URL

{% raw %}
```liquid
{{context.${metadata}.checkout_url}}
```
{% endraw %}

{% endtab %}
{% tab Order confirmation and feedback survey %}

### 注文確認とフィードバック調査

**注文確認＆フィードバック調査**テンプレートを使用して、注文の成功を確認し、顧客満足度を向上させます。

![「注文確認」キャンバステンプレートが適用され、「エントリルール」が展開された状態。]({% image_buster /assets/img_archive/order_confirmation_feedback.png %})

#### 設定

キャンバスページで [**キャンバステンプレートを使用**] > [**Braze テンプレート**] を選択し、**注文確認＆フィードバック調査**テンプレートを適用します。 

##### デフォルト設定

キャンバスでは、以下の設定が事前に構成されています。

- 基本情報 
    - キャンバス名: **注文確認とフィードバック調査**
    - コンバージョンイベント: `ecommerce.session_start`
        - コンバージョン期限: 10日間 
- エントリスケジュール 
    - ユーザーが `ecommerce.cart_updated` イベントを実行した場合のアクションベースのトリガー
    - 開始時刻はキャンバステンプレートを作成した時点です<br><br>![キャンバスの「アクションベースのオプション」。]({% image_buster /assets/img/ecommerce/feedback_entry.png %})<br><br>
- ターゲットオーディエンス 
    - エントリオーディエンス 
        - これらのアプリを **1回以上**使用したことがある 
        - メールが**空白ではない**
    - エントリコントロール
        - ユーザーは即時にキャンバスへの再エントリが可能です
    - 終了条件 
        - 該当しない<br><br>![キャンバスの追加フィルターとエントリコントロール。]({% image_buster /assets/img/ecommerce/feedback_entry_exit.png %})<br><br>
- 送信設定 
    - 購読中またはオプトイン済みのユーザー 
- メッセージステップ 
    - メールテンプレートと HTML ブロックを確認し、Liquid テンプレートの例を使用して事前構築済みテンプレートのメッセージに製品を追加します。独自のメールテンプレートを使用する場合は、次のセクションで示すように [Liquid 変数](#message-personalization)を参照することもできます。

#### メール向けの注文確認のパーソナライゼーション

注文完了後に注文確認メールへ HTML 製品ブロックを追加する方法の例を以下に示します。

{% raw %}
```json
<table style="width:100%">
  {% for item in {{context.${products}}} %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200" /></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{item.product_name}}</li>
        <li>Price: {{item.price}}</li>
        <li>Quantity: {{item.quantity}}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

##### 注文ステータス URL

{% raw %}
```liquid
{{context.${metadata}.order_status_url}}
```
{% endraw %}

{% endtab %}
{% endtabs %}