---
nav_title: キャンバスの作成
article_title: キャンバスの作成
page_order: 1
description: "キャンバスの作成と起動方法について説明します。基本情報の設定、エントリスケジュール、ターゲットオーディエンス、送信設定、ジャーニーの構築などを網羅しています。"
tool: Canvas
search_rank: 1
---

# キャンバスの作成 {#create-a-canvas}

> このリファレンス記事では、キャンバスの作成、管理、テストに必要なステップについて説明します。このガイドに従うか、[Brazeラーニングコースの キャンバス クイック概要](https://learning.braze.com/quick-overview-canvas-setup)をご確認ください。[Braze キャンバステンプレート]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates)から始めることで、セットアップを迅速に進めることもできます。詳細については、[キャンバステンプレート]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates)を参照してください。

{% details 元のキャンバスエディターの詳細を展開 %}
元のキャンバスエクスペリエンスを使用してキャンバスを作成または複製することはできなくなりました。Brazeでは、最新のエディターに[キャンバスをクローン]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases)することを推奨しています。
{% enddetails %}

## ステップ 1: 新しいキャンバスをセットアップする {#step-1-set-up-a-new-canvas}

まず、**Messaging** > **キャンバス** に移動し、**Create キャンバス** を選択します。

キャンバスビルダーが、キャンバスのセットアップをステップバイステップでガイドします。名前の設定からコンバージョンイベントの設定、適切なユーザーをカスタマージャーニーに取り込むところまで、すべてカバーしています。以下の各タブを選択して、各ビルダーステップで調整できる設定を確認してください。

{% tabs local %}
  {% tab 基本情報 %}
    ここでは、キャンバスの基本情報を設定します。
    - キャンバスに名前を付ける
    - チームを追加する
    - タグを追加する
    - コンバージョンイベントを割り当て、イベントタイプと期限を選択する

    [基本情報ステップ](#step-11-start-with-your-canvas-basics)の詳細をご覧ください。
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
    - サブスクリプション設定を選択する
    - キャンバスメッセージの送信レート制限を設定する
    - サイレント時間を有効にして設定する

    [送信設定ステップ](#step-14-select-your-send-settings)の詳細をご覧ください。
  {% endtab %}
  {% tab キャンバスの構築 %}
    ここでは、キャンバスを構築します。

    キャンバスビルダーを使用して[キャンバスを構築する](#step-2-build-your-canvas)方法をご覧ください。
  {% endtab %}
  {% tab サマリー %}
    ここでは、キャンバスの詳細のサマリーを確認できます。[キャンバス承認ワークフロー]({{site.baseurl}}/user_guide/messaging/governance/approvals)が有効になっている場合、起動前にリストされたキャンバスの詳細を承認できます。

  {% endtab %}
{% endtabs %}

### ステップ 1.1: キャンバスの基本情報から始める {#step-11-start-with-your-canvas-basics}

ここでは、キャンバスに名前を付け、[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams#teams)を割り当て、[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags#tags)を作成または追加します。キャンバスのコンバージョンイベントも割り当てることができます。

{% alert tip %}
キャンバスにタグを付けると、検索やレポートの作成が簡単になります。たとえば、[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reports/report_builder)を使用する際に、特定のタグでフィルタリングできます。
{% endalert %}

![キャンバスの詳細ページ。キャンバス名、説明、ロケーション、タグのフィールドがあります。]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

#### コンバージョンイベントを選択する {#choose-conversion-events}

コンバージョンイベントタイプを選択し、記録するコンバージョンを選択します。これらの[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)は、キャンバスの効率を測定します。

![1次コンバージョンイベント A。購入のコンバージョンイベントタイプが設定されており、3日間のコンバージョン期限内に購入を行ったユーザーのコンバージョンを記録します。]({% image_buster /assets/img/add_canvas_conversions.png %})

キャンバスに複数のバリアントまたはコントロールグループがある場合、Brazeはこのコンバージョンイベントを使用して、このコンバージョン目標を達成するための最適なバリエーションを決定します。同じロジックを使用して、複数のコンバージョンイベントを作成できます。

### ステップ 1.2: キャンバスのエントリスケジュールを決定する {#step-12-determine-your-canvas-entry-schedule}

ユーザーがキャンバスに入る方法を3つの中から選択できます。

#### エントリスケジュールのタイプ {#entry-schedule-types}

{% tabs local %}
{% tab スケジュール配信 %}
スケジュール配信では、キャンペーンをスケジュールするのと同様に、ユーザーは時間スケジュールに基づいてエントリします。キャンバスの起動と同時にユーザーを登録したり、将来の特定の時点でジャーニーに入れたり、定期的（毎日、毎週、毎月）にエントリさせたりできます。

月次の定期スケジュールを選択した場合、選択した日が存在しない月があることに注意してください。たとえば、キャンバスを毎月31日に送信するように設定したとします。この場合、Brazeはその月の最終日（4月30日など）に送信します。4月31日は存在しないためです。

この例では、時間ベースのオプションに基づいて、ユーザーは2025年11月14日から2025年12月31日まで、毎週火曜日のローカルタイムゾーンの午後12時にこのキャンバスにエントリします。

![「エントリスケジュール」ページ。タイプが「スケジュール」に設定されています。選択に基づいて、頻度、開始時間、繰り返し、曜日などの時間ベースのオプションが表示されています。]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})

ローカルタイムゾーン配信を使用する場合、Brazeはエントリ適格性を2回評価します。最初にスケジュールされた日のサモア時間（UTC+13）で、次にユーザーのローカルタイムゾーンで評価します。ユーザーがキャンバスに入るには、両方のチェックで適格である必要があります。エントリフィルターが相対的な時間ウィンドウ（たとえば「2日以上前」）を使用している場合、最初のチェック時点で24時間が経過していない可能性があり、ユーザーが1日遅れてエントリすることがあります。これを避けるには、少なくとも2日以上のより広い時間ウィンドウを使用してください。詳細については、[Brazeはローカルタイムゾーン配信のユーザーをいつ評価しますか？]({{site.baseurl}}/user_guide/messaging/campaigns/faq#when-does-braze-evaluate-users-for-local-time-zone-delivery)を参照してください。
{% endtab %}
{% tab アクションベースの配信 %}
アクションベースの配信では、ユーザーはアプリを開く、購入する、カスタムイベントをトリガーするなどの特定のアクションを実行した際にキャンバスに入り、メッセージの受信を開始します。

**エントリオーディエンス**ウィンドウから、再適格性のルールやフリークエンシーキャップの設定など、キャンバスの動作の他の側面を制御できます。アクションベースの配信は、アプリ内メッセージを含むキャンバスコンポーネントでは使用できないことに注意してください。

![アクションベースの配信の例。ユーザーは購入を行った場合にキャンバスに入ります。エントリウィンドウは2025年6月10日午後1時30分に開始されます。]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

{% alert important %}
アクションベースのキャンバスが予想より早くメッセージを送信する場合は、カスタムイベントのタイムスタンプが過去の時刻ではなく現在の時刻で送信されているか確認してください。たとえば、アクションベースのキャンバスにユーザーがカスタムイベントを実行してから3時間の遅延がある場合、Brazeはカスタムイベントと共に送信されたタイムスタンプを使用してその遅延を評価します。タイムスタンプが3時間以上過去の場合、Brazeは遅延がすでに経過したものとして扱い、メッセージを即座に送信します。
{% endalert %}
{% endtab %}
{% tab APIトリガー配信 %}
APIトリガー配信では、API経由で[`/canvas/trigger/send` エンドポイント]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)を使用してユーザーが追加された後、キャンバスに入りメッセージの受信を開始します。ダッシュボードでは、これを行うcURLリクエストの例を確認でき、[コンテキストオブジェクト]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)を使用してオプションの[`context`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)を割り当てることもできます。

![APIトリガー配信の例。キャンバス IDとcURLリクエストの例が表示されています。]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

APIトリガー配信には以下のエンドポイントを使用できます。
- [POST: APIトリガー配信でキャンバスメッセージを送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)
- [POST: APIトリガーキャンバスをスケジュール]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases)
- [POST: スケジュール済みAPIトリガーキャンバスを更新]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases)
{% endtab %}
{% endtabs %}

配信方法を選択した後、ユースケースに合わせて設定を調整し、ターゲットオーディエンスの設定に進みます。

