---
nav_title: Hoja de referencia regex
permalink: /regex_cheat_sheet/
hidden: true
---

# Hoja de referencia regex {#regex-reference-sheet}

Esta página sirve como guía de referencia rápida para expresiones regulares, incluyendo tokens comunes, metasecuencias, tokens generales, constantes de grupo y mucho más.

{% tabs %}
{% tab Common tokens %}

| Tokens comunes |
| ------------- |
| Un solo carácter de: a, b o c | `[abc]` |
| Un carácter excepto: a, b o c | `[^abc]` |
| Un carácter en el rango: a-z | `[a-z]` |
| Un carácter fuera del rango: a-z | `[^a-z]` |
| Un carácter en el rango: a-z o A-Z | `[a-zA-Z]` |
| Cualquier carácter individual | `.` |
| Cualquier carácter de espacio en blanco | `\s` |
| Cualquier carácter que no sea espacio en blanco | `\S` |
| Cualquier dígito | `\d` |
| Cualquier no dígito | `\D` |
| Cualquier carácter de palabra | `\w` |
| Cualquier carácter que no sea de palabra | `\W` |
| Captura lo encerrado | `(...)` |
| Coincide con a o b | `(a|b)` |
| Cero o uno de a | `a?` |
| Cero o más de a | `a*` |
| Uno o más de a | `a+` |
| Exactamente 3 de a | `a{3}` |
| Entre 3 y 6 de a | `a{3,6}` |
| Inicio de cadena | `^` |
| Fin de cadena | `$` |
| Límite de palabra | `\n` |
| Límite de no-palabra | `\B` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% tab Meta sequence %}

| Metasecuencia |
| ------------- |
| Cualquier secuencia Unicode, incluidos saltos de línea | `\X` |
| Coincide con una unidad de datos | `\C` |
| Nuevas líneas Unicode | `\R` |
| Carácter de espacio en blanco vertical | `\v` |
| Negación de \v | `\V` |
| Carácter de espacio en blanco horizontal | `\h` |
| Negación de \h | `\H` |
| Restablecer coincidencia | `\K` |
| Coincidir con el enésimo subpatrón | `\n` |
| propiedad Unicode X | `\pX` |
| Negación de \pX | `\PX` |
| propiedad Unicode o categoría de script | `\p{...}` |
| Negación de \p | `\P{...}` |
| Cita; tratar como literales | `\Q...|E` |
| Coincide con el subpatrón 'name' | `\k<name>` |
| Coincide con el subpatrón 'name' | `\k'name'` |
| Coincide con el subpatrón 'name' | `\k{name}` |
| Coincidir con el enésimo subpatrón | `\gn` |
| Coincidir con el enésimo subpatrón | `\g{n}` |
| Recurrir al enésimo grupo de captura | `\g<n>` |
| Recurrir al enésimo grupo de captura | `\g'n'` |
| Coincidir con el enésimo subpatrón anterior relativo | `\g{-n}` |
| Recurrir al enésimo subpatrón próximo relativo | `\g<+n>` |
| Coincidir con el enésimo remitente próximo relativo | `\g'+n'` |
| Grupo de captura con nombre recursivo | `'letter'` |
| Coincidir con el grupo de captura previamente nombrado 'letter' | `\g{letter}` |
| Recurrir al grupo de captura nombrado 'letter' | `\g<letter>` |
| Carácter hexadecimal YY | `\xYY` |
| Carácter hexadecimal YYYY | `\x{YYYY}` |
| Carácter octal ddd | `\ddd` |
| Carácter de control Y | `\cY` |
| Carácter de retroceso | `[\b]` |
| Hace literal cualquier carácter | `\` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% tab General tokens %}

| Tokens generales |
| -------------- |
| Nueva línea | `\n` |
| Retorno de carro | `\r` |
| Tabulación | `\t` |
| Carácter nulo | `\0` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }

{% endtab %}
{% tab Character class modifiers %}

| Modificadores de clase de carácter |
| ------------------------- |
| Un solo carácter de: a, b o c | `[abc]` |
| Un carácter excepto\: a, b o c | `[^abc]` |
| Un carácter en el rango: a-z | `[a-z]` |
| Un carácter fuera del rango: a-z | `[^a-z]` |
| Un carácter en el rango: a-z o A-Z | `[a-zA-Z]` |
| Letras y dígitos | `[:alnum:]` |
| Letras | `[:alpha:]` |
| Códigos ASCII 0-127 | `[:ascii:]` |
| Solo espacio o tabulación | `[:blank:]` |
| Caracteres de control | `[:cntrl:]` |
| Dígitos | `[:digit:]` |
| Caracteres visibles (no espacio) | `[:word:]` |
| Letras minúsculas | `[:xdigit:]` |
| Letras mayúsculas | `[:<:]` |
| Caracteres de palabra | `[:>:]` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% tab Group constants %}

| Constantes de grupo |
| --------------- |
| Captura todo lo encerrado | `(...)` |
| Coincide con a o b | `(a|b)` |
| Coincide con todo lo encerrado | `(?:...)` |
| Agrupación atómica (sin captura) | `(?>...)` |
| Número de grupo de subpatrón duplicado | `(?|...)` |
| Comentario | `(?#...)` |
| Para insensibilidad a mayúsculas y minúsculas | `(?i)` |
| Grupo de captura con nombre | `(?'name'...)` |
| Grupo de captura con nombre | `(?<name>...)` |
| Grupo de captura con nombre | `(?P<name>...)` |
| Modificadores en línea | `(?imsxXU)` |
| Sentencias condicionales | `(?(1)yes|no)` |
| Sentencias condicionales recursivas | `(?(R#)yes|no)` |
| Sentencia condicional | `(?(R&name)yes|no)` |
| Lookahead condicional | `(?(?=...)yes|no)` |
| Lookbehind condicional | `(?(?<=...)yes|no)` |
| Recurrir a todo el patrón | `(?R)` |
| Recurrir al primer subpatrón | `(?1)` |
| Recurrir al primer subpatrón relativo | `(?+1)` |
| Recurrir al subpatrón 'name' | `(?&name)` |
| Coincidir con el subpatrón 'name' | `(?P=name)` |
| Recurrir al subpatrón 'name' | `(?P>name)` |
| Predefinir patrones antes de usarlos | `(?(DEFINE)...)` |
| Lookahead positivo | `(?=...)` |
| Lookahead negativo | `(?!...)` |
| Lookbehind positivo | `(?<=...)` |
| Lookbehind negativo | `(?<!...)` |
| Verbo de control | `(*ACCEPT)` |
| Verbo de control | `(*FAIL)` |
| Verbo de control | `(*MARK:NAME)` |
| Verbo de control | `(*COMMIT)` |
| Verbo de control | `(*PRUNE)` |
| Verbo de control | `(*SKIP)` |
| Verbo de control | `(*THEN)` |
| Modificador de patrón | `(*UTF)` |
| Modificador de patrón | `(*UTF8)` |
| Modificador de patrón | `(*UTF16)` |
| Modificador de patrón | `(*UTF32)` |
| Modificador de patrón | `(*UCP)` |
| Modificador de salto de línea | `(*CR)` |
| Modificador de salto de línea | `(*LF)` |
| Modificador de salto de línea | `(*CRLF)` |
| Modificador de salto de línea | `(*ANYCRLF)` |
| Modificador de salto de línea | `(*ANY)` |
| Modificador de salto de línea | `\R` |
| Modificador de salto de línea | `(*BSR_ANYCRLF)` |
| Modificador de salto de línea | `(*BSR_UNICODE)` |
| Modificador del motor regex | `(*LIMIT_MATCH=x)` |
| Modificador del motor regex | `(*LIMIT_RECURSION=d)` |
| Modificador del motor regex | `(*NO_AUTO_POSSESS)` |
| Modificador del motor regex | `(*NO_START_OPT)` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% tab Quantifiers %}

| Cuantificadores |
| ----------- |
| Cero o uno de a | `a?` |
| Cero o más de a | `a*` |
| Uno o más de a | `a+` |
| Exactamente 3 de a | `a{3}` |
| 3 o más de a | `a{3,}` |
| Entre 3 y 6 de a | `a{3,6}` |
| Cuantificador codicioso | `a*` |
| Cuantificador perezoso | `a*?` |
| Cuantificador posesivo | `a*+` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% tab Anchors %}

| Anclas |
| ------- |
| Inicio de coincidencia | `\G` |
| Inicio de cadena | `^` |
| Fin de cadena | `$` |
| Inicio de cadena | `\A` |
| Fin de cadena | `\Z` |
| Fin absoluto de cadena | `\z` |
| Límite de palabra | `\b` |
| Límite de no-palabra | `\B` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}

{% tab Flags and modifiers %}

| Indicadores y modificadores |
| ------------------- |
| Global | `g` |
| Multilínea | `m` |
| Sensible a mayúsculas y minúsculas | `l` |
| Ignorar espacios en blanco | `x` |
| Línea única | `s` |
| Unicode | `u` |
| Extendido | `X` |
| No codicioso | `U` |
| Ancla | `A` |
| Nombres de grupo duplicados | `J` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }

{% endtab %}
{% tab Substitution %}

| Sustitución |
| ------------ |
| Contenido completo de la coincidencia | `\0` |
| Contenido del grupo de captura 1 | `\1 or $1` |
| Contenido del grupo de captura `foo` | `${foo}` |
| Valores de sustitución hexadecimales | `\x20, \x{06fa}` |
| Tabulación | `\t` |
| Retorno de carro | `\r` |
| Nueva línea | `\n` |
| Avance de página | `\f` |
| Transformación a mayúsculas | `\U` |
| Transformación a minúsculas | `\L` |
| Finalizar cualquier transformación | `\E` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% endtabs %}