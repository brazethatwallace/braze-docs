---
nav_title: Content Cardsの作成
article_title: Content Cardsの作成
page_order: 1
description: "このリファレンス記事では、Brazeのキャンペーンやキャンバスを使用してContent Cardsを作成、構成、設定、送信する方法について説明します。"
tool:
  - Canvas
  - Campaigns
channel:
  - content cards
search_rank: 3.9

---

# Content Cardsの作成 {#create-a-content-card}

> この記事では、キャンペーンやキャンバスを構築する際にBrazeでContent Cardsを作成する方法について説明します。ここでは、メッセージタイプの選択、カードの作成、メッセージ配信のスケジュール設定について順を追って説明します。

## ステップ1: メッセージの作成場所を選択する {#step-1-choose-where-to-build-your-message}

キャンペーンは、シンプルな単一メッセージング（1つのメッセージで製品についてユーザーに通知するなど）に使用します。キャンバスは、複数ステップのユーザージャーニー（時間の経過に伴うユーザー行動に基づいてカスタマイズされた製品提案を送信するなど）に使用します。

{% tabs %}
{% tab キャンペーン %}

1. **メッセージング** > **キャンペーン** に移動し、**キャンペーンを作成** を選択します。
2. **Content Cards** を選択するか、複数チャネルをターゲットとするキャンペーンの場合は **マルチチャネル** を選択します。
3. キャンペーンにわかりやすく意味のある名前を付けます。
4. 必要に応じて[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)と[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)を追加します。
   * タグを使用すると、キャンペーンを見つけやすくなり、レポートを作成しやすくなります。たとえば、[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reports/report_builder)を使用する際に、関連するタグでフィルタリングできます。
5. キャンペーンに必要な数のバリアントを追加して名前を付けます。追加した各バリアントに対して、異なるプラットフォーム、メッセージタイプ、レイアウトを選択できます。バリアントの詳細については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似している、または同じコンテンツを持つ場合は、追加のバリアントを追加する前にメッセージを作成してください。その後、**バリアントを追加** ドロップダウンから **バリアントからコピー** を選択できます。
{% endalert %}

{% endtab %}
{% tab キャンバス %}

1. キャンバスコンポーザーを使用して[キャンバスを作成]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)します。
2. キャンバスの設定後、キャンバスビルダーでメッセージステップを追加します。ステップにわかりやすく意味のある名前を付けます。
3. メッセージングチャネルとして **Content Cards** を選択します。
4. BrazeがContent Cardsのオーディエンスの適格性とパーソナライゼーションを計算するタイミングを選択します。ステップエントリ時または初回インプレッション時（推奨）を選択できます。Content Cardsを含むステップは、スケジュール配信またはアクションベースで設定できます。
5. ユーザーが購入を完了した場合やカスタムイベントを実行した場合にContent Cardsを削除するかどうかを選択します。
6. Content Cardsの有効期限（フィード内の表示期間）を設定します。一定期間後または特定の時刻に設定できます。
7. **配信設定**で、必要に応じてこのステップのオーディエンス（受信者）をフィルタリングします。セグメントを指定し、追加のフィルターを加えることで、オーディエンスをさらに絞り込むことができます。オーディエンスオプションは、遅延後のメッセージ送信時にチェックされます。
8. メッセージと組み合わせたい他のメッセージングチャネルを選択します。

{% endtab %}
{% endtabs %}

## ステップ2: メッセージタイプを指定する {#step-2-specify-your-message-types}

3つの基本的なContent Cardsタイプから1つを選択します: **クラシック**、**キャプション付き画像**、**画像のみ**。

各タイプの想定される動作と外観の詳細については、[クリエイティブの詳細]({{site.baseurl}}/user_guide/channels/content_cards/creative_details)を参照するか、以下の表のリンクを確認してください。これらのContent Cardsタイプは、モバイルアプリとWebアプリケーションの両方で使用できます。

