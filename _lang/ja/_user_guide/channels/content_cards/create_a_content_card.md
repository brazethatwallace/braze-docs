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

## ステップ1:メッセージの作成場所を選択する {#step-1-choose-where-to-build-your-message}

キャンペーンは、シンプルな単一メッセージング（1つのメッセージで製品についてユーザーに通知するなど）に使用します。キャンバスは、複数ステップのユーザージャーニー（時間の経過に伴うユーザーの行動に基づいてカスタマイズされた製品提案を送信するなど）に使用します。

{% tabs %}
{% tab キャンペーン %}

1. **メッセージング** > **キャンペーン**に移動し、**キャンペーンを作成**を選択します。
2. **Content Cards**を選択するか、複数のチャネルをターゲットとするキャンペーンの場合は**マルチチャネル**を選択します。
3. キャンペーンにわかりやすく意味のある名前を付けます。
4. 必要に応じて[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)と[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)を追加します。
   * タグを使用すると、キャンペーンを見つけやすくなり、レポートを作成しやすくなります。たとえば、[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reports/report_builder)を使用する場合、関連するタグでフィルタリングできます。
5. キャンペーンに必要な数のバリアントを追加して名前を付けます。追加したバリアントごとに、異なるプラットフォーム、メッセージタイプ、レイアウトを選択できます。バリアントの詳細については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似している、または同じコンテンツを持つ場合は、追加のバリアントを追加する前にメッセージを作成してください。その後、**バリアントを追加**ドロップダウンから**バリアントからコピー**を選択できます。
{% endalert %}

{% endtab %}
{% tab キャンバス %}

1. キャンバスコンポーザーを使用して[キャンバスを作成]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)します。
2. キャンバスの設定後、キャンバスビルダーでメッセージステップを追加します。ステップにわかりやすく意味のある名前を付けます。
3. メッセージングチャネルとして**Content Cards**を選択します。
4. BrazeがContent Cardsのオーディエンス適格性とパーソナライゼーションを計算するタイミングを選択します。これは、ステップエントリ時またはファーストインプレッション時（推奨）に設定できます。Content Cardsを含むステップは、スケジュール配信またはアクションベースで設定できます。
5. ユーザーが購入を完了した場合やカスタムイベントを実行した場合にContent Cardsを削除するかどうかを選択します。
6. Content Cardsの有効期限（フィード内の表示期間）を設定します。一定期間後または特定の時刻に設定できます。
7. **配信設定**で、必要に応じてこのステップのオーディエンス（受信者）をフィルタリングします。セグメントを指定し、追加のフィルターを追加することで、オーディエンスをさらに絞り込むことができます。オーディエンスオプションは、遅延後のメッセージ送信時にチェックされます。
8. メッセージと組み合わせたい他のメッセージングチャネルを選択します。

{% endtab %}
{% endtabs %}

## ステップ2:メッセージタイプを指定する {#step-2-specify-your-message-types}

3つの基本的なContent Cardsタイプから1つを選択します：**クラシック**、**キャプション付き画像**、**画像のみ**。

各タイプの想定される動作と外観の詳細については、[クリエイティブの詳細]({{site.baseurl}}/user_guide/channels/content_cards/creative_details)を参照するか、以下の表のリンクを確認してください。これらのContent Cardsタイプは、モバイルアプリとWebアプリケーションの両方で使用できます。

| メッセージタイプ | 例 | 説明 |
|---|---|---|
|[クラシック]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types)| ![ワークアウトクラスの予約を促す小さなアイコンとテキストを含むクラシックContent Card。]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) |クラシックカードは、太字のタイトル、メッセージテキスト、およびタイトルとテキストの先頭に配置されるオプションの画像を含むシンプルなレイアウトです。クラシックカードには正方形の画像またはアイコンを使用するのが最適です。|
|[キャプション付き画像]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types)| ![ウェイトリフターの画像とワークアウトクラスの予約を促すテキストを含むキャプション付きContent Card。]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | キャプション付き画像カードは、コピーと目を引く画像でコンテンツを紹介します。|
|[画像のみ]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types)| ![テキストのみの画像のみContent Card。]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | 画像のみカードは、画像、GIF、その他のクリエイティブなテキスト以外のコンテンツ用のスペースで注目を集めます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ2:メッセージタイプを指定する" }

## ステップ3:Content Cardsを作成する {#step-3-compose-a-content-card}

