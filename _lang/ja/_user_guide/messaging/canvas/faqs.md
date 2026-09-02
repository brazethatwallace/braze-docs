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

キャンバスには最大200ステップまで追加できます。

### キャンバスエントリプロパティにサイズ制限はありますか？ {#are-there-size-limits-for-canvas-entry-properties}

はい。[キャンバスコンテキストオブジェクト]({{site.baseurl}}/api/objects_filters/context_object)（キャンバスエントリプロパティ）の最大サイズは50&nbsp;KBです。その制限内でペイロードをできるだけ小さく保ってください。キャンバスでのエントリプロパティとイベントプロパティの動作については、[コンテキストとイベントプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)を参照してください。

### 「Too many キャンバス branches」エラーが表示されるのはなぜですか？ {#why-do-i-see-a-too-many-canvas-branches-error}

このエラーは、ステップの分岐とエントリオーディエンスのサイズの組み合わせにより、クラスターのパフォーマンスに問題が発生し、メッセージの送信が妨げられる可能性がある場合に表示されます。解決手順（[オーディエンスパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)の使用、分岐やオーディエンスサイズの削減、キャンバスフローでの再構築など）については、[「Too many キャンバス branches」エラー]({{site.baseurl}}/user_guide/messaging/canvas/troubleshooting#too-many-canvas-branches-error)を参照してください。

### キャンバスで再適格性を有効にしてBrazeAI<sup>TM</sup>で最適化を使用できますか？ {#can-i-use-optimize-with-brazeai-with-re-eligibility-in-a-canvas}

はい。キャンバスでは、再適格性が有効な場合に[BrazeAI<sup>TM</sup>で最適化]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai)を使用できます。Brazeは、割り当てが時間の経過とともに変化するため、再エントリ時に同じバリアントを保証することはできません。キャンペーンでは、**BrazeAI<sup>TM</sup>で最適化**が有効な場合、再適格性のウィンドウが24時間以上必要です。

### コンポーネントとステップの違いは何ですか？ {#whats-the-difference-between-a-component-and-a-step}

[コンポーネント]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about)は、キャンバスの効果を判断するために使用できるキャンバスの個別パーツです。コンポーネントには、ユーザージャーニーの分割、ディレイの追加、複数のキャンバスパスのテストなどのアクションを含めることができます。キャンバスのステップとは、キャンバスの分岐におけるパーソナライズされたユーザージャーニーを指します。本質的に、キャンバスはユーザージャーニーのステップを構成する個別のコンポーネントで構成されています。

### 切断されたステップがあるキャンバスをローンチできますか？ {#can-i-launch-a-canvas-with-disconnected-steps}

はい。また、ローンチ後に切断されたステップがあるキャンバスを保存することもできます。

### 切断されたステップに到達したユーザーはどこに行きますか？ {#where-do-users-go-when-theyve-reached-a-disconnected-step}

ユーザーがキャンバスワークフローの切断されたステップにいる場合、後続のステップがあればそのステップに進み、ステップの設定がユーザーの進行方法を決定します。これは、ユーザーがキャンバスの残りの部分に直接接続しなくても、ステップに変更を加えられるようにするためです。これにより、すぐにライブにする前にテストを行うためのスペースも確保でき、実質的に下書きの保存が可能になります。

ステップを切断する前に、キャンバスステップで保留中のユーザーの分析ビューを確認することをお勧めします。

### 1つのバリアントで複数の分岐があるキャンバスで、オーディエンスと送信時間が同一の場合はどうなりますか？ {#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches}

各ステップに対してジョブがキューに入れられ、ほぼ同時に実行され、そのうちの1つが「勝利」します。実際には、ある程度均等に分類される場合がありますが、最初に作成されたステップに少なくとも若干のバイアスがかかる可能性があります。

さらに、その分布がどのようになるかについて正確な保証はできません。均等な分割が必要な場合は、[ランダムバケット番号]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers)フィルターを追加してください。

### キャンバスのオーディエンスはどのように評価されますか？ {#how-are-canvas-audiences-evaluated}

デフォルトでは、キャンバスのフルステップのフィルターとセグメントは送信時に確認されます。条件分岐ステップは、前のステップを受信した直後（またはディレイの前）に評価を実行します。

### 例外イベントはいつトリガーされますか？ {#when-does-an-exception-event-trigger}

例外イベントは、ユーザーが関連付けられたキャンバスコンポーネントの受信を待機している間にのみトリガーされます。ユーザーが事前にアクションを実行した場合、例外イベントはトリガーされません。特定のイベントを事前に実行したユーザーを除外したい場合は、代わりに[フィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)を使用してください。

### キャンバスの編集は、すでにキャンバス内にいるユーザーにどのように影響しますか？ {#how-does-editing-a-canvas-affect-users-already-in-the-canvas}

マルチステップキャンバスの一部のステップを編集した場合、すでにオーディエンスに含まれていたがまだステップを受信していないユーザーは、メッセージの更新バージョンを受信します。ただし、これはまだそのステップの評価が行われていない場合にのみ発生します。

ローンチ後に編集できる内容の詳細については、[ローンチ後のキャンバスの変更]({{site.baseurl}}/post-launch_edits)を参照してください。

### キャンバスを停止するとどうなりますか？ {#what-happens-when-you-stop-a-canvas}

キャンバスを停止すると、以下が適用されます。

- ユーザーはキャンバスへのエントリが阻止されます。
- フロー内のユーザーの位置に関係なく、それ以上のメッセージは送信されません。
- **例外：**メールを含むキャンバスはすぐには停止しません。送信リクエストがSendGridに送信された後は、ユーザーへの配信を停止するためにできることはありません。

### 1つのキャンバスを構築すべきですか、それともユーザーライフサイクルごとに別々のキャンバスを構築すべきですか？ {#should-i-build-one-canvas-or-separate-canvases-per-user-lifecycle}

キャンバスで達成したい目標に応じて、ユーザージャーニーの構築方法に異なるアプローチが必要になる場合があります。キャンバスの柔軟性により、ユーザーライフサイクルのあらゆる段階でユーザージャーニーをマッピングできます。効果的なユーザージャーニーを作成するための合理化されたアプローチの例については、[Brazeキャンバステンプレート]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates)をご覧ください。

## メッセージと配信 {#messages-and-delivery}

### キャンバスのアプリ内メッセージはいつ送信されますか？ {#when-are-in-app-messages-in-canvas-sent}

アプリ内メッセージは、次のセッション開始時に送信されます。つまり、キャンバスが停止される前にユーザーがキャンバスステップに入った場合、アプリ内メッセージがまだ期限切れになっていなければ、次のセッション開始時にアプリ内メッセージを受信します。

キャンバスが停止される前にユーザーがセッションを開始していても、アプリ内メッセージがすぐに表示されない場合があります。これは、アプリ内メッセージがカスタムイベントによってトリガーされる場合や、遅延が設定されている場合に発生する可能性があります。つまり、キャンバスが停止された後にユーザーがアプリ内メッセージのインプレッションを記録し、アプリ内メッセージを「受信」する可能性があります。ただし、ユーザーはキャンバスが停止される前にセッションを開始している必要がありますが、キャンバスステップを受信した**後**である必要があります。

{% alert note %}
キャンバスを停止しても、メッセージの受信を待っているユーザーはユーザージャーニーから退出しません。キャンバスを再度有効にした場合、ユーザーがまだメッセージを待っていれば、メッセージを受信します（ただし、メッセージが送信されるべき時間が過ぎている場合は受信しません）。
{% endalert %}

### キャンバスでインプレッションが記録されているのに、送信数がゼロと表示されるのはなぜですか？ {#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged}

アプリ内メッセージステップを含むキャンバスで*メッセージ送信数*が常にゼロの場合、これはアプリ内メッセージの配信が他のメッセージングチャネルとは異なる仕組みで動作するためです。

アプリ内メッセージは、Brazeから「プッシュ」されるのではなく、SDKによって「プル」されます。対象ユーザーへのアプリ内メッセージは、セッション開始時に自動的に配信され、トリガーイベントが発生するまで表示を「待機」します。対象ユーザーはセッション開始時にメッセージを受信するため、Brazeはこれを送信イベントとして報告しません。ユーザーがトリガーイベントを実行すると、メッセージが表示され、Brazeはインプレッションを記録し、ユーザープロファイル上でキャンバスステップ（またはキャンペーン）を受信済みとしてマークします。そのため、アプリ内メッセージの*送信数*の合計はゼロになります。

### 長い遅延やブランチの後にユーザーがアプリ内メッセージを受信しなかったのはなぜですか？ {#why-didnt-users-receive-my-in-app-message-after-a-long-delay-or-branch}

上流の[遅延]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)ステップとオーディエンスチェックが完了した後、ユーザーはメッセージステップに到達した時点でアプリ内メッセージの対象となります。メッセージがカレンダー日付または**ステップが利用可能になった後の短い期間**で期限切れになる場合、遅いブランチのユーザーは期限切れ後に到達し、メッセージを見ることができない可能性があります。期限切れを最も長い現実的なパス遅延に合わせてください。詳細と例については、[アプリ内メッセージの有効期限]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas#in-app-message-expiration)を参照してください。

### 「キャンバス Entry Properties may not be used in In-App Messages.」と表示されるのはなぜですか？ {#why-do-i-see-canvas-entry-properties-may-not-be-used-in-in-app-messages}

このメッセージは、パーソナライゼーションがキャンバスのアプリ内メッセージでは解決できないフィールドを参照している場合に表示されます。[コンテキストとイベントプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)および[メッセージステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)に記載されている`context`オブジェクトを使用してください。レガシーのLiquid名前空間`canvas_entry_properties`には、`context`とは異なる制約があります。複数のステップにわたって値を保持する必要がある場合は、Brazeチームと[元のキャンバスエディターでの永続プロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties)を確認してください。保存された値は、デバイスがアプリ内ペイロードをダウンロードする前にユーザーがキャンバスを退出すると消去されます。

### キャンバスのドラッグ＆ドロップアプリ内メッセージのボタンクリックはどこで確認できますか？ {#where-can-i-find-button-clicks-for-drag-and-drop-in-app-messages-in-canvas}

ドラッグ＆ドロップアプリ内メッセージのボタンレベルの指標は、**キャンバスの詳細**内の**メッセージ**ステップ分析カードに表示されます。キャンバスの概要レベルだけではありません。キャンバスを開き、メッセージステップを選択し、そこでアプリ内エンゲージメントを確認してください。レポートの概念については、[キャンバス分析による測定とテスト]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics)を参照してください。

### 同じキャンバスメッセージステップまたは多変量送信で、バリアントごとに異なる送信時間をスケジュールできますか？ {#can-i-schedule-different-send-times-for-each-variant-in-the-same-canvas-message-step-or-multivariate-send}

いいえ。同じ多変量構成またはメッセージステップ内のバリアントは、1つの配信スケジュールを共有します。同じスケジュール送信に対して、あるバリアントを午後6時に、別のバリアントを午後7時に送信するよう割り当てることはできません。

送信をずらしたり、パスごとに異なる時間を使用するには、以下の方法を試してください。

- メッセージステップの間に遅延ステップを挟んで分離し、各メッセージに独自のスケジュールを持たせます。
- ブランチまたは[テストパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)ステップを使用して、ユーザーが異なるタイミングのパスをたどるようにします。
- ユースケースが1つのキャンバス内に留まる必要がない場合は、個別のキャンペーンを使用します。

