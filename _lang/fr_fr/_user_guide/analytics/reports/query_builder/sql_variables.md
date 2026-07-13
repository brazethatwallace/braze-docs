---
nav_title: Variables SQL
article_title: Variables SQL du Générateur de requêtes
page_order: 2
page_type: reference
description: "Découvrez comment utiliser des variables dans le Générateur de requêtes afin de réutiliser vos requêtes et d'éviter de coder en dur des données dans votre code."
tool: Reports
---

# Variables SQL du Générateur de requêtes {#query-builder-sql-variables}

> Découvrez comment utiliser des variables SQL dans le Générateur de requêtes afin de réutiliser vos requêtes et d'éviter de coder en dur des données dans votre code.

## Pourquoi utiliser des variables SQL ? {#why-use-sql-variables}

Les avantages de l'utilisation de variables SQL incluent :

- Gagner du temps en créant une variable Campaign à sélectionner dans une liste lors de la création de votre rapport, au lieu de coller des identifiants Campaign.
- Remplacer des valeurs en ajoutant des variables qui vous permettent de réutiliser le rapport pour des cas d'utilisation légèrement différents à l'avenir (comme un événement personnalisé différent).
- Réduire les erreurs utilisateur lors de la modification de votre SQL en diminuant la quantité de modifications nécessaires pour chaque rapport. Les collègues plus à l'aise avec SQL peuvent créer des rapports que des collègues moins techniques peuvent ensuite utiliser.

## Utiliser des variables {#using-variables}

### Étape 1 : Ajouter une variable {#step-1-add-a-variable}

Pour ajouter une variable à votre requête, utilisez la syntaxe suivante :

{% raw %}
```sql
{{variable_type.${custom_label}}}
```
{% endraw %}

Remplacez les éléments suivants :

| Marque substitutive | Description |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `variable_type`   | Le type de variable prédéfini que vous souhaitez utiliser, comme `campaign` ou `catalog_fields`. Pour la liste complète, consultez [Types de variables pris en charge](#variable-types). |
| `custom_label` | Le libellé utilisé pour identifier la variable dans l'onglet **Variables** de votre Générateur de requêtes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 1 : Ajouter une variable" }

Dans l'exemple suivant, le nombre total d'utilisateurs entre le premier et le dernier jour d'un mois est interrogé pour une Campaign. Chaque variable se verra attribuer une valeur à l'étape suivante.

{% raw %}
```sql
SELECT COUNT(*) AS total_users
FROM USERS_CAMPAIGNS_REVENUE_SHARED
WHERE campaign_id = '{{campaign.${Campaign}}}'
  AND TIME > '{{start_date.${Month First Day}}}'
  AND TIME < '{{end_date.${Month Last Day}}}';
```
{% endraw %}

### Étape 2 : Attribuer une valeur {#step-2-assign-a-value}

Par défaut, l'onglet **Variables** n'est pas affiché dans le Générateur de requêtes. Il n'apparaît qu'après l'ajout de votre première variable à la requête. Vous pourrez alors lui attribuer une valeur. Les valeurs spécifiques que vous pouvez choisir dépendront du [type](#variable-types) de cette variable.

Dans l'exemple suivant, la Campaign « Summer Feature Launch » est attribuée comme valeur, ainsi que le premier et le dernier jour de juin 2025.

![L'onglet « Variables » dans le Générateur de requêtes montrant l'exemple donné.]({% image_buster /assets/img/query_builder_example.png %})

## Types de variables généraux {#variable-types}

### Nombre {#number}

`number` peut être utilisé en combinaison avec d'autres variables non-chaîne. Accepte tout nombre positif ou négatif, y compris les nombres décimaux, comme `5.5`.

{% tabs %}
{% tab utilisation %}
{% raw %}
```sql
some_number_column < {{number.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Chaîne de caractères {#string}

Pour modifier des valeurs de chaîne répétitives entre les exécutions de rapports. Utilisez cette variable pour éviter de coder en dur une valeur plusieurs fois dans votre SQL.

{% tabs %}
{% tab utilisation %}
{% raw %}
```sql
'{{string.${add a string here.}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Liste {#list}

Pour sélectionner à partir d'une liste d'options.

{% tabs local %}
{% tab choisir une option %}
{% subtabs %}
{% subtab utilisation %}
{% raw %}
```sql
{{options.${metrics} | is_radio_button: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab choisir plusieurs options %}
{% subtabs %}
{% subtab utilisation %}
{% raw %}
```sql
{{options.${metrics} | is_multi_select: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Bouton radio {#radio-button}

Pour afficher les options sous forme de boutons radio au lieu d'un menu déroulant dans l'onglet **Variables**. Cela ne peut pas être utilisé seul&#8212;il doit être utilisé en combinaison avec une [liste](#list).

{% tabs %}
{% tab utilisation %}
```sql
is_radio_button: 'true'
```
{% endtab %}
{% endtabs %}

![Un exemple de bouton radio rendu dans Braze.]({% image_buster /assets/img_archive/sql_variables_campaigns.png %}){: style="max-width:50%;"}

#### Sélection multiple {#multi-select}

Pour déterminer si le menu déroulant permet une sélection unique ou multiple. Cela ne peut pas être utilisé seul&#8212;il doit être utilisé en combinaison avec une [liste](#list).

{% tabs %}
{% tab utilisation %}
```sql
is_multi_select: 'true'
```
{% endtab %}
{% endtabs %}

![Un exemple de liste à sélection multiple rendu dans Braze.]({% image_buster /assets/img_archive/sql_variables_productname.png %}){: style="max-width:50%;"}

#### Options {#options}

Pour fournir la liste des options sélectionnables sous la forme d'un libellé et d'une valeur. Le libellé est ce qui est affiché et la valeur est ce par quoi la variable est remplacée lorsque l'option est sélectionnée. Cela ne peut pas être utilisé seul&#8212;il doit être utilisé en combinaison avec une [liste](#list).

{% tabs %}
{% tab utilisation %}
```sql
options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'
```
{% endtab %}
{% endtabs %}

## Types de variables spécifiques à Braze {#braze-specific-variable-types}

### Plage de dates {#date-range}

Pour afficher un calendrier permettant de sélectionner des dates. Remplacez `start_date` et `end_date` par un horodatage Unix en secondes pour une date spécifiée en UTC, comme `1696517353`. Vous pouvez également définir uniquement une `start_date` ou une `end_date` pour n'afficher qu'une seule date dans le calendrier. Si les libellés de votre `start_date` et `end_date` ne correspondent pas, ils seront traités comme deux dates distinctes plutôt que comme une plage de dates.

{% tabs %}
{% tab utilisation %}
{% raw %}
```
time > {{start_date.${custom_label}}} AND time < {{end_date.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

Vous pouvez définir la plage de dates sur l'une des options suivantes. Si `start_date` et `end_date` sont tous deux utilisés et partagent le même libellé, toutes les options seront affichées. Sinon, si un seul est utilisé, seule l'option spécifiée sera affichée.

| Option | Description | Valeurs requises |
| --- | --- | --- |
| Relative | Spécifie les X derniers jours | Nécessite `start_date` |
| Date de début | Spécifie une date de début | Nécessite `start_date` |
| Date de fin | Spécifie une date de fin | Nécessite `end_date` |
| Plage de dates | Spécifie à la fois une date de début et une date de fin | Nécessite à la fois `start_date` et `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Plage de dates" }

Votre Liquid sera utilisé pour afficher un calendrier dans la plage de dates donnée :

![Un exemple de calendrier rendu dans Braze.]({% image_buster /assets/img_archive/query_builder_time_range.png %}){: style="max-width:50%;"}

### Campaigns

{% tabs local %}
{% tab une Campaign %}
Pour sélectionner une Campaign. Partager le même libellé avec un Canvas entraînera l'affichage d'un bouton radio dans l'onglet **Variables** permettant de choisir entre Canvas ou Campaign.

{% subtabs %}
{% subtab utilisation %}
{% raw %}
```sql
campaign_id = '{{campaign.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab plusieurs Campaigns %}
Pour sélectionner plusieurs Campaigns. Partager le même libellé avec un Canvas entraînera l'affichage d'un bouton radio dans l'onglet **Variables** permettant de choisir entre Canvas ou Campaign.

- **Valeur de remplacement :** identifiants BSON des Campaigns

{% subtabs %}
{% subtab utilisation %}
{% raw %}
```sql
campaign_id IN ({{campaigns.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab variantes de Campaign %}
Pour sélectionner des variantes de Campaign appartenant à la Campaign sélectionnée. Cela doit être utilisé conjointement avec une variable Campaign ou Campaigns.

- **Valeur de remplacement :** identifiants API des variantes de Campaign, chaînes de caractères délimitées par des virgules comme `api-id1, api-id2`.

{% subtabs %}
{% subtab utilisation %}
{% raw %}
```sql
message_variation_api_id IN ({{campaign_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
Toutes les variables Campaign et Canvas doivent utiliser les mêmes identifiants afin de synchroniser les états au sein d'un même groupe.
{% endalert %}

### Canvas {#canvases}

{% tabs local %}
{% tab un Canvas %}
Pour sélectionner un Canvas. Partager le même libellé avec une Campaign entraînera l'affichage d'un bouton radio dans l'onglet **Variables** permettant de choisir entre Canvas ou Campaign.

- **Valeur de remplacement :** identifiant BSON du Canvas

{% subtabs %}
{% subtab utilisation %}
{% raw %}
```sql
canvas_id = '{{canvas.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab plusieurs Canvas %}
Pour sélectionner plusieurs Canvas. Partager le même libellé avec une Campaign entraînera l'affichage d'un bouton radio dans l'onglet **Variables** permettant de choisir entre Canvas ou Campaign.

- **Valeur de remplacement :** identifiants BSON des Canvas

{% subtabs %}
{% subtab utilisation %}
{% raw %}
```sql
canvas_id IN ({{canvases.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab variantes de Canvas %}
Pour sélectionner des variantes de Canvas appartenant à un Canvas choisi. Cela doit être utilisé avec une variable Canvas. Défini sur un ou plusieurs identifiants API de variantes de Canvas, sous forme de chaîne séparée par des virgules, comme dans `api-id1, api-id2`.

{% subtabs %}
{% subtab utilisation %}
{% raw %}
```sql
canvas_variation_api_id IN ({{canvas_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab une étape de Canvas %}
Pour sélectionner une étape de Canvas appartenant à un Canvas choisi. Cela doit être utilisé avec une variable Canvas.

{% subtabs %}
{% subtab utilisation %}
{% raw %}
```sql
canvas_step_api_id = '{{canvas_step.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab plusieurs étapes de Canvas %}
Pour sélectionner des étapes de Canvas appartenant à des Canvas choisis. Cela doit être utilisé avec une variable Canvas.

{% subtabs %}
{% subtab utilisation %}
{% raw %}
```sql
canvas_step_api_id IN ({{canvas_steps.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
Toutes les variables Campaign et Canvas doivent utiliser les mêmes identifiants afin de synchroniser les états au sein d'un même groupe.
{% endalert %}

### Produits {#products}

`products` est utilisé pour sélectionner un ou plusieurs produits depuis le tableau de bord de Braze.

{% tabs %}
{% tab utilisation %}
{% raw %}
```sql
({{products.${custom_label}}})
```
{% endraw %}
{% endtab %}

{% tab exemple %}
{% raw %}
```sql
SELECT product_name
FROM FULL_GAME_AND_DLC
WHERE product_id IN ({{products.${Games with DLC}}});
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Événements personnalisés {#custom-events}

Sélectionnez un ou plusieurs événements personnalisés ou propriétés d'événements personnalisés à partir d'une liste.

{% tabs local %}
{% tab événement %}
`custom_events` est utilisé pour sélectionner un ou plusieurs événements personnalisés depuis le tableau de bord de Braze.

{% subtabs %}
{% subtab utilisation %}
{% raw %}
```sql
'{{custom_events.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}

{% subtab exemple %}
{% raw %}
```sql
SELECT event_name
FROM CUSTOM_EVENTS_TABLE
WHERE event_name IN ({{custom_events.${Purchased Game}}});
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab propriétés %}
`custom_event_properties` est utilisé pour sélectionner une ou plusieurs propriétés de l'événement personnalisé actuellement sélectionné. Nécessite une variable `custom_events` définie.

{% subtabs %}
{% subtab utilisation %}
{% raw %}
```sql
name = '{{custom_event_properties.${property names)}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Espace de travail {#workspace}

`workspace` est utilisé pour sélectionner un seul espace de travail depuis le tableau de bord de Braze.

{% tabs %}
{% tab utilisation %}
{% raw %}
```sql
workspace_id = '{{workspace.${app_group_id}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Catalogues {#catalogs}

Sélectionnez un ou plusieurs catalogues ou champs de catalogue à partir d'une liste.

{% tabs local %}
{% tab catalogues %}
`catalogs` est utilisé pour sélectionner un ou plusieurs catalogues depuis le tableau de bord de Braze.

{% subtabs %}
{% subtab utilisation %}
{% raw %}
```sql
catalog_id = '{{catalogs.${catalog}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab champs de catalogue %}
`catalog_fields` est utilisé pour définir un ou plusieurs champs du catalogue actuellement sélectionné. Nécessite une variable `catalogs` définie.

{% subtabs %}
{% subtab utilisation %}
{% raw %}
```sql
field_name = '{{catalog_fields.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Segments

Pour sélectionner des Segments dont le [suivi analytique]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) est activé. Défini sur l'identifiant analytique du Segment, qui correspond aux identifiants stockés dans la colonne `user_segment_membership_ids` dans les tables où cette colonne est disponible.

{% tabs %}
{% tab utilisation %}
{% raw %}
```sql
{{segments.${analytics_segments}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Étiquettes {#tags}

Pour sélectionner des étiquettes pour les Campaigns et Canvas. Défini sur les Campaigns et Canvas avec des identifiants BSON séparés par des virgules entre guillemets simples, associés aux étiquettes sélectionnées.

{% tabs %}
{% tab utilisation %}
{% raw %}
```sql
{{tags.${some tags}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Métadonnées de variable {#variable-metadata}

Les métadonnées peuvent être attachées à une variable pour modifier son comportement en les ajoutant avec un caractère pipe ( &#124; ) après le libellé de la variable. L'ordre des métadonnées n'a pas d'importance et vous pouvez en ajouter autant que nécessaire. De plus, tous les types de métadonnées peuvent être utilisés pour n'importe quelle variable, à l'exception des métadonnées spéciales qui sont spécifiques à certaines variables (cela sera indiqué dans ces cas). L'utilisation de toutes les métadonnées est facultative et sert à modifier le comportement par défaut de la variable.

{% tabs %}
{% tab utilisation %}
{% raw %}
```sql
{{string.${my var}| is_required: 'false' | description: 'My optional string var'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Valeur booléenne {#boolean}

Pour savoir si la valeur d'une variable est remplie. Cela est utile pour les variables facultatives où vous souhaitez court-circuiter une condition si la valeur d'une variable n'est pas remplie. Peut être défini sur `true` ou `false` en fonction de la valeur de l'autre variable.

{% tabs %}
{% tab utilisation %}
{% raw %}
```sql
{{string.${type_name_has_no_value} | visible: 'false'}} or {{string.${type_name_has_value} | visible: 'false'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

`type` et `name` font référence à la variable référencée. Par exemple, pour court-circuiter la variable facultative suivante : {% raw %}`{{campaigns.${messaging}}`{% endraw %} :

{% raw %}
```sql
{{string.${campaigns_messaging_has_no_value}  | visible: 'false'}} OR campaign_id IN ({{campaigns.${messaging} | is_required: 'false'}})
```
{% endraw %}

### Visible {#visible}

Pour déterminer si les variables sont visibles. Toutes les variables sont visibles par défaut dans l'onglet **Variables**, où vous pouvez saisir des valeurs.

Il existe plusieurs variables spéciales dont la valeur dépend d'une autre variable, par exemple si une autre variable a une valeur. Ces variables spéciales sont marquées comme non visibles afin qu'elles n'apparaissent pas dans l'onglet **Variables**.

{% tabs %}
{% tab utilisation %}
```sql
visible: 'false'
```
{% endtab %}
{% endtabs %}

### Requis {#required}

Pour déterminer si les variables sont requises par défaut. Une valeur vide pour une variable conduit généralement à une requête incorrecte.

{% tabs %}
{% tab utilisation %}
```sql
required: 'false'
```
{% endtab %}
{% endtabs %}

### Ordre {#order}

Pour sélectionner la position de la variable dans l'onglet **Variables**.

{% tabs %}
{% tab utilisation %}
```sql
order: '1'
```
{% endtab %}
{% endtabs %}

### Inclure des guillemets {#include-quotes}

{% tabs local %}
{% tab guillemets simples %}
Pour entourer les valeurs d'une variable avec des guillemets simples.

{% subtabs %}
{% subtab utilisation %}
```sql
include_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab guillemets doubles %}
Pour entourer les valeurs d'une variable avec des guillemets doubles.

{% subtabs %}
{% subtab utilisation %}
```sql
include_double_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Marque substitutive {#placeholder}

Pour spécifier le texte de marque substitutive affiché dans le champ de saisie de la variable.

{% tabs %}
{% tab utilisation %}
```sql
placeholder: 'enter some value'
```
{% endtab %}
{% endtabs %}

### Description {#description}

Pour spécifier le texte de description affiché sous le champ de saisie de la variable.

{% tabs %}
{% tab utilisation %}
```sql
description: 'some description'
```
{% endtab %}
{% endtabs %}

### Valeur par défaut {#default-value}

Pour spécifier la valeur par défaut de la variable lorsqu'aucune valeur n'est spécifiée.

{% tabs %}
{% tab utilisation %}
```sql
default_value: '5'
```
{% endtab %}
{% endtabs %}

### Masquer le libellé {#hide-label}

Pour masquer le libellé de la variable.

{% tabs %}
{% tab utilisation %}
```sql
hide_label: 'true'
```
{% endtab %}
{% endtabs %}