メッセージエディターの**作成**タブで、メッセージのコンテンツと動作のすべての側面を編集できます。

![メッセージエディターの作成タブにあるサンプルContent Cardsの詳細。]({% image_buster /assets/img/content_card_compose.png %})

ここに表示されるコンテンツは、前のステップで選択した**カードタイプ**によって異なりますが、以下のオプションのいずれかが含まれる場合があります。

### 言語 {#language}

**言語を追加**を選択して、提供されたリストから希望の言語を追加します。これにより、メッセージに[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic)が挿入されます。コンテンツを作成する前に言語を選択して、Liquid内の適切な場所にテキストを入力できるようにすることをお勧めします。使用可能な言語の完全なリストについては、[サポートされている言語]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization#languages-supported)を参照してください。

![言語として英語、スペイン語、フランス語が選択され、国際化するフィールドとしてタイトル、説明、リンクテキストが選択されたウィンドウ。]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

#### 右から左に読むメッセージの作成 {#create-right-to-left-messages}

右から左に読むメッセージの最終的な表示は、サービスプロバイダーのレンダリング方法に大きく依存します。できるだけ正確に表示される右から左に読むメッセージを作成するためのベストプラクティスについては、[右から左に読むメッセージの作成]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)を参照してください。

#### タイトルとメッセージ {#title-and-message}

好きな内容を記述できます。制限はありませんが、メッセージを素早く伝えてユーザーにクリックしてもらえるほど効果的です。明確で簡潔なタイトルとメッセージコンテンツをお勧めします。これらのフィールドは画像のみカードには提供されません。

#### 画像 {#image}

Content Cardsに画像を追加するには、**画像を追加**を選択するか、画像URLを入力します。**画像を追加**を選択すると**メディアライブラリ**が開き、以前にアップロードした画像を選択するか、新しい画像を追加できます。

メッセージタイプとプラットフォームごとに推奨される比率と要件が異なる場合があるため、画像を発注または作成する前に必ず確認してください。Content Cardsのメッセージフィールドは合計サイズが2&nbsp;KBに制限されていることに注意してください。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### トップに固定 {#pin-to-top}

Brazeは固定されたカードをユーザーのフィードの上部に表示し、ユーザーはそれを閉じることができません。ユーザーのフィードに複数の固定カードがある場合、Brazeは時系列順に並べます。BrazeがContent Cardsを配信する際、カードは固定または非固定のいずれかであり、そのステータスはカードの有効期間中変更されません。キャンペーンの固定設定を変更した場合、更新は将来送信されるカードにのみ適用されます。すでにユーザーのフィードにあるカードの固定ステータスは変更されません。

![モバイルとWebのBraze Content Cardsプレビューの並列表示。「このカードをフィードのトップに固定する」オプションが選択されています。]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### クリック時の動作 {#on-click-behavior}

ユーザーがカード内の表示されたリンクをクリックすると、リンクはアプリ内のより深い場所または別のサイトに誘導できます。Content Cardsのクリック時の動作を選択する場合は、それに応じて**リンクテキスト**を更新することを忘れないでください。

Content Cardsのリンクで使用できるアクションは以下のとおりです。

| アクション | 説明 |
|---|---|
| Web URLにリダイレクト | ネイティブでないWebページを開きます。|
| [アプリへのディープリンク]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content) | アプリ内の既存の画面にディープリンクします。|
| カスタムイベントをログに記録 | トリガーする[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)を選択します。別のContent Cardsの表示や追加のメッセージングのトリガーに使用できます。|
| カスタム属性をログに記録 | 現在のユーザーに設定する[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)を選択します。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="クリック時の動作" }

**カスタムイベントをログに記録**と**カスタム属性をログに記録**オプションには、以下のSDKバージョンの互換性が必要です。

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## ステップ4:追加設定を構成する（オプション） {#step-4-configure-additional-settings-optional}

[キーと値のペア]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs)を使用して、カードのカテゴリを作成したり、[複数のContent Cardsフィード]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed#multiple-feeds)を作成したり、カードのソート方法をカスタマイズしたりできます。

メッセージにキーと値のペアを追加するには、**設定**タブに移動して**新しいペアを追加**を選択します。

## ステップ5:キャンペーンまたはキャンバスの残りの部分を構築する {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab キャンペーン %}

キャンペーンの残りの部分を構築します。Content Cardsを構築するためのツールの最適な使用方法の詳細については、次のセクションに進んでください。

