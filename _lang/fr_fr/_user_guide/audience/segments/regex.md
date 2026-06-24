---
nav_title: "Expressions régulières"
article_title: "Expressions régulières"
page_order: 8
description: "Cet article de référence explique ce que sont les expressions régulières (regex), comment commencer à les utiliser, et propose une fonctionnalité de débogueur pour valider et tester les expressions régulières."
page_type: reference
tool:
  - Testing Tools

---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/regular-expression-basics-for-braze){: style="float:right;width:120px;border:0;" class="noimgborder"} Expressions régulières {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomregular-expression-basics-for-braze-stylefloatrightwidth120pxborder0-classnoimgborder-regular-expressions}

> Une expression régulière, communément appelée regex, est une séquence de caractères qui définit un modèle de recherche. Les expressions régulières vous permettent de valider des groupements de texte et d'effectuer des actions de recherche et de remplacement. Chez Braze, nous utilisons les expressions régulières pour vous offrir une solution de correspondance de chaînes de caractères plus flexible dans votre segmentation et le filtrage de campagnes pour votre audience cible.<br><br>Cette page couvre les expressions régulières (regex), comment les utiliser, les questions fréquemment posées, et fournit un débogueur regex pour tester les expressions régulières.

<!--{% multi_lang_include video.html id="3h5Xbhl-TxE" align="right" %}-->

Dans le cours d'apprentissage Braze associé, nous vous montrons comment les expressions régulières peuvent être utilisées et testées sur [Regex101](https://regex101.com/). Nous proposons également un [testeur regex intégré](#regex-debugger), une page de référence utile, des données d'exemple référencées dans la vidéo Braze Learning sur les regex, ainsi que quelques questions fréquemment posées.

## Ressources {#resources}

