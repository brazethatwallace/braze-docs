---
nav_title: Recommandations générées par l'IA
article_title: Créer des recommandations d'articles basées sur l'intelligence artificielle
description: "Cet article de référence explique comment créer une recommandation d'article par intelligence artificielle pour les articles d'un catalogue."
page_order: 1
---

# Créer des recommandations d'articles basées sur l'intelligence artificielle {#create-ai-item-recommendations}

> Découvrez comment créer un moteur de recommandation par intelligence artificielle à partir des articles de votre catalogue.

## À propos des recommandations d'articles par l'IA {#about-ai-item-recommendations}

Utilisez les recommandations d'articles par l'IA pour calculer les produits les plus populaires ou créer des recommandations personnalisées par l'IA pour un [catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs) spécifique. Après avoir créé votre recommandation, vous pouvez utiliser la personnalisation pour insérer ces produits dans vos messages.

{% alert tip %}
Les [recommandations personnalisées par l'IA](#recommendation-types) fonctionnent au mieux avec au moins quelques centaines d'articles de catalogue, au maximum 100 000 articles de catalogue, et généralement au moins 30 000 utilisateurs disposant de données d'achat ou d'interaction. Il ne s'agit que d'un guide approximatif et les résultats peuvent varier. Les autres types de recommandation peuvent fonctionner avec moins de données, y compris lorsque **Plus populaire** est utilisé comme solution de repli.
{% endalert %}

{% multi_lang_include brazeai/recommendations/ai.md section="Plan-specific features" %}

## Créer une recommandation d'articles par IA {#creating-an-ai-item-recommendation}

### Prérequis {#prerequisites}

Avant de commencer, vous devez disposer des éléments suivants :

- Au moins un [catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs) pour utiliser l'un des [types de recommandation]({{site.baseurl}}/user_guide/brazeai/item_recommendations).
- Des données d'achat ou d'événement sur Braze (événements personnalisés, événement de commande passée ou objet d'achat) qui incluent une référence à l'article et doivent correspondre aux ID d'articles du catalogue.

### Étape 1 : Créer une nouvelle recommandation {#step-1-create-a-new-recommendation}

Vous pouvez créer une recommandation d'articles par IA depuis deux endroits dans le tableau de bord :

{% tabs local %}
{% tab Depuis le menu de navigation %}
1. Accédez à **Analytics** > **AI Item Recommendation**.
2. Sélectionnez **Create Prediction** > **AI Item Recommendation**.
{% endtab %}

{% tab Depuis un catalogue %}
Vous pouvez également choisir de créer une recommandation directement depuis un catalogue individuel. Sélectionnez votre catalogue depuis la page **Catalogs**, puis sélectionnez **Create Recommendation**.
{% endtab %}
{% endtabs %}

### Étape 2 : Ajouter les détails de la recommandation {#step-2-add-recommendation-details}

Donnez un nom et une description facultative à votre recommandation.

![Étape « Détails de la recommandation » avec les champs de nom et de description.]({% image_buster /assets/img/item_recs_1.png %})

### Étape 3 : Définir votre recommandation {#recommendation-type}

Sélectionnez un type de recommandation. Chaque type utilise les six derniers mois de données d'interaction avec les articles, telles que les données d'achat, de commande passée ou d'événement personnalisé. Pour des informations plus détaillées et des cas d'usage pour chaque type, consultez [Types et cas d'usage]({{site.baseurl}}/user_guide/brazeai/item_recommendations).

{% alert tip %}
Lorsque vous utilisez **Plus récent** ou **Personnalisé par l'IA**, les utilisateurs ne disposant pas de suffisamment de données pour créer des recommandations individualisées reçoivent les articles **Plus populaire** en solution de repli. La solution de repli **Plus populaire** ne renvoie que les articles existant dans le catalogue lié.<br><br>Pour les recommandations **Personnalisé par l'IA**, consultez le **Taux de personnalisation** sur la page **Analytics** pour voir quel pourcentage d'utilisateurs ayant effectué l'événement configuré au cours des 24 derniers mois disposent de recommandations personnalisées stockées sur leur profil. Pour les recommandations **Plus récent**, la page **Analytics** affiche la part d'utilisateurs recevant des recommandations **Plus récent** par rapport à la solution de repli **Plus populaire**.
{% endalert %}

#### Étape 3.1 : Exclure les achats ou interactions précédents (facultatif) {#step-31-exclude-prior-purchases-or-interactions-optional}

Pour éviter de suggérer des articles qu'un utilisateur a déjà achetés ou avec lesquels il a déjà interagi, sélectionnez **Do not recommend items users have previously interacted with**. Cette option n'est disponible que lorsque le **Type** de recommandation est défini sur **AI Personalized**.

![Étape « Définir votre recommandation » avec « Personnalisé par l'IA » comme type et l'option « Ne pas recommander les articles avec lesquels les utilisateurs ont déjà interagi » sélectionnée.]({% image_buster /assets/img/item_recs_2-3.png %})

Ce paramètre empêche les messages de réutiliser les articles qu'un utilisateur a déjà achetés ou avec lesquels il a interagi, à condition que la recommandation ait été mise à jour récemment. Les articles achetés ou avec lesquels l'utilisateur a interagi entre les mises à jour de recommandation peuvent toujours apparaître. Pour la version gratuite des recommandations d'articles, les mises à jour ont lieu chaque semaine. Pour la version pro des recommandations d'articles par IA, les mises à jour ont lieu toutes les 24 heures.

Par exemple, lorsque vous utilisez la version pro des recommandations d'articles par IA, si un utilisateur achète quelque chose puis reçoit un e-mail marketing dans les 30 minutes, l'article qu'il vient d'acheter pourrait ne pas être exclu de l'e-mail à temps. Cependant, tout message envoyé après 24 heures n'inclura pas cet article.

#### Étape 3.2 : Sélectionner un catalogue {#step-32-select-a-catalog}

S'il n'est pas déjà renseigné, sélectionnez le [catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs) à partir duquel cette recommandation extraira les articles.

#### Étape 3.3 : Ajouter une sélection (facultatif) {#step-33-add-a-selection-optional}

Si vous souhaitez un contrôle plus précis sur votre recommandation, choisissez une [sélection]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) pour appliquer des filtres personnalisés. Les sélections filtrent les recommandations par colonnes spécifiques de votre catalogue, telles que la marque, la taille ou l'emplacement. Les sélections contenant du Liquid ne peuvent pas être utilisées dans votre recommandation.

![Un exemple de la sélection « en stock » sélectionnée pour la recommandation.]({% image_buster /assets/img/item_recs_2-2.png %})

{% alert tip %}
Si vous ne trouvez pas votre sélection, assurez-vous qu'elle est d'abord configurée dans votre catalogue.
{% endalert %}

### Étape 4 : Sélectionner l'interaction pour piloter les recommandations {#step-4-select-the-interaction-to-drive-recommendations}

Sélectionnez l'événement pour lequel vous souhaitez que cette recommandation soit optimisée. Cet événement est généralement un achat, mais il peut également s'agir de toute interaction avec un article.

{% alert tip %}
Lors de la configuration des recommandations d'articles par IA, votre choix d'événement est important. Votre événement déclencheur détermine qui reçoit une recommandation générée par l'IA — les recommandations d'articles par IA sont générées pour les utilisateurs ayant effectué l'événement que vous configurez, ce choix détermine donc directement qui reçoit des recommandations. Sélectionnez un événement qui couvre l'intégralité du Segment d'audience que vous souhaitez atteindre.<br><br>En même temps, trouvez un équilibre entre couverture et pertinence. Les événements en haut de l'entonnoir (comme Produit consulté) tendent à capturer une audience plus large mais sont moins liés aux résultats commerciaux, tandis que les événements en bas de l'entonnoir (comme Acheté) tendent à produire des recommandations plus ciblées et pertinentes pour l'activité. Le meilleur événement est celui qui équilibre la couverture avec l'influence sur les résultats.
{% endalert %}

Vous pouvez optimiser pour :

- Les événements d'achat avec l'[objet d'achat]({{site.baseurl}}/api/objects_filters/purchase_object)
- Les événements personnalisés représentant un achat
- Les événements personnalisés représentant toute autre interaction avec un article (comme les consultations de produits, les clics ou les lectures de médias)
- Les commandes passées avec l'[événement de commande passée]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events?tab=ecommerce.order_placed)

Si vous choisissez **Custom Event**, sélectionnez votre événement dans la liste.

![L'événement personnalisé « purchase » sélectionné comme méthode de suivi actuelle des événements.]({% image_buster /assets/img/item_recs_3.png %})

{% alert note %}
Les événements personnalisés doivent disposer de suffisamment de données avant d'apparaître dans la liste des événements. Si votre événement personnalisé n'apparaît pas, c'est peut-être parce que le backend de Braze ne l'a pas encore traité ou qu'il ne dispose pas de suffisamment de données pour l'entraînement du modèle. Les recommandations par IA s'appuient sur des données historiques pour générer des informations, de sorte que les événements nouvellement créés ou rarement déclenchés ne seront pas disponibles tant que davantage de données n'auront pas été collectées.
{% endalert %}

### Étape 5 : Choisir le nom de propriété correspondant {#property-name}

Pour créer une recommandation, vous devez indiquer à Braze quel champ de votre événement d'interaction (événement de commande passée, objet d'achat ou événement personnalisé) contient l'identifiant unique correspondant au champ `id` d'un article dans le catalogue. Vous n'êtes pas sûr ? [Consultez les exigences](#requirements).

Sélectionnez ce champ pour le **Property Name**.

Le champ **Property Name** est pré-rempli avec une liste de champs envoyés via le SDK à Braze. Si suffisamment de données sont fournies, ces propriétés sont également classées par ordre de probabilité d'être la propriété correcte. Sélectionnez celle qui correspond au champ `id` du catalogue.

![Le nom de propriété « purchase_item » sélectionné, correspondant aux ID d'articles dans le catalogue.]({% image_buster /assets/img/item_recs_4.png %})

#### Exigences {#requirements}

Il existe certaines exigences pour la sélection de votre propriété :

- Doit correspondre au champ `id` de votre catalogue sélectionné.
- **Si vous avez sélectionné l'événement de commande passée ou si vous utilisez les [événements eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events) pour entraîner les recommandations d'articles :** Saisissez `products.product_id` pour l'ID du produit.
  - Le champ peut se trouver dans un tableau de produits, ou se terminer par un tableau d'ID. Dans les deux cas, chaque ID de produit sera traité comme un événement séparé et séquentiel avec le même horodatage.
- **Si vous avez sélectionné l'objet d'achat :** Doit être le `product_id` ou un champ de l'objet `properties` de votre événement d'interaction.
- **Si vous avez sélectionné un événement personnalisé :** Doit être un champ de l'objet `properties` de votre événement personnalisé.
- Les champs imbriqués doivent être saisis dans le menu déroulant **Property Name** en notation par points avec le format `event_property.nested_property`. Par exemple, pour sélectionner la propriété imbriquée `district_name` au sein de la propriété d'événement `location`, vous saisiriez `location.district_name`. Pour en savoir plus sur les propriétés imbriquées dans les événements personnalisés, consultez [Objets imbriqués]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).

#### Exemples de mappages {#example-mappings}

Les exemples de mappages suivants font tous deux référence à ce catalogue d'exemple :

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table aria-label="Exemples de mappages" class="tg">
  <caption>Exemples de mappages</caption>
<thead>
  <tr>
    <th class="tg-0pky">id</th>
    <th class="tg-0pky">title</th>
    <th class="tg-0pky">price</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">ADI-BL-7</td>
    <td class="tg-0pky">Adidas Black Size 7</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-RD-8</td>
    <td class="tg-0pky">Adidas Red Size 8</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-WH-9</td>
    <td class="tg-0pky">Adidas White Size 9</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-PP-10</td>
    <td class="tg-0pky">Adidas Purple Size 10</td>
    <td class="tg-0pky">75.00 USD</td>
  </tr>
</tbody>
</table>

{% tabs %}
{% tab Événement personnalisé %}

Supposons que vous souhaitiez utiliser l'événement personnalisé `added_to_cart` afin de recommander des produits similaires avant que le client ne passe à la caisse. L'événement `added_to_cart` possède une propriété d'événement `product_sku`.

La propriété `product_sku` doit alors contenir au moins l'une des valeurs de la colonne `id` du catalogue d'exemple : « ADI-BL-7 », « ADI-RD-8 », « ADI-WH-9 » ou « ADI-PP-10 ». Vous n'avez pas besoin d'événements pour chaque article du catalogue, mais vous en avez besoin de certains pour que le moteur de recommandation dispose de suffisamment de contenu pour fonctionner.

##### Exemple d'objet d'événement personnalisé {#example-custom-event-object}

Cet événement a `"product_sku": "ADI-BL-7"`, qui correspond au premier article du catalogue d'exemple.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "product_sku": "ADI-BL-7"
      }
    }
  ]
}
```

##### Exemple d'objet d'événement personnalisé avec un tableau de produits {#example-custom-event-object-with-an-array-of-products}

Si les propriétés de votre événement contiennent plusieurs produits dans un tableau, chaque ID de produit sera traité comme un événement séparé et séquentiel. Cet événement peut utiliser la propriété `products.sku` pour correspondre aux premier et troisième articles du catalogue d'exemple.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "transaction_id": "2ff3f9a9-8803-4c3a-91da-14adbf93dc99",
        "products": [
          { "sku": "ADI-BL-7" },
          { "sku": "ADI-WH-9" }
        ]
      }
    }
  ]
}
```

