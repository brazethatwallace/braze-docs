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

### キャンバスに含められるステップの数は？ {#how-many-steps-i-can-include-in-a-canvas}

キャンバスには最大200ステップを追加できます。

### キャンバスエントリプロパティにサイズ制限はありますか？ {#are-there-size-limits-for-canvas-entry-properties}

はい。[キャンバスコンテキストオブジェクト]({{site.baseurl}}/api/objects_filters/context_object)（キャンバスエントリプロパティ）の最大サイズは50&nbsp;KBです。ペイロードはこの制限内でできるだけ小さくしてください。キャンバスでのエントリプロパティとイベントプロパティの仕組みについては、[コンテキストとイベントプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)を参照してください。

### 「Too many キャンバス branches」エラーが表示されるのはなぜですか？ {#why-do-i-see-a-too-many-canvas-branches-error}

このエラーは、ステップの分岐とエントリオーディエンスサイズの組み合わせにより、メッセージの送信を妨げるクラスターパフォーマンスの問題が発生する可能性がある場合に表示されます。解決手順（[オーディエンスパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)の使用、分岐やオーディエンスサイズの削減、キャンバスフローでの再構築など）については、[「Too many キャンバス branches」エラー]({{site.baseurl}}/user_guide/messaging/canvas/troubleshooting#too-many-canvas-branches-error)を参照してください。

### キャンバスで再エントリを有効にしてBrazeAI<sup>TM</sup>で最適化を使用できますか？ {#can-i-use-optimize-with-brazeai-with-re-eligibility-in-a-canvas}

はい。キャンバスでは再エントリが有効な場合に[BrazeAI<sup>TM</sup>で最適化]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai)を使用できます。Brazeは再エントリ時に同じバリアントを保証することはできません。これは、時間の経過とともに割り当てが変化するためです。キャンペーンでは、**BrazeAI<sup>TM</sup>で最適化**が有効な場合、24時間以上の再エントリウィンドウが必要です。

### コンポーネントとステップの違いは何ですか？ {#whats-the-difference-between-a-component-and-a-step}

[コンポーネント]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about)は、キャンバスの効果を判断するために使用できるキャンバスの個々のパーツです。コンポーネントには、ユーザージャーニーの分割、遅延の追加、複数のキャンバスパスのテストなどのアクションを含めることができます。キャンバスのステップとは、キャンバスブランチにおけるパーソナライズされたユーザージャーニーを指します。基本的に、キャンバスはユーザージャーニーのステップを作成する個々のコンポーネントで構成されています。

### 切断されたステップがあるキャンバスをローンチできますか？ {#can-i-launch-a-canvas-with-disconnected-steps}

はい。ローンチ後に切断されたステップがあるキャンバスを保存することもできます。

### 切断されたステップに到達したユーザーはどうなりますか？ {#where-do-users-go-when-theyve-reached-a-disconnected-step}

ユーザーがキャンバスワークフローの切断されたステップにいる場合、後続のステップがあればそのステップに進みます。ステップの設定によって、ユーザーがどのように進むかが決まります。これは、ステップをキャンバスの残りの部分に直接接続しなくても、ユーザーがステップに変更を加えられるようにするためのものです。また、すぐにライブにする前にテストする余地も与えられるため、事実上下書きの保存が可能になります。

ステップを切断する前に、キャンバスステップで保留中のユーザーの分析ビューを確認することをお勧めします。

### オーディエンスと送信時間が同じで、1つのバリアントに複数のブランチがあるキャンバスの場合、どうなりますか？ {#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches}

各ステップに対してジョブがキューに入れられ、ほぼ同じ時間に実行され、そのうちの1つが「勝ち」ます。実際には、ある程度均等に分散される可能性がありますが、最初に作成されたステップに若干偏る可能性が高いです。

さらに、その分布がどのようになるかについて正確な保証はできません。均等な分割が必要な場合は、[ランダムバケット番号]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers)フィルターを追加してください。

### キャンバスのオーディエンスはどのように評価されますか？ {#how-are-canvas-audiences-evaluated}

デフォルトでは、キャンバスのフルステップのフィルターとセグメントは送信時に確認されます。条件分岐ステップは、前のステップを受信した直後（または遅延の前）に評価を実行します。

### 例外イベントはいつトリガーされますか？ {#when-does-an-exception-event-trigger}

例外イベントは、ユーザーが関連付けられたキャンバスコンポーネントの受信を待っている間にのみトリガーされます。ユーザーが事前にアクションを実行した場合、例外イベントはトリガーされません。特定のイベントを事前に実行したユーザーを除外したい場合は、代わりに[フィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)を使用してください。

### キャンバスの編集は、すでにキャンバスにいるユーザーにどのように影響しますか？ {#how-does-editing-a-canvas-affect-users-already-in-the-canvas}

複数ステップのキャンバスの一部のステップを編集した場合、すでにオーディエンスに含まれているがまだステップを受信していないユーザーは、メッセージの更新バージョンを受け取ります。これは、ユーザーがまだそのステップの評価を受けていない場合にのみ発生することに注意してください。

ローンチ後に編集できる内容の詳細については、[ローンチ後のキャンバスの変更]({{site.baseurl}}/post-launch_edits)を参照してください。

### キャンバスを停止するとどうなりますか？ {#what-happens-when-you-stop-a-canvas}

キャンバスを停止すると、以下が適用されます。

- ユーザーはキャンバスに入ることができなくなります。
- ユーザーがフローのどの位置にいても、それ以上のメッセージは送信されません。
- **例外：** メールを含むキャンバスはすぐには停止しません。送信リクエストがSendGridに送られた後は、ユーザーへの配信を停止する手段はありません。

### ユーザーライフサイクルごとに1つのキャンバスを構築すべきですか、それとも別々のキャンバスにすべきですか？ {#should-i-build-one-canvas-or-separate-canvases-per-user-lifecycle}

