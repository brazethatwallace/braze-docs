---
nav_title: Aperçu de la mise à niveau Shopify
article_title: Aperçu de la mise à niveau Shopify
description: "Cet article de référence décrit comment mettre à niveau votre intégration Shopify vers la dernière version."
page_type: partner
search_tag: Partner
permalink: "/shopify_upgrade_overview/"
hidden: true
---

# Aperçu de la mise à niveau Shopify {#shopify-upgrade-overview}

> Dans le cadre de notre engagement à vous offrir la meilleure expérience possible, nous exigeons que toutes les intégrations Shopify soient [mises à niveau]({{site.baseurl}}/shopify/) vers la dernière version d'ici le 28 août 2025. Cette mise à niveau est essentielle car des changements importants dans la technologie de Shopify auront un impact sur le fonctionnement de notre intégration.

## Dates clés {#key-dates}

- **De fin février à avril :** Vous recevrez des notifications indiquant quand votre groupe spécifique (cohorte) sera prêt pour la mise à niveau. Restez attentif à ces informations importantes.
- **Date limite de mise à niveau :** Tous les clients doivent terminer la mise à niveau avant le **28 août 2025**.

{% multi_lang_include shopify_alerts.md alert='breaking' %}

## Qu'est-ce qui change dans l'intégration Shopify ? {#whats-changing-in-the-shopify-integration}

Dans le cadre des plans de Shopify pour améliorer l'extensibilité du paiement, des changements importants sont à venir pour son intégration avec Braze. Voici ce que vous devez savoir :

