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
- [Regex-Spickzettel]({{site.baseurl}}/regex_cheat_sheet)
- [Beispieldaten-RTF]({% image_buster /assets/download_file/regex-dummy-data.rtf %})

## Regex-Debugger {#regex-debugger}

{% alert important %}
Dieses Tool dient nur als Referenz und garantiert nicht, dass der reguläre Ausdruck zu 100 % mit der Braze-Plattform übereinstimmt. Reguläre Ausdrücke in Braze für Segmentierung und Filter fügen automatisch den `/gi`-Modifikator hinzu. Der [gi-Modifikator](https://w3schools.sinsixx.com/jsref/jsref_regexp_modifier_gi.asp.htm) wird verwendet, um eine Suche ohne Berücksichtigung der Groß-/Kleinschreibung nach allen Vorkommen eines regulären Ausdrucks in einem String durchzuführen.
<br>
Reguläre Ausdrücke für Eigenschaften von angepassten Event-Triggern und Trigger-Filter verwenden den `/g`-Modifikator (Groß-/Kleinschreibung wird berücksichtigt, siehe [g-Modifikator](https://www.w3schools.com/jsref/jsref_regexp_g.asp)) und verwenden nicht den `/i`-Modifikator. Für die Nichtberücksichtigung der Groß-/Kleinschreibung bei Eigenschaften von angepassten Event-Triggern und Trigger-Filtern verwenden Sie stattdessen `(?i)`. Zum Beispiel erfasst `Matches regex (?i)STOP(?-i)` jede Verwendung von „STOP“ in beliebiger Schreibweise (wie „stop“, „please stop“ und „never stop sending me messages“).
{% endalert %}

{% tabs %}
{% tab Regex-Debugger %}
<div>
Dieses Formular ermöglicht eine grundlegende Validierung und das Testen von regulären Ausdrücken.
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
Wert(e) prüfen: <textarea style="" placeholder="match string" id="regex_text"></textarea><br /><br />
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

Nein. Wenn der Wert leer ist, werden Nutzer:innen nicht in den Filter `does not match regex` einbezogen.

### Wie kann ich mehrere exakte Werte (ODER-Logik) für ein angepasstes String-Attribut abgleichen? {#how-do-i-match-any-of-several-exact-values-or-logic-for-a-string-custom-attribute}

Verwenden Sie Alternation mit Start- und Endankern, damit jeder Wert exakt übereinstimmt und keine Teilübereinstimmungen erfasst werden. Um zum Beispiel exakt `gold`, `silver` oder `bronze` abzugleichen:

```
(^gold$)|(^silver$)|(^bronze$)
```

### Wie filtere ich bei der Segmentierung nach Posteingangs-spezifischen E-Mail-Adressen? {#how-do-i-filter-for-inbox-specific-email-addresses-when-segmenting}

{% raw %}
Verwenden Sie den E-Mail-Adress-Filter und setzen Sie ihn auf `matches regex`. Verwenden Sie dann den regulären Ausdruck für E-Mail-Adressen:

```
[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z.-]+
```

Dieser Regex lässt sich in die folgenden drei Teile aufgliedern:

- `[a-zA-Z0-9.+_-]+` ist der Anfang der E-Mail-Adresse vor dem At-Zeichen `@`. Also der „Name“ in „name@example.com“.
- `[a-zA-Z0-9.-]+` ist der erste Teil der Domain. Also „example“ in „name@example.com“.
- `[a-zA-Z.-]+` ist der letzte Teil der Domain. Also „com“ in „name@example.com“.

{% endraw %}

### Wie filtere ich nach E-Mail-Adressen, die zu einer bestimmten Domain gehören? {#how-do-i-filter-for-email-addresses-associated-to-a-specific-domain}

Angenommen, Sie möchten nach E-Mails filtern, die auf „@braze.com“ enden. Verwenden Sie den E-Mail-Adress-Filter, setzen Sie ihn auf `matches regex` und geben Sie „@braze.com“ in das Regex-Feld ein. Das Gleiche gilt für jede andere E-Mail-Domain.

![Filter für eine E-Mail-Adresse, die dem Regex „@braze.com“ entspricht.]({% image_buster /assets/img/regex/regeximg1.png %})

### Wie kann ich Zahlenstrings nach Werten ≥ x oder ≤ x filtern? {#how-can-i-use-filter-number-strings-for-values-x-or-x}

Wenn Sie nach Werten suchen, die größer oder gleich (≥) x sind, verwenden Sie den folgenden Regex:

```
^([x-y]|\d{z,})$
```

Dabei ist `x-y` der Zahlenbereich (0–9) der ersten Ziffer und `z` die Anzahl der Ziffern von x plus eins. Für Werte größer oder gleich 50 wäre der Regex demnach `^([5-9][0-9]|\d{3,})$`.

Wenn Sie nach Werten suchen, die kleiner oder gleich (≤) x sind, verwenden Sie den folgenden Regex:

```
^([x-y]|[a-b])$
```

Dabei ist `x-y` der Zahlenbereich (0–9) der ersten Ziffer und `a-b` der untere Bereich von x. Für Werte kleiner oder gleich 50 wäre der Regex demnach `^([5-9][0-9]|[0-4][0-9])$`.

### Wie filtere ich angepasste Attribute, die mit einem bestimmten String beginnen? {#how-do-i-filter-custom-attributes-that-start-with-a-specific-string}

Verwenden Sie das Caret-Symbol (`^`), um anzugeben, womit der String beginnt, und geben Sie dann den Namen des angepassten Attributs ein, das Sie angeben möchten.

Wenn Sie beispielsweise Nutzer:innen ansprechen möchten, die in Städten leben, die mit „San“ beginnen, wäre Ihr Regex `^San \w`. Mit diesem Regex würden Sie erfolgreich Nutzer:innen aus Städten wie San Francisco, San Diego, San Jose usw. ansprechen.

![Filter für einen Ort, der dem Regex „^San \w“ entspricht.]({% image_buster /assets/img/regex/regeximg2.png %})

### Wie filtere ich nach bestimmten Telefonnummern? {#how-do-i-filter-for-specific-phone-numbers}

Bevor Sie Regex zum Filtern von Telefonnummern verwenden, beachten Sie, dass Telefonnummern, die für Nutzerprofile hinterlegt sind, im [E.164](https://en.wikipedia.org/wiki/E.164)-Format vorliegen müssen, wie unter [Nutzer-Telefonnummern]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers) angegeben.

Wenn Sie nach US-Telefonnummern suchen, verwenden Sie das Regex-Format `1?\d\d\d\d\d\d\d\d\d\d`, wobei jede Wiederholung von `\d` eine Ziffer ist, die Sie angeben möchten. Die ersten drei Ziffern sind die Vorwahl.

Ebenso ist das Format für britische Telefonnummern `^\+4\d\d\d\d\d\d\d\d\d\d\d`. Für jedes andere Land wird die jeweilige Landesvorwahl gefolgt von der erforderlichen Anzahl an `\d`-Wiederholungen für jede verbleibende Ziffer verwendet. Im Fall von Litauen mit der Landesvorwahl „3“ wäre der Regex also `^\+3\d\d\d\d\d\d\d\d\d\d`.

Wenn Ihre britischen Mobilnummern ohne führendes `+` im gängigen Format gespeichert sind und mit `447` beginnen (zum Beispiel `447123456789`), können Sie sie mit folgendem Ausdruck abgleichen:

```
^447\d{9}$
```

Angenommen, Sie möchten Nutzer:innen nach Telefonnummer für eine bestimmte Vorwahl, „718“, filtern. Verwenden Sie den Telefonnummer-Filter, setzen Sie ihn auf `matches regex` und geben Sie den folgenden Regex ein:

```
^1?718\d\d\d\d\d\d\d
```

![Filter für eine Telefonnummer, die dem Regex „^1?718\d\d\d\d\d\d\d“ entspricht.]({% image_buster /assets/img/regex/regeximg3.png %})

### Wie unterscheidet sich der Regex-Abgleich zwischen Segmenten und benutzerdefinierten Event-Trigger-Eigenschaften? {#how-does-regex-matching-differ-between-segments-and-custom-event-trigger-properties}

Segment-Filter wenden automatisch einen Abgleich ohne Berücksichtigung der Groß-/Kleinschreibung an (entspricht dem `/gi`-Modifikator). Benutzerdefinierte Event-Trigger-Eigenschaften und Trigger-Filter verwenden einen Abgleich mit Berücksichtigung der Groß-/Kleinschreibung (entspricht nur `/g`).

Wenn Sie bei einer Trigger-Eigenschaft einen Abgleich ohne Berücksichtigung der Groß-/Kleinschreibung benötigen, verwenden Sie Inline-Flags in Ihrem Muster – zum Beispiel `(?i)STOP(?-i)`, um `stop`, `STOP` oder `Stop` abzugleichen.

Weitere Beispiele finden Sie im Hinweis im Abschnitt [Regex-Debugger](#regex-debugger).