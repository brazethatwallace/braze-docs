---
nav_title: Fiche de référence des expressions régulières
permalink: /regex_cheat_sheet/
hidden: true
---

# Fiche de référence des expressions régulières {#regex-reference-sheet}

Cette page sert de guide de référence rapide pour les expressions régulières, y compris les jetons courants, les méta-séquences, les jetons généraux, les constantes de groupe, et plus encore.

{% tabs %}
{% tab Common tokens %}

| Jetons courants |
| ------------- |
| Un caractère unique parmi : a, b ou c | `[abc]` |
| Un caractère sauf : a, b ou c | `[^abc]` |
| Un caractère dans la plage : a-z | `[a-z]` |
| Un caractère hors de la plage : a-z | `[^a-z]` |
| Un caractère dans la plage : a-z ou A-Z | `[a-zA-Z]` |
| Tout caractère unique | `.` |
| Tout caractère d'espace blanc | `\s` |
| Tout caractère n'étant pas un espace blanc | `\S` |
| Tout chiffre | `\d` |
| Tout caractère autre qu'un chiffre | `\D` |
| Tout caractère de mot | `\w` |
| Tout caractère n'étant pas un mot | `\W` |
| Capture le contenu entre parenthèses | `(...)` |
| Fait correspondre a ou b | `(a|b)` |
| Zéro ou un a | `a?` |
| Zéro ou plusieurs a | `a*` |
| Un ou plusieurs a | `a+` |
| Exactement 3 a | `a{3}` |
| Entre 3 et 6 a | `a{3,6}` |
| Début de la chaîne de caractères | `^` |
| Fin de la chaîne de caractères | `$` |
| Une limite de mot | `\n` |
| Limite sans mot | `\B` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% tab Meta sequence %}

| Méta-séquence |
| ------------- |
| Toutes les séquences Unicode, sauts de ligne inclus | `\X` |
| Fait correspondre une unité de données | `\C` |
| Sauts de ligne Unicode | `\R` |
| Caractère d'espace blanc vertical | `\v` |
| Négation de \v | `\V` |
| Caractère d'espace blanc horizontal | `\h` |
| Négation de \h | `\H` |
| Réinitialiser la correspondance | `\K` |
| Fait correspondre le nième sous-motif | `\n` |
| Propriété Unicode X | `\pX` |
| Négation de \pX | `\PX` |
| Propriété Unicode ou catégorie de script | `\p{...}` |
| Négation de \p | `\P{...}` |
| Citation ; traiter comme des littéraux | `\Q...|E` |
| Fait correspondre le sous-motif « name » | `\k<name>` |
| Fait correspondre le sous-motif « name » | `\k'name'` |
| Fait correspondre le sous-motif « name » | `\k{name}` |
| Fait correspondre le nième sous-motif | `\gn` |
| Fait correspondre le nième sous-motif | `\g{n}` |
| Récurse le nième groupe de capture | `\g<n>` |
| Récurse le nième groupe de capture | `\g'n'` |
| Fait correspondre le nième sous-motif relatif précédent | `\g{-n}` |
| Récurse le nième sous-motif relatif suivant | `\g<+n>` |
| Fait correspondre le nième soumetteur relatif suivant | `\g'+n'` |
| Groupe de capture de noms récursif | `'letter'` |
| Fait correspondre le groupe de capture précédemment nommé « letter » | `\g{letter}` |
| Récurse le groupe de capture nommé « letter » | `\g<letter>` |
| Caractère hexadécimal YY | `\xYY` |
| Caractère hexadécimal YYYY | `\x{YYYY}` |
| Caractère octal ddd | `\ddd` |
| Caractère de contrôle Y | `\cY` |
| Caractère de retour arrière | `[\b]` |
| Rend n'importe quel caractère littéral | `\` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% tab General tokens %}

| Jetons généraux |
| -------------- |
| Nouvelle ligne | `\n` |
| Retour chariot | `\r` |
| Tabulation | `\t` |
| Caractère nul | `\0` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }

{% endtab %}
{% tab Character class modifiers %}

| Modificateurs de classe de caractères |
| ------------------------- |
| Un caractère unique parmi : a, b ou c | `[abc]` |
| Un caractère sauf\: a, b ou c | `[^abc]` |
| Un caractère dans la plage : a-z | `[a-z]` |
| Un caractère hors de la plage : a-z | `[^a-z]` |
| Un caractère dans la plage : a-z ou A-Z | `[a-zA-Z]` |
| Lettres et chiffres | `[:alnum:]` |
| Lettres | `[:alpha:]` |
| Codes ASCII 0 à 127 | `[:ascii:]` |
| Espace ou tabulation uniquement | `[:blank:]` |
| Caractères de contrôle | `[:cntrl:]` |
| Chiffres | `[:digit:]` |
| Caractères visibles (pas d'espace) | `[:word:]` |
| Lettres minuscules | `[:xdigit:]` |
| Lettres majuscules | `[:<:]` |
| Caractères de mot | `[:>:]` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% tab Group constants %}

