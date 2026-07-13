---
nav_title: Tutoriels
article_title: "Tutoriels : Écrire du code Liquid"
page_order: 11
description: "Cette page de référence contient des tutoriels adaptés aux débutants pour vous aider à démarrer avec le code Liquid."
page_type: tutorial
---

# Tutoriels : Écrire du code Liquid {#tutorials-writing-liquid-code}

> Vous débutez avec Liquid ? Ces tutoriels vous aideront à démarrer l'écriture de code Liquid pour des cas d'usage adaptés aux débutants. Chaque tutoriel couvre une combinaison différente d'objectifs d'apprentissage, tels que la logique conditionnelle et les opérateurs.

À la fin de ces tutoriels, vous serez en mesure de :

- Écrire du code Liquid pour des cas d'usage courants
- Enchaîner de la logique conditionnelle Liquid pour personnaliser les messages en fonction des données utilisateur
- Utiliser des variables et des filtres pour écrire des équations qui exploitent les valeurs des attributs
- Reconnaître les commandes de base dans le code Liquid et comprendre de manière générale ce que fait le code

| Tutoriel | Objectifs d'apprentissage |
| --- | --- |
| [Personnaliser les messages par segments d'utilisateurs](#segments) | valeurs par défaut, logique conditionnelle |
| [Rappels de panier abandonné](#reminders) | opérateurs, logique conditionnelle |
| [Compte à rebours d'événement](#countdown) | variables, filtres de date |
| [Message d'anniversaire mensuel](#birthday) | variables, filtres de date, opérateurs |
| [Promouvoir un produit favori](#favorite-product) | variables, filtres de date, équations, opérateurs |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Tutoriels : Écrire du code Liquid" }

## Messages personnalisés par segments d'utilisateurs {#segments}

Personnalisons les messages pour différents segments d'utilisateurs, comme les clients VIP et les nouveaux utilisateurs abonnés.

1. Ouvrez le message avec des salutations personnalisées à envoyer selon que vous disposez ou non du prénom de l'utilisateur. Pour cela, créez une étiquette Liquid qui inclut l'attribut `first_name` et une valeur par défaut à utiliser si `first_name` est vide. Dans ce scénario, utilisons « traveler » comme valeur par défaut.

{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
```
{% endraw %}

{: start="2"}
2. Maintenant, définissons le message à envoyer si l'utilisateur est un client VIP. Nous aurons besoin d'une étiquette de logique conditionnelle pour cela : `if`. Cette étiquette indique que si l'attribut personnalisé `vip_status` est égal à `VIP`, le code Liquid suivant sera exécuté. Dans ce cas, un message spécifique sera envoyé.

{% raw %}
```liquid
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
```
{% endraw %}

{: start="3"}
3. Envoyons un message personnalisé pour les utilisateurs qui sont de nouveaux utilisateurs abonnés. Nous utiliserons l'étiquette de logique conditionnelle `elsif` pour spécifier que si le `vip_status` de l'utilisateur est `new`, le message suivant sera envoyé.

{% raw %}
```liquid
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
```
{% endraw %}

{: start="4"}
4. Qu'en est-il des utilisateurs qui ne sont ni VIP ni nouveaux ? Nous pouvons envoyer un message à tous les autres utilisateurs avec l'étiquette `else`, qui spécifie que le message suivant doit être envoyé si les conditions précédentes ne sont pas remplies. Ensuite, nous pouvons fermer la logique conditionnelle avec l'étiquette `endif`, car il n'y a plus d'autres statuts VIP à considérer.

{% raw %}
```liquid
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}

{% details Code Liquid complet %}
{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}
{% enddetails %}

## Rappels de panier abandonné {#reminders}

Envoyons des messages personnalisés pour rappeler aux utilisateurs les articles laissés dans leur panier. Nous les personnaliserons davantage en fonction du nombre d'articles dans le panier : s'il y en a trois ou moins, nous les listerons tous. S'il y en a plus de trois, nous enverrons un message plus concis.

1. Vérifions si le panier de l'utilisateur est vide en ouvrant une logique conditionnelle Liquid avec l'opérateur `!=`, qui signifie « n'est pas égal à ». Ici, nous définirons la condition pour que l'attribut personnalisé `cart_items` ne soit pas égal à une valeur vide.

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
```
{% endraw %}

{: start="2"}
2. Nous devrons ensuite affiner notre vérification et déterminer si le panier contient plus de trois articles en utilisant l'opérateur `>`, qui signifie « supérieur à ».

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
```
{% endraw %}

{: start="3"}
3. Rédigez un message qui salue l'utilisateur par son prénom, ou si celui-ci n'est pas disponible, utilisez « there » comme valeur par défaut. Précisez ce qui doit être affiché s'il y a plus de trois articles dans le panier. Comme nous ne voulons pas submerger l'utilisateur avec une liste complète, listons les trois premiers `cart_items`.

{% raw %}
```liquid
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
```
{% endraw %}

{: start="4"}
4. Utilisez l'étiquette `else` pour spécifier ce qui doit se passer si les conditions précédentes ne sont pas remplies (autrement dit, si `cart_items` est vide ou contient moins de trois articles), puis fournissez le message à envoyer. Comme trois articles ne prennent pas beaucoup de place, nous pouvons tous les lister. Nous utiliserons l'opérateur Liquid `join` et `,` pour spécifier que les articles doivent être listés avec une virgule comme séparateur. Fermez la logique avec `endif`.

{% raw %}
```liquid
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you.
{% endif %}
```
{% endraw %}

{: start="5"}
5. Utilisez `else` puis un `abort_message` pour indiquer au code Liquid de ne pas envoyer de message si le panier ne remplit aucune des conditions précédentes. Autrement dit, si le panier est vide. Fermez la logique avec `endif`.

{% raw %}
```liquid
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}

{% details Code Liquid complet %}
{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you.
{% endif %}
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}
{% enddetails %}

## Compte à rebours d'événement {#countdown}

Envoyons aux utilisateurs un message indiquant combien de jours il reste avant une vente anniversaire. Pour cela, nous utiliserons des variables afin de créer des équations qui manipulent les valeurs des attributs.

1. Tout d'abord, assignons la variable `sale_date` à l'attribut personnalisé `anniversary_date` et appliquons le filtre `date: "s"`. Cela convertit `anniversary_date` en un format d'horodatage exprimé en secondes, puis assigne cette valeur à `sale_date`.

{% raw %}
```liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
```
{% endraw %}

{: start="2"}
2. Nous devons également assigner une variable pour capturer l'horodatage d'aujourd'hui. Assignons la variable `today` à `now` (la date et l'heure actuelles), puis appliquons le filtre `date: "%s"`.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
```
{% endraw %}

{: start="3"}
3. Maintenant, calculons combien de secondes séparent le moment présent (`today`) de la vente anniversaire (`sale_date`). Pour cela, assignons la variable `difference` à la valeur de `sale_date` moins `today`.

{% raw %}
```liquid
{% assign difference =  event_date | minus: today %}
```
{% endraw %}

{: start="4"}
4. Nous devons maintenant convertir `difference` en une valeur exploitable dans un message, car il n'est pas idéal d'indiquer à l'utilisateur combien de secondes le séparent d'une vente. Assignons `difference_days` à `event_date` et divisons-le par `86400` pour obtenir le nombre de jours.

{% raw %}
```liquid
{% assign difference_days = difference | divided_by: 86400 %}
```
{% endraw %}

{: start="5"}
5. Enfin, créons le message à envoyer.

{% raw %}
```liquid
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}

{% details Code Liquid complet %}
{% raw %}
```liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
{% assign today =  'now' | date: "%s"  %}
{% assign difference =  event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}
{% enddetails %}

## Message d'anniversaire mensuel {#birthday}

Envoyons une promotion spéciale à tous les utilisateurs dont l'anniversaire tombe dans le mois en cours. Les utilisateurs dont l'anniversaire ne tombe pas ce mois-ci ne recevront aucun message.

1. Tout d'abord, récupérons le mois en cours. Nous assignerons la variable `this_month` à `now` (la date et l'heure actuelles), puis utiliserons le filtre `date: "%B"` pour spécifier que la variable doit correspondre au mois.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
```
{% endraw %}

{: start="2"}
2. Maintenant, récupérons le mois de naissance à partir de la `date_of_birth` de l'utilisateur. Nous assignerons la variable `birth_month` à `date_of_birth`, puis utiliserons le filtre `date: "%B"`.

{% raw %}
```liquid
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
```
{% endraw %}

{: start="3"}
3. Maintenant que nous avons deux variables dont la valeur est un mois, nous pouvons les comparer avec de la logique conditionnelle. Définissons la condition pour que `this_month` soit égal au `birth_month` de l'utilisateur.

{% raw %}
```liquid
{% if {{this_month}} == {{birth_month}} %}
```
{% endraw %}

{: start="4"}
4. Créons le message à envoyer si ce mois est aussi le mois de naissance de l'utilisateur.

{% raw %}
```liquid
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
```
{% endraw %}

{: start="5"}
5. Utilisez l'étiquette `else` pour spécifier ce qui se passe si la condition n'est pas remplie (car ce mois n'est pas le mois de naissance de l'utilisateur).

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="6"}
6. Nous ne voulons pas envoyer de message si le mois de naissance de l'utilisateur n'est pas le mois en cours, nous utiliserons donc `abort_message` pour annuler le message, puis fermerons la logique conditionnelle avec `endif`.

{% raw %}
```liquid
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}

{% details Code Liquid complet %}
{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
{% if {{this_month}} == {{birth_month}} %}
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
{% else %}
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}
{% enddetails %}

## Promotion du produit favori {#favorite-product}

Promouvons le produit favori d'un utilisateur si son dernier achat remonte à plus de six mois.

1. Tout d'abord, nous utiliserons de la logique conditionnelle pour vérifier si nous disposons du produit favori et de la dernière date d'achat de l'utilisateur.

{% raw %}
```liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
```
{% endraw %}

{: start="2"}
2. Ensuite, nous indiquerons que si nous ne disposons pas du produit favori ou de la dernière date d'achat de l'utilisateur, aucun message ne doit être envoyé.

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="3"}
3. Nous utiliserons `else` pour spécifier ce qui doit se passer si la condition ci-dessus n'est pas remplie (car nous _disposons_ du produit favori et de la dernière date d'achat de l'utilisateur).

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="4"}
4. Si nous disposons de la date d'achat, nous devons l'assigner à une variable afin de pouvoir la comparer à la date du jour. Tout d'abord, créons une valeur pour la date du jour en assignant la variable `today` à `now` (la date et l'heure actuelles) et en utilisant le filtre `date: "%s"` pour convertir la valeur en un format d'horodatage exprimé en secondes. Nous ajouterons le filtre `plus: 0` pour ajouter un « 0 » à l'horodatage. Cela ne modifie pas la valeur de l'horodatage, mais s'avère utile pour l'utiliser dans de futures équations.

