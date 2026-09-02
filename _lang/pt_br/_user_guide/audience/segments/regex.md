---
nav_title: "Expressões regulares"
article_title: "Expressões regulares"
page_order: 8
description: "Este artigo de referência aborda o que são expressões regulares (regex), como começar a usá-las e oferece funcionalidade de depuração para validar e testar expressões regulares."
page_type: reference
tool:
  - Testing Tools


---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/regular-expression-basics-for-braze){: style="float:right;width:120px;border:0;" class="noimgborder"} Expressões regulares {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomregular-expression-basics-for-braze-stylefloatrightwidth120pxborder0-classnoimgborder-regular-expressions}

> Expressão regular, comumente conhecida como regex, é uma sequência de caracteres que define um padrão de busca. Expressões regulares permitem validar agrupamentos de texto e realizar ações de busca e substituição. Na Braze, utilizamos expressões regulares para oferecer uma solução mais flexível de correspondência de strings na segmentação e filtragem de campanhas para o seu público-alvo.<br><br>Esta página aborda expressões regulares (regex), como usá-las, perguntas frequentes e fornece um depurador de regex para testar expressões regulares.

<!--{% multi_lang_include video.html id="3h5Xbhl-TxE" align="right" %}-->

No curso do Braze Learning vinculado, mostramos como expressões regulares podem ser usadas e testadas no [Regex101](https://regex101.com/). Também oferecemos um [testador de regex interno](#regex-debugger), uma página de referência útil, dados de exemplo referenciados no vídeo de regex do Braze Learning, além de algumas perguntas frequentes.

## Recursos {#resources}

- Curso do Braze Learning [Noções básicas de expressão regular](https://learning.braze.com/regular-expression-basics-for-braze)
- [Cheat Sheet de Regex]({{site.baseurl}}/regex_cheat_sheet)
- [Dados de exemplo RTF]({% image_buster /assets/download_file/regex-dummy-data.rtf %})

## Depurador de regex {#regex-debugger}

{% alert important %}
Esta ferramenta serve apenas como referência e não garante que a regex corresponda 100% com a plataforma da Braze. As expressões regulares na Braze para segmentação e filtros adicionam automaticamente o modificador `/gi`. O [modificador gi](https://w3schools.sinsixx.com/jsref/jsref_regexp_modifier_gi.asp.htm) é usado para fazer uma busca que não diferencia maiúsculas de minúsculas em todas as ocorrências de uma expressão regular em uma string.
<br>
Expressões regulares para propriedades de disparo de eventos personalizados e filtros de disparo usam o modificador `/g` (diferencia maiúsculas de minúsculas, consulte o [modificador g](https://www.w3schools.com/jsref/jsref_regexp_g.asp)) e não usam o modificador `/i`. Para que não haja diferenciação entre maiúsculas e minúsculas em propriedades de disparo de eventos personalizados e filtros de disparo, use `(?i)`. Por exemplo, `Matches regex (?i)STOP(?-i)` captura qualquer uso de "STOP" em qualquer formato de caixa (como "stop", "please stop" e "never stop sending me messages").
{% endalert %}

{% tabs %}
{% tab Depurador de regex %}
<div>
Este formulário permite a validação e o teste básico de expressões regulares.
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
Verificar valor(es): <textarea style="" placeholder="string de correspondência" id="regex_text"></textarea><br /><br />
​
Resultados correspondentes<span id="reg_count"></span>: <div id="regex_results"></div>
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

## Perguntas frequentes {#frequently-asked-questions}

### O filtro `does not match regex` inclui valores em branco? {#does-the-does-not-match-regex-filter-include-blank-values}

Não. Se o valor estiver em branco, o usuário não será incluído no filtro `does not match regex`.

### Como faço para corresponder a qualquer um de vários valores exatos (lógica OR) para um atributo personalizado do tipo string? {#how-do-i-match-any-of-several-exact-values-or-logic-for-a-string-custom-attribute}

Use alternância com âncoras de início e fim para que cada valor corresponda exatamente e você não capture correspondências parciais. Por exemplo, para corresponder exatamente a `gold`, `silver` ou `bronze`:

```
(^gold$)|(^silver$)|(^bronze$)
```

### Como faço para filtrar endereços de e-mail específicos de uma caixa de entrada ao segmentar? {#how-do-i-filter-for-inbox-specific-email-addresses-when-segmenting}

{% raw %}
Use o filtro de endereço de e-mail e defina-o como `matches regex`. Em seguida, referencie o regex para endereços de e-mail:

```
[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z.-]+
```

Podemos dividir esse regex nas três partes a seguir:

- `[a-zA-Z0-9.+_-]+` é o início do endereço de e-mail antes do caractere arroba `@`. Ou seja, o "name" em "name@example.com".
- `[a-zA-Z0-9.-]+` é a primeira parte do domínio. Ou seja, o "example" em "name@example.com".
- `[a-zA-Z.-]+` é a última parte do domínio. Ou seja, o "com" em "name@example.com".

{% endraw %}

### Como faço para filtrar endereços de e-mail associados a um domínio específico? {#how-do-i-filter-for-email-addresses-associated-to-a-specific-domain}

Digamos que você queira filtrar e-mails que terminam com "@braze.com". Use o filtro de endereço de e-mail, defina-o como `matches regex` e insira "@braze.com" no campo de regex. O mesmo se aplica a qualquer outro domínio de e-mail.

![Filtro para um endereço de e-mail que corresponde ao regex "@braze.com".]({% image_buster /assets/img/regex/regeximg1.png %})

### Como posso usar filtros de strings numéricas para valores ≥ x ou ≤ x? {#how-can-i-use-filter-number-strings-for-values-x-or-x}

Se você está buscando valores maiores ou iguais a (≥) x, use o seguinte regex:

```
^([x-y]|\d{z,})$
```

Onde `x-y` é o intervalo de números (0-9) do primeiro dígito, e `z` é um a mais que o número de dígitos de x. Por exemplo, para valores maiores ou iguais a 50, o regex seria `^([5-9][0-9]|\d{3,})$`.

Se você está buscando valores menores ou iguais a (≤) x, use o seguinte regex:

```
^([x-y]|[a-b])$
```

Onde `x-y` é o intervalo de números (0-9) do primeiro dígito, e `a-b` é o intervalo inferior de x. Por exemplo, para valores menores ou iguais a 50, o regex seria `^([5-9][0-9]|[0-4][0-9])$`.

### Como faço para filtrar atributos personalizados que começam com uma string específica? {#how-do-i-filter-custom-attributes-that-start-with-a-specific-string}

Use o símbolo circunflexo (`^`) para indicar o início da string e insira o nome do atributo personalizado que deseja especificar.

Por exemplo, se você está tentando segmentar usuários que moram em cidades que começam com "San", seu regex seria `^San \w`. Com esse regex, você segmentaria com sucesso usuários de cidades como San Francisco, San Diego, San Jose, e assim por diante.

![Filtro para uma cidade que corresponde ao regex "^San \w".]({% image_buster /assets/img/regex/regeximg2.png %})

### Como faço para filtrar números de telefone específicos? {#how-do-i-filter-for-specific-phone-numbers}

Antes de usar regex para filtrar números de telefone, lembre-se de que os números registrados nos perfis de usuário devem estar no formato [E.164](https://en.wikipedia.org/wiki/E.164), conforme especificado em [Números de telefone do usuário]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers).

Supondo que você esteja buscando números de telefone dos EUA, use o formato de regex `1?\d\d\d\d\d\d\d\d\d\d`, onde cada repetição de `\d` é um dígito que você deseja especificar. Os três primeiros dígitos são o código de área.

Da mesma forma, o formato para números de telefone do Reino Unido é `^\+4\d\d\d\d\d\d\d\d\d\d\d`. Qualquer outro país seria o respectivo código do país, seguido pelo número necessário de repetições de `\d` para cada dígito restante. Então, no caso da Lituânia, com código de país "3", o regex seria `^\+3\d\d\d\d\d\d\d\d\d\d`.

Se seus números de celular do Reino Unido estiverem armazenados sem o `+` inicial, no formato comum começando com `447` (por exemplo, `447123456789`), você pode correspondê-los com:

```
^447\d{9}$
```

Por exemplo, digamos que você queira filtrar usuários por número de telefone para um código de área específico, "718". Use o filtro de número de telefone, defina-o como `matches regex` e insira o seguinte regex:

```
^1?718\d\d\d\d\d\d\d
```

![Filtro para um número de telefone que corresponde ao regex "^1?718\d\d\d\d\d\d\d".]({% image_buster /assets/img/regex/regeximg3.png %})

### Qual é a diferença da correspondência regex entre Segments e propriedades de disparo de eventos personalizados? {#how-does-regex-matching-differ-between-segments-and-custom-event-trigger-properties}

Os filtros de Segment or segmento aplicam automaticamente correspondência sem distinção entre maiúsculas e minúsculas (equivalente ao modificador `/gi`). As propriedades de disparo de eventos personalizados e os filtros de disparo usam correspondência com distinção entre maiúsculas e minúsculas (equivalente apenas ao `/g`).

Se você precisar de correspondência sem distinção entre maiúsculas e minúsculas em uma propriedade de disparo, use flags inline no seu padrão — por exemplo, `(?i)STOP(?-i)` para corresponder a `stop`, `STOP` ou `Stop`.

Para mais exemplos, consulte a nota na seção [Depurador de regex](#regex-debugger).