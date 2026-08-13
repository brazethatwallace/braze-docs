---
nav_title: トラブルシューティング
article_title: Canvasのトラブルシューティング
page_order: 7
page_type: reference
description: "標準的な調査パス、症状インデックス、メッセージング履歴やメッセージング診断ダッシュボードへのリンクを使用して、Canvasのエントリ、送信、分析の問題を診断します。"
tool: Canvas
---

# キャンバスのトラブルシューティング {#troubleshoot-canvases}

> このページでは、キャンバスのエントリ、送信、分析の問題を診断します。定義や詳細については、[キャンバス FAQ]({{site.baseurl}}/user_guide/messaging/canvas/faqs)を参照してください。

{% alert note %}
**メッセージング履歴**と**メッセージング診断**のログは、イベントから最大**30日間**利用可能です。特定のインシデントの調査にサポートが必要な場合は、その期間内に[Brazeサポート](#standard-investigation-path)にお問い合わせください。
{% endalert %}

## まずはここから：症状を確認する {#start-here-match-your-symptom}

| 症状 | 参照先 |
| --- | --- |
| ユーザーがキャンバスにエントリしなかった | [ユーザーがキャンバスにエントリしなかった](#user-didnt-enter-the-canvas) |
| ユーザーがエントリしたがメッセージやステップを受信しなかった | [ユーザーがキャンバスのメッセージやステップを受信しなかった](#user-didnt-receive-a-canvas-message-or-step) |
| 誰もエントリしない、または予想より少ないユーザーしかエントリしなかった | [キャンバスのエントリが少ない、またはゼロ](#low-or-zero-canvas-entries) |
| 送信数や配信数が推定オーディエンスより少ない | [送信数が予想より少ない](#lower-sends-than-expected) |
| キャンバスの分析が正しくない（コントロールグループ、コンバージョン、送信数ゼロ） | [キャンバスの分析の不一致](#canvas-analytics-mismatches) |
| 分析でエントリ数よりはるかに多い送信数、またはエントリ数より多い離脱数が表示される | [日付範囲のフィルタリングにより予期しない数値が表示されることがある](#date-range-filtering-can-show-unexpected-numbers) |
| キャンバスが保存できない、またはエディターがフリーズする | [エディターと保存の問題](#editor-and-save-issues) |
| キャンバスを停止したがメッセージが送信された | [停止したキャンバスの動作](#stopped-canvas-behavior) |
| 起動時に「キャンバスのブランチが多すぎます」エラーが表示される | [「キャンバスのブランチが多すぎます」エラー](#too-many-canvas-branches-error) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="キャンバスの症状" }

## 標準的な調査パス {#standard-investigation-path}

このワークフローを使用して、特定のユーザーまたは集計送信の問題を調査します。すべてのインシデントについてステップ1から始めてください。

1. キャンバスがアクティブであることを確認します（下書き、停止済み、またはアーカイブ済みではないこと）。
2. エントリスケジュール（スケジュールされたウィンドウ、タイムゾーン、アクションベースのトリガー、またはAPIトリガーのエントリ）が、ユーザーがエントリすると予想されるタイミングと一致していることを確認します。
3. **オーディエンス** > **ユーザー検索**に移動し、プロファイルを開いて**メッセージ履歴**（過去30日間）を選択して、ユーザーのメッセージングレコードを確認します。
   - 予想される送信時刻のレコードが存在しない場合、問題はメッセージではなくエントリにあります。[ユーザーがキャンバスにエントリしなかった](#user-didnt-enter-the-canvas)に移動してください。
4. キャンバスの**変更ログ**と、ターゲティングに使用されているセグメントの変更ログを確認します。インシデント中にオーディエンス、ステップ、または送信設定が変更されていないことを確認します。
5. [メッセージング診断ダッシュボード]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard)を開き、中止およびドロップの理由を確認して、キャンバス分析ページで集計結果を確認します。
   - 認識できない結果が表示された場合は、診断ドキュメントの[中止の結果]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes)を参照してください。
   - ステップのエントリがゼロ（送信がゼロではなく）の場合は、前のステップタイプ（[アクションパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)、[遅延]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)、[オーディエンスパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)、または[条件分岐]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)）を確認してください。
6. それでも解決しない場合は、キャンバスID、影響を受けたユーザーID、タイムスタンプ（タイムゾーン付き）、およびメッセージ履歴またはメッセージング診断のスクリーンショットを添えて、30日以内に[Brazeサポート]({{site.baseurl}}/braze_support)に連絡してください。

起動前に、[テストキャンバスの送信]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases)と[ユーザーパスのプレビュー]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths)を使用して設定を検証してください。

## ユーザーがキャンバスにエントリしなかった {#user-didnt-enter-the-canvas}

**症状：** 期待していたタイミングでユーザーがキャンバスにエントリしなかった、またはトリガーイベントが示す数よりもエントリしたユーザーが少ない。

Brazeがエントリトリガーを評価する前に、ユーザーは**ターゲットオーディエンス**に一致している必要があります（[属性の変更]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)トリガーを除く）。トリガーだけでは、評価時にユーザーがオーディエンスに含まれていなかった場合、エントリは保証されません。

再適格性と再エントリは、[エントリコントロールの選択]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls)で別々のコントロールです。

- **再適格性：** ユーザーがキャンバスを退出した後に再度エントリできるかどうかを決定します（時間枠と**ユーザーにキャンバスへの再エントリを許可する**設定）。
- **再エントリ：** 現在キャンバス内にいるユーザーが同時に別のパスにエントリできるかどうかを決定します。

ユーザーは再適格であっても、まだキャンバス内にいるためにブロックされる場合や、退出済みでも再適格性の時間枠外である場合があります。ユーザーがキャンバスに再エントリしない場合は、両方の設定を確認してください。

以下を確認してください。

- **エントリスケジュールとタイムゾーン：** キャンバスが有効であり、ユーザーが[エントリウィンドウ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule)中にトリガーを実行したことを確認します。
- **評価時のターゲットオーディエンス：** セグメントとフィルターの変更ログを確認します。[ユーザー検索]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)は、一部のフィルタータイプ（例：文字列形式の日付属性）で偽陽性を示す場合があります。
- **エントリ上限：** [最大エントリ数]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls)またはオーディエンス上限に達している可能性があります。
- **グローバルコントロールグループ：** [グローバルコントロールグループ]({{site.baseurl}}/user_guide/audience/global_control_group)に含まれるユーザーは、メッセージングキャンバスにエントリしません。
- **キャンバスコントロールグループ：** エントリ時にキャンバスコントロールグループに割り当てられたユーザーは、バリアントメッセージを受信しません。バリアントの割り当てはエントリ時に行われ、セグメントフィルターを通じて行われるものではありません。[キャンバス分析の不一致](#canvas-analytics-mismatches)を参照してください。
- **退出条件：** ユーザーがエントリ前またはエントリ中に[退出条件]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria)に一致した可能性があります。エントリと退出が同じイベントを使用している場合は、[エントリ条件と退出条件の一致]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/matching_entry_and_exit_criteria)を参照してください。
- **APIトリガーエントリ：** ユーザーが[`/canvas/trigger/send`エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)で追加されたことを確認します。キャンバスエントリフィルターで[セグメントを作成]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)し、[`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)でユーザーをエクスポートできます。

### トリガーイベント数がキャンバスエントリ数より多い {#trigger-event-count-is-higher-than-canvas-entries}

**症状：** トリガーイベントのボリュームがキャンバスエントリ数より多い。

Brazeは同じ瞬間に発生した複数のエントリ試行を重複排除するため、トリガーイベントよりもキャンバスエントリが少なくなる場合があります。複数のエントリをテストする場合は、トリガーイベントを少なくとも1秒間隔で実行してください。

ユーザーが1秒以内に同じトリガーを複数回実行した場合、Brazeは1回のエントリのみを処理します。再エントリまたは再適格性ルールが適用される場合は、メッセージング診断で**ユーザーが再適格でない**などの結果を確認してください。

{% details 夏時間と毎日スケジュールされたキャンバス %}

夏時間（DST）の切り替え日には、毎日スケジュールされたキャンバスが通常より最大1時間早くまたは遅く実行される場合があります。エントリ条件がスケジュールされたエントリ時刻の1時間以内のタイムスタンプを持つカスタム属性やイベントに依存している場合、属性やイベントがまだ記録されていないため、DST当日にユーザーが適格にならない可能性があります。

例えば、ユーザーが通常キャンバスのタイムゾーンで午後3時にカスタム属性の更新を受け取り、キャンバスが同じタイムゾーンで毎日午後3時30分に実行されるとします。春の時計を進めるDSTの日には、キャンバスがその属性更新に対して通常より最大1時間早くユーザーを評価する可能性があり、属性が記録される前に評価が行われます。再適格性がオフになっている場合、前日にエントリしたユーザーは再エントリできず、その日のエントリがゼロになります。

これを回避するには、カスタム属性またはイベントの更新がキャンバスのスケジュールされたエントリ時刻の1時間以上前に行われるようにしてください。

{% enddetails %}

## ユーザーがキャンバスのメッセージやステップを受信しなかった {#user-didnt-receive-a-canvas-message-or-step}

**症状：** ユーザーがキャンバスにエントリしたが、期待されるメッセージやステップを受信しなかった。

ユーザーの[**メッセージ履歴**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab)で、キャンバスのステップとタイムスタンプを確認してください。記録が存在しない場合は、[ユーザーがキャンバスにエントリしなかった](#user-didnt-enter-the-canvas)に戻ってください。

次に、トリガーまたはステップタイプごとに以下を確認してください。

- **カスタムイベントまたは購入トリガー：** イベントが**Analytics** > **カスタムイベントレポート**（購入の場合は**収益**）に表示されることを確認します。イベントのタイムスタンプを、キャンバスが公開された時刻およびステップに設定されたスケジュール遅延と比較してください。
- **APIトリガーエントリ：** [ユーザーがキャンバスにエントリしなかった](#user-didnt-enter-the-canvas)で説明されているように、キャンバスのセグメントフィルターとエクスポートでエントリを確認します。
- **アクションパスまたはメッセージステップのトリガー：** ユーザーが前提条件となるイベントを実行したこと、および[イベントプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#event-properties)がそのステップで利用可能であることを確認します。
- **アプリ内メッセージステップ：** アプリ内メッセージは、ユーザーがステップにエントリした後の次のセッション開始時に送信され、SDKイベントからのみ送信されます（REST APIからは送信されません）。[キャンバスのアプリ内メッセージはいつ送信されますか？]({{site.baseurl}}/user_guide/messaging/canvas/faqs#when-are-in-app-messages-in-canvas-sent)（キャンバスFAQ）を参照してください。
- **キャンバスのコントロールグループ：** ユーザーがエントリ時にキャンバスのコントロールグループに割り当てられていないことを確認します。
- **チャネルの適格性と送信設定：** 購読ステータス、プッシュ有効状態、およびステップごとの[送信設定]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings)（例：**購読設定**がオプトイン済みユーザーのみに設定されている場合）を確認します。マルチチャネルキャンバスの**ターゲットオーディエンス**に単一チャネルのフィルターを追加しないでください。
- **配信バリデーション：** メッセージステップで**メッセージ送信時にオーディエンスを検証**を有効にしている場合、送信時にフィルターに一致しなくなったユーザーはメッセージを受信しません。[配信バリデーション]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations)を参照してください。
- **サイレント時間、インテリジェントタイミング、フリークエンシーキャップ、レート制限：** これらにより、送信が延期、抑制、または中止される場合があります。サイレント時間による中止後も、ユーザーはキャンバスに残る場合があります。
- **競合：** ユーザーが複数のアクションを同時にトリガーした場合は、[競合]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions)を参照してください。

{% alert important %}
キャンバスのメッセージステップが送信を中止した場合でも、ユーザーは次のステップに進みます。キャンバスは中止時にも進行するため、後続の遅延ステップやアクションパスステップが永続的にブロックされることはありません。[ユーザーの進行方法]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance)および[中止の結果]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes)を参照してください。
{% endalert %}

ステップレベルのフィルター、ブランチ間の競合、およびアプリ内メッセージの分岐動作については、[キャンバスフローでの起動 — トラブルシューティング]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#troubleshooting)および[キャンバスFAQ]({{site.baseurl}}/user_guide/messaging/canvas/faqs#messages-and-delivery)を参照してください。

{% alert important %}
アクションベースのキャンバスが予想より早くメッセージを送信する場合は、カスタムイベントのタイムスタンプが過去の日時ではなく現在の時刻を使用していることを確認してください。Brazeはイベントとともに送信されたタイムスタンプから遅延を評価します。[アクションベースの配信]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule)を参照してください。
{% endalert %}

## キャンバスのエントリが少ない、またはゼロ {#low-or-zero-canvas-entries}

**症状：** キャンバスに誰もエントリしない、または予想より少ないユーザーしかエントリしない。

まず[キャンバスフローの起動チェックリスト]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#launch-checklist)を確認してから、以下を確認してください。

- キャンバスがアクティブであり、現在の時刻がスケジュールされたエントリウィンドウ内であること。
- [エントリ設定]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls)（再適格性、最大エントリ数、エントリ上限）が、エントリを期待するユーザーを許可していること。
- ターゲットオーディエンスとセグメントフィルターが、起動後も期待するユーザーと一致していること。
- グローバルおよびキャンバスのコントロールグループの割合が、各パスにエントリするユーザーとメッセージを受信するユーザーの比率を正しく示していること。
- ワークスペースのレート制限やエントリキューにより、ユーザーが適格になってからエントリまたはステップに進むまでに遅延が発生することが想定されていること。

単一のユーザーについては、[標準的な調査パス]({{site.baseurl}}/braze_support)に従ってください。夏時間（DST）に関連するゼロエントリについては、[ユーザーがキャンバスにエントリしなかった](#user-didnt-enter-the-canvas)の折りたたみセクションを参照してください。

## 予想より送信数が少ない {#lower-sends-than-expected}

**症状：** キャンバスステップの推定オーディエンスに対して、送信数または配信数が少ない。

一般的な原因には、送信時のオーディエンス再評価、チャネルの適格性、コントロールグループ、サイレント時間帯、インテリジェントタイミング、レート制限、アプリ内メッセージの配信動作（アプリ内メッセージでは*送信数*がゼロでインプレッションがあるのは想定どおりの動作です）が含まれます。

メッセージステップで多くのユーザーがエントリしたにもかかわらず送信数が少ない場合は、Liquidの`abort_message()`が送信をキャンセルしていないか確認してください。メッセージアクティビティログの確認、属性の欠落、テスト送信については、[高い中止率のトラブルシューティング]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages#troubleshooting-high-abort-rates)を参照してください。

詳細なリストについては、キャンバスFAQの[推定オーディエンスサイズより送信数が少ないのはなぜですか？]({{site.baseurl}}/user_guide/messaging/canvas/faqs#why-are-sends-lower-than-the-estimated-audience-size)、およびキャンペーン向けの[推定オーディエンスサイズより送信数が少ないのはなぜですか？]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size)を参照してください。

[メッセージング診断ダッシュボード]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard)を使用して、ステップレベルでの中止理由やドロップ理由を確認できます。

## キャンバス分析の不一致 {#canvas-analytics-mismatches}

**症状：** キャンバス分析が正しくない（コントロールグループの分割、コンバージョン、またはゼロ送信）。

コントロールグループとバリアントの割り当ては、ビルダーで設定したパーセンテージに基づいてキャンバスエントリ時に行われます。セグメントフィルターを通じて行われるわけではありません。特定のチャネルを受信できないユーザーでもバリアントにエントリする場合があります。**ターゲットオーディエンス**をチャネルフィルターで絞り込むのではなく、ステップごとの[送信設定]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings)を使用して、各メッセージタイプを受信するユーザーを制限してください。

キャンバスのコントロールグループと[グローバルコントロールグループ]({{site.baseurl}}/user_guide/audience/global_control_group)を区別してください。フィルターの定義については、キャンバスFAQの[「キャンバスバリアントに入っていない」と「キャンバスコントロールグループに含まれていない」の違いは何ですか？]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group)を参照してください。

{% details バリアントの送信数がバリアントのパーセンテージより低くなる理由 %}

次のシナリオを想像してみてください。

- キャンバスに1つのバリアントと1つのコントロールグループがあります。
- バリアントの最初のステップはプッシュ通知です。
- ユーザーの90%がバリアントにエントリするよう選択され、10%がコントロールグループにエントリするよう選択されました。

![90%のバリアントと10%のコントロールグループを持つキャンバスの例。]({% image_buster /assets/img_archive/trouble15.png %})

このシナリオでは、キャンバスにエントリするユーザーの90%がバリアントにエントリします。

アクティブユーザーセグメントを確認すると、29.8kのユーザーが含まれていますが、そのうちプッシュが有効なのは64%のみであることがわかります。

![「プッシュ有効」フィルターが「true」に設定され、推定ユーザー数が29.8kのセグメント。]({% image_buster /assets/img_archive/trouble16.png %})

つまり、ユーザーの90%がバリアントにエントリするよう指定しても、そのすべてのユーザーがプッシュ通知を受信できるわけではありません。プッシュを受信できないユーザーもバリアントにはエントリします。送信数はエントリ時のバリアント割り当てではなく、ステップ時のチャネル適格性を反映しています。

{% enddetails %}

### 日付範囲フィルタリングで予期しない数値が表示される場合 {#date-range-filtering-can-show-unexpected-numbers}

**症状：** キャンバスまたはステップの分析で、エントリ数よりはるかに多い送信数や、エントリしたユーザーよりも多くのユーザーがステップを退出しているなど、予期しない数値や不自然な数値が表示される。

これは、キャンバス分析ページの上部にある日付範囲カレンダーフィルターを使用した場合に発生することがあります。一部のユーザーアクションを除外する日付範囲を選択すると、表示される指標は各ユーザーのジャーニーの一部のみを示す場合があります。

例：
- 日付範囲がほとんどのユーザーがエントリした後から始まり、メッセージを受信した期間を含む場合、100件のエントリに対して8,000件の送信が表示されることがあります。
- 日付範囲が退出のみをキャプチャし、それ以前のエントリを含まない場合、前のステップにエントリしたユーザーよりも多くのユーザーが次のステップに移動しているように表示されることがあります。

これを解決するには、キャンバスが開始された日から現在までのすべての日付を含むように日付範囲を調整するか、必要な指標に関連する全期間をカバーする範囲を選択してください。

コンバージョン率の定義とステップレベルの分析については、キャンバスFAQの[分析とコンバージョン]({{site.baseurl}}/user_guide/messaging/canvas/faqs#analytics-and-conversions)を参照してください。

## エディターと保存の問題 {#editor-and-save-issues}

**症状：** キャンバスエディターが読み込まれない、フリーズする、または変更が保存されない。

| 症状 | 最も可能性の高い原因 |
| --- | --- |
| 保存ボタンがエラーなしで無限に回転する | キャンバスオーディエンスまたはステップフィルターに空または不完全なカスタム属性フィルターがあります。フィルターを削除するか、有効な属性を選択してください |
| 編集中に「Request Timed Out」エラーが発生する | ブラウザー拡張機能の干渉、広告ブロッカー、またはセッションの期限切れが原因です。シークレットウィンドウまたは別のブラウザーで試してください |
| バリアントをアーカイブした後に保存できない | アーカイブされたバリアントがダウンストリームでまだ参照されています。ステップの接続を確認し、バリアントを復元または置き換えてください |
{: .reset-td-br-1 .reset-td-br-2 aria-label="エディターの症状" }

大規模または複雑なキャンバスでエディターがフリーズする場合は、以下を試してください。

- ブラウザーのキャッシュとCookieをクリアしてから、ページを再読み込みしてください。企業の広告ブロッカーやブラウザー拡張機能がBrazeプラットフォームに干渉する場合があります。
- キャンバスのズームコントロールを使用して、表示を25%または10%に縮小し、ブラウザーがレンダリングするUIの量を減らしてください。
- 別のWebブラウザーを試してください。

キャンバスが読み込まれず進行しない場合、以前のバージョンが正しく保存されておらず、無効なステップが含まれている可能性があります。ダッシュボードからキャンバスを複製してください。問題が解決しない場合は、[サポートチケット]({{site.baseurl}}/braze_support)を開いてください。

「Request Timed Out」のサポートチケットには、画面録画、タイムスタンプとタイムゾーン、ブラウザーとバージョン、再現手順、およびオプションでブラウザーの開発者ツールからのHARログを含めてください。詳細については、キャンバスFAQの[「Request Timed Out」エラーのサポートチケットを送信する際に何を含めるべきですか？]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error)を参照してください。

## キャンバス停止時の動作 {#stopped-canvas-behavior}

**症状：** キャンバスを停止したのに、ユーザーがまだメッセージを受信しています。

キャンバスを停止すると、ユーザーはキャンバスに入ることができなくなり、キャンバスフローからそれ以上のメッセージは送信されません。ただし、すでにメールサービスプロバイダーに引き渡されたメール送信は取り消すことができません。

遅延ステップまたはアクションパスステップで待機中のユーザーは、キャンバスを停止しても自動的にジャーニーから削除されません。スケジュールされた送信時刻が過ぎる前にキャンバスを再度有効にすると、保留中のステップがそのまま送信される場合があります。

詳細については、キャンバスFAQの[キャンバスを停止するとどうなりますか？]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-when-you-stop-a-canvas)を参照してください。

## 「キャンバスのブランチが多すぎます」エラー {#too-many-canvas-branches-error}

**症状：** スケジュールされたキャンバスを起動する際に「キャンバスのブランチが多すぎます」エラーが表示されます。

このエラーは、ステップの分岐とエントリオーディエンスサイズの組み合わせにより、メッセージの送信を妨げるクラスターパフォーマンスの問題が発生する可能性がある場合に表示されます。Brazeは、スケジュールされたエントリを持つキャンバスを起動する際にこのメッセージを表示します。下書きを保存する際には表示されません。

解決するには：

- キャンバス内のステップの分岐を減らします。
- エントリオーディエンスサイズを縮小します。
- 多数の並列パスの代わりに、[オーディエンスパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)を使用して分岐を統合します。
- キャンバスがオリジナルエディターを使用している場合は、[キャンバスフローに複製]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases)し、キャンバスコンポーネントで再構築します。

変更なしでキャンバスを起動する必要があり、キャンバスフローに移行できない場合は、[サポート]({{site.baseurl}}/support_contact)にお問い合わせください。

## サポートへの問い合わせが必要な場合 {#when-to-contact-support}

[標準的な調査パス](#standard-investigation-path)を完了しても問題が解決しない場合は、問題発生から30日以内に[Brazeサポート]({{site.baseurl}}/braze_support)にお問い合わせください。

以下の情報を含めてください：

- キャンバスIDと影響を受けたユーザーID（external IDまたはBraze ID）
- タイムゾーン付きのタイムスタンプ
- **メッセージング履歴**または**メッセージング診断**のスクリーンショットまたはエクスポート
- エディターの「Request Timed Out」エラーの場合は、[エディターと保存の問題](#editor-and-save-issues)に記載されている詳細情報