{% tabs %}
{% tab Abandoned browse %}

### Navigation abandonnée {#abandoned-browse}

Utilisez le modèle **Abandoned browse** pour engager les utilisateurs qui ont consulté des produits sans les ajouter à leur panier ni passer de commande.

![Un modèle Canvas « Abandoned Browse » appliqué avec les « Entry Rules » développées.]({% image_buster /assets/img_archive/abandoned_browse.png %})

#### Configuration {#setup}

Sur la page Canvas, sélectionnez **Use a Canvas Template** > **Braze templates**, puis appliquez le modèle **Abandoned browse**.

##### Paramètres par défaut {#default-settings}

Les paramètres suivants sont préconfigurés dans votre Canvas :
- Bases
    - Nom du Canvas : **Abandoned browse**
    - Événement de conversion : `ecommerce.order placed`
        - Date limite de conversion : 3 jours
- Planification d'entrée
    - Basé sur l'action lorsqu'un utilisateur effectue l'événement `ecommerce.product_viewed`
    - L'heure de début correspond au moment où vous créez le modèle Canvas<br><br>![« Action Based Options » pour le Canvas.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry.png %})<br><br>
- Audience cible
    - Audience d'entrée
        - L'e-mail **n'est pas vide**
        - Vous pouvez également modifier les critères de l'audience d'entrée pour répondre aux besoins de votre entreprise
    - Contrôles d'entrée
        - Les utilisateurs peuvent réintégrer ce Canvas une fois sa durée totale écoulée
    - Critères de sortie
        - Effectue `ecommerce.cart_updated`, `ecommerce.checkout_started` ou `ecommerce.order_placed`<br><br>![Contrôles d'entrée et critères de sortie pour le Canvas.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry_exit.png %})<br><br>
- Paramètres d'envoi
    - Utilisateurs abonnés ou ayant donné leur accord explicite (opt-in)
- Étape de délai
    - Délai d'une heure
- Étape de message
    - Consultez le modèle d'e-mail et le bloc HTML avec un exemple de modèle Liquid pour ajouter des produits à votre message dans le modèle préconstruit. Si vous utilisez votre propre modèle d'e-mail, vous pouvez également vous référer aux [variables Liquid](#message-personalization), comme illustré dans la section suivante.

#### Personnalisation des produits pour les e-mails de navigation abandonnée {#abandoned-browse-product-personalization-for-emails}

Voici un exemple montrant comment ajouter un bloc HTML de produit à votre e-mail de navigation abandonnée.

{% raw %}
```java
<table aria-label="Abandoned browse product personalization for emails" style="width:100%">
  <tr>
    <th><img src="{{context.${image_url}}}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{context.${product_name}}}</li>
        <li>Price: ${{context.${price}}}</li>
      </ul>
    </th>
  </tr>
</table>
```
{% endraw %}

##### URL du produit {#product-url}

{% raw %}
```liquid
{{context.${product_url}}}
```
{% endraw %}

{% endtab %}
{% tab Abandoned cart %}

### Panier abandonné {#abandoned-cart}

Utilisez le modèle **Abandoned cart** pour récupérer les ventes potentiellement perdues de clients ayant ajouté des produits à leur panier sans poursuivre vers le paiement ni passer de commande.

![Un modèle Canvas « Abandoned Cart » appliqué avec les « Entry Rules » développées.]({% image_buster /assets/img_archive/abandoned_cart.png %})

#### Configuration

Sur la page Canvas, sélectionnez **Use a Canvas Template** > **Braze templates**, puis appliquez le modèle **Abandoned cart**.

##### Paramètres par défaut

Les paramètres suivants sont préconfigurés dans votre Canvas :
- Bases
    - Nom du Canvas : **Abandoned cart**
    - Événement de conversion : `ecommerce.order_placed`
        - Date limite de conversion : 3 jours
- Planification d'entrée
    - Déclencheur basé sur l'action lorsqu'un utilisateur déclenche l'événement **Perform Cart Updated Event** (situé dans la liste déroulante)
    - L'heure de début correspond au moment où vous créez le modèle Canvas<br><br>![« Action Based Options » pour le Canvas.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry.png %})<br><br>
- Audience cible
    - Audience d'entrée
        - A utilisé ces applications **plus de 0** fois
        - L'e-mail **n'est pas vide**
    - Contrôles d'entrée
        - Les utilisateurs sont immédiatement rééligibles pour entrer dans le Canvas
    - Critères de sortie
        - Effectue `ecommerce.cart_updated`, `ecommerce.checkout_started` ou `ecommerce.order_placed`<br><br>![Contrôles d'entrée et critères de sortie pour le Canvas.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry_exit.png %})<br><br>
- Paramètres d'envoi
    - Utilisateurs abonnés ou ayant donné leur accord explicite (opt-in)
- Étape de délai
     - Délai de 4 heures
- Étape de message
    - Consultez le modèle d'e-mail et le bloc HTML avec un exemple de modèle Liquid pour ajouter des produits à votre message dans le modèle préconstruit. Si vous utilisez votre propre modèle d'e-mail, vous pouvez également vous référer aux [variables Liquid](#message-personalization), comme illustré dans la section suivante.

#### Fonctionnement de la logique de réentrée pour le panier abandonné {#how-abandoned-cart-re-entry-logic-works}

Lorsqu'un utilisateur commence le processus de paiement, son panier est marqué comme `checkout_started`. À partir de ce moment, toute mise à jour ultérieure du panier avec le même ID de panier ne permettra pas à l'utilisateur de réintégrer le parcours de panier abandonné.

1. Lorsqu'un utilisateur ajoute un article à son panier, il entre dans le Canvas.
2. Chaque fois qu'il ajoute ou met à jour des articles, il réintègre le Canvas, ce qui maintient les données de son panier et les messages à jour.
3. Lorsque l'utilisateur commence le processus de paiement, son panier est étiqueté `checkout_started` et il sort du Canvas.
4. Toute mise à jour future du panier utilisant le même ID de panier ne déclenchera pas de réentrée, car ce panier est déjà passé à l'étape de paiement.

Lorsque les utilisateurs passent au parcours de paiement, ils sont ciblés par le [Canvas de paiement abandonné](#abandoned-checkout), conçu pour les utilisateurs plus avancés dans leur parcours d'achat.

#### Personnalisation des produits du panier abandonné pour les e-mails {#abandoned-cart-checkout}

Les parcours de panier abandonné nécessitent une étiquette Liquid spéciale `shopping_cart` pour la personnalisation des produits.

Voici un exemple montrant comment ajouter un bloc HTML avec votre étiquette Liquid `shopping_cart` pour intégrer des produits dans votre e-mail.

{% raw %}
```java
<table aria-label="Abandoned cart product personalization for emails #abandoned-cart-checkout" style="width:100%">
  {% shopping_cart {{context.${cart_id}}} %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

{% alert note %}
Si vous utilisez Shopify, ajoutez le nom de votre catalogue pour obtenir l'URL de l'image de la variante.
{% endalert %}

##### URL du panier en HTML {#html-cart-url}

Si vous souhaitez rediriger les utilisateurs vers leur panier, vous pouvez ajouter une propriété d'événement imbriquée sous l'objet de métadonnées, par exemple :

{% raw %}
```liquid
{{context.${metadata}.cart_url}}
```
{% endraw %}

Si vous utilisez Shopify, créez l'URL de votre panier en utilisant ce modèle Liquid :

{% raw %}
```liquid
{{context.${source}}}/checkouts/cn/{{context.${cart_id}}}
```
{% endraw %}

{% endtab %}
{% tab Abandoned checkout %}

### Paiement abandonné {#abandoned-checkout}

Utilisez le modèle **Abandoned checkout** pour cibler les clients qui ont commencé le processus de paiement mais sont partis avant de passer leur commande.

![Un modèle Canvas « Abandoned Checkout » appliqué avec les « Entry Rules » développées.]({% image_buster /assets/img_archive/abandoned_checkout.png %})

#### Configuration

Sur la page Canvas, sélectionnez **Use a Canvas Template** > **Braze templates**, puis appliquez le modèle **Abandoned checkout**.

##### Paramètres par défaut

Les paramètres suivants sont préconfigurés dans votre Canvas :

- Bases
    - Nom du Canvas : **Abandoned checkout**
    - Événement de conversion : `ecommerce.order_placed`
        - Date limite de conversion : 3 jours
- Planification d'entrée
    - Déclencheur basé sur l'action lorsqu'un utilisateur effectue l'événement `ecommerce.checkout_started`
    - L'heure de début correspond au moment où vous créez le modèle Canvas<br><br>![« Action Based Options » pour le Canvas.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry.png %})
- Audience cible
    - Audience d'entrée
        - A utilisé ces applications **plus de 0** fois
        - L'e-mail **n'est pas vide**
    - Contrôles d'entrée
        - Les utilisateurs sont immédiatement rééligibles pour entrer dans le Canvas
        - Critères de sortie
            - Effectue les événements `ecommerce.order_placed`<br><br>![Contrôles d'entrée et critères de sortie pour le Canvas.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry_exit.png %})<br><br>
- Paramètres d'envoi
    - Utilisateurs abonnés ou ayant donné leur accord explicite (opt-in)
- Étape de délai
    - Délai de 4 heures
- Étape de message
    - Consultez le modèle d'e-mail et le bloc HTML avec un exemple de modèle Liquid pour ajouter des produits à votre message dans le modèle préconstruit. Si vous utilisez votre propre modèle d'e-mail, vous pouvez également vous référer aux [variables Liquid](#message-personalization), comme illustré dans la section suivante.

#### Personnalisation des e-mails de paiement abandonné {#abandoned-checkout-personalization-for-emails}

Les parcours de paiement abandonné nécessitent une étiquette Liquid spéciale `shopping_cart` pour la personnalisation des produits.

Voici un exemple montrant comment ajouter un bloc HTML avec votre étiquette Liquid `shopping_cart` pour intégrer des produits dans votre e-mail.

{% raw %}
```java
<table aria-label="Abandoned checkout personalization for emails" style="width:100%">
  {% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
    {% endfor %}
</table>
```
{% endraw %}

##### `abort_if_not_abandoned` {#abort-if-not-abandoned}

Le paramètre `abort_if_not_abandoned` est spécifique au cas d'usage du paiement abandonné et s'utilise uniquement avec l'étiquette Liquid `shopping_cart` en combinaison avec l'événement `ecommerce.checkout_started`.

| Valeur | Comportement |
| ----- | -------- |
| `true` (par défaut) | Le message est annulé si le panier n'a pas été abandonné, c'est-à-dire si l'utilisateur a depuis finalisé sa commande. |
| `false` | Le message est envoyé même si le panier n'est pas dans un état abandonné, ce qui permet à l'e-mail d'inclure les détails du panier quel que soit le statut actuel du paiement. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="abortifnotabandoned #abort-if-not-abandoned" }

Définissez `abort_if_not_abandoned` sur `false` lorsque vous souhaitez envoyer le rappel de paiement indépendamment du fait que le panier soit encore considéré comme abandonné au moment de l'envoi. Si vous omettez le paramètre ou le définissez sur `true`, Braze annule le message pour les utilisateurs ayant déjà finalisé leur achat.

##### URL de paiement {#checkout-url}

{% raw %}
```liquid
{{context.${metadata}.checkout_url}}
```
{% endraw %}

{% endtab %}
{% tab Order confirmation and feedback survey %}

### Confirmation de commande et enquête de satisfaction {#order-confirmation-and-feedback-survey}

Utilisez le modèle **Order confirmation & feedback survey** pour confirmer les commandes réussies et améliorer la satisfaction des clients.

![Un modèle Canvas « Order confirmation » appliqué avec les « Entry Rules » développées.]({% image_buster /assets/img_archive/order_confirmation_feedback.png %})

#### Configuration

Sur la page Canvas, sélectionnez **Use a Canvas Template** > **Braze templates**, puis appliquez le modèle **Order confirmation & feedback survey**.

##### Paramètres par défaut

Les paramètres suivants sont préconfigurés dans votre Canvas :

- Bases
    - Nom du Canvas : **Order confirmation with feedback survey**
    - Événement de conversion : `ecommerce.session_start`
        - Date limite de conversion : 10 jours
- Planification d'entrée
    - Déclencheur basé sur l'action lorsqu'un utilisateur effectue l'événement `ecommerce.cart_updated`
    - L'heure de début correspond au moment où vous créez le modèle Canvas<br><br>![« Action Based Options » pour le Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry.png %})<br><br>
- Audience cible
    - Audience d'entrée
        - A utilisé ces applications **plus de 0** fois
        - L'e-mail **n'est pas vide**
    - Contrôles d'entrée
        - Les utilisateurs sont immédiatement rééligibles pour entrer dans le Canvas
    - Critères de sortie
        - Sans objet<br><br>![Filtres supplémentaires et contrôles d'entrée pour le Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry_exit.png %})<br><br>
- Paramètres d'envoi
    - Utilisateurs abonnés ou ayant donné leur accord explicite (opt-in)
- Étape de message
    - Consultez le modèle d'e-mail et le bloc HTML avec un exemple de modèle Liquid pour ajouter des produits à votre message dans le modèle préconstruit. Si vous utilisez votre propre modèle d'e-mail, vous pouvez également vous référer aux [variables Liquid](#message-personalization), comme illustré dans la section suivante.

#### Personnalisation des e-mails de confirmation de commande {#order-confirmation-personalization-for-emails}

Voici un exemple montrant comment ajouter un bloc HTML de produit à votre confirmation de commande après qu'une commande a été passée.

{% raw %}
```json
<table aria-label="Order confirmation personalization for emails" style="width:100%">
  {% for item in {{context.${products}}} %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200" /></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{item.product_name}}</li>
        <li>Price: {{item.price}}</li>
        <li>Quantity: {{item.quantity}}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

##### URL du statut de la commande {#order-status-url}

{% raw %}
```liquid
{{context.${metadata}.order_status_url}}
```
{% endraw %}

{% endtab %}
{% endtabs %}