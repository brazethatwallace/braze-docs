---
nav_title: トラブルシューティング
article_title: Canvasのトラブルシューティング
page_order: 7
page_type: reference
description: "標準的な調査パス、症状インデックス、メッセージング履歴やメッセージング診断ダッシュボードへのリンクを使用して、Canvasのエントリ、送信、分析の問題を診断します。"
tool: Canvas
---

# Canvasのトラブルシューティング {#troubleshoot-canvases}

> このページでは、Canvasのエントリ、送信、分析の問題を診断します。定義や詳細については、[Canvas FAQ]({{site.baseurl}}/user_guide/messaging/canvas/faqs)を参照してください。

{% alert note %}
**メッセージング履歴**と**メッセージング診断**のログは、イベントから最大**30日間**利用可能です。特定のインシデントの調査にサポートが必要な場合は、その期間内に[Brazeサポート](#standard-investigation-path)にお問い合わせください。
{% endalert %}

## まずはここから：症状を確認する {#start-here-match-your-symptom}

| 症状 | 参照先 |
| --- | --- |
| ユーザーがCanvasに入らなかった | [ユーザーがCanvasに入らなかった](#user-didnt-enter-the-canvas) |
| ユーザーが入ったがメッセージやステップを受信しなかった | [ユーザーがCanvasのメッセージやステップを受信しなかった](#user-didnt-receive-a-canvas-message-or-step) |
| 誰も入らなかった、または予想より少ないユーザーしか入らなかった | [Canvasエントリが少ない、またはゼロ](#low-or-zero-canvas-entries) |
| 送信数や配信数が推定オーディエンスより少ない | [予想より送信数が少ない](#lower-sends-than-expected) |
| Canvas分析が正しくない（コントロールグループ、コンバージョン、送信数ゼロ） | [Canvas分析の不一致](#canvas-analytics-mismatches) |
| Canvasが保存できない、またはエディターがフリーズする | [エディターと保存の問題](#editor-and-save-issues) |
| Canvasを停止したがメッセージが送信された | [停止したCanvasの動作](#stopped-canvas-behavior) |
| 起動時に「Canvasのブランチが多すぎます」エラーが表示される | [「Canvasのブランチが多すぎます」エラー](#too-many-canvas-branches-error) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvasの症状" }

## 標準的な調査パス {#standard-investigation-path}

このワークフローを使用して、特定のユーザーまたは集計送信の問題を調査します。すべてのインシデントでステップ1から開始してください。

1. Canvasがアクティブであることを確認します（下書き、停止、またはアーカイブ済みでないこと）。
2. エントリスケジュール（スケジュールされた時間枠、タイムゾーン、アクションベースのトリガー、またはAPIトリガーのエントリ）が、ユーザーが入ると予想するタイミングと一致していることを確認します。
3. **オーディエンス** > **ユーザーを検索**に移動し、プロファイルを開いて**メッセージング履歴**（過去30日間）を選択して、ユーザーのメッセージング記録を確認します。
   - 予想される送信時刻のレコードが存在しない場合、問題はメッセージではなくエントリにあります。[ユーザーがCanvasに入らなかった](#user-didnt-enter-the-canvas)に進んでください。
4. Canvasの**変更ログ**と、ターゲティングに使用されているSegmentsの変更ログを確認します。インシデント中にオーディエンス、ステップ、または送信設定が変更されていないことを確認してください。
5. Canvas分析ページで集計結果を確認するには、[メッセージング診断ダッシュボード]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard)を開き、中止およびドロップの理由を確認します。
   - 認識できない結果が表示された場合は、診断ドキュメントの[中止の結果]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes)を参照してください。
   - ステップでエントリがゼロ（送信数ゼロではなく）の場合は、前のステップタイプ（[アクションパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)、[遅延]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)、[オーディエンスパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)、または[条件分岐]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)）を確認してください。
6. それでも解決しない場合は、Canvas ID、影響を受けたユーザーID、タイムスタンプ（タイムゾーン付き）、メッセージング履歴またはメッセージング診断のスクリーンショットを添えて、30日以内に[Brazeサポート]({{site.baseurl}}/braze_support)にお問い合わせください。

起動前に、[テストCanvasの送信]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases)と[ユーザーパスのプレビュー]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths)を使用してセットアップを検証してください。

## ユーザーがCanvasに入らなかった {#user-didnt-enter-the-canvas}

**症状：** ユーザーが予想したタイミングでCanvasに入らなかった、またはトリガーイベントが示すよりも少ないユーザーしか入らなかった。

ユーザーは、Brazeがエントリトリガーを評価する前に**ターゲットオーディエンス**に一致している必要があります（[属性の変更]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)トリガーを除く）。トリガーだけでは、評価時にユーザーがオーディエンスに含まれていなければエントリは保証されません。

再適格性と再エントリは、[エントリコントロールの選択]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls)で別々のコントロールです。

- **再適格性：** ユーザーがCanvasを退出した後に再度入ることが許可されるかどうかを決定します（時間枠と**ユーザーのCanvas再エントリを許可**設定）。
- **再エントリ：** 現在Canvas内にいるユーザーが同時に別のパスに入ることができるかどうかを決定します。

ユーザーは再適格であっても、まだCanvas内にいるためにブロックされることがあります。また、退出していても再適格性の時間枠外である場合もあります。ユーザーがCanvasに再エントリしない場合は、両方の設定を確認してください。

以下を確認してください。

- **エントリスケジュールとタイムゾーン：** Canvasがライブであり、ユーザーが[エントリ時間枠]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule)中にトリガーを実行したことを確認します。
- **評価時のターゲットオーディエンス：** Segmentとフィルターの変更ログを確認します。[ユーザー検索]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)は、一部のフィルタータイプ（文字列形式の日付属性など）で偽陽性を示すことがあります。
- **エントリキャップ：** [最大エントリ数]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls)またはオーディエンスキャップに達している可能性があります。
- **グローバルコントロールグループ：** [グローバルコントロールグループ]({{site.baseurl}}/user_guide/audience/global_control_group)のユーザーはメッセージングCanvasesに入りません。
- **Canvasコントロールグループ：** エントリ時にCanvasコントロールグループに割り当てられたユーザーは、バリアントメッセージを受信しません。バリアントの割り当てはエントリ時に行われ、Segmentフィルターを通じて行われるわけではありません。[Canvas分析の不一致](#canvas-analytics-mismatches)を参照してください。
- **退出条件：** ユーザーがエントリ前またはエントリ中に[退出条件]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria)に一致した可能性があります。エントリと退出が同じイベントを使用する場合は、[エントリ条件と退出条件の一致]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/matching_entry_and_exit_criteria)を参照してください。
- **APIトリガーのエントリ：** ユーザーが[`/canvas/trigger/send`エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)で追加されたことを確認します。Canvasエントリフィルターで[Segmentを作成]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)し、[`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)でユーザーをエクスポートできます。

### トリガーイベント数がCanvasエントリより多い {#trigger-event-count-is-higher-than-canvas-entries}

**症状：** トリガーイベントのボリュームがCanvasエントリ数より多い。

Brazeは同じ瞬間に発生した複数のエントリ試行を重複排除するため、トリガーイベントよりもCanvasエントリが少なくなることがあります。複数のエントリをテストする場合は、トリガーイベントを少なくとも1秒間隔で実行してください。

ユーザーが1秒以内に同じトリガーを複数回実行した場合、Brazeは1つのエントリのみを処理します。再エントリまたは再適格性ルールが適用される場合は、メッセージング診断で**ユーザーが再適格でない**などの結果を確認してください。

{% details 夏時間と毎日スケジュールされたCanvas %}

夏時間（DST）の切り替え日には、毎日スケジュールされたCanvasが通常より最大1時間早くまたは遅く実行されることがあります。エントリ条件がカスタム属性やタイムスタンプ付きのイベントに依存しており、それがスケジュールされたエントリ時刻の1時間以内に該当する場合、属性やイベントがまだ記録されていないため、DSTの日にユーザーが資格を満たさない可能性があります。

たとえば、ユーザーが通常Canvasのタイムゾーンで午後3時にカスタム属性の更新を受け取り、Canvasが同じタイムゾーンで毎日午後3時30分に実行されるとします。春の時計を進めるDSTの日には、Canvasがその属性更新に対して通常より最大1時間早くユーザーを評価する可能性があり、属性がまだ記録されていない状態で評価されます。再適格性がオフになっている場合、前日までに入ったユーザーは再エントリできず、その日のエントリがゼロになります。

これを回避するには、カスタム属性またはイベントの更新がCanvasのスケジュールされたエントリ時刻の1時間以上前に行われるようにしてください。

{% enddetails %}

## ユーザーがCanvasのメッセージやステップを受信しなかった {#user-didnt-receive-a-canvas-message-or-step}

**症状：** ユーザーがCanvasに入ったが、予想されるメッセージやステップを受信しなかった。

ユーザーの[**メッセージング履歴**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab)でCanvasステップとタイムスタンプを確認してください。レコードが存在しない場合は、[ユーザーがCanvasに入らなかった](#user-didnt-enter-the-canvas)に戻ってください。

次に、トリガーまたはステップタイプ別に以下を確認してください。

- **カスタムイベントまたは購入トリガー：** イベントが**Analytics** > **カスタムイベントレポート**（購入の場合は**収益**）に表示されることを確認します。イベントのタイムスタンプを、Canvasがライブになった時刻およびステップのスケジュールされた遅延と比較してください。
- **APIトリガーのエントリ：** [ユーザーがCanvasに入らなかった](#user-didnt-enter-the-canvas)で説明されているように、CanvasのSegmentフィルターとエクスポートでエントリを確認します。
- **アクションパスまたはメッセージステップのトリガー：** ユーザーが前提条件のイベントを実行し、[イベントプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#event-properties)がステップで利用可能であることを確認します。
- **アプリ内メッセージステップ：** アプリ内メッセージは、ユーザーがステップに入った後の次のセッション開始時に送信され、SDKイベントからのみ送信されます（REST APIからは送信されません）。Canvas FAQの[Canvasのアプリ内メッセージはいつ送信されますか？]({{site.baseurl}}/user_guide/messaging/canvas/faqs#when-are-in-app-messages-in-canvas-sent)を参照してください。
- **Canvasコントロールグループ：** ユーザーがエントリ時にCanvasコントロールグループに割り当てられていないことを確認します。
- **チャネルの適格性と送信設定：** サブスクリプションステータス、プッシュ有効状態、およびステップごとの[送信設定]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings)（たとえば、**サブスクリプション設定**がオプトインユーザーのみに設定されている場合）を確認します。マルチチャネルCanvasesの**ターゲットオーディエンス**に単一チャネルのフィルターを追加しないでください。
- **配信バリデーション：** メッセージステップで**メッセージ送信時にオーディエンスを検証**を有効にしている場合、送信時にフィルターに一致しなくなったユーザーはメッセージを受信しません。[配信バリデーション]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations)を参照してください。
- **サイレント時間帯、インテリジェントタイミング、フリークエンシーキャップ、レート制限：** これらにより、送信が延期、抑制、または中止されることがあります。サイレント時間帯による中止後も、ユーザーはCanvas内に残ることがあります。
- **競合：** ユーザーが複数のアクションを同時にトリガーした場合は、[競合]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions)を参照してください。

{% alert important %}
Canvasのメッセージステップが送信を中止した場合でも、ユーザーは次のステップに進みます。Canvasは中止時に進行するため、後続の遅延やアクションパスのステップが永久にブロックされることはありません。[ユーザーの進行方法]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance)と[中止の結果]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes)を参照してください。
{% endalert %}

ステップレベルのフィルター、ブランチ間の競合、IAMの分岐動作については、[キャンバスフローでの起動 — トラブルシューティング]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#troubleshooting)と[Canvas FAQ]({{site.baseurl}}/user_guide/messaging/canvas/faqs#messages-and-delivery)を参照してください。

{% alert important %}
アクションベースのCanvasが予想より早くメッセージを送信する場合は、カスタムイベントのタイムスタンプが現在の時刻を使用しており、過去の日時ではないことを確認してください。Brazeはイベントとともに送信されたタイムスタンプから遅延を評価します。[アクションベースの配信]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule)を参照してください。
{% endalert %}

## Canvasエントリが少ない、またはゼロ {#low-or-zero-canvas-entries}

**症状：** 誰も入らなかった、または予想より少ないユーザーしかCanvasに入らなかった。

[キャンバスフローでの起動チェックリスト]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#launch-checklist)から始めて、以下を確認してください。

- Canvasがアクティブであり、現在の時刻がスケジュールされたエントリ時間枠内であること。
- [エントリ設定]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls)（再適格性、最大エントリ数、エントリキャップ）が、予想するユーザーのエントリを許可していること。
- ターゲットオーディエンスとSegmentフィルターが、起動後も予想するユーザーに一致していること。
- グローバルおよびCanvasコントロールグループの割合が、各パスに入るユーザーとメッセージを受信するユーザーの割合を示していること。
- ワークスペースのレート制限またはエントリキューにより、ユーザーが資格を満たしてからエントリまたはステップに進むまでの間に遅延が発生する可能性があること。

単一のユーザーについては、[標準的な調査パス]({{site.baseurl}}/braze_support)に従ってください。DSTに関連するエントリゼロについては、[ユーザーがCanvasに入らなかった](#user-didnt-enter-the-canvas)の折りたたみセクションを参照してください。

## 予想より送信数が少ない {#lower-sends-than-expected}

**症状：** Canvasステップの推定オーディエンスに対して、送信数や配信数が少ない。

一般的な原因には、送信時のオーディエンス再評価、チャネルの適格性、コントロールグループ、サイレント時間帯、インテリジェントタイミング、レート制限、アプリ内メッセージの配信動作（アプリ内メッセージではインプレッションがあっても*送信数*がゼロになるのは想定どおりの動作です）が含まれます。

詳細なリストについては、Canvas FAQの[推定オーディエンスサイズより送信数が少ないのはなぜですか？]({{site.baseurl}}/user_guide/messaging/canvas/faqs#why-are-sends-lower-than-the-estimated-audience-size)と、Campaignsの[推定オーディエンスサイズより送信数が少ないのはなぜですか？]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size)を参照してください。

[メッセージング診断ダッシュボード]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard)を使用して、ステップレベルの中止およびドロップの理由を確認してください。

## Canvas分析の不一致 {#canvas-analytics-mismatches}

**症状：** Canvas分析が正しくない（コントロールグループの分割、コンバージョン、または送信数ゼロ）。

コントロールグループとバリアントの割り当ては、Segmentフィルターではなく、ビルダーで設定した割合に基づいてCanvasのエントリ時に行われます。特定のチャネルを受信できないユーザーでもバリアントに入ることがあります。各メッセージタイプの受信者を制限するには、**ターゲットオーディエンス**をチャネルフィルターで絞り込むのではなく、ステップごとの[送信設定]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings)を使用してください。

Canvasコントロールグループと[グローバルコントロールグループ]({{site.baseurl}}/user_guide/audience/global_control_group)を区別してください。フィルターの定義については、Canvas FAQの[「Canvasバリアントに入っていない」と「Canvasコントロールグループに含まれていない」の違いは何ですか？]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group)を参照してください。

{% details バリアントの送信数がバリアントの割合より少なくなる理由 %}

以下のシナリオを想像してみましょう。

- Canvasには単一のバリアントとコントロールグループがあります。
- バリアントの最初のステップはプッシュ通知です。
- 90%のユーザーがバリアントに入るように選択され、10%がコントロールグループに入るように選択されました。

![90%のバリアントと10%のコントロールグループを持つCanvasの例。]({% image_buster /assets/img_archive/trouble15.png %})

このシナリオでは、Canvasに入るユーザーの90%がバリアントに入ります。

アクティブユーザーのSegmentを確認すると、29.8kのユーザーが含まれているにもかかわらず、プッシュが有効なのはそのうち64%のみであることがわかります。

![「プッシュ有効」フィルターが「true」に設定され、推定ユーザー数が29.8kのSegment。]({% image_buster /assets/img_archive/trouble16.png %})

つまり、90%のユーザーがバリアントに入るように指定しても、それらのユーザー全員がプッシュ通知を受信できるわけではありません。プッシュを受信できないユーザーもバリアントには入ります。送信数はエントリ時のバリアント割り当てではなく、ステップでのチャネル適格性を反映しています。

{% enddetails %}

コンバージョン率の定義とステップレベルの分析については、Canvas FAQの[分析とコンバージョン]({{site.baseurl}}/user_guide/messaging/canvas/faqs#analytics-and-conversions)を参照してください。

## エディターと保存の問題 {#editor-and-save-issues}

**症状：** Canvasエディターが読み込まれない、フリーズする、または変更が保存できない。

| 症状 | 最も可能性の高い原因 |
| --- | --- |
| 保存ボタンがエラーなしで無限に回転する | Canvasオーディエンスまたはステップフィルターに空または不完全なカスタム属性フィルターがある — フィルターを削除するか、有効な属性を選択してください |
| 編集中に「リクエストタイムアウト」エラーが表示される | ブラウザ拡張機能の干渉、広告ブロッカー、またはセッションの期限切れ — シークレットウィンドウまたは別のブラウザを試してください |
| バリエーションをアーカイブした後に保存できない | アーカイブされたバリエーションがダウンストリームでまだ参照されている — ステップの接続を確認し、バリエーションを復元または置き換えてください |
{: .reset-td-br-1 .reset-td-br-2 aria-label="エディターの症状" }

大規模または複雑なCanvasでエディターがフリーズする場合は、以下を試してください。

- ブラウザのキャッシュとCookieをクリアしてから、ページを再読み込みしてください。会社の広告ブロッカーやブラウザ拡張機能がBrazeプラットフォームに干渉する可能性があります。
- Canvasのズームコントロールを使用して、表示を25%または10%に縮小し、ブラウザがレンダリングするUIの量を減らしてください。
- 別のWebブラウザを試してください。

Canvasが読み込まれず進行しない場合、以前のバージョンが正しく保存されておらず、無効なステップが含まれている可能性があります。ダッシュボードからCanvasを複製してください。問題が解決しない場合は、[サポートチケット]({{site.baseurl}}/braze_support)を開いてください。

「リクエストタイムアウト」のサポートチケットには、画面録画、タイムスタンプとタイムゾーン、ブラウザとバージョン、再現手順、およびオプションでブラウザの開発者ツールからのHARログを含めてください。Canvas FAQの[「リクエストタイムアウト」エラーのサポートチケットを送信する際に何を含めるべきですか？]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error)を参照してください。

## 停止したCanvasの動作 {#stopped-canvas-behavior}

**症状：** Canvasを停止したが、ユーザーがまだメッセージを受信した。

Canvasを停止すると、ユーザーはエントリできなくなり、Canvasフローからそれ以上のメッセージは送信されません。メールサービスプロバイダーにすでに引き渡されたメール送信は取り消すことができません。

遅延またはアクションパスのステップで待機しているユーザーは、Canvasを停止しても自動的にジャーニーから削除されません。スケジュールされた送信時刻が経過する前にCanvasを再有効化すると、保留中のステップを受信する可能性があります。

詳細については、Canvas FAQの[Canvasを停止するとどうなりますか？]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-when-you-stop-a-canvas)を参照してください。

## 「Canvasのブランチが多すぎます」エラー {#too-many-canvas-branches-error}

**症状：** スケジュールされたCanvasを起動する際に「Canvasのブランチが多すぎます」エラーが表示される。

このエラーは、ステップの分岐とエントリオーディエンスのサイズの組み合わせにより、クラスターのパフォーマンスに問題が生じ、メッセージの送信が妨げられる可能性がある場合に表示されます。Brazeはこのメッセージを、スケジュールされたエントリのCanvasを起動するときに表示します。下書きを保存するときには表示されません。

これを解決するには：

- Canvas内のステップの分岐を減らします。
- エントリオーディエンスのサイズを縮小します。
- 多数の並列パスの代わりに、[オーディエンスパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)を使用して分岐を統合します。
- Canvasがオリジナルエディターを使用している場合は、[キャンバスフローに複製]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases)して、Canvasコンポーネントで再構築します。

変更せずにCanvasを起動する必要があり、キャンバスフローに移行できない場合は、[サポート]({{site.baseurl}}/support_contact)にお問い合わせください。

## サポートに問い合わせるタイミング {#when-to-contact-support}

[標準的な調査パス](#standard-investigation-path)を完了してもまだサポートが必要な場合は、問題発生から30日以内に[Brazeサポート]({{site.baseurl}}/braze_support)にお問い合わせください。

以下を含めてください。

- Canvas IDと影響を受けたユーザーID（external IDまたはBraze ID）
- タイムスタンプとタイムゾーン
- **メッセージング履歴**または**メッセージング診断**のスクリーンショットまたはエクスポート
- エディターの「リクエストタイムアウト」エラーの場合は、[エディターと保存の問題](#editor-and-save-issues)に記載されている詳細