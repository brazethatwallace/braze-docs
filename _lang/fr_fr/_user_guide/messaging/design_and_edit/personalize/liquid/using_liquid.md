---
nav_title: Utiliser Liquid
article_title: Utiliser Liquid
page_order: 0
description: "Cet article de référence fournit un aperçu des cas d'utilisation courants de Liquid et explique comment inclure des étiquettes Liquid dans vos messages."
search_rank: 2
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/dynamic-personalization-with-liquid){: style="float:right;width:120px;border:0;" class="noimgborder"}Utiliser Liquid {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecompathdynamic-personalization-with-liquid-stylefloatrightwidth120pxborder0-classnoimgborderuse-liquid}

> Cet article vous montre comment utiliser différents attributs utilisateur pour insérer dynamiquement des informations personnelles dans vos messages.

Liquid est un langage de modèles open source développé par Shopify et écrit en Ruby. Vous pouvez l'utiliser dans Braze pour extraire les données du profil utilisateur dans vos messages et personnaliser ces données. Par exemple, vous pouvez utiliser des étiquettes Liquid pour créer des messages conditionnels, comme envoyer différentes offres en fonction de la date anniversaire d'abonnement d'un utilisateur. De plus, les filtres peuvent manipuler les données, par exemple en convertissant la date d'inscription d'un utilisateur d'un horodatage vers un format plus lisible, tel que « 15 janvier 2022 ». Pour plus de détails sur la syntaxe Liquid et ses fonctionnalités, consultez [Étiquettes de personnalisation prises en charge]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

## Comment ça fonctionne {#how-it-works}

Les étiquettes Liquid agissent comme des marques substitutives dans vos messages. Elles peuvent extraire des informations consenties du compte de votre utilisateur et permettre la personnalisation ainsi que des pratiques d'envoi de messages pertinentes.

Dans le bloc suivant, vous pouvez voir une double utilisation d'une étiquette Liquid pour appeler le prénom de l'utilisateur, ainsi qu'une étiquette par défaut au cas où l'utilisateur n'aurait pas enregistré son prénom.

{% raw %}
```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```
{% endraw %}

Pour une utilisatrice nommée Janet Doe, le message apparaîtrait de l'une des manières suivantes :

```
Hi Janet, thanks for using the App!
```

Ou...

```
Hi Valued User, thanks for using the App!
```

{% alert important %}
Les commentaires HTML (`<!-- -->`) sont supprimés avant toute lecture du Liquid, de sorte que les étiquettes Liquid à l'intérieur des commentaires HTML **ne s'affichent pas** dans votre message. Pour un rendu correct, assurez-vous que toutes les étiquettes Liquid que vous souhaitez utiliser se trouvent en dehors des commentaires HTML.
{% endalert %}

## Valeurs prises en charge pour la substitution {#supported-values-to-substitute}

Les valeurs suivantes peuvent être substituées dans un message, en fonction de leur disponibilité :

- [Informations utilisateur de base]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) (par exemple, `first_name`, `last_name`, `email_address`)
- [Attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)
    - [Attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support#liquid-templating)
- [Propriétés d'événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events)
- [Informations sur l'appareil le plus récemment utilisé]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#most-recently-used-device-information)
- [Informations sur l'appareil ciblé]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#targeted-device-information)

Vous pouvez également extraire du contenu directement depuis un serveur web grâce au [Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) de Braze.

{% alert important %}
Braze prend actuellement en charge Liquid jusqu'à la version Liquid 5 de Shopify incluse.
{% endalert %}

## Utiliser Liquid {#using-liquid}

En utilisant les [étiquettes Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags), vous pouvez améliorer la qualité de vos messages en les enrichissant d'une touche personnelle.

### Syntaxe Liquid {#liquid-syntax}

Liquid suit une structure, ou syntaxe, spécifique que vous devez garder à l'esprit lorsque vous créez une personnalisation dynamique. Voici quelques règles de base à retenir :

1. **Utilisez des guillemets droits dans Braze :** il y a une différence entre les guillemets courbes (**' '**) et les guillemets droits (**&#39; &#39;**). Utilisez des guillemets droits (**&#39; &#39;**) dans votre Liquid dans Braze. Vous pouvez voir des guillemets courbes lors du copier-coller depuis certains éditeurs de texte, ce qui peut causer des problèmes dans votre Liquid. Si vous saisissez les guillemets directement dans le tableau de bord de Braze, tout ira bien !
2. **Les accolades vont par paires :** chaque accolade doit être ouverte et fermée **{ }**. Assurez-vous d'utiliser des accolades !
3. **Les instructions if vont par paires :** pour chaque `if`, vous avez besoin d'un `endif` pour indiquer que l'instruction `if` est terminée.
4. **Les instructions case vont par paires :** pour chaque `case`, vous avez besoin d'un `endcase` pour fermer le bloc.
5. **Les noms de variables doivent utiliser des caractères ASCII :** les noms de variables Liquid (créés avec `assign` ou `capture`) ne prennent en charge que les lettres ASCII, les chiffres et les underscores. Les noms d'attributs de personnalisation Braze (à l'intérieur de `custom_attribute.${...}` ou `event_properties.${...}`) peuvent inclure des caractères non ASCII.

#### Où utiliser les opérateurs et les filtres {#where-to-use-operators-and-filters}

Les opérateurs (tels que `==`, `!=`, `>`, `and`, `or`) et les filtres (tels que `| size`, `| plus`) ne peuvent être utilisés que dans des contextes Liquid spécifiques.

| Contexte | Opérateurs | Filtres |
|-----------|-----------|---------|
| `assign` | Non pris en charge | Pris en charge |
| `if`, `elsif`, `unless` | Pris en charge | Non pris en charge |
| `case`, `when` | Correspondance d'égalité uniquement[^case_when_ops] | Non pris en charge |
| `for` | Non pris en charge | Non pris en charge |
| Accès aux tableaux (`[ ]`) | Non pris en charge | Non pris en charge |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Où utiliser les opérateurs et les filtres" }

[^case_when_ops]: Dans les étiquettes `case` et `when`, Liquid compare l'expression `case` à chaque valeur `when` en utilisant l'égalité (similaire à l'enchaînement de `if` et `elsif` avec `==`). Vous ne pouvez pas utiliser d'opérateurs de comparaison ou logiques arbitraires à l'intérieur d'une clause `when` comme vous le feriez avec `if` et `elsif`. Pour des exemples, consultez [Logique de messagerie conditionnelle]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#case-and-when-tags).

Lorsque vous avez besoin d'une valeur filtrée dans un contexte qui ne prend pas en charge les filtres, assignez d'abord le résultat à une variable.

{% raw %}

##### Utiliser le résultat d'un filtre dans une condition {#use-a-filter-result-in-a-conditional}

Vous ne pouvez pas utiliser un filtre directement dans une instruction conditionnelle. Ceci est incorrect :

```liquid
{% if my_array | size > 3 %}
You have more than 3 items!
{% endif %}
```

À la place, assignez le résultat du filtre à une variable :

```liquid
{% assign array_size = my_array | size %}
{% if array_size > 3 %}
You have more than 3 items!
{% endif %}
```

##### Utiliser le résultat d'un filtre dans une boucle for {#use-a-filter-result-in-a-for-loop}

Vous ne pouvez pas appliquer un filtre à l'itérable dans une boucle `for`. Ceci est incorrect :

```liquid
{% for item in my_array | reverse %}
{{ item }}
{% endfor %}
```

À la place, assignez la valeur filtrée à une variable :

```liquid
{% assign reversed = my_array | reverse %}
{% for item in reversed %}
{{ item }}
{% endfor %}
```

##### Utiliser le résultat d'un filtre pour l'accès aux tableaux {#use-a-filter-result-for-array-access}

Vous ne pouvez pas utiliser un filtre à l'intérieur de crochets. Ceci est incorrect :

```liquid
{{ my_array[my_var | minus: 1] }}
```

À la place, assignez d'abord la valeur filtrée :

```liquid
{% assign adjusted_index = my_var | minus: 1 %}
{{ my_array[adjusted_index] }}
```

##### Stocker le résultat d'une comparaison dans une variable {#store-a-comparison-result-in-a-variable}

Vous ne pouvez pas utiliser un opérateur dans une instruction `assign`. Ceci est incorrect :

```liquid
{% assign is_vip = total_spend > 100 %}
{% if is_vip %}
Welcome to the VIP lounge!
{% endif %}
```

À la place, utilisez une condition pour définir la variable :

```liquid
{% assign is_vip = false %}
{% if total_spend > 100 %}
{% assign is_vip = true %}
{% endif %}

{% if is_vip %}
Welcome to the VIP lounge!
{% endif %}
```

{% endraw %}

#### Attributs par défaut et attributs personnalisés {#default-attributes-and-custom-attributes}

{% raw %}

Si vous incluez le texte suivant dans votre message : `{{${first_name}}}`, le prénom de l'utilisateur (extrait du profil utilisateur) sera substitué lors de l'envoi du message. Vous pouvez utiliser le même format avec d'autres attributs utilisateur par défaut.

Si vous souhaitez utiliser la valeur d'un attribut personnalisé, vous devez ajouter l'espace de noms « custom_attribute » à la variable. Par exemple, pour utiliser un attribut personnalisé nommé « zip code », vous incluriez `{{custom_attribute.${zip code}}}` dans votre message.

### Insérer des étiquettes {#inserting-tags}

Vous pouvez insérer des étiquettes en tapant deux accolades ouvrantes `{{` dans n'importe quel message, ce qui déclenchera une fonctionnalité d'auto-complétion qui continuera à se mettre à jour au fur et à mesure de votre saisie. Vous pouvez même sélectionner une variable parmi les options qui apparaissent pendant que vous tapez.

Si vous utilisez une étiquette personnalisée, vous pouvez copier et coller l'étiquette dans le message de votre choix.

#### Exceptions pour les doubles accolades {#exceptions-for-double-brackets}

Si vous utilisez une étiquette à l'intérieur d'une autre étiquette Liquid, comme `{% assign %}` ou `{% if %}`, vous pouvez utiliser soit les doubles accolades, soit aucune accolade. Ce n'est que lorsque l'étiquette est utilisée seule qu'elle doit être encadrée par des doubles accolades. Par souci de simplicité, vous pouvez toujours utiliser les doubles accolades.

Les étiquettes suivantes sont toutes correctes :

```liquid
{% if custom_attribute.${Number_Game_Attended} == 1 %}
{% if {{custom_attribute.${Number_Game_Attended}}} == 1 %}

{% assign value_one = {{custom_attribute.${one}}} %}
{% assign value_one = custom_attribute.${one} %}
```

{% endraw %}

{% alert note %}

Si vous utilisez Liquid dans vos e-mails, veillez à :

1. L'insérer en utilisant l'éditeur HTML plutôt que l'éditeur classique. L'éditeur classique peut interpréter le Liquid comme du texte brut. Par exemple, le Liquid serait interprété comme {% raw %}`Hi {{ ${first_name} }}, thanks for using our service!`{% endraw %} au lieu d'insérer le prénom de l'utilisateur.
2. Placer le code Liquid uniquement à l'intérieur de la balise `<body>`. Le placer en dehors de cette balise peut entraîner un rendu incohérent lors de la réception.

{% endalert %}

### Basculer entre les éditeurs HTML et classique {#switching-between-html-and-classic-editors}

Lorsque vous basculez entre les éditeurs HTML et classique, les extraits de code Liquid et les Content Blocks peuvent changer de position dans votre message. Vérifiez votre modèle après avoir changé d'éditeur. Si vous avez besoin d'un contrôle de mise en page plus prévisible, utilisez l'éditeur par glisser-déposer.

### Insérer des variables pré-formatées {#inserting-pre-formatted-variables}

Vous pouvez insérer des variables pré-formatées avec des valeurs par défaut via la fenêtre modale **Ajouter une personnalisation** située à proximité de tout champ de texte avec modèle.

![La fenêtre modale Ajouter une personnalisation qui apparaît après avoir sélectionné l'insertion de personnalisation. La fenêtre modale contient des champs pour le type de personnalisation, l'attribut, la valeur par défaut facultative, et affiche un aperçu de la syntaxe Liquid.]({% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}){: style="max-width:90%;"}

La fenêtre modale insérera le Liquid avec votre valeur par défaut spécifiée à l'endroit où se trouvait votre curseur. Le point d'insertion est également indiqué par la zone de prévisualisation, qui affiche le texte avant et après. Si un bloc de texte est surligné, le texte surligné sera remplacé.

![Un GIF de la fenêtre modale Ajouter une personnalisation montrant l'utilisateur qui saisit « fellow traveler » comme valeur par défaut, et la fenêtre modale qui remplace le texte surligné « name » dans le compositeur par l'extrait de code Liquid.]({% image_buster /assets/img_archive/insert_var_shot.gif %})