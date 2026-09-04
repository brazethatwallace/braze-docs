---
nav_title: Shopify Markets
article_title: Shopify Markets
description: "Cet article de référence explique comment configurer et utiliser l'intégration Shopify Markets avec Braze."
page_type: partner
search_tag: Partner
permalink: "/shopify_markets/"
hidden: true
---

# Shopify Markets

> Cet article couvre l'intégration Shopify Markets (actuellement en bêta), y compris ce qui est inclus, comment elle fonctionne et comment utiliser vos données de marchés dans vos communications. Braze déploie progressivement des fonctionnalités Markets supplémentaires tout au long de la période bêta, en évoluant pour prendre en charge des structures de marchés plus complexes au fil du temps.

{% alert important %}
Shopify Markets est actuellement en bêta. Pour plus d'informations, contactez votre gestionnaire du succès des clients Braze.
{% endalert %}

## Fonctionnement de l'intégration {#how-the-integration-works}

Shopify Markets étend votre intégration Shopify existante. Connectez votre vitrine par défaut via le chemin d'intégration [standard]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) ou [personnalisé (SDK)]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration), puis sélectionnez les marchés que vous souhaitez que Braze synchronise parmi les marchés configurés de votre boutique. Les intégrations existantes peuvent ajouter des marchés sans perturber les catalogues, les groupes d'abonnement ou les événements. Pour des instructions étape par étape, consultez [Configuration de Shopify Markets](#shopify-markets-setup).

Shopify Markets offre les fonctionnalités suivantes :

- **Profils tenant compte du marché.** L'intégration capture la locale Shopify de chaque utilisateur ainsi que les attributs standard de pays et de langue de Braze, afin que vous puissiez segmenter et déclencher par marché sans configuration personnalisée.
- **Catalogues localisés.** Les données produits spécifiques au marché se synchronisent quotidiennement : prix, devise et disponibilité par marché, ainsi que les titres, descriptions et URL de produits traduits.
- **Personnalisation tenant compte du marché.** Utilisez l'étiquette Liquid {% raw %}`{% shopify_market %}`{% endraw %} pour personnaliser avec les produits du catalogue de chaque marché de l'utilisateur, y compris le contenu traduit de Shopify. Vous pouvez également référencer les détails du marché, comme la devise de présentation, à partir des événements Shopify pris en charge comme `ecommerce.order_placed`.
- **Repli sur la boutique par défaut.** Lorsqu'un utilisateur n'appartient à aucun de vos marchés connectés, Braze utilise les paramètres et produits de votre boutique par défaut, afin que chaque utilisateur reçoive un message complet et précis.

Pour des exemples, consultez [Utiliser les données utilisateur Markets](#use-markets-user-data) et [Cas d'usage de catalogue tenant compte des marchés](#tutorial-show-products-and-prices-per-market).

## Types de marchés Shopify pris en charge {#supported-shopify-market-types}

Durant cette phase de la bêta, vous pouvez sélectionner jusqu'à 25 marchés mono-pays dans Braze, sous réserve des règles suivantes :

- Chaque marché sélectionné doit être un [marché mono-pays](https://help.shopify.com/en/manual/markets/getting-started/market-types#country-or-region-markets) actif. Les marchés B2B et de vente au détail ne sont pas pris en charge.
  - Le paramètre « Utiliser les devises locales » de Shopify n'est pas pris en charge
- Un pays ne peut appartenir qu'à un seul marché sélectionné.
- Les marchés multi-pays ne sont pas pris en charge dans cette phase de la bêta.

Chaque marché sélectionné nécessite un catalogue de marché avec des produits actifs pour que Braze puisse prendre en charge :

- La tarification spécifique au marché sur les produits, en utilisant la devise définie dans le catalogue de marché
- La disponibilité des produits par marché
- Les traductions de produits effectuées via l'application Shopify Translate & Adapt (comme le titre du produit ou le titre de la variante)

![Profil de marché Shopify pour un marché Australie.]({% image_buster /assets/img/shopify/shopify_markets_example.png %})

### Considérations {#considerations}

#### Général {#general}

- **Une seule boutique connectée :** vous ne pouvez connecter qu'une seule boutique Shopify compatible Markets à un espace de travail Braze à la fois.
- **Portée des locales :** les locales récupèrent les titres et descriptions de produits traduits en fonction de ce que vous avez configuré via l'application Shopify Translate & Adapt, ainsi que les URL spécifiques à la locale. Le prix, la devise et les autres champs de catalogue partagés restent identiques entre les locales au sein d'un marché. Par défaut, Braze utilise la [langue par défaut](https://help.shopify.com/en/manual/markets/languages) de chaque marché, la locale principale que Shopify attribue à ce marché. Si la prise en charge étendue des locales est activée pour votre compte, Braze synchronise les locales supplémentaires configurées pour ce marché.

#### Catalogue de marché {#market-catalog}

- **Nouvelles vues de marché dans votre catalogue Shopify d'origine :** Markets ne crée pas de catalogues séparés. Au lieu de cela, ils sont affichés dans votre catalogue Shopify d'origine. Les données Markets sont ajoutées sous forme de nouvelles lignes de catalogue à votre catalogue Shopify.
- **Sélections de catalogue :** jusqu'à 30 sélections de catalogue.
- **Fréquence d'actualisation :** les données produits du catalogue de marché s'actualisent une fois par jour.
- **Catalogues de marché avec tarification uniquement :** un catalogue de marché avec tarification uniquement définit des prix spécifiques au marché sans publier les produits sur un canal de vente. L'inventaire et la disponibilité des produits se synchronisent depuis votre catalogue de boutique par défaut, tandis que le prix reflète la liste de prix du catalogue de marché ou la tarification contextuelle.

### Fonctionnalités non prises en charge {#unsupported-features}

Les éléments suivants ne sont pas pris en charge dans cette bêta :

- Déclencheurs de baisse de prix et de retour en stock pour les catalogues de marché
- Double abonnement e-mail et SMS pour les groupes d'abonnement configurés par marché
- Groupes de marchés imbriqués ou workflows de groupes de pays au-delà du modèle actuel de sélection mono-pays et multi-pays
- Sélection de plus de 25 marchés
- Export de catalogue pour les catalogues compatibles Markets
- Parité complète avec la conversion en devise locale de Shopify, les règles d'arrondi et le comportement de prix le plus bas multi-catalogue lors de la navigation et du paiement

## Configuration de Shopify Markets {#shopify-markets-setup}

### Étape 1 : Connecter votre boutique Shopify compatible Markets {#step-1-connect-your-shopify-markets-enabled-store}

1. Connectez votre boutique en utilisant soit l'[intégration standard Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) soit l'[intégration personnalisée Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration). Une fois votre boutique connectée, configurez Shopify Markets dans le compositeur de configuration.
2. Complétez le flux OAuth et confirmez que Braze demande les portées Markets dans l'OAuth :
   - `read_markets`
   - `read_publications`
   - `read_locales`
3. Une fois l'autorisation réussie et le compositeur de configuration ouvert, sélectionnez **Begin Setup**.
4. Activez les SDK Braze.

### Étape 2 : Sélectionner votre marché et vos paramètres de données {#step-2-select-your-market-and-data-settings}

1. Dans **Track Shopify Data**, sélectionnez **Sync Shopify Markets data**.
2. Sélectionnez **Select Markets** pour choisir votre marché, et assurez-vous d'avoir choisi de suivre les événements comportementaux et les attributs utilisateur.
   - (Facultatif) Activez le remplissage historique

#### Données utilisateur Markets {#markets-user-data}

Pour prendre en charge Shopify Markets, Braze synchronise plus de données que les [événements et attributs standard]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#tracked-shopify-events) de l'intégration.

Braze écrit ce contexte de marché supplémentaire sur chaque profil utilisateur :

| Type de donnée | Valeur | Source de données |
| --- | --- | --- |
| Attribut personnalisé | `shopify_locale` | Shopify |
| Attribut standard | langue du navigateur | SDK Braze |
| Attribut standard | pays | SDK Braze |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Type de donnée du profil utilisateur"}

Braze collecte également les propriétés d'événement de commande supplémentaires suivantes pour prendre en charge le contexte des marchés :

| Type de donnée | Événements impactés | Nouvelles propriétés ajoutées |
| --- | --- | --- |
| Événements eCommerce recommandés | `ecommerce.order_placed`<br>`ecommerce.order_cancelled`<br>`ecommerce.order_refunded` | `country`, `presentment_currency`, `market_handle` |
| Événements personnalisés | `shopify_paid_order`<br>`shopify_fulfilled_order`<br>`shopify_partially_fulfilled_order` | `country`, `presentment_currency`, `market_handle` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Type de donnée d'événement de commande"}

Chaque propriété est dérivée des sources suivantes :

| Propriété | Source de données |
| --- | --- |
| `country` | `default_address` du client Shopify ; si indisponible, Braze utilise `shipping_address` |
| `presentment_currency` | Valeur monétaire de présentation Shopify |
| `market_handle` | Marché Shopify configuré pour le pays de la commande ; défini uniquement lorsque les marchés sont configurés et que le pays correspond |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sources de données des propriétés d'événement de commande"}

### Étape 3 : Gérer les utilisateurs {#step-3-manage-users}

1. Sélectionnez votre type d'`external_id` dans le menu déroulant.
2. Activez les abonnements e-mail et SMS depuis Shopify, ce qui permet à Braze de synchroniser les états d'abonnement e-mail et SMS depuis Shopify. Vous avez deux options :
  - **Utiliser l'intégration :** Braze synchronise les états e-mail et SMS. Vous n'avez qu'à choisir les groupes d'abonnement vers lesquels ils se synchronisent.
  - **Créer la vôtre :** pour un contrôle plus fin de la gestion des états, vous pouvez créer une intégration personnalisée en utilisant les endpoints de groupes d'abonnement Braze.
3. Créez des groupes d'abonnement par défaut pour chaque pays associé à vos marchés synchronisés lors de la configuration.
  - **Nouvelle intégration Shopify :** attribuez un groupe d'abonnement e-mail et SMS par défaut par pays.
  - **Intégration Shopify existante :** le groupe par défaut actuel de votre boutique cesse de se synchroniser. Attribuez de nouveaux groupes e-mail et SMS par défaut par pays. Votre ancienne configuration ne se transfère pas automatiquement.

#### Fonctionnement des abonnements et désabonnements {#how-opt-ins-and-unsubscribes-work}

Lors de la configuration, vous configurez des groupes d'abonnement e-mail et SMS par défaut pour chaque pays associé à vos marchés synchronisés (jusqu'à 25 pays). Cela est requis avant de pouvoir enregistrer la configuration de votre pays. Vous pouvez également attribuer des groupes d'abonnement supplémentaires par pays si vous souhaitez diriger le consentement vers plus d'une liste.

##### Le consentement s'applique à tous les pays configurés {#consent-applies-to-all-configured-countries}

Lorsque l'état de consentement d'un utilisateur change dans Shopify, Braze applique ce changement à tous les groupes d'abonnement par défaut de chaque pays liés à votre boutique connectée, pas seulement au pays spécifique de l'utilisateur :
  - Si un utilisateur devient abonné dans Shopify, il est abonné au groupe d'abonnement e-mail ou SMS par défaut de chaque pays que vous avez configuré.
  - Si un utilisateur se désabonne dans Shopify, il est désabonné du groupe d'abonnement e-mail ou SMS par défaut de chaque pays que vous avez configuré.

{% alert important %}
Le consentement Shopify est par boutique, pas par pays. Dans Shopify, le consentement est suivi une fois pour l'e-mail et une fois pour le SMS par enregistrement client, et ne s'abonne ni ne se désabonne par pays ou par type de liste. Pour cette raison, Braze ne peut pas appliquer les changements de consentement à un seul pays ou un seul groupe d'abonnement. Un événement d'abonnement ou de désabonnement dans Shopify s'applique toujours à tous les groupes d'abonnement par défaut de vos pays configurés en même temps. <br><br> Au sein de Braze, cependant, vous pouvez avoir un contrôle plus granulaire des abonnements et désabonnements au niveau des groupes d'abonnement à mesure que les utilisateurs interagissent avec les canaux de communication.
{% endalert %}

### Étape 4 : Synchroniser les produits {#step-4-sync-products}

1. Pour synchroniser les produits au sein de votre marché, sélectionnez **Sync Shopify products and variants to Braze**.
2. Attribuez l'**ID de catalogue** Braze et configurez tout paramètre supplémentaire.

Votre catalogue inclut une vue par marché pour les produits par défaut de votre boutique. Pour chaque produit publié sur votre marché, Braze ajoute une ligne de marché à votre catalogue existant, en plus des [champs de catalogue Shopify standard]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs#supported-shopify-catalog-data) déjà pris en charge. La synchronisation peut prendre quelques minutes si vous activez Shopify Markets sur une intégration existante.

Sur les lignes de marché, ces champs ont des valeurs spécifiques au marché :

| Champ | Description |
| --- | --- |
| {% raw %}`market_handle`{% endraw %} | Identifie le marché pour la ligne. Les lignes du marché par défaut utilisent `default` ; les marchés supplémentaires utilisent leur identifiant (par exemple, `au`). |
| {% raw %}`locale`{% endraw %} | Lorsque la prise en charge étendue des locales est activée, identifie la locale pour la ligne (par exemple, `fr`). |
| {% raw %}`price`{% endraw %} | Prix spécifique au marché issu de la tarification contextuelle du marché. |
| {% raw %}`compare_at_price`{% endraw %} | Prix comparatif spécifique au marché, ou `0` lorsque Shopify n'a pas de prix comparatif pour ce marché. |
| {% raw %}`product_title`{% endraw %} | Titre du produit traduit lorsqu'une traduction Shopify existe pour la locale de la ligne. |
| {% raw %}`variant_title`{% endraw %} | Titre de la variante traduit lorsqu'une traduction Shopify existe pour la locale de la ligne. |
| {% raw %}`product_url`{% endraw %} | URL de la vitrine pour le marché et la locale lorsque les URL localisées sont activées ; sinon, il s'agit de l'URL produit `myshopify.com` par défaut. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Champs de catalogue des lignes de marché"}

Les lignes de marché utilisent un `id` composite préfixé par l'identifiant du marché, comme `<market>_<variant_id>`. Lorsque la prise en charge étendue des locales est activée, l'ID inclut également la locale (par exemple, `<market>_<locale>_<variant_id>`). Vos produits par défaut conservent leurs ID d'origine.

### Étape 5 : Activer les canaux {#step-5-activate-channels}

1. (Facultatif) Choisissez d'activer ou non la **messagerie dans le navigateur**.
2. Sélectionnez **Finish Setup**.

## Utiliser les données utilisateur Markets {#use-markets-user-data}

Une fois ces attributs et propriétés présents sur les profils utilisateur, vous pouvez les utiliser pour cibler les utilisateurs par marché et personnaliser les messages.

### Cibler par marché dans la segmentation {#target-by-market-in-segmentation}

Filtrez par pays, langue du navigateur ou `shopify_locale` dans les Segments et dans les critères d'entrée de Campaign ou Canvas. Par exemple, créez une audience d'utilisateurs dans un marché spécifique, ou divisez un Canvas par locale.

### Personnaliser et déclencher avec Liquid {#personalize-and-trigger-with-liquid}

Référencez les données directement dans vos messages.

| Donnée utilisateur à référencer | Liquid à utiliser |
| --- | --- |
| La locale de l'utilisateur | {% raw %}`{{custom_attribute.${shopify_locale}}}`{% endraw %} |
| Le pays de l'utilisateur | {% raw %}`{{${country}}}`{% endraw %} |
| Le pays d'une commande (dans un message déclenché) | {% raw %}`{{event_properties.${country}}}`{% endraw %} |
| Le marché d'une commande (dans un message déclenché) | {% raw %}`{{event_properties.${market_handle}}}`{% endraw %} |
| La devise d'une commande (dans un message déclenché) | {% raw %}`{{event_properties.${presentment_currency}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Données utilisateur à référencer avec Liquid"}

### Déclencher des messages à partir de l'activité de commande {#trigger-messages-from-order-activity}

Les nouvelles propriétés de commande accompagnent chaque événement de commande, ce qui vous permet de déclencher un message à partir d'une commande et de personnaliser son contenu en utilisant des détails tenant compte du marché.

Une version simple dans le corps du message pourrait ressembler à :

{% raw %}
```liquid
Thanks for your order! Your total: {{event_properties.${presentment_currency}}} {{event_properties.${total_value}}}
```
{% endraw %}

Comme les propriétés sont sur l'événement lui-même, le message reste fidèle au marché de chaque utilisateur sans configuration supplémentaire.

## Tutoriel : Afficher les produits et les prix par marché {#tutorial-show-products-and-prices-per-market}

Utilisez un catalogue tenant compte des marchés pour créer un seul message qui affiche à chaque utilisateur les produits et les prix de son propre marché.

1. Créez une sélection qui utilise les données de marchés.
2. Référencez la sélection dans un message avec Liquid.

Vous pouvez utiliser un marché fixe lorsqu'un message cible un marché spécifique.

### Étape 1 : Créer une sélection en utilisant les données de marchés {#step-1-create-a-selection-using-markets-data}

Les [sélections]({{site.baseurl}}/catalog_selections) sont des ensembles de produits organisés que vous référencez dans les messages. Pour les catalogues Shopify avec des marchés synchronisés, la section **Filter settings** inclut une zone **Market scope** qui limite les données produits à un marché ou les personnalise par utilisateur.

1. Accédez à votre catalogue Shopify et ouvrez l'onglet **Selections**.
2. Sélectionnez **Create Selection**, puis nommez la sélection, ajoutez une description facultative et définissez une limite de résultats.
3. Dans **Filter settings**, sous **Market scope**, utilisez le menu déroulant **Market** pour choisir comment la sélection résout les produits spécifiques au marché :
   - **Personalized :** chaque destinataire voit les produits et les prix du marché correspondant à l'attribut `country` de son profil.
   - **A synced market :** sélectionnez un marché par nom pour fixer la sélection sur les produits et les prix de ce marché. Utilisez cette option lorsqu'un message cible un seul marché.
4. Terminez tout critère de filtre supplémentaire, puis enregistrez la sélection.
5. Dans **Preview for user**, sélectionnez un utilisateur pour voir ce que la sélection renvoie pour ce profil. Les sélections qui utilisent **Personalized** ne peuvent être prévisualisées qu'après avoir sélectionné un utilisateur.

| Cible | Filtre |
| --- | --- |
| Un marché spécifique | `market_handle` = `au` |
| Produits par défaut uniquement | `market_handle` = `default` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cibles et filtres associés"}

{% alert note %}
Si vous ne spécifiez pas de marché, Braze utilise vos produits par défaut.
{% endalert %}

### Étape 2 : Ajouter des sélections de catalogue tenant compte des marchés aux messages {#step-2-add-market-aware-catalog-selections-to-messages}

Pour servir à chaque utilisateur les produits de son propre marché dans un seul message, créez une sélection avec ce filtre :

| Nom de la sélection | Champ | Opérateur | Valeur |
| --- | --- | --- | --- |
| `market_products` | `market_handle` | equals | {% raw %}`{{shopify_market.handle}}`{% endraw %} |
| `default_products` | `market_handle` | equals | `default` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Nom de la sélection et filtres associés"}

Au moment de l'envoi, Braze remplace {% raw %}`{{shopify_market.handle}}`{% endraw %} par le marché de chaque utilisateur, de sorte que `market_products` donne à chacun les bons produits. `default_products` est le repli pour les utilisateurs sans marché correspondant.

Référencez votre sélection dans votre message avec l'étiquette {% raw %}`{% shopify_market %}`{% endraw %} :

{% raw %}
```liquid
{% shopify_market %}
{% if shopify_market.handle %}
  {% catalog_selection_items <your_catalog_name> <your_market-catalog_selection_name> %}
  {% for item in items %}
    {{ item.product_title }} — {{ item.price }}
  {% endfor %}
{% else %}
  {% catalog_selection_items <your_catalog_name> <your_default-catalog_selection_name> %}
  {% for item in items %}
    {{ item.product_title }} — {{ item.price }}
  {% endfor %}
{% endif %}
```
{% endraw %}

- Placez {% raw %}`{% shopify_market %}`{% endraw %} avant {% raw %}`{% catalog_selection_items %}`{% endraw %} afin que le marché de l'utilisateur soit défini avant l'exécution de la sélection.
- Remplacez `<your_catalog_name>` par votre catalogue, et utilisez vos propres noms de sélection s'ils diffèrent.
- La vérification {% raw %}`{{shopify_market.handle}}`{% endraw %} dirige les utilisateurs sans marché correspondant vers `default_products`, afin qu'ils reçoivent quand même des produits au lieu d'un message vide.

Prévisualisez en tant qu'utilisateur de votre marché pour confirmer que le message affiche les produits, les prix et les titres traduits de ce marché.