---
nav_title: 7月
page_order: 6
noindex: true
page_type: update
description: "この記事には2017年7月のリリースノートが含まれています。"
---

# 2017年7月 {#july-2017}

## Webプッシュにおける大きな画像 {#large-images-in-web-push}

WindowsおよびAndroidのChrome用Webプッシュで大きな画像のサポートを追加しました。これにより、リッチで魅力的なカスタマーエクスペリエンスを構築できるようになります。[Webプッシュ]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web/)について詳しくはこちらをご覧ください。

## メールフィールドの更新 {#updates-to-email-fields}

間違ったアドレスを誤って入力しないように、特定の差出人アドレスのセットにメールをロックできるようになりました。メール作成フォームには、過去6か月間に使用されたアドレスが事前に入力され、プロセスが効率化されます。詳細については、[メールのベストプラクティス]({{site.baseurl}}/user_guide/channels/email/best_practices/)をご確認ください。

## キャンペーン詳細APIの更新 {#updates-to-campaign-details-api}

`/campaign/details` エンドポイントがメッセージに関する情報を提供するようになり、APIを使用して件名、HTML本文、差出人アドレス、返信先フィールドを取得できるようになりました。[Braze API]({{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api)について詳しくはこちらをご覧ください。

## Liquidテンプレーティングの更新 {#updates-to-liquid-templating}

キャンバスおよびキャンペーンでバリアント属性をテンプレート化する機能を追加しました。キャンバスではバリアントの API IDと名前を、キャンペーンではメッセージの `message_api_id` と `message_name` をテンプレート化できるようになりました。これらの更新により、メッセージングの柔軟性が向上し、パーソナライズされたキャンペーンを構築できるようになります。[パーソナライズされたメッセージング]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/)について詳しくはこちらをご覧ください。

## 新しいHTMLメールエディター {#new-html-email-editor}

ライブプレビュー、Liquidによるパーソナライゼーション、行番号と構文ハイライトを備えた改良されたフルスクリーンテキストエディターを使用して、簡単にメールを作成・テストできるようになりました。[メールの作成]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template)について詳しくはこちらをご覧ください。

## プレビューの更新 {#updates-to-previews}

キャンペーンおよびキャンバスでメッセージプレビューを下にスクロールしても画面ウィンドウが追従するようになり、変更が常に反映されていることを確認できます。詳細については、[プレビューとテスト]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#step-6-preview-message)を参照してください。

## 新しいセグメントメンバーシップフィルター {#new-segment-membership-filter}

[セグメントメンバーシップフィルター]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#targeting-filters)を追加しました。これにより、既存のセグメントのいずれかへのメンバーシップに基づいてユーザーをターゲット設定できます。さらに、セグメントフィルターで「And」と「Or」ロジックの両方を使用する機能、およびセグメントを相互にネストする機能を追加しました。これらの更新により、カスタマイズされたメッセージをより正確に顧客に送信できるようになります。

## Androidプレビューの更新 {#update-to-android-preview}

Android N以降のAndroidの最新バージョンを反映するために、[Androidプレビュー]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#step-5-preview-message)を更新しました。