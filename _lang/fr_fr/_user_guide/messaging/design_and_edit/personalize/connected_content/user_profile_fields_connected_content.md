---
nav_title: Récupérer les données du profil utilisateur
article_title: Récupérer les données du profil utilisateur dans les appels de Contenu connecté
page_order: 3
description: "Cet article explique comment récupérer les profils utilisateur dans vos appels de Contenu connecté, ainsi que les bonnes pratiques liées au templating Liquid."
toc_headers: h2
---

# Récupérer les données du profil utilisateur dans les appels de Contenu connecté

> Cette page explique comment récupérer les profils utilisateur dans vos appels de Contenu connecté, ainsi que les bonnes pratiques liées au templating Liquid.

## Conditions préalables

Si une réponse de Contenu connecté contient des champs de profil utilisateur (au sein d'une étiquette de personnalisation Liquid), ces valeurs doivent être définies plus tôt dans le message avec Liquid, avant l'appel de Contenu connecté, afin que le renvoi Liquid s'affiche correctement. De même, le flag `:rerender` doit être inclus dans la requête. Notez que le flag `:rerender` ne fonctionne qu'à un seul niveau de profondeur, ce qui signifie qu'il ne s'appliquera pas aux étiquettes de Contenu connecté imbriquées.

## Templating Liquid dans les appels de Contenu connecté

Pour la personnalisation, Braze récupère les champs du profil utilisateur avant de les transmettre à Liquid. Par conséquent, si la réponse du Contenu connecté contient des champs de profil utilisateur, ceux-ci doivent être définis au préalable.

Par exemple, si l'appel de Contenu connecté était le suivant :
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}

La réponse du Contenu connecté est {% raw %}`Your language is ${language}`{% endraw %}. Le contenu affiché dans cet exemple est `Hi Jon, your language is`.

La langue elle-même ne sera pas interprétée par le template. En effet, Braze doit savoir quels champs récupérer de l'utilisateur avant d'effectuer l'appel de Contenu connecté.

Pour que le renvoi Liquid s'affiche correctement, vous devez inclure l'étiquette {% raw %}`${language}`{% endraw %} n'importe où dans la requête, comme illustré dans l'extrait de code suivant. Le préprocesseur Liquid saura alors récupérer l'attribut « language » de l'utilisateur afin de l'avoir prêt pour le templating de la réponse.

{%raw%}
```liquid
Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}

{% alert important %}
N'oubliez pas que l'option du flag `:rerender` ne fonctionne qu'à un seul niveau de profondeur. Si la réponse du Contenu connecté contient elle-même d'autres étiquettes de Contenu connecté ou des étiquettes de catalogue, Braze ne procédera pas à un nouveau rendu de ces étiquettes supplémentaires.
{% endalert %}

## Bonnes pratiques

### Utiliser `json_escape` avec les étiquettes Liquid susceptibles de casser le format JSON

Lorsque vous utilisez `:rerender`, ajoutez le filtre `json_escape` à toute étiquette Liquid susceptible de casser le format JSON. Si vos étiquettes Liquid contiennent des caractères qui cassent le format JSON, l'intégralité de la réponse du Contenu connecté sera interprétée comme du texte et intégrée telle quelle dans le message, et aucune des variables ne sera enregistrée.

Par exemple, si la propriété d'événement `message` dans l'exemple ci-dessous contient des caractères susceptibles de casser le format JSON, ajoutez le filtre `json_escape` comme dans cet exemple :

{% raw %}
```liquid
[{
"message":"{{event_properties.${message} | json_escape}}"
}]
```
{% endraw %}