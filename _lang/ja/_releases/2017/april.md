---
nav_title: 4月
page_order: 9
noindex: true
page_type: update
description: "この記事には2017年4月のリリースノートが含まれています。"
---

# 2017年4月 {#april-2017}

## HTMLブラウザ内メッセージ {#html-in-browser-messages}

カスタムHTMLやメールキャプチャ形式を含むインタラクティブなブラウザ内メッセージタイプがサポートされるようになりました。これにより、どこにいても顧客にリーチできます。[アプリ内メッセージ]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices/)について詳しくはこちらをご覧ください。

## コネクテッドコンテンツによるパーソナライズされたアプリ内メッセージ {#personalized-in-app-message-with-connected-content}

トリガーされたアプリ内メッセージに {% raw %} {%connected_content%} {% endraw %} ブロックを追加しました。これにより、API経由でアクセス可能な情報をメッセージに直接挿入して、豊富なパーソナライゼーションを追加できます。プッシュ、メール、webhookに加えて、アプリ内でもコネクテッドコンテンツを使用できるようになりました。[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)について詳しくはこちらをご覧ください。

## News Feedカードのナビゲーションを改善 {#improved-navigation-for-news-feed-cards}

News Feedカードを作成するためのUIを改善し、ナビゲートやキャンペーンの作成がより簡単になりました。[News Feedカード]({{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/#news-feed-cards)について詳しくはこちらをご覧ください。

## iOSリッチ通知のプレビューを改善 {#improved-preview-for-ios-rich-notifications}

iOSのプレビュー通知でリッチ通知が表示されるようになり、フォントサイズに至るまで、顧客に送信する内容を正確に確認できるようになりました。[iOSリッチ通知]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications)について詳しくはこちらをご覧ください。

## プッシュ統計に「Influenced Opens」を追加 {#added-influenced-opens-to-push-statistics}

Brazeで提供されている標準的なキャンペーンおよびキャンバスの統計一覧に「Influenced Opens」を追加しました。これにより、Influenced、Direct、Total Opensの内訳がわかりやすくなります。[Influenced Opens]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/)について詳しくはこちらをご覧ください。

## 内部グループへのアップグレード {#upgrade-to-internal-groups}

複数の内部グループを作成し、SDKロギング、REST APIロギング、またはメッセージコンテンツテストのいずれに使用するかを示すプロパティを割り当てることができるようになりました。[イベントユーザーログ]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab)について詳しくはこちらをご覧ください。

> 更新：内部グループを使用して[シードメールを送信]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/#seed-groups)することもできます。

## Web URLの新しいオプション {#new-options-for-web-urls}

プッシュメッセージ、アプリ内メッセージ、ブラウザ内メッセージ、News FeedカードについてWeb URLを外部Webブラウザで開くオプションが追加されました。「アプリにディープリンクする」アクションもHTTP/HTTPSディープリンクと互換性を持つようになりました。BranchやAppleのユニバーサルリンクなどのパートナーを使用する場合は、SDKのカスタマイズが必要になります。[ディープリンク]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/#what-is-deep-linking)について詳しくはこちらをご覧ください。

## 新しい「コンバージョンを実行」イベントキャンバス {#new-performed-conversion-event-canvas}

新しい「コンバージョンを実行」イベントと「キャンバスコントロール内」フィルターを追加し、リターゲティングオプションを改善しました。[リターゲティングフィルター]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns/#retarget-campaigns)の使用について詳しくはこちらをご覧ください。