---
nav_title: Tags
article_title: Tags
page_order: 10
page_type: reference
description: "Dieser Referenzartikel behandelt Tags für Campaigns, Canvases, Segments und angepasste Daten im Braze-Dashboard."
tool:
  - Campaigns
  - Canvas
---

# Tags {#tags}

> Braze erfasst Informationen zu Autor:in, Bearbeiter:in, Datum und Status von Segments, Campaigns und Canvases und bietet Ihnen die Möglichkeit, Tags zu erstellen, um Ihre Engagements weiter zu organisieren und zu sortieren.

## Tags für Campaigns, Canvases und Segments {#campaign-canvas-and-segment-tags}

Sie können Tags hinzufügen, wenn Sie eine Campaign, ein Canvas oder ein Segment erstellen oder bearbeiten. Klicken Sie unter dem Engagement-Namen auf <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tags** und wählen Sie ein vorhandenes Tag aus, oder beginnen Sie zu tippen, um ein neues Tag hinzuzufügen.

![Hinzufügen von Tags bei der Erstellung einer Campaign.]({% image_buster /assets/img_archive/tags_add_tag.png %}){: style="max-width:60%;" }

{% alert important %}
Sie können bis zu 175 Tags zu einer Campaign, einem Canvas oder einem Segment hinzufügen.
{% endalert %}

### Massen-Tagging {#bulk-tagging}

Sie können auch Tags zu mehreren Campaigns, Canvases oder Segments hinzufügen, indem Sie mehrere Engagements auswählen und <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tag As** auswählen.

![Gleichzeitiges Hinzufügen von Tags zu mehreren Campaigns.]({% image_buster /assets/img_archive/tags_apply_multiple.gif %})

{% alert important %}
Wenn Sie Massen-Tagging verwenden, um ein neues Tag auf mehrere Campaigns anzuwenden, die bereits unterschiedliche Tags haben, erhält jede ausgewählte Campaign das neue Tag, und alle Tags, die bei einer Campaign vorhanden sind, werden auf alle anderen ausgewählten Campaigns angewendet – auch wenn diese Tags ursprünglich nicht mit ihnen verknüpft waren.
{% endalert %}

### Tags anzeigen {#viewing-tags}

Die Tags, die für eine Campaign, ein Canvas oder ein Segment festgelegt wurden, sind auf der Detailseite in der Nähe des Engagement-Namens sichtbar. Sie erscheinen auch in den Campaign-Analytics.

![Tags auf der Seite „Campaign Analytics“.]({% image_buster /assets/img_archive/tag_details_page.png %}){: style="max-width:60%;" }

### Nach Tag filtern {#filtering-by-tag}

Tags sind in der Liste der Campaigns, Canvases oder Segments sichtbar, zusammen mit zusätzlichen Tags für Statusbezeichnungen wie **Archived** und **Draft**. Um nach einem Tag zu filtern, wählen Sie den Tag-Namen aus der Liste der Tags aus.

![Tags in der Liste der Campaigns.]({% image_buster /assets/img_archive/tags_grid.png %})

## Tags für angepasste Daten {#custom-data-tags}

Tags können auch zu angepassten Daten hinzugefügt werden, wenn Sie [angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#managing-custom-attributes) und [angepasste Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events#adding-tags) verwalten.

{% alert important %}
Dieses Feature befindet sich derzeit im Early Access. Wenden Sie sich an Ihren CSM, wenn Sie an diesem Early Access teilnehmen möchten.
{% endalert %}

Informationen zum Umbenennen, Entfernen oder Verschachteln von Tags in Ihrem Dashboard finden Sie unter [Tags verwalten]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags).