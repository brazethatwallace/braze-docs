---
nav_title: キャンバスの作成
article_title: キャンバスの作成
page_order: 1
description: "キャンバスの作成と起動方法について説明します。基本情報の設定、エントリスケジュール、ターゲットオーディエンス、送信設定、ジャーニーの構築などを網羅しています。"
tool: Canvas
search_rank: 1
---

# キャンバスの作成 {#create-a-canvas}

> このリファレンス記事では、キャンバスの作成、管理、テストに必要なステップについて説明します。このガイドに従うか、[Braze Learningコースのキャンバスクイック概要](https://learning.braze.com/quick-overview-canvas-setup)をご確認ください。[Brazeキャンバステンプレート]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates)から始めることで、セットアップを迅速に進めることもできます。詳細については、[キャンバステンプレート]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates)を参照してください。

{% details 元のキャンバスエディターの詳細を展開 %}
元のキャンバスエクスペリエンスを使用してキャンバスを作成または複製することはできなくなりました。Brazeでは、最新のエディターに[キャンバスをクローン]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases)することを推奨しています。
{% enddetails %}

## ステップ1: 新しいキャンバスを設定する {#step-1-set-up-a-new-canvas}

まず、**メッセージング** > **キャンバス**に移動し、**キャンバスを作成**を選択します。

キャンバスビルダーが、キャンバスの設定をステップバイステップでガイドします。名前の設定からコンバージョンイベントの設定、対象ユーザーのカスタマージャーニーへの導入まで、すべてをカバーしています。以下の各タブを選択して、各ビルダーステップで調整できる設定を確認してください。

