---
nav_title: キャンバスデータ
article_title: キャンバスデータのエクスポート
page_order: 3
page_type: reference
description: "このリファレンス記事では、キャンバスの分析データをエクスポートする方法について説明します。"
tool:
  - Canvas
  - Reports

---

# キャンバスデータのエクスポート {#export-canvas-data}

> ユーザーデータをCSVにエクスポートできます。このページでは、キャンバス全体または特定のキャンバスコンポーネントのデータをエクスポートする方法について説明します。

## キャンバスのデータをエクスポートする {#exporting-data-for-a-canvas}

キャンバスのデータをエクスポートするには、次の手順に従います。

1. **メッセージング** > **キャンバス**に移動し、キャンバスを選択します。
2. **キャンバスの詳細**セクションで**ユーザーデータ**ドロップダウンを選択します。
3. 次のいずれかのエクスポートオプションを選択します。
  - **ユーザーデータをCSV形式でエクスポート**、または
  - **メールアドレスをCSV形式でエクスポート**

キャンバスに入った全ユーザーのデータをCSVファイルとしてエクスポートすることもできます。

## キャンバスにエントリまたは再エントリしたユーザーをエクスポートする {#export-users-who-entered-or-re-entered-a-canvas}

[再適格性]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)が有効になっている場合、ユーザーは同じキャンバスに複数回エントリできます。キャンバスの詳細ページの**ユーザーデータをCSV形式でエクスポート**オプションでは、キャンバスにエントリしたユーザーがエクスポートされますが、各ユーザーのエントリ回数やエントリのタイムスタンプは含まれません。

ユーザーがキャンバスにエントリまたは再エントリした日時を分析するには、次のいずれかのオプションを使用します。

- **ユーザーごとの最新エントリ：** [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)エンドポイントを使用して、[`canvases_received`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)フィールドを含むセグメントをエクスポートします。各キャンバスについて、エクスポートにはそのユーザーの`last_entered`と`last_exited`のタイムスタンプが含まれます。`canvases_received`フィールドには過去90日間のデータが含まれます。
- **再エントリを含むすべてのエントリ：** Braze CurrentsまたはSnowflake Data Sharingの[キャンバスエントリイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#canvas-entry-events)を使用します。各`users.canvas.Entry`イベントは1回のキャンバスエントリを表し、`time`タイムスタンプが含まれます。ユーザーごとのイベント数をカウントして、エントリ回数を確認します。
- **ダッシュボードでユーザーリストを作成する：** **キャンバスバリエーションにエントリ済み**フィルターを使用してセグメントを作成し、そのセグメントをCSVにエクスポートします。[キャンバスのトラブルシューティング]({{site.baseurl}}/user_guide/messaging/canvas/troubleshooting#user-didnt-enter-a-canvas)を参照してください。

{% alert note %}
Currentsを統合しておらず、過去のすべてのエントリタイムスタンプが必要な場合は、Brazeのカスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

元のワークフローの特定のキャンバスステップについては、ステップの詳細ページで**ユーザーデータをCSV形式でエクスポート**を使用します。

## コンポーネントのデータをエクスポートする（元のワークフローのみ） {#exporting-data-for-a-component-original-workflow-only}

キャンバスの結果は、元のキャンバスワークフローのコンポーネント単位でエクスポートできます。これを行うには、特定のコンポーネントを選択し、**キャンバスステップの詳細**ページで**ユーザーデータ**ドロップダウンを選択します。

![キャンバスの詳細ページのユーザーデータドロップダウン。]({% image_buster /assets/img/canvas_csv_export.png %})

{% alert tip %}
CSVおよびAPIのエクスポートに関するヘルプについては、[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)の記事を参照してください。
{% endalert %}