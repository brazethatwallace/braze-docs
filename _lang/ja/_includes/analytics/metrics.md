{% if include.metric == "AMP Clicks" %}
<i>AMPクリック数</i>は、AMP HTMLメールのクリック数の合計で、HTML、プレーンテキスト、およびAMP HTMLバージョンのメールの総計です。
{% endif %}

{% if include.metric == "AMP Opens" %}
<i>AMP開封数</i>は、AMP HTMLメールおよびAMP HTMLバージョンのメールの開封総数です。
{% endif %}

{% if include.metric == "Audience" %}
<i>オーディエンス</i>は、特定のメッセージを受け取ったユーザーの割合です。この数値はBrazeから提供されます。
{% endif %}

{% if include.metric == "Bounces" %}
<i>バウンス数</i>は、意図した受信者に正常に配信されなかったメッセージの総数です。
{% endif %}

{% if include.metric == "Estimated Real Opens" %}
<i>推定実開封数</i>は、機械による開封が存在しなかった場合にどれだけのユニーク開封があるかを推定したもので、Braze独自の統計モデルの結果です。
{% endif %}

{% if include.metric == "Help" %}
<i>ヘルプ</i>は、ユーザーがメッセージに<a href="https://braze.com/docs/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">HELPキーワード</a> で返信し、HELP自動レスポンスが送信された場合です。
{% endif %}

{% if include.metric == "Hard Bounce" %}
<i>ハードバウンス</i>は、永久的な配信エラーによって受信者にメールが届かないことをいいます。ドメイン名が存在しないか、受信者が不明なため、ハードバウンスが発生する可能性があります。
{% endif %}

{% if include.metric == "Soft Bounce" %}
<i>ソフトバウンス</i>は、受信者のメールアドレスが有効であるにもかかわらず、一時的な配信エラーによってメールが受信者に届かないことをいいます。ソフトバウンスが発生する理由として、受信者の受信トレイがいっぱいである、サーバーが停止している、メッセージが受信者の受信トレイには大きすぎる、などがあります。
{% endif %}

{% if include.metric == "Deferral" %}
<i>延期</i>は、メールがすぐに配信されなかった場合です。ただし、Brazeはこの一時的な配信失敗の後、最大72時間までメールの再送信を試行し、特定のCampaignの試行が停止される前に配信成功の可能性を最大化します。
{% endif %}

{% if include.metric == "Body Click" %}
Push Stories通知は、通知がクリックされると<i>ボディクリック</i>を記録します。メッセージが展開されたとき、またはアクションボタンがクリックされたときには記録されません。
{% endif %}

{% if include.metric == "Body Clicks" %}
<i>ボディクリック</i>は、従来のエディターで作成されたボタン（ボタン1、ボタン2）のないメッセージをユーザーがクリックしたとき、また、HTMLエディターやドラッグ＆ドロップエディターで作成されたメッセージが引数のない<code>brazeBridge.logClick()</code>を使用したときに発生します。
{% endif %}

{% if include.metric == "Button 1 Clicks" %}
<i>ボタン1クリック数</i>は、メッセージのボタン1をクリックした総数です。
{% endif %}

{% if include.metric == "Button 2 Clicks" %}
<i>ボタン2クリック数</i>は、メッセージのボタン2をクリックした総数です。
{% endif %}

{% if include.metric == "Choices Submitted" %}
<i>送信された選択肢数</i>は、<a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>簡単な調査</a> の質問ページでユーザーが送信ボタンをクリックしたときに選択された選択肢の総数です。
{% endif %}

{% if include.metric == "Click-to-Open Rate" %}
<i>クリック開封率</i>は、開封されたメールのうち、単一のユーザーまたは機械によって少なくとも1回クリックされたものの割合です。この指標は<a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>レポートビルダー</a> でのみ利用可能です。
{% endif %}

