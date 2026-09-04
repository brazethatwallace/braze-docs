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

BrazeとAmplitudeの双方向統合により、[Amplitudeコホート]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences)、ユーザー特性、およびイベントをBrazeに同期できます。また、Braze Currentsを活用して[BrazeイベントをAmplitudeにエクスポートし](#data-export-integration)、製品データとマーケティングデータのより深い分析を実行できます。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| Amplitude アカウント | このパートナーシップを利用するには、[Amplitude アカウント](https://amplitude.com/)が必要です。 |
| Currents | Amplitude にデータをエクスポートするには、アカウントに [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## データエクスポートの連携 {#data-export-integration}

BrazeからAmplitudeにエクスポートできるイベントとイベントプロパティの完全なリストは、以下のセクションに記載されています。Amplitudeに送信されるすべてのイベントには、ユーザーの`external_user_id`がAmplitudeユーザーIDとして含まれます。Braze固有のイベントプロパティは、Amplitudeに送信されるデータの`event_properties`キーの下に送信されます。

{% alert important %}
この機能を使用するには、AmplitudeのユーザーIDがBrazeのexternal IDと一致する必要があります。
{% endalert %}

Brazeは、`external_user_id`が設定されているユーザー、または`device_id`が設定されている匿名ユーザーのイベントデータのみを送信します。匿名ユーザーの場合、SDKでAmplitudeのデバイスIDをBrazeのデバイスIDと同期する必要があります。例：

```java
amplitude.setDeviceId(Appboy.getInstance(context).getDeviceId();)
```

Amplitudeには2種類のイベントをエクスポートできます。メッセージ送信に直接関連するBrazeイベントで構成される[メッセージエンゲージメントイベント](#supported-currents-events)と、セッション、カスタムイベント、プラットフォームを通じて追跡された購入などのアプリやWebサイトのアクティビティを含む[顧客行動イベント](#supported-currents-events)です。すべての通常イベントには`[Appboy]`というプレフィックスが付き、すべてのカスタムイベントには`[Appboy] [Custom Event]`というプレフィックスが付きます。カスタムイベントと購入イベントのプロパティには、それぞれ`[Custom event property]`と`[Purchase property]`というプレフィックスが付きます。

{% alert note %}
Braze Currentsは、Amplitudeにイベントをエクスポートする際に`[Appboy]`プレフィックスを付与します。このラベルはBrazeのレガシー製品名を参照しています。これは想定された動作であり、SDKや連携の問題を示すものではありません。
{% endalert %}

Brazeに命名されインポートされたすべてのコホートには、`[Amplitude]`というプレフィックスと`cohort_id`のサフィックスが付きます。つまり、`cohort_id`が「abcd1234」の「TEST_COHORT」というコホートは、Brazeフィルターでは`[Amplitude] TEST_COHORT: abcd1234`というタイトルになります。

追加のイベントエンタイトルメントへのアクセスが必要な場合は、アカウントマネージャーに連絡するか、[サポートチケット]({{site.baseurl}}/user_guide/administer/personal/braze_support)を開いてください。

### ステップ1：BrazeでAmplitude連携を設定する {#step-1-configure-amplitude-integration-in-braze}

Amplitudeで、AmplitudeエクスポートAPIキーを確認します。

{% alert warning %}
AmplitudeのAPIキーを最新の状態に保ってください。コネクタの認証情報が期限切れになると、コネクタはイベントの送信を停止します。これが**48時間**以上続くと、コネクタのイベントは破棄され、データは永久に失われます。
{% endalert %}

### ステップ2：Braze Currentを作成する {#step-2-create-braze-current}

Brazeで、**Currents > + Create Current > Create Amplitude Export** に移動します。連携名、連絡先メールアドレス、AmplitudeエクスポートAPIキー、およびAmplitudeリージョンをリストされたフィールドに入力します。次に、追跡したいイベントを選択します。利用可能なイベントのリストが提供されます。最後に、**Launch Current** をクリックします。

{% alert note %}
Braze CurrentsからAmplitudeに送信されたイベントは、Amplitudeのイベントボリュームクォータにカウントされます。
{% endalert %}

![Braze AmplitudeのCurrentsページ。このページには、連携名、連絡先メールアドレス、APIキー、USリージョンのフィールドがあります。Currentsページの下半分には、送信可能なCurrentsイベントが一覧表示されています。]({% image_buster /assets/img/amplitude4.png %})

{% alert tip %}
AmplitudeのAPIキーを貼り付ける際に「Invalid API key」エラーが表示される場合は、キーを手動で入力してみてください。一部のブラウザでは、コピー＆ペースト時に非表示の文字が追加され、バリデーションエラーが発生することがあります。
{% endalert %}

{% tab note %}
詳細については、Amplitudeの[Appboy Amplitude Integration](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration)を参照してください。
{% endtab %}

## レート制限 {#rate-limits}

CurrentsはAmplitudeのHTTP APIに接続します。このAPIには、デバイスあたり30イベント/秒の[レート制限](https://developers.amplitude.com/docs/http-api-v2#upload-limit)と、デバイスあたり1日500Kイベントの非公開の制限があります。これらのしきい値を超えると、AmplitudeはCurrentsを通じて記録されたイベントをスロットリングします。インテグレーション内のデバイスがこのレート制限を超えた場合、すべてのデバイスからのイベントがAmplitudeに表示されるまでに遅延が発生する可能性があります。

通常の状況では、デバイスが30イベント/秒または1日500Kイベントを超えるレポートを行うことはありません。このイベントパターンは、インテグレーションの設定ミスによってのみ発生します。このような遅延を回避するには、SDKインテグレーションの手順に記載されている通常のレートでイベントをレポートするようにSDKインテグレーションを設定し、単一のデバイスに対して大量のイベントを生成する自動テストの実行を控えてください。

## サポートされているCurrentsイベント {#supported-currents-events}

Brazeは、以下のイベントをAmplitudeにエクスポートすることをサポートしています。

- [メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)
- [顧客行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)

各イベントのペイロード構造については、[メッセージエンゲージメントイベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)および[顧客行動イベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)の **Amplitude** タブを選択してください。