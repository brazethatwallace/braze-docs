---
nav_title: "Reguläre Ausdrücke"
article_title: "Reguläre Ausdrücke"
page_order: 8
description: "Dieser Referenzartikel behandelt reguläre Ausdrücke (Regex), wie Sie diese verwenden können, und bietet eine Debugger-Funktionalität zum Validieren und Testen regulärer Ausdrücke."
page_type: reference
tool:
  - Testing Tools

---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/regular-expression-basics-for-braze){: style="float:right;width:120px;border:0;" class="noimgborder"} Reguläre Ausdrücke {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomregular-expression-basics-for-braze-stylefloatrightwidth120pxborder0-classnoimgborder-regular-expressions}

> Ein regulärer Ausdruck, allgemein als Regex bekannt, ist eine Zeichenfolge, die ein Suchmuster definiert. Reguläre Ausdrücke ermöglichen es Ihnen, Textgruppierungen zu validieren und Such- und Ersetzungsaktionen durchzuführen. Bei Braze nutzen wir reguläre Ausdrücke, um Ihnen eine flexiblere Lösung für den Zeichenkettenabgleich bei Ihrer Segmentierung und Campaign-Filterung für Ihre Zielgruppe zu bieten.<br><br>Diese Seite behandelt reguläre Ausdrücke (Regex), wie Sie diese verwenden können, häufig gestellte Fragen und bietet einen Regex-Debugger zum Testen regulärer Ausdrücke.

<!--{% multi_lang_include video.html id="3h5Xbhl-TxE" align="right" %}-->

