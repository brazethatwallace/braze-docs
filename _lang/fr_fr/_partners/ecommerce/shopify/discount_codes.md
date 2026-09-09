---
nav_title: Codes de réduction uniques
article_title: Envoyer des codes de réduction uniques
alias: /shopify_discount_codes/
page_order: 7
description: "Cet article de référence couvre un cas d'usage soumis par la communauté qui consiste à utiliser les codes de promotion Braze avec le Shopify Bulk Discount Code Bot pour envoyer des codes de réduction uniques par le biais de vos Campaigns et Canvas."
---

# Envoyer des codes de réduction uniques via Shopify {#send-unique-discount-codes-through-shopify}

> Ce cas d'usage soumis par la communauté montre comment utiliser les [codes de promotion]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes) Braze avec le Shopify Bulk Discount Code Bot pour générer des codes de réduction uniques pour vos Campaigns et Canvas. Des codes de réduction uniques permettent d'éviter l'exploitation de codes de promotion génériques.

{% alert important %}
Il s'agit d'une intégration proposée par la communauté et qui n'est pas directement prise en charge par Braze. Le Bulk Discount Code Bot est directement pris en charge par Shopify. Seuls les codes de promotion Braze sont pris en charge par Braze.
{% endalert %}

## Conditions requises {#requirements}

| Condition | Description |
| --- | --- |
| Configurer une boutique Shopify | Confirmez que vous avez déjà [configuré une boutique Shopify avec Braze]({{site.baseurl}}/shopify_overview). |
| Installer l'application Bulk Discount Code Bot | Téléchargez l'application [Bulk Discount Code Bot](https://apps.shopify.com/bulk-discount-generator) dans la boutique d'applications Shopify. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions requises" }

## Générer des codes de réduction uniques {#generating-unique-discount-codes}

### Étape 1 : Configurer vos codes de réduction {#step-1-configure-your-discount-codes}

Utilisez le Bulk Discount Code Bot pour configurer vos codes de réduction en fonction du nombre de codes à générer, de la longueur du code, de la valeur de la réduction, et plus encore.

![Les options de configuration pour un ensemble de réductions.][1]{: width="1203" height="677" style="max-width:100%;"}

### Étape 2 : Exporter vos codes {#step-2-export-your-codes}

Recherchez votre ensemble de réductions dans la barre de recherche du Bulk Discount Code Bot, puis sélectionnez **Export Codes** > **Download Codes** pour télécharger un fichier CSV dans votre dossier Téléchargements.

![Barre de recherche avec un menu déroulant affichant l'ensemble de réductions et une rangée de boutons à sélectionner.][2]{: width="1163" height="858" style="max-width:70%;"}

Dans le fichier CSV, supprimez la ligne 1 pour retirer l'en-tête de colonne « Promo ». Cela empêche « Promo » de devenir un code de réduction dans Braze.

![Un diagramme montrant la suppression de l'en-tête de ligne « Promo » dans un fichier CSV.][3]{: width="448" height="222" style="max-width:60%;"}

### Étape 3 : Ajouter vos codes de réduction à Braze {#step-3-add-your-discount-codes-to-braze}

Dans Braze, accédez à **Data Settings** > **Promotion Codes** > **Create Promotion Code List** et [configurez votre liste de codes de réduction]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create#create). Assurez-vous de faire correspondre la date d'expiration configurée par le Bulk Discounts Code Bot.

Ensuite, téléchargez votre fichier CSV et sélectionnez **Save List**.

### Étape 4 : Ajouter vos codes de réduction à une campagne Braze ou une étape Canvas {#step-4-add-your-discount-codes-to-a-braze-campaign-or-canvas-step}

Si vous souhaitez utiliser vos codes de réduction uniques dans une Campaign à envoi unique, ou si cela ne vous dérange pas que les utilisateurs reçoivent plusieurs codes uniques à travers différentes Campaigns ou étapes Canvas, copiez l'extrait de code Liquid depuis la liste de codes de promotion que vous avez enregistrée.

![Un extrait de code Liquid avec un bouton pour le copier.][4]{: width="958" height="295" style="max-width:60%;"}

Collez l'extrait de code Liquid dans une Campaign ou une étape Canvas.

<video autoplay muted loop playsinline loading="lazy" width="800" height="540" style="max-width:100%;height:auto;aspect-ratio:800/540;" aria-label="Une vidéo montrant l'ajout de l'extrait de code Liquid à une étape Canvas.">
  <source src="{% image_buster /assets/img/shopify/liquid_promo_code.mp4 %}" type="video/mp4">
</video>

Si vous souhaitez que les utilisateurs reçoivent un seul code de réduction unique, quel que soit le nombre de fois où le code de réduction est référencé dans des Campaigns ou des Canvas, créez une étape [User Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) directement avant la première étape Message qui attribue le code de réduction à un attribut personnalisé, comme « Promo Code ».

{% alert tip %}
Vous pouvez également [créer un attribut personnalisé]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) en accédant à **Data Settings** > **Custom Attributes**.
{% endalert %}

Dans l'étape User Update, procédez comme suit pour chaque champ :
- **Attribute Name :** Sélectionnez **Promo Code**.
- **Action :** Sélectionnez **Update**.
- **Key Value :** Collez l'extrait de code Liquid.

![Une étape User Update qui met à jour un attribut « Promo Code » avec l'extrait de code Liquid.][6]{: width="2464" height="1322" style="max-width:100%;"}

Vous pouvez maintenant ajouter l'attribut personnalisé {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %} à n'importe quel message, et le code de réduction sera automatiquement intégré.

## Comportement des codes de réduction {#discount-code-behavior}

{% details Campaign multicanal ou étape Canvas %}

Lorsqu'un extrait de code de réduction est utilisé dans une Campaign multicanal ou une étape Canvas, les utilisateurs reçoivent toujours un code unique. Si un utilisateur est éligible pour recevoir un code via plusieurs canaux, il recevra le même code sur chaque canal. Autrement dit, un utilisateur éligible ne recevra qu'un seul code pour l'ensemble des messages envoyés par cette Campaign ou cette étape Canvas.

{% enddetails %}

{% details Différentes étapes Canvas ou Campaigns distinctes %}

Lorsqu'un code de réduction est référencé par plusieurs étapes dans le même Canvas ou par des Campaigns distinctes, un utilisateur éligible recevra plusieurs codes de promotion uniques (un code pour chaque étape Canvas ou Campaign).

{% enddetails %}

[1]: {% image_buster /assets/img/shopify/configure_discount_codes.png %}
[2]: {% image_buster /assets/img/shopify/export_discount_codes.png %}
[3]: {% image_buster /assets/img/shopify/edited_codes_csv.png %}
[4]: {% image_buster /assets/img/shopify/liquid_code_snippet.png %}
[6]: {% image_buster /assets/img/shopify/user_update_step.png %}