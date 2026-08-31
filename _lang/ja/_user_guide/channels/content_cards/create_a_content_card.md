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

## ステップ1：メッセージの作成場所を選択する {#step-1-choose-where-to-build-your-message}

キャンペーンは、シンプルな単発メッセージに使用します（1つのメッセージで製品についてユーザーに知らせる場合など）。キャンバスは、複数ステップのユーザージャーニーに使用します（時間の経過に伴うユーザー行動に基づいてカスタマイズされた製品提案を送信する場合など）。

{% tabs %}
{% tab キャンペーン %}

1. **メッセージング** > **キャンペーン** に移動し、**キャンペーンを作成** を選択します。
2. **Content Cards** を選択するか、複数のチャネルを対象としたキャンペーンの場合は **マルチチャネル** を選択します。
3. キャンペーンにわかりやすく意味のある名前を付けます。
4. 必要に応じて[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)と[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)を追加します。
   * タグを使用すると、キャンペーンを見つけやすくなり、レポートを作成しやすくなります。たとえば、[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reports/report_builder)を使用する際に、関連するタグでフィルタリングできます。
5. キャンペーンに必要な数のバリアントを追加して名前を付けます。追加した各バリアントに対して、異なるプラットフォーム、メッセージタイプ、レイアウトを選択できます。バリアントの詳細については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似している場合や同じコンテンツの場合は、追加のバリアントを追加する前にメッセージを作成してください。次に、**バリアントを追加** ドロップダウンから **バリアントからコピー** を選択できます。
{% endalert %}

{% endtab %}
{% tab キャンバス %}

1. キャンバスコンポーザーを使用して[キャンバスを作成]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)します。
2. キャンバスの設定が完了したら、キャンバスビルダーでメッセージステップを追加します。ステップにわかりやすく意味のある名前を付けます。
3. メッセージングチャネルとして **Content Cards** を選択します。
4. BrazeがContent Cardsのオーディエンスの適格性とパーソナライゼーションを計算するタイミングを選択します。ステップエントリ時またはファーストインプレッション時（推奨）に設定できます。Content Cardsを含むステップは、スケジュール配信またはアクションベースで配信できます。
5. ユーザーが購入を完了したときやカスタムイベントを実行したときにContent Cardsを削除するかどうかを選択します。
6. Content Cardsの有効期限（フィード内の表示期間）を設定します。一定期間後または特定の時間に設定できます。
7. **配信設定** で、必要に応じてこのステップのオーディエンスまたは受信者をフィルタリングします。セグメントを指定し、追加のフィルターを設定することで、さらにオーディエンスを絞り込めます。オーディエンスのオプションは、ディレイの後、メッセージが送信される時点で確認されます。
8. メッセージと組み合わせたい他のメッセージングチャネルを選択します。

{% endtab %}
{% endtabs %}

## ステップ2: メッセージタイプを指定する {#step-2-specify-your-message-types}

3つの基本的なContent Cardsタイプのいずれかを選択します: **クラシック**、**キャプション付き画像**、**画像のみ**。

各タイプの想定される動作と外観の詳細については、[クリエイティブの詳細]({{site.baseurl}}/user_guide/channels/content_cards/creative_details)を参照するか、以下の表のリンクを確認してください。これらのContent Cardsタイプは、モバイルアプリとWebアプリケーションの両方で利用できます。

| メッセージタイプ | 例 | 説明 |
|---|---|---|
| [クラシック]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types) | ![小さなアイコンとワークアウトクラスの予約を促すテキストが表示されたクラシックContent Card。]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) | クラシックカードは、太字のタイトル、メッセージテキスト、およびタイトルとテキストの先頭に配置されるオプションの画像を備えたシンプルなレイアウトです。クラシックカードには正方形の画像やアイコンの使用が最適です。 |
| [キャプション付き画像]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types) | ![ウェイトリフターの画像とワークアウトクラスの予約を促すテキストが表示されたキャプション付きContent Card。]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | キャプション付き画像カードは、コピーと目を引く画像でコンテンツを紹介します。 |
| [画像のみ]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types) | ![テキストのみの画像のみContent Card。]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | 画像のみカードは、画像、GIF、およびその他のクリエイティブなテキスト以外のコンテンツ用のスペースで注目を集めます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ2: メッセージタイプを指定する" }

