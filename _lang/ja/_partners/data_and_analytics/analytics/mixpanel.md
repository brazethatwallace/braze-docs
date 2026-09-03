---
nav_title: Mixpanel
article_title: Mixpanel
alias: /partners/mixpanel/
description: "このリファレンス記事では、BrazeとMixpanelのパートナーシップについて説明します。Mixpanelはビジネス分析プラットフォームであり、MixpanelコホートをBrazeにインポートしてBrazeセグメントを作成できます。作成したセグメントは、今後のBrazeキャンペーンやキャンバスでユーザーをターゲットにするために使用できます。"
page_type: partner
search_tag: Partner
tool: Currents

---

# [![Braze Learningコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2){: style="float:right;width:120px;border:0;" class="noimgborder"}Mixpanel {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecommixpanel-integration-with-braze339085scorm2u7y2e6qrldh2-stylefloatrightwidth120pxborder0-classnoimgbordermixpanel}

> [Mixpanel](https://mixpanel.com/)はビジネス分析プラットフォームであり、Mixpanelから他のプラットフォームにイベントをエクスポートして、より深い分析を実行できます。収集されたデータは、カスタムレポートの作成やユーザーエンゲージメントとリテンションの測定に使用できます。

BrazeとMixpanelの統合により、[MixpanelコホートをBrazeにインポートして]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/mixpanel_cohort_import)Brazeセグメントを作成できます。このセグメントは、今後のBrazeキャンペーンやキャンバスでユーザーをターゲットにするために使用できます。コホート同期はBrazeのコホートメンバーシップを更新しますが、Mixpanelのイベントやユーザープロパティをインポートするものではありません。詳細については、[Mixpanelコホートインポート]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/mixpanel_cohort_import#data-import-integration)を参照してください。

Braze Currentsを利用して[BrazeイベントをMixpanelにエクスポート](#data-export-integration)し、コンバージョン、リテンション、製品使用率に関する詳細な分析を促進することもできます。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| Mixpanel アカウント | このパートナーシップを利用するには、[Mixpanel アカウント](https://mixpanel.com/)が必要です。 |
| Currents | Mixpanel にデータをエクスポートするには、アカウントに [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## データエクスポート統合 {#data-export-integration}

BrazeからMixpanelにエクスポートできるイベントの完全なリストは、このセクションに記載されています。Mixpanelに送信されるすべてのイベントには、ユーザーの`external_user_id`がMixpanel Distinct IDとして含まれます。現時点では、Brazeは`external_user_id`が設定されていないユーザーのイベントデータは送信しません。

Mixpanelには2種類のイベントをエクスポートできます。メッセージ送信に直接関連するBrazeイベントで構成される[メッセージエンゲージメントイベント](#supported-currents-events)と、セッション、カスタムイベント、プラットフォームを通じてトラッキングされた購入などのその他のアプリやWebサイトのアクティビティを含む[顧客行動イベント](#supported-currents-events)です。すべてのカスタムイベントには`[Braze Custom Event]`というプレフィックスが付きます。カスタムイベントプロパティと購入イベントプロパティには、それぞれ`[Custom event property]`と`[Purchase property]`というプレフィックスが付きます。

追加のイベントエンタイトルメントへのアクセスが必要な場合は、アカウントマネージャーに連絡するか、[サポートチケット]({{site.baseurl}}/braze_support)を開いてください。

### ステップ1:Mixpanelの認証情報を取得する {#step-1-get-mixpanel-credentials}

Mixpanelのダッシュボードで、新規または既存のプロジェクトの**Project Settings**をクリックします。ここでMixpanel APIシークレットとMixpanelトークンを確認できます。これらの認証情報は、次のステップでCurrents接続を作成する際に使用します。

### ステップ2:Braze Currentを作成する {#step-2-create-braze-current}

1. Brazeで**Currents** > **+ Create Current** > **Create Mixpanel Export**に移動します。
2. 表示されたフィールドに統合名、連絡先メールアドレス、Mixpanel APIシークレット、Mixpanelトークンを入力します。
3. トラッキングするイベントを選択します。利用可能なイベントのリストが提供されます。
4. **Launch Current**を選択します。

![Braze Mixpanel Currentsページ。このページには、統合名、連絡先メールアドレス、APIシークレット、Mixpanelエクスポートトークンのフィールドがあります。Currentsページの下半分には、送信可能なCurrentsイベントのリストが表示されます。]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab note %}
詳しくはMixpanelの[統合ドキュメント](https://help.mixpanel.com/hc/en-us/articles/360001243663)をご覧ください。
{% endtab %}

## サポートされているCurrentsイベント {#supported-currents-events}

Brazeは以下のイベントをMixpanelにエクスポートすることをサポートしています。

- [メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)
- [顧客行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)

各イベントのペイロード構造については、[メッセージエンゲージメントイベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)および[顧客行動イベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)の**Mixpanel**タブを選択してください。

## トラブルシューティング {#troubleshooting}

### Mixpanel APIキーとBraze external IDの確認 {#verify-mixpanel-api-key-and-braze-external-id}

Mixpanel APIキーと`braze_external_id`の値が、BrazeとMixpanelの両方で想定どおりに一致していることを確認してください。コホート同期APIはプロダクト間でユーザーグループを共有するため、Brazeの`external_id`とMixpanelが送信する識別子が一致していない場合、同期が正しく動作しません。Mixpanelからのコホート同期はMixpanelのスケジュールに基づいて実行されます（例：1回、またはおよそ2時間ごと）。そのため、確認の間に時間を置いてください。

### 実装ステータスの確認 {#check-implementation-status}

`braze_external_id`がMixpanelに実装されていることを確認してください。

### ユーザープロパティを直接設定する {#set-the-user-property-directly}

あいまいさを減らすため、Mixpanelで`braze_external_id`を直接設定してください。

### プロパティの自動設定（SDK） {#automatic-property-setting-sdks}

Mixpanel SDKは、同じアプリケーションにBraze SDKが統合されている場合、`braze_external_id`を自動的に設定できます。MixpanelとBrazeの両方を一緒に実装する場合、通常は両方のSDKをインストールする以外に追加の設定は必要ありません。

{% alert note %}
`braze_external_id`は、Brazeで`changeUser()`が呼び出されたときには設定されません。Mixpanelが初期化されるか、セッションを開始するとき（「init」または「start session」時）に設定されます。
{% endalert %}