### 配信スケジュールまたはトリガーを選択する {#choose-a-delivery-schedule-or-trigger}

Content Cardsは、スケジュールされた時刻、アクション、またはAPIトリガーに基づいて配信できます。詳細については、[キャンペーンのスケジュール設定]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)を参照してください。

キャンペーンの期間と[サイレント時間]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)を設定し、Content Cardsの有効期限を決定することもできます。特定の有効期限日またはカードの有効期限が切れるまでの日数（最大30日）を設定します。すべてのバリアントの有効期限は同一です。

有効期限のカウントダウンはカードの送信時刻から開始されます。

- **スケジュールされたキャンペーン：**カウントダウンはスケジュールされた起動時刻に開始されます。
- **アクションベースのキャンペーン：**カウントダウンはユーザーがトリガーアクションを実行した時点で開始されます。

たとえば、アクションベースのContent Cardsが本日午後2時に送信され、有効期限が1日の場合、翌日の午後2時に有効期限が切れます。

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

アクションベースの配信では、Content Cardsが表示されるまでに短い遅延が予想されます。たとえば、キャンペーンがセッション開始時にトリガーされる場合、このトリガーイベントはまずBrazeのサーバーにフラッシュされる必要があります。次に、キャンペーンに対するユーザーの適格性が記録されます。SDKが同期すると、カードが作成され、同じ同期レスポンスで返されます。ユーザーの適格性が記録される前にSDK同期が行われた場合、ユーザーはカードを受信しません。初回セッションのユーザーの場合、この遅延は避けられません。既存のユーザーで即時の利用可能性が必要な場合は、代わりにスケジュール配信の使用を検討してください。

#### スケジュール配信 {#scheduled-delivery}

スケジュール配信のContent Cardsキャンペーンでは、カードが作成されるタイミングを指定することで、Brazeが新しいContent Cardsキャンペーンのオーディエンス適格性とパーソナライゼーションを評価するタイミングを選択できます。詳細については、[カード作成]({{site.baseurl}}/card_creation)を参照してください。

#### ターゲットユーザーを選択する {#choose-users-to-target}

次に、セグメントまたはフィルターを選択してオーディエンスを絞り込み、[ユーザーをターゲット]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)にします。おおよそのセグメント人口のプレビューが自動的に表示されます。正確なセグメントメンバーシップは、メッセージが送信される前に常に計算されることに注意してください。

{% multi_lang_include audience/target_audiences.md %}

#### コンバージョンイベントを選択する {#choose-conversion-events}

Brazeでは、キャンペーンを受信した後にユーザーが特定のアクション（[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)）を実行する頻度を追跡できます。ユーザーが指定されたアクションを実行した場合にコンバージョンがカウントされる最大30日間の時間枠を設定するオプションがあります。

{% endtab %}

{% tab キャンバス %}

まだ完了していない場合は、キャンバスコンポーネントの残りのセクションを完了してください。キャンバスの残りの部分の構築方法、[多変量テスト]({{site.baseurl}}/user_guide/messaging/ab_testing)や[インテリジェントセレクション]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection)の実装方法などの詳細については、キャンバスドキュメントの[キャンバスの構築]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas)ステップを参照してください。

{% endtab %}
{% endtabs %}

## ステップ6:確認してデプロイする {#step-6-review-and-deploy}

キャンペーンまたはキャンバスの最後の構築が完了したら、詳細を確認し、[テスト]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages)を行い、準備ができたら送信します。詳細については、[テストメッセージの送信]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=content%20card)を参照してください。

{% alert warning %}
Content Cardsは起動後に編集できません。新しいユーザーへの送信を停止し、ユーザーのフィードから削除することのみ可能です。このシナリオへの対処方法については、[起動済みカードの更新]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#updating-launched-cards)を参照してください。
{% endalert %}

次に、[Content Cardsレポート]({{site.baseurl}}/user_guide/channels/content_cards/reporting)を確認して、Content Cardsキャンペーンの結果にアクセスする方法を学びましょう。

## 知っておくべきこと {#things-to-know}

### ペイロードとフィードの制限 {#payload-and-feed-limitations}

パフォーマンスをサポートするために、Content Cardsには2つの主要な制約があります：各カードのペイロードサイズの制限と、フィードに表示できるカードの最大数です。

#### Content Cardsのサイズ制限 {#size-limitations-for-content-cards}