キャンペーンでの多変量およびABテストの概念については、[多変量およびABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。

### キャンバスメッセージステップでユーザーがグローバルフリークエンシーキャップに達した場合はどうなりますか？ {#what-happens-if-a-user-is-global-frequency-capped-at-a-canvas-message-step}

キャップされたチャネルについてはその送信を受信しませんが、グローバルフリークエンシーキャップによりメッセージが送信されなかった場合でも、メッセージステップはユーザーを進行させます。ステップごとの進行ケースについては、[ユーザーの進行方法]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance)を参照してください。グローバルフリークエンシーキャップだけではユーザーをキャンバスから退出させません。この動作はメッセージステップの**配信バリデーション**とは別のものです。詳細については、[レート制限とフリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)を参照してください。

### 送信数が推定オーディエンスサイズより少ないのはなぜですか？ {#why-are-sends-lower-than-the-estimated-audience-size}

送信数が**推定オーディエンス**より少なくなる理由は、[キャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size)と同じ理由が多く含まれます。フリークエンシーキャップ、厳密なデバイスまたはブラウザフィルター、再エリジビリティウィンドウ、レート制限、チャネルレベルの除外（例えば、プッシュ到達可能性やメール購読と配信可能性のチェック）などです。

キャンバス固有の要因も影響します。

- **アクションベースまたはAPIトリガーエントリ:** ユーザーはエントリ行動を実行した後にのみエントリ（およびステップを受信）するため、実際の送信数はそれらのアクションが発生するまで事前の推定を下回ります。
- **オーディエンスパス:** ユーザーは条件を満たす最も優先度の高いブランチにルーティングされるため、下流のブランチはフラットなセグメント数が示すよりも少ないユーザーを受信する可能性があります。
- **オーディエンスと送信時のチェック:** フルステップは、別途設定しない限り送信時にフィルターを再評価します。キャンバスが作成された時点で条件を満たしていたユーザーが、メッセージ送信前に脱落する可能性があります。
- **コントロールグループ:** グローバルまたはキャンバスのコントロールグループは、エントリしたユーザーの一部をメッセージングから除外します。
- **クワイエットアワーと遅延:** メッセージが保留またはリスケジュールされ、閲覧中のレポートウィンドウから送信がずれる可能性があります。
- **最大エントリまたはオーディエンスキャップ:** エントリまたは送信キャップにより、基盤となるセグメントが大きくても追加のユーザーが制限されます。
- **レポートウィンドウ:** 分析の範囲に、推定と比較しているすべての送信が含まれていない場合があります。

### 推定オーディエンスとキャンバスユーザー数が一致しないのはなぜですか？ {#why-dont-estimated-audience-and-canvas-user-counts-match}

