---
nav_title: Filtres
article_title: Filtres Liquid
page_order: 3
description: "Cette page de référence répertorie les filtres qui peuvent être utilisés pour reformater du contenu statique ou dynamique."

---

# Filtres {#filters}

> Cet article de référence fournit un aperçu des filtres dans Liquid et présente les filtres pris en charge par Braze. Vous cherchez des idées sur la façon d'utiliser ces filtres ? Consultez notre [bibliothèque de cas d'utilisation Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases/).

Les filtres permettent de modifier la sortie de nombres, chaînes de caractères, variables et objets dans Liquid. Vous pouvez utiliser des filtres pour reformater du texte statique ou dynamique, par exemple pour convertir une chaîne de caractères de minuscules en majuscules ou pour effectuer des opérations mathématiques comme l'addition ou la division.

{% alert important %}
Braze ne prend pas en charge tous les filtres Liquid de Shopify. Cette page tente de répertorier les filtres Liquid que Braze a testés, mais il ne s'agit pas nécessairement d'une liste exhaustive. Testez toujours votre code Liquid avant d'envoyer des messages. <br><br>Si vous avez des questions sur un filtre qui n'est pas répertorié ici, contactez votre gestionnaire de la satisfaction client.
{% endalert %}

## Syntaxe des filtres {#filter-syntax}

{% raw %}

Les filtres doivent être placés dans une balise de sortie `{{ }}` et sont indiqués par un caractère pipe `|`.

{% endraw %}

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{"Big Sale" | upcase}}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
BIG SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

Dans cet exemple, `Big Sale` est une chaîne de caractères et `upcase` est le filtre appliqué.

{% alert note %}
Les filtres peuvent être utilisés dans les instructions `assign` et les balises de sortie {% raw %}(`{{ }}`){% endraw %}, mais pas dans les conditions (`if`, `elsif`, `unless`), les blocs `case`/`when`, les boucles `for` ou les crochets d'accès aux tableaux. Pour utiliser une valeur filtrée dans l'un de ces contextes, assignez d'abord le résultat à une variable. Pour plus de détails, consultez [Où utiliser les opérateurs et les filtres]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid/#where-to-use-operators-and-filters).
{% endalert %}

### Syntaxe pour plusieurs filtres {#syntax-for-multiple-filters}