{% tabs local %}
  {% tab 基本設定 %}
    ここでは、キャンバスの基本設定を行います。
    - キャンバスに名前を付ける
    - チームを追加する
    - タグを追加する
    - コンバージョンイベントを割り当て、イベントタイプと期限を選択する

    [基本設定ステップ](#step-11-start-with-your-canvas-basics)の詳細をご覧ください。
  {% endtab %}
  {% tab エントリスケジュール %}
    ここでは、ユーザーがいつ、どのようにキャンバスに入るかを決定します。
    - スケジュール: 時間ベースのキャンバスエントリです
    - アクションベース: ユーザーが定義されたアクションを実行した後にキャンバスに入ります
    - APIトリガー: APIリクエストを使用してユーザーをキャンバスに入れます

    [エントリスケジュールステップ](#step-12-determine-your-canvas-entry-schedule)の詳細をご覧ください。
  {% endtab %}
  {% tab ターゲットオーディエンス %}
    ここでは、ターゲットオーディエンスを選択します。
    - セグメントとフィルターを追加してオーディエンスを作成する
    - キャンバスの再エントリとエントリ制限を微調整する
    - ターゲットオーディエンスのサマリーを確認する

    [ターゲットオーディエンスステップ](#step-13-set-your-target-entry-audience)の詳細をご覧ください。
  {% endtab %}
  {% tab 送信設定 %}
    ここでは、キャンバスの送信設定を選択します。
    - 購読設定を選択する
    - キャンバスメッセージの送信レート制限を設定する
    - サイレント時間を有効にして設定する

    [送信設定ステップ](#step-14-select-your-send-settings)の詳細をご覧ください。
  {% endtab %}
  {% tab キャンバスを構築 %}
    ここでは、キャンバスを構築します。

    キャンバスビルダーを使用して[キャンバスを構築する](#step-2-build-your-canvas)方法をご覧ください。
  {% endtab %}
  {% tab サマリー %}
    ここでは、キャンバスの詳細のサマリーが表示されます。[キャンバス承認ワークフロー]({{site.baseurl}}/user_guide/messaging/governance/approvals)を有効にしている場合は、起動前にリストされたキャンバスの詳細を承認できます。

  {% endtab %}
{% endtabs %}

### ステップ1.1: キャンバスの基本設定から始める {#step-11-start-with-your-canvas-basics}

ここでは、キャンバスに名前を付け、[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)を割り当て、[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)を作成または追加します。キャンバスのコンバージョンイベントも割り当てることができます。

{% alert tip %}
キャンバスにタグを付けると、検索やレポートの作成が簡単になります。たとえば、[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reports/report_builder)を使用する際に、特定のタグでフィルタリングできます。
{% endalert %}

![キャンバス名、説明、場所、タグのフィールドがあるキャンバス詳細ページ。]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

#### コンバージョンイベントを選択する {#choose-conversion-events}

コンバージョンイベントのタイプを選択し、記録するコンバージョンを選択します。これらの[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)は、キャンバスの効率を測定します。

![1次コンバージョンイベントAで、購入コンバージョンイベントタイプを使用し、3日間のコンバージョン期限内に購入を行ったユーザーのコンバージョンを記録する設定。]({% image_buster /assets/img/add_canvas_conversions.png %})

キャンバスに複数のバリアントまたはコントロールグループがある場合、Brazeはこのコンバージョンイベントを使用して、このコンバージョン目標を達成するための最適なバリエーションを決定します。同じロジックを使用して、複数のコンバージョンイベントを作成できます。

### ステップ1.2: キャンバスのエントリスケジュールを決定する {#step-12-determine-your-canvas-entry-schedule}

ユーザーがキャンバスに入る方法を3つの中から選択できます。

#### エントリスケジュールのタイプ {#entry-schedule-types}

{% tabs local %}
{% tab スケジュール配信 %}
スケジュール配信では、キャンペーンをスケジュールするのと同様に、ユーザーは時間スケジュールに基づいてエントリします。キャンバスの起動と同時にユーザーを登録したり、将来の特定の時点でジャーニーに入れたり、定期的（毎日、毎週、または毎月）に入れたりできます。

月次の定期スケジュールを選択した場合、選択した日が存在しない月があることに注意してください。たとえば、キャンバスを毎月31日に送信するように設定したとします。この場合、Brazeはその月の最終日に送信します（4月31日は存在しないため、4月30日など）。

この例では、時間ベースのオプションに基づいて、ユーザーは2025年11月14日から2025年12月31日まで、毎週火曜日の正午（ローカルタイムゾーン）にこのキャンバスに入ります。

![タイプが「スケジュール」に設定された「エントリスケジュール」ページ。選択に基づいて、頻度、開始時間、繰り返し、曜日などの時間ベースのオプションが表示されています。]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})

ローカルタイムゾーン配信を使用する場合、Brazeはエントリ適格性を2回評価します。最初にスケジュールされた日のサモア時間（UTC+13）で、次にユーザーのローカルタイムで評価します。ユーザーがキャンバスに入るには、両方のチェックで適格である必要があります。エントリフィルターが相対的な時間ウィンドウ（たとえば「2日以上前」）を使用している場合、最初のチェック時に24時間が経過していない可能性があり、ユーザーが1日遅れてエントリすることがあります。これを避けるには、少なくとも2日以上のより広い時間ウィンドウを使用してください。詳細については、[Brazeはローカルタイムゾーン配信でいつユーザーを評価しますか？]({{site.baseurl}}/user_guide/messaging/campaigns/faq#when-does-braze-evaluate-users-for-local-time-zone-delivery)をご覧ください。
{% endtab %}
{% tab アクションベース配信 %}
アクションベース配信では、ユーザーはアプリを開く、購入する、カスタムイベントをトリガーするなどの特定のアクションを実行した際にキャンバスに入り、メッセージの受信を開始します。

**エントリオーディエンス**ウィンドウから、再適格性のルールやフリークエンシーキャップ設定など、キャンバスの動作の他の側面を制御できます。アクションベース配信は、アプリ内メッセージを含むキャンバスコンポーネントでは使用できないことに注意してください。

![アクションベース配信の例。ユーザーは購入を行った場合にキャンバスに入ります。エントリウィンドウは2025年6月10日午後1時30分に開始されます。]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

{% alert note %}
**キャンバスステップとのインタラクション**は、キャンバスのアクションベースのエントリトリガーとしては使用できません。キャンペーンのトリガーとしてのみ使用できます。あるキャンバスから別のキャンバスをトリガーするには、[送信先]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination)キャンバスコンポーネントを使用するか、`/canvas/trigger/send`エンドポイントを呼び出す[Braze間Webhook]({{site.baseurl}}/user_guide/channels/webhooks/use_case_create_a_braze_to_braze_webhook#trigger-a-second-canvas-from-an-initial-canvas)を作成してください。
{% endalert %}

{% alert important %}
アクションベースのキャンバスが予想より早くメッセージを送信する場合は、カスタムイベントのタイムスタンプが過去の日時ではなく現在の時刻で送信されていることを確認してください。たとえば、アクションベースのキャンバスにユーザーがカスタムイベントを実行してから3時間の遅延がある場合、Brazeはカスタムイベントと共に送信されたタイムスタンプを使用してその遅延を評価します。タイムスタンプが3時間以上過去の日時になっている場合、Brazeは遅延がすでに経過したものとして扱い、メッセージを即座に送信します。
{% endalert %}
{% endtab %}
{% tab APIトリガー配信 %}
APIトリガー配信では、ユーザーはAPIを介して[`/canvas/trigger/send`エンドポイント]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)を使用して追加された後、キャンバスに入りメッセージの受信を開始します。ダッシュボードでは、これを行うcURLリクエストの例を確認でき、[コンテキストオブジェクト]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)を使用してオプションの[`context`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)を割り当てることもできます。

![キャンバスIDとcURLリクエストの例が表示されたAPIトリガー配信の例。]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

APIトリガー配信には、以下のエンドポイントを使用できます。
- [POST: APIトリガー配信によるキャンバスメッセージの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)
- [POST: APIトリガーキャンバスのスケジュール]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases)
- [POST: スケジュール済みAPIトリガーキャンバスの更新]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases)
{% endtab %}
{% endtabs %}