**推定オーディエンス**は、推定が実行された時点でセグメントとエントリフィルターに一致するユーザーを反映します。その後、遅延またはアクションベースのエントリ、再エリジビリティ、APIトリガー、またはブランチルーティングにより、スナップショットと比較してジャーニーに触れるプロファイルの数が増加する可能性があります。また、送信時のフィルターが失敗するとユーザーが脱落し、実際のエントリまたは送信数が減少します。タイミング、キャップ、評価設定を[送信数が推定オーディエンスサイズより少ないのはなぜですか？](#why-are-sends-lower-than-the-estimated-audience-size)と合わせて比較してください。

### *ユニーク受信者*がターゲットしたユーザー数より多いのはなぜですか？ {#why-is-_unique-recipients_-higher-than-the-number-of-users-i-targeted}

*ユニーク受信者*は、Brazeがキャンバスおよびキャンペーンレポートで**日別のユニーク受信者**をトラッキングするため、想定したオーディエンスよりも多くなることがあります。これは、ユーザーがジャーニー内でメッセージを受信するたびに正確なコンバージョンアトリビューションを行うためです。

例えば、あるユーザーが月曜日にキャンバスステップを受信し、金曜日に再度受信して、それぞれの送信後にコンバージョンした場合、Brazeは2つの受信者行と2つのスコープ内コンバージョンをカウントできます。定期的なエントリや再エリジビリティにより、同じ少数のプロファイルセットが数日間にわたって複数の*ユニーク受信者*を生成する可能性があります。

### キャンバスの送信率が低下しているのはなぜですか？ {#why-is-my-canvas-experiencing-lower-send-rates}

日次スケジュールのキャンバスが時間の経過とともに送信ユーザー数が減少している場合、以下を確認してください。

- **再エリジビリティが有効になっているか確認する:** 再エリジビリティがない場合、Brazeは各ユーザーをキャンバスに一度だけエントリさせます。日次スケジュールのキャンバスでは、オーディエンスに一致し、まだキャンバスにエントリしていないユーザーのみが各エントリの対象となります。より多くのユーザーがエントリするにつれて、後のエントリでは対象ユーザーが少なくなるため、エントリ量が減少します。
- **オーディエンスが固定メンバーシップかどうか確認する:** 固定ユーザーリスト（セグメントフィルターとして使用された[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)など）から構築されたオーディエンスは、自動的に新しいメンバーを獲得しません。新しいエントリユーザーがいなければ、ユーザーがキャンバスにエントリするにつれてエントリ量が回復することはありません。

[配信速度のレート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting)および単一オカレンスの送信数を減少させるその他の要因については、[送信数が推定オーディエンスサイズより少ないのはなぜですか？](#why-are-sends-lower-than-the-estimated-audience-size)を参照してください。

### 小さなコントロールグループセグメントの履歴メンバーシップが変動するのはなぜですか？ {#why-does-a-small-control-group-segment-show-changes-in-historical-membership}

履歴メンバーシップチャートは推定サンプルを使用するため、小さなセグメント（[グローバルコントロールグループ]({{site.baseurl}}/user_guide/audience/global_control_group)セグメントを含む）は、基盤となるオーディエンスが安定していても日々の変動を示すことがあります。推定の仕組みとチャートが変動する理由については、[履歴セグメントメンバーシップサイズの表示]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#viewing-historical-segment-membership-size)を参照してください。

## 分析とコンバージョン {#analytics-and-conversions}

### コンバージョンダッシュボードはキャンバスのコンバージョンをどのようにアトリビューションしますか？ {#how-does-the-conversions-dashboard-attribute-canvas-conversions}

[コンバージョンダッシュボード]({{site.baseurl}}/user_guide/analytics/dashboards/conversions)は、選択した[アトリビューション方法]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#attribution-methods)（例：**受信時**、**送信時**、**開封時**、**クリック時**）に基づいてキャンバスのコンバージョンをアトリビューションします。ユーザーがレポートに表示されるには、キャンバスまたはキャンペーンにエントリし、選択したアトリビューション方法を記録し、レポート設定内でコンバージョンイベントを実行する必要があります。

キャンバス分析におけるステップレベルおよびバリアントレベルのコンバージョンルールについては、[キャンバスでユーザーのコンバージョンはどのようにトラッキングされますか？](#how-are-user-conversions-tracked-in-a-canvas)を参照してください。

### キャンバスでユーザーのコンバージョンはどのようにトラッキングされますか？ {#how-are-user-conversions-tracked-in-a-canvas}

ユーザーはキャンバスのエントリごとに1回だけコンバージョンできます。コンバージョンは、そのエントリでユーザーが受信した最新のメッセージに割り当てられます。キャンバスの先頭にある概要ブロックには、メッセージを受信したかどうかに関係なく、そのパス内のユーザーが実行したすべてのコンバージョンが反映されます。後続の各ステップには、そのステップがユーザーの最後に受信したステップであった間に発生したコンバージョンのみが表示されます。

{% alert note %}
ユーザーがキャンバスに再エントリした場合、コンバージョンイベントは最新のエントリに対してのみトラッキングされます。コンバージョンイベントがバックフィルされた場合でも、以前のエントリに対してはコンバージョンイベントは記録されません。
{% endalert %}

{% details 例を展開 %}

**例1**

10件のプッシュ通知を含むキャンバスパスがあり、コンバージョンイベントが「セッション開始」（「アプリを開く」）の場合：

- ユーザーAはエントリ後、最初のメッセージを受信する前にアプリを開きます。
- ユーザーBは各プッシュ通知の後にアプリを開きます。

**結果:** 概要には2件のコンバージョンが表示されますが、個別のステップでは最初のステップで1件のコンバージョンが表示され、後続のすべてのステップではゼロになります。

{% alert note %}
コンバージョンイベントが発生した時点でサイレント時間帯がアクティブな場合でも、同じルールが適用されます。
{% endalert %}

**例2**

サイレント時間帯が有効な1ステップのキャンバスがある場合：

1. ユーザーがキャンバスにエントリします。
2. 最初のステップには遅延がありませんが、設定されたサイレント時間帯内にあるため、メッセージは抑制されます。
3. ユーザーがコンバージョンイベントを実行します。

**結果:** ユーザーはキャンバスバリアント全体ではコンバージョンとしてカウントされますが、ステップを受信していないため、ステップではカウントされません。

{% enddetails %}

### コンバージョン率の種類の違いは何ですか？ {#whats-the-difference-between-the-different-conversion-rate-types}

- キャンバス全体のコンバージョンは、コンバージョンイベントを完了したユニークユーザー数を反映しており、各ユーザーが完了したコンバージョン数ではありません。
- バリアントのコンバージョン率またはキャンバスの先頭にある概要ブロックは、メッセージを受信したかどうかに関係なく、そのパス内のユーザーが実行したすべてのコンバージョンを集計合計として反映します。
- ステップのコンバージョン率は、そのメッセージステップを受信し、設定されたコンバージョンイベントのいずれかを完了した人数を反映します。

### キャンバスのステップコンバージョン率がキャンバスバリアントの合計コンバージョン率と等しくないのはなぜですか？ {#why-is-my-canvas-step-conversion-rate-not-equal-to-my-canvas-variant-total-conversion-rate}

キャンバスバリアントのコンバージョン合計が、そのステップ合計の合算よりも大きくなることはよくあります。これは、ユーザーがバリアントにエントリした時点でバリアントのコンバージョンイベントを実行できるためです。ただし、同じコンバージョンイベントはキャンバスステップにはカウントされません。そのため、キャンバスにエントリし、最初のキャンバスステップを受信する前にコンバージョンイベントを実行したユーザーは、バリアントのコンバージョン合計にはカウントされますが、ステップ合計にはカウントされません。キャンバスにエントリしたがいずれのステップも受信する前にキャンバスを退出したユーザーについても同様です。

また、ユーザーがバリアントにエントリし、ステップからメッセージを送信されず、その後コンバージョンする可能性もあります。この場合、ステップレベルではコンバージョンは記録されません。ただし、ユーザーは技術的にコンバージョンしているため、キャンバスレベルではコンバージョンが記録されます。

### APIトリガーのキャンバスをユーザーが受信したことを確認するにはどうすればよいですか？ {#how-can-i-confirm-if-my-users-received-an-api-triggered-canvas}

キャンバスフィルターを使用して[セグメントを作成]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)し、ユーザーがキャンバスにエントリしたか、特定のキャンバスステップを受信したかを確認できます。例えば、ユーザーがAPIトリガーのキャンバスにエントリしたことを確認するにはキャンバスエントリフィルターを使用し、キャンバスからメッセージを受信したことを確認するにはステップ受信フィルターを使用します。その後、[`/users/export/segment` エンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)を使用して、そのセグメントのユーザーをエクスポートできます。

### キャンバスを削除できますか？ {#can-i-delete-a-canvas}

いいえ。ただし、[キャンバスをアーカイブ]({{site.baseurl}}/user_guide/messaging/governance/archiving)することは可能です。

### アーカイブされたキャンバスやキャンペーンを再開するにはどうすればよいですか？ {#how-do-i-resume-an-archived-canvas-or-campaign}

アーカイブされたメッセージは、編集可能な状態に戻すまで送信されません。キャンペーンまたはキャンバスの[アーカイブを解除]({{site.baseurl}}/user_guide/messaging/governance/archiving#unarchiving)し、エントリスケジュールまたは送信時刻を将来のウィンドウに設定するか（クリーンなコピーが必要な場合はジャーニーを複製してから）、必要に応じて**再開**または起動してください。詳細については、[キャンペーンとキャンバスのアーカイブ]({{site.baseurl}}/user_guide/messaging/governance/archiving)を参照してください。

### エラーが表示されないのにキャンバスが保存されないのはなぜですか？ {#why-doesnt-my-canvas-save-when-no-error-appears}

オーディエンスまたはステップレベルのフィルターで空の**カスタム属性**フィルターがあると、詳細なバリデーションメッセージなしに保存がブロックされることがあります。各フィルターカードを開き、不完全なカスタム属性ルールを削除するか、属性名と値の両方を入力してから、再度**保存**を選択してください。

### キャンバスやキャンペーンからタグが消えたのはなぜですか？ {#why-did-a-tag-disappear-from-my-canvas-or-campaign}

ワークスペースから[タグ]({{site.baseurl}}/user_guide/messaging/governance/tags)が削除されると、Brazeはそのタグを参照していたすべてのキャンペーンとキャンバスからタグを削除します。このクリーンアップは、キャンバスの変更ログに独自の行として常に記録されるわけではありません。

### 各キャンバスコンポーネントの分析を表示するにはどうすればよいですか？ {#how-can-i-view-analytics-for-each-of-my-canvas-components}

キャンバスコンポーネントの分析を表示するには、キャンバスに移動し、**キャンバスの詳細**ページを下にスクロールしてください。ここで、各コンポーネントの分析を表示できます。詳細については、[キャンバス分析]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics)を参照してください。

### キャンバスステップからのエンゲージメントはいつユーザープロファイルに表示されますか？ {#when-is-engagement-from-a-canvas-step-visible-on-a-user-profile}

`Received Message from キャンバス Step` などのフィルターは、Brazeがそのステップに対応する送信、受信、またはエンゲージメントイベントを記録した後に更新されます。アプリ内メッセージは、送信スタイルの指標とは別にインプレッションを記録する場合があります。[キャンバスでインプレッションが記録されているのに送信がゼロと表示されるのはなぜですか？](#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged)を参照してください。同じイベントは**キャンバスの詳細**のステップ指標にも表示されます。

### ユニークユーザー数を見る場合、キャンバス分析とセグメンターではどちらがより正確ですか？ {#when-looking-at-the-number-of-unique-users-is-canvas-analytics-or-the-segmenter-more-accurate}

セグメンターは、キャンバスやキャンペーンの統計よりもユニークユーザーデータに関してより正確な統計です。これは、キャンバスやキャンペーンの統計は何かが発生した際にBrazeがインクリメントする数値であり、セグメンターの数値とは異なる結果になる可能性のある変数が存在するためです。例えば、ユーザーはキャンバスやキャンペーンに対して複数回コンバージョンすることがあります。

### キャンバスにエントリするユーザー数が予想される数と一致しないのはなぜですか？ {#why-does-the-number-of-users-entering-a-canvas-not-match-the-expected-number}

キャンバスにエントリするユーザー数は、オーディエンスとトリガーの評価方法により、予想される数と異なる場合があります。Brazeでは、オーディエンスはトリガーの前に評価されます（[属性変更]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)トリガーを使用する場合を除く）。これにより、トリガーアクションが評価される前に、選択したオーディエンスに含まれていないユーザーはキャンバスから除外されます。

### キャンバスジャーニー中の匿名ユーザーはどうなりますか？ {#what-happens-to-anonymous-users-during-their-canvas-journey}

匿名ユーザーはキャンバスにエントリしたり退出したりできますが、識別されるまでそのアクションは特定のユーザープロファイルに関連付けられないため、分析でインタラクションが完全にトラッキングされない場合があります。[クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder)を使用して、これらの指標のレポートを生成できます。

{% alert tip %}
キャンバスのトラブルシューティングについてさらに支援が必要な場合は、問題発生から30日以内にBrazeサポートにお問い合わせください。診断ログは過去30日分のみ保持されています。
{% endalert %}

### 現在キャンバスジャーニーにいるユーザーをキャンペーンやセグメントから除外できますか？ {#can-i-exclude-users-who-are-currently-in-a-canvas-journey-from-a-campaign-or-segment}

`Entered キャンバス Variation`、`In キャンバス Control Group`、`Received Message from キャンバス Step` などの[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)を使用して、キャンバスのエントリ、バリアント割り当て、またはステップエンゲージメントに基づいてユーザーをターゲティングできます。これらのフィルターはエントリ履歴とインタラクションを評価するものであり、ユーザーがまだアクティブなジャーニーを進行中かどうかを示すものではありません。

アクティブなキャンバス参加に基づいてユーザーを含めたり除外したりするには、キャンバスのエントリと退出に[ユーザー更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)ステップを追加してカスタム属性を設定およびクリアし、キャンペーンやセグメントでそれらの属性に基づいてフィルタリングしてください。

## セグメンテーション {#segmentation}

### 「キャンバスバリエーションに入っていない」と「キャンバスコントロールグループに属していない」の違いは何ですか？ {#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group}

フィルターの完全な定義については、[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)を参照してください。

#### キャンバスバリエーションに入っていない {#has-not-entered-canvas-variation}

ユーザーが特定のキャンバスのバリエーションパスに一度も入っていないことを意味します。コントロールグループに属していないすべてのユーザーが、そのキャンバスに入ったかどうかに関係なく含まれます。これには、別のバリエーションに入ったユーザーや、どのバリエーションにも入っていないユーザーが含まれます。

#### キャンバスコントロールグループに属していない {#is-not-in-canvas-control-group}

ユーザーがキャンバスに入ったものの、コントロールグループには属しておらず、結果としてバリエーションを受け取ったことを意味します。これにはキャンバスに入ったユーザーのみが含まれます。

バリエーションの割り当てはキャンバスへのエントリ時に行われます。ユーザーがキャンバスに入っていない場合、バリアントは割り当てられません。つまり、コントロールグループにもバリアントにも属しません。

## オリジナルキャンバスエディター {#original-canvas-editor}

{% details オリジナルキャンバスエディターのFAQを展開 %}

### 既存のキャンバスをオリジナルエディターから現在のエディターに変換するにはどうすればよいですか？ {#how-do-i-convert-an-existing-canvas-from-the-original-editor-to-the-current-editor}

[キャンバスを複製]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases)できます。これにより、最新のキャンバスワークフローでオリジナルキャンバスのコピーが作成されます。

### 現在のキャンバスエディターとオリジナルキャンバスエディターの主な違いは何ですか？ {#what-are-the-main-differences-between-the-current-and-original-canvas-editors}

#### キャンバスコンポーネントツールバー {#canvas-component-toolbar}

以前のオリジナルキャンバスエディターでは、ユーザージャーニーでステップを作成するたびに、デフォルトでフルステップが追加されていました。これらのフルステップは異なるキャンバスコンポーネントに置き換えられ、編集体験の可視性とカスタマイズ性が向上しました。キャンバスステップツールバーからすべてのキャンバスコンポーネントをすぐに確認できます。

#### ステップの動作 {#step-behavior}

以前は、各フルステップに遅延とスケジュール設定、例外イベント、オーディエンスフィルター、メッセージ設定、メッセージ進行オプションなどの情報が1つのコンポーネントにすべて含まれていました。現在のエディターではこれらが個別の設定になっており、キャンバス構築体験がよりカスタマイズしやすくなり、機能面でもいくつかの違いが生じています。

#### メッセージコンポーネントの進行 {#message-component-advancement}

[メッセージコンポーネント]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)は、ステップに入るすべてのユーザーを進行させます。メッセージ進行の動作を指定する必要がないため、全体的なステップの設定がシンプルになります。**メッセージ送信時に進行**オプションを実装したい場合は、前のステップを受信しなかったユーザーをフィルタリングするために、別のオーディエンスパスを追加してください。

