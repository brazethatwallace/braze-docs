---
nav_title: トラブルシューティング
article_title: Segmentsのトラブルシューティング
page_order: 9
page_type: reference
tool:
  - Segments
description: "このリファレンス記事では、セグメントエラー、ユーザーの適格性、フィルターの問題、分析の不一致に関するトラブルシューティングについて説明します。フィルターの定義については、セグメンテーションフィルターを参照してください。セグメントサイズの推定値と正確なカウントについては、セグメントサイズの測定を参照してください。"
---

# Segmentsのトラブルシューティング {#troubleshoot-segments}

> 以下から該当する症状を見つけて、適切なセクションに移動してください。このページでは、起動エラー、ユーザーの適格性、フィルターの問題、分析の不一致について説明します。フィルターの定義については、[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/)を参照してください。セグメントサイズの推定値、正確なカウント、履歴メンバーシップチャートについては、[セグメントサイズの測定]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size/)を参照してください。

## まずはここから：症状を確認する {#start-here-match-your-symptom}

| 症状 | 参照先 |
|---------|-------|
| オーディエンスが複雑すぎる | [ターゲットオーディエンスが複雑すぎて起動できない](#target-audience-is-too-complex-to-launch) |
| フィルターが保存できない | [フィルターが10,000バイトを超えているか、長すぎて保存できない](#filter-exceeds-10000-bytes-or-is-too-long-to-save) |
| Segmentにユーザーがいない | [Segmentのユーザーがゼロと表示される](#segment-shows-zero-users) |
| ユーザーがSegmentに含まれていない | [標準的な調査パス](#standard-investigation-path) |
| Segmentが予想より大きい | [Segmentが予想よりはるかに大きい](#segment-is-much-larger-than-expected) |
| Segmentのカウントがキャンペーン分析と一致しない | [*送信済みメッセージ*または*ユニーク受信者*の不一致](#message-sent-or-unique-recipients-in-campaign-analytics-doesnt-match-segment-count) |
| フィルターオプションが変更された | [フィルターオプションが変更された](#filter-options-changed) |
| ユーザーが間違ったアプリに表示される | [特定のアプリでフィルタリングすると他のアプリのユーザー情報が表示される](#info-displays-for-users-of-other-apps-when-i-filter-for-a-specific-app) |
| 過去の時点でユーザーがこのSegmentに含まれていたか？ | [遡及的なSegmentメンバーシップ](#retroactive-segment-membership) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="まずはここから：症状を確認する" }

## 標準的な調査パス {#standard-investigation-path}

ユーザーがSegmentに含まれるべきなのに含まれていない場合、またはSegmentのカウントが正しくないように見える場合は、このワークフローを使用してください。

1. **起動がブロックされた場合：** オーディエンスの複雑さや10,000バイトのフィルターエラーがCampaignまたはCanvasに表示された場合は、[エラー](#errors)（CSVの回避策、フィルターの簡素化）から始めてください。
2. **ユーザープレビューまたはユーザー検索：** 特定のユーザーをSegmentフィルターに対してテストします。ユーザーが条件の一部またはすべてに一致しない場合、一致しない条件がトラブルシューティング用に一覧表示されます。手順については、セグメントの作成の[セグメントのテスト]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#testing-segments)を参照してください。
3. **正確な統計を計算する：** Segmentの推定値が0ユーザーと表示される場合や正しくないように見える場合は、**到達可能なユーザー**パネルで**正確な統計を計算**を選択してください。計算前にSegmentを保存してください。計算がすでに実行中の場合は、完了するまで待ってください。新しい計算が完了するまで古い数値が表示される場合があります。詳細については、[正確な統計の計算]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size/#calculating-exact-statistics)を参照してください。
4. **フィルター値を確認する：** タイプミス、データタイプの不一致、古いキャンバスステップの参照、[否定フィルター + ORロジック](#segment-is-much-larger-than-expected)がないか確認してください。
5. **複雑さを確認する：** 起動がブロックされている場合は、[ターゲットオーディエンスが複雑すぎて起動できない](#target-audience-is-too-complex-to-launch)を参照してください。
6. **サポートに連絡する：** フィルター最適化に関するさらなるサポートについては、[サポートに連絡]({{site.baseurl}}/braze_support/)してください。

## Segmentのユーザーがゼロと表示される {#segment-shows-zero-users}

ダッシュボードのSegmentサイズは、多くの場合ユーザーのサンプルに基づく推定値です。非常に小さなSegmentでは、フィルターに一致するユーザーがいても、0を含む推定範囲が表示される場合があります。

- 正確なカウントを取得するには、**到達可能なユーザー**パネルで**正確な統計を計算**を選択してください。最初にSegmentを保存してください。詳細については、[推定カウントに関する考慮事項]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size/#considerations-for-estimate-counts)を参照してください。
- 小さなSegmentで**ユーザープレビュー**がゼロユーザーを返した場合でも、Segmentが空であるとは限りません。確認するには**正確な統計を計算**を実行してください。詳細については、[ユーザープレビュー]({{site.baseurl}}/user_guide/audience/segments/segment_data/#user-preview)を参照してください。

## 遡及的なSegmentメンバーシップ {#retroactive-segment-membership}

Brazeはユーザーごとの履歴Segmentメンバーシップを保存しません。特定のユーザーが過去の送信時にSegmentに含まれていたかどうかを調べることはできません。

特定の時点でのメンバーシップを記録するには、CampaignまたはCanvasを送信する前に、ダッシュボードからSegmentのユーザーをエクスポートするか、[`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)エンドポイントを呼び出してください。詳細については、[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/)（Segmentメンバーシップフィルター）および[セグメントデータをCSVにエクスポート]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv/)を参照してください。

## エラー {#errors}

### ターゲットオーディエンスが複雑すぎて起動できない {#target-audience-is-too-complex-to-launch}

このまれなエラーは、ターゲットオーディエンスに含まれる正規表現の値が多すぎる場合、正規表現の値が過度に長い場合、フィルターが過度に詳細な場合（「30,000件の郵便番号のいずれかに該当」など）、またはフィルターが多すぎる場合に発生します。これには、参照されたSegment内のフィルターや**ターゲットオーディエンス**ステップで追加されたフィルターなど、CampaignまたはCanvasオーディエンス内のすべてのフィルターが含まれます。

![複雑さのしきい値に達したターゲットオーディエンスのエラー。]({% image_buster /assets/img/segment/target_audience_too_complex_error.png %})

CampaignまたはCanvasにSegmentフィルターを追加すると、それらのフィルターはBraze内でクエリに変換されます（これらのクエリの文字数は、ダッシュボードユーザーが目にする文字数と1:1で対応するわけではありません）。BrazeがCampaignまたはCanvasを送信する際、ターゲットオーディエンス内のすべてのフィルターを組み合わせたクエリを実行します。ターゲットオーディエンスの結果クエリの文字数を制限するしきい値が適用されます。特定のCampaignまたはCanvasについて、参照されるすべてのSegmentの文字数と、すべての追加フィルターの文字数が合計されます。特定のSegmentについては、すべてのフィルターとフィルター値の文字数が合計されます。

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

特定のユーザーが現在のSegmentに一致するかどうかをテストするには、[ユーザープレビューまたはユーザー検索]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#testing-segments)を使用してください。

### 特定のアプリでフィルタリングすると他のアプリのユーザー情報が表示される {#info-displays-for-users-of-other-apps-when-i-filter-for-a-specific-app}

ユーザーは複数のアプリを持つことができるため、セグメンテーションページの**使用アプリ**セクションで特定のアプリを選択すると、少なくともそのアプリを持つユーザーの結果が返されます。このフィルターは、そのアプリのみを持つユーザーの結果を返すわけではありません。

## フィルタリング {#filtering}

### フィルターオプションが変更された {#filter-options-changed}

フィルターオプションは、カスタム属性としてBrazeに渡されるデータの形式（データタイプ）に関連しています。Brazeがカスタム属性に対して認識しているデータタイプを確認するには、**データ設定** > **カスタム属性**に移動してください。

フィルターオプションが変更された場合、データが以前とは異なる形式（データタイプ）でBrazeに渡されていることを示しています。さまざまなデータタイプとそのフィルタリングオプションの詳細な説明については、[カスタム属性のデータタイプ]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#custom-attribute-data-types)を参照してください。

ダッシュボードでカスタム属性のデータタイプを変更すると、異なる形式でBrazeに送信されるデータは拒否されることに注意してください。カスタム属性がアクティブなCampaigns、Canvases、またはSegmentsで参照されている間は、そのデータタイプを変更できません。ダッシュボードにエラーが表示され、変更がブロックされます。

カスタム属性の**値**タブには、約250,000ユーザーのサンプルからの結果が表示されます。トラブルシューティングのために特定の属性値が存在するかどうかを確認する目的で**値**タブを使用しないでください。詳細については、[値タブ]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#values-tab)を参照してください。

### Segmentが予想よりはるかに大きい {#segment-is-much-larger-than-expected}

制限的に見えるフィルターにもかかわらずSegmentが予想よりはるかに大きい場合は、同じ属性に対して否定フィルター（`is not`、`does not equal`、`does not match regex`、`not included`）を**OR**演算子で複数回使用していないか確認してください。この組み合わせは、その属性のすべての値を持つユーザーをターゲットにしてしまう可能性があります。

**OR**の代わりに**AND**を使用するタイミングについては、セグメントの作成の[OR演算子を避けるべき場合]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#when-to-avoid-the-or-operator)を参照してください。

## 分析とレポート {#analytics-and-reporting}

### Campaign分析の*送信済みメッセージ*または*ユニーク受信者*がSegmentのカウントと一致しない {#message-sent-or-unique-recipients-in-campaign-analytics-doesnt-match-segment-count}

Campaign分析の*送信済みメッセージ*または*ユニーク受信者*の数が、Segmentフィルター`Has received message from campaign X`のユーザー数と一致しない場合、3つの理由が考えられます。

1. **Campaignの起動後にユーザーがアーカイブ、孤立、または削除された可能性がある**<br><br>たとえば、1,000人のユーザーがCampaignを受信し、同日にCSVエクスポートを行ったとします。1,000人のユーザーが報告されます。翌月、その1,000人のうち50人が削除されたとします（たとえば、`users/delete`エンドポイントによって）。別のCSVエクスポートを行うと、950人のユーザーが報告されますが、**Campaign分析**の*ユニーク受信者*数は依然として1,000のままです。<br><br>つまり、*ユニーク受信者*指標は累積カウントであり、セグメンターとCSVエクスポートは現在存在するユーザーのカウントを提供します。<br><br>

2. **Campaignに再適格性が設定されており、ユーザーが複数回Campaignに再エントリーできる**<br><br>たとえば、メールCampaignの再適格性がゼロ分に設定されている（ユーザーがオーディエンスSegmentの要件を満たす限りCampaignに再エントリーできる）とし、Campaignが1か月以上実行されているとします。**Campaign分析**の*送信済みメッセージ*数は、重複ユーザーへの送信メッセージが含まれるため、Segmentの数と一致しません。<br><br>これは、Brazeがユニークユーザーを*ユニークデイリー受信者*、つまり1日に特定のメッセージを受信したユーザー数としてカウントするためです。つまり、再適格ユーザーは「ユニーク」の時間枠が1日しか持続しないため、ユニーク受信者として複数回カウントされます。その結果、*ユニークデイリー受信者*の数がCSVエクスポートのユーザープロファイル数よりも多くなる場合があります。CSVファイルのユーザープロファイルは真にユニークです。<br><br>

3. **チャネル識別子を共有するユーザーがフィルターに一致した**<br><br>`Has received message from campaign X`フィルター（およびその他の「受信済み」フィルター）は、メッセージを受信、開封、またはクリックした別のユーザープロファイルと同じプッシュトークンやメールアドレスなどのチャネル識別子を共有するユーザーに一致する場合があります。

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
