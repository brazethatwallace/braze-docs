---
nav_title: ナビゲーションディープリンク
article_title: Braze Pilotのナビゲーションディープリンク
page_order: 4
page_type: reference
description: "この参照記事では、エンジニアや開発者に必要な統合ステップを簡単に説明します。"
---

# Braze Pilotのナビゲーションディープリンク {#navigation-deep-links-in-braze-pilot}

> Braze Pilotは、BrazeメッセージングからPilotアプリの特定の部分へのディープリンクをサポートしています。これにより、エンゲージメントのユースケースを作成し、ユーザーをPilotアプリケーションのさまざまな部分に誘導できます。また、オプションのディープリンクパラメーターを使用して、アプリ内の特定のページのコンテンツをユーザーに合わせてカスタマイズすることもできます。ディープリンクの詳細については、[アプリ内コンテンツへのディープリンク]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#what-is-deep-linking)を参照してください。

## 全般 {#general}

これらは、Pilotアプリのメインナビゲーションページのディープリンクです。

| 画面 | ディープリンク |
| --- | --- |
| プロジェクト | `braze-pilot://navigation/projects` |
| ログデータ | `braze-pilot://navigation/logdata` |
| 設定 | `braze-pilot://navigation/setup` |
| 言語の変更 | `braze-pilot://navigation/selectlanguage` |
| カメラ | `braze-pilot://navigation/camera` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="全般" }

## Steppington
これらは、PilotにおけるSteppington架空ブランドアプリのディープリンクです。

### ディープリンクの例 {#steppington-example-deep-link}

`braze-pilot://navigation/steppington/workout?title=Running&icon=HEART_DETAILS&image=https://picsum.photos/400&info=This%20workout%20is%20awesome%21&workout=5k%20Run&calories=600&length=25&workout_info_left_text=Road%20Run&workout_info_left_icon=RUNNING_HOME&workout_info_center_text=120%20BPM&workout_info_center_icon=HEART_DETAILS&workout_info_right_text=25%3A00&workout_info_right_icon=TIMER_DETAILS`

### パラメーターなしのディープリンク {#steppington-deep-links-without-parameters}

| 画面 | ディープリンク |
| --- | --- |
| スプラッシュスクリーン | `braze-pilot://navigation/steppington/splash` |
| ホーム | `braze-pilot://navigation/steppington/home` |
| Steppington+ページ | `braze-pilot://navigation/steppington/plus` |
| 目標画面 | `braze-pilot://navigation/steppington/goals` |
| 目標変更画面 | `braze-pilot://navigation/steppington/changegoals` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="パラメーターなしのディープリンク" }

### パラメーター付きのディープリンク {#steppington-deep-links-with-parameters}

| 画面 | ディープリンク |
| --- | --- |
| ワークアウト | `braze-pilot://navigation/steppington/workout` |
| アクティブワークアウト | `braze-pilot://navigation/steppington/activeworkout` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="パラメーター付きのディープリンク" }

#### 使用可能なパラメーター {#steppington-accepted-parameters}

<style>
table td {
    word-break: break-word;
}
th:nth-child(1), td:nth-child(1) {
    width: 22%;
}
th:nth-child(2), td:nth-child(2) {
    width: 30%;
}
th:nth-child(3), td:nth-child(3) {
    width: 8%;
}
th:nth-child(4), td:nth-child(4) {
    width: 13%;
}
th:nth-child(5), td:nth-child(5) {
    width: 10%;
}
th:nth-child(6), td:nth-child(6) {
    width: 30%;
}
</style>