配信方法を選択した後、ユースケースに合わせて設定を調整し、ターゲットオーディエンスの設定に進みます。

{% details オリジナルエディターを使用するキャンバスの重複排除動作 %}
再適格性のウィンドウがキャンバスの最大期間より短い場合、ユーザーは再エントリして複数のコンポーネントのメッセージを受信できます。ユーザーの再エントリが前回のエントリと同じコンポーネントに到達するエッジケースでは、Brazeはそのコンポーネントのメッセージを重複排除します。

ユーザーがキャンバスに再エントリし、前回のエントリと同じコンポーネントに到達し、各エントリでアプリ内メッセージの対象となる場合、セッションを2回再開する限り、ユーザーはメッセージを2回受信します（アプリ内メッセージの優先度に依存します）。
{% enddetails %}

### ステップ1.3: ターゲットエントリオーディエンスを設定する {#step-13-set-your-target-entry-audience}

**ターゲットオーディエンス**ステップでは、定義した条件に一致するユーザーのみがジャーニーに入ることができます。つまり、Brazeはユーザーがキャンバスジャーニーに入る**前に**、まずターゲットオーディエンスの適格性を評価します。たとえば、新規ユーザーをターゲットにしたい場合は、1週間以内にアプリを初めて使用したユーザーのセグメントを選択できます。

{% alert important %}
複数のアプリがあるワークスペースでは、キャンバスのエントリオーディエンスの適格性（セグメントとフィルターを含む）は、ユーザーがキャンバスに入る時点でのみ評価され、個々のメッセージステップでは評価されません。ワークスペースに複数のアプリがあり、メッセージステップが特定のアプリのユーザーのみをターゲットにする必要がある場合は、各メッセージステップで以下のいずれかのアプローチを使用してください。
- メッセージステップの[配信バリデーション]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations)で**メッセージ送信時にオーディエンスを検証**を有効にし、アプリ固有のセグメントまたはフィルターを追加します。
- Liquidを使用して、送信時にターゲットデバイスまたはアプリを確認します。

