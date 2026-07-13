---
nav_title: Amplitude
article_title: Amplitude コホートインポート
description: "このリファレンス記事では、プロダクト分析およびビジネスインテリジェンスプラットフォームである Amplitude のコホートインポート機能について説明します。"
page_type: partner
search_tag: Partner
---

# Amplitude コホートインポート {#amplitude-cohort-import}

> この記事では、[Amplitude](https://amplitude.com/) から Braze にユーザーコホートをインポートする方法について説明します。Amplitudeの統合やその他の機能の詳細については、[Amplitudeのメイン記事]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences)を参照してください。

## データインポート統合 {#data-import-integration}

設定するすべての統合は、アカウントのデータポイントボリュームにカウントされます。

### ステップ1:Braze データインポートキーを取得する {#step-1-get-the-braze-data-import-key}

Brazeで、**パートナー連携** > **テクノロジーパートナー**に移動し、**Amplitude** を選択します。ここでRESTエンドポイントを確認し、Brazeデータインポートキーを生成できます。

生成後、新しいキーを作成するか、既存のキーを無効にできます。データインポートキーとRESTエンドポイントは、次のステップでAmplitudeのダッシュボードにポストバックを設定する際に使用します。<br><br>![Brazeの Amplitude テクノロジーパートナーページ。データインポートキーとエンドポイントが表示されています。]({% image_buster /assets/img/amplitude3.png %})

### ステップ2:Amplitude で Braze 統合を設定する {#step-2-set-up-the-braze-integration-in-amplitude}

Amplitudeで、**Sources & Destinations** > **[プロジェクト名]** > **Destinations** > **Braze** に移動します。表示されるプロンプトでBrazeデータインポートキーとRESTエンドポイントを入力し、**Save** をクリックします。

![Brazeコホート同期用のAmplitude送信先設定。認証情報が入力されています。]({% image_buster /assets/img/amplitude.png %})

### ステップ3:Amplitude コホートを Braze にエクスポートする {#step-3-export-an-amplitude-cohort-to-braze}

まず、AmplitudeからBrazeにユーザーをエクスポートするために、エクスポートしたいユーザーの[コホート](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts)を作成します。次に、識別済みユーザーと匿名ユーザーの両方を取得するために、以下の識別子マッピングプロパティを使用して、そのコホートに対して2つの同期を設定します。
- ユーザー ID（External ID）
- デバイス ID

Amplitudeアカウントで複数のBraze接続を設定できます。これにより、既知のユーザーにはユーザーIDを同期する接続を、匿名ユーザーにはデバイスIDを同期する接続を、それぞれ構成できます。

コホートを作成したら、**Sync to...** をクリックして、これらのユーザーをBrazeにエクスポートします。

{% alert important %}
Braze内に既に存在するユーザーのみがコホートに追加または削除されます。コホートインポートではBrazeに新しいユーザーは作成されません。
{% endalert %}

#### 同期頻度の定義 {#defining-sync-cadence}

コホート同期は、1回限りの同期、毎日または毎時間のスケジュール同期、あるいは1分ごとに更新されるリアルタイム同期として設定できます。

設定したすべての統合はデータポイントを記録します。Brazeデータポイントの詳細について質問がある場合は、Brazeアカウントマネージャーにお問い合わせください。

### ステップ4:Braze でユーザーをセグメント化する {#step-4-segment-users-in-braze}

Brazeでこれらのユーザーのセグメントを作成するには、**エンゲージメント**の下の**セグメント**に移動し、セグメントに名前を付け、フィルターとして**Amplitude Cohorts**を選択します。次に、「次を含む」オプションを使用し、Amplitudeで作成したコホートを選択します。

![Brazeセグメントビルダーで、フィルター「amplitude_cohorts」が「includes_value」および「Amplitude cohort test」に設定されています。]({% image_buster /assets/img/amplitude2.png %})

保存後、キャンバスやキャンペーン作成時のユーザーターゲティングステップでこのセグメントを参照できます。

## ユーザーマッチング {#user-matching}

識別済みユーザーは、`external_id` または `alias` のいずれかで照合できます。匿名ユーザーは `device_id` で照合できます。元々匿名ユーザーとして作成された識別済みユーザーは `device_id` では識別できず、`external_id` または `alias` で識別する必要があります。