---
nav_title: 8月
page_order: 6
noindex: true
page_type: update
description: "この記事には、2020年8月のリリースノートが含まれています。"
---
# 8月 {#august}

## external ID移行エンドポイント {#external-id-migration-endpoints}

Brazeは、2つの新しいexternal ID移行エンドポイントをリリースしました。これらのエンドポイントにより、Braze APIを使用してユーザーのBraze external IDの名前変更や削除が可能になります。これらのエンドポイントを活用することで、異なるネーミングスキーマを持つユーザーを、履歴データを保持したまま移行できます。[`users.external_ids.rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)および[`users.external_ids.remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/)エンドポイントの詳細については、ドキュメントをご覧ください。

## Predictive Churn

BrazeのPredictive Suiteでは、機械学習を直接利用できます。[Predictive Churn]({{site.baseurl}}/user_guide/brazeai/)から始めることで、Brazeプラットフォーム内のデータをシームレスに活用し、効果的にアクションを起こすことがこれまで以上に簡単になります。これを使えば、特定の顧客ベースの解約リスクを予測するカスタマイズされた機械学習モデルを作成し、手遅れになる前に機械学習がリスクありと判断したユーザーにメッセージを送ることができます。

この機能のプレビューは、8月初旬に対象となるBrazeのお客様のダッシュボードに表示されます。完全な機能へのアクセスについては、アカウントマネージャーにお問い合わせください。

## Currentsトラッキングプロパティの更新 {#updates-to-currents-tracking-properties}

特定のCurrentsメッセージエンゲージメントイベント内に、トラッキングプロパティ`canvas_variation_name`および`canvas_step_name`が追加されました。全リストについては、[メッセージエンゲージメントイベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)および[Currentsの変更ログ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)をご確認ください。

## Amazon Personalizeパートナーシップ {#amazon-personalize-partnership}

Amazon Personalizeは、機械学習を利用して、Webサイトやアプリケーション向けに高品質なレコメンデーションを作成します。Amazon Personalizeを使用すると、リアルタイムでパーソナライズされた商品やコンテンツのレコメンデーション、ターゲットを絞ったマーケティングプロモーションを提供し、カスタマーエンゲージメントを向上させることができます。詳しくは、[Amazon Personalize]({{site.baseurl}}/partners/amazon_personalize/)のドキュメントをご覧ください。

## Vizbeeパートナーシップ {#vizbee-partnership}

Vizbeeは、家庭内のすべてのスマートフォンとスマートテレビを1つのシームレスなデバイスとして連携させ、優れたユーザー体験を実現します。Vizbeeは、通知、ディープリンク、メールなどの既存のモバイルアプリマーケティングチャネルを活用して、すべてのCTVデバイス（Roku、FireTV、Samsung TV、LG TVなど）で視聴者を獲得し、エンゲージメントを高めるのに役立ちます。詳細については、[Vizbee]({{site.baseurl}}/partners/message_orchestration/deeplinking/vizbee_for_tv_deeplinking/)のドキュメントをご覧ください。

## Bluedotパートナーシップ {#bluedot-partnership}

Bluedotは、アプリのための正確でわかりやすいジオフェンシングを提供するロケーションプラットフォームです。BluedotのSDKを使用すると、よりスマートにメッセージを送信し、モバイル注文のチェックインを自動化し、ワークフローを最適化し、摩擦のない体験を作成できます。詳細については、[Bluedot]({{site.baseurl}}/partners/data_augmentation/contextual_location/bluedot/#bluedot)のドキュメントをご覧ください。

## Iterateパートナーシップ {#iterate-partnership}

Iterateは、スマートで使いやすく、ブランドに合わせたルックアンドフィールのアンケートツールを提供し、顧客から簡単に学べるようにします。詳細については、[Iterate]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/surveys/iterate/)のドキュメントをご覧ください。