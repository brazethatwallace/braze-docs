---
nav_title: メッセージクレジット - Delta
permalink: "/message_credits_delta_a3sy/"
hidden: true
noindex: true
hide_toc: true
---

# メッセージクレジット - Delta（機密） {#message-credits-delta-confidential}

> メッセージクレジットは、Brazeのネイティブエージェントコンソール、SMS、MMS、RCS、WhatsApp、LINE向けのクロスプロダクトパッケージング構造です。メッセージクレジットは、Brazeのメッセージングチャネルや特定のAI機能を活用する際に、柔軟で透明性の高いエクスペリエンスを提供します。クレジットにより、このページの表に記載されているすべてのチャネルにアクセスできます。

{% alert note %}
プロダクトごとにレポートの計測単位が異なります。<br><br>
<b>エージェントコンソール:</b> 呼び出し回数<br>
<b>SMS:</b> セグメント<br>
<b>MMS:</b> 送信数<br>
<b>WhatsApp:</b> 配信メッセージ数<br>
<b>RCS:</b> 配信セグメント数、配信送信数<br>
<b>LINE:</b> 送信数<br>
<b>KakaoTalk:</b> 送信数<br>

なお、SMS、MMS、RCSに関連するキャリア料金は別途（後払いで）請求され、このメッセージクレジットSKUの一部とはみなされません。
{% endalert %}

## 定義 {#definitions}

各列の定義は以下のとおりです。

|---------|-------------------------------------------------|
| **送信先** | Brazeプラットフォームを通じて送信される最終的な地域、国、またはアクションの種類 |
| **1送信あたりのクレジット** | 1回の送信に必要なメッセージクレジットの正確な数<br>（1送信あたりのクレジット = クレジット比率 × 送信先乗数） |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


## メッセージクレジット - Delta のクレジット比率表 {#credit-ratio-table-for-message-credits-delta}

{% details クリックして展開 %}
<table class="credits-table" aria-label="メッセージクレジット - Delta のクレジット比率表">
    <colgroup>
        <col span="3">
        <col class="col-highlight">
    </colgroup>
    <thead>
    <tr>
        <th><b>チャネル</b></th>
        <th><b>送信先</b></th>
        <th class="credits-column"><b>1送信あたりのクレジット</b></th>
    </tr>
    </thead>
    <tbody>