## ステップ3：Content Cardを作成する {#step-3-compose-a-content-card}

メッセージエディターの**作成**タブで、メッセージのコンテンツと動作のすべての側面を編集できます。

![メッセージエディターの作成タブにおけるContent Cardの詳細のサンプル。]({% image_buster /assets/img/content_card_compose.png %})

ここでの内容は、前のステップで選択した**カードタイプ**に応じて異なりますが、以下のオプションのいずれかが含まれる場合があります。

### 言語 {#language}

**言語を追加**を選択して、提供されたリストから希望する言語を追加します。これにより、メッセージに [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic) が挿入されます。コンテンツを記入する前に言語を選択し、Liquid内の適切な場所にテキストを入力できるようにすることをお勧めします。利用可能な言語の一覧については、[サポートされている言語]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization#languages-supported)をご覧ください。

![言語として英語、スペイン語、フランス語が選択され、国際化するフィールドとしてタイトル、説明、リンクテキストが選択されたウィンドウ。]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

#### 右から左へ記述するメッセージの作成 {#create-right-to-left-messages}

右から左へ記述するメッセージの最終的な外観は、サービスプロバイダーがどのようにレンダリングするかに大きく依存します。可能な限り正確に表示される右から左へ記述するメッセージを作成するためのベストプラクティスについては、[右から左に記述するメッセージの作成]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)を参照してください。

#### タイトルとメッセージ {#title-and-message}

何でも自由に記入できます。文字数に制限はありませんが、メッセージをすばやく伝え、顧客にクリックしてもらえるようにするのがベストです。明確で簡潔なタイトルとメッセージ内容をお勧めします。なお、これらのフィールドは画像のみのカードでは提供されません。

#### 画像 {#image}

Content Cardに画像を追加するには、**画像を追加**を選択するか、画像URLを入力します。**画像を追加**を選択すると**メディアライブラリ**が開き、以前にアップロードした画像を選択するか、新しい画像を追加できます。

メッセージタイプやプラットフォームごとに推奨される比率や要件が異なる場合がありますので、画像を発注または作成する前に必ず確認してください。Content Cardのメッセージフィールドは合計サイズが2&nbsp;KBに制限されていることにご注意ください。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### トップにピン留め {#pin-to-top}

Brazeはピン留めされたカードをユーザーのフィードの最上部に表示し、ユーザーはそれを非表示にすることができません。ユーザーのフィードに複数のピン留めされたカードがある場合、Brazeはそれらを時系列順に並べます。BrazeがContent Cardを配信するとき、カードはピン留めされるか、されないかのいずれかであり、そのステータスはカードの有効期間中変更されません。キャンペーンのピン留め設定を変更した場合、その更新は変更後に送信されたカードにのみ適用されます。すでにユーザーのフィードにあるカードのピン留めステータスは変更されません。

![「このカードをフィードのトップにピン留めする」オプションが選択された状態の、モバイルとWeb向けのBraze Content Cardプレビューの並列表示。]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### クリック時の動作 {#on-click-behavior}

顧客がカード内に表示されたリンクをクリックすると、リンクはアプリのより深い部分または別のサイトに誘導できます。Content Cardのクリック時の動作を選択する場合は、それに合わせて**リンクテキスト**も更新することを忘れないでください。

Content Cardのリンクでは以下のアクションが利用できます。

| アクション | 説明 |
|---|---|
| Web URLにリダイレクト | ネイティブではないWebページを開きます。 |
| [アプリ内へのディープリンク]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content) | アプリ内の既存の画面にディープリンクします。 |
| カスタムイベントを記録 | トリガーする[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)を選択します。別のContent Cardの表示や追加のメッセージングのトリガーに使用できます。 |
| カスタム属性を記録 | 現在のユーザーに設定する[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)を選択します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="クリック時の動作" }

**カスタムイベントを記録**および**カスタム属性を記録**オプションには、以下のSDKバージョンの互換性が必要です。

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## ステップ4：追加設定を構成する（オプション） {#step-4-configure-additional-settings-optional}

[キーと値のペア]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs)を使用して、カードのカテゴリを作成したり、[複数のContent Cardsフィード]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed#multiple-feeds)を作成したり、カードの並べ替え方法をカスタマイズしたりできます。

メッセージにキーと値のペアを追加するには、**設定**タブに移動して**新しいペアを追加**を選択します。

