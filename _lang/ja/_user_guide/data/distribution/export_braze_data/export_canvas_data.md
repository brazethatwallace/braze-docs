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

# Canvas データのエクスポート {#export-canvas-data}

> ユーザーデータをCSVにエクスポートできます。このページでは、Canvas全体または特定のCanvasコンポーネントのデータをエクスポートする方法について説明します。

## Canvasのデータをエクスポートする {#exporting-data-for-a-canvas}

Canvasのデータをエクスポートするには、次の手順に従います。

1. **メッセージング** > **Canvas** に移動し、Canvasを選択します。
2. **Canvas Details** セクションで**ユーザーデータ**ドロップダウンを選択します。
3. 次のいずれかのエクスポートオプションを選択します。
  - **ユーザーデータを CSV 形式でエクスポート**、または
  - **メールアドレスを CSV 形式でエクスポート**

Canvasに入った全ユーザーのデータをCSVファイルとしてエクスポートすることもできます。

## コンポーネントのデータをエクスポートする（元のワークフローのみ） {#exporting-data-for-a-component-original-workflow-only}

Canvasの結果は、元のCanvasワークフローのコンポーネント単位でエクスポートできます。これを行うには、特定のコンポーネントを選択し、**Canvas Step Details** ページで**ユーザーデータ**ドロップダウンを選択します。

![Canvas Details ページのユーザーデータドロップダウン。]({% image_buster /assets/img/canvas_csv_export.png %})

{% alert tip %}
CSVおよびAPIのエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)」の記事を参照してください。
{% endalert %}