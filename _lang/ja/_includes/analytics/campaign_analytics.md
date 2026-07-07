## 分析を表示する {#viewing-analytics}

キャンペーンを開始したら、そのキャンペーンの詳細ページに戻って主要な指標を確認できます。**キャンペーン**ページに移動し、キャンペーンを選択して詳細ページを開きます。{% if include.channel != "banner" %}{% if include.channel == "Content Card" %}Content Cards{% elsif include.channel == "banner" %}バナー{% elsif include.channel == "email" %}メール{% elsif include.channel == "in-app message" %}アプリ内メッセージ{% elsif include.channel == "KakaoTalk" %}KakaoTalkメッセージ{% elsif include.channel == "push" %}プッシュメッセージ{% elsif include.channel == "SMS" %}SMSメッセージ{% elsif include.channel == "whatsapp" %}WhatsAppメッセージ{% elsif include.channel == "webhook" %}webhook{% endif %}をキャンバスで送信した場合は、[キャンバス分析]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics)を参照してください。{% endif %}

{% alert tip %}
レポートに記載されている用語や指標の定義をお探しですか？以下を参照してください。
  {% if include.channel == "email" %}[メール分析用語集]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary)
  {% elsif include.channel == "banner" %}[レポート指標用語集]({{site.baseurl}}/user_guide/data/report_metrics)でバナーによるフィルタリングを行ってください。
  {% elsif include.channel == "Content Card" %}[レポート指標用語集]({{site.baseurl}}/user_guide/data/report_metrics)でContent Cardsによるフィルタリングを行ってください。
  {% elsif include.channel == "in-app message" %}[レポート指標用語集]({{site.baseurl}}/user_guide/data/report_metrics)でアプリ内メッセージによるフィルタリングを行ってください。
  {% elsif include.channel == "push" %}[レポート指標用語集]({{site.baseurl}}/user_guide/data/report_metrics)でプッシュによるフィルタリングを行ってください。
  {% elsif include.channel == "SMS" %}[レポート指標用語集]({{site.baseurl}}/user_guide/data/report_metrics)でSMS/MMSおよびRCSによるフィルタリングを行ってください。
  {% elsif include.channel == "whatsapp" %}[レポート指標用語集]({{site.baseurl}}/user_guide/data/report_metrics)でWhatsAppによるフィルタリングを行ってください。
  {% elsif include.channel == "webhook" %}[レポート指標用語集]({{site.baseurl}}/user_guide/data/report_metrics)でWebhookによるフィルタリングを行ってください。{% endif %}
{% endalert %}

**キャンペーン分析**タブから、一連のパネルでレポートを確認できます。以下のセクションに記載されているものより多い場合も少ない場合もありますが、それぞれに有用な目的があります。

### 期間 {#time-range}

**キャンペーン分析**の期間設定は、デフォルトで現在時刻から過去90日間を表示します。これは、キャンペーンが90日以上前に開始された場合、指定した期間の分析データが「0」と表示されることを意味します。古いキャンペーンの全分析データを表示するには、レポートの時間範囲を調整してください。

### キャンペーンの詳細 {#campaign-details}

**キャンペーンの詳細**パネルには、
  {% if include.channel == "banner" %}バナー
  {% elsif include.channel == "Content Card" %}コンテンツカード
  {% elsif include.channel == "email" %}メール
  {% elsif include.channel == "in-app message" %}アプリ内メッセージ
  {% elsif include.channel == "KakaoTalk" %}KakaoTalkメッセージ
  {% elsif include.channel == "push" %}プッシュメッセージ
  {% elsif include.channel == "SMS" %}SMS、MMS、RCS
  {% elsif include.channel == "whatsapp" %}WhatsAppメッセージ
  {% elsif include.channel == "webhook" %}Webhook
  {% endif %}の全体的なパフォーマンスのハイレベルな概要が表示されます。

このパネルでは、受信者に送信されたメッセージの数、1次コンバージョン率、このメッセージによって生み出された総収益などの全体的な指標を確認できます。このページから、配信、オーディエンス、コンバージョン設定を確認することもできます。

{% alert note %}
ダッシュボードとSnowflakeの分析数値はわずかに異なる場合があります。Brazeはダッシュボードの数値を測定し、Snowflakeへの行の記録を別々に行います。Snowflakeの方がより正確なデータソースであるため、これらのソース間に差異がある場合は、Snowflakeのデータを参照することをお勧めします。
{% endalert %}

{% if include.channel == "whatsapp" %}
{% alert note %}
WhatsAppチャネルには既読率が含まれます。この指標は既読通知をオンにしているユーザーにのみ配信されるため、値は異なる場合があります。
{% endalert %}
{% endif %}

{% if include.channel == "Content Card" %}
![キャンペーンのパフォーマンスを判断するために使用される指標の概要を含むキャンペーン詳細パネル。]({% image_buster /assets/img/cc-campaign-details.png %})

{% elsif include.channel == "banner" %}
![キャンペーンのパフォーマンスを判断するために使用される指標の概要を含むキャンペーン詳細パネル。]({% image_buster /assets/img/banners/campaign_details.png %})

{% elsif include.channel == "email" %}
![キャンペーンのパフォーマンスを判断するために使用される指標の概要を含むキャンペーン詳細パネル。]({% image_buster /assets/img/campaign_details_email.png %})

{% elsif include.channel == "push" %}
![キャンペーンのパフォーマンスを判断するために使用される指標の概要を含むキャンペーン詳細パネル。]({% image_buster /assets/img/campaign_details_push.png %})

{% elsif include.channel == "SMS" %}
![キャンペーンのパフォーマンスを判断するために使用される指標の概要を含むキャンペーン詳細パネル。]({% image_buster /assets/img/campaign_details_sms.png %})

{% elsif include.channel == "in-app message" %}
![キャンペーンのパフォーマンスを判断するために使用される指標の概要を含むキャンペーン詳細パネル。]({% image_buster /assets/img/campaign_details_iam.png %})

キャンバスでは、作成したキャンバスにアプリ内メッセージのパフォーマンスがマッピングされます。ページ上部のコントロールパネルを使用して、他のメッセージングタイプ（チャネル）をクリアし、キャンバス内のアプリ内メッセージのみを表示できます。

![In-App Messageのチェックボックスが選択されたチャネル選択オプション。]({% image_buster /assets/img/in-app_message_canvas_reporting.png %})

{% elsif include.channel == "KakaoTalk" %}
![キャンペーンの詳細セクション。]({% image_buster /assets/img/kakaotalk/campaign_details.png %})

{% elsif include.channel == "webhook" %}
![キャンペーンのパフォーマンスを判断するために使用される指標の概要を含むキャンペーン詳細パネル。]({% image_buster /assets/img/campaign_details_webhook.png %})

{% endif %}

#### 推定オーディエンスと現在のオーディエンス {#estimated-audience-and-current-audience}

ワークスペースの規模に応じて、**キャンペーンの詳細**パネルではオーディエンス統計が**推定オーディエンス**または**現在のオーディエンス**と表示されます。

以下の表は、各ラベルの意味をまとめたものです。

