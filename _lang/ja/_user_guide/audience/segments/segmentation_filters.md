---
page_order: 3
nav_title: セグメンテーションフィルター
article_title: セグメンテーションフィルター
layout: glossary_page
glossary_top_header: "セグメンテーションフィルター"
glossary_top_text: "Braze SDKは、特定の機能や属性に基づいてユーザーをセグメント化し、ターゲティングするための強力なフィルターを提供します。フィルターカテゴリーでこれらのフィルターを検索または絞り込むことができます。<br><br>ユーザーのセグメント化に使用できるさまざまなカスタム属性データタイプについては、<a href=\"/docs/user_guide/data/activation/attributes/custom_attributes#custom-attribute-data-types\">カスタム属性データタイプ</a> をご覧ください。"

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
    description: フィルターが使用される場所（Segments、Campaignsなど）でSegmentメンバーシップに基づいてフィルタリングし、1つのCampaign内で複数の異なるSegmentsをターゲットにできます。<br><br>このフィルターを既に使用しているSegmentsは、他のSegmentsにさらに含めたりネストしたりすることはできません。これは、Segment AがSegment Bを含み、Segment Bが再びSegment Aを含もうとするサイクルが発生する可能性があるためです。そのような場合、Segmentは自身を参照し続け、実際に誰がそのSegmentに属しているかを計算することが不可能になります。また、このようなSegmentsのネストは複雑さを増し、処理速度を低下させる可能性があります。代わりに、同じフィルターを使用して含めたいSegmentを再作成してください。
    tags:
      - Segment or CSV membership
  - name: Braze Segment Extensions
    description: Brazeダッシュボードでセグメントエクステンションを作成した後、Segmentにそれらのエクステンションを含めるか除外するかを選択できます。
    tags:
      - Segment or CSV membership
  - name: Updated/Imported from CSV
    description: ユーザーがCSVアップロードの一部であったかどうかに基づいてセグメント化します。
    tags:
      - Segment or CSV membership
  - name: Custom Attributes
    description: ユーザーがカスタム記録された属性値に一致するかどうかを判定します。<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Custom attribute
  - name: Created At
    description: ユーザープロファイルが作成された日時でセグメント化します。ユーザーがCSVまたはAPIで追加された場合、このフィルターは追加された日付を反映します。ユーザーがCSVまたはAPIで追加されておらず、SDKによって最初のセッションが追跡された場合、このフィルターはその最初のセッションの日付を反映します。
    tags:
      - Other Filters
  - name: Created From
    description: "ユーザープロファイルが作成された場所でセグメント化します。<br><br>以下の値がサポートされています:<br>- SDK (<code>sdk</code>): Braze SDKを通じて作成されたユーザープロファイル。<br>- REST API (<code>rest</code>): Braze REST APIを通じて作成されたユーザープロファイル。<br>- プッシュトークンインポート (<code>pti</code>): プッシュトークンインポートを通じて作成されたユーザープロファイル。<br>- CSV (<code>csv</code>): CSVインポートを通じて作成されたユーザープロファイル。<br>- デモ (<code>demo</code>): デモデータを通じて作成されたユーザープロファイル。<br>- SMS (<code>sms</code>): SMSを通じて作成されたユーザープロファイル。<br>- Shopify (<code>shopify</code>): Shopifyを通じて作成されたユーザープロファイル。<br>- WhatsApp (<code>whats_app</code>): WhatsAppを通じて作成されたユーザープロファイル。<br>- プロバイダーイベント (<code>provider_event</code>): プロバイダーイベントを通じて作成されたユーザープロファイル。<br>- プロバイダー同期 (<code>provider_sync</code>): プロバイダー同期を通じて作成されたユーザープロファイル。<br>- ランディングページ (<code>landing_page</code>): ランディングページを通じて作成されたユーザープロファイル。"
    tags:
      - Other Filters
  - name: Nested Custom Attributes
    description: カスタム属性のプロパティである属性です。<br><br>階層化された時間カスタム属性をフィルタリングする場合、「年の日」または「時間」に基づいてフィルタリングすることを選択できます。「年の日」は比較のために月と日のみをチェックします。「時間」は年を含む完全なタイムスタンプを比較します。
    tags:
      - Custom attribute
  - name: Day of Recurring Event
    description: このフィルターは「日付」データタイプのカスタム属性の月と日を確認しますが、年は確認しません。このフィルターは年次イベントに便利です。<br><br>タイムゾーン&#58;<br>このフィルターは、メッセージがローカルタイムスケジューリングオプションを使用して送信される限り、ユーザーのタイムゾーンに合わせて調整されます。それ以外の場合、このフィルターは会社のタイムゾーンを使用します。
    tags:
      - Custom attribute
  - name: Custom Event
    description: ユーザーが特別に記録されたイベントを実行したかどうかを判定します。<br><br>例:<br>プロパティactivity_nameでアクティビティが完了。<br><br>タイムゾーン:<br>UTC - 暦日 = 1暦日は24〜48時間のユーザー履歴を確認します
    tags:
      - Custom events
  - name: First Did Custom Event
    description: ユーザーが特別に記録されたイベントを実行した最も早い時間を判定します。（24時間期間）<br><br>例:<br>初回のカート放棄が1日未満前<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Custom events
  - name: Last Did Custom Event
    description: ユーザーが特別に記録されたイベントを実行した最新の時間を判定します。このフィルターは0.25時間などの小数をサポートしています。（24時間期間）<br><br>例:<br>最後のカート放棄が1日未満前<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Custom events
  - name: X Custom Event In Y Days
    description: 指定された暦日数（1〜30日）の間に、ユーザーが特別に記録されたイベントを0〜50回実行したかどうかを判定します。（暦日 = 1暦日は24〜48時間のユーザー履歴を確認します）<br> <a href="/docs/x-in-y-behavior/">X-in-Y動作の詳細はこちらをご覧ください。</a> <br><br>例:<br>過去1暦日にカート放棄がちょうど0回<br><br>タイムゾーン:<br>UTC - すべてのタイムゾーンに対応するため、1暦日はSegmentが評価される時間に応じて24〜48時間のユーザー履歴を確認します。2暦日の場合は48〜72時間のユーザー履歴を確認し、以降同様です。
    tags:
      - Custom events
  - name: X Custom Event Property In Y Days
    description: 指定された暦日数（1〜30日）の間に、ユーザーが特定のプロパティに関連して特別に記録されたイベントを0〜50回実行したかどうかを判定します。（暦日 = 1暦日は24〜48時間のユーザー履歴を確認します）<br><a href="/docs/x-in-y-behavior/">X-in-Y動作の詳細はこちらをご覧ください。</a> <br><br>例:<br>過去1暦日にプロパティ「event_name」でお気に入りに追加がちょうど0回<br><br>タイムゾーン:<br>UTC - すべてのタイムゾーンに対応するため、1暦日はSegmentが評価される時間に応じて24〜48時間のユーザー履歴を確認します。2暦日の場合は48〜72時間のユーザー履歴を確認し、以降同様です。
    tags:
      - Custom events
  - name: Email Address
    description: テスト用に個別のメールアドレスでCampaignの受信者を指定できます。また、フィルター内の「メールアドレスが空白でない」指定子を使用して、すべてのユーザー（配信停止済みを含む）にトランザクションメールを送信し、オプトインステータスに関係なくメールの配信を最大化することもできます。<br><br>このフィルターはユーザープロファイルにメールアドレスがあるかどうかのみをチェックしますが、<a href="/docs/user_guide/audience/segments/segmentation_filters#email-available">メール利用可能</a> フィルターは追加の条件をチェックします。
    tags:
      - Other Filters
  - name: External User ID
    description: テスト用に個別のユーザーIDでCampaignの受信者を指定できます。
    tags:
      - Other Filters
  - name: "Random Bucket #"
    description: ランダムに割り当てられた番号（0〜9999を含む）でユーザーをセグメント化します。A/Bテストや多変量テスト用に、真にランダムなユーザーの均等に分布されたSegmentsを作成できます。
    tags:
      - Other Filters
  - name: Session Count
    description: ワークスペース内のいずれかのアプリでのセッション数でユーザーをセグメント化します。
    tags:
      - Sessions
  - name: Session Count For App
    description: 特定の指定されたアプリでのセッション数でユーザーをセグメント化します。
    tags:
      - Sessions
  - name: X Sessions In Last Y Days
    description: 指定された暦日数（1〜30日）の間に、アプリでのセッション数（0〜50回）でユーザーをセグメント化します。<br> <a href="/docs/x-in-y-behavior/">X-in-Y動作の詳細はこちらをご覧ください。</a>
    tags:
      - Sessions
  - name: First Used App
    description: ユーザーがアプリを開いた最も早い記録時間でセグメント化します。<em>これは、Braze SDKが統合されたバージョンのアプリを使用した最初のセッションをキャプチャします。</em>（24時間期間）<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Sessions
  - name: First Used Specific App
    description: ワークスペース内のいずれかのアプリを開いた最も早い記録時間でユーザーをセグメント化します。（24時間期間）<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Sessions
  - name: Last Used App
    description: ユーザーがアプリを開いた最新の時間でセグメント化します。（24時間期間）<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Sessions
  - name: Last Used Specific App
    description: 特定の指定されたアプリを開いた最新の時間でユーザーをセグメント化します。（24時間期間）<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Sessions
  - name: Median Session Duration
    description: アプリでのセッション時間の中央値でユーザーをセグメント化します。
    tags:
      - Sessions
  - name: Received Message from Campaign
    description: 特定のCampaignを受信したかどうかでユーザーをセグメント化します。<br><br>Content Cards、バナー、アプリ内メッセージの場合、これはユーザーがインプレッションを記録した時点であり、カードやアプリ内メッセージが送信された時点ではありません。<br><br>プッシュとWebhookの場合、これはメッセージがユーザーに送信された時点です。<br><br>WhatsAppの場合、これは最後のメッセージAPIリクエストがWhatsAppに送信された時点であり、メッセージがユーザーのデバイスに配信された時点ではありません。<br><br>メールの場合、ターゲットのユーザープロファイルは、メールリクエストがメールサービスプロバイダーに送信された時点でこのフィルターに一致します（実際に配信されたかどうかに関係なく）。<br><br>SMSおよびRCSの場合、これは最後のメッセージがSMSまたはRCSプロバイダーに配信された時点です。メッセージがユーザーのデバイスに配信されたことを保証するものではありません。<br><br>メッセージが配信、開封、またはクリックされると、Brazeは同じチャネル識別子（メールアドレスや電話番号など）を共有するすべてのプロファイルのデータを更新するため、メッセージを受信した人と識別子を共有するユーザーは、そのプロファイルにCampaignが直接送信されていなくても、このフィルターに一致する場合があります。
    tags:
      - Retargeting
  - name: Received Campaign Variant
    description: 多変量Campaignのどのバリアントを受信したかでユーザーをセグメント化します。<br><br>このフィルターは多変量および多変量クイックプッシュCampaignsに適用されます。API Campaigns、標準マルチチャネルCampaigns、およびフィーチャーフラグ実験Campaignsは、Campaignセレクターに表示されません。WebhookのみのCampaignsもCampaignセレクターに表示されません。<br><br>Content Cards、バナー、アプリ内メッセージの場合、これはユーザーがインプレッションを記録した時点であり、カードやアプリ内メッセージが送信された時点ではありません。<br><br>プッシュとWebhookの場合、これはメッセージがユーザーに送信された時点です。<br><br>WhatsAppの場合、これは最後のメッセージAPIリクエストがWhatsAppに送信された時点であり、メッセージがユーザーのデバイスに配信された時点ではありません。<br><br>メールの場合、ターゲットのユーザープロファイルは、メールリクエストがメールサービスプロバイダーに送信された時点でこのフィルターに一致します（実際に配信されたかどうかに関係なく）。<br><br>SMSおよびRCSの場合、これは最後のメッセージがSMSまたはRCSプロバイダーに配信された時点です。メッセージがユーザーのデバイスに配信されたことを保証するものではありません。<br><br>メッセージが配信、開封、またはクリックされると、Brazeは同じチャネル識別子（メールアドレスや電話番号など）を共有するすべてのプロファイルのデータを更新するため、メッセージを受信した人と識別子を共有するユーザーは、そのプロファイルにCampaignが直接送信されていなくても、このフィルターに一致する場合があります。
    tags:
      - Retargeting
  - name: Received Message from Canvas Step
    description: 特定のCanvasコンポーネントを受信したかどうかでユーザーをセグメント化します。<br><br>Content Cardsとアプリ内メッセージの場合、これはユーザーがインプレッションを記録した時点であり、カードやアプリ内メッセージが送信された時点ではありません。<br><br>プッシュとWebhookの場合、これはメッセージがユーザーに送信された時点です。<br><br>WhatsAppの場合、これは最後のメッセージAPIリクエストがWhatsAppに送信された時点であり、メッセージがユーザーのデバイスに配信された時点ではありません。<br><br>メールの場合、ターゲットのユーザープロファイルは、メールリクエストがメールサービスプロバイダーに送信された時点でこのフィルターに一致します（実際に配信されたかどうかに関係なく）。<br><br>SMSおよびRCSの場合、これは最後のメッセージがSMSまたはRCSプロバイダーに配信された時点です。メッセージがユーザーのデバイスに配信されたことを保証するものではありません。<br><br>メッセージが配信、開封、またはクリックされると、Brazeは同じチャネル識別子（メールアドレスや電話番号など）を共有するすべてのプロファイルのデータを更新するため、メッセージを受信した人と識別子を共有するユーザーは、そのプロファイルにCampaignが直接送信されていなくても、このフィルターに一致する場合があります。
    tags:
      - Retargeting
  - name: Last Received Message from Specific Canvas Step
    description: 特定のCanvasコンポーネントを受信した時期でユーザーをセグメント化します。<br><br>配信、開封、またはクリックが発生すると、同じチャネル識別子（メールアドレスや電話番号など）を共有するすべてのプロファイルのデータが更新されるため、メッセージを受信した人と識別子を共有するユーザーは、明示的にメッセージが送信されていなくても、このフィルターに一致する場合があります。重複からユーザープロファイルを分離するには、「Entered Canvas Variation」を使用してください。<br><br>このフィルターは、ユーザーが他のCanvasコンポーネントを受信した時期は考慮しません。
    tags:
      - Retargeting
  - name: Last Received Message from Specific Campaign
    description: 特定のCampaignを受信したかどうかでユーザーをセグメント化します。<br><br>配信、開封、またはクリックが発生すると、同じチャネル識別子（メールアドレスや電話番号など）を共有するすべてのプロファイルのデータが更新されるため、メッセージを受信した人と識別子を共有するユーザーは、明示的にメッセージが送信されていなくても、このフィルターに一致する場合があります。<br><br>このフィルターは、ユーザーが他のCampaignsを受信した時期は考慮しません。
    tags:
      - Retargeting
  - name: Received Message from Campaign or Canvas with Tag
    description: 特定のタグを持つ特定のCampaignまたはCanvasを受信したかどうかでユーザーをセグメント化します。<br><br>Content Cards、バナー（Campaignsのみ）、アプリ内メッセージの場合、これはユーザーがインプレッションを記録した時点であり、カードやアプリ内メッセージが送信された時点ではありません。<br><br>プッシュとWebhookの場合、これはメッセージがユーザーに送信された時点です。<br><br>WhatsAppの場合、これは最後のメッセージAPIリクエストがWhatsAppに送信された時点であり、メッセージがユーザーのデバイスに配信された時点ではありません。<br><br>メールの場合、ターゲットのユーザープロファイルは、メールリクエストがメールサービスプロバイダーに送信された時点でこのフィルターに一致します（実際に配信されたかどうかに関係なく）。<br><br>SMSおよびRCSの場合、これは最後のメッセージがSMSまたはRCSプロバイダーに配信された時点です。メッセージがユーザーのデバイスに配信されたことを保証するものではありません。<br><br>メッセージが配信、開封、またはクリックされると、Brazeは同じチャネル識別子（メールアドレスや電話番号など）を共有するすべてのプロファイルのデータを更新するため、メッセージを受信した人と識別子を共有するユーザーは、そのプロファイルにCampaignが直接送信されていなくても、このフィルターに一致する場合があります。
    tags:
      - Retargeting
  - name: Last Received Message from Campaign or Canvas With Tag
    description: 特定のタグを持つ特定のCampaignまたはCanvasを受信した時期でユーザーをセグメント化します。このフィルターは、ユーザーが他のCampaignsやCanvasesを受信した時期は考慮しません。（24時間期間）
    tags:
      - Retargeting
  - name: Has Never Received a Message from Campaign or Canvas Step
    description: いずれかのCampaignまたはCanvasコンポーネントを受信したかどうかでユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: Last Received Email
    description: メールメッセージを最後に受信した時間でユーザーをセグメント化します。（24時間期間）<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Retargeting
  - name: Last Received Push
    description: プッシュ通知を最後に受信した時間でユーザーをセグメント化します。（24時間期間）<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Retargeting
  - name: Last In App Message Impression
    description: アプリ内メッセージを最後に閲覧した時間でユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: Last Received SMS
    description: 最後のSMS、MMS、またはRCSメッセージがSMSまたはRCSプロバイダーに配信された時間でユーザーをセグメント化します。メッセージがユーザーのデバイスに配信されたことを保証するものではありません。（24時間期間）<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Retargeting
  - name: Last Received Webhook
    description: Brazeがそのユーザーに対してWebhookを最後に送信した時間でユーザーをセグメント化します。（24時間期間）<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Retargeting
  - name: Last Received WhatsApp
    description: WhatsAppメッセージを最後に受信した時間でユーザーをセグメント化します。これは最後のメッセージAPIリクエストがWhatsAppに送信された時点であり、メッセージがユーザーのデバイスに配信された時点ではありません。（24時間期間）<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Retargeting
  - name: Live Activities Push to Start Registered for App
    description: 特定のアプリでiOSプッシュ通知を通じてLive Activityを開始するために登録されているかどうかでユーザーをセグメント化します。
    tags:
      - Devices
  - name: Clicked/Opened Campaign
    description: 特定のCampaignとのインタラクションでフィルタリングします。メールメッセージの場合、開封イベントにはマシンオープンと非マシンオープンの両方が含まれます。<br><br>メールの場合、「メールを開封（マシンオープン）」と「メールを開封（その他のオープン）」でフィルタリングするオプションも含まれます。配信停止リンクやユーザー設定センターのクリックはこのフィルターにカウントされません。複数のユーザーが同じメールアドレスを共有している場合:<br>- メールが開封またはクリックされると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージ送信後、開封またはクリック前にメールアドレスを変更した場合、開封またはクリックは元のユーザーではなく、そのメールアドレスを持つ残りのすべてのユーザーに適用されます。<br><br>SMSおよびRCSの場合、インタラクションは次のように定義されます:<br>- ユーザーが特定のキーワードカテゴリーに一致する返信SMSまたはRCSを最後に送信した場合。これは、この電話番号を持つすべてのユーザーが受信した最新のCampaignに帰属します。Campaignは過去4時間以内に受信されている必要があります。<br>- ユーザーが特定のCampaignからの、ユーザークリックトラッキングが有効になっているSMSまたはRCSメッセージ内の短縮リンクを最後に選択した場合。
    tags:
      - Retargeting
  - name: Clicked/Opened Campaign or Canvas With Tag
    description: 特定のタグを持つ特定のCampaignとのインタラクションでフィルタリングします。メールメッセージの場合、開封イベントにはマシンオープンと非マシンオープンの両方が含まれます。<br><br>メールの場合、「メールを開封（マシンオープン）」と「メールを開封（その他のオープン）」でフィルタリングするオプションが含まれます。複数のユーザーが同じメールアドレスを共有している場合:<br>- メールが開封またはクリックされると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージ送信後、開封またはクリック前にメールアドレスを変更した場合、開封またはクリックは元のユーザーではなく、そのメールアドレスを持つ残りのすべてのユーザーに適用されます。<br><br>SMSおよびRCSの場合、インタラクションは次のように定義されます:<br>- ユーザーが特定のキーワードカテゴリーに一致する返信SMSまたはRCSを最後に送信した場合。これは、この電話番号を持つすべてのユーザーが受信した最新のCampaignに帰属します。Campaignは過去4時間以内に受信されている必要があります。<br>- ユーザーが特定のタグ付きCampaignまたはキャンバスステップからの、ユーザークリックトラッキングが有効になっているSMSまたはRCSメッセージ内の短縮リンクを最後に選択した場合。
    tags:
      - Retargeting
  - name: Clicked/Opened Step
    description: 特定のCanvasコンポーネントとのインタラクションでフィルタリングします。メールメッセージの場合、開封イベントにはマシンオープンと非マシンオープンの両方が含まれます。<br><br>メールの場合、「メールを開封（マシンオープン）」と「メールを開封（その他のオープン）」でフィルタリングするオプションが含まれます。<br><br>SMSおよびRCSの場合、インタラクションは次のように定義されます:<br>- ユーザーが特定のキーワードカテゴリーに一致する返信SMSまたはRCSを最後に送信した場合。これは、この電話番号を持つすべてのユーザーが受信した最新のCampaignに帰属します。Campaignは過去4時間以内に受信されている必要があります。<br>- ユーザーが特定のキャンバスステップからの、ユーザークリックトラッキングが有効になっているSMSまたはRCSメッセージ内の短縮リンクを最後に選択した場合。
    tags:
      - Retargeting
  - name: Clicked Alias in Campaign
    description: 特定のCampaign内の特定のエイリアスをクリックしたかどうかでユーザーをフィルタリングします。これはメールメッセージにのみ適用されます。<br><br>複数のユーザーが同じメールアドレスを共有している場合:<br>- メールが開封またはクリックされると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージ送信後、開封またはクリック前にメールアドレスを変更した場合、開封またはクリックは元のユーザーではなく、そのメールアドレスを持つ残りのすべてのユーザーに適用されます。
    tags:
      - Retargeting
  - name: Clicked Alias in Canvas Step
    description: 特定のCanvas内の特定のエイリアスをクリックしたかどうかでユーザーをフィルタリングします。これはメールメッセージにのみ適用されます。<br><br>複数のユーザーが同じメールアドレスを共有している場合:<br>- メールが開封またはクリックされると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージ送信後、開封またはクリック前にメールアドレスを変更した場合、開封またはクリックは元のユーザーではなく、そのメールアドレスを持つ残りのすべてのユーザーに適用されます。
    tags:
      - Retargeting
  - name: Clicked Alias in Any Campaign or Canvas Step
    description: いずれかのCampaignまたはCanvas内の特定のエイリアスをクリックしたかどうかでユーザーをフィルタリングします。これはメールメッセージにのみ適用されます。<br><br>複数のユーザーが同じメールアドレスを共有している場合:<br>- メールが開封またはクリックされると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージ送信後、開封またはクリック前にメールアドレスを変更した場合、開封またはクリックは元のユーザーではなく、そのメールアドレスを持つ残りのすべてのユーザーに適用されます。
    tags:
      - Retargeting
  - name: Hard Bounced
    description: メールアドレスがハードバウンスしたかどうか（メールアドレスが無効など）でユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: Soft Bounced
    description: Y日間にX回ソフトバウンスしたかどうかでユーザーをセグメント化します。Segmentフィルターは過去30日間のみ遡ることができますが、セグメントエクステンションを使用するとさらに遡ることができます。<br><br>このフィルターは、Currentsのソフトバウンスイベントとは異なる動作をします。ソフトバウンスSegmentフィルターは、72時間のリトライ期間中に配信が成功しなかった場合にソフトバウンスをカウントします。Currentsでは、失敗したリトライごとにソフトバウンスイベントとして送信されます。
    tags:
      - Retargeting
  - name: Has Marked You As Spam
    description: メッセージをスパムとしてマークしたかどうかでユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: Invalid Phone Number
    description: 電話番号が無効かどうかでユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: Last Sent Specific SMS Inbound Keyword Category
    description: 特定のサブスクリプショングループ内の特定のキーワードカテゴリーでSMS、MMS、またはRCSを最後に送信した時期でユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: Converted From Campaign
    description: 特定のCampaignでコンバージョンしたかどうかでユーザーをセグメント化します。このフィルターにはコントロールグループのユーザーは含まれません。
    tags:
      - Retargeting
  - name: Converted From Canvas
    description: 特定のCanvasでコンバージョンしたかどうかでユーザーをセグメント化します。このフィルターにはコントロールグループのユーザーは含まれません。
    tags:
      - Retargeting
  - name: In Campaign Control Group
    description: 特定の多変量Campaignのコントロールグループに所属していたかどうかでユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: In Canvas Control Group
    description: 特定のCanvasのコントロールグループに所属していたかどうかでユーザーをセグメント化します。このフィルターはCanvasに入ったユーザーのみを評価するため、入ったことのないユーザーは結果から完全に除外されます。<br><br>例えば、Canvasのコントロールグループに所属していないユーザーをフィルタリングすると、Canvasに入り、非コントロールバリアントに割り当てられたユーザーのみが返されます。Canvasに入ったことのないユーザーは含まれません。Canvasへの参加に関係なくすべてのユーザーを含めるには、代わりに<code>Entered Canvas Variation</code>フィルターを使用してください。
    tags:
      - Retargeting
  - name: Last Enrolled in Any Control Group
    description: Campaign内でコントロールグループに最後に入った時間でユーザーをセグメント化します。<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Retargeting
  - name: Entered Canvas Variation
    description: 特定のCanvasのバリエーションパスに入ったかどうかでユーザーをセグメント化します。このフィルターはすべてのユーザーを評価します。<br><br>例えば、Canvasバリエーションのコントロールグループに入っていないユーザーをフィルタリングすると、Canvasに入ったかどうかに関係なく、コントロールグループに所属していないすべてのユーザーが返されます。
    tags:
      - Retargeting
  - name: Last Received Any Message
    description: 最後に受信したメッセージを判定してユーザーをセグメント化します。（24時間期間）<br><br>Content Cards、バナー、アプリ内メッセージの場合、これはユーザーが最後にインプレッションを記録した時点であり、カードやアプリ内メッセージが最後に送信された時点ではありません。<br><br>プッシュとWebhookの場合、これはいずれかのメッセージがユーザーに送信された時点です。<br><br>WhatsAppの場合、これは最後のメッセージAPIリクエストがWhatsAppに送信された時点であり、メッセージがユーザーのデバイスに配信された時点ではありません。<br><br>メールの場合、ターゲットのユーザープロファイルは、メールリクエストがメールサービスプロバイダーに送信された時点でこのフィルターに一致します（実際に配信されたかどうかに関係なく）。<br><br>SMSおよびRCSの場合、これは最後のメッセージがSMSまたはRCSプロバイダーに配信された時点です。メッセージがユーザーのデバイスに配信されたことを保証するものではありません。<br><br>メッセージが配信、開封、またはクリックされると、Brazeは同じチャネル識別子（メールアドレスや電話番号など）を共有するすべてのプロファイルのデータを更新するため、メッセージを受信した人と識別子を共有するユーザーは、そのプロファイルにCampaignが直接送信されていなくても、このフィルターに一致する場合があります。<br><br>例:<br>最終メッセージ受信が1日未満前 = 24時間未満前<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Retargeting
  - name: Last Engaged With Message
    description: メッセージングチャネル（バナー、Content Cards、メール、アプリ内、SMS、RCS、プッシュ、WhatsApp）のいずれかを最後にクリックまたは開封した時間でユーザーをセグメント化します。<br><br>Content Cards、バナー、アプリ内メッセージの場合、これはユーザーがインプレッションを記録した時点であり、カードやアプリ内メッセージが送信された時点ではありません。<br><br>プッシュとWebhookの場合、これはメッセージがユーザーに送信された時点です。<br><br>WhatsAppの場合、これは最後のメッセージAPIリクエストがWhatsAppに送信された時点であり、メッセージがユーザーのデバイスに配信された時点ではありません。<br><br>メールメッセージの場合、開封イベントにはマシンオープンと非マシンオープンの両方が含まれます。（24時間期間）<br><br>メールの場合、ターゲットのユーザープロファイルは、メールリクエストがメールサービスプロバイダーに送信された時点でこのフィルターに一致します（実際に配信されたかどうかに関係なく）。「メールを開封（マシンオープン）」と「メールを開封（その他のオープン）」でフィルタリングするオプションも含まれます。<br><br>SMSおよびRCSの場合、これはユーザーがユーザークリックトラッキングが有効になっているメッセージ内の短縮リンクを最後に選択した時点です。<br><br>メッセージが配信、開封、またはクリックされると、Brazeは同じチャネル識別子（メールアドレスや電話番号など）を共有するすべてのプロファイルのデータを更新するため、メッセージを受信した人と識別子を共有するユーザーは、そのプロファイルにCampaignが直接送信されていなくても、このフィルターに一致する場合があります。<br><br>タイムゾーン:<br>会社のタイムゾーン
    tags:
      - Retargeting
  - name: Clicked card
    description: 特定のContent Cardsをクリックしたかどうかでユーザーをセグメント化します。このフィルターは、「Clicked/Opened Campaign」、「Clicked/Opened Campaign or Canvas With Tag」、「Clicked/Opened Step」のサブフィルターとして利用できます。
    tags:
      - Retargeting
  - name: Feature Flags
    description: 特定の<a href="/docs/developer_guide/feature_flags/">フィーチャーフラグ</a> が現在有効になっているユーザーのSegmentです。
    tags:
      - Retargeting
  - name: Subscription Group
    description: メール、SMS、MMS、RCS、またはWhatsAppのサブスクリプショングループでユーザーをセグメント化します。アーカイブされたグループは表示されず、使用できません。
    tags:
      - Channel subscription behavior
  - name: Email Available
    description: 有効なメールアドレスを持ち、メールに購読中またはオプトインしているかどうかでユーザーをセグメント化します。このフィルターは3つの条件をチェックします&#58; ユーザーがメールの配信停止をしているか、Brazeがハードバウンスを受信したか、メールがスパムとしてマークされたか。これらの条件のいずれかが満たされた場合、またはユーザーにメールが存在しない場合、そのユーザーは含まれません。<br><br>メール利用可能が<code>false</code>のユーザーは、Campaignオーディエンスから除外され、メールを受信しません。送信設定がすべてのユーザー（配信停止済みユーザーを含む）に送信するように構成されている場合でも同様です。<br><br>オプトインステータスが重要なメールの場合、<a href="/docs/user_guide/audience/segments/segmentation_filters#email-address">メールアドレス</a> の代わりにメール利用可能を使用してください。追加の条件により、メールを受信する資格のあるユーザーをターゲットにできます。
    tags:
      - Channel subscription behavior
  - name: Email Opt In Date
    description: メールにオプトインした日付でユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: Email Subscription Status
    description: メールのサブスクリプションステータスでユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: Email Unsubscribed Date
    description: 今後のメールの配信停止をした日付でユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: Foreground Push Enabled
    description: 仮承認プッシュ認可を持つか、フォアグラウンドプッシュが有効なユーザーをセグメント化します。具体的には、このカウントには以下が含まれます:<br>1. プッシュの仮承認を受けたiOSユーザー。<br>2. いずれかのアプリでフォアグラウンドプッシュが有効で、プッシュサブスクリプションステータスが配信停止でないユーザー。これらのユーザーについては、フォアグラウンドプッシュのみがカウントされます。<br><br>フォアグラウンドプッシュ有効には、配信停止したユーザーは含まれません。<br><br>このフィルターでセグメント化した後、下部パネルの<em>到達可能なユーザー</em>で、Android、iOS、Webのそれぞれの内訳を確認できます。
    tags:
      - Channel subscription behavior
  - name: Foreground Push Enabled for App
    description: デバイス上のアプリでプッシュが有効かどうかでセグメント化します。アプリのフォアグラウンドプッシュが有効なユーザーです。プッシュサブスクリプションステータスは考慮されません。このカウントには、フォアグラウンドおよびバックグラウンドプッシュトークンの仮承認を受けたユーザーが含まれます。
    tags:
      - Channel subscription behavior
  - name: Background or Foreground Push Enabled
    description: プッシュトークンを持ち、配信停止していないかどうかでセグメント化します。いずれかのアプリでバックグラウンドまたはフォアグラウンドプッシュが有効なユーザーです。
    tags:
      - Channel subscription behavior
  - name: Push Opt In Date
    description: プッシュにオプトインした日付でユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: Push Subscription Status
    description: プッシュの<a href="/docs/user_guide/channels/push/push_setup/push_subscription_states#push-subscription-state">サブスクリプションステータス</a> でユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: Push Unsubscribed Date
    description: 今後のプッシュ通知の配信停止をした日付でユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: Purchased Product
    description: アプリで購入した製品でユーザーをセグメント化します。
    tags:
      - Purchase behavior
  - name: Total Number of Purchases
    description: アプリでの購入回数でユーザーをセグメント化します。
    tags:
      - Purchase behavior
  - name: X Product Purchased In Y Days
    description: 特定の製品が購入された回数でユーザーをフィルタリングします。
    tags:
      - Purchase behavior
  - name: X Purchases in Last Y Days
    description: 指定された暦日数（1〜30日）の間に購入した回数（0〜50回）でユーザーをセグメント化します。<br> <a href="/docs/x-in-y-behavior/">X-in-Y動作の詳細はこちらをご覧ください。</a>
    tags:
      - Purchase behavior
  - name: X Purchase Property In Y Days
    description: 指定された暦日数（1〜30日）の間に、特定の購入プロパティに関連して購入が行われた回数でユーザーをセグメント化します。<br> <a href="/docs/x-in-y-behavior/">X-in-Y動作の詳細はこちらをご覧ください。</a>
    tags:
      - Purchase behavior
  - name: First Made Purchase
    description: ユーザーがアプリで購入を行った最も早い時間でセグメント化します。
    tags:
      - Purchase behavior
  - name: First Purchase For App
    description: ユーザーがアプリから購入を行った最も早い時間でセグメント化します。
    tags:
      - Purchase behavior
  - name: Last Made Purchase
    description: 最後に購入を行った時間でユーザーをフィルタリングします。
    tags:
      - Purchase behavior
  - name: Last Purchased Product
    description: 特定の製品を最後に購入した時期でユーザーをフィルタリングします。
    tags:
      - Purchase behavior
  - name: Money Spent
    description: アプリで支出した金額でユーザーをセグメント化します。
    tags:
      - Purchase behavior
  - name: X Money Spent in Y Days
    description: 指定された暦日数（1〜30日）の間にアプリで支出した金額でユーザーをセグメント化します。この金額には直近50回の購入の合計のみが含まれます。<br> <a href="/docs/x-in-y-behavior/">X-in-Y動作の詳細はこちらをご覧ください。</a>
    tags:
      - Purchase behavior
  - name: Last order placed (last 730 days)
    description: 最後に注文を行った時期でユーザーをセグメント化します。これは注文完了の<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> に基づいています（eコマースイベントを追跡していないワークスペースにはこのフィルターのデータがありません）。ユーザーはこのフィルターに対して1日1回評価され、最大ルックバックウィンドウは過去2年間です。<br><br>このフィルターはベータ版です。このフィルターの使用に興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
    tags:
      - eCommerce
  - name: Total orders count (last 730 days)
    description: 過去2年間のユーザーの注文合計数でセグメント化します。注文完了の<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> に基づいています（eコマースイベントを追跡していないワークスペースにはこのフィルターのデータがありません）。このカウントにはキャンセルされた注文は含まれません。キャンセルされた注文は注文キャンセルの<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> を使用して追跡する必要があります。ユーザーはこのフィルターに対して1日1回評価されます。<br><br>このフィルターはベータ版です。このフィルターの使用に興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
    tags:
      - eCommerce
  - name: Total orders count
    description: ユーザーの全期間にわたる注文合計数でセグメント化します。注文完了の<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> に基づいています（eコマースイベントを追跡していないワークスペースにはこのフィルターのデータがありません）。このカウントにはキャンセルされた注文は含まれません。キャンセルされた注文は注文キャンセルの<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> を使用して追跡する必要があります。ユーザーはこのフィルターに対してリアルタイムで評価されます。<br><br>このフィルターはベータ版です。このフィルターの使用に興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
    tags:
      - eCommerce
  - name: Total canceled orders count (last 730 days)
    description: 過去2年間にユーザーがキャンセルした注文の合計数でセグメント化します。注文完了の<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> に基づいています（eコマースイベントを追跡していないワークスペースにはこのフィルターのデータがありません）。ユーザーはこのフィルターに対して1日1回評価されます。<br><br>このフィルターはベータ版です。このフィルターの使用に興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
    tags:
      - eCommerce
  - name: Customer lifetime value (last 730 days)
    description: ブランドとの購入履歴を通じてユーザーが生み出すと予想される総収益でセグメント化します。計算は過去730日間を考慮し、平均注文額（AOV）に注文合計数を掛け、ユーザーのアクティブな購入期間（最初の注文から最新の注文までの期間）を考慮します。このフィルターは<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> で追跡されたデータを使用します（eコマースイベントを追跡していないワークスペースにはこのフィルターのデータがありません）。ユーザーはこのフィルターに対して1日1回評価されます。<br><br>このフィルターはベータ版です。このフィルターの使用に興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
    tags:
      - eCommerce
  - name: Total refund value (last 730 days)
    description: 過去2年間にユーザーに付与された返金額でセグメント化します。注文返金の<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> に基づいています（eコマースイベントを追跡していないワークスペースにはこのフィルターのデータがありません）。ユーザーはこのフィルターに対して1日1回評価されます。<br><br>このフィルターはベータ版です。このフィルターの使用に興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
    tags:
      - eCommerce
  - name: Total refund value
    description: ユーザーの全期間にわたって付与された返金の合計額でセグメント化します。注文返金の<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> に基づいています（eコマースイベントを追跡していないワークスペースにはこのフィルターのデータがありません）。ユーザーはこのフィルターに対してリアルタイムで評価されます。<br><br>このフィルターはベータ版です。このフィルターの使用に興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
    tags:
      - eCommerce
  - name: Total revenue (last 730 days)
    description: 過去2年間のユーザーの注文から生成された合計収益でセグメント化します。注文返金の<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> に関連する収益を、注文完了のeコマースイベントに関連する収益から差し引いて計算されます（eコマースイベントを追跡していないワークスペースにはこのフィルターのデータがありません）。ユーザーはこのフィルターに対して1日1回評価されます。<br><br>このフィルターはベータ版です。このフィルターの使用に興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
    tags:
      - eCommerce
  - name: Total revenue
    description: ユーザーの全期間にわたる注文から生成された合計収益でセグメント化します。注文返金の<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> に関連する収益を、注文完了のeコマースイベントに関連する収益から差し引いて計算されます（eコマースイベントを追跡していないワークスペースにはこのフィルターのデータがありません）。ユーザーはこのフィルターに対してリアルタイムで評価されます。<br><br>このフィルターはベータ版です。このフィルターの使用に興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
    tags:
      - eCommerce
  - name: Average order value (last 730 days)
    description: 過去2年間のユーザーの注文の平均（平均値）額でセグメント化します。注文完了の<a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eコマース推奨イベント</a> に基づいています（eコマースイベントを追跡していないワークスペースにはこのフィルターのデータがありません）。ユーザーはこのフィルターに対して1日1回評価されます。<br><br>このフィルターはベータ版です。このフィルターの使用に興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
    tags:
      - eCommerce
  - name: Country
    description: 最後に示された国の位置情報でユーザーをセグメント化します。
    tags:
      - Demographic attributes
  - name: City
    description: 最後に示された市区町村の位置情報でユーザーをセグメント化します。
    tags:
      - Demographic attributes
  - name: Language
    description: 優先言語でユーザーをセグメント化します。
    tags:
      - Demographic attributes
  - name: Age
    description: アプリ内で示された年齢でユーザーをセグメント化します。
    tags:
      - Demographic attributes
  - name: Birthday
    description: アプリ内で示された誕生日でユーザーをセグメント化します。<br>2月29日が誕生日のユーザーは、3月1日を含むSegmentsに含まれます。<br><br>12月または1月の誕生日をターゲットにするには、ターゲットとする年の12か月の範囲内でのみフィルターロジックを挿入してください。つまり、前年の12月を遡ったり、翌年の1月を先取りしたりするロジックを挿入しないでください。例えば、12月の誕生日をターゲットにするには、「12月31日に」、「12月31日より前」、または「11月30日より後」でフィルタリングできます。
    tags:
      - Demographic attributes
  - name: Gender
    description: アプリ内で示された性別でユーザーをセグメント化します。
    tags:
      - Demographic attributes
  - name: Unformatted Phone Number
    description: 未フォーマットの電話番号でユーザーをセグメント化します。かっこ、ダッシュ、その他の記号は含まれません。
    tags:
      - Demographic attributes
  - name: First Name
    description: アプリ内で示された名でユーザーをセグメント化します。
    tags:
      - Demographic attributes
  - name: Last Name
    description: アプリ内で示された姓でユーザーをセグメント化します。
    tags:
      - Demographic attributes
  - name: Has App
    description: ユーザーがアプリをインストールしたことがあるかどうかでセグメント化します。これには、現在アプリがインストールされているユーザーと、過去にアンインストールしたユーザーが含まれます。通常、このフィルターに含まれるには、ユーザーがアプリを開く（セッションを開始する）必要があります。ただし、ユーザーがBrazeにインポートされ、手動でアプリに関連付けられた場合など、いくつかの例外があります。
    tags:
      - App
  - name: Most Recent App Version Name
    description: ユーザーのアプリの最新バージョン名でセグメント化します。<br><br>「未満」または「以下」を使用する場合、メインアプリバージョンが存在しない場合、このフィルターは<code>true</code>を返します。これは、ユーザーがそのアプリバージョンよりも古いためです。つまり、ユーザーの最後のメインアプリバージョンが存在しない場合、自動的にフィルターに一致します。
    tags:
      - App
  - name: Most Recent App Version Number
    description: ユーザーのアプリの最新バージョン番号でセグメント化します。かっこ内のバージョン番号がフィルタリングに使用され、その前の番号は参照用です。例えば、「3.7.0(134.0.0.0)」の場合、「134.0.0.0」がフィルタリングされるバージョン番号です。<br><br>「未満」または「以下」を使用する場合、メインアプリバージョンが存在しない場合、このフィルターは<code>true</code>を返します。これは、ユーザーがそのアプリバージョンよりも古いためです。つまり、ユーザーの最後のメインアプリバージョンが存在しない場合、自動的にフィルターに一致します。<br><br>現在のアプリバージョンが反映されるまでに時間がかかる場合があります。ユーザープロファイルのアプリバージョンは、SDKによって情報がキャプチャされた時点で更新されますが、これはユーザーがアプリを開いた時に依存します。ユーザーがアプリを開かない場合、現在のバージョンは更新されません。これらのフィルターは遡及的にも適用されません。現在および将来のバージョンに対して「より大きい」または「等しい」を使用することをお勧めしますが、過去のバージョンフィルターを使用すると予期しない動作が発生する可能性があります。
    tags:
      - App
  - name: Uninstalled
    description: アプリをアンインストールし、再インストールしていないかどうかでユーザーをセグメント化します。
    tags:
      - Uninstall
  - name: Device Carrier
    description: デバイスキャリアでユーザーをセグメント化します。
    tags:
      - Devices
  - name: Device Count
    description: アプリを使用したデバイスの数でユーザーをセグメント化します。
    tags:
      - Devices
  - name: Device Model
    description: 携帯電話のモデルバージョンでユーザーをセグメント化します。
    tags:
      - Devices
  - name: Device OS
    description: 指定されたオペレーティングシステムを持つ1つ以上のデバイスを持つユーザーをセグメント化します。オペレーティングシステムの範囲でユーザーをセグメント化するには、<a href="/docs/user_guide/audience/segments/segmentation_filters#device-os-version-number">デバイスOSバージョン番号</a> フィルターを使用してください。
    tags:
      - Devices
  - name: Device OS Version Number
    description: 指定された範囲内のオペレーティングシステムバージョンを持つ1つ以上のデバイスを持つユーザーをセグメント化します。例えば、iOSオペレーティングシステムバージョンが26.0以上のユーザーをターゲットにできます。
    tags:
      - Devices
  - name: Most Recent Device Locale
    description: 最近使用されたデバイスの<a href="/docs/user_guide/messaging/messaging_fundamentals/localization">ロケール情報</a> でユーザーをセグメント化します。
    tags:
      - Devices
  - name: Most Recent Watch Model
    description: 最新のスマートウォッチモデルでユーザーをセグメント化します。
    tags:
      - Devices
  - name: Provisionally Authorized on iOS
    description: 特定のアプリでiOS 12の仮承認を受けたユーザーを検索できます。
    tags:
      - Devices
  - name: Web Browser
    description: Webサイトへのアクセスに使用するWebブラウザーでユーザーをセグメント化します。
    tags:
      - Devices
  - name: Device IDFA
    description: テスト用にIDFAでCampaignの受信者を指定できます。
    tags:
      - Advertising use cases
  - name: Device IDFV
    description: テスト用にIDFVでCampaignの受信者を指定できます。
    tags:
      - Advertising use cases
  - name: Device Google Ad ID
    description: Google広告IDでユーザーをセグメント化します。
    tags:
      - Advertising use cases
  - name: Device Roku Ad ID
    description: Roku広告IDでユーザーをセグメント化します。
    tags:
      - Advertising use cases
  - name: Device Windows Ad ID
    description: Windows広告IDでユーザーをセグメント化します。
    tags:
      - Advertising use cases
  - name: Ad Tracking Enabled
    description: ユーザーが広告トラッキングにオプトインしているかどうかに基づいてフィルタリングできます。広告トラッキングは、Appleがすべてのiデバイスに割り当てるIDFAまたは「広告主向け識別子」に関連しており、SDKで設定できます。この識別子により、広告主はユーザーを追跡し、ターゲット広告を配信できます。
    tags:
      - Advertising use cases
  - name: Most Recent Location
    description: アプリを使用した最後に記録された位置情報でユーザーをセグメント化します。
    tags:
      - Location
  - name: Location Available
    description: 位置情報を報告したかどうかでユーザーをセグメント化します。このフィルターを使用するには、アプリに<a href="/docs/search/?query=location%20tracking">位置情報の追跡が統合されている</a> 必要があります。
    tags:
      - Location
  - name: Amplitude Cohorts
    description: Amplitudeを使用しているクライアントは、Amplitudeでコホートを選択してインポートすることでSegmentsを補完できます。
    tags:
      - Cohort membership
  - name: Census Cohorts
    description: Censusを使用しているクライアントは、Censusでコホートを選択してインポートすることでSegmentsを補完できます。
    tags:
      - Cohort membership
  - name: Heap Cohorts
    description: Heapを使用しているクライアントは、Heapでコホートを選択してインポートすることでSegmentsを補完できます。
    tags:
      - Cohort membership
  - name: Hightouch Cohorts
    description: Hightouchを使用しているクライアントは、Hightouchでコホートを選択してインポートすることでSegmentsを補完できます。
    tags:
      - Cohort membership
  - name: Kubit Cohorts
    description: Kubitを使用しているクライアントは、Kubitでコホートを選択してインポートすることでSegmentsを補完できます。
    tags:
      - Cohort membership
  - name: Mixpanel Cohorts
    description: Mixpanelを使用しているクライアントは、Mixpanelでコホートを選択してインポートすることでSegmentsを補完できます。
    tags:
      - Cohort membership
  - name: Segment Cohorts
    description: Segmentを使用しているクライアントは、Segmentでコホートを選択してインポートすることでSegmentsを補完できます。
    tags:
      - Cohort membership
  - name: Tinyclues Cohorts
    description: Tinycluesを使用しているクライアントは、Tinycluesでコホートを選択してインポートすることでSegmentsを補完できます。
    tags:
      - Cohort membership
  - name: Install Attribution Ad
    description: インストールが帰属する広告でユーザーをセグメント化します。
    tags:
      - User Attributes
  - name: Install Attribution Adgroup
    description: インストールが帰属する広告グループでユーザーをセグメント化します。
    tags:
      - Install attribution
  - name: Install Attribution Campaign
    description: インストールが帰属する広告Campaignでユーザーをセグメント化します。
    tags:
      - Install attribution
  - name: Install Attribution Source
    description: インストールが帰属するソースでユーザーをセグメント化します。
    tags:
      - Install attribution
  - name: Churn Risk Category
    description: 特定の予測に基づく解約リスクカテゴリーでユーザーをセグメント化します。
    tags:
      - Intelligence and predictive
  - name: Churn Risk Score
    description: 特定の予測に基づく解約リスクスコアでユーザーをセグメント化します。
    tags:
      - Intelligence and predictive
  - name: Event Likelihood Category
    description: 特定の予測に基づくイベント実行の可能性カテゴリーでユーザーをセグメント化します。
    tags:
      - Intelligence and predictive
  - name: Event Likelihood Score
    description: 特定の予測に基づくイベント実行の可能性スコアでユーザーをセグメント化します。
    tags:
      - Intelligence and predictive
  - name: Intelligent Channel
    description: 過去3か月間で最もアクティブなチャネルでユーザーをセグメント化します。
    tags:
      - Intelligence and predictive
  - name: Message Open Likelihood
    description: 指定されたチャネルでメッセージを<a href="/docs/user_guide/brazeai/intelligence_suite/intelligent_channel#individual-channels">開封する可能性</a> に基づいて、0〜100のスケールでユーザーをフィルタリングします。チャネルの可能性を測定するのに十分なデータがないユーザーは、「is blank」を使用して選択できます。<br><br>メールの場合、マシンオープンは可能性の計算から除外されます。
    tags:
      - Intelligence and predictive
  - name: Number of Facebook Friends Using App
    description: 同じアプリを使用しているFacebook友達の数でユーザーをセグメント化します。
    tags:
      - Social activity
  - name: Connected Facebook
    description: アプリをFacebookに接続したかどうかでユーザーをセグメント化します。
    tags:
      - Social activity
  - name: Connected Twitter
    description: アプリをX（旧Twitter）に接続したかどうかでユーザーをセグメント化します。
    tags:
      - Social activity
  - name: Number of Twitter Followers
    description: X（旧Twitter）のフォロワー数でユーザーをセグメント化します。
    tags:
      - Social activity
  - name: Phone Number
    description: E.164形式の電話番号フィールドでユーザーをセグメント化します。<br><br>電話番号がBrazeに送信されると、BrazeはSMS、RCS、WhatsAppチャネルでの送信に使用される<a href="/docs/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#importing-phone-numbers">E.164形式</a> に変換しようとします。番号が正しくフォーマットされていない場合、変換プロセスが失敗し、ユーザープロファイルに未フォーマットの電話番号はあるが送信用電話番号がないという結果になります。このSegmentフィルターは、E.164形式の電話番号（利用可能な場合）でユーザーを返します。<br><br>ユースケース:<br>- SMS、RCS、またはWhatsAppメッセージを送信する際に、最も正確なターゲットオーディエンスサイズを把握するためにこのフィルターを使用します。<br>- このフィルターで正規表現（regex）を使用して、特定の国コードの電話番号でセグメント化します。<br>- E.164変換プロセスに失敗した電話番号でユーザーをセグメント化するためにこのフィルターを使用します。
    tags:
      - Other Filters
---