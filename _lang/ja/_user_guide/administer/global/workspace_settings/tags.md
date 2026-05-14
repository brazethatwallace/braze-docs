---
nav_title: タグの管理
article_title: タグの管理
page_order: 6
page_type: reference
description: "このリファレンス記事では、Brazeダッシュボードでのタグの管理方法について説明します。タグのネスト、名前変更、Campaigns、Canvases、Segments全体でのタグの整理などを取り上げます。"
---

# タグの管理 {#managing-tags}

> Campaigns、Canvases、Segments全体で使用するタグを一元的に管理できます。タグの名前変更、削除、追加を行うには、**設定** > **タグ管理**に移動します。

Campaigns、Canvases、Segments、カスタムデータにタグを追加する方法については、[タグ]({{site.baseurl}}/user_guide/messaging/governance/tags/)を参照してください。

## タグのネスト {#nesting-tags}

タグをさらに整理するために、親タグの下にネストできます。たとえば、すべてのホリデータグを親タグ `Holidays` の下にネストしたり、マーケティングファネルのステージに関連するすべてのタグを親タグ `Funnel` の下にネストしたりできます。

![ネストされたグループごとに整理されたタグのリストを表示するタグ管理ページ。]({% image_buster /assets/img_archive/tags_view.png %})

新しいタグをネストするには、タグを作成し、**Nest Tag Under**を選択して、新しいタグをネストする既存のタグを選択します。

既存のタグをネストするには、**タグ管理**ページに移動し、タグのある行にカーソルを合わせて**<i class="fas fa-pencil-alt"></i>Edit**を選択します。次に、**Nest Tag Under**を選択して親タグを選択します。

![「Nest Tag Under」オプションが選択された新しいタグダイアログ。]({% image_buster /assets/img_archive/tag_nested.png %}){: style="max-width:70%;" }

## ベストプラクティス {#tags-best-practices}

タグを使用して、Campaigns、Canvases、Segmentsをビジネス目標、ファネルステージ、地域などで整理します。

次の表は、eコマースアプリで役立つタグの例を示しています。

<style>
table td {
    word-break: break-word;
}
</style>


<table aria-label="Best practices #tags-best-practices">
  <caption>ベストプラクティス</caption>
<thead>
  <tr>
    <th>ファネル</th>
    <th>ビジネス目標</th>
    <th>地域</th>
    <th>Campaigns</th>
    <th>ホリデー</th>
    <th>トランザクション</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>On-boarding<br>Re-engagement<br>Loyal<br>PowerUser<br>Churn<br>Lost</td>
    <td>HighSpender<br>ActiveUser<br>NewUsers<br>FacebookAttribution<br>FirstAction</td>
    <td>UnitedStates<br>Northeast<br>Midwest<br>South<br>West<br>LATAM<br>AP<br>WesternEurope<br>MiddleEast</td>
    <td>Sales<br>Coupons<br>Events</td>
    <td>MLK<br>SuperBowl<br>PiDay<br>StPatricksDay<br>MarchMadness<br>Easter<br>Passover<br>MothersDay<br>MemorialDay<br>FathersDay<br>FourthJuly<br>LaborDay<br>VeteransDay<br>ColumbusDay<br>PresidentsDay<br>Halloween<br>RoshHashanah<br>Thanksgiving<br>Christmas<br>Hanukkah<br>NewYears</td>
    <td>Transactional<br>Notification<br>ConnectedActionTaken</td>
  </tr>
</tbody>
</table>

## ユースケース {#use-cases}

以下は、メッセージングライフサイクルを管理するためにタグを使用する一般的なユースケースです。

{% tabs %}
{% tab スロットリング %}

### スロットリング {#throttling}

顧客が特定の種類のCampaignを受信する頻度を制限します。たとえば、プロモーションCampaignの頻度を制限するために、次のフィルターを設定できます。

`Last received campaign` にタグ `Promo` が付いたものを5日以上前に受信
<br>`OR`<br>
`Has not received campaign` にタグ `Promo` が付いたもの

{% endtab %}
{% tab レポート %}

### レポート {#reporting}

エンゲージメントレポートを設定して、特定のタグが付いたすべてのCampaignのボリュームを監視します。たとえば、すべてのプッシュCampaignを監視したい場合は、それらのCampaignに `Push Reporting` のようなタグを追加し、[エンゲージメントレポート]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports/#automatically-select-campaigns-or-canvases)を設定して、タグ付けされたCampaignのレポートを毎日送信するようにできます。

{% endtab %}
{% endtabs %}