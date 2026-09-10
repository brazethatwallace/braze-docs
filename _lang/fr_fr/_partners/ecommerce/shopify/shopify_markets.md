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

Shopify Markets étend votre intégration Shopify existante. Connectez votre boutique par défaut via le parcours d'intégration [standard]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) ou [personnalisé (SDK)]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration), puis sélectionnez les marchés que vous souhaitez que Braze synchronise parmi les marchés configurés dans votre boutique. Les intégrations existantes peuvent ajouter des marchés sans perturber les catalogues, les groupes d'abonnement ou les événements. Pour des instructions détaillées, consultez [Configuration de Shopify Markets](#shopify-markets-setup).

Shopify Markets offre les fonctionnalités suivantes :

- **Profils adaptés au marché :** L'intégration capture la locale Shopify de chaque utilisateur ainsi que les attributs standard de pays et de langue de Braze, ce qui vous permet de segmenter et de déclencher des messages par marché sans configuration personnalisée.
- **Catalogues localisés :** Les données produit spécifiques à chaque marché sont synchronisées quotidiennement, y compris les prix et les devises, ainsi que les titres, descriptions et URL de produits traduits.
- **Personnalisation adaptée au marché :** Utilisez l'étiquette Liquid {% raw %}`{% shopify_market %}`{% endraw %} pour personnaliser vos messages avec les produits du catalogue correspondant au marché de chaque utilisateur, y compris le contenu traduit par Shopify. Vous pouvez également référencer des détails de marché, tels que la devise de présentation, à partir d'événements Shopify pris en charge comme `ecommerce.order_placed`.
- **Repli sur la boutique par défaut :** Lorsqu'un utilisateur n'appartient à aucun de vos marchés connectés, Braze utilise les paramètres et les produits de votre boutique par défaut, afin que chaque utilisateur reçoive un message complet et exact.

Pour des exemples, consultez [Utiliser les données utilisateur Markets](#use-markets-user-data) et [Tutoriel : Afficher les produits et les prix par marché](#tutorial-show-products-and-prices-per-market).

## Types de marchés Shopify pris en charge {#supported-shopify-market-types}

Vous pouvez sélectionner jusqu'à 25 [marchés actifs à pays unique ou à plusieurs pays](https://help.shopify.com/en/manual/markets/getting-started/market-types#country-or-region-markets). Chaque pays ne peut appartenir qu'à un seul marché sélectionné.

Les marchés de sous-régions, les marchés de vente au détail, les marchés B2B et les marchés de canaux ne sont pas pris en charge.

### Ce dont chaque marché a besoin {#what-each-market-needs}

Chaque marché sélectionné nécessite un catalogue de marché contenant des produits actifs. Braze lit les informations suivantes à partir de ce catalogue :

| Données | Description |
| --- | --- |
| Prix | Définis dans le catalogue du marché, dans la devise spécifiée pour ce marché. Le paramètre « Use local currencies » de Shopify n'est pas pris en charge. |
| Traductions | Traductions adaptées réalisées via l'application Shopify Translate & Adapt, telles que le titre du produit et le titre de la variante. Braze ne prend actuellement pas en charge les paramètres de langue spécifiques aux marchés. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ce dont chaque marché a besoin" }

![Profil de marché Shopify pour un marché Australie.]({% image_buster /assets/img/shopify/shopify_markets_example.png %})

### Considérations {#considerations}

#### Général {#general}

- **Un seul magasin connecté :** Vous ne pouvez connecter qu'un seul magasin Shopify compatible avec Markets à un espace de travail Braze à la fois.
- **Portée des paramètres régionaux :** Les paramètres régionaux récupèrent les titres et descriptions de produits traduits en fonction de ce que vous avez configuré via l'application Shopify Translate & Adapt, ainsi que les URL spécifiques aux paramètres régionaux. Le prix, la devise et les autres champs partagés du catalogue restent identiques entre les paramètres régionaux au sein d'un marché. Par défaut, Braze utilise la [langue par défaut](https://help.shopify.com/en/manual/markets/languages) de chaque marché, c'est-à-dire le paramètre régional principal que Shopify attribue à ce marché. Si vous activez la prise en charge étendue des paramètres régionaux, Braze synchronise les paramètres régionaux supplémentaires configurés pour ce marché.

#### Catalogue de marché {#market-catalog}

- **Nouvelles vues de marché dans votre catalogue Shopify d'origine :** Markets ne crée pas de catalogues distincts. Au lieu de cela, Braze les affiche dans votre catalogue Shopify d'origine. Les données de marché sont ajoutées sous forme de nouvelles lignes de catalogue à votre catalogue Shopify.
- **Sélections de catalogue :** Jusqu'à 30 sélections de catalogue.
- **Fréquence d'actualisation :** Les données produit du catalogue de marché sont actualisées une fois par jour.
- **Prix de marché et contenu localisé :** Les lignes de marché incluent le prix du marché et le `compare_at_price`, y compris les titres de produits et de variantes localisés ainsi que les URL de produits lorsque les traductions sont configurées via l'application Shopify Translate & Adapt.
- **Quantité en stock :** Les lignes de marché incluent des valeurs de stock agrégées. Braze ne propose actuellement pas la possibilité de différencier le stock entre les emplacements.
- **Baisse de prix :** Prise en charge pour les catalogues de marché. Un changement de prix dans un catalogue de marché se déclenche sur le prix de ce marché plutôt que sur le prix par défaut de votre magasin. Étant donné que les données produit du catalogue de marché sont actualisées une fois par jour, les baisses de prix sont détectées quotidiennement plutôt qu'au moment où le prix change dans Shopify.
- **Retour en stock :** Le [retour en stock]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications) est pris en charge pour les produits de votre catalogue de magasin par défaut. Les lignes de marché ne déclenchent pas de notifications de retour en stock. Le retour en stock examine le stock total disponible pour une variante de produit dans tous les emplacements Shopify, de sorte qu'un ajout de stock dans un emplacement de vente au détail peut déclencher une notification.

## Configuration de Shopify Markets {#shopify-markets-setup}

### Si vous disposez déjà d'une intégration Shopify active {#if-you-already-have-an-active-shopify-integration}

Markets s'ajoute à votre intégration actuelle. Vous n'avez pas besoin de la déconnecter ni de reconstruire votre configuration.

- Vos groupes d'abonnement deviennent vos groupes à l'échelle de la boutique et continuent de recevoir chaque abonnement, y compris les groupes supplémentaires que vous avez attribués.
- Vos abonnés existants restent dans les groupes auxquels ils appartiennent déjà. Si vous ajoutez des groupes par pays ultérieurement, Braze n'y ajoute pas les abonnés existants.
- Votre catalogue continue de se synchroniser. Les lignes de marché sont ajoutées à celui-ci plutôt qu'à un nouveau catalogue, et vos sélections existantes continuent de fonctionner avec vos lignes par défaut.
- Votre boutique par défaut apparaît à côté de vos marchés sélectionnés, vous permettant d'attribuer des groupes d'abonnement et de créer des sélections de catalogue de la même manière.

Si votre boutique est déjà connectée, commencez par l'[Étape 2](#step-2-select-your-market-user-data) pour en savoir plus sur chaque configuration et son fonctionnement.

### Étape 1 : Connecter votre boutique Shopify avec Markets activé {#step-1-connect-your-shopify-markets-enabled-store}

1. Connectez votre boutique en utilisant soit l'[intégration standard Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration), soit l'[intégration personnalisée Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration). Une fois votre boutique connectée, configurez Shopify Markets dans le compositeur de configuration.
2. Complétez le flux OAuth et confirmez que Braze demande les portées markets dans l'OAuth :
   - `read_markets`
   - `read_publications`
   - `read_locales`
3. Une fois l'autorisation réussie et le compositeur de configuration ouvert, sélectionnez **Begin Setup**.
4. Activez les SDK Braze.

### Étape 2 : Sélectionner les données utilisateur de votre marché {#step-2-select-your-market-user-data}

1. Dans **Track Shopify Data**, sélectionnez **Sync Shopify Markets data**.
2. Sélectionnez **Select Markets** pour choisir votre marché, et assurez-vous d'avoir sélectionné le suivi des événements comportementaux et des attributs utilisateur.
   - (Facultatif) Activez le remplissage historique

#### Données utilisateur des marchés {#markets-user-data}

Pour prendre en charge Shopify Markets, Braze synchronise des données supplémentaires au-delà des [événements et attributs standard]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#tracked-shopify-events) de l'intégration.

##### Attributs du profil utilisateur {#user-profile-attributes}

| Attribut | Type de données | Description | Source des données |
| --- | --- | --- | --- |
| `shopify_locale` | Attribut personnalisé | La langue dans laquelle le client navigue sur votre boutique, comme `en` ou `fr-CA`. Elle change lorsqu'il change de langue sur la vitrine. | Locale du client Shopify |
| `browser_language` | Attribut standard | La langue définie dans le navigateur du client. | SDK Braze |
| `country` | Attribut standard | Le pays du client. | SDK Braze |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Attributs du profil utilisateur"}

##### Propriétés d'événement de commande {#order-event-properties}

| Propriété | Description | Source des données |
| --- | --- | --- |
| `country` | Code pays à deux lettres du client. | L'adresse par défaut (`default_address`) du client dans Shopify, ou l'adresse de livraison (`shipping_address`) de la commande si aucune adresse par défaut n'est définie |
| `presentment_currency` | La devise dans laquelle le client a payé, qui peut différer de la devise de votre boutique. | Devise de présentation de la commande Shopify |
| `market_handle` | Identifiant du marché correspondant au pays du client. Vide lorsqu'aucun marché configuré ne correspond. | Braze, à partir de votre configuration de marché |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Propriétés d'événement de commande"}

Ces propriétés sont ajoutées aux :

- Événements eCommerce recommandés : `ecommerce.order_placed`, `ecommerce.order_cancelled`, `ecommerce.order_refunded`
- Événements personnalisés : `shopify_paid_order`, `shopify_fulfilled_order`, `shopify_partially_fulfilled_order`

##### Fonctionnement de ces propriétés d'événement de marché {#how-these-market-event-properties-work}

| Propriété | Fonctionnement |
| --- | --- |
| `market_handle` | `market_handle` est l'identifiant que vous avez donné au marché dans Shopify, comme `france`. Le même identifiant préfixe les ID de lignes de marché dans votre catalogue, comme `france_46714756268231`. Il est vide lorsque vous n'avez pas configuré de marchés, ou lorsque le pays de la commande ne correspond à aucun marché que vous avez configuré, donc vérifiez la présence d'une valeur vide avant de l'utiliser dans Liquid ou un filtre de Segment. |
| `country` | `country` provient de l'adresse par défaut du client et utilise l'adresse de livraison (`shipping_address`) si l'adresse par défaut n'existe pas. Par exemple, un client en France qui envoie une commande au Japon conserve le marché France. |
| Propriétés d'événement | Les propriétés d'événement sont un instantané du moment où l'événement s'est produit et ne changent pas par la suite. Si un client met à jour son adresse par défaut ultérieurement, les nouveaux événements utilisent son nouveau pays tandis que les événements passés conservent le pays avec lequel ils ont été enregistrés. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fonctionnement des propriétés d'événement de marché"}

##### Devise {#currency}

Les événements Shopify de panier, de paiement et de commande pris en charge comportent deux ensembles de valeurs :
- La devise de votre boutique dans les champs de prix et de total existants, inchangés
- L'objet `presentment_currency` contenant les montants que le client a vus et payés

Utilisez `presentment_currency` lorsque vous montrez à un client ce qu'il a payé, comme dans une confirmation de commande ou un message de panier abandonné. Utilisez les valeurs en devise de la boutique lorsque vous comparez le chiffre d'affaires entre les marchés, car elles sont déjà dans une seule devise.

##### Informations produit localisées {#localized-product-information}

Les événements Shopify pris en charge comportent les titres de produit et de variante dans la langue par défaut de votre boutique. Braze ne traduit pas les payloads d'événement.

Les titres traduits, les descriptions et les URL de produit se trouvent dans les lignes de marché de votre catalogue. Pour afficher des informations produit localisées dans un message, recherchez le produit dans votre catalogue en utilisant l'ID du produit ou de la variante provenant de l'événement.

### Étape 3 : Gérer les utilisateurs {#step-3-manage-users}

1. Sélectionnez votre type d'`external_id` dans le menu déroulant.
2. Activez les abonnements e-mail et SMS depuis Shopify, ce qui permet à Braze de synchroniser les états d'abonnement e-mail et SMS depuis Shopify. Vous avez deux options :
   - **Utiliser l'intégration :** Braze synchronise les états e-mail et SMS. Sélectionnez les groupes d'abonnement vers lesquels ils se synchronisent.
   - **Créer votre propre solution :** Pour un contrôle plus fin de la gestion des états, créez une intégration personnalisée en utilisant les endpoints de groupes d'abonnement de Braze.
3. Sélectionnez les groupes d'abonnement vers lesquels le consentement Shopify se synchronise :
   - **Groupes à l'échelle de la boutique (obligatoire) :** Sélectionnez au moins un groupe e-mail et un groupe SMS. Chaque abonnement que Braze reçoit de Shopify y est enregistré.
   - **Groupes par pays (facultatif) :** Attribuez un ou plusieurs groupes à n'importe quel pays dans vos marchés synchronisés. Les abonnements y sont également enregistrés lorsque Braze peut déterminer le pays du client.

#### Fonctionnement des abonnements et des désabonnements {#how-opt-ins-and-opt-outs-work}

Dans Shopify, chaque client a un état de consentement e-mail et un état de consentement SMS. Lorsque les clients s'abonnent, ils s'abonnent à votre marque, pas à un pays ou une liste.

Braze enregistre chaque abonnement dans vos groupes à l'échelle de la boutique. Si vous configurez des groupes par pays et que Braze peut déterminer dans quel pays se trouve le client, l'abonnement est également enregistré dans les groupes de ce pays.

Si vous ne configurez pas de groupes par pays, les abonnements sont enregistrés uniquement dans vos groupes à l'échelle de la boutique, ce qui correspond à la manière dont Shopify gère le consentement aujourd'hui.

#### Comment Braze détermine le pays {#how-braze-determines-country}

| Canal | Détermination du pays |
| ------- | ---------------------------- |
| E-mail   | Utilise d'abord la locale Shopify du client ; si elle n'est pas disponible, utilise l'attribut country de son profil Braze. |
| SMS     | Utilise le pays du numéro de téléphone, tel que déterminé par les modèles de routage par pays E.164. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Détermination du pays par Braze selon le canal"}

Une locale identifie un pays uniquement lorsqu'elle inclut une région, comme `fr-FR`. Une locale `fr` seule ne le permet pas.

Pour le SMS, le pays provient du numéro de téléphone. L'acheteur doit être ajouté à un groupe d'abonnement capable d'envoyer des messages à ce numéro.

#### Ce qui se passe lorsqu'une personne s'abonne {#what-happens-when-someone-opts-in}

| Statut du pays                           | Groupes à l'échelle de la boutique | Groupes par pays                        |
|------------------------------------------|-------------------|---------------------------------------|
| Déterminé et configuré dans vos marchés | Abonné        | Abonné aux groupes de ce pays   |
| Ne peut pas être déterminé                      | Abonné        | Non abonné                        |
| Déterminé, mais non configuré dans vos marchés | Abonné    | Non abonné                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Résultats d'abonnement selon le statut du pays"}

L'appartenance au groupe d'abonnement est basée sur les événements de consentement provenant de Shopify. Si le pays ou la locale d'un acheteur change, son appartenance au groupe ne change pas. Braze la met à jour uniquement lorsque Shopify envoie un nouvel événement de consentement, par exemple si le consentement est recueilli à nouveau auprès de l'acheteur sur Shopify après le changement de pays ou de locale.

{% alert note %}
Les groupes par pays contrôlent le consentement, pas la langue. Un pays peut avoir plus d'une langue. Les clients anglophones et francophones au Canada, `en-CA` et `fr-CA`, appartiennent au même groupe par pays. Utilisez `shopify_locale` dans vos messages pour spécifier la langue.
{% endalert %}

#### Ce qui se passe lorsqu'une personne se désabonne {#what-happens-when-someone-opts-out}

Un désabonnement dans Shopify retire l'utilisateur de chaque groupe d'abonnement attribué à votre intégration Shopify. C'est identique que la personne se soit désabonnée via un site de marché ou via sa page de compte Shopify.

Les groupes d'abonnement de votre espace de travail qui ne sont pas attribués à l'intégration ne sont pas affectés.

#### Abonnements provenant de pays que vous n'avez pas configurés {#opt-ins-from-countries-you-havent-configured}

Si un client s'abonne depuis un pays qui ne fait pas partie de vos marchés configurés, que vous ne l'ayez jamais ajouté ou que vous ayez retiré ce marché, il est abonné à vos groupes à l'échelle de la boutique. Il n'est ajouté à aucun groupe par pays.

Configurer des marchés ne restreint pas les personnes auxquelles vous pouvez envoyer des messages. Si vous ne pouvez pas envoyer de messages vers un pays pour des raisons légales ou réglementaires, excluez ces utilisateurs avec un filtre de Segment ou redirigez-les vers un groupe d'abonnement distinct.

{% alert tip %}
Créez ce Segment comme une liste d'autorisation des pays que vous desservez, pas comme une liste d'exclusion de ceux que vous ne desservez pas. Les utilisateurs dont le pays n'a pas pu être déterminé n'ont aucune valeur de pays, donc une liste d'exclusion ne les détectera pas.
{% endalert %}

Pour le SMS, les autorisations par pays de chaque groupe d'abonnement contrôlent toujours la distribution. Un utilisateur dont le pays n'est pas autorisé sur le groupe ne recevra pas de messages de celui-ci.

#### Les utilisateurs ne sont pas ajoutés aux groupes par pays ultérieurement {#users-arent-added-to-country-groups-later}

Si Braze ne peut pas déterminer le pays d'un client lors de son abonnement, il est ajouté uniquement à vos groupes à l'échelle de la boutique. Si son pays devient connu ultérieurement, il n'est pas automatiquement ajouté aux groupes de ce pays.

Lorsque vous activez Markets dans une boutique déjà intégrée, vos groupes d'abonnement existants deviennent vos groupes à l'échelle de la boutique. Les abonnés existants restent abonnés à ces groupes et ne sont pas automatiquement ajoutés aux nouveaux groupes par pays.

Pour les ajouter vous-même, créez un Segment pour ces utilisateurs et abonnez-les en utilisant une étape [User Update]({{site.baseurl}}/user_update) de Canvas.

#### Comptabiliser les abonnés entre les groupes {#counting-subscribers-across-groups}

Un abonnement peut ajouter un utilisateur à plus d'un groupe d'abonnement, donc additionner les totaux des groupes compte la même personne plusieurs fois. Utilisez un Segment lorsque vous avez besoin d'un décompte d'abonnés uniques.

#### Fonctionnement {#how-it-works}

1. Un client s'abonne au SMS lors du paiement ou via un formulaire.
2. Shopify envoie l'abonnement à Braze.
3. Braze définit l'utilisateur comme en attente et envoie votre SMS de confirmation.
4. Le client répond avec votre mot-clé de confirmation et devient abonné.
5. S'il ne répond pas avant la fin de la fenêtre de confirmation, il reste en attente.

Pour en savoir plus, consultez [Double abonnement]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in).
### Étape 4 : Synchroniser les produits {#step-4-sync-products}

1. Pour synchroniser les produits au sein de votre marché, sélectionnez **Sync Shopify products and variants to Braze**.
2. Attribuez l'ID de catalogue Braze et configurez les paramètres supplémentaires.

Votre catalogue inclut une vue par marché pour les produits par défaut de votre boutique. Pour chaque produit publié sur votre marché, Braze ajoute une ligne de marché à votre catalogue existant, en plus des [champs de catalogue Shopify standard]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs#supported-shopify-catalog-data) déjà pris en charge. La synchronisation peut prendre quelques minutes si vous activez Shopify Markets sur une intégration existante.

Sur les lignes de marché, ces champs ont des valeurs spécifiques au marché :

| Champ | Description |
| --- | --- |
| `id` | Un ID composite préfixé avec l'identifiant du marché, comme `france_46714756268231`. Les lignes par défaut conservent leurs ID d'article originaux. |
| `market_handle` | L'identifiant que vous avez donné au marché dans Shopify, comme `france`. |
| `locale` | La locale du marché, qui détermine la langue du contenu traduit. |
| `price` | Prix spécifique au marché provenant de la tarification contextuelle du marché, après application des ajustements de liste de prix. |
| `compare_at_price` | Prix comparatif spécifique au marché après ajustements. Braze retourne `0` lorsqu'aucun prix comparatif ne se résout pour ce marché, y compris lorsque la liste de prix du marché est configurée pour annuler les prix comparatifs. |
| `product_title` et `variant_title` | Titres traduits, lorsque les traductions sont configurées via l'application Shopify Translate & Adapt. |
| `product_url` | L'URL du produit pour ce marché. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Champs de catalogue des lignes de marché"}

{% alert important %}
`inventory_quantity` n'est pas inclus dans les lignes de marché. Il apparaît uniquement sur les lignes par défaut, où il reflète le stock total disponible pour une variante de produit à travers tous les emplacements Shopify.<br><br>Lorsque vous utilisez `compare_at_price` dans Liquid, vérifiez la valeur « 0 » avant de l'afficher ou de calculer une réduction. Un marché sans prix comparatif affiche un prix de zéro ou une réduction incorrecte.
{% endalert %}

### Étape 5 : Activer les canaux {#step-5-activate-channels}

1. (Facultatif) Sélectionnez si vous souhaitez activer la communication dans le navigateur.
2. Sélectionnez **Finish Setup**.

## Utiliser les données utilisateur de Markets {#use-markets-user-data}

Une fois ces attributs et propriétés présents sur les profils utilisateur, vous pouvez les utiliser pour cibler les utilisateurs par marché et personnaliser les messages.

### Cibler par marché dans la segmentation {#target-by-market-in-segmentation}

Filtrez par pays, langue du navigateur ou `shopify_locale` dans les Segments et dans les critères d'entrée d'une Campaign ou d'un Canvas. Par exemple, constituez une audience d'utilisateurs sur un marché spécifique, ou divisez un Canvas par locale.

### Déclencher et personnaliser avec Liquid {#trigger-and-personalize-with-liquid}

Référencez les données de marché dans vos messages avec ces variables Liquid.

#### Depuis le profil utilisateur {#from-the-user-profile}

| Attribut | Liquid |
| --- | --- |
| La langue du client | {% raw %}`{{custom_attribute.${shopify_locale}}}`{% endraw %} |
| Le pays du client | {% raw %}`{{${country}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variables Liquid du profil utilisateur Markets"}

#### Depuis les événements de commande {#from-order-events}

| Propriété d'événement | Liquid |
| --- | --- |
| Le pays de la commande | {% raw %}`{{event_properties.${country}}}`{% endraw %} |
| Le marché de la commande | {% raw %}`{{event_properties.${market_handle}}}`{% endraw %} |
| La devise dans laquelle le client a payé | {% raw %}`{{event_properties.${metadata}.presentment_currency.code}}`{% endraw %} |
| Le total de la commande dans cette devise | {% raw %}`{{event_properties.${metadata}.presentment_currency.<total_value>}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variables Liquid des événements de commande Markets"}

#### Afficher les prix dans la devise du client {#show-prices-in-the-customers-currency}

Associez toujours un montant à son code de devise. Un montant affiché seul est l'erreur la plus courante dans les communications multi-marchés, car « 129.95 » signifie quelque chose de différent sur chaque marché.

Utilisez le total de la commande pour les messages au niveau de la commande, comme une confirmation, et le prix du produit pour le contenu au niveau du produit, comme un panier ou une recommandation.

{% raw %}
```liquid
Thanks for your order! Your total: {{event_properties.${metadata}.presentment_currency.code}}
{{event_properties.${metadata}.presentment_currency.<total field>}}
```
{% endraw %}

Comme ces propriétés accompagnent l'événement, le message reste exact pour le marché de chaque client sans configuration supplémentaire.

#### Vérifier les valeurs vides {#check-for-empty-values}

Deux valeurs ne seront pas toujours présentes, et toutes deux s'affichent incorrectement lorsqu'elles sont absentes.

`market_handle` est vide lorsque le pays du client ne correspond à aucun marché configuré. Vérifiez avant de créer une branche dessus :

{% raw %}
```liquid
{% if event_properties.${market_handle} != blank %}
  ...
{% endif %}
```
{% endraw %}

`compare_at_price` renvoie `0` lorsqu'aucun prix de comparaison ne se résout pour ce marché. Vérifiez la valeur `0` avant de l'afficher ou de calculer une remise, sinon le client verra un prix barré à zéro.

#### Afficher les informations produit localisées {#show-localized-product-information}

Les noms de produits dans les événements sont dans la langue par défaut de votre boutique. Pour afficher des titres, descriptions ou URL de produits traduits, recherchez le produit dans votre catalogue en utilisant l'ID de produit ou de variante de l'événement. Pour un exemple, consultez le [Tutoriel : afficher les produits et les prix par marché](#tutorial-show-products-and-prices-per-market).

### Déclencher des messages à partir de l'activité de commande {#trigger-messages-from-order-activity}

Les propriétés de marché sont incluses avec les événements Shopify pris en charge, de sorte qu'une Campaign ou un Canvas déclenché par une commande peut les utiliser sans configuration supplémentaire. Ces événements incluent `country`, `presentment_currency` et `market_handle`.

| Type d'événement | Événements |
| --- | --- |
| Événements eCommerce recommandés | `ecommerce.order_placed`, `ecommerce.order_cancelled`, `ecommerce.order_refunded` |
| Événements personnalisés | `shopify_paid_order`, `shopify_fulfilled_order`, `shopify_partially_fulfilled_order` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Événements de commande Shopify Markets avec propriétés de marché"}

`presentment_currency` offre la couverture la plus large par rapport aux autres. Elle est incluse avec les événements de panier, de paiement et de commande pris en charge, de sorte qu'un message de panier abandonné peut afficher le montant vu par le client même si les événements de panier ne contiennent pas `country` ou `market_handle`. Pour plus de détails, consultez [Devise](#currency).

## Rapports Markets {#markets-reporting}

Lorsque Markets est activé, Braze ventile le chiffre d'affaires et les performances des messages par pays.

### Chiffre d'affaires par pays {#revenue-by-country}

Votre rapport de chiffre d'affaires inclut une ventilation par pays en complément de la ventilation par application, à la fois sur la durée de vie et sur une période sélectionnée.

Chaque commande est attribuée à un pays, et la totalité de son chiffre d'affaires est affectée à ce pays. Le pays est d'abord déterminé à partir de la commande, puis du profil de l'acheteur. Les commandes pour lesquelles aucune de ces informations n'est disponible apparaissent sous **Inconnu**.

Le chiffre d'affaires est affiché en USD, comme le reste du rapport de chiffre d'affaires. Pour voir ce qu'un acheteur a réellement payé, utilisez `presentment_currency` sur l'événement de commande.

### Performance par pays {#performance-by-country}

Les analyses de Campaign et de Canvas incluent un tableau **Performance par pays** montrant les résultats d'un message dans chaque pays, ainsi qu'une ligne de total pour chaque pays. La devise et le chiffre d'affaires total sont agrégés à partir du champ `presentment_currency` de la commande.

| Colonne | Ce qu'elle affiche |
| --- | --- |
| Pays | Chaque pays atteint par votre message. |
| Devise | La devise utilisée pour le chiffre d'affaires de ce pays, agrégée à partir du champ presentment_currency. |
| Chiffre d'affaires total | Le chiffre d'affaires attribué à ce pays. |
| Achats | Les achats attribués à ce pays. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Détail des colonnes du tableau de performance par pays"}

## Supprimer un marché {#remove-a-market}

La suppression d'un marché empêche Braze de synchroniser de nouvelles données pour ses pays. Elle ne supprime pas les données que vous possédez déjà.

### Groupes d'abonnement {#subscription-groups}

La suppression d'un marché met à jour votre configuration des marchés. Elle ne supprime pas les groupes d'abonnement de votre espace de travail et ne retire pas les utilisateurs déjà abonnés aux groupes de pays.

#### Ce qui change dans votre configuration {#what-changes-in-your-setup}

- Les pays du marché supprimé n'apparaissent plus dans l'interface des marchés.
- Braze retire les affectations de groupes d'abonnement de ces pays de votre configuration d'intégration.

#### Ce qui reste identique {#what-stays-the-same}

- Les groupes d'abonnement par pays restent dans votre espace de travail et demeurent disponibles pour le ciblage, mais Shopify ne synchronise plus les désinscriptions vers ces groupes. Les utilisateurs qui se désabonnent dans Shopify peuvent toujours apparaître comme abonnés dans ces groupes de pays, sauf si vous mettez à jour leur statut d'abonnement d'une autre manière, par exemple via les [endpoints de groupes d'abonnement]({{site.baseurl}}/api/endpoints/subscription_groups) ou un workflow de désinscription dans Braze.
- Les utilisateurs déjà abonnés aux groupes de pays d'un marché supprimé restent abonnés.

#### Synchronisation future du consentement {#future-consent-sync}

- Les nouveaux abonnements des acheteurs dans les pays supprimés sont synchronisés uniquement vers vos groupes à l'échelle du magasin, de la même manière que les [abonnements provenant de pays que vous n'avez pas configurés](#opt-ins-from-countries-you-havent-configured).
- Braze ne synchronise plus les nouveaux abonnements ni les désinscriptions vers les groupes de pays des pays supprimés.
- Les groupes d'abonnement à l'échelle du magasin continuent de recevoir les mises à jour de consentement.

### Données utilisateur {#user-data}

- Les attributs déjà présents sur le profil d'un utilisateur, y compris `shopify_locale` et `country`, ne changent pas.
- Le `market_handle` dans les nouveaux événements de commande n'est plus disponible.
- Les filtres de Segment par marché Shopify pour les marchés supprimés ne sont plus disponibles.
- Les références Liquid à un marché supprimé ne sont plus disponibles.

### Catalogues {#catalogs}

- Les lignes de marché pour ce marché cessent de s'actualiser et sont retirées de votre catalogue.
- Les sélections de catalogue basées sur ces lignes de marché cessent de renvoyer des produits. Mettez-les à jour ou supprimez-les avant votre prochain envoi.
- Vos lignes par défaut, ainsi que les sélections basées sur celles-ci, ne sont pas affectées.

## Tutoriel : Afficher les produits et les prix par marché {#tutorial-show-products-and-prices-per-market}

Utilisez un catalogue compatible avec les marchés pour créer un seul message qui montre à chaque utilisateur les produits et les prix de son propre marché.

1. Créez une sélection qui utilise les données de marchés.
2. Référencez la sélection dans un message avec Liquid.

Vous pouvez utiliser un marché fixe lorsqu'un message cible un marché spécifique.

### Étape 1 : Créer une sélection à partir des données de marchés {#step-1-create-a-selection-using-markets-data}

Les [sélections]({{site.baseurl}}/catalog_selections) sont des ensembles de produits que vous référencez dans vos messages. Pour les catalogues Shopify avec des marchés synchronisés, la section **Filter settings** inclut une zone **Market scope** qui limite les données produit à un seul marché ou les personnalise par utilisateur.

1. Accédez à votre catalogue Shopify et ouvrez l'onglet **Selections**.
2. Sélectionnez **Create Selection**, puis nommez la sélection, ajoutez une description facultative et définissez une limite de résultats.
3. Dans **Filter settings**, sous **Market scope**, choisissez comment la sélection résout les produits spécifiques au marché dans le menu déroulant **Market** :
   - **Personalized :** Chaque destinataire voit les produits et les prix du marché correspondant à l'attribut `country` de son profil.
   - **A synced market :** Sélectionnez un marché par nom pour associer la sélection aux produits et prix de ce marché. Utilisez cette option lorsqu'un message cible un seul marché.
4. Terminez les éventuels critères de filtre supplémentaires, puis enregistrez la sélection.
5. Dans **Preview for user**, sélectionnez un utilisateur pour voir ce que la sélection renvoie pour ce profil. Les sélections qui utilisent **Personalized** ne peuvent être prévisualisées qu'après avoir sélectionné un utilisateur.

| Cible | Filtre |
| --- | --- |
| Un marché spécifique | `market_handle` = `au` |
| Produits par défaut uniquement | `market_handle` = `default` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cibles et filtres associés"}

{% alert note %}
Si vous ne spécifiez pas de marché, Braze utilise vos produits par défaut.
{% endalert %}

### Étape 2 : Ajouter des sélections de catalogue compatibles avec les marchés aux messages {#step-2-add-market-aware-catalog-selections-to-messages}

Pour servir à chaque utilisateur les produits de son propre marché dans un seul message, créez une sélection avec ce filtre :

| Nom de la sélection | Champ | Opérateur | Valeur |
| --- | --- | --- | --- |
| `market_products` | `market_handle` | equals | {% raw %}`{{shopify_market.handle}}`{% endraw %} |
| `default_products` | `market_handle` | equals | `default` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Nom de la sélection et filtres associés"}

Au moment de l'envoi, Braze remplace {% raw %}`{{shopify_market.handle}}`{% endraw %} par le marché de chaque utilisateur, de sorte que `market_products` fournit à chacun les bons produits. `default_products` sert de solution de repli pour les utilisateurs sans marché correspondant.

Référencez votre sélection dans votre message avec la balise {% raw %}`{% shopify_market %}`{% endraw %} :

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
- Remplacez `<your_catalog_name>` par le nom de votre catalogue, et utilisez vos propres noms de sélection s'ils diffèrent.
- La vérification de {% raw %}`{{shopify_market.handle}}`{% endraw %} redirige les utilisateurs sans marché correspondant vers `default_products`, de sorte qu'ils reçoivent tout de même des produits au lieu d'un message vide.
- Lorsque vous utilisez `compare_at_price` dans Liquid, vérifiez la valeur « 0 » avant de l'afficher ou de calculer une remise. Un marché sans prix comparatif affiche un prix de zéro ou produit une remise incorrecte.

Prévisualisez en tant qu'utilisateur de votre marché pour confirmer que le message affiche les produits, les prix et les titres traduits de ce marché.