---
nav_title: カスタム属性
article_title: カスタム属性
page_order: 1
page_type: reference
description: "このページでは、カスタム属性について説明し、さまざまなカスタム属性データタイプについて解説します。"
search_rank: 1
---

# [![Braze Learning コース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}カスタム属性 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-attributes}

> このページでは、ユーザー固有の特性のコレクションであるカスタム属性について説明します。カスタム属性は、ユーザーに関する属性や、アプリケーション内の価値の低いアクションに関する情報を格納するのに最適です。

Brazeに保存すると、カスタム属性を使用してオーディエンスセグメントを構築し、Liquidを使用してメッセージングをパーソナライズできます。カスタムイベントとは異なり、カスタム属性の時系列情報は保存されないため、時系列情報に基づくグラフを取得できない点に注意してください。

{% alert important %}
**名前は完全一致です。** カスタム属性キーは**大文字と小文字が区別されます**。例えば、`Home_City`と`home_city`は2つの異なる属性です。[REST API]({{site.baseurl}}/api/endpoints/user_data/post_user_track)やSDKを通じてデータを送信する場合、Brazeは属性名の**先頭と末尾のスペースを除去します**。そのため、`greeting`と` greeting `は同じキーに解決されます。属性を参照するすべての場所（**データ設定** > **カスタム属性**、APIおよびSDKペイロード、CSVインポート）で同じスペルと大文字小文字を使用してください。[データタイプを強制]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data#data-type-coercion)した場合にBrazeが受信値をどのように変換するかについては、[カスタムデータの管理]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data)を参照してください。
{% endalert %}

## ユースケース {#use-cases}

一般的なカスタム属性のユースケースには、以下のようなものがあります。

- ロイヤルティティア、購読ステータス、希望言語、プランタイプなどの特性に基づいてユーザーをセグメント化し、オーディエンスのターゲティングや抑制を行う
- ユーザーの名、報酬ポイント、お気に入りカテゴリなどの属性を参照して、[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)でメッセージをパーソナライズする
- オンボーディングステージ、アカウントステータス、トライアル終了日など、ライフサイクルステージやユーザーの状態をトラッキングする
- [数値属性]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#numbers)で価値の低いアクションをカウントする（例：ユーザーが機能を閲覧するたびに`feature_views_count`属性をインクリメントする）
- [時間属性]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#time)を使用して、価値の低いアクションが最後に発生した日時を記録する（例：`last_support_ticket_at`や`last_password_reset_at`）
- お気に入りのジャンルや最近閲覧したコンテンツなど、ユーザーの興味や履歴を[配列]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#arrays)として保存し、興味ベースのターゲティングに活用する
- 構造化された設定や複数の保存済み住所など、より豊富なプロファイルデータを[オブジェクト]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)や[オブジェクトの配列]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)として保存する
- [属性トリガー]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers)を使用して、属性値が変更されたときにアクションベースのメッセージをトリガーする（例：ユーザーの`rewards_tier`が変更されたときにティアアップ通知を送信する）

## カスタム属性の管理 {#managing-custom-attributes}

ダッシュボードでカスタム属性の作成および管理を行うには、**データ設定** > **カスタム属性**に移動します。

![ブール値である4つのカスタム属性。]({% image_buster /assets/img/export_custom_attributes.png %})

**最終更新日**の列には、カスタム属性が最後に編集された時間（ブロックリストやアクティブに設定された時間など）が表示されます。

{% alert important %}
メッセージのターゲットを正しく設定するには、カスタム属性のデータタイプが実際のカスタム属性と一致していることを確認してください。<br><br>例えば、`newsletter_subscribed`が文字列として定義されている場合、Liquid構文は次のようになります：{% raw %}`{% if {{custom_attribute.${newsletter_subscribed}}} == 'true' %}`{% endraw %}。`newsletter_subscribed`がブール値として定義されている場合、Liquid構文には単一引用符を使用しません：{% raw %}`{% if {{custom_attribute.${newsletter_subscribed}}} == true %}`{% endraw %}。
{% endalert %}

このページから、既存のカスタム属性の表示、管理、作成、またはブロックリストへの追加ができます。カスタム属性の横にあるメニューから、以下のアクションを選択します。

### ブロックリスト {#blocklisting}

カスタム属性は、アクションメニューで個別にブロックリストに追加することも、最大100個の属性を選択して一括でブロックリストに追加することもできます。

カスタム属性をブロックすると：

- その属性に関するデータは今後収集されなくなります。
- その属性のブロックが解除されない限り、既存のデータは利用できなくなります。
- その属性はフィルターやグラフに表示されなくなります。

さらに、ブロックされたカスタム属性がBrazeの他の領域でフィルターやトリガーによって現在参照されている場合、警告モーダルが表示され、それを参照しているフィルターやトリガーのすべてのインスタンスが削除およびアーカイブされることが説明されます。

カスタムデータのブロックリストへの追加と削除の詳細については、[カスタムデータのブロックリスト]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data)を参照してください。

### 個人を特定できる情報（PII）としてマークする {#mark-as-personally-identifiable-information-pii}

管理者は、このページからカスタム属性を作成し、PIIとしてマークすることもできます。これらの属性は、管理者と「View Custom Attributes Marked as PII」権限を持つダッシュボードユーザーにのみ表示されます。

### 説明を追加する {#add-descriptions}

`Manage Events, Attributes, Purchases`の[ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)を持っている場合、カスタム属性の作成後に説明を追加できます。カスタム属性の**説明を編集**を選択し、チームへのメモなど、任意の内容を入力します。

### タグを追加する {#add-tags}