{% details 元のエディターを使用したキャンバスの重複排除動作 %}
再適格性のウィンドウがキャンバスの最大期間より短い場合、ユーザーは再エントリして複数のコンポーネントのメッセージを受信できます。ユーザーの再エントリが前回のエントリと同じコンポーネントに到達するエッジケースでは、Brazeはそのコンポーネントのメッセージを重複排除します。

ユーザーがキャンバスに再エントリし、前回のエントリと同じコンポーネントに到達し、各エントリでアプリ内メッセージの対象となる場合、セッションを2回再開する限り、ユーザーはメッセージを2回受信します（アプリ内メッセージの優先度に依存します）。
{% enddetails %}

### ステップ 1.3: ターゲットエントリオーディエンスを設定する {#step-13-set-your-target-entry-audience}

**ターゲットオーディエンス**ステップでは、定義した条件に一致するユーザーのみがジャーニーに入ることができます。つまり、Brazeはユーザーがキャンバスジャーニーに入る**前に**、まずターゲットオーディエンスの適格性を評価します。たとえば、新規ユーザーをターゲットにしたい場合、1週間以内にアプリを初めて使用したユーザーのセグメントを選択できます。

**エントリコントロール**では、キャンバスが実行されるようにスケジュールされるたびにユーザー数を制限できます。APIトリガーベースおよびアクションベースのキャンバスの場合、この制限はUTC時間の毎時に適用されます。

{% multi_lang_include alerts/warning_alerts.md alert='キャンバス race condition audience trigger' %}

#### オーディエンスのテスト {#testing-your-audience}

ターゲットオーディエンスにセグメントとフィルターを追加した後、[ユーザーを検索]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)して、オーディエンス条件に一致するかどうかを確認することで、オーディエンスが期待通りに設定されているかテストできます。

![「ユーザー検索」フィールド。外部ユーザーIDまたはBraze IDで検索できます。]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### エントリコントロールの選択 {#selecting-entry-controls}

エントリコントロールは、ユーザーがキャンバスに再エントリできるかどうかを決定します。エントリスケジュールのタイプに応じて、選択したケイデンスでこのキャンバスに入る可能性のある人数を制限することもできます。

- **スケジュール:** キャンバスのライフタイム、またはキャンバスがスケジュールされるたび
- **アクションベース:** 毎時、毎日、またはキャンバスのライフタイム
- **APIトリガー:** 毎時、毎日、またはキャンバスのライフタイム

たとえば、アクションベースのキャンバスで**エントリ数を制限**を選択し、**最大エントリ数**フィールドを5,000ユーザーに設定し、制限ケイデンスを**毎日**にした場合、キャンバスは1日あたり5,000ユーザーにのみ送信します。

![「エントリコントロール」ページ。「ユーザーのキャンバス再エントリを許可」と「エントリ数を制限」のチェックボックスが表示されています。後者では、最大エントリ数を設定し、エントリスケジュールのタイプに応じたケイデンスを選択できます（たとえば、スケジュールエントリの場合はキャンバスのライフタイムまたはキャンバスがスケジュールされるたび、アクションベースおよびAPIトリガーエントリの場合は毎時、毎日、またはキャンバスのライフタイム）。]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
Brazeでは、IPウォーミングのときに**キャンバスがスケジュールされるたび**を選択しないことを推奨しています。送信量が増加する可能性があるためです。
{% endalert %}

#### 終了条件の設定 {#setting-exit-criteria}

[終了条件]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria)を設定すると、キャンバスから退出させたいユーザーを決定できます。ユーザーが例外イベントを実行するか、セグメントとフィルターに一致した場合、それ以降のメッセージは受信しません。

#### ターゲット層の計算 {#calculating-target-population}

**ターゲット層**セクションでは、選択したセグメントや追加のフィルターなどのオーディエンスのサマリーと、メッセージングチャネルごとの到達可能なユーザー数の内訳を確認できます。デフォルトの推定値ではなく、ターゲットオーディエンスの到達可能なユーザーの正確な数を計算するには、[正確な統計を計算]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#calculating-exact-statistics)を選択します。

注意事項:

