---
nav_title: 4月
page_order: 9
noindex: true
page_type: update
description: "この記事には2020年4月のリリースノートが含まれています。"
---
# 2020年4月 {#april-2020}

## Movable Inkのパートナーシップ {#movable-ink-partnership}

Movable Inkは、プッシュ、アプリ内メッセージ、およびコンテンツカードキャンペーンでカウントダウンタイマー、投票、スクラッチオフなどのインテリジェントクリエイティブ機能を使用する機能をBrazeのお客様に提供します。Movable InkとBrazeは、ダイナミックなデータドリブン型のメッセージに対するより包括的なアプローチを実現し、重要事項に関するリアルタイムのエレメントをユーザーに提供します。

キャンペーンに[Movable Inkを統合]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/movable_ink/)しましょう！

## インテリジェントタイミング {#intelligent-timing}

キャンペーンのスケジュールを設定する場合、[インテリジェントタイミング]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/)（以前はインテリジェント配信）を使用して、Brazeが個人がエンゲージする可能性が最も高いと判断した時間に、各ユーザーへメッセージを配信できます。

この機能の更新内容は次のとおりです。
- **サイレント時間の明確化**：サイレント時間機能に変更はありませんが、UIは明確化のために調整されています。
- **プレビューチャートの追加**：インテリジェントタイミングを使用して、1日の各時間にメッセージを受信するユーザー数と、最適な時間を計算するのに十分なデータがあるユーザーの割合を確認するためのチャートを生成できるようになりました。
- **カスタムフォールバックの追加**：最適な時刻を計算するのに十分なエンゲージメントデータがないユーザーにメッセージを送信するローカル時刻を選択できるようになりました。

## Facebookオーディエンスエクスポート {#facebook-audience-export}

Brazeでは、Braze セグメントページからユーザーを手動でエクスポートしてFacebookカスタムオーディエンスを作成する機能を提供しています。これは1回限りの静的オーディエンスエクスポートであり、新しい[Facebookカスタムオーディエンス]({{site.baseurl}}/partners/facebook/)のみが作成されます。

すべてのクラスタで利用可能な新しいBraze Facebookオーディエンスエクスポートプロセスは、明確な統合ステップでワークフローを合理化します。カスタムオーディエンスを送信するためにOAuth Redirect URIをホワイトリストに登録したり、統合するためにFacebookアプリ設定を調整したりする必要はなくなりました。

{% alert important %}
現在Facebookカスタムオーディエンスを使用しているすべてのクライアントは、これらの新しいステップを使用してBraze セグメントを再統合する必要があることにご注意ください。
{% endalert%}


## コンテンツブロックおよびメールテンプレートAPIの更新 {#content-block-and-email-template-api-updates}

[template/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/)および[content_block/list]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) APIエンドポイントが更新され、新しい`tags`フィールドが追加されました。このフィールドは、現在のブロックまたはメールテンプレートに適用されるタグを配列として一覧表示します。

## パーソナライズされた差出人アドレス {#personalized-from-address}

Braze内でメールメッセージを作成する際に、メール作成画面の**送信情報**セクションでメッセージの差出人アドレスをパーソナライズできるようになりました。サポートされている任意の[パーソナライゼーションタグ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/)を使用できます。

![パーソナライズされた差出人アドレス]({% image_buster /assets/img/personalized-from-name.png %}){: style="max-width:80%"}