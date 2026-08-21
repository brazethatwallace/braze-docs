---
nav_title: カスタムフォームブロックの作成
article_title: ランディングページでのカスタムフォームブロックの作成
page_order: 6
page_type: reference
description: "Brazeランディングページでカスタムインタラクティブフォーム入力を構築し、その値を標準フォームブロックと一緒にバリデーションおよび送信する方法を説明します。"
---

# ランディングページでのカスタムフォームブロックの作成 {#create-custom-form-blocks-on-landing-pages}

> Brazeランディングページの[フォームブロック]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)は、テキストフィールド、チェックボックス、ドロップダウンなどの標準入力をキャプチャします。カスタムフォームブロックは、星評価、絵文字センチメントピッカー、スクラッチカードなど、独自のインタラクティブ要素を構築できるようにすることで、可能性を広げます。

訪問者がカスタムフォームを送信すると、選択した値はバリデーションされ、標準フィールドと一緒に保存された後、カスタムユーザー属性としてBrazeに送信されます。これにより、ランディングページエディターを離れることなく、より豊かで魅力的な入力を収集できます。

カスタムフォームブロックは、単一のJavaScriptヘルパー `window.brazeHelpers.forms.registerFormInput` を使用して構築します。これはランディングページの**カスタムコード**ブロックから呼び出します。

{% alert note %}
アンケートとアプリ内メッセージには独自のフォームブロックがありますが、`registerFormInput`（カスタムコードUIをフォームブロックに接続するためのJavaScript API）はランディングページでのみ利用可能です。
{% endalert %}

## 仕組み {#how-it-works}

カスタムフォーム入力とは、ランディングページ上の要素で、その値をキャプチャしてフォームと一緒に送信したいものです。その要素を登録することで、Brazeフォームシステムに接続します。登録により、Brazeはどの要素を監視するか、現在の値をどのように読み取るか、フォーム送信時にその値をどう処理するかを認識します。

