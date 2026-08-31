---
nav_title: AB テスト
article_title: AB テスト
page_order: 6
layout: dev_guide
guide_top_header: "AB テスト"
guide_top_text: "実験を行ってメッセージングを最適化しましょう。ABテストでは、同じキャンペーンの複数のバージョンに対するユーザーの応答を比較します。多変量テストでは、これを2つ以上の変数に拡張します。Brazeでは、セットアッププロセスが同じであるため、これらの用語は同じ意味で使用されます。<a href=\"/docs/user_guide/brazeai/intelligence_suite/variant_selection\">BrazeAI<sup>TM</sup>で最適化</a> を使用して、結果を自動的に最適化しましょう。"

page_type: landing
description: "BrazeでABテストと多変量実験を設定し、分析します。"

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

- **新しいメッセージングタイプを試す場合：** 実験して、ユーザーに何が響くかを学びましょう。
- **オンボーディングキャンペーンや定期送信：** トラフィックの多いキャンペーンが可能な限り効果的であることを確認しましょう。
- **複数のメッセージアイデアがある場合：** テストを実施し、データドリブン型の意思決定を行いましょう。
- **前提を検証する場合：** 従来のマーケティング戦術が実際に特定のオーディエンスに効果があるかどうかをテストしましょう。

## 効果的なテストを実施するためのヒント {#tips-for-running-effective-tests}

- **大きなサンプルを使用する**ことで、結果が平均的なユーザーを反映し、外れ値に左右されないようにします。
- **テストグループをランダム化する**ことで、反応率の違いがサンプルの違いではなく、メッセージの違いを反映するようにします。
- **何をテストしているかを把握してください。**単一の変更を分離すると、どの要素が最も大きな影響を与えたかを特定できます。複数の違いをテストすると、より広範なアプローチを比較できます。
- **テスト期間を事前に設定し**、初期の結果が有望に見えても、テストを早期に終了しないでください。
- **起動前にテストを追加してください。**実行中のキャンペーンにテストを追加すると、不正確な結果が生じます。キャンペーンを複製し、元のキャンペーンを停止してから、複製にテストを追加してください。
- **[コントロールグループ]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#including-a-control-group)を含める**ことで、メッセージをまったく送信しない場合と比較した影響を測定します。