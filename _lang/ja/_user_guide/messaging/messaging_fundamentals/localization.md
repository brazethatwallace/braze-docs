---
nav_title: ローカライゼーション
article_title: ローカライゼーション
page_order: 8
description: "このリファレンス記事では、ローカライゼーションの基本、CampaignsとCanvasesにおけるさまざまなオーケストレーションアプローチの利点、およびメッセージングでパーソナライゼーションを処理するさまざまな方法について説明します。"
tool:
    - Campaigns
    - Canvas
---

# ローカライゼーション {#localization}

> 多くの国に顧客を持つ企業にとって、Brazeの導入初期にローカライゼーションに取り組むことで、時間とリソースを節約できます。

## 仕組み {#how-it-works}

ロケール情報は、[Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration)（自動）または[REST API]({{ site.baseurl }}/api/endpoints/user_data/post_user_track)を使用して収集したデータに基づいて、ユーザーのプロファイルに保存されます。ロケールには言語と地域識別子が含まれます。この情報は、Brazeのセグメンテーションツールで**国**と**言語**の下から利用できます。

{% alert tip %}
SDKによるロケールの収集方法の技術的な詳細については、[iOS](https://developer.apple.com/library/ios/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html)、[Android](http://developer.android.com/reference/java/util/Locale.html)、[Web](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/language)の公式ドキュメントを参照してください。
{% endalert %}

## 翻訳管理 {#translation-management}

翻訳を管理するために、以下のアプローチを検討してください。

{% tabs local %}
{% tab Campaign %}
### すべてに1つのテンプレート {#one-template-for-all}

このアプローチでは、[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)を使用して、Braze内の単一のテンプレートにローカライゼーションを適用します。送信後、ダッシュボードには集約されたCampaign分析が表示されます。ユーザーレベルのエンゲージメントは、カスタムSegmentファネルを使用して測定できます。たとえば、**国**と**受信したCampaign**フィルターを組み合わせることで測定できます。

| メリット | 考慮事項 |
| --- | --- |
| - 一元化されたアプローチ<br>- メール作成時間の短縮、メールを複数回作成する必要がない | - 手動でのレポート作成<br>- Campaignレポートには国別ではなく集約された指標が表示される<br>- Liquidが期待どおりに表示されることを十分にテストする必要がある<br>- 国の値の取得方法や設定した国の数によっては、各国のテストが難しい場合がある<br>- タイムゾーンをまたいだ特定の時間での送信スケジュールが難しい<br>- 国ごとに異なるコンテンツを送信したい場合に使いにくい |
| --- | --- | --- |
{: .reset-td-br-1 .reset-td-br-2 aria-label="すべてに1つのテンプレート" }

### 国ごとに1つのテンプレート {#one-template-per-country}

このアプローチでは、テンプレートを異なる送信ロケールに分離します。送信後、ダッシュボードは各国ごとに送信分析をレポートし、下流のユーザーレベルの[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents#access-currents)イベントも特定のCampaignに紐付けられます。

- テンプレートは、メンテナンスとトラッキングの目的で[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags#tags)を実装することで恩恵を受けます。
- Campaignsは、同じ[Brazeテンプレート]({{site.baseurl}}/user_guide/messaging/templates)と[Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)（Liquidを含む[メールテンプレート]({{site.baseurl}}/user_guide/messaging/templates/email_templates)など）から設定を継承できます。
- 既存のCampaignsとテンプレートは[複製]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/duplicating)して、より迅速な価値実現が可能です。

| メリット | 考慮事項 |
| --- | --- |
| - 複数のロケーションにスケーラブル<br>- Braze内での国別収益レポート（Campaign単位など）<br>- 国ごとに大幅に異なるコンテンツがある場合の柔軟性 | - 戦略的な構造化が必要<br>- より多くの構築作業が必要（各国ごとに個別のCampaignsなど） |
{: .reset-td-br-1 .reset-td-br-2 aria-label="国ごとに1つのテンプレート" }
{% endtab %}

{% tab Canvas %}
### すべてに1つのジャーニー {#one-journey-for-all}

このアプローチでは、[Canvasの基本]({{site.baseurl}}/user_guide/messaging/canvas/canvas_basics#building-the-customer-journey)とLiquidを使用して、各ユーザーのメッセージングを定義し、ローカライゼーションを処理します。

Canvasが送信された後、ダッシュボードには集約された[Canvas分析]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics)が表示されます。ユーザーレベルのエンゲージメントは、カスタム[Segmentファネル]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size)を使用して測定できます。たとえば、[**国**]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#country)と[**受信したキャンバスステップ**]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#received-canvas-step)フィルターを組み合わせることで測定できます。

| メリット | 考慮事項 |
| --- | --- |
| - 一元化されたアプローチ<br>- メール作成時間の短縮 - メールを複数回作成する必要がない | - 手動でのレポート作成<br>- Canvasレポートには国別ではなく集約された指標が表示される<br>- Liquidが期待どおりに表示されることを十分にテストする必要がある<br>- 国の値の取得方法や設定した国の数によっては、各国のテストが難しい場合がある<br>- タイムゾーンをまたいだ特定の時間での送信スケジュールが難しい<br>- 国ごとに異なるコンテンツを送信したい場合に使いにくい |
{: .reset-td-br-1 .reset-td-br-2 aria-label="すべてに1つのジャーニー" }

### 国ごとに1つのジャーニー {#one-journey-per-country}

このアプローチでは、[Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)ジャーニービルダーが、複数の[Canvasコンポーネント]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components)を使用してユーザージャーニーを作成する柔軟性を提供します。これらのコンポーネントは、コンポーネントレベルおよびジャーニー全体のレベルで[複製]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/duplicating)できます。

ローカライゼーションは以下の方法で実現できます：

- 国ごとに個別のCanvases。これにより、オーディエンスフィルターを使用してファネルの上部で複雑なユーザージャーニーが定義されます
- 国ごとのカスタムユーザージャーニー。[オーディエンスパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)を実装して、各ジャーニーで大規模にユーザーを直感的にセグメント化し、単一のCanvas内で各国ごとに個別のメッセージスレッドを作成します

送信後、ダッシュボードは顧客の現在のロケーションに基づいて、国別の動的な分析とユーザーレベルの[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents#access-currents)イベントを提供します。

| メリット | 考慮事項 |
| --- | --- |
| - Braze内での国別収益レポート（Canvas、バリアント、ステップ単位など）<br>- 国ごとに大幅に異なるコンテンツがある場合の柔軟性<br>- 将来的にジャーニーの一部として他のチャネルを追加可能 | - 戦略的な構造化が必要<br>- より多くの構築作業が必要（各国ごとに個別のメッセージステップなど）<br>- 単一のCanvas内で各国ごとにカスタムの複雑なジャーニーがある場合、Canvasが大きくなり読みにくくなる可能性がある |
{: .reset-td-br-1 .reset-td-br-2 aria-label="国ごとに1つのジャーニー" }
{% endtab %}
{% endtabs %}

## 翻訳されたメッセージの送信 {#sending-translated-messages}

ユーザーの言語、ロケール、またはカスタム属性に基づいてパーソナライズされたメッセージを送信するには、以下のいずれかの方法を使用してください。

### 翻訳Liquidタグ（推奨） {#translation-liquid-tag}

Brazeは、単一のメッセージで異なる言語のユーザーをターゲットにするための{% raw %}`{% translation salutation %}Hello!{% endtranslation %}`{% endraw %} Liquidタグをサポートしています。

詳しい手順については、[翻訳タグの使用ガイド]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)を参照してください。

### 代替アプローチ {#alternative-approaches}

{% tabs local %}
{% tab カスタムLiquid %}
メッセージ本文にコンテンツを手動で貼り付け、[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize)を使用して受信者に正しい言語を[条件付き]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic)で表示できます。これを行うには：

1. メッセージを作成し、**Language**を選択して、選択した各言語のLiquid条件ロジックを生成します。
2. 以下のLiquidテンプレートを使用してメッセージを構築できます。テンプレートを含む各フィールドについて、テンプレートの括弧付きセグメントの後にバリエーションを入力する必要があります。バリエーションは、その前の括弧内で参照されている言語コードに対応する必要があります。
    {% raw %}
    ```liquid
    {% if ${language} == 'en' %}
    This is a message in English from Braze!
    {% elsif ${language} == 'es' %}
    Este es un mensaje en español de Braze !
    {% elsif ${language} == 'zh' %}
    这是一条来自Braze的中文消息。
    {% else %}
    This is a message from Braze! This will go to anyone who does not match the other specified languages!
    {% endif %}
    ```
    {% endraw %}
3. 送信前にユーザーのIDまたはメールアドレスを入力して、言語に応じてメッセージがどのように表示されるかを確認し、メッセージをテストしてください。

{% alert tip %}
メッセージングには常に{% raw %}`{% else %}`{% endraw %}ステートメントを含めることをお勧めします。ほとんどのユーザーは特定の言語のメッセージを見ますが、以下のユーザーにはこのテキストが表示されます：
- 言語が選択されていない
- Brazeがサポートしていない言語を使用している
- デバイスの言語が検出できない
{% endalert %}
{% endtab %}