## ステップ5: キャンペーンまたはキャンバスの残りの部分を構築する {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab キャンペーン %}

キャンペーンの残りの部分を構築します。Content Cardsを構築するためのツールの最適な使用方法について、以下のセクションに進んで詳細をご確認ください。

### 配信スケジュールまたはトリガーを選択する {#choose-a-delivery-schedule-or-trigger}

Content Cardsは、スケジュールされた時間、アクション、またはAPIトリガーに基づいて配信できます。詳しくは、[キャンペーンのスケジュール]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)を参照してください。

また、キャンペーンの期間や[サイレント時間]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)を設定し、Content Cardsの有効期限を決定することもできます。特定の有効期限日、またはカードの有効期限が切れるまでの日数（最大30日）を設定できます。すべてのバリアントで同じ有効期限（期間または特定の時間）を使用する必要があります。

有効期限のカウントダウンはカードの送信時刻から開始されます。

- **スケジュールされたキャンペーン：** カウントダウンはスケジュールされた開始時刻から始まります。
- **アクションベースのキャンペーン：** カウントダウンはユーザーがトリガーアクションを実行した時点から始まります。

たとえば、アクションベースのContent Cardsが本日午後2時に1日の有効期限で送信された場合、翌日の午後2時に有効期限が切れます。

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

アクションベースの配信では、Content Cardsが表示されるまでに短い遅延が発生することが予想されます。この遅延が発生する理由と最小化する方法については、[トリガーイベントの直後にContent Cardsが表示されないのはなぜですか？]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#why-dont-content-cards-appear-immediately-after-a-trigger-event)を参照してください。

#### スケジュール配信 {#scheduled-delivery}

スケジュール配信によるContent Cardsキャンペーンでは、カードの作成タイミングを指定することで、新しいContent Cardsキャンペーンに対してBrazeがオーディエンスの適格性とパーソナライゼーションを評価するタイミングを選択できます。詳しくは、[カード作成]({{site.baseurl}}/card_creation)を参照してください。

#### ターゲットユーザーを選択する {#choose-users-to-target}

次に、セグメントやフィルターを選択してオーディエンスを絞り込み、[ユーザーをターゲット]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)にします。そのおおよそのセグメント人口のプレビューが自動的に表示されます。正確なセグメントメンバーシップは、メッセージが送信される前に常に計算されることにご注意ください。

{% multi_lang_include audience/target_audiences.md %}

#### コンバージョンイベントを選択する {#choose-conversion-events}

Brazeでは、キャンペーンを受信した後にユーザーが特定のアクション（[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)）を実行する頻度をトラッキングできます。ユーザーが指定されたアクションを実行した場合にコンバージョンがカウントされる最大30日間のウィンドウを設定するオプションがあります。

{% endtab %}

{% tab キャンバス %}

まだ完了していない場合は、キャンバスコンポーネントの残りのセクションを完了してください。多変量テストや[BrazeAI<sup>TM</sup>で最適化]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai)など、キャンバスの残りの部分を構築する方法の詳細については、[キャンバスを構築する]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas)を参照してください。

{% endtab %}
{% endtabs %}

## ステップ6: レビューとデプロイ {#step-6-review-and-deploy}

キャンペーンまたはキャンバスの作成が完了したら、詳細を確認し、[テスト]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages)を行ってから送信してください。詳しくは、[テストメッセージの送信]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=content%20card)を参照してください。

{% alert note %}
Content Cardsは本番環境ではプッシュ通知を必要としませんが、テスト送信ではプッシュペイロードでカードが配信されるため、テストデバイスでプッシュが有効になっている必要があります。テスト用のContent Cardsは送信後約5分で期限切れになります。
{% endalert %}

{% alert warning %}
Content Cardsは起動後に編集できません。新しいユーザーへの送信を停止したり、ユーザーのフィードから削除したりすることのみ可能です。このシナリオへの対処方法については、[送信済みカードの更新]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#updating-launched-cards)を参照してください。
{% endalert %}

次に、[Content Cardsレポート]({{site.baseurl}}/user_guide/channels/content_cards/reporting)で、Content Cardsキャンペーンの結果にアクセスする方法を確認してください。

## 知っておくべきこと {#things-to-know}