これらの対策がない場合、あるアプリでジャーニーの対象となったユーザーが、ワークスペース内の他のアプリも使用している場合、別のアプリ向けのメッセージを受信する可能性があります。
{% endalert %}

**エントリコントロール**では、キャンバスが実行されるようにスケジュールされるたびにユーザー数を制限できます。APIトリガーベースおよびアクションベースのキャンバスの場合、この制限はUTC時間の毎時に適用されます。

{% multi_lang_include alerts/warning_alerts.md alert='キャンバス race condition audience trigger' %}

#### オーディエンスのテスト {#testing-your-audience}

ターゲットオーディエンスにセグメントとフィルターを追加した後、[ユーザーを検索]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)して、オーディエンス条件に一致するかどうかを確認することで、オーディエンスが期待どおりに設定されているかテストできます。

![外部ユーザーIDまたはBraze IDで検索できる「ユーザー検索」フィールド。]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### エントリコントロールの選択 {#selecting-entry-controls}

エントリコントロールは、ユーザーがキャンバスに再エントリできるかどうかを決定します。エントリスケジュールのタイプに応じて、選択したケイデンスでこのキャンバスに入る可能性のある人数を制限することもできます。

- **スケジュール:** キャンバスのライフタイムまたはキャンバスがスケジュールされるたび
- **アクションベース:** 毎時、毎日、またはキャンバスのライフタイム
- **APIトリガー:** 毎時、毎日、またはキャンバスのライフタイム

たとえば、スケジュールされたキャンバスで**エントリ数を制限**を選択し、**最大エントリ数**フィールドを500,000ユーザーに設定し、制限ケイデンスとして**キャンバスがスケジュールされるたび**を選択した場合、キャンバスはスケジュールされた送信ごとに500,000ユーザーにのみ送信します。

![「キャンバスへの再エントリを許可」と「エントリ数を制限」のチェックボックスが表示された「エントリコントロール」ページ。]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
IPウォームアップには**キャンバスがスケジュールされるたび**を選択することはお勧めしません。送信量が増加する可能性があるためです。
{% endalert %}

#### 終了条件の設定 {#setting-exit-criteria}

[終了条件]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria)を設定すると、キャンバスから退出させたいユーザーを決定できます。ユーザーが例外イベントを実行するか、セグメントとフィルターに一致した場合、それ以降のメッセージは受信しません。

#### ターゲット層の計算 {#calculating-target-population}

**ターゲット層**セクションでは、選択したセグメントや追加フィルターなどのオーディエンスのサマリーと、メッセージングチャネルごとのリーチ可能なユーザー数の内訳を確認できます。デフォルトの推定値ではなく、ターゲットオーディエンスのリーチ可能なユーザーの正確な数を計算するには、[正確な統計を計算]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#calculating-exact-statistics)を選択します。

以下の点に注意してください。

- 正確な統計の計算には数分かかる場合があります。この機能はセグメントレベルでのみ正確な統計を計算し、フィルターやフィルターグループレベルでは計算しません。
- 正確な統計の読み込み中は、概算値が表示される場合があります。正確な数値は読み込み完了時に**リーチ可能なユーザー**セクションに表示されます。**追加統計を表示**を選択すると、詳細な内訳を確認できます。
- 大規模なセグメントの場合、正確な統計を計算しても若干の変動が見られることは正常です。この機能の精度は99.999%以上と予想されます。

ターゲットユーザーの平均ライフタイム収益などの追加統計を表示するには、**追加統計を表示**を選択します。

![正確な統計を計算するオプションがあるターゲット層の内訳。]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

#### ターゲットオーディエンス数がリーチ可能なユーザー数と異なる理由 {#why-the-target-audience-count-could-differ-from-the-reachable-users-count}

{% multi_lang_include audience/segments.md section='Differing audience size' %}

### ステップ1.4: 送信設定を選択する {#step-14-select-your-send-settings}

**送信設定**を選択して、購読設定の編集、レート制限の有効化、[サイレント時間]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)の有効化を行います。[レート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-rate-limiting)や[フリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping)を有効にすることで、ユーザーへのマーケティングプレッシャーを軽減し、過剰なメッセージ送信を防ぐことができます。