Vous pouvez utiliser plusieurs filtres sur une même sortie. Ils sont appliqués de gauche à droite.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
 {{ "Big Sale" | upcase | remove: "BIG" }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Filtres de tableaux {#array-filters}

Les filtres de tableaux sont utilisés pour modifier la sortie des tableaux.

| Filtre               | Définition                                                                                                         | Pris en charge |
| :------------------- | :----------------------------------------------------------------------------------------------------------------- | :-------- |
| [join](https://shopify.dev/docs/api/liquid/filters/join)          | Joint les éléments d'un tableau avec le caractère passé en paramètre. Le résultat est une chaîne de caractères unique.          | ✅  Oui   |
| [first](https://shopify.dev/docs/api/liquid/filters/first)         | Renvoie le premier élément d'un tableau. Dans un tableau d'attributs personnalisés, il s'agit de la valeur la plus anciennement ajoutée.                | ✅  Oui   |
| [last](https://shopify.dev/docs/api/liquid/filters/last)          | Renvoie le dernier élément d'un tableau. Dans un tableau d'attributs personnalisés, il s'agit de la valeur la plus récemment ajoutée.          | ✅  Oui   |
| [compact](https://shopify.dev/api/liquid/filters/compact)       | Supprime tous les éléments `nil` d'un tableau.                                                                             | ✅  Oui   |
| [concat](https://shopify.dev/api/liquid/filters/concat)        | Combine un tableau avec un autre tableau.                                                                              | ✅  Oui   |
| [find_index](https://shopify.dev/docs/api/liquid/filters/find_index)         | Renvoie l'élément situé à l'index spécifié dans un tableau. Le premier élément d'un tableau est référencé avec `[0]`. | ⛔  Non   |
| [map](https://shopify.dev/api/liquid/filters/map)           | Accepte un attribut d'élément de tableau en paramètre et crée un tableau à partir de la valeur de chaque élément du tableau.        | ✅  Oui   |
| [reverse](https://shopify.dev/api/liquid/filters/reverse)       | Inverse l'ordre des éléments d'un tableau.                                                                       | ✅  Oui   |
| [size](https://shopify.dev/api/liquid/filters/size)          | Renvoie la taille d'une chaîne de caractères (le nombre de caractères) ou d'un tableau (le nombre d'éléments).                      | ✅  Oui   |
| [slice](https://shopify.dev/api/liquid/filters/slice)        | Renvoie une sous-chaîne d'une chaîne de caractères ou un sous-ensemble d'un tableau, à partir de l'index spécifié.                          | ✅  Oui   |
| [sort](https://shopify.dev/api/liquid/filters/sort)         | Trie les éléments d'un tableau selon un attribut donné d'un élément du tableau.                                    | ✅  Oui   |
| [sort_natural](https://shopify.dev/api/liquid/sort_natural) | Trie les éléments d'un tableau par ordre alphabétique sans tenir compte de la casse.                                                | ✅  Oui   |
| [uniq](https://shopify.dev/api/liquid/filters/uniq)         | Supprime les doublons d'éléments dans un tableau.                                                           | ✅  Oui   |
| [where](https://shopify.dev/api/liquid/where)        | Filtre un tableau pour n'inclure que les éléments ayant une valeur de propriété spécifique.                                             | ✅  Oui   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Filtres de tableaux" }

## Filtres de couleur {#color-filters}

Les [filtres de couleur](https://shopify.dev/api/liquid/filters/color-filters) ne sont pas pris en charge dans Braze.

## Filtres de police {#font-filters}

Les [filtres de police](https://shopify.dev/api/liquid/filters/font-filters) ne sont pas pris en charge dans Braze.

## Filtres mathématiques {#math-filters}

Les filtres mathématiques vous permettent d'effectuer des opérations mathématiques. Si vous utilisez plusieurs filtres sur une même sortie, ils seront appliqués de gauche à droite.

| Filtre  | Définition      | Pris en charge |
| :------ |:----------------| :-------- |
| [abs](https://shopify.dev/api/liquid/filters/abs)        | Renvoie la valeur absolue d'un nombre.     | ✅  Oui   |
| [at_most](https://shopify.dev/api/liquid/filters/at_most)    | Limite un nombre à une valeur maximale.   | ✅  Oui   |
| [at_least](https://shopify.dev/api/liquid/filters/at_least)   | Limite un nombre à une valeur minimale.   | ✅  Oui   |
| [ceil](https://shopify.dev/api/liquid/filters/ceil)       | Arrondit une sortie à l'entier supérieur.  | ✅  Oui   |
| [divided_by](https://shopify.dev/api/liquid/filters/divided_by) | Divise une sortie par un nombre. La sortie est arrondie à l'entier inférieur. Consultez l'astuce suivante pour éviter l'arrondi. | ✅  Oui   |
| [floor](https://shopify.dev/api/liquid/filters/floor)      | Arrondit une sortie à l'entier inférieur.        | ✅  Oui   |
| [minus](https://shopify.dev/api/liquid/filters/minus)      | Soustrait un nombre d'une sortie.          | ✅  Oui   |
| [plus](https://shopify.dev/api/liquid/filters/plus)       | Ajoute un nombre à une sortie.     | ✅  Oui   |
| [round](https://shopify.dev/api/liquid/filters/round)      | Arrondit la sortie à l'entier le plus proche ou au nombre de décimales spécifié.  | ✅  Oui   |
| [times](https://shopify.dev/api/liquid/filters/times)     | Multiplie une sortie par un nombre.       | ✅  Oui   |
| [modulo](https://shopify.dev/api/liquid/filters/modulo)    | Divise une sortie par un nombre et renvoie le reste.   | ✅  Oui   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Filtres mathématiques" }

{% alert tip %}
Lorsque vous divisez des entiers par des entiers dans Liquid, si le résultat est un float (nombre à décimales), Liquid arrondira automatiquement à l'entier inférieur. En revanche, diviser des entiers par des floats donnera toujours un float. Vous pouvez donc convertir vos entiers en float (1.0, 2.0, 3.0) pour obtenir un float en retour.
{% raw %}
<br><br>Par exemple, `{{15 | divided_by: 2}}` renverra `7`, tandis que `{{15 | divided_by: 2.0}}` renverra `7.5`.
{% endraw %}
{% endalert %}

### Opérations mathématiques avec des attributs personnalisés {#mathematical-operations-with-custom-attributes}

Gardez à l'esprit que vous ne pouvez pas effectuer d'opérations mathématiques entre deux attributs personnalisés.

{% raw %}

```liquid
{{custom_attribute.${current_rewards_balance} | plus: {{custom_attribute.${giftcard_balance}}}}}
```

Cet exemple ne fonctionnerait pas car vous ne pouvez pas référencer plusieurs attributs personnalisés dans une seule ligne de Liquid. Vous devez plutôt assigner une variable à au moins l'une de ces valeurs avant d'exécuter les fonctions mathématiques. L'addition de deux attributs personnalisés nécessite deux lignes de Liquid :

1. Une pour assigner l'attribut personnalisé à une variable,
2. Une pour effectuer l'addition.

#### Cas d'utilisation : calculer le solde actuel {#use-case-calculate-current-balance}

Supposons que nous voulions calculer le solde actuel d'un utilisateur en additionnant le solde de sa carte cadeau et le solde de ses récompenses.

1. Utilisez la balise `assign` pour substituer l'attribut personnalisé `current_rewards_balance` par le terme « balance ». Vous disposez maintenant d'une variable nommée `balance` que vous pouvez manipuler.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

{: start="2"}
2. Utilisez le filtre `plus` pour combiner le solde de la carte cadeau de chaque utilisateur avec son solde de récompenses, représenté par l'objet `{{balance}}`.
{% endraw %}
{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
You have $35 to spend!
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Filtres monétaires {#money-filters}

Si vous informez un utilisateur de son achat, d'un solde de compte ou de tout ce qui concerne de l'argent, vous devriez utiliser les filtres monétaires. Ces filtres garantissent que vos décimales sont au bon endroit et qu'aucune partie de votre mise à jour n'est perdue (comme ce `0` gênant à la fin).

| Filtre         | Définition          | Pris en charge |
| :--------------- | :--------------- | :-------- |
| [money](https://shopify.dev/api/liquid/filters/money)      | Formate les nombres pour s'assurer que les décimales sont au bon endroit et que les zéros ne sont pas supprimés à la fin des nombres.   | ✅  Oui   |
| [money_with_currency](https://shopify.dev/api/liquid/filters/money_with_currency)    | Formate les nombres avec le symbole de la devise.     | ⛔  Non    |
| [money_without_currency](https://shopify.dev/api/liquid/filters/money_without_currency)     | Formate les nombres sans le symbole de la devise.      | ⛔  Non    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Filtres monétaires" }

{% alert important %}
Pour formater correctement un nombre avec le filtre `money`, supprimez les virgules dans le nombre et ajoutez le filtre `plus: 0` avant le filtre `money`. Par exemple, consultez le code Liquid suivant :<br><br>
{% raw %}
```liquid
{% assign my_int = "350000.25" | plus: 0 %}
{{ my_int | money }}
```
{% endraw %}
{% endalert %}

### Filtre money de Shopify versus filtre money de Braze {#shopify-money-filter-versus-braze-money-filter}

{% alert warning %}
Le comportement du filtre `money` de Shopify diffère de son utilisation dans Braze. Consultez les exemples suivants pour une description précise du comportement attendu.
{% endalert %}

{% raw %}
Si vous saisissez un attribut personnalisé (comme `account_balance`), vous devriez toujours utiliser le filtre `money` pour placer vos décimales au bon endroit et empêcher les zéros de disparaître à la fin des nombres :

```liquid
${{custom_attribute.${account_balance} | money}}
```
{% endraw %}

| AVEC LE FILTRE MONEY                       | SANS LE FILTRE MONEY                    |
| :------------------------------------------ | :------------------------------------------ |
| ![Avec le filtre money]({% image_buster /assets/img/with_money_filter.png %})                     | ![Sans le filtre money]({% image_buster /assets/img/without_money_filter.png %})                  |
| Où `account_balance` est saisi à `17.8`. | Où `account_balance` est saisi à `17.8`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Filtre money de Shopify versus filtre money de Braze" }

Le filtre `money` dans Braze diffère de celui de Shopify car il n'applique pas automatiquement les points décimaux selon un paramètre prédéfini. Par exemple, prenons le scénario suivant où `rewards_redeemed` contient une valeur de `145` :

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | money }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
$145.00
```
{% endraw %}
{% endtab %}
{% endtabs %}

Selon le filtre [money](https://shopify.dev/api/liquid/filters/money) de Shopify, la sortie devrait être `$1.45`, mais dans Braze, la sortie sera `$145.00`. Pour contourner ce problème, vous pouvez utiliser le filtre `divided_by` pour convertir le nombre en décimal avant d'appliquer le filtre money :

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | divided_by: 100.00 | money }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
$1.45
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Filtres de chaînes de caractères {#string-filters}

Les filtres de chaînes de caractères sont utilisés pour manipuler les sorties et les variables de chaînes de caractères. Les chaînes de caractères sont une combinaison de caractères alphanumériques et doivent être entourées de guillemets droits.

{% alert note %}
Les guillemets droits sont différents des guillemets courbes dans Liquid. Faites attention lorsque vous copiez et collez du code Liquid depuis un éditeur de texte dans Braze, car les guillemets courbes provoqueront des erreurs dans votre code Liquid. Si vous écrivez votre code Liquid directement dans Braze, les guillemets droits seront appliqués automatiquement.
{% endalert %}

| Filtre          | Description     | Pris en charge |
| :--------------- | ------------- | --------- |
| [append](https://shopify.dev/api/liquid/filters/append)     | Ajoute des caractères à la fin d'une chaîne de caractères.           | ✅  Oui   |
| [camelize](https://shopify.dev/docs/api/liquid/filters/camelize)     | Convertit une chaîne de caractères en CamelCase.             | ⛔  Non    |
| [capitalize](https://shopify.dev/api/liquid/filters/capitalize)     | Met en majuscule le premier mot d'une chaîne de caractères et met en minuscules les caractères restants.         | ✅  Oui   |
| [downcase](https://shopify.dev/api/liquid/filters/downcase)      | Convertit une chaîne de caractères en minuscules.         | ✅  Oui   |
| [escape](https://shopify.dev/api/liquid/filters/escape)    | Échappe une chaîne de caractères.             | ✅  Oui   |
| [handleize](https://shopify.dev/api/liquid/filters/handleize)        | Formate une chaîne de caractères en handle.        | ⛔  Non    |
| [md5](https://shopify.dev/api/liquid/filters/md5)    | Convertit une chaîne de caractères en hash MD5. Consultez les [filtres d'encodage]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/#encoding-filters) pour en savoir plus.   | ✅  Oui   |
| [sha1](https://shopify.dev/api/liquid/filters/sha1)    | Convertit une chaîne de caractères en hash SHA-1. Consultez les [filtres d'encodage]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/#encoding-filters) pour en savoir plus.  | ✅  Oui   |
| hmac_sha1_hex<br>(anciennement [hmac_sha_1](https://shopify.dev/api/liquid/filters/string-filters#hmac_sha1)) | Convertit une chaîne de caractères en hash SHA-1 à l'aide d'un code d'authentification de message par hachage (HMAC). Passez la clé secrète du message en paramètre du filtre. Consultez les [filtres d'encodage]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/#encoding-filters) pour en savoir plus. | ✅  Oui   |
| [hmac_sha256](https://shopify.dev/api/liquid/filters/hmac_sha256)    | Convertit une chaîne de caractères en hash SHA-256 à l'aide d'un code d'authentification de message par hachage (HMAC). Passez la clé secrète du message en paramètre du filtre.       | ✅  Oui   |
| hmac_sha512 | Convertit une chaîne de caractères en hash SHA-512 à l'aide d'un code d'authentification de message par hachage (HMAC). Passez la clé secrète du message en paramètre du filtre. | ✅  Oui  |
| [newline_to_br](https://shopify.dev/api/liquid/filters/newline_to_br)     | Insère une balise HTML de saut de ligne `<br>` devant chaque saut de ligne dans une chaîne de caractères.        | ✅  Oui   |
| [pluralize](https://shopify.dev/api/liquid/filters/pluralize)   | Renvoie la version singulière ou plurielle d'une chaîne de caractères anglaise en fonction de la valeur d'un nombre.      | ⛔  Non    |
| [prepend](https://shopify.dev/api/liquid/filters/prepend)     | Ajoute des caractères au début d'une chaîne de caractères.      | ✅  Oui   |
| [remove](https://shopify.dev/api/liquid/filters/remove)      | Supprime toutes les occurrences d'une sous-chaîne dans une chaîne de caractères.       | ✅  Oui   |
| [remove_first](https://shopify.dev/api/liquid/filters/remove_first)    | Supprime uniquement la première occurrence d'une sous-chaîne dans une chaîne de caractères.      | ✅  Oui   |
| [replace](https://shopify.dev/api/liquid/filters/replace)        | Remplace toutes les occurrences d'une chaîne de caractères par une sous-chaîne.   | ✅  Oui   |
| [replace_first](https://shopify.dev/api/liquid/filters/replace_first)        | Remplace la première occurrence d'une chaîne de caractères par une sous-chaîne.      | ✅  Oui   |
| [slice](https://shopify.dev/api/liquid/filters/slice)       | Le filtre slice renvoie une sous-chaîne, à partir de l'index spécifié.       | ✅  Oui   |
| [split](https://shopify.dev/api/liquid/filters/split)  | Le filtre split prend une sous-chaîne en paramètre. La sous-chaîne est utilisée comme délimiteur pour diviser une chaîne de caractères en tableau.            | ✅  Oui   |
| [strip](https://shopify.dev/api/liquid/filters/strip)   | Supprime les tabulations, espaces et sauts de ligne (tous les espaces blancs) des côtés gauche et droit d'une chaîne de caractères.                                                                                                    | ✅  Oui   |
| [lstrip](https://shopify.dev/api/liquid/filters/lstrip)     | Supprime les tabulations, espaces et sauts de ligne (tous les espaces blancs) du côté gauche d'une chaîne de caractères.    | ⛔  Non    |
| [rstrip](https://shopify.dev/api/liquid/filters/rstrip)             | Supprime les tabulations, espaces et sauts de ligne (tous les espaces blancs) du côté droit d'une chaîne de caractères.          | ⛔  Non    |
| [strip_html](https://shopify.dev/api/liquid/filters/strip_html)         | Supprime toutes les balises HTML d'une chaîne de caractères.        | ✅  Oui   |
| [strip_newlines](https://shopify.dev/api/liquid/filters/strip_newlines)  | Supprime tous les sauts de ligne d'une chaîne de caractères.        | ✅  Oui   |
| [truncate](https://shopify.dev/api/liquid/filters/truncate)    | Tronque une chaîne de caractères au nombre de caractères passé en premier paramètre. Des points de suspension (...) sont ajoutés à la chaîne tronquée et sont inclus dans le nombre de caractères.    | ✅  Oui   |
| [truncatewords](https://shopify.dev/api/liquid/filters/truncatewords)   | Tronque une chaîne de caractères au nombre de mots passé en premier paramètre. Des points de suspension (...) sont ajoutés à la chaîne tronquée.    | ✅  Oui   |
| [upcase](https://shopify.dev/api/liquid/filters/upcase)   | Convertit une chaîne de caractères en majuscules.      | ✅  Oui   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Filtres de chaînes de caractères" }

## Filtres supplémentaires {#additional-filters}

Les filtres généraux suivants servent à de nombreuses fins, notamment le formatage ou la conversion de contenu.

| Filtre                | Description                                                                                                                      | Pris en charge |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| [date](https://shopify.dev/api/liquid/filters/date)           | Convertit un horodatage dans un autre format de date. Consultez le [filtre date](#date-filter) pour en savoir plus.         | ✅  Oui   |
| [default](https://shopify.dev/api/liquid/filters/default)        | Définit une valeur par défaut pour toute variable sans valeur assignée. Peut être utilisé avec des chaînes de caractères, des tableaux et des hashes.      | ✅  Oui   |
| [format_address](https://shopify.dev/api/liquid/filters/format_address) | Formate une adresse pour afficher les éléments de l'adresse dans l'ordre correspondant à leur localisation.        | ⛔  Non    |
| [highlight](https://shopify.dev/api/liquid/filters/highlight)      | Entoure les mots dans les résultats de recherche avec une balise HTML `<strong>` ayant la classe highlight s'ils correspondent aux termes de recherche soumis. | ⛔  Non    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Filtres supplémentaires" }

Vous trouverez d'autres filtres pris en charge, tels que les filtres d'encodage et d'URL, sur notre page [Filtres avancés]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/).

### Filtre date {#date-filter}

Le filtre `date` peut être utilisé pour convertir un horodatage dans un format de date différent. Vous pouvez passer des paramètres au filtre `date` pour reformater l'horodatage. Pour des exemples de ces paramètres, consultez [strfti.me](http://www.strfti.me/).

Par exemple, supposons que la valeur de `date_attribute` soit l'horodatage `2021-06-03 17:13:41 UTC`.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%b %d'}}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
03 June
```
{% endraw %}
{% endtab %}
{% endtabs %}

En plus des options de formatage `strftime`, Braze prend également en charge la conversion d'un horodatage en temps Unix avec le filtre date `%s`. Par exemple, pour obtenir `date_attribute` en temps Unix :

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%s' }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
1433351621
```
{% endraw %}
{% endtab %}
{% endtabs %}