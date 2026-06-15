---
nav_title: Regex-Referenzblatt
permalink: /regex_cheat_sheet/
hidden: true
---

# Regex-Referenzblatt {#regex-reference-sheet}

Diese Seite dient als Kurzanleitung für reguläre Ausdrücke, einschließlich häufiger Token, Metasequenzen, allgemeiner Token, Gruppenkonstanten und mehr.

{% tabs %}
{% tab Common tokens %}

| Häufige Token |
| ------------- |
| Ein einzelnes Zeichen aus: a, b oder c | `[abc]` |
| Ein Zeichen außer: a, b oder c | `[^abc]` |
| Ein Zeichen im Bereich: a–z | `[a-z]` |
| Ein Zeichen nicht im Bereich: a–z | `[^a-z]` |
| Ein Zeichen im Bereich: a–z oder A–Z | `[a-zA-Z]` |
| Jedes einzelne Zeichen | `.` |
| Jedes Whitespace-Zeichen | `\s` |
| Jedes Nicht-Whitespace-Zeichen | `\S` |
| Jede Ziffer | `\d` |
| Jede Nicht-Ziffer | `\D` |
| Jedes Wortzeichen | `\w` |
| Jedes Nicht-Wort-Zeichen | `\W` |
| Klammerinhalt erfassen | `(...)` |
| Entspricht entweder a oder b | `(a|b)` |
| Null oder eins von a | `a?` |
| Null oder mehr von a | `a*` |
| Eins oder mehr von a | `a+` |
| Genau 3 von a | `a{3}` |
| Zwischen 3 und 6 von a | `a{3,6}` |
| Anfang der Zeichenkette | `^` |
| Ende der Zeichenkette | `$` |
| Wortgrenze | `\n` |
| Keine Wortgrenze | `\B` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% tab Meta sequence %}

| Metasequenz |
| ------------- |
| Beliebige Unicode-Sequenzen, einschließlich Zeilenumbrüche | `\X` |
| Eine Dateneinheit abgleichen | `\C` |
| Unicode-Zeilenumbrüche | `\R` |
| Vertikales Whitespace-Zeichen | `\v` |
| Negation von \v | `\V` |
| Horizontales Whitespace-Zeichen | `\h` |
| Negation von \h | `\H` |
| Übereinstimmung zurücksetzen | `\K` |
| n-tes Teilmuster abgleichen | `\n` |
| Unicode-Eigenschaft X | `\pX` |
| Negation von \pX | `\PX` |
| Unicode-Eigenschaft oder Skript-Kategorie | `\p{...}` |
| Negation von \p | `\P{...}` |
| Zitat; als Literale behandeln | `\Q...|E` |
| Teilmuster „name“ abgleichen | `\k<name>` |
| Teilmuster „name“ abgleichen | `\k'name'` |
| Teilmuster „name“ abgleichen | `\k{name}` |
| n-tes Teilmuster abgleichen | `\gn` |
| n-tes Teilmuster abgleichen | `\g{n}` |
| Rekurs auf n-te Erfassungsgruppe | `\g<n>` |
| Rekurs auf n-te Erfassungsgruppe | `\g'n'` |
| n-tes relatives vorheriges Teilmuster abgleichen | `\g{-n}` |
| Rekurs auf n-tes relatives nachfolgendes Teilmuster | `\g<+n>` |
| n-tes relatives nachfolgendes Teilmuster abgleichen | `\g'+n'` |
| Rekursive benannte Erfassungsgruppe | `'letter'` |
| Zuvor benannte Erfassungsgruppe „letter“ abgleichen | `\g{letter}` |
| Rekurs auf benannte Erfassungsgruppe „letter“ | `\g<letter>` |
| Hex-Zeichen YY | `\xYY` |
| Hex-Zeichen YYYY | `\x{YYYY}` |
| Oktalzeichen ddd | `\ddd` |
| Steuerzeichen Y | `\cY` |
| Backspace-Zeichen | `[\b]` |
| Macht jedes Zeichen literal | `\` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% tab General tokens %}

| Allgemeine Token |
| -------------- |
| Zeilenumbruch | `\n` |
| Wagenrücklauf | `\r` |
| Tab | `\t` |
| Nullzeichen | `\0` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }

{% endtab %}
{% tab Character class modifiers %}

| Zeichenklassen-Modifikatoren |
| ------------------------- |
| Ein einzelnes Zeichen aus: a, b oder c | `[abc]` |
| Ein Zeichen außer\: a, b oder c | `[^abc]` |
| Ein Zeichen im Bereich: a–z | `[a-z]` |
| Ein Zeichen nicht im Bereich: a–z | `[^a-z]` |
| Ein Zeichen im Bereich: a–z oder A–Z | `[a-zA-Z]` |
| Buchstaben und Ziffern | `[:alnum:]` |
| Buchstaben | `[:alpha:]` |
| ASCII-Codes 0–127 | `[:ascii:]` |
| Nur Leerzeichen oder Tab | `[:blank:]` |
| Steuerzeichen | `[:cntrl:]` |
| Ziffern | `[:digit:]` |
| Sichtbare Zeichen (kein Leerzeichen) | `[:word:]` |
| Kleinbuchstaben | `[:xdigit:]` |
| Großbuchstaben | `[:<:]` |
| Wortzeichen | `[:>:]` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% tab Group constants %}

| Gruppenkonstanten |
| --------------- |
| Klammerinhalt erfassen | `(...)` |
| Entspricht entweder a oder b | `(a|b)` |
| Klammerinhalt abgleichen | `(?:...)` |
| Atomare Gruppierung (ohne Erfassung) | `(?>...)` |
| Teilmuster-Gruppennummer duplizieren | `(?|...)` |
| Kommentar | `(?#...)` |
| Groß-/Kleinschreibung ignorieren | `(?i)` |
| Benannte Erfassungsgruppe | `(?'name'...)` |
| Benannte Erfassungsgruppe | `(?<name>...)` |
| Benannte Erfassungsgruppe | `(?P<name>...)` |
| Inline-Modifikatoren | `(?imsxXU)` |
| Bedingte Anweisungen | `(?(1)yes|no)` |
| Rekursive bedingte Anweisungen | `(?(R#)yes|no)` |
| Bedingte Anweisung | `(?(R&name)yes|no)` |
| Bedingtes Lookahead | `(?(?=...)yes|no)` |
| Bedingtes Lookbehind | `(?(?<=...)yes|no)` |
| Rekurs auf gesamtes Muster | `(?R)` |
| Rekurs auf erstes Teilmuster | `(?1)` |
| Rekurs auf erstes relatives Teilmuster | `(?+1)` |
| Rekurs auf Teilmuster „name“ | `(?&name)` |
| Teilmuster „name“ abgleichen | `(?P=name)` |
| Rekurs auf Teilmuster „name“ | `(?P>name)` |
| Muster vor der Verwendung definieren | `(?(DEFINE)...)` |
| Positives Lookahead | `(?=...)` |
| Negatives Lookahead | `(?!...)` |
| Positives Lookbehind | `(?<=...)` |
| Negatives Lookbehind | `(?<!...)` |
| Steuerverb | `(*ACCEPT)` |
| Steuerverb | `(*FAIL)` |
| Steuerverb | `(*MARK:NAME)` |
| Steuerverb | `(*COMMIT)` |
| Steuerverb | `(*PRUNE)` |
| Steuerverb | `(*SKIP)` |
| Steuerverb | `(*THEN)` |
| Mustermodifikator | `(*UTF)` |
| Mustermodifikator | `(*UTF8)` |
| Mustermodifikator | `(*UTF16)` |
| Mustermodifikator | `(*UTF32)` |
| Mustermodifikator | `(*UCP)` |
| Zeilenumbruchmodifikator | `(*CR)` |
| Zeilenumbruchmodifikator | `(*LF)` |
| Zeilenumbruchmodifikator | `(*CRLF)` |
| Zeilenumbruchmodifikator | `(*ANYCRLF)` |
| Zeilenumbruchmodifikator | `(*ANY)` |
| Zeilenumbruchmodifikator | `\R` |
| Zeilenumbruchmodifikator | `(*BSR_ANYCRLF)` |
| Zeilenumbruchmodifikator | `(*BSR_UNICODE)` |
| Regex-Engine-Modifikator | `(*LIMIT_MATCH=x)` |
| Regex-Engine-Modifikator | `(*LIMIT_RECURSION=d)` |
| Regex-Engine-Modifikator | `(*NO_AUTO_POSSESS)` |
| Regex-Engine-Modifikator | `(*NO_START_OPT)` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% tab Quantifiers %}

