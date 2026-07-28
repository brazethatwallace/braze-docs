---
nav_title: トラブルシューティング
article_title: Braze SDKのアプリ内メッセージのトラブルシューティング
page_order: 50
description: "症状インデックス、標準的な調査パス、キャンバスのIn-App Messagesに関する注意事項、プラットフォーム固有のSDKチェックを使用して、アプリ内メッセージが配信または表示されない原因を診断します。"
channel:
  - in-app messages

---

# アプリ内メッセージのトラブルシューティング {#troubleshoot-in-app-messages}

> このページでは、アプリ内メッセージがデバイスに配信または表示されない原因を診断します。ダッシュボード側の設定（優先度、トリガー、セグメント、再適格性）については、[アプリ内メッセージFAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq)を参照してください。

デバッグを始める前に、自分自身を[テストユーザー]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users)として追加し、[テストメッセージの送信]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages)を確認してください。

## まずはここから：症状を確認する {#start-here-match-your-symptom}

| 症状 | 参照先 |
| --- | --- |
| 1人のユーザーにアプリ内メッセージが表示されなかった | [1人のユーザー](#in-app-message-not-shown-for-one-user) |
| 1つのプラットフォーム（Android、iOS、またはWeb）でアプリ内メッセージが表示されなかった | [1つのプラットフォーム](#in-app-message-not-shown-on-one-platform) |
| **キャンバス**ステップのアプリ内メッセージが表示されなかった | [キャンバスのアプリ内メッセージ](#canvas-in-app-messages) |
| アプリ内メッセージが遅れて表示された、または遅延後に表示された | [タイミングと遅延表示](#timing-and-delayed-display) |
| インプレッションやクリックが正しくない | [インプレッションと分析](#impressions-and-analytics) |
| イベントユーザーログで`triggers`が欠落または空 | [配信のトラブルシューティング](#delivery-troubleshooting) |
| トリガーは返されたがデバイスに何も表示されない | [プラットフォーム固有の表示トラブルシューティング](#platform-specific-display-troubleshooting) |
| アプリ内メッセージのアセットの読み込みに失敗する（iOS、`NSURLError` -1008） | [アセットの読み込み（Swiftタブ）](?sdktab=swift#swift_asset-loading) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="アプリ内メッセージの症状" }

## 標準的な調査パス {#standard-investigation-path}

すべてのインシデントでこのワークフローを使用してください。ステップ1から開始してください。

1. テストデバイスで**セッション開始**がログに記録されていることを確認します。アプリ内メッセージはセッション開始時にリクエストされます。
2. [イベントユーザーログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log)を開き、そのセッション開始に対するSDKリクエストを見つけます。**Response Data**で以下を確認します。
   - 生のJSONで、`respond_with`に`"triggers": true`が含まれていることを確認します。
   - **Requested Responses**行に**`triggers`**が含まれている必要があります。
   - **Trigger In-App Message**行には、そのリクエストに対して返された各アプリ内メッセージが一覧表示されます。
   - `triggers`キーまたは**Trigger In-App Message**行がない場合は、[メッセージがリクエストされない場合のトラブルシューティング](#troubleshoot-messages-not-being-requested)を参照してください。
   - `triggers`が存在するが空（`[]`）の場合は、[メッセージが返されない場合のトラブルシューティング](#troubleshoot-messages-not-being-returned)を参照してください。
   - **Trigger In-App Message**行が存在するが何も表示されない場合は、[プラットフォーム固有の表示トラブルシューティング](#platform-specific-display-troubleshooting)を参照してください。
   - 各トリガーペイロードには`type`が含まれます：`inapp`（標準）または`templated_iam`（表示前にテンプレートリクエストが必要）。[アプリ内メッセージの種類]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#types-of-in-app-messages)を参照してください。
3. ダッシュボード側の適格性（セグメント、再適格性、フリークエンシーキャップ、優先度、コントロールグループ）については、[配信のトラブルシューティング](#delivery-troubleshooting)と[アプリ内メッセージFAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq)を参照してください。
4. デバイス側の表示の問題（デリゲート、レート制限、画面の向き、セッションタイムアウト）については、[プラットフォーム固有の表示トラブルシューティング](#platform-specific-display-troubleshooting)でSDKタブを選択してください。

## キャンバスのアプリ内メッセージ {#canvas-in-app-messages}

**症状：** ユーザーがキャンバスのアプリ内メッセージステップに入ったが、期待したタイミングでメッセージが表示されなかった。

キャンバスとアプリ内メッセージに関するチケットの大半は、以下の3つの動作に起因します。

1. **次のセッションでの表示：** キャンバスのアプリ内メッセージは、ステップが処理された後の*次の*セッション開始時に適格になります。セッション中にすぐに表示されるわけではありません。キャンバスFAQの[キャンバスのアプリ内メッセージはいつ送信されますか？]({{site.baseurl}}/user_guide/messaging/canvas/faqs#when-are-in-app-messages-in-canvas-sent)を参照してください。
2. **ステップエントリ時の配信バリデーション：** メッセージステップで**メッセージ送信時にオーディエンスを検証**が有効になっている場合、セグメントメンバーシップとフリークエンシーキャップは、表示時ではなくユーザーが**ステップに入った時点**で評価されます。[配信バリデーション]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations)を参照してください。
3. **遅延とセッションタイムアウト：** ユーザーがSDKのセッションタイムアウトよりも長い遅延ステップに入った場合、アプリ内メッセージステップの前に新しいセッションが開始される可能性があります。期待するタイミングのセッション開始時にメッセージが取得されない場合があります。

利用可能時間枠、有効期限、キャンバス分析での_送信数_ゼロについては、キャンバスFAQの[アプリ内メッセージと配信]({{site.baseurl}}/user_guide/messaging/canvas/faqs#messages-and-delivery)を参照してください。

{% alert important %}
キャンバスのアプリ内メッセージは、SDKを通じて送信されたイベントによってのみトリガーできます。REST APIではトリガーできません。
{% endalert %}

## 1人のユーザーにアプリ内メッセージが表示されなかった {#in-app-message-not-shown-for-one-user}

**症状：** 1人のユーザーが期待したアプリ内メッセージを受信しなかった。他のユーザーには影響がない可能性があります。

以下を確認してください。

- SDKが新しいアプリ内メッセージをリクエストする**セッション開始**時に、ユーザーがセグメントに含まれていましたか？
- キャンペーンまたはキャンバスのターゲティングルールに基づいて、ユーザーは適格または再適格でしたか？[キャンペーンとキャンバスの再適格性]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)を参照してください。
- [フリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)が適用されましたか？
- ユーザーはキャンペーンのコントロールグループに含まれていましたか？キャンペーンがABテスト用に設定されているかどうかを確認してください。
- より優先度の高いアプリ内メッセージが代わりに表示されましたか？アプリ内メッセージFAQの[同じセッションで複数のアプリ内メッセージを表示できますか？]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#can-multiple-in-app-messages-display-in-the-same-session)を参照してください。
- デバイスはキャンペーンで指定された画面の向きでしたか？
- トリガー間のデフォルトの最小間隔（30秒）によってメッセージが抑制されましたか？[デフォルトのレート制限のオーバーライド]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#overriding-the-default-rate-limit)を参照してください。

その後、[標準的な調査パス](#standard-investigation-path)に従ってください。

## 1つのプラットフォームでアプリ内メッセージが表示されなかった {#in-app-message-not-shown-on-one-platform}

**症状：** Android、iOS、またはWebでアプリ内メッセージが表示されないが、他のプラットフォームでは動作する可能性があります。

| 考えられる原因 | 確認事項 |
| --- | --- |
| **Send To**ターゲットが間違っている | キャンペーンまたはキャンバスステップが適切に**モバイルアプリ**または**Webブラウザー**をターゲットにしていることを確認してください。Web専用のキャンペーンはAndroidデバイスには送信されません。 |
| カスタムUIまたはハンドラーが表示を抑制している | デリゲート（モバイル）または[`braze.subscribeToInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage)（Web）を確認してください。[カスタマイズ]({{site.baseurl}}/developer_guide/in_app_messages/customization)およびプラットフォームのSDKタブを参照してください。 |
| このプラットフォームで統合が一度も動作していない | このプラットフォームとアプリバージョンで以前にアプリ内メッセージが表示されたことがあるか確認してください。 |
| デバイスでトリガーが発火しなかった | トリガーはSDKを通じてローカルで発生する必要があります。REST API呼び出しではSDKのアプリ内メッセージをトリガーできません。[メッセージのトリガー]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages)を参照してください。 |
| イベントユーザーログで`triggers`が空 | セグメント、再適格性、フリークエンシーキャップ、またはコントロールグループの問題です。[メッセージが返されない場合のトラブルシューティング](#troubleshoot-messages-not-being-returned)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="プラットフォームの症状と原因" }

## すべてのユーザーにアプリ内メッセージが表示されなかった {#in-app-message-not-shown-for-all-users}

**症状：** ユーザーが誰もアプリ内メッセージを受信しなかった、または期待より少ないユーザーしか受信しなかった。

以下を確認してください。

- ダッシュボードとアプリの統合の両方で、トリガーアクションが正しく設定されていますか？
- より優先度の高いアプリ内メッセージがキャンペーンを横取りしましたか？[アプリ内メッセージFAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#can-multiple-in-app-messages-display-in-the-same-session)を参照してください。
- 最新のSDKバージョンを使用していますか？一部のアプリ内メッセージタイプには最小SDKバージョンの要件があります。
- セッションが正しく統合されていますか？このアプリでセッション分析が動作していることを確認してください。
- カスタマイズされたUIライブラリーが表示を妨げていませんか？[カスタマイズ]({{site.baseurl}}/developer_guide/in_app_messages/customization)を参照してください。

その後、[標準的な調査パス](#standard-investigation-path)に従ってください。

## タイミングと遅延表示 {#timing-and-delayed-display}

**症状：** アプリ内メッセージが期待より遅れて表示された、または新しいセッションまで表示されなかった。

一般的な原因：

- **キャンペーンのセッション開始時プリフェッチ：** アプリ内メッセージはセッション開始時にキャッシュされ、トリガーが発火した時に表示されます。次のセッション開始前に発生したトリガーは、そのセッションまで表示されません。[メッセージのトリガー]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages)を参照してください。
- **キャンバスの次のセッション動作：** [キャンバスのアプリ内メッセージ](#canvas-in-app-messages)を参照してください。
- **ダッシュボードでスケジュールされた遅延：** キャンペーンまたはステップに遅延が設定されていないか確認してください。
- **トリガー同期の競合：** ユーザーがセッション開始直後にイベントをログに記録した場合、トリガーがまだ同期されていない可能性があります。セッション開始でトリガーし、意図したイベントでセグメントを設定することで、イベント後の次のセッションで配信されるようにすることを検討してください。
- **連続するアプリ内メッセージ：** ツアーでメッセージを遅延または復元している場合は、[トリガーされたアプリ内メッセージの遅延]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages)を参照してください。
- **大きなアセットまたは遅いCDN：** HTMLアプリ内メッセージの画像と動画を最適化してください。モバイルでは、低速ネットワークで表示前に画像がダウンロードされる場合があります。プラットフォーム固有の注意事項については、SDKタブを選択してください。

{% alert note %}
アプリ内メッセージがセッション開始でトリガーされ、セッションタイムアウトを延長している場合、その時間枠内でアプリを閉じて再度開いてもセッションは更新されません。たとえば、300秒のタイムアウトの場合、セッション開始のアプリ内メッセージはセッションが実際に更新されるまで表示されません。これがテストに影響する場合は、セッションタイムアウトまたはトリガータイプを調整してください。
{% endalert %}

## 配信のトラブルシューティング {#delivery-troubleshooting}

アプリ内メッセージの問題の大半は、**配信**（デバイスがトリガーを受信しなかった）または**表示**（トリガーは到着したが表示されなかった）のいずれかです。まず[配信](#troubleshooting-in-app-message-delivery)を確認し、次に[表示](#platform-specific-display-troubleshooting)を確認してください。

### 配信のトラブルシューティング {#troubleshooting-in-app-message-delivery}

SDKはセッション開始時にBrazeサーバーにアプリ内メッセージをリクエストします。SDKがトリガーをリクエストし、Brazeがそれらを返していることを確認してください。

#### メッセージがリクエストされ返されているか確認する {#check-if-messages-are-requested-and-returned}

1. 自分自身を[テストユーザー]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users)として追加します。
2. 自分のユーザーをターゲットにしたアプリ内メッセージキャンペーンを設定します。
3. アプリケーションで新しいセッションを開始します。
4. [イベントユーザーログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log)で、セッション開始イベントに対するSDKリクエストを見つけます。**Response Data**で以下を確認します。
   - 生のJSONで、`respond_with`に`"triggers": true`が含まれていることを確認します。
   - **Requested Responses**行には、レスポンスのトップレベルキーが一覧表示されます。アプリ内メッセージの場合、**`triggers`**が含まれている必要があります。
   - **Trigger In-App Message**行には、そのリクエストに対して返された各アプリ内メッセージが一覧表示されます。

   次にトリアージします。
   - `triggers`キーまたは**Trigger In-App Message**行がない場合は、[メッセージがリクエストされない場合のトラブルシューティング](#troubleshoot-messages-not-being-requested)を参照してください。
   - `triggers`が存在するが空（`[]`）の場合は、[メッセージが返されない場合のトラブルシューティング](#troubleshoot-messages-not-being-returned)を参照してください。
   - **Trigger In-App Message**行が存在するがデバイスに何も表示されない場合は、[プラットフォーム固有の表示トラブルシューティング](#platform-specific-display-troubleshooting)を参照してください。
   - 各トリガーペイロードには`type`が含まれます：`inapp`（標準）または`templated_iam`（表示前にテンプレートリクエストが必要）。[アプリ内メッセージの種類]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#types-of-in-app-messages)を参照してください。
5. レスポンスデータに正しいアプリ内メッセージが表示されていることを確認します。

![SDKリクエストとレスポンスデータを含むイベントユーザーログ]({% image_buster /assets/img_archive/event_user_log_iams.png %})

##### メッセージがリクエストされない場合のトラブルシューティング {#troubleshoot-messages-not-being-requested}

アプリ内メッセージがリクエストされていない場合、アプリがセッションを正しくトラッキングしていない可能性があります。アプリ内メッセージはセッション開始時に更新されます。セッションタイムアウトのセマンティクスに基づいて、アプリがセッションを開始していることを確認してください。

![セッション開始イベントの成功を表示するイベントユーザーログのSDKリクエスト]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

##### メッセージが返されない場合のトラブルシューティング {#troubleshoot-messages-not-being-returned}

アプリ内メッセージが返されていない場合、ターゲティングまたは適格性の問題が発生している可能性があります。

1. セグメントにユーザーが含まれていない。
   - ユーザーの[**エンゲージメント**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#engagement-tab)タブで、期待するセグメントを確認してください。
2. ユーザーがすでにメッセージを受信しており、再適格ではなかった。
   - [再適格性の設定]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)と[アプリ内メッセージFAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#campaigns)を確認してください。
3. ユーザーがフリークエンシーキャップに達した。
   - [フリークエンシーキャップの設定]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)を確認してください。
4. ユーザーがコントロールグループに入った。
   - **キャンペーンバリアントを受信した**フィルターを**コントロール**に設定したセグメントを作成するか、統合テスト中はコントロールグループをオプトアウトしてください。
5. より優先度の高いアプリ内メッセージが優先された。[アプリ内メッセージFAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#can-multiple-in-app-messages-display-in-the-same-session)を参照してください。

アーカイブ済みキャンペーン、トリガー設定、サイレント時間については、[アプリ内メッセージFAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq)を参照してください。

## インプレッションと分析 {#impressions-and-analytics}

**症状：** インプレッション数またはクリック数が期待と一致しない。

- **_インプレッション_が_ユニークインプレッション_より多い：** ユーザーが複数のデバイスを持っている場合や、スケジュールされた遅延により同じユーザーが複数回適格になった場合に想定される動作です。[キャンペーンとキャンバスの再適格性]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)を参照してください。
- **インプレッションが期待より少ない：** ユーザーがメッセージを閲覧しなかった可能性（インプレッションは表示時にログに記録されます）、複数の高優先度メッセージが互いに横取りした可能性、またはトリガー同期の競合が適用された可能性があります。キャンバスのアプリ内メッセージについては、[キャンバスのアプリ内メッセージ](#canvas-in-app-messages)を参照してください。指標の完全な定義については、[アプリ内メッセージレポート]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting)と[アプリ内メッセージFAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq)を参照してください。
- **インプレッションが以前より少ない：** セグメントとキャンペーンの変更ログを確認してください。より優先度の高いキャンペーンで同じトリガーイベントを再利用していないか確認してください。

![キャンペーン詳細ページの変更ログを表示するリンク。ユーザーが最後にキャンペーンを閲覧してから7件の変更があります。]({% image_buster /assets/img_archive/trouble4.png %})

デリゲートまたはカスタムハンドラーを使用してアプリ内メッセージを手動で表示している場合は、インプレッションとクリックを自分でログに記録する必要があります。SwiftとAndroidの詳細については、[プラットフォーム固有の表示トラブルシューティング](#platform-specific-display-troubleshooting)のSDKタブを参照してください。Webについては、[アプリ内メッセージデータのログ記録]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data)を参照してください。

## プラットフォーム固有の表示トラブルシューティング {#platform-specific-display-troubleshooting}

イベントユーザーログに**Trigger In-App Message**行が表示されているがデバイスに何も表示されない場合は、SDKタブを選択して表示チェック（デリゲート、レート制限、画面の向き、カスタムハンドラー）を確認してください。

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/in_app_messages/troubleshooting.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/in_app_messages/troubleshooting.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/in_app_messages/troubleshooting.md %}
{% endsdktab %}
{% endsdktabs %}