| Constantes de groupe |
| --------------- |
| Capture tout le contenu entre parenthèses | `(...)` |
| Fait correspondre a ou b | `(a|b)` |
| Fait correspondre tout le contenu entre parenthèses | `(?:...)` |
| Regroupement atomique (sans capture) | `(?>...)` |
| Duplique le numéro de groupe de sous-motif | `(?|...)` |
| Commentaire | `(?#...)` |
| Pour l'insensibilité à la casse | `(?i)` |
| Groupe de capture nommé | `(?'name'...)` |
| Groupe de capture nommé | `(?<name>...)` |
| Groupe de capture nommé | `(?P<name>...)` |
| Modificateurs en ligne | `(?imsxXU)` |
| Instructions conditionnelles | `(?(1)yes|no)` |
| Instructions conditionnelles récursives | `(?(R#)yes|no)` |
| Instruction conditionnelle | `(?(R&name)yes|no)` |
| Condition d'anticipation | `(?(?=...)yes|no)` |
| Condition de rétrospection | `(?(?<=...)yes|no)` |
| Récurse l'ensemble du motif | `(?R)` |
| Récurse le premier sous-motif | `(?1)` |
| Récurse le premier sous-motif relatif | `(?+1)` |
| Récurse le sous-motif « name » | `(?&name)` |
| Fait correspondre le sous-motif « name » | `(?P=name)` |
| Récurse le sous-motif « name » | `(?P>name)` |
| Prédéfinir les motifs avant utilisation | `(?(DEFINE)...)` |
| Anticipation positive | `(?=...)` |
| Anticipation négative | `(?!...)` |
| Rétrospection positive | `(?<=...)` |
| Rétrospection négative | `(?<!...)` |
| Verbe de contrôle | `(*ACCEPT)` |
| Verbe de contrôle | `(*FAIL)` |
| Verbe de contrôle | `(*MARK:NAME)` |
| Verbe de contrôle | `(*COMMIT)` |
| Verbe de contrôle | `(*PRUNE)` |
| Verbe de contrôle | `(*SKIP)` |
| Verbe de contrôle | `(*THEN)` |
| Modificateur de motif | `(*UTF)` |
| Modificateur de motif | `(*UTF8)` |
| Modificateur de motif | `(*UTF16)` |
| Modificateur de motif | `(*UTF32)` |
| Modificateur de motif | `(*UCP)` |
| Modificateur de saut de ligne | `(*CR)` |
| Modificateur de saut de ligne | `(*LF)` |
| Modificateur de saut de ligne | `(*CRLF)` |
| Modificateur de saut de ligne | `(*ANYCRLF)` |
| Modificateur de saut de ligne | `(*ANY)` |
| Modificateur de saut de ligne | `\R` |
| Modificateur de saut de ligne | `(*BSR_ANYCRLF)` |
| Modificateur de saut de ligne | `(*BSR_UNICODE)` |
| Modificateur de moteur d'expression régulière | `(*LIMIT_MATCH=x)` |
| Modificateur de moteur d'expression régulière | `(*LIMIT_RECURSION=d)` |
| Modificateur de moteur d'expression régulière | `(*NO_AUTO_POSSESS)` |
| Modificateur de moteur d'expression régulière | `(*NO_START_OPT)` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% tab Quantifiers %}

| Quantificateurs |
| ----------- |
| Zéro ou un a | `a?` |
| Zéro ou plusieurs a | `a*` |
| Un ou plusieurs a | `a+` |
| Exactement 3 a | `a{3}` |
| 3 ou plus de a | `a{3,}` |
| Entre 3 et 6 a | `a{3,6}` |
| Quantificateur glouton | `a*` |
| Quantificateur paresseux | `a*?` |
| Quantificateur possessif | `a*+` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% tab Anchors %}

| Ancres |
| ------- |
| Début de la correspondance | `\G` |
| Début de la chaîne de caractères | `^` |
| Fin de la chaîne de caractères | `$` |
| Début de la chaîne de caractères | `\A` |
| Fin de la chaîne de caractères | `\Z` |
| Fin absolue de la chaîne de caractères | `\z` |
| Une limite de mot | `\b` |
| Une limite sans mot | `\B` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}

{% tab Flags and modifiers %}

| Indicateurs et modificateurs |
| ------------------- |
| Global | `g` |
| Multiligne | `m` |
| Sensible à la casse | `l` |
| Ignorer les espaces blancs | `x` |
| Ligne unique | `s` |
| Unicode | `u` |
| Étendu | `X` |
| Non glouton | `U` |
| Ancre | `A` |
| Noms de groupe dupliqués | `J` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }

{% endtab %}
{% tab Substitution %}

| Substitution |
| ------------ |
| Contenu complet de la correspondance | `\0` |
| Contenu du groupe de capture 1 | `\1 or $1` |
| Contenu du groupe de capture `foo` | `${foo}` |
| Valeurs de remplacement hexadécimales | `\x20, \x{06fa}` |
| Tabulation | `\t` |
| Retour chariot | `\r` |
| Nouvelle ligne | `\n` |
| Saut de page | `\f` |
| Transformation en majuscules | `\U` |
| Transformation en minuscules | `\L` |
| Mettre fin à toute transformation | `\E` |
{: .reset-td-br-1 aria-label="Regex reference sheet" }
{% endtab %}
{% endtabs %}