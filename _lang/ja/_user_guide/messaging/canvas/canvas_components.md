---
nav_title: キャンバスコンポーネント
article_title: キャンバスコンポーネント
page_order: 3
alias: "/user_guide/messaging/canvas/canvas_components/about/"
layout: dev_guide
guide_top_header: "キャンバスコンポーネント"
guide_top_text: "キャンバスコンポーネントを使用して、キャンバスジャーニーを強化しましょう。キャンバスコンポーネントを使用すると、過剰なフルステップを1つに置き換えることで、キャンバスの効果を判断するプロセスを簡素化できます。キャンバスのコンポーネントとは、キャンバスブランチにおけるパーソナライズされたユーザージャーニーを指します。"

page_type: landing
description: "このランディングページには、より高度なキャンバスの作成に役立つキャンバスコンポーネントの記事がまとめられています。これらのコンポーネントには、メッセージステップ、遅延ステップ、条件分岐ステップなどがあります。"
tool: Canvas

guide_featured_title: "セクション記事"
guide_featured_list:
  - name: アクションパスステップ
    link: /docs/user_guide/messaging/canvas/canvas_components/action_paths
    image: /assets/img/braze_icons/zap.svg
  - name: エージェントステップ
    link: /docs/user_guide/messaging/canvas/canvas_components/agent_step
    image: /assets/img/braze_icons/briefcase-01.svg
  - name: オーディエンスパスステップ
    link: /docs/user_guide/messaging/canvas/canvas_components/audience_paths
    image: /assets/img/braze_icons/users-01.svg 
  - name: オーディエンス同期ステップ
    link: /docs/partners/canvas_audience_sync/
    image: /assets/img/braze_icons/refresh-ccw-02.svg
  - name: コンテンツオプティマイザーステップ
    link: /docs/user_guide/messaging/canvas/canvas_components/content_optimizer_step
    image: /assets/img/braze_icons/target-04.svg
  - name: コンテキストステップ
    link: /docs/user_guide/messaging/canvas/canvas_components/context
    image: /assets/img/braze_icons/file-search-02.svg
  - name: 条件分岐ステップ
    link: /docs/user_guide/messaging/canvas/canvas_components/decision_split
    image: /assets/img/braze_icons/dataflow-04.svg
  - name: 遅延ステップ
    link: /docs/user_guide/messaging/canvas/canvas_components/delay_step
    image: /assets/img/braze_icons/clock-stopwatch.svg
  - name: 実験パスステップ
    link: /docs/user_guide/messaging/canvas/canvas_components/experiment_step
    image: /assets/img/braze_icons/columns-01.svg
  - name: フィーチャーフラグ
    link: /docs/user_guide/messaging/canvas/canvas_components/feature_flags
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: メッセージステップ
    link: /docs/user_guide/messaging/canvas/canvas_components/message_step
    image: /assets/img/braze_icons/message-square-02.svg
  - name: 送信先ステップ
    link: /docs/user_guide/messaging/canvas/canvas_components/send_to_destination
    image: /assets/img/braze_icons/dataflow-02.svg
  - name: ユーザーの更新ステップ
    link: /docs/user_guide/messaging/canvas/canvas_components/user_update
    image: /assets/img/braze_icons/user-check-01.svg
---

## キャンバスコンポーネントについて

キャンバスコンポーネントを使用すると、新しいユーザージャーニーを実現し、プロセスを改善してオーディエンスへのリーチの効果を高めることができます。

### ユーザージャーニーのカスタマイズ

![条件分岐ステップの後に遅延ステップとメッセージステップが続くキャンバスユーザージャーニーの例。]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %}){: style="float:right;max-width:55%;margin-left:15px;"}

[アクションパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)を使用すると、購入などのアクションやエンゲージメントイベントに基づいてユーザージャーニーを分岐できます。オーディエンスをフィルタリングしてターゲティングしたい場合は、[オーディエンスパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)を使用すると、オーディエンス条件に基づいてユーザーを異なるキャンバスパスに送ることで、ユーザーターゲティングを簡素化できます。

[条件分岐]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)コンポーネントは、シンプルな「はい/いいえ」のロジックを使用して、アクションまたはユーザー属性に基づく2つの相互排他的なパスを作成します。これにより、ユーザーグループの特定とターゲティングが可能になります。

[遅延]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)コンポーネントを使用すると、キャンバス内の単一ステップを遅延させることができます。キャンバス内のこのスタンドアロンの遅延ステップは、特定のタイミングでユーザーにメッセージを送信する場合に最適です。さらに、遅延コンポーネントは、オーディエンスがコンポーネントの条件を満たすための時間を確保することで、オーディエンスリーチを拡大する効果もあります。

### テスト

ユーザージャーニーを作成する際に、最も効果的なキャンバスパスをテストしたい場合があります。[実験パス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)を使用すると、任意のステップで複数のキャンバスパスをテストできます。また、ステップ間の接続を高レベルのプレビューとして使用することもできます。オレンジ色の接続は、前のステップがユーザーを次のステップにすぐに進めることを示しています。

### 統合

ブランドのファーストパーティユーザーデータと同期したいですか？[Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) および [Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) で利用可能なオーディエンス同期オプションを活用しましょう。