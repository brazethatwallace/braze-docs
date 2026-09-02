---
page_order: 3
nav_title: セグメンテーションフィルター
article_title: セグメンテーションフィルター
layout: glossary_page
glossary_top_header: "セグメンテーションフィルター"
glossary_top_text: "Braze SDKは、特定の機能や属性に基づいてユーザーをセグメント化し、ターゲティングするための強力なフィルターを提供します。フィルターカテゴリーでこれらのフィルターを検索または絞り込むことができます。<br><br>ユーザーのセグメント化に使用できるさまざまなカスタム属性データタイプについては、<a href=\"/docs/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types\">カスタム属性データタイプ</a> をご覧ください。"

page_type: glossary
tool: Segments
description: "この用語集では、ユーザーのセグメント化とターゲティングに使用できるフィルターを一覧にしています。"
search_rank: 2
glossary_tag_name: フィルターカテゴリー
glossary_filter_text: "カテゴリーを選択して用語集を絞り込みます:"

glossary_tags:
  - name: Segment or CSV membership
  - name: Custom attribute
  - name: Custom events
  - name: Sessions
  - name: Retargeting
  - name: Channel subscription behavior
  - name: Purchase behavior
  - name: eCommerce
  - name: Demographic attributes
  - name: App
  - name: Uninstall
  - name: Devices
  - name: Location
  - name: Cohort membership
  - name: Install attribution
  - name: Intelligence and predictive
  - name: Social activity
  - name: Other Filters
  - name: Advertising use cases
  - name: User Attributes