#### 遅延の「以内」動作 {#delay-in-behavior}

[遅延コンポーネント]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)は、次のステップに進む前に遅延時間全体を待ちます。

例えば、4月12日に遅延コンポーネントがあり、遅延が1日後の午後2時にユーザーを次のステップに送信するように設定されているとします。ユーザーが4月13日の午後2時01分にコンポーネントに入ったとします。
- オリジナルワークフローの場合、ユーザーは4月14日の午後2時に次のステップに進みます。これはエントリ時刻から1日未満です。
- 現在のエディターでは、ユーザーは4月15日の午後2時に次のステップに進みます。同じ時刻ですが、エントリ時刻から1日以上経過しています。

#### インテリジェントタイミングの動作 {#intelligent-timing-behavior}

[インテリジェントタイミング]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)はメッセージコンポーネントに格納されるため、遅延はインテリジェントタイミングの計算の前に適用されます。つまり、ユーザーがコンポーネントに入るタイミングによっては、オリジナルキャンバスワークフローで構築されたキャンバスよりもメッセージの受信が遅くなる場合があります。

例えば、遅延が2日に設定され、インテリジェントタイミングがオンで、メッセージの最適な送信時刻が午後2時と判断されたとします。ユーザーが午後2時01分に遅延ステップに入ります。
- **現在のワークフロー：**遅延が経過するまで48時間かかるため、ユーザーは3日目の午後2時にメッセージを受信します。
- **オリジナルワークフロー：**ユーザーは2日目の午後2時にメッセージを受信します。