| フッターラベル | 使用される場合 |
| --- | --- |
| **推定オーディエンス** | Brazeはデフォルトでデータベース全体のカウントを実行しません。オーディエンスサイズはサンプルから推定・外挿されます。これはセグメントビルダーの**到達可能なユーザー**の範囲と同様です。特に大規模なワークスペースや、ワークスペースに対する割合が小さいセグメントでは、誤差が生じることがあります。 |
| **現在のオーディエンス** | Brazeがワークスペースプロファイルの完全スキャンでデフォルトの統計を計算できるため、表示されるオーディエンスサイズはサンプリングされていない現在のカウントです（ただし、チャネルの到達可能性、サブスクリプションルール、その他のターゲティングオプションの影響は受けます）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="推定オーディエンスと現在のオーディエンス" }

サンプリングの動作、**正確な統計を計算**、**到達可能なユーザー**のセグメンテーションの詳細については、[セグメントサイズの測定]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size)を参照してください。

{% if include.channel == "Content Card" %}

#### コントロールグループ {#cc-control-group}

個々のコンテンツカードの影響を測定するには、A/Bテストに[コントロールグループ]({{site.baseurl}}/user_guide/intelligence/multivariate_testing#step-4-choose-a-segment-and-distribute-your-users-across-variants)を追加できます。トップレベルの**キャンペーンの詳細**パネルには、コントロールグループバリアントの指標は含まれません。

{% elsif include.channel == "SMS" %}

#### コントロールグループ {#sms-control-group}

個々のSMS、MMS、またはRCSメッセージの影響を測定するには、A/Bテストに[コントロールグループ]({{site.baseurl}}/user_guide/intelligence/multivariate_testing#step-4-choose-a-segment-and-distribute-your-users-across-variants)を追加できます。トップレベルの**キャンペーンの詳細**パネルには、コントロールグループバリアントの指標は含まれません。

{% elsif include.channel == "whatsapp" %}

#### コントロールグループ {#whatsapp-control-group}

個々のWhatsAppメッセージの影響を測定するには、A/Bテストに[コントロールグループ]({{site.baseurl}}/user_guide/intelligence/multivariate_testing#step-4-choose-a-segment-and-distribute-your-users-across-variants)を追加できます。トップレベルの**キャンペーンの詳細**パネルには、コントロールグループバリアントの指標は含まれません。

{% elsif include.channel == "webhook" %}

#### コントロールグループ {#webhook-control-group}

個々のWebhookメッセージの影響を測定するには、A/Bテストに[コントロールグループ]({{site.baseurl}}/user_guide/intelligence/multivariate_testing#step-4-choose-a-segment-and-distribute-your-users-across-variants)を追加できます。トップレベルの**キャンペーンの詳細**パネルには、コントロールグループバリアントの指標は含まれません。

{% endif %}

#### 最後に表示してからの変更 {#changes-since-last-viewed}

チームの他のメンバーによるキャンペーンへの更新数は、キャンペーン概要ページの*最後に表示してからの変更*指標で追跡されます。**最後に表示してからの変更**を選択すると、キャンペーンの名前、スケジュール、タグ、メッセージ、オーディエンス、承認ステータス、またはチームアクセス設定の更新に関する変更ログを表示できます。各更新について、誰がいつ更新を行ったかを確認できます。この変更ログを使用してキャンペーンの変更を監査できます。

<!--
### Message Performance

The **Message Performance** panel outlines how well your message has performed across various dimensions. The metrics in this panel vary depending on your chosen messaging channel, and whether or not you are running a multivariate test. You can click on the <i class="fa fa-eye preview-icon"></i> **Preview** icon to view your message for each variant or channel.
-->
{% if include.channel == "Content Card" %}
### Content Cardsのパフォーマンス {#content-card-performance}

**Content Cardsパフォーマンス**パネルでは、メッセージがさまざまな側面でどの程度のパフォーマンスを示したかを確認できます。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>**プレビュー**アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

![Content Cardsのメッセージパフォーマンス分析]({% image_buster /assets/img/cc-message-performance.png %})

{% elsif include.channel == "email" %}
### メールのパフォーマンス {#email-performance}

**メールパフォーマンス**パネルでは、メッセージがさまざまな側面でどの程度のパフォーマンスを示したかを確認できます。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>**プレビュー**アイコンを選択すると、バリアントやチャネルごとにメッセージを表示できます。

![メールメッセージのパフォーマンス分析]({% image_buster /assets/img_archive/email_message_performance.png %})

{% elsif include.channel == "in-app message" %}
### アプリ内メッセージのパフォーマンス {#in-app-message-performance}

**アプリ内メッセージパフォーマンス**パネルでは、メッセージがさまざまな側面でどの程度のパフォーマンスを示したかを確認できます。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>**プレビュー**アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

![アプリ内メッセージのパフォーマンス分析]({% image_buster /assets/img_archive/iam_message_performance.png %})

{% elsif include.channel == "push" %}
### プッシュのパフォーマンス {#push-performance}

**プッシュパフォーマンス**パネルでは、メッセージがさまざまな側面でどの程度のパフォーマンスを示したかを確認できます。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>**プレビュー**アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

![プッシュメッセージのパフォーマンス分析]({% image_buster /assets/img_archive/push_message_performance.png %})

{% elsif include.channel == "SMS" %}
### SMS/MMS/RCSのパフォーマンス {#smsmmsrcs-performance}

**SMS/MMS/RCSパフォーマンス**パネルでは、メッセージがさまざまな側面でどの程度のパフォーマンスを示したかを確認できます。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>**プレビュー**アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

![コントロールグループ、バリアント1、バリアント2の指標テーブルを含むSMS/MMS/RCSパフォーマンスパネル。]({% image_buster /assets/img_archive/sms_message_performance.png %})

{% elsif include.channel == "banner" %}
### バナーのパフォーマンス {#banner-performance}

**バナーパフォーマンス**パネルでは、メッセージがさまざまな側面でどの程度のパフォーマンスを示したかを確認できます。これらの指標は、メッセージングチャネルや多変量テストを実施しているかどうかによって異なります。

![コントロールグループ、バリアント1、バリアント2の指標テーブルを含むSMS/MMSパフォーマンスパネル。]({% image_buster /assets/img/banners/banner_performance.png %})

{% elsif include.channel == "KakaoTalk" %}
### KakaoTalkのパフォーマンス {#kakaotalk-performance}

**KakaoTalkパフォーマンス**パネルでは、メッセージがさまざまな側面でどの程度のパフォーマンスを示したかを確認できます。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>**プレビュー**アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

{% elsif include.channel == "webhook" %}
### Webhookのパフォーマンス {#webhook-performance}

**Webhookパフォーマンス**パネルでは、メッセージがさまざまな側面でどの程度のパフォーマンスを示したかを確認できます。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>**プレビュー**アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

![コントロールグループとバリアント1の指標テーブルを含むWebhookパフォーマンスパネル。]({% image_buster /assets/img/webhook_message_performance.png %})

{% elsif include.channel == "whatsapp" %}
### WhatsAppのパフォーマンス {#whatsapp-performance}

**WhatsAppパフォーマンス**パネルでは、メッセージがさまざまな側面でどの程度のパフォーマンスを示したかを確認できます。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>**プレビュー**アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

![バリアント1の指標テーブルを含むWhatsAppパフォーマンスパネル。]({% image_buster /assets/img/whatsapp_message_performance.png %})

{% endif %}

表示を簡素化する場合は、<i class="fas fa-plus"></i>**列を追加/削除**をクリックし、必要に応じて指標をクリアします。デフォルトでは、すべての指標が表示されます。

{% if include.channel == "email" %}

#### ヒートマップ {#heatmaps}

ヒートマップを使用すると、1つのメールキャンペーン内の異なるリンクがどの程度成功したかを確認できます。**メッセージ分析**セクションから、**メールパフォーマンス**パネルに移動します。**プレビューとヒートマップ**を選択して、メールキャンペーンとヒートマップのプレビューを表示します。または、バリアント名のハイパーリンクを選択してヒートマップを表示することもできます。

{% alert note %}
キャンペーン分析では、バリアントごとに最大100件のユニークURLのクリックデータが、合計クリック数順に表示されます。URLは正規化された形式（クエリパラメーターを含まない）でグループ化されます。バリアントに100件を超えるユニークな正規化URLがある場合、クリック数上位100件のみが表示されます。この制限を超えるURLのクリックデータは存在しますが、ダッシュボードやヒートマップには表示されません。リンクエイリアスが有効な場合、クリックは生のURLではなくリンクIDで追跡されるため、通常はユニークエントリ数が少なくなり、この制限に達する可能性が低くなります。
{% endalert %}

このビューでは、**ヒートマップ表示**トグルを使用して、キャンペーンの存続期間中のクリックの全体的な頻度と場所を示すメールのビジュアルビューを表示できます。**合計クリック数によるリンクテーブル**パネルでは、メールキャンペーン内のすべてのリンクを表示し、合計クリック数で並べ替えることができます。これにより、ユーザーがどこに移動しているかについて追加のインサイトが得られます。参照用にヒートマップのコピーを保存するには、ダウンロードボタンを選択します。

{% alert note %}
リンクが動的URLにLiquidを使用している場合、クリックされたURLがメッセージ内のレンダリングされたリンクと十分に一致せず、ヒートマップがそのリンクにクリックを関連付けられない場合があるため、それらのリンクがヒートマップに表示されないことがあります。全体像を把握するには、**合計クリック数によるリンクテーブル**パネルのクリックデータを使用してください。
{% endalert %}

![メールキャンペーンと、リンクエイリアスの例とその合計クリック数を示すパネルを含むプレビューとヒートマップページの例。]({% image_buster /assets/img_archive/email_heatmap_example.png %})

#### 画像 {#images}

ヒートマップのプレビューやエクスポートで画像が壊れるのを防ぐために、画像URLのCORSを有効にすることをお勧めします。

エクスポートで画像が欠落している場合は、開発者と協力して画像アセットがクロスオリジンアクセスを許可するようにしてください。サーバーは`Access-Control-Allow-Origin`ヘッダーに`*`またはBrazeダッシュボードのドメインを返す必要があります。

{% endif %}

{% if include.channel == "Content Card" %}

#### コンテンツカードの指標 {#content-card-metrics}

以下は、メッセージのパフォーマンスを確認する際に表示される主な指標の内訳です。すべてのContent Cards指標の完全な定義については、[レポート指標用語集]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics)を参照し、Content Cardsでフィルタリングしてください。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="コンテンツカードの指標">
    <caption class="sr-only">コンテンツカードのパフォーマンス指標</caption>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#messages-sent">Messages Sent</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Messages Sent' %} <br><br>
                この計算方法は、
                <a href="/docs/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression">カード作成</a> で選択した内容によって異なります：<br><br>
                <ul>
                    <li><b>開始時またはステップエントリ時：</b>作成され、閲覧可能なカードの数です。ユーザーがカードを閲覧したかどうかはカウントされません。</li>
                    <li><b>最初のインプレッション発生時：</b>ユーザーに表示されたカードの数です。</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#total-impressions">Total Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} 同じユーザーに対して複数回増加する可能性があります。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-impressions">Unique Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">このカウントは、</span>ユーザーがコンテンツカードを2回目に閲覧しても増加しません。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-daily-impressions">Unique Daily Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Daily Impressions' %} <br><br> ユーザーは毎日ユニークデイリーインプレッションを持つことができるため、<i>Unique Impressions</i>よりもこの数値が高くなることが想定されます。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-clicks">Unique Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} これにはBrazeが提供する配信停止リンクのクリックも含まれます。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-dismissals">Unique Dismissals</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}</td>
        </tr>
    </tbody>
</table>

{% alert note %}
インプレッションの記録方法については、Web、Android、iOSで若干のニュアンスの違いがあります。一般的にBrazeは、ユーザーがフィード内の特定のコンテンツカードまでスクロールした後、カードが表示されたときにインプレッションを記録します。
{% endalert %}

#### ユニークデイリーインプレッションとユニークインプレッション {#unique-daily-impressions-versus-unique-impressions}

メッセージの可視性をカバーする指標がいくつかあります。これには_Unique Daily Impressions_と_Unique Impressions_が含まれます。これらの指標をよりよく理解するために、いくつかのシナリオ例を見てみましょう。

例えば、今日コンテンツカードを閲覧し、翌日に同じキャンペーンから新しいカードを受け取り、さらにその翌日にも受け取った場合、_Unique Daily Impression_として3回カウントされます。ただし、_Unique Impression_は1回のみカウントされます。また、カードがデバイスで利用可能であったため、_Messages Sent_の数にもカウントされます。

別の例として、15万件の_Messages Sent_を示すContent Cardsキャンペーンで5件の_Unique Impressions_があるとします。これは、カードが（バックエンドで）15万人のオーディエンスに利用可能になったものの、その送信後に以下のステップをすべて実行したのはわずか5人のユーザーのデバイスだけだったことを意味します：

1. セッションを開始した、またはアプリが明示的にContent Cardsの同期を要求した（またはその両方）
2. Content Cardsビューに移動した
3. SDKがインプレッションを記録し、サーバーにログを送信した

_Messages Sent_は閲覧可能なContent Cardsを指し、_Unique Daily Impressions_は実際に閲覧されたContent Cardsを指します。

{% elsif include.channel == "banner" %}

### バナー指標 {#banner-metrics}

これらは、バナーキャンペーンのパフォーマンスを確認する際に追跡すべき重要な指標です。バナーのクリック数とインプレッション数はSDKで自動的に追跡されます。

すべてのバナー指標の完全な定義については、[レポート指標用語集]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics)を参照し、バナーでフィルタリングしてください。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="バナーの指標">
    <caption class="sr-only">バナーのパフォーマンス指標</caption>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">Total Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} バナーの場合、インプレッションはユーザーセッションごとに1回記録されます。同じセッション内で同じバナーが複数回表示された場合、インプレッションは1回のみ記録されます。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">Unique Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">各ユーザーは1回のみカウントされます。</span></td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">Total Clicks</a></td>
            <td class="no-split"><i>Total Clicks</i>は、同じユーザーが複数回クリックしたかどうかにかかわらず、配信されたメッセージ内でクリックしたユーザーの総数（および割合）です。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-dismissals">Total Dismissals</a></td>
            <td class="no-split"><i>Total Dismissals</i>は、ユーザーがバナーを閉じた合計回数です。閉じる動作が有効になっているバナーでのみ利用可能です。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">Unique Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks No Dispatch ID' %} 各ユーザーは1回のみカウントされます。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#primary-conversions">Primary Conversions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-daily-impressions">Unique Daily Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Daily Impressions' %} <br><br> 閲覧者は毎日ユニークデイリーインプレッションを持つことができるため、<i>Unique Impressions</i>よりもこの数値が高くなることが想定されます。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#revenue">Revenue</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confidence">Confidence</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Confidence' %}</td>
        </tr>
    </tbody>
</table>

#### バナー指標の計算例 {#banner-metrics-calculation-examples}

メッセージの可視性をカバーする指標がいくつかあります。これには_Unique Daily Impressions_と_Unique Impressions_が含まれます。これらの指標をよりよく理解するために、いくつかのシナリオ例を見てみましょう。

例えば、今日バナーを閲覧し、翌日に同じバナーを閲覧し、さらにその翌日にも閲覧した場合、_Unique Daily Impression_として3回カウントされます。ただし、_Unique Impression_は1回のみカウントされます。

別の例として、バナーキャンペーンで5件の_Unique Impressions_があるとします。これは、以下のすべてのステップを実行したユーザーのデバイスがわずか5台だったことを意味します：

1. セッションを開始した、またはアプリが明示的にバナーの同期を要求した（またはその両方）
2. バナービューに移動した
3. SDKがインプレッションを記録し、サーバーにログを送信した

_Unique Daily Impressions_は、実際に閲覧されたバナーを指します。

{% elsif include.channel == "email" %}

#### メール指標 {#email-metrics}

他のチャネルでは見られない、メール固有の主な指標をいくつか紹介します。Brazeで使用されるすべてのメール指標の完全な定義については、[メール分析用語集]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary)を参照してください。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="メールの指標">
    <caption class="sr-only">メールのパフォーマンス指標</caption>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">Unique Clicks</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} これはメールについて7日間の期間で追跡され、<a href='{{ site.homeurl }}{{ site.baseurl }}/user_guide/messaging/messaging_fundamentals/dispatch_id/'>dispatch_id</a> によって測定されます。これにはBrazeが提供する配信停止リンクのクリックも含まれます。この数値は5〜10%の範囲が目安です。10%を超える場合は非常に優秀です！
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-opens">Unique Opens</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Unique Opens' %} メールについては、7日間の期間で追跡されます。この数値は30〜40%の範囲が目安です。40%を超える場合は非常に優秀です！
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#click-to-open-rate">Click-to-Open Rate</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#spam">Spam Rate</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Spam' %} この指標が0.08を超える場合、メッセージの文面が売り込み色が強すぎるか、メールアドレスの収集方法を見直す必要がある（メッセージの受信を希望しているユーザーに送信しているか確認する）兆候かもしれません。
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unsubscribers-or-unsub">Unsubscribers or Unsub</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#other-opens">Other Opens</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Other Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#estimated-real-opens">Estimated Real Opens</a></td>
            <td class="no-split"> {% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %} 詳細は次のセクションを参照してください。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#machine-opens">Machine Opens</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Machine Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">Bounces</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#hard-bounce">Hard Bounce</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#soft-bounce">Soft Bounce</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deferral">Deferral</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deferral' %}</td>
        </tr>
    </tbody>
</table>

##### 配信とバウンス {#deliveries-and-bounces}

ダッシュボードでは*ハードバウンス*が強調表示されます。一部の*バウンス*はソフトバウンスの場合があり、その数だけでは一致しません。ソフトバウンスは以下の計算式で概算できます：

_送信数 −（配信数 + ハードバウンス数）≈ ソフトバウンス数_

_配信数_はメールサービスプロバイダー（ESP）の再試行期間中に再試行が成功するにつれて増加する可能性がありますが、1回限りの送信の場合、_送信数_とハードバウンス数は送信完了後に固定されます。SendGridとSparkPostは最大72時間再試行します。Amazon SESは最大14時間再試行します。

###### 一般的な配信トラブルシューティングのシナリオ {#common-delivery-troubleshooting-scenarios}

メール分析を確認する際は、以下のパターンに注意してください：

- **_送信数_と（_配信数_ + _ハードバウンス数_）の差：** 1回限りの送信後のESP再試行期間中、この差はソフトバウンスまたはまだ再試行中の延期を反映していることが多いです。再試行が完了した後、残りの差は通常、ソフトバウンスして配信されなかったメッセージを意味します。これらの送信はキャンペーンの_配信数_や_バウンス数_にはカウントされません。[配信とバウンス](#deliveries-and-bounces)の計算式を使用して、処理中のソフトバウンスを概算してください。
- **再試行完了後も_配信数_が低い場合：** 再試行が完了しても配信率が低い場合は、この送信のボリュームを通常のパターンと比較してください。メールボックスプロバイダーは、送信者のレピュテーションに対してボリュームが急増した場合、メールを延期、スロットル、またはソフトバウンスすることがあります。[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)に`Email was deferred due to the following reason(s): [IPs were throttled by recipient server]`のようなメッセージが表示されることがあります。大量送信のペースを調整するには[配信速度レート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting)を使用し、追加のトラブルシューティング手順については[スロットルされたIP]({{site.baseurl}}/user_guide/channels/email/reporting#throttled-ips)を参照してください。
- **キャンペーン分析にソフトバウンスと延期が表示されない：** キャンペーン分析では_ハードバウンス_が強調表示されますが、_ソフトバウンス_や_延期_は個別の列として含まれません。これらのイベントはメッセージアクティビティログ、[ソフトバウンスセグメントフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#soft-bounced)、またはCurrentsの延期イベントで監視してください。再試行の仕組みについては、[延期](#deferrals)を参照してください。
- **配信率が合計100%にならない場合：** _配信率%_、_バウンス率%_、_スパム率%_は_送信数_の100%にならない場合があります。ESP再試行期間後にソフトバウンスして配信されなかったメッセージは、キャンペーンの_配信数_や_バウンス数_にカウントされないため、_送信数_の一部がこれらの率で説明されないことがあります。最終的な配信パフォーマンスを判断する前に再試行が完了するのを待つか、[配信とバウンス](#deliveries-and-bounces)の計算式を使用してまだ再試行中の送信数を推定してください。

##### 開封イベントなしのクリック {#clicks-without-an-open-event}

開封トラッキングピクセルが読み込まれない場合、開封なしでクリックが記録されることがあります。例えば、Gmailでメッセージがクリップされた場合や、ユーザーが画像を無効にしている場合（開封ピクセルは通常フッターにあります）です。一部のクライアントは画像をプロキシ経由で取得するため（Apple Mailなど）、ユーザーがメールを読んだときではなく、サーバーが最初にピクセルを取得したときに開封が記録される場合があります。企業ドメインではデフォルトで画像がブロックされていることが多いです。

クリックと開封が異なる日に記録されることもあります。ユーザーが5月16日に画像オフの状態でクリックし（開封なし）、5月17日にウェブメールで開封する（その時点で開封が記録される）場合があります。

##### *Unique Clicks*が*Unique Opens*を上回る場合 {#higher-unique-clicks-than-unique-opens}

オーディエンスから低い比率を期待していても、*Unique Clicks*が*Unique Opens*を大幅に上回る（例えば、ユニーク開封1件あたり複数のユニーククリック）場合があります。このパターンは通常、開封が過少カウントされているか、クリックが膨張しているか、またはその両方を意味します。ただし、これはBrazeがクリックを単独で誤ってカウントしていることを意味するものではありません。

Brazeは、開封トラッキングピクセルが読み込まれたときにメールの開封を記録します。このピクセルは、BrazeがメッセージHTMLに追加する小さな透明画像（通常1 x 1&nbsp;pxと説明されます）です。ピクセルが読み込まれない場合、その閲覧に対して開封は記録されませんが、リンクのクリックは引き続き記録されるため、クリック開封率やこれら2つの指標のバランスが偏って見えることがあります。

**メールボックスが開封トラッキングピクセルを読み込まなかった場合**

ピクセルが読み込まれない可能性がある場合：

- **メッセージがクリップされた場合。** 長いHTMLは、末尾のピクセルを含むコンテンツを「メッセージ全体を表示」のような切り捨ての背後に押しやります。Gmailでは、約[102&nbsp;KB]({{site.baseurl}}/user_guide/channels/email/best_practices/email_styling#email-size)を超えるメッセージがクリップされることが多く、メッセージ全体が開かれるまで（場合によってはクライアントによってはそれでも）ピクセルの読み込みが妨げられることがあります。
- **画像がブロックまたは制限されている場合。** より厳格な受信トレイセキュリティ（企業アカウントに多い）は、受信者が画像の読み込みを選択するまでリモート画像をブロックする可能性があるため、トラッキングリンクをクリックしても開封ピクセルが発火しません。
- **メッセージがスパムまたはバルクフォルダにある場合。** 多くのプロバイダーは、これらのフォルダではデフォルトでリモート画像（開封ピクセルを含む）を読み込みません。

**対処方法**

- **クリッピング：** HTMLを短縮・簡素化し、未使用のスタイルやアセットを削除し、メッセージ全体のサイズをクライアントの制限内に収めてください。Gmailの場合、[メールサイズ]({{site.baseurl}}/user_guide/channels/email/best_practices/email_styling#email-size)に記載されているように約102&nbsp;KB未満を目指してください。
- **受信トレイセキュリティと画像の読み込み：** デフォルトで画像を読み込むかどうかを変更できるのは、受信者（またはそのITポリシー）のみです。
- **スパム配置：** [メールの到達性の改善]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability)とリストの衛生管理に注力してください。メールが一貫してスパムに振り分けられ、指標がおかしく見える場合は、[Brazeサポート]({{site.baseurl}}/user_guide/administer/personal/braze_support)にお問い合わせください。

**セキュリティまたはボットによるリンクへのアクティビティ**

一部のメールセキュリティ製品は、脅威をスキャンするためにリンクをたどります。これらのリクエストは画像を読み込まずにクリックを記録する可能性があるため、対応する開封なしでクリックアクティビティが表示されることがあります。

##### 延期 {#deferrals}

延期（Deferred/Deferral）とは、メールがすぐに配信されなかったものの、Brazeがこの一時的な配信エラーの後、配信成功の可能性を最大化するためにESPを通じてメールを再試行することを指します。SendGridとSparkPostは最大72時間再試行します。Amazon SESは最大14時間再試行します。延期の一般的な理由には、受信トレイプロバイダーからのレピュテーションに基づくメールボリュームのレート制限、一時的な接続の問題、DNSエラーなどがあります。

_延期_は_ソフトバウンス_とは異なります。この再試行期間中にメールが正常に配信されなかった場合、Brazeは送信されたキャンペーンごとに1つのソフトバウンスイベントを送信します。2025年2月25日以前は、これらの再試行は1回のキャンペーン送信に対して複数のソフトバウンスとしてカウントされていました。

_延期_は現在、CurrentsまたはBraze Snowflake機能（クエリビルダー、SQLセグメント、Snowflakeデータ共有など）を使用した場合のみ利用可能です。キャンペーンやキャンバス分析にこれを含めたい場合は、[製品フィードバックを送信]({{site.baseurl}}/user_guide/administrative/access_braze/portal)してください。

##### 推定実質開封率 {#estimated-real-open-rate}

この統計は、Brazeが独自に作成した分析モデルを使用して、マシン開封が存在しないかのようにキャンペーンのユニーク開封率の推定値を再構築するものです。一部の開封イベントについてメール送信者から*Machine Opens*というラベルを受け取る場合がありますが、これらのラベルは実際の開封をマシン開封と誤って分類することが多いです。つまり、*Other Opens*は（実際のユーザーによる）実際の開封を過小評価している可能性が高いです。代わりに、Brazeは各キャンペーンのクリックデータを使用して、実際の人間がメッセージを開封した率を推測します。これにより、AppleのMPPを含むさまざまなマシン開封メカニズムが補われます。

_推定実質開封率_はメール送信開始から24時間後に算出され、その後72時間ごとに再計算されます。

この指標は継続的に再計算されるため、_推定実質開封率_の値は時間の経過とともに変化する可能性があります。新しいエンゲージメントシグナル（開封やクリックなど）が受信され、モデルに組み込まれるにつれて値は変動します。実際には、_推定実質開封率_はキャンペーンがアクティブな間、毎日更新され続けることがあります。

通常、統計を正常に計算するには配信済みメールが約10,000通必要ですが、この数はクリック率によって異なります。統計が計算できない場合、その列には「--」と表示されます。

###### 注意事項 {#considerations}

推定実質開封率はキャンペーンでのみ利用可能で、Currentsのイベントではレポートされません。この指標は、2023年11月14日以前に開始されたアクティブなキャンペーンにのみ遡及して算出されます。

##### クリック率の増加に対応する {#handling-increases-in-click-rates}

開封率は、メールキャンペーンを追跡するための有益な指標です。ただし、これらの開封率は、メールキャンペーンに対する人間のエンゲージメントを必ずしも正確に示す指標ではありません。定義上、開封イベントはユーザーがメールを開封したときに発生し、透明な開封トラッキングピクセルが正常にダウンロードされたことを意味します。

さらに、セキュリティスキャンツールの使用により開封率が膨張する可能性があります。これらのツールの中には、リンクをクリックしてその正当性を確認することで、受信メールに悪意のあるコンテンツが含まれていないかスキャンしてユーザーを保護するものがあります。これらのクリックは「ボットクリック」または「非人間的インタラクション」（NHI）と呼ばれることがあります。

結局のところ、メールが当社のサーバーを離れた後は、その後何が起きるかについて把握できる範囲は限られていますが、結果に影響するNHIを管理するための推奨事項は以下の通りです：

1. この事象はすべての送信者とほぼすべての受信者に発生する可能性があることに注意してください。クリック数は開封数と同様に、メッセージに対する人間のインタラクションを示す完全に信頼できる指標ではないため、NHIを防ぐことはできません。
2. より高いポジティブなエンゲージメントは、より低いNHIと相関する傾向があるため、メールメッセージングの[ベストプラクティス]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices)に従うことが重要です。これには、ユーザーからメール送信の明示的な許可を得ることや、エンゲージメントのないサブスクライバーを定期的にSunsetting（配信停止）することが含まれます。
3. 可能な限り、メールにHTTPSリンクを使用してください。NHIは安全なリンクを使用する送信者に対してはそれほど一般的に発生しません。
4. ワンクリックで配信停止できる仕組みを使用している場合は、ユーザーが通知設定を編集・管理できるページに誘導する[ユーザー設定センター]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview)の作成を検討してください。NHIによって誤ってユーザーの登録が解除される可能性があるため、これは有用です。
5. コンバージョン数、アプリセッション数、サイト訪問数など、メールマーケティングの成功を測定するために[他の指標]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-performance)の使用も検討してください。
6. メールキャンペーンに隠しリンクを追加します。このリンクは、白地に白のテキストや句読点など、人間が気づかないようなものにします。ボットはすべてのリンクをクリックする傾向があるため、見えないリンクでクリックイベントを生成しているユーザーは実際にはNHIの結果であると結論付けることができます。つまり、その開封やクリックは必ずしもポジティブなエンゲージメントを示しているわけではありません。

{% elsif include.channel == "in-app message" %}

#### アプリ内メッセージ指標 {#in-app-message-metrics}

分析に表示される主なアプリ内メッセージの指標をいくつか紹介します。Brazeで使用されるすべてのアプリ内メッセージ指標の完全な定義については、[レポート指標用語集]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics)を参照してください。

{% alert note %}
*Button 1 Clicks*と*Button 2 Clicks*のレポートは、アプリ内メッセージで**Identifier for Reporting**をそれぞれ「0」と「1」に指定した場合にのみ機能します。

![「Identifier for Reporting」フィールドの値が「0」。]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}
{% endalert %}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="アプリ内メッセージの指標">
    <caption class="sr-only">アプリ内メッセージのパフォーマンス指標</caption>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#body-clicks">Body Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Body Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-1-clicks">Button 1 Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-2-clicks">Button 2 Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">Unique Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">Total Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversions-b-c-d">Conversions (B, C, D)</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-conversions">Total Conversions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversion-rate">Conversion Rate</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#close-message">Close Message</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Close Message' %}</td>
        </tr>
    </tbody>
</table>

#### コントロールグループとバリアント間の差異 {#discrepancies-between-control-groups-and-variants}

アプリ内メッセージキャンペーンでバリアントを50対50に分割した場合、コントロールグループがバリアントよりもわずかに高い割合になることがあります（例：コントロールグループが51%、バリアントが49%）。この差異はレンダリング時間の違いによって生じます。例えば、バリアントメッセージが大きな画像やテンプレート化されたConnected Contentを使用していて、レンダリングが完了する前にユーザーが離脱した場合、コントロールグループはメッセージを表示せずにインプレッションを記録します。

コントロールグループとバリアントグループの分布はほぼ均等になるように意図されていますが、バリアントへの割り当てはアプリ内メッセージが実際にデバイスに送信されたときに行われます。一部のユーザーはアプリ内メッセージをトリガーしない場合があり（例：必要なカスタムイベントをトリガーするアクションを行わない）、これがグループサイズの差異を引き起こす可能性があります。

{% elsif include.channel == "KakaoTalk" %}

### KakaoTalk指標 {#kakaotalk-metrics}

分析に表示される主なKakaoTalk指標をいくつか紹介します。詳細については、[レポート指標用語集]({{site.baseurl}}/user_guide/data/report_metrics)を参照してください。

{% alert note %}
現在、KakaoTalkキャンペーンでは推定または正確なオーディエンス統計は利用できません。
{% endalert %}

| 用語 | 定義 |
| --- | --- |
| オーディエンス | *オーディエンス*は、特定のメッセージを受信したユーザーの割合です。<br><br>*（バリアント内の受信者数）/（ユニーク受信者数）* |
| ユニーク受信者数 | *ユニーク受信者数*は、1日あたりのユニーク受信者数、つまり1日に新しいメッセージを受信したユーザー数です。このカウントがユーザーに対して複数回増加するには、ユーザーが別の日に新しいメッセージを受信する必要があります。この数値は`user_id`に基づいています。詳細については、[レポート指標用語集のユニーク受信者数]({{site.baseurl}}/user_guide/data/report_metrics#unique-recipients)を参照してください。 |
| 送信数 | キャンペーンで送信されたメッセージの総数です。これはメッセージがデバイスに受信または配信されたことを意味するものではなく、メッセージが送信されたことのみを示します。 |
| クリック数の合計 | 送信されたKakaoTalkメッセージがユーザーによってクリックされた合計回数です。 |
| エラー数 | *エラー数*は、KakaoTalkプロバイダーから返されたエラーの数です（送信プロセス中に増加します）。 |
| 収益 | *収益*は、設定された1次コンバージョン期間内のキャンペーン受信者からのドル建て収益です。 |
| 1次コンバージョン数 | *1次コンバージョン数*は、Brazeキャンペーンから受信したメッセージを操作または閲覧した後に、定義されたイベントが発生した回数です。この定義されたイベントは、キャンペーン構築時に設定します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="KakaoTalkの指標" }

{% elsif include.channel == "push" %}

#### プッシュ指標 {#push-metrics}

以下は、メッセージのパフォーマンスを確認する際に表示される主な指標の内訳です。すべてのプッシュ指標の完全な定義については、[レポート指標用語集]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics)を参照し、プッシュでフィルタリングしてください。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="プッシュの指標">
    <caption class="sr-only">プッシュのパフォーマンス指標</caption>
    <thead>
        <tr>
            <th>指標</th>
            <th>説明</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">Bounces</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %} <a href="#bounced-push">バウンスしたプッシュ通知</a> を参照してください。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#direct-opens">Direct Opens</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opens">Opens</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opens' %}</td>
        </tr>
    </tbody>
