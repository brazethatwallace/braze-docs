---
nav_title: Blocs produit
article_title: Blocs produit en glisser-déposer
page_order: 5
description: "Cet article de référence traite des blocs produit en glisser-déposer, qui permettent aux utilisateurs d'ajouter et de configurer rapidement des vitrines dynamiques ou statiques d'articles de catalogue."
tool:
    - Campaigns
    - Canvas
alias: /dnd_product_blocks/
---

# Blocs produit en glisser-déposer {#drag-and-drop-product-blocks}

> L'éditeur par glisser-déposer vous permet d'ajouter et de configurer rapidement des blocs produit dans vos messages pour une mise en valeur fluide de vos produits, sans avoir besoin de créer du code Liquid personnalisé.

{% alert important %}
La fonctionnalité de bloc produit en glisser-déposer est en accès anticipé et n'est actuellement disponible que pour les e-mails. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l'accès anticipé.
{% endalert %}

## Conditions {#requirements}

| Exigence | Description |
| --- | --- |
| Événements recommandés pour le commerce électronique | Les [événements recommandés pour le commerce électronique]({{site.baseurl}}/ecommerce_events/) fournissent des schémas de données normalisés pour les événements comportementaux clés qui se produisent avant et après la passation d'une commande. Ces événements remplaceront à terme l'ancien événement d'achat de Braze et deviendront la norme pour le suivi des comportements liés au commerce. <br><br> Les événements recommandés pour le commerce électronique sont requis pour les blocs produit dynamiques. |
| Modèles de Canvas pour le commerce électronique | Les événements recommandés pour le commerce électronique prennent en charge des modèles prédéfinis, y compris des modèles de Canvas pour le commerce électronique conçus pour des cas d'utilisation essentiels tels que la navigation abandonnée, les paniers abandonnés et les confirmations de commande. <br><br>Si vous prévoyez d'implémenter l'un de ces cas d'utilisation essentiels du commerce électronique à l'aide des [modèles de Canvas pour le commerce électronique]({{site.baseurl}}/ecommerce_use_cases/), vous devez utiliser ou suivre le modèle de Canvas fourni. |
| Catalogue Braze | Vous devez créer un catalogue Braze qui inclut les champs suivants, que vous utilisez dans la configuration de votre bloc produit :{::nomarkdown}<code><ul><li>product_title</li><li>product_url</li><li>variant_image_url</li></ul></code>{:/} |
| Sélection de catalogue | Pour les blocs produit statiques, vous devez créer une [sélection de catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) pour spécifier quels produits inclure dans votre bloc produit. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements" }

## Types de blocs produit en glisser-déposer {#types-of-drag-and-drop-product-blocks}

| Bloc produit | Objectif | Cas d'utilisation | Disponibilité |
| --- | --- | --- | --- |
| Dynamique | Personnalisez vos messages avec une vitrine de produits basée sur les interactions des clients en utilisant les [événements recommandés pour le commerce électronique]({{site.baseurl}}/ecommerce_events/) et les catalogues au sein de nos [modèles de Canvas pour le commerce électronique]({{site.baseurl}}/ecommerce_use_cases/). | {::nomarkdown}<ul><li>Navigation abandonnée</li><li>Panier abandonné</li><li>Paiement abandonné</li><li>Confirmations de commande</li></ul>{:/} | Disponible uniquement dans Canvas. |
| Statique | Personnalisez les produits en utilisant les données stockées dans un catalogue Braze. Vous devez utiliser une [sélection de catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) pour spécifier quels produits inclure. | Idéal pour mettre en avant les lancements de nouveaux produits ou les offres spécifiques à une catégorie. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Types of drag-and-drop product blocks" }

## Configuration du contenu des blocs produit {#product-block-content-configuration}

Chaque type de bloc a des configurations de contenu différentes.

### Champs produit {#product-fields}

Dans la section **Product Fields**, sélectionnez votre type de bloc produit, puis activez les champs que vous souhaitez inclure pour chaque produit. Chaque champ est extrait de sources différentes en fonction du type de bloc produit que vous sélectionnez.

#### Bloc produit dynamique {#dynamic-product-block}

| Champ produit | Source |
| --- | --- |
| Image de la variante | Catalogues |
| Titre du produit | Catalogues |
| Bouton pour l'URL du produit | Catalogues |
| Prix | Propriété de l'événement recommandé pour le commerce électronique |
| Quantité | Propriété de l'événement recommandé pour le commerce électronique |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dynamic product block" }

