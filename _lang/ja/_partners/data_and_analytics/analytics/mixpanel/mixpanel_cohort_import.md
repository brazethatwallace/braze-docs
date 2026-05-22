---
nav_title: Mixpanel
article_title: Mixpanel コホートインポート
description: "このリファレンス記事では、ビジネス分析プラットフォームであるMixpanelのコホートインポート機能について説明します。MixpanelコホートをBrazeにインポートしてBraze セグメントを作成し、今後のBraze キャンペーンやキャンバスでユーザーをターゲットにすることができます。"
page_type: partner
search_tag: Partner
---

# Mixpanel コホートインポート {#mixpanel-cohort-import}

> この記事では、[Mixpanel](https://mixpanel.com/) からBrazeにユーザーコホートをインポートする方法について説明します。Mixpanelとその他の機能の統合についての詳細は、[Mixpanelのメイン記事]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/)を参照してください。

## データインポート統合 {#data-import-integration}

MixpanelからBrazeにコホートを同期すると、Brazeは既存のBrazeプロファイルにMixpanelがマッチできるユーザーのコホートメンバーシップ更新を受信します。同期後、**Mixpanel cohorts** セグメントフィルターを使用してそれらのユーザーをターゲットにできます。

コホート同期では、Mixpanelイベント、Mixpanelユーザープロパティ、またはカスタム属性はBrazeにインポートされません。同期頻度を含むコネクターの動作はMixpanelで制御されます。セットアップの詳細については、[MixpanelのBrazeコホート同期ドキュメント](https://docs.mixpanel.com/docs/cohort-sync/integrations/braze)を参照してください。ユーザーマッチングの要件については、[ユーザーマッチング](#user-matching)を参照してください。

設定した統合はデータポイントを記録します。Brazeデータポイントの詳細について質問がある場合は、Brazeアカウントマネージャーにお問い合わせください。

{% alert important %}
Mixpanelのデータリテンションポリシーに従い、2010年1月1日より前に送信されたイベントはインポート中に削除されます。
{% endalert %}

### ステップ 1: Brazeデータインポートキーを取得する {#step-1-get-the-braze-data-import-key}

Brazeで**パートナー連携** > **テクノロジーパートナー**に移動し、**Mixpanel**を選択します。ここでRESTエンドポイントを確認し、Brazeデータインポートキーを生成できます。

生成後、新しいキーを作成するか、既存のキーを無効にできます。データインポートキーとRESTエンドポイントは、次のステップでMixpanelのダッシュボードでポストバックを設定する際に使用します。<br><br>![]({% image_buster /assets/img_archive/currents-mixpanel-edit.png %})

### ステップ 2: MixpanelでBrazeとの統合をセットアップする {#step-2-set-up-the-braze-integration-in-mixpanel}

1. Mixpanelで**Data Management > Integrations**に移動します。
2. Braze統合のタブを選択し、**Connect**を選択します。
3. 表示されるプロンプトで、BrazeデータインポートキーとRESTエンドポイントを入力します。
4. **Continue**を選択します。

![]({% image_buster /assets/img_archive/mixpanel2.png %}){: style="max-width:50%;"}

### ステップ 3: MixpanelコホートをBrazeにエクスポートする {#step-3-export-a-mixpanel-cohort-to-braze}

Mixpanelで**Data Management > Cohorts**に移動します。Brazeに送信するコホートを選択し、**Export to Braze**を選択します。最後に、ワンタイムシンクまたはダイナミックシンクを選択します。ダイナミックシンクを選択すると、Mixpanelが管理する定期スケジュールでコホートが更新されます。最新の同期頻度については、[MixpanelのBrazeコホート同期ドキュメント](https://docs.mixpanel.com/docs/cohort-sync/integrations/braze)を参照してください。

![]({% image_buster /assets/img_archive/mixpanel3.png %}){: style="max-width:50%;"}

{% alert important %}
Braze内に既に存在するユーザーのみがコホートに追加または削除されます。コホートインポートではBrazeに新しいユーザーは作成されません。
{% endalert %}

### ステップ 4: Brazeでユーザーをセグメントする {#step-4-segment-users-in-braze}

Brazeでこれらのユーザーのセグメントを作成するには、**Audience** > **セグメント**に移動し、セグメントに名前を付け、フィルターとして**Mixpanel_Cohorts**を選択します。次に「includes」オプションを使用し、Mixpanelで作成したコホートを選択します。

![Brazeのセグメントビルダーで、ユーザー属性フィルター「Mixpanel cohorts」が「includes」と「Braze cohort」に設定されています。]({% image_buster /assets/img_archive/mixpanel1.png %})

保存後、キャンバスやキャンペーン作成時のユーザーターゲティングステップでこのセグメントを参照できます。

## ユーザーマッチング {#user-matching}

識別されたユーザーは、`external_id`または`alias`のどちらかで照合できます。匿名ユーザーは`device_id`で照合できます。元々匿名ユーザーとして作成された識別済みユーザーは`device_id`では識別できず、`external_id`または`alias`で識別する必要があります。

## トラブルシューティング {#troubleshooting}

Mixpanelコホートの同期が不完全に見える場合や、特定のユーザーに対して更新されない場合は、Mixpanelのメイン記事の[トラブルシューティング]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/#troubleshooting)を参照してください。

コネクター固有の手順と同期頻度については、[MixpanelのBrazeコホート同期ドキュメント](https://docs.mixpanel.com/docs/cohort-sync/integrations/braze)を参照してください。