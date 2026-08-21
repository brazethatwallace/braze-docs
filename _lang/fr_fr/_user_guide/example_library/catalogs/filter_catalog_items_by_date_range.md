---
nav_title: Filtrer par plage de dates
article_title: Filtrer les éléments de catalogue par plage de dates
page_order: 1
page_type: reference
description: "Utilisez les sélections de catalogue avec des expressions de date Liquid pour afficher les éléments de catalogue dans une fenêtre temporelle glissante, comme les événements des sept prochains jours."
---

# Filtrer les éléments de catalogue par plage de dates {#filter-catalog-items-by-date-range}

> Cet exemple montre comment une place de marché de billets fictive utilise les sélections de catalogue et les expressions de date Liquid pour n'envoyer par e-mail aux consommateurs que les événements à venir dans les sept prochains jours à partir du moment de l'envoi. Vous créez une sélection avec des filtres temporels glissants, puis vous affichez les éléments de catalogue correspondants dans une Campaign ou un message Canvas.

## À propos de cet exemple {#about-this-example}

MovieCanon, une place de marché de billets fictive, utilise ce modèle pour s'assurer que les campagnes par e-mail ne listent que les concerts et spectacles pertinents dans le temps.

Ce modèle utilise deux fonctionnalités de Braze ensemble :

- Une [sélection de catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) avec des filtres de champ `time` dont les valeurs sont des extraits de code Liquid qui calculent une fenêtre temporelle glissante au moment de l'envoi
- L'étiquette Liquid {% raw %}`{% catalog_selection_items %}`{% endraw %} dans le corps du message pour afficher les lignes de catalogue correspondantes

## Considérations {#considerations}

- Créez un champ de catalogue `time` pour la colonne datetime sur laquelle vous filtrez, et non un champ string. Stockez les valeurs au format [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601), par exemple `2026-06-20T19:30:00Z`. Pour les types pris en charge, consultez [Types de données pris en charge]({{site.baseurl}}/user_guide/data/activation/catalogs/create#supported-data-types).
- Les opérateurs `before` et `after` utilisent des comparaisons strictes. Les événements exactement égaux à un horodatage limite peuvent être exclus. Utilisez des horodatages complets lorsque vous avez besoin que la fenêtre commence au moment de l'envoi. Les valeurs de date seule `YYYY-MM-DD` sont converties en minuit UTC ce jour-là.
- Le Liquid dans les filtres de sélection est évalué au moment de l'envoi. La variable `'now'` reflète le moment où le message est rendu, généralement en UTC. Vérifiez que la fenêtre résultante correspond à votre intention à travers les fuseaux horaires.
- Le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), les [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks), les tags de catalogue et `abort_message` ne sont pas pris en charge dans les valeurs de filtre de sélection de catalogue. Si un filtre inclut une étiquette non autorisée, la sélection ne renvoie aucun élément sans générer d'erreur.
- Vous pouvez ajouter jusqu'à 10 filtres par sélection et renvoyer jusqu'à 50 éléments. Ajustez la fenêtre de sept jours en modifiant les secondes ajoutées à `'now'` (`604800` = 7 jours multipliés par `86400` secondes par jour).
- Les tableaux de résultats de sélection de catalogue sont indexés à partir de zéro (`items[0]` est le premier élément).
- Testez le Liquid des filtres, le Liquid du message et la logique d'abandon en dehors de votre espace de travail de production avant d'envoyer à des audiences de production.

## Configuration {#setup}

Cet exemple suppose un catalogue nommé `live_events` avec les champs suivants :

| Champ | Type | Exemple de valeur |
| ----- | ---- | ----------------- |
| `id` | String | `show-1042` |
| `event_name` | String | `Summer Jazz Night` |
| `event_date_time` | Time | `2026-06-20T19:30:00Z` |
| `ticket_price` | Number | `45` |
| `city` | String | `Austin` |
| `venue` | String | `Riverside Amphitheater` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Champs du catalogue" }

Si vous n'avez pas encore de catalogue similaire, [créez un catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/create) et importez ou synchronisez vos données d'événements au préalable.

### Étape 1 : Créer la sélection de catalogue {#step-1-create-the-catalog-selection}

