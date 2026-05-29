---
nav_title: 5月
page_order: 8
noindex: true
page_type: update
description: "この記事には2019年5月のリリースノートが含まれています。"
---

# 2019年5月 {#may-2019}

## Content Cards

Content Cardsは、顧客のアプリおよびWeb体験内に表示される永続的なコンテンツです。

Content Cardsを使用すると、顧客が愛用するアプリ内で、体験を中断することなく、高度にターゲットを絞ったリッチコンテンツのダイナミックなストリームを送信できます。また、メールやプッシュ通知などの他のチャネルとContent Cardsを組み合わせて、一貫したマーケティング戦略を実現することもできます。

![Content Cardsフィード]({% image_buster /assets/img/cc-feed.png %}){: height="50%" width="50%"}

さらに、Content Cardsはカードのピン留め、カードの却下、APIベースの配信、カスタムカードの有効期限、カード分析など、よりパーソナライズされた機能をサポートしています。

通知センター、ホームページフィード、プロモーションフィードの作成にご活用ください。

サポートされているBraze SDKバージョンに更新する必要があります：
- iOS：3.8.0以降
- Android：2.6.0以降
- Web：2.2.0以降

[Content Cardsの詳細についてはこちらをご覧ください。]({{site.baseurl}}/user_guide/channels/content_cards/)

{% alert update %}
CurrentsのContent CardsおよびContent CardsのAPIドキュメントは、今週後半にリリースされる予定です。お楽しみに！
{% endalert %}

## Rokuプラットフォームの追加 {#roku-platform-addition}

Brazeは機能に新しいチャネルを追加しました！新しいチャネルに拡大することで、お客様は視聴行動を理解してデータを充実させたり、関連するすべてのチャネルを通じて消費者に有意義な体験を提供したりできるようになります。

データの強化やカスタムイベントのトラッキングのために、[Rokuデバイスからデータを取得]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=roku)できるようになりました。

## CanvasまたはCampaignの更新に関する通知設定 {#notification-preferences-for-canvas-or-campaign-updates}

この[新しい通知]({{site.baseurl}}/user_guide/administrative/company_settings/notification_preferences/#notification-preferences)は、CampaignまたはCanvasがアクティブ化、更新、再アクティブ化、または非アクティブ化されたときにメールで通知します。Brazeアカウントの**通知設定**でこれを有効にしてください。

## Jamppテクノロジーパートナードキュメント {#jampp-technology-partner-documentation}

Jamppは、モバイル顧客の獲得とリターゲティングのためのパフォーマンスマーケティングプラットフォームです。行動データと予測およびプログラマティック技術を組み合わせて、消費者が初めて購入する、またはより頻繁に購入するように促すパーソナルで関連性の高い広告を表示することで、広告主の収益を生み出します。

Brazeのお客様は、Braze Webhookチャネルを構成してイベントをJamppにストリーミングすることで、[Jamppと統合]({{site.baseurl}}/partners/jampp/)できます。その結果、モバイル広告エコシステム内でJamppを使用してリターゲティングの取り組みにより豊富なデータセットを追加することができます。

## アプリ内メッセージ用プラットフォームピッカー {#platform-picker-for-in-app-messages}

Campaign作成プロセスのこのステップを強調するプラットフォームピッカーにより、アプリ内メッセージの送信先と対象プラットフォームの選択が簡単になりました。

![プラットフォームピッカー]({% image_buster /assets/img/iam_platforms.gif %})

## メールのディスパッチID Currentsフィールド {#dispatch-id-currents-field-for-email}

{% alert update %}
CanvasとCampaignの間で`dispatch_id`の動作が異なるのは、Brazeがキャンバスステップ（スケジュール可能なエントリステップを除く）を「スケジュールされた」場合でもトリガーイベントとして扱うためです。CanvasやCampaignでの[`dispatch_id`の動作]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id/)について詳しくはこちらをご覧ください。

