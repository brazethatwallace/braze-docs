---
nav_title: キャンバスの概要
article_title: キャンバスの概要
page_order: 0.5
page_type: reference
description: "このリファレンス記事では、4つの便利なキャンバスのユースケースについて説明します。"
tool: Canvas

---

# キャンバスの概要 {#canvas-outlines}

> この記事では、[遅延]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)ステップと[メッセージ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)ステップを組み合わせて、ターゲットを絞ったパーソナライズ済みメッセージングを実現するためにキャンバスを活用する方法を、いくつかの例を通じてご紹介します。

[![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/page/courses){: style="float:right;width:120px;border:0;" class="noimgborder"}

Brazeラーニングでは、一般的なキャンバスの概要を扱う専用コースもいくつか提供しています。動画、レッスン、インタラクティブな演習を組み合わせた、技術用語やコンセプトに関する貴重なインサイトをぜひご確認ください。

- [キャンバスフローでカスタマージャーニーを作成する](https://learning.braze.com/create-customer-journeys-with-canvas-flow)
- [新規ロイヤルティメンバーのオンボーディング](https://learning.braze.com/new-loyalty-member-onboarding)
- [離脱ユーザー](https://learning.braze.com/lapsing-users)
- [放棄カートのユーザージャーニーを構築する](https://learning.braze.com/build-an-abandoned-cart-user-journey)

## オンボーディング {#onboarding}

たとえば、レストランがユーザーの初回予約をサポートするオンボーディングを行いたいとします。このキャンバスはオンボーディング専用なので、キャンバスの起動に最適なタイミングは、すべての新規顧客のセッション開始時です。ダイニングのオーディエンスに素早く効果的にリーチするために、SMSメッセージングチャネルを活用できます。

![オンボーディングに関連するスクリーンショット]({% image_buster /assets/img_archive/canvas_outline_onboarding.png %}){: style="max-width:90%;"}

### アップセル {#upsell}

効果的なキャンバスを構築・送信することで、サブスクリプションのアップセルを促進することもできます。たとえば、アプリの無料版を利用しているアクティブユーザーをアップグレードしたい場合、顧客がカスタムイベント「3時間ストリーミング」に到達したときにトリガーされるアクションベースのキャンバスを作成できます。メッセージステップを使用して、これらの顧客にプレミアムサブスクリプションへの登録を促すことができます。

![効果的なキャンバスを構築・送信することで、サブスクリプションのアップセルを促進することもできます。たとえば、アプリの無料版を利用しているアクティブユーザーをアップグレードしたい場合、顧客がカスタムイベント「3時間ストリーミング」に到達したときにトリガーされるアクションベースのキャンバスを作成できます。メッセージステップを使用して、これらの顧客にプレミアムサブスクリプションへの登録を促すことができます。]({% image_buster /assets/img_archive/canvas_outline_upsell.png %}){: style="max-width:90%;"}

### 放棄カート {#abandoned-carts}

小売ビジネスでは、未完了の購入について顧客にリマインドする必要が頻繁に生じます。アクションベースのキャンバスを使用すると、登録済みのすべての顧客に対して、放棄カート内のアイテムの購入を促すリマインダーを送信できます。また、異なる遅延時間を設定することで、メッセージングに対する顧客の反応をテストすることもできます。

![放棄カートに関連するスクリーンショット]({% image_buster /assets/img_archive/canvas_outline_cart.png %}){: style="max-width:90%;"}

### 顧客向けリソース {#customer-resources}

キャンバスを使用して、顧客にリソースに関する情報を提供できます。たとえば、航空会社の場合、3日後に旅行を予約している顧客に対して、フライト情報と関連する空港のFAQを含む週次メールをスケジュールするキャンバスを作成し、事前に情報を届けることができます。

![キャンバスを使用して、顧客にリソースに関する情報を提供できます。たとえば、航空会社の場合、3日後に旅行を予約している顧客に対して、フライト情報と関連する空港のFAQを含む週次メールをスケジュールするキャンバスを作成し、事前に情報を届けることができます。]({% image_buster /assets/img_archive/canvas_outline_resource.png %}){: style="max-width:90%;"}