### ペイロードとフィードの制限 {#payload-and-feed-limitations}

パフォーマンスをサポートするため、Content Cardsには2つの主要な制約があります。各カードのペイロードサイズの制限と、フィードに表示できるカードの最大数です。

#### Content Cardsのサイズ制限 {#size-limitations-for-content-cards}

単一のContent Cardのデータペイロード全体は、Liquidパーソナライゼーションがレンダリングされた**後**で2 KBを超えることはできません。これには以下が含まれます。

* タイトル
* メッセージ
* 画像URL（画像ファイルサイズではなく、URL文字列自体の長さ）
* リンクテキスト
* 指定されたすべてのプラットフォームのリンクURL（iOS、Android、Web用の個別URLはすべて合計に含まれます）
* キーと値のペア（キー名とその値の両方）

Liquidを使用して長いテキスト文字列（カスタム属性からなど）を取得すると、制限を超える可能性があります。

キャンペーンコンポーザーは、静的コンテンツが制限を超えた場合に警告を表示します。Liquidを使用するダイナミックコンテンツのサイズは予測されません。メッセージサイズが2 KBを超えると、送信時に中止されます。これらの中止は、メッセージアクティビティログで理由 `Content card maximum size exceeded` として確認できます。

{% alert important %}
テスト送信では、2 KBを超えるContent Cardsでも正常に配信・表示される場合があります。
{% endalert %}

Content Cardsのペイロードサイズを管理するためのベストプラクティスは以下の通りです。

* 長いリンクにはURL短縮サービスを使用します。URL、特に長いトラッキングパラメータを含むURLは、サイズ制限の問題が発生する可能性があります。URL短縮サービスを使用すると、文字数を大幅に削減でき、ペイロードのスペースを確保できます。
* Liquidでダイナミックコンテンツを切り詰めます。ユーザー属性やAPI呼び出しからのダイナミックテキストでカードをパーソナライズする場合、コンテンツの長さは予測できないことがあります。`truncate`などのLiquidフィルターを積極的に使用して、ダイナミックテキストの長さに上限を設定してください。
* マルチプラットフォームURLを効率的に使用します。2 KBの制限には、定義するすべてのプラットフォームのURLが含まれます。各プラットフォームに長い固有のURLを使用すると、ペイロードサイズが倍増する可能性があります。可能であれば、すべてのプラットフォームで機能する単一のリンクを使用するか、必要に応じてURL短縮サービスを使用してください。
* リッチなコンテンツにはバナーを検討します。常に大量のコンテンツを必要とするユースケースでは、Content Cardsが適切なチャネルではない場合があります。バナーには同じ2 KBのペイロード制限がなく、アプリやWebサイトのエクスペリエンスにリッチなコンテンツを直接埋め込むのに適しています。

#### フィード内のカード数 {#number-of-cards-in-feed}

各ユーザーは、任意の時点でフィードに最大250枚の有効期限切れでないContent Cardsを持つことができます。この制限を超えると、Brazeは未読であっても最も古いカードを返さなくなります。却下されたカードもこの制限にカウントされるため、却下されたカードが多いと古いカードに利用可能なスペースが減少します。

カード制限に関する問題を防ぐために、以下のベストプラクティスをお勧めします。

- **短い有効期限を使用する：**時間に敏感なキャンペーン（週末セールなど）では、特定の有効期限を設定します。これにより、カードはフィードから自動的に削除され、関連性がなくなった後は制限にカウントされなくなります。
- **アクションベースの削除を活用する：**トランザクション型や目標ベースのカードに削除イベントを設定します。例えば、ユーザーにプロファイルの完了を促すカードは、`profile_completed`イベントが記録されたらすぐに削除する必要があります。
- **長期実行キャンペーンを監査する：**繰り返しまたは継続中のキャンペーンを確認し、時間の経過とともにフィードに多くのカードが蓄積されてユーザーに悪い体験を提供していないことを確認してください。

### Content Cardsの再適格性について {#understanding-re-eligibility-for-content-cards}

再適格性は、ユーザーが同じキャンペーンからメッセージを複数回受信できるかどうか、またいつ受信できるかを決定します。Content Cardsでは、再適格性の仕組みを理解することが、繰り返しキャンペーンの管理やユーザーが重複または古いメッセージを受信しないようにするために重要です。

