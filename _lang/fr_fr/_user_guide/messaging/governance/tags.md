---
nav_title: Balises
article_title: Balises
page_order: 10
page_type: reference
description: "Cet article de référence couvre les balises pour les campagnes, les Canvas, les segments et les données personnalisées dans le tableau de bord de Braze."
tool:
  - Campaigns
  - Canvas
---

# Balises {#tags}

> Braze suit les informations relatives à l'auteur, à l'éditeur, à la date et au statut des segments, des campagnes et des Canvas, et vous permet de créer des balises pour organiser et trier davantage vos engagements.

## Balises pour les Campaign, Canvas et Segments {#campaign-canvas-and-segment-tags}

Vous pouvez ajouter des balises lors de la création ou de la modification d'une Campaign, d'un Canvas ou d'un Segment. Cliquez sur <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tags** sous le nom de l'engagement et sélectionnez une balise existante, ou commencez à taper pour ajouter une nouvelle balise.

![Ajout de balises lors de la création d'une Campaign.]({% image_buster /assets/img_archive/tags_add_tag.png %}){: style="max-width:60%;" }

{% alert important %}
Vous pouvez ajouter jusqu'à 175 balises à une Campaign, un Canvas ou un Segment.
{% endalert %}

### Balisage en masse {#bulk-tagging}

Vous pouvez également ajouter des balises à plusieurs Campaign, Canvas ou Segments en sélectionnant plusieurs engagements et en cliquant sur <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tag As**.

![Ajout de balises à plusieurs Campaign en même temps.]({% image_buster /assets/img_archive/tags_apply_multiple.gif %})

{% alert important %}
Lorsque vous utilisez le balisage en masse pour appliquer une nouvelle balise à plusieurs Campaign qui possèdent déjà des balises différentes, chaque Campaign sélectionnée reçoit la nouvelle balise, et toutes les balises présentes sur une Campaign sont appliquées à toutes les autres Campaign sélectionnées, même si ces balises ne leur étaient pas initialement associées.
{% endalert %}

### Affichage des balises {#viewing-tags}

Les balises définies sur une Campaign, un Canvas ou un Segment sont visibles sur la page de détails, à proximité du nom de l'engagement. Elles apparaissent également dans l'analyse des Campaign.

![Balises affichées sur la page d'analyse de la Campaign.]({% image_buster /assets/img_archive/tag_details_page.png %}){: style="max-width:60%;" }

### Filtrage par balise {#filtering-by-tag}

Les balises sont visibles dans la liste des Campaign, Canvas ou Segments, ainsi que des balises supplémentaires pour les libellés de statut tels que **Archived** et **Draft**. Pour filtrer par balise, sélectionnez le nom de la balise dans la liste des balises.

![Balises dans la liste des Campaign.]({% image_buster /assets/img_archive/tags_grid.png %})

## Balises de données personnalisées {#custom-data-tags}

Les balises peuvent également être ajoutées aux données personnalisées lors de la gestion des [attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#managing-custom-attributes) et des [événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events#adding-tags).

{% alert important %}
Cette fonctionnalité est actuellement en accès anticipé. Contactez votre gestionnaire du succès des clients si vous souhaitez participer à cet accès anticipé.
{% endalert %}

Pour plus d'informations sur le renommage, la suppression ou l'imbrication des balises dans votre tableau de bord, consultez [Gestion des balises]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags).