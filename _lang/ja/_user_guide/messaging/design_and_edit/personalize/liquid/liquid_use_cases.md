---
nav_title: Liquidユースケースライブラリ
article_title: Liquidユースケースライブラリ
page_order: 10
search_rank: 2
excerpt_separator: ""
page_type: glossary
layout: liquid_use_case_glossary
description: "このランディングページには、記念日、アプリの使用状況、カウントダウンなど、カテゴリ別に整理されたLiquidのユースケースサンプルが掲載されています。"

---

{% api %}

## 記念日と祝日 {#anniversaries-and-holidays}

{% apitags %}
Anniversaries and holidays
{% endapitags %}

- [ユーザーの記念年に基づいてメッセージをパーソナライズする](#anniversary-year)
- [ユーザーの誕生日週に基づいてメッセージをパーソナライズする](#birthday-week)
- [誕生月のユーザーにCampaignを送信する](#birthday-month)
- [主要な祝日にメッセージを送信しないようにする](#holiday-avoid)

### ユーザーの記念年に基づいてメッセージをパーソナライズする {#anniversary-year}

このユースケースでは、ユーザーの初回サインアップ日に基づいてアプリの記念日を計算し、何年目のお祝いかに応じて異なるメッセージを表示する方法を示します。

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign this_day = 'now' | date: "%d" %}
{% assign anniversary_month = {{custom_attribute.${registration_date}}} | date: "%B" %}
{% assign anniversary_day = {{custom_attribute.${registration_date}}} | date: "%d" %}
{% assign anniversary_year = {{custom_attribute.${registration_date}}} | date: "%Y" %}

{% if this_month == anniversary_month %}
{% if this_day == anniversary_day %}
{% if anniversary_year == '2021' %}
Exactly one year ago today we met for the first time!

{% elsif anniversary_year == '2020' %}
Exactly two years ago today we met for the first time!

{% elsif anniversary_year == '2019' %}
Exactly three years ago today we met for the first time!

{% else %}
{% abort_message("Not same year") %}
{% endif %}

{% else %}
{% abort_message("Not same day") %}
{% endif %}

{% else %}
{% abort_message("Not same month") %}
{% endif %}
```
{% endraw %}

**説明:** ここでは、予約変数`now`を使用して、現在の日時を[ISO 8601](http://en.wikipedia.org/wiki/ISO_8601)形式でテンプレートに挿入しています。フィルター`%B`（「May」のような月名）と`%d`（「18」のような日）で現在の月と日をフォーマットします。次に、`signup_date`の値にも同じ日時フィルターを使用して、条件タグとロジックで2つの値を比較できるようにします。

さらに3つの変数ステートメントを繰り返して、`signup_date`の`%B`と`%d`を取得し、`%Y`（「2021」のような年）も追加します。これにより、`signup_date`の日時が年だけに変換されます。日と月がわかればユーザーの記念日が今日かどうかを確認でき、年がわかれば何年経ったかがわかるため、何年目のお祝いかを伝えることができます。

{% alert tip %} サインアップ日を収集してきた年数分の条件を作成できます。{% endalert %}

### ユーザーの誕生日週に基づいてメッセージをパーソナライズする {#birthday-week}

このユースケースでは、ユーザーの誕生日を見つけて現在の日付と比較し、誕生日週の前、最中、後に特別な誕生日メッセージを表示する方法を示します。

{% raw %}
```liquid
{% assign this_week = 'now' | date: '%W' %}
{% assign birthday_week = {{${date_of_birth}}} | date: '%W' %}
{% assign last_week = {{this_week}} | minus: 1 %}
{% assign next_week = {{this_week}} | plus: 1 %}
{% assign birthday_week_conversion = {{birthday_week}} | plus: 0 %}
{% if {{last_week}} == {{birthday_week_conversion}} %}
Happy birthday for last week!
{% elsif {{birthday_week}} == {{this_week}} %}
Happy birthday for this week!
{% elsif {{next_week}} == {{birthday_week_conversion}} %}
Happy birthday for next week!
{% else %}
No birthday for you!
{% endif %}
```
{% endraw %}

**説明:** [記念年](#anniversary-year)のユースケースと同様に、ここでは予約変数`now`を取得し、`%W`フィルター（年間52週のうちの第12週のような週番号）を使用して、ユーザーの誕生日が該当する年間の週番号を取得します。ユーザーの誕生日週が現在の週と一致する場合、お祝いメッセージを送信します。

`last_week`と`next_week`のステートメントも含めて、メッセージングをさらにパーソナライズしています。

### 誕生月のユーザーにCampaignを送信する {#birthday-month}

このユースケースでは、ユーザーの誕生月を計算し、誕生日が今月かどうかを確認し、該当する場合は特別なメッセージを送信する方法を示します。

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
{% if {{this_month}} == {{birth_month}} %}
Message body
{% else %}
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}

**説明:** [誕生日週](#birthday-week)のユースケースと同様ですが、ここでは`%B`フィルター（「May」のような月名）を使用して、今月が誕生日のユーザーを計算します。月次メールで誕生日のユーザーに呼びかけるなどの活用が考えられます。

### 主要な祝日にメッセージを送信しないようにする {#holiday-avoid}

このユースケースでは、ホリデーシーズン中にメッセージを送信しつつ、エンゲージメントが低くなりがちな主要な祝日の当日は送信を避ける方法を示します。

{% raw %}
```liquid
{% assign today = 'now' | date: '%Y-%m-%d' %}
{% if today == "2023-12-24" or today == "2023-12-25" or today == "2023-12-26" %}
{% abort_message %}
{% else %}
Message if today isn't one of the provided holidays.
{% endif %}
```
{% endraw %}

**説明:** ここでは、`today`という用語を予約変数`now`（現在の日時）に割り当て、フィルター`%Y`（「2023」のような年）、`%m`（「12」のような月）、`%d`（「25」のような日）を使用して日付をフォーマットします。次に条件文を実行し、変数`today`が指定した祝日と一致する場合、メッセージを中止します。

この例では、クリスマスイブ、クリスマス、ボクシングデー（クリスマスの翌日）を使用しています。

{% endapi %}

{% api %}

## アプリの使用状況 {#app-usage}

{% apitags %}
App usage
{% endapitags %}

- [セッションを記録していないユーザーにその言語でメッセージを送信する](#app-session-language)
- [ユーザーが最後にアプリを開いた時期に基づいてメッセージをパーソナライズする](#app-last-opened)
- [ユーザーが3日以内にアプリを使用した場合に異なるメッセージを表示する](#app-last-opened-less-than)

### セッションを記録していないユーザーにその言語でメッセージを送信する {#app-session-language}

このユースケースでは、ユーザーがセッションを記録したかどうかを確認し、記録していない場合は、カスタム属性で手動収集した言語に基づいてメッセージを表示するロジックを含めます。アカウントに言語情報が紐づいていない場合は、デフォルト言語でメッセージを表示します。ユーザーがセッションを記録している場合は、ユーザーに紐づいた言語情報を取得し、適切なメッセージを表示します。

{% raw %}
```liquid
{% if {{${last_used_app_date}}} == nil %}
{% if {{custom_attribute.${user_language}}} == 'en' %}
Message in English based on custom attribute
{% elsif {{custom_attribute.${user_language}}} == 'fr' %}
Message in French based on custom attribute
{% else %}
Does not have language - Default language
{% endif %}
{% else %}
{% if ${language} == 'en' %}
Message in English based on Language
{% elsif ${language} == 'fr' %}
Message in French based on Language
{% else %}
Has language - Default language
{% endif %}
{% endif %}
```
{% endraw %}

{% raw %}
**説明:** ここでは、ネストされた2つのグループ化された`if`ステートメントを使用しています。最初の`if`ステートメントは、`last_used_app_date`が`nil`かどうかを確認して、ユーザーがセッションを開始したかどうかをチェックします。これは、`{{${language}}}`がユーザーのセッション記録時にSDKによって自動収集されるためです。ユーザーがセッションを記録していない場合、まだ言語情報がないため、言語関連のカスタム属性が保存されているかどうかを確認し、その情報に基づいて可能であればその言語でメッセージを表示します。
{% endraw %}

2番目の`if`ステートメントは、標準（デフォルト）属性を確認するだけです。ユーザーの`last_used_app_date`が`nil`ではないため、セッションを記録済みであり、言語情報を取得できているからです。

{% alert note %}
[`Nil`](https://shopify.github.io/liquid/basics/types/#nil)は、Liquidコードが結果を返さない場合に返される予約変数です。`Nil`は`if`ブロック内で`false`として扱われます。
{% endalert %}

### ユーザーが最後にアプリを開いた時期に基づいてメッセージをパーソナライズする {#app-last-opened}

このユースケースでは、ユーザーが最後にアプリを開いた時刻を計算し、経過時間に応じて異なるパーソナライズされたメッセージを表示します。

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Happy to see you again!
{% else %}
It's been a while; here are some of our latest updates.
{% endif %}
```
{% endraw %}

### ユーザーが3日以内にアプリを使用した場合に異なるメッセージを表示する {#app-last-opened-less-than}

このユースケースでは、ユーザーがどのくらい前にアプリを使用したかを計算し、経過時間に応じて異なるパーソナライズされたメッセージを表示します。

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Message for a recently active user
{% else %}
Message for a less active user
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## カウントダウン {#countdowns}

{% apitags %}
Countdowns
{% endapitags %}

- [今日の日付にX日を加算する](#countdown-add-x-days)
- [設定した時点からのカウントダウンを計算する](#countdown-difference-days)
- [特定の配送日と優先度のカウントダウンを作成する](#countdown-shipping-options)
- [日数でカウントダウンを作成する](#countdown-days)
- [日から時間、分へのカウントダウンを作成する](#countdown-dynamic)
- [特定の日付までの残り日数を表示する](#countdown-future-date)
- [カスタム日付属性の到来までの残り日数を表示する](#countdown-custom-date-attribute)
- [残り時間を表示し、残りX時間の場合はメッセージを中止する](#countdown-abort-window)
- [ユーザーのメンバーシップ終了のX日前にアプリ内メッセージを送信する](#countdown-membership-expiry)
- [ユーザーの日付と言語に基づいてアプリ内メッセージをパーソナライズする](#countdown-personalize-language)
- [30日後の日付を月と日のフォーマットでテンプレートに挿入する](#countdown-template-date)

### 今日の日付にX日を加算する {#countdown-add-x-days}

このユースケースでは、現在の日付に特定の日数を加算して、メッセージ内で参照・追加します。たとえば、週末のエリアイベントを紹介する週中のメッセージを送信したい場合に使用できます。

{% raw %}
```liquid
Here are the movies we're showing on {{ "now" | date:'%s' | plus:259200 | date:"%F" }}!
```
{% endraw %}

`plus`の値は常に秒単位なので、最後にフィルター`%F`を使用して秒を日付に変換します。

{% alert important %}
メッセージにイベントリストへのURLやディープリンクを含めて、将来のアクションのリストにユーザーを誘導することをお勧めします。
{% endalert %}

### 設定した時点からのカウントダウンを計算する {#countdown-difference-days}

このユースケースでは、特定の日付と現在の日付の差を日数で計算します。この差を使用して、ユーザーにカウントダウンを表示できます。

{% raw %}
```liquid
{% assign event_date = '2023-12-31' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
you have {{ difference_days }} days left!
```
{% endraw %}

### 特定の配送日と優先度のカウントダウンを作成する {#countdown-shipping-options}

このユースケースでは、さまざまな配送オプションを取得し、受け取りまでの所要時間を計算し、特定の日付までに荷物を受け取れるよう購入を促すメッセージを表示します。

{% raw %}
```liquid
{% assign standard_shipping_start = "2023-12-10T00:00-05:00" | date: "%s" %}
{% assign standard_shipping_end = "2023-12-20T13:00-05:00" | date: "%s" %}
{% assign express_shipping_end = "2023-12-22T24:00-05:00" | date: "%s" %}
{% assign overnight_shipping_end = "2023-12-23T24:00-05:00" | date: "%s" %}
{% assign today = 'now' | date: "%s" %}

{% assign difference_s = standard_shipping_end | minus: today %}
{% assign difference_s_days = difference_s | divided_by: 86400.00 | round %}
{% assign difference_e = express_shipping_end | minus: today %}
{% assign difference_e_days = difference_e | divided_by: 86400.00 | round %}
{% assign difference_o = overnight_shipping_end | minus: today %}
{% assign difference_o_days = difference_o | divided_by: 86400.00 | round %}

{% if today >= standard_shipping_start and today <= standard_shipping_end %}
{% if difference_s_days == 0 %}
This is the last day to order with standard shipping, so your order gets here on time for Christmas Eve!
{% elsif difference_s_days == 1 %}
There is {{difference_s_days}} day left to order with standard shipping, so your order gets here on time for Christmas Eve!

{% else %}
There are {{difference_s_days}} days left to order with standard shipping so your order gets here on time for Christmas Eve!
{% endif %}
{% elsif today > standard_shipping_end and today < express_shipping_end %}
{% if difference_e_days == 1 %}
There is {{difference_e_days}} day left to order with express shipping, so your order gets here on time for Christmas Eve!
{% else %}
There are {{difference_e_days}} days left to order with express shipping so your order gets here on time for Christmas Eve!
{% endif %}
{% elsif today >= express_shipping_end and today < overnight_shipping_end %}
This is the last day for overnight shipping so your order gets here on time for Christmas Eve!
{% else %}
{% abort_message("Unable to order and ship in time") %}
{% endif %}
```
{% endraw %}

### 日数でカウントダウンを作成する {#countdown-days}

このユースケースでは、特定のイベントと現在の日付の間の残り時間を計算し、イベントまでの残り日数を表示します。

{% raw %}
```liquid
{% assign event_date = {{custom_attribute.${last_selected_event_date}}} | date: "%s" %}
{% assign today =  'now' | date: "%s"  %}
{% assign difference =  event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Your order will arrive in {{ difference_days }} days!
```
{% endraw %}

{% alert important %}
`date`値を持つカスタム属性フィールドが必要です。
{% endalert %}

### 日から時間、分へのカウントダウンを作成する {#countdown-dynamic}

このユースケースでは、特定のイベントと現在の日付の間の残り時間を計算します。イベントまでの残り時間に応じて、時間の値（日、時間、分）を変更し、異なるパーソナライズされたメッセージを表示します。

たとえば、顧客の注文到着まで2日ある場合は「ご注文は2日後に届きます」と表示し、1日未満の場合は「ご注文は17時間後に届きます」と変更できます。

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign scheme_finish = "2017-10-13T10:30:30" | date: "%s" %}
{% assign difference_seconds =  scheme_finish | minus: today %}
{% assign difference_minutes = difference_seconds | divided_by: 60 %}
{% assign difference_hours = difference_seconds | divided_by: 3600 %}
{% assign difference_days = difference_seconds | divided_by: 86400 %}
{% if {{difference_minutes}} > 59 and {{difference_minutes}} < 1440 %}
You have {{difference_hours}} hours left till your order arrives!
{% elsif {{difference_minutes}} < 59 %}
You have {{difference_minutes}} minutes left till your order arrives!
{% else %}
You have {{difference_days}} days left till your order arrives!
{% endif %}
```
{% endraw %}

{% alert important %}
`date`値を持つカスタム属性フィールドが必要です。また、日、時間、分で時間を表示する際のしきい値を設定する必要があります。
{% endalert %}

### 特定の日付までの残り日数を表示する {#countdown-future-date}

このユースケースでは、現在の日付と将来のイベント日の差を計算し、イベントまでの残り日数を示すメッセージを表示します。

{% raw %}
```liquid
{% assign event_date = '2024-01-15' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
There are {{difference_days}} days until your birthday!
```
{% endraw %}

### カスタム日付属性の到来までの残り日数を表示する {#countdown-custom-date-attribute}

このユースケースでは、現在の日付と将来の日付の差を日数で計算し、差が設定した数値と一致する場合にメッセージを表示します。

この例では、カスタム日付属性の2日前にユーザーにメッセージが届きます。それ以外の場合、メッセージは送信されません。

{% raw %}
```liquid
{% assign today = 'now' | date: '%j' | plus: 0 %}
{% assign surgery_date = {{custom_attribute.${surgery_date}}} | date: '%j' | plus: 0 %}

{% assign difference_days = {{surgery_date}} | minus: {{today}} %}
{% if difference_days == 2 %}
Your surgery is in 2 days on {{custom_attribute.${surgery_date}}}
{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### 残り時間を表示し、残りX時間の場合はメッセージを中止する {#countdown-abort-window}

このユースケースでは、特定の日付までの残り時間を計算し、その長さに応じて（日付が近すぎる場合はメッセージをスキップして）異なるパーソナライズされたメッセージを表示します。

たとえば、「ロンドン行きのチケット購入まであとX時間です」と表示しますが、ロンドン行きのフライト時刻まで2時間以内の場合はメッセージを送信しません。

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign dep_time = {{event_properties.${outboundDate}}} | date: "%s" %}
{% assign time_to_dep = dep_time | minus: today %}
{% if {{time_to_dep}} < 7200 %}
{% abort_message("OutboundDate less than 2 hours") %}
{% elsif {{time_to_dep}} > 7200 and {{time_to_dep}} < 86400 %}
Don't forget to buy your ticket to {{event_properties.${toStation}}} within next 24 hours!
{% else %}
Still traveling to {{event_properties.${toStation}}} in more than 24 hours? Book now!
{% endif %}
```
{% endraw %}

{% alert important %} カスタムイベントプロパティが必要です。{% endalert %}

### ユーザーのメンバーシップ終了のX日前にアプリ内メッセージを送信する {#countdown-membership-expiry}

このユースケースでは、メンバーシップの有効期限を取得し、期限切れまでの残り時間を計算し、メンバーシップの残り期間に応じて異なるメッセージを表示します。

{% raw %}
```liquid
{% assign membership_expiry = {{custom_attribute.${membership_expiry_date}}} | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = membership_expiry | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}

{% if difference_days > 4 and difference_days <= 7 %}
You have {{difference_days}} days left in your trial, make sure you upgrade!

{% elsif difference_days > 2 and difference_days <= 4 %}
HURRY! You have {{difference_days}} days left in your trial, make sure you upgrade!

{% elsif difference_days == 2 %}
LAST CHANCE! You have {{difference_days}} days left in your trial. Make sure you upgrade!

{% else %}
You have few days left in your trial. Make sure to upgrade!
{% endif %}
```
{% endraw %}

### ユーザーの日付と言語に基づいてアプリ内メッセージをパーソナライズする {#countdown-personalize-language}

このユースケースでは、イベントまでのカウントダウンを計算し、ユーザーの言語設定に基づいてその言語でカウントダウンを表示します。

たとえば、月に1回ユーザーにアップセルメッセージを送信して、オファーの有効期間を知らせる場合、4つのアプリ内メッセージを使用できます。

- 初回
- 残り2日
- 残り1日
- 最終日

{% raw %}
```liquid
{% assign today = 'now' | date: "%s" %}
{% assign end_date = "2021-04-16T23:59:59" | date: "%s" %}
{% assign difference = end_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
{% if {{difference_days}} >= 3 %}
{% if ${language} == 'de' %}

Hallo, das Angebot gilt bis zum 16.04.

{% elsif ${language} == 'ch' %}
Grüezi, das Angebot gilt bis zum 16.04.

{% elsif ${language} == 'en' %}
The offer is valid until 16.04.

{% else %}
The offer is valid until 16.04.

{% endif %}
{% elsif {{difference_days}} == 2 %}
{% if ${language} == 'de' %}
INSERT MESSAGE

{% elsif ${language} == 'ch' %}
INSERT MESSAGE

{% elsif ${language} == 'en' %}
INSERT MESSAGE

{% else %}
INSERT MESSAGE
{% endif %}

{% elsif {{difference_days}} == 1 %}
{% if ${language} == 'de' %}
INSERT MESSAGE

{% elsif ${language} == 'ch' %}
INSERT MESSAGE

{% elsif ${language} == 'en' %}
INSERT MESSAGE

{% else %}
INSERT MESSAGE
{% endif %}

{% elsif {{difference_days}} == 0 %}
{% if ${language} == 'de' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'ch' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'en' %}
Grüezi, das Angebot gilt noch heute.

{% else %}
Hi, the offer is only valid today.
{% endif %}

{% else %}
{% abort_message("Calculation failed") %}
{% endif %}
```
{% endraw %}

{% alert important %}
`date`値を割り当て、指定した日付が日付範囲外の場合の中止ロジックを含める必要があります。正確な日の計算には、割り当てる終了日に23:59:59を含める必要があります。
{% endalert %}

### 30日後の日付を月と日のフォーマットでテンプレートに挿入する {#countdown-template-date}

このユースケースでは、メッセージングで使用するために30日後の日付を表示します。

{% raw %}
```liquid
{% assign today = 'now' | date: "%s" %}
{% assign thirty_days = today | plus: 2592000 | date: "%B %d" %}
```
{% endraw %}

{% endapi %}

{% api %}

## カスタム属性 {#custom-attribute}

{% apitags %}
Custom attribute
{% endapitags %}

- [一致するカスタム属性に基づいてメッセージをパーソナライズする](#attribute-matching)
- [ヨーロッパの数値表記規則に合わせて通貨をフォーマットする](#european-currency-format)
- [2つのカスタム属性を減算して差額を金額として表示する](#attribute-monetary-difference)
- [フルネームがfirst_nameフィールドに保存されている場合にユーザーの名を参照する](#attribute-first-name)

### 一致するカスタム属性に基づいてメッセージをパーソナライズする {#attribute-matching}

このユースケースでは、ユーザーが特定のカスタム属性を持っているかどうかを確認し、持っている場合は異なるパーソナライズされたメッセージを表示します。

{% raw %}
```liquid
{% if custom_attribute.${hasShovel} == true and custom_attribute.${VisitToGroundTooTough} > 0 %}
The ground is very hard. The dirt road goes East.
{% elsif custom_attribute.${hasShovel} == true %}
The dirt road goes East.
{% elsif custom_attribute.${VisitToStart} > 0 %}
The dirt road goes East.
The shovel here.
{% else %}
You are at a dead-end of a dirt road. The road goes to the east. In the distance, you can see that it will eventually fork off. The trees here are very tall royal palms, and they are spaced equidistant from each other.
There is a shovel here.
{% endif %}
```
{% endraw %}

### ヨーロッパの数値表記規則に合わせて通貨をフォーマットする {#european-currency-format}

小数点にカンマ、千の位にピリオドを使用するロケール（ドイツやイタリアなど）では、[`money`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters/#money-filter)フィルターと[`number_with_delimiter`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/#number-formatting-filters)フィルターを`replace`と組み合わせて区切り文字を入れ替えます。ピリオドとカンマが同じパスで入れ替わらないように、`#`を一時的なプレースホルダーとして使用します。

{% raw %}
```liquid
{{ 1234567.89 | money | number_with_delimiter | replace: '.', '#' | replace: ',', '.' | replace: '#', ',' }}
```

**出力:** `1.234.567,89`

**説明:** `money`フィルターは小数点以下を追加しますが、通貨記号やロケール固有の区切り文字は追加しません。`number_with_delimiter`はUS形式の千の位区切りを追加し、`replace`フィルターでヨーロッパ形式に変換します。
{% endraw %}

### 2つのカスタム属性を減算して差額を金額として表示する {#attribute-monetary-difference}

このユースケースでは、2つの金額カスタム属性を取得し、差額を計算して表示することで、目標達成までの残り金額をユーザーに知らせます。

{% raw %}
```liquid
{% assign event_goal = {{custom_attribute.${last_selected_event_personal_goal}}} %}
{% assign current_raised =  {{custom_attribute.${last_selected_event_personal_amount_raised}}} %}
{% assign difference =  event_goal | minus: current_raised %}
You only have ${{ difference | round: 0 | number_with_delimiter }} left to raise!
```
{% endraw %}

### フルネームがfirst_nameフィールドに保存されている場合にユーザーの名を参照する {#attribute-first-name}

このユースケースでは、ユーザーの名（姓と名が1つのフィールドに保存されている場合）を取得し、その名を使用してウェルカムメッセージを表示します。

{% raw %}
```liquid
{{${first_name} | truncatewords: 1, "" | default: 'hi'}}
{% assign name = {{${first_name}}} | split: ' ' %}
Hi {{name[0]}}, here's your message!
```

**説明:** `split`フィルターは、`{{${first_name}}}`に保持されている文字列を配列に変換します。`{{name[0]}}`を使用することで、配列の最初の項目（ユーザーの名）のみを参照します。

{% endraw %}
{% endapi %}

{% api %}

## カスタムイベント {#custom-event}

{% apitags %}
Custom event
{% endapitags %}

- [カスタムイベントが現在から2時間以内の場合にプッシュ通知を中止する](#event-abort-push)
- [ユーザーがカスタムイベントを3回実行するたびにCampaignを送信する](#event-three-times)
- [1つのカテゴリからのみ購入したユーザーにメッセージを送信する](#event-purchased-one-category)
- [過去1か月間にカスタムイベントが発生した回数を追跡する](#track)


### カスタムイベントが現在から2時間以内の場合にプッシュ通知を中止する {#event-abort-push}

このユースケースでは、イベントまでの時間を計算し、残り時間に応じて異なるパーソナライズされたメッセージを表示します。

たとえば、カスタムイベントプロパティが今後2時間以内に到来する場合にプッシュ送信を防止したい場合があります。この例では、電車のチケットの放棄カートのシナリオを使用しています。

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign dep_time = {{event_properties.${outboundDate_Time}}} | date: "%s" %}
{% assign time_to_dep = dep_time | minus: today %}
{% if {{time_to_dep}} <= 7200 %}
{% abort_message("OutboundDate less than 2 hours") %}
{% elsif {{time_to_dep}} > 7200 and {{time_to_dep}} < 86400 %}
Don't forget to buy your ticket to {{event_properties.${toStation}}} within next 24 hours
{% else %}
Still traveling to {{event_properties.${toStation}}} in more than 24 hours? Book now
{% endif %}
```
{% endraw %}

### ユーザーがカスタムイベントを3回実行するたびにCampaignを送信する {#event-three-times}

このユースケースでは、ユーザーがカスタムイベントを3回実行したかどうかを確認し、該当する場合はメッセージを表示するかCampaignを送信します。

{% raw %}
```liquid
{% assign cadence = custom_attribute.${example} | minus: 1 | modulo: 3 %}
{% if custom_attribute.${example} == blank %}
{% abort_message("Error calculating cadence") %}
{% elsif cadence != 0 %}
{% abort_message("Skip message") %}
{% endif %}
Did you forget something in your shopping cart?
```
{% endraw %}

{% alert important %} カスタムイベントカウントのイベントプロパティを持つか、BrazeエンドポイントへのWebhookを使用する必要があります。これは、ユーザーがイベントを実行するたびにカスタム属性（`example_event_count`）をインクリメントするためです。この例では3回ごとのケイデンス（1、4、7、10など）を使用しています。ケイデンスをゼロから開始する場合（0、3、6、9など）は、`minus: 1`を削除してください。
{% endalert %}

### 1つのカテゴリからのみ購入したユーザーにメッセージを送信する {#event-purchased-one-category}

このユースケースでは、ユーザーが購入したカテゴリのリストを取得し、購入カテゴリが1つだけの場合にメッセージを表示します。

{% raw %}
```liquid
{% assign category = {{custom_attribute.${categories_purchased}}} %}
{% assign uniq_cat = {{category | uniq }} %}
{% if {{uniq_cat | size}} == 1 %}
{{uniq_cat}}
{% else %}
{% abort_message("Purchase category doesn't exist") %}
{% endif %}
```
{% endraw %}

### 過去1か月間にカスタムイベントが発生した回数を追跡する {#track}

このユースケースでは、当月の1日から前月までの間にカスタムイベントが記録された回数を計算します。その後、users/trackコールを実行してこの値をカスタム属性として保存できます。なお、このCampaignは月次データを使用できるようになるまで、2か月連続で実行する必要があります。

{% raw %}
```liquid

{% capture body %}
{
 "braze_id": "{{${braze_id}}}",
 "fields_to_export": ["custom_events"]
}

{% endcapture %}

{% connected_content YOUR_BRAZE_ENDPOINT/users/export/ids
 :method post
  :headers { "Authorization": "Bearer YOUR_API_KEY" }
  :body {{body}}
 :content_type application/json
 :save response
  :retry %}

{% for custom_event in response.users[0].custom_events %}
{% assign ce_name = custom_event.name %}
{% comment %} The following custom event name will need to be amended for the target custom event. {% endcomment %}

{% if ce_name == "Project Exported" %}
{% comment %}{{custom_event.name}}: {{custom_event.count}}{% endcomment %}
{% assign current_count = custom_event.count %}
{% endif %}
{% endfor %}

{% assign prev_month_count = {{custom_attribute.${projects_exported_prev_month}}} %}
{% assign latest_count = current_count | minus: prev_month_count %}
{% assign now = "now" | date: "%s" %}
{% assign yesterday = {{now}} | minus: 86400 %}
{% assign previous_month = {{yesterday}} | date: "%B" %}
{% assign previous_year = {{yesterday}} | date: "%y" %}
{% assign formatted_month = previous_month | downcase %}
{% comment %}The Custom Event name that is being tracked will be needed to be amended for the target Custom Event in the Attribute Name below. {% endcomment %}
```

```json
"attributes": [
  {
    "external_id":"{{${user_id}}}",
       "projects_exported_{{formatted_month}}_{{previous_year}}": "{{latest_count}}"
  }
]
```

{% endraw %}

{% endapi %}

{% api %}

## 言語 {#language}

{% apitags %}
Language
{% endapitags %}

- [月名を別の言語で表示する](#language-display-month)
- [ユーザーの言語に基づいて画像を表示する](#language-image-display)
- [曜日とユーザーの言語に基づいてメッセージをパーソナライズする](#language-personalize-message)

### 月名を別の言語で表示する {#language-display-month}

このユースケースでは、現在の日付、月、年を表示し、月名を別の言語で表示します。この例ではスウェーデン語を使用しています。

{% raw %}
```liquid
{% assign day = 'now' | date: "%e" %}
{% assign year =  'now' | date: "%Y" %}
{% assign month =  'now' | date: "%B" %}

{% if {{month}} == 'January' %}
{{day}} Januari {{year}}
{% elsif {{month}} == 'February' %}
{{day}} Februari {{year}}
{% elsif {{month}} == 'March' %}
{{day}} Mars {{year}}
{% elsif {{month}} == 'April' %}
{{day}} April {{year}}
{% elsif {{month}} == 'May' %}
{{day}} Maj {{year}}
{% elsif {{month}} == 'June' %}
{{day}} Juni {{year}}
{% elsif {{month}} == 'July' %}
{{day}} Juli {{year}}
{% elsif {{month}} == 'August' %}
{{day}} Augusti {{year}}
{% elsif {{month}} == 'September' %}
{{day}} September {{year}}
{% elsif {{month}} == 'October' %}
{{day}} Oktober {{year}}
{% elsif {{month}} == 'November' %}
{{day}} November {{year}}
{% elsif {{month}} == 'December' %}
{{day}} December {{year}}
{% endif %}
```
{% endraw %}

### ユーザーの言語に基づいて画像を表示する {#language-image-display}

このユースケースでは、ユーザーの言語に基づいて画像を表示します。なお、このユースケースはBrazeメディアライブラリにアップロードされた画像でのみテストされています。

{% raw %}
```liquid
{% if ${language} == 'en' %}
English image URL (for example, https://cdn-staging.braze.com/appboy/communication/assets/image_assets/images/60aecba96a93150c749b4d57/original.png?1622068137)
{% elsif ${language} == 'ru' %}
Russian image URL
{% elsif ${language} == 'es' %}
Spanish image URL
{% else %}
Fallback image URL
{% endif %}
```
{% endraw %}

### 曜日とユーザーの言語に基づいてメッセージをパーソナライズする {#language-personalize-message}

このユースケースでは、現在の曜日を確認し、その曜日に基づいて、ユーザーの言語が提供された言語オプションのいずれかに設定されている場合、その言語で特定のメッセージを表示します。

この例は火曜日で止まっていますが、各曜日に対して繰り返すことができます。

{% raw %}
```liquid
{% assign today  = 'now' | date: '%A' %}

{% if today == 'Monday' %}
{% if ${language} == 'es' %}
Compra hoy y lleva tu aprendizaje de idiomas a niveles más altos. 🚀

{% elsif ${language} == 'en' %}
Purchase today and take your language learning to the next level. 🚀

{% elsif ${language} == 'zh' %}
今天就购买并将您的语言提高到一个新水平吧。🚀

{% else %}
It's Monday, but the language doesn't match
{% endif %}

{% elsif today == 'Tuesday' %}

{% if ${language} == 'zh' %}
不要忘记解锁以获取完整版本哦。🔓

{% elsif ${language} == 'en' %}
Don't forget to unlock the full version of your language. 🔓

{% elsif ${language} == 'ja' %}
すべての機能を使ってみませんか 🔓

{% elsif ${language} == 'es' %}
No te olivides de desbloquear la versión completa del programa de idiomas. 🔓

{% else %}
tuesday default
{% endif %}
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## その他 {#miscellaneous}

{% apitags %}
Miscellaneous
{% endapitags %}

- [マーケティングメールをブロックしている顧客へのメール送信を避ける](#misc-avoid-blocked-emails)
- [顧客のサブスクリプション状態を使用してメッセージ内のコンテンツをパーソナライズする](#misc-personalize-content)
- [文字列内のすべての単語の最初の文字を大文字にする](#misc-capitalize-words-string)
- [カスタム属性の値を配列と比較する](#misc-compare-array)
- [今後のイベントリマインダーを作成する](#misc-event-reminder)
- [配列内の文字列を検索する](#misc-string-in-array)
- [配列内の最大値を見つける](#misc-largest-value)
- [配列内の最小値を見つける](#misc-smallest-value)
- [文字列の末尾をクエリする](#misc-query-end-of-string)
- [複数の組み合わせを持つカスタム属性から配列内の値をクエリする](#misc-query-array-values)
- [文字列を電話番号にフォーマットする](#phone-number)

### マーケティングメールをブロックしている顧客へのメール送信を避ける {#misc-avoid-blocked-emails}

このユースケースでは、Content Blocksに保存されたブロック済みユーザーのリストを取得し、それらのブロック済みユーザーが今後のCampaignやCanvasesで連絡やターゲティングされないようにします。

{% alert important %}
このLiquidを使用するには、まずブロック済みメールのリストをContent Blocks内に保存してください。リストには、メールアドレス間に余分なスペースや文字を挿入しないでください（例：`test@braze.com,abc@braze.com`）。
{% endalert %}

{% raw %}
```liquid
{% assign blocked_emails = {{content_blocks.${BlockedEmailList}}} | split: ',' %}
{% for email in blocked_emails %}
    {% if {{${email_address}}} == email %}
    {% abort_message("Email is blocked") %}
    {% break %}
    {% endif %}
{% endfor %}
Your message here!
```
{% endraw %}

**説明:** ここでは、ブロック済みメールのContent Blocksを参照して、潜在的な受信者のメールがこのリストに含まれているかどうかを確認します。メールが見つかった場合、メッセージは送信されません。

{% alert note %}
Content Blocksのサイズ制限は5 MBです。
{% endalert %}

### 顧客のサブスクリプション状態を使用してメッセージ内のコンテンツをパーソナライズする {#misc-personalize-content}

このユースケースでは、顧客のサブスクリプション状態を取得してパーソナライズされたコンテンツを送信します。特定のサブスクリプショングループに購読しているユーザーには、メールサブスクリプショングループ向けの限定メッセージが届きます。

{% raw %}
```liquid
{% if {{subscribed_state.${subscription_group_id}}} == 'subscribed' %}
This is an exclusive message for subscribed users!
{% else %} This is the default message for other users.
{% endif %}
```
{% endraw %}

### 文字列内のすべての単語の最初の文字を大文字にする {#misc-capitalize-words-string}

このユースケースでは、単語の文字列を取得し、配列に分割して、各単語の最初の文字を大文字にします。

{% raw %}
```liquid
{% assign words_array = {{custom_attribute.${address}}} | split: ' ' %}
{% for words in {{words_array}} %}
{{ words | capitalize | append: ' ' }}
{% endfor %}
```
{% endraw %}

**説明:** ここでは、選択した文字列属性に変数を割り当て、`split`フィルターを使用して文字列を配列に分割しています。次に`for`タグを使用して、新しく作成した配列の各項目に変数`words`を割り当て、`capitalize`フィルターと`append`フィルターで各用語の間にスペースを追加して表示しています。

### カスタム属性の値を配列と比較する {#misc-compare-array}

このユースケースでは、お気に入りの店舗のリストを取得し、ユーザーのお気に入りの店舗がそのリストに含まれているかどうかを確認し、含まれている場合はそれらの店舗からの特別オファーを表示します。

{% raw %}
```liquid
{% assign favorite_stores = 'Target,Walmart,Costco' | split: ',' %}
{% for store in favorite_stores %}
{% if {{custom_attribute.${favorited_stores}}} contains {{store}} %}
Today's offer from {{store}}

{% break %}

{% else %}
{% abort_message("No attribute found") %}
{% endif %}
{% endfor %}
```
{% endraw %}

{% alert important %} このシーケンスには、主要な条件文に`break`タグがあります。これにより、一致が見つかるとループが停止します。多くの一致またはすべての一致を表示したい場合は、`break`タグを削除してください。{% endalert %}

### 今後のイベントリマインダーを作成する {#misc-event-reminder}

このユースケースでは、カスタムイベントに基づいて今後のリマインダーを設定できます。このシナリオ例では、26日以上先のポリシー更新日に対してリマインダーを設定し、ポリシー更新日の26日前、13日前、7日前、または2日前にリマインダーを送信します。

このユースケースでは、以下を[WebhookのCampaign]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/)またはキャンバスステップの本文に配置する必要があります。

{% raw %}
```liquid
{% comment %}
Depending on how the reminder_capture property is passed to Braze, with/without a timestamp, the number of days could impact whether a user falls on either side of the 26/13/7/2-day windows.
Once users have been assigned to a Reminder journey/flow, they are then scheduled to enter a subsequent Canvas.
This 'Event Listener' can be used to split out users into different journeys based on the Custom Event properties sent to Braze.
{% endcomment %}

{% comment %}
When testing, make sure the campaign ID, campaign API endpoint, Canvas ID, Canvas API endpoint are entered correctly. In this example, the Canvas ID and Canvas API endpoint have been set up for sharing with the client. In practice, this can be testing using a campaign ID and Campaign API endpoint.
{% endcomment %}

{% comment %}
The following step calculates how much there is between today's date and the Reminder Date as 'time_to_reminder'.
{% endcomment %}

{% assign today = "now" | date: '%s' %}
{% assign reminder_start_date = {{event_properties.${reminder_date}}} | date: '%s' %}
{% assign time_to_reminder = reminder_start_date | minus: today %}

{% comment %}
The following step checks if the time_to_reminder is more than 26 days away; if this is true, then the user is scheduled to enter the subsequent Canvas 26 days before the reminder_date.
The time is converted from 'seconds from 1970' to the appropriate Reminder Date in the required ISO 8601 format.
N.B. Additional time zones would need to be catered for by adding an additional API Schedule property of "in_local_time"
{% endcomment %}

{% if {{time_to_reminder}} > 2246400 %}
{% assign time_to_first_message = reminder_start_date | plus: 2246400 %}
{{ time_to_first_message | date: '%Y-%m-%dT%H:%M' }}
{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than 26 days away but more than 13 days away.
Users are scheduled to enter the journey on day 13.
{% endcomment %}

{% elsif 1123200 > {{time_to_reminder}} and {{time_to_reminder}} < 2246399 %}
{% assign time_to_first_message = reminder_start_date | plus: 1123200 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than 13 days away but more than seven days away.
Users are scheduled to enter the journey on day 7.
{% endcomment %}

{% elsif 604800 > {{time_to_reminder}} and {{time_to_reminder}} < 1123199 %}
{% assign time_to_first_message = reminder_start_date | plus: 604800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than seven days away but more than two days away.
Users are scheduled to enter the journey on day 2.
{% endcomment %}

{% elsif {{time_to_reminder}} < 604799 and {{time_to_reminder}} > 172860 %}
{% assign time_to_first_message = reminder_start_date | plus: 172800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}
{% endif %}
```
{% endraw %}

{% alert important %}

カスタムイベント`reminder_capture`が必要であり、カスタムイベントプロパティには少なくとも以下を含める必要があります。

- `reminder-id`: カスタムイベントの識別子
- `reminder_date`: ユーザーが送信したリマインダーの期日
- `message_personalisation_X`: 送信時にメッセージをパーソナライズするために必要なプロパティ

{% endalert %}

### 配列内の文字列を検索する {#misc-string-in-array}

このユースケースでは、カスタム属性の配列に特定の文字列が含まれているかどうかを確認し、存在する場合は特定のメッセージを表示します。

{% raw %}
```liquid
{% if custom_attribute.${PartnershipProgramsNotLinked} contains 'Hertz' %}
Link your Hertz account to use Hertz Fast Lane.
{% endif %}
```
{% endraw %}

### 配列内の最大値を見つける {#misc-largest-value}

このユースケースでは、指定されたカスタム属性配列内の最大値を計算し、ユーザーメッセージングで使用します。

たとえば、現在のハイスコアやアイテムの最高入札額をユーザーに表示したい場合があります。

{% raw %}
```liquid
{% assign maxValue = 0 %}
{% for attribute in {{custom_attribute.${array_attribute}}} %}
{% assign compareValue = {{attribute | plus: 0}} %}
{% if compareValue > maxValue %}
{% assign maxValue = compareValue %}
{% endif %}
{% endfor %}
{{maxValue}}
```
{% endraw %}

{% alert important %}
整数値を持ち、配列（リスト）の一部であるカスタム属性を使用する必要があります。{% endalert %}

### 配列内の最小値を見つける {#misc-smallest-value}

このユースケースでは、指定されたカスタム属性配列内の最小値を計算し、ユーザーメッセージングで使用します。

たとえば、最低スコアや最安値のアイテムをユーザーに表示したい場合があります。

{% raw %}
```liquid
{% assign minValue = custom_attribute.${array_attribute}[0] | plus: 0 %}
{% for attribute in {{custom_attribute.${array_attribute}}} %}
{% assign compareValue = {{attribute | plus: 0}} %}
{% if compareValue < minValue %}
{% assign minValue = compareValue %}
{% endif %}
{% endfor %}
{{minValue}}
```
{% endraw %}

{% alert important %} 整数値を持ち、配列（リスト）の一部であるカスタム属性を使用する必要があります。{% endalert %}

### 文字列の末尾をクエリする {#misc-query-end-of-string}

このユースケースでは、メッセージングで使用するために文字列の末尾をクエリします。

{% raw %}
```liquid
{% assign interest = {{custom_attribute.${Buyer Interest}}} | first %}
{% assign marketplace = interest | split: "" | reverse | join: "" | truncate: 4, "" %}
{% if {{marketplace}} == '3243' %}

Your last marketplace search was on {{custom_attribute.${Last marketplace buyer interest} | date: '%d.%m.%Y'}}. Check out all of our new offers.

{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

### 複数の組み合わせを持つカスタム属性から配列内の値をクエリする {#misc-query-array-values}

このユースケースでは、まもなく期限切れになる番組のリストを取得し、ユーザーのお気に入りの番組がそのリストに含まれているかどうかを確認し、含まれている場合はまもなく期限切れになることを通知するメッセージを表示します。

{% raw %}
```liquid
{% assign expired_shows = 'Modern Family,The Rookie,Body of Proof,Felicity' | split: ',' %}
{% for show in expired_shows %}
{% if {{custom_attribute.${Favorite Shows}}} contains {{show}} %}
{% assign new_shows = new_shows | append: {{show}} | append: '*' %}
{% endif %}
{% endfor %}
{% assign new_shows_clean = new_shows | split: '*' %}
{% if new_shows_clean.size != 0 %}

All episodes of {{new_shows_clean | join: ', ' }} expire on 9/8 - watch them now before they're gone!

{% else %}
{% abort_message("Not found") %}
{% endif %}
```
{% endraw %}

{% alert important %} まず配列間の一致を見つけ、最後に一致を分割するロジックを構築する必要があります。{% endalert %}

### 文字列を電話番号にフォーマットする {#phone-number}

このユースケースでは、`phone_number`ユーザープロファイルフィールド（デフォルトでは整数の文字列としてフォーマットされています）をインデックスし、ローカルの電話番号標準に基づいて再フォーマットする方法を示します。たとえば、1234567890を(123)-456-7890に変換します。

{% raw %}
```liquid
{% assign phone = {{${phone_number}}} | remove: "-" | split: '' %}

({{ phone[0] }}{{ phone[1] }}{{ phone[2] }})-{{ phone[3] }}{{ phone[4] }}{{ phone[5] }}-{{ phone[6] }}{{ phone[7] }}{{ phone[8] }}{{ phone[9] }}
```
{% endraw %}

{% endapi %}

{% api %}

## プラットフォームターゲティング {#platform-targeting}

{% apitags %}
Platform targeting
{% endapitags %}

- [デバイスOSによってコピーを差別化する](#platform-device-os)
- [特定のプラットフォームのみをターゲットにする](#platform-target)
- [特定のOSバージョンのiOSデバイスのみをターゲットにする](#platform-target-ios-version)
- [Webブラウザのみをターゲットにする](#platform-target-web)
- [特定のモバイルキャリアをターゲットにする](#platform-target-carrier)

### デバイスOSによってコピーを差別化する {#platform-device-os}

このユースケースでは、ユーザーがどのプラットフォームを使用しているかを確認し、プラットフォームに応じて特定のメッセージを表示します。

たとえば、モバイルユーザーには短いバージョンのメッセージコピーを表示し、その他のユーザーには通常の長いバージョンのコピーを表示したい場合があります。また、モバイルユーザーに関連するメッセージを表示しつつ、Webユーザーには関連しないメッセージを表示することもできます。たとえば、iOSのメッセージではApple Payについて言及し、AndroidのメッセージではGoogle Payについて言及するなどです。

{% raw %}
```liquid
{% if targeted_device.${platform} == "ios" or targeted_device.${platform} == "android" %}
This is a shorter copy.

{% else %}
This is the regular copy and much longer than the short version.
{% endif %}
```
{% endraw %}

{% alert note %}
Liquidは大文字と小文字を区別します。`targeted_device.${platform}`はすべて小文字で値を返します。
{% endalert %}

### 特定のプラットフォームのみをターゲットにする {#platform-target}

このユースケースでは、ユーザーのデバイスプラットフォームを取得し、プラットフォームに応じてメッセージを表示します。

たとえば、Androidユーザーにのみメッセージを送信したい場合があります。これは、セグメンテーションツール内でアプリを選択する代替手段として使用できます。

{% raw %}
```liquid
{% if {{targeted_device.${platform}}} == 'android' %}

This is a message for an Android user!

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### 特定のOSバージョンのデバイスのみをターゲットにする {#platform-target-ios-version}

このユースケースでは、ユーザーのOSバージョンが特定のバージョンセットに該当するかどうかを確認し、該当する場合は特定のメッセージを表示します。

この例では、OSバージョン10.0以前のユーザーに、デバイスOSのサポートを段階的に終了することを警告するメッセージを送信しています。

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == "10.0" or {{targeted_device.${os}}} == "10.0.1" or {{targeted_device.${os}}} == "10.0.2" or {{targeted_device.${os}}} == "10.0.3" or {{targeted_device.${os}}} == "10.1" or {{targeted_device.${os}}} == "10.2" or {{targeted_device.${os}}} == "10.2.1" or {{targeted_device.${os}}} == "10.3" or {{targeted_device.${os}}} == "10.3.1" or {{targeted_device.${os}}} == "10.3.2" or {{targeted_device.${os}}} == "10.3.3" or {{targeted_device.${os}}} == "10.3.4" or {{targeted_device.${os}}} == "9.3.1" or {{targeted_device.${os}}} == "9.3.2" or {{targeted_device.${os}}} == "9.3.3" or {{targeted_device.${os}}} == "9.3.4" or {{targeted_device.${os}}} == "9.3.5" %}

We are phasing out support for your device's operating system. Be sure to update to the latest software for the best app experience.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Webブラウザのみをターゲットにする {#platform-target-web}

このユースケースでは、ユーザーのターゲットデバイスがMacまたはWindowsで動作しているかどうかを確認し、該当する場合は特定のメッセージを表示します。

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == 'Mac' or {{targeted_device.${os}}} == 'Windows' %}

This message will display on your desktop web browser.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

以下のユースケースでは、WebユーザーがiOSまたはAndroidを使用しているかどうかを確認し、該当する場合は特定のメッセージを表示します。

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == 'iOS' and {{targeted_device.${platform}}} == 'web' %}

Content for iOS.

{% elsif {{targeted_device.${os}}} == 'android' and {{targeted_device.${platform}}} == 'web' %}

Content for Android.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### 特定のモバイルキャリアをターゲットにする {#platform-target-carrier}

このユースケースでは、ユーザーのデバイスキャリアがVerizonかどうかを確認し、該当する場合は特定のメッセージを表示します。

プッシュ通知とアプリ内メッセージチャネルでは、Liquidを使用してメッセージ本文にデバイスキャリアを指定できます。受信者のデバイスキャリアが一致しない場合、メッセージは送信されません。

{% raw %}
```liquid
{% if {{targeted_device.${carrier}}} contains "verizon" or {{targeted_device.${carrier}}} contains "Verizon" %}

This is a message for Verizon users!

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## SMS

{% apitags %}
SMS
{% endapitags %}

- [受信SMSキーワードに基づいて異なるメッセージで応答する](#sms-keyword-response)

### 受信SMSキーワードに基づいて異なるメッセージで応答する {#sms-keyword-response}

このユースケースでは、動的なSMSキーワード処理を組み込み、特定の受信メッセージに対して異なるメッセージコピーで応答します。たとえば、「START」とテキスト送信した場合と「JOIN」とテキスト送信した場合で異なる応答を送信できます。

{% raw %}
```liquid
{% assign inbound_message = {{sms.${inbound_message_body}}} | downcase | strip %}
{% if inbound_message contains 'start' %}
Thanks for joining our SMS program! Make sure your account is up to date for the best deals!

{% elsif inbound_message contains 'join' %}
Thanks for joining our SMS program! Create an account to get the best deals!

{% else %}
Thanks for joining our SMS program!

{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## タイムゾーン {#time-zones}

{% apitags %}
Time zones
{% endapitags %}

- [ユーザーのタイムゾーンをテンプレートに挿入する](#users-time-zone)
- [ユーザーのタイムゾーンに応じてメッセージをパーソナライズする](#personalize-timezone)
- [カスタム属性にCSTタイムゾーンを付加する](#time-append-cst)
- [タイムスタンプを挿入する](#time-insert-timestamp)
- [ユーザーのローカルタイムゾーンの時間枠内でのみCanvasプッシュを送信する](#time-canvas-window)
- [ユーザーのローカルタイムゾーンの時間枠内で繰り返しアプリ内メッセージCampaignを送信する](#time-reocurring-iam-window)
- [ユーザーのローカルタイムゾーンで平日と週末に異なるメッセージを送信する](#time-weekdays-vs-weekends)
- [ユーザーのローカルタイムゾーンの時間帯に基づいて異なるメッセージを送信する](#time-of-day)
- [送信時に時間範囲外の場合にメッセージを中止する](#abort-send-time-hour-range)
- [固定タイムゾーンの時間枠外でメッセージを中止する](#abort-fixed-timezone-window)

{% alert note %}
ユーザーが予期しないローカル時刻にメッセージを受信した場合、デバイスまたはプロファイルのタイムゾーンが変更された可能性があります（たとえば、旅行後など）。ローカルタイム配信では、送信時のプロファイルのタイムゾーンを使用します。{% raw %}`{{${time_zone}}}`{% endraw %}などの値が期待どおりに反映されるには、ユーザーが通常の地域で新しいセッションを開始する必要がある場合があります。ただし、[ユーザーのタイムゾーンをテンプレートに挿入する](#users-time-zone)ことは可能です。
{% endalert %}

### ユーザーのタイムゾーンをテンプレートに挿入する {#users-time-zone}

デフォルトでは、Liquidの日付と時刻は協定世界時（UTC）で表示されます。ユーザーのローカルタイムゾーンで日付と時刻を表示するには、`time_zone`フィルターを`date`フィルターと組み合わせて使用します。

#### ローカルの日付と時刻を割り当てる {#assign-local-date-and-time}

ユーザーのローカルタイムゾーンでの現在の日付と時刻を反映する変数を割り当てるには、次の形式を使用します。

{% raw %}
```liquid
{% assign local_date_time = 'now' | time_zone:{{${time_zone}}} | date: '%B %e, %Y' %}
{{local_date_time}}
```
{% endraw %}

- `now`: 現在の日付と時刻をUTCで取得します。
- `time_zone`: {% raw %}`{{${time_zone}}}`{% endraw %}パーソナライゼーションタグを使用して、デフォルト属性からユーザーのローカルタイムゾーンを取得します。
- `date`: ユーザーのローカルの日付と時刻を指定に従ってフォーマットします。前の例では、「February 26, 2026」のようにフォーマットされた文字列が表示されます。その他のフォーマットオプションについては、[strftime.net](strftime.net)を参照してください。

#### カスタム属性にユーザーのタイムゾーンを適用する {#apply-the-users-time-zone-with-custom-attributes}

次のように、`time_zone`フィルターをカスタム属性に適用できます。

{% raw %}
```liquid
{{custom_attribute.${date_time_attribute} | time_zone: {{${time_zone}}} | date: '%a, %b %e, %Y'}}
```
{% endraw %}

これにより、`date_time_attribute`が曜日の省略形、月の省略形、日、4桁の年の順にフォーマットされて出力されます。

### ユーザーのタイムゾーンに応じてメッセージをパーソナライズする {#personalize-timezone}

このユースケースでは、ユーザーのタイムゾーンに基づいて異なるメッセージを表示します。

{% raw %}
```liquid
{% if {{${time_zone}}} == 'xx' %}
Message for time zone xx.
{% elsif {{${time_zone}}} == 'yy' %}
Message for time zone yy.
{% else %}
{% abort_message("Invalid time zone") %}
{% endif %}
```
{% endraw %}

### カスタム属性にCSTタイムゾーンを付加する {#time-append-cst}

このユースケースでは、指定されたタイムゾーンでカスタム日付属性を表示します。

オプション1:
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone: -0005 | date: '%B, %d %Y' }}
```
{% endraw %}

オプション2:
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone: 'America/Chicago' | date: '%B %d %Y %z' }}
```
{% endraw %}

### タイムスタンプを挿入する {#time-insert-timestamp}

このユースケースでは、現在のタイムゾーンのタイムスタンプを含むメッセージを表示します。

以下の例では、日付をYYYY-mm-dd HH:MM:SSの形式で表示します（例：2021-05-03 10:41:04）。

{% raw %}
```liquid
{{${user_id} | default: 'You'}} received a campaign, rendered at ({{ "now" | time_zone: ${time_zone} | date: "%Y-%m-%d %H:%M:%S" }})
```
{% endraw %}

### ユーザーのローカルタイムゾーンの時間枠内でのみCanvasプッシュを送信する {#time-canvas-window}

このユースケースでは、ユーザーのローカルタイムゾーンでの時刻を確認し、設定された時間内であれば特定のメッセージを表示します。

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}

Here's a message that will send between 8 am and 8 pm!
```
{% endraw %}

### ユーザーのローカルタイムゾーンの時間枠内で繰り返しアプリ内メッセージCampaignを送信する {#time-reocurring-iam-window}

このユースケースでは、ユーザーの現在の時刻が設定された時間枠内にある場合にメッセージを表示します。

たとえば、以下のシナリオでは、店舗が閉店していることをユーザーに知らせます。

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 21 or hour < 10 %}

Store's closed. Come back between 11 am and 9 pm!

{% else %}
{% abort_message("Not sent because the store is open") %}
{% endif %}
```
{% endraw %}

### ユーザーのローカルタイムゾーンで平日と週末に異なるメッセージを送信する {#time-weekdays-vs-weekends}

このユースケースでは、ユーザーの現在の曜日が土曜日か日曜日かを確認し、曜日に応じて異なるメッセージを表示します。

{% raw %}
```liquid
{% assign today = 'now' | time_zone: ${time_zone} | date: "%A" %}
{% if {{today}} == 'Saturday' or {{today}} == 'Sunday' %}
It's {{today}}, why don't you open the app for your transactions?

{% else %}
It's {{today}}, why don't you visit the store?
{% endif %}
```
{% endraw %}

### ユーザーのローカルタイムゾーンの時間帯に基づいて異なるメッセージを送信する {#time-of-day}

このユースケースでは、ユーザーの現在の時刻が設定された時間枠外にある場合にメッセージを表示します。

たとえば、時間帯に依存する時間限定のオファーについてユーザーに伝えたい場合があります。

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}

Check out this new bar after work today. HH specials!
```
{% endraw %}

{% alert note %} これは[クワイエットアワー]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types/#time-based-options)の逆です。{% endalert %}

### 送信時に時間範囲外の場合にメッセージを中止する {#abort-send-time-hour-range}

このユースケースでは、現在の時間が定義された範囲外の場合にメッセージを中止します。`time_zone`フィルターを適用しない限り、メッセージがレンダリングされる時刻（デフォルトではUTC）を使用し、ユーザーのローカルタイムゾーンは使用しません。ユーザーのローカルタイムゾーンに基づいてメッセージを送信するには、[ユーザーのローカルタイムゾーンの時間帯に基づいて異なるメッセージを送信する](#time-of-day)を参照してください。

{% raw %}
```liquid
{% assign time = 'now' %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside hour range") %}
{% endif %}

Check out this new bar after work today. HH specials!
```
{% endraw %}

### 固定タイムゾーンの時間枠外でメッセージを中止する {#abort-fixed-timezone-window}

このユースケースでは、特定のタイムゾーン（この例ではシンガポール時間）で現在の時刻が定義された時間枠外の場合にメッセージを中止します。各ユーザーの`time_zone`属性ではなく、1つの地域に紐づいたクワイエットアワーのようなルールが必要な場合に、このパターンを使用できます。

{% raw %}
```liquid
{% assign time = 'now' | time_zone: 'Asia/Singapore' %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% assign minute = time | date: '%M' | plus: 0 %}

{% if hour < 20 or hour > 21 or (hour == 21 and minute > 45) %}
{% abort_message("Not within eligible time of 8 pm–9:45 pm SGT") %}
{% endif %}

Sign up for our exclusive time-limited offer now!
```
{% endraw %}

{% endapi %}

{% api %}

## 週/日/月 {#weekdaymonth}

{% apitags %}
Week/Day/Month
{% endapitags %}

- [前月の名前をメッセージに取り込む](#month-name)
- [毎月末にCampaignを送信する](#month-end)
- [月の最後の（平日）にCampaignを送信する](#day-of-month-last)
- [月の各日に異なるメッセージを送信する](#day-of-month)
- [曜日ごとに異なるメッセージを送信する](#day-of-week)
- [特定のカレンダー日にメッセージを中止する](#abort-specific-calendar-date)
- [特定の曜日にメッセージを中止する](#abort-specific-weekday)

### 前月の名前をメッセージに取り込む {#month-name}

このユースケースでは、現在の月を取得し、前月を表示してメッセージングで使用します。

{% raw %}
```liquid
{% assign today = 'now' | date: "%m" %}
{% assign last_month = {{today}} | minus: 1 %}
{% if last_month == 1 %}
{% assign month = "January" %}
{% elsif last_month == 2 %}
{% assign month = "February" %}
{% elsif last_month == 3 %}
{% assign month = "March" %}
{% elsif last_month == 4 %}
{% assign month = "April" %}
{% elsif last_month == 5 %}
{% assign month = "May" %}
{% elsif last_month == 6 %}
{% assign month = "June" %}
{% elsif last_month == 7 %}
{% assign month = "July" %}
{% elsif last_month == 8 %}
{% assign month = "August" %}
{% elsif last_month == 9 %}
{% assign month = "September" %}
{% elsif last_month == 10 %}
{% assign month = "October" %}
{% elsif last_month == 11 %}
{% assign month = "November" %}
{% elsif last_month == 0 %}
{% assign month = "December" %}
{% endif %}

Here's an overview of what your spending looked like in {{month}}.
```
{% endraw %}

同じ結果を得るために、以下の方法も使用できます。

{% raw %}
```liquid
{% assign last_month_name = 'now' | date: "%Y-%m-01" | date: '%s' | minus: 1 | date: "%B" %}

Here's an overview of what your spending looked like in {{last_month_name}}.
```
{% endraw %}

### 毎月末にCampaignを送信する {#month-end}

このユースケースでは、現在の日付が日付リストに含まれているかどうかを確認し、日付に応じて特定のメッセージを表示します。

{% alert note %} うるう年（2月29日）は考慮されていません。{% endalert %}

{% raw %}
```liquid
{% assign current_date = 'now' | date: '%b %d' %}

{% if current_date == "Jan 31" or current_date == "Feb 28" or current_date == "Mar 31" or current_date == "Apr 30" or current_date == "May 31" or current_date == "Jun 30" or current_date == "Jul 31" or current_date == "Aug 31" or current_date == "Sep 30" or current_date == "Oct 31" or current_date == "Nov 30" or current_date == "Dec 31" %}

The date is correct

{% else %}
{% abort_message("Date is not listed") %}
{% endif %}
```
{% endraw %}

### 月の最後の（平日）にCampaignを送信する {#day-of-month-last}

このユースケースでは、現在の月と日を取得し、現在の日が月の最後の平日に該当するかどうかを計算します。

たとえば、毎月最後の水曜日にユーザーに製品フィードバックのアンケートを送信したい場合があります。

{% raw %}
```liquid
{% comment %}Pull the day, day name, month, and year from today's date.{% endcomment %}
{% assign current_day = "now" | date: "%d" %}
{% assign current_day_name = "now" | date: "%a" %}
{% assign current_month = "now" | date: "%b" %}
{% assign current_year = "now" | date: "%Y" %}

{% comment %}Assign the correct number of days for the current month.{% endcomment %}

{% if current_month == "Jan" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Mar" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Apr" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "May" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Jun" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Jul" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Aug" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Sep" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Oct" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Nov" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Dec" %}
{% assign last_day_of_month = 31 %}
{% endif %}

{% comment %}Assign the correct number of days if the current month is February, taking into account leap years.{% endcomment %}

{% assign leap_year_remainder = current_year | modulo: 4 %}
{% if leap_year_remainder == 0 and current_month == "Feb" %}
{% assign last_day_of_month = 29 %}
{% elsif current_month == "Feb" %}
{% assign last_day_of_month = 28 %}
{% endif %}

{% comment %}Check that today's date is within a week of the last day of the month. If not, abort the message. If so, check that today is Wednesday. If not, abort the message.{% endcomment %}

{% assign diff_in_days = last_day_of_month | minus: current_day | plus: 1%}
{% if diff_in_days <= 7 %}
{% unless current_day_name == "Wed" %}
{% abort_message("Wrong day of the week") %}
{% endunless %}
{% else %}
{% abort_message("Not the last week of the month") %}
{% endif %}
```
{% endraw %}

### 月の各日に異なるメッセージを送信する {#day-of-month}

このユースケースでは、現在の日付がリスト上の日付と一致するかどうかを確認し、日に応じて異なるメッセージを表示します。

{% raw %}
```liquid
{% assign today = 'now' | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_1 = "2019-12-01" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_2 = "2019-12-02" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_3 = "2019-12-03" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}

{% if today == day_1 %}
Message for 2019-12-01

{% elsif today == day_2 %}
Message for 2019-12-02

{% elsif today == day_3%}
Message for 2019-12-03

{% else %}
{% abort_message("Date not listed") %}
{% endif %}
```
{% endraw %}

### 曜日ごとに異なるメッセージを送信する {#day-of-week}

このユースケースでは、現在の曜日を確認し、曜日に応じて異なるメッセージを表示します。

{% raw %}
```liquid
{% assign today = 'now' | date: "%A" %}
{% case today %}
{% when 'Monday' %}
Monday copy

{% when 'Tuesday' %}
Tuesday copy

{% when 'Wednesday' %}
Wednesday copy

{% when  'Thursday' %}
Thursday copy

{% when  'Friday' %}
Friday copy

{% when 'Saturday' %}
Saturday copy

{% when 'Sunday' %}
Sunday copy

{% else %}
Default copy
{% endcase %}
```
{% endraw %}

{% alert note %}
「Default copy」の行を{% raw %}`{% abort_message() %}`{% endraw %}に置き換えて、曜日が不明な場合にメッセージの送信を防止できます。
{% endalert %}

### 特定のカレンダー日にメッセージを中止する {#abort-specific-calendar-date}

このユースケースでは、毎年選択した月と日（この例では5月5日）にメッセージを中止します。`date`フィルターで構築した明確な月日の文字列と現在の日付を比較します。

{% raw %}
```liquid
{% assign date = 'now' | date: '%d/%m' %}
{% if date == '05/05' %}
{% abort_message('No message on the 5th of May') %}
{% endif %}
```
{% endraw %}

### 特定の曜日にメッセージを中止する {#abort-specific-weekday}

このユースケースでは、Liquidが実行される曜日が指定した曜日（この例では`Wednesday`）の場合にメッセージを中止します。`%A`フィルターは英語の完全な曜日名を返します。

{% raw %}
```liquid
{% assign weekday = 'now' | date: '%A' %}
{% if weekday == 'Wednesday' %}
{% abort_message("No message on Wednesdays") %}
{% endif %}
```
{% endraw %}

{% endapi %}

このライブラリの多くの例では、条件が満たされない場合に送信をスキップするために`abort_message`タグを使用しています。Liquidによる送信中止の完全なリファレンス（日付や時間ベースのパターンを含む）については、[Liquidメッセージの中止]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/)を参照してください。