{% alert tip %}
コンテンツを30日以上持続させたい場合は、[バナー]({{site.baseurl}}/user_guide/channels/banners)をお試しください。
{% endalert %}

#### 再適格性の計算方法 {#how-re-eligibility-is-calculated}

再適格性をオンにすると、ユーザーがキャンペーンに「再エントリ」できるまでのカウントダウンは、メッセージが送信された後に始まります。このカウントダウンが開始される具体的なタイミングは、カード作成設定によって異なります。

- [ファーストインプレッション時]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation#differences)を使用するContent Cardsは、インプレッション時間を使用して再適格性を計算します。
- キャンペーン開始時、マルチチャネルキャンペーン、またはキャンバスステップエントリ時に作成されたContent Cardsは、送信時間またはインプレッション時間のうち最も遅い方を使用します。

#### 30日間の有効期限と再適格性 {#the-30-day-expiration-and-re-eligibility}

混乱の一般的な原因は、キャンペーンの再適格性とすべてのContent Cardsの自動30日間有効期限の相互作用です。

すべてのContent Cardsは、送信または削除されてから30日後にBrazeのシステムから自動的にパージされます。再適格性を**オフ**にした長期実行の繰り返しキャンペーンがある場合、ユーザーは30日後に同じカードを再度受信する可能性があります。元のカードがパージされると、システムはそのユーザーがキャンペーンを受信した記録を認識しなくなり、次のセッションでそのユーザーが再び適格になります。

ユーザーが特定のキャンペーンからメッセージを1回だけ受信するようにするには、キャンペーンまたはキャンバスステップにこのキャンペーンからメッセージを受信していないユーザーのオーディエンスフィルターを追加します。このフィルターは、長期実行キャンペーンからの重複送信を防ぐ最も確実な方法です。

### 配信済みContent Cardsの管理 {#managing-live-content-cards}

Content Cardsは送信後、ユーザーに配信される準備が整った「受信トレイ」で待機します（メールと同様の仕組みです）。コンテンツがContent Cardに取り込まれると（表示時に）、そのライフスパン中に変更することはできません。これは、Connected Contentを通じてAPIを呼び出し、エンドポイントからのデータが変更された場合でも適用されます。このデータは更新されません。新しいユーザーへの送信を停止し、ユーザーのフィードから削除することのみが可能です。キャンペーンを変更した場合、変更後に送信されたカードのみに更新が含まれます。

#### 配信済みカードの更新 {#updating-launched-cards}

すでにカードを受信したユーザーのカードを変更するには、以下のいずれかの方法を使用する必要があります。

##### オプション1：キャンペーンを複製する（即時変更に推奨） {#option-1-duplicate-the-campaign-recommended-for-immediate-changes}

{% alert tip %}
このオプションは、カードに最新のコンテンツを表示するメッセージ、変更をすぐに反映する必要がある場合、または再適格性がオフになっている場合にお勧めします。
{% endalert %}

最初のアプローチは、キャンペーンをアーカイブして、新しい複製キャンペーンを起動することです。

1. 元のキャンペーンを停止し、プロンプトが表示されたら`Remove card after the next sync`を選択します。
2. キャンペーンを複製し、編集を行い、新しいバージョンを起動します。

キャンペーンを複製する場合、新しいバージョンのオーディエンスを定義する必要があります。セグメンテーションフィルターを使用して、更新されたカードを受信するユーザーを制御します。
* ユーザーがContent Cardに再適格にならない場合は、フィルター`Received Message from キャンペーン`を条件`Has Not`に設定して、Content Cardの以前のバージョンを受信していないユーザーをフィルタリングできます。
* 以前のカードを受信したユーザーがX日後に再適格になる場合は、`Last Received Message from specific campaign`をX日以上前に設定するフィルター、**または**`Received Message from キャンペーン`を`Has Not`条件で設定できます。

###### 影響 {#impact}

- **既存の受信者：**新規および既存の受信者は、適格であれば次のフィード更新時に更新されたカードを確認します。
- **レポート：**カードの各バージョンには個別の分析があります。

例えば、セッション開始でトリガーされ、再適格性が30日に設定されたキャンペーンがあるとします。ユーザーが2日前にキャンペーンを受信し、コピーを変更したいとします。まず、キャンペーンをアーカイブしてフィードからカードを削除します。次に、キャンペーンを複製し、新しいコピーで再起動します。ユーザーが別のセッションを開始すると、すぐに新しいカードを受信します。