| メッセージタイプ | 例 | 説明 |
|---|---|---|
|[クラシック]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types)| ![ワークアウトクラスの予約を促す小さなアイコンとテキストが表示されたクラシックContent Card。]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) | クラシックカードは、太字のタイトル、メッセージテキスト、およびタイトルとテキストの先頭に配置されるオプションの画像を備えたシンプルなレイアウトです。クラシックカードには正方形の画像またはアイコンの使用が最適です。 |
|[キャプション付き画像]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types)| ![ウェイトリフターの画像とワークアウトクラスの予約を促すテキストが表示されたキャプション付きContent Card。]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | キャプション付き画像カードは、コピーと目を引く画像でコンテンツを紹介します。 |
|[画像のみ]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types)| ![テキストのみが表示された画像のみのContent Card。]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | 画像のみカードは、画像、GIF、その他のテキスト以外のクリエイティブコンテンツ用のスペースで注目を集めます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ2: メッセージタイプを指定する" }

## ステップ3: Content Cardsを作成する {#step-3-compose-a-content-card}

メッセージエディターの**作成**タブで、メッセージのコンテンツと動作のすべての側面を編集できます。

![メッセージエディターの作成タブにおけるContent Cardsの詳細のサンプル。]({% image_buster /assets/img/content_card_compose.png %})

ここに表示されるコンテンツは、前のステップで選択した**カードタイプ**によって異なりますが、以下のオプションのいずれかが含まれる場合があります。

### 言語 {#language}

**言語を追加**を選択して、提供されたリストから希望する言語を追加します。これにより、メッセージに[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic)が挿入されます。コンテンツを作成する前に言語を選択し、Liquid内の適切な場所にテキストを入力できるようにすることをお勧めします。使用可能な言語の完全なリストについては、[サポートされている言語]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization#languages-supported)を参照してください。

![英語、スペイン語、フランス語が言語として選択され、タイトル、説明、リンクテキストが国際化するフィールドとして選択されたウィンドウ。]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

#### 右から左へのメッセージを作成する {#create-right-to-left-messages}

右から左へのメッセージの最終的な表示は、サービスプロバイダーがどのようにレンダリングするかに大きく依存します。できるだけ正確に表示される右から左へのメッセージを作成するためのベストプラクティスについては、[右から左へのメッセージの作成]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)を参照してください。

#### タイトルとメッセージ {#title-and-message}

自由に記述できます。制限はありませんが、メッセージを素早く伝えて顧客にクリックしてもらえるほど効果的です。明確で簡潔なタイトルとメッセージコンテンツをお勧めします。これらのフィールドは画像のみのカードには提供されないことに注意してください。

#### 画像 {#image}

Content Cardsに画像を追加するには、**画像を追加**を選択するか、画像URLを入力します。**画像を追加**を選択すると**メディアライブラリ**が開き、以前にアップロードした画像を選択するか、新しい画像を追加できます。

メッセージタイプとプラットフォームごとに推奨される比率と要件が異なる場合があるため、画像を依頼したりゼロから作成したりする前に、必ず確認してください。Content Cardsのメッセージフィールドは合計サイズが2&nbsp;KBに制限されていることに注意してください。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### トップに固定 {#pin-to-top}

Brazeは固定されたカードをユーザーのフィードの上部に表示し、ユーザーはそれを閉じることができません。ユーザーのフィードに複数の固定カードがある場合、Brazeはそれらを時系列順に並べます。BrazeがContent Cardsを配信する際、カードは固定または非固定のいずれかであり、そのステータスはカードの有効期間中変更されません。キャンペーンの固定設定を変更した場合、更新は変更後に送信されたカードにのみ適用されます。すでにユーザーのフィードにあるカードの固定ステータスは変更されません。

![「このカードをフィードのトップに固定する」オプションが選択された、モバイルとWebのBrazeにおけるContent Cardsプレビューの並列表示。]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### クリック時の動作 {#on-click-behavior}

顧客がカード内の表示されたリンクをクリックすると、リンクはアプリ内のより深い場所または別のサイトに誘導できます。Content Cardsのクリック時の動作を選択する場合は、それに応じて**リンクテキスト**を更新することを忘れないでください。

Content Cardsのリンクには以下のアクションが利用可能です。