キャンバスで達成したい目標に応じて、ユーザージャーニーの構築に異なるアプローチが必要になる場合があります。キャンバスの柔軟性により、ユーザーライフサイクルのあらゆる段階のユーザージャーニーをマッピングできます。効果的なユーザージャーニーを作成するための合理化されたアプローチの例については、[Brazeキャンバステンプレート]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates)をご覧ください。

## メッセージと配信 {#messages-and-delivery}

### キャンバスのアプリ内メッセージはいつ送信されますか？ {#when-are-in-app-messages-in-canvas-sent}

アプリ内メッセージは、次のセッション開始時に送信されます。つまり、キャンバスが停止される前にユーザーがキャンバスステップに入った場合、アプリ内メッセージの有効期限が切れていなければ、次のセッション開始時にそのアプリ内メッセージを受信します。

ユーザーがキャンバス停止前にセッションを開始しても、アプリ内メッセージがすぐに表示されない場合があります。これは、アプリ内メッセージがカスタムイベントによってトリガーされる場合や遅延がある場合に発生する可能性があります。つまり、キャンバスが停止された後に、ユーザーがアプリ内メッセージのインプレッションを記録し、アプリ内メッセージを「受信」する可能性があります。ただし、ユーザーはキャンバスが停止される前に、かつキャンバスステップを受け取った**後**にセッションを開始している必要があります。

{% alert note %}
キャンバスを停止しても、メッセージの受信を待っているユーザーがユーザージャーニーから退出することはありません。キャンバスを再有効化した時点でユーザーがまだメッセージを待っている場合、そのメッセージを受信します（ただし、メッセージが送信されるべきだった時間が過ぎている場合は受信しません）。
{% endalert %}

### キャンバスで送信数がゼロなのにインプレッションが記録されているのはなぜですか？ {#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged}

アプリ内メッセージステップを含むキャンバスで*送信されたメッセージ*が常にゼロの場合、アプリ内メッセージの配信が他のメッセージングチャネルとは異なる仕組みで動作しているためです。

アプリ内メッセージは、Brazeから「プッシュ」されるのではなく、SDKによって「プル」されます。対象ユーザーのアプリ内メッセージはセッション開始時に自動的に配信され、トリガーイベントが発生するまで表示を「待機」します。対象ユーザーがセッションを開始した時点でメッセージを受信するため、Brazeはこれを送信イベントとして報告しません。ユーザーがトリガーイベントを実行すると、メッセージが表示され、Brazeはインプレッションを記録し、ユーザープロファイル上でキャンバスステップ（またはキャンペーン）を受信済みとしてマークします。その結果、アプリ内メッセージの*送信数*の合計はゼロになります。

### 長い遅延や分岐の後にユーザーがアプリ内メッセージを受信しなかったのはなぜですか？ {#why-didnt-users-receive-my-in-app-message-after-a-long-delay-or-branch}

上流の[遅延]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)ステップとオーディエンスチェックが完了した後、ユーザーはメッセージステップに到達した時点でアプリ内メッセージの対象になります。メッセージの有効期限がカレンダー日付で設定されている場合や、**ステップが利用可能になってからの期間**が短い場合、遅いブランチのユーザーは有効期限後に到達し、メッセージを見ることができません。有効期限を最も長い現実的なパス遅延に合わせてください。詳細と例については、[アプリ内メッセージの有効期限]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas#in-app-message-expiration)を参照してください。

### 「キャンバス Entry Properties may not be used in In-App Messages.」と表示されるのはなぜですか？ {#why-do-i-see-canvas-entry-properties-may-not-be-used-in-in-app-messages}

このメッセージは、パーソナライゼーションがキャンバスのアプリ内メッセージで解決できないフィールドを参照している場合に表示されます。[コンテキストとイベントプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)および[メッセージステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)で説明されている`context`オブジェクトを使用してください。レガシーのLiquid名前空間`canvas_entry_properties`には`context`とは異なる制約があります。複数のステップにわたって値を保持する必要がある場合は、Brazeチームと[オリジナルキャンバスエディターの永続プロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties)を確認してください。デバイスがアプリ内ペイロードをダウンロードする前にユーザーがキャンバスを退出すると、保存された値はクリアされます。

### キャンバスのドラッグ＆ドロップアプリ内メッセージのボタンクリックはどこで確認できますか？ {#where-can-i-find-button-clicks-for-drag-and-drop-in-app-messages-in-canvas}

ドラッグ＆ドロップアプリ内メッセージのボタンレベルの指標は、キャンバスの概要レベルだけでなく、**キャンバスの詳細**内の**メッセージ**ステップ分析カードに表示されます。キャンバスを開き、メッセージステップを選択して、アプリ内エンゲージメントを確認してください。レポートの概念については、[キャンバス分析での測定とテスト]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics)を参照してください。

### 同じキャンバスのメッセージステップまたは多変量送信でバリアントごとに異なる送信時間をスケジュールできますか？ {#can-i-schedule-different-send-times-for-each-variant-in-the-same-canvas-message-step-or-multivariate-send}

いいえ。同じ多変量構成またはメッセージステップ内のバリアントは、1つの配信スケジュールを共有します。同じスケジュール送信で、あるバリアントを午後6時に、別のバリアントを午後7時に送信するよう割り当てることはできません。

送信を時間差で行う場合や、パスごとに異なる時間を使用する場合は、以下の方法をお試しください。

- メッセージステップの間に遅延ステップを配置して、各メッセージに独自のスケジュールを設定します。
- ブランチまたは[実験パス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)ステップを使用して、ユーザーが異なるタイミングのパスをたどるようにします。
- ユースケースが1つのキャンバス内にある必要がない場合は、キャンペーンを分けます。

キャンペーンにおける多変量テストとABテストの概念については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。

### キャンバスのメッセージステップでユーザーがグローバルフリークエンシーキャップの対象になった場合はどうなりますか？ {#what-happens-if-a-user-is-global-frequency-capped-at-a-canvas-message-step}

