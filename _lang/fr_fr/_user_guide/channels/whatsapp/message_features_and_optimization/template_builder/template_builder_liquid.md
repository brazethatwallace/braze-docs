---
nav_title: Liquid
article_title: Liquid dans le générateur de modèles WhatsApp
description: "Cet article de référence couvre les Message Extras et la logique conditionnelle Liquid dans le générateur de modèles WhatsApp."
alias: /whatsapp_template_builder_liquid/
page_type: reference
channel:
  - WhatsApp
page_order: 1
---

# Liquid dans le générateur de modèles WhatsApp {#liquid-in-the-whatsapp-template-builder}

> Vous pouvez utiliser Liquid pour personnaliser les modèles dans le générateur de modèles WhatsApp, mais la structure de modèles de Meta crée des contraintes qui n'existent pas dans les autres canaux Braze. Deux cas d'utilisation de Liquid en particulier nécessitent un traitement spécial : les Message Extras et la logique conditionnelle d'envoi de messages.

Pour les Message Extras et la logique conditionnelle d'envoi de messages, Meta exige que chaque variable d'un modèle contienne du contenu réellement rendu au moment de l'envoi. Les variables qui renvoient des chaînes de caractères vides, ou qui se comportent comme des métadonnées invisibles plutôt que du texte visible, provoquent des échecs d'envoi. Les conditions qui modifient la structure statique du message plutôt que le seul contenu de la variable entraînent également un comportement inattendu.

{% alert note %}
Les contraintes décrites dans cet article s'appliquent uniquement aux messages de modèle (messages sortants utilisant un modèle approuvé par Meta). Elles ne s'appliquent pas aux messages de réponse (envoyés dans une fenêtre de messagerie de 24 heures ouverte par un utilisateur), ni aux Message Extras, à la logique conditionnelle et aux autres cas d'utilisation de Liquid dans les autres canaux Braze.
{% endalert %}

## Aperçu {#overview}

| Cas d'utilisation | Pris en charge ? | Notes |
| ----- | ----- | ----- |
| `message_extras` dans une variable avec d'autres contenus visibles | ✅ Oui | L'étiquette est capturée ; le texte visible satisfait l'exigence de contenu de variable de Meta |
| `message_extras` comme seul contenu d'une variable | ❌ Non | Se résout en chaîne vide ; provoque un échec d'envoi |
| Liquid conditionnel dans un emplacement de variable | ✅ Oui | Braze évalue avant l'envoi ; Meta ne voit que la valeur finale rendue |
| Liquid conditionnel en dehors d'un emplacement de variable | ❌ Non | Les étiquettes Liquid sont rendues comme du texte littéral ; le destinataire voit la syntaxe brute |
| Modèle commençant ou se terminant par un emplacement de variable | ❌ Non | Meta exige du texte statique au début et à la fin de chaque modèle |
| Emplacement de variable qui se résout en chaîne vide | ❌ Non | Meta exige un contenu non vide dans chaque variable au moment de l'envoi |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Référence rapide" }

## Message Extras {#message-extras}

L'[étiquette Liquid `message_extras`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras) vous permet d'annoter un message avec des métadonnées clé-valeur au moment de l'envoi. Ces données ne sont pas rendues dans le corps du message. Elles sont transmises au Contenu connecté, à Currents ou à d'autres mécanismes de capture de données à des fins d'attribution, de mesure d'impact et d'enrichissement d'événements.

{% raw %}
```liquid
{% message_extras :key campaign_id :value "spring_promo_2025" %}
```
{% endraw %}

### Pourquoi les variables Message Extras autonomes échouent {#why-standalone-message-extras-variables-fail}

Dans le générateur de modèles WhatsApp, les variables de modèle (telles que {% raw %}`{{1}}`, `{{2}}`{% endraw %}) correspondent directement à des expressions Liquid. La validation de Meta exige que chaque emplacement de variable dans le modèle approuvé contienne un contenu non vide au moment de l'envoi ; il doit s'agir de quelque chose qui s'affiche comme du texte visible pour le destinataire.

Comme `message_extras` ne produit aucune sortie, le placer seul dans une variable de modèle soumet une chaîne vide pour cet emplacement de variable. Meta rejette cela, et l'envoi du message échoue.

{% details Utilisation incorrecte pour le générateur de modèles WhatsApp %}