</table>

> 通知の配信は、Appleプッシュ通知サービス（APNs）による「ベストエフォート」です。アプリにデータを配信することを目的としておらず、新しいデータが利用可能であることをユーザーに通知することのみを目的としています。重要な違いは、APNsがデバイスに正常に配信した数ではなく、APNsに正常に配信されたメッセージの数が表示されることです。

##### 配信停止の追跡 {#tracking-unsubscribes}

プッシュ通知の配信停止はキャンペーン分析の指標に含まれておらず、AppleやGoogleなどのプロバイダーによるユーザーのプッシュステータスの更新に依存します。これらの更新は頻度が低く、予測不可能な場合があります。そのため、プッシュの配信停止はプッシュキャンペーン分析の指標として含まれていません。

ただし、手動でプッシュの配信停止を追跡することで、通知の頻度やコンテンツの関連性に対するユーザーの反応について貴重なインサイトを得ることができます。プッシュの配信停止を追跡する方法は2つあります：セグメントフィルターまたはカスタムフィルターを使用する方法です。

{% tabs local %}
{% tab セグメントフィルター %}

プッシュが有効になっていないユーザー、つまりサブスクライブまたはオプトインしておらず、[フォアグラウンドプッシュトークン]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration#push-tokens)を持っていないユーザーを識別するセグメントを作成できます。例えば、アプリ内の配信停止数を確認するには、以下のセグメントを「OR」条件で組み合わせます：

- `Background or Foreground Push Enabled is false`
- `Has Uninstalled`

![アプリに対する「Background or Foreground Push Enabled」フィルターがfalseであり、「Has Uninstalled」フィルターが選択されているセグメントビルダーセクション。]({% image_buster /assets/img/push_unsub_segment_example.png %})

セグメンテーションフィルターはおおよその目安であり、特定の日付やキャンペーンに結びつけることはできません。

{% endtab %}
{% tab カスタムフィルター %}

{% alert important %}
サブスクリプション変更のカスタムイベントをログに記録すると、[データポイント]({{site.baseurl}}/user_guide/data_and_analytics/data_points#consumption-count)が消費されます。または、セグメントフィルターを使用して、プッシュが有効になっていないユーザーを識別し、ターゲットにしてください。
{% endalert %}

別の回避策として、この指標を追跡するために、ユーザーのプッシュ有効ステータスが`true`か`false`かに基づいて、プッシュの配信停止のカスタムイベントを作成することもお勧めします。

{% endtab %}
{% endtabs %}

##### 開封を把握する {#understanding-opens}

*Direct Opens*と*Influenced Opens*には「開封」という言葉が含まれていますが、実際には異なる指標です。*Direct Opens*はプッシュ通知を直接開封することを指します。*Influenced Opens*は、プッシュ通知を受け取った後、特定の時間内にプッシュ通知を開かずにアプリを開封することを指します。つまり、*Influenced Opens*はアプリの開封を指し、プッシュ通知の開封ではありません。

##### プッシュアクションボタンとレポート {#push-action-buttons-and-reporting}

[プッシュアクションボタン]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons)を追加すると、**プッシュパフォーマンス**パネルに**Direct Opens**などの指標とともに、**Body Clicks**、**Button 1 Clicks**、**Button 2 Clicks**が表示されます。これらの列は異なるインタラクションを測定するため、エンゲージメントを解釈する際に比較してください。