<tr>
        <td>エージェントコンソール</td>
        <td>Braze Auto</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>エージェントコンソール</td>
        <td>BYO LLM API Key</td>
        <td>0.16</td>
    </tr>
    <tr>
        <td>SMS - US / CA</td>
        <td>カナダ</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>SMS - US / CA</td>
        <td>カナダ トールフリー</td>
        <td>1.30</td>
    </tr>
    <tr>
        <td>SMS - US / CA</td>
        <td>アメリカ合衆国</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>SMS - US / CA</td>
        <td>アメリカ合衆国 トールフリー</td>
        <td>1.50</td>
    </tr>
    <tr>
        <td>MMS - US / CA</td>
        <td>カナダ ロングコード</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>MMS - US / CA</td>
        <td>カナダ ショートコード</td>
        <td>12.00</td>
    </tr>
    <tr>
        <td>MMS - US / CA</td>
        <td>カナダ トールフリー</td>
        <td>3.90</td>
    </tr>
    <tr>
        <td>MMS - US / CA</td>
        <td>アメリカ合衆国</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>MMS - US / CA</td>
        <td>アメリカ合衆国 トールフリー</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>アブハジア</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>アフガニスタン</td>
        <td>94.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>アルバニア</td>
        <td>22.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>アルジェリア</td>
        <td>52.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>米領サモア</td>
        <td>47.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>アンドラ</td>
        <td>33.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>アンゴラ</td>
        <td>22.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>アンギラ</td>
        <td>33.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>アンティグア・バーブーダ</td>
        <td>24.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>アルゼンチン</td>
        <td>10.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>アルメニア</td>
        <td>34.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>アルバ</td>
        <td>26.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>オーストラリア MMS</td>
        <td>31.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>オーストラリア SMS</td>
        <td>3.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>オーストリア</td>
        <td>17.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>アゼルバイジャン</td>
        <td>97.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>バハマ</td>
        <td>12.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>バーレーン</td>
        <td>9.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>バングラデシュ</td>
        <td>58.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>バルバドス</td>
        <td>30.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ベラルーシ</td>
        <td>63.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ベルギー</td>
        <td>24.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ベリーズ</td>
        <td>69.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ベナン</td>
        <td>36.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>バミューダ</td>
        <td>29.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ブータン</td>
        <td>101.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ボリビア</td>
        <td>36.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ボスニア・ヘルツェゴビナ</td>
        <td>21.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ボツワナ</td>
        <td>25.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ブラジル</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ブルネイ</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ブルガリア</td>
        <td>27.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ブルキナファソ</td>
        <td>33.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ブルンジ</td>
        <td>94.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>カンボジア</td>
        <td>43.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>カメルーン</td>
        <td>34.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>カーボベルデ</td>
        <td>36.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>カリブ海オランダ</td>
        <td>21.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ケイマン諸島</td>
        <td>33.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>中央アフリカ共和国</td>
        <td>30.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>チャド</td>
        <td>73.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>チリ</td>
        <td>16.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>中国</td>
        <td>6.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>コロンビア</td>
        <td>0.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>コモロ</td>
        <td>61.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>コンゴ</td>
        <td>50.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>クック諸島</td>
        <td>35.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>コスタリカ</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>クロアチア</td>
        <td>23.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>キューバ</td>
        <td>21.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>キュラソー</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>キプロス</td>
        <td>21.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>チェコ共和国</td>
        <td>10.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>デンマーク</td>
        <td>10.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ジブチ</td>
        <td>40.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ドミニカ国</td>
        <td>37.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ドミニカ共和国</td>
        <td>12.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>コンゴ民主共和国</td>
        <td>57.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>エクアドル</td>
        <td>27.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>エジプト</td>
        <td>24.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>エルサルバドル</td>
        <td>24.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>赤道ギニア</td>
        <td>43.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>エリトリア</td>
        <td>24.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>エストニア</td>
        <td>24.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>エスワティニ</td>
        <td>5.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>エチオピア</td>
        <td>86.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>フォークランド諸島</td>
        <td>34.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>フェロー諸島</td>
        <td>17.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>フィジー</td>
        <td>41.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>フィンランド</td>
        <td>14.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>フランス</td>
        <td>9.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>フランス領ギアナ</td>
        <td>46.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>フランス領ポリネシア</td>
        <td>45.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ガボン</td>
        <td>66.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ガンビア</td>
        <td>41.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ジョージア</td>
        <td>26.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ドイツ</td>
        <td>18.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ガーナ</td>
        <td>22.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ジブラルタル</td>
        <td>27.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ギリシャ</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>グリーンランド</td>
        <td>10.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>グレナダ</td>
        <td>40.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>グアドループ</td>
        <td>34.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>グアム</td>
        <td>17.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>グアテマラ</td>
        <td>32.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ガーンジー</td>
        <td>8.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ギニア</td>
        <td>38.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ギニアビサウ</td>
        <td>39.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ガイアナ</td>
        <td>45.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ハイチ</td>
        <td>59.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ホンジュラス</td>
        <td>21.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>香港</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ハンガリー</td>
        <td>19.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>アイスランド</td>
        <td>17.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>インド</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>インドネシア</td>
        <td>66.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>イラン</td>
        <td>62.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>イラク</td>
        <td>47.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>アイルランド</td>
        <td>13.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>マン島</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>イスラエル</td>
        <td>37.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>イタリア</td>
        <td>7.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>コートジボワール</td>
        <td>24.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ジャマイカ</td>
        <td>30.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>日本</td>
        <td>10.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ジャージー</td>
        <td>7.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ヨルダン</td>
        <td>55.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>カザフスタン</td>
        <td>55.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ケニア</td>
        <td>26.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>キリバス</td>
        <td>36.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>大韓民国</td>
        <td>6.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>コソボ</td>
        <td>9.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>クウェート</td>
        <td>33.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>キルギスタン</td>
        <td>61.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ラオス人民民主共和国</td>
        <td>15.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ラトビア</td>
        <td>18.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>レバノン</td>
        <td>30.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>レソト</td>
        <td>51.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>リベリア</td>
        <td>34.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>リビア</td>
        <td>81.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>リヒテンシュタイン</td>
        <td>8.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>リトアニア</td>
        <td>13.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ルクセンブルク</td>
        <td>18.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>マカオ</td>
        <td>14.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>マケドニア</td>
        <td>18.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>マダガスカル</td>
        <td>94.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>マラウイ</td>
        <td>57.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>マレーシア</td>
        <td>14.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>モルディブ</td>
        <td>18.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>マリ</td>
        <td>39.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>マルタ</td>
        <td>16.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>マーシャル諸島</td>
        <td>40.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>マルティニーク</td>
        <td>33.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>モーリタニア</td>
        <td>65.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>モーリシャス</td>
        <td>40.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>マヨット</td>
        <td>23.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>メキシコ</td>
        <td>2.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ミクロネシア</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>モルドバ</td>
        <td>15.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>モナコ</td>
        <td>46.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>モンゴル</td>
        <td>70.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>モンテネグロ</td>
        <td>28.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>モントセラト</td>
        <td>27.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>モロッコ</td>
        <td>26.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>モザンビーク</td>
        <td>27.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ミャンマー</td>
        <td>58.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ナミビア</td>
        <td>15.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ナウル</td>
        <td>11.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ネパール</td>
        <td>38.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>オランダ</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ニューカレドニア</td>
        <td>44.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ニュージーランド</td>
        <td>19.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ニカラグア</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ニジェール</td>
        <td>74.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ナイジェリア</td>
        <td>50.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ニウエ</td>
        <td>48.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ノーフォーク島</td>
        <td>7.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>北マケドニア</td>
        <td>3.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>北キプロス</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ノルウェー</td>
        <td>10.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>オマーン</td>
        <td>36.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>パキスタン</td>
        <td>74.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>パラオ</td>
        <td>25.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>パレスチナ自治区</td>
        <td>76.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>パナマ</td>
        <td>22.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>パプアニューギニア</td>
        <td>190.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>パラグアイ</td>
        <td>18.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ペルー</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>フィリピン</td>
        <td>2.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ポーランド</td>
        <td>5.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ポルトガル</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>プエルトリコ</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>カタール</td>
        <td>5.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>レユニオン/マヨット</td>
        <td>48.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ルーマニア</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ロシア</td>
        <td>95.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ルワンダ</td>
        <td>46.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>セントクリストファー・ネイビス</td>
        <td>9.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>セントルシア</td>
        <td>10.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>サンピエール島・ミクロン島</td>
        <td>23.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>セントビンセントおよびグレナディーン諸島</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>サモア</td>
        <td>46.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>サンマリノ</td>
        <td>27.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>サントメ・プリンシペ</td>
        <td>32.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>サウジアラビア</td>
        <td>19.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>セネガル</td>
        <td>51.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>セルビア</td>
        <td>60.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>セーシェル</td>
        <td>9.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>シエラレオネ</td>
        <td>47.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>シンガポール</td>
        <td>7.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>シント・マールテン</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>スロバキア</td>
        <td>22.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>スロベニア</td>
        <td>37.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ソロモン諸島</td>
        <td>20.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ソマリア</td>
        <td>47.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>南アフリカ</td>
        <td>3.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>南オセチア</td>
        <td>20.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>南スーダン</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>スペイン</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>スリランカ</td>
        <td>56.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>スーダン</td>
        <td>41.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>スリナム</td>
        <td>32.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>スワジランド</td>
        <td>23.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>スウェーデン</td>
        <td>8.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>スイス</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>シリア</td>
        <td>78.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>台湾</td>
        <td>8.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>タジキスタン</td>
        <td>113.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>タンザニア</td>
        <td>53.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>タイ</td>
        <td>3.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>東ティモール</td>
        <td>28.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>トーゴ</td>
        <td>38.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>トンガ</td>
        <td>31.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>トリニダード・トバゴ</td>
        <td>30.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>チュニジア</td>
        <td>70.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>トルコ</td>
        <td>7.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>トルクメニスタン</td>
        <td>50.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>タークス・カイコス諸島</td>
        <td>33.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ツバル</td>
        <td>33.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ウガンダ</td>
        <td>40.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ウクライナ</td>
        <td>28.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>アラブ首長国連邦</td>
        <td>12.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>英国</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>不明</td>
        <td>39.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ウルグアイ</td>
        <td>21.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ウズベキスタン</td>
        <td>68.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>バヌアツ</td>
        <td>41.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ベネズエラ</td>
        <td>21.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ベトナム</td>
        <td>30.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>英領ヴァージン諸島</td>
        <td>47.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>米領ヴァージン諸島</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ウォリス・フツナ</td>
        <td>27.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>イエメン</td>
        <td>60.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ザンビア</td>
        <td>67.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>ジンバブエ</td>
        <td>35.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>アルゼンチン 認証</td>
        <td>6.90</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>アルゼンチン マーケティング</td>
        <td>16.39</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>アルゼンチン マーケティング - BYO</td>
        <td>0.62</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>アルゼンチン マーケティング - 最適化配信</td>
        <td>16.39</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>アルゼンチン ユーティリティ</td>
        <td>6.90</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ブラジル 認証</td>
        <td>1.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ブラジル マーケティング</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ブラジル マーケティング - BYO</td>
        <td>0.63</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ブラジル マーケティング - 最適化配信</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ブラジル ユーティリティ</td>
        <td>1.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>チリ 認証</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>チリ マーケティング</td>
        <td>23.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>チリ マーケティング - BYO</td>
        <td>0.89</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>チリ マーケティング - 最適化配信</td>
        <td>23.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>チリ ユーティリティ</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>コロンビア 認証</td>
        <td>0.05</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>コロンビア マーケティング</td>
        <td>3.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>コロンビア マーケティング - BYO</td>
        <td>0.13</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>コロンビア マーケティング - 最適化配信</td>
        <td>3.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>コロンビア ユーティリティ</td>
        <td>0.05</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>エジプト 認証</td>
        <td>0.96</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>エジプト 認証 国際</td>
        <td>17.24</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>エジプト マーケティング</td>
        <td>28.47</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>エジプト マーケティング - BYO</td>
        <td>0.64</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>エジプト マーケティング - 最適化配信</td>
        <td>28.47</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>エジプト ユーティリティ</td>
        <td>1.38</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>フランス 認証</td>
        <td>7.96</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>フランス マーケティング</td>
        <td>37.99</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>フランス マーケティング - BYO</td>
        <td>0.86</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>フランス マーケティング - 最適化配信</td>
        <td>37.99</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>フランス ユーティリティ</td>
        <td>7.96</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ドイツ 認証</td>
        <td>14.59</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ドイツ マーケティング</td>
        <td>36.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ドイツ マーケティング - BYO</td>
        <td>1.37</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ドイツ マーケティング - 最適化配信</td>
        <td>36.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ドイツ ユーティリティ</td>
        <td>14.59</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>インド 認証</td>
        <td>0.37</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>インド 認証 国際</td>
        <td>7.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>インド マーケティング</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>インド マーケティング - BYO</td>
        <td>0.12</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>インド マーケティング - 最適化配信</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>インド ユーティリティ</td>
        <td>0.37</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>インドネシア 認証</td>
        <td>6.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>インドネシア 認証 国際</td>
        <td>36.08</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>インドネシア マーケティング</td>
        <td>10.90</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>インドネシア マーケティング - BYO</td>
        <td>0.41</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>インドネシア マーケティング - 最適化配信</td>
        <td>10.90</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>インドネシア ユーティリティ</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>イスラエル 認証</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>イスラエル マーケティング</td>
        <td>9.36</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>イスラエル マーケティング - BYO</td>
        <td>0.35</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>イスラエル マーケティング - 最適化配信</td>
        <td>9.36</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>イスラエル ユーティリティ</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>イタリア 認証</td>
        <td>7.96</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>イタリア マーケティング</td>
        <td>18.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>イタリア マーケティング - BYO</td>
        <td>0.69</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>イタリア マーケティング - 最適化配信</td>
        <td>18.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>イタリア ユーティリティ</td>
        <td>7.96</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>マレーシア 認証</td>
        <td>3.70</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>マレーシア 認証 国際</td>
        <td>11.09</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>マレーシア マーケティング</td>
        <td>22.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>マレーシア マーケティング - BYO</td>
        <td>0.86</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>マレーシア マーケティング - 最適化配信</td>
        <td>22.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>マレーシア ユーティリティ</td>
        <td>3.70</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>メキシコ 認証</td>
        <td>2.25</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>メキシコ マーケティング</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>メキシコ マーケティング - BYO</td>
        <td>0.31</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>メキシコ マーケティング - 最適化配信</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>メキシコ ユーティリティ</td>
        <td>2.25</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>オランダ 認証</td>
        <td>13.26</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>オランダ マーケティング</td>
        <td>42.37</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>オランダ マーケティング - BYO</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>オランダ マーケティング - 最適化配信</td>
        <td>42.37</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>オランダ ユーティリティ</td>
        <td>13.26</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ナイジェリア 認証</td>
        <td>1.78</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ナイジェリア 認証 国際</td>
        <td>19.90</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ナイジェリア マーケティング</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ナイジェリア マーケティング - BYO</td>
        <td>0.52</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ナイジェリア マーケティング - 最適化配信</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ナイジェリア ユーティリティ</td>
        <td>1.78</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>北米 認証</td>
        <td>1.06</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>北米 マーケティング</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>北米 マーケティング - BYO</td>
        <td>0.25</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>北米 マーケティング - 最適化配信</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>北米 ユーティリティ</td>
        <td>1.06</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他 認証</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他 マーケティング</td>
        <td>16.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他 マーケティング - BYO</td>
        <td>0.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他 マーケティング - 最適化配信</td>
        <td>16.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他 ユーティリティ</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>パキスタン 認証</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>パキスタン 認証 国際</td>
        <td>19.90</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>パキスタン マーケティング</td>
        <td>12.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>パキスタン マーケティング - BYO</td>
        <td>0.47</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>パキスタン マーケティング - 最適化配信</td>
        <td>12.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>パキスタン ユーティリティ</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ペルー 認証</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ペルー マーケティング</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ペルー マーケティング - BYO</td>
        <td>0.70</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ペルー マーケティング - 最適化配信</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ペルー ユーティリティ</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他アフリカ 認証</td>
        <td>1.06</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他アフリカ マーケティング</td>
        <td>5.97</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他アフリカ マーケティング - BYO</td>
        <td>0.23</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他アフリカ マーケティング - 最適化配信</td>
        <td>5.97</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他アフリカ ユーティリティ</td>
        <td>1.06</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他アジア太平洋 認証</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他アジア太平洋 マーケティング</td>
        <td>19.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他アジア太平洋 マーケティング - BYO</td>
        <td>0.73</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他アジア太平洋 マーケティング - 最適化配信</td>
        <td>19.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他アジア太平洋 ユーティリティ</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他中東欧 認証</td>
        <td>5.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他中東欧 マーケティング</td>
        <td>22.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他中東欧 マーケティング - BYO</td>
        <td>0.86</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他中東欧 マーケティング - 最適化配信</td>
        <td>22.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他中東欧 ユーティリティ</td>
        <td>5.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他ラテンアメリカ 認証</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他ラテンアメリカ マーケティング</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他ラテンアメリカ マーケティング - BYO</td>
        <td>0.74</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他ラテンアメリカ マーケティング - 最適化配信</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他ラテンアメリカ ユーティリティ</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他メッセージタイプ - BYO</td>
        <td>0.10</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他中東 認証</td>
        <td>2.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他中東 マーケティング</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他中東 マーケティング - BYO</td>
        <td>0.34</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他中東 マーケティング - 最適化配信</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他中東 ユーティリティ</td>
        <td>2.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他西欧 認証</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他西欧 マーケティング</td>
        <td>15.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他西欧 マーケティング - BYO</td>
        <td>0.59</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他西欧 マーケティング - 最適化配信</td>
        <td>15.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>その他西欧 ユーティリティ</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ロシア 認証</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ロシア マーケティング</td>
        <td>21.28</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ロシア マーケティング - BYO</td>
        <td>0.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ロシア マーケティング - 最適化配信</td>
        <td>21.28</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>ロシア ユーティリティ</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>サウジアラビア 認証</td>
        <td>3.05</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>サウジアラビア 認証 国際</td>
        <td>15.86</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>サウジアラビア マーケティング</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>サウジアラビア マーケティング - BYO</td>
        <td>0.46</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>サウジアラビア マーケティング - 最適化配信</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>サウジアラビア ユーティリティ</td>
        <td>3.05</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>南アフリカ 認証</td>
        <td>2.84</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>南アフリカ 認証 国際</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>南アフリカ マーケティング</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>南アフリカ マーケティング - BYO</td>
        <td>0.38</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>南アフリカ マーケティング - 最適化配信</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>南アフリカ ユーティリティ</td>
        <td>2.84</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>スペイン 認証</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>スペイン マーケティング</td>
        <td>16.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>スペイン マーケティング - BYO</td>
        <td>0.62</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>スペイン マーケティング - 最適化配信</td>
        <td>16.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>スペイン ユーティリティ</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>トルコ 認証</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>トルコ マーケティング</td>
        <td>2.89</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>トルコ マーケティング - BYO</td>
        <td>0.11</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>トルコ マーケティング - 最適化配信</td>
        <td>2.89</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>トルコ ユーティリティ</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>アラブ首長国連邦 認証</td>
        <td>4.17</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>アラブ首長国連邦 認証 国際</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>アラブ首長国連邦 マーケティング</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>アラブ首長国連邦 マーケティング - BYO</td>
        <td>0.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>アラブ首長国連邦 マーケティング - 最適化配信</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>アラブ首長国連邦 ユーティリティ</td>
        <td>4.17</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>英国 認証</td>
        <td>5.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>英国 マーケティング</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>英国 マーケティング - BYO</td>
        <td>0.53</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>英国 マーケティング - 最適化配信</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>英国 ユーティリティ</td>
        <td>5.80</td>
    </tr>
    <tr>
        <td>LINE</td>
        <td>全リージョン</td>
        <td>0.15</td>
    </tr>
    <tr>
        <td>KakaoTalk</td>
        <td>全リージョン</td>
        <td>0.20</td>
    </tr>
    <tr>
        <td>Webhook</td>
        <td>スタンダード</td>
        <td>0.08</td>
    </tr>
    <tr>
        <td>BYO SMS コネクター</td>
        <td>Infobip - 全リージョン</td>
        <td>0.30</td>
    </tr>
    <tr>
        <td>BYO SMS コネクター</td>
        <td>Twilio - 全リージョン</td>
        <td>0.30</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>ブラジル - Basic</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>ブラジル - Single</td>
        <td>3.50</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>コロンビア - Basic</td>
        <td>1.90</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>コロンビア - Single</td>
        <td>2.40</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>フランス - Basic</td>
        <td>12.60</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>フランス - Single</td>
        <td>12.60</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>ドイツ - Basic</td>
        <td>12.50</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>ドイツ - Single</td>
        <td>12.80</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>イタリア - Basic</td>
        <td>4.70</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>イタリア - Single</td>
        <td>6.70</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>メキシコ - Basic</td>
        <td>6.10</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>メキシコ - Single</td>
        <td>6.90</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>シンガポール - Basic</td>
        <td>4.30</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>シンガポール - Single</td>
        <td>8.30</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>スペイン - Basic</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>スペイン - Single</td>
        <td>13.90</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>スウェーデン - Basic</td>
        <td>7.20</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>スウェーデン - Single</td>
        <td>10.30</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>英国 - Basic</td>
        <td>7.80</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>英国 - Single</td>
        <td>14.10</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>アメリカ合衆国 - Basic - 非推奨</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>アメリカ合衆国 - Rich</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>アメリカ合衆国 - Rich Media</td>
        <td>1.30</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>アメリカ合衆国 - Single - 非推奨</td>
        <td>1.30</td>
    </tr>
    </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% enddetails %}

