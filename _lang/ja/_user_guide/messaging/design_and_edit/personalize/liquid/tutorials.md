---
nav_title: チュートリアル
article_title: "チュートリアル: Liquid コードの書き方"
page_order: 11
description: "このリファレンスページには、Liquid コードを始めるための初心者向けチュートリアルが含まれています。"
page_type: tutorial
---

# チュートリアル: Liquid コードの書き方 {#tutorials-writing-liquid-code}

> Liquid は初めてですか？これらのチュートリアルは、初心者向けのユースケースで Liquid コードの書き方を学ぶのに役立ちます。各チュートリアルでは、条件ロジックや演算子など、さまざまな学習目標の組み合わせを扱います。

これらのチュートリアルを完了すると、以下のことができるようになります。

- 一般的なユースケース向けの Liquid コードを書く
- Liquid の条件ロジックを組み合わせて、ユーザーデータに基づいてメッセージをパーソナライズする
- 変数とフィルターを使用して、属性の値を利用した数式を書く
- Liquid コードの基本的なコマンドを認識し、コードが何をしているかを大まかに理解する

| チュートリアル | 学習目標 |
| --- | --- |
| [ユーザーセグメント向けにメッセージをパーソナライズする](#segments) | デフォルト値、条件ロジック |
| [放棄カートのリマインダー](#reminders) | 演算子、条件ロジック |
| [イベントカウントダウン](#countdown) | 変数、日付フィルター |
| [月間誕生日メッセージ](#birthday) | 変数、日付フィルター、演算子 |
| [お気に入り製品のプロモーション](#favorite-product) | 変数、日付フィルター、数式、演算子 |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Tutorials: Writing Liquid code" }

## ユーザーセグメント向けのパーソナライズメッセージ {#segments}

VIP 顧客や新規サブスクライバーなど、さまざまなユーザーセグメント向けにメッセージをカスタマイズしましょう。

1. ユーザーの名がある場合とない場合に送信するパーソナライズされた挨拶を含むメッセージを開きます。これを行うには、属性 `first_name` と、`first_name` が空白の場合に使用するデフォルト値を含む Liquid タグを作成します。このシナリオでは、デフォルト値として「traveler」を使用しましょう。

{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
```
{% endraw %}

{: start="2"}
2. 次に、ユーザーが VIP 顧客の場合に送信するメッセージを設定しましょう。これには条件ロジックタグ `if` を使用する必要があります。このタグは、カスタム属性 `vip_status` が `VIP` に等しい場合、以下の Liquid が実行されることを示します。この場合、特定のメッセージが送信されます。

{% raw %}
`````````liquid
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
```
{% endraw %}

{: start="3"}
3. 新規サブスクライバーのユーザー向けにカスタマイズされたメッセージを送信しましょう。条件ロジックタグ `elsif` を使用して、ユーザーの `vip_status` が `new` の場合、以下のメッセージが送信されるように指定します。

{% raw %}
`````````liquid
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
```
{% endraw %}

{: start="4"}
4. VIP でも新規でもないユーザーはどうでしょうか？`else` タグを使用して、前の条件が満たされない場合に以下のメッセージを送信するように指定できます。そして、考慮すべき VIP ステータスがこれ以上ないため、`endif` タグで条件ロジックを閉じます。

{% raw %}
`````````liquid
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}

{% details 完全な Liquid コード %}
{% raw %}
`````````liquid
Happy summer, {{${first_name} | default: "traveler"}}!
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}
{% enddetails %}

## 放棄カートのリマインダー {#reminders}

カートに残っているアイテムをユーザーに思い出させるパーソナライズメッセージを送信しましょう。カート内のアイテム数に基づいてさらにカスタマイズし、3つ以下の場合はすべてのアイテムをリストアップし、3つを超える場合はより簡潔なメッセージを送信します。

1. まず、「等しくない」を意味する演算子 `!=` を使用して Liquid の条件ロジックを開き、ユーザーのカートが空かどうかを確認しましょう。この場合、カスタム属性 `cart_items` が空白の値に等しくないという条件を設定します。

{% raw %}
`````````liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
```
{% endraw %}

{: start="2"}
2. 次に、「より大きい」を意味する演算子 `>` を使用して、カートに3つを超えるアイテムがあるかどうかを確認する必要があります。

{% raw %}
`````````liquid
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
```
{% endraw %}

{: start="3"}
3. ユーザーの名で挨拶するメッセージを書きます。名が利用できない場合は、デフォルト値として「there」を使用します。カートに3つを超えるアイテムがある場合に表示する内容を含めます。ユーザーに完全なリストで圧倒したくないので、最初の3つの `cart_items` をリストアップしましょう。

{% raw %}
`````````liquid
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
```
{% endraw %}

{: start="4"}
4. `else` タグを使用して、前の条件が満たされない場合（つまり、`cart_items` が空白または3つ未満の場合）に何が起こるかを指定し、送信するメッセージを提供します。3つのアイテムはそれほどスペースを取らないので、すべてリストアップできます。Liquid 演算子 `join` と `,` を使用して、アイテムがカンマで区切られてリストアップされるように指定します。`endif` でロジックを閉じます。

{% raw %}
`````````liquid
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you.
{% endif %}
```
{% endraw %}

{: start="5"}
5. `else` を使用し、次に `abort_message` を使用して、カートが前の条件のいずれも満たさない場合（つまり、カートが空の場合）にメッセージを送信しないように Liquid コードに指示します。`endif` でロジックを閉じます。

{% raw %}
`````````liquid
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}

{% details 完全な Liquid コード %}
{% raw %}
`````````liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you.
{% endif %}
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}
{% enddetails %}

## イベントカウントダウン {#countdown}

アニバーサリーセールまでの残り日数をユーザーに伝えるメッセージを送信しましょう。これを行うために、変数を使用して属性の値を操作する数式を作成します。

1. まず、変数 `sale_date` をカスタム属性 `anniversary_date` に割り当て、`date: "s"` フィルターを適用しましょう。これにより、`anniversary_date` が秒単位で表されるタイムスタンプ形式に変換され、その値が `sale_date` に割り当てられます。

{% raw %}
`````````liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
```
{% endraw %}

{: start="2"}
2. 今日のタイムスタンプをキャプチャする変数も割り当てる必要があります。変数 `today` を `now`（現在の日時）に割り当て、`date: "%s"` フィルターを適用しましょう。

{% raw %}
`````````liquid
{% assign today =  'now' | date: "%s"  %}
```
{% endraw %}

{: start="3"}
3. 次に、現在（`today`）とアニバーサリーセール（`sale_date`）の間の秒数を計算しましょう。これを行うには、変数 `difference` を `sale_date` から `today` を引いた値に割り当てます。

{% raw %}
`````````liquid
{% assign difference =  event_date | minus: today %}
```
{% endraw %}

{: start="4"}
4. 次に、`difference` をメッセージで参照できる値に変換する必要があります。セールまでの秒数をユーザーに伝えるのは理想的ではないためです。`difference_days` を `event_date` に割り当て、`86400` で割って日数を取得しましょう。

{% raw %}
`````````liquid
{% assign difference_days = difference | divided_by: 86400 %}
```
{% endraw %}

{: start="5"}
5. 最後に、送信するメッセージを作成しましょう。

{% raw %}
`````````liquid
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}

{% details 完全な Liquid コード %}
{% raw %}
`````````liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
{% assign today =  'now' | date: "%s"  %}
{% assign difference =  event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}
{% enddetails %}

## 月間誕生日メッセージ {#birthday}

今月が誕生月であるすべてのユーザーに特別なプロモーションを送信しましょう。今月が誕生月でないユーザーにはメッセージは送信されません。

1. まず、今月を取得しましょう。変数 `this_month` を `now`（現在の日時）に割り当て、`date: "%B"` フィルターを使用して変数が月に等しくなるように指定します。

{% raw %}
`````````liquid
{% assign this_month = 'now' | date: "%B" %}
```
{% endraw %}

{: start="2"}
2. 次に、ユーザーの `date_of_birth` から誕生月を取得しましょう。変数 `birth_month` を `date_of_birth` に割り当て、`date: "%B"` フィルターを使用します。

{% raw %}
`````````liquid
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
```
{% endraw %}

{: start="3"}
3. 月を値として持つ2つの変数ができたので、条件ロジックで比較できます。`this_month` がユーザーの `birth_month` に等しいという条件を設定しましょう。

{% raw %}
`````````liquid
{% if {{this_month}} == {{birth_month}} %}
```
{% endraw %}

{: start="4"}
4. 今月がユーザーの誕生月でもある場合に送信するメッセージを作成しましょう。

{% raw %}
`````````liquid
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
```
{% endraw %}

{: start="5"}
5. `else` タグを使用して、条件が満たされない場合（今月がユーザーの誕生月ではない場合）に何が起こるかを指定します。

{% raw %}
`````````liquid
{% else %}
```
{% endraw %}

{: start="6"}
6. ユーザーの誕生月が今月でない場合はメッセージを送信したくないので、`abort_message` を使用してメッセージをキャンセルし、`endif` で条件ロジックを閉じます。

{% raw %}
`````````liquid
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}

{% details 完全な Liquid コード %}
{% raw %}
`````````liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
{% if {{this_month}} == {{birth_month}} %}
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
{% else %}
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}
{% enddetails %}

## お気に入り製品のプロモーション {#favorite-product}

ユーザーの最終購入日が6か月以上前の場合に、お気に入り製品をプロモーションしましょう。

1. まず、条件ロジックを使用して、ユーザーのお気に入り製品と最終購入日があるかどうかを確認します。

{% raw %}
`````````liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
```
{% endraw %}

{: start="2"}
2. 次に、ユーザーのお気に入り製品または最終購入日がない場合、メッセージを送信しないように指定します。

{% raw %}
`````````liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="3"}
3. `else` を使用して、上記の条件が満たされない場合（ユーザーのお気に入り製品と最終購入日が*ある*場合）に何が起こるかを指定します。

{% raw %}
`````````liquid
{% else %}
```
{% endraw %}

{: start="4"}
4. 購入日がある場合、今日の日付と比較できるように変数に割り当てる必要があります。まず、変数 `today` を `now`（現在の日時）に割り当て、`date: "%s"` フィルターを使用して値を秒単位で表されるタイムスタンプ形式に変換して、今日の日付の値を作成しましょう。`plus: 0` フィルターを追加して、タイムスタンプに「0」を加えます。これはタイムスタンプの値を変更しませんが、将来の数式でタイムスタンプを使用する際に役立ちます。


{% raw %}
`````````liquid
{% assign today = 'now' | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="5"}
5. 次に、変数 `last_purchase_date` をカスタム属性 `last_purchase_date` に割り当て、`date: "s"` フィルターを使用して、最終購入日を秒単位でキャプチャしましょう。再び `plus: 0` フィルターを追加します。

{% raw %}
`````````liquid
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="6"}
6. 最終購入日と今日の日付が秒単位であるため、6か月が何秒かを計算する必要があります。数式（約6か月 × 30.44日 × 24時間 × 60分 × 60秒）を作成し、変数 `six_months` に割り当てましょう。`times` を使用して時間単位の乗算を指定します。

