---
nav_title: Messages produit
article_title: Messages produit
page_order: 4
description: "Cette page explique comment utiliser les messages produit WhatsApp pour envoyer des messages WhatsApp interactifs qui présentent des produits de votre catalogue Meta."
page_type: reference
alias: "/whatsapp_product_messages/"
tool:
 - Campaigns
channel:
 - WhatsApp
---

# Messages produit {#product-messages}

> Les messages produit vous permettent d'envoyer des messages WhatsApp interactifs qui présentent des produits directement depuis votre catalogue Meta.

Lorsque vous envoyez un message produit WhatsApp à un utilisateur, celui-ci suit le parcours client suivant :

1. L'utilisateur reçoit votre message produit ou catalogue dans WhatsApp.
2. L'utilisateur ajoute des produits à son panier directement depuis WhatsApp.
3. L'utilisateur appuie sur **Place order** dans WhatsApp.
4. Votre site web ou application reçoit les données du panier depuis Braze et génère un lien de paiement.
5. L'utilisateur est redirigé vers votre site web ou application pour finaliser son achat.

Lorsque les utilisateurs ajoutent des articles à leur panier via les messages catalogue, Braze reçoit des données webhook pour les actions de suivi.

## Conditions requises {#requirements}

| Condition | Description |
| --- | --- |
| Compte WhatsApp Business | Pour utiliser les messages produit WhatsApp, vous devez disposer d'un compte WhatsApp Business connecté à Braze. |
| Catalogue Meta | Vous devez configurer un catalogue Meta dans votre Commerce Manager. |
| Conformité aux conditions | Respectez les [conditions et politiques commerciales de Meta](https://www.facebook.com/policies_center/commerce). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements" }

## Types de messages produit {#product-message-types}

{% alert note %}
Améliorez votre expérience de messages produit grâce au sélecteur de produits intégré, accessible lors de l'étape 4 de la [configuration des messages produit](#setting-up-product-messages).
{% endalert %}

{% tabs local %}
{% tab Messages catalogue %}

Les messages catalogue affichent l'intégralité de votre catalogue de produits dans un format interactif. Ils sont disponibles en tant que [messages modèle et messages de réponse](#building-a-product-message).

Si vous avez activé les autorisations de catalogue pour Braze lors de la [configuration](#setting-up-product-messages), vous pouvez sélectionner la miniature visible par les utilisateurs.

{% alert note %}
Vous n'avez pas besoin de faire de sélections de produits supplémentaires dans Braze, car la connexion au catalogue est gérée par Meta et est donc héritée dans votre catalogue de produits.
{% endalert %}


{% endtab %}
{% tab Messages multi-produits %}

Les messages multi-produits mettent en avant des produits spécifiques de votre catalogue, avec jusqu'à 30 articles mis en avant par message. Ils sont disponibles en tant que [messages modèle et messages de réponse](#building-a-product-message).

Vous pouvez sélectionner les produits manuellement avec des ID ou, si vous avez activé les autorisations de catalogue lors de la [configuration](#setting-up-product-messages), utiliser le sélecteur de produits déroulant.

{% alert important %}
Il existe un problème d'affichage d'en-tête connu avec les modèles de messages multi-produits sur Meta. Meta est au courant du problème et travaille sur un correctif.
{% endalert %}

{% endtab %}
{% tab Produit unique %}

Les messages produit unique mettent en avant un produit spécifique de votre catalogue de produits. Ils sont disponibles en tant que [messages de réponse](#building-a-product-message).

Vous pouvez sélectionner les produits manuellement avec des ID ou, si vous avez activé les autorisations de catalogue lors de la [configuration](#setting-up-product-messages), utiliser le sélecteur de produits déroulant.

{% endtab %}
{% endtabs %}

## Configuration des messages produit {#setting-up-product-messages}

1. Dans le [Meta Commerce Manager](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fbusiness.facebook.com%2Fcommerce_manager%2F#), suivez [les instructions de Meta](https://www.facebook.com/business/help/1275400645914358?id=725943027795860&ref=search_new_1) pour créer votre catalogue Meta. Assurez-vous d'être dans le même portefeuille Meta Business que celui où réside votre compte WhatsApp Business connecté à Braze.
2. Suivez les instructions de Meta pour [connecter votre catalogue Meta](https://www.facebook.com/business/help/1953352334878186?id=2042840805783715) à votre compte WhatsApp Business connecté à Braze en attribuant l'autorisation « Manage Catalog » dans Meta Business Manager.

![Page « Catalogs » de Meta avec une flèche pointant vers le bouton « Assign partner » pour le catalogue appelé « sweeney_catalog ».]({% image_buster /assets/img/whatsapp/meta_catalog.png %}){: style="max-width:90%;"}

Assurez-vous d'utiliser l'ID Braze Business Manager, `332231937299182`, comme ID d'entreprise partenaire.

![Fenêtre de partage d'un catalogue avec un partenaire contenant des champs pour saisir un ID d'entreprise partenaire et attribuer l'autorisation « Manage catalog ».]({% image_buster /assets/img/whatsapp/share_meta_catalog.png %}){: style="max-width:70%;"}

{: start="3"}
3. Sélectionnez les paramètres de votre catalogue Meta. Vous devez sélectionner **Show catalog icon in chat header** pour envoyer des messages catalogue.

![Page de paramètres du gestionnaire WhatsApp pour le catalogue « Catalog_products ».]({% image_buster /assets/img/whatsapp/meta_catalog_settings.png %}){: style="max-width:90%;"}

{: start="4"}
4. Dans Braze, suivez le processus d'[inscription intégrée]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup/) pour fournir les autorisations. Assurez-vous de sélectionner **tous** les catalogues pour lesquels vous souhaitez fournir des autorisations. Cela débloquera le sélecteur de produits intégré de Braze.

![Fenêtre avec cinq catalogues sélectionnés pour fournir des autorisations.]({% image_buster /assets/img/whatsapp/select_catalogs.png %}){: style="max-width:50%;"}

{% alert tip %}
Pour les bonnes pratiques à suivre lors de la création de catalogues Meta, consultez [Conseils pour créer un catalogue de haute qualité dans Commerce Manager](https://www.facebook.com/business/help/2086567618225367?id=725943027795860).
{% endalert %}

## Créer un message produit {#building-a-product-message}

Vous pouvez créer un message produit en utilisant un modèle de message WhatsApp ou un message de réponse.

{% tabs local %}
{% tab Modèle de message WhatsApp %}

1. Dans votre Meta Business Manager, accédez à **Message Templates**.
2. Sélectionnez **Catalog** comme format, puis choisissez entre **Catalog message** (affiche le catalogue complet) et **Multi-product catalog message** (met en avant des articles spécifiques).
3. Dans Braze, créez une Campaign WhatsApp ou une étape de message Canvas.
4. Sélectionnez le groupe d'abonnement correspondant à l'endroit où vous avez soumis le modèle.
5. Sélectionnez **WhatsApp Template Message**.
6. Sélectionnez le modèle que vous souhaitez utiliser.
    - Si vous sélectionnez un modèle multi-produits, fournissez le titre de la section et les ID de contenu des produits à mettre en avant. Vous pouvez soit copier l'ID de contenu directement depuis votre Meta Commerce Manager, soit, si vous avez activé les autorisations pour le sélecteur de produits intégré, sélectionner les articles.

![Liste d'articles avec des champs pour saisir vos titres de section et ID de contenu.]({% image_buster /assets/img/whatsapp/multi_product_template.png %}){: style="max-width:60%;"}

![Liste d'articles avec un menu déroulant d'articles à sélectionner.]({% image_buster /assets/img/whatsapp/content_id_items.png %}){: style="max-width:60%;"}

{: start="7"}
7. Continuez à créer votre message.

{% endtab %}
{% tab Message de réponse %}

1. Dans Braze, créez une Campaign WhatsApp ou une étape de message Canvas.
2. Sélectionnez un groupe d'abonnement.
3. Sélectionnez **Response Message**.
4. Sélectionnez **Meta Product Messages**.

![Options pour sélectionner un type de message et une disposition de message de réponse, avec « Response Message » et « Meta Product Messages » mis en surbrillance.]({% image_buster /assets/img/whatsapp/response_message_layouts.png %}){: style="max-width:90%;"}

{: start="5"}
5. Sélectionnez le [type de message](#product-message-types) que vous souhaitez utiliser.

![Sélection de la disposition du message « Multi-product ».]({% image_buster /assets/img/whatsapp/multi-product_message_layout.png %}){: style="max-width:90%;"}

{: start="6"}
6. Continuez à créer votre message.

![Exemple de message produit Meta avec des informations renseignées pour les produits.]({% image_buster /assets/img/whatsapp/example_response_message.png %}){: style="max-width:90%;"}

{% endtab %}
{% endtabs %}

## Gestion des produits {#managing-products}

### Accéder au Commerce Manager {#accessing-commerce-manager}

Dans votre Meta Business Manager, accédez à **Commerce Manager** et sélectionnez votre organisation. Ici, vous pouvez gérer les ressources de votre catalogue, telles que :
- Créer de nouveaux catalogues
- Ajouter des produits aux catalogues existants
- Mettre à jour les informations produit
- Supprimer les articles abandonnés

{% alert important %}
Si vous supprimez des produits référencés de votre catalogue, les messages associés ne pourront pas être envoyés.
{% endalert %}

## Réception des questions entrantes sur les produits {#receiving-inbound-product-questions}

Les utilisateurs peuvent répondre à votre message produit ou catalogue avec des questions sur les produits. Celles-ci arrivent sous forme de messages entrants, qui peuvent ensuite être triés avec un [parcours d'action]({{site.baseurl}}/action_paths/).

De plus, Braze extrait l'ID du produit et l'ID du catalogue de ces questions. Si vous souhaitez automatiser les réponses ou transmettre les questions à une autre équipe (comme le support client), vous pouvez inclure ces détails. Par exemple, vous pourriez personnaliser les réponses avec les propriétés WhatsApp `inbound_product_id` ou `inbound_catalog_id`.

![Fenêtre « Ajouter une personnalisation » avec un type de personnalisation « WhatsApp Properties » et un attribut mis en surbrillance « inbound_product_id ».]({% image_buster /assets/img/whatsapp/inbound_product_questions.png %}){: style="max-width:60%;"}

## Paiement : traitement du panier et webhooks {#checkout-cart-processing-and-webhooks}

Lorsque les utilisateurs interagissent avec vos messages produit WhatsApp, ils peuvent parcourir les produits et ajouter des articles à leur panier. Cependant, il n'existe actuellement aucune fonctionnalité de paiement intégrée pour les informations de livraison ou le traitement des paiements. Nous vous encourageons plutôt à créer un panier dans votre propre application ou site web et à diriger les utilisateurs vers ce panier à l'aide d'un lien personnalisé.

### Points à considérer {#considerations}

- **Pas de paiement intégré :** les utilisateurs ne peuvent pas finaliser leurs achats directement dans WhatsApp. Toutes les transactions doivent être redirigées vers votre site web ou application.
- **Lien personnalisé requis :** vous devez créer un lien personnalisé qui dirige les utilisateurs vers leur panier sur votre plateforme.
- **Configuration manuelle :** le processus de configuration nécessite une configuration manuelle de votre panier et de vos workflows d'envoi de messages.

{% alert note %}
Nous ne prenons actuellement pas en charge les paiements directement dans WhatsApp, et la prise en charge future sera spécifique à chaque pays (actuellement, Meta ne le propose qu'aux entreprises basées en Inde, au Brésil et à Singapour et travaillant directement avec des utilisateurs dans ces pays).
{% endalert %}

### Configuration des déclencheurs d'événements de panier {#setting-up-cart-event-triggers}

Lorsqu'un client passe une commande dans WhatsApp, Braze effectue automatiquement les actions suivantes :
1. Réception du contenu du panier depuis WhatsApp (ID de produits, quantités et autres données de commande).
2. Création d'un événement eCommerce `ecommerce.cart_update` avec toutes les données pertinentes, y compris `source = whats_app`.
3. Déclenchement d'une réponse, vous permettant de configurer des Campaigns automatisées pour répondre à la commande.

L'événement eCommerce `ecommerce.cart_update` n'apparaît dans la liste de Braze qu'après l'envoi d'un événement, ce qui peut être fait en générant un message produit de test depuis Braze et en soumettant un événement de panier.
L'événement de panier inclut :

- **ID du panier :** identifiant unique du panier
- **Produits :** liste des articles avec les ID de produits, les quantités et les prix
- **Valeur totale :** somme de tous les articles
- **Devise :** la devise du panier
- **Source :** marquée comme « whats_app »
- **Métadonnées :** données supplémentaires comme l'ID du catalogue et le texte du message

Vous pouvez trouver des informations supplémentaires sur les événements de panier Braze dans [Types d'événements eCommerce recommandés]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/#types-of-ecommerce-recommended-events).

### Configuration d'une réponse déclenchée {#setting-up-a-triggered-response}

1. Créez un déclencheur d'événement personnalisé pour `ecommerce.cart_updated`.
2. Ajoutez un filtre de propriété pour `source = "whats_app"`.

![Étape Canvas pour un déclencheur d'événement personnalisé `ecommerce.cart_updated` avec la propriété de base « source » égale à `whats_app`.]({% image_buster /assets/img/whatsapp/product_message_canvas_step.png %})

{: start="3"}
3. Configurez les actions de suivi en fonction des données du panier.

### Implémentations de paiement recommandées {#recommended-checkout-implementations}

{% tabs local %}
{% tab Liens de panier basés sur Liquid %}

Utilisez Liquid pour créer des URL de panier directement dans votre message de réponse. C'est la meilleure option si vous avez des ID de produits cohérents entre WhatsApp et votre plateforme eCommerce.

#### Exemple Liquid {#example-liquid}

{% raw %}
```liquid
{% assign cart_link = "http://alejandro-test-new.myshopify.com/cart/" %}
{% for product in event_properties.products %}
 {% assign variant_id = product.product_id %}
 {% assign quantity = product.quantity %}
 {% if forloop.first %}
   {% assign cart_link = cart_link | append: variant_id | append: ":" | append: quantity %}
 {% else %}
   {% assign cart_link = cart_link | append: "," | append: variant_id | append: ":" | append: quantity %}
 {% endif %}
{% endfor %}
{{ cart_link }}
```
{% endraw %}

#### Configuration {#setup}

1. Créez une Campaign de message de réponse WhatsApp avec le déclencheur d'un événement eCommerce `ecommerce.cart_update`.
2. Créez un message suivant avec l'URL du panier.
3. Construisez votre URL de panier avec Liquid. Si vous utilisez Shopify, vous pouvez [créer un lien permanent de panier](https://shopify.dev/docs/apps/build/checkout/create-cart-permalinks) avec l'exemple Liquid précédent.

![Diagramme montrant le workflow de l'expérience de paiement pour un panier généré par Liquid : Meta envoie un message de commande reçue à Braze, qui déclenche un déclencheur basé sur une action puis crée un message avec un lien de panier, qui envoie ensuite un message WhatsApp.]({% image_buster /assets/img/whatsapp/liquid_generated_cart_link_checkout.png %})

{% endtab %}
{% tab Contenu connecté %}

Effectuez un appel API vers votre système eCommerce pour générer une URL de paiement personnalisée. C'est la meilleure option si vous avez besoin d'une génération dynamique d'URL de panier ou d'un mappage de produits complexe.

#### Configuration

1. Créez une Campaign webhook ou une étape Canvas déclenchée par l'événement eCommerce [`ecommerce.cart_update`]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events?tab=ecommerce.cart_updated), qui enverra les données du panier à votre système eCommerce.
2. Créez une Campaign WhatsApp ou une étape de message Canvas déclenchée par le même événement eCommerce pour envoyer un message de réponse WhatsApp avec l'URL du panier à l'utilisateur. Suivez les instructions du message de réponse suivant pour utiliser le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/).

![Diagramme montrant le workflow de l'expérience de paiement pour un appel de contenu connecté : Meta envoie un message de commande reçue à Braze, qui effectue des appels aller-retour avec une plateforme eCommerce, puis envoie un message WhatsApp.]({% image_buster /assets/img/whatsapp/connected_content_checkout.png %})

{% endtab %}
{% tab Webhooks et événements personnalisés %}

Utilisez des webhooks pour envoyer les données du panier à votre système, puis déclenchez des messages de suivi via des événements personnalisés. C'est la meilleure option pour les intégrations complexes nécessitant un traitement approfondi du panier ou des workflows en plusieurs étapes.

#### Configuration

Créez une Campaign webhook ou une étape Canvas déclenchée par l'événement eCommerce `ecommerce.cart_update`, qui enverra les données du panier à votre système eCommerce. Votre API effectuera ensuite les actions suivantes :
1. Réception des données du panier
2. Création d'un panier dans votre système
3. Génération de l'URL de paiement
4. Envoi d'un événement `checkout_started` à Braze, déclenchant l'envoi de votre message WhatsApp avec le lien de paiement

![Diagramme montrant le workflow de l'expérience de paiement pour les webhooks et événements personnalisés : Meta envoie un message de commande reçue à Braze, qui effectue des appels aller-retour avec une plateforme eCommerce, puis envoie un message WhatsApp avec l'URL du panier.]({% image_buster /assets/img/whatsapp/webhooks_custom_events_checkout.png %})

{% endtab %}
{% endtabs %}

## Tests et validation {#testing-and-validation}

### Conditions requises pour les messages de test {#test-message-requirements}

La fonctionnalité de panier est conservée entre les messages de test, mais le traitement du résultat entrant n'est pas conservé.

### Prévisualisation du message {#message-preview}

- Les images et détails des produits sont extraits de votre catalogue Meta.
- La prévisualisation interactive affiche des marques substitutives jusqu'à ce que l'intégration soit terminée.

### Codes d'erreur {#error-codes}

- Si un ID de produit n'existe pas dans le catalogue, vous recevrez l'erreur `product not found for product_retailer_id, fake-product-id, in catalog_id, 1903196950214359`.
- Si un catalogue est déconnecté du WABA, vous recevrez l'erreur `Check if catalog is linked to the WhatsApp Business Account and the catalog is enabled in the WhatsApp Commerce Settings`.