キャップ対象のチャネルではその送信を受信しませんが、グローバルフリークエンシーキャップによってメッセージが送信されなかった場合でも、メッセージステップはユーザーを次のステップに進めます。ステップごとの進行ケースについては、[ユーザーの進行方法]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance)を参照してください。グローバルフリークエンシーキャップだけではユーザーをキャンバスから退出させません。この動作はメッセージステップの**配信バリデーション**とは別のものです。詳細については、[レート制限とフリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)を参照してください。

### 送信数が推定オーディエンスサイズより少ないのはなぜですか？ {#why-are-sends-lower-than-the-estimated-audience-size}

送信数が**推定オーディエンス**より少なくなる理由は、[キャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size)と同じ理由が多く含まれます。フリークエンシーキャップ、厳格なデバイスまたはブラウザフィルター、再適格ウィンドウ、レート制限、チャネルレベルの除外（例：プッシュ到達可能性やメール購読と配信性チェック）などです。

キャンバス固有の要因も適用されます。

- **アクションベースまたはAPIトリガーのエントリ：** ユーザーはエントリ行動を実行した後にのみエントリ（およびステップの受信）するため、それらのアクションが発生するまで実際の送信数は事前の推定を下回ります。
- **オーディエンスパス：** ユーザーは適格な最も優先度の高いブランチにルーティングされるため、下流のブランチはフラットなセグメント数が示すよりも少ないユーザーを受け取る可能性があります。
- **オーディエンスと送信時チェック：** 特に設定を変更しない限り、完全なステップは送信時にフィルターを再評価します。キャンバス構築時に適格だったユーザーが、メッセージ送信前に脱落する場合があります。
- **コントロールグループ：** グローバルまたはキャンバスのコントロールグループは、エントリしたユーザーの一部をメッセージングから除外します。
- **サイレントアワーと遅延：** メッセージが保留またはリスケジュールされ、閲覧しているレポートウィンドウから送信がずれる場合があります。
- **最大エントリ数またはオーディエンスキャップ：** 基盤となるセグメントが大きくても、エントリまたは送信キャップにより追加のユーザーが停止されます。
- **レポートウィンドウ：** 分析の範囲に、推定値と比較しているすべての送信が含まれていない場合があります。

### 推定オーディエンスとキャンバスのユーザー数が一致しないのはなぜですか？ {#why-dont-estimated-audience-and-canvas-user-counts-match}

**推定オーディエンス**は、推定実行時にセグメントとエントリフィルターに一致するユーザーを反映します。その時点以降、遅延またはアクションベースのエントリ、再適格、APIトリガー、またはブランチルーティングにより、スナップショットと比較してジャーニーに触れるプロファイル数が増加する場合があります。また、送信時フィルターが失敗するとユーザーが脱落し、実際のエントリや送信数が減少する場合もあります。タイミング、キャップ、評価設定を[送信数が推定オーディエンスサイズより少ないのはなぜですか？](#why-are-sends-lower-than-the-estimated-audience-size)と併せて確認してください。

### *ユニーク受信者*がターゲットしたユーザー数より多いのはなぜですか？ {#why-is-_unique-recipients_-higher-than-the-number-of-users-i-targeted}

*ユニーク受信者*が予想よりも多くなることがあります。これは、Brazeがキャンバスおよびキャンペーンのレポートで**日別ユニーク受信者**を追跡しているためです。これにより、ユーザーがジャーニー内でメッセージを受信するたびに正確なコンバージョンアトリビューションがサポートされます。

例えば、ユーザーが月曜日にキャンバスステップを受信し、金曜日に再度受信して、各送信後にコンバージョンした場合、Brazeは2つの受信者行と2つの対象コンバージョンをカウントできます。繰り返しエントリや再適格により、同じ少数のプロファイルが数日間にわたって複数の*ユニーク受信者*を生成する可能性があります。

### キャンバスの送信率が低下しているのはなぜですか？ {#why-is-my-canvas-experiencing-lower-send-rates}

日次スケジュールのキャンバスが時間の経過とともに送信ユーザー数が減少している場合は、以下を確認してください。

- **再適格が有効になっているか確認してください：** 再適格がない場合、Brazeは各ユーザーをキャンバスに1回のみエントリさせます。日次スケジュールのキャンバスでは、オーディエンスに一致し、まだキャンバスにエントリしていないユーザーのみが各エントリの対象となります。より多くのユーザーがエントリするにつれて、後のエントリごとに対象ユーザーが少なくなり、エントリボリュームが減少します。
- **オーディエンスのメンバーシップが固定されていないか確認してください：** 固定されたユーザーリスト（セグメントフィルターとして使用される[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)など）から構築されたオーディエンスは、自動的に新しいメンバーを追加しません。新しいエントリがなければ、ユーザーがキャンバスにエントリするにつれてエントリボリュームが回復することはありません。

[配信速度レート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting)および単一の発生で送信数を低下させるその他の要因については、[送信数が推定オーディエンスサイズより少ないのはなぜですか？](#why-are-sends-lower-than-the-estimated-audience-size)を参照してください。

### 小さなコントロールグループセグメントで過去のメンバーシップに変動が見られるのはなぜですか？ {#why-does-a-small-control-group-segment-show-changes-in-historical-membership}

過去のメンバーシップチャートは推定サンプルを使用しているため、小さなセグメント（[グローバルコントロールグループ]({{site.baseurl}}/user_guide/audience/global_control_group)セグメントを含む）では、基盤となるオーディエンスが安定していても日ごとの変動が表示される場合があります。推定の仕組みとチャートが変動する理由については、[過去のセグメントメンバーシップサイズの表示]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#viewing-historical-segment-membership-size)を参照してください。

## 分析とコンバージョン {#analytics-and-conversions}

### コンバージョンダッシュボードはキャンバスのコンバージョンをどのようにアトリビューションしますか？ {#how-does-the-conversions-dashboard-attribute-canvas-conversions}

[コンバージョンダッシュボード]({{site.baseurl}}/user_guide/analytics/dashboards/conversions)は、選択した[アトリビューション方法]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#attribution-methods)（例：**受信時**、**送信時**、**開封時**、**クリック時**）に基づいてキャンバスのコンバージョンをアトリビューションします。レポートにユーザーが表示されるには、キャンバスまたはキャンペーンにエントリし、選択したアトリビューション方法を記録し、レポート設定内のコンバージョンイベントを実行する必要があります。

キャンバス分析におけるステップレベルおよびバリアントレベルのコンバージョンルールについては、[キャンバスでユーザーのコンバージョンはどのようにトラッキングされますか？](#how-are-user-conversions-tracked-in-a-canvas)を参照してください。

### キャンバスでユーザーのコンバージョンはどのようにトラッキングされますか？ {#how-are-user-conversions-tracked-in-a-canvas}

ユーザーはキャンバスのエントリごとに1回のみコンバージョンできます。コンバージョンは、そのエントリにおいてユーザーが最後に受信したメッセージに割り当てられます。キャンバスの冒頭にあるサマリーブロックは、メッセージを受信したかどうかに関係なく、そのパス内でユーザーが実行したすべてのコンバージョンを反映します。それ以降の各ステップは、そのステップがユーザーが受信した最新のステップであった間に発生したコンバージョンのみを表示します。

{% alert note %}
ユーザーがキャンバスに再エントリした場合、コンバージョンイベントは最新のエントリに対してのみトラッキングされます。コンバージョンイベントがバックフィルされた場合でも、以前のエントリに対してはコンバージョンイベントは記録されません。
{% endalert %}

{% details 例を展開 %}

**例1**

10件のプッシュ通知を含むキャンバスパスがあり、コンバージョンイベントが「セッション開始」（「アプリを開く」）の場合：

- ユーザーAは、エントリ後、最初のメッセージを受信する前にアプリを開きます。
- ユーザーBは、各プッシュ通知の後にアプリを開きます。

**結果：** サマリーには2件のコンバージョンが表示されますが、個々のステップでは最初のステップで1件のコンバージョンが表示され、それ以降のすべてのステップでは0件になります。

{% alert note %}
コンバージョンイベントが発生した時点でサイレント時間が有効な場合も、同じルールが適用されます。
{% endalert %}

**例2**

サイレント時間が有効な1ステップのキャンバスの場合：

1. ユーザーがキャンバスにエントリします。
2. 最初のステップには遅延がありませんが、設定されたサイレント時間内にあるため、メッセージは抑制されます。
3. ユーザーがコンバージョンイベントを実行します。

**結果：** ユーザーはキャンバスバリアント全体ではコンバージョンとしてカウントされますが、ステップを受信していないため、ステップではカウントされません。

{% enddetails %}

### 異なるコンバージョン率タイプの違いは何ですか？ {#whats-the-difference-between-the-different-conversion-rate-types}

- キャンバス全体のコンバージョンは、コンバージョンイベントを完了したユニークユーザー数を反映しており、各ユーザーが完了したコンバージョン数ではありません。
- バリアントのコンバージョン率またはキャンバスの冒頭にあるサマリーブロックは、メッセージを受信したかどうかに関係なく、そのパス内でユーザーが実行したすべてのコンバージョンの合計を反映します。
- ステップのコンバージョン率は、そのメッセージステップを受信し、指定されたコンバージョンイベントのいずれかを完了した個人の数を反映します。

### キャンバスステップのコンバージョン率がキャンバスバリアントの合計コンバージョン率と等しくないのはなぜですか？ {#why-is-my-canvas-step-conversion-rate-not-equal-to-my-canvas-variant-total-conversion-rate}

キャンバスバリアントのコンバージョン合計がステップ合計の合算より大きくなることはよくあります。これは、ユーザーがバリアントにエントリするとすぐにそのバリアントのコンバージョンイベントを実行できるためです。ただし、同じコンバージョンイベントはキャンバスステップにはカウントされません。そのため、キャンバスにエントリし、最初のキャンバスステップを受信する前にコンバージョンイベントを実行したユーザーは、バリアントのコンバージョン合計にはカウントされますが、ステップ合計にはカウントされません。キャンバスにエントリしたが、いずれのステップも受信する前にキャンバスを離脱したユーザーについても同様です。

また、ユーザーがバリアントにエントリし、ステップからメッセージを送信されず、その後コンバージョンする可能性もあります。この場合、コンバージョンはステップレベルでは記録されません。ただし、ユーザーは技術的にはコンバージョンしたため、キャンバスレベルではコンバージョンが記録されます。

### APIトリガーのキャンバスをユーザーが受信したことを確認するにはどうすればよいですか？ {#how-can-i-confirm-if-my-users-received-an-api-triggered-canvas}

キャンバスフィルターを使用して[セグメントを作成]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)し、ユーザーがキャンバスにエントリしたか、特定のキャンバスステップを受信したかを確認できます。たとえば、ユーザーがAPIトリガーのキャンバスにエントリしたことを確認したい場合はキャンバスエントリフィルターを使用し、キャンバスからメッセージを受信したことを確認したい場合は受信ステップフィルターを使用します。その後、[`/users/export/segment`エンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)を使用して、そのセグメント内のユーザーをエクスポートできます。

### キャンバスを削除できますか？ {#can-i-delete-a-canvas}

いいえ。ただし、[キャンバスをアーカイブ]({{site.baseurl}}/user_guide/messaging/governance/archiving)することは可能です。

### アーカイブされたキャンバスやキャンペーンを再開するにはどうすればよいですか？ {#how-do-i-resume-an-archived-canvas-or-campaign}

アーカイブされたメッセージは、編集可能な状態に戻すまで送信されません。キャンペーンまたはキャンバスを[アーカイブ解除]({{site.baseurl}}/user_guide/messaging/governance/archiving#unarchiving)し、エントリスケジュールまたは送信時間を将来の期間に設定するか（クリーンコピーが必要な場合はジャーニーを複製してください）、必要に応じて**再開**またはローンチします。[キャンペーンとキャンバスのアーカイブ]({{site.baseurl}}/user_guide/messaging/governance/archiving)を参照してください。

### エラーが表示されないのにキャンバスが保存されないのはなぜですか？ {#why-doesnt-my-canvas-save-when-no-error-appears}

オーディエンスまたはステップレベルのフィルターに空の**カスタム属性**フィルターがあると、詳細なバリデーションメッセージなしに保存がブロックされることがあります。各フィルターカードを開き、不完全なカスタム属性ルールを削除するか、属性名と値の両方を入力してから、もう一度**保存**を選択してください。

### キャンバスやキャンペーンからタグが消えたのはなぜですか？ {#why-did-a-tag-disappear-from-my-canvas-or-campaign}

ワークスペースから[タグ]({{site.baseurl}}/user_guide/messaging/governance/tags)が削除されると、Brazeはそのタグを参照していたすべてのキャンペーンとキャンバスからそのタグを削除します。このクリーンアップは、キャンバスの変更ログに独自の行を生成するとは限りません。

### 各キャンバスコンポーネントの分析を表示するにはどうすればよいですか？ {#how-can-i-view-analytics-for-each-of-my-canvas-components}

キャンバスコンポーネントの分析を表示するには、キャンバスに移動し、**キャンバスの詳細**ページを下にスクロールします。ここで、各コンポーネントの分析を確認できます。詳細については、[キャンバス分析]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics)を参照してください。

### キャンバスステップからのエンゲージメントがユーザープロファイルに表示されるのはいつですか？ {#when-is-engagement-from-a-canvas-step-visible-on-a-user-profile}

`Received Message from キャンバス Step`などのフィルターは、Brazeがそのステップに対応する送信、受信、またはエンゲージメントイベントを記録した後に更新されます。アプリ内メッセージは、送信スタイルの指標とは別にインプレッションを記録する場合があります。[インプレッションが記録されているのに、キャンバスで送信数がゼロと表示されるのはなぜですか？](#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged)を参照してください。これらの同じイベントは、**キャンバスの詳細**のステップ指標に表示されます。

### ユニークユーザー数を確認する場合、キャンバス分析とセグメンターのどちらがより正確ですか？ {#when-looking-at-the-number-of-unique-users-is-canvas-analytics-or-the-segmenter-more-accurate}

セグメンターは、キャンバスやキャンペーンの統計と比較して、ユニークユーザーデータのより正確な統計です。これは、キャンバスやキャンペーンの統計が、何かが発生した際にBrazeがインクリメントする数値であるためであり、この数値がセグメンターの数値と異なる結果になる変数が存在する可能性があります。たとえば、ユーザーはキャンバスやキャンペーンに対して複数回コンバージョンする場合があります。

### キャンバスにエントリするユーザー数が予想と一致しないのはなぜですか？ {#why-does-the-number-of-users-entering-a-canvas-not-match-the-expected-number}

キャンバスにエントリするユーザー数が予想と異なる場合があります。これは、オーディエンスとトリガーの評価方法によるものです。Brazeでは、オーディエンスはトリガーの前に評価されます（[属性値の変更]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)トリガーを使用する場合を除く）。そのため、トリガーアクションが評価される前に、選択したオーディエンスに含まれていないユーザーはキャンバスから除外されます。

### キャンバスジャーニー中の匿名ユーザーはどうなりますか？ {#what-happens-to-anonymous-users-during-their-canvas-journey}

匿名ユーザーはキャンバスにエントリおよび離脱できますが、識別されるまではそのアクションは特定のユーザープロファイルに関連付けられないため、分析でインタラクションが完全にトラッキングされない場合があります。[クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder)を使用して、これらの指標のレポートを生成できます。

{% alert tip %}
キャンバスのトラブルシューティングに関するさらなるサポートが必要な場合は、問題発生から30日以内にBrazeサポートに連絡してください。診断ログは過去30日分のみ保持されています。
{% endalert %}

### 現在キャンバスジャーニー中のユーザーをキャンペーンやセグメントから除外できますか？ {#can-i-exclude-users-who-are-currently-in-a-canvas-journey-from-a-campaign-or-segment}

`Entered キャンバス Variation`、`In キャンバス Control Group`、`Received Message from キャンバス Step`などの[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)を使用して、キャンバスのエントリ、バリアント割り当て、またはステップエンゲージメントに基づいてユーザーをターゲティングできます。これらのフィルターはエントリ履歴とインタラクションを評価するもので、ユーザーがアクティブなジャーニーをまだ進行中かどうかを示すものではありません。

アクティブなキャンバス参加状況に基づいてユーザーを含めたり除外したりするには、キャンバスのエントリおよび離脱時に[ユーザー更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)ステップを追加してカスタム属性を設定およびクリアし、キャンペーンやセグメントでそれらの属性に基づいてフィルタリングします。

## セグメンテーション {#segmentation}

### 「キャンバスバリエーションに入っていない」と「キャンバスコントロールグループに属していない」の違いは何ですか？ {#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group}

フィルターの完全な定義については、[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)を参照してください。

#### キャンバスバリエーションに入っていない {#has-not-entered-canvas-variation}

ユーザーが特定のキャンバスのバリエーションパスに一度も入っていないことを意味します。コントロールグループに属していないすべてのユーザーが含まれ、キャンバスに入ったかどうかは問いません。これには、別のバリエーションに入ったユーザーや、どのバリエーションにも入っていないユーザーが含まれます。

#### キャンバスコントロールグループに属していない {#is-not-in-canvas-control-group}

ユーザーがキャンバスに入ったが、コントロールグループには属しておらず、結果としてバリエーションを受信したことを意味します。これにはキャンバスに入ったユーザーのみが含まれます。

バリエーションの割り当てはキャンバスへのエントリ時に行われます。ユーザーがキャンバスに入っていない場合、バリアントは割り当てられません。つまり、コントロールグループにもバリアントにも属しません。

## オリジナルキャンバスエディター {#original-canvas-editor}

{% details オリジナルキャンバスエディターのFAQを展開する %}

### 既存のキャンバスをオリジナルエディターから現在のエディターに変換するにはどうすればよいですか？ {#how-do-i-convert-an-existing-canvas-from-the-original-editor-to-the-current-editor}

[キャンバスを複製]({{site.baseurl}}/cloning_canvases)できます。これにより、最新のキャンバスワークフローでオリジナルキャンバスのコピーが作成されます。

### 現在のキャンバスエディターとオリジナルキャンバスエディターの主な違いは何ですか？ {#what-are-the-main-differences-between-the-current-and-original-canvas-editors}

#### キャンバスコンポーネントツールバー {#canvas-component-toolbar}

以前のオリジナルキャンバスエディターでは、ユーザージャーニーにステップを作成するたびに、デフォルトでフルステップが追加されていました。これらのフルステップは異なるキャンバスコンポーネントに置き換えられ、編集時の可視性とカスタマイズ性が向上しています。キャンバスステップツールバーからすべてのキャンバスコンポーネントをすぐに確認できます。

#### ステップの動作 {#step-behavior}

以前は、各フルステップに遅延とスケジュール設定、例外イベント、オーディエンスフィルター、メッセージ設定、メッセージ進行オプションなどの情報がすべて1つのコンポーネントに含まれていました。現在のエディターではこれらが個別の設定になっており、キャンバス構築体験がよりカスタマイズ可能になり、機能面でもいくつかの違いがあります。

#### メッセージコンポーネントの進行 {#message-component-advancement}

[メッセージコンポーネント]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)は、ステップに入ったすべてのユーザーを進行させます。メッセージ進行動作を指定する必要がないため、全体的なステップの設定がシンプルになります。**メッセージ送信時に進行**オプションを実装する場合は、前のステップを受信しなかったユーザーをフィルタリングするために、別のオーディエンスパスを追加してください。

#### 遅延の「〜以内」の動作 {#delay-in-behavior}

[遅延コンポーネント]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)は、次のステップに進む前に遅延時間全体を待機します。

例えば、4月12日に遅延コンポーネントがあり、1日後の午後2時に次のステップにユーザーを送るよう設定されているとします。ユーザーが4月13日の午後2時01分にコンポーネントに入ったとします。
- オリジナルワークフローでは、ユーザーは4月14日の午後2時に次のステップに進みます。これはエントリ時間から1日未満です。
- 現在のエディターでは、ユーザーは4月15日の午後2時に次のステップに進みます。時刻は同じですが、エントリ時間から1日以上経過しています。

#### インテリジェントタイミングの動作 {#intelligent-timing-behavior}

[インテリジェントタイミング]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)はメッセージコンポーネントに格納されるため、遅延はインテリジェントタイミングの計算より前に適用されます。つまり、ユーザーがコンポーネントに入るタイミングによっては、オリジナルキャンバスワークフローで構築されたキャンバスよりもメッセージの受信が遅くなる場合があります。

例えば、遅延が2日に設定されていて、インテリジェントタイミングが有効で、メッセージ送信の最適な時刻が午後2時と判断されたとします。ユーザーが午後2時01分に遅延ステップに入ったとします。
- **現在のワークフロー：**遅延が経過するまで48時間かかるため、ユーザーは3日目の午後2時にメッセージを受信します。
- **オリジナルワークフロー：**ユーザーは2日目の午後2時にメッセージを受信します。

インテリジェントタイミングが有効な場合、メッセージはユーザーがメッセージコンポーネントに入ってから24時間以内に、特定されたインテリジェントな時刻に送信されます（遅延コンポーネントが関与していない場合でも同様です）。

#### 例外イベント {#exception-events}

##### サイレント時間 {#quiet-hours}

例外イベントはアクションパスを使用して適用され、メッセージステップとは別です。サイレント時間はメッセージコンポーネントで適用されます。つまり、ユーザーがすでにアクションパスを通過し（例外イベントで除外されず）、メッセージコンポーネントに到達した時にサイレント時間に遭遇し、サイレント時間終了後にメッセージを再送信するようキャンバスが設定されている場合、例外イベントは適用されなくなります。このユースケースは一般的ではありません。

セグメントとフィルターについては、メッセージステップに配信バリデーションがあり、送信時に検証される追加のセグメントとフィルターを設定できます。これにより、前述のサイレント時間のエッジケースを防ぐことができます。

##### 「〜以内」または「次の〜」スケジュール設定 {#in-or-on-the-next-schedule-setting}

例外イベントはアクションパスを使用して作成されます。アクションパスは「X時間経過後」のみをサポートしており、「X時間以内」や「次のX時間」はサポートしていません。

{% enddetails %}

### 「リクエストタイムアウト」エラーのサポートチケットを送信する際に何を含めるべきですか？ {#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error}

キャンバスの編集中に「リクエストタイムアウト」エラーが発生し、[Brazeサポート]({{site.baseurl}}/braze_support)に連絡する必要がある場合は、解決を迅速化するために以下の情報を含めてください。

{% multi_lang_include messaging/support_ticket_request_timed_out_details.md context='canvas' %}

## キャンバスの配信とトラブルシューティング {#canvas-delivery-and-troubleshooting}

### 孤立したユーザーはキャンバスメッセージを受信できますか？ {#are-orphaned-users-eligible-to-receive-canvas-messages}

いいえ。[孤立したユーザー]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users)はメッセージの受信対象になりません。キャンバスジャーニーの途中でプロファイルが孤立した場合、そのユーザーはフローからサイレントに退出します。分析では、その退出に対して**退出**イベントが常に表示されるとは限らず、ワークフローサマリーには `exited_date` や `exit_reason` のない `partial_update_token` が含まれることがあります。

マージと孤立したプロファイルの詳細については、[重複ユーザーのマージ]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users)を参照してください。

### アクティブなキャンバスやキャンペーンを停止した場合、既にESPに送信されたメッセージは配信されますか？ {#if-i-stop-an-active-canvas-or-campaign-do-messages-already-sent-to-the-esp-still-deliver}

はい。Brazeがメールサービスプロバイダー (ESP) にリクエストを送信した後、Brazeはその送信を取り消すことができません。キャンバスやキャンペーンを停止すると新しい送信リクエストは防止されますが、既にESPに引き渡されたメッセージは引き続き配信される可能性があり、ESPが処理する際に送信カウントが増加することがあります。

これは[キャンバスを停止した場合](#what-happens-when-you-stop-a-canvas)に記載されている動作と同じです。送信中のメールは即座に停止されません。

### ユーザーに表示されるコンテンツがないキャンバスWebhookステップが実行されたことを確認するにはどうすればよいですか？ {#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content}

Brazeは、キャンペーンとキャンバスの[Webhook]({{site.baseurl}}/user_guide/channels/webhooks)ステップについて、Webhookの**送信数**と関連する配信結果を追跡します。ステップ分析、[Webhookレポート](#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content)、または[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)のWebhookイベントを使用して、ステップが実行されたことを確認してください。サーバー側の受信証明が必要な場合は、エンドポイントのリクエストログで追加の確認ができます。

BrazeにはWebhookステップ用の不可視トラッキングピクセルが組み込まれていません。カスタムの1ピクセル画像リクエストではなく、BrazeのWebhookメトリクスとエンドポイントのロギングを利用してください。

### Webhookステップにボディフィールドがないのはなぜですか？ {#why-does-my-webhook-step-have-no-body-field}

Webhookステップは `POST`、`PUT`、`PATCH`、`DELETE` にリクエストボディを使用します。メソッドを `GET` に切り替えると、GETリクエストはリクエストボディをサポートしないため、Brazeはボディフィールドを削除します。JSONやフォームデータを送信する必要がある場合は、ボディをサポートするメソッドに戻してください。メソッドの詳細については、[Webhookを作成する]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#http-method)を参照してください。

### Webhookステップでspacer.gifを使用するにはどうすればよいですか？ {#how-do-i-use-spacergif-in-a-webhook-step}

Brazeは `cdn.braze.com` および `braze-images.com` で `spacer.gif` プレースホルダー画像をホスティングしています。外部エンドポイントを呼び出さずにステップを実行する必要がある場合に、WebhookのURLをこの画像に向けるチームもあります。標準のWebhookステップでは実際のエンドポイントを呼び出すべきです。[WebhookのURLにspacer.gifを使用するにはどうすればよいですか？]({{site.baseurl}}/user_guide/channels/webhooks/reporting)で説明されているように、[Webhookレポート]({{site.baseurl}}/user_guide/channels/webhooks/reporting)とエンドポイントのログを使用して配信を確認してください。

### 「invalid next-step-id」エラーでキャンバスが読み込まれないのはなぜですか？ {#why-wont-my-canvas-load-with-an-invalid-next-step-id-error}

このコンソールエラーは、部分的な削除、複製、またはインポート後などに、少なくとも1つのステップが欠落しているか無効な次のステップを参照していることを意味します。エディターでキャンバスを開き、孤立したステップを再接続するか、有効なダウンストリームパスがなくなったステップを削除してください。それでもキャンバスが読み込まれない場合は、キャンバスIDとコンソールエラーのスクリーンショットを添えて[Brazeサポート]({{site.baseurl}}/braze_support)に連絡してください。

### Currentsのキャンバスコンバージョンタイムスタンプがキャンバス分析と異なるのはなぜですか？ {#why-does-a-canvas-conversion-timestamp-in-currents-differ-from-my-canvas-analytics}

Currentsはキャンバスのコンバージョンを[`users.canvas.Conversion`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#canvas-conversion-events)イベントとして記録します。イベントの `time` はコンバージョンイベントが発生した時刻です。そのイベントの `conversion_behavior` フィールドはコンバージョンの定義（タイプとウィンドウ）を記述します。キャンバス分析では、コンバージョンウィンドウ内のキャンバスエントリを基準にコンバージョンを集計することもあります。エクスポートを照合する場合は、Currentsの `time` をコンバージョンイベントのタイムスタンプとキャンバスのコンバージョンウィンドウ設定と比較してください。

### Currentsで `canvas_step_name` がnullになるのはなぜですか？ {#why-is-canvas_step_name-null-in-currents}

`canvas_step_name` などのキャンペーンおよびキャンバスの名前フィールドは、ステップの作成や名前変更の直後など、Brazeがステップメタデータの伝播を完了する前にCurrentsイベントが送信された場合に `null` になることがあります。詳細については、[Currentsデータでキャンペーン名やキャンバスステップ名がNULLになるのはなぜですか？]({{site.baseurl}}/user_guide/data/distribution/braze_currents/faq#why-is-the-campaign-name-or-canvas-step-name-null-in-my-currents-data)を参照してください。

### ユーザー更新ステップで配列が更新されないのはなぜですか？ {#why-isnt-my-array-updating-in-a-user-update-step}

[ユーザー更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)ステップのJSONを確認してください。配列やネストされた属性の更新には、変更する属性に対する有効なパスと値が必要です。外部ユーザーIDなど、ステップが自動的に提供するフィールドは含めないでください。起動前にステップの**プレビューとテスト**タブを使用してペイロードを確認してください。

### `external_id` のないユーザーにキャンバスメッセージを送信できますか？ {#can-i-send-canvas-messages-to-users-without-an-external_id}

はい。Brazeのユーザープロファイルが既に存在していれば可能です。`external_id` のないユーザーは[匿名ユーザー]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles)であり、`braze_id` または[ユーザーエイリアス]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases)で参照できます。キャンバスエントリの前に、[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)またはSDKでプロファイルを作成または更新し、[アクションベースまたはAPIトリガーのエントリ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule)を使用してください。標準のキャンバスターゲティングにはBrazeユーザープロファイルが必要です。プロファイルのないメールアドレスだけではキャンバスメッセージを送信できません。

### トリガーイベントの実行回数よりもユーザーのキャンバスへのエントリ回数が少ないのはなぜですか？ {#why-did-a-user-enter-a-canvas-fewer-times-than-they-performed-the-trigger-event}

アクションベースおよびAPIトリガーのキャンバスでは、Brazeはトリガーイベントを重複排除し、同じキャンバスに対してユーザーが**1秒あたり最大約1回**しかエントリできないようにしています。ユーザーが1秒以内に同じトリガーを複数回実行した場合、1つのエントリのみが処理されます。

同じ秒内に複数のエントリを許可するには、トリガーイベントの間隔を少なくとも1.1秒空けてください（たとえば、サーバー側でイベントのタイミングを制御している場合）。同じ秒内の複数のトリガーを許可するキャンペーンスタイルの動作については、適切なスケジューリングと再エントリ設定を持つ[キャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns)とユースケースを比較してください。

### APIトリガーのキャンバスでユーザーはいつ重複排除されますか？ {#when-are-users-de-duplicated-in-api-triggered-canvases}

ユーザーがAPIトリガーのキャンバスに再エントリし、前回のエントリで同一のメッセージのためにすでにキューに入っているディレイステップに到達した場合、Brazeは重複送信を防ぐためにユーザーを重複排除します。2番目のキャンバスインスタンスは退出するため、エントリ数が送信数を超えることがあります。

### テストプッシュが間違ったアプリに届くのに、ライブ送信は正しく見えるのはなぜですか？ {#why-does-a-test-push-go-to-the-wrong-app-but-live-sends-look-correct}

ユーザープロファイルの**テストプッシュ**は、そのプロファイルのプッシュ有効なすべてのデバイスに配信されます。デバイスに複数のアプリがインストールされている場合、OSは通常、最初に利用可能なアプリにテスト通知を配信しますが、それは検証したいアプリとは異なる場合があります。

アプリ固有のターゲティングを確認するには、プロファイルの**テストプッシュ**だけに頼るのではなく、狭いオーディエンス（たとえば `external_id` でフィルター）を使用して、キャンペーンまたはキャンバス経由でライブまたはテストメッセージを送信してください。

複数のアプリを持つ**キャンバス**のメッセージステップでは、メッセージステップの**送信時にオーディエンスを検証**をオンにして、送信時にセグメントとフィルターのチェックが実行されるようにします。詳細については、[メッセージステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)を参照してください。

一般的なテストプッシュの動作については、[テストメッセージの送信]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages)と[プッシュ通知FAQ]({{site.baseurl}}/user_guide/channels/push/faqs)を参照してください。

### iOSとAndroidでPush Storiesをデバッグするにはどうすればよいですか？ {#how-do-i-debug-push-stories-on-ios-and-android}

セットアップとクリエイティブの要件については、[Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories)を参照してください。実装とリッチプッシュ通知の処理については、開発者ガイドの[リッチプッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/rich)と[Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories)を参照してください。

### 「キャンバスメッセージが24時間以上遅延」メールは誰に届きますか？ {#who-receives-the-canvas-messages-delayed-24-hours-email}

Brazeは、キャンバスメッセージがレート制限により24時間以上遅延した場合にこの通知を送信します。メールは、影響を受けたキャンバスに以前変更を加えたダッシュボードユーザー（キャンバスの変更ログに基づく）に送信されます。Brazeがこれらの受信者を特定できない場合、メールはワークスペースの**会社管理者**に送信されます。

### 例外イベント後、ユーザーはいつメッセージの受信を停止しますか？ {#when-does-a-user-stop-receiving-messages-after-an-exception-event}

Brazeは例外イベントが発生した時点で退出を記録しますが、タイマーが終了するまでユーザーがステップ内に残ることがあります。これはディレイステップで最も顕著です。スケジュールされたステップとイベントトリガーのステップでは動作も異なります。タイムライン、例、分析上の注意点については、[退出条件]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria)を参照してください。