1. ランディングページの**カスタムコード**ブロック内にカスタムUIを構築し、`id`などの安定したCSSセレクターを付与します。
2. 設定オブジェクトを指定して `window.brazeHelpers.forms.registerFormInput` を呼び出し、要素を登録します。
3. Brazeは必要に応じて `getValue` 関数を呼び出し、現在の値を読み取ります。
4. フィールドが必須の場合、または `onValidate` 関数を提供した場合、Brazeは値が通過するまで送信をブロックし、無効な要素にスタイル設定可能なCSSクラスを付与します。[バリデーションと必須フィールド](#validation-and-required-fields)を参照してください。
5. フォームが送信されバリデーションに通過すると、Brazeは `onSubmit` 関数を呼び出します。ここでBraze SDKを呼び出して、カスタムユーザー属性などの情報を記録できます。

値の読み取り、バリデーション、送信を行う関数を自分で提供するため、このアプローチはほぼすべてのカスタムフォーム要素で機能し、エディターの標準フィールドタイプに限定されません。

## 基本フレームワーク {#basic-framework}

最もシンプルな登録は、1つの要素をターゲットにし、必須として扱い、データ属性から値を読み取り、フォーム送信時にその値をカスタムユーザー属性に書き込みます。このページの例のように、`DOMContentLoaded` リスナーで呼び出しをラップして、`registerFormInput` が実行される前に要素が存在するようにしてください：

```js
document.addEventListener("DOMContentLoaded", () => {
  window.brazeHelpers.forms.registerFormInput({
    selector: "#my-custom-input",
    isRequired: true,
    getValue: (element) => element.dataset.value ?? null,
    onSubmit: (value) => {
      window.brazeBridge.getUser().setCustomUserAttribute("my_attribute", value);
    },
  });
});
```

ページ上のカスタム入力ごとに `registerFormInput` を1回呼び出します。ランディングページエディターで配置した標準フォームフィールドは登録する必要はありません。登録は**カスタムコード**ブロックで構築したカスタム入力にのみ必要です。

## 設定リファレンス {#configuration-reference}

`registerFormInput` は単一の設定オブジェクトを受け取ります。関数シグネチャとして表現すると、完全な形は次のとおりです：

```js
window.brazeHelpers.forms.registerFormInput({
  // Provide exactly one of `selector` or `element` to identify the input.
  selector?: string,
  element?: HTMLElement,
  isRequired?: boolean | Promise<boolean>,
  getValue: (element: HTMLElement) => value,
  onValidate?: (value, element: HTMLElement) => boolean | Promise<boolean>,
  onSubmit?: (value, element: HTMLElement) => void | Promise<void>,
});
```

最低限、要素を特定する方法（`selector` または `element`）と `getValue` 関数を提供する必要があります。それ以外はすべてオプションです。

| プロパティ | 型 | 必須 | 説明 |
| --- | --- | --- | --- |
| `selector` | `string` | はい（または `element`） | カスタム要素に一致するCSSセレクター（例：`"#scratch-card"`）。Brazeはバリデーションおよび送信時に `querySelector` で遅延解決するため、`registerFormInput` の実行後にDOMに追加された要素にも一致できます。 |
| `element` | `HTMLElement` | はい（または `selector`） | `selector` の代わりに使用する要素への直接参照です。要素がページに接続されている間のみ使用され、両方が提供された場合は `selector` より優先されます。 |
| `isRequired` | `boolean \| Promise<boolean>` | いいえ | `true` の場合、入力に空でない値が入るまでフォームを送信できません。`null`、`undefined`、空文字列（空白のみの文字列を含む）、空配列はすべて空として扱われます。ブール値に解決されるPromiseも指定でき、Brazeは入力がバリデーションされるたびに再評価するため、実行時に必須状態を決定できます。デフォルトは `false` です。完全なバリデーション順序については[バリデーションと必須フィールド](#validation-and-required-fields)を参照してください。 |
| `getValue` | `function` | はい | 入力の現在の値を返します。Brazeは一致した要素を引数として渡すため、DOM（例：`element.dataset.sentiment`）や独自のコード内の変数から値を読み取ることができます。まだ値がない場合は `null` を返してください。 |
| `onValidate` | `function` | いいえ | 現在の値と一致した要素を受け取り、`boolean \| Promise<boolean>`（`isRequired` と同じ戻り値の型）を返す必要があります。`true` は値が有効、`false` は無効を意味します。値の存在以上のルールを適用するために使用します（例：許可された値のセットに含まれているかの確認）。省略した場合、`isRequired` とネイティブ制約バリデーションのみが適用されます。 |
| `onSubmit` | `function` | いいえ | フォームが送信されバリデーションに通過したときに実行されます。現在の値と一致した要素を受け取ります。ここで値をBrazeに記録します（通常は `setCustomUserAttribute` を使用）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="設定リファレンス" }

### onSubmitで値を処理する {#act-on-the-value-in-onsubmit}

`onSubmit` はプレーンなJavaScriptコールバックなので、インテグレーションの必要に応じてキャプチャした値を処理できます。`onSubmit` はフォーム送信の一部として実行されるため、その中で行われる `brazeBridge` 呼び出しは、ランディングページを匿名で開いた訪問者に対しても期待どおりに動作します。ブリッジ呼び出しが機能するもう1つの状況については、[ブリッジの利用可能性]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge#bridge-availability)を参照してください。

最も一般的なパターンは、ランディングページで利用可能な[Braze JavaScriptブリッジ]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge)を使用して、キャプチャした値をユーザープロファイルに書き込むことです：

```js
window.brazeBridge.getUser().setCustomUserAttribute("attribute_name", value);
```

ワークスペースに既に存在するカスタム属性名、または作成したいカスタム属性名を使用してください。渡した値はユーザーのプロファイルに保存され、セグメンテーション、パーソナライゼーション、フォローアップメッセージのトリガーに使用できます。

カスタム属性に限定されません。同じコールバックから、任意の[`brazeBridge.getUser()` メソッド]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge#supported-methods)を呼び出すことができます。例えば、ユーザーを購読グループに追加したり、標準属性を設定したり、カスタムイベントを記録したり、独自のAPIエンドポイントに値を送信したりできます。

{% alert note %}
`onSubmit` 内で `requestImmediateDataFlush` を呼び出す必要はありません。フォーム送信プロセスは、`onSubmit` コールバックの完了後に自動的にすべてのデータをBrazeにフラッシュします。
{% endalert %}

## 例 {#examples}

以下の例は完全で自己完結型です。各例はマークアップ、`<script>` タグ、`<style>` タグを含む単一のブロックで、ランディングページの1つの**カスタムコード**（HTML）ブロックに貼り付けます。各スクリプトの末尾付近にある `registerFormInput` 呼び出しが、カスタム入力をBrazeフォームに接続します。コードサンプルにカーソルを合わせ、コピーアイコンを選択してコピーしてください。

{% alert important %}
これらの例は完全に訪問者のブラウザで実行されます。スクラッチオフの例では、「賞品」は訪問者のブラウザのJavaScriptによって選択されるため、技術に詳しい訪問者はそのコードを変更して好きな結果を得ることができます。報酬、割引、または厳密な訪問者ごとの適用が必要なその他の結果にこのパターンを頼らないでください。セキュリティや収益に関わるものは、代わりに独自のサーバーでバリデーションしてください。
{% endalert %}

<div class="scrollable-code-examples" markdown="1">

{% tabs local %}
{% tab センチメントピッカー %}

**目標：** 訪問者が嬉しい顔または悲しい顔を選択し、その選択が `feedback_sentiment` という名前の文字列カスタム属性に書き込まれます。

以下を単一の**カスタムコード**（HTML）ブロックに貼り付けてください：

```html
<div id="sentiment-picker" class="sentiment-picker">
  <button type="button" data-sentiment="positive" aria-label="Happy">🙂</button>
  <button type="button" data-sentiment="negative" aria-label="Unhappy">🙁</button>
</div>

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const picker = document.getElementById("sentiment-picker");

    picker.querySelectorAll("button").forEach((button) => {
      button.addEventListener("click", () => {
        picker.dataset.sentiment = button.dataset.sentiment;
        picker.querySelectorAll("button").forEach((b) => b.classList.remove("selected"));
        button.classList.add("selected");
      });
    });

    window.brazeHelpers.forms.registerFormInput({
      selector: "#sentiment-picker",
      isRequired: true,
      getValue: (element) => element.dataset.sentiment ?? null,
      onSubmit: (value) => {
        window.brazeBridge.getUser().setCustomUserAttribute("feedback_sentiment", value);
      },
    });
  });
</script>

<style>
  .sentiment-picker {
    display: flex;
    gap: 16px;
    justify-content: center;
    font-size: 40px;
  }

  .sentiment-picker button {
    background: none;
    border: 2px solid transparent;
    border-radius: 12px;
    cursor: pointer;
    line-height: 1;
    padding: 8px;
  }

  .sentiment-picker button.selected {
    border-color: #1f2933;
  }

  /* Braze adds this class to the registered element when validation fails. */
  .sentiment-picker.bz-validation-error {
    outline: 3px solid #f94144;
    outline-offset: 4px;
    border-radius: 12px;
  }
</style>
```

**仕組み：** ボタンを選択すると、その `data-sentiment` 値がコンテナ要素に保存されます。`getValue` は、Brazeが渡すコンテナ要素からその値を読み取ります。`isRequired` が `true` であるため、訪問者が顔を選択するまでフォームは送信されず、空の間はコンテナに `bz-validation-error` クラスが付与されます。送信時に、選択された値（`"positive"` または `"negative"`）が `feedback_sentiment` に書き込まれます。

{% endtab %}
{% tab スクラッチオフ %}

**目標：** 訪問者がカードをスクラッチして3つの割引（10% Off、20% Off、または25% Off）のいずれかを表示し、その割引が `scratch_off_reward` という名前の文字列カスタム属性に書き込まれます。

この例では、HTMLキャンバス上にスクラッチオフカードを描画します。ページ読み込み時にランダムに報酬が選択され、訪問者がスクラッチして削る不透明なレイヤーの下に隠されます。このキャンバスアプローチは好みのスクラッチウィジェットに置き換えることができます。Brazeに接続するのは `registerFormInput` 呼び出しのみです。以下を単一の**カスタムコード**（HTML）ブロックに貼り付けてください：

```html
<div id="scratch-card" class="scratch-card" data-reward="">
  <span class="scratch-card__reward"></span>
  <canvas class="scratch-card__surface" width="300" height="150"></canvas>
</div>

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const rewards = ["10% Off", "20% Off", "25% Off"];

    const card = document.getElementById("scratch-card");
    const label = card.querySelector(".scratch-card__reward");
    const canvas = card.querySelector(".scratch-card__surface");
    const ctx = canvas.getContext("2d");

    // Randomly assign which reward this visitor will reveal.
    const reward = rewards[Math.floor(Math.random() * rewards.length)];
    label.textContent = reward;

    // Paint the opaque scratch layer over the reward.
    ctx.fillStyle = "#b3b3b3";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.globalCompositeOperation = "destination-out";

    let isScratching = false;

    function scratchAt(event) {
      const rect = canvas.getBoundingClientRect();
      ctx.beginPath();
      ctx.arc(event.clientX - rect.left, event.clientY - rect.top, 18, 0, Math.PI * 2);
      ctx.fill();
    }

    canvas.addEventListener("pointerdown", () => { isScratching = true; });
    canvas.addEventListener("pointermove", (event) => {
      if (isScratching) scratchAt(event);
    });
    canvas.addEventListener("pointerup", () => {
      isScratching = false;
      // The visitor has scratched the card, so record the revealed reward.
      card.dataset.reward = reward;
    });

    window.brazeHelpers.forms.registerFormInput({
      selector: "#scratch-card",
      isRequired: true,
      getValue: (element) => element.dataset.reward || null,
      onValidate: (value) => rewards.includes(value),
      onSubmit: (value) => {
        window.brazeBridge.getUser().setCustomUserAttribute("scratch_off_reward", value);
      },
    });
  });
</script>

<style>
  .scratch-card {
    position: relative;
    width: 300px;
    height: 150px;
    margin: 0 auto;
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  }

  /* The reward sits underneath and is revealed as the canvas is scratched away. */
  .scratch-card__reward {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    font-weight: 700;
    color: #1f2933;
  }

  .scratch-card__surface {
    position: absolute;
    inset: 0;
    border-radius: 12px;
    cursor: pointer;
    touch-action: none;
  }

  /* Braze adds this class to the registered element when validation fails. */
  .scratch-card.bz-validation-error {
    outline: 3px solid #f94144;
    outline-offset: 4px;
    border-radius: 12px;
  }
</style>
```