| アクション | 説明 |
|---|---|
| Web URLにリダイレクト | ネイティブでないWebページを開きます。 |
| [アプリへのディープリンク]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content) | アプリ内の既存の画面にディープリンクします。 |
| カスタムイベントを記録 | トリガーする[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)を選択します。別のContent Cardsの表示や追加のメッセージングのトリガーに使用できます。 |
| カスタム属性を記録 | 現在のユーザーに設定する[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)を選択します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="クリック時の動作" }

**カスタムイベントを記録**および**カスタム属性を記録**オプションには、以下のSDKバージョンの互換性が必要です。

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## ステップ4: 追加設定を構成する（オプション） {#step-4-configure-additional-settings-optional}

[キーと値のペア]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs)を使用して、カードのカテゴリを作成したり、[複数のContent Cardsフィード]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed#multiple-feeds)を作成したり、カードの並べ替え方法をカスタマイズしたりできます。

メッセージにキーと値のペアを追加するには、**設定**タブに移動して**新しいペアを追加**を選択します。

## ステップ5: キャンペーンまたはキャンバスの残りの部分を構築する {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab キャンペーン %}

キャンペーンの残りの部分を構築します。Content Cardsを構築するためのツールの最適な使い方については、次のセクションに進んでください。

### 配信スケジュールまたはトリガーを選択する {#choose-a-delivery-schedule-or-trigger}

Content Cardsは、スケジュールされた時間、アクション、またはAPIトリガーに基づいて配信できます。詳細については、[キャンペーンのスケジュール]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)を参照してください。

また、キャンペーンの期間と[サイレント時間]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)を設定し、Content Cardsの有効期限を決定することもできます。特定の有効期限日、またはカードの有効期限が切れるまでの日数（最大30日）を設定します。すべてのバリアントの有効期限は同一です。

有効期限のカウントダウンは、カードの送信時刻から開始されます。

- **スケジュールされたキャンペーン:** カウントダウンはスケジュールされた起動時刻に開始されます。
- **アクションベースのキャンペーン:** カウントダウンはユーザーがトリガーアクションを実行した時点で開始されます。

たとえば、アクションベースのContent Cardsが本日午後2時に送信され、有効期限が1日の場合、翌日の午後2時に期限切れとなります。

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

アクションベースの配信では、Content Cardsが表示されるまでに短い遅延が予想されます。この遅延が発生する理由と最小限に抑える方法の詳細については、[トリガーイベントの直後にContent Cardsが表示されないのはなぜですか？]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#why-dont-content-cards-appear-immediately-after-a-trigger-event)を参照してください。

#### スケジュール配信 {#scheduled-delivery}

スケジュール配信のContent Cardsキャンペーンでは、カードの作成タイミングを指定することで、Brazeが新しいContent Cardsキャンペーンのオーディエンスの適格性とパーソナライゼーションを評価するタイミングを選択できます。詳細については、[カード作成]({{site.baseurl}}/card_creation)を参照してください。

#### ターゲットユーザーを選択する {#choose-users-to-target}

次に、セグメントまたはフィルターを選択してオーディエンスを絞り込み、[ユーザーをターゲット]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)にします。おおよそのセグメント人口のプレビューが自動的に表示されます。正確なセグメントメンバーシップは、メッセージが送信される前に常に計算されることに留意してください。

{% multi_lang_include audience/target_audiences.md %}

#### コンバージョンイベントを選択する {#choose-conversion-events}

Brazeでは、キャンペーンを受信した後にユーザーが特定のアクション（[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)）を実行する頻度をトラッキングできます。ユーザーが指定されたアクションを実行した場合にコンバージョンがカウントされる最大30日間のウィンドウを設定するオプションがあります。

{% endtab %}

{% tab キャンバス %}

まだ完了していない場合は、キャンバスコンポーネントの残りのセクションを完了してください。キャンバスの残りの部分の構築方法、[多変量テスト]({{site.baseurl}}/user_guide/messaging/ab_testing)や[インテリジェントセレクション]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection)の実装などの詳細については、キャンバスドキュメントの[キャンバスを構築する]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas)ステップを参照してください。

{% endtab %}
{% endtabs %}

