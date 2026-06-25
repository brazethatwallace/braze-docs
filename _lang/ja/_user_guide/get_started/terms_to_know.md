---
page_order: 10
nav_title: 知っておくべき用語
article_title: 知っておくべき Braze 用語

layout: glossary_page
glossary_top_header: "知っておくべき用語"
glossary_top_text: "これらの用語は、Brazeを通じて顧客やユーザーとのより良い関係を築く旅を始める際に役立ちます。オンボーディングを始める前に、ぜひお読みください。"
page_type: glossary
description: "この用語集では、Brazeオンボーディングプロセスを進める際に知っておくべき重要な用語について説明します。"

glossaries:
  - name: Active user
    display_name: "アクティブユーザー"
    description: "Campaignのターゲティングにおいて、Brazeは特定の期間の<a href=\"{{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/active_user_campaigns\">アクティブユーザー</a> を、その期間にセッションを持つすべてのユーザーとして定義します（API経由で更新されたユーザーもその期間にカウントされます）。<a href=\"{{site.baseurl}}/user_archival/#active-users\">ユーザーアーカイブ</a> やリーチ可能性の統計では、Brazeはプロファイルの更新、ユーザーへのメッセージ送信、メッセージとのインタラクションも含む、より広い定義を使用します。"
  - name: Alloys
    display_name: "Alloys"
    description: "Alloysは、Brazeの<a href=\"{{site.baseurl}}/partners/home/\">テクノロジーパートナー</a> です。"
  - name: Anonymous users
    display_name: "匿名ユーザー"
    description: "SDK経由でユーザープロファイルが認識されると、関連付けられた<a href=\"{{site.baseurl}}/api/basics/#user-ids\">BrazeユーザーID</a> で匿名ユーザープロファイルが作成されます。"
  - name: API campaigns
    display_name: "APIキャンペーン"
    description: "<a href=\"{{site.baseurl}}/api/api_campaigns/\">APIキャンペーン</a> は、Brazeダッシュボードを使用して<code>campaign_id</code>（およびバリエーションID）を生成し、コピー、オーディエンス、スケジュール、アセットは<a href=\"{{site.baseurl}}/api/endpoints/messaging/\">メッセージングAPI</a> を通じて提供します。これは、ダッシュボードで完全に設定されたCampaignをAPI経由でトリガーする<a href=\"{{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/\">APIトリガーCampaign</a> とは異なります。"
  - name: Application program interface (API)
    display_name: "アプリケーションプログラムインターフェイス（API）"
    description: "<a href=\"{{site.baseurl}}/api/basics/#api-overview\">Braze API</a> は、モバイルSDK経由ではなく、HTTP経由で直接ユーザーのアクションを記録できるWebサービスを提供します。これにより、例えば、アプリやWebサイト内では追跡されないユーザーデータをBrazeに渡すことができます。"
  - name: App instance
    display_name: "アプリインスタンス"
    description: アプリインスタンスとは、ワークスペースに集められたさまざまなサイトやアプリを指します。
  - name: Braze (the product)
    display_name: "Braze（製品）"
    description: ダッシュボードと呼ばれることもあるこの製品は、Brazeプラットフォームの中心となるすべてのデータとインタラクションを制御します。Brazeの顧客は、通知の管理、ターゲットを絞ったメッセージングCampaignの設定、分析の表示に使用します。開発者は、APIキーやプッシュ通知の認証情報など、アプリを統合するための設定を管理するために使用します。
  - name: Team
    display_name: "チーム"
    description: "Brazeの管理者は、ダッシュボードユーザーのサブセットを、ユーザーの役割と権限が異なる<a href=\"{{site.baseurl}}/user_guide/administer/global/user_management/teams\">チーム</a> に分けることができます。これにより、Braze管理者はグループメンバーシップによって特定の機能へのアクセスを制限できます。"
  - name: Campaign
    display_name: "Campaign"
    description: "Campaignは、顧客にパーソナライズされたレスポンスを提供するためのカスタマイズ可能なメッセージング手法です。さまざまなメッセージングチャネルを使って<a href=\"{{site.baseurl}}/user_guide/messaging/campaigns\">Campaignを構築</a> し、独自のメッセージを送ることができます。"
  - name: Canvas
    display_name: "Canvas"
    description: "<a href=\"{{site.baseurl}}/user_guide/messaging/canvas\">Canvas</a> は、マーケターが複数のメッセージとステップからなるCampaignを設定し、まとまりのあるジャーニーを形成できる単一の統一インターフェイスです。Canvasを使用すると、包括的な分析を使用してこれらのエクスペリエンスを比較し、最適化することで、完全なユーザーエクスペリエンスを提供できます。"
  - name: Connected Content
    display_name: "コネクテッドコンテンツ"
    description: "<a href=\"{{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content\">コネクテッドコンテンツ</a> は、カスタマーエンゲージメントとコンバージョンを強化するため、マーケティングパーソナライゼーションを拡大します。ユーザーに送信するメッセージに、APIを使ってアクセスできるあらゆる情報を直接挿入できます。コネクテッドコンテンツでは、Webサーバーやパブリックにアクセス可能なAPIから直接コンテンツを取り込むことができます。"
  - name: Content Cards
    display_name: "Content Cards"
    description: "<a href=\"{{site.baseurl}}/user_guide/channels/content_cards\">Content Cards</a> によって、顧客のエクスペリエンスを中断することなく、顧客が愛用するアプリ内で、高度にターゲットを絞ったリッチコンテンツのダイナミックなストリームを送信できます。Content Cardsは、iOS、Android、およびWebユーザーに送信できます。"
  - name: Conversion event
    display_name: "コンバージョンイベント"
    description: "<a href=\"{{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events\">コンバージョンイベント</a> は、メッセージを受信した後（またはCanvasやコントロールグループへのエントリー後、チャネルや設定に応じて）、受信者がコンバージョンウィンドウ内で価値の高いアクションを実行したかどうかを記録する成功指標です。コンバージョンイベントを使用して、送信だけでなくCampaignやCanvasのパフォーマンスを測定できます。"
  - name: Currents
    display_name: "Currents"
    description: "Brazeのデータストリーミングエクスポートである<a href=\"{{site.baseurl}}/user_guide/data/distribution/braze_currents\">Currents</a> は、特定のBrazeパッケージに含まれています。Braze Currentsを使用すると、フラットファイルを使用したデータストレージ経由での連携、またはバッチ化されたJSONペイロードを指定されたエンドポイントに送信して、行動分析や顧客データのパートナーとの連携ができます。"
  - name: Custom attributes
    display_name: "カスタム属性"
    description: "<a href=\"{{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes\">カスタム属性</a> とは、ユーザー独自の特徴を集めたものです。ユーザーに関する属性や、アプリケーション内での価値の低いアクションに関する情報を保存するのに適しています。ダッシュボード内でユーザーにカスタム属性を割り当てることができます。<a href=\"{{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift\">Swift</a> と<a href=\"{{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android\">Android</a> 両方のCampaignで、これらの属性に従ってユーザーをフィルタリングし、セグメント化できます。"
  - name: Custom events
    display_name: "カスタムイベント"
    description: "<a href=\"{{site.baseurl}}/user_guide/data/activation/events/custom_events\">カスタムイベント</a> はユーザーによって行われるアクションであり、アプリケーションに対する価値の高いユーザーインタラクションをトラッキングするのに適しています。"
  - name: Data point
    display_name: "データポイント"
    description: "データポイントは以下の場合にカウントされます。<a href=\"{{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes\">カスタム属性</a> が設定または更新されたとき（同じ値で更新している場合でも）、<a href=\"{{site.baseurl}}/user_guide/data/activation/events/custom_events\">カスタムイベント</a> や購入イベントがログに記録されたとき、標準データ（たとえば、<code>email</code>、<code>first_name</code>、<code>last_name</code>、<code>country</code>、あるいは<code>home_city</code>）が記録されるとき、セッションが開始されるとき、セッションが終了するとき。"
  - name: Deep linking
    display_name: "ディープリンク"
    description: "<a href=\"{{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/\">ディープリンク</a> は、顧客を次のアクションやエンゲージメントに導くために使われます。ディープリンクを使えば、Webサイトまたはモバイルアプリ内のターゲットコンテンツとメッセージを接続できます。"
  - name: Dormant users
    display_name: "休眠ユーザー"
    description: "過去12か月間に該当するアクティビティがない場合、ユーザーは<a href=\"{{site.baseurl}}/user_archival/#dormant-users\">休眠</a> 状態とみなされます。ワークスペース内のアプリやWebサイトを使用しておらず、ワークスペースからメッセージを受信しておらず、12か月以上更新されていない場合です。デフォルトでは、Brazeは休眠アーカイブに12か月のウィンドウを使用しますが、会社の設定で日数を上書きできます。"
  - name: Endpoint
    display_name: "エンドポイント"
    description: "通信チャネルの終端（API<a href=\"{{site.baseurl}}/api/endpoints/\">エンドポイント</a> とも呼ばれます）で、メッセージの送信とスケジューリングのためにBrazeメッセージングAPI内で使用されます。"
  - name: Exception event
    display_name: "例外イベント"
    description: "Canvasにおいて、<a href=\"{{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events\">例外イベント</a> は、特定のアクションが発生したときにユーザーをジャーニーから除外するものです（例：注文の完了）。これにより、ユーザーがゴールを達成した後のフォローアップメッセージの関連性が保たれます。終了の評価とタイミングについては、<a href=\"{{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria/\">終了条件</a> を参照してください。"
  - name: External ID
    display_name: "External ID"
    description: "<code>external_id</code>は、Brazeユーザープロファイルの主要なユーザー識別子です。自社システムからIDを割り当てることで、チャネルやデバイスをまたいで同一人物を紐付けます。匿名プロファイルには、ユーザーを識別するまで<code>external_id</code>がない場合があります。詳細については、<a href=\"{{site.baseurl}}/user_guide/get_started/users_and_segments/\">ユーザーとSegments</a> および<a href=\"{{site.baseurl}}/api/basics/#user-ids\">ユーザーID</a> を参照してください。"
  - name: Frequency capping
    display_name: "フリークエンシーキャップ"
    description: "<a href=\"{{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/\">フリークエンシーキャップ</a> を使用すると、オーディエンスに過度の負担をかけることなくコミュニケーションを管理できます。これは、ユーザーが短期間に大量の通信を受信しないようにするためのメッセージの自動制限です。"
  - name: HIPAA
    display_name: "HIPAA"
    description: "HIPAAとは、Health Insurance Portability and Accountability Actの頭文字をとったものです。Brazeは<a href=\"{{site.baseurl}}/developer_guide/disclosures/security_qualifications/#hipaa\">HIPAAに準拠しています</a>。HIPAA要件には、管理的、物理的、技術的セキュリティが含まれます。"
  - name: In-app message
    display_name: "アプリ内メッセージ"
    description: "<a href=\"{{site.baseurl}}/user_guide/channels/in_app_messages\">アプリ内メッセージ</a> は、アプリケーション内に表示されるモバイルメッセージです。プッシュ通知でユーザーの一日を邪魔することなく、コンテンツを届けることができます。カスタマイズされ調整されたアプリ内メッセージは、ユーザーエクスペリエンスを向上させ、オーディエンスがアプリから最大限の価値を得るのに役立ちます。"
  - name: Inactive users
    display_name: "非アクティブユーザー"
    description: "主要なメッセージングチャネル（例：メール、SMS、プッシュ、WhatsApp、LINE（設定に応じて））でリーチできず、ワークスペース内のアプリやWebサイトを6か月以上使用しておらず、ワークスペースからメッセージを6か月以上受信しておらず、6か月以上更新されていない場合、ユーザーは<a href=\"{{site.baseurl}}/user_archival/#inactive-users\">非アクティブ</a> とみなされます。非アクティブユーザーは、休眠ユーザーとともにアーカイブの対象となります。デフォルトでは、Brazeは非アクティブアーカイブに6か月のウィンドウを使用しますが、会社の設定で日数を上書きできます。"
  - name: IP warming
    display_name: "IPウォーミング"
    description: "<a href=\"{{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming\">IPウォーミング</a> とは、専用IPから送信されるメールの量を徐々に増やすことです。これは、インターネットサービスプロバイダーからの評判を確立するのに役立ち、メッセージがフラグを立てられる可能性を最小限に抑えます。"
  - name: Key-value pairs
    display_name: "キーと値のペア"
    description: "<a href=\"{{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs\">キーと値のペア</a> とは、キーが一意の識別子で、値がコンテンツであるリンクされたデータ項目です。ユーザーデバイスに追加のデータペイロードを送信するために使用できます。"
  - name: Liquid
    display_name: "Liquid"
    description: "Liquidは、Shopifyによって作成され、Rubyで書かれた、一般的に使用されている顧客向けのテンプレート言語です。<a href=\"{{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid\">Liquid</a> はダイナミックなコンテンツを読み込んだり、引き出したりするのに使われます。Liquidでは、オブジェクト、タグ、フィルターを使って、<a href=\"{{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags\">個人的なカスタマイズを加える</a> ことができます。"
  - name: Messaging channel
    display_name: "メッセージングチャネル"
    description: "<a href=\"{{site.baseurl}}/user_guide/channels/\">メッセージングチャネル</a> とは、携帯電話やWebブラウザのプッシュ通知、メール、アプリ内メッセージなどを通じて、顧客とバーチャルにコミュニケーションできる方法です。"
  - name: Monthly active user (MAU)
    display_name: "月間アクティブユーザー（MAU）"
    description: 過去30日以内にセッションを行ったユーザーです。
  - name: Multichannel messaging
    display_name: "マルチチャネルメッセージング"
    description: "メール、Webプッシュ、モバイルプッシュ通知の組み合わせなど、さまざまな媒体でユーザーにメッセージを送ることです。<a href=\"{{site.baseurl}}/developer_guide/getting_started/platform_overview/#multichannel-messaging\">メッセージングチャネル</a> は、失われたユーザーを再びエンゲージし、アクティブユーザーを維持し、ブランドアンバサダーを活性化するために、協調して定期的に使用するのが最適です。"
  - name: Multivariate testing
    display_name: "多変量テスト"
    description: "<a href=\"{{site.baseurl}}/user_guide/messaging/ab_testing\">ABテスト</a> は、少数のメッセージバージョンを比較します。<a href=\"{{site.baseurl}}/user_guide/messaging/ab_testing/create_tests/\">多変量テスト</a> は、複数の変数を同時に比較し、どの組み合わせが最もパフォーマンスが高いかを確認します。サポートされているCampaignタイプについて、ダッシュボードから両方を設定できます。"
  - name: New user
    display_name: "新規ユーザー"
    description: Brazeでは、新規ユーザーとは、アプリを新規にインストールしたユーザーのことを指します。あるいは、Braze内でこれまで識別されていないユーザーIDを持つユーザーとして定義することもできます。
  - name: Personalization
    display_name: "パーソナライゼーション"
    description: "テクノロジーを使用して、ユーザーとのコミュニケーションの際に各ユーザーの好みや傾向を考慮に入れる方法です。<a href=\"{{site.baseurl}}/user_guide/messaging/design_and_edit/personalize\">パーソナライズされたメッセージング</a> は、顧客の好みに合わせてカスタマイズすることで、価値ある顧客体験を構築するのに役立ちます。"
  - name: Push message
    display_name: "プッシュメッセージ"
    description: "<a href=\"{{site.baseurl}}/user_guide/channels/push\">プッシュメッセージ</a>（プッシュ通知）とは、モバイルアプリケーションから表示される通知のことです。プッシュ通知は、iOSでもAndroidでも、ポップアップダイアログやバナーとして表示されることが多いです。"
  - name: Push token
    display_name: "プッシュトークン"
    description: "プッシュトークンは、アプリとiOS、Android、またはWebデバイス間の接続を作成するために、AppleまたはGoogleによって作成され、割り当てられた一意のキーです。<a href=\"{{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens\">プッシュトークンの移行</a> とは、すでに生成されたキーをBrazeにインポートすることです。"
  - name: Push time to live (TTL)
    display_name: "プッシュTTL"
    description: "<a href=\"{{site.baseurl}}/user_guide/administer/global/workspace_settings/push_settings\">プッシュTTL</a> とも呼ばれ、有効時間とは、Campaignがオフラインのユーザーへの配信試行を続ける期間を示します。"
  - name: Race condition
    display_name: "競合"
    description: "<a href=\"{{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions\">競合</a> とは、ソフトウェア工学の概念であり、システムが複数の操作を同時に実行しようとしたときに発生する望ましくない状況を説明するものですが、システムの性質上、操作を正しく実行するには正しい順序で実行しなければなりません。<br><br>Brazeプラットフォームでは、イベント発生時に記録されたユーザーデータに基づいてトリガーCampaignをセグメント化すると、競合が発生する可能性があります。これは、Segmentメンバーシップが決定されCampaignが送信された時点で、Campaignがセグメント化されたユーザー属性の変更がまだユーザーに対して処理されていない場合に起こり、ユーザーがCampaignを受け取らないことにつながります。"
  - name: Rate limiting
    display_name: "レート制限"
    description: "<a href=\"{{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/\">レート制限</a> は、Brazeからメッセージが送信される速度を制御します（例：1分あたりの配信速度や、Segmentフィルターを使用したユーザー中心の制限）。同じページのフリークエンシーキャップと連携して機能し、フリークエンシーキャップはユーザーが一定期間に受信するメッセージ数を制限します。"
  - name: Segmentation
    display_name: "セグメンテーション"
    description: "ダッシュボードの<a href=\"{{site.baseurl}}/user_guide/audience/segments\">セグメンテーション</a> では、アプリ内での行動や人口統計データなどの強力なフィルターに基づいて、ユーザーのグループやエクステンションを作成できます。"
  - name: Software development kit (SDK)
    display_name: "ソフトウェア開発キット（SDK）"
    description: "<a href=\"{{site.baseurl}}/developer_guide/getting_started/sdk_overview/\">SDK</a> は、モバイルアプリ、Webサイト、コネクテッドエクスペリエンスに統合され、マーケティング、メッセージング、分析のためのツールを提供します。Brazeは<a href=\"{{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift\">Swift</a> や<a href=\"{{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android\">Android</a> などのプラットフォーム向けにSDKインテグレーションガイドを公開しています。Webやその他のプラットフォームについては、SDK概要からリンクされているインテグレーションパスに従ってください。"
  - name: Subscription groups
    display_name: "購読グループ"
    description: "<a href=\"{{site.baseurl}}/user_guide/channels/email/subscriptions/#subscription-groups\">購読グループ</a> は、グローバルなサブスクリプション状態の上に重ねて、きめ細かなオプトインの選択肢（例：ニュースレターとプロモーション）を提供します。SMSやWhatsAppなどのチャネルにも同様のパターンがあります。チャネルで必要な場合は、常に購読グループをターゲットにしてください。"
  - name: Sunsetting
    display_name: "Sunsetting（配信停止）"
    description: "Sunsetting（配信停止）とは、反応のないユーザーを特定し、ユーザーによるアクションなしで、そのユーザーへの積極的なメッセージングを停止するプロセスのことです。<a href=\"{{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies/\">メール</a> や<a href=\"{{site.baseurl}}/user_guide/channels/push/best_practices/#implement-a-sunset-policy-for-unresponsive-users\">プッシュ</a> メッセージのサンセットポリシーを作成することで、開封率への影響を抑えることができます。"
  - name: Tag
    display_name: "タグ"
    description: "<a href=\"{{site.baseurl}}/user_guide/administer/global/workspace_settings/tags\">タグ</a> は、1つまたは複数のCampaignにまたがるエンゲージメントの分類、整理、並べ替えに役立つツールです。"
  - name: User alias
    display_name: "ユーザーエイリアス"
    description: "<a href=\"{{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users#assigning-user-aliases\">ユーザーエイリアス</a> は、<code>external_id</code>が存在する前に匿名プロファイルに割り当てることができる代替識別子です。ユーザーがログインするまで、デバイスやチャネルをまたいで同一人物を参照できます。"
  - name: User archival
    display_name: "ユーザーアーカイブ"
    description: "<a href=\"{{site.baseurl}}/user_archival/\">ユーザーアーカイブ</a> とは、アーカイブされたユーザーのことです。Brazeでは、これには非アクティブユーザーと休眠ユーザーの両方が含まれます。アーカイブは、Brazeサービスの非アクティブおよび休眠ルールを評価します（スケジューリング、ユーザー数のしきい値などのワークスペースの適格性、会社の設定やCanvasでウィンドウをカスタマイズする方法については、ユーザーアーカイブを参照してください）。"
  - name: User profile
    display_name: "ユーザープロファイル"
    description: "<a href=\"{{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/\">ユーザープロファイル</a> は、Braze内の各ユーザーの中心的なレコードであり、識別子、属性、イベント、購入、デバイス、エンゲージメント履歴、メッセージ履歴が含まれます。プロファイルは、チャネル全体のセグメンテーション、パーソナライゼーション、コンプライアンスワークフローを支えます。"
  - name: Webhook
    display_name: "Webhook"
    description: "<a href=\"{{site.baseurl}}/user_guide/channels/webhooks\">Webhook</a> を使用して、SMSテキストメッセージの配信など、アプリ以外のアクションをトリガーできます。Webhookを使って、他のシステムやアプリケーションにリアルタイムの情報を提供できます。この機能の柔軟性により、どんなエンドポイントにも情報を送ることができます。"
  - name: Workspace
    display_name: "ワークスペース"
    description: "<a href=\"{{site.baseurl}}/user_guide/get_started/workspaces/\">ワークスペース</a> は、Brazeがデータを保存し、チームがCampaign、Canvas、Segmentを構築するコンテナです。各ワークスペースには、1つ以上の<a href=\"{{site.baseurl}}/user_guide/get_started/workspaces/#understanding-workspaces\">アプリインスタンス</a>（そのワークスペースにデータを送信する個々のアプリやサイト）が含まれます。"

---