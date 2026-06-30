---
nav_title: "カタログセグメント"
article_title: "カタログセグメント"
page_order: 0
page_type: reference
alias: "/catalog_segments/"
description: "この記事では、カタログセグメントの作成方法について説明します。カタログセグメントは、SQLセグメントエクステンションでカタログデータを使用してユーザーのオーディエンスを構築します。"
tool: Segments
---

# カタログセグメント {#catalog-segments}

> カタログセグメントは、カタログデータとカスタムイベントまたは購入のデータを組み合わせて作成されるSQLセグメントエクステンションの一種です。セグメントで参照し、キャンペーンやキャンバスでターゲティングできます。

カタログセグメントは、SQLを使用してカタログのデータとカスタムイベントまたは購入のデータを結合します。そのためには、カタログとカスタムイベントまたは購入の間で共通の識別子フィールドが必要です。たとえば、カタログ内のアイテムIDの値は、カスタムイベントのプロパティの値と一致する必要があります。

## カタログセグメントの作成 {#creating-a-catalog-segment}

1. **セグメントエクステンション** > **新規エクステンションを作成** > **テンプレートから開始**に移動し、テンプレートを選択します。<br>![イベント、購入、またはRFMセグメントのカタログセグメントを作成するオプションを含むモーダル。]({% image_buster /assets/img/catalog-segments-template.png %}){: style="max-width:80%" }

{: start="2"}
2. SQLエディターにテンプレートが自動的に入力されます。<br>![事前生成されたテンプレートを含むSQLエディター。]({% image_buster /assets/img/catalog-segments-editor.png %}){: style="max-width:80%" }<br>このテンプレートは、ユーザーイベントデータとカタログデータを結合し、特定のカタログアイテムに関与したユーザーをセグメント化します。

3. **変数**タブを使用して、セグメントを生成する前にテンプレートに必要なフィールドを入力します。<br>Brazeがカタログアイテムとのエンゲージメントに基づいてユーザーを識別するには、以下を行う必要があります：<br> - カタログフィールドを含むカタログを選択する <br> - イベントプロパティを含むカスタムイベントを選択する <br> - カタログフィールドとイベントプロパティの値を一致させる

変数を選択するためのガイドラインは以下のとおりです：

| 変数フィールド | 説明 |
| --- | --- |
| `Catalog` | ユーザーのターゲティングに使用するカタログの名前。 |
| `Catalog field`| `Custom event property`と同じ値を含むカタログ内のフィールド。多くの場合、IDの一種です。eコマースのユースケースでは、`shopify_id`になります。 |
| `Custom event` | カスタムイベントの名前。`Catalog field`と一致する値を持つプロパティを含む同じイベントです。eコマースのユースケースでは、`Made Order`になります。 |
| `Custom event property` | `Catalog field`と値が一致するカスタムイベントプロパティの名前。eコマースのユースケースでは、`Shopify_ID`になります。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="カタログセグメントの作成" }

{: start="4"}
4. 必要に応じて、カタログ内の特定のフィールド値でセグメント化するために、ユースケースに合わせた追加のオプションフィールドを入力します：
- `Catalog field`：このカタログ内の特定のフィールド（列名）
- `Value`：そのフィールドまたは列内の特定の値 <br><br> ヘルスアプリを例にすると、予約可能な各医師のカタログ内に`specialty`というフィールドがあり、`vision`や`dental`などの値が含まれているとします。`dental`の値を持つ医師を訪問したユーザーをセグメント化するには、`Catalog field`として`specialty`を選択し、`Value`として`dental`を選択します。

5. SQLセグメントを作成した後、**プレビューを実行**をクリックして、クエリがユーザーを返すか、エラーがないかを確認することをお勧めします。[クエリ結果のプレビュー]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#previewing-results)、[SQLセグメントエクステンションの管理]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#managing-sql-segment-extensions)などの詳細については、[SQLセグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)をご確認ください。

{% alert note %}
`CATALOGS_ITEMS_SHARED`テーブルを使用するSQLセグメントを作成する場合は、カタログIDを指定する必要があります。例：

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### SQLの反転が必要かどうかの判断 {#determining-if-you-need-to-invert-sql}

イベントがゼロのユーザーを直接クエリすることはできませんが、**SQLを反転**を使用してこれらのユーザーをターゲティングできます。

たとえば、購入が3回未満のユーザーをターゲティングするには、まず購入が3回以上のユーザーを選択するクエリを作成します。次に、**SQLを反転**を選択して、購入が3回未満のユーザー（購入がゼロのユーザーを含む）をターゲティングします。