- 正確な統計の計算には数分かかる場合があります。この機能はセグメントレベルでのみ正確な統計を計算し、フィルターやフィルターグループレベルでは計算しません。
- 正確な統計の読み込み中は、概算値が表示される場合があります。正確な数値は読み込みが完了すると**到達可能なユーザー**セクションに表示されます。**追加統計を表示**を選択すると、詳細な内訳を確認できます。
- 大規模なセグメントの場合、正確な統計を計算しても若干の変動が見られることは正常です。この機能の精度は99.999%以上と想定されています。

ターゲットユーザーの平均ライフタイム収益などの追加統計を表示するには、**追加統計を表示**を選択します。

![正確な統計を計算するオプション付きのターゲット層の内訳。]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

#### ターゲットオーディエンス数と到達可能なユーザー数が異なる理由 {#why-the-target-audience-count-could-differ-from-the-reachable-users-count}

{% multi_lang_include audience/segments.md section='Differing audience size' %}

### ステップ 1.4: 送信設定を選択する {#step-14-select-your-send-settings}

**送信設定**を選択して、サブスクリプション設定の編集、レート制限の有効化、[サイレント時間]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)の有効化を行います。[レート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#rate-limiting-and-canvas-components)または[フリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#frequency-capping)を有効にすることで、ユーザーへのマーケティングプレッシャーを軽減し、過剰なメッセージ送信を防ぐことができます。

メールとプッシュチャネルをターゲットとするキャンバスの場合、明示的にオプトインしたユーザーのみがメッセージを受信するようにキャンバスを制限したい場合があります（購読中または購読解除のユーザーを除外）。たとえば、オプトインステータスが異なる3人のユーザーがいるとします。

- **ユーザー A** はメールを購読中で、プッシュが有効です。このユーザーはメールを受信しませんが、プッシュは受信します。
- **ユーザー B** はメールにオプトインしていますが、プッシュは有効ではありません。このユーザーはメールを受信しますが、プッシュは受信しません。
- **ユーザー C** はメールにオプトインしており、プッシュも有効です。このユーザーはメールとプッシュの両方を受信します。

これを行うには、**サブスクリプション設定**を「オプトインしたユーザーのみ」に送信するように設定します。このオプションにより、オプトインしたユーザーのみがメールを受信し、Brazeはデフォルトでプッシュが有効なユーザーにのみプッシュを送信します。

これらのサブスクリプション設定はステップごとに適用されるため、エントリオーディエンスには影響しません。したがって、この設定は各キャンバスステップを受信するためのユーザーの適格性を評価するために使用されます。

{% alert important %}
この設定では、**ターゲットオーディエンス**ステップにオーディエンスを単一チャネルに制限するフィルター（たとえば `Foreground Push Enabled = True` や `Email Subscription = Opted-In`）を含めないでください。
{% endalert %}

必要に応じて、キャンバスの[サイレント時間]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)（メッセージが送信されない時間帯）を指定できます。**送信設定**で**サイレント時間を有効にする**にチェックを入れます。次に、ユーザーのローカルタイムゾーンでサイレント時間を選択し、メッセージを中止するか次の利用可能な時間に送信するかを設定します。

**次の利用可能な時間に送信**を選択した場合、サイレント時間中はメッセージが抑制され、サイレント時間外の次の利用可能な時間に送信されます。たとえば、サイレント時間がユーザーのローカルタイムゾーンで午前11時30分から午後2時30分に設定されており、ユーザーが午前11時35分にメッセージステップに入ったとします。この時間はサイレント時間内であるため、メッセージはまだ送信されず、ユーザーはサイレント時間終了後の午後2時30分にメッセージステップを受信します。

![「サイレント時間」ページ。サイレント時間を有効にするチェックボックスが表示されています。有効にすると、開始時間、終了時間、フォールバック動作を設定できます。]({% image_buster /assets/img/quiet_hours.png %})

## ステップ 2: キャンバスを構築する {#step-2-build-your-canvas}

{% alert tip %}
[Braze キャンバステンプレート]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates)を使用して、時間を節約しキャンバスの作成を効率化しましょう！事前構築されたテンプレートのライブラリーを閲覧して、ユースケースに合ったものを見つけ、特定のニーズに合わせてカスタマイズしてください。詳細については、[キャンバステンプレート]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates)を参照してください。
{% endalert %}

### ステップ 2.1: バリアントを追加する {#step-21-add-a-variant}

![「バリアントを追加」ボタンが選択され、「バリアントを追加」オプションのコンテキストメニューが表示されています。]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

**バリアントを追加**を選択し、キャンバスに新しいバリアントを追加します。バリアントはユーザーがたどるジャーニーを表し、複数のステップと分岐を含めることができます。

<i class="fas fa-plus-circle"></i> プラスボタンを選択して、追加のバリアントを追加できます。新しいバリアントを追加すると、ユーザーがバリアント間でどのように分配されるかを調整でき、異なるエンゲージメント戦略の効果を比較・分析できます。

![Braze キャンバスの2つのバリアント例。]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
デフォルトでは、キャンバスのバリアント割り当てはユーザーIDとキャンバス IDの決定論的ハッシュによって決定されます（ユーザーの[ランダムバケット番号]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers)ではありません）。つまり、バリアント配分の割合が変更されない限り、特定のユーザーは再エントリ時に常に同じバリアントに割り当てられます。起動後にバリアント配分を調整した場合、ユーザーがキャンバスに再エントリする際に異なるバリアントに割り当てられる可能性があります。<br><br>配分の割合を変更しても固定された割り当てが必要な場合は、単一のキャンバスバリアントを使用し、[オーディエンスパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)ステップでユーザーをルーティングしてください。ジャーニーの最初に[ユーザーの更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)ステップを使用して乱数をカスタム属性に保存し、オーディエンスパスでその属性をフィルタリングします。

{% details 手順を展開 %}

1. 乱数を保存する**数値**カスタム属性を作成します。`lottery_number` や `random_assignment` など、見つけやすい名前を付けてください。ダッシュボードで**データ設定** > **カスタム属性**に移動します。<br><br>
2. 単一のキャンバスバリアントを使用します（または各バリアントに同じユーザーの更新ステップを追加します）。ジャーニーの最初に[ユーザーの更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)ステップを追加します。このステップは、ユーザーがオーディエンスパスステップに到達する前に乱数を生成して保存します。<br><br>
3. ユーザーの更新ステップで、[高度なJSONエディター]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#advanced-json-editor)を選択します。{% raw %}{% random %}{% endraw %} タグを使用して数値を生成します。詳細については、[乱数を含むメッセージを送信する]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#send-messages-with-a-random-number)を参照してください。たとえば、{% raw %}`{% random 10 %}`{% endraw %} は0から9の整数を返します。ステップ1のカスタム属性を以下のようなJSONで設定します:<br><br>{% raw %}
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
{% raw %}`{% if %}`{% endraw %} ブロックは、属性が空白の場合にのみ数値を設定するため、ユーザーがキャンバスに再エントリしても同じ割り当てが維持されます。<br><br>

{: start="4"}
4. ユーザーの更新ステップの後に[オーディエンスパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)ステップを追加します。各オーディエンスグループで、バリアント配分の割合を使用する代わりに、カスタム属性に基づくフィルターを追加します。<br><br>たとえば、{% raw %}`{% random 10 %}`{% endraw %} を使用した場合、あるグループは `lottery_number` が**4未満**、別のグループは**3より大きく7未満**、3番目のグループは**6より大きく10未満**とすることができます。

{% enddetails %}
{% endalert %}

### ステップ 2.2: キャンバスステップを追加する {#step-22-add-canvas-steps}

**コンポーネント**サイドバーからコンポーネントをドラッグ＆ドロップして、キャンバスワークフローにステップを追加できます。または、<i class="fas fa-plus-circle"></i> プラスボタンを選択して、ポップオーバーメニューからコンポーネントを追加します。

{% alert tip %}
ステップを追加していくと、ズームレベルを切り替えて詳細にフォーカスしたり、ユーザージャーニー全体を俯瞰したりできます。<kbd>Shift</kbd> + <kbd>+</kbd> でズームイン、<kbd>Shift</kbd> + <kbd>-</kbd> でズームアウトできます。
{% endalert %}

![Braze キャンバスに遅延ステップを追加するコンポーネント検索ウィンドウ。]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert important %}
キャンバスには最大200ステップまで追加できます。キャンバスが200ステップを超えると、読み込みの問題が発生する可能性があります。
{% endalert %}

#### 最大期間 {#maximum-duration}

