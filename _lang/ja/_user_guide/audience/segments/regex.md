---
nav_title: "正規表現"
article_title: "正規表現"
page_order: 8
description: "このリファレンス記事では、正規表現（regex）とは何か、その使い方、およびデバッガー機能を使って正規表現の検証とテストを行う方法について説明しています。"
page_type: reference
tool:
  - Testing Tools


---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/regular-expression-basics-for-braze){: style="float:right;width:120px;border:0;" class="noimgborder"} 正規表現 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomregular-expression-basics-for-braze-stylefloatrightwidth120pxborder0-classnoimgborder-regular-expressions}

> 正規表現（一般的にregexとして知られています）は、検索パターンを定義する文字列です。正規表現を使用すると、テキストのグループ化を検証したり、検索と置換のアクションを実行したりできます。Brazeでは、正規表現を活用して、ターゲットオーディエンスのセグメンテーションやキャンペーンフィルタリングにおいて、より柔軟な文字列マッチングソリューションを提供しています。<br><br>このページでは、正規表現（regex）の概要、使い方、よくある質問、および正規表現をテストするためのregexデバッガーについて説明しています。

<!--{% multi_lang_include video.html id="3h5Xbhl-TxE" align="right" %}-->

リンク先のBrazeラーニングコースでは、正規表現を[Regex101](https://regex101.com/)で使用およびテストする方法を紹介しています。また、[組み込みのregexテスター](#regex-debugger)、便利なリファレンスページ、regexのBrazeラーニング動画で参照されるサンプルデータ、およびよくある質問も提供しています。

## リソース {#resources}

- [正規表現の基礎](https://learning.braze.com/regular-expression-basics-for-braze) Braze Learningコース
- [正規表現チートシート]({{site.baseurl}}/regex_cheat_sheet)
- [サンプルデータ RTF]({% image_buster /assets/download_file/regex-dummy-data.rtf %})

## 正規表現デバッガー {#regex-debugger}

{% alert important %}
このツールはあくまで参考用であり、Brazeプラットフォームでの正規表現の一致を100%保証するものではありません。Brazeでのセグメンテーションおよびフィルター用の正規表現には、自動的に`/gi`修飾子が付加されます。[gi修飾子](https://w3schools.sinsixx.com/jsref/jsref_regexp_modifier_gi.asp.htm)は、文字列内の正規表現に一致するすべての箇所を大文字・小文字を区別せずに検索するために使用されます。
<br>
カスタムイベントのトリガープロパティおよびトリガーフィルター用の正規表現では、`/g`修飾子（大文字・小文字を区別、[g修飾子](https://www.w3schools.com/jsref/jsref_regexp_g.asp)を参照）を使用し、`/i`修飾子は使用しません。カスタムイベントのトリガープロパティおよびトリガーフィルターで大文字・小文字を区別しない検索を行うには、代わりに`(?i)`を使用してください。例えば、`Matches regex (?i)STOP(?-i)`は、あらゆる大文字・小文字の組み合わせでの「STOP」の使用（「stop」、「please stop」、「never stop sending me messages」など）に一致します。
{% endalert %}

{% tabs %}
{% tab 正規表現デバッガー %}
<div>
このフォームでは、正規表現の基本的な検証とテストを行うことができます。
​
正規表現:
​
<div class="input-group">
  <div class="input-group-prepend"><span class="input-group-text">/</span>
  </div>
 <input id="regex_input" value="" class="form-control" placeholder="regex" style="" />
 <div class="input-group-append"><span class="input-group-text">/gi</span>
 </div>
</div>
<br />
チェック値: <textarea style="" placeholder="match string" id="regex_text"></textarea><br /><br />
​
一致結果<span id="reg_count"></span>: <div id="regex_results"></div>
</div>
<style type="text/css">
#regex_text {
  -moz-appearance: textfield-multiline;
  -webkit-appearance: textarea;
  border: 1px solid #ced4da !important;
  overflow: auto;
  padding: 2px;
  resize: both;
  white-space: pre-wrap;
  width:100%;
  height: 250px;
  padding: 5px 15px 5px 1.2em;
  border-radius: 0.25rem;
}
#regex_input {
  border: 1px solid #ced4da !important;
  padding: 0 15px 0 5px;
}
#regex_input.invalid {
  background-color: #f8eef7;
}
.regex_highlight {
  background-color: #66d4b333;
}
#regex_results {
  width: 100%;
  min-height: 2em;
  padding: 5px 15px 5px 0.2em;
}
</style>
<script type="text/javascript">
$( document ).ready(function() {
  function update_inputmatch() {
    var regexInput = $('#regex_input').val();
    var validreg = true;
    $('#regex_input').removeClass('invalid');
    try {
      var regex = new RegExp(regexInput,'gi');
      $('#regex_results').html('');
    } catch(e) {
      $('#regex_input').addClass('invalid');
      validreg = false;
      $('#regex_results').html('Invalid Regular Expression').prepend('&nbsp;&nbsp;&nbsp;');
    }
    if (validreg){
      if ($('#regex_text').val() ) {
        if (regexInput) {
          var input_str = $('#regex_text').val().split(/\r?\n/);
          var input_replaced = [];
          var reg_count = 0;
          for (var i = 0; i < input_str.length; i++) {
            var inp_rep = ''
            var matched = input_str[i].match(regex);
            if (matched) {
              inp_rep = '<i class="far fa-check-square"></i> ';
              reg_count++;
            }
            else {
              inp_rep = '<i class="far fa-square"></i> ';
            }
            inp_rep += input_str[i].replace(regex,'<span class="regex_highlight">$&</span>');
            input_replaced.push(inp_rep)
          }
          if (reg_count) {
            $('#reg_count').html(' (' + reg_count + ')');
          }
          else {
            $('#reg_count').html('');
          }
          $('#regex_results').html(input_replaced.join('<br />'));
        }
      }
      else {
        $('#regex_results').html('');
      }
    }
  }
  $('#regex_input, #regex_text').keyup(function(k){
    update_inputmatch();
  });
});
</script>

{% endtab %}
{% endtabs %}

## よくある質問 {#frequently-asked-questions}

### `does not match regex` フィルターには空白値が含まれますか？ {#does-the-does-not-match-regex-filter-include-blank-values}

いいえ。値が空白の場合、そのユーザーは `does not match regex` フィルターに含まれません。

### 文字列カスタム属性に対して、複数の正確な値のいずれかに一致させる（OR ロジック）にはどうすればよいですか？ {#how-do-i-match-any-of-several-exact-values-or-logic-for-a-string-custom-attribute}

先頭アンカーと末尾アンカーを使った交互パターンを使用して、各値が正確に一致し、部分一致が発生しないようにします。たとえば、`gold`、`silver`、または `bronze` に正確に一致させるには次のようにします。

```
(^gold$)|(^silver$)|(^bronze$)
```

### セグメンテーション時に、受信トレイ固有のメールアドレスをフィルタリングするにはどうすればよいですか？ {#how-do-i-filter-for-inbox-specific-email-addresses-when-segmenting}

{% raw %}
メールアドレスフィルターを使用し、`matches regex` に設定します。次に、メールアドレス用の正規表現を参照します。

```
[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z.-]+
```

この正規表現は次の3つの部分に分けることができます。

- `[a-zA-Z0-9.+_-]+` は `@` 文字の前のメールアドレスの先頭部分です。「name@example.com」の「name」にあたります。
- `[a-zA-Z0-9.-]+` はドメインの最初の部分です。「name@example.com」の「example」にあたります。
- `[a-zA-Z.-]+` はドメインの最後の部分です。「name@example.com」の「com」にあたります。

{% endraw %}

### 特定のドメインに関連付けられたメールアドレスをフィルタリングするにはどうすればよいですか？ {#how-do-i-filter-for-email-addresses-associated-to-a-specific-domain}

たとえば、「@braze.com」で終わるメールをフィルタリングしたいとします。メールアドレスフィルターを使用し、`matches regex` に設定して、正規表現フィールドに「@braze.com」と入力します。他のメールドメインにも同様に適用できます。

