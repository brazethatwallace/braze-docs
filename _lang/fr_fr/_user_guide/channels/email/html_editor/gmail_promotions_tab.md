---
nav_title: "Onglet Promotions de Gmail"
article_title: "Onglet Promotions de Gmail"
page_order: 8
description: "Cet article de référence explique comment utiliser Braze pour créer la carte de promotions mobiles Gmail à partir de votre campagne par e-mail."
channel:
  - email
toc_headers: h2
---

# Onglet Promotions de Gmail {#gmail-promotions-tab}

> L'[onglet Promotions de Gmail mobile](https://developers.google.com/gmail/promotab/) permet aux marketeurs d'envoyer davantage d'informations via des annotations dans une « carte » plutôt que de se limiter à la ligne d'objet ou à l'accroche. Braze dispose d'un outil intégré pour vous aider à créer la carte à partir de votre campagne par e-mail.

## Conditions préalables {#prerequisites}

Tout d'abord, transférez vos domaines et sous-domaines à l'équipe en charge de l'onglet Promotions de Google, à l'adresse <a href="mailto:p-promo-outreach@google.com">p-promo-outreach@google.com</a>, pour être ajouté à la liste d'autorisation de Gmail. Cela vous permet d'utiliser toute fonctionnalité affichant des images riches, comme le carrousel de produits pour l'onglet Promotions de Gmail.

## Créer la carte avec Braze {#build-the-card-with-braze}

Suivez ces étapes pour créer une carte de promotion Gmail pour une campagne par e-mail. Notez que quitter la section **Content** dans l'éditeur réinitialisera les champs et les informations de l'onglet **Gmail Promotion**. Finalisez la configuration de votre carte de promotion et copiez le code HTML généré afin de ne pas perdre votre code HTML.

### Étape 1 : Créer une campagne par e-mail {#step-1-create-an-email-campaign}

Commencez par [créer votre campagne par e-mail]({{site.baseurl}}/user_guide/channels/email/html_editor/), puis sélectionnez l'**éditeur de code HTML** comme expérience d'édition.

### Étape 2 : Ajouter les détails à la carte Gmail Promotion {#step-2-add-details-to-gmail-promotion-card}

Ensuite, accédez à la section **Content** de l'éditeur HTML et sélectionnez l'onglet **Gmail Promotion**. Remplissez les champs sous **Basic Information**, puis sélectionnez **Generate HTML Code**. Cela générera le script pour votre carte de l'onglet Gmail Promo dans la section **Copy and Paste HTML code into `<Head>`**.

![Exemple de création d'une carte.]({% image_buster /assets/img/create-gmail-promo.png %})

### Étape 3 : Personnaliser votre carte Gmail Promotion {#step-3-customize-your-gmail-promotion-card}

Choisissez d'inclure une offre de réduction, une carte d'offre, une carte de promotion, ou toutes ces options pour votre carte Gmail Promotion.

{% tabs %}
{% tab Offre de réduction %}

La configuration d'une offre de réduction vous permet de spécifier les dates de validité d'une remise.

1. Activez le basculeur **Discount Offer**.
2. Pour **Offer**, saisissez un court résumé de la réduction. Par exemple : « 20% off ».
3. Pour **Code**, ajoutez le code de promotion qu'un utilisateur doit appliquer lors du paiement.
4. Ensuite, sélectionnez la date et l'heure de début de l'offre de réduction.
5. Déterminez si l'offre de réduction doit se terminer à un moment précis ou ne jamais expirer.

![Options pour spécifier la valeur de l'offre, le code, ainsi que la date et l'heure de début d'une offre de réduction.]({% image_buster /assets/img/gmail_promo_discount_details.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Cartes d'offre %}

Utilisez les cartes d'offre pour fournir les informations clés d'une offre directement en haut du corps de l'e-mail. Cela permet aux destinataires de comprendre rapidement les détails de l'offre et de passer à l'action. Par exemple, vous pouvez utiliser les cartes d'offre pour promouvoir des offres à durée limitée et éviter aux utilisateurs de chercher les détails dans l'e-mail.

1. Activez le basculeur **Deal Card**.
2. Pour **Offer**, saisissez un court résumé de la réduction. Par exemple : « 20% off all shoes ».
3. (facultatif) Pour **Code**, ajoutez le code de promotion qu'un utilisateur doit appliquer lors du paiement.
4. Saisissez au moins l'une des URL suivantes.
-  **Offer Page URL :** L'URL de la page d'atterrissage spécifique à l'offre. Cela crée un bouton « Shop now » (ou similaire). Nous recommandons de fournir cette URL pour votre carte d'offre.
- **Merchant Homepage URL :** L'URL de votre page d'accueil principale. Utilisez ce champ uniquement si une URL de page d'offre spécifique n'est pas disponible.
5. (facultatif) Ajoutez une date de début pour l'offre.
6. Déterminez si l'offre doit se terminer à un moment précis ou ne jamais expirer.

![Options pour spécifier la valeur de l'offre, le code, ainsi que la date et l'heure de début d'une carte d'offre.]({% image_buster /assets/img/gmail_promo_deal_cards.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Cartes de promotion %}

Les cartes de promotion dans votre carrousel de produits sont utiles pour ajouter des images à votre offre. Vous pouvez également personnaliser les variables de votre carrousel de produits et inclure jusqu'à dix aperçus d'images, chaque image étant unique.

1. Activez le basculeur **Promotion Cards**.
2. Sélectionnez **Add promotion card**. Chaque image de votre carrousel de produits doit avoir une URL unique et utiliser le même rapport hauteur/largeur (4:5, 1:1, 1.91:1).
3. Incluez une URL d'image.
4. Pour **Target URL**, ajoutez le lien de votre promotion.

{% alert tip %}
Nous recommandons de télécharger vos images de produits dans la bibliothèque multimédia, puis de copier-coller les URL dans les champs appropriés. Seuls les formats d'image statiques (PNG et JPEG) sont acceptés. Certains formats d'image (GIF) seront téléchargés mais ne s'afficheront pas comme prévu.
{% endalert %}

{: start="5"}
5. Personnalisez votre carte de promotion en ajoutant un titre, une devise, un prix et une valeur de réduction.

| Propriété personnalisable | Description |
|---|---|
| Titre | (facultatif) Description d'une ou deux phrases pour la promotion. S'affiche sous l'image d'aperçu. |
| Devise | (facultatif) La devise du prix. |
| Prix | Le prix de la promotion. |
| Valeur de la réduction | Le montant déduit du prix d'origine. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Exemple de carrousel de produits d'une entreprise nommée Motto avec l'objet de l'e-mail « Nos chaussettes les plus vendues sont en promotion », avec trois images de chaussettes et leurs prix réduits.]({% image_buster /assets/img_archive/product_carousel.png %}){: style="max-width:40%;"}

{% endtab %}
{% endtabs %}

### Étape 4 : Générer et coller le code HTML {#step-4-generate-and-paste-html-code}

Après avoir créé votre carte Gmail Promotion, sélectionnez **Generate HTML Code**. Copiez et collez le script dans l'élément `<head>` du code HTML de votre e-mail.

{% alert tip %}
Pour l'éditeur par glisser-déposer, copiez et collez le code HTML généré dans la section des [balises head personnalisées]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/#custom-head-tags) sous **Sending Settings**.
{% endalert %}

{% alert warning %}
Le script Promotions n'apparaît que si votre e-mail arrive dans l'onglet Promotions de Gmail. Actuellement, Gmail utilise des algorithmes pour déterminer où votre e-mail sera classé. Cependant, si un utilisateur marque un jour votre e-mail comme promotion, l'algorithme de Gmail sera ignoré et votre e-mail arrivera automatiquement dans l'onglet Promotions par la suite.
{% endalert %}

### Étape 5 : Tester avec l'outil de prévisualisation de Gmail {#step-5-test-using-gmails-preview-tool}

Pour tester les annotations lors d'envois à faible volume, vous devez d'abord utiliser l'[outil de prévisualisation](https://developers.google.com/workspace/gmail/promotab/preview) de Gmail pour valider les annotations. Si vous ignorez cette étape, le carrousel de produits et l'aperçu d'image unique ne se déclencheront qu'à des volumes d'envoi plus élevés.

## Mesurer les cartes Gmail {#measure-gmail-cards}

Gmail ne fournit pas d'analyse sur ces cartes, et les fournisseurs de services d'e-mailing (ESP) comme Braze ne peuvent pas insérer leur propre suivi de liens sur les liens de la section d'en-tête (y compris les cartes de promotion et les carrousels de produits). Cependant, vous pouvez ajouter des paramètres UTM ou des codes uniques aux URL lors de la configuration. Ces paramètres vous permettent de suivre l'engagement à l'aide de vos propres outils d'analyse web ou de suivi des conversions, car le suivi fait partie de l'URL elle-même et n'est pas inséré par l'ESP. Le suivi des clics au niveau de l'ESP n'est pas disponible pour ces liens.

### Intégrer des images {#incorporate-images}

Gmail a constaté de meilleurs résultats avec des images percutantes en lien avec le message de l'e-mail. Gmail ne recommande pas d'utiliser un design uniquement textuel, car cet espace a été conçu pour apporter un langage visuel, essentiel au marketing par e-mail, à l'aperçu. N'utilisez pas d'images avec du texte tronqué et ne réutilisez pas les mêmes images dans plusieurs campagnes.

### Décrire les offres {#describe-offers}

Gmail déconseille d'utiliser des phrases complètes, comme « Achetez-en 1, obtenez-en 1 gratuit ou Réductions sur tous les shorts et chemises », car elles risquent d'être tronquées, de ne plus attirer l'attention et de concurrencer la ligne d'objet. Cet espace ne doit être utilisé que pour engager vos clients avec votre message ; évitez donc tout langage similaire à « Ouvrez cet e-mail maintenant » ou « Cliquez ici pour les offres ». Il est préférable de ne pas répéter votre ligne d'objet.

## Bonnes pratiques {#best-practices}

De manière générale, suivez les [bonnes pratiques de l'onglet Promotions de Gmail](https://developers.google.com/gmail/promotab/best-practices).

Lors de la création de votre carte, posez-vous les questions suivantes :

- Le script d'annotation est-il valide ? [Prévisualisez avec Google](https://developers.google.com/workspace/gmail/promotab/preview).
- L'option **Show original** dans Gmail montre-t-elle le script dans le message brut ?
- L'e-mail arrive-t-il dans **Promotions** ? Les cartes ne s'appliquent que dans cet onglet.
- Avez-vous testé sur ordinateur de bureau et sur appareil mobile ?

{% alert tip %}
Bien que Liquid soit pris en charge dans le script, nous recommandons de tester minutieusement pour éviter les erreurs.
{% endalert %}

### Prévisualiser votre annotation {#preview-your-annotation}

Utilisez l'[outil de prévisualisation](https://developers.google.com/workspace/gmail/promotab/preview) pour prévisualiser votre annotation. Notez que l'envoi d'un e-mail de test à vous-même ne fonctionnera pas pour les annotations, car votre annotation ne s'affiche que si l'e-mail est envoyé à un nombre significatif de destinataires. Assurez-vous d'envoyer l'e-mail final (avec ses URL d'images) à au moins 100 destinataires Gmail.

N'utilisez pas Google Workspace pour envoyer des e-mails avec des annotations. Utilisez uniquement des domaines e-mail autorisés pour envoyer des annotations à un grand groupe de destinataires.

### Respecter les directives relatives aux images {#adhere-to-image-guidelines}

Vérifiez que vos images respectent ces directives :
- Utilisez des images de haute qualité et haute résolution.
- Toutes les images annotées doivent utiliser le même rapport hauteur/largeur. Les rapports hauteur/largeur pris en charge sont : 4:5, 1:1, 1.91:1.
- Utilisez des tailles d'image correctes. Le minimum est de 256x256 ; le maximum est de 4096x4096 pixels.

Gmail recommande d'éviter :
- L'utilisation excessive de texte dans vos images
- L'utilisation d'images qui ne sont que des icônes
- L'utilisation d'images avec des masques arrondis
- L'utilisation d'URL d'images personnalisées

### S'enregistrer auprès de DMARC {#register-with-dmarc}

Pour que vos annotations s'affichent correctement, confirmez que les domaines soumis sont enregistrés auprès de DMARC et que toutes les politiques sont activées.

## Foire aux questions {#frequently-asked-questions}

### Comment ajouter un logo d'expéditeur ? {#how-do-i-add-a-sender-logo}

Utilisez les [annotations Google](https://developers.google.com/workspace/gmail/promotab/overview) pour ajouter votre logo et votre carte de promotion dans l'application Gmail. L'affichage est contrôlé par Gmail, pas par Braze.

### Pourquoi mon message promotionnel n'affiche-t-il pas la carte de promotion ou le carrousel de produits dans la boîte de réception de l'utilisateur final ? {#why-is-my-promotional-message-not-displaying-the-promotion-card-or-product-carousel-in-the-end-users-inbox}

De nombreux facteurs déterminent si le carrousel de produits sera affiché dans l'onglet Promotions de Gmail.

Toutes les images de l'annotation doivent passer un filtre de qualité. Pour que le carrousel de produits s'affiche, toutes les images de l'annotation doivent respecter le rapport hauteur/largeur recommandé et être des images de produits en gros plan, de haute qualité et haute résolution. Les images doivent contenir peu ou pas de texte. Le filtre de qualité exclut également le contenu inapproprié : les images doivent donc être adaptées à tous les publics.

De plus, Gmail impose un plafond de densité sur le nombre de carrousels de produits affichés dans l'onglet Promotions d'un utilisateur. Par exemple, si un utilisateur est abonné à de nombreuses marques qui utilisent des carrousels de produits dans leurs e-mails promotionnels, Gmail finit par limiter le nombre de carrousels de produits affichés.

En raison des réglementations de Google en matière de confidentialité et de sécurité, les e-mails avec annotations doivent être envoyés en masse pour que l'annotation fonctionne. Il est recommandé de lancer une campagne et de l'envoyer à au moins 100 destinataires pour que le système de Google la détecte comme un « envoi de masse ». Les URL d'images ne doivent pas varier d'un destinataire à l'autre.

### Comment les clics sur une carte de promotion ou un carrousel de produits sont-ils suivis ? {#how-are-clicks-on-a-promotion-card-or-product-carousel-tracked}

Braze ou tout autre ESP ne peut pas insérer de suivi de liens sur les liens de la section d'en-tête. Cela signifie que les clics ne peuvent pas être suivis sur une carte de promotion ou un carrousel de produits.

### Existe-t-il un moyen de savoir combien d'utilisateurs ont reçu un carrousel de produits ? {#is-there-a-way-to-see-how-many-users-received-a-product-carousel}

Gmail détermine quand et à qui afficher la carte, il n'y a donc aucune garantie que chaque destinataire verra le carrousel de produits.

### Pourquoi ne vois-je pas les annotations dans mon onglet Promotions de Gmail ? {#why-dont-i-see-annotations-in-my-gmail-promotions-tab}

Les annotations ne sont pas prises en charge pour Google Workspace. Pour prévisualiser les annotations, vous pouvez créer une adresse e-mail personnelle avec Gmail.

Notez que les annotations ne s'affichent pas dans l'onglet **Principal** ni dans aucun autre onglet de l'application mobile Gmail. Les annotations ne s'afficheront pas après qu'un utilisateur a ouvert un e-mail ou si vous utilisez le type d'annotation `DiscountOffer` et que la date et l'heure ont déjà expiré.

{% alert tip %}
Pour aller plus loin dans la résolution des problèmes, consultez le [guide de résolution des problèmes de Google pour les promotions par e-mail](https://developers.google.com/workspace/gmail/promotab/troubleshooting).
{% endalert %}