##### オプション2：同じキャンペーンを停止して再起動する {#option-2-stop-and-relaunch-the-same-campaign}

{% alert tip %}
このオプションは、通知センターやメッセージ受信トレイでのユニークなメッセージ（プロモーションなど）、分析を統一することが重要な場合、またはメッセージの適時性が懸念でない場合（既存の受信者が更新されたカードを確認するために適格ウィンドウを待つことができる場合など）にお勧めします。
{% endalert %}

このアプローチでは、すべての分析が単一のキャンペーンに統一されます。新たに適格になったユーザーは新しいカードを受信しますが、既存の受信者への更新は再適格になるまで遅延します。

1. キャンペーンを停止し、プロンプトが表示されたら**Remove card after the next sync**を選択します。
2. 必要に応じてキャンペーンを編集します。
3. キャンペーンを再開します。

###### 影響

* **既存の受信者：**すでにカードを受信したユーザーは、再適格になるまで更新されたカードを受信しません。再適格性がオフになっている場合、新しいカードを受信することはありません。
* **レポート：**1つのキャンペーンに、起動されたカードバージョンのすべてのレポート分析が含まれます。Brazeは起動されたバージョン間を区別しません。

例えば、セッション開始でトリガーされ、再適格性が30日に設定されたキャンペーンがあるとします。ユーザーが2日前にキャンペーンを受信し、コピーを変更したいとします。まず、キャンペーンを停止してフィードからカードを削除します。次に、新しいコピーでキャンペーンを再公開します。ユーザーが別のセッションを開始すると、28日後に新しいカードを受信します。

{% alert note %}
キャンペーンを停止し、削除イベント設定を編集してから、フィードからカードを削除せずにキャンペーンを再開すると、ユーザーのフィードにある既存のカードは更新された削除イベント設定を使用します。カードは最初に送信されたときの元の削除イベント設定を保持しません。
{% endalert %}

#### カードの削除と有効期限 {#removing-and-expiring-cards}

##### 手動でのカード削除 {#manual-card-removal}

キャンペーンを停止することで、すべてのユーザーのフィードからカードをいつでも手動で削除できます。

1. Content Cardsキャンペーンを開き、キャンペーンを停止を選択します。
2. プロンプトが表示されたら、**Remove card after the next sync**を選択します。カードは次のフィード更新時に削除されます。

##### 自動カード削除 {#action-based-card-removal}

ユーザーが購入の完了や機能の有効化などの特定のアクションを実行したときに、カードを自動的に削除できます。

キャンペーンまたはキャンバスステップで、削除イベントを指定します。ユーザーがそのイベントを実行すると、Brazeがイベントを処理した後の次のフィード更新時にカードがフィードから削除されます。

{% alert note %}
この削除は即座には行われません。処理に遅延があるため、カードが消えるまでに数分かかり、フィードの更新が複数回必要になる場合があります。
{% endalert %}

{% alert tip %}
ユーザーのフィードからカードを削除するカスタムイベントや購入を複数指定できます。それらのアクションのいずれかがユーザーによって実行されると、キャンペーンのカードによって送信された既存のカードはすべて削除されます。適格なカードは、メッセージのスケジュールに従って引き続き送信されます。
{% endalert %}

![Content Card削除イベントオプションを含むContent Card削除条件パネル。]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

##### カードの有効期限 {#card-expiration}

Content Cardsは、送信されてから最大30日間利用可能です。30日後、Brazeはユーザーフィードからカードを削除し、Brazeのシステムからパージします。

#### カードを30日以上持続させる {#making-cards-last-longer-than-30-days}

{% alert tip %}
30日間のContent Card制限よりも長くメッセージを持続させる必要があるユースケースでは、バナーの使用を検討してください。バナーは永続性を考慮して設計されており、必須の有効期限がないため、必要な限り表示し続けることができます。
{% endalert %}

カードが常に利用可能であるように見せたい場合は、30日ごとにカードを事実上置き換える繰り返しキャンペーンを作成できます。

1. Content Cardsの有効期間を30日に設定します。
2. キャンペーンの再適格性を30日に設定します。
3. 「セッション開始」でトリガーされるようにキャンペーンを設定します。

