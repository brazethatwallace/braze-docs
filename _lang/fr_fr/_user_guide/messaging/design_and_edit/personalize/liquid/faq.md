---
nav_title: FAQ
article_title: Questions fréquemment posées
page_order: 12
description: "Cet article fournit des réponses aux questions fréquemment posées sur Liquid."
toc_headers: h2
---

# Questions fréquemment posées {#frequently-asked-questions}

> Sur cette page, vous trouverez des réponses aux questions fréquemment posées sur Liquid.

{% alert note %}
Braze ne prend pas actuellement en charge 100 % du Liquid de Shopify, mais seulement certaines parties que nous avons tenté de décrire dans notre documentation. Testez tous les messages utilisant Liquid avant de les envoyer afin de réduire le risque d'erreurs ou d'utilisation de Liquid non pris en charge.
{% endalert %}

## À propos de Liquid dans Braze {#about-liquid-in-braze}

### Comment utiliser les extraits de code Liquid dans Braze ? {#how-do-i-use-liquid-snippets-in-braze}

Dans de nombreux cas, vous pouvez intégrer des extraits de code Liquid en accédant à vos Campaigns ou Canvas, puis en insérant du Liquid dans la fenêtre modale de personnalisation, par exemple dans le corps d'un e-mail ou dans vos Segments.

#### Où puis-je en savoir plus ? {#where-can-i-learn-more}

Pour en savoir plus sur Liquid, consultez notre parcours guidé [Personnalisation dynamique avec Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid) sur Braze Learning. Vous pouvez également consulter la [bibliothèque de cas d'usage Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases) pour trouver de l'inspiration et une variété d'exemples de personnalisation utilisant Liquid.

### Quelle est la différence entre l'utilisation de Liquid et du contenu connecté pour la personnalisation ? {#whats-the-difference-between-using-liquid-and-connected-content-for-personalization}

Le contenu connecté de Braze est un exemple d'étiquette Liquid. Il est également utilisé pour la personnalisation, mais les données proviennent d'un endpoint externe plutôt que de données stockées dans Braze. Consultez notre section dédiée au [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) pour en savoir plus sur les possibilités de personnalisation de vos messages.

### Qu'est-ce que le templating Liquid ? {#what-is-liquid-templating}

C'est la manière la plus courante d'utiliser Liquid dans Braze. Le templating Liquid consiste à extraire des données du profil d'un utilisateur pour les insérer dans un message. Ces données peuvent aller du prénom de l'utilisateur aux événements personnalisés issus d'un message déclenché par un événement.

Consultez les [Étiquettes de personnalisation prises en charge]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) pour obtenir la liste complète des étiquettes Liquid prises en charge.

### L'utilisation de Liquid consomme-t-elle des points de donnée ? {#does-using-liquid-log-data-points}

Non.

## Étiquettes de personnalisation et sources de données {#personalization-tags-and-data-sources}

### Comment utiliser Liquid pour envoyer un message d'accueil personnalisé ? {#how-can-i-use-liquid-to-send-a-personalized-greeting}

Pour un message d'accueil personnalisé utilisant le prénom de l'utilisateur, vous pouvez extraire les attributs standard du profil utilisateur tels que {% raw %}`{{${first_name}}}` et `{{${last_name}}}`{% endraw %}.

Vous pouvez également utiliser une instruction Liquid {% raw %}`{% if X %}`{% endraw %} pour effectuer un rendu conditionnel basé sur n'importe quel critère, comme le jour de la semaine ou des attributs personnalisés. Pour plus d'informations sur les opérateurs Liquid pris en charge dans les instructions conditionnelles, consultez [Opérateurs]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/operators).

### Comment personnaliser un message en fonction de la localisation d'un utilisateur ? {#how-can-i-personalize-a-message-based-on-a-users-location}

{% raw %}
Il existe un attribut par défaut pour la localisation de l'utilisateur : `{{${most_recent_location}}}`.
{% endraw %}

{% raw %}
### Quelle est la différence entre {{campaign.${name}}} et {{campaign.${message_name}}} ? {#whats-the-difference-between-campaignname-and-campaignmessage_name}

`{{campaign.${name}}}` et `{{campaign.${message_name}}}` sont toutes deux des étiquettes de personnalisation Liquid prises en charge. Ces deux étiquettes font référence aux attributs de la Campaign. `{{campaign.${name}}}` désigne le nom de votre Campaign, et `{{campaign.${message_name}}}` est le nom de votre variante de message.
{% endraw %}

Pour l'utilisation dans les URL et les chaînes de requête (par exemple, lorsqu'un nom contient `%` ou des espaces), consultez [Noms de Campaign dans les URL]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#campaign-names-in-urls).