インテリジェントタイミングがオンの場合、メッセージはユーザーがメッセージコンポーネントに入ってから24時間以内に、特定されたインテリジェントタイムに送信されます（遅延コンポーネントが含まれていない場合も同様です）。

#### 例外イベント {#exception-events}

##### サイレント時間帯 {#quiet-hours}

例外イベントはアクションパスを使用して適用され、メッセージステップとは別になっています。サイレント時間帯はメッセージコンポーネントで適用されます。つまり、ユーザーがすでにアクションパスを通過し（例外イベントで除外されず）、メッセージコンポーネントに到達した時点でサイレント時間帯に遭遇し、サイレント時間帯の終了後にメッセージを再送信するようにキャンバスが設定されている場合、例外イベントは適用されなくなります。このユースケースは一般的ではありません。

セグメントとフィルターについては、メッセージステップに配信バリデーションがあり、送信時にバリデーションされる追加のセグメントとフィルターを設定できます。これにより、前述のサイレント時間帯のエッジケースを防ぐことができます。

##### 「以内」または「次の」スケジュール設定 {#in-or-on-the-next-schedule-setting}

例外イベントはアクションパスを使用して作成されます。アクションパスは「X時間のウィンドウの後」のみをサポートし、「X時間以内」や「次のX時間」はサポートしていません。

{% enddetails %}

### 「リクエストタイムアウト」エラーのサポートチケットを送信する際に何を含めるべきですか？ {#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error}

キャンバスの編集中に「リクエストタイムアウト」エラーが発生し、[Brazeサポート]({{site.baseurl}}/user_guide/administer/personal/braze_support)に連絡する必要がある場合は、解決を迅速にするために以下の情報を含めてください。

{% multi_lang_include messaging/support_ticket_request_timed_out_details.md context='canvas' %}

## キャンバスの配信とトラブルシューティング {#canvas-delivery-and-troubleshooting}

### 孤立したユーザーはキャンバスメッセージを受信できますか？ {#are-orphaned-users-eligible-to-receive-canvas-messages}

いいえ。[孤立したユーザー]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users)はメッセージを受信する資格がありません。ユーザーがキャンバスジャーニーの途中でプロファイルが孤立した場合、そのユーザーはフローからサイレントに退出します。分析では、その退出に対する**Exited**イベントが常に表示されるとは限らず、ワークフローサマリーに`exited_date`や`exit_reason`のない`partial_update_token`が含まれる場合があります。

マージと孤立したプロファイルの詳細については、[重複ユーザーのマージ]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users)を参照してください。

### アクティブなキャンバスやキャンペーンを停止した場合、すでにESPに送信されたメッセージは配信されますか？ {#if-i-stop-an-active-canvas-or-campaign-do-messages-already-sent-to-the-esp-still-deliver}

はい。Brazeがメールサービスプロバイダー (ESP) にリクエストを送信した後、Brazeはその送信を取り消すことはできません。キャンバスやキャンペーンを停止すると、新しい送信リクエストは防止されますが、すでにESPに引き渡されたメッセージは引き続き配信される可能性があり、ESPが処理する際に送信カウントが増加する場合があります。

これは[キャンバスを停止した場合](#what-happens-when-you-stop-a-canvas)に説明されている動作と同じです。送信中のメールは即座に停止されるわけではありません。

### ユーザーに表示されるコンテンツがないキャンバスのWebhookステップが実行されたことを確認するにはどうすればよいですか？ {#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content}

Brazeは、キャンペーンおよびキャンバスの[Webhook]({{site.baseurl}}/user_guide/channels/webhooks)ステップについて、Webhookの**送信数**と関連する配信結果をトラッキングします。ステップの分析、[Webhookレポート](#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content)、または[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)のWebhookイベントを使用して、ステップが実行されたことを確認してください。サーバー側の受信証明が必要な場合は、エンドポイントのリクエストログで追加の確認ができます。

Brazeには、Webhookステップ用のビルトインの非表示トラッキングピクセルは含まれていません。カスタムの1ピクセル画像リクエストではなく、BrazeのWebhookメトリクスとエンドポイントのログを活用してください。

### Webhookステップにボディフィールドがないのはなぜですか？ {#why-does-my-webhook-step-have-no-body-field}

Webhookステップは、`POST`、`PUT`、`PATCH`、`DELETE`でリクエストボディを使用します。メソッドを`GET`に切り替えると、GETリクエストはリクエストボディをサポートしないため、Brazeはボディフィールドを削除します。JSONやフォームデータを送信する必要がある場合は、ボディをサポートするメソッドに戻してください。メソッドの詳細については、[Webhookの作成]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#http-method)を参照してください。

### Webhookステップでspacer.gifを使用するにはどうすればよいですか？ {#how-do-i-use-spacergif-in-a-webhook-step}

Brazeは`cdn.braze.com`および`braze-images.com`で`spacer.gif`プレースホルダー画像をホストしています。一部のチームでは、外部エンドポイントを呼び出さずにステップを実行する必要がある場合に、WebhookのURLをこの画像に向けています。標準的なWebhookステップでは実際のエンドポイントを呼び出す必要があります。[ユーザーに表示されるコンテンツがないキャンバスのWebhookステップが実行されたことを確認するにはどうすればよいですか？]({{site.baseurl}}/user_guide/channels/webhooks/reporting)で説明されているように、[Webhookレポート]({{site.baseurl}}/user_guide/channels/webhooks/reporting)とエンドポイントログを使用して配信を確認してください。

### 「invalid next-step-id」エラーでキャンバスが読み込めないのはなぜですか？ {#why-wont-my-canvas-load-with-an-invalid-next-step-id-error}

このコンソールエラーは、少なくとも1つのステップが欠落している、または無効な次のステップを指していることを意味します。例えば、部分的な削除、複製、インポートの後に発生することがあります。エディターでキャンバスを開き、孤立したステップを再接続するか、有効な下流パスがなくなったステップを削除してください。それでもキャンバスが読み込めない場合は、キャンバスIDとコンソールエラーのスクリーンショットを添えて[Brazeサポート]({{site.baseurl}}/user_guide/administer/personal/braze_support)にお問い合わせください。

### Currentsのキャンバスコンバージョンタイムスタンプがキャンバス分析と異なるのはなぜですか？ {#why-does-a-canvas-conversion-timestamp-in-currents-differ-from-my-canvas-analytics}

Currentsは、キャンバスのコンバージョンを[`users.canvas.Conversion`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#canvas-conversion-events)イベントとして記録します。イベントの`time`はコンバージョンイベントが発生した時刻です。そのイベントの`conversion_behavior`フィールドは、コンバージョン定義（タイプとウィンドウ）を記述します。キャンバス分析では、コンバージョンウィンドウ内のキャンバスエントリに対するコンバージョンも集計される場合があります。エクスポートを照合する際は、Currentsの`time`をコンバージョンイベントのタイムスタンプおよびキャンバスのコンバージョンウィンドウ設定と比較してください。

### Currentsで`canvas_step_name`がnullになるのはなぜですか？ {#why-is-canvas_step_name-null-in-currents}

`canvas_step_name`などのキャンペーンおよびキャンバスの名前フィールドは、Brazeがステップメタデータの伝播を完了する前にCurrentsイベントが送信された場合（例えば、ステップの作成や名前変更の直後）に`null`になることがあります。詳細については、[Currentsデータでキャンペーン名またはキャンバスステップ名が`NULL`になるのはなぜですか？]({{site.baseurl}}/user_guide/data/distribution/braze_currents/faq#why-is-the-campaign-name-or-canvas-step-name-null-in-my-currents-data)を参照してください。

### ユーザー更新ステップで配列が更新されないのはなぜですか？ {#why-isnt-my-array-updating-in-a-user-update-step}

[ユーザー更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)ステップのJSONを確認してください。配列およびネストされた属性の更新には、変更する属性の有効なパスと値が必要です。外部ユーザーIDなど、ステップが自動的に提供するフィールドは含めないでください。起動前にステップの**プレビューとテスト**タブを使用してペイロードを確認してください。

### `external_id`を持たないユーザーにキャンバスメッセージを送信できますか？ {#can-i-send-canvas-messages-to-users-without-an-external_id}

はい、Brazeユーザープロファイルがすでに存在している場合は可能です。`external_id`を持たないユーザーは[匿名ユーザー]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles)であり、`braze_id`または[ユーザーエイリアス]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases)で参照できます。キャンバスエントリの前に、[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)またはSDKを使用してプロファイルを作成または更新し、[アクションベースまたはAPIトリガーエントリ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule)を使用してください。標準的なキャンバスターゲティングにはBrazeユーザープロファイルが必要です。プロファイルのないメールアドレスだけにキャンバスメッセージを送信することはできません。

### ユーザーがトリガーイベントを実行した回数よりも少ない回数しかキャンバスにエントリしなかったのはなぜですか？ {#why-did-a-user-enter-a-canvas-fewer-times-than-they-performed-the-trigger-event}

アクションベースおよびAPIトリガーのキャンバスでは、Brazeはトリガーイベントの重複排除を行い、同じキャンバスに対してユーザーが**1秒あたり最大約1回**しかエントリできないようにしています。ユーザーが1秒以内に同じトリガーを複数回実行した場合、1回のエントリのみが処理されます。

同じ秒内に複数のエントリを許可するには、トリガーイベントの間隔を少なくとも1.1秒空けてください（例えば、サーバーからイベントタイミングを制御する場合）。同じ秒内の複数トリガーを許可するキャンペーンスタイルの動作については、適切なスケジューリングと再適格性設定を持つ[キャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns)とユースケースを比較してください。

### APIトリガーのキャンバスでユーザーが重複排除されるのはいつですか？ {#when-are-users-de-duplicated-in-api-triggered-canvases}

ユーザーがAPIトリガーのキャンバスに再エントリし、前回のエントリで同一のメッセージに対してすでにキューに入っている遅延ステップに到達した場合、Brazeは重複送信を防ぐためにユーザーの重複排除を行います。2番目のキャンバスインスタンスは退出するため、エントリ数が送信数を上回る場合があります。

### テストプッシュが間違ったアプリに送信されますが、ライブ送信は正しいのはなぜですか？ {#why-does-a-test-push-go-to-the-wrong-app-but-live-sends-look-correct}

ユーザープロファイルの**テストプッシュ**は、そのプロファイルに紐づくプッシュ有効なすべてのデバイスに配信されます。デバイスに複数のアプリがインストールされている場合、OSは通常、最初に利用可能なアプリにテスト通知を配信しますが、それは検証したいアプリではない場合があります。

アプリ固有のターゲティングを確認するには、プロファイルの**テストプッシュ**だけに頼るのではなく、狭いオーディエンス（例えば`external_id`でフィルター）を持つキャンペーンまたはキャンバスを通じてライブメッセージまたはテストメッセージを送信してください。

複数のアプリを持つ**キャンバス**のメッセージステップでは、メッセージステップの**送信時にオーディエンスを検証**をオンにして、送信時にセグメントとフィルターのチェックが実行されるようにしてください。詳細については、[メッセージステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)を参照してください。

テストプッシュの一般的な動作については、[テストメッセージの送信]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages)および[プッシュFAQ]({{site.baseurl}}/user_guide/channels/push/faqs)を参照してください。

### iOSとAndroidでPush Storiesをデバッグするにはどうすればよいですか？ {#how-do-i-debug-push-stories-on-ios-and-android}

設定とクリエイティブ要件については、[Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories)を参照してください。実装とリッチプッシュ通知の処理については、開発者ガイドの[リッチプッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/rich)および[Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories)を参照してください。

### 「キャンバスメッセージが24時間以上遅延しています」というメールは誰に届きますか？ {#who-receives-the-canvas-messages-delayed-24-hours-email}

Brazeは、キャンバスメッセージがレート制限により24時間以上遅延している場合にこの通知を送信します。このメールは、影響を受けるキャンバスに以前変更を加えたダッシュボードユーザー（キャンバス変更ログに基づく）に送信されます。Brazeがそれらの受信者を特定できない場合、メールはワークスペースの**会社管理者**に送信されます。

### 例外イベント後、ユーザーはいつメッセージの受信を停止しますか？ {#when-does-a-user-stop-receiving-messages-after-an-exception-event}

Brazeは例外イベントが発生した時点で退出を記録しますが、タイマーが終了するまでユーザーがステップ内に留まる場合があります。これは遅延ステップで最も顕著に見られます。動作はスケジュールされたステップとイベントトリガーステップでも異なります。タイムライン、例、分析の注意点については、[退出条件]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria)を参照してください。

