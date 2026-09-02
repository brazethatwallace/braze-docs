---
nav_title: "Expresiones regulares"
article_title: "Expresiones regulares"
page_order: 8
description: "Este artículo de referencia cubre qué son las expresiones regulares (regex), cómo empezar a usarlas, y ofrece funcionalidad de depuración para validar y probar expresiones regulares."
page_type: reference
tool:
  - Testing Tools


---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/regular-expression-basics-for-braze){: style="float:right;width:120px;border:0;" class="noimgborder"} Expresiones regulares {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomregular-expression-basics-for-braze-stylefloatrightwidth120pxborder0-classnoimgborder-regular-expressions}

> Una expresión regular, conocida comúnmente como regex, es una secuencia de caracteres que define un patrón de búsqueda. Las expresiones regulares te permiten validar agrupaciones de texto y realizar acciones de buscar y reemplazar. En Braze, aprovechamos las expresiones regulares para ofrecerte una solución de coincidencia de cadenas más flexible en tu segmentación y filtrado de Campaign para tu audiencia objetivo.<br><br>Esta página cubre las expresiones regulares (regex), cómo usarlas, preguntas frecuentes, y proporciona un depurador de regex para probar expresiones regulares.

<!--{% multi_lang_include video.html id="3h5Xbhl-TxE" align="right" %}-->