「Manage Events, Attributes, Purchases」の[ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)を持っている場合、カスタム属性の作成後にタグを追加できます。タグは属性リストのフィルタリングに使用できます。

### カスタム属性を削除する {#remove-custom-attributes}

ユーザープロファイルからカスタム属性を削除するには、2つの方法があります。

* [ユーザーの更新ステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#removing-custom-attributes)で、削除するカスタム属性名を選択します。
* APIリクエストで[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track)に`null`値を設定します。

### データをエクスポートする {#export-data}

カスタム属性のリストをCSVファイルとしてエクスポートするには、ページ上部の**すべてエクスポート**を選択します。CSVファイルが生成され、ダウンロードリンクがメールで送信されます。

## カスタム属性のタイプを変更する {#change-custom-attribute-type}

### 前提条件 {#prerequisites}

カスタム属性が、アクティブなキャンペーン、キャンバス、またはセグメントで現在使用されていないことが必要です。属性がまだ参照されている状態でデータタイプを変更しようとすると、ダッシュボードにエラーが表示され、変更がブロックされます。

### データタイプの変更 {#changing-the-data-type}

1. セグメントやフィルターでその属性を使用しているアクティブなキャンペーンまたはキャンバスを停止します。
2. すべてのセグメント、キャンペーン、キャンバスフィルターからその属性を削除します。
3. **データ設定** > **カスタム属性**（または**カスタムイベント**）に移動し、属性を見つけて、目的のデータタイプに更新します。
4. 既存のユーザープロファイルの属性値を新しいデータタイプに合わせて更新します（例：[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を使用）。
5. 関連するセグメント、キャンペーン、キャンバスに属性を再適用し、停止したキャンペーンやキャンバスを再開します。

### 注意事項 {#things-to-know}

- **ユーザーデータは遡って更新されません。** ユーザープロファイルに古いデータタイプの属性があった場合、その値は変更されません。セグメンテーションフィルターは新しいデータタイプを検索するため、古い値を持つユーザーはプロファイルが更新されるまで、一致するセグメントから除外されます。
- **新しいデータは新しいデータタイプと一致する必要があります。** 変更後、この属性に対して以前のデータタイプを送信するAPI呼び出しやSDKイベントは受け付けられません。新しいデータタイプに一致する値のみが取り込まれます。
- **フィルターは自動的に更新されません。** 変更された属性を参照しているセグメントやキャンペーンのフィルターは遡って更新されません。変更後にフィルターを削除して再追加する必要があります。

## 使用状況レポートを表示する {#view-usage-reports}

使用状況レポートには、特定のカスタム属性を使用しているすべてのキャンバス、キャンペーン、セグメントが一覧表示されます。このリストにはLiquidの使用は含まれません。

対象のカスタム属性の横にあるチェックボックスを選択し、**使用状況レポートを表示**を選択すると、一度に最大100件の使用状況レポートを表示できます。

### 値タブ {#values-tab}

使用状況レポートを表示する際に、**値**タブを選択すると、約250,000人のユーザーのサンプルに基づいて、選択したカスタム属性の上位の値を確認できます。結果はユーザーのサブセットからサンプリングされるため、サンプルにはすべての既存の値が含まれるわけではありません。そのため、**値**タブはトラブルシューティングや、すべてのユーザーのデータを組み込む必要があるユースケースには使用しないでください。

![選択したカスタム属性の使用状況レポート。「値」タブが開かれ、「US」や「PR」などの国属性値の円グラフが表示されています。]({% image_buster /assets/img/usage_report_values.png %}){: style="max-width:80%;"}

## カスタム属性を設定する {#set-custom-attributes}

以下は、さまざまなプラットフォームでカスタム属性を設定するために使用されるメソッドの一覧です。

{% details プラットフォーム別のドキュメントを展開 %}

- [Android and FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=unity)
- [.NET MAUI (formerly Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes)

{% enddetails %}

## カスタム属性のストレージ {#custom-attribute-storage}

**ユーザープロファイル**に保存されるすべてのデータ（カスタム属性データを含む）は、各プロファイルが<a href="/docs/user_archival#active-users">アクティブ</a> である限り、無期限に保持されます。

カスタム属性として保存できるすべてのデータタイプ（ブール値、数値、文字列、配列、時間、オブジェクト、オブジェクトの配列）の完全なリファレンスについては、[カスタム属性のデータタイプ]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types)を参照してください。

### 空文字列とnull値 {#blank-strings-versus-null-values}

カスタム属性をクリアまたは設定解除する場合、空文字列（`""`）を渡すか`null`を渡すかによって動作が異なります。

| 値 | 動作 |
| --- | --- |
| `""`（空文字列） | 属性は空の値に設定され、ユーザープロファイルに引き続き表示されます。 |
| `null` | 属性はユーザープロファイルから完全に削除されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="空文字列とnull値" }
{: .reset-td-br-1 .reset-td-br-2 aria-label="空文字列とnull値" }
{: .reset-td-br-1 .reset-td-br-2 aria-label="空文字列とnull値" }

{% alert important %}
文字列以外のデータタイプで、Brazeダッシュボードでデータタイプが手動で設定されている場合（自動検出ではない場合）、値の設定を解除するには`null`を使用する必要があります。`""`の送信は文字列属性にのみ有効です。例えば、ブール値属性に`""`を設定すると空文字列として扱われ、そのタイプでは無効な値となります。ブール値の設定を解除するには、`null`を渡してください。

CSVインポートは`null`をサポートしていない点に注意してください。CSVインポートのブール値は`TRUE`または`FALSE`である必要があります。
{% endalert %}