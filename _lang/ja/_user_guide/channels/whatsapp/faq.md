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
- [WhatsApp Businessアカウント](#whatsapp-business-accounts)
- [WhatsApp Businessアカウントの電話番号](#whatsapp-business-account-phone-numbers)
- [オプトインと購読管理](#opt-in-and-subscription-management)
- [メッセージング制限と品質評価](#messaging-limits-and-quality-rating)
- [WhatsAppテンプレートとコンポーザー](#whatsapp-templates-and-composer)
- [配信性と請求](#deliverability-and-billing)
- [インテグレーション、データ、レポート](#integrations-data-and-reporting)
- [メディアと画像](#media-and-images)

### WhatsApp Businessアカウント {#whatsapp-business-accounts}

#### WhatsApp Businessアカウントはどのように作成しますか？ {#how-do-i-create-a-whatsapp-business-account}
Brazeダッシュボードの埋め込みサインアップフローを通じてWhatsApp Businessアカウント（WABA）を作成することをお勧めします。

#### すでにMeta Businessアカウントを持っています。それでもWhatsApp Businessアカウントは必要ですか？ {#i-already-have-a-meta-business-account-do-i-still-need-a-whatsapp-business-account}
はい、WhatsApp Businessアカウントを作成する必要があります。メインのMeta Businessアカウントの下に[WABAをネストする]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)ことをお勧めします。

#### WhatsApp Businessアカウントにはどのようにアクセスしますか？ {#how-do-i-access-my-whatsapp-business-account}
埋め込みサインアップフローを完了した後、business.facebook.comで[WhatsAppセクション](https://business.facebook.com/wa/manage/home)に移動してアカウントにアクセスできます。

#### 複数のWABAをBrazeに接続できますか？ {#can-i-connect-multiple-wabas-to-braze}
はい、ワークスペースあたり最大10個のWhatsApp Businessアカウントを追加でき、各Businessアカウントは異なるMeta Business マネージャーの下にネストできます。

![BrazeとWhatsAppのエコシステムの図。ワークスペースとWhatsApp Businessアカウントの接続関係を示しています。1つの購読グループを1つの電話番号に、複数のWhatsApp Businessアカウントを1つのワークスペースに、1つのワークスペースを複数のMeta Businessポートフォリオに接続できます。]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %})

#### WhatsApp Businessアカウントの通貨を変更できますか？ {#can-i-change-my-whatsapp-business-account-currency}
いいえ。MetaがWhatsApp Businessアカウントの通貨を管理しており、Brazeでは変更や換算ができません。別の通貨を使用するには、その通貨で[別のWhatsApp Businessアカウントを作成する]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)か、Metaサポートに連絡して既存のアカウントの通貨を更新できるかどうかお問い合わせください。

#### ビジネス認証とは何ですか？ {#what-is-business-verification}
ビジネス認証とは、ブランドが正当なビジネスであることを確認するためにWhatsAppが使用する概念です。WhatsApp マネージャーで完了できます。メッセージングを拡大するためにもビジネス認証が必要です。ビジネス認証がない場合、顧客はローリング24時間で最大250人の一意のエンドユーザーにしか送信できません。

#### 公式ビジネスアカウントとは何ですか？ {#what-is-an-official-business-account}
OBAは、表示名の横に緑色のチェックマークが表示されるもので、任意です。ビジネス認証の完了後に公式ビジネスアカウントを申請できます。ビジネス認証と公式ビジネスアカウントは異なるWhatsAppの概念であることに注意してください。

#### WhatsApp Businessの表示名が拒否される理由は何ですか？ {#why-might-my-whatsapp-business-display-name-be-rejected}
WhatsApp Businessの表示名の拒否はMetaが管理しています。表示名が拒否された場合は、[WhatsAppの表示名ガイドライン](https://faq.whatsapp.com/793641088597363)を参照してください。

表示名がガイドラインを満たしているにもかかわらず拒否される場合、Brazeでは具体的な理由を確認できません。ただし、拒否の最も一般的な理由は、ビジネスのオンラインプレゼンスが低すぎるか、[規制対象または制限対象の製品](https://business.whatsapp.com/policy#further-guidance)をマーケティングしていることです。

表示名の拒否に関する詳細なガイダンスについては、[Metaリソース]({{site.baseurl}}/user_guide/channels/whatsapp/meta_resources)を参照してください。

### WhatsApp Businessアカウントの電話番号 {#whatsapp-business-account-phone-numbers}
#### WhatsApp Businessアカウントには電話番号が必要ですか？ {#do-i-need-a-phone-number-for-my-whatsapp-business-account}
はい、アクセスできる番号が必要です。埋め込みサインアップフローを進める際に、2要素認証で電話番号を確認するよう求められます。この電話番号は他のWhatsAppアカウント（ビジネスまたは個人）で使用されていないものである必要があります。

#### WhatsAppではどのような種類の電話番号がサポートされていますか？ {#what-types-of-phone-numbers-are-supported-with-whatsapp}
詳細については、Metaの[電話番号](https://developers.facebook.com/docs/whatsapp/phone-numbers)に関する要件を参照してください。

#### 1つの電話番号を複数のWABAで使用できますか？ {#can-i-use-one-phone-number-across-multiple-wabas}
いいえ。電話番号を複数のWABAで共有することはできません。

#### 特定の国にメッセージを送信するには、特定の種類の電話番号が必要ですか？ {#do-i-need-a-specific-type-of-phone-number-to-send-messages-to-specific-countries}
いいえ。WhatsAppでは、サポートされている任意の電話番号から任意の国のエンドユーザーにメッセージを送信できます。詳細については、Metaの[電話番号](https://developers.facebook.com/docs/whatsapp/phone-numbers)に関する要件を参照してください。

#### ユーザーの電話番号はBrazeでどのように保存する必要がありますか？ {#how-do-user-phone-numbers-need-to-be-stored-in-braze}
ユーザーの電話番号は[E.164形式]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers#formatting)で保存する必要があります。

#### ユーザーの電話番号をインポートできますか？ {#can-i-import-user-phone-numbers}
はい。[ユーザーの電話番号をインポート]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers)できます。

### オプトインと購読管理 {#opt-in-and-subscription-management}

#### WhatsAppでエンドユーザーにマーケティングメッセージを送信するには、オプトインを収集する必要がありますか？ {#do-i-need-to-collect-opt-in-to-send-marketing-messages-to-end-users-on-whatsapp}
はい、WhatsAppではエンドユーザーにマーケティングメッセージを送信するために、ビジネスが[オプトイン同意を収集する](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)ことが求められます。

#### オプトイン同意を収集するために、エンドユーザーに積極的にメッセージを送信できますか？ {#can-i-proactively-message-end-users-on-whatsapp-to-collect-opt-in-consent}
エンドユーザーに積極的にメッセージを送信する場合、最初のビジネス発信メッセージで、ユーザーがビジネスからマーケティングメッセージを受信したいかどうかを尋ね、Metaの[オプトイン取得](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)に関する要件に準拠する必要があります。WhatsAppはチャネル上のビジネスの評判を監視しているため、エンドユーザーに対して明示的であり、ユーザーが受信したいと示したメッセージのみを送信することがベストプラクティスとして推奨されます。

#### オプトイン収集時にエンドユーザーの電話番号も収集する必要がありますか？ {#do-i-need-to-collect-the-end-users-phone-number-when-i-collect-opt-in}
メッセージを送信するには、Brazeプロファイルにエンドユーザーの電話番号が必要です。
- すでに番号を持っている場合は、オプトイン時に収集する必要はありません。
- エンドユーザーの番号を持っていない場合は、オプトイン方法に電話番号の取得を含める必要があります。

#### オプトインしたエンドユーザーの購読ステータスはどのように更新しますか？ {#how-do-i-update-the-subscription-status-of-end-users-who-opt-in}
WhatsAppチャネルの購読管理は、他のBrazeチャネルと同様に機能します。詳細については、[ユーザー購読の管理]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)を参照してください。

#### WhatsAppでマーケティングメッセージの受信にオプトインしたユーザーのリストがすでにある場合、Brazeでの購読ステータスはどのように更新しますか？ {#if-i-already-have-a-list-of-users-who-have-opted-in-to-receive-marketing-messages-on-whatsapp-how-do-i-update-their-subscription-status-in-braze}
[ユーザーインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import#updating-subscription-group-status-optional)を通じて購読ステータスを更新できます。

#### オプトインの収集にはどのような方法を使用すべきですか？ {#what-methods-should-i-use-to-collect-opt-ins}
コンプライアンスを維持するために、[Metaのオプトイン方法に関するガイドライン](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)を参照することをBrazeでは推奨しています。キャンバスとキャンペーンのセットアップ方法については、[オプトインとオプトアウト]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs)を参照してください。

#### WhatsAppにはダブルオプトインが必要ですか？ {#is-double-opt-in-required-for-whatsapp}
いいえ、ダブルオプトインは必要ありません。

#### ユーザーはWhatsAppメッセージからどのようにオプトアウトしますか？ {#how-do-my-users-opt-out-of-whatsapp-messages}
ユーザーは2つの方法でオプトアウトできます。
1. 特定のオプトアウトワードを含むインバウンドWhatsAppメッセージを設定し、Webhookを使用してユーザーの購読ステータスを更新します。
2. WhatsAppテンプレート内にオプトアウトのクイック返信を追加し、対応するWebhookで更新します。

#### サードパーティを通じてWhatsAppメッセージを送信する場合、BrazeのWhatsApp購読グループを使用できますか？ {#can-i-use-a-braze-whatsapp-subscription-group-if-i-send-whatsapp-messages-through-a-third-party}
いいえ。BrazeのWhatsApp購読グループは、BrazeのWhatsAppチャネルを通じて送信されるメッセージに適用されます。サードパーティプロバイダーやBrazeのWhatsAppキャンペーンおよびキャンバス外のカスタムインテグレーションを通じてWhatsAppメッセージを送信する場合、オプトイン同意をカスタム属性（または独自の購読モデル）に保存し、その属性をセグメンテーションと適格性判定に使用できます。BrazeがWhatsApp番号を所有している場合の関連パターンについては、[BrazeでWhatsAppのサポートとマーケティングを連携するにはどうすればよいですか？](#how-do-i-connect-whatsapp-support-and-marketing-in-braze)を参照してください。

### メッセージング制限と品質評価 {#messaging-limits-and-quality-rating}

#### メッセージング制限とは何ですか？ {#what-are-messaging-limits}
メッセージング制限とは、WhatsAppの信頼性構築のための概念です。各電話番号がローリング24時間で開始できるビジネス発信の会話の最大数を決定します。メッセージング制限には、1k、10k、100k、無制限の4つのレベルがあります。

#### メッセージング制限を引き上げるにはどうすればよいですか？ {#how-do-i-increase-my-messaging-limit}
以下の条件を満たすと、WhatsAppがメッセージング制限を引き上げます。
1. [電話番号のステータス](https://www.facebook.com/business/help/896873687365001)が**Connected**
2. [電話番号の品質評価](https://www.facebook.com/business/help/896873687365001)が**Medium**または**High**
3. 過去7日間に、一意のユーザーとX回以上の会話を開始している（Xは現在のメッセージング制限を2で割った値）

そのため、100kから無制限に引き上げるには、7日間で少なくとも50,000回のビジネス発信の会話を送信する必要があります。

#### メッセージング制限を引き上げるにはどのくらいの時間がかかりますか？ {#how-long-does-it-take-to-increase-my-messaging-limits}
前述のすべての条件を満たした場合、メッセージング制限を1kから無制限に4日間で引き上げることができます。

#### 現在のメッセージング制限はどこで確認できますか？ {#where-can-i-see-my-current-messaging-limit}
現在のメッセージング制限は、**WhatsApp マネージャー > Overview Dashboard > Insights**タブで確認できます。

#### メッセージング制限に達している状態でメッセージを送信しようとするとどうなりますか？ {#what-happens-if-i-attempt-to-send-messages-when-i-have-already-reached-my-messaging-limit}
現在の制限を超える一意のユーザーにキャンペーンやキャンバスを送信しようとすると、メッセージは送信に失敗します。Brazeは、メッセージング制限が引き上げられた場合、最大1日間メッセージの再送信を試行し続けます。

#### メッセージング制限は下がることがありますか？ {#can-my-messaging-limit-decrease}
はい、電話番号の品質評価が低下しすぎると、WhatsAppがメッセージング制限を引き下げるリスクがあります。Brazeでは、WhatsApp マネージャーダッシュボードで直接通知を購読し、電話番号のステータスやメッセージング制限レベルの更新など、品質に関する更新の通知を受け取ることをお勧めします。

#### 電話番号の品質評価に影響する要因は何ですか？品質評価が低下しすぎるとどうなりますか？ {#what-factors-affect-phone-number-quality-rating-and-what-happens-when-my-quality-rating-drops-too-low}
電話番号の品質評価に影響する要因には、エンドユーザーがビジネスをブロックすること（およびブロック時に提供する理由）、エンドユーザーがビジネスを報告することが含まれます。

品質評価が低い場合、電話番号のステータスは**Connected**から**Flagged**に変更されます。7日間で品質が改善されない場合、ステータスは**Connected**に戻ります。ただし、メッセージング制限は次のレベルに引き下げられます。例えば、以前100,000のメッセージング制限を持っていた電話番号は、現在10,000のメッセージング制限になります。

#### Metaのスループット制限とは何ですか？ {#what-is-the-meta-throughput-limit}
MetaにはWABAのメッセージング制限とは別のスループット制限があります。クラウドAPIがサポートするデフォルトの制限は1秒あたり80メッセージです。キャンペーンがこの制限を超えると思われる場合は、制限の引き上げを[リクエスト](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/#throughput)できます。Metaでは、キャンペーン送信の少なくとも3日前にこのリクエストを提出することを推奨しています。

### WhatsAppテンプレートとコンポーザー {#whatsapp-templates-and-composer}

#### WhatsAppテンプレートとは何ですか？ {#what-is-a-whatsapp-template}
WhatsAppでは、すべてのビジネス発信メッセージが承認済みテンプレートを使用して開始される必要があります。テンプレートにはメッセージのコピーと、画像、コールトゥアクション、クイック返信ボタンなどのオプションのリッチメディアが含まれます。WhatsAppがテンプレートを承認した後、BrazeでWhatsAppメッセージの作成に使用できます。

#### WhatsAppテンプレートはどこで作成、編集、管理しますか？ {#where-do-i-create-edit-and-manage-my-whatsapp-templates}
Brazeの[WhatsAppテンプレートビルダー]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder)またはMetaのWhatsApp マネージャーでテンプレートを作成して送信できます。いずれの場所で作成されたテンプレートも、ステータスインジケーター付きでBrazeダッシュボードに表示されます。送信後、ロックされたフィールドにはMetaの再承認が必要です。詳細については、[テンプレートビルダーFAQの編集制限]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder#can-i-edit-a-template-after-its-been-approved)を参照してください。

#### WhatsAppがテンプレート送信をレビューするのにどのくらいかかりますか？ {#how-long-does-it-take-whatsapp-to-review-a-template-submission}
承認プロセスには最大24時間かかりますが、多くの場合テンプレートは数時間または数分で処理されます。

#### ある時点でいくつのテンプレートを持てますか？ {#how-many-templates-can-i-have-at-a-given-time}
メッセージテンプレートの制限はビジネス認証ステータスによって異なります。制限は**WhatsApp マネージャー > Message Templates**ページで確認できます。

#### Brazeでテンプレートのコピーとリッチメディアをパーソナライズするにはどうすればよいですか？ {#how-do-i-personalize-template-copy-and-rich-media-in-braze}
WhatsAppでは、メッセージテンプレートに変数パラメーターを挿入できます。メッセージの先頭や末尾に変数パラメーターを配置することはできません。変数パラメーターはBrazeプラットフォームでLiquidロジックを使用して入力できます。変数パラメーターの詳細については、[BrazeでのWhatsAppメッセージの作成]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message)を参照してください。

#### テンプレートが拒否されました。Brazeは承認を手助けしてくれますか？ {#my-template-got-rejected-can-braze-help-me-get-it-approved}
Brazeチームにはテンプレートの拒否理由を確認する権限がありません。WhatsApp Business マネージャーと直接連携してテンプレートを編集し、再送信してください。必要に応じてサンプルテンプレートを提供してください。テンプレートがMetaの[ビジネス](https://www.whatsapp.com/legal/business-policy/?fbclid=IwAR2qWg6yFKdyjDMxJkbNSM38FLGsxXxffC1qStY2gaHOyp-gl_8g72rZNIw)または[コマース](https://www.whatsapp.com/legal/commerce-policy/?fbclid=IwAR3bzN3LTZ-7kO-wnO7X3smtPKGy0asxaFod-U1Ub8B9JUpnrfy1_y7LpAQ)ポリシーに準拠していることを再確認してください。

#### Brazeでリッチメディアをターゲティングまたはパーソナライズできますか？ {#can-rich-media-be-targeted-or-personalized-in-braze}
はい。メディアライブラリから静的画像をアップロードするか、URLで画像を追加し、[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)や[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)でパーソナライズできます。画像URLはURL内の任意の場所で完全なLiquidロジックをサポートしています。これはテンプレートメッセージとレスポンスメッセージ（メディアメッセージとクイック返信レイアウト）に適用されます。詳細については、[ダイナミック画像]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#dynamic-images)を参照してください。

#### WhatsAppテンプレートではどのような種類のリッチメディアがサポートされていますか？ {#what-kind-of-rich-media-is-supported-in-whatsapp-templates}
WhatsAppテンプレートには、画像、コールトゥアクション（URLまたは電話番号）、クイック返信ボタンを追加できます。これらの要素はWhatsAppで直接テンプレートを作成する際に追加できます。

#### テンプレートがWhatsAppのコマースポリシー違反として誤ってフラグされた場合はどうすればよいですか？ {#what-if-my-template-was-falsely-flagged-for-violating-whatsapps-commerce-policy}
Metaがテンプレートを誤ってフラグしたと思われる場合は、WhatsAppからのメールにあるレビューリンクを使用して再レビューをリクエストしてください。WhatsApp Businessチームが決定をレビューし、適切な場合は取り消します。

#### インポートしたWhatsAppテンプレートがコンポーザーで「Message Incomplete」と表示されるのはなぜですか？ {#why-does-my-imported-whatsapp-template-show-message-incomplete-in-the-composer}
「Message Incomplete」の警告は、必要なテンプレート変数スロットがコンポーザーで有効な値で入力されていない場合に表示されます。

[WhatsAppテンプレートビルダー]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder)を使用してテンプレートを作成すると、Brazeは変数を連番のプレースホルダー（{% raw %}`{{1}}`、`{{2}}`、`{{3}}`{% endraw %}など）に再採番します。MetaのWhatsApp マネージャーで外部的に作成されたテンプレートには、変数マッピングでエラーが発生しやすいパターンが含まれている場合があります。例えば：

- 非連番の番号付け（例：{% raw %}`{{1}}`、`{{3}}`、`{{5}}`{% endraw %}）
- シーケンス内の欠落した変数（例：{% raw %}`{{2}}`{% endraw %}のスキップ）
- 1以外の番号から始まる変数

これを解決するには、MetaのWhatsApp マネージャーでテンプレートを編集して連番のプレースホルダー形式を使用し、Brazeに再インポートしてください。Brazeで、各必須変数フィールドが有効なLiquid値で入力されていることを確認してください。

#### テンプレートがプレビューできるにもかかわらず、WhatsAppキャンペーンが送信されないのはなぜですか？ {#why-is-my-whatsapp-campaign-not-sending-despite-template-previewing}
テンプレートは正しくプレビューされるが、処理レジャーに**Abort**と「Param text cannot have new-line/tab characters or more than 4 consecutive spaces」という詳細が表示される場合は、メッセージ内のLiquidテンプレートパラメーター値を確認してください。WhatsAppでは、パラメーターテキストの値に以下が含まれないことが要求されます：

- 改行文字
- タブ文字
- 4つ以上の連続スペース

テンプレートパラメーターを入力するLiquidロジックが、送信前にこれらの文字を削除するか、テキストを適切にフォーマットすることを確認してください。

### 配信性と請求 {#deliverability-and-billing}

#### メッセージが配信されない理由は何ですか？ {#why-would-a-message-not-be-delivered}
メッセージが配信されない理由は、ネットワークの問題やデバイスの電源が切れているなど、さまざまです。

#### メッセージが配信されない場合、請求されますか？ {#if-a-message-is-not-delivered-will-i-be-billed}
いいえ。メッセージが配信されない場合、請求されません。

#### ユーザーが自分のビジネスをブロックした場合はどうなりますか？ {#what-happens-if-a-user-blocks-my-business}
ユーザーがビジネスをブロックした場合、その後のメッセージ送信は配信されず、請求もされません。ユーザーの購読ステータスは更新されません。

#### ユーザーがメッセージを報告した場合はどうなりますか？ {#what-happens-if-a-user-reports-a-message}
ユーザーがメッセージを報告した場合でも、そのユーザーにその後のメッセージを送信できます。ただし、報告はチャネル上の品質評価に影響する可能性があります。ユーザーの購読ステータスは更新されません。

#### WhatsAppアカウントを報告したユーザーを今後の配信から除外するにはどうすればよいですか？ {#how-can-i-exclude-users-who-report-my-whatsapp-account-from-upcoming-launches}
Brazeはアカウントがフラグされたり報告されたりした場合にWhatsAppから通知を受け取らないため、Brazeでそのようなユーザーを自動的に特定したり除外したりすることはできません。アカウントを報告したユーザーは、WhatsApp購読グループに残り、今後のメッセージの対象となり続ける可能性があります。

ただし、ユーザーがオプトアウトキーワードで返信した際にトリガーされるキャンペーンを設定し、[`/subscription/status/set`エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)を使用して自動的に購読解除することができます。詳細については、[WhatsAppのオプトインとオプトアウトプロセス]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-opt-in-and-opt-out-process)を参照してください。

#### WhatsApp配信が失敗した場合、BrazeはSMSへの自動フォールバックをサポートしていますか？ {#does-braze-support-automatic-sms-fallback-when-whatsapp-delivery-fails}

いいえ。BrazeではネイティブのWhatsApp-to-SMSフォールバックパスを提供していません。別のチャネルで再試行するには、WhatsApp送信に失敗したユーザーをセグメント化し（例えば、Currentsの失敗イベントを通じて）、SMSまたはメールキャンペーンをターゲティングしてください。

#### WhatsAppのレスポンスメッセージは無料ですか？ {#are-whatsapp-response-messages-free}

Brazeのキャンペーンまたはキャンバスエディターで作成されたレスポンスメッセージ（承認済みWhatsAppテンプレートではないもの）は、Metaによってサービスメッセージとして扱われます。2026年9月30日まで、BrazeのネイティブWhatsAppインテグレーションを通じて送信されるサービスメッセージは、オープンなカスタマーサービスウィンドウ内で[レスポンスメッセージ]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages)として送信された場合、アクションクレジットを消費しません。

2026年10月1日以降、サービスメッセージは配信されたメッセージごとにアクションクレジットを消費します。この分類はメッセージ自体に依存します。テンプレート化されていないレスポンスは、会話がテンプレートで開始された場合でもサービスメッセージです。承認済みのマーケティング、ユーティリティ、または認証テンプレートで返信した場合、メッセージはそのテンプレートカテゴリに従って課金されます。

| メッセージタイプ | アクションクレジット | 注記 |
|---|---|---|
| レスポンスメッセージ（インバウンド返信） | 2026年9月30日まで消費なし、2026年10月1日以降消費 | Brazeで作成。Meta承認テンプレートではありません。Metaはサービスメッセージとして分類します。 |
| テンプレートメッセージ | 消費 | マーケティング、ユーティリティ、認証、期間限定オファーテンプレートは送信ごとに課金されます。 |
| サービスウィンドウ内のユーティリティテンプレート | 2026年9月30日までMetaによる課金なし、2026年10月1日以降課金 | アクションクレジットの消費は契約に従います。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="レスポンスメッセージのアクションクレジット" }

元の24時間ウィンドウ後にユーザーがクイック返信をタップするキャンバスフローについては、[24時間ウィンドウ外のクイック返信とインバウンドメッセージ]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window)を参照してください。

#### 24時間ウィンドウが閉じた後にユーザーが返信またはクイック返信をタップした場合はどうなりますか？ {#what-happens-if-a-user-replies-or-taps-a-quick-reply-after-the-24-hour-window-closes}
新しい24時間のカスタマーサービスウィンドウが開きます。[24時間ウィンドウ外のクイック返信とインバウンドメッセージ]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window)を参照してください。

#### WhatsAppのクイック返信のために、キャンバスのアクションパスを31日間に設定する必要がありますか？ {#do-i-need-to-set-my-canvas-action-path-to-31-days-for-whatsapp-quick-replies}
いいえ。デフォルトのアクションパス期間で十分です。[24時間ウィンドウ外のクイック返信とインバウンドメッセージ]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window)を参照してください。

#### 特定のキャンペーンやキャンバスが消費したWhatsAppクレジットの数を確認できますか？ {#can-i-see-how-many-whatsapp-credits-a-specific-campaign-or-canvas-consumed}
現時点ではBrazeダッシュボードでは確認できません。キャンペーンとキャンバスの分析では送信数、配信数、失敗数は表示されますが、メッセージごとのクレジット消費は表示されません。テンプレートカテゴリとメッセージタイプによって課金方法が異なるため、送信数はクレジット使用量と1対1で一致しません。請求の詳細については、[WhatsAppのレスポンスメッセージは無料ですか？](#are-whatsapp-response-messages-free)を参照してください。

### インテグレーション、データ、レポート {#integrations-data-and-reporting}

#### テクノロジーパートナーの下にWhatsAppが表示されないのはなぜですか？ {#why-isnt-whatsapp-listed-under-technology-partners}
WhatsAppは、WhatsAppが会社に対して有効になっている場合に**テクノロジーパートナー**ページに表示されます。そのページにWhatsAppが表示されない場合は、Brazeアカウントチームに連絡して、ダッシュボードにWhatsAppがプロビジョニングされていることを確認してください。

#### BrazeはWhatsAppのチャットボットや有人チャットなどのカスタマーサポートのユースケースをサポートしていますか？ {#does-braze-support-customer-support-use-cases-like-chatbots-and-human-assisted-chat-for-whatsapp}
Braze内または直接インテグレーションを通じたチャットボットや有人チャットはサポートしていません。

すでにWhatsAppをカスタマーサポートチャネルとして使用している場合は、現在のセットアップを維持し、マーケティングメッセージング用にBraze経由で新しいWABAを作成することをお勧めします。このWABAには新しい電話番号が必要です。

#### BrazeでWhatsAppのサポートとマーケティングを連携するにはどうすればよいですか？ {#how-do-i-connect-whatsapp-support-and-marketing-in-braze}

WhatsAppのLiquidプロパティを使用して、インバウンドWhatsAppメッセージのコンテンツ（メッセージ本文やメディアURLを含む）をBrazeから他のプラットフォーム（カスタマーサポートツールを含む）に転送できます。詳細については、[サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)を参照してください。

Brazeに情報を送信する場合、例えばユーザーがアクティブなサポート会話中であることを示すには、カスタム属性（例：ブーリアン値「has existing support chat = true/false」）をログに記録し、マーケティングキャンペーンのセグメンテーション基準として使用できます。また、2つのチャットスレッド間をディープリンクで接続し、マーケティングスレッドからサポートスレッドへ、またその逆にユーザーを誘導することもできます。

#### Brazeはユーザーの返信を保存しますか？ {#does-braze-store-user-responses}
メッセージは処理に必要な期間のみ保存されます。ユーザーメッセージにアクセスするには、Currentsを使用してください。

#### Brazeダッシュボードではどのような指標が利用可能ですか？ {#what-metrics-are-available-in-the-braze-dashboard}
Brazeダッシュボードでは、ユニーク受信者数、送信数、配信数、既読数、失敗数を確認できます。Brazeが既読をトラッキングするには、ユーザーの既読確認が「オン」になっている必要があります。他のチャネルと同様に、キャンペーンのパフォーマンスを監視するためのコンバージョンイベントも設定できます。

#### WhatsAppの会話とは何ですか？ {#what-is-a-whatsapp-conversation}
WhatsAppは双方向メッセージングに焦点を当てたチャネルであるため、個々のメッセージの数ではなく会話を基準にしています。会話は、ビジネスとエンドユーザー間の24時間のスレッドです。

- **ビジネス発信の会話**：ビジネスがエンドユーザーに承認済みテンプレートメッセージを送信して開始する会話です。ビジネスがメッセージを送信すると、24時間ウィンドウが開始されます。
- **ユーザー発信の会話**：エンドユーザーがビジネスにメッセージを送信して開始する会話です。ビジネスが返信メッセージを送信すると、24時間ウィンドウが開始されます。

### メディアと画像 {#media-and-images}

#### WhatsAppメッセージとして送信された画像が読み込まれないのはなぜですか？ {#why-wont-images-load-when-sent-as-a-whatsapp-message}
WhatsAppメッセージ内の画像がダウンロードできない、またはダウンロードアイコンが反応しないとユーザーから報告された場合、これは古いバージョンのWhatsAppアプリにおける既知の問題が原因である可能性があります。この問題は通常、デバイスを最新バージョンのWhatsAppにアップグレードすることで解決できます。