_Direct Opens_は、メッセージの直接開封としてカウントされるインタラクションのダッシュボード指標を反映します。[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)またはSnowflakeの**Push Notification Open**イベントは、プッシュインタラクションをより広範に記述し、`button_action_type`（例：`close`）や`button_string`などのオプションフィールドを含むことがあります。フィールドの定義については、[Push Notification Openイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#push-notification-open-events)を参照してください。

**iOS**の場合、Brazeのデフォルト通知カテゴリ（**Yes** / **No**、**Accept** / **Decline**、**Confirm** / **Cancel**など）は固定のペアリングを使用します。最初のアクションは`OPEN_APP`、URI、またはディープリンクをサポートし（コンポーザーの**On-Click Behavior**に対応）、もう一方のアクションはデフォルトで`CLOSE`を使用します。これは通知を閉じ、アプリを開きません。デフォルトのマッピングについては、[Apple push action button object]({{site.baseurl}}/api/objects_filters/messaging/apple_object#apple-push-action-button-object-for-braze-default-buttons)を参照してください。

そのため、閉じるプリセットボタン（例：**No**や**Decline**）のタップは通常、_Direct Opens_にはカウントされません。これらのタップは、ログに記録された場合、`button_action_type`が`close`に設定され、`button_string`がタップされたアクションを識別する形で**Push Notification Open**エクスポートに表示されることがあります。キャンペーン分析とウェアハウスデータを比較する際は、これらのペイロードフィールドを使用して、閉じるタップを通知本文やプライマリアクションのタップと同じように扱わないようにしてください。

**Android**の場合、ボタンごとに**On-Click Behavior**（**Open App**、**Redirect to Web URL**、**Deep Link**）を設定するため、レポートはiOSのデフォルトの`OPEN_APP` / `CLOSE`分割ではなく、設定したアクションに従います。

##### プッシュ通知の送信数がユニーク受信者数を超える可能性がある理由 {#why-push-sends-can-exceed-unique-recipients}

以下の理由により、_送信数_が_ユニーク受信者数_を上回る場合があります：

- **再適格性がオンになっている：** キャンペーンまたはキャンバスの設定で再適格性が有効になっている場合、セグメントと配信条件を満たすユーザーは同じプッシュ通知を複数回受け取ることができます。その結果、総送信数が多くなります。
- **ユーザーが複数のデバイスを持っている：** 再適格性が有効になっていない場合、ユーザーが複数のデバイスをプロファイルに関連付けていることで差異が説明される場合があります。例えば、ユーザーがスマートフォンとタブレットの両方を持っていて、プッシュ通知が登録されたすべてのデバイスに送信される場合です。各配信は送信としてカウントされますが、ユニーク受信者は1人のみ記録されます。
- **ユーザーが複数のアプリに割り当てられている：** ユーザーが複数のアプリに関連付けられている場合（新しいアプリのテスト時など）、それぞれのアプリで同じプッシュ通知を受け取ることがあります。これが送信数の増加につながります。

##### バウンスが発生する理由 {#bounced-push}

{% tabs %}
{% tab Appleプッシュ通知サービス %}

バウンスは、Appleプッシュ通知サービス（APNs）において、プッシュ通知が対象のアプリがインストールされていないデバイスに配信されようとするときに発生します。APNsはまた、デバイスのトークンを任意に変更する権利を持っています。以前にトークンを登録した時点（各セッション開始時にユーザーのプッシュトークンを登録する場合など）から送信時刻までの間にプッシュトークンが変更されたユーザーのデバイスに送信しようとすると、バウンスが発生します。

ユーザーが次回のアプリ開封時にデバイス設定でプッシュを無効にした場合、SDKはプッシュが無効にされたことを検知し、Brazeに通知します。この時点で、プッシュ有効状態を無効に更新します。無効化されたユーザーが新しいセッションを持つ前にプッシュキャンペーンを受信すると、キャンペーンは正常に送信され、配信されたように表示されます。このユーザーに対してプッシュがバウンスすることはありません。その後のセッションで、ユーザーにプッシュを送信しようとすると、Brazeはフォアグラウンドトークンがあるかどうかを既に認識しているため、通知は送信されません。

配信前に期限切れとなったプッシュ通知は失敗とはみなされず、バウンスとして記録されることもありません。

{% endtab %}
{% tab Firebase Cloud Messaging %}

Firebase Cloud Messaging（FCM）のバウンスは3つのケースで発生する可能性があります：

| シナリオ | 説明 |
| -- | -- |
| アンインストールされたアプリケーション | メッセージがデバイスに配信されようとして、そのデバイスで対象のアプリがアンインストールされている場合、メッセージは破棄され、デバイスの登録IDは無効になります。今後そのデバイスにメッセージを送信しようとすると、NotRegisteredエラーが返されます。 |
| バックアップされたアプリケーション | アプリケーションがバックアップされると、アプリケーションが復元される前に登録IDが無効になる可能性があります。この場合、FCMはアプリケーションの登録IDを保存しなくなり、アプリケーションはメッセージを受信しなくなります。そのため、アプリケーションのバックアップ時に登録IDを保存すべきでは**ありません**。 |
| 更新されたアプリケーション | アプリケーションが更新されると、以前のバージョンの登録IDが使えなくなることがあります。そのため、更新されたアプリケーションは既存の登録IDを置き換える必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="バウンスが発生する理由" }

{% endtab %}
{% endtabs %}


{% elsif include.channel == "SMS" %}

#### SMS、MMS、RCS指標 {#sms-mms-and-rcs-metrics}

以下は、メッセージのパフォーマンスを確認する際に表示される主な指標の内訳です。すべてのSMS、MMS、RCS指標の完全な定義については、[レポート指標用語集]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics)を参照し、SMS/MMSおよびRCSでフィルタリングしてください。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="SMS、MMS、RCSの指標">
    <caption class="sr-only">SMS、MMS、RCSのパフォーマンス指標</caption>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sent">Sent</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sent' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#delivery-failures">Delivery Failures</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confirmed-delivery">Confirmed Delivery</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#rejections">Rejections</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Rejections' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opt-out">Opt-Out</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opt-Out' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#help">Help</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">Total Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "webhook" %}