{% raw %}
```liquid
{% assign today = 'now' | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="5"}
5. Maintenant, capturons la dernière date d'achat en secondes en assignant la variable `last_purchase_date` à l'attribut personnalisé `last_purchase_date` et en utilisant le filtre `date: "s"`. Nous ajouterons à nouveau le filtre `plus: 0`.

{% raw %}
```liquid
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="6"}
6. Comme la dernière date d'achat et la date du jour sont en secondes, nous devrons calculer combien de secondes représentent six mois. Créons une équation (environ 6 mois × 30,44 jours × 24 heures × 60 minutes × 60 secondes) et assignons-la à la variable `six_months`. Nous utiliserons `times` pour spécifier la multiplication des unités de temps.

{% raw %}
```liquid
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
```
{% endraw %}

{: start="7"}
7. Maintenant que toutes nos valeurs temporelles sont en secondes, nous pouvons les utiliser dans des équations. Assignons une variable appelée `today_minus_last_purchase_date` qui prend la valeur d'aujourd'hui et en soustrait `last_purchase_date`. Cela nous donne le nombre de secondes écoulées depuis le dernier achat.

{% raw %}
```liquid
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
```
{% endraw %}

{: start="8"}
8. Comparons maintenant directement nos valeurs temporelles dans la logique conditionnelle. Définissons la condition pour que `today_minus_last_purchase_date` soit supérieur ou égal (`>=`) à six mois. Autrement dit, le dernier achat remonte à au moins six mois.

