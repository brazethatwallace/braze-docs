---
nav_title: Folha de referência de regex
permalink: /regex_cheat_sheet/
hidden: true
---

# Folha de referência de regex {#regex-reference-sheet}

Esta página serve como um guia de referência rápida para expressões regulares, incluindo tokens comuns, metassequências, tokens gerais, constantes de grupo e muito mais.

{% tabs %}
{% tab Common tokens %}

| Tokens comuns |
| ------------- |
| Um único caractere de: a, b ou c | `[abc]` |
| Um caractere, exceto: a, b ou c | `[^abc]` |
| Um caractere no intervalo: a-z | `[a-z]` |
| Um caractere fora do intervalo: a-z | `[^a-z]` |
| Um caractere no intervalo: a-z ou A-Z | `[a-zA-Z]` |
| Qualquer caractere único | `.` |
| Qualquer caractere de espaço em branco | `\s` |
| Qualquer caractere que não seja espaço em branco | `\S` |
| Qualquer dígito | `\d` |
| Qualquer não dígito | `\D` |
| Qualquer caractere de palavra | `\w` |
| Qualquer caractere que não seja de palavra | `\W` |
| Captura o conteúdo delimitado | `(...)` |
| Corresponde a a ou b | `(a|b)` |
| Zero ou um de a | `a?` |
| Zero ou mais de a | `a*` |
| Um ou mais de a | `a+` |
| Exatamente 3 de a | `a{3}` |
| Entre 3 e 6 de a | `a{3,6}` |
| Início da string | `^` |
| Fim da string | `$` |
| Um limite de palavra | `\n` |
| Limite de não palavra | `\B` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% tab Meta sequence %}

| Metassequência |
| ------------- |
| Quaisquer sequências Unicode, incluindo quebras de linha | `\X` |
| Corresponde a uma unidade de dados | `\C` |
| Novas linhas Unicode | `\R` |
| Caractere de espaço em branco vertical | `\v` |
| Negação de \v | `\V` |
| Caractere de espaço em branco horizontal | `\h` |
| Negação de \h | `\H` |
| Redefinir correspondência | `\K` |
| Corresponde ao enésimo subpadrão | `\n` |
| Propriedade Unicode X | `\pX` |
| Negação de \pX | `\PX` |
| Propriedade Unicode ou categoria de script | `\p{...}` |
| Negação de \p | `\P{...}` |
| Citar; tratar como literais | `\Q...|E` |
| Corresponde ao subpadrão 'name' | `\k<name>` |
| Corresponde ao subpadrão 'name' | `\k'name'` |
| Corresponde ao subpadrão 'name' | `\k{name}` |
| Corresponde ao enésimo subpadrão | `\gn` |
| Corresponde ao enésimo subpadrão | `\g{n}` |
| Recursão do enésimo grupo de captura | `\g<n>` |
| Recursão do enésimo grupo de captura | `\g'n'` |
| Corresponde ao enésimo subpadrão anterior relativo | `\g{-n}` |
| Recursão do enésimo subpadrão futuro relativo | `\g<+n>` |
| Corresponde ao enésimo submitter futuro relativo | `\g'+n'` |
| Grupo de captura de nomes recursivos | `'letter'` |
| Corresponde ao grupo de captura nomeado 'letter' | `\g{letter}` |
| Recursão do grupo de captura nomeado 'letter' | `\g<letter>` |
| Caractere hexadecimal YY | `\xYY` |
| Caractere hexadecimal YYYY | `\x{YYYY}` |
| Caractere octal ddd | `\ddd` |
| Caractere de controle Y | `\cY` |
| Caractere de backspace | `[\b]` |
| Torna qualquer caractere literal | `\` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% tab General tokens %}

| Tokens gerais |
| -------------- |
| Nova linha | `\n` |
| Retorno de carro | `\r` |
| Tabulação | `\t` |
| Caractere nulo | `\0` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }

{% endtab %}
{% tab Character class modifiers %}

| Modificadores de classe de caractere |
| ------------------------- |
| Um único caractere de: a, b ou c | `[abc]` |
| Um caractere, exceto\: a, b ou c | `[^abc]` |
| Um caractere no intervalo: a-z | `[a-z]` |
| Um caractere fora do intervalo: a-z | `[^a-z]` |
| Um caractere no intervalo: a-z ou A-Z | `[a-zA-Z]` |
| Letras e dígitos | `[:alnum:]` |
| Letras | `[:alpha:]` |
| Códigos ASCII 0-127 | `[:ascii:]` |
| Espaço ou tabulação apenas | `[:blank:]` |
| Caracteres de controle | `[:cntrl:]` |
| Dígitos | `[:digit:]` |
| Caracteres visíveis (sem espaço) | `[:word:]` |
| Letras minúsculas | `[:xdigit:]` |
| Letras maiúsculas | `[:<:]` |
| Caracteres de palavra | `[:>:]` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% tab Group constants %}

| Constantes de grupo |
| --------------- |
| Captura tudo o que estiver delimitado | `(...)` |
| Corresponde a a ou b | `(a|b)` |
| Corresponde a tudo o que estiver delimitado | `(?:...)` |
| Agrupamento atômico (sem captura) | `(?>...)` |
| Número de grupo de subpadrão duplicado | `(?|...)` |
| Comentário | `(?#...)` |
| Para insensibilidade a maiúsculas e minúsculas | `(?i)` |
| Grupo de captura nomeado | `(?'name'...)` |
| Grupo de captura nomeado | `(?<name>...)` |
| Grupo de captura nomeado | `(?P<name>...)` |
| Modificadores em linha | `(?imsxXU)` |
| Declarações condicionais | `(?(1)yes|no)` |
| Declarações condicionais recursivas | `(?(R#)yes|no)` |
| Declaração condicional | `(?(R&name)yes|no)` |
| Condicional de lookahead | `(?(?=...)yes|no)` |
| Condicional de lookbehind | `(?(?<=...)yes|no)` |
| Recursão de todo o padrão | `(?R)` |
| Recursão do primeiro subpadrão | `(?1)` |
| Recursão do primeiro subpadrão relativo | `(?+1)` |
| Recursão do subpadrão 'name' | `(?&name)` |
| Corresponde ao subpadrão 'name' | `(?P=name)` |
| Recursão do subpadrão 'name' | `(?P>name)` |
| Pré-definição de padrões antes do uso | `(?(DEFINE)...)` |
| Lookahead positivo | `(?=...)` |
| Lookahead negativo | `(?!...)` |
| Lookbehind positivo | `(?<=...)` |
| Lookbehind negativo | `(?<!...)` |
| Verbo de controle | `(*ACCEPT)` |
| Verbo de controle | `(*FAIL)` |
| Verbo de controle | `(*MARK:NAME)` |
| Verbo de controle | `(*COMMIT)` |
| Verbo de controle | `(*PRUNE)` |
| Verbo de controle | `(*SKIP)` |
| Verbo de controle | `(*THEN)` |
| Modificador de padrão | `(*UTF)` |
| Modificador de padrão | `(*UTF8)` |
| Modificador de padrão | `(*UTF16)` |
| Modificador de padrão | `(*UTF32)` |
| Modificador de padrão | `(*UCP)` |
| Modificador de quebra de linha | `(*CR)` |
| Modificador de quebra de linha | `(*LF)` |
| Modificador de quebra de linha | `(*CRLF)` |
| Modificador de quebra de linha | `(*ANYCRLF)` |
| Modificador de quebra de linha | `(*ANY)` |
| Modificador de quebra de linha | `\R` |
| Modificador de quebra de linha | `(*BSR_ANYCRLF)` |
| Modificador de quebra de linha | `(*BSR_UNICODE)` |
| Modificador de mecanismo regex | `(*LIMIT_MATCH=x)` |
| Modificador de mecanismo regex | `(*LIMIT_RECURSION=d)` |
| Modificador de mecanismo regex | `(*NO_AUTO_POSSESS)` |
| Modificador de mecanismo regex | `(*NO_START_OPT)` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% tab Quantifiers %}

