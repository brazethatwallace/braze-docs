---
nav_title: Mise à niveau de Shopify
article_title: "Mise à niveau de votre intégration Shopify"
description: "Découvrez comment mettre à niveau votre intégration Shopify pour Braze."
page_type: partner
search_tag: Partner
permalink: "/shopify_standard_upgrade/"
hidden: true
---

# Mise à niveau de votre intégration Shopify (standard) {#upgrading-your-shopify-integration-standard}

> Découvrez comment mettre à niveau votre intégration Shopify en utilisant le parcours standard pour Braze. Dans le cadre de notre engagement à vous offrir la meilleure expérience possible, nous exigeons que toutes les intégrations Shopify soient [mises à niveau]({{site.baseurl}}/shopify) vers la dernière version d'ici le 28 août 2025. Cette mise à niveau est essentielle car des changements significatifs dans la technologie de Shopify auront un impact sur le fonctionnement de notre intégration.

## Qui est éligible ? {#whos-eligible}

Ce parcours de mise à niveau est destiné aux marques disposant d'une boutique en ligne Shopify.

{% multi_lang_include partners/shopify_alerts.md alert='breaking' %}

## Conditions requises pour la mise à niveau {#upgrade-requirements}

Avant de commencer, vérifiez les points suivants :

- **Changements critiques :** Assurez-vous d'avoir examiné tous les changements importants entre l'ancien connecteur et le nouveau connecteur dans l'[aperçu de la mise à niveau Shopify]({{site.baseurl}}/shopify_upgrade_overview#subscriber-collection).
- **Prérequis de mise à niveau :** Assurez-vous d'avoir rempli tous les [prérequis de mise à niveau]({{site.baseurl}}/shopify_upgrade_overview#upgrade-prerequisites) nécessaires avec vos équipes d'ingénierie et de marketing.
- **Changements majeurs :** Examinez et corrigez tous les changements majeurs signalés dans Braze. Pour un guide complet, continuez vers [Corriger les changements majeurs](#fixing-breaking-changes-fixing-breaking-changes).

## Corriger les changements majeurs {#fixing-breaking-changes}

Dans Braze, accédez à **Intégrations partenaires** > **Shopify**, puis sélectionnez **Start upgrade**.

![Panneau avec une option pour démarrer la mise à niveau.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_upgrade.png %}){: style="max-width:35%;"}

Tous les Canvas, Campaigns et Segments impactés qui utilisent des données Shopify seront signalés.

![Fenêtre modale pour examiner ce qui est impacté par les changements majeurs.]({% image_buster /assets/unlisted_docs/img/shopify/review_breaking_changes.png %})

Pour la plupart des événements, nous recommandons d'inclure les nouveaux événements et attributs Shopify requis en utilisant un opérateur « OR » pour faciliter une mise à niveau fluide des messages actifs. Pour des cas plus spécifiques, consultez les informations suivantes :

{% tabs local %}
{% tab Panier abandonné %}
Pour les messages de panier abandonné, vous devrez utiliser les nouveaux modèles de Canvas de panier abandonné qui incluent :

{% multi_lang_include partners/shopify/abandoned_cart_template_features.md %}
{% endtab %}

{% tab Paiement abandonné %}
Pour les messages de paiement abandonné, vous devrez utiliser le nouveau modèle de Canvas de paiement abandonné qui inclut :

{% multi_lang_include partners/shopify/abandoned_checkout_template_features.md %}

Pour une liste complète des nouveaux modèles de Canvas eCommerce et des blocs HTML prédéfinis pour la personnalisation des produits disponibles via l'intégration, consultez [Créer vos parcours utilisateur Canvas]({{site.baseurl}}using_shopify_with_braze#create-your-canvas-user-journeys).

{% alert important %}
Si vous ne tenez pas compte des messages actifs qui utilisent des événements abandonnés dans l'intégration Shopify, les messages impactés ne seront plus envoyés à vos clients.
{% endalert %}

