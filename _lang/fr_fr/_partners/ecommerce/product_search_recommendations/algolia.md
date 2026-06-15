---
nav_title: Algolia
article_title: Algolia
description: "Découvrez comment utiliser Algolia avec le Contenu connecté de Braze pour fournir dynamiquement des résultats de recherche personnalisés et des recommandations produit dans vos messages Braze."
alias: /partners/algolia/
page_type: partner
search_tag: Partner
---

# Algolia

> [Algolia](https://www.algolia.com/) est une plateforme de recherche et de découverte qui aide les développeurs à créer des expériences de recherche rapides, pertinentes et évolutives. Grâce à une approche API-first, Algolia combine des algorithmes de classement avancés avec des informations basées sur l'intelligence artificielle pour offrir une recherche fluide sur site, une navigation et une découverte de contenu personnalisée.

L'intégration d'Algolia et de Braze utilise le [Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) pour alimenter les résultats de recherche et les recommandations produit propulsés par Algolia dans vos messages Braze. En interrogeant l'API d'Algolia au moment de l'envoi, vous pouvez fournir du contenu personnalisé qui dirige les utilisateurs vers des pages de détail produit ou des pages d'accueil à fort taux de conversion.

## Cas d'utilisation {#use-cases}

- **Promouvoir les produits tendance :** Intégrez automatiquement les produits tendance ou les plus performants d'Algolia dans les messages Braze pour promouvoir les articles à fort intérêt et augmenter l'engagement.
- **Personnaliser les campagnes avec l'intelligence de recherche :** Personnalisez les Campaigns Braze en utilisant l'intelligence de recherche et de navigation d'Algolia pour proposer des produits ou des catégories alignés sur les intérêts de chaque utilisateur.

## Conditions préalables {#prerequisites}

| Condition | Description |
|-------------|-------------|
| Compte Algolia | Un compte Algolia est requis pour bénéficier de ce partenariat. |
| Identifiants API Algolia | Votre clé API Algolia et votre ID d'application. |
| Index produit Algolia | Un index Algolia alimenté avec vos données produit. Ceci est requis pour utiliser les API Search ou Recommend. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration {#integration}

### Étape 1 : Configurer votre requête API Algolia {#step-1-set-up-your-algolia-api-request}

Pour plus d'informations sur les formats de requête, les structures de réponse et l'utilisation, consultez la documentation de l'[API Algolia Search](https://www.algolia.com/doc/rest-api/search) et de l'[API Algolia Recommend](https://www.algolia.com/doc/rest-api/recommend). Si vous avez besoin d'aide pour la configuration, contactez l'équipe Algolia.

{% tabs local %}
{% tab Search API %}

#### Exemple de requête Search API {#example-search-api-request}

```
POST https://{ALGOLIA_APP_ID}-dsn.algolia.net/1/indexes/{INDEX_NAME}/query
Content-Type: application/json
X-Algolia-API-Key: {ALGOLIA_API_KEY}
X-Algolia-Application-Id: {ALGOLIA_APP_ID}
```

#### Exemple de payload de requête {#example-query-payload}

```json
{
  "query": "",
  "hitsPerPage": 4,
  "filters": "category_page_id:'this week's offers'",
  "attributesToRetrieve": ["name", "price", "image", "url"]
}
```

Dans cet exemple, la requête récupère les quatre premiers résultats d'une page qui utilise un filtre de catégorie basé sur un attribut appelé `category_page_id`. Le paramètre `attributesToRetrieve` limite la réponse pour maintenir le payload à une taille gérable.

**Exemple de cas d'utilisation :** Pour mettre en avant les résultats de recherche de `https://www.yoursite.com/weekly-offers` dans une Campaign Braze d'offres hebdomadaires, interrogez l'index Algolia correspondant et appliquez des filtres pour récupérer les meilleurs résultats de cette page.

{% alert tip %}
Récupérez des champs supplémentaires à l'aide de `attributesToRetrieve` pour enrichir la personnalisation, comme les notes, les avis ou les réductions.
{% endalert %}

{% endtab %}
{% tab Recommend API %}

#### Exemple de requête Recommend API {#example-recommend-api-request}

```
POST https://{ALGOLIA_APP_ID}.algolia.net/1/indexes/*/recommendations
Content-Type: application/json
X-Algolia-API-Key: {ALGOLIA_API_KEY}
X-Algolia-Application-Id: {ALGOLIA_APP_ID}
```

#### Exemple de payload de requête

```json
{
  "requests": [
    {
      "indexName": "prod_ECOM",
      "model": "trending-items",
      "threshold": 40,
      "maxRecommendations": 4
    }
  ]
}
```

L'API Recommend prend en charge plusieurs modèles, notamment **Frequently Bought Together**, **Related Products**, **Trending Items**, **Trending Facet Values** et **Looking Similar**. Cet exemple utilise le modèle **Trending Items**.

{% alert important %}
Si vos recommandations reposent sur des attributs spécifiques à l'utilisateur ou des objectIDs, soyez attentif aux limites de débit définies dans votre contrat Algolia. Consultez la section [Considérations](#considerations) pour les bonnes pratiques.
{% endalert %}

{% endtab %}
{% endtabs %}

### Étape 2 : Implémenter le Contenu connecté Braze {#step-2-implement-braze-connected-content}

Utilisez la fonctionnalité Contenu connecté de Braze pour effectuer des appels API vers les endpoints Algolia et injecter dynamiquement la réponse dans un message. Pour plus d'informations sur la configuration, le formatage des requêtes et les bonnes pratiques, consultez [Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/).

{% tabs local %}
{% tab Search API %}

#### Exemple de requête Contenu connecté Search {#example-connected-content-search-request}

{% raw %}
```liquid
{% capture request_body %}
{
  "query": "",
  "hitsPerPage": 4,
  "filters": "category_page_id:'this week's offers'",
  "attributesToRetrieve": ["name", "price", "image", "url"]
}
{% endcapture %}

{% connected_content https://{{ALGOLIA_APP_ID}}-dsn.algolia.net/1/indexes/{{INDEX_NAME}}/query
  :method post
  :headers {"X-Algolia-API-Key":"{{ALGOLIA_API_KEY}}", "X-Algolia-Application-Id":"{{ALGOLIA_APP_ID}}", "Content-Type": "application/json"}
  :body {{request_body}}
  :save algolia_search
%}
```
{% endraw %}

{% endtab %}
{% tab Recommend API %}

#### Exemple de requête Contenu connecté Recommend {#example-connected-content-recommend-request}

{% raw %}
```liquid
{% capture request_body %}
{
  "requests": [
    {
      "indexName": "prod_ECOM",
      "model": "trending-items",
      "threshold": 40,
      "maxRecommendations": 4
    }
  ]
}
{% endcapture %}

{% connected_content https://{{ALGOLIA_APP_ID}}.algolia.net/1/indexes/*/recommendations
  :method post
  :headers {"X-Algolia-Application-Id":"{{ALGOLIA_APP_ID}}", "X-Algolia-API-Key":"{{ALGOLIA_API_KEY}}", "Content-Type": "application/json"}
  :body {{request_body}}
  :save algolia_recommendations
%}
```
{% endraw %}

{% endtab %}
{% endtabs %}

### Étape 3 : Formater les résultats de recherche dans les messages Braze {#step-3-format-search-results-in-braze-messages}

Après avoir récupéré les résultats d'Algolia, utilisez Liquid pour analyser la réponse de l'API et afficher dynamiquement les résultats dans votre message.

{% tabs local %}
{% tab Search API %}

#### Exemple de modèle d'e-mail Liquid pour Search API {#example-liquid-email-template-for-search-api}

{% raw %}
```liquid
{% for item in algolia_search.hits %}
  <div style="margin-bottom: 10px;">
    <img src="{{ item.image }}" alt="{{ item.name }}" width="100"/>
    <p><strong>{{ item.name }}</strong></p>
    <p>Price: ${{ item.price }}</p>
    <a href="{{ item.url }}">View Product</a>
  </div>
{% endfor %}
```
{% endraw %}

Cela génère une liste de produits à partir des résultats de la Search API dans le corps du message. Chaque lien produit dirige les utilisateurs vers une page de détail produit (PDP) ou une page d'accueil spécifique à la campagne.

{% endtab %}
{% tab Recommend API %}

#### Exemple de modèle d'e-mail Liquid pour Recommend API {#example-liquid-email-template-for-recommend-api}

{% raw %}
```liquid
{% for item in algolia_recommendations.hits %}
  <div style="margin-bottom: 10px;">
    <img src="{{ item.image }}" alt="{{ item.name }}" width="100"/>
    <p><strong>{{ item.name }}</strong></p>
    <p>Price: ${{ item.price }}</p>
    <a href="{{ item.url }}">View Product</a>
  </div>
{% endfor %}
```
{% endraw %}

Cela génère une liste de produits recommandés à partir des résultats de la Recommend API dans le corps du message. Chaque lien produit dirige les utilisateurs vers une page de détail produit (PDP) ou une page d'accueil spécifique à la campagne.

{% endtab %}
{% endtabs %}

## Considérations {#considerations}

### Éviter les requêtes uniques {#avoiding-unique-queries}

Soyez attentif aux limites de débit Algolia définies dans votre contrat. Évitez d'effectuer des requêtes spécifiques à l'utilisateur, car celles-ci peuvent rapidement dépasser le nombre de requêtes allouées. Pour personnaliser les résultats, ciblez un segment plutôt qu'un ID utilisateur individuel, ou filtrez par catégorie ou marque plutôt que par un objectID spécifique. Utilisez les attributs Braze pour personnaliser davantage les recommandations.

### Mise en cache des résultats du Contenu connecté {#caching-connected-content-results}

Mettez en cache les résultats du Contenu connecté à l'aide de `cache_max_age` pour minimiser les requêtes API vers Algolia et améliorer les performances. Pour plus d'informations, consultez [Mise en cache des réponses]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses/).