| Quantificadores |
| ----------- |
| Zero ou um de a | `a?` |
| Zero ou mais de a | `a*` |
| Um ou mais de a | `a+` |
| Exatamente 3 de a | `a{3}` |
| 3 ou mais de a | `a{3,}` |
| Entre 3 e 6 de a | `a{3,6}` |
| Quantificador ganancioso | `a*` |
| Quantificador preguiçoso | `a*?` |
| Quantificador possessivo | `a*+` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% tab Anchors %}

| Âncoras |
| ------- |
| Início da correspondência | `\G` |
| Início da string | `^` |
| Fim da string | `$` |
| Início da string | `\A` |
| Fim da string | `\Z` |
| Fim absoluto da string | `\z` |
| Um limite de palavra | `\b` |
| Um limite de não palavra | `\B` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}

{% tab Flags and modifiers %}

| Sinalizadores e modificadores |
| ------------------- |
| Global | `g` |
| Multilinha | `m` |
| Diferencia maiúsculas de minúsculas | `l` |
| Ignorar espaços em branco | `x` |
| Linha única | `s` |
| Unicode | `u` |
| Estendido | `X` |
| Não ganancioso | `U` |
| Âncora | `A` |
| Nomes de grupos duplicados | `J` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }

{% endtab %}
{% tab Substitution %}

| Substituição |
| ------------ |
| Conteúdo completo da correspondência | `\0` |
| Conteúdo do grupo de captura 1 | `\1 or $1` |
| Conteúdo do grupo de captura `foo` | `${foo}` |
| Valores de substituição hexadecimais | `\x20, \x{06fa}` |
| Tabulação | `\t` |
| Retorno de carro | `\r` |
| Nova linha | `\n` |
| Form-feed | `\f` |
| Transformação para maiúsculas | `\U` |
| Transformação para minúsculas | `\L` |
| Encerrar qualquer transformação | `\E` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% endtabs %}