{% raw %}
```
Template variable {{1}}: {% message_extras :key attribution_source :value "canvas_a" %}
```
{% endraw %}

Au moment de l'envoi, {% raw %}`{{1}}`{% endraw %} se résout en chaîne vide, provoquant un échec d'envoi.

{% enddetails %}

### Utilisation correcte {#correct-usage}

Pour inclure correctement une étiquette `message_extras`, intégrez-la dans une variable existante. Cela signifie placer l'étiquette dans un bloc Liquid qui produit une sortie visible ; plus précisément, dans la même expression qui alimente une vraie variable de modèle. Meta accepte la variable car elle contient du contenu, Braze capture les métadonnées, et le destinataire ne voit que le texte rendu.

#### Exemple {#example}

Supposons que le corps du modèle soit :

{% raw %}
```
Hi {{1}}, your order has shipped.
```
{% endraw %}

Et que la variable {% raw %}`{{1}}`{% endraw %} soit associée à :

{% raw %}
```
{{ ${first_name} | default: "there" }}
```
{% endraw %}

Pour joindre un Message Extra, réécrivez l'expression de la variable ainsi :

{% raw %}
```
{{ ${first_name} | default: "there" }}{% message_extras :key order_source :value "canvas_spring" %}
```
{% endraw %}

Au moment de l'envoi, {% raw %}`{{1}}`{% endraw %} se résout en quelque chose comme `"Alex"`, un contenu visible qui satisfait l'exigence de Meta. L'étiquette `message_extras` est évaluée et ses données sont capturées, mais elle ne contribue en rien à la chaîne rendue que le destinataire voit.

### Règles clés {#key-rules}

- N'affectez jamais `message_extras` comme seul contenu d'une variable de modèle.
- Joignez toujours l'étiquette à une variable qui se résout en texte visible.
- Vous pouvez ajouter plusieurs étiquettes `message_extras` à la même expression de variable sans affecter la sortie rendue.
- Utilisez ce modèle dans le corps, l'en-tête et tout autre emplacement de variable.

## Logique conditionnelle d'envoi de messages {#conditional-messaging-logic}

Dans les canaux de communication, les blocs Liquid `if/elsif/else` peuvent inclure ou exclure conditionnellement des sections entières de texte. Braze rend la sortie Liquid complète avant l'envoi, et le résultat est ce que la logique produit.

Cependant, les modèles WhatsApp approuvés par Meta ont une structure fixe. Meta considère le contenu des modèles en deux catégories :

- **Texte statique :** chaînes codées en dur qui sont confirmées à la création du modèle et restent identiques pour chaque destinataire.
- **Emplacements de variable :** positions de marque substitutive (telles que {% raw %}`{{1}}`{% endraw %}) dont le contenu est rempli au moment de l'envoi.

### Pourquoi la logique conditionnelle en dehors d'un emplacement de variable échoue {#why-conditional-messaging-logic-outside-a-variable-slot-fails}

Le ratio entre texte statique et emplacements de variable dans un modèle approuvé est fixe, ne peut pas changer par envoi et comporte des limites strictes. Meta exige un minimum de texte statique pour chaque emplacement de variable dans le modèle ; vous ne pouvez pas avoir un modèle composé principalement ou entièrement de variables. Cela signifie que vous ne pouvez pas inclure de Liquid conditionnel qui ajoute ou supprime du texte que Meta considère comme du contenu statique confirmé.

Si vous essayez d'utiliser un bloc `if/else` pour inclure ou exclure conditionnellement un bloc de texte statique, Meta n'évalue pas la logique. Les étiquettes Liquid en dehors d'un emplacement de variable sont traitées comme du texte littéral en sortie. Le destinataire voit les étiquettes de syntaxe Liquid brutes ({% raw %}`{% if %}`, `{% else %}`, `{% endif %}`{% endraw %}) et tout le contenu des branches tel quel dans son message.

{% details Utilisation incorrecte pour le générateur de modèles WhatsApp %}

{% raw %}
```
{% if ${loyalty_tier} == "gold" %}Hi {{1}}, we have an exclusive Gold member offer.{% else %}Hi {{1}}, we have a special offer for you.{% endif %}
```
{% endraw %}

Cela tente d'inclure deux modèles approuvés différents en un seul. L'encapsulation conditionnelle du texte statique ne se comportera pas comme prévu.

{% enddetails %}

### Utilisation correcte

