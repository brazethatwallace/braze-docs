---
nav_title: Canvas データ
article_title: Canvas データのエクスポート
page_order: 3
page_type: reference
description: "このリファレンス記事では、Canvasの分析データをエクスポートする方法について説明します。"
tool:
  - Canvas
  - Reports

---

# キャンバス データのエクスポート {#export-canvas-data}

> ユーザーデータをCSVにエクスポートできます。このページでは、キャンバス全体または特定のキャンバスコンポーネントのデータをエクスポートする方法について説明します。

## キャンバスのデータをエクスポートする {#exporting-data-for-a-canvas}

キャンバスのデータをエクスポートするには、次の手順に従います。

1. **メッセージング** > **キャンバス** に移動し、キャンバスを選択します。
2. **キャンバスの詳細** セクションで**ユーザーデータ**ドロップダウンを選択します。
3. 次のいずれかのエクスポートオプションを選択します。
  - **ユーザーデータを CSV 形式でエクスポート**、または
  - **メールアドレスを CSV 形式でエクスポート**

キャンバスに入った全ユーザーのデータをCSVファイルとしてエクスポートすることもできます。

## コンポーネントのデータをエクスポートする（元のワークフローのみ） {#exporting-data-for-a-component-original-workflow-only}

キャンバスの結果は、元のキャンバスワークフローのコンポーネント単位でエクスポートできます。これを行うには、特定のコンポーネントを選択し、**キャンバスステップ Details** ページで**ユーザーデータ**ドロップダウンを選択します。

![キャンバスの詳細 ページのユーザーデータドロップダウン。]({% image_buster /assets/img/canvas_csv_export.png %})

{% alert tip %}
CSVおよびAPIのエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)」の記事を参照してください。
{% endalert %}