## ステップ6: 確認とデプロイ {#step-6-review-and-deploy}

キャンペーンまたはキャンバスの構築が完了したら、詳細を確認し、[テスト]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages)を行ってから送信します。詳細については、[テストメッセージの送信]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=content%20card)を参照してください。

{% alert warning %}
Content Cardsは起動後に編集できません。新しいユーザーへの送信を停止したり、ユーザーのフィードから削除したりすることのみ可能です。このシナリオへの対処方法については、[送信済みカードの更新]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#updating-launched-cards)を参照してください。
{% endalert %}

次に、[Content Cardsレポート]({{site.baseurl}}/user_guide/channels/content_cards/reporting)を確認して、Content Cardsキャンペーンの結果にアクセスする方法を学びましょう。

## 知っておくべきこと {#things-to-know}

### ペイロードとフィードの制限 {#payload-and-feed-limitations}

パフォーマンスをサポートするために、Content Cardsには2つの主要な制約があります。各カードのペイロードサイズの制限と、フィードに表示できるカードの最大数です。

#### Content Cardsのサイズ制限 {#size-limitations-for-content-cards}

単一のContent Cardsのデータペイロード全体は、Liquidパーソナライゼーションがレンダリングされた**後**で2 KBを超えることはできません。これには以下が含まれます。

* タイトル
* メッセージ
* 画像URL（画像ファイルサイズではなく、URL文字列自体の長さ）
* リンクテキスト
* 指定されたすべてのプラットフォームのリンクURL（iOS、Android、Web用の個別のURLはすべて合計にカウントされます）
* キーと値のペア（キー名とその値の両方）

Liquidを使用して長いテキスト文字列（カスタム属性からなど）を取得すると、制限を超える可能性があります。

キャンペーンコンポーザーは、静的コンテンツが制限を超えた場合に警告を表示します。Liquidを使用したダイナミックコンテンツのサイズは予測されません。メッセージサイズが2 KBを超えた場合、送信時に中止されます。これらの中止は、メッセージアクティビティログで理由 `Content card maximum size exceeded` として確認できます。

{% alert important %}
テスト送信中は、2 KBを超えるContent Cardsでも正常に配信および表示される場合があります。
{% endalert %}

Content Cardsのペイロードサイズを管理するためのベストプラクティスを以下に示します。

* 長いリンクにはURL短縮サービスを使用してください。URL、特に広範なトラッキングパラメーターを含むURLは、サイズ制限の問題が発生する可能性があります。URL短縮サービスを使用すると、文字数を大幅に削減し、ペイロードのスペースを確保できます。
* Liquidでダイナミックコンテンツを切り詰めてください。ユーザー属性やAPI呼び出しからのダイナミックテキストでカードをパーソナライズする場合、コンテンツの長さは予測できない場合があります。`truncate` などのLiquidフィルターを積極的に使用して、ダイナミックテキストの長さを制限してください。
* マルチプラットフォームURLを効率的に使用してください。2 KBの制限には、定義するすべてのプラットフォームのURLが含まれます。各プラットフォームに長い固有のURLを使用すると、ペイロードのサイズが倍増する可能性があります。可能であれば、すべてのプラットフォームで機能する単一のリンクを使用するか、必要に応じてURL短縮サービスを使用してください。
* よりリッチなコンテンツにはバナーを検討してください。大量のコンテンツを常に必要とするユースケースでは、Content Cardsは適切なチャネルではない場合があります。バナーには同じ2 KBのペイロード制限がなく、アプリやWebサイトのエクスペリエンスにリッチなコンテンツを直接埋め込むのに適しています。

#### フィード内のカード数 {#number-of-cards-in-feed}

各ユーザーは、任意の時点でフィードに最大250枚の有効期限内のContent Cardsを持つことができます。この制限を超えると、Brazeは未読であっても最も古いカードを返さなくなります。却下されたカードもこの制限にカウントされるため、却下されたカードが多いと、古いカードに利用できるスペースが減少します。

カード制限に関する問題を防ぐために、以下のベストプラクティスをお勧めします。