En el curso de Braze Learning enlazado, te mostramos cómo se pueden usar y probar las expresiones regulares en [Regex101](https://regex101.com/). También ofrecemos un [probador de regex interno](#regex-debugger), una página de referencia útil, datos de ejemplo referenciados en el video de regex de Braze Learning, así como algunas preguntas frecuentes.

## Recursos {#resources}

- [Fundamentos de expresiones regulares](https://learning.braze.com/regular-expression-basics-for-braze) Curso de Braze Learning
- [Hoja de referencia de regex]({{site.baseurl}}/regex_cheat_sheet)
- [Datos de ejemplo RTF]({% image_buster /assets/download_file/regex-dummy-data.rtf %})

## Depurador de regex {#regex-debugger}

{% alert important %}
Esta herramienta está pensada solo como referencia y no garantiza que la regex coincida al 100% con la plataforma Braze. Las expresiones regulares en Braze para segmentación y filtros añaden automáticamente el modificador `/gi`. El [modificador gi](https://w3schools.sinsixx.com/jsref/jsref_regexp_modifier_gi.asp.htm) se usa para realizar una búsqueda sin distinción entre mayúsculas y minúsculas de todas las ocurrencias de una expresión regular en una cadena.
<br>
Las expresiones regulares para propiedades de desencadenamiento de eventos personalizados y filtros de desencadenamiento usan el modificador `/g` (con distinción entre mayúsculas y minúsculas, consulta el [modificador g](https://www.w3schools.com/jsref/jsref_regexp_g.asp)) y no usan el modificador `/i`. Para no distinguir entre mayúsculas y minúsculas en propiedades de desencadenamiento de eventos personalizados y filtros de desencadenamiento, usa `(?i)` en su lugar. Por ejemplo, `Matches regex (?i)STOP(?-i)` captura cualquier uso de "STOP" en cualquier combinación de mayúsculas y minúsculas (como "stop", "please stop" y "never stop sending me messages").
{% endalert %}

{% tabs %}
{% tab Depurador de regex %}
<div>
Este formulario permite la validación y prueba básica de expresiones regulares.
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
Valor(es) a comprobar: <textarea style="" placeholder="cadena de coincidencia" id="regex_text"></textarea><br /><br />
​
Resultados de coincidencia<span id="reg_count"></span>: <div id="regex_results"></div>
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

## Preguntas frecuentes {#frequently-asked-questions}

### ¿El filtro `does not match regex` incluye valores en blanco? {#does-the-does-not-match-regex-filter-include-blank-values}

No. Si el valor está en blanco, el usuario no se incluirá en el filtro `does not match regex`.

### ¿Cómo puedo coincidir con varios valores exactos (lógica OR) para un atributo personalizado de cadena? {#how-do-i-match-any-of-several-exact-values-or-logic-for-a-string-custom-attribute}

Usa la alternancia con anclas de inicio y fin para que cada valor coincida exactamente y no captures coincidencias parciales. Por ejemplo, para coincidir exactamente con `gold`, `silver` o `bronze`:

```
(^gold$)|(^silver$)|(^bronze$)
```

### ¿Cómo filtro direcciones de correo electrónico específicas del buzón de entrada al segmentar? {#how-do-i-filter-for-inbox-specific-email-addresses-when-segmenting}

{% raw %}
Usa el filtro de dirección de correo electrónico, configúralo como `matches regex`. Luego haz referencia a la regex para direcciones de correo electrónico:

```
[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z.-]+
```

Podemos dividir esta regex en las siguientes tres partes:

- `[a-zA-Z0-9.+_-]+` es el comienzo de la dirección de correo electrónico antes del carácter arroba `@`. Es decir, el "name" en "name@example.com".
- `[a-zA-Z0-9.-]+` es la primera parte del dominio. Es decir, el "example" en "name@example.com".
- `[a-zA-Z.-]+` es la última parte del dominio. Es decir, el "com" en "name@example.com".

{% endraw %}

### ¿Cómo filtro direcciones de correo electrónico asociadas a un dominio específico? {#how-do-i-filter-for-email-addresses-associated-to-a-specific-domain}

Supongamos que quieres filtrar correos electrónicos que terminen con "@braze.com". Usarías el filtro de dirección de correo electrónico, lo configurarías como `matches regex` e ingresarías "@braze.com" en el campo de regex. Lo mismo aplica para cualquier otro dominio de correo electrónico.

![Filtro para una dirección de correo electrónico que coincide con la regex "@braze.com".]({% image_buster /assets/img/regex/regeximg1.png %})

### ¿Cómo puedo usar cadenas de números de filtro para valores ≥ x o ≤ x? {#how-can-i-use-filter-number-strings-for-values-x-or-x}

Si buscas valores mayores o iguales (≥) a x, usa la siguiente regex:

```
^([x-y]|\d{z,})$
```

Donde `x-y` es el rango de números (0-9) del primer dígito, y `z` es uno más que la cantidad de dígitos de x. Por ejemplo, para valores mayores o iguales a 50, la regex sería `^([5-9][0-9]|\d{3,})$`.

Si buscas valores menores o iguales (≤) a x, usa la siguiente regex:

```
^([x-y]|[a-b])$
```

Donde `x-y` es el rango de números (0-9) del primer dígito, y `a-b` es el rango del límite inferior de x. Por ejemplo, para valores menores o iguales a 50, la regex sería `^([5-9][0-9]|[0-4][0-9])$`.

### ¿Cómo filtro atributos personalizados que comienzan con una cadena específica? {#how-do-i-filter-custom-attributes-that-start-with-a-specific-string}

Usa el símbolo de intercalación (`^`) para indicar con qué comienza la cadena, y luego ingresa el nombre del atributo personalizado que deseas especificar.

Por ejemplo, si intentas dirigirte a usuarios que viven en ciudades que comienzan con "San", tu regex sería `^San \w`. Con esta regex, podrías dirigirte exitosamente a usuarios de ciudades como San Francisco, San Diego, San José, etc.

![Filtro para una ciudad que coincide con la regex "^San \w".]({% image_buster /assets/img/regex/regeximg2.png %})

### ¿Cómo filtro números de teléfono específicos? {#how-do-i-filter-for-specific-phone-numbers}

Antes de usar regex para filtrar números de teléfono, recuerda que los números registrados en los perfiles de usuario deben estar en formato [E.164](https://en.wikipedia.org/wiki/E.164), como se especifica en [Números de teléfono de usuario]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers).

Suponiendo que buscas números de teléfono de EE. UU., usa el formato de regex `1?\d\d\d\d\d\d\d\d\d\d`, donde cada repetición de `\d` es un dígito que deseas especificar. Los primeros tres dígitos son el código de área.

De igual manera, el formato para números de teléfono del Reino Unido es `^\+4\d\d\d\d\d\d\d\d\d\d\d`. Cualquier otro país sería el código de país correspondiente, seguido del número necesario de repeticiones de `\d` para cada dígito restante. Así, en el caso de Lituania con un código de país "3", su regex sería `^\+3\d\d\d\d\d\d\d\d\d\d`.

Si tus números móviles del Reino Unido están almacenados sin un `+` inicial en el formato común que comienza con `447` (por ejemplo, `447123456789`), puedes coincidir con ellos usando:

```
^447\d{9}$
```

Por ejemplo, supongamos que quisieras filtrar usuarios por número de teléfono para un código de área específico, "718". Usa el filtro de número de teléfono, configúralo como `matches regex` e ingresa la siguiente regex:

```
^1?718\d\d\d\d\d\d\d
```

![Filtro para un número de teléfono que coincide con la regex "^1?718\d\d\d\d\d\d\d".]({% image_buster /assets/img/regex/regeximg3.png %})

### ¿En qué se diferencia la coincidencia con regex entre Segments y las propiedades de activación de eventos personalizados? {#how-does-regex-matching-differ-between-segments-and-custom-event-trigger-properties}

Los filtros de Segment aplican automáticamente la coincidencia sin distinción entre mayúsculas y minúsculas (equivalente al modificador `/gi`). Las propiedades de activación de eventos personalizados y los filtros de activación usan coincidencia con distinción entre mayúsculas y minúsculas (equivalente solo a `/g`).

Si necesitas coincidencia sin distinción entre mayúsculas y minúsculas en una propiedad de activación, usa indicadores en línea en tu patrón; por ejemplo, `(?i)STOP(?-i)` para coincidir con `stop`, `STOP` o `Stop`.

Para más ejemplos, consulta la nota en la sección [Depurador de regex](#regex-debugger).