### アクションパスステップでリンクエイリアスのインタラクションを選択するとエラーが表示されるのはなぜですか？ {#why-does-my-action-paths-step-show-an-error-when-i-select-a-link-alias-interaction}

メールのインタラクティビティトリガー（例えば、**メールでエイリアスをクリック**や**任意のキャンペーンまたはキャンバスステップでエイリアスをクリック**）を使用するアクショングループには、そのリンクを含むメッセージをすでに送信したメッセージステップが必要です。メールがアクションパスステップのクリックを評価する前に送信されるようにステップを追加または並べ替えるか、このキャンバスでユーザーがすでに受信したメッセージに一致するインタラクションを選択してください。インタラクショントリガーの完全なリストについては、[アクションベース配信]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)を参照してください。

### 過去のカスタムイベントタイムスタンプは、アクションベースのキャンバスやキャンペーンにどのように影響しますか？ {#how-do-historical-custom-event-timestamps-affect-action-based-canvases-and-campaigns}

Brazeは、適格なイベントが取り込まれ、ユーザーがオーディエンスルールを満たした時点でアクションベースのジャーニーを評価します。イベントがキャンバスやキャンペーンがアクティブだったウィンドウの外でプロファイルに到達した場合、またはユーザーがオーディエンスに一致する前に到達した場合、エントリまたは下流の送信が期待どおりに行われない場合があります。ユーザープロファイルのアクティビティログと[カスタムイベントのトラブルシューティング]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#troubleshooting-custom-events)のトラブルシューティングステップを使用して、イベントのタイムスタンプを稼働開始時間とセグメントメンバーシップと比較してください。動作が期待と一致しない場合は、[Brazeサポート]({{site.baseurl}}/user_guide/administer/personal/braze_support)にお問い合わせください。