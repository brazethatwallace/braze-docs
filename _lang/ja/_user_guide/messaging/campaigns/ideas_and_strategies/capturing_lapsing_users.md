---
nav_title: 離脱ユーザーの獲得
article_title: 離脱ユーザーの獲得
page_order: 1
page_type: tutorial
description: "このハウツー記事では、離脱ユーザーの問題と、Braze Campaignsを効果的に使用してそれらのユーザーを再エンゲージする方法について説明します。"
tool:
  - Segments
  - Campaigns

---

# 離脱ユーザーの獲得 {#capture-lapsing-users}

> オーディエンスが減少している場合、呼び戻す取り組みが非常に重要です。Brazeを使用すると、自動化された定期的なリエンゲージメントCampaignsを設定して、離脱ユーザーを獲得できます。アプリに最適なリエンゲージメントの期間と頻度を選択できますが、ここでは例として14日間のリエンゲージメントプランを紹介します。

ユーザーのターゲティングの詳細については、Campaignのセットアップに関する[Brazeラーニングコース](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)をご覧ください。

## ステップ 1:ユーザーをセグメント化する {#step-1-segment-users}

まず、以下のフィルターを使用して、過去2週間アプリを使用していないユーザーをターゲットとするSegmentを作成します。

- **最後にアプリを使用した日**が2週間以上前
- **最後にアプリを使用した日**が3週間未満前

![ステップ1に関連するスクリーンショット：ユーザーのセグメント化。]({% image_buster /assets/img_archive/2weeklapse1.png %}){: style="max-width:70%;"}

Segmentに「Lapsed Users – 2 Weeks」のような覚えやすい名前を付けます。Campaignを毎週繰り返すように設定するため、Segmentに少なくとも1週間分のユーザーが含まれるようにする必要があります。そのため、最後にアプリを使用したのが2〜3週間前のユーザーを選択しています。

## ステップ 2:Campaignを作成する {#step-2-create-a-campaign}

次に、**キャンペーンを作成**をクリックし、このSegmentに送信するCampaignの種類を選択します。この例では、新しい[プッシュCampaign]({{site.baseurl}}/user_guide/channels/push/create_a_push_message)を作成します。

![「キャンペーンを作成」をクリックし、このSegmentに送信するCampaignの種類を選択します。この例では、新しいプッシュCampaignを作成します。]({% image_buster /assets/img_archive/2weeklapse2.png %}){: style="max-width:70%;"}

Campaignに「Message to Lapsed Users - 2 Weeks」と名前を付け、メッセージのコンテンツを作成します。この例ではiOSユーザーのみをターゲットにしますが、BrazeはAndroidとiOSの両方のプッシュ通知に使用できます。

ユーザーが最後にアプリを使用した時期が近いほど、タイムリーで関連性の高いコンテンツが重要になります。2週間アプリを使用していないユーザーにメッセージを送る場合、関連性のあるコンテンツを表示し、アプリを使用するメリットを強調することが大切です。

![ステップ2に関連するスクリーンショット：Campaignの作成。]({% image_buster /assets/img_archive/2weeklapse3.png %}){: style="max-width:70%;"}

次に、**時間ベースのスケジューリングオプション**で[ローカルタイムゾーン配信]({{site.baseurl}}/help/faqs#what-does-local-time-zone-delivery-offer)を使用して、毎週木曜日の午後5時45分にメッセージを送信する定期スケジュールを作成します。セッショングラフを確認して、利用率が高い時間帯の直前にユーザーをターゲットにすることをお勧めします。これにより、ユーザーがアプリを使用する可能性が最も高いタイミングでリエンゲージメントを試みることができます。この設定は後から変更でき、最初の仮説をテストすることも可能です。

![時間ベースのスケジューリングオプションでローカルタイムゾーン配信を使用して、毎週木曜日の午後5時45分にメッセージを送信する定期スケジュールを作成します。セッショングラフを確認して、利用率が高い時間帯の直前にユーザーをターゲットにすることをお勧めします。]({% image_buster /assets/img_archive/2weeklapse4.png %}){: style="max-width:70%;"}

## ステップ 3:Campaignを起動する {#step-3-launch-the-campaign}

これでCampaignを送信する準備が整いました。コンポーザーの最後のページで設定を確認し、**キャンペーンを起動**をクリックしてください。