Im verlinkten Braze-Lernkurs zeigen wir Ihnen, wie reguläre Ausdrücke auf [Regex101](https://regex101.com/) verwendet und getestet werden können. Wir bieten außerdem einen [internen Regex-Tester](#regex-debugger), eine hilfreiche Referenzseite, Beispieldaten, auf die im Regex-Braze-Lernvideo verwiesen wird, sowie einige häufig gestellte Fragen.

## Ressourcen {#resources}

- [Grundlagen regulärer Ausdrücke](https://learning.braze.com/regular-expression-basics-for-braze) Braze-Lernkurs
- [Regex-Spickzettel]({{site.baseurl}}/regex_cheat_sheet/)
- [Beispieldaten RTF]({% image_buster /assets/download_file/regex-dummy-data.rtf %})

## Regex-Debugger {#regex-debugger}

{% alert important %}
Dieses Tool dient nur als Referenz und garantiert nicht, dass der Regex zu 100 % mit der Braze-Plattform übereinstimmt. Reguläre Ausdrücke in Braze für Segmentierung und Filter fügen automatisch den `/gi`-Modifikator hinzu. Der [gi-Modifikator](https://w3schools.sinsixx.com/jsref/jsref_regexp_modifier_gi.asp.htm) wird verwendet, um eine Suche ohne Berücksichtigung der Groß-/Kleinschreibung nach allen Vorkommen eines regulären Ausdrucks in einem String durchzuführen.
<br>
Reguläre Ausdrücke für Eigenschaften von angepassten Event-Triggern und Trigger-Filter verwenden den `/g`-Modifikator (Groß-/Kleinschreibung wird berücksichtigt, siehe [g-Modifikator](https://www.w3schools.com/jsref/jsref_regexp_g.asp)) und verwenden nicht den `/i`-Modifikator. Für die Nichtberücksichtigung der Groß-/Kleinschreibung bei Eigenschaften von angepassten Event-Triggern und Trigger-Filtern verwenden Sie stattdessen `(?i)`. Zum Beispiel fängt `Matches regex (?i)STOP(?-i)` jede Verwendung von „STOP“ in beliebiger Schreibweise ab (wie „stop“, „please stop“ und „never stop sending me messages“).
{% endalert %}

{% tabs %}
{% tab Regex Debugger %}
<div>
Dieses Formular ermöglicht eine grundlegende Validierung und das Testen regulärer Ausdrücke.
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
Prüfwert(e): <textarea style="" placeholder="match string" id="regex_text"></textarea><br /><br />
​
Übereinstimmende Ergebnisse<span id="reg_count"></span>: <div id="regex_results"></div>
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

## Häufig gestellte Fragen {#frequently-asked-questions}

### Schließt der Filter `does not match regex` leere Werte ein? {#does-the-does-not-match-regex-filter-include-blank-values}

Nein. Wenn der Wert leer ist, werden die Nutzer:innen nicht in den Filter `does not match regex` einbezogen.

### Wie gleiche ich einen von mehreren exakten Werten (ODER-Logik) für ein angepasstes String-Attribut ab? {#how-do-i-match-any-of-several-exact-values-or-logic-for-a-string-custom-attribute}

Verwenden Sie Alternation mit Start- und Endankern, damit jeder Wert exakt übereinstimmt und Sie keine Teilübereinstimmungen erhalten. Um beispielsweise exakt `gold`, `silver` oder `bronze` abzugleichen:

```
(^gold$)|(^silver$)|(^bronze$)
```

### Wie filtere ich beim Segmentieren nach Posteingangs-spezifischen E-Mail-Adressen? {#how-do-i-filter-for-inbox-specific-email-addresses-when-segmenting}

{% raw %}
Verwenden Sie den E-Mail-Adressfilter und setzen Sie ihn auf `matches regex`. Referenzieren Sie dann den Regex für E-Mail-Adressen:

```
[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z.-]+
```

Wir können diesen Regex in die folgenden drei Teile aufgliedern:

- `[a-zA-Z0-9.+_-]+` ist der Anfang der E-Mail-Adresse vor dem At-Zeichen `@`. Also der „Name“ in „name@example.com“.
- `[a-zA-Z0-9.-]+` ist der erste Teil der Domain. Also „example“ in „name@example.com“.
- `[a-zA-Z.-]+` ist der letzte Teil der Domain. Also „com“ in „name@example.com“.

{% endraw %}

### Wie filtere ich nach E-Mail-Adressen, die mit einer bestimmten Domain verknüpft sind? {#how-do-i-filter-for-email-addresses-associated-to-a-specific-domain}

Angenommen, Sie möchten nach E-Mails filtern, die auf „@braze.com“ enden. Sie würden den E-Mail-Adressfilter verwenden, ihn auf `matches regex` setzen und „@braze.com“ in das Regex-Feld eingeben. Dasselbe gilt für jede andere E-Mail-Domain.

![Filter für eine E-Mail-Adresse, die dem Regex „@braze.com“ entspricht.]({% image_buster /assets/img/regex/regeximg1.png %})

### Wie kann ich Zahlen-Strings für Werte ≥ x oder ≤ x filtern? {#how-can-i-use-filter-number-strings-for-values-x-or-x}

Wenn Sie nach Werten suchen, die größer oder gleich (≥) x sind, verwenden Sie den folgenden Regex:

```
^([x-y]|\d{z,})$
```

Dabei ist `x-y` der Bereich der Zahlen (0–9) der ersten Ziffer und `z` ist eins mehr als die Anzahl der Ziffern von x. Zum Beispiel wäre der Regex für Werte größer oder gleich 50: `^([5-9][0-9]|\d{3,})$`.

Wenn Sie nach Werten suchen, die kleiner oder gleich (≤) x sind, verwenden Sie den folgenden Regex:

```
^([x-y]|[a-b])$
```

Dabei ist `x-y` der Bereich der Zahlen (0–9) der ersten Ziffer und `a-b` ist der untere Grenzbereich von x. Zum Beispiel wäre der Regex für Werte kleiner oder gleich 50: `^([5-9][0-9]|[0-4][0-9])$`.

### Wie filtere ich angepasste Attribute, die mit einem bestimmten String beginnen? {#how-do-i-filter-custom-attributes-that-start-with-a-specific-string}

Verwenden Sie das Caret-Symbol (`^`), um anzugeben, womit der String beginnt, und geben Sie dann den Namen des angepassten Attributs ein, das Sie angeben möchten.

Wenn Sie beispielsweise Nutzer:innen ansprechen möchten, die in Städten leben, die mit „San“ beginnen, wäre Ihr Regex `^San \w`. Mit diesem Regex würden Sie erfolgreich Nutzer:innen aus Städten wie San Francisco, San Diego, San Jose und so weiter ansprechen.

![Filter für einen Ort, der dem Regex „^San \w“ entspricht.]({% image_buster /assets/img/regex/regeximg2.png %})

### Wie filtere ich nach bestimmten Telefonnummern? {#how-do-i-filter-for-specific-phone-numbers}

Bevor Sie Regex zum Filtern von Telefonnummern verwenden, denken Sie daran, dass die für Nutzerprofile protokollierten Nummern im [E.164](https://en.wikipedia.org/wiki/E.164)-Format vorliegen müssen, wie in [Nutzer-Telefonnummern]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers/) angegeben.

Angenommen, Sie suchen nach US-Telefonnummern, verwenden Sie das Regex-Format `1?\d\d\d\d\d\d\d\d\d\d`, wobei jede Wiederholung von `\d` eine Ziffer ist, die Sie angeben möchten. Die ersten drei Ziffern sind die Vorwahl.

Ebenso ist das Format für britische Telefonnummern `^\+4\d\d\d\d\d\d\d\d\d\d\d`. Für jedes andere Land wäre es die jeweilige Landesvorwahl, gefolgt von der erforderlichen Anzahl von `\d`-Wiederholungen für jede verbleibende Ziffer. Im Fall von Litauen mit der Landesvorwahl „3“ wäre der Regex also `^\+3\d\d\d\d\d\d\d\d\d\d`.

Wenn Ihre britischen Mobilnummern ohne führendes `+` im gängigen Format mit `447` gespeichert sind (zum Beispiel `447123456789`), können Sie diese mit folgendem Ausdruck abgleichen:

```
^447\d{9}$
```

Angenommen, Sie möchten Nutzer:innen nach Telefonnummer für eine bestimmte Vorwahl, „718“, filtern. Verwenden Sie den Telefonnummernfilter, setzen Sie ihn auf `matches regex` und geben Sie den folgenden Regex ein:

```
^1?718\d\d\d\d\d\d\d
```

![Filter für eine Telefonnummer, die dem Regex „^1?718\d\d\d\d\d\d\d“ entspricht.]({% image_buster /assets/img/regex/regeximg3.png %})