Les conditions sont valides et prises en charge à l'intérieur d'un emplacement de variable, où elles contrôlent la valeur qui remplit cette variable. Meta voit uniquement que {% raw %}`{{1}}`{% endraw %} a été rempli avec du contenu ; il n'inspecte pas comment le Liquid interne est arrivé à cette valeur.

#### Exemple

{% raw %}
```
{% if ${loyalty_tier} == "gold" %}exclusive Gold member{% else %}valued customer{% endif %}
```
{% endraw %}

Utilisé comme valeur d'une variable de modèle, cela produit soit `"exclusive Gold member"` soit `"valued customer"`. Les deux sont des chaînes non vides qui satisfont l'exigence de contenu de variable de Meta.

Le corps du modèle lui-même reste structurellement inchangé :

{% raw %}
```
Hi {{1}}, we have a special offer for you.
```
{% endraw %}

### Placer la logique conditionnelle dans un emplacement de variable {#place-conditional-logic-inside-a-variable-slot}

Il existe deux façons de placer du Liquid conditionnel dans un emplacement de variable dans le générateur de modèles :

1. **Utiliser un Content Block (prend en charge le préremplissage) :** construisez votre logique conditionnelle dans un Content Block, puis référencez le bloc depuis la variable. Cette approche prend en charge le préremplissage, ce qui signifie que la variable peut afficher une valeur d'aperçu dans le générateur de modèles avant l'envoi.
2. **Utiliser une marque substitutive et coller du Liquid (pas de préremplissage) :** ajoutez une marque substitutive comme {% raw %}`{{1}}`{% endraw %} lors de la création du modèle, puis collez votre expression Liquid complète directement dans cet emplacement de variable. Cette approche ne prend pas en charge le préremplissage, mais elle fonctionne pour toute logique Liquid.

### Autres composants Liquid affectés par la même contrainte {#other-liquid-components-affected-by-the-same-constraint}

Toute étiquette Liquid qui ne produit pas de sortie visible est rendue comme du texte brut si elle est placée en dehors d'une variable. Cela inclut :

- **`catalog_items` :** le Liquid qui recherche et référence des données de Catalogue doit se trouver à l'intérieur d'un emplacement de variable, sinon les étiquettes apparaissent telles quelles dans le message.
- **`assign` :** les étiquettes d'affectation de variable (telles que {% raw %}{% assign discount = "20%" %}{% endraw %}) ne produisent pas de sortie par elles-mêmes. Si elles sont utilisées en dehors d'un emplacement de variable pour définir une valeur destinée à être utilisée plus tard dans le message, l'étiquette `assign` s'affiche littéralement. Incluez toute logique `assign` au début de l'expression Liquid à l'intérieur de l'emplacement de variable où sa sortie est nécessaire.
- **Content Blocks contenant uniquement des étiquettes Liquid :** si un Content Block contient de la logique Liquid mais ne produit pas de texte visible (par exemple, il utilise uniquement des étiquettes `assign` ou `message_extras`), le référencer en dehors d'un emplacement de variable fait apparaître le contenu brut du bloc dans le message. Les Content Blocks qui ne produisent pas de sortie visible doivent être intégrés dans un emplacement de variable aux côtés de contenu qui s'affiche.

### Contraintes structurelles supplémentaires {#additional-structural-constraints}

Meta exige que les modèles :

- **Commencent par du texte statique.** Les modèles ne peuvent pas s'ouvrir avec un emplacement de variable (tel que {% raw %}`{{1}} is ready for you`{% endraw %}).
- **Se terminent par du texte statique.** Les modèles ne peuvent pas se terminer par un emplacement de variable.

Ces contraintes existent indépendamment de l'utilisation de Liquid. Elles s'appliquent à la structure du modèle approuvé elle-même.

### Règles clés

- Utilisez librement les conditions à l'intérieur des expressions d'emplacement de variable pour contrôler la valeur rendue.
- N'utilisez pas de conditions pour ajouter, supprimer ou permuter du texte statique (les parties du message qui ne sont pas des emplacements de variable).
- Assurez-vous que chaque branche conditionnelle à l'intérieur d'une variable produit une chaîne non vide (voir [Message Extras](#message-extras) pour comprendre pourquoi les chaînes vides provoquent des échecs).
- Le modèle doit commencer et se terminer par du texte statique tel que soumis à Meta.