**仕組み：** ページが読み込まれると、スクリプトは3つの報酬のうち1つをランダムに選び、キャンバス上にその上に不透明なレイヤーを描画します。訪問者がキャンバス上をドラッグすると、`"destination-out"` コンポジットモードがそのレイヤーを消去し、下の報酬が表示されます。`pointerup` 時に、表示された報酬がカードの `data-reward` 属性に書き込まれます。`getValue` はそこから値を読み取り、`onValidate` は定義された3つの報酬のいずれかであることを確認し、`isRequired` はカードがスクラッチされるまで送信を防ぎます。送信時に、表示された割引（例：`"20% Off"`）が `scratch_off_reward` に書き込まれます。

{% endtab %}
{% tab キャンペーンアトリビューション %}

**目標：** 訪問者をランディングページに誘導したキャンペーンをキャプチャし、ダウンストリームのレポートとアトリビューションのためにカスタムイベントプロパティとして記録します。

この例では、ランディングページのフォーム送信を特定のキャンペーンに帰属させる方法を示します。メール、SMS、またはWhatsAppメッセージのランディングページURLに {% raw %}`{{campaign.${api_id}}}`{% endraw %} のようなLiquid変数を追加することで、キャンペーン識別子をランディングページに渡すことができます。カスタムフォームブロックはURLからこのパラメーターを読み取り、キャンペーンAPI IDをイベントプロパティとしてカスタムイベントとして記録するため、どのキャンペーンがフォーム送信を促進しているかを追跡しやすくなります。

以下を単一の**カスタムコード**（HTML）ブロックに貼り付けてください：

```html
<input type="hidden" id="campaign-attribution" value="" />

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const hiddenInput = document.getElementById("campaign-attribution");
    const campaignApiId = new URLSearchParams(window.location.search).get("campaign_api_id");

    if (campaignApiId) {
      hiddenInput.value = campaignApiId;
    }

    window.brazeHelpers.forms.registerFormInput({
      selector: "#campaign-attribution",
      isRequired: false,
      getValue: (element) => element.value || null,
      onSubmit: async (value) => {
        if (!value) {
          return;
        }

        await window.brazeBridge.logCustomEvent("landing_page_form_submitted", {
          campaign_api_id: value,
        });
      },
    });
  });
</script>
```

**仕組み：** ランディングページにリンクするメール、SMS、またはWhatsAppメッセージを作成する際に、Liquidテンプレートを使用してURLにキャンペーン識別子を追加します：{% raw %}`https://your-landing-page.com?campaign_api_id={{campaign.${api_id}}}`{% endraw %}。訪問者がそのメッセージからランディングページに到着すると、スクリプトはURLから `campaign_api_id` パラメーターを読み取り、非表示の入力フィールドに保存します。フォーム送信時にキャンペーンIDが存在する場合、`onSubmit` コールバックはキャンペーンAPI IDをイベントプロパティとして `landing_page_form_submitted` という名前のカスタムイベントを記録します。このイベントはCurrentsに表示され、レポート、セグメンテーション、アトリビューション分析に使用できます。

{% alert tip %}
このパターンを拡張して、メッセージバリエーション、キャンバスステップ、またはアトリビューション目的でランディングページに渡したいその他のLiquid変数など、追加のURLパラメーターをキャプチャすることもできます。
{% endalert %}

{% endtab %}
{% endtabs %}

</div>

## バリデーションと必須フィールド {#validation-and-required-fields}

入力は、フォームを送信する前に、適用されるすべての以下のレイヤーを通過する必要があります：