- **短い有効期限を使用する：** 時間に敏感なキャンペーン（週末セールなど）には、特定の有効期限を設定してください。これにより、カードはフィードから自動的に削除され、関連性がなくなった後は制限にカウントされなくなります。
- **アクションベースの削除を活用する：** トランザクションまたは目標ベースのカードに削除イベントを設定してください。たとえば、ユーザーにプロフィールの完成を促すカードは、`profile_completed` イベントが記録されたらすぐに削除する必要があります。
- **長期実行キャンペーンを監査する：** 繰り返しまたは継続中のキャンペーンを確認して、時間の経過とともにフィードにカードが多すぎてユーザーのエクスペリエンスが低下していないことを確認してください。

### Content Cardsの再適格性を理解する {#understanding-re-eligibility-for-content-cards}

再適格性は、ユーザーが同じキャンペーンからメッセージを複数回受信できるかどうか、またいつ受信できるかを決定します。Content Cardsの場合、この仕組みを理解することは、繰り返しキャンペーンを管理し、ユーザーが重複したメッセージや古いメッセージを受信しないようにするために重要です。

{% alert tip %}
コンテンツを30日以上持続させたいですか？[バナー]({{site.baseurl}}/user_guide/channels/banners)をお試しください。
{% endalert %}

#### 再適格性の計算方法 {#how-re-eligibility-is-calculated}

再適格性をオンにすると、ユーザーがキャンペーンに「再エントリ」できるまでのカウントダウンは、メッセージが送信された後に開始されます。このカウントダウンが開始される具体的なタイミングは、カード作成設定によって異なります。

- [初回インプレッション時]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation#differences)を使用するContent Cardsは、インプレッション時間を使用して再適格性を計算します。
- キャンペーン起動時、マルチチャネルキャンペーン、またはキャンバスステップエントリ時に作成されたContent Cardsは、送信時間またはインプレッション時間のいずれか遅い方を使用します。

#### 30日間の有効期限と再適格性 {#the-30-day-expiration-and-re-eligibility}

混乱の一般的な原因は、キャンペーンの再適格性とすべてのContent Cardsの自動30日間有効期限の相互作用です。

すべてのContent Cardsは、送信または削除されてから30日後にBrazeのシステムから自動的にパージされます。再適格性が**オフ**になっている長期実行の繰り返しキャンペーンがある場合、ユーザーは30日後に同じカードを再度受信する可能性があります。元のカードがパージされると、システムはそのユーザーがキャンペーンを受信した記録を認識しなくなり、次のセッションで再び適格になります。

ユーザーが特定のキャンペーンからメッセージを1回だけ受信するようにするには、このキャンペーンからメッセージを受信していないユーザー向けのオーディエンスフィルターをキャンペーンまたはキャンバスステップに追加してください。このフィルターは、長期実行キャンペーンからの重複送信を防ぐ最も信頼性の高い方法です。

### ライブContent Cardsの管理 {#managing-live-content-cards}

Content Cardsが送信された後、ユーザーに配信される準備ができた「受信トレイ」で待機します（メールで起こることと同様です）。コンテンツがContent Cardsに取り込まれた後（表示時）、その有効期間中に変更することはできません。これは、Connected Contentを通じてAPIを呼び出し、エンドポイントからのデータが変更された場合でも適用されます。このデータは更新されません。新しいユーザーへの送信を停止し、ユーザーのフィードから削除することのみが可能です。キャンペーンを変更した場合、変更後に送信されたカードのみが更新を含みます。

#### 起動済みカードの更新 {#updating-launched-cards}

すでにカードを受信したユーザーのカードを変更するには、以下のいずれかの方法を使用する必要があります。

##### オプション1：キャンペーンを複製する（即時変更に推奨） {#option-1-duplicate-the-campaign-recommended-for-immediate-changes}

{% alert tip %}
カードに最新のコンテンツを表示する場合、変更をすぐに反映する必要がある場合、または再適格性がオフになっている場合に、このオプションをお勧めします。
{% endalert %}

最初のアプローチは、キャンペーンをアーカイブし、新しい複製キャンペーンを起動することです。

