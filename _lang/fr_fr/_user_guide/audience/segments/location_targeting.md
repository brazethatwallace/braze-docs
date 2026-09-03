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

> Cet article vous explique comment configurer le ciblage par localisation afin de segmenter les utilisateurs en fonction de leur emplacement le plus récent.

## Étape 1 : Créer votre segment {#step-1-create-your-segment}

Accédez à la page **Segments**, sous **Audience**, pour afficher tous vos segments d'utilisateurs actuels. Sur cette page, vous pouvez créer et nommer de nouveaux segments. Pour commencer, sélectionnez **Create Segment** et donnez un nom à votre segment.

![Fenêtre modale pour créer un segment.]({% image_buster /assets/img_archive/createsegment2.png %}){: style="max-width:70%;"}

## Étape 2 : Personnaliser votre emplacement {#step-2-customize-your-location}

Après avoir créé votre Segment, ajoutez un filtre `Most Recent Location` pour mettre en évidence les utilisateurs en fonction du dernier endroit où ils ont utilisé votre application. Vous avez la possibilité de cibler les utilisateurs à l'intérieur ou à l'extérieur d'une région circulaire standard ou d'une région polygonale personnalisable.

![Filtre pour un emplacement le plus récent dans un cercle.]({% image_buster /assets/img_archive/filter_recent_location.png %})

### Utilisateurs sans données de localisation {#users-without-location-data}

Les utilisateurs sans données de localisation — y compris ceux dont la localisation a été précédemment enregistrée puis effacée — correspondent aux filtres `most recent location outside of circle` et `most recent location outside of polygon`. Pour exclure les utilisateurs sans données de localisation, combinez le filtre `Most Recent Location` avec un filtre `Location Available`.

{% tabs %}
{% tab Circulaire %}

### Régions circulaires {#circular-regions}

Pour les régions circulaires, vous pouvez déplacer l'origine et ajuster le rayon de localisation pour votre segmentation.

![Un contour circulaire de villes entre le New Jersey et New York.]({% image_buster /assets/img_archive/location_circle.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Polygonale %}

### Régions polygonales {#polygonal-regions}

Pour les régions polygonales, vous pouvez désigner plus précisément les zones que vous souhaitez inclure dans votre Segment.

![Un contour de l'État de New York comme région polygonale sélectionnée.]({% image_buster /assets/img_archive/create_polygon.png %}){: style="max-width:70%;"}

{% endtab %}
{% endtabs %}

## Prise en charge des balises et du géorepérage par les partenaires {#partnership-support-for-beacon-and-geofence}

En combinant la prise en charge existante des balises ou du géorepérage avec nos fonctionnalités de ciblage et de communication, vous obtenez davantage d'informations sur les actions physiques de vos utilisateurs et pouvez leur envoyer des messages en conséquence. Vous pouvez tirer parti du suivi de localisation avec certains de nos partenaires :

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare)