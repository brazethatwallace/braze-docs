---
nav_title: Currents用Amplitude
article_title: Currents用Amplitude
page_order: 0
description: "このリファレンス記事では、Braze Currentsと、製品分析およびビジネスインテリジェンスプラットフォームであるAmplitudeとのパートナーシップについて説明します。"
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Currents用Amplitude {#amplitude-for-currents}

> [Amplitude](https://amplitude.com/) は製品分析およびビジネスインテリジェンスプラットフォームです。

BrazeとAmplitudeの双方向統合により、[Amplitudeコホート]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences)、ユーザー特性、およびイベントをBrazeに同期できます。また、Braze Currentsを活用して[BrazeイベントをAmplitudeにエクスポートし](#data-export-integration)、製品データとマーケティングデータのより深い分析を実行できます。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| Amplitude アカウント | このパートナーシップを利用するには、[Amplitude アカウント](https://amplitude.com/)が必要です。 |
| Currents | データを Amplitude にエクスポートするには、アカウントに [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## データエクスポート連携 {#data-export-integration}

BrazeからAmplitudeにエクスポートできるイベントとイベントプロパティの完全なリストは、以下のセクションに記載されています。Amplitudeに送信されるすべてのイベントには、ユーザーの`external_user_id`がAmplitudeユーザーIDとして含まれます。Braze固有のイベントプロパティは、Amplitudeに送信されるデータの`event_properties`キーの下で送信されます。

{% alert important %}
この機能を使用するには、AmplitudeのユーザーIDがBrazeのexternal IDと一致している必要があります。
{% endalert %}

Brazeは、`external_user_id`が設定されているユーザー、または`device_id`が設定されている匿名ユーザーのイベントデータのみを送信します。匿名ユーザーの場合、SDKでAmplitudeのデバイスIDとBrazeのデバイスIDを同期する必要があります。例：

```java
amplitude.setDeviceId(Appboy.getInstance(context).getDeviceId();)
```

Amplitudeにエクスポートできるイベントは2種類あります。[メッセージエンゲージメントイベント](#supported-currents-events)は、メッセージ送信に直接関連するBrazeイベントで構成されます。[顧客行動イベント](#supported-currents-events)には、セッション、カスタムイベント、プラットフォームを通じて追跡される購入など、その他のアプリやWebサイトのアクティビティが含まれます。すべての通常イベントには`[Appboy]`のプレフィックスが付き、すべてのカスタムイベントには`[Appboy] [Custom Event]`のプレフィックスが付きます。カスタムイベントプロパティと購入イベントプロパティには、それぞれ`[Custom event property]`と`[Purchase property]`のプレフィックスが付きます。

{% alert note %}
Braze Currentsは、Amplitudeにイベントをエクスポートする際に`[Appboy]`プレフィックスを適用します。このラベルはBrazeのレガシー製品名を参照しています。これは想定された動作であり、SDKや連携の問題を示すものではありません。
{% endalert %}

Brazeに命名およびインポートされたすべてのコホートには、`[Amplitude]`のプレフィックスと`cohort_id`のサフィックスが付きます。つまり、`cohort_id`が「abcd1234」で「TEST_COHORT」という名前のコホートは、Brazeフィルターでは`[Amplitude] TEST_COHORT: abcd1234`と表示されます。

追加のイベント権限にアクセスする必要がある場合は、アカウントマネージャーに連絡するか、[サポートチケット]({{site.baseurl}}/braze_support)を開いてください。

### ステップ1：BrazeでAmplitude連携を設定する {#step-1-configure-amplitude-integration-in-braze}

Amplitudeで、AmplitudeエクスポートAPIキーを確認します。

{% alert warning %}
AmplitudeのAPIキーを最新の状態に保ってください。コネクタの認証情報が期限切れになると、コネクタはイベントの送信を停止します。**48時間**以上この状態が続くと、コネクタのイベントは破棄され、データは永久に失われます。
{% endalert %}

### ステップ2：Braze Currentを作成する {#step-2-create-braze-current}

Brazeで、**Currents > + Create Current > Create Amplitude Export** に移動します。連携名、連絡先メールアドレス、AmplitudeエクスポートAPIキー、およびAmplitudeリージョンを所定のフィールドに入力します。次に、追跡するイベントを選択します。利用可能なイベントのリストが表示されます。最後に、**Launch Current** をクリックします。

{% alert note %}
Braze CurrentsからAmplitudeに送信されたイベントは、Amplitudeのイベントボリュームクォータにカウントされます。
{% endalert %}

![Braze Amplitude Currentsページ。このページには、連携名、連絡先メールアドレス、APIキー、USリージョンのフィールドがあります。Currentsページの下半分には、送信可能なCurrentsイベントの一覧が表示されます。]({% image_buster /assets/img/amplitude4.png %})

{% alert tip %}
AmplitudeのAPIキーを貼り付ける際に「Invalid API key」エラーが表示される場合は、キーを手動で入力してみてください。一部のブラウザでは、コピー＆ペースト時に非表示の文字が追加され、バリデーションエラーの原因となることがあります。
{% endalert %}

{% tab note %}
詳細については、Amplitudeの[Appboy Amplitude Integration](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration)を参照してください。
{% endtab %}

## レート制限 {#rate-limits}

CurrentsはAmplitudeのHTTP APIに接続します。このAPIには、デバイスあたり30イベント/秒の[レート制限](https://developers.amplitude.com/docs/http-api-v2#upload-limit)と、デバイスあたり1日50万イベントの非公開の制限があります。これらのしきい値を超えると、AmplitudeはCurrentsを通じてログされたイベントをスロットリングします。インテグレーション内のデバイスがこのレート制限を超えた場合、すべてのデバイスからのイベントがAmplitudeに表示されるまでに遅延が発生する可能性があります。

通常の状況では、デバイスが30イベント/秒または1日50万イベントを超えてレポートすることはなく、このイベントパターンはインテグレーションの設定ミスによってのみ発生します。この種の遅延を回避するには、SDKインテグレーションの手順に記載されている通常のレートでイベントをレポートするようにSDKインテグレーションを設定し、単一のデバイスで多数のイベントを生成する自動テストの実行を控えてください。

## サポートされている Currents イベント {#supported-currents-events}

Brazeは、以下のイベントをAmplitudeにエクスポートすることをサポートしています。

- [メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)
- [顧客行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)

各イベントのペイロード構造については、[メッセージエンゲージメントイベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)および[顧客行動イベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)で **Amplitude** タブを選択してください。