メールとプッシュチャネルをターゲットとするキャンバスの場合、明示的にオプトインしたユーザーのみがメッセージを受信するようにキャンバスを制限することをお勧めします（購読済みまたは購読解除済みのユーザーを除外）。たとえば、オプトインステータスが異なる3人のユーザーがいるとします。

{% multi_lang_include messaging/intelligent_channel_user_examples.md %}

これを行うには、**購読設定**を「オプトインしたユーザーのみ」に送信するように設定します。このオプションにより、オプトインしたユーザーのみがメールを受信し、Brazeはデフォルトでプッシュが有効なユーザーにのみプッシュを送信します。

これらの購読設定はステップごとに適用されるため、エントリオーディエンスには影響しません。この設定は、各キャンバスステップを受信するためのユーザーの適格性を評価するために使用されます。

{% alert important %}
この設定では、**ターゲットオーディエンス**ステップにオーディエンスを単一のチャネルに制限するフィルター（たとえば、`Foreground Push Enabled = True`や`Email Subscription = Opted-In`）を含めないでください。
{% endalert %}

キャンバスの[サイレント時間]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)（メッセージが送信されない時間帯）を指定することもできます。**送信設定**で**サイレント時間を有効にする**にチェックを入れます。次に、ユーザーのローカルタイムでサイレント時間を選択し、メッセージを中止するか、次に利用可能な時間に送信するかを選択します。

**次に利用可能な時間に送信**が選択されている場合、サイレント時間はメッセージを抑制し、サイレント時間外の次に利用可能な時間に送信します。たとえば、サイレント時間がユーザーのローカルタイムで午前11時30分から午後2時30分の間にメッセージの送信を防ぐように設定されており、ユーザーが午前11時35分にメッセージステップに入ったとします。この時間はサイレント時間内であるため、メッセージはまだ送信されず、ユーザーはサイレント時間後の午後2時30分にメッセージステップを受信します。

![サイレント時間を有効にするチェックボックスが表示された「サイレント時間」ページ。有効にすると、開始時間、終了時間、フォールバック動作を設定できます。]({% image_buster /assets/img/quiet_hours.png %})

## ステップ2: キャンバスを構築する {#step-2-build-your-canvas}

{% alert tip %}
[Braze キャンバステンプレート]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates)を使用して、キャンバス作成の時間を節約し、効率化しましょう！事前に構築されたテンプレートのライブラリを参照して、ユースケースに合ったものを見つけ、特定のニーズに合わせてカスタマイズしてください。詳細については、[キャンバステンプレート]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates)をご覧ください。
{% endalert %}

### ステップ2.1: バリアントを追加する {#step-21-add-a-variant}

![「バリアントを追加」ボタンが選択され、「バリアントを追加」オプションを含むコンテキストメニューが表示されている様子。]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

**バリアントを追加**を選択し、キャンバスに新しいバリアントを追加します。バリアントはユーザーがたどるジャーニーを表し、複数のステップや分岐を含めることができます。

<i class="fas fa-plus-circle"></i> プラスボタンを選択して、追加のバリアントを追加できます。新しいバリアントを追加すると、ユーザーがバリアント間でどのように分配されるかを調整でき、異なるエンゲージメント戦略の効果を比較・分析できます。

![Brazeキャンバスの2つのバリアント例。]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
デフォルトでは、キャンバスのバリアント割り当てはユーザーIDとキャンバスIDの決定論的ハッシュ（ユーザーの[ランダムバケット番号]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers)ではありません）によって決定されます。つまり、バリアント分配の割合が変更されない限り、特定のユーザーは再エントリ時に常に同じバリアントに割り当てられます。起動後にバリアント分配を調整すると、ユーザーがキャンバスに再エントリした際に異なるバリアントに割り当てられる場合があります。<br><br>分配割合が変更されても割り当てを固定したい場合は、単一のキャンバスバリアントを使用し、[オーディエンスパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)ステップでユーザーをルーティングしてください。ジャーニーの開始時に、[ユーザー更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)ステップを使用してランダムな数値をカスタム属性に保存し、オーディエンスパスでその属性をフィルターします。