1. **`isRequired`** は、空でない値の存在に基づいて送信をゲートします。入力にまだ値がない場合は `getValue` から `null` を返して、Brazeが空であることを認識できるようにしてください。空文字列（空白のみの文字列を含む）と空配列も空として扱われますが、`0` と `false` は値が存在するものとして扱われます。`isRequired` はブール値またはブール値に解決されるPromiseで、入力がバリデーションされるたびに再評価されます。
2. **ネイティブ制約バリデーション。** 一致した要素が標準HTML `checkValidity()` APIをサポートしている場合（例：`required`、`pattern`、`min`、`max` を持つネイティブ `<input>`）、Brazeはそれを実行し、失敗した場合に送信をブロックします。完全にカスタムの非ネイティブ要素（`div`、`canvas` など）の場合、このチェックは常に通過するため、独自のロジックに干渉することはありません。
3. **`onValidate`** は、独自のルールに基づいて送信をゲートします。現在の値と一致した要素を受け取り、`boolean \| Promise<boolean>`（`isRequired` と同じ戻り値の型）を返す必要があります。`true` は値が有効、`false` は無効を意味します。許可値チェック、フォーマットチェック、範囲チェック、またはJavaScriptで表現できる任意のロジックに使用してください。

### エラースタイリング {#error-styling}

入力がバリデーションに失敗するたびに、Brazeは `selector` または `element` で一致した要素にCSSクラス `bz-validation-error` を追加し、入力が有効になるとクラスを削除します。無効な状態を好きなようにスタイル設定してください。例えば、問題のある入力に注意を引くアウトラインやボーダーなどを、要素と `bz-validation-error` クラスを組み合わせたルールで追加します：

```css
#my-custom-input.bz-validation-error {
  outline: 3px solid #f94144;
  outline-offset: 4px;
}
```

エラー状態のスタイリングはオプションですが推奨されます。これにより、訪問者はどのカスタム入力が送信をブロックしているかを確認できます。このページの各[例](#examples)には `bz-validation-error` ルールが含まれています。

## ベストプラクティス {#best-practices}

- 安定した一意のセレクターを使用してください。`id` が最も安全な選択です。複数の要素に一致する可能性のあるセレクターは避けてください。
- 値がない場合は、空文字列や `undefined` ではなく `null` を返してください。これにより、必須チェックが予測どおりに動作します。空文字列と空配列も空として扱われますが、`null` は「値なし」の最も明確なシグナルです。
- `getValue` は軽量で同期的に保ってください。Brazeは複数回呼び出す可能性があるため、重い処理を行うのではなく、現在の値を読み取って返すようにしてください。
- `bz-validation-error` 状態をスタイル設定して、訪問者がどのカスタム入力が送信をブロックしているかを確認できるようにしてください。
- カスタム属性名を事前に定義し、一貫性を保つことで、後でデータに基づいて確実にセグメンテーションできるようにしてください。
- 完全な送信をテストしてください。送信後にユーザープロファイルに属性が表示されること、および必須ルールとバリデーションルールが期待どおりに送信をブロックすることを確認してください。

## トラブルシューティング {#troubleshooting}

### 何も選択していないのにフォームが送信される {#the-form-submits-even-though-nothing-was-selected}
`isRequired` が `true` に設定されていることを確認してください。Brazeは `null`、`undefined`、空文字列（空白のみの文字列を含む）、空配列を値なしとして扱います。何も選択されていないときに `getValue` が別のもの（例：空でないデフォルト値やプレースホルダー）を返している場合、必須チェックはそれを検出しません。

### プロファイルに値が表示されない {#the-value-doesnt-appear-on-the-profile}
`onSubmit` が正しい属性名で `window.brazeBridge.getUser().setCustomUserAttribute` を呼び出していること、および**カスタムコード**ブロックがフォームと同じランディングページにあることを確認してください。

### 登録が何も行わないように見える {#registration-seems-to-do-nothing}
`registerFormInput` が実行されるときにセレクターがDOM内に存在する要素に一致していること、およびスクリプトがその要素がレンダリングされた後に実行されていることを確認してください。次に、ブラウザの開発者コンソールを開いてください。`registerFormInput` は設定をバリデーションし、何か問題がある場合（例：`getValue` の欠落、有効なCSSセレクターでないセレクター、型が間違っているプロパティ）、登録を無視し、`[brazeHelpers.forms.registerFormInput]` というプレフィックス付きの警告をログに記録して、何が無効だったかを説明します。

## 関連コンテンツ {#related-content}

- [ランディングページ用JavaScriptブリッジ]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge)では、`onSubmit` で使用する完全な `brazeBridge` リファレンスを説明しています。
- [ランディングページの作成]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)