{% tab Content Blocks %}
Brazeの[Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)は再利用可能なコンテンツブロックです。ブロックが変更されると、そのブロックへのすべての参照が変更されます。たとえば、メールのヘッダーやフッターの更新はすべてのメールに反映されます。また、翻訳を格納するためにも使用できます。これらのブロックはREST APIを使用して[作成]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block#create-content-block)および[更新]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block)することもでき、ユーザーはプログラムで翻訳をアップロードできます。

ダッシュボードでCampaignを構築する際、Content Blocksはタグ{% raw %}`{{content_blocks.${name_of_content_block}}}`{% endraw %}を使用して参照できます。これらのブロックには、オプション1に示すように各言語の条件ロジック内にすべての翻訳を含めることも、各言語ごとに個別のブロックを使用することもできます。

Content Blocksは翻訳管理プロセスとしても活用できます。翻訳が必要なコンテンツをContent Block内に格納し、取得、翻訳、更新します：
1. ダッシュボードで「Needs Translation」タグ付きのContent Blockを手動で作成します。
2. サービスが[`/content_blocks/list`エンドポイント]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks)を使用して、すべてのContent Blocksを毎晩取得します。
3. サービスが[`/content_blocks/info`エンドポイント]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information)を通じて各Content Blockの詳細を取得し、翻訳対象としてタグ付けされたブロックを確認します。
4. 翻訳サービスが「Needs Translation」のすべてのContent Blocksの本文を翻訳します。
5. サービスが[`/content_block/update`エンドポイント]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block)にアクセスして、翻訳されたコンテンツを更新し、タグを「Translation Complete」に更新します。
{% endtab %}

{% tab カタログ %}
[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs)を使用すると、APIおよびCSVファイルを介してインポートされたJSONオブジェクトからデータにアクセスし、カスタム属性やカスタムイベントプロパティと同様にLiquidを通じてメッセージを充実させることができます。例：

{% subtabs local %}
{% subtab API %}

以下のAPI呼び出しでカタログを作成します：
```bash
curl --location --request POST 'https://your_api_endpoint/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "catalogs": [
   {
     "name": "translations",
     "description": "My localization samples",
     "fields": [
       {
         "name": "id",
         "type": "string"
       },
       {
         "name": "context",
         "type": "string"
       },
       {
         "name": "language",
         "type": "string"
       },
       {
         "name": "body",
         "type": "string"
       }
     ]
   }
 ]
}'
```

以下のAPI呼び出しでアイテムを追加します：

```bash
curl --location --request POST 'https://your_api_endpoint/catalogs/translations/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "items": [
   {
     "id": "1",
     "context": "1",
     "language": "en",
     "body": "Hey"
   },
   {
     "id": "2",
     "context": "1",
     "language": "es",
     "body": "Hola"
   },
   {
     "id": "3",
     "context": "1",
     "language": "pt",
     "body": "Oi"
   },
   {
     "id": "4",
     "context": "1",
     "language": "de",
     "body": "Hallo"
   }
 ]
}'
```
{% endsubtab%}
{% subtab CSV %}
以下の形式でCSVを作成します：

| id | context | language | body |
| --- | --- | --- | --- |
| 1 | 1 | en | Hey |
| 2 | 1 | es | Hola |
| 3 | 1 | pt | Oi |
| 4 | 1 | de | Hallo |
| 5 | 2 | en | Hey |
| 6 | 2 | es | Hola |
| 7 | 2 | pt | Oi |
| 8 | 2 | de | Hallo |
| 9 | 3 | en | Hey |
| 10 | 3 | es | Hola |
| 11 | 3 | pt | Oi |
| 12 | 3 | de | Hallo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="代替アプローチ" }
{% endsubtab %}
{% endsubtabs %}