<table aria-label="使用可能なパラメーター">
  <caption>使用可能なパラメーター</caption>
    <thead>
        <tr>
            <th>パラメーター</th>
            <th>説明</th>
            <th>必須</th>
            <th>デフォルト（未指定の場合）</th>
            <th>型</th>
            <th>例</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>title</code></td>
            <td>画面上部に表示されるタイトルです。</td>
            <td>はい</td>
            <td></td>
            <td>文字列</td>
            <td>Running</td>
        </tr>
        <tr>
            <td><code>icon</code></td>
            <td>使用するアイコンを表す文字列です。</td>
            <td>いいえ</td>
            <td><code>RUNNING_HOME</code></td>
            <td>文字列</td>
            <td>HEART_DETAILS</td>
        </tr>
        <tr>
            <td><code>image</code></td>
            <td>アイテムの画像のURLです。</td>
            <td>はい</td>
            <td></td>
            <td>文字列</td>
            <td><code>https://picsum.photos/400</code></td>
        </tr>
        <tr>
            <td><code>info</code></td>
            <td>ワークアウト開始ボタンの上に表示されるワークアウトに関する情報です。</td>
            <td>はい</td>
            <td></td>
            <td>文字列</td>
            <td>This%20workout%20is%20awesome%21</td>
        </tr>
        <tr>
            <td><code>workout</code></td>
            <td>ワークアウトの名前です。<code>st_completed_class</code>イベントで送信されます。</td>
            <td>はい</td>
            <td></td>
            <td>数値</td>
            <td>5k%20Run</td>
        </tr>
        <tr>
            <td><code>calories</code></td>
            <td>アクティブワークアウト画面に表示されるカロリー数です。<code>st_completed_class</code>イベントで送信されます。</td>
            <td>いいえ</td>
            <td>500〜1,250のランダムな数値</td>
            <td>数値</td>
            <td>600</td>
        </tr>
        <tr>
            <td><code>length</code></td>
            <td>ワークアウトの長さです。<code>st_completed_class</code>イベントで送信されます。</td>
            <td>いいえ</td>
            <td></td>
            <td>数値</td>
            <td>25</td>
        </tr>
        <tr>
            <td><code>workout_info_left_text</code></td>
            <td>アクティブワークアウト画面の左側のカードに使用されるテキストです。</td>
            <td>いいえ</td>
            <td></td>
            <td>文字列</td>
            <td>Road%20Run</td>
        </tr>
        <tr>
            <td><code>workout_info_left_icon</code></td>
            <td>アクティブワークアウト画面の左側のカードに使用されるアイコンです。</td>
            <td>いいえ</td>
            <td></td>
            <td>文字列</td>
            <td>RUNNING_HOME</td>
        </tr>
        <tr>
            <td><code>workout_info_center_text</code></td>
            <td>アクティブワークアウト画面の中央のカードに使用されるテキストです。</td>
            <td>いいえ</td>
            <td></td>
            <td>文字列</td>
            <td>120%20BPM</td>
        </tr>
        <tr>
            <td><code>workout_info_center_icon</code></td>
            <td>アクティブワークアウト画面の中央のカードに使用されるアイコンです。</td>
            <td>いいえ</td>
            <td></td>
            <td>文字列</td>
            <td>HEART_DETAILS</td>
        </tr>
        <tr>
            <td><code>workout_info_right_text</code></td>
            <td>アクティブワークアウト画面の右側のカードに使用されるテキストです。</td>
            <td>いいえ</td>
            <td></td>
            <td>文字列</td>
            <td>25%3A00</td>
        </tr>
        <tr>
            <td><code>workout_info_right_icon</code></td>
            <td>アクティブワークアウト画面の右側のカードに使用されるアイコンです。</td>
            <td>いいえ</td>
            <td></td>
            <td>文字列</td>
            <td>TIMER_DETAILS</td>
        </tr>
    </tbody>
</table>

##### アイコンオプション {#icon-options}

| アイコン | 画像 |
| --- | --- |
| `RUNNING_HOME` | ![ランニングシューズのアイコン。]({% image_buster /assets/img/braze_pilot/running_home_icon.png %}){:style="max-width:30%"} |
| `HEART_DETAILS` | ![ハートのアイコン。]({% image_buster /assets/img/braze_pilot/heart_details_icon.png %}){:style="max-width:30%"} |
| `TIMER_DETAILS` | ![ストップウォッチのアイコン。]({% image_buster /assets/img/braze_pilot/timer_details_icon.png %}){:style="max-width:30%"} |
| `YOGA_HOME` | ![ヨガポーズをとる人のアイコン。]({% image_buster /assets/img/braze_pilot/yoga_home_icon.png %}){:style="max-width:30%"} |
| `BICYCLE_HOME` | ![自転車のアイコン。]({% image_buster /assets/img/braze_pilot/bicycle_home_icon.png %}){:style="max-width:30%"} |
| `DUMBBELL_HOME` | ![ダンベルのアイコン。]({% image_buster /assets/img/braze_pilot/dumbbell_home_icon.png %}){:style="max-width:30%"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="アイコンオプション" }

## PantsLabyrinth
これらは、PilotにおけるPantsLabyrinth架空ブランドアプリのディープリンクです。

### ディープリンクの例 {#pantslabyrinth-example-deep-link}

`braze-pilot://navigation/pantslabyrinth/itemdetails?name=Jeans&price=85&image=https://picsum.photos/400&description=This%20item%20is%20awesome%21&quantity=2&size=Large&colors=%230000FF,%23FF0000&color_strings=White,Blue&selected_color=1`

### パラメーターなしのディープリンク {#pantslabyrinth-deep-links-without-parameters}

| 画面 | ディープリンク |
| --- | --- |
| スプラッシュスクリーン | `braze-pilot://navigation/pantslabyrinth/splash` |
| ウェルカム画面 | `braze-pilot://navigation/pantslabyrinth/welcome` |
| リスト画面 | `braze-pilot://navigation/pantslabyrinth/listing` |
| カートページ | `braze-pilot://navigation/pantslabyrinth/cart` |
| ウィッシュリストページ | `braze-pilot://navigation/pantslabyrinth/wishlist` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="パラメーターなしのディープリンク" }

### パラメーター付きのディープリンク {#pantslabyrinth-deep-links-with-parameters}

| 画面 | ディープリンク |
| --- | --- |
| アイテム詳細ページ | `braze-pilot://navigation/pantslabyrinth/itemdetails` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="パラメーター付きのディープリンク" }