1. 元のキャンペーンを停止し、プロンプトが表示されたら `Remove card after the next sync` を選択します。
2. キャンペーンを複製し、編集を行い、新しいバージョンを起動します。

キャンペーンを複製する場合、新しいバージョンのオーディエンスを定義する必要があります。セグメンテーションフィルターを使用して、更新されたカードを受信するユーザーを制御します。
* ユーザーがContent Cardsに再適格になるべきでない場合、フィルター `Received Message from キャンペーン` を条件 `Has Not` に設定して、以前のバージョンのContent Cardsを受信していないユーザーをフィルタリングできます。
* 以前のカードを受信したユーザーがX日後に再適格になるべき場合、`Last Received Message from specific campaign` をX日以上前に設定するか、**または** `Received Message from キャンペーン` を `Has Not` 条件で設定できます。

###### 影響 {#impact}

- **既存の受信者：** 新規および既存の受信者は、適格であれば次のフィード更新時に更新されたカードを確認できます。
- **レポート：** カードの各バージョンには個別の分析があります。

たとえば、セッション開始でトリガーされるキャンペーンを設定し、再適格性を30日に設定したとします。ユーザーが2日前にキャンペーンを受信し、コピーを変更したいとします。まず、キャンペーンをアーカイブし、フィードからカードを削除します。次に、キャンペーンを複製し、新しいコピーで再起動します。ユーザーが別のセッションを開始すると、すぐに新しいカードを受信します。

##### オプション2：同じキャンペーンを停止して再起動する {#option-2-stop-and-relaunch-the-same-campaign}

{% alert tip %}
通知センターやメッセージ受信トレイ内のユニークなメッセージ（プロモーションなど）、分析を統一することが重要な場合、またはメッセージの適時性が問題にならない場合（既存の受信者が更新されたカードを確認するまで適格性ウィンドウを待つことができる場合など）に、このオプションの使用をお勧めします。
{% endalert %}

このアプローチでは、すべての分析が単一のキャンペーンに統一されます。新たに適格になったユーザーは新しいカードを受信しますが、既存の受信者への更新は再適格になるまで遅延します。

1. キャンペーンを停止し、プロンプトが表示されたら**次回の同期後にカードを削除**を選択します。
2. 必要に応じてキャンペーンを編集します。
3. キャンペーンを再開します。

###### 影響

* **既存の受信者：** すでにカードを受信したユーザーは、再適格になるまで更新されたカードを受信しません。再適格性がオフになっている場合、新しいカードを受信することはありません。
* **レポート：** 1つのキャンペーンに、起動されたカードバージョンのすべてのレポート分析が含まれます。Brazeは起動されたバージョン間を区別しません。

たとえば、セッション開始でトリガーされ、再適格性が30日に設定されたキャンペーンがあるとします。ユーザーが2日前にキャンペーンを受信し、コピーを変更したいとします。まず、キャンペーンを停止し、フィードからカードを削除します。次に、新しいコピーでキャンペーンを再公開します。ユーザーが別のセッションを開始すると、28日後に新しいカードを受信します。

{% alert note %}
キャンペーンを停止し、削除イベント設定を編集し、フィードからカードを削除せずにキャンペーンを再開した場合、ユーザーのフィードにある既存のカードは更新された削除イベント設定を使用します。カードは最初に送信されたときの元の削除イベント設定を保持しません。
{% endalert %}

#### カードの削除と有効期限 {#removing-and-expiring-cards}

##### 手動によるカードの削除 {#manual-card-removal}

キャンペーンを停止することで、いつでもすべてのユーザーのフィードからカードを手動で削除できます。

1. Content Cardsのキャンペーンを開き、キャンペーンを停止を選択します。
2. プロンプトが表示されたら、**次回の同期後にカードを削除**を選択します。カードは次のフィード更新時に削除されます。

##### 自動カード削除 {#action-based-card-removal}

購入の完了や機能の有効化など、ユーザーが特定のアクションを実行したときにカードを自動的に削除できます。

キャンペーンまたはキャンバスステップで、削除イベントを指定します。ユーザーがそのイベントを実行すると、Brazeがイベントを処理した後の次のフィード更新時にカードがフィードから削除されます。