- Cours d'apprentissage Braze [Les bases des expressions régulières](https://learning.braze.com/regular-expression-basics-for-braze)
- [Aide-mémoire regex]({{site.baseurl}}/regex_cheat_sheet/)
- [Données d'exemple RTF]({% image_buster /assets/download_file/regex-dummy-data.rtf %})

## Débogueur regex {#regex-debugger}

{% alert important %}
Cet outil est uniquement destiné à servir de référence et ne garantit pas que l'expression régulière corresponde à 100 % avec la plateforme Braze. Les expressions régulières dans Braze pour la segmentation et les filtres ajoutent automatiquement le modificateur `/gi`. Le [modificateur gi](https://w3schools.sinsixx.com/jsref/jsref_regexp_modifier_gi.asp.htm) est utilisé pour effectuer une recherche insensible à la casse de toutes les occurrences d'une expression régulière dans une chaîne de caractères.
<br>
Les expressions régulières pour les propriétés de déclencheur d'événements personnalisés et les filtres de déclencheur utilisent le modificateur `/g` (sensible à la casse, voir [modificateur g](https://www.w3schools.com/jsref/jsref_regexp_g.asp)) et n'utilisent pas le modificateur `/i`. Pour l'insensibilité à la casse des propriétés de déclencheur d'événements personnalisés et des filtres de déclencheur, utilisez `(?i)` à la place. Par exemple, `Matches regex (?i)STOP(?-i)` capture toute utilisation de « STOP » quelle que soit la casse (comme « stop », « please stop » et « never stop sending me messages »).
{% endalert %}

{% tabs %}
{% tab Regex Debugger %}
<div>
Ce formulaire permet la validation et le test de base des expressions régulières.
​
Regex :
​
<div class="input-group">
  <div class="input-group-prepend"><span class="input-group-text">/</span>
  </div>
 <input id="regex_input" value="" class="form-control" placeholder="regex" style="" />
 <div class="input-group-append"><span class="input-group-text">/gi</span>
 </div>
</div>
<br />
Valeur(s) à vérifier : <textarea style="" placeholder="match string" id="regex_text"></textarea><br /><br />
​
Résultats correspondants<span id="reg_count"></span> : <div id="regex_results"></div>
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

## Questions fréquemment posées {#frequently-asked-questions}

### Le filtre `does not match regex` inclut-il les valeurs vides ? {#does-the-does-not-match-regex-filter-include-blank-values}

Non. Si la valeur est vide, l'utilisateur ne sera pas inclus dans le filtre `does not match regex`.

### Comment faire correspondre exactement l'une de plusieurs valeurs (logique OU) pour un attribut personnalisé de type chaîne de caractères ? {#how-do-i-match-any-of-several-exact-values-or-logic-for-a-string-custom-attribute}

Utilisez l'alternance avec des ancres de début et de fin pour que chaque valeur corresponde exactement et que vous n'obteniez pas de correspondances partielles. Par exemple, pour correspondre exactement à `gold`, `silver` ou `bronze` :

```
(^gold$)|(^silver$)|(^bronze$)
```

### Comment filtrer les adresses e-mail spécifiques à une boîte de réception lors de la segmentation ? {#how-do-i-filter-for-inbox-specific-email-addresses-when-segmenting}

{% raw %}
Utilisez le filtre d'adresse e-mail et définissez-le sur `matches regex`. Puis référencez l'expression régulière pour les adresses e-mail :

```
[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z.-]+
```

On peut décomposer cette expression régulière en trois parties :

- `[a-zA-Z0-9.+_-]+` est le début de l'adresse e-mail avant le caractère arobase `@`. C'est le « nom » dans « name@example.com ».
- `[a-zA-Z0-9.-]+` est la première partie du domaine. C'est « example » dans « name@example.com ».
- `[a-zA-Z.-]+` est la dernière partie du domaine. C'est « com » dans « name@example.com ».

{% endraw %}

### Comment filtrer les adresses e-mail associées à un domaine spécifique ? {#how-do-i-filter-for-email-addresses-associated-to-a-specific-domain}

Supposons que vous souhaitiez filtrer les e-mails se terminant par « @braze.com ». Vous utiliseriez le filtre d'adresse e-mail, le définiriez sur `matches regex`, et saisiriez « @braze.com » dans le champ regex. La même méthode s'applique pour tout autre domaine e-mail.

![Filtre pour une adresse e-mail correspondant à l'expression régulière « @braze.com ».]({% image_buster /assets/img/regex/regeximg1.png %})

### Comment utiliser des chaînes de filtrage numériques pour des valeurs ≥ x ou ≤ x ? {#how-can-i-use-filter-number-strings-for-values-x-or-x}

Si vous recherchez des valeurs supérieures ou égales à (≥) x, utilisez l'expression régulière suivante :

```
^([x-y]|\d{z,})$
```

Où `x-y` est la plage de chiffres (0-9) du premier chiffre, et `z` est le nombre de chiffres de x plus un. Par exemple, pour des valeurs supérieures ou égales à 50, l'expression régulière serait `^([5-9][0-9]|\d{3,})$`.

Si vous recherchez des valeurs inférieures ou égales à (≤) x, utilisez l'expression régulière suivante :

```
^([x-y]|[a-b])$
```

Où `x-y` est la plage de chiffres (0-9) du premier chiffre, et `a-b` est la plage inférieure de x. Par exemple, pour des valeurs inférieures ou égales à 50, l'expression régulière serait `^([5-9][0-9]|[0-4][0-9])$`.

### Comment filtrer les attributs personnalisés qui commencent par une chaîne spécifique ? {#how-do-i-filter-custom-attributes-that-start-with-a-specific-string}

Utilisez le symbole accent circonflexe (`^`) pour indiquer par quoi la chaîne commence, puis saisissez le nom de l'attribut personnalisé que vous souhaitez spécifier.

Par exemple, si vous essayez de cibler les utilisateurs qui vivent dans des villes commençant par « San », votre expression régulière serait `^San \w`. Avec cette expression régulière, vous cibleriez avec succès les utilisateurs de villes comme San Francisco, San Diego, San Jose, etc.

![Filtre pour une ville correspondant à l'expression régulière « ^San \w ».]({% image_buster /assets/img/regex/regeximg2.png %})

### Comment filtrer des numéros de téléphone spécifiques ? {#how-do-i-filter-for-specific-phone-numbers}

Avant d'utiliser les expressions régulières pour filtrer les numéros de téléphone, n'oubliez pas que les numéros enregistrés pour les profils utilisateur doivent être au format [E.164](https://en.wikipedia.org/wiki/E.164), tel que spécifié dans [Numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers/).

En supposant que vous recherchez des numéros de téléphone américains, utilisez le format regex `1?\d\d\d\d\d\d\d\d\d\d`, où chaque répétition de `\d` est un chiffre que vous souhaitez spécifier. Les trois premiers chiffres correspondent à l'indicatif régional.

De même, le format pour les numéros de téléphone britanniques est `^\+4\d\d\d\d\d\d\d\d\d\d\d`. Pour tout autre pays, il s'agit de l'indicatif pays correspondant, suivi du nombre nécessaire de répétitions de `\d` pour chaque chiffre restant. Ainsi, dans le cas de la Lituanie avec un indicatif pays « 3 », l'expression régulière serait `^\+3\d\d\d\d\d\d\d\d\d\d`.

Si vos numéros de téléphone mobiles britanniques sont stockés sans le `+` initial, dans le format courant commençant par `447` (par exemple, `447123456789`), vous pouvez les faire correspondre avec :

```
^447\d{9}$
```

Par exemple, supposons que vous souhaitiez filtrer les utilisateurs par numéro de téléphone pour un indicatif régional spécifique, « 718 ». Utilisez le filtre de numéro de téléphone, définissez-le sur `matches regex`, et saisissez l'expression régulière suivante :

```
^1?718\d\d\d\d\d\d\d
```

![Filtre pour un numéro de téléphone correspondant à l'expression régulière « ^1?718\d\d\d\d\d\d\d ».]({% image_buster /assets/img/regex/regeximg3.png %})