{% details 手順を展開 %}

1. ランダムな数値を保存するための**数値**カスタム属性を作成します。`lottery_number`や`random_assignment`など、見つけやすい名前を付けてください。ダッシュボードで、**データ設定** > **カスタム属性**に移動します。<br><br>
2. 単一のキャンバスバリアントを使用します（または各バリアントに同じユーザー更新ステップを追加します）。ジャーニーの最初に[ユーザー更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)ステップを追加します。このステップは、ユーザーがオーディエンスパスステップに到達する前にランダムな数値を生成して保存します。<br><br>
3. ユーザー更新ステップで、[高度なJSONエディター]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#advanced-json-editor)を選択します。{% raw %}{% random %}{% endraw %}タグを使用して数値を生成します。詳細については、[ランダムな数値を含むメッセージを送信する]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#send-messages-with-a-random-number)をご覧ください。例えば、{% raw %}`{% random 10 %}`{% endraw %}は0から9までの整数を返します。ステップ1のカスタム属性を以下のようなJSONで設定します。<br><br>{% raw %}
```json
{% if {{custom_attribute.${lottery_number}}} == blank %}
{% capture lottery_number_str %}{% random 10 %}{% endcapture %}
{
  "attributes": [
    {
      "lottery_number": {{ lottery_number_str | plus: 0 }}
    }
  ]
}
{% endif %}
```
{% endraw %}
<br><br>
{% raw %}`{% if %}`{% endraw %}ブロックは、属性が空白の場合にのみ数値を設定するため、ユーザーがキャンバスに再エントリしても同じ割り当てが維持されます。<br><br>

{: start="4"}
4. ユーザー更新ステップの後に[オーディエンスパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)ステップを追加します。各オーディエンスグループで、バリアント分配の割合を使用する代わりに、カスタム属性に基づくフィルターを追加します。<br><br>例えば、{% raw %}`{% random 10 %}`{% endraw %}を使用した場合、あるグループは`lottery_number`が**4未満**、別のグループは**3より大きく7未満**、3番目のグループは**6より大きく10未満**のようにフィルターを設定できます。

{% enddetails %}
{% endalert %}

### ステップ2.2: キャンバスステップを追加する {#step-22-add-canvas-steps}

**コンポーネント**サイドバーからコンポーネントをドラッグ＆ドロップして、キャンバスワークフローにステップを追加できます。または、<i class="fas fa-plus-circle"></i> プラスボタンを選択して、ポップオーバーメニューからコンポーネントを追加します。

{% alert tip %}
ステップを追加していくと、ズームレベルを切り替えて詳細にフォーカスしたり、ユーザージャーニー全体を俯瞰したりできます。<kbd>Shift</kbd> + <kbd>+</kbd>でズームイン、<kbd>Shift</kbd> + <kbd>-</kbd>でズームアウトできます。
{% endalert %}

![コンポーネント検索ウィンドウからBrazeキャンバスに遅延ステップを追加している様子。]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert important %}
キャンバスには最大200ステップまで追加できます。キャンバスが200ステップを超えると、読み込みの問題が発生する場合があります。
{% endalert %}

#### 最大期間 {#maximum-duration}

キャンバスジャーニーのステップが増えると、最大期間はユーザーがこのキャンバスを完了するまでにかかる最長の時間を表します。これは、最も長いパスについて、各バリアントの各ステップの遅延とトリガーウィンドウを合計して計算されます。例えば、キャンバスに3日間の遅延を持つ遅延ステップとメッセージステップがある場合、キャンバスの最大期間は3日間になります。

#### ステップの編集 {#editing-a-step}

ユーザージャーニーのステップを編集したい場合は、キャンバスワークフローに応じた方法を確認してください。