キャンバスジャーニーのステップが増えると、最大期間はユーザーがこのキャンバスを完了するのにかかる最長の時間を表します。これは、最長パスの各バリアントの各ステップの遅延とトリガーウィンドウを合計して計算されます。たとえば、キャンバスに3日の遅延を持つ遅延ステップとメッセージステップがある場合、キャンバスの最大期間は3日です。

#### ステップの編集 {#editing-a-step}

ユーザージャーニーのステップを編集したい場合は、キャンバスワークフローに応じた方法を確認してください。

キャンバスワークフロー内の任意のコンポーネントを選択して編集できます。たとえば、ワークフローの最初のステップである[遅延]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)コンポーネントを特定の日に編集したいとします。ステップを選択して設定を表示し、遅延を3月1日に調整します。これにより、3月1日にユーザーはキャンバスの次のステップに進みます。

![「遅延」ステップの例。遅延が「特定の日まで」に設定されています。]({% image_buster /assets/img_archive/edit_delay_flow.png %})

または、[アクションパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)ステップの**アクション設定**をすばやく編集・調整して、ユーザーを一定期間保持することもできます。これにより、この評価期間中のアクションに基づいて次のパスが優先されます。

![キャンバスの2番目のステップ「アクション設定」。評価ウィンドウが1日に設定されています。]({% image_buster /assets/img_archive/action_paths_flow.png %})

キャンバスの軽量コンポーネントにより、シンプルな編集体験が実現され、キャンバスの細部の調整がより簡単になります。

#### キャンバス内のメッセージ {#messages-in-canvas}

キャンバスコンポーネント内のメッセージを編集して、特定のステップが送信するメッセージを制御します。キャンバスはメール、モバイルおよびWebプッシュメッセージ、webhookを送信して他のシステムと連携できます。キャンペーンと同様に、特定の[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid)テンプレートを使用してメッセージをパーソナライズできます。

{% alert tip %}
キャンバスコンポーネント名をメッセージやリンクテンプレートに含められることをご存知ですか？<br>
キャンバスで `campaign.${name}` Liquidタグを使用すると、現在のキャンバスコンポーネント名を表示できます。
{% endalert %}

メッセージコンポーネントは、ユーザーに送信されるメッセージを管理します。**メッセージングチャネル**を選択し、**配信設定**を調整してキャンバスメッセージングを最適化できます。このコンポーネントの詳細については、[メッセージ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)を参照してください。

![「メッセージの設定」ステップ。「メッセージングチャネル」が選択されており、Androidプッシュ通知、Content Cards、メールなどの利用可能なメッセージングチャネルのリストが表示されています。]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

キャンバスコンポーネントの設定が完了したら、**Done** を選択します。

{% tabs local %}
{% tab キャンバスエントリプロパティ %}

[`context` オブジェクト]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)は、キャンバス作成の**エントリスケジュール**ステップで設定され、ユーザーをキャンバスに入れるトリガーを示します。これらのプロパティは、APIトリガーキャンバスのエントリペイロードのプロパティにもアクセスできます。`context` オブジェクトは最大50 KBまでです。

キャンバスへのエントリ時に作成されたこれらのプロパティを参照する場合は、次のLiquidを使用します: {% raw %} ``context.${property_name}`` {% endraw %}。イベントはこの方法で使用するには、カスタムイベントまたは購入イベントである必要があることに注意してください。

{% raw %}
たとえば、次のリクエストを考えてみましょう: `"context" : {"product_name" : "shoes", "product_price" : 79.99}`。このLiquid ``{{context.${product_name}}}`` を使用して、メッセージに「shoes」という単語を追加できます。
{% endraw %}

{% endtab %}

{% tab イベントプロパティ %}
イベントプロパティは、カスタムイベントと購入に設定するプロパティです。これらの `event_properties` は、アクションベースの配信を使用するキャンペーンやキャンバスで使用できます。

キャンバスでは、カスタムイベントと購入イベントのプロパティは、アクションパスステップに続く任意のメッセージステップのLiquidで使用できます。これらの `event_properties` を参照する場合は、このLiquid {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %} を使用します。これらのイベントは、メッセージコンポーネントでこの方法で使用するには、カスタムイベントまたは購入イベントである必要があります。

