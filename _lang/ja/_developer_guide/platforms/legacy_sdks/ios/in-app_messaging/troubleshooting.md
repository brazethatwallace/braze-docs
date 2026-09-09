---
nav_title: トラブルシューティング
article_title: iOS 向けアプリ内メッセージングのトラブルシューティング
platform: iOS
page_order: 7
description: "このリファレンス記事では、iOS のアプリ内メッセージに関するトラブルシューティングのトピックを取り上げます。"
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# アプリ内メッセージのトラブルシューティング {#troubleshoot-in-app-messages}

## インプレッション {#impressions}

### インプレッションまたはクリックの分析がログに記録されない {#impression-or-click-analytics-arent-being-logged}

アプリ内メッセージのデリゲートを設定してメッセージの表示やクリックアクションを手動で処理している場合は、アプリ内メッセージのクリックとインプレッションを手動でログに記録する必要があります。

#### インプレッションが予想より少ない {#impressions-are-lower-than-expected}

トリガーはセッション開始時にデバイスへ同期されるまでに時間がかかるため、セッション開始直後にユーザーがイベントや購入をログに記録すると競合が発生する可能性があります。考えられる回避策の1つとして、キャンペーンのトリガーをセッション開始に変更し、目的のイベントや購入でセグメントを作成する方法があります。この場合、アプリ内メッセージはイベント発生後の次のセッション開始時に配信されます。

## 期待したアプリ内メッセージが表示されない {#expected-in-app-message-did-not-display}

アプリ内メッセージの問題の多くは、配信と表示の2つの主要なカテゴリに分類できます。期待したアプリ内メッセージがデバイスに表示されなかった理由をトラブルシューティングするには、まず[アプリ内メッセージがデバイスに配信されたこと](#troubleshooting-in-app-message-delivery)を確認し、次に[メッセージの表示をトラブルシューティング](#troubleshooting-in-app-message-display)してください。

### アプリ内メッセージの配信 {#troubleshooting-in-app-message-delivery}

SDKはセッション開始時にBrazeサーバーからアプリ内メッセージをリクエストします。アプリ内メッセージがデバイスに配信されているかどうかを確認するには、アプリ内メッセージがSDKによってリクエストされ、Brazeサーバーから返されていることを確認する必要があります。

#### メッセージがリクエストされて返されているか確認する {#check-if-messages-are-requested-and-returned}

1. ダッシュボードで自分自身を[テストユーザー]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users)として追加します。
2. 自分のユーザーをターゲットにしたアプリ内メッセージキャンペーンを設定します。
3. アプリケーションで新しいセッションが発生していることを確認します。
4. [イベントユーザーログ]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab)を使用して、セッション開始時にデバイスがアプリ内メッセージをリクエストしていることを確認します。テストユーザーのセッション開始イベントに関連するSDKリクエストを見つけてください。
  - アプリがトリガーされたアプリ内メッセージをリクエストする予定だった場合、**Response Data**の**Requested Responses**フィールドに`trigger`と表示されているはずです。
  - アプリがオリジナルのアプリ内メッセージをリクエストする予定だった場合、**Response Data**の**Requested Responses**フィールドに`in_app`と表示されているはずです。
5. [イベントユーザーログ]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab)を使用して、正しいアプリ内メッセージがレスポンスデータに返されているか確認します。<br>![アプリ内メッセージリクエストのイベントユーザーログエントリ。]({% image_buster /assets/img_archive/event_user_log_iams.png %})

#### メッセージがリクエストされない場合のトラブルシューティング {#troubleshoot-messages-not-being-requested}

アプリ内メッセージがリクエストされていない場合、アプリがセッションを正しくトラッキングしていない可能性があります。アプリ内メッセージはセッション開始時に更新されるためです。また、アプリのセッションタイムアウトのセマンティクスに基づいて、実際にセッションが開始されていることを確認してください。

![イベントユーザーログに表示される、セッション開始イベントが成功したSDKリクエスト。]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

### メッセージが返されない場合のトラブルシューティング {#troubleshoot-messages-not-being-returned}

アプリ内メッセージが返されない場合、キャンペーンのターゲティングに問題がある可能性があります。

- セグメントにユーザーが含まれていない。
  - ユーザーの[**エンゲージメント**]({{ site.baseurl }}/user_guide/audience/manage_audience/user_profiles/#engagement-tab)タブを確認し、**セグメント**の下に正しいセグメントが表示されているか確認してください。
- ユーザーが以前にそのアプリ内メッセージを受信しており、再度受信する再適格性がない。
  - **キャンペーン Composer**の**配信**ステップにある[キャンペーン再適格性設定]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/)を確認し、再適格性設定がテスト設定と一致していることを確認してください。
- ユーザーがキャンペーンのフリークエンシーキャップに達した。
  - キャンペーンの[フリークエンシーキャップ設定]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping)を確認し、テスト設定と一致していることを確認してください。
- キャンペーンにコントロールグループがある場合、ユーザーがコントロールグループに入った可能性がある。
  - これが発生したかどうかは、受信キャンペーンバリアントフィルターを使用してセグメントを作成し、キャンペーンバリアントを**コントロール**に設定して、ユーザーがそのセグメントに入っているか確認することで確認できます。
  - インテグレーションテスト用のキャンペーンを作成する際は、コントロールグループの追加をオプトアウトしてください。

### アプリ内メッセージの表示 {#troubleshooting-in-app-message-display}

アプリがアプリ内メッセージを正常にリクエストして受信しているにもかかわらず表示されない場合、デバイス側のロジックが表示を妨げている可能性があります。

- トリガーされたアプリ内メッセージは、[トリガー間の最小時間間隔]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/in-app_message_delivery#minimum-time-interval-between-triggers)（デフォルトは30秒）に基づいてレート制限されています。
- アプリ内メッセージの処理をカスタマイズするデリゲートを設定している場合、そのデリゲートがアプリ内メッセージの表示に影響を与えていないか確認してください。
- 画像のダウンロードに失敗すると、画像を含むアプリ内メッセージは表示されません。`SDWebImage`フレームワークが適切に統合されていないと、画像のダウンロードは常に失敗します。デバイスログを確認して、画像のダウンロードが失敗していないことを確認してください。
- デバイスの向きがアプリ内メッセージで指定された向きと一致しない場合、アプリ内メッセージは表示されません。デバイスが正しい向きになっていることを確認してください。