glossaries:
  - name: Segment Membership
    display_name: "セグメントメンバーシップ"
    description: フィルターが使用される場所（セグメント、キャンペーンなど）でセグメントメンバーシップに基づいてフィルタリングし、1つのキャンペーン内で複数の異なるセグメントをターゲットにできます。<br><br>特定の時点でのセグメントメンバーシップをキャプチャするには、キャンペーンまたはキャンバスを送信する前に、ダッシュボードからセグメントのユーザーをエクスポートするか、<a href="/docs/api/endpoints/export/user_data/post_users_segment/"><code>/users/export/segment</code>エンドポイント</a> を呼び出してください。Brazeはユーザーごとのセグメンテーション履歴を保存しないため、過去の特定の時点でユーザーがセグメントに含まれていたかどうかを遡って確認することはできません。詳細については、<a href="/docs/user_guide/data/distribution/export_braze_data/segment_data_to_csv/">セグメントデータをCSVにエクスポート</a> を参照してください。<br><br>このフィルターを既に使用しているセグメントは、他のセグメントにさらに含めたりネストしたりすることはできません。これは、セグメントAがセグメントBを含み、セグメントBが再びセグメントAを含もうとするサイクルが発生する可能性があるためです。そのような場合、セグメントは自身を参照し続け、実際に誰がそのセグメントに属しているかを計算することが不可能になります。また、このようなセグメントのネストは複雑さを増し、処理速度を低下させる可能性があります。代わりに、同じフィルターを使用して含めたいセグメントを再作成してください。<br><br>**Segment Membership**フィルターのドロップダウンにセグメントが表示されない場合は、同じフィルターで再作成して新しいセグメントを選択するか、サイクルを生成する形でこのオーディエンスに既に依存していないことを確認してください。
    tags:
      - Segment or CSV membership
  - name: Braze Segment Extensions
    display_name: "Brazeセグメントエクステンション"
    description: Brazeダッシュボードでセグメントエクステンションを作成した後、セグメントにそれらのエクステンションを含めるか除外するかを選択できます。
    tags:
      - Segment or CSV membership
  - name: Updated/Imported from CSV
    display_name: "CSVからの更新/インポート"
    description: ユーザーがCSVアップロードの一部であったかどうかに基づいてセグメント化します。Brazeはセグメンテーション目的で、ユーザープロファイルごとに直近100件のCSVインポートのみを保持します。リターゲティング用に選択された100件を超えるCSVインポートにユーザーが含まれている場合、直近100件のみがこのフィルターで利用可能です。それより古いインポートはそのユーザーに一致しなくなります。
    tags:
      - Segment or CSV membership
  - name: Custom Attributes
    display_name: "カスタム属性"
    description: ユーザーがカスタム記録された属性値に一致するかどうかを判定します。日付および時間間隔の比較の最大ルックバック期間は100年です。<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Custom attribute
  - name: Created At
    display_name: "作成日時"
    description: ユーザープロファイルが作成された日時でセグメント化します。ユーザーがCSVまたはAPIで追加された場合、このフィルターは追加された日付を反映します。ユーザーがCSVまたはAPIで追加されておらず、SDKによって最初のセッションが追跡された場合、このフィルターはその最初のセッションの日付を反映します。最大ルックバック期間は100年です。
    tags:
      - Other Filters
  - name: Created From
    display_name: "作成元"
    description: "ユーザープロファイルが作成された場所でセグメント化します。<br><br>以下の値がサポートされています:<br>- SDK (<code>sdk</code>): Braze SDKを通じて作成されたユーザープロファイル。<br>- REST API (<code>rest</code>): Braze REST APIを通じて作成されたユーザープロファイル。<br>- プッシュトークンインポート (<code>pti</code>): プッシュトークンインポートを通じて作成されたユーザープロファイル。<br>- CSV (<code>csv</code>): CSVインポートを通じて作成されたユーザープロファイル。<br>- デモ (<code>demo</code>): デモデータを通じて作成されたユーザープロファイル。<br>- SMS (<code>sms</code>): SMSを通じて作成されたユーザープロファイル。<br>- Shopify (<code>shopify</code>): Shopifyを通じて作成されたユーザープロファイル。<br>- WhatsApp (<code>whats_app</code>): WhatsAppを通じて作成されたユーザープロファイル。<br>- プロバイダーイベント (<code>provider_event</code>): プロバイダーイベントを通じて作成されたユーザープロファイル。<br>- プロバイダー同期 (<code>provider_sync</code>): プロバイダー同期を通じて作成されたユーザープロファイル。<br>- ランディングページ (<code>landing_page</code>): ランディングページを通じて作成されたユーザープロファイル。"
    tags:
      - Other Filters
  - name: Nested Custom Attributes
    display_name: "階層化カスタム属性"
    description: カスタム属性のプロパティである属性です。<br><br>階層化された時間カスタム属性をフィルタリングする場合、「Day of Year」または「Time」に基づいてフィルタリングすることを選択できます。「Day of Year」は比較のために月と日のみをチェックします。「Time」は年を含む完全なタイムスタンプを比較します。時間間隔の比較の最大ルックバック期間は100年です。同じロジックがキャンバスのオーディエンスパスのコンテキスト変数をフィルタリングする場合にも適用されます。詳細については、<a href="/docs/user_guide/messaging/design_and_edit/personalize/sources/context_variables/#day-of-year-and-time-filters-for-date-context-variables">日付コンテキスト変数のDay of YearフィルターとTimeフィルター</a> を参照してください。
    tags:
      - Custom attribute
  - name: Day of Recurring Event
    display_name: "定期イベントの日"
    description: このフィルターは「日付」データタイプのカスタム属性の月と日を確認しますが、年は確認しません。このフィルターは年次イベントに便利です。<br><br>タイムゾーン&#58;<br>このフィルターは、メッセージがローカルタイムスケジューリングオプションを使用して送信される限り、ユーザーのタイムゾーンに合わせて調整されます。それ以外の場合、このフィルターは会社のタイムゾーンを使用します。
    tags:
      - Custom attribute
  - name: Custom Event
    display_name: "カスタムイベント"
    description: ユーザーが特別に記録されたイベントを実行したかどうかを判定します。<br><br>例:<br>プロパティactivity_nameでアクティビティが完了。<br><br>タイムゾーン:<br>UTC - 暦日 = 1暦日は24〜48時間のユーザー履歴を確認します
    tags:
      - Custom events
  - name: First Did Custom Event
    display_name: "初回カスタムイベント実行"
    description: ユーザーが特別に記録されたイベントを実行した最も早い時間を判定します。最大ルックバック期間は100年です。（24時間期間）<br><br>例:<br>初回のカート放棄が1日未満前<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Custom events
  - name: Last Did Custom Event
    display_name: "最終カスタムイベント実行"
    description: ユーザーが特別に記録されたイベントを実行した最新の時間を判定します。このフィルターは0.25時間などの小数をサポートしています。最大ルックバック期間は100年です。（24時間期間）<br><br>例:<br>最後のカート放棄が1日未満前<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Custom events
  - name: X Custom Event In Y Days
    display_name: "Y日間にX回のカスタムイベント"
    description: 指定された暦日数（1〜30日）の間に、ユーザーが特別に記録されたイベントを0〜50回実行したかどうかを判定します。（暦日 = 1暦日は24〜48時間のユーザー履歴を確認します）<br> <a href="/docs/x-in-y-behavior">X-in-Y動作の詳細はこちらをご覧ください。</a> <br><br>例:<br>過去1暦日にカート放棄がちょうど0回<br><br>タイムゾーン:<br>UTC - すべてのタイムゾーンに対応するため、1暦日はセグメントが評価される時間に応じて24〜48時間のユーザー履歴を確認します。2暦日の場合は48〜72時間のユーザー履歴を確認し、以降同様です。
    tags:
      - Custom events
  - name: X Custom Event Property In Y Days
    display_name: "Y日間にX回のカスタムイベントプロパティ"
    description: 指定された暦日数（1〜30日）の間に、ユーザーが特定のプロパティに関連して特別に記録されたイベントを0〜50回実行したかどうかを判定します。（暦日 = 1暦日は24〜48時間のユーザー履歴を確認します）<br><a href="/docs/x-in-y-behavior">X-in-Y動作の詳細はこちらをご覧ください。</a> <br><br>例:<br>過去1暦日にプロパティ「event_name」でお気に入りに追加がちょうど0回<br><br>タイムゾーン:<br>UTC - すべてのタイムゾーンに対応するため、1暦日はセグメントが評価される時間に応じて24〜48時間のユーザー履歴を確認します。2暦日の場合は48〜72時間のユーザー履歴を確認し、以降同様です。
    tags:
      - Custom events
  - name: Email Address
    display_name: "メールアドレス"
    description: テスト用に個別のメールアドレスでキャンペーンの受信者を指定できます。また、フィルター内の「Email Address is not Blank」指定子を使用して、すべてのユーザー（購読解除済みを含む）にトランザクションメールを送信し、オプトインステータスに関係なくメールの配信を最大化することもできます。<br><br>このフィルターはユーザープロファイルにメールアドレスがあるかどうかのみをチェックしますが、<a href="/docs/user_guide/audience/segments/segmentation_filters#email-available">Email Available</a> フィルターは追加の条件をチェックします。
    tags:
      - Other Filters
  - name: External User ID
    display_name: "外部ユーザーID"
    description: テスト用に個別のユーザーIDでキャンペーンの受信者を指定できます。
    tags:
      - Other Filters
  - name: "Random Bucket #"
    display_name: "ランダムバケット番号"
    description: ランダムに割り当てられた番号（0〜9999を含む）でユーザーをセグメント化します。A/Bテストや多変量テスト用に、真にランダムなユーザーの均等に分布されたセグメントを作成できます。
    tags:
      - Other Filters
  - name: Session Count
    display_name: "セッション数"
    description: ワークスペース内のいずれかのアプリでのセッション数でユーザーをセグメント化します。
    tags:
      - Sessions
  - name: Session Count For App
    display_name: "アプリごとのセッション数"
    description: 特定の指定されたアプリでのセッション数でユーザーをセグメント化します。
    tags:
      - Sessions
  - name: X Sessions In Last Y Days
    display_name: "過去Y日間にXセッション"
    description: 指定された暦日数（1〜30日）の間に、アプリでのセッション数（0〜50回）でユーザーをセグメント化します。<br> <a href="/docs/x-in-y-behavior">X-in-Y動作の詳細はこちらをご覧ください。</a>
    tags:
      - Sessions
  - name: First Used App
    display_name: "アプリの初回使用"
    description: ユーザーがアプリを開いた最も早い記録時間でセグメント化します。<em>これは、Braze SDKが統合されたバージョンのアプリを使用した最初のセッションをキャプチャします。</em>最大ルックバック期間は100年です。（24時間期間）<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Sessions
  - name: First Used Specific App
    display_name: "特定アプリの初回使用"
    description: ワークスペース内のいずれかのアプリを開いた最も早い記録時間でユーザーをセグメント化します。最大ルックバック期間は100年です。（24時間期間）<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Sessions
  - name: Last Used App
    display_name: "アプリの最終使用"
    description: ユーザーがアプリを開いた最新の時間でセグメント化します。最大ルックバック期間は100年です。（24時間期間）<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Sessions
  - name: Last Used Specific App
    display_name: "特定アプリの最終使用"
    description: 特定の指定されたアプリを開いた最新の時間でユーザーをセグメント化します。最大ルックバック期間は100年です。（24時間期間）<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Sessions
  - name: Median Session Duration
    display_name: "セッション時間の中央値"
    description: アプリでのセッション時間の中央値でユーザーをセグメント化します。
    tags:
      - Sessions
  - name: Received Message from Campaign
    display_name: "キャンペーンからのメッセージ受信"
    description: 特定のキャンペーンを受信したかどうかでユーザーをセグメント化します。<br><br>Content Cards、バナー、アプリ内メッセージの場合、これはユーザーがインプレッションを記録した時点であり、カードやアプリ内メッセージが送信された時点ではありません。<br><br>プッシュとWebhookの場合、これはメッセージがユーザーに送信された時点です。<br><br>WhatsAppの場合、これは最後のメッセージAPIリクエストがWhatsAppに送信された時点であり、メッセージがユーザーのデバイスに配信された時点ではありません。<br><br>メールの場合、ターゲットのユーザープロファイルは、メールリクエストがメールサービスプロバイダーに送信された時点でこのフィルターに一致します（実際に配信されたかどうかに関係なく）。<br><br>SMSおよびRCSの場合、ユーザーは送信時にメッセージを「受信した」とみなされます。メッセージがユーザーのデバイスに届かなかった場合でも、ユーザーはこのフィルターに一致します。<br><br>メッセージが配信、開封、またはクリックされると、Brazeは同じチャネル識別子（メールアドレスや電話番号など）を共有するすべてのプロファイルのデータを更新するため、メッセージを受信した人と識別子を共有するユーザーは、そのプロファイルにキャンペーンが直接送信されていなくても、このフィルターに一致する場合があります。
    tags:
      - Retargeting
  - name: Received Campaign Variant
    display_name: "キャンペーンバリアントの受信"
    description: 多変量キャンペーンのどのバリアントを受信したかでユーザーをセグメント化します。<br><br>このフィルターは多変量および多変量クイックプッシュキャンペーンに適用されます。APIキャンペーン、標準マルチチャネルキャンペーン、およびフィーチャーフラグ実験キャンペーンは、キャンペーンセレクターに表示されません。Webhookのみのキャンペーンもキャンペーンセレクターに表示されません。<br><br>Content Cards、バナー、アプリ内メッセージの場合、これはユーザーがインプレッションを記録した時点であり、カードやアプリ内メッセージが送信された時点ではありません。<br><br>プッシュとWebhookの場合、これはメッセージがユーザーに送信された時点です。<br><br>WhatsAppの場合、これは最後のメッセージAPIリクエストがWhatsAppに送信された時点であり、メッセージがユーザーのデバイスに配信された時点ではありません。<br><br>メールの場合、ターゲットのユーザープロファイルは、メールリクエストがメールサービスプロバイダーに送信された時点でこのフィルターに一致します（実際に配信されたかどうかに関係なく）。<br><br>SMSおよびRCSの場合、ユーザーは送信時にメッセージを「受信した」とみなされます。メッセージがユーザーのデバイスに届かなかった場合でも、ユーザーはこのフィルターに一致します。<br><br>メッセージが配信、開封、またはクリックされると、Brazeは同じチャネル識別子（メールアドレスや電話番号など）を共有するすべてのプロファイルのデータを更新するため、メッセージを受信した人と識別子を共有するユーザーは、そのプロファイルにキャンペーンが直接送信されていなくても、このフィルターに一致する場合があります。
    tags:
      - Retargeting
  - name: Received Message from Canvas Step
    display_name: "キャンバスステップからのメッセージ受信"
    description: 特定のキャンバスコンポーネントを受信したかどうかでユーザーをセグメント化します。<br><br>Content Cardsとアプリ内メッセージの場合、これはユーザーがインプレッションを記録した時点であり、カードやアプリ内メッセージが送信された時点ではありません。<br><br>プッシュとWebhookの場合、これはメッセージがユーザーに送信された時点です。<br><br>WhatsAppの場合、これは最後のメッセージAPIリクエストがWhatsAppに送信された時点であり、メッセージがユーザーのデバイスに配信された時点ではありません。<br><br>メールの場合、ターゲットのユーザープロファイルは、メールリクエストがメールサービスプロバイダーに送信された時点でこのフィルターに一致します（実際に配信されたかどうかに関係なく）。<br><br>SMSおよびRCSの場合、ユーザーは送信時にメッセージを「受信した」とみなされます。メッセージがユーザーのデバイスに届かなかった場合でも、ユーザーはこのフィルターに一致します。<br><br>メッセージが配信、開封、またはクリックされると、Brazeは同じチャネル識別子（メールアドレスや電話番号など）を共有するすべてのプロファイルのデータを更新するため、メッセージを受信した人と識別子を共有するユーザーは、そのプロファイルにキャンペーンが直接送信されていなくても、このフィルターに一致する場合があります。
    tags:
      - Retargeting
  - name: Last Received Message from Specific Canvas Step
    display_name: "特定キャンバスステップからの最終メッセージ受信"
    description: 特定のキャンバスコンポーネントを受信した時期でユーザーをセグメント化します。最大ルックバック期間は100年です。<br><br>配信、開封、またはクリックが発生すると、同じチャネル識別子（メールアドレスや電話番号など）を共有するすべてのプロファイルのデータが更新されるため、メッセージを受信した人と識別子を共有するユーザーは、明示的にメッセージが送信されていなくても、このフィルターに一致する場合があります。重複からユーザープロファイルを分離するには、「Entered Canvas Variation」を使用してください。<br><br>このフィルターは、ユーザーが他のキャンバスコンポーネントを受信した時期は考慮しません。
    tags:
      - Retargeting
  - name: Last Received Message from Specific Campaign
    display_name: "特定キャンペーンからの最終メッセージ受信"
    description: 特定のキャンペーンを受信したかどうかでユーザーをセグメント化します。最大ルックバック期間は100年です。<br><br>配信、開封、またはクリックが発生すると、同じチャネル識別子（メールアドレスや電話番号など）を共有するすべてのプロファイルのデータが更新されるため、メッセージを受信した人と識別子を共有するユーザーは、明示的にメッセージが送信されていなくても、このフィルターに一致する場合があります。<br><br>このフィルターは、ユーザーが他のキャンペーンを受信した時期は考慮しません。
    tags:
      - Retargeting
  - name: Received Message from Campaign or Canvas with Tag
    display_name: "タグ付きキャンペーンまたはキャンバスからのメッセージ受信"
    description: 特定のタグを持つ特定のキャンペーンまたはキャンバスを受信したかどうかでユーザーをセグメント化します。<br><br>このフィルターの実行時に、Brazeは選択されたタグを使用する直近200件の送信済みキャンペーンおよびキャンバスのみを評価します。<br><br>Content Cards、バナー（キャンペーンのみ）、アプリ内メッセージの場合、これはユーザーがインプレッションを記録した時点であり、カードやアプリ内メッセージが送信された時点ではありません。<br><br>プッシュとWebhookの場合、これはメッセージがユーザーに送信された時点です。<br><br>WhatsAppの場合、これは最後のメッセージAPIリクエストがWhatsAppに送信された時点であり、メッセージがユーザーのデバイスに配信された時点ではありません。<br><br>メールの場合、ターゲットのユーザープロファイルは、メールリクエストがメールサービスプロバイダーに送信された時点でこのフィルターに一致します（実際に配信されたかどうかに関係なく）。<br><br>SMSおよびRCSの場合、ユーザーは送信時にメッセージを「受信した」とみなされます。メッセージがユーザーのデバイスに届かなかった場合でも、ユーザーはこのフィルターに一致します。<br><br>メッセージが配信、開封、またはクリックされると、Brazeは同じチャネル識別子（メールアドレスや電話番号など）を共有するすべてのプロファイルのデータを更新するため、メッセージを受信した人と識別子を共有するユーザーは、そのプロファイルにキャンペーンが直接送信されていなくても、このフィルターに一致する場合があります。
    tags:
      - Retargeting
  - name: Last Received Message from Campaign or Canvas With Tag
    display_name: "タグ付きキャンペーンまたはキャンバスからの最終メッセージ受信"
    description: 特定のタグを持つ特定のキャンペーンまたはキャンバスを受信した時期でユーザーをセグメント化します。このフィルターは、ユーザーが他のキャンペーンやキャンバスを受信した時期は考慮しません。最大ルックバック期間は100年です。（24時間期間）
    tags:
      - Retargeting
  - name: Has Never Received a Message from Campaign or Canvas Step
    display_name: "キャンペーンまたはキャンバスステップからのメッセージ未受信"
    description: いずれかのキャンペーンまたはキャンバスコンポーネントを受信したかどうかでユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: Last Received Email
    display_name: "最終メール受信"
    description: メールメッセージを最後に受信した時間でユーザーをセグメント化します。最大ルックバック期間は100年です。（24時間期間）<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Retargeting
  - name: Last Received Push
    display_name: "最終プッシュ受信"
    description: プッシュ通知を最後に受信した時間でユーザーをセグメント化します。最大ルックバック期間は100年です。（24時間期間）<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Retargeting
  - name: Last In App Message Impression
    display_name: "最終アプリ内メッセージインプレッション"
    description: アプリ内メッセージを最後に閲覧した時間でユーザーをセグメント化します。最大ルックバック期間は100年です。
    tags:
      - Retargeting
  - name: Last Received SMS
    display_name: "最終SMS受信"
    description: 最後のSMS、MMS、またはRCSメッセージがSMSまたはRCSプロバイダーに配信された時間でユーザーをセグメント化します。メッセージがユーザーのデバイスに配信されたことを保証するものではありません。最大ルックバック期間は100年です。（24時間期間）<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Retargeting
  - name: Last Received Webhook
    display_name: "最終Webhook受信"
    description: Brazeがそのユーザーに対してWebhookを最後に送信した時間でユーザーをセグメント化します。最大ルックバック期間は100年です。（24時間期間）<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Retargeting
  - name: Last Received WhatsApp
    display_name: "最終WhatsApp受信"
    description: WhatsAppメッセージを最後に受信した時間でユーザーをセグメント化します。これは最後のメッセージAPIリクエストがWhatsAppに送信された時点であり、メッセージがユーザーのデバイスに配信された時点ではありません。最大ルックバック期間は100年です。（24時間期間）<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Retargeting
  - name: Live Activities Push to Start Registered for App
    display_name: "アプリのLive Activities Push to Start登録"
    description: 特定のアプリでiOSプッシュ通知を通じてLive Activityを開始するために登録されているかどうかでユーザーをセグメント化します。
    tags:
      - Devices
  - name: Clicked/Opened Campaign
    display_name: "キャンペーンのクリック/開封"
    description: 特定のキャンペーンとのインタラクションでフィルタリングします。アプリ内メッセージの場合、クリックにはボディクリックとボタンクリックが含まれます。閉じるアクションやXでメッセージを閉じる操作はカウントされません。<br><br>メールの場合、開封イベントにはマシンオープンと非マシンオープンの両方が含まれます。このフィルターには「opened any email (machine opens)」と「opened any email (other opens)」でフィルタリングするオプションも含まれます。購読解除リンクやユーザー設定センターのクリックはこのフィルターにカウントされません。複数のユーザーが同じメールアドレスを共有している場合:<br>- メールが開封またはクリックされると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージ送信後、開封またはクリック前にメールアドレスを変更した場合、開封またはクリックは元のユーザーではなく、そのメールアドレスを持つ残りのすべてのユーザーに適用されます。<br><br>SMSおよびRCSの場合、インタラクションは次のように定義されます:<br>- ユーザーが特定のキーワードカテゴリーに一致する返信SMSまたはRCSを最後に送信した場合。これは、この電話番号を持つすべてのユーザーが受信した最新のキャンペーンに帰属します。キャンペーンは過去4時間以内に受信されている必要があります。<br>- ユーザーが特定のキャンペーンからの、ユーザークリックトラッキングが有効になっているSMSまたはRCSメッセージ内の短縮リンクを最後に選択した場合。
    tags:
      - Retargeting
  - name: Clicked/Opened Campaign or Canvas With Tag
    display_name: "タグ付きキャンペーンまたはキャンバスのクリック/開封"
    description: 特定のタグを持つ特定のキャンペーンとのインタラクションでフィルタリングします。アプリ内メッセージの場合、クリックにはボディクリックとボタンクリックが含まれます。閉じるアクションやXでメッセージを閉じる操作はカウントされません。<br><br>メールの場合、開封イベントにはマシンオープンと非マシンオープンの両方が含まれます。このフィルターには「opened any email (machine opens)」と「opened any email (other opens)」でフィルタリングするオプションも含まれます。複数のユーザーが同じメールアドレスを共有している場合:<br>- メールが開封またはクリックされると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージ送信後、開封またはクリック前にメールアドレスを変更した場合、開封またはクリックは元のユーザーではなく、そのメールアドレスを持つ残りのすべてのユーザーに適用されます。<br><br>SMSおよびRCSの場合、インタラクションは次のように定義されます:<br>- ユーザーが特定のキーワードカテゴリーに一致する返信SMSまたはRCSを最後に送信した場合。これは、この電話番号を持つすべてのユーザーが受信した最新のキャンペーンに帰属します。キャンペーンは過去4時間以内に受信されている必要があります。<br>- ユーザーが特定のタグ付きキャンペーンまたはキャンバスステップからの、ユーザークリックトラッキングが有効になっているSMSまたはRCSメッセージ内の短縮リンクを最後に選択した場合。
    tags:
      - Retargeting
  - name: Clicked/Opened Step
    display_name: "ステップのクリック/開封"
    description: 特定のキャンバスコンポーネントとのインタラクションでフィルタリングします。アプリ内メッセージの場合、クリックにはボディクリックとボタンクリックも含まれます。閉じるアクションやXでメッセージを閉じる操作はカウントされません。<br><br>メールの場合、開封イベントにはマシンオープンと非マシンオープンの両方が含まれます。このフィルターには「opened any email (machine opens)」と「opened any email (other opens)」でフィルタリングするオプションも含まれます。<br><br>SMSおよびRCSの場合、インタラクションは次のように定義されます:<br>- ユーザーが特定のキーワードカテゴリーに一致する返信SMSまたはRCSを最後に送信した場合。これは、この電話番号を持つすべてのユーザーが受信した最新のキャンペーンに帰属します。キャンペーンは過去4時間以内に受信されている必要があります。<br>- ユーザーが特定のキャンバスステップからの、ユーザークリックトラッキングが有効になっているSMSまたはRCSメッセージ内の短縮リンクを最後に選択した場合。
    tags:
      - Retargeting
  - name: Clicked Alias in Campaign
    display_name: "キャンペーン内のエイリアスクリック"
    description: 特定のキャンペーン内の特定のエイリアスをクリックしたかどうかでユーザーをフィルタリングします。これはメールメッセージにのみ適用されます。<br><br>複数のユーザーが同じメールアドレスを共有している場合:<br>- メールが開封またはクリックされると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージ送信後、開封またはクリック前にメールアドレスを変更した場合、開封またはクリックは元のユーザーではなく、そのメールアドレスを持つ残りのすべてのユーザーに適用されます。
    tags:
      - Retargeting
  - name: Clicked Alias in Canvas Step
    display_name: "キャンバスステップ内のエイリアスクリック"
    description: 特定のキャンバス内の特定のエイリアスをクリックしたかどうかでユーザーをフィルタリングします。これはメールメッセージにのみ適用されます。<br><br>複数のユーザーが同じメールアドレスを共有している場合:<br>- メールが開封またはクリックされると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージ送信後、開封またはクリック前にメールアドレスを変更した場合、開封またはクリックは元のユーザーではなく、そのメールアドレスを持つ残りのすべてのユーザーに適用されます。
    tags:
      - Retargeting
  - name: Clicked Alias in Any Campaign or Canvas Step
    display_name: "任意のキャンペーンまたはキャンバスステップ内のエイリアスクリック"
    description: いずれかのキャンペーンまたはキャンバス内の特定のエイリアスをクリックしたかどうかでユーザーをフィルタリングします。これはメールメッセージにのみ適用されます。<br><br>複数のユーザーが同じメールアドレスを共有している場合:<br>- メールが開封またはクリックされると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージ送信後、開封またはクリック前にメールアドレスを変更した場合、開封またはクリックは元のユーザーではなく、そのメールアドレスを持つ残りのすべてのユーザーに適用されます。
    tags:
      - Retargeting
  - name: Hard Bounced
    display_name: "ハードバウンス"
    description: メールアドレスがハードバウンスしたかどうか（メールアドレスが無効など）でユーザーをセグメント化します。無効なメールを持つユーザーをエクスポートするには、<a href="/docs/api/endpoints/email/get_list_hard_bounces/"><code>/email/hard_bounces</code>エンドポイント</a> を呼び出すか、メールアドレスが空白でない、メールが利用不可、メール購読ステータスが購読解除でないなどのフィルターでセグメントを作成してください。
    tags:
      - Retargeting
  - name: Soft Bounced
    display_name: "ソフトバウンス"
    description: Y日間にX回ソフトバウンスしたかどうかでユーザーをセグメント化します。セグメントフィルターは過去30日間のみ遡ることができますが、セグメントエクステンションを使用するとさらに遡ることができます。<br><br>このフィルターは、Currentsのソフトバウンスイベントとは異なる動作をします。ソフトバウンスセグメントフィルターは、72時間のリトライ期間中に配信が成功しなかった場合にソフトバウンスをカウントします。Currentsでは、失敗したリトライごとにソフトバウンスイベントとして送信されます。
    tags:
      - Retargeting
  - name: Has Marked You As Spam
    display_name: "スパムとしてマーク"
    description: メッセージをスパムとしてマークしたかどうかでユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: Invalid Phone Number
    display_name: "無効な電話番号"
    description: 電話番号が無効かどうかでユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: Last Sent Specific SMS Inbound Keyword Category
    display_name: "特定SMS受信キーワードカテゴリーの最終送信"
    description: 特定の購読グループ内の特定のキーワードカテゴリーでSMS、MMS、またはRCSを最後に送信した時期でユーザーをセグメント化します。最大ルックバック期間は100年です。
    tags:
      - Retargeting
  - name: Converted From Campaign
    display_name: "キャンペーンからのコンバージョン"
    description: 特定のキャンペーンでコンバージョンしたかどうかでユーザーをセグメント化します。このフィルターにはコントロールグループのユーザーは含まれません。
    tags:
      - Retargeting
  - name: Converted From Canvas
    display_name: "キャンバスからのコンバージョン"
    description: 特定のキャンバスでコンバージョンしたかどうかでユーザーをセグメント化します。このフィルターにはコントロールグループのユーザーは含まれません。
    tags:
      - Retargeting
  - name: In Campaign Control Group
    display_name: "キャンペーンコントロールグループ所属"
    description: 特定の多変量キャンペーンのコントロールグループに所属していたかどうかでユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: In Canvas Control Group
    display_name: "キャンバスコントロールグループ所属"
    description: 特定のキャンバスのコントロールグループに所属していたかどうかでユーザーをセグメント化します。このフィルターはキャンバスに入ったユーザーのみを評価するため、入ったことのないユーザーは結果から完全に除外されます。<br><br>例えば、キャンバスのコントロールグループに所属していないユーザーをフィルタリングすると、キャンバスに入り、非コントロールバリアントに割り当てられたユーザーのみが返されます。キャンバスに入ったことのないユーザーは含まれません。キャンバスへの参加に関係なくすべてのユーザーを含めるには、代わりに<code>Entered Canvas Variation</code>フィルターを使用してください。
    tags:
      - Retargeting
  - name: Last Enrolled in Any Control Group
    display_name: "任意のコントロールグループへの最終登録"
    description: キャンペーン内でコントロールグループに最後に入った時間でユーザーをセグメント化します。最大ルックバック期間は100年です。<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Retargeting
  - name: Entered Canvas Variation
    display_name: "キャンバスバリエーションへの参加"
    description: 特定のキャンバスのバリエーションパスに入ったかどうかでユーザーをセグメント化します。このフィルターはすべてのユーザーを評価します。<br><br>例えば、キャンバスバリエーションのコントロールグループに入っていないユーザーをフィルタリングすると、キャンバスに入ったかどうかに関係なく、コントロールグループに所属していないすべてのユーザーが返されます。
    tags:
      - Retargeting
  - name: Last Received Any Message
    display_name: "任意のメッセージの最終受信"
    description: 最後に受信したメッセージを判定してユーザーをセグメント化します。最大ルックバック期間は100年です。（24時間期間）<br><br>Content Cards、バナー、アプリ内メッセージの場合、これはユーザーが最後にインプレッションを記録した時点であり、カードやアプリ内メッセージが最後に送信された時点ではありません。<br><br>プッシュとWebhookの場合、これはいずれかのメッセージがユーザーに送信された時点です。<br><br>WhatsAppの場合、これは最後のメッセージAPIリクエストがWhatsAppに送信された時点であり、メッセージがユーザーのデバイスに配信された時点ではありません。<br><br>メールの場合、ターゲットのユーザープロファイルは、メールリクエストがメールサービスプロバイダーに送信された時点でこのフィルターに一致します（実際に配信されたかどうかに関係なく）。<br><br>SMSおよびRCSの場合、ユーザーは送信時にメッセージを「受信した」とみなされます。メッセージがユーザーのデバイスに届かなかった場合でも、ユーザーはこのフィルターに一致します。<br><br>メッセージが配信、開封、またはクリックされると、Brazeは同じチャネル識別子（メールアドレスや電話番号など）を共有するすべてのプロファイルのデータを更新するため、メッセージを受信した人と識別子を共有するユーザーは、そのプロファイルにキャンペーンが直接送信されていなくても、このフィルターに一致する場合があります。<br><br>例:<br>最終メッセージ受信が1日未満前 = 24時間未満前<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Retargeting
  - name: Last Engaged With Message
    display_name: "メッセージとの最終エンゲージメント"
    description: メッセージングチャネル（バナー、Content Cards、メール、アプリ内、SMS、RCS、プッシュ、WhatsApp）のいずれかを最後にクリックまたは開封した時間でユーザーをセグメント化します。<br><br>Content Cards、バナー、アプリ内メッセージの場合、これはユーザーがインプレッションを記録した時点であり、カードやアプリ内メッセージが送信された時点ではありません。<br><br>プッシュとWebhookの場合、これはメッセージがユーザーに送信された時点です。<br><br>WhatsAppの場合、これは最後のメッセージAPIリクエストがWhatsAppに送信された時点であり、メッセージがユーザーのデバイスに配信された時点ではありません。<br><br>メールメッセージの場合、開封イベントにはマシンオープンと非マシンオープンの両方が含まれます。最大ルックバック期間は100年です。（24時間期間）<br><br>メールの場合、ターゲットのユーザープロファイルは、メールリクエストがメールサービスプロバイダーに送信された時点でこのフィルターに一致します（実際に配信されたかどうかに関係なく）。「opened any email (machine opens)」と「opened any email (other opens)」でフィルタリングするオプションも含まれます。<br><br>SMSおよびRCSの場合、これはユーザーがユーザークリックトラッキングが有効になっているメッセージ内の短縮リンクを最後に選択した時点です。<br><br>メッセージが配信、開封、またはクリックされると、Brazeは同じチャネル識別子（メールアドレスや電話番号など）を共有するすべてのプロファイルのデータを更新するため、メッセージを受信した人と識別子を共有するユーザーは、そのプロファイルにキャンペーンが直接送信されていなくても、このフィルターに一致する場合があります。<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Retargeting
  - name: Clicked card
    display_name: "カードのクリック"
    description: 特定のContent Cardsをクリックしたかどうかでユーザーをセグメント化します。このフィルターは、「Clicked/Opened Campaign」、「Clicked/Opened Campaign or Canvas With Tag」、「Clicked/Opened Step」のサブフィルターとして利用できます。
    tags:
      - Retargeting
  - name: Feature Flags
    display_name: "フィーチャーフラグ"
    description: 特定の<a href="/docs/developer_guide/feature_flags">フィーチャーフラグ</a> が現在有効になっているユーザーのセグメントです。
    tags:
      - Retargeting
  - name: Subscription Group
    display_name: "購読グループ"
    description: メール、SMS、MMS、RCS、またはWhatsAppの購読グループでユーザーをセグメント化します。アーカイブされたグループは表示されず、使用できません。
    tags:
      - Channel subscription behavior
  - name: Email Available
    display_name: "メール利用可能"
    description: 有効なメールアドレスを持ち、メールに購読中またはオプトインしているかどうかでユーザーをセグメント化します。このフィルターは3つの条件をチェックします&#58; ユーザーがメールの購読解除をしているか、Brazeがハードバウンスを受信したか、メールがスパムとしてマークされたか。これらの条件のいずれかが満たされた場合、またはユーザーにメールが存在しない場合、そのユーザーは含まれません。<br><br>Email Availableが<code>false</code>のユーザーは、キャンペーンオーディエンスから除外され、メールを受信しません。送信設定がすべてのユーザー（購読解除済みユーザーを含む）に送信するように構成されている場合でも同様です。<br><br>オプトインステータスが重要なメールの場合、<a href="/docs/user_guide/audience/segments/segmentation_filters#email-address">Email Address</a> の代わりにEmail Availableを使用してください。追加の条件により、メールを受信する資格のあるユーザーをターゲットにできます。
    tags:
      - Channel subscription behavior
  - name: Email Opt In Date
    display_name: "メールオプトイン日"
    description: メールにオプトインした日付でユーザーをセグメント化します。最大ルックバック期間は100年です。
    tags:
      - Channel subscription behavior
  - name: Email Subscription Status
    display_name: "メール購読ステータス"
    description: メールの購読ステータスでユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: Email Unsubscribed Date
    display_name: "メール購読解除日"
    description: 今後のメールの購読解除をした日付でユーザーをセグメント化します。最大ルックバック期間は100年です。
    tags:
      - Channel subscription behavior
  - name: Foreground Push Enabled
    display_name: "フォアグラウンドプッシュ有効"
    description: 仮承認プッシュ認可を持つか、フォアグラウンドプッシュが有効なユーザーをセグメント化します。具体的には、このカウントには以下が含まれます:<br>1. プッシュの仮承認を受けたiOSユーザー。<br>2. いずれかのアプリでフォアグラウンドプッシュが有効で、プッシュ購読ステータスが購読解除でないユーザー。これらのユーザーについては、フォアグラウンドプッシュのみがカウントされます。<br><br>Foreground Push Enabledには、購読解除したユーザーは含まれません。<br><br>このフィルターでセグメント化した後、下部パネルの<em>到達可能なユーザー</em>で、Android、iOS、Webのそれぞれの内訳を確認できます。
    tags:
      - Channel subscription behavior
  - name: Foreground Push Enabled for App
    display_name: "アプリのフォアグラウンドプッシュ有効"
    description: デバイス上のアプリでプッシュが有効かどうかでセグメント化します。アプリのフォアグラウンドプッシュが有効なユーザーです。プッシュ購読ステータスは考慮されません。このカウントには、フォアグラウンドおよびバックグラウンドプッシュトークンの仮承認を受けたユーザーが含まれます。
    tags:
      - Channel subscription behavior
  - name: Background or Foreground Push Enabled
    display_name: "バックグラウンドまたはフォアグラウンドプッシュ有効"
    description: プッシュトークンを持ち、購読解除していないかどうかでセグメント化します。いずれかのアプリでバックグラウンドまたはフォアグラウンドプッシュが有効なユーザーです。
    tags:
      - Channel subscription behavior
  - name: Push Opt In Date
    display_name: "プッシュオプトイン日"
    description: プッシュにオプトインした日付でユーザーをセグメント化します。最大ルックバック期間は100年です。
    tags:
      - Channel subscription behavior
  - name: Push Subscription Status
    display_name: "プッシュ購読ステータス"
    description: プッシュの<a href="/docs/user_guide/channels/push/push_setup/push_subscription_states">購読ステータス</a> でユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: Push Unsubscribed Date
    display_name: "プッシュ購読解除日"
    description: 今後のプッシュ通知の購読解除をした日付でユーザーをセグメント化します。最大ルックバック期間は100年です。
    tags:
      - Channel subscription behavior
  - name: Purchased Product
    display_name: "購入した製品"
    description: アプリで購入した製品でユーザーをセグメント化します。
    tags:
      - Purchase behavior
  - name: Total Number of Purchases
    display_name: "購入合計回数"
    description: アプリでの購入回数でユーザーをセグメント化します。
    tags:
      - Purchase behavior
  - name: X Product Purchased In Y Days
    display_name: "Y日間にX製品を購入"
    description: 特定の製品が購入された回数でユーザーをフィルタリングします。
    tags:
      - Purchase behavior
  - name: X Purchases in Last Y Days
    display_name: "過去Y日間にX回購入"
    description: 指定された暦日数（1〜30日）の間に購入した回数（0〜50回）でユーザーをセグメント化します。<br> <a href="/docs/x-in-y-behavior">X-in-Y動作の詳細はこちらをご覧ください。</a>
    tags:
      - Purchase behavior
  - name: X Purchase Property In Y Days
    display_name: "Y日間にX回の購入プロパティ"
    description: 指定された暦日数（1〜30日）の間に、特定の購入プロパティに関連して購入が行われた回数でユーザーをセグメント化します。<br> <a href="/docs/x-in-y-behavior">X-in-Y動作の詳細はこちらをご覧ください。</a>
    tags:
      - Purchase behavior
  - name: First Made Purchase
    display_name: "初回購入"
    description: ユーザーがアプリで購入を行った最も早い時間でセグメント化します。最大ルックバック期間は100年です。
    tags:
      - Purchase behavior
  - name: First Purchase For App
    display_name: "アプリでの初回購入"
    description: ユーザーがアプリから購入を行った最も早い時間でセグメント化します。最大ルックバック期間は100年です。
    tags:
      - Purchase behavior
  - name: Last Made Purchase
    display_name: "最終購入"
    description: 最後に購入を行った時間でユーザーをフィルタリングします。最大ルックバック期間は100年です。
    tags:
      - Purchase behavior
  - name: Last Purchased Product
    display_name: "最終購入製品"
    description: 特定の製品を最後に購入した時期でユーザーをフィルタリングします。最大ルックバック期間は100年です。
    tags:
      - Purchase behavior
  - name: Money Spent
    display_name: "支出金額"
    description: アプリで支出した金額でユーザーをセグメント化します。
    tags:
      - Purchase behavior
  - name: X Money Spent in Y Days
    display_name: "Y日間にX金額を支出"
    description: 指定された暦日数（1〜30日）の間にアプリで支出した金額でユーザーをセグメント化します。この金額には直近50回の購入の合計のみが含まれます。<br> <a href="/docs/x-in-y-behavior">X-in-Y動作の詳細はこちらをご覧ください。</a>
    tags:
      - Purchase behavior
  - name: Last order placed (last 730 days)
    display_name: "最終注文（過去730日間）"
    description: 最後に注文を行った時期でユーザーをセグメント化します。これは注文完了の<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> に基づいています（eコマースイベントを追跡していないワークスペースにはこのフィルターのデータがありません）。ユーザーはこのフィルターに対して1日1回評価され、最大ルックバックウィンドウは過去2年間です。<br><br>このフィルターはベータ版です。このフィルターの使用に興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
    tags:
      - eCommerce
  - name: Total orders count (last 730 days)
    display_name: "注文合計数（過去730日間）"
    description: 過去2年間のユーザーの注文合計数でセグメント化します。注文完了の<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> に基づいています（eコマースイベントを追跡していないワークスペースにはこのフィルターのデータがありません）。このカウントにはキャンセルされた注文は含まれません。キャンセルされた注文は注文キャンセルの<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> を使用して追跡する必要があります。ユーザーはこのフィルターに対して1日1回評価されます。<br><br>このフィルターはベータ版です。このフィルターの使用に興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
    tags:
      - eCommerce
  - name: Total orders count
    display_name: "注文合計数"
    description: ユーザーの全期間にわたる注文合計数でセグメント化します。注文完了の<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> に基づいています（eコマースイベントを追跡していないワークスペースにはこのフィルターのデータがありません）。このカウントにはキャンセルされた注文は含まれません。キャンセルされた注文は注文キャンセルの<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> を使用して追跡する必要があります。ユーザーはこのフィルターに対してリアルタイムで評価されます。<br><br>このフィルターはベータ版です。このフィルターの使用に興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
    tags:
      - eCommerce
  - name: Total canceled orders count (last 730 days)
    display_name: "キャンセル注文合計数（過去730日間）"
    description: 過去2年間にユーザーがキャンセルした注文の合計数でセグメント化します。注文完了の<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> に基づいています（eコマースイベントを追跡していないワークスペースにはこのフィルターのデータがありません）。ユーザーはこのフィルターに対して1日1回評価されます。<br><br>このフィルターはベータ版です。このフィルターの使用に興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
    tags:
      - eCommerce
  - name: Customer lifetime value (last 730 days)
    display_name: "顧客LTV or 生涯価値（過去730日間）"
    description: ブランドとの購入履歴を通じてユーザーが生み出すと予想される総収益でセグメント化します。計算は過去730日間を考慮し、平均注文額（AOV）に注文合計数を掛け、ユーザーのアクティブな購入期間（最初の注文から最新の注文までの期間）を考慮します。このフィルターは<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> で追跡されたデータを使用します（eコマースイベントを追跡していないワークスペースにはこのフィルターのデータがありません）。ユーザーはこのフィルターに対して1日1回評価されます。<br><br>このフィルターはベータ版です。このフィルターの使用に興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
    tags:
      - eCommerce
  - name: Total refund value (last 730 days)
    display_name: "返金合計額（過去730日間）"
    description: 過去2年間にユーザーに付与された返金額でセグメント化します。注文返金の<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> に基づいています（eコマースイベントを追跡していないワークスペースにはこのフィルターのデータがありません）。ユーザーはこのフィルターに対して1日1回評価されます。<br><br>このフィルターはベータ版です。このフィルターの使用に興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
    tags:
      - eCommerce
  - name: Total refund value
    display_name: "返金合計額"
    description: ユーザーの全期間にわたって付与された返金の合計額でセグメント化します。注文返金の<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> に基づいています（eコマースイベントを追跡していないワークスペースにはこのフィルターのデータがありません）。ユーザーはこのフィルターに対してリアルタイムで評価されます。<br><br>このフィルターはベータ版です。このフィルターの使用に興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
    tags:
      - eCommerce
  - name: Total revenue (last 730 days)
    display_name: "合計収益（過去730日間）"
    description: 過去2年間のユーザーの注文から生成された合計収益でセグメント化します。注文返金の<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> に関連する収益を、注文完了のeコマースイベントに関連する収益から差し引いて計算されます（eコマースイベントを追跡していないワークスペースにはこのフィルターのデータがありません）。ユーザーはこのフィルターに対して1日1回評価されます。<br><br>このフィルターはベータ版です。このフィルターの使用に興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
    tags:
      - eCommerce
  - name: Total revenue
    display_name: "合計収益"
    description: ユーザーの全期間にわたる注文から生成された合計収益でセグメント化します。注文返金の<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> に関連する収益を、注文完了のeコマースイベントに関連する収益から差し引いて計算されます（eコマースイベントを追跡していないワークスペースにはこのフィルターのデータがありません）。ユーザーはこのフィルターに対してリアルタイムで評価されます。<br><br>このフィルターはベータ版です。このフィルターの使用に興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
    tags:
      - eCommerce
  - name: Average order value (last 730 days)
    display_name: "平均注文額（過去730日間）"
    description: 過去2年間のユーザーの注文の平均（平均値）額でセグメント化します。注文完了の<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> に基づいています（eコマースイベントを追跡していないワークスペースにはこのフィルターのデータがありません）。ユーザーはこのフィルターに対して1日1回評価されます。<br><br>このフィルターはベータ版です。このフィルターの使用に興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
    tags:
      - eCommerce
  - name: Country
    display_name: "国"
    description: 最後に示された国の位置情報でユーザーをセグメント化します。
    tags:
      - Demographic attributes
  - name: City
    display_name: "市区町村"
    description: 最後に示された市区町村の位置情報でユーザーをセグメント化します。
    tags:
      - Demographic attributes
  - name: Language
    display_name: "言語"
    description: 優先言語でユーザーをセグメント化します。
    tags:
      - Demographic attributes
  - name: Age
    display_name: "年齢"
    description: アプリ内で示された年齢でユーザーをセグメント化します。
    tags:
      - Demographic attributes
  - name: Birthday
    display_name: "誕生日"
    description: アプリ内で示された誕生日でユーザーをセグメント化します。<br>2月29日が誕生日のユーザーは、3月1日を含むセグメントに含まれます。<br><br>12月または1月の誕生日をターゲットにするには、ターゲットとする年の12か月の範囲内でのみフィルターロジックを挿入してください。つまり、前年の12月を遡ったり、翌年の1月を先取りしたりするロジックを挿入しないでください。例えば、12月の誕生日をターゲットにするには、「on December 31」、「before December 31」、または「after November 30」でフィルタリングできます。
    tags:
      - Demographic attributes
  - name: Gender
    display_name: "性別"
    description: アプリ内で示された性別でユーザーをセグメント化します。
    tags:
      - Demographic attributes
  - name: Unformatted Phone Number
    display_name: "未フォーマット電話番号"
    description: 未フォーマットの電話番号でユーザーをセグメント化します。かっこ、ダッシュ、その他の記号は含まれません。
    tags:
      - Demographic attributes
  - name: First Name
    display_name: "名"
    description: アプリ内で示された名でユーザーをセグメント化します。
    tags:
      - Demographic attributes
  - name: Last Name
    display_name: "姓"
    description: アプリ内で示された姓でユーザーをセグメント化します。
    tags:
      - Demographic attributes
  - name: Has App
    display_name: "アプリ所有"
    description: ユーザーがアプリをインストールしたことがあるかどうかでセグメント化します。これには、現在アプリがインストールされているユーザーと、過去にアンインストールしたユーザーが含まれます。通常、このフィルターに含まれるには、ユーザーがアプリを開く（セッションを開始する）必要があります。ただし、ユーザーがBrazeにインポートされ、手動でアプリに関連付けられた場合など、いくつかの例外があります。
    tags:
      - App
  - name: Most Recent App Version Name
    display_name: "最新アプリバージョン名"
    description: ユーザーのアプリの最新バージョン名でセグメント化します。<br><br>「less than」または「less than or equal to」を使用する場合、メインアプリバージョンが存在しない場合、このフィルターは<code>true</code>を返します。これは、ユーザーがそのアプリバージョンよりも古いためです。つまり、ユーザーの最後のメインアプリバージョンが存在しない場合、自動的にフィルターに一致します。
    tags:
      - App
  - name: Most Recent App Version Number
    display_name: "最新アプリバージョン番号"
    description: ユーザーのアプリの最新バージョン番号でセグメント化します。かっこ内のバージョン番号がフィルタリングに使用され、その前の番号は参照用です。例えば、「3.7.0(134.0.0.0)」の場合、「134.0.0.0」がフィルタリングされるバージョン番号です。<br><br>「less than」または「less than or equal to」を使用する場合、メインアプリバージョンが存在しない場合、このフィルターは<code>true</code>を返します。これは、ユーザーがそのアプリバージョンよりも古いためです。つまり、ユーザーの最後のメインアプリバージョンが存在しない場合、自動的にフィルターに一致します。<br><br>現在のアプリバージョンが反映されるまでに時間がかかる場合があります。ユーザープロファイルのアプリバージョンは、SDKによって情報がキャプチャされた時点で更新されますが、これはユーザーがアプリを開いた時に依存します。ユーザーがアプリを開かない場合、現在のバージョンは更新されません。これらのフィルターは遡及的にも適用されません。現在および将来のバージョンに対して「greater than」または「equal」を使用することをお勧めしますが、過去のバージョンフィルターを使用すると予期しない動作が発生する可能性があります。
    tags:
      - App
  - name: Uninstalled
    display_name: "アンインストール済み"
    description: バックエンドで現在アンインストール済みとしてマークされているかどうかでユーザーをセグメント化します。アンインストール後にアプリを再インストールしたユーザーは含まれません。このフィルターは現在のアンインストール状態を反映しており、すべてのアンインストールイベントの履歴ログではありません。最大ルックバック期間は100年です。
    tags:
      - Uninstall
  - name: Device Carrier
    display_name: "デバイスキャリア"
    description: デバイスキャリアでユーザーをセグメント化します。
    tags:
      - Devices
  - name: Device Count
    display_name: "デバイス数"
    description: アプリを使用したデバイスの数でユーザーをセグメント化します。
    tags:
      - Devices
  - name: Device Model
    display_name: "デバイスモデル"
    description: 携帯電話のモデルバージョンでユーザーをセグメント化します。
    tags:
      - Devices
  - name: Device OS
    display_name: "デバイスOS"
    description: 指定されたオペレーティングシステムを持つ1つ以上のデバイスを持つユーザーをセグメント化します。オペレーティングシステムの範囲でユーザーをセグメント化するには、<a href="/docs/user_guide/audience/segments/segmentation_filters#device-os-version-number">Device OS Version Number</a> フィルターを使用してください。
    tags:
      - Devices
  - name: Device OS Version Number
    display_name: "デバイスOSバージョン番号"
    description: 指定された範囲内のオペレーティングシステムバージョンを持つ1つ以上のデバイスを持つユーザーをセグメント化します。例えば、iOSオペレーティングシステムバージョンが26.0以上のユーザーをターゲットにできます。
    tags:
      - Devices
  - name: Most Recent Device Locale
    display_name: "最新デバイスロケール"
    description: 最近使用されたデバイスの<a href="/docs/user_guide/messaging/messaging_fundamentals/localization">ロケール情報</a> でユーザーをセグメント化します。
    tags:
      - Devices
  - name: Most Recent Watch Model
    display_name: "最新ウォッチモデル"
    description: 最新のスマートウォッチモデルでユーザーをセグメント化します。
    tags:
      - Devices
  - name: Provisionally Authorized on iOS
    display_name: "iOSでの仮承認"
    description: 特定のアプリでiOS 12の仮承認を受けたユーザーを検索できます。
    tags:
      - Devices
  - name: Web Browser
    display_name: "Webブラウザー"
    description: Webサイトへのアクセスに使用するWebブラウザーでユーザーをセグメント化します。このフィルターは、最近使用されたブラウザーだけでなく、ユーザーのデバイス履歴内のすべてのブラウザーに対してマッチします。
    tags:
      - Devices
  - name: Device IDFA
    display_name: "デバイスIDFA"
    description: テスト用にIDFAでキャンペーンの受信者を指定できます。
    tags:
      - Advertising use cases
  - name: Device IDFV
    display_name: "デバイスIDFV"
    description: テスト用にIDFVでキャンペーンの受信者を指定できます。
    tags:
      - Advertising use cases
  - name: Device Google Ad ID
    display_name: "デバイスGoogle広告ID"
    description: Google広告IDでユーザーをセグメント化します。
    tags:
      - Advertising use cases
  - name: Device Roku Ad ID
    display_name: "デバイスRoku広告ID"
    description: Roku広告IDでユーザーをセグメント化します。
    tags:
      - Advertising use cases
  - name: Device Windows Ad ID
    display_name: "デバイスWindows広告ID"
    description: Windows広告IDでユーザーをセグメント化します。
    tags:
      - Advertising use cases
  - name: Ad Tracking Enabled
    display_name: "広告トラッキング有効"
    description: ユーザーが広告トラッキングにオプトインしているかどうかに基づいてフィルタリングできます。広告トラッキングは、AppleがすべてのiOSデバイスに割り当てるIDFAまたは「広告主向け識別子」に関連しており、SDKで設定できます。この識別子により、広告主はユーザーを追跡し、ターゲット広告を配信できます。
    tags:
      - Advertising use cases
  - name: Most Recent Location
    display_name: "最新の位置情報"
    description: アプリを使用した最後に記録された位置情報でユーザーをセグメント化します。
    tags:
      - Location
  - name: Location Available
    display_name: "位置情報利用可能"
    description: 位置情報を報告したかどうかでユーザーをセグメント化します。このフィルターを使用するには、アプリに<a href="/docs/search?query=location%20tracking">位置情報の追跡が統合されている</a> 必要があります。
    tags:
      - Location
  - name: Amplitude Cohorts
    display_name: "Amplitudeコホート"
    description: Amplitudeを使用しているクライアントは、Amplitudeでコホートを選択してインポートすることでセグメントを補完できます。
    tags:
      - Cohort membership
  - name: Census Cohorts
    display_name: "Censusコホート"
    description: Censusを使用しているクライアントは、Censusでコホートを選択してインポートすることでセグメントを補完できます。
    tags:
      - Cohort membership
  - name: Heap Cohorts
    display_name: "Heapコホート"
    description: Heapを使用しているクライアントは、Heapでコホートを選択してインポートすることでセグメントを補完できます。
    tags:
      - Cohort membership
  - name: Hightouch Cohorts
    display_name: "Hightouchコホート"
    description: Hightouchを使用しているクライアントは、Hightouchでコホートを選択してインポートすることでセグメントを補完できます。
    tags:
      - Cohort membership
  - name: Kubit Cohorts
    display_name: "Kubitコホート"
    description: Kubitを使用しているクライアントは、Kubitでコホートを選択してインポートすることでセグメントを補完できます。
    tags:
      - Cohort membership
  - name: Mixpanel Cohorts
    display_name: "Mixpanelコホート"
    description: Mixpanelを使用しているクライアントは、Mixpanelでコホートを選択してインポートすることでセグメントを補完できます。
    tags:
      - Cohort membership
  - name: Segment Cohorts
    display_name: "Segmentコホート"
    description: Segmentを使用しているクライアントは、Segmentでコホートを選択してインポートすることでセグメントを補完できます。
    tags:
      - Cohort membership
  - name: Tinyclues Cohorts
    display_name: "Tinycluesコホート"
    description: Tinycluesを使用しているクライアントは、Tinycluesでコホートを選択してインポートすることでセグメントを補完できます。
    tags:
      - Cohort membership
  - name: Install Attribution Ad
    display_name: "インストールアトリビューション広告"
    description: インストールが帰属する広告でユーザーをセグメント化します。
    tags:
      - User Attributes
  - name: Install Attribution Adgroup
    display_name: "インストールアトリビューション広告グループ"
    description: インストールが帰属する広告グループでユーザーをセグメント化します。
    tags:
      - Install attribution
  - name: Install Attribution Campaign
    display_name: "インストールアトリビューションキャンペーン"
    description: インストールが帰属する広告キャンペーンでユーザーをセグメント化します。
    tags:
      - Install attribution
  - name: Install Attribution Source
    display_name: "インストールアトリビューションソース"
    description: インストールが帰属するソースでユーザーをセグメント化します。
    tags:
      - Install attribution
  - name: Churn Risk Category
    display_name: "解約リスクカテゴリー"
    description: 特定の予測に基づく解約リスクカテゴリーでユーザーをセグメント化します。
    tags:
      - Intelligence and predictive
  - name: Churn Risk Score
    display_name: "解約リスクスコア"
    description: 特定の予測に基づく解約リスクスコアでユーザーをセグメント化します。
    tags:
      - Intelligence and predictive
  - name: Event Likelihood Category
    display_name: "イベント可能性カテゴリー"
    description: 特定の予測に基づくイベント実行の可能性カテゴリーでユーザーをセグメント化します。
    tags:
      - Intelligence and predictive
  - name: Event Likelihood Score
    display_name: "イベント可能性スコア"
    description: 特定の予測に基づくイベント実行の可能性スコアでユーザーをセグメント化します。
    tags:
      - Intelligence and predictive
  - name: Intelligent Channel
    display_name: "インテリジェントチャネル"
    description: 過去3か月間で最もアクティブなチャネルでユーザーをセグメント化します。
    tags:
      - Intelligence and predictive
  - name: Message Open Likelihood
    display_name: "メッセージ開封の可能性"
    description: 指定されたチャネルでメッセージを<a href="/docs/user_guide/brazeai/intelligence_suite/intelligent_channel#individual-channels">開封する可能性</a> に基づいて、0〜100のスケールでユーザーをフィルタリングします。チャネルの可能性を測定するのに十分なデータがないユーザーは、「is blank」を使用して選択できます。<br><br>メールの場合、マシンオープンは可能性の計算から除外されます。
    tags:
      - Intelligence and predictive
  - name: Number of Facebook Friends Using App
    display_name: "アプリを使用しているFacebook友達の数"
    description: 同じアプリを使用しているFacebook友達の数でユーザーをセグメント化します。
    tags:
      - Social activity
  - name: Connected Facebook
    display_name: "Facebook接続済み"
    description: アプリをFacebookに接続したかどうかでユーザーをセグメント化します。
    tags:
      - Social activity
  - name: Connected Twitter
    display_name: "Twitter接続済み"
    description: アプリをX（旧Twitter）に接続したかどうかでユーザーをセグメント化します。
    tags:
      - Social activity
  - name: Number of Twitter Followers
    display_name: "Twitterフォロワー数"
    description: X（旧Twitter）のフォロワー数でユーザーをセグメント化します。
    tags:
      - Social activity
  - name: Phone Number
    display_name: "電話番号"
    description: E.164形式の電話番号フィールドでユーザーをセグメント化します。<br><br>電話番号がBrazeに送信されると、BrazeはSMS、RCS、WhatsAppチャネルでの送信に使用される<a href="/docs/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#import-phone-numbers">E.164形式</a> に変換しようとします。番号が正しくフォーマットされていない場合、変換プロセスが失敗し、ユーザープロファイルに未フォーマットの電話番号はあるが送信用電話番号がないという結果になります。このセグメントフィルターは、E.164形式の電話番号（利用可能な場合）でユーザーを返します。<br><br>ユースケース:<br>- SMS、RCS、またはWhatsAppメッセージを送信する際に、最も正確なターゲットオーディエンスサイズを把握するためにこのフィルターを使用します。<br>- このフィルターで正規表現（regex）を使用して、特定の国コードの電話番号でセグメント化します。<br>- E.164変換プロセスに失敗した電話番号でユーザーをセグメント化するためにこのフィルターを使用します。
    tags:
      - Other Filters
---