#### Webhook指標 {#webhook-metrics}

分析に表示される主なWebhook指標をいくつか紹介します。Brazeで使用されるすべてのWebhook指標の完全な定義については、[レポート指標用語集]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics)を参照してください。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Webhookの指標">
    <caption class="sr-only">Webhookのパフォーマンス指標</caption>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">Unique Recipients</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">Sends</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#errors">Errors</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Errors' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "whatsapp" %}

#### WhatsApp指標 {#whatsapp-metrics}

分析に表示される主なWhatsApp指標をいくつか紹介します。Brazeで使用されるすべてのWhatsApp指標の完全な定義については、[レポート指標用語集]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics)を参照してください。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="WhatsAppの指標">
    <caption class="sr-only">WhatsAppのパフォーマンス指標</caption>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">Sends</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deliveries">Deliveries</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#reads">Reads</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Reads' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#failures">Failures</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Failures' %}</td>
        </tr>
    </tbody>
</table>

#### エンドユーザーのブロックとレポートの指標 {#end-user-blocking-and-reporting-metrics}

追加の指標には[WhatsAppマネージャーダッシュボード](https://www.facebook.com/business/help/683499390267496?content_id=NZUBj7XjkYjYuWx)からアクセスできますが、利用可能なすべてのインサイトにアクセスするには[アクセス権の確認](https://www.facebook.com/business/help/218116047387456)が必要です。

{% endif %}

### 過去のパフォーマンス {#historical-performance}

**過去のパフォーマンス**パネルでは、**メッセージパフォーマンス**パネルの指標を時系列のグラフとして表示できます。パネル上部のフィルターを使用して、グラフに表示される統計やチャネルを変更します。このグラフの時間範囲は、常にページ上部で指定された時間範囲を反映します。

日ごとの内訳を取得するには、<i class="fas fa-bars"></i>ハンバーガーメニューをクリックし、**CSVダウンロード**を選択してレポートのCSVエクスポートを受け取ります。

![2021年2月から2022年5月までのメールに関する統計例を示す過去のパフォーマンスパネルのグラフ。]({% image_buster /assets/img/cc-historical-performance.png %})

{% if include.channel == "in-app message" %}

{% alert note %}
最新バージョンのBrazeのアプリ内メッセージ（第3世代）を表示できるユーザーにのみ送信することを選択した場合、**ターゲットオーディエンス**は選択内容を反映するようには調整されません。
{% endalert %}

{% endif %}

{% if include.channel == "SMS" %}

### キーワード応答 {#keyword-responses}

**キーワード応答**パネルには、メッセージ受信後にユーザーが返信した受信キーワードのタイムラインが表示されます。

![キャンペーンレベルのSMS/MMS/RCSキーワード応答パネル。時間経過に伴うキーワード分布の折れ線グラフと、キーワードカテゴリセクション（オプトイン、オプトアウト、ヘルプ、その他、詳細、コーチングのチェックボックスが選択されている）が含まれます。]({% image_buster /assets/img/sms/keyword_responses.png %})

ここでは、[リターゲティング]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns)の次のステップを決定し、便利に[セグメントを作成]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment)するために、各キーワードカテゴリの応答分布を確認することもできます。

