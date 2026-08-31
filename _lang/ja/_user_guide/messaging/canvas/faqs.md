---
nav_title: FAQ
article_title: キャンバス FAQ
page_order: 8
alias: "/canvas_v2_101/"
description: "この記事では、キャンバスに関するよくある質問への回答を提供します。"
tool: Canvas
toc_headers: h2

---

# よくある質問 {#frequently-asked-questions}

> この記事では、キャンバスに関するよくある質問への回答を提供します。

## キャンバスの構築と編集 {#building-and-editing-canvas}

### キャンバスに含められるステップ数は？ {#how-many-steps-i-can-include-in-a-canvas}

キャンバスには最大200ステップを追加できます。

### キャンバスエントリプロパティにサイズ制限はありますか？ {#are-there-size-limits-for-canvas-entry-properties}

はい。[キャンバスコンテキストオブジェクト]({{site.baseurl}}/api/objects_filters/context_object)（キャンバスエントリプロパティ）の最大サイズは50&nbsp;KBです。ペイロードはその制限内でできるだけ小さく保ってください。キャンバスでのエントリプロパティとイベントプロパティの動作については、[コンテキストとイベントプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)を参照してください。

### 「Too many キャンバス branches」エラーが表示されるのはなぜですか？ {#why-do-i-see-a-too-many-canvas-branches-error}

このエラーは、ステップの分岐とエントリオーディエンスサイズの組み合わせにより、クラスターのパフォーマンスに問題が生じ、メッセージ送信が妨げられる可能性がある場合に表示されます。解決手順（[オーディエンスパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)の使用、分岐やオーディエンスサイズの削減、キャンバスフローでの再構築など）については、[「Too many キャンバス branches」エラー]({{site.baseurl}}/user_guide/messaging/canvas/troubleshooting#too-many-canvas-branches-error)を参照してください。

### キャンバスで再エントリ有効時にインテリジェントセレクションを使用できますか？ {#can-i-use-intelligent-selection-with-re-eligibility-in-a-canvas}

はい。キャンバスでは再エントリが有効な場合でも[インテリジェントセレクション]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection)を使用できますが、キャンペーンではインテリジェントセレクションを有効にするために24時間以上の再エントリウィンドウが必要です。Brazeは再エントリ時に同じバリアントになることを保証できません。配分は時間の経過とともに変化するためです。

### コンポーネントとステップの違いは何ですか？ {#whats-the-difference-between-a-component-and-a-step}

[コンポーネント]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about)は、キャンバスの効果を判断するために使用できるキャンバスの個々の部品です。コンポーネントには、ユーザージャーニーの分岐、ディレイの追加、複数のキャンバスパスのテストなどのアクションを含めることができます。キャンバスのステップとは、キャンバスのブランチにおけるパーソナライズされたユーザージャーニーを指します。つまり、キャンバスはユーザージャーニーのステップを構成する個々のコンポーネントで成り立っています。

### 切断されたステップがあるキャンバスをローンチできますか？ {#can-i-launch-a-canvas-with-disconnected-steps}

はい。ローンチ後に切断されたステップを含むキャンバスを保存することもできます。

### 切断されたステップに到達したユーザーはどうなりますか？ {#where-do-users-go-when-theyve-reached-a-disconnected-step}

ユーザーがキャンバスワークフローの切断されたステップにいる場合、後続のステップがあればそのステップに進みます。ステップの設定に基づいてユーザーの進み方が決まります。これは、ステップをキャンバスの残りの部分に直接接続しなくてもユーザーがステップに変更を加えられるようにするための仕様です。また、すぐに本番環境に反映する前にテストを行う余地が生まれ、実質的に下書きの保存が可能になります。

ステップを切断する前に、そのキャンバスステップで待機中のユーザーがいないか分析ビューを確認することをお勧めします。

### バリアントが1つで複数のブランチを持つキャンバスで、オーディエンスと送信時刻が同一の場合はどうなりますか？ {#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches}

各ステップに対してジョブがキューに入れられます。これらはほぼ同時に実行され、いずれか1つが「優先」されます。実際には、ある程度均等に分散される可能性がありますが、最初に作成されたステップに若干偏る傾向があります。

さらに、その分布がどのようになるかについて保証はできません。均等な分割を行いたい場合は、[ランダムバケット番号]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers)フィルターを追加してください。

### キャンバスのオーディエンスはどのように評価されますか？ {#how-are-canvas-audiences-evaluated}

デフォルトでは、キャンバスのフルステップのフィルターとセグメントは送信時に評価されます。条件分岐ステップは、前のステップを受信した直後（またはディレイの前）に評価を行います。

### 例外イベントはいつトリガーされますか？ {#when-does-an-exception-event-trigger}

例外イベントは、ユーザーが関連するキャンバスコンポーネントの受信を待っている間にのみトリガーされます。ユーザーが事前にアクションを実行した場合、例外イベントはトリガーされません。特定のイベントを事前に実行したユーザーを除外したい場合は、代わりに[フィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)を使用してください。

### キャンバスの編集は、すでにキャンバス内にいるユーザーにどのような影響を与えますか？ {#how-does-editing-a-canvas-affect-users-already-in-the-canvas}

マルチステップキャンバスの一部のステップを編集した場合、すでにオーディエンスに含まれているがまだそのステップを受信していないユーザーは、更新されたバージョンのメッセージを受け取ります。これは、まだそのステップの評価が行われていない場合にのみ発生します。

ローンチ後に編集できる内容の詳細については、[ローンチ後のキャンバスの変更]({{site.baseurl}}/post-launch_edits)を参照してください。

### キャンバスを停止するとどうなりますか？ {#what-happens-when-you-stop-a-canvas}

キャンバスを停止すると、以下が適用されます。

- ユーザーはキャンバスにエントリできなくなります。
- フロー内のユーザーの位置に関係なく、それ以上メッセージは送信されません。
- **例外：**メールを含むキャンバスは即座に停止しません。送信リクエストがSendGridに送られた後は、ユーザーへの配信を阻止することはできません。

### ユーザーライフサイクルごとに1つのキャンバスを構築すべきですか、それとも別々のキャンバスを構築すべきですか？ {#should-i-build-one-canvas-or-separate-canvases-per-user-lifecycle}

キャンバスで達成したい内容に応じて、ユーザージャーニーの構築方法にはさまざまなアプローチが必要になる場合があります。キャンバスの柔軟性により、ユーザーライフサイクルのあらゆるステージに対応したユーザージャーニーをマッピングできます。効果的なユーザージャーニーを作成するための合理的なアプローチの例については、[Brazeキャンバステンプレート]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates)をご覧ください。

## メッセージと配信 {#messages-and-delivery}

### キャンバスのアプリ内メッセージはいつ送信されますか？ {#when-are-in-app-messages-in-canvas-sent}

アプリ内メッセージは次のセッション開始時に送信されます。つまり、キャンバスが停止される前にユーザーがキャンバスステップに入った場合、アプリ内メッセージがまだ有効期限切れになっていなければ、次のセッション開始時にそのアプリ内メッセージを受信します。

キャンバスが停止される前にユーザーがセッションを開始したものの、アプリ内メッセージがすぐには表示されないケースもあります。これは、アプリ内メッセージがカスタムイベントでトリガーされる場合や、遅延が設定されている場合に発生する可能性があります。そのため、キャンバスが停止された後にユーザーがアプリ内メッセージのインプレッションを記録し、アプリ内メッセージを「受信」することがあり得ます。ただし、ユーザーはキャンバスが停止される前にセッションを開始している必要がありますが、キャンバスステップを受信した**後**でなければなりません。

{% alert note %}
キャンバスを停止しても、メッセージの受信を待っているユーザーがユーザージャーニーから退出することはありません。キャンバスを再度有効にした場合、ユーザーがまだメッセージを待っていれば、そのメッセージを受信します（ただし、メッセージが送信されるべき時間がすでに過ぎている場合は受信しません）。
{% endalert %}

### キャンバスでインプレッションが記録されているのに送信数がゼロと表示されるのはなぜですか？ {#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged}

アプリ内メッセージステップを含むキャンバスで*送信されたメッセージ*が常にゼロの場合、これはアプリ内メッセージの配信が他のメッセージングチャネルとは異なる仕組みで動作するためです。

アプリ内メッセージは、Brazeから「プッシュ」されるのではなく、SDKによって「プル」されます。対象となるユーザーのアプリ内メッセージは、セッション開始時に自動的に配信され、表示されるまでトリガーイベントを「待機」します。対象ユーザーがセッションを開始した際にメッセージを受信するため、Brazeはこれを送信イベントとして報告しません。ユーザーがトリガーイベントを実行すると、メッセージが表示され、Brazeはインプレッションを記録し、ユーザープロファイル上でキャンバスステップ（またはキャンペーン）を受信済みとしてマークします。その結果、アプリ内メッセージの*送信数*の合計はゼロになります。

### 長い遅延やブランチの後にユーザーがアプリ内メッセージを受信しなかったのはなぜですか？ {#why-didnt-users-receive-my-in-app-message-after-a-long-delay-or-branch}

上流の[遅延]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)ステップとオーディエンスチェックが完了した後、ユーザーがアプリ内メッセージの対象になるのはメッセージステップに到達したときのみです。メッセージの有効期限がカレンダー日付で設定されている場合、または**ステップが利用可能になってからの期間**が短いウィンドウに設定されている場合、遅いブランチにいるユーザーは有効期限が切れた後に到着し、メッセージを見ることがない可能性があります。有効期限は、最も長い現実的なパス遅延に合わせて調整してください。詳細と例については、[アプリ内メッセージの有効期限]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas#in-app-message-expiration)を参照してください。

### 「キャンバス Entry Properties may not be used in In-App Messages.」と表示されるのはなぜですか？ {#why-do-i-see-canvas-entry-properties-may-not-be-used-in-in-app-messages}

このメッセージは、パーソナライゼーションがキャンバスのアプリ内メッセージでは解決できないフィールドを参照している場合に表示されます。[コンテキストとイベントプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)および[メッセージステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)で説明されているように、`context`オブジェクトを使用してください。レガシーのLiquid名前空間`canvas_entry_properties`には`context`とは異なる制約があります。複数のステップにわたって値を保持する必要がある場合は、Brazeチームと[オリジナルキャンバスエディターの永続プロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties)を確認してください。デバイスがアプリ内ペイロードをダウンロードする前にユーザーがキャンバスを退出すると、保存された値はクリアされます。

### キャンバスのドラッグ＆ドロップアプリ内メッセージのボタンクリックはどこで確認できますか？ {#where-can-i-find-button-clicks-for-drag-and-drop-in-app-messages-in-canvas}

ドラッグ＆ドロップアプリ内メッセージのボタンレベルの指標は、キャンバスの概要ではなく、**キャンバスの詳細**内の**メッセージ**ステップの分析カードに表示されます。キャンバスを開き、メッセージステップを選択して、アプリ内エンゲージメントを確認してください。レポートの概念については、[キャンバス分析による測定とテスト]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics)を参照してください。

### 同じキャンバスのメッセージステップや多変量送信で、各バリアントに異なる送信時間をスケジュールできますか？ {#can-i-schedule-different-send-times-for-each-variant-in-the-same-canvas-message-step-or-multivariate-send}

いいえ。同じ多変量設定またはメッセージステップのバリアントは、1つの配信スケジュールを共有します。同じスケジュールされた送信に対して、1つのバリアントを午後6時に、別のバリアントを午後7時に送信するよう割り当てることはできません。

送信をずらしたり、パスごとに異なる時間を使用するには、以下の方法をお試しください。

- メッセージステップの間に遅延ステップを配置し、各メッセージが独自のスケジュールを持つようにします。
- ブランチまたは[実験パス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)ステップを使用して、ユーザーが異なるタイミングのパスをたどるようにします。
- ユースケースが1つのキャンバス内にとどまる必要がない場合は、別々のキャンペーンを使用します。

キャンペーンでの多変量およびABテストの概念については、[多変量およびABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。

### キャンバスのメッセージステップでユーザーがグローバルフリークエンシーキャップに達した場合はどうなりますか？ {#what-happens-if-a-user-is-global-frequency-capped-at-a-canvas-message-step}

該当するチャネルの送信は行われませんが、グローバルフリークエンシーキャップによってメッセージが送信されなかった場合でも、メッセージステップはユーザーを次に進めます。ステップごとの進行ケースについては、[ユーザーの進行方法]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance)を参照してください。グローバルフリークエンシーキャップだけではユーザーをキャンバスから退出させません。この動作はメッセージステップの**配信バリデーション**とは別のものです。詳細については、[レート制限とフリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)を参照してください。

### 推定オーディエンスサイズよりも送信数が少ないのはなぜですか？ {#why-are-sends-lower-than-the-estimated-audience-size}

送信数が**推定オーディエンス**よりも少なくなる理由は、[キャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size)と多くの点で同じです。フリークエンシーキャップ、厳格なデバイスまたはブラウザフィルター、再適格性ウィンドウ、レート制限、チャネルレベルの除外（プッシュ到達性やメールの購読と配信性のチェックなど）が含まれます。

キャンバス固有の要因も該当します。

- **アクションベースまたはAPIトリガーのエントリ：** ユーザーはエントリ行動を実行した後にのみ進入（およびステップを受信）するため、それらのアクションが発生するまで、実際の送信数は事前の推定を下回ります。
- **オーディエンスパス：** ユーザーは適格な最も優先度の高いブランチにルーティングされるため、下流のブランチは、フラットなセグメント数が示すよりも少ないユーザーを受信する可能性があります。
- **オーディエンスと送信時チェック：** フルステップは、別途設定しない限り、送信時にフィルターを再評価します。キャンバスが作成された時点で適格だったユーザーが、メッセージ送信前に脱落することがあります。
- **コントロールグループ：** グローバルまたはキャンバスのコントロールグループは、エントリの一部をメッセージングから除外します。
- **サイレント時間と遅延：** メッセージが保留またはリスケジュールされ、表示中のレポートウィンドウから送信がずれることがあります。
- **最大エントリまたはオーディエンスキャップ：** エントリまたは送信キャップは、基礎となるセグメントがより大きい場合でも追加のユーザーを停止します。
- **レポートウィンドウ：** 分析の範囲には、推定と比較しているすべての送信が含まれていない場合があります。

### 推定オーディエンスとキャンバスのユーザー数が一致しないのはなぜですか？ {#why-dont-estimated-audience-and-canvas-user-counts-match}

**推定オーディエンス**は、推定の実行時にセグメントとエントリフィルターに一致するユーザーを反映します。その時点以降、遅延エントリやアクションベースのエントリ、再適格性、APIトリガー、またはブランチルーティングにより、スナップショットと比較してジャーニーに関与するプロファイル数が増加することがあります。また、送信時フィルターが失敗するとユーザーが脱落し、実際のエントリ数や送信数が減少します。タイミング、キャップ、評価設定を[推定オーディエンスサイズよりも送信数が少ないのはなぜですか？](#why-are-sends-lower-than-the-estimated-audience-size)と合わせて比較してください。

### *ユニーク受信者数*がターゲットにしたユーザー数よりも多いのはなぜですか？ {#why-is-_unique-recipients_-higher-than-the-number-of-users-i-targeted}

*ユニーク受信者数*が予想よりも多くなるのは、Brazeがキャンバスおよびキャンペーンのレポートで**日次ユニーク受信者**をトラッキングしているためです。これにより、ユーザーがジャーニーでメッセージを受信するたびに正確なコンバージョンアトリビューションが可能になります。

たとえば、ユーザーが月曜日にキャンバスステップを受信し、金曜日に再度受信して、それぞれの送信後にコンバージョンした場合、Brazeは2つの受信者行と2つの対象範囲内コンバージョンをカウントできます。繰り返しエントリや再適格性がある場合、同じ少数のプロファイルセットが数日間にわたって複数の*ユニーク受信者*を生成する可能性があります。

### キャンバスの送信率が低下しているのはなぜですか？ {#why-is-my-canvas-experiencing-lower-send-rates}

日次スケジュールのキャンバスが時間の経過とともに送信ユーザー数が減少している場合、以下を確認してください。

- **再適格性が有効になっているか確認する：** 再適格性がない場合、Brazeは各ユーザーをキャンバスに1回のみ進入させます。日次スケジュールのキャンバスでは、オーディエンスに一致し、まだキャンバスに進入していないユーザーのみが各エントリの対象になります。より多くのユーザーが進入するにつれて、後のエントリには対象ユーザーが少なくなるため、エントリ量は減少します。
- **オーディエンスのメンバーシップが固定かどうか確認する：** 固定ユーザーリスト（セグメントフィルターとして使用される[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)など）から構築されたオーディエンスは、自動的に新しいメンバーを獲得しません。新規エントリがなければ、ユーザーがキャンバスに進入してもエントリ量は回復できません。

[配信速度レート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting)やその他の単一発生の送信数を低下させる要因については、[推定オーディエンスサイズよりも送信数が少ないのはなぜですか？](#why-are-sends-lower-than-the-estimated-audience-size)を参照してください。

### 小さなコントロールグループセグメントの履歴メンバーシップに変動が表示されるのはなぜですか？ {#why-does-a-small-control-group-segment-show-changes-in-historical-membership}

履歴メンバーシップチャートは推定サンプルを使用しているため、小さなセグメント（[グローバルコントロールグループ]({{site.baseurl}}/user_guide/audience/global_control_group)セグメントを含む）では、基礎となるオーディエンスが安定している場合でも日々の変動が表示されることがあります。推定の仕組みとチャートが変動する理由については、[セグメントの履歴メンバーシップサイズの表示]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#viewing-historical-segment-membership-size)を参照してください。

## 分析とコンバージョン {#analytics-and-conversions}

### コンバージョンダッシュボードはキャンバスのコンバージョンをどのようにアトリビューションしますか？ {#how-does-the-conversions-dashboard-attribute-canvas-conversions}

[コンバージョンダッシュボード]({{site.baseurl}}/user_guide/analytics/dashboards/conversions)は、選択した[アトリビューション方法]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#attribution-methods)（例：**受信時**、**送信時**、**開封時**、**クリック時**）に基づいてキャンバスのコンバージョンをアトリビューションします。レポートにユーザーが表示されるには、キャンバスまたはキャンペーンにエントリし、選択されたアトリビューション方法を記録し、レポート設定内でコンバージョンイベントを実行する必要があります。

キャンバス分析におけるステップレベルおよびバリアントレベルのコンバージョンルールについては、[キャンバスでユーザーのコンバージョンはどのようにトラッキングされますか？](#how-are-user-conversions-tracked-in-a-canvas)を参照してください。

### キャンバスでユーザーのコンバージョンはどのようにトラッキングされますか？ {#how-are-user-conversions-tracked-in-a-canvas}

ユーザーはキャンバスのエントリごとに1回のみコンバージョンできます。コンバージョンは、そのエントリでユーザーが受信した最新のメッセージに割り当てられます。キャンバスの冒頭にあるサマリーブロックは、メッセージを受信したかどうかに関係なく、そのパス内のユーザーが実行したすべてのコンバージョンを反映します。後続の各ステップでは、そのステップがユーザーが受信した最新のステップであった間に発生したコンバージョンのみが表示されます。

{% alert note %}
ユーザーがキャンバスに再エントリした場合、コンバージョンイベントは最新のエントリに対してのみトラッキングされます。コンバージョンイベントがバックフィルされた場合でも、以前のエントリに対してはコンバージョンイベントは記録されません。
{% endalert %}

{% details 例を展開 %}

**例 1**

10件のプッシュ通知を含むキャンバスパスがあり、コンバージョンイベントが「セッション開始」（「アプリを開く」）の場合：

- ユーザー A はエントリ後、最初のメッセージを受信する前にアプリを開きます。
- ユーザー B は各プッシュ通知の後にアプリを開きます。

**結果:** サマリーには2件のコンバージョンが表示されますが、個別のステップでは最初のステップで1件のコンバージョンが表示され、後続のすべてのステップでは0件となります。

{% alert note %}
コンバージョンイベントが発生した時にサイレント時間帯がアクティブな場合、同じルールが適用されます。
{% endalert %}

**例 2**

サイレント時間帯が有効になっている1ステップのキャンバスの場合：

1. ユーザーがキャンバスにエントリします。
2. 最初のステップにはディレイがありませんが、設定されたサイレント時間帯内のため、メッセージは抑制されます。
3. ユーザーがコンバージョンイベントを実行します。

**結果:** ユーザーはキャンバスバリアント全体ではコンバージョン済みとしてカウントされますが、ステップを受信していないため、ステップではカウントされません。

{% enddetails %}

### 異なるコンバージョン率の種類の違いは何ですか？ {#whats-the-difference-between-the-different-conversion-rate-types}

- キャンバス全体のコンバージョンは、コンバージョンイベントを完了したユニークユーザーの数を反映しており、各ユーザーが完了したコンバージョンの数ではありません。
- バリアントコンバージョン率またはキャンバスの冒頭にあるサマリーブロックは、メッセージを受信したかどうかに関係なく、そのパス内のユーザーが実行したすべてのコンバージョンを集計合計として反映します。
- ステップコンバージョン率は、そのメッセージステップを受信し、設定されたコンバージョンイベントのいずれかを完了した個人の数を反映します。

### キャンバスのステップコンバージョン率がキャンバスバリアントの合計コンバージョン率と等しくないのはなぜですか？ {#why-is-my-canvas-step-conversion-rate-not-equal-to-my-canvas-variant-total-conversion-rate}

キャンバスバリアントのコンバージョン合計がそのステップ合計の合算よりも大きくなることは一般的です。これは、ユーザーがバリアントにエントリするとすぐにバリアントのコンバージョンイベントを実行できるためです。しかし、この同じコンバージョンイベントはキャンバスステップにはカウントされません。そのため、キャンバスにエントリし、最初のキャンバスステップを受信する前にコンバージョンイベントを実行したユーザーは、バリアントのコンバージョン合計にはカウントされますが、ステップ合計にはカウントされません。キャンバスにエントリしたが、いずれのステップも受信する前にキャンバスを離脱したユーザーにも同じことが当てはまります。

また、ユーザーがバリアントにエントリし、ステップからメッセージが送信されず、その後コンバージョンする場合もあります。この場合、ステップレベルではコンバージョンは記録されません。しかし、ユーザーは技術的にはコンバージョンしているため、キャンバスレベルではコンバージョンが記録されます。

### APIトリガーのキャンバスをユーザーが受信したことを確認するにはどうすればよいですか？ {#how-can-i-confirm-if-my-users-received-an-api-triggered-canvas}

キャンバスフィルターを使用して[セグメントを作成]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)することで、ユーザーがキャンバスにエントリしたか、特定のキャンバスステップを受信したかを確認できます。例えば、ユーザーがAPIトリガーのキャンバスにエントリしたことを確認する場合はキャンバスエントリフィルターを使用し、キャンバスからメッセージを受信したことを確認する場合は受信ステップフィルターを使用します。その後、[`/users/export/segment`エンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)を使用して、そのセグメントのユーザーをエクスポートします。

### キャンバスを削除できますか？ {#can-i-delete-a-canvas}

いいえ。ただし、[キャンバスをアーカイブする]({{site.baseurl}}/user_guide/messaging/governance/archiving)ことはできます。

### アーカイブされたキャンバスやキャンペーンを再開するにはどうすればよいですか？ {#how-do-i-resume-an-archived-canvas-or-campaign}

アーカイブされたメッセージは、編集可能な状態に戻すまで送信されません。キャンペーンまたはキャンバスを[アーカイブ解除]({{site.baseurl}}/user_guide/messaging/governance/archiving#unarchiving)し、エントリスケジュールまたは送信時間を将来の期間に設定し（クリーンなコピーが必要な場合はジャーニーを複製し）、必要に応じて**再開**またはローンチしてください。詳しくは[キャンペーンとキャンバスのアーカイブ]({{site.baseurl}}/user_guide/messaging/governance/archiving)を参照してください。

### エラーが表示されないのにキャンバスが保存されないのはなぜですか？ {#why-doesnt-my-canvas-save-when-no-error-appears}

オーディエンスまたはステップレベルのフィルターに空の**カスタム属性**フィルターがあると、詳細なバリデーションメッセージが表示されずに保存がブロックされることがあります。各フィルターカードを開き、不完全なカスタム属性ルールを削除するか、属性名と値の両方を入力してから、再度**保存**を選択してください。

### キャンバスやキャンペーンからタグが消えたのはなぜですか？ {#why-did-a-tag-disappear-from-my-canvas-or-campaign}

ワークスペースから[タグ]({{site.baseurl}}/user_guide/messaging/governance/tags)が削除されると、Brazeはそのタグを参照していたすべてのキャンペーンとキャンバスからそのタグを削除します。このクリーンアップは、キャンバスの変更ログに独自の行として表示されないことがあります。

### 各キャンバスコンポーネントの分析を表示するにはどうすればよいですか？ {#how-can-i-view-analytics-for-each-of-my-canvas-components}

キャンバスコンポーネントの分析を表示するには、キャンバスに移動し、**キャンバスの詳細**ページを下にスクロールします。ここで、各コンポーネントの分析を表示できます。詳しくは[キャンバス分析]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics)を参照してください。

### キャンバスステップからのエンゲージメントはいつユーザープロファイルに表示されますか？ {#when-is-engagement-from-a-canvas-step-visible-on-a-user-profile}

`Received Message from キャンバス Step`などのフィルターは、Brazeがそのステップに対応する送信、受信、またはエンゲージメントイベントを記録した後に更新されます。アプリ内メッセージは、送信スタイルの指標とは別にインプレッションを記録することがあります。[インプレッションが記録されているのにキャンバスの送信数がゼロと表示される場合があるのはなぜですか？](#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged)を参照してください。これらの同じイベントは**キャンバスの詳細**のステップ指標にも表示されます。

### ユニークユーザー数を見る場合、キャンバス分析とセグメンターのどちらがより正確ですか？ {#when-looking-at-the-number-of-unique-users-is-canvas-analytics-or-the-segmenter-more-accurate}

セグメンターは、キャンバスやキャンペーンの統計と比較して、ユニークユーザーデータのより正確な統計です。これは、キャンバスとキャンペーンの統計は、何かが発生した際にBrazeがインクリメントする数値であるため、この数値がセグメンターの数値と異なる結果になる変数が存在する可能性があるためです。例えば、ユーザーはキャンバスやキャンペーンに対して複数回コンバージョンすることができます。

### キャンバスにエントリするユーザー数が期待する数と異なるのはなぜですか？ {#why-does-the-number-of-users-entering-a-canvas-not-match-the-expected-number}

キャンバスにエントリするユーザー数は、オーディエンスとトリガーの評価方法により、期待する数と異なる場合があります。Brazeでは、オーディエンスはトリガーの前に評価されます（[属性の変更]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)トリガーを使用している場合を除く）。これにより、トリガーアクションが評価される前に、選択したオーディエンスに含まれていないユーザーがキャンバスから除外されます。

### キャンバスジャーニー中の匿名ユーザーはどうなりますか？ {#what-happens-to-anonymous-users-during-their-canvas-journey}

匿名ユーザーはキャンバスにエントリおよび離脱できますが、識別されるまでそのアクションは特定のユーザープロファイルに関連付けられないため、分析でインタラクションが完全にトラッキングされない場合があります。[クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder)を使用して、これらの指標のレポートを生成できます。

{% alert tip %}
キャンバスのトラブルシューティングについてさらにサポートが必要な場合は、問題の発生から30日以内にBrazeサポートにお問い合わせください。直近30日分の診断ログのみが保持されています。
{% endalert %}

### 現在キャンバスジャーニー中のユーザーをキャンペーンやセグメントから除外できますか？ {#can-i-exclude-users-who-are-currently-in-a-canvas-journey-from-a-campaign-or-segment}

`Entered キャンバス Variation`、`In キャンバス Control Group`、`Received Message from キャンバス Step`などの[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)を使用して、キャンバスのエントリ、バリアント割り当て、またはステップのエンゲージメントに基づいてユーザーをターゲットできます。これらのフィルターはエントリ履歴とインタラクションを評価するものであり、ユーザーがアクティブなジャーニーをまだ進行中かどうかを示すものではありません。

アクティブなキャンバスへの参加に基づいてユーザーを含めたり除外したりするには、キャンバスのエントリと離脱に[ユーザー更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)ステップを追加してカスタム属性を設定およびクリアし、キャンペーンやセグメントでそれらの属性に基づいてフィルタリングしてください。

## セグメンテーション {#segmentation}

### 「キャンバスバリエーションに入っていない」と「キャンバスコントロールグループに含まれていない」の違いは何ですか？ {#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group}

フィルターの完全な定義については、[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)を参照してください。

#### キャンバスバリエーションに入っていない {#has-not-entered-canvas-variation}

ユーザーが特定のキャンバスのバリエーションパスに一度も入っていないことを意味します。コントロールグループに含まれていないすべてのユーザーが対象となり、キャンバスに入ったかどうかは問いません。これには、別のバリエーションに入ったユーザーや、どのバリエーションにも入っていないユーザーが含まれます。

#### キャンバスコントロールグループに含まれていない {#is-not-in-canvas-control-group}

ユーザーがキャンバスに入ったが、コントロールグループには含まれておらず、結果としてバリエーションを受け取ったことを意味します。これにはキャンバスに入ったユーザーのみが含まれます。

バリエーションの割り当てはキャンバスへのエントリ時に行われます。ユーザーがキャンバスに入っていない場合、どのバリアントにも割り当てられません。つまり、コントロールグループにもバリアントにも含まれません。

## 従来のキャンバスエディター {#original-canvas-editor}

{% details 従来のキャンバスエディターのFAQを展開 %}

### 従来のエディターの既存のキャンバスを現在のエディターに変換するにはどうすればよいですか？ {#how-do-i-convert-an-existing-canvas-from-the-original-editor-to-the-current-editor}

[キャンバスを複製]({{site.baseurl}}/cloning_canvases)できます。これにより、従来のキャンバスのコピーが最新のキャンバスワークフローで作成されます。

### 現在のキャンバスエディターと従来のキャンバスエディターの主な違いは何ですか？ {#what-are-the-main-differences-between-the-current-and-original-canvas-editors}

#### キャンバスコンポーネントツールバー {#canvas-component-toolbar}

以前の従来のキャンバスエディターでは、ユーザージャーニーでステップを作成するたびに、デフォルトでフルステップが追加されていました。これらのフルステップはさまざまなキャンバスコンポーネントに置き換えられ、編集エクスペリエンスの可視性とカスタマイズ性が向上しました。すべてのキャンバスコンポーネントをキャンバスステップツールバーからすぐに確認できます。

#### ステップの動作 {#step-behavior}

以前は、各フルステップに遅延やスケジュール設定、例外イベント、オーディエンスフィルター、メッセージ設定、メッセージ進行オプションなどの情報がすべて1つのコンポーネントに含まれていました。現在のエディターではこれらが個別の設定になっているため、キャンバス構築エクスペリエンスのカスタマイズ性が向上し、機能にいくつかの違いが生じています。

#### メッセージコンポーネントの進行 {#message-component-advancement}

[メッセージコンポーネント]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)は、ステップに入ったすべてのユーザーを進行させます。メッセージ進行の動作を指定する必要がないため、全体的なステップの設定がシンプルになります。**メッセージ送信時に進行**オプションを実装したい場合は、前のステップを受信しなかったユーザーをフィルタリングするために、別のオーディエンスパスを追加してください。

#### 遅延の「以内」の動作 {#delay-in-behavior}

[遅延コンポーネント]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)は、次のステップに進む前に遅延時間全体を待機します。

例えば、4月12日に遅延コンポーネントがあり、遅延が1日後の午後2時にユーザーを次のステップに送る設定になっているとします。ユーザーが4月13日の午後2時01分にコンポーネントに入った場合：
- 従来のワークフローでは、ユーザーは4月14日の午後2時に次のステップに進みます。これはエントリ時刻から1日未満です。
- 現在のエディターでは、ユーザーは4月15日の午後2時に次のステップに進みます。同じ時刻ですが、エントリ時刻から1日以上経過しています。

#### インテリジェントタイミングの動作 {#intelligent-timing-behavior}

[インテリジェントタイミング]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)はメッセージコンポーネントに保存されるため、遅延はインテリジェントタイミングの計算前に適用されます。つまり、ユーザーがコンポーネントに入るタイミングによっては、従来のキャンバスワークフローで構築されたキャンバスよりもメッセージの受信が遅くなる場合があります。

例えば、遅延が2日に設定され、インテリジェントタイミングがオンで、メッセージの最適な送信時刻が午後2時と判定されたとします。ユーザーが午後2時01分に遅延ステップに入った場合：
- **現在のワークフロー:** 遅延が経過するまでに48時間かかるため、ユーザーは3日目の午後2時にメッセージを受信します。
- **従来のワークフロー:** ユーザーは2日目の午後2時にメッセージを受信します。

インテリジェントタイミングがオンの場合、メッセージはユーザーがメッセージコンポーネントに入ってから24時間以内に、特定されたインテリジェントな時刻に送信されます（遅延コンポーネントが関与していなくても同様です）。

#### 例外イベント {#exception-events}

##### サイレント時間帯 {#quiet-hours}

例外イベントはアクションパスを使用して適用され、メッセージステップとは別になっています。サイレント時間帯はメッセージコンポーネントで適用されます。つまり、ユーザーがすでにアクションパスを通過し（例外イベントで除外されず）、メッセージコンポーネントに到達した時点でサイレント時間帯に該当し、サイレント時間帯終了後にメッセージを再送信するようキャンバスが設定されていた場合、例外イベントは適用されなくなります。このユースケースは一般的ではありません。

セグメントとフィルターについては、メッセージステップに配信バリデーションがあり、送信時に検証される追加のセグメントとフィルターを設定できます。これにより、前述のサイレント時間帯のエッジケースを防ぐことができます。

##### 「以内」または「次の」スケジュール設定 {#in-or-on-the-next-schedule-setting}

例外イベントはアクションパスを使用して作成されます。アクションパスは「X時間のウィンドウの後」のみをサポートし、「X時間以内」や「次のX時間に」はサポートしていません。

{% enddetails %}

### 「リクエストタイムアウト」エラーに関するサポートチケットを送信する際には何を含めるべきですか？ {#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error}

キャンバスの編集中に「リクエストタイムアウト」エラーが発生し、[Brazeサポート]({{site.baseurl}}/braze_support)に連絡する必要がある場合は、解決を迅速化するために以下の情報を含めてください。

{% multi_lang_include messaging/support_ticket_request_timed_out_details.md context='canvas' %}

## キャンバスの配信とトラブルシューティング {#canvas-delivery-and-troubleshooting}

### 孤立したユーザーはキャンバスメッセージを受信できますか？ {#are-orphaned-users-eligible-to-receive-canvas-messages}

いいえ。[孤立したユーザー]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users)はメッセージを受信する資格がありません。ユーザーがキャンバスジャーニーに参加中にプロファイルが孤立した場合、そのユーザーはフローからサイレントに退出します。分析では、その退出に対して**Exited**イベントが常に表示されるとは限りません。また、ワークフローサマリーに`exited_date`や`exit_reason`のない`partial_update_token`が含まれることがあります。

マージと孤立したプロファイルの詳細については、[重複ユーザーのマージ]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users)を参照してください。

### アクティブなキャンバスやキャンペーンを停止した場合、すでにESPに送信されたメッセージは配信されますか？ {#if-i-stop-an-active-canvas-or-campaign-do-messages-already-sent-to-the-esp-still-deliver}

はい。Brazeがメールサービスプロバイダー (ESP) にリクエストを送信した後、Brazeはその送信を取り消すことができません。キャンバスやキャンペーンを停止すると、新しい送信リクエストは防止されますが、すでにESPに引き渡されたメッセージは配信される可能性があり、ESPが処理する際に送信カウントが増加することがあります。

これは[キャンバスを停止した場合](#what-happens-when-you-stop-a-canvas)で説明されている動作と同じです。処理中のメール送信はすぐには停止されません。

### ユーザーに表示されるコンテンツがないキャンバスのwebhookステップが実行されたことを確認するには？ {#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content}

Brazeは、キャンペーンおよびキャンバスの[webhook]({{site.baseurl}}/user_guide/channels/webhooks)ステップについて、webhookの**送信**および関連する配信結果をトラッキングします。ステップの分析、[webhookレポート]({{site.baseurl}}/user_guide/channels/webhooks/reporting)、または[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)のwebhookイベントを使用して、ステップが実行されたことを確認してください。サーバー側の受信証明が必要な場合は、エンドポイントのリクエストログも追加の確認手段となります。

Brazeには、webhookステップ用のビルトインの非表示トラッキングピクセルは含まれていません。カスタムの1ピクセル画像リクエストではなく、Brazeのwebhookメトリクスとエンドポイントのログに依存してください。

### webhookステップにボディフィールドがないのはなぜですか？ {#why-does-my-webhook-step-have-no-body-field}

webhookステップは`POST`、`PUT`、`PATCH`、`DELETE`にリクエストボディを使用します。メソッドを`GET`に切り替えると、GETリクエストはリクエストボディをサポートしないため、Brazeはボディフィールドを削除します。JSONまたはフォームデータを送信する必要がある場合は、ボディをサポートするメソッドに切り替えてください。メソッドの詳細については、[webhookの作成]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#http-method)を参照してください。

### webhookステップでspacer.gifを使用するには？ {#how-do-i-use-spacergif-in-a-webhook-step}

Brazeは`cdn.braze.com`と`braze-images.com`に`spacer.gif`プレースホルダー画像をホストしています。外部エンドポイントを呼び出さずにステップを実行する必要がある場合に、webhook URLをこの画像に向けるチームもあります。標準的なwebhookステップは実際のエンドポイントを呼び出す必要があります。配信を確認するには、[webhookレポート]({{site.baseurl}}/user_guide/channels/webhooks/reporting)とエンドポイントログを使用してください。詳しくは[ユーザーに表示されるコンテンツがないキャンバスのwebhookステップが実行されたことを確認するには？](#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content)をご覧ください。

### 「invalid next-step-id」エラーでキャンバスが読み込まれないのはなぜですか？ {#why-wont-my-canvas-load-with-an-invalid-next-step-id-error}

このコンソールエラーは、少なくとも1つのステップが存在しないか無効な次のステップを参照していることを意味します。たとえば、部分的な削除、複製、インポートの後に発生することがあります。エディタでキャンバスを開き、孤立したステップを再接続するか、有効なダウンストリームパスがなくなったステップを削除してください。それでもキャンバスが読み込まれない場合は、キャンバスIDとコンソールエラーのスクリーンショットを添えて[Brazeサポート]({{site.baseurl}}/braze_support)に連絡してください。

### Currentsのキャンバスコンバージョンタイムスタンプがキャンバス分析と異なるのはなぜですか？ {#why-does-a-canvas-conversion-timestamp-in-currents-differ-from-my-canvas-analytics}

Currentsはキャンバスコンバージョンを[`users.canvas.Conversion`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#canvas-conversion-events)イベントとして記録します。イベントの`time`はコンバージョンイベントが発生した時刻です。そのイベントの`conversion_behavior`フィールドはコンバージョン定義（タイプとウィンドウ）を記述します。キャンバス分析では、コンバージョンウィンドウ内のキャンバスエントリに対するコンバージョンも集計されることがあります。エクスポートを照合する際は、Currentsの`time`をコンバージョンイベントのタイムスタンプおよびキャンバスのコンバージョンウィンドウ設定と比較してください。

### Currentsで`canvas_step_name`がnullになるのはなぜですか？ {#why-is-canvas_step_name-null-in-currents}

`canvas_step_name`などのキャンペーンおよびキャンバスの名前フィールドは、Brazeがステップメタデータの伝播を完了する前にCurrentsイベントが送信された場合、`null`になることがあります。たとえば、ステップを作成または名前変更した直後に発生する可能性があります。詳細については、[Currentsデータでキャンペーン名またはキャンバスステップ名が`NULL`なのはなぜですか？]({{site.baseurl}}/user_guide/data/distribution/braze_currents/faq#why-is-the-campaign-name-or-canvas-step-name-null-in-my-currents-data)を参照してください。

### ユーザー更新ステップで配列が更新されないのはなぜですか？ {#why-isnt-my-array-updating-in-a-user-update-step}

[ユーザー更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)ステップのJSONを確認してください。配列やネストされた属性の更新には、変更する属性の有効なパスと値が必要です。外部ユーザーIDなど、ステップが自動的に提供するフィールドは含めないでください。起動前にステップの**プレビューとテスト**タブを使用してペイロードを確認してください。

### `external_id`を持たないユーザーにキャンバスメッセージを送信できますか？ {#can-i-send-canvas-messages-to-users-without-an-external_id}

はい。Brazeユーザープロファイルがすでに存在している場合に可能です。`external_id`を持たないユーザーは[匿名ユーザー]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles)であり、`braze_id`または[ユーザーエイリアス]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases)で参照できます。キャンバスにエントリする前に、[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)またはSDKでプロファイルを作成または更新してから、[アクションベースまたはAPIトリガーのエントリ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule)を使用してください。標準的なキャンバスのターゲティングにはBrazeユーザープロファイルが必要です。プロファイルのないメールアドレスだけにキャンバスメッセージを送信することはできません。

### トリガーイベントを実行した回数よりもユーザーがキャンバスにエントリした回数が少ないのはなぜですか？ {#why-did-a-user-enter-a-canvas-fewer-times-than-they-performed-the-trigger-event}

アクションベースおよびAPIトリガーのキャンバスでは、Brazeはトリガーイベントの重複を排除するため、ユーザーは同じキャンバスに対して**1秒あたり最大約1回**しかエントリできません。ユーザーが1秒以内に同じトリガーを複数回実行した場合、1回のエントリのみが処理されます。

同じ秒内に複数のエントリを許可するには、トリガーイベントを少なくとも1.1秒間隔で送信してください（たとえば、サーバーからイベントのタイミングを制御する場合）。同じ秒のトリガーを複数回許可するキャンペーン形式の動作については、適切なスケジューリングと再適格性設定を持つ[キャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns)とユースケースを比較してください。

### APIトリガーのキャンバスでユーザーの重複排除はいつ行われますか？ {#when-are-users-de-duplicated-in-api-triggered-canvases}

ユーザーがAPIトリガーのキャンバスに再エントリし、前回のエントリから同一メッセージのためにすでにキューに入っている遅延ステップに到達した場合、Brazeは重複送信を防ぐためにユーザーの重複を排除します。2回目のキャンバスインスタンスは退出するため、エントリ数が送信数を超えることがあります。

### テストプッシュが間違ったアプリに送信されるのに、ライブ送信は正しいのはなぜですか？ {#why-does-a-test-push-go-to-the-wrong-app-but-live-sends-look-correct}

ユーザープロファイルの**テストプッシュ**は、そのプロファイルのプッシュ有効なすべてのデバイスに配信されます。デバイスに複数のアプリがインストールされている場合、OSは通常、最初に利用可能なアプリにテスト通知を配信しますが、それは検証したいアプリではない可能性があります。

アプリ固有のターゲティングを確認するには、プロファイルの**テストプッシュ**だけに頼るのではなく、限定的なオーディエンス（たとえば`external_id`でフィルター）を持つキャンペーンまたはキャンバスを通じてライブまたはテストメッセージを送信してください。

**キャンバス**の複数アプリを持つメッセージステップでは、メッセージステップの**送信時にオーディエンスを検証**をオンにして、セグメントとフィルターのチェックが送信時に実行されるようにしてください。詳細については、[メッセージステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)を参照してください。

テストプッシュの一般的な動作については、[テストメッセージの送信]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages)と[プッシュFAQ]({{site.baseurl}}/user_guide/channels/push/faqs)を参照してください。

### iOSとAndroidでPush Storiesをデバッグするには？ {#how-do-i-debug-push-stories-on-ios-and-android}

セットアップとクリエイティブ要件については、[Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories)を参照してください。実装とリッチプッシュ通知の処理については、開発者ガイドの[リッチプッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/rich)と[Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories)を参照してください。

### 「キャンバス Messages Delayed 24+ Hours」メールは誰に届きますか？ {#who-receives-the-canvas-messages-delayed-24-hours-email}

Brazeは、キャンバスメッセージがレート制限により24時間以上遅延した場合にこの通知を送信します。このメールは、影響を受けるキャンバスに以前変更を加えたダッシュボードユーザー（キャンバスの変更ログに基づく）に送信されます。Brazeがこれらの受信者を特定できない場合、メールはワークスペースの**会社管理者**に送信されます。

### 例外イベント発生後、ユーザーはいつメッセージの受信を停止しますか？ {#when-does-a-user-stop-receiving-messages-after-an-exception-event}

Brazeは例外イベントが発生するとすぐに退出を記録しますが、タイマーが完了するまでユーザーがステップ内に留まることがあります。これは特に遅延ステップで顕著です。動作は、スケジュールされたステップとイベントトリガーのステップでも異なります。タイムライン、例、分析の注意点については、[終了条件]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria)を参照してください。