{% if include.metric == "Close Message" %}
<i>メッセージを閉じる</i>は、メッセージの [閉じる] ボタンをクリックした合計回数です。これは、従来のエディターではなく、ドラッグ＆ドロップエディターで作成されたアプリ内メッセージにのみ存在します。
{% endif %}

{% if include.metric == "Confirmed Deliveries" %}
<i>確認済み配信</i>は、通信事業者がターゲットの電話番号にメッセージが配信されたことを確認した場合です。
{% endif %}

{% if include.metric == "Confidence" %}
<i>信頼度</i>は、メッセージの特定のバリアントのパフォーマンスがコントロールグループよりも優れているという信頼度の割合です。
{% endif %}

{% if include.metric == "Confirmation Page Button" %}
<i>確認ページボタン</i>は、<a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>簡単な調査</a> の確認ページにあるコールトゥアクションボタンのクリック数の合計です。
{% endif %}

{% if include.metric == "Confirmation Page Dismissals" %}
<i>確認ページ却下数</i>は、<a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>簡単な調査</a> の確認ページにある [閉じる] (x) ボタンのクリック数の合計です。
{% endif %}

{% if include.metric == "Conversion Rate" %}
<i>コンバージョン率</i>は、メッセージの全受信者と比較して、定義されたイベントが発生した回数の割合です。このイベントは、Campaignを作成するときに決定します。
{% endif %}

{% if include.metric == "Conversion Window" %}
<i>コンバージョンウィンドウ</i>は、メッセージを受け取ってから、ユーザーのアクションがトラッキングされ、コンバージョンイベントに帰属されるまでの日数です。この期間の後に発生したコンバージョンは、コンバージョンイベントに帰属されません。
{% endif %}

{% if include.metric == "Conversions (B, C, D)" %}
<i>コンバージョン (B, C, D)</i>は、1次コンバージョンイベントの後に追加されるコンバージョンイベントです。これは、Braze Campaignから受信したメッセージと対話または閲覧した後に、定義されたイベントが発生した回数です。
{% endif %}

{% if include.metric == "Total Conversions" %}
<i>合計コンバージョン数</i>は、ユーザーがアプリ内メッセージCampaignを閲覧した後、特定のコンバージョンイベントを完了した合計回数です。
{% endif %}

{% if include.metric == "Deliveries" %}
<i>配信数</i>は、受信サーバーが受け入れたメッセージリクエスト数の合計（または割合）です。これは、メッセージがデバイスに届いたことを意味するのではなく、メッセージがサーバーに受け入れられたことのみを意味します。
{% endif %}

{% if include.metric == "Deliveries %" %}
<i>配信数%</i>は、メール可能な相手に正常に送受信されたメッセージ（送信数）の合計数に対する割合です。
{% endif %}

{% if include.metric == "Delivery Failures" %}
<i>配信失敗</i>は、キューがオーバーフローしたためにSMSを送信できなかった場合です（ロングコードまたはショートコードが処理できる以上のレートでSMSを送信した場合）。
{% endif %}

{% if include.metric == "Delivery Failures RCS" %}
<i>配信失敗</i>は、キューがオーバーフローしたためにRCSを送信できなかった場合です（RCS検証済みの送信者が処理できる以上の速度でRCSを送信した場合）。
{% endif %}

{% if include.metric == "Failed Delivery Rate" %}
<i>配信失敗率</i>は、メッセージを送信できなかったために失敗した送信の割合です。これは、キューのオーバーフロー、アカウントの停止、MMSの場合のメディアエラーなど、さまざまな理由で発生する可能性があります。
{% endif %}

{% if include.metric == "Direct Opens" %}
<i>直接開封数</i>は、通知を直接押してアプリやWebサイトを開いたユーザーの総数（または割合）です。
{% endif %}

{% if include.metric == "Emailable" %}
<i>メール可能なユーザー数</i>は、レコードにメールアドレスがあり、明示的にオプトインまたは購読しているユーザーの合計数です。
{% endif %}