- **Abandon des Script Tags et de `checkout.liquid` :** Shopify supprime progressivement les Script Tags et `checkout.liquid`. Après août 2025, le SDK Web de Braze ne se chargera plus sur les pages de paiement via les Script Tags, sauf si vous migrez vers la dernière version de l'intégration.
- **Améliorations générales de l'intégration :**
    - **Introduction d'événements recommandés :** Nous ajoutons des événements eCommerce recommandés à l'intégration, ce qui simplifie les cas d'utilisation eCommerce courants grâce à des modèles prédéfinis dans Braze.
    - **Gestion simplifiée des identités :** Nous améliorons notre approche de la gestion des identités utilisateur, ce qui améliorera le suivi et l'attribution des données d'utilisateurs anonymes. Pour plus d'informations sur le traitement de la gestion des identités, consultez [Synchronisation des utilisateurs et des données]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview/#user-and-data-syncing).
    - **Listes d'abonnés e-mail et SMS :** Si vous collectez actuellement des abonnés e-mail et SMS, des groupes d'abonnement par défaut pour chaque canal seront automatiquement créés dans le cadre de la mise à niveau. Lorsque Braze synchronise les opt-ins e-mail et SMS, Braze ne remplacera plus l'état d'abonnement global sur le profil utilisateur et mettra simplement à jour l'opt-in du groupe d'abonnement.
    - Pour tous les détails sur les changements entre la version actuelle et la nouvelle version, consultez le [journal des modifications](#full-changelog).

{% alert important %}
Cette mise à niveau est essentielle pour maintenir le bon fonctionnement de votre intégration entre Shopify et Braze. Nous vous recommandons de collaborer étroitement avec votre équipe de développement pour évaluer la portée et les implications de ces changements et faciliter une transition fluide.
{% endalert %}

## Prérequis de mise à niveau {#upgrade-requirements}

Avant de commencer le processus de mise à niveau sur la page d'intégration Shopify, remplissez les prérequis suivants avec votre équipe technique :

- **Vérifiez les personnalisations du SDK :** Si vous avez personnalisé votre intégration Braze et Shopify (par exemple, en enregistrant des événements personnalisés ou des attributs), assurez-vous que ces personnalisations fonctionneront correctement après la mise à niveau. Si vous avez créé vos propres événements de navigateur pour des actions comme « produit consulté » ou « panier mis à jour », coordonnez-vous avec vos développeurs pour les supprimer avant la mise à niveau, car ils dupliqueront les fonctionnalités fournies par le nouveau connecteur.

{% alert important %}
Si vous utilisez une boutique en ligne Shopify et que vos développeurs ont implémenté les SDK Braze directement sur votre site Shopify, ou via Google Tag Manager ou une plateforme de données client, vous devez prévoir d'arrêter de les utiliser lors de la mise à niveau vers le nouveau connecteur Shopify.
{% endalert %}

- **Vérifiez la gestion des identités :** Si vous utilisez un ID externe Braze, travaillez avec votre équipe de développement pour vous assurer qu'il est compatible avec la nouvelle intégration. Si vous définissez l'ID externe dans votre expérience de boutique Shopify, demandez à vos développeurs de l'ajuster pour éviter les conflits avec le [nouveau processus de gestion des identités]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_overview/#user-and-data-syncing).
- **Préparez les campagnes, Canvas et Segments impactés :** Pendant le processus de mise à niveau guidé, vous pouvez consulter et exporter toutes les campagnes, tous les Canvas et tous les Segments qui dépendent des données Shopify. Nous vous recommandons d'ajouter les nouveaux événements et attributs Shopify requis en utilisant un opérateur « OU » pour faciliter une mise à niveau fluide de vos messages actifs.
- **Créez des parcours utilisateur de panier et de paiement abandonnés :** Le parcours utilisateur de panier abandonné doit désormais utiliser le déclencheur « Performed Cart Updated » dans les critères d'entrée de votre Canvas. De plus, vous devez utiliser la nouvelle étiquette Liquid de panier d'achat pour les parcours utilisateur de panier abandonné et de paiement abandonné. Vous pouvez utiliser nos nouveaux [modèles de Canvas]({{site.baseurl}}/using_shopify_with_braze/#create-your-canvas-user-journeys) pour vous aider à démarrer.

Compléter ces étapes facilitera une mise à niveau réussie vers la dernière version de l'intégration Shopify.

## Options d'intégration {#integration-options}

Braze propose deux options d'intégration pour les marchands Shopify, conçues pour répondre aux besoins variés des entreprises eCommerce : **intégration standard** et **intégration personnalisée**.

{% tabs local %}
{% tab Standard %}
L'intégration standard est conçue pour les boutiques en ligne Shopify, offrant un processus de configuration fluide et simple. Cette option vous permet de connecter rapidement votre boutique Shopify à Braze, vous donnant accès à de puissants outils d'engagement client sans expertise technique approfondie. Avec cette option d'intégration, vous pouvez synchroniser les données client, automatiser l'envoi de messages personnalisés et améliorer vos efforts marketing grâce aux fonctionnalités complètes de Braze.

Pour mettre à niveau votre intégration Shopify existante via le parcours de mise à niveau standard, consultez [Mise à niveau de votre intégration Shopify (standard)]({{site.baseurl}}/shopify_standard_upgrade/).
{% endtab %}

{% tab Personnalisée %}
L'intégration personnalisée offre une solution plus flexible et composable si vous utilisez Shopify Hydrogen ou si vous gérez une boutique headless. Cette option vous permet d'implémenter les SDK Braze directement dans votre environnement Shopify, permettant une intégration plus profonde et des fonctionnalités sur mesure. Que vous cherchiez à créer des expériences client uniques ou à optimiser des workflows spécifiques, l'intégration personnalisée fournit les outils nécessaires pour exploiter pleinement les capacités de Braze dans une configuration headless.

Pour mettre à niveau votre intégration Shopify existante via le parcours de mise à niveau personnalisé, consultez [Mise à niveau de votre intégration Shopify (personnalisée)]({{site.baseurl}}/shopify_custom_upgrade/).
{% endtab %}
{% endtabs %}

## Journal des modifications {#changelog}

{% alert important %}
Cette intégration utilise Shopify comme source de vérité pour les attributs et événements pris en charge. Par conséquent, Shopify peut remplacer des valeurs préexistantes, comme des attributs standard ou personnalisés, sur un profil utilisateur lors de la synchronisation des données.
{% endalert %}

### Intégration standard {#standard-integration}

| Version précédente | Dernière version |
| --- | --- |
| {::nomarkdown}<ul><li>Script Tag support</li><li>Braze Web SDK only</li><li>Shopify webhooks for events and products</li></ul>{:/} | {::nomarkdown}<ul><li>Web Pixel API support</li><li>New Braze app embed</li><li>Braze Web SDK & JavaScript SDK</li><li>Shopify webhooks for events and products</ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Intégration standard" }

### Identifiants utilisateur pris en charge par l'intégration {#user-identifiers-supported-by-the-integration}

| Identifiants utilisateur | Version précédente | Dernière version |
| --- | --- | --- |
| ID d'appareil Braze |  {::nomarkdown}<ul><li>A randomly generated ID that is stored on the browser</li></ul>{:/} | {::nomarkdown} <ul><li>A randomly generated ID that is stored on the browser</li></ul>{:/}|
| Alias Braze | {::nomarkdown}<ul><li>Shopify customer ID</li><li>Shopify email</li></ul>{:/} | {::nomarkdown}<ul><li>Shopify cart token</li><li>Shopify checkout token</li></ul>{:/}|
| ID externe Braze | {::nomarkdown}<ul><li>N/A</li></ul>{:/}| {::nomarkdown}<ul><li>Shopify customer ID</li><li>Email</li><li>Hashed email (SHA-256, SHA-1, MD5)</li><li>Custom external ID</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Identifiants utilisateur pris en charge par l'intégration" }

Pour plus de détails sur la synchronisation des utilisateurs et la gestion des ID, consultez [Données utilisateur et synchronisation]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_overview/#user-and-data-syncing).

{% alert note %}
Par défaut, Braze convertit automatiquement les e-mails provenant de Shopify en minuscules avant de les utiliser comme ID externe. Si vous utilisez l'e-mail ou l'e-mail haché comme ID externe, confirmez que vos adresses e-mail sont également converties en minuscules avant de les attribuer comme ID externe ou avant de les hacher à partir d'autres sources de données. Cela permettra d'éviter les divergences d'ID externes et la création de profils utilisateur en double dans Braze.
{% endalert %}

### Événements Shopify pris en charge {#supported-shopify-events}

| Événements ou attributs | Version précédente | Dernière version |
| --- | --- | --- |
| Événements |  {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=product%20viewed">shopify_product_viewed</a></li></ul>{:/} | {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=product%20viewed">ecommerce.product_viewed</a></li><li>Added <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#abandoned-browse">abandoned browse Canvas template</a></li></ul>{:/} |
| Événements |  {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?tab=example%20payload">shopify_product_clicked</a></li></ul>{:/} | {::nomarkdown}<ul><li>Deprecated event</li></ul>{:/} |
| Événements | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=abandoned%20cart&tab=example%20payload">shopify_abandoned_cart</a></li><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/setting_up_shopify/#advanced-settings-optional">Abandoned cart timer setting</a></li></ul>{:/} | {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=cart%20updated">ecommerce.cart_updated</a></li><li>Deprecated abandoned cart timer setting</li><li>Added <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#abandoned-cart">abandoned cart Canvas template</a></li></ul>{:/} |
| Événements | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=abandoned%20checkout&tab=example%20payload">shopify_abandoned_checkout</a></li><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/setting_up_shopify/#advanced-settings-optional">Abandoned cart timer setting</a></li></ul>{:/}| {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=checkout%20started">ecommerce.checkout_started</a></li><li>Deprecated abandoned checkout timer setting</li><li>Added <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#abandoned-checkout">abandoned checkout Canvas template</a></li></ul>{:/}|
| Événements | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=created%20order&tab=example%20payload">shopify_created_order</a></li></ul>{:/} | {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20placed">ecommerce.order_placed</a></li><li>Added <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#order-confirmation-and-feedback-survey">order confirmation & post-purchase survey Canvas template</a></li></ul>{:/}|
| Événements | {::nomarkdown}<ul><li><a href="https://braze.com/unlisted_docs/using_shopify_with_braze/?tab=order%20confirmation">Braze purchase event</a></li></ul>{:/}| {::nomarkdown}<ul><li>Deprecated event. Use <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20placed">ecommerce.order_placed</a>.</li></ul>{:/}|
| Événements | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=paid%20order&tab=example%20payload">shopify_paid_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Événements | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=partially%20fulfilled%20order&tab=example%20payload">shopify_partially_fulfilled_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Événements | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=fulfilled%20order&tab=example%20payload">shopify_fulfilled_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Événements | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=cancelled%20order&tab=example%20payload">shopify_cancelled_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20cancelled">ecommerce.order_cancelled</a></li></ul>{:/}|
| Événements | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=created%20refund&tab=example%20payload">shopify_created_refund</a></li></ul>{:/}| {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20refunded">ecommerce.order_refunded</a></li></ul>{:/}|
| Événements | {::nomarkdown}<ul><li>No Shopify account login event</li></ul>{:/}| {::nomarkdown}<ul><li>Added <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=account%20login#tracked-shopify-events">shopify_account_login</a></li></ul>{:/}|
| Attributs | {::nomarkdown}<ul><li>shopify_total_spent</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Attributs | {::nomarkdown}<ul><li>shopify_order_count</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Attributs | {::nomarkdown}<ul><li>shopify_last_order_id</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Attributs | {::nomarkdown}<ul><li>shopify_last_order_name</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Attributs | {::nomarkdown}<ul><li>shopify_zipcode</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Attributs | {::nomarkdown}<ul><li>shopify_province</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Événements Shopify pris en charge" }

### Collecte d'abonnés {#subscriber-collection}

| Type de collecte | Version précédente | Dernière version |
| --- | --- | --- |
| Collecte d'abonnés e-mail |  {::nomarkdown}<ul><li>Override for global email subscription state</li><li>Ability to assign one or more subscription groups</li><li>No default subscription group for the integration for the connected Shopify store</li></ul>{:/} | {::nomarkdown}<ul><li>Deprecated override functionality</li><li>A default subscription group will be created as part of the upgrade</li><li>Ability to assign additional subscription groups</li></ul>{:/} |
| Collecte d'abonnés SMS |  {::nomarkdown}<ul><li>Required to assign one or more subscription groups</li><li>No default subscription group for the integration for the connected Shopify store</li></ul>{:/} | {::nomarkdown}<ul><li>A default subscription group will be created as part of the upgrade</li><li>Ability to assign additional subscription groups</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Collecte d'abonnés" }

{% alert note %}
Si vous collectez actuellement des abonnés e-mail ou SMS, un nouveau groupe d'abonnement par défaut sera créé une fois la mise à niveau terminée. Le groupe d'abonnement par défaut portera le nom de votre vitrine Shopify. Ce processus peut prendre jusqu'à 5 heures. <br><br>Une fois les groupes d'abonnement disponibles, assurez-vous de les inclure dans vos campagnes, Segments ou Canvas actifs pour atteindre efficacement vos acheteurs abonnés.
{% endalert %}

### Synchronisation des produits {#product-sync}

| Type de synchronisation | Version précédente | Dernière version |
| --- | --- | --- |
| Synchronisation initiale des produits | {::nomarkdown}<ul><li>If product syncing is enabled, initial import of all products in your storefront</li><li>Ability to only import active products</li></ul>{:/} | {::nomarkdown}<ul><li>No&nbsp;changes</li></ul>{:/} |
| Synchronisation des produits en temps réel | {::nomarkdown}<ul><li>Real-time syncs when products are created, updated, or deleted from your store</li></ul>{:/} | {::nomarkdown}<ul><li>No&nbsp;changes</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Synchronisation des produits" }

### Canaux {#channels}

| Canal | Version précédente | Dernière version |
| --- | --- | --- |
| In-App Messages |  {::nomarkdown}<ul><li>Included within standard integrations for Shopify online stores</li></ul>{:/} | {::nomarkdown}<ul><li>No changes</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Canaux" }