![Champs produit pour un bloc produit dynamique, divisés en données de catalogue et données d'événement.]({% image_buster /assets/img/product_blocks/dynamic_fields.png %}){: style="max-width:50%;"}

#### Bloc produit statique {#static-product-block}

| Champ produit | Source |
| --- | --- |
| Image de la variante | Catalogues |
| Titre du produit | Catalogues |
| Bouton pour l'URL du produit | Catalogues |
| Prix | Catalogues |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Static product block" }

![Champs produit pour un bloc produit statique, tous catégorisés comme données de catalogue.]({% image_buster /assets/img/product_blocks/static_fields.png %}){: style="max-width:50%;"}

### Options de disposition {#layout-options}

Utilisez les options de disposition pour personnaliser l'affichage de vos produits au sein de votre bloc produit.

| Option | Description |
| --- | --- |
| Orientation du produit | Choisissez comment l'image et les champs produit au sein du bloc sont orientés. |
| Alignement | Ajustez l'alignement des champs de texte et du bouton au sein du bloc. |
| Nombre maximum de produits par ligne | Affichez jusqu'à trois produits par ligne, jusqu'à 12 produits au total pour les blocs produit statiques et jusqu'à 24 produits au total pour les blocs produit dynamiques. |
| Espacement des produits | Définissez l'espacement entre les produits. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Layout options" }

![Options de disposition pour l'orientation du produit, l'alignement, le nombre maximum de produits par ligne et l'espacement des produits.]({% image_buster /assets/img/product_blocks/layout_options.png %}){: style="max-width:50%;"}

### Paramètres de style globaux des e-mails {#global-email-style-settings}

Les [paramètres de style globaux des e-mails]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings/) vous permettent d'appliquer un style cohérent à vos e-mails dans Braze. Vous pouvez ainsi définir des styles spécifiques — polices, couleurs et designs de boutons — qui s'appliqueront automatiquement à tous vos e-mails.

#### Fonctionnement des paramètres de style globaux avec les blocs produit {#how-global-email-style-settings-work-with-product-blocks}

Les styles existants pour les paragraphes et les boutons s'appliquent automatiquement aux éléments de texte et de bouton au sein du bloc produit. Votre bloc produit utilise donc systématiquement la mise en forme que vous avez définie pour les paragraphes et les boutons, ce qui garantit un aspect cohérent dans l'ensemble de votre e-mail.

## Configuration des blocs produit {#setting-up-product-blocks}

### Configuration du catalogue {#catalog-setup}

{% alert important %}
Si vous utilisez l'intégration Braze et Shopify pour la [synchronisation des produits]({{site.baseurl}}/shopify_catalogs/), aucune étape supplémentaire n'est nécessaire pour utiliser les blocs produit en glisser-déposer.<br><br> Si vous ne disposez pas d'informations sur les variantes de produit, vous devez dupliquer les informations de niveau supérieur du produit dans les champs produit et variante de produit au sein des payloads d'événements et des catalogues. Concrètement, vous devez fournir les mêmes détails de produit pour les deux identifiants afin de maintenir la cohérence nécessaire au bon fonctionnement du bloc produit.
{% endalert %}

Pour utiliser les blocs produit en glisser-déposer, vous devez configurer un catalogue Braze qui inclut des valeurs de champs spécifiques. Ces champs sont utilisés dans la configuration de votre bloc produit. Assurez-vous que votre catalogue inclut les champs suivants :

| Champ | Description |
| --- | --- |
| `product_title` | Le titre du produit. |
| `product_url` | L'URL où les clients peuvent consulter ou acheter le produit. |
| `variant_image_url` | L'URL de l'image de la variante. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Catalog setup" }

Prenez de l'avance en vous appuyant sur cet [exemple de catalogue de produits]({{site.baseurl}}/assets/download_file/ecommerce_product_catalog_sample.csv), qui inclut les champs requis.

![Un exemple de fichier CSV avec les champs requis en plus d'autres champs.]({% image_buster /assets/img/ecommerce/sample_product_catalog.png %})

#### Mappage vers les champs du catalogue {#mapping-to-catalog-fields}

Dans l'onglet **Settings** de votre catalogue, vous pouvez activer le bouton **Product blocks** pour mapper vers des champs et des informations spécifiques de votre catalogue. Cela vous permet de sélectionner les champs à utiliser comme titre du produit, URL du produit et URL de l'image. Notez que les champs du catalogue Shopify sont mappés par défaut et ne peuvent pas être modifiés.

{% alert note %}
Si vous n'utilisez pas Shopify, vous pouvez contacter votre gestionnaire de compte pour activer le mappage de champs, ce qui vous permet de connecter n'importe quel catalogue aux blocs produit et de mapper ses champs vers `product_title`, `product_url` et `variant_image_url`.
{% endalert %}

## Création de blocs produit {#creating-product-blocks}

Ce guide vous accompagne à travers les étapes de création, de test et de vérification du fonctionnement d'un bloc produit dynamique ou statique à l'aide de notre éditeur d'e-mails par glisser-déposer.

### Étape 1 : Créer une campagne e-mail ou une étape e-mail dans un Canvas {#step-1-create-an-email-campaign-or-email-canvas-step}

#### Bloc produit dynamique

{% alert note %}
Les blocs produit dynamiques nécessitent des [événements recommandés pour le commerce électronique]({{site.baseurl}}/ecommerce_events/) et ne peuvent être utilisés que dans des [Canvas]({{site.baseurl}}/ecommerce_use_cases/). Pour les utilisateurs Braze Shopify, ces événements sont automatiquement inclus dans l'intégration. Pour les utilisateurs non-Shopify, vous devez travailler avec vos développeurs pour transmettre ces événements à Braze et vous assurer que l'identifiant produit principal au sein des événements est ajouté comme ID d'article du catalogue.
{% endalert %}

Créez un nouveau Canvas qui utilise l'un des modèles Braze disponibles pour votre cas d'utilisation spécifique :
- Navigation abandonnée
- Panier abandonné
- Paiement abandonné
- Confirmations de commande

Pour des instructions détaillées sur la création de vos Canvas pour le commerce électronique, consultez les [cas d'utilisation du commerce électronique]({{site.baseurl}}/ecommerce_use_cases/).

#### Bloc produit statique

Créez une campagne e-mail par glisser-déposer, un Canvas basé sur une action ou un modèle qui comporte une étape de message e-mail par glisser-déposer.

### Étape 2 : Ajouter un bloc produit {#step-2-add-a-product-block}

{% tabs %}
{% tab Bloc produit dynamique %}

Dans l'étape de message, créez un e-mail ou modifiez le modèle existant à l'aide du compositeur d'e-mails par glisser-déposer.
Faites glisser un bloc produit dans votre message e-mail.
Confirmez que le type de bloc dynamique est sélectionné.
Sélectionnez le catalogue de produits que vous souhaitez utiliser pour la personnalisation. Assurez-vous qu'il correspond aux produits des événements entrants que vous ciblez.

{% endtab %}
{% tab Bloc produit statique %}

Faites glisser un bloc produit dans votre message e-mail et sélectionnez le type de bloc statique.
Sélectionnez le catalogue que vous souhaitez utiliser pour votre bloc produit. Vous devez sélectionner une sélection de catalogue pour spécifier quels produits s'affichent dans votre bloc produit.

{% endtab %}
{% endtabs %}

![L'onglet « Contenu » contenant des blocs éditeur, tels que les blocs produit.]({% image_buster /assets/img/product_blocks/product_block.png %}){: style="max-width:40%;"}

### Étape 3 : Configurer les champs produit {#step-3-configure-product-fields}

Sélectionnez les [champs produit](#product-fields) à afficher dans le bloc produit. Sélectionnez **Apply Settings** après chaque modification pour voir les mises à jour dans l'éditeur.

Vous pouvez également personnaliser le texte avant vos étiquettes Liquid. Par exemple, vous pouvez ajouter un signe dollar ($) devant le prix d'un article ou remplacer le terme « quantité » par « montant » ou un autre libellé de votre choix.

![Bloc produit avec un signe dollar ajouté devant le prix de l'article.]({% image_buster /assets/img/product_blocks/liquid.png %}){: style="max-width:45%;"}

### Étape 4 : Configurer les paramètres de disposition {#step-4-configure-layout-settings}

Modifiez les [options de disposition](#layout-options) pour mettre à jour l'affichage des produits au sein de votre bloc produit, et assurez-vous de sélectionner **Apply Settings** après chaque modification.

### Étape 5 : Prévisualiser et tester votre message {#step-5-preview-and-test-your-message}

{% tabs %}
{% tab Bloc produit dynamique %}

1. Dans la section **Preview & Test**, prévisualisez le message en tant qu'utilisateur personnalisé.
2. Spécifiez le nombre d'articles que vous souhaitez afficher dans la prévisualisation.
3. Confirmez que le nombre correct d'articles apparaît et que vos options de disposition sont appliquées correctement. Notez que les articles qui apparaissent sont sélectionnés aléatoirement.

![Onglet « Preview as a User » avec une section déroulante « Dynamic product block » qui spécifie d'afficher 4 articles.]({% image_buster /assets/img/product_blocks/preview_as_a_user.png %}){: style="max-width:40%;"}

{% endtab %}
{% tab Bloc produit statique %}

Une prévisualisation est générée dans le compositeur par glisser-déposer lorsque vous appliquez des modifications à votre bloc produit.

![Compositeur d'e-mails par glisser-déposer affichant un bloc produit généré avec différentes tuiles d'articles.]({% image_buster /assets/img/product_blocks/static_block_preview.png %})

{% endtab %}
{% endtabs %}

Une fois que vous avez terminé la création de votre message et confirmé qu'il correspond à vos attentes, vous êtes prêt à l'envoyer !