---
nav_title: データ辞書
article_title: Braze Pilot用データディクショナリ
page_order: 3
page_type: reference
description: "この参考記事では、エンジニアや開発者に必要な統合ステップを簡単に説明します。"
---

# データ辞書 {#data-dictionary}

> Braze Pilot内の各アプリシミュレーションは、アプリ内でのユーザーアクティビティに基づいてさまざまなイベントや属性を収集するよう設計されています。

## データへのアプローチ {#the-approach-to-data}

このアプリは、架空のブランドが代表する業界で典型的なカスタム属性とイベントを記録します。これらの属性を使用して、さまざまな一般的なユースケースのデモを実行できます。
一般的に、すべてのイベントと属性には、そのデータを担当するアプリシミュレーションに対応する短いコードがプレフィックスとして付きます。以下に例を示します。

- Steppingtonアプリシミュレーションで記録されたすべてのデータには、`st_` がプレフィックスとして付きます
- PantsLabyrinthアプリシミュレーションで記録されたすべてのデータには、`pl_` がプレフィックスとして付きます
- MovieCanonアプリシミュレーションで記録されたすべてのデータには、`mc_` がプレフィックスとして付きます

## 記録されたイベントと属性のリスト {#list-of-logged-events-and-attributes}

以下の表は、Braze Pilotによって記録されるイベントと属性の一覧です。

<style>
table td {
    word-break: break-word;
}
th:nth-child(1), td:nth-child(1) {
    width: 32%;
}
th:nth-child(2), td:nth-child(2) {
    width: 15%;
}
th:nth-child(3), td:nth-child(3) {
    width: 10%;
}
th:nth-child(4), td:nth-child(4) {
    width: 20%;
}
th:nth-child(5), td:nth-child(5) {
    width: 28%;
}
</style>

<table aria-label="記録されたイベントと属性のリスト">
  <caption>記録されたイベントと属性のリスト</caption>
    <thead>
        <tr>
            <th>名前</th>
            <th>アプリ</th>
            <th>タイプ</th>
            <th>プロパティ</th>
            <th>記録されるタイミング</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>mc_entered_app</code></td>
            <td>MovieCanon</td>
            <td>イベント</td>
            <td></td>
            <td>ユーザーがMovieCanonアプリに入った時</td>
        </tr>
        <tr>
            <td><code>mc_watched_movie</code></td>
            <td>MovieCanon</td>
            <td>イベント</td>
            <td><code>title: string</code></td>
            <td>ユーザーが動画の視聴を完了した時</td>
        </tr>
        <tr>
            <td><code>mc_viewed_movie_page</code></td>
            <td>MovieCanon</td>
            <td>イベント</td>
            <td><code>title: string</code></td>
            <td>ユーザーが映画ページを閲覧した時</td>
        </tr>
        <tr>
            <td><code>pl_viewed_item</code></td>
            <td>PantsLabyrinth</td>
            <td>イベント</td>
            <td><code>item_name: string</code></td>
            <td>ユーザーが商品ページを閲覧した時</td>
        </tr>
        <tr>
            <td><code>pl_entered_app</code></td>
            <td>PantsLabyrinth</td>
            <td>イベント</td>
            <td></td>
            <td>ユーザーがPantsLabyrinthアプリに入った時</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_wishlist</code></td>
            <td>PantsLabyrinth</td>
            <td>イベント</td>
            <td><code>item_name: string</code></td>
            <td>ユーザーがウィッシュリストにアイテムを追加した時</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_cart</code></td>
            <td>PantsLabyrinth</td>
            <td>イベント</td>
            <td><code>item_name: string</code></td>
            <td>ユーザーがカートにアイテムを追加した時</td>
        </tr>
        <tr>
            <td><code>&lt;purchase_event&gt;</code></td>
            <td>PantsLabyrinth</td>
            <td>イベント</td>
            <td><code>name: string</code><br><code>price: number</code></td>
            <td>ユーザーが購入を完了した時</td>
        </tr>
        <tr>
            <td><code>st_entered_app</code></td>
            <td>Steppington</td>
            <td>イベント</td>
            <td></td>
            <td>ユーザーがSteppingtonアプリに入った時</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>Steppington</td>
            <td>イベント</td>
            <td><code>class_type: string</code><br><code>calories_burned: number</code><br><code>workout_length: number</code></td>
            <td>ユーザーがワークアウトを完了した時</td>
        </tr>
        <tr>
            <td><code>st_viewed_premium_benefit</code></td>
            <td>Steppington</td>
            <td>イベント</td>
            <td><code>benefit_type: string</code></td>
            <td>ユーザーがSteppington+タブにアクセスした時（フィーチャーフラグで有効化されている場合）</td>
        </tr>
        <tr>
            <td><code>st_viewed_class</code></td>
            <td>Steppington</td>
            <td>イベント</td>
            <td><code>class_type: string</code></td>
            <td>ユーザーがワークアウトページにアクセスした時</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>Steppington</td>
            <td>イベント</td>
            <td><code>class_type: string</code><br><code>calories_burned: number</code><br><code>workout_length: number</code></td>
            <td>ユーザーがワークアウトを完了した時</td>
        </tr>
        <tr>
            <td><code>st_most_recent_completed_class</code></td>
            <td>Steppington</td>
            <td>属性</td>
            <td><code>string</code></td>
            <td>ユーザーがワークアウトを完了した時</td>
        </tr>
        <tr>
            <td><code>st_favorited_class</code></td>
            <td>Steppington</td>
            <td>イベント</td>
            <td><code>class_type: string</code></td>
            <td>ユーザーがクラスをお気に入りに追加した時</td>
        </tr>
        <tr>
            <td><code>st_unfavorited_class</code></td>
            <td>Steppington</td>
            <td>イベント</td>
            <td><code>class_type: string</code></td>
            <td>ユーザーがクラスのお気に入り登録を解除した時</td>
        </tr>
        <tr>
            <td><code>st_started_free_trial</code></td>
            <td>Steppington</td>
            <td>イベント</td>
            <td></td>
            <td>ユーザーが<strong>Start Free Trial</strong>ボタンを選択した時</td>
        </tr>
        <tr>
            <td><code>st_set_goal</code></td>
            <td>Steppington</td>
            <td>イベント</td>
            <td><code>goal_name: string</code><br><code>goal: number</code><br><code>units: string</code></td>
            <td>ユーザーが<strong>Start Free Trial</strong>ボタンを選択した時</td>
        </tr>
    </tbody>
</table>