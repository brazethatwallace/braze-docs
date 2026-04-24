---
nav_title: Propriétés d'entrée persistantes
article_title: Propriétés d'entrée persistantes
alias: "/persistent_entry/"
page_type: reference
description: "Cet article de référence explique comment utiliser les propriétés d'entrée persistantes dans votre Canvas pour envoyer des messages plus ciblés et offrir une expérience utilisateur hautement personnalisée."
tool: Canvas
page_order: 5
---

# Propriétés d'entrée persistantes

> Lorsqu'un Canvas est déclenché par un événement personnalisé, un achat ou un appel API, vous pouvez utiliser les métadonnées de l'appel API, de l'événement personnalisé ou de l'événement d'achat pour la personnalisation de chaque étape de votre workflow Canvas. Ces propriétés vous permettent d'envoyer des messages plus ciblés.

{% alert important %}
Les propriétés d'entrée persistantes sont un vestige de l'éditeur Canvas d'origine. Certaines références obsolètes à des termes comme « propriétés d'entrée Canvas » subsistent à titre historique. Pour l'éditeur Canvas actuel mis à jour, consultez [Propriétés de contexte et d'événement]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/).
{% endalert %}

## Utiliser les propriétés d'entrée

Les propriétés d'entrée peuvent être utilisées dans les Canvas déclenchés par une action et par l'API. Ces propriétés d'entrée sont définies lorsqu'un Canvas est déclenché par un événement personnalisé, un achat ou un appel API. Consultez les articles suivants pour en savoir plus :

- [Objet des propriétés d'entrée Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/)
- [Objet des propriétés d'événement]({{site.baseurl}}/api/objects_filters/event_object/)
- [Objet d'achat]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-product_id)

Les propriétés transmises par ces objets peuvent être référencées à l'aide de l'étiquette Liquid `canvas_entry_properties`. Par exemple, une requête contenant `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}` pourrait ajouter le mot « shoes » à un message en utilisant le Liquid {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}.

Lorsqu'un Canvas contient un message avec l'étiquette Liquid `canvas_entry_properties`, les valeurs associées à ces propriétés sont enregistrées pendant toute la durée du parcours de l'utilisateur dans le Canvas et supprimées lorsque l'utilisateur quitte le Canvas. Notez que les propriétés d'entrée Canvas sont uniquement disponibles pour référence dans Liquid. Pour filtrer sur les propriétés au sein du Canvas, utilisez plutôt la [segmentation par propriétés d'événement]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects/).

{% alert note %}
L'objet des propriétés d'entrée Canvas a une taille maximale de 50 Ko.
{% endalert %}

## Mettre à jour un Canvas pour utiliser les propriétés d'entrée

Si un Canvas actif qui ne contenait auparavant aucun message utilisant `canvas_entry_properties` est modifié pour inclure `canvas_entry_properties`, la valeur correspondant à cette propriété ne sera pas disponible pour les utilisateurs qui sont entrés dans le Canvas avant l'ajout de `canvas_entry_properties`. Les valeurs ne seront enregistrées que pour les utilisateurs qui entrent dans le Canvas après la modification.

Par exemple, si vous avez initialement lancé un Canvas sans propriétés d'entrée le 3 novembre, puis ajouté une nouvelle propriété `product_name` au Canvas le 11 novembre, les valeurs de `product_name` ne seront enregistrées que pour les utilisateurs entrés dans le Canvas à partir du 11 novembre.

Si une propriété d'entrée Canvas est nulle ou vide, vous pouvez annuler les messages à l'aide de conditions. L'extrait de code suivant montre comment utiliser Liquid pour annuler un message.
{%raw%}
```
{% if canvas_entry_properties.${product_name} == blank %}
{% abort_message() %}
{% endif %}
```
{%endraw%}

Pour en savoir plus sur l'annulation de messages avec Liquid, consultez notre [documentation Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/#abort-messages).

## Propriétés d'entrée Canvas globales

Avec `canvas_entry_properties`, vous pouvez définir des propriétés globales qui s'appliquent à tous les utilisateurs, ou des propriétés spécifiques à un utilisateur qui ne s'appliquent qu'à l'utilisateur concerné. La propriété spécifique à l'utilisateur prévaut sur la propriété globale pour cet utilisateur.

### Exemple de requête

```
url -X POST \
-H 'Content-Type:application/json' \
-d '{
      "api_key": "a valid rest api key",
      "canvas_id": "the ID of your Canvas",
         "canvas_entry_properties": {
            "food_allergies": "none"
          },
      "recipients": [
        {
          "external_user_id": Customer_123,
          "canvas_entry_properties": {
            "food_allergies": ["dairy", "soy"],
            "nutrition": {
              "calories_per_serving": 200,
              "serving_size_in_ounces": 4
            }
          }
        }
      ]
    }' \
```
 
Dans cette requête, la valeur globale pour « food allergies » est « none ». Pour Customer_123, la valeur est « dairy ». Les messages de ce Canvas contenant l'extrait Liquid {%raw%}`{{canvas_entry_properties.${food_allergies}}}`{%endraw%} afficheront « dairy » pour Customer_123 et « none » pour tous les autres utilisateurs. 

## Cas d'utilisation

Imaginons que vous avez un Canvas déclenché lorsqu'un utilisateur consulte un article sur votre site e-commerce sans l'ajouter à son panier. La première étape du Canvas pourrait être une notification push lui demandant s'il souhaite acheter l'article. Vous pouvez référencer le nom du produit en utilisant {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}

![]({% image_buster /assets/img/persistent_entry_properties/PEP1.png %}){: style="border:0;margin-left:15px;"}

La deuxième étape peut envoyer une autre notification push invitant l'utilisateur à finaliser son achat s'il a ajouté l'article à son panier mais ne l'a pas encore acheté. Vous pouvez continuer à référencer la propriété d'entrée `product_name` en utilisant {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}.

![]({% image_buster /assets/img/persistent_entry_properties/PEP12.png %}){: style="border:0;margin-left:15px;"}