1. Accédez à **Data Settings** > **Catalogs** et sélectionnez le catalogue `live_events`.
2. Ouvrez l'onglet **Selection** et sélectionnez **Create Selection**.
3. Nommez la sélection `seven_day_window` et ajoutez une description facultative, par exemple « Événements se produisant dans les sept prochains jours. »
4. Définissez une **Results limit** pour le nombre maximum d'événements à renvoyer (jusqu'à 50).
5. N'enregistrez pas encore. Ajoutez les filtres de date dans les étapes suivantes.

### Étape 2 : Ajouter le filtre de borne supérieure {#step-2-add-the-upper-bound-filter}

Ajoutez un filtre sur le champ `event_date_time` :

| Paramètre | Valeur |
| ---------- | ------ |
| **Filter field** | `event_date_time` |
| **Operator** | `before` |
| **Value** | Extrait de code Liquid |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paramètres du filtre de borne supérieure" }

Dans le champ de valeur du filtre, saisissez cet extrait de code Liquid. Il calcule un horodatage sept jours après le moment de l'envoi :

{% raw %}
```liquid
{% assign seven_days = 'now' | date: '%s' | plus: 604800 %}{{ seven_days | date: "%Y-%m-%dT%H:%M:%SZ" }}
```
{% endraw %}

Cela définit la borne supérieure de la fenêtre afin que seuls les événements antérieurs à cet horodatage soient inclus.

### Étape 3 : Ajouter le filtre de borne inférieure {#step-3-add-the-lower-bound-filter}

Ajoutez un second filtre sur le même champ :

| Paramètre | Valeur |
| ---------- | ------ |
| **Filter field** | `event_date_time` |
| **Operator** | `after` |
| **Value** | Extrait de code Liquid |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paramètres du filtre de borne inférieure" }

Saisissez cet extrait de code Liquid pour la borne inférieure. Il utilise l'heure d'envoi actuelle afin que les événements déjà commencés soient exclus :

{% raw %}
```liquid
{{ 'now' | date: "%Y-%m-%dT%H:%M:%SZ" }}
```
{% endraw %}

Ensemble, les deux filtres renvoient les éléments de catalogue dont `event_date_time` est postérieur à l'heure d'envoi actuelle et antérieur à sept jours après l'heure d'envoi. Sélectionnez **Create Selection** pour enregistrer.

### Étape 4 : Référencer la sélection dans un message {#step-4-reference-the-selection-in-a-message}

Dans votre Campaign ou votre message Canvas, insérez du Liquid qui récupère les éléments de la sélection. Vous pouvez utiliser **Add personalization** (**Catalog Items** > **Use a selection**) ou coller l'étiquette manuellement :

{% raw %}
```liquid
{% catalog_selection_items live_events seven_day_window %}
Here are some upcoming events:

{{ items[0].event_name }} — ${{ items[0].ticket_price }}
{{ items[0].city }} · {{ items[0].venue }}

{{ items[1].event_name }} — ${{ items[1].ticket_price }}
{{ items[1].city }} · {{ items[1].venue }}
```
{% endraw %}

Remplacez les index de tableau codés en dur par une boucle si vous devez afficher un nombre variable de résultats.

### Étape 5 : Gérer les résultats vides {#step-5-handle-empty-results}

Lorsqu'aucun élément de catalogue ne correspond à la sélection, le tableau `items` est vide et le bloc balisé n'affiche rien. Pour ignorer l'envoi ou afficher un contenu de remplacement, encadrez l'étiquette dans une condition :

{% raw %}
```liquid
{% catalog_selection_items live_events seven_day_window %}
{% if items.size == 0 %}
{% abort_message('Catalog selection returned 0 items') %}
{% endif %}

Here are some upcoming events:
{{ items[0].event_name }}
```
{% endraw %}

Pour en savoir plus, consultez [Abandon de messages]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages).

## Articles connexes {#related-articles}

- [Créer un catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/create)
- [Sélections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)
- [Utiliser des catalogues dans les campagnes]({{site.baseurl}}/user_guide/data/activation/catalogs/use)
- [Filtre Liquid `date`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters#date-filter)
- [Bibliothèque de cas d'usage Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases)