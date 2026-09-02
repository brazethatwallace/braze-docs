---
nav_title: Détails créatifs
article_title: Détails créatifs pour les Content Cards
page_order: 2
description: "Cet article présente les détails créatifs tels que les recommandations de taille d'image et le comportement de fermeture pour les trois types standard de Content Cards."
channel:
  - content cards
tool: Media

---

# Détails créatifs pour les Content Cards {#creative-details-for-content-cards}

> La personnalisation des Content Cards et du flux dans lequel elles se trouvent ne peut pas être effectuée lors du processus de création de Campaign : vous devez travailler avec vos ingénieurs et développeurs pour créer et personnaliser vos cartes. Pour les détails techniques, consultez notre [documentation développeur]({{site.baseurl}}/developer_guide/getting_started/customization_overview).

## Types de Content Cards {#content-card-types}

{% tabs %}
{% tab Classique %}

La carte classique est idéale pour les messages et notifications standard, ou même pour catégoriser visuellement les messages à l'aide d'icônes. L'image est facultative, mais elle doit respecter un rapport hauteur/largeur de 1:1.

![Image d'une carte classique avec les détails recommandés et un exemple de carte classique]({% image_buster /assets/img/content_card_classic.png %}){: width="1358" height="2871" style="max-width:45%;border:0;"}

| Fonctionnalité de la carte | Détails |
| --- | ---|
| Texte de l'en-tête | 18 px ; Gras <br> Une seule ligne de texte est idéale. <br> Vous pouvez utiliser Liquid ici pour personnaliser votre message. |
| Texte du message | 13 px ; Poids normal <br> Deux à quatre lignes de texte est idéal. <br> Vous pouvez utiliser Liquid ici pour personnaliser votre message. |
| Texte du lien | Facultatif. <br> 13&nbsp;px <br> Lien vers une page web ou deep link vers l'intérieur de votre application. |
| Image | Facultative. <br> Le rapport doit être de 1:1. <br> Nous recommandons une qualité d'image de 60 x 60&nbsp;px. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Types de Content Cards" }

{% endtab %}
{% tab Image avec légende %}

La carte Image avec légende est un excellent moyen de mettre en valeur et d'attirer l'attention sur du contenu important, comme une grande promotion ou une nouvelle fonctionnalité de l'application.

![Image d'une carte Image avec légende avec les détails recommandés et un exemple de carte Image avec légende]({% image_buster /assets/img/content_card_captioned.png %}){: width="2880" height="2877" style="max-width:90%;border:0;"}

| Fonctionnalité de la carte | Détails |
| --- | ---|
| Texte de l'en-tête | 18 px ; Gras <br> Une seule ligne de texte est idéale. <br> Vous pouvez utiliser Liquid ici pour personnaliser votre message. |
| Texte du message | 13 px ; Poids normal <br> Deux à quatre lignes de texte est idéal. <br> Vous pouvez utiliser Liquid ici pour personnaliser votre message. |
| Texte du lien | Facultatif. <br> 13&nbsp;px <br> Lien vers une page web ou deep link vers l'intérieur de votre application. |
| Image | Rapport 4:3 suggéré. <br> 600&nbsp;px de largeur minimum.  <br> Prend en charge les formats PNG, JPEG et GIF haute résolution. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Types de Content Cards" }

{% endtab %}
{% tab Image uniquement %}

Si vous souhaitez davantage de contrôle créatif, la carte image uniquement est faite pour vous. Créez votre image avec l'outil de votre choix et téléversez-la dans ce type de carte.

![Image d'une Content Card image uniquement avec les détails recommandés et un exemple d'image uniquement]({% image_buster /assets/img/content_card_banner.png %}){: width="1358" height="2871" style="max-width:45%;border:0;"}

| Fonctionnalité de la carte | Détails |
| --- | ---|
| Carte avec lien | Facultatif. <br> 13&nbsp;px <br> Le comportement au clic renvoie vers une page web ou un deep link vers l'intérieur de votre application. |
| Image | Tout rapport hauteur/largeur pris en charge. <br> 600&nbsp;px de largeur minimum.  <br> Prend en charge les formats PNG, JPEG et GIF haute résolution. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Types de Content Cards" }

{% endtab %}
{% endtabs %}

## Détails créatifs généraux {#general}

Les Content Cards prennent en charge le texte et les images, y compris les GIF, de manière native. Actuellement, le style personnalisé des cartes, comme des couleurs de police différentes ou plusieurs images, ne peut pas être configuré dans le tableau de bord. Vous pouvez appliquer un style personnalisé à vos Content Cards et à votre flux lors de l'intégration. Pour plus de détails, consultez [Personnaliser les cartes]({{site.baseurl}}/developer_guide/content_cards/customizing_cards) pour le SDK Braze.

### Comportement de fermeture {#dismissal-behavior}

Pour fermer une carte, l'utilisateur peut soit la faire glisser sur mobile, soit utiliser la fonction `close X`, comme illustré dans la capture d'écran suivante. Le `x` n'apparaît au survol que pour le SDK Web.

![Image montrant les comportements de fermeture par glissement ou par bouton de fermeture pour une carte]({% image_buster /assets/img/dismissal-cc.png %}){: width="1800" height="504"}

Si un utilisateur a fermé toutes ses cartes ou si vous n'avez pas envoyé de nouvelles mises à jour, le flux de l'utilisateur ressemblera généralement à ceci :

![Image d'un flux de Content Cards vide]({% image_buster /assets/img/empty-cc.png %}){: width="832" height="1478" style="max-width:45%"}

{% alert tip %}
Gardez vos Content Cards pertinentes en les configurant pour qu'elles se ferment lorsque l'utilisateur effectue une action pertinente. Par exemple, configurez les Content Cards promotionnelles pour qu'elles se ferment dès que l'utilisateur effectue un achat, afin qu'il ne continue pas à voir une offre pour un produit qu'il a déjà acheté.
{% endalert %}

### Utilisation des GIF dans les Content Cards {#using-gifs-in-content-cards}

| Content Cards pour Android | Content Cards pour iOS | Content Cards pour le Web |
| --- | --- |---|
| Le SDK Android ne prend pas en charge les GIF animés par défaut. Pour savoir comment activer cette prise en charge, consultez [GIF]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs?sdktab=android). | Le SDK Swift ne prend pas en charge les GIF animés par défaut. Pour savoir comment activer cette prise en charge, consultez le [tutoriel de prise en charge des GIF](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support). | La prise en charge des GIF est incluse par défaut dans l'intégration du SDK Web. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Utilisation des GIF dans les Content Cards" }