このテンプレートを使って、Braze Docsのあらゆるページやセクションを作成できます。環境のセットアップ、プレビュー、コンテンツタイプについては、リポジトリへのアクセス権を持つコントリビューターは`docs/contributing/`配下のハンドブック（例: `generating_a_preview.md`や`content_types.md`）を参照してください。その他のユーザーは[ドキュメントフィードバック]({{site.baseurl}}/feedback/)からドキュメントチームにお問い合わせいただけます。

{% details テンプレートを表示 %}
{% raw %}
`````markdown
---
nav_title: NAV_TITLE
article_title: ARTICLE_TITLE
description: "SHORT_DESCRIPTION."
alias: /OPTIONAL_SHORT_ARTICLE_TITLE/
page_type: reference
layout: OPTIONAL_LAYOUT_FILE
---

<!-- ページのタイトル。ページ内のタイトル表示に使用されます。 -->
# ARTICLE_TITLE

<!-- 概要は '>' 文字で始まり、カバーする内容について説明します。オプションの後続段落では、トピックをハイレベルで紹介します。 -->
> DESCRIPTION.

INTRODUCTION.

<!-- このタスクの前提条件です。前提条件が不要な場合は、このセクションを削除できます。 -->
## 前提条件

始める前に、以下を完了する必要があります:

- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE

<!-- 機能のワークフローについてのオプションの簡単な説明です。 -->
## 仕組み

CONTENT.

<!-- ユーザーに機能の統合と有効化の手順を案内します。 -->
 ## インテグレーション
CONTENT.

<!-- ネストされたステップを含むハウツーガイドです。 -->
## TASK_TO_COMPLETE

<!-- タスクのオプションの概要です。 -->
CONTENT.

<!-- ステップの目標を説明するアクション指向のヘッダーです。 -->
### ステップ 1: ACTION_TO_COMPLETE

<!-- 番号付きの箇条書きまたは段落を使用して、このアクションの完了方法を説明します -->
CONTENT.

### ステップ 2: ACTION_TO_COMPLETE

CONTENT.
<!-- サポートされるデータタイプ、フィールド、定義などのオプションの参照です。 -->
### REFERENCE_TO_ASSIST_WITH_ACTION

CONTENT.

<!-- オプションのステップの場合は、ヘッダーの末尾に「（オプション）」を追加します。 -->
### ステップ 3: OPTIONAL_ACTION_TO_COMPLETE（オプション）

CONTENT.
<!-- サポートされる内容についてのオプションのセクションです。ネストされたヘッダーを追加してより具体的にできます。 -->
## サポートされるデータタイプ / サポートされる属性 / サポートされるイベント / サポートされるその他
CONTENT.
<!-- 機能を使用する前にユーザーが確認すべき重要な考慮事項についてのオプションのセクションです。 -->
## 考慮事項

CONTENT.

<!-- よくある問題のトラブルシューティングをユーザーに案内するオプションのセクションです。 -->
## トラブルシューティング

### ISSUE_TO_TROUBLESHOOT
CONTENT.

```
{% endraw %}
{% enddetails %}