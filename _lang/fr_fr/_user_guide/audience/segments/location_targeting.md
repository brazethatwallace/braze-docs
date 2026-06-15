---
nav_title: Ciblage par localisation
article_title: Ciblage par localisation
page_order: 7
page_type: tutorial
tool:
- Segments
- Location
description: "Cet article pratique vous explique comment configurer le ciblage par localisation, vous permettant de segmenter les utilisateurs par emplacement."

---

# Ciblage par localisation {#location-targeting}

> Cet article vous explique comment configurer le ciblage par localisation, vous permettant de segmenter les utilisateurs en fonction de leur emplacement le plus récent. C'est idéal si vous souhaitez mettre en place des campagnes et des stratégies basées sur la localisation.

## Étape 1 : Créer votre segment {#step-1-create-your-segment}

Accédez à la page **Segments**, sous **Audience**, pour afficher tous vos segments d'utilisateurs actuels. Sur cette page, vous pouvez créer et nommer de nouveaux segments. Pour commencer, sélectionnez **Créer un segment** et donnez un nom à votre segment.

![Fenêtre modale pour créer un segment.]({% image_buster /assets/img_archive/createsegment2.png %}){: style="max-width:70%;"}

## Étape 2 : Personnaliser votre localisation {#step-2-customize-your-location}

Après avoir créé votre segment, ajoutez un filtre **Most Recent Location** pour cibler les utilisateurs en fonction du dernier endroit où ils ont utilisé votre application. Vous avez la possibilité de mettre en évidence les utilisateurs à l'intérieur ou à l'extérieur d'une région circulaire standard ou d'une région polygonale personnalisable.

![Filtre pour un emplacement le plus récent dans un cercle.]({% image_buster /assets/img_archive/filter_recent_location.png %})

{% tabs %}
{% tab Circular %}

### Régions circulaires {#circular-regions}

Pour les régions circulaires, vous pouvez déplacer l'origine et ajuster le rayon de localisation pour votre segmentation.

![Un contour circulaire de villes entre le New Jersey et New York.]({% image_buster /assets/img_archive/location_circle.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Polygonal %}

### Régions polygonales {#polygonal-regions}

Pour les régions polygonales, vous pouvez désigner plus précisément les zones que vous souhaitez inclure dans votre segment.

![Un contour de l'État de New York comme région polygonale sélectionnée.]({% image_buster /assets/img_archive/create_polygon.png %}){: style="max-width:70%;"}

{% endtab %}
{% endtabs %}

## Prise en charge des balises et du géorepérage par les partenaires {#partnership-support-for-beacon-and-geofence}

La combinaison de la prise en charge existante des balises ou du géorepérage avec nos fonctionnalités de ciblage et d'envoi de messages vous fournit davantage d'informations sur les actions physiques de vos utilisateurs, vous permettant ainsi de leur envoyer des messages en conséquence. Vous pouvez tirer parti du suivi de localisation avec certains de nos partenaires :

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion/)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)