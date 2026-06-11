---
nav_title: タグの管理
article_title: タグの管理
page_order: 6
page_type: reference
description: "このリファレンス記事では、Brazeダッシュボードでのタグの管理方法について説明します。タグのネスト、名前変更、キャンペーン、Canvas、Segment全体でのタグの整理などを取り上げます。"
---

# タグの管理 {#managing-tags}

> キャンペーン、Canvas、Segment全体で使用するタグを一元的に管理できます。タグの名前変更、削除、追加を行うには、**設定** > **タグ管理**に移動します。

キャンペーン、Canvas、Segment、カスタムデータにタグを追加する方法については、[タグ]({{site.baseurl}}/user_guide/messaging/governance/tags/)を参照してください。

## タグのネスト {#nesting-tags}

タグをさらに整理するために、親タグの下にネストできます。たとえば、すべてのホリデータグを親タグ `Holidays` の下にネストしたり、マーケティングファネルのステージに関連するすべてのタグを親タグ `Funnel` の下にネストしたりできます。

![ネストされたグループごとに整理されたタグのリストを表示するタグ管理ページ。]({% image_buster /assets/img_archive/tags_view.png %})

新しいタグをネストするには、タグを作成し、**Nest Tag Under**を選択して、新しいタグをネストする既存のタグを選択します。

既存のタグをネストするには、**タグ管理**ページに移動し、タグのある行にカーソルを合わせて**<i class="fas fa-pencil-alt"></i>Edit**を選択します。次に、**Nest Tag Under**を選択して親タグを選択します。

### 親タグが使用中だが **Nest Tag Under** に表示されない場合 {#parent-tag-is-in-use-but-missing-from-nest-tag-under}

親タグがダッシュボードで適用されているにもかかわらず、新しいタグの作成時に **Nest Tag Under** ドロップダウンに表示されない場合は、その親タグをスタンドアロンタグとして再作成して、リストで検索可能にしてください。この動作は、親タグがワークスペース内の別の場所でネストされた依存関係としてのみ存在する場合に想定される動作です。

![「Nest Tag Under」オプションが選択された新しいタグダイアログ。]({% image_buster /assets/img_archive/tag_nested.png %}){: style="max-width:70%;" }

## ベストプラクティス {#tags-best-practices}

タグを使用して、キャンペーン、Canvas、Segmentをビジネス目標、ファネルステージ、地域などで整理します。

次の表は、eコマースアプリで役立つタグの例を示しています。

<style>
table td {
    word-break: break-word;
}
</style>


<table aria-label="ベストプラクティス">
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

顧客が特定の種類のキャンペーンを受信する頻度を制限します。たとえば、プロモーションキャンペーンの頻度を制限するために、次のフィルターを設定できます。

`Last received campaign` にタグ `Promo` が付いたものを5日以上前に受信
<br>`OR`<br>
`Has not received campaign` にタグ `Promo` が付いたもの

{% endtab %}
{% tab レポート %}

### レポート {#reporting}

エンゲージメントレポートを設定して、特定のタグが付いたすべてのキャンペーンのボリュームを監視します。たとえば、すべてのプッシュキャンペーンを監視したい場合は、それらのキャンペーンに `Push Reporting` のようなタグを追加し、[エンゲージメントレポート]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports/#automatically-select-campaigns-or-canvases)を設定して、タグ付けされたキャンペーンのレポートを毎日送信するようにできます。

{% endtab %}
{% endtabs %}