_更新は2019年8月に記録されました。_
{% endalert %}

Currentsの機能を継続的に強化する取り組みの一環として、すべてのコネクタータイプでCurrentsのメールイベントにフィールドとして`dispatch_id`を追加します。

`dispatch_id`は、Brazeプラットフォームからの送信（ディスパッチ）ごとに生成される一意のIDです。

スケジュール済みのメッセージを受信したすべての顧客に同じ`dispatch_id`が割り当てられますが、アクションベースメッセージやAPIトリガーメッセージを受信した顧客にはメッセージごとに固有の`dispatch_id`が割り当てられます。`dispatch_id`フィールドを使用すると、定期的なCampaignのどのインスタンスがコンバージョンを担当しているかを識別できるため、より多くのインサイトと、どのタイプのCampaignがビジネス目標の達成に役立っているかについての情報を得ることができます。

## 「自分のものだけを表示」Campaign並べ替え機能 {#only-show-mine-campaign-sorting-feature}

ユーザーがCampaignグリッドの`Only Show Mine`チェックボックスをオンにすると、結果はログインしているユーザーによって作成されたCampaignのみを表示するようにフィルターされます。さらに、ユーザーは`created_by_me:true`を入力して検索バーを使用できます。

また、Campaignグリッドのサイドバーはサイズ変更可能になりました！

## エイリアスによるユーザーの削除 {#delete-users-by-alias}

`users/delete`エンドポイントを使用して、[エイリアスでユーザーを削除]({{site.baseurl}}/api/endpoints/user_data/#user-delete-request)できるようになりました！

## メールクリック数と開封数のユニーク計算 {#unique-calculation-for-email-clicks-and-opens}

メールのユニーククリック数とユニーク開封数が、ユーザーごとに7日間の期間で取得・表示されるようになりました。この7日間の期間内において、各`dispatch_id`でカウントが1ずつ増加します。

`dispatch_id`を使用すると、繰り返しメッセージに各メッセージの実際のユニーク開封数またはユニーククリック数を反映させることができます。Currentsで`dispatch_id`を利用できるようになったため、このデータを簡単に照合できるようになります。

Mailjetも使用しているユーザーは、以前のユニーク判定の時間枠が30日間を超えていたため、これらの数値が急増する可能性があります。この変更については3週間前にお知らせ済みです。SendGridをご利用のお客様は違いを感じないはずです。

これらの更新された用語は、[レポート指標用語集]({{site.baseurl}}/user_guide/analytics/metrics_glossary/)で検索できます。

{% alert update %}
CanvasとCampaignの間で`dispatch_id`の動作が異なるのは、Brazeがキャンバスステップ（スケジュール可能なエントリステップを除く）を「スケジュールされた」場合でもトリガーイベントとして扱うためです。[CanvasとCampaignにおける`dispatch_id`の動作]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id/)について詳しくはこちらをご覧ください。

_更新は2019年8月に記録されました。_
{% endalert %}

## 最もエンゲージされたチャネル {#most-engaged-channel}

{% alert update %}
[2019年11月の製品リリース]({{site.baseurl}}/help/release_notes/2019/november/#intelligence-suite)時点で、「最もエンゲージされたチャネル」は[「インテリジェントチャネル」]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel/)に改名されました。
{% endalert %}

最もエンゲージされたチャネルフィルターは、選択されたメッセージングチャネルが「最適な」チャネルであるオーディエンスの一部を選択します。この場合、「最適」とは「ユーザーの履歴を考慮した場合、エンゲージメントの可能性が最も高い」という意味です。メール、Webプッシュ、またはモバイルプッシュ（利用可能なモバイルOSやデバイスを含む）をチャネルとして選択できます。

この新しいフィルターを[セグメンテーションフィルターライブラリー]({{site.baseurl }}/user_guide/engagement_tools/segments/segmentation_filters/)でご確認ください。