Pour en savoir plus, consultez [Événements Shopify pris en charge]({{site.baseurl}}/shopify_upgrade_overview#supported-shopify-events).
{% endtab %}

{% tab Listes d'abonnés %}
Si vous collectez des abonnés e-mail ou SMS depuis Shopify via l'intégration, confirmez que vos messages actifs incluent les listes d'abonnés correspondantes pour votre boutique Shopify.

Lorsque la mise à niveau sera terminée, de nouveaux groupes d'abonnement par défaut seront créés pour votre intégration, que vous devrez exploiter dans le cadre de vos messages actifs. Pour plus d'informations sur les changements, consultez [Collecte d'abonnés]({{site.baseurl}}/shopify_upgrade_overview#subscriber-collection).
{% endtab %}
{% endtabs %}

## Mise à niveau de Shopify {#upgrading-shopify}

{% alert important %}
Il est essentiel de [corriger tous les changements majeurs](#fixing-breaking-changes) avant de démarrer votre mise à niveau.
{% endalert %}

### Étape 1 : Démarrer la mise à niveau {#step-1-start-the-upgrade}

Dans Braze, accédez à **Intégrations partenaires** > **Shopify**, puis sélectionnez **Start upgrade**.

![Panneau avec une option pour démarrer la mise à niveau.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_upgrade.png %}){: style="max-width:35%;"}

Acceptez les conditions générales en cochant la case, puis sélectionnez **Start the upgrade**.

![Fenêtre modale pour confirmer que vous comprenez que la mise à niveau peut entraîner des changements majeurs.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_upgrade.png %})

### Étape 2 : Configurer les SDK Braze {#step-2-set-up-the-braze-sdks}

L'intégration standard ajoutera automatiquement les SDK Braze à votre site Shopify. Si vous avez déjà intégré les SDK Braze directement ou utilisé un outil tiers pour cela, coordonnez-vous avec vos développeurs pour supprimer le déploiement précédent du SDK lors de la mise à niveau.

![Fenêtre modale confirmant que la nouvelle intégration déploiera automatiquement le SDK Braze et JavaScript sur votre boutique.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_integration.png %}){: style="max-width:70%;"}

### Étape 3 : Réautoriser l'application Braze {#step-3-reauthorize-the-braze-app}

Pour réautoriser l'application Braze, sélectionnez **Go to Shopify**.

![Panneau de mise à niveau Shopify avec un bouton pour accéder à Shopify afin de réautoriser l'application Braze.]({% image_buster /assets/unlisted_docs/img/shopify/reauthorize_braze_app.png %}){: style="max-width:35%;"}

Sur le site Shopify, suivez les instructions pour réautoriser votre application Braze. Cela permet à Braze d'accéder à vos données Shopify.

{% alert note %}
Le processus de réautorisation peut prendre quelques minutes, mais il se mettra automatiquement à jour sur votre page Shopify une fois terminé.
{% endalert %}

![La page « Integration Settings » affichant l'état des événements Shopify.]({% image_buster /assets/unlisted_docs/img/shopify/reauthorization_status.png %})

### Étape 4 : Choisir un type d'ID externe {#step-4-choose-an-external-id-type}

Le type d'ID externe que vous choisissez sera attribué aux nouveaux profils clients Shopify lorsqu'un compte Shopify est créé ou qu'une commande est passée. Il sera également utilisé pour mettre à jour les profils utilisateur existants s'ils possèdent déjà un alias d'ID client Shopify mais n'ont pas d'ID externe attribué dans Braze.

Pour choisir votre type d'ID externe, retournez dans Braze puis sélectionnez **Confirm external ID**.

![Panneau de mise à niveau Shopify avec un bouton pour confirmer l'ID externe.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_external_id.png %}){: style="max-width:35%;"}

Choisissez l'ID externe que vous souhaitez utiliser pour l'intégration Shopify de votre espace de travail. Lorsque vous avez terminé, sélectionnez **Set external ID**.

![Fenêtre modale avec un menu déroulant pour sélectionner l'ID externe.]({% image_buster /assets/unlisted_docs/img/shopify/external_id_field.png %}){: style="max-width:70%;"}

{% alert important %}
L'utilisation d'une adresse e-mail ou d'une adresse e-mail hachée comme ID externe Braze peut aider à simplifier la gestion des identités à travers vos sources de données. Cependant, il est important de considérer les risques potentiels pour la confidentialité des utilisateurs et la sécurité des données.<br><br>

- **Informations devinables :** Les adresses e-mail sont facilement devinables, ce qui les rend vulnérables aux attaques.
- **Risque d'exploitation :** Si un utilisateur malveillant modifie son navigateur web pour envoyer l'adresse e-mail de quelqu'un d'autre comme ID externe, il pourrait potentiellement accéder à des messages sensibles ou à des informations de compte.
{% endalert %}

Par défaut, Braze convertit automatiquement les e-mails provenant de Shopify en minuscules avant de les utiliser comme ID externe. Si vous utilisez un e-mail ou un e-mail haché comme ID externe, confirmez que vos adresses e-mail sont également converties en minuscules avant de les attribuer comme ID externe ou avant de les hacher à partir d'autres sources de données. Cela permet d'éviter les divergences dans les ID externes et la création de profils utilisateur en double dans Braze.

Si vous avez sélectionné un type d'ID externe personnalisé, passez aux étapes 4.1 à 4.3. Sinon, continuez à l'étape 5.

#### Étape 4.1 : Créer le métachamp `braze.external_id` {#step-41-create-the-brazeexternal_id-metafield}

{% multi_lang_include partners/shopify/customer_metafield_definition_steps.md %}

Une fois le métachamp créé, renseignez-le pour vos clients. Nous recommandons les approches suivantes :

- **Écouter les webhooks de création de clients :** Configurez un webhook pour écouter les [événements `customer/create`](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks). Cela vous permet d'écrire le métachamp lorsqu'un nouveau client est créé.
- **Remplir rétroactivement les clients existants :** Utilisez l'[API Admin](https://shopify.dev/docs/api/admin-graphql) ou l'[API Customer](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) pour remplir rétroactivement le métachamp pour les clients précédemment créés.

#### Étape 4.2 : Créer un endpoint pour récupérer votre ID externe {#step-42-create-an-endpoint-to-retrieve-your-external-id}

Vous devez créer un endpoint public que Braze peut appeler pour récupérer l'ID externe. Cela est nécessaire pour les scénarios où Shopify ne peut pas fournir le métachamp `braze.external_id`.

##### Spécifications de l'endpoint {#endpoint-specifications}

**Méthode :** `GET`

| Paramètres | Description |
| --- | --- |
| `shopify_customer_id` | L'ID client Shopify. |
| `email_address` | L'adresse e-mail de l'utilisateur connecté. |
| `shopify_storefront` | La vitrine pour la requête. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### Exemple d'endpoint {#example-endpoint}

```
GET
https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@example.com&shopify_storefront=dev-store.myshopify.com
```

##### Réponse attendue {#expected-response}

Braze attend un code de statut `200`. Tout autre code est considéré comme un échec.

{% raw %}
```json
{
    "external_id": "my_external_id"
}
```
{% endraw %}

{% alert important %}
Il est important de valider que le `shopify_customer_id` et l'`email_address` correspondent aux valeurs du client dans Shopify. Vous pouvez utiliser l'[API Admin](https://shopify.dev/docs/api/admin-graphql) ou l'[API Customer](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) pour valider ces paramètres et récupérer le métachamp `braze.external_id`.
{% endalert %}

#### Étape 4.3 : Saisir votre ID externe {#step-43-input-your-external-id}

Répétez l'[étape 4](#step-4-choose-an-external-id-type) et saisissez l'URL de votre endpoint après avoir sélectionné l'ID externe personnalisé comme type d'ID externe Braze.

##### Considérations {#considerations}

{% multi_lang_include partners/shopify/external_id_generation_notes.md %}

### Étape 5 : Activer l'intégration de l'application Braze {#step-5-enable-the-braze-app-embed}

Pour activer l'intégration de l'application Braze dans le thème de votre boutique, retournez dans Braze puis sélectionnez **Go to Shopify**.

![Panneau de mise à niveau Shopify avec un bouton pour activer l'intégration de l'application Braze.]({% image_buster /assets/unlisted_docs/img/shopify/enable_app_embed.png %}){: style="max-width:35%;"}

Sur le site Shopify, activez l'intégration de l'application Braze, puis enregistrez vos modifications.

![Exemple d'intégration d'application.]({% image_buster /assets/unlisted_docs/img/shopify/app_embed.png %})

### Étape 6 : Vérifier la mise à niveau {#step-6-verify-the-upgrade}

De retour dans Braze, vous serez alerté lorsque l'installation de votre intégration Shopify sera terminée.

![Page d'intégration Shopify avec une bannière de succès.]({% image_buster /assets/unlisted_docs/img/shopify/success_integration.png %})

Pour vérifier que votre nouveau connecteur Shopify est en production, testez les éléments suivants :

{% multi_lang_include partners/shopify/upgrade_validation_checklist.md %}

Si vous avez des questions, [contactez l'assistance]({{site.baseurl}}/user_guide/administrative/access_braze/support).