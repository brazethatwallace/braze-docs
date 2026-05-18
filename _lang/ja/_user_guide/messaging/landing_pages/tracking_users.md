---
nav_title: ユーザーの追跡
article_title: フォームを通じたユーザーの追跡
description: "ランディングページのフォームを送信したユーザーを識別するために、メッセージにLiquidタグを追加する方法を説明します。"
page_order: 2
---

# フォームを通じたユーザーの追跡 {#track-users-through-a-form}

> ランディングページのLiquidタグをメッセージに追加することで、ランディングページのフォームを送信したユーザーを追跡する方法を説明します。このLiquidタグは、メール、SMS、アプリ内メッセージなど、Brazeのすべてのメッセージングチャネルでサポートされています。トラッキングデータの詳細については、[ランディングページのトラッキングデータについて]({{site.baseurl}}/user_guide/messaging/landing_pages/about_tracking_data/)を参照してください。

## 前提条件 {#prerequisites}

開始する前に、[ランディングページ]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/)と[キャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign/)を作成する必要があります。

## 仕組み {#how-it-works}

Brazeの単一チャネルまたはマルチチャネルメッセージに{% raw %}`{% landing_page_url %}`{% endraw %}Liquidタグを追加できます。ユーザーがそのランディングページにアクセスしてフォームを送信すると、Brazeは新しいプロファイルを作成するのではなく、そのデータを既存のプロファイルに自動的にリンクします。以下の例では、ランディングページのLiquidタグを使用して顧客を調査にリンクしています。

{% raw %}
```html
<a href="{% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

{% alert tip %}
ランディングページは、ページURLを外部チャネルに埋め込むことでリードジェネレーションにも使用できます。ランディングページを作成した後、**Landing Page Details**に移動して、ランディングページのユニークURLを取得してください。
{% endalert %}

## ランディングページのLiquidタグの使用 {#using-landing-page-liquid-tags}

### ステップ 1: ページURLの確認 {#page-url}

BrazeはランディングページのURLを使用して、ユニークなLiquidタグを生成します。現在のページURLを変更する場合は、**Messaging** > **Landing Pages**に移動し、ランディングページを開きます。**page URL**で新しいページURLを入力できます。

{% alert warning %}
メッセージ送信後にページURLを変更すると、古いURLを使用してランディングページにアクセスしようとしたユーザーは`404`ページに転送されます。
{% endalert %}

![BrazeのランディングページのページURL例。]({% image_buster /assets/img/landing_pages/url-handle-example.png %}){: style="max-width:80%;"}

### ステップ 2: Liquidタグの生成 {#step-2-generate-the-liquid-tag}

**Messaging** > **キャンペーン**に移動し、キャンペーンを選択します。メッセージエディターで**Personalization**を選択します。

![ドラッグ＆ドロップエディターの「Add personalization」ボタン。]({% image_buster /assets/img/landing_pages/select-personalization.png %}){: style="max-width:75%;"}

Brazeは[ランディングページURL](#page-url)を使用してLiquidタグを自動的に生成します。タグを生成するには、以下の表を参照してください。

| **パーソナライゼーションタイプ** | **Landing Page**を選択します。|
| **ランディングページ** | [事前に作成した](#prerequisites)ランディングページを選択します。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 2: Liquidタグの生成" }

Liquidタグをメッセージに追加するには、**Insert**を選択するか、スニペットをクリップボードにコピーして手動で追加します。

![選択したランディングページの自動生成されたLiquidタグ。]({% image_buster /assets/img/landing_pages/get-snippet.png %}){: style="max-width:40%;"}

スニペットは以下のようになります。

{% raw %}
`````````ruby
{% landing_page_url custom-url-handle %}
```
{% endraw %}

### ステップ 3: メッセージの最終確認と送信 {#step-3-finalize-and-send-your-message}

Liquidスニペットをメッセージに埋め込み、残りのメッセージを完成させます。例：

{% raw %}
`````````html
<a href="{% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

準備ができたら、メッセージを送信してランディングページを通じたユーザーの追跡を開始できます。