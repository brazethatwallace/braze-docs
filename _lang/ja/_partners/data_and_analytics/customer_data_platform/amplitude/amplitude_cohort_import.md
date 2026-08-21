---
nav_title: Amplitude
article_title: Amplitude コホートインポート
description: "このリファレンス記事では、プロダクト分析およびビジネスインテリジェンスプラットフォームである Amplitude のコホートインポート機能について説明します。"
page_type: partner
search_tag: Partner
---

# Amplitude コホートインポート {#amplitude-cohort-import}

> この記事では、[Amplitude](https://amplitude.com/) から Braze にユーザーコホートをインポートする方法について説明します。Amplitudeの統合やその他の機能の詳細については、[Amplitudeのメイン記事]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences)を参照してください。

## データインポート連携 {#data-import-integration}

設定した連携は、アカウントのデータポイント消費量にカウントされます。

### ステップ1:Brazeデータインポートキーを取得する {#step-1-get-the-braze-data-import-key}

Brazeで、**パートナー連携** > **テクノロジーパートナー**に移動し、**Amplitude**を選択します。ここで、RESTエンドポイントを確認し、Brazeデータインポートキーを生成できます。

生成後、新しいキーを作成したり、既存のキーを無効化したりできます。データインポートキーとRESTエンドポイントは、次のステップでAmplitudeのダッシュボードでポストバックを設定する際に使用します。<br><br>![データインポートキーとエンドポイントが表示されたBraze Amplitudeテクノロジーパートナーページ。]({% image_buster /assets/img/amplitude3.png %})

### ステップ2:AmplitudeでBraze連携を設定する {#step-2-set-up-the-braze-integration-in-amplitude}

Amplitudeで、**Sources & Destinations** > **[プロジェクト名]** > **Destinations** > **Braze**に移動します。表示されるプロンプトで、Brazeデータインポートキーとエンドポイントを入力し、**Save**をクリックします。

![認証情報が入力されたBrazeコホート同期用のAmplitude送信先設定。]({% image_buster /assets/img/amplitude.png %})

### ステップ3:AmplitudeコホートをBrazeにエクスポートする {#step-3-export-an-amplitude-cohort-to-braze}

まず、AmplitudeからBrazeにユーザーをエクスポートするには、エクスポートしたいユーザーの[コホート](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts)を作成します。次に、識別済みユーザーと匿名ユーザーの両方をキャプチャするために、以下の識別子マッピングプロパティを使用してそのコホートに2つの同期を設定します：
- ユーザー ID（External ID）
- デバイス ID

Amplitudeアカウントで複数のBraze接続を設定できます。これにより、既知のユーザーに対してはユーザー IDを同期する接続を設定し、匿名ユーザーに対してはデバイス IDを同期する別の接続を設定できます。

コホートを作成したら、**Sync to...**をクリックして、これらのユーザーをBrazeにエクスポートします。

{% alert important %}
Braze内にすでに存在するユーザーのみがコホートに追加または削除されます。コホートインポートでは、Brazeに新しいユーザーは作成されません。
{% endalert %}

#### 同期頻度の定義 {#defining-sync-cadence}

コホート同期は、ワンタイム同期、毎日または毎時のスケジュール、さらには毎分更新されるリアルタイム同期に設定できます。

設定した連携はデータポイントを記録します。Brazeデータポイントの詳細についてご質問がある場合は、Brazeアカウントマネージャーにお問い合わせください。

### ステップ4:Brazeでユーザーをセグメントする {#step-4-segment-users-in-braze}

Brazeでこれらのユーザーのセグメントを作成するには、**エンゲージメント**の下にある**セグメント**に移動し、セグメントに名前を付け、フィルターとして**Amplitude Cohorts**を選択します。次に、「includes」オプションを使用して、Amplitudeで作成したコホートを選択します。

![Brazeセグメントビルダーで、フィルター「amplitude_cohorts」が「includes_value」と「Amplitude cohort test」に設定されている。]({% image_buster /assets/img/amplitude2.png %})

保存後、ターゲットユーザーステップでキャンバスまたはキャンペーン作成時にこのセグメントを参照できます。

## ユーザーマッチング {#user-matching}

識別済みユーザーは、`external_id` または `alias` のいずれかでマッチングできます。匿名ユーザーは `device_id` でマッチングできます。もともと匿名ユーザーとして作成された識別済みユーザーは、`device_id` では識別できないため、`external_id` または `alias` で識別する必要があります。

## FAQ

### Amplitudeコホートの一覧を取得できますか？ {#can-i-pull-a-list-of-amplitude-cohorts}

Brazeでは、すべてのAmplitudeコホート定義のカタログをエクスポートするAPIは提供していません。コホートは以下の場所で表示・使用できます。

1. **Amplitude内：**Amplitudeダッシュボードでコホートを表示・管理してから、Brazeに同期します。
2. **Braze内：**コホートが同期された後、**Amplitude Cohorts**セグメントフィルターを使用してユーザーをターゲットにします。このフィルターには、Amplitudeから送信された名前で同期済みコホートが一覧表示されます。

コホート同期エラーについては、まずAmplitudeでユーザーIDの整合性とAPIキーを確認してください。[コホートを同期する際に「このフィルターに対して十分なデータがまだありません」と表示される場合]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences#we-do-not-have-enough-data-yet-for-this-filter-when-syncing-a-cohort)を参照してください。