リンク短縮を使用すると、SMSまたはRCSメッセージに含まれるURLを自動的に短縮し、クリックスルー率の分析を収集できます。これにより、追加のエンゲージメント指標が提供され、ユーザーがキャンペーンにどのように関わっているかを理解するのに役立ちます。

リンク短縮は、キャンペーンとキャンバスの両方で[メッセージバリアントレベル]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#step-1-create-your-campaign)で有効にできます。リンク短縮が有効になると、クリックによりCurrentsを通じて送信される[SMSクリックイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)が生成されます。

{% multi_lang_include channels/sms/rcs_link_shortening_note.md %}

リンクは共有ショートドメイン（`brz.ai`）またはカスタムリンク短縮ドメインを使用して短縮され、作成日から9週間有効です。URLの例は `https://brz.ai/8jshX2dj` のようになります。

## リンク短縮の使用 {#using-link-shortening}

リンク短縮を使用するには、メッセージ作成画面のリンク短縮チェックボックスが選択されていることを確認してください。

{% tabs %}
{% tab SMS composer %}

![リンク短縮のチェックボックスが選択されたSMSメッセージ作成画面。]({% image_buster /assets/img/link_shortening/shortening1.png %}){: width="1562" height="1068"}

{% endtab %}
{% tab RCS composer %}

![リンク短縮のチェックボックスが選択されたRCSメッセージ作成画面。]({% image_buster /assets/img/link_shortening/shortening1_rcs.png %}){: width="1476" height="1222"}

{% endtab %}
{% endtabs %}

Brazeは`http://`または`https://`で始まるURLのみを認識します。URLが認識されると、**プレビュー**セクションにプレースホルダーURLが表示されます。Brazeは短縮後のメッセージの長さを推定しますが、より正確な推定のために、テストユーザーを選択してメッセージを下書きとして保存するよう警告が表示されます。

![「メッセージ」ボックスに長いURLがあり、プレビューに生成された短縮リンクが表示されているメッセージ作成画面。]({% image_buster /assets/img/link_shortening/shortening3.png %}){: width="1552" height="612"}

### UTMパラメーターの追加 {#adding-utm-parameters}

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## URLでのLiquidパーソナライゼーション {#liquid-personalization-in-urls}

Brazeのメッセージ作成画面内で直接URLを動的に構築し、ダイナミックなUTMパラメーターをURLに追加したり、ユーザーにユニークなリンクを送信したりする方法については、[URLでLiquidパーソナライゼーションを使用する]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#use-liquid-personalization-in-urls)を参照してください。

## テスト {#testing}

キャンペーンやキャンバスを開始する前に、まずメッセージをプレビューしてテストすることをお勧めします。これを行うには、**テスト**タブに移動して、SMSまたはRCSメッセージを[コンテンツテストグループ]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups)または個々のユーザーにプレビューして送信します。

このプレビューは、関連するパーソナライゼーションと短縮URLで更新されます。文字数と[課金対象セグメント]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator)も、レンダリングされたパーソナライゼーションと短縮URLを反映して更新されます。

テストメッセージを送信する前にキャンペーンまたはキャンバスを保存して、メッセージで配信される短縮URLの表示を受け取るようにしてください。テスト送信前にキャンペーンまたはキャンバスが保存されていない場合、テスト送信にはプレースホルダーURLが含まれます。

{% alert important %}
アクティブなキャンバス内で下書きが作成された場合、短縮URLは生成されません。実際の短縮URLは、キャンバスの下書きがアクティブになったときに生成されます。
{% endalert %}

![テスト受信者を選択するフィールドがあるメッセージの「テスト」タブ]({% image_buster /assets/img/link_shortening/shortening2.png %}){: width="1544" height="1140"}

{% alert note %}
Liquidパーソナライゼーションと短縮URLは、ユーザーが選択された後に**テスト**タブでテンプレート化されます。正確な文字数を取得するために、ユーザーが選択されていることを確認してください。
{% endalert %}

## クリックトラッキング {#click-tracking}

リンク短縮がオンになっている場合、**SMS/MMS/RCSパフォーマンス**テーブルには**合計クリック数**という列が含まれ、バリアントごとのクリックイベント数と関連するクリック率が表示されます。指標の詳細については、[メッセージパフォーマンス]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting)を参照してください。

![SMSおよびMMSパフォーマンス指標テーブル。]({% image_buster /assets/img/link_shortening/shortening4.png %}){: width="1586" height="191"}

**過去のパフォーマンス**テーブルと**SMS/MMS/RCSパフォーマンス**テーブルにも**合計クリック数**のオプションがあり、クリックイベントの日次時系列が表示されます。クリックはリダイレクト時（ユーザーがリンクにアクセスした場合など）にカウントされ、1人のユーザーに対して複数回カウントされることがあります。

## ユーザーのリターゲティング {#retargeting-users}

リターゲティングのガイダンスについては、[リターゲティング]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting#filter-by-advanced-tracking-links)をご覧ください。

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### URLをクリックした個々のユーザーを特定できますか？ {#do-i-know-which-individual-users-are-clicking-on-a-url}

はい。[SMSリターゲティングフィルター]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting)またはCurrentsから送信されるSMSクリックイベント（`users.messages.sms.ShortLinkClick`）を使用して、URLをクリックしたユーザーをリターゲティングできます。

### リンク短縮はディープリンクやユニバーサルリンクで機能しますか？ {#does-link-shortening-work-with-deep-links-or-universal-links}

リンク短縮はディープリンクでは機能しません。代替手段として、BranchやAppsFlyer などのサードパーティプロバイダーのユニバーサルリンクを短縮することは可能ですが、ユーザーに短時間のリダイレクトや「ちらつき」が発生する場合があります。これは、短縮リンクがアプリの起動をサポートするユニバーサルリンクに解決される前に、まずWeb経由でルーティングされるためです。また、ユニバーサルリンクを短縮した際に発生する可能性のある問題（アトリビューションの破損や予期しないリダイレクトなど）について、Brazeではトラブルシューティングができません。

{% alert note %}
ユニバーサルリンクでリンク短縮を実装する前に、期待どおりの動作であることを確認するためにユーザーエクスペリエンスをテストしてください。
{% endalert %}

### `send_ids`はSMSクリックイベントに関連付けられていますか？ {#are-send_ids-associated-with-sms-click-events}

いいえ。ただし、一般的には[クエリビルダー]({{site.baseurl}}/query_builder)を使用して、以下のクエリでCurrentsデータを照会することにより、`send_ids`をクリックイベントに関連付けることができます。

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL;
```