### リンクエイリアスのインタラクションを選択するとアクションパスステップにエラーが表示されるのはなぜですか？ {#why-does-my-action-paths-step-show-an-error-when-i-select-a-link-alias-interaction}

メールのインタラクティビティトリガー（たとえば**メール内のエイリアスをクリック**や**キャンペーンまたはキャンバスステップ内のエイリアスをクリック**）を使用するアクショングループには、そのリンクを含むメッセージをすでに送信したメッセージステップが必要です。アクションパスステップがクリックを評価する前にメールが送信されるようにステップを追加または並べ替えるか、ユーザーがこのキャンバスですでに受信したメッセージに一致するインタラクションを選択してください。インタラクショントリガーの完全なリストについては、[アクションベース配信]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)を参照してください。

### 過去のカスタムイベントタイムスタンプはアクションベースのキャンバスやキャンペーンにどのように影響しますか？ {#how-do-historical-custom-event-timestamps-affect-action-based-canvases-and-campaigns}

Brazeは、適格なイベントが取り込まれ、ユーザーがオーディエンスルールを満たした時点でアクションベースのジャーニーを評価します。キャンバスやキャンペーンがアクティブだったウィンドウの外でイベントがプロファイルに到達した場合、またはユーザーがオーディエンスに一致する前にイベントが発生した場合、エントリやダウンストリームの送信が期待通りに行われないことがあります。イベントのタイムスタンプを公開時刻およびセグメントメンバーシップと比較するには、ユーザープロファイルのアクティビティログと[カスタムイベントのトラブルシューティング]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#troubleshooting-custom-events)のトラブルシューティング手順を使用してください。それでも動作が期待と一致しない場合は、[Brazeサポート]({{site.baseurl}}/braze_support)に連絡してください。