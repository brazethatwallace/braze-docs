---
nav_title: タグ
article_title: タグ
page_order: 6
page_type: reference
description: "このリファレンス記事では、Brazeダッシュボードでのキャンペーン、Canvases、セグメント、カスタムデータのタグについて説明します。"
tool:
  - Campaigns
  - Canvas
---

# タグ {#tags}

> Brazeは、Segments、Campaigns、Canvasesの作成者、エディター、日付、ステータス情報を追跡し、エンゲージメントをさらに整理・分類するためのタグを作成する機能を提供します。

## Campaign、Canvas、Segmentのタグ {#campaign-canvas-and-segment-tags}

Campaign、Canvas、またはSegmentの作成時や編集時にタグを追加できます。エンゲージメント名の下にある<span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tags**をクリックし、既存のタグを選択するか、入力を開始して新しいタグを追加します。

![Campaign作成時にタグを追加する。]({% image_buster /assets/img_archive/tags_add_tag.png %}){: style="max-width:60%;" }

{% alert important %}
Campaign、Canvas、またはSegmentには最大175個のタグを追加できます。
{% endalert %}

### 一括タグ付け {#bulk-tagging}

複数のCampaigns、Canvases、またはSegmentsを選択し、<span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tag As**を選択することで、一括でタグを追加することもできます。

![複数のCampaignsに同時にタグを追加する。]({% image_buster /assets/img_archive/tags_apply_multiple.gif %})

{% alert important %}
一括タグ付けを使用して、すでに異なるタグが設定されている複数のCampaignsに新しいタグを適用すると、選択した各Campaignに新しいタグが追加され、いずれかのCampaignに存在するタグが、元々関連付けられていなかった場合でも、選択した他のすべてのCampaignsに適用されます。
{% endalert %}

### タグの表示 {#viewing-tags}

Campaign、Canvas、またはSegmentに設定されたタグは、エンゲージメント名の近くにある詳細ページで確認できます。また、Campaign分析にも表示されます。

![Campaign分析ページに表示されるタグ。]({% image_buster /assets/img_archive/tag_details_page.png %}){: style="max-width:60%;" }

### タグによるフィルタリング {#filtering-by-tag}

タグは、Campaigns、Canvases、またはSegmentsのリストに、**Archived**や**Draft**などのステータスラベルの追加タグとともに表示されます。タグでフィルタリングするには、タグのリストからタグ名を選択します。

![Campaignsのリストに表示されるタグ。]({% image_buster /assets/img_archive/tags_grid.png %})

## カスタムデータのタグ {#custom-data-tags}

[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#managing-custom-attributes)や[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events#adding-tags)を管理する際に、カスタムデータにタグを追加することもできます。

{% alert important %}
この機能は現在、早期アクセス段階です。この早期アクセスへの参加に興味がある場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

ダッシュボード全体でのタグの名前変更、削除、ネストについては、[タグの管理]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags#managing-tags)を参照してください。