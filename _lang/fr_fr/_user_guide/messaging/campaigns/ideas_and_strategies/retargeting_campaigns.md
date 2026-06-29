---
nav_title: Reciblage de campagnes
article_title: Recibler des campagnes
page_order: 2
page_type: reference
description: "Cet article de référence explique comment et pourquoi envisager le reciblage de campagnes en fonction des messages reçus par vos utilisateurs."
tool:
  - Campaigns
  
---

# Recibler des campagnes

> En reciblant des campagnes en fonction des actions précédentes de l'utilisateur, par exemple s'il a ouvert ou non un e-mail, vous pouvez reclassifier vos utilisateurs et ouvrir la voie à une approche de marketing axé sur les données efficace.

Braze prend en charge le reciblage des utilisateurs en fonction des messages qu'ils ont reçus. Vous pouvez recibler les utilisateurs en fonction de leurs interactions avec vos campagnes et vos Canvas. 

Chacun de ces filtres de reciblage vous offre plusieurs options une fois ajoutés. Pour en savoir plus sur le ciblage des utilisateurs, consultez notre [cours d'apprentissage Braze](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sur la configuration des campagnes !

![Section Détails du segment avec le menu déroulant des filtres disponibles.]({% image_buster /assets/img_archive/retarget.png %}){: style="max-width:80%;"}

## Filtres de reciblage

Vous pouvez utiliser les filtres de reciblage de cette section pour vos utilisateurs dans vos campagnes et Canvas.

### A cliqué/ouvert une campagne

Utilisez ce filtre pour trouver les utilisateurs qui ont ou n'ont pas :

- Cliqué sur un e-mail
- Cliqué sur un message in-app
- Ouvert directement une notification push
- Ouvert un e-mail
- Vu un message in-app

![]({% image_buster /assets/img_archive/clickedopened.png %})

Ce filtre peut être affiné en sélectionnant la campagne que vous souhaitez recibler.

### A cliqué ou ouvert une campagne ou un Canvas avec une étiquette

Utilisez ce filtre pour trouver les utilisateurs qui ont ou n'ont pas interagi avec des campagnes ou des Canvas portant une étiquette donnée :

- Cliqué sur un e-mail
- Cliqué sur un message in-app
- Ouvert directement une notification push
- Ouvert un e-mail
- Vu un message in-app

![]({% image_buster /assets/img_archive/retarget_tag_filter.png %})

### A converti à partir d'une campagne

Utilisez ce filtre pour trouver les utilisateurs qui ont ou n'ont pas converti (sur la base de la conversion principale) dans votre campagne cible.

Pour les campagnes récurrentes, ce filtre indique si les utilisateurs ont converti sur le message le plus récent de la campagne.

![]({% image_buster /assets/img_archive/converted_from_campaign.png %})

### A converti à partir d'un Canvas

Utilisez ce filtre pour trouver les utilisateurs qui ont ou n'ont pas converti (sur la base de la conversion principale) dans votre Canvas cible.

Pour les Canvas récurrents, ce filtre indique si les utilisateurs ont converti à un moment quelconque de leur parcours dans le Canvas.

![]({% image_buster /assets/img_archive/converted_from_canvas.png %})

### Dans le groupe de contrôle d'une campagne

Utilisez ce filtre pour trouver les utilisateurs qui font ou ne font pas partie du groupe de contrôle de votre campagne cible.

![]({% image_buster /assets/img_archive/campaign_control_group.png %})

### Dans le groupe de contrôle d'un Canvas

Utilisez ce filtre pour trouver les utilisateurs qui font ou ne font pas partie du groupe de contrôle de votre Canvas cible, que vous pouvez sélectionner dans le menu déroulant.

![]({% image_buster /assets/img_archive/canvas_control_group.png %})

### Dernier message reçu d'une campagne spécifique

Utilisez ce filtre pour trouver les utilisateurs qui ont reçu pour la dernière fois une campagne spécifique avant ou après une date ou un nombre de jours donné. Ce filtre ne tient pas compte du moment où les utilisateurs ont reçu d'autres campagnes.

{% multi_lang_include audience/segments.md section='same channel identifier' %}

![]({% image_buster /assets/img_archive/last_received_specific_campaign.png %})

### Dernier message reçu d'une campagne ou d'un Canvas avec une étiquette

Utilisez ce filtre pour trouver les utilisateurs qui ont reçu pour la dernière fois une campagne ou un Canvas portant une étiquette donnée avant ou après une date ou un nombre de jours donné. Ce filtre ne tient pas compte du moment où les utilisateurs ont reçu d'autres campagnes ou Canvas.

![]({% image_buster /assets/img_archive/last_received_campaign_with_tag.png %})

### A reçu un message d'une campagne

Utilisez ce filtre pour trouver les utilisateurs qui ont ou n'ont pas reçu votre campagne cible.

{% multi_lang_include audience/segments.md section='same channel identifier' %}

![]({% image_buster /assets/img_archive/receivedcamp.png %})

### A reçu un message d'une campagne ou d'un Canvas avec une étiquette

Utilisez ce filtre pour trouver les utilisateurs qui ont ou n'ont pas reçu une campagne ou un Canvas portant votre étiquette cible.

![]({% image_buster /assets/img_archive/received_campaign_with_tag.png %})

## Avantages du reciblage de campagnes

Le reciblage est particulièrement efficace lorsque le segment d'origine inclut également une action spécifique que vous souhaitez voir les utilisateurs effectuer. Par exemple, imaginons que vous ayez une carte ciblant les utilisateurs qui n'ont jamais effectué d'achat. La carte fait la promotion d'un achat in-app à prix réduit. Le segment initial se présente comme suit :

- Argent dépensé dans l'application est exactement 0
- Dernière utilisation de l'application il y a moins de 14 jours

Le nombre total d'utilisateurs dans le segment est de 100 000 et vous savez, grâce aux statistiques des cartes de contenu, que 60 000 utilisateurs uniques ont vu la carte et que 20 000 utilisateurs uniques ont cliqué dessus. Grâce au segmenteur, nous pouvons voir combien de ces utilisateurs ayant cliqué sur la carte ont effectivement réalisé un achat :

- Argent dépensé dans l'application est supérieur à 0
- A cliqué sur la carte est Nom de la carte

Après avoir examiné ces statistiques, nous pouvons créer un segment d'utilisateurs qui ont cliqué sur la carte mais n'ont pas effectué d'achat :

- Argent dépensé dans l'application est exactement 0
- A cliqué sur la carte est Nom de la carte

Nous pouvons recibler ce segment avec des messages supplémentaires autour de la promotion ou d'un autre achat in-app. Le reciblage peut être réalisé à l'aide d'une campagne de communication. Une approche multicanale vous permet d'atteindre les utilisateurs là où ils sont le plus susceptibles de répondre, augmentant ainsi l'efficacité de vos campagnes.