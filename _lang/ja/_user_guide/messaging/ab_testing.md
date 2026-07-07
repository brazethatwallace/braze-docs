---
nav_title: AB テスト
article_title: AB テスト
page_order: 6
layout: dev_guide
guide_top_header: "AB テスト"
guide_top_text: "実験を行ってメッセージングを最適化しましょう。ABテストでは、同じCampaignの複数のバージョンに対するユーザーの応答を比較します。多変量テストでは、これを2つ以上の変数に拡張します。Brazeでは、セットアッププロセスが同じであるため、これらの用語は同じ意味で使用されます。ABテストと<a href='/docs/user_guide/brazeai/intelligence_suite/intelligent_selection'>インテリジェントセレクション</a> を組み合わせて、結果を自動的に最適化しましょう。"

page_type: landing
description: "BrazeでABテストと多変量実験をセットアップし、分析します。"

guide_featured_title: "セクション記事"
guide_featured_list:
  - name: コンセプト
    link: /docs/user_guide/messaging/ab_testing/concepts
    image: /assets/img/braze_icons/lightbulb-02.svg
  - name: テストの作成
    link: /docs/user_guide/messaging/ab_testing/create_tests
    image: /assets/img/braze_icons/plus-circle.svg
  - name: 最適化
    link: /docs/user_guide/messaging/ab_testing/optimizations
    image: /assets/img/braze_icons/settings-01.svg
  - name: 分析
    link: /docs/user_guide/messaging/ab_testing/analytics
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: FAQ
    link: /docs/user_guide/messaging/ab_testing/faq
    image: /assets/img/braze_icons/annotation-question.svg
---

## ABテストを使用するタイミング {#when-to-use-ab-tests}

- **新しいメッセージングタイプを試す場合:** 実験を行い、ユーザーに響くものを学びましょう。
- **オンボーディングキャンペーンや定期送信:** トラフィックの多いキャンペーンを可能な限り効果的にしましょう。
- **複数のメッセージアイデアがある場合:** テストを実行し、データドリブン型の意思決定を行いましょう。
- **前提を検証する場合:** 従来のマーケティング戦術が特定のオーディエンスに実際に効果があるかどうかをテストしましょう。

## 効果的なテストを実行するためのヒント {#tips-for-running-effective-tests}

- **大きなサンプルサイズを使用して**、結果が平均的なユーザーを反映し、外れ値に左右されないようにしましょう。
- **テストグループをランダム化して**、応答率の違いがサンプルの違いではなく、メッセージの違いを反映するようにしましょう。
- **何をテストしているかを把握しましょう。** 単一の変更を分離することで、どの要素が最も大きな影響を与えたかを特定できます。複数の違いをテストすることで、より広範なアプローチを比較できます。
- **テスト期間を事前に設定し**、初期の結果が有望に見えても、テストを早期に終了しないでください。
- **起動前にテストを追加しましょう。** 実行中のキャンペーンにテストを追加すると、不正確な結果が生じます。キャンペーンを複製し、元のキャンペーンを停止してから、複製にテストを追加してください。
- **[コントロールグループ]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#including-a-control-group)を含めて**、メッセージを送信しない場合と比較した影響を測定しましょう。