------
## エージェントコンソールの詳細 {#agent-console-details}
Brazeは、Brazeプラットフォームから送信されたエージェントコンソールの呼び出しに対してメッセージクレジットを課金します。呼び出しは、エージェントがLLMへのコールを開始した時点で記録されます。デフォルトでは、契約にはサブスクリプション期間の各期間ごとに1万回の呼び出しが含まれています。

## SMS/MMSチャネルの詳細 {#smsmms-channel-details}

### SMSセグメント {#sms-segments}

SMSメッセージセグメントは、SMS業界でメッセージをカウントする方法です。メッセージセグメントとは、定義された文字数（GSM-7エンコーディングでは160文字、UCS-2エンコーディングでは67文字）までのグループであり、1回のSMS送信で送られます。GSM-7エンコーディングを使用して161文字のSMSを送信した場合、2つのメッセージセグメントが送信されたことになります。複数のメッセージセグメントを送信すると、追加料金が発生します。

### MMSセグメント {#mms-segments}

MMSの場合、メッセージの上限は5 MB（マルチメディアアセットとメッセージ本文のサイズを含む）です。安全のため、Brazeではマルチメディアアセットを600 KB以下に抑え、メッセージ本文も含めることを推奨しています。

### RCSの種類 {#rcs-types}

RCSは、SMSとMMSの次世代版です。SMSのような直接的で高エンゲージメントなチャネルの利点を備えつつ、リッチコンテンツ（画像、動画、ドキュメント）、認証済みおよびブランド付き送信、おすすめの返信やアクションなどのインタラクティブ機能など、現代の消費者が期待するよりリッチな機能を提供します。