![キーワードカテゴリ、応答分布、リターゲティングの列を持つテーブル。キーワードカテゴリでセグメントを作成するオプションが提供されています。]({% image_buster /assets/img/sms/keyword_segments.png %})

{% endif %}

### コンバージョンイベントの詳細 {#conversion-event-details}

**コンバージョンイベントの詳細**パネルには、キャンペーンのコンバージョンイベントのパフォーマンスが表示されます。詳細については、[コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events#step-3-view-results)を参照してください。

![コンバージョンイベントの詳細パネル。]({% image_buster /assets/img/cc-conversion.png %})

### コンバージョンの相関 {#conversion-correlation}

**コンバージョンの相関**パネルでは、どのようなユーザー属性と行動がキャンペーンに設定した結果に役立つか、または悪影響を与えるかを把握できます。詳細については、[コンバージョンの相関]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation)を参照してください。

![1次コンバージョンイベントAからのユーザー属性と行動に関する分析を含むコンバージョンの相関パネル。]({% image_buster /assets/img/convcorr.png %})

{% if include.channel == "KakaoTalk" %}

## レポートビルダー {#report-builder}

[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reporting/report_builder)を使用して、KakaoTalkキャンペーンのカスタムレポートを作成することもできます。レポートを作成する際、**チャネル**で**KakaoTalk**を選択するか、KakaoTalkキャンペーンに適用したタグでフィルタリングすることで、KakaoTalkキャンペーンのみを含めるようにフィルタリングできます。

