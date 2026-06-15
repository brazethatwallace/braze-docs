---
nav_title: Mixpanel
article_title: Mixpanel
alias: /partners/mixpanel/
description: "このリファレンス記事では、BrazeとMixpanelのパートナーシップについて説明します。Mixpanelはビジネス分析プラットフォームであり、MixpanelコホートをBrazeにインポートしてBraze セグメントを作成できます。作成したセグメントは、今後のBraze キャンペーンやキャンバスでユーザーをターゲットにするために使用できます。"
page_type: partner
search_tag: Partner
tool: Currents

---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2){: style="float:right;width:120px;border:0;" class="noimgborder"}Mixpanel {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecommixpanel-integration-with-braze339085scorm2u7y2e6qrldh2-stylefloatrightwidth120pxborder0-classnoimgbordermixpanel}

> [Mixpanel](https://mixpanel.com/)はビジネス分析プラットフォームであり、Mixpanelから他のプラットフォームにイベントをエクスポートして、より深い分析を実行できます。収集されたデータは、カスタムレポートの作成やユーザーエンゲージメントとリテンションの測定に使用できます。

BrazeとMixpanelの統合により、[MixpanelコホートをBrazeにインポートして]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/mixpanel_cohort_import/)Braze セグメントを作成できます。このセグメントは、今後のBraze キャンペーンやキャンバスでユーザーをターゲットにするために使用できます。コホート同期はBrazeのコホートメンバーシップを更新しますが、Mixpanelのイベントやユーザープロパティをインポートするものではありません。詳細については、[Mixpanelコホートインポート]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/mixpanel_cohort_import/#data-import-integration)を参照してください。

Braze Currentsを利用して[BrazeイベントをMixpanelにエクスポート](#data-export-integration)し、コンバージョン、リテンション、製品使用率に関する詳細な分析を促進することもできます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Mixpanelアカウント | このパートナーシップを活用するには、[Mixpanelアカウント](https://mixpanel.com/)が必要です。 |
| Currents | Mixpanelにデータをエクスポートするには、アカウントに[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## データエクスポートの統合 {#data-export-integration}

BrazeからMixpanelにエクスポートできるすべてのイベントを以下に示します。Mixpanelに送信されるすべてのイベントには、ユーザーの`external_user_id`がMixpanel Distinct IDとして含まれます。現時点では、Brazeは`external_user_id`を設定していないユーザーのイベントデータを送信しません。

Mixpanelにエクスポートできるイベントは2種類あります。[メッセージエンゲージメントイベント](#supported-currents-events)（メッセージ送信に直接関連するBrazeイベントで構成される）と、[顧客行動イベント](#supported-currents-events)（セッション、カスタムイベント、プラットフォーム経由で追跡された購入などのその他のアプリまたはWebサイトアクティビティを含む）です。すべてのカスタムイベントには、接頭辞として`[Braze Custom Event]`が付いています。カスタムイベントプロパティの接頭辞は`[Custom event property]`、購入イベントプロパティの接頭辞は`[Purchase property]`です。

その他のイベントの種類にアクセスする必要がある場合は、アカウントマネージャーに問い合わせるか、[サポートチケット]({{site.baseurl}}/braze_support/)を開いてください。

### ステップ1: Mixpanel認証情報を取得する {#step-1-get-mixpanel-credentials}

Mixpanelダッシュボードで、新規または既存のプロジェクトの**Project Settings**をクリックします。ここにMixpanel APIシークレットとMixpanelトークンがあります。これらの認証情報は、次のステップでCurrents接続を作成するために使用します。

### ステップ2: Braze Currentを作成する {#step-2-create-braze-current}

1. Brazeで**Currents** > **+ Create Current** > **Create Mixpanel Export**に移動します。
2. 表示されているフィールドに、統合名、連絡先メール、Mixpanel APIシークレット、Mixpanelトークンを入力します。
3. 追跡したいイベントを選択します。利用可能なイベントのリストが提供されます。
4. **Launch Current**を選択します。

![Braze Mixpanel Currentsページ。このページには、統合名、連絡先メール、APIシークレット、およびMixpanelエクスポートトークンのフィールドが含まれます。Currentsページの下半分には、送信可能なCurrentsイベントがリストされています。]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab note %}
詳細については、Mixpanelの[統合に関するドキュメント](https://help.mixpanel.com/hc/en-us/articles/360001243663)を参照してください。
{% endtab %}

## サポートされているCurrentsイベント {#supported-currents-events}

Brazeでは、以下のイベントをMixpanelにエクスポートできます。

- [メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)
- [顧客行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)

各イベントのペイロード構造については、[メッセージエンゲージメントイベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)および[顧客行動イベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)の**Mixpanel**タブを選択してください。

## トラブルシューティング {#troubleshooting}

### Mixpanel APIキーとBraze external IDを確認する {#verify-mixpanel-api-key-and-braze-external-id}

Mixpanel APIキーと`braze_external_id`の値が、BrazeとMixpanelの両方で期待どおりであることを確認してください。コホート同期APIは製品間でユーザーグループを共有しますが、Brazeの`external_id`とMixpanelが送信する識別子が一致しない場合、同期は正しく動作しません。Mixpanelからのコホート同期はMixpanelのスケジュール（例: 1回または約2時間ごと）で実行されるため、確認の間に時間を置いてください。

### 実装ステータスを確認する {#check-implementation-status}

Mixpanelで`braze_external_id`が実装されていることを確認してください。

### ユーザープロパティを直接設定する {#set-the-user-property-directly}

あいまいさを減らすために、Mixpanelで`braze_external_id`を直接設定してください。

### 自動プロパティ設定（SDK） {#automatic-property-setting-sdks}

Mixpanel SDKは、同じアプリケーションにBraze SDKが統合されている場合、`braze_external_id`を自動的に設定できます。MixpanelとBrazeの両方を一緒に実装する場合、通常は両方のSDKをインストールする以外に追加の設定は必要ありません。

{% alert note %}
`braze_external_id`はBrazeで`changeUser()`が呼び出されたときに設定されるのではなく、Mixpanelが初期化されるかセッションを開始するとき（「init」または「start session」時）に設定されます。
{% endalert %}