| Quantoren |
| ----------- |
| Null oder eins von a | `a?` |
| Null oder mehr von a | `a*` |
| Eins oder mehr von a | `a+` |
| Genau 3 von a | `a{3}` |
| 3 oder mehr von a | `a{3,}` |
| Zwischen 3 und 6 von a | `a{3,6}` |
| Gieriger Quantor | `a*` |
| Fauler Quantor | `a*?` |
| Possessiver Quantor | `a*+` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% tab Anchors %}

| Anker |
| ------- |
| Match-Beginn | `\G` |
| Anfang der Zeichenkette | `^` |
| Ende der Zeichenkette | `$` |
| Anfang der Zeichenkette | `\A` |
| Ende der Zeichenkette | `\Z` |
| Absolutes Ende der Zeichenkette | `\z` |
| Wortgrenze | `\b` |
| Keine Wortgrenze | `\B` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}

{% tab Flags and modifiers %}

| Flags und Modifikatoren |
| ------------------- |
| Global | `g` |
| Mehrzeilig | `m` |
| Groß-/Kleinschreibung beachten | `l` |
| Whitespace ignorieren | `x` |
| Einzeilig | `s` |
| Unicode | `u` |
| Erweitert | `X` |
| Nicht gierig | `U` |
| Anker | `A` |
| Doppelte Gruppennamen | `J` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }

{% endtab %}
{% tab Substitution %}

| Substitution |
| ------------ |
| Vollständiger Match-Inhalt | `\0` |
| Inhalt der Erfassungsgruppe 1 | `\1 or $1` |
| Inhalt der Erfassungsgruppe `foo` | `${foo}` |
| Hexadezimale Ersatzwerte | `\x20, \x{06fa}` |
| Tab | `\t` |
| Wagenrücklauf | `\r` |
| Zeilenumbruch | `\n` |
| Seitenvorschub | `\f` |
| Umwandlung in Großbuchstaben | `\U` |
| Umwandlung in Kleinbuchstaben | `\L` |
| Beliebige Transformation beenden | `\E` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% endtabs %}