単一のContent Cardsのデータペイロード全体は、Liquidパーソナライゼーションがレンダリングされた**後**で2 KBを超えることはできません。これには以下が含まれます：

* タイトル
* メッセージ
* 画像URL（URL文字列自体の長さであり、画像ファイルサイズではありません）
* リンクテキスト
* 指定されたすべてのプラットフォームのリンクURL（iOS、Android、Webの個別のURLはすべて合計にカウントされます）
* キーと値のペア（キー名とその値の両方）

Liquidを使用して長いテキスト文字列（カスタム属性からなど）を取得すると、制限を超える可能性があります。

キャンペーンコンポーザーは、静的コンテンツが制限を超えた場合に警告を表示します。Liquidを使用した動的コンテンツのサイズは予測しません。メッセージサイズが2 KBを超えた場合、送信時に中止されます。これらの中止は、メッセージアクティビティログで理由`Content card maximum size exceeded`として確認できます。

{% alert important %}
テスト送信時には、2 KBを超えるContent Cardsでも配信および正常に表示される場合があります。
{% endalert %}

Content Cardsのペイロードサイズを管理するためのベストプラクティスは以下のとおりです：

* 長いリンクにはURL短縮サービスを使用します。URL、特に広範なトラッキングパラメーターを含むものは、サイズ制限の問題が発生する可能性があります。URL短縮サービスを使用すると、文字数を大幅に削減し、ペイロード内のスペースを確保できます。
* Liquidで動的コンテンツを切り詰めます。ユーザー属性やAPI呼び出しからの動的テキストでカードをパーソナライズする場合、コンテンツの長さが予測できないことがあります。`truncate`などのLiquidフィルターを積極的に使用して、動的テキストの長さに上限を設定してください。
* マルチプラットフォームURLを効率的に使用します。2 KBの制限には、定義したすべてのプラットフォームのURLが含まれます。各プラットフォームに長くユニークなURLを使用すると、ペイロードのサイズが倍増する可能性があります。可能であれば、すべてのプラットフォームで機能する単一のリンクを使用するか、必要に応じてURL短縮サービスを使用してください。
* よりリッチなコンテンツにはバナーを検討します。大量のコンテンツを常に必要とするユースケースでは、Content Cardsが適切なチャネルではない場合があります。バナーには同じ2 KBのペイロード制限がなく、アプリやWebサイトのエクスペリエンスにリッチなコンテンツを直接埋め込むのに適しています。

#### フィード内のカード数 {#number-of-cards-in-feed}

各ユーザーは、フィード内に最大250枚の有効期限内のContent Cardsを同時に保持できます。この制限を超えると、Brazeは未読であっても最も古いカードを返さなくなります。閉じたカードもこの制限にカウントされるため、閉じたカードが多いと古いカード用のスペースが減少する可能性があります。

カード制限に関する問題を防ぐために、以下のベストプラクティスをお勧めします：

- **短い有効期限を使用する：**時間に敏感なキャンペーン（週末セールなど）の場合、特定の有効期限日を設定します。これにより、カードはフィードから自動的に削除され、関連性がなくなった後は制限にカウントされません。
- **アクションベースの削除を活用する：**トランザクションまたは目標ベースのカードに削除イベントを設定します。たとえば、ユーザーにプロファイルの完成を促すカードは、`profile_completed`イベントがログに記録されたらすぐに削除する必要があります。
- **長期実行キャンペーンを監査する：**定期的または継続的なキャンペーンを確認して、時間の経過とともにフィードに多すぎるカードが蓄積され、ユーザーに悪い体験を与えていないことを確認します。

### Content Cardsの再適格性について {#understanding-re-eligibility-for-content-cards}

再適格性は、ユーザーが同じキャンペーンからメッセージを複数回受信できるかどうか、またいつ受信できるかを決定します。Content Cardsの場合、この仕組みを理解することは、定期的なキャンペーンを管理し、ユーザーが重複したメッセージや古いメッセージを受信しないようにするために重要です。

{% alert tip %}
コンテンツを30日以上持続させたい場合は、[バナー]({{site.baseurl}}/user_guide/channels/banners)をお試しください。
{% endalert %}

#### 再適格性の計算方法 {#how-re-eligibility-is-calculated}

再適格性を有効にすると、ユーザーがキャンペーンに「再エントリ」できるまでのカウントダウンは、メッセージが送信された後に開始されます。このカウントダウンが開始される具体的なタイミングは、カード作成の設定によって異なります：

