---
nav_title: Bibliothèque de cas d'utilisation Liquid
article_title: Bibliothèque de cas d'utilisation Liquid
page_order: 10
search_rank: 2
excerpt_separator: ""
page_type: glossary
layout: liquid_use_case_glossary
description: "Cette page regroupe des exemples de cas d'utilisation Liquid organisés par catégorie : anniversaires, utilisation de l'application, comptes à rebours, et bien plus encore."

---

{% api %}

## Anniversaires et jours fériés {#anniversaries-and-holidays}

{% apitags %}
Anniversaries and holidays
{% endapitags %}

- [Personnaliser les messages en fonction de l'année d'anniversaire d'inscription d'un utilisateur](#anniversary-year)
- [Personnaliser les messages en fonction de la semaine d'anniversaire d'un utilisateur](#birthday-week)
- [Envoyer des Campaigns aux utilisateurs pendant leur mois d'anniversaire](#birthday-month)
- [Éviter d'envoyer des messages lors des jours fériés importants](#holiday-avoid)

### Personnaliser les messages en fonction de l'année d'anniversaire d'inscription d'un utilisateur {#anniversary-year}

Ce cas d'utilisation montre comment calculer l'anniversaire d'inscription d'un utilisateur à partir de sa date d'inscription initiale et afficher différents messages en fonction du nombre d'années célébrées.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign this_day = 'now' | date: "%d" %}
{% assign anniversary_month = {{custom_attribute.${registration_date}}} | date: "%B" %}
{% assign anniversary_day = {{custom_attribute.${registration_date}}} | date: "%d" %}
{% assign anniversary_year = {{custom_attribute.${registration_date}}} | date: "%Y" %}

{% if this_month == anniversary_month %}
{% if this_day == anniversary_day %}
{% if anniversary_year == '2021' %}
Exactly one year ago today we met for the first time!

{% elsif anniversary_year == '2020' %}
Exactly two years ago today we met for the first time!

{% elsif anniversary_year == '2019' %}
Exactly three years ago today we met for the first time!

{% else %}
{% abort_message("Not same year") %}
{% endif %}

{% else %}
{% abort_message("Not same day") %}
{% endif %}

{% else %}
{% abort_message("Not same month") %}
{% endif %}
```
{% endraw %}

**Explication :** Ici, nous utilisons la variable réservée `now` pour insérer la date et l'heure actuelles au format [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601). Les filtres `%B` (mois comme « May ») et `%d` (jour comme « 18 ») formatent le mois et le jour actuels. Nous appliquons ensuite les mêmes filtres de date et d'heure aux valeurs de `signup_date` pour pouvoir comparer les deux valeurs à l'aide de balises et de logique conditionnelles.

Ensuite, nous répétons trois autres déclarations de variables pour obtenir les `%B` et `%d` de la `signup_date`, en ajoutant également `%Y` (année comme « 2021 »). Cela réduit la date et l'heure de la `signup_date` à l'année uniquement. Connaître le jour et le mois nous permet de vérifier si l'anniversaire d'inscription de l'utilisateur est aujourd'hui, et connaître l'année nous indique combien d'années se sont écoulées — ce qui nous permet de savoir pour combien d'années le féliciter !

{% alert tip %} Vous pouvez créer autant de conditions que d'années pendant lesquelles vous avez collecté des dates d'inscription. {% endalert %}

### Personnaliser les messages en fonction de la semaine d'anniversaire d'un utilisateur {#birthday-week}

Ce cas d'utilisation montre comment trouver la date d'anniversaire d'un utilisateur, la comparer à la date actuelle, puis afficher des messages d'anniversaire spéciaux avant, pendant et après sa semaine d'anniversaire.

{% raw %}
```liquid
{% assign this_week = 'now' | date: '%W' %}
{% assign birthday_week = {{${date_of_birth}}} | date: '%W' %}
{% assign last_week = {{this_week}} | minus: 1 %}
{% assign next_week = {{this_week}} | plus: 1 %}
{% assign birthday_week_conversion = {{birthday_week}} | plus: 0 %}
{% if {{last_week}} == {{birthday_week_conversion}} %}
Happy birthday for last week!
{% elsif {{birthday_week}} == {{this_week}} %}
Happy birthday for this week!
{% elsif {{next_week}} == {{birthday_week_conversion}} %}
Happy birthday for next week!
{% else %}
No birthday for you!
{% endif %}
```
{% endraw %}

**Explication :** Comme pour le cas d'utilisation de l'[année d'anniversaire](#anniversary-year), nous prenons ici la variable réservée `now` et utilisons le filtre `%W` (semaine, par exemple la semaine 12 sur 52 dans une année) pour obtenir le numéro de la semaine de l'année dans laquelle tombe l'anniversaire de l'utilisateur. Si la semaine d'anniversaire de l'utilisateur correspond à la semaine en cours, nous lui envoyons un message de félicitations !

Nous incluons également des déclarations pour `last_week` et `next_week` afin de personnaliser davantage vos messages.

### Envoyer des Campaigns aux utilisateurs pendant leur mois d'anniversaire {#birthday-month}

Ce cas d'utilisation montre comment calculer le mois d'anniversaire d'un utilisateur, vérifier si son anniversaire tombe dans le mois en cours, et si c'est le cas, envoyer un message spécial.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
{% if {{this_month}} == {{birth_month}} %}
Message body
{% else %}
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}

**Explication :** Comme pour le cas d'utilisation de la [semaine d'anniversaire](#birthday-week), sauf qu'ici nous utilisons le filtre `%B` (mois comme « May ») pour identifier les utilisateurs dont l'anniversaire tombe ce mois-ci. Une application possible serait de s'adresser aux utilisateurs fêtant leur anniversaire dans un e-mail mensuel.

### Éviter d'envoyer des messages lors des jours fériés importants {#holiday-avoid}

Ce cas d'utilisation montre comment envoyer des messages pendant la période des fêtes tout en évitant les jours fériés importants, lorsque l'engagement est susceptible d'être faible.

{% raw %}
```liquid
{% assign today = 'now' | date: '%Y-%m-%d' %}
{% if today == "2023-12-24" or today == "2023-12-25" or today == "2023-12-26" %}
{% abort_message %}
{% else %}
Message if today isn't one of the provided holidays.
{% endif %}
```
{% endraw %}

**Explication :** Ici, nous assignons le terme `today` à la variable réservée `now` (la date et l'heure actuelles), en utilisant les filtres `%Y` (année comme « 2023 »), `%m` (mois comme « 12 ») et `%d` (jour comme « 25 ») pour formater la date. Nous exécutons ensuite notre instruction conditionnelle : si la variable `today` correspond aux jours fériés de votre choix, le message sera annulé.

L'exemple fourni utilise la veille de Noël, le jour de Noël et le lendemain de Noël (Boxing Day).

{% endapi %}

{% api %}

## Utilisation de l'application {#app-usage}

{% apitags %}
App usage
{% endapitags %}

- [Envoyer des messages dans la langue d'un utilisateur s'il n'a pas enregistré de session](#app-session-language)
- [Personnaliser les messages en fonction de la dernière ouverture de l'application par l'utilisateur](#app-last-opened)
- [Afficher un message différent si l'utilisateur a utilisé l'application il y a moins de trois jours](#app-last-opened-less-than)

### Envoyer des messages dans la langue d'un utilisateur s'il n'a pas enregistré de session {#app-session-language}

Ce cas d'utilisation vérifie si un utilisateur a enregistré une session. Si ce n'est pas le cas, une logique est incluse pour afficher un message basé sur la langue collectée manuellement via un attribut personnalisé, le cas échéant. S'il n'y a aucune information de langue liée à son compte, le message s'affichera dans la langue par défaut. Si un utilisateur a enregistré une session, toute information de langue liée à l'utilisateur sera récupérée et le message approprié sera affiché.

{% raw %}
```liquid
{% if {{${last_used_app_date}}} == nil %}
{% if {{custom_attribute.${user_language}}} == 'en' %}
Message in English based on custom attribute
{% elsif {{custom_attribute.${user_language}}} == 'fr' %}
Message in French based on custom attribute
{% else %}
Does not have language - Default language
{% endif %}
{% else %}
{% if ${language} == 'en' %}
Message in English based on Language
{% elsif ${language} == 'fr' %}
Message in French based on Language
{% else %}
Has language - Default language
{% endif %}
{% endif %}
```
{% endraw %}

{% raw %}
**Explication :** Ici, nous utilisons deux instructions `if` groupées et imbriquées. La première instruction `if` vérifie si l'utilisateur a démarré une session en vérifiant si `last_used_app_date` est `nil`. En effet, `{{${language}}}` est collecté automatiquement par le SDK lorsqu'un utilisateur enregistre une session. Si l'utilisateur n'a pas enregistré de session, nous n'avons pas encore sa langue. Cette vérification regarde donc si des attributs personnalisés liés à la langue ont été enregistrés, et en fonction de cette information, affichera un message dans cette langue, si possible.
{% endraw %}

La seconde instruction `if` vérifie simplement l'attribut standard (par défaut), car l'utilisateur n'a pas `nil` pour `last_used_app_date`, ce qui signifie qu'il a enregistré une session et que nous avons sa langue.

{% alert note %}
[`Nil`](https://shopify.github.io/liquid/basics/types/#nil) est une variable réservée qui est renvoyée lorsque le code Liquid ne produit aucun résultat. `Nil` est traité comme `false` dans un bloc `if`.
{% endalert %}

### Personnaliser les messages en fonction de la dernière ouverture de l'application par l'utilisateur {#app-last-opened}

Ce cas d'utilisation calcule la dernière fois qu'un utilisateur a ouvert votre application et affiche un message personnalisé différent en fonction de la durée écoulée.

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Happy to see you again!
{% else %}
It's been a while; here are some of our latest updates.
{% endif %}
```
{% endraw %}

### Afficher un message différent si l'utilisateur a utilisé l'application il y a moins de trois jours {#app-last-opened-less-than}

Ce cas d'utilisation calcule depuis combien de temps un utilisateur a utilisé votre application et, en fonction de la durée écoulée, affiche un message personnalisé différent.

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Message for a recently active user
{% else %}
Message for a less active user
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## Comptes à rebours {#countdowns}

{% apitags %}
Countdowns
{% endapitags %}

- [Ajouter X jours à la date du jour](#countdown-add-x-days)
- [Calculer un compte à rebours à partir d'un point dans le temps](#countdown-difference-days)
- [Créer un compte à rebours pour des dates et priorités de livraison spécifiques](#countdown-shipping-options)
- [Créer un compte à rebours en jours](#countdown-days)
- [Créer un compte à rebours de jours en heures en minutes](#countdown-dynamic)
- [Afficher le nombre de jours restants jusqu'à une certaine date](#countdown-future-date)
- [Afficher le nombre de jours restants jusqu'à l'arrivée d'un attribut de date personnalisé](#countdown-custom-date-attribute)
- [Afficher le temps restant et annuler le message s'il ne reste que X temps](#countdown-abort-window)
- [Message in-app à envoyer X jours avant la fin de l'abonnement de l'utilisateur](#countdown-membership-expiry)
- [Personnaliser les messages in-app en fonction de la date et de la langue de l'utilisateur](#countdown-personalize-language)
- [Insérer dans un modèle la date dans 30 jours, formatée en mois et jour](#countdown-template-date)

### Ajouter x jours à la date du jour {#countdown-add-x-days}

Ce cas d'utilisation ajoute un nombre spécifique de jours à la date actuelle pour le référencer et l'insérer dans les messages. Par exemple, vous pourriez envoyer un message en milieu de semaine présentant les événements du week-end dans la région.

{% raw %}
```liquid
Here are the movies we're showing on {{ "now" | date:'%s' | plus:259200 | date:"%F" }}!
```
{% endraw %}

La valeur `plus` est toujours en secondes, c'est pourquoi nous terminons avec le filtre `%F` pour convertir les secondes en jours.

{% alert important %}
Vous pouvez inclure une URL ou un lien profond vers une liste d'événements dans votre message afin de diriger l'utilisateur vers une liste d'activités à venir.
{% endalert %}

### Calculer un compte à rebours à partir d'un point dans le temps {#countdown-difference-days}

Ce cas d'utilisation calcule la différence en jours entre une date spécifique et la date actuelle. Cette différence peut servir à afficher un compte à rebours à vos utilisateurs.

{% raw %}
```liquid
{% assign event_date = '2023-12-31' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
you have {{ difference_days }} days left!
```
{% endraw %}

### Créer un compte à rebours pour des dates et priorités de livraison spécifiques {#countdown-shipping-options}

Ce cas d'utilisation capture différentes options de livraison, calcule le temps nécessaire pour la réception et affiche des messages encourageant les utilisateurs à acheter à temps pour recevoir leur colis avant une certaine date.

{% raw %}
```liquid
{% assign standard_shipping_start = "2023-12-10T00:00-05:00" | date: "%s" %}
{% assign standard_shipping_end = "2023-12-20T13:00-05:00" | date: "%s" %}
{% assign express_shipping_end = "2023-12-22T24:00-05:00" | date: "%s" %}
{% assign overnight_shipping_end = "2023-12-23T24:00-05:00" | date: "%s" %}
{% assign today = 'now' | date: "%s" %}

{% assign difference_s = standard_shipping_end | minus: today %}
{% assign difference_s_days = difference_s | divided_by: 86400.00 | round %}
{% assign difference_e = express_shipping_end | minus: today %}
{% assign difference_e_days = difference_e | divided_by: 86400.00 | round %}
{% assign difference_o = overnight_shipping_end | minus: today %}
{% assign difference_o_days = difference_o | divided_by: 86400.00 | round %}

{% if today >= standard_shipping_start and today <= standard_shipping_end %}
{% if difference_s_days == 0 %}
This is the last day to order with standard shipping, so your order gets here on time for Christmas Eve!
{% elsif difference_s_days == 1 %}
There is {{difference_s_days}} day left to order with standard shipping, so your order gets here on time for Christmas Eve!

{% else %}
There are {{difference_s_days}} days left to order with standard shipping so your order gets here on time for Christmas Eve!
{% endif %}
{% elsif today > standard_shipping_end and today < express_shipping_end %}
{% if difference_e_days == 1 %}
There is {{difference_e_days}} day left to order with express shipping, so your order gets here on time for Christmas Eve!
{% else %}
There are {{difference_e_days}} days left to order with express shipping so your order gets here on time for Christmas Eve!
{% endif %}
{% elsif today >= express_shipping_end and today < overnight_shipping_end %}
This is the last day for overnight shipping so your order gets here on time for Christmas Eve!
{% else %}
{% abort_message("Unable to order and ship in time") %}
{% endif %}
```
{% endraw %}

### Créer un compte à rebours en jours {#countdown-days}

Ce cas d'utilisation calcule le temps restant entre un événement spécifique et la date actuelle, puis affiche le nombre de jours restants avant l'événement.

{% raw %}
```liquid
{% assign event_date = {{custom_attribute.${last_selected_event_date}}} | date: "%s" %}
{% assign today =  'now' | date: "%s"  %}
{% assign difference =  event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Your order will arrive in {{ difference_days }} days!
```
{% endraw %}

{% alert important %}
Vous aurez besoin d'un champ d'attribut personnalisé avec une valeur de type `date`.
{% endalert %}

### Créer un compte à rebours de jours en heures en minutes {#countdown-dynamic}

Ce cas d'utilisation calcule le temps restant entre un événement spécifique et la date actuelle. En fonction du temps restant avant l'événement, il adapte l'unité de temps (jours, heures, minutes) pour afficher différents messages personnalisés.

Par exemple, s'il reste deux jours avant l'arrivée de la commande d'un client, vous pourriez dire « Votre commande arrivera dans 2 jours ». S'il reste moins d'un jour, vous pourriez afficher « Votre commande arrivera dans 17 heures ».

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign scheme_finish = "2017-10-13T10:30:30" | date: "%s" %}
{% assign difference_seconds =  scheme_finish | minus: today %}
{% assign difference_minutes = difference_seconds | divided_by: 60 %}
{% assign difference_hours = difference_seconds | divided_by: 3600 %}
{% assign difference_days = difference_seconds | divided_by: 86400 %}
{% if {{difference_minutes}} > 59 and {{difference_minutes}} < 1440 %}
You have {{difference_hours}} hours left till your order arrives!
{% elsif {{difference_minutes}} < 59 %}
You have {{difference_minutes}} minutes left till your order arrives!
{% else %}
You have {{difference_days}} days left till your order arrives!
{% endif %}
```
{% endraw %}

{% alert important %}
Vous aurez besoin d'un champ d'attribut personnalisé avec une valeur de type `date`. Vous devrez également définir des seuils temporels pour déterminer quand le temps doit être affiché en jours, heures et minutes.
{% endalert %}

### Afficher le nombre de jours restants jusqu'à une certaine date {#countdown-future-date}

Ce cas d'utilisation calcule la différence entre la date actuelle et une date d'événement future, puis affiche un message indiquant le nombre de jours restants avant l'événement.

{% raw %}
```liquid
{% assign event_date = '2024-01-15' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
There are {{difference_days}} days until your birthday!
```
{% endraw %}

### Afficher le nombre de jours restants jusqu'à l'arrivée d'un attribut de date personnalisé {#countdown-custom-date-attribute}

Ce cas d'utilisation calcule la différence en jours entre les dates actuelle et future, puis affiche un message si la différence correspond à un nombre défini.

Dans cet exemple, un utilisateur recevra un message deux jours avant l'attribut de date personnalisé. Sinon, le message ne sera pas envoyé.

{% raw %}
```liquid
{% assign today = 'now' | date: '%j' | plus: 0 %}
{% assign surgery_date = {{custom_attribute.${surgery_date}}} | date: '%j' | plus: 0 %}

{% assign difference_days = {{surgery_date}} | minus: {{today}} %}
{% if difference_days == 2 %}
Your surgery is in 2 days on {{custom_attribute.${surgery_date}}}
{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Afficher le temps restant et annuler le message s'il ne reste que x temps {#countdown-abort-window}

Ce cas d'utilisation calcule le temps restant jusqu'à une certaine date et, en fonction de la durée (en ignorant le message si la date est trop proche), affiche différents messages personnalisés.

Par exemple, « Il vous reste x heures pour acheter votre billet pour Londres », mais sans envoyer le message s'il reste moins de deux heures avant le vol pour Londres.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign dep_time = {{event_properties.${outboundDate}}} | date: "%s" %}
{% assign time_to_dep = dep_time | minus: today %}
{% if {{time_to_dep}} < 7200 %}
{% abort_message("OutboundDate less than 2 hours") %}
{% elsif {{time_to_dep}} > 7200 and {{time_to_dep}} < 86400 %}
Don't forget to buy your ticket to {{event_properties.${toStation}}} within next 24 hours!
{% else %}
Still traveling to {{event_properties.${toStation}}} in more than 24 hours? Book now!
{% endif %}
```
{% endraw %}

{% alert important %} Vous aurez besoin d'une propriété d'événement personnalisé. {% endalert %}

### Message in-app à envoyer x jours avant la fin de l'abonnement des utilisateurs {#countdown-membership-expiry}

Ce cas d'utilisation capture la date d'expiration de l'abonnement, calcule le temps restant avant l'expiration et affiche différents messages en fonction du délai restant.

{% raw %}
```liquid
{% assign membership_expiry = {{custom_attribute.${membership_expiry_date}}} | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = membership_expiry | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}

{% if difference_days > 4 and difference_days <= 7 %}
You have {{difference_days}} days left in your trial, make sure you upgrade!

{% elsif difference_days > 2 and difference_days <= 4 %}
HURRY! You have {{difference_days}} days left in your trial, make sure you upgrade!

{% elsif difference_days == 2 %}
LAST CHANCE! You have {{difference_days}} days left in your trial. Make sure you upgrade!

{% else %}
You have few days left in your trial. Make sure to upgrade!
{% endif %}
```
{% endraw %}

### Personnaliser les messages in-app en fonction de la date et de la langue des utilisateurs {#countdown-personalize-language}

Ce cas d'utilisation calcule un compte à rebours jusqu'à un événement et, en fonction du paramètre de langue de l'utilisateur, affiche le compte à rebours dans sa langue.

Par exemple, vous pourriez envoyer une série de messages de vente incitative aux utilisateurs une fois par mois pour leur indiquer combien de temps une offre est encore valide, avec quatre messages in-app :

- Initial
- 2 jours restants
- 1 jour restant
- Dernier jour

{% raw %}
```liquid
{% assign today = 'now' | date: "%s" %}
{% assign end_date = "2021-04-16T23:59:59" | date: "%s" %}
{% assign difference = end_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
{% if {{difference_days}} >= 3 %}
{% if ${language} == 'de' %}

Hallo, das Angebot gilt bis zum 16.04.

{% elsif ${language} == 'ch' %}
Grüezi, das Angebot gilt bis zum 16.04.

{% elsif ${language} == 'en' %}
The offer is valid until 16.04.

{% else %}
The offer is valid until 16.04.

{% endif %}
{% elsif {{difference_days}} == 2 %}
{% if ${language} == 'de' %}
INSERT MESSAGE

{% elsif ${language} == 'ch' %}
INSERT MESSAGE

{% elsif ${language} == 'en' %}
INSERT MESSAGE

{% else %}
INSERT MESSAGE
{% endif %}

{% elsif {{difference_days}} == 1 %}
{% if ${language} == 'de' %}
INSERT MESSAGE

{% elsif ${language} == 'ch' %}
INSERT MESSAGE

{% elsif ${language} == 'en' %}
INSERT MESSAGE

{% else %}
INSERT MESSAGE
{% endif %}

{% elsif {{difference_days}} == 0 %}
{% if ${language} == 'de' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'ch' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'en' %}
Grüezi, das Angebot gilt noch heute.

{% else %}
Hi, the offer is only valid today.
{% endif %}

{% else %}
{% abort_message("Calculation failed") %}
{% endif %}
```
{% endraw %}

{% alert important %}
Vous devrez assigner une valeur de type `date` et inclure une logique d'annulation si la date donnée se situe en dehors de la plage de dates. Pour des calculs au jour exact, la date de fin assignée doit inclure 23:59:59.
{% endalert %}

### Insérer dans un modèle la date dans 30 jours, formatée en mois et jour {#countdown-template-date}

Ce cas d'utilisation affiche la date dans 30 jours pour l'utiliser dans les messages.

{% raw %}
```liquid
{% assign today = 'now' | date: "%s" %}
{% assign thirty_days = today | plus: 2592000 | date: "%B %d" %}
```
{% endraw %}

{% endapi %}

{% api %}

## Attribut personnalisé {#custom-attribute}

{% apitags %}
Custom attribute
{% endapitags %}

- [Personnaliser un message en fonction d'attributs personnalisés correspondants](#attribute-matching)
- [Formater une devise selon les conventions numériques européennes](#european-currency-format)
- [Soustraire deux attributs personnalisés pour afficher la différence en valeur monétaire](#attribute-monetary-difference)
- [Référencer le prénom d'un utilisateur si son nom complet est stocké dans le champ first_name](#attribute-first-name)

### Personnaliser un message en fonction d'attributs personnalisés correspondants {#attribute-matching}

Ce cas d'utilisation vérifie si un utilisateur possède des attributs personnalisés spécifiques et, si c'est le cas, affiche différents messages personnalisés.

{% raw %}
```liquid
{% if custom_attribute.${hasShovel} == true and custom_attribute.${VisitToGroundTooTough} > 0 %}
The ground is very hard. The dirt road goes East.
{% elsif custom_attribute.${hasShovel} == true %}
The dirt road goes East.
{% elsif custom_attribute.${VisitToStart} > 0 %}
The dirt road goes East.
The shovel here.
{% else %}
You are at a dead-end of a dirt road. The road goes to the east. In the distance, you can see that it will eventually fork off. The trees here are very tall royal palms, and they are spaced equidistant from each other.
There is a shovel here.
{% endif %}
```
{% endraw %}

### Formater une devise selon les conventions numériques européennes {#european-currency-format}

Pour les locales qui utilisent une virgule comme séparateur décimal et un point comme séparateur de milliers (par exemple, l'Allemagne ou l'Italie), utilisez les filtres [`money`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters#money-filter) et [`number_with_delimiter`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#number-formatting-filters) avec `replace` pour intervertir les séparateurs. Utilisez `#` comme marque substitutive temporaire afin que les points et les virgules ne soient pas intervertis lors de la même passe.

{% raw %}
```liquid
{{ 1234567.89 | money | number_with_delimiter | replace: '.', '#' | replace: ',', '.' | replace: '#', ',' }}
```

**Résultat :** `1.234.567,89`

**Explication :** Le filtre `money` ajoute les décimales mais n'ajoute pas de symbole monétaire ni de séparateurs spécifiques à la locale. `number_with_delimiter` ajoute les séparateurs de milliers au format américain, et les filtres `replace` les convertissent au format européen.
{% endraw %}

### Soustraire deux attributs personnalisés pour afficher la différence en valeur monétaire {#attribute-monetary-difference}

Ce cas d'utilisation capture deux attributs personnalisés monétaires, puis calcule et affiche la différence pour indiquer aux utilisateurs combien il leur reste à collecter pour atteindre leur objectif.

{% raw %}
```liquid
{% assign event_goal = {{custom_attribute.${last_selected_event_personal_goal}}} %}
{% assign current_raised =  {{custom_attribute.${last_selected_event_personal_amount_raised}}} %}
{% assign difference =  event_goal | minus: current_raised %}
You only have ${{ difference | round: 0 | number_with_delimiter }} left to raise!
```
{% endraw %}

### Référencer le prénom d'un utilisateur si son nom complet est stocké dans le champ first_name {#attribute-first-name}

Ce cas d'utilisation capture le prénom d'un utilisateur (si le prénom et le nom sont stockés dans un seul champ) puis utilise ce prénom pour afficher un message de bienvenue.

{% raw %}
```liquid
{{${first_name} | truncatewords: 1, "" | default: 'hi'}}
{% assign name = {{${first_name}}} | split: ' ' %}
Hi {{name[0]}}, here's your message!
```

**Explication :** Le filtre `split` transforme la chaîne de caractères contenue dans `{{${first_name}}}` en un tableau. En utilisant `{{name[0]}}`, nous ne faisons référence qu'au premier élément du tableau, c'est-à-dire le prénom de l'utilisateur.

{% endraw %}
{% endapi %}

{% api %}

## Événement personnalisé {#custom-event}

{% apitags %}
Custom event
{% endapitags %}

- [Annuler une notification push si un événement personnalisé est dans les deux heures à venir](#event-abort-push)
- [Envoyer une Campaign chaque fois qu'un utilisateur effectue un événement personnalisé trois fois](#event-three-times)
- [Envoyer un message aux utilisateurs qui n'ont acheté que dans une seule catégorie](#event-purchased-one-category)
- [Suivre le nombre de fois qu'un événement personnalisé s'est produit au cours du mois précédent](#track)


### Annuler une notification push si un événement personnalisé est dans les deux heures à venir {#event-abort-push}

Ce cas d'utilisation calcule le temps restant avant un événement et, en fonction du temps restant, affiche différents messages personnalisés.

Par exemple, vous pourriez vouloir empêcher l'envoi d'une notification push si une propriété d'événement personnalisé arrive dans les deux prochaines heures. Cet exemple utilise le scénario d'un panier abandonné pour un billet de train.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign dep_time = {{event_properties.${outboundDate_Time}}} | date: "%s" %}
{% assign time_to_dep = dep_time | minus: today %}
{% if {{time_to_dep}} <= 7200 %}
{% abort_message("OutboundDate less than 2 hours") %}
{% elsif {{time_to_dep}} > 7200 and {{time_to_dep}} < 86400 %}
Don't forget to buy your ticket to {{event_properties.${toStation}}} within next 24 hours
{% else %}
Still traveling to {{event_properties.${toStation}}} in more than 24 hours? Book now
{% endif %}
```
{% endraw %}

### Envoyer une Campaign chaque fois qu'un utilisateur effectue un événement personnalisé trois fois {#event-three-times}

Ce cas d'utilisation vérifie si un utilisateur a effectué un événement personnalisé trois fois et, si c'est le cas, affiche un message ou envoie une Campaign.

{% raw %}
```liquid
{% assign cadence = custom_attribute.${example} | minus: 1 | modulo: 3 %}
{% if custom_attribute.${example} == blank %}
{% abort_message("Error calculating cadence") %}
{% elsif cadence != 0 %}
{% abort_message("Skip message") %}
{% endif %}
Did you forget something in your shopping cart?
```
{% endraw %}

{% alert important %} Vous devez disposer d'une propriété d'événement pour le compteur d'événements personnalisés ou utiliser un webhook vers votre endpoint Braze. Cela permet d'incrémenter un attribut personnalisé (`example_event_count`) chaque fois que l'utilisateur effectue l'événement. Cet exemple utilise une cadence de trois (1, 4, 7, 10, etc.). Pour commencer la cadence à zéro (0, 3, 6, 9, etc.), supprimez `minus: 1`.
{% endalert %}

### Envoyer un message aux utilisateurs qui n'ont acheté que dans une seule catégorie {#event-purchased-one-category}

Ce cas d'utilisation capture la liste des catégories dans lesquelles un utilisateur a acheté et, si une seule catégorie d'achat existe, affiche un message.

{% raw %}
```liquid
{% assign category = {{custom_attribute.${categories_purchased}}} %}
{% assign uniq_cat = {{category | uniq }} %}
{% if {{uniq_cat | size}} == 1 %}
{{uniq_cat}}
{% else %}
{% abort_message("Purchase category doesn't exist") %}
{% endif %}
```
{% endraw %}

### Suivre le nombre de fois qu'un événement personnalisé s'est produit au cours du mois précédent {#track}

Ce cas d'utilisation calcule le nombre de fois qu'un événement personnalisé a été enregistré entre le 1er du mois en cours et le mois précédent. Vous pouvez ensuite exécuter un appel users/track pour mettre à jour et stocker cette valeur en tant qu'attribut personnalisé. Notez que cette Campaign doit fonctionner pendant deux mois consécutifs avant que les données mensuelles puissent être utilisées.

{% raw %}
```liquid

{% capture body %}
{
 "braze_id": "{{${braze_id}}}",
 "fields_to_export": ["custom_events"]
}

{% endcapture %}

{% connected_content YOUR_BRAZE_ENDPOINT/users/export/ids
 :method post
  :headers { "Authorization": "Bearer YOUR_API_KEY" }
  :body {{body}}
 :content_type application/json
 :save response
  :retry %}

{% for custom_event in response.users[0].custom_events %}
{% assign ce_name = custom_event.name %}
{% comment %} The following custom event name will need to be amended for the target custom event. {% endcomment %}

{% if ce_name == "Project Exported" %}
{% comment %}{{custom_event.name}}: {{custom_event.count}}{% endcomment %}
{% assign current_count = custom_event.count %}
{% endif %}
{% endfor %}

{% assign prev_month_count = {{custom_attribute.${projects_exported_prev_month}}} %}
{% assign latest_count = current_count | minus: prev_month_count %}
{% assign now = "now" | date: "%s" %}
{% assign yesterday = {{now}} | minus: 86400 %}
{% assign previous_month = {{yesterday}} | date: "%B" %}
{% assign previous_year = {{yesterday}} | date: "%y" %}
{% assign formatted_month = previous_month | downcase %}
{% comment %}The Custom Event name that is being tracked will be needed to be amended for the target Custom Event in the Attribute Name below. {% endcomment %}
```

```json
"attributes": [
  {
    "external_id":"{{${user_id}}}",
       "projects_exported_{{formatted_month}}_{{previous_year}}": "{{latest_count}}"
  }
]
```

{% endraw %}

{% endapi %}

{% api %}

## Langue {#language}

{% apitags %}
Language
{% endapitags %}

- [Afficher les noms de mois dans une autre langue](#language-display-month)
- [Afficher une image en fonction de la langue d'un utilisateur](#language-image-display)
- [Personnaliser les messages en fonction du jour de la semaine et de la langue de l'utilisateur](#language-personalize-message)

### Afficher les noms de mois dans une autre langue {#language-display-month}

Ce cas d'utilisation affiche la date, le mois et l'année actuels, avec le mois dans une autre langue. L'exemple fourni utilise le suédois.

{% raw %}
```liquid
{% assign day = 'now' | date: "%e" %}
{% assign year =  'now' | date: "%Y" %}
{% assign month =  'now' | date: "%B" %}

{% if {{month}} == 'January' %}
{{day}} Januari {{year}}
{% elsif {{month}} == 'February' %}
{{day}} Februari {{year}}
{% elsif {{month}} == 'March' %}
{{day}} Mars {{year}}
{% elsif {{month}} == 'April' %}
{{day}} April {{year}}
{% elsif {{month}} == 'May' %}
{{day}} Maj {{year}}
{% elsif {{month}} == 'June' %}
{{day}} Juni {{year}}
{% elsif {{month}} == 'July' %}
{{day}} Juli {{year}}
{% elsif {{month}} == 'August' %}
{{day}} Augusti {{year}}
{% elsif {{month}} == 'September' %}
{{day}} September {{year}}
{% elsif {{month}} == 'October' %}
{{day}} Oktober {{year}}
{% elsif {{month}} == 'November' %}
{{day}} November {{year}}
{% elsif {{month}} == 'December' %}
{{day}} December {{year}}
{% endif %}
```
{% endraw %}

### Afficher une image en fonction de la langue d'un utilisateur {#language-image-display}

Ce cas d'utilisation affiche une image en fonction de la langue d'un utilisateur. Notez que ce cas d'utilisation n'a été testé qu'avec des images téléchargées dans la bibliothèque multimédia de Braze.

{% raw %}
```liquid
{% if ${language} == 'en' %}
English image URL (for example, https://cdn-staging.braze.com/appboy/communication/assets/image_assets/images/60aecba96a93150c749b4d57/original.png?1622068137)
{% elsif ${language} == 'ru' %}
Russian image URL
{% elsif ${language} == 'es' %}
Spanish image URL
{% else %}
Fallback image URL
{% endif %}
```
{% endraw %}

### Personnaliser les messages en fonction du jour de la semaine et de la langue de l'utilisateur {#language-personalize-message}

Ce cas d'utilisation vérifie le jour actuel de la semaine et, en fonction du jour, si la langue de l'utilisateur correspond à l'une des options fournies, affiche un message spécifique dans sa langue.

L'exemple fourni s'arrête au mardi mais peut être répété pour chaque jour de la semaine.

{% raw %}
```liquid
{% assign today  = 'now' | date: '%A' %}

{% if today == 'Monday' %}
{% if ${language} == 'es' %}
Compra hoy y lleva tu aprendizaje de idiomas a niveles más altos. 🚀

{% elsif ${language} == 'en' %}
Purchase today and take your language learning to the next level. 🚀

{% elsif ${language} == 'zh' %}
今天就购买并将您的语言提高到一个新水平吧。🚀

{% else %}
It's Monday, but the language doesn't match
{% endif %}

{% elsif today == 'Tuesday' %}

{% if ${language} == 'zh' %}
不要忘记解锁以获取完整版本哦。🔓

{% elsif ${language} == 'en' %}
Don't forget to unlock the full version of your language. 🔓

{% elsif ${language} == 'ja' %}
すべての機能を使ってみませんか 🔓

{% elsif ${language} == 'es' %}
No te olivides de desbloquear la versión completa del programa de idiomas. 🔓

{% else %}
tuesday default
{% endif %}
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## Divers {#miscellaneous}

{% apitags %}
Miscellaneous
{% endapitags %}

- [Éviter d'envoyer des e-mails aux clients qui ont bloqué les e-mails marketing](#misc-avoid-blocked-emails)
- [Utiliser l'état d'abonnement d'un client pour personnaliser le contenu des messages](#misc-personalize-content)
- [Mettre en majuscule la première lettre de chaque mot dans une chaîne de caractères](#misc-capitalize-words-string)
- [Comparer la valeur d'un attribut personnalisé avec un tableau](#misc-compare-array)
- [Créer un rappel d'événement à venir](#misc-event-reminder)
- [Trouver une chaîne de caractères dans un tableau](#misc-string-in-array)
- [Trouver la plus grande valeur dans un tableau](#misc-largest-value)
- [Trouver la plus petite valeur dans un tableau](#misc-smallest-value)
- [Interroger la fin d'une chaîne de caractères](#misc-query-end-of-string)
- [Interroger les valeurs d'un tableau à partir d'un attribut personnalisé avec plusieurs combinaisons](#misc-query-array-values)
- [Formater une chaîne de caractères en numéro de téléphone](#phone-number)

### Éviter d'envoyer des e-mails aux clients qui ont bloqué les e-mails marketing {#misc-avoid-blocked-emails}

Ce cas d'utilisation prend une liste d'utilisateurs bloqués enregistrée dans un Content Block et vérifie que ces utilisateurs bloqués ne sont pas contactés ou ciblés dans les Campaigns ou Canvas à venir.

{% alert important %}
Pour utiliser ce Liquid, enregistrez d'abord la liste des e-mails bloqués dans un Content Block. La liste ne doit contenir aucun espace ni caractère supplémentaire entre les adresses e-mail (par exemple, `test@braze.com,abc@braze.com`).
{% endalert %}

{% raw %}
```liquid
{% assign blocked_emails = {{content_blocks.${BlockedEmailList}}} | split: ',' %}
{% for email in blocked_emails %}
    {% if {{${email_address}}} == email %}
    {% abort_message("Email is blocked") %}
    {% break %}
    {% endif %}
{% endfor %}
Your message here!
```
{% endraw %}

**Explication :** Ici, nous vérifions si l'e-mail du destinataire potentiel figure dans cette liste en référençant le Content Block des e-mails bloqués. Si l'e-mail est trouvé, le message ne sera pas envoyé.

{% alert note %}
Les Content Blocks ont une limite de taille de 5 Mo.
{% endalert %}

### Utiliser l'état d'abonnement d'un client pour personnaliser le contenu des messages {#misc-personalize-content}

Ce cas d'utilisation utilise l'état d'abonnement d'un client pour envoyer du contenu personnalisé. Les clients abonnés à un groupe d'abonnement spécifique recevront un message exclusif pour les groupes d'abonnement e-mail.

{% raw %}
```liquid
{% if {{subscribed_state.${subscription_group_id}}} == 'subscribed' %}
This is an exclusive message for subscribed users!
{% else %} This is the default message for other users.
{% endif %}
```
{% endraw %}

### Mettre en majuscule la première lettre de chaque mot dans une chaîne de caractères {#misc-capitalize-words-string}

Ce cas d'utilisation prend une chaîne de mots, les divise en un tableau et met en majuscule la première lettre de chaque mot.

{% raw %}
```liquid
{% assign words_array = {{custom_attribute.${address}}} | split: ' ' %}
{% for words in {{words_array}} %}
{{ words | capitalize | append: ' ' }}
{% endfor %}
```
{% endraw %}

**Explication :** Ici, nous avons assigné une variable à notre attribut de chaîne choisi et utilisé le filtre `split` pour diviser la chaîne en un tableau. Nous avons ensuite utilisé la balise `for` pour assigner la variable `words` à chacun des éléments de notre tableau nouvellement créé, avant d'afficher ces mots avec le filtre `capitalize` et le filtre `append` pour ajouter des espaces entre chacun des termes.

### Comparer la valeur d'un attribut personnalisé avec un tableau {#misc-compare-array}

Ce cas d'utilisation prend une liste de magasins favoris, vérifie si l'un des magasins favoris d'un utilisateur figure dans cette liste et, si c'est le cas, affiche une offre spéciale de ces magasins.

{% raw %}
```liquid
{% assign favorite_stores = 'Target,Walmart,Costco' | split: ',' %}
{% for store in favorite_stores %}
{% if {{custom_attribute.${favorited_stores}}} contains {{store}} %}
Today's offer from {{store}}

{% break %}

{% else %}
{% abort_message("No attribute found") %}
{% endif %}
{% endfor %}
```
{% endraw %}

{% alert important %} Cette séquence contient une balise `break` dans l'instruction conditionnelle principale. Cela provoque l'arrêt de la boucle lorsqu'une correspondance est trouvée. Si vous souhaitez afficher plusieurs ou toutes les correspondances, supprimez la balise `break`. {% endalert %}

### Créer un rappel d'événement à venir {#misc-event-reminder}

Ce cas d'utilisation permet aux utilisateurs de configurer des rappels à venir basés sur des événements personnalisés. Le scénario d'exemple permet à un utilisateur de définir un rappel pour une date de renouvellement de police à 26 jours ou plus, les rappels étant envoyés 26, 13, 7 ou 2 jours avant la date de renouvellement.

Avec ce cas d'utilisation, le contenu suivant doit être placé dans le corps d'une [campagne webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) ou d'une étape du Canvas.

{% raw %}
```liquid
{% comment %}
Depending on how the reminder_capture property is passed to Braze, with/without a timestamp, the number of days could impact whether a user falls on either side of the 26/13/7/2-day windows.
Once users have been assigned to a Reminder journey/flow, they are then scheduled to enter a subsequent Canvas.
This 'Event Listener' can be used to split out users into different journeys based on the Custom Event properties sent to Braze.
{% endcomment %}

{% comment %}
When testing, make sure the campaign ID, campaign API endpoint, Canvas ID, Canvas API endpoint are entered correctly. In this example, the Canvas ID and Canvas API endpoint have been set up for sharing with the client. In practice, this can be testing using a campaign ID and Campaign API endpoint.
{% endcomment %}

{% comment %}
The following step calculates how much there is between today's date and the Reminder Date as 'time_to_reminder'.
{% endcomment %}

{% assign today = "now" | date: '%s' %}
{% assign reminder_start_date = {{event_properties.${reminder_date}}} | date: '%s' %}
{% assign time_to_reminder = reminder_start_date | minus: today %}

{% comment %}
The following step checks if the time_to_reminder is more than 26 days away; if this is true, then the user is scheduled to enter the subsequent Canvas 26 days before the reminder_date.
The time is converted from 'seconds from 1970' to the appropriate Reminder Date in the required ISO 8601 format.
N.B. Additional time zones would need to be catered for by adding an additional API Schedule property of "in_local_time"
{% endcomment %}

{% if {{time_to_reminder}} > 2246400 %}
{% assign time_to_first_message = reminder_start_date | plus: 2246400 %}
{{ time_to_first_message | date: '%Y-%m-%dT%H:%M' }}
{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than 26 days away but more than 13 days away.
Users are scheduled to enter the journey on day 13.
{% endcomment %}

{% elsif 1123200 > {{time_to_reminder}} and {{time_to_reminder}} < 2246399 %}
{% assign time_to_first_message = reminder_start_date | plus: 1123200 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than 13 days away but more than seven days away.
Users are scheduled to enter the journey on day 7.
{% endcomment %}

{% elsif 604800 > {{time_to_reminder}} and {{time_to_reminder}} < 1123199 %}
{% assign time_to_first_message = reminder_start_date | plus: 604800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than seven days away but more than two days away.
Users are scheduled to enter the journey on day 2.
{% endcomment %}

{% elsif {{time_to_reminder}} < 604799 and {{time_to_reminder}} > 172860 %}
{% assign time_to_first_message = reminder_start_date | plus: 172800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}
{% endif %}
```
{% endraw %}

{% alert important %}

Vous aurez besoin d'un événement personnalisé `reminder_capture`, et les propriétés de l'événement personnalisé doivent inclure au minimum :

- `reminder-id` : identifiant de l'événement personnalisé
- `reminder_date` : date soumise par l'utilisateur pour l'échéance de son rappel
- `message_personalisation_X` : toutes les propriétés nécessaires pour personnaliser le message au moment de l'envoi

{% endalert %}

### Trouver une chaîne de caractères dans un tableau {#misc-string-in-array}

Ce cas d'utilisation vérifie si un tableau d'attributs personnalisés contient une chaîne de caractères spécifique et, si elle existe, affiche un message spécifique.

{% raw %}
```liquid
{% if custom_attribute.${PartnershipProgramsNotLinked} contains 'Hertz' %}
Link your Hertz account to use Hertz Fast Lane.
{% endif %}
```
{% endraw %}

### Trouver la plus grande valeur dans un tableau {#misc-largest-value}

Ce cas d'utilisation calcule la valeur la plus élevée dans un tableau d'attributs personnalisés donné pour l'utiliser dans les messages aux utilisateurs.

Par exemple, vous pourriez vouloir montrer à un utilisateur le meilleur score actuel ou l'enchère la plus élevée sur un article.

{% raw %}
```liquid
{% assign maxValue = 0 %}
{% for attribute in {{custom_attribute.${array_attribute}}} %}
{% assign compareValue = {{attribute | plus: 0}} %}
{% if compareValue > maxValue %}
{% assign maxValue = compareValue %}
{% endif %}
{% endfor %}
{{maxValue}}
```
{% endraw %}

{% alert important %}
Vous devez utiliser un attribut personnalisé qui a une valeur entière et qui fait partie d'un tableau (liste). {% endalert %}

### Trouver la plus petite valeur dans un tableau {#misc-smallest-value}

Ce cas d'utilisation calcule la valeur la plus basse dans un tableau d'attributs personnalisés donné pour l'utiliser dans les messages aux utilisateurs.

Par exemple, vous pourriez vouloir montrer à un utilisateur le score le plus bas ou l'article le moins cher.

{% raw %}
```liquid
{% assign minValue = custom_attribute.${array_attribute}[0] | plus: 0 %}
{% for attribute in {{custom_attribute.${array_attribute}}} %}
{% assign compareValue = {{attribute | plus: 0}} %}
{% if compareValue < minValue %}
{% assign minValue = compareValue %}
{% endif %}
{% endfor %}
{{minValue}}
```
{% endraw %}

{% alert important %} Vous devez utiliser un attribut personnalisé qui a une valeur entière et qui fait partie d'un tableau (liste). {% endalert %}

### Interroger la fin d'une chaîne de caractères {#misc-query-end-of-string}

Ce cas d'utilisation interroge la fin d'une chaîne de caractères pour l'utiliser dans les messages.

{% raw %}
```liquid
{% assign interest = {{custom_attribute.${Buyer Interest}}} | first %}
{% assign marketplace = interest | split: "" | reverse | join: "" | truncate: 4, "" %}
{% if {{marketplace}} == '3243' %}

Your last marketplace search was on {{custom_attribute.${Last marketplace buyer interest} | date: '%d.%m.%Y'}}. Check out all of our new offers.

{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

### Interroger les valeurs d'un tableau à partir d'un attribut personnalisé avec plusieurs combinaisons {#misc-query-array-values}

Ce cas d'utilisation prend une liste d'émissions bientôt expirées, vérifie si l'une des émissions favorites d'un utilisateur figure dans cette liste et, si c'est le cas, affiche un message informant l'utilisateur qu'elles expireront bientôt.

{% raw %}
```liquid
{% assign expired_shows = 'Modern Family,The Rookie,Body of Proof,Felicity' | split: ',' %}
{% for show in expired_shows %}
{% if {{custom_attribute.${Favorite Shows}}} contains {{show}} %}
{% assign new_shows = new_shows | append: {{show}} | append: '*' %}
{% endif %}
{% endfor %}
{% assign new_shows_clean = new_shows | split: '*' %}
{% if new_shows_clean.size != 0 %}

All episodes of {{new_shows_clean | join: ', ' }} expire on 9/8 - watch them now before they're gone!

{% else %}
{% abort_message("Not found") %}
{% endif %}
```
{% endraw %}

{% alert important %} Vous devrez d'abord trouver les correspondances entre les tableaux, puis construire la logique à la fin pour séparer les correspondances. {% endalert %}

### Formater une chaîne de caractères en numéro de téléphone {#phone-number}

Ce cas d'utilisation vous montre comment indexer le champ `phone_number` du profil utilisateur (par défaut, formaté comme une chaîne d'entiers) et le reformater selon vos normes locales de numéro de téléphone. Par exemple, 1234567890 en (123)-456-7890.

{% raw %}
```liquid
{% assign phone = {{${phone_number}}} | remove: "-" | split: '' %}

({{ phone[0] }}{{ phone[1] }}{{ phone[2] }})-{{ phone[3] }}{{ phone[4] }}{{ phone[5] }}-{{ phone[6] }}{{ phone[7] }}{{ phone[8] }}{{ phone[9] }}
```
{% endraw %}

{% endapi %}

{% api %}

## Ciblage par plateforme {#platform-targeting}

{% apitags %}
Platform targeting
{% endapitags %}

- [Différencier le texte par système d'exploitation de l'appareil](#platform-device-os)
- [Cibler uniquement une plateforme spécifique](#platform-target)
- [Cibler uniquement les appareils iOS avec une version spécifique du système d'exploitation](#platform-target-ios-version)
- [Cibler uniquement les navigateurs web](#platform-target-web)
- [Cibler un opérateur mobile spécifique](#platform-target-carrier)

### Différencier le texte par système d'exploitation de l'appareil {#platform-device-os}

Ce cas d'utilisation vérifie sur quelle plateforme se trouve un utilisateur et, en fonction de sa plateforme, affiche un message spécifique.

Par exemple, vous pourriez montrer aux utilisateurs mobiles des versions plus courtes du texte tout en montrant aux autres utilisateurs la version régulière et plus longue. Vous pourriez également montrer aux utilisateurs mobiles certains messages pertinents pour eux mais qui ne le seraient pas pour les utilisateurs web. Par exemple, les messages iOS pourraient parler d'Apple Pay, tandis que les messages Android devraient mentionner Google Pay.

{% raw %}
```liquid
{% if targeted_device.${platform} == "ios" or targeted_device.${platform} == "android" %}
This is a shorter copy.

{% else %}
This is the regular copy and much longer than the short version.
{% endif %}
```
{% endraw %}

{% alert note %}
Liquid est sensible à la casse, `targeted_device.${platform}` renvoie la valeur entièrement en minuscules.
{% endalert %}

### Cibler uniquement une plateforme spécifique {#platform-target}

Ce cas d'utilisation capture la plateforme de l'appareil des utilisateurs et, en fonction de la plateforme, affiche un message.

Par exemple, vous pourriez vouloir envoyer un message uniquement aux utilisateurs Android. Cela peut servir d'alternative à la sélection d'une application dans l'outil de segmentation.

{% raw %}
```liquid
{% if {{targeted_device.${platform}}} == 'android' %}

This is a message for an Android user!

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Cibler uniquement les appareils avec une version spécifique du système d'exploitation {#platform-target-ios-version}

Ce cas d'utilisation vérifie si la version du système d'exploitation d'un utilisateur fait partie d'un certain ensemble de versions et, si c'est le cas, affiche un message spécifique.

L'exemple utilisé envoie un avertissement aux utilisateurs ayant une version du système d'exploitation 10.0 ou antérieure, les informant que le support de leur système d'exploitation est en cours d'abandon.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == "10.0" or {{targeted_device.${os}}} == "10.0.1" or {{targeted_device.${os}}} == "10.0.2" or {{targeted_device.${os}}} == "10.0.3" or {{targeted_device.${os}}} == "10.1" or {{targeted_device.${os}}} == "10.2" or {{targeted_device.${os}}} == "10.2.1" or {{targeted_device.${os}}} == "10.3" or {{targeted_device.${os}}} == "10.3.1" or {{targeted_device.${os}}} == "10.3.2" or {{targeted_device.${os}}} == "10.3.3" or {{targeted_device.${os}}} == "10.3.4" or {{targeted_device.${os}}} == "9.3.1" or {{targeted_device.${os}}} == "9.3.2" or {{targeted_device.${os}}} == "9.3.3" or {{targeted_device.${os}}} == "9.3.4" or {{targeted_device.${os}}} == "9.3.5" %}

We are phasing out support for your device's operating system. Be sure to update to the latest software for the best app experience.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Cibler uniquement les navigateurs web {#platform-target-web}

Ce cas d'utilisation vérifie si l'appareil cible d'un utilisateur fonctionne sous Mac ou Windows et, si c'est le cas, affiche un message spécifique.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == 'Mac' or {{targeted_device.${os}}} == 'Windows' %}

This message will display on your desktop web browser.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

Le cas d'utilisation suivant vérifie si un utilisateur web est sur iOS ou Android et, si c'est le cas, affiche un message spécifique.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == 'iOS' and {{targeted_device.${platform}}} == 'web' %}

Content for iOS.

{% elsif {{targeted_device.${os}}} == 'android' and {{targeted_device.${platform}}} == 'web' %}

Content for Android.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Cibler un opérateur mobile spécifique {#platform-target-carrier}

Ce cas d'utilisation vérifie si l'opérateur de l'appareil d'un utilisateur est Verizon et, si c'est le cas, affiche un message spécifique.

Pour les notifications push et les canaux de messages in-app, vous pouvez spécifier l'opérateur de l'appareil dans le corps de votre message en utilisant Liquid. Si l'opérateur de l'appareil du destinataire ne correspond pas, le message ne sera pas envoyé.

{% raw %}
```liquid
{% if {{targeted_device.${carrier}}} contains "verizon" or {{targeted_device.${carrier}}} contains "Verizon" %}

This is a message for Verizon users!

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## SMS

{% apitags %}
SMS
{% endapitags %}

- [Répondre avec différents messages en fonction du mot-clé SMS entrant](#sms-keyword-response)

### Répondre avec différents messages en fonction du mot-clé SMS entrant {#sms-keyword-response}

Ce cas d'utilisation intègre le traitement dynamique des mots-clés SMS pour répondre à des messages entrants spécifiques avec un texte différent. Par exemple, vous pouvez envoyer des réponses différentes lorsque quelqu'un envoie « START » par rapport à « JOIN ».

{% raw %}
```liquid
{% assign inbound_message = {{sms.${inbound_message_body}}} | downcase | strip %}
{% if inbound_message contains 'start' %}
Thanks for joining our SMS program! Make sure your account is up to date for the best deals!

{% elsif inbound_message contains 'join' %}
Thanks for joining our SMS program! Create an account to get the best deals!

{% else %}
Thanks for joining our SMS program!

{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## Fuseaux horaires {#time-zones}

{% apitags %}
Time zones
{% endapitags %}

- [Insérer dans un modèle le fuseau horaire de l'utilisateur](#users-time-zone)
- [Personnaliser un message en fonction du fuseau horaire d'un utilisateur](#personalize-timezone)
- [Ajouter le fuseau horaire CST à un attribut personnalisé](#time-append-cst)
- [Insérer un horodatage](#time-insert-timestamp)
- [Envoyer une notification push Canvas uniquement pendant une fenêtre horaire dans le fuseau horaire local de l'utilisateur](#time-canvas-window)
- [Envoyer une campagne de messages in-app récurrente pendant une fenêtre horaire dans le fuseau horaire local de l'utilisateur](#time-reocurring-iam-window)
- [Envoyer des messages différents en semaine et le week-end dans le fuseau horaire local de l'utilisateur](#time-weekdays-vs-weekends)
- [Envoyer des messages différents en fonction de l'heure de la journée dans le fuseau horaire local de l'utilisateur](#time-of-day)
- [Annuler un message en dehors d'une plage horaire au moment de l'envoi](#abort-send-time-hour-range)
- [Annuler un message en dehors d'une fenêtre horaire dans un fuseau horaire fixe](#abort-fixed-timezone-window)

{% alert note %}
Si un utilisateur reçoit un message à une heure locale inattendue, le fuseau horaire de son appareil ou de son profil a peut-être changé (par exemple, après un voyage). La distribution en heure locale utilise le fuseau horaire du profil au moment de l'envoi ; les utilisateurs peuvent avoir besoin d'une nouvelle session dans leur région habituelle avant que des valeurs telles que {% raw %}`{{${time_zone}}}`{% endraw %} reflètent ce que vous attendez. Cependant, vous pouvez [insérer dans un modèle le fuseau horaire de l'utilisateur](#users-time-zone).
{% endalert %}

### Insérer dans un modèle le fuseau horaire de l'utilisateur {#users-time-zone}

Par défaut, les dates et heures dans Liquid sont affichées en temps universel coordonné (UTC). Pour afficher les dates et heures dans le fuseau horaire local de l'utilisateur, utilisez le filtre `time_zone` avec le filtre `date`.

#### Assigner la date et l'heure locales {#assign-local-date-and-time}

Pour assigner une variable qui reflète la date et l'heure actuelles dans le fuseau horaire local de l'utilisateur, utilisez ce format :

{% raw %}
```liquid
{% assign local_date_time = 'now' | time_zone:{{${time_zone}}} | date: '%B %e, %Y' %}
{{local_date_time}}
```
{% endraw %}

- `now` : récupère la date et l'heure actuelles en UTC.
- `time_zone` : récupère le fuseau horaire local de l'utilisateur à partir de l'attribut par défaut en utilisant la balise de personnalisation {% raw %}`{{${time_zone}}}`{% endraw %}.
- `date` : formate la date et l'heure locales de l'utilisateur selon vos spécifications. Dans l'exemple précédent, le système affiche une chaîne formatée comme « February 26, 2026 ». Pour plus d'options de formatage, consultez [strftime.net](strftime.net).

#### Appliquer le fuseau horaire de l'utilisateur avec des attributs personnalisés {#apply-the-users-time-zone-with-custom-attributes}

Vous pouvez appliquer le filtre `time_zone` aux attributs personnalisés, comme ceci :

{% raw %}
```liquid
{{custom_attribute.${date_time_attribute} | time_zone: {{${time_zone}}} | date: '%a, %b %e, %Y'}}
```
{% endraw %}

Cela affiche le `date_time_attribute` formaté avec le jour de la semaine abrégé, suivi du mois abrégé, du jour et de l'année à quatre chiffres.

### Personnaliser un message en fonction du fuseau horaire d'un utilisateur {#personalize-timezone}

Ce cas d'utilisation affiche différents messages en fonction du fuseau horaire d'un utilisateur.

{% raw %}
```liquid
{% if {{${time_zone}}} == 'xx' %}
Message for time zone xx.
{% elsif {{${time_zone}}} == 'yy' %}
Message for time zone yy.
{% else %}
{% abort_message("Invalid time zone") %}
{% endif %}
```
{% endraw %}

### Ajouter le fuseau horaire CST à un attribut personnalisé {#time-append-cst}

Ce cas d'utilisation affiche un attribut de date personnalisé dans un fuseau horaire donné.

Option 1 :
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone: -0005 | date: '%B, %d %Y' }}
```
{% endraw %}

Option 2 :
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone: 'America/Chicago' | date: '%B %d %Y %z' }}
```
{% endraw %}

### Insérer un horodatage {#time-insert-timestamp}

Ce cas d'utilisation affiche un message qui inclut un horodatage dans le fuseau horaire actuel de l'utilisateur.

L'exemple suivant affiche la date au format AAAA-mm-jj HH:MM:SS, par exemple 2021-05-03 10:41:04.

{% raw %}
```liquid
{{${user_id} | default: 'You'}} received a campaign, rendered at ({{ "now" | time_zone: ${time_zone} | date: "%Y-%m-%d %H:%M:%S" }})
```
{% endraw %}

### Envoyer une notification push Canvas uniquement pendant une fenêtre horaire dans le fuseau horaire local de l'utilisateur {#time-canvas-window}

Ce cas d'utilisation vérifie l'heure d'un utilisateur dans son fuseau horaire local et, si elle se situe dans une fenêtre horaire définie, affiche un message spécifique.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}

Here's a message that will send between 8 am and 8 pm!
```
{% endraw %}

### Envoyer une campagne de messages in-app récurrente pendant une fenêtre horaire dans le fuseau horaire local de l'utilisateur {#time-reoccurring-iam-window}

Ce cas d'utilisation affiche un message si l'heure actuelle de l'utilisateur se situe dans une fenêtre définie.

Par exemple, le scénario suivant informe un utilisateur qu'un magasin est fermé.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 21 or hour < 10 %}

Store's closed. Come back between 11 am and 9 pm!

{% else %}
{% abort_message("Not sent because the store is open") %}
{% endif %}
```
{% endraw %}

### Envoyer des messages différents en semaine et le week-end dans le fuseau horaire local de l'utilisateur {#time-weekdays-vs-weekends}

Ce cas d'utilisation vérifie si le jour actuel de l'utilisateur est un samedi ou un dimanche et, en fonction du jour, affiche des messages différents.

{% raw %}
```liquid
{% assign today = 'now' | time_zone: ${time_zone} | date: "%A" %}
{% if {{today}} == 'Saturday' or {{today}} == 'Sunday' %}
It's {{today}}, why don't you open the app for your transactions?

{% else %}
It's {{today}}, why don't you visit the store?
{% endif %}
```
{% endraw %}

### Envoyer des messages différents en fonction de l'heure de la journée dans le fuseau horaire local de l'utilisateur {#time-of-day}

Ce cas d'utilisation affiche un message si l'heure actuelle de l'utilisateur se situe en dehors d'une fenêtre définie.

Par exemple, vous pourriez vouloir informer un utilisateur d'une opportunité limitée dans le temps qui dépend de l'heure de la journée.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}

Check out this new bar after work today. HH specials!
```
{% endraw %}

{% alert note %} C'est l'opposé des [heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types#time-based-options). {% endalert %}

### Annuler un message en dehors d'une plage horaire au moment de l'envoi {#abort-send-time-hour-range}

Ce cas d'utilisation annule le message lorsque l'heure actuelle se situe en dehors d'une plage définie. Il utilise l'heure à laquelle le message est rendu, qui est en UTC par défaut sauf si vous appliquez le filtre `time_zone`, et non le fuseau horaire local de l'utilisateur. Pour envoyer des messages en fonction du fuseau horaire local d'un utilisateur, consultez [Envoyer des messages différents en fonction de l'heure de la journée dans le fuseau horaire local de l'utilisateur](#time-of-day).

{% raw %}
```liquid
{% assign time = 'now' %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside hour range") %}
{% endif %}

Check out this new bar after work today. HH specials!
```
{% endraw %}

### Annuler un message en dehors d'une fenêtre horaire dans un fuseau horaire fixe {#abort-fixed-timezone-window}

Ce cas d'utilisation annule le message lorsque l'heure actuelle se situe en dehors d'une fenêtre définie dans un fuseau horaire spécifique (l'heure de Singapour dans cet exemple). Vous pouvez utiliser ce modèle lorsque vous avez besoin d'une règle de type heures calmes liée à une région plutôt qu'à l'attribut `time_zone` de chaque utilisateur.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: 'Asia/Singapore' %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% assign minute = time | date: '%M' | plus: 0 %}

{% if hour < 20 or hour > 21 or (hour == 21 and minute > 45) %}
{% abort_message("Not within eligible time of 8 pm–9:45 pm SGT") %}
{% endif %}

Sign up for our exclusive time-limited offer now!
```
{% endraw %}

{% endapi %}

{% api %}

## Semaine/Jour/Mois {#weekdaymonth}

{% apitags %}
Week/Day/Month
{% endapitags %}

- [Récupérer le nom du mois précédent dans un message](#month-name)
- [Envoyer une Campaign à la fin de chaque mois](#month-end)
- [Envoyer une Campaign le dernier jour ouvrable du mois](#day-of-month-last)
- [Envoyer un message différent chaque jour du mois](#day-of-month)
- [Envoyer un message différent chaque jour de la semaine](#day-of-week)
- [Annuler un message à une date calendaire spécifique](#abort-specific-calendar-date)
- [Annuler un message un jour spécifique de la semaine](#abort-specific-weekday)

### Récupérer le nom du mois précédent dans un message {#month-name}

Ce cas d'utilisation prend le mois en cours et affiche le mois précédent pour l'utiliser dans les messages.

{% raw %}
```liquid
{% assign today = 'now' | date: "%m" %}
{% assign last_month = {{today}} | minus: 1 %}
{% if last_month == 1 %}
{% assign month = "January" %}
{% elsif last_month == 2 %}
{% assign month = "February" %}
{% elsif last_month == 3 %}
{% assign month = "March" %}
{% elsif last_month == 4 %}
{% assign month = "April" %}
{% elsif last_month == 5 %}
{% assign month = "May" %}
{% elsif last_month == 6 %}
{% assign month = "June" %}
{% elsif last_month == 7 %}
{% assign month = "July" %}
{% elsif last_month == 8 %}
{% assign month = "August" %}
{% elsif last_month == 9 %}
{% assign month = "September" %}
{% elsif last_month == 10 %}
{% assign month = "October" %}
{% elsif last_month == 11 %}
{% assign month = "November" %}
{% elsif last_month == 0 %}
{% assign month = "December" %}
{% endif %}

Here's an overview of what your spending looked like in {{month}}.
```
{% endraw %}

Vous pouvez également utiliser ce qui suit pour obtenir le même résultat.

{% raw %}
```liquid
{% assign last_month_name = 'now' | date: "%Y-%m-01" | date: '%s' | minus: 1 | date: "%B" %}

Here's an overview of what your spending looked like in {{last_month_name}}.
```
{% endraw %}

### Envoyer une Campaign à la fin de chaque mois {#month-end}

Ce cas d'utilisation vérifie si la date actuelle fait partie d'une liste de dates et, en fonction de la date, affiche un message spécifique.

{% alert note %} Cela ne prend pas en compte les années bissextiles (29 février). {% endalert %}

{% raw %}
```liquid
{% assign current_date = 'now' | date: '%b %d' %}

{% if current_date == "Jan 31" or current_date == "Feb 28" or current_date == "Mar 31" or current_date == "Apr 30" or current_date == "May 31" or current_date == "Jun 30" or current_date == "Jul 31" or current_date == "Aug 31" or current_date == "Sep 30" or current_date == "Oct 31" or current_date == "Nov 30" or current_date == "Dec 31" %}

The date is correct

{% else %}
{% abort_message("Date is not listed") %}
{% endif %}
```
{% endraw %}

### Envoyer une Campaign le dernier jour ouvrable du mois {#day-of-month-last}

Ce cas d'utilisation capture le mois et le jour actuels et calcule si le jour actuel tombe dans la dernière semaine ouvrable du mois.

Par exemple, vous pourriez vouloir envoyer un sondage à vos utilisateurs le dernier mercredi du mois pour recueillir leur avis sur le produit.

{% raw %}
```liquid
{% comment %}Pull the day, day name, month, and year from today's date.{% endcomment %}
{% assign current_day = "now" | date: "%d" %}
{% assign current_day_name = "now" | date: "%a" %}
{% assign current_month = "now" | date: "%b" %}
{% assign current_year = "now" | date: "%Y" %}

{% comment %}Assign the correct number of days for the current month.{% endcomment %}

{% if current_month == "Jan" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Mar" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Apr" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "May" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Jun" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Jul" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Aug" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Sep" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Oct" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Nov" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Dec" %}
{% assign last_day_of_month = 31 %}
{% endif %}

{% comment %}Assign the correct number of days if the current month is February, taking into account leap years.{% endcomment %}

{% assign leap_year_remainder = current_year | modulo: 4 %}
{% if leap_year_remainder == 0 and current_month == "Feb" %}
{% assign last_day_of_month = 29 %}
{% elsif current_month == "Feb" %}
{% assign last_day_of_month = 28 %}
{% endif %}

{% comment %}Check that today's date is within a week of the last day of the month. If not, abort the message. If so, check that today is Wednesday. If not, abort the message.{% endcomment %}

{% assign diff_in_days = last_day_of_month | minus: current_day | plus: 1%}
{% if diff_in_days <= 7 %}
{% unless current_day_name == "Wed" %}
{% abort_message("Wrong day of the week") %}
{% endunless %}
{% else %}
{% abort_message("Not the last week of the month") %}
{% endif %}
```
{% endraw %}

### Envoyer un message différent chaque jour du mois {#day-of-month}

Ce cas d'utilisation vérifie si la date actuelle correspond à une date dans une liste et, en fonction du jour, affiche un message distinct.

{% raw %}
```liquid
{% assign today = 'now' | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_1 = "2019-12-01" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_2 = "2019-12-02" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_3 = "2019-12-03" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}

{% if today == day_1 %}
Message for 2019-12-01

{% elsif today == day_2 %}
Message for 2019-12-02

{% elsif today == day_3%}
Message for 2019-12-03

{% else %}
{% abort_message("Date not listed") %}
{% endif %}
```
{% endraw %}

### Envoyer un message différent chaque jour de la semaine {#day-of-week}

Ce cas d'utilisation vérifie le jour actuel de la semaine et, en fonction du jour, affiche un message distinct.

{% raw %}
```liquid
{% assign today = 'now' | date: "%A" %}
{% case today %}
{% when 'Monday' %}
Monday copy

{% when 'Tuesday' %}
Tuesday copy

{% when 'Wednesday' %}
Wednesday copy

{% when  'Thursday' %}
Thursday copy

{% when  'Friday' %}
Friday copy

{% when 'Saturday' %}
Saturday copy

{% when 'Sunday' %}
Sunday copy

{% else %}
Default copy
{% endcase %}
```
{% endraw %}

{% alert note %}
Vous pouvez remplacer la ligne « Default copy » par {% raw %}`{% abort_message() %}`{% endraw %} pour empêcher l'envoi du message si le jour de la semaine est inconnu.
{% endalert %}

### Annuler un message à une date calendaire spécifique {#abort-specific-calendar-date}

Ce cas d'utilisation annule le message à un mois et un jour choisis chaque année (le 5 mai dans l'exemple). Il compare la date actuelle à une chaîne mois-jour non ambiguë construite avec le filtre `date`.

{% raw %}
```liquid
{% assign date = 'now' | date: '%d/%m' %}
{% if date == '05/05' %}
{% abort_message('No message on the 5th of May') %}
{% endif %}
```
{% endraw %}

### Annuler un message un jour spécifique de la semaine {#abort-specific-weekday}

Ce cas d'utilisation annule le message lorsque Liquid s'exécute un jour de la semaine donné (`Wednesday` dans l'exemple). Le filtre `%A` renvoie le nom complet du jour de la semaine en anglais.

{% raw %}
```liquid
{% assign weekday = 'now' | date: '%A' %}
{% if weekday == 'Wednesday' %}
{% abort_message("No message on Wednesdays") %}
{% endif %}
```
{% endraw %}

{% endapi %}

De nombreux exemples de cette bibliothèque utilisent la balise `abort_message` pour ignorer un envoi lorsque les conditions ne sont pas remplies. Pour une référence complète sur l'annulation d'envois avec Liquid, y compris les modèles basés sur la date et l'heure, consultez [Annuler les messages Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages).