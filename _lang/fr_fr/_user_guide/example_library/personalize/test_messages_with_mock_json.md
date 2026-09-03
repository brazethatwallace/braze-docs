---
nav_title: Tester les messages avec du JSON simulé
article_title: Tester les messages avec du JSON simulé dans l'aperçu
page_order: 1
page_type: reference
description: "Utilisez les balises Liquid capture et json_parse pour simuler du contenu connecté ou du JSON de type entrée dans l'aperçu du compositeur de messages, sans lancer de Campaign ni envoyer de messages de test."
---

# Tester les messages avec du JSON simulé dans l'aperçu {#test-messages-with-mock-json-in-preview}

> Simulez du JSON de type API ou de type entrée dans votre message avec `capture` et `json_parse` afin de valider le Liquid et la mise en page dans l'aperçu du compositeur avant de lancer une Campaign, de déclencher un Canvas ou d'appeler du contenu connecté en direct.

## À propos de cet exemple {#about-this-example}

Flash & Thread, une marque fictive de vêtements, crée des messages qui dépendent de réponses de contenu connecté, de variables de contexte Canvas ou de données de profil sous forme de tableaux d'objets. Déclencher de vrais appels API ou lancer des Campaigns à chaque itération ralentit le développement.

Ce modèle intègre un payload JSON simulé dans le corps du message, le stocke avec `capture`, puis l'analyse avec `json_parse` afin que Liquid puisse référencer des champs structurés dans la section **Preview**, sans appel de contenu connecté en direct, sans entrée Canvas déclenchée par API, ni envoi de test.

Utilisez ce modèle pendant le développement de vos messages. Il ne remplace pas les tests de bout en bout avec de vrais déclencheurs, des envois de test ou la [prévisualisation des parcours utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths) dans Canvas.

## Considérations {#considerations}

- Cette approche prend en charge l'aperçu du compositeur pendant le développement. Effectuez des envois de test et des vérifications en conditions réelles avant de lancer auprès de vos clients.
- Un bloc `capture` seul stocke le JSON sous forme de chaîne de caractères. Ne référencez les champs qu'après avoir appliqué **`json_parse`** — sinon l'aperçu peut rester vide.
- Le JSON fictif doit être valide. Un JSON invalide provoque l'échec de `json_parse` ou renvoie des structures inattendues.
- Supprimez ou retirez les blocs fictifs avant le lancement, ou protégez votre Liquid de production afin que les données fictives ne soient utilisées que dans l'aperçu (par exemple avec un indicateur de commentaire que vous supprimez avant la mise en production).
- Les extraits de code Liquid de cet article sont des exemples. Testez-les dans vos canaux et avec vos propres structures de payload.
- Pour le contenu connecté en production, supprimez le bloc fictif et utilisez votre tag d'URL en direct. Consultez [Effectuer un appel API]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call).

## Configuration {#setup}

Cet exemple simule une réponse de type contenu connecté pour une liste de produits, destinée à un e-mail qui boucle sur `listings`.

### Étape 1 : Capturer le JSON simulé dans le message {#step-1-capture-mock-json-in-the-message}

Utilisez `capture` pour stocker la chaîne JSON. Utilisez une syntaxe JSON valide à l'intérieur du bloc (guillemets doubles sur les clés et les valeurs de type chaîne de caractères).

{% raw %}
```liquid
{% capture mock_response %}
{
  "success": true,
  "listings": [
    {
      "id": 45731,
      "name": "Summit Trail Jacket",
      "image_url": "https://example.com/images/trail-jacket.png",
      "price": {
        "actual": "89.00",
        "currency": "USD"
      },
      "link": "https://example.com/products/trail-jacket",
      "product_category": "Outerwear",
      "properties": {
        "size": "L",
        "colour": "Navy",
        "limited_edition": false
      },
      "out_of_stock": false
    }
  ]
}
{% endcapture %}
```
{% endraw %}

### Étape 2 : Analyser le JSON avec json_parse {#step-2-parse-json-with-json_parse}

Assignez la structure analysée à une variable que vous référencerez dans le reste du message.

{% raw %}
```liquid
{% assign response_json = mock_response | json_parse %}
```
{% endraw %}

Sans `json_parse`, la notation par points sur la chaîne capturée (par exemple {% raw %}`{{ mock_response.listings }}`{% endraw %}) affiche généralement un résultat vide dans l'aperçu.

### Étape 3 : Référencer les champs analysés en Liquid {#step-3-reference-parsed-fields-in-liquid}

Parcourez le tableau analysé et affichez les champs comme vous le feriez pour une réponse d'API en direct.

{% raw %}
```liquid
{% for listing in response_json.listings %}
{{ listing.name }} — {{ listing.price.actual }} {{ listing.price.currency }}
{% endfor %}
```
{% endraw %}

Accédez à la section **Aperçu** dans le compositeur de messages et vérifiez que les champs s'affichent correctement.

### Étape 4 : Appliquer le même schéma à d'autres structures JSON {#step-4-apply-the-same-pattern-to-other-json-shapes}

Utilisez le même flux `capture` + `json_parse` pour simuler :

| Données à tester | Structure JSON simulée |
| --- | --- |
| Variables de contexte Canvas | Objet avec les clés de propriétés attendues par votre message |
| Tableau d'objets sur un profil | Tableau JSON d'objets avec les mêmes clés que votre attribut personnalisé |
| Réponse de contenu connecté | Exemple de JSON d'API enregistré à partir d'un appel précédent réussi |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Données à tester et structure JSON" }

Remplacez les variables simulées par du Liquid de production (variables de contexte Canvas, attributs personnalisés ou balises de contenu connecté) avant de lancer votre envoi.

## Articles connexes {#related-articles}

- [Envoyer des messages de test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages)
- [Prévisualiser les parcours utilisateur dans Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths)
- [Filtres Liquid avancés (`json_parse`)]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters)
- [Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [Tableau d'objets]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)
- [Variables de contexte]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables)