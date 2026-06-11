---
nav_title: Currents用Amplitude
article_title: Currents用Amplitude
page_order: 0
description: "このリファレンス記事では、Braze Currentsと、製品分析およびビジネスインテリジェンスプラットフォームであるAmplitudeとのパートナーシップについて説明します。"
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Currents用Amplitude {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomamplitude-integration-with-braze-stylefloatrightwidth120pxborder0-classnoimgborderamplitude-for-currents}

> [Amplitude](https://amplitude.com/) は製品分析およびビジネスインテリジェンスプラットフォームです。

BrazeとAmplitudeの双方向統合により、[Amplitudeコホート]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences/)、ユーザー特性、およびイベントをBrazeに同期できます。また、Braze Currentsを活用して[BrazeイベントをAmplitudeにエクスポートし](#data-export-integration)、製品データとマーケティングデータのより深い分析を実行できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Amplitudeアカウント | このパートナーシップを活用するには、[Amplitudeアカウント](https://amplitude.com/)が必要です。 |
| Currents | Amplitudeにデータをエクスポートするには、アカウントに[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## データエクスポートの統合 {#data-export-integration}

BrazeからAmplitudeにエクスポートできるイベントとイベントプロパティの完全なリストは、以下のセクションに記載されています。Amplitudeに送信されるすべてのイベントには、ユーザーの`external_user_id`がAmplitudeユーザーIDとして含まれます。Braze固有のイベントプロパティは、Amplitudeに送信されるデータの`event_properties`キーで送信されます。

{% alert important %}
この機能を使用するには、AmplitudeのユーザーIDがBrazeのexternal IDに一致している必要があります。
{% endalert %}

Brazeがイベントデータを送信するのは、`external_user_id`を設定したユーザーか、`device_id`を設定した匿名ユーザーのみです。匿名ユーザーの場合は、SDKでAmplitudeのデバイスIDとBrazeのデバイスIDを同期させる必要があります。以下に例を示します。

```java
amplitude.setDeviceId(Appboy.getInstance(context).getDeviceId();)
```

Amplitudeには2種類のイベントをエクスポートできます。[メッセージエンゲージメントイベント](#supported-currents-events)（メッセージ送信に直接関連するBrazeイベントで構成される）と、[顧客行動イベント](#supported-currents-events)（セッション、カスタムイベント、プラットフォーム経由で追跡された購入などのその他のアプリまたはWebサイトアクティビティを含む）です。すべての標準的なイベントには`[Appboy]`が接頭辞として付加され、すべてのカスタムイベントには`[Appboy] [Custom Event]`が付加されます。カスタムイベントプロパティの接頭辞は`[Custom event property]`、購入イベントプロパティの接頭辞は`[Purchase property]`です。

名前が付けられBrazeにインポートされるすべてのコホートには、接頭辞として`[Amplitude]`が、接尾辞として`cohort_id`が付加されます。これは、「TEST_COHORT」という名前のコホートで`cohort_id`が「abcd1234」の場合、Brazeフィルターでは`[Amplitude] TEST_COHORT: abcd1234`という名前になることを意味します。

その他のイベントの種類にアクセスする必要がある場合は、アカウントマネージャーに問い合わせるか、[サポートチケット]({{site.baseurl}}/braze_support/)を開いてください。

### ステップ 1: BrazeでAmplitude統合を設定する {#step-1-configure-amplitude-integration-in-braze}

Amplitudeで、AmplitudeエクスポートAPIキーを見つけます。

{% alert warning %}
Amplitude APIキーを最新の状態に保ってください。コネクターの認証情報が期限切れになると、コネクターはイベントの送信を停止します。この状態が**48時間**以上続くと、コネクターのイベントは削除され、データは永久に失われます。
{% endalert %}

### ステップ 2: Braze Currentを作成する {#step-2-create-braze-current}

Brazeで**Currents > + Create Current > Create Amplitude Export**に移動します。統合名、連絡先メール、AmplitudeエクスポートAPIキー、およびAmplitudeリージョンを、リストされているフィールドに入力します。次に、追跡したいイベントを選択します。利用可能なイベントのリストが提供されます。最後に**Launch Current**をクリックします。

{% alert note %}
Braze CurrentsからAmplitudeに送信されたイベントは、Amplitudeのイベントボリューム割り当ての対象となります。
{% endalert %}

![Braze Amplitude Currentsページ。このページには、統合名、連絡先メール、APIキー、USリージョンのフィールドがあります。Currentsページの下半分には、送信可能なCurrentsイベントが表示されます。]({% image_buster /assets/img/amplitude4.png %})

{% tab note %}
詳細については、Amplitudeの[統合に関するドキュメント](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration)を参照してください。
{% endtab %}

## レート制限 {#rate-limits}

CurrentsはAmplitudeのHTTP APIに接続しますが、このAPIには1デバイスあたり30イベント/秒という[レート制限](https://developers.amplitude.com/docs/http-api-v2#upload-limit)と、1デバイスあたり500Kイベント/日という文書化されていない制限があります。これらのしきい値を超えた場合、AmplitudeはCurrentsを通じて記録されるイベントをスロットリングします。統合内のデバイスがこのレート制限を超えると、すべてのデバイスからのイベントがAmplitudeに表示されるタイミングが遅れることがあります。

通常の状況では、デバイスが報告するイベント数は30イベント/秒または500Kイベント/日を超えることはありません。このようなイベントパターンは、統合の設定に誤りがある場合にのみ発生します。このような遅延を回避するには、SDK統合がSDK統合手順で指定されている通常のレートでイベントを報告するようにし、1つのデバイスに対して多くのイベントを生成する自動テストの実行を控えてください。

## サポートされているCurrentsイベント {#supported-currents-events}

Brazeでは、以下のイベントをAmplitudeにエクスポートできます。

- [メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)
- [顧客行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)

各イベントのペイロード構造については、[メッセージエンゲージメントイベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)および[顧客行動イベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)の**Amplitude**タブを選択してください。