{% endif %}

{% if include.channel == "whatsapp" %}

### Meta分析 {#meta-analytics}

Brazeの分析に加えて、WhatsAppビジネスマネージャーでテンプレートレベルの分析にもアクセスできます。詳細については、[Metaのドキュメント](https://www.facebook.com/business/help/218116047387456)を参照してください。

{% endif %}

{% if include.channel == "SMS" %}

### SMS Currentsイベント {#sms-currents-events}

メールと同様に、BrazeはSMSメッセージがユーザーに届く過程で、メッセージに関連するユーザーレベルのイベントを受信します。受信SMSイベントはすべて、[SMS InboundReceived]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events)イベントを通じてCurrentsイベントとしても送信されます。これにより、ユーザーがBrazeプラットフォーム外でテキスト入力したメッセージに対して、追加のアクションやレポートを実行できます。

{% alert note %}
受信メッセージは1,600文字を超えると切り捨てられます。
{% endalert %}

{% endif %}

{% if include.channel != "whatsapp" %}

## リテンションレポート {#retention-report}

リテンションレポートには、特定のキャンペーン{% if include.channel != "banner" %}またはキャンバス{% endif %}において、指定した期間にユーザーが選択したリテンションイベントを実行した割合が表示されます。詳細については、[リテンションレポート]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports)を参照してください。

## 目標到達プロセスレポート {#funnel-report}

目標到達プロセスレポートは、キャンペーン{% if include.channel != "banner" %}またはキャンバス{% endif %}を受け取った後の顧客のジャーニーを分析できるビジュアルレポートを提供します。キャンペーン{% if include.channel != "banner" %}またはキャンバス{% endif %}でコントロールグループや複数のバリアントを使用している場合、異なるバリアントがコンバージョンファネルにどのような影響を与えたかをより細かいレベルで理解し、このデータに基づいて最適化できます。

詳細については、[目標到達プロセスレポート]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports)を参照してください。

{% endif %}