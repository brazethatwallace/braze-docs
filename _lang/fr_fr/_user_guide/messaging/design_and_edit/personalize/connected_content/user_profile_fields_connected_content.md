---
nav_title: Extraire des données de profil utilisateur
article_title: Récupérer les données du profil utilisateur dans les appels de contenu connecté
page_order: 3
description: "Cet article explique comment extraire les profils utilisateurs dans vos appels de contenu connecté et les bonnes pratiques impliquant la création de modèles Liquid."
toc_headers: h2
---

# Extraire les données du profil utilisateur dans les appels de contenu connecté {#pull-user-profile-data-in-connected-content-calls}

> Cette page explique comment intégrer les profils utilisateurs dans vos appels de contenu connecté et présente les bonnes pratiques en matière de création de modèles Liquid.

## Conditions préalables {#prerequisites}

Si une réponse de contenu connecté contient des champs de profil utilisateur (dans une étiquette de personnalisation Liquid), ces valeurs doivent être définies plus tôt dans le message avec Liquid, avant l'appel de contenu connecté, afin de rendre le passback Liquid correctement. De même, l'indicateur `:rerender` doit être inclus dans la requête. Notez que l'indicateur `:rerender` n'a qu'un seul niveau de profondeur, ce qui signifie qu'il ne s'applique pas aux balises de contenu connecté imbriquées.

## Le templating Liquid dans les appels de contenu connecté {#liquid-templating-in-connected-content-calls}

Pour la personnalisation, Braze extrait les champs de profil utilisateur avant de transmettre ce champ à Liquid. Donc si la réponse du contenu connecté comporte des champs de profil utilisateur, ceux-ci doivent être définis au préalable.

Par exemple, s'il s'agissait de l'appel de contenu connecté :
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}

La réponse du contenu connecté est {% raw %}`Your language is ${language}`{% endraw %}. Le contenu affiché dans cet exemple est `Hi Jon, your language is`.

La langue elle-même ne sera pas interprétée par le template. En effet, Braze doit savoir quels champs récupérer de l'utilisateur avant d'effectuer l'appel de contenu connecté.

Pour que le passback Liquid s'affiche correctement, vous devez inclure l'étiquette {% raw %}`${language}`{% endraw %} n'importe où dans la requête, comme illustré dans l'extrait de code suivant. Le préprocesseur Liquid saura alors récupérer l'attribut « language » de l'utilisateur afin de l'avoir prêt pour le templating de la réponse.

{%raw%}
```liquid
Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}

{% alert important %}
N'oubliez pas que l'option de l'indicateur `:rerender` n'a qu'un seul niveau de profondeur. Si la réponse du contenu connecté contient elle-même d'autres balises de contenu connecté ou des balises de catalogue, Braze ne procédera pas à un nouveau rendu de ces balises supplémentaires.
{% endalert %}

## Bonnes pratiques {#best-practices}

### Utiliser `json_escape` avec les étiquettes Liquid susceptibles de casser le format JSON {#use-json_escape-with-liquid-tags-that-could-break-the-json-format}

Lorsque vous utilisez `:rerender`, ajoutez le filtre `json_escape` à toute étiquette Liquid susceptible de casser le format JSON. Si vos étiquettes Liquid contiennent des caractères qui cassent le format JSON, l'intégralité de la réponse du contenu connecté sera interprétée comme du texte et intégrée telle quelle dans le message, et aucune des variables ne sera enregistrée.

Par exemple, si la propriété d'événement `message` dans l'exemple de la section suivante contient des caractères susceptibles de casser le format JSON, ajoutez le filtre `json_escape` comme dans cet exemple :

{% raw %}
```liquid
[{
"message":"{{event_properties.${message} | json_escape}}"
}]
```
{% endraw %}