キャンバスワークフロー内の任意のコンポーネントを選択して、ステップを編集できます。例えば、ワークフローの最初のステップである[遅延]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)コンポーネントを特定の日付に編集したいとします。ステップを選択して設定を表示し、遅延を3月1日に調整します。これにより、3月1日にユーザーがキャンバスの次のステップに進みます。

![遅延が「特定の日まで」に設定された「遅延」ステップの例。]({% image_buster /assets/img_archive/edit_delay_flow.png %})

または、[アクションパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)ステップの**アクション設定**をすばやく編集・調整して、ユーザーを一定期間保持することもできます。これにより、この評価期間中のアクションに基づいて次のパスが優先されます。

![キャンバスの2番目のステップ「アクション設定」で、評価ウィンドウが1日に設定されている様子。]({% image_buster /assets/img_archive/action_paths_flow.png %})

キャンバスの軽量コンポーネントにより、シンプルな編集体験が実現され、キャンバスの細部の調整がより簡単になります。

#### キャンバス内のメッセージ {#messages-in-canvas}

キャンバスコンポーネント内のメッセージを編集して、特定のステップが送信するメッセージを制御します。キャンバスはメール、モバイルおよびWebプッシュメッセージ、webhookを送信して他のシステムと連携できます。キャンペーンと同様に、特定の[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid)テンプレートを使用してメッセージをパーソナライズできます。

{% alert tip %}
キャンバスコンポーネント名をメッセージやリンクテンプレートに含められることをご存知ですか？<br>
`campaign.${name}` Liquidタグをキャンバスで使用すると、現在のキャンバスコンポーネント名を表示できます。
{% endalert %}

メッセージコンポーネントは、ユーザーに送信されるメッセージを管理します。**メッセージングチャネル**を選択し、**配信設定**を調整してキャンバスメッセージングを最適化できます。このコンポーネントの詳細については、[メッセージ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)をご覧ください。

![「メッセージの設定」ステップで、「メッセージングチャネル」が選択され、Androidプッシュ、Content Cards、メールなどの利用可能なメッセージングチャネルのリストが表示されている様子。]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

キャンバスコンポーネントの設定が完了したら、**完了**を選択します。

{% tabs local %}
{% tab キャンバスエントリプロパティ %}

[`context`オブジェクト]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)は、キャンバス作成の**エントリスケジュール**ステップで設定され、ユーザーをキャンバスにエントリさせるトリガーを示します。これらのプロパティは、APIトリガーキャンバスのエントリペイロードのプロパティにもアクセスできます。`context`オブジェクトは最大50 KBまでです。

キャンバスへのエントリ時に作成されたこれらのプロパティを参照する場合は、次のLiquidを使用します: {% raw %} ``context.${property_name}`` {% endraw %}。イベントはカスタムイベントまたは購入イベントである必要があります。

{% raw %}
例えば、次のリクエストを考えてみましょう: `"context" : {"product_name" : "shoes", "product_price" : 79.99}`。このLiquid ``{{context.${product_name}}}``を使用して、メッセージに「shoes」という単語を追加できます。
{% endraw %}

{% endtab %}

{% tab イベントプロパティ %}
イベントプロパティは、カスタムイベントと購入に対して設定するプロパティです。これらの`event_properties`は、アクションベース配信のキャンペーンやキャンバスで使用できます。

キャンバスでは、カスタムイベントと購入イベントのプロパティは、アクションパスステップに続く任意のメッセージステップのLiquidで使用できます。これらの`event_properties`を参照する場合は、このLiquid {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %}を使用します。これらのイベントは、メッセージコンポーネントでこの方法で使用するには、カスタムイベントまたは購入イベントである必要があります。

アクションパスに続く最初のメッセージステップでは、そのアクションパスで参照されているイベントに関連する`event_properties`を使用できます。このアクションパスステップとメッセージステップの間に、他のステップ（別のアクションパスやメッセージステップ以外）を配置できます。`event_properties`にアクセスできるのは、メッセージステップがアクションパスステップの「その他全員」以外のパスにさかのぼれる場合のみです。

{% endtab %}
{% endtabs %}

