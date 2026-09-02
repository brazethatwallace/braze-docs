---
nav_title: "정규표현식"
article_title: "정규표현식"
page_order: 8
description: "이 참조 문서에서는 정규표현식(regex)이 무엇인지, 사용을 시작하는 방법, 그리고 정규표현식을 검증하고 테스트할 수 있는 디버거 기능에 대해 다룹니다."
page_type: reference
tool:
  - Testing Tools


---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/regular-expression-basics-for-braze){: style="float:right;width:120px;border:0;" class="noimgborder"} 정규표현식 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomregular-expression-basics-for-braze-stylefloatrightwidth120pxborder0-classnoimgborder-regular-expressions}

> 정규표현식(일반적으로 regex라고 함)은 검색 패턴을 정의하는 문자 시퀀스입니다. 정규표현식을 사용하면 텍스트 그룹을 검증하고 찾기 및 바꾸기 작업을 수행할 수 있습니다. Braze에서는 정규표현식을 활용하여 세분화 및 타겟 오디언스를 위한 Campaign 필터링에서 보다 유연한 문자열 매칭 솔루션을 제공합니다.<br><br>이 페이지에서는 정규표현식(regex), 사용 방법, 자주 묻는 질문을 다루며, 정규표현식을 테스트할 수 있는 regex 디버거를 제공합니다.

<!--{% multi_lang_include video.html id="3h5Xbhl-TxE" align="right" %}-->