### Comment utiliser Liquid avec des objets imbriqués ? {#how-do-i-use-liquid-with-nested-objects}

Braze dispose d'une fonctionnalité intégrée qui génère du code Liquid pour les Segments pouvant être utilisés dans un message. Plus précisément, vous pouvez créer un segment correspondant à plusieurs critères au sein d'un objet.

Pour plus d'informations, consultez [Segmentation multicritères]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support#segmentation-behavior-with-arrays-of-objects).

### Comment utiliser les propriétés d'événement pour personnaliser un message déclenché par un événement ? {#how-do-i-use-event-attributes-to-personalize-a-message-that-an-event-is-triggering}

{% raw %}
Vous pouvez accéder aux propriétés des événements déclenchés par API avec l'étiquette `api_triggered_property` : `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### Braze prend-il en charge un tableau de tableaux en Liquid ? {#does-braze-support-an-array-of-arrays-in-liquid}

Liquid ne prend pas nativement en charge les tableaux de tableaux. Stockez les valeurs sous forme de tableau de chaînes de caractères séparées par des virgules et utilisez le filtre `split` pour les analyser au besoin.

## Variables et syntaxe {#variables-and-syntax}

### Comment affecter des variables avec Liquid ? {#how-do-i-assign-variables-with-liquid}

Vous pouvez créer et affecter des variables en utilisant l'étiquette `assign`. Cela crée une variable dans le composeur de messages qui peut également être référencée dans l'ensemble de votre message.

### Quand utiliser `assign` plutôt que `capture` ? {#when-should-i-use-assign-versus-capture}

`assign` et `capture` créent tous deux des variables Liquid, mais ils ont des usages différents :

- `assign` est destiné aux variables simples qui stockent une seule valeur, comme une valeur booléenne, un nombre ou une chaîne de caractères simple. Vous pouvez également appliquer un seul filtre sur la même ligne.
- `capture` est destiné au stockage d'un bloc de texte pouvant inclure plusieurs variables, chaînes de caractères ou expressions complexes.

Utilisez `capture` lorsque la valeur est trop complexe pour une seule instruction `assign`, comme des URL utilisant d'autres variables Liquid ou des attributs personnalisés en tant que paramètres. `capture` est également préféré lors de l'implémentation de variables Liquid dans le corps des appels de contenu connecté.

#### Exemples {#examples}

{% raw %}
```liquid
{% comment %}Use assign for custom attributes{% endcomment %}
{% assign name = {{custom_attribute.${first_name}}} %}
{% assign price = {{custom_attribute.${price}}} | plus: 0 %}

{% comment %}Use assign for a simple variable{% endcomment %}
{% assign discount_label = "20% off" %}
Hello {{ customer.first_name | default: "there" }}, enjoy {{ discount_label }} on your next order!

{% comment %}Use capture for complex strings{% endcomment %}
{% capture greeting %}Hello, {{custom_attribute.${first_name}}}! Your order #{{custom_attribute.${order_id}}} is ready.{% endcapture %}
{{ greeting }}

{% comment %}Use capture to create conditional content{% endcomment %}
{% capture promo_block %}
{% if customer.vip == true %}
As a VIP member, you get free shipping.
{% else %}
Join our VIP program to unlock free shipping.
{% endif %}
{% endcapture %}
```
{% endraw %}

### Les variables Liquid sont-elles partagées entre la ligne d'objet et le corps du message ? {#do-liquid-variables-carry-between-subject-line-and-body}

Non. Braze effectue le rendu de chaque composant du message séparément (ligne d'objet, corps HTML, accroche, titre push, etc.). Les affectations ou captures que vous effectuez dans un champ ne sont pas disponibles dans un autre. Répétez l'appel Liquid ou de contenu connecté dans chaque champ qui nécessite la valeur.

### Qu'est-ce que la logique de boucle for et comment l'utiliser ? {#what-is-for-loop-logic-and-how-can-i-use-it}

Les boucles for sont également connues sous le nom d'[étiquettes d'itération](https://shopify.github.io/liquid/tags/iteration/). L'utilisation de la logique de boucle for dans vos extraits de code Liquid vous permet de parcourir des blocs Liquid jusqu'à ce qu'une condition soit remplie.

Dans Braze, cela peut être utilisé pour vérifier des éléments dans un attribut personnalisé de type tableau, ou une liste de valeurs et d'objets renvoyés par un appel de [catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs), de [sélection]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) ou de [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content). Plus précisément, vous pouvez utiliser la logique de boucle for dans vos messages pour vérifier si un produit est en stock ou s'il a une note minimale.

Par exemple, supposons que vous ayez un catalogue appelé « Games » avec une sélection appelée « cheap_games ». Pour extraire les titres des jeux dans « cheap_games », vous pouvez utiliser cet extrait de code Liquid :

{% raw %}
```liquid
{% catalog_selection_items Games cheap_games %}
{% for item in items %}
 Get this game: {{ item.title }}
{% endfor %}
```
{% endraw %}

Une fois les conditions définies remplies, votre message peut être envoyé. Cette logique est un moyen pratique de gagner du temps, plutôt que de répéter des blocs Liquid pour différentes conditions.

### Qu'est-ce que la logique d'abandon et comment l'utiliser ? {#what-is-abort-logic-and-how-can-i-use-it}

La logique d'abandon vous permet d'empêcher l'envoi d'un message si les conditions sont remplies. Cela est particulièrement utile pour éviter d'envoyer des messages incomplets à vos utilisateurs. Pour des exemples de logique d'abandon dans vos campagnes marketing, consultez [Abandon de messages]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages).

### Puis-je utiliser Liquid à l'intérieur de l'étiquette `abort_message` ? {#can-i-use-liquid-inside-the-abort_message-tag}

Non. L'étiquette {% raw %}`{% abort_message %}`{% endraw %} accepte une chaîne de caractères statique entre guillemets, pas de personnalisation Liquid. Utilisez d'autres logiques Liquid avant l'étiquette si vous avez besoin d'un comportement d'abandon conditionnel.

### Comment masquer des numéros de téléphone avec Liquid ? {#how-do-i-mask-phone-numbers-with-liquid}

Vous pouvez masquer des numéros de téléphone en utilisant le filtre `slice` pour extraire des chiffres spécifiques et le filtre `append` pour les combiner avec des caractères de masquage.

#### Masquer tous les chiffres sauf les quatre derniers {#mask-all-but-the-last-four-digits}

Pour afficher un numéro de téléphone à 10 chiffres sous la forme `******7890` :

{% raw %}
```liquid
{% assign phone = {{${phone_number}}} | split: '' %}
{% assign masked_phone = '' %}
{% for i in (0..5) %}
  {% assign masked_phone = masked_phone | append: '*' %}
{% endfor %}
{% for i in (6..9) %}
  {% assign masked_phone = masked_phone | append: phone[i] %}
{% endfor %}
{{ masked_phone }}
```
{% endraw %}

#### Afficher les trois premiers et les quatre derniers chiffres {#show-the-first-three-and-last-four-digits}

Pour afficher un numéro de téléphone à 10 chiffres sous la forme `123***7890` :

{% raw %}
```liquid
{% assign first_part = {{${phone_number}}} | slice: 0, 3 %}
{% assign last_part = {{${phone_number}}} | slice: -4, 4 %}
{% assign masked_phone_number = first_part | append: "***" | append: last_part %}
{{ masked_phone_number }}
```
{% endraw %}

## Canvas, catalogues et propriétés de déclenchement {#canvas-catalogs-and-trigger-properties}

### Pourquoi mon Liquid déclenché par API échoue-t-il dans Braze ? {#why-is-my-api-triggered-liquid-failing-in-braze}