### ステップ2.3: 接続を編集する {#step-23-edit-connections}

ステップ間の接続を移動するには、2つのコンポーネントを接続する矢印を選択し、別のコンポーネントを選択します。接続を削除するには、矢印を選択し、キャンバスコンポーザーのフッターにある**接続をキャンセル**を選択します。

単一のバリアントに同じオーディエンスと送信時間を持つ複数の分岐がある場合、Brazeはそれらの分岐間で均等な分割を保証しません。分配は最初に作成された分岐が優先される場合があります。均等な分割を行うには、各分岐に[ランダムバケット番号]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers)フィルターを使用してください。詳細については、[1つのバリアントを持つキャンバスで複数の分岐がある場合、オーディエンスと送信時間が同一だとどうなりますか？]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches)をご覧ください。

## ステップ3: コントロールグループを追加する {#step-3-add-a-control-group}

キャンバスにコントロールグループを追加するには、<i class="fas fa-plus-circle"></i> プラスボタンを選択して新しいバリアントを追加します。

Brazeはコントロールグループに配置されたユーザーのコンバージョンを追跡しますが、これらのユーザーにはメッセージは送信されません。正確なテストを維持するために、コンバージョンイベント選択画面に表示されるとおり、バリアントとコントロールグループのコンバージョン数をまったく同じ期間で追跡します。

メッセージ間の配分を調整するには、**バリアント名**ヘッダーをダブルクリックします。

この例では、キャンバスが2つのバリアントに分割されています。バリアント1にはユーザーの70%が割り当てられています。2番目のバリアントは、残りの30%のユーザーが含まれるコントロールグループです。

![Brazeキャンバスのバリアント例。70%が「バリアント1」に進み、最初のステップで1日遅延した後、2番目のステップでメッセージを送信します。残りの30%はフォローアップステップのない「コントロール」に進みます。]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

### キャンバスのインテリジェントセレクション {#intelligent-selection-for-canvas}

インテリジェントセレクション機能が多変量キャンバスで利用できるようになりました。多変量キャンペーンの[インテリジェントセレクション]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection)機能と同様に、キャンバスのインテリジェントセレクションは各キャンバスバリアントのパフォーマンスを分析し、各バリアントに振り分けられるユーザーの割合を調整します。この配分は、コンバージョンの合計期待数を最大化するために、各バリアントのパフォーマンス指標に基づいて行われます。

多変量キャンバスでは、コピーだけでなく、タイミングやチャネルもテストできることを覚えておいてください。インテリジェントセレクションを使用すると、キャンバスをより効率的にテストでき、ユーザーが最適なキャンバスジャーニーに送られることを確信できます。

![「バリアント配分の編集」ページで「インテリジェントセレクション」オプションが有効になっています。キャンバスを分析・最適化する際、ページ全体に水平バーが表示され、色やサイズが異なる複数のセクションに分割されています。これは視覚的な表現であり、特定の分析データとは関連していません。]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

キャンバスのインテリジェントセレクションは、各バリアントに振り分けられるユーザーの配分を段階的にリアルタイムで調整することで、キャンバスの結果を最適化します。統計アルゴリズムがバリアントの中から決定的な勝者を判定すると、パフォーマンスの低いバリアントを除外し、キャンバスの今後の対象受信者すべてを勝者バリアントに割り当てます。

このため、インテリジェントセレクションは、新しいユーザーが頻繁にエントリするキャンバスで最も効果的に機能します。

## ステップ4：保存して起動する {#step-4-save-and-launch}

キャンバスの作成が完了したら、**キャンバスを起動**を選択してキャンバスを保存し、起動します。キャンバスを起動すると、**キャンバスの詳細**ページでジャーニーの分析データを確認できるようになります。

下書きとしてキャンバスを保存し、後で戻って作業を続けることもできます。

![Brazeのキャンバスの例。]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
起動後にキャンバスを編集する必要がありますか？ご安心ください！詳しくは[起動後のキャンバスの編集]({{site.baseurl}}/post-launch_edits)をご覧ください。
{% endalert %}