---
nav_title: トラブルシューティング
article_title: キャンバスのトラブルシューティング
page_order: 7
page_type: reference
description: "標準的な調査パス、症状インデックス、メッセージング履歴やメッセージング診断ダッシュボードへのリンクを使用して、キャンバスのエントリ、送信、分析の問題を診断します。"
tool: Canvas
---

# キャンバスのトラブルシューティング {#troubleshoot-canvases}

> このページでは、キャンバスのエントリ、送信、分析の問題を診断します。定義や詳細については、[キャンバスFAQ]({{site.baseurl}}/user_guide/messaging/canvas/faqs)を参照してください。

{% alert note %}
**メッセージング履歴**と**メッセージング診断**のログは、イベントから最大**30日間**利用可能です。特定のインシデントの調査にサポートが必要な場合は、その期間内に[Brazeサポート](#standard-investigation-path)にお問い合わせください。
{% endalert %}

## まずはここから：症状を確認する {#start-here-match-your-symptom}

| 症状 | 参照先 |
| --- | --- |
| ユーザーがキャンバスにエントリしなかった | [ユーザーがキャンバスにエントリしなかった](#user-didnt-enter-the-canvas) |
| ユーザーがエントリしたがメッセージやステップを受信しなかった | [ユーザーがキャンバスのメッセージやステップを受信しなかった](#user-didnt-receive-a-canvas-message-or-step) |
| エントリしたユーザーがいない、または予想より少ない | [キャンバスのエントリ数が少ない、またはゼロ](#low-or-zero-canvas-entries) |
| 送信数や配信数が推定オーディエンスより少ない | [送信数が予想より少ない](#lower-sends-than-expected) |
| キャンバスの分析が正しくない（コントロールグループ、コンバージョン、送信数ゼロ） | [キャンバスの分析の不一致](#canvas-analytics-mismatches) |
| 分析でエントリ数よりはるかに多い送信数、またはエントリ数より多い離脱数が表示される | [日付範囲のフィルタリングで予期しない数値が表示されることがある](#date-range-filtering-can-show-unexpected-numbers) |
| キャンバスが保存できない、またはエディターがフリーズする | [エディターと保存の問題](#editor-and-save-issues) |
| キャンバスのバリアントを削除できない | [アーカイブされたセグメントが原因でキャンバスのバリアントを削除できない](#cant-delete-a-canvas-variant-because-of-an-archived-segment) |
| キャンバスを停止したがメッセージが送信された | [停止したキャンバスの動作](#stopped-canvas-behavior) |
| 起動時に「Too many キャンバス branches」エラーが表示される | [「Too many キャンバス branches」エラー](#too-many-canvas-branches-error) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="キャンバスの症状" }

## 標準的な調査パス {#standard-investigation-path}

特定のユーザーまたは集約的な送信の問題を調査するには、このワークフローを使用してください。すべてのインシデントでステップ1から始めてください。

1. キャンバスがアクティブであること（下書き、停止、またはアーカイブされていないこと）を確認します。
2. エントリスケジュール（スケジュールされたウィンドウ、タイムゾーン、アクションベースのトリガー、またはAPIトリガーエントリ）が、ユーザーのエントリが期待されるタイミングと一致していることを確認します。
3. **オーディエンス** > **ユーザー検索**に移動し、プロファイルを開いて**メッセージング履歴**（過去30日間）を選択して、ユーザーのメッセージング記録を確認します。
   - 期待される送信時刻の記録が存在しない場合、問題はメッセージではなくエントリにあります。[ユーザーがキャンバスにエントリしなかった](#user-didnt-enter-the-canvas)に移動してください。
4. キャンバスの**変更ログ**と、ターゲティングに使用されているセグメントの変更ログを確認します。インシデント中にオーディエンス、ステップ、または送信設定が変更されていないことを確認します。
5. [メッセージング診断ダッシュボード]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard)を開いて中止およびドロップの理由を確認し、キャンバス分析ページで集約結果を確認します。
   - 認識できない結果が表示された場合は、診断ドキュメントの[中止の結果]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes)を参照してください。
   - ステップのエントリがゼロ（送信がゼロではなく）の場合は、前のステップタイプ（[アクションパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)、[遅延]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)、[オーディエンスパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)、または[条件分岐]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)）を確認してください。
6. それでも解決しない場合は、キャンバスID、影響を受けたユーザーID、タイムスタンプ（タイムゾーン付き）、メッセージング履歴またはメッセージング診断のスクリーンショットを添えて、30日以内に[Brazeサポート]({{site.baseurl}}/user_guide/administer/personal/braze_support)にお問い合わせください。

起動前に、[テストキャンバスの送信]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases)と[ユーザーパスのプレビュー]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths)を使用して設定を検証してください。

## ユーザーがキャンバスにエントリしなかった {#user-didnt-enter-the-canvas}

**症状：** ユーザーが期待どおりにキャンバスにエントリしなかった、またはトリガーイベントの数と比べてエントリしたユーザーが少ない。

ユーザーは、Brazeがエントリトリガーを評価する前に**ターゲットオーディエンス**に一致している必要があります（[属性変更]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)トリガーを除く）。トリガーだけでは、評価時にユーザーがオーディエンスに含まれていなかった場合、エントリは保証されません。

再適格性と再エントリは、[エントリコントロールの選択]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls)における別々のコントロールです。

- **再適格性：** ユーザーがキャンバスを退出した後に再びエントリできるかどうかを決定します（時間ウィンドウと**ユーザーにキャンバスへの再エントリを許可する**設定）。
- **再エントリ：** 現在キャンバス内にいるユーザーが同時並行のパスにエントリできるかどうかを決定します。

ユーザーは再適格であっても、まだキャンバス内にいるためにブロックされることがあります。また、退出済みであっても再適格性ウィンドウの範囲外にいる場合もあります。ユーザーがキャンバスに再エントリしない場合は、両方の設定を確認してください。

以下を確認してください。

- **エントリスケジュールとタイムゾーン：** キャンバスが有効で、ユーザーが[エントリウィンドウ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule)中にトリガーを実行したことを確認します。
- **評価時のターゲットオーディエンス：** セグメントとフィルターの変更ログを確認します。[ユーザー検索]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)は、一部のフィルタータイプ（例：文字列形式の日付属性）で偽陽性を表示する場合があります。
- **エントリ上限：** [最大エントリ数]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls)またはオーディエンス上限に達している可能性があります。
- **グローバルコントロールグループ：** [グローバルコントロールグループ]({{site.baseurl}}/user_guide/audience/global_control_group)内のユーザーは、メッセージングキャンバスにエントリしません。
- **キャンバスコントロールグループ：** エントリ時にキャンバスのコントロールグループに割り当てられたユーザーは、バリアントメッセージを受信しません。バリアントの割り当てはエントリ時に行われ、セグメントフィルターを通じて行われるわけではありません。[キャンバス分析の不一致](#canvas-analytics-mismatches)を参照してください。
- **退出条件：** ユーザーがエントリの前または途中で[退出条件]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria)に一致した可能性があります。エントリと退出で同じイベントを使用している場合は、[エントリ条件と退出条件の一致]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/matching_entry_and_exit_criteria)を参照してください。
- **APIトリガーによるエントリ：** ユーザーが[`/canvas/trigger/send`エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)で追加されたことを確認します。キャンバスエントリフィルターで[セグメントを作成]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)し、[`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)でユーザーをエクスポートできます。

### トリガーイベント数がキャンバスのエントリ数より多い {#trigger-event-count-is-higher-than-canvas-entries}

**症状：** トリガーイベントのボリュームがキャンバスのエントリ数より多い。

Brazeは同じ瞬間に発生した複数のエントリ試行を重複排除するため、トリガーイベントよりもキャンバスのエントリ数が少なくなる場合があります。複数のエントリをテストする場合は、トリガーイベントの間隔を少なくとも1秒空けてください。

ユーザーが1秒以内に同じトリガーを複数回実行した場合、Brazeは1回のエントリのみを処理します。再エントリまたは再適格性ルールが適用されている場合は、メッセージング診断で**ユーザーが再適格でない**などの結果を確認してください。

{% details 夏時間と毎日スケジュールされたキャンバス %}

夏時間（DST）の切り替え日には、毎日スケジュールされたキャンバスが通常より最大1時間早くまたは遅く実行される場合があります。エントリ条件がスケジュールされたエントリ時刻の前後1時間以内のタイムスタンプを持つカスタム属性やイベントに依存している場合、属性やイベントがまだ記録されていないため、DSTの日にユーザーが適格にならない可能性があります。

例えば、通常ユーザーがキャンバスのタイムゾーンで午後3時にカスタム属性の更新を受け取り、キャンバスが同じタイムゾーンで毎日午後3時30分に実行されるとします。春の時計を進めるDSTの日には、キャンバスがその属性更新に対して通常より最大1時間早くユーザーを評価する場合があり、属性が記録される前に評価が行われます。再適格性がオフになっている場合、以前の日にエントリしたユーザーは再エントリできず、その日のエントリがゼロになります。

これを避けるために、カスタム属性やイベントの更新がキャンバスのスケジュールされたエントリ時刻の1時間以上前に行われるようにしてください。

{% enddetails %}

## ユーザーがキャンバスのメッセージやステップを受信しなかった {#user-didnt-receive-a-canvas-message-or-step}

**症状：** ユーザーがキャンバスにエントリしたが、期待されるメッセージやステップを受け取らなかった。

ユーザーの[**メッセージ履歴**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab)でキャンバスのステップとタイムスタンプを確認してください。記録が存在しない場合は、[ユーザーがキャンバスにエントリしなかった](#user-didnt-enter-the-canvas)に戻ってください。

次に、トリガーまたはステップタイプに応じて以下を確認してください。

- **カスタムイベントまたは購入トリガー：** イベントが**Analytics** > **カスタムイベントレポート**（購入の場合は**Revenue**）に表示されることを確認します。イベントのタイムスタンプを、キャンバスが公開された時刻およびステップに設定されたスケジュール遅延と比較してください。
- **APIトリガーエントリ：** [ユーザーがキャンバスにエントリしなかった](#user-didnt-enter-the-canvas)で説明されているように、キャンバスのセグメントフィルターとエクスポートでエントリを確認します。
- **アクションパスまたはメッセージステップのトリガー：** ユーザーが前提条件となるイベントを実行したこと、および[イベントプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#event-properties)がステップで利用可能であることを確認します。
- **アプリ内メッセージステップ：** アプリ内メッセージは、ユーザーがステップにエントリした後の次のセッション開始時に送信され、SDKイベントからのみ送信されます（REST APIからは送信されません）。[キャンバスのアプリ内メッセージはいつ送信されますか？]({{site.baseurl}}/user_guide/messaging/canvas/faqs#when-are-in-app-messages-in-canvas-sent)（キャンバスFAQ）を参照してください。
- **キャンバスのコントロールグループ：** ユーザーがエントリ時にキャンバスのコントロールグループに割り当てられていないことを確認します。
- **チャネルの適格性と送信設定：** 購読ステータス、プッシュ有効状態、およびステップごとの[送信設定]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings)（例：**購読設定**がオプトイン済みユーザーのみに設定されている場合）を確認します。マルチチャネルのキャンバスで**ターゲットオーディエンス**に単一チャネルのフィルターを追加しないでください。
- **配信バリデーション：** メッセージステップで**メッセージ送信時にオーディエンスを検証する**を有効にしている場合、送信時にフィルターに一致しなくなったユーザーはメッセージを受信しません。[配信バリデーション]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations)を参照してください。
- **サイレント時間、インテリジェントタイミング、フリークエンシーキャップ、およびレート制限：** これらは送信を遅延、抑制、または中止する可能性があります。サイレント時間による中止の後も、ユーザーはキャンバス内に残る場合があります。
- **競合：** ユーザーが複数のアクションを同時にトリガーした場合は、[競合]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions)を参照してください。

{% alert important %}
キャンバスのメッセージステップが送信を中止した場合でも、ユーザーは次のステップに進みます。キャンバスは中止時に進行するため、後続の遅延ステップやアクションパスステップが永久にブロックされることはありません。[ユーザーの進行方法]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance)および[中止の結果]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes)を参照してください。
{% endalert %}

ステップレベルのフィルター、ブランチ間の競合、およびアプリ内メッセージの分岐動作については、[キャンバスフローで開始する — トラブルシューティング]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#troubleshooting)および[キャンバスFAQ]({{site.baseurl}}/user_guide/messaging/canvas/faqs#messages-and-delivery)を参照してください。

{% alert important %}
アクションベースのキャンバスが予想より早くメッセージを送信する場合は、カスタムイベントのタイムスタンプが過去の日時ではなく現在の時刻を使用していることを確認してください。Brazeはイベントと一緒に送信されたタイムスタンプから遅延を評価します。[アクションベースの配信]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule)を参照してください。
{% endalert %}

## キャンバスのエントリが少ない、またはゼロ {#low-or-zero-canvas-entries}

**症状：** キャンバスに誰もエントリしない、または予想より少ないユーザーしかエントリしない。

[キャンバスフロー起動チェックリスト]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#launch-checklist)から始めて、以下を確認してください。

- キャンバスがアクティブで、現在の時刻がスケジュールされたエントリウィンドウ内にあること。
- [エントリ設定]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls)（再適格性、最大エントリ数、エントリ上限）が、エントリを想定しているユーザーを許可していること。
- ターゲットオーディエンスとセグメントフィルターが、起動後も想定しているユーザーと一致していること。
- グローバルおよびキャンバスのコントロールグループの割合が、各パスにエントリするユーザーとメッセージを受信するユーザーの比率を正しく示していること。
- ワークスペースのレート制限やエントリキューにより、ユーザーが適格になってからエントリまたはステップに進むまでに遅延が発生することが想定されていること。

単一のユーザーについては、[標準的な調査パス]({{site.baseurl}}/user_guide/administer/personal/braze_support)に従ってください。夏時間（DST）関連のエントリゼロについては、[ユーザーがキャンバスにエントリしなかった](#user-didnt-enter-the-canvas)の折りたたみセクションを参照してください。

## 送信数が予想より少ない {#lower-sends-than-expected}

**症状：** キャンバスステップの推定オーディエンスに対して、送信数または配信数が少ない。

一般的な原因として、送信時のオーディエンス再評価、チャネルの適格性、コントロールグループ、サイレント時間、インテリジェントタイミング、レート制限、アプリ内メッセージの配信動作（アプリ内メッセージでは_送信数_がゼロでインプレッションがあるのは想定どおりの動作です）が挙げられます。

メッセージステップに多くのユーザーがエントリしたにもかかわらず送信数が少ない場合は、Liquid の `abort_message()` が送信をキャンセルしていないか確認してください。メッセージアクティビティログの確認、属性の欠落、テスト送信については、[高い中断率のトラブルシューティング]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages#troubleshooting-high-abort-rates)を参照してください。

詳細なリストについては、キャンバスFAQの[推定オーディエンスサイズより送信数が少ないのはなぜですか？]({{site.baseurl}}/user_guide/messaging/canvas/faqs#why-are-sends-lower-than-the-estimated-audience-size)、およびキャンペーン向けの[推定オーディエンスサイズより送信数が少ないのはなぜですか？]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size)を参照してください。

[メッセージング診断ダッシュボード]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard)を使用して、ステップレベルでの中断理由やドロップ理由を確認できます。

## キャンバス分析の不一致 {#canvas-analytics-mismatches}

**症状：** キャンバス分析が正しく表示されない（コントロールグループの分割、コンバージョン、送信数がゼロなど）。

コントロールグループとバリアントの割り当ては、セグメントフィルターではなく、ビルダーで設定したパーセンテージに基づいてキャンバスエントリ時に行われます。特定のチャネルを受信できないユーザーもバリアントにエントリする場合があります。**ターゲットオーディエンス**をチャネルフィルターで絞り込むのではなく、ステップごとの[送信設定]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings)を使用して、各メッセージタイプを受信するユーザーを制限してください。

キャンバスのコントロールグループと[グローバルコントロールグループ]({{site.baseurl}}/user_guide/audience/global_control_group)を区別してください。フィルターの定義については、キャンバスFAQの[「キャンバスバリアントに入っていない」と「キャンバスのコントロールグループに含まれていない」の違いは何ですか？]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group)を参照してください。

{% details バリアントの送信数がバリアントのパーセンテージより少なくなる理由 %}

次のシナリオを想像してみてください。

- キャンバスに1つのバリアントと1つのコントロールグループがあります。
- バリアントの最初のステップはプッシュ通知です。
- ユーザーの90%がバリアントに、10%がコントロールグループにエントリするよう選択されました。

![90%のバリアントと10%のコントロールグループを持つキャンバスの例。]({% image_buster /assets/img_archive/trouble15.png %})

このシナリオでは、キャンバスにエントリしたユーザーの90%がバリアントにエントリします。

アクティブユーザーセグメントを確認すると、29.8kのユーザーが含まれていますが、そのうちプッシュが有効なのは64%のみであることがわかります。

![「プッシュが有効」フィルターが「true」に設定され、推定ユーザー数が29.8kのセグメント。]({% image_buster /assets/img_archive/trouble16.png %})

つまり、ユーザーの90%がバリアントにエントリするよう指定した場合でも、そのすべてのユーザーがプッシュ通知を受信できるわけではありません。プッシュを受信できないユーザーも関係なくバリアントにエントリします。送信数はエントリ時のバリアント割り当てではなく、ステップ時のチャネル適格性を反映します。

{% enddetails %}

### 日付範囲フィルターで予期しない数値が表示される {#date-range-filtering-can-show-unexpected-numbers}

**症状：** キャンバスまたはステップの分析で、エントリ数よりはるかに多い送信数や、エントリしたユーザー数よりも多いステップ退出ユーザー数など、予期しない数値や起こりえない数値が表示される。

これは、キャンバス分析ページ上部の日付範囲カレンダーフィルターを使用した場合に発生することがあります。一部のユーザーアクションを除外する日付範囲を選択すると、表示される指標が各ユーザーのジャーニーの一部のみを示す場合があります。

例：
- 日付範囲がほとんどのユーザーのエントリ後から開始され、メッセージ受信時を含む場合、100件のエントリに対して8,000件の送信が表示されることがあります。
- 日付範囲が退出のみをキャプチャし、それ以前のエントリを含まない場合、前のステップにエントリしたユーザー数よりも多くのユーザーが次のステップに移動しているように表示されることがあります。

これを解決するには、キャンバスが開始された日から現在までのすべての日付を含むように日付範囲を調整するか、必要な指標に関連する期間全体をカバーする範囲を選択してください。

コンバージョン率の定義とステップレベルの分析については、キャンバスFAQの[分析とコンバージョン]({{site.baseurl}}/user_guide/messaging/canvas/faqs#analytics-and-conversions)を参照してください。

## エディターと保存の問題 {#editor-and-save-issues}

**症状：** キャンバスエディターが読み込まれない、フリーズする、または変更が保存されない。

| 症状 | 最も可能性の高い原因 |
| --- | --- |
| 保存ボタンがエラーなしで無限に回転する | キャンバスオーディエンスまたはステップフィルターに空または不完全なカスタム属性フィルターがある — フィルターを削除するか、有効な属性を選択してください |
| 編集中に「Request Timed Out」エラーが発生する | ブラウザー拡張機能の干渉、広告ブロッカー、または古いセッション — シークレットウィンドウまたは別のブラウザーを試してください |
| バリアントをアーカイブした後に保存できない | アーカイブされたバリアントが下流でまだ参照されている — ステップの接続を確認し、バリアントを復元または置き換えてください |
{: .reset-td-br-1 .reset-td-br-2 aria-label="エディターの症状" }

大規模または複雑なキャンバスでエディターがフリーズする場合は、以下を試してください。

- ブラウザーのキャッシュとCookieをクリアしてから、ページを再読み込みしてください。企業の広告ブロッカーやブラウザー拡張機能がBrazeプラットフォームに干渉する場合があります。
- キャンバスのズームコントロールを使用して、表示を25%または10%に縮小し、ブラウザーがレンダリングするUIの量を減らしてください。
- 別のWebブラウザーを試してください。

キャンバスが読み込まれず進行しない場合は、以前のバージョンが正しく保存されておらず、無効なステップが含まれている可能性があります。ダッシュボードからキャンバスを複製してください。問題が解決しない場合は、[サポートチケット]({{site.baseurl}}/user_guide/administer/personal/braze_support)を送信してください。

「Request Timed Out」のサポートチケットには、画面録画、タイムスタンプとタイムゾーン、ブラウザーとバージョン、再現手順、およびオプションでブラウザーの開発者ツールからのHARログを含めてください。詳しくは、キャンバスFAQの[「Request Timed Out」エラーのサポートチケットを送信する際に何を含めるべきですか？]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error)を参照してください。

{% multi_lang_include audience/segments.md section='キャンバス variant archived segment' %}

## キャンバス停止時の動作 {#stopped-canvas-behavior}

**症状：**キャンバスを停止したのに、ユーザーがまだメッセージを受信しています。

キャンバスを停止すると、ユーザーはエントリできなくなり、キャンバスフローからそれ以上のメッセージは送信されません。メールサービスプロバイダーにすでに引き渡されたメール送信は取り消すことができません。

遅延ステップまたはアクションパスステップで待機中のユーザーは、キャンバスを停止しても自動的にジャーニーから削除されません。スケジュールされた送信時刻が過ぎる前にキャンバスを再度有効にした場合、ユーザーは保留中のステップを受信する可能性があります。

詳細については、キャンバスFAQの[キャンバスを停止するとどうなりますか？]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-when-you-stop-a-canvas)を参照してください。

## 「キャンバスの分岐が多すぎます」エラー {#too-many-canvas-branches-error}

**症状：** スケジュールされたキャンバスを起動する際に「Too many キャンバス branches」エラーが表示されます。

このエラーは、ステップの分岐とエントリオーディエンスのサイズの組み合わせにより、メッセージの送信を妨げるクラスターパフォーマンスの問題が発生する可能性がある場合に表示されます。Brazeは、スケジュールされたエントリのキャンバスを起動する際にこのメッセージを表示します。下書きを保存するときには表示されません。

解決するには：

- キャンバス内のステップの分岐を減らします。
- エントリオーディエンスのサイズを縮小します。
- 多数の並列パスの代わりに、[オーディエンスパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)を使用して分岐を統合します。
- キャンバスがオリジナルエディターを使用している場合は、[キャンバスフローに複製]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases)し、キャンバスコンポーネントを使用して再構築します。

変更を加えずにキャンバスを起動する必要があり、キャンバスフローに移行できない場合は、[サポート]({{site.baseurl}}/support_contact)にお問い合わせください。

## サポートへの問い合わせが必要な場合 {#when-to-contact-support}

[標準的な調査パス](#standard-investigation-path)を完了しても問題が解決しない場合は、問題発生から30日以内に[Brazeサポート]({{site.baseurl}}/user_guide/administer/personal/braze_support)にお問い合わせください。

以下の情報を含めてください：

- キャンバスIDと影響を受けたユーザーID（external IDまたはBraze ID）
- タイムゾーン付きのタイムスタンプ
- **Messaging History**または**Messaging Diagnostics**のスクリーンショットまたはエクスポート
- エディターの「Request Timed Out」エラーの場合は、[エディターと保存の問題](#editor-and-save-issues)に記載されている詳細情報