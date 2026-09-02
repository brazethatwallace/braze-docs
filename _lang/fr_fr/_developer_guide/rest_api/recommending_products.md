---
nav_title: Recommander des produits aux utilisateurs
article_title: Recommander des produits aux utilisateurs
page_order: 4
page_type: reference
description: "Cet article de référence explique comment utiliser la REST API de Braze, les catalogues et le contenu connecté pour recommander des produits aux utilisateurs sur différents canaux de communication."
---

# Recommander des produits aux utilisateurs {#recommending-products-to-users}

> Utilisez la REST API de Braze avec les [catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs/create) ou le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) pour afficher des recommandations produit personnalisées dans vos messages. Cette approche vous permet de connecter votre propre moteur de recommandation à l'écosystème de messaging de Braze, afin que les utilisateurs non techniques puissent gérer le contenu et les messages associés à chaque recommandation.

Avec cette approche, vous pouvez :

- Stocker des recommandations produit sur les profils utilisateur depuis votre backend à l'aide de la REST API.
- Récupérer les métadonnées produit au moment de l'envoi grâce aux catalogues ou au contenu connecté.
- Afficher des recommandations personnalisées sur n'importe quel canal de communication, y compris l'e-mail, les notifications push, les messages in-app, et bien plus.

## Prérequis {#prerequisites}

Pour suivre ce guide, vous avez besoin des éléments suivants :

| Condition requise | Description |
| --- | --- |
| Clé API REST Braze | Une clé disposant de la permission `users.track` et, si vous gérez les catalogues via l'API, des permissions de catalogues correspondantes. Pour en créer une, accédez à **Paramètres** > **Clés API**. |
| Catalogue Braze | Un catalogue contenant les métadonnées de vos produits (telles que le nom, la catégorie, le prix et l'URL de l'image). Pour en créer un, consultez [Créer un catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/create). |
| Connaissances en Liquid | Une familiarité intermédiaire avec [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) pour la création de modèles avec des variables personnalisées et l'utilisation du contenu connecté. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Étape 1 : Stocker les recommandations sur les profils utilisateur {#step-1-store-recommendations-on-user-profiles}

Pour commencer, stockez les recommandations produit générées par votre moteur de recommandation sur les profils utilisateur Braze sous forme d'attributs personnalisés. Cela vous permet de référencer les produits recommandés de chaque utilisateur au moment de l'envoi du message.

1. Déterminez les données de recommandation à stocker, telles que les ID de produit ou les catégories préférées.
2. Utilisez l'endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) pour écrire la recommandation en tant qu'attribut personnalisé sur le profil utilisateur.

### Exemple de requête {#example-request}

```http
POST YOUR_REST_ENDPOINT/users/track
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Remplacez `YOUR_REST_ENDPOINT` par l'[URL de l'endpoint REST]({{site.baseurl}}/api/basics#endpoints) de votre espace de travail.

```json
{
  "attributes": [
    {
      "external_id": "user123",
      "recommended_product_id": "1001"
    }
  ]
}
```

Utilisez des noms d'attributs significatifs (tels que `recommended_product_id`) afin de pouvoir les référencer facilement dans les modèles Liquid par la suite. Maintenez vos recommandations à jour en les actualisant régulièrement au fur et à mesure que votre moteur de recommandation produit de nouveaux résultats.

## Étape 2 : Récupérer les métadonnées produit {#step-2-retrieve-product-metadata}

Après avoir stocké un identifiant de recommandation sur chaque profil utilisateur, vous devez récupérer les métadonnées produit complètes (nom, prix, image, etc.) à inclure dans votre message. Vous avez deux options :

- **Option A :** [Catalogues Braze](#option-a-braze-catalogs) — stocker les informations produit directement dans Braze pour des recherches rapides et intégrées.
- **Option B :** [Contenu connecté](#option-b-connected-content) — récupérer les informations produit depuis une API externe au moment de l'envoi.

### Option A : Catalogues Braze {#option-a-braze-catalogs}

Si vous avez créé un [catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/create) avec votre inventaire de produits, vous pouvez rechercher des éléments directement dans votre message en utilisant Liquid. Pour un guide complet, consultez [Utiliser les catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs/use).

#### Recommander un élément de catalogue spécifique {#recommend-a-specific-catalog-item}

{% raw %}
Pour référencer un produit spécifique par ID, utilisez l'étiquette Liquid `catalog_items`. Par exemple, pour recommander le produit `1001` d'un catalogue nommé `retail_products` :

```liquid
{% catalog_items retail_products 1001 %}

We have a new item we think you'll like:
Category: {{ items[0].category }}
Name: {{ items[0].name }}
Price: ${{ items[0].price }}
```
{% endraw %}

#### Recommander plusieurs éléments de catalogue {#recommend-multiple-catalog-items}

{% raw %}
Vous pouvez également référencer plusieurs éléments dans une seule étiquette. Par exemple, pour mettre en avant trois produits :

```liquid
{% catalog_items retail_products 1001 1003 1005 %}

New items added in:
- {{ items[0].category }}
- {{ items[1].category }}
- {{ items[2].category }}

Visit our store to learn more!
```
{% endraw %}

#### Créer un modèle d'éléments à partir de la recommandation d'un utilisateur {#template-items-using-a-users-recommendation}

{% raw %}
Combinez l'attribut personnalisé de l'[étape 1](#step-1-store-recommendations-on-user-profiles) avec une recherche de catalogue pour personnaliser la recommandation pour chaque utilisateur :

```liquid
{% catalog_items retail_products {{custom_attribute.${recommended_product_id}}} %}

Hi {{${first_name}}}, check out our pick for you:
{{ items[0].name }} — ${{ items[0].price }}
```
{% endraw %}

### Option B : Contenu connecté {#option-b-connected-content}

Si les métadonnées de vos produits se trouvent dans un service externe plutôt que dans un catalogue Braze, utilisez le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call) pour les récupérer au moment de l'envoi.

{% raw %}
Par exemple, si votre API interne renvoie les détails d'un produit par ID :

```liquid
{% connected_content https://api.yourcompany.com/products/{{custom_attribute.${recommended_product_id}}} :save product %}

Hi {{${first_name}}}, we think you'll love:
{{ product.name }} — ${{ product.price }}
```
{% endraw %}

Pour plus de détails sur les appels API depuis vos messages, consultez [Effectuer un appel API]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call).

{% alert warning %}
Évitez d'utiliser le contenu connecté pour récupérer une grande liste de produits, puis d'itérer sur cette liste en Liquid au moment de l'envoi. Les payloads de réponse volumineux augmentent la latence d'envoi et peuvent provoquer des délais d'expiration de message ou des échecs de distribution à grande échelle. Stockez plutôt uniquement les ID de produits spécifiques dont un utilisateur a besoin sur son profil (voir l'[étape 1](#step-1-store-recommendations-on-user-profiles)), et récupérez les métadonnées pour ces éléments individuels ou utilisez les [catalogues](#option-a-braze-catalogs), qui sont optimisés pour des recherches rapides.
{% endalert %}

## Étape 3 : Vérifier votre intégration {#step-3-verify-your-integration}

Après avoir terminé la configuration, vérifiez votre intégration :

1. Utilisez l'endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) pour écrire une recommandation de test dans votre propre profil utilisateur.
2. Envoyez un message de test qui fait référence au produit recommandé en utilisant les Catalogs ou le contenu connecté.
3. Confirmez que les détails du produit s'affichent correctement dans le message distribué.
4. Dans le tableau de bord de Braze, accédez à la page de résultats de la Campaign ou du Canvas et confirmez que l'envoi est bien enregistré.

## Considérations {#considerations}

- Maintenez l'exactitude des données de recommandation en mettant à jour régulièrement les attributs personnalisés à mesure que votre moteur de recommandation produit de nouveaux résultats.
- Utilisez les [fonctionnalités de personnalisation]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) de Braze pour affiner davantage les messages, par exemple en intégrant des données spécifiques à l'utilisateur aux détails des produits.
- Envisagez d'utiliser la [distribution déclenchée par API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) pour déclencher des messages depuis votre backend en utilisant des modèles définis dans le tableau de bord de Braze.