アクションパスに続く最初のメッセージステップでは、そのアクションパスで参照されているイベントに関連する `event_properties` を使用できます。このアクションパスステップとメッセージステップの間に、他のステップ（別のアクションパスやメッセージステップ以外）を挟むことができます。`event_properties` にアクセスできるのは、メッセージステップがアクションパスステップのその他のユーザー以外のパスにさかのぼれる場合のみであることに注意してください。

{% endtab %}
{% endtabs %}

### ステップ 2.3: 接続を編集する {#step-23-edit-connections}

ステップ間の接続を移動するには、2つのコンポーネントを接続する矢印を選択し、別のコンポーネントを選択します。接続を削除するには、矢印を選択し、キャンバスコンポーザーのフッターにある**Cancel Connection**を選択します。

単一のバリアントに同じオーディエンスと送信時間を持つ複数の分岐がある場合、Brazeはそれらの分岐間で均等な分割を保証しません。配分は最初に作成された分岐が優先される場合があります。均等な分割を行うには、各分岐に[ランダムバケット番号]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers)フィルターを使用してください。詳細については、[1つのバリアントを持つキャンバスで、オーディエンスと送信時間が同一の複数の分岐がある場合はどうなりますか？]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches)を参照してください。

## ステップ 3: コントロールグループを追加する {#step-3-add-a-control-group}

<i class="fas fa-plus-circle"></i> プラスボタンを選択して新しいバリアントを追加することで、キャンバスにコントロールグループを追加できます。

Brazeはコントロールグループに配置されたユーザーのコンバージョンを追跡しますが、メッセージは受信しません。正確なテストを維持するために、コンバージョンイベント選択画面に表示されているように、バリアントとコントロールグループのコンバージョン数をまったく同じ期間追跡します。

**バリアント名**ヘッダーをダブルクリックして、メッセージ間の配分を調整できます。

この例では、キャンバスを2つのバリアントに分割しています。バリアント1にはユーザーの70%が含まれます。2番目のバリアントは残りの30%のユーザーを含むコントロールグループです。

![Braze キャンバスのバリアント例。70%が「バリアント1」に進み、最初のステップで1日遅延し、2番目のステップでメッセージを送信します。残りの30%は後続ステップのない「コントロール」に進みます。]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

### キャンバスのインテリジェントセレクション {#intelligent-selection-for-canvas}

インテリジェントセレクション機能が多変量キャンバスで利用可能になりました。多変量キャンペーンの[インテリジェントセレクション]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection)機能と同様に、キャンバスのインテリジェントセレクションは各キャンバスバリアントのパフォーマンスを分析し、各バリアントに送られるユーザーの割合を調整します。この配分は、各バリアントのパフォーマンス指標に基づいて、コンバージョンの合計期待数を最大化するように行われます。

多変量キャンバスでは、コピーだけでなく、タイミングやチャネルもテストできることを覚えておいてください。インテリジェントセレクションを使用すると、キャンバスをより効率的にテストでき、ユーザーが最適なキャンバスジャーニーに送られることに自信を持てます。

![「インテリジェントセレクション」オプションが「バリアント配分の編集」ページで有効になっています。キャンバスを分析・最適化する際、ページ全体に水平バーが表示され、色とサイズが異なる複数のセクションに分割されています。これは視覚的な表現であり、特定の分析に対応するものではありません。]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

キャンバスのインテリジェントセレクションは、各バリアントに振り分けられるユーザーの配分を段階的にリアルタイムで調整することで、キャンバスの結果を最適化します。統計アルゴリズムがバリアント間で決定的な勝者を判定すると、パフォーマンスの低いバリアントを除外し、キャンバスの今後の適格な受信者すべてを勝者バリアントに割り当てます。

このため、インテリジェントセレクションは新しいユーザーが頻繁にエントリするキャンバスで最も効果的に機能します。

## ステップ 4: 保存して起動する {#step-4-save-and-launch}

キャンバスの作成が完了したら、**Launch キャンバス** を選択してキャンバスを保存し起動します。キャンバスを起動すると、**キャンバスの詳細** ページでジャーニーの分析データが入ってくるのを確認できます。

後で戻る必要がある場合は、キャンバスを下書きとして保存することもできます。

![Brazeのキャンバス例。]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
起動後にキャンバスを編集する必要がありますか？可能です！詳細については、[起動後のキャンバスの編集]({{site.baseurl}}/post-launch_edits)を参照してください。
{% endalert %}