![「過去30日間にメールを1〜4回クリック」というセグメントエクステンションで、SQLを反転するオプションが選択されている状態。]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:70%;"}

{% alert important %}
イベントがゼロのユーザーを特にターゲティングする場合を除き、SQLを反転する必要はありません。**SQLを反転**が選択されている場合は、その機能が必要であること、およびセグメントが目的のオーディエンスと一致していることを確認してください。たとえば、クエリがイベントが1回以上のユーザーをターゲティングしている場合、反転するとイベントがゼロのユーザーのみがターゲティングされます。
{% endalert %}

## セグメントメンバーシップの更新 {#refreshing-segment-membership}

カタログセグメントのセグメントメンバーシップを更新するには、カタログセグメントを開き、**アクション** > **更新** > **はい、更新します**を選択します。

{% alert tip %}
ユーザーが定期的に出入りすることが予想されるセグメントを作成した場合は、そのセグメントをキャンペーンやキャンバスでターゲティングする前に、使用しているカタログセグメントを手動で更新してください。
{% endalert %}

### 更新設定の指定 {#designating-refresh-settings}

{% multi_lang_include audience/segments.md section='Refresh settings' %}

## ユースケース {#use-cases}

{% tabs local %}
{% tab Health %}

### ヘルスアプリ {#health-app}

ヘルスアプリがあり、歯科医の予約をしたユーザーをセグメント化したいとします。また、以下のものがあるとします：

- 患者が予約できるさまざまな医師を含むカタログ`Doctors`。各医師には`doctor ID`が割り当てられています
- カタログの`doctor ID`フィールドと同じ値を共有する`doctor ID`プロパティを持つカスタムイベント`Booked Visit`
- `dental`の値を含むカタログ内の`speciality`フィールド

以下の変数を使用してカタログセグメントを設定します：

| 変数 | プロパティ |
| --- | --- |
| `Catalog`| Doctors |
| `Catalog field` | doctor ID |
| `Custom event`| Booked Visit|
| `Custom event property` | doctor ID |
| `(Under Filter SQL Results) Catalog field` | Specialty |
| `(Under Filter SQL Results) Value`| Dental |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ヘルスアプリ" }

{% endtab %}
{% tab SaaS %}

### SaaSプラットフォーム {#saas-platform}

B2B SaaSプラットフォームがあり、既存顧客の従業員であるユーザーをセグメント化したいとします。また、以下のものがあるとします：

- 現在SaaSプラットフォームを使用しているさまざまなアカウントを含むカタログ`Accounts`。各アカウントには`account ID`が割り当てられています
- カタログの「account ID」フィールドと同じ値を共有する「account ID」プロパティを持つカスタムイベント`Event Attendance`
- `enterprise`の値を含むカタログ内の`Classification`フィールド

以下の変数を使用してカタログセグメントを設定します：

| 変数 | プロパティ |
| --- | --- |
| `Catalog` | Accounts |
| `Catalog field `| account ID |
| `Custom event` | Event Attendance |
| `Custom event property` | account ID |
| `(Under Filter SQL Results) Catalog field` | Classification |
| `(Under Filter SQL Results) Value` | Enterprise |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SaaSプラットフォーム" }

{% endtab %}
{% endtabs %}

## よくある質問 {#frequently-asked-questions}

### カタログセグメントの実行はSQLセグメントエクステンションのクレジットを消費しますか？ {#does-running-a-catalog-segment-consume-sql-segment-extension-credits}

はい、カタログセグメントはSQLを利用しており、SQLセグメントエクステンションのクレジットを消費します。詳細については、[SQLセグメントの使用状況]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#monitoring-your-sql-segments-usage)をご確認ください。

### カタログセグメントの作成はSQLセグメントエクステンションの割り当てを消費しますか？ {#does-creating-a-catalog-segment-consume-sql-segment-extension-allotments}

はい。SQLセグメントエクステンションがセグメントエクステンションの割り当てにカウントされるのと同様に、カタログセグメントもその割り当てにカウントされます。

### 現在のテンプレートでは対応できないカタログセグメントのユースケースがあります。どのように設定すればよいですか？ {#i-have-a-catalog-segment-use-case-that-the-current-template-doesnt-serve-how-should-i-set-that-up}

カスタマーサポートマネージャーまたは[Brazeサポート]({{site.baseurl}}/user_guide/administer/personal/braze_support)にお問い合わせください。