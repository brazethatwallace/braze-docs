---
nav_title: ベストプラクティス
article_title: Canvasのベストプラクティス
page_order: 1
description: "この記事では、Canvasとキャンバスフローを使用してユーザージャーニーを作成・カスタマイズするためのベストプラクティスを紹介します。"
tool: Canvas

---

# Canvasのベストプラクティス {#canvas-best-practices}

> この記事では、Canvasとキャンバスフローを使用してユーザージャーニーを作成・カスタマイズするためのベストプラクティスを紹介します。

## 目的を明確にする {#identify-your-purpose}

何を、誰に、なぜ行うのかを掘り下げましょう！
- ユーザーに何を達成してもらいたいですか？
- リーチしたいユーザーは誰ですか？
- なぜこのCanvasを構築するのですか？

## 組み合わせて活用する {#mix-and-match}

[Canvasコンポーネント]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about)を使って、ユーザージャーニーの新しい組み合わせを実現しましょう。
- [条件分岐]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)でユーザーを分割し、異なるワークフローを構築しましょう。
- [遅延]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)ステップでユーザージャーニーに間隔を設けましょう。
- キャンバスフローの任意の場所に[スタンドアロンメッセージ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)を追加しましょう。

{% alert note %}
キャンバスステップでは、ユーザーをフロー内で前方にのみ移動させることができます。ステップを前のステップにリンクするようにCanvasを設定することはできません。これはユーザーを逆方向に送ることになるためです。このバリデーションにより、ユーザーはCanvas内を一方向にのみ進むことが保証されます。
{% endalert %}

## よりリッチなメッセージを作成する {#create-richer-messages}

よりリッチなメッセージでユーザーの関心を引きましょう。

- オンボーディングCanvasesに[アプリ内メッセージ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas)を組み込み、第一印象を最大限に活用しましょう。
- Canvasジャーニーにプロモーションオファーやプッシュ通知用の[Content Cards]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/content-cards_in_canvas)を導入しましょう。

## ユーザージャーニーをテストする {#test-your-user-journeys}

コントロールグループを組み込んで、Canvasメッセージングの効果を測定しましょう。これにより、Canvasがどのように受け取られたかを理解できます！

- Canvasの各ステップに名前を付けて、ユーザージャーニーを識別しましょう。
- ユーザージャーニーで[実験パス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)コンポーネントを活用し、作成した異なるパスにユーザーをランダムに割り当てましょう。
- 遅延ステップとメッセージステップを使ってユーザージャーニーを多様化し、最も効果的なパスを見つけましょう。
- [Canvas分析]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics)を確認して、ユーザージャーニーの各コンポーネントのパフォーマンスを把握しましょう。
- 初回起動後に[Canvasを編集]({{site.baseurl}}/post-launch_edits)しましょう。

## Canvasのスケジュール設定 {#scheduling-your-canvases}

{% alert note %}
Canvasでは、すでに過ぎた時刻でのスケジュール送信は使用できません。ただし、Campaignがスケジュールされたのとまったく同じ分（またはその数秒前）にCanvasを起動することは可能です。これにより、Canvasがスケジュールされたエントリ時刻を逃し、ユーザーがCanvasに入れなくなる可能性があります。スケジュール送信時刻の数分以内にCampaignsが編集された場合は、Canvasを即時送信することをお勧めします。
{% endalert %}

{% alert important %}
スケジュールされたエントリまたは送信ウィンドウの直前にオーディエンス、スケジュール、または配信設定を変更した場合、一部のユーザーはすでにステップで待機中であるか、以前の設定で評価されている可能性があるため、全員が変更を反映するとは限りません。スケジュールの変更、オーディエンスの変更、**エンキュー時に評価**、およびメッセージステップの配信タイミングがどのように連携するかについては、[起動後のCanvasの変更]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch)を参照してください。不明な場合は、Canvasを停止してから複製し、再起動してクリーンな再評価を行ってください。
{% endalert %}

キャンバスステップについては、Canvasのスケジュール設定時に以下の点を考慮してください。

- スケジュールの変更は、まだステップの受信を待っていないユーザーにのみ適用されます。
- オーディエンスの変更はデフォルトですべてのユーザーに適用されますが、ステップの受信を待っていないユーザーにのみ変更を適用するようにスケジュールすることもできます。
- デプロイ後すぐに配信するようにスケジュールされたCanvasを編集し、**更新**を選択すると、実質的にそのCanvasが送信されます。

### 起動後の編集 {#post-launch-edits}

アクティブなCanvasを停止する際に未保存の下書きが存在する場合、停止によってその下書きが破棄される可能性があります。進行中の編集を保持する必要がある場合は、停止する前に下書きを保存、起動、または破棄してください。

#### オーディエンス評価のタイミング {#audience-evaluation-timing}

Brazeは、Canvasビルダーおよび個々のステップの異なるタイミングでオーディエンスを評価します。設定の詳細については、以下を参照してください。

- Canvasを作成する際の[ターゲットエントリオーディエンスの設定]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-13-set-your-target-entry-audience)と[Canvasエントリスケジュールの決定]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule)
- [ターゲットオーディエンスとエントリ条件の連携]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users#how-target-audience-and-entry-criteria-work-together)
- メッセージステップの[配信設定の編集]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#step-2-edit-delivery-settings)
- オーディエンスパスステップの[ユーザーの評価方法]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths#how-users-are-evaluated)

ライブCanvasをスケジュールされたエントリまたは送信ウィンドウの直前に編集した場合、すでに**メッセージ**ステップのキューに入っているユーザーには変更が反映されない可能性があります。詳細については、[起動後のCanvasの編集]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch)を参照してください。