- [ファーストインプレッション時]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation#differences)を使用するContent Cardsは、インプレッション時刻を使用して再適格性を計算します。
- キャンペーン起動時、マルチチャネルキャンペーン、またはキャンバスステップエントリ時に作成されたContent Cardsは、送信時刻またはインプレッション時刻のいずれか遅い方を使用します。

#### 30日間の有効期限と再適格性 {#the-30-day-expiration-and-re-eligibility}

よくある混乱の原因は、キャンペーンの再適格性とすべてのContent Cardsの自動30日間有効期限の相互作用です。

すべてのContent Cardsは、送信または削除されてから30日後にBrazeのシステムから自動的にパージされます。再適格性を**オフ**にした長期実行の定期キャンペーンがある場合、ユーザーは30日後に同じカードを再度受信する可能性があります。元のカードがパージされると、システムはそのユーザーがキャンペーンを受信した記録を認識しなくなり、次のセッションで再び適格になります。

ユーザーが特定のキャンペーンからメッセージを1回だけ受信するようにするには、キャンペーンまたはキャンバスステップに、このキャンペーンからメッセージを受信していないユーザー向けのオーディエンスフィルターを追加してください。このフィルターは、長期実行キャンペーンからの重複送信を防ぐ最も信頼性の高い方法です。

### ライブContent Cardsの管理 {#managing-live-content-cards}

Content Cardsが送信された後、ユーザーに配信される準備ができた「受信トレイ」で待機します（メールの場合と同様）。コンテンツがContent Cardsに取り込まれた後（表示時）、その有効期間中は変更できません。これは、Connected Contentを通じてAPIを呼び出し、エンドポイントからのデータが変更された場合でも適用されます。このデータは更新されません。新しいユーザーへの送信を停止し、ユーザーのフィードから削除することのみ可能です。キャンペーンを変更した場合、送信される将来のカードのみが更新されます。

#### 起動済みカードの更新 {#updating-launched-cards}

すでにカードを受信したユーザーのカードを変更するには、以下のいずれかの方法を使用する必要があります：

##### オプション1:キャンペーンを複製する（即時変更に推奨） {#option-1-duplicate-the-campaign-recommended-for-immediate-changes}

{% alert tip %}
カードに最新のコンテンツを表示する場合、変更をすぐに反映する必要がある場合、または再適格性がオフの場合に、このオプションをお勧めします。
{% endalert %}

最初のアプローチは、キャンペーンをアーカイブし、新しい複製キャンペーンを起動することです：

1. 元のキャンペーンを停止し、プロンプトが表示されたら`Remove card after the next sync`を選択します。
2. キャンペーンを複製し、編集を行い、新しいバージョンを起動します。

キャンペーンを複製する場合、新しいバージョンのオーディエンスを定義する必要があります。セグメンテーションフィルターを使用して、更新されたカードを受信するユーザーを制御します：
* ユーザーがContent Cardsに再適格になるべきでない場合、`Received Message from キャンペーン`フィルターの条件を`Has Not`に設定して、以前のバージョンのContent Cardsを受信していないユーザーをフィルタリングできます。
* 以前のカードを受信したユーザーがX日後に再適格になるべき場合、`Last Received Message from specific campaign`フィルターをX日以上前に設定するか、**または**`Received Message from キャンペーン`フィルターの条件を`Has Not`に設定できます。

###### 影響 {#impact}

- **既存の受信者：**新規および既存の受信者は、適格であれば次のフィード更新時に更新されたカードを確認できます。
- **レポート：**カードの各バージョンには個別の分析があります。

たとえば、セッション開始時にトリガーされるキャンペーンを設定し、再適格性を30日に設定したとします。ユーザーが2日前にキャンペーンを受信し、コピーを変更したいとします。まず、キャンペーンをアーカイブしてフィードからカードを削除します。次に、キャンペーンを複製し、新しいコピーで再起動します。ユーザーが別のセッションを開始すると、すぐに新しいカードを受信します。

##### オプション2:同じキャンペーンを停止して再起動する {#option-2-stop-and-relaunch-the-same-campaign}

{% alert tip %}
通知センターやメッセージ受信トレイ内のユニークなメッセージ（プロモーションなど）、分析を統一することが重要な場合、またはメッセージの即時性が問題にならない場合（既存の受信者が適格性の時間枠まで待ってから更新されたカードを確認できる場合など）に、このオプションをお勧めします。
{% endalert %}