![「@braze.com」の正規表現に一致するメールアドレスのフィルター。]({% image_buster /assets/img/regex/regeximg1.png %})

### x 以上 (≥) または x 以下 (≤) の値で数値文字列をフィルタリングするにはどうすればよいですか？ {#how-can-i-use-filter-number-strings-for-values-x-or-x}

x 以上 (≥) の値を検索する場合は、次の正規表現を使用します。

```
^([x-y]|\d{z,})$
```

ここで `x-y` は最初の桁の数値範囲（0-9）、`z` は x の桁数より1つ多い数です。たとえば、50以上の値に対する正規表現は `^([5-9][0-9]|\d{3,})$` となります。

x 以下 (≤) の値を検索する場合は、次の正規表現を使用します。

```
^([x-y]|[a-b])$
```

ここで `x-y` は最初の桁の数値範囲（0-9）、`a-b` は x の下限範囲です。たとえば、50以下の値に対する正規表現は `^([5-9][0-9]|[0-4][0-9])$` となります。

### 特定の文字列で始まるカスタム属性をフィルタリングするにはどうすればよいですか？ {#how-do-i-filter-custom-attributes-that-start-with-a-specific-string}

キャレット記号（`^`）を使用して文字列の先頭を示し、指定したいカスタム属性の名前を入力します。

たとえば、「San」で始まる都市に住むユーザーをターゲットにしたい場合、正規表現は `^San \w` になります。この正規表現を使用すると、San Francisco、San Diego、San Jose などの都市のユーザーを正常にターゲットにできます。

![「^San \w」の正規表現に一致する市区町村のフィルター。]({% image_buster /assets/img/regex/regeximg2.png %})

### 特定の電話番号をフィルタリングするにはどうすればよいですか？ {#how-do-i-filter-for-specific-phone-numbers}

正規表現を使用して電話番号をフィルタリングする前に、ユーザープロファイルに記録されている番号は、[ユーザーの電話番号]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers)で指定されているとおり、[E.164](https://en.wikipedia.org/wiki/E.164) 形式である必要があることを覚えておいてください。

米国の電話番号を検索する場合は、正規表現形式 `1?\d\d\d\d\d\d\d\d\d\d` を使用します。各 `\d` の繰り返しは指定したい数字です。最初の3桁は市外局番です。

同様に、英国の電話番号の形式は `^\+4\d\d\d\d\d\d\d\d\d\d\d` です。他の国の場合は、それぞれの国番号に続いて、残りの各桁に必要な数の `\d` を繰り返します。リトアニアの場合、国番号は「3」なので、正規表現は `^\+3\d\d\d\d\d\d\d\d\d\d` となります。

英国の携帯電話番号が先頭に `+` なしで `447` から始まる一般的な形式（たとえば `447123456789`）で保存されている場合は、次のように一致させることができます。

```
^447\d{9}$
```

たとえば、特定の市外局番「718」で電話番号をフィルタリングしたいとします。電話番号フィルターを使用し、`matches regex` に設定して、次の正規表現を入力します。

```
^1?718\d\d\d\d\d\d\d
```

![「^1?718\d\d\d\d\d\d\d」の正規表現に一致する電話番号のフィルター。]({% image_buster /assets/img/regex/regeximg3.png %})

### セグメントとカスタムイベントトリガープロパティでは、正規表現のマッチングはどのように異なりますか？ {#how-does-regex-matching-differ-between-segments-and-custom-event-trigger-properties}

セグメントフィルターは大文字小文字を区別しないマッチング（`/gi` 修飾子に相当）を自動的に適用します。カスタムイベントトリガープロパティとトリガーフィルターは大文字小文字を区別するマッチング（`/g` のみに相当）を使用します。

トリガープロパティで大文字小文字を区別しないマッチングが必要な場合は、パターンでインラインフラグを使用します。たとえば、`(?i)STOP(?-i)` を使用すると、`stop`、`STOP`、または `Stop` に一致させることができます。

その他の例については、[正規表現デバッガー](#regex-debugger)セクションのメモを参照してください。