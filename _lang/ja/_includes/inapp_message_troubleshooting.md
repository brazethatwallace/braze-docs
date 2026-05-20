## 基本チェック {#basic-checks}

### あるユーザーにアプリ内メッセージが表示されない {#my-in-app-message-wasnt-shown-for-one-user}

1. SDKが新しいアプリ内メッセージをリクエストするセッション開始時に、ユーザーはセグメントに含まれていましたか？
2. キャンペーンのターゲティングルールに基づいて、ユーザーはアプリ内メッセージを受信する資格がありましたか、または再資格がありましたか？
3. ユーザーはフリークエンシーキャップの影響を受けましたか？
4. ユーザーはコントロールグループに含まれていましたか？キャンペーンがABテスト用に設定されているか確認してください。
5. 期待されたメッセージの代わりに、より優先度の高い別のアプリ内メッセージが表示されましたか？
6. デバイスはキャンペーンで指定された正しい向きになっていましたか？
7. SDKによって適用される、トリガー間のデフォルトの30秒の最小時間間隔によってメッセージが抑制されましたか？

### このプラットフォームですべてのユーザーにアプリ内メッセージが表示されなかった {#my-in-app-message-wasnt-shown-to-all-users-on-this-platform}

1. キャンペーンは、モバイルアプリまたはWebブラウザのいずれかを適切にターゲットとするように設定されていますか？例えば、キャンペーンがWebブラウザのみをターゲットにしている場合、Androidデバイスには送信されません。
2. カスタムUIを実装していますか？意図したとおりに機能していますか？他のアプリ側のカスタム処理や抑制が表示を妨げていませんか？
3. この特定のプラットフォームとアプリのバージョンで、アプリ内メッセージが正常に表示されたことはありますか？
4. トリガーはデバイスのローカルで発生しましたか？RESTコールを使用してSDKのアプリ内メッセージをトリガーすることはできません。

### すべてのユーザーにアプリ内メッセージが表示されなかった {#my-in-app-message-wasnt-shown-for-all-users}

1. ダッシュボードおよびアプリの連携で、トリガーアクションは適切に設定されていましたか？
2. 期待されたメッセージの代わりに、より優先度の高い別のアプリ内メッセージが表示されましたか？
3. SDKのバージョンは最新ですか？アプリ内メッセージの種類によってはSDKのバージョン要件があります。
4. セッションは連携で適切に統合されていますか？このアプリでセッション分析は機能していますか？
5. カスタマイズされたコンポーネントライブラリーを使用していませんか？アプリ内メッセージの表示に干渉している可能性があります。

### アプリ内メッセージの表示に時間がかかった {#my-in-app-message-took-a-lot-of-time-to-appear}

1. CDNからHTMLベースのアプリ内メッセージに大きな画像や動画ファイルを配信している場合は、ファイルが可能な限り小さくなるように最適化されていること、およびCDNのパフォーマンスが高いことを確認してください。
2. ダッシュボードでアプリ内メッセージに `delay` を設定していないか確認してください。
{% case include.sdk %}
  {% when "iOS", "Android" %}
3. 状況に応じて、アプリ内メッセージは表示前に関連画像をダウンロードするか、ディスクから読み込みます。低速のネットワーク接続や非常にパフォーマンスの低いデバイスを使用している場合、この処理に時間がかかることがあります。画像ができるだけ小さくなるように最適化されていることを確認してください。
{% endcase %}

これらのシナリオの詳細については、<a id="troubleshooting-in-app-advanced">高度なトラブルシューティングのセクション</a>を参照してください。

## インプレッションとクリック分析の問題 {#issues-with-impressions-and-click-analytics}

{% if include.sdk == "iOS" %}
### インプレッションとクリックが記録されない {#impressions-and-clicks-arent-being-logged}

メッセージ表示またはクリックアクションを手動で処理するようにアプリ内メッセージデリゲートを設定している場合は、アプリ内メッセージの[クリック数](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:))と[インプレッション](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logimpression(using:))を手動で記録する必要があります。
{% elsif include.sdk == "Android" %}
### インプレッションとクリックが記録されない {#impressions-and-clicks-arent-being-logged}
メッセージ表示やクリックアクションを手動で処理するようにアプリ内メッセージデリゲートを設定している場合は、アプリ内メッセージのクリック数やインプレッションを手動で記録する必要があります。
{% endif %}

### *インプレッション*が*ユニークインプレッション*より多い {#impressions-are-greater-than-unique-impressions}

これは想定される動作であり、以下の場合に発生する可能性があります。

- 再資格がオフになっていても、キャンペーンを受信したユーザーが複数のデバイスを持っている場合があります。キャンペーンのトリガーは次のセッション開始時に更新されるため、別のデバイスが既にキャンペーンをトリガーしたかどうかは、ユーザーが新しいセッションを開始するまでわかりません。
- アプリ内メッセージにトリガーイベント発生後数分間のスケジュール遅延が設定されている場合、ユーザーがメッセージを複数回受信した可能性があります。

再資格の詳細については、[キャンペーンとキャンバスの再資格]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/)を参照してください。

### インプレッションが予想より低い {#impressions-are-lower-than-expected}

1. トリガーはセッション開始時にデバイスへの同期に時間がかかるため、ユーザーがセッション開始直後にイベントや購入を記録すると競合が発生する可能性があります。考えられる回避策の1つは、キャンペーンをセッション開始でトリガーするように変更し、目的のイベントまたは購入でセグメント化することです。なお、イベント発生後の次回セッション開始時にアプリ内メッセージが配信されることに注意してください。

2. キャンペーンがセッション開始やカスタムイベントによってトリガーされる場合、このイベントやセッションがメッセージをトリガーするのに十分な頻度で発生していることを確認する必要があります。このデータを[概要]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#understanding-your-app-usage-data)（セッションデータの場合）または[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting)ページで確認してください。

![カスタムイベントページには、カスタムイベント「お気に入りに追加」が1か月間に発生した回数のグラフが表示されています]({% image_buster /assets/img_archive/trouble5.png %})

その他の理由として以下が考えられます。

- ユーザーがアプリ内メッセージを閲覧していないため、インプレッションが記録されていない。
- 複数のアプリ内メッセージが互いに干渉している（優先度の高いメッセージが複数ある場合など）。
- メッセージがキャンバス内にある場合、ユーザーがアプリ内メッセージを受信する前に、セッションタイムアウトより長い遅延ステップに入っている可能性がある。

### インプレッションが以前より低下している {#impressions-are-lower-than-they-used-to-be}

1. ローンチ後、誰も意図せずにセグメントやキャンペーンを変更していないことを確認してください。セグメントとキャンペーンの変更ログから、いつ、誰が、どのような変更を行ったかについてインサイトを得ることができます。

![キャンペーン詳細ページで、ユーザーがキャンペーンを最後に閲覧してからの7つの変更点を含む変更ログを表示するためのリンク]({% image_buster /assets/img_archive/trouble4.png %})

{: start="2"}
2. トリガーイベントを、優先度の高い別のアプリ内メッセージキャンペーンで再利用していないことを確認してください。

## 高度なトラブルシューティング {#troubleshooting-in-app-advanced}

ほとんどのアプリ内メッセージの問題は、配信と表示の2つの主要なカテゴリに分けることができます。期待したアプリ内メッセージがデバイスに表示されなかった原因をトラブルシューティングするには、<a id="troubleshooting-in-app-message-delivery">アプリ内メッセージがデバイスに配信された</a>ことを確認してから、<a id="troubleshooting-in-app-message-display">メッセージ表示のトラブルシューティング</a>を行います。

### 配信のトラブルシューティング {#troubleshooting-in-app-message-delivery}

SDKはセッション開始時にBrazeサーバーからアプリ内メッセージをリクエストします。アプリ内メッセージがデバイスに配信されているかどうかを確認するには、アプリ内メッセージがSDKによってリクエストされ、Brazeサーバーによって返されていることを確認する必要があります。

#### メッセージがリクエストされ、返されたかどうかを確認する {#check-if-messages-are-requested-and-returned}

1. ダッシュボードで自分自身を[テストユーザー]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users)として追加します。
2. ユーザーをターゲットとしたアプリ内メッセージキャンペーンを設定します。
3. アプリケーションで新しいセッションが発生することを確認します。
4. [イベントユーザーログ]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab)を使用して、セッション開始時にデバイスがアプリ内メッセージをリクエストしていることを確認します。テストユーザーのセッション開始イベントに関連付けられたSDKリクエストを見つけてください。
  - トリガーされたアプリ内メッセージをリクエストするためのアプリであれば、**Response Data**の**Requested Responses**フィールドに `trigger` が表示されます。
  - アプリが元のアプリ内メッセージをリクエストするためのものだった場合、**Response Data**の**Requested Responses**フィールドに `in_app` が表示されます。