{% if include.metric == "Errors" %}
<i>エラー数</i>は、Webhookイベントによって返されたエラーの数です（送信プロセス中に増加します）。
{% endif %}

{% if include.metric == "Failures" %}
<i>失敗</i>は、インターネットサービスプロバイダーがハードバウンスを返したため、WhatsAppメッセージを送信できなかった場合です。ハードバウンスは、永続的な配信の失敗を意味します。
{% endif %}

{% if include.metric == "Influenced Opens" %}
<i>誘発された開封数</i>は、プッシュ通知の送信後に、プッシュを直接開封せずにアプリを開いたユーザーの総数（または割合）です。
{% endif %}

{% if include.metric == "Lifetime Revenue" %}
<i>生涯収益</i>は、開始以降に受け取った<code>PurchaseEvents</code>価格の合計値（USD）です。
{% endif %}

{% if include.metric == "Lifetime Value Per User" %}
<i>ユーザーあたりの生涯価値</i>は、<i>生涯収益</i>を<i>総ユーザー数</i>（ホームページに記載）で割ったものです。
{% endif %}

{% if include.metric == "Average Daily Revenue" %}
<i>日次平均収益</i>は、指定された日のCampaignとCanvasの収益の合計の平均です。
{% endif %}

{% if include.metric == "Daily Purchases" %}
<i>日次購入数</i>は、期間中のユニーク<code>PurchaseEvents</code>の合計を平均した数です。
{% endif %}

{% if include.metric == "Daily Revenue Per User" %}
<i>ユーザーあたりの日次収益</i>は、日次収益を日次アクティブユーザー数で割った平均です。
{% endif %}

{% if include.metric == "Machine Opens" %}
<i>機械開封</i>には、iOS 15のAppleのメールプライバシー保護（MPP）の影響を受ける「開封」の割合が含まれます。例えば、ユーザーがAppleデバイスのメールアプリを使用してメールを開封した場合、これは<i>機械開封</i>としてログに記録されます。
{% endif %}

{% if include.metric == "Other Opens" %}
<i>その他の開封</i>には、<i>機械開封</i>として識別されないメールが含まれます。例えば、ユーザーが別のプラットフォーム（携帯電話のGmailアプリ、デスクトップブラウザーのGmailなど）でメールを開封すると、これは<i>その他の開封</i>としてログに記録されます。
{% endif %}

{% if include.metric == "Opens" %}
<i>開封</i>は、<i>直接開封</i>と<i>誘発された開封</i>の両方を含むインスタンスで、Braze SDKが独自のアルゴリズムを用いて、プッシュ通知によってユーザーがアプリを開封したと判断したものを指します。
{% endif %}

{% if include.metric == "Opt-Out" %}
<i>オプトアウト</i>は、ユーザーがメッセージに<a href="https://braze.com/docs/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">オプトアウトキーワード</a> で返信し、SMSまたはRCSプログラムから購読解除された場合です。
{% endif %}

{% if include.metric == "Pending Retry" %}
<i>再試行保留中数</i>は、受信サーバーによって一時的に拒否されたが、メールサービスプロバイダー（ESP）によって再配信が試行されたリクエストの数です。ESPは、タイムアウト期間に達する（通常は72時間後）まで配信を再試行します。
{% endif %}

{% if include.metric == "Primary Conversions (A) or Primary Conversion Event" %}
<i>1次コンバージョン (A)</i>または<i>1次コンバージョンイベント</i>は、Braze Campaignから受信したメッセージの操作後または表示後に、定義されたイベントが発生した回数です。この定義されたイベントは、Campaignを作成するときに決定します。
{% endif %}

{% if include.metric == "Reads" %}
<i>既読</i>は、ユーザーがメッセージを読んだ場合です。Brazeが既読数を追跡するには、ユーザーの既読レシートが「オン」になっている必要があります。
{% endif %}