### Content Cardsの同期と更新 {#content-card-sync-and-refresh}

Content Cardsはスケジュールに従って、またアプリがフィードを更新するときに同期されます。同期動作はフル同期と部分同期で異なり、SDK統合はセッション開始時にカードが更新されるタイミングに影響します。実装の詳細については、[Content Cardsフィードのカスタマイズ]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed)および[Content Cardsの作成]({{site.baseurl}}/developer_guide/content_cards/creating_cards)を参照してください。

### Content Cardsキャンペーンの停止による影響 {#impact-of-stopping-content-cards-campaigns}

キャンペーンを停止し、**Remove card after the next sync**を選択すると、Brazeは次のフィード更新時にユーザーフィードからカードを削除します。ユーザーが閲覧する前に削除されたカードにはインプレッションが記録されないため、インプレッション数が送信数よりも少なくなる場合があります。

## トラブルシューティング {#troubleshooting}

### トリガーイベントの直後にContent Cardsが表示されないのはなぜですか？ {#why-dont-content-cards-appear-immediately-after-a-trigger-event}

アクションベースの配信キャンペーン（セッション開始など）では、トリガーイベントからカードが利用可能になるまでに短い遅延が発生することが想定されます。この遅延が発生する理由は以下の通りです。

- トリガーイベントがBrazeのサーバーにフラッシュされる
- キャンペーンがトリガーされ、ユーザーの適格性が記録される
- そのユーザー向けにContent Cardsがデータベースに作成される
- SDKが同期し、利用可能なすべてのカードをデバイスに取得する

SDKの同期がユーザーの適格性の記録より前に行われた場合、ユーザーはカードを受信しません。

初回セッション中の新規ユーザーについては、この遅延は避けられません。即座に利用可能にする必要がある既存ユーザーについては、代わりにスケジュール配信の使用を検討してください。

新規ユーザーと既存ユーザーの両方で遅延を最小限に抑える必要がある場合は、2つのキャンペーンを作成できます。

- **セッション数が0より大きい既存ユーザー：** スケジュール配信キャンペーンを使用します。カードは事前に作成され、即座に利用可能になります。
- **セッション数が0の新規ユーザー：** アクショントリガーキャンペーンを使用します。カードは最初のセッショントリガーの後に作成されます。

このアプローチにより、既存ユーザーはカードを即座に表示できる一方、新規ユーザーにも初回セッションでの短い遅延の後に配信できます。レイテンシーを改善するための追加の戦略については、[Content Cardsの低レイテンシー要件の改善]({{site.baseurl}}/user_guide/channels/content_cards/best_practices/improving_low_latency_requirements)を参照してください。

### インプレッションまたは却下のタイムスタンプがキャンペーンのスケジュール外になるのはなぜですか？ {#why-do-impression-or-dismiss-timestamps-fall-outside-the-campaign-schedule}

分析やCurrentsのインプレッションおよび却下のタイムスタンプは、ユーザーがContent Cardsを閲覧または却下した時点を反映しており、Brazeがカードを作成または送信した時点ではありません。カードはContent Cardsが更新されるまでユーザーのフィードに残ることがあるため、インプレッションや却下のタイムスタンプはキャンペーンの送信ウィンドウの後になる場合があります。

時刻がまだ想定と異なる場合は、以下を確認してください。

- 分析を会社のタイムゾーンで表示しているか、Currentsでのユーザーのタイムゾーンで表示しているかを確認してください。
- ユーザーが実際にカードを受信した後に閲覧または却下したかどうかを確認し、送信時刻だけと比較していないか確認してください。

Content Cardsの指標の詳細については、[Content Cardsレポート]({{site.baseurl}}/user_guide/channels/content_cards/reporting)を参照してください。

### 「キャンペーンのすべての有効期限の値が一致する必要があります」エラー {#all-expiration-values-for-a-campaign-must-match-error}

このエラーは、多変量Content Cardsキャンペーンでバリアント間で異なる有効期限設定が使用されている場合に表示されます。すべてのバリアントに同じ有効期限（期間または特定の時刻）を設定するか、キャンペーンを単一バリアントに減らしてから、再度保存してください。キャンペーンの作成時に有効期限を設定する方法については、[配信スケジュールまたはトリガーの選択](#choose-a-delivery-schedule-or-trigger)を参照してください。