{% raw %}
Une paire d'accolades supplémentaire est une cause fréquente. Par exemple, `{{{api_trigger_properties.${attribute_key}}}}` n'est pas une syntaxe de personnalisation Braze valide. Utilisez exactement deux accolades ouvrantes et deux accolades fermantes : `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### Existe-t-il des limites de taille pour les propriétés de contexte Canvas ? {#are-there-size-limits-for-canvas-context-properties}

Braze n'impose pas de limite stricte sur les [propriétés de contexte Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties), mais maintenez les payloads en dessous d'environ 1 Ko (~1 000 caractères). Des objets plus volumineux peuvent augmenter l'utilisation de la mémoire et retarder le rendu des messages lors d'envois à fort volume.

### Pourquoi est-ce que j'obtiens une erreur Liquid lors de la prévisualisation de certains types de données dans le tableau de bord ? {#why-do-i-get-a-liquid-error-when-previewing-certain-data-types-in-the-dashboard}

Certains types de [propriétés de contexte Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) nécessitent une conversion en Liquid avant de les utiliser dans des comparaisons ou des calculs. Par exemple, lorsque vous avez besoin d'un comportement numérique :

{% raw %}
```liquid
{{context.${property_name} | plus: 0}}
```
{% endraw %}

### Pourquoi mon extrait de code Liquid de catalogue renvoie-t-il un message d'abandon ? {#why-does-my-catalog-liquid-snippet-return-an-abort-message}

Si un extrait de code Liquid de catalogue s'interrompt lors de l'envoi, recréez l'extrait depuis le menu de personnalisation en sélectionnant des éléments de catalogue individuels au lieu d'utiliser une sélection en masse ou entièrement dynamique. Consultez [Catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs) et [Sélections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections).

## Content Blocks et le composeur de messages {#content-blocks-and-the-message-composer}

### Pourquoi y a-t-il des espaces supplémentaires dans les messages utilisant des Content Blocks ? {#why-is-there-extra-spacing-in-messages-that-use-content-blocks}

Si vous remarquez des espaces supplémentaires dans les messages envoyés qui utilisent des Content Blocks avec Liquid, il se peut que vous ayez des sauts de paragraphe ou de ligne inutiles dans vos instructions conditionnelles. Écrivez vos instructions conditionnelles sur une seule ligne plutôt que sur plusieurs lignes.

#### Exemple {#example}

{% raw %}
```liquid
{% if {{custom_attribute.${has_discount}}} == true %}Discounted Item{% elsif {{custom_attribute.${is_new_arrival}}} == true %}New Arrival{% else %}Regular Item{% endif %}
```
{% endraw %}

### Pourquoi mon Content Block n'apparaît-il pas dans **Row** dans l'outil de recherche du glisser-déposer ? {#why-is-my-content-block-missing-from-row-in-the-drag-and-drop-search-tool}

Certains Content Blocks n'apparaissent pas sous **Row** dans la recherche de l'éditeur glisser-déposer. Ajoutez un bloc HTML depuis l'onglet **Content** (**Advanced**), puis insérez l'étiquette Liquid du Content Block dans ce bloc HTML pour afficher le contenu du bloc.

### Pourquoi la prévisualisation de mon Content Block en glisser-déposer diffère-t-elle de la vue de composition ? {#why-does-my-drag-and-drop-content-block-preview-differ-from-the-compose-view}

Lorsque vous intégrez un Content Block avec Liquid via un modèle, les media queries mobiles du bloc peuvent ne pas s'appliquer de la même manière dans la prévisualisation que lorsque vous glissez le bloc directement dans un message. Glisser le bloc préserve la mise en page mais le découple du bloc source, de sorte que les modifications futures du bloc ne mettent plus automatiquement à jour le message.

### Comment prévisualiser les valeurs des propriétés d'événement dans le composeur de messages ? {#how-do-i-preview-event-property-values-in-message-composer}

Utilisez **Prévisualiser en tant qu'utilisateur personnalisé** et saisissez des exemples de valeurs de propriétés d'événement personnalisé pour l'utilisateur que vous prévisualisez. Cela est également utile pour les messages avec une logique d'abandon lorsque vous avez besoin de valeurs de prévisualisation qui ne déclenchent pas d'abandon.

## Liquid dans les e-mails {#liquid-in-email-messages}

### Pourquoi mon message s'interrompt-il avec « Invalid from email address for recipient: » ? {#why-does-my-message-abort-with-invalid-from-email-address-for-recipient}

Cet abandon se produit lorsque le Liquid dans l'adresse **De** produit une syntaxe invalide, comme une variable manquante, des espaces supplémentaires ou des caractères non autorisés. Prévisualisez avec un utilisateur test et vérifiez que l'adresse **De** rendue correspond à votre domaine d'envoi configuré.

### Comment créer une adresse de réponse dynamique ? {#how-do-i-create-a-dynamic-reply-to-address}

Utilisez Liquid dans le champ **Reply-To** lorsque votre espace de travail prend en charge la configuration dynamique de l'adresse de réponse. Associez-le à vos paramètres de nom d'affichage **De** selon vos besoins. Consultez [Paramètres des e-mails]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences) pour les options spécifiques à l'espace de travail.

## Résolution des erreurs Liquid {#troubleshooting-liquid-errors}

### Pourquoi est-ce que je vois une erreur Liquid « Unexpected end token » ? {#why-am-i-seeing-an-unexpected-end-token-liquid-error}

Cette erreur indique généralement des accolades en trop ou manquantes. N'imbriquez pas {% raw %}`{{ }}`{% endraw %} à l'intérieur d'une autre expression d'étiquette Liquid. Par exemple, utilisez {% raw %}`{{custom_attribute.${date_of_birth} | date: '%s'}}`{% endraw %} plutôt que d'envelopper la référence d'attribut dans une paire d'accolades supplémentaire.

### Pourquoi la relance du contenu connecté n'est-elle pas disponible pour mon message in-app ? {#why-is-connected-content-retry-unavailable-for-my-in-app-message}

{% raw %}
L'étiquette `{% connected_content %}` avec relance n'est pas prise en charge pour tous les types de messages, y compris certains formats de messages in-app. Supprimez les paramètres de relance ou utilisez un canal pris en charge pour les appels de contenu connecté avec relance.
{% endraw %}