{% if include.metric == "Read Rate" %}
<i>既読率</i>は、送信のうち既読になった割合です。これは、既読レシートをオンにしているユーザーにのみ提供されます。
{% endif %}

{% if include.metric == "Received" %}
<i>受信済み</i>はチャネルごとに定義が異なり、ユーザーがメッセージを閲覧したとき、ユーザーが定義されたトリガーアクションを実行したとき、またはメッセージがメッセージプロバイダーに送信されたときのいずれかです。
{% endif %}

{% if include.metric == "Rejections" %}
<i>拒否</i>は、SMSまたはRCSがキャリアによって拒否された場合です。これは、通信事業者のコンテンツフィルタリング、宛先デバイスの可用性、電話番号の使用停止など、さまざまな理由で発生する可能性があります。
{% endif %}

{% if include.metric == "Revenue" %}
<i>収益</i>は、設定された<a href='/docs/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events'>1次コンバージョン期間</a> 内のCampaign受信者からのドル単位の総収益です。
{% endif %}

{% if include.metric == "Messages Sent" %}
<i>送信済みメッセージ数</i>は、Campaignで送信されたメッセージの合計数です。スケジュールされたCampaignを開始した後、この指標には、レート制限のためにまだ送信されていないものも含め、送信されたすべてのメッセージが含まれます。これは、メッセージが受信されたりデバイスに配信されたことを意味するのではなく、メッセージが送信されたことのみを意味します。
{% endif %}

{% if include.metric == "Sent" %}
<i>送信済み</i>は、CampaignまたはCanvasステップが開始またはトリガーされ、BrazeからSMSまたはRCSが送信されたことを意味します。エラーによってSMSまたはRCSがユーザーの端末に届かなかった可能性もあります。
{% endif %}

{% if include.metric == "Sends" %}
<i>送信数</i>は、1つのCampaignで送信されたメッセージの総数です。スケジュールされたCampaignを開始した後、この指標には、レート制限のためにまだ送信されていないものも含め、送信されたすべてのメッセージが含まれます。これは、メッセージが受信されたりデバイスに配信されたことを意味するのではなく、メッセージが送信されたことのみを意味します。
{% endif %}

{% if include.metric == "Sends to Carrier" %}
<i>キャリアへの送信数</i>は非推奨ですが、すでにご利用のユーザーについては引き続きサポートされます。これは、<i>確認済み配信数</i>、<i>拒否数</i>、および通信事業者によって配信または拒否が確認されなかった<i>送信数</i>の合計です。一部の通信事業者がこの確認を提供していないか、送信時に提供できないため、通信事業者が配信や拒否の確認を提供していない場合も含まれます。
{% endif %}

{% if include.metric == "Sends to Carrier Rate" %}
<i>キャリアへの送信率</i>は、送信されたメッセージの合計のうち、<i>キャリアへの送信</i>として分類されたメッセージの割合です。一部の通信事業者が配信確認や拒否確認を提供しないか、送信時に提供できない場合も含まれます。この指標は非推奨ですが、すでにご利用のユーザーについては引き続きサポートされます。
{% endif %}

{% if include.metric == "Spam" %}
<i>スパム</i>は、受信者によって「スパム」とマークされたメールの総数です。Brazeはこれらのユーザーの購読状態を変更しませんが、「購読解除を含むすべてのユーザーに送信する」ように設定されているトランザクションメールを送信しない限り、これらのユーザーは今後のメールから自動的に除外されます。
{% endif %}

{% if include.metric == "Survey Page Dismissals" %}
<i>調査ページ却下数</i>は、<a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>簡単な調査</a> の質問ページにある [閉じる] (x) ボタンのクリック数の合計です。
{% endif %}

{% if include.metric == "Survey Submissions" %}
<i>調査送信数</i>は、<a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>簡単な調査</a> の送信ボタンをクリックした回数の合計です。
{% endif %}