##### Exemple d'objet d'événement personnalisé avec un objet imbriqué contenant un tableau d'ID de produits {#example-custom-event-object-with-a-nested-object-containing-a-product-id-array}

Si vos ID de produits sont des valeurs dans un tableau plutôt que des objets, vous pouvez utiliser la même notation et chaque ID de produit sera traité comme un événement séparé et séquentiel. Cela peut être combiné de manière flexible avec des objets imbriqués dans l'événement suivant en configurant la propriété comme `purchase.product_skus` pour correspondre aux premier et troisième articles du catalogue d'exemple.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "transaction_id": "13791e08-7c22-4f6c-8cc6-832c76af3743",
        "purchase": {
          "product_skus": ["ADI-BL-7", "ADI-WH-9"]
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab Objet d'achat %}

Un objet d'achat est transmis via l'API lorsqu'un achat a été effectué.

En termes de mappage, une logique similaire s'applique pour les objets d'achat comme pour les événements personnalisés, sauf que vous pouvez choisir entre utiliser le `product_id` de l'objet d'achat ou un champ de l'objet `properties`.

N'oubliez pas que vous n'avez pas besoin d'événements pour chaque article du catalogue, mais vous en avez besoin de certains pour que le moteur de recommandation dispose de suffisamment de contenu pour fonctionner.

##### Exemple d'objet d'achat mappé à l'ID de produit {#example-purchase-object-mapped-to-product-id}

Cet événement a `"product_id": "ADI-BL-7"`, qui correspond au premier article du catalogue.

```json
{
  "purchases": [
    {
      "external_id": "user1",
      "app_id": "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id": "ADI-BL-7",
      "currency": "USD",
      "price": 100.00,
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "color": "black",
        "checkout_duration": 180,
        "size": "7",
        "brand": "Adidas"
      }
    }
  ]
}
```

##### Exemple d'objet d'achat mappé à un champ de propriétés {#example-purchase-object-mapped-to-a-properties-field}

Cet événement a une propriété `"sku": "ADI-RD-8"`, qui correspond au deuxième article du catalogue.

```json
{
  "purchases": [
    {
      "external_id": "user1",
      "app_id": "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id": "shoes",
      "currency": "USD",
      "price": 100.00,
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "sku": "ADI-RD-8",
        "color": "red",
        "checkout_duration": 180,
        "size": "8",
        "brand": "Adidas"
      }
    }
  ]
}
```

{% endtab %}
{% tab Événement de commande passée %}

##### Exemple d'objet de commande passée mappé à l'ID de produit {#example-order-placed-object-mapped-to-product-id}

```json
{
  "name": "ecommerce.order_placed",
  "properties": {
    "order_id": "order_123",
    "total_value": 200.0,
    "currency": "USD",
    "products": [
      {
        "product_id": "ADI-BL-7",
        "product_name": "Adidas Black Size 7",
        "variant_id": "ADI-BL-7-default",
        "quantity": 1,
        "price": 100.0
      }
    ],
    "source": "storefront"
  }
}
```

{% endtab %}
{% endtabs %}

### Étape 6 : Entraîner la recommandation {#step-6-train-the-recommendation}

Lorsque vous êtes prêt, sélectionnez **Create Recommendation**. Ce processus peut prendre de 10 minutes à 36 heures. Vous recevrez une notification par e-mail lorsque la recommandation aura été entraînée avec succès ou une explication des raisons pour lesquelles la création a pu échouer.

Vous pouvez retrouver la recommandation sur la page **Predictions**, où vous pouvez ensuite la modifier ou l'archiver selon vos besoins. Les recommandations sont automatiquement réentraînées une fois par semaine (version payante) ou par mois (version gratuite).