{% raw %}
`````````liquid
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
```
{% endraw %}

{: start="7"}
7. すべての時間値が秒単位になったので、数式でそれらの値を使用できます。`today_minus_last_purchase_date` という変数を割り当て、今日の値から `last_purchase_date` を引きます。これにより、最終購入からの経過秒数が得られます。

{% raw %}
`````````liquid
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
```
{% endraw %}

{: start="8"}
8. 次に、条件ロジックで時間値を直接比較しましょう。`today_minus_last_purchase_date` が6か月以上（`>=`）であるという条件を定義します。つまり、最終購入日が少なくとも6か月前であるということです。

{% raw %}
`````````liquid
{% if today_minus_last_purchase_date >= six_months %}
```
{% endraw %}

{: start="9"}
9. 最終購入が少なくとも6か月前の場合に送信するメッセージを作成しましょう。

{% raw %}
`````````liquid
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
```
{% endraw %}

{: start="10"}
10. `else` タグを使用して、条件が満たされない場合（購入が6か月以上前ではない場合）に何が起こるかを指定します。

{% raw %}
`````````liquid
{% else %}
```
{% endraw %}

{: start="11"}
11. `abort_message` を含めてメッセージをキャンセルします。

{% raw %}
`````````liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="12"}
12. 最後に、2つの `endif` タグで Liquid を終了します。最初の `endif` はお気に入り製品または最終購入日の条件チェックを閉じ、2番目の `endif` は最終購入日が少なくとも6か月前であるかの条件チェックを閉じます。

{% raw %}
`````````liquid
{% endif %}
{% endif %}
```
{% endraw %}

{% details 完全な Liquid コード %}
{% raw %}
`````````liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
{% abort_message("No favorite product or last purchase date") %}
{% else %}
{% assign today = 'now' | date: "%s" | plus: 0 %}
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
{% if today_minus_last_purchase_date >= six_months %}
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
{% else %}
{% abort_message("Last purchase was less than six months ago") %}
{% endif %}
{% endif %}
```
{% endraw %}
{% enddetails %}