---
nav_title: Synchronisation des produits Shopify
article_title: Synchronisation des produits Shopify
alias: /shopify_catalogs/
page_order: 5
description: "Cet article de référence explique comment importer vos produits Shopify dans les catalogues Braze."
---

# Synchronisation des produits Shopify {#shopify-product-sync}

> Vous pouvez synchroniser tous les produits de votre boutique Shopify avec un [catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/) Braze pour une personnalisation plus poussée des messages.

Les catalogues Shopify se mettent à jour en quasi-temps réel à mesure que vous apportez des modifications aux produits de votre boutique Shopify. Vous pouvez enrichir votre panier abandonné, votre confirmation de commande et bien plus encore avec les détails et informations produit les plus à jour.

En plus de prendre en charge les [données produit Shopify de base](#supported-shopify-catalog-data), vous pouvez synchroniser les collections Shopify, les étiquettes de produit et les métachamps de produit vers votre catalogue Braze. Ces champs supplémentaires permettent une personnalisation plus riche, des sélections de catalogue plus précises et une segmentation plus puissante grâce aux [Extensions de segments]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/).

## Configurer la synchronisation des produits Shopify {#set-up}

Si vous avez déjà installé votre boutique Shopify, vous pouvez toujours synchroniser vos produits en suivant les instructions ci-dessous.

### Étape 1 : Activer la synchronisation {#step-1-turn-on-the-sync}

Vous pouvez synchroniser vos produits avec un catalogue Braze via le flux d'installation Shopify ou sur la page partenaire Shopify.

![Étape 3 du processus de configuration avec « Shopify Variant ID » comme « identifiant de produit du catalogue ».]({% image_buster /assets/img/shopify/sync_products_step1.png %})

### Étape 2 : Sélectionner votre identifiant de produit {#step-2-select-your-product-identifier}

Sélectionnez l'identifiant de produit à utiliser comme ID de catalogue :
- Shopify Variant ID
- SKU

Les valeurs d'ID et d'en-tête pour l'identifiant de produit que vous choisissez ne peuvent inclure que des lettres, des chiffres, des tirets et des underscores. Si l'identifiant de produit ne respecte pas ce format, Braze le filtrera de votre synchronisation de catalogue.

Il s'agira de l'identifiant principal que vous utiliserez pour référencer les informations du catalogue Braze.

{% alert note %}
Si vous sélectionnez SKU comme ID de votre catalogue, assurez-vous que tous vos produits et variantes dans votre boutique ont un SKU défini et qu'il est unique.<br><br>
- Si un article n'a pas de SKU, Braze ne peut pas synchroniser ce produit dans le catalogue.
- Si plusieurs produits possèdent le même SKU, cela peut entraîner un comportement inattendu ou l'écrasement involontaire des informations du produit par le SKU en double.
{% endalert %}

### Étape 3 : Configurer des données produit supplémentaires (facultatif) {#step-3}

Vous pouvez activer de manière facultative la synchronisation des étiquettes de produit, des collections Shopify et des métachamps. Activez ou modifiez ces paramètres après la synchronisation initiale depuis la page partenaire Shopify.

{% alert note %}
Ajoutez d'abord les étiquettes de produit, les collections Shopify et les métachamps dans Shopify. S'ils n'existent pas dans Shopify, ils n'apparaîtront pas dans Braze.
{% endalert %}

![Paramètres de synchronisation des produits et variantes Shopify vers Braze.]({% image_buster /assets/img/shopify/additional_product_data.png %})

{% tabs global %}
{% tab Étiquettes de produit %}

1. Sur la page **Synchroniser les données produit vers Braze**, cochez la case **Synchroniser les étiquettes de produit** pour ouvrir la fenêtre modale **Sélectionner les étiquettes de produit**.
2. Sélectionnez jusqu'à 20 étiquettes de produit à synchroniser avec votre catalogue Braze. Seules les étiquettes que vous sélectionnez seront synchronisées.

![Fenêtre modale de sélection des étiquettes de produit avec une sélection d'étiquettes.]({% image_buster /assets/img/shopify/select_product_tags.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Métachamps de produit %}

1. Si vous disposez d'une intégration Shopify existante, réautorisez l'application Braze Shopify pour installer les nouvelles autorisations requises pour la synchronisation des produits. Si vous êtes un nouveau client, passez à l'étape suivante.

![Bannière invitant à réautoriser l'application Braze Shopify.]({% image_buster /assets/img/shopify/banner_to_reauthorize.png %})

{: start="2"}
2. Sélectionnez **Synchroniser les métachamps de produit** pour ouvrir la fenêtre modale de configuration des métachamps.

![Section de synchronisation des données produit vers Braze avec des options à sélectionner parmi plusieurs paramètres, y compris les collections.]({% image_buster /assets/img/shopify/select_collections.png %})

{: start="3"}
3. Sélectionnez jusqu'à 20 métachamps recherchables à synchroniser. Chacun devient une colonne distincte dans votre catalogue, utilisable dans des fonctionnalités comme les sélections de catalogue ou les Extensions de segments.
- Lors du nommage des métachamps, notez que les espaces deviennent « _ » et que tous les caractères spéciaux sont supprimés pour respecter les restrictions de nommage des champs de catalogue Braze.

![Fenêtre modale de sélection des métachamps de produit.]({% image_buster /assets/img/shopify/select_metafields.png %}){: style="max-width:80%;"}

{% subtabs %}
{% subtab Métachamps pris en charge %}

Braze prend en charge les objets de métachamps suivants ainsi que certains de leurs types respectifs.

| Type de métachamp | Type de données |
|--------------------------------------------------|--------------------------------------------------------|
| `boolean` | Valeur booléenne |
| `color`, `list.color` | Chaîne de caractères (couleur hexadécimale, comme `#FFF123`), Tableau de chaînes de caractères |
| `date`, `list.date` | Chaîne de caractères (date ISO 8601), Tableau de chaînes de caractères (dates ISO 8601) |
| `date_time`, `list.date_time` | Chaîne de caractères (datetime ISO 8601), Tableau de chaînes de caractères (datetimes ISO 8601) |
| `id`, `list.id` | Chaîne de caractères, Tableau de chaînes de caractères |
| `multi_line_text_field` | Chaîne de caractères |
| `number_decimal` | Chaîne de caractères |
| `number_integer` | Entier |
| `single_line_text_field`, `list.single_line_text_field` | Chaîne de caractères, Tableau de chaînes de caractères |
| `url`, `list.url` | Chaîne de caractères (URL), Tableau de chaînes de caractères (URL) |
| `metaobject_reference`, `list.metaobject_reference` | Chaîne de caractères, Tableau de chaînes de caractères |
| `mixed_reference`, `list.mixed_reference` | Chaîne de caractères, Tableau de chaînes de caractères |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 3 : Configurer des données produit supplémentaires (facultatif) #step-3" }

{% endsubtab %}
{% subtab Métachamps non pris en charge %}

Braze ne prend pas en charge les objets de métachamps suivants, y compris certains types de liste respectifs :

- `dimension` (`list.dimension`)
- `weight` (`list.weight`)
- `link` (`list.link`)
- `json`
- `list.number_decimal`
- `list.number_integer`
- `money`
- `rating` (`list.rating`)
- `volume` (`list.volume`)
- `rich_text_field`

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Collections %}

1. Sélectionnez **Synchroniser les collections Shopify** pour ouvrir la fenêtre modale de configuration des collections.
2. Sélectionnez jusqu'à 20 collections à synchroniser.
  - La fenêtre modale fournit une liste recherchable des 5 000 collections les plus récemment créées ou mises à jour de votre boutique Shopify.
  - Les collections précédemment sélectionnées qui ne figurent plus dans les 5 000 premières apparaîtront toujours dans votre sélection.

{% alert note %}
Braze utilise l'ID de collection Shopify pour identifier les collections synchronisées, qui sont ensuite utilisées lors de la création de sélections de catalogue et de filtres de segments.
{% endalert %}

![Fenêtre modale de sélection des collections depuis un menu déroulant.]({% image_buster /assets/img/shopify/selected_collections.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

{% alert tip %}
Pour des exemples d'utilisation de chaque type de données produit, consultez les [cas d'utilisation des catalogues Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/?tab=shopify%20product%20metafields#shopify-catalog-use-cases).
{% endalert %}

### Étape 4 : Suivre la progression de la synchronisation {#step-4-track-your-sync-progress}

Après avoir enregistré votre configuration, Braze commencera à synchroniser vos produits et mettra à jour le statut sur **En cours** sur votre page partenaire Shopify. Le temps de synchronisation dépend du nombre de produits et de variantes dans votre boutique.

Vous pouvez quitter la page une fois la synchronisation en cours ; Braze vous enverra une notification sur le tableau de bord lorsque la synchronisation sera terminée. Une fois terminée, le statut passera à **Actif** et vous pourrez consulter vos produits en sélectionnant le nom du catalogue sur votre page partenaire Shopify.

![Page des paramètres d'intégration avec un statut de synchronisation des produits.]({% image_buster /assets/img/shopify/track_sync_progress.png %})

Vous pouvez également consulter les étiquettes de produit, les métachamps et les collections synchronisés dans votre catalogue Shopify sous forme de nouvelles colonnes.

![Catalogue Shopify avec des données synchronisées.]({% image_buster /assets/img/shopify/synced_catalog.png %})

{% alert important %}
Si votre synchronisation dépasse votre limite de stockage de catalogue, Braze arrête la synchronisation et les nouvelles mises à jour de produits ne sont plus reflétées. Contactez votre gestionnaire de la satisfaction client pour mettre à niveau votre niveau si nécessaire.
{% endalert %}

### Étape 5 : Gérer votre configuration {#step-5-manage-your-configuration}

Chaque type de synchronisation dispose d'une carte récapitulative sur la page partenaire Shopify affichant le nombre total synchronisé, le statut actuel et un lien vers votre catalogue. Sélectionnez l'icône d'affichage pour consulter votre configuration active et la modifier.

Vous pouvez modifier votre synchronisation de produits Shopify, y compris la gestion de vos étiquettes de produit, collections et métachamps de produit, à tout moment depuis la page partenaire Shopify.

![Page des paramètres d'intégration avec une synchronisation active du catalogue de produits.]({% image_buster /assets/img/shopify/active_catalog_sync.png %})

{% alert important %}
La modification de vos sélections synchronisées peut affecter les Campaigns, Canvas ou sélections de catalogue actifs qui y font référence. Mettez à jour le contenu actif pour qu'il fonctionne correctement lorsque vous appliquez les modifications.
{% endalert %}

## Données de catalogue Shopify prises en charge {#supported-shopify-catalog-data}

| Champ | Type de données | Exemples |
|----------------------|----------------|-----------------------------------------------------------------------------------|
| `id` | chaîne de caractères | `45264808411274` lorsque l'identifiant de produit du catalogue est **Shopify Variant ID**<br><br>`12345` lorsque l'identifiant de produit du catalogue est **SKU** (correspond à la valeur que vous avez sélectionnée à l'[étape 2](#step-2-select-your-product-identifier)) |
| `store_name` | chaîne de caractères | "your-store" (sous-domaine de la boutique Shopify, sans `.myshopify.com`) |
| `shopify_product_id` | nombre | `7939032613002` (stocké sous forme de nombre dans votre catalogue Braze ; les API Shopify peuvent renvoyer cet ID sous forme de chaîne de caractères) |
| `shopify_variant_id` | nombre | `45264808411274` (stocké sous forme de nombre dans votre catalogue Braze ; les API Shopify peuvent renvoyer cet ID sous forme de chaîne de caractères) |
| `product_title` | chaîne de caractères | "Classic leather jacket" |
| `variant_title` | chaîne de caractères | "Large / Red", "Medium" ou "Default Title" pour les produits à variante unique |
| `status` | chaîne de caractères | "active", "draft", "archived" |
| `product_image_url` | chaîne de caractères | "https://cdn.shopify.com/s/files/1/0641/0970/7402/files/t_shir.jpg?v=1736538760" |
| `variant_image_url` | chaîne de caractères | Même URL de type CDN que l'image du produit lorsqu'aucune image de variante n'existe ; sinon une URL d'image spécifique à la variante |
| `vendor` | chaîne de caractères | "Flash and Thread", "PantsLabyrinth" |
| `product_type` | chaîne de caractères | "Outerwear", "T-Shirts" (depuis le champ **Product type** du produit dans Shopify) |
| `product_url` | chaîne de caractères | "https://your-store.myshopify.com/products/classic-leather-jacket" |
| `product_handle` | chaîne de caractères | "classic-leather-jacket" |
| `published_scope` | chaîne de caractères | "web", "global" |
| `price` | nombre | `10.00`, `24.99`<br><br>Shopify renvoie souvent les prix sous forme de chaînes de caractères (par exemple `"199.00"` dans l'API REST Admin). Braze les convertit en nombres pour ce champ de catalogue. |
| `compare_at_price` | nombre | `15.00` lorsque le champ **Compare at price** est défini dans Shopify<br><br>`0` lorsque Shopify n'a pas de prix de comparaison. Les API Shopify renvoient généralement `null` pour un prix de comparaison non défini ; Braze stocke `0` dans le catalogue afin que le champ soit toujours numérique (il s'agit d'une valeur par défaut de Braze, et non d'une valeur envoyée par Shopify sous forme de `0`). |
| `inventory_quantity` | nombre | `20`, `0` ou une valeur négative lorsque la survente est autorisée (par exemple `-18`) |
| `options` | chaîne de caractères | "Size,Color"<br><br>Shopify autorise jusqu'à trois types d'options par produit (par exemple Size, Color, Material). La valeur `options` est une liste de ces noms séparés par des virgules. |
| `option_values` | chaîne de caractères | "Medium,Red", "Large,Red"<br><br>Chaque valeur correspond au même ordre que `options` (jusqu'à trois valeurs). |
| `sku` | chaîne de caractères | "12345", "SKU-001-RED-L" |
| `product_tags` | tableau | `["Summer", "Sale", "New"]`<br><br>Nécessite la synchronisation des étiquettes de produit. |
| `collection_ids` | tableau | `[123456789012, 987654321098]` (ID de collections Shopify)<br><br>Nécessite la synchronisation des collections Shopify. |
| `Metafield columns` | Varie selon le type | Chaque métachamp synchronisé apparaît sous forme de colonne distincte nommée par sa clé. Consultez les [métachamps pris en charge](#step-3) dans l'onglet « Métachamps de produit » de l'étape 3 pour plus d'informations. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Données de catalogue Shopify prises en charge" }

{% alert warning %}
Votre catalogue Shopify est géré par Shopify. Pour mettre à jour votre catalogue, apportez les modifications directement dans votre boutique Shopify, et elles seront automatiquement synchronisées avec Braze. Pour supprimer votre catalogue Shopify, accédez à la page partenaire Shopify dans Braze et [désactivez la synchronisation](#deactivate).
{% endalert %}

## Cas d'utilisation des catalogues Shopify {#shopify-catalog-use-cases}

Ces cas d'utilisation montrent comment vous pouvez exploiter les données de votre catalogue Shopify synchronisé pour personnaliser vos messages.

{% alert warning %}
Braze synchronise jusqu'à 250 variantes de chaque produit Shopify dans votre catalogue. Les variantes au-delà de cette limite ne sont pas synchronisées. Si vous avez besoin de plus de 250 variantes par produit, contactez votre gestionnaire de la satisfaction client Braze.
{% endalert %}

{% tabs %}
{% tab Étiquettes de produit %}

Utilisez les étiquettes de produit pour personnaliser les messages en fonction de la catégorisation de vos produits dans Shopify. Par exemple, vous pouvez envoyer une promotion présentant tous les produits étiquetés « Summer Sale » via une [sélection de catalogue]({{site.baseurl}}/catalog_selections/), ou créer un segment d'utilisateurs ayant acheté des produits étiquetés « Premium ».

Les étiquettes de produit sont stockées sous forme de champ tableau sur chaque élément du catalogue. Pour configurer la synchronisation des étiquettes de produit, consultez [Étiquettes de produit Shopify](#shopify-product-tags).

### Sélection de catalogue {#catalog-selection}

1. Dans Shopify, attribuez aux produits concernés l'étiquette de produit « Women's ».

![Un type de produit « Women's - Sweaters » avec les étiquettes « Women's », « Sweaters » et « Men ».]({% image_buster /assets/img/shopify/product_tag_womens.png %}){: style="max-width:40%;"}

{: start="2"}
2. Dans Braze, activez la synchronisation des étiquettes et sélectionnez l'étiquette de produit « Women's ».

![Fenêtre modale de sélection des étiquettes de produit Shopify, avec 15 étiquettes liées aux vêtements sélectionnées, dont « Women's ».]({% image_buster /assets/img/shopify/select_product_tags_womens.png %}){: style="max-width:80%;"}

### Personnalisation {#personalization}

{% alert note %}
Lorsque vous référencez des étiquettes de produit ou des collections dans les sélections de catalogue, utilisez uniquement la valeur elle-même sans les crochets `[]` ni les guillemets `""` qui apparaissent dans les données du catalogue. Par exemple, si une étiquette de produit s'affiche sous la forme `["Women's"]` dans votre catalogue, écrivez `Women's` dans votre filtre de sélection.
{% endalert %}

1. Créez une sélection de catalogue qui filtre les produits possédant l'étiquette de produit correspondante, comme « Women's ». Vous ne pouvez utiliser qu'un seul champ tableau unique au sein d'une même sélection de catalogue, et jusqu'à 50 produits dans votre sélection de catalogue.

![Une sélection de catalogue qui filtre les étiquettes de produit ayant l'attribut « Women's ».]({% image_buster /assets/img/shopify/edit_product_tags_selection.png %})

{: start="2"}
2. Dans le compositeur de messages, ajoutez la sélection à l'endroit où vous souhaitez intégrer les produits de la sélection de catalogue étiquetés « Women's ». Par exemple, vous pourriez utiliser un bloc produit HTML comme celui-ci :

{% raw %}
```liquid
{% catalog_selection_items se-team-ecommerce_shopify_catalog womens_clothing %}

{% if items[0] == blank %}
{% abort_message('Catalog selection returned no items') %}
{% endif %}

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">
  {% for item in items %}
  {% if forloop.index0 < 3 %}
  {% assign title = item.product_title | default: '' %}
  {% assign image_url = item.variant_image_url | default: '' %}
  {% assign price = item.price | default: '' %}
  {% assign url = item.product_url | default: '' %}

  <tr>
    <td width="200" valign="top" style="padding:12px 12px 12px 0;">
      {% if image_url == blank %}
      <div style="width:200px;height:200px;background:#f2f2f2;line-height:200px;text-align:center;font-family:Arial,sans-serif;font-size:12px;color:#666;">
        No image
      </div>
      {% else %}
        {% if url == blank %}
        <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
        {% else %}
        <a href="{{ url }}" style="text-decoration:none;">
          <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
        </a>
        {% endif %}
      {% endif %}
    </td>

    <td valign="top" style="padding:12px 0;font-family:Arial,sans-serif;font-size:14px;line-height:20px;color:#111;">
      {% if title != blank %}<div style="font-weight:600;">{{ title | escape }}</div>{% endif %}
      {% if price != blank %}<div>Price: ${{ price }}</div>{% endif %}
      {% if url != blank %}<div><a href="{{ url }}" style="color:#F84B09;">View product</a></div>{% endif %}
    </td>
  </tr>
  {% endif %}
  {% endfor %}
</table>
```
{% endraw %}

Ou, si vous souhaitez mentionner des produits spécifiques étiquetés « Women's » dans une notification push, vous pouvez utiliser l'outil **Ajouter une personnalisation** et spécifier vos éléments de catalogue.

{% raw %}
```liquid
Checkout the latest women's clothing:
    {% catalog_selection_items se-team-ecommerce_shopify_catalog womens_clothing %}
    {{ items[0].product_title}}{{items[0].price}}
    {{ items[1].product_title}}{{items[1].price}}
    {{ items[2].product_title}}{{items[2].price}}
```
{% endraw %}

![Compositeur de notification push avec une sélection de catalogue intégrant trois éléments avec une étiquette de produit.]({% image_buster /assets/img/shopify/add_personalization_product_tags.png %})

### Segmentation par catalogue (SQL) {#catalog-segmentation-sql}

Utilisez les [Extensions de segments]({{site.baseurl}}/user_guide/audience/segments/segment_extension/) pour créer des segments basés sur les utilisateurs ayant interagi avec une étiquette de produit. Par exemple, pour trouver les utilisateurs ayant interagi avec des éléments de catalogue contenant une étiquette de produit spécifique, utilisez cette requête :

{% raw %}
```liquid
-- Description:
-- This query fetches users who have engaged with catalog items that contain a specific product tag. It joins the catalog
-- to custom events by matching any element in an array within events.properties.products (e.g. any product
-- with variant_id equal to a catalog item), using Snowflake LATERAL FLATTEN to explode the array.
SELECT
DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
                items.field_name = 'id'
                    AND
                items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
            )
            OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    and events.app_group_id = '<app_group_id>'
    AND items.catalog_id = '<catalog_id>'
    AND (items.field_name = 'product_tags' AND ARRAY_CONTAINS('<product_tag_value>'::VARIANT, TRY_PARSE_JSON(items.field_value)));
```
{% endraw %}

{% endtab %}
{% tab Métachamps de produit %}

Utilisez les métachamps de produit pour personnaliser les messages avec des détails produit personnalisés au-delà des champs standard de Shopify. Par exemple, incluez des instructions d'entretien dans une confirmation de commande, affichez le pays d'origine dans un e-mail de recommandation, ou segmentez les utilisateurs ayant acheté un matériau spécifique.

Chaque métachamp synchronisé devient une colonne distincte dans votre catalogue, avec un type de données déterminé par le type de métachamp. Pour configurer la synchronisation des métachamps, consultez [Métachamps de produit Shopify](#shopify-product-metafields).

### Sélection de catalogue

1. Dans Shopify, définissez le métachamp de produit `seasonal` sur les produits concernés avec la valeur `summer` (il s'agit d'une valeur de métachamp, pas d'une étiquette de produit).

![Fenêtre modale d'ajout de métachamps de produit, incluant le métachamp seasonal avec la valeur summer.]({% image_buster /assets/img/shopify/summer_product_metafield.png %}){: style="max-width:80%;"}

{: start="2"}
2. Dans Braze, activez la synchronisation des métachamps et sélectionnez `custom.seasonal` (ou l'espace de noms et la clé correspondant à votre métachamp Shopify).

![Fenêtre modale de sélection des métachamps de produit, avec un menu déroulant étendu affichant quatre éléments sélectionnés, dont custom.seasonal.]({% image_buster /assets/img/shopify/select_metafields.png %}){: style="max-width:80%;"}

### Personnalisation

1. Créez une [sélection de catalogue]({{site.baseurl}}/catalog_selections/) qui filtre les métachamps incluant la valeur correspondante.

![Une sélection de catalogue qui filtre les métachamps ayant l'attribut summer.]({% image_buster /assets/img/shopify/metafields_selection.png %})

{: start="2"}
2. Dans le compositeur de messages, ajoutez la sélection à l'endroit où vous souhaitez intégrer les métachamps de produit. Par exemple, vous pourriez utiliser un bloc produit HTML comme celui-ci :

{% raw %}
```liquid
{% catalog_selection_items se-team-ecommerce_shopify_catalog seasonal_summer %}

{% if items[0] == blank %}
{% abort_message('Catalog selection returned no items') %}
{% endif %}

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">
  {% for item in items %}
  {% if forloop.index0 < 3 %}
  {% assign title = item.product_title | default: '' %}
  {% assign image_url = item.variant_image_url | default: '' %}
  {% assign price = item.price | default: '' %}
  {% assign url = item.product_url | default: '' %}

  <tr>
    <td width="200" valign="top" style="padding:12px 12px 12px 0;">
      {% if image_url == blank %}
      <div style="width:200px;height:200px;background:#f2f2f2;line-height:200px;text-align:center;font-family:Arial,sans-serif;font-size:12px;color:#666;">
        No image
      </div>
      {% else %}
        {% if url == blank %}
        <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
        {% else %}
        <a href="{{ url }}" style="text-decoration:none;">
          <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
        </a>
        {% endif %}
      {% endif %}
    </td>

    <td valign="top" style="padding:12px 0;font-family:Arial,sans-serif;font-size:14px;line-height:20px;color:#111;">
      {% if title != blank %}<div style="font-weight:600;">{{ title | escape }}</div>{% endif %}
      {% if price != blank %}<div>Price: ${{ price }}</div>{% endif %}
      {% if url != blank %}<div><a href="{{ url }}" style="color:#F84B09;">View product</a></div>{% endif %}
    </td>
  </tr>
  {% endif %}
  {% endfor %}
</table>
```
{% endraw %}

Ou, si vous souhaitez mentionner des produits spécifiques avec une valeur de métachamp donnée dans une notification push, vous pouvez utiliser l'outil **Ajouter une personnalisation** et spécifier vos éléments de catalogue.

{% raw %}
```liquid
Check out the latest summer products:
    {% catalog_selection_items se-team-ecommerce_shopify_catalog seasonal_summer %}
    {{ items[0].product_title}}{{items[0].price}}
    {{ items[1].product_title}}{{items[1].price}}
    {{ items[2].product_title}}{{items[2].price}}
```
{% endraw %}

![Compositeur de notification push avec une sélection de catalogue intégrant trois éléments à l'aide d'une sélection basée sur les métachamps.]({% image_buster /assets/img/shopify/add_personalization_metafields.png %})

### Segmentation par catalogue (SQL)

Utilisez les [Extensions de segments]({{site.baseurl}}/user_guide/audience/segments/segment_extension/) pour créer des segments basés sur les utilisateurs ayant interagi avec un métachamp de produit. Par exemple, pour trouver les utilisateurs ayant déclenché un événement e-commerce avec un produit dont le tableau de métachamps contient une valeur spécifique, utilisez cette requête :

{% raw %}
```sql
-- -----------------------------------------------------------------------------
-- When the metafield is stored as a JSON array in catalog field_value (for example,
-- '["winter","summer"]' or a list-type Shopify metafield serialized to JSON),
-- use ARRAY_CONTAINS like product_tags. Cast the element you search for to
-- VARIANT so types match the parsed array elements.
-- -----------------------------------------------------------------------------

-- Description:
-- Fetches users who triggered the ecommerce event with a product whose
-- metafield array contains a specific value (for example, segment on "seasonal").
-- For a date range, add events.time >= $start_date AND events.time <= $end_date.
-- For first/last triggered, reuse the CTE pattern from Template 3 with this
-- ARRAY_CONTAINS predicate instead of items.field_value = '<metafield_value>'.
SELECT
    DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
            items.field_name = 'id'
            AND items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
        )
        OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    AND events.app_group_id = '<app_group_id>'
    AND items.catalog_id = '<catalog_id>'
    AND items.field_name = '<metafield_name>'
    AND ARRAY_CONTAINS('<array_element_value>'::VARIANT, TRY_PARSE_JSON(items.field_value));
```
{% endraw %}

Si vous souhaitez segmenter les clients ayant passé une commande avec des métachamps de produit spécifiques, utilisez l'un des modèles SQL d'Extension de segments suivants (toutes les périodes, période spécifique, premier ou dernier déclenchement d'un événement).

{% raw %}
```sql
-- =============================================================================
-- Segment Extension: Metafields × Ecommerce Events — Example SQL Templates
-- =============================================================================
-- Metafield column names in CATALOGS_ITEMS_SHARED follow:
--   field_name = 'metafield_<namespace>_<key>'
-- Replace placeholders: app_group_id, catalog_id, event name, and the metafield
-- field_name + value. For array-type metafield values, use ARRAY_CONTAINS
-- with TRY_PARSE_JSON(items.field_value) similar to the product_tags example.
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Template 1: Map metafields to event triggers (all time)
-- -----------------------------------------------------------------------------
-- Users who have ever triggered the ecommerce event with a product that has
-- the given metafield value. Event-agnostic: change events.name for the
-- desired event (e.g. ecommerce.order_placed, ecommerce.product_viewed).
-- -----------------------------------------------------------------------------

-- Description:
-- Fetches users who have engaged with catalog items that have a specific
-- product metafield. Joins the catalog to custom events by matching
-- events.properties.products (e.g. variant_id) to catalog items.
SELECT
    DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
            items.field_name = 'id'
            AND items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
        )
        OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    AND events.app_group_id = '<app_group_id>'
    AND items.catalog_id = '<catalog_id>'
    AND items.field_name = '<metafield_name>'
    AND items.field_value = '<metafield_value>';


-- -----------------------------------------------------------------------------
-- Template 2: Map metafields to event triggers (for a specific period)
-- -----------------------------------------------------------------------------
-- Same as Template 1, restricted to events within a time window. Use
-- $start_date and $end_date (Segment Extension parameters) or literal
-- Unix timestamps.
-- -----------------------------------------------------------------------------

-- Description:
-- Fetches users who triggered the ecommerce event with a product that has
-- the given metafield value within the specified time range.
SELECT
    DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
            items.field_name = 'id'
            AND items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
        )
        OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    AND events.app_group_id = '<app_group_id>'
    AND events.time >= $start_date
    AND events.time <= $end_date
    AND items.catalog_id = '<catalog_id>'
    AND items.field_name = '<metafield_name>'
    AND items.field_value = '<metafield_value>';


-- -----------------------------------------------------------------------------
-- Template 3: Map metafields — first or last triggered an event
-- -----------------------------------------------------------------------------
-- Users for whom the *first* (earliest) or *last* (most recent) matching
-- event (by time) involved a product with the given metafield. Switch
-- ORDER BY to time ASC for first, time DESC for last.
-- -----------------------------------------------------------------------------

-- Description:
-- Fetches users whose first (or last) occurrence of the ecommerce event
-- involved a catalog item with the specified metafield value.
WITH events_with_catalog_metafield AS (
    SELECT
        events.user_id,
        events.time,
        events.id AS event_id,
        ROW_NUMBER() OVER (
            PARTITION BY events.user_id
            ORDER BY events.time ASC   -- use DESC for "last triggered"
        ) AS rn
    FROM
        USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
        LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
        JOIN CATALOGS_ITEMS_SHARED AS items ON (
            (
                items.field_name = 'id'
                AND items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
            )
            OR
            items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
        )
    WHERE
        events.name = 'ecommerce.order_placed'
        AND events.app_group_id = '<app_group_id>'
        AND items.catalog_id = '<catalog_id>'
        AND items.field_name = '<metafield_name>'
        AND items.field_value = '<metafield_value>'
)
SELECT
    user_id
FROM
    events_with_catalog_metafield
WHERE
    rn = 1;
```
{% endraw %}

{% endtab %}
{% tab Collections %}

Utilisez les collections Shopify pour intégrer des regroupements de produits sélectionnés dans vos messages, qui sont également utilisés sur votre site Shopify et vos expériences sur l'application. Par exemple, mettez en avant les « Nouveautés » dans un e-mail promotionnel, proposez des ventes croisées avec les « Meilleures ventes » dans un Canvas de panier abandonné, ou ciblez les utilisateurs ayant consulté une collection saisonnière.

### Sélection de catalogue

1. Dans Shopify, créez une collection « New Women's Products - In Stock » avec vos produits les plus performants.

![Liste des collections Shopify, incluant « New Women's Products - In Stock ».]({% image_buster /assets/img/shopify/shopify_collections.png %})

{: start="2"}
2. Dans Braze, activez la synchronisation des collections et sélectionnez « Women's Products - In Stock ».

![Fenêtre modale de sélection des collections, avec un menu déroulant étendu sélectionnant quatre collections.]({% image_buster /assets/img/shopify/select_collections_id.png %})

{% alert note %}
Pour les collections Shopify, vous devez utiliser l'**ID de collection**, qui se trouve dans l'URL lorsque vous consultez la collection. Par exemple, une URL `https://admin.shopify.com/store/se-team-ecommerce/collections/470645342446` a l'ID de collection `470645342446`.
{% endalert %}

### Personnalisation

{% alert note %}
Lorsque vous référencez des ID de collection dans les sélections de catalogue, utilisez uniquement la valeur numérique de l'ID sans les crochets `[]` qui apparaissent dans les données du catalogue. Par exemple, si les ID de collection s'affichent sous la forme `[123456789012, 987654321098]` dans votre catalogue, écrivez simplement l'ID numérique (comme `470645342446`) dans votre filtre de sélection.
{% endalert %}

1. Créez une sélection de catalogue nommée « New Women's Products - In Stock » qui filtre les produits possédant l'ID de cette collection. Vous ne pouvez utiliser qu'un seul champ tableau unique au sein d'une même sélection de catalogue, et jusqu'à 50 produits dans votre collection.
 - Vous pouvez également créer vos propres sélections personnalisées en filtrant avec le champ **Collections**.

![Une sélection de catalogue qui filtre les collections ayant l'attribut ID de collection « 470645342446 ».]({% image_buster /assets/img/shopify/collections_selection.png %})

{: start="2"}
2. Dans votre message, intégrez votre collection en utilisant la sélection que vous avez créée ou en référençant directement la collection. Par exemple, vous pourriez utiliser un bloc produit HTML comme celui-ci :

{% raw %}
```liquid
{% catalog_selection_items se-team-ecommerce_shopify_catalog shopify_collection_womens_instock %}

{% if items[0] == blank %}
{% abort_message('Catalog selection returned no items') %}
{% endif %}

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">
  {% for item in items %}
  {% if forloop.index0 < 3 %}
  {% assign title = item.product_title | default: '' %}
  {% assign image_url = item.variant_image_url | default: '' %}
  {% assign price = item.price | default: '' %}
  {% assign url = item.product_url | default: '' %}

  <tr>
    <td width="200" valign="top" style="padding:12px 12px 12px 0;">
      {% if image_url == blank %}
      <div style="width:200px;height:200px;background:#f2f2f2;line-height:200px;text-align:center;font-family:Arial,sans-serif;font-size:12px;color:#666;">
        No image
      </div>
      {% else %}
      {% if url == blank %}
      <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
      {% else %}
      <a href="{{ url }}" style="text-decoration:none;">
        <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
      </a>
      {% endif %}
      {% endif %}
    </td>

    <td valign="top" style="padding:12px 0;font-family:Arial,sans-serif;font-size:14px;line-height:20px;color:#111;">
      {% if title != blank %}<div style="font-weight:600;">{{ title | escape }}</div>{% endif %}
      {% if price != blank %}<div>Price: ${{ price }}</div>{% endif %}
      {% if url != blank %}<div><a href="{{ url }}" style="color:#F84B09;">View product</a></div>{% endif %}
    </td>
  </tr>
  {% endif %}
  {% endfor %}
</table>
```
{% endraw %}

Ou, si vous souhaitez mentionner des nouveaux produits spécifiques dans une notification push, vous pouvez utiliser l'outil **Ajouter une personnalisation** et spécifier vos éléments de catalogue.

{% raw %}
```liquid
Checkout the latest women's clothing:
    {% catalog_selection_items se-team-ecommerce_shopify_catalog shopify_collection_womens_instock %}
    {{ items[0].product_title}}{{items[0].price}}
    {{ items[1].product_title}}{{items[1].price}}
    {{ items[2].product_title}}{{items[2].price}}
```
{% endraw %}

![Compositeur de notification push avec une sélection de catalogue intégrant trois éléments avec une étiquette de produit.]({% image_buster /assets/img/shopify/add_personalization_collections.png %})

### Segmentation par catalogue (SQL)

Créez un segment d'utilisateurs ayant interagi avec une collection. Utilisez les [Extensions de segments]({{site.baseurl}}/user_guide/audience/segments/segment_extension/) pour créer des segments basés sur l'appartenance à une collection. Par exemple, pour trouver les utilisateurs ayant acheté des produits d'une collection spécifique au cours de la dernière année, utilisez cette requête :

{% raw %}
```json
-- Description:
-- This query fetches users who have engaged with catalog items that contain a specific collection ID. It joins the catalog
-- to custom events by matching any element in an array within events.properties.products (e.g. any product
-- with variant_id equal to a catalog item), using Snowflake LATERAL FLATTEN to explode the array.
SELECT
DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
                items.field_name = 'id'
                    AND
                items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
            )
            OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    and events.app_group_id = '<app_group_id>'
    AND items.catalog_id = '<catalog_id>'
    AND (items.field_name = 'collection_ids' AND ARRAY_CONTAINS('<collection_ids_value>'::VARIANT, TRY_PARSE_JSON(items.field_value)));
```
{% endraw %}

{% endtab %}
{% endtabs %}

{% alert tip %}
Vous pouvez également configurer des [notifications de baisse de prix]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/) et des [notifications de retour en stock]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/) !<br><br> Notez que pour chaque cas d'utilisation, vous devez créer un événement personnalisé qui capture le statut d'abonnement d'un utilisateur dans votre catalogue. L'événement personnalisé nécessite une propriété d'événement qui correspond soit au [SKU, soit au Shopify Variant ID]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs/#step-2-select-your-product-identifier) que vous avez sélectionné dans le cadre de la synchronisation de vos produits Shopify.
{% endalert %}

## Désactiver la synchronisation des produits {#deactivate}

La désactivation de la fonctionnalité de synchronisation des produits Shopify supprimera l'intégralité de votre catalogue et de vos produits. Cela peut également avoir un impact sur les messages qui utilisent activement les données produit de ce catalogue. Confirmez que vous avez mis à jour ou mis en pause ces Campaigns ou Canvas avant la désactivation, car cela pourrait entraîner l'envoi de messages sans détails sur les produits. Ne supprimez pas directement le catalogue Shopify sur la page des catalogues.

## Résolution des problèmes {#troubleshooting}

Si la synchronisation de vos produits Shopify rencontre une erreur, cela pourrait être dû aux erreurs suivantes. Suivez les instructions pour corriger le problème et résoudre la synchronisation :

| Erreur | Raison | Solution |
| --- | --- | --- |
| Erreur du serveur | Cela se produit lorsqu'il y a une erreur de serveur du côté de Shopify au moment de la synchronisation de vos produits. | [Désactivez la synchronisation](#deactivate) et resynchronisez l'ensemble de votre inventaire de produits. |
| SKU en double | Cela se produit si vous utilisez un SKU comme ID d'article de catalogue et que plusieurs produits partagent le même SKU. Comme l'ID de l'article du catalogue doit être unique, tous vos produits doivent avoir des SKU uniques. | Vérifiez votre liste complète de produits et de variantes dans Shopify pour vous assurer qu'il n'y a pas de SKU en double. S'il y en a, mettez-les à jour pour qu'ils soient uniques dans votre compte de boutique Shopify. Une fois la correction effectuée, [désactivez la synchronisation](#deactivate) et resynchronisez l'ensemble de votre inventaire de produits. |
| Limite du catalogue dépassée | Cela se produit lorsque vous dépassez votre limite de catalogue. Braze ne pourra pas terminer la synchronisation ou la maintenir active en raison de l'absence d'espace de stockage disponible. | Il existe deux solutions à ce problème :<br><br>1. Contactez votre gestionnaire de compte pour passer à un niveau supérieur afin d'augmenter votre limite de catalogue.<br><br>2. Libérez de l'espace de stockage en supprimant l'un des éléments suivants :<br>- Des articles de catalogue d'autres catalogues<br>- D'autres catalogues<br>- Des sélections créées<br><br> Après avoir utilisé l'une ou l'autre des solutions, la synchronisation doit être désactivée puis relancée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Résolution des problèmes" }