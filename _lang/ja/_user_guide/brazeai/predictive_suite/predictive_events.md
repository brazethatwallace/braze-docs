---
nav_title: 予測イベント
article_title: 予測イベント
description: "この記事では、Braze 予測スイートに含まれるツール「予測イベント」（旧称：購入予測）について説明します。このツールは、ユーザーが特定のイベントを実行する可能性に基づいて、そのユーザーを識別しメッセージを送信する機能をマーケターに提供します。"
page_order: 9
alias: /predictive_purchases/
search_rank: 1
---

# 予測イベント {#predictive-events}

> 予測イベントは、Braze 予測スイートにおける強力なツールであり、ユーザーが特定のイベントを実行する可能性に基づいて、そのユーザーを識別しメッセージングを行います。イベント予測を作成すると、Brazeは[勾配ブースティング決定木](https://en.wikipedia.org/wiki/Gradient_boosting)を使用して機械学習モデルをトレーニングし、過去のアクティビティから学習して将来のアクティビティを予測します。

## 予測イベントについて {#about-predictive-events}

予測が作成されると、ユーザーには、選択したイベントを実行する可能性を示す0から100までの[可能性スコア]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/analytics/#purchase_score)が割り当てられます。スコアが高いほど、ユーザーがそのイベントを実行する可能性が高くなります。また、ユーザーは低、中、高の可能性カテゴリ別にソートされます。

予測イベントの本当の価値は、予測結果を使ってセグメントやキャンペーンを作成することにあります。マーケターは、**Prediction**ページで直接ターゲットを絞ったキャンペーンを構築して、すぐに収益を上げる結果を得たり、将来のキャンペーンやキャンバスのためにセグメントを保存したりできます。最初にどのユーザーをターゲットに設定すべきかがわからない場合は、可能性スコアに基づくユーザーへのメッセージングについての[戦略的考慮事項]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/messaging_users/#strategy)をお読みください。

![「予測イベントの仕組み」と題されたグラフィックで、ユーザーデータが機械学習モデルに取り込まれる様子を示しています。ラベルには「過去のデータでトレーニングし、一定期間にイベントを実行したユーザーと実行しなかったユーザーの行動を比較する」と記載されています。また、機械学習の結果として、ユーザーがイベントを実行する可能性が低い順から高い順にランク付けされている様子も示されています。ラベルには「将来のイベントの可能性を予測し、正確で便利なターゲティングのためにユーザーに可能性スコアを割り当てる」と記載されています。]({% image_buster /assets/img/how_predictive_events_works.png %})

## 予測イベントへのアクセス {#accessing-predictive-events}

{% multi_lang_include brazeai/predictions_page_access.md %}

この機能を購入する前に、プレビューモードで利用できます。これにより、合成データを使用したデモ予測の表示や、一度に1つのプレビュー予測モデルの作成が可能です。この予測は実際のユーザーデータに基づいて作成されますが、可能性スコアに従ってメッセージングのターゲットにユーザーを設定することはできません。また、作成後に定期的に更新されることもありません。

プレビューでは、この1つの予測を編集して再構築したり、アーカイブして別の予測を作成したりすることで、[異なるオーディエンス]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/#audience)の期待される[予測品質]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/analytics/#prediction_quality)をテストし、分析に慣れることもできます。