- RCSの課金は、2つの異なるメッセージタイプを中心としています（米国向けの区別あり）：
    - **Basic RCS：** テキストのみ、最大160文字
    - **Single RCS：** リッチコンテンツを含むメッセージ、または160文字を超えるテキストのみのメッセージ
    - **Rich RCS（米国のみ）：** テキストのみ、限定的なサジェスチョン/ボタン（quickReply、dialPhone、webviewなしのopenURL）を含む場合があり、160 UTF-8バイトごとにセグメント化
    - **Rich Media RCS（米国のみ）：** メディアを含むメッセージ、またはよりリッチなサジェスチョン/ボタン（webview、位置情報、カレンダーなど）を含むテキスト。1メッセージとしてカウント

## WhatsAppチャネルの詳細 {#whatsapp-channel-details}

{% multi_lang_include whatsapp/about_credits.md content="h3" %}

## その他のチャネルの詳細 {#additional-channel-details}

### Webhook {#webhooks}

Webhookは2024年12月9日にメッセージクレジットの対象となりました。Brazeは、Brazeプラットフォームから送信されたすべてのwebhookに対してメッセージクレジットを課金します。デフォルトでは、契約にはサブスクリプション期間の各期間ごとに10万件のwebhookが含まれています。追加のwebhookは、注文書に従って課金されます。

