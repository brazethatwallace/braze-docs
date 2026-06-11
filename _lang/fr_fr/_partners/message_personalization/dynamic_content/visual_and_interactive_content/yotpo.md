---
nav_title: Yotpo
article_title: Yotpo
alias: /partners/yotpo/
description: "Cet article de référence présente le partenariat entre Braze et Yotpo, une plateforme leader de marketing eCommerce qui aide des milliers de marques avant-gardistes à accélérer la croissance des ventes directes au consommateur."
page_type: partner
search_tag: Partner
---

# Yotpo

> [Yotpo](https://www.yotpo.com/), la principale plateforme de marketing eCommerce, aide des milliers de marques avant-gardistes à accélérer la croissance du direct-to-consumer. L'approche de plateforme unique de Yotpo intègre des solutions axées sur les données pour les avis, la fidélisation, le marketing par SMS et plus encore, donnant aux marques les moyens de créer des expériences clients plus intelligentes et à plus fort taux de conversion.

_Cette intégration est maintenue par Yotpo._

## À propos de l'intégration {#about-the-integration}

Grâce à l'intégration de Braze et de Yotpo, vous pouvez extraire et afficher de manière dynamique les évaluations par étoiles, les meilleurs avis et le contenu visuel généré par les utilisateurs (CGU) sur les produits dans les e-mails et les autres canaux de communication de Braze. Vous pouvez également inclure les données de fidélisation au niveau du client dans les e-mails et autres méthodes de communication afin de créer une interaction plus personnalisée, ce qui stimule les ventes et la fidélisation.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Yotpo | Un compte Yotpo est nécessaire pour bénéficier de ce partenariat. |
| Clé API des avis Yotpo | Cette API sera mise en œuvre dans l'extrait de code de Contenu connecté.<br><br>Pour plus d'informations, reportez-vous à la section [Trouver votre clé d'application Yotpo et votre clé secrète](https://support.yotpo.com/en/article/finding-your-yotpo-app-key-and-secret-key). |
| Clé API de fidélisation Yotpo | Cette clé API et cet identifiant unique global (GUID) seront mis en œuvre dans l'extrait de code de Contenu connecté.<br><br>Pour plus d'informations, reportez-vous à la section [Trouver votre clé API et GUID de fidélisation et de recommandation](https://support.yotpo.com/en/article/finding-your-loyalty-referrals-api-key-and-guid)|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Avant de continuer, confirmez que l'ID du produit Yotpo est le même que le `product_id` qui sera extrait dynamiquement de Braze. Cette étape est obligatoire pour que l'intégration fonctionne.

Pour trouver votre ID de produit Yotpo, procédez comme suit :

1. Rendez-vous sur le site web de votre boutique.
2. Ouvrez la page du produit.
3. Faites un clic droit et sélectionnez **Inspect**.
4. Appuyez sur <kbd>Control</kbd> + <kbd>F</kbd> et recherchez `yotpo-main` dans le code. La variable `data-product ID` et sa valeur apparaissent dans la div Yotpo.

![Inspectez et recherchez yotpo-main pour trouver la variable data-product ID]({% image_buster /assets/img/yotpo/image1.png %})

## Intégration {#integration}

Pour intégrer Yotpo et Braze, procédez comme suit :

1. Rendez-vous sur votre tableau de bord de Braze.
2. Sur la page **Campaigns**, cliquez sur **Create Campaign** et sélectionnez **Email**.
3. Sélectionnez le modèle de votre choix.
4. Cliquez sur **Edit email body** et ajoutez l'extrait de [Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) correspondant à votre cas d'utilisation :
    - [Afficher la note en étoiles et le nombre d'avis d'un produit](#star-review-count)
    - [Afficher un avis 5 étoiles récent pour un produit](#five-star-review)
    - [Afficher les CGU visuels par produit](#visual-ugc)
    - [Afficher le solde de fidélité d'un client dans un e-mail](#loyalty-balance)

### Afficher la note en étoiles et le nombre d'avis d'un produit {#star-review-count}

Utilisez cet extrait de code pour fournir la note moyenne publique et le nombre total d'avis pour un produit inclus dans l'e-mail :

{% raw %}
```liquid
{% connected_content https://api.yotpo.com/products/<YOTPO-API-KEY>/{{event_properties.${product_id}}}/bottomline :save result %}

{% if {{result.response.bottomline.average_score}} != 0 %}

The average rating for this product is:

{{result.response.bottomline.average_score}}/5, based on {{result.response.bottomline.total_reviews}} reviews.

{% else %}
{% endif %}
```
{% endraw %}

Remplacez `<YOTPO-API-KEY>` par votre clé API des avis Yotpo. Le `product_id` sera extrait dynamiquement de Braze. Pour que l'intégration fonctionne, le `product_id` dans Braze doit correspondre à l'ID du produit dans Yotpo (généralement l'ID du produit parent eCommerce).

![Remplacez YOTPO-API-KEY par votre clé API des avis Yotpo]({% image_buster /assets/img/yotpo/image2.png %})

### Afficher un avis 5 étoiles récent pour un produit {#five-star-review}

Utilisez cet extrait de code pour fournir un avis de premier plan (publié) pour un produit spécifique inclus dans l'e-mail :

{% raw %}
```liquid
{% connected_content https://api.yotpo.com/v1/widget/<YOTPO-API-KEY>/products/{{event_properties.${product_id}}}/reviews.json?per_page=50&star=5&sort=votes_up :save result %}

{% if {{result.response.reviews[0].score}} == 5 %}

Recent 5 Star Review for this product:

{{result.response.reviews[0].content}}

{% else %}
{% endif %}
```
{% endraw %}

Remplacez `<YOTPO-API-KEY>` par votre clé API des avis Yotpo. Le `product_id` sera extrait dynamiquement de Braze. Pour que l'intégration fonctionne, le `product_id` dans Braze doit correspondre à l'ID du produit dans Yotpo (généralement l'ID du produit parent eCommerce).

Voici à quoi ressemblera l'extrait de code dans votre éditeur d'e-mail :

![Exemple d'extrait de code dans l'éditeur d'e-mail pour des avis 5 étoiles récents]({% image_buster /assets/img/yotpo/image3.png %})

### Afficher les CGU visuels par produit {#visual-ugc}

Utilisez cet extrait de code pour récupérer les images Yotpo étiquetées et publiées et les ajouter à vos e-mails à la place de l'image de stock ou en tant que galerie supplémentaire :

{% raw %}
```liquid

{% connected_content https://api.yotpo.com/v1/widget/<YOTPO-API-KEY>/albums/product/{{event_properties.${product_id}}}?per_page=1 :save result %}

{% if {{result.response.images[0].tagged_products[0].image_url}} != null %}

The Visual content of the product:

<img src="{{result.response.images[0].tagged_products[0].image_url}}" border="0" width="200" height="200" alt="" />

{% else %}

Image return NULL

{% endif %}
```
{% endraw %}

Remplacez `<YOTPO-API-KEY>` par votre clé API des avis Yotpo. Le `product_id` sera extrait dynamiquement de Braze. Pour que l'intégration fonctionne, le `product_id` dans Braze doit correspondre à l'ID du produit dans Yotpo (généralement l'ID du produit parent eCommerce).

L'extrait de code ressemblera à ceci :

![Exemple d'éditeur d'e-mail affichant un extrait de code d'images publiées sur Yotpo]({% image_buster /assets/img/yotpo/image4.png %})

### Afficher le solde de fidélité d'un client dans un e-mail {#loyalty-balance}

Utilisez cet extrait de code pour récupérer le solde de points de fidélité d'un client et l'utiliser dans vos e-mails :

{% raw %}
```liquid
{% connected_content

https://loyalty.yotpo.com/api/v2/customers?customer_email=**{{${email_address}}}**
:method get
:headers {
    "x-guid": "<YOTPO-LOYALTY-GUID>",
    "x-api-key": "<YOTPO-LOYALTY-API-KEY>"
        }
:content_type application/json
:save publication
%}

You have {{publication.points_balance}} points

Only {{publication.vip_tier_upgrade_requirements.points_needed}} more points to become part of our VIP Tier!
```
{% endraw %}

Remplacez `<YOTPO-LOYALTY-GUID>` et `<YOTPO-LOYALTY-API-KEY>` par vos identifiants de fidélité Yotpo. L'`email_address` est extraite dynamiquement de Braze. Pour que l'intégration fonctionne, l'adresse e-mail doit être celle du client qui reçoit l'e-mail.

L'extrait de code ressemblera à ceci :

![Exemple d'éditeur d'e-mail affichant un extrait de code du solde de fidélité du client]({% image_buster /assets/img/yotpo/image5.png %})

## Questions fréquemment posées {#faq}

### Que se passe-t-il si je n'ai pas d'avis 5 étoiles ? {#what-if-i-dont-have-a-5-star-review}

Si vous n'avez pas d'avis 5 étoiles (par exemple si la réponse de l'endpoint renvoie NULL pour l'avis 5 étoiles), aucun contenu ne sera affiché.

### Que faire si je n'ai pas d'image publiée pour un produit ? {#what-if-i-dont-have-an-image-published-for-a-product}

Si vous n'avez pas d'images pour un produit (par exemple si la réponse de l'endpoint renvoie NULL pour l'image du produit), aucun contenu ne sera affiché.

### Puis-je personnaliser l'apparence ou extraire d'autres champs de données de Yotpo ? {#can-i-customize-the-look-and-feel-or-pull-other-data-fields-from-yotpo}

Oui ! Pour découvrir les autres points de données et les options de personnalisation disponibles, reportez-vous à la section [Effectuer un appel API]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/). Pour ce faire, vous aurez peut-être besoin de l'aide d'un développeur front-end.

{% alert note %}
Yotpo ne prend pas en charge les exigences personnalisées au-delà de ce qui est décrit dans ce guide.
{% endalert %}