#### 使用可能なパラメーター {#pantslabyrinth-accepted-parameters}

<style>
table td {
    word-break: break-word;
}
th:nth-child(1), td:nth-child(1) {
    width: 20%;
}
th:nth-child(2), td:nth-child(2) {
    width: 30%;
}
th:nth-child(3), td:nth-child(3) {
    width: 8%;
}
th:nth-child(4), td:nth-child(4) {
    width: 13%;
}
th:nth-child(5), td:nth-child(5) {
    width: 10%;
}
th:nth-child(6), td:nth-child(6) {
    width: 30%;
}
</style>

<table aria-label="使用可能なパラメーター">
  <caption>使用可能なパラメーター</caption>
    <thead>
        <tr>
            <th>パラメーター</th>
            <th>説明</th>
            <th>必須</th>
            <th>デフォルト（未指定の場合）</th>
            <th>型</th>
            <th>例</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>name</code></td>
            <td>アイテムの名前です。</td>
            <td>はい</td>
            <td></td>
            <td>文字列</td>
            <td>Jeans</td>
        </tr>
        <tr>
            <td><code>price</code></td>
            <td>アイテムの価格です。</td>
            <td>はい</td>
            <td></td>
            <td>文字列</td>
            <td>85</td>
        </tr>
        <tr>
            <td><code>image</code></td>
            <td>アイテムの画像のURLです。</td>
            <td>はい</td>
            <td></td>
            <td>文字列</td>
            <td><code>https://picsum.photos/400</code></td>
        </tr>
        <tr>
            <td><code>description</code></td>
            <td>アイテムの説明です。</td>
            <td>はい</td>
            <td></td>
            <td>文字列</td>
            <td>This%20item%20is%20awesome%21</td>
        </tr>
        <tr>
            <td><code>quantity</code></td>
            <td>アイテムの数量です。</td>
            <td>いいえ</td>
            <td>1</td>
            <td>数値</td>
            <td>2</td>
        </tr>
        <tr>
            <td><code>size</code></td>
            <td>アイテムのサイズを表す文字列です。</td>
            <td>いいえ</td>
            <td>M</td>
            <td>文字列</td>
            <td>Large</td>
        </tr>
        <tr>
            <td><code>colors</code></td>
            <td>カンマ区切りの16進カラーのリストです。アイテムで使用可能なカラーを表します。</td>
            <td>いいえ</td>
            <td>%23000000</td>
            <td>文字列</td>
            <td>%230000FF,%23FF0000</td>
        </tr>
        <tr>
            <td><code>color_strings</code></td>
            <td>カンマ区切りのカラー名のリストです。テキストでカラーを表します。</td>
            <td>いいえ</td>
            <td>Black</td>
            <td>文字列</td>
            <td>Blue, Red</td>
        </tr>
        <tr>
            <td><code>selected_color</code></td>
            <td>ユーザーが画面に到着したときにカラーセレクターで選択されるカラーのインデックスです。値が指定されていない場合は、最初のカラーが選択されます。</td>
            <td>いいえ</td>
            <td>0</td>
            <td>数値</td>
            <td>1</td>
        </tr>
    </tbody>
</table>

## MovieCanon
これらは、PilotにおけるMovieCanon架空ブランドアプリのディープリンクです。

### ディープリンクの例 {#moviecanon-example-deep-link}

`braze-pilot://navigation/moviecannon/moviedetails?id=1&title=Jaws&thumbnail=https://picsum.photos/400&video=0&description=This%20video%20is%20awesome%21`

### パラメーターなしのディープリンク {#moviecanon-deep-links-without-parameters}

| 画面 | ディープリンク |
| --- | --- |
| スプラッシュスクリーン | `braze-pilot://navigation/moviecannon/splash` |
| ウェルカム画面 | `braze-pilot://navigation/moviecannon/welcome` |
| 映画一覧ページ | `braze-pilot://navigation/moviecannon/moviecannon` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="パラメーターなしのディープリンク" }

### パラメーター付きのディープリンク {#moviecanon-deep-links-with-parameters}

| 画面 | ディープリンク |
| --- | --- |
| 映画詳細ページ | `braze-pilot://navigation/moviecannon/moviedetails` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="パラメーター付きのディープリンク" }

#### 使用可能なパラメーター {#moviecanon-accepted-parameters}

| パラメーター | 説明 | 必須 | 型 | 例 |
| --- | --- | --- | --- | --- |
| `id` | 映画のIDです。 | はい | 数値 | 1 |
| `title` | 映画のタイトルです。 | はい | 文字列 | Jaws |
| `thumbnail` | 映画の再生前に表示されるサムネイルのWeb URLです。 | はい | 文字列 | `https://picsum.photos/400` |
| `video` | 表示する動画リスト内のインデックスです。 | いいえ | 数値 | 0 |
| `description` | 動画の説明です。 | はい | 文字列 | `This%20video%20is%20awesome%21` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="使用可能なパラメーター" }