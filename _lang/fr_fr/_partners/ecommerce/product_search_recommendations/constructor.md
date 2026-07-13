---
nav_title: Constructor
article_title: Constructor
description: "Cet article de référence présente le partenariat entre Braze et Constructor. Ce partenariat vous permet de tirer parti de la découverte de produits hors site de Constructor pour générer et fournir de manière dynamique des recommandations de produits personnalisées dans les messages Braze."
alias: /partners/constructor/
page_type: partner
search_tag: Partner
---

# Constructor

> [Constructor](https://constructor.com/) est une plateforme de recherche et de découverte de produits qui utilise l'intelligence artificielle et le machine learning pour offrir des recherches, des recommandations et des expériences de navigation personnalisées pour les sites web d'eCommerce et de vente au détail.

Grâce à l'intégration entre Braze et Constructor, vous pouvez utiliser la découverte de produits hors site de Constructor pour générer et fournir de manière dynamique des recommandations de produits personnalisées dans les messages Braze.

## Cas d'usage {#use-cases}

- **Suivi des paniers abandonnés et des commandes passées** : générez des recommandations de produits dynamiques basées sur le comportement de l'utilisateur et le contenu du panier pour envoyer des rappels de panier abandonné personnalisés ou des suggestions après la commande.
- **Recommandations de produits similaires pour les articles du panier abandonné** : suggérez des produits similaires aux articles laissés dans le panier d'un utilisateur pour maintenir son intérêt et lui proposer des alternatives.
- **Rappels des articles récemment consultés** : notifiez les utilisateurs des articles qu'ils ont récemment consultés mais qu'ils n'ont pas encore achetés, afin de les encourager à finaliser leur achat.
- **Campagnes de promotion** : envoyez des messages promotionnels personnalisés avec des recommandations de produits adaptées aux préférences des utilisateurs pour les ventes saisonnières ou les offres spéciales.
- **Suggestions de produits visuellement similaires** : recommandez des articles visuellement similaires à ceux que l'utilisateur a récemment consultés, afin de l'aider à découvrir des options connexes qu'il pourrait préférer.

## Prérequis {#prerequisites}

| Condition | Description |
|-------------|-------------|
| Compte Constructor | Un compte Constructor avec son service de découverte hors site activé est nécessaire pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration {#integration}

Collaborez avec votre équipe d'onboarding Constructor pour mener à bien le processus d'intégration. Assurez-vous que les données comportementales de votre site web ou d'autres sources de données pertinentes sont disponibles pour permettre des recommandations de produits personnalisées. Votre équipe d'onboarding Constructor vous aidera également à configurer les extraits de code HTML nécessaires à l'utilisation dans les messages Braze.

## URL de l'API de découverte hors site de Constructor {#constructors-offsite-discovery-api-url}

Vous pouvez utiliser l'URL de l'API de découverte hors site de Constructor pour afficher les images des produits et diriger les utilisateurs vers la page de détail du produit appropriée. Vous trouverez ci-dessous une description de la structure de l'endpoint et un exemple d'utilisation :

### Exemple {#example}

```html
<a href="https://offsite-discovery.cnstrc.com/v1/product/url?position=[position]&ui=[ui]&pod_id=[pod_id]&key=[key]&style_id=[style_id]&campaign_id=[campaign_id]" target="_blank">
  <img
    src="https://offsite-discovery.cnstrc.com/v1/product/image?position=[position]&ui=[ui]&pod_id=[pod_id]&key=[key]&style_id=[style_id]&campaign_id=[campaign_id]"
    width="200"
    border="0"
    alt="Shop Now"
  />
</a>
```

### Paramètres {#parameters}

| Paramètre | Description |
|-------------|-------------|
| `position` | Fait référence au classement de l'article recommandé dans la liste suggérée (par exemple, `position = 2`). <br>![Classement de la position de l'article.]({% image_buster /assets/img/constructor/constructor_position.png %}) |
| `ui` | Représente l'identifiant de l'utilisateur, essentiel pour personnaliser les résultats des recommandations. Définissez le paramètre `ui` comme étant l'`external_id` du client dans Braze. S'il est omis, Constructor renverra des recommandations générales au lieu de recommandations spécifiques à l'utilisateur. |
| `pod_id` | Identifiant du pod contenant la stratégie et les règles de searchandising pour les recommandations (par exemple, un pod avec une stratégie bestseller génère un bestseller personnalisé). |
| `key` | La clé d'index Constructor pour ce client. |
| `style_id` | Détermine les images affichées pour la fiche produit. Par exemple, différents `style_ids` affichent des images de fiches produits distinctes. |
| `campaign_id` | ID unique pour la campagne d'e-mail. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paramètres" }

### Entrées facultatives {#optional-inputs}

| Entrée | Description |
|-------------|-------------|
| `item_id` | Représente l'élément initiateur. Nécessaire pour les stratégies basées sur les articles, telles que les alternatives, les complémentaires et les lots. Par exemple, le premier élément d'un e-mail est l'élément initiateur, les éléments suivants constituant des alternatives. |
| `num_results` | Nombre de produits à ajouter à l'e-mail. La valeur par défaut est 10, jusqu'à 100. Par exemple, `num_results = 3` signifie que trois recommandations sont ajoutées. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Entrées facultatives" }