연결된 Braze 학습 과정에서는 정규표현식을 [Regex101](https://regex101.com/)에서 사용하고 테스트하는 방법을 보여줍니다. 또한 [자체 regex 테스터](#regex-debugger), 유용한 참조 페이지, regex Braze 학습 동영상에서 참조하는 샘플 데이터, 그리고 자주 묻는 질문도 제공합니다.

## 리소스 {#resources}

- [정규표현식 기초](https://learning.braze.com/regular-expression-basics-for-braze) Braze 학습 코스
- [정규식 치트 시트]({{site.baseurl}}/regex_cheat_sheet)
- [샘플 데이터 RTF]({% image_buster /assets/download_file/regex-dummy-data.rtf %})

## 정규식 디버거 {#regex-debugger}

{% alert important %}
이 도구는 참조용으로만 사용되며, 정규식이 Braze 플랫폼과 100% 일치한다고 보장하지 않습니다. Braze에서 세분화 및 필터에 사용되는 정규표현식은 자동으로 `/gi` 수정자를 추가합니다. [gi 수정자](https://w3schools.sinsixx.com/jsref/jsref_regexp_modifier_gi.asp.htm)는 문자열에서 정규표현식의 모든 일치 항목을 대소문자 구분 없이 검색하는 데 사용됩니다.
<br>
커스텀 이벤트 트리거 속성정보 및 트리거 필터에 사용되는 정규표현식은 `/g` 수정자(대소문자 구분, [g 수정자](https://www.w3schools.com/jsref/jsref_regexp_g.asp) 참조)를 사용하며, `/i` 수정자는 사용하지 않습니다. 커스텀 이벤트 트리거 속성정보 및 트리거 필터에서 대소문자를 구분하지 않으려면 `(?i)`를 대신 사용하세요. 예를 들어, `Matches regex (?i)STOP(?-i)`는 대소문자에 관계없이 "STOP"의 모든 사용을 포착합니다("stop", "please stop", "never stop sending me messages" 등).
{% endalert %}

{% tabs %}
{% tab 정규식 디버거 %}
<div>
이 양식을 사용하여 정규표현식의 기본 유효성 검사 및 테스트를 수행할 수 있습니다.
​
정규식:
​
<div class="input-group">
  <div class="input-group-prepend"><span class="input-group-text">/</span>
  </div>
 <input id="regex_input" value="" class="form-control" placeholder="regex" style="" />
 <div class="input-group-append"><span class="input-group-text">/gi</span>
 </div>
</div>
<br />
확인할 값: <textarea style="" placeholder="match string" id="regex_text"></textarea><br /><br />
​
일치 결과<span id="reg_count"></span>: <div id="regex_results"></div>
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

## 자주 묻는 질문 {#frequently-asked-questions}

### `does not match regex` 필터에 빈 값이 포함되나요? {#does-the-does-not-match-regex-filter-include-blank-values}

아니요. 값이 비어 있으면 해당 사용자는 `does not match regex` 필터에 포함되지 않습니다.

### 문자열 커스텀 속성에 대해 여러 정확한 값 중 하나와 일치시키려면(OR 로직) 어떻게 해야 하나요? {#how-do-i-match-any-of-several-exact-values-or-logic-for-a-string-custom-attribute}

시작 앵커와 끝 앵커를 사용한 교대(alternation)를 활용하면 각 값이 정확히 일치하며 부분 일치가 발생하지 않습니다. 예를 들어, `gold`, `silver`, 또는 `bronze`와 정확히 일치시키려면 다음과 같이 작성합니다:

```
(^gold$)|(^silver$)|(^bronze$)
```

### 세분화 시 받은편지함별 이메일 주소를 필터링하려면 어떻게 해야 하나요? {#how-do-i-filter-for-inbox-specific-email-addresses-when-segmenting}

{% raw %}
이메일 주소 필터를 사용하고 `matches regex`로 설정합니다. 그런 다음 이메일 주소에 대한 정규식을 참조합니다:

```
[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z.-]+
```

이 정규식은 다음 세 부분으로 나눌 수 있습니다:

- `[a-zA-Z0-9.+_-]+`는 `@` 문자 앞에 오는 이메일 주소의 시작 부분입니다. 예를 들어 "name@example.com"에서 "name" 부분입니다.
- `[a-zA-Z0-9.-]+`는 도메인의 첫 번째 부분입니다. 예를 들어 "name@example.com"에서 "example" 부분입니다.
- `[a-zA-Z.-]+`는 도메인의 마지막 부분입니다. 예를 들어 "name@example.com"에서 "com" 부분입니다.

{% endraw %}

### 특정 도메인에 연결된 이메일 주소를 필터링하려면 어떻게 해야 하나요? {#how-do-i-filter-for-email-addresses-associated-to-a-specific-domain}

"@braze.com"으로 끝나는 이메일을 필터링하고 싶다고 가정해 보겠습니다. 이메일 주소 필터를 사용하고 `matches regex`로 설정한 다음, 정규식 필드에 "@braze.com"을 입력합니다. 다른 이메일 도메인에도 동일하게 적용됩니다.

!["@braze.com" 정규식과 일치하는 이메일 주소 필터.]({% image_buster /assets/img/regex/regeximg1.png %})

### 숫자 문자열을 ≥ x 또는 ≤ x 값으로 필터링하려면 어떻게 해야 하나요? {#how-can-i-use-filter-number-strings-for-values-x-or-x}

x 이상(≥)의 값을 검색하려면 다음 정규식을 사용합니다:

```
^([x-y]|\d{z,})$
```

여기서 `x-y`는 첫 번째 자릿수의 숫자 범위(0-9)이고, `z`는 x의 자릿수보다 1 큰 값입니다. 예를 들어, 50 이상의 값에 대한 정규식은 `^([5-9][0-9]|\d{3,})$`입니다.

x 이하(≤)의 값을 검색하려면 다음 정규식을 사용합니다:

```
^([x-y]|[a-b])$
```

여기서 `x-y`는 첫 번째 자릿수의 숫자 범위(0-9)이고, `a-b`는 x의 하한 범위입니다. 예를 들어, 50 이하의 값에 대한 정규식은 `^([5-9][0-9]|[0-4][0-9])$`입니다.

### 특정 문자열로 시작하는 커스텀 속성을 필터링하려면 어떻게 해야 하나요? {#how-do-i-filter-custom-attributes-that-start-with-a-specific-string}

캐럿 기호(`^`)를 사용하여 문자열의 시작 부분을 지정한 다음, 지정하려는 커스텀 속성의 이름을 입력합니다.

예를 들어, "San"으로 시작하는 도시에 거주하는 사용자를 타겟팅하려면 정규식은 `^San \w`입니다. 이 정규식을 사용하면 San Francisco, San Diego, San Jose 등의 도시에 있는 사용자를 성공적으로 타겟팅할 수 있습니다.

!["^San \w" 정규식과 일치하는 구/군/시 필터.]({% image_buster /assets/img/regex/regeximg2.png %})

### 특정 전화번호를 필터링하려면 어떻게 해야 하나요? {#how-do-i-filter-for-specific-phone-numbers}

정규식을 사용하여 전화번호를 필터링하기 전에, 고객 프로필에 기록된 번호는 [사용자 전화번호]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers)에 명시된 대로 [E.164](https://en.wikipedia.org/wiki/E.164) 형식이어야 한다는 점을 기억하세요.

미국 전화번호를 검색한다고 가정하면, 정규식 형식 `1?\d\d\d\d\d\d\d\d\d\d`를 사용합니다. 여기서 각 `\d`는 지정하려는 숫자입니다. 처음 세 자리는 지역 코드입니다.

마찬가지로, 영국 전화번호의 형식은 `^\+4\d\d\d\d\d\d\d\d\d\d\d`입니다. 다른 국가의 경우 해당 국가 코드 뒤에 나머지 각 자릿수에 대한 필요한 수의 `\d` 반복을 추가합니다. 예를 들어 국가 코드가 "3"인 리투아니아의 경우, 정규식은 `^\+3\d\d\d\d\d\d\d\d\d\d`입니다.

영국 휴대전화 번호가 `447`로 시작하는 일반 형식으로 앞에 `+` 없이 저장되어 있는 경우(예: `447123456789`), 다음과 같이 매칭할 수 있습니다:

```
^447\d{9}$
```

예를 들어, 특정 지역 코드 "718"에 대해 전화번호로 사용자를 필터링하고 싶다고 가정해 보겠습니다. 전화번호 필터를 사용하고 `matches regex`로 설정한 다음, 다음 정규식을 입력합니다:

```
^1?718\d\d\d\d\d\d\d
```

!["^1?718\d\d\d\d\d\d\d" 정규식과 일치하는 전화번호 필터.]({% image_buster /assets/img/regex/regeximg3.png %})

### Segments와 커스텀 이벤트 트리거 속성정보 간에 정규식 매칭은 어떻게 다른가요? {#how-does-regex-matching-differ-between-segments-and-custom-event-trigger-properties}

Segment 필터는 자동으로 대소문자를 구분하지 않는 매칭을 적용합니다(`/gi` 수정자와 동일). 커스텀 이벤트 트리거 속성정보 및 트리거 필터는 대소문자를 구분하는 매칭을 사용합니다(`/g`만 해당).

트리거 속성정보에서 대소문자를 구분하지 않는 매칭이 필요한 경우, 패턴에 인라인 플래그를 사용합니다. 예를 들어 `(?i)STOP(?-i)`는 `stop`, `STOP`, 또는 `Stop`과 일치합니다.

더 많은 예시는 [정규식 디버거](#regex-debugger) 섹션의 참고 사항을 확인하세요.