### 自社SMS（BYO SMS）コネクター {#bring-your-own-byo-sms-connectors}

Brazeでは、「BYO SMSコネクター」モデルを通じて、サードパーティプロバイダーと統合してSMSメッセージを送信できます。Brazeは、BYO SMSコネクターを通じてBrazeプラットフォームから送信された各メッセージに対してメッセージクレジットを課金します。

### LINE

Brazeは、Brazeプラットフォームから送信されたすべてのLINEメッセージに対してメッセージクレジットを課金します。

## 課金リージョンの内訳 {#billing-region-breakdown}

### 北米 {#north-america}

米国、カナダ

### その他のアフリカ {#rest-of-africa}

アルジェリア、アンゴラ、ベナン、ボツワナ、ブルキナファソ、ブルンジ、カメルーン、チャド、コンゴ、エリトリア、エチオピア、ガボン、ガンビア、ガーナ、ギニアビサウ、コートジボワール、ケニア、レソト、リベリア、リビア、マダガスカル、マラウイ、マリ、モーリタニア、モロッコ、モザンビーク、ナミビア、ニジェール、ルワンダ、セネガル、シエラレオネ、ソマリア、南スーダン、スーダン、エスワティニ、タンザニア、トーゴ、チュニジア、ウガンダ、ザンビア