このアプローチでは、すべての分析が単一のキャンペーンに統一されます。新たに適格になったユーザーは新しいカードを受信しますが、既存の受信者への更新は再適格になるまで遅延します：

1. キャンペーンを停止し、プロンプトが表示されたら**次の同期後にカードを削除**を選択します。
2. 必要に応じてキャンペーンを編集します。
3. キャンペーンを再開します。

###### 影響

- **既存の受信者：**すでにカードを受信したユーザーは、再適格になるまで更新されたカードを受信しません。再適格性がオフの場合、新しいカードを受信することはありません。
- **レポート：**1つのキャンペーンに、起動されたカードバージョンのすべてのレポート分析が含まれます。Brazeは起動されたバージョン間を区別しません。

たとえば、セッション開始時にトリガーされ、再適格性が30日に設定されたキャンペーンがあるとします。ユーザーが2日前にキャンペーンを受信し、コピーを変更したいとします。まず、キャンペーンを停止してフィードからカードを削除します。次に、新しいコピーでキャンペーンを再公開します。ユーザーが別のセッションを開始すると、28日後に新しいカードを受信します。

#### カードの削除と有効期限 {#removing-and-expiring-cards}

##### 手動によるカードの削除 {#manual-card-removal}

キャンペーンを停止することで、いつでもすべてのユーザーのフィードからカードを手動で削除できます。

1. Content Cardsキャンペーンを開き、**キャンペーンを停止**を選択します。
2. プロンプトが表示されたら、**次の同期後にカードを削除**を選択します。カードは次のフィード更新時に削除されます。

##### 自動カード削除 {#action-based-card-removal}

購入の完了や機能の有効化など、ユーザーが特定のアクションを実行したときにカードを自動的に削除できます。

キャンペーンまたはキャンバスステップで、削除イベントを指定します。ユーザーがそのイベントを実行すると、Brazeがイベントを処理した後の次のフィード更新時にカードがフィードから削除されます。

{% alert note %}
この削除は即時ではありません。処理の遅延があるため、カードが消えるまでに数分かかり、複数回のフィード更新が必要になる場合があります。
{% endalert %}

{% alert tip %}
ユーザーのフィードからカードを削除するべき複数のカスタムイベントと購入を指定できます。ユーザーがそれらのアクションの**いずれか**を実行すると、キャンペーンのカードによって送信された既存のカードが削除されます。将来の適格なカードは、メッセージのスケジュールに従って引き続き送信されます。
{% endalert %}

![Content Cards削除イベントオプションを含むContent Cards削除条件パネル。]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

##### カードの有効期限 {#card-expiration}

Content Cardsは、送信されてから最大30日間利用可能です。30日後、Brazeはユーザーのフィードからカードを削除し、Brazeのシステムからパージします。

#### カードを30日以上持続させる {#making-cards-last-longer-than-30-days}

{% alert tip %}
30日間のContent Cards制限よりも長くメッセージを持続させる必要があるユースケースでは、バナーの使用を検討してください。バナーは永続性を考慮して設計されており、必須の有効期限がないため、必要な限り表示し続けることができます。
{% endalert %}

カードが常に利用可能であるように見せたい場合は、30日ごとにカードを効果的に置き換える定期キャンペーンを作成できます：

1. Content Cardsの期間を30日に設定します。
2. キャンペーンの再適格性を30日に設定します。
3. キャンペーンを「セッション開始」時にトリガーするように設定します。

### Content Cardsの同期と更新 {#content-card-sync-and-refresh}

Content Cardsはスケジュールに基づいて同期され、アプリがフィードを更新するときにも同期されます。同期の動作はフル同期と部分同期で異なり、SDKの統合はセッション開始時にカードが更新されるタイミングに影響します。実装の詳細については、[Content Cardsフィードのカスタマイズ]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed)と[Content Cardsの作成]({{site.baseurl}}/developer_guide/content_cards/creating_cards)を参照してください。

### Content Cardsキャンペーンの停止による影響 {#impact-of-stopping-content-cards-campaigns}

キャンペーンを停止して**次の同期後にカードを削除**を選択すると、Brazeは次のフィード更新時にユーザーのフィードからカードを削除します。ユーザーが閲覧する前に削除されたカードにはインプレッションが記録されないため、インプレッション数が送信数よりも少なくなる場合があります。