これらのカタログアイテムは、以下に示す[パーソナライゼーション]({{site.baseurl}}/user_guide/data/activation/catalogs/create#using-catalogs-in-a-message)、またはデータのグループを作成できる[セレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)を使用して参照できます。

{% raw %}
```liquid
{% catalog_items translations 1 %}
{{items[0].body}}
//returns “Hey”
```
{% endraw %}
{% endtab %}

{% tab Brazeパートナー %}
多くのBrazeパートナーが、[Transifex]({{site.baseurl}}/partners/message_personalization/localization/transifex#about-transifex)や[Crowdin](https://crowdin.com/)などのローカライゼーションソリューションを提供しています。通常、ユーザーは社内チームや翻訳エージェンシーと併せてプラットフォームを使用します。翻訳はそこにアップロードされ、REST APIを介してアクセスできるようになります。これらのサービスは[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)も活用することが多く、ユーザーはAPIを介して翻訳を取得できます。

たとえば、以下のコネクテッドコンテンツ呼び出しはTransifexとCrowdinを呼び出して翻訳を取得し、{% raw %}`{{${language}}}`{% endraw %}を活用して特定のユーザーに対する正しい翻訳を識別します。この翻訳はJSONブロック「strings」に保存され、参照されます。

{% subtabs local %}
{% subtab Transifexの例 %}
{% raw %}
```liquid
{% connected_content https://www.transifex.com/api/2/project/example/resource/example/translation/{{${language}}}/strings :basic_auth semc :save strings %}
{{strings[0].translation}}
```
{% endraw %}
{% endsubtab %}
{% subtab Crowdinの例 %}
{% raw %}
```liquid
{% connected_content https://api.crowdin.com/api/project/braze-test/export-file?key=you_api_key&language={{${language}}}&file=test.json&export_translated_only=1 :save response %}
{{response.value_1}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab スプレッドシート %}
スプレッドシートに翻訳を格納し、以下のいずれかの方法を使用して関連する言語でメッセージを送信します。

{% subtabs local %}
{% subtab コネクテッドコンテンツ %}
翻訳エージェンシーと協力してGoogleスプレッドシートに翻訳を保存し、[Brazeコネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)を使用してこのコンテンツをクエリできます。メッセージを送信すると、各ユーザーの選択した言語に基づいて、関連する翻訳がCampaign本文に取り込まれます。

{% alert note %}
Google Sheets APIには、プロジェクトあたり100秒間に500リクエストの制限があります。コネクテッドコンテンツ呼び出しはキャッシュできますが、このソリューションは高トラフィックのCampaignにはスケーラブルではありません。
{% endalert %}
{% endsubtab %}

{% subtab SheetDB経由のJSON API %}
このオプションは、GoogleスプレッドシートをコネクテッドコンテンツでクエリされるJSONオブジェクトに変換する代替方法を提供します。スプレッドシートをSheetDB経由でJSON APIに変換することで、API呼び出しの頻度に応じて[複数のサブスクリプションティア](https://sheetdb.io/pricing)から選択できます。

スプレッドシートの構造はオプション4の手順に従いますが、SheetDBはオブジェクトをクエリするための[追加フィルター](https://docs.sheetdb.io/#sheetdb-api)も提供しています。

一部のユーザーは、SheetDBの[検索メソッド](https://docs.sheetdb.io/#get-search-in-document)をGETリクエスト呼び出しに実装して、{% raw %}`{{${language}}}`{% endraw %} Liquidタグに基づいてJSONオブジェクトをフィルタリングし、大きな条件ブロックを構築する代わりに単一の言語の結果を自動的に返すことで、LiquidとConnected Blockの依存関係を減らしてSheetDBを実装することを好む場合があります。

#### ステップ1：Googleスプレッドシートのフォーマット {#step-1-format-the-google-sheet}

まず、言語が異なるオブジェクトになるようにGoogleスプレッドシートを構築します：

| language | title1 | body1 | title2 | body2 |
| en | Hey | 1 | Hey2 | 5 |
| es | Hola | 2 | Hola2 | 6 |
| pt | Oi | 3 | Oi2 | 7 |
| de | Hallo | 4 | Hallo2 | 8 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="ステップ1：Googleスプレッドシートのフォーマット" }

#### ステップ2：コネクテッドコンテンツ呼び出しで言語Liquidタグを使用 {#step-2-use-the-language-liquid-tag-in-a-connected-content-call}

次に、コネクテッドコンテンツ呼び出し内で{% raw %}`{{${language}}}`{% endraw %} Liquidタグを実装します。SheetDBはスプレッドシートの作成時に`sheet_id`を自動生成します。

{% raw %}
```liquid
{% connected_content https://sheetdb.io/api/v1/[sheet_id]/search?language={{${language}}} :save result%}
```
{% endraw %}

#### ステップ3：メッセージのテンプレート化 {#step-3-template-your-messages}

最後に、Liquidを使用してメッセージをテンプレート化します：

{% raw %}
```liquid
{{result[0].title1}} //returns “Hey”
{{result[0].title2}} //returns “Hey2”
```
{% endraw %}

##### 考慮事項 {#considerations}

- {% raw %}`{{${language}}}`{% endraw %}フィールドはすべてのユーザーに対して定義されている必要があります。定義されていない場合、言語が設定されていないユーザーのフォールバックハンドラーとしてLiquid条件ブロックを含める必要があります。
- Googleスプレッドシート内のデータモデリングは、メッセージオブジェクトを持つのではなく、言語駆動の縦方向の構造に従う必要があります。
- SheetDBは限定的な無料アカウントと複数の有料オプションを提供しており、Campaign戦略に基づいて検討する必要があります。
- コネクテッドコンテンツ呼び出しはキャッシュできます。API呼び出しの予測頻度を測定し、検索メソッドを使用する代わりにメインのSheetDBエンドポイントを呼び出す代替アプローチを検討することをお勧めします。
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}