---
nav_title: トラブルシューティング
article_title: Segmentsのトラブルシューティング
page_order: 9
page_type: reference
tool:
  - Segments
description: "このリファレンス記事では、Segmentsを使用する際のトラブルシューティング手順と考慮事項について説明します。"
---

# Segmentsのトラブルシューティング {#troubleshoot-segments}

> このページでは、BrazeでSegmentsを作成・管理する際に発生する可能性のある一般的な問題と質問について説明します。

## エラー {#errors}

### ターゲットオーディエンスが複雑すぎて起動できない {#target-audience-is-too-complex-to-launch}

このまれなエラーは、ターゲットオーディエンスに含まれる正規表現の値が多すぎる場合、正規表現の値が過度に長い場合、フィルターが過度に詳細な場合（「30,000件の郵便番号のいずれかに該当」など）、またはフィルターが多すぎる場合に発生します。これには、参照されたSegments内のフィルターや**ターゲットオーディエンス**ステップで追加されたフィルターなど、CampaignまたはCanvasオーディエンス内のすべてのフィルターが含まれます。

![複雑さのしきい値に達したターゲットオーディエンスのエラー。]({% image_buster /assets/img/segment/target_audience_too_complex_error.png %})

CampaignまたはCanvasにSegmentフィルターを追加すると、それらのフィルターはBraze内でクエリに変換されます（これらのクエリの文字数は、ダッシュボードユーザーが目にする文字数と1:1で対応するわけではありません）。BrazeがCampaignまたはCanvasを送信する際、ターゲットオーディエンス内のすべてのフィルターを組み合わせたクエリを実行します。ターゲットオーディエンスの結果クエリの文字数を制限するしきい値が適用されます。特定のCampaignまたはCanvasについて、参照されるすべてのSegmentsの文字数と、すべての追加フィルターの文字数が合計されます。特定のSegmentについては、すべてのフィルターとフィルター値の文字数が合計されます。

Campaign、Canvas、またはSegmentがしきい値を超えて起動できない場合、ダッシュボードにエラーが表示されます。このエラーが表示された場合は、再度起動する前にターゲットオーディエンスを簡素化してください。以下の対応が含まれます。

- オーディエンスが複数のSegmentsを参照している場合、同じフィルターが複数のSegmentsに含まれているなどの冗長性がないことを確認してください。
- Segmentフィルターで古いデータを参照していないことを確認してください。たとえば、Canvasが数か月前に停止されているにもかかわらず、過去1週間に特定のキャンバスステップを受信していないユーザーを検索するフィルターは古いフィルターです。
- ユーザーIDやメールアドレスのリストだけで構成されるSegments（多くの場合、正規表現フィルターを使用）は、[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/)に変換し、単一のCSVフィルターに簡素化できます。
- CDIを使用している場合は、データウェアハウスからグループを直接取得するCDI Segmentを作成できる場合があります。

フィルター最適化に関するさらなるサポートについては、[サポートに連絡]({{site.baseurl}}/braze_support/)することもできます。

{% alert note %}
文字数の制限は2025年4月から開始されました。2025年4月以前に起動されたCampaignsおよびCanvasesは免除されており、引き続き制限を超えることができますが、新しく作成されたCampaignsおよびCanvasesは制限を超えることができません。免除されたCampaignまたはCanvasを編集または複製した場合、オーディエンスが制限以下に更新されるまで起動**できません**。
{% endalert %}

### X件のアクティブまたは停止中のCampaignsまたはCanvasesがオーディエンス複雑さのしきい値を超えている {#x-active-or-stopped-campaigns-or-canvases-exceed-the-audience-complexity-threshold}

このバナーは、アクティブまたは停止中のCampaignsまたはCanvasesのオーディエンスがオーディエンス複雑さのしきい値を超えている場合に、CampaignまたはCanvasリストの上部に表示されます。バナーを選択すると、しきい値を超えているCampaignsまたはCanvasesのみにリストがフィルタリングされます。その後、[ターゲットオーディエンスが複雑すぎて起動できない](#target-audience-is-too-complex-to-launch)のトラブルシューティング手順に従ってください。

![4件のアクティブまたは停止中のCanvasesがオーディエンス複雑さのしきい値を超えていることを示すエラーバナー。]({% image_buster /assets/img/segment/audience_complexity_threshold_banner.png %})

### フィルターが10,000バイトを超えているか、長すぎて保存できない {#filter-exceeds-10000-bytes-or-is-too-long-to-save}

Brazeは個々のSegmentフィルターを最大10,000バイトに制限しています。これは英語の文字で10,000文字、日本語の文字で3,333文字に相当します。フィルターがSegment内にあるか、CampaignまたはCanvasに直接追加されているかにかかわらず、個々のフィルターが10,000バイトを超えると警告が表示されます。

![10,000文字を超える値を持つフィルターのエラーバナー。]({% image_buster /assets/img/segment/filter_error.png %})

![属性値が10,000文字を超えるカスタム属性フィルター `menu_item` のエラー。]({% image_buster /assets/img/segment/segment_filter_error.png %})

このエラーは非常にまれですが、発生する場合は通常、ユーザーIDやメールアドレスのリストをターゲットとする正規表現フィルターで発生します。その場合、以下の手順でフィルターをCSVに変換できます。

1. 影響を受けるSegmentまたは特定の正規表現フィルターからユーザーをエクスポートします。
2. 必要に応じてCSVをクリーンアップします。Braze IDまたはAppboy IDが必要ですが、不要な場合は他のすべての列を削除できます。また、データが最新であることを確認するためにレビューすることをお勧めします（たとえば、ターゲットにする必要がなくなったユーザーを削除します）。
3. CSVファイルを再度[インポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/)します。これにより、ユーザーが自動的に単一の高効率なCSVベースのフィルターにグループ化されます。

## ユーザーの動作 {#user-behavior}

### ユーザーがSegmentに含まれなくなった {#user-is-no-longer-in-a-segment}

Segmentの作成中にユーザーが利用できない場合、Segmentの適格性を決定するユーザーデータが、ユーザー自身のアクティビティや、以前にインタラクションした他のCampaignsやCanvasesの結果として変更された可能性があります。再適格性がオンになっている場合、ユーザープロファイルには受信したCampaignの最新データが表示されます。

### 特定のアプリでフィルタリングすると他のアプリのユーザー情報が表示される {#info-displays-for-users-of-other-apps-when-i-filter-for-a-specific-app}

ユーザーは複数のアプリを持つことができるため、セグメンテーションページの**使用アプリ**セクションで特定のアプリを選択すると、少なくともそのアプリを持つユーザーの結果が返されます。このフィルターは、そのアプリのみを持つユーザーの結果を返すわけではありません。

## フィルタリング {#filtering}

### フィルターオプションが変更された {#filter-options-changed}

フィルターオプションは、カスタム属性としてBrazeに渡されるデータの形式（データタイプ）に関連しています。Brazeがカスタム属性に対して認識しているデータタイプを確認するには、**データ設定** > **カスタム属性**に移動してください。

フィルターオプションが変更された場合、データが以前とは異なる形式（データタイプ）でBrazeに渡されていることを示しています。さまざまなデータタイプとそのフィルタリングオプションの詳細な説明については、[カスタム属性のデータタイプ]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#custom-attribute-data-types)を参照してください。

ダッシュボードでカスタム属性のデータタイプを変更すると、異なる形式でBrazeに送信されるデータは拒否されることに注意してください。

## 分析とレポート {#analytics-and-reporting}

### Campaign分析の*送信済みメッセージ*または*ユニーク受信者*がSegment数と一致しない {#message-sent-or-unique-recipients-in-campaign-analytics-doesnt-match-segment-count}

Campaign分析の*送信済みメッセージ*または*ユニーク受信者*の数が、Segmentフィルター`Has received message from campaign X`のユーザー数と一致しない場合、3つの理由が考えられます。

1. **Campaignの起動後にユーザーがアーカイブ、孤立、または削除された可能性がある**<br><br>たとえば、1,000人のユーザーがCampaignを受信し、同日にCSVエクスポートを行ったとします。1,000人のユーザーが報告されます。翌月、その1,000人のうち50人が削除されたとします（たとえば、`users/delete`エンドポイントによって）。別のCSVエクスポートを行うと、950人のユーザーが報告されますが、**Campaign分析**の*ユニーク受信者*数は依然として1,000のままです。<br><br>つまり、*ユニーク受信者*指標は累積カウントであり、セグメンターとCSVエクスポートは現在存在するユーザーのカウントを提供します。<br><br>

2. **Campaignに再適格性が設定されており、ユーザーが複数回Campaignに再エントリーできる**<br><br>たとえば、メールCampaignの再適格性がゼロ分に設定されている（ユーザーはオーディエンスSegmentの要件を満たす限りCampaignに再エントリーできる）とし、Campaignが1か月以上実行されているとします。**Campaign分析**の*送信済みメッセージ*数は、重複ユーザーへの送信メッセージが含まれるため、Segmentの数と一致しません。<br><br>これは、Brazeがユニークユーザーを*ユニークデイリー受信者*、つまり1日に特定のメッセージを受信したユーザー数としてカウントするためです。つまり、再適格ユーザーは「ユニーク」の時間枠が1日しか持続しないため、ユニーク受信者として複数回カウントされます。その結果、*ユニークデイリー受信者*の数がCSVエクスポートのユーザープロファイル数よりも多くなる場合があります。CSVファイルのユーザープロファイルは真にユニークです。<br><br>

3. **チャネル識別子を共有するユーザーがフィルターに一致した**<br><br>`Has received message from campaign X`フィルター（およびその他の「受信済み」フィルター）は、メッセージを受信、開封、またはクリックした人とチャネル識別子を共有するユーザーに一致する場合があります。

### ユーザーが1つのアプリでのみセッションを記録しているにもかかわらず2つのアプリに割り当てられている {#user-is-assigned-to-two-apps-despite-logging-a-session-in-only-one-app}

Segmentを作成する際、[特定のアプリを使用した]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#step-3-choose-your-app-or-platform)ユーザーをターゲットにできます。ユーザーが特定のアプリに割り当てられるには、そのアプリでセッションを持っている必要がありますが、アプリでセッションを記録していなくてもユーザーが特定のアプリに割り当てられる2つのシナリオがあります。

最初のシナリオは、`/users/track`エンドポイントを使用する際に`app_id`フィールドが入力されている場合です。具体的には、以下の例のように[イベント]({{site.baseurl}}/api/objects_filters/event_object/)または[購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/)を使用する場合です。

```json
{
    "events": [
    {
      "external_id": "john_doe123",
      "app_id": "my_web_app_id",
      "name": "Custom Event",
      "time": "2025-08-17T19:20:30+1:00"
    }
  ]
}
```

2番目のシナリオは、プッシュトークンを移行するために`/users/track`エンドポイントを使用する際に`app_id`フィールドが入力されている場合です。以下の例のようになります。

```json
{
"app_group_id": "{YOUR_APP_GROUP_ID}",
"attributes": [
{
      "push_token_import": false,
      "external_id": "external_id1",
      "country": "US",
      "language": "en",
      "{YOUR_CUSTOM_ATTRIBUTE}": "{YOUR_VALUE}",
      "push_tokens": [
        {"app_id": "{APP_ID_OF_OS}", "token": "{PUSH_TOKEN_STRING}"}
      ]
  }
]
}
```