{% alert note %}
この削除は即時ではありません。処理の遅延があるため、カードが消えるまでに数分かかり、複数回のフィード更新が必要になる場合があります。
{% endalert %}

{% alert tip %}
ユーザーのフィードからカードを削除するべき複数のカスタムイベントと購入を指定できます。これらのアクションのいずれかがユーザーによって実行されると、キャンペーンのカードによって送信された既存のカードが削除されます。適格なカードは、メッセージのスケジュールに従って引き続き送信されます。
{% endalert %}

![Content Cardsの削除イベントオプションを含むContent Cards削除条件パネル。]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

##### カードの有効期限 {#card-expiration}

Content Cardsは送信されてから最大30日間利用可能です。30日後、Brazeはユーザーフィードからカードを削除し、Brazeのシステムからパージします。

#### カードを30日以上持続させる {#making-cards-last-longer-than-30-days}

{% alert tip %}
30日間のContent Cards制限よりも長くメッセージを持続させる必要があるユースケースには、バナーの使用を検討してください。バナーは永続性を考慮して設計されており、必須の有効期限がないため、必要な限り表示し続けることができます。
{% endalert %}

カードが常に利用可能であるように見せたい場合、30日ごとにカードを効果的に置き換える繰り返しキャンペーンを作成できます。

1. Content Cardsの有効期間を30日に設定します。
2. キャンペーンの再適格性を30日に設定します。
3. キャンペーンを「セッション開始」でトリガーするように設定します。

### Content Cardsの同期と更新 {#content-card-sync-and-refresh}

Content Cardsはスケジュールに従って、またアプリがフィードを更新するときに同期されます。同期動作はフル同期と部分同期で異なり、SDKの統合はセッション開始時にカードが更新されるタイミングに影響します。実装の詳細については、[Content Cardsフィードのカスタマイズ]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed)および[Content Cardsの作成]({{site.baseurl}}/developer_guide/content_cards/creating_cards)を参照してください。

### Content Cardsキャンペーンの停止の影響 {#impact-of-stopping-content-cards-campaigns}

キャンペーンを停止して**次回の同期後にカードを削除**を選択すると、Brazeは次のフィード更新時にユーザーフィードからカードを削除します。ユーザーが閲覧する前に削除されたカードにはインプレッションが記録されないため、インプレッション数は送信数よりも少なくなる場合があります。

## トラブルシューティング {#troubleshooting}

### トリガーイベント後にContent Cardsがすぐに表示されないのはなぜですか？ {#why-dont-content-cards-appear-immediately-after-a-trigger-event}

アクションベースの配信キャンペーン（セッション開始など）では、トリガーイベントからカードが利用可能になるまでに短い遅延が発生することが想定されています。この遅延は以下の理由で発生します。

- トリガーイベントがBrazeのサーバーにフラッシュされる
- キャンペーンがトリガーされ、ユーザーの適格性が記録される
- そのユーザーのContent Cardsがデータベースに作成される
- SDKが同期し、利用可能なすべてのカードをデバイスに取得する

SDKの同期がユーザーの適格性の記録前に行われた場合、ユーザーはカードを受信しません。

初回セッション中の新規ユーザーの場合、この遅延は避けられません。即時利用が必要な既存ユーザーの場合は、代わりにスケジュール配信の使用を検討してください。

新規ユーザーと既存ユーザーの両方で遅延を最小限に抑える必要がある場合は、2つのキャンペーンを作成できます。

- **セッション数が0より大きい既存ユーザー：** スケジュール配信キャンペーンを使用します。カードは事前に作成され、すぐに利用可能です。
- **セッション数が0の新規ユーザー：** アクショントリガーキャンペーンを使用します。カードは最初のセッショントリガー後に作成されます。

このアプローチにより、既存ユーザーはカードを即座に確認でき、新規ユーザーにも初回セッションでの短い遅延の後にリーチできます。レイテンシーを改善するための追加の戦略については、[Content Cardsの低レイテンシー要件の改善]({{site.baseurl}}/user_guide/channels/content_cards/best_practices/improving_low_latency_requirements)を参照してください。