### リンクエイリアスのインタラクションを選択したときにアクションパスステップでエラーが表示されるのはなぜですか？ {#why-does-my-action-paths-step-show-an-error-when-i-select-a-link-alias-interaction}

メールのインタラクティビティトリガー（たとえば、**メール内のエイリアスをクリック**や**任意のキャンペーンまたはキャンバスステップでエイリアスをクリック**）を使用するアクショングループには、そのリンクを含むメッセージを既に送信したメッセージステップが必要です。メールがアクションパスステップでクリックを評価する前に送信されるように、ステップを追加または並べ替えるか、ユーザーがこのキャンバスで既に受信したメッセージに一致するインタラクションを選択してください。インタラクショントリガーの完全なリストについては、[アクションベースの配信]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)を参照してください。

### 過去のカスタムイベントのタイムスタンプはアクションベースのキャンバスやキャンペーンにどのように影響しますか？ {#how-do-historical-custom-event-timestamps-affect-action-based-canvases-and-campaigns}

Brazeは、適格なイベントが取り込まれ、ユーザーがオーディエンスルールを満たしたときにアクションベースのジャーニーを評価します。キャンバスやキャンペーンがアクティブだったウィンドウ外でイベントがプロファイルに到着した場合、またはユーザーがオーディエンスに一致する前にイベントが到着した場合、エントリやダウンストリームの送信が期待どおりに行われないことがあります。ユーザープロファイルのアクティビティログと[カスタムイベントのトラブルシューティング]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#troubleshooting-custom-events)のトラブルシューティング手順を使用して、イベントのタイムスタンプを公開時刻とセグメントメンバーシップと比較してください。動作が期待と一致しない場合は、[Brazeサポート]({{site.baseurl}}/braze_support)に連絡してください。