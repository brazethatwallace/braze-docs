---
nav_title: VWO
article_title: VWOとBrazeの統合
description: "VWOとBrazeを統合する方法について説明します。"
alias: /partners/vwo/
page_type: partner
search_tag: Partner
---

# VWO

> [VWO](https://vwo.com/) は、顧客行動データに裏打ちされたコンバージョン最適化プログラムをチームが実行できるようにすることで、ブランドが主要なビジネス指標を強化するのを支援する強力な実験プラットフォームです。VWOを使えば、顧客データの一元化、行動インサイトの獲得、仮説の構築、複数プラットフォーム（サーバー、Web、モバイル）でのA/Bテストの実行、機能の展開、エクスペリエンスのパーソナライズ、カスタマージャーニー全体の最適化が可能になります。

VWOとBrazeを統合することで、VWOの実験データを活用してターゲットセグメントを作成し、パーソナライズされたキャンペーンを配信できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|-----------------|-------------|
| VWOアカウント | 実験データにアクセスできるVWOアカウントが必要です。 |
| Brazeアカウント | Webページに[Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)が統合されたアクティブなBrazeアカウントが必要です。また、イベントプロパティのセグメンテーションを有効にする必要があります。リクエストするには、[考慮事項](#request-event-property-segmentation)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## VWOとBrazeの統合 {#integrating-vwo-with-braze}

### ステップ1:VWOでBraze統合を有効にする {#step-1-enable-the-braze-integration-in-vwo}

1. VWOアカウントにログインします。
2. VWOダッシュボードで、**Configurations** > **Integrations** に移動します。ここでは、ワークスペースレベルで統合を有効にできます。これにより、統合はデフォルトで今後のすべてのテストキャンペーンに適用されます。

   ![VWO統合設定]({% image_buster /assets/img/vwo/vwo1_settings.png %})

4. Braze統合を選択して有効にします。
5. 必要に応じて、既存のあらゆるキャンペーンに対してBraze統合を有効にできます。そのためには、キャンペーンを選択し、**Configuration** > **Integrations** に移動して、Brazeを有効にします。

   ![Braze統合を有効にする]({% image_buster /assets/img/vwo/vwo2_enable_braze.png %})

6. 統合を有効にすると、VWOはキャンペーンレベルでBrazeへの実験データの送信を開始します。

### ステップ2:VWOイベントプロパティを使用してBrazeでセグメントを作成する {#step-2-create-a-segment-in-braze-with-vwo-event-properties}

1. Brazeダッシュボードで、**セグメント** > **+ Create セグメント** を選択します。
3. **Create セグメント** ウィンドウで、セグメントの名前を入力し、**Create セグメント** を選択します。
4. 新しく作成したセグメントで、**Filters** > **Add Filter** を選択し、フィルタータイプとして **Custom Event** を選択します。
6. フィルターのドロップダウンで、**VWO** を検索します。
7. 関連するVWOプロパティを選択し、必要な値を指定します。
8. 必要であれば、訪問回数と時間枠を設定します。完了したら、**Save** を選択します。

   ![Brazeでのセグメント作成]({% image_buster /assets/img/vwo/vwo3_braze_segment.png %})

9. セグメント条件に一致するユーザー数を表示するには、**Calculate Exact Statistics** を選択します。

   ![Brazeのセグメント統計]({% image_buster /assets/img/vwo/vwo4_braze_segment_calculate_size.png %})

## データフロー {#data-flow}

VWOは、キャンペーン実験データを以下のフォーマットでカスタムイベントとしてBrazeに送信します。

- **イベント名:** VWO
- **イベントプロパティ:** `vwo_campaign_name`、`vwo_variation_name`

{% alert tip %}
これらのカスタムイベントプロパティは、セグメンテーションおよびターゲティングにも使用できます。
{% endalert %}

## 考慮事項 {#considerations}

### イベントプロパティセグメンテーションのリクエスト {#request-event-property-segmentation}

イベントプロパティセグメンテーションを使用するには、事前にBrazeで有効にしておく必要があります。次のテンプレートを使用して、Brazeカスタマーサクセスマネージャーまたはサポートチームに問い合わせてください。

   <table aria-label="Request event property segmentation">
     <caption>Request event property segmentation</caption>
   <thead>
      <tr>
         <th>フィールド</th>
         <th>詳細</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><strong>件名</strong></td>
         <td>Request to Enable Event Property セグメントation for VWO Integration</td>
      </tr>
      <tr>
         <td><strong>本文</strong></td>
         <td>
         Hello Braze Team,<br><br>
         We would like to enable event property segmentation for events sent from our VWO&lt;&gt;Braze integration. Here are the details:<br><br>
         - <strong>Event Name:</strong> VWO<br>
         - <strong>Event Properties:</strong> <code>vwo_campaign_name</code>, <code>vwo_variation_name</code><br><br>
         Please confirm once the properties have been enabled in our account.<br><br>
         Thank you.
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 aria-label="Request event property segmentation" }

### Brazeデータポイント {#braze-data-points}

VWOからBrazeに送信されるカスタムイベント（セグメンテーションで有効になっているすべてのイベントプロパティを含む）は、Brazeインスタンスのデータポイントを記録します。

### 制限事項

現在、この統合はテストデータのリアルタイム同期をサポートしていません。テストデータがBrazeに表示されるまで、最大15分ほど遅れる場合があります。

## トラブルシューティング {#troubleshooting}

BrazeでVWOのデータが表示されない場合:

1. テストキャンペーンが実行されているページを右クリックし、**Inspect Element** を選択します。
2. **Network** タブで、**Braze** を検索し、Brazeのネットワークコールをフィルタリングします。
3. ネットワークコールはページの読み込み時に入力されます。ネットワークコールを表示するにはページをリロードしてください。
4. ネットワークコールを選択すると、詳細が表示されます。
5. **Payload** タブの **Request Payload** セクションに移動し、events: の中にname: **ce** というカスタムイベントを示すイベントを見つけます。
6. 0: および data: を展開すると、n: "VWO"（カスタムイベントの名前）と p: {vwo_campaign_name: "<your vwo campaign name>", vwo_variation_name: "<variation name>"} が表示されます。これらは、値がVWOからBrazeにプッシュされていることを示しています。

 ![Brazeのトラブルシューティング]({% image_buster /assets/img/vwo/vwo5_troubleshooting.png %})

その他のサポートについては、VWOカスタマーサクセスマネージャーにお問い合わせください。