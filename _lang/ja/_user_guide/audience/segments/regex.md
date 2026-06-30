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

- [正規表現の基礎](https://learning.braze.com/regular-expression-basics-for-braze) Brazeラーニングコース
- [Regexチートシート]({{site.baseurl}}/regex_cheat_sheet)
- [サンプルデータRTF]({% image_buster /assets/download_file/regex-dummy-data.rtf %})

## Regexデバッガー {#regex-debugger}

{% alert important %}
このツールはあくまで参考用であり、Brazeプラットフォームでのregexマッチが100%一致することを保証するものではありません。Brazeのセグメンテーションおよびフィルターにおける正規表現は、自動的に`/gi`修飾子を追加します。[gi修飾子](https://w3schools.sinsixx.com/jsref/jsref_regexp_modifier_gi.asp.htm)は、文字列内の正規表現のすべての出現箇所を大文字小文字を区別せずに検索するために使用されます。
<br>
カスタムイベントのトリガープロパティおよびトリガーフィルターの正規表現は、`/g`修飾子（大文字小文字を区別、[g修飾子](https://www.w3schools.com/jsref/jsref_regexp_g.asp)を参照）を使用し、`/i`修飾子は使用しません。カスタムイベントのトリガープロパティおよびトリガーフィルターで大文字小文字を区別しない場合は、代わりに`(?i)`を使用してください。例えば、`Matches regex (?i)STOP(?-i)`は、「STOP」のあらゆる大文字小文字の組み合わせ（「stop」、「please stop」、「never stop sending me messages」など）をキャッチします。
{% endalert %}

{% tabs %}
{% tab Regex Debugger %}
<div>
このフォームでは、正規表現の基本的な検証とテストを行うことができます。
​
Regex:
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
マッチ結果<span id="reg_count"></span>: <div id="regex_results"></div>
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

### `does not match regex`フィルターには空白の値が含まれますか？ {#does-the-does-not-match-regex-filter-include-blank-values}

いいえ。値が空白の場合、そのユーザーは`does not match regex`フィルターに含まれません。

### 文字列カスタム属性に対して複数の正確な値のいずれかにマッチさせるにはどうすればよいですか（OR論理）？ {#how-do-i-match-any-of-several-exact-values-or-logic-for-a-string-custom-attribute}

交互パターンと開始・終了アンカーを使用して、各値が正確にマッチし、部分一致を拾わないようにします。例えば、`gold`、`silver`、または`bronze`に正確にマッチさせるには：

```
(^gold$)|(^silver$)|(^bronze$)
```

### セグメンテーション時に受信トレイ固有のメールアドレスをフィルタリングするにはどうすればよいですか？ {#how-do-i-filter-for-inbox-specific-email-addresses-when-segmenting}

{% raw %}
メールアドレスフィルターを使用し、`matches regex`に設定します。次に、メールアドレス用のregexを参照してください：

```
[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z.-]+
```

このregexは以下の3つの部分に分解できます：

- `[a-zA-Z0-9.+_-]+`は、`@`文字の前のメールアドレスの先頭部分です。つまり、「name@example.com」の「name」の部分です。
- `[a-zA-Z0-9.-]+`は、ドメインの最初の部分です。つまり、「name@example.com」の「example」の部分です。
- `[a-zA-Z.-]+`は、ドメインの最後の部分です。つまり、「name@example.com」の「com」の部分です。

{% endraw %}

### 特定のドメインに関連付けられたメールアドレスをフィルタリングするにはどうすればよいですか？ {#how-do-i-filter-for-email-addresses-associated-to-a-specific-domain}

例えば、「@braze.com」で終わるメールをフィルタリングしたい場合、メールアドレスフィルターを使用し、`matches regex`に設定して、regexフィールドに「@braze.com」と入力します。他のメールドメインについても同様です。

![「@braze.com」のregexに一致するメールアドレスのフィルター]({% image_buster /assets/img/regex/regeximg1.png %})

### 値が≥ xまたは≤ xの数値文字列をフィルタリングするにはどうすればよいですか？ {#how-can-i-use-filter-number-strings-for-values-x-or-x}

x以上（≥）の値を検索する場合は、以下のregexを使用します：

```
^([x-y]|\d{z,})$
```

ここで、`x-y`は最初の桁の数値範囲（0-9）、`z`はxの桁数より1つ多い数です。例えば、50以上の値の場合、regexは`^([5-9][0-9]|\d{3,})$`となります。

x以下（≤）の値を検索する場合は、以下のregexを使用します：

```
^([x-y]|[a-b])$
```

ここで、`x-y`は最初の桁の数値範囲（0-9）、`a-b`はxの下限範囲です。例えば、50以下の値の場合、regexは`^([5-9][0-9]|[0-4][0-9])$`となります。

### 特定の文字列で始まるカスタム属性をフィルタリングするにはどうすればよいですか？ {#how-do-i-filter-custom-attributes-that-start-with-a-specific-string}

キャレット記号（`^`）を使用して文字列の先頭を示し、指定したいカスタム属性の名前を入力します。

例えば、「San」で始まる都市に住むユーザーをターゲットにしたい場合、regexは`^San \w`となります。このregexを使用すると、San Francisco、San Diego、San Joseなどの都市のユーザーを正常にターゲットにできます。

![「^San \w」のregexに一致する市区町村のフィルター]({% image_buster /assets/img/regex/regeximg2.png %})

### 特定の電話番号をフィルタリングするにはどうすればよいですか？ {#how-do-i-filter-for-specific-phone-numbers}

regexを使用して電話番号をフィルタリングする前に、ユーザープロファイルに記録される番号は、[ユーザーの電話番号]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers)で指定されている[E.164](https://en.wikipedia.org/wiki/E.164)形式である必要があることを覚えておいてください。

米国の電話番号を検索する場合、regex形式は`1?\d\d\d\d\d\d\d\d\d\d`を使用します。ここで、`\d`の各繰り返しは指定したい桁を表します。最初の3桁は市外局番です。

同様に、英国の電話番号の形式は`^\+4\d\d\d\d\d\d\d\d\d\d\d`です。他の国の場合は、それぞれの国番号の後に、残りの各桁に必要な数の`\d`の繰り返しを続けます。例えば、国番号が「3」のリトアニアの場合、regexは`^\+3\d\d\d\d\d\d\d\d\d\d`となります。

英国のモバイル番号が先頭の`+`なしで`447`から始まる一般的な形式（例：`447123456789`）で保存されている場合、以下でマッチさせることができます：

```
^447\d{9}$
```

例えば、特定の市外局番「718」で電話番号をフィルタリングしたい場合、電話番号フィルターを使用し、`matches regex`に設定して、以下のregexを入力します：

```
^1?718\d\d\d\d\d\d\d
```

![「^1?718\d\d\d\d\d\d\d」のregexに一致する電話番号のフィルター]({% image_buster /assets/img/regex/regeximg3.png %})