---
nav_title: Types de messages
article_title: Types de messages LINE
page_order: 0
description: "Cet article couvre les différents types de messages LINE."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/message_types/
---

# Types de messages LINE {#line-message-types}

> Cet article couvre les types de messages LINE que vous pouvez rédiger, y compris leurs aspects et limitations.

Lorsque vous rédigez un message LINE, vous pouvez glisser-déposer des types de messages dans l'éditeur, puis les personnaliser.

![Panneau des types de messages avec les types de messages à glisser dans l'éditeur, notamment texte, image, message enrichi et message à base de cartes.]({% image_buster /assets/img/line/line_message_types.png %}){: style="max-width:40%;"}

## Texte {#text}

Un message texte LINE peut contenir jusqu'à 5 000 caractères et inclure des emojis ainsi que de la personnalisation Liquid.

Les cas d'utilisation incluent :
- Annoncer une promotion à durée limitée sur les stocks en liquidation
- Envoyer des vœux d'anniversaire personnalisés avec des cartes de promotion uniques
- Partager des mises à jour rapides sur les événements à venir

![Un message texte rappelant à l'utilisateur de ne pas oublier une soirée Black Friday et la possibilité d'économiser jusqu'à 80 % avant minuit.]({% image_buster /assets/img/line/line_text_message.png %}){: style="max-width:40%;"}

## Image {#image}

Un message image LINE peut être ajouté via la [bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/), une URL ou Liquid. Ces images sont autonomes et ne contiennent pas de liens cliquables.

Les cas d'utilisation incluent :
- Mettre en valeur une destination de vacances pour inciter les utilisateurs à envisager l'achat de billets d'avion
- Mettre en avant des promotions de fin de saison pour encourager les utilisateurs à faire le plein de vêtements d'hiver pour l'année prochaine avec de bonnes affaires
- Lancer un compte à rebours visuel pour une vente annuelle dans tout le magasin

![Un message image faisant la promotion d'une vente de grille-pain.]({% image_buster /assets/img/line/line_image_message.png %}){: style="max-width:40%;"}

### Image par URL {#url-image}

Utilisez les images par URL pour les cas d'utilisation qui intègrent :
- Des images dynamiques Liquid en incluant le Liquid dans votre attribut source d'image. Par exemple, vous pouvez insérer {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} comme URL d'image pour inclure le prénom d'un utilisateur dans l'image
- Du [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) en récupérant des images directement depuis votre serveur web ou des API accessibles publiquement
- Des [catalogues Braze]({{site.baseurl}}/user_guide/data/activation/catalogs/) en accédant aux images depuis des fichiers CSV importés et des endpoints d'API

| **Spécifications** | **Propriétés recommandées** |
|--------------------------|----------------------------|
| Longueur de l'URL du fichier image | 2 000 caractères maximum  |
| Format d'image          | PNG, JPEG             |
| Taille du fichier     |  10&nbsp;Mo maximum |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Image par URL" }

## Messages enrichis (image map) {#rich-messages-image-map}

Un message enrichi LINE est une image contenant un ou plusieurs liens qui s'ouvrent en sélectionnant des zones spécifiques de l'image. Sélectionnez un modèle de message enrichi pour choisir comment les liens sont mappés sur l'image.

Les cas d'utilisation incluent :
- Afficher une grille de sacs à main récemment arrivés avec des liens vers la page produit de chaque sac
- Présenter un menu interactif qui lance une commande combo en sélectionnant un article
- Disposer plusieurs promotions parmi lesquelles les utilisateurs peuvent choisir en sélectionnant une case de la grille

![Un message enrichi à six cases avec une photo d'une grille en noir et blanc que les utilisateurs peuvent toucher pour recevoir une offre aléatoire.]({% image_buster /assets/img/line/line_rich_message.png %})

### Image map {#image-map}

| **Spécifications** | **Propriétés recommandées** |
|--------------------------|----------------------------|
| Longueur de l'URL du fichier image | 2 000 caractères maximum  |
| Format d'image          | PNG (peut être transparent), JPEG             |
| Rapport hauteur/largeur          | 1:1 (largeur:hauteur)
| Taille du fichier     |  10&nbsp;Mo maximum |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Image map" }

### Lien URI {#uri-link}

| **Spécifications** | **Propriétés recommandées** |
|--------------------------|----------------------------|
| Nombre de caractères      | 1 000 maximum |
| Schémas              | HTTP, HTTPS, LINE, tel |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Lien URI" }

### Texte

Un message enrichi textuel peut contenir jusqu'à 400 caractères.

## Message à base de cartes (carrousel) {#card-based-carousel}

Un message à base de cartes LINE permet aux utilisateurs de faire défiler plusieurs messages, comme un carrousel, et d'agir sur les messages les plus pertinents pour eux en sélectionnant une carte ou les boutons d'une carte.

Les cas d'utilisation incluent :
- Afficher des promotions pour des articles de menu spécifiques
- Mettre en avant les vestes les plus vendues de la saison
- Présenter un échantillon d'ustensiles et gadgets de cuisine inclus dans un kit

![Un message à base de cartes avec au moins deux cartes faisant la promotion de sandwichs dans l'éditeur.]({% image_buster /assets/img/line/line_card_message.png %})

### Message {#message}

| **Spécifications** | **Propriétés recommandées** |
|--------------------------|----------------------------|
| Colonnes                  | 10 maximum |
| Rapport hauteur/largeur             | Rectangle : 1.51:1 <br> Carré : 1:1  |
| Titre                    | 40 caractères maximum
{: .reset-td-br-1 .reset-td-br-2 aria-label="Message" }


### Image

| **Spécifications** | **Propriétés recommandées** |
|--------------------------|----------------------------|
| URL de l'image                 | 2 000 caractères maximum |
| Format d'image              | JPEG ou PNG |
| Largeur                     | 1 024 pixels  |
| Taille du fichier                 | 1 Mo |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Image" }


### Texte

| **Spécifications** | **Propriétés recommandées** |
|-------------------------|----------------------------|
| Caractères              | 120 maximum (sans image ni titre) <br> 60 maximum (message avec une image ou un titre)  |
| Actions                 | 3 maximum |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Texte" }