### その他のアジア太平洋 {#rest-of-asia-pacific}

アフガニスタン、オーストラリア、バングラデシュ、カンボジア、中国、日本、ラオス、モンゴル、ネパール、ニュージーランド、パプアニューギニア、フィリピン、スリランカ、台湾、タジキスタン、タイ、トルクメニスタン、ウズベキスタン、ベトナム

### その他の中央・東ヨーロッパ {#rest-of-central-eastern-europe}

アルバニア、アルメニア、アゼルバイジャン、ベラルーシ、ブルガリア、クロアチア、チェコ共和国、ジョージア、ギリシャ、ラトビア、リトアニア、マケドニア、モルドバ、セルビア、スロバキア、スロベニア、ウクライナ

### その他のラテンアメリカ {#rest-of-latin-america}

ボリビア、コスタリカ、ドミニカ共和国、エクアドル、エルサルバドル、グアテマラ、ハイチ、ホンジュラス、ジャマイカ、ニカラグア、パナマ、パラグアイ、プエルトリコ、ウルグアイ、ベネズエラ

### その他の中東 {#rest-of-middle-east}

バーレーン、イラク、ヨルダン、クウェート、レバノン、オマーン、イエメン

### その他の西ヨーロッパ {#rest-of-western-europe}

オーストリア、ベルギー、デンマーク、フィンランド、アイルランド、ノルウェー、ポルトガル、スウェーデン、スイス