{% raw %}
```liquid
{% if today_minus_last_purchase_date >= six_months %}
```
{% endraw %}

{: start="9"}
9. Créons le message à envoyer si le dernier achat remonte à au moins six mois.

{% raw %}
```liquid
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
```
{% endraw %}

{: start="10"}
10. Nous utiliserons l'étiquette `else` pour spécifier ce qui doit se passer si la condition n'est pas remplie (car l'achat ne remonte pas à au moins six mois).

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="11"}
11. Nous inclurons un `abort_message` pour annuler le message.

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="12"}
12. Pour terminer, nous fermerons le code Liquid avec deux étiquettes `endif`. La première `endif` ferme la vérification conditionnelle du produit favori ou de la dernière date d'achat, et la seconde `endif` ferme la vérification conditionnelle pour savoir si le dernier achat remonte à au moins six mois.

{% raw %}
```liquid
{% endif %}
{% endif %}
```
{% endraw %}

{% details Code Liquid complet %}
{% raw %}
```liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
{% abort_message("No favorite product or last purchase date") %}
{% else %}
{% assign today = 'now' | date: "%s" | plus: 0 %}
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
{% if today_minus_last_purchase_date >= six_months %}
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
{% else %}
{% abort_message("Last purchase was less than six months ago") %}
{% endif %}
{% endif %}
```
{% endraw %}
{% enddetails %}