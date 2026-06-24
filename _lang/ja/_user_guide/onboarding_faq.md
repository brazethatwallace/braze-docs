---
article_title: FAQ
hidden: true
permalink: /onboarding_faq/
excerpt_separator: ""
page_type: glossary
layout: onboarding_faq
description: "このページでは、よくある質問をカテゴリー別にまとめています。"

---

{% multi_lang_include video.html id="keAZAlBR9zc" source="youtube" %}


<!--- Users --->

{% api %}

### 匿名ユーザーデータはどのように処理すればよいですか？ {#how-do-i-handle-anonymous-user-data}

{% apitags %}
Users
{% endapitags %}

最初に、ユーザープロファイルがSDKを通じて認識されると、Brazeは関連付けられた`braze_id`を持つ匿名ユーザープロファイルを作成します。これはBrazeによって設定される一意のユーザー識別子です。

匿名ユーザーをさらに追跡するために、匿名ユーザーに識別子をタグ付けできる[ユーザーエイリアス]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/#user-aliases)を実装できます。これらのユーザーは、エイリアスを使用してエクスポートしたり、APIから参照したりすることができます。

エイリアスを持つ匿名ユーザープロファイルが後で`external_id`で認識された場合、通常の識別済みユーザープロファイルとして扱われますが、既存のエイリアスは保持され、そのエイリアスで引き続き参照できます。

識別済みユーザーとマージしたいエイリアスユーザーの場合、保持したい実際のプロファイルに関連するフィールドをマージできます。エイリアスプロファイルからデータを削除する前に、[識別子によるユーザープロファイルのエクスポートエンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)を使用してそのデータをエクスポートする必要があります。その後、[ユーザー追跡エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を使って、これらのイベントを保持しているプロファイルに投稿できます。これにより、一方のプロファイルには記録されていたが、もう一方には記録されていなかった属性など、保持したいデータが保存されます。

Brazeで新規および既存のユーザーデータを収集するさまざまな方法の詳細については、[データ収集のベストプラクティス]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices/)を参照してください。

{% endapi %}
{% api %}

### Brazeの外部で既に収集・識別したユーザーをインポートするにはどうすればよいですか？ {#how-can-i-import-users-i-have-already-collected-and-identified-outside-of-braze}

{% apitags %}
Users
{% endapitags %}

過去に識別されたユーザーをインポートするには、CSVをBrazeにアップロードするか、APIを通じてデータを送信します。

#### CSV

**オーディエンス** > **ユーザーをインポートする**から、CSVファイルを使用してユーザープロファイルをアップロードおよび更新できます。顧客データをインポートする際には、各顧客の一意の識別子（`external_id`とも呼ばれます）を指定する必要があります。

CSVインポートを開始する前に、Brazeでユーザーをどのように識別するかをエンジニアリングチームから理解しておくことが重要です。一般的に、これは内部で使用されるデータベースIDです。これは、モバイルとWebでBraze SDKがユーザーを識別する方法と一致する必要があります。これにより、各顧客がデバイスを問わずBraze内で単一のユーザープロファイルを持つようになります。Brazeの[ユーザープロファイルのライフサイクル]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/)の詳細をご覧ください。

インポートで`external_id`を指定すると、Brazeは同じ`external_id`を持つ既存のユーザーを更新します。見つからない場合は、その`external_id`を持つ新しい識別済みユーザーを作成します。

CSVインポートテンプレートの詳細およびダウンロードについては、[ユーザーインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/#csv)を参照してください。

#### API

API経由でユーザーをアップロードするには、[ユーザー追跡エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を使用してBrazeにインポートできます。

ユーザーが既にBrazeに存在するかどうか不明な場合は、[識別子によるユーザープロファイルのエクスポートエンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)を実装して確認できます。ユーザーが既にBrazeに存在することを確認した場合は、`/users/track`エンドポイントを使用して、Brazeに既に存在するユーザープロファイルに追加したい新しいデータを投稿できます。

{% alert note %}
`/users/track`エンドポイントを使用する際には、以下の点に留意してください。

- このエンドポイントを通じてエイリアスのみのユーザーを作成する場合は、`_update_existing_only`フラグを明示的にfalseに設定する必要があります。
- このエンドポイントを使用してサブスクリプションステータスを更新すると、external IDで指定されたユーザー（例: User1）と、そのユーザー（User1）と同じメールアドレスを持つすべてのユーザーのサブスクリプションステータスの両方が更新されます。
{% endalert %}

{% endapi %}
{% api %}

### プッシュサブスクリプションのステータスの違いは何ですか？ {#whats-the-difference-between-the-push-subscription-statuses}

{% apitags %}
Users
{% endapitags %}

プッシュサブスクリプションの状態オプションには、購読中、オプトイン、配信停止の3つがあります。

デフォルトでは、プッシュ通知でユーザーがメッセージを受信するには、プッシュサブスクリプションの状態が購読中またはオプトインのいずれかであり、かつプッシュが有効になっている必要があります。メッセージの作成時に、必要に応じてこの設定をオーバーライドできます。

| オプトイン状態 | 説明 |
|---|---|
| 購読中 | Brazeでユーザープロファイルが作成されたときのデフォルトのプッシュサブスクリプション状態です。 |
| オプトイン | ユーザーがプッシュ通知を受け取ることを明示的に希望した状態です。Brazeは、ユーザーがOSレベルのプッシュプロンプトを承認した場合に、ユーザーのオプトイン状態を自動的に`Opted-In`に移動します。<br><br>これはAndroid 12以下のユーザーには適用されません。|
| 配信停止 | ユーザーがアプリケーションやブランドが提供するその他の方法で、プッシュ配信を明示的に解除した状態です。デフォルトで、Brazeのプッシュキャンペーンは`Subscribed`または`Opted-in`のユーザーのみをターゲットにします。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="プッシュサブスクリプションのステータスの違いは何ですか？" }

{% endapi %}
{% api %}

### 重複ユーザーを特定した場合はどうすればよいですか？ {#what-if-ive-identified-duplicated-users}

{% apitags %}
Users
{% endapitags %}

重複ユーザーを特定した場合、それらのユーザープロファイルをクリーンアップする必要があります。以下の手順で行うことができます。

1. `/users/export/ids`エンドポイントを使用してユーザープロファイルをエクスポートします。
2. 正しいユーザープロファイルを特定し（最終的にはチームが正しい情報を決定する必要があります）、以下のいずれかを行います。
    - `/user/track`エンドポイントを使用して、保持したい実際のプロファイルに関連するフィールドをマージする。
    - users/deleteエンドポイントを使用して、データをマージせずに重複した不要なプロファイルを削除する。ユーザープロファイルを削除した後は、**その情報を取り戻す方法はありません**。

{% alert important %}
最初に、正しい`external_id`と対応するカスタム属性およびイベントで新しいユーザープロファイルをインポートすることをお勧めします。ユーザープロファイルは削除すると取得できなくなるため、削除は最後のステップとして行ってください。
{% endalert %}

その他の注意点：

- 重複したユーザープロファイルのエンゲージメントデータ（受信したCampaignsやCanvasesなど）は失われます。過去のエンゲージメントコンテキストを保持する唯一の方法は、カスタム属性として追加することです（受信したすべてのCampaignsやCanvasesの配列カスタム属性など）。
- ユーザープロファイルを移行する際、重複するプロファイルのうちどれを保持するかはチームの判断に委ねられます。Brazeが削除するプロファイルのリストを決定したり提供したりすることはできません。
- 最終的には、チームがユーザーの体験に基づいてサインアッププロセスを評価し、ユーザーが識別されたときのみ`changeUser()`メソッドを呼び出すようにすることが重要です。

{% endapi %}
{% api %}

<!-- セグメント -->

### CSVでユーザーグループをインポートする際にセグメントを作成するにはどうすればよいですか？ {#how-do-i-create-a-segment-when-i-import-a-group-of-users-through-csv}

{% apitags %}
Segments
{% endapitags %}

CSVファイルをインポートするには、[ユーザー]セクションの**ユーザーインポート**ページに移動します。**最近のインポート**テーブルには、最近のインポートが最大20件まで表示され、ファイル名、ファイル内の行数、正常にインポートされた行数、各ファイルの合計行数、各インポートのステータスが確認できます。

**CSVインポート**パネルには、インポートの手順とインポートを開始するボタンがあります。**Select CSV File**をクリックし、目的のファイルを選択します。次に、**Start Import**をクリックする前に、「What do you want us to do with the users in this CSV」の下で、このリストの処理方法をBrazeに指定するオプションがあります。

**Import Users in this CSV and also make it possible to retarget this specific batch of users as a group**を選択し、次に**Automatically generate a segment from the users who are imported from this CSV**を選択します。**Start Import**をクリックすると、Brazeがファイルをアップロードし、列ヘッダーと各列のデータタイプをチェックし、セグメントを作成します。

CSVテンプレートをダウンロードするには、[ユーザーインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/#csv)を参照してください。

{% endapi %}
{% api %}

### セグメントを作成する際にどのような種類のフィルターを使用できますか？ {#what-types-of-filters-can-i-use-when-creating-a-segment}

{% apitags %}
Segments
{% endapitags %}

Braze SDKは、特定の機能や属性に基づいてユーザーをセグメント化し、ターゲットを絞るための強力なフィルター群を提供します。[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/)用語集を使用して、フィルターカテゴリ（カスタムデータ、ユーザーアクティビティ、リターゲティング、マーケティングアクティビティ、ユーザー属性、インストールアトリビューション、ソーシャルアクティビティ、テスト、その他）でこれらのフィルターを検索したり絞り込んだりすることができます。

{% endapi %}
{% api %}

### ロケーションターゲティングを設定して、直近のロケーションでユーザーをセグメント化し、ロケーションベースのCampaignsや戦略に活用するにはどうすればよいですか？ {#how-do-i-set-up-location-targeting-so-that-i-can-segment-users-by-their-most-recent-location-and-use-it-in-my-location-based-campaigns-and-strategies}

{% apitags %}
Segments
{% endapitags %}

エンゲージメントの下にある**Segments**ページに移動し、現在のユーザーセグメントをすべて表示します。このページでは、新しいセグメントを作成して名前を付けることができます。開始するには、**セグメントを作成**をクリックし、セグメントに名前を付けます。

セグメントを作成したら、`Most Recent Location`フィルターを追加して、アプリを最後に使用した場所でユーザーをターゲットに設定します。標準の円形リージョンでユーザーをハイライトするか、カスタムのポリゴンリージョンを作成できます。

- 円形リージョンの場合は、原点を移動し、セグメンテーションのロケーション半径を調整できます。
- ポリゴンリージョンの場合は、セグメントに含めたいエリアをより具体的に指定できます。

{% alert tip %}
Brazeパートナーの支援を受けながらロケーションターゲティングを活用することに興味がありますか？利用可能なBrazeの[文脈に応じたロケーションパートナー]({{site.baseurl}}/partners/message_personalization/)をご覧ください。
{% endalert %}

{% endapi %}
{% api %}

### 過去365日間のカスタムイベントや購入行動に基づいて、ユーザーの正確なリストをターゲットにするにはどうすればよいですか？ {#how-can-i-target-precise-lists-of-users-based-on-their-custom-event-and-purchase-behavior-in-the-past-365-days}

{% apitags %}
Segments
{% endapitags %}

[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/)を使用できます！セグメントエクステンションを使えば、通常のセグメントでは不可能な、より正確なユーザーリストをターゲットにすることができます。

1つのワークスペースにつき最大10個のセグメントエクステンションを作成できます。これらのエクステンションリストは、生成後にセグメントのフィルターとして含めるか除外することができます。セグメントエクステンションを作成する際に、24時間ごとにリストを再生成するように指定することもできます。

1. エンゲージメントの下にある**Segments**を展開し、**セグメントエクステンション**をクリックします。
2. セグメントエクステンションテーブルから、**+ Create New Extension**をクリックします。
3. フィルタリングするユーザーのタイプを記述して、セグメントエクステンションに名前を付けます。これにより、このエクステンションをフィルターとしてセグメントに適用する際に、簡単かつ正確に見つけることができます。
4. ターゲット設定の基準を購入またはカスタムイベントのどちらかから選択します。
5. ユーザーリストのターゲットにしたい購入アイテムまたは特定のカスタムイベントを選択します。
6. ユーザーがイベントを完了する必要がある回数（より多い、より少ない、または等しい）と、さかのぼる日数（最大365日）を選択します。

ターゲティングの精度を上げるために、**Add Property Filters**を選択し、購入またはカスタムイベントの特定のプロパティに基づいてセグメントすることができます。Brazeは、文字列、数値、ブール値、および時間オブジェクトに基づくイベントプロパティのセグメンテーションをサポートしています。

[ネストされたイベントプロパティ]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects/)に基づくセグメンテーションもサポートしています。

セグメントエクステンションはイベントプロパティの長期保存に依存しており、30日間のカスタムイベントプロパティ保存制限はありません。つまり、過去1年以内に追跡されたイベントプロパティを振り返ることができ、トラッキングはエクステンションがセットアップされるまで待つ必要はありません。

{% alert note %}
セグメントエクステンション内でイベントプロパティを使用しても、データポイント使用量には影響しません。
{% endalert %}

{% endapi %}
{% api %}

#### セグメントエクステンションを常に最新の状態に保つ {#keeping-segment-extensions-up-to-date}

{% apitags %}
Segments
{% endapitags %}

このエクステンションで特定の時点の1つのスナップショットを表すか、毎日再生成するかを指定できます。エクステンションは常に最初の保存後に処理を開始します。エクステンションを毎日再生成する場合は、**Regenerate Extension Daily**を選択すると、会社のタイムゾーンで毎日午前0時頃に再生成の処理が開始されます。

完了したら、**Save**をクリックします。エクステンションの処理が開始されます。エクステンションの生成にかかる時間は、ユーザーの数、キャプチャするカスタムイベントまたは購入イベントの数、履歴をさかのぼる日数によって異なります。

最後に、エクステンションを作成した後、セグメントを作成したり、CampaignやCanvasのオーディエンスを定義する際にフィルターとして使用できます。まず、**User Attributes**セクションのフィルターリストから`Braze Segment Extension`を選択します。Brazeセグメントエクステンションフィルターリストから、このセグメントに含めるまたは除外したいエクステンションを選択します。エクステンションの基準を表示するには、**View Extension Details**をクリックします。これで、通常どおりセグメントの作成を進めることができます。

{% endapi %}
{% api %}

<!-- Campaigns -->

### マルチチャネルCampaignはどのように作成しますか？ {#how-do-you-create-a-multichannel-campaign}

{% apitags %}
Campaigns
{% endapitags %}

セットアップ手順、サポートされるチャネル、コンポーザーの切り替え方法については、**Campaignを作成する**の[マルチチャネルCampaigns]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign/#multichannel-campaigns)を参照してください。

{% endapi %}
{% api %}

### Campaignsのテストと最適化を開始するにはどのような方法がありますか？ {#what-are-some-ways-i-can-start-testing-and-optimizing-campaigns}

{% apitags %}
Campaigns
{% endapitags %}

多変量Campaignsを作成し、複数のバリアントでCanvasesを実行することから始めるのがおすすめです。例えば、[多変量Campaign]({{site.baseurl}}/user_guide/messaging/ab_testing/)を実行して、コピーや件名が異なる1つのメッセージをテストできます。複数のバリアントを持つCanvasesは、ワークフロー全体のテストに役立ちます。

{% endapi %}
{% api %}

### 特定のCampaignまたはCanvasのユニーク受信者数と送信数に差があるのはなぜですか？ {#why-is-there-a-difference-between-the-number-of-unique-recipients-and-the-number-of-sends-for-a-given-campaign-or-canvas}

{% apitags %}
Campaigns
{% endapitags %}

この違いの原因として考えられるのは、CampaignまたはCanvasの再適格性がオンになっていることです。これがオンの場合、セグメントと配信設定に該当するユーザーがメッセージを複数回受信できるようになります。再適格性がオンになっていない場合、送信数とユニーク受信者数の違いは、ユーザーがプラットフォームをまたぐ複数のデバイスをプロファイルに関連付けていることが原因と考えられます。

例えば、iOSとWebの両方のプッシュ通知を持つCanvasがある場合、モバイルデバイスとデスクトップデバイスの両方を使用する特定のユーザーは複数のメッセージを受信する可能性があります。

{% endapi %}
{% api %}

### ローカルタイムゾーン配信で何が可能になりますか？ {#what-does-local-time-zone-delivery-offer}

{% apitags %}
Campaigns
{% endapitags %}

ローカルタイムゾーン配信では、ユーザーの個々のタイムゾーンに基づいてセグメントにメッセージングCampaignsを配信できます。ローカルタイムゾーン配信がない場合、CampaignsはBrazeの貴社のタイムゾーン設定に基づいてスケジュールされます。

例えば、ロンドンに拠点を置く企業が午後12時にCampaignを送信すると、アメリカ西海岸のユーザーには午前4時に届きます。アプリが特定の国でのみ提供されている場合はこれが問題にならないかもしれませんが、そうでない場合は、早朝にプッシュ通知をユーザー群に送信することは極力避けることをお勧めします。

{% endapi %}
{% api %}

### Brazeはユーザーのタイムゾーンをどのように認識しますか？ {#how-does-braze-recognize-a-users-time-zone}

{% apitags %}
Campaigns
{% endapitags %}

Brazeはユーザーのタイムゾーンをデバイスから自動的に判別します。これは、タイムゾーンの正確さとユーザーの完全なカバレッジをサポートするように設計されています。ユーザーAPIを通じて作成されたユーザーや、タイムゾーンなしで作成されたユーザーは、SDKによってアプリで認識されるまで、デフォルトのタイムゾーンとして貴社のタイムゾーンが使用されます。

会社のタイムゾーンは[会社の設定]({{site.baseurl}}/user_guide/administer/global/admin_settings/)で確認できます。

{% endapi %}
{% api %}

### ローカルタイムゾーンのCampaignをスケジュールするにはどうすればよいですか？ {#how-do-i-schedule-a-local-time-zone-campaign}

{% apitags %}
Campaigns
{% endapitags %}

Campaignをスケジュールする際は、指定した時刻に送信することを選択してから、**Send campaign to users in their local time zone**を選択する必要があります。

Brazeでは、すべてのローカルタイムゾーンCampaignsを24時間前までにスケジュールすることを強く推奨しています。このようなCampaignは丸一日かけて送信する必要があるため、24時間前にスケジュールすることで、セグメント全体にメッセージを届けることができます。ただし、必要に応じて24時間以内にスケジュールすることも可能です。Brazeは、送信時刻から1時間以上経過しているユーザーにはメッセージを送信しないことに注意してください。

例えば、午後1時にローカルタイムゾーンの午後3時にCampaignをスケジュールした場合、そのCampaignはローカルタイムが午後3時〜4時のすべてのユーザーに即時送信されますが、ローカルタイムが午後5時のユーザーには送信されません。さらに、Campaignで選択する送信時刻は、会社のタイムゾーンでまだ到来していない時刻でなければなりません。

24時間以内にスケジュールされているローカルタイムゾーンのCampaignを編集しても、メッセージのスケジュールは変更されません。ローカルタイムゾーンのCampaignを後の時刻（例えば午後6時ではなく午後7時）に送信するよう編集した場合、元の送信時刻が選択されたときにターゲットセグメントにいたユーザーは、引き続き元の時刻（午後6時）にメッセージを受信します。ローカルタイムゾーンをより早い時刻（例えば午後5時ではなく午後4時）に送信するよう編集しても、Campaignは元の時刻（午後5時）にすべてのセグメントメンバーに送信されます。

{% alert note %}
キャンバスステップの場合、ローカルタイムゾーン配信の次のステップを受信するために、ユーザーが24時間ステップにいる必要はありません。
{% endalert %}

ユーザーがCampaignの再適格性を許可されている場合、元の時刻（午後5時）に再度受信します。ただし、それ以降のCampaignでは、メッセージは更新された時刻にのみ送信されます。

{% endapi %}
{% api %}

### ローカルタイムゾーンのCampaignsの変更はいつ有効になりますか？ {#when-do-changes-to-local-time-zone-campaigns-take-effect}

{% apitags %}
Campaigns
{% endapitags %}

ローカルタイムゾーンCampaignsのターゲットセグメントには、セグメント全体への配信を保証するために、時間ベースのフィルターに少なくとも48時間の期間を含める必要があります。例えば、次のフィルターで2日目のユーザーをターゲットにするセグメントを考えてみましょう。

- 過去1日以上前に初めてアプリを使用
- 過去2日間以内に初めてアプリを使用

ローカルタイムゾーン配信は、配信時刻とユーザーのローカルタイムゾーンに基づいて、このセグメントのユーザーを逃す可能性があります。これは、ユーザーのタイムゾーンが配信をトリガーする前に、ユーザーがセグメントを離れる可能性があるためです。

{% endapi %}
{% api %}

### 開始前のスケジュールされたCampaignsにどのような変更を加えることができますか？ {#what-changes-can-i-make-to-scheduled-campaigns-ahead-of-launch}

{% apitags %}
Campaigns
{% endapitags %}

Campaignがスケジュールされている場合、メッセージを送信するためにキューに入れる前に、メッセージの構成以外の編集を行う必要があります。すべてのCampaignsと同様に、Campaign開始後にコンバージョンイベントを編集することはできません。

{% endapi %}
{% api %}

### スケジュールされたCampaignのメッセージがキューに入る前の「セーフゾーン」とは何ですか？ {#what-is-the-safe-zone-before-messages-on-a-scheduled-campaign-are-queued}

{% apitags %}
Campaigns
{% endapitags %}

- 1回限りのスケジュールCampaignsは、送信予定時刻まで編集できます。
- 定期的なスケジュールCampaignsは、送信予定時刻まで編集できます。
- ローカル送信時間Campaignsは、送信予定時刻の24時間前まで編集できます。
- 最適な送信時間のCampaignsは、送信予定日の24時間前まで編集できます。

{% endapi %}
{% api %}

### 「セーフゾーン」内で編集を行った場合はどうなりますか？ {#what-if-i-make-an-edit-within-the-safe-zone}

{% apitags %}
Campaigns
{% endapitags %}

この時間内にCampaignsの送信時刻を変更すると、次のような望ましくない動作につながる可能性があります。

- Brazeは、送信時刻から1時間以上遅れたユーザーにはメッセージを送信しません。
- 既にキューに入れられたメッセージは、調整された時刻ではなく、元のキュー時刻に送信される場合があります。

{% endapi %}
{% api %}

### 「セーフゾーン」が既に経過している場合はどうすればよいですか？ {#what-should-i-do-if-the-safe-zone-has-already-passed}

{% apitags %}
Campaigns
{% endapitags %}

Campaignsが意図どおりに動作するように、現在のCampaignを停止することをお勧めします（これにより、キューに入っているメッセージがすべて停止します）。その後、Campaignを複製し、必要に応じて変更を加え、新しいCampaignを開始します。既に最初のCampaignを受信したユーザーは、必要に応じてこのCampaignから除外してください。

タイムゾーン送信に対応できるよう、Campaignのスケジュール時間を再調整してください。

{% endapi %}
{% api %}

### Brazeはローカルタイムゾーン配信のユーザーをいつ評価しますか？ {#when-does-braze-evaluate-users-for-local-time-zone-delivery}

{% apitags %}
Campaigns
{% endapitags %}

Brazeは次のタイミングでユーザーのエントリ適格性を評価します。

- スケジュールされた日のサモア時間（UTC+13）
- スケジュールされた日のユーザーのローカルタイム

ユーザーがエントリ適格性を得るには、両方のチェックに合格する必要があります。例えば、2021年8月7日午後2時（ローカルタイムゾーン）にCanvasの開始がスケジュールされている場合、ニューヨーク在住のユーザーをターゲットにするには、以下の適格性チェックが必要です。

- 2021年8月6日午後9時（ニューヨーク時間）
- 2021年8月7日午後2時（ニューヨーク時間）

エントリするには、ユーザーは両方の評価時点でオーディエンスとフィルターに一致している必要があります。ユーザーが最初のチェックで不適格となった場合、Brazeは2回目のチェックを実行しません。ユーザーが開始前にセグメントに一定期間いる必要はなく、各チェック時点での適格性のみが重要です。

この評価動作は、[ダッシュボードでCampaignをどのくらい前にスケジュールするか]({{site.baseurl}}/user_guide/messaging/campaigns/faq/#how-do-i-schedule-a-local-time-zone-campaign)とは別のものです。詳しい説明、例、スケジュールのガイダンスについては、CampaignsのFAQの[Brazeはローカルタイムゾーン配信のユーザーをいつ評価しますか？]({{site.baseurl}}/user_guide/messaging/campaigns/faq/#when-does-braze-evaluate-users-for-local-time-zone-delivery)と[ローカルタイムゾーンのCampaignをスケジュールするにはどうすればよいですか？]({{site.baseurl}}/user_guide/messaging/campaigns/faq/#how-do-i-schedule-a-local-time-zone-campaign)を参照してください。

{% endapi %}
{% api %}

### Campaignに入るユーザー数が予想数と一致しないのはなぜですか？ {#why-does-the-number-of-users-entering-a-campaign-not-match-the-expected-number}

{% apitags %}
Campaigns
{% endapitags %}

Campaignに入るユーザー数は、オーディエンスやトリガーの評価方法によって予想数と異なる場合があります。Brazeでは、オーディエンスはトリガーの前に評価されます（[属性の変更トリガー]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers/#change-custom-attribute-value)を使用する場合を除きます）。これにより、トリガーアクションが評価される前に、ユーザーが選択したオーディエンスに含まれていない場合、Campaignから脱落する原因となります。

{% endapi %}
{% api %}

<!-- Canvases -->

### バリアントが1つで分岐が複数あるCanvasで、オーディエンスと送信時刻が同一の場合はどうなりますか？ {#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches}

{% apitags %}
Canvases
{% endapitags %}

各ステップのジョブをキューに入れ、ほぼ同時に実行し、どちらかが「勝ちます」。実際には、ほぼ均等に分配される可能性がありますが、最初に作成されたステップが若干有利になる傾向があります。

また、この分布がどのようになるかを正確に保証することはできません。均等に分けたい場合は、[ランダムバケット番号]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/)フィルターを追加してください。

{% endapi %}
{% api %}

### Canvasを停止するとどうなりますか？ {#what-happens-when-you-stop-a-canvas}

{% apitags %}
Canvases
{% endapitags %}

Canvasを停止すると、以下が適用されます。

- ユーザーがCanvasに入れなくなります。
- ユーザーがフローのどの位置にいても、メッセージはそれ以上送信されません。
    - **例外:** メールCanvasesはすぐには停止しません。送信リクエストがSendGridに送られた後は、ユーザーへの配信を停止するためにBrazeができることはありません。

{% alert note %}
Canvasを停止しても、ステップで待機しているユーザーは退出しません。Canvasを再度有効にしてもユーザーがまだ待機している場合、ユーザーはステップを完了し、次のコンポーネントに進みます。ただし、ユーザーが次のコンポーネントに進むべき時間が既に過ぎている場合、ユーザーはCanvasを退出します。
{% endalert %}

{% endapi %}
{% api %}

### 例外イベントはいつトリガーされますか？ {#when-does-an-exception-event-trigger}

{% apitags %}
Canvases
{% endapitags %}

例外イベントがトリガーされるのは、ユーザーがそのイベントに関連するCanvasコンポーネントの受信を待機している間だけです。ユーザーが事前にアクションを実行した場合、例外イベントはトリガーされません。

事前に特定のイベントを実行したユーザーを除外したい場合は、代わりに[フィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/)を使用してください。

{% endapi %}
{% api %}

### Canvasの編集は、既にCanvasに入っているユーザーにどのような影響を与えますか？ {#how-does-editing-a-canvas-affect-users-already-in-the-canvas}

{% apitags %}
Canvases
{% endapitags %}

マルチステップCanvasの一部のステップを編集した場合、既にオーディエンスに含まれているがステップをまだ受け取っていないユーザーは、更新後のバージョンのメッセージを受け取ります。これは、まだそのステップで評価されていない場合にのみ該当することに注意してください。

開始後に編集できる内容の詳細については、[開始後にCanvasを変更する]({{site.baseurl}}/post-launch_edits/)を参照してください。

{% endapi %}
{% api %}

### Canvasでユーザーのコンバージョンはどのように追跡されますか？ {#how-are-user-conversions-tracked-in-a-canvas}

{% apitags %}
Canvases
{% endapitags %}

ユーザーがコンバージョンできるのは、Canvasのエントリごとに1回のみです。

コンバージョンは、そのエントリでユーザーが受信した最新のメッセージに割り当てられます。Canvasの最初にある要約ブロックには、メッセージを受け取ったかどうかに関わらず、そのパス内でユーザーが行ったすべてのコンバージョンが反映されます。それ以降の各ステップには、そのステップがユーザーが最後に受け取ったステップであった間に発生したコンバージョンのみが表示されます。

{% details ユースケース %}

#### ユースケース 1 {#use-case-1}

Canvasのパスに10個のプッシュ通知があり、コンバージョンイベントは「セッション開始」（「アプリを開く」）になっているとします。

- ユーザーAはエントリ後、最初のメッセージを受け取る前にアプリを開きます。
- ユーザーBはプッシュ通知のたびにアプリを開きます。

**結果:**
要約には2つのコンバージョンが表示されますが、個々のステップでは最初のステップのコンバージョンが1、それ以降のステップではすべてゼロとなります。

{% alert note %}
コンバージョンイベントが発生したときにサイレント時間がアクティブな場合、同じルールが適用されます。
{% endalert %}

#### ユースケース 2 {#use-case-2}

サイレント時間を有効にした1ステップのCanvasがあるとします。

1. ユーザーがCanvasに入ります。
2. 最初のステップに遅延はありませんが、サイレント時間内であるため、メッセージは抑制されます。
3. ユーザーがコンバージョンイベントを実行します。

**結果:**
ユーザーはCanvasのバリアント全体ではコンバージョン済みとしてカウントされますが、ステップを受け取っていないため、ステップに対してはカウントされません。

{% enddetails %}

{% endapi %}
{% api %}

### ユニークユーザー数を見る場合、Canvas分析とセグメンターのどちらがより正確ですか？ {#when-looking-at-the-number-of-unique-users-is-canvas-analytics-or-the-segmenter-more-accurate}

{% apitags %}
Canvases
{% endapitags %}

セグメンターは、CanvasやCampaignの統計と比較して、より正確なユニークユーザーデータの統計を提供します。これは、CanvasやCampaignの統計値は、何かが起こるとBrazeによってインクリメントされる数値であるためです。そのため、変数によってはこの数値がセグメンターの数値と異なる可能性があります。例えば、ユーザーは1つのCanvasやCampaignで複数回コンバージョンする可能性があります。

{% endapi %}
{% api %}

### Canvasに入るユーザー数が予想数と一致しないのはなぜですか？ {#why-does-the-number-of-users-entering-a-canvas-not-match-the-expected-number}

{% apitags %}
Canvases
{% endapitags %}

Canvasに入るユーザー数は、オーディエンスやトリガーの評価方法によって予想数と異なる場合があります。Brazeでは、オーディエンスはトリガーの前に評価されます（[属性の変更]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers/#change-custom-attribute-value)トリガーを使用する場合を除きます）。そのため、選択したオーディエンスに含まれない場合、ユーザーはトリガーアクションが評価される前にCanvasから脱落します。

{% endapi %}
{% api %}

<!-- 分析 -->

### Brazeはどのような指標を測定していますか？ {#what-metrics-does-braze-measure}

{% apitags %}
Analytics
{% endapitags %}

チャネルに応じて、Brazeはさまざまな指標を測定し、Campaignの成功を判断し、今後のCampaignsに反映させることができます。包括的なリストは、[レポート指標用語集]({{site.baseurl}}/user_guide/analytics/metrics_glossary/)を参照してください。

{% endapi %}
{% api %}

### Brazeの収益はどのように計算されますか？ {#how-is-revenue-calculated-in-braze}

{% apitags %}
Analytics
{% endapitags %}

**収益**ページでは、特定の期間の特定商品の収益または購入、またはアプリの総収益または購入に関するデータを表示できます。これらの収益データは、一定のコンバージョン期間内にCampaign受信者が行った購入から生成されます。

ただし、Brazeはマーケティングツールであり、収益管理ツールではないことに注意する必要があります。弊社の[購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/)は払い戻しやキャンセルをサポートしていないため、他のツールとデータを比較する際に差異が生じる可能性があります。

{% endapi %}
{% api %}

### Currentsではどのようなレポート機能が有効になりますか？ {#what-reporting-capabilities-does-currents-enable}

{% apitags %}
Analytics
{% endapitags %}

Currentsツールは、メッセージングエンゲージメントと顧客行動データの両方を、弊社の多くのデータパートナーのいずれかに継続的にストリーミングします。これにより、Brazeが作成するユニークで価値のあるデータを活用して、クラス最高のパートナー各社におけるビジネスインテリジェンスと分析の取り組みを強化できます。

このデータには、メッセージングエンゲージメントの指標にとどまらず、カスタム属性やイベントのパフォーマンスなど、より複雑な数値も含まれます。詳細については、[Currentsのイベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)を参照してください。

{% endapi %}
{% api %}

### 定期的なエンゲージメントレポートをスケジュールするにはどうすればよいですか？ {#how-can-i-schedule-a-recurring-engagement-report}

{% apitags %}
Analytics
{% endapitags %}

定期的なエンゲージメントレポートをスケジュールするには、以下の手順を行います。

1. ダッシュボードアカウントで、**Data**の下にある**Engagement Reports**に移動します。
2. **+ Create New Report**をクリックします。
3. レポートにまとめたい[CampaignsとCanvasメッセージ]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports/#manually-select-campaigns-or-canvases)を（個別または[タグごとに]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports/#automatically-select-campaigns-or-canvases)）追加します。
4. レポートに[統計を追加]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports/#add-statistics-to-your-report)します。
5. レポートの圧縮とデリミタを選択します。
6. このレポートを受け取る会社ユーザーのメールアドレスを入力します。
7. レポートでデータを実行する[期間]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports/#time-frame)を選択します。
8. データの内訳を確認したい[間隔（毎日、毎週など）]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports/#data-display)を選択します。
9. レポートを[すぐに送信]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports/#send-immediately)するか、[将来の指定時刻]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports/#send-at-designated-time)に送信するかを設定します。
10. レポートを実行し、メールが届いたら開きましょう！

{% endapi %}
{% api %}

### エンゲージメントレポートとレポートビルダーの違いは何ですか？ {#whats-the-difference-between-engagement-reports-and-the-report-builder}

{% apitags %}
Analytics
{% endapitags %}

エンゲージメントレポートは、CampaignsやCanvasesからの特定のメッセージに対するエンゲージメント統計のCSVを、トリガーメールで提供します。特定のデータは、CampaignまたはCanvasレベルで集計され、個々のバリアントやステップレベルではありません。レポートはダッシュボードに保存されず、レポートを再実行すると統計が更新される場合があります。

レポートビルダーを使用すると、複数のCampaignsまたはCanvasesの結果を1つのビューで比較できるため、主要な指標に最も影響を与えたエンゲージメント戦略を簡単に判断できます。CampaignsとCanvasesの両方について、データをエクスポートし、レポートを保存して今後表示できます。

Brazeのレポートと分析の使用方法の詳細については、[レポートの概要]({{site.baseurl}}/user_guide/analytics/reports/)を参照してください。

{% endapi %}