---
nav_title: Amplitude
article_title: Amplitude
page_order: 0
alias: /partners/amplitude_recommend/
description: "この参考記事では、Brazeと製品分析およびビジネスインテリジェンスプラットフォームであるAmplitudeのパートナーシップについて概説しています。"
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Braze Learningコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomamplitude-integration-with-braze-stylefloatrightwidth120pxborder0-classnoimgborderamplitude}

> [Amplitude](https://amplitude.com/) は製品分析およびビジネスインテリジェンスプラットフォームです。

BrazeとAmplitudeの双方向統合により、[Amplitudeコホート]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import)、ユーザー特性、およびイベントをBrazeにインポートし、将来のキャンペーンやキャンバスでユーザーをターゲティングできるセグメントを作成できます。また、Braze Currentsを利用して[BrazeイベントをAmplitudeにエクスポートし]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents#data-export-integration)、製品データやマーケティングデータの詳細な分析を行うこともできます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Amplitudeアカウント | このパートナーシップを活用するには、[Amplitudeアカウント](https://amplitude.com/)が必要です。 |
| Currents | Amplitudeにデータをエクスポートするには、アカウントに[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents)を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合を選択する {#choose-an-integration}

AmplitudeとBrazeは2つの異なる統合方法を提供しています。以下のドキュメントを参照して、ニーズに適した方法を判断してください。

- Brazeイベントストリーミング：Amplitudeの生イベントデータをそのままBrazeに転送できる統合です。
- [コホートインポート]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import)：AmplitudeのコホートをBrazeに転送できる統合です。

## Brazeイベントストリーミング {#braze-event-streaming}

### 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Braze REST APIキー | すべての権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL][1]。エンドポイントはインスタンスのBraze URLに応じて異なります。 |
| Brazeアプリ識別子 | Amplitudeイベントを受け取るアプリの識別子です。これは、**Brazeダッシュボード > 開発者コンソール > 設定**で確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

### Amplitudeの設定 {#amplitude-setup}

1. Amplitudeで**Data Destinations**に移動し、「Braze - Event Stream」を探します。
2. 同期名を入力し、**Create Sync**をクリックします。
3. **Edit**をクリックし、Braze REST APIエンドポイント、REST APIキー、およびBrazeアプリ識別子を入力します。
4. イベント送信フィルターを使用して、送信するイベントを選択します。すべてのイベントを送信することもできますが、Amplitudeでは最も重要なイベントを選択することを推奨しています。
5. 完了したら、送信先を有効にして保存します。

この統合の詳細については、[Brazeイベントストリーミング](https://www.docs.developers.amplitude.com/data/destinations/braze/)を参照してください。

## ユーザー特性と計算を同期する {#sync-user-traits-and-computations}

Audiencesを使用して、ユーザープロパティと計算をカスタム属性としてBrazeに送信します。過去90日間にアクティブであったユーザーのユーザープロパティまたは計算プロパティを同期できます。

ユーザーのプロパティや計算が更新されると、Amplitudeはそのユーザープロパティや計算と同じ名前のカスタム属性をBrazeで更新します。

ユーザー特性と計算の同期により、Braze内にまだ存在しないユーザー識別子に対して新しいユーザーが作成されます。計算とユーザー特性は、ユーザー識別子を使用してのみ同期できます。ユーザー識別子は、次のいずれかになります。
- External ID
- Braze ID
- ユーザーエイリアス
- メールアドレス

[プロパティ、レコメンデーション、コホートをサードパーティの送信先に同期する](https://help.amplitude.com/hc/en-us/articles/360060055531)方法の詳細については、Amplitudeのドキュメントを参照してください。

### ユーザープロパティと計算を同期する方法 {#how-to-sync-user-properties-and-computations}

Amplitude Audiencesで、**Syncs** > **Create Sync**を選択します。

![Amplitude AudiencesのSyncsページでCreate Syncが選択されている画面。]({% image_buster /assets/img/amplitude11.png %})

次に、ユーザープロパティ、計算、コホート、またはレコメンデーションの同期を選択します。

{% tabs %}
{% tab ユーザープロパティの同期 %}

**User Property**を選択し、同期するユーザープロパティを選択します。

![同期するユーザープロパティを選択するAmplitude同期設定ステップ。]({% image_buster /assets/img/amplitude7.png %})

次に、ユーザープロパティの同期先を選択します。

![プロパティをBrazeに同期するためのAmplitude送信先セレクター。]({% image_buster /assets/img/amplitude8.png %})

最後に、同期の頻度を定義します。

![ケイデンスを1回限りの同期かスケジュールされた同期かを定義します。]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% tab 計算の同期 %}

**Computation**を選択し、同期する計算を選択します。

![同期する計算を選択するAmplitude同期設定ステップ。]({% image_buster /assets/img/amplitude10.png %})

次に、計算の同期先を選択します。

![計算をBrazeに同期するためのAmplitude送信先セレクター。]({% image_buster /assets/img/amplitude8.png %})

最後に、同期の頻度を定義します。

![ケイデンスを1回限りの同期かスケジュールされた同期かを定義します。]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% endtabs %}

## トラブルシューティング {#troubleshooting}

### コホート同期時に「We do not have enough data yet for this filter」と表示される {#we-do-not-have-enough-data-yet-for-this-filter-when-syncing-a-cohort}

[Amplitudeコホートをインポート]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import)する際にこのエラーが発生した場合は、以下を試してください。

1. **ユーザーIDの一致を確認します。** AmplitudeのユーザーID（Amplitude IDではなく）が、BrazeのExternal User ID（BrazeまたはBSON IDではなく）と正確に一致している必要があります。たとえば、AmplitudeのユーザーID `12345` は、BrazeのExternal User ID `12345` と一致する必要があります。
2. **Braze APIキーを再生成します。** Brazeダッシュボードで、**パートナー連携** > **テクノロジーパートナー** > **Amplitude**に移動し、**Generate New Key**を選択します。その後、新しいAPIキーを使用してAmplitudeコホートの同期を再試行してください。
3. **Amplitudeでコホートが同期されたことを確認します。** Brazeでさらにトラブルシューティングを行う前に、[Amplitudeサポート](https://help.amplitude.com/)に連絡して、Amplitude側でコホートが正常に同期されたことを確認してください。

## AmplitudeユーザープロファイルAPIエンドポイント {#amplitude-user-profile-api-endpoints}

Connected Contentで使用できる一般的なAmplitude APIエンドポイントを確認するには、専用の[Amplitude APIドキュメント]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_user_profile_api)を参照してください。