{% if include.metric == "Total Clicks" %}
<i>クリック数の合計</i>は、配信されたメッセージ内のリンクをクリックしたユニークな受信者の数（または割合）です。
{% endif %}

{% if include.metric == "Total Dismissals" %}
<i>却下数の合計</i>は、ユーザーがCampaignのメッセージを却下した回数です。Content Cardsの場合、各カードの却下がカウントされます。バナーの場合、却下動作が有効になっているときにユーザーがバナーを却下した回数がカウントされます。
{% endif %}

{% if include.metric == "Total Impressions" %}
<i>総インプレッション数</i>は、メッセージが表示された回数です。Brazeは、メッセージがユーザーの画面上で表示された時点でのみインプレッションを記録します。例えば、メッセージがページの下部に配置されている場合、ユーザーがスクロールしてメッセージが表示されるまで、そのインプレッションは記録されません。ユーザーに同じメッセージが2回表示された場合、2回のインプレッションとしてカウントされます。
{% endif %}

{% if include.metric == "Total Opens" %}
<i>開封数の合計</i>は、開封されたメッセージ数の合計です。
{% endif %}

{% if include.metric == "Total Revenue" %}
<i>総収益</i>は、設定された1次コンバージョン期間内のCampaign受信者からのドル単位の総収益です。
{% endif %}

{% if include.metric == "Unique Clicks" %}
<i>ユニーククリック数</i>は、メッセージ内のリンクを少なくとも1回クリックした受信者の固有数で、<a href='https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/dispatch_id/'>dispatch_id</a> によって測定されます。
{% endif %}

{% if include.metric == "Unique Dismissals" %}
<i>ユニーク却下数</i>は、CampaignからContent Cardsを却下したユニーク受信者の数です。あるユーザーがCampaignからContent Cardsを複数回却下した場合、ユニーク却下1回としてカウントされます。
{% endif %}

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

{% if include.metric == "Unique Impressions" %}
<i>ユニークインプレッション数</i>は、特定のCampaignから送信されたメッセージを閲覧したユーザーの総数です。インプレッションは、メッセージがユーザーの画面に表示されたときのみ記録されます。
{% endif %}

{% if include.metric == "Unique Daily Impressions" %}
<i>日次ユニークインプレッション数</i>は、指定された日にメッセージを閲覧したユニークユーザーの数です。このカウントはカレンダー日ごとにリセットされるため、同じメッセージを2日間にわたって閲覧したユーザーは2回カウントされます。この指標は、同名の課金指標と一致します。
{% endif %}

{% if include.metric == "Unique Recipients" %}
<i>ユニーク受信者数</i>は、1日のユニーク受信者数、つまり1日に新しいメッセージを受信したユーザーの数です。このカウントが1人のユーザーに対して複数回増分されるためには、そのユーザーが別の日に新しいメッセージを受け取る必要があります。
{% endif %}

{% if include.metric == "Unique Opens" %}
<i>ユニーク開封数</i>は、配信されたメッセージのうち、1人のユーザーが少なくとも1回開封したメッセージの総数（または割合）で、7日間にわたってトラッキングされます。
{% endif %}

{% if include.metric == "Unsubscribers or Unsub" %}
<i>配信停止者数</i>または<i>Unsub</i>は、配信停止に至ったメッセージの数です。配信停止は、Brazeがメッセージ本文内のBraze配信停止URLからの配信停止を処理したとき、またはlist-unsubscribeヘッダーからの配信停止をBrazeが処理したときに発生します。
{% endif %}

{% if include.metric == "Unsubscribes" %}
<i>購読解除数</i>は、Brazeが提供する配信停止パス（メッセージ本文内のBraze配信停止URLや、Brazeがリクエストを処理するlist-unsubscribeを含む）を通じて、サブスクリプション状態が配信停止に変更された受信者の数です。
{% endif %}

{% if include.metric == "Variation" %}
<i>バリエーション数</i>は、Campaignのバリエーションの数で、作成者の定義によって異なります。
{% endif %}