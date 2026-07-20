---
nav_title: FAQ
article_title: FAQ
page_order: 30
description: "この記事では、WhatsAppキャンペーンの設定時に最もよく寄せられる質問について説明します。"
page_type: FAQ
channel:
  - WhatsApp

---

# よくある質問 {#frequently-asked-questions}

> このページでは、WhatsAppに関する最も重要な質問にお答えします！<br><br>このFAQは、法的助言を提供することを意図しておらず、法的助言として依拠することはできません。WhatsAppチャネルの使用は、Meta Platforms, Inc.の特定の要件に従います。適用されるすべての要件および特に適用される可能性のある法律に準拠してWhatsAppチャネルを使用していることを確認するために、法律顧問の助言を求めてください。

## FAQトピック {#faq-topics}
- [WhatsAppビジネスアカウント](#whatsapp-business-accounts)
- [WhatsAppビジネスアカウントの電話番号](#whatsapp-business-account-phone-numbers)
- [オプトインと購読管理](#opt-in-and-subscription-management)
- [メッセージング制限と品質評価](#messaging-limits-and-quality-rating)
- [WhatsAppテンプレートとコンポーザー](#whatsapp-templates-and-composer)
- [配信到達性と課金](#deliverability-and-billing)
- [インテグレーション、データ、レポート](#integrations-data-and-reporting)

### WhatsAppビジネスアカウント {#whatsapp-business-accounts}

#### WhatsAppビジネスアカウントを作成するにはどうすればよいですか？ {#how-do-i-create-a-whatsapp-business-account}
Brazeダッシュボードの埋め込みサインアップフローを通じてWhatsAppビジネスアカウント（WABA）を作成することをお勧めします。

#### すでにMetaビジネスアカウントを持っています。それでもWhatsAppビジネスアカウントは必要ですか？ {#i-already-have-a-meta-business-account-do-i-still-need-a-whatsapp-business-account}
はい、WhatsAppビジネスアカウントを作成する必要があります。[メインのMetaビジネスアカウントの下にWABAをネストする]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)ことをお勧めします。

#### WhatsAppビジネスアカウントにアクセスするにはどうすればよいですか？ {#how-do-i-access-my-whatsapp-business-account}
埋め込みサインアップフローを完了した後、business.facebook.comの[WhatsAppセクション](https://business.facebook.com/wa/manage/home)に移動してアカウントにアクセスできます。

#### 複数のWABAをBrazeに接続できますか？ {#can-i-connect-multiple-wabas-to-braze}
はい、ワークスペースごとに最大10個のWhatsAppビジネスアカウントを追加でき、各ビジネスアカウントは異なるMeta Business Managerの下にネストできます。

![BrazeとWhatsAppのエコシステムの図。ワークスペースとWhatsAppビジネスアカウントの接続関係を示しています。1つの購読グループを1つの電話番号に、複数のWhatsAppビジネスアカウントを1つのワークスペースに、1つのワークスペースを複数のMeta Business Portfolioに接続できます。]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %})

#### WhatsAppビジネスアカウントの通貨を変更できますか？ {#can-i-change-my-whatsapp-business-account-currency}
いいえ。MetaがWhatsAppビジネスアカウントの通貨を管理しており、Brazeでは変更や変換ができません。別の通貨を使用するには、その通貨で[別のWhatsAppビジネスアカウントを作成する]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)か、Metaサポートに連絡して既存のアカウントの通貨を更新できるかどうかを確認してください。

#### ビジネス認証とは何ですか？ {#what-is-business-verification}
ビジネス認証は、ブランドが正当なビジネスであることを確認するために使用されるWhatsAppの概念です。WhatsApp Managerで完了できます。ビジネス認証は、メッセージングのスケーリングにも必要です。ビジネス認証がない場合、顧客はローリング24時間内に最大250人のユニークエンドユーザーにのみ送信できます。

#### 公式ビジネスアカウントとは何ですか？ {#what-is-an-official-business-account}
OBA（公式ビジネスアカウント）は、表示名の横に緑色のチェックマークが付き、任意で取得できます。ビジネス認証の完了後に公式ビジネスアカウントを申請できます。ビジネス認証と公式ビジネスアカウントは異なるWhatsAppの概念であることに注意してください。

### WhatsAppビジネスアカウントの電話番号 {#whatsapp-business-account-phone-numbers}

#### WhatsAppビジネスアカウントに電話番号は必要ですか？ {#do-i-need-a-phone-number-for-my-whatsapp-business-account}
はい、アクセスできる番号が必要です。埋め込みサインアップフローを進める際に、2要素認証で電話番号を確認するよう求められます。この電話番号は、他のWhatsAppアカウント（ビジネスまたは個人）で使用することはできません。

#### WhatsAppではどのような種類の電話番号がサポートされていますか？ {#what-types-of-phone-numbers-are-supported-with-whatsapp}
詳細については、Metaの[電話番号](https://developers.facebook.com/docs/whatsapp/phone-numbers)に関する要件を参照してください。

#### 1つの電話番号を複数のWABAで使用できますか？ {#can-i-use-one-phone-number-across-multiple-wabas}
いいえ。電話番号を複数のWABAで共有することはできません。

#### 特定の国にメッセージを送信するために特定の種類の電話番号が必要ですか？ {#do-i-need-a-specific-type-of-phone-number-to-send-messages-to-specific-countries}
いいえ。WhatsAppでは、サポートされている任意の電話番号から任意の国のエンドユーザーにメッセージを送信できます。詳細については、Metaの[電話番号](https://developers.facebook.com/docs/whatsapp/phone-numbers)に関する要件を参照してください。

#### ユーザーの電話番号はBrazeでどのように保存する必要がありますか？ {#how-do-user-phone-numbers-need-to-be-stored-in-braze}
ユーザーの電話番号は[E.164形式]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers#formatting)で保存する必要があります。

#### ユーザーの電話番号をインポートできますか？ {#can-i-import-user-phone-numbers}
はい。[ユーザーの電話番号をインポート]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers)できます。

### オプトインと購読管理 {#opt-in-and-subscription-management}

#### WhatsAppでエンドユーザーにマーケティングメッセージを送信するためにオプトインを収集する必要がありますか？ {#do-i-need-to-collect-opt-in-to-send-marketing-messages-to-end-users-on-whatsapp}
はい、WhatsAppでは、エンドユーザーにマーケティングメッセージを送信するために、企業が[オプトイン同意を収集する](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)ことを要求しています。

#### オプトイン同意を収集するために、エンドユーザーに積極的にメッセージを送信できますか？ {#can-i-proactively-message-end-users-on-whatsapp-to-collect-opt-in-consent}
エンドユーザーに積極的にメッセージを送信する場合、最初のビジネス発信メッセージでは、ユーザーがあなたのビジネスからマーケティングメッセージを受信したいかどうかを尋ね、Metaの[オプトイン取得](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)に関する要件に準拠する必要があります。WhatsAppはチャネル上でのビジネスの評判を監視するため、エンドユーザーに対して明確にし、受信を希望したメッセージのみを送信することがベストプラクティスとして推奨されます。

#### オプトイン収集時にエンドユーザーの電話番号を収集する必要がありますか？ {#do-i-need-to-collect-the-end-users-phone-number-when-i-collect-opt-in}
メッセージを送信するには、Brazeプロファイルにエンドユーザーの電話番号が必要です。
- すでに番号を持っている場合は、オプトイン時に収集する必要はありません。
- エンドユーザーの番号を持っていない場合は、オプトイン方法に電話番号の取得を含める必要があります。

#### オプトインしたエンドユーザーの購読ステータスを更新するにはどうすればよいですか？ {#how-do-i-update-the-subscription-status-of-end-users-who-opt-in}
WhatsAppチャネルの購読管理は、他のBrazeチャネルと同様に機能します。詳細については、[ユーザー購読の管理]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)を参照してください。

#### WhatsAppでマーケティングメッセージの受信にオプトインしたユーザーのリストがすでにある場合、Brazeで購読ステータスを更新するにはどうすればよいですか？ {#if-i-already-have-a-list-of-users-who-have-opted-in-to-receive-marketing-messages-on-whatsapp-how-do-i-update-their-subscription-status-in-braze}
[ユーザーインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import#updating-subscription-group-status-optional)を通じて購読ステータスを更新できます。

#### オプトインを収集するためにどのような方法を使用すべきですか？ {#what-methods-should-i-use-to-collect-opt-ins}
コンプライアンスを維持するために、[Metaのオプトイン方法に関するガイドライン](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)を参照することをBrazeは推奨しています。Brazeの[チャネルとオプトインのアイデアと提案](https://docs.google.com/document/d/1rNKnKN2oIn-e9bXdYEvnwdlzlCsEOKs-xREcdVvPBE8/edit)も参照してください。

#### WhatsAppではダブルオプトインは必要ですか？ {#is-double-opt-in-required-for-whatsapp}
いいえ、ダブルオプトインは必要ありません。

#### ユーザーはWhatsAppメッセージをどのようにオプトアウトしますか？ {#how-do-my-users-opt-out-of-whatsapp-messages}
ユーザーは2つの方法でオプトアウトできます。
1. 特定のオプトアウトワードを含む受信WhatsAppメッセージを設定し、Webhookを使用してユーザーの購読ステータスを更新します。
2. WhatsAppテンプレート内にオプトアウトのクイック返信を追加し、対応するWebhookで更新します。

### メッセージング制限と品質評価 {#messaging-limits-and-quality-rating}

#### メッセージング制限とは何ですか？ {#what-are-messaging-limits}
メッセージング制限は、WhatsAppの信頼性構築の概念です。各電話番号がローリング24時間内に開始できるビジネス発信会話の最大数を決定します。メッセージング制限には4つのレベルがあります：1k、10k、100k、無制限です。

#### メッセージング制限を引き上げるにはどうすればよいですか？ {#how-do-i-increase-my-messaging-limit}
以下の条件を満たすと、WhatsAppがメッセージング制限を引き上げます。
1. [電話番号のステータス](https://www.facebook.com/business/help/896873687365001)が**Connected**である
2. [電話番号の品質評価](https://www.facebook.com/business/help/896873687365001)が**Medium**または**High**である
3. 過去7日間に、X人以上のユニークユーザーとの会話を開始している（Xは現在のメッセージング制限を2で割った値）

したがって、100kから無制限に引き上げるには、7日間で少なくとも50,000件のビジネス発信会話を送信する必要があります。

#### メッセージング制限の引き上げにはどのくらいの時間がかかりますか？ {#how-long-does-it-take-to-increase-my-messaging-limits}
上記のすべての条件が満たされている場合、4日間で1kから無制限にメッセージング制限を引き上げることができます。

#### 現在のメッセージング制限はどこで確認できますか？ {#where-can-i-see-my-current-messaging-limit}
**WhatsApp Manager > Overview Dashboard > Insights**タブで現在のメッセージング制限を確認できます。

#### メッセージング制限に達した状態でメッセージを送信しようとするとどうなりますか？ {#what-happens-if-i-attempt-to-send-messages-when-i-have-already-reached-my-messaging-limit}
現在の制限を超えるユニークユーザーにキャンペーンまたはキャンバスを送信しようとすると、メッセージの送信に失敗します。Brazeは、メッセージング制限が引き上げられた場合に備えて、最大1日間メッセージの再送信を試み続けます。

#### メッセージング制限は下がることがありますか？ {#can-my-messaging-limit-decrease}
はい、電話番号の品質評価が低くなりすぎると、WhatsAppがメッセージング制限を引き下げるリスクがあります。Brazeは、電話番号のステータスやメッセージング制限レベルの更新など、WhatsAppからの品質関連の更新を購読して通知を受け取ることをお勧めします。WhatsApp Managerダッシュボードで直接通知を購読できます。

#### 電話番号の品質評価に影響する要因は何ですか？品質評価が低くなりすぎるとどうなりますか？ {#what-factors-affect-phone-number-quality-rating-and-what-happens-when-my-quality-rating-drops-too-low}
電話番号の品質評価に影響する要因には、エンドユーザーがビジネスをブロックすること（およびブロック時に提供する理由）やエンドユーザーがビジネスを報告することが含まれます。

品質評価が低い場合、電話番号のステータスは**Connected**から**Flagged**に変わります。7日間で品質が改善されない場合、ステータスは**Connected**に戻ります。ただし、メッセージング制限は次のレベルに引き下げられます。たとえば、以前100,000のメッセージング制限を持っていた電話番号は、10,000のメッセージング制限になります。

#### Metaのスループット制限とは何ですか？ {#what-is-the-meta-throughput-limit}
Metaには、WABAのメッセージング制限とは別のスループット制限があります。クラウドAPIがサポートするデフォルトの制限は、1秒あたり80メッセージです。キャンペーンがこの制限を超える可能性がある場合は、制限の引き上げを[リクエスト](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/#throughput)できます。Metaは、キャンペーン送信の少なくとも3日前にこのリクエストを提出することを推奨しています。

### WhatsAppテンプレートとコンポーザー {#whatsapp-templates-and-composer}

#### WhatsAppテンプレートとは何ですか？ {#what-is-a-whatsapp-template}
WhatsAppでは、すべてのビジネス発信メッセージが承認済みテンプレートを使用して開始される必要があります。テンプレートには、メッセージのコピーと、画像、コールトゥアクション、クイック返信ボタンなどのオプションのリッチメディアが含まれます。WhatsAppがテンプレートを承認した後、BrazeでWhatsAppメッセージを作成するために使用できます。

#### WhatsAppテンプレートはどこで作成、編集、管理しますか？ {#where-do-i-create-edit-and-manage-my-whatsapp-templates}
テンプレートの作成、編集、管理、および承認への提出は、WhatsApp Managerで直接行います。WABAがBrazeに接続された後、ダッシュボードですべてのテンプレートがステータスインジケーター付きで表示されます。テンプレートが却下された場合は、WhatsApp Managerを通じて直接再提出します。**テンプレートはBrazeで直接作成または編集することはできません。**

#### WhatsAppがテンプレートの提出を審査するのにどのくらいかかりますか？ {#how-long-does-it-take-whatsapp-to-review-a-template-submission}
承認プロセスには最大24時間かかる場合がありますが、多くの場合、テンプレートは数時間または数分で処理されます。

#### 一度にいくつのテンプレートを持つことができますか？ {#how-many-templates-can-i-have-at-a-given-time}
メッセージテンプレートの制限は、ビジネス認証ステータスによって異なります。**WhatsApp Manager > Message Templates**ページで制限を確認できます。

#### Brazeでテンプレートのコピーとリッチメディアをパーソナライズするにはどうすればよいですか？ {#how-do-i-personalize-template-copy-and-rich-media-in-braze}
WhatsAppでは、メッセージテンプレートに変数パラメーターを挿入できます。メッセージは変数パラメーターで開始または終了することはできません。変数パラメーターは、BrazeプラットフォームのLiquidロジックで入力できます。変数パラメーターの詳細については、[BrazeでのWhatsAppメッセージの作成]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message)を参照してください。

#### テンプレートが却下されました。Brazeが承認を手助けしてくれますか？ {#my-template-got-rejected-can-braze-help-me-get-it-approved}
Brazeチームはテンプレートの却下理由を確認することができません。WhatsApp Business Managerで直接テンプレートを編集して再提出してください。必要に応じてサンプルテンプレートを提供してください。テンプレートがMetaの[ビジネス](https://www.whatsapp.com/legal/business-policy/?fbclid=IwAR2qWg6yFKdyjDMxJkbNSM38FLGsxXxffC1qStY2gaHOyp-gl_8g72rZNIw)または[コマース](https://www.whatsapp.com/legal/commerce-policy/?fbclid=IwAR3bzN3LTZ-7kO-wnO7X3smtPKGy0asxaFod-U1Ub8B9JUpnrfy1_y7LpAQ)ポリシーに準拠していることを再確認してください。

#### Brazeでリッチメディアをターゲティングまたはパーソナライズできますか？ {#can-the-rich-media-be-targeted-or-personalized-in-braze}
画像はメディアライブラリからアップロードできますが、動的にターゲティングすることはできません。URLについては、リンクの最後の部分を[Liquidを使用して動的に入力]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#use-liquid-personalization-in-urls)できます。

#### WhatsAppテンプレートではどのようなリッチメディアがサポートされていますか？ {#what-kind-of-rich-media-is-supported-in-whatsapp-templates}
WhatsAppテンプレートには、画像、コールトゥアクション（URLまたは電話番号）、クイック返信ボタンを追加できます。これらの要素は、WhatsAppで直接テンプレートを作成する際に追加できます。

#### テンプレートがWhatsAppのコマースポリシーに違反しているとして誤ってフラグ付けされた場合はどうすればよいですか？ {#what-if-my-template-was-falsely-flagged-for-violating-whatsapps-commerce-policy}
Metaがテンプレートを誤ってフラグ付けしたと思われる場合は、WhatsAppからのメールに記載されている審査リンクを使用して再審査をリクエストしてください。WhatsApp Businessチームが判断を審査し、適切であれば取り消します。

#### インポートしたWhatsAppテンプレートがコンポーザーで「Message Incomplete」と表示されるのはなぜですか？ {#why-does-my-imported-whatsapp-template-show-message-incomplete-in-the-composer}
「Message Incomplete」の警告は、必須のテンプレート変数スロットがコンポーザーで有効な値で埋められていない場合に表示されます。

[WhatsAppテンプレートビルダー]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder)を使用してテンプレートを作成すると、Brazeは変数を連番のプレースホルダー（{% raw %}`{{1}}`、`{{2}}`、`{{3}}`{% endraw %}など）に番号を振り直します。MetaのWhatsApp Managerで外部的に作成されたテンプレートには、変数マッピングでエラーが発生しやすいパターンが含まれている場合があります。例えば：

- 連番でない番号付け（例：{% raw %}`{{1}}`、`{{3}}`、`{{5}}`{% endraw %}）
- シーケンス内の変数の欠落（例：{% raw %}`{{2}}`{% endraw %}のスキップ）
- 1以外の番号から始まる変数

これを解決するには、MetaのWhatsApp Managerでテンプレートを編集して連番のプレースホルダー形式を使用し、Brazeに再インポートしてください。Brazeで、各必須変数フィールドに有効なLiquid値が入力されていることを確認してください。

#### テンプレートのプレビューは正常に表示されるのに、WhatsAppキャンペーンが送信されないのはなぜですか？ {#why-is-my-whatsapp-campaign-not-sending-despite-template-previewing}
テンプレートのプレビューは正常に表示されるのに、処理台帳に**Abort**と「Param text cannot have new-line/tab characters or more than 4 consecutive spaces」という詳細が表示される場合は、メッセージ内のLiquidテンプレートパラメーター値を確認してください。WhatsAppでは、パラメーターテキスト値に以下を含めることができません：

- 改行文字
- タブ文字
- 4つ以上の連続するスペース

テンプレートパラメーターを入力するLiquidロジックが、送信前にこれらの文字を削除するか、テキストを適切にフォーマットしていることを確認してください。

### 配信到達性と課金 {#deliverability-and-billing}

#### メッセージが配信されない理由は何ですか？ {#why-would-a-message-not-be-delivered}
ネットワークの問題やデバイスの電源がオフになっているなど、メッセージが配信されない理由はさまざまです。

#### メッセージが配信されなかった場合、課金されますか？ {#if-a-message-is-not-delivered-will-i-be-billed}
いいえ。メッセージが配信されなかった場合、課金されません。

#### ユーザーが私のビジネスをブロックした場合はどうなりますか？ {#what-happens-if-a-user-blocks-my-business}
ユーザーがあなたのビジネスをブロックした場合、その後送信しようとするメッセージは配信されず、課金もされません。

#### ユーザーがメッセージを報告した場合はどうなりますか？ {#what-happens-if-a-user-reports-a-message}
ユーザーがメッセージを報告した場合でも、そのユーザーに後続のメッセージを送信できます。ただし、報告はチャネル上の品質評価に影響を与える可能性があります。

#### ユーザーが私のビジネスをブロックまたは報告した場合、Brazeで購読ステータスは更新されますか？ {#if-a-user-blocks-or-reports-my-business-will-their-subscription-status-be-updated-in-braze}
いいえ。Brazeの購読ステータスは更新されません。

#### WhatsAppアカウントを報告したユーザーを今後の配信から除外するにはどうすればよいですか？ {#how-can-i-exclude-users-who-report-my-whatsapp-account-from-upcoming-launches}
Brazeは、アカウントがフラグ付けまたは報告された際にWhatsAppから通知を受け取らないため、Brazeでそれらのユーザーを自動的に特定または除外することはできません。アカウントを報告したユーザーは、WhatsApp購読グループに残り、今後のメッセージの対象となり続ける可能性があります。

ただし、ユーザーがオプトアウトキーワードで返信した際にトリガーされるキャンペーンを設定し、[`/subscription/status/set`エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)を使用して自動的に購読解除することができます。詳細については、[WhatsAppのオプトインとオプトアウトプロセス]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-opt-in-and-opt-out-process)を参照してください。

#### WhatsAppの応答メッセージは無料ですか？ {#are-whatsapp-response-messages-free}

Brazeのキャンペーンまたはキャンバスエディターで作成された応答メッセージ（承認済みWhatsAppテンプレートではないもの）は、Metaによってサービスメッセージとして扱われます。BrazeのネイティブWhatsAppインテグレーションを通じて送信されるサービスメッセージは、オープンなカスタマーサービスウィンドウ内で[応答メッセージ]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages)として送信される場合、アクションクレジットを消費しません。

| メッセージタイプ | アクションクレジット | 備考 |
|---|---|---|
| 応答メッセージ（受信返信） | 消費しない | Brazeで作成。Meta承認済みテンプレートではない。 |
| テンプレートメッセージ | 消費する | マーケティング、ユーティリティ、認証、期間限定オファーテンプレートは送信ごとに課金されます。 |
| サービスウィンドウ内のユーティリティテンプレート | Metaは課金しない | Metaは、ユーザー発信メッセージから24時間以内に送信されたユーティリティテンプレートに対して課金しません。アクションクレジットの消費は契約に従います。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="応答メッセージのアクションクレジット" }

元の24時間ウィンドウの後にユーザーがクイック返信をタップするキャンバスフローについては、[24時間ウィンドウ外のクイック返信と受信メッセージ]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window)を参照してください。

#### 24時間ウィンドウが閉じた後にユーザーが返信またはクイック返信をタップした場合はどうなりますか？ {#what-happens-if-a-user-replies-or-taps-a-quick-reply-after-the-24-hour-window-closes}
新しい24時間のカスタマーサービスウィンドウが開きます。[24時間ウィンドウ外のクイック返信と受信メッセージ]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window)を参照してください。

#### WhatsAppのクイック返信のためにキャンバスのアクションパスを31日に設定する必要がありますか？ {#do-i-need-to-set-my-canvas-action-path-to-31-days-for-whatsapp-quick-replies}
いいえ。デフォルトのアクションパス期間で十分です。[24時間ウィンドウ外のクイック返信と受信メッセージ]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window)を参照してください。

#### 特定のキャンペーンまたはキャンバスが消費したWhatsAppクレジット数を確認できますか？ {#can-i-see-how-many-whatsapp-credits-a-specific-campaign-or-canvas-consumed}
現在、Brazeダッシュボードでは確認できません。キャンペーンおよびキャンバスの分析では送信数、配信数、失敗数が表示されますが、メッセージごとのクレジット消費量は表示されません。テンプレートカテゴリーやメッセージタイプによって課金が異なるため、送信数はクレジット使用量と1対1で一致しません。課金の詳細については、[WhatsAppの応答メッセージは無料ですか？](#are-whatsapp-response-messages-free)を参照してください。

### インテグレーション、データ、レポート {#integrations-data-and-reporting}

#### BrazeはWhatsAppのチャットボットや有人チャットなどのカスタマーサポートのユースケースをサポートしていますか？ {#does-braze-support-customer-support-use-cases-like-chatbots-and-human-assisted-chat-for-whatsapp}
Braze内または直接インテグレーションを通じたチャットボットや有人チャットはサポートしていません。

すでにWhatsAppをカスタマーサポートチャネルとして使用している場合は、現在の設定を維持し、マーケティングメッセージング用にBraze経由で新しいWABAを作成することをお勧めします。このWABAには新しい電話番号が必要です。

#### カスタマーサポートメッセージングとBraze経由のマーケティングメッセージングの間の「ギャップを埋める」にはどうすればよいですか？ {#how-can-i-bridge-the-gap-between-my-customer-support-messaging-and-my-marketing-messaging-via-braze}
WhatsAppのLiquidプロパティを使用して、受信WhatsAppメッセージのコンテンツ（メッセージ本文やメディアURLを含む）をBrazeから他のプラットフォーム（カスタマーサポートツールを含む）に転送できます。詳細については、[サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)を参照してください。

Brazeに情報を送信するには、たとえばユーザーがアクティブなサポート会話中であることを示すために、カスタム属性（ブール値の「既存のサポートチャットあり = true/false」など）をログに記録し、マーケティングキャンペーンのセグメンテーション基準として使用できます。また、2つのチャットスレッド間でディープリンクを設定して、マーケティングスレッドからサポートスレッドへ、またはその逆にユーザーを誘導することもできます。

#### Brazeはユーザーの応答を保存しますか？ {#does-braze-store-user-responses}
メッセージは処理に必要な時間のみ保存されます。ユーザーメッセージにアクセスするには、Currentsを使用してください。

#### Brazeダッシュボードではどのような指標が利用できますか？ {#what-metrics-are-available-in-the-braze-dashboard}
Brazeダッシュボードでは、ユニーク受信者数、送信数、配信数、既読数、失敗数を確認できます。Brazeが既読を追跡するには、ユーザーの既読確認が「オン」になっている必要があります。他のチャネルと同様に、キャンペーンのパフォーマンスを監視するためにコンバージョンイベントを設定することもできます。

#### WhatsApp会話とは何ですか？ {#what-is-a-whatsapp-conversation}
WhatsAppは双方向メッセージングに焦点を当てたチャネルであるため、（個々のメッセージ数ではなく）会話を基準としています。会話とは、ビジネスとエンドユーザー間の24時間のスレッドです。

- **ビジネス発信会話**：ビジネスが承認済みテンプレートメッセージをエンドユーザーに送信して開始する会話です。ビジネスがメッセージを送信すると同時に、24時間のウィンドウが始まります。
- **ユーザー発信会話**：エンドユーザーがビジネスにメッセージを送信する会話です。ビジネスが応答メッセージを送信すると、24時間のウィンドウが始まります。