5. [イベントユーザーログ]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab)を使用して、応答データに正しいアプリ内メッセージが返されているか確認します。<br>![]({% image_buster /assets/img_archive/event_user_log_iams.png %})

##### リクエストされていないメッセージのトラブルシューティング {#troubleshoot-messages-not-being-requested}

アプリ内メッセージがリクエストされていない場合、アプリ内メッセージはセッション開始時にリフレッシュされるため、アプリがセッションを正しくトラッキングしていない可能性があります。また、アプリのセッションタイムアウトのセマンティクスに基づいて、アプリが実際にセッションを開始していることを確認してください。

![イベントユーザーログに記録されたSDKリクエストは、セッション開始イベントが成功したことを示しています。]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

##### メッセージが返されない問題のトラブルシューティング {#troubleshoot-messages-not-being-returned}

アプリ内メッセージが返されない場合、キャンペーンターゲティングの問題が発生している可能性があります。

1. セグメントにユーザーが含まれていない。
  - ユーザーの[**エンゲージメント**]({{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab)タブを確認し、**セグメント**欄に正しいセグメントが表示されているか確認してください。
2. ユーザーが以前にアプリ内メッセージを受信しており、再度受信する資格がなかった。
  - **キャンペーン Composer**の**Delivery**ステップにある[キャンペーン再資格設定]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/)を確認し、再資格設定がテスト設定と一致していることを確認してください。
3. ユーザーがキャンペーンのフリークエンシーキャップに達した。
  - キャンペーンの[フリークエンシーキャップ設定]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping)を確認し、テスト設定と一致していることを確認してください。
4. キャンペーンにコントロールグループが存在した場合、ユーザーがコントロールグループに分類された可能性があります。
  - キャンペーンバリアントが**Control**に設定されている受信キャンペーンバリアントフィルターでセグメントを作成し、ユーザーがそのセグメントに分類されたかどうかを確認することで、これが発生したかどうかを確認できます。
  - 連携テスト目的でキャンペーンを作成する場合は、コントロールグループの追加をオプトアウトしてください。


### 表示のトラブルシューティング {#troubleshooting-in-app-message-display}

アプリがアプリ内メッセージのリクエストと受信に成功しているにもかかわらず表示されない場合、デバイス側のロジックが表示を妨げている可能性があります。

1. トリガーイベントは想定どおりに発生していますか？これをテストするには、メッセージを別のアクション（セッション開始など）でトリガーするように設定し、表示されるかどうかを確認してください。
{% if include.sdk == "iOS" %}
2. トリガーされたアプリ内メッセージは、[トリガー間の最小時間間隔]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers)（デフォルトは30秒）に基づいてレート制限されます。
{% elsif include.sdk == "Android" %}
2. トリガーされたアプリ内メッセージは、[トリガー間の最小時間間隔]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers)（デフォルトは30秒）に基づいてレート制限されます。
{% elsif include.sdk == "Web" %}
2. トリガーされたアプリ内メッセージは、[トリガー間の最小時間間隔]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers)（デフォルトは30秒）に基づいてレート制限されます。
{% endif %}
3. 画像のダウンロードに失敗すると、画像付きのアプリ内メッセージが表示されなくなります。デバイスのログを確認して、画像のダウンロードに失敗していないか確認してください。メッセージから画像を一時的に削除して、それで表示されるかどうか試してみてください。
{% case include.sdk %}
  {% when "iOS", "Android" %}
4. アプリ内メッセージ処理をカスタマイズするようにデリゲートを設定している場合は、デリゲートがアプリ内メッセージの表示に影響していないことを確認してください。
  {% when "Web" %}
5. `braze.subscribeToInAppMessage` または `appboy.subscribeToNewInAppMessages` を介してカスタムのアプリ内メッセージ処理を行っている場合は、そのサブスクリプションがアプリ内メッセージの表示に影響を及ぼしていないことを確認してください。
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
6. デバイスの向きがアプリ内メッセージで指定された向きと一致しない場合、アプリ内メッセージは表示されません。デバイスの向きが正しいことを確認してください。
{% endcase %}
7. アプリ内メッセージがセッション開始によってトリガーされ、拡張セッションタイムアウトが設定されている場合、メッセージが表示される速さに影響します。例えば、セッションタイムアウトが300秒に設定されている場合、それ未満の時間でアプリを閉じて再